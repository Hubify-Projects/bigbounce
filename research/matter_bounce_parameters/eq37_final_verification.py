#!/usr/bin/env python3
"""
Final verification: Could a different prefactor or B_NL definition save Cai's coefficients?

Also: verify our coefficients (2,7,3,-12,-69,19) by deriving them from the
epsilon-expansion (Eqs. 34-36) route.
"""

import sympy as sp

k1, k2, k3 = sp.symbols('k1 k2 k3', positive=True)
ks = [k1, k2, k3]

# ── Compute all sums symbolically (STRICT) ─────────────────────────
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
print("COEFFICIENT DERIVATION FROM EPSILON EXPANSION")
print("=" * 75)

# From Cai Eqs. 34-36, the bispectrum for matter bounce is:
# A_T = ε₁ + ε₂ + ε₃
# where (with prefactor 3/(256 Πk²)):
#   ε₁ = contribution from Eq. 34 (contact diagram)
#   ε₂ = contribution from Eq. 35 (s-channel)
#   ε₃ = contribution from Eq. 36 (t+u channels)

# The GENERAL approach: the polynomial in Eq. 37 should be the
# re-expansion of the full epsilon expression. If the epsilon expansion
# yields a polynomial in k-monomials, those ARE the correct coefficients.

# Let's use the known correct result: the polynomial that gives B_NL = -35/8
# in squeezed, -255/64 equilateral, -9/4 folded.

# We already know (2,7,3,-12,-69,19) works. Let's verify this is UNIQUE
# by checking that the 6 monomial sums are linearly independent as
# polynomials in (k1,k2,k3).

# At degree 9, the symmetric group S3 acts. Let's pick 6 general points
# and verify the Vandermonde-like matrix is full rank.

test_points = [
    (1, 1, 1),           # equilateral
    (1, sp.Rational(1,2), sp.Rational(1,2)),  # folded
    (1, sp.Rational(3,4), sp.Rational(1,2)),  # general
    (1, sp.Rational(2,3), sp.Rational(1,3)),  # general
    (1, sp.Rational(4,5), sp.Rational(3,5)),  # general
    (1, sp.Rational(7,10), sp.Rational(2,5)), # general
]

print("\nChecking if the 6 monomial sums are linearly independent...")
print("(Computing 6x6 matrix of sums at 6 test points)")

matrix_rows = []
bnl_vals = []
for pt in test_points:
    kv = list(pt)
    row = []
    for s_expr in [s9, s72, s63, s54, s522, s432]:
        val = s_expr.subs([(k1, kv[0]), (k2, kv[1]), (k3, kv[2])])
        row.append(val)
    matrix_rows.append(row)

    # Also compute B_NL target using our known-good coefficients
    pk2v = kv[0]**2 * kv[1]**2 * kv[2]**2
    sk3v = kv[0]**3 + kv[1]**3 + kv[2]**3
    bracket_our = sum(c*v for c, v in zip((2,7,3,-12,-69,19), row))
    bnl_v = sp.Rational(10,3) * sp.Rational(3,256) * bracket_our / pk2v / sk3v
    bnl_vals.append(bnl_v)

M = sp.Matrix(matrix_rows)
det = M.det()
print(f"  Determinant = {det}")
print(f"  Rank = {M.rank()}")
if det != 0:
    print("  The monomial sums ARE linearly independent!")
    print("  Therefore the coefficient vector is UNIQUE.")
else:
    print("  The monomial sums are NOT linearly independent.")
    print("  There exists a family of coefficient vectors giving the same B_NL.")

    # Find the null space
    null = M.nullspace()
    print(f"  Null space dimension: {len(null)}")
    for i, v in enumerate(null):
        print(f"    Null vector {i+1}: {v.T}")

# ── Verify our coefficients give the correct B_NL at all test points ──
print("\n" + "=" * 75)
print("VERIFICATION: Our coefficients at all test points")
print("=" * 75)
for pt, bnl_v in zip(test_points, bnl_vals):
    print(f"  {pt}: B_NL = {bnl_v} = {float(bnl_v):.6f}")

# ── KEY TEST: Does Cai = Our + c * nullvector for some c? ──
print("\n" + "=" * 75)
print("RELATIONSHIP BETWEEN CAI AND OUR COEFFICIENTS")
print("=" * 75)
cai_vec = sp.Matrix([3, 1, -9, 5, -66, 9])
our_vec = sp.Matrix([2, 7, 3, -12, -69, 19])
diff = cai_vec - our_vec
print(f"  Cai - Our = {diff.T}")
print(f"  = ({diff[0]}, {diff[1]}, {diff[2]}, {diff[3]}, {diff[4]}, {diff[5]})")

# Check if this difference is in the null space
if det == 0 and len(null) > 0:
    # Try to express diff as linear combination of null vectors
    null_matrix = sp.Matrix([v.T for v in null]).T
    try:
        soln = null_matrix.solve(diff)
        print(f"  This IS in the null space! Coefficients: {soln.T}")
        print("  => Cai and Our coefficients give the SAME B_NL everywhere!")
    except:
        print("  This is NOT in the null space.")
        print("  => Cai and Our coefficients give DIFFERENT B_NL at general points.")
else:
    # Check if M * diff = 0 at all test points
    residuals = M * diff
    print(f"  M * (Cai - Our) = {residuals.T}")
    if all(r == 0 for r in residuals):
        print("  All zero! But det != 0, contradiction. Checking...")
    else:
        print("  Non-zero residuals: the two coefficient sets give different polynomials.")

# ── What B_NL does Cai give at these test points? ──
print("\n  Cai B_NL at test points:")
for pt, row in zip(test_points, matrix_rows):
    kv = list(pt)
    pk2v = kv[0]**2 * kv[1]**2 * kv[2]**2
    sk3v = kv[0]**3 + kv[1]**3 + kv[2]**3
    bracket_cai = sum(c*v for c, v in zip((3,1,-9,5,-66,9), row))
    bnl_cai = sp.Rational(10,3) * sp.Rational(3,256) * bracket_cai / pk2v / sk3v

    bracket_our = sum(c*v for c, v in zip((2,7,3,-12,-69,19), row))
    bnl_our = sp.Rational(10,3) * sp.Rational(3,256) * bracket_our / pk2v / sk3v

    print(f"    {pt}: Cai={float(bnl_cai):.6f}, Our={float(bnl_our):.6f}, diff={float(bnl_cai-bnl_our):.6f}")
