# Foundation G — Early Screening Memo

**Date:** 2026-03-15

---

## Purpose

Identify the top 2 and bottom 2 candidate classes before investing
in detailed analysis. Be blunt.

---

## Bottom 2: Likely to Collapse Immediately

### BOTTOM: Candidate C — Regularity Boundary Condition

**Why it collapses:**

The regularity condition at the bounce is: H = 0, all curvature
invariants finite. In spin-torsion cosmology, the modified Friedmann
equation at H = 0 gives:

```
0 = (8πG/3)(ρ_crit - ρ_crit²/ρ_crit) + Λ/3
0 = 0 + Λ/3
→ Λ = 0
```

This is just the Friedmann equation evaluated at the bounce. It says
"Λ = 0 at the moment when matter exactly compensates everything."
But this is not a CONSTRAINT on Λ — it is a TAUTOLOGY. The equation
H² = f(ρ, Λ) always has H = 0 when f(ρ, Λ) = 0, for ANY Λ. You
can reach H = 0 for any value of Λ by choosing the right ρ_bounce.

In the spin-torsion model specifically, ρ_bounce = ρ_crit is fixed
by the theory, so Λ is determined: Λ = 0. But this conflicts with
observation (Λ_obs > 0). So either:
- The model predicts Λ = 0 (wrong)
- Λ ≠ 0 means the bounce density adjusts: ρ_bounce ≠ ρ_crit (but
  then the bounce mechanism itself changes)

Either way: the regularity condition either gives the WRONG answer
(Λ = 0) or is NOT a constraint (Λ is absorbed by adjusting ρ_bounce).

**Verdict: FAIL_BOUNCE_IRRELEVANT + FAIL_NO_NARROWING.** The
condition is a tautology of the Friedmann equation, not a new
constraint on Λ.

### SECOND BOTTOM: Candidate D — Topological Sector Selection

**Why it collapses:**

1. **RR̃ = 0 on FRW.** The Pontryagin density vanishes identically
   on conformally flat backgrounds. The bounce (which is FRW) does
   not contribute to any gravitational topological charge.

2. **The Nieh-Yan density** is topological in EC gravity (Foundation B).
   Its integral is a topological invariant — it does not depend on
   dynamics and therefore the bounce does not affect it.

3. **In MAG**, the Nieh-Yan becomes non-topological, but Foundation B
   showed this breaks shift symmetry (topological-shift duality).
   The torsion-dependent correction is Q ∧ e ∧ T, which vanishes
   on FRW (Q₀ = T₀ = 0).

4. **Vacuum energy dependence on topological sector** is a QCD/gauge
   theory effect (θ-vacuum), not a gravitational effect. The bounce
   is a gravitational phenomenon that does not directly affect the
   QCD θ parameter.

**Verdict: FAIL_BOUNCE_IRRELEVANT.** Topological invariants are
either trivial on FRW (Pontryagin), or already analyzed and found
to be constrained by the topological-shift duality (Nieh-Yan),
or unrelated to the bounce (gauge θ-vacua).

---

## Top 2: Most Serious Candidates

### TOP: Candidate A — Bounce-Conditioned Sequestering

**Why it's the strongest:**

1. **The framework exists.** Kaloper-Padilla sequestering is a
   published, analyzed mechanism with a concrete action principle.

2. **The bounce provides something specific:** finite 4-volume per
   cycle. Generic cosmology does NOT provide this. Inflation gives
   V₄ → ∞. A singularity gives ill-defined V₄. A cyclic bounce
   gives finite, calculable V₄.

3. **Cycle matching conditions** are genuinely new mathematics. The
   requirement that global variables σ₁, σ₂ are consistent across
   the bounce boundary is a CONDITION that exists only because the
   bounce is nonsingular and regular.

4. **Test G1 (bounce relevance): LIKELY PASSES.** Remove the bounce
   → no cycle → V₄ → ∞ → sequestering constraint changes qualitatively.

**But: three serious risks remain.**

- The cycle matching condition for σ₁, σ₂ may be trivially
  satisfied (Test G2: hidden tuning).
- The residual Λ per cycle may still depend on μ₁, μ₂ as free
  parameters (Test G2 again).
- Requires cyclic cosmology, which is itself an unproven assumption.

**Assessment: worth one detailed test (Phase 2).** The bounce has
the clearest role here: providing the ONLY known nonsingular,
finite-V₄ cosmological boundary that allows sequestering to have
finite, well-defined global integrals.

### SECOND: Candidate E — Global Constraint + Bounce Matching

**Why it's second:**

1. **The matching condition idea is structurally novel.** Rather than
   asking the bounce to contribute to a volume integral (Foundation E,
   failed), the matching condition asks the bounce to CONSTRAIN a
   relationship between pre-bounce and post-bounce curvature.

2. **Time-reversal symmetry** at the bounce is a specific property
   that not all cosmologies share. If the bounce is time-symmetric,
   this imposes R(t_b + τ) = R(t_b - τ), which constrains the
   cosmological evolution.

3. **The constraint χ₀ could be DETERMINED** by the matching
   condition rather than freely specified.

**But: Foundation E already showed that ∫√g R is dominated by
late-time evolution.** A local matching condition at the bounce
constrains R AT the bounce, not the global integral. The connection
between local matching and global constraint is unclear.

**Assessment: worth screening at the structural level, but likely
collapses to Foundation E territory (local condition ≠ global
constraint).**

---

## The Single Key Question

> **Does the spin-torsion bounce provide a finite, calculable
> cycle 4-volume V₄ that transforms generic sequestering into
> a framework with a DETERMINISTIC residual Λ?**

If YES: the bounce plays an essential role that no other cosmological
scenario provides. Foundation G is genuinely new.

If NO (V₄ is finite but Λ_residual still depends on free parameters
μ₁, μ₂): the bounce is helpful but decorative. Foundation G collapses
to "sequestering is nice, the bounce makes V₄ finite, but Λ is still
tuned."

**This question determines everything.** It is the single test that
separates "bounce as essential selector" from "bounce as decorative
story."

---

## Recommended Phase 2 Focus

1. **Primary: Candidate A (bounce-conditioned sequestering).**
   Write the sequestering action on a cyclic bounce cosmology.
   Compute V₄ per cycle. Determine whether Λ_residual is fixed
   by V₄ + μ₁,₂, and whether the bounce matching conditions
   constrain μ₁, μ₂.

2. **Secondary: Candidate E (global constraint + matching).**
   Only if Candidate A shows promise. Check whether bounce
   time-reversal symmetry constrains χ₀.

3. **Skip: Candidates B, C, D.** C is a tautology. D has no FRW
   content. B requires a landscape (too speculative for this
   program's standards).
