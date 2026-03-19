#!/usr/bin/env python3
"""
Combined-integrand f_NL for the matter bounce.

ALL 6 Maldacena cubic action terms are summed into a SINGLE integrand
before numerical integration. This ensures that:
1. Growing-mode divergences cancel at the integrand level
2. The UV (early-time) divergences from individual χ-terms cancel in the sum
3. No catastrophic cancellation between separately computed large integrals

Uses mpmath for arbitrary precision to preserve Re[I] (which is 7 orders
below Im[I] but contributes 30% to the physical bispectrum through the
cross-term Im[ext]·Re[I]).
"""
from mpmath import mp, mpf, mpc, quad, exp, sqrt, fabs, re as mpre, im as mpim, j, inf, pi

mp.dps = 50  # 50 decimal digits

# ============================================================
# MODE FUNCTIONS
# ============================================================
def ghat(x):
    """Dimensionless stripped mode function."""
    return exp(-j*x) * (1 - j/x) / x**2

def ghat_prime(x):
    """d/dx of ghat."""
    return exp(-j*x) * (-j - mpf(3)/x + 3*j/x**2) / x**2


def compute_fnl_combined(r_val, xf_val, x0_val, eps_reg_val, dps=50, verbose=True):
    """
    Compute f_NL using the combined integrand (all 6 terms summed).

    Parameters:
        r_val: squeeze ratio k1/k
        xf_val: late-time cutoff (x = k*eta, negative)
        x0_val: early-time cutoff (large negative)
        eps_reg_val: iε regulator for convergence
        dps: decimal digits of precision
    """
    mp.dps = dps
    r = mpf(r_val)
    xf = mpf(xf_val)
    x0 = mpf(x0_val)
    eps_reg = mpf(eps_reg_val)

    # ============================================================
    # Mode functions at internal time x (units k=1, a0=M_Pl=1)
    # zeta_k = ghat(k*eta) / sqrt(6*k)
    # zeta'_k = sqrt(k) * ghat'(k*eta) / sqrt(6)  [d/d(eta)]
    # chi_k = -(3/2) * eta^4 * zeta'_k / k^2
    #
    # For short mode (k=1): zeta_k(x) = ghat(x)/sqrt(6)
    #                       zeta'_k(x) = ghat'(x)/sqrt(6)
    #                       chi_k(x) = -(3/2)*x^4*ghat'(x)/(sqrt(6))
    #
    # For long mode (k1=r): zeta_{k1}(x) = ghat(r*x)/sqrt(6*r)
    #                       zeta'_{k1}(x) = sqrt(r)*ghat'(r*x)/sqrt(6)
    #                       chi_{k1}(x) = -(3/2)*x^4*sqrt(r)*ghat'(r*x)/(sqrt(6)*r^2)
    # ============================================================

    s6 = sqrt(mpf(6))
    s6r = sqrt(6*r)

    def zk(x): return ghat(x) / s6
    def zk1(x): return ghat(r*x) / s6r
    def zkp(x): return ghat_prime(x) / s6
    def zk1p(x): return sqrt(r) * ghat_prime(r*x) / s6
    def chi_k(x): return mpf('-1.5') * x**4 * zkp(x)
    def chi_k1(x): return mpf('-1.5') * x**4 * zk1p(x) / r**2

    # ============================================================
    # COMBINED INTEGRAND: sum of all 6 terms at each x
    #
    # Each term contributes to the integrand of:
    # J = ∫ [combined] dx
    # B = -(9/2) * Im[ext * J] (in appropriate units)
    # f_NL = (5/12) * B / PP
    #
    # But we must be careful: different terms have different
    # overall coefficients and structures. The combined integrand
    # sums ALL vertex contributions for a given squeezed-limit
    # momentum configuration.
    #
    # The integrand for the in-in bispectrum (before ext multiplication) is:
    # -(coefficient) * (vertex integrand)
    # summed over all terms and permutations.
    #
    # For consistency, define the TOTAL integrand as:
    # F(x) = sum_terms [vertex_coeff * permutation_sum * integrand(x)]
    # Then B = -2 * Im[ext * ∫F dx]  (the -2 from the commutator)
    # ============================================================

    def combined_integrand(x):
        """Sum of all 6 Maldacena terms at point x."""
        d = exp(eps_reg * x)  # iε damping

        zk_val = zk(x)
        zk1_val = zk1(x)
        zkp_val = zkp(x)
        zk1p_val = zk1p(x)
        chi_k_val = chi_k(x)
        chi_k1_val = chi_k1(x)

        # ======== TERM 1: (9/4) a² ζ ζ'² ========
        # 3 perms: (k1 undiff) + 2*(k undiff, k1 diff)
        t1 = mpf('2.25') * x**4 * (
            zk1_val * zkp_val**2  # perm 1
            + 2 * zk_val * zk1p_val * zkp_val  # perms 2+3
        )

        # ======== TERM 2: (9/4) a² ζ (∂ζ)² ========
        # Dominant perm: k1 undiff, -k2·k3 ≈ +k² = 1
        # (perms with k1 in gradient: suppressed by k1²/k²)
        t2 = mpf('2.25') * x**4 * zk1_val * zk_val**2

        # ======== TERM 3: -2a²ε ζ'(∂ζ)(∂χ) ========
        # After χ substitution: -(9/2)·(kb·kc)/kc²·η⁸·ζ'_{ka}·ζ_{kb}·ζ'_{kc}
        #
        # 4 non-suppressed permutations in squeezed limit:
        # Assigns 1+2 (ka=k1, chi on short): coeff = +(9/2) each, mode fns = zk1p·zk·zkp
        # Assigns 4+6 (ka=k, chi on k1): coeff = +(9/4) each, mode fns = zkp·zk·zk1p
        # All have the SAME mode function product zk1p·zk·zkp
        # Total: 2*(9/2) + 2*(9/4) = 9 + 9/2 = 27/2
        t3 = mpf('13.5') * x**8 * zk1p_val * zk_val * zkp_val

        # ======== TERM 4: (9/16) a² ζ² ζ' ========
        # 3 perms: (k1 diff) + 2*(k diff)
        t4 = mpf('0.5625') * x**4 * (
            zk_val**2 * zk1p_val  # perm a: k1 differentiated
            + 2 * zk1_val * zk_val * zkp_val  # perms b+c: k differentiated
        )

        # ======== TERM 5: (3/4) ∂²ζ (∂χ)² ========
        # After χ-sub: (27/16)·k_a²·(k_b·k_c)/(k_b²k_c²)·η⁸·ζ·ζ'·ζ'
        # Dominant perms (b+c): ka=k, {kb,kc}={k1,k}
        # (3/4)·k²·(k1·k)/(k1²·k²)·ζ_k·χ_{k1}·χ_k * 2
        # k1·k ≈ -k1²/2, so factor = (3/4)·(-r²/2)·2 = -(3/4)·r²
        t5 = mpf('0.75') * (-r**2) * zk_val * chi_k1_val * chi_k_val

        # ======== TERM 6: (9/32) ∂²ζ χ² ========
        # Dominant perms (b+c): ka=k, {kb,kc}={k1,k}
        # (9/32)·(-k²)·ζ_k·χ_{k1}·χ_k * 2
        t6 = 2 * mpf('0.28125') * (-mpf(1)) * zk_val * chi_k1_val * chi_k_val

        return (t1 + t2 + t3 + t4 + t5 + t6) * d

    # ============================================================
    # INTEGRATION
    # ============================================================
    if verbose:
        print(f"Integrating combined (dps={dps}, xf={xf_val}, r={r_val}, x0={x0_val})...")

        # Check integrand at a few points
        for xtest in [mpf('-100'), mpf('-10'), mpf('-1'), mpf('-0.1')]:
            val = combined_integrand(xtest)
            print(f"  F({float(xtest):8.1f}) = {float(mpre(val)):+.6e} + {float(mpim(val)):+.6e}j")

    I_re = quad(lambda x: mpre(combined_integrand(x)), [x0, xf],
                method='tanh-sinh', maxdegree=8)
    I_im = quad(lambda x: mpim(combined_integrand(x)), [x0, xf],
                method='tanh-sinh', maxdegree=8)
    I_combined = mpc(I_re, I_im)

    if verbose:
        print(f"  I_combined = {float(mpre(I_combined)):+.10e} + {float(mpim(I_combined)):+.10e}j")
        print(f"  |Re/Im| = {float(fabs(mpre(I_combined)/mpim(I_combined))):.6e}")

    # ============================================================
    # EXTERNAL LEGS AND POWER SPECTRA
    # ============================================================
    ext = zk1(xf).conjugate() * (zk(xf).conjugate())**2
    P1 = fabs(zk1(xf))**2
    Pk = fabs(zk(xf))**2
    PP = P1 * Pk

    # ============================================================
    # BISPECTRUM AND f_NL
    # ============================================================
    # B = -2 * Im[ext * I_combined]
    product = ext * I_combined
    B = -2 * mpim(product)
    fnl_intr = mpf(5)/mpf(12) * B / PP
    fnl_total = fnl_intr + mpf(5)/mpf(4)

    if verbose:
        print(f"\n  ext = {float(mpre(ext)):+.6e} + {float(mpim(ext)):+.6e}j")
        print(f"  ext*I = {float(mpre(product)):+.6e} + {float(mpim(product)):+.6e}j")
        print(f"  Im[ext*I] = {float(mpim(product)):+.6e}")
        print(f"  B = {float(B):+.6e}")
        print(f"  PP = {float(PP):+.6e}")
        print(f"\n  f_NL (intrinsic) = {float(fnl_intr):+.10f}")
        print(f"  f_NL (field redef) = +1.2500000000")
        print(f"  f_NL (TOTAL)       = {float(fnl_total):+.10f}")
        print(f"\n  Targets: Cai=-4.375, L-B=-2.1875, T1-only=+1.5625")

    return float(fnl_intr), float(fnl_total)


