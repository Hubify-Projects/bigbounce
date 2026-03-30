# 8.47M Galaxy Chirality Catalog

**Status:** Analysis Complete | **Paper:** 4 (~75% ready) | **Target:** MNRAS

## Overview
Largest bias-audited galaxy handedness measurement ever produced. 8,474,531 galaxies classified for spiral direction (CW/CCW/NOT_SPIRAL) using ViT-Small with equivariant post-processing.

## Key Results
- 93.7% accuracy, 8/8 bias tests passed
- Equivariant CW fraction = 0.5012 (parity conserved)
- No evidence for large-scale parity violation
- 40x larger than prior work (CE-ResNet 1.95M)
- 32x GPU speedup via DataLoader optimization

## Files
- Paper: `arxiv/paper4_chirality_catalog.tex` (798 lines, compiled PDF)
- Pipeline: `pipelines/p2_chirality/`
- Catalog: `pipelines/p2_chirality/outputs/chirality_catalog_v2_COMPLETE.parquet` (268MB)
- Explorer: `galaxy-explorer.html`
- Model: [bamfai/galaxy-chirality-v2](https://huggingface.co/bamfai/galaxy-chirality-v2)

## Cost
~$80 (H100 inference)
