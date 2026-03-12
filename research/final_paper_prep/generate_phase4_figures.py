#!/usr/bin/env python3
"""
Phase 4 figures:
  1. cosmology_dataset_comparison_framework.pdf — 3-panel cross-dataset comparison
  2. dneff_posterior_full_tension.pdf — ΔNeff posterior with SM + WP4 overlays
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.gridspec import GridSpec

CHAIN_DIR = os.path.join(os.path.dirname(__file__),
    '../../reproducibility/cosmology/frozen/full_tension_20260311_1728/chains')
FIG_DIR = os.path.join(os.path.dirname(__file__), '../../paper/figures')
os.makedirs(FIG_DIR, exist_ok=True)

plt.rcParams.update({
    'font.size': 11, 'axes.labelsize': 13, 'axes.titlesize': 14,
    'xtick.labelsize': 10, 'ytick.labelsize': 10, 'legend.fontsize': 9,
    'figure.dpi': 150, 'savefig.dpi': 300, 'savefig.bbox': 'tight',
    'text.usetex': False, 'font.family': 'serif',
})


def parse_header(filepath):
    with open(filepath) as f:
        line = f.readline().strip()
    tokens = line.split()
    return tokens[1:] if tokens[0] == '#' else tokens


def load_combined(burn_frac=0.3):
    """Load all chains combined with burn-in removal. Return data + header."""
    header = None
    all_data = []
    for i in range(1, 7):
        fpath = os.path.join(CHAIN_DIR, f'chain_{i:02d}', 'spin_torsion.1.txt')
        if not os.path.exists(fpath):
            continue
        if header is None:
            header = parse_header(fpath)
        data = np.loadtxt(fpath)
        n_burn = int(len(data) * burn_frac)
        all_data.append(data[n_burn:])
    combined = np.vstack(all_data)
    return combined, header


def fig_dataset_comparison():
    """Cross-dataset comparison framework (publication-quality)."""
    print("Generating cross-dataset comparison framework...")

    ft = {'H0': (67.68, 1.06), 'dNeff': (-0.020, 0.169), 'S8': (0.814, 0.008)}
    planck_lcdm = {'H0': (67.36, 0.54), 'dNeff': (0.0, 0.0), 'S8': (0.832, 0.013)}
    shoes = (73.04, 1.04)
    des_s8 = (0.776, 0.017)

    fig = plt.figure(figsize=(15, 5.5))
    gs = GridSpec(1, 3, figure=fig, wspace=0.3)

    datasets = ['full_tension', 'planck_bao_sn\n(pending)', 'planck_only\n(pending)', 'planck_bao\n(pending)']
    y_main = [0, 1.2, 2.4, 3.6]
    y_ref = [5.0]

    # --- Panel A: H0 ---
    ax = fig.add_subplot(gs[0])
    # full_tension
    ax.errorbar(ft['H0'][0], y_main[0], xerr=ft['H0'][1], fmt='o', color='#1565C0',
                capsize=6, markersize=9, linewidth=2.2, zorder=5)
    # placeholders
    for k in range(1, 4):
        ax.plot(68.0, y_main[k], 's', color='#BDBDBD', markersize=9, zorder=3)
        ax.errorbar(68.0, y_main[k], xerr=1.5, fmt='none', ecolor='#BDBDBD',
                    capsize=4, linewidth=1.5, zorder=2)
    # Planck LCDM reference
    ax.errorbar(planck_lcdm['H0'][0], y_ref[0], xerr=planck_lcdm['H0'][1], fmt='D',
                color='#E65100', capsize=6, markersize=8, linewidth=2, zorder=5)
    # SH0ES band
    ax.axvspan(shoes[0]-shoes[1], shoes[0]+shoes[1], alpha=0.12, color='#D32F2F', zorder=1)
    ax.axvline(shoes[0], color='#D32F2F', linestyle=':', alpha=0.6, linewidth=1.5)
    ax.text(shoes[0]+0.3, 5.6, 'SH0ES', fontsize=8, color='#D32F2F', va='bottom')

    all_y = y_main + y_ref
    all_labels = datasets + ['Planck 2018\n(LCDM)']
    ax.set_yticks(all_y)
    ax.set_yticklabels(all_labels)
    ax.set_xlabel(r'$H_0$ [km/s/Mpc]')
    ax.set_title('(a) Hubble Constant', fontweight='bold')
    ax.set_xlim(63, 77)
    ax.set_ylim(-0.8, 6.2)
    ax.invert_yaxis()
    ax.grid(True, alpha=0.2, axis='x')
    ax.axhline(4.3, color='gray', linewidth=0.5, linestyle='-')

    # --- Panel B: Delta_Neff ---
    ax = fig.add_subplot(gs[1])
    ax.errorbar(ft['dNeff'][0], y_main[0], xerr=ft['dNeff'][1], fmt='o', color='#1565C0',
                capsize=6, markersize=9, linewidth=2.2, zorder=5)
    for k in range(1, 4):
        ax.plot(0.05, y_main[k], 's', color='#BDBDBD', markersize=9, zorder=3)
        ax.errorbar(0.05, y_main[k], xerr=0.2, fmt='none', ecolor='#BDBDBD',
                    capsize=4, linewidth=1.5, zorder=2)
    # SM reference
    ax.axvline(0.0, color='#2E7D32', linestyle='--', alpha=0.8, linewidth=2, zorder=4)
    ax.text(0.02, 5.6, 'SM', fontsize=9, color='#2E7D32', fontweight='bold', va='bottom')

    ax.set_yticks(y_main)
    ax.set_yticklabels(datasets)
    ax.set_xlabel(r'$\Delta N_{\rm eff}$')
    ax.set_title(r'(b) $\Delta N_{\rm eff}$', fontweight='bold')
    ax.set_xlim(-0.6, 0.6)
    ax.set_ylim(-0.8, 4.4)
    ax.invert_yaxis()
    ax.grid(True, alpha=0.2, axis='x')

    # --- Panel C: S8 ---
    ax = fig.add_subplot(gs[2])
    ax.errorbar(ft['S8'][0], y_main[0], xerr=ft['S8'][1], fmt='o', color='#1565C0',
                capsize=6, markersize=9, linewidth=2.2, zorder=5)
    for k in range(1, 4):
        ax.plot(0.81, y_main[k], 's', color='#BDBDBD', markersize=9, zorder=3)
        ax.errorbar(0.81, y_main[k], xerr=0.012, fmt='none', ecolor='#BDBDBD',
                    capsize=4, linewidth=1.5, zorder=2)
    # Planck LCDM
    ax.errorbar(planck_lcdm['S8'][0], y_ref[0], xerr=planck_lcdm['S8'][1], fmt='D',
                color='#E65100', capsize=6, markersize=8, linewidth=2, zorder=5)
    # DES Y3 band
    ax.axvspan(des_s8[0]-des_s8[1], des_s8[0]+des_s8[1], alpha=0.12, color='#7B1FA2', zorder=1)
    ax.axvline(des_s8[0], color='#7B1FA2', linestyle=':', alpha=0.6, linewidth=1.5)
    ax.text(des_s8[0]-0.003, 5.6, 'DES Y3', fontsize=8, color='#7B1FA2', ha='right', va='bottom')

    ax.set_yticks(all_y)
    ax.set_yticklabels(all_labels)
    ax.set_xlabel(r'$S_8$')
    ax.set_title(r'(c) $S_8$', fontweight='bold')
    ax.set_xlim(0.73, 0.87)
    ax.set_ylim(-0.8, 6.2)
    ax.invert_yaxis()
    ax.grid(True, alpha=0.2, axis='x')
    ax.axhline(4.3, color='gray', linewidth=0.5, linestyle='-')

    fig.suptitle('Cross-Dataset Cosmological Parameter Comparison', fontsize=15, fontweight='bold', y=1.01)

    for fmt in ['pdf', 'png']:
        out = os.path.join(FIG_DIR, f'cosmology_dataset_comparison_framework.{fmt}')
        plt.savefig(out)
        print(f"  Saved: {out}")
    plt.close()


def fig_dneff_posterior():
    """ΔNeff posterior with SM expectation and WP4 mechanism regions."""
    print("Generating ΔNeff posterior figure...")

    combined, header = load_combined()
    weight_idx = 0
    dneff_idx = header.index('delta_neff')
    weights = combined[:, weight_idx]
    dneff = combined[:, dneff_idx]

    # Weighted KDE
    from scipy.stats import gaussian_kde
    # Expand weighted samples for KDE
    n_eff = int(weights.sum())
    rng = np.random.default_rng(42)
    indices = rng.choice(len(dneff), size=min(50000, n_eff),
                         p=weights/weights.sum(), replace=True)
    kde_samples = dneff[indices]
    kde = gaussian_kde(kde_samples, bw_method=0.05)

    x = np.linspace(-0.8, 0.8, 500)
    y = kde(x)
    y /= y.max()  # normalize to peak=1

    fig, ax = plt.subplots(figsize=(10, 6))

    # Posterior
    ax.fill_between(x, y, alpha=0.25, color='#1565C0')
    ax.plot(x, y, color='#1565C0', linewidth=2.5, label=r'full_tension posterior')

    # 68% CI shading
    mean_val = np.average(dneff, weights=weights)
    std_val = np.sqrt(np.average((dneff - mean_val)**2, weights=weights))
    ax.axvspan(mean_val - std_val, mean_val + std_val, alpha=0.1, color='#1565C0', zorder=1)

    # SM expectation
    ax.axvline(0.0, color='#2E7D32', linestyle='--', linewidth=2.5, alpha=0.9,
               label=r'Standard Model ($\Delta N_{\rm eff} = 0$)', zorder=4)

    # WP4 reheating mechanism region [0.05, 0.40]
    ax.axvspan(0.05, 0.40, alpha=0.12, color='#FF6F00', zorder=1)
    ax.annotate('WP4 Reheating\n[0.05, 0.40]', xy=(0.225, 0.85), fontsize=9,
                color='#FF6F00', fontweight='bold', ha='center',
                xycoords=('data', 'axes fraction'))

    # WP4 decay mechanism region [0.01, 0.25]
    ax.axvspan(0.01, 0.25, alpha=0.08, color='#AD1457', zorder=1)
    ax.annotate('WP4 Decay\n[0.01, 0.25]', xy=(0.13, 0.75), fontsize=9,
                color='#AD1457', fontweight='bold', ha='center',
                xycoords=('data', 'axes fraction'))

    # Observational constraints
    # BBN: -0.10 ± 0.21
    bbn_x = np.linspace(-0.8, 0.8, 200)
    bbn_y = np.exp(-0.5 * ((bbn_x - (-0.10)) / 0.21)**2)
    ax.plot(bbn_x, bbn_y * 0.5, color='#795548', linewidth=1.5, linestyle=':',
            alpha=0.7, label='BBN (Burns+ 2024)')

    # ACT DR6: Neff = 2.68 ± 0.29 -> dNeff = -0.37 ± 0.29
    act_x = np.linspace(-0.8, 0.8, 200)
    act_y = np.exp(-0.5 * ((act_x - (-0.37)) / 0.29)**2)
    ax.plot(act_x, act_y * 0.4, color='#00695C', linewidth=1.5, linestyle='-.',
            alpha=0.7, label='ACT DR6')

    # Mean and annotation
    ax.axvline(mean_val, color='#1565C0', linestyle=':', linewidth=1.5, alpha=0.6)
    ax.annotate(f'Mean = {mean_val:.3f}\n68% CI: [{mean_val-std_val:.3f}, {mean_val+std_val:.3f}]',
                xy=(mean_val, 1.02), fontsize=9, ha='center', va='bottom',
                xycoords=('data', 'axes fraction'),
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#1565C0', alpha=0.9))

    ax.set_xlabel(r'$\Delta N_{\rm eff}$', fontsize=14)
    ax.set_ylabel('Normalized posterior density', fontsize=13)
    ax.set_title(r'$\Delta N_{\rm eff}$ Posterior — full_tension (Planck + BAO + SN + $H_0$ + $S_8$)',
                 fontsize=13, fontweight='bold')
    ax.set_xlim(-0.7, 0.7)
    ax.set_ylim(0, 1.15)
    ax.legend(loc='upper left', framealpha=0.9, fontsize=9)
    ax.grid(True, alpha=0.15)

    for fmt in ['pdf', 'png']:
        out = os.path.join(FIG_DIR, f'dneff_posterior_full_tension.{fmt}')
        plt.savefig(out)
        print(f"  Saved: {out}")
    plt.close()


if __name__ == '__main__':
    fig_dataset_comparison()
    fig_dneff_posterior()
    print("\nPhase 4 figures complete.")
