#!/usr/bin/env python3
"""Angular cross-match of P4 chirality catalog vs DESI DR1 redshift catalog.

Strategy:
  - Build SkyCoord arrays for both catalogs.
  - For each DESI source, find the nearest P4 neighbour on the sphere.
  - Accept matches within `primary_radius_arcsec` (config-pinned).
  - For sensitivity analysis, also emit indicator columns for each radius in
    `sensitivity_radii_arcsec`.
  - Duplicate resolution: nearest-neighbour wins (config-pinned).

Outputs:
  - p5_matched_chirality_desi.parquet
  - p5_matched_chirality_desi_summary.json
  - sidecar provenance

Notes:
  - astropy's match_to_catalog_sky uses a KD-tree on unit-sphere xyz so this
    scales fine to 22.5M × 8.5M on a single host with enough RAM (~10-15 GB).
  - For really memory-constrained hosts, see `--chunk-desi` to stream DESI in
    N chunks. The catalog (P4) is loaded once.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import load_config, write_provenance, ensure_dir, resolve_p5_path, utc_now


def _derive_imaging_leg(dec: np.ndarray) -> np.ndarray:
    """Coarse imaging-leg from declination (the HF P4 parquet drops the
    canonical `imaging_leg` column). Boundaries follow DESI Legacy Survey
    convention: BASS+MzLS for Dec >= 32.375 deg, DES for Dec < -18 deg
    (DES footprint southern coverage), DECaLS in between."""
    leg = np.empty(len(dec), dtype=object)
    leg[:] = "DECaLS"
    leg[dec >= 32.375] = "BASS+MzLS"
    leg[dec < -18.0] = "DES"
    return leg


def _load_p4(cfg: dict) -> pd.DataFrame:
    path = resolve_p5_path(cfg["paths"]["p4_catalog"])
    if not path.exists():
        raise FileNotFoundError(
            f"P4 catalog missing at {path}. Run scripts/01_fetch_p4_catalog.py first."
        )
    print(f"[p4] reading {path}")
    # Actual HF parquet schema (verified 2026-05-15): dr8_id, ra, dec,
    # class_eq/class_raw_x/class_raw_y, p_{cw,ccw,ns}_{eq,raw_x,raw_y},
    # confidence_eq, confidence_raw, image_url. NO objid/imaging_leg/mag_r/axial_ratio_ba.
    df = pd.read_parquet(path, columns=[
        "dr8_id", "ra", "dec", "class_eq",
        "p_cw_eq", "p_ccw_eq", "p_ns_eq",
        "confidence_eq",
    ])
    # Derive imaging_leg from Dec since the HF parquet drops it
    df["imaging_leg"] = _derive_imaging_leg(df["dec"].to_numpy())
    # Optional confidence cut
    min_conf = cfg["filters"]["classifier"].get("min_confidence")
    if min_conf is not None:
        p_max = df[["p_cw_eq", "p_ccw_eq", "p_ns_eq"]].max(axis=1)
        df = df[p_max >= float(min_conf)].reset_index(drop=True)
    if not cfg["filters"]["classifier"].get("keep_non_spirals", True):
        df = df[df["class_eq"] != "NS"].reset_index(drop=True)
    keep_legs = cfg["filters"]["imaging"].get("keep_legs")
    if keep_legs:
        df = df[df["imaging_leg"].isin(keep_legs)].reset_index(drop=True)
    print(f"[p4] kept {len(df):,} rows after filters")
    return df


def _load_desi(cfg: dict) -> pd.DataFrame:
    path = resolve_p5_path(cfg["paths"]["desi_zall"])
    if not path.exists():
        raise FileNotFoundError(
            f"DESI catalog missing at {path}. Run scripts/02_fetch_desi_dr1.py first."
        )
    print(f"[desi] reading {path}")
    df = pd.read_parquet(path)
    rs = cfg["filters"]["redshift_quality"]
    if rs.get("require_zwarn_zero", True) and "ZWARN" in df.columns:
        df = df[df["ZWARN"] == 0]
    if "Z" in df.columns:
        df = df[(df["Z"] >= rs.get("z_min", 0.0)) & (df["Z"] <= rs.get("z_max", 5.0))]
    if rs.get("drop_zfail", True) and "SPECTYPE" in df.columns:
        df = df[df["SPECTYPE"].isin(["GALAXY", "QSO"])]   # drop STAR; bad fits already gated by ZWARN
    df = df.reset_index(drop=True)
    print(f"[desi] kept {len(df):,} rows after redshift-quality filters")
    return df


def _crossmatch(
    p4: pd.DataFrame,
    desi: pd.DataFrame,
    primary_radius_arcsec: float,
    sens_radii: list[float],
) -> pd.DataFrame:
    from astropy.coordinates import SkyCoord
    from astropy import units as u

    print("[match] building SkyCoord arrays")
    p4_sc = SkyCoord(ra=p4["ra"].to_numpy() * u.deg, dec=p4["dec"].to_numpy() * u.deg)
    desi_sc = SkyCoord(
        ra=desi["TARGET_RA"].to_numpy() * u.deg,
        dec=desi["TARGET_DEC"].to_numpy() * u.deg,
    )

    print(f"[match] nearest-neighbor (DESI -> P4); N_desi={len(desi):,} N_p4={len(p4):,}")
    t0 = time.time()
    idx, sep2d, _ = desi_sc.match_to_catalog_sky(p4_sc)
    sep_arcsec = sep2d.to(u.arcsec).value
    print(f"[match] done in {time.time()-t0:.1f}s")

    matched_mask = sep_arcsec <= primary_radius_arcsec
    print(f"[match] {matched_mask.sum():,} within {primary_radius_arcsec}\" "
          f"({100*matched_mask.mean():.3f}% of DESI sources)")

    out = pd.DataFrame({
        "desi_targetid": desi["TARGETID"].to_numpy(),
        "desi_ra": desi["TARGET_RA"].to_numpy(),
        "desi_dec": desi["TARGET_DEC"].to_numpy(),
        "desi_z": desi["Z"].to_numpy() if "Z" in desi.columns else np.nan,
        "desi_zerr": desi["ZERR"].to_numpy() if "ZERR" in desi.columns else np.nan,
        "desi_zwarn": desi["ZWARN"].to_numpy() if "ZWARN" in desi.columns else np.nan,
        "desi_spectype": desi["SPECTYPE"].to_numpy() if "SPECTYPE" in desi.columns else "",
        "desi_subtype": desi["SUBTYPE"].to_numpy() if "SUBTYPE" in desi.columns else "",
        "desi_desi_target": desi["DESI_TARGET"].to_numpy() if "DESI_TARGET" in desi.columns else 0,
        "desi_bgs_target": desi["BGS_TARGET"].to_numpy() if "BGS_TARGET" in desi.columns else 0,
        "desi_program": desi["PROGRAM"].to_numpy() if "PROGRAM" in desi.columns else "",
        "desi_survey": desi["SURVEY"].to_numpy() if "SURVEY" in desi.columns else "",
        "desi_healpix": desi["HEALPIX"].to_numpy() if "HEALPIX" in desi.columns else 0,
        "desi_morphtype": desi["MORPHTYPE"].to_numpy() if "MORPHTYPE" in desi.columns else "",
        "match_dr8_id": p4["dr8_id"].to_numpy()[idx],
        "match_ra": p4["ra"].to_numpy()[idx],
        "match_dec": p4["dec"].to_numpy()[idx],
        "match_class_eq": p4["class_eq"].to_numpy()[idx],
        "match_p_cw": p4["p_cw_eq"].to_numpy()[idx],
        "match_p_ccw": p4["p_ccw_eq"].to_numpy()[idx],
        "match_p_ns": p4["p_ns_eq"].to_numpy()[idx],
        "match_confidence_eq": p4["confidence_eq"].to_numpy()[idx],
        "match_imaging_leg": p4["imaging_leg"].to_numpy()[idx],
        "sep_arcsec": sep_arcsec,
    })
    out["matched_primary"] = matched_mask
    for r in sens_radii:
        out[f"matched_{r}arcsec"] = sep_arcsec <= r
    out["match_confidence"] = out[["match_p_cw", "match_p_ccw", "match_p_ns"]].max(axis=1)
    return out


def _dedupe(out: pd.DataFrame, strategy: str) -> pd.DataFrame:
    """If multiple DESI sources collide on the same P4 objid, keep only one."""
    if strategy == "keep_all":
        return out
    df = out[out["matched_primary"]].copy()
    df = df.sort_values("sep_arcsec", ascending=True)
    if strategy == "nearest":
        df = df.drop_duplicates(subset=["match_dr8_id"], keep="first")
    elif strategy == "reject_both":
        dup_ids = df.duplicated(subset=["match_dr8_id"], keep=False)
        df = df[~dup_ids]
    else:
        raise ValueError(f"Unknown duplicate_strategy: {strategy}")
    out["matched_primary_deduped"] = False
    out.loc[df.index, "matched_primary_deduped"] = True
    return out


def _summarize(out: pd.DataFrame, cfg: dict) -> dict[str, Any]:
    primary = out[out.get("matched_primary_deduped", out["matched_primary"])]
    s: dict[str, Any] = {
        "config_version": cfg["version"],
        "config_hash": cfg["_config_hash"],
        "primary_radius_arcsec": cfg["crossmatch"]["primary_radius_arcsec"],
        "duplicate_strategy": cfg["crossmatch"]["duplicate_strategy"],
        "totals": {
            "desi_input_rows": int(len(out)),
            "matched_primary": int(out["matched_primary"].sum()),
            "matched_primary_deduped": int(primary.shape[0]),
        },
        "class_eq_counts": {
            k: int(v) for k, v in primary["match_class_eq"].value_counts().items()
        },
        "desi_spectype_counts": {
            k: int(v) for k, v in primary["desi_spectype"].value_counts().items()
        },
        "imaging_leg_counts": {
            k: int(v) for k, v in primary["match_imaging_leg"].value_counts().items()
        },
        "redshift_summary": {
            "min": float(primary["desi_z"].min()) if len(primary) else None,
            "median": float(primary["desi_z"].median()) if len(primary) else None,
            "max": float(primary["desi_z"].max()) if len(primary) else None,
        },
        "sep_summary_arcsec": {
            "p50": float(primary["sep_arcsec"].median()) if len(primary) else None,
            "p90": float(primary["sep_arcsec"].quantile(0.9)) if len(primary) else None,
            "p99": float(primary["sep_arcsec"].quantile(0.99)) if len(primary) else None,
        },
        "sensitivity": {
            f"{r}arcsec_matches": int(out[f"matched_{r}arcsec"].sum())
            for r in cfg["crossmatch"]["sensitivity_radii_arcsec"]
        },
    }
    # CW/CCW counts among spirals
    sp = primary[primary["match_class_eq"].isin(["CW", "CCW"])]
    if len(sp):
        n_cw = int((sp["match_class_eq"] == "CW").sum())
        n_ccw = int((sp["match_class_eq"] == "CCW").sum())
        n_sp = n_cw + n_ccw
        s["chirality_among_spirals"] = {
            "n_cw": n_cw,
            "n_ccw": n_ccw,
            "n_spirals": n_sp,
            "cw_fraction": (n_cw / n_sp) if n_sp else None,
            "binomial_sigma_from_half": (
                (n_cw - 0.5 * n_sp) / (0.5 * n_sp ** 0.5) if n_sp else None
            ),
        }
    s["written_utc"] = utc_now()
    return s


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=None)
    parser.add_argument("--limit-desi", type=int, default=None,
                        help="Subsample DESI to N rows (testing only).")
    args = parser.parse_args()

    cfg = load_config(args.config)
    p4 = _load_p4(cfg)
    desi = _load_desi(cfg)
    if args.limit_desi:
        desi = desi.iloc[: args.limit_desi].reset_index(drop=True)
        print(f"[debug] subsampling DESI to first {args.limit_desi:,} rows")

    out = _crossmatch(
        p4,
        desi,
        primary_radius_arcsec=float(cfg["crossmatch"]["primary_radius_arcsec"]),
        sens_radii=list(cfg["crossmatch"]["sensitivity_radii_arcsec"]),
    )
    out = _dedupe(out, strategy=cfg["crossmatch"]["duplicate_strategy"])

    out_path = resolve_p5_path(cfg["paths"]["out_matched"])
    ensure_dir(out_path.parent)
    out.to_parquet(out_path, index=False)

    summary = _summarize(out, cfg)
    summary_path = resolve_p5_path(cfg["paths"]["out_summary"])
    summary_path.write_text(json.dumps(summary, indent=2))

    write_provenance(out_path, {
        "p4_rows_after_filter": int(len(p4)),
        "desi_rows_after_filter": int(len(desi)),
        "config_version": cfg["version"],
        "config_hash": cfg["_config_hash"],
    })

    print(f"[done] wrote {out_path}")
    print(f"[done] wrote {summary_path}")
    print(json.dumps(summary["totals"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
