# Tensor Power Spectrum from the Spin-Torsion Bounce

**Date:** 2026-03-15

---

## Setup

The tensor perturbation equation:

```
v_k'' + (k² - a''/a) v_k = 0
```

with effective potential:

```
U(η) = a''/a = 2α²a_b² / (1 + 4α²t(η)²)^{3/2}
```

The potential is a localized positive bump centered at the bounce.
Far from the bounce (pure radiation), U = 0 exactly.

---

## Bogoliubov Coefficients: Numerical Results

The tensor mode equation was solved numerically for k/k_b
ranging from 0.03 to 16 (see notebook 03).

### Key numerical finding

The Bogoliubov coefficient follows:

```
┌──────────────────────────────────────────────────────┐
│                                                      │
│   |β_k|² ≈ C × (k_b/k)²    for k ≪ k_b             │
│                                                      │
│   with C ≈ 0.855  (numerically determined)           │
│                                                      │
└──────────────────────────────────────────────────────┘
```

Numerical verification (k² |β_k|² / k_b² should be constant):

| k/k_b | |β_k|² | k² |β_k|² / k_b² |
|--------|--------|-------------------|
| 0.032 | 857 | 0.855 |
| 0.049 | 363 | 0.857 |
| 0.060 | 236 | 0.856 |
| 0.075 | 154 | 0.855 |
| 0.092 | 100 | 0.854 |
| 0.114 | 64.8 | 0.849 |
| 0.142 | 42.0 | 0.844 |
| 0.218 | 17.5 | 0.831 |

The product k² |β_k|² is constant to ~3% across a decade in k.

### Physical origin of the 1/k² scaling

This follows from scattering theory. For a localized potential
U(η) with Fourier transform Ũ(q), the Born approximation gives:

```
|β_k| ≈ |Ũ(2k)| / (2k)
```

For k → 0: Ũ(0) = ∫ U(η) dη = I₀ (a finite positive number).

```
|β_k|² → I₀² / (4k²)    as k → 0
```

This 1/k² scaling is EXACT at leading order and persists beyond
the Born regime. It is a universal result for scattering off any
localized potential in 1D.

### k-dependence summary

| Regime | |β_k|² | Scaling |
|--------|--------|---------|
| k ≪ k_b | C(k_b/k)² ≈ 0.855 k_b²/k² | Inverse square |
| k ~ k_b | ~ 1 | Transition region |
| k ≫ k_b | → 0 | Exponential suppression |

### Normalization check

The Bogoliubov normalization |α_k|² - |β_k|² = 1 was verified
to 10⁻⁶ precision at all k values.

---

## Power Spectrum

The tensor power spectrum (two polarizations):

```
P_T(k) = (4k²)/(π² M_Pl²) × (1 + 2|β_k|²) × (1/a²)
```

The shape is determined by k² × (1 + 2|β_k|²).

### Three regimes

**1. k ≪ k_b (infrared — bounce signal):**

|β_k|² ≈ C k_b²/k² with C ≈ 0.855. The k² prefactor CANCELS
the 1/k² from the Bogoliubov coefficient:

```
P_T(k) ∝ k² × 2C k_b²/k² = 2C k_b² = CONSTANT
```

```
┌──────────────────────────────────────────────────┐
│                                                  │
│   P_T(k) ≈ CONSTANT    for k ≪ k_b              │
│                                                  │
│   The spectrum is FLAT (scale-invariant)          │
│   n_T ≈ 0                                        │
│                                                  │
└──────────────────────────────────────────────────┘
```

**This is a critical result.** The bounce produces a SCALE-
INVARIANT tensor spectrum at low k, not a blue-tilted one.

**2. k ~ k_b (bounce scale):**

|β_k|² ~ O(1). Transition between the flat signal regime and
the vacuum-dominated regime.

**3. k ≫ k_b (ultraviolet — vacuum):**

|β_k|² → 0. The spectrum approaches the vacuum:

```
P_T(k) → (4k²)/(π² M_Pl² a²)    (vacuum, n_T = 2)
```

This is NOT a signal — it is the standard vacuum spectrum.

---

## Spectrum Shape

```
log P_T
    │
    │                                    **** (vacuum k²)
    │                                ****
    │                            ****
    │                        ****
    ├────── * * * * * * * ****── ← flat signal (n_T = 0)
    │                   ***
    │                  *
    │  bounce signal  *   vacuum
    │  dominates      *   dominates
    │                *
    │               *
    └───────────────────────────────── log k
                    k_b
```

