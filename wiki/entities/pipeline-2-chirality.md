---
title: "Pipeline 2: Galaxy Chirality Catalog"
type: entity
tags: [pipeline, chirality, galaxy, parity]
last_updated: 2026-04-17
canonical_status_file: project-context/paper4_chirality_status.md
sources:
  - project-context/paper4_chirality_status.md
---

# Pipeline 2: Galaxy Chirality Catalog

> **Canonical status file:** [`project-context/paper4_chirality_status.md`](../../project-context/paper4_chirality_status.md)
>
> That file is the single source of truth. It covers artifacts (HuggingFace + Convex + B2 + on-pod), scripts, bias audit, dipole analysis, and submission readiness together.

## Status

**COMPLETE.** 8,474,531 galaxies classified, 8/8 bias tests pass, 0.43σ null dipole, 91.5% CE-ResNet cross-check. CNN classifier deployed on H100/H200 with DataLoader optimization (32× speedup from 29 min to 65 s per 44K-image shard — see `project-context/gpu-inference-playbook.md`).

## Published to

- HuggingFace: `bamfai/galaxy-chirality-catalog` (CC-BY-4.0), `bamfai/galaxy-chirality-v2` (model)
- Convex DB (8.47M rows, synced 2026-03-28)
- Backblaze B2 (full parquet snapshot)

## Scientific interpretation

Null result for large-scale parity violation from galaxy morphology. CW/(CW+CCW) = 0.4974, consistent with exact parity. Dipole is consistent with zero. This constrains but does not rule out bounce cosmology — most bounce models do not predict parity violation at the galaxy-morphology level. See SSOT §1 & §3 for the full claim audit.

## Connections

- Paper: [[paper-4-chirality]]
- GPU playbook: `project-context/gpu-inference-playbook.md`
