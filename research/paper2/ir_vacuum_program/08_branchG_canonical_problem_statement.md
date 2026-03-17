# Branch G Canonical Problem Statement: One-Loop Gravitational Effective Action

**Date:** 2026-03-13
**Version:** v2 (FROZEN)
**Status:** LOCKED — changes only by versioned addendum (see 08a_branchG_freeze_log.md)
**Purpose:** Answer 6 questions with zero ambiguity before any Branch G computation begins
**Prerequisite:** Track B is CLOSED (Gate 1 failed). This is a new program, not a continuation.

---

## What This Memo Does Not Assume

- Does not assume the one-loop effective action generates a vacuum-like term
- Does not assume a finite remainder survives after standard renormalization
- Does not assume any particular sign or magnitude of the induced vacuum energy
- Does not assume the result is regulator-independent without explicit check
- Does not assume that a cosmological-constant-like term in Γ_eff has physical content beyond counterterm bookkeeping
- Does not assume the Holst sector produces anything qualitatively new at one loop — that is what we test
- Does not assume the condensate route works (Track B is closed)
- Does not assume de Sitter background results extend to general late-time behavior

---

## What Track B Taught Us

Before defining Branch G, we record what was learned:

1. **Perfect-square structure:** L_4f = −G_eff(J^μ)² with J = axial + (1/γ)×vector. The couplings are constrained, not independent.

2. **Wrong channel for NJL:** The scalar/pseudoscalar channel is repulsive at γ = 0.274. G_SP ∝ (γ²−1)/(γ²+1) changes sign at γ = 1. The NJL condensate mechanism fails for the physical value of γ.

3. **Gravitational coupling is subcritical by 175×:** Even for attractive channels, the torsion-induced four-fermion coupling is far below the NJL critical coupling.

4. **Branch G is structurally different from Track B.** It does not require an NJL condensate. The question is whether the one-loop gravitational effective action — the object Γ[g] obtained by integrating out ALL matter on a curved background — contains a vacuum-like term that is not merely a restatement of bare-Λ renormalization.

---

## Question 1: What exact microscopic action are we starting from?

The same Einstein-Cartan-Holst action as Track B:

```
S = S_grav[e, ω] + S_ferm[e, ω, ψ]
```

where:

```
S_grav = (M_Pl²/2) ∫ [ε_{IJKL} + (2/γ) η_{I[K} η_{L]J}] e^I ∧ e^J ∧ F^{KL}[ω]

S_ferm = ∫ d⁴x |e| [ψ̄_i iγ^μ D_μ ψ_i − m_i ψ̄_i ψ_i]
```

with D_μ = ∂_μ + ¼ ω_μ^{IJ} γ_I γ_J. The Barbero-Immirzi parameter γ = 0.274 is fixed. No bare cosmological constant is included in the starting action — whether one is generated is what we test.

**Caveat on "no bare Λ":** Starting with bare Λ = 0 in the microscopic action is a bookkeeping choice, not itself evidence of derivation. In any QFT, the renormalized cosmological constant is a free parameter set by a renormalization condition. A genuinely derived result requires a finite, physically meaningful remainder after renormalization that is not equivalent to arbitrary fixing of the renormalized Λ. The absence of bare Λ from S does not guarantee this — it must be demonstrated.

**Convention lock:** Same as Track B — (+, −, −, −), γ⁵ = iγ⁰γ¹γ²γ³, κ² = 8πG = M_Pl⁻².

**No additional tree-level operators** beyond the EC+Holst+Dirac sector. If the one-loop effective action generates operators beyond Einstein-Hilbert + Λ (e.g., R², R_μν R^μν, parity-odd Pontryagin terms), those are recorded as predictions of the computation, not inputs.

---

## Question 2: What exact object are we computing?

**The target object is the one-loop gravitational effective action:**

```
Γ_eff[e] = S_grav[e, ω̊[e]] + Γ^(1-loop)_ferm[e]
```

where ω̊[e] is the torsion-free Levi-Civita connection (after torsion elimination), and:

