#!/usr/bin/env python3
"""
Full shape projection of the matter-bounce bispectrum onto the local template.

Computes the cosine overlap cos(θ) = <S_MB, S_local> / (|S_MB| · |S_local|)
where the inner product integrates over the allowed triangle domain.

The matter-bounce shape function S_MB(k₁,k₂,k₃) = AT / (k₁k₂k₃) where
AT = (3/(256·k₁²k₂²k₃²)) × {polynomial}.

The local template shape function S_local(k₁,k₂,k₃) ∝ 1/(k₁³k₂³) + 2 perms.

Convention: the inner product is ∫ S₁·S₂ · w(k₁,k₂,k₃) dk₁dk₂dk₃
where w is a weight function. Standard choice: w = (k₁k₂k₃)² (Babich et al. 2004).
"""
import numpy as np
from itertools import permutations

# ============================================================
# SHAPE FUNCTIONS
# ============================================================

def AT_matter_bounce(k1, k2, k3):
    """
    Cai et al. total shape function AT(k1,k2,k3).
    Uses verified coefficient set (4,5,-9,0,-68,19) with prefactor 3/(256·Πk²).
    """
    ks = [k1, k2, k3]
    pk2 = k1**2 * k2**2 * k3**2

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

    c1, c2, c3, c4, c5, c6 = 4, 5, -9, 0, -68, 19
    bracket = c1*s9 + c2*s72 + c3*s63 + c4*s54 + c5*s522 + c6*s432
    return (3.0 / (256 * pk2)) * bracket


def shape_matter_bounce(k1, k2, k3):
    """
    Matter-bounce bispectrum shape S_MB = AT / (k1*k2*k3).
    Normalized for the cosine inner product with weight (k1*k2*k3)^2.
    """
    return AT_matter_bounce(k1, k2, k3) / (k1 * k2 * k3)


def shape_local(k1, k2, k3):
    """
    Local template shape: S_local ∝ 1/(k1³k2³) + 1/(k1³k3³) + 1/(k2³k3³).
    This is the standard Babich-Creminelli-Zaldarriaga template.
    """
    return 1.0/(k1**3 * k2**3) + 1.0/(k1**3 * k3**3) + 1.0/(k2**3 * k3**3)


def shape_equilateral(k1, k2, k3):
    """Equilateral template for comparison."""
    K = k1 + k2 + k3
    return -1.0/(k1**3 * k2**3) - 1.0/(k1**3 * k3**3) - 1.0/(k2**3 * k3**3) \
           - 2.0/(k1**2 * k2**2 * k3**2) \
           + 1.0/(k1 * k2**2 * k3**3) + 5.0 # simplified — using the actual template below
    # Actually, let's use the Creminelli et al. form properly
    p1 = k1*k2*k3
    p2 = k1*k2 + k1*k3 + k2*k3
    p3 = k1 + k2 + k3
    # The equilateral template from Creminelli et al. 2006:
    return (-6.0 * (1.0/(k1**3*k2**3) + 1.0/(k1**3*k3**3) + 1.0/(k2**3*k3**3))
            - 6.0 * 1.0/(k1**2*k2**2*k3**2)
            + 6.0 * (1.0/(k1*k2**2*k3**3) + 1.0/(k1**2*k2*k3**3) + 1.0/(k1*k2**3*k3**2)
                   + 1.0/(k1**2*k2**3*k3) + 1.0/(k1**3*k2*k3**2) + 1.0/(k1**3*k2**2*k3)))


# ============================================================
# INNER PRODUCT OVER TRIANGLE DOMAIN
# ============================================================

