# Detector Forecast: PGT Bounce GW Spectrum

**Date:** 2026-03-16

---

## 1. Detector Sensitivity Curves

### Current and planned GW detectors

| Detector | Band (Hz) | Peak Ω_GW h² sensitivity | Status |
|----------|----------|------------------------|--------|
| LIGO O5 | 10–5000 | ~10⁻⁹ | Operating |
| Virgo O5 | 10–5000 | ~10⁻⁸ | Operating |
| KAGRA | 10–5000 | ~10⁻⁸ | Operating |
| Einstein Telescope | 1–10⁴ | ~10⁻¹³ | Planned (2030s) |
| Cosmic Explorer | 5–10⁴ | ~10⁻¹³ | Planned (2030s) |
| LISA | 10⁻⁴–10⁻¹ | ~10⁻¹³ | Planned (2037) |
| DECIGO | 10⁻²–10² | ~10⁻¹⁶ | Proposed |
| BBO | 10⁻²–10² | ~10⁻¹⁷ | Conceptual |
| NANOGrav/IPTA | 10⁻⁹–10⁻⁷ | ~10⁻¹⁰ | Operating |
| SKA-PTA | 10⁻⁹–10⁻⁷ | ~10⁻¹² | Planned (2030s) |

---

## 2. PGT Bounce Spectrum Overlay

### Peak amplitude

```
Ω_GW,peak h² = 1.6 × 10⁻⁵ × (m_T/M_Pl)² × C₀
```

Taking C₀ ~ 0.3 (typical for radiation bounce):

```
Ω_GW,peak h² ≈ 5 × 10⁻⁶ × (m_T/M_Pl)²
```

### Overlay table

| m_T (GeV) | f_b (Hz) | Ω_peak h² | Best detector | Sensitivity | Gap |
|-----------|---------|----------|--------------|------------|-----|
| 10⁹ | 2.4 × 10⁵ | 3.4 × 10⁻²⁶ | None (above band) | — | — |
| 10⁷ | 2.4 × 10⁴ | 3.4 × 10⁻³⁰ | ET/CE | 10⁻¹³ | 10¹⁷ |
| 10⁵ | 2.4 × 10³ | 3.4 × 10⁻³⁴ | ET/CE | 10⁻¹³ | 10²¹ |
| 10³ | 240 | 3.4 × 10⁻³⁸ | ET/CE | 10⁻¹³ | 10²⁵ |
| 10 | 24 | 3.4 × 10⁻⁴² | ET/CE | 10⁻¹³ | 10²⁹ |
| 10⁻¹ | 2.4 | 3.4 × 10⁻⁴⁶ | ET/CE | 10⁻¹³ | 10³³ |
| 10⁻³ | 0.24 | 3.4 × 10⁻⁵⁰ | DECIGO | 10⁻¹⁶ | 10³⁴ |
| 10⁻⁵ | 0.024 | 3.4 × 10⁻⁵⁴ | DECIGO | 10⁻¹⁶ | 10³⁸ |
| 10⁻⁷ | 2.4 × 10⁻³ | 3.4 × 10⁻⁵⁸ | LISA | 10⁻¹³ | 10⁴⁵ |
| 10⁻⁹ | 2.4 × 10⁻⁴ | 3.4 × 10⁻⁶² | LISA | 10⁻¹³ | 10⁴⁹ |
| 10⁻¹⁵ | 2.4 × 10⁻⁷ | 3.4 × 10⁻⁷⁴ | SKA-PTA | 10⁻¹² | 10⁶² |

### Minimum gap

The smallest gap occurs at the highest m_T that still falls within
a detector band. For ET/CE (f range 1–10⁴ Hz):

```
m_T,max ~ 10⁷ GeV  →  f_b ~ 2.4 × 10⁴ Hz  →  Ω_peak ~ 3 × 10⁻³⁰
Gap to ET: 10⁻³⁰ / 10⁻¹³ = 10⁻¹⁷  →  GAP = 10¹⁷
```

**The minimum gap between the PGT bounce signal and ANY detector
is 17 orders of magnitude.** This occurs at the upper edge of the
ET band (f ~ 10⁴ Hz, m_T ~ 10⁷ GeV).

