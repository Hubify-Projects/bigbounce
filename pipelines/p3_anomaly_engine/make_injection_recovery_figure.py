#!/usr/bin/env python3
"""
Generate publication-quality injection-recovery figure for Paper 3.

Shows amplitude-sweep recovery curves for all 6 surveys with gate
thresholds and PASS/FAIL annotations. Single-column revtex4-2 width.
"""

import json
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE = "/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/pathc_injection_recovery"
OUT_DIR = "/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/figures_p3"
os.makedirs(OUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------
def load_json(fname):
    with open(os.path.join(BASE, fname)) as f:
        return json.load(f)

sdss_em   = load_json("injection_recovery_sdss_native.json")
sdss_cont = load_json("injection_recovery_continuum_sdss_native.json")
lam_em    = load_json("injection_recovery_lamost_native.json")
lam_cont  = load_json("injection_recovery_continuum_lamost_native.json")
erosita   = load_json("injection_recovery_erosita.json")
gaia      = load_json("injection_recovery_gaia.json")

# Nominal x-axis amplitudes
AMPS = [0.5, 1.0, 2.0, 5.0, 10.0, 20.0]
LABELS = ["0.5×", "1×", "2×", "5×", "10×", "20×"]

def curve_from_levels(data):
    """Extract recovery fractions from JSON with 'levels' key (spectral files)."""
    keys = ["0.5x", "1.0x", "2.0x", "5.0x", "10.0x", "20.0x"]
    return [data["levels"][k]["recovery_fraction"] for k in keys]

def curve_from_amp_curve(data):
    """Extract recovery fractions from JSON with 'amplitude_recovery_curve' key."""
    keys = ["0.5x", "1x", "2x", "5x", "10x", "20x"]
    return [data["amplitude_recovery_curve"][k] for k in keys]

# Build per-survey records
surveys = [
    {
        "label": "SDSS DR18\n(continuum-dip)",
        "label_short": "SDSS\ncont.-dip",
        "fracs": curve_from_levels(sdss_cont),
        "gate_pass": sdss_cont["gate_pass"],
        "color": "#2166ac",   # blue
        "ls": "-",
        "marker": "o",
    },
    {
        "label": "SDSS DR18\n(emission-line)",
        "label_short": "SDSS\nem.-line",
        "fracs": curve_from_levels(sdss_em),
        "gate_pass": sdss_em["gate_pass"],
        "color": "#4393c3",   # light blue
        "ls": "--",
        "marker": "s",
    },
    {
        "label": "LAMOST DR10\n(continuum-dip)",
        "label_short": "LAMOST\ncont.-dip",
        "fracs": curve_from_levels(lam_cont),
        "gate_pass": lam_cont["gate_pass"],
        "color": "#d6604d",   # red
        "ls": "-",
        "marker": "o",
    },
    {
        "label": "LAMOST DR10\n(emission-line)",
        "label_short": "LAMOST\nem.-line",
        "fracs": curve_from_levels(lam_em),
        "gate_pass": lam_em["gate_pass"],
        "color": "#f4a582",   # light red
        "ls": "--",
        "marker": "s",
    },
    {
        "label": "eROSITA DR1\n(latent IF)",
        "label_short": "eROSITA\nlatent IF",
        "fracs": curve_from_amp_curve(erosita),
        "gate_pass": erosita["gate_pass"],
        "color": "#4d9221",   # green
        "ls": "-.",
        "marker": "^",
    },
    {
        "label": "Gaia DR3\n(variab. IF)",
        "label_short": "Gaia\nvariab. IF",
        "fracs": curve_from_amp_curve(gaia),
        "gate_pass": gaia["gate_pass"],
        "color": "#762a83",   # purple
        "ls": ":",
        "marker": "D",
    },
]

# ---------------------------------------------------------------------------
# Figure layout
# ---------------------------------------------------------------------------
# revtex4-2 single-column: 3.375 inches wide.  Height ~2.8 for a clean ratio.
FIG_W = 3.375
FIG_H = 3.0

plt.rcParams.update({
    "font.family":        "serif",
    "font.size":          7.5,
    "axes.labelsize":     8.0,
    "axes.titlesize":     8.5,
    "xtick.labelsize":    7.0,
    "ytick.labelsize":    7.0,
    "legend.fontsize":    6.2,
    "legend.framealpha":  0.9,
    "legend.edgecolor":   "0.75",
    "axes.linewidth":     0.7,
    "xtick.major.width":  0.6,
    "ytick.major.width":  0.6,
    "xtick.minor.width":  0.4,
    "ytick.minor.width":  0.4,
    "lines.linewidth":    1.3,
    "lines.markersize":   4.0,
    "figure.dpi":         300,
    "savefig.dpi":        300,
    "savefig.bbox":       "tight",
    "savefig.pad_inches": 0.02,
    "pdf.fonttype":       42,  # embed fonts as Type 1 / TrueType
    "ps.fonttype":        42,
})

fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))

