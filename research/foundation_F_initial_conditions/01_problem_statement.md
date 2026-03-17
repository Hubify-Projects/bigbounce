# Foundation F — Problem Statement

**Date:** 2026-03-15

---

## Why Foundations A–E Failed

| Foundation | Mechanism | Barrier |
|-----------|-----------|---------|
| A | Local propagating torsion → DE | Mass-coupling lock: m and g both set by G |
| B | Geometric pseudoscalar (Nieh-Yan) | Topological-shift duality: mass protection ↔ geometric content |
| C | Curvature-dependent mass | Scalar-tensor universality: reduces to generic EFT on FRW |
| D | Disformal effective metrics | Planck suppression: one ∂φ per vertex, distinctive effects ~ 10⁻¹²² |
| E | Global vacuum mechanisms | Scale separation: bounce contributes ~ 10⁻³² to ∫√g R |

Two classes of mechanism have been exhausted:

1. **Local field mechanisms (A–D):** Any propagating geometric field
   that could drive DE is either locked (A), unprotected (B), generic
   (C), or suppressed (D).

2. **Global spacetime-integral mechanisms (E):** Any volume-weighted
   global quantity (∫√g, ∫√g R, ⟨L_matter⟩) is dominated by late-time
   evolution. The bounce contributes negligibly.

---

## Why Initial Conditions Are Not Volume-Suppressed

The barriers in A–E share a common structure: they involve CONTINUOUS
quantities that are either time-averaged, volume-weighted, or
coupling-suppressed. These operations dilute early-time (bounce)
contributions relative to late-time cosmological evolution.

Initial conditions are structurally different:

- They are set ONCE, at a single moment (the bounce)
- They are NOT averaged over spacetime volume
- They propagate forward deterministically through the field equations
- Their influence on late-time physics depends on the DYNAMICS of
  the field, not on the weight of the bounce era in an integral

A scalar field φ with value φ_i at the bounce evolves according to:

```
φ̈ + 3Hφ̇ + V'(φ) = 0
```

The solution φ(t_today) depends on φ_i through the full dynamical
evolution — not through a volume average. If the potential has
attractor behavior, many different φ_i converge to the same late-time
state. If the potential has sensitive dependence, φ_i matters
enormously.

**The question is whether attractors or sensitive dependence governs
the evolution from bounce to today.**

---

## How Bounce Physics Could Set Initial Conditions

At the bounce:
- ρ ~ ρ_crit ~ M_Pl⁴
- H = 0 (by definition of the bounce)
- Ḣ > 0 (transition from contraction to expansion)
- R ~ M_Pl² (curvature is Planck-scale)
- Spin density s ~ M_Pl³ (if matter is fermionic)
- Torsion T ~ M_Pl (from T = -κ²s)

A scalar field φ coupled to any of these quantities could receive:

1. **Curvature-induced displacement:** If φ couples non-minimally
   (ξRφ² or similar), the Planck-scale curvature at the bounce
   generates a force F ~ ξM_Pl² φ that displaces φ from its vacuum.

2. **Torsion-induced displacement:** If φ couples to torsion
   invariants (T²φ², or the Nieh-Yan density), the large torsion
   at the bounce displaces φ.

3. **Kinetic energy from the bounce:** The rapid expansion just
   after the bounce (Ḣ ~ M_Pl²) generates a large Hubble friction
   that can freeze φ at a displaced value.

4. **Symmetry breaking at Planck scale:** A symmetry protecting φ
   (shift symmetry, discrete symmetry) could be broken at the Planck
   scale, giving φ a vacuum expectation value set by M_Pl.

---

## The Target

Test whether a scalar field, starting with bounce-determined initial
conditions, evolves to produce the observed dark energy at late times.

The target is NOT to derive φ from geometry (Foundations A–D closed
this). The target is to determine whether the bounce CONSTRAINS the
initial state of an otherwise-generic scalar field enough to make
the DE prediction SPECIFIC rather than freely tunable.

---

## Success Criteria

A viable Foundation F candidate must satisfy ALL of:

1. **Bounce-determined initial conditions:** The value φ_i and/or
   φ̇_i at the bounce is determined by bounce-era physics (curvature,
   torsion, spin density), not freely chosen.

2. **Late-time dark energy:** The field evolves to produce w ≈ -1
   and ρ_DE ~ 10⁻¹²² M_Pl⁴ at the present epoch.

3. **No extreme fine-tuning of the initial state:** The range of
   φ_i values that produce viable DE should not require precision
   better than O(10⁻¹⁰) relative to the bounce-determined scale.
   (Some tuning is acceptable; 10⁻¹²² is not.)

4. **At least one predictive relation:** Bounce parameters
   (ρ_crit, torsion coupling, spin density) should determine at
   least one DE parameter (ρ_DE, w, or the DE onset epoch) with
   limited freedom.

---

## Failure Criteria

| Failure | Meaning |
|---------|---------|
| FAIL_GENERIC_INITIAL | Bounce sets φ_i ~ M_Pl but any φ_i ~ M_Pl gives viable DE |
| FAIL_FINE_TUNED_INITIAL | Viable DE requires φ_i tuned to precision unavailable from bounce |
| FAIL_ATTRACTOR_WASHOUT | Attractor dynamics erase all memory of φ_i before today |
| FAIL_NO_LATE_DE | Field does not produce dark energy regardless of initial conditions |
| FAIL_NO_PREDICTIVE_LINK | Bounce parameters do not constrain DE parameters meaningfully |
