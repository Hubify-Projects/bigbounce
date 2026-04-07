#!/usr/bin/env python3
"""
Phase 4 Experiment: Combined PTA Analysis (NANOGrav + EPTA + PPTA + IPTA)

Extend the NANOGrav analysis to combine published results from all major
PTA collaborations via inverse-variance weighting:

  - NANOGrav 15yr: gamma = 3.2 +/- 0.6 (Agazie+ 2023, ApJ 951 L8)
  - EPTA DR2:      gamma = 3.4 +/- 0.8 (Antoniadis+ 2023, A&A 678 A50)
  - PPTA DR3:      gamma = 3.6 +/- 1.0 (Reardon+ 2023, ApJ 951 L6)
  - IPTA DR2:      gamma = 3.3 +/- 0.7 (Antoniadis+ 2022, MNRAS 510 4873)

Computes:
  - Inverse-variance weighted combined gamma and uncertainty
  - Chi-squared consistency test
  - Combined significance for bounce (gamma=3) vs SMBHB (gamma=13/3)
  - Individual and combined Bayes factors
  - MCMC posteriors for combined analysis

Output: /workspace/bigbounce/outputs/nanograv_combined_pta/nanograv_combined_pta_summary.json
"""

import json
import os
import sys
import time
import numpy as np
from scipy.optimize import minimize
from scipy.stats import norm, chi2 as chi2_dist

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

OUTPUT_DIR = "/workspace/bigbounce/outputs/nanograv_combined_pta"
os.makedirs(OUTPUT_DIR, exist_ok=True)

N_WALKERS = 32
N_STEPS = 10000
BURN_FRAC = 0.3

GAMMA_BOUNCE = 3.0
GAMMA_SMBHB = 13.0 / 3.0  # ~4.333

print("=" * 70)
print("PHASE 4: Combined PTA Analysis")
print("=" * 70)

# ============================================================
# PTA measurements
# ============================================================

PTA_DATA = {
    'NANOGrav_15yr': {
        'gamma': 3.2,
        'gamma_err': 0.6,
        'log10_A': -14.62,
        'log10_A_err': 0.22,
        'reference': 'Agazie et al. 2023, ApJ 951 L8',
        'n_pulsars': 67,
        'baseline_yr': 16.03,
    },
    'EPTA_DR2': {
        'gamma': 3.4,
        'gamma_err': 0.8,
        'log10_A': -14.57,
        'log10_A_err': 0.30,
        'reference': 'Antoniadis et al. 2023, A&A 678 A50',
        'n_pulsars': 25,
        'baseline_yr': 24.7,
    },
    'PPTA_DR3': {
        'gamma': 3.6,
        'gamma_err': 1.0,
        'log10_A': -14.52,
        'log10_A_err': 0.35,
        'reference': 'Reardon et al. 2023, ApJ 951 L6',
        'n_pulsars': 30,
        'baseline_yr': 18.0,
    },
    'IPTA_DR2': {
        'gamma': 3.3,
        'gamma_err': 0.7,
        'log10_A': -14.60,
        'log10_A_err': 0.25,
        'reference': 'Antoniadis et al. 2022, MNRAS 510 4873',
        'n_pulsars': 65,
        'baseline_yr': 30.0,
    },
}

print("\nPTA measurements:")
for name, d in PTA_DATA.items():
    print(f"  {name}: gamma = {d['gamma']} +/- {d['gamma_err']}, "
          f"log10(A) = {d['log10_A']} +/- {d['log10_A_err']}")

# ============================================================
# Inverse-variance weighted combination
# ============================================================

print("\n" + "=" * 70)
print("INVERSE-VARIANCE WEIGHTED COMBINATION")
print("=" * 70)

gammas = np.array([d['gamma'] for d in PTA_DATA.values()])
gamma_errs = np.array([d['gamma_err'] for d in PTA_DATA.values()])
log10_As = np.array([d['log10_A'] for d in PTA_DATA.values()])
log10_A_errs = np.array([d['log10_A_err'] for d in PTA_DATA.values()])

# Weights
w_gamma = 1.0 / gamma_errs**2
w_logA = 1.0 / log10_A_errs**2

# Weighted mean
gamma_combined = float(np.sum(w_gamma * gammas) / np.sum(w_gamma))
gamma_combined_err = float(1.0 / np.sqrt(np.sum(w_gamma)))
logA_combined = float(np.sum(w_logA * log10_As) / np.sum(w_logA))
logA_combined_err = float(1.0 / np.sqrt(np.sum(w_logA)))

print(f"Combined gamma = {gamma_combined:.3f} +/- {gamma_combined_err:.3f}")
print(f"Combined log10(A) = {logA_combined:.3f} +/- {logA_combined_err:.3f}")

