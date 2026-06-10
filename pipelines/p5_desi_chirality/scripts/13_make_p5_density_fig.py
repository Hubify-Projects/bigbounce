#!/usr/bin/env python3
"""P5 paper figure: CW fraction per density quintile with classifier-monopole
prediction overlay.

The Paper IV catalog-wide monopole offset Delta_fCW = -0.0026 predicts a
per-quintile sigma_from_half = -0.0026 * 2 * sqrt(N) at fixed N. We
overlay this prediction on the observed quintile values; deviations
beyond the monopole prediction are the only candidates for density-
correlated environmental signal.

Input:
    pipelines/p5_desi_chirality/results/analysis_density/cw_fraction_by_density.csv

Output:
    pipelines/p5_desi_chirality/figures/fig_p5_cw_vs_density.png
"""
from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import beta as beta_dist

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
P5 = REPO / "pipelines/p5_desi_chirality"
FIG_DIR = P5 / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

SRC = P5 / "results/analysis_density/cw_fraction_by_density.csv"
OUT = FIG_DIR / "fig_p5_cw_vs_density.png"

PAPER4_GLOBAL_F = 0.4974
PAPER4_DELTA = PAPER4_GLOBAL_F - 0.5  # -0.0026


def _ci_95(n_cw: int, n: int) -> tuple[float, float]:
    if n == 0:
        return (float("nan"), float("nan"))
    a, b = 0.5 + n_cw, 0.5 + (n - n_cw)
    return beta_dist.ppf(0.025, a, b), beta_dist.ppf(0.975, a, b)


def main() -> int:
    df = pd.read_csv(SRC)
    df["q_label"] = [f"Q{i+1}" for i in range(len(df))]
    xs = np.arange(len(df))
    cis = [_ci_95(int(r["n_cw"]), int(r["n"])) for _, r in df.iterrows()]
    yerr_lo = df["cw_fraction"].to_numpy() - np.array([c[0] for c in cis])
    yerr_hi = np.array([c[1] for c in cis]) - df["cw_fraction"].to_numpy()
    # Monopole prediction per quintile at fixed N: predicted f_CW = 0.5 + Delta
    pred_f = PAPER4_GLOBAL_F  # same for every bin (catalog-wide)

    fig, (ax_f, ax_s) = plt.subplots(1, 2, figsize=(10.4, 4.2))

    # LEFT panel: f_CW per quintile + 95% CI
    ax_f.bar(xs, df["cw_fraction"].to_numpy(), color="#64748b",
             edgecolor="black", linewidth=0.7, alpha=0.85)
    ax_f.errorbar(xs, df["cw_fraction"].to_numpy(),
                   yerr=[yerr_lo, yerr_hi], fmt="none",
                   ecolor="black", elinewidth=1.0, capsize=4)
    ax_f.axhline(0.5, linestyle="--", color="#94a3b8", linewidth=1.0,
                 label="parity 0.5")
    ax_f.axhline(PAPER4_GLOBAL_F, linestyle=":", color="#dc2626", linewidth=1.0,
                 label=f"Paper IV $\\bar f_{{\\rm CW}}={PAPER4_GLOBAL_F}$")
    ax_f.set_ylim(0.485, 0.510)
    ax_f.set_xticks(xs)
    ax_f.set_xticklabels(
        [f"{r['q_label']}\n[{int(r['density_low'])}, {int(r['density_high'])}]"
         for _, r in df.iterrows()],
        fontsize=7,
        rotation=30,
        ha="right",
    )
    ax_f.set_xlabel("density quintile (k=5 NN density range)", fontsize=8.5)
    ax_f.set_ylabel("$f_{\\rm CW}$", fontsize=10)
    ax_f.set_title("CW fraction per projected-density quintile\n"
                   "($k\\!=\\!5$ NN density proxy; $n\\!=\\!158{,}327$/bin)",
                   fontsize=10.5)
    ax_f.legend(loc="upper right", fontsize=8.5, frameon=True)

    # RIGHT panel: sigma_from_half per quintile + monopole prediction band
    sigma_obs = df["sigma_from_half"].to_numpy()
    sigma_pred = PAPER4_DELTA * 2 * np.sqrt(df["n"].to_numpy())  # negative
    ax_s.bar(xs, sigma_obs, color="#94a3b8", edgecolor="black",
             linewidth=0.7, alpha=0.85, label="observed $\\sigma$")
    ax_s.plot(xs, sigma_pred, marker="D", linestyle="-",
              color="#dc2626", linewidth=1.5, markersize=8,
              label="Paper IV monopole prediction\n($\\sigma_{\\rm pred}=-2 \\Delta f_{\\rm CW} \\sqrt{N}$)")
    ax_s.axhline(0.0, linestyle="-", color="black", linewidth=0.5)
    ax_s.axhline(-3.29, linestyle=":", color="#0369a1", linewidth=0.8,
                 label="Bonferroni-5 $\\alpha\\!=\\!0.01$")
    ax_s.axhline(+3.29, linestyle=":", color="#0369a1", linewidth=0.8)
    ax_s.set_xticks(xs)
    ax_s.set_xticklabels([r["q_label"] for _, r in df.iterrows()], fontsize=10)
    ax_s.set_ylabel("$\\sigma_{\\rm from\\,half}$", fontsize=10)
    ax_s.set_title("Observed vs Paper IV-monopole-predicted $\\sigma$\n"
                   "(deviation from monopole = density-correlated signal)",
                   fontsize=10.5)
    ax_s.legend(loc="lower right", fontsize=8.0, frameon=True)
    ax_s.set_ylim(-5.5, +1.5)

    fig.suptitle("Density-quintile null: observed deviation tracks the Paper IV "
                 "classifier-monopole, not the local density",
                 fontsize=11.5, y=0.99)
    fig.tight_layout()
    fig.savefig(OUT, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {OUT.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
