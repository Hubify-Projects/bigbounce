---
title: "Paper 3: Multi-Survey Anomaly Catalog"
type: entity
tags: [paper, anomaly, desi, sdss, erosita, lamost, fnl]
last_updated: 2026-04-04
sources:
  - pipelines/p3_anomaly_engine/
  - project-context/paper3_science_highlights.md
  - project-context/post_sweep_followon_plan.md
---

# Paper 3: Multi-Survey Anomaly Catalog

**Lines:** 735 LaTeX | **Status:** ~95% ready

## Summary

Comprehensive paper documenting the multi-survey anomaly sweep: 8 surveys, ~33.5M sources, ~328K anomalies. Includes f_NL improvement measurement and novel object discoveries.

## Key Results

- **Surveys:** DESI DR1, SDSS DR18, eROSITA DR1, LAMOST DR10, Planck, ACT DR6, NEOWISE, Gaia DR3
- **Total sources:** ~33.5M scored
- **Total anomalies:** ~328,448
- **f_NL improvement:** 6.1% (DESI alone), 16.4% (DESI + SDSS)
- **SPHEREx forecast:** 4.38-sigma detection
- **Novel fraction:** 58.8% of cross-matched anomalies not in SIMBAD

## 7 Science Highlights

1. Redshift neuron (latent dim 067, emergent physical encoding)
2. Unsupervised photo-z (sigma_NMAD = 0.028)
3. "Correctly classified but spectrally anomalous" paradox (2,575 objects)
4. Extreme IR variability in reionization-era QSOs (6 at z > 4)
5. Anomaly score as survey quality probe (Spearman rho = -0.89 with SNR)
6. ~1,000 genuinely uncataloged objects
7. Gold anomalies cluster in latent space (2.2x random density)

## Remaining Work

- Compile LaTeX to PDF (needs texlive-publishers on pod)
- Peer review round 1
- Decision on including birefringence beta result
- 6 experiments need QC re-runs before final numbers

## Connections

- Survey data from [[desi-dr1]], [[sdss-dr18]], [[erosita-dr1]], [[lamost-dr10]], [[planck-cmb]], [[act-dr6]], [[neowise]], [[gaia-dr3]]
- f_NL connection to [[fnl-prediction]]
- Methodology described in [[anomaly-detection-methodology]]
