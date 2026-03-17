# Model Comparison: PGT Bounce vs Alternative GW Sources

**Date:** 2026-03-16

---

## 1. Comparison Framework

We compare the PGT bounce GW spectrum against four alternative
sources of a stochastic gravitational wave background (SGWB):

1. Slow-roll inflation
2. LQC bounce
3. Generic symmetric radiation bounce
4. First-order phase transitions

The comparison uses three criteria:
- **Amplitude**: Can the signal be detected?
- **Shape**: Can the spectrum be distinguished from alternatives?
- **Frequency range**: Does the signal fall in a detector band?

---

## 2. Slow-Roll Inflation

### Spectrum

```
Ω_GW^{inf}(f) h² ≈ 1.5 × 10⁻¹⁵ × r × (f/f_*)^{n_T} × T²(f)
```

where:
- r: tensor-to-scalar ratio (0 < r < 0.03 current bound)
- n_T = -r/8: consistency relation (red tilt)
- f_*: CMB pivot frequency ~ 7.7 × 10⁻¹⁷ Hz
- T²(f): transfer function (≈ 0.39 for f > f_eq ~ 10⁻¹⁷ Hz)

For r = 0.01:
```
Ω_GW^{inf} h² ≈ 6 × 10⁻¹⁸    (flat, f > f_eq)
```

### Comparison with PGT bounce

| Property | Inflation (r=0.01) | PGT bounce |
|----------|-------------------|-----------|
| Amplitude | 6 × 10⁻¹⁸ | 10⁻⁵ × (m_T/M_Pl)² |
| Equal when | — | m_T ~ 6 × 10¹² GeV |
| Shape | Near-flat, n_T = -0.00125 | Flat + exponential cutoff |
| f_b at equal amp. | — | ~2 × 10⁷ Hz |
| Detectable? | DECIGO maybe | Neither |

The PGT bounce matches the inflationary amplitude when
m_T ~ 10¹² GeV, but at that mass f_b ~ 10⁷ Hz — above all
detectors. At lower m_T (in-band), the bounce amplitude is
much smaller than even the inflationary background.

### Shape distinguishability

If both were detectable at the SAME frequency:

```
Bounce: Ω ∝ const. for f < f_b, then exp(-f/f_b)
Inflation: Ω ∝ f^{n_T} ≈ const. (very slight red tilt)
```

Below f_b, both look flat to within 0.1% (the inflationary tilt
n_T ~ -10⁻³ is unmeasurable). The ONLY distinguishing feature
is the exponential cutoff above f_b — but this requires measuring
the spectrum both below AND above f_b, which is impossible if the
amplitude is undetectable.

**Verdict: INDISTINGUISHABLE in practice** (both below sensitivity).

---

## 3. LQC Bounce

### Spectrum

LQC has ρ_crit ≈ 0.41 ρ_Pl, giving:

```
Ω_GW^{LQC}(f) h² ≈ 10⁻⁵ × 0.41 × |β^{LQC}(f/f_b^{LQC})|²
                   ≈ 4 × 10⁻⁶ × S_LQC(f/f_b^{LQC})
```

with f_b^{LQC} ~ 10⁸–10¹⁰ Hz (depending on quantum ambiguities).

### Shape differences

LQC includes quantum-geometry corrections:

1. **Holonomy corrections**: modify the effective potential at the
   bounce, changing the oscillation pattern near k_b.

2. **Inverse-volume corrections**: add a scale-dependent term
   that can modify the low-k plateau (potentially giving a slight
   blue tilt n_T > 0 at very low k).

3. **Quantum bounce asymmetry**: in some LQC models, the bounce
   is not perfectly symmetric, modifying the transfer function.

### Comparison

| Property | PGT bounce | LQC bounce |
|----------|-----------|-----------|
| ρ_crit | m_T² M_Pl² (tunable) | 0.41 ρ_Pl (fixed) |
| f_b | Tunable | ~10⁸–10¹⁰ Hz |
| Peak Ω h² | 10⁻⁵(m_T/M_Pl)² | ~4 × 10⁻⁶ |
| Low-f tilt | n_T = 0 (flat) | n_T ~ 0 or slightly blue |
| Oscillation pattern | Classical (smooth) | Quantum-modified |
| Cutoff shape | exp(-αf/f_b) | Similar + quantum wiggles |

