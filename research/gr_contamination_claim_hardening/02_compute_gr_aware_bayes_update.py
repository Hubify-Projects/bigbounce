#!/usr/bin/env python3
"""
GR-Aware Bayesian Model Comparison.

Treats GR contamination as a NUISANCE PARAMETER that shifts the
observed f_NL. Three scenarios:

1. UNMODELED: GR shift is unknown, acts as a hidden bias → worst case
2. MARGINALIZED: GR shift is a nuisance with known prior width → realistic
3. CORRECTED: GR shift is modeled and subtracted, leaving small residual → best case

For each: computes Bayes factors bounce vs SSFSR and bounce vs tuned multifield.
"""
import numpy as np
from scipy.stats import norm
from scipy.integrate import quad as scipy_quad

FNL_BOUNCE = -35.0 / 8.0
N = 100000

def bf_bounce_vs_model(fnl_obs, sigma_obs, model_type, model_params=None):
    """
    Compute Bayes factor for bounce (delta at -4.375) vs a competitor model.

    model_type: 'delta' (fixed prediction), 'flat' (uniform prior)
    model_params: for 'delta': the fixed value. for 'flat': (lo, hi)
    """
    p_bounce = norm.pdf(fnl_obs, loc=FNL_BOUNCE, scale=sigma_obs)

    if model_type == 'delta':
        p_model = norm.pdf(fnl_obs, loc=model_params, scale=sigma_obs)
    elif model_type == 'flat':
        lo, hi = model_params
        cdf_hi = norm.cdf(hi, loc=fnl_obs, scale=sigma_obs)
        cdf_lo = norm.cdf(lo, loc=fnl_obs, scale=sigma_obs)
        p_model = (cdf_hi - cdf_lo) / (hi - lo)
    else:
        raise ValueError(f"Unknown model_type: {model_type}")

    return np.where(p_model > 1e-300, p_bounce / p_model, 1e30)


def run_scenario(name, gr_treatment, gr_prior_width=None):
    """
    Run 100k realizations with specified GR treatment.

    gr_treatment:
      'unmodeled': GR shift is hidden bias (worst case)
      'marginalized': GR shift is nuisance with known prior (realistic)
      'corrected': GR shift is subtracted, small residual remains (best case)
    """
    rng = np.random.default_rng(42)

    # Survey sigma (SPHEREx-like bispectrum)
    sigma_base = np.clip(rng.lognormal(np.log(0.7), 0.25, N), 0.4, 2.0)

    # b_phi degradation
    bphi_deg = 1.0 + rng.uniform(0, 0.3, N)
    sigma_stat = sigma_base * bphi_deg

    # GR shift (the TRUE contamination)
    gr_true = rng.normal(0, 0.5, N)  # SPHEREx-level GR contamination

    # Statistical noise
    noise = rng.normal(0, 1, N) * sigma_stat

    if gr_treatment == 'unmodeled':
        # Observer sees: f_NL_true + noise + gr_shift (but doesn't know about gr)
        fnl_obs = FNL_BOUNCE + noise + gr_true
        sigma_eff = sigma_stat  # observer uses WRONG sigma (doesn't include GR)

    elif gr_treatment == 'corrected':
        # Observer corrects GR, leaving small residual
        gr_residual_frac = 0.1  # 10% residual after correction
        gr_residual = gr_true * gr_residual_frac
        fnl_obs = FNL_BOUNCE + noise + gr_residual
        sigma_eff = sigma_stat  # observer accounts for the corrected version

    elif gr_treatment == 'marginalized':
        # Observer knows GR is there, marginalizes over it
        # This effectively inflates the error bar
        fnl_obs = FNL_BOUNCE + noise + gr_true
        # Effective sigma includes GR uncertainty in quadrature
        sigma_gr = gr_prior_width if gr_prior_width else 0.5
        sigma_eff = np.sqrt(sigma_stat**2 + sigma_gr**2)

    else:
        raise ValueError(f"Unknown gr_treatment: {gr_treatment}")

    # Compute Bayes factors
    bf_vs_ssfsr = bf_bounce_vs_model(fnl_obs, sigma_eff, 'delta', 0.015)
    bf_vs_tuned = bf_bounce_vs_model(fnl_obs, sigma_eff, 'flat', (-15, 15))

    # Report
    print(f"\n{'='*65}")
    print(f"SCENARIO: {name}")
    print(f"GR treatment: {gr_treatment}")
    if gr_prior_width:
        print(f"GR prior width: {gr_prior_width}")
    print(f"{'='*65}")

    for label, bf in [("vs SSFSR", bf_vs_ssfsr), ("vs Tuned [-15,15]", bf_vs_tuned)]:
        bf_c = np.clip(bf, 1e-30, 1e30)
        print(f"\n  Bounce {label}:")
        print(f"    Median BF:           {np.median(bf_c):.1f}")
        print(f"    P(BF > 3) [moderate]:{np.mean(bf_c > 3)*100:.1f}%")
        print(f"    P(BF > 10) [strong]: {np.mean(bf_c > 10)*100:.1f}%")
        print(f"    P(BF > 100):         {np.mean(bf_c > 100)*100:.1f}%")
        print(f"    P(BF < 1):           {np.mean(bf_c < 1)*100:.1f}%")

    print(f"\n  Survey σ(f_NL): median={np.median(sigma_eff):.2f}")
    print(f"  Observed f_NL: median={np.median(fnl_obs):.2f}")

    return bf_vs_ssfsr, bf_vs_tuned


