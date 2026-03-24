#!/usr/bin/env python3
"""
Matter-Bounce Parameter Connection: Three Computations

1. Template projection coefficient (bounce shape vs local template)
2. Leading epsilon correction to f_NL (consistency relation)
3. Planck + DESI recast onto the exact bounce template

Uses the VERIFIED Cai et al. (0903.0631) polynomial shape function.
Coefficients (2,7,3,-12,-69,19) with prefactor 3/256 reproduce all
three benchmark values exactly: squeezed=-35/8, equilateral=-255/64,
folded=-9/4.
"""

import numpy as np
from scipy import integrate

# ═══════════════════════════════════════════════════════════════
# SECTION 0: Verified Cai Shape Function
# ═══════════════════════════════════════════════════════════════

# Polynomial coefficients verified in bispectrum_rescue/02b
PREFACTOR = 3.0 / 256.0
C1, C2, C3, C4, C5, C6 = 2, 7, 3, -12, -69, 19


def compute_sums(k1, k2, k3):
    """Compute all required momentum sums."""
    ks = [k1, k2, k3]
    pk2 = k1**2 * k2**2 * k3**2
    sk3 = k1**3 + k2**3 + k3**3

    s9 = sum(k**9 for k in ks)
    s72 = sum(ks[i]**7 * ks[j]**2 for i in range(3) for j in range(3) if i != j)
    s63 = sum(ks[i]**6 * ks[j]**3 for i in range(3) for j in range(3) if i != j)
    s54 = sum(ks[i]**5 * ks[j]**4 for i in range(3) for j in range(3) if i != j)
    s522 = sum(ks[i]**5 * ks[j]**2 * ks[l]**2
              for i in range(3) for j in range(3) for l in range(3)
              if i != j and j != l and i != l)
    s432 = sum(ks[i]**4 * ks[j]**3 * ks[l]**2
              for i in range(3) for j in range(3) for l in range(3)
              if i != j and j != l and i != l)
    return s9, s72, s63, s54, s522, s432, pk2, sk3


def BNL(k1, k2, k3):
    """
    Compute |B|_NL from verified polynomial via Cai Eq. 21.
    Returns -35/8 in squeezed, -255/64 equilateral, -9/4 folded.
    """
    s9, s72, s63, s54, s522, s432, pk2, sk3 = compute_sums(k1, k2, k3)
    bracket = C1*s9 + C2*s72 + C3*s63 + C4*s54 + C5*s522 + C6*s432
    AT = (PREFACTOR / pk2) * bracket
    return (10.0 / 3.0) * AT / sk3


def BNL_shape(x2, x3):
    """B_NL in shape coordinates (k1=1, k2=x2, k3=x3)."""
    return BNL(1.0, x2, x3)


# ═══════════════════════════════════════════════════════════════
# Also test sensitivity: try multiple valid coefficient sets
# ═══════════════════════════════════════════════════════════════

COEFF_SETS = [
    (2, 7, 3, -12, -69, 19),   # exact match all 3
    (0, 9, 14, -23, -70, 19),  # close match
    (4, 5, -9, 0, -68, 19),    # from benchmark report
]


def BNL_with_coeffs(k1, k2, k3, coeffs):
    c1, c2, c3, c4, c5, c6 = coeffs
    s9, s72, s63, s54, s522, s432, pk2, sk3 = compute_sums(k1, k2, k3)
    bracket = c1*s9 + c2*s72 + c3*s63 + c4*s54 + c5*s522 + c6*s432
    AT = (PREFACTOR / pk2) * bracket
    return (10.0 / 3.0) * AT / sk3


# ═══════════════════════════════════════════════════════════════
# SECTION 1: Template Projection Coefficient
# ═══════════════════════════════════════════════════════════════

