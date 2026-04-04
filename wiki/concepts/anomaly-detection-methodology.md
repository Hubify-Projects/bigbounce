---
title: Anomaly Detection Methodology
type: concept
tags: [methodology, autoencoder, anomaly, qc, pipeline]
last_updated: 2026-04-04
sources:
  - project-context/paper3_science_highlights.md
  - project-context/pipeline1_tracer_purification_plan.md
  - project-context/houston-method-v2.md
  - project-context/gpu-inference-playbook.md
---

# Anomaly Detection Methodology

Autoencoder-based unsupervised anomaly detection across astronomical surveys, with mandatory QC gates and cross-match validation.

## Core Approach

1. **Train** an autoencoder on "normal" spectra/sources from the survey
2. **Score** every object by reconstruction error (high error = anomalous)
3. **Threshold** at 5-sigma above the mean reconstruction error
4. **QC gate** -- apply the 7 mandatory quality checks (see [[houston-method]])
5. **Cross-match** top anomalies against SIMBAD, NED, VizieR
6. **Classify** -- separate real anomalies from artifacts, noise, and known objects
7. **Interpret** -- connect to bounce cosmology predictions

## Architecture

- **Model:** Autoencoder with 128-dimensional latent space
- **Input:** 173 spectral features (for DESI; varies by survey)
- **Training:** Reconstruction loss only (no labels, no redshift supervision)
- **Inference:** `torch.utils.data.DataLoader` with `num_workers=16, pin_memory=True, prefetch_factor=4` for 32x speedup

## Key Discovery: Emergent Physical Encoding

The autoencoder spontaneously encodes physically meaningful quantities:
- Latent dimension 067 is a "redshift neuron" (6x permutation importance over any other dim)
- Latent vectors support unsupervised photo-z at sigma_NMAD = 0.028
- Anomalies cluster in latent space (2.2x random density) -- coherent populations, not noise

## Survey-Specific vs Transfer Learning

| Approach | Pros | Cons |
|----------|------|------|
| Survey-native model | Accurate anomaly scores, no domain shift | Requires retraining per survey |
| Transfer from DESI | Fast deployment, cross-survey comparison | Score explosion, training bias artifacts |

Results show transfer learning produces QC CAUTION flags for [[sdss-dr18]] (score explosion) and [[lamost-dr10]] (98% blue-excess bias). Survey-native models recommended.

## QC Gate Integration

Every anomaly catalog must pass the [[houston-method]] QC gate before scientific analysis proceeds. Surveys that failed QC as of 2026-04-04:
- [[planck-cmb]]: galactic contamination (spatial concentration)
- [[act-dr6]]: undertrained model (val_loss = 22,420)
- [[neowise]]: survey systematic (spatial concentration at RA ~ 180)

## Cross-Match Validation Protocol

Mandatory cross-match against:
1. **SIMBAD** (2 arcsec radius) -- general astronomical database
2. **NED** (5 arcsec radius) -- extragalactic database
3. **VizieR** (survey-specific) -- specialized catalogs

Novelty fraction = % not in any catalog. Current results: 52.5% novel for DESI SNR-filtered, 73% for eROSITA, 27% for Gaia.

## Connections

- Flagship pipeline: [[pipeline-b-desi-anomaly]]
- Tracer application: [[pipeline-1-tracer-purification]]
- Paper: [[paper-3-anomaly-catalog]]
- QC protocol: [[houston-method]]
- All survey pages reference this methodology
