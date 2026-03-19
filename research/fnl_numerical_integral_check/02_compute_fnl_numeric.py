#!/usr/bin/env python3
"""
Numerical evaluation of f_NL for the matter bounce cosmology.

Computes the in-in bispectrum integral from scratch using exact Bunch-Davies
mode functions for matter contraction (w=0, epsilon=3/2, nu=3/2).

Target: f_NL = -35/8 (Cai et al.) or -35/16 (Li-Brandenberger)?

Author: Houston Golden / Claude Code
Date: 2026-03-17
"""

import numpy as np
from scipy import integrate
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# MODE FUNCTIONS
# =============================================================================
#
# Background: a(eta) = a0 * eta^2,  H = 2/eta,  epsilon = 3/2
# eta in (-inf, 0^-)
#
# Mukhanov-Sasaki: v_k'' + (k^2 - 2/eta^2) v_k = 0
# Bunch-Davies solution: v_k(eta) = e^{-ik*eta}/sqrt(2k) * (1 - i/(k*eta))
#
# Curvature perturbation: zeta_k = v_k / z,  z = a*sqrt(2*epsilon) = sqrt(3)*a0*eta^2
#
# "Stripped" mode function g_k(eta) = zeta_k(eta):
#   g_k(eta) = e^{-ik*eta} / (sqrt(6)*a0*k^{3/2}*eta^2) * (1 - i/(k*eta))
#
# Dimensionless: x = k*eta
#   g_k = k^{1/2}/(sqrt(6)*a0) * ghat(x)
#   ghat(x) = e^{-ix} * (1 - i/x) / x^2
#
#   g_k' = d(g_k)/d(eta) = k * k^{1/2}/(sqrt(6)*a0) * ghat'(x)
#   ghat'(x) = e^{-ix} * (-i - 3/x + 3i/x^2) / x^2

def ghat(x):
    """Dimensionless mode function ghat(x) = e^{-ix}(1 - i/x)/x^2"""
    return np.exp(-1j * x) * (1.0 - 1j / x) / x**2

def ghat_prime(x):
    """Derivative ghat'(x) = e^{-ix}(-i - 3/x + 3i/x^2)/x^2"""
    return np.exp(-1j * x) * (-1j - 3.0 / x + 3j / x**2) / x**2

def ghat_abs2(x):
    """
    |ghat(x)|^2 = (1 + 1/x^2) / x^4
    Used for power spectrum normalization.
    """
    return (1.0 + 1.0 / x**2) / x**4


# =============================================================================
# BISPECTRUM INTEGRAL — FULL NUMERICAL EVALUATION
# =============================================================================
#
# Dominant vertex: (9/4) M_Pl^2 * a^2 * zeta * (zeta')^2
#
# In-in bispectrum from this vertex:
#   B = -2 * (9/4) * M_Pl^2 * Im[ g*_{k1}(eta_f) g*_{k2}(eta_f) g*_{k3}(eta_f)
#       * sum_perms int_{-inf}^{eta_f} d(eta') a^2(eta') g_{ka}(eta') g'_{kb}(eta') g'_{kc}(eta') ]
#
# In squeezed limit k1 -> 0, k2 = k3 = k, using dimensionless x = k*eta:
#
# Permutation 1 (long mode zeta_{k1} undifferentiated):
#   integrand ~ g_{k1}(eta') * g'_k(eta') * g'_k(eta')
#   With long-mode approx g_{k1} ~ -i/(sqrt(6)*a0*k1^{3/2}*eta'^3)
#
# After extracting all prefactors, f_NL = (5/12)*B / (P(k1)*P(k)) reduces to
# a pure number involving dimensionless integrals.
#
# STRATEGY: Compute f_NL directly from the RATIO at finite eta_f, verify cancellation.

