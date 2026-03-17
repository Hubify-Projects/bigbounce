#!/usr/bin/env python3
"""
Computation 3: Fierz Rearrangement of the Torsion-Induced Four-Fermion Interaction
===================================================================================

Reference: Canonical Problem Statement §Q4–Q5 (frozen v3)
Input: L_4f = -G_eff (J^μ)² where J^μ = ψ̄γ^μγ⁵ψ + (1/γ)ψ̄γ^μψ
Output: Channel decomposition into scalar/pseudoscalar/vector/axial/tensor

THIS IS THE FIRST MAKE-OR-BREAK COMPUTATION.
It determines whether Q5 Possibility A or B is realized.

Status: EXACT (Fierz identities are algebraic identities)

Key references:
  - Fierz (1937) — original rearrangement theorem
  - Nieves & Pal (2003) — complete Fierz identity tables
  - Buballa (2005) — NJL review with Fierz for color+flavor
  - Klevansky (1992) — NJL review, Fierz in 4D
"""

import sympy as sp
from sympy import Rational, Matrix, eye, symbols, simplify, sqrt, latex

print("=" * 70)
print("COMPUTATION 3: FIERZ REARRANGEMENT")
print("Torsion-induced four-fermion interaction → channel decomposition")
print("=" * 70)

# =============================================================================
# FIERZ IDENTITIES IN 4D
# =============================================================================
#
# The complete basis of 4×4 matrices in Dirac space is:
#   Γ_A = {1, γ⁵, γ^μ, γ^μγ⁵, σ^{μν}}
#   with dimensions {1, 1, 4, 4, 6} = 16 total
#
# The Fierz identity for rearranging (ψ̄₁ Γ_A ψ₂)(ψ̄₃ Γ_B ψ₄)
# into (ψ̄₁ Γ_C ψ₄)(ψ̄₃ Γ_D ψ₂) is:
#
#   (ψ̄₁ Γ_A ψ₂)(ψ̄₃ Γ_B ψ₄) = Σ_{C,D} F_{AB}^{CD} (ψ̄₁ Γ_C ψ₄)(ψ̄₃ Γ_D ψ₂)
#
# For IDENTICAL fermions (ψ₁ = ψ₂ = ψ₃ = ψ₄ = ψ), we need the
# self-rearrangement:
#
#   (ψ̄ Γ_A ψ)(ψ̄ Γ_B ψ) = Σ_C F_{AB}^{C} (ψ̄ Γ_C ψ)²
#
# The standard Fierz matrix for identical fermions (same flavor, same color)
# in 4D is:
#
# Convention: rows/columns labeled by S, P, V, A, T
# where S = 1, P = iγ⁵, V = γ^μ, A = γ^μγ⁵, T = σ^{μν}/√2
#
# The Fierz matrix F such that:
#   (ψ̄ Γ_a ψ)(ψ̄ Γ_b ψ) → Σ_c F_{ab,c} (ψ̄ Γ_c ψ)(ψ̄ Γ_c ψ)
#
# Wait — for identical fermions, the Fierz rearrangement of a current-current
# interaction is more specific. Let me be precise.
#
# We need to Fierz-rearrange:
#   (ψ̄ γ^μ Γ ψ)(ψ̄ γ_μ Γ' ψ)
# where Γ, Γ' ∈ {1, γ⁵}
#
# The standard Fierz identity for vector-type currents:
#
#   (ψ̄ γ^μ ψ)(ψ̄ γ_μ ψ) =
#       -(ψ̄ψ)² - (ψ̄iγ⁵ψ)² + (1/2)(ψ̄σ^{μν}ψ)²
#       [for a single Dirac fermion with N_c colors]
#
# But the exact coefficients depend on:
#   1. Whether we include color (N_c) factors
#   2. Whether we use Fierz for (12)(34) → (14)(32) or (13)(24)
#   3. Sign conventions for γ⁵

# =============================================================================
# THE FIERZ TABLE WE NEED
# =============================================================================
#
# For a SINGLE Dirac fermion (N_c colors summed externally), the
# standard NJL Fierz identities are:
#
# (ψ̄γ^μψ)(ψ̄γ_μψ) = -(ψ̄ψ)² - (ψ̄iγ⁵ψ)² + (1/2)(ψ̄σ^{μν}ψ)²
#
# (ψ̄γ^μγ⁵ψ)(ψ̄γ_μγ⁵ψ) = -(ψ̄ψ)² - (ψ̄iγ⁵ψ)² + (1/2)(ψ̄σ^{μν}ψ)²
#
# (ψ̄γ^μψ)(ψ̄γ_μγ⁵ψ) = +(ψ̄ψ)(ψ̄iγ⁵ψ) + (ψ̄iγ⁵ψ)(ψ̄ψ)
#                          - (1/2)(ψ̄σ^{μν}ψ)(ψ̄σ_{μν}iγ⁵ψ)
#
# WAIT — I need to be much more careful here.
# Let me derive the Fierz identities from first principles.
#
# The Fierz rearrangement theorem states:
#
# (ψ̄_α Γ^A_{αβ} ψ_β)(ψ̄_γ Γ^B_{γδ} ψ_δ)
#   = -Σ_C (1/4) tr(Γ^A Γ^C Γ^B Γ_C) × (ψ̄_α Γ^C_{αδ} ψ_δ)(ψ̄_γ (Γ_C)_{γβ} ψ_β)
#
# For identical fermions ψ₁ = ψ₂ = ψ₃ = ψ₄, the minus sign comes from
# the anticommutation needed to rearrange the fermion fields.

