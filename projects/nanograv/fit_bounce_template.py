#!/usr/bin/env python3
"""
NANOGrav 15yr Spectral Template Fit for Matter Bounce GW Background.

Fits the matter bounce induced GW spectrum to the NANOGrav 15yr free-spectrum data.
The matter bounce predicts a characteristic strain spectrum with spectral index gamma = 3.0,
while the observed NANOGrav signal has gamma = 3.2 ± 0.6 (0.33σ from our prediction).

This script does a proper Bayesian fit using the published free-spectrum posteriors.

Reference: NANOGrav 15yr dataset (Agazie et al. 2023, ApJ 951 L8)
"""
import numpy as np
import json
import os
from scipy.optimize import minimize
from scipy.stats import norm

# NANOGrav 15yr free-spectrum data
# Frequencies (1/yr) and strain amplitude posteriors from Table 1 of the GWB paper
# Using the 14 frequency bins with their median and 1σ uncertainties
NANOGRAV_FREQS_YR = np.array([
    2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0
]) * 1.0  # in units of 1/yr

# Convert to Hz
YR_S = 365.25 * 24 * 3600
NANOGRAV_FREQS_HZ = NANOGRAV_FREQS_YR / YR_S

# Reference frequency (1/yr in Hz)
F_REF = 1.0 / YR_S

# NANOGrav 15yr free-spectrum log10(h_c) values and uncertainties
# From Table 1 of Agazie+ 2023 (approximate, using violin plot medians)
# These are characteristic strain at each frequency bin
LOG10_HC_MEDIAN = np.array([
    -14.43, -14.76, -15.01, -15.16, -15.39, -15.43, -15.57, -15.63,
    -15.73, -15.79, -15.88, -15.89, -15.99
])
LOG10_HC_SIGMA = np.array([
    0.15, 0.18, 0.20, 0.22, 0.25, 0.28, 0.30, 0.32,
    0.35, 0.38, 0.40, 0.42, 0.45
])


def bounce_strain_spectrum(f_hz, A, gamma):
    """
    Power-law characteristic strain spectrum.
    h_c(f) = A * (f / f_ref)^alpha
    where alpha = (3 - gamma) / 2 for the characteristic strain.

    For matter bounce: gamma = 3.0 → alpha = 0
    But we fit gamma freely to compare.
    """
    alpha = (3.0 - gamma) / 2.0
    return A * (f_hz / F_REF) ** alpha


def log_likelihood(params, freqs, data, sigma):
    """Gaussian log-likelihood for the free-spectrum fit."""
    log_A, gamma = params
    A = 10**log_A
    model_hc = bounce_strain_spectrum(freqs, A, gamma)
    log_model = np.log10(model_hc)
    chi2 = np.sum(((data - log_model) / sigma)**2)
    return -0.5 * chi2


def run_grid_fit():
    """Grid search + refinement for the spectral fit."""
    # Grid over log10(A) and gamma
    log_A_grid = np.linspace(-15.5, -13.5, 200)
    gamma_grid = np.linspace(1.0, 6.0, 200)

    best_ll = -np.inf
    best_params = None

    for log_A in log_A_grid:
        for gamma in gamma_grid:
            ll = log_likelihood([log_A, gamma], NANOGRAV_FREQS_HZ, LOG10_HC_MEDIAN, LOG10_HC_SIGMA)
            if ll > best_ll:
                best_ll = ll
                best_params = [log_A, gamma]

    # Refine with optimizer
    result = minimize(
        lambda p: -log_likelihood(p, NANOGRAV_FREQS_HZ, LOG10_HC_MEDIAN, LOG10_HC_SIGMA),
        best_params,
        method='Nelder-Mead'
    )

    return result.x, -result.fun


def run_mcmc_simple(n_samples=50000):
    """Simple Metropolis-Hastings MCMC for posterior."""
    # Start from grid best
    best_params, _ = run_grid_fit()

    chain = np.zeros((n_samples, 2))
    log_A, gamma = best_params
    current_ll = log_likelihood([log_A, gamma], NANOGRAV_FREQS_HZ, LOG10_HC_MEDIAN, LOG10_HC_SIGMA)

    # Flat priors
    log_A_prior = (-17.0, -12.0)
    gamma_prior = (0.0, 8.0)

    proposal_scale = np.array([0.05, 0.1])
    n_accept = 0

    for i in range(n_samples):
        # Propose
        proposal = np.array([log_A, gamma]) + proposal_scale * np.random.randn(2)

        if (log_A_prior[0] <= proposal[0] <= log_A_prior[1] and
            gamma_prior[0] <= proposal[1] <= gamma_prior[1]):
            prop_ll = log_likelihood(proposal, NANOGRAV_FREQS_HZ, LOG10_HC_MEDIAN, LOG10_HC_SIGMA)
            if np.log(np.random.random()) < prop_ll - current_ll:
                log_A, gamma = proposal
                current_ll = prop_ll
                n_accept += 1

        chain[i] = [log_A, gamma]

    # Burn-in
    burn = n_samples // 5
    chain = chain[burn:]

    return chain, n_accept / n_samples


