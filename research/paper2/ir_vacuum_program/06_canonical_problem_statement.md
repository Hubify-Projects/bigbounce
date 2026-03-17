# Canonical Problem Statement

**Date:** 2026-03-13
**Version:** v3 (FROZEN)
**Status:** LOCKED — changes only by versioned addendum (see 06a_frozen_assumptions_and_change_log.md)
**Purpose:** Answer 7 questions with zero ambiguity before any computation begins

---

## What This Memo Does Not Assume

- Does not assume Φ = ⟨ψ̄ iγ⁵ψ⟩ ≠ 0
- Does not assume the Holst term uniquely drives the pseudoscalar channel
- Does not assume the condensate persists after spin density vanishes
- Does not assume w = −1
- Does not assume a regulator-independent vacuum scale without explicit check
- Does not assume the pseudoscalar channel dominates over competing channels (scalar, vector, tensor) without Fierz analysis

---

## Question 1: What exact microscopic action are we starting from?

The Einstein-Cartan-Holst action minimally coupled to N_f Dirac fermions:

```
S = S_grav[e, ω] + S_ferm[e, ω, ψ]
```

where:

```
S_grav = (M_Pl²/2) ∫ [ε_{IJKL} + (2/γ) η_{I[K} η_{L]J}] e^I ∧ e^J ∧ F^{KL}[ω]

S_ferm = ∫ d⁴x |e| [ψ̄_i iγ^μ D_μ ψ_i − m_i ψ̄_i ψ_i]
```

with D_μ = ∂_μ + ¼ ω_μ^{IJ} γ_I γ_J. The index i = 1, ..., N_f runs over fermion species. γ is the Barbero-Immirzi parameter, treated as a **fixed constant** (not a dynamical field) throughout this program.

**No additional tree-level operators** are introduced in the starting action. No Nieh-Yan boundary term (it vanishes for compact spacetimes without boundary). No higher-curvature corrections. No scalar fields. Renormalization may require the standard counterterm structure of the effective action (curvature-squared terms, etc.), but no extra dynamical sector is assumed at the outset.

**Convention lock:** We use (+, −, −, −) metric signature, γ⁵ = iγ⁰γ¹γ²γ³ with (γ⁵)² = 1, and κ² = 8πG = M_Pl⁻².

---

## Question 2: What fields are dynamical?

**In the microscopic theory:** all three — tetrad, spin connection, and fermions — are dynamical fields in the first-order variational principle.

**In the computation:** we evaluate the fermion determinant on a prescribed homogeneous background geometry. The tetrad remains the gravitational field variable of the effective action Γ_eff[e, σ, π], but in the first pass we work on a fixed background to extract the induced vacuum structure.

| Field | Microscopic status | Computational treatment |
|-------|-------------------|------------------------|
| e^I_μ (tetrad) | Dynamical | Prescribed background (first pass); effective action is a functional of e |
| ω^{IJ}_μ (spin connection) | Algebraic (non-propagating in EC) | Eliminated exactly via its own EOM |
| ψ_i (Dirac fermions) | Dynamical | Integrated out at one loop |

The goal is to infer the induced gravitational effective action as a functional of e^I_μ, not merely a matter effective potential on a frozen geometry. The background approximation is a computational first step, not an ontological claim.

---

## Question 3: What is being integrated out, and in what order?

Each step is labeled by its logical status: **exact** vs. **approximation**.

**Step 1 — Torsion elimination:**
- **Status: Exact classical field elimination.** The spin connection ω is non-propagating in EC gravity. Its EOM is algebraic — no approximation is involved.

```
ω^{IJ}_μ = ω̊^{IJ}_μ[e] + K^{IJ}_μ[ψ̄, ψ, γ]
```

Substituting back yields the reduced action with three four-fermion couplings:

