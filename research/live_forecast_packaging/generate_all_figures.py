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

# ------------------------------------------------------------
# Publication style — consistent fonts/sizes + a colorblind-safe
# (Wong 2011) palette applied across every figure. Presentation
# only; no plotted value is changed by this block.
# ------------------------------------------------------------
plt.rcParams.update({
    'font.size': 12,
    'axes.titlesize': 13,
    'axes.labelsize': 13,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'legend.fontsize': 10,
    'axes.linewidth': 0.8,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
})
# Wong colorblind-safe palette
CB_BLUE   = '#0072B2'   # SPHEREx
CB_ORANGE = '#E69F00'   # MegaMapper
CB_GREEN  = '#009E73'   # thresholds / favorable
CB_VERMIL = '#D55E00'   # exclusion / wrong sign
CB_SKY    = '#56B4E9'
CB_YELLOW = '#F0E442'
CB_PURPLE = '#CC79A7'
CB_GREY   = '#999999'

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
    # Corrected amplitude: the Cai et al. shape polynomial (BNL) carries the
    # spurious +(99/128) sum k_i^3 local term (Appendix A), so its bare
    # squeezed limit is -35/8. The certified matter-bounce amplitude is
    # -35/16 = exactly one-half (3-way certified: vertex re-sum + Li et al.
    # general-c_s at c_s=1). We plot the Cai shape normalized to its corrected
    # squeezed amplitude, i.e. scaled by 1/2, so the curve converges to -35/16
    # and the benchmark values match tab:benchmarks (-2.1875, -1.992, -1.125).
    CORR = 0.5  # -35/16 / (-35/8): halves the printed Cai amplitude
    k1_arr = np.geomspace(0.001, 1.0, 200)
    bnl_arr = [CORR * BNL(k1, 1.0, 1.0) for k1 in k1_arr]

    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    ax.semilogx(k1_arr, bnl_arr, '-', color=CB_BLUE, lw=2)
    ax.axhline(-35/16, color=CB_VERMIL, ls='--', lw=1.2, label=r'Squeezed limit: $-35/16 = -2.1875$')
    ax.axhline(-255/128, color=CB_ORANGE, ls=':', lw=1.2, label=r'Equilateral: $-255/128 = -1.992$')

    # Mark special points (corrected amplitude)
    ax.plot(1e-3, CORR * BNL(1e-3, 1, 1), 'o', color=CB_VERMIL, ms=8, zorder=5)
    ax.plot(1.0, CORR * BNL(1, 1, 1), 's', color=CB_ORANGE, ms=8, zorder=5)
    ax.plot(0.5, CORR * BNL(0.5, 1, 1), '^', color=CB_GREEN, ms=8, zorder=5,
            label=r'Folded ($k_1=2k_2=2k_3$): $-9/8 = -1.125$')

    ax.set_xlabel('$k_1 / k$')
    ax.set_ylabel('$|B|_{NL}(k_1, k, k)$')
    ax.set_title('Matter-Bounce Bispectrum: Squeezed-Limit Convergence')
    ax.legend(loc='upper right')
    ax.set_ylim(-2.75, -0.75)
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
    # Bars show the template-corrected significances used in the paper text at the
    # CORRECTED central f_NL = -35/16 = -2.1875 (Appendix A) — every value is
    # exactly one-half of the erroneous -35/8 input, matching the fig:surveys
    # caption verbatim. No number is invented here; each entry is read from the
    # caption/text (significance scales linearly with |f_NL|):
    #  - SPHEREx naive uncorrected: |f_NL|/sigma = 2.1875/0.70 = 3.13 sigma (reference only)
    #  - SPHEREx template-corrected optimistic bispectrum: 2.6-2.75 sigma
    #  - SPHEREx realistic post-systematic-budget envelope: 1.3-2.75 sigma
    #  - SPHEREx all-combined conservative endpoint: 1.3-1.4 sigma
    #  - MegaMapper ideal (template-corrected): 3.7-3.85 sigma
    #  - MegaMapper illustrative design-uncertainty envelope: 1.5-3.5 sigma
    fig, ax = plt.subplots(1, 1, figsize=(13, 5))

    surveys = ['SPHEREx bispec.\n(naive, uncorrected;\nnot used in headline)',
               'SPHEREx bispec.\n(template-corrected,\noptimistic)',
               'SPHEREx\n(realistic\npost-budget)',
               'SPHEREx\n(all-combined\nconservative)',
               'MegaMapper\n(ideal, template-\ncorrected)',
               'MegaMapper\n(illustrative\nenvelope)',
               'MegaMapper\n(conservative)', 'MegaMapper\n(single-tracer)']
    #                naive  opt   real  allc  MMid  MMill MMcons MMst
    central = [3.13, 2.675, 2.025, 1.35, 3.775, 2.5, 1.5, 0.875]
    low =     [3.13, 2.6,   1.3,   1.3,  3.7,   1.5, 0.75, 0.5]
    high =    [3.13, 2.75,  2.75,  1.4,  3.85,  3.5, 2.5, 1.25]

    colors = [CB_GREY, CB_BLUE, CB_BLUE, CB_BLUE,
              CB_ORANGE, CB_ORANGE, CB_ORANGE, CB_ORANGE]
    alphas =  [0.55, 0.95, 0.75, 0.55, 0.95, 0.75, 0.6, 0.45]
    hatches = ['//', None, None, None, None, None, None, None]

    x = np.arange(len(surveys))
    for i in range(len(surveys)):
        b = ax.bar(x[i], central[i], color=colors[i], alpha=alphas[i],
                   edgecolor='black', lw=0.5)
        if hatches[i]:
            b[0].set_hatch(hatches[i])
    for i in range(len(surveys)):
        if high[i] > low[i]:
            ax.errorbar(x[i], central[i],
                        yerr=[[central[i]-low[i]], [high[i]-central[i]]],
                        fmt='none', ecolor='black', capsize=5, lw=1.5)

    ax.axhline(5, color=CB_GREEN, ls='--', lw=1.5, alpha=0.8, label=r'$5\sigma$ discovery threshold')
    ax.axhline(3, color=CB_YELLOW, ls='--', lw=1.8, alpha=0.9, label=r'$3\sigma$ evidence threshold')

    ax.set_xticks(x)
    ax.set_xticklabels(surveys, fontsize=8)
    ax.set_ylabel(r'Detection Significance ($\sigma$)')
    ax.set_title(r'$f_{NL} = -35/16$: Survey Detection Significance (template-corrected)')
    ax.legend()
    ax.set_ylim(0, 6)
    ax.grid(axis='y', alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(OUTDIR, 'fig2_survey_comparison.png'))
    plt.close()
    print("Figure 2: survey comparison — DONE")

