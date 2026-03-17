# Foundation E — Phase 1 Screening

**Date:** 2026-03-14

---

## Purpose

Before committing to heavy derivation work, identify the two most
serious candidate mechanisms for Phase 2 testing.

---

## Screening Criteria

Each candidate is evaluated against three rapid-screening questions:

1. **Does it have a well-defined action?** (Can we write S[g, fields, global vars]?)
2. **Does it clearly evade Weinberg's no-go?** (Weinberg showed that
   local adjustment mechanisms fail because the equations of motion
   don't constrain Λ separately from other curvature terms.)
3. **Is there a natural bounce connection?** (Does the mechanism
   interact with or benefit from the existence of a bounce phase?)

---

## Candidate Screening

### A: Vacuum Energy Sequestering

| Criterion | Assessment |
|-----------|-----------|
| Well-defined action? | **YES** — Kaloper-Padilla action is explicit |
| Evades Weinberg? | **YES** — global variables are outside Weinberg's local framework |
| Natural bounce connection? | **YES** — finite 4-volume requirement aligns with cyclic/bounce cosmology |

**Phase 2 recommendation: YES — strongest candidate.**

Rationale: The sequestering mechanism has a clear, published action
principle. It operates through global (non-local) constraints that
are structurally immune to the barriers identified in A–D. The
requirement that spacetime have finite 4-volume is naturally
satisfied in a bounce cosmology (the universe has finite past
duration from the bounce).

Key Phase 2 question: Does the residual Λ in a bounce cosmology
take a specific (potentially correct) value, or is it still
unconstrained?

### B: 4-Form / Flux Adjustment

| Criterion | Assessment |
|-----------|-----------|
| Well-defined action? | **YES** — Brown-Teitelboim / Bousso-Polchinski |
| Evades Weinberg? | **PARTIALLY** — classical adjustment evades, but landscape is needed |
| Natural bounce connection? | **WEAK** — bounce could trigger membrane nucleation, but connection is loose |

**Phase 2 recommendation: NO (deferred to Phase 3 if A fails).**

Rationale: The mechanism is well-defined but requires a landscape
of vacua. The connection to bounce cosmology is speculative (the
bounce might trigger membrane nucleation, but this requires the
bounce to couple to membrane dynamics, which is an additional
assumption). The landscape requirement makes this more suitable
as a backup than a primary candidate.

### C: Global Constraint (∫R = χ₀)

| Criterion | Assessment |
|-----------|-----------|
| Well-defined action? | **PARTIALLY** — action can be written but variational principle is subtle |
| Evades Weinberg? | **UNCLEAR** — may be equivalent to choosing Λ by hand |
| Natural bounce connection? | **YES** — the bounce contributes a large curvature pulse to ∫R |

**Phase 2 recommendation: YES — second candidate.**

Rationale: The global curvature constraint has the most direct
connection to bounce cosmology. The bounce at ρ ~ M_Pl⁴ produces
a brief but intense positive curvature pulse. If ∫√g R is fixed by
a topological or boundary condition, the late-time curvature (and
hence Λ) is CONSTRAINED by the bounce-era curvature contribution.

This is the most "bounce-specific" mechanism: the bounce DETERMINES
(or at least constrains) the late-time Λ.

Key Phase 2 question: Is χ₀ itself tuned, or is it fixed by the
theory? If χ₀ is a topological invariant, this is powerful. If χ₀
is a free parameter, the mechanism just relocates tuning.

### D: Nonlocal Action (f(□⁻¹R))

| Criterion | Assessment |
|-----------|-----------|
| Well-defined action? | **YES** — Deser-Woodard, Maggiore-Mancarella |
| Evades Weinberg? | **NO** — auxiliary field formulation IS a scalar-tensor theory |
| Natural bounce connection? | **WEAK** — □⁻¹R is sensitive to full history, but mechanism is generic |

**Phase 2 recommendation: NO.**

Rationale: The auxiliary field equivalence means this IS a
scalar-tensor theory. Foundation C already showed that scalar-tensor
theories on FRW are generically absorbed by universality. The
nonlocal formulation is mathematically interesting but physically
equivalent to what we've already tested.

### E: Boundary / Topological

| Criterion | Assessment |
|-----------|-----------|
| Well-defined action? | **NO** — no calculational framework exists |
| Evades Weinberg? | **UNKNOWN** |
| Natural bounce connection? | **POTENTIALLY** — but too speculative to assess |

**Phase 2 recommendation: NO (too speculative for current program).**

Rationale: Without a well-defined action, this cannot be tested
systematically. The idea is intriguing (the bounce as a "boundary"
that fixes vacuum data) but lacks the mathematical structure needed
for concrete calculations.

---

## Phase 2 Selections

### Primary: Candidate A — Vacuum Energy Sequestering

**Why:** Best-developed framework. Clear action principle. Natural
finite-4-volume connection to bounce cosmology. Published literature
to build on. Concrete tests available.

**Phase 2 tasks:**
1. Write the Kaloper-Padilla action with EC/PGT gravity sector
2. Compute the global constraint equations with torsion
3. Evaluate the residual Λ in a bounce cosmology
4. Test radiative stability
5. Identify predictions

### Secondary: Candidate C — Global Curvature Constraint

**Why:** Most direct bounce-Λ connection. The bounce curvature pulse
constrains late-time Λ. Simple enough to test quickly.

**Phase 2 tasks:**
1. Write the constrained action with Lagrange multiplier
2. Compute ∫√g R through a bounce phase
3. Determine whether χ₀ is tuned or fixed
4. Check consistency with known cosmological evolution
5. Compare residual Λ with observations

---

## Decision Points

- If Candidate A passes Tests E1–E3: proceed to full Phase 2 analysis
- If Candidate A fails E1 (hidden tuning in μ₁, μ₂): switch to C
- If both A and C fail: reassess Foundation F (bounce-linked DE sector)
- If A produces a genuine bounce-Λ relation: this is a major result