if __name__ == "__main__":
    print("=" * 65)
    print("MATTER BOUNCE f_NL — COMBINED INTEGRAND (ALL 6 TERMS)")
    print("mpmath arbitrary precision")
    print("=" * 65)

    # Main computation
    fi, ft = compute_fnl_combined(
        r_val=1e-3, xf_val=-0.01, x0_val=-500,
        eps_reg_val=1e-4, dps=50, verbose=True
    )

    # Convergence tests
    print(f"\n{'='*65}")
    print("CONVERGENCE TESTS")
    print(f"{'='*65}")

    print("\n--- xf dependence ---")
    for xf in [-0.1, -0.05, -0.01, -0.005]:
        _, ft2 = compute_fnl_combined(r_val=1e-3, xf_val=xf, x0_val=-500,
                                       eps_reg_val=1e-4, dps=50, verbose=False)
        print(f"  xf={xf:8.4f}  f_NL={ft2:+.8f}")

    print("\n--- Squeeze ratio ---")
    for rv in [0.01, 0.001, 0.0001]:
        _, ft2 = compute_fnl_combined(r_val=rv, xf_val=-0.01, x0_val=-500,
                                       eps_reg_val=1e-4, dps=50, verbose=False)
        print(f"  r={rv:.5f}  f_NL={ft2:+.8f}")

    print("\n--- Precision ---")
    for dp in [30, 40, 50, 60]:
        _, ft2 = compute_fnl_combined(r_val=1e-3, xf_val=-0.01, x0_val=-500,
                                       eps_reg_val=1e-4, dps=dp, verbose=False)
        print(f"  dps={dp:3d}  f_NL={ft2:+.8f}")

    print("\n--- iε regulator ---")
    for eps in [1e-3, 1e-4, 1e-5]:
        _, ft2 = compute_fnl_combined(r_val=1e-3, xf_val=-0.01, x0_val=-500,
                                       eps_reg_val=eps, dps=50, verbose=False)
        print(f"  ε={eps:.0e}  f_NL={ft2:+.8f}")

    print("\nDone.")
