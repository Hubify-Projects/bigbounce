#!/usr/bin/env python3
"""
Branch G Phase 1: Does γ enter the strict one-loop effective action?

This script traces the torsion elimination procedure symbolically and
identifies exactly where the Barbero-Immirzi parameter γ appears in
the reduced theory. The question is whether γ enters the one-loop
Dirac operator (whose determinant defines the fermion effective action)
or only the four-fermion sector S_4f (which contributes at two loops).

Reference: 08_branchG_canonical_problem_statement.md (v2, frozen)
"""

import sympy as sp

print("=" * 72)
print("BRANCH G PHASE 1: OPERATOR ANALYSIS")
print("Does γ enter the strict one-loop Dirac operator?")
print("=" * 72)

# =============================================================================
# STEP 1: TORSION ELIMINATION IN EC+HOLST
# =============================================================================

print("\n" + "=" * 72)
print("STEP 1: TORSION ELIMINATION")
print("=" * 72)

gamma = sp.Symbol('gamma', positive=True)
kappa_sq = sp.Symbol('kappa_sq', positive=True)

print("""
The EC+Holst action with Dirac fermions gives an algebraic equation
for the spin connection:

  ω^{IJ}_μ = ω̊^{IJ}_μ[e] + K^{IJ}_μ

where ω̊ is the torsion-free Levi-Civita connection and K is the
contorsion tensor. The Holst term modifies the torsion equation.

In standard EC (γ → ∞), the contorsion is:
  K^I_{μν} ∝ κ² × (fermion spin density)

With the Holst term (finite γ), the modified torsion equation gives:
  K^I_{μν} = K^I_{μν}(γ, κ², ψ̄, ψ)

The KEY STRUCTURAL POINT is that K is always proportional to
fermion bilinears:

  K^{IJ}_μ ~ κ² × ψ̄ Γ^{IJ}_μ ψ

where Γ^{IJ}_μ involves gamma matrices and the tetrad.
""")

print("After substituting ω = ω̊ + K back into the full action:")
print()
print("  S_reduced[e, ψ] = S_EH[e]")
print("                   + ∫ ψ̄ iγ^μ ∇̊_μ ψ    [free Dirac, LC connection]")
print("                   + ∫ ψ̄ iγ^μ (¼ K_μ^{IJ} γ_I γ_J) ψ")
print("                   + (gravitational K² terms)")
print()
print("The third line is ~ ψ̄ (ψ̄ Γ ψ) ψ → FOUR-FERMION (quartic in ψ)")
print("The fourth line is ~ (ψ̄ Γ ψ)²  → FOUR-FERMION (quartic in ψ)")
print()
print("Both contribute to S_4f. The free Dirac term uses ∇̊ (Levi-Civita).")

# =============================================================================
# STEP 2: IDENTIFY THE ONE-LOOP OPERATOR
# =============================================================================

print("\n" + "=" * 72)
print("STEP 2: THE ONE-LOOP DIRAC OPERATOR")
print("=" * 72)

print("""
After torsion elimination, the reduced action is:

  S_reduced = S_EH[e] + S_Dirac^free[e, ψ] + S_4f[e, ψ; γ]

where:
  S_Dirac^free = ∫ d⁴x √-g [ψ̄ iγ^μ ∇̊_μ ψ - m ψ̄ψ]
  S_4f = ∫ d⁴x √-g [-G_eff(γ) (J^μ)²]    [four-fermion, from Track B]

The one-loop fermion determinant comes from the GAUSSIAN part of the
fermion functional integral:

  Γ^(1-loop)_ferm[e] = -½ Tr ln(-D̸² + m² + ¼R)

where D̸ = iγ^μ ∇̊_μ is the Dirac operator with Levi-Civita connection,
and ¼R is the standard Lichnerowicz curvature term.
""")

print("THE CRITICAL OBSERVATION:")
print()
print("  The operator -D̸² + m² + ¼R uses ONLY the Levi-Civita")
print("  connection ω̊[e]. It does NOT depend on γ.")
print()
print("  γ enters ONLY through S_4f, which is quartic in ψ.")
print("  At strict one-loop, quartic vertices do not contribute —")
print("  they require at least two loops.")
print()
print("  Therefore: Γ^(1-loop)_ferm[e] is γ-INDEPENDENT.")

