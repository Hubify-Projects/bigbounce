---
title: NEOWISE Infrared Anomaly Survey
type: entity
tags: [survey, anomaly, neowise, infrared, time-domain]
last_updated: 2026-04-04
sources:
  - project-context/active_pods_and_pipelines.md
  - project-context/post_sweep_followon_plan.md
---

# NEOWISE

**Status:** COMPLETE | **QC:** FAIL

## Summary

Anomaly detection on NEOWISE infrared time-domain data. Results dominated by a survey systematic -- all top anomalies cluster at RA ~ 180 deg.

## Numbers

| Metric | Value |
|--------|-------|
| Sources scored | 43,500 |
| Anomalies | 436 (1%) |
| Top anomaly concentration | All at RA ~ 180 deg |

## QC Failure

- **Spatial concentration:** All top anomalies cluster around RA ~ 180 deg
- **Root cause:** Survey systematic (likely scanning pattern artifact or depth variation)
- **Recommendation:** Re-run with spatial detrending or ecliptic-coordinate correction to remove scan-pattern systematics

## Scientific Potential

NEOWISE infrared variability is valuable for:
- AGN identification via W1-W2 color and variability
- Extreme IR-variable QSOs at high redshift (see [[desi-dr1]] finding of 6 QSOs at z > 4 with W2 amplitudes 3-5.5 mag)
- Cross-match with ZTF alerts for multi-wavelength transient identification

## Pending Follow-Up

- Cross-match anomalies with ZTF alerts
- Cross-match with AGN catalogs (Veron-Cetty, Milliquas)
- Check for periodicity in anomalous light curves
- Cross-match with [[erosita-dr1]] (infrared x X-ray for AGN)

## Connections

- Cross-match with [[desi-dr1]] pending
- Cross-match with [[erosita-dr1]] pending (AGN hunting)
- Included in [[paper-3-anomaly-catalog]] (with caveat)
- QC failure documented in [[survey-anomaly-rates]]
