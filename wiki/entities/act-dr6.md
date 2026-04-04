---
title: ACT DR6 CMB Anomaly Survey
type: entity
tags: [survey, anomaly, cmb, act, birefringence]
last_updated: 2026-04-04
sources:
  - project-context/active_pods_and_pipelines.md
  - project-context/post_sweep_followon_plan.md
---

# ACT DR6

**Status:** COMPLETE | **QC:** FAIL

## Summary

Autoencoder anomaly detection on Atacama Cosmology Telescope Data Release 6 CMB patches. Undertrained model with extremely high validation loss.

## Numbers

| Metric | Value |
|--------|-------|
| Patches analyzed | 20,000 |
| Anomalies | 200 (1%) |
| Validation loss | 22,420 |
| Runtime | ~5 min (+ 20 min download) |

## QC Failure

- **Training quality:** val_loss = 22,420 indicates the model never converged
- **Root cause:** Insufficient training epochs and/or inappropriate architecture for ACT data format
- **Recommendation:** Train longer with learning rate scheduling, or use a different architecture suited to ACT map properties

## Birefringence Measurement

ACT IQU polarization data (5.3 GB) was used for a birefringence measurement:
- Result: beta = 17.4 deg +/- 12.1 deg
- Status: Systematic-dominated (foreground contamination)
- The simple FFT estimator is insufficient for sub-degree birefringence
- Needs NaMaster or PolSpice for proper pseudo-Cl estimation with mode-coupling correction

See [[birefringence]] for full analysis.

## Connections

- Cross-matched with [[planck-cmb]] (15 matches, not significant)
- Birefringence pipeline deployed here -- see [[birefringence]]
- Included in [[paper-3-anomaly-catalog]] (with caveat)
- QC failure documented in [[survey-anomaly-rates]]
