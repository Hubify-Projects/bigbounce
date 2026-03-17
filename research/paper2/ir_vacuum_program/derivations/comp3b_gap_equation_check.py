#!/usr/bin/env python3
"""
Quick check: does the NJL gap equation have solutions for γ > 1
in proper-time regularization? The previous scan showed NO condensation
even for attractive couplings, which suggests a bug.
"""

import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

kappa_sq = 1.0

def gap_function(M, G, Lambda, N_c, R=0.0):
    """
    The NJL gap equation in proper-time regularization:
      M = 2G × N_c × I(M, Λ, R)
    where I is the fermion loop integral.

    Returns M - 2G × N_c × I (should be zero at the solution).

    In proper-time: I = (M / 4π²) × [Λ² - M² ln(1+Λ²/M²) + (R/12)ln(1+Λ²/M²)]
    """
    if abs(M) < 1e-15:
        return M  # M=0 is always a solution

    M2 = M**2
    L2 = Lambda**2

    # The standard NJL condensate integral (3+1 dim, proper-time cutoff)
    I = (M / (4 * np.pi**2)) * (
        L2 - M2 * np.log(1 + L2/M2)
    )

    # Curvature correction
    if R != 0:
        I += (M / (4 * np.pi**2)) * (R / 12) * np.log(1 + L2/M2)

    return M - 2 * G * N_c * I

# Test for γ = 2.0 (attractive)
gamma_test = 2.0
G_SP_test = (3 * kappa_sq / 16) * (gamma_test**2 - 1) / (gamma_test**2 + 1)
print(f"Testing gap equation for γ = {gamma_test}")
print(f"G_SP = {G_SP_test:.6f}")
print()

Lambda = 1.0  # Planck scale cutoff
N_c = 1

# Scan gap function
M_scan = np.linspace(0.001, 1.0, 500)
gap_vals = [gap_function(M, G_SP_test, Lambda, N_c) for M in M_scan]

print("Gap function g(M) = M - 2G × loop_integral:")
print(f"  g(0.001) = {gap_function(0.001, G_SP_test, Lambda, N_c):.6f}")
print(f"  g(0.1)   = {gap_function(0.1, G_SP_test, Lambda, N_c):.6f}")
print(f"  g(0.5)   = {gap_function(0.5, G_SP_test, Lambda, N_c):.6f}")
print(f"  g(1.0)   = {gap_function(1.0, G_SP_test, Lambda, N_c):.6f}")

# For a nontrivial solution, g(M) must cross zero at M > 0
# The condition for condensation is:
# dg/dM |_{M=0} < 0 (the trivial solution is unstable)
# which means: 1 - 2G × N_c × dI/dM|_{M=0} < 0
# dI/dM|_{M=0} = Λ²/(4π²)  (leading term)
# So: 1 - 2G × N_c × Λ²/(4π²) < 0
# G > 2π²/(N_c Λ²)

G_crit = 2 * np.pi**2 / (N_c * Lambda**2)
print(f"\nCritical coupling: G_crit = 2π²/(N_c Λ²) = {G_crit:.4f}")
print(f"Our coupling:      G_SP  = {G_SP_test:.4f}")
print(f"Ratio G_SP/G_crit = {G_SP_test/G_crit:.4f}")

if G_SP_test > G_crit:
    print("→ ABOVE critical coupling: condensation expected!")
elif G_SP_test > 0:
    print("→ BELOW critical coupling: no condensation in flat space")
    print("  But gravitational catalysis may help at R > 0")
else:
    print("→ REPULSIVE: no condensation possible")

# The issue is that G_SP ~ 0.11 while G_crit ~ 19.7
# The gravitational four-fermion coupling is FAR too weak!
# This is because G ~ κ² ~ 1/M_Pl² and Λ ~ M_Pl,
# so G × Λ² ~ κ² × M_Pl² ~ 1, but the critical coupling
# requires G × Λ² ~ 2π² ~ 20.

print(f"\n★ The gravitational coupling is {G_crit/G_SP_test:.0f}× too weak")
print(f"  for NJL condensation, even with attractive sign!")
print()
print("This is the STANDARD result: the EC four-fermion interaction")
print("is too weak to trigger chiral symmetry breaking because")
print("G ~ κ² ~ 1/M_Pl² and Λ ~ M_Pl, giving G×Λ² ~ O(1)")
print("while the NJL critical coupling requires G×Λ² ~ O(4π²) ≈ 40.")

