---
title: Bounce Cosmology Portfolio Strategy
type: concept
tags: [bounce, strategy, portfolio, quintom, pbh, nanograv]
last_updated: 2026-04-04
sources:
  - project-context/bounce_portfolio_strategy.md
  - project-context/CURRENT_STATUS.md
---

# Bounce Cosmology Portfolio

Model-agnostic strategy: prove bounce cosmology beats inflation across multiple models and observational channels.

## Strategic Reframe

- **Old:** "Our ECH Model B predicts f_NL = -35/8. Single point of failure."
- **New:** "Bounce cosmology has a portfolio of testable predictions across multiple models. f_NL = -35/8 is the flagship, but the case is built across 6 channels."

The 14 ECH barriers are ECH-specific. Other bounce models (quintom, cuscuton, ekpyrotic) bypass them entirely. The barriers MAP the structural requirements for bounce-DE unification -- they are constructive, not terminal.

## Six Observational Channels

| Channel | Best Model | Prediction | Experiment | Timeline | Status |
|---------|-----------|------------|------------|----------|--------|
| Galaxy bispectrum f_NL | Matter bounce | f_NL = -35/8 (parameter-free) | SPHEREx | ~2028 | **FLAGSHIP** |
| PBH dark matter | Asymmetric matter bounce | Asteroid-mass PBHs, f_PBH ~ 0.001-1 | LISA, microlensing | ~2035 | Viable |
| Induced GW spectrum | Matter bounce -> PBH | f^2 IR scaling, gamma = 3 | NANOGrav/PTA | NOW | **0.48-sigma consistent (Paper 3 §6 v2b: gamma = 3.20 +/- 0.42)** |
| Bounce -> DE unification | Quintom bounce | w(z) crosses -1 | DESI DR2 | NOW | Theoretical channel (Paper 1 §VII.H: this program uses zero free w0-wa samples; the DESI DR2 2.8-4.2 sigma signal is treated as observational context, not a BigBounce-group result) |
| GW echoes | Ekpyrotic bounce (GUT-scale) | Oscillatory Omega_GW | CE/ET | ~2035 | Conditional |
| Perturbative safety | Cuscuton bounce | No strong coupling | Theoretical | Complete | Supporting |

## MCMC Results

- **w0-wa quintom:** theoretical channel only. Paper 1 §VII.H is explicit: zero free w0-wa samples among the 309,789 frozen posterior samples in this program. Earlier "P(quintom-B) = 98.6%" bookkeeping was fire-#21 confabulation (corrected fire #25). The DESI DR2 2.8-4.2 sigma w-crossing signal is cited as observational context; it is not a BigBounce-group MCMC result.
- **Delta_Neff:** Approximately 0 in all datasets
- **H0:** 67.68 (standard LCDM value)
- **Total posterior samples:** 424,181+ across 3 frozen dataset combinations

## Research Tracks

- **Track A (f_NL forecast):** Existing, Paper 2 ready. See [[fnl-prediction]].
- **Track B (quintom bounce-DE):** Key literature gap -- no f_NL computed for any quintom bounce. Opportunity: compute f_NL for Lee-Wick quintom bounce.
- **Track C (PBH + induced GW):** f_NL = -35/8 regulates abundance (Choudhury+ 2025). NANOGrav consistent (Papanikolaou 2025).
- **Track D (cuscuton):** Supporting evidence for perturbative safety. Discrimination table contrast.

## Key Literature

- Choudhury+ (2025), arXiv:2409.18983 -- f_NL = -35/8 as PBH regulator
- Papanikolaou (2025), arXiv:2504.11641 -- NANOGrav consistency with matter bounce
- Cai (2511.19994) -- Quintom bounce review
- Cai, Qiu, Piao, Li, Zhang (2007), arXiv:0704.1090 -- Original quintom bounce

## Connections

- Flagship prediction: [[fnl-prediction]]
- Supporting channel: [[birefringence]]
- Discrimination: [[bounce-vs-inflation]]
- Foundation: [[paper-1-spin-torsion]] (14 barriers)
- Chirality null result: [[pipeline-2-chirality]]