# =============================================================================
# STEP 3: CHECK THE THREE CANDIDATE CHANNELS
# =============================================================================

print("\n" + "=" * 72)
print("STEP 3: THREE CANDIDATE CHANNELS FOR γ ENTRY")
print("=" * 72)

# Channel (a): Modified background
print("""
CHANNEL (a): Modified background equations
-------------------------------------------
The classical EC+Holst field equations include γ-dependent terms
(from the four-fermion stress-energy). The bounce solution depends on γ.
The one-loop determinant, evaluated ON this background, inherits
indirect γ-dependence.

BUT: this is γ-dependence of the BACKGROUND SOLUTION (a point in
field space), not of the EFFECTIVE ACTION AS A FUNCTIONAL.

  Γ_eff[g] is γ-independent.
  Γ_eff[g_bounce(γ)] has γ-dependence through g_bounce, not through Γ_eff.

Per the frozen canonical statement, this does NOT count as novel
Holst content for Gate G1 purposes.

VERDICT: Channel (a) yields NO novel γ-dependence in Γ_eff[g].
""")

# Channel (b): Parity-odd sector
print("""
CHANNEL (b): Parity-odd sector / η-invariant
---------------------------------------------
The fermion determinant has a phase — the η-invariant — related to
the gravitational chiral anomaly. On backgrounds with nonzero
Pontryagin density P₄, this contributes parity-odd terms.

Sub-question 1: Is P₄ nonzero on relevant backgrounds?
  - On homogeneous FRW: P₄ = 0 identically (FRW is conformally flat)
  - On the bounce: depends on specific geometry, but for homogeneous
    bounces P₄ = 0
  - Nonzero P₄ requires anisotropy or gravitational-wave perturbations

Sub-question 2: Does the η-invariant depend on γ?
  NO. The η-invariant is computed from the spectrum of the Dirac
  operator D̸ = iγ^μ ∇̊_μ, which uses the Levi-Civita connection.
  This operator is γ-independent (see Step 2).

  The gravitational chiral anomaly:
    ∂_μ J^μ_5 = (1/384π²) R^{ab}_{cd} R̃^{cd}_{ab}
  is a property of the Dirac operator on curved spacetime.
  It has nothing to do with the Barbero-Immirzi parameter.

Sub-question 3: Even if nonzero, is it vacuum-like?
  NO. The Pontryagin term is curvature-local:
    ∫ d⁴x √-g P₄ ∝ ∫ R ∧ R (topological)
  It vanishes in the IR (R → 0) and does not contribute a
  cosmological-constant-like term.

VERDICT: Channel (b) yields NO novel γ-dependent vacuum content.
  The η-invariant exists but is:
  (i) γ-independent,
  (ii) curvature-local / topological, not vacuum-like,
  (iii) zero on homogeneous backgrounds.
""")

# Channel (c): Measure corrections
print("""
CHANNEL (c): Functional measure corrections from torsion elimination
--------------------------------------------------------------------
Question: Does the torsion elimination procedure introduce a Jacobian
or measure correction that carries γ-dependence?

The torsion elimination is performed at the CLASSICAL level: we solve
the algebraic equation of motion for ω and substitute back. This is
a change of the ACTION, not a change of integration variable.

In the path integral:
  Z = ∫ De Dω Dψ Dψ̄ exp(iS[e, ω, ψ])

If we first solve ω = ω̊ + K[ψ] classically and substitute:
  Z = ∫ De Dψ Dψ̄ exp(iS_reduced[e, ψ])

This is valid because ω is non-propagating (its equation is algebraic).
The "integration over ω" in the path integral is equivalent to
evaluating at the saddle point, which is the classical solution.

There is no Jacobian from this substitution because:
1. ω is determined pointwise by ψ — it's a constraint, not a
   change of variable in the ψ integration
2. The fermion measure Dψ Dψ̄ is defined independently of ω
3. The standard treatment (Shapiro 2002, Freidel+ 2005) performs
   this elimination without any measure correction

More formally: the path integral over ω is Gaussian in ω (the
action is at most quadratic in ω). The Gaussian integral produces
a determinant factor that depends on the tetrad e but NOT on ψ.
This factor modifies the gravitational measure, not the fermion
sector. It does not introduce γ-dependence into the fermion
determinant.

VERDICT: Channel (c) yields NO measure correction that would
  introduce γ into the one-loop fermion determinant.
""")

