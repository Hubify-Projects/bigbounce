---
title: "f_NL = -35/8 Prediction"
type: concept
tags: [fnl, bounce, prediction, spherex, discriminator]
last_updated: 2026-04-04
sources:
  - project-context/bounce_portfolio_strategy.md
  - project-context/pipeline1_tracer_purification_plan.md
  - project-context/CURRENT_STATUS.md
---

# f_NL = -35/8 Prediction

The decisive discriminator between bounce cosmology and inflation.

## The Number

**f_NL = -35/8 = -4.375**

This is a parameter-free prediction of the matter bounce cosmology. It requires no model tuning, no free parameters, no assumptions beyond the contraction phase being matter-dominated. It is mechanism-independent: it holds for any bounce model where the contracting phase is approximately matter-dominated (matter bounce, certain quintom bounces, asymmetric bounces).

Standard slow-roll inflation predicts f_NL ~ 0.01 (effectively zero). A measurement of f_NL = -4.375 would be a 4+ sigma deviation from inflation and a direct confirmation of bounce cosmology.

## Triple Role

The same number f_NL = -35/8 simultaneously:

1. **Predicts galaxy bispectrum** -- directly measurable by SPHEREx via three-point correlation function of galaxy positions. This is the primary test.
2. **Regulates PBH abundance** -- negative f_NL naturally prevents primordial black hole overproduction (Choudhury+ 2025, EPJC 85:472). Inflationary models with positive f_NL tend to overproduce PBHs, requiring fine-tuning.
3. **Shapes induced GW spectrum** -- encodes non-Gaussian clustering that modifies the gravitational wave spectrum from PBH formation, detectable by LISA and PTAs.

This triple role is unique to matter bounce cosmology.

## Current Constraints

| Source | sigma(f_NL) | Our prediction at... |
|--------|-------------|---------------------|
| Planck bispectrum (bounce template) | 4.76 | 0.1-sigma from measured |
| DESI DR1 SDB alone | 9.05 | 0.5-sigma |
| Planck + DESI combined | 2.94 | 0.9-sigma from zero |
| With anomaly tracer purification | ~3.3 (forecast) | ~1.3-sigma |
| SPHEREx (2028) | ~0.7-1.0 | 4-6 sigma |

## Improvement from Anomaly Catalogs

- DESI anomaly tracers: 6.1% improvement in sigma(f_NL) -- clears 5% publishable threshold
- DESI + SDSS combined: 16.4% improvement
- Fisher forecast corrected: sigma(f_NL) = 8.98 standard, 8.12 multi-tracer
- SPHEREx detection forecast with improvement: 4.38-sigma

## NANOGrav Consistency

The induced GW spectrum from matter bounce has universal f^2 infrared scaling, giving spectral index gamma = 3.0. NANOGrav 15yr measures gamma = 3.2 +/- 0.6. The prediction is within 0.33-sigma (Papanikolaou 2025, arXiv:2504.11641).

## Connections

- Paper: [[paper-2-fnl-forecast]]
- Tracer improvement: [[pipeline-1-tracer-purification]]
- Portfolio context: [[bounce-portfolio]]
- Data: [[desi-dr1]], [[sdss-dr18]]
- Discrimination: [[bounce-vs-inflation]]
