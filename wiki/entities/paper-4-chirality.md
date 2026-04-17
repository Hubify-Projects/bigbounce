---
title: "Paper 4: Galaxy Chirality Catalog"
type: entity
tags: [paper, chirality, galaxy, dipole]
last_updated: 2026-04-17
canonical_status_file: project-context/paper4_chirality_status.md
sources:
  - project-context/paper4_chirality_status.md
---

# Paper 4: Galaxy Chirality Catalog

> **Canonical status file:** [`project-context/paper4_chirality_status.md`](../../project-context/paper4_chirality_status.md)
>
> That file is the single source of truth. Do not rely on older lists of "remaining work" — they were accurate at a point in time but the work has since been done.

## One-line status

Paper 4 is science-complete (8.47M galaxies classified, 8/8 bias tests, 0.43σ null dipole, Shamir refuted 7×) and arXiv-submission-ready once four trivial admin items are resolved. See canonical status file for the blocker list and execution plan.

## Core numbers (every figure traceable — see SSOT §3)

| Metric | Value |
|--------|-------|
| Galaxies classified | 8,474,531 |
| Classification accuracy (3-class) | 93.7% |
| Bias tests passed | 8/8 |
| CW/(CW+CCW) equivariant | 0.4974 |
| Dipole significance (null) | 0.43σ |
| Shamir 3% asymmetry refutation | 7× smaller (max 0.47%) |
| External cross-check (CE-ResNet) | 91.5% agreement |

## Connections

- Pipeline: [[pipeline-2-chirality]]
- Cross-reference from Paper 2: `pipelines/p2_chirality/paper2_chirality_section.tex`
- GPU inference playbook: `project-context/gpu-inference-playbook.md` (DataLoader 32× speedup pattern)