```
Γ^(1-loop)_ferm[e] = −½ Tr ln(−D̸² + ...)
```

is the one-loop fermion determinant evaluated on the background geometry defined by e.

**Critical distinction from Track B:** The target is NOT a condensate order parameter. It is the effective action as a functional of the tetrad. We are asking what gravitational operators are induced, not whether a fermion bilinear acquires a VEV.

**Tetrad vs metric language:** The tetrad e^I_μ is used for derivation convenience (it is the natural variable in first-order formalism). For the late-time dark-energy interpretation, the physically relevant object is the diffeomorphism-covariant gravitational effective action — i.e., the metric effective action Γ[g_μν] obtained by restricting to torsion-free, Lorentz-gauge-fixed configurations. If there are residual parity-sensitive Lorentz-frame structures that matter before reducing to metric variables, those must be identified explicitly in Phase 1. The late-time target is a diffeomorphism-covariant statement, not a frame-dependent one.

**The specific question:** Does Γ_eff[e] contain a term of the form

```
Γ_eff ⊃ − ∫ d⁴x √−g  Λ_eff
```

where Λ_eff is:
- nonzero,
- not removable by standard counterterm subtraction without destroying physical content,
- not restricted to high-curvature backgrounds,
- and has a value/sign that is independent of the renormalization scheme used?

If yes, this is a derived vacuum energy. If no, the minimal theory does not generate dark energy at one loop.

---

## Question 3: What fields are eliminated, in what order?

Each step is labeled by its logical status.

**Step 1 — Torsion elimination:**
- **Status: Exact.** Same as Track B. The spin connection is non-propagating in EC gravity. Its EOM is algebraic. After elimination:

```
S_reduced[e, ψ] = S_EH[e] + S_Dirac[e, ψ] + S_4f[e, ψ; γ]
```

where S_4f contains the torsion-induced four-fermion interaction with the perfect-square structure discovered in Track B. Note: torsion elimination is performed BEFORE the functional integral, not after. This is the standard procedure and produces a metric-like theory with four-fermion vertices.

**Step 2 — Fermion functional integration:**
- **Status: One-loop approximation.** Integrate out all fermion species ψ_i in the background of a prescribed geometry:

```
e^{iΓ^(1)_ferm[e]} = ∫ Dψ Dψ̄  exp(iS_Dirac[e, ψ] + iS_4f[e, ψ; γ])
```

The four-fermion term S_4f makes this a non-Gaussian integral. Two sub-approaches:

Two sub-approaches must be distinguished:

**Approach A (Hubbard-Stratonovich first):** Introduce auxiliary fields to linearize S_4f, then integrate out ψ exactly (Gaussian), then evaluate the auxiliary field integral at saddle point. This was the Track B approach. It decomposes the problem into condensate channels. The auxiliary-field saddle-point evaluation is an approximation beyond strict one-loop, and it reintroduces condensate-like structure — partially reopening Track B logic.

**Approach B (Strict one-loop):** Treat S_4f as a vertex in the loop expansion. At one loop, the four-fermion vertex does not contribute — only the standard fermion determinant in curved space appears. The four-fermion terms from S_4f enter at two loops or beyond.

---

### ⚠ Scope Control: Approach A vs Approach B

**Branch G v1 is restricted to Approach B (strict one-loop).**

In the strict one-loop expansion, S_4f does not contribute. The one-loop fermion determinant is that of a free Dirac field in curved spacetime. The Holst/torsion sector enters only through the classical torsion elimination (Step 1), which may modify the background around which we expand, but S_4f does not appear as a vertex at this order.

**Approach A (Hubbard-Stratonovich + saddle point) is OUT OF SCOPE for Branch G v1.** It constitutes a different approximation program that partially reopens Track B-like structure in disguise: the auxiliary-field saddle is an approximation beyond strict one-loop, and whether it condenses is precisely the Track B question already answered negatively. If Approach B yields no novel finite-γ content, the correct response is to close Branch G v1 under FM-G6 — not to silently escalate to Approach A.