# =============================================================================
# WITH CURVATURE: THE CATALYSIS LOGARITHM
# =============================================================================

print("\n" + "=" * 70)
print("GRAVITATIONAL CATALYSIS CHECK")
print("=" * 70)

# With R > 0, the gap function at small M becomes:
# g(M) ≈ M × [1 - (G N_c / 2π²)(Λ² + (R/12)ln(Λ²/M²))]
#
# The logarithmic divergence as M → 0 means:
# for ANY G > 0 and R > 0, g(M) → -∞ as M → 0⁺
# while g(M) → +∞ as M → ∞
# So there MUST be a zero crossing → nontrivial solution exists!
#
# BUT: the solution may be EXPONENTIALLY small:
# M* ~ Λ exp(-const/G)
# For G = G_SP ~ 0.1:
# M* ~ Λ × exp(-2π²/(G × N_c × R/12))
# = exp(-2π² × 12 / (0.1 × 1 × R))
# = exp(-240π²/R)
# For R = 1: M* ~ exp(-2369) ≈ 0

for R_test in [0.0, 0.1, 1.0, 10.0, 100.0, 1000.0]:
    if R_test == 0:
        # No catalysis at R=0
        print(f"\n  R = {R_test}: no catalysis (need R > 0)")
        continue

    gap_small = gap_function(1e-10, G_SP_test, Lambda, N_c, R_test)
    gap_large = gap_function(0.5, G_SP_test, Lambda, N_c, R_test)

    # Estimate M* from the gap equation
    # M ≈ Λ exp(-C/G) where C = 2π²/(N_c × R/12)
    C = 2 * np.pi**2 * 12 / (N_c * R_test)
    M_star_est = Lambda * np.exp(-C / G_SP_test)

    print(f"\n  R = {R_test}:")
    print(f"    g(1e-10) = {gap_small:.6e}")
    print(f"    g(0.5)   = {gap_large:.6e}")
    print(f"    Estimated M* ~ Λ exp(-{C/G_SP_test:.1f}) = {M_star_est:.2e} M_Pl")

    # Try to find the solution numerically
    try:
        if gap_small * gap_large < 0:
            M_solution = brentq(lambda M: gap_function(M, G_SP_test, Lambda, N_c, R_test),
                               1e-15, 0.5)
            print(f"    Numerical M* = {M_solution:.6e} M_Pl")
        else:
            # Try with a very small starting point
            gap_tiny = gap_function(1e-100, G_SP_test, Lambda, N_c, R_test)
            if gap_tiny < 0:
                M_solution = brentq(lambda M: gap_function(M, G_SP_test, Lambda, N_c, R_test),
                                   1e-100, 0.5, xtol=1e-120)
                print(f"    Numerical M* = {M_solution:.6e} M_Pl")
            else:
                print(f"    No sign change found")
    except Exception as e:
        print(f"    Solver error: {e}")

# =============================================================================
# KEY INSIGHT: EVEN WITH CATALYSIS, M* IS ABSURDLY SMALL
# =============================================================================

print("\n" + "=" * 70)
print("KEY INSIGHT")
print("=" * 70)
print()
print("Even if gravitational catalysis produces a nonzero M* at R > 0,")
print("the condensate is EXPONENTIALLY SUPPRESSED:")
print()
print("  M* ~ Λ × exp(-const/(G_SP × R))")
print()
print(f"For G_SP = {G_SP_test:.4f} and R = 1 (Planck curvature):")
C_planck = 2 * np.pi**2 * 12 / (N_c * 1.0)
print(f"  M* ~ exp(-{C_planck/G_SP_test:.0f}) ≈ 10^({-C_planck/G_SP_test/np.log(10):.0f})")
print()
print("The vacuum energy would be V ~ M*⁴, which is")
print(f"  V ~ 10^({-4*C_planck/G_SP_test/np.log(10):.0f}) M_Pl⁴")
print()
print("For comparison, the observed dark energy density is:")
print("  ρ_Λ ~ 10^{-122} M_Pl⁴")
print()
print("So the catalyzed condensate vacuum energy is either:")
print("  - Essentially zero (far below observed Λ)")
print("  - Or the mechanism doesn't work at all for repulsive coupling")
print()
print("BOTTOM LINE:")
print("  The NJL condensation route to dark energy from torsion")
print("  does not work at γ = 0.274, by a HUGE margin.")
print("  The coupling is both the wrong sign AND too weak.")