def compute_overlap(shape1, shape2, n_points=200, k_min_ratio=0.01):
    """
    Compute the cosine overlap between two shapes over the triangle domain.

    Uses the parametrization k₂ = x·k₃, k₁ = y·k₃ with k₃ = 1 (scale-free),
    and the triangle inequality: |k₂-k₃| ≤ k₁ ≤ k₂+k₃.

    Weight: w = (k₁k₂k₃)² (standard choice from Babich et al.).
    The integral is: ∫∫ S₁·S₂ · (k₁k₂k₃)² dk₁dk₂ over the allowed domain.

    We parametrize: k₃ = 1 (WLOG by scale invariance), k₂ ∈ [k_min, 1], k₁ ∈ [1-k₂, k₂].
    The ordering k₁ ≤ k₂ ≤ k₃ = 1 avoids double-counting.
    """
    k3 = 1.0
    k2_min = k_min_ratio  # avoid degenerate triangles
    k2_max = 1.0

    # Use 2D numerical integration with the trapezoidal rule
    k2_arr = np.linspace(k2_min, k2_max, n_points)
    dk2 = k2_arr[1] - k2_arr[0]

    ip_12 = 0.0  # <shape1, shape2>
    ip_11 = 0.0  # <shape1, shape1>
    ip_22 = 0.0  # <shape2, shape2>

    for k2 in k2_arr:
        # Triangle inequality: |k2 - k3| <= k1 <= k2 + k3
        # With ordering k1 <= k2 <= k3=1:
        k1_min = max(k_min_ratio, 1.0 - k2)  # triangle inequality lower bound
        k1_max = k2  # ordering constraint k1 <= k2

        if k1_max <= k1_min:
            continue

        k1_arr = np.linspace(k1_min, k1_max, n_points)
        dk1 = k1_arr[1] - k1_arr[0] if len(k1_arr) > 1 else 0

        for k1 in k1_arr:
            try:
                s1 = shape1(k1, k2, k3)
                s2 = shape2(k1, k2, k3)
                w = (k1 * k2 * k3)**2

                ip_12 += s1 * s2 * w * dk1 * dk2
                ip_11 += s1 * s1 * w * dk1 * dk2
                ip_22 += s2 * s2 * w * dk1 * dk2
            except (ZeroDivisionError, FloatingPointError):
                continue

    norm1 = np.sqrt(ip_11)
    norm2 = np.sqrt(ip_22)

    if norm1 == 0 or norm2 == 0:
        return 0.0, ip_12, ip_11, ip_22

    cosine = ip_12 / (norm1 * norm2)
    return cosine, ip_12, ip_11, ip_22


if __name__ == "__main__":
    print("=" * 65)
    print("MATTER-BOUNCE SHAPE PROJECTION ONTO LOCAL TEMPLATE")
    print("=" * 65)

    # Quick sanity: check shape values at benchmark points
    print("\n--- Shape function sanity checks ---")
    for name, k1, k2, k3 in [("Squeezed", 0.001, 1, 1), ("Equilateral", 1, 1, 1), ("Folded", 1, 0.5, 0.5)]:
        AT = AT_matter_bounce(k1, k2, k3)
        sk3 = k1**3 + k2**3 + k3**3
        BNL = (10.0/3.0) * AT / sk3
        print(f"  {name:12s}: |B|_NL = {BNL:+.4f}")
    print(f"  Targets: sq=-4.375, eq=-3.984, fold=-2.250")

    # Main computation: cosine overlap with local template
    print("\n--- Shape projection computation ---")
    print("Computing overlap integral over triangle domain...")

    # Convergence study
    print("\n  Resolution convergence:")
    for n in [50, 100, 150, 200]:
        cos_theta, _, _, _ = compute_overlap(shape_matter_bounce, shape_local, n_points=n, k_min_ratio=0.01)
        print(f"    n={n:4d}  cos(θ) = {cos_theta:.6f}")

    # k_min sensitivity
    print("\n  Squeezed-limit cutoff sensitivity:")
    for k_min in [0.1, 0.05, 0.02, 0.01, 0.005]:
        cos_theta, _, _, _ = compute_overlap(shape_matter_bounce, shape_local, n_points=150, k_min_ratio=k_min)
        print(f"    k_min/k_max = {k_min:.3f}  cos(θ) = {cos_theta:.6f}")

    # Best estimate
    print("\n--- BEST ESTIMATE ---")
    cos_best, ip12, ip11, ip22 = compute_overlap(shape_matter_bounce, shape_local, n_points=200, k_min_ratio=0.005)
    print(f"  cos(θ) = {cos_best:.6f}")
    print(f"  f_NL^eff = f_NL × cos(θ) = {-4.375 * cos_best:.4f}")
    print(f"  Signal reduction from non-local shape: {(1-cos_best)*100:.1f}%")

    # Effective significance
    print("\n--- SIGNIFICANCE IMPACT ---")
    for sigma_fnl in [0.3, 0.5, 1.0, 1.5, 2.5]:
        sig = abs(-4.375 * cos_best) / sigma_fnl
        print(f"  σ(f_NL) = {sigma_fnl:.1f}  →  significance = {sig:.1f}σ")

    print("\nDone.")