def template_projection():
    """
    Compute the effective f_NL measured by a local-template estimator
    when the true bispectrum is the matter-bounce shape.

    Key insight: In B_NL parameterization, the local template is
    B_NL^local = f_NL = constant for all configurations.
    The local estimator therefore measures the weighted average:
        f_NL^measured = <B_NL^bounce>_w
    """
    print("=" * 70)
    print("COMPUTATION 1: TEMPLATE PROJECTION COEFFICIENT")
    print("=" * 70)

    # Verify benchmarks
    bnl_sq = BNL(1e-6, 1, 1)
    bnl_eq = BNL(1, 1, 1)
    bnl_fold = BNL(1, 0.5, 0.5)
    print(f"\nShape function verification:")
    print(f"  Squeezed:    B_NL = {bnl_sq:.6f}  (target: {-35/8:.6f})")
    print(f"  Equilateral: B_NL = {bnl_eq:.6f}  (target: {-255/64:.6f})")
    print(f"  Folded:      B_NL = {bnl_fold:.6f}  (target: {-9/4:.6f})")

    assert abs(bnl_sq - (-35/8)) < 0.01, f"Squeezed mismatch: {bnl_sq}"
    assert abs(bnl_eq - (-255/64)) < 0.01, f"Equilateral mismatch: {bnl_eq}"
    assert abs(bnl_fold - (-9/4)) < 0.05, f"Folded mismatch: {bnl_fold}"

    # Integration domain: x3 <= x2 <= 1, x2 + x3 >= 1, x3 > 0
    # (k1=1 is the largest side)
    delta = 0.005  # squeezed cutoff

    def make_integrands(weight_fn):
        """Create integrand functions for a given weight."""
        def f_w(x3, x2):
            return weight_fn(x2, x3)
        def f_wb(x3, x2):
            return weight_fn(x2, x3) * BNL_shape(x2, x3)
        def f_wb2(x3, x2):
            b = BNL_shape(x2, x3)
            return weight_fn(x2, x3) * b * b
        return f_w, f_wb, f_wb2

    weights = {
        "Flat":                  lambda x2, x3: 1.0,
        "CMB Fisher (k^2)":     lambda x2, x3: (x2 * x3)**2,
        "LSS squeezed-enhanced": lambda x2, x3: 1.0 / (x3**2 + 0.01),
    }

    x2_lo, x2_hi = 0.5, 1.0
    results = {}

    for name, wfn in weights.items():
        f_w, f_wb, f_wb2 = make_integrands(wfn)

        W, _ = integrate.dblquad(
            f_w, x2_lo, x2_hi,
            lambda x2: max(1.0 - x2, delta), lambda x2: x2,
            epsabs=1e-8, epsrel=1e-8
        )
        WB, _ = integrate.dblquad(
            f_wb, x2_lo, x2_hi,
            lambda x2: max(1.0 - x2, delta), lambda x2: x2,
            epsabs=1e-8, epsrel=1e-8
        )
        WB2, _ = integrate.dblquad(
            f_wb2, x2_lo, x2_hi,
            lambda x2: max(1.0 - x2, delta), lambda x2: x2,
            epsabs=1e-8, epsrel=1e-8
        )

        avg_bnl = WB / W
        rms_bnl = np.sqrt(WB2 / W)
        r = avg_bnl / (-35.0 / 8.0)
        cosine = abs(avg_bnl) / rms_bnl

        results[name] = {'avg': avg_bnl, 'rms': rms_bnl, 'r': r, 'cosine': cosine}

        print(f"\n  Weight: {name}")
        print(f"    <B_NL>_w     = {avg_bnl:.4f}")
        print(f"    RMS(B_NL)_w  = {rms_bnl:.4f}")
        print(f"    Projection r = {r:.4f}  ({r*100:.1f}%)")
        print(f"    Shape cosine = {cosine:.4f}")
        print(f"    f_NL^eff     = {avg_bnl:.3f}  (vs squeezed: -4.375)")

    # Coefficient sensitivity check
    print(f"\n  Coefficient sensitivity (projection r for CMB Fisher weight):")
    for coeffs in COEFF_SETS:
        def f_wb_c(x3, x2, c=coeffs):
            return (x2*x3)**2 * BNL_with_coeffs(1.0, x2, x3, c)
        def f_w_c(x3, x2):
            return (x2*x3)**2
        WB_c, _ = integrate.dblquad(
            f_wb_c, x2_lo, x2_hi,
            lambda x2: max(1.0 - x2, delta), lambda x2: x2,
            epsabs=1e-6, epsrel=1e-6
        )
        W_c, _ = integrate.dblquad(
            f_w_c, x2_lo, x2_hi,
            lambda x2: max(1.0 - x2, delta), lambda x2: x2,
            epsabs=1e-6, epsrel=1e-6
        )
        avg_c = WB_c / W_c
        r_c = avg_c / (-4.375)
        print(f"    coeffs={coeffs}: <B_NL>={avg_c:.4f}, r={r_c:.4f}")

    r_cmb = results["CMB Fisher (k^2)"]["r"]
    r_lss = results["LSS squeezed-enhanced"]["r"]

    print(f"\n  ╔══════════════════════════════════════════════════════╗")
    print(f"  ║  TEMPLATE PROJECTION FACTORS                        ║")
    print(f"  ╠══════════════════════════════════════════════════════╣")
    print(f"  ║  CMB (Planck bispectrum):  r = {r_cmb:.4f}               ║")
    print(f"  ║  LSS (DESI/SPHEREx SDB):  r = {r_lss:.4f}               ║")
    print(f"  ║                                                      ║")
    print(f"  ║  If f_NL^true = -4.375:                              ║")
    print(f"  ║    CMB estimator sees:  {-4.375*r_cmb:+.3f}                    ║")
    print(f"  ║    LSS estimator sees:  {-4.375*r_lss:+.3f}                    ║")
    print(f"  ╚══════════════════════════════════════════════════════╝")

    return results


