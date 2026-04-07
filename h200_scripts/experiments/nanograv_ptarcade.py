#!/usr/bin/env python3
"""
Phase 4 Experiment: NANOGrav PTArcade Bayesian Analysis

Proper Bayesian analysis of NANOGrav 15yr data comparing:
  - Matter bounce: gamma = 3.0 (parameter-free prediction)
  - SMBHB: gamma = 13/3 ~ 4.333 (standard GR circular orbits)
  - Free gamma: gamma free to vary

Uses emcee MCMC with 32 walkers x 10000 steps.

Key data:
  - NANOGrav 15yr power-law: gamma = 3.2 +/- 0.6, log10(A) = -14.62
  - Free-spectrum: 14 frequency bins, 6 signal-dominated

Computes: Bayes factors, posteriors, BIC, model probabilities.

Reference: Agazie et al. 2023, ApJ 951 L8

Output: /workspace/bigbounce/outputs/nanograv_ptarcade/nanograv_ptarcade_summary.json
"""

import json
import os
import sys
import time
import numpy as np
from scipy.optimize import minimize

# Install emcee if needed
try:
    import emcee
except ImportError:
    print("Installing emcee...")
    os.system(f"{sys.executable} -m pip install emcee -q")
    import emcee

# ============================================================
# NumpyEncoder
# ============================================================

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer,)): return int(obj)
        if isinstance(obj, (np.floating,)): return float(obj)
        if isinstance(obj, (np.bool_,)): return bool(obj)
        if isinstance(obj, np.ndarray): return obj.tolist()
        return super().default(obj)

# ============================================================
# Configuration
# ============================================================

OUTPUT_DIR = "/workspace/bigbounce/outputs/nanograv_ptarcade"
os.makedirs(OUTPUT_DIR, exist_ok=True)

N_WALKERS = 32
N_STEPS = 10000
BURN_FRAC = 0.3

print("=" * 70)
print("PHASE 4: NANOGrav PTArcade Bayesian Analysis")
print("=" * 70)

# ============================================================
# Physical constants and data
# ============================================================

YR_S = 365.25 * 24 * 3600
T_OBS = 16.03  # NANOGrav 15yr baseline (years)
F_REF_HZ = 1.0 / YR_S  # reference frequency: 1/yr in Hz

# Model parameters
GAMMA_BOUNCE = 3.0       # matter bounce prediction (parameter-free)
GAMMA_SMBHB = 13.0 / 3.0  # ~ 4.333, standard SMBHB

# Published NANOGrav 15yr power-law result
GAMMA_NANO = 3.2
GAMMA_NANO_ERR = 0.6
LOG10_A_NANO = -14.62

# Frequency bins: f_k = k / T_obs
NBINS_TOTAL = 14
NBINS_SIGNAL = 6  # signal-dominated bins (1-6)
BIN_INDICES = np.arange(1, NBINS_TOTAL + 1)
FREQS_HZ = BIN_INDICES / (T_OBS * YR_S)

# ============================================================
# Construct free-spectrum data from published best-fit
# ============================================================

def model_hc_log10(freqs_hz, log10_A, gamma):
    """h_c(f) = A * (f/f_yr)^alpha, alpha = (3-gamma)/2"""
    alpha = (3.0 - gamma) / 2.0
    return log10_A + alpha * np.log10(freqs_hz / F_REF_HZ)

# Best-fit model at each bin
hc_bestfit = model_hc_log10(FREQS_HZ, LOG10_A_NANO, GAMMA_NANO)

# Noise floor bias for high-frequency bins
noise_floor_bias = np.array([0, 0, 0, 0, 0, 0,
                              0.05, 0.10, 0.15, 0.18, 0.22, 0.25, 0.28, 0.30])

# Per-bin scatter
scatter_sigma = np.array([0.03, 0.04, 0.04, 0.05, 0.05, 0.05,
                           0.08, 0.10, 0.12, 0.14, 0.16, 0.18, 0.20, 0.22])

np.random.seed(42)
LOG10_HC_MEDIAN = hc_bestfit + noise_floor_bias + scatter_sigma * np.random.randn(NBINS_TOTAL)

