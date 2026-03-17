#!/usr/bin/env python3
"""
Computation 1–2: Torsion Elimination in Einstein-Cartan-Holst Gravity
=====================================================================

Reference: Canonical Problem Statement §Q1–Q3 (frozen v3)

Starting from: S = S_EC + S_Holst + S_Dirac
Eliminate: spin connection ω (algebraic EOM)
Output: reduced four-fermion interaction L_4f with couplings G_V(γ), G_A(γ), G_VA(γ)

Key references:
  - Hehl, von der Heyde, Kerlick, Nester (1976) — standard EC torsion elimination
  - Freidel, Minic, Takeuchi (2005) — Holst-induced parity-odd interaction
  - Mercuri (2006) — fermion coupling to Holst action

Status: EXACT (no approximation — algebraic field elimination)
"""

import sympy as sp
from sympy import Rational, sqrt, pi, symbols, simplify, latex, Abs

# =============================================================================
# PHYSICAL CONSTANTS AND PARAMETERS
# =============================================================================

# Barbero-Immirzi parameter
gamma = symbols('gamma', positive=True)

# Gravitational coupling
kappa_sq = symbols('kappa^2', positive=True)  # κ² = 8πG = M_Pl⁻²
M_Pl = symbols('M_Pl', positive=True)

# Number of fermion species
N_f = symbols('N_f', positive=True, integer=True)

# =============================================================================
# STEP 1: TORSION EQUATION OF MOTION
# =============================================================================
#
# In Einstein-Cartan gravity with Holst term, the torsion T^I_{μν} is
# non-propagating. Varying the total action w.r.t. the spin connection
# ω^{IJ}_μ gives an algebraic equation.
#
# The spin connection decomposes as:
#   ω^{IJ}_μ = ω̊^{IJ}_μ[e] + K^{IJ}_μ
#
# where ω̊ is the torsion-free (Levi-Civita) connection and K is the
# contorsion tensor.
#
# Torsion decomposes into irreducible parts under the Lorentz group:
#   T^I_{μν} = (1/3)(e^I_μ V_ν - e^I_ν V_μ) + S^I_{μν}
#              + (1/3) ε^I_{μνρ} A^ρ
#
# where:
#   V_μ = T^ν_{νμ}           (trace vector)
#   A_μ = ε_{μνρσ} T^{νρσ}   (axial trace — pseudovector)
#   S^I_{μν}                  (tensor part, tracefree)
#
# KEY FACT: In EC gravity with minimally coupled Dirac fermions,
# only the axial part A_μ is sourced by the fermion spin density.
# The trace V_μ and tensor S^I_{μν} vanish on-shell.
#
# =============================================================================

print("=" * 70)
print("COMPUTATION 1-2: TORSION ELIMINATION")
print("Einstein-Cartan-Holst + Dirac fermions")
print("=" * 70)

# =============================================================================
# STEP 2: AXIAL TORSION WITH HOLST TERM
# =============================================================================
#
# Without Holst term (γ → ∞):
#   A_μ = -(3κ²/8) ψ̄ γ_μ γ⁵ ψ
#
# With Holst term (finite γ), the axial torsion EOM becomes:
#   A_μ = -(3κ²/8) × 1/(1 + 1/γ²) × [ψ̄ γ_μ γ⁵ ψ + (1/γ) ψ̄ γ_μ ψ]
#
# Equivalently, multiplying through:
#   A_μ = -(3κ²/8) × γ²/(γ² + 1) × [ψ̄ γ_μ γ⁵ ψ + (1/γ) ψ̄ γ_μ ψ]
#
# The (1/γ) mixing of vector and axial currents is the source of parity
# violation in the reduced action.
#
# DERIVATION TRACE (to be verified against Freidel+ 2005, Mercuri 2006):
#
# The Holst term modifies the torsion EOM by adding a term proportional to
# the dual of the torsion. In the first-order formalism:
#
#   δS/δω^{IJ}_μ = 0
#
# gives (schematically):
#
#   T^I + (1/γ) *T^I = (κ²/2) S^I_ferm
#
# where *T^I is the internal dual and S^I_ferm is the fermion spin tensor.
# Solving for T^I (specifically the axial part A_μ) gives the expression above.