```
L_4f = −G_V(γ) (ψ̄γ^μψ)² − G_A(γ) (ψ̄γ^μγ⁵ψ)² − G_VA(γ) (ψ̄γ^μψ)(ψ̄γ_μγ⁵ψ)
```

The coupling constants are (to be verified in Computation 2):

```
G_V = (3κ²/32) × γ²/(1+γ²)
G_A = (3κ²/32) × 1/(1+γ²)        [VERIFY SIGN AND PREFACTOR]
G_VA = (3κ²/32) × γ/(1+γ²)        [VERIFY — THIS IS THE PARITY-SENSITIVE COUPLING]
```

Limits: γ → ∞ gives G_VA → 0, recovering standard EC. γ → 0 gives G_V → 0.

**Step 2 — Hubbard-Stratonovich transformation:**
- **Status: Exact auxiliary-field rewriting.** No information is gained or lost. Introduces scalar σ and pseudoscalar π to linearize the four-fermion terms:

```
S_ferm = ∫ d⁴x √−g [ψ̄(iγ^μD_μ − m − σ − iγ⁵π)ψ + V_tree(σ, π)]
```

**Step 3 — Fermion integration:**
- **Status: Semiclassical truncation (one-loop).** This is the first genuine approximation. Integrate out ψ to get:

```
Γ_eff[σ, π; g] = V_tree(σ, π) − i Tr ln[iγ^μD_μ − M_eff(σ, π)]
```

- **Status of V_eff extraction: Renormalized effective-potential approximation.** The fermion determinant is evaluated using heat-kernel expansion on the curved background, with dimensional regularization and renormalization at scale μ.

**Approximation stack (explicit):**
1. Torsion elimination — exact
2. Hubbard-Stratonovich — exact rewriting
3. Fermion determinant — one-loop truncation (first semiclassical approximation)
4. Heat-kernel expansion — adiabatic/Seeley-DeWitt expansion to specified order
5. Renormalization — scheme-dependent; physical conclusions must survive cross-check

A referee should judge the result by the reliability of steps 3–5, not by verbal claims downstream.

---

## Question 4: What is the candidate condensate / order parameter?

**The primary order parameter is the pseudoscalar bilinear:**

```
Φ ≡ ⟨ψ̄ iγ⁵ψ⟩
```

This is the vacuum expectation value of the auxiliary field π at the minimum of V_eff:

```
π* = argmin_{π} V_eff(σ*(π), π)
```

with σ* determined self-consistently by ∂V_eff/∂σ = 0.

**Why focus on this channel first?** The Holst-dependent interaction contributes most directly to parity-sensitive axial/pseudoscalar structures after torsion elimination. In standard EC (γ → ∞), the scalar condensate ⟨ψ̄ψ⟩ already exists; the pseudoscalar channel is the candidate for genuinely new vacuum structure.

**Competing channels are acknowledged and will be checked.** The scalar channel (⟨ψ̄ψ⟩), mixed scalar-pseudoscalar competition, and axial-vector/tensor channels after Fierz rearrangement must all be examined at the effective-action stage (Computation 3). The pseudoscalar is not selected because it is narratively convenient — it is the first channel to investigate because it is the one most directly sensitive to the Holst-dependent coupling. If the Fierz analysis shows that a different channel dominates, the order parameter choice will be revised.

**Caution:** We do not yet know whether G_VA is large enough, whether V_eff actually has a minimum with π* ≠ 0, or whether the pseudoscalar channel is even the most attractive channel after full Fierz rearrangement. Until Computation 5 is complete, the statement "the Holst term drives a pseudoscalar condensate" is a **hypothesis**, not a result.

---

## Question 5: What symmetry allows or forbids the condensate?

**This is the most delicate part of the setup. Read carefully.**

Under parity P, the fermion bilinears transform as:
- ψ̄ψ → +ψ̄ψ (scalar, P-even)
- ψ̄ iγ⁵ψ → −ψ̄ iγ⁵ψ (pseudoscalar, P-odd)

