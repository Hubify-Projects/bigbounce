---
title: SDSS DR18 Anomaly Survey
type: entity
tags: [survey, anomaly, sdss]
last_updated: 2026-04-04
sources:
  - project-context/active_pods_and_pipelines.md
  - project-context/post_sweep_followon_plan.md
---

# SDSS DR18

**Status:** COMPLETE | **QC:** CAUTION

## Summary

Transfer-learning anomaly detection on SDSS Data Release 18 using the DESI-trained autoencoder. Second-largest spectroscopic anomaly catalog in the program.

## Numbers

| Metric | Value |
|--------|-------|
| Spectra scored | 2,304,830 |
| Anomalies | 77,905 (3.4%) |
| Runtime | 2.8 hours |
| Backup size | 1.8 GB |
| UMAP clusters | 14 |
| High-z candidates | 4,117 |
| QSO candidates | 585 |

## QC Issues

- **Score explosion:** Anomaly scores reach up to 10^11 (far beyond physical range)
- **Domain shift:** DESI-trained model applied to SDSS spectra without retraining
- **Recommendation:** Retrain autoencoder on SDSS-native spectra, or apply score normalization

The 3.4% anomaly rate (vs 0.87% for DESI) likely reflects domain shift rather than a genuinely higher anomaly population.

## Cross-Match Results

- SDSS x DESI: 3 matches found
  - z ~ 5.27 QSO: known object (SDSS J144350.66+362315.1), validates pipeline
  - Anomalous star (score=49.5): TIC 374313355, time-variable, best follow-up target
  - z ~ 0.86 mismatch: not in NED/SIMBAD, classification discrepancy (SDSS: QSO z=0.860, DESI: GALAXY z=0.823), possible BAL QSO

## Connections

- Transfer-learned from [[desi-dr1]] model
- Cross-matched with [[desi-dr1]] (3 matches)
- Combined with DESI for 16.4% f_NL improvement -- see [[fnl-prediction]]
- Included in [[paper-3-anomaly-catalog]]
- QC issues documented in [[survey-anomaly-rates]]
