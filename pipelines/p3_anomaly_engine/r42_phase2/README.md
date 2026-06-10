---
license: mit
tags: [astronomy, cosmology, anomaly-detection, autoencoder, desi, ensemble]
---

# DESI BigAE 5-Seed Ensemble (R42 Phase 1)

5 BigAE autoencoders (496->128 latent) retrained with seeds 101, 202, 303, 404, 505 on a 47K DESI training proxy and scored on a 100K out-of-distribution DESI DR1 set. Used for ensemble error bars on Paper 3 (BigBounce anomaly catalog) B10 reproducibility BLOCKER.

## Files
- `bigae_seed{101,202,303,404,505}.pt` — PyTorch state dicts for each seed
- `mse_seed{101,202,303,404,505}.npy` — per-spectrum reconstruction MSE on the 100K OOD set (N=100,000)
- `phase1_ensemble.json` — per-seed val_mse, OOD median/p99/max, ensemble agreement summary

## Architecture
```
Encoder: 496 -> 512 -> 256 -> 128
Decoder: 128 -> 256 -> 512 -> 496
```

## Headline numbers (100K OOD set)
- Ensemble median of per-seed means: **0.384**
- Ensemble p99 of per-seed means: **60.18**
- Ensemble relative std: **2.04%** (tight cross-seed convergence)

## Reproducibility
Trained 2026-05-01 on H200 (RunPod, 80 GB SXM) in ~22 s wall clock for all 5 seeds at 6 epochs each.

## Citation
Companion to bamfai/desi-spectral-anomaly-detector and bamfai/bigbounce-anomaly-catalog.

Houston Golden, BigBounce program, 2026.