def compute_fnl_direct(squeeze_ratio=1e-3, xf=-0.01, x_early=-1000.0,
                       eps_reg=1e-4, include_subleading_perms=True,
                       verbose=True):
    """
    Compute f_NL by directly evaluating the bispectrum and power spectra
    at finite eta_f, then taking the ratio.

    All mode functions are exact Bunch-Davies. The long mode uses the
    superhorizon approximation only where k1*|eta| << 1.

    Parameters
    ----------
    squeeze_ratio : float
        k1/k ratio (should be << 1 for squeezed limit)
    xf : float
        x_f = k * eta_f (late-time cutoff, should be small negative)
    x_early : float
        x_early = k * eta_early (early-time cutoff, should be large negative)
    eps_reg : float
        iε regulator for convergence at early times
    include_subleading_perms : bool
        Whether to include permutations 2,3 (long mode differentiated)
    verbose : bool
        Print intermediate results

    Returns
    -------
    fnl_intrinsic : float
        The intrinsic f_NL from the in-in integral (before field redefinition)
    fnl_total : float
        Total f_NL = intrinsic + 5/4 (field redefinition)
    """

    r = squeeze_ratio  # k1/k

    # Late-time mode functions (at x_f = k*eta_f)
    # Long mode: x1_f = k1*eta_f = r * xf
    x1f = r * xf

    # -------------------------------------------------------
    # Power spectra at eta_f (divergent, but cancel in ratio)
    # P(k) = |g_k|^2 = k/(6*a0^2) * |ghat(xf)|^2
    # P(k1) = k1/(6*a0^2) * |ghat(x1f)|^2
    # Product: P(k1)*P(k) = k*k1/(36*a0^4) * |ghat(x1f)|^2 * |ghat(xf)|^2
    # -------------------------------------------------------

    P_product_dimless = ghat_abs2(x1f) * ghat_abs2(xf)  # dimensionless part
    # The full P(k1)*P(k) = (k*k1)/(36*a0^4) * P_product_dimless
    # But we'll track the dimensional prefactors separately.

    # -------------------------------------------------------
    # External mode functions for bispectrum
    # g*_{k1}(eta_f) * g*_k(eta_f) * g*_k(eta_f)
    # = [k1^{1/2}/(sqrt(6)*a0)]* [k^{1/2}/(sqrt(6)*a0)]^2 * ghat*(x1f) * ghat*(xf)^2
    # = k1^{1/2} * k / (6*sqrt(6)*a0^3) * ghat*(x1f) * ghat*(xf)^2
    # -------------------------------------------------------

    ext_dimless = np.conj(ghat(x1f)) * np.conj(ghat(xf))**2

    # -------------------------------------------------------
    # Internal integral: Permutation 1
    # long mode (k1) undifferentiated, short modes (k) differentiated
    #
    # Int = int d(eta') a0^2*eta'^4 * g_{k1}(eta') * g'_k(eta')^2
    #
    # In terms of x = k*eta':
    #   eta' = x/k,  d(eta') = dx/k
    #   eta'^4 = x^4/k^4
    #   g_{k1}(eta') = k1^{1/2}/(sqrt(6)*a0) * ghat(r*x)   [since k1*eta' = r*x]
    #   g'_k(eta') = k^{3/2}/(sqrt(6)*a0) * ghat'(x)         [since k*eta' = x]
    #
    # Int = a0^2 * (x^4/k^4) * k1^{1/2}/(sqrt(6)*a0) * ghat(r*x)
    #       * [k^{3/2}/(sqrt(6)*a0)]^2 * [ghat'(x)]^2 * dx/k
    #     = a0^2 * k1^{1/2} * k^3 / (6*sqrt(6)*a0^3)
    #       * (1/k^5) * int dx x^4 ghat(r*x) [ghat'(x)]^2
    #     = k1^{1/2} / (6*sqrt(6)*a0*k^2) * int dx x^4 ghat(r*x) [ghat'(x)]^2
    # -------------------------------------------------------

    def integrand_perm1_real(x):
        """Real part of x^4 * ghat(r*x) * [ghat'(x)]^2 with iε damping."""
        # iε prescription: multiply e^{-ikη} by e^{-ε|kη|} = e^{ε*x} (since x < 0)
        # This damps the oscillations at early times
        damping = np.exp(eps_reg * x)  # x is negative, so this -> 0 as x -> -inf
        val = x**4 * ghat(r * x) * ghat_prime(x)**2 * damping
        return val.real

    def integrand_perm1_imag(x):
        """Imaginary part."""
        damping = np.exp(eps_reg * x)
        val = x**4 * ghat(r * x) * ghat_prime(x)**2 * damping
        return val.imag

    # Integrate from x_early to x_f
    result_r1, err_r1 = integrate.quad(integrand_perm1_real, x_early, xf,
                                        limit=2000, epsabs=1e-14, epsrel=1e-12)
    result_i1, err_i1 = integrate.quad(integrand_perm1_imag, x_early, xf,
                                        limit=2000, epsabs=1e-14, epsrel=1e-12)

    J1 = complex(result_r1, result_i1)  # dimensionless integral for perm 1

    if verbose:
        print(f"Perm 1 integral: J1 = {J1:.10f}")
        print(f"  |J1| = {abs(J1):.10f}")
        print(f"  Quad errors: Re={err_r1:.2e}, Im={err_i1:.2e}")

    # -------------------------------------------------------
    # Permutations 2,3: long mode differentiated
    # g'_{k1}(eta') * g_k(eta') * g'_k(eta')  (×2 for perms 2 and 3)
    #
    # g'_{k1}(eta') = k1 * k1^{1/2}/(sqrt(6)*a0) * ghat'(r*x) * r
    #   Wait, more carefully:
    #   g'_{k1}(eta') = d/d(eta') g_{k1}(eta')
    #                 = k1^{1/2}/(sqrt(6)*a0) * d/d(eta') ghat(k1*eta')
    #                 = k1^{1/2}/(sqrt(6)*a0) * k1 * ghat'(k1*eta')
    #                 = k1^{3/2}/(sqrt(6)*a0) * ghat'(r*x)
    #
    # g_k(eta') = k^{1/2}/(sqrt(6)*a0) * ghat(x)
    # g'_k(eta') = k^{3/2}/(sqrt(6)*a0) * ghat'(x)
    #
    # Integral for perm 2:
    # Int2 = a0^2 * int d(eta') eta'^4 * g'_{k1}(eta') * g_k(eta') * g'_k(eta')
    #      = a0^2 * k1^{3/2}*k^{1/2}*k^{3/2} / (6*sqrt(6)*a0^3)
    #        * (1/k^5) * int dx x^4 ghat'(r*x) ghat(x) ghat'(x)
    #      = k1^{3/2} / (6*sqrt(6)*a0*k) * int dx x^4 ghat'(r*x) ghat(x) ghat'(x)
    #
    # The ratio of Int2's prefactor to Int1's prefactor is:
    #   (k1^{3/2} / k) / (k1^{1/2} / k^2) = k1 * k / 1 = k1*k
    # Wait, let me redo: Int1 prefactor = k1^{1/2}/(6*sqrt(6)*a0*k^2)
    #                     Int2 prefactor = k1^{3/2}/(6*sqrt(6)*a0*k)
    # Ratio: Int2/Int1 ~ (k1/k) * (J2/J1)
    # Since k1/k = r << 1, Perm 2,3 are suppressed by r in the PREFACTOR,
    # but the integral J2 might be enhanced. Let's compute it anyway.
    # -------------------------------------------------------

    J2 = complex(0, 0)
    if include_subleading_perms:
        def integrand_perm2_real(x):
            damping = np.exp(eps_reg * x)
            val = x**4 * ghat_prime(r * x) * ghat(x) * ghat_prime(x) * damping
            return val.real

        def integrand_perm2_imag(x):
            damping = np.exp(eps_reg * x)
            val = x**4 * ghat_prime(r * x) * ghat(x) * ghat_prime(x) * damping
            return val.imag

        result_r2, err_r2 = integrate.quad(integrand_perm2_real, x_early, xf,
                                            limit=2000, epsabs=1e-14, epsrel=1e-12)
        result_i2, err_i2 = integrate.quad(integrand_perm2_imag, x_early, xf,
                                            limit=2000, epsabs=1e-14, epsrel=1e-12)
        J2 = complex(result_r2, result_i2)

        if verbose:
            print(f"Perm 2 integral: J2 = {J2:.10f}")
            print(f"  |J2| = {abs(J2):.10f}")

    # -------------------------------------------------------
    # Assemble the FULL bispectrum
    #
    # B = -2 * (9/4) * M_Pl^2 * Im[ ext * (I1 + I2 + I3) ]
    # where:
    #   ext = g*_{k1}(etaf) g*_k(etaf) g*_k(etaf)
    #       = k1^{1/2} * k / (6*sqrt(6)*a0^3) * ext_dimless
    #
    #   I1 = k1^{1/2} / (6*sqrt(6)*a0*k^2) * J1
    #   I2 = I3 = k1^{3/2} / (6*sqrt(6)*a0*k) * J2
    #
    # ext * I1 = [k1^{1/2}*k/(6*sqrt(6)*a0^3)] * [k1^{1/2}/(6*sqrt(6)*a0*k^2)]
    #            * ext_dimless * J1
    #          = k1 / (216*a0^4*k) * ext_dimless * J1
    #
    # ext * I2 = [k1^{1/2}*k/(6*sqrt(6)*a0^3)] * [k1^{3/2}/(6*sqrt(6)*a0*k)]
    #            * ext_dimless * J2
    #          = k1^2 / (216*a0^4) * ext_dimless * J2
    #
    # So ext * (I1 + 2*I2) = (k1/(216*a0^4)) * ext_dimless * (J1/k + 2*k1*J2)
    #
    # B = -2 * (9/4) * M_Pl^2 * k1/(216*a0^4) * Im[ext_dimless * (J1/k + 2*k1*J2)]
    #   = -(9/2) * M_Pl^2 * k1 / (216*a0^4) * Im[ext_dimless * (J1/k + 2*k1*J2)]
    #
    # Now P(k1)*P(k) = (k*k1)/(36*a0^4) * (1/(36*a0^4)) ... wait, I need to be
    # more careful. Let me use physical units properly.
    #
    # Actually, let me just compute f_NL as a ratio where everything cancels.
    # -------------------------------------------------------

    # CLEANER APPROACH: Work purely in dimensionless quantities.
    #
    # f_NL = (5/12) * B / (P(k1) * P(k))
    #
    # P(k) = k/(6*a0^2) * |ghat(xf)|^2
    # P(k1) = k1/(6*a0^2) * |ghat(x1f)|^2
    #
    # P(k1)*P(k) = k*k1/(36*a0^4) * |ghat(x1f)|^2 * |ghat(xf)|^2
    #
    # B = -2*(9/4)*M_Pl^2 * Im[...]
    #
    # Hmm, M_Pl^2 appears in B but not in P*P. This seems wrong — let me recheck.
    #
    # Actually, the cubic action is:
    #   S_3 = M_Pl^2 * int d^4x a^2 epsilon * (...)
    # But zeta has dimensions of 1, and the action is dimensionless.
    # The mode function g_k = v_k/z with z = a*sqrt(2*epsilon)*M_Pl
    # So g_k = v_k/(a*sqrt(2*epsilon)*M_Pl)
    #
    # Wait. Let me reconsider. The Mukhanov variable is v = z*R where z = a*sqrt(2*epsilon)*M_Pl
    # and R = zeta (comoving curvature perturbation).
    #
    # So v = z*zeta, meaning zeta = v/z = v/(a*sqrt(2*epsilon)*M_Pl)
    #
    # Power spectrum: P_zeta(k) = k^3/(2*pi^2) * |zeta_k|^2 = k^3/(2*pi^2) * |v_k|^2/z^2
    #
    # Actually, the simpler way: the relation B = <zeta zeta zeta> contains zeta^3,
    # and f_NL = (5/12)*B/P^2 contains zeta^3/zeta^4 = 1/zeta, so it's dimensionless.
    # The M_Pl dependence cancels between B (from the cubic action) and P^2 (from the
    # normalization of zeta).
    #
    # Let me just track everything carefully with z = a*sqrt(2*epsilon)*M_Pl = sqrt(3)*a0*eta^2*M_Pl
    #
    # zeta_k = v_k/z = v_k / (sqrt(3)*a0*eta^2*M_Pl)
    #        = e^{-iketa}*(1-i/(keta)) / (sqrt(2k)*sqrt(3)*a0*eta^2*M_Pl)
    #        = e^{-iketa}*(1-i/(keta)) / (sqrt(6k)*a0*eta^2*M_Pl)
    #
    # So g_k(eta) = zeta_k(eta) = (1/M_Pl) * e^{-iketa}/[sqrt(6k)*a0*eta^2] * (1-i/(keta))
    #
    # P(k) = |zeta_k(etaf)|^2 = 1/(M_Pl^2 * 6*a0^2*k*eta_f^4) * (1 + 1/(k*eta_f)^2)
    #       ... wait, I had |ghat(xf)|^2 above, let me just redo systematically.

    # ===== SYSTEMATIC DIMENSIONLESS COMPUTATION =====
    #
    # Define zeta_k(eta) = (1/(sqrt(6)*a0*M_Pl)) * (k^{-3/2}/eta^2) * e^{-iketa}*(1-i/(keta))
    #                    = (1/(sqrt(6)*a0*M_Pl*k^{1/2})) * ghat(x)    where x = keta
    #
    # Then zeta'_k(eta) = (k/(sqrt(6)*a0*M_Pl*k^{1/2})) * ghat'(x)
    #                   = (k^{1/2}/(sqrt(6)*a0*M_Pl)) * ghat'(x)
    #
    # Power spectrum (mode amplitude, NOT the P(k) with k^3/(2pi^2)):
    # <zeta_k zeta_k'> = (2pi)^3 delta(k+k') * |zeta_k|^2
    # |zeta_k(eta_f)|^2 = 1/(6*a0^2*M_Pl^2*k) * |ghat(xf)|^2
    #
    # For f_NL extraction we use the "non-k^3" convention:
    # B(k1,k2,k3) = <zeta_{k1} zeta_{k2} zeta_{k3}>'   (momentum-conserving part)
    # P(k) = |zeta_k|^2
    # f_NL = (5/12) * B(k1,k,k) / (P(k1)*P(k))   in squeezed limit
    #
    # Cubic vertex contribution to B:
    # B = -2 * (coefficient) * Im[zeta*_{k1} zeta*_{k2} zeta*_{k3} * int d(eta') a^2 ...]
    #
    # The coefficient of the dominant vertex in the cubic action is:
    # S_3 = M_Pl^2 * int d^3x d(eta) * a^2 * epsilon^2 * zeta * (zeta')^2
    #     = (9/4) * M_Pl^2 * int ... * zeta * (zeta')^2
    # Wait: the term is epsilon^2 * a^2 * zeta * (zeta')^2 and epsilon = 3/2 so epsilon^2 = 9/4.
    # But actually from Maldacena's action, the coefficient is just epsilon^2, which at epsilon=3/2
    # gives 9/4. But I should double-check.
    #
    # From file 02 (cubic action setup), the dominant term is:
    #   L_3 ⊃ a^2 * epsilon^2 * zeta * (zeta')^2  with coefficient = 1
    # so S_3 has M_Pl^2 * a^2 * epsilon^2 * zeta * (zeta')^2
    #
    # But actually in the Maldacena (2003) cubic action, the coefficient of the
    # zeta * (zeta')^2 term is just a^2 * epsilon, not epsilon^2.
    # Let me be MORE careful.
    #
    # From Maldacena (2003) Eq. (19) [or ADM form], the cubic Lagrangian has:
    #   L_3 = M_Pl^2 * [a * epsilon * zeta * (zeta')^2 + ...]
    # The factor is a*epsilon (with one factor of a, not a^2).
    #
    # Hmm, this depends on the gauge and variable conventions. Let me look at what
    # Cai et al. actually use and be consistent with our file 02.
    #
    # From our file 02:
    #   Term 1: a^2 * epsilon^2 * zeta * (zeta')^2
    # with the overall M_Pl^2 prefactor.
    #
    # Since epsilon = 3/2 is constant, epsilon^2 = 9/4.
    # And a^2 = a0^2 * eta^4.
    #
    # OK let me just proceed with the RATIO approach directly.
    # The key insight: f_NL is a pure number that doesn't depend on M_Pl or a0.
    # I'll compute it by tracking all factors and verifying they cancel.

    # ===== RATIO COMPUTATION =====
    #
    # Let me define everything in terms of dimensionless mode functions and track
    # the k-dependent prefactors.
    #
    # zeta_k = C_k * ghat(keta),   where C_k = 1/(sqrt(6)*a0*M_Pl*sqrt(k))
    # zeta'_k = C_k * k * ghat'(keta)
    #
    # P(k1) = C_{k1}^2 * |ghat(x1f)|^2 = 1/(6*a0^2*M_Pl^2*k1) * |ghat(x1f)|^2
    # P(k) = C_k^2 * |ghat(xf)|^2 = 1/(6*a0^2*M_Pl^2*k) * |ghat(xf)|^2
    #
    # P(k1)*P(k) = 1/(36*a0^4*M_Pl^4*k1*k) * |ghat(x1f)|^2 * |ghat(xf)|^2
    #
    # For the bispectrum:
    # B = -2 * epsilon^2 * M_Pl^2 * Im[zeta*_1 zeta*_2 zeta*_3 * sum_perms Integral]
    #
    # Perm 1: Integral_1 = int d(eta') a0^2*eta'^4 * zeta_{k1}(eta') * zeta'_k(eta')^2
    #   = a0^2 * C_{k1} * C_k^2 * k^2 * (1/k^5) * int dx x^4 ghat(r*x) [ghat'(x)]^2
    #   = a0^2 * C_{k1} * C_k^2 * (1/k^3) * J1
    #   where J1 = int dx x^4 ghat(r*x) [ghat'(x)]^2
    #
    # External: zeta*_1 zeta*_2 zeta*_3 = C_{k1} * C_k^2 * ghat*(x1f) * ghat*(xf)^2
    #
    # So: ext * Integral_1 = a0^2 * C_{k1}^2 * C_k^4 * (1/k^3) * ext_dimless * J1
    #   = a0^2 * [1/(6*a0^2*M_Pl^2)]^2 * [1/(k1*k^2)] * (1/k^3) * ext_dimless * J1
    #   ... hmm getting messy. Let me just track the ratio.
    #
    # f_NL = (5/12) * B / (P1*P)
    #       = (5/12) * [-2*eps^2*M_Pl^2 * Im(ext * sum I)] / (P1*P)
    #
    # For Perm 1:
    # ext*I1 = C_{k1}^2 * C_k^4 * k^2 * a0^2 / k^5 * ext_dimless * J1
    # P1*P = C_{k1}^2 * C_k^2 * |ghat(x1f)|^2 * |ghat(xf)|^2
    #
    # Ratio (ext*I1)/(P1*P) = C_k^2 * k^2 * a0^2 / k^5 * (ext_dimless*J1)/(|...|^2*|...|^2)
    #   = [1/(6*a0^2*M_Pl^2*k)] * a0^2/k^3 * (ext*J1)/(PP)
    #   = 1/(6*M_Pl^2*k^4) * (ext*J1)/(PP_dimless)
    #
    # And f_NL ~ (5/12)*(-2*eps^2*M_Pl^2) * 1/(6*M_Pl^2*k^4) * Im[ext*J1]/PP_dimless
    #          = (5/12)*(-2*9/4)/(6*k^4) * Im[ext*J1]/PP_dimless
    #          ...this still has k^4 in it, which must cancel from J1.
    #
    # J1 = int dx x^4 ghat(rx) [ghat'(x)]^2
    # Near xf -> 0: ghat(rx) ~ -i/(rx)^3 = -i/(r^3 x^3)
    #   ghat'(x)^2 ~ (-3/x)^2/x^4 * e^{-2ix} ... actually superhorizon:
    #   ghat'(x) ~ e^{-ix}*(-3/x + 3i/x^2)/x^2 -> -3/(x^3) + 3i/x^4
    #   [ghat'(x)]^2 -> 9/x^6 - 18i/x^7 - 9/x^8
    # So integrand ~ x^4 * (-i/(r^3 x^3)) * 9/x^6 = -9i/(r^3 x^5)
    # This diverges as x^{-5} near 0. So J1 ~ 1/(4*r^3*xf^4) diverges as xf^{-4}.
    #
    # This xf^{-4} divergence in J1 provides the k^4 (since xf = k*etaf, xf^{-4} = k^{-4}*etaf^{-4})
    # and the etaf^{-4} cancels against the power spectra (which go as etaf^{-6} each,
    # but ext goes as etaf^{-6} too, net etaf^{-4} in the ratio).
    # Actually: ext ~ (x1f)^{-6} * xf^{-12} ... no. Let me just compute numerically.
    #
    # I'll avoid all this algebra and just compute everything numerically.

    # =================================================================
    # DIRECT NUMERICAL COMPUTATION (no cancellation by hand)
    # =================================================================

    # Define: everything in units where k = 1, a0*M_Pl = 1
    # Then C_k = 1/sqrt(6), and P(k) = |ghat(xf)|^2/6, etc.

    # Power spectra (k=1 units):
    P_k1 = ghat_abs2(x1f) / (6.0 * r)    # P(k1) = |ghat(x1f)|^2 / (6*k1) with k1 = r
    P_k = ghat_abs2(xf) / 6.0              # P(k) = |ghat(xf)|^2 / 6

    PP = P_k1 * P_k

    # External modes (k=1 units):
    # zeta*_{k1} = (1/sqrt(6*k1)) * ghat*(x1f) = ghat*(x1f)/sqrt(6*r)
    # zeta*_k = (1/sqrt(6)) * ghat*(xf)
    # Product = ghat*(x1f)*ghat*(xf)^2 / (6*sqrt(6)*sqrt(r))
    ext = np.conj(ghat(x1f)) * np.conj(ghat(xf))**2 / (6.0 * np.sqrt(6.0) * np.sqrt(r))

    # Perm 1 integral (k=1 units):
    # int d(eta') * a0^2*eta'^4 * zeta_{k1}(eta') * zeta'_k(eta')^2
    # = a0^2 * C_{k1} * C_k^2 * k^2 / k^5 * J1     (with k=1, a0*M_Pl=1 so a0^2 * C^2 etc.)
    #
    # Let me just be very explicit:
    # zeta_{k1}(eta') = (1/sqrt(6*r)) * ghat(r*x)     [x = eta' since k=1]
    # zeta'_k(eta') = (1/sqrt(6)) * 1 * ghat'(x)       [k=1]
    # a0^2 * eta'^4 = 1 * x^4 / M_Pl^2    ... wait, a0^2*M_Pl^2 = 1, so a0^2 = 1/M_Pl^2
    #
    # Hmm, I set a0*M_Pl = 1, so a0 = 1/M_Pl, a0^2 = 1/M_Pl^2.
    #
    # This is getting tangled. Let me use a COMPLETELY EXPLICIT approach.

    # =================================================================
    # FULLY EXPLICIT: work in "natural" units for this problem
    # =================================================================
    # Set: k = 1 (momenta in units of k)
    #       a0 = 1 (scale factor normalization)
    #       M_Pl = 1 (Planck mass)
    # Then all physical quantities are pure numbers.
    #
    # Mode functions:
    #   zeta_k(eta) = ghat(keta) / sqrt(6*k)   [k in units of k_ref = 1]
    #   zeta'_k(eta) = k * ghat'(keta) / sqrt(6*k) = sqrt(k/6) * ghat'(keta)
    #
    # Power spectrum:
    #   P(k) = |zeta_k(eta_f)|^2 = |ghat(k*eta_f)|^2 / (6*k)
    #
    # Bispectrum from dominant vertex:
    #   S_3 = epsilon^2 * int d^3x deta a^2(eta) zeta(zeta')^2
    #   (with M_Pl = 1, and coefficient epsilon^2 from our file 02)
    #
    #   B = -2 * epsilon^2 * Im[ zeta*_1(etaf) zeta*_2(etaf) zeta*_3(etaf)
    #       * (Perm1 + Perm2 + Perm3) ]
    #
    #   Perm1 = int_{-inf}^{etaf} d(eta') a^2(eta') zeta_{k1}(eta') [zeta'_k(eta')]^2
    #
    # With k=1, k1=r:
    #   zeta_{k1}(eta') = ghat(r*eta') / sqrt(6*r)
    #   zeta'_k(eta') = ghat'(eta') / sqrt(6)  [k=1]
    #   a^2(eta') = eta'^4  [a0=1]
    #
    #   Perm1 = [1/sqrt(6*r)] * [1/6] * int d(eta') eta'^4 ghat(r*eta') [ghat'(eta')]^2
    #
    #   But eta' is dimensional (units of 1/k = 1). With x = k*eta' = eta':
    #   Perm1 = 1/(6*sqrt(6*r)) * J1     where J1 = int dx x^4 ghat(rx) [ghat'(x)]^2
    #
    #   Similarly for external modes:
    #   ext = zeta*_{k1}(etaf) * [zeta*_k(etaf)]^2
    #       = [ghat*(r*xf)/sqrt(6r)] * [ghat*(xf)/sqrt(6)]^2
    #       = ghat*(r*xf) * ghat*(xf)^2 / (6*sqrt(6r))
    #       = ghat*(x1f) * ghat*(xf)^2 / (6*sqrt(6*r))
    #
    # ext * Perm1 = [ghat*(x1f)*ghat*(xf)^2 / (6*sqrt(6r))] * [J1/(6*sqrt(6r))]
    #            = ghat*(x1f)*ghat*(xf)^2 * J1 / (36 * 6 * r)
    #            = ghat*(x1f)*ghat*(xf)^2 * J1 / (216 * r)
    #
    # B_perm1 = -2 * eps^2 * Im[ext*Perm1] = -2*(9/4) * Im[...] / (216*r)
    #         = -(9/2) / (216*r) * Im[ghat*(x1f)*ghat*(xf)^2 * J1]
    #         = -1/(48*r) * Im[ghat*(x1f)*ghat*(xf)^2 * J1]
    #
    # P(k1)*P(k) = |ghat(x1f)|^2/(6*r) * |ghat(xf)|^2/6 = |ghat(x1f)|^2*|ghat(xf)|^2/(36*r)
    #
    # f_NL_perm1 = (5/12) * B_perm1 / (P1*P)
    #            = (5/12) * [-1/(48*r)] * Im[ghat*(x1f)*ghat*(xf)^2 * J1]
    #              / [|ghat(x1f)|^2*|ghat(xf)|^2/(36*r)]
    #            = (5/12) * [-36*r/(48*r)] * Im[ghat*(x1f)*ghat*(xf)^2 * J1]
    #              / [|ghat(x1f)|^2*|ghat(xf)|^2]
    #            = (5/12) * (-3/4) * Im[ghat*(x1f)*ghat*(xf)^2*J1] / [|ghat(x1f)|^2*|ghat(xf)|^2]
    #            = -5/16 * Im[ghat*(x1f)*ghat*(xf)^2*J1] / [|ghat(x1f)|^2*|ghat(xf)|^2]

    # OK! Now I have a clean dimensionless formula. Let me verify:
    # f_NL_intrinsic (from Perm 1 alone) = -5/16 * Im[ghat*(x1f)*ghat*(xf)^2*J1] / [|ghat(x1f)|^2*|ghat(xf)|^2]
    #
    # But wait — I used epsilon^2 = 9/4 as the cubic action coefficient.
    # Let me double-check: from Maldacena (2003), the cubic action for single-field
    # in comoving gauge has:
    #   S_3 = M_Pl^2 int d^4x { a*epsilon^2*zeta*(zeta')^2 + ... }
    # Note: it's a*epsilon^2, not a^2*epsilon^2!
    #
    # From our file 02: "Term 1: a^2 * epsilon^2 * zeta * (zeta')^2"
    # This has a^2. But Maldacena has a*epsilon^2*zeta*(zeta')^2 / c_s^2, and
    # actually looking at it more carefully, the ADM cubic action has various terms.
    # The coefficient depends on the exact form.
    #
    # Let me reconsider. The standard Maldacena cubic action in conformal time is:
    #   S_3 = int d^3x deta [ epsilon^2 a zeta (zeta')^2 + ... ]
    # (See Maldacena 2003 Eq. 19, Chen et al. 2007, or any review)
    # Note: this is a (not a^2), and M_Pl^2 is absorbed into the definition with
    # the quadratic action giving the standard v_k normalization.
    #
    # Actually, the confusion arises because different references use different
    # overall normalizations. The standard form, with zeta canonically normalized
    # via v = z*zeta, z = a*sqrt(2*epsilon)*M_Pl, is:
    #
    # S_2 = (1/2) int d^3x deta [v'^2 - c_s^2 (∂v)^2 + (z''/z) v^2]
    # S_3 = ... (in terms of v or zeta)
    #
    # For the in-in calculation, the interaction Hamiltonian is:
    #   H_int = -L_3
    # And the bispectrum is:
    #   <zeta^3> = -i int_{-inf}^{eta_f} <[H_int(eta'), zeta^3(eta_f)]> deta'
    #            = 2 Im[ int_{-inf}^{eta_f} <zeta^3(etaf) H_int(eta')> deta' ]
    #
    # The issue is what exactly goes into H_int. Let me use Cai et al.'s notation
    # directly since we're comparing to their result.
    #
    # From Cai et al. (2009, arXiv:0903.0631), they use the Maldacena action and
    # define B_zeta via their Eq. (16). Their final answer is A_T which gives f_NL.
    #
    # Rather than re-derive the cubic action coefficient, let me take a different approach:
    # USE THE KNOWN RESULT FOR SLOW-ROLL INFLATION AS A CALIBRATION.
    #
    # In slow-roll inflation (de Sitter, epsilon -> 0), the dominant cubic vertex
    # gives f_NL = (5/12)*epsilon for the local shape, which matches the known
    # Maldacena consistency relation f_NL = (5/12)(1-n_s) ~ (5/12)*2*epsilon.
    # Wait, actually f_NL^local = (5/12)(1-n_s) = (5/6)*epsilon for slow-roll.
    # And the field redefinition gives 5*epsilon/6, with the intrinsic f_NL being
    # of order epsilon^2 (from the in-in integral). So for inflation, the in-in
    # integral gives a very small contribution.
    #
    # This calibration approach won't cleanly work. Let me instead go back to
    # first principles.

    # =================================================================
    # CLEAN DERIVATION FROM FIRST PRINCIPLES
    # =================================================================
    #
    # I'll follow the standard in-in formalism exactly.
    #
    # The cubic Lagrangian for a canonical scalar field (c_s = 1) driving
    # matter contraction, in comoving gauge, from Maldacena (2003):
    #
    # S_3 = int d^3x deta {
    #   a^2 epsilon [epsilon * zeta * (zeta')^2 - epsilon * zeta * (del zeta)^2
    #                + (1/2) d(epsilon/a')/deta * a'^2 * zeta^2 * zeta' + ...]
    # }
    #
    # where a' = a*H in conformal time sense, i.e., a' = da/deta = 2*a0*eta for
    # matter contraction. Actually I realize a' means aH? No, a' = da/deta.
    # For a = a0*eta^2: a' = 2*a0*eta, and a*H = a*(2/eta) = 2*a0*eta = a'.
    # So aH = a' for our background. Good.
    #
    # The first term is: a^2 * epsilon * epsilon * zeta * (zeta')^2
    #                   = a^2 * epsilon^2 * zeta * (zeta')^2
    #
    # OK so from our file 02, the coefficient IS a^2 * epsilon^2 = a0^2 * eta^4 * (9/4).
    # But Maldacena has a^2 * epsilon (with another epsilon inside).
    # Let me look at this differently.
    #
    # Standard form (e.g., Chen 2010 review, Eq. 2.15):
    # For c_s = 1, the leading cubic action is:
    #   S_3 ⊃ int d^3x deta * a^2 * epsilon^2 * zeta * (zeta')^2
    #
    # But this has NO explicit M_Pl dependence because zeta is already dimensionless
    # and the action is written in "reduced Planck units" where M_Pl = 1.
    # OR: the cubic action inherits M_Pl^2 from the overall Einstein-Hilbert action.
    #
    # The resolution: in the action S = M_Pl^2 int R ..., the quadratic action
    # for zeta is S_2 = M_Pl^2 int d^3x deta epsilon a^2 [(zeta')^2 - (del zeta)^2]
    # and the cubic is S_3 = M_Pl^2 int d^3x deta [epsilon^2 a^2 zeta (zeta')^2 + ...]
    #
    # The mode function v_k satisfies v_k'' + (k^2 - z''/z) v_k = 0
    # with v_k = z * zeta_k,  z = a*sqrt(2*epsilon)*M_Pl
    #
    # When we write zeta in terms of creation/annihilation operators:
    #   zeta(x,eta) = int d^3k/(2pi)^3 [zeta_k(eta) a_k e^{ikx} + h.c.]
    # with zeta_k = v_k/(z) = v_k/(a*sqrt(2*epsilon)*M_Pl)
    #
    # The in-in formula gives:
    # <zeta_{k1} zeta_{k2} zeta_{k3}> =
    #   -i int_{-inf}^{etaf} deta' <0|[H_3(eta'), zeta_{k1}(etaf) zeta_{k2}(etaf) zeta_{k3}(etaf)]|0>
    # = 2 Im{ zeta*_{k1}(etaf) zeta*_{k2}(etaf) zeta*_{k3}(etaf) * int deta' ... }
    #
    # For the vertex M_Pl^2 * a^2 * eps^2 * zeta * (zeta')^2:
    # H_3 = -L_3 in conformal time (up to spatial volume factor)
    # H_3 = -M_Pl^2 * a^2 * eps^2 * int d^3x zeta(zeta')^2
    #
    # When we Fourier transform and contract:
    # H_3 ⊃ -M_Pl^2 * eps^2 * a^2(eta') * zeta_{k1}(eta') * zeta'_{k2}(eta') * zeta'_{k3}(eta')
    #       + (2 more permutations)
    #
    # The contribution to the bispectrum (perm 1):
    # B_1 = -2 M_Pl^2 * eps^2 * Im{ zeta*_1(etaf) zeta*_2(etaf) zeta*_3(etaf)
    #        * int deta' a^2(eta') zeta_{k1}(eta') zeta'_k(eta') zeta'_k(eta') }
    #
    # Note the SIGN: H_3 = -L_3, and the in-in formula has -i*H_3, giving +i*L_3,
    # and B = 2*Im[+i * zeta*^3 * int zeta zeta' zeta'] = 2*Im[...]
    # Actually: B = 2*Im[ zeta*^3 * (-i) * int deta' <0|T{H_3(eta') zeta^3}|0> ]
    # = 2*Im[ zeta*^3 * (-i) * (-M_Pl^2 eps^2) * int deta' a^2 zeta zeta'^2 ]
    # = 2*M_Pl^2*eps^2 * Im[ i * zeta*^3 * int deta' a^2 zeta zeta'^2 ]
    # = 2*M_Pl^2*eps^2 * Re[ zeta*^3 * int deta' a^2 zeta zeta'^2 ]
    #   (since Im[i*z] = Re[z])
    # Hmm wait, Im[i*z] = Re[z] only if z is real. For complex z:
    # Im[i*(a+ib)] = Im[ia - b] = a = Re[z]. Yes, Im[i*z] = Re[z].
    #
    # So: B_1 = 2*M_Pl^2*eps^2 * Re[ zeta*_1 zeta*_2 zeta*_3 * int deta' a^2 zeta_1 zeta'_2 zeta'_3 ]
    #
    # Hmm, but the sign depends on the sign conventions in the in-in formula.
    # The standard in-in formula is:
    #   <Q(eta)> = <0| T_bar{ exp(i int H_I)} Q(eta) T{ exp(-i int H_I) } |0>
    # At first order:
    #   <zeta^3> = -i int_{-inf}^{eta} <0| [H_I(eta'), zeta^3(eta)] |0> deta'
    # The commutator [H_I, zeta^3] = H_I zeta^3 - zeta^3 H_I
    # = <..> = -i { <0|H_I zeta^3|0> - <0|zeta^3 H_I|0> } integrated
    # = -i { <0|H_I zeta^3|0> - c.c. } = -i * 2i * Im[<0|H_I zeta^3|0>]
    # = 2 Im[<0|H_I(eta') zeta^3(etaf)|0>]
    #
    # <0|H_I(eta') zeta^3(etaf)|0> contracts with zeta*^3(etaf) and zeta(eta'):
    # For vertex -M_Pl^2 eps^2 a^2 zeta zeta'^2:
    # <0| (-M_Pl^2 eps^2 a^2 zeta_{k1} zeta'_{k2} zeta'_{k3}) (zeta*_{k1} zeta*_{k2} zeta*_{k3}) |0>
    # = -M_Pl^2 eps^2 a^2 * zeta_{k1}(eta') zeta'_{k2}(eta') zeta'_{k3}(eta')
    #   * zeta*_{k1}(etaf) zeta*_{k2}(etaf) zeta*_{k3}(etaf)
    #
    # So: B_1 = 2 * Im[ int deta' (-M_Pl^2 eps^2 a^2) zeta_{k1} zeta'_k zeta'_k * zeta*_1 zeta*_k^2 ]
    #         = -2 M_Pl^2 eps^2 * Im[ zeta*_1 zeta*_k^2 int deta' a^2 zeta_{k1} zeta'_k^2 ]
    #
    # Great, so:
    # B = -2 M_Pl^2 eps^2 * Im[ zeta*_1 zeta*_k^2 * (sum of 3 perm integrals) ]
    #
    # f_NL = (5/12) * B / (P1 * P)

    eps = 1.5  # epsilon = 3/2 for matter contraction

    # In units k=1, a0=1, M_Pl=1:
    # zeta_k(eta) = ghat(k*eta)/sqrt(6*k)
    # zeta'_k(eta) = sqrt(k/6) * ghat'(k*eta)

    def zeta_k(k_val, x_dimless):
        """zeta mode function at dimensionless time x = k_ref*eta, for momentum k_val"""
        return ghat(k_val * x_dimless / 1.0) / np.sqrt(6.0 * k_val)
        # Actually x_dimless = eta (since k_ref=1), so k*eta = k_val * x_dimless

    # Wait, I defined x = k*eta earlier where k is the SHORT mode momentum.
    # But now I want eta as the variable (since k_ref = 1 means eta is in units of 1/k_ref).
    # Let me use eta directly, with k = 1 for short modes and k1 = r for long mode.

    # eta_f = xf (since k=1)
    eta_f = xf

    # Mode functions at eta_f:
    # Short mode (k=1): zeta_k(eta_f) = ghat(eta_f)/sqrt(6)
    # Long mode (k1=r): zeta_{k1}(eta_f) = ghat(r*eta_f)/sqrt(6*r)

    zeta_k1_f = ghat(r * eta_f) / np.sqrt(6.0 * r)
    zeta_k_f = ghat(eta_f) / np.sqrt(6.0)

    # Power spectra at eta_f:
    P1 = np.abs(zeta_k1_f)**2
    Pk = np.abs(zeta_k_f)**2
    PP_val = P1 * Pk

    # External modes product:
    ext_val = np.conj(zeta_k1_f) * np.conj(zeta_k_f)**2

    # Permutation 1 integral: int d(eta') eta'^4 * zeta_{k1}(eta') * [zeta'_k(eta')]^2
    # zeta_{k1}(eta') = ghat(r*eta')/sqrt(6*r)
    # zeta'_k(eta') = d/d(eta')[ghat(eta')/sqrt(6)] = ghat'(eta')/sqrt(6)  [k=1]
    #   Wait: zeta_k(eta) = ghat(k*eta)/sqrt(6*k), so
    #   zeta'_k(eta) = k*ghat'(k*eta)/sqrt(6*k) = sqrt(k)*ghat'(k*eta)/sqrt(6)
    #   For k=1: zeta'_k(eta) = ghat'(eta)/sqrt(6)
    #   For k1=r: zeta'_{k1}(eta) = sqrt(r)*ghat'(r*eta)/sqrt(6)

    def integrand_p1_real(eta):
        """Perm 1: zeta_{k1} * [zeta'_k]^2 * eta^4, real part"""
        damping = np.exp(eps_reg * eta)  # iε prescription
        z1 = ghat(r * eta) / np.sqrt(6.0 * r)  # zeta_{k1}
        zp = ghat_prime(eta) / np.sqrt(6.0)      # zeta'_k (k=1)
        val = eta**4 * z1 * zp**2 * damping
        return val.real

    def integrand_p1_imag(eta):
        damping = np.exp(eps_reg * eta)
        z1 = ghat(r * eta) / np.sqrt(6.0 * r)
        zp = ghat_prime(eta) / np.sqrt(6.0)
        val = eta**4 * z1 * zp**2 * damping
        return val.imag

    # Integrate
    I1_r, e1_r = integrate.quad(integrand_p1_real, x_early, eta_f,
                                 limit=5000, epsabs=1e-14, epsrel=1e-12)
    I1_i, e1_i = integrate.quad(integrand_p1_imag, x_early, eta_f,
                                 limit=5000, epsabs=1e-14, epsrel=1e-12)
    I1 = complex(I1_r, I1_i)

    if verbose:
        print(f"\n=== Permutation 1 (long mode undiff.) ===")
        print(f"I1 = {I1:.10e}")
        print(f"|I1| = {abs(I1):.10e}")
        print(f"Errors: Re={e1_r:.2e}, Im={e1_i:.2e}")

    # Permutations 2,3: zeta'_{k1} * zeta_k * zeta'_k * eta^4
    I2 = complex(0, 0)
    if include_subleading_perms:
        def integrand_p2_real(eta):
            damping = np.exp(eps_reg * eta)
            zp1 = np.sqrt(r) * ghat_prime(r * eta) / np.sqrt(6.0)  # zeta'_{k1}
            z_k = ghat(eta) / np.sqrt(6.0)           # zeta_k (k=1)
            zp_k = ghat_prime(eta) / np.sqrt(6.0)    # zeta'_k (k=1)
            val = eta**4 * zp1 * z_k * zp_k * damping
            return val.real

        def integrand_p2_imag(eta):
            damping = np.exp(eps_reg * eta)
            zp1 = np.sqrt(r) * ghat_prime(r * eta) / np.sqrt(6.0)
            z_k = ghat(eta) / np.sqrt(6.0)
            zp_k = ghat_prime(eta) / np.sqrt(6.0)
            val = eta**4 * zp1 * z_k * zp_k * damping
            return val.imag

        I2_r, e2_r = integrate.quad(integrand_p2_real, x_early, eta_f,
                                     limit=5000, epsabs=1e-14, epsrel=1e-12)
        I2_i, e2_i = integrate.quad(integrand_p2_imag, x_early, eta_f,
                                     limit=5000, epsabs=1e-14, epsrel=1e-12)
        I2 = complex(I2_r, I2_i)

        if verbose:
            print(f"\n=== Permutation 2 (long mode diff., ×2) ===")
            print(f"I2 = {I2:.10e}")
            print(f"|I2| = {abs(I2):.10e}")
            print(f"Errors: Re={e2_r:.2e}, Im={e2_i:.2e}")

    # Total integral (3 perms: 1 of type I1, 2 of type I2)
    I_total = I1 + 2.0 * I2

    # Bispectrum:
    # B = -2 * M_Pl^2 * eps^2 * Im[ ext * I_total ]
    # With M_Pl = 1:
    B_val = -2.0 * eps**2 * np.imag(ext_val * I_total)

    # f_NL:
    fnl_intrinsic = (5.0 / 12.0) * B_val / PP_val
    fnl_total = fnl_intrinsic + 5.0 / 4.0  # field redefinition

    if verbose:
        print(f"\n=== Assembly ===")
        print(f"ext * I_total = {ext_val * I_total:.10e}")
        print(f"Im[ext * I_total] = {np.imag(ext_val * I_total):.10e}")
        print(f"B = {B_val:.10e}")
        print(f"P(k1) = {P1:.10e}")
        print(f"P(k) = {Pk:.10e}")
        print(f"P(k1)*P(k) = {PP_val:.10e}")
        print(f"\n{'='*50}")
        print(f"f_NL (intrinsic) = {fnl_intrinsic:.6f}")
        print(f"f_NL (field redef) = {5.0/4.0:.6f}")
        print(f"f_NL (TOTAL)       = {fnl_total:.6f}")
        print(f"{'='*50}")
        print(f"\nComparison:")
        print(f"  Cai et al. (-35/8):  {-35.0/8.0:.6f}")
        print(f"  Li-Brand. (-35/16):  {-35.0/16.0:.6f}")
        print(f"  Our result:          {fnl_total:.6f}")

        # Check relative agreement
        diff_cai = abs(fnl_total - (-35.0/8.0)) / abs(35.0/8.0)
        diff_li = abs(fnl_total - (-35.0/16.0)) / abs(35.0/16.0)
        print(f"\n  Relative diff from Cai: {diff_cai:.6f} ({diff_cai*100:.4f}%)")
        print(f"  Relative diff from L-B: {diff_li:.6f} ({diff_li*100:.4f}%)")

    return fnl_intrinsic, fnl_total


