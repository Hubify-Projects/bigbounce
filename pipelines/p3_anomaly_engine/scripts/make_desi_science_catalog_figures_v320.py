#!/usr/bin/env python3
"""Generate manuscript figures directly from the P3 v3.2.0 release."""

from pathlib import Path
import json

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[3]
RELEASE = ROOT / "pipelines/p3_anomaly_engine/desi_science_catalog_v3.2.0"
CATALOG = RELEASE / "desi_dr1_science_anomaly_candidates_v3.2.0.parquet"
FIGURES = ROOT / "pipelines/p3_anomaly_engine/figures"


def save(fig: plt.Figure, stem: str) -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    for suffix in ("pdf", "png"):
        fig.savefig(FIGURES / f"{stem}.{suffix}", dpi=220, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    data = pd.read_parquet(CATALOG)
    audit = json.loads((RELEASE / "SELECTION_AUDIT.json").read_text())
    palette = {"GALAXY": "#2563eb", "QSO": "#dc2626", "STAR": "#ca8a04"}

    fig, axes = plt.subplots(1, 3, figsize=(10.8, 3.35), constrained_layout=True)
    ax = axes[0]
    for kind in ("GALAXY", "QSO", "STAR"):
        group = data[data["spectype"] == kind]
        ax.scatter(
            group["target_ra"], group["target_dec"], s=17 if kind != "STAR" else 34,
            c=palette[kind], alpha=0.78, edgecolors="none", label=f"{kind} ({len(group)})",
        )
    tail = data[data["match_separation_arcsec"] > 0.1]
    ax.scatter(tail["target_ra"], tail["target_dec"], s=52, facecolors="none",
               edgecolors="black", linewidths=0.8, label=">0.1 arcsec (11)")
    ax.set(xlabel="Right ascension (deg)", ylabel="Declination (deg)", title="(a) DESI-footprint coverage")
    ax.invert_xaxis()
    ax.legend(fontsize=6.7, frameon=False, loc="lower left")

    ax = axes[1]
    bins = np.linspace(-0.05, 6.15, 26)
    for kind in ("GALAXY", "QSO", "STAR"):
        group = data[data["spectype"] == kind]
        ax.hist(group["z"], bins=bins, histtype="step", linewidth=1.6,
                color=palette[kind], label=kind)
    ax.set(xlabel="Redrock redshift $z$", ylabel="Candidates per bin", title="(b) Descriptive redshift distribution")
    ax.set_yscale("symlog", linthresh=1)
    ax.legend(fontsize=7, frameon=False)

    ax = axes[2]
    for kind in ("GALAXY", "QSO", "STAR"):
        group = data[data["spectype"] == kind]
        ax.scatter(group["z"], group["original_score"], s=18, c=palette[kind],
                   alpha=0.75, edgecolors="none")
    ax.set(xlabel="Redrock redshift $z$", ylabel="Original anomaly score $S$",
           title="(c) Score metadata (not a validation axis)")
    save(fig, "p3_v320_catalog_overview")

    waterfall = audit["waterfall"]
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.25), constrained_layout=True)
    ax = axes[0]
    labels = ["1 arcsec +\nscience bits", "+ global\nprimary", "+ ZWARN=0\nrelease"]
    values = [waterfall["existing_bitmask_1arcsec"], waterfall["remaining_zcat_primary"],
              waterfall["released_zcat_primary_zwarn0"]]
    bars = ax.bar(labels, values, color=["#94a3b8", "#64748b", "#2563eb"], width=0.68)
    for bar, value in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 35, f"{value:,}",
                ha="center", va="bottom", fontsize=8)
    ax.set(ylabel="Rows", title="(a) Declared selection waterfall")
    ax.set_ylim(0, 2750)

    ax = axes[1]
    sep = np.sort(data["match_separation_arcsec"].to_numpy(float))
    survival = np.arange(len(sep), 0, -1)
    ax.step(sep, survival, where="post", color="#2563eb", linewidth=1.5)
    ax.axvline(0.1, color="#111827", linestyle="--", linewidth=1, label="quality-tier boundary")
    ax.axvline(1.0, color="#dc2626", linestyle=":", linewidth=1, label="join limit")
    ax.set(xscale="log", yscale="log", xlabel="Separation threshold (arcsec)",
           ylabel="Candidates at or above threshold", title="(b) Disclosed separation tail")
    ax.legend(fontsize=6.7, frameon=False)
    save(fig, "p3_v320_selection_waterfall")


if __name__ == "__main__":
    main()
