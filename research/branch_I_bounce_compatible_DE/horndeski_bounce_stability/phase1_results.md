# Branch I Phase 1 Results: Horndeski Stability at the Bounce

**Date:** 2026-03-16

---

## Verdict: BRANCH_I_WEAK

---

## What Was Tested

Whether the spin-torsion bounce (H = 0, Ḣ ≈ 3.52 M_Pl²)
constrains which Horndeski/scalar-tensor dark energy models
are viable, by checking ghost freedom, gradient stability,
sound speed regularity, and EFT validity for six model classes.

---

## Results by Class

| Class | Verdict | Key finding |
|-------|---------|-------------|
| A: Quintessence | TRIVIALLY_COMPATIBLE | Stability = constants (1,1,M²,1) |
| B: K-essence | TRIVIALLY_COMPATIBLE | X → 0 → canonical limit |
| C: Braiding | EFT_INAPPLICABLE | Q_S → 0 at bounce; M ~ H₀ ≪ M_Pl |
| D: Non-minimal | COMPATIBLE_WITH_CAVEAT | Tachyonic kick exp(√(21ξ)), bounded |
| E: Quartic/Quintic | TRIVIALLY_COMPATIBLE | Pre-empted by GW170817 |
| F: DHOST | EFT_INAPPLICABLE | Degeneracy algebraic; Λ_SC ≪ M_Pl |

---

## Assessment Against Success Criteria

### Strong success criteria

| Criterion | Met? | Detail |
|-----------|------|--------|
| Nontrivial exclusion of a DE class | **NO** | No class is excluded by the bounce |
| Narrowed viable parameter region | **NO** | ξ bound is weaker than existing |
| Sharp stability criterion | **MARGINAL** | Q_S → 0 for braiding is sharp but requires Phase 2 |

### Moderate success criteria

| Criterion | Met? | Detail |
|-----------|------|--------|
| Methodological constraint | **YES** | EFT α-parameterization breaks at H = 0 |
| Model class that COULD fail | **YES** | Braiding Q_S → 0 (unresolved) |

### Failure criteria

| Criterion | Met? | Detail |
|-----------|------|--------|
| All models trivially compatible | **MOSTLY** | 4/6 classes trivially compatible |
| Analysis reduces to generic statements | **PARTIALLY** | Scale separation dominates |

---

## The Five Findings

### Finding 1 — METHODOLOGICAL (moderate interest)

**The EFT-of-DE α-parameterization is singular at H = 0.**

The Bellini-Sawicki parameters α_K ∝ 1/H², α_B ∝ 1/H diverge
at the bounce. Physical stability quantities remain finite.
This means standard Boltzmann codes (hi_class, EFTCAMB) cannot
be applied to bouncing cosmologies without reformulation in
terms of Lagrangian-level quantities.

*Publishability: moderate. This is a useful warning for the
bouncing cosmology community but is not a deep physics result.*

### Finding 2 — STRUCTURAL (expected)

**Scale separation (ρ_DE/ρ_crit ~ 10⁻¹²²) makes DE a negligible
spectator at the bounce.**

DE fields are frozen (X → 0, φ̇ ~ 10⁻⁶⁰ M_Pl²) during the
bounce. All stability conditions that depend on X or φ̇ reduce
to their X = 0 limits, which are typically trivial (canonical).

*Publishability: this is the EXPECTED null result. Important to
state but not surprising.*

### Finding 3 — EFT BREAKDOWN (important caveat)

**DE theories with low internal scales (M ~ H₀ for braiding,
Λ ~ 10⁻⁴⁰ M_Pl for DHOST) cannot be assessed at Planck
curvature. Their EFT descriptions are invalid.**

This is neither compatibility nor incompatibility — it is
UNDETERMINED. Assessing bounce compatibility for these theories
requires their UV completions, which are unknown.

*Publishability: moderate. It constrains the claims one can
make about bounce-compatible DE.*

### Finding 4 — TRANSIENT EFFECT (marginal)

**Non-minimally coupled scalars (ξRφ²) receive a tachyonic
kick at the bounce with growth factor exp(√(21ξ)).**

For |ξ| ≲ O(1), this is negligible. For |ξ| ~ 10, the kick
is significant but bounded. The bounce constraint ξ ≲ O(10)
is WEAKER than existing solar system and CMB bounds on ξ.

*Publishability: low. The bounce provides no new constraint
beyond what is already known.*

### Finding 5 — STRONG COUPLING (most promising)

**The scalar perturbation normalization Q_S → 0 for cubic
Horndeski braiding when H → 0 and X → 0 simultaneously.**

