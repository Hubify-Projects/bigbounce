#!/usr/bin/env python3
"""
Deep analysis of the squeezed limit for Eq. 37.

The squeezed limit is k1 → 0, k2 = k3 = k.
In this limit, the bispectrum formula should give f_NL = -35/8.

But this is DERIVED from the ε-expansion (Eqs. 34-36), not directly from Eq. 37.
Eq. 37 is a re-expansion of the same expression in momentum monomials.

Let's check: does the Eq. 37 polynomial even CONVERGE to -35/8 in the squeezed limit?
The issue is that Σk³ → 2k³ while individual momentum monomials scale differently.
"""

from fractions import Fraction
import sympy as sp

# Use symbolic computation for the squeezed limit
eps, k = sp.symbols('eps k', positive=True)

# k1 = eps, k2 = k3 = k
k1, k2, k3 = eps, k, k
ks = [k1, k2, k3]

# Compute all sums symbolically (STRICT convention for triple sums)
s9 = sum(ki**9 for ki in ks)
s72 = sum(ks[i]**7 * ks[j]**2 for i in range(3) for j in range(3) if i != j)
s63 = sum(ks[i]**6 * ks[j]**3 for i in range(3) for j in range(3) if i != j)
s54 = sum(ks[i]**5 * ks[j]**4 for i in range(3) for j in range(3) if i != j)
s522 = sum(ks[i]**5 * ks[j]**2 * ks[l]**2
          for i in range(3) for j in range(3) for l in range(3)
          if i != j and j != l and i != l)
s432 = sum(ks[i]**4 * ks[j]**3 * ks[l]**2
          for i in range(3) for j in range(3) for l in range(3)
          if i != j and j != l and i != l)
pk2 = k1**2 * k2**2 * k3**2
sk3 = k1**3 + k2**3 + k3**3

print("=" * 75)
print("SYMBOLIC SQUEEZED LIMIT ANALYSIS")
print("k1 = eps, k2 = k3 = k")
print("=" * 75)

print("\nMonomial sums (expanded):")
for name, val in [("s9", s9), ("s72", s72), ("s63", s63), ("s54", s54),
                   ("s522", s522), ("s432", s432), ("pk2", pk2), ("sk3", sk3)]:
    expanded = sp.expand(val)
    print(f"  {name} = {expanded}")

# Compute B_NL with Cai's coefficients
CAI = (3, 1, -9, 5, -66, 9)
OUR = (2, 7, 3, -12, -69, 19)

for label, coeffs in [("Cai (3,1,-9,5,-66,9)", CAI), ("Our (2,7,3,-12,-69,19)", OUR)]:
    bracket = coeffs[0]*s9 + coeffs[1]*s72 + coeffs[2]*s63 + coeffs[3]*s54 + coeffs[4]*s522 + coeffs[5]*s432
    bracket_expanded = sp.expand(bracket)
    AT = sp.Rational(3, 256) * bracket / pk2
    BNL = sp.Rational(10, 3) * AT / sk3

    # Simplify
    BNL_simplified = sp.simplify(BNL)

    # Take the limit eps → 0
    BNL_limit = sp.limit(BNL, eps, 0)

    print(f"\n--- {label} ---")
    print(f"  Bracket = {bracket_expanded}")
    print(f"  B_NL (simplified) = {sp.simplify(sp.cancel(BNL))}")
    print(f"  B_NL limit (eps→0) = {BNL_limit}")
    print(f"  As decimal: {float(BNL_limit):.6f}")
    print(f"  Target: -35/8 = {-35/8:.6f}")
    print(f"  Match: {'YES' if BNL_limit == sp.Rational(-35, 8) else 'NO'}")

# Now check: what does B_NL simplify to at equilateral and folded?
print("\n" + "=" * 75)
print("EQUILATERAL AND FOLDED (exact symbolic)")
print("=" * 75)