print("\n--- Fierz identity derivation ---")
print()
print("Strategy: derive the Fierz coefficients from the trace formula")
print("and apply to the specific current structure J^μ = A^μ + (1/γ)V^μ")
print()

# =============================================================================
# FIERZ COEFFICIENTS FROM TRACE FORMULA
# =============================================================================
#
# The complete Dirac basis (normalized):
#   Γ^S = 1           (1 component)
#   Γ^P = iγ⁵         (1 component)
#   Γ^V_μ = γ_μ       (4 components)
#   Γ^A_μ = γ_μγ⁵     (4 components)
#   Γ^T_{μν} = σ_{μν}/√2  (6 components)
#
# Normalization: tr(Γ^a Γ^b) = 4 δ^{ab}  (for the scalar/pseudoscalar)
#                tr(γ^μ γ^ν) = 4 g^{μν}
#                etc.
#
# The Fierz rearrangement for a product of two bilinears with
# the SAME fermion field (i.e., exchange identity) is:
#
# (ψ̄ M ψ)(ψ̄ N ψ) = -(1/4) Σ_a c_a tr(M Γ^a N Γ_a) × (ψ̄ Γ^a ψ)(ψ̄ Γ_a ψ)
#
# where c_a = 1/n_a with n_a being the number of components:
#   c_S = 1, c_P = 1, c_V = 1/4, c_A = 1/4, c_T = 1/6
#
# Actually, let me use the standard formulation more carefully.
#
# The key identity (Itzykson & Zuber, eq. 2-79; Klevansky 1992, Appendix):
#
# For EXCHANGE Fierz (rearranging 12 × 34 → 14 × 32):
#
# δ_{αδ} δ_{γβ} = (1/4) Σ_A (Γ^A)_{αβ} (Γ_A)_{γδ}
#
# where the sum is over the complete basis with normalization
# tr(Γ^A Γ^B) = 4δ^{AB}.
#
# Applied to (ψ̄ M ψ)(ψ̄ N ψ):
#
# (ψ̄_α M_{αβ} ψ_β)(ψ̄_γ N_{γδ} ψ_δ)
# = -ψ̄_α M_{αβ} N_{γδ} ψ_δ ψ̄_γ ψ_β   [anticommute ψψ̄]
# = -(1/4) Σ_A ψ̄_α M_{αβ} (Γ_A)_{γβ'} N_{γ'δ} ψ_δ δ_{ββ'} δ_{γγ'} ...
#
# This is getting complicated with indices. Let me just USE the known
# results for the specific cases we need.

# =============================================================================
# STANDARD FIERZ RESULTS FOR VECTOR AND AXIAL CURRENTS
# =============================================================================
#
# The following are standard results (see e.g., Klevansky 1992, Buballa 2005):
#
# For a single flavor, single color Dirac fermion:
#
# (VV): (ψ̄γ^μψ)(ψ̄γ_μψ) Fierz→
#   = -(ψ̄ψ)² - (ψ̄iγ⁵ψ)² + (1/2)(ψ̄γ^μψ)(ψ̄γ_μψ)
#     + (1/2)(ψ̄γ^μγ⁵ψ)(ψ̄γ_μγ⁵ψ) + 0×(tensor)
#
# WAIT — that can't be right because it's circular (VV on both sides).
#
# The issue is that for identical fermions, the Fierz rearrangement
# gives BACK the same type of expressions. We need to be more careful.
#
# Let me approach this differently.
#
# For the NJL model, what we actually need is the MEAN-FIELD decomposition
# (Hubbard-Stratonovich), not just Fierz identities. The HS transformation
# requires that we identify which channels (S, P, V, A, T) the interaction
# can be decomposed into.
#
# For a general four-fermion interaction L = G(ψ̄Γ_Aψ)(ψ̄Γ_Bψ),
# the HS decomposition introduces auxiliary fields for each channel
# that has an attractive (negative coefficient) interaction.
#
# The key mathematical identity we need is:
#
# For the CURRENT-CURRENT interaction (J^μ)(J_μ) where J has both V and A parts:
#
# J^μ = ψ̄γ^μγ⁵ψ + (1/γ)ψ̄γ^μψ
#
# (J^μ)(J_μ) = (ψ̄γ^μγ⁵ψ)² + (2/γ)(ψ̄γ^μγ⁵ψ)(ψ̄γ_μψ) + (1/γ²)(ψ̄γ^μψ)²
#
# We need to Fierz-rearrange each of these three terms into S, P, T channels.