**If Approach A is later deemed necessary,** it requires a new branch definition (Branch G-A or equivalent) with its own canonical problem statement, not a silent scope expansion of Branch G v1.

---

**Step 3 — Heat-kernel expansion:**
- **Status: Asymptotic expansion.** The fermion determinant is evaluated via the Schwinger-DeWitt / heat-kernel expansion:

```
Γ^(1)_ferm = −½ ∫_0^∞ ds/s  Tr(e^{−s(−D̸²)}) × (regularization)
```

The expansion produces local curvature invariants:

```
Γ^(1)_ferm = ∫ d⁴x √−g [a₀Λ⁴ + a₁Λ²R + a₂(αR² + βR_μνR^μν + γ_P E₄ + δ_P P₄) + ...]
```

where Λ is the UV cutoff (in proper-time scheme), E₄ is the Gauss-Bonnet term, P₄ is the Pontryagin density, and the a_n are Seeley-DeWitt coefficients.

The a₀ term is the candidate vacuum energy. The question is whether, after renormalization, anything physical remains.

**Step 4 — Renormalization:**
- **Status: Scheme-dependent.** This is the critical step where Branch G lives or dies. See Question 5.

**Approximation stack (explicit):**
1. Torsion elimination — exact
2. Fermion integration — one-loop (first semiclassical approximation)
3. Heat-kernel expansion — asymptotic / Seeley-DeWitt to order a₂ (curvature-squared)
4. Background geometry — homogeneous FRW in first pass, then generalize
5. Renormalization — scheme-dependent; physical conclusions must survive cross-check

---

## Question 4: Under what precise circumstances can γ enter Γ_eff[e] at the stated approximation order?

**This is the make-or-break question. It determines whether Branch G has any novel content beyond standard QFT-in-curved-spacetime results. If the answer is "γ does not enter in any physically meaningful way," Branch G closes at Phase 1.**

### The central Phase 1 question

After exact torsion elimination, the strict one-loop fermion determinant is that of a free Dirac field on a Levi-Civita background. The four-fermion interaction S_4f enters only at two loops or beyond (it is quartic in ψ and cannot contribute a one-loop correction to the fermion propagator). The Holst parameter γ enters the classical action through torsion elimination, but the one-loop OPERATOR — the squared Dirac operator −D̸² whose determinant is computed — is the standard curved-space Dirac operator.

If this is the complete picture, then γ does not enter Γ^(1-loop)_ferm at all. The one-loop effective action is identical to the standard Dirac-fermion-in-curved-spacetime result, which is a textbook computation with no novel Holst content. Branch G would then close under FM-G6.

### Three candidate channels for finite-γ entry

Before closing, Phase 1 must rigorously check three channels through which γ MIGHT enter the one-loop object. Each must be evaluated individually:

**(a) Modified background equations:**
The classical EC+Holst field equations include γ-dependent terms (the torsion-induced four-fermion stress-energy modifies the classical geometry). The bounce solution and its curvature profile depend on γ. The one-loop determinant, evaluated on this γ-dependent background, inherits indirect γ-dependence. However, this is γ-dependence of the BACKGROUND SOLUTION, not of the one-loop OPERATOR or its Seeley-DeWitt coefficients. It does not constitute novel content in the effective action itself — it is just the standard one-loop result evaluated at a γ-dependent point in field space. **This channel does not count as novel Holst content for Gate G1 purposes.** The effective action as a FUNCTIONAL is γ-independent at one loop; only the field configuration at which it is evaluated depends on γ.

**(b) Parity-odd sector / η-invariant:**
The fermion determinant has a phase — the η-invariant (Atiyah-Patodi-Singer) — related to the gravitational chiral anomaly. On backgrounds with nonzero Pontryagin density P₄ = R^{ab}_{cd} R^{cd}_{ab} (using the dual), this phase contributes parity-odd terms to Γ_eff. The question is:
- Is the Pontryagin density nonzero on the relevant backgrounds (FRW, bounce)?
- If so, does the η-invariant contribution have vacuum-like (constant) character, or is it purely topological / curvature-local?
- Does this contribution depend on γ in any way beyond the background dependence already excluded in (a)?
- Is it physical (gauge-invariant, regulator-robust) or merely formal?
- Does it survive in the late-time low-curvature limit, or does it vanish as P₄ → 0?

