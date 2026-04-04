---
title: "Pipeline 1: Tracer Purification for f_NL"
type: entity
tags: [pipeline, fnl, tracer, desi, highz]
last_updated: 2026-04-04
sources:
  - project-context/pipeline1_tracer_purification_plan.md
  - project-context/post_sweep_followon_plan.md
---

# Pipeline 1: Tracer Purification for f_NL

**Priority:** HIGHEST AI PIPELINE | **Status:** Step 1 DONE, Steps 2-6 NOT STARTED

## Summary

The closed loop from anomaly detection to f_NL measurement improvement. Uses AI-discovered anomalous spectra to find missed high-z QSO tracers, improving the scale-dependent bias signal that tests f_NL = -35/8.

## The Science

Scale-dependent bias: Delta_b(k) = (b1 - 1) * f_NL * delta_crit / (alpha(k) * k^2). Signal strongest for highly biased tracers (QSOs at z > 2) at ultra-large scales. Better tracers = better bias = tighter sigma(f_NL).

## Pipeline Steps

| Step | Description | Status |
|------|-------------|--------|
| 1. Catalog | Pull and catalog H200 anomaly results | DONE (195K anomalies) |
| 2. Cross-match | Match anomalies against Legacy Survey + unWISE | NOT STARTED |
| 3. Classify | Separate high-z QSOs from AGN/stars/artifacts | NOT STARTED |
| 4. Validate bias | Measure angular auto-correlation w(theta) | NOT STARTED |
| 5. Re-measure sigma(f_NL) | Multi-tracer recomputation | NOT STARTED |
| 6. Paper | Integrate into Paper 3 | Draft exists |

## Current Constraint Status

| Configuration | sigma(f_NL) |
|--------------|-------------|
| Planck bispectrum alone | 4.76 (bounce template) |
| DESI DR1 SDB alone | 9.05 |
| Planck + DESI combined | 2.94 (best current) |
| With tracer purification (forecast) | ~3.3 |
| SPHEREx (2028) | ~0.7-2 |

## Measured Improvements So Far

- DESI anomaly tracers: 6.1% improvement in sigma(f_NL)
- DESI + SDSS combined: 16.4% improvement
- SPHEREx detection forecast: 4.38-sigma

These are statistical estimates. Steps 2-6 (the novel science) would validate whether the improvement holds with actual bias measurements.

## What Makes This Novel

1. First autoencoder anomaly search at full DESI DR1 scale (~18M spectra)
2. AI-discovered tracers fed back into a cosmological measurement (closed loop)
3. Direct connection to f_NL = -35/8 prediction (not generic improvement)
4. Anomaly catalog is a standalone data product regardless of f_NL outcome

## Connections

- Input from [[pipeline-b-desi-anomaly]] and [[desi-dr1]]
- Science target: [[fnl-prediction]]
- Paper output: [[paper-3-anomaly-catalog]]
- Methodology: [[anomaly-detection-methodology]]