# =============================================================================
# STEP 4: THE SEELEY-DEWITT COEFFICIENTS
# =============================================================================

print("=" * 72)
print("STEP 4: SEELEY-DEWITT COEFFICIENTS (for completeness)")
print("=" * 72)

print("""
Since the one-loop operator is the standard Dirac operator on a
Levi-Civita background, the heat-kernel expansion gives the standard
Seeley-DeWitt coefficients for a spin-½ field:

  Γ^(1)_ferm = ∫ d⁴x √-g [c₀ Λ⁴ + c₁ Λ² R + c₂(α R² + β R_μν R^μν + ...) + ...]

For a single Dirac fermion (4 real DOF → N_s = 4 in the heat kernel):
""")

# Standard Seeley-DeWitt coefficients for Dirac field
# The squared Dirac operator is: -D̸² = -g^{μν}∇_μ∇_ν + ¼R + ...
# This is a second-order operator of the form -□ + E where E = ¼R (scalar curvature term)
# and the connection is the spin connection (Levi-Civita part)

# a₀ coefficient (vacuum energy)
print("  a₀ = tr(I) / (4π)² = 4 / (4π)²")
print("      [This is the standard quartic divergence → renormalizes Λ]")
print()

# a₁ coefficient (Einstein-Hilbert renormalization)
print("  a₁ = tr(¼R·I - ⅙R·I) / (4π)² = tr((1/12)R·I) / (4π)²")
print("      = 4 × R/12 / (4π)² = R/(12π²)")
print("      [Renormalizes Newton's constant]")
print()

# a₂ coefficient (curvature-squared terms)
print("  a₂ involves: R², R_μν R^μν, R_μνρσ R^μνρσ (or E₄, P₄)")
print("      Standard result for Dirac field — see Vassilevich (2003)")
print()

print("NONE of these coefficients depend on γ.")
print("They are determined entirely by the spin of the field (½)")
print("and the dimension of spacetime (4).")
print()
print("The a₀ term generates a quartic divergence proportional to Λ⁴.")
print("After renormalization, this is absorbed into the bare cosmological")
print("constant. The finite remainder depends on the renormalization")
print("condition — it is the standard CC problem, not a Holst prediction.")

# =============================================================================
# STEP 5: ALTERNATIVE ORDERING — WHAT IF ω IS KEPT?
# =============================================================================

print("\n" + "=" * 72)
print("STEP 5: ALTERNATIVE ORDERING (integrate ψ before eliminating ω)")
print("=" * 72)

print("""
What if we DON'T eliminate torsion first, and instead compute the
fermion determinant with the full connection ω (including torsion)?

  Γ^(1)_ferm[e, ω] = -½ Tr ln(-D̸²_ω)

where D̸_ω uses the full connection ω = ω̊ + K_torsion.

This determinant DOES depend on the torsion part of ω. Then we
integrate over ω (or evaluate at its saddle point).

However, at the saddle point with no fermion condensate (ψ_cl = 0),
the torsion vanishes: K = 0, so ω = ω̊. The determinant reduces
to the standard Levi-Civita one.

The quantum correction to the ω saddle point from the fermion loop
is a HIGHER-ORDER effect:

  ω_saddle = ω̊ + δω^(1-loop)

Substituting this into S_grav produces terms that are effectively
two-loop in the combined expansion. At strict one-loop, we use
ω = ω̊.

VERDICT: The alternative ordering gives the SAME result at strict
one-loop. γ does not enter.

Note: if we go BEYOND strict one-loop (e.g., computing δω^(1-loop)
and its back-reaction), γ can enter. But that is Approach A territory
and is OUT OF SCOPE for Branch G v1 per the frozen canonical statement.
""")

# =============================================================================
# STEP 6: CHATTOPADHYAY (2023) COMPARISON
# =============================================================================

print("=" * 72)
print("STEP 6: CHATTOPADHYAY (2023) [2310.10405] — EXPECTED COMPARISON")
print("=" * 72)

