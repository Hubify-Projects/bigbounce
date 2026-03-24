# Current-Data Extraction Program

Three publication-grade pipelines for extracting matter-bounce-relevant information from current public data.

## Pipelines

| Pipeline | Goal | Primary Data |
|----------|------|-------------|
| **F1** — Bispectrum | Bounce-specific f_NL extraction from CMB | Planck PR3/PR4 public products |
| **F2** — LSS/PNG | Tracer-enhanced PNG extraction from galaxy surveys | DESI DR1 + Legacy Surveys + unWISE |
| **F3** — CMB Residuals/EB | Robustness support for birefringence + bispectrum | Planck + ACT maps |

## Methodology

All pipelines follow the same standards (see `docs/validation_standards.md`):
1. Reproduce known baseline first
2. Injection/recovery validation
3. Null tests
4. Holdout robustness
5. Nuisance audit
6. Honest final claim

## Canonical Values

| Parameter | Value | Confidence | Source |
|-----------|-------|-----------|--------|
| f_NL (Planck convention) | -35/8 = -4.375 | 92% | Phase 1 normalization audit |
| Template mismatch r | 0.84 ± 0.02 | A- | Robustness audit (10 weights) |
| ALP birefringence β | 0.27° | Prediction | Natural ALP parameters |

## Current Status

| Pipeline | Status | Level |
|----------|--------|-------|
| F1 | Scaffolding | — |
| F2 | Scaffolding | — |
| F3 | Scaffolding | — |
