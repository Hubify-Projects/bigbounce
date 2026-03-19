# 03: SPHEREx Forecast Hardening

## SPHEREx f_NL Capability — Hardened Assessment

### Published Forecasts

The SPHEREx science book (Doré et al. 2014) quotes σ(f_NL) ~ 0.5 (optimistic, multi-tracer at high z). More recent analyses incorporate realistic photo-z performance, tracer selection, and systematics:

- **Optimistic (design goal):** σ(f_NL) = 0.5
- **Realistic (most likely):** σ(f_NL) = 0.8-1.5
- **Conservative (degraded photo-z):** σ(f_NL) = 2.0-3.0

SPHEREx is primarily a PHOTOMETRIC survey. Its f_NL constraint comes from the scale-dependent bias in the galaxy angular power spectrum C_ℓ, not the 3D power spectrum P(k). The photometric redshifts (R ~ 40-130) provide crude radial information but substantially less than a spectroscopic survey.

### Hardened Significance for f_NL = -4.375

| Scenario | σ(f_NL) | Significance | Assessment |
|----------|---------|-------------|-----------|
| Design goal | 0.5 | 8.75σ | **Likely too optimistic** — assumes perfect multi-tracer |
| Realistic | 1.0 | 4.4σ | **Plausible central** — includes moderate photo-z degradation |
| Conservative | 2.0 | 2.2σ | **Plausible floor** — significant photo-z issues |
| Pessimistic | 3.0 | 1.5σ | Not decisive |

### SPHEREx-Specific Fragilities

1. **Photo-z scatter:** The R ~ 40-130 spectral resolution limits redshift accuracy. For high-z galaxies, photo-z scatter σ_z/(1+z) ~ 0.03-0.1 degrades radial mode counting.

2. **Tracer selection:** SPHEREx will identify tracers using infrared colors/spectral features. The bias properties of these tracers have significant uncertainty before launch.

3. **Galactic foreground subtraction:** SPHEREx operates in the infrared where zodiacal light, Galactic dust, and stellar contamination are significant at low spatial frequencies.

### What SPHEREx Can and Cannot Do

**CAN provide a meaningful hint:** At σ = 1.0, measuring f_NL = -4 ± 1 would be a 4σ evidence of negative non-Gaussianity, which is:
- 4× stronger than Planck's current constraint
- The correct sign for the bounce prediction
- Sufficient to motivate MegaMapper-class follow-up

**CANNOT provide a definitive kill:** Even at σ = 1.0, measuring f_NL = 0 ± 1 only excludes -4.375 at 4.4σ. Strong evidence, but not the 5σ gold standard. MegaMapper would still be needed for definitive exclusion.

### SPHEREx Decision Thresholds

| SPHEREx measures | Verdict | Action |
|-----------------|---------|--------|
| f_NL = -4 ± 1 | **STRONGLY_SUPPORTS** | Major evidence for bounce; fast-track MegaMapper |
| -3 < f_NL < -1 | **SUPPORTS** | Positive signal; MegaMapper confirmation needed |
| -1 < f_NL < +1 | **WEAKENS** at ~3-4σ | Tension with bounce; MegaMapper essential for definitive test |
| f_NL > +2 | **SERIOUSLY_WEAKENS** | Wrong sign; bounce in trouble but not killed |
| f_NL = 0 ± 0.5 | **KILLS** at 8.75σ (only if σ truly = 0.5) | Extremely unlikely SPHEREx achieves this |

### Honest Bottom Line for SPHEREx

**Central expectation: SPHEREx at σ(f_NL) ~ 1.0 gives a 4.4σ detection if the bounce is real.** This is strong evidence but not definitive. The main uncertainty is photo-z quality, which won't be known until after launch and commissioning.

SPHEREx is the FIRST REAL TEST. It arrives ~2028. The result will either generate enormous excitement (if f_NL < -2) or create significant tension (if f_NL ≈ 0) with the bounce paradigm.
