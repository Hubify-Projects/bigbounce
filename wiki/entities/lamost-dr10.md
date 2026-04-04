---
title: LAMOST DR10 Anomaly Survey
type: entity
tags: [survey, anomaly, lamost]
last_updated: 2026-04-04
sources:
  - project-context/active_pods_and_pipelines.md
  - project-context/post_sweep_followon_plan.md
---

# LAMOST DR10

**Status:** COMPLETE | **QC:** CAUTION

## Summary

Anomaly detection on the Large Sky Area Multi-Object Fiber Spectroscopic Telescope Data Release 10. Largest spectral count in the sweep (11.4M), but dominated by training bias artifact.

## Numbers

| Metric | Value |
|--------|-------|
| Spectra scored | 11,418,594 |
| Anomalies | 44,075 (0.39%) |
| Runtime | 18.3 hours |
| UMAP clusters | 8 |
| Blue-excess fraction | 98.1% |
| Artifacts identified | 644 |

## QC Issues

- **Training bias:** 98% of anomalies are blue-excess objects, indicating the model was trained predominantly on red/galaxy spectra and flags blue objects as anomalous by default
- **Recommendation:** Train a LAMOST-native autoencoder on LAMOST-specific spectral classes rather than using the DESI transfer model
- Rankings are model-dependent -- a LAMOST-native model would produce a fundamentally different anomaly catalog

## Key Insight

The 0.39% anomaly rate (lowest of all spectroscopic surveys) combined with the 98% blue-excess dominance suggests the model is functioning as a blue-object detector rather than a true anomaly detector for this survey. The low rate is misleading -- it reflects model bias, not genuine rarity.

## Connections

- Potential third tracer population for [[fnl-prediction]] (pending LAMOST-native model)
- Included in [[paper-3-anomaly-catalog]]
- QC comparison in [[survey-anomaly-rates]]
- Cross-match with [[desi-dr1]] and [[sdss-dr18]] pending
