#!/usr/bin/env python3
"""
Numerical reproduction of Cai et al. (0903.0631) f_NL = -35/8.

Uses Cai's EXACT mode functions and cubic Lagrangian directly.
Computes the shape function A_T as the ratio B·Πk³/Pζ²,
where all growing-mode factors cancel.

Key conventions (from Cai):
  X_k(η) = (1 - ikη)e^{+ikη}/η³          (Eq. 24, with η̃_B = 0)
  X'_k(η) = (k²η² + 3ikη - 3)e^{ikη}/η⁴  (derivative)
  u_k = A·i·X_k/√(2k³)                    (Eq. 23)
  χ = ∂⁻²ζ̇                                (Cai's convention)
  ε = 3/2

The bispectrum is computed via the in-in formula evaluated at
η_B (bounce time). The shape function A_T is η_B-independent.
"""
from mpmath import mp, mpf, mpc, quad, exp, sqrt, fabs, re as mpre, im as mpim, pi, j
import sys

mp.dps = 40

def Xk(k, eta):
    """Cai's rescaled mode function X_k(η) = (1-ikη)e^{ikη}/η³"""
    return (1 - j*k*eta) * exp(j*k*eta) / eta**3

def Xk_prime(k, eta):
    """d/dη of X_k = (k²η² + 3ikη - 3)e^{ikη}/η⁴"""
    return (k**2 * eta**2 + 3*j*k*eta - 3) * exp(j*k*eta) / eta**4

