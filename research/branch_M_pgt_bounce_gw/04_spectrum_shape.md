# Spectral Shape of the PGT Bounce GW Background

**Date:** 2026-03-16

---

## 1. The Universal Bounce Spectrum

### Three regimes

The GW spectrum from a symmetric radiation bounce has a universal
shape determined by the Bogoliubov coefficients |β_κ|² as a
function of κ = k/k_b:

```
                    |β_κ|²
                 |
            C₀   |--------\
                 |          \
                 |           \  oscillations
                 |            \.../\.../\
                 |                       \
                 |                        \  exp(-πκ)
            10⁻⁵ |                         \
                 |______________________________\_____ κ
                 0.01    0.1     1      3     10
```

**Regime I (κ ≪ 1): Flat plateau**

```
|β_κ|² → C₀ ≈ const.
```

Super-horizon modes (k ≪ k_b) are amplified uniformly by the
bounce. The constant C₀ depends on the exact bounce profile:

- For a sharp (instantaneous) bounce: C₀ = 1/4
- For the radiation bounce a = a_b(1+4α²t²)^{1/4}: C₀ ~ 0.1–0.5
  (determined numerically)
- For a smoother bounce: C₀ < 0.1

The plateau gives a FLAT Ω_GW spectrum at low frequencies:

```
Ω_GW ∝ |β_κ|² = const.    →   n_T = 0 (scale-invariant)
```

**Regime II (κ ~ 1): Oscillatory peak**

```
|β_κ|² ~ (C₀/κ²) × [1 + A sin(2κ + φ)]
```

Near the bounce scale, modes interact resonantly with the
effective potential. The Bogoliubov coefficient shows oscillatory
features superimposed on a 1/κ² envelope. The oscillation period
is Δκ ~ 1 (set by the bounce width in conformal time).

**Regime III (κ ≫ 1): Exponential cutoff**

```
|β_κ|² ~ exp(-πκ)
```

Sub-horizon modes pass through the bounce adiabatically. The
particle production is exponentially suppressed. The decay constant
π is characteristic of a smooth, symmetric barrier (WKB tunneling
exponent for the potential V = 2/(1+4τ²)^{3/2}).

---

## 2. Spectral Tilt

### At low frequencies (f ≪ f_b)

The spectrum is flat:

```
n_T = d ln Ω_GW / d ln f = 0    (at f ≪ f_b)
```

This is **scale-invariant**, the same as de Sitter inflation
at leading order.

### At intermediate frequencies (f ~ f_b)

The spectrum transitions from flat to falling. The effective tilt:

```
n_T(f ~ f_b) ~ -2    (from the 1/κ² envelope)
```

### At high frequencies (f ≫ f_b)

The spectrum falls exponentially:

```
Ω_GW ∝ exp(-πf/f_b)
```

No power-law tilt is defined in this regime.

---

## 3. Cutoff Frequency

### Definition

The frequency above which the spectrum is suppressed by more than
e⁻¹ relative to the plateau:

```
f_cut ≈ f_b / π ≈ 0.32 f_b
```

For the numerical profile: the transition from plateau to
exponential falloff occurs at κ_cut ~ 1–2, so:

```
f_cut ~ f_b to 2f_b
```

### Dependence on m_T

```
f_cut ~ f_b = 2.6 × 10¹⁰ × (m_T/M_Pl)^{1/2}  Hz
```

| m_T (GeV) | f_cut (Hz) | Band |
|-----------|-----------|------|
| 10⁷ | ~10⁴ | LIGO upper |
| 10³ | ~10² | LIGO |
| 10⁻¹ | ~2 | ET |
| 10⁻⁵ | ~0.02 | LISA/Decihertz |
| 10⁻⁹ | ~2 × 10⁻⁴ | LISA |

---

## 4. Comparison with Inflationary Spectrum

### Inflationary GW background

Slow-roll inflation produces:

```
Ω_GW^{inf}(f) h² = A_T × (f/f_*)^{n_T} × T²(f)
```

where:
- A_T ~ 10⁻¹⁵ r (with r ~ 0.01–0.06 if tensor modes exist)
- n_T = -r/8 (consistency relation, slightly red)
- T²(f) is the transfer function (constant for f > f_eq)
- The spectrum extends from f ~ 10⁻¹⁸ Hz (horizon) to
  f ~ 10⁸ Hz (reheating scale)

**Shape: nearly flat over many decades** (very slight red tilt).

### PGT bounce GW background

```
Ω_GW^{bounce}(f) h² = 1.6 × 10⁻⁵ × (m_T/M_Pl)² × |β(f/f_b)|²
```

**Shape: flat for f < f_b, exponential cutoff above f_b.**

### Key differences

| Property | Inflation | PGT bounce |
|----------|----------|-----------|
| Low-f tilt | n_T = -r/8 (red, small) | n_T = 0 (flat) |
| Frequency range | 10⁻¹⁸ to ~10⁸ Hz | 0 to ~f_b |
| Cutoff | At reheating scale (~10⁸ Hz) | At f_b (tunable) |
| Oscillations | None | Near f_b |
| Amplitude | ~ 10⁻¹⁵ r | ~ 10⁻⁵ (m_T/M_Pl)² |

### Shape distinguishability

**In principle, the bounce spectrum is distinguishable** from
inflation by:

1. **The exponential cutoff** at f_b. Inflation has no sharp
   cutoff in the GW detector bands (reheating cutoff is at
   much higher frequency).

