#!/usr/bin/env python3
"""
CORRECTED v3: Exact conformal-time in-in integrand from Cai Eq. 15

Starting from Cai's COSMIC TIME cubic action:
  L_3 = (ε²-ε³/2)a³ ζ ζ̇² + ε²a ζ(∂ζ)² - 2ε²a³ ζ̇(∂ζ)(∂χ) + (ε³/2)a³ ζ(∂ᵢ∂ⱼχ)²
  where χ ≡ ∂⁻²ζ̇, dots are cosmic time.

Converting to conformal time (dt = a dη, ζ̇ = ζ'/a, χ_k = -ζ'_k/(a k²)):

  ∫ dt L_3 = ∫ dη × a × L_3

  Term 1: (ε²-ε³/2) × a × a³ × ζ × (ζ'/a)² = (ε²-ε³/2) × a² × ζ × ζ'²
  Term 2: ε² × a × a × ζ × (∂ζ)² = ε² × a² × ζ × (∂ζ)²  [BUT ∂ is comoving!]
  Term 3: -2ε² × a × a³ × (ζ'/a) × (∂ζ)(∂χ_conf) where χ_conf = -ζ'/(a k²)
         = -2ε² × a³ × ζ' × (∂ζ) × (-ζ'/(a k²))
         = +2ε² × a² × ζ' × (∂ζ) × ζ'/k²
  Term 4: (ε³/2) × a × a³ × ζ × [(∂ᵢ∂ⱼ)(-ζ'/(a k²))]²
         = (ε³/2) × a⁴ × ζ × (kᵢkⱼ/k²)² × (ζ'/(a k²))²
         = (ε³/2) × a² × ζ × (k·k')²/(k²k'²) × ζ' × ζ' / (k² k'²)
         ... actually (∂ᵢ∂ⱼχ)² for TWO chi fields at different k:
         = (ε³/2) × a² × ζ × ζ'_b ζ'_c × (kb·kc)²/(kb²kc²) / (a²)
         = (ε³/2) × ζ × ζ'_b ζ'_c × (kb·kc)²/(kb²kc²)

Wait, let me be more careful with Term 4. The two χ fields are at momenta kb and kc.
∂ᵢ∂ⱼχ_kb = (-kb_i kb_j / kb²) × (-ζ̇_kb/kb²) ... no:
χ_k = ∂⁻²ζ̇_k. In k-space: ∇²χ = ζ̇, so -k²χ_k = ζ̇_k → χ_k = -ζ̇_k/k²
∂ᵢ∂ⱼχ in k-space: ∂ᵢ∂ⱼ → -kᵢkⱼ (from two spatial derivatives)
So ∂ᵢ∂ⱼχ_kb = -kb_i kb_j × χ_kb = -kb_i kb_j × (-ζ̇_kb/kb²) = kb_i kb_j ζ̇_kb / kb²

(∂ᵢ∂ⱼχ)² for two fields at kb, kc:
= Σ_ij (kb_i kb_j ζ̇_kb / kb²)(kc_i kc_j ζ̇_kc / kc²)
= (kb·kc)² ζ̇_kb ζ̇_kc / (kb² kc²)

In conformal time: ζ̇ = ζ'/a
So: (∂ᵢ∂ⱼχ)² = (kb·kc)² (ζ'_kb/a)(ζ'_kc/a) / (kb² kc²)
              = (kb·kc)² ζ'_kb ζ'_kc / (a² kb² kc²)

Term 4 in conformal time:
= (ε³/2) × a × a³ × ζ_ka × (kb·kc)² ζ'_kb ζ'_kc / (a² kb² kc²)
= (ε³/2) × a² × ζ_ka × (kb·kc)² ζ'_kb ζ'_kc / (kb² kc²)

OK so ALL four terms have the SAME a-power: a².

Summary of conformal-time integrand (∫ dη × integrand):

Term 1: (ε²-ε³/2) × a² × ζ_a × ζ'_b × ζ'_c
Term 2: ε² × a² × ζ_a × (kb·kc) × ζ_b × ζ_c   [wait: (∂ζ)² involves spatial gradients]
Term 3: +2ε² × a² × ζ'_a × (kb·kc) × ζ_b × ζ'_c / kc²
Term 4: (ε³/2) × a² × ζ_a × (kb·kc)² × ζ'_b × ζ'_c / (kb² kc²)

Wait, Term 2 needs more care. The term is ε²a ζ(∂ζ)².
In k-space: (∂ζ)² at momenta kb, kc means ∂ᵢζ_kb ∂ᵢζ_kc = kb·kc × ζ_kb × ζ_kc
Conformal-time integrand: a × ε²a × ζ_ka × kb·kc × ζ_kb × ζ_kc = ε² a² × ζ_ka × (kb·kc) × ζ_kb ζ_kc

And Term 3: -2ε²a³ ζ̇(∂ζ)(∂χ)
ζ̇ = ζ'/a, ∂ζ at kb = ikb ζ_kb, ∂χ at kc = ikc χ_kc = ikc(-ζ̇_kc/kc²) = -ikc ζ'_kc/(a kc²)
(∂ζ)(∂χ) = kb·kc × ζ_kb × (-ζ'_kc/(a kc²))
Full term: -2ε² × a × a³ × (ζ'_ka/a) × kb·kc × ζ_kb × (-ζ'_kc/(a kc²))
= -2ε² × a³ × ζ'_ka × kb·kc × ζ_kb × (-ζ'_kc/(a kc²))
= +2ε² × a² × ζ'_ka × (kb·kc/kc²) × ζ_kb × ζ'_kc

So the conformal-time integrand for EACH term is:

  T1: (ε²-ε³/2) × a² × [ζ_a ζ'_b ζ'_c + perms]
  T2: ε²         × a² × [ζ_a (kb·kc) ζ_b ζ_c + perms]
  T3: +2ε²       × a² × [ζ'_a (kb·kc/kc²) ζ_b ζ'_c + ALL 6 perms]
  T4: (ε³/2)     × a² × [ζ_a (kb·kc)²/(kb²kc²) ζ'_b ζ'_c + perms]

ALL HAVE a² !!

In the variable x = kη for the short mode (k=1): a = (-η)^p = (-x)^p
For p=1: a = -x, a² = x²

So the x-power for ALL terms is x² (not x⁴ or x⁸ as in the old code!).

The old code had x⁴ for T1 and x⁸ for T3 because it was using DIFFERENT
definitions of the mode functions and χ. In particular:
- The old ghat had 1/x² (not 1/x³)
- The old χ had extra x⁴ factors

With Cai's correct mode functions (1/x³) and correct χ (-ζ'/ak² = ghat'/(x sqrt(6))),
all terms should have x² from a².

THIS IS THE FIX.
"""

