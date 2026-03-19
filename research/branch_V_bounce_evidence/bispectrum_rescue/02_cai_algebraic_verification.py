#!/usr/bin/env python3
"""
Algebraic verification of Cai et al. (0903.0631) Eq. 38: |B|_NL = -35/8
by evaluating their shape function contributions (Eqs. 28, 31, 32, 33)
individually and summing in the squeezed limit.

Uses exact floating-point arithmetic (no integration needed).
"""
import numpy as np
from itertools import permutations

eps = 1.5  # ε = 3/2

def compute_sums(k1, k2, k3):
    """Compute all required momentum sums for Cai's shape functions."""
    ks = [k1, k2, k3]

    # Σ kᵢ^a (sum over i=1,2,3)
    def S1(a): return sum(k**a for k in ks)

    # Σ_{i≠j} kᵢ^a kⱼ^b (ordered pairs, 6 terms)
    def S2(a, b):
        return sum(ks[i]**a * ks[j]**b for i in range(3) for j in range(3) if i != j)

    # Σ_{i≠j≠k} kᵢ^a kⱼ^b kₖ^c (all three distinct, 6 terms)
    def S3(a, b, c):
        return sum(ks[i]**a * ks[j]**b * ks[l]**c
                   for i in range(3) for j in range(3) for l in range(3)
                   if i != j and j != l and i != l)

    prod_k2 = k1**2 * k2**2 * k3**2
    return S1, S2, S3, prod_k2


def A_red(k1, k2, k3):
    """
    Field redefinition contribution (Cai Eq. 28).

    Ared = (-ε/2 + ε/8)Σk³ + (ε²/32)Σkᵢkⱼ²
           - (ε²/(32·Πk²)){Σk⁷k² + Σk⁶k³ - 2Σk⁵k⁴ - 2Σk⁵k²k² - Σk⁴k³k²}
    """
    S1, S2, S3, pk2 = compute_sums(k1, k2, k3)

    part1 = (-eps/2 + eps/8) * S1(3)
    part2 = (eps**2 / 32) * S2(1, 2)
    bracket = S2(7, 2) + S2(6, 3) - 2*S2(5, 4) - 2*S3(5, 2, 2) - S3(4, 3, 2)
    part3 = -(eps**2 / (32 * pk2)) * bracket

    return part1 + part2 + part3


def A_zeta_zdot2(k1, k2, k3):
    """
    ζζ̇² vertex contribution (Cai Eq. 31).

    A = (-ε²/12 + ε³/24) Σk³
    """
    S1, _, _, _ = compute_sums(k1, k2, k3)
    return (-eps**2/12 + eps**3/24) * S1(3)


def A_zdot_dz_dchi(k1, k2, k3):
    """
    ζ̇(∂ζ)(∂χ) vertex contribution (Cai Eq. 32).

    A = (ε²/(24·Πk²)) {2Σk⁷k² - 2Σk⁵k⁴ - Σk⁵k²k²}

    Note: this comes from the raw text "ǫ2/(24 Q ki2)" with the bracket terms.
    """
    S1, S2, S3, pk2 = compute_sums(k1, k2, k3)
    bracket = 2*S2(7, 2) - 2*S2(5, 4) - S3(5, 2, 2)
    return (eps**2 / (24 * pk2)) * bracket


def A_zeta_didj_chi2(k1, k2, k3):
    """
    ζ(∂ᵢ∂ⱼχ)² vertex contribution (Cai Eq. 33).

    A = (ε³/(96·Πk²)) {Σk⁹ - 3Σk⁷k² - Σk⁶k³ + 3Σk⁵k⁴ - Σk⁵k²k² + Σk⁴k³k²}
    """
    S1, S2, S3, pk2 = compute_sums(k1, k2, k3)
    bracket = S1(9) - 3*S2(7, 2) - S2(6, 3) + 3*S2(5, 4) - S3(5, 2, 2) + S3(4, 3, 2)
    return (eps**3 / (96 * pk2)) * bracket


def BNL(k1, k2, k3):
    """Compute |B|_NL from total A_T via Cai Eq. 21."""
    AT = A_red(k1, k2, k3) + A_zeta_zdot2(k1, k2, k3) + \
         A_zdot_dz_dchi(k1, k2, k3) + A_zeta_didj_chi2(k1, k2, k3)
    sum_k3 = k1**3 + k2**3 + k3**3
    return (10.0/3.0) * AT / sum_k3


if __name__ == "__main__":
    print("=" * 65)
    print("VERIFICATION OF CAI ET AL. Eq. 38: |B|_NL = -35/8")
    print("=" * 65)

    print("\n--- Individual contributions in squeezed limit ---")
    print("k1 → 0, k2 = k3 = 1\n")

    for k1 in [0.1, 0.01, 0.001, 1e-4, 1e-5, 1e-6]:
        ar = A_red(k1, 1, 1)
        a1 = A_zeta_zdot2(k1, 1, 1)
        a2 = A_zdot_dz_dchi(k1, 1, 1)
        a3 = A_zeta_didj_chi2(k1, 1, 1)
        at = ar + a1 + a2 + a3
        bnl = BNL(k1, 1, 1)
        print(f"k1={k1:.1e}: Ared={ar:+12.4f}  Azz2={a1:+8.4f}  "
              f"Azdz={a2:+12.4f}  Adidj={a3:+12.4f}  "
              f"AT={at:+12.4f}  |B|_NL={bnl:+10.6f}")

    print(f"\nTarget: |B|_NL = -35/8 = {-35/8:.6f}")

    # Also check special shapes
    print("\n--- Special shapes ---")
    # Equilateral: k1 = k2 = k3 = 1
    bnl_eq = BNL(1, 1, 1)
    print(f"Equilateral (1,1,1): |B|_NL = {bnl_eq:.6f}  (Cai Eq. 40: {-255/64:.6f})")

    # Folded: k1 = 2k2 = 2k3, so k1=1, k2=k3=0.5
    bnl_fold = BNL(1, 0.5, 0.5)
    print(f"Folded (1,0.5,0.5):  |B|_NL = {bnl_fold:.6f}  (Cai Eq. 41: {-9/4:.6f})")
