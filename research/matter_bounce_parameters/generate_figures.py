#!/usr/bin/env python3
"""
Generate 3 paper-ready figures for the matter-bounce parameter connection.

1. B_NL shape slices: bounce vs local across triangle configurations
2. Template overlap robustness: r across 10 weighting schemes
3. Forecast significance: naive vs template-corrected
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# ── Style ──
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 11,
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'figure.dpi': 200,
})

OUTDIR = '/Users/houstongolden/Desktop/CODE_2026/bigbounce/public/images'

# ── Cai shape function (verified polynomial) ──
PREFACTOR = 3.0 / 256.0
C = (2, 7, 3, -12, -69, 19)

def compute_sums(k1, k2, k3):
    ks = [k1, k2, k3]
    pk2 = k1**2 * k2**2 * k3**2
    sk3 = k1**3 + k2**3 + k3**3
    s9 = sum(k**9 for k in ks)
    s72 = sum(ks[i]**7 * ks[j]**2 for i in range(3) for j in range(3) if i != j)
    s63 = sum(ks[i]**6 * ks[j]**3 for i in range(3) for j in range(3) if i != j)
    s54 = sum(ks[i]**5 * ks[j]**4 for i in range(3) for j in range(3) if i != j)
    s522 = sum(ks[i]**5 * ks[j]**2 * ks[l]**2
              for i in range(3) for j in range(3) for l in range(3)
              if i != j and j != l and i != l)
    s432 = sum(ks[i]**4 * ks[j]**3 * ks[l]**2
              for i in range(3) for j in range(3) for l in range(3)
              if i != j and j != l and i != l)
    return s9, s72, s63, s54, s522, s432, pk2, sk3

def BNL(k1, k2, k3):
    s9, s72, s63, s54, s522, s432, pk2, sk3 = compute_sums(k1, k2, k3)
    bracket = C[0]*s9 + C[1]*s72 + C[2]*s63 + C[3]*s54 + C[4]*s522 + C[5]*s432
    AT = (PREFACTOR / pk2) * bracket
    return (10.0 / 3.0) * AT / sk3


# ═══════════════════════════════════════════════════════
# FIGURE 1: B_NL Shape Slices — Bounce vs Local
# ═══════════════════════════════════════════════════════

def fig1_shape_slices():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

    # Slice 1: k1=1, k2=1, k3 varies (squeezed series)
    x3_vals = np.linspace(0.01, 1.0, 200)
    bnl_bounce = [BNL(1.0, 1.0, x3) for x3 in x3_vals]
    bnl_local = [-35/8] * len(x3_vals)

    ax1.plot(x3_vals, bnl_bounce, 'k-', linewidth=2, label='Matter bounce')
    ax1.plot(x3_vals, bnl_local, '--', color='#2563eb', linewidth=1.5, label='Local template')
    ax1.fill_between(x3_vals, bnl_bounce, bnl_local, alpha=0.08, color='#dc2626')
    ax1.axhline(-35/8, color='#999', linewidth=0.5, linestyle=':')
    ax1.set_xlabel(r'$k_3 / k_1$  (squeeze ratio)', fontsize=11)
    ax1.set_ylabel(r'$|B|_{\rm NL}$', fontsize=12)
    ax1.set_title(r'Squeezed series: $k_1 = k_2 = 1$, $k_3$ varies', fontsize=10)
    ax1.legend(fontsize=9, loc='lower right')
    ax1.set_ylim(-4.6, -3.5)
    ax1.annotate(r'$-35/8$', xy=(0.05, -4.375), fontsize=9, color='#2563eb')

    # Slice 2: k1=1, k2=k3=x (isosceles/folded series)
    x_vals = np.linspace(0.5, 1.0, 200)
    bnl_iso = [BNL(1.0, x, x) for x in x_vals]
    bnl_local2 = [-35/8] * len(x_vals)

    ax2.plot(x_vals, bnl_iso, 'k-', linewidth=2, label='Matter bounce')
    ax2.plot(x_vals, bnl_local2, '--', color='#2563eb', linewidth=1.5, label='Local template')
    ax2.fill_between(x_vals, bnl_iso, bnl_local2, alpha=0.08, color='#dc2626')

    # Mark special points
    ax2.plot(0.5, -2.25, 'v', color='#16a34a', markersize=10, zorder=5)
    ax2.annotate('Folded\n$-9/4$', xy=(0.5, -2.25), xytext=(0.56, -2.5),
                fontsize=8, color='#16a34a', arrowprops=dict(arrowstyle='->', color='#16a34a', lw=0.8))
    ax2.plot(1.0, BNL(1,1,1), 's', color='#f59e0b', markersize=8, zorder=5)
    ax2.annotate('Equilateral\n$-255/64$', xy=(1.0, BNL(1,1,1)), xytext=(0.82, -3.5),
                fontsize=8, color='#f59e0b', arrowprops=dict(arrowstyle='->', color='#f59e0b', lw=0.8))

    ax2.set_xlabel(r'$k_2/k_1 = k_3/k_1$', fontsize=11)
    ax2.set_ylabel(r'$|B|_{\rm NL}$', fontsize=12)
    ax2.set_title(r'Isosceles series: $k_1 = 1$, $k_2 = k_3 = x$', fontsize=10)
    ax2.legend(fontsize=9, loc='lower right')
    ax2.set_ylim(-4.8, -1.8)
    ax2.annotate('63% shape\nvariation', xy=(0.65, -3.3), fontsize=9, color='#dc2626',
                fontweight='bold', ha='center')

    fig.suptitle(r'Matter-bounce $|B|_{\rm NL}$ vs local template (constant $= -35/8$)',
                fontsize=12, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(f'{OUTDIR}/fig_bnl_shape_slices.png', bbox_inches='tight', dpi=200)
    print(f"  Saved: fig_bnl_shape_slices.png")
    plt.close()


# ═══════════════════════════════════════════════════════
# FIGURE 2: Template Overlap Robustness
# ═══════════════════════════════════════════════════════

def fig2_overlap_robustness():
    # Data from robustness audit
    weights = [
        ("Flat", 0.835),
        ("CMB Fisher", 0.876),
        ("CMB+noise", 0.879),
        ("LSS SDB", 0.829),
        ("LSS hard", 0.831),
        ("SPHEREx", 0.830),
        ("MegaMapper", 0.828),
        ("Equil masked", 0.821),
        ("Squeezed only", 0.827),
        ("No squeezed", 0.835),
    ]

    names = [w[0] for w in weights]
    vals = [w[1] for w in weights]

    fig, ax = plt.subplots(figsize=(10, 5))

    colors = ['#1a1a1a'] * 7 + ['#999'] * 3  # main weights dark, extreme cuts gray
    bars = ax.barh(range(len(names)), vals, color=colors, edgecolor='white', height=0.7)

    # Mean and range band
    mean_r = np.mean(vals[:7])
    std_r = np.std(vals[:7])
    ax.axvline(mean_r, color='#dc2626', linewidth=1.5, linestyle='-', label=f'Mean = {mean_r:.3f}')
    ax.axvspan(mean_r - std_r, mean_r + std_r, alpha=0.1, color='#dc2626',
               label=f'±1σ = ±{std_r:.3f}')

    ax.set_yticks(range(len(names)))
    ax.set_yticklabels(names, fontsize=10)
    ax.set_xlabel('Amplitude recovery factor  $r$', fontsize=12)
    ax.set_xlim(0.79, 0.91)
    ax.legend(fontsize=9, loc='lower right')
    ax.invert_yaxis()

    # Add value labels
    for i, (n, v) in enumerate(weights):
        ax.text(v + 0.002, i, f'{v:.3f}', va='center', fontsize=9, color='#333')

    ax.set_title(r'Template overlap $r$ across 10 weighting schemes', fontsize=12, fontweight='bold')
    ax.text(0.80, 9.5, 'Gray = extreme cuts\n(adversarial tests)', fontsize=8, color='#999')

    plt.tight_layout()
    plt.savefig(f'{OUTDIR}/fig_template_overlap_robustness.png', bbox_inches='tight', dpi=200)
    print(f"  Saved: fig_template_overlap_robustness.png")
    plt.close()


# ═══════════════════════════════════════════════════════
# FIGURE 3: Forecast Comparison — Naive vs Corrected
# ═══════════════════════════════════════════════════════

def fig3_forecast_comparison():
    r = 0.876  # CMB Fisher

    surveys = [
        ("Planck\n2018", 5.1),
        ("Planck\n+DESI", 4.1),
        ("AI\ntracers", 2.5),
        ("Simons\nObs.", 2.0),
        ("SPHEREx", 0.7),
        ("CMB-S4", 0.5),
        ("Mega-\nMapper", 0.5),
    ]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), gridspec_kw={'width_ratios': [3, 2]})

    names = [s[0] for s in surveys]
    sigmas = [s[1] for s in surveys]

    # Significance if f_NL = -35/8
    sig_naive = [abs(-35/8) / s for s in sigmas]
    sig_corr = [abs(-35/8) * r / s for s in sigmas]

    # Significance if f_NL = -35/16
    sig_naive_alt = [abs(-35/16) / s for s in sigmas]
    sig_corr_alt = [abs(-35/16) * r / s for s in sigmas]

    x = np.arange(len(names))
    w = 0.35

    ax1.bar(x - w/2, sig_naive, w, color='#e5e5e5', edgecolor='#999', label=r'Naive ($f_{\rm NL} = -35/8$)')
    ax1.bar(x + w/2, sig_corr, w, color='#1a1a1a', edgecolor='#333', label=r'Template-corrected ($r = 0.876$)')

    ax1.axhline(5, color='#16a34a', linewidth=1, linestyle='--', alpha=0.5)
    ax1.text(6.3, 5.15, r'$5\sigma$', fontsize=8, color='#16a34a')
    ax1.axhline(3, color='#f59e0b', linewidth=1, linestyle='--', alpha=0.5)
    ax1.text(6.3, 3.15, r'$3\sigma$', fontsize=8, color='#f59e0b')

    ax1.set_xticks(x)
    ax1.set_xticklabels(names, fontsize=9)
    ax1.set_ylabel(r'Detection significance ($\sigma$)', fontsize=11)
    ax1.legend(fontsize=8, loc='upper left')
    ax1.set_title(r'If $f_{\rm NL} = -35/8 = -4.375$ (canonical)', fontsize=11, fontweight='bold')
    ax1.set_ylim(0, 14)

    # Right panel: -35/8 vs -35/16 (template-corrected only)
    ax2.bar(x - w/2, sig_corr, w, color='#1a1a1a', edgecolor='#333', label=r'$-35/8$ (corrected)')
    ax2.bar(x + w/2, sig_corr_alt, w, color='#bbb', edgecolor='#999', label=r'$-35/16$ (corrected)')

    ax2.axhline(5, color='#16a34a', linewidth=1, linestyle='--', alpha=0.5)
    ax2.axhline(3, color='#f59e0b', linewidth=1, linestyle='--', alpha=0.5)

    ax2.set_xticks(x)
    ax2.set_xticklabels(names, fontsize=9)
    ax2.legend(fontsize=8, loc='upper left')
    ax2.set_title(r'Normalization sensitivity ($-35/8$ vs $-35/16$)', fontsize=11, fontweight='bold')
    ax2.set_ylim(0, 14)

    fig.suptitle('Survey forecast significance: template mismatch and normalization impact',
                fontsize=12, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(f'{OUTDIR}/fig_forecast_template_corrected.png', bbox_inches='tight', dpi=200)
    print(f"  Saved: fig_forecast_template_corrected.png")
    plt.close()


# ═══════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════

if __name__ == '__main__':
    print("Generating matter-bounce parameter figures...")
    fig1_shape_slices()
    fig2_overlap_robustness()
    fig3_forecast_comparison()
    print("Done.")
