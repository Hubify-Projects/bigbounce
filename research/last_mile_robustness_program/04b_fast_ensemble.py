#!/usr/bin/env python3
"""
FAST vectorized Monte Carlo Bayes factor ensemble.
Uses closed-form Bayes factor (no numerical integration needed).

For bounce (delta at μ) vs flat prior on [a,b]:
  BF = p(d|bounce) / p(d|flat)
     = N(d; μ, σ) / [(Φ((b-d)/σ) - Φ((a-d)/σ)) / (b-a)]
     = (b-a) × N(d; μ, σ) / [Φ((b-d)/σ) - Φ((a-d)/σ)]
"""
import numpy as np
from scipy.stats import norm

FNL_BOUNCE = -35.0 / 8.0
N_REAL = 100000

def bf_delta_vs_flat(d, sigma, mu_delta, prior_lo, prior_hi):
    """Vectorized Bayes factor: delta(mu_delta) vs flat[prior_lo, prior_hi]."""
    p_delta = norm.pdf(d, loc=mu_delta, scale=sigma)
    # Evidence for flat prior = integral of likelihood × 1/(hi-lo)
    cdf_hi = norm.cdf(prior_hi, loc=d, scale=sigma)
    cdf_lo = norm.cdf(prior_lo, loc=d, scale=sigma)
    p_flat = (cdf_hi - cdf_lo) / (prior_hi - prior_lo)
    return np.where(p_flat > 0, p_delta / p_flat, np.inf)

def bf_delta_vs_delta(d, sigma, mu1, mu2):
    """Vectorized Bayes factor: delta(mu1) vs delta(mu2)."""
    p1 = norm.pdf(d, loc=mu1, scale=sigma)
    p2 = norm.pdf(d, loc=mu2, scale=sigma)
    return np.where(p2 > 0, p1 / p2, np.inf)

print("=" * 75)
print(f"LAST-MILE ROBUSTNESS: 100,000 MONTE CARLO REALIZATIONS")
print(f"Assumes bounce is true: f_NL = -35/8 = -4.375")
print("=" * 75)

rng = np.random.default_rng(42)

# ================================================================
# SAMPLE SURVEY ASSUMPTIONS
# ================================================================

# SPHEREx base σ: log-normal around 0.7
sigma_sp_base = np.clip(rng.lognormal(np.log(0.7), 0.3, N_REAL), 0.3, 3.0)

# MegaMapper base σ: log-normal around 0.5
sigma_mm_base = np.clip(rng.lognormal(np.log(0.5), 0.4, N_REAL), 0.2, 5.0)

# Multi-tracer success (70% works, 30% fails → 3× degradation)
mt_works = rng.random(N_REAL) < 0.7
sigma_mm_mt = np.where(mt_works, sigma_mm_base, sigma_mm_base * 3)

# b_φ nuisance: 0-50% degradation
bphi_deg = 1.0 + rng.uniform(0, 0.5, N_REAL)
sigma_sp = sigma_sp_base * bphi_deg
sigma_mm = sigma_mm_mt * bphi_deg

# GR systematic residual shift
gr_sp = rng.normal(0, 0.3, N_REAL)
gr_mm = rng.normal(0, 0.7, N_REAL)

# Mock observations (bounce is true)
fnl_obs_sp = FNL_BOUNCE + rng.normal(0, 1, N_REAL) * sigma_sp + gr_sp
fnl_obs_mm = FNL_BOUNCE + rng.normal(0, 1, N_REAL) * sigma_mm + gr_mm

# ================================================================
# COMPUTE BAYES FACTORS (fully vectorized, instant)
# ================================================================

bf_sp_tuned = bf_delta_vs_flat(fnl_obs_sp, sigma_sp, FNL_BOUNCE, -15, 15)
bf_sp_ssfsr = bf_delta_vs_delta(fnl_obs_sp, sigma_sp, FNL_BOUNCE, 0.015)
bf_mm_tuned = bf_delta_vs_flat(fnl_obs_mm, sigma_mm, FNL_BOUNCE, -15, 15)
bf_mm_ssfsr = bf_delta_vs_delta(fnl_obs_mm, sigma_mm, FNL_BOUNCE, 0.015)
bf_comb_tuned = bf_sp_tuned * bf_mm_tuned
bf_comb_ssfsr = bf_sp_ssfsr * bf_mm_ssfsr

