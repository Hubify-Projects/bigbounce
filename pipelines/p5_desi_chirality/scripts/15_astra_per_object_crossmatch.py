#!/usr/bin/env python3
"""ASTRA-DESI EDR per-object cross-validation for P5.

Loads ASTRA-DESI EDR per-galaxy classification probabilities (Zapata-Zuluaga
et al. 2026, arXiv:2604.01456; Zenodo 10.5281/zenodo.19358024), cross-matches
by TARGETID against the P5 matched chirality x DESI catalog, and computes
chirality-by-environment statistics under two ASTRA classifiers:
  (a) ASTRA argmax: env_class = argmax over {void, sheet, filament, knot}.
  (b) ASTRA entropy-weighted: probability-weighted fractional contribution to
      each class (each galaxy contributes P_class to each class's count).

Output: results/astra_per_object/summary.json + cw_fraction_by_env_astra.csv

The result is the first per-object cross-validation of the V-Web canonical
classifier against an external published DESI environmental catalog, in the
ASTRA EDR rosette overlap region (~657k ASTRA galaxies; ~75k intersect P5).

The mapping ASTRA -> V-Web class:
  PVOID -> void
  PSHEET -> wall   (ASTRA "sheet" is V-Web "wall"; both are 1-eigenvalue class)
  PFILAMENT -> filament
  PKNOT -> cluster (ASTRA "knot" is V-Web "cluster"; both are 3-eigenvalue class)
"""
from __future__ import annotations

import glob
import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow.parquet as pq
from astropy.io import fits

REPO_ROOT = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
P5_ROOT = REPO_ROOT / "pipelines/p5_desi_chirality"
ASTRA_PROBS_DIR = P5_ROOT / "data/desi_env/astra_edr/probabilities"
P5_MATCHED = P5_ROOT / "results/p5_matched_chirality_desi.parquet"
VWEB_ENV = P5_ROOT / "data/desi_env/desi_env_vweb.parquet"
OUT_DIR = P5_ROOT / "results/analysis_astra_per_object"

ASTRA_TO_VWEB = {
    "PVOID": "void",
    "PSHEET": "wall",
    "PFILAMENT": "filament",
    "PKNOT": "cluster",
}
ENV_CLASSES = ["void", "wall", "filament", "cluster"]


def load_astra() -> pd.DataFrame:
    rows = []
    for f in sorted(glob.glob(str(ASTRA_PROBS_DIR / "zone_*_probability.fits.gz"))):
        with fits.open(f) as h:
            d = h[1].data
            rows.append(pd.DataFrame({
                "TARGETID": d["TARGETID"].astype(np.int64),
                "TRACERTYPE": np.asarray(d["TRACERTYPE"]).astype(str),
                "PVOID": d["PVOID"].astype(np.float32),
                "PSHEET": d["PSHEET"].astype(np.float32),
                "PFILAMENT": d["PFILAMENT"].astype(np.float32),
                "PKNOT": d["PKNOT"].astype(np.float32),
            }))
    df = pd.concat(rows, ignore_index=True)
    # cross-zone duplicates: average probabilities per TARGETID
    df = df.groupby("TARGETID", as_index=False).agg({
        "TRACERTYPE": "first",
        "PVOID": "mean",
        "PSHEET": "mean",
        "PFILAMENT": "mean",
        "PKNOT": "mean",
    })
    # renormalize (averaging may break sum=1)
    s = df[["PVOID", "PSHEET", "PFILAMENT", "PKNOT"]].sum(axis=1)
    for c in ["PVOID", "PSHEET", "PFILAMENT", "PKNOT"]:
        df[c] = df[c] / s
    return df


def load_p5_spirals() -> pd.DataFrame:
    df = pq.read_table(
        str(P5_MATCHED),
        columns=["desi_targetid", "match_class_eq", "matched_primary_deduped"],
    ).to_pandas()
    df = df[df["matched_primary_deduped"]]
    df = df[df["match_class_eq"].isin(["CW", "CCW"])].copy()
    df["TARGETID"] = df["desi_targetid"].astype(np.int64)
    return df[["TARGETID", "match_class_eq"]]


def load_vweb() -> pd.DataFrame:
    df = pq.read_table(str(VWEB_ENV), columns=["TARGETID", "env_class"]).to_pandas()
    df["TARGETID"] = df["TARGETID"].astype(np.int64)
    df["env_class"] = df["env_class"].astype(str)
    # zall has ~3.57% duplicate TARGETIDs (re-observed galaxies); collapse to first.
    df = df.drop_duplicates(subset="TARGETID", keep="first").reset_index(drop=True)
    return df


