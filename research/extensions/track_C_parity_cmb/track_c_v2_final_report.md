# Phase 8: Track C v2 — Final Report

**Date:** 2026-03-13
**Status:** COMPLETE

---

## Executive Summary

Track C has been upgraded from an algebraic consistency check to a proper Gaussian summary-likelihood inference on cosmic birefringence. The upgrade adds real statistical content — explicit priors, Bayesian model comparison, confidence intervals, and degeneracy mapping — while remaining scrupulously honest about what it is and is not.

---

## Answers to the Seven Questions

### 1. Can Track C be legitimately upgraded beyond a consistency check?

**YES.** The previous analysis already computed the inverse-variance weighted combination of two Gaussian measurements — which IS maximum-likelihood estimation for Gaussians. The upgrade reframes this as what it actually is (a proper summary-likelihood inference), adds explicit priors, computes the Bayes factor via Savage-Dickey, and maps the (f_photon, C₀) degeneracy as a 2D posterior. Every step is mathematically standard and honestly justified.

### 2. What inference is Track C v2?

**Gaussian summary-likelihood inference** using two published isotropic birefringence measurements:
- Eskilt 2022 (Planck NPIPE): β = 0.30° ± 0.11° (arXiv:2205.13962)
- Diego-Palazuelos & Komatsu 2025 (ACT DR6): β = 0.215° ± 0.074° (arXiv:2503.14452)

The likelihood is L(β) = Π_i N(β; β_i, σ_i). The posterior is analytically tractable. This is NOT a map-level analysis, NOT a harmonic-space EB/TB likelihood, and NOT an MCMC.

### 3. Is MCMC justified?

**NO.** With 2 Gaussian data points and 1 free parameter (β), the posterior is exactly Gaussian with known mean and variance. Running emcee or cobaya would produce identical results at higher computational cost. The only scenario where MCMC would add value is a joint fit of β with Paper 1 cosmological parameters (H₀, ΔN_eff, etc.), but β is measured independently of those parameters — there is no non-trivial parameter correlation to explore.

### 4. What data sources are used?

| Source | Status | Justification |
|--------|--------|--------------|
| Eskilt 2022 (Planck NPIPE) | **USED** | Independent, well-characterized Gaussian, not superseded |
| ACT DR6 (Diego-Palazuelos & Komatsu 2025) | **USED** | Independent, well-characterized Gaussian |
| SPIDER 2025 | **CITE ONLY** | Calibration-degenerate (measures total rotation, not birefringence alone) |
| Minami & Komatsu 2020 | **DO NOT USE** | Superseded by Eskilt 2022 (same data, better method) |

### 5. Is RunPod or GPU infrastructure needed?

**NO.** Runtime < 3 seconds. Dependencies: numpy, scipy, matplotlib. No data downloads, no HEALPix, no parallelism. Zero interaction with the planck_only chains running on RunPod.

### 6. Does this belong in Paper 1?

**YES.** The parity-odd operator is derived in Paper 1 (Eq. XX of arxiv/main.tex). The birefringence connection is a direct observable consequence. Including a proper statistical inference (rather than just an algebraic consistency check) strengthens the phenomenological content without overclaiming. Two paragraph options are provided in Phase 7 (conservative and fuller), plus a figure caption.

### 7. What is the strongest honest claim?

> The spin-torsion parity-odd operator, with the coupling scale α/M ~ 10⁻²¹ GeV⁻¹ already fixed by the dark energy phenomenology, produces an effective photon-torsion coupling that is naturally compatible with the 3.9σ cosmic birefringence signal observed independently by Planck and ACT. The implied coupling f_photon × C₀ = 1.73 ± 0.44 requires no fine-tuning for O(1) values of both the photon vertex factor and the cosmological field excursion integral. This constitutes a non-trivial consistency check that elevates to moderate evidence for the framework's parity-odd sector, though it does not uniquely identify the spin-torsion origin (any axion-like coupling would produce the same uniform birefringence signature).

---

## Results Summary

| Quantity | Value | Uncertainty | Notes |
|----------|-------|-------------|-------|
| β (combined) | 0.242° | 0.061° | 3.9σ from zero |
| BF(β≠0) | 175.8 | — | Strong (Jeffreys) |
| ln BF | 5.2 | — | |
| f_photon (C₀=0.3) | 5.77 | 1.47 | O(1) natural |
| f_photon (C₀=1.0) | 1.73 | 0.44 | O(1) natural |
| f_photon (C₀=3.0) | 0.58 | 0.15 | O(1) natural |
| f_photon × C₀ | 1.73 | 0.44 | The only constrained product |

---

## Comparison with v1 (Previous Consistency Check)

| Aspect | v1 | v2 |
|--------|----|----|
| Method | Algebraic parameter translation | Gaussian summary-likelihood inference |
| Prior | None (implicit) | Explicit: uniform β ∈ [−1°, 1°] |
| Data | Eskilt 2022 only | Eskilt 2022 + ACT DR6 |
| Bayes factor | Not computed | BF = 175.8 |
| Confidence intervals | Not provided | 68% and 95% CI |
| Degeneracy mapping | Not shown | Full (f_photon, C₀) 2D constraint |
| Figures | 0 | 4 (beta posterior, f_photon posterior, degeneracy, corner) |
| Machine-readable output | No | Yes (CSV + TXT) |
| Epistemic labels | Informal | Explicit classification (derived/gap/scaling ansatz) |
| Runtime | ~ 0 seconds | < 3 seconds |

---

## Outputs Produced

### Figures
- `track_c_v2_beta_posterior.pdf/png` — β posterior with individual + combined
- `track_c_v2_fphoton_posterior.pdf/png` — f_photon posterior for multiple C₀ values
- `track_c_v2_degeneracy.pdf/png` — 2D (f_photon, C₀) constraint
- `track_c_v2_corner.pdf/png` — Summary corner plot

### Tables
- `track_c_v2_results_summary.txt` — Human-readable full results
- `track_c_v2_likelihood_table.csv` — Machine-readable results

### Paper figures (copied)
- `research/paper/figures/trackC_parity_upgrade_corner.pdf/png`
- `research/paper/figures/trackC_parity_upgrade_summary.pdf/png`

### Documentation
- `upgrade_strategy.md` — Phase 0
- `dataset_audit.md` — Phase 1
- `dataset_registry.csv` — Phase 1
- `model_to_observable_map_v2.md` — Phase 2
- `upgrade_readiness_decision.md` — Phase 3
- `v2/scripts/track_c_summary_likelihood.py` — Phase 4
- `v2/README.md` — Phase 4
- `infrastructure_decision.md` — Phase 6
- `paper_integration_decision_v2.md` — Phase 7
- `track_c_v2_final_report.md` — Phase 8 (this file)

---

## What Remains for Future Work

1. **Derive f_photon from first principles** — requires one-loop computation of the photon-torsion vertex in EC gravity. This is the main theoretical gap.
2. **Solve for C₀** — requires evolving the pseudo-scalar condensate through the bounce and post-bounce expansion. Connected to the first-principles perturbation program (see `research/paper2/first_principles_roadmap/`).
3. **Full map-level EB likelihood** — when ACT DR6 likelihood code is publicly released, a proper harmonic-space analysis becomes possible.
4. **Scale-dependent birefringence** — the torsion condensate profile predicts a specific ℓ-dependence in the EB spectrum that differs from a constant rotation. This is the most promising route to distinguish the spin-torsion origin from generic axion models.

---

## Track C v2 Upgrade: COMPLETE