print("=" * 70)
print("FIERZ REARRANGEMENT: CURRENT-CURRENT → SCALAR CHANNELS")
print("=" * 70)
print()
print("The four-fermion interaction is:")
print("  L_4f = -G_eff × (J^μ)(J_μ)")
print("  J^μ = ψ̄γ^μγ⁵ψ + (1/γ)ψ̄γ^μψ")
print()
print("We need to Fierz-rearrange (J^μ)(J_μ) into scalar channels")
print("suitable for Hubbard-Stratonovich decomposition.")
print()

# =============================================================================
# FIERZ IDENTITIES: THE CORRECT APPROACH
# =============================================================================
#
# The standard Fierz identity for 4D Dirac matrices:
#
# (ψ̄₁ Γ^A ψ₂)(ψ̄₃ Γ^B ψ₄) = Σ_CD F^{CD}_{AB} (ψ̄₁ Γ^C ψ₄)(ψ̄₃ Γ^D ψ₂)
#
# where the Fierz matrix is:
#
# F^{CD}_{AB} = -(1/16) tr(Γ^C Γ^A Γ^D Γ^B)
#
# For IDENTICAL fermions (all ψ's the same), we set ψ₁=ψ₂=ψ₃=ψ₄=ψ
# and get:
#
# (ψ̄ Γ^A ψ)(ψ̄ Γ^B ψ) = -Σ_{CD} (1/16) tr(Γ^C Γ^A Γ^D Γ^B) (ψ̄ Γ^C ψ)(ψ̄ Γ^D ψ)
#
# The minus sign is from fermion anticommutation.
#
# For our case, we need three specific identities:
# 1. Γ^A = γ^μ, Γ^B = γ_μ  (VV contraction)
# 2. Γ^A = γ^μγ⁵, Γ^B = γ_μγ⁵  (AA contraction)
# 3. Γ^A = γ^μ, Γ^B = γ_μγ⁵  (VA cross-term)
#
# Using the standard trace technology in 4D:

print("Computing Fierz coefficients using trace technology...")
print()

# The basis elements (with their Lorentz-contracted forms for current-current):
# After contraction over μ, we have scalars in Dirac space.
#
# γ^μ γ_μ = 4·1                    (VV contraction)
# γ^μγ⁵ γ_μγ⁵ = γ^μ γ_μ = 4·1     (AA contraction, using {γ⁵,γ^μ}=0)
#
# Wait, let me be careful:
# (ψ̄γ^μγ⁵ψ)(ψ̄γ_μγ⁵ψ) means γ^μγ⁵ ⊗ γ_μγ⁵ in the (12)⊗(34) space
# The Fierz rearrangement mixes the spinor indices.
#
# Actually, for the mean-field / HS decomposition, we don't strictly need
# the full Fierz rearrangement. We need to identify which BILINEAR channels
# the interaction couples to.
#
# The standard NJL approach (Klevansky 1992, §2.2):
#
# For pure axial-axial: (ψ̄γ^μγ⁵ψ)²
#   Fierz → +(ψ̄ψ)² + (ψ̄iγ⁵ψ)² - (1/2)(ψ̄γ^μψ)² - (1/2)(ψ̄γ^μγ⁵ψ)²
#
# For pure vector-vector: (ψ̄γ^μψ)²
#   Fierz → +(ψ̄ψ)² + (ψ̄iγ⁵ψ)² - (1/2)(ψ̄γ^μψ)² - (1/2)(ψ̄γ^μγ⁵ψ)²
#
# THESE ARE THE SAME! The AA and VV have identical Fierz rearrangements
# into scalar channels (for identical fermions).
#
# Reference: Klevansky, Rev. Mod. Phys. 64, 649 (1992), eq. (2.8)-(2.10)
#
# For the cross-term: (ψ̄γ^μψ)(ψ̄γ_μγ⁵ψ)
#   Fierz → -2(ψ̄ψ)(ψ̄iγ⁵ψ) + (tensor terms)
#
# Let me now do this properly using explicit Fierz tables.

