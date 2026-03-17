# Foundation G — Structural Tests

**Date:** 2026-03-15

---

## Test Framework

Each candidate must pass six structural tests. Tests are applied
in order; early failure terminates evaluation.

---

## Test G1 — Bounce Relevance

### Question
Does the spin-torsion bounce genuinely affect the global variable
or branch selection? Or would ANY cosmological scenario (singular
Big Bang, inflation, generic initial conditions) give the same
result?

### How to check
- Remove the bounce from the cosmology. Replace with:
  (a) a standard Big Bang singularity
  (b) a generic inflationary epoch
- Does the global variable/branch selection change?
- If the answer is the SAME without the bounce, the bounce is
  decorative.

### Key discriminator
The bounce is relevant ONLY IF the selection mechanism uses a
property UNIQUE to the bounce:
- H = 0 at a finite-density surface (unique to bounces)
- Torsion-driven repulsion at ρ_crit (unique to spin-torsion)
- Finite 4-volume per cycle (unique to cyclic bounces)
- Nonsingular regularity (unique to bounce, absent in singularity)

If the mechanism uses only "high density" or "early universe" —
inflation provides the same environment. Not bounce-specific.

### Verdict
- **PASS:** Mechanism changes qualitatively when bounce is removed.
- **FAIL_BOUNCE_IRRELEVANT:** Same result with or without bounce.

---

## Test G2 — Hidden Tuning

### Question
Is the selected vacuum value genuinely DETERMINED by the mechanism,
or does it repackage a free parameter as a "selection"?

### How to check
Count the free parameters in the mechanism:
- How many are needed to specify the global variable?
- How many are determined by the bounce condition?
- How many remain free and must be tuned to match Λ_obs?

If (free parameters after bounce condition) ≥ (free parameters
before bounce condition), the bounce does not reduce tuning.

### Key discriminator
Genuine determination: the bounce condition FIXES the global
variable in terms of known physics (M_Pl, ρ_crit, torsion
couplings). No additional free parameter needed.

Hidden tuning: the bounce condition RELATES the global variable
to another free parameter (coupling constant, boundary value,
topological number) that itself must be tuned.

### Verdict
- **PASS:** Free parameter count decreases; Λ is narrowed.
- **FAIL_HIDDEN_TUNING:** Free parameter count unchanged; tuning
  relocated.

---

## Test G3 — Generic Sequestering Collapse

### Question
Is the mechanism essentially standard Kaloper-Padilla sequestering
(or another known framework) with the bounce added as a narrative
motivation?

### How to check
- Write the mechanism WITHOUT mentioning the bounce.
- Is it a known framework? (sequestering, 4-form, unimodular, ...)
- Can the same framework be applied to ANY cosmology?
- Does the bounce add any MATHEMATICAL content (new equation,
  new constraint, new variable) or only MOTIVATION?

### Key discriminator
Generic collapse occurs when: the bounce enters the mechanism
only through the sentence "the bounce provides finite 4-volume"
or "the bounce provides a high-energy epoch" — statements that
could be made about inflation, reheating, or any early-universe
scenario.

Genuine novelty requires: the bounce introduces a SPECIFIC
CONDITION (not available from other scenarios) that modifies the
mathematical content of the framework.

### Verdict
- **PASS:** Mechanism has mathematical content that requires the bounce.
- **FAIL_GENERIC_COLLAPSE:** Mechanism is known framework + bounce
  narrative.

---

## Test G4 — Variational / Branch Consistency

### Question
Is the action principle, variational structure, or branch-selection
logic mathematically well-defined?

### How to check
- Can the action be varied consistently (boundary terms, global
  variables, local fields)?
- If branch selection: is the selection rule well-defined? (Not
  "the bounce somehow selects" but a concrete criterion.)
- Are there ghost instabilities, gradient problems, or Ostrogradski
  issues?
- Does the mechanism respect causality? (Or does it require
  knowledge of the future, as in some sequestering formulations?)

### Key discriminator
The mechanism must have a concrete mathematical formulation. "The
bounce selects a vacuum" is not a mechanism — it is a wish. The
RULE by which the bounce selects must be stated and shown to be
consistent.

### Verdict
- **PASS:** Well-defined action/selection rule, no pathologies.
- **FAIL_INCONSISTENT:** Ill-defined, acausal, or pathological.

---

## Test G5 — Predictive Narrowing

### Question
Does the mechanism narrow the allowed range of Λ compared to
the generic expectation?

### How to check
- Without the mechanism: Λ ranges from -M_Pl⁴ to +M_Pl⁴.
- With the mechanism: what is the allowed range of Λ?
- Is the range narrower? By how many orders of magnitude?
- If the mechanism produces Λ = 0 exactly: is this consistent with
  observations (Λ_obs ≠ 0)?

### Key discriminator
Meaningful narrowing: the mechanism reduces the allowed Λ range by
at least ~50 orders of magnitude (from 10¹²² down to 10⁷⁰ or less).

Trivial narrowing: the mechanism says "Λ is some function of
parameters" without constraining those parameters. The range is
unchanged.

### Verdict
- **PASS:** Allowed Λ range is meaningfully narrowed.
- **FAIL_NO_NARROWING:** Λ range is unchanged or trivially restricted.

---

## Test G6 — Cosmology Compatibility

### Question
Can the mechanism coexist with observed cosmological evolution
(radiation → matter → DE domination) and with the spin-torsion
bounce?

### How to check
- Does the mechanism modify the Friedmann equations in a way that
  conflicts with BBN, CMB, or structure formation?
- Does the mechanism require the universe to recollapse (which may
  conflict with observations of accelerating expansion)?
- Does the mechanism interfere with the bounce dynamics (torsion
  repulsion, maximal density)?
- Is the selected Λ compatible with Λ_obs ~ 10⁻¹²² M_Pl⁴?

### Verdict
- **PASS:** Compatible with bounce + standard cosmological evolution.
- **FAIL_INCOMPATIBLE:** Conflicts with observations or bounce dynamics.

---

## Evaluation Order

```
G1 (bounce relevance)
  → if FAIL: stop, verdict FAIL_BOUNCE_IRRELEVANT

G3 (generic sequestering collapse)
  → if FAIL: stop, verdict FAIL_GENERIC_COLLAPSE

G4 (variational consistency)
  → if FAIL: stop, verdict FAIL_INCONSISTENT

G2 (hidden tuning)
  → if FAIL: stop, verdict FAIL_HIDDEN_TUNING

G5 (predictive narrowing)
  → if FAIL: stop, verdict FAIL_NO_NARROWING

G6 (cosmology compatibility)
  → if FAIL: stop, verdict FAIL_INCOMPATIBLE

All pass → SURVIVES_PHASE1
```

G1 and G3 are applied first because they are the most likely failure
modes. If the bounce is irrelevant or the mechanism is generic
sequestering in disguise, there is no point testing further.
