#!/usr/bin/env python3
"""
Check Cai's ACTUAL Eq. 37 coefficients from the paper:
  A_T = (3/(256 Πk²)) × {3Σk⁹ + Σk⁷k² - 9Σk⁶k³ + 5Σk⁵k⁴ - 66Σk⁵k²k² + 9Σk⁴k³k²}

Compare against:
  1. Our fit coefficients (2, 7, 3, -12, -69, 19)
  2. The ε-decomposition (Eqs. 34+35+36)
  3. The vertex sum (Eqs. 28+31+32+33)
"""

def compute_sums(k1, k2, k3):
    ks = [k1, k2, k3]
    pk2 = k1**2 * k2**2 * k3**2
    sk3 = k1**3 + k2**3 + k3**3
    s9 = sum(k**9 for k in ks)
    s72 = sum(ks[i]**7 * ks[j]**2 for i in range(3) for j in range(3) if i != j)
    s63 = sum(ks[i]**6 * ks[j]**3 for i in range(3) for j in range(3) if i != j)
    s54 = sum(ks[i]**5 * ks[j]**4 for i in range(3) for j in range(3) if i != j)
    s522 = sum(ks[i]**5 * ks[j]**2 * ks[l]**2
              for i in range(3) for j in range(3) for l in range(3)
              if i != j and j != l and i != l)
    s432 = sum(ks[i]**4 * ks[j]**3 * ks[l]**2
              for i in range(3) for j in range(3) for l in range(3)
              if i != j and j != l and i != l)
    return s9, s72, s63, s54, s522, s432, pk2, sk3


def BNL_with_coeffs(k1, k2, k3, coeffs, pf=3.0/256):
    s9, s72, s63, s54, s522, s432, pk2, sk3 = compute_sums(k1, k2, k3)
    bracket = coeffs[0]*s9 + coeffs[1]*s72 + coeffs[2]*s63 + coeffs[3]*s54 + coeffs[4]*s522 + coeffs[5]*s432
    AT = (pf / pk2) * bracket
    return (10.0/3.0) * AT / sk3, AT


print("=" * 70)
print("CAI EQ. 37 DIRECT CHECK")
print("=" * 70)

# Cai's actual coefficients from the paper image
CAI_ACTUAL = (3, 1, -9, 5, -66, 9)

# Our fit coefficients
OUR_FIT = (2, 7, 3, -12, -69, 19)

# Test configurations
configs = [
    ("Squeezed", 1e-6, 1, 1, -35/8),
    ("Equilateral", 1, 1, 1, -255/64),
    ("Folded", 1, 0.5, 0.5, -9/4),
    ("General", 1, 0.8, 0.3, None),
]

print(f"\n  {'Config':<15s} {'Cai actual':>12s} {'Our fit':>12s} {'Target':>10s} {'Match?':>8s}")
print("  " + "-" * 62)

for name, k1, k2, k3, target in configs:
    bnl_cai, _ = BNL_with_coeffs(k1, k2, k3, CAI_ACTUAL)
    bnl_our, _ = BNL_with_coeffs(k1, k2, k3, OUR_FIT)
    target_str = f"{target:.4f}" if target else "—"

    match = "YES" if target and abs(bnl_cai - target) < 0.01 else ("—" if not target else "NO")
    print(f"  {name:<15s} {bnl_cai:>+12.4f} {bnl_our:>+12.4f} {target_str:>10s} {match:>8s}")

# Check if Cai's actual coefficients satisfy the constraint c1+c2+c3+c4 = 0
print(f"\n  Constraint check (c1+c2+c3+c4 = 0 for finiteness):")
print(f"    Cai actual: {CAI_ACTUAL[0]}+{CAI_ACTUAL[1]}+{CAI_ACTUAL[2]}+{CAI_ACTUAL[3]} = {sum(CAI_ACTUAL[:4])}")
print(f"    Our fit:    {OUR_FIT[0]}+{OUR_FIT[1]}+{OUR_FIT[2]}+{OUR_FIT[3]} = {sum(OUR_FIT[:4])}")

# Detailed: compute AT at equilateral for Cai's actual coefficients
s9, s72, s63, s54, s522, s432, pk2, sk3 = compute_sums(1, 1, 1)
print(f"\n  Momentum sums at equilateral (1,1,1):")
print(f"    Σk⁹={s9}, Σk⁷k²={s72}, Σk⁶k³={s63}, Σk⁵k⁴={s54}, Σk⁵k²k²={s522}, Σk⁴k³k²={s432}")
print(f"    Πk²={pk2}, Σk³={sk3}")

bracket_cai = 3*s9 + 1*s72 - 9*s63 + 5*s54 - 66*s522 + 9*s432
bracket_our = 2*s9 + 7*s72 + 3*s63 - 12*s54 - 69*s522 + 19*s432
print(f"    Bracket (Cai): {bracket_cai}")
print(f"    Bracket (our): {bracket_our}")
print(f"    AT (Cai): {(3/256)*bracket_cai:.6f}")
print(f"    AT (our): {(3/256)*bracket_our:.6f}")

# Also check at a GENERAL non-degenerate point where the underdetermination matters
print(f"\n  GENERAL configuration test (1, 0.7, 0.4):")
bnl_cai, at_cai = BNL_with_coeffs(1, 0.7, 0.4, CAI_ACTUAL)
bnl_our, at_our = BNL_with_coeffs(1, 0.7, 0.4, OUR_FIT)
print(f"    B_NL (Cai actual): {bnl_cai:+.6f}")
print(f"    B_NL (our fit):    {bnl_our:+.6f}")
print(f"    Difference:        {bnl_cai - bnl_our:+.6f}")
print(f"    Ratio:             {bnl_cai/bnl_our:.6f}")
if abs(bnl_cai - bnl_our) > 0.01:
    print(f"    >>> THESE DIFFER! The two coefficient sets give different shapes.")
    print(f"    >>> Only Cai's actual coefficients should be used for template overlap.")