def run_convergence_tests():
    """Run the computation with different parameters to test convergence."""

    print("=" * 70)
    print("CONVERGENCE TESTS")
    print("=" * 70)

    # 1. Vary eta_f (late-time cutoff)
    print("\n--- Test 1: Vary eta_f (should be independent) ---")
    for xf in [-0.1, -0.05, -0.01, -0.005, -0.001]:
        fi, ft = compute_fnl_direct(xf=xf, verbose=False)
        print(f"  xf = {xf:8.4f}  =>  f_NL = {ft:.6f}")

    # 2. Vary squeeze ratio
    print("\n--- Test 2: Vary squeeze ratio (should converge as r -> 0) ---")
    for r in [0.1, 0.01, 0.001, 0.0001]:
        fi, ft = compute_fnl_direct(squeeze_ratio=r, verbose=False)
        print(f"  k1/k = {r:8.5f}  =>  f_NL = {ft:.6f}")

    # 3. Vary early-time cutoff (UV)
    print("\n--- Test 3: Vary early-time cutoff (should converge) ---")
    for x0 in [-100, -500, -1000, -5000, -10000]:
        fi, ft = compute_fnl_direct(x_early=x0, verbose=False)
        print(f"  x_early = {x0:7d}  =>  f_NL = {ft:.6f}")

    # 4. Vary iε regulator
    print("\n--- Test 4: Vary iε regulator (should converge as ε -> 0) ---")
    for eps in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
        fi, ft = compute_fnl_direct(eps_reg=eps, verbose=False)
        print(f"  ε = {eps:.0e}  =>  f_NL = {ft:.6f}")

    # 5. Effect of subleading permutations
    print("\n--- Test 5: Subleading permutations ---")
    fi_no, ft_no = compute_fnl_direct(include_subleading_perms=False, verbose=False)
    fi_yes, ft_yes = compute_fnl_direct(include_subleading_perms=True, verbose=False)
    print(f"  Without perms 2,3: f_NL = {ft_no:.6f}")
    print(f"  With perms 2,3:    f_NL = {ft_yes:.6f}")
    print(f"  Difference:        {abs(ft_yes - ft_no):.6f}")


