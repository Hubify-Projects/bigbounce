#!/usr/bin/env python3
"""
Last-Mile Robustness: Monte Carlo ensemble of Bayes factors
over realistic survey-assumption uncertainty.

Samples over:
  - mock measured f_NL (what nature gives us, drawn from bounce prediction + noise)
  - σ(f_NL) uncertainty (survey performance varies)
  - b_φ nuisance (degrades effective σ)
  - GR systematic residual (shifts the measured value)
  - multi-tracer success (discrete: works or doesn't)

For each realization: computes Bayes factor bounce vs tuned-multifield.
Output: distribution of Bayes factors showing how robust the advantage is.
"""
import numpy as np
from scipy.stats import norm
from scipy.integrate import quad

FNL_BOUNCE = -35.0 / 8.0  # = -4.375

def bayes_factor_bounce_vs_tuned(fnl_measured, sigma, prior_lo=-15, prior_hi=15):
    """Bayes factor: bounce (delta at -35/8) vs tuned multifield (flat prior)."""
    p_bounce = norm.pdf(fnl_measured, loc=FNL_BOUNCE, scale=sigma)
    # Tuned multifield: flat prior over [prior_lo, prior_hi]
    def integrand(fnl_true):
        return norm.pdf(fnl_measured, loc=fnl_true, scale=sigma) / (prior_hi - prior_lo)
    p_tuned, _ = quad(integrand, prior_lo, prior_hi, limit=200)
    return p_bounce / p_tuned if p_tuned > 0 else np.inf

def bayes_factor_bounce_vs_ssfsr(fnl_measured, sigma):
    """Bayes factor: bounce vs standard single-field (delta at +0.015)."""
    p_bounce = norm.pdf(fnl_measured, loc=FNL_BOUNCE, scale=sigma)
    p_ssfsr = norm.pdf(fnl_measured, loc=0.015, scale=sigma)
    return p_bounce / p_ssfsr if p_ssfsr > 0 else np.inf


def run_ensemble(n_realizations=100000, seed=42):
    """Run the full Monte Carlo ensemble."""
    rng = np.random.default_rng(seed)

    # ================================================================
    # SURVEY ASSUMPTION DISTRIBUTIONS
    # ================================================================

    # 1. Base σ(f_NL) for SPHEREx: log-normal around 0.7, range ~0.4-2.0
    sigma_spherex_base = rng.lognormal(np.log(0.7), 0.3, n_realizations)
    sigma_spherex_base = np.clip(sigma_spherex_base, 0.3, 3.0)

    # 2. Base σ(f_NL) for MegaMapper: log-normal around 0.5, range ~0.3-3.0
    sigma_mm_base = rng.lognormal(np.log(0.5), 0.4, n_realizations)
    sigma_mm_base = np.clip(sigma_mm_base, 0.2, 5.0)

    # 3. Multi-tracer success (MegaMapper): 70% chance works, 30% chance fails
    multi_tracer_works = rng.random(n_realizations) < 0.7
    # If fails: σ degrades by factor 3
    sigma_mm_effective = np.where(multi_tracer_works, sigma_mm_base, sigma_mm_base * 3)

    # 4. b_φ nuisance: degrades σ by factor (1 + δb_φ) where δb_φ ~ U(0, 0.5)
    bphi_degradation = 1.0 + rng.uniform(0, 0.5, n_realizations)
    sigma_spherex = sigma_spherex_base * bphi_degradation
    sigma_mm = sigma_mm_effective * bphi_degradation

    # 5. GR systematic residual: shifts measured f_NL by δf ~ N(0, 0.5) for SPHEREx
    #    and δf ~ N(0, 1.0) for MegaMapper (higher z = larger GR effect)
    gr_shift_spherex = rng.normal(0, 0.3, n_realizations)
    gr_shift_mm = rng.normal(0, 0.7, n_realizations)

    # 6. True f_NL: assume bounce is correct → f_NL_true = -4.375
    fnl_true = FNL_BOUNCE

    # 7. Mock measured values: f_NL_obs = f_NL_true + noise + GR shift
    noise_spherex = rng.normal(0, 1, n_realizations) * sigma_spherex
    noise_mm = rng.normal(0, 1, n_realizations) * sigma_mm

    fnl_obs_spherex = fnl_true + noise_spherex + gr_shift_spherex
    fnl_obs_mm = fnl_true + noise_mm + gr_shift_mm

    # ================================================================
    # COMPUTE BAYES FACTORS
    # ================================================================

    bf_spherex_vs_tuned = np.zeros(n_realizations)
    bf_spherex_vs_ssfsr = np.zeros(n_realizations)
    bf_mm_vs_tuned = np.zeros(n_realizations)
    bf_mm_vs_ssfsr = np.zeros(n_realizations)
    bf_combined_vs_tuned = np.zeros(n_realizations)

    for i in range(n_realizations):
        bf_spherex_vs_tuned[i] = bayes_factor_bounce_vs_tuned(
            fnl_obs_spherex[i], sigma_spherex[i])
        bf_spherex_vs_ssfsr[i] = bayes_factor_bounce_vs_ssfsr(
            fnl_obs_spherex[i], sigma_spherex[i])
        bf_mm_vs_tuned[i] = bayes_factor_bounce_vs_tuned(
            fnl_obs_mm[i], sigma_mm[i])
        bf_mm_vs_ssfsr[i] = bayes_factor_bounce_vs_ssfsr(
            fnl_obs_mm[i], sigma_mm[i])
        # Combined: multiply independent Bayes factors
        bf_combined_vs_tuned[i] = bf_spherex_vs_tuned[i] * bf_mm_vs_tuned[i]

    return {
        'bf_spherex_vs_tuned': bf_spherex_vs_tuned,
        'bf_spherex_vs_ssfsr': bf_spherex_vs_ssfsr,
        'bf_mm_vs_tuned': bf_mm_vs_tuned,
        'bf_mm_vs_ssfsr': bf_mm_vs_ssfsr,
        'bf_combined_vs_tuned': bf_combined_vs_tuned,
        'sigma_spherex': sigma_spherex,
        'sigma_mm': sigma_mm,
        'fnl_obs_spherex': fnl_obs_spherex,
        'fnl_obs_mm': fnl_obs_mm,
        'multi_tracer_works': multi_tracer_works,
    }