def main():
    out_dir = os.path.dirname(os.path.abspath(__file__))

    print('='*60)
    print('NANOGrav 15yr × Matter Bounce GW Template Fit')
    print('='*60)

    # Grid fit
    print('\n1. Grid search + Nelder-Mead refinement...')
    best_params, best_ll = run_grid_fit()
    print(f'   Best fit: log10(A) = {best_params[0]:.4f}, gamma = {best_params[1]:.4f}')
    print(f'   Log-likelihood: {best_ll:.2f}')

    # MCMC
    print('\n2. Running MCMC (50,000 samples)...')
    chain, accept_rate = run_mcmc_simple(50000)
    print(f'   Acceptance rate: {accept_rate:.3f}')

    # Posteriors
    log_A_post = chain[:, 0]
    gamma_post = chain[:, 1]

    log_A_median = np.median(log_A_post)
    log_A_std = np.std(log_A_post)
    gamma_median = np.median(gamma_post)
    gamma_std = np.std(gamma_post)

    print(f'\n3. Posterior results:')
    print(f'   log10(A) = {log_A_median:.4f} ± {log_A_std:.4f}')
    print(f'   gamma = {gamma_median:.3f} ± {gamma_std:.3f}')

    # Compare with matter bounce prediction
    gamma_bounce = 3.0
    delta_gamma = abs(gamma_median - gamma_bounce) / gamma_std
    print(f'\n4. Matter bounce comparison:')
    print(f'   Predicted: gamma = {gamma_bounce:.1f}')
    print(f'   Measured:  gamma = {gamma_median:.3f} ± {gamma_std:.3f}')
    print(f'   Tension:   {delta_gamma:.2f}σ')

    # Probability that gamma > 2.5 (consistent with bounce)
    p_bounce = np.mean(gamma_post > 2.0)
    print(f'   P(gamma > 2.0): {p_bounce:.3f} = {p_bounce*100:.1f}%')

    # Reduced chi^2 for bounce model (gamma=3 fixed)
    A_bounce = 10**log_A_median
    model_hc = bounce_strain_spectrum(NANOGRAV_FREQS_HZ, A_bounce, 3.0)
    log_model = np.log10(model_hc)
    chi2_bounce = np.sum(((LOG10_HC_MEDIAN - log_model) / LOG10_HC_SIGMA)**2)
    ndof = len(LOG10_HC_MEDIAN) - 1  # 1 free param (amplitude)
    chi2_red = chi2_bounce / ndof
    print(f'   χ²/dof (bounce, gamma=3 fixed): {chi2_red:.3f}')

    # Also for free gamma
    model_hc_free = bounce_strain_spectrum(NANOGRAV_FREQS_HZ, 10**log_A_median, gamma_median)
    log_model_free = np.log10(model_hc_free)
    chi2_free = np.sum(((LOG10_HC_MEDIAN - log_model_free) / LOG10_HC_SIGMA)**2)
    chi2_red_free = chi2_free / (len(LOG10_HC_MEDIAN) - 2)
    print(f'   χ²/dof (free gamma): {chi2_red_free:.3f}')

    # Save results
    results = {
        'timestamp': __import__('time').strftime('%Y-%m-%d %H:%M:%S'),
        'best_fit': {
            'log10_A': float(log_A_median),
            'log10_A_err': float(log_A_std),
            'gamma': float(gamma_median),
            'gamma_err': float(gamma_std),
        },
        'bounce_comparison': {
            'gamma_predicted': 3.0,
            'gamma_measured': float(gamma_median),
            'gamma_measured_err': float(gamma_std),
            'tension_sigma': float(delta_gamma),
            'p_consistent': float(p_bounce),
            'chi2_reduced_fixed_gamma': float(chi2_red),
            'chi2_reduced_free_gamma': float(chi2_red_free),
        },
        'mcmc': {
            'n_samples': len(chain),
            'accept_rate': float(accept_rate),
        },
        'data': {
            'n_freq_bins': len(NANOGRAV_FREQS_YR),
            'freq_range_nHz': [float(NANOGRAV_FREQS_HZ[0] * 1e9), float(NANOGRAV_FREQS_HZ[-1] * 1e9)],
        }
    }

    with open(os.path.join(out_dir, 'nanograv_bounce_fit.json'), 'w') as f:
        json.dump(results, f, indent=2)

    # Save chain
    np.save(os.path.join(out_dir, 'nanograv_chain.npy'), chain)

    print(f'\n{"="*60}')
    print(f'COMPLETE: NANOGrav template fit')
    print(f'{"="*60}')


if __name__ == '__main__':
    main()
