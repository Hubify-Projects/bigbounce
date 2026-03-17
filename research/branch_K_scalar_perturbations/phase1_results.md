# Branch K Phase 1 Results: Scalar Perturbations Through the Bounce

**Date:** 2026-03-16

---

## Verdict: BRANCH_K_GENERIC

---

## What Was Computed

The Bardeen potential equation for scalar perturbations of a
radiation fluid on the spin-torsion bounce background:

```
Φ̈ + 5HΦ̇ + [k²/(3a²) + 2Ḣ + 4H²]Φ = 0
```

was analyzed analytically and numerically for the exact background
a(t) = a_b(1+4α²t²)^{1/4}. The transfer function T(k), vacuum
spectrum, growing mode behavior, non-Gaussianity, and
observational implications were assessed.

---

## Key Results

### Result 1: Transfer function T(k) = 1 for all observable modes

**Analytic proof:** The Bardeen equation has exact time-reversal
symmetry on the spin-torsion bounce background. Under η → -η,
the growing mode of contraction maps to the decaying mode of
expansion. The constant mode maps to itself with unit amplitude.

**Numerical confirmation:** T(k) = 1.000 to machine precision
for k/k_b < 0.1. Features appear only at k ~ k_b (GHz scales).

**Consequence:** The bounce does not modify the scalar power
spectrum at any observable scale. P_S,out = P_S,in.

### Result 2: Growing mode problem resolved by time symmetry

The growing mode amplifies by (k_b/k)³ ~ 10⁸⁴ for CMB modes
during contraction. This DOES NOT contaminate the post-bounce
spectrum because the time-reversal symmetry of the bounce
maps the growing mode entirely to the decaying mode of the
expanding phase. No matching ambiguity, no spectral distortion.

### Result 3: No bounce-specific non-Gaussianity

The torsion (J⁵)² interaction generates f_NL ~ 10⁻⁵⁶ at CMB
scales (suppressed by (k/k_b)² localization). Generic mode
coupling gives f_NL ~ O(1) at most (same as any bounce). No
distinctive non-Gaussian signal.

### Result 4: r ~ 10⁻⁵⁵ (trivially consistent)

The tensor-to-scalar ratio r = P_T/P_S ~ 10⁻⁶⁴/10⁻⁹ = 10⁻⁵⁵
is 51 orders of magnitude below any conceivable detection
threshold. The bounce predicts effectively zero primordial
tensors at CMB scales.

### Result 5: Scalar spectrum is pre-bounce dependent

The observed spectrum (A_s, n_s, running) is entirely
determined by the pre-bounce contraction mechanism, which the
minimal model does not specify. A pure radiation contraction
gives P_S ∝ k⁴ (excluded). A viable spectrum requires a
matter-dominated or ekpyrotic pre-bounce phase (outside the
minimal model).

---

## Assessment Against Success Criteria

### Strong success criteria

| Criterion | Met? |
|-----------|------|
| T(k) has distinctive feature at observable scales | **NO** |
| Feature is spin-torsion specific | **NO** (at obs. scales) |
| Feature is testable | **NO** |

### Moderate success criteria