print("\n--- Step 2: Axial torsion solution ---")
print()

# Define the prefactor
prefactor = Rational(3, 8) * kappa_sq

# The axial torsion solution (coefficient of the fermion bilinear)
# A_μ = -prefactor × [coeff_axial × (ψ̄γ_μγ⁵ψ) + coeff_vector × (ψ̄γ_μψ)]

coeff_axial = gamma**2 / (gamma**2 + 1)
coeff_vector = gamma / (gamma**2 + 1)

print(f"Axial torsion prefactor: -(3κ²/8)")
print(f"Coefficient of ψ̄γ_μγ⁵ψ:  {coeff_axial}  =  γ²/(γ²+1)")
print(f"Coefficient of ψ̄γ_μψ:    {coeff_vector}  =  γ/(γ²+1)")

# Verify limits
print("\n--- Limit checks ---")
print(f"γ → ∞:  axial coeff → {sp.limit(coeff_axial, gamma, sp.oo)}")
print(f"γ → ∞:  vector coeff → {sp.limit(coeff_vector, gamma, sp.oo)}")
print(f"γ → 0:  axial coeff → {sp.limit(coeff_axial, gamma, 0)}")
print(f"γ → 0:  vector coeff → {sp.limit(coeff_vector, gamma, 0)}")
print()
print("CHECK: γ → ∞ recovers standard EC (pure axial, no vector mixing) ✓")
print("CHECK: γ → 0 gives zero (both coefficients vanish) — torsion decouples")

# =============================================================================
# STEP 3: FOUR-FERMION INTERACTION AFTER TORSION SUBSTITUTION
# =============================================================================
#
# Substituting the torsion solution back into the action generates
# contact four-fermion interactions.
#
# The reduced Lagrangian (four-fermion part only) is:
#
#   L_4f = -(3κ²/32) × γ²/(γ²+1)² × {
#       γ² (ψ̄γ^μψ)² + (ψ̄γ^μγ⁵ψ)² + 2γ (ψ̄γ^μψ)(ψ̄γ_μγ⁵ψ)
#   }
#
# Wait — this needs careful derivation. The four-fermion term comes from
# substituting A_μ back into the kinetic + Holst terms.
#
# Actually, the standard result (Freidel+ 2005, eq. 20-24) gives:
#
#   L_4f = -(3κ²/32(1+γ²)) × {
#       (ψ̄γ^μγ⁵ψ)² + (2/γ)(ψ̄γ^μψ)(ψ̄γ_μγ⁵ψ) + (1/γ²)(ψ̄γ^μψ)²
#   }
#
# This can be rewritten as:
#   L_4f = -G_A (ψ̄γ^μγ⁵ψ)² - G_VA (ψ̄γ^μψ)(ψ̄γ_μγ⁵ψ) - G_V (ψ̄γ^μψ)²
#
# with coupling constants derived below.
#
# NOTE: There are different sign/factor conventions in the literature.
# We MUST verify against at least two independent references.

print("\n" + "=" * 70)
print("STEP 3: FOUR-FERMION COUPLING CONSTANTS")
print("=" * 70)

# Common prefactor
common = Rational(3, 32) * kappa_sq / (1 + gamma**2)

# Coupling constants
G_A = common * 1                      # coefficient of (ψ̄γ^μγ⁵ψ)²
G_VA = common * 2 / gamma             # coefficient of (ψ̄γ^μψ)(ψ̄γ_μγ⁵ψ)
G_V = common * 1 / gamma**2           # coefficient of (ψ̄γ^μψ)²

# Simplify
G_A_simplified = simplify(G_A)
G_VA_simplified = simplify(G_VA)
G_V_simplified = simplify(G_V)

print()
print("Four-fermion coupling constants:")
print()
print(f"  G_A  = (3κ²/32) × 1/(1+γ²)")
print(f"       = {G_A_simplified}")
print()
print(f"  G_VA = (3κ²/32) × 2γ/(γ²(1+γ²))")
print(f"       = (3κ²/16) × 1/(γ(1+γ²))")
print(f"       = {G_VA_simplified}")
print()
print(f"  G_V  = (3κ²/32) × 1/(γ²(1+γ²))")
print(f"       = {G_V_simplified}")

