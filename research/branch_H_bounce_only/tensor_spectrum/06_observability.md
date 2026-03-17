# Observability Assessment

**Date:** 2026-03-15

---

## The Result

The spin-torsion bounce produces a tensor perturbation spectrum
with:

```
Shape:      P_T(k) ≈ constant   for k < k_b    (n_T ≈ 0)
Amplitude:  P_T ≈ 2 × 10⁻⁶⁴    (in dimensionless units)
Peak:       k_b ≈ 1.88 a_b M_Pl  →  f_b ≈ 8 GHz today
```

The spectrum is flat (scale-invariant) below the bounce scale,
with an absolute amplitude of ~10⁻⁶⁴.

---

## Why the Amplitude is 10⁻⁶⁴

The amplitude has three factors:

```
P_T = (4/π²) × (k_b/M_Pl)² × (2|β|² + 1) × (1/a_0²)
```

1. **(k_b/M_Pl)²:** Since k_b = 1.88 a_b M_Pl, this gives
   (1.88 a_b)² ≈ 3.5 a_b² = 3.5 (in a_b = 1 units)

2. **(2|β|² + 1):** The Bogoliubov factor. At k ≪ k_b,
   k² × (2|β_k|²) = 1.71 k_b². So the product of factors
   1 and 2 gives O(1) in Planck units.

3. **1/a_0²:** The dilution factor. Using a_b/a_0 ≈ 9.3 × 10⁻³³:
   ```
   (a_b/a_0)² ≈ 8.6 × 10⁻⁶⁵
   ```

**The dilution factor dominates.** The universe has expanded by
a factor of ~10³² since the bounce. The graviton energy density
has been diluted by (a_b/a_0)⁴ ≈ 10⁻¹²⁹, and the power spectrum
(which scales as amplitude squared / volume) by (a_b/a_0)² ≈
10⁻⁶⁵.

This is the SAME scale separation that killed Foundations A–G,
now manifesting in the perturbation sector.

---

## Band-by-Band Assessment

Since the bounce spectrum is FLAT for f < f_b, the amplitude is
the same at ALL observable frequencies: P_T ≈ 2 × 10⁻⁶⁴.

### CMB Scales (f ~ 10⁻¹⁸ Hz)

**Observable:** B-mode polarization (BICEP, LiteBIRD, CMB-S4)

**Bounce signal:** P_T ≈ 2 × 10⁻⁶⁴

**Detection threshold:** r ≈ 10⁻³ → P_T ≈ 2 × 10⁻¹²

**Gap: 10⁵² orders of magnitude. UNOBSERVABLE.**

### PTA Frequencies (f ~ 10⁻⁸ Hz)

**Observable:** Pulsar timing arrays (NANOGrav, EPTA, PPTA, IPTA)

**Bounce signal:** Ω_GW h² ≈ P_T × (k/(a₀H₀))² / 12 (evaluated
at the relevant k). At PTA frequencies:

```
k_PTA/(a₀H₀) ~ 10¹⁰
Ω_GW h² ~ 10⁻⁶⁴ × 10²⁰ / 12 ~ 10⁻⁴⁵
```

**Detection threshold:** Ω_GW h² ≈ 10⁻⁹

**Gap: 10³⁶. UNOBSERVABLE.**

### LISA Band (f ~ 10⁻² Hz)

**Bounce signal:** Ω_GW h² ~ 10⁻⁶⁴ × (k_LISA/(a₀H₀))² / 12

```
k_LISA/(a₀H₀) ~ 10¹⁶
Ω_GW h² ~ 10⁻⁶⁴ × 10³² / 12 ~ 10⁻³³
```

**Detection threshold:** Ω_GW h² ≈ 10⁻¹³

**Gap: 10²⁰. UNOBSERVABLE.**

### Ground-Based Detectors (f ~ 1–10⁴ Hz)

**LIGO/ET/CE:**

```
k_LIGO/(a₀H₀) ~ 10²⁰
Ω_GW h² ~ 10⁻⁶⁴ × 10⁴⁰ / 12 ~ 10⁻²⁵
```

**Detection threshold:** Ω_GW h² ≈ 10⁻¹⁰ (ET stochastic search)

**Gap: 10¹⁵. UNOBSERVABLE.**

### High-Frequency Detectors (f ~ 10⁶–10¹⁰ Hz)

**Proposed concepts:** magnon-based, inverse Gertsenshtein, BAW

```
k_HF/(a₀H₀) ~ 10²⁸
Ω_GW h² ~ 10⁻⁶⁴ × 10⁵⁶ / 12 ~ 10⁻⁹
```

