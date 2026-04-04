---
title: "Paper 2: f_NL Forecast"
type: entity
tags: [paper, fnl, spherex, fisher]
last_updated: 2026-04-04
sources:
  - research/focused_paper_source_integration/02_full_draft.tex
  - project-context/CURRENT_STATUS.md
---

# Paper 2: f_NL Forecast

**Version:** v1.3.0 | **Pages:** 12 | **Status:** SUBMISSION-READY

## Summary

Focused paper on the matter bounce f_NL = -35/8 prediction and its testability. Presents the Fisher matrix forecast for SPHEREx detection significance.

## Key Content

- **Prediction:** f_NL = -35/8 = -4.375, parameter-free, mechanism-independent across all matter bounce variants
- **Fisher forecast:** sigma(f_NL) = 8.98 (standard), 8.12 (multi-tracer)
- **SPHEREx sensitivity:** sigma ~ 0.7-1.0, giving 4-6 sigma detection if prediction is correct
- **Current combined constraint:** Planck + DESI sigma(f_NL) = 2.94 (best), prediction at 0.9-sigma from zero
- **Template projection:** Planck bispectrum f_NL = -0.9 +/- 5.1 projected onto bounce template (alpha_L = 0.97) gives f_NL = -3.89 +/- 4.76

## Computation Scripts

11 Python scripts backing this paper (see `project-context/computation_scripts.md`):
- ALP field evolution, f_NL epsilon correction, transparency verification
- Template projection, photon-torsion coupling, Fisher forecast
- Photo-z degradation, b_phi sensitivity

## File Location

- Source: `research/focused_paper_source_integration/02_full_draft.tex`

## Connections

- Science detailed in [[fnl-prediction]]
- Tracer improvement from [[pipeline-1-tracer-purification]] would strengthen this paper
- f_NL triple role documented in [[bounce-portfolio]]
- SPHEREx timeline on website: `timeline.html`
