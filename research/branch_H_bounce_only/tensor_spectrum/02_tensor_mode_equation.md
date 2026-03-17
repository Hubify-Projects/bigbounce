# Tensor Mode Equation Through the Bounce

**Date:** 2026-03-15

---

## Tensor Perturbations on FRW

The metric with tensor perturbations:

```
ds² = a²(η)[-dη² + (δ_ij + h_ij)dx^i dx^j]
```

where h_ij is transverse-traceless: h^i_i = 0, ∂_i h^{ij} = 0.

Each Fourier mode h_k has two polarizations (+, ×). The equation
of motion from the linearized Einstein equations:

```
h_k'' + 2(a'/a)h_k' + k²h_k = 0
```

---

## Mukhanov Variable for Tensors

Define the canonical variable:

```
v_k = (a M_Pl / 2) h_k
```

Substituting into the equation of motion:

```
v_k'' + (k² - a''/a) v_k = 0
```

This is a Schrödinger-type equation with effective potential
U(η) = a''/a.

---

## The Effective Potential

### Standard radiation domination (no bounce)

For a ∝ η: a'' = 0, so U(η) = 0.

The tensor modes are FREE PLANE WAVES at all times:
```
v_k = (1/√(2k)) e^{-ikη}   (positive frequency)
```

No mode amplification occurs. No gravitational wave production.
This is the well-known result that radiation domination does not
produce tensor perturbations.

### Spin-torsion bounce

From the background solution:

```
U(η) = a''/a = 2α²a_b² / (1 + 4α²t(η)²)^{3/2}
```

This is a LOCALIZED POSITIVE BUMP centered at the bounce (η = 0).

```
         U(η)
          │
  2α²a_b² ┤ ·····***·····
          │ ····*   *····
          │ ···*     *···
          │ ··*       *··
          │ ·*         *·
          │·*           *·
          0─────────────────── η
              ← Δη →
```

The bump:
- Height: U_0 = 2α²a_b² ≈ 3.52 M_Pl² a_b²
- Width: Δη ~ 1/(α a_b) ~ 1/(1.33 M_Pl a_b)
- Area: ∫U dη > 0 (positive definite)

---

## Mode Behavior in Different k Regimes

### k ≫ k_b (high frequency, short wavelength)

The mode oscillation period is MUCH shorter than the bounce
duration. The potential U is a slow perturbation:

```
v_k ≈ (1/√(2k)) e^{-ikη}    (adiabatic, unaffected)
```

No significant mode mixing. |β_k|² → 0 exponentially.

### k ~ k_b (resonant scale)

Maximum interaction with the potential. Strong mode mixing.
Must be solved numerically.

### k ≪ k_b (low frequency, long wavelength)

The mode wavelength is MUCH longer than the bounce duration. The
mode "sees" the bounce as a sudden event:

```
v_k'' ≈ U(η) v_k    (k² term negligible)
```

Two independent solutions:
- Growing: v₁ = a (verified: a'' = U × a)
- Decaying: v₂ = a ∫^η dη'/a²

The incoming vacuum mode connects to a specific combination of
growing and decaying modes after the bounce.

---

## Bogoliubov Transformation

Before the bounce (η → -∞), the mode is in the vacuum state:

```
v_k^{in} = (1/√(2k)) e^{-ikη}
```

After the bounce (η → +∞), the mode is a superposition:

```
v_k^{out} = α_k (1/√(2k)) e^{-ikη} + β_k (1/√(2k)) e^{+ikη}
```

where α_k and β_k are the Bogoliubov coefficients satisfying:

```
|α_k|² - |β_k|² = 1
```

The number of gravitons produced per mode:

```
n_k = |β_k|²
```

---

## Why the Bounce Produces Gravitons

In standard radiation domination: a''/a = 0 → no potential →
no scattering → β_k = 0 → no graviton production.