### Standard EC (γ → ∞):

In the γ → ∞ Einstein-Cartan limit, the torsion-induced four-fermion sector contains only parity-even combinations in the reduced action. The effective potential V_eff(σ, π) satisfies V_eff(σ, π) = V_eff(σ, −π). Therefore, within this channel truncation, π = 0 remains a stationary point of V_eff. Accordingly, the standard expectation in this truncation is a nontrivial minimum of the form (σ* ≠ 0, π* = 0), i.e., chiral symmetry breaking without spontaneous parity breaking.

### With Holst term (finite γ):

After torsion elimination, the Holst-dependent interaction generates in the reduced interaction basis the G_VA coupling, which is parity-sensitive. The key computational question — **not yet answered** — is what this coupling does to the effective potential:

**Possibility A:** The G_VA term, after Fierz rearrangement and Hubbard-Stratonovich transformation, induces an explicit odd-power term in π (e.g., a σπ cross-coupling or a term linear in π). In this case, V_eff(σ, π) ≠ V_eff(σ, −π), the π → −π degeneracy would be removed, and a minimum at π* ≠ 0 would become structurally possible.

**Possibility B:** The G_VA term modifies only the even coefficients of the effective potential (e.g., changing the coefficient of π² or π⁴). In this case, the π → −π symmetry of V_eff is preserved, π = 0 remains a stationary point, and whether condensation occurs depends on whether the modified even coefficients make the origin unstable — not on explicit symmetry breaking. The Holst sector would change whether condensation happens but not literally break the sign symmetry.

**What we claim at this stage:** The Holst-dependent interaction modifies the pseudoscalar channel. Whether this modification takes the form of explicit symmetry breaking in V_eff (Possibility A) or modified even coefficients (Possibility B) is determined by the Fierz rearrangement in Computation 3. Both possibilities can in principle yield Φ ≠ 0, but through different mechanisms, and the interpretation is different.

**What we do not claim:** We do not claim that the Holst term "breaks parity" in the microscopic action. The Holst term is not treated here as an explicit microscopic parity-breaking matter interaction; its physical parity sensitivity arises only after coupling to fermions and reducing the torsion sector. The parity properties of the reduced effective action are a derived consequence, not an input assumption.

**Bottom line:** The Holst-dependent reduced interaction is treated as modifying the pseudoscalar channel. Whether that modification produces (i) explicit π → −π asymmetry in the effective potential or instead (ii) only changes the even coefficients controlling instability of the origin is a derived question to be settled by the Fierz-rearranged auxiliary-field analysis. At this stage we claim only that the Holst sector may permit or bias pseudoscalar condensation; we do not yet claim that it forces it.

---

## Question 6: What observable low-energy quantity would count as success?

**Three gates, in order. All must pass.**

### Gate 1: Condensate Existence

The renormalized effective potential V_eff(σ, π), evaluated at curvature scales characteristic of the bounce regime, admits a stationary point (σ*, π*) with π* ≠ 0, and the Hessian H_ij = ∂_i ∂_j V_eff |_{(σ*, π*)} is positive definite. This establishes a genuine local minimum rather than a saddle or flat direction.

**Note:** "Curvature scales characteristic of the bounce regime" rather than a specific value R ~ M_Pl², because the bounce solutions may span a range depending on ρ_c.

### Gate 2: Vacuum Persistence

The minimum (σ*, π*) persists when R → 0 and the fermion spin source s → 0.

**Precise criterion:** After setting the explicit late-time spin density s → 0, the renormalized effective potential V_eff(σ, π; R = 0, s = 0) still has a local minimum at (σ*, π*) ≠ (0, 0), with:
- H_ij = ∂_i ∂_j V_eff |_{(σ*, π*)} positive definite (stable minimum)
- ΔV ≡ V_eff(σ*, π*) − V_eff(0, 0) ≠ 0 (the condensate vacuum differs from the trivial vacuum)