A skeptical reader will note that on a homogeneous FRW background, P₄ = 0 identically (FRW is conformally flat). So the parity-odd sector requires either (i) perturbations away from FRW, or (ii) the bounce geometry itself having nonzero Pontryagin density. This must be checked explicitly, not assumed.

**(c) Torsion-modified Dirac operator:**
In first-order formalism before torsion elimination, the Dirac operator uses the full connection ω = ω̊ + K, where K is the contorsion. After torsion elimination, K is expressed in terms of fermion bilinears. At one loop, the fermion determinant should be computed AFTER torsion elimination (i.e., using ω̊ only). But one must verify that this elimination is performed correctly in the functional integral measure and that no residual γ-dependent terms survive in the one-loop operator from the elimination procedure itself (e.g., through Jacobian factors or measure corrections). If the functional measure is trivial (as is standard), this channel produces nothing. If there are measure corrections, they must be checked.

### Novel Holst content criterion

**Branch G counts as nontrivially alive only if, at the stated approximation order (strict one-loop, Approach B), the renormalized effective action Γ_eff[e] contains at least one finite or regulator-robust term whose existence, sign, or classification depends nontrivially on finite γ and either disappears or changes qualitatively in the γ → ∞ Einstein-Cartan limit.**

If no such term can be isolated after checking channels (a), (b), and (c), then FM-G6 fires and Branch G v1 closes at Phase 1. This is not a failure of the program — it is the program working as designed.

### What must be determined in Phase 1

1. Does the strict one-loop Dirac operator (after torsion elimination) carry any γ-dependent structure, or is it the standard curved-space Dirac operator?
2. Is the Pontryagin density P₄ nonzero on the relevant backgrounds? If not, channel (b) is empty.
3. If P₄ ≠ 0, does the η-invariant contribute a vacuum-like (constant, IR-surviving) term, or only a curvature-local / topological term?
4. Are there functional-measure corrections from torsion elimination that introduce γ at one loop?
5. What does Chattopadhyay (2023) [2310.10405] already establish about these questions?

### The most relevant existing computation

Chattopadhyay (2023) [2310.10405]: One-loop effective action in chiral EC gravity. This paper is the closest existing calculation. Phase 1 must begin by understanding what this paper already establishes. If it already answers the central question — in either direction — then Branch G may reduce to a literature review rather than a new computation.

### Honest assessment

The most likely outcome of Phase 1 is FM-G6: the strict one-loop effective action has no novel finite-γ content beyond standard curved-spacetime results. If this happens, it means the minimal EC+Holst+Dirac theory does not produce novel vacuum structure at one loop, and the standard cosmological constant problem is simply reproduced — not solved, not repackaged, just unchanged.

This would be a clean negative result. Combined with Track B's failure, it would mean: neither the condensate route nor the one-loop effective-action route yields novel vacuum physics from the Holst sector at γ = 0.274. The framework remains phenomenological.

---

## Question 5: What counts as success? (Three gates)

### Gate G1 — Nontrivial Finite-γ Vacuum Structure

**Question:** Does the renormalized one-loop effective action contain a cosmological-constant-like contribution whose physical interpretation is not exhausted by ordinary bare-Λ renormalization AND whose nontrivial existence depends on finite γ at the stated approximation order?

**Both halves are required.** A generic vacuum divergence that exists for any QFT in curved spacetime does not pass Gate G1 — even if it is "nonzero" after renormalization. Similarly, a term that exists only for reasons unrelated to the Holst sector does not pass.

