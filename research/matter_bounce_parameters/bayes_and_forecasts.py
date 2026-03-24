#!/usr/bin/env python3
"""
Matter-Bounce vs Inflation: Bayes Factor & Forecast Analysis

Extends compute_all.py with:
1. Bayes factor B(bounce/inflation) as function of measured f_NL
2. Full experiment forecast table with bounce-template corrections
3. Sensitivity to the -35/8 vs -35/16 ambiguity
4. The 3-column discrimination table (observable / mission / theory)
"""

import numpy as np

# From compute_all.py results
R_CMB = 0.876     # CMB projection factor
R_LSS = 0.829     # LSS projection factor
FNL_BOUNCE = -4.349  # epsilon-corrected prediction
FNL_BOUNCE_ALT = -35/16  # = -2.1875, Li-Brandenberger alternative
SIGMA_BOUNCE_RANGE = 0.013  # epsilon uncertainty band


# ═══════════════════════════════════════════════════════════════
# 1. BAYES FACTOR: bounce vs inflation
# ═══════════════════════════════════════════════════════════════

def bayes_factor_analysis():
    """
    Compute the Bayes factor between bounce and inflation as a
    function of measured f_NL^local.

    Models:
    - Bounce: f_NL = f_NL_bounce (delta function prior, parameter-free)
    - Inflation (vanilla single-field): f_NL = 0 (delta function)
    - Inflation (multifield): f_NL ~ Uniform(-10, +10) (broad prior)

    For a measurement f_NL^obs ± sigma:
      B(bounce/vanilla) = L(obs|bounce) / L(obs|vanilla)
        = exp(-0.5*((obs-f_bounce)/sigma)^2) / exp(-0.5*(obs/sigma)^2)
        = exp(-(f_bounce^2 - 2*obs*f_bounce)/(2*sigma^2))

    For multifield inflation with uniform prior [-a, +a]:
      L(obs|multi) = (1/2a) * integral_{-a}^{a} exp(-0.5*(obs-f)^2/sigma^2) df
                   = (1/2a) * sqrt(2*pi) * sigma * [Phi((a-obs)/sigma) - Phi((-a-obs)/sigma)]
    """
    print("=" * 70)
    print("1. BAYES FACTOR: BOUNCE vs INFLATION")
    print("=" * 70)

    from scipy.stats import norm

    f_bounce_cmb = FNL_BOUNCE * R_CMB   # what CMB estimator would see
    f_bounce_lss = FNL_BOUNCE * R_LSS   # what LSS estimator would see

    # Multifield inflation prior range
    a_multi = 10.0  # uniform on [-10, +10]

    def log_bf_vs_vanilla(f_obs, sigma, f_pred):
        """Log Bayes factor: bounce vs vanilla (f_NL=0)."""
        return -(f_pred**2 - 2*f_obs*f_pred) / (2*sigma**2)

    def log_bf_vs_multifield(f_obs, sigma, f_pred, a=10.0):
        """Log Bayes factor: bounce vs multifield uniform prior."""
        # L(obs|bounce)
        log_L_bounce = -0.5 * ((f_obs - f_pred)/sigma)**2
        # L(obs|multi) = (1/2a) * sqrt(2pi) * sigma * [Phi(...) - Phi(...)]
        phi_hi = norm.cdf((a - f_obs) / sigma)
        phi_lo = norm.cdf((-a - f_obs) / sigma)
        log_L_multi = np.log(1/(2*a)) + 0.5*np.log(2*np.pi) + np.log(sigma) + np.log(phi_hi - phi_lo)
        return log_L_bounce - log_L_multi

    # Scenario table: what if the true f_NL IS the bounce value?
    print(f"\n  If bounce is true (f_NL^true = {FNL_BOUNCE:.3f}):")
    print(f"  CMB estimator sees: {f_bounce_cmb:.3f}")
    print(f"  LSS estimator sees: {f_bounce_lss:.3f}")

    print(f"\n  {'Experiment':<25s} {'σ_local':>7s} {'f_obs':>7s} "
          f"{'B vs 0':>8s} {'B vs multi':>10s} {'Jeffreys':>12s}")
    print("  " + "-" * 73)

    experiments = [
        ("Planck 2018",       5.1,  "CMB"),
        ("Planck+DESI (now)", 4.1,  "mixed"),
        ("AI tracers",        2.5,  "LSS"),
        ("Simons Obs.",       2.0,  "CMB"),
        ("SPHEREx bispec",    0.7,  "mixed"),
        ("CMB-S4",            0.5,  "CMB"),
        ("MegaMapper SDB",    0.5,  "LSS"),
        ("MegaMapper+CMB-S4", 0.35, "mixed"),
    ]

    for name, sigma, etype in experiments:
        if etype == "CMB":
            f_obs = f_bounce_cmb
        elif etype == "LSS":
            f_obs = f_bounce_lss
        else:
            f_obs = FNL_BOUNCE * (R_CMB + R_LSS) / 2

        lbf_v = log_bf_vs_vanilla(f_obs, sigma, f_obs)  # obs = pred if bounce is true
        lbf_m = log_bf_vs_multifield(f_obs, sigma, f_obs)
        bf_v = np.exp(lbf_v)
        bf_m = np.exp(lbf_m)

        # Jeffreys scale
        if bf_v > 100:
            strength = "DECISIVE"
        elif bf_v > 30:
            strength = "Very strong"
        elif bf_v > 10:
            strength = "Strong"
        elif bf_v > 3:
            strength = "Substantial"
        else:
            strength = "Weak"

        if bf_v > 1e6:
            bf_v_str = f"{bf_v:.0e}"
        elif bf_v > 100:
            bf_v_str = f"{bf_v:.0f}"
        else:
            bf_v_str = f"{bf_v:.1f}"

        if bf_m > 1e6:
            bf_m_str = f"{bf_m:.0e}"
        elif bf_m > 100:
            bf_m_str = f"{bf_m:.0f}"
        else:
            bf_m_str = f"{bf_m:.1f}"

        print(f"  {name:<25s} {sigma:>7.2f} {f_obs:>+7.2f} "
              f"{bf_v_str:>8s} {bf_m_str:>10s} {strength:>12s}")

    # What if measured f_NL = 0 (no signal)?
    print(f"\n  If f_NL^true = 0 (bounce is wrong):")
    print(f"  {'Experiment':<25s} {'σ_local':>7s} "
          f"{'B(0/bounce)':>12s} {'Bounce ruled out?':>20s}")
    print("  " + "-" * 68)

    for name, sigma, etype in experiments:
        if etype == "CMB":
            f_pred = f_bounce_cmb
        elif etype == "LSS":
            f_pred = f_bounce_lss
        else:
            f_pred = FNL_BOUNCE * (R_CMB + R_LSS) / 2

        # If obs = 0, Bayes factor for vanilla over bounce
        lbf = -log_bf_vs_vanilla(0, sigma, f_pred)
        bf = np.exp(lbf)
        nsigma = abs(f_pred) / sigma

        if bf > 100:
            verdict = f"YES ({nsigma:.1f}σ)"
        elif bf > 10:
            verdict = f"Likely ({nsigma:.1f}σ)"
        elif bf > 3:
            verdict = f"Suggestive ({nsigma:.1f}σ)"
        else:
            verdict = f"No ({nsigma:.1f}σ)"

        if bf > 1e6:
            bf_str = f"{bf:.0e}"
        elif bf > 100:
            bf_str = f"{bf:.0f}"
        else:
            bf_str = f"{bf:.1f}"

        print(f"  {name:<25s} {sigma:>7.2f} {bf_str:>12s} {verdict:>20s}")


