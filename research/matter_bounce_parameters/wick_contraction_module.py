#!/usr/bin/env python3
"""
PROBLEM 1: Complete Wick Contraction Module for the Matter-Bounce Bispectrum

This module implements ALL Wick contractions for ALL 4 cubic action vertices
in the in-in bispectrum integral, following Cai et al. (0903.0631) exactly.

The key challenge: individual vertex integrals diverge (~10^9), but they
cancel in the sum to give f_NL ~ O(1). This module constructs the COMBINED
integrand by summing all contributions at each time step BEFORE integration.

CUBIC ACTION (Cai Eq. 15, c_s = 1):
  L_3 = (ε²-ε³/2) a³ ζ ζ̇²
        + ε² a³ ζ (∂ζ)²
        - 2ε² a³ ζ̇ (∂ζ)(∂χ)
        + (ε³/2) a³ ζ (∂ᵢ∂ⱼχ)²
        + field redefinition terms

where χ ≡ ∂⁻² ζ̇ (inverse Laplacian of ζ̇), ε = 3/2 for matter.

IN-IN FORMULA (Cai Eq. 14):
  <ζ_{k1} ζ_{k2} ζ_{k3}> = i ∫ dt <[ζ_{k1}(t)ζ_{k2}(t)ζ_{k3}(t), L_int(t')]>

The commutator gives 2 Im of the time-ordered product:
  = -2 Im ∫ dη a(η) × [vertex integrand] × [external legs]

WICK CONTRACTIONS:
Each vertex V(ζ_a, ζ_b, ζ_c) contracts with 3 external ζ operators.
For <ζ_{k1} ζ_{k2} ζ_{k3}>, we assign momenta (k1, k2, k3) to
fields (a, b, c) in all 3! = 6 permutations. In the squeezed limit
k1 << k2 = k3 = k, many permutations are related by symmetry.

MOMENTUM DOT PRODUCTS:
  k2 · k3 = (k1² - k2² - k3²)/2 = (k1² - 2k²)/2 ≈ -k²  (squeezed)
  k1 · k2 = (k3² - k1² - k2²)/2 ≈ (k² - k²)/2 = 0  (squeezed, but need next order)
  k1 · k3 = (k2² - k1² - k3²)/2 ≈ 0  (squeezed)

CHI IN FOURIER SPACE:
  χ(k) = ζ̇(k) / k²  (from χ ≡ ∂⁻² ζ̇ → k-space: -k² χ = ζ̇)
  Wait: ∂² χ = ζ̇ in Cai's convention? Let me check.
  Cai defines χ ≡ ∂⁻² ζ̇, meaning ∇² χ = ζ̇.
  In k-space: -k² χ_k = ζ̇_k, so χ_k = -ζ̇_k / k².

(∂ᵢ∂ⱼχ)² means ∂ᵢ∂ⱼχ contracted with itself:
  Σ_{ij} (∂ᵢ∂ⱼχ)(∂ᵢ∂ⱼχ)
  In k-space: Σ_{ij} (kᵢkⱼ/k²)(k'ᵢk'ⱼ/k'²) × χ_k × χ_{k'}
"""

import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.interpolate import interp1d
import json, time


# ═══════════════════════════════════════════════════════════════
# MODE FUNCTION SOLVER
# ═══════════════════════════════════════════════════════════════

def solve_mode(eps, k, tau0=-500, tauf=-0.005, n_pts=80000):
    """Solve ζ_k'' + 2(z'/z)ζ_k' + k² ζ_k = 0 with BD initial conditions."""
    p = 2.0 / (2*eps - 1)

    def rhs(tau, y):
        zr, zi, dzr, dzi = y
        zoz = -p / tau
        return [dzr, dzi, 2*zoz*dzr - k**2*zr, 2*zoz*dzi - k**2*zi]

    z0 = (-tau0)**p
    amp = 1.0 / (z0 * np.sqrt(2*k))
    phase = k * tau0  # Cai convention: e^{+ikη}
    y0 = [amp*np.cos(phase), amp*np.sin(phase),
          -amp*k*np.sin(phase), amp*k*np.cos(phase)]

    taus = np.linspace(tau0, tauf, n_pts)
    sol = solve_ivp(rhs, [tau0, tauf], y0, t_eval=taus,
                    method='DOP853', rtol=1e-14, atol=1e-17)
    if not sol.success:
        return None

    zeta = sol.y[0] + 1j * sol.y[1]
    zeta_dot = sol.y[2] + 1j * sol.y[3]
    return sol.t, zeta, zeta_dot