---

## 3. What m_T Would Be Needed for Detection?

### Requirement

```
Ω_peak h² ≥ Ω_sensitivity h²
5 × 10⁻⁶ × (m_T/M_Pl)² ≥ Ω_sens
m_T ≥ M_Pl × √(Ω_sens / 5 × 10⁻⁶)
```

| Detector | Ω_sens h² | Required m_T (GeV) | Corresponding f_b (Hz) | In band? |
|----------|----------|-------------------|----------------------|:--------:|
| LIGO O5 | 10⁻⁹ | 5.5 × 10¹⁶ | 5.5 × 10⁹ | **NO** |
| ET | 10⁻¹³ | 5.5 × 10¹⁴ | 5.5 × 10⁸ | **NO** |
| LISA | 10⁻¹³ | 5.5 × 10¹⁴ | 5.5 × 10⁸ | **NO** |
| DECIGO | 10⁻¹⁶ | 1.7 × 10¹³ | 1.0 × 10⁸ | **NO** |
| BBO | 10⁻¹⁷ | 5.5 × 10¹² | 5.5 × 10⁷ | **NO** |

For EVERY detector: the required m_T places f_b at ~10⁸–10¹⁰ Hz,
far ABOVE the detector band.

### The universal bound

The condition for detection:

```
m_T ≥ M_Pl × √(Ω_sens / 5 × 10⁻⁶)
```

The corresponding frequency:

```
f_b = 2.6 × 10¹⁰ × (m_T/M_Pl)^{1/2}
    ≥ 2.6 × 10¹⁰ × (Ω_sens / 5 × 10⁻⁶)^{1/4}
```

For the BEST conceivable detector (BBO, Ω_sens ~ 10⁻¹⁷):

```
f_b ≥ 2.6 × 10¹⁰ × (10⁻¹⁷ / 5 × 10⁻⁶)^{1/4}
    = 2.6 × 10¹⁰ × (2 × 10⁻¹²)^{1/4}
    = 2.6 × 10¹⁰ × 1.2 × 10⁻³
    = 3.1 × 10⁷ Hz
```

**Even with the most optimistic detector concept (BBO), the
detectable bounce signal is at f > 30 MHz — far above the
detector band (0.01–100 Hz).**

---

## 4. The Detection Impossibility Theorem

### Statement

> For any GW detector operating in a band [f_min, f_max] with
> energy density sensitivity Ω_sens h², the vacuum-amplification
> GW background from a symmetric bounce at critical density
> ρ_crit satisfies:
>
> If Ω_GW(f_b) h² ≥ Ω_sens h², then f_b ≥ f_det,min
>
> where f_det,min ~ 10⁷ Hz × (Ω_sens / 10⁻¹⁷)^{1/4}.
>
> Since f_det,min ≫ f_max for ALL planned and proposed GW detectors,
> the vacuum-amplification bounce signal is UNDETECTABLE.

### Proof sketch

```
Ω_peak ~ (H_b/M_Pl)² ~ (ρ_crit/M_Pl⁴) ~ (f_b/f_Pl)⁴

Detection requires: Ω_peak ≥ Ω_sens
                    (f_b/f_Pl)⁴ ≥ Ω_sens/10⁻⁵
                    f_b ≥ f_Pl × (Ω_sens/10⁻⁵)^{1/4}
                        ~ 10¹⁰ × (10⁻¹³/10⁻⁵)^{1/4}
                        ~ 10¹⁰ × 10⁻² = 10⁸ Hz
```

All GW detectors operate below 10⁴ Hz. The minimum detectable f_b
is ~10⁷–10⁸ Hz. **The gap is at least 10³ in frequency.**

### Generality

This result applies to ANY bouncing cosmology (PGT, EC, LQC,
ekpyrotic, etc.) where the GW production mechanism is vacuum
amplification through the bounce. It does NOT apply to:

- Phase transitions (energy comes from latent heat, not vacuum)
- Preheating/parametric resonance (energy comes from inflaton decay)
- Cosmic strings (topological defect, continuous source)

These non-vacuum sources can produce detectable signals because
their amplitude is NOT tied to (H/M_Pl)².

---

## 5. Could Non-Vacuum Sources Help?