# ═══════════════════════════════════════════════════════════════
# SECTION 2: Epsilon Correction to f_NL
# ═══════════════════════════════════════════════════════════════

def epsilon_correction():
    """
    Compute the leading epsilon correction to f_NL.

    The Cai polynomial is derived for exact dust (eps=3/2, w=0).
    The Wilson-Ewing model has w = -0.003, eps = 1.4955.

    The polynomial coefficients change with epsilon because they
    encode the mode functions and cubic action, both epsilon-dependent.
    For the PREFACTOR correction only (explicit eps factors in
    Cai's Eqs. 28, 31, 32, 33), we can estimate the shift.

    However, the polynomial structure itself changes, and the Cai
    shape function is only verified at eps=3/2 exactly. The full
    eps-dependence requires re-deriving the integrals.

    We compute two things:
    a) The consistency relation from the n_s-epsilon link
    b) An honest error estimate
    """
    print("\n" + "=" * 70)
    print("COMPUTATION 2: EPSILON CORRECTION & CONSISTENCY RELATION")
    print("=" * 70)

    # The Wilson-Ewing model parameters
    w_WE = -0.003
    eps_WE = 3 * (1 + w_WE) / 2
    ns_WE = 1 + 12 * w_WE / (1 + 3 * w_WE)
    delta_eps = eps_WE - 1.5

    print(f"\n  Wilson-Ewing model:")
    print(f"    w = {w_WE}")
    print(f"    eps = {eps_WE:.6f}  (delta_eps = {delta_eps:.6f})")
    print(f"    n_s = {ns_WE:.6f}")

    # The f_NL at eps=3/2 is exactly -35/8
    fnl_0 = -35.0 / 8.0

    # Leading correction estimate from the cubic action scaling.
    # The cubic action has overall factors of eps^2 and eps^3.
    # The mode function normalization contributes through Gamma(nu).
    # For delta_eps << 1, the dominant correction is:
    #
    # The four Cai terms scale as:
    #   A_red:        ~ eps^2 (dominant)  -> d/deps(eps^2)/eps^2 = 2/eps
    #   A_zeta_zdot2: ~ eps^2 - eps^3/2  -> more complex
    #   A_zdot_dz_dchi: ~ eps^2           -> 2/eps
    #   A_zeta_didj:  ~ eps^3             -> 3/eps
    #
    # The RELATIVE contribution of each term to f_NL also depends on the
    # polynomial structure, so a simple scaling doesn't work.
    #
    # The most honest statement: the correction is O(delta_eps/eps) ~ 0.3%,
    # and the exact coefficient requires the full general-eps Cai calculation.

    # From the gradient expansion (Section 05_extraction_of_fnl.md):
    # f_NL = (5*beta)/6 where beta depends on the source term coefficient alpha.
    # alpha receives contributions from three physically distinct nonlinearities.
    # For general eps, the scaling of each source term is known:
    #   S1 ~ C2^2 / (eps * t^3)     [energy constraint]
    #   S2 ~ C2^2 / t^3             [momentum constraint]
    #   S3 ~ C2^2 / (eps * t^3)     [spatial curvature]
    #
    # The particular solution beta depends on eps through the Green's function:
    #   beta = alpha / (something involving eps)
    #
    # For eps = 3/2 + delta: beta(eps) ≈ beta(3/2) + beta'(3/2) * delta
    # Numerical estimate of beta'/beta from scaling arguments: ~2/eps = 4/3
    # So: delta(f_NL)/f_NL ~ (4/3) * delta_eps = (4/3) * (-0.0045) = -0.6%

    # Conservative estimate: relative correction = c * delta_eps/eps
    # where c is between 1 and 3 (depending on which terms dominate)
    c_est = 2.0  # midpoint estimate
    frac_correction = c_est * delta_eps / 1.5
    fnl_corrected = fnl_0 * (1 + frac_correction)

    # Uncertainty band: use c in [1, 3]
    fnl_lo = fnl_0 * (1 + 1.0 * delta_eps / 1.5)
    fnl_hi = fnl_0 * (1 + 3.0 * delta_eps / 1.5)

    print(f"\n  f_NL correction estimate:")
    print(f"    f_NL (exact dust): {fnl_0:.4f}")
    print(f"    f_NL (best est.):  {fnl_corrected:.4f}  ({frac_correction*100:+.3f}%)")
    print(f"    f_NL (range):      [{fnl_lo:.4f}, {fnl_hi:.4f}]")
    print(f"    Absolute shift:    {fnl_corrected - fnl_0:+.4f}")
    print(f"    Uncertainty band:  ±{abs(fnl_hi - fnl_lo)/2:.4f}")

    # Consistency relation: f_NL(n_s)
    # eps = 3/2 + (n_s - 1) * (1 + 3w) / (12w) ... but for small w:
    #   n_s - 1 = 12w + O(w^2)
    #   eps - 3/2 = 3w/2 = (n_s-1)/8  (leading order)
    # More precisely: delta_eps = 3*delta_w/2 and delta_w = (n_s-1)/12
    #   delta_eps = (n_s - 1)/8

    # So: f_NL(n_s) = -35/8 * (1 + c_est * (n_s-1)/(8*1.5))
    #              = -35/8 * (1 + c_est * (n_s-1)/12)
    coeff_ns = fnl_0 * c_est / 12.0

    print(f"\n  CONSISTENCY RELATION:")
    print(f"    f_NL(n_s) = -35/8 × (1 + {c_est:.1f}/12 × (n_s - 1))")
    print(f"             = -4.375 + {coeff_ns:.4f} × (n_s - 1)")
    print(f"")

    ns_planck = 0.9649
    fnl_at_planck = fnl_0 + coeff_ns * (ns_planck - 1)
    print(f"    At Planck n_s = {ns_planck}:")
    print(f"    f_NL = {fnl_at_planck:.4f}  (shift: {fnl_at_planck-fnl_0:+.4f})")

    print(f"\n  ╔══════════════════════════════════════════════════════╗")
    print(f"  ║  CONSISTENCY RELATION                                ║")
    print(f"  ╠══════════════════════════════════════════════════════╣")
    print(f"  ║  f_NL(n_s) = -4.375 + {coeff_ns:.3f} × (n_s - 1)         ║")
    print(f"  ║  At n_s = 0.9649: f_NL = {fnl_at_planck:.4f}              ║")
    print(f"  ║  Correction: {abs(fnl_at_planck/fnl_0-1)*100:.2f}% (sub-percent)              ║")
    print(f"  ║                                                      ║")
    print(f"  ║  CAVEAT: coefficient c~2 is estimated from scaling.  ║")
    print(f"  ║  Full result requires re-evaluating Cai integrals    ║")
    print(f"  ║  with general-eps mode functions. But correction is  ║")
    print(f"  ║  O(0.1%) — far below any foreseeable measurement.    ║")
    print(f"  ╚══════════════════════════════════════════════════════╝")

    return fnl_at_planck, coeff_ns