# =============================================================================
# THE STANDARD FIERZ IDENTITY TABLE (Klevansky 1992)
# =============================================================================
#
# For a single-flavor Dirac fermion, the Fierz rearrangement of
# current-current interactions into scalar channels is given by
# the matrix equation:
#
# | (SS) |     | 1    1   -1/2  -1/2  1/8  |   | (SS) |
# | (PP) |     | 1    1   -1/2  -1/2  1/8  |   | (PP) |
# | (VV) | = - | -2  -2    1     1   -1/4  | × | (VV) |
# | (AA) |     | -2  -2    1     1   -1/4  |   | (AA) |
# | (TT) |     | 12  12   -3    -3   3/4   |   | (TT) |
#
# Wait, this is the Fierz matrix relating (ψ̄Γ_Aψ)(ψ̄Γ_Aψ) on the left
# to (ψ̄Γ_Bψ)(ψ̄Γ_Bψ) on the right. But this is for the rearrangement
# (12)(34) → (14)(32), which for identical fermions gives back (ψ̄Γψ)(ψ̄Γψ).
#
# Let me be very explicit. The standard 4D Fierz identity (Itzykson & Zuber):
#
# δ_αδ δ_γβ = (1/4)[δ_αβ δ_γδ + (γ⁵)_αβ(γ⁵)_γδ
#              + (γ^μ)_αβ(γ_μ)_γδ - (γ^μγ⁵)_αβ(γ_μγ⁵)_γδ
#              + (1/2)(σ^{μν})_αβ(σ_{μν})_γδ]
#
# For a bilinear product (ψ̄ Γ^A ψ)(ψ̄ Γ^B ψ) with identical fermions:
#
# (ψ̄_α Γ^A_αβ ψ_β)(ψ̄_γ Γ^B_γδ ψ_δ)
#
# Insert the completeness relation between ψ_β and ψ̄_γ:
# ... this gives the standard Fierz formula with a -1 from anticommutation.
#
# THE RESULT I NEED (verified from multiple sources):
#
# For single-flavor Dirac fermion (no color), the Fierz decomposition is:

print("FIERZ DECOMPOSITION OF VECTOR/AXIAL CURRENT-CURRENT INTERACTIONS")
print("(single flavor, contracted over Lorentz index μ)")
print()

# Define symbolic γ (Barbero-Immirzi)
gamma = symbols('gamma', positive=True)

# The three terms in (J^μ)(J_μ):
# Term 1: (ψ̄γ^μγ⁵ψ)(ψ̄γ_μγ⁵ψ)  coefficient: 1
# Term 2: (ψ̄γ^μψ)(ψ̄γ_μψ)          coefficient: 1/γ²
# Term 3: (ψ̄γ^μγ⁵ψ)(ψ̄γ_μψ) + h.c. coefficient: 2/γ  (from cross-term)

# Standard Fierz results for these (using Klevansky 1992 conventions):
#
# The Fierz identity applied to current-current for IDENTICAL fermions gives:
#
# (ψ̄γ^μγ⁵ψ)(ψ̄γ_μγ⁵ψ) = (ψ̄ψ)² + (ψ̄iγ⁵ψ)² + ...  [same flavor exchange]
# (ψ̄γ^μψ)(ψ̄γ_μψ) = (ψ̄ψ)² + (ψ̄iγ⁵ψ)² + ...  [same]
# (ψ̄γ^μψ)(ψ̄γ_μγ⁵ψ) = -2(ψ̄ψ)(ψ̄iγ⁵ψ) + ...
#
# But I must derive the exact coefficients, not trust "..."
#
# Let me use the EXPLICIT Fierz matrix.
#
# The Fierz matrix for 4D Dirac spinors (basis: S, P, V, A, T):
# The matrix F satisfies:
#   (ψ̄ Γ_i ψ)(ψ̄ Γ_j ψ) = Σ_k F^k_{ij} (ψ̄ Γ_k ψ)²
#
# where the sum involves appropriate Lorentz contractions.
#
# For current-current (one Lorentz index contracted):
#
# (ψ̄ γ^μ A ψ)(ψ̄ γ_μ B ψ) where A, B ∈ {1, γ⁵}
#
# This equals: (ψ̄)_α (γ^μ A)_{αβ} ψ_β (ψ̄)_γ (γ_μ B)_{γδ} ψ_δ
#
# Fierz rearrange (exchange β ↔ δ with minus sign):
# = -(1/4) Σ_C (ψ̄)_α (γ^μ A)_{αβ} (Γ_C)_{δβ} (ψ̄)_γ (γ_μ B)_{γδ'} δ_{δδ'} ψ_δ (Γ^C)...
#
# OK this index gymnastics is error-prone. Let me just use the KNOWN results
# and verify them numerically with explicit gamma matrices.

print("Using explicit 4×4 gamma matrix representation to verify Fierz identities")
print()

# =============================================================================
# EXPLICIT GAMMA MATRIX COMPUTATION
# =============================================================================

# Dirac representation of gamma matrices
# γ⁰ = diag(1,1,-1,-1)
# γⁱ = [[0, σⁱ], [-σⁱ, 0]]
# γ⁵ = [[0, 1], [1, 0]]

from sympy import I, zeros

# Pauli matrices
sigma_1 = Matrix([[0, 1], [1, 0]])
sigma_2 = Matrix([[0, -I], [I, 0]])
sigma_3 = Matrix([[1, 0], [0, -1]])
id2 = eye(2)

# Gamma matrices in Dirac representation
gamma_0 = Matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, -1, 0],
    [0, 0, 0, -1]
])

def block_matrix(A, B, C, D):
    """Build 4×4 from 2×2 blocks."""
    top = A.row_join(B)
    bot = C.row_join(D)
    return top.col_join(bot)

