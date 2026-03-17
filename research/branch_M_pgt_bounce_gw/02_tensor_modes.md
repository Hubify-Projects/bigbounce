# Tensor Mode Equation for the PGT Bounce

**Date:** 2026-03-16

---

## 1. Tensor Perturbation Equation

### General form

Tensor perturbations h_{ij} on a FRW background satisfy:

```
h_k'' + 2(a'/a) h_k' + k² h_k = 0
```

in conformal time (prime = d/dη), or equivalently with the
canonical variable μ_k = a h_k:

```
μ_k'' + (k² - a''/a) μ_k = 0
```

This is a Schrödinger-type equation with effective potential
V_T(η) = a''/a.

### PGT modifications

In the PGT bounce, there is in principle an additional term from
the propagating torsion mode coupling to tensor perturbations:

```
μ_k'' + (k² - a''/a - δV_torsion) μ_k = 0
```

From Branch L Phase 2 (File 05), the torsion correction is:

```
δV_torsion / (a''/a) ~ m_T/M_Pl ≪ 1
```

**We drop δV_torsion.** The torsion-specific correction is
negligible (suppressed by 12–26 orders of magnitude). The tensor
equation is the STANDARD GR equation on the modified background.

This is the defining feature of the Branch M analysis: the GW
spectrum comes from the BACKGROUND GEOMETRY, not from torsion
perturbative effects.

---

## 2. Effective Potential

### Exact expression (cosmic time parameterization)

From File 01:

```
a''/a = a_b² × 2α² / (1 + 4α²t²)^{3/2}
```

where α = m_T √(8π/3).

### In dimensionless variables

Define τ = αt (dimensionless cosmic time) and κ = k/k_b
(dimensionless wavenumber, with k_b = α a_b). Then the mode
equation in conformal time becomes:

```
d²μ_κ/dη̃² + (κ² - Ṽ(η̃)) μ_κ = 0
```

where η̃ = k_b η is dimensionless conformal time and:

```
Ṽ(η̃) = (a''/a) / k_b² = 2 / (1 + 4τ²)^{3/2}    [in cosmic time]
```

The conformal time version requires the η(t) mapping. Near the
bounce (τ ≪ 1):

```
η̃ ≈ τ    (since a ≈ a_b → dη = dt/a_b)
Ṽ ≈ 2(1 - 6τ²)    [Taylor expansion]
```

### Potential shape

```
     Ṽ
     |
  2  |    ****
     |  **    **
     |**        **
  1  |            **
     |              ***
     |                 ****
  0  |________________________ η̃
    -3  -2  -1   0   1   2   3
```

- Peak value: Ṽ(0) = 2
- Half-maximum width: Δη̃ ~ 0.77 (from File 01: t_{1/2} ≈ 0.383/α)
- Decay: Ṽ ~ 2/|η̃|³ for |η̃| ≫ 1

### Comparison with other potentials

| Model | Potential shape | Peak value | Decay |
|-------|----------------|-----------|-------|
| PGT radiation bounce | Smooth bell, (1+4τ²)^{-3/2} | 2 k_b² | 1/η³ |
| De Sitter inflation | ν²/η² (power law) | ∞ at η→0 | 1/η² |
| LQC bounce | Similar bell + quantum corrections | ~ k_b² | 1/η³ |
| Matter bounce | Different shape (w=0 contraction) | ~ k_b² | 1/η² |

The radiation bounce potential is:
- SHARPER than de Sitter (decays as 1/η³ vs 1/η²)
- FINITE at the bounce (unlike de Sitter which diverges)
- SYMMETRIC about η = 0 (unlike inflation which has only one side)

---

## 3. Mode Solutions

### WKB regions

For κ² ≫ Ṽ (high k, away from bounce): modes oscillate freely.

```
μ_κ ≈ (1/√2k) exp(±ikη)
```

No particle production in WKB regime.

### Scattering problem

The symmetric potential defines a quantum scattering problem.
An incoming plane wave from η → -∞ (contracting phase) scatters
off the potential and emerges as a superposition of transmitted
and reflected waves at η → +∞ (expanding phase):

```
μ_κ → (1/√2k) [α_k e^{-ikη} + β_k e^{+ikη}]    as η → +∞
```

where α_k, β_k are the Bogoliubov coefficients satisfying
|α_k|² - |β_k|² = 1.

The number of gravitons produced:

```
N_k = |β_k|²
```

### Analytic estimate for |β_k|²

For a smooth symmetric potential barrier of height V₀ and width Δ:

**Over-barrier (k² > V₀):** WKB gives exponentially small reflection:

```
|β_k|² ~ exp(-2 ∫ dk̃ √(k̃² - V₀)) ~ exp(-π k Δ)
```

For k ≫ k_b: |β_k|² ~ exp(-π k/k_b) (exponential suppression).