**Success criterion:** A finite, nonzero, regulator-robust vacuum energy contribution appears in Γ_eff[e] that:
- does not vanish when the bare cosmological constant is set to zero, OR whose existence/nonexistence does not depend on the choice of bare Λ
- has identifiable, nontrivial dependence on finite γ (i.e., it either disappears or changes qualitatively in the γ → ∞ EC limit)
- carries physical information beyond the universal statement "the cosmological constant must be renormalized"

**Failure criterion:**
- Only standard counterterm renormalization appears (bare Λ absorbs all vacuum energy, no finite remainder is independent of this choice)
- The induced vacuum energy has no more physical content than the statement "the cosmological constant must be renormalized" — which is true in ANY QFT and constitutes no derivation
- A vacuum term exists but has no γ-dependence: it is the standard curved-spacetime Dirac determinant result, not a Holst-sector prediction

**Why this gate is nontrivial:** In standard QFT on curved spacetime, the a₀ Seeley-DeWitt coefficient generates a quartic divergence that renormalizes the bare cosmological constant. This is not a prediction — it is a universal requirement. Gate G1 asks whether BEYOND this, the EC+Holst+Dirac theory at finite γ produces a specific, identifiable vacuum contribution that is absent in the γ → ∞ limit and carries physical information about the Holst sector.

**Why the γ-dependence requirement matters:** Without it, Gate G1 could be "passed" trivially by the generic existence of vacuum-energy divergences in any QFT. That would be a meaningless success. The entire point of Branch G is to test whether the Holst sector contributes something novel. If it does not, the result is just the standard cosmological constant problem, and no derivation has been achieved.

### Gate G2 — IR Physicality

**Question:** Does the vacuum-like term survive as a physically meaningful late-time contribution rather than a curvature-local UV artifact?

**Success criterion:**
- The vacuum contribution remains nonzero and physically meaningful in the limit R → 0 (low curvature / late universe)
- It is not exclusively tied to high-curvature structures (R², R_μν R^μν, etc.) that vanish in the IR
- Its existence, sign, and classification (vacuum vs. non-vacuum) are regulator-robust: these must agree between dimensional regularization and proper-time cutoff

**Failure criterion:**
- The term disappears or becomes undefined in the low-curvature limit
- It depends entirely on scheme/subtraction prescription in existence or sign
- It exists only on special backgrounds (e.g., exact de Sitter) with no general late-time meaning

**What "IR physicality" means precisely:** The term must contribute to the effective gravitational equations at late times (low curvature, no early-universe sources) as a genuine constant in the effective Einstein equations, not as a curvature-dependent correction that turns off when curvature vanishes.

### Gate G3 — Dark Energy Viability

**Question:** Does the surviving term behave like acceptable late-time dark energy?

**Success criterion:**
- Positive vacuum energy (de Sitter, not anti-de Sitter)
- Effective equation of state w ≈ −1 (exact or |1+w| < 10⁻² over late-time evolution)
- No instability, ghost, or pathological stress-energy interpretation
- Derivable mapping to Paper 1's phenomenological dark-energy sector

**Failure criterion:**
- Wrong sign (AdS-like): Λ_eff < 0
- Non-vacuum-like behavior: w far from −1, strong time dependence, anisotropic stress
- Dependence on background that prevents clean late-time DE interpretation
- Magnitude not matchable to observed ρ_Λ by any reasonable choice of parameters

**Sub-outcomes (same structure as Track B):**
- **Exact w = −1:** Genuine derived cosmological constant. Major result.
- **Quasi-de Sitter:** |1+w| < 10⁻². Derived evolving dark energy. Still major.
- **Metastable plateau:** Effective Λ with finite but long-lived vacuum. Acceptable.
- **Wrong magnitude:** Right structure but ρ_eff ≫ or ≪ ρ_Λ^obs. Publishable partial result (constrains theory space).

---

## Question 6: What precise result would count as failure?

**Any single gate failure terminates the corresponding claim:**