gamma_1 = block_matrix(zeros(2), sigma_1, -sigma_1, zeros(2))
gamma_2 = block_matrix(zeros(2), sigma_2, -sigma_2, zeros(2))
gamma_3 = block_matrix(zeros(2), sigma_3, -sigma_3, zeros(2))

gamma_5 = block_matrix(zeros(2), id2, id2, zeros(2))  # = iγ⁰γ¹γ²γ³

# Verify: γ⁵ = iγ⁰γ¹γ²γ³
gamma5_check = I * gamma_0 * gamma_1 * gamma_2 * gamma_3
assert gamma_5 == gamma5_check, "γ⁵ definition check failed!"

# Verify: {γ⁵, γ^μ} = 0
for g in [gamma_0, gamma_1, gamma_2, gamma_3]:
    assert simplify(gamma_5 * g + g * gamma_5) == zeros(4), "Anticommutation check failed!"

# Verify: (γ⁵)² = 1
assert gamma_5 * gamma_5 == eye(4), "γ⁵² = 1 check failed!"

gamma_mu = [gamma_0, gamma_1, gamma_2, gamma_3]
# With metric (+,-,-,-)
metric = [1, -1, -1, -1]

print("Gamma matrices verified: {γ⁵,γ^μ}=0, (γ⁵)²=1 ✓")
print()

# =============================================================================
# FIERZ IDENTITY VERIFICATION VIA EXPLICIT TRACE
# =============================================================================
#
# The Fierz rearrangement for identical fermions:
#
# (ψ̄ M ψ)(ψ̄ N ψ) = -(1/16) Σ_{A} tr(M Γ_A) tr(N Γ^A) × (ψ̄ Γ_A ψ)²
#                     -(1/16) Σ_{A≠B} tr(M Γ_A) tr(N Γ^B) × (ψ̄ Γ_A ψ)(ψ̄ Γ_B ψ)
#
# WAIT — that's not right either. Let me start from the correct formula.
#
# The Fierz identity in the form we need:
#
# M_{αβ} N_{γδ} = (1/16) Σ_A Σ_B tr(M Γ_A N Γ_B) × (Γ^A)_{αδ} (Γ^B)_{γβ}
#
# So:
# (ψ̄ M ψ)(ψ̄ N ψ) = ψ̄_α M_{αβ} ψ_β ψ̄_γ N_{γδ} ψ_δ
#                    = -ψ̄_α M_{αβ} N_{γδ} ψ_δ ψ̄_γ ψ_β  [anticommute]
#                    = -(1/16) Σ_{AB} tr(M Γ_A N Γ_B) ψ̄_α (Γ^A)_{αδ} ψ_δ ψ̄_γ (Γ^B)_{γβ} ψ_β
#                    = -(1/16) Σ_{AB} tr(M Γ_A N Γ_B) (ψ̄ Γ^A ψ)(ψ̄ Γ^B ψ)
#
# This IS the correct formula.
#
# For our case:
#   AA: M = γ^μγ⁵, N = γ_μγ⁵  (summed over μ)
#   VV: M = γ^μ, N = γ_μ  (summed over μ)
#   VA: M = γ^μ, N = γ_μγ⁵  (summed over μ) [or M = γ^μγ⁵, N = γ_μ]

# Build the complete Dirac basis
# Γ_A for A = 0..15
basis = []
basis_names = []

# S: identity
basis.append(eye(4))
basis_names.append('S')

# P: iγ⁵
basis.append(I * gamma_5)
basis_names.append('P')

# V: γ^μ (4 elements)
for mu in range(4):
    basis.append(gamma_mu[mu])
    basis_names.append(f'V{mu}')

# A: γ^μγ⁵ (4 elements)
for mu in range(4):
    basis.append(gamma_mu[mu] * gamma_5)
    basis_names.append(f'A{mu}')

# T: σ^{μν} = (i/2)[γ^μ, γ^ν] (6 elements, μ < ν)
for mu in range(4):
    for nu in range(mu+1, 4):
        sigma_munu = (I / 2) * (gamma_mu[mu] * gamma_mu[nu] - gamma_mu[nu] * gamma_mu[mu])
        basis.append(sigma_munu)
        basis_names.append(f'T{mu}{nu}')

assert len(basis) == 16, f"Expected 16 basis elements, got {len(basis)}"
print(f"Complete Dirac basis: {len(basis)} elements ✓")
print(f"  S(1) + P(1) + V(4) + A(4) + T(6) = 16")
print()

# =============================================================================
# COMPUTE FIERZ COEFFICIENTS FOR (AA), (VV), (VA)
# =============================================================================

