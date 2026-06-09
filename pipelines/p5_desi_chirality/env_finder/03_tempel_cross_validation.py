#!/usr/bin/env python3
"""P5 env_finder — Tempel+2014/2018 FoF group-catalog cross-validation.

Independent cosmic-web classification cross-check. Tempel et al. 2014
(A&A 566 A1, arXiv:1402.1350) and the 2018 update use a friends-of-friends
group finder on SDSS spectroscopic galaxies. The labels they produce are
not identical to V-Web {void, wall, filament, cluster} — Tempel
categorizes galaxies into groups by FoF linking length, then assigns
each group a richness; environment for a galaxy is "in a group of
multiplicity N" (cluster-like at N>=20, isolated at N==1).

To compare directly with V-Web we map the Tempel multiplicity to a
4-class scheme:
    multiplicity == 1         -> isolated     (~ V-Web void/wall)
    2 <= multiplicity < 5     -> small_group  (~ V-Web wall)
    5 <= multiplicity < 20    -> filament_like
    multiplicity >= 20        -> cluster_like

The script joins the Tempel catalog to the P5 matched chirality catalog
on the spectro-galaxy crossmatch (RA/Dec within 1''), computes CW
fraction per Tempel class, and writes a side-by-side comparison with
the V-Web cosmic-web classification.

STUB STATUS (cron fire #3, 2026-05-21): the Tempel catalog has not yet
been ingested into pipelines/p5_desi_chirality/data/desi_env/tempel/.
The Tempel 2014 SDSS DR10 catalog is publicly available at
http://cosmodb.to.ee/tempel-2014-FoF/ and the 2018 update on the A&A
supplementary materials page. This stub:

    1. Documents the join contract (input schema + output schema).
    2. Implements the Tempel-class -> 4-bin mapping.
    3. Will execute end-to-end once the Tempel catalog parquet lands at
       the canonical path below.

Expected input parquet schema
-----------------------------
    pipelines/p5_desi_chirality/data/desi_env/tempel/tempel_2014_fof.parquet
        ra            float64    decimal deg
        dec           float64    decimal deg
        z             float64
        group_id      int64
        multiplicity  int64

Output
------
    pipelines/p5_desi_chirality/env_finder/reports/03_tempel_cross_validation.json
    pipelines/p5_desi_chirality/results/analysis_cosmic_web/cw_fraction_by_env__tempel_fof.csv

Cross-validation summary statistic
----------------------------------
- For each Tempel class, report n, n_cw, f_cw, sigma_from_half.
- Per-class delta vs the V-Web class with the same expected sample size
  (multiplicity==1 vs V-Web void; 2..5 vs wall; 5..20 vs filament;
  >=20 vs cluster).
- Concordance metric: cw_fraction_delta = |f_cw_Tempel - f_cw_V-Web| per
  class. Spec: concordance < 0.002 (i.e. < 0.2 percentage points) is
  expected if both classifiers see the same underlying chirality field.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
P5 = REPO / "pipelines/p5_desi_chirality"
TEMPEL_PATH = P5 / "data/desi_env/tempel/tempel_2014_fof.parquet"
MATCHED_PATH = P5 / "results/p5_matched_chirality_desi.parquet"
OUT_JSON = P5 / "env_finder/reports/03_tempel_cross_validation.json"
OUT_CSV = P5 / "results/analysis_cosmic_web/cw_fraction_by_env__tempel_fof.csv"
V_WEB_CSV = P5 / "results/analysis_cosmic_web/cw_fraction_by_env__desi_env_vweb.csv"

TEMPEL_CLASS_BINS = [
    ("isolated", 1, 2),       # multiplicity == 1
    ("small_group", 2, 5),    # 2 <= m < 5
    ("filament_like", 5, 20), # 5 <= m < 20
    ("cluster_like", 20, 10**9),  # m >= 20
]


def _utc() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def _classify_multiplicity(mult: int) -> str:
    for name, lo, hi in TEMPEL_CLASS_BINS:
        if lo <= mult < hi:
            return name
    return "unknown"


def _summarize_class(df: pd.DataFrame, class_col: str = "tempel_class") -> pd.DataFrame:
    rows = []
    sp = df[df["match_class_eq"].isin(["CW", "CCW"])]
    for cls, sub in sp.groupby(class_col):
        n = len(sub)
        n_cw = int((sub["match_class_eq"] == "CW").sum())
        f_cw = n_cw / n if n else np.nan
        sigma = (n_cw - 0.5 * n) / (0.5 * np.sqrt(n)) if n > 0 else np.nan
        rows.append({
            "tempel_class": str(cls),
            "n": int(n),
            "n_cw": n_cw,
            "n_ccw": int(n - n_cw),
            "cw_fraction": float(f_cw) if n else None,
            "sigma_from_half": float(sigma) if n > 0 else None,
        })
    return pd.DataFrame(rows)


def _vweb_concordance(tempel_df: pd.DataFrame,
                      overlap_df: pd.DataFrame | None = None) -> dict:
    """Like-for-like concordance: V-Web side restricted to the SAME Tempel-
    overlap galaxies (R22prov OAI-E3 closure). Falls back to the canonical
    full-sample CSV only if the overlap frame is not supplied."""
    pairings = [
        ("isolated", "void"),
        ("small_group", "wall"),
        ("filament_like", "filament"),
        ("cluster_like", "cluster"),
    ]
    out = {}
    if overlap_df is not None:
        env_path = P5 / "data/desi_env/desi_env_vweb.parquet"
        env = pd.read_parquet(env_path, columns=["TARGETID", "env_class"])
        env = env.drop_duplicates("TARGETID")
        ov = overlap_df.merge(env, left_on="desi_targetid",
                              right_on="TARGETID", how="left")
        out["basis"] = "vweb_restricted_to_tempel_overlap"
        for t_cls, v_cls in pairings:
            t_sub = ov[ov["tempel_class"] == t_cls]
            v_sub = ov[ov["env_class"] == v_cls]
            if len(t_sub) == 0 or len(v_sub) == 0:
                out[f"{t_cls}_vs_{v_cls}"] = {"concordance_pp": None, "ok": False}
                continue
            f_t = float((t_sub["match_class_eq"] == "CW").mean())
            f_v = float((v_sub["match_class_eq"] == "CW").mean())
            delta = abs(f_t - f_v)
            out[f"{t_cls}_vs_{v_cls}"] = {
                "concordance_pp": round(delta * 100, 4),
                "ok": delta < 0.002,
                "tempel_f_cw": f_t, "tempel_n": int(len(t_sub)),
                "vweb_f_cw_on_overlap": f_v, "vweb_n_on_overlap": int(len(v_sub)),
            }
        return out
    if not V_WEB_CSV.exists():
        return {"skipped": True, "reason": "V-Web canonical CSV not on disk"}
    vweb = pd.read_csv(V_WEB_CSV)
    out["basis"] = "vweb_full_sample_csv (NOT like-for-like; legacy)"
    for t_cls, v_cls in pairings:
        t_row = tempel_df[tempel_df["tempel_class"] == t_cls]
        v_row = vweb[vweb["env_class"] == v_cls]
        if len(t_row) == 0 or len(v_row) == 0:
            out[f"{t_cls}_vs_{v_cls}"] = {"concordance_pp": None, "ok": False}
            continue
        delta = abs(float(t_row.iloc[0]["cw_fraction"]) - float(v_row.iloc[0]["cw_fraction"]))
        out[f"{t_cls}_vs_{v_cls}"] = {
            "concordance_pp": round(delta * 100, 4),
            "ok": delta < 0.002,
            "tempel_f_cw": float(t_row.iloc[0]["cw_fraction"]),
            "vweb_f_cw": float(v_row.iloc[0]["cw_fraction"]),
        }
    return out


def main() -> int:
    if not TEMPEL_PATH.exists():
        # STUB MODE: write a status JSON marking what is pending.
        OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
        stub = {
            "status": "PENDING_TEMPEL_INGEST",
            "expected_input": str(TEMPEL_PATH.relative_to(REPO)),
            "expected_schema": {
                "ra": "float64",
                "dec": "float64",
                "z": "float64",
                "group_id": "int64",
                "multiplicity": "int64",
            },
            "source": "Tempel+2014 A&A 566 A1 arXiv:1402.1350; cosmodb.to.ee/tempel-2014-FoF/",
            "tempel_class_bins": [
                {"name": name, "multiplicity_min": lo, "multiplicity_max": hi}
                for name, lo, hi in TEMPEL_CLASS_BINS
            ],
            "join_contract": {
                "on": "celestial-sphere nearest-neighbour within 1'' (astropy SkyCoord.match_to_catalog_sky)",
                "primary_key_for_chirality_side": "desi_targetid (de-duplicated nearest-sep winner)",
            },
            "writes_when_ingested": [
                str(OUT_JSON.relative_to(REPO)),
                str(OUT_CSV.relative_to(REPO)),
            ],
            "concordance_spec": "cw_fraction_delta per Tempel<->V-Web class pair < 0.002 (0.2pp)",
            "generated_at_utc": _utc(),
        }
        OUT_JSON.write_text(json.dumps(stub, indent=2))
        print(f"STUB: wrote pending-state JSON to {OUT_JSON.relative_to(REPO)}")
        print(f"      Ingest the Tempel catalog at {TEMPEL_PATH.relative_to(REPO)} and rerun.")
        return 2

    print(f"[{_utc()}] Loading Tempel catalog ...")
    tempel = pd.read_parquet(TEMPEL_PATH)
    tempel["tempel_class"] = tempel["multiplicity"].map(_classify_multiplicity)
    print(f"  {len(tempel):,} Tempel rows; per-class: {tempel['tempel_class'].value_counts().to_dict()}")

    print(f"[{_utc()}] Loading matched chirality catalog ...")
    matched = pd.read_parquet(MATCHED_PATH)
    print(f"  matched rows: {len(matched):,}")
    # Pre-filter to the DECLARED chirality-relevant parent BEFORE the spatial
    # NN join: matched_primary_deduped AND CW/CCW (n = 791,635). The pre-
    # v0.1.51 run omitted the matched_primary_deduped filter, so the published
    # 110,586-row "overlap" included non-primary / duplicate nearest-label
    # rows (R22prov OAI-E3 closure; see scripts/17_v0151_closure_recomputes.py).
    matched = matched[matched.get("matched_primary_deduped", matched["matched_primary"])
                      & matched["match_class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
    print(f"  chirality-relevant rows for env join: {len(matched):,}")

    # Spatial nearest-neighbour join (Tempel does not carry DESI TARGETID
    # natively). We use the same 1'' acceptance as the chirality x DESI
    # cross-match; in practice Tempel and DESI overlap nontrivially on
    # SDSS DR10 spectro-z'd galaxies.
    from astropy.coordinates import SkyCoord
    from astropy import units as u
    print(f"[{_utc()}] Sky-coord NN join (1'' acceptance) ...")
    # Matched catalog uses `desi_ra`/`desi_dec` for the joined positions (the
    # chirality-side `match_ra`/`match_dec` are the DR8 Tractor positions used
    # for the original chirality x DESI x-match). For env joins we use the DESI
    # spectro positions as primary.
    ra_col = "desi_ra" if "desi_ra" in matched.columns else "ra"
    dec_col = "desi_dec" if "desi_dec" in matched.columns else "dec"
    sc_matched = SkyCoord(ra=matched[ra_col].to_numpy() * u.deg,
                           dec=matched[dec_col].to_numpy() * u.deg)
    sc_tempel = SkyCoord(ra=tempel["ra"].to_numpy() * u.deg,
                          dec=tempel["dec"].to_numpy() * u.deg)
    idx, sep, _ = sc_matched.match_to_catalog_sky(sc_tempel)
    mask = sep.arcsec <= 1.0
    matched_with_tempel = matched[mask].copy().reset_index(drop=True)
    matched_with_tempel["tempel_class"] = tempel.iloc[idx[mask]]["tempel_class"].values
    print(f"  joined: {len(matched_with_tempel):,} matched-with-Tempel rows")

    per_class = _summarize_class(matched_with_tempel)
    per_class.to_csv(OUT_CSV, index=False)
    concordance = _vweb_concordance(per_class, overlap_df=matched_with_tempel)
    summary = {
        "status": "OK",
        "tempel_source": str(TEMPEL_PATH.relative_to(REPO)),
        "matched_rows": int(len(matched_with_tempel)),
        "per_class": per_class.to_dict(orient="records"),
        "vweb_concordance": concordance,
        "generated_at_utc": _utc(),
    }
    OUT_JSON.write_text(json.dumps(summary, indent=2))
    print(f"\nWrote per-class CSV to {OUT_CSV.relative_to(REPO)}")
    print(f"Wrote summary JSON to {OUT_JSON.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
