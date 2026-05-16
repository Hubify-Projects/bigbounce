#!/usr/bin/env python3
"""Analysis D — regional coherence via HEALPix.

For a grid of NSIDEs (configured), compute CW fraction per pixel +
significance vs the global rate, then run a label-shuffle permutation null
on the same pixelization to get the chance distribution of pixel-level
deviations. Output per-NSIDE summary tables + maps.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import load_config, resolve_p5_path, ensure_dir, utc_now


def _ang2pix(nside: int, ra_deg: np.ndarray, dec_deg: np.ndarray) -> np.ndarray:
    import healpy as hp
    theta = np.deg2rad(90.0 - dec_deg)
    phi = np.deg2rad(ra_deg)
    return hp.ang2pix(nside, theta, phi, nest=False)


def _pixel_table(pix: np.ndarray, labels: np.ndarray, min_count: int) -> pd.DataFrame:
    df = pd.DataFrame({"pix": pix, "y": labels})
    g = df.groupby("pix")["y"].agg(["sum", "count"]).reset_index()
    g = g.rename(columns={"sum": "n_cw", "count": "n"})
    g["n_ccw"] = g["n"] - g["n_cw"]
    g["cw_fraction"] = g["n_cw"] / g["n"]
    g["sigma_from_half"] = (g["n_cw"] - 0.5 * g["n"]) / (0.5 * np.sqrt(g["n"]))
    g = g[g["n"] >= min_count].reset_index(drop=True)
    return g


def _permutation_null(pix: np.ndarray, labels: np.ndarray, min_count: int,
                      n_perm: int, seed: int) -> dict:
    rng = np.random.default_rng(seed)
    base = _pixel_table(pix, labels, min_count)
    obs_max = float(np.nanmax(np.abs(base["sigma_from_half"].to_numpy())))
    null = np.zeros(n_perm)
    for k in range(n_perm):
        perm = rng.permutation(labels)
        t = _pixel_table(pix, perm, min_count)
        null[k] = np.nanmax(np.abs(t["sigma_from_half"].to_numpy()))
    return {
        "n_pixels": int(len(base)),
        "obs_max_abs_sigma": obs_max,
        "null_p99_max_abs_sigma": float(np.quantile(null, 0.99)),
        "p_value": float((null >= obs_max).mean()),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=None)
    args = parser.parse_args()
    cfg = load_config(args.config)

    matched_path = resolve_p5_path(cfg["paths"]["out_matched"])
    if not matched_path.exists():
        print(f"ERROR: {matched_path} missing.")
        return 2
    out_dir = ensure_dir(resolve_p5_path("results/analysis_healpix"))

    df = pd.read_parquet(matched_path)
    df = df[df.get("matched_primary_deduped", df["matched_primary"])]
    sp = df[df["match_class_eq"].isin(["CW", "CCW"])].copy()

    ra = sp["desi_ra"].to_numpy()
    dec = sp["desi_dec"].to_numpy()
    labels = (sp["match_class_eq"] == "CW").astype(int).to_numpy()

    nsides = list(cfg["analysis"]["healpix"]["nsides"])
    min_count = int(cfg["analysis"]["healpix"]["min_count_per_pixel"])
    seed = int(cfg["statistics"]["random_seed"])
    n_perm = int(cfg["analysis"].get("permutation_n", 1000))

    summaries = {}
    for nside in nsides:
        try:
            pix = _ang2pix(nside, ra, dec)
        except ImportError:
            print("ERROR: healpy required. `pip install healpy`.")
            return 2
        table = _pixel_table(pix, labels, min_count)
        table.to_csv(out_dir / f"nside{nside}_cw_per_pixel.csv", index=False)
        summaries[str(nside)] = _permutation_null(pix, labels, min_count, n_perm, seed)

    out = {
        "written_utc": utc_now(),
        "config_version": cfg["version"],
        "n_spirals": int(len(sp)),
        "nside_results": summaries,
    }
    (out_dir / "summary.json").write_text(json.dumps(out, indent=2))
    print(f"[done] wrote {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