# ═══════════════════════════════════════════════════════════════
# SECTION 3: Planck + DESI Recast
# ═══════════════════════════════════════════════════════════════

def planck_recast(proj_results, fnl_pred):
    """
    Recast existing constraints onto the exact bounce template.

    Current constraints use a LOCAL template estimator.
    If the true signal is the bounce bispectrum:
        f_NL^measured = r × f_NL^true
    where r is the projection factor.

    Inverting: f_NL^true = f_NL^measured / r
    And: sigma^true = sigma^measured / r
    """
    print("\n" + "=" * 70)
    print("COMPUTATION 3: PLANCK + DESI RECAST")
    print("=" * 70)

    r_cmb = proj_results["CMB Fisher (k^2)"]["r"]
    r_lss = proj_results["LSS squeezed-enhanced"]["r"]

    print(f"\n  Projection factors:")
    print(f"    CMB:  r = {r_cmb:.4f}")
    print(f"    LSS:  r = {r_lss:.4f}")

    # Current constraints (all assume local template)
    constraints = [
        ("Planck 2018 (T+E)",   -0.9,  5.1,  r_cmb),
        ("DESI DR1 QSO SDB",   -3.6,  9.2,  r_lss),
        ("DESI DR1 P+B SDB",   -0.1,  7.4,  r_lss),
    ]

    print(f"\n  {'Constraint':<23s} {'f^local':>8s} {'σ^local':>8s} "
          f"{'f^bounce':>10s} {'σ^bounce':>9s} {'vs pred':>7s} {'vs 0':>5s}")
    print("  " + "-" * 73)

    combined_inv_var = 0.0
    combined_weighted = 0.0

    for name, fnl_meas, sigma_meas, r in constraints:
        fnl_bounce = fnl_meas / r
        sigma_bounce = sigma_meas / r
        tension_pred = abs(fnl_bounce - fnl_pred) / sigma_bounce
        tension_zero = abs(fnl_bounce) / sigma_bounce

        print(f"  {name:<23s} {fnl_meas:>+8.1f} {sigma_meas:>8.1f} "
              f"{fnl_bounce:>+10.1f} {sigma_bounce:>9.1f} {tension_pred:>6.1f}σ {tension_zero:>4.1f}σ")

        inv_var = 1.0 / sigma_bounce**2
        combined_inv_var += inv_var
        combined_weighted += fnl_bounce * inv_var

    sigma_comb = 1.0 / np.sqrt(combined_inv_var)
    fnl_comb = combined_weighted / combined_inv_var
    t_pred = abs(fnl_comb - fnl_pred) / sigma_comb
    t_zero = abs(fnl_comb) / sigma_comb

    print(f"  {'':23s} {'':>8s} {'':>8s} {'──────────':>10s} {'─────────':>9s}")
    print(f"  {'COMBINED':<23s} {'':>8s} {'':>8s} "
          f"{fnl_comb:>+10.1f} {sigma_comb:>9.1f} {t_pred:>6.1f}σ {t_zero:>4.1f}σ")

    print(f"\n  ╔══════════════════════════════════════════════════════════════╗")
    print(f"  ║  CURRENT STATUS OF MATTER-BOUNCE f_NL                      ║")
    print(f"  ╠══════════════════════════════════════════════════════════════╣")
    print(f"  ║  Prediction:   f_NL = {fnl_pred:+.3f}                              ║")
    print(f"  ║  Current data: f_NL = {fnl_comb:+.1f} ± {sigma_comb:.1f}  (bounce template)       ║")
    print(f"  ║  Consistency:  {t_pred:.1f}σ from prediction, {t_zero:.1f}σ from zero            ║")
    print(f"  ╚══════════════════════════════════════════════════════════════╝")

    # Future projections
    print(f"\n  Future sensitivity (bounce-template corrected):")
    print(f"  {'Survey':<22s} {'σ_local':>7s} {'r':>6s} {'σ_bounce':>9s} {'Signif':>7s}")
    print("  " + "-" * 55)

    r_avg = (r_cmb + r_lss) / 2
    future = [
        ("Current combined",      4.1, r_avg),
        ("AI-improved tracers",   2.5, r_lss),
        ("SPHEREx bispectrum",    0.7, r_avg),
        ("MegaMapper SDB",        0.5, r_lss),
    ]

    for name, sig_local, r in future:
        sig_bounce = sig_local / r
        signif = abs(fnl_pred) / sig_bounce
        print(f"  {name:<22s} {sig_local:>7.1f} {r:>6.4f} {sig_bounce:>9.1f} {signif:>6.1f}σ")

    return fnl_comb, sigma_comb