### Possibility 1: Torsion oscillation after bounce

After the bounce, the propagating torsion mode oscillates and
decays. If this decay is violent (parametric resonance), it could
produce GWs beyond the vacuum level.

Estimate: The torsion energy density at the bounce is:
```
ρ_torsion ~ m_T² τ² ~ ρ_crit (at most)
```

The GW production from torsion oscillation:
```
ρ_GW ~ (G ρ_torsion)² / m_T ~ (ρ_crit/M_Pl²)² / m_T
     = m_T⁴ M_Pl⁴ / (M_Pl⁴ × m_T) = m_T³
```

Wait — more carefully. The GW production rate from a coherently
oscillating scalar of mass m and amplitude φ₀:

```
dρ_GW/dt ~ (m⁶ φ₀²) / M_Pl²
```

For the torsion: m = m_T, φ₀ ~ M_Pl (maximum amplitude at bounce):

```
dρ_GW/dt ~ m_T⁶ M_Pl² / M_Pl² = m_T⁶
```

Over a Hubble time H⁻¹ ~ 1/m_T (at the bounce):

```
ρ_GW ~ m_T⁶ / m_T = m_T⁵
```

The fraction:
```
ε = ρ_GW / ρ_crit ~ m_T⁵ / (m_T² M_Pl²) = (m_T/M_Pl)³
```

This is EVEN MORE suppressed than the vacuum amplification
((m_T/M_Pl)² → (m_T/M_Pl)³).

**Torsion oscillation does not help.**

### Possibility 2: Pre-bounce contraction amplification

If the contraction phase has a matter-dominated epoch (w = 0),
tensor modes grow during contraction:

```
h_k ∝ a⁻¹ ~ t^{-2/3}    (growing in contraction as a shrinks)
```

This could amplify the tensor spectrum at large scales. However:

1. The amplification is model-dependent (requires specifying the
   contraction history)
2. The amplified modes are at frequencies set by the contraction
   horizon, not the bounce scale
3. This is a PRE-BOUNCE effect, not a bounce signature

**Outside the scope of bounce-specific predictions.**

### Possibility 3: Particle production at the bounce scale

Parametric resonance during the bounce could enhance particle
production beyond the single-scattering (Bogoliubov) estimate.
However, the bounce is ~ 1 oscillation period long (t_bounce ~ 1/m_T,
oscillation period ~ 1/m_T), so there is no time for resonant
buildup.

**No parametric enhancement available.**

---

## 6. Summary

### Detectability assessment

| Detector | In-band f_b possible? | In-band amplitude? | Detectable? |
|----------|:--------------------:|:------------------:|:-----------:|
| LIGO O5 | YES (m_T ~ 10–10⁷ GeV) | NO (gap 10¹⁷+) | **NO** |
| ET/CE | YES (m_T ~ 0.1–10⁷ GeV) | NO (gap 10¹⁷+) | **NO** |
| LISA | YES (m_T ~ 10⁻⁹–10⁻⁵ GeV) | NO (gap 10³⁸+) | **NO** |
| DECIGO | YES (m_T ~ 10⁻⁵–10 GeV) | NO (gap 10²⁹+) | **NO** |
| BBO | YES (m_T ~ 10⁻⁵–10 GeV) | NO (gap 10²⁶+) | **NO** |
| NANOGrav | YES (m_T ~ 10⁻¹⁹–10⁻¹⁵ GeV) | NO (gap 10⁵⁰+) | **NO** |

### The minimum gap

**17 orders of magnitude** (ET at f ~ 10⁴ Hz, m_T ~ 10⁷ GeV).

This is the closest any detector can come to the PGT bounce signal.
It corresponds to the UPPER edge of the ET band with the LARGEST
viable m_T.

### Final assessment

The PGT bounce vacuum-amplification GW spectrum is:
- **Theoretically well-defined** (one-parameter family, universal shape)
- **Qualitatively distinctive** (flat + exponential cutoff ≠ inflation)
- **Quantitatively undetectable** (minimum 10¹⁷ gap to best detector)
- **Universally undetectable** (not specific to PGT; any vacuum-
  amplification bounce faces the same (H/M_Pl)² suppression)