| Gate failed | Result | Interpretation |
|-------------|--------|----------------|
| Gate G1 fails | No finite-γ vacuum contribution beyond standard CC renormalization | The theory does not derive dark energy. The CC problem is neither solved nor repackaged — it is just the standard CC problem, unchanged by the Holst sector. |
| Gate G2 fails | Vacuum term exists only at high curvature or is scheme-dependent in existence/sign | Early-universe physics only, or no predictive content. Not a dark-energy derivation. |
| Gate G3a fails | Λ_eff < 0 | AdS vacuum. Mechanism works against dark energy. |
| Gate G3b fails | Result is scheme-dependent in sign or classification | No predictive power. |
| Gate G3c fails | w far from −1 | Not vacuum-like. Different dark-sector model, not dark energy. |

**Predeclared failure modes:**

**FM-G1: Pure renormalization only.** The effective action only tells you the cosmological constant must be renormalized. No finite remainder with independent physical meaning. This is the most likely failure mode and would close Branch G immediately.

**FM-G2: High-curvature-only term.** A vacuum-like contribution appears only in the bounce/high-curvature regime and does not persist into the IR. May be interesting for early-universe dynamics but does not solve the dark-energy problem.

**FM-G3: Scheme dependence kills predictivity.** Existence, sign, or classification of the vacuum term depends strongly on regulator or renormalization prescription. No predictive first-principles claim allowed.

**FM-G4: Wrong-sign vacuum.** Effective Λ is negative. Branch fails for dark energy but may still constrain theory space.

**FM-G5: Non-vacuum late-time behavior.** Derived stress-energy gives w far from −1, or no clean perfect-fluid interpretation.

**FM-G6: Trivial one-loop reduction (EARLY KILL — Phase 1).** After exact torsion elimination, the strict one-loop effective action reduces to the standard curved-space Dirac determinant with no physically meaningful finite-γ dependence beyond ordinary renormalization bookkeeping. All three candidate channels (modified background, parity-odd sector, measure corrections) yield no novel Holst content. In this case, Branch G v1 closes at Phase 1 without proceeding to Gates G1–G3. This is not a soft failure — it is the primary expected outcome and the program working as designed. The result would mean that the minimal EC+Holst+Dirac theory at strict one-loop simply reproduces the standard cosmological constant problem, unchanged by the Holst sector.

---

## Renormalization Strategy

**Primary regulator:** Dimensional regularization (d = 4 − 2ε).

**Cross-check:** Proper-time (Schwinger) cutoff.

**What must be regulator-independent to count as physical:**
- Existence or nonexistence of a finite vacuum remainder after renormalization
- Sign of Λ_eff
- Whether Λ_eff depends on γ, m_i, N_f in a nontrivial way
- Classification of late-time behavior

**What may be scheme-dependent (acceptable):**
- Exact numerical value of Λ_eff (this IS the residual fine-tuning question)
- Higher-order curvature coefficients

**Renormalization conditions:**
- In the "no bare Λ" convention: set the bare cosmological constant to zero and determine whether the theory generates a finite vacuum energy
- In the "standard renormalization" convention: impose a renormalization condition on Λ at a chosen scale μ and determine whether the running Λ(μ) has nontrivial content beyond the standard running of any QFT

**Red flag:** If the entire physical content of Branch G reduces to "the cosmological constant runs, and you can choose its value by a renormalization condition," then nothing has been derived. This is FM-G1.

---

## Computation Sequence (Phases)

### Phase 1 — Formal Setup (no numerics)

Tasks:
- Verify whether strict one-loop (Approach B) or Hubbard-Stratonovich saddle (Approach A) is the correct starting point
- Identify the exact Dirac operator whose determinant is computed, after torsion elimination
- Determine what γ-dependent content, if any, enters the one-loop operator
- Read and analyze Chattopadhyay (2023) [2310.10405] in detail
- Write the Seeley-DeWitt expansion to a₂ order for the relevant operator
- Identify which coefficients are sensitive to the Holst/parity-odd sector

Deliverable: one technical memo with the exact operator, its heat-kernel coefficients, and a clear statement of where γ enters (if at all).

