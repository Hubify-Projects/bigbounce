---
title: Bounce vs Inflation Observational Discriminators
type: comparison
tags: [bounce, inflation, discriminator, fnl, birefringence, quintom]
last_updated: 2026-04-04
sources:
  - project-context/bounce_portfolio_strategy.md
  - project-context/CURRENT_STATUS.md
---

# Bounce vs Inflation

The observational discriminators between bounce cosmology and standard LCDM + inflation, and the current status of each test.

## Discrimination Table

| Observable | Bounce Prediction | Inflation Prediction | Current Data | Status |
|-----------|-------------------|---------------------|-------------|--------|
| f_NL (local) | -35/8 = -4.375 | ~0.01 | -0.9 +/- 5.1 (Planck) | Consistent with both. SPHEREx decisive (~2028). |
| w(z) crossing -1 | Yes (quintom bounce) | No (Lambda) | w0=-0.871, wa=-0.542 (2.3-sigma) | Favors bounce at 98.6% |
| GW spectral index gamma | 3.0 (matter bounce) | -- | 3.2 +/- 0.6 (NANOGrav) | 0.33-sigma consistent with bounce |
| CMB birefringence beta | 0.27 deg (ALP) | 0 | 0.342 +/- 0.094 deg (3.6-sigma) | 0.8-sigma from prediction |
| PBH abundance | Naturally regulated | Overproduction (fine-tuning) | Unconstrained | Theoretical advantage for bounce |
| Tensor-to-scalar r | Model-dependent | 0.003-0.06 | r < 0.036 (95%) | Not yet discriminating |
| Delta_Neff | ~0 (our MCMC) | ~0 | ~0 (all datasets) | Consistent with both |

## Current Scorecard

| Channel | Favors | Significance | Decisive? |
|---------|--------|-------------|-----------|
| w-crossing | Bounce (quintom) | 2.3-sigma | Not yet (need DESI DR2) |
| NANOGrav GW | Bounce (matter) | 0.33-sigma from prediction | Not yet (need more PTA data) |
| Birefringence | Bounce (ALP) | 3.6-sigma signal exists, 0.8-sigma from our prediction | Not yet (need LiteBIRD for 9-sigma) |
| f_NL | Undetermined | Within noise | SPHEREx will be decisive |
| PBH regulation | Bounce (theoretical) | Qualitative | Need LISA for quantitative |
| Perturbative safety | Bounce (cuscuton) | Established | Supporting only |

## The Decisive Test

**SPHEREx (~2028):** sigma(f_NL) ~ 0.7-1.0. If f_NL = -4.375, detection at 4-6 sigma. This single measurement would:
- Confirm or rule out the matter bounce f_NL prediction
- If confirmed: simultaneously validate PBH regulation and GW spectral shape
- If null: matter bounce ruled out, but quintom/ekpyrotic bounce models remain viable

## Model Discrimination (Among Bounce Models)

| Model | f_NL | w-crossing | GW echoes | Safety |
|-------|------|-----------|-----------|--------|
| Matter bounce | -35/8 (parameter-free) | No | No | Yes |
| Quintom bounce | Unknown (literature gap) | Yes | No | Yes |
| Cuscuton bounce | Different | No | No | Proven |
| Ekpyrotic bounce | ~0 | No | Yes (GUT-scale) | Conditional |
| Inflation | ~0.01 | No | No | Yes |

The quintom f_NL is the key literature gap. If quintom f_NL ~ -35/8 (expected since contraction dynamics similar), the prediction becomes even more robust.

## Connections

- f_NL details: [[fnl-prediction]]
- Birefringence details: [[birefringence]]
- Portfolio strategy: [[bounce-portfolio]]
- Data driving these tests: [[desi-dr1]], [[pipeline-1-tracer-purification]]
- Papers: [[paper-1-spin-torsion]], [[paper-2-fnl-forecast]]