| Criterion | Met? |
|-----------|------|
| T(k) is calculable through the bounce | **YES** |
| Growing mode cleanly resolved | **YES** |
| Consistency check (bounce doesn't spoil spectrum) | **YES** |

### Failure criteria

| Criterion | Met? |
|-----------|------|
| T(k) ≈ 1 for all observable modes | **YES** (failure) |
| Features only at k ~ k_b (GHz) | **YES** (failure) |
| Generic to all symmetric radiation bounces | **YES** (failure) |

**Three of three failure criteria met. The scalar sector
provides no distinctive observable from the bounce.**

---

## Why GENERIC and Not CLOSED

The verdict is GENERIC rather than CLOSED because:

1. The CALCULATION is clean and well-defined (the Bardeen
   equation is regular through the bounce, no matching
   ambiguity). This is worth documenting.

2. The GROWING MODE RESOLUTION via time-reversal symmetry is
   a positive structural property of the model (even though it
   results in a null observational signal).

3. The CONSISTENCY with CMB data is non-trivial — some bounce
   models DO conflict with observed scalar spectra. The
   spin-torsion bounce does not.

However, none of these rise above "generic radiation bounce
physics." Every time-symmetric radiation bounce has the same
properties.

---

## What Is Spin-Torsion Specific

| Property | Specific to EC? | Observable? |
|----------|----------------|------------|
| ρ_crit = 0.21 M_Pl⁴ | YES | NO (sets k_b at GHz) |
| Exact bounce profile a(t) | YES | NO (affects only k ~ k_b) |
| (J⁵)² perturbation corrections | YES | NO (f_NL ~ 10⁻⁵⁶) |
| Time-reversal symmetry | NO (generic symmetric bounce) | — |
| T(k) = 1 for k ≪ k_b | NO (any symmetric bounce) | — |
| Growing mode resolution | NO (any symmetric bounce) | — |

**Everything observable is generic. Everything specific is
unobservable.**

---

## The Root Cause (Same as All Previous Branches)

The bounce operates at the Planck scale:

```
ρ_crit ~ M_Pl⁴,  k_b ~ M_Pl,  t_bounce ~ t_Pl
```

Observable cosmological perturbations are at vastly larger scales:

```
k_CMB ~ 10⁻²⁸ k_b,  λ_CMB ~ 10²⁸ λ_bounce
```

The 28-order-of-magnitude gap between the bounce scale and the
observable scale means the bounce is a sub-resolution event for
ALL cosmological probes. This is the same scale separation
barrier that closed Branches H, I, and J.

**The minimal spin-torsion bounce is too brief, too small, and
too energetic to leave any imprint on the observable universe.**

---

## Comparison Across All Branches

| Branch | Sector | Result | Root cause |
|--------|--------|--------|-----------|
| H (tensors) | P_T, n_T | ~10⁻⁶⁴, n_T ≈ 0 | (a_b/a_0)² dilution |
| H (parity) | Δχ | 0 exactly | Parity-even interaction |
| I (Horndeski) | Stability | Trivially compatible | ρ_DE/ρ_crit ~ 10⁻¹²² |
| J (state selection) | DE state | Liouville prevents | Phase-space conservation |
| **K (scalars)** | **T(k), P_S** | **T = 1, no feature** | **k_CMB/k_b ~ 10⁻²⁸** |

**The common thread: the Planck-scale bounce is invisible to
low-energy cosmological observations.**

---

## Is Phase 2 Justified?

### For scalar perturbations: NO

A Phase 2 (MCMC/data fitting) is not justified because:
- T(k) = 1 means the bounce adds no parameters to fit
- The scalar spectrum is entirely pre-bounce dependent
- There is no bounce-specific feature to constrain

### For the broader program: ASSESSMENT NEEDED

With Branches H, I, J, K all giving null/generic results, the
minimal spin-torsion bounce program has been comprehensively
explored. The question is whether the accumulated negative
results constitute a publishable characterization of the model.

---

## Summary

| Item | Result |
|------|--------|
| Transfer function T(k) | 1.000 for k ≪ k_b |
| Features at observable scales | **NONE** |
| Growing mode resolved? | YES (time-reversal symmetry) |
| Scalar tilt modification | 0 |
| r prediction | ~10⁻⁵⁵ (undetectable) |
| f_NL (torsion-specific) | ~10⁻⁵⁶ (negligible) |
| Scalar spectrum determined by? | Pre-bounce mechanism (not specified) |
| Spin-torsion specific at obs. scales? | **NO** |
| Distinctive feature found? | **NO** |
| Generic or specific? | **GENERIC** (any symmetric radiation bounce) |
| Phase 2 recommended? | **NO** |
| Branch K Phase 1 verdict | **BRANCH_K_GENERIC** |
| Recommended next move | Assess whether comprehensive null results are publishable |
