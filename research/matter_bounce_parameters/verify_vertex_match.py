#!/usr/bin/env python3
"""
Verify that individual vertex contributions match between
Cai et al. (0903.0631) and Li et al. (1612.02036) at c_s = 1.

If they match term-by-term but the total A differs by 2 in the
squeezed limit, the factor of 2 is in how the polynomial terms
combine — a normalization convention, not a physics error.
"""
import numpy as np

eps = 1.5
cs = 1.0

print("="*65)
print("VERTEX-BY-VERTEX COMPARISON: Cai vs Li at c_s = 1, eps = 3/2")
print("="*65)

# We compare the coefficient of Σk_i³ for each vertex
# (the "local-like" part that dominates the squeezed limit)

# ─── Cai Eq. (28) bottom: A_red ───
# A_red = (-eps/2 + eps^2/8) Σk³ + ...
cai_red_coeff = -eps/2 + eps**2/8
print(f"\n1. Field redefinition (Σk³ coefficient):")
print(f"   Cai Eq.(28): (-ε/2 + ε²/8) = {cai_red_coeff:.6f}")

# ─── Li Eq. (4.12): A_redef ───
# A_redef = (3ε/16 - 3/(4c_s²)) Σk³ + ...
li_red_coeff = 3*eps/16 - 3/(4*cs**2)
print(f"   Li  Eq.(4.12): (3ε/16 - 3/(4c_s²)) = {li_red_coeff:.6f}")
print(f"   MATCH: {np.isclose(cai_red_coeff, li_red_coeff)}")

# ─── Cai Eq. (31): A_ζζ̇² ───
# A_ζζ̇² = (-ε²/12 + ε³/24) Σk³
cai_zzdot_coeff = -eps**2/12 + eps**3/24
print(f"\n2. ζζ̇² vertex (Σk³ coefficient):")
print(f"   Cai Eq.(31): (-ε²/12 + ε³/24) = {cai_zzdot_coeff:.6f}")

# ─── Li Eq. (4.14): A_ζζ̇² ───
# A_ζζ̇² = -(c_s²/8)[1/c_s⁴(ε-3+3c_s²) - ε²/2] Σk³
li_zzdot_coeff = -(cs**2/8) * (1/cs**4 * (eps - 3 + 3*cs**2) - eps**2/2)
print(f"   Li  Eq.(4.14): -(c_s²/8)[...] = {li_zzdot_coeff:.6f}")
print(f"   MATCH: {np.isclose(cai_zzdot_coeff, li_zzdot_coeff)}")

# ─── Cai Eq. (32): A_ζ̇∂ζ∂χ (Σk³ part) ───
# From Eq. (32) bottom line: A = -ε²/12 Σk³ + ...
cai_zdzdchi_coeff = -eps**2/12
print(f"\n3. ζ̇∂ζ∂χ vertex (Σk³ coefficient):")
print(f"   Cai Eq.(32): (-ε²/12) = {cai_zdzdchi_coeff:.6f}")

# ─── Li Eq. (4.15): A_ζ̇∂ζ∂χ ───
# A = -(ε/8) Σk³ + ... (momentum-dep terms)
li_zdzdchi_coeff = -eps/8
print(f"   Li  Eq.(4.15): (-ε/8) = {li_zdzdchi_coeff:.6f}")
print(f"   MATCH: {np.isclose(cai_zdzdchi_coeff, li_zdzdchi_coeff)}")

# ─── Cai Eq. (33): A_ζ(∂ᵢ∂ⱼχ)² (Σk³ part) ───
# From Eq. (33) bottom line: A = -ε³/48 Σk³ + ...
cai_didj_coeff = -eps**3/48
print(f"\n4. ζ(∂ᵢ∂ⱼχ)² vertex (Σk³ coefficient):")
print(f"   Cai Eq.(33): (-ε³/48) = {cai_didj_coeff:.6f}")