### Can they be distinguished?

**If both had detectable amplitudes at the same frequency:**

The oscillation pattern near f_b would differ. LQC has quantum-
geometry modifications (holonomy parameter μ̄ enters the potential).
The PGT bounce has a classical potential with no quantum corrections.

In principle: the near-f_b oscillation pattern distinguishes them.

**In practice:** Neither is detectable. LQC has f_b too high for
detectors. PGT can have f_b in-band but amplitude too low.

**Verdict: Distinguishable in principle, undetectable in practice.**

---

## 4. Generic Symmetric Radiation Bounce

### The universality problem

ANY symmetric radiation bounce (regardless of the microscopic
mechanism) produces a GW spectrum with the same qualitative shape:

```
Ω_GW(f) h² = A × S(f/f_b)
```

where S(x) is a universal shape function (flat plateau below f_b,
exponential cutoff above f_b, oscillations near f_b).

The ONLY things that distinguish different bounce models:

1. **Amplitude A**: Proportional to ρ_crit/M_Pl⁴, the bounce
   energy scale relative to the Planck scale.

2. **Frequency f_b**: Set by ρ_crit and the expansion history.

3. **Oscillation fine structure**: The exact pattern of oscillations
   near f_b depends on the bounce profile a(t), which differs
   between models.

4. **Low-k behavior**: Deviations from exact flatness at f ≪ f_b
   depend on the pre-bounce contraction history.

### Can PGT be distinguished from a generic bounce?

At the level of the smooth spectrum (plateau + cutoff): **NO.**
All radiation bounces at the same ρ_crit give the same smooth
spectrum.

At the level of oscillation fine structure: **YES, in principle.**
The PGT bounce has a specific a(t) = a_b(1+4α²t²)^{1/4} which
gives specific oscillation positions and amplitudes. A different
bounce model (e.g., Gaussian bounce a = a_b exp(α²t²/2)) gives
different oscillations.

But: the oscillation fine structure requires measuring the spectrum
with relative precision ΔΩ/Ω ~ 10% at f ~ f_b. This requires
the smooth spectrum to be above detector sensitivity in the first
place — which it is not.

**Verdict: The PGT bounce is NOT distinguishable from a generic
radiation bounce at the same scale.**

---

## 5. First-Order Phase Transitions

### Spectrum

A first-order phase transition at temperature T_* produces:

```
Ω_GW^{PT}(f) h² ~ 10⁻⁵ × κ² × (α/(1+α))² × (H_*/β)² × S_PT(f/f_*)
```

where:
- κ: efficiency of energy conversion to kinetic energy
- α: strength parameter (latent heat / radiation energy)
- β: inverse duration of the transition
- f_*: characteristic frequency ~ β × (T_*/T₀)

The shape S_PT is a broken power law:
```
S_PT(x) ~ x³    for x ≪ 1   (causal growth)
S_PT(x) ~ x⁻¹   for x ≫ 1   (power-law decay)
```

### Comparison

| Property | PGT bounce | Phase transition |
|----------|-----------|-----------------|
| Low-f slope | n_T = 0 (flat) | n_T = 3 (causal) |
| High-f slope | Exponential cutoff | Power-law decay (f⁻¹) |
| Peak shape | Broad plateau | Sharp peak |
| Amplitude | (m_T/M_Pl)² × 10⁻⁵ | Up to ~10⁻⁸ |
| f_peak | f_b (tunable) | f_* (depends on T_*) |

### Shape distinguishability

**The bounce and phase-transition spectra are QUALITATIVELY
DIFFERENT:**

- Bounce: FLAT below f_b, exponential above. No peak.
- Phase transition: RISES as f³ below f_*, FALLS as f⁻¹ above f_*.
  Has a sharp peak.

This is the MOST distinctive shape comparison. The low-frequency
behavior alone separates them: flat (bounce) vs f³ (phase
transition).

**But again: the bounce amplitude is undetectable.** A phase
transition with strong parameters (large α, small β) can produce
Ω ~ 10⁻⁸ in the LISA band — genuinely detectable. The PGT bounce
at LISA frequencies gives Ω ~ 10⁻⁵³.

**Verdict: Qualitatively distinguishable shapes, but the bounce
signal is undetectable.**

---

