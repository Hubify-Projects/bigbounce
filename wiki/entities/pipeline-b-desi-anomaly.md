---
title: "Pipeline B: DESI Anomaly Detection"
type: entity
tags: [pipeline, desi, autoencoder, anomaly]
last_updated: 2026-04-04
sources:
  - project-context/pipeline1_tracer_purification_plan.md
  - project-context/enhanced_18M_rerun_spec.md
---

# Pipeline B: DESI Anomaly Detection

**Status:** COMPLETE

## Summary

The flagship anomaly detection pipeline. A BigAE autoencoder trained on DESI DR1 spectral classes, deployed at scale to score the full 22.5M-spectrum Main Survey catalog.

## Architecture

- **Model:** Autoencoder (128-dim latent space, 173 input features)
- **Training:** Unsupervised on known DESI spectral classes (reconstruction loss only)
- **Inference:** Parallel scoring across full DR1 catalog
- **Scoring:** Reconstruction error as anomaly score, sigma-clipped at 5-sigma
- **Published model:** HuggingFace `bamfai/desi-spectral-anomaly-detector`

## Outputs

- 195,829 anomalies with TARGETID, RA, DEC, z, anomaly_score, band residuals, DESI class
- 128-dim latent vectors for all scored objects
- UMAP embeddings and HDBSCAN cluster assignments
- SNR-filtered catalog (2,145 objects)
- Gold anomaly catalog (83 objects)

## Scale Achievement

90x larger than prior autoencoder-based anomaly detection on DESI (Liang+ 2023 ApJL, Nicolaou+ 2026 MNRAS used ~200-250K EDR spectra). First application to the full DR1 Main Survey.

## Transfer Learning

The DESI-trained model was applied via transfer learning to:
- [[sdss-dr18]] (2.3M spectra -- QC: CAUTION due to domain shift)
- [[lamost-dr10]] (11.4M spectra -- QC: CAUTION due to training bias)

Results suggest survey-specific models are needed for reliable anomaly detection on non-DESI data.

## Connections

- Results feed [[pipeline-1-tracer-purification]]
- Primary data for [[paper-3-anomaly-catalog]]
- Survey page: [[desi-dr1]]
- Methodology: [[anomaly-detection-methodology]]
