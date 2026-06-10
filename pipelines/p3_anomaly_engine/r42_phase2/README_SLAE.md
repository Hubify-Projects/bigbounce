---
license: mit
tags: [astronomy, cosmology, anomaly-detection, autoencoder, desi, second-level]
---

# DESI Second-Level AE (SLAE) 640D -> 16D (R42 Phase 2)

SLAE compresses the concatenated 640D ensemble latent (5 BigAE seeds x 128D) into a 16D ultra-rare latent for the BigBounce DESI DR1 anomaly catalog.

## Files
- `slae_16d.pt` — PyTorch state dict
- `slae_mse.npy` — per-spectrum SLAE reconstruction MSE on the 100K OOD set
- `phase2_slae.json` — top-10/top-100 indices into the OOD set, val MSE, OOD percentiles
- `phase4_agreement.json` — ensemble agreement on top-100 SLAE outliers (cross-validation)

## Architecture
```
Encoder: 640 -> 256 -> 64 -> 16
Decoder: 16 -> 64 -> 256 -> 640
```

## Headline numbers
- Top-100 SLAE ultra-rare anomalies: 100% agreement with single-seed BigAE p99 thresholds across all 5 seeds (mean fraction = 1.000, std = 0.000)
- This means SLAE picks the same ultra-rare set that ALL 5 BigAE seeds independently flag

## Companion artifacts
- bamfai/desi-bigae-ensemble-v1 (5-seed BigAE pack)
- bamfai/desi-spectral-anomaly-detector (single-best BigAE)
- bamfai/bigbounce-anomaly-catalog (319K anomaly catalog)

Houston Golden, BigBounce program, 2026.
