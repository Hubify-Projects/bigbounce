#!/usr/bin/env python3
"""
Figure: The 14 structural barriers of ECH cosmology, as a publication-quality
table rendered in matplotlib. This is the paper's signature visual.

Renders Table 1 (barriers) as a figure for maximum visual impact.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# ── Data ──
barriers = [
    # (number, name, branch, root_cause, failure_mode)
    ( 1, "Mass-coupling lock",         "A", "m and g locked by single PGT parameter t₃",             "I"),
    ( 2, "Topological-shift duality",  "B", "Shift symmetry ↔ geometric content exclusive",          "I"),
    ( 3, "Scalar-tensor universality", "C", "T₀ = Q₀ = 0 on FRW; only R(g) survives",               "I"),
    ( 4, "Planck suppression",         "D", "1 ∂φ/vertex; disformal needs 2; dim-8 ~ 10⁻¹²²",       "I"),
    ( 5, "Scale separation",           "E", "Bounce ~ 10⁻³² of spacetime volume integrals",          "II"),
    ( 6, "Attractor-sensitivity",      "F", "Attractors erase φᵢ; otherwise 10⁻³⁰ precision needed", "II"),
    ( 7, "Parameter immunity",         "G", "Action params ≠ boundary conditions; cyclic incompatible","II"),
    ( 8, "Parity-even interaction",    "H", "(J⁵)² is parity-even; R̃R = 0 on FRW",                  "III"),
    ( 9, "Phase-space conservation",   "J", "Liouville theorem at H = 0; no contraction",            "IV"),
    (10, "UV–IR specificity",         "L", "Generic mechanisms don't need the bounce",               "III"),
    (11, "Decoupling universality",    "L", "Light torsion: g_eff ~ m_T / M²_Pl",                    "I"),
    (12, "Vacuum amplification\nceiling", "M", "Ω_GW ∝ (H_b/M_Pl)²; gap ≥ 10¹⁷ to detectors",      "III"),
    (13, "Gravitational democracy",    "N", "Torsion ~ 1% of Planck-era channels; B, L conserved",   "V"),
    (14, "Bounce–vacuum decoupling",   "O", "Trigger (bounce) ≠ outcome (ρ_DE)",                     "V"),
]

failure_mode_names = {
    "I":   "Geometric specificity\nlost on FRW",
    "II":  "Scale separation\n(10¹²² hierarchy)",
    "III": "Generic or\nundetectable",
    "IV":  "Hamiltonian\nconservation",
    "V":   "Gravitational\ndemocracy",
}

failure_mode_colors = {
    "I":   "#E15759",   # red
    "II":  "#F28E2B",   # orange
    "III": "#76B7B2",   # teal
    "IV":  "#B07AA1",   # purple
    "V":   "#59A14F",   # green
}

# ── Figure ──
fig, ax = plt.subplots(figsize=(12, 8.5))
ax.set_xlim(0, 12)
ax.set_ylim(-0.5, 15.5)
ax.axis('off')

# Title
ax.text(6.0, 15.2, "Fourteen Structural Barriers of ECH Bounce Cosmology",
        fontsize=15, fontweight='bold', ha='center', va='center')

# Column headers
headers = [
    (0.3,  "#"),
    (1.0,  "Barrier"),
    (4.0,  "Branch"),
    (5.0,  "Physical mechanism"),
    (10.2, "Failure mode"),
]
y_header = 14.4
for x, text in headers:
    ax.text(x, y_header, text, fontsize=10, fontweight='bold', va='center')

ax.plot([0.1, 11.8], [14.0, 14.0], color='black', lw=1.5)

# Rows
for i, (num, name, branch, cause, mode) in enumerate(barriers):
    y = 13.4 - i * 0.97

    # Alternating background
    if i % 2 == 0:
        rect = FancyBboxPatch((0.1, y - 0.42), 11.7, 0.85,
                               boxstyle="round,pad=0.02",
                               facecolor='#f5f5f5', edgecolor='none', zorder=0)
        ax.add_patch(rect)

    # Number
    ax.text(0.4, y, str(num), fontsize=9.5, ha='center', va='center',
            fontweight='bold')

    # Name
    ax.text(1.0, y, name, fontsize=9, va='center')

    # Branch
    ax.text(4.1, y, branch, fontsize=9.5, ha='center', va='center',
            fontweight='bold', color='#333333',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#e0e0e0',
                      edgecolor='#aaaaaa', lw=0.5))

    # Mechanism
    ax.text(5.0, y, cause, fontsize=8.2, va='center', style='italic',
            color='#444444')

    # Failure mode badge
    color = failure_mode_colors[mode]
    ax.text(10.3, y, mode, fontsize=9, ha='center', va='center',
            fontweight='bold', color='white',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=color,
                      edgecolor='none'))

# Bottom line
ax.plot([0.1, 11.8], [0.0, 0.0], color='black', lw=1.0)

# Legend for failure modes
y_leg = -0.4
ax.text(0.3, y_leg, "Failure modes:", fontsize=9, fontweight='bold',
        va='center')
x_leg = 2.2
for mode_key in ["I", "II", "III", "IV", "V"]:
    color = failure_mode_colors[mode_key]
    label = failure_mode_names[mode_key].replace('\n', ' ')
    ax.text(x_leg, y_leg, f"{mode_key}: {label}", fontsize=7.5,
            va='center', color=color, fontweight='bold')
    x_leg += 2.1

fig.tight_layout()

outdir = '/Users/houstongolden/Desktop/CODE_2026/bigbounce/research/final_phase/drafts'
fig.savefig(f'{outdir}/fig_barrier_table.png', dpi=300, bbox_inches='tight')
fig.savefig(f'{outdir}/fig_barrier_table.pdf', dpi=300, bbox_inches='tight')
print(f"Saved to {outdir}/fig_barrier_table.png and .pdf")
