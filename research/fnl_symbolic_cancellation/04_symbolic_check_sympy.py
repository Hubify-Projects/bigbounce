#!/usr/bin/env python3
"""
Symbolic + high-precision numerical verification of the f_NL cancellation structure.

Part 1: SymPy verification that Im[ext × I_superhorizon] = 0 (phase structure proof)
Part 2: mpmath high-precision computation of the full f_NL with all 6 terms

The key insight: the k₁⁻² divergence from Term 6 is in Re[ext×I], not Im[ext×I].
The physical bispectrum B = 2·Im[ext×I] is finite and comes from horizon crossing.
"""

import sympy as sp
from sympy import I, sqrt, re, im, simplify, symbols, conjugate, oo, pi

print("=" * 70)
print("PART 1: SYMBOLIC PHASE STRUCTURE VERIFICATION")
print("=" * 70)

# Define symbolic variables
eta = symbols('eta', real=True, negative=True)
k, k1 = symbols('k k1', positive=True)
A = symbols('A', positive=True)  # normalization constant

# Superhorizon mode functions (|kη| → 0, η < 0)
# g_k(η) → -i/(√(2k³)·η³)  [exact in superhorizon limit]
# Since η < 0: η³ < 0, so -i/η³ = -i/(neg) = pos·i

# For symbolic clarity, define as explicit complex expressions:
g_k_super = -I / (sqrt(2*k**3) * eta**3)
g_k_prime_super = 3*I / (sqrt(2*k**3) * eta**4)

g_k1_super = -I / (sqrt(2*k1**3) * eta**3)
g_k1_prime_super = 3*I / (sqrt(2*k1**3) * eta**4)

# External legs at eta_f (superhorizon):
eta_f = symbols('eta_f', real=True, negative=True)
ext_k1 = conjugate(g_k1_super.subs(eta, eta_f))
ext_k = conjugate(g_k_super.subs(eta, eta_f))
ext = ext_k1 * ext_k**2

print("\n--- Mode function phases ---")
print(f"g_k(η) superhorizon = {g_k_super}")
print(f"g*_k(η_f) = {ext_k}")
print(f"g*_k(η_f)² = {simplify(ext_k**2)}")
print(f"ext = g*_{k1} · g*_k² = {simplify(ext)}")

# Check: is ext purely imaginary?
ext_simplified = simplify(ext)
re_ext = simplify(re(ext_simplified))
im_ext = simplify(im(ext_simplified))
print(f"\nRe[ext] = {re_ext}")
print(f"Im[ext] = {im_ext}")
if re_ext == 0:
    print("✓ ext is purely imaginary on superhorizon")
else:
    print("✗ ext has real part (unexpected)")

# Now check the integrand for Term 1:
# η⁴ · g_{k₁}(η') · [g'_k(η')]²
print("\n--- Term 1 integrand phase ---")
T1_integrand = eta**4 * g_k1_super * g_k_prime_super**2
T1_simplified = simplify(T1_integrand)
re_T1 = simplify(re(T1_simplified))
im_T1 = simplify(im(T1_simplified))
print(f"T1 integrand = {T1_simplified}")
print(f"Re[T1] = {re_T1}")
print(f"Im[T1] = {im_T1}")

# Product ext × T1_integrand
product_T1 = simplify(ext_simplified * T1_simplified)
re_product = simplify(re(product_T1))
im_product = simplify(im(product_T1))
print(f"\next × T1_integrand = {product_T1}")
print(f"Re[ext × T1] = {re_product}")
print(f"Im[ext × T1] = {im_product}")
if im_product == 0:
    print("✓ PROVEN: Im[ext × T1_superhorizon] = 0")

# Term 6 (the problematic one):
# η⁸ · ζ_k · ζ'_{k₁} · ζ'_k / k₁²
# Using g functions (without 1/A factors, which cancel in f_NL):
print("\n--- Term 6 integrand phase ---")
T6_integrand = eta**8 * g_k_super * g_k1_prime_super * g_k_prime_super / k1**2
T6_simplified = simplify(T6_integrand)
re_T6 = simplify(re(T6_simplified))
im_T6 = simplify(im(T6_simplified))
print(f"T6 integrand = {T6_simplified}")
print(f"Re[T6] = {re_T6}")
print(f"Im[T6] = {im_T6}")

