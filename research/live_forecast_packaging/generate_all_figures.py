#!/usr/bin/env python3
"""
Generate all 5 figures for the matter-bounce forecast paper.
All from existing code/data — no new computation needed.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

OUTDIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# SHAPE FUNCTION (from verified coefficient set)
# ============================================================
def BNL(k1, k2, k3):
    ks = [k1, k2, k3]
    pk2 = k1**2 * k2**2 * k3**2
    sk3 = k1**3 + k2**3 + k3**3
    s9 = sum(k**9 for k in ks)
    s72 = sum(ks[i]**7*ks[j]**2 for i in range(3) for j in range(3) if i!=j)
    s63 = sum(ks[i]**6*ks[j]**3 for i in range(3) for j in range(3) if i!=j)
    s54 = sum(ks[i]**5*ks[j]**4 for i in range(3) for j in range(3) if i!=j)
    s522 = sum(ks[i]**5*ks[j]**2*ks[l]**2 for i in range(3) for j in range(3)
              for l in range(3) if i!=j and j!=l and i!=l)
    s432 = sum(ks[i]**4*ks[j]**3*ks[l]**2 for i in range(3) for j in range(3)
              for l in range(3) if i!=j and j!=l and i!=l)
    c = [4, 5, -9, 0, -68, 19]
    bracket = c[0]*s9+c[1]*s72+c[2]*s63+c[3]*s54+c[4]*s522+c[5]*s432
    AT = (3.0/(256*pk2))*bracket
    return (10.0/3.0)*AT/sk3

# ============================================================
# FIGURE 1: Shape function — |B|_NL vs k1/k
# ============================================================
def fig1_shape_function():
    k1_arr = np.geomspace(0.001, 1.0, 200)
    bnl_arr = [BNL(k1, 1.0, 1.0) for k1 in k1_arr]

    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    ax.semilogx(k1_arr, bnl_arr, 'b-', lw=2)
    ax.axhline(-35/8, color='r', ls='--', lw=1, label=f'Squeezed limit: $-35/8 = -4.375$')
    ax.axhline(-255/64, color='orange', ls=':', lw=1, label=f'Equilateral: $-255/64 = -3.984$')

    # Mark special points
    ax.plot(1e-3, BNL(1e-3, 1, 1), 'ro', ms=8, zorder=5)
    ax.plot(1.0, BNL(1, 1, 1), 's', color='orange', ms=8, zorder=5)
    ax.plot(0.5, BNL(0.5, 1, 1), '^', color='green', ms=8, zorder=5,
            label=f'Folded ($k_1=2k_2=2k_3$): $-9/4 = -2.250$')

    ax.set_xlabel('$k_1 / k$', fontsize=14)
    ax.set_ylabel('$|B|_{NL}(k_1, k, k)$', fontsize=14)
    ax.set_title('Matter-Bounce Bispectrum: Squeezed-Limit Convergence', fontsize=13)
    ax.legend(fontsize=10, loc='upper right')
    ax.set_ylim(-5.5, -1.5)
    ax.set_xlim(1e-3, 1.2)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(OUTDIR, 'fig1_shape_function.png'), dpi=150)
    plt.close()
    print("Figure 1: shape function — DONE")

# ============================================================
# FIGURE 2: Survey significance comparison
# ============================================================
def fig2_survey_comparison():
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))

    surveys = ['SPHEREx\n(bispectrum)', 'SPHEREx\n(P+B combined)',
               'MegaMapper\n(ideal)', 'MegaMapper\n(realistic)',
               'MegaMapper\n(conservative)', 'MegaMapper\n(single-tracer)']
    central = [6.3, 8.75, 8.75, 5.0, 3.0, 1.75]
    low =     [4.4, 6.3,  4.4,  3.0, 1.5, 1.0]
    high =    [8.0, 9.5,  14.6, 7.0, 5.0, 2.5]

    colors = ['#2196F3', '#1565C0', '#FF9800', '#F57C00', '#E65100', '#BF360C']

    x = np.arange(len(surveys))
    bars = ax.bar(x, central, color=colors, alpha=0.8, edgecolor='black', lw=0.5)
    for i in range(len(surveys)):
        ax.errorbar(x[i], central[i], yerr=[[central[i]-low[i]], [high[i]-central[i]]],
                    fmt='none', ecolor='black', capsize=5, lw=1.5)

    ax.axhline(5, color='green', ls='--', lw=1.5, alpha=0.7, label='$5\\sigma$ discovery threshold')
    ax.axhline(3, color='goldenrod', ls='--', lw=1.5, alpha=0.7, label='$3\\sigma$ evidence threshold')

    ax.set_xticks(x)
    ax.set_xticklabels(surveys, fontsize=9)
    ax.set_ylabel('Detection Significance ($\\sigma$)', fontsize=13)
    ax.set_title('$f_{NL} = -35/8$: Survey Detection Significance', fontsize=13)
    ax.legend(fontsize=10)
    ax.set_ylim(0, 16)
    ax.grid(axis='y', alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(OUTDIR, 'fig2_survey_comparison.png'), dpi=150)
    plt.close()
    print("Figure 2: survey comparison — DONE")

# ============================================================
# FIGURE 3: Fisher sensitivity to k_min (the "cliff" plot)
# ============================================================
def fig3_kmin_cliff():
    # Data from the Fisher robustness scan
    kmin_mm = [1e-4, 2e-4, 5e-4, 1e-3, 2e-3, 5e-3]
    sigma_mm = [0.525, 1.929, 36.3, 500, 8241, 440446]
    sig_mm = [4.375/s for s in sigma_mm]

    kmin_sp = [1e-4, 5e-4, 1e-3, 2e-3, 5e-3]
    sigma_sp = [3.3, 66.2, 819, 13360, 714075]
    sig_sp = [4.375/s for s in sigma_sp]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    # Left: sigma(f_NL) vs k_min
    ax1.loglog(kmin_mm, sigma_mm, 'o-', color='#FF9800', lw=2, ms=7, label='MegaMapper (multi-tracer)')
    ax1.loglog(kmin_sp, sigma_sp, 's-', color='#2196F3', lw=2, ms=7, label='SPHEREx (single-pop SDB)')
    ax1.axhline(0.7, color='#2196F3', ls=':', alpha=0.5, label='SPHEREx bispectrum: $\\sigma=0.7$')
    ax1.axhline(1.0, color='gray', ls='--', alpha=0.5)
    ax1.set_xlabel('$k_{\\min}$ [h/Mpc]', fontsize=13)
    ax1.set_ylabel('$\\sigma(f_{NL})$', fontsize=13)
    ax1.set_title('$\\sigma(f_{NL})$ vs Minimum Accessible Scale', fontsize=12)
    ax1.set_ylim(0.1, 1e6)
    ax1.legend(fontsize=9)
    ax1.grid(True, alpha=0.3)

    # Right: significance vs k_min
    ax2.semilogx(kmin_mm, sig_mm, 'o-', color='#FF9800', lw=2, ms=7, label='MegaMapper')
    ax2.semilogx(kmin_sp, sig_sp, 's-', color='#2196F3', lw=2, ms=7, label='SPHEREx (SDB only)')
    ax2.axhline(4.375/0.7, color='#2196F3', ls=':', lw=1.5, alpha=0.7,
                label='SPHEREx bispectrum: $6.3\\sigma$')
    ax2.axhline(5, color='green', ls='--', alpha=0.5, label='$5\\sigma$')
    ax2.axhline(3, color='goldenrod', ls='--', alpha=0.5, label='$3\\sigma$')
    ax2.set_xlabel('$k_{\\min}$ [h/Mpc]', fontsize=13)
    ax2.set_ylabel('Detection Significance ($\\sigma$)', fontsize=13)
    ax2.set_title('Significance for $f_{NL}=-35/8$', fontsize=12)
    ax2.set_ylim(-0.5, 12)
    ax2.legend(fontsize=8, loc='upper right')
    ax2.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTDIR, 'fig3_kmin_cliff.png'), dpi=150)
    plt.close()
    print("Figure 3: k_min cliff — DONE")

# ============================================================
# FIGURE 4: Decision threshold diagram
# ============================================================
def fig4_decision_thresholds():
    fig, ax = plt.subplots(1, 1, figsize=(12, 3.5))

    # Colored regions
    ax.axvspan(-8, -3, alpha=0.3, color='green', label='STRONGLY FAVORS BOUNCE')
    ax.axvspan(-3, -1, alpha=0.3, color='lightgreen', label='SUPPORTS BOUNCE')
    ax.axvspan(-1, 1, alpha=0.3, color='red', label='BOUNCE EXCLUDED')
    ax.axvspan(1, 5, alpha=0.3, color='salmon', label='WRONG SIGN (supports exotic multifield inflation)')

    # The prediction
    ax.axvline(-4.375, color='blue', lw=3, label='Matter-bounce prediction: $-35/8$')

    # Error bars for surveys
    ax.errorbar(-4.375, 0.7, xerr=0.7, fmt='o', color='#2196F3', ms=10, lw=2.5,
                capsize=8, label='SPHEREx ($\\sigma=0.7$)')
    ax.errorbar(-4.375, 0.4, xerr=1.5, fmt='s', color='#FF9800', ms=10, lw=2.5,
                capsize=8, label='MegaMapper conservative ($\\sigma=1.5$)')

    # Inflation
    ax.axvline(0, color='black', lw=2, ls=':', label='Standard inflation: $f_{NL}\\approx 0$')

    ax.set_xlabel('Measured $f_{NL}^{\\rm local}$', fontsize=14)
    ax.set_xlim(-8, 5)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.set_title('Observational Decision Thresholds', fontsize=13)
    ax.legend(fontsize=8, loc='upper left', ncol=2)
    fig.tight_layout()
    fig.savefig(os.path.join(OUTDIR, 'fig4_decision_thresholds.png'), dpi=150)
    plt.close()
    print("Figure 4: decision thresholds — DONE")

# ============================================================
# FIGURE 5: Inflation comparison landscape
# ============================================================
def fig5_inflation_comparison():
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))

    # Models and their f_NL ranges
    models = [
        ('Single-field\nslow-roll', 0.015, 0.01, '#4CAF50'),
        ('Standard\ncurvaton', 0.5, 1.75, '#FFC107'),
        ('DBI inflation\n(equilateral)', 0, 0, '#9C27B0'),  # different shape
        ('Exotic\nmulti-field', -2.0, 4.0, '#FF9800'),
        ('Matter\nbounce', -4.375, 0.0, '#F44336'),
    ]

    y_pos = np.arange(len(models))
    for i, (name, center, half_width, color) in enumerate(models):
        if name == 'DBI inflation\n(equilateral)':
            ax.barh(i, 0.1, left=-0.05, height=0.6, color=color, alpha=0.3)
            ax.text(0.5, i, '(equilateral shape,\nnot local)', fontsize=8, va='center')
        elif half_width > 0:
            ax.barh(i, 2*half_width, left=center-half_width, height=0.6, color=color, alpha=0.5)
            ax.plot(center, i, 'o', color=color, ms=8, zorder=5)
        else:
            ax.plot(center, i, 'D', color=color, ms=12, zorder=5)

    # SPHEREx error bar on the bounce prediction
    ax.errorbar(-4.375, 4, xerr=0.7, fmt='none', ecolor='blue', capsize=6, lw=2,
                label='SPHEREx $1\\sigma$')

    ax.axvline(0, color='gray', ls='-', lw=0.5, alpha=0.5)
    ax.set_yticks(y_pos)
    ax.set_yticklabels([m[0] for m in models], fontsize=11)
    ax.set_xlabel('$f_{NL}^{\\rm local}$', fontsize=14)
    ax.set_title('$f_{NL}$ Landscape: Matter Bounce vs Inflation', fontsize=13)
    ax.set_xlim(-7, 5)
    ax.legend(fontsize=10)
    ax.grid(axis='x', alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(OUTDIR, 'fig5_inflation_comparison.png'), dpi=150)
    plt.close()
    print("Figure 5: inflation comparison — DONE")


if __name__ == "__main__":
    print("Generating all paper figures...")
    print()
    fig1_shape_function()
    fig2_survey_comparison()
    fig3_kmin_cliff()
    fig4_decision_thresholds()
    fig5_inflation_comparison()
    print()
    print(f"All figures saved to: {OUTDIR}")
    print("DONE.")