def per_class_stats(sub: pd.DataFrame, class_col: str) -> list[dict]:
    rows = []
    for cls in ENV_CLASSES:
        sel = sub[class_col] == cls
        n = int(sel.sum())
        if n == 0:
            rows.append({"env_class": cls, "n": 0, "n_cw": 0, "cw_fraction": float("nan"), "sigma_from_half": float("nan")})
            continue
        n_cw = int((sel & (sub["match_class_eq"] == "CW")).sum())
        f = n_cw / n
        sigma = (n_cw - 0.5 * n) / (0.5 * np.sqrt(n))
        rows.append({"env_class": cls, "n": n, "n_cw": n_cw, "cw_fraction": float(f), "sigma_from_half": float(sigma)})
    return rows


def weighted_stats(sub: pd.DataFrame) -> list[dict]:
    """Each galaxy contributes P_class fractional count and P_class * (CW==1) fractional CW.
    Effective n_eff = sum(P_class) and effective n_cw = sum(P_class * isCW).
    Sigma uses n_eff with Var = sum(P_class * (1 - P_class)) under independent-galaxy approximation."""
    is_cw = (sub["match_class_eq"] == "CW").astype(np.float32).values
    rows = []
    for cls, p_col in [(c, p) for p, c in ASTRA_TO_VWEB.items()]:
        p = sub[p_col].values
        n_eff = float(p.sum())
        n_cw_eff = float((p * is_cw).sum())
        f = n_cw_eff / n_eff if n_eff > 0 else float("nan")
        # variance of sum_i p_i * X_i with X_i Bernoulli(0.5) under null = sum p_i^2 * 0.25
        var = float(0.25 * (p ** 2).sum())
        sigma = (n_cw_eff - 0.5 * n_eff) / np.sqrt(var) if var > 0 else float("nan")
        rows.append({"env_class": cls, "n_eff": n_eff, "n_cw_eff": n_cw_eff, "cw_fraction": float(f), "sigma_from_half": float(sigma)})
    return rows