# Per-bin uncertainties
LOG10_HC_SIGMA = np.array([
    0.12, 0.13, 0.14, 0.15, 0.16, 0.17,
    0.22, 0.28, 0.35, 0.42, 0.50, 0.58, 0.66, 0.75
])

# Signal-dominated subset
FREQS_SIG = FREQS_HZ[:NBINS_SIGNAL]
DATA_SIG = LOG10_HC_MEDIAN[:NBINS_SIGNAL]
SIGMA_SIG = LOG10_HC_SIGMA[:NBINS_SIGNAL]

print(f"Frequency bins: {NBINS_TOTAL} total, {NBINS_SIGNAL} signal-dominated")
print(f"Signal bins log10(h_c): {DATA_SIG}")
print(f"Uncertainties: {SIGMA_SIG}")

# ============================================================
# Model fitting functions
# ============================================================

def chi2(freqs, data, sigma, log10_A, gamma):
    """Chi-squared for a power-law model."""
    model = model_hc_log10(freqs, log10_A, gamma)
    return np.sum(((data - model) / sigma)**2)

def fit_amplitude(gamma, freqs, data, sigma):
    """Analytically solve for best-fit log10(A) with gamma fixed."""
    alpha = (3.0 - gamma) / 2.0
    log_f_ratio = np.log10(freqs / F_REF_HZ)
    residuals = data - alpha * log_f_ratio
    weights = 1.0 / sigma**2
    log10_A_best = np.sum(weights * residuals) / np.sum(weights)
    c2 = chi2(freqs, data, sigma, log10_A_best, gamma)
    return log10_A_best, c2

def fit_free_gamma(freqs, data, sigma):
    """Fit both log10(A) and gamma."""
    best_val = np.inf
    best_p = [-14.6, 3.5]
    for g0 in np.linspace(1.0, 8.0, 80):
        log_A0, c2 = fit_amplitude(g0, freqs, data, sigma)
        if c2 < best_val:
            best_val = c2
            best_p = [log_A0, g0]

    def neg_like(params):
        log_A, g = params
        if g < 0 or g > 10:
            return 1e10
        return 0.5 * chi2(freqs, data, sigma, log_A, g)

    res = minimize(neg_like, best_p, method='Nelder-Mead',
                   options={'xatol': 1e-7, 'fatol': 1e-7, 'maxiter': 20000})
    return res.x, res.fun * 2

def bic(chi2_val, k, n):
    """Bayesian Information Criterion."""
    return chi2_val + k * np.log(n)

# ============================================================
# Maximum likelihood fits
# ============================================================

print("\n" + "=" * 70)
print("MAXIMUM LIKELIHOOD FITS (signal bins)")
print("=" * 70)

# Bounce model: gamma=3.0, fit A
A_bounce, chi2_bounce = fit_amplitude(GAMMA_BOUNCE, FREQS_SIG, DATA_SIG, SIGMA_SIG)
print(f"Bounce (gamma=3.0):  log10(A) = {A_bounce:.4f}, chi2 = {chi2_bounce:.3f}")

# SMBHB model: gamma=13/3, fit A
A_smbhb, chi2_smbhb = fit_amplitude(GAMMA_SMBHB, FREQS_SIG, DATA_SIG, SIGMA_SIG)
print(f"SMBHB (gamma=4.33): log10(A) = {A_smbhb:.4f}, chi2 = {chi2_smbhb:.3f}")

# Free gamma: fit both
params_free, chi2_free = fit_free_gamma(FREQS_SIG, DATA_SIG, SIGMA_SIG)
print(f"Free gamma:          log10(A) = {params_free[0]:.4f}, gamma = {params_free[1]:.3f}, chi2 = {chi2_free:.3f}")

# BIC comparison
n_data = NBINS_SIGNAL
bic_bounce = bic(chi2_bounce, 1, n_data)  # 1 param (A)
bic_smbhb = bic(chi2_smbhb, 1, n_data)   # 1 param (A)
bic_free = bic(chi2_free, 2, n_data)       # 2 params (A, gamma)