At Gate 2, ΔV ≠ 0 is a structural criterion showing that the nontrivial vacuum remains distinct from the trivial one after the explicit source is removed. The sign and phenomenological viability of that vacuum energy are imposed only at Gate 3.

If the minimum is metastable (local but not global), the tunneling rate Γ_tunnel must satisfy Γ_tunnel⁻¹ ≫ t_universe ≈ 4.4 × 10¹⁷ s.

**What "persists" means precisely:** The system remains in a self-sustaining nontrivial vacuum after the external source is removed. Having been prepared in the condensate vacuum by early-universe dynamics, it does not relax to the trivial vacuum on cosmological timescales.

### Gate 3: Vacuum-Like Stress-Energy

Derive T_μν^eff from the renormalized effective action Γ_eff. For Gate 3, the auxiliary-field description is treated as the effective low-energy representation of the condensate sector, from which the homogeneous stress-energy tensor is extracted. In homogeneous FRW background, extract ρ_Φ and p_Φ.

**Precise criteria:**

(a) **Positive vacuum energy:** The condensate contribution to the renormalized vacuum energy density, extracted from the effective action and equivalent in the homogeneous limit to the value of the effective potential at the relevant minimum, must satisfy ρ_Φ > 0 (de Sitter, not anti-de Sitter).

(b) **Predictive (not UV-dominated):** The following conclusions must be regulator-independent to count as physical: existence of the nontrivial minimum, its local stability, the sign of the condensate vacuum energy, and the classification of the late-time behavior as exact, quasi-de Sitter, or metastable. Specifically: these must agree between dimensional regularization and proper-time cutoff schemes. If they do not, the result has no predictive content.

(c) **Vacuum-like equation of state:** |1 + w_Φ| < ε over the range a_transition < a < a_0, where:
- w_Φ ≡ p_Φ/ρ_Φ
- ε = 10⁻² for theory-stage success (demonstrating approximate de Sitter behavior)
- ε can be tightened later if cosmological data warrants it
- a_transition is defined dynamically as the epoch after which the condensate trajectory remains within the late-time basin of attraction of the relevant minimum

**What "success" means in practice:** One of three sub-outcomes:
- **Exact w = −1:** The condensate is frozen at its minimum with no residual dynamics. Equivalent to a cosmological constant.
- **Quasi-de Sitter (|1+w| < 10⁻²):** Slowly varying condensate. Observationally indistinguishable from Λ at current precision, but potentially distinguishable by next-generation surveys.
- **Metastable plateau:** The condensate sits in a local minimum with finite but cosmologically long lifetime. Behaves as Λ for practical purposes.

All three sub-outcomes count as Gate 3 success. Failure is |1 + w| ~ O(1) or w not well-defined (e.g., due to strong oscillations about the minimum, non-perfect-fluid stress-energy, or significant anisotropic stress from gradient terms).

### Full success criterion (all three gates passed):
The spin-torsion condensate produces a vacuum energy

```
ρ_Φ = V_eff(σ*, π*) > 0,   regulator-independent,   |1 + w| < 10⁻²
```

that can in principle be matched to the phenomenological Λ in Paper 1's cosmological fits.

---

## Question 7: What precise result would count as failure?

**Any single gate failure terminates the corresponding claim:**

| Gate failed | Result | Interpretation |
|-------------|--------|----------------|
| Gate 1 fails | No nontrivial minimum in V_eff at any curvature, or pseudoscalar channel is not the dominant attractive channel | Condensate mechanism does not work as hypothesized. The four-fermion coupling from torsion is subcritical, or a different channel dominates. |
| Gate 2 fails | Minimum exists at high R but disappears at R → 0 | Condensate is transient. Framework produces early-universe physics but not late-time dark energy. |
| Gate 3a fails | V_eff(σ*, π*) < 0 | Wrong sign — AdS vacuum, not dS. Mechanism works against dark energy. |
| Gate 3b fails | Existence or sign of ρ_Φ depends on regulator choice | UV-dominated or scheme-dependent. No predictive power. Cosmological constant problem repackaged, not solved. |
| Gate 3c fails | |1 + w| ~ O(1) | Not vacuum-like. Stress-energy is matter-like or radiation-like. |

