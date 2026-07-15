#!/usr/bin/env python3
"""Render the Paper 1B NaMaster validation figure from exact-window JSON.

The figure is a derived artifact.  Its numerical inputs remain the canonical
JSON outputs so every plotted point and uncertainty can be independently
checked without digitizing the image.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "reproducibility/p1_namaster_500mc/results/physical_spectrum_v2"
SUMMARY = RESULTS / "summary.json"
DECLARED = RESULTS / "declared_fsky_sign_battery.json"
OUTPUT = ROOT / "arxiv/figures/fig_namaster_recovery.png"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    summary = load(SUMMARY)
    declared = load(DECLARED)
    result = summary["results"]

    injected = np.array([
        result["beta_null"]["input_beta_deg"],
        result["beta_paper1"]["input_beta_deg"],
        result["beta_observed"]["input_beta_deg"],
    ])
    recovered = np.array([
        result["beta_null"]["recovered_beta_deg"],
        result["beta_paper1"]["recovered_beta_deg"],
        result["beta_observed"]["recovered_beta_deg"],
    ])

    positive = sorted(
        (item for item in declared["results"] if item["beta_deg"] > 0),
        key=lambda item: item["fsky_actual_apodized"],
    )
    fsky = np.array([item["fsky_actual_apodized"] for item in positive])
    fsky_recovered = np.array([item["recovered_beta_deg"] for item in positive])
    fsky_scatter = np.array([item["per_realization_beta_std_deg"] for item in positive])
    fsky_se = np.array([item["mc_mean_standard_error_deg"] for item in positive])

    canonical_fsky = float(summary["f_sky"])
    canonical_recovered = float(result["beta_paper1"]["recovered_beta_deg"])
    canonical_scatter = float(result["beta_paper1"]["per_realization_beta_std_deg"])
    canonical_se = float(result["beta_paper1"]["mc_mean_standard_error_deg"])
    fsky = np.insert(fsky, 0, canonical_fsky)
    fsky_recovered = np.insert(fsky_recovered, 0, canonical_recovered)
    fsky_scatter = np.insert(fsky_scatter, 0, canonical_scatter)
    fsky_se = np.insert(fsky_se, 0, canonical_se)

    plt.style.use("seaborn-v0_8-whitegrid")
    fig, axes = plt.subplots(1, 2, figsize=(12.4, 5.2), constrained_layout=True)

    axis = axes[0]
    limits = (-0.018, 0.365)
    axis.plot(limits, limits, color="0.35", linewidth=1.2, linestyle="--", label="ideal recovery")
    axis.scatter(injected, recovered, s=72, color="#2869a6", zorder=3, label="exact-window 500 MC")
    for x, y in zip(injected, recovered, strict=True):
        axis.annotate(
            rf"$\Delta\hat{{\beta}}={y-x:+.3f}^\circ$",
            (x, y),
            xytext=(7, -17 if x else 9),
            textcoords="offset points",
            fontsize=9,
        )
    axis.set(xlim=limits, ylim=limits, xlabel=r"injected $\beta$ [deg]", ylabel=r"mean recovered $\hat\beta$ [deg]")
    axis.set_title("(a) Exact bandpower-window recovery")
    axis.legend(frameon=False, loc="upper left")

    axis = axes[1]
    axis.errorbar(
        fsky,
        fsky_recovered,
        yerr=fsky_scatter,
        fmt="none",
        ecolor="#8bb5d9",
        elinewidth=5,
        alpha=0.5,
        label=r"single-realization $\sigma_\beta$",
    )
    axis.errorbar(
        fsky,
        fsky_recovered,
        yerr=fsky_se,
        fmt="o",
        color="#2869a6",
        capsize=4,
        label=r"mean $\pm$ MC standard error",
    )
    axis.axhline(0.27, color="0.35", linewidth=1.2, linestyle="--", label=r"injected $0.27^\circ$")
    axis.set(xlabel=r"apodized $f_{\rm sky}$", ylabel=r"mean recovered $\hat\beta$ [deg]")
    axis.set_title("(b) Declared sky-fraction checks")
    axis.legend(frameon=False, fontsize=9)

    fig.suptitle("NaMaster synthetic-sky validation (500 realizations per point)", fontsize=13)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=220, metadata={"Software": "plot_exact_window_results.py"})
    plt.close(fig)
    print(OUTPUT)


if __name__ == "__main__":
    main()
