#!/usr/bin/env python3
"""
Generate comparison figures for two frozen MCMC datasets.

Datasets:
  full_tension    — 175,545 samples, 6 chains
  planck_bao_sn   — 132,949 samples, 6 chains

Outputs (PNG 300 dpi + PDF):
  paper/figures/cosmology_dataset_comparison_two_frozen.{png,pdf}
  paper/figures/fig_dneff_viability_two_frozen.{png,pdf}
  public/images/fig_dneff_viability_two_frozen.png  (copy)
"""

import os
import shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from scipy.stats import norm

# ── paths ──────────────────────────────────────────────────────────────
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
FIG_DIR = os.path.join(ROOT, "paper", "figures")
IMG_DIR = os.path.join(ROOT, "public", "images")
os.makedirs(FIG_DIR, exist_ok=True)
os.makedirs(IMG_DIR, exist_ok=True)

# ── data ───────────────────────────────────────────────────────────────
datasets = {
    "full_tension": {
        "label": "Full tension\n(175 545 samples)",
        "color": "#2166ac",
        "marker": "o",
        "H0":        (67.68, 0.97),
        "delta_neff":(-0.020, 0.17),
        "sigma8":    (0.803, 0.008),
        "S8":        (0.828, 0.016),
        "omegam":    (0.308, 0.006),
        "tau":       (0.054, 0.007),
        "ns":        (0.965, 0.004),
    },
    "planck_bao_sn": {
        "label": "Planck+BAO+SN\n(132 949 samples)",
        "color": "#b2182b",
        "marker": "s",
        "H0":        (67.79, 1.09),
        "delta_neff":(0.065, 0.17),
        "sigma8":    (0.812, 0.009),
        "S8":        (0.831, 0.018),
        "omegam":    (0.312, 0.006),
        "tau":       (0.056, 0.007),
        "ns":        (0.967, 0.006),
    },
}

pending = ["Planck-only\n(pending)", "Planck+BAO\n(pending)"]

refs = {
    "SH0ES":       {"H0": (73.04, 1.04)},
    "Planck 2018": {"H0": (67.36, 0.54)},
    "DES Y3":      {"S8": (0.776, 0.017)},
}

# ── publication style ──────────────────────────────────────────────────
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.linewidth": 0.8,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.major.size": 4,
    "ytick.major.size": 4,
    "legend.frameon": True,
    "legend.framealpha": 0.9,
    "legend.edgecolor": "0.8",
    "figure.dpi": 150,
})


# =====================================================================
# FIGURE 1 — 3-panel dataset comparison (H0, delta_neff, S8)
# =====================================================================
def fig1_dataset_comparison():
    fig, axes = plt.subplots(1, 3, figsize=(11.5, 4.0))
    fig.subplots_adjust(left=0.07, right=0.97, bottom=0.22, top=0.88, wspace=0.38)

    panels = [
        ("H0",        r"$H_0$ [km s$^{-1}$ Mpc$^{-1}$]", "(a)"),
        ("delta_neff", r"$\Delta N_\mathrm{eff}$",          "(b)"),
        ("S8",        r"$S_8$",                              "(c)"),
    ]

    ref_bands = {
        "H0": [
            ("SH0ES", 73.04, 1.04, "#fee08b", 0.35),
            ("Planck 2018", 67.36, 0.54, "#d1e5f0", 0.45),
        ],
        "delta_neff": [
            ("SM", 0.0, None, None, None),           # vertical line only
            ("BBN 2$\\sigma$", 0.41, None, None, None),  # vertical line only
        ],
        "S8": [
            ("DES Y3", 0.776, 0.017, "#d9f0d3", 0.45),
        ],
    }

    y_positions = [3, 2, 1, 0]  # full_tension, planck_bao_sn, pending1, pending2
    y_labels_all = [
        datasets["full_tension"]["label"],
        datasets["planck_bao_sn"]["label"],
        pending[0],
        pending[1],
    ]

    for ax, (param, xlabel, panel_label) in zip(axes, panels):
        # reference bands / lines
        for entry in ref_bands.get(param, []):
            name, val, err, col, alpha = entry
            if err is not None and col is not None:
                ax.axhspan(-1, 5, xmin=0, xmax=1, alpha=0)  # dummy
                ax.axvspan(val - err, val + err, color=col, alpha=alpha,
                           label=name, zorder=0)
                ax.axvline(val, color="0.45", ls="--", lw=0.6, zorder=1)
            else:
                style = "-" if "SM" in name else ":"
                ax.axvline(val, color="0.35", ls=style, lw=0.9, zorder=1)
                ax.text(val, 3.55, name, ha="center", va="bottom",
                        fontsize=7, color="0.3")

        # frozen datasets
        for i, key in enumerate(["full_tension", "planck_bao_sn"]):
            d = datasets[key]
            mean, std = d[param]
            ax.errorbar(mean, y_positions[i], xerr=std, fmt=d["marker"],
                        color=d["color"], ms=7, capsize=4, capthick=1.2,
                        elinewidth=1.2, zorder=5, label=d["label"] if param == "H0" else None)

        # pending placeholders
        for j, lbl in enumerate(pending):
            yp = y_positions[2 + j]
            ax.plot([], [])  # skip
            ax.annotate("pending", xy=(0.5, yp), xycoords=("axes fraction", "data"),
                        ha="center", va="center", fontsize=8, color="0.55",
                        fontstyle="italic")

        ax.set_yticks(y_positions)
        ax.set_yticklabels(y_labels_all, fontsize=7.5)
        ax.set_ylim(-0.7, 4.2)
        ax.set_xlabel(xlabel, fontsize=10)
        ax.text(0.03, 0.95, panel_label, transform=ax.transAxes,
                fontsize=11, fontweight="bold", va="top")

        if param == "H0":
            ax.legend(loc="lower right", fontsize=6.5, handlelength=1.5)

    fig.suptitle("DRAFT --- 2/4 datasets frozen", fontsize=12, fontweight="bold",
                 color="0.4", y=0.97)

    for ext in ("png", "pdf"):
        path = os.path.join(FIG_DIR, f"cosmology_dataset_comparison_two_frozen.{ext}")
        fig.savefig(path, dpi=300, bbox_inches="tight")
        print(f"  saved {path}")
    plt.close(fig)