def compute_AT_and_BNL(k1, k2, k3, eta_B=-0.001, eta_start=-500, eps_reg=1e-4, verbose=True):
    """
    Compute A_T and |B|_NL for the matter bounce using Cai's conventions.

    Strategy: compute A_T = <ζ³>'·Πk³/Pζ² as a ratio where η_B dependence cancels.

    A_T = (|A|²/2) × 2Re[G_ext · i · I_total] / |X₁|²|X₂|²|X₃|²

    where the |A|² factors cancel between numerator (from <ζ³>') and denominator (from Pζ²).
    """
    k1, k2, k3 = mpf(k1), mpf(k2), mpf(k3)
    eta_B = mpf(eta_B)
    eta_0 = mpf(eta_start)
    eps = mpf(eps_reg)

    # External legs at η_B
    X1B = Xk(k1, eta_B)
    X2B = Xk(k2, eta_B)
    X3B = Xk(k3, eta_B)
    G_ext = X1B.conjugate() * X2B.conjugate() * X3B.conjugate()
    G_den = fabs(X1B)**2 * fabs(X2B)**2 * fabs(X3B)**2

    # Power spectrum (scale-invariant part)
    # Pζ = |X_k(η_B)|²/2 (with A=1)
    # Use geometric mean for generality
    Pk1 = fabs(X1B)**2 / 2
    Pk2 = fabs(X2B)**2 / 2
    Pk3 = fabs(X3B)**2 / 2

    # ε = 3/2 for matter contraction
    epsilon = mpf('1.5')
    # Vertex coefficients (cosmic → conformal time, Cai Eq. 15)
    coeff_zzdot2 = epsilon**2 - epsilon**3/2  # = 9/4 - 27/16 = 9/16
    coeff_zdot_dz_dchi = -2 * epsilon**2       # = -9/2
    coeff_z_didj_chi2 = epsilon**3 / 2         # = 27/16

    # a²(η) = a₀²η⁴. Set a₀ = 1.
    def a2(eta): return eta**4

    # Damping for convergence at early times
    def damp(eta): return exp(eps * eta)

    # ====================================================================
    # VERTEX 1: (ε²-ε³/2) a² ζ ζ̇²
    # In conformal time: coeff · a² · X_{ka} · X'_{kb} · X'_{kc}
    # Sum over 6 permutations (3 choices × 2 for identical ζ̇'s)
    # ====================================================================
    def V1_integrand(eta):
        d = damp(eta)
        X1 = Xk(k1, eta); X2 = Xk(k2, eta); X3 = Xk(k3, eta)
        X1p = Xk_prime(k1, eta); X2p = Xk_prime(k2, eta); X3p = Xk_prime(k3, eta)
        a2v = a2(eta)

        # 6 permutations: X_a X'_b X'_c for all orderings
        s = (X1*X2p*X3p + X1*X3p*X2p +   # a=1, (b,c)=(2,3) and (3,2)
             X2*X1p*X3p + X2*X3p*X1p +   # a=2
             X3*X1p*X2p + X3*X2p*X1p)    # a=3
        return coeff_zzdot2 * a2v * s * d

    # ====================================================================
    # VERTEX 2: -2ε² a² ζ̇ (∂ζ)(∂χ)
    # χ = ∂⁻²ζ̇ → in Fourier: χ_k = -ζ̇_k/k² = -(X'_k/a)/k² (conformal)
    # ∂ᵢζ → ik_i ζ, ∂ᵢχ → ik_i χ
    # (∂ζ)(∂χ) → -(k_b·k_c) ζ_{kb} χ_{kc}
    #
    # After χ sub: coeff × a² × ζ̇_{ka} × (k_b·k_c/k_c²) × ζ_{kb} × ζ̇_{kc}
    # In conformal: X'_a/a × (k_b·k_c/k_c²) × X_b × X'_c/a
    # Combined with a² and the extra a from dt: coeff × (k_b·k_c/k_c²) × X'_a × X_b × X'_c
    #
    # NOTE: (k_b·k_c) for momenta summing to zero:
    # k_b·k_c = (k_a² - k_b² - k_c²)/2
    # ====================================================================
    def kdot(ka, kb, kc):
        """Dot product k_b·k_c = (k_a²-k_b²-k_c²)/2"""
        return (ka**2 - kb**2 - kc**2) / 2

    def V2_integrand(eta):
        d = damp(eta)
        a2v = a2(eta)  # FIX: was missing a²(η) factor
        X1 = Xk(k1, eta); X2 = Xk(k2, eta); X3 = Xk(k3, eta)
        X1p = Xk_prime(k1, eta); X2p = Xk_prime(k2, eta); X3p = Xk_prime(k3, eta)

        # 6 permutations: ζ̇_a (∂ζ_b)(∂χ_c)
        # Each gives: coeff × a² × (kb·kc/kc²) × X'_a × X_b × X'_c
        s = mpf(0)
        ks = [(k1,k2,k3), (k1,k3,k2), (k2,k1,k3), (k2,k3,k1), (k3,k1,k2), (k3,k2,k1)]
        Xs = [X1, X2, X3]
        Xps = [X1p, X2p, X3p]
        idx = {k1:0, k2:1, k3:2}

        for ka, kb, kc in ks:
            ia, ib, ic = idx[ka], idx[kb], idx[kc]
            dot_bc = kdot(ka, kb, kc)
            s += (dot_bc / kc**2) * Xps[ia] * Xs[ib] * Xps[ic]

        return coeff_zdot_dz_dchi * a2v * s * d

    # ====================================================================
    # VERTEX 3: (ε³/2) a³ ζ (∂ᵢ∂ⱼχ)²
    # (∂ᵢ∂ⱼχ)² = Σᵢⱼ (∂ᵢ∂ⱼχ)(∂ᵢ∂ⱼχ)
    # In Fourier: (kb_i kb_j/kb²)(kc_i kc_j/kc²) χ_{kb} χ_{kc}
    #           = (kb·kc)²/(kb²kc²) × χ_b χ_c
    # χ_k = -ζ̇_k/k² = -(X'_k/a)/k²
    # Combined: (kb·kc)²/(kb²kc²) × X'_b/(a·kb²) × X'_c/(a·kc²)
    #         = (kb·kc)²/(kb⁴kc⁴) × X'_b × X'_c / a²
    #
    # With vertex coeff × a³ × ζ_a × (...) × dt = coeff × a⁴ × X_a × (...)/a² × dη
    # = coeff × a² × X_a × (kb·kc)²/(kb⁴kc⁴) × X'_b × X'_c × dη
    # Wait: a³ × dt = a³ × a dη = a⁴ dη. And 1/a² from the two χ's.
    # Net: a² × X_a × (kb·kc)²/(kb⁴kc⁴) × X'_b × X'_c
    # ====================================================================
    def V3_integrand(eta):
        d = damp(eta)
        X1 = Xk(k1, eta); X2 = Xk(k2, eta); X3 = Xk(k3, eta)
        X1p = Xk_prime(k1, eta); X2p = Xk_prime(k2, eta); X3p = Xk_prime(k3, eta)
        a2v = a2(eta)

        # 3 permutations: ζ_a × (∂ᵢ∂ⱼχ_b)(∂ᵢ∂ⱼχ_c)
        # (χ pair is symmetric, so 3 not 6)
        s = mpf(0)
        triples = [(k1,k2,k3,X1,X2p,X3p), (k2,k1,k3,X2,X1p,X3p), (k3,k1,k2,X3,X1p,X2p)]
        for ka,kb,kc,Xa,Xpb,Xpc in triples:
            dot_bc = kdot(ka, kb, kc)
            factor = dot_bc**2 / (kb**4 * kc**4)
            s += factor * Xa * Xpb * Xpc
        s *= 2  # Factor 2 for the symmetric χ pair

        return coeff_z_didj_chi2 * a2v * s * d

    # ====================================================================
    # INTEGRATE
    # ====================================================================
    if verbose:
        print(f"Computing A_T for k=({float(k1):.4f},{float(k2):.4f},{float(k3):.4f}), etaB={float(eta_B)}")

    def integrate_complex(f, a, b):
        Ir = quad(lambda x: mpre(f(x)), [a, b], method='tanh-sinh', maxdegree=6)
        Ii = quad(lambda x: mpim(f(x)), [a, b], method='tanh-sinh', maxdegree=6)
        return mpc(Ir, Ii)

    if verbose: print("  V1 (ζζ̇²)...", end=" ", flush=True)
    I1 = integrate_complex(V1_integrand, eta_0, eta_B)
    if verbose: print("done")

    if verbose: print("  V2 (ζ̇∂ζ∂χ)...", end=" ", flush=True)
    I2 = integrate_complex(V2_integrand, eta_0, eta_B)
    if verbose: print("done")

    if verbose: print("  V3 (ζ(∂ᵢ∂ⱼχ)²)...", end=" ", flush=True)
    I3 = integrate_complex(V3_integrand, eta_0, eta_B)
    if verbose: print("done")

    I_vertex_total = I1 + I2 + I3

    # ====================================================================
    # COMPUTE A_T (from vertex contributions only, field redef added later)
    #
    # A_T_vertex = η_B^12 × 2Re[G_ext × i × I_total]
    # (the η_B^12 comes from Πk³/Pζ² normalization)
    #
    # More precisely: A_T = (1/(8·Pζ²)) × |A|^6 × 2Re[G_ext·i·I]/Πk³ × Πk³
    # With Pζ = |A|²|X|²/2, A=1:
    # A_T = (1/(8·|X|⁴/4)) × 2Re[G_ext·i·I] = 1/(2|X|⁴) × 2Re[...]
    # = Re[G_ext·i·I] / |X|⁴
    # But |X|⁴ ≠ G_den = |X₁|²|X₂|²|X₃|² (which is |X|⁶)
    # ====================================================================

    # Actually, let me just compute A_T = B_primed × Πk³ / Pζ²
    # where B_primed = |A|⁶/(8Πk³) × 2Re[G_ext × i × I_total]
    # and Pζ² = |A|⁴ × |X_ref|⁴ / 4
    # (using geometric mean |X_ref|² = (|X₁||X₂||X₃|)^{2/3} ← but Pζ should be k-independent)
    # For scale-invariant: |X_k|² ≈ same for all k at η_B.
    # Use Pζ = |X_{k2}|²/2 (reference scale k2)

    Pz = fabs(X2B)**2 / 2  # Pζ at reference scale
    Pz2 = Pz**2
    Pk3_prod = k1**3 * k2**3 * k3**3

    # B' = (1/(8·Pk3_prod)) × 2Re[G_ext × i × I_vertex]
    B_vertex = 2 * mpre(G_ext * j * I_vertex_total) / (8 * Pk3_prod)

    A_T_vertex = B_vertex * Pk3_prod / Pz2

    # Sum of k³
    sk3 = k1**3 + k2**3 + k3**3

    BNL_vertex = mpf(10)/mpf(3) * A_T_vertex / sk3

    # ====================================================================
    # FIELD REDEFINITION (Eq. 28)
    # This is a CONTACT term (no time integral).
    # We verified algebraically that the total AT (including Ared)
    # reproduces -35/8 in the squeezed limit.
    #
    # For now, compute vertex contribution only and compare with Cai's
    # individual vertex results (Eqs. 31-33).
    # ====================================================================

    if verbose:
        print(f"\n  === VERTEX CONTRIBUTIONS (without field redef) ===")
        print(f"  I1(ζζ̇²)      = {float(mpre(I1)):+.6e} + {float(mpim(I1)):+.6e}j")
        print(f"  I2(ζ̇∂ζ∂χ)    = {float(mpre(I2)):+.6e} + {float(mpim(I2)):+.6e}j")
        print(f"  I3(ζ(∂∂χ)²)  = {float(mpre(I3)):+.6e} + {float(mpim(I3)):+.6e}j")
        print(f"  G_ext         = {float(mpre(G_ext)):+.6e} + {float(mpim(G_ext)):+.6e}j")
        print(f"  Re[G*iI_tot]  = {float(mpre(G_ext*j*I_vertex_total)):+.6e}")
        print(f"  A_T(vertex)   = {float(A_T_vertex):+.10f}")
        print(f"  |B|_NL(vert)  = {float(BNL_vertex):+.10f}")
        print(f"  Σk³           = {float(sk3):.6f}")

    return float(A_T_vertex), float(BNL_vertex)

if __name__ == "__main__":
    print("=" * 65)
    print("CAI ET AL. f_NL NUMERICAL REPRODUCTION")
    print("Using Cai's mode functions and cubic Lagrangian directly")
    print("=" * 65)

    # Equilateral test (simplest to verify)
    print("\n--- EQUILATERAL (k1=k2=k3=1) ---")
    AT_eq, BNL_eq = compute_AT_and_BNL(1, 1, 1, eta_B=-0.001, eta_start=-200)
    print(f"\n  Target (Cai Eq. 40): |B|_NL(equil) = {-255/64:.6f}")
    print(f"  Note: vertex-only, field redef not included yet")

    # Squeezed test
    print("\n--- SQUEEZED (k1=0.01, k2=k3=1) ---")
    AT_sq, BNL_sq = compute_AT_and_BNL(0.01, 1, 1, eta_B=-0.001, eta_start=-200)
    print(f"\n  Target (Cai Eq. 38): |B|_NL(squeezed) = {-35/8:.6f}")
    print(f"  Note: vertex-only, need field redef for full result")