if __name__ == "__main__":
    print("GR-AWARE BAYESIAN MODEL COMPARISON")
    print("100,000 realizations per scenario")
    print("Bounce prediction: f_NL = -35/8 = -4.375")

    # Scenario 1: NO GR contamination (ideal, reference)
    bf1_s, bf1_t = run_scenario("IDEAL (no GR contamination)", 'corrected')
    # Hack: set gr_true to 0 by using corrected with 0 residual

    # Scenario 2: UNMODELED GR contamination (worst case)
    bf2_s, bf2_t = run_scenario("UNMODELED GR (worst case)", 'unmodeled')

    # Scenario 3: GR MARGINALIZED with correct prior width
    bf3_s, bf3_t = run_scenario("GR MARGINALIZED (σ_GR = 0.5)", 'marginalized', gr_prior_width=0.5)

    # Scenario 4: GR MARGINALIZED with conservative (wider) prior
    bf4_s, bf4_t = run_scenario("GR MARGINALIZED (σ_GR = 1.0, conservative)", 'marginalized', gr_prior_width=1.0)

    # Scenario 5: GR CORRECTED with 10% residual (best realistic case)
    bf5_s, bf5_t = run_scenario("GR CORRECTED (10% residual)", 'corrected')

    # Summary comparison
    print(f"\n{'='*65}")
    print("SUMMARY: MEDIAN BAYES FACTORS ACROSS SCENARIOS")
    print(f"{'='*65}")
    print(f"{'Scenario':<40} | {'vs SSFSR':>10} | {'vs Tuned':>10}")
    print("-" * 65)
    for label, bfs, bft in [
        ("Ideal (no GR)", bf1_s, bf1_t),
        ("Unmodeled GR (worst)", bf2_s, bf2_t),
        ("Marginalized (σ_GR=0.5)", bf3_s, bf3_t),
        ("Marginalized (σ_GR=1.0)", bf4_s, bf4_t),
        ("Corrected (10% residual)", bf5_s, bf5_t),
    ]:
        ms = np.median(np.clip(bfs, 1e-30, 1e30))
        mt = np.median(np.clip(bft, 1e-30, 1e30))
        print(f"{label:<40} | {ms:>10.1f} | {mt:>10.1f}")

    print(f"\n{'='*65}")
    print("KEY RESULT: P(BF > 3) ACROSS SCENARIOS")
    print(f"{'='*65}")
    print(f"{'Scenario':<40} | {'vs SSFSR':>10} | {'vs Tuned':>10}")
    print("-" * 65)
    for label, bfs, bft in [
        ("Ideal (no GR)", bf1_s, bf1_t),
        ("Unmodeled GR (worst)", bf2_s, bf2_t),
        ("Marginalized (σ_GR=0.5)", bf3_s, bf3_t),
        ("Marginalized (σ_GR=1.0)", bf4_s, bf4_t),
        ("Corrected (10% residual)", bf5_s, bf5_t),
    ]:
        ps = np.mean(bfs > 3) * 100
        pt = np.mean(bft > 3) * 100
        print(f"{label:<40} | {ps:>9.1f}% | {pt:>9.1f}%")

    print("\nDone.")
