#!/usr/bin/env python3
"""
Bayesian model comparison: bounce benchmark vs inflation competitors.

For each mock survey outcome (measured f_NL ± σ), computes the Bayes factor
between the bounce (delta-function prediction at -35/8) and each inflation
competitor class (parameterized prediction with prior over free parameters).

The Bayes factor naturally encodes the Occam penalty: models with wider
prior ranges pay a larger penalty for accommodating any specific value.
"""
import numpy as np
from scipy.integrate import quad
from scipy.stats import norm

# ============================================================
# BOUNCE BENCHMARK: delta function at f_NL = -35/8
# ============================================================
FNL_BOUNCE = -35.0 / 8.0  # = -4.375

def likelihood_bounce(fnl_measured, sigma):
    """P(data | bounce) = Gaussian likelihood at the fixed prediction."""
    return norm.pdf(fnl_measured, loc=FNL_BOUNCE, scale=sigma)


# ============================================================
# INFLATION COMPETITOR CLASSES
# ============================================================

def likelihood_ssfsr(fnl_measured, sigma):
    """Standard single-field slow-roll: delta at f_NL = +0.015."""
    return norm.pdf(fnl_measured, loc=0.015, scale=sigma)


def evidence_nonattractor(fnl_measured, sigma, prior_range=(-10, 10)):
    """Non-attractor single-field: f_NL is a free parameter in prior_range.
    Natural value is +5/2 but transition-dependent, so we use a broad flat prior."""
    lo, hi = prior_range
    def integrand(fnl_true):
        return norm.pdf(fnl_measured, loc=fnl_true, scale=sigma) * 1.0/(hi - lo)
    result, _ = quad(integrand, lo, hi, limit=200)
    return result


def evidence_curvaton(fnl_measured, sigma):
    """Standard quadratic curvaton: f_NL = 5/(4r) - 5r/6 - 5/3 for r in (0,1].
    Prior: flat in r_dec from 0.01 to 1.0."""
    r_lo, r_hi = 0.01, 1.0
    def fnl_curvaton(r):
        return 5.0/(4*r) - 5*r/6.0 - 5.0/3.0
    def integrand(r):
        fnl_true = fnl_curvaton(r)
        return norm.pdf(fnl_measured, loc=fnl_true, scale=sigma) * 1.0/(r_hi - r_lo)
    result, _ = quad(integrand, r_lo, r_hi, limit=200)
    return result


def evidence_tuned_multifield(fnl_measured, sigma, prior_range=(-15, 15)):
    """Self-interacting curvaton / tuned multifield: f_NL anywhere in prior_range.
    This represents the 'inflation can tune anything' class."""
    lo, hi = prior_range
    def integrand(fnl_true):
        return norm.pdf(fnl_measured, loc=fnl_true, scale=sigma) * 1.0/(hi - lo)
    result, _ = quad(integrand, lo, hi, limit=200)
    return result


def evidence_rapid_turn(fnl_measured, sigma, prior_range=(-15, 15)):
    """Rapid-turn multifield: even broader prior (3 params compressed to f_NL range)."""
    # Same structure as tuned multifield but potentially broader range
    lo, hi = prior_range
    def integrand(fnl_true):
        return norm.pdf(fnl_measured, loc=fnl_true, scale=sigma) * 1.0/(hi - lo)
    result, _ = quad(integrand, lo, hi, limit=200)
    return result


# ============================================================
# BAYES FACTOR COMPUTATION
# ============================================================

def compute_all_bayes_factors(fnl_measured, sigma, prior_tuned=(-15,15), prior_nonattr=(-10,10)):
    """Compute Bayes factors B = P(data|bounce) / P(data|competitor) for all competitors."""
    p_bounce = likelihood_bounce(fnl_measured, sigma)

    results = {}

    # vs standard single-field
    p_ssfsr = likelihood_ssfsr(fnl_measured, sigma)
    results['vs_SSFSR'] = p_bounce / p_ssfsr if p_ssfsr > 0 else np.inf

    # vs non-attractor
    p_nonattr = evidence_nonattractor(fnl_measured, sigma, prior_nonattr)
    results['vs_NonAttractor'] = p_bounce / p_nonattr if p_nonattr > 0 else np.inf

    # vs standard curvaton
    p_curv = evidence_curvaton(fnl_measured, sigma)
    results['vs_Curvaton'] = p_bounce / p_curv if p_curv > 0 else np.inf

    # vs tuned multifield
    p_tuned = evidence_tuned_multifield(fnl_measured, sigma, prior_tuned)
    results['vs_TunedMulti'] = p_bounce / p_tuned if p_tuned > 0 else np.inf

    # vs rapid-turn (broader prior)
    p_rapid = evidence_rapid_turn(fnl_measured, sigma, prior_tuned)
    results['vs_RapidTurn'] = p_bounce / p_rapid if p_rapid > 0 else np.inf

    return results


