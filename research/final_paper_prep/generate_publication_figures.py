#!/usr/bin/env python3
"""
Generate publication-quality figures from frozen full_tension chain data.

Outputs:
  paper/figures/full_tension_final_convergence.png    — R-hat and ESS vs samples
  paper/figures/full_tension_final_ess_growth.png     — ESS growth curves
  paper/figures/full_tension_final_correlation.png    — Parameter correlation heatmap
  paper/figures/cosmology_dataset_comparison_draft.png — Cross-dataset comparison (placeholder)
"""

import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy import stats

# Paths
CHAIN_DIR = os.path.join(os.path.dirname(__file__),
    '../../reproducibility/cosmology/frozen/full_tension_20260311_1728/chains')
FIG_DIR = os.path.join(os.path.dirname(__file__), '../../paper/figures')
os.makedirs(FIG_DIR, exist_ok=True)

# Style
plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 9,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'text.usetex': False,
})

# Parameter definitions
PARAMS = {
    'H0':         {'idx': None, 'label': 'H0 [km/s/Mpc]', 'range': (60, 80)},
    'delta_neff': {'idx': None, 'label': 'delta_Neff',     'range': (-2, 2)},
    'tau':        {'idx': None, 'label': 'tau',             'range': (0.01, 0.15)},
    'sigma8':     {'idx': None, 'label': 'sigma8',          'range': (0.5, 1.2)},
    'omegam':     {'idx': None, 'label': 'Omega_m',         'range': (0.1, 0.6)},
    'ns':         {'idx': None, 'label': 'n_s',             'range': (0.8, 1.1)},
    'S8':         {'idx': None, 'label': 'S8',              'range': (0.5, 1.2)},
}

DERIVED_NAMES = {
    'H0': 'H0', 'delta_neff': 'delta_neff', 'tau': 'tau',
    'sigma8': 'sigma8', 'omegam': 'omegam', 'ns': 'ns',
    'S8': 'S8', 'nnu': 'nnu', 'age': 'age',
    'ombh2': 'ombh2', 'omch2': 'omch2', 'logA': 'logA',
}


def parse_header(filepath):
    """Parse chain file header, handling the '#' prefix correctly."""
    with open(filepath) as f:
        line = f.readline().strip()
    tokens = line.split()
    if tokens[0] == '#':
        return tokens[1:]
    tokens[0] = tokens[0].lstrip('#')
    return tokens


def load_chains(burn_frac=0.3):
    """Load all 6 chains with burn-in removal."""
    chains = []
    header = None
    for i in range(1, 7):
        cdir = os.path.join(CHAIN_DIR, f'chain_{i:02d}')
        fpath = os.path.join(cdir, 'spin_torsion.1.txt')
        if not os.path.exists(fpath):
            print(f"  Warning: {fpath} not found, skipping")
            continue
        if header is None:
            header = parse_header(fpath)
        data = np.loadtxt(fpath)
        n_burn = int(len(data) * burn_frac)
        chains.append(data[n_burn:])
        print(f"  Chain {i}: {len(data)} total, {len(data)-n_burn} after burn-in")

    # Map parameter names to column indices
    for pname in PARAMS:
        if pname in header:
            PARAMS[pname]['idx'] = header.index(pname)
        elif pname == 'omegam' and 'omegam' in header:
            PARAMS[pname]['idx'] = header.index('omegam')

    # Verify
    for pname, pinfo in PARAMS.items():
        if pinfo['idx'] is None:
            print(f"  Warning: {pname} not found in header!")
            # Try common alternatives
            for alt in [pname.lower(), pname.upper()]:
                if alt in header:
                    pinfo['idx'] = header.index(alt)
                    break

    return chains, header