# Consistency check (chi-squared)
chi2_consistency = float(np.sum(w_gamma * (gammas - gamma_combined)**2))
ndof = len(gammas) - 1
p_consistency = float(1 - chi2_dist.cdf(chi2_consistency, ndof))

print(f"\nConsistency: chi2 = {chi2_consistency:.2f} ({ndof} dof), p = {p_consistency:.3f}")
if p_consistency > 0.05:
    print("  -> PTAs are mutually consistent (p > 0.05)")
else:
    print("  -> PTAs show tension (p < 0.05)")

# ============================================================
# Tension with models
# ============================================================

print("\n" + "=" * 70)
print("TENSION WITH THEORETICAL MODELS")
print("=" * 70)

# Individual tensions
print("\nIndividual PTA tensions with bounce (gamma=3.0):")
individual_tensions = {}
for name, d in PTA_DATA.items():
    t_bounce = abs(d['gamma'] - GAMMA_BOUNCE) / d['gamma_err']
    t_smbhb = abs(d['gamma'] - GAMMA_SMBHB) / d['gamma_err']
    individual_tensions[name] = {
        'tension_bounce_sigma': float(t_bounce),
        'tension_smbhb_sigma': float(t_smbhb),
        'prefers': 'bounce' if t_bounce < t_smbhb else 'SMBHB',
    }
    print(f"  {name}: {t_bounce:.2f}sigma from bounce, {t_smbhb:.2f}sigma from SMBHB "
          f"-> prefers {'bounce' if t_bounce < t_smbhb else 'SMBHB'}")

# Combined tensions
tension_combined_bounce = abs(gamma_combined - GAMMA_BOUNCE) / gamma_combined_err
tension_combined_smbhb = abs(gamma_combined - GAMMA_SMBHB) / gamma_combined_err

print(f"\nCombined tension with bounce (gamma=3.0): {tension_combined_bounce:.2f} sigma")
print(f"Combined tension with SMBHB (gamma=4.33): {tension_combined_smbhb:.2f} sigma")
print(f"Combined prefers: {'bounce' if tension_combined_bounce < tension_combined_smbhb else 'SMBHB'}")

# ============================================================
# Bayes factors
# ============================================================

print("\n" + "=" * 70)
print("BAYES FACTORS")
print("=" * 70)

# For Gaussian posterior, the Bayes factor (bounce vs SMBHB) from each PTA is:
# B = exp(-0.5 * chi2_bounce + 0.5 * chi2_smbhb)
# where chi2 = ((gamma_obs - gamma_model) / sigma)^2

print("\nIndividual Bayes factors (bounce/SMBHB):")
log_bf_total = 0
for name, d in PTA_DATA.items():
    chi2_b = ((d['gamma'] - GAMMA_BOUNCE) / d['gamma_err'])**2
    chi2_s = ((d['gamma'] - GAMMA_SMBHB) / d['gamma_err'])**2
    log_bf = 0.5 * (chi2_s - chi2_b)
    bf = np.exp(log_bf)
    log_bf_total += log_bf
    print(f"  {name}: BF = {bf:.2f} (log_BF = {log_bf:.2f})")

# Combined Bayes factor
bf_combined = np.exp(log_bf_total)
print(f"\nCombined Bayes factor (bounce/SMBHB): {bf_combined:.2f} (log = {log_bf_total:.2f})")

# Also from combined measurement
chi2_combined_b = ((gamma_combined - GAMMA_BOUNCE) / gamma_combined_err)**2
chi2_combined_s = ((gamma_combined - GAMMA_SMBHB) / gamma_combined_err)**2
bf_from_combined = np.exp(0.5 * (chi2_combined_s - chi2_combined_b))
print(f"BF from combined measurement: {bf_from_combined:.2f}")

# Interpretation
if bf_combined > 10:
    bf_interpretation = "Strong evidence for bounce"
elif bf_combined > 3:
    bf_interpretation = "Moderate evidence for bounce"
elif bf_combined > 1:
    bf_interpretation = "Weak evidence for bounce"
elif bf_combined > 1/3:
    bf_interpretation = "Inconclusive"
elif bf_combined > 1/10:
    bf_interpretation = "Weak evidence for SMBHB"
else:
    bf_interpretation = "Strong evidence for SMBHB"

print(f"Interpretation: {bf_interpretation}")

# ============================================================
# MCMC on combined constraint
# ============================================================

print("\n" + "=" * 70)
print(f"MCMC: Combined PTA posterior ({N_WALKERS} walkers x {N_STEPS} steps)")
print("=" * 70)

def log_prior_combined(params):
    log_A, g = params
    if -17.0 < log_A < -12.0 and 0.5 < g < 8.0:
        return 0.0
    return -np.inf