2. **The oscillatory features** near f_b. Inflation produces
   a smooth, featureless spectrum.

3. **Exact scale invariance** (n_T = 0) below f_b. Inflation
   gives a tiny red tilt n_T = -r/8.

**In practice, none of these differences are detectable** because
the bounce spectrum amplitude is 10¹³–10⁴⁹ below detector
sensitivity (the (m_T/M_Pl)² suppression).

---

## 5. Comparison with LQC Bounce

### LQC spectrum

Loop quantum cosmology also produces a bounce GW background:

```
Ω_GW^{LQC}(f) ~ 10⁻⁵ × (ρ_crit^{LQC}/M_Pl⁴) × |β^{LQC}(f/f_b^{LQC})|²
```

with ρ_crit^{LQC} ≈ 0.41 ρ_Pl (close to the Planck scale in LQC).

The LQC bounce has additional quantum-geometry corrections that
modify the effective potential:

```
V_LQC(η) = a''/a + δV_quantum
```

where δV_quantum encodes holonomy and inverse-volume corrections.

### Shape comparison

| Property | PGT bounce | LQC bounce |
|----------|-----------|-----------|
| Low-f behavior | Flat (n_T = 0) | Flat or slightly blue |
| Cutoff | At f_b = f(m_T) | At f_b^{LQC} ~ 10⁸–10¹⁰ Hz |
| Oscillation period | Set by a''/a shape | Modified by quantum corrections |
| Amplitude | (m_T/M_Pl)² × 10⁻⁵ | ~10⁻⁵ × 0.41 ~ 4 × 10⁻⁶ |

The LQC bounce has ρ_crit close to M_Pl⁴, so its amplitude is
much larger: Ω ~ 10⁻⁶ (close to detectable with future experiments).
But f_b^{LQC} ~ 10⁸–10¹⁰ Hz, far above all GW detectors.

**The PGT bounce can have f_b in detector bands but with
undetectable amplitude. LQC has near-detectable amplitude but
at frequencies far above detector bands.**

Both face the SAME tradeoff: amplitude × frequency² ~ const.

---

## 6. High-Frequency Tail

### Shape of the exponential cutoff

For κ > 1, the WKB approximation gives:

```
|β_κ|² ≈ exp(-2 Im ∫ √(κ² - Ṽ(η)) dη)
```

where the integral is over the classically forbidden region
(where κ² < Ṽ).

For the radiation bounce potential Ṽ = 2/(1+4τ²)^{3/2}:

The turning points η_±(κ) satisfy:
```
κ² = 2/(1 + 4τ²)^{3/2}
```

For κ² < 2 (under-barrier): two real turning points exist.
For κ² > 2: no real turning points (fully over-barrier), the
exponential integral comes from the complex-τ plane.

The decay constant in the exponential:

```
|β_κ|² ~ exp(-α_decay × κ)
```

where α_decay depends on the exact potential shape. For a generic
smooth barrier: α_decay ~ π (order of magnitude).

For the specific radiation bounce: α_decay can be computed
numerically (see notebook, Cell 7). Expected value: α_decay ≈ 2–4.

### Comparison with inflationary reheating cutoff

The inflationary spectrum has a cutoff at the reheating scale:

```
f_reh ~ 10⁸ Hz × (T_reh / 10¹⁵ GeV)
```

This cutoff is typically a POWER-LAW decay (related to the equation
of state during reheating), not an exponential.

**The exponential cutoff is a distinctive BOUNCE signature.**
However, it is only detectable if the spectrum is above sensitivity
near f_b — which it is not (due to (m_T/M_Pl)² suppression).

---

## 7. Summary: The Spectrum Shape

### Complete parametric description

```
Ω_GW(f) h² = Ω₀ × S(f/f_b)
```

where:
```
Ω₀ = 1.6 × 10⁻⁵ × (m_T/M_Pl)² × C₀     (overall amplitude)
f_b = 2.6 × 10¹⁰ × (m_T/M_Pl)^{1/2} Hz   (bounce frequency)
```

and the shape function S(x) is:

```
S(x) = { 1                            for x ≪ 1
        { 1/x² × [1 + A sin(2x+φ)]   for x ~ 1
        { exp(-α x)                    for x ≫ 1
```

with α ~ 2–4, A ~ O(1), φ ~ O(1) (numerical constants from the
exact bounce profile).

### One-parameter family

The spectrum is a ONE-PARAMETER FAMILY indexed by m_T (or
equivalently f_b). The shape S(x) is universal — the same for ALL
values of m_T. Changing m_T shifts the spectrum horizontally
(in frequency) and vertically (in amplitude) but does not change
its shape.

### Is the shape distinctive?

**YES — the bounce spectrum has a qualitatively different shape
from inflation:**

- Flat plateau + exponential cutoff (bounce) vs
- Near-flat power law over many decades (inflation)

**NO — the shape is NOT distinctive among bouncing models:**

- All symmetric radiation bounces produce the same qualitative
  shape (flat + exponential cutoff)
- The quantitative differences (exact C₀, α_decay, oscillation
  pattern) are model-dependent but small
- Cannot distinguish PGT bounce from LQC bounce or any other
  radiation bounce if the amplitudes are the same

### The fundamental limitation

The spectrum shape IS distinctive (bounce vs inflation) but the
amplitude is too low to observe. The shape distinguishability is
a theoretical result with no observational consequence.