# x positions (log-spaced labels but plotted at integer indices for clarity)
x = np.arange(len(AMPS))

# ---------------------------------------------------------------------------
# Reference lines (draw first so they sit behind data)
# ---------------------------------------------------------------------------
# 50 % gate threshold
ax.axhline(50.0, color="0.35", lw=0.9, ls="--", zorder=1, label="50% gate")

# 5× noise evaluation point: index 3 in AMPS=[0.5,1,2,5,10,20]
ax.axvline(3, color="0.55", lw=0.8, ls=":", zorder=1, label="5× eval pt.")

# Light fill above gate for visual reference
ax.axhspan(50.0, 105.0, color="0.93", zorder=0)

# ---------------------------------------------------------------------------
# Survey curves
# ---------------------------------------------------------------------------
for sv in surveys:
    y = [f * 100.0 for f in sv["fracs"]]
    ax.plot(x, y,
            color=sv["color"],
            ls=sv["ls"],
            marker=sv["marker"],
            markerfacecolor=sv["color"],
            markeredgewidth=0.5,
            markeredgecolor="white",
            zorder=3,
            label=sv["label"])

# ---------------------------------------------------------------------------
# PASS / FAIL annotations at the 5× point (x=3)
# ---------------------------------------------------------------------------
# Determine vertical offset to avoid stacking labels on top of one another.
# Collect (y_at_5x, gate_pass, short_label) and sort by y so annotations
# are placed from bottom to top with nudges as needed.

eval_points = []
for sv in surveys:
    y5 = sv["fracs"][3] * 100.0   # index 3 = 5×
    eval_points.append({
        "y": y5,
        "pass": sv["gate_pass"],
        "short": sv["label_short"],
        "color": sv["color"],
    })

# Sort by y value
eval_points.sort(key=lambda d: d["y"])

# Assign text y positions with a minimum gap of 5 percentage-point units
min_gap = 6.0
text_ys = []
for ep in eval_points:
    if not text_ys:
        text_ys.append(ep["y"])
    else:
        next_y = max(ep["y"], text_ys[-1] + min_gap)
        text_ys.append(next_y)

# --- nudge pass group above 50 if any overlap would be confusing ---
# (simple approach: just use the computed text_ys directly)

for ep, ty in zip(eval_points, text_ys):
    verdict = "PASS" if ep["pass"] else u"FAIL\u2217"
    # small box annotation
    ax.annotate(
        verdict,
        xy=(3, ep["y"]),
        xytext=(3.25, ty),
        fontsize=5.0,
        color=ep["color"],
        fontweight="bold" if ep["pass"] else "normal",
        va="center",
        ha="left",
        arrowprops=dict(
            arrowstyle="-",
            color=ep["color"],
            lw=0.5,
            shrinkA=2,
            shrinkB=2,
        ),
        zorder=5,
    )

# ---------------------------------------------------------------------------
# Axes formatting
# ---------------------------------------------------------------------------
ax.set_xlim(-0.5, 5.7)
ax.set_ylim(-4.0, 108.0)

ax.set_xticks(x)
ax.set_xticklabels(LABELS)
ax.set_xlabel(r"Injection amplitude ($\times$ noise $\sigma$)")
ax.set_ylabel("Recovery fraction (%)")

ax.yaxis.set_major_locator(ticker.MultipleLocator(25))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(12.5))
ax.set_yticks([0, 25, 50, 75, 100])
ax.set_yticklabels(["0", "25", "50", "75", "100"])

# No top/right spines (academic style)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Tick marks inward
ax.tick_params(axis="both", direction="in", which="both",
               top=False, right=False)

# Legend (two-column to save space)
leg = ax.legend(
    loc="upper left",
    ncol=1,
    handlelength=2.0,
    columnspacing=0.8,
    handletextpad=0.4,
    borderpad=0.5,
    frameon=True,
)

# Add gate-line entries to legend
# (they're already labeled in the axhline/axvline calls above)

# ---------------------------------------------------------------------------
# Footnote for FAIL* explanation
# ---------------------------------------------------------------------------
ax.text(
    0.01, -0.13,
    u"\u2217FAIL-with-diagnostic: gate not cleared but companion XV metric confirms\n"
    u"detector stability (eROSITA 81.5\u202f%, Gaia 41\u202f%, LAMOST 9.7\u00d7 cont./em.).",
    transform=ax.transAxes,
    fontsize=4.8,
    va="top",
    ha="left",
    color="0.4",
    linespacing=1.4,
)

fig.tight_layout(rect=[0, 0.07, 1, 1])

# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------
pdf_path = os.path.join(OUT_DIR, "fig_injection_recovery.pdf")
png_path = os.path.join(OUT_DIR, "fig_injection_recovery.png")

fig.savefig(pdf_path, format="pdf")
fig.savefig(png_path, format="png")

print(f"Saved PDF: {pdf_path}")
print(f"Saved PNG: {png_path}")
plt.close(fig)
