---
title: eROSITA DR1 X-ray Anomaly Survey
type: entity
tags: [survey, anomaly, erosita, xray]
last_updated: 2026-04-04
sources:
  - project-context/active_pods_and_pipelines.md
---

# eROSITA DR1

**Status:** COMPLETE | **QC:** PASS

## Summary

X-ray anomaly detection on the eROSITA Data Release 1 catalog. Fast execution (8 seconds) due to tabular rather than spectral data. High novelty fraction.

## Numbers

| Metric | Value |
|--------|-------|
| Sources scored | 930,203 |
| Anomalies (BigAE top-cut) | 298 (0.03%, Paper 3 Table 1 canonical) |
| Runtime | ~7 minutes (A100 80 GB, full train+score, fire #26) |
| Novelty fraction (not in SIMBAD) | 68% |
| HuggingFace block | `bamfai/bigbounce-anomaly-catalog::blocks/erosita_dr1/erosita_dr1_anomalies.parquet` (uploaded fire #26) |

> **Historical note:** An earlier 2026-04-02 scan used a 1% cut returning 9,303 anomalies. The canonical Paper 3 Table 1 figure is 298 BigAE top-cut (score ≥ 3.412). The 1% figure was a placeholder before the top-cut policy landed.

## QC Assessment

QC: PASS. No score explosions, no spatial concentration artifacts, reasonable anomaly distribution. The 73% novelty fraction is expected for X-ray sources, many of which are not individually cataloged in optical databases.

## Scientific Value

X-ray anomalies complement optical surveys by tracing:
- Active galactic nuclei (AGN) in unusual states
- X-ray binary systems
- Hot gas in galaxy clusters
- Transient phenomena (tidal disruption events, X-ray flashes)

Cross-matching eROSITA anomalies with optical anomalies from [[desi-dr1]] and [[sdss-dr18]] would identify multi-wavelength anomalous objects -- the highest-priority follow-up targets.

## Connections

- Cross-match with [[desi-dr1]] pending (optical x X-ray)
- Cross-match with [[neowise]] pending (X-ray x infrared -- AGN hunting)
- Included in [[paper-3-anomaly-catalog]]
- Comparison in [[survey-anomaly-rates]]
