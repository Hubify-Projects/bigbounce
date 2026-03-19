# 04: SPHEREx Forecast Refinement

## SPHEREx Mission Parameters

- Launch: ~2025-2026, data: ~2027-2028
- All-sky spectrophotometric survey (0.75-5 μm)
- ~450 million galaxies with spectral resolution R ~ 40-130
- Primary f_NL science: scale-dependent bias from galaxy power spectrum
- Design goal: σ(f_NL^local) ~ 0.5-1.0 (depending on galaxy sample and systematics)

## f_NL Sensitivity Estimates

SPHEREx f_NL forecasts from the literature vary:
- Doré et al. (2014, SPHEREx Science Book): σ(f_NL) ~ 0.5 (optimistic, multi-tracer)
- More recent assessments: σ(f_NL) ~ 0.8-2.0 (depending on photo-z quality and bias modeling)

The key issue: SPHEREx uses PHOTOMETRIC redshifts (R~40-130), not spectroscopic. This limits the radial resolution and degrades the large-scale power spectrum measurement compared to a spectroscopic survey.

## Significance for f_NL = -4.375

| SPHEREx scenario | σ(f_NL) | Significance | Interpretation |
|-----------------|---------|-------------|----------------|
| Optimistic (multi-tracer, best photo-z) | 0.5 | **8.75σ** | Definitive detection |
| Central (single-tracer, good photo-z) | 1.0 | **4.4σ** | Strong evidence |
| Conservative (limited photo-z, systematics) | 1.5 | **2.9σ** | Suggestive hint |
| Pessimistic (severe photo-z degradation) | 3.0 | **1.5σ** | Not decisive |

## SPHEREx Decision Thresholds

If SPHEREx measures f_NL = X ± σ:

| Measurement | Verdict |
|-------------|---------|
| X = -4 ± 1.0 | **STRONGLY_SUPPORTS** bounce (3-5σ from zero, correct sign and magnitude) |
| -6 < X < -2 | **SUPPORTS** bounce (correct sign, within factor 2 of prediction) |
| -2 < X < 0 | **INCONCLUSIVE** (could be null or weak signal) |
| X = 0 ± 1.0 | **WEAKENS** bounce at 2-4σ level (but not definitive — need MegaMapper for kill shot) |
| X > +2 | **WEAKENS** bounce strongly (wrong sign) |

## Can SPHEREx Provide a Meaningful Hint?

**YES, if σ(f_NL) ≤ 1.5.** At the central estimate (σ ~ 1.0, significance 4.4σ), SPHEREx would provide strong evidence either for or against the matter bounce — enough to trigger a major reorientation of the field toward or away from bounce cosmology.

**NO, if σ(f_NL) > 2.5.** At the pessimistic end, SPHEREx cannot distinguish f_NL = -4 from f_NL = 0 at more than 1.5σ.

## Timeline

SPHEREx results relevant to f_NL are expected ~2028-2029. This is the FIRST real test of the matter-bounce prediction. MegaMapper (if funded and built) would follow ~2032-2035 for a definitive test.