# =====================================================================
# FIGURE 2 — 2-panel dNeff viability + whisker comparison
# =====================================================================
def fig2_dneff_viability():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.5))
    fig.subplots_adjust(left=0.08, right=0.96, bottom=0.15, top=0.90, wspace=0.35)

    # ── Panel (a): delta_neff posteriors ──
    x = np.linspace(-0.7, 1.1, 600)

    for key in ["full_tension", "planck_bao_sn"]:
        d = datasets[key]
        mu, sig = d["delta_neff"]
        pdf = norm.pdf(x, mu, sig)
        ax1.plot(x, pdf, color=d["color"], lw=1.8,
                 label=d["label"].replace("\n", " "))
        ax1.fill_between(x, pdf, alpha=0.15, color=d["color"])

    # WP4 regions
    ax1.axvspan(0.05, 0.40, color="#a6dba0", alpha=0.22, label="WP4 reheating [0.05, 0.40]")
    ax1.axvspan(0.01, 0.25, color="#c2a5cf", alpha=0.18, label="WP4 decay [0.01, 0.25]")

    # reference lines
    ax1.axvline(0.0, color="k", ls="-", lw=0.9, label="SM ($\\Delta N_\\mathrm{eff}=0$)")
    ax1.axvline(0.41, color="0.3", ls=":", lw=1.0, label="BBN 2$\\sigma$ upper (0.41)")
    ax1.axvline(0.40, color="#e66101", ls="--", lw=1.0, label="ACT DR6 central (0.40)")

    ax1.set_xlabel(r"$\Delta N_\mathrm{eff}$", fontsize=11)
    ax1.set_ylabel("Probability density", fontsize=10)
    ax1.set_xlim(-0.65, 1.05)
    ax1.set_ylim(bottom=0)
    ax1.legend(fontsize=6.5, loc="upper right", ncol=1)
    ax1.text(0.03, 0.95, "(a)", transform=ax1.transAxes,
             fontsize=12, fontweight="bold", va="top")

    # ── Panel (b): normalized whisker plot ──
    params_order = ["H0", "delta_neff", "sigma8", "S8", "omegam", "tau", "ns"]
    param_labels = [r"$H_0$", r"$\Delta N_\mathrm{eff}$", r"$\sigma_8$",
                    r"$S_8$", r"$\Omega_m$", r"$\tau$", r"$n_s$"]

    y_vals = np.arange(len(params_order))

    for i_ds, key in enumerate(["full_tension", "planck_bao_sn"]):
        d = datasets[key]
        offsets = []
        errs = []
        for p in params_order:
            mu, sig = d[p]
            ft_mu, ft_sig = datasets["full_tension"][p]
            offsets.append((mu - ft_mu) / ft_sig)
            errs.append(sig / ft_sig)

        shift = 0.12 if key == "planck_bao_sn" else -0.12
        ax2.errorbar(offsets, y_vals + shift, xerr=errs,
                     fmt=d["marker"], color=d["color"], ms=6,
                     capsize=3.5, capthick=1.0, elinewidth=1.0,
                     label=d["label"].replace("\n", " "), zorder=5)

    ax2.axvline(0, color="0.6", ls="-", lw=0.7, zorder=0)
    ax2.axvspan(-1, 1, color="0.92", alpha=0.5, zorder=0)
    ax2.set_yticks(y_vals)
    ax2.set_yticklabels(param_labels, fontsize=9.5)
    ax2.set_xlabel(r"$(x - x_\mathrm{full\_tension}) \;/\; \sigma_\mathrm{full\_tension}$",
                   fontsize=9.5)
    ax2.set_xlim(-3.5, 3.5)
    ax2.legend(fontsize=7, loc="lower right")
    ax2.text(0.03, 0.95, "(b)", transform=ax2.transAxes,
             fontsize=12, fontweight="bold", va="top")

    fig.suptitle("DRAFT --- 2/4 datasets frozen", fontsize=12, fontweight="bold",
                 color="0.4", y=0.97)

    for ext in ("png", "pdf"):
        path = os.path.join(FIG_DIR, f"fig_dneff_viability_two_frozen.{ext}")
        fig.savefig(path, dpi=300, bbox_inches="tight")
        print(f"  saved {path}")

    # copy PNG to public/images/
    src = os.path.join(FIG_DIR, "fig_dneff_viability_two_frozen.png")
    dst = os.path.join(IMG_DIR, "fig_dneff_viability_two_frozen.png")
    shutil.copy2(src, dst)
    print(f"  copied {dst}")

    plt.close(fig)


# ── main ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Figure 1: 3-panel dataset comparison")
    fig1_dataset_comparison()
    print()
    print("Figure 2: dNeff viability + whisker comparison")
    fig2_dneff_viability()
    print("\nDone.")
