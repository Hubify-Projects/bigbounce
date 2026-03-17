# Foundation E — Distinctive Predictions

**Date:** 2026-03-14

---

## Question

Does the combined sequestering + bounce model produce any distinctive
consequences that neither mechanism produces alone?

---

## Prediction Search

### 1. Modified cosmological evolution near the bounce?

The sequestering constraint modifies the Einstein equations by
projecting out the constant vacuum component of T_μν. Near the
bounce, T_μν is dominated by the spin-torsion repulsion term,
not by vacuum energy.

The sequestering modification is:
```
G_μν = 8πG(T_μν - ⟨T⟩g_μν/4) + Λ_residual g_μν
```

At the bounce: T_μν is dominated by matter at ρ ~ M_Pl⁴. The
vacuum subtraction ⟨T⟩/4 is dominated by late-time averages
(which are ~ρ_Λ ~ 10⁻⁴⁷ GeV⁴). So:

```
Correction at bounce: ⟨T⟩/T_bounce ~ 10⁻⁴⁷/10⁷⁶ ~ 10⁻¹²³
```

**The sequestering correction is negligible at the bounce.**

The bounce dynamics are completely unaffected by sequestering.

**Verdict: NO distinctive prediction from modified bounce dynamics.**

---

### 2. Constraints on vacuum energy evolution?

Sequestering absorbs constant vacuum shifts but NOT time-dependent
changes. If the vacuum energy evolves during a phase transition
(e.g., QCD, EW), the sequestering only absorbs the before/after
constant difference, not the dynamics of the transition.

In a bounce cosmology, the most dramatic "transition" is the bounce
itself. But the bounce is a gravitational transition (driven by
spin-torsion repulsion), not a vacuum transition. The vacuum energy
before and after the bounce is the same.

**Verdict: NO distinctive prediction from vacuum evolution constraints.**

---

### 3. Relations between bounce parameters and late-time Λ?

For Λ_residual = μ₁⁴/V₄:

The bounce enters V₄ only through the bounce-era contribution to
the spacetime volume, which is negligible (Check 1 of bounce
compatibility).

The bounce energy scale M_Pl enters the torsion action but does
not appear in the sequestering scales μ₁, μ₂.

There is no structural connection between the bounce parameters
(spin density, torsion coupling constants) and the sequestering
parameters (μ₁, μ₂).

**Verdict: NO bounce-Λ relation exists in the minimal framework.**

---

### 4. Finite-future requirement as prediction?

Sequestering requires V₄ < ∞. A bounce cosmology with only a PAST
bounce (no future recollapse) has V₄ → ∞.

The combination of sequestering + bounce cosmology PREDICTS:
```
If sequestering is the CC mechanism, the universe must
eventually recollapse or undergo a future bounce.
```

This IS a prediction, but it is:
- From sequestering alone (not bounce-specific)
- Not testable in the near term
- A very general statement about the far future

**Verdict: WEAK prediction (recollapse requirement). Not bounce-specific.**

---

### 5. Cyclic cosmology link?

If the bounce is part of a CYCLIC cosmology (the universe bounces
repeatedly), then V₄ might be naturally finite per cycle. The
sequestering constraint would apply to each cycle:

```
Λ_residual^(n) = μ₁⁴ / V₄^(n)
```

where V₄^(n) is the 4-volume of the n-th cycle. If cycles have
similar duration and expansion:

```
Λ_residual ~ μ₁⁴ / (a_max³ × T_cycle × V_spatial)
```

This connects Λ to the maximum expansion factor a_max and the
cycle period T_cycle. If these are determined by the bounce
dynamics, there IS a bounce-Λ connection.

But: this requires:
- Cyclic cosmology (not just a single bounce)
- a_max and T_cycle determined by microphysics (not initial conditions)
- Periodicity (or at least regularity) of cycles

None of these are established.

**Verdict: CONDITIONAL prediction. Interesting if cyclic cosmology
is viable, but speculative.**

---

### 6. Torsion contribution to ⟨L_matter⟩?

The σ₂ constraint fixes ⟨L_matter⟩ = μ₂⁴. In EC gravity, L_matter
includes the spin-torsion contact interaction:

```
L_spin = -κ²(s^μ s_μ) ~ -κ² ρ_spin²/m_f²
```

This is negative (attractive four-fermion interaction). Its
spacetime average is:

```
⟨L_spin⟩ ~ -κ² × ⟨ρ_spin²/m_f²⟩
```

At early times (near bounce): ⟨ρ_spin²⟩ is large.
At late times: ⟨ρ_spin²⟩ ~ 0 (diluted by expansion).

The spin contribution to ⟨L_matter⟩ is dominated by the bounce era:
```
⟨L_spin⟩ ~ -κ² M_Pl⁴ × V₄^bounce / V₄ ~ negligible
```

(Same negligibility as before: bounce 4-volume is tiny.)

**Verdict: NO. Spin-torsion contribution to ⟨L_matter⟩ is negligible.**

---

## Summary of Prediction Search

| Possible prediction | Exists? | Bounce-specific? | Testable? |
|--------------------|---------|-------------------|-----------|
| Modified bounce dynamics | No | — | — |
| Vacuum evolution constraint | No | — | — |
| Bounce parameter → Λ relation | No | — | — |
| Future recollapse required | Weak | No (from sequestering) | No (far future) |
| Cyclic Λ determination | Conditional | Yes (if cyclic) | No (requires cyclic model) |
| Torsion → ⟨L_matter⟩ link | No | — | — |

**No distinctive prediction emerges from the sequestering + bounce
combination in the minimal framework.**

---

## Why This Happens

The fundamental reason is a **scale separation problem:**

- The bounce operates at ρ ~ M_Pl⁴ for Δt ~ t_Pl
- Sequestering operates over the FULL spacetime history
- The bounce-era contribution to ANY spacetime average is
  suppressed by V₄^bounce / V₄^total ~ 10⁻⁶⁰ (or smaller)

The bounce is too brief and too early to dominate any global
quantity. Its effects are diluted by the vast late-time expansion.

This is structurally similar to Foundation C (scalar-tensor
universality): the late-time cosmology dominates, and the
early-time geometric content is washed out.

---

## What Would Change This

1. **Cyclic cosmology:** If the universe bounces many times, the
   bounce contribution accumulates. After N cycles:
   ⟨L_spin⟩_accumulated ~ N × ⟨L_spin⟩_per_cycle. For N large
   enough, this could matter.

2. **Non-perturbative bounce effects:** If the bounce triggers a
   phase transition that PERMANENTLY changes the vacuum (not just
   transiently), the sequestering constraint would absorb the
   before/after shift but the transition itself would be bounce-
   specific.

3. **Modified sequestering action:** If the sequestering constraint
   involves a curvature-weighted integral (e.g., ∫√g R × L_matter)
   rather than a volume-weighted integral (∫√g L_matter), the
   bounce contribution would be enhanced by the large R at the
   bounce.

Option 3 is the most interesting: it suggests that a CURVATURE-
WEIGHTED sequestering variant might produce a bounce-Λ connection.
This would be a modification of the Kaloper-Padilla mechanism
specifically motivated by bounce cosmology.

**This is a potential Phase 2 direction if the minimal mechanism
is deemed worth pursuing despite its lack of bounce-specific
predictions.**
