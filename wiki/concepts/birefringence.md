---
title: Cosmic Birefringence
type: concept
tags: [birefringence, alp, cmb, polarization, act]
last_updated: 2026-04-04
sources:
  - project-context/post_sweep_followon_plan.md
  - project-context/active_pods_and_pipelines.md
---

# Cosmic Birefringence

ALP-mediated rotation of CMB polarization plane. Supporting (not decisive) evidence channel for bounce cosmology.

## The Prediction

**beta = 0.27 deg**

Axion-like particles (ALPs) coupled to the torsion field in Einstein-Cartan gravity rotate the CMB polarization angle by beta = 0.27 deg. This matches the observed 3.6-sigma signal: beta_obs = 0.342 +/- 0.094 deg (Minami & Komatsu 2020, from Planck HFI data).

## ACT H200 Measurement

An independent measurement was attempted using ACT DR6 IQU polarization data (5.3 GB):

| Metric | Value |
|--------|-------|
| Measured beta | 17.4 deg +/- 12.1 deg |
| Status | Systematic-dominated |
| Dominant systematic | Foreground contamination |
| Estimator used | Simple FFT |

The result is not scientifically meaningful. The simple FFT estimator is insufficient for sub-degree birefringence measurement.

## Required Improvements

1. **Galactic mask + point source mask** -- remove foreground contamination
2. **NaMaster or PolSpice** -- proper pseudo-Cl estimation with mode-coupling correction
3. **Cross-frequency cleaning** -- separate CMB from dust and synchrotron
4. **Multipole-by-multipole estimator** -- instead of broadband FFT

## Simulation Validation

The birefringence pipeline was validated on simulations:
- Injected beta = 0.27 deg
- Recovered beta = 0.261 +/- 0.037 deg (unbiased)
- Caught a factor-of-2 bug in the standard formula during validation

## Future Tests

- **LiteBIRD** (launch ~2032): sigma(beta) ~ 0.03 deg, giving ~9-sigma test of the 0.27 deg prediction
- **Simons Observatory**: improved polarization sensitivity
- Proper ACT/Planck analysis with NaMaster would give sigma ~ 0.1 deg

## Connections

- ACT data: [[act-dr6]]
- Planck data: [[planck-cmb]]
- Prediction source: [[paper-1-spin-torsion]]
- Portfolio context: [[bounce-portfolio]] (supporting channel)
- Discrimination: [[bounce-vs-inflation]]