# ═══════════════════════════════════════════════════════════════
# 2. SENSITIVITY TO -35/8 vs -35/16 AMBIGUITY
# ═══════════════════════════════════════════════════════════════

def convention_sensitivity():
    """
    What changes if the true value is -35/16 instead of -35/8?
    This is the unresolved factor-of-2 from the Li-Brandenberger
    normalization convention.
    """
    print("\n" + "=" * 70)
    print("2. SENSITIVITY TO -35/8 vs -35/16 AMBIGUITY")
    print("=" * 70)

    f1 = -35/8    # Cai et al. value (70% confident)
    f2 = -35/16   # Li-Brandenberger value

    r = (R_CMB + R_LSS) / 2  # average projection

    print(f"\n  {'':30s} {'f_NL = -35/8':>14s} {'f_NL = -35/16':>14s}")
    print("  " + "-" * 62)
    print(f"  {'Squeezed-limit f_NL':<30s} {f1:>+14.3f} {f2:>+14.3f}")
    print(f"  {'After projection (CMB, r={R_CMB:.3f})':<30s} {f1*R_CMB:>+14.3f} {f2*R_CMB:>+14.3f}")
    print(f"  {'After projection (LSS, r={R_LSS:.3f})':<30s} {f1*R_LSS:>+14.3f} {f2*R_LSS:>+14.3f}")

    print(f"\n  Detection significance (if bounce true):")
    print(f"  {'Experiment':<25s} {'σ_local':>7s} {'Signif (-35/8)':>15s} {'Signif (-35/16)':>16s}")
    print("  " + "-" * 67)

    for name, sigma in [
        ("Planck+DESI (now)", 4.1),
        ("AI tracers",        2.5),
        ("SPHEREx",           0.7),
        ("MegaMapper",        0.5),
        ("MegaMapper+CMB-S4", 0.35),
    ]:
        sig1 = abs(f1 * r) / sigma
        sig2 = abs(f2 * r) / sigma
        print(f"  {name:<25s} {sigma:>7.2f} {sig1:>14.1f}σ {sig2:>15.1f}σ")

    print(f"\n  ╔══════════════════════════════════════════════════════════════╗")
    print(f"  ║  KEY: The -35/8 vs -35/16 ambiguity is a FACTOR OF 2 in    ║")
    print(f"  ║  significance. At -35/16, SPHEREx gives 2.7σ (evidence)    ║")
    print(f"  ║  instead of 5.3σ (discovery). Resolving this convention     ║")
    print(f"  ║  is URGENT before SPHEREx data arrives.                     ║")
    print(f"  ╚══════════════════════════════════════════════════════════════╝")


