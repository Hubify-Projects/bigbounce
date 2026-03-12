#!/usr/bin/env python3
"""
BigBounce Paper 2 — Figure: Physical viability of the preferred ΔNeff region

Three-panel horizontal layout:
  Panel A: Cosmology posterior distributions for ΔNeff
  Panel B: Observational constraints (BBN, CMB, Paper 1 preferred)
  Panel C: WP4 reheating mechanism realization space

Author: Houston Golden
Generated: 2026-03-06
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.colors import LogNorm, Normalize
import matplotlib.gridspec as gridspec

# ============================================================
# Data
# ============================================================

SNAP = "/Users/houstongolden/Desktop/CODE_2026/bigbounce/research/paper2/archives/paper2_snapshot_20260306_0706"

# Panel A: Current MCMC cohort_main estimates (preliminary)
# Using approximate Gaussian posteriors based on chain means and spread
posteriors = {
    "Planck + BAO": {"mean": 0.114, "sigma": 0.18, "color": "#2166ac", "ls": "-"},
    "Planck + BAO + SN": {"mean": 0.117, "sigma": 0.15, "color": "#b2182b", "ls": "-"},
    "Full tension": {"mean": -0.011, "sigma": 0.12, "color": "#1b7837", "ls": "-"},
}

# Panel B: Observational constraints
constraints = [
    {"label": "Paper 1 preferred", "lo": -0.05, "hi": 0.25, "color": "#fee08b", "rank": 0},
    {"label": "BBN allowed\n(Yeh+ 2022)", "lo": -0.5, "hi": 0.5, "color": "#91bfdb", "rank": 1},
    {"label": "CMB allowed\n(Planck 2018)", "lo": -0.5, "hi": 0.34, "color": "#fc8d59", "rank": 2},
    {"label": "ACT DR6\n(Calabrese+ 2025)", "lo": -0.1, "hi": 0.40, "color": "#d9ef8b", "rank": 3},
]

# Panel C: WP4 reheating scan (T_rh = 1e6 GeV — best fit)
param_g = np.load(f"{SNAP}/paper2/wp4_dneff_microphysics/runs/reheating/param_g_hidden.npy")
param_Br = np.load(f"{SNAP}/paper2/wp4_dneff_microphysics/runs/reheating/param_Br_dr.npy")
dneff_grid = np.load(f"{SNAP}/paper2/wp4_dneff_microphysics/runs/reheating/dneff_grid_Treh_1e+06.npy")
mask_allowed = np.load(f"{SNAP}/paper2/wp4_dneff_microphysics/runs/reheating/mask_allowed_Treh_1e+06.npy")

# ============================================================
# Figure setup
# ============================================================

fig = plt.figure(figsize=(16, 5.5))
gs = gridspec.GridSpec(1, 3, width_ratios=[1.0, 0.6, 1.2], wspace=0.35)

ax_a = fig.add_subplot(gs[0])
ax_b = fig.add_subplot(gs[1])
ax_c = fig.add_subplot(gs[2])

# ============================================================
# Panel A — Cosmology posterior
# ============================================================

dneff_x = np.linspace(-0.6, 0.8, 500)

for label, p in posteriors.items():
    y = np.exp(-0.5 * ((dneff_x - p["mean"]) / p["sigma"]) ** 2)
    y /= y.max()
    ax_a.plot(dneff_x, y, color=p["color"], lw=2.2, ls=p["ls"], label=label)
    ax_a.fill_between(dneff_x, 0, y, alpha=0.08, color=p["color"])

# ΔNeff = 0 reference
ax_a.axvline(0, color="gray", ls="--", lw=1.0, alpha=0.6, zorder=0)

# Preferred region shading
ax_a.axvspan(0.05, 0.25, alpha=0.12, color="#ffcc00", zorder=0, label="Preferred region")

ax_a.set_xlabel(r"$\Delta N_{\rm eff}$", fontsize=13)
ax_a.set_ylabel("Posterior density (normalized)", fontsize=12)
ax_a.set_title("(a) Cosmology posterior", fontsize=13, fontweight="bold", pad=10)
ax_a.set_xlim(-0.5, 0.6)
ax_a.set_ylim(0, 1.15)
ax_a.legend(loc="upper left", fontsize=9, framealpha=0.9)
ax_a.tick_params(labelsize=10)

# ============================================================
# Panel B — Observational constraints
# ============================================================

for c in constraints:
    y = c["rank"]
    ax_b.barh(y, c["hi"] - c["lo"], left=c["lo"], height=0.6,
              color=c["color"], edgecolor="black", linewidth=0.8, alpha=0.85)
    ax_b.text(c["hi"] + 0.02, y, c["label"], va="center", fontsize=8.5)

# Preferred region
ax_b.axvspan(0.05, 0.25, alpha=0.15, color="#ffcc00", zorder=0)
ax_b.axvline(0, color="gray", ls="--", lw=1.0, alpha=0.5)

ax_b.set_xlabel(r"$\Delta N_{\rm eff}$", fontsize=13)
ax_b.set_title("(b) Observational bounds", fontsize=13, fontweight="bold", pad=10)
ax_b.set_xlim(-0.6, 0.9)
ax_b.set_ylim(-0.5, len(constraints) - 0.5)
ax_b.set_yticks([])
ax_b.tick_params(labelsize=10)

# ============================================================
# Panel C — Mechanism realization (WP4 reheating)
# ============================================================

# Create 2D meshgrid for pcolormesh
G, B = np.meshgrid(param_g, param_Br)

# Clip ΔNeff to reasonable range for plotting
dneff_plot = np.clip(dneff_grid, 1e-3, 2.0)

# Plot ΔNeff heatmap
pcm = ax_c.pcolormesh(G, B, dneff_plot, cmap="viridis",
                       norm=LogNorm(vmin=0.01, vmax=1.0),
                       shading="nearest", rasterized=True)

# Contours at target ΔNeff values
try:
    contour_levels = [0.10, 0.15, 0.20]
    cs = ax_c.contour(G, B, dneff_grid, levels=contour_levels,
                       colors=["white", "#ffcc00", "white"],
                       linewidths=[1.5, 2.5, 1.5],
                       linestyles=["--", "-", "--"])
    ax_c.clabel(cs, fmt=r"$\Delta N_{\rm eff}=%.2f$", fontsize=8, inline=True)
except Exception:
    pass

# Mask disallowed region (BBN > 0.5 or CMB > 0.34)
mask_disallowed = ~mask_allowed
ax_c.contourf(G, B, mask_disallowed.astype(float),
              levels=[0.5, 1.5], colors=["black"], alpha=0.3)

# Highlight overlap region (allowed AND in preferred range 0.1-0.2)
preferred_mask = mask_allowed & (dneff_grid >= 0.10) & (dneff_grid <= 0.20)
if preferred_mask.any():
    ax_c.contour(G, B, preferred_mask.astype(float),
                 levels=[0.5], colors=["#ff6600"], linewidths=[2.5])

ax_c.set_xlabel(r"$g_{*,\rm hidden}$", fontsize=13)
ax_c.set_ylabel(r"$\mathrm{Br}_{\rm dr}$", fontsize=13)
ax_c.set_title(r"(c) Reheating mechanism ($T_{\rm rh}=10^6\,$GeV)",
               fontsize=13, fontweight="bold", pad=10)
ax_c.set_yscale("log")
ax_c.tick_params(labelsize=10)

# Colorbar
cbar = fig.colorbar(pcm, ax=ax_c, shrink=0.85, pad=0.02)
cbar.set_label(r"$\Delta N_{\rm eff}$", fontsize=12)
cbar.ax.tick_params(labelsize=9)

# ============================================================
# Draft annotation
# ============================================================

fig.text(0.5, 0.01,
         "Draft figure — parameters and contours will be updated once final MCMC convergence is complete.",
         ha="center", fontsize=9, style="italic", color="gray",
         bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow", edgecolor="gray", alpha=0.7))

# ============================================================
# Overall title
# ============================================================

fig.suptitle("Physical viability of the preferred $\\Delta N_{\\rm eff}$ region",
             fontsize=15, fontweight="bold", y=0.98)

plt.tight_layout(rect=[0, 0.04, 1, 0.94])

# ============================================================
# Save
# ============================================================

pdf_path = "/Users/houstongolden/Desktop/CODE_2026/bigbounce/paper/figures/fig_dneff_viability.pdf"
png_path = "/Users/houstongolden/Desktop/CODE_2026/bigbounce/public/images/dneff_viability.png"

fig.savefig(pdf_path, dpi=300, bbox_inches="tight", backend="pdf")
fig.savefig(png_path, dpi=200, bbox_inches="tight")

print(f"Saved: {pdf_path}")
print(f"Saved: {png_path}")
print("Done.")