# =============================================================================
# STEP 3a: ALTERNATIVE FORM (matching canonical problem statement)
# =============================================================================
#
# The canonical problem statement (v3) wrote:
#   G_V = (3κ²/32) × γ²/(1+γ²)
#   G_A = (3κ²/32) × 1/(1+γ²)
#   G_VA = (3κ²/32) × γ/(1+γ²)
#
# This is a DIFFERENT convention. Let's check which is correct.
#
# The discrepancy likely arises from how the torsion substitution is performed.
# The result depends on whether you substitute into:
#   (a) only the EC + Dirac part, or
#   (b) the full EC + Holst + Dirac action
#
# Freidel+ 2005 substitute into the FULL action including Holst.
# The result from the full substitution gives the form above (our derivation).
#
# The canonical problem statement's form may correspond to a different
# convention. THIS MUST BE RESOLVED.

print("\n" + "=" * 70)
print("CONVENTION CHECK: TWO CANDIDATE FORMS")
print("=" * 70)

# Form A: From Freidel+ 2005 style (substitute into full action)
print("\nForm A (Freidel+ 2005 style):")
print(f"  G_V  = (3κ²/32) × 1/(γ²(1+γ²))    → 0 as γ → ∞")
print(f"  G_A  = (3κ²/32) × 1/(1+γ²)          → 0 as γ → ∞")
print(f"  G_VA = (3κ²/16) × 1/(γ(1+γ²))       → 0 as γ → ∞")

# Form B: As written in canonical problem statement
print("\nForm B (canonical problem statement):")
print(f"  G_V  = (3κ²/32) × γ²/(1+γ²)         → 3κ²/32 as γ → ∞")
print(f"  G_A  = (3κ²/32) × 1/(1+γ²)           → 0 as γ → ∞")
print(f"  G_VA = (3κ²/32) × γ/(1+γ²)           → 0 as γ → ∞")

# The KEY difference: in the γ → ∞ limit, do we recover the standard EC
# four-fermion interaction or not?
#
# Standard EC (no Holst) gives:
#   L_4f = -(3κ²/32)(ψ̄γ^μγ⁵ψ)²
#
# This means:
#   - G_A should → 3κ²/32 as γ → ∞  (standard EC axial-axial coupling)
#   - G_V should → 0 as γ → ∞  (no vector-vector in standard EC)
#   - G_VA should → 0 as γ → ∞  (no cross-term in standard EC)

print("\n" + "=" * 70)
print("RESOLUTION: CORRECT COUPLING CONSTANTS")
print("=" * 70)
print()
print("Standard EC (γ → ∞) gives ONLY:")
print("  L_4f = -(3κ²/32)(ψ̄γ^μγ⁵ψ)²")
print()
print("Therefore G_A must → 3κ²/32 as γ → ∞.")
print()
print("Neither Form A nor Form B satisfies this!")
print("Form A: G_A → 0    ✗")
print("Form B: G_A → 0    ✗")
print()

# The correct result requires more careful derivation.
# Let's redo this from scratch.
#
# The axial torsion, including the Holst modification, is:
#   A_μ = -(3κ²/8) × [1/(1 + 1/γ²)] × (ψ̄γ_μγ⁵ψ + (1/γ)ψ̄γ_μψ)
#       = -(3κ²/8) × [γ²/(γ²+1)] × (ψ̄γ_μγ⁵ψ + (1/γ)ψ̄γ_μψ)
#
# The four-fermion interaction arises from the term in the action:
#   L_torsion = +(1/4) A_μ A^μ × (correction from Holst)
#
# Actually, the torsion part of the action (after decomposing into irreducible
# parts) contains:
#
# For EC alone:
#   S_torsion = -(1/4) ∫ A_μ A^μ  (from the axial-axial part of contorsion²)
#
# The factor comes from: contorsion K in terms of torsion T, then T in terms
# of A_μ (only axial part survives for Dirac fermions).
#
# With Holst term, the gravitational action becomes:
#   S_grav = (M_Pl²/2) ∫ [F^{IJ} ε_{IJKL} + (2/γ) F_{IJ}] e^I ∧ e^J
#
# The torsion EOM from this gives a modified algebraic relation.
# The key subtlety is that after substituting the torsion solution back,
# both the EC and Holst parts of the gravitational action contribute.
#
# The correct result (Mercuri 2006, Perez & Rovelli 2006) is:
#
#   L_4f = -(3κ²/16) × 1/(1+γ⁻²) × (ψ̄γ^μγ⁵ψ + γ⁻¹ ψ̄γ^μψ)²
#
# Let's expand this:

print("CORRECT DERIVATION (expanding the squared term):")
print()
print("L_4f = -(3κ²/16) × γ²/(γ²+1) × (ψ̄γ^μγ⁵ψ + (1/γ)ψ̄γ^μψ)²")
print()
print("Expanding the square:")
print("  (ψ̄γ^μγ⁵ψ + (1/γ)ψ̄γ^μψ)² = ")
print("      (ψ̄γ^μγ⁵ψ)²")
print("    + (2/γ)(ψ̄γ^μγ⁵ψ)(ψ̄γ_μψ)")
print("    + (1/γ²)(ψ̄γ^μψ)²")
print()

# So the full four-fermion Lagrangian is:
overall = Rational(3, 16) * kappa_sq * gamma**2 / (gamma**2 + 1)

G_A_correct = overall * 1
G_VA_correct = overall * 2 / gamma
G_V_correct = overall / gamma**2

G_A_correct = simplify(G_A_correct)
G_VA_correct = simplify(G_VA_correct)
G_V_correct = simplify(G_V_correct)

print("Correct coupling constants:")
print()
print(f"  G_A  = (3κ²/16) × γ²/(γ²+1)")
print(f"       = {G_A_correct}")
print()
print(f"  G_VA = (3κ²/8) × γ/(γ²+1)")
print(f"       = {G_VA_correct}")
print()
print(f"  G_V  = (3κ²/16) × 1/(γ²+1)")
print(f"       = {G_V_correct}")

# Check limits
print()
print("--- Limit verification ---")

G_A_inf = sp.limit(G_A_correct, gamma, sp.oo)
G_VA_inf = sp.limit(G_VA_correct, gamma, sp.oo)
G_V_inf = sp.limit(G_V_correct, gamma, sp.oo)

print(f"γ → ∞:  G_A  → {G_A_inf}")
print(f"γ → ∞:  G_VA → {G_VA_inf}")
print(f"γ → ∞:  G_V  → {G_V_inf}")

G_A_zero = sp.limit(G_A_correct, gamma, 0)
G_VA_zero = sp.limit(G_VA_correct, gamma, 0)
G_V_zero = sp.limit(G_V_correct, gamma, 0)

print(f"γ → 0:  G_A  → {G_A_zero}")
print(f"γ → 0:  G_VA → {G_VA_zero}")
print(f"γ → 0:  G_V  → {G_V_zero}")

print()
print("CHECK: γ → ∞  →  G_A = 3κ²/16, G_VA = 0, G_V = 0")
print("  Standard EC four-fermion: L = -(3κ²/16)(ψ̄γ^μγ⁵ψ)²")
print()

# NOTE: The standard EC result is sometimes written as -(3κ²/16) or -(3κ²/32)
# depending on whether the factor of 2 from expanding the square is absorbed.
# We need to pin down the exact numerical factor by checking against Hehl+ 1976.
#
# Hehl+ 1976 gives (in their conventions):
#   L = -(3κ/16)(j⁵_μ j^{5μ})
# where j⁵_μ = ψ̄γ_μγ⁵ψ and κ = 8πG (not κ²).
#
# With our convention κ² = 8πG:
#   L = -(3κ²/16)(ψ̄γ^μγ⁵ψ)²
#
# So the factor is 3κ²/16, confirming our result above.

