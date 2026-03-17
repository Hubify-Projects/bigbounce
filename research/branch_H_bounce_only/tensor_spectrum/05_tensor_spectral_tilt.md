# Tensor Spectral Tilt

**Date:** 2026-03-15

---

## Definition

```
n_T(k) = d ln P_T / d ln k
```

---

## Numerical Result

The numerical solver (notebook 03) gives:

```
┌──────────────────────────────────────────┐
│                                          │
│   n_T ≈ 0    for k ≪ k_b                │
│                                          │
│   (measured: n_T = -0.002 ± 0.01)        │
│                                          │
└──────────────────────────────────────────┘
```

The spectrum is FLAT (scale-invariant) at low frequencies.
NOT blue-tilted as initially expected from naive arguments.

---

## Derivation

The tensor power spectrum:

```
P_T(k) ∝ k² × (1 + 2|β_k|²)
```

Taking the logarithmic derivative:

```
n_T = 2 + d ln(1 + 2|β_k|²) / d ln k
```

### The critical cancellation

Numerically: |β_k|² = C (k_b/k)² for k ≪ k_b, with C ≈ 0.855.

For |β_k|² ≫ 1 (i.e., k ≪ k_b):

```
1 + 2|β_k|² ≈ 2C (k_b/k)²

d ln[2C(k_b/k)²] / d ln k = d ln(k⁻²) / d ln k = -2
```

Therefore:

```
n_T = 2 + (-2) = 0
```

**The k² phase-space factor exactly cancels the 1/k² Bogoliubov
scaling, giving a flat spectrum.**

### Why |β_k|² ∝ 1/k²

This follows from scattering theory for a localized potential.
The Born approximation:

```
β_k ≈ -i/(2k) ∫ dη U(η) e^{2ikη}
```

For k → 0:

```
β_k → -i I₀/(2k)     where I₀ = ∫ dη U(η) > 0
```

```
|β_k|² → I₀²/(4k²)
```

This 1/k² scaling is EXACT at leading order for ANY localized
potential and persists beyond the Born approximation. It is
the 1D analog of the s-wave scattering cross-section diverging
at zero energy.

---

## n_T in Each Regime

### k ≪ k_b (infrared signal)

```
n_T = 0      (flat, scale-invariant)
```

Physical reason: all modes with k ≪ k_b "see" the same thin
potential barrier. The scattering amplitude |β_k| ∝ 1/k because
the interaction time ∝ 1/k for a slow mode. Combined with the
k² from the spectrum definition, this gives exactly n_T = 0.

### k ~ k_b (transition)

n_T transitions from 0 to 2 near the peak of the spectrum.
The exact behavior depends on the detailed shape of the Bogoliubov
coefficient transition region.

### k ≫ k_b (vacuum)

```
n_T = 2      (vacuum spectrum)
```

|β_k|² → 0 exponentially, so the spectrum is just the vacuum
P_T ∝ k². This is not a physical signal.

---

## n_T Profile

```
n_T
 3 │
   │
 2 ┤                              *************  (vacuum)
   │                            **
 1 ┤                          **
   │                         *
 0 ┤─────────────────*******── (signal: n_T = 0)
   │
-1 ┤
   │
-2 ┤
   └───────────────────────────────────── log(k/k_b)
     -2    -1     0     1     2     3
```

---

## Comparison with Other Models

| Model | n_T | Mechanism |
|-------|-----|-----------|
| Slow-roll inflation | -r/8 ≈ -0.005 | Horizon exit in quasi-dS |
| **Spin-torsion bounce** | **≈ 0** | **Scattering off bounce potential** |
| Matter bounce | ≈ 0 | Horizon exit in matter contraction |
| Ekpyrotic | ≈ 2 (blue) | Steep contraction, no mode exit |
| Pre-Big-Bang (string) | +3 | Dilaton-driven contraction |

The spin-torsion bounce gives n_T ≈ 0, which is:
- Different from inflation (n_T < 0) — but only marginally
- Same as matter bounce (n_T ≈ 0) — NOT distinctive
- Different from ekpyrotic (n_T ≈ 2) and string (n_T = 3)

**The spectral index n_T ≈ 0 does NOT uniquely identify the
spin-torsion bounce.** It is shared with matter bounce models.

---

## Why the Naive n_T = 2 Argument Fails

An initial estimate assumed |β_k|² ≈ const for k ≪ k_b, which
would give P_T ∝ k² and n_T = 2. This was WRONG because:

1. The constant-|β|² assumption treats the bounce as a "sudden"
   event in conformal time. But even though the bounce is brief
   in COSMIC time (Δt ~ t_Pl), it occupies a finite range in
   CONFORMAL time (Δη ~ 1/(α a_b)).

2. In conformal time, the mode evolution for small k is not
   "frozen" during the bounce — it undergoes significant
   evolution because the potential U is large (U₀ ~ k_b² ≫ k²).

3. The correct behavior is |β_k|² ∝ 1/k², which follows from
   standard 1D scattering theory and is confirmed numerically.

**Lesson:** for bouncing cosmologies with radiation domination,
the tensor spectral index is always n_T ≈ 0, never n_T = 2.
The k² spectrum requires |β_k|² = const, which does NOT hold
for any smooth, localized potential.

---

## Genericity of n_T = 0

The result n_T ≈ 0 is NOT specific to the spin-torsion bounce.
It holds for ANY bouncing cosmology where:

1. The bounce is radiation-dominated (a''/a = 0 away from bounce)
2. The bounce potential U(η) is localized and smooth
3. The initial state is the Bunch-Davies vacuum

The k² × 1/k² cancellation is UNIVERSAL. Only the amplitude
(proportional to I₀² = [∫U dη]²) depends on the specific bounce
model. For the spin-torsion bounce, I₀ is determined by α and a_b.

**This means the spectral tilt cannot distinguish the spin-torsion
bounce from any other radiation-dominated bounce model.**

---

## What WOULD Give n_T ≠ 0?

To obtain a non-zero n_T, one would need:

1. **A non-radiation pre-bounce phase** (w ≠ 1/3): This makes
   a''/a ≠ 0 during contraction, changing the mode evolution
   before the bounce.

2. **A very wide bounce** (Δη ~ 1/k for the mode of interest):
   This violates the "thin barrier" approximation and changes
   the k-dependence of |β_k|².

3. **Additional fields** at the bounce: New degrees of freedom
   could modify the effective potential in a k-dependent way.

None of these apply to the MINIMAL spin-torsion bounce with
radiation domination.

---

## Verdict on n_T

| Statement | Assessment |
|-----------|-----------|
| n_T ≈ 0 at k ≪ k_b | CONFIRMED (analytic + numeric) |
| Blue-tilted? | **NO** (flat spectrum, n_T = 0) |
| Different from inflation? | Marginally (0 vs -0.005) |
| Distinctive to spin-torsion? | **NO** (generic for radiation bounce) |
| Observable? | **NO** (amplitude 10⁻⁶⁴, gap > 10⁴⁹) |