product_T6 = simplify(ext_simplified * T6_simplified)
re_product_T6 = simplify(re(product_T6))
im_product_T6 = simplify(im(product_T6))
print(f"\next × T6_integrand = {product_T6}")
print(f"Re[ext × T6] = {re_product_T6}")
print(f"Im[ext × T6] = {im_product_T6}")
if im_product_T6 == 0:
    print("✓ PROVEN: Im[ext × T6_superhorizon] = 0")
    print("  The k₁⁻² divergence from T6 is in Re only — does NOT affect B = 2·Im[...]")


# ======================================================================
print("\n" + "=" * 70)
print("PART 2: HIGH-PRECISION NUMERICAL COMPUTATION")
print("=" * 70)

try:
    from mpmath import mp, mpf, mpc, quad, exp, sqrt as mpsqrt, im as mpim, re as mpre, fabs, pi as mppi, inf

    mp.dps = 40  # 40 decimal digits

    def ghat_mp(x):
        """Dimensionless mode function with mpmath precision."""
        return exp(-1j * x) * (1 - 1j / x) / x**2

    def ghat_prime_mp(x):
        """Derivative with mpmath precision."""
        return exp(-1j * x) * (-1j - mpf(3) / x + 3j / x**2) / x**2

    def compute_fnl_mpmath(r_val=1e-3, xf_val=-0.5, x_early=-200, verbose=True):
        """
        Compute f_NL with mpmath arbitrary precision.

        Key change from float64 version: use xf = -0.5 (near horizon crossing)
        to avoid the deep superhorizon regime where precision is lost.
        """
        r = mpf(r_val)
        xf = mpf(xf_val)
        x0 = mpf(x_early)
        eps_reg = mpf('1e-4')

        # Mode functions at eta_f (x = k*eta_f = xf since k=1)
        gk_f = ghat_mp(xf)
        gk1_f = ghat_mp(r * xf)

        # Power spectra (dimensionless)
        Pk1 = fabs(ghat_mp(r * xf))**2 / (6 * r)
        Pk = fabs(ghat_mp(xf))**2 / mpf(6)
        PP = Pk1 * Pk

        # External legs
        ext_val = gk1_f.conjugate() * (gk_f.conjugate())**2

        # Damping function
        def damp(x):
            return exp(eps_reg * x)

        # ============================================================
        # TERM 1: (9/4) a² ζ ζ'²
        # Perm 1 (dominant): k₁ undiff, k diff
        # integrand = (9/4) * x⁴/k⁴ * ζ_{k₁}(x/k) * [ζ'_k(x/k)]² * dx/k
        # In units k=1: (9/4) * x⁴ * g_{k₁}(rx)/√(6r) * [g'_k(x)/√6]² * damping
        # Wait, I need to use the ζ mode functions, not g.
        # ζ_k = g_k / (√3 · M_Pl) [in our units with a₀=M_Pl=1: ζ_k = g_k/√3... actually
        # from the derivation: ζ_k = ghat(kη)/(√(6k)). With k=1: ζ_k = ghat(η)/√6]
        # ============================================================

        coeff_T1 = mpf(9) / mpf(4)

        def zeta_k1(x):
            return ghat_mp(r * x) / mpsqrt(6 * r)

        def zeta_k(x):
            return ghat_mp(x) / mpsqrt(mpf(6))

        def zeta_k1_prime(x):
            return mpsqrt(r) * ghat_prime_mp(r * x) / mpsqrt(mpf(6))

        def zeta_k_prime(x):
            return ghat_prime_mp(x) / mpsqrt(mpf(6))

        # chi functions
        def chi_k1(x):
            return mpf('-1.5') * x**4 * zeta_k1_prime(x) / r**2

        def chi_k(x):
            return mpf('-1.5') * x**4 * zeta_k_prime(x)

        # --- Term 1 (all 3 perms) ---
        def T1_integrand(x):
            d = damp(x)
            p1 = coeff_T1 * x**4 * zeta_k1(x) * zeta_k_prime(x)**2 * d
            p23 = coeff_T1 * x**4 * zeta_k(x) * zeta_k1_prime(x) * zeta_k_prime(x) * d
            return p1 + 2 * p23

        if verbose:
            print("\nIntegrating Term 1...")
        I_T1 = quad(lambda x: [mpre(T1_integrand(x)), mpim(T1_integrand(x))],
                     [x0, xf], method='tanh-sinh', error=True, maxdegree=8)
        I_T1_val = mpc(I_T1[0][0], I_T1[0][1])
        if verbose:
            print(f"  I_T1 = {I_T1_val}")

        # --- Term 2: (9/4) a² ζ (∂ζ)² ---
        # Squeezed: -k₂·k₃ ≈ k² = 1 for the dominant perm
        coeff_T2 = mpf(9) / mpf(4)
        def T2_integrand(x):
            d = damp(x)
            return coeff_T2 * mpf(1) * x**4 * zeta_k1(x) * zeta_k(x) * zeta_k(x) * d

        if verbose:
            print("Integrating Term 2...")
        I_T2 = quad(lambda x: [mpre(T2_integrand(x)), mpim(T2_integrand(x))],
                     [x0, xf], method='tanh-sinh', error=True, maxdegree=8)
        I_T2_val = mpc(I_T2[0][0], I_T2[0][1])

        # --- Term 3: after χ-sub, dominant squeezed perms ---
        # Perm with χ_{k₁}: (9/4)η⁸ ζ'_k ζ_k ζ'_{k₁} (after k₁²/k₁² cancellation)
        # Plus perm with ka=k₁: -(9/2)η⁸ ζ'_{k₁} ζ_k ζ'_k (with χ_k)
        def T3_integrand(x):
            d = damp(x)
            # Perm with χ_{k₁} (×2 for both assignments): already cancelled k₁² factor
            p_chi_k1 = mpf(9) / mpf(4) * x**8 * zeta_k_prime(x) * zeta_k(x) * zeta_k1_prime(x) * d
            # Perm with ka=k₁, χ_k: -(9/2)·(k₂·k₃/k₃²)·η⁸·ζ'_{k₁}·ζ_k·ζ'_k
            # k₂·k₃ = -k² = -1, k₃² = k² = 1
            # so factor = -(9/2)·(-1)/1 = 9/2
            p_chi_k = mpf(9) / mpf(2) * x**8 * zeta_k1_prime(x) * zeta_k(x) * zeta_k_prime(x) * d
            return 2 * p_chi_k1 + p_chi_k

        if verbose:
            print("Integrating Term 3...")
        I_T3 = quad(lambda x: [mpre(T3_integrand(x)), mpim(T3_integrand(x))],
                     [x0, xf], method='tanh-sinh', error=True, maxdegree=8)
        I_T3_val = mpc(I_T3[0][0], I_T3[0][1])

        # --- Term 4: (9/16) a² ζ² ζ' ---
        coeff_T4 = mpf(9) / mpf(16)
        def T4_integrand(x):
            d = damp(x)
            pa = coeff_T4 * x**4 * zeta_k(x)**2 * zeta_k1_prime(x) * d
            pb = coeff_T4 * x**4 * zeta_k1(x) * zeta_k(x) * zeta_k_prime(x) * d
            return pa + 2 * pb

        if verbose:
            print("Integrating Term 4...")
        I_T4 = quad(lambda x: [mpre(T4_integrand(x)), mpim(T4_integrand(x))],
                     [x0, xf], method='tanh-sinh', error=True, maxdegree=8)
        I_T4_val = mpc(I_T4[0][0], I_T4[0][1])

        # --- Term 5+6 combined (using explicit chi) ---
        # T5: (27/16)·k_a²·(k_b·k_c)/(k_b²k_c²)·η⁸·ζ·ζ'·ζ'
        # T6: -(81/128)·k_a²/(k_b²k_c²)·η⁸·ζ·ζ'·ζ'
        # For perm (b): ka=k, kb=k₁, kc=k
        # T5_b: (27/16)·1·(k₁·k)/(k₁²·1)·η⁸·ζ_k·ζ'_{k₁}·ζ'_k
        #      = (27/16)·(-k₁²/2)/k₁²·η⁸·... = -(27/32)·η⁸·...
        # T6_b: -(81/128)·1/k₁²·η⁸·ζ_k·ζ'_{k₁}·ζ'_k
        #
        # For perm (a): ka=k₁, kb=k, kc=k → suppressed by k₁²
        #
        # I use the explicit chi functions for T5+T6 to capture all contributions:
        def T56_integrand(x):
            d = damp(x)
            c1 = chi_k1(x)
            ck = chi_k(x)

            # T5: (3/4)·(-k_a²)·(-(k_b·k_c))·ζ_{ka}·χ_{kb}·χ_{kc}
            # = (3/4)·k_a²·(k_b·k_c)·ζ_{ka}·χ_{kb}·χ_{kc}
            # Perm (b): ka=k, kb=k₁, kc=k:
            #   (3/4)·1·(k₁·k)·ζ_k·χ_{k₁}·χ_k = (3/4)·(-k₁²/2)·ζ_k·c1·ck
            T5_b = mpf(3)/mpf(4) * (-r**2/2) * zeta_k(x) * c1 * ck * d
            # Perm (c): ka=k, kb=k, kc=k₁:
            #   (3/4)·1·(k·k₁)·ζ_k·χ_k·χ_{k₁} = same as T5_b
            T5_c = T5_b  # by k₂↔k₃ symmetry

            # T6: (9/32)·(-k_a²)·ζ_{ka}·χ_{kb}·χ_{kc}
            # Perm (b): (9/32)·(-1)·ζ_k·χ_{k₁}·χ_k
            T6_b = mpf(9)/mpf(32) * (-mpf(1)) * zeta_k(x) * c1 * ck * d
            T6_c = T6_b

            return T5_b + T5_c + T6_b + T6_c

        if verbose:
            print("Integrating Terms 5+6...")
        I_T56 = quad(lambda x: [mpre(T56_integrand(x)), mpim(T56_integrand(x))],
                      [x0, xf], method='tanh-sinh', error=True, maxdegree=8)
        I_T56_val = mpc(I_T56[0][0], I_T56[0][1])

        # --- Total ---
        I_total = I_T1_val + I_T2_val + I_T3_val + I_T4_val + I_T56_val
        B_total = -2 * mpim(ext_val * I_total)

        # Individual contributions
        B_T1 = -2 * mpim(ext_val * I_T1_val)
        B_T2 = -2 * mpim(ext_val * I_T2_val)
        B_T3 = -2 * mpim(ext_val * I_T3_val)
        B_T4 = -2 * mpim(ext_val * I_T4_val)
        B_T56 = -2 * mpim(ext_val * I_T56_val)

        fnl_T1 = mpf(5)/mpf(12) * B_T1 / PP
        fnl_T2 = mpf(5)/mpf(12) * B_T2 / PP
        fnl_T3 = mpf(5)/mpf(12) * B_T3 / PP
        fnl_T4 = mpf(5)/mpf(12) * B_T4 / PP
        fnl_T56 = mpf(5)/mpf(12) * B_T56 / PP

        fnl_intrinsic = mpf(5)/mpf(12) * B_total / PP
        fnl_total = fnl_intrinsic + mpf(5)/mpf(4)

        if verbose:
            print(f"\n{'='*60}")
            print(f"f_NL DECOMPOSITION (mpmath, {mp.dps} digits)")
            print(f"xf = {xf_val}, r = {r_val}")
            print(f"{'='*60}")
            print(f"  T1 (ε²a²ζζ'²):    {float(fnl_T1):+.8f}")
            print(f"  T2 (ε²a²ζ(∂ζ)²):  {float(fnl_T2):+.8f}")
            print(f"  T3 (χ-sub):        {float(fnl_T3):+.8f}")
            print(f"  T4 (a²ζ²ζ'):       {float(fnl_T4):+.8f}")
            print(f"  T5+T6 (χ² terms):  {float(fnl_T56):+.8f}")
            print(f"  {'─'*50}")
            print(f"  Intrinsic:         {float(fnl_intrinsic):+.8f}")
            print(f"  Field redef:       +1.25000000")
            print(f"  TOTAL:             {float(fnl_total):+.8f}")
            print(f"{'='*60}")
            print(f"  Targets: Cai=-4.375, L-B=-2.1875")

        return float(fnl_intrinsic), float(fnl_total)

    # Main computation
    print("\n--- Main computation ---")
    fi, ft = compute_fnl_mpmath(r_val=1e-3, xf_val=-0.5, x_early=-200, verbose=True)

    # Convergence tests
    print(f"\n{'='*60}")
    print("CONVERGENCE TESTS")
    print(f"{'='*60}")

    print("\n--- xf dependence ---")
    for xf in [-1.0, -0.5, -0.3, -0.1]:
        _, ft = compute_fnl_mpmath(r_val=1e-3, xf_val=xf, x_early=-200, verbose=False)
        print(f"  xf={xf:6.2f}  f_NL={ft:+.6f}")

    print("\n--- Squeeze ratio ---")
    for r in [0.01, 0.001, 0.0001]:
        _, ft = compute_fnl_mpmath(r_val=r, xf_val=-0.5, x_early=-200, verbose=False)
        print(f"  r={r:.5f}  f_NL={ft:+.6f}")

except ImportError:
    print("\nmpmath not available. Install with: pip install mpmath")
    print("Skipping high-precision computation.")
except Exception as e:
    print(f"\nError in mpmath computation: {e}")
    import traceback
    traceback.print_exc()

print("\nDone.")