def main() -> int:
    t0 = time.time()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"[{time.time()-t0:6.1f}s] Loading ASTRA probabilities ...", flush=True)
    astra = load_astra()
    print(f"  ASTRA unique TARGETIDs: {len(astra):,}")

    print(f"[{time.time()-t0:6.1f}s] Loading P5 deduped-primary spirals ...", flush=True)
    p5 = load_p5_spirals()
    print(f"  P5 spirals (CW+CCW, deduped primary): {len(p5):,}")

    print(f"[{time.time()-t0:6.1f}s] Loading V-Web env labels ...", flush=True)
    vweb = load_vweb()
    print(f"  V-Web rows: {len(vweb):,}")

    print(f"[{time.time()-t0:6.1f}s] Joining ...", flush=True)
    j = p5.merge(astra, on="TARGETID", how="inner")
    print(f"  P5 x ASTRA spirals: {len(j):,}")
    j = j.merge(vweb, on="TARGETID", how="inner")
    print(f"  P5 x ASTRA x V-Web (all three labels): {len(j):,}")

    # ASTRA argmax classifier
    prob_cols = ["PVOID", "PSHEET", "PFILAMENT", "PKNOT"]
    argmax_idx = j[prob_cols].values.argmax(axis=1)
    j["astra_argmax_class"] = [ASTRA_TO_VWEB[prob_cols[i]] for i in argmax_idx]

    print(f"[{time.time()-t0:6.1f}s] Computing per-class statistics ...", flush=True)
    astra_argmax_rows = per_class_stats(j, "astra_argmax_class")
    vweb_rows = per_class_stats(j, "env_class")
    astra_weighted_rows = weighted_stats(j)

    # Class-by-class agreement: confusion matrix V-Web vs ASTRA argmax
    confusion = pd.crosstab(j["env_class"], j["astra_argmax_class"]).reindex(
        index=ENV_CLASSES, columns=ENV_CLASSES, fill_value=0
    )

    # Headline: cw_fraction range across env classes (require n>=100 to suppress
    # small-sample artifacts; V-Web puts ~3 spirals in void/wall on this overlap)
    N_MIN_HEADLINE = 100

    def _range(rows, key="cw_fraction", n_key="n"):
        vals = [r[key] for r in rows if r.get(n_key, 0) >= N_MIN_HEADLINE and not np.isnan(r[key])]
        if not vals:
            return float("nan")
        return float(max(vals) - min(vals))

    astra_argmax_range = _range(astra_argmax_rows)
    vweb_range = _range(vweb_rows)
    astra_weighted_range = _range(astra_weighted_rows, n_key="n_eff")

    # Headline: max |sigma_from_half| across env classes for each classifier
    def _max_sig(rows, n_key="n"):
        sigs = [abs(r["sigma_from_half"]) for r in rows if r.get(n_key, 0) >= N_MIN_HEADLINE and not np.isnan(r["sigma_from_half"])]
        return float(max(sigs)) if sigs else float("nan")

    summary = {
        "written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "data": {
            "astra_galaxies_total": int(len(astra)),
            "p5_spirals_total": int(len(p5)),
            "vweb_rows_total": int(len(vweb)),
            "overlap_p5_x_astra": int(len(j)),
        },
        "classifiers": {
            "astra_argmax": {
                "per_class": astra_argmax_rows,
                "cw_fraction_range_pp": astra_argmax_range * 100 if not np.isnan(astra_argmax_range) else None,
                "max_abs_sigma_from_half": _max_sig(astra_argmax_rows),
            },
            "astra_entropy_weighted": {
                "per_class": astra_weighted_rows,
                "cw_fraction_range_pp": astra_weighted_range * 100 if not np.isnan(astra_weighted_range) else None,
                "max_abs_sigma_from_half": _max_sig(astra_weighted_rows, n_key="n_eff"),
            },
            "vweb_on_same_overlap": {
                "per_class": vweb_rows,
                "cw_fraction_range_pp": vweb_range * 100 if not np.isnan(vweb_range) else None,
                "max_abs_sigma_from_half": _max_sig(vweb_rows),
            },
        },
        "confusion_matrix_vweb_vs_astra_argmax": confusion.to_dict(),
        "provenance": {
            "astra_source": "arXiv:2604.01456 / Zenodo 10.5281/zenodo.19358024",
            "astra_files": str(ASTRA_PROBS_DIR),
            "p5_matched_catalog": str(P5_MATCHED),
            "vweb_env": str(VWEB_ENV),
            "class_mapping": ASTRA_TO_VWEB,
        },
    }

    out_json = OUT_DIR / "summary.json"
    with out_json.open("w") as fh:
        json.dump(summary, fh, indent=2)
    print(f"[{time.time()-t0:6.1f}s] Wrote {out_json}", flush=True)

    # Also write CSV form for paper table
    out_csv = OUT_DIR / "cw_fraction_by_env_astra.csv"
    csv_rows = []
    for r in astra_argmax_rows:
        csv_rows.append({"classifier": "astra_argmax", **r})
    for r in astra_weighted_rows:
        csv_rows.append({"classifier": "astra_entropy_weighted", **{k: v for k, v in r.items()}})
    for r in vweb_rows:
        csv_rows.append({"classifier": "vweb_on_same_overlap", **r})
    pd.DataFrame(csv_rows).to_csv(out_csv, index=False)
    print(f"[{time.time()-t0:6.1f}s] Wrote {out_csv}", flush=True)

    print(f"[{time.time()-t0:6.1f}s] DONE.", flush=True)
    print()
    print("HEADLINE:")
    print(f"  Overlap (V-Web x ASTRA x P5 spirals): {len(j):,}")
    print(f"  cw_fraction range across env classes (pp):")
    print(f"    V-Web on same overlap: {summary['classifiers']['vweb_on_same_overlap']['cw_fraction_range_pp']:.3f}")
    print(f"    ASTRA argmax:           {summary['classifiers']['astra_argmax']['cw_fraction_range_pp']:.3f}")
    print(f"    ASTRA entropy-weighted: {summary['classifiers']['astra_entropy_weighted']['cw_fraction_range_pp']:.3f}")
    print(f"  Max |sigma_from_half| across env classes:")
    print(f"    V-Web on same overlap: {summary['classifiers']['vweb_on_same_overlap']['max_abs_sigma_from_half']:.3f}")
    print(f"    ASTRA argmax:           {summary['classifiers']['astra_argmax']['max_abs_sigma_from_half']:.3f}")
    print(f"    ASTRA entropy-weighted: {summary['classifiers']['astra_entropy_weighted']['max_abs_sigma_from_half']:.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