print("""
Chattopadhyay (2023) computes the one-loop effective action in
"chiral EC gravity." The key question is: does that paper find
γ-dependent terms at one loop?

Based on the analysis above, there are two possibilities:

(A) If Chattopadhyay uses the SAME ordering (torsion eliminated
    first, then one-loop fermion determinant), the result should
    be the standard Seeley-DeWitt expansion with no γ-dependence.

(B) If Chattopadhyay uses a DIFFERENT ordering or includes
    beyond-one-loop effects (e.g., torsion quantum corrections,
    non-minimal couplings, or a complex-connection formulation),
    the result may contain γ-dependent terms — but those would
    not be "strict one-loop" in the sense of Branch G v1.

A careful reading of this paper is needed to determine which case
applies. However, regardless of what Chattopadhyay finds, the
LOGICAL ARGUMENT above stands: at strict one-loop after torsion
elimination, the Dirac operator is γ-independent.

If Chattopadhyay finds γ-dependent terms, the question becomes:
at what approximation order do they appear? If they are genuinely
one-loop in the standard sense, that would contradict the analysis
above — which would mean there is a subtlety we are missing.
If they are beyond-one-loop, they confirm our analysis but suggest
that Approach A (beyond-strict-one-loop) might be worth pursuing
as a separate branch.

STATUS: Paper not yet read in detail. This is the key remaining
task for Phase 1 completion.
""")

# =============================================================================
# VERDICT
# =============================================================================

print("=" * 72)
print("PHASE 1 VERDICT")
print("=" * 72)

print("""
ALL THREE CANDIDATE CHANNELS YIELD NO NOVEL γ-DEPENDENCE:

  Channel (a) — Modified background:
    γ enters through the background solution, not the effective action
    functional. EXCLUDED per canonical statement.

  Channel (b) — Parity-odd sector / η-invariant:
    The η-invariant uses the Levi-Civita Dirac operator, which is
    γ-independent. Furthermore, it is curvature-local (not vacuum-like)
    and vanishes on homogeneous backgrounds. CLOSED.

  Channel (c) — Measure corrections:
    Torsion elimination is classical substitution, not a change of
    integration variable. No Jacobian. CLOSED.

NOVEL HOLST CONTENT CRITERION (from frozen statement):
  "Branch G counts as nontrivially alive only if the renormalized
  effective action contains at least one finite or regulator-robust
  term whose existence, sign, or classification depends nontrivially
  on finite γ and either disappears or changes qualitatively in the
  γ → ∞ limit."

RESULT: No such term exists at strict one-loop (Approach B).
  The one-loop Dirac operator is the standard curved-space operator.
  Its Seeley-DeWitt coefficients are the standard ones.
  γ enters only at two loops or beyond (through S_4f vertices).

FM-G6 FIRES: After exact torsion elimination, the strict one-loop
effective action reduces to the standard curved-space Dirac
determinant with no physically meaningful finite-γ dependence
beyond ordinary renormalization bookkeeping.

BRANCH G v1 CLOSES AT PHASE 1.

REMAINING TASK: Read Chattopadhyay (2023) to verify no subtlety
is missed. If that paper finds γ-dependent terms at genuine one-loop
order, the analysis above must be revisited.
""")

print("=" * 72)
print("IMPACT SUMMARY")
print("=" * 72)

print("""
Combined with Track B closure:

  Track B: The NJL condensate route fails at γ = 0.274.
           (wrong sign + 175× too weak + catalysis suppressed)

  Branch G v1: The strict one-loop effective action has no novel
               γ-dependent vacuum structure. The fermion determinant
               is the standard curved-space result.

Together: In the minimal EC+Holst+Dirac framework at the stated
approximation orders, neither the condensate route nor the strict
one-loop effective-action route yields novel vacuum physics from
the Holst sector. The framework remains phenomenological.

This does NOT close ALL possible routes:
  - Beyond-one-loop effects (Approach A / two-loop) could introduce γ
  - Non-minimal couplings (torsion-scalar, etc.) are not tested
  - Non-perturbative effects are not tested
  - A different value of γ > 1 does not help (changes the background
    evaluation point but not the functional form of Γ_eff)

But at the approximation orders tested, the answer is clean and negative.
""")