def compute_fierz_coefficients(M_matrices):
    """
    Compute the Fierz decomposition of Σ_μ (ψ̄ M^μ ψ)(ψ̄ N_μ ψ)
    where M_matrices is a list of (M^μ, N_μ, metric_factor) tuples.

    Returns coefficients c_{AB} such that:
    Σ_μ (ψ̄ M^μ ψ)(ψ̄ N_μ ψ) = -(1/16) Σ_{AB} c_{AB} (ψ̄ Γ^A ψ)(ψ̄ Γ^B ψ)
    """
    # c_{AB} = Σ_μ g_μμ × tr(M^μ Γ_A N_μ Γ_B)
    n = len(basis)
    coeffs = sp.zeros(n, n)

    for M, N, g_factor in M_matrices:
        for a in range(n):
            for b in range(n):
                tr_val = (M * basis[a] * N * basis[b]).trace()
                coeffs[a, b] += simplify(g_factor * tr_val)

    return coeffs

def extract_channel_coefficients(coeffs):
    """
    From the full 16×16 Fierz coefficient matrix, extract the
    coefficients of the physical channels:
    (SS), (PP), (SP+PS), (VV), (AA), (TT)

    where (XY) means (ψ̄ Γ_X ψ)(ψ̄ Γ_Y ψ)
    """
    # S = index 0, P = index 1
    # V = indices 2-5, A = indices 6-9, T = indices 10-15

    # (SS) coefficient
    c_SS = coeffs[0, 0]

    # (PP) coefficient
    c_PP = coeffs[1, 1]

    # (SP) + (PS) coefficient (the parity-odd cross-term!)
    c_SP = coeffs[0, 1] + coeffs[1, 0]

    # (VV) coefficient: Σ_μ g^μμ coeffs[V_μ, V_μ]
    c_VV = sum(metric[mu] * coeffs[2+mu, 2+mu] for mu in range(4))

    # (AA) coefficient: Σ_μ g^μμ coeffs[A_μ, A_μ]
    c_AA = sum(metric[mu] * coeffs[6+mu, 6+mu] for mu in range(4))

    # (TT) coefficient: Σ_{μ<ν} coeffs[T_{μν}, T_{μν}]
    t_idx = 10
    c_TT = sp.S(0)
    for mu in range(4):
        for nu in range(mu+1, 4):
            # Need metric factors for both indices
            c_TT += metric[mu] * metric[nu] * coeffs[t_idx, t_idx]
            t_idx += 1

    return {
        'SS': simplify(c_SS),
        'PP': simplify(c_PP),
        'SP': simplify(c_SP),
        'VV': simplify(c_VV),
        'AA': simplify(c_AA),
        'TT': simplify(c_TT)
    }

# --- Compute AA: (ψ̄γ^μγ⁵ψ)(ψ̄γ_μγ⁵ψ) ---
print("Computing Fierz decomposition of (ψ̄γ^μγ⁵ψ)(ψ̄γ_μγ⁵ψ)...")
AA_matrices = []
for mu in range(4):
    M = gamma_mu[mu] * gamma_5
    N = gamma_mu[mu] * gamma_5
    AA_matrices.append((M, N, metric[mu]))

AA_coeffs = compute_fierz_coefficients(AA_matrices)
AA_channels = extract_channel_coefficients(AA_coeffs)

print("  (AA) Fierz decomposition:")
for ch, val in AA_channels.items():
    if val != 0:
        print(f"    {ch}: {val}/16")

# --- Compute VV: (ψ̄γ^μψ)(ψ̄γ_μψ) ---
print("\nComputing Fierz decomposition of (ψ̄γ^μψ)(ψ̄γ_μψ)...")
VV_matrices = []
for mu in range(4):
    M = gamma_mu[mu]
    N = gamma_mu[mu]
    VV_matrices.append((M, N, metric[mu]))

VV_coeffs = compute_fierz_coefficients(VV_matrices)
VV_channels = extract_channel_coefficients(VV_coeffs)

print("  (VV) Fierz decomposition:")
for ch, val in VV_channels.items():
    if val != 0:
        print(f"    {ch}: {val}/16")

# --- Compute VA: (ψ̄γ^μψ)(ψ̄γ_μγ⁵ψ) ---
print("\nComputing Fierz decomposition of (ψ̄γ^μψ)(ψ̄γ_μγ⁵ψ)...")
VA_matrices = []
for mu in range(4):
    M = gamma_mu[mu]
    N = gamma_mu[mu] * gamma_5
    VA_matrices.append((M, N, metric[mu]))

VA_coeffs = compute_fierz_coefficients(VA_matrices)
VA_channels = extract_channel_coefficients(VA_coeffs)

print("  (VA) Fierz decomposition:")
for ch, val in VA_channels.items():
    if val != 0:
        print(f"    {ch}: {val}/16")

# =============================================================================
# COMBINE: FULL (J^μ)(J_μ) DECOMPOSITION
# =============================================================================

print("\n" + "=" * 70)
print("FULL FIERZ DECOMPOSITION OF (J^μ)(J_μ)")
print("J^μ = ψ̄γ^μγ⁵ψ + (1/γ)ψ̄γ^μψ")
print("=" * 70)
print()
print("(J^μ)(J_μ) = (AA) + (2/γ)(VA) + (1/γ²)(VV)")
print()

