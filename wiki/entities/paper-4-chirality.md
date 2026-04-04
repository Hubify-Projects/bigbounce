---
title: "Paper 4: Galaxy Chirality Catalog"
type: entity
tags: [paper, chirality, galaxy, dipole]
last_updated: 2026-04-04
sources:
  - pipelines/p2_chirality/chirality_catalog_paper.tex
  - public/papers/chirality_catalog_paper.pdf
  - project-context/CURRENT_STATUS.md
---

# Paper 4: Galaxy Chirality Catalog

**Lines:** 1,099 LaTeX | **Status:** ~85% ready

## Summary

Catalog paper documenting the largest galaxy chirality (handedness) classification ever performed. Tests cosmological parity violation via the CW/CCW spiral ratio and cosmic dipole alignment.

## Key Results

| Metric | Value |
|--------|-------|
| Galaxies classified | 8,474,531 |
| Classification accuracy | 93.7% |
| Bias tests passed | 8/8 |
| CW/(CW+CCW) ratio | 0.4974 |
| Dipole significance | 0.43-sigma (null) |
| Classes | CW, CCW, NOT_SPIRAL |

## Interpretation

The chirality ratio is consistent with parity symmetry (0.5 expected). The dipole is consistent with zero. This is a null result for cosmological parity violation from galaxy morphology, but the catalog itself is a major data product.

## Remaining Work

1. Add confusion matrix figure
2. Add training curves figure
3. Add redshift distribution figure
4. Final peer review

## File Locations

- Source: `pipelines/p2_chirality/chirality_catalog_paper.tex`
- PDF: `public/papers/chirality_catalog_paper.pdf`
- Figures: `public/images/chirality/`

## Data Products

Published to:
- HuggingFace: `bamfai/bigbounce-mcmc`
- Convex: Catalog C (8.47M rows)
- Backblaze B2

## Connections

- Pipeline: [[pipeline-2-chirality]]
- Uses GPU inference playbook (DataLoader 32x speedup)
- Null result constrains but does not close bounce models -- see [[bounce-portfolio]]