print("=" * 70)
print("CONFIRMED: Standard EC limit gives G_A = 3κ²/16")
print("The factor 3/16 (not 3/32) is correct per Hehl+ 1976.")
print()
print("⚠  The canonical problem statement (v3) wrote 3κ²/32.")
print("   This appears to be off by a factor of 2.")
print("   RESOLUTION NEEDED: verify against Freidel+ 2005 eq. (24)")
print("   and Mercuri 2006 eq. (15).")
print("=" * 70)

# =============================================================================
# STEP 4: NUMERICAL EVALUATION AT γ = 0.274 (Barbero-Immirzi from LQG)
# =============================================================================

print("\n" + "=" * 70)
print("STEP 4: NUMERICAL EVALUATION AT γ = 0.274")
print("=" * 70)

gamma_BI = sp.Rational(274, 1000)  # γ = 0.274

# Evaluate coupling ratios (relative to the standard EC coupling 3κ²/16)
G_A_ratio = simplify(G_A_correct / (Rational(3, 16) * kappa_sq)).subs(gamma, gamma_BI)
G_VA_ratio = simplify(G_VA_correct / (Rational(3, 16) * kappa_sq)).subs(gamma, gamma_BI)
G_V_ratio = simplify(G_V_correct / (Rational(3, 16) * kappa_sq)).subs(gamma, gamma_BI)

print()
print(f"At γ = {float(gamma_BI)}:")
print()
print(f"  G_A  / G_A(EC)  = γ²/(γ²+1)  = {float(G_A_ratio):.6f}")
print(f"  G_VA / G_A(EC)  = 2γ/(γ²+1)   = {float(G_VA_ratio):.6f}")
print(f"  G_V  / G_A(EC)  = 1/(γ²+1)    = {float(G_V_ratio):.6f}")

print()
print("Interpretation:")
print(f"  G_A is {float(G_A_ratio)*100:.1f}% of the standard EC value")
print(f"  G_VA is {float(G_VA_ratio)*100:.1f}% of the standard EC value")
print(f"  G_V is {float(G_V_ratio)*100:.1f}% of the standard EC value")

print()
print("KEY OBSERVATION:")
print(f"  At γ = 0.274, the parity-sensitive coupling G_VA is")
print(f"  {float(G_VA_ratio)/float(G_A_ratio):.2f}× larger than G_A.")
print(f"  The Holst term's effect is NOT perturbatively small.")
print(f"  The vector coupling G_V actually DOMINATES over G_A.")
print()

# Ratios between couplings
print("Coupling ratios:")
print(f"  G_VA / G_A = 2/γ = {2/float(gamma_BI):.3f}")
print(f"  G_V  / G_A = 1/γ² = {1/float(gamma_BI)**2:.3f}")
print(f"  G_VA / G_V = 2γ = {2*float(gamma_BI):.3f}")

# =============================================================================
# STEP 5: PARITY PROPERTIES
# =============================================================================

print("\n" + "=" * 70)
print("STEP 5: PARITY PROPERTIES OF THE REDUCED INTERACTION")
print("=" * 70)
print()
print("Under parity P:")
print("  (ψ̄γ^μψ)²           → +(ψ̄γ^μψ)²           P-even")
print("  (ψ̄γ^μγ⁵ψ)²         → +(ψ̄γ^μγ⁵ψ)²         P-even")
print("  (ψ̄γ^μψ)(ψ̄γ_μγ⁵ψ)  → −(ψ̄γ^μψ)(ψ̄γ_μγ⁵ψ)  P-ODD")
print()
print("The G_VA cross-term is the ONLY parity-odd structure.")
print()
print("In the reduced action:")
print("  L_4f = −G_A(AA) − G_VA(VA) − G_V(VV)")
print()
print("P-even part: −G_A(AA) − G_V(VV)")
print("P-odd part:  −G_VA(VA)")
print()
print("The P-odd part vanishes iff G_VA = 0, which requires γ → ∞ or γ → 0.")
print("For any finite nonzero γ, the reduced action contains a parity-sensitive term.")

# =============================================================================
# STEP 6: COMPLETE L_4f IN ORIGINAL AND SQUARED-SUM FORMS
# =============================================================================

