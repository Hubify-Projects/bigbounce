#!/usr/bin/env python3
"""
regen_fig_cw_by_env_bar.py

R1 closure item R16 (P4' truth-audit, ROUND_2026-09-02-P4P-v4P.0.1-EXACTPDF-a9cc2618-R1):
fig_p5_cw_by_env_bar.png's baked-in legend read "Paper IV global f_CW=0.4974" --
an undefined internal series label with no meaning to a standalone reader.
This script is a P4'-local, non-mutating regeneration of that figure: it reads
the SAME committed P5 CSV (pipelines/p5_desi_chirality/results/analysis_cosmic_web/
cw_fraction_by_env__desi_env_vweb.csv) with the SAME plotting logic as
pipelines/p5_desi_chirality/scripts/11_make_p5_paper_figures.py::fig_cw_by_env_bar,
changing only the legend label to a reader-comprehensible one. It writes ONLY
into pipelines/p4prime_chirality_test/paper/ -- it does not touch the P5
source repo's own figure or script.

No plotted value changes: same CSV, same bars, same 95% Jeffreys CI, same
reference line at 0.4974 (P4's catalog-wide global f_CW; P4 Sec. "Catalog",
Table cw_frac).
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import beta as beta_dist

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif", "Times New Roman", "Computer Modern Roman"],
    "savefig.dpi": 300,
    "figure.dpi": 300,
})
SAVE_DPI = 300

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent
CW_BY_ENV = (
    REPO / "pipelines" / "p5_desi_chirality" / "results" / "analysis_cosmic_web"
    / "cw_fraction_by_env__desi_env_vweb.csv"
)
OUT = HERE / "fig_p5_cw_by_env_bar.png"

ENV_ORDER = ["void", "wall", "filament", "cluster"]
ENV_COLORS = {
    "void": "#cbd5e1",
    "wall": "#94a3b8",
    "filament": "#64748b",
    "cluster": "#475569",
}


def _binomial_ci_95(n_cw: int, n: int) -> tuple[float, float]:
    """Jeffreys 95% credible interval on the binomial p."""
    if n == 0:
        return (float("nan"), float("nan"))
    a, b = 0.5 + n_cw, 0.5 + (n - n_cw)
    return beta_dist.ppf(0.025, a, b), beta_dist.ppf(0.975, a, b)


def main() -> None:
    df = pd.read_csv(CW_BY_ENV).set_index("env_class").reindex(ENV_ORDER)
    fig, ax = plt.subplots(figsize=(5.8, 4.2))
    xs = np.arange(len(ENV_ORDER))
    yvals = df["cw_fraction"].to_numpy()
    cis = [_binomial_ci_95(int(r["n_cw"]), int(r["n"])) for _, r in df.iterrows()]
    yerr_lo = yvals - np.array([c[0] for c in cis])
    yerr_hi = np.array([c[1] for c in cis]) - yvals
    ax.bar(xs, yvals, color=[ENV_COLORS[e] for e in ENV_ORDER],
           edgecolor="black", linewidth=0.8, alpha=0.85)
    ax.errorbar(xs, yvals, yerr=[yerr_lo, yerr_hi], fmt="none",
                ecolor="black", elinewidth=1.1, capsize=4)
    ax.axhline(0.5, linestyle="--", color="#94a3b8", linewidth=1.1,
               label="parity ($f_{\\rm CW}=0.5$)")
    ax.axhline(0.4974, linestyle=":", color="#dc2626", linewidth=1.0,
               label="catalog global $\\bar f_{\\rm CW}=0.4974$")
    ax.set_ylim(0.43, 0.53)
    ax.set_xticks(xs)
    ax.set_xticklabels([f"{e.title()}\n$n$={int(df.loc[e,'n']):,}" for e in ENV_ORDER],
                       fontsize=9)
    ax.set_ylabel("CW fraction $f_{\\rm CW}$", fontsize=10)
    ax.set_title("CW fraction per cosmic-web class (canonical T-Web,\n"
                 "$n=812{,}793$ env-labeled rows)",
                 fontsize=11)
    ax.legend(loc="upper right", fontsize=8.5, frameon=True)
    fig.tight_layout()
    fig.savefig(OUT, dpi=SAVE_DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