from mpmath import (mp, mpf, mpc, quad, exp, sqrt, fabs,
                     re as mpre, im as mpim, j)

mp.dps = 50

# ═══════════════════════════════════════════════════════
# CORRECT Cai mode functions (e^{+jx} phase)
# ═══════════════════════════════════════════════════════
# Cai Eq. 24: X_k(η) = (1-ikη) e^{ikη} / η³
# In x = kη: ghat(x) = (1-ix) e^{ix} / x³

def ghat(x):
    return (1 - j*x) * exp(j*x) / x**3

def ghat_prime(x):
    """d/dx of ghat = e^{ix}(x² + 3ix - 3)/x⁴"""
    return exp(j*x) * (x**2 + 3*j*x - 3) / x**4


def compute_fnl_v3(r_val, xf_val, x0_val, eps_reg_val, dps=50, verbose=True):
    mp.dps = dps
    r = mpf(r_val)
    xf = mpf(xf_val)
    x0 = mpf(x0_val)
    eps_reg = mpf(eps_reg_val)
    eps = mpf('1.5')

    s6 = sqrt(mpf(6))
    s6r = sqrt(6*r)

    # Mode functions (Cai convention)
    def zk(x): return ghat(x) / s6
    def zk1(x): return ghat(r*x) / s6r
    def zkp(x): return ghat_prime(x) / s6           # dζ_k/dx
    def zk1p(x): return sqrt(r) * ghat_prime(r*x) / s6  # dζ_{k1}/dx

    # Momentum dot products (exact)
    k1 = r
    k2 = mpf(1)
    k3 = mpf(1)
    k2_dot_k3 = (k1**2 - k2**2 - k3**2) / 2  # ≈ -1 for r<<1
    k1_dot_k2 = (k3**2 - k1**2 - k2**2) / 2  # ≈ 0 for r<<1
    k1_dot_k3 = (k2**2 - k1**2 - k3**2) / 2  # ≈ 0 for r<<1

    # Coefficients at ε = 3/2
    c1 = eps**2 - eps**3/2    # = 9/16
    c2 = eps**2               # = 9/4
    c3_coeff = 2 * eps**2     # = 9/2 (note: +2ε² because the double-negative resolved)
    c4 = eps**3 / 2           # = 27/16

    def combined_integrand(x):
        """
        All 4 vertex terms in conformal time, each with a² = x² prefactor.

        p = 1 for dust, so a(η) = (-η)^1 and in x = kη: a = -x/k = -x (for k=1).
        a² = x².
        """
        d = exp(eps_reg * x)

        # Mode function values
        u1 = zk1(x)   # ζ_{k1}
        u2 = zk(x)    # ζ_{k2} = ζ_{k3} (k2=k3=1)
        u3 = zk(x)
        du1 = zk1p(x) # ζ'_{k1}
        du2 = zkp(x)   # ζ'_{k2}
        du3 = zkp(x)   # ζ'_{k3}

        a_sq = x**2  # a² = x² for p=1

        # ═══════ Term 1: (ε²-ε³/2) a² ζ_a ζ'_b ζ'_c ═══════
        # 3 permutations of which momentum is undifferentiated
        t1 = c1 * a_sq * (
            u1 * du2 * du3 +    # a=k1, b=k2, c=k3
            u2 * du1 * du3 +    # a=k2, b=k1, c=k3
            u3 * du1 * du2      # a=k3, b=k1, c=k2
        )

        # ═══════ Term 2: ε² a² ζ_a (kb·kc) ζ_b ζ_c ═══════
        # 3 permutations
        t2 = c2 * a_sq * (
            u1 * k2_dot_k3 * u2 * u3 +   # a=k1
            u2 * k1_dot_k3 * u1 * u3 +   # a=k2
            u3 * k1_dot_k2 * u1 * u2     # a=k3
        )

        # ═══════ Term 3: +2ε² a² ζ'_a (kb·kc/kc²) ζ_b ζ'_c ═══════
        # 6 permutations: (a=ζ̇, b=∂ζ, c=∂χ) for all assignments
        # Each gives: ζ'_a × (kb·kc) × ζ_b × ζ'_c / kc²
        t3 = c3_coeff * a_sq * (
            # a=k1 (ζ̇), b=k2 (∂ζ), c=k3 (∂χ):
            du1 * k2_dot_k3 * u2 * du3 / k3**2 +
            # a=k1, b=k3, c=k2:
            du1 * k3_dot_k2 * u3 * du2 / k2**2 +
            # a=k2, b=k1, c=k3:
            du2 * k1_dot_k3 * u1 * du3 / k3**2 +
            # a=k2, b=k3, c=k1:
            du2 * k3_dot_k1 * u3 * du1 / k1**2 +
            # a=k3, b=k1, c=k2:
            du3 * k1_dot_k2 * u1 * du2 / k2**2 +
            # a=k3, b=k2, c=k1:
            du3 * k2_dot_k1 * u2 * du1 / k1**2
        )

        # ═══════ Term 4: (ε³/2) a² ζ_a (kb·kc)²/(kb²kc²) ζ'_b ζ'_c ═══════
        # 3 permutations
        t4 = c4 * a_sq * (
            u1 * k2_dot_k3**2 / (k2**2 * k3**2) * du2 * du3 +
            u2 * k1_dot_k3**2 / (k1**2 * k3**2) * du1 * du3 +
            u3 * k1_dot_k2**2 / (k1**2 * k2**2) * du1 * du2
        )

        return (t1 + t2 + t3 + t4) * d

    # Need symmetric dot products
    k3_dot_k2 = k2_dot_k3
    k3_dot_k1 = k1_dot_k3
    k2_dot_k1 = k1_dot_k2

    # Integrate
    if verbose:
        print("Integrating (dps=%d, xf=%s, r=%s, x0=%s)..." % (dps, xf_val, r_val, x0_val))
        for xt in [mpf(-100), mpf(-10), mpf(-1), mpf('-0.1')]:
            val = combined_integrand(xt)
            print("  F(%8.1f) = %+.6e + %+.6ej" % (float(xt), float(mpre(val)), float(mpim(val))))

    I_re = quad(lambda x: mpre(combined_integrand(x)), [x0, xf],
                method='tanh-sinh', maxdegree=8)
    I_im = quad(lambda x: mpim(combined_integrand(x)), [x0, xf],
                method='tanh-sinh', maxdegree=8)
    I = mpc(I_re, I_im)

    if verbose:
        print("  I = %+.10e + %+.10ej" % (float(mpre(I)), float(mpim(I))))

    # External legs at xf
    ext = zk1(xf).conjugate() * (zk(xf).conjugate())**2
    PP = fabs(zk1(xf))**2 * fabs(zk(xf))**2

    # Bispectrum: B = -2 Im[ext × I]
    product = ext * I
    B = -2 * mpim(product)
    fnl_intr = mpf(5)/mpf(12) * B / PP
    fnl_redef = mpf(5)/mpf(4)  # 5ε/6 = 5/4 at ε=3/2
    fnl_total = fnl_intr + fnl_redef

    if verbose:
        print("  B = %+.6e" % float(B))
        print("  f_NL (intrinsic) = %+.10f" % float(fnl_intr))
        print("  f_NL (field redef) = +1.2500000000")
        print("  f_NL (TOTAL)       = %+.10f" % float(fnl_total))
        print("  Targets: -35/8 = -4.375, -35/16 = -2.1875")
        diff8 = abs(float(fnl_total) + 4.375)
        diff16 = abs(float(fnl_total) + 2.1875)
        if diff8 < 1.0:
            print("  >>> CLOSE TO -35/8 (diff = %.3f)" % diff8)
        elif diff16 < 1.0:
            print("  >>> CLOSE TO -35/16 (diff = %.3f)" % diff16)
        else:
            print("  >>> diff from -35/8: %.3f, from -35/16: %.3f" % (diff8, diff16))

    return float(fnl_intr), float(fnl_total)


if __name__ == "__main__":
    print("=" * 65)
    print("CORRECTED v3: EXACT CONFORMAL-TIME DERIVATION")
    print("All terms have a² = x² prefactor (derived from scratch)")
    print("=" * 65)

    fi, ft = compute_fnl_v3(1e-3, -0.01, -500, 1e-4, dps=50, verbose=True)

    print("\n--- xf convergence ---")
    for xf in [-0.1, -0.05, -0.01, -0.005, -0.001]:
        _, ft2 = compute_fnl_v3(1e-3, xf, -500, 1e-4, dps=50, verbose=False)
        print("  xf=%8.4f  f_NL=%+.8f" % (xf, ft2))

    print("\n--- Squeeze ratio ---")
    for rv in [0.01, 0.001, 0.0001]:
        _, ft2 = compute_fnl_v3(rv, -0.01, -500, 1e-4, dps=50, verbose=False)
        print("  r=%8.5f  f_NL=%+.8f" % (rv, ft2))