def compute_cumulative_rhat(chains, param_idx, weight_idx=0, n_points=50):
    """Compute R-hat as a function of cumulative samples."""
    max_len = min(len(c) for c in chains)
    fractions = np.linspace(0.1, 1.0, n_points)
    rhats = []
    sample_counts = []

    for frac in fractions:
        n = int(max_len * frac)
        if n < 10:
            continue
        chain_means = []
        chain_vars = []
        total_n = 0
        for c in chains:
            x = c[:n, param_idx]
            w = c[:n, weight_idx]
            wsum = w.sum()
            if wsum == 0:
                continue
            m = np.average(x, weights=w)
            v = np.average((x - m)**2, weights=w)
            chain_means.append(m)
            chain_vars.append(v)
            total_n += wsum

        if len(chain_means) < 2:
            continue

        chain_means = np.array(chain_means)
        chain_vars = np.array(chain_vars)
        grand_mean = np.mean(chain_means)
        B = np.var(chain_means, ddof=1)
        W = np.mean(chain_vars)

        if W > 0:
            rhat_minus1 = B / W
        else:
            rhat_minus1 = np.nan

        rhats.append(rhat_minus1)
        sample_counts.append(int(total_n))

    return np.array(sample_counts), np.array(rhats)


def compute_cumulative_ess(chains, param_idx, weight_idx=0, n_points=50):
    """Compute ESS as a function of cumulative samples using FFT autocorrelation."""
    max_len = min(len(c) for c in chains)
    fractions = np.linspace(0.1, 1.0, n_points)
    ess_vals = []
    sample_counts = []

    for frac in fractions:
        n = int(max_len * frac)
        if n < 20:
            continue
        total_ess = 0
        total_n = 0
        for c in chains:
            x = c[:n, param_idx]
            N = len(x)
            if N < 20:
                continue
            x_centered = x - x.mean()
            # FFT-based autocorrelation
            fft_x = np.fft.fft(x_centered, n=2*N)
            acf = np.fft.ifft(fft_x * np.conj(fft_x)).real[:N]
            acf /= acf[0] if acf[0] != 0 else 1

            # Compute integrated autocorrelation time
            tau_int = 1.0
            for k in range(1, N):
                if acf[k] < 0.05:
                    break
                tau_int += 2 * acf[k]

            chain_ess = N / tau_int
            total_ess += chain_ess
            total_n += N

        ess_vals.append(total_ess)
        sample_counts.append(total_n)

    return np.array(sample_counts), np.array(ess_vals)


def fig_convergence(chains, header):
    """Figure: Chain convergence — R-hat and ESS vs samples."""
    print("Generating convergence figure...")
    fig, axes = plt.subplots(2, 3, figsize=(14, 8))

    key_params = ['H0', 'delta_neff', 'tau']
    colors = ['#2196F3', '#FF5722', '#4CAF50']

    for i, pname in enumerate(key_params):
        pidx = PARAMS[pname]['idx']
        if pidx is None:
            continue

        # R-hat panel
        ax = axes[0, i]
        samples, rhats = compute_cumulative_rhat(chains, pidx)
        ax.semilogy(samples, rhats, color=colors[i], linewidth=2)
        target = 0.01 if pname != 'tau' else 0.02
        ax.axhline(target, color='red', linestyle='--', alpha=0.7, label=f'Target: {target}')
        ax.set_title(f'{PARAMS[pname]["label"]}')
        ax.set_ylabel('R-1' if i == 0 else '')
        ax.legend(loc='upper right', fontsize=8)
        ax.grid(True, alpha=0.3)

        # ESS panel
        ax = axes[1, i]
        samples, ess = compute_cumulative_ess(chains, pidx)
        ax.plot(samples, ess, color=colors[i], linewidth=2)
        target_ess = 2000 if pname != 'tau' else 1000
        ax.axhline(target_ess, color='red', linestyle='--', alpha=0.7, label=f'Target: {target_ess}')
        ax.set_xlabel('Total samples')
        ax.set_ylabel('ESS' if i == 0 else '')
        ax.legend(loc='lower right', fontsize=8)
        ax.grid(True, alpha=0.3)

    fig.suptitle('full_tension: Convergence Diagnostics', fontsize=14, fontweight='bold')
    plt.tight_layout()
    out = os.path.join(FIG_DIR, 'full_tension_final_convergence.png')
    plt.savefig(out)
    plt.close()
    print(f"  Saved: {out}")