# ============================================================
# FIGURE 3: Fisher sensitivity to k_min (the "cliff" plot)
# ============================================================
def fig3_kmin_cliff():
    # Corrected central amplitude |f_NL| = 35/16 = 2.1875 (Appendix A), half the
    # erroneous 35/8. The left panel (sigma vs k_min) is amplitude-independent
    # (unchanged). The right panel significance = |f_NL|/sigma is recomputed at
    # the corrected 2.1875, matching the fig:kmin caption "significance for the
    # corrected central f_NL = -35/16". No sigma(f_NL) value is changed.
    FNL = 35/16  # 2.1875
    kmin_mm = [1e-4, 2e-4, 5e-4, 1e-3, 2e-3, 5e-3]
    sigma_mm = [0.525, 1.929, 36.3, 500, 8241, 440446]
    sig_mm = [FNL/s for s in sigma_mm]

    kmin_sp = [1e-4, 5e-4, 1e-3, 2e-3, 5e-3]
    sigma_sp = [3.3, 66.2, 819, 13360, 714075]
    sig_sp = [FNL/s for s in sigma_sp]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    # Left: sigma(f_NL) vs k_min (amplitude-independent)
    ax1.loglog(kmin_mm, sigma_mm, 'o-', color=CB_ORANGE, lw=2, ms=7, label='MegaMapper (multi-tracer)')
    ax1.loglog(kmin_sp, sigma_sp, 's-', color=CB_BLUE, lw=2, ms=7, label='SPHEREx (single-pop SDB)')
    ax1.axhline(0.7, color=CB_BLUE, ls=':', alpha=0.7, label=r'SPHEREx bispectrum: $\sigma=0.7$')
    ax1.axhline(1.0, color=CB_GREY, ls='--', alpha=0.6)
    ax1.set_xlabel(r'$k_{\min}$ [h/Mpc]')
    ax1.set_ylabel(r'$\sigma(f_{NL})$')
    ax1.set_title(r'$\sigma(f_{NL})$ vs Minimum Accessible Scale')
    ax1.set_ylim(0.1, 1e6)
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Right: significance vs k_min (at corrected f_NL = -35/16)
    ax2.semilogx(kmin_mm, sig_mm, 'o-', color=CB_ORANGE, lw=2, ms=7, label='MegaMapper')
    ax2.semilogx(kmin_sp, sig_sp, 's-', color=CB_BLUE, lw=2, ms=7, label='SPHEREx (SDB only)')
    ax2.axhline(FNL/0.7, color=CB_BLUE, ls=':', lw=1.5, alpha=0.8,
                label=r'SPHEREx bispectrum: $3.1\sigma$')
    ax2.axhline(5, color=CB_GREEN, ls='--', alpha=0.7, label=r'$5\sigma$')
    ax2.axhline(3, color=CB_YELLOW, ls='--', lw=1.6, alpha=0.9, label=r'$3\sigma$')
    ax2.set_xlabel(r'$k_{\min}$ [h/Mpc]')
    ax2.set_ylabel(r'Detection Significance ($\sigma$)')
    ax2.set_title(r'Significance for $f_{NL}=-35/16$')
    ax2.set_ylim(-0.5, 6)
    ax2.legend(loc='upper right')
    ax2.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTDIR, 'fig3_kmin_cliff.png'))
    plt.close()
    print("Figure 3: k_min cliff — DONE")

