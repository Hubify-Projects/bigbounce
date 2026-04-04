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
| Anomalies (top 1%) | 9,303 |
| Runtime | 8 seconds |
| Novelty fraction (not in SIMBAD) | 73% |

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
