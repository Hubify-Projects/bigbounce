#!/usr/bin/env python3
"""
Test two interpretations of the Cai Eq. 37 triple-index summation convention.

From arXiv:0903.0631 Eq. 37:
  A_T = (3/(256 Πk²)) × {3Σk⁹ + Σk⁷k² - 9Σk⁶k³ + 5Σk⁵k⁴ - 66Σ_{i≠j≠k}k_i⁵k_j²k_k² + 9Σ_{i≠j≠k}k_i⁴k_j³k_k²}

The TeX source writes the last two sums as sum_{i neq j neq k}.
This is AMBIGUOUS:
  (a) "Strict": all three indices pairwise distinct (i≠j, j≠k, i≠k) → 3! = 6 terms each
  (b) "Relaxed": only i≠j AND j≠k, but i=k is allowed → 6 + 6(i=k extras) = 12 terms each

For the relaxed case, the i=k extra terms are:
  Σ_{i≠j≠k} k_i⁵k_j²k_k²  with i=k →  Σ_{i≠j} k_i⁷k_j²  (3 ordered pairs × ... wait, 6 ordered pairs total)
  Σ_{i≠j≠k} k_i⁴k_j³k_k²  with i=k →  Σ_{i≠j} k_i⁶k_j³

So relaxed = strict + these extra 2-index sums.

We test whether either interpretation reproduces Cai's published benchmarks:
  squeezed:    B_NL = -35/8  = -4.375
  equilateral: B_NL = -255/64 ≈ -3.984375
  folded:      B_NL = -9/4   = -2.25
"""

from fractions import Fraction


def compute_sums_strict(k1, k2, k3):
    """All three indices pairwise distinct: 6 terms for triple sums."""
    ks = [k1, k2, k3]
    pk2 = k1**2 * k2**2 * k3**2
    sk3 = k1**3 + k2**3 + k3**3

    # Single-index sums (3 terms)
    s9 = sum(k**9 for k in ks)

    # Two-index sums (6 ordered pairs)
    s72 = sum(ks[i]**7 * ks[j]**2 for i in range(3) for j in range(3) if i != j)
    s63 = sum(ks[i]**6 * ks[j]**3 for i in range(3) for j in range(3) if i != j)
    s54 = sum(ks[i]**5 * ks[j]**4 for i in range(3) for j in range(3) if i != j)

    # Triple-index sums, STRICT: all pairwise distinct (6 terms)
    s522 = sum(ks[i]**5 * ks[j]**2 * ks[l]**2
              for i in range(3) for j in range(3) for l in range(3)
              if i != j and j != l and i != l)
    s432 = sum(ks[i]**4 * ks[j]**3 * ks[l]**2
              for i in range(3) for j in range(3) for l in range(3)
              if i != j and j != l and i != l)

    return s9, s72, s63, s54, s522, s432, pk2, sk3


def compute_sums_relaxed(k1, k2, k3):
    """i≠j AND j≠k only (i=k allowed): 12 terms for triple sums."""
    ks = [k1, k2, k3]
    pk2 = k1**2 * k2**2 * k3**2
    sk3 = k1**3 + k2**3 + k3**3

    # Single-index sums (3 terms)
    s9 = sum(k**9 for k in ks)

    # Two-index sums (6 ordered pairs)
    s72 = sum(ks[i]**7 * ks[j]**2 for i in range(3) for j in range(3) if i != j)
    s63 = sum(ks[i]**6 * ks[j]**3 for i in range(3) for j in range(3) if i != j)
    s54 = sum(ks[i]**5 * ks[j]**4 for i in range(3) for j in range(3) if i != j)

    # Triple-index sums, RELAXED: i≠j AND j≠k (allows i=k) → 12 terms
    s522 = sum(ks[i]**5 * ks[j]**2 * ks[l]**2
              for i in range(3) for j in range(3) for l in range(3)
              if i != j and j != l)
    s432 = sum(ks[i]**4 * ks[j]**3 * ks[l]**2
              for i in range(3) for j in range(3) for l in range(3)
              if i != j and j != l)

    return s9, s72, s63, s54, s522, s432, pk2, sk3


