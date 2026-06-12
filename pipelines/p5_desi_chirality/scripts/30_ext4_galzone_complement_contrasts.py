#!/usr/bin/env python3
"""EXT4 closure NM-B — GALZONE catalog-native non-void complement contrasts.

Closes the truth-audit NM-B finding (EXT4_P5_TRUTH_AUDIT.md):
the Bonferroni-5 primary family declared the two-sample Δf_CW contrast as the
primary estimand, but Table II rows 4–5 (GALZONE catalog-native V2-REVOLVER and
V2-VIDE) tabulate only the one-sample void f_CW. This script computes the
non-void complement (GALZONE-joined rows that FAIL the catalog-native void cut
OUT=0 ∧ ZONE≥0 ∧ VOID0≥0) and emits true two-sample Δf_CW / SE / z / p / 95% CI
using the same sign convention and binomial-SE formulae as
tab:desivast_three_algo (the sphere-PIS three-algo contrast table).

Sign convention (matches Table tab:desivast_three_algo):
    Δf_CW ≡ f_CW^{non-void} − f_CW^{void}

Variance: independent-binomial,  SE(Δ) = sqrt( p_v(1−p_v)/n_v + p_nv(1−p_nv)/n_nv ).
z_Δ = Δf_CW / SE(Δ); p two-sided normal; 95% CI = Δ ± 1.95996 · SE.

Output: pipelines/p5_desi_chirality/outputs/30_ext4_galzone_complement_contrasts.json
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

P5 = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P5 / "env_finder"))

MATCHED = P5 / "results/p5_matched_chirality_desi.parquet"
DESIVAST_DIR = P5 / "data/desivast"
OUT = P5 / "outputs/30_ext4_galzone_complement_contrasts.json"

Z_DESIVAST_MAX = 0.24
Z_CRIT_95 = 1.959963984540054  # two-sided 95% normal critical value


def _sig(n_cw: int, n: int) -> float:
    return float((n_cw - 0.5 * n) / (0.5 * np.sqrt(n))) if n else float("nan")


def _cls_row(sub: pd.DataFrame) -> dict:
    n = int(len(sub))
    n_cw = int((sub["match_class_eq"] == "CW").sum())
    return {
        "n": n,
        "n_cw": n_cw,
        "cw_fraction": (n_cw / n) if n else None,
        "sigma_from_half": _sig(n_cw, n),
    }


def _two_sample_contrast(void: dict, nonvoid: dict) -> dict:
    p_v = void["cw_fraction"]
    p_nv = nonvoid["cw_fraction"]
    n_v = void["n"]
    n_nv = nonvoid["n"]
    delta = p_nv - p_v
    se = float(np.sqrt(p_v * (1 - p_v) / n_v + p_nv * (1 - p_nv) / n_nv))
    z = delta / se if se > 0 else float("nan")
    # two-sided normal p
    from math import erf, sqrt
    p_two = 2.0 * (1.0 - 0.5 * (1.0 + erf(abs(z) / sqrt(2.0))))
    ci_lo = delta - Z_CRIT_95 * se
    ci_hi = delta + Z_CRIT_95 * se
    return {
        "delta_f_cw_nonvoid_minus_void": float(delta),
        "SE_delta": float(se),
        "z_delta": float(z),
        "p_two_sided": float(p_two),
        "ci95_lo": float(ci_lo),
        "ci95_hi": float(ci_hi),
    }


def load_spirals() -> pd.DataFrame:
    cols = ["desi_targetid", "match_class_eq", "desi_z",
            "matched_primary_deduped"]
    m = pd.read_parquet(MATCHED, columns=cols)
    sp = m[m["matched_primary_deduped"]
           & m["match_class_eq"].isin(["CW", "CCW"])].copy()
    return sp.reset_index(drop=True)


def per_algo(sp: pd.DataFrame, algo: str) -> dict:
    from astropy.io import fits

    lz = sp[sp["desi_z"] <= Z_DESIVAST_MAX][
        ["desi_targetid", "match_class_eq"]]
    gzs, zvs = [], []
    zone_offset = 0
    for gc in ["NGC", "SGC"]:
        with fits.open(
                DESIVAST_DIR / f"DESIVAST_BGS_VOLLIM_{algo}_{gc}.fits") as fh:
            gz = fh["GALZONE"].data
            zv = fh["ZONEVOID"].data
            gd = pd.DataFrame({
                "TARGET": np.asarray(gz["TARGET"], dtype=np.int64),
                "ZONE": np.asarray(gz["ZONE"], dtype=np.int64),
                "OUT": np.asarray(gz["OUT"], dtype=np.int64),
            })
            zd = pd.DataFrame({
                "ZONE": np.asarray(zv["ZONE"], dtype=np.int64),
                "VOID0": np.asarray(zv["VOID0"], dtype=np.int64),
            })
            gd.loc[gd["ZONE"] >= 0, "ZONE"] += zone_offset
            zd["ZONE"] += zone_offset
            zone_offset += int(zd["ZONE"].max()) + 1
            gzs.append(gd)
            zvs.append(zd)
    gal = pd.concat(gzs, ignore_index=True)
    zone = pd.concat(zvs, ignore_index=True)
    gal = gal.merge(zone, on="ZONE", how="left")
    gal["VOID0"] = gal["VOID0"].fillna(-1).astype(np.int64)
    j = lz.merge(gal, left_on="desi_targetid", right_on="TARGET", how="inner")

    base_void = (j["OUT"] == 0) & (j["ZONE"] >= 0) & (j["VOID0"] >= 0)
    void_rows = _cls_row(j[base_void])
    nonvoid_rows = _cls_row(j[~base_void])
    contrast = _two_sample_contrast(void_rows, nonvoid_rows)
    return {
        "n_joined_galzone_rows": int(len(j)),
        "void_catalog_native": void_rows,
        "nonvoid_complement": nonvoid_rows,
        "contrast": contrast,
        "definitions": {
            "void_cut": "OUT==0 AND ZONE>=0 AND VOID0>=0 (catalog-native)",
            "nonvoid_complement": "GALZONE-joined rows that FAIL the void cut",
            "sign_convention": "Delta f_CW = f_CW^{non-void} - f_CW^{void}",
            "SE_formula": "sqrt(p_v(1-p_v)/n_v + p_nv(1-p_nv)/n_nv)",
            "z_crit_95": Z_CRIT_95,
        },
    }


def main() -> None:
    t0 = time.time()
    print(f"[{time.time()-t0:6.1f}s] loading spirals ...", flush=True)
    sp = load_spirals()
    print(f"[{time.time()-t0:6.1f}s] spirals: {len(sp):,}", flush=True)

    out = {
        "written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "script": "scripts/30_ext4_galzone_complement_contrasts.py",
        "closes": ["EXT4-NM-B (Bonferroni-5 GALZONE one-sample/two-sample mismatch)"],
        "audit_reference": "project-context/peer-reviews/EXT4_P5_TRUTH_AUDIT.md",
        "matched_spirals_z_leq_0p24": int(
            (sp["desi_z"] <= Z_DESIVAST_MAX).sum()),
        "by_algorithm": {},
    }
    for algo in ["V2_REVOLVER", "V2_VIDE"]:
        print(f"[{time.time()-t0:6.1f}s] {algo} ...", flush=True)
        out["by_algorithm"][algo] = per_algo(sp, algo)
        r = out["by_algorithm"][algo]
        c = r["contrast"]
        print(
            f"[{time.time()-t0:6.1f}s]   n_void={r['void_catalog_native']['n']} "
            f"n_nonvoid={r['nonvoid_complement']['n']} "
            f"Δ={c['delta_f_cw_nonvoid_minus_void']:+.4f} "
            f"SE={c['SE_delta']:.4f} z={c['z_delta']:+.3f} "
            f"p={c['p_two_sided']:.3f}", flush=True)

    out["runtime_seconds"] = round(time.time() - t0, 2)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2))
    print(f"[{time.time()-t0:6.1f}s] wrote {OUT}", flush=True)


if __name__ == "__main__":
    main()