The bounce breaks this by creating a transient potential barrier
U(η) > 0. This barrier REFLECTS incoming modes, converting
negative-frequency components into positive-frequency components
(particle creation).

The physical mechanism: the rapid change in the expansion rate
during the bounce does work on the vacuum fluctuations, promoting
virtual graviton pairs to real gravitons.

---

## Born Approximation (k ≫ k_b)

For high-frequency modes, the first Born approximation gives:

```
β_k ≈ (1/2ik) ∫_{-∞}^{+∞} dη U(η) e^{2ikη}
```

```
|β_k|² ≈ (1/4k²) |Ũ(2k)|²
```

where Ũ(q) = ∫ U(η) e^{iqη} dη is the Fourier transform of the
effective potential.

For a potential of width Δη ~ 1/(αa_b) and height U_0 ~ α²a_b²:

```
|Ũ(q)|² ~ U_0² Δη² × exp(-2q²Δη²)  [Gaussian estimate]
```

At q = 2k:

```
|β_k|² ~ (α²a_b² / k)² × exp(-8k²/(α²a_b²))
        = (k_b²/k)² × exp(-4k²/k_b²)    [for k ≫ k_b]
```

Exponential suppression above the bounce scale. ✓

---

## Low-k Limit (k ≪ k_b)

### Born approximation

For a localized potential U(η), the first Born approximation:

```
β_k ≈ -(i/2k) ∫ dη U(η) e^{2ikη}
```

For k → 0:

```
|β_k|² → I₀²/(4k²)     where I₀ = ∫ U(η) dη > 0
```

This gives |β_k|² ∝ 1/k² — diverging at low k. The 1/k²
scaling is EXACT at leading order (standard 1D scattering theory)
and persists beyond the Born regime.

### Numerical confirmation

The mode equation was solved numerically (notebook 03). The
product k² |β_k|² is constant to ~3% for k/k_b from 0.03 to 0.2:

```
k² |β_k|² ≈ 0.855 k_b²    (numerically determined)
```

At specific values:
- k/k_b = 0.14: |β_k|² ≈ 42
- k/k_b = 0.09: |β_k|² ≈ 100
- k/k_b = 0.03: |β_k|² ≈ 860

### Physical meaning

The 1/k² scaling means: longer-wavelength modes are MORE strongly
affected by the bounce. This is because the interaction time
scales as 1/k for a slow mode traversing a localized potential.
The amplitude of particle production grows without bound as
k → 0 (though the energy per particle decreases).

For the power spectrum, the k² phase-space factor CANCELS the
1/k² from |β_k|², giving a FLAT (scale-invariant) spectrum.

---

## Expected Spectrum Shape

```
|β_k|²:

 ~860 ┤ *
      │ *
      │  *
 ~100 ┤   *
      │    **
  ~42 ┤      *
      │       **
      │         ***
   ~1 ┤ · · · · · · ***· · · · ·
      │                 ****
   ~0 ┤                     *****→ 0
      └──────────────────────────────── k
      0          k_b        2k_b
```

Three regimes:
1. k ≪ k_b: |β_k|² ∝ 1/k² (inverse square law)
2. k ~ k_b: transition region, |β_k|² ~ 1
3. k ≫ k_b: |β_k|² → 0 exponentially

---

## Key Result: Radiation a''/a = 0 Away From Bounce

The most important structural feature is that for pure radiation
domination, a''/a = 0 EXACTLY. This means:

1. There is NO amplification of modes outside the bounce region
2. ALL graviton production comes from the bounce itself
3. The spectrum has a HARD characteristic scale k_b ~ a_b M_Pl
4. Modes with k ≪ k_b are produced with roughly equal occupation
   number |β|² ≈ const
5. Modes with k ≫ k_b are not produced

This is fundamentally different from inflation, where the
effective potential a''/a ≈ 2/η² persists for the entire
inflationary epoch, producing modes continuously as they exit the
Hubble radius.