def BNL_with_sums(sums, coeffs, pf_num=3, pf_den=256):
    """Compute B_NL using Fraction arithmetic for exact results."""
    s9, s72, s63, s54, s522, s432, pk2, sk3 = sums
    bracket = (coeffs[0]*s9 + coeffs[1]*s72 + coeffs[2]*s63
               + coeffs[3]*s54 + coeffs[4]*s522 + coeffs[5]*s432)
    AT = Fraction(pf_num, pf_den) * bracket / pk2
    BNL = Fraction(10, 3) * AT / sk3
    return BNL, AT


def BNL_float(k1, k2, k3, coeffs, compute_fn, pf=3.0/256):
    """Float version for non-integer k values."""
    s9, s72, s63, s54, s522, s432, pk2, sk3 = compute_fn(k1, k2, k3)
    bracket = (coeffs[0]*s9 + coeffs[1]*s72 + coeffs[2]*s63
               + coeffs[3]*s54 + coeffs[4]*s522 + coeffs[5]*s432)
    AT = pf * bracket / pk2
    BNL = (10.0/3.0) * AT / sk3
    return BNL


# ─── Cai's published coefficients ───────────────────────────────────────
CAI = (3, 1, -9, 5, -66, 9)
OUR_FIT = (2, 7, 3, -12, -69, 19)

# ─── Exact integer benchmarks (Fraction arithmetic) ─────────────────────
print("=" * 75)
print("EQ. 37 SUM CONVENTION TEST")
print("Testing Cai coefficients (3, 1, -9, 5, -66, 9) under two interpretations")
print("=" * 75)

# --- Part 1: Equilateral (1,1,1) — exact fractions ---
print("\n─── EQUILATERAL (1, 1, 1) ─── Target: -255/64")
for label, compute_fn in [("STRICT (all distinct, 6 terms)", compute_sums_strict),
                           ("RELAXED (i≠j,j≠k, 12 terms)", compute_sums_relaxed)]:
    sums = compute_fn(Fraction(1), Fraction(1), Fraction(1))
    s9, s72, s63, s54, s522, s432, pk2, sk3 = sums
    print(f"\n  {label}:")
    print(f"    s9={s9}, s72={s72}, s63={s63}, s54={s54}, s522={s522}, s432={s432}")
    print(f"    pk2={pk2}, sk3={sk3}")

    bnl, at = BNL_with_sums(sums, CAI)
    print(f"    Bracket = {CAI[0]}*{s9} + {CAI[1]}*{s72} + ({CAI[2]})*{s63} + {CAI[3]}*{s54} + ({CAI[4]})*{s522} + {CAI[5]}*{s432}")
    bracket = CAI[0]*s9 + CAI[1]*s72 + CAI[2]*s63 + CAI[3]*s54 + CAI[4]*s522 + CAI[5]*s432
    print(f"    Bracket = {bracket}")
    print(f"    A_T = (3/256) * {bracket} / {pk2} = {at} = {float(at):.6f}")
    print(f"    B_NL = (10/3) * A_T / {sk3} = {bnl} = {float(bnl):.6f}")
    target = Fraction(-255, 64)
    print(f"    Target: {target} = {float(target):.6f}")
    print(f"    MATCH: {'YES' if bnl == target else 'NO'}")

# --- Part 2: Folded (1, 1/2, 1/2) — exact fractions ---
print("\n─── FOLDED (1, 1/2, 1/2) ─── Target: -9/4")
for label, compute_fn in [("STRICT (all distinct, 6 terms)", compute_sums_strict),
                           ("RELAXED (i≠j,j≠k, 12 terms)", compute_sums_relaxed)]:
    sums = compute_fn(Fraction(1), Fraction(1, 2), Fraction(1, 2))
    s9, s72, s63, s54, s522, s432, pk2, sk3 = sums
    print(f"\n  {label}:")
    print(f"    s9={s9}, s72={s72}, s63={s63}, s54={s54}, s522={s522}, s432={s432}")

    bnl, at = BNL_with_sums(sums, CAI)
    bracket = CAI[0]*s9 + CAI[1]*s72 + CAI[2]*s63 + CAI[3]*s54 + CAI[4]*s522 + CAI[5]*s432
    print(f"    Bracket = {bracket}")
    print(f"    B_NL = {bnl} = {float(bnl):.6f}")
    target = Fraction(-9, 4)
    print(f"    Target: {target} = {float(target):.6f}")
    print(f"    MATCH: {'YES' if bnl == target else 'NO'}")