**Partial failures that are still publishable:**
- Gate 1 passes, Gate 2 fails: publish as "transient condensate in bouncing cosmology" — interesting early-universe physics
- Gates 1–2 pass, Gate 3c fails (w ≠ −1 but |1+w| moderate): publish as "dynamical dark energy from torsion condensate" — evolving dark sector, changes Paper 1's fits
- Gates 1–2 pass, Gate 3a fails (AdS): publish as negative result — important for the field
- Pseudoscalar channel subdominant but scalar channel condenses: revise order parameter, re-evaluate

**Total failure:** Gate 1 fails outright in all channels. The framework remains phenomenological. Paper 1 stands as-is with w = −1 as an assumption. This is an acceptable scientific outcome.

---

## Renormalization Strategy (Decided Upfront)

**Primary regulator:** Dimensional regularization (d = 4 − 2ε) throughout.

**Rationale:** The NJL model is non-renormalizable, so results depend on regularization scheme. Dimensional regularization is preferred because:
1. It respects gauge invariance and diffeomorphism invariance
2. It does not introduce a hard UV cutoff (avoids Λ⁴ artifacts)
3. It cleanly separates the finite (physical) part of V_eff from the divergent part
4. It is standard for heat-kernel calculations in curved spacetime

**Cross-check:** After the main calculation, repeat with proper-time cutoff regularization.

**What must be regulator-independent to count as physical:**
- Existence or nonexistence of a nontrivial minimum in V_eff
- Sign of the Hessian H_ij at the minimum (local stability)
- Sign of the vacuum energy offset ΔV = V_eff(σ*, π*) − V_eff(0, 0)
- Presence or absence of a source-independent vacuum offset after renormalization
- Qualitative symmetry structure of the effective potential (whether odd terms in π appear)
- Classification of late-time behavior as exact w = −1, quasi-de Sitter, or metastable

**What may be scheme-dependent (and that is acceptable):**
- The exact numerical value of ρ_Φ (this is the residual fine-tuning question, separate from existence)
- Higher-order coefficients in the potential

**Red flag:** If the very existence of the condensate (Gate 1), or the sign of the vacuum energy (Gate 3a), depends on the regulator choice, the result has no predictive content and the program has failed at the level of robustness.

**Renormalization conditions:** Set at the scale μ = M_eff(σ*, π*), the effective fermion mass at the condensate minimum. Running to μ → 0 (deep IR) must not destabilize the minimum.

---

## Summary Table

| Question | Answer |
|----------|--------|
| Microscopic action | EC + Holst + Dirac, first-order formalism, γ fixed, no extra tree-level operators |
| Dynamical fields | All dynamical microscopically; tetrad evaluated on prescribed background in first pass |
| Integrated out | ω (exact, algebraic), then ψ (one-loop semiclassical truncation) |
| Order parameter | Φ = ⟨ψ̄ iγ⁵ψ⟩ (pseudoscalar condensate) — first channel to check, not assumed dominant |
| Symmetry | Holst sector modifies pseudoscalar channel; whether by explicit odd terms or modified even coefficients is TBD (Computation 3) |
| Success | Three quantitative gates: condensate exists (Hessian > 0), persists at s = 0 (ΔV ≠ 0), gives |1+w| < 10⁻² |
| Failure | Any gate fails; most likely: subcritical coupling (Gate 1) or transient condensate (Gate 2) |
| Regulator | Dimensional regularization primary, proper-time cross-check; existence/sign/classification must be scheme-independent |
