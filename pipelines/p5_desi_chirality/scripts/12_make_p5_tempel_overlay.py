#!/usr/bin/env python3
"""P5 paper figure: V-Web vs Tempel side-by-side bar overlay.

Produces a single 2-panel figure (left: V-Web canonical run; right: Tempel
FoF cross-validation) so reviewers can visually verify the
like-for-like filament-class concordance at 0.29pp (declared-parent overlap, v0.1.51).

Both panels render CW fraction per environment class with 95% Jeffreys
binomial credible intervals + parity-0.5 dashed reference + Paper IV
global f_CW=0.4974 dotted reference. The y-axis range is shared between
panels.

Inputs:
    pipelines/p5_desi_chirality/results/analysis_cosmic_web/cw_fraction_by_env__desi_env_vweb.csv
    pipelines/p5_desi_chirality/results/analysis_cosmic_web/cw_fraction_by_env__tempel_fof.csv

Output:
    pipelines/p5_desi_chirality/figures/fig_p5_vweb_vs_tempel_overlay.png
"""
from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import beta as beta_dist

REPO = Path(__file__).resolve().parents[3]
P5 = REPO / "pipelines/p5_desi_chirality"
FIG_DIR = P5 / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

VWEB_CSV = P5 / "results/analysis_cosmic_web/cw_fraction_by_env__desi_env_vweb.csv"
TEMPEL_CSV = P5 / "results/analysis_cosmic_web/cw_fraction_by_env__tempel_fof.csv"

VWEB_ORDER = ["void", "wall", "filament", "cluster"]
TEMPEL_ORDER = ["isolated", "small_group", "filament_like", "cluster_like"]
VWEB_COLORS = {
    "void": "#cbd5e1",
    "wall": "#94a3b8",
    "filament": "#64748b",
    "cluster": "#475569",
}
TEMPEL_COLORS = {
    "isolated": "#fde68a",
    "small_group": "#fbbf24",
    "filament_like": "#d97706",
    "cluster_like": "#92400e",
}


def _ci_95(n_cw: int, n: int) -> tuple[float, float]:
    if n == 0:
        return (float("nan"), float("nan"))
    a, b = 0.5 + n_cw, 0.5 + (n - n_cw)
    return beta_dist.ppf(0.025, a, b), beta_dist.ppf(0.975, a, b)


def _draw(ax, df, order, colors, title, ylim, *, xlabel_prefix=""):
    df = df.set_index(df.columns[0]).reindex(order)
    n_col = "n"
    cw_col = "cw_fraction"
    ncw_col = "n_cw"
    yvals = df[cw_col].to_numpy()
    cis = [_ci_95(int(r[ncw_col]), int(r[n_col])) for _, r in df.iterrows()]
    yerr_lo = yvals - np.array([c[0] for c in cis])
    yerr_hi = np.array([c[1] for c in cis]) - yvals
    xs = np.arange(len(order))
    ax.bar(xs, yvals, color=[colors[e] for e in order],
           edgecolor="black", linewidth=0.7, alpha=0.85)
    ax.errorbar(xs, yvals, yerr=[yerr_lo, yerr_hi], fmt="none",
                ecolor="black", elinewidth=1.0, capsize=3.5)
    ax.axhline(0.5, linestyle="--", color="#94a3b8", linewidth=1.0,
               label="parity 0.5")
    ax.axhline(0.4974, linestyle=":", color="#dc2626", linewidth=1.0,
               label="Paper IV $\\bar f_{\\rm CW}$ 0.4974")
    ax.set_xticks(xs)
    ax.set_xticklabels(
        [f"{xlabel_prefix}{e}\n$n$={int(df.loc[e, n_col]):,}" for e in order],
        fontsize=8.5,
    )
    ax.set_ylim(*ylim)
    ax.set_title(title, fontsize=10.5)
    ax.set_ylabel("$f_{\\rm CW}$", fontsize=10)
    ax.tick_params(axis="y", labelsize=9)


def main() -> int:
    vweb = pd.read_csv(VWEB_CSV)
    tempel = pd.read_csv(TEMPEL_CSV)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 4.4),
                                    sharey=True)
    ylim = (0.43, 0.53)
    _draw(ax1, vweb, VWEB_ORDER, VWEB_COLORS,
          "(a) T-Web (canonical $R_s=25$ Mpc/$h$, $\\lambda_{\\rm th}=0$)\n"
          "$n=812{,}793$ environment-labelled rows", ylim)
    _draw(ax2, tempel.rename(columns={"tempel_class": "env_class"}),
          TEMPEL_ORDER, TEMPEL_COLORS,
          "(b) Tempel+2014 FoF cross-validation\n"
          "$n=96{,}753$ Tempel-overlap matched spirals (declared parent)", ylim)
    # Add (a)/(b) text annotations top-left of each panel
    ax1.text(0.02, 0.98, "(a)", transform=ax1.transAxes,
             fontsize=12, fontweight="bold", va="top", ha="left")
    ax2.text(0.02, 0.98, "(b)", transform=ax2.transAxes,
             fontsize=12, fontweight="bold", va="top", ha="left")
    # concordance annotation: like-for-like overlap filament concordance 0.29pp
    ax1.annotate(
        "like-for-like filament concordance (overlap): $0.29$ pp ($\\sim$$0.5\\sigma$)",
        xy=(2, 0.498), xytext=(2.1, 0.461),
        fontsize=8.5, ha="left",
        arrowprops=dict(arrowstyle="->", color="#0369a1", lw=0.8),
    )
    ax2.annotate("$\\leftarrow$ filament_like 0.4980", xy=(2, 0.498),
                 xytext=(2.1, 0.461),
                 fontsize=8.5, ha="left", color="#0369a1",
                 arrowprops=dict(arrowstyle="->", color="#0369a1", lw=0.8))
    ax2.legend(loc="upper right", fontsize=8.5, frameon=True)
    fig.suptitle("T-Web vs Tempel FoF cross-validation: per-class CW fraction "
                 "with 95% Jeffreys binomial CI",
                 fontsize=11.5, y=0.99)
    fig.tight_layout()
    out = FIG_DIR / "fig_p5_vweb_vs_tempel_overlay.png"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {out.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
