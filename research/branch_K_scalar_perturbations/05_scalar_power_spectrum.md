# Scalar Power Spectrum Through the Bounce

**Date:** 2026-03-16

---

## The Transfer Function Result

### Analytic prediction (from time-reversal symmetry)

For super-Hubble modes (k ≪ k_b):

```
T(k) = 1    (exact, for adiabatic perturbations)
```

The bounce is perfectly transparent. The constant mode of the
Bardeen potential passes through unchanged.

### Numerical confirmation

The Bardeen equation Φ̈ + 5HΦ̇ + [k²/(3a²) + 2Ḣ + 4H²]Φ = 0
was solved for k/k_b ranging from 10⁻³ to 5:

| k/k_b | |T(k)|² |
|--------|---------|
| 0.001 | 1.000000 |
| 0.003 | 1.000000 |
| 0.01 | 1.000000 |
| 0.03 | 1.00000 |
| 0.1 | 1.0000 |
| 0.3 | ~1.00 |
| 0.5 | oscillatory |
| 1.0 | oscillatory |
| 2.0 | oscillatory |

For k/k_b < 0.1: |T|² = 1 to numerical precision.
For k/k_b ~ 0.3–5: oscillatory features (analogous to
quantum scattering off a potential barrier).

### Observable regime

All CMB and LSS scales have k/k_b ~ 10⁻²⁸:

```
k_CMB ~ 0.01 Mpc⁻¹
k_b ~ 10²⁵ Mpc⁻¹ (today)
k_CMB/k_b ~ 10⁻²⁸
```

This is deep in the T(k) = 1 regime. The bounce has
ZERO effect on the observable scalar spectrum.

---

## The Output Scalar Spectrum

### General relation

```
P_S,out(k) = |T(k)|² × P_S,in(k) = P_S,in(k)
```

for all k ≪ k_b (all observable modes).

### The input spectrum is NOT predicted

The spin-torsion bounce does not specify the contracting phase.
The input spectrum depends on the pre-bounce mechanism:

| Pre-bounce mechanism | P_S,in(k) | n_s | Compatible with CMB? |
|---------------------|-----------|-----|---------------------|
| Radiation contraction (vacuum) | ∝ k⁴ | 5 | NO (excluded) |
| Matter contraction | ∝ k⁰ | 1 | YES (needs tilt source) |
| Ekpyrotic contraction | ∝ k^{n_ek} | model-dep. | Possibly |
| Slow contraction | ∝ k^{n_sc} | model-dep. | Possibly |

**The minimal spin-torsion bounce is AGNOSTIC about the scalar
spectrum.** It neither produces nor modifies the observed
n_s ≈ 0.965.

### What the bounce tells us

The bounce tells us NOTHING about:
- The scalar amplitude A_s ≈ 2.1 × 10⁻⁹
- The scalar tilt n_s ≈ 0.965
- The running dn_s/d ln k ≈ -0.005

These are determined by the pre-bounce mechanism.

---

## Spectral Features

### At observable scales (k ≪ k_b): NONE

T(k) = 1 means no features. The spectrum is whatever came in.

### At the bounce scale (k ~ k_b): oscillatory

The transfer function has oscillatory features at k ~ k_b
(same mathematical structure as the tensor Bogoliubov
coefficients). These oscillations are:

- Located at f ~ 1–30 GHz (today)
- Amplitude: O(1) deviations from T = 1
- Period: Δk ~ k_b
- Completely unobservable with current or planned experiments

### Comparison with tensor features

The scalar and tensor effective potentials are both localized
bumps at the bounce with height ~ k_b² and width ~ 1/k_b.
The scalar features are qualitatively similar to the tensor
features (Branch H).

| Property | Tensor | Scalar |
|----------|--------|--------|
| Feature scale | k ~ k_b | k ~ k_b |
| Feature frequency (today) | ~8 GHz | ~8 GHz |
| Feature amplitude | O(1) | O(1) |
| Observable? | NO | NO |

---

## The Scalar-to-Tensor Ratio

### Definition at CMB scales

```
r = P_T(k_*) / P_S(k_*)    at k_* = 0.05 Mpc⁻¹
```