# --- Part 3: Squeezed limit ---
print("\n─── SQUEEZED (ε→0, 1, 1) ─── Target: -35/8")
print("  Using k1=1e-10 for near-squeezed float evaluation")
eps = 1e-10
for label, compute_fn in [("STRICT (all distinct, 6 terms)", compute_sums_strict),
                           ("RELAXED (i≠j,j≠k, 12 terms)", compute_sums_relaxed)]:
    bnl = BNL_float(eps, 1.0, 1.0, CAI, compute_fn)
    target = -35.0/8.0
    print(f"\n  {label}:")
    print(f"    B_NL = {bnl:+.8f}")
    print(f"    Target: {target:.8f}")
    print(f"    MATCH: {'YES' if abs(bnl - target) < 1e-4 else 'NO'}")

# --- Part 4: Analytic squeezed limit via Fraction with tiny rational ---
print("\n─── SQUEEZED (exact, ε=1/1000000, 1, 1) ─── Target: -35/8")
for label, compute_fn in [("STRICT", compute_sums_strict),
                           ("RELAXED", compute_sums_relaxed)]:
    eps_frac = Fraction(1, 1000000)
    sums = compute_fn(eps_frac, Fraction(1), Fraction(1))
    bnl, at = BNL_with_sums(sums, CAI)
    # In squeezed limit, B_NL → -35/8 + O(ε)
    print(f"\n  {label}:")
    print(f"    B_NL = {float(bnl):.10f}")
    print(f"    Target: {float(Fraction(-35, 8)):.10f}")
    print(f"    Difference from -35/8: {float(bnl - Fraction(-35, 8)):+.2e}")

# --- Part 5: Understand the difference ---
print("\n" + "=" * 75)
print("UNDERSTANDING THE DIFFERENCE")
print("=" * 75)
print("\nRelaxed triple sums = Strict triple sums + extra terms from i=k:")
print("  Σ_{relaxed} k_i⁵k_j²k_k² = Σ_{strict} k_i⁵k_j²k_k² + Σ_{i≠j} k_i⁷k_j²")
print("  Σ_{relaxed} k_i⁴k_j³k_k² = Σ_{strict} k_i⁴k_j³k_k² + Σ_{i≠j} k_i⁶k_j³")
print()
print("So the Cai bracket under relaxed interpretation becomes:")
print("  3·s9 + 1·s72 - 9·s63 + 5·s54 - 66·(s522_strict + s72) + 9·(s432_strict + s63)")
print("  = 3·s9 + (1-66)·s72 + (-9+9)·s63 + 5·s54 - 66·s522_strict + 9·s432_strict")
print("  = 3·s9 - 65·s72 + 0·s63 + 5·s54 - 66·s522_strict + 9·s432_strict")
print()
print("Compare with Cai strict = 3·s9 + 1·s72 - 9·s63 + 5·s54 - 66·s522_strict + 9·s432_strict")
print()

# Verify the algebraic identity
print("Verify: relaxed sums = strict sums + extra 2-index sums")
for label, k_tuple in [("Equilateral", (Fraction(1), Fraction(1), Fraction(1))),
                        ("Folded", (Fraction(1), Fraction(1,2), Fraction(1,2)))]:
    strict = compute_sums_strict(*k_tuple)
    relaxed = compute_sums_relaxed(*k_tuple)
    ks = list(k_tuple)
    extra_s72 = sum(ks[i]**7 * ks[j]**2 for i in range(3) for j in range(3) if i != j)
    extra_s63 = sum(ks[i]**6 * ks[j]**3 for i in range(3) for j in range(3) if i != j)

    print(f"\n  {label}:")
    print(f"    s522: strict={strict[4]}, relaxed={relaxed[4]}, diff={relaxed[4]-strict[4]}, s72={extra_s72}, match={relaxed[4]-strict[4]==extra_s72}")
    print(f"    s432: strict={strict[5]}, relaxed={relaxed[5]}, diff={relaxed[5]-strict[5]}, s63={extra_s63}, match={relaxed[5]-strict[5]==extra_s63}")