The flat signal (n_T ≈ 0) dominates at k < k_b.
The rising vacuum (n_T = 2) dominates at k > k_b.
The transition occurs near k ~ k_b.

---

## Absolute Amplitude

The flat spectrum amplitude (for k ≪ k_b):

```
P_T = (4/π²M_Pl²a_0²) × 2 × 0.855 × k_b²
    = (4 × 1.71 × 1.88² × a_b² × M_Pl²)/(π² M_Pl² a_0²)
    = (4 × 1.71 × 3.53 × (a_b/a_0)²) / π²
```

Using a_b/a_0 ≈ 9.3 × 10⁻³³:

```
P_T ≈ 24.2 × (9.3 × 10⁻³³)² / 9.87
    ≈ 2.1 × 10⁻⁶⁴
```

This is a tiny number. Compare:
- CMB tensor bound: r < 0.036 → P_T < 7.5 × 10⁻¹¹
- Bounce signal: P_T ≈ 2 × 10⁻⁶⁴

The gap is **10⁵³ orders of magnitude.**

---

## P_T at Observable Frequencies

Because the bounce signal is FLAT (n_T ≈ 0), the amplitude at
ALL frequencies below k_b is the SAME:

```
P_T(f) ≈ 2 × 10⁻⁶⁴    for ALL f < f_b ≈ 8 GHz
```

| Scale | f [Hz] | P_T | Detection threshold | Gap |
|-------|--------|-----|--------------------|----- |
| CMB | 10⁻¹⁸ | 2×10⁻⁶⁴ | 10⁻¹⁰ | 10⁵⁴ |
| PTA | 10⁻⁸ | 2×10⁻⁶⁴ | 10⁻¹⁵ | 10⁴⁹ |
| LISA | 10⁻² | 2×10⁻⁶⁴ | 10⁻¹³ | 10⁵¹ |
| ET | 3 | 2×10⁻⁶⁴ | 10⁻¹³ | 10⁵¹ |
| LIGO | 100 | 2×10⁻⁶⁴ | 10⁻¹⁰ | 10⁵⁴ |

**At every observable frequency, the bounce signal is at least
10⁴⁹ below the detection threshold.**

---

## The Fundamental Problem

The bounce tensor spectrum has one overwhelming problem:

### Amplitude suppression from dilution

The amplitude is suppressed by (a_b/a_0)² ≈ 10⁻⁶⁵. This factor
comes from the expansion of the universe from the bounce to today:

```
P_T ∝ 1/a² ∝ (a_b/a_0)²
```

The bounce creates gravitons at Planck energy, but by today they
have been diluted by 10⁶⁵ orders of magnitude in power. No
amount of particle creation (|β|² ~ 1–1000) can compensate this.

**The dilution factor (a_b/a_0)² ≈ 10⁻⁶⁵ is the same scale
separation barrier identified throughout the A–G program, now
appearing in the perturbation sector.**

---

## Comparison with Inflation

| Property | Inflation | Spin-torsion bounce |
|----------|-----------|-------------------|
| n_T | -r/8 < 0 (red) | ≈ 0 (flat) |
| Spectrum shape | Nearly flat (slight red) | Flat below k_b, vacuum above |
| CMB amplitude | P_T ~ 10⁻¹⁰ × r | P_T ~ 10⁻⁶⁴ |
| Observable? | Yes (if r > 10⁻³) | No (by 10⁵⁰+) |
| Mechanism | Horizon exit during inflation | Scattering off bounce potential |

Inflation produces observable tensors because it operates for
~60 e-folds, continuously amplifying modes at the Hubble scale.
The bounce operates for ~1 Planck time at the Planck scale —
a single, brief event that creates gravitons but not enough to
overcome dilution.

---

## Summary

```
P_T(k) ≈ 2 × 10⁻⁶⁴     for k ≪ k_b  (n_T ≈ 0, flat)
P_T(k) peaks at k ~ k_b ≈ 1.88 a_b M_Pl
Peak frequency today: f_b ≈ 8 GHz
Amplitude at ALL observable frequencies: ~ 2 × 10⁻⁶⁴
Detection gap: > 10⁴⁹ at every detector band
```

**The tensor power spectrum is approximately scale-invariant
(n_T ≈ 0) but has an amplitude of ~10⁻⁶⁴, making it unobservable
by at least 49 orders of magnitude at every frequency band.**