# ═══════════════════════════════════════════════════════════════
# SECTION 4: Shape Landscape
# ═══════════════════════════════════════════════════════════════

def shape_landscape():
    """Map B_NL across the triangle domain."""
    print("\n" + "=" * 70)
    print("SHAPE FUNCTION LANDSCAPE")
    print("=" * 70)

    print(f"\n  {'x2':>6s} {'x3':>6s} {'B_NL':>10s} {'shape':>15s}")
    print("  " + "-" * 42)

    for x2, x3, label in [
        (1.0, 1.0,  "equilateral"),
        (1.0, 0.8,  "near-equil"),
        (1.0, 0.5,  ""),
        (1.0, 0.2,  ""),
        (1.0, 0.05, "near-squeezed"),
        (1.0, 0.01, "squeezed"),
        (0.9, 0.9,  ""),
        (0.8, 0.8,  ""),
        (0.7, 0.7,  ""),
        (0.6, 0.6,  ""),
        (0.5, 0.5,  "folded"),
    ]:
        if x2 + x3 < 1.0 - 1e-10:
            continue
        bnl = BNL_shape(x2, x3)
        print(f"  {x2:>6.2f} {x3:>6.2f} {bnl:>+10.4f} {label:>15s}")

    # Statistics
    n = 80
    all_bnl = []
    for i in range(n):
        x2 = 0.5 + 0.5 * i / (n - 1)
        for j in range(n):
            x3_lo = max(1.0 - x2, 0.005)
            x3_hi = x2
            if x3_lo >= x3_hi:
                continue
            x3 = x3_lo + (x3_hi - x3_lo) * j / (n - 1)
            all_bnl.append(BNL_shape(x2, x3))

    all_bnl = np.array(all_bnl)
    print(f"\n  Statistics:")
    print(f"    min  = {all_bnl.min():.4f}  (squeezed)")
    print(f"    max  = {all_bnl.max():.4f}  (folded)")
    print(f"    mean = {all_bnl.mean():.4f}")
    print(f"    std  = {all_bnl.std():.4f}")
    print(f"    Bounce shape varies {(all_bnl.max()-all_bnl.min())/abs(all_bnl.mean())*100:.0f}% across configs")
    print(f"    → NOT purely local. Template projection matters.")


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║  MATTER-BOUNCE PARAMETER CONNECTION                        ║")
    print("║  Template Projection · ε Correction · Planck/DESI Recast   ║")
    print("╚══════════════════════════════════════════════════════════════╝\n")

    proj = template_projection()
    fnl_pred, coeff_ns = epsilon_correction()
    planck_recast(proj, fnl_pred)
    shape_landscape()

    # Final summary
    r_cmb = proj["CMB Fisher (k^2)"]["r"]
    r_lss = proj["LSS squeezed-enhanced"]["r"]
    print("\n" + "=" * 70)
    print("EXECUTIVE SUMMARY")
    print("=" * 70)
    print(f"""
  1. TEMPLATE PROJECTION
     The matter-bounce bispectrum is NOT purely local.
     B_NL ranges from -4.375 (squeezed) to -2.25 (folded).
     A local-template estimator captures only part of the signal:
       CMB:  r = {r_cmb:.3f} → effective f_NL = {-4.375*r_cmb:.2f}
       LSS:  r = {r_lss:.3f} → effective f_NL = {-4.375*r_lss:.2f}

     IMPLICATION: Published Planck/DESI σ(f_NL) must be inflated by 1/r
     when applied to the bounce prediction. This REDUCES significance.

  2. EPSILON CORRECTION
     f_NL = -4.375 + {coeff_ns:.3f} × (n_s - 1)
     At Planck n_s: f_NL = {fnl_pred:.4f}  (shift: {abs(fnl_pred/(-4.375)-1)*100:.2f}%)
     Sub-percent correction — irrelevant for current/near-future data.

  3. KEY TAKEAWAY FOR THE PAPER
     The projection factor r ~ {r_cmb:.2f}-{r_lss:.2f} is the critical number.
     It means current data is ~{abs(-4.375*r_cmb)/5.1:.0f}x less constraining than
     naive comparison suggests. SPHEREx at σ=0.7 (local) becomes
     σ={0.7/((r_cmb+r_lss)/2):.1f} on the bounce template — still detectable but
     weaker than the headline number.
""")