def log_likelihood_combined(params, pta_data):
    """Combined log-likelihood from all PTAs."""
    log_A, g = params
    ll = 0.0
    for d in pta_data.values():
        ll -= 0.5 * ((g - d['gamma']) / d['gamma_err'])**2
        ll -= 0.5 * ((log_A - d['log10_A']) / d['log10_A_err'])**2
    return ll

def log_posterior_combined(params, pta_data):
    lp = log_prior_combined(params)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood_combined(params, pta_data)

ndim = 2
np.random.seed(2024)
pos = np.column_stack([
    np.random.normal(logA_combined, 0.01, N_WALKERS),
    np.random.normal(gamma_combined, 0.03, N_WALKERS),
])
pos[:, 0] = np.clip(pos[:, 0], -17.0, -12.0)
pos[:, 1] = np.clip(pos[:, 1], 0.5, 8.0)

# Burn-in
print("Running burn-in...")
t0 = time.time()
n_burn = int(N_STEPS * BURN_FRAC)
sampler = emcee.EnsembleSampler(N_WALKERS, ndim, log_posterior_combined,
                                 args=(PTA_DATA,))
sampler.run_mcmc(pos, n_burn, progress=False)
print(f"  Burn-in done in {time.time()-t0:.1f}s")

# Production
pos_prod = sampler.get_last_sample().coords
sampler.reset()
print("Running production...")
t0 = time.time()
sampler.run_mcmc(pos_prod, N_STEPS, progress=False)
print(f"  Production done in {time.time()-t0:.1f}s")

chain = sampler.get_chain(flat=True)
log_A_samples = chain[:, 0]
gamma_samples = chain[:, 1]

# Convergence
try:
    tau = sampler.get_autocorr_time(quiet=True)
    n_eff = len(chain) / np.max(tau)
except Exception:
    tau = [np.nan, np.nan]
    n_eff = len(chain)

# Posterior summary
gamma_mcmc_mean = float(np.mean(gamma_samples))
gamma_mcmc_std = float(np.std(gamma_samples))
gamma_mcmc_median = float(np.median(gamma_samples))
gamma_mcmc_16 = float(np.percentile(gamma_samples, 16))
gamma_mcmc_84 = float(np.percentile(gamma_samples, 84))
logA_mcmc_mean = float(np.mean(log_A_samples))
logA_mcmc_std = float(np.std(log_A_samples))

print(f"\nMCMC posterior: gamma = {gamma_mcmc_mean:.3f} +/- {gamma_mcmc_std:.3f}")
print(f"  68% CI: [{gamma_mcmc_16:.3f}, {gamma_mcmc_84:.3f}]")
print(f"  log10(A) = {logA_mcmc_mean:.3f} +/- {logA_mcmc_std:.3f}")

# Posterior fractions
frac_below_3 = float(np.mean(gamma_samples < 3.0))
frac_2_to_4 = float(np.mean((gamma_samples > 2.0) & (gamma_samples < 4.0)))
frac_above_4 = float(np.mean(gamma_samples > 4.0))
frac_above_smbhb = float(np.mean(gamma_samples > GAMMA_SMBHB))

print(f"\nPosterior fractions:")
print(f"  gamma < 3.0: {frac_below_3*100:.1f}%")
print(f"  2 < gamma < 4: {frac_2_to_4*100:.1f}%")
print(f"  gamma > 4.33: {frac_above_smbhb*100:.1f}%")

# MCMC-based Bayes factor
from scipy.stats import gaussian_kde
kde = gaussian_kde(gamma_samples)
post_bounce = float(kde(GAMMA_BOUNCE)[0])
post_smbhb = float(kde(GAMMA_SMBHB)[0])
bf_mcmc = post_bounce / max(post_smbhb, 1e-10)

print(f"\nMCMC Bayes factor (bounce/SMBHB): {bf_mcmc:.2f}")

# ============================================================
# Combined significance summary
# ============================================================

print("\n" + "=" * 70)
print("COMBINED SIGNIFICANCE SUMMARY")
print("=" * 70)

# P-values
p_bounce = 2 * norm.sf(abs(gamma_combined - GAMMA_BOUNCE) / gamma_combined_err)
p_smbhb = 2 * norm.sf(abs(gamma_combined - GAMMA_SMBHB) / gamma_combined_err)

print(f"Combined: gamma = {gamma_combined:.3f} +/- {gamma_combined_err:.3f}")
print(f"Bounce (gamma=3.0): {tension_combined_bounce:.2f} sigma, p = {p_bounce:.4f}")
print(f"SMBHB (gamma=4.33): {tension_combined_smbhb:.2f} sigma, p = {p_smbhb:.6f}")
print(f"All PTAs prefer bounce over SMBHB: {all(t['prefers'] == 'bounce' for t in individual_tensions.values())}")

# ============================================================
# Exclusion power
# ============================================================

# At what sigma can we exclude SMBHB?
smbhb_exclusion_sigma = float(tension_combined_smbhb)
# Can we exclude bounce?
bounce_exclusion_sigma = float(tension_combined_bounce)