# --- Part 6: Effective coefficients under relaxed interpretation ---
print("\n" + "=" * 75)
print("EFFECTIVE COEFFICIENTS")
print("=" * 75)
print("\nIf Cai uses relaxed convention, the effective coefficients in terms of")
print("STRICT sums are:")
print("  c1_eff = 3 (unchanged)")
print("  c2_eff = 1 + (-66)*1 = -65  (s72 absorbs i=k terms from s522)")
print("  c3_eff = -9 + 9*1 = 0       (s63 absorbs i=k terms from s432)")
print("  c4_eff = 5 (unchanged)")
print("  c5_eff = -66 (unchanged, now applied to strict s522)")
print("  c6_eff = 9 (unchanged, now applied to strict s432)")
print()
print("But our fit coefficients are (2, 7, 3, -12, -69, 19).")
print("These DON'T match (3, -65, 0, 5, -66, 9) either.")

# --- Part 7: What about k≠j AND i≠k only (not i≠j)? ---
print("\n" + "=" * 75)
print("ALTERNATIVE RELAXED: j≠k AND i≠k only (allows i=j)")
print("=" * 75)

def compute_sums_relaxed_alt(k1, k2, k3):
    """j≠k AND i≠k only (allows i=j) — another possible reading."""
    ks = [k1, k2, k3]
    pk2 = k1**2 * k2**2 * k3**2
    sk3 = k1**3 + k2**3 + k3**3
    s9 = sum(k**9 for k in ks)
    s72 = sum(ks[i]**7 * ks[j]**2 for i in range(3) for j in range(3) if i != j)
    s63 = sum(ks[i]**6 * ks[j]**3 for i in range(3) for j in range(3) if i != j)
    s54 = sum(ks[i]**5 * ks[j]**4 for i in range(3) for j in range(3) if i != j)
    # j≠k AND i≠k (allows i=j)
    s522 = sum(ks[i]**5 * ks[j]**2 * ks[l]**2
              for i in range(3) for j in range(3) for l in range(3)
              if j != l and i != l)
    s432 = sum(ks[i]**4 * ks[j]**3 * ks[l]**2
              for i in range(3) for j in range(3) for l in range(3)
              if j != l and i != l)
    return s9, s72, s63, s54, s522, s432, pk2, sk3


print("\n  Equilateral (1,1,1):")
sums = compute_sums_relaxed_alt(Fraction(1), Fraction(1), Fraction(1))
bnl, at = BNL_with_sums(sums, CAI)
print(f"    B_NL = {bnl} = {float(bnl):.6f}, target -255/64 = {float(Fraction(-255,64)):.6f}, MATCH: {'YES' if bnl == Fraction(-255,64) else 'NO'}")

print("\n  Folded (1, 1/2, 1/2):")
sums = compute_sums_relaxed_alt(Fraction(1), Fraction(1,2), Fraction(1,2))
bnl, at = BNL_with_sums(sums, CAI)
print(f"    B_NL = {bnl} = {float(bnl):.6f}, target -9/4 = {float(Fraction(-9,4)):.6f}, MATCH: {'YES' if bnl == Fraction(-9,4) else 'NO'}")

# --- Part 8: What about i≠j AND i≠k only (allows j=k)? ---
print("\n" + "=" * 75)
print("ALTERNATIVE RELAXED 2: i≠j AND i≠k only (allows j=k)")
print("=" * 75)