def fig_ess_growth(chains, header):
    """Figure: ESS growth curves for all 7 key parameters."""
    print("Generating ESS growth figure...")
    fig, ax = plt.subplots(figsize=(10, 6))

    colors = plt.cm.tab10(np.linspace(0, 1, 7))

    for i, (pname, pinfo) in enumerate(PARAMS.items()):
        pidx = pinfo['idx']
        if pidx is None:
            continue
        samples, ess = compute_cumulative_ess(chains, pidx)
        ax.plot(samples, ess, color=colors[i], linewidth=2, label=pinfo['label'])

    ax.axhline(2000, color='red', linestyle='--', alpha=0.7, label='Target (H0, dNeff)')
    ax.axhline(1000, color='orange', linestyle='--', alpha=0.7, label='Target (tau)')
    ax.set_xlabel('Total samples (after burn-in)')
    ax.set_ylabel('Effective Sample Size (ESS)')
    ax.set_title('full_tension: ESS Growth Curves', fontweight='bold')
    ax.legend(loc='upper left', ncol=2)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    out = os.path.join(FIG_DIR, 'full_tension_final_ess_growth.png')
    plt.savefig(out)
    plt.close()
    print(f"  Saved: {out}")


def fig_correlation(chains, header):
    """Figure: Parameter correlation heatmap."""
    print("Generating correlation heatmap...")

    # Combine all chains
    combined = np.vstack(chains)
    weight_idx = 0
    weights = combined[:, weight_idx]

    param_names = list(PARAMS.keys())
    param_labels = [PARAMS[p]['label'] for p in param_names]
    param_indices = [PARAMS[p]['idx'] for p in param_names]

    n_params = len(param_names)
    corr_matrix = np.zeros((n_params, n_params))

    for i in range(n_params):
        for j in range(n_params):
            if param_indices[i] is None or param_indices[j] is None:
                corr_matrix[i, j] = np.nan
                continue
            xi = combined[:, param_indices[i]]
            xj = combined[:, param_indices[j]]

            # Weighted correlation
            wi = np.average(xi, weights=weights)
            wj = np.average(xj, weights=weights)
            cov = np.average((xi - wi) * (xj - wj), weights=weights)
            si = np.sqrt(np.average((xi - wi)**2, weights=weights))
            sj = np.sqrt(np.average((xj - wj)**2, weights=weights))

            if si > 0 and sj > 0:
                corr_matrix[i, j] = cov / (si * sj)
            else:
                corr_matrix[i, j] = np.nan

    fig, ax = plt.subplots(figsize=(8, 7))
    im = ax.imshow(corr_matrix, cmap='RdBu_r', vmin=-1, vmax=1, aspect='equal')

    ax.set_xticks(range(n_params))
    ax.set_yticks(range(n_params))
    ax.set_xticklabels(param_labels, rotation=45, ha='right')
    ax.set_yticklabels(param_labels)

    # Annotate cells
    for i in range(n_params):
        for j in range(n_params):
            val = corr_matrix[i, j]
            if not np.isnan(val):
                color = 'white' if abs(val) > 0.6 else 'black'
                ax.text(j, i, f'{val:.2f}', ha='center', va='center',
                       fontsize=9, color=color, fontweight='bold' if abs(val) > 0.5 else 'normal')

    plt.colorbar(im, ax=ax, label='Correlation coefficient', shrink=0.8)
    ax.set_title('full_tension: Parameter Correlations', fontweight='bold')
    plt.tight_layout()
    out = os.path.join(FIG_DIR, 'full_tension_final_correlation.png')
    plt.savefig(out)
    plt.close()
    print(f"  Saved: {out}")