**Detection threshold:** Ω_GW h² ≈ 10⁻⁵ (optimistic projection)

This is the ONLY band where the signal even APPROACHES detection
thresholds — and it's still 4 orders of magnitude below the
most optimistic projected sensitivity.

---

## Summary Table

| Detector | f [Hz] | Ω_GW h² (bounce) | Ω_GW h² (threshold) | Gap |
|----------|--------|------------------|---------------------|-----|
| CMB (B-mode) | 10⁻¹⁸ | — | r > 10⁻³ | 10⁵² |
| PTA | 10⁻⁸ | 10⁻⁴⁵ | 10⁻⁹ | 10³⁶ |
| LISA | 10⁻² | 10⁻³³ | 10⁻¹³ | 10²⁰ |
| ET | 3 | 10⁻²⁶ | 10⁻¹⁰ | 10¹⁶ |
| LIGO | 100 | 10⁻²⁵ | 10⁻¹⁰ | 10¹⁵ |
| HF (GHz) | 10⁹ | 10⁻⁹ | 10⁻⁵ | **10⁴** |

The best case is high-frequency GHz detectors, where the gap
is "only" 10⁴. But these detectors are at the concept stage
with no timeline for construction.

---

## BBN Constraint

The total GW energy density:

```
Ω_GW,total h² = ∫ d(ln f) Ω_GW(f) h²
```

Since Ω_GW ∝ f⁰ × f² = f² (the flat P_T times the f² from
the energy density conversion), the integral is dominated by the
high-frequency cutoff at f_b:

```
Ω_GW,total h² ~ Ω_GW(f_b) h² × O(1) ~ 10⁻⁹ × O(1)
```

The BBN bound: Ω_GW h² < 1.12 × 10⁻⁶.

**The bounce passes the BBN constraint comfortably.** But this
is not a virtue — the signal is simply too small to constrain
anything.

---

## Could Anything Amplify the Signal?

### 1. More particle production?

|β_k|² ~ 42-800 for k < k_b. Could a modified bounce produce
|β_k|² ~ 10⁵⁰? No — the bounce lasts ~t_Pl, and parametric
amplification is limited by the number of "oscillations" of the
effective potential, which is ~1 for a single bounce.

### 2. Multiple bounces (cyclic)?

If the universe undergoes N bounces, each producing |β|² ~ 42,
the total amplification could be ~ N × 42. For N ~ 10⁵⁰, this
could bridge the gap. But Foundation G showed cyclic cosmology
is incompatible with Λ_obs in spin-torsion gravity.

### 3. Resonance effects?

If the effective potential has oscillatory features, specific
modes could be resonantly amplified (like preheating). But the
spin-torsion bounce potential is a smooth, single bump — no
resonance structure.

### 4. Pre-bounce amplification?

A contracting phase before the bounce could amplify modes at
CMB scales (matter bounce scenario). But this requires ADDITIONAL
physics beyond the spin-torsion bounce:
- A mechanism to produce matter-dominated contraction
- Transition from matter to radiation before the bounce
- No instabilities during contraction

The spin-torsion bounce ALONE does not provide this.

---

## The Honest Assessment

**The spin-torsion bounce, as a MINIMAL model (radiation domination,
single bounce, no pre-bounce phase), produces a tensor spectrum
that is unobservable by at least 10⁴ orders of magnitude at any
detector.**

The flat spectrum (n_T ≈ 0) is a definite prediction, but it:
1. Cannot be tested (amplitude too small)
2. Is not distinctive (shared with matter bounce)
3. Reflects the same scale separation that blocked A–G

**Observable tensor predictions require additional physics beyond
the minimal spin-torsion bounce.** The bounce itself is a
~1 Planck time event that cannot produce enough gravitational
wave power to be detectable after 10³² orders of expansion.

---

## Comparison: Why Inflation Works and the Bounce Doesn't

| Factor | Inflation | Bounce |
|--------|-----------|--------|
| Duration | ~60 e-folds (10⁻³⁶ to 10⁻³² s) | ~ 1 t_Pl (10⁻⁴³ s) |
| Scale of modes produced | Hubble scale H⁻¹ ~ 10⁻²⁶ m | Planck scale l_Pl ~ 10⁻³⁵ m |
| Modes at CMB scale | Produced DIRECTLY at CMB scale | NOT produced at CMB scale |
| Amplification mechanism | Continuous horizon exit | Single scattering event |
| Amount of amplification | exp(2π k/H) per mode | |β|² ~ 42 per mode |

**Inflation produces observable tensors because it operates for
a LONG time at the RIGHT SCALE.** The bounce operates for a
SHORT time at the WRONG SCALE (Planck instead of Hubble).