**Under-barrier (k² < V₀ = 2k_b²):** The mode tunnels through.
For k ≪ k_b:

```
|β_k|² ~ (k/k_b)^{2n}
```

where n depends on the potential shape. For the radiation bounce
potential V = 2k_b²/(1+4τ²)^{3/2}, the low-k behavior can be
derived from the asymptotic matching.

### Low-k limit: super-horizon modes

For k ≪ k_b, the mode spends the entire bounce in the
super-horizon regime (k² ≪ a''/a). The growing and decaying
solutions:

```
μ_grow ~ a(η)
μ_decay ~ a(η) ∫ dη'/a²(η')
```

The growing mode gives constant h_k (frozen perturbation). The
time-reversal symmetry of the bounce maps the growing mode of
contraction to the decaying mode of expansion (same as Branch K
for scalars). Result: |β_k|² → const for k → 0.

Specifically, for the symmetric radiation bounce:

```
|β_k|² → C₀ × (k/k_b)⁰ = C₀    for k → 0
```

where C₀ is an order-unity constant determined by the exact
potential shape.

### Summary of |β_k|² behavior

```
|β_k|² ≈ { C₀                           for k ≪ k_b
          { oscillatory × (k_b/k)²       for k ~ k_b
          { exp(-π k/k_b)                 for k ≫ k_b
```

---

## 4. Gravitational Wave Energy Density Spectrum

### Definition

```
Ω_GW(k) = (1/ρ_c) × dρ_GW/d ln k
```

where ρ_c = 3H₀²M_Pl²/(8π) is the critical density today.

### Relation to Bogoliubov coefficients

The GW energy density per logarithmic frequency interval:

```
Ω_GW(k) = (k²/(12 H₀² a₀²)) × P_T(k)
```

where P_T(k) is the tensor power spectrum. For modes that were
in the vacuum state before the bounce:

```
P_T(k) = (2/π²) × (k/a₀)² × |β_k|² / k
        = (2/π²) × (k/a₀²) × |β_k|²
```

Wait — more carefully. The tensor power spectrum from particle
production:

```
P_T(k) = (16πG/π²) × (k³/2π²) × |μ_k|²/a²
```

For the vacuum + produced particles:

```
|μ_k|² = (1 + 2|β_k|²) / (2k)
```

The excess over vacuum (the produced gravitons):

```
P_T^{bounce}(k) = (16πG) × (k²/(2π²a²)) × |β_k|²/k
                 = (8G/π) × (k/a)² × |β_k|²
```

### Ω_GW today

After redshifting to today:

```
Ω_GW(f) = Ω_rad × (k/k_eq)² × |β_k|²   [for k > k_eq, sub-horizon at matter-radiation equality]
```

More precisely:

```
Ω_GW(f) h² = (3 Ω_rad h²) / (4π²) × (H_b/M_Pl)² × |β_k|² × T²(k)
```

where H_b ~ α ~ m_T is the Hubble scale at the bounce and T(k)
is the transfer function from bounce to today (accounting for
expansion history).

### Standard parametrization

Using the result from cosmological GW backgrounds:

```
Ω_GW(f) h² ≈ 1.6 × 10⁻⁵ × (g_*/g_{*,0}) × (H_b/M_Pl)² × |β_k|²
```

With H_b ~ α ~ m_T:

```
Ω_GW(f) h² ≈ 1.6 × 10⁻⁵ × (m_T/M_Pl)² × |β_k|²
```

For modes at the bounce scale (k ~ k_b, |β_k|² ~ O(1)):

```
Ω_GW(f_b) h² ~ 10⁻⁵ × (m_T/M_Pl)²
```

This is the PEAK amplitude.

### Spectral shape from |β_k|² behavior

```
Ω_GW(f) h² ≈ 1.6 × 10⁻⁵ × (m_T/M_Pl)² × |β_{k(f)}|²
```

Substituting the three regimes:

| Frequency range | |β_k|² | Ω_GW h² |
|----------------|--------|---------|
| f ≪ f_b | C₀ (constant) | ~ 10⁻⁵ (m_T/M_Pl)² |
| f ~ f_b | O(1), oscillatory | ~ 10⁻⁵ (m_T/M_Pl)² |
| f ≫ f_b | exp(-πf/f_b) | exponentially suppressed |

**The spectrum is approximately FLAT for f < f_b, with an
exponential cutoff above f_b.**

---

## 5. Comparison with Branch H (Minimal EC)

The Branch H tensor spectrum had:

```
P_T ~ 10⁻⁶⁴    (at CMB scales, undetectable)
```

because k_b was at GHz (f_b ~ 40 GHz) and the spectrum was
evaluated at f ~ 10⁻¹⁸ Hz (CMB).

In the PGT case, f_b is at Hz–mHz. The spectrum at f ~ f_b
is:

```
Ω_GW(f_b) h² ~ 10⁻⁵ × (m_T/M_Pl)²
```

For m_T = 10⁻³ GeV (decihertz band):

```
Ω_GW h² ~ 10⁻⁵ × (10⁻³/10¹⁹)² = 10⁻⁵ × 10⁻⁴⁴ = 10⁻⁴⁹
```

**Still far below detector sensitivity (10⁻¹³ for LISA).**

### Wait — this contradicts the Phase 2 estimate

Phase 2 (File 06) estimated Ω ~ 10⁻⁵ × ε with ε ~ O(1).
The issue: the Phase 2 estimate assumed the bounce converts an
O(1) fraction of its energy to GWs. But the Bogoliubov calculation
shows that only the VACUUM fluctuation modes near k_b are amplified,
and their energy is:

```
ρ_GW / ρ_crit = ∫ d ln k × (k⁴/ρ_crit) × |β_k|²/(2k)
              ~ k_b⁴ / ρ_crit ~ (m_T a_b)⁴ / (m_T² M_Pl²)
```

The factor a_b⁴ is crucial. At the bounce, a_b ≪ a_0, and the
physical wavenumber is k_b/a_b ~ m_T (in natural units). The
energy density of produced gravitons at the bounce:

```
ρ_GW(bounce) ~ ∫ dk k³ |β_k|² / (2π²a_b⁴)
             ~ k_b⁴ / (a_b⁴ × 2π²) × (Δk/k_b) × |β|²
             ~ m_T⁴ / (2π²)    for |β|² ~ 1 near k_b
```

The fraction:

```
ε = ρ_GW / ρ_crit ~ m_T⁴ / (m_T² M_Pl²) = m_T²/M_Pl²
```

**The conversion efficiency is ε ~ (m_T/M_Pl)², NOT O(1).**

The Phase 2 estimate was too optimistic. The correct peak amplitude:

```
Ω_GW(f_b) h² ~ 10⁻⁵ × (m_T/M_Pl)² × |β_peak|²
             ~ 10⁻⁵ × (m_T/M_Pl)²
```

This recovers the amplitude from the Bogoliubov calculation and
is much smaller than the naïve ε ~ O(1) estimate.

---

## 6. Revised Amplitude Table

| m_T (GeV) | f_b (Hz) | (m_T/M_Pl)² | Ω_GW h² (peak) | Band |
|-----------|---------|-----------|--------------|------|
| 10⁷ | 2.4 × 10⁴ | 10⁻²⁴ | 10⁻²⁹ | LIGO |
| 10⁵ | 2.4 × 10³ | 10⁻²⁸ | 10⁻³³ | LIGO |
| 10³ | 2.4 × 10² | 10⁻³² | 10⁻³⁷ | LIGO |
| 10 | 24 | 10⁻³⁶ | 10⁻⁴¹ | ET |
| 10⁻¹ | 2.4 | 10⁻⁴⁰ | 10⁻⁴⁵ | ET |
| 10⁻³ | 0.24 | 10⁻⁴⁴ | 10⁻⁴⁹ | Decihertz |
| 10⁻⁵ | 0.024 | 10⁻⁴⁸ | 10⁻⁵³ | LISA |
| 10⁻⁷ | 2.4 × 10⁻³ | 10⁻⁵² | 10⁻⁵⁷ | LISA |

**ALL values are far below detector sensitivity.**

Detector sensitivities:
- LIGO: Ω_GW h² ~ 10⁻⁹
- ET: Ω_GW h² ~ 10⁻¹³
- LISA: Ω_GW h² ~ 10⁻¹³
- DECIGO: Ω_GW h² ~ 10⁻¹⁶

Minimum gap to ANY detector: **10¹³ (for LIGO at m_T ~ 10⁷ GeV).**

---

## 7. What Went Wrong with the Phase 2 Estimate

The Phase 2 naïve argument was:

> "Any bounce converts O(1) of its energy to GWs."

This is WRONG for vacuum fluctuation amplification. The correct
statement:

> "The bounce amplifies vacuum modes near k_b, producing graviton
> number |β_k|² ~ O(1). But the ENERGY in these gravitons is
> ~ k_b⁴ ~ m_T⁴, while the total energy is ρ_crit ~ m_T² M_Pl².
> The fraction is m_T²/M_Pl² ≪ 1."

The factor (m_T/M_Pl)² is the familiar graviton-production
suppression: the bounce creates O(1) gravitons per mode, but each
graviton carries energy ~ m_T, while the total energy budget is
~ m_T M_Pl. The ratio is m_T/M_Pl per graviton, squared for
energy density.

**This is NOT the mass-coupling lock.** This is the standard
graviton-production efficiency in ANY cosmological background.
It applies to inflation too (where Ω_GW ~ 10⁻⁵ × r, with r
proportional to (H_inf/M_Pl)²).
