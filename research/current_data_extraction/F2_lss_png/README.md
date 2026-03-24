# F2 — LSS / Tracer-Enhanced PNG Extraction

## Scientific Question

Can improved tracer selection from existing data reduce the effective uncertainty on local-PNG-like signals relevant to the canonical bounce benchmark?

## Canonical Target

f_NL = -35/8 = -4.375 (Planck convention)
Current best: Planck + DESI combined σ(f_NL) ≈ 4.1 (local template)

## Pipeline Stages

| Stage | Description | Gating |
|-------|-------------|--------|
| F2.1 | Baseline sample + benchmark | Must pass first |
| F2.2 | Enhanced tracer sample | Requires F2.1 |
| F2.3 | Selection-function / leakage audit | Mandatory before any claim |
| F2.4 | Spatial holdout validation | Mandatory |
| F2.5 | Injection / recovery in mocks | Mandatory |
| F2.6 | Utility curves | After F2.2-F2.5 |
| F2.7 | Combined current-data inference | After all above |

## Data Products Required

### Baseline sample (F2.1)

| Dataset | Source | Size | Fields needed | In repo? |
|---------|--------|------|---------------|----------|
| DESI DR1 spectroscopic catalog | DESI public release | ~18M targets | RA, Dec, z, target type, quality flags | No — need to download |
| Legacy Surveys DR10 photometry | legacysurvey.org | ~2B objects | g/r/z/W1/W2 mags, morphology, masks | No — query via API |
| unWISE catalog | unwise.me | ~2B sources | W1/W2 mags, motion, blending flags | No — need download |

### For enhanced sample (F2.2)

- Cross-matches of above catalogs
- DESI target selection bitmasks for QSO/LRG/ELG identification
- Galactic extinction maps (SFD or Planck thermal dust)
- Stellar density maps (Gaia)
- Survey depth / seeing maps (Legacy Surveys randoms)

### For mocks (F2.5)

- DESI mock catalogs (if publicly available)
- Or: EZmocks / QPM mocks with known f_NL injection
- Minimum: lognormal mocks with local-PNG imprint

## RunPod Requirements

| Task | Pod type | Reason | Est. time |
|------|----------|--------|-----------|
| Catalog download + cross-match | CPU (32-core) | Large I/O, no GPU needed | 2-4 hours |
| ML training (XGBoost/LightGBM) | CPU (32-core) | Tree models don't benefit from GPU | 1-2 hours |
| Mock generation + PNG injection | CPU (32-core) | Monte Carlo, parallelizable | 2-4 hours |
| Neural tracer model (if justified) | GPU (A100/H100) | Only if tree models insufficient | 2-4 hours |