def fig_dataset_comparison():
    """Figure: Cross-dataset comparison (full_tension + placeholders)."""
    print("Generating cross-dataset comparison figure...")

    # full_tension values
    ft = {
        'H0':    (67.68, 1.06),
        'dNeff': (-0.020, 0.169),
        'S8':    (0.814, 0.008),
    }

    # Reference values
    planck_lcdm = {
        'H0':    (67.36, 0.54),
        'dNeff': (0.0, None),  # SM value
        'S8':    (0.832, 0.013),
    }

    shoes_h0 = (73.04, 1.04)  # Riess+ 2022
    des_s8 = (0.776, 0.017)   # DES Y3

    fig = plt.figure(figsize=(14, 5))
    gs = GridSpec(1, 3, figure=fig, wspace=0.35)

    # Panel A: H0
    ax = fig.add_subplot(gs[0])
    y_pos = [0, 1, 2, 3]
    labels = ['full_tension', 'planck_bao_sn\n(pending)', 'planck_only\n(pending)', 'Planck 2018\nLCDM']

    # full_tension
    ax.errorbar(ft['H0'][0], 0, xerr=ft['H0'][1], fmt='o', color='#2196F3',
                capsize=5, markersize=8, linewidth=2, label='full_tension')
    # placeholders
    ax.plot(68.0, 1, 's', color='gray', alpha=0.3, markersize=8)
    ax.plot(67.5, 2, 's', color='gray', alpha=0.3, markersize=8)
    # Planck LCDM
    ax.errorbar(planck_lcdm['H0'][0], 3, xerr=planck_lcdm['H0'][1], fmt='D',
                color='#FF9800', capsize=5, markersize=7, linewidth=2)
    # SH0ES band
    ax.axvspan(shoes_h0[0]-shoes_h0[1], shoes_h0[0]+shoes_h0[1], alpha=0.15, color='red', label='SH0ES')
    ax.axvline(shoes_h0[0], color='red', linestyle=':', alpha=0.5)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels)
    ax.set_xlabel('H0 [km/s/Mpc]')
    ax.set_title('Panel A: H0', fontweight='bold')
    ax.legend(loc='upper right', fontsize=8)
    ax.grid(True, alpha=0.3, axis='x')
    ax.set_xlim(64, 76)

    # Panel B: Delta_Neff
    ax = fig.add_subplot(gs[1])
    ax.errorbar(ft['dNeff'][0], 0, xerr=ft['dNeff'][1], fmt='o', color='#2196F3',
                capsize=5, markersize=8, linewidth=2)
    ax.plot(0.08, 1, 's', color='gray', alpha=0.3, markersize=8)
    ax.plot(0.0, 2, 's', color='gray', alpha=0.3, markersize=8)
    ax.axvline(0.0, color='green', linestyle='--', alpha=0.7, label='SM (dNeff=0)')

    ax.set_yticks(y_pos[:3])
    ax.set_yticklabels(labels[:3])
    ax.set_xlabel('delta_Neff')
    ax.set_title('Panel B: delta_Neff', fontweight='bold')
    ax.legend(loc='upper right', fontsize=8)
    ax.grid(True, alpha=0.3, axis='x')
    ax.set_xlim(-0.6, 0.6)

    # Panel C: S8
    ax = fig.add_subplot(gs[2])
    ax.errorbar(ft['S8'][0], 0, xerr=ft['S8'][1], fmt='o', color='#2196F3',
                capsize=5, markersize=8, linewidth=2)
    ax.plot(0.81, 1, 's', color='gray', alpha=0.3, markersize=8)
    ax.plot(0.82, 2, 's', color='gray', alpha=0.3, markersize=8)
    ax.errorbar(planck_lcdm['S8'][0], 3, xerr=planck_lcdm['S8'][1], fmt='D',
                color='#FF9800', capsize=5, markersize=7, linewidth=2)
    # DES band
    ax.axvspan(des_s8[0]-des_s8[1], des_s8[0]+des_s8[1], alpha=0.15, color='purple', label='DES Y3')
    ax.axvline(des_s8[0], color='purple', linestyle=':', alpha=0.5)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels)
    ax.set_xlabel('S8')
    ax.set_title('Panel C: S8', fontweight='bold')
    ax.legend(loc='upper right', fontsize=8)
    ax.grid(True, alpha=0.3, axis='x')
    ax.set_xlim(0.74, 0.86)

    fig.suptitle('Cross-Dataset Comparison (DRAFT — pending datasets shown as gray)',
                 fontsize=13, fontweight='bold', y=1.02)
    plt.tight_layout()
    out = os.path.join(FIG_DIR, 'cosmology_dataset_comparison_draft.png')
    plt.savefig(out)
    plt.close()
    print(f"  Saved: {out}")


def main():
    print("Loading frozen chain data...")
    chains, header = load_chains(burn_frac=0.3)
    print(f"  Loaded {len(chains)} chains, header has {len(header)} columns")
    print(f"  Parameter mapping: {[(p, PARAMS[p]['idx']) for p in PARAMS]}")

    fig_convergence(chains, header)
    fig_ess_growth(chains, header)
    fig_correlation(chains, header)
    fig_dataset_comparison()

    print("\nAll figures generated successfully.")


if __name__ == '__main__':
    main()