def report_results(results):
    """Print summary statistics."""
    print("=" * 75)
    print("LAST-MILE ROBUSTNESS: BAYES FACTOR ENSEMBLE (100,000 realizations)")
    print("Assumes bounce is true: f_NL = -35/8 = -4.375")
    print("=" * 75)

    for name, key in [
        ("SPHEREx vs Tuned Multifield", 'bf_spherex_vs_tuned'),
        ("SPHEREx vs Standard Inflation", 'bf_spherex_vs_ssfsr'),
        ("MegaMapper vs Tuned Multifield", 'bf_mm_vs_tuned'),
        ("MegaMapper vs Standard Inflation", 'bf_mm_vs_ssfsr'),
        ("COMBINED vs Tuned Multifield", 'bf_combined_vs_tuned'),
    ]:
        bf = results[key]
        log_bf = np.log10(np.clip(bf, 1e-10, 1e30))

        print(f"\n--- {name} ---")
        print(f"  Median Bayes factor:    {np.median(bf):.1f}")
        print(f"  Mean log10(BF):         {np.mean(log_bf):.2f}")
        print(f"  10th percentile BF:     {np.percentile(bf, 10):.1f}")
        print(f"  90th percentile BF:     {np.percentile(bf, 90):.1f}")
        print(f"  P(BF > 3)  [moderate]:  {np.mean(bf > 3)*100:.1f}%")
        print(f"  P(BF > 10) [strong]:    {np.mean(bf > 10)*100:.1f}%")
        print(f"  P(BF > 30) [v.strong]:  {np.mean(bf > 30)*100:.1f}%")
        print(f"  P(BF > 100)[decisive]:  {np.mean(bf > 100)*100:.1f}%")
        print(f"  P(BF < 1)  [infl wins]: {np.mean(bf < 1)*100:.1f}%")

    # Survey performance stats
    print(f"\n--- Survey Performance Distribution ---")
    print(f"  SPHEREx σ(f_NL): median={np.median(results['sigma_spherex']):.2f}, "
          f"10th={np.percentile(results['sigma_spherex'],10):.2f}, "
          f"90th={np.percentile(results['sigma_spherex'],90):.2f}")
    print(f"  MegaMapper σ(f_NL): median={np.median(results['sigma_mm']):.2f}, "
          f"10th={np.percentile(results['sigma_mm'],10):.2f}, "
          f"90th={np.percentile(results['sigma_mm'],90):.2f}")
    print(f"  Multi-tracer success rate: {np.mean(results['multi_tracer_works'])*100:.0f}%")

    # What fraction of the time does the COMBINED analysis favor bounce?
    bf_comb = results['bf_combined_vs_tuned']
    print(f"\n--- COMBINED SPHEREx + MegaMapper ---")
    print(f"  P(combined BF > 10):    {np.mean(bf_comb > 10)*100:.1f}%")
    print(f"  P(combined BF > 100):   {np.mean(bf_comb > 100)*100:.1f}%")
    print(f"  P(combined BF > 1000):  {np.mean(bf_comb > 1000)*100:.1f}%")
    print(f"  Median combined BF:     {np.median(bf_comb):.0f}")


if __name__ == "__main__":
    print("Running 100,000 Monte Carlo realizations...")
    results = run_ensemble(n_realizations=100000)
    report_results(results)
    print("\nDone.")