# Combined channel coefficients
# The full Fierz result is -(1/16) × [AA_coeffs + (2/γ)VA_coeffs + (1/γ²)VV_coeffs]
# applied to the bilinear products

channels = ['SS', 'PP', 'SP', 'VV', 'AA', 'TT']

print("Channel decomposition coefficients (multiply by -1/16 × G_eff):")
print()

gamma_sym = symbols('gamma', positive=True)

for ch in channels:
    aa_val = AA_channels[ch]
    vv_val = VV_channels[ch]
    va_val = VA_channels[ch]

    # Total = aa + (2/γ)va + (1/γ²)vv
    total = aa_val + 2 * va_val / gamma_sym + vv_val / gamma_sym**2
    total_simplified = simplify(total)

    if total_simplified != 0:
        print(f"  {ch}: coefficient = {total_simplified}/16")

        # Evaluate at γ = 0.274
        val_BI = float(total_simplified.subs(gamma_sym, sp.Rational(274, 1000)))
        print(f"        at γ=0.274: {val_BI:.4f}/16 = {val_BI/16:.6f}")

        # Check sign (determines attractive vs repulsive)
        # The interaction is L = -G_eff × (J²)
        # After Fierz: L = -G_eff × (-1/16) × Σ c_ch × (bilinear)²
        #            = (G_eff/16) × Σ c_ch × (bilinear)²
        # For HS decomposition, NEGATIVE c_ch → ATTRACTIVE channel
        # (because then L contains -(|c_ch| G_eff/16)(bilinear)²
        # which can be decoupled with an auxiliary field)
        if val_BI < 0:
            print(f"        → ATTRACTIVE (suitable for condensation)")
        elif val_BI > 0:
            print(f"        → REPULSIVE")
        print()

# =============================================================================
# THE CRITICAL QUESTION: SCALAR-PSEUDOSCALAR MIXING
# =============================================================================

print("=" * 70)
print("THE CRITICAL RESULT: SCALAR-PSEUDOSCALAR CHANNEL STRUCTURE")
print("=" * 70)
print()

# Extract the key coefficients
c_SS_total = simplify(AA_channels['SS'] + 2*VA_channels['SS']/gamma_sym + VV_channels['SS']/gamma_sym**2)
c_PP_total = simplify(AA_channels['PP'] + 2*VA_channels['PP']/gamma_sym + VV_channels['PP']/gamma_sym**2)
c_SP_total = simplify(AA_channels['SP'] + 2*VA_channels['SP']/gamma_sym + VV_channels['SP']/gamma_sym**2)

print(f"Coefficient of (ψ̄ψ)²:           c_SS = {c_SS_total}/16")
print(f"Coefficient of (ψ̄iγ⁵ψ)²:        c_PP = {c_PP_total}/16")
print(f"Coefficient of (ψ̄ψ)(ψ̄iγ⁵ψ):    c_SP = {c_SP_total}/16")
print()

# Check if SP cross-term is nonzero
if simplify(c_SP_total) != 0:
    print("★★★ THE SCALAR-PSEUDOSCALAR CROSS-TERM IS NONZERO! ★★★")
    print()
    print("This means: V_eff(σ, π) will contain a σπ cross-coupling.")
    print("This is Possibility A from the canonical problem statement:")
    print("  'explicit odd-power term in π (e.g., a σπ cross-coupling)'")
    print()
    print("The π → −π symmetry of V_eff IS explicitly broken.")
    print("A minimum with π* ≠ 0 is structurally possible.")
    print()

    # Check γ dependence
    c_SP_inf = sp.limit(c_SP_total, gamma_sym, sp.oo)
    c_SP_zero = sp.limit(c_SP_total, gamma_sym, 0)
    print(f"Limit checks:")
    print(f"  γ → ∞: c_SP → {c_SP_inf}  (must vanish — standard EC has no parity breaking)")
    print(f"  γ → 0: c_SP → {c_SP_zero}")

else:
    print("The scalar-pseudoscalar cross-term VANISHES.")
    print("This is Possibility B: only even coefficients are modified.")
    print("The π → −π symmetry of V_eff is PRESERVED.")

# =============================================================================
# THE EFFECTIVE INTERACTION IN SCALAR CHANNELS
# =============================================================================

print()
print("=" * 70)
print("EFFECTIVE INTERACTION FOR HUBBARD-STRATONOVICH DECOMPOSITION")
print("=" * 70)
print()

# The full four-fermion Lagrangian in scalar/pseudoscalar channels:
# L_4f = -G_eff × (J²)
#       = -G_eff × (-1/16) × [c_SS (ψ̄ψ)² + c_PP (ψ̄iγ⁵ψ)² + c_SP (ψ̄ψ)(ψ̄iγ⁵ψ) + ...]
#       = (G_eff/16) × [c_SS (ψ̄ψ)² + c_PP (ψ̄iγ⁵ψ)² + c_SP (ψ̄ψ)(ψ̄iγ⁵ψ) + ...]
#
# Define effective couplings in the scalar/pseudoscalar sector:

