#!/usr/bin/env python3
"""P5 paper figure generation — cron fire #4, 2026-05-21.

Builds three figures backed by on-disk Phase 1 + Phase 2 artifacts:
    fig_p5_volume_fractions_pie.png   — V-Web canonical run volume fractions
    fig_p5_cw_by_env_bar.png          — CW fraction per env class + 95% binomial CI
    fig_p5_phase2_sensitivity_heatmap.png — per-cell range of CW fraction across
                                            the 9 (R_s, lambda_th) sweep cells

Inputs:
    pipelines/p5_desi_chirality/env_finder/reports/01_volume_fractions.json
    pipelines/p5_desi_chirality/results/analysis_cosmic_web/cw_fraction_by_env__desi_env_vweb.csv
    pipelines/p5_desi_chirality/env_finder/reports/02_phase2_sweep.csv

Output figures:
    pipelines/p5_desi_chirality/figures/fig_p5_volume_fractions_pie.png
    pipelines/p5_desi_chirality/figures/fig_p5_cw_by_env_bar.png
    pipelines/p5_desi_chirality/figures/fig_p5_phase2_sensitivity_heatmap.png
"""
from __future__ import annotations

import json
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

VOLFRAC = P5 / "env_finder/reports/01_volume_fractions.json"
CW_BY_ENV = P5 / "results/analysis_cosmic_web/cw_fraction_by_env__desi_env_vweb.csv"
PHASE2_CSV = P5 / "env_finder/reports/02_phase2_sweep.csv"

ENV_ORDER = ["void", "wall", "filament", "cluster"]
ENV_COLORS = {
    "void": "#cbd5e1",
    "wall": "#94a3b8",
    "filament": "#64748b",
    "cluster": "#475569",
}


def fig_volume_fractions_pie() -> None:
    data = json.loads(VOLFRAC.read_text())
    frac = data["volume_fractions_in_footprint"]
    fig, ax = plt.subplots(figsize=(5.2, 4.4))
    sizes = [frac[e] for e in ENV_ORDER]
    colors = [ENV_COLORS[e] for e in ENV_ORDER]
    labels = [f"{e.title()}\n{100*frac[e]:.1f}%" for e in ENV_ORDER]
    wedges, texts = ax.pie(
        sizes, labels=labels, colors=colors,
        startangle=90, counterclock=False,
        wedgeprops=dict(linewidth=1.5, edgecolor="white"),
        textprops=dict(fontsize=10),
    )
    ax.set_title(
        "V-Web volume fractions, in-footprint mask\n"
        f"($R_s=25$\\,Mpc/$h$, $\\lambda_{{\\rm th}}=0$, $N_{{\\rm grid}}=256^3$)",
        fontsize=11,
    )
    fig.tight_layout()
    out = FIG_DIR / "fig_p5_volume_fractions_pie.png"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {out.relative_to(REPO)}")


def _binomial_ci_95(n_cw: int, n: int) -> tuple[float, float]:
    """Jeffreys 95% credible interval on the binomial p."""
    if n == 0:
        return (float("nan"), float("nan"))
    a, b = 0.5 + n_cw, 0.5 + (n - n_cw)
    return beta_dist.ppf(0.025, a, b), beta_dist.ppf(0.975, a, b)


def fig_cw_by_env_bar() -> None:
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
               label="Paper IV global $\\bar f_{\\rm CW}=0.4974$")
    ax.set_ylim(0.43, 0.53)
    ax.set_xticks(xs)
    ax.set_xticklabels([f"{e.title()}\n$n$={int(df.loc[e,'n']):,}" for e in ENV_ORDER],
                       fontsize=9)
    ax.set_ylabel("CW fraction $f_{\\rm CW}$", fontsize=10)
    ax.set_title("CW fraction per cosmic-web class (canonical V-Web,\n"
                 "$n=791{,}635$ chirality-relevant matched spirals)",
                 fontsize=11)
    ax.legend(loc="upper right", fontsize=8.5, frameon=True)
    fig.tight_layout()
    out = FIG_DIR / "fig_p5_cw_by_env_bar.png"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {out.relative_to(REPO)}")


def fig_phase2_sensitivity_heatmap() -> None:
    df = pd.read_csv(PHASE2_CSV)
    # range per cell across env classes
    rng_by_cell = df.groupby(["R_s_mpc_h", "lambda_th"])["cw_fraction"].agg(
        lambda x: float(x.max() - x.min())
    ).reset_index()
    pivot = rng_by_cell.pivot(index="R_s_mpc_h", columns="lambda_th",
                              values="cw_fraction")
    pivot = pivot.sort_index(ascending=False)  # higher R_s on top
    fig, ax = plt.subplots(figsize=(5.2, 4.0))
    im = ax.imshow(pivot.values * 100,  # → percentage points
                   cmap="viridis", aspect="auto")
    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label("$f_{\\rm CW}$ range across env (pp)", fontsize=10)
    # annotate cells
    for i in range(pivot.shape[0]):
        for j in range(pivot.shape[1]):
            ax.text(j, i, f"{pivot.values[i,j]*100:.2f}",
                    ha="center", va="center", color="white",
                    fontsize=9, fontweight="bold")
    ax.set_xticks(range(pivot.shape[1]))
    ax.set_xticklabels([f"{l:g}" for l in pivot.columns], fontsize=10)
    ax.set_yticks(range(pivot.shape[0]))
    ax.set_yticklabels([f"{r:g}" for r in pivot.index], fontsize=10)
    ax.set_xlabel("$\\lambda_{\\rm th}$ (eigenvalue threshold)", fontsize=10)
    ax.set_ylabel("$R_s$ (Mpc/$h$)", fontsize=10)
    ax.set_title("Phase 2 sensitivity: per-cell range of $f_{\\rm CW}$\n"
                 "across {void, wall, filament, cluster}", fontsize=11)
    fig.tight_layout()
    out = FIG_DIR / "fig_p5_phase2_sensitivity_heatmap.png"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {out.relative_to(REPO)}")


def main() -> int:
    if not VOLFRAC.exists() or not CW_BY_ENV.exists() or not PHASE2_CSV.exists():
        print("[FATAL] one or more inputs missing")
        return 1
    fig_volume_fractions_pie()
    fig_cw_by_env_bar()
    fig_phase2_sensitivity_heatmap()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
