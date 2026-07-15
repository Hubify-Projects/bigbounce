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
  - calibrated_brier_score
model-index:
  - name: bamfai/galaxy-chirality-v2
    results:
      - task:
          type: image-classification
          name: Spiral galaxy chirality (CW / CCW / NS)
        dataset:
          name: Historical mixed-source training reconstruction (not exactly reproducible)
          type: image-classification
        metrics:
          - type: equivariance_suppression
            value: 2.98
            name: raw → equivariant asymmetry suppression factor
---

# Galaxy Chirality Classifier (bamfai/galaxy-chirality-v2)

**Companion model for the current Paper IV manuscript —
*An Observed-Label Chirality-Dipole Null in 949,584 High-Confidence DESI
Spirals and an 8.5-Million-Galaxy Catalog*.**

Current manuscript source: [`Hubify-Projects/bigbounce`](https://github.com/Hubify-Projects/bigbounce/blob/main/pipelines/p2_chirality/chirality_catalog_paper.tex).
No immutable repository tag or DOI for the current Paper IV manuscript is claimed.

## Model overview

- Architecture: **ViT-Small/16** with mirror-equivariant test-time
  augmentation. Z₂ 2-fold flip is the production TTA mode (D₄ 8-fold
  tested on hold-outs only; see Paper IV §sec:tta).
- Output classes: **CW**, **CCW**, **NS** (not-spiral).
- Calibration: per-class Platt scaling (L-BFGS on a held-out 20% split).
  Raw → calibrated → equivariant residuals reported in Paper IV
  Table V (raw +0.79% / 28.8σ → calibrated +0.4% / 14.6σ → equivariant
  −0.26% / 9.5σ).
- Equivariance suppression factor **2.98×** (raw asymmetry +1.576% →
  equivariant asymmetry −0.529%).

## Catalog scale

Applied to the DESI Legacy DR8 8.47M-galaxy footprint via the canonical
Paper IV pipeline:

- 8,474,531 galaxies in the science-facing catalog
- 1,592,107 CW + 1,609,053 CCW = 3,201,160 chirality-relevant spirals
- Catalog-wide CW fraction (post-TTA equivariant) **0.4974 ± 0.000279**,
  a **−9.47σ classifier-residual monopole** relative to 0.5 in raw-count
  binomial units, not a cosmological dipole. The distinct primary
  fixed-occupancy dipole statistic is consistent with its null
  (`z=+0.7053169638`; one-sided empirical-rank `p=0.2246775322`).

## Current Paper IV result

The primary high-confidence observed-label statistic is consistent with zero
under fixed-occupancy label randomization (`z=0.7053169638`, one-sided
empirical-rank `p=0.2246775322`). It is not a calibrated true-spin,
physical-amplitude, or primordial-parity bound. WLS and harmonic results use
different supports or nulls and are retained as systematics diagnostics rather
than headline detection tests.

## Historical v1.0.123–v1.0.125 changelog

The following entries document an older manuscript state. They are preserved
for provenance and do not describe the current manuscript or establish a
current clean-review verdict.

- **v1.0.123** closed the Houston-shared external review on v1.0.122 (ChatGPT
  MAJOR REVISIONS + Grok MINOR REVISIONS + Gemini MAJOR REVISIONS; 9 BLOCKER +
  10 MAJOR bundled hard-fix; 2 BLOCKERs audit-falsified). Stripped all
  internal-review scaffolding (`Perplexity R22`, `P4-EXT`, `P4-INT`,
  `R20-Grok-B2 closure`, etc.); fixed 3 undefined section references; tightened
  Shamir 2022 framing; softened "three-interpretation closure" → "diagnostic";
  added explicit "headline uses p_CW-weighted maps not argmax labels" defense
  against the 21% D4-TTA flip-rate concern. HF dataset README also pushed to
  v1.0.123 in the same fire.
- **v1.0.124** closed ChatGPT MAJOR M3: new mask pixel-count-threshold robustness
  sweep (5 cells × MASTER coupling matrix × N=200 monopole-only null) shows the
  canonical-mask ℓ=1 σ is robust at +6.31 to +8.26 across n_total > {1,5,10,20,50}.
  Signal does **not** attenuate at higher thresholds — rules out the
  low-count-edge artifact interpretation. New §IX.B "Mask robustness" subsection
  + Table V + pre-specified estimator hierarchy paragraph.
- **v1.0.125** closed Gemini MAJOR M-2: new DECaLS [0.5,0.6) stratum-specific
  cross-spectrum C^{An}_ell on the 938,563-spiral stratum (f_sky=0.279). Result:
  r_ℓ=1 = −0.70 (σ = −1.68), same negative-correlation sign as full canonical
  −0.49 with **larger** magnitude. The DECaLS-stratum excess is anti-correlated
  with its own pixel-density at the same scale as the canonical depth-systematic
  signature — directly ties the stratum's family-corrected ~2.4σ excess to the
  depth-correlated systematic family (interpretation ii), not a separate
  DECaLS-specific physical signal.

## Historical R-round record

At the historical Paper IV `v1.0.125` state, the project recorded:
**3 consecutive 5/5 clean R-rounds (R23 + R24 + R25)** across DeepSeek-V4-Pro
+ Gemini-3.1-Pro + GPT-5 + Grok-4.3 + Perplexity-Sonar-Pro
(45 of 45 reviewers returned 0 BLOCKER / 0 MAJOR). This historical record is
not a review result for the current manuscript.

## Usage

```python
from huggingface_hub import hf_hub_download
import torch
import torch.nn as nn
import timm

ckpt_path = hf_hub_download(
    repo_id="bamfai/galaxy-chirality-v2",
    filename="chirality_model_v2_best.pt",
    revision="237d021c451d75cf86a875e86d4de498b74e2f12",
)

class Head(nn.Module):
    def __init__(self):
        super().__init__()
        self.h = nn.Sequential(
            nn.LayerNorm(384), nn.Linear(384, 512), nn.GELU(), nn.Dropout(0.3),
            nn.Linear(512, 256), nn.GELU(), nn.Dropout(0.2), nn.Linear(256, 3),
        )
    def forward(self, x):
        return self.h(x)

state = torch.load(ckpt_path, map_location="cpu", weights_only=True)
encoder = timm.create_model("vit_small_patch16_224", pretrained=False,
                            num_classes=0)
head = Head()
encoder.load_state_dict(state["enc"])
head.load_state_dict(state["head"])
encoder.eval()
head.eval()
```

The checkpoint is a PyTorch dictionary with `enc`, `head`, `val_acc`, `epoch`,
and `n_classes` entries, not a standalone safetensors model. Exact production
preprocessing and equivariant inference are documented in
[`run_eq_dataloader.py`](https://github.com/Hubify-Projects/bigbounce/blob/main/pipelines/p2_chirality/run_eq_dataloader.py).
Because the historical environment and training realization are not fully
pinned, this loading example does not claim standalone exact reproducibility.

## Companion catalog dataset

Per-galaxy CW/CCW/NS labels + per-class equivariant ranking scores:
[`bamfai/galaxy-chirality-catalog`](https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog)
(see the dataset card for its pinned data/provider commits; no current manuscript tag is
claimed here).

## Citation

```bibtex
@misc{golden_chirality_2026,
  author = {Houston Golden},
  title  = {An Observed-Label Chirality-Dipole Null in 949,584 High-Confidence
            DESI Spirals and an 8.5-Million-Galaxy Catalog},
  year   = {2026},
  url    = {https://github.com/Hubify-Projects/bigbounce/blob/main/pipelines/p2_chirality/chirality_catalog_paper.tex},
  note   = {Paper IV, current manuscript; no DOI assigned}
}
```

## Bias and limitations

- Applied to DESI Legacy DR8 imaging. Generalization to other
  surveys (HSC, KiDS, future LSST) requires re-validation.
- The historical training realization is not exactly reproducible: the
  committed README reports 92.10% three-class validation accuracy, while an
  immutable-repository audit reconstructs 93.6878% with 21,293 training and
  5,323 validation rows. Conflicting total/non-spiral counts, absent retained
  object/split membership, and missing random-state/run receipts prevent either
  metric from being treated as a resolved, exactly replayable validation.
- A residual catalog-wide CW-fraction offset of −0.002647 (a −9.47σ deviation
  from 0.5 at N = 3.2M chirality-relevant spirals) is attributable to
  classifier-residual bias and is documented in Paper IV §VI.E.
- For environment-dependent chirality, see the companion Paper V
  (`pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`).

## Provenance

- **Current manuscript**: Paper IV source linked above.
- **Audited model revision**: `237d021c451d75cf86a875e86d4de498b74e2f12`.
- **Historical card state**: v1.0.125 framing is retained above only as a
  labeled changelog; it is superseded by the current manuscript framing.
- **Publication identifiers**: no immutable tag for the current manuscript, arXiv identifier, or
  DOI is claimed.
