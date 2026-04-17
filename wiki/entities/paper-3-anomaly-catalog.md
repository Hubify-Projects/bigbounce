---
title: "Paper 3: Multi-Survey Anomaly Catalog"
type: entity
tags: [paper, anomaly, desi, sdss, erosita, lamost, fnl, nanograv]
last_updated: 2026-04-17
canonical_status_file: project-context/paper3_anomaly_catalog_status.md
sources:
  - project-context/paper3_anomaly_catalog_status.md
---

# Paper 3: Multi-Survey Anomaly Catalog

> **Canonical status file:** [`project-context/paper3_anomaly_catalog_status.md`](../../project-context/paper3_anomaly_catalog_status.md)
>
> That file is the single source of truth. Old "Remaining Work" lists on earlier versions of this page are obsolete — the paper was fully compiled 2026-04-15 and locked for submission 2026-04-16.

## One-line status

Paper 3 is science-complete and arXiv-ready. 8 surveys · 37.3 M sources · 319,443 anomalies · 58.8 % SIMBAD-novel · σ(f_NL) improved 6.1 % (DESI) / 16.4 % (DESI+SDSS) / 9.5 % (latent-space) · SPHEREx projection 4.38σ · NANOGrav γ = 3.20 ± 0.42 (ΔBIC = 7.0 favouring bounce). Canonical manuscript: `pipelines/p3_anomaly_engine/paper3_draft.tex` (1,032 lines, revtex4-2, 27 MB PDF with 21 figures).

## Core numbers (every figure traceable — see SSOT §3)

| Metric | Value |
|--------|-------|
| Surveys | 8 (DESI DR1, SDSS DR18, LAMOST DR10, eROSITA DR1, Planck CMB, ACT DR6, Gaia DR3, NEOWISE) |
| Sources scored | 37,292,042 |
| Total anomalies | 319,443 |
| SIMBAD-novel fraction | 58.8 % |
| DESI DR1 anomalies | 195,829 (0.87 %) |
| High-z (z = 6.0–6.23) QSOs in DESI | 12 |
| σ(f_NL) improvement (DESI+SDSS) | 16.4 % |
| SPHEREx detection significance (f_NL = −35/8) | 4.38σ |
| NANOGrav γ | 3.20 ± 0.42 (0.48σ from bounce γ = 3.0) |
| ΔBIC(SMBHB − bounce) | 7.0 |

## Connections

- Pipeline: [[pipeline-b-desi-anomaly]]
- f_NL theory: [[fnl-prediction]]
- Related paper: [[paper-4-chirality]] (shares the bias-measurement infrastructure for Principle-10 DO-NOW strengthening)
- Downstream: [[anomaly-detection-methodology]]