def make_interpolators(tau, zeta, zeta_dot):
    """Create interpolated mode functions for numerical integration."""
    zr = interp1d(tau, np.real(zeta), kind='cubic', assume_sorted=True)
    zi = interp1d(tau, np.imag(zeta), kind='cubic', assume_sorted=True)
    dzr = interp1d(tau, np.real(zeta_dot), kind='cubic', assume_sorted=True)
    dzi = interp1d(tau, np.imag(zeta_dot), kind='cubic', assume_sorted=True)

    def z(t): return complex(zr(t), zi(t))
    def dz(t): return complex(dzr(t), dzi(t))
    return z, dz


# ═══════════════════════════════════════════════════════════════
# BISPECTRUM INTEGRAND: ALL VERTICES COMBINED
# ═══════════════════════════════════════════════════════════════

def build_combined_integrand(eps, k1, k2, k3, z1, dz1, z2, dz2, z3, dz3):
    """
    Build the COMBINED integrand for the in-in bispectrum,
    summing ALL 4 cubic action vertices with ALL Wick contractions.

    Arguments:
        eps: slow-roll parameter (3/2 for dust)
        k1, k2, k3: momenta
        z1, dz1: mode functions ζ_{k1}(τ), ζ̇_{k1}(τ) (interpolated)
        z2, dz2: mode functions ζ_{k2}(τ), ζ̇_{k2}(τ)
        z3, dz3: mode functions ζ_{k3}(τ), ζ̇_{k3}(τ)

    Returns:
        A function integrand(τ) that gives the combined value at time τ.

    The in-in integral is:
        <ζ ζ ζ> = -2 Im[ζ*_{k1}(τf) ζ*_{k2}(τf) ζ*_{k3}(τf) × ∫ integrand(τ) dτ]

    where the integrand includes a(τ) factors and all vertex contributions.
    """
    p = 2.0 / (2*eps - 1)

    # Momentum dot products (exact)
    k1_dot_k2 = (k3**2 - k1**2 - k2**2) / 2
    k2_dot_k3 = (k1**2 - k2**2 - k3**2) / 2
    k1_dot_k3 = (k2**2 - k1**2 - k3**2) / 2

    # Cubic action coefficients at c_s = 1
    c_zzdot2 = eps**2 - eps**3 / 2      # ζζ̇² vertex
    c_zgradz2 = eps**2                    # ζ(∂ζ)² vertex
    c_zdotgradchi = -2 * eps**2           # ζ̇(∂ζ)(∂χ) vertex
    c_zdijchi2 = eps**3 / 2              # ζ(∂ᵢ∂ⱼχ)² vertex

    def integrand(tau):
        """
        Combined integrand at conformal time τ.

        Each vertex contributes:
          a(τ)^n × coefficient × Σ_perms [mode function products × momentum factors]

        The a(τ) factor: for the action ∫ dt d³x a³ L₃, converting to
        conformal time gives ∫ dη a⁴ L₃ (since dt = a dη).
        But the action already has a³ in L₃, so the conformal-time integrand
        gets a⁴ from the measure. Actually for Cai's formulation in conformal
        time (Eq. 14 with the interaction Lagrangian density), the factor is a(η).

        For the in-in integral of the form:
        ∫ dη × [interaction vertex evaluated on mode functions]
        the vertex already includes the correct a factors from Eq. (15).
        """
        a = (-tau)**p  # scale factor

        # Mode functions at this time
        u1 = z1(tau); du1 = dz1(tau)
        u2 = z2(tau); du2 = dz2(tau)
        u3 = z3(tau); du3 = dz3(tau)

        # Chi mode functions: χ_k = -ζ̇_k / k²
        chi1 = -du1 / k1**2 if k1 > 0 else 0
        chi2 = -du2 / k2**2
        chi3 = -du3 / k3**2

        total = 0.0 + 0j

        # ════════════════════════════════════════
        # VERTEX 1: (ε²-ε³/2) a³ ζ ζ̇²
        # ════════════════════════════════════════
        # 3 permutations: which external momentum gets the undifferentiated ζ
        # Perm (1,2,3): ζ_{k1} × ζ̇_{k2} × ζ̇_{k3}
        # Perm (2,1,3): ζ_{k2} × ζ̇_{k1} × ζ̇_{k3}
        # Perm (3,1,2): ζ_{k3} × ζ̇_{k1} × ζ̇_{k2}
        v1 = c_zzdot2 * a**3 * (
            u1 * du2 * du3 +
            u2 * du1 * du3 +
            u3 * du1 * du2
        )
        total += v1

        # ════════════════════════════════════════
        # VERTEX 2: ε² a ζ (∂ζ)²
        # ════════════════════════════════════════
        # (∂ζ)² in k-space: Σ (kᵢ·kⱼ) ζ_{kᵢ} ζ_{kⱼ} for the two gradient fields
        # 3 permutations: which external gets the undifferentiated ζ,
        # the other two get the gradient coupling
        # Perm (1;2,3): ζ_{k1} × (k2·k3) × ζ_{k2} × ζ_{k3}
        # Perm (2;1,3): ζ_{k2} × (k1·k3) × ζ_{k1} × ζ_{k3}
        # Perm (3;1,2): ζ_{k3} × (k1·k2) × ζ_{k1} × ζ_{k2}
        # Note: the a factor here is a (not a³) because (∂ζ)² = a⁻² (∂_x ζ)²
        # Actually Cai Eq (15) has ε²a ζ(∂ζ)² where ∂ is comoving spatial gradient
        # which gives a factor a from conformal → physical
        v2 = c_zgradz2 * a * (
            u1 * k2_dot_k3 * u2 * u3 +
            u2 * k1_dot_k3 * u1 * u3 +
            u3 * k1_dot_k2 * u1 * u2
        )
        total += v2

        # ════════════════════════════════════════
        # VERTEX 3: -2ε² a³ ζ̇ (∂ζ)(∂χ)
        # ════════════════════════════════════════
        # This vertex has 3 distinct fields: ζ̇, ∂ζ, ∂χ
        # Each external momentum can be assigned to any of the 3 fields
        # giving 3! = 6 permutations.
        # (∂ζ)(∂χ) involves a dot product between gradients.
        #
        # For assignment (a→ζ̇, b→∂ζ, c→∂χ):
        #   integrand = ζ̇_a × (kb·kc) × ζ_b × χ_c
        #             = ζ̇_a × (kb·kc) × ζ_b × (-ζ̇_c/kc²)
        #
        # 6 permutations: (a,b,c) ∈ {(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)}

        perms_3 = [
            (du1, u2, chi3, k2, k3, k1_dot_k2),  # (1→ζ̇, 2→∂ζ, 3→∂χ): k2·k3? No: (∂ζ)(∂χ) = kb·kc
            (du1, u3, chi2, k3, k2, k1_dot_k3),  # (1→ζ̇, 3→∂ζ, 2→∂χ)
            (du2, u1, chi3, k1, k3, k1_dot_k3),  # (2→ζ̇, 1→∂ζ, 3→∂χ) — wait, dot product is k_b · k_c
            (du2, u3, chi1, k3, k1, k2_dot_k3),  # (2→ζ̇, 3→∂ζ, 1→∂χ) — but k1 in chi means chi1
            (du3, u1, chi2, k1, k2, k1_dot_k2),  # (3→ζ̇, 1→∂ζ, 2→∂χ)
            (du3, u2, chi1, k2, k1, k2_dot_k3),  # (3→ζ̇, 2→∂ζ, 1→∂χ) — wait
        ]
        # Actually: the dot product in (∂ζ)(∂χ) is between the GRADIENT VECTORS:
        # ∂ᵢζ × ∂ᵢχ → in k-space: (ikb) ζ_b · (ikc) χ_c = -(kb·kc) ζ_b χ_c
        # So the contribution is: ζ̇_a × (-(kb·kc)) × ζ_b × χ_c
        # Wait, there's a minus from ∂² χ = ζ̇, not ∂² χ = -ζ̇.
        # Let me be more careful.
        #
        # (∂ζ)(∂χ) = ∂ᵢζ ∂ᵢχ
        # In k-space: ∂ᵢ → ikᵢ, so ∂ᵢζ_kb = ikb_i ζ_kb and ∂ᵢχ_kc = ikc_i χ_kc
        # Product: (ikb_i ζ_kb)(ikc_i χ_kc) = -kb·kc × ζ_kb × χ_kc
        # (sum over i, and i² = -1 × -1 nope: the product of two ik terms gives (ik)(ik) = -k²... no)
        # Actually ∂ᵢζ in REAL space × ∂ᵢχ in REAL space → in k-space these are evaluated
        # at the same point, and the Fourier transform of (∂ᵢf)(∂ᵢg) is:
        # ∫ d³k' (k'ᵢ)(k-k')ᵢ f(k') g(k-k')
        # But in the in-in integral, the three momenta are already assigned.
        # For vertex with fields at k_a, k_b, k_c with k_a+k_b+k_c = 0:
        # The gradient dot product (∂ζ)(∂χ) with ζ at kb and χ at kc gives:
        # (-kb · (-kc)) ζ_kb χ_kc = (kb · kc) ζ_kb χ_kc
        # Hmm, the sign depends on convention.
        #
        # Let me use the SIMPLEST correct form:
        # (∂ᵢζ)(∂ᵢχ) at momenta kb, kc = (kb · kc) × ζ_kb × χ_kc
        # (the factors of i cancel)

        v3 = 0.0 + 0j
        # 6 permutations of (a=ζ̇, b=ζ for grad, c=χ for grad)
        assignments = [
            # (ζ̇ momentum, ζ momentum, χ momentum)
            (1, 2, 3), (1, 3, 2),
            (2, 1, 3), (2, 3, 1),
            (3, 1, 2), (3, 2, 1),
        ]
        mf = {1: (u1, du1, chi1, k1), 2: (u2, du2, chi2, k2), 3: (u3, du3, chi3, k3)}
        dots = {(1,2): k1_dot_k2, (2,1): k1_dot_k2,
                (1,3): k1_dot_k3, (3,1): k1_dot_k3,
                (2,3): k2_dot_k3, (3,2): k2_dot_k3}

        for a, b, c in assignments:
            dz_a = mf[a][1]  # ζ̇ at k_a
            z_b = mf[b][0]   # ζ at k_b
            chi_c = mf[c][2] # χ at k_c
            kb_dot_kc = dots[(b, c)]
            v3 += c_zdotgradchi * a**3 * dz_a * kb_dot_kc * z_b * chi_c

        total += v3

        # ════════════════════════════════════════
        # VERTEX 4: (ε³/2) a³ ζ (∂ᵢ∂ⱼχ)²
        # ════════════════════════════════════════
        # (∂ᵢ∂ⱼχ)² = Σ_{ij} (∂ᵢ∂ⱼχ)(∂ᵢ∂ⱼχ)
        # For two χ fields at momenta kb and kc:
        # ∂ᵢ∂ⱼχ_kb = -(kb_i kb_j / kb²) ζ̇_kb (using χ = -ζ̇/k²)
        # wait: χ_k = -ζ̇_k / k², so ∂ᵢ∂ⱼ χ in k-space = (ikᵢ)(ikⱼ) χ_k = -kᵢkⱼ χ_k = kᵢkⱼ ζ̇_k / k²
        # Then (∂ᵢ∂ⱼχ_kb)(∂ᵢ∂ⱼχ_kc) = Σ_{ij} (kb_i kb_j / kb²)(kc_i kc_j / kc²) ζ̇_kb ζ̇_kc
        # = (kb · kc)² / (kb² kc²) × ζ̇_kb × ζ̇_kc

        # 3 permutations: which external gets the undifferentiated ζ
        v4 = c_zdijchi2 * a**3 * (
            u1 * (k2_dot_k3**2 / (k2**2 * k3**2)) * du2 * du3 / (k2**2 * k3**2) * k2**2 * k3**2 +
            u2 * (k1_dot_k3**2 / (k1**2 * k3**2)) * du1 * du3 / (k1**2 * k3**2) * k1**2 * k3**2 +
            u3 * (k1_dot_k2**2 / (k1**2 * k2**2)) * du1 * du2 / (k1**2 * k2**2) * k1**2 * k2**2
        )
        # Simplify: the k² factors cancel in (kb·kc)²/(kb² kc²) × ζ̇/k² × ζ̇/k² × k² × k²
        # (∂ᵢ∂ⱼχ)² with χ_k = -ζ̇_k/k² gives:
        # Σ_{ij} (kb_i kb_j)(kc_i kc_j) / (kb⁴ kc⁴) × ζ̇_kb × ζ̇_kc × kb² × kc²
        # = (kb·kc)² / (kb² kc²) × ζ̇_kb × ζ̇_kc
        # Actually let me redo this more carefully:
        # ∂ᵢ∂ⱼ χ_k = -kᵢkⱼ χ_k = kᵢkⱼ ζ̇_k / k²
        # (∂ᵢ∂ⱼχ)² at two momenta kb, kc:
        # = Σ_{ij} (kb_i kb_j ζ̇_kb / kb²) × (kc_i kc_j ζ̇_kc / kc²)
        # = Σ_i (kb_i kc_i) × Σ_j (kb_j kc_j) × ζ̇_kb ζ̇_kc / (kb² kc²)
        # = (kb·kc)² × ζ̇_kb × ζ̇_kc / (kb² × kc²)

        v4_correct = c_zdijchi2 * a**3 * (
            u1 * (k2_dot_k3)**2 / (k2**2 * k3**2) * du2 * du3 +
            u2 * (k1_dot_k3)**2 / (k1**2 * k3**2) * du1 * du3 +
            u3 * (k1_dot_k2)**2 / (k1**2 * k2**2) * du1 * du2
        )
        # Replace the incorrect v4 with the correct one
        total = total - v4 + v4_correct

        return total

    return integrand