# ================================================================
# REPORT
# ================================================================

def report(name, bf):
    bf_clean = np.clip(bf, 1e-30, 1e30)
    log_bf = np.log10(bf_clean)
    print(f"\n--- {name} ---")
    print(f"  Median BF:              {np.median(bf_clean):.1f}")
    print(f"  Mean log10(BF):         {np.mean(log_bf):.2f}")
    print(f"  10th pctile BF:         {np.percentile(bf_clean, 10):.2f}")
    print(f"  90th pctile BF:         {np.percentile(bf_clean, 90):.1f}")
    print(f"  P(BF > 3)  [moderate]:  {np.mean(bf > 3)*100:.1f}%")
    print(f"  P(BF > 10) [strong]:    {np.mean(bf > 10)*100:.1f}%")
    print(f"  P(BF > 100)[decisive]:  {np.mean(bf > 100)*100:.1f}%")
    print(f"  P(BF < 1)  [infl wins]: {np.mean(bf < 1)*100:.1f}%")
    print(f"  P(BF < 1/3)[strong inf]:{np.mean(bf < 1/3)*100:.1f}%")

report("SPHEREx vs Tuned Multifield [-15,+15]", bf_sp_tuned)
report("SPHEREx vs Standard Single-Field", bf_sp_ssfsr)
report("MegaMapper vs Tuned Multifield [-15,+15]", bf_mm_tuned)
report("MegaMapper vs Standard Single-Field", bf_mm_ssfsr)
report("COMBINED (SPHEREx × MegaMapper) vs Tuned Multifield", bf_comb_tuned)
report("COMBINED vs Standard Single-Field", bf_comb_ssfsr)

print(f"\n--- Survey Performance Distribution ---")
print(f"  SPHEREx σ(f_NL):  median={np.median(sigma_sp):.2f}, "
      f"[10th,90th]=[{np.percentile(sigma_sp,10):.2f}, {np.percentile(sigma_sp,90):.2f}]")
print(f"  MegaMapper σ(f_NL): median={np.median(sigma_mm):.2f}, "
      f"[10th,90th]=[{np.percentile(sigma_mm,10):.2f}, {np.percentile(sigma_mm,90):.2f}]")
print(f"  Multi-tracer success: {mt_works.mean()*100:.0f}%")
print(f"  GR shift SPHEREx: mean={gr_sp.mean():.3f}, std={gr_sp.std():.3f}")
print(f"  GR shift MegaMapper: mean={gr_mm.mean():.3f}, std={gr_mm.std():.3f}")

# Prior sensitivity
print(f"\n--- PRIOR SENSITIVITY (SPHEREx vs Tuned, at median realization) ---")
med_idx = np.argsort(bf_sp_tuned)[N_REAL//2]
d_med = fnl_obs_sp[med_idx]
s_med = sigma_sp[med_idx]
for lo, hi in [(-5,5), (-10,10), (-15,15), (-20,20), (-50,50)]:
    bf = bf_delta_vs_flat(np.array([d_med]), np.array([s_med]), FNL_BOUNCE, lo, hi)[0]
    print(f"  Prior [{lo:>4},{hi:>4}]: BF = {bf:.1f}")

print("\n" + "=" * 75)
print("HEADLINE NUMBERS")
print("=" * 75)
print(f"\nIf the bounce is true and SPHEREx + MegaMapper both observe:")
print(f"  P(combined BF > 10 vs tuned multifield):  {np.mean(bf_comb_tuned > 10)*100:.1f}%")
print(f"  P(combined BF > 100 vs tuned multifield): {np.mean(bf_comb_tuned > 100)*100:.1f}%")
print(f"  P(combined BF > 10 vs SSFSR):             {np.mean(bf_comb_ssfsr > 10)*100:.1f}%")
print(f"  Median combined BF vs tuned:              {np.median(bf_comb_tuned):.0f}")
print(f"  Median combined BF vs SSFSR:              {np.median(np.clip(bf_comb_ssfsr,0,1e30)):.0e}")

print("\nDone.")