This could signal that scalar perturbations become strongly
coupled at the bounce, invalidating the perturbative treatment.
Whether this is a genuine physical problem or a gauge artifact
requires a dedicated perturbation analysis.

If genuine, this would mean: braiding DE models with M ~ H₀
are not only outside their EFT validity at the bounce, but
specifically have a perturbation theory breakdown tied to the
H = 0 crossing. This would be a NONTRIVIAL result.

*Publishability: conditional on Phase 2 analysis confirming
the strong coupling is physical.*

---

## Why BRANCH_I_WEAK (Not CLOSED or PROMISING)

### Why not CLOSED

Finding 5 (Q_S → 0 for braiding) is genuinely unresolved. If
the strong coupling is physical, it would be a nontrivial bounce
constraint on braiding DE models. This deserves Phase 2 work.

The methodological finding (α-parameterization breakdown) is
real and useful, even though it is not a stability exclusion.

### Why not PROMISING

- 4/6 model classes are trivially compatible (no bounce content)
- The non-minimal coupling constraint is weaker than existing bounds
- The EFT breakdown for braiding/DHOST may be generic (any theory
  with Λ ≪ M_Pl fails at Planck curvature, bounce or not)
- The Q_S → 0 finding may turn out to be a gauge artifact

The probability of a nontrivial, publishable-grade result from
Phase 2 is estimated at 20-30%.

---

## What Phase 2 Would Require

If pursued, Phase 2 for Branch I would involve:

1. **Braiding perturbation analysis** (highest priority)
   - Solve scalar perturbation equation through H = 0 crossing
   - Determine whether Q_S → 0 creates physical strong coupling
   - Compute effective strong coupling scale at the bounce
   - Assess whether perturbations remain bounded despite Q_S → 0

2. **Braiding contraction dynamics** (medium priority)
   - Solve full braiding EOM through contraction to bounce
   - Determine actual φ̇ at bounce after anti-friction amplification
   - Check whether amplified φ̇ changes the Q_S → 0 conclusion

3. **Non-minimal coupling trajectory** (low priority)
   - Solve field evolution through bounce with tachyonic kick
   - Determine whether field rejoins late-time DE trajectory
   - Only interesting for large ξ ≳ 10

Estimated effort: 2-3 sessions for item 1, 1-2 for item 2.

---

## Comparison with Branch H

| Aspect | Branch H (tensors) | Branch I (Horndeski) |
|--------|-------------------|---------------------|
| Primary result | P_T ~ 10⁻⁶⁴ (weak) | Trivially compatible (weak) |
| Root cause | Scale separation | Scale separation |
| Distinctive content | None (generic bounce) | Methodological (α-param) |
| Phase 2 potential | LOW (scalar likely same) | LOW-MODERATE (Q_S → 0) |
| Clean closure? | YES | MOSTLY (1 unresolved) |

Both branches are dominated by the same structural fact: the
bounce is a Planck-scale event and DE is 10¹²² orders of magnitude
below the bounce scale. This hierarchy prevents interesting
bounce-DE interplay for most model classes.

---

## Honest Assessment

The Branch I Phase 1 analysis is MOSTLY a confirmation of the
expected null result. The bounce is too brief and too energetic
for DE-scale physics to matter, and DE-scale physics is too feeble
to affect the bounce.

The two non-trivial findings (α-parameterization breakdown and
Q_S → 0 for braiding) are REAL but MODEST. Neither constitutes
a major physics result. Together, they could form a useful section
in a broader paper on bouncing cosmology constraints, but neither
would support a standalone publication.

The most honest characterization: **the bounce and dark energy
are ships passing in the night, separated by 122 orders of
magnitude. Asking whether they constrain each other is like
asking whether your choice of shoes affects satellite orbits.
The answer is technically yes (gravitational backreaction), but
the effect is unmeasurably small.**

---

## Summary Table

| Item | Result |
|------|--------|
| Classes tested | 6 (A–F within Horndeski + DHOST) |
| Trivially compatible | 4 (A, B, D, E) |
| EFT inapplicable | 2 (C, F) |
| Incompatible | 0 |
| Strongest candidate for constraint | C (braiding): Q_S → 0 at H = 0 |
| Weakest candidate | A (quintessence): stability = constants |
| Nontrivial DE constraint? | **NO** (at Phase 1 level) |
| Methodological finding? | **YES** (α-param breakdown) |
| Phase 1 verdict | **BRANCH_I_WEAK** |
| Phase 2 recommended? | CONDITIONAL (only if Q_S → 0 confirmed physical) |