for label, coeffs in [("Cai", CAI), ("Our", OUR)]:
    for config_name, kvals in [("Equilateral (1,1,1)", (1,1,1)), ("Folded (1,1/2,1/2)", (1, sp.Rational(1,2), sp.Rational(1,2)))]:
        k1v, k2v, k3v = kvals
        ksv = [k1v, k2v, k3v]
        s9v = sum(ki**9 for ki in ksv)
        s72v = sum(ksv[i]**7 * ksv[j]**2 for i in range(3) for j in range(3) if i != j)
        s63v = sum(ksv[i]**6 * ksv[j]**3 for i in range(3) for j in range(3) if i != j)
        s54v = sum(ksv[i]**5 * ksv[j]**4 for i in range(3) for j in range(3) if i != j)
        s522v = sum(ksv[i]**5 * ksv[j]**2 * ksv[l]**2
                  for i in range(3) for j in range(3) for l in range(3)
                  if i != j and j != l and i != l)
        s432v = sum(ksv[i]**4 * ksv[j]**3 * ksv[l]**2
                  for i in range(3) for j in range(3) for l in range(3)
                  if i != j and j != l and i != l)
        pk2v = k1v**2 * k2v**2 * k3v**2
        sk3v = k1v**3 + k2v**3 + k3v**3

        bracket = (coeffs[0]*s9v + coeffs[1]*s72v + coeffs[2]*s63v
                   + coeffs[3]*s54v + coeffs[4]*s522v + coeffs[5]*s432v)
        AT = sp.Rational(3, 256) * bracket / pk2v
        BNL = sp.Rational(10, 3) * AT / sk3v

        print(f"  {label} @ {config_name}: B_NL = {BNL} = {float(BNL):.6f}")

# Now the KEY question: since our fit coefficients give the right equilateral and folded
# but WRONG squeezed limit, maybe the published f_NL = -35/8 is NOT computed from Eq. 37
# but from the ε-expansion (Eqs. 34-36). Let's verify what Eq. 37 with the correct
# coefficients actually gives in the squeezed limit.

print("\n" + "=" * 75)
print("KEY INSIGHT: SQUEEZED LIMIT FROM EQ. 37 vs FROM EPSILON EXPANSION")
print("=" * 75)
print("""
The squeezed limit f_NL = -35/8 comes from Cai Eq. 34-36 (the epsilon expansion),
NOT from evaluating Eq. 37 at (eps, 1, 1) and taking eps → 0.

Eq. 37 is the shape function S(k1,k2,k3), which diverges term-by-term in the
squeezed limit. The f_NL = -35/8 is extracted by a DIFFERENT procedure:
taking the bispectrum B(k1,k2,k3) in the limit k1 << k2 ≈ k3 and comparing
to the local ansatz B_local = (6/5) f_NL [P(k1)P(k2) + cyclic].

So the "benchmark" for squeezed is NOT "evaluate B_NL(eps,1,1) from Eq. 37".
It should match the analytic squeezed limit derived separately.

Let's verify: does our B_NL formula give -35/8 in the eps→0 limit?
""")

# The BNL formula is B_NL = (10/3) * A_T / Σk³
# where A_T = (3/(256 Πk²)) * bracket
# In the squeezed limit k1→0, k2=k3=k:
#   Πk² = k1² k⁴ → 0
#   Σk³ = k1³ + 2k³ → 2k³
# So we need to be careful about how the bracket scales with k1.

# Let's see the leading behavior
print("Leading behavior of bracket terms as eps → 0:")
for name, val in [("s9", s9), ("s72", s72), ("s63", s63), ("s54", s54),
                   ("s522", s522), ("s432", s432)]:
    # Get leading term in eps
    series = sp.series(sp.expand(val), eps, 0, n=3)
    print(f"  {name} = {series}")

print(f"\n  pk2 = {sp.series(sp.expand(pk2), eps, 0, n=3)}")
print(f"  sk3 = {sp.series(sp.expand(sk3), eps, 0, n=3)}")

# The ratio bracket/pk2 needs to be finite for B_NL to be finite
for label, coeffs in [("Cai", CAI), ("Our", OUR)]:
    bracket = coeffs[0]*s9 + coeffs[1]*s72 + coeffs[2]*s63 + coeffs[3]*s54 + coeffs[4]*s522 + coeffs[5]*s432
    ratio = bracket / pk2
    ratio_series = sp.series(ratio, eps, 0, n=3)
    print(f"\n  bracket/pk2 for {label}:")
    print(f"    = {ratio_series}")
    bnl_ratio = sp.Rational(10,3) * sp.Rational(3,256) * ratio / sk3
    bnl_limit = sp.limit(bnl_ratio, eps, 0)
    print(f"    B_NL limit = {bnl_limit} = {float(bnl_limit):.6f}")
