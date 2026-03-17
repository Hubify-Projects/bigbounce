# Foundation E — Structural Tests

**Date:** 2026-03-14

---

## Test Framework

Each candidate mechanism must pass five structural tests before
proceeding to detailed calculation.

---

## Test E1 — Hidden Tuning Relocation

### Question
Does the mechanism genuinely neutralize vacuum energy, or does it
relocate the fine-tuning to another parameter?

### What to check
- Are there free parameters (mass scales, coupling constants) that
  must be tuned to reproduce Λ ~ 10⁻¹²² M_Pl⁴?
- If the mechanism introduces global variables (Lagrange multipliers,
  integration constants), do these carry the fine-tuning?
- Can the mechanism handle an ARBITRARY vacuum shift δΛ from a phase
  transition without retuning?

### Verdicts
- **PASS:** Mechanism absorbs arbitrary constant vacuum shifts with
  no parameter adjustment. Residual Λ depends on history, not tuning.
- **FAIL_HIDDEN_TUNING:** Fine-tuning is relocated to boundary
  conditions, auxiliary parameters, or the choice of global variables.

### Application to candidates
- **Sequestering (A):** The scales μ₁, μ₂ must be examined. If
  Λ_residual ~ μ₁⁴/μ₂⁴, are μ₁, μ₂ natural?
- **4-form (B):** The flux quantum Δq must be small enough. Is the
  number of flux values fine-tuned?
- **Global constraint (C):** Is χ₀ a tuned parameter?
- **Nonlocal (D):** Is the function f(□⁻¹R) fine-tuned?
- **Boundary (E):** Are boundary data tuned?

---

## Test E2 — Radiative Stability of Vacuum Energy

### Question
Is the mechanism stable against radiative corrections from matter
loops?

### What to check
- Matter loops contribute δΛ ~ M⁴/(16π²) for each particle species
  with mass M. Does the mechanism cancel these WITHOUT knowing the
  particle spectrum in advance?
- If a new heavy particle is added to the theory, does the mechanism
  automatically adjust, or must parameters be retuned?
- Does the mechanism work order by order in perturbation theory,
  or only non-perturbatively?

### Verdicts
- **PASS:** Mechanism cancels arbitrary constant vacuum shifts from
  any source, independent of the matter content.
- **FAIL_RADIATIVE:** Mechanism requires knowledge of the particle
  spectrum or breaks down at loop level.

### Application to candidates
- **Sequestering (A):** The σ₂ constraint averages L_matter over
  spacetime. Does this capture loop corrections?
- **4-form (B):** Flux adjustment is classical. Does it survive
  quantum corrections to q?
- **Global constraint (C):** ∫R = χ₀ is a classical constraint.
  Is it stable under renormalization?

---

## Test E3 — Consistency with Bounce Cosmology

### Question
Is the mechanism compatible with spin-torsion bounce dynamics?

### What to check
- The bounce requires ρ → ρ_max ~ M_Pl⁴ at the bounce point,
  with torsion-driven repulsion preventing singularity formation.
  Does the global mechanism interfere with this?
- Does the mechanism require Λ_eff = 0 (which conflicts with
  observations) or does it allow Λ_eff ~ 10⁻¹²² M_Pl⁴?
- Does the bounce contribute to the global variables (spacetime
  4-volume, integrated curvature) in a way that is calculable?
- Does torsion at the bounce modify the global constraint?

### Verdicts
- **PASS:** Mechanism is fully compatible with bounce dynamics.
  The bounce phase contributes to but does not break the global
  constraint.
- **FAIL_BOUNCE_INCOMPATIBLE:** Mechanism requires conditions
  that conflict with the bounce (e.g., no high-curvature phase,
  no torsion, specific topology).

### Application to candidates
- **Sequestering (A):** The 4-volume integral ∫√g includes the
  bounce era. The bounce has very high curvature but small
  4-volume (brief duration). Likely compatible.
- **4-form (B):** Flux is a constant. The bounce doesn't change
  it. Compatible.
- **Global constraint (C):** ∫√g R includes a large R pulse from
  the bounce. This CONSTRAINS the late-time R (and hence Λ).
  Potentially interesting.

---

## Test E4 — Reduction to Ordinary ΛCDM or Quintessence

### Question
After all analysis, does the mechanism reduce to simply choosing
a cosmological constant or a quintessence-like scalar?

### What to check
- Can the global variables be "solved for" to produce a local
  effective theory with a cosmological constant?
- If auxiliary fields are introduced to make the action local,
  do they propagate? If so, the mechanism IS a scalar-tensor theory.
- Does the mechanism's prediction for cosmic evolution differ
  from ΛCDM in any measurable way?

### Verdicts
- **PASS:** Mechanism produces cosmological evolution that is
  DIFFERENT from simply inserting Λ. The difference is structural
  (not parametric).
- **FAIL_LOCAL_COLLAPSE:** After analysis, mechanism is equivalent
  to ΛCDM with a specific Λ value, or to a quintessence model.

---

## Test E5 — Predictive Power Beyond Parameter Tuning

### Question
Does the mechanism make predictions beyond simply fitting Λ_observed?

### What to check
- Does the mechanism predict RELATIONS between Λ and other
  physical quantities (particle masses, phase transition scales,
  spacetime topology, bounce parameters)?
- Does it constrain the equation of state w(z)?
- Does it predict observable consequences at late times or
  near phase transitions?
- Can it be falsified by observations that don't simply measure Λ?

### Verdicts
- **PASS:** Mechanism makes at least one prediction beyond the
  value of Λ. This prediction is in principle testable.
- **FAIL_NO_PREDICTIVITY:** Mechanism can fit any Λ with
  appropriate parameter choice. No additional predictions.

---

## Verdict Labels

| Verdict | Meaning |
|---------|---------|
| SURVIVES_PHASE1 | Passes all five tests. Proceed to Phase 2. |
| FAIL_HIDDEN_TUNING | Fine-tuning relocated, not eliminated |
| FAIL_RADIATIVE | Breaks down under radiative corrections |
| FAIL_BOUNCE_INCOMPATIBLE | Conflicts with spin-torsion bounce |
| FAIL_LOCAL_COLLAPSE | Reduces to ΛCDM or quintessence |
| FAIL_NO_PREDICTIVITY | No structural predictions beyond Λ |

---

## Phase 1 Screening Strategy

Apply tests in order: E1 → E2 → E3 → E4 → E5.

A candidate that fails E1 (hidden tuning) should not be tested
further — the tuning problem is the entire point.

A candidate that passes E1–E2 but fails E3 (bounce incompatibility)
is still interesting as a general CC mechanism, but is not relevant
to this research program specifically.

E4 and E5 are the hardest tests and require the most detailed
analysis. Only candidates surviving E1–E3 should be subjected
to these.