# ═══════════════════════════════════════════════════════════════
# 3. MASTER DISCRIMINATION TABLE
# ═══════════════════════════════════════════════════════════════

def discrimination_table():
    """
    The 3-column table: observable / what missions measure / what bounce predicts.
    This is the core intellectual product of the parameter connection work.
    """
    print("\n" + "=" * 70)
    print("3. MASTER DISCRIMINATION TABLE")
    print("=" * 70)

    print("""
  ┌─────────────────────┬──────────────────────────┬────────────────────────────┐
  │     Observable       │   What experiments do     │   What bounce predicts     │
  ├─────────────────────┼──────────────────────────┼────────────────────────────┤
  │                      │                          │                            │
  │ Local f_NL           │ Planck: -0.9 ± 5.1      │ -4.375  (exact dust)       │
  │ (bispectrum)         │ DESI SDB: ~-2 ± 7       │ -4.349  (quasi-dust)       │
  │                      │ SPHEREx: σ ~ 0.7         │ Parameter-free.            │
  │                      │ MegaMapper: σ ~ 0.5      │ Negative, large, unique.   │
  │                      │                          │ Projection r = 0.83-0.88   │
  │                      │                          │                            │
  ├─────────────────────┼──────────────────────────┼────────────────────────────┤
  │                      │                          │                            │
  │ Cosmic birefringence │ Planck+ACT: 0.34±0.09°  │ β = 0.27°  (natural ALP)   │
  │ (EB cross-power)     │ LiteBIRD: σ ~ 0.04°     │ Bounce-INDEPENDENT.        │
  │                      │                          │ Supporting, not decisive.  │
  │                      │                          │                            │
  ├─────────────────────┼──────────────────────────┼────────────────────────────┤
  │                      │                          │                            │
  │ Spectral tilt n_s    │ Planck: 0.9649 ± 0.0042 │ n_s = 1 - 12ε              │
  │                      │                          │ ε ≈ 0.003 (fitted)         │
  │                      │                          │ SAME ε connects to f_NL    │
  │                      │                          │                            │
  ├─────────────────────┼──────────────────────────┼────────────────────────────┤
  │                      │                          │                            │
  │ Tensor-to-scalar r   │ BICEP/Keck: r < 0.036   │ r ~ 10⁻⁴  (LQC)           │
  │                      │ LiteBIRD: σ ~ 0.001     │ Untestable. Silent sector. │
  │                      │                          │                            │
  ├─────────────────────┼──────────────────────────┼────────────────────────────┤
  │                      │                          │                            │
  │ Running α_s          │ Planck: -0.006 ± 0.013  │ α_s = -144ε² ~ -10⁻³      │
  │                      │                          │ Unmeasurably small.        │
  │                      │                          │                            │
  ├─────────────────────┼──────────────────────────┼────────────────────────────┤
  │                      │                          │                            │
  │ Isocurvature modes   │ Planck: < 3.7% (95%)    │ Zero. Single-field.        │
  │                      │                          │ Consistency check.         │
  │                      │                          │                            │
  ├─────────────────────┼──────────────────────────┼────────────────────────────┤
  │                      │                          │                            │
  │ ΔN_eff              │ Planck+BAO: 0.0 ± 0.2   │ ΔN_eff = 0                 │
  │ (extra radiation)    │ MCMC: 309K samples       │ No bounce relic.           │
  │                      │                          │ Perturbation transparency. │
  │                      │                          │                            │
  └─────────────────────┴──────────────────────────┴────────────────────────────┘

  DISCRIMINATOR RANKING:

  1. f_NL = -4.35          DECISIVE    SPHEREx 5σ, MegaMapper 7σ
                                       Opposite sign from most inflation models
                                       Only observable with paradigm-level power

  2. Birefringence β=0.27° SUPPORTING  Already 3.6σ, LiteBIRD 9σ
                                       But bounce-independent — doesn't SELECT bounce

  3. n_s = 0.964           FITTED      Determines ε, no discrimination power alone

  4. Everything else       SILENT      r, α_s, ΔN_eff all unmeasurable or null
""")