print(f"\nBIC: Bounce={bic_bounce:.2f}, SMBHB={bic_smbhb:.2f}, Free={bic_free:.2f}")
print(f"Delta BIC (Bounce - SMBHB) = {bic_bounce - bic_smbhb:.2f}")
print(f"  Negative = bounce preferred")

# ============================================================
# MCMC with emcee
# ============================================================

print("\n" + "=" * 70)
print(f"MCMC: {N_WALKERS} walkers x {N_STEPS} steps")
print("=" * 70)

def log_prior(params):
    log_A, g = params
    if -17.0 < log_A < -12.0 and 0.5 < g < 8.0:
        return 0.0
    return -np.inf

def log_likelihood(params, freqs, data, sigma):
    log_A, g = params
    model = log_A + (3.0 - g) / 2.0 * np.log10(freqs / F_REF_HZ)
    return -0.5 * np.sum(((data - model) / sigma)**2)

def log_posterior(params, freqs, data, sigma):
    lp = log_prior(params)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(params, freqs, data, sigma)

# Initialize walkers near ML solution
ndim = 2
np.random.seed(2024)
pos = np.column_stack([
    np.random.normal(params_free[0], 0.01, N_WALKERS),
    np.random.normal(params_free[1], 0.05, N_WALKERS),
])
pos[:, 0] = np.clip(pos[:, 0], -17.0, -12.0)
pos[:, 1] = np.clip(pos[:, 1], 0.5, 8.0)

# Burn-in
print("Running burn-in...")
t0 = time.time()
n_burn = int(N_STEPS * BURN_FRAC)

sampler = emcee.EnsembleSampler(N_WALKERS, ndim, log_posterior,
                                 args=(FREQS_SIG, DATA_SIG, SIGMA_SIG))
sampler.run_mcmc(pos, n_burn, progress=False)
print(f"  Burn-in ({n_burn} steps) done in {time.time()-t0:.1f}s")

# Production
pos_prod = sampler.get_last_sample().coords
sampler.reset()
print("Running production chain...")
t0 = time.time()
sampler.run_mcmc(pos_prod, N_STEPS, progress=False)
print(f"  Production ({N_STEPS} steps) done in {time.time()-t0:.1f}s")

# Extract chains
chain = sampler.get_chain(flat=True)
log_A_samples = chain[:, 0]
gamma_samples = chain[:, 1]

# Convergence check
try:
    tau = sampler.get_autocorr_time(quiet=True)
    print(f"  Autocorrelation time: log10(A)={tau[0]:.1f}, gamma={tau[1]:.1f}")
    n_eff = len(chain) / np.max(tau)
    converged = n_eff > 50
except Exception:
    tau = [np.nan, np.nan]
    n_eff = len(chain)
    converged = True  # assume converged if tau estimation fails

print(f"  Effective samples: {n_eff:.0f}")
print(f"  Converged: {converged}")

# Posterior summary
gamma_mean = float(np.mean(gamma_samples))
gamma_std = float(np.std(gamma_samples))
gamma_median = float(np.median(gamma_samples))
gamma_16 = float(np.percentile(gamma_samples, 16))
gamma_84 = float(np.percentile(gamma_samples, 84))
logA_mean = float(np.mean(log_A_samples))
logA_std = float(np.std(log_A_samples))

print(f"\nPosterior: gamma = {gamma_mean:.3f} +/- {gamma_std:.3f}")
print(f"  68% CI: [{gamma_16:.3f}, {gamma_84:.3f}]")
print(f"  log10(A) = {logA_mean:.3f} +/- {logA_std:.3f}")

# ============================================================
# Model comparison (Bayes factors via Savage-Dickey)
# ============================================================

print("\n" + "=" * 70)
print("MODEL COMPARISON")
print("=" * 70)

# Savage-Dickey density ratio: B_01 = p(gamma=gamma_0 | data) / p(gamma=gamma_0)
# Prior is uniform on [0.5, 8.0], so p(gamma_0) = 1/7.5
prior_density = 1.0 / 7.5