### Bounce prediction

From Branch H: P_T(k_*) ≈ 2 × 10⁻⁶⁴ (bounce-generated
from vacuum).

The scalar spectrum at k_* is observed: P_S(k_*) ≈ 2.1 × 10⁻⁹.

```
r = 2 × 10⁻⁶⁴ / 2.1 × 10⁻⁹ ≈ 10⁻⁵⁵
```

### Observational status

Current bound: r < 0.03 (Planck + BICEP/Keck 2021).
Future sensitivity: r ~ 10⁻³ (CMB-S4, LiteBIRD).

The bounce prediction r ~ 10⁻⁵⁵ is:
- 10⁵³ below current bounds
- 10⁵² below future sensitivity
- Completely undetectable

### Is this a useful prediction?

NO. The prediction r ~ 10⁻⁵⁵ is consistent with observations
but provides no useful constraint. It is equivalent to saying
"the bounce produces no observable tensors at CMB scales."

---

## The Growing Mode Resolution

### The problem (for other bounce models)

In generic bouncing cosmologies, the growing mode of the
Bardeen potential (∝ 1/(kη)³ in radiation) can amplify by
enormous factors during contraction. If the bounce matching
is imperfect, this growing mode leaks into the post-bounce
constant mode, contaminating the spectrum.

For CMB modes: the growth factor is (k_b/k)³ ~ 10⁸⁴.
Even a tiny leakage of 10⁻⁸⁴ would be O(1) in the
post-bounce spectrum.

### The resolution (for the spin-torsion bounce)

The spin-torsion bounce has EXACT time-reversal symmetry
(radiation on both sides, a(t) = a(-t)). This symmetry
guarantees:

```
Growing mode (contraction) → Decaying mode (expansion)
Constant mode → Constant mode
```

with NO leakage. The transfer matrix is the identity.

### Significance

This is a CONSISTENCY result: the spin-torsion bounce does not
spoil whatever scalar spectrum the pre-bounce mechanism creates.
The growing mode is handled cleanly without matching ambiguity.

This is in contrast to some other bounce models (e.g.,
ekpyrotic bounces) where the growing mode problem requires
careful treatment and can spoil the spectrum.

### Is this specific to spin-torsion?

NO. The resolution is specific to TIME-SYMMETRIC bounces, not
to spin-torsion physics. Any bounce with the same equation of
state on both sides (contraction = time-reverse of expansion)
has the same property.

The spin-torsion bounce happens to be time-symmetric because
it is radiation-dominated on both sides (the torsion correction
ρ² is symmetric). But a generic radiation bounce in LQC or
other frameworks also has this symmetry.

---

## What IS Specific to Spin-Torsion

The following quantities are model-specific:

1. **ρ_crit = 0.21 M_Pl⁴** — determines k_b and the
   oscillatory feature scale. LQC has ρ_crit ≈ 0.41 ρ_Pl.
   The feature scale differs by O(1).

2. **The exact bounce profile** a(t) = a_b(1+4α²t²)^{1/4}
   — determines the precise shape of the oscillatory features
   at k ~ k_b. Different from LQC's a(t).

3. **The effective scalar potential shape** — the specific
   form of 2Ḣ + 4H² at the bounce. Different from other
   bounce models.

ALL of these differences are confined to k ~ k_b (GHz scales).
At observable scales, all time-symmetric radiation bounces are
IDENTICAL.

---

## Summary

| Quantity | Value | Observable? |
|----------|-------|------------|
| T(k) for k ≪ k_b | 1.000 (exact) | N/A (no signal) |
| Feature scale | k ~ k_b ~ 8 GHz | NO |
| n_s modification | 0 | N/A |
| A_s modification | 0 | N/A |
| r | ~10⁻⁵⁵ | NO (10⁵² below reach) |
| Growing mode leakage | 0 (exact) | N/A |
| Spin-torsion-specific at observable k? | NO | — |

**The scalar power spectrum through the spin-torsion bounce is
UNCHANGED at all observable scales. No features, no tilt
modification, no amplitude change. The growing mode is cleanly
resolved by time-reversal symmetry. The bounce is transparent.**
