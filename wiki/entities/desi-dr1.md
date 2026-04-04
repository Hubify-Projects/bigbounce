---
title: DESI DR1 Anomaly Survey
type: entity
tags: [survey, anomaly, desi, fnl, flagship]
last_updated: 2026-04-04
sources:
  - project-context/active_pods_and_pipelines.md
  - project-context/pipeline1_tracer_purification_plan.md
  - project-context/paper3_science_highlights.md
  - pipelines/h200_results/
---

# DESI DR1

**Status:** COMPLETE | **QC:** PASS

## Summary

Flagship anomaly detection run on the full DESI Data Release 1 Main Survey catalog. Largest autoencoder-based spectral anomaly search ever performed on DESI, extending prior work (~200-250K EDR spectra) by ~90x in scale.

## Numbers

| Metric | Value |
|--------|-------|
| Spectra scored | 22,500,000 (18.7M in main run + enhanced rerun) |
| Anomalies (>5-sigma) | 195,829 (0.87%) |
| SNR-filtered anomalies | 2,145 |
| Uncataloged (not in SIMBAD/NED) | 1,127 (52.5% of SNR-filtered) |
| Taxonomy families | 10 |
| AGN identified | 76 |
| f_NL improvement | 6.1% (standard), 9.5% (multi-tracer forecast) |
| Gold anomalies | 83 (69 are QSOs at z > 5) |
| Latent dimensions | 128 |
| Feature columns | 173 |

## Key Findings

- Autoencoder spontaneously learned a "redshift neuron" (latent dim 067, 6x importance)
- Unsupervised photo-z at sigma_NMAD = 0.028 from latent vectors
- 2,575 objects with high pipeline confidence AND high anomaly score (the "correctly classified but spectrally anomalous" paradox)
- 6 QSOs at z > 4 with extreme IR variability (W2 amplitude 3-5.5 mag)
- Gold anomalies cluster 2.2x denser than random in latent space
- Anomaly score correlates strongly with SNR (Spearman rho = -0.89)

## Model

BigAE autoencoder trained on known DESI spectral classes. Published: HuggingFace `bamfai/desi-spectral-anomaly-detector`.

## Connections

- Feeds [[pipeline-1-tracer-purification]] (steps 2-6 pending)
- Primary dataset for [[paper-3-anomaly-catalog]]
- f_NL improvement quantified in [[fnl-prediction]]
- Cross-matched with [[sdss-dr18]] (3 matches found, including z=5.27 QSO)
- Methodology described in [[anomaly-detection-methodology]]