def interpret_bf(bf):
    """Interpret Bayes factor."""
    if bf > 100: return "DECISIVE_BOUNCE"
    if bf > 30: return "VERY_STRONG_BOUNCE"
    if bf > 10: return "STRONG_BOUNCE"
    if bf > 3: return "MODERATE_BOUNCE"
    if bf > 1/3: return "INCONCLUSIVE"
    if bf > 1/10: return "MODERATE_INFLATION"
    return "STRONG_INFLATION"


# ============================================================
# MAIN: MOCK OUTCOME GRID
# ============================================================

if __name__ == "__main__":
    print("=" * 80)
    print("BAYESIAN MODEL COMPARISON: BOUNCE vs INFLATION COMPETITORS")
    print("=" * 80)

    # Mock survey configurations
    surveys = [
        ("SPHEREx (bispectrum)", 0.7),
        ("SPHEREx (combined)", 0.5),
        ("MegaMapper (realistic)", 1.0),
        ("MegaMapper (design)", 0.5),
    ]

    # Mock measured values
    mock_fnls = [0.0, -1.0, -2.0, -3.0, -4.375, -6.0]

    for survey_name, sigma in surveys:
        print(f"\n{'='*80}")
        print(f"SURVEY: {survey_name} (σ = {sigma})")
        print(f"{'='*80}")
        print(f"{'fnl_meas':>10} | {'vs_SSFSR':>14} | {'vs_NonAttr':>14} | {'vs_Curvaton':>14} | {'vs_TunedMF':>14} | {'Verdict':>20}")
        print("-" * 100)

        for fnl_m in mock_fnls:
            bfs = compute_all_bayes_factors(fnl_m, sigma)
            # Main verdict: vs the strongest competitor (tuned multifield)
            bf_main = bfs['vs_TunedMulti']
            verdict = interpret_bf(bf_main)

            print(f"{fnl_m:>10.3f} | "
                  f"{bfs['vs_SSFSR']:>14.1f} | "
                  f"{bfs['vs_NonAttractor']:>14.1f} | "
                  f"{bfs['vs_Curvaton']:>14.1f} | "
                  f"{bfs['vs_TunedMulti']:>14.1f} | "
                  f"{verdict:>20}")

    # Prior sensitivity
    print(f"\n{'='*80}")
    print("PRIOR SENSITIVITY (for f_NL_measured = -4.375, σ = 0.7)")
    print(f"{'='*80}")
    print(f"{'Prior range':>20} | {'vs_TunedMF BF':>15} | {'Verdict':>20}")
    print("-" * 60)

    for lo, hi in [(-5, 5), (-10, 10), (-15, 15), (-20, 20), (-50, 50)]:
        bfs = compute_all_bayes_factors(-4.375, 0.7, prior_tuned=(lo, hi))
        bf = bfs['vs_TunedMulti']
        print(f"[{lo:>4}, {hi:>4}]          | {bf:>15.1f} | {interpret_bf(bf):>20}")

    # Summary for the key detection scenario
    print(f"\n{'='*80}")
    print("KEY SCENARIO: SPHEREx detects f_NL = -4.375 ± 0.7")
    print(f"{'='*80}")
    bfs = compute_all_bayes_factors(-4.375, 0.7)
    for comp, bf in bfs.items():
        print(f"  Bounce vs {comp:20s}: Bayes factor = {bf:>10.1f}  [{interpret_bf(bf)}]")

    print(f"\n{'='*80}")
    print("KEY SCENARIO: MegaMapper detects f_NL = -4.375 ± 0.5")
    print(f"{'='*80}")
    bfs = compute_all_bayes_factors(-4.375, 0.5)
    for comp, bf in bfs.items():
        print(f"  Bounce vs {comp:20s}: Bayes factor = {bf:>10.1f}  [{interpret_bf(bf)}]")

    print("\nDone.")