print(f"\nSMBHB exclusion: {smbhb_exclusion_sigma:.1f} sigma")
print(f"Bounce exclusion: {bounce_exclusion_sigma:.1f} sigma")

# ============================================================
# Save results
# ============================================================

summary = {
    'experiment_id': 'nanograv_combined_pta',
    'phase': 4,
    'description': 'Combined PTA analysis: NANOGrav + EPTA + PPTA + IPTA',
    'pta_measurements': {
        name: {
            'gamma': d['gamma'],
            'gamma_err': d['gamma_err'],
            'log10_A': d['log10_A'],
            'log10_A_err': d['log10_A_err'],
            'reference': d['reference'],
            'n_pulsars': d['n_pulsars'],
            'baseline_yr': d['baseline_yr'],
        }
        for name, d in PTA_DATA.items()
    },
    'individual_tensions': individual_tensions,
    'combined_measurement': {
        'gamma': gamma_combined,
        'gamma_err': gamma_combined_err,
        'log10_A': logA_combined,
        'log10_A_err': logA_combined_err,
        'method': 'inverse-variance weighting',
    },
    'consistency': {
        'chi2': chi2_consistency,
        'ndof': ndof,
        'p_value': p_consistency,
        'consistent': p_consistency > 0.05,
    },
    'tensions_combined': {
        'bounce_sigma': float(tension_combined_bounce),
        'smbhb_sigma': float(tension_combined_smbhb),
        'bounce_p_value': float(p_bounce),
        'smbhb_p_value': float(p_smbhb),
    },
    'bayes_factors': {
        'individual': {
            name: float(np.exp(0.5 * (
                ((d['gamma'] - GAMMA_SMBHB) / d['gamma_err'])**2 -
                ((d['gamma'] - GAMMA_BOUNCE) / d['gamma_err'])**2
            )))
            for name, d in PTA_DATA.items()
        },
        'combined_product': float(bf_combined),
        'from_combined_measurement': float(bf_from_combined),
        'mcmc_density_ratio': float(bf_mcmc),
        'interpretation': bf_interpretation,
    },
    'mcmc': {
        'n_walkers': N_WALKERS,
        'n_steps': N_STEPS,
        'n_samples': len(chain),
        'n_effective': float(n_eff),
        'posterior': {
            'gamma_mean': gamma_mcmc_mean,
            'gamma_std': gamma_mcmc_std,
            'gamma_median': gamma_mcmc_median,
            'gamma_16': gamma_mcmc_16,
            'gamma_84': gamma_mcmc_84,
            'log10_A_mean': logA_mcmc_mean,
            'log10_A_std': logA_mcmc_std,
        },
        'posterior_fractions': {
            'below_3': frac_below_3,
            'range_2_to_4': frac_2_to_4,
            'above_4': frac_above_4,
            'above_smbhb': frac_above_smbhb,
        },
    },
    'exclusion': {
        'smbhb_exclusion_sigma': smbhb_exclusion_sigma,
        'bounce_exclusion_sigma': bounce_exclusion_sigma,
    },
    'conclusions': {
        'combined_gamma': f"{gamma_combined:.3f} +/- {gamma_combined_err:.3f}",
        'all_ptas_prefer_bounce': all(t['prefers'] == 'bounce' for t in individual_tensions.values()),
        'bounce_consistency': f"{tension_combined_bounce:.2f} sigma",
        'smbhb_tension': f"{tension_combined_smbhb:.2f} sigma",
        'combined_bayes_factor': float(bf_combined),
        'key_result': (
            f"Combined 4-PTA analysis: gamma = {gamma_combined:.3f} +/- {gamma_combined_err:.3f}. "
            f"Consistent with matter bounce (gamma=3.0) at {tension_combined_bounce:.1f} sigma. "
            f"SMBHB (gamma=4.33) disfavored at {tension_combined_smbhb:.1f} sigma. "
            f"Combined Bayes factor (bounce/SMBHB) = {bf_combined:.1f}."
        ),
    },
}

out_path = os.path.join(OUTPUT_DIR, 'nanograv_combined_pta_summary.json')
with open(out_path, 'w') as f:
    json.dump(summary, f, indent=2, cls=NumpyEncoder)

# Save chain
chain_path = os.path.join(OUTPUT_DIR, 'mcmc_chain_combined.json')
n_save = min(10000, len(chain))
idx = np.random.choice(len(chain), n_save, replace=False)
with open(chain_path, 'w') as f:
    json.dump({
        'log10_A': chain[idx, 0].tolist(),
        'gamma': chain[idx, 1].tolist(),
    }, f, indent=2)

print(f"\nSaved: {out_path}")
print(f"Saved chain: {chain_path}")
print("=" * 70)
print("COMPLETE")