# ============================================================
# FIGURE 4: Decision threshold diagram
# ============================================================
def fig4_decision_thresholds():
    # Corrected prediction f_NL = -35/16 = -2.1875 (Appendix A, 3-way certified),
    # half the erroneous -35/8. Decision regions re-centered so the corrected
    # prediction sits in the dark-green "strongly favors bounce" zone (matching
    # the paper caption: "dark green -- measurement near the corrected -35/16
    # prediction, strongly favors the bounce").
    FNL = -35/16  # -2.1875
    fig, ax = plt.subplots(1, 1, figsize=(12, 3.5))

    # Colored regions (re-centered on the corrected -35/16 prediction)
    ax.axvspan(-4, -1.5, alpha=0.30, color=CB_GREEN, label='STRONGLY FAVORS BOUNCE')
    ax.axvspan(-1.5, -0.5, alpha=0.18, color=CB_GREEN, label='SUPPORTS BOUNCE')
    ax.axvspan(-0.5, 0.5, alpha=0.30, color=CB_VERMIL, label='BOUNCE EXCLUDED')
    ax.axvspan(0.5, 4, alpha=0.16, color=CB_VERMIL, label='WRONG SIGN (supports exotic multifield inflation)')

    # The prediction
    ax.axvline(FNL, color=CB_BLUE, lw=3, label=r'Matter-bounce prediction: $-35/16$')

    # Error bars for surveys (centered on the corrected prediction)
    ax.errorbar(FNL, 0.7, xerr=0.7, fmt='o', color=CB_BLUE, ms=10, lw=2.5,
                capsize=8, label=r'SPHEREx ($\sigma=0.7$)')
    ax.errorbar(FNL, 0.4, xerr=1.5, fmt='s', color=CB_ORANGE, ms=10, lw=2.5,
                capsize=8, label=r'MegaMapper conservative ($\sigma=1.5$)')

    # Inflation
    ax.axvline(0, color='black', lw=2, ls=':', label=r'Standard inflation: $f_{NL}\approx 0$')

    ax.set_xlabel(r'Measured $f_{NL}^{\rm local}$')
    ax.set_xlim(-4.5, 4)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.set_title('Observational Decision Thresholds')
    ax.legend(fontsize=8, loc='upper left', ncol=2)
    fig.tight_layout()
    fig.savefig(os.path.join(OUTDIR, 'fig4_decision_thresholds.png'))
    plt.close()
    print("Figure 4: decision thresholds — DONE")

# ============================================================
# FIGURE 5: Inflation comparison landscape
# ============================================================
def fig5_inflation_comparison():
    # Matter-bounce prediction at the CORRECTED central f_NL = -35/16 = -2.1875
    # (Appendix A), half the erroneous -35/8. Model f_NL positions and the
    # SPHEREx 1-sigma error bar are placed at -2.1875; no other value changed.
    FNL = -35/16  # -2.1875
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))

    # Models and their f_NL ranges (colorblind-safe palette)
    models = [
        ('Single-field\nslow-roll', 0.015, 0.01, CB_GREEN),
        ('Standard\ncurvaton', 0.5, 1.75, CB_YELLOW),
        ('DBI inflation\n(equilateral)', 0, 0, CB_PURPLE),  # different shape
        ('Exotic\nmulti-field', -2.0, 4.0, CB_ORANGE),
        ('Matter\nbounce', FNL, 0.0, CB_VERMIL),
    ]

    y_pos = np.arange(len(models))
    for i, (name, center, half_width, color) in enumerate(models):
        if name == 'DBI inflation\n(equilateral)':
            ax.barh(i, 0.1, left=-0.05, height=0.6, color=color, alpha=0.35)
            ax.text(0.5, i, '(equilateral shape,\nnot local)', fontsize=8, va='center')
        elif half_width > 0:
            ax.barh(i, 2*half_width, left=center-half_width, height=0.6, color=color, alpha=0.5)
            ax.plot(center, i, 'o', color=color, ms=8, zorder=5)
        else:
            ax.plot(center, i, 'D', color=color, ms=12, zorder=5)

    # SPHEREx error bar on the corrected bounce prediction
    ax.errorbar(FNL, 4, xerr=0.7, fmt='none', ecolor=CB_BLUE, capsize=6, lw=2,
                label=r'SPHEREx $1\sigma$ ($\sigma=0.7$)')

    ax.axvline(0, color=CB_GREY, ls='-', lw=0.6, alpha=0.6)
    ax.set_yticks(y_pos)
    ax.set_yticklabels([m[0] for m in models])
    ax.set_xlabel(r'$f_{NL}^{\rm local}$')
    ax.set_title(r'$f_{NL}$ Landscape: Matter Bounce vs Inflation')
    ax.set_xlim(-7, 5)
    ax.legend()
    ax.grid(axis='x', alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(OUTDIR, 'fig5_inflation_comparison.png'))
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