# ─── Li Eq. (4.16): A_ζ(∂ᵢ∂ⱼχ)² ───
# A = -(c_s²ε²/32) Σk³ + ...
li_didj_coeff = -(cs**2 * eps**2) / 32
print(f"   Li  Eq.(4.16): (-(c_s²ε²)/32) = {li_didj_coeff:.6f}")
print(f"   MATCH: {np.isclose(cai_didj_coeff, li_didj_coeff)}")

# ─── Li Eq. (4.18): A_ζ̇³ (new term, only for c_s ≠ 1) ───
# A_ζ̇³ = -(9/2)(1 - 1/c_s² + 2λ/Σ) Σk³
# At c_s = 1: λ/Σ = (1-c_s²)/(6c_s²) = 0
li_zdot3_coeff = -(9.0/2) * (1 - 1/cs**2 + 2*(1-cs**2)/(6*cs**2))
print(f"\n5. ζ̇³ vertex (only Li, vanishes at c_s=1):")
print(f"   Li  Eq.(4.18): = {li_zdot3_coeff:.6f}")
print(f"   Vanishes: {np.isclose(li_zdot3_coeff, 0.0)}")

# ─── Total Σk³ coefficient ───
print(f"\n{'='*65}")
print(f"TOTAL Σk³ COEFFICIENTS:")
cai_total = cai_red_coeff + cai_zzdot_coeff + cai_zdzdchi_coeff + cai_didj_coeff
li_total = li_red_coeff + li_zzdot_coeff + li_zdzdchi_coeff + li_didj_coeff + li_zdot3_coeff

print(f"   Cai:  {cai_total:.6f}")
print(f"   Li:   {li_total:.6f}")
print(f"   Ratio Cai/Li: {cai_total/li_total:.4f}")
print(f"   Match: {np.isclose(cai_total, li_total)}")

# ─── Squeezed limit check ───
print(f"\n{'='*65}")
print(f"SQUEEZED LIMIT:")
print(f"   Cai Eq.(44): A_T|_sq = -(21/8)k³ = {-21/8:.6f} k³")

# For Li, from Eq. (4.23) at c_s=1:
# F ≃ (3/8)(-33/2 + 13/c_s²)(k/k_1)
li_F_coeff = (3.0/8) * (-33.0/2 + 13.0/cs**2)
print(f"   Li Eq.(4.23): F ≃ {li_F_coeff:.6f} × (k/k₁)")
print(f"   Since F = A_tot/(k₁k₂k₃) and k₂=k₃=k:")
print(f"   A_tot|_sq = {li_F_coeff:.6f} × k³")
print(f"")
print(f"   Ratio: A_T(Cai) / A_tot(Li) = {(-21/8) / li_F_coeff:.4f}")

# ─── f_NL from each ───
cai_fnl = (10.0/3) * (-21.0/8) / 2  # /2 because Σk³ = 2k³ in squeezed
li_fnl = (10.0/3) * li_F_coeff / 2
print(f"\n   f_NL (Cai):  (10/3)×(-21/8)/(2) = {cai_fnl:.4f}")
print(f"   f_NL (Li):   (10/3)×({li_F_coeff:.4f})/(2) = {li_fnl:.4f}")
print(f"   Ratio: {cai_fnl/li_fnl:.4f}")

print(f"\n{'='*65}")
print(f"DIAGNOSIS:")
if np.isclose(cai_total, li_total, rtol=0.01):
    print(f"   Individual vertex Σk³ coefficients: MATCH")
    print(f"   But squeezed-limit A differs by factor {(-21/8)/li_F_coeff:.2f}")
    print(f"   → Difference is in the MOMENTUM-DEPENDENT terms")
    print(f"     (the k⁷k², k⁶k³, etc. polynomials), not the")
    print(f"     Σk³ local-like piece.")
else:
    print(f"   Vertex Σk³ coefficients DO NOT match!")
    ratio = cai_total / li_total
    print(f"   Ratio: {ratio:.4f}")
    print(f"   The factor of 2 enters at the individual vertex level.")
    if np.isclose(ratio, 2.0, rtol=0.01):
        print(f"   → Clean factor of 2 in the vertex prefactors.")
        print(f"   → Likely: different mode function normalization")
        print(f"     or different convention for A in Eq.(19) vs Eq.(4.9).")
