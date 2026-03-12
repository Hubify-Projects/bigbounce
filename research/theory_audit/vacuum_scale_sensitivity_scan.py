#!/usr/bin/env python3
"""
Vacuum Energy Scale Sensitivity Scan

Tests how sensitive the predicted dark energy density ρ_Λ is to the
underlying parameters of the spin-torsion cosmology framework.

Key equation (main.tex Eq. 14):
    ρ_Λ = [(α/M) · M_Pl] × D_inf × M_Pl⁴

where:
    (α/M) · M_Pl  ~ 10^{-2}  (one-loop parity-odd suppression)
    D_inf = exp(-3 N_tot) × (T_reh / M_GUT)^{3/2}
    M_Pl = 1.221 × 10^{19} GeV

Observed: ρ_obs ≈ 2.846 × 10^{-47} GeV⁴  (Planck 2018)

Monte Carlo scan: 100,000 samples over physically motivated ranges.
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Output directory
FIG_DIR = os.path.join(os.path.dirname(__file__), '../../paper/figures')
os.makedirs(FIG_DIR, exist_ok=True)

# Physical constants (natural units, GeV)
M_PL = 1.2209e19       # Planck mass [GeV]
RHO_OBS = 2.846e-47    # Observed ρ_Λ [GeV⁴]  (Planck 2018)
M_PL4 = M_PL**4        # M_Pl⁴ [GeV⁴]

# Number of samples
N_SAMPLES = 100_000

np.random.seed(42)


def compute_rho_lambda(alpha_M_Mpl, N_tot, T_reh_GeV, M_GUT_GeV):
    """
    Compute predicted vacuum energy density.

    Parameters
    ----------
    alpha_M_Mpl : float
        Dimensionless one-loop factor [(α/M) × M_Pl], expected ~10^{-2}
    N_tot : float
        Total inflationary e-folds
    T_reh_GeV : float
        Reheating temperature [GeV]
    M_GUT_GeV : float
        GUT scale [GeV]

    Returns
    -------
    rho_lambda : float
        Predicted ρ_Λ [GeV⁴]
    """
    D_inf = np.exp(-3.0 * N_tot) * (T_reh_GeV / M_GUT_GeV)**1.5
    rho = alpha_M_Mpl * D_inf * M_PL4
    return rho


def sample_parameters(n):
    """
    Sample parameters from physically motivated prior ranges.

    Ranges:
    - alpha_M_Mpl: log-uniform in [10^{-4}, 10^{0}]
        One-loop factor; natural range from perturbative estimates.
        Central expectation ~10^{-2} from g²γ/(32π²).

    - N_tot: uniform in [60, 200]
        Must exceed N_obs ≈ 55-60. Upper bound from typical slow-roll models.
        Paper's fitted value: 92.

    - T_reh: log-uniform in [10^{6}, 10^{16}] GeV
        From low-scale (MeV) to GUT-scale reheating.

    - M_GUT: log-uniform in [10^{15}, 10^{17}] GeV
        Standard GUT range.

    Returns dict of arrays.
    """
    params = {}

    # (α/M)·M_Pl: log-uniform [10^{-4}, 1]
    log_alpha = np.random.uniform(-4, 0, n)
    params['alpha_M_Mpl'] = 10**log_alpha

    # N_tot: uniform [60, 200]
    params['N_tot'] = np.random.uniform(60, 200, n)

    # T_reh: log-uniform [10^6, 10^16] GeV
    log_Treh = np.random.uniform(6, 16, n)
    params['T_reh'] = 10**log_Treh

    # M_GUT: log-uniform [10^{15}, 10^{17}] GeV
    log_MGUT = np.random.uniform(15, 17, n)
    params['M_GUT'] = 10**log_MGUT

    return params


def run_scan():
    """Run the Monte Carlo scan."""
    print(f"Running sensitivity scan with {N_SAMPLES:,} samples...")

    params = sample_parameters(N_SAMPLES)

    rho_pred = compute_rho_lambda(
        params['alpha_M_Mpl'],
        params['N_tot'],
        params['T_reh'],
        params['M_GUT']
    )

    ratio = rho_pred / RHO_OBS
    log_ratio = np.log10(np.abs(ratio) + 1e-300)  # avoid log(0)

    # Viable region: 0.01 < ratio < 100
    viable = (ratio > 0.01) & (ratio < 100)
    viable_frac = np.sum(viable) / N_SAMPLES

    print(f"  Viable fraction (0.01 < ρ_pred/ρ_obs < 100): {viable_frac:.6f} ({np.sum(viable)} samples)")
    print(f"  log10(ratio) range: [{log_ratio.min():.1f}, {log_ratio.max():.1f}]")
    print(f"  Median log10(ratio): {np.median(log_ratio):.1f}")

    return params, rho_pred, ratio, log_ratio, viable


def compute_sensitivities(params, log_ratio):
    """Compute parameter sensitivities via Spearman rank correlation."""
    from scipy.stats import spearmanr

    sensitivities = {}
    for pname, pvals in params.items():
        if pname in ('T_reh', 'M_GUT', 'alpha_M_Mpl'):
            corr, pval = spearmanr(np.log10(pvals), log_ratio)
        else:
            corr, pval = spearmanr(pvals, log_ratio)
        sensitivities[pname] = {'rho_s': corr, 'p_value': pval}
        print(f"  {pname:15s}: ρ_s = {corr:+.4f} (p = {pval:.2e})")

    return sensitivities


def make_plots(params, ratio, log_ratio, viable, sensitivities):
    """Generate all publication figures."""
    print("Generating figures...")

    fig = plt.figure(figsize=(18, 14))
    gs = GridSpec(2, 2, figure=fig, hspace=0.3, wspace=0.3)

    # --- Panel 1: Histogram of log10(ρ_pred/ρ_obs) ---
    ax = fig.add_subplot(gs[0, 0])
    bins = np.linspace(-200, 200, 200)
    ax.hist(log_ratio, bins=bins, color='#1565C0', alpha=0.7, edgecolor='none', density=True)
    ax.axvline(0, color='#D32F2F', linewidth=2.5, linestyle='--', label=r'$\rho_{\rm pred} = \rho_{\rm obs}$')
    ax.axvspan(-2, 2, alpha=0.15, color='#4CAF50', label='Viable: 0.01 < ratio < 100')
    ax.set_xlabel(r'$\log_{10}(\rho_{\rm pred} / \rho_{\rm obs})$', fontsize=13)
    ax.set_ylabel('Probability density', fontsize=12)
    ax.set_title('(a) Predicted Vacuum Energy Distribution', fontweight='bold')
    ax.legend(fontsize=9)
    ax.set_xlim(-200, 200)
    ax.grid(True, alpha=0.2)

    # --- Panel 2: Sensitivity scatter — N_tot dominates ---
    ax = fig.add_subplot(gs[0, 1])
    n_plot = min(10000, N_SAMPLES)
    idx = np.random.choice(N_SAMPLES, n_plot, replace=False)
    sc = ax.scatter(params['N_tot'][idx], log_ratio[idx],
                    c=np.log10(params['alpha_M_Mpl'][idx]),
                    cmap='viridis', s=1, alpha=0.3, rasterized=True)
    ax.axhline(0, color='#D32F2F', linewidth=2, linestyle='--')
    ax.axhspan(-2, 2, alpha=0.1, color='#4CAF50')
    ax.set_xlabel(r'$N_{\rm tot}$ (total e-folds)', fontsize=13)
    ax.set_ylabel(r'$\log_{10}(\rho_{\rm pred} / \rho_{\rm obs})$', fontsize=12)
    ax.set_title(r'(b) Sensitivity to $N_{\rm tot}$', fontweight='bold')
    cb = plt.colorbar(sc, ax=ax)
    cb.set_label(r'$\log_{10}[(\alpha/M)\cdot M_{\rm Pl}]$', fontsize=10)
    ax.set_ylim(-200, 200)
    ax.grid(True, alpha=0.2)

    # --- Panel 3: Viable parameter region heatmap ---
    ax = fig.add_subplot(gs[1, 0])

    # 2D histogram: N_tot vs log10(alpha_M_Mpl), colored by viable fraction
    n_bins = 50
    N_edges = np.linspace(60, 200, n_bins + 1)
    alpha_edges = np.linspace(-4, 0, n_bins + 1)

    viable_counts = np.zeros((n_bins, n_bins))
    total_counts = np.zeros((n_bins, n_bins))

    N_idx = np.digitize(params['N_tot'], N_edges) - 1
    alpha_idx = np.digitize(np.log10(params['alpha_M_Mpl']), alpha_edges) - 1

    for i in range(N_SAMPLES):
        ni, ai = N_idx[i], alpha_idx[i]
        if 0 <= ni < n_bins and 0 <= ai < n_bins:
            total_counts[ai, ni] += 1
            if viable[i]:
                viable_counts[ai, ni] += 1

    with np.errstate(divide='ignore', invalid='ignore'):
        frac = np.where(total_counts > 0, viable_counts / total_counts, np.nan)

    im = ax.pcolormesh(N_edges, alpha_edges, frac, cmap='hot', vmin=0, vmax=1, shading='flat')
    ax.set_xlabel(r'$N_{\rm tot}$', fontsize=13)
    ax.set_ylabel(r'$\log_{10}[(\alpha/M)\cdot M_{\rm Pl}]$', fontsize=12)
    ax.set_title('(c) Viable Region (0.01 < ratio < 100)', fontweight='bold')
    cb = plt.colorbar(im, ax=ax)
    cb.set_label('Fraction viable', fontsize=10)
    ax.grid(True, alpha=0.2, color='white')

    # Mark paper's fiducial point
    ax.plot(92, np.log10(0.01), '*', color='cyan', markersize=15, markeredgecolor='white',
            markeredgewidth=1.5, zorder=5, label=r'Paper fiducial ($N_{\rm tot}=92$)')
    ax.legend(fontsize=9)

    # --- Panel 4: Sensitivity ranking bar chart ---
    ax = fig.add_subplot(gs[1, 1])

    names = list(sensitivities.keys())
    labels = [r'$(\alpha/M)\cdot M_{\rm Pl}$', r'$N_{\rm tot}$', r'$T_{\rm reh}$', r'$M_{\rm GUT}$']
    rhos = [sensitivities[n]['rho_s'] for n in names]
    abs_rhos = [abs(r) for r in rhos]

    # Sort by absolute sensitivity
    order = np.argsort(abs_rhos)[::-1]
    colors = ['#D32F2F' if rhos[i] < 0 else '#1565C0' for i in order]

    ax.barh(range(len(names)), [rhos[i] for i in order], color=[colors[j] for j in range(len(order))],
            edgecolor='black', linewidth=0.5)
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels([labels[i] for i in order], fontsize=11)
    ax.set_xlabel(r'Spearman $\rho_s$ with $\log_{10}(\rho_{\rm pred}/\rho_{\rm obs})$', fontsize=12)
    ax.set_title('(d) Parameter Sensitivity Ranking', fontweight='bold')
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_xlim(-1.1, 1.1)
    ax.grid(True, alpha=0.2, axis='x')

    fig.suptitle('Vacuum Energy Scale Sensitivity Analysis — Spin-Torsion Framework',
                 fontsize=16, fontweight='bold', y=0.98)

    for fmt in ['png', 'pdf']:
        out = os.path.join(FIG_DIR, f'vacuum_scale_sensitivity.{fmt}')
        plt.savefig(out, dpi=300, bbox_inches='tight')
        print(f"  Saved: {out}")
    plt.close()


def viable_fraction_by_param(params, viable):
    """Compute the fraction of viable samples as a function of each parameter."""
    results = {}

    # N_tot bins
    N_bins = np.linspace(60, 200, 29)
    N_centers = 0.5 * (N_bins[:-1] + N_bins[1:])
    N_fracs = []
    for i in range(len(N_bins) - 1):
        mask = (params['N_tot'] >= N_bins[i]) & (params['N_tot'] < N_bins[i+1])
        if mask.sum() > 0:
            N_fracs.append(viable[mask].mean())
        else:
            N_fracs.append(0)
    results['N_tot'] = (N_centers, np.array(N_fracs))

    # log10(alpha_M_Mpl) bins
    alpha_bins = np.linspace(-4, 0, 21)
    alpha_centers = 0.5 * (alpha_bins[:-1] + alpha_bins[1:])
    alpha_fracs = []
    for i in range(len(alpha_bins) - 1):
        log_a = np.log10(params['alpha_M_Mpl'])
        mask = (log_a >= alpha_bins[i]) & (log_a < alpha_bins[i+1])
        if mask.sum() > 0:
            alpha_fracs.append(viable[mask].mean())
        else:
            alpha_fracs.append(0)
    results['alpha_M_Mpl'] = (alpha_centers, np.array(alpha_fracs))

    return results


def main():
    params, rho_pred, ratio, log_ratio, viable = run_scan()

    print("\nSensitivity analysis (Spearman rank correlations):")
    sensitivities = compute_sensitivities(params, log_ratio)

    print("\nViable fraction analysis:")
    vf = viable_fraction_by_param(params, viable)
    peak_N = vf['N_tot'][0][np.argmax(vf['N_tot'][1])]
    peak_alpha = vf['alpha_M_Mpl'][0][np.argmax(vf['alpha_M_Mpl'][1])]
    print(f"  Peak viable N_tot: ~{peak_N:.0f}")
    print(f"  Peak viable log10(alpha_M_Mpl): ~{peak_alpha:.1f}")

    # Fine-tuning metrics
    viable_frac = viable.mean()
    print(f"\n  Overall viable fraction: {viable_frac:.6f}")
    print(f"  Fine-tuning measure: 1/{1/viable_frac:.0f}")

    # N_tot specific: what range of N_tot is viable (marginalizing over others)?
    viable_N = params['N_tot'][viable]
    if len(viable_N) > 0:
        N_range = viable_N.max() - viable_N.min()
        N_total_range = 200 - 60
        print(f"  Viable N_tot range: [{viable_N.min():.1f}, {viable_N.max():.1f}] (width {N_range:.1f})")
        print(f"  N_tot fractional range: {N_range/N_total_range:.4f}")
    else:
        print("  No viable samples found!")

    make_plots(params, ratio, log_ratio, viable, sensitivities)
    print("\nScan complete.")

    # Return key results for report generation
    return {
        'n_samples': N_SAMPLES,
        'viable_fraction': viable_frac,
        'sensitivities': sensitivities,
        'viable_N_range': (viable_N.min(), viable_N.max()) if len(viable_N) > 0 else (0, 0),
        'peak_N': peak_N,
        'median_log_ratio': np.median(log_ratio),
    }


if __name__ == '__main__':
    main()
