#!/usr/bin/env python3
"""Figures (first run).

Produces:
  - fig_sky_footprint.png
  - fig_z_histogram.png
  - fig_cw_vs_z.png
  - fig_cw_vs_density.png
  - fig_healpix_cw_residual_nside{32}.png
  - fig_radius_sensitivity.png
  - fig_confidence_sensitivity.png

All other figures (cosmic-web env, full null grid) are emitted by analysis
scripts as data CSV; this script renders the headline panels.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import load_config, resolve_p5_path, ensure_dir


def _save(fig, out_path: Path) -> None:
    fig.savefig(out_path, dpi=200, bbox_inches="tight")
    print(f"[fig] {out_path}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=None)
    args = parser.parse_args()
    cfg = load_config(args.config)

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    matched_path = resolve_p5_path(cfg["paths"]["out_matched"])
    if not matched_path.exists():
        print(f"ERROR: {matched_path} missing.")
        return 2
    figs = ensure_dir(resolve_p5_path("figures"))
    df = pd.read_parquet(matched_path)
    df = df[df.get("matched_primary_deduped", df["matched_primary"])]

    # 1. Sky footprint
    fig, ax = plt.subplots(figsize=(9, 4.5))
    sample = df.sample(min(100_000, len(df)), random_state=0)
    ax.scatter(sample["desi_ra"], sample["desi_dec"], s=0.5, alpha=0.3)
    ax.set_xlabel("RA (deg)"); ax.set_ylabel("Dec (deg)")
    ax.set_title(f"Matched footprint (N={len(df):,})")
    _save(fig, figs / "fig_sky_footprint.png"); plt.close(fig)

    # 2. Redshift histogram
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.hist(df["desi_z"], bins=80)
    ax.set_xlabel("DESI z"); ax.set_ylabel("count")
    ax.set_title("Matched-spiral redshift distribution")
    _save(fig, figs / "fig_z_histogram.png"); plt.close(fig)

    # 3. CW fraction vs redshift
    z_csv = resolve_p5_path("results/analysis_redshift/cw_fraction_by_z.csv")
    if z_csv.exists():
        t = pd.read_csv(z_csv)
        z_mid = 0.5 * (t["z_low"] + t["z_high"])
        fig, ax = plt.subplots(figsize=(7, 4.5))
        ax.errorbar(z_mid, t["cw_fraction"],
                    yerr=[t["cw_fraction"] - t["ci95_low"], t["ci95_high"] - t["cw_fraction"]],
                    fmt="o", capsize=3)
        ax.axhline(0.5, ls="--", color="gray", lw=0.8)
        ax.set_xlabel("redshift z"); ax.set_ylabel("CW fraction")
        ax.set_title("CW fraction vs redshift (95% CI)")
        _save(fig, figs / "fig_cw_vs_z.png"); plt.close(fig)

    # 4. CW fraction vs density quantile
    d_csv = resolve_p5_path("results/analysis_density/cw_fraction_by_density.csv")
    if d_csv.exists():
        t = pd.read_csv(d_csv)
        q_mid = 0.5 * (t["q_low"] + t["q_high"])
        fig, ax = plt.subplots(figsize=(7, 4.5))
        ax.scatter(q_mid, t["cw_fraction"], s=40)
        ax.axhline(0.5, ls="--", color="gray", lw=0.8)
        ax.set_xlabel("density quantile (low → high)"); ax.set_ylabel("CW fraction")
        ax.set_title("CW fraction vs local projected density")
        _save(fig, figs / "fig_cw_vs_density.png"); plt.close(fig)

    # 5. HEALPix residual (nside=32 default)
    hp_csv_candidates = list(resolve_p5_path("results/analysis_healpix").glob("nside*_cw_per_pixel.csv"))
    if hp_csv_candidates:
        t = pd.read_csv(hp_csv_candidates[0])
        fig, ax = plt.subplots(figsize=(7, 4.5))
        ax.hist(t["sigma_from_half"], bins=60)
        ax.set_xlabel("σ from half (per pixel)"); ax.set_ylabel("pixel count")
        ax.set_title(f"HEALPix per-pixel CW deviation — {hp_csv_candidates[0].stem}")
        _save(fig, figs / "fig_healpix_cw_residual.png"); plt.close(fig)

    # 6. Radius sensitivity
    r_csv = resolve_p5_path("results/analysis_systematics/radius_sensitivity.csv")
    if r_csv.exists():
        t = pd.read_csv(r_csv)
        fig, ax = plt.subplots(figsize=(7, 4.5))
        ax.plot(t["radius_arcsec"], t["sigma_from_half"], "o-")
        ax.axhline(0, ls="--", color="gray", lw=0.8)
        ax.set_xlabel("match radius (arcsec)"); ax.set_ylabel("σ from half")
        ax.set_title("CW fraction sensitivity to match radius")
        _save(fig, figs / "fig_radius_sensitivity.png"); plt.close(fig)

    # 7. Confidence sensitivity
    c_csv = resolve_p5_path("results/analysis_systematics/confidence_sensitivity.csv")
    if c_csv.exists():
        t = pd.read_csv(c_csv)
        fig, ax = plt.subplots(figsize=(7, 4.5))
        ax.plot(t["min_confidence"], t["sigma_from_half"], "o-")
        ax.axhline(0, ls="--", color="gray", lw=0.8)
        ax.set_xlabel("min classifier confidence"); ax.set_ylabel("σ from half")
        ax.set_title("CW fraction sensitivity to confidence threshold")
        _save(fig, figs / "fig_confidence_sensitivity.png"); plt.close(fig)

    print("[done]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