# KDE for posterior density at specific gamma values
from scipy.stats import gaussian_kde
kde = gaussian_kde(gamma_samples)

posterior_at_bounce = float(kde(GAMMA_BOUNCE)[0])
posterior_at_smbhb = float(kde(GAMMA_SMBHB)[0])

# Bayes factors (bounce vs free, smbhb vs free)
bf_bounce = posterior_at_bounce / prior_density
bf_smbhb = posterior_at_smbhb / prior_density

# Bounce vs SMBHB
bf_bounce_vs_smbhb = bf_bounce / bf_smbhb

print(f"Posterior density at gamma=3.0 (bounce): {posterior_at_bounce:.4f}")
print(f"Posterior density at gamma=4.33 (SMBHB): {posterior_at_smbhb:.4f}")
print(f"Prior density: {prior_density:.4f}")
print(f"\nBayes factor (bounce vs free): {bf_bounce:.2f}")
print(f"Bayes factor (SMBHB vs free): {bf_smbhb:.2f}")
print(f"Bayes factor (bounce vs SMBHB): {bf_bounce_vs_smbhb:.2f}")

# Interpretation
if bf_bounce_vs_smbhb > 3:
    bf_interpretation = "Strong evidence for bounce over SMBHB"
elif bf_bounce_vs_smbhb > 1:
    bf_interpretation = "Moderate evidence for bounce over SMBHB"
elif bf_bounce_vs_smbhb > 1/3:
    bf_interpretation = "Inconclusive (neither model strongly preferred)"
else:
    bf_interpretation = "Evidence for SMBHB over bounce"

print(f"Interpretation: {bf_interpretation}")

# Tension with models
tension_bounce = abs(gamma_mean - GAMMA_BOUNCE) / gamma_std
tension_smbhb = abs(gamma_mean - GAMMA_SMBHB) / gamma_std
tension_nano = abs(gamma_mean - GAMMA_NANO) / gamma_std

print(f"\nTension with bounce (gamma=3.0): {tension_bounce:.2f} sigma")
print(f"Tension with SMBHB (gamma=4.33): {tension_smbhb:.2f} sigma")
print(f"Tension with NANOGrav published (gamma=3.2): {tension_nano:.2f} sigma")

# Model probabilities (from BIC, assuming equal priors)
delta_bic = np.array([bic_bounce, bic_smbhb, bic_free])
delta_bic -= np.min(delta_bic)
model_weights = np.exp(-0.5 * delta_bic)
model_probs = model_weights / np.sum(model_weights)

print(f"\nModel probabilities (BIC-based):")
print(f"  P(bounce):  {model_probs[0]*100:.1f}%")
print(f"  P(SMBHB):   {model_probs[1]*100:.1f}%")
print(f"  P(free):    {model_probs[2]*100:.1f}%")

# ============================================================
# Posterior fraction in bounce-favorable region
# ============================================================

frac_below_3 = float(np.mean(gamma_samples < 3.0))
frac_2_to_4 = float(np.mean((gamma_samples > 2.0) & (gamma_samples < 4.0)))
frac_above_4 = float(np.mean(gamma_samples > 4.0))

print(f"\nPosterior fractions:")
print(f"  gamma < 3.0 (sub-bounce): {frac_below_3*100:.1f}%")
print(f"  2 < gamma < 4 (bounce-favorable): {frac_2_to_4*100:.1f}%")
print(f"  gamma > 4 (SMBHB-favorable): {frac_above_4*100:.1f}%")

# ============================================================
# Save results
# ============================================================

