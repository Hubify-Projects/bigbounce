---
title: "Pipeline 2: Galaxy Chirality Catalog"
type: entity
tags: [pipeline, chirality, galaxy, parity]
last_updated: 2026-04-04
sources:
  - project-context/active_pods_and_pipelines.md
---

# Pipeline 2: Galaxy Chirality Catalog

**Status:** COMPLETE

## Summary

Largest galaxy chirality (handedness) classification ever performed. CNN classifier deployed on H100 GPU with DataLoader optimization (32x speedup from 29 min to 65s per 44K-image shard).

## Results

| Metric | Value |
|--------|-------|
| Galaxies classified | 8,474,531 |
| Classification | CW / CCW / NOT_SPIRAL |
| Accuracy | 93.7% |
| Bias tests passed | 8/8 |
| CW/(CW+CCW) | 0.4974 |
| Dipole significance | 0.43-sigma (null) |

## Infrastructure

- **GPU:** NVIDIA H100 pod
- **Key optimization:** `torch.utils.data.DataLoader` with `num_workers=16, pin_memory=True, prefetch_factor=4` -- documented in `project-context/gpu-inference-playbook.md`
- **Published to:** HuggingFace, Convex (8.47M rows), Backblaze B2

## Scientific Interpretation

Null result for cosmological parity violation from galaxy morphology. The CW/CCW ratio is consistent with 0.5 (no excess of either handedness). The dipole is consistent with zero (no preferred direction in the universe from galaxy spin data).

This constrains but does not rule out bounce cosmology -- most bounce models do not predict parity violation at the galaxy morphology level.

## Connections

- Paper: [[paper-4-chirality]]
- Null result context: [[bounce-portfolio]] (supporting, not decisive)
- GPU playbook used here applies to all future inference -- see [[anomaly-detection-methodology]]