def compute_sums_relaxed_jk(k1, k2, k3):
    """i≠j AND i≠k only (allows j=k)."""
    ks = [k1, k2, k3]
    pk2 = k1**2 * k2**2 * k3**2
    sk3 = k1**3 + k2**3 + k3**3
    s9 = sum(k**9 for k in ks)
    s72 = sum(ks[i]**7 * ks[j]**2 for i in range(3) for j in range(3) if i != j)
    s63 = sum(ks[i]**6 * ks[j]**3 for i in range(3) for j in range(3) if i != j)
    s54 = sum(ks[i]**5 * ks[j]**4 for i in range(3) for j in range(3) if i != j)
    # i≠j AND i≠k (allows j=k)
    s522 = sum(ks[i]**5 * ks[j]**2 * ks[l]**2
              for i in range(3) for j in range(3) for l in range(3)
              if i != j and i != l)
    s432 = sum(ks[i]**4 * ks[j]**3 * ks[l]**2
              for i in range(3) for j in range(3) for l in range(3)
              if i != j and i != l)
    return s9, s72, s63, s54, s522, s432, pk2, sk3


print("\n  Equilateral (1,1,1):")
sums = compute_sums_relaxed_jk(Fraction(1), Fraction(1), Fraction(1))
bnl, at = BNL_with_sums(sums, CAI)
s522_val = sums[4]
s432_val = sums[5]
print(f"    s522={s522_val}, s432={s432_val}")
print(f"    B_NL = {bnl} = {float(bnl):.6f}, target -255/64 = {float(Fraction(-255,64)):.6f}, MATCH: {'YES' if bnl == Fraction(-255,64) else 'NO'}")

print("\n  Folded (1, 1/2, 1/2):")
sums = compute_sums_relaxed_jk(Fraction(1), Fraction(1,2), Fraction(1,2))
bnl, at = BNL_with_sums(sums, CAI)
print(f"    B_NL = {bnl} = {float(bnl):.6f}, target -9/4 = {float(Fraction(-9,4)):.6f}, MATCH: {'YES' if bnl == Fraction(-9,4) else 'NO'}")

print(f"\n  Squeezed (1e-10, 1, 1):")
bnl = BNL_float(1e-10, 1.0, 1.0, CAI, compute_sums_relaxed_jk)
print(f"    B_NL = {bnl:+.8f}, target = -4.37500000, MATCH: {'YES' if abs(bnl - (-35.0/8.0)) < 1e-4 else 'NO'}")

# --- Part 9: Cross-check with our fit coefficients under strict ---
print("\n" + "=" * 75)
print("CROSS-CHECK: Our fit (2,7,3,-12,-69,19) under strict convention")
print("=" * 75)

print("\n  Equilateral (1,1,1):")
sums = compute_sums_strict(Fraction(1), Fraction(1), Fraction(1))
bnl, at = BNL_with_sums(sums, OUR_FIT)
print(f"    B_NL = {bnl} = {float(bnl):.6f}, target -255/64, MATCH: {'YES' if bnl == Fraction(-255,64) else 'NO'}")

print("\n  Folded (1, 1/2, 1/2):")
sums = compute_sums_strict(Fraction(1), Fraction(1,2), Fraction(1,2))
bnl, at = BNL_with_sums(sums, OUR_FIT)
print(f"    B_NL = {bnl} = {float(bnl):.6f}, target -9/4, MATCH: {'YES' if bnl == Fraction(-9,4) else 'NO'}")

print(f"\n  Squeezed (1e-10, 1, 1):")
bnl = BNL_float(1e-10, 1.0, 1.0, OUR_FIT, compute_sums_strict)
print(f"    B_NL = {bnl:+.8f}, target = -4.37500000, MATCH: {'YES' if abs(bnl - (-35.0/8.0)) < 1e-4 else 'NO'}")


# --- Part 10: Summary ---
print("\n" + "=" * 75)
print("SUMMARY")
print("=" * 75)
print("""
Convention interpretations tested for Cai (3,1,-9,5,-66,9):
  1. STRICT: i≠j, j≠k, i≠k (all pairwise distinct, 6 permutations)
  2. RELAXED: i≠j, j≠k only (allows i=k, 12 terms)
  3. ALT-RELAXED: j≠k, i≠k only (allows i=j, 12 terms)
  4. ALT-RELAXED-2: i≠j, i≠k only (allows j=k, 12 terms)

And our fit coefficients (2,7,3,-12,-69,19) under STRICT convention.
""")