**Gate 0 (internal, before continuing):** If Phase 1 shows that the one-loop object has zero novel Holst/torsion content (FM-G6), stop and report this as a soft closure.

### Phase 2 — Local Effective Action

Tasks:
- Compute or organize the heat-kernel coefficients a₀, a₁, a₂ for the torsion-eliminated Dirac operator
- Identify all generated local operators: Λ, R, R², R_μν R^μν, Pontryagin, Gauss-Bonnet
- Determine which are γ-dependent
- Evaluate whether a₀ (the vacuum energy coefficient) carries any information beyond standard QFT

Deliverable: coefficient table for local terms in Γ_eff.

**Gate G1 checkpoint:** Does the a₀ coefficient, after renormalization, leave a finite remainder with physical content?

### Phase 3 — IR Persistence Test

Tasks:
- Take the low-curvature / late-time limit of Γ_eff
- Separate pure Λ-renormalization from any genuinely induced finite remainder
- Test scheme dependence of the remainder
- Test background dependence (FRW → general)

Deliverable: Gate G2 result (yes/no/ambiguous on IR persistence).

### Phase 4 — Cosmological Interpretation (only if Gates G1–G2 pass)

Tasks:
- Derive effective stress-energy from Γ_eff
- Extract ρ_eff, p_eff, w_eff
- Compare to Paper 1 phenomenological ansatz
- Determine magnitude relative to ρ_Λ^obs

Deliverable: Gate G3 result and mapping to Paper 1.

---

## Key Reference

Chattopadhyay (2023) [2310.10405]: One-loop effective action in chiral Einstein-Cartan gravity. This is the most directly relevant existing computation. Phase 1 must begin by understanding what this paper already establishes and what remains to be done.

---

## Predeclared Expectation

The most likely non-failure outcome at this order is not a full derivation of late-time dark energy, but a sharpened statement about whether minimal finite-γ EC+Holst has any nontrivial one-loop gravitational vacuum structure beyond standard renormalization. The most likely outcome overall is FM-G6 (trivial one-loop reduction) or FM-G1 (pure renormalization only). This expectation is recorded here so that the program's success criteria are not unconsciously loosened after results arrive.

---

## If Branch G Fails

If all three failure-mode categories (no novel content, scheme-dependent, wrong sign/magnitude) are realized, the honest end state is:

> In the minimal EC+Holst+Dirac framework at γ = 0.274, neither the condensate route (Track B) nor the one-loop effective-action route (Branch G) yields a first-principles late-time dark-energy derivation. The framework remains phenomenological.

This is an acceptable scientific outcome. It would close the first-principles derivation program for the minimal model while preserving Paper 1's phenomenological framework.

The pair of negative results (Track B + Branch G) constitutes a meaningful map of what this model class does NOT do, and is independently publishable.

---

## Summary Table

| Question | Answer |
|----------|--------|
| Microscopic action | EC + Holst + Dirac, γ = 0.274 fixed, no bare Λ, no extra operators |
| Target object | One-loop gravitational effective action Γ_eff[e] after torsion elimination and fermion integration |
| Key distinction from Track B | No NJL condensate required; target is Γ[g], not ⟨ψ̄iγ⁵ψ⟩ |
| Integration order | ω eliminated exactly → ψ integrated at one loop → heat-kernel expansion |
| Novel content question | Does the Holst/torsion sector contribute anything beyond standard QFT-in-curved-space at one loop? |
| Gate G1 | Finite-γ vacuum term beyond standard CC renormalization |
| Gate G2 | Survives in IR, scheme-robust in existence/sign |
| Gate G3 | Positive, w ≈ −1, mappable to Paper 1 |
| Scope control | Approach B (strict one-loop) ONLY; Approach A requires separate branch |
| Most likely failure | FM-G6 (trivial one-loop reduction, Phase 1 kill) or FM-G1 (pure renormalization) |
| Key reference | Chattopadhyay (2023) [2310.10405] |
| Regulator | Dim reg primary, proper-time cross-check |
