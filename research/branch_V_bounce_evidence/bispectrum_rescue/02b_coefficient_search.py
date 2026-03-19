#!/usr/bin/env python3
"""
Determine the correct coefficients in Cai's Eq. 37 by fitting to their
three reported special-case values:
  Squeezed: |B|_NL = -35/8
  Equilateral: |B|_NL = -255/64
  Folded (k1=2k2=2k3): |B|_NL = -9/4

AT = prefactor/Πk² × {c1·Σk⁹ + c2·Σk⁷k² + c3·Σk⁶k³ + c4·Σk⁵k⁴
                       + c5·Σk⁵k²k² + c6·Σk⁴k³k²}
"""
import numpy as np
from scipy.optimize import minimize

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

def BNL(coeffs, prefactor, k1, k2, k3):
    c1, c2, c3, c4, c5, c6 = coeffs
    s9, s72, s63, s54, s522, s432, pk2, sk3 = compute_sums(k1, k2, k3)
    bracket = c1*s9 + c2*s72 + c3*s63 + c4*s54 + c5*s522 + c6*s432
    AT = (prefactor / pk2) * bracket
    return (10.0/3.0) * AT / sk3

# Targets
target_sq = -35.0/8   # squeezed
target_eq = -255.0/64  # equilateral
target_fold = -9.0/4   # folded

# Analytical constraints for squeezed limit k1→0:
# At k1=0: bracket → 2(c1+c2+c3+c4) must = 0 for finite result
# At order k1²: bracket → k1²·(2c2 + 4c5 + 2c6)
# Then BNL_sq = (10/3) × prefactor × (2c2+4c5+2c6)/2 = (10/3)·prefactor·(c2+2c5+c6)

print("ANALYTICAL CONSTRAINTS:")
print(f"  (1) c1+c2+c3+c4 = 0  [finiteness in squeezed limit]")
print(f"  (2) (10/3)·pf·(c2+2c5+c6) = {target_sq}")
print(f"  (3) (10/3)·(pf/1)·(3c1+6(c2+c3+c4+c5+c6))/3 = {target_eq}")
print()

# Try different prefactors
for pf_num, pf_den in [(3,256), (1,256), (9,256), (3,128), (3,64)]:
    pf = pf_num / pf_den

    # From constraint 2:
    # (10/3)·pf·(c2+2c5+c6) = -35/8
    target_combo = target_sq * 3 / (10 * pf)

    # From constraint 3 (equilateral, all sums = 3 or 6):
    # AT(eq) = pf·(3c1+6c2+6c3+6c4+6c5+6c6)
    # BNL(eq) = (10/3)·pf·(3c1+6c2+6c3+6c4+6c5+6c6)/3
    # Using c4=-(c1+c2+c3): 6c4 = -6c1-6c2-6c3
    # bracket_eq = 3c1+6c2+6c3-6c1-6c2-6c3+6c5+6c6 = -3c1+6(c5+c6)
    # BNL(eq) = (10/9)·pf·(-3c1+6(c5+c6))
    target_eq_combo = target_eq * 9 / (10 * pf)  # = -3c1+6(c5+c6)

    print(f"Prefactor = {pf_num}/{pf_den} = {pf:.6f}:")
    print(f"  c2+2c5+c6 = {target_combo:.4f}")
    print(f"  -3c1+6(c5+c6) = {target_eq_combo:.4f}")

    # Try standard coefficients from Eq. 37
    for c5_try in range(-70, -50):
        for c6_try in range(0, 20):
            # c2 from constraint 2
            c2_try = target_combo - 2*c5_try - c6_try
            if abs(c2_try - round(c2_try)) > 0.01:
                continue
            c2_try = round(c2_try)

            # c1 from constraint 3
            c1_val = (6*(c5_try+c6_try) - target_eq_combo) / 3
            if abs(c1_val - round(c1_val)) > 0.01:
                continue
            c1_try = round(c1_val)

            # c4 from constraint 1
            # c3 is free, c4 = -(c1+c2+c3)
            # Use folded to determine c3

            for c3_try in range(-15, 15):
                c4_try = -(c1_try + c2_try + c3_try)
                coeffs = [c1_try, c2_try, c3_try, c4_try, c5_try, c6_try]

                bnl_sq = BNL(coeffs, pf, 1e-6, 1, 1)
                bnl_eq = BNL(coeffs, pf, 1, 1, 1)
                bnl_fold = BNL(coeffs, pf, 1, 0.5, 0.5)

                err = (bnl_sq - target_sq)**2 + (bnl_eq - target_eq)**2 + (bnl_fold - target_fold)**2
                if err < 0.01:
                    print(f"  *** MATCH: c=({c1_try},{c2_try},{c3_try},{c4_try},{c5_try},{c6_try})")
                    print(f"      BNL_sq={bnl_sq:.6f} (target {target_sq})")
                    print(f"      BNL_eq={bnl_eq:.6f} (target {target_eq})")
                    print(f"      BNL_fold={bnl_fold:.6f} (target {target_fold})")
    print()
