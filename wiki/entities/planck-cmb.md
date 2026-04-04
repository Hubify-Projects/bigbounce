---
title: Planck CMB Anomaly Survey
type: entity
tags: [survey, anomaly, cmb, planck]
last_updated: 2026-04-04
sources:
  - project-context/active_pods_and_pipelines.md
  - project-context/post_sweep_followon_plan.md
---

# Planck CMB

**Status:** COMPLETE | **QC:** FAIL

## Summary

Autoencoder anomaly detection on Planck CMB temperature patches. Results dominated by galactic contamination -- all top anomalies cluster at Dec < -84 deg (galactic polar region).

## Numbers

| Metric | Value |
|--------|-------|
| Patches analyzed | 20,000 |
| Anomalies | 200 (1%) |
| Top anomaly location | All at Dec < -84 deg |

## QC Failure

- **Spatial concentration:** All top anomalies within the galactic polar cap
- **Root cause:** No galactic mask applied before anomaly detection
- **Failure mode:** The autoencoder correctly identifies that galactic foreground residuals are "anomalous" relative to the CMB -- but this is a known systematic, not a discovery

## Required Fix

Re-run with:
1. Galactic mask (standard Planck masks: GAL060, GAL070, GAL080)
2. Point source mask (Planck catalog of compact sources)
3. Multipole-by-multipole analysis to separate foreground from CMB anomalies

## Cross-Match with ACT

Planck x ACT cross-match found 15 coincident anomalous patches vs 12.2 expected from random. NOT statistically significant (1.2x random). Neither the Cold Spot nor hemispheric asymmetry was independently confirmed by both experiments.

## Connections

- Cross-matched with [[act-dr6]] (not significant)
- Birefringence measurement attempted via [[birefringence]]
- Included in [[paper-3-anomaly-catalog]] (with caveat)
- QC failure documented in [[survey-anomaly-rates]]