# ═══════════════════════════════════════════════════════════════
# 4. WHAT THE PAPER SHOULD SAY
# ═══════════════════════════════════════════════════════════════

def paper_implications():
    """Concrete numbers for the paper."""
    print("=" * 70)
    print("4. NUMBERS FOR THE PAPER")
    print("=" * 70)

    r_avg = (R_CMB + R_LSS) / 2

    print(f"""
  NEW RESULTS from this analysis:

  A. Template projection factor: r_CMB = {R_CMB:.3f}, r_LSS = {R_LSS:.3f}
     → The matter-bounce bispectrum has ~{(1-r_avg)*100:.0f}% non-local contamination
     → All published σ(f_NL) must be divided by r when applied to bounce
     → This has NOT been quantified in the literature before

  B. Effective f_NL for estimators:
     → CMB local estimator sees f_NL^eff = {FNL_BOUNCE * R_CMB:.2f} (not {FNL_BOUNCE:.2f})
     → LSS SDB estimator sees f_NL^eff = {FNL_BOUNCE * R_LSS:.2f} (not {FNL_BOUNCE:.2f})

  C. Corrected significance forecasts:
     → SPHEREx: {abs(FNL_BOUNCE*r_avg)/0.7:.1f}σ (was {abs(FNL_BOUNCE)/0.7:.1f}σ naive)
     → MegaMapper: {abs(FNL_BOUNCE*r_avg)/0.5:.1f}σ (was {abs(FNL_BOUNCE)/0.5:.1f}σ naive)
     → Still discovery-grade. The projection penalty is moderate.

  D. Consistency relation (new, testable):
     f_NL(n_s) = -4.375 - 0.729 × (n_s - 1)
     → Single-parameter curve connecting spectral tilt to non-Gaussianity
     → No equivalent in standard inflation (multifield f_NL is unconstrained)
     → Measures both n_s and f_NL, checks if on curve

  E. Convention urgency:
     → If true value is -35/16, SPHEREx drops from {abs(-35/8*r_avg)/0.7:.1f}σ to {abs(-35/16*r_avg)/0.7:.1f}σ
     → Resolving the Cai vs Li-Brandenberger factor of 2 is critical
     → Requires: careful comparison of their f_NL definitions

  F. Current data status:
     → Combined Planck+DESI on bounce template: f_NL = -1.3 ± 4.5
     → 0.7σ from bounce prediction, 0.3σ from zero
     → Consistent with both. No discrimination yet.
""")

    # The key equation to add to Paper 2/3
    print(f"  KEY EQUATION FOR THE PAPER:")
    print(f"")
    print(f"    f_NL^{{measured}} = r × f_NL^{{bounce}}")
    print(f"    where r = {R_CMB:.3f} (CMB) or {R_LSS:.3f} (LSS)")
    print(f"")
    print(f"    σ(f_NL^{{bounce}}) = σ(f_NL^{{local}}) / r")
    print(f"")
    print(f"    This comes from the shape mismatch:")
    print(f"    B_NL^{{bounce}} varies from -4.375 (squeezed) to -2.25 (folded)")
    print(f"    while B_NL^{{local}} = const for all configurations.")
    print(f"    The weighted average <B_NL^bounce> / B_NL^squeeze = r.")


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║  BAYES FACTORS, FORECASTS, AND DISCRIMINATION ANALYSIS     ║")
    print("╚══════════════════════════════════════════════════════════════╝\n")

    bayes_factor_analysis()
    convention_sensitivity()
    discrimination_table()
    paper_implications()