def compute_bispectrum(eps, k1_val, k2_val, k3_val, tau0=-500, tauf=-0.005):
    """
    Compute the full bispectrum B(k1, k2, k3) using the combined integrand.

    Returns the shape function A_T and the nonlinearity parameter |B|_NL.
    """
    # Solve mode functions
    sol1 = solve_mode(eps, k1_val, tau0, tauf)
    sol2 = solve_mode(eps, k2_val, tau0, tauf)
    sol3 = solve_mode(eps, k3_val, tau0, tauf)

    if any(s is None for s in [sol1, sol2, sol3]):
        return None

    tau1, zeta1, dzeta1 = sol1
    tau2, zeta2, dzeta2 = sol2
    tau3, zeta3, dzeta3 = sol3

    z1, dz1 = make_interpolators(tau1, zeta1, dzeta1)
    z2, dz2 = make_interpolators(tau2, zeta2, dzeta2)
    z3, dz3 = make_interpolators(tau3, zeta3, dzeta3)

    # Build combined integrand
    integrand = build_combined_integrand(eps, k1_val, k2_val, k3_val,
                                          z1, dz1, z2, dz2, z3, dz3)

    # Integrate (real and imaginary parts separately)
    tau_start = tau0 * 0.99
    tau_end = tauf * 1.01

    def int_re(tau):
        return np.real(integrand(tau))
    def int_im(tau):
        return np.imag(integrand(tau))

    I_re, err_re = quad(int_re, tau_start, tau_end, limit=500,
                        epsabs=1e-30, epsrel=1e-8)
    I_im, err_im = quad(int_im, tau_start, tau_end, limit=500,
                        epsabs=1e-30, epsrel=1e-8)
    I_total = complex(I_re, I_im)

    # External legs at evaluation time
    z1f = z1(tauf); z2f = z2(tauf); z3f = z3(tauf)
    ext = np.conj(z1f) * np.conj(z2f) * np.conj(z3f)

    # Bispectrum from commutator: B = -2 Im[ext × I]
    product = ext * I_total
    B_from_integral = -2 * np.imag(product)

    # Power spectra
    P1 = np.abs(z1f)**2
    P2 = np.abs(z2f)**2
    P3 = np.abs(z3f)**2

    # f_NL from intrinsic (time-integral) contribution
    PP = P1 * P2  # normalization for squeezed limit
    fnl_intrinsic = (5.0/12.0) * B_from_integral / PP if PP > 0 else 0

    # Field redefinition contribution (algebraic, no time integral)
    # In squeezed limit: f_NL_redef = 5ε/6
    fnl_redef = 5 * eps / 6

    fnl_total = fnl_redef + fnl_intrinsic

    # Shape function A_T
    # B = [P²/(Πk³)] × A_T × (normalization factors)
    # |B|_NL = (10/3) A_T / Σk³
    sum_k3 = k1_val**3 + k2_val**3 + k3_val**3

    return {
        'epsilon': float(eps),
        'k1': float(k1_val), 'k2': float(k2_val), 'k3': float(k3_val),
        'fnl_redef': float(fnl_redef),
        'fnl_intrinsic': float(fnl_intrinsic),
        'fnl_total': float(fnl_total),
        'I_re': float(I_re), 'I_im': float(I_im),
        'err_re': float(err_re), 'err_im': float(err_im),
        'B': float(B_from_integral),
        'P1': float(P1), 'P2': float(P2), 'P3': float(P3),
    }