def run_subleading_vertices():
    """
    Check the contribution of subleading vertices in the cubic action.

    From file 02, the subleading terms are:
    Term 2: -a^2 * epsilon^2 * zeta * (del zeta)^2   [suppressed by k^2 eta^2]
    Term 3: (1/2) * a^2 * d(epsilon*H)/deta * (1/H) * zeta^2 * zeta'
            = (1/2) * a^2 * (3/4) * (eta/2) * zeta^2 * zeta'
            ... actually this needs more careful evaluation

    For now, we focus on Term 1 (dominant) and note that subleading terms are
    suppressed by (k*eta_f)^2 ~ xf^2 << 1 in the squeezed limit.
    """

    print("\n" + "=" * 70)
    print("SUBLEADING VERTEX CHECK (Term 2: gradient term)")
    print("=" * 70)

    # Term 2: -epsilon^2 * a^2 * zeta * (del zeta)^2
    # In Fourier space for our triangle: k2·k3 = (k1^2 - 2k^2)/2 ~ -k^2 for squeezed
    # So this contributes: +epsilon^2 * k^2 * a^2 * zeta_{k1} * zeta_k * zeta_k
    # (with +k^2 from the dot product of gradients, and no derivatives)

    r = 1e-3
    xf = -0.01
    x_early = -1000.0
    eps_reg = 1e-4
    eta_f = xf
    eps = 1.5

    def integrand_term2_real(eta):
        damping = np.exp(eps_reg * eta)
        z1 = ghat(r * eta) / np.sqrt(6.0 * r)
        zk1 = ghat(eta) / np.sqrt(6.0)
        zk2 = ghat(eta) / np.sqrt(6.0)
        # k2·k3 ~ -k^2 = -1 (k=1), and no derivatives on short modes
        val = eta**4 * z1 * zk1 * zk2 * (-1.0) * damping  # -k^2 from gradient
        return val.real

    def integrand_term2_imag(eta):
        damping = np.exp(eps_reg * eta)
        z1 = ghat(r * eta) / np.sqrt(6.0 * r)
        zk1 = ghat(eta) / np.sqrt(6.0)
        zk2 = ghat(eta) / np.sqrt(6.0)
        val = eta**4 * z1 * zk1 * zk2 * (-1.0) * damping
        return val.imag

    I_t2_r, _ = integrate.quad(integrand_term2_real, x_early, eta_f, limit=5000, epsabs=1e-14, epsrel=1e-12)
    I_t2_i, _ = integrate.quad(integrand_term2_imag, x_early, eta_f, limit=5000, epsabs=1e-14, epsrel=1e-12)
    I_t2 = complex(I_t2_r, I_t2_i)

    # Compare to Term 1
    def integrand_t1_real(eta):
        damping = np.exp(eps_reg * eta)
        z1 = ghat(r * eta) / np.sqrt(6.0 * r)
        zp = ghat_prime(eta) / np.sqrt(6.0)
        val = eta**4 * z1 * zp**2 * damping
        return val.real

    def integrand_t1_imag(eta):
        damping = np.exp(eps_reg * eta)
        z1 = ghat(r * eta) / np.sqrt(6.0 * r)
        zp = ghat_prime(eta) / np.sqrt(6.0)
        val = eta**4 * z1 * zp**2 * damping
        return val.imag

    I_t1_r, _ = integrate.quad(integrand_t1_real, x_early, eta_f, limit=5000, epsabs=1e-14, epsrel=1e-12)
    I_t1_i, _ = integrate.quad(integrand_t1_imag, x_early, eta_f, limit=5000, epsabs=1e-14, epsrel=1e-12)
    I_t1 = complex(I_t1_r, I_t1_i)

    ratio = abs(I_t2) / abs(I_t1) if abs(I_t1) > 0 else float('inf')
    print(f"  |I_term2| / |I_term1| = {ratio:.6f}")
    print(f"  Term 2 is {'negligible' if ratio < 0.01 else 'NON-NEGLIGIBLE'} ({ratio*100:.2f}% of Term 1)")


