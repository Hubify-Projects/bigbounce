# Branch O: First Calculation Target

**Date:** 2026-03-16

---

## Selection

No candidate is recommended for Phase 2.

---

## Rationale

All seven candidates fail the OOM screening. The failures are
structural, not parametric — no reasonable parameter adjustment
can save any candidate.

### The hierarchy of failures:

**Candidates B, C, E, F, G — DEAD at Test O2 (not bounce-specific):**
These mechanisms are generic to any hot cosmology. The bounce is
decorative. No calculation can change this because the mechanisms
explicitly don't depend on bounce parameters.

**Candidate A — DEAD at Test K2 (hierarchy):**
The first-order phase transition can be triggered by bounce
curvature (marginally bounce-specific for ECH), but the resulting
vacuum energy ρ_DE = ΔV is set by hidden-sector parameters with
no connection to the bounce. A Phase 2 calculation of the
transition dynamics would give: "the transition occurs if
|ξ|R_b > barrier height." This is trivially satisfied (R_b ~ M_Pl²
overwhelms any sub-Planckian barrier). The result is already known
at OOM level. No useful new information from a detailed calculation.

**Candidate D — DEAD at Test K2 (hierarchy) for ECH; timing-
marginal for PGT:**
The PGT bounce has enough duration for moderate-barrier tunneling
(S_E < 80). But even if the tunneling calculation is done in
detail, the outcome is: "the field tunnels to the true vacuum
during the PGT bounce if S_E < 80." The vacuum energy of the
true vacuum is STILL set by hidden-sector parameters. Knowing
the exact S_E threshold doesn't help because the threshold tells
us nothing about ρ_DE.

---

## What a Phase 2 Calculation Could Determine

For the least-dead candidate (D, PGT tunneling):

**Calculation:** Solve the CdL bounce equation in a time-dependent
background R(t) = R_b/(1 + m_T²t²)^n for a specific hidden-sector
potential V(χ). Determine the exact threshold S_E^{crit} below
which the transition completes during the bounce.

**Result:** S_E^{crit} = f(m_T, ξ, potential shape). A number
between 1 and 100.

**What this tells us:** Whether a specific hidden-sector potential
has its false vacuum destabilized by the PGT bounce. This is a
compatibility test (Branch I territory), not a prediction.

**What this does NOT tell us:** The vacuum energy of the resulting
state. The connection to ρ_DE. Any predictive content.

**Estimated effort:** 2-3 days for the numerical CdL calculation.

**Expected outcome:** A number (S_E^{crit} ~ 50-80) that
constrains hidden-sector model space but provides no new physics
insight for the bounce-DE connection.

**Risk-reward assessment:** LOW reward for MODERATE effort.
The calculation would produce a numerical constraint on hidden-
sector models compatible with the PGT bounce, which is a minor
addition to Branch I (compatibility) territory. It does not
advance the bounce→DE program.

---

## If Forced to Pick One Calculation

If a Phase 2 calculation MUST be done (against the recommendation),
the least wasteful option is:

**Target: Gravitational particle production spectrum in the PGT
bounce for a hidden-sector scalar.**

This addresses the cleanest question: how much hidden-sector
energy does the bounce produce?

```
Calculation: Solve the mode equation
  χ̈_k + 3Hχ̇_k + (k²/a² + m² + ξR)χ_k = 0
through the PGT bounce, compute Bogoliubov coefficients β_k,
integrate to get ρ_h = ∫ dk k² |β_k|² ω_k / (2π²a³).
```

**Expected result:** ρ_h ~ f(m_h, ξ, m_T) × m_T² M_Pl². The
function f is O(1) for m_h ~ m_T and exponentially suppressed
for m_h ≫ m_T.

**Kill criterion:** If ρ_h is too small to even heat the hidden
sector to its transition temperature, ALL thermal/transition
mechanisms die instantly.

**Estimated effort:** 1-2 days (standard Bogoliubov calculation,
similar to Branch H tensor calculation).

**Risk:** Medium. The result is expected to confirm ρ_h ~ m_h²M_Pl²
(standard gravitational production scaling). This is known from
the literature and unlikely to reveal surprises. But it would
provide a definitive normalization.

---

## Honest Assessment

Doing any Phase 2 calculation on Branch O is a poor use of time.
The structural barrier (Barrier 13: decoupling of bounce scale
from vacuum energy) prevents any mechanism from connecting the
bounce to ρ_DE. This barrier is not evaded by numerical precision.

The recommended action is to close Branch O and update the
barrier catalog.
