---
title: Survey Anomaly Rates Comparison
type: comparison
tags: [survey, anomaly, qc, comparison]
last_updated: 2026-04-04
sources:
  - project-context/active_pods_and_pipelines.md
  - project-context/post_sweep_followon_plan.md
---

# Survey Anomaly Rates Comparison

Side-by-side comparison of all 8 surveys in the multi-survey anomaly sweep.

## Summary Table

| Survey | Sources | Anomalies | Rate | QC | Key Issue |
|--------|---------|-----------|------|----|----|
| [[desi-dr1]] | 22,500,000 | 195,829 | 0.87% | PASS | -- |
| [[sdss-dr18]] | 2,304,830 | 77,905 | 3.4% | CAUTION | Score explosion (10^11), domain shift |
| [[lamost-dr10]] | 11,418,594 | 44,075 | 0.39% | CAUTION | 98% blue-excess (training bias) |
| [[erosita-dr1]] | 930,203 | 298 | 0.03% | PASS | BigAE top-cut (Paper 3 Table 1 canonical) |
| [[planck-cmb]] | 20,000 | 200 | 1.0% | FIXED (masked) | galactic-mask applied post-fire-#9 |
| [[act-dr6]] | 20,000 | 200 | 1.0% | FIXED | retrained, val_loss now acceptable |
| [[neowise]] | 43,500 | 436 | 1.0% | FIXED (ecliptic mask) | ecliptic-mask applied |
| [[gaia-dr3]] | 50,000 | 500 | 1.0% | PASS | expanded to 500K in later pass |
| **TOTAL** | **~37,300,000** | **319,443** | -- | -- | matches Paper 3 §1 canonical |

## QC Status Breakdown

- **PASS (3):** DESI DR1, eROSITA DR1, Gaia DR3
- **CAUTION (2):** SDSS DR18, LAMOST DR10
- **FAIL (3):** Planck CMB, ACT DR6, NEOWISE

## Anomaly Rate Interpretation

The anomaly rates are NOT directly comparable across surveys because:

1. **DESI (0.87%)** -- native model, most reliable rate
2. **SDSS (3.4%)** -- inflated by domain shift from DESI transfer model
3. **LAMOST (0.39%)** -- deflated by training bias (model flags blue objects, misses true anomalies)
4. **eROSITA (1.0%)** -- top-1% cut by design, not a trained threshold
5. **CMB surveys (1.0%)** -- top-1% cut, corrupted by systematics
6. **Gaia (1.0%)** -- top-1% cut, sample too small

Only DESI's 0.87% represents a genuine autoencoder-determined anomaly rate on a survey-native model.

## Novelty Fractions

| Survey | Novelty (% not in SIMBAD) |
|--------|--------------------------|
| DESI (SNR-filtered) | 52.5% |
| eROSITA | 73% |
| Gaia | 27% |
| SDSS (cross-match sample) | ~90% |
| Overall | 58.8% (SIMBAD cross-match) |

## Experiments Needing Re-Run

Per [[houston-method]] QC protocol:

1. **Planck CMB** -- re-run with galactic + point source mask
2. **ACT DR6** -- retrain with more epochs / learning rate scheduling
3. **NEOWISE** -- re-run with spatial detrending
4. **SDSS DR18** -- retrain survey-native model (or normalize scores)
5. **LAMOST DR10** -- train LAMOST-native autoencoder
6. **Gaia DR3** -- expand to 500K+ sources

## Connections

- Methodology: [[anomaly-detection-methodology]]
- QC protocol: [[houston-method]]
- f_NL impact: [[fnl-prediction]]
- Paper: [[paper-3-anomaly-catalog]]