if __name__ == "__main__":
    print("=" * 70)
    print("NUMERICAL EVALUATION OF f_NL FOR MATTER BOUNCE")
    print("=" * 70)
    print("\nConventions:")
    print("  Background: a(eta) = a0*eta^2, H = 2/eta, epsilon = 3/2")
    print("  Mode eq: v'' + (k^2 - 2/eta^2)v = 0")
    print("  BD solution: v_k = e^{-iketa}/sqrt(2k) * (1 - i/(keta))")
    print("  f_NL = (5/12)*B/(P1*P) in Planck convention")
    print("  Field redef: +5/4")
    print(f"\nTarget values:")
    print(f"  Cai et al.:        f_NL = -35/8  = {-35/8:.6f}")
    print(f"  Li-Brandenberger:  f_NL = -35/16 = {-35/16:.6f}")

    # Main computation
    print("\n" + "=" * 70)
    print("MAIN COMPUTATION")
    print("=" * 70)
    fnl_i, fnl_t = compute_fnl_direct(
        squeeze_ratio=1e-3,
        xf=-0.01,
        x_early=-2000.0,
        eps_reg=1e-4,
        include_subleading_perms=True,
        verbose=True
    )

    # Convergence tests
    run_convergence_tests()

    # Subleading vertices
    run_subleading_vertices()

    print("\n" + "=" * 70)
    print("FINAL RESULT")
    print("=" * 70)
    print(f"\n  f_NL (intrinsic from in-in integral) = {fnl_i:.6f}")
    print(f"  f_NL (field redefinition)             = {5/4:.6f}")
    print(f"  f_NL (TOTAL)                          = {fnl_t:.6f}")
    print(f"\n  Expected -35/8  = {-35/8:.6f}")
    print(f"  Expected -35/16 = {-35/16:.6f}")

    if abs(fnl_t - (-35/8)) < 0.1:
        print(f"\n  >>> MATCHES Cai et al. (-35/8) <<<")
    elif abs(fnl_t - (-35/16)) < 0.1:
        print(f"\n  >>> MATCHES Li-Brandenberger (-35/16) <<<")
    else:
        print(f"\n  >>> MATCHES NEITHER — NEW RESULT <<<")
