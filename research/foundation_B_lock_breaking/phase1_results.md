# Foundation B — Phase 1 Results

**Date:** 2026-03-14

---

## Outcome: PARTIAL_BREAK_FOUND

---

## Summary

We surveyed five candidate mechanisms for breaking the mass-coupling
lock identified in Foundation A (PGT propagating torsion). Using a
general lock analysis framework and symbolic computation, we tested
each candidate's Lagrangian for independent mass and coupling scaling.

**The mass-coupling lock is NOT an inescapable feature of geometric
dark-energy theories.** It is a property of theories where a single
parameter controls both the kinetic normalization and the mass of
the propagating mode. Breaking the lock requires introducing an
independent mass-generating mechanism — which is exactly how it
works in the Standard Model (Higgs mechanism) and in QCD (axion).

---

## Results by Model

| Model | Lock status | Mass natural? | Phase 2? |
|-------|-------------|---------------|----------|
| PGT 0⁻ (baseline) | **LOCKED** | N/A | No (closed) |
| A: PGT + Higgs portal | **PARTIALLY_UNLOCKED** | No — new hierarchy | Backup |
| B: Geometric ALP (MAG) | **FULLY_UNLOCKED** * | Yes (shift symmetry) | **PRIMARY** |
| C: Two-field PGT | **FORMALLY_UNLOCKED** | Unknown | Conditional |
| D: Vacuum sequestering | **ORTHOGONAL** | N/A | Separate line |
| E: MAG distortion field | **UNKNOWN** | Unknown | Long-term |

\* Conditional on the Nieh-Yan form being non-topological in MAG.

---

## The Central Finding

The ALP architecture — a pseudoscalar with shift-symmetry-protected
mass, broken by a non-perturbative scale Λ, and coupled to matter
through an independent geometric coupling α — is the unique structure
among those tested that achieves full lock-breaking with technical
naturalness.

```
m = Λ² / f      (mass from symmetry breaking — can be tiny)
g = α / f        (coupling from geometric sector — independent of Λ)

R = m/g = Λ²/α   (depends on Λ and α, NOT on f alone)

At Λ → 0: m → 0 while g remains finite. Shift symmetry restored.
```

The question is whether any geometric theory (metric-affine gravity,
extended PGT, or other) naturally produces this structure WITHOUT
collapsing to a generic (non-geometric) ALP — i.e., without Route T1
repeating.

---

## What Distinguishes This From Route T1

Route T1 failed because the dynamical Immirzi field θ coupled to the
Nieh-Yan density N₄, and N₄ is topological (exact) in standard PGT.
After torsion elimination, the θ-N₄ coupling reduced to a total
derivative plus standard ALP terms with no geometric fingerprint.

The key hypothesis for Model B is: **in metric-affine gravity (where
non-metricity Q ≠ 0), the Nieh-Yan form is NOT exact.** If true:

1. The θ-N₄ coupling retains local dynamical content (survives DR1).
2. The shift symmetry θ → θ + c protects the mass (passes DR2).
3. The non-topological geometric coupling provides a non-generic
   prediction distinguishing it from a standard ALP (passes DR3).
4. The mass and coupling are independent (passes DR5 — lock broken).

If the Nieh-Yan form IS still effectively topological in MAG on shell,
then Model B collapses to T1 and the break fails.

---

## Phase 2 First-Check

**Compute dN₄ in metric-affine gravity.**

The Nieh-Yan 4-form is N₄ = d(e^I ∧ T_I). In metric-compatible
theories (torsion but no non-metricity), dN₄ = 0 in 4D (exact form).

In MAG, the torsion T^I = De^I involves a connection with non-metricity.
The question is: does the non-metricity modify the closure of N₄?

Specifically:
- Compute T^I_MAG = De^I where D includes non-metricity
- Compute N₄ = e^I ∧ T_I
- Compute dN₄
- Determine: is dN₄ = 0 identically, or does it depend on Q?

If dN₄ involves Q (non-metricity), then N₄ is non-topological in MAG,
and Model B is viable.

If dN₄ = 0 identically even with Q ≠ 0, Model B fails.

This is a definite mathematical question with a checkable answer.

---

## New Ideas Generated

Three new ideas emerged from the analysis that should be tracked:

1. **Composite geometric pseudoscalar:** A pseudo-Goldstone boson from
   torsion condensation in PGT. Mass from condensation scale, coupling
   from torsion-matter vertex. Could produce the ALP structure from
   strong-coupling dynamics rather than from a fundamental field.

2. **Dimensional transmutation:** If PGT torsion couplings run under
   RG flow, an exponentially small scale Λ_tor (like Λ_QCD) could
   be generated, providing a natural origin for the tiny mass without
   fine-tuning.

3. **Environmental mass (chameleon/symmetron for torsion):** If the
   torsion mass depends on the local curvature R, it could be
   cosmologically light (R ~ H₀²) while heavy in the solar system
   (R ~ R_sun), naturally evading fifth-force constraints.

---

## Verdict

The mass-coupling lock is a real structural obstruction but NOT an
absolute barrier. The ALP architecture provides a proven template
for breaking it. The open question — and the subject of Phase 2 —
is whether this architecture can be realized geometrically through
the metric-affine Nieh-Yan coupling, or whether it inevitably
collapses to a non-geometric ALP (Route T1 failure mode).

**Next action:** Compute dN₄ in metric-affine gravity.