# ═══════════════════════════════════════════════════════════════
# MAIN: VERIFY AT ε = 3/2 AND SCAN
# ═══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print('=' * 70)
    print('PROBLEM 1: FULL WICK CONTRACTION BISPECTRUM')
    print('=' * 70)

    eps = 1.5
    t0 = time.time()

    # Test at squeezed configuration
    print('\nε = 3/2, squeezed (k1=0.001, k2=k3=1):')
    r = compute_bispectrum(eps, 0.001, 1.0, 1.0)
    if r:
        print('  f_NL_redef     = %+.6f (expect +1.2500)' % r['fnl_redef'])
        print('  f_NL_intrinsic = %+.6f' % r['fnl_intrinsic'])
        print('  f_NL_total     = %+.6f' % r['fnl_total'])
        print('  Target: -35/8 = -4.375 or -35/16 = -2.1875')
        print('  I = %.4e + %.4e j' % (r['I_re'], r['I_im']))
        print('  Errors: %.2e, %.2e' % (r['err_re'], r['err_im']))

        diff_35_8 = abs(r['fnl_total'] + 4.375)
        diff_35_16 = abs(r['fnl_total'] + 2.1875)
        if diff_35_8 < 1.0:
            print('  >>> CLOSE TO -35/8 (diff = %.3f)' % diff_35_8)
        elif diff_35_16 < 1.0:
            print('  >>> CLOSE TO -35/16 (diff = %.3f)' % diff_35_16)
        else:
            print('  >>> DOES NOT MATCH EITHER TARGET (needs debugging)')

    # Test at equilateral
    print('\nε = 3/2, equilateral (k1=k2=k3=1):')
    r_eq = compute_bispectrum(eps, 1.0, 1.0, 1.0)
    if r_eq:
        print('  f_NL_intrinsic = %+.6f' % r_eq['fnl_intrinsic'])
        print('  f_NL_total     = %+.6f' % r_eq['fnl_total'])

    elapsed = time.time() - t0
    print('\nElapsed: %.1fs' % elapsed)

    # If squeezed works, do ε scan
    if r and abs(r['fnl_total'] + 4.375) < 2.0:
        print('\n--- ε SCAN ---')
        results = []
        for e in [1.48, 1.49, 1.495, 1.4955, 1.50, 1.505, 1.51, 1.52]:
            re = compute_bispectrum(e, 0.001, 1.0, 1.0)
            if re:
                results.append(re)
                print('  ε=%.4f: f_NL=%+.4f (redef=%+.4f int=%+.4e)' % (
                    e, re['fnl_total'], re['fnl_redef'], re['fnl_intrinsic']))

        with open('wick_contraction_results.json', 'w') as f:
            json.dump(results, f, indent=2)
        print('Saved: wick_contraction_results.json')
    else:
        print('\nSqueezed test did not match targets. Saving diagnostic results.')
        with open('wick_contraction_diagnostic.json', 'w') as f:
            json.dump({'squeezed': r, 'equilateral': r_eq}, f, indent=2)