## 6. Summary Comparison Table

| Source | Peak Ω h² | f_peak | Low-f slope | High-f behavior | Detectable? |
|--------|----------|--------|-------------|----------------|:-----------:|
| PGT bounce (m_T=10⁻⁵) | 10⁻⁵³ | 0.02 Hz | n=0 (flat) | exp cutoff | **NO** |
| PGT bounce (m_T=10³) | 10⁻³⁷ | 240 Hz | n=0 | exp cutoff | **NO** |
| PGT bounce (m_T=10⁷) | 10⁻²⁹ | 2.4×10⁴ Hz | n=0 | exp cutoff | **NO** |
| Inflation (r=0.01) | 6×10⁻¹⁸ | flat | n=-0.001 | extends to ~10⁸ Hz | DECIGO maybe |
| LQC bounce | 4×10⁻⁶ | ~10⁹ Hz | n~0 | exp cutoff | **NO** (wrong f) |
| Phase transition | up to 10⁻⁸ | LISA/LIGO | n=3 | f⁻¹ | **YES** |
| Cosmic strings | ~10⁻⁸ | broad | n=0 | flat | **YES** |

### The landscape of SGWB detectability

The PGT bounce spectrum sits in the BOTTOM of the amplitude range
for EVERY detector band. It is below ALL other predicted SGWB
sources by many orders of magnitude.

---

## 7. The Fundamental Tradeoff

### Why the bounce spectrum is always below sensitivity

The bounce amplitude scales as:
```
Ω_peak ~ (m_T/M_Pl)² ~ (ρ_crit/M_Pl⁴)
```

The bounce frequency scales as:
```
f_b ~ (m_T/M_Pl)^{1/2} ~ (ρ_crit/M_Pl⁴)^{1/4}
```

Eliminating m_T:
```
Ω_peak ~ f_b⁴ / (M_Pl⁴ × ρ_radiation⁴ / M_Pl⁴)
       ~ (f_b / f_Pl)⁴     [up to numerical factors]
```

where f_Pl ~ 10¹⁰ Hz × (M_Pl/M_Pl)^{1/2} ~ 10¹⁰ Hz is the
Planck bounce frequency.

**The amplitude goes as the FOURTH power of the frequency ratio.**

To bring f_b from f_Pl ~ 10¹⁰ Hz down to LISA frequencies
(f ~ 10⁻³ Hz) requires a factor of 10⁻¹³ in frequency,
which gives a factor of 10⁻⁵² in amplitude.

**This is the same scale-separation barrier from Branches H–K,
now manifesting in the amplitude-frequency tradeoff of the GW
spectrum.** Lowering the bounce scale to observable frequencies
necessarily lowers the amplitude below sensitivity.

### Is this specific to torsion?

**NO.** This tradeoff applies to ANY bouncing cosmology where the
GW spectrum comes from vacuum fluctuation amplification:

```
Ω_peak ~ (H_bounce/M_Pl)² ~ (ρ_crit/M_Pl⁴) ~ (f_b/f_Pl)⁴
```

It applies to LQC, ekpyrotic, matter bounce, or any other bounce
mechanism. It is a CONSEQUENCE OF GENERAL RELATIVITY: the
graviton production efficiency is always (H/M_Pl)², where H is
the expansion rate at the production epoch.

The only way to beat this tradeoff:
1. Have a source beyond vacuum amplification (e.g., parametric
   resonance, preheating, phase transitions — but these are
   post-bounce processes, not bounce-specific)
2. Have a pre-bounce contraction that amplifies modes coherently
   (but this requires a specific contraction model, not just the
   bounce)

**The vacuum amplification ceiling is universal.**

---

## 8. Verdict on Model Distinguishability

| Comparison | Distinguishable in principle? | Distinguishable in practice? |
|-----------|:---------------------------:|:---------------------------:|
| PGT bounce vs inflation | YES (shape) | **NO** (amplitude) |
| PGT bounce vs LQC | YES (oscillations) | **NO** (amplitude) |
| PGT bounce vs generic bounce | MARGINALLY (oscillations) | **NO** (amplitude) |
| PGT bounce vs phase transition | YES (low-f slope) | **NO** (amplitude) |

**The PGT bounce spectrum has distinctive features but is
undetectable by any planned or conceivable GW detector.**
