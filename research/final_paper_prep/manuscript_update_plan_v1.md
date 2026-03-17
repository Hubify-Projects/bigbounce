# Manuscript Update Plan v1 -- arxiv/main.tex

**Date:** 2026-03-12
**Target version:** v1.3.0 -> v1.5.0
**Status:** Two frozen datasets available; two datasets still running/paused

## Frozen Datasets

| Parameter   | full_tension               | planck_bao_sn              |
|-------------|----------------------------|----------------------------|
| H0          | 67.68 +/- 1.06             | 67.79 +/- 1.09             |
| dNeff       | -0.020 +/- 0.169           | +0.065 +/- 0.17            |
| sigma8      | 0.803 +/- 0.008            | 0.812 +/- 0.009            |
| omegam      | 0.308 +/- 0.005            | 0.312 +/- 0.006            |
| tau         | 0.054 +/- 0.007            | 0.056 +/- 0.007            |
| S8          | 0.814 +/- 0.008            | 0.831 +/- 0.018            |

**Pipeline:** Cobaya v3.6.1 independent verification.

## Pending Datasets

| Dataset      | Status  |
|--------------|---------|
| planck_only  | RUNNING |
| planck_bao   | PAUSED  |

## Original Manuscript Values (v1.3.0, Fisher-matrix / v3.5 analysis)

- H0 = 69.2 +/- 0.8
- sigma8 = 0.785 +/- 0.016
- 236,622 samples, 64 chains

## Theory Audit Summary

- Dimensional consistency: 10/12
- Limit checks: 5/5
- Monte Carlo sensitivity scan: 10^5 tuning, N_tot dominant (Spearman |rho_s| = 0.996)
- Viable fraction from 100K-sample scan: 2.2%

---

## Section-by-Section Plan

### Abstract (lines 60-66)

- **UPDATE:** Replace "236,622 samples, 64 chains" with actual frozen sample counts from full_tension and planck_bao_sn runs.
- **UPDATE:** Add two-dataset comparison narrative (delta_neff consistent with zero in both frozen datasets).
- **KEEP:** Original analysis values (H0 = 69.2) as the original results; they remain the primary Fisher-matrix predictions.
- **ADD:** Independent verification results showing consistency with Standard Model (dNeff straddles zero).
- **PENDING:** planck_only, planck_bao results -- leave placeholder or omit until frozen.

### Executive Summary Table (lines 94-109)

- **UPDATE:** Add a verification results column or footnote citing the two frozen datasets.
- **PENDING:** Final cross-dataset comparison cannot be completed until planck_only and planck_bao are frozen.

### Section 7 -- Cosmological Fits (lines 652+)

- **UPDATE:** MCMC configuration paragraph with frozen dataset details (sampler settings, convergence criteria, chain lengths).
- **UPDATE:** Verification subsection with full_tension and planck_bao_sn frozen values (table above).
- **ADD:** New results table with both frozen datasets side by side, plus [PENDING] columns for planck_only and planck_bao.
- **INSERT:** `cosmology_dataset_comparison_two_frozen.pdf` figure showing parameter posteriors for both frozen datasets.
- **INSERT:** `fig_dneff_viability_two_frozen.pdf` figure showing dNeff viability across dataset combinations.
- **PENDING:** planck_only and planck_bao columns marked [PENDING] in table and figure.

### Fine-Tuning Discussion (lines 752-777)

- **UPDATE:** Add Monte Carlo sensitivity scan results (100K samples, viable fraction 2.2%).
- **INSERT:** `vacuum_scale_sensitivity.pdf` figure illustrating the tuning landscape.
- **UPDATE:** Strengthen N_tot dominance claim with Spearman |rho_s| = 0.996 from sensitivity scan.

### Discussion (lines 938+)

- **ADD:** Brief paragraph on limit behavior checks (5/5 pass: GR recovery, flat-space, zero-torsion, high-energy, low-energy).
- **UPDATE:** Fine-tuning narrative with scan quantification (2.2% viable fraction, 10^5 tuning, N_tot dominant).

### Conclusions (lines 1119+)

- **UPDATE:** Verification paragraph with frozen values from both datasets.
- **UPDATE:** Fine-tuning paragraph with scan results.
- **PENDING:** Full cross-dataset narrative deferred until planck_only and planck_bao freeze.

### Appendix B -- Parameter Summary (lines 1201+)

- **UPDATE:** Table with frozen dataset values (full_tension, planck_bao_sn).
- **PENDING:** planck_only, planck_bao values to be inserted when frozen.

### Appendix K -- Claims Classification (lines 1547+)

- **UPDATE:** Add claims from theory audit (dimensional consistency 10/12, limit checks 5/5).
- **UPDATE:** delta_neff status: consistent with zero in both frozen datasets; does not support BSM physics claim.

### Version/Date

- **UPDATE:** v1.3.0 -> v1.5.0
- **UPDATE:** Date -> 2026-03-12
- **UPDATE:** Reproducibility URLs to point to v1.5.0 tag/release.

---

## Figures to Insert

| Figure file                                  | Target location        |
|----------------------------------------------|------------------------|
| cosmology_dataset_comparison_two_frozen.pdf   | Section 7              |
| fig_dneff_viability_two_frozen.pdf            | Section 7              |
| vacuum_scale_sensitivity.pdf                  | Section 7 or Discussion|

---

## Values Safe to Quote Now

All values from the two frozen datasets listed in the table at the top of this document:
- full_tension: H0 = 67.68 +/- 1.06, dNeff = -0.020 +/- 0.169, sigma8 = 0.803 +/- 0.008, omegam = 0.308 +/- 0.005, tau = 0.054 +/- 0.007, S8 = 0.814 +/- 0.008
- planck_bao_sn: H0 = 67.79 +/- 1.09, dNeff = +0.065 +/- 0.17, sigma8 = 0.812 +/- 0.009, omegam = 0.312 +/- 0.006, tau = 0.056 +/- 0.007, S8 = 0.831 +/- 0.018

## Values That Must Remain [PENDING]

- planck_only results (currently RUNNING)
- planck_bao results (currently PAUSED)

Do not quote these in the manuscript until their chains are frozen and validated.
