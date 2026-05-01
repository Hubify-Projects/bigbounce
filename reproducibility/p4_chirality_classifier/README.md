# Paper 4 — 8.47 M-Galaxy ViT-Small Chirality Classifier

**Closes:** R42 finding `P1-OA-B1` (GPT-5 cross-model peer review,
2026-05-01) — Paper 1 §VI references the chirality classifier and
8.47 M-galaxy CW/CCW catalog (cited via `Golden:2026chirality`); Paper 1's
"Data and Code Availability" said "No CNN galaxy classifier is included."
This directory closes that gap. Paper 4 itself is the catalog paper; this
bundle is what a reviewer needs to re-run inference end-to-end given the
public Galaxy-Zoo DESI image set and the public HF-hosted weights.

## What this directory reproduces

| Quantity | Value | Source |
|---|---:|---|
| Total galaxies classified | 8 474 531 | `pipelines/p2_chirality/run_v2_inference.py` |
| 3-class validation accuracy | 0.937 | `chirality_model_v2_best.pt` ckpt['val_acc'] |
| Global CW / (CW+CCW) | 0.4974 | catalog summary |
| Global Bias-hardening tests | 8/8 PASS | `pipelines/p2_chirality/BIAS_AUDIT_REPORT.md` |

These are the canonical Paper 4 numbers and the cross-paper anchor used in
Paper 1 §VI ("Robustness to Galaxy Spin Null Results").

## Files

```
p4_chirality_classifier/
├── README.md                       # this file
├── requirements.txt                # pip install dependencies
└── scripts/
    ├── fetch_weights.sh            # one-liner curl / HF snapshot for the weights
    ├── train_chirality_v2.py       # training pipeline (mirror of pod copy)
    └── run_v2_inference.py         # 8.47 M streaming inference (mirror)
```

## Why the weights are not bundled

The `chirality_model_v2_best.pt` checkpoint is a ViT-Small + 3-class head
saved with `weights_only=True` (~88 MB serialized), which is past the
50 MB practical commit ceiling on GitHub. HuggingFace is the canonical
home:

```
https://huggingface.co/bamfai/galaxy-chirality-v2
```

`scripts/fetch_weights.sh` will download the file with either `curl` or
`huggingface-cli`. After fetch, `run_v2_inference.py` expects the
checkpoint at `OUTPUT_DIR/chirality_model_v2_best.pt` (default
`/workspace/analysis3_outputs/`); pass `--weights` or set the environment
to relocate.

## How to reproduce inference

```bash
# 1. install deps
pip install -r requirements.txt

# 2. fetch the v2 model weights (~88 MB)
bash scripts/fetch_weights.sh ./weights

# 3. point the inference script at the weights
export OUTPUT_DIR=./weights
python scripts/run_v2_inference.py
# Streams mwalmsley/gz_desi from HF; writes
#   ./weights/chirality_catalog_v2_full.parquet
# Runtime: ≈ 8 h on a single H200 with the DataLoader pattern in
# project-context/gpu-inference-playbook.md (32× speedup vs serial PIL).
```

## How to re-train (optional)

Skip this if you only need to re-run inference. The training script
`scripts/train_chirality_v2.py` reproduces the bias-hardened classifier
from scratch:

- Backbone: `timm.vit_small_patch16_224` (ImageNet-pretrained init).
- Head: 384 → 512 → 256 → 3 with LayerNorm, GELU, dropout (0.3, 0.2).
- Loss: 3-way cross-entropy + flip-equivariance consistency penalty.
- Data: 26 626 images from Galaxy Zoo 1 (5 000 high-confidence CW + 5 000
  high-confidence CCW + 16 626 NOT_SPIRAL) supplemented with synthetic
  hard negatives (rotated, JPEG-compressed, low-S/N) for bias hardening.
- Train test in `pipelines/p2_chirality/BIAS_AUDIT_REPORT.md` (8 tests,
  all PASS).

## Companion artifacts on HuggingFace

| Artifact | HF path | Visibility |
|---|---|---|
| Catalog (8.47 M rows, parquet) | `bamfai/galaxy-chirality-catalog` | Houston-pending (R42 B23) |
| Model weights + card | `bamfai/galaxy-chirality-v2` | public |

The catalog dataset visibility flip is documented in
`project-context/SSOT/paper-4/status.md` under the "HF dataset visibility"
heading; that decision belongs to Houston (HF dashboard → settings →
visibility → public).

## Provenance

- The local mirrors here (`scripts/run_v2_inference.py`,
  `scripts/train_chirality_v2.py`) are byte-identical to the canonical
  copies at `pipelines/p2_chirality/run_v2_inference.py` and
  `pipelines/p2_chirality/train_chirality_v2.py`. Copies are kept in this
  directory so the reproducibility bundle is self-contained.
- The 8.47 M-row catalog file (`chirality_catalog_v2_full.parquet`,
  ~ 600 MB) is not bundled here either — it lives on HF under
  `bamfai/galaxy-chirality-catalog` (currently private; flip is
  Houston-decision).
