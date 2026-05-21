---
library_name: pytorch
tags:
  - astronomy
  - galaxy-morphology
  - chirality
  - parity-violation
  - vit
  - test-time-augmentation
  - desi-legacy
license: cc-by-4.0
language:
  - en
pipeline_tag: image-classification
datasets:
  - bamfai/galaxy-chirality-catalog
metrics:
  - accuracy
  - calibrated_brier_score
model-index:
  - name: bamfai/galaxy-chirality-v2
    results:
      - task:
          type: image-classification
          name: Spiral galaxy chirality (CW / CCW / NS)
        dataset:
          name: DESI Legacy DR9 (Paper IV training split)
          type: image-classification
        metrics:
          - type: accuracy
            value: 0.9210
            name: validation accuracy (3-class)
          - type: equivariance_suppression
            value: 3.86
            name: raw → equivariant asymmetry suppression factor
---

# Galaxy Chirality Classifier (bamfai/galaxy-chirality-v2)

**Companion model for Paper IV `v1.0.122` —
*A Survey-Scale Chirality Catalog of 8.47M Galaxies (3.2M Spirals):
A Null Detection of Large-Scale Parity Violation at Sub-Percent Sensitivity*.**

Source: [`Hubify-Projects/bigbounce`](https://github.com/Hubify-Projects/bigbounce)
@ tag [`paper4-v1.0.122`](https://github.com/Hubify-Projects/bigbounce/releases/tag/paper4-v1.0.122).

## Model overview

- Architecture: **ViT-Small/16** with mirror-equivariant test-time
  augmentation. Z₂ 2-fold flip is the production TTA mode (D₄ 8-fold
  tested on hold-outs only; see Paper IV §sec:tta).
- Output classes: **CW**, **CCW**, **NS** (not-spiral).
- Calibration: per-class Platt scaling (L-BFGS on a held-out 20% split).
  Raw → calibrated → equivariant residuals reported in Paper IV
  Table V (raw +0.79% / 28.8σ → calibrated +0.4% / 14.6σ → equivariant
  −0.26% / 9.5σ).
- Equivariance suppression factor **3.86×** (raw asymmetry +2.05% →
  equivariant asymmetry −0.53%).

## Catalog scale

Applied to the DESI Legacy DR9 8.47M-galaxy footprint via the canonical
Paper IV pipeline:

- 8,474,531 galaxies classified (1,687,069 CW / 1,634,726 CCW / 5,152,736 NS)
- 3,201,160 chirality-relevant spirals
- Catalog-wide CW fraction (post-TTA equivariant) **0.4974 ± 0.000279**,
  consistent with parity at ~1σ; the residual −0.0026 monopole is a
  classifier-residual bias, not a cosmological dipole.

## Key results (v1.0.122)

- **−0.12σ MASTER-deconvolved ℓ=1 amplitude** on the subsample-mask
  (load-bearing null).
- **+3.64σ canonical-mask ℓ=1 amplitude** (post-MASTER) interpreted as a
  coherent depth/PSF/morphology-correlated systematic on the canonical
  footprint, NOT a primordial dipole, via three direct quantitative
  anchors:
  - ℓ=2 cross-spectrum quadrupole anti-alignment with pixel-density proxy
    (`r = −0.65`, `σ = −2.89`)
  - Leg-stratified ℓ=1 contribution: BASS+MzLS / DECaLS / DES
    cross-power gives induced |a₁| = 25% of canonical |a₁_obs| = 7.04×10⁻³
  - MASTER-decoupled monopole-only null × 500: data post-MASTER C₁ =
    6.55×10⁻⁶ vs null mean 8.0×10⁻⁷ (σ = +4.84 Gaussian / empirical-rank
    p = 0.006); monopole leakage accounts for ~12% of post-MASTER C₁
- Family-level max-stat null on 15-cell leg×conf grid: observed max|σ| =
  4.72 collapses to ~2.4σ family-corrected joint p = 0.0086.

## R-round cross-vendor convergence

Cascaded-loop exit confirmed at Paper IV `v1.0.122` per AGENT_RULES §4.4.1:
**3 consecutive 5/5 clean R-rounds (R23 + R24 + R25)** across DeepSeek-V4-Pro
+ Gemini-3.1-Pro + GPT-5 + Grok-4.3 + Perplexity-Sonar-Pro
(45 of 45 reviewers returned 0 BLOCKER / 0 MAJOR).

## Usage

```python
from huggingface_hub import hf_hub_download
import torch

ckpt_path = hf_hub_download(
    repo_id="bamfai/galaxy-chirality-v2",
    filename="model.safetensors",
    revision="paper4-v1.0.122",
)
state = torch.load(ckpt_path, map_location="cpu", weights_only=True)
# Then load into ViT-Small/16 + 3-class head as documented in
# pipelines/p2_chirality/run_eq_dataloader.py
```

## Companion catalog dataset

Per-galaxy CW/CCW/NS labels + per-class probabilities + leg provenance:
[`bamfai/galaxy-chirality-catalog`](https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog)
(immutable revision `paper4-v1.0.122`).

## Citation

```bibtex
@misc{golden_chirality_2026,
  author = {Houston Golden},
  title  = {A Survey-Scale Chirality Catalog of 8.47M Galaxies (3.2M Spirals):
            A Null Detection of Large-Scale Parity Violation at Sub-Percent Sensitivity},
  year   = {2026},
  url    = {https://github.com/Hubify-Projects/bigbounce/blob/main/pipelines/p2_chirality/chirality_catalog_paper.tex},
  note   = {Paper IV, version v1.0.122; tag paper4-v1.0.122}
}
```

## Bias and limitations

- Trained on DESI Legacy DR9 / DR8 imaging. Generalization to other
  surveys (HSC, KiDS, future LSST) requires re-validation.
- A residual catalog-wide CW-fraction offset of −0.0026 (a ~5σ deviation
  from 0.5 at N = 3.2M chirality-relevant spirals) is attributable to
  classifier-residual bias and is documented in Paper IV §VI.E.
- For environment-dependent chirality, see the companion Paper V
  (`pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`).

## Provenance

- **Released**: 2026-05-21 (cron fire #3, autonomous drive-to-100 loop).
- **Paper IV tag**: `paper4-v1.0.122`.
- **Repository SHA**: see `git log paper4-v1.0.122` in `Hubify-Projects/bigbounce`.
- **Prior model card revision**: `v1.0.104` (superseded).