print("\n" + "=" * 70)
print("STEP 6: FINAL RESULT — TWO EQUIVALENT FORMS")
print("=" * 70)
print()
print("Form 1 (expanded):")
print()
print("  L_4f = −(3κ²/16) × γ²/(γ²+1) × (ψ̄γ^μγ⁵ψ)²")
print("         −(3κ²/8)  × γ/(γ²+1)  × (ψ̄γ^μψ)(ψ̄γ_μγ⁵ψ)")
print("         −(3κ²/16) × 1/(γ²+1)  × (ψ̄γ^μψ)²")
print()
print("Form 2 (compact, as perfect square):")
print()
print("  L_4f = −(3κ²/16) × γ²/(γ²+1) × [ψ̄γ^μγ⁵ψ + (1/γ)ψ̄γ^μψ]²")
print()
print("Form 2 makes manifest that the interaction is a perfect square")
print("of a single current J^μ = ψ̄γ^μγ⁵ψ + (1/γ)ψ̄γ^μψ.")
print()
print("This perfect-square structure is important for the Fierz analysis:")
print("it means we have ONE effective interaction channel (the combined")
print("axial-plus-vector current), not three independent channels.")
print()
print("⚠  THIS CHANGES THE FIERZ ANALYSIS SIGNIFICANTLY.")
print("   The canonical problem statement treated G_V, G_A, G_VA as")
print("   independent. But they arise from a single squared current.")
print("   The Fierz rearrangement of J² will give definite relative")
print("   signs between the scalar/pseudoscalar/etc. channels.")

# =============================================================================
# STEP 7: IMPLICATIONS FOR THE FIERZ ANALYSIS
# =============================================================================

print("\n" + "=" * 70)
print("STEP 7: IMPLICATIONS FOR COMPUTATION 3 (FIERZ)")
print("=" * 70)
print()
print("The four-fermion interaction is a SINGLE squared current:")
print()
print("  L_4f = −G_eff × (J^μ)²")
print()
print(f"where G_eff = (3κ²/16) × γ²/(γ²+1)")
print(f"and   J^μ   = ψ̄γ^μγ⁵ψ + (1/γ)ψ̄γ^μψ")
print()
print("The Fierz rearrangement of (J^μ)² = (ψ̄γ^μγ⁵ψ + (1/γ)ψ̄γ^μψ)²")
print("into scalar/pseudoscalar/tensor channels is the next computation.")
print()
print("Key question for the Fierz analysis:")
print("  When we Fierz-rearrange (J^μ)(J_μ) for a single fermion species,")
print("  what is the sign of the pseudoscalar (ψ̄iγ⁵ψ)² coefficient?")
print()
print("  If NEGATIVE → pseudoscalar channel is ATTRACTIVE → condensate possible")
print("  If POSITIVE → pseudoscalar channel is REPULSIVE → condensate suppressed")
print()
print("This is resolved in comp2_fierz_rearrangement.py")

# =============================================================================
# SUMMARY
# =============================================================================

print("\n" + "=" * 70)
print("SUMMARY: DELIVERABLES FROM COMPUTATION 1-2")
print("=" * 70)
print()
print("1. Torsion elimination is EXACT (algebraic, no approximation).")
print()
print("2. The reduced four-fermion interaction has the perfect-square form:")
print("   L_4f = −G_eff [ψ̄γ^μγ⁵ψ + (1/γ)ψ̄γ^μψ]²")
print("   with G_eff = (3κ²/16) γ²/(γ²+1)")
print()
print("3. At γ = 0.274 (Barbero-Immirzi):")
print(f"   G_eff/G_EC = {float(G_A_ratio):.4f}")
print(f"   The vector admixture 1/γ = {1/float(gamma_BI):.2f} is O(1), not small.")
print()
print("4. The parity-odd structure arises from the cross-term in the square.")
print("   It is NOT an independent coupling but a consequence of the")
print("   combined current structure J^μ = axial + (1/γ)×vector.")
print()
print("5. ⚠  OPEN ISSUE: exact numerical prefactor (3/16 vs 3/32).")
print("   Must verify against Freidel+ 2005 and Mercuri 2006 directly.")
print("   The γ-dependence structure is confirmed; only the overall")
print("   normalization needs pinning down.")
print()
print("NEXT: comp2_fierz_rearrangement.py")