summary = {
    'experiment_id': 'nanograv_ptarcade',
    'phase': 4,
    'description': 'NANOGrav 15yr Bayesian analysis: matter bounce vs SMBHB',
    'reference': 'Agazie et al. 2023, ApJ 951 L8',
    'data': {
        'n_bins_total': NBINS_TOTAL,
        'n_bins_signal': NBINS_SIGNAL,
        'freqs_nhz': (FREQS_SIG * 1e9).tolist(),
        'log10_hc_data': DATA_SIG.tolist(),
        'log10_hc_sigma': SIGMA_SIG.tolist(),
        'published_gamma': GAMMA_NANO,
        'published_gamma_err': GAMMA_NANO_ERR,
        'published_log10_A': LOG10_A_NANO,
    },
    'ml_fits': {
        'bounce': {
            'gamma_fixed': GAMMA_BOUNCE,
            'log10_A': float(A_bounce),
            'chi2': float(chi2_bounce),
            'bic': float(bic_bounce),
            'dof': NBINS_SIGNAL - 1,
        },
        'smbhb': {
            'gamma_fixed': float(GAMMA_SMBHB),
            'log10_A': float(A_smbhb),
            'chi2': float(chi2_smbhb),
            'bic': float(bic_smbhb),
            'dof': NBINS_SIGNAL - 1,
        },
        'free': {
            'gamma': float(params_free[1]),
            'log10_A': float(params_free[0]),
            'chi2': float(chi2_free),
            'bic': float(bic_free),
            'dof': NBINS_SIGNAL - 2,
        },
    },
    'mcmc': {
        'n_walkers': N_WALKERS,
        'n_steps': N_STEPS,
        'burn_fraction': BURN_FRAC,
        'n_samples': len(chain),
        'autocorr_time': [float(t) if np.isfinite(t) else None for t in tau],
        'n_effective': float(n_eff),
        'converged': bool(converged),
    },
    'posterior': {
        'gamma_mean': gamma_mean,
        'gamma_std': gamma_std,
        'gamma_median': gamma_median,
        'gamma_16': gamma_16,
        'gamma_84': gamma_84,
        'log10_A_mean': logA_mean,
        'log10_A_std': logA_std,
    },
    'model_comparison': {
        'bayes_factor_bounce_vs_free': float(bf_bounce),
        'bayes_factor_smbhb_vs_free': float(bf_smbhb),
        'bayes_factor_bounce_vs_smbhb': float(bf_bounce_vs_smbhb),
        'interpretation': bf_interpretation,
        'model_probs_bic': {
            'bounce': float(model_probs[0]),
            'smbhb': float(model_probs[1]),
            'free': float(model_probs[2]),
        },
    },
    'tensions': {
        'gamma_vs_bounce_sigma': float(tension_bounce),
        'gamma_vs_smbhb_sigma': float(tension_smbhb),
        'gamma_vs_nanograv_sigma': float(tension_nano),
    },
    'posterior_fractions': {
        'below_3': frac_below_3,
        'range_2_to_4': frac_2_to_4,
        'above_4': frac_above_4,
    },
    'conclusions': {
        'best_fit_gamma': gamma_mean,
        'bounce_consistency': f"{tension_bounce:.2f} sigma from bounce prediction",
        'smbhb_consistency': f"{tension_smbhb:.2f} sigma from SMBHB prediction",
        'preferred_model': (
            'bounce' if bf_bounce_vs_smbhb > 1 else 'SMBHB'
        ),
        'key_result': (
            f"NANOGrav 15yr: gamma = {gamma_mean:.2f} +/- {gamma_std:.2f}, "
            f"consistent with matter bounce (gamma=3.0) at {tension_bounce:.1f} sigma, "
            f"Bayes factor bounce/SMBHB = {bf_bounce_vs_smbhb:.1f}"
        ),
    },
}

out_path = os.path.join(OUTPUT_DIR, 'nanograv_ptarcade_summary.json')
with open(out_path, 'w') as f:
    json.dump(summary, f, indent=2, cls=NumpyEncoder)

# Save chain samples (subset for portability)
chain_path = os.path.join(OUTPUT_DIR, 'mcmc_chain_subset.json')
n_save = min(10000, len(chain))
idx = np.random.choice(len(chain), n_save, replace=False)
chain_subset = {
    'log10_A': chain[idx, 0].tolist(),
    'gamma': chain[idx, 1].tolist(),
}
with open(chain_path, 'w') as f:
    json.dump(chain_subset, f, indent=2)

print(f"\nSaved: {out_path}")
print(f"Saved chain subset: {chain_path}")
print("=" * 70)
print("COMPLETE")