kappa_sq_sym = symbols('kappa^2', positive=True)
G_eff = Rational(3, 16) * kappa_sq_sym * gamma_sym**2 / (gamma_sym**2 + 1)

# The scalar/pseudoscalar part of L_4f is:
# L_SP = (G_eff/16) × [c_SS (ψ̄ψ)² + c_PP (ψ̄iγ⁵ψ)² + c_SP (ψ̄ψ)(ψ̄iγ⁵ψ)]

G_s = simplify(G_eff * c_SS_total / 16)  # effective scalar coupling
G_p = simplify(G_eff * c_PP_total / 16)  # effective pseudoscalar coupling
G_sp = simplify(G_eff * c_SP_total / 16) # effective scalar-pseudoscalar mixing

print("Effective couplings in the scalar/pseudoscalar sector:")
print()
print(f"  G_s  (scalar):     {G_s}")
print(f"  G_p  (pseudoscalar): {G_p}")
print(f"  G_sp (cross-term): {G_sp}")
print()
print("The effective Lagrangian in scalar/pseudoscalar channels is:")
print()
print("  L_SP = G_s (ψ̄ψ)² + G_p (ψ̄iγ⁵ψ)² + G_sp (ψ̄ψ)(ψ̄iγ⁵ψ) + (V,A,T channels)")
print()
print("For the Hubbard-Stratonovich transformation:")
print("  - Introduce σ ~ ⟨ψ̄ψ⟩ and π ~ ⟨ψ̄iγ⁵ψ⟩")
print("  - The cross-term G_sp requires a MIXED HS transformation")
print("    (σπ mixing in the tree-level potential)")

# Evaluate at γ = 0.274
print()
print("=" * 70)
print(f"NUMERICAL VALUES AT γ = 0.274")
print("=" * 70)
gamma_BI = sp.Rational(274, 1000)

G_s_val = float(G_s.subs([(gamma_sym, gamma_BI), (kappa_sq_sym, 1)]))
G_p_val = float(G_p.subs([(gamma_sym, gamma_BI), (kappa_sq_sym, 1)]))
G_sp_val = float(G_sp.subs([(gamma_sym, gamma_BI), (kappa_sq_sym, 1)]))

print()
print(f"  G_s  / κ² = {G_s_val:.6f}")
print(f"  G_p  / κ² = {G_p_val:.6f}")
print(f"  G_sp / κ² = {G_sp_val:.6f}")
print()

if G_sp_val != 0:
    print(f"  |G_sp / G_s| = {abs(G_sp_val/G_s_val):.4f}")
    print(f"  |G_sp / G_p| = {abs(G_sp_val/G_p_val):.4f}")

# =============================================================================
# SUMMARY AND IMPLICATIONS
# =============================================================================

print()
print("=" * 70)
print("SUMMARY: COMPUTATION 3 RESULTS")
print("=" * 70)
print()
print("1. The Fierz rearrangement of the torsion-induced (J^μ)(J_μ)")
print("   interaction has been computed explicitly using gamma matrices.")
print()
print("2. Key result for the canonical problem statement Q5:")

if simplify(c_SP_total) != 0:
    print("   → Possibility A is REALIZED.")
    print("   → The parity-sensitive G_VA cross-term generates an explicit")
    print("     σπ mixing term in the scalar/pseudoscalar channel.")
    print("   → V_eff(σ,π) will NOT be symmetric under π → −π.")
    print("   → A minimum with π* ≠ 0 is structurally permitted.")
else:
    print("   → Possibility B is realized.")
    print("   → No σπ mixing; only even coefficients are modified.")

print()
print("3. Channel attractiveness (for condensation):")
if G_s_val < 0:
    print(f"   Scalar (σ):       ATTRACTIVE (G_s < 0)")
else:
    print(f"   Scalar (σ):       REPULSIVE (G_s > 0)")
if G_p_val < 0:
    print(f"   Pseudoscalar (π): ATTRACTIVE (G_p < 0)")
else:
    print(f"   Pseudoscalar (π): REPULSIVE (G_p > 0)")

print()
print("4. ⚠  IMPORTANT CAVEATS:")
print("   - This is for a SINGLE Dirac fermion flavor. With N_f flavors,")
print("     the Fierz coefficients may differ due to flavor traces.")
print("   - Color (N_c) factors are not included. For QCD-like fermions,")
print("     additional color Fierz rearrangement is needed.")
print("   - The tensor channel coefficients should be checked for")
print("     completeness (we focused on S, P, SP).")
print()
print("NEXT: comp3_hubbard_stratonovich.py")
print("  → Introduce auxiliary fields σ, π")
print("  → Derive V_tree(σ, π) including the cross-term")
print("  → Set up the fermion determinant for one-loop computation")
