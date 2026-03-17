# Pre-Audit Manuscript Report: v1.6.0-preaudit

**Date:** 2026-03-13
**PDF:** `arxiv/main.pdf` (35 pages, 1.92 MB)
**Compiler:** Tectonic (local)
**Undefined references:** 0
**BibTeX warnings:** 0

---

## Changes Made in This Pass

### Must-Fix Items (from manuscript_sync_audit.md)

| # | Issue | Resolution |
|---|-------|-----------|
| 1 | Total samples 175,545 → 176,840 | Updated in 4 locations: abstract (line 63), verification table (line 454), MCMC config (line 703), conclusions (line 1204) |
| 2 | Missing `corner_H0_sigma8_Neff.pdf` | Reference removed from Reproducibility appendix (line 1622). File cannot be generated locally (no GetDist). |
| 3 | BibTeX: missing journal in Shamir2024 | Added `journal = {arXiv preprint}` |
| 4 | BibTeX: empty author in ECTorsionDESI2025 | Added correct authors: Liu, Li, Xu, Biesiada, Wang (verified from arXiv:2507.04265) |

### Track C v2 Integration

The birefringence consistency check (Sec. 10.3) has been upgraded:

| Aspect | Before | After |
|--------|--------|-------|
| Method description | "inverse-variance weighting" | "Gaussian summary-likelihood consistency check" |
| Combined β | 0.24° ± 0.06° | 0.242° ± 0.061° (more precise) |
| Bayes factor | Not mentioned | BF ≈ 176 (Savage-Dickey) |
| Prior | Implicit | Explicit: uniform β ∈ [−1°, 1°] |
| f_photon constraint | f_photon ≈ 1.7 ± 0.4 | f_photon × C₀ = 1.73 ± 0.44 |
| Degeneracy | Not mentioned | (f_photon, C₀) hyperbolic degeneracy noted |
| Generic-model caveat | Present | Strengthened: cites Carroll 1998, notes distinguishing test |
| Framing | "consistency check" | "consistency check" (preserved per instructions) |

Updated in: Sec. 10.3 (main text + figure caption), Conclusions, Claims Classification table.

### Other Updates

- Paper date: March 12 → March 13, 2026
- Version tag: v1.6.0 → v1.6.0-preaudit
- Reproducibility appendix: Cobaya version clarified (v3.5 original / v3.6.1 verification)

---

## Figures Included (11)

| # | File | Type | Data Source | Current? |
|---|------|------|-------------|----------|
| 1 | figure1_lqg_holst_derivation_enhanced.png | Schematic | Theory | YES |
| 2 | figure2_galaxy_spin_comprehensive.png | Schematic | Surveys | YES |
| 3 | figure_3a_tension_resolution.png | Schematic | Literature | YES |
| 4 | fig_dneff_viability_two_frozen.pdf | Generated | Both frozen chains | YES |
| 5 | cosmology_dataset_comparison_two_frozen.pdf | Generated | Both frozen chains | YES |
| 6 | figure3b_tensions_resolution_comprehensive.png | Schematic | Literature | YES |
| 7 | figure6_parameter_naturalness.png | Schematic | Theory | YES |
| 8 | vacuum_scale_sensitivity.pdf | Generated | Monte Carlo scan | YES |
| 9 | consistency_window_birefringence.pdf | Generated | Published β values | YES |
| 10 | figure4_distance_impact.png | Schematic | Theory | YES |
| 11 | figure5_rotation_expansion.png | Schematic | Theory | YES |

**All 11 figures present in `arxiv/figures/` and verified.**

---

## Tables Included (13)

| # | Label | Caption |
|---|-------|---------|
| 1 | tab:summary | Executive summary of key results |
| 2 | tab:surveys | Galaxy spin asymmetry detections |
| 3 | tab:verification | Independent verification (frozen MCMC chains) |
| 4 | tab:H0data | Hubble constant measurements |
| 5 | tab:S8data | σ₈/S₈ measurements |
| 6 | tab:modelcomp | Bayesian model comparison |
| 7 | tab:ic | Information criteria across datasets |
| 8 | tab:finetuning | Fine-tuning comparison |
| 9 | tab:errorbudget | Combined error budget |
| 10 | tab:limits | Limit behavior |
| 11 | tab:params | Complete parameter summary |
| 12 | tab:fullcomp | (embedded) Full-multipole χ² values |
| 13 | tab:claims | Claims classification |

---

## Datasets Frozen

| Dataset | Samples | R̂−1 | Freeze Date | Status |
|---------|---------|------|-------------|--------|
| full_tension | 176,840 | < 0.001 | 2026-03-11 | FROZEN ✓ |
| planck_bao_sn | 132,949 | < 0.002 | 2026-03-12 | FROZEN ✓ |

## Datasets Pending

| Dataset | Status | ETA |
|---------|--------|-----|
| planck_only | In progress (RunPod) | ~Mar 19–20 |
| planck_bao | Not yet started | After planck_only |

---

## Remaining Placeholders

| Location | Placeholder |
|----------|------------|
| Tab. 3, line 458 | `Planck-only: [PENDING---in progress]` |
| Tab. 3, line 459 | `Planck+BAO: [PENDING---not yet started]` |
| App. B footnote, line 1321 | `Two additional dataset combinations... are [PENDING]` |

---

## Remaining Issues

### None Critical

| # | Issue | Severity | Notes |
|---|-------|----------|-------|
| 1 | Overfull/underfull hbox warnings | Cosmetic | ~90 warnings, standard for revtex4-2 twocolumn |
| 2 | 4 uncited bib entries | Low | CMBS4_2019, Euclid2024, LSST2019, PantosS82026 — kept for potential future use |
| 3 | planck_bao_sn convergence_report.txt column scramble | Internal | Does not affect manuscript; MANIFEST has correct values |
| 4 | full_tension MANIFEST.md parameter table scrambled | Internal | Does not affect manuscript; CORRECTED JSON is authoritative |
| 5 | GetDist plots for planck_bao_sn not generated | Deferred | Needs RunPod; not referenced in manuscript |

---

## Verification Checklist

- [x] All figures present and referenced correctly
- [x] All tables present and referenced correctly
- [x] All citations resolve (0 undefined)
- [x] BibTeX compiles with 0 warnings
- [x] Sample counts match frozen artifact packs
- [x] Parameter values match frozen chains to stated precision
- [x] Track C v2 birefringence results integrated
- [x] Theory audit results reflected (dimensional consistency, limits, fine-tuning)
- [x] Placeholders clearly marked for pending datasets
- [x] Deprecated galaxy_spin_data.csv NOT referenced
- [x] Reproducibility section updated
- [x] PDF compiles cleanly (35 pages)

---

## Section Structure (Verified)

1. Introduction
2. Theoretical Framework
3. Observational Signatures and Evidence
4. Enhanced Theoretical Derivations
5. Data Methods: Galaxy Spin Analysis
6. Data Methods: CMB E-B Analysis
7. Cosmological Fits and Model Comparison
8. Systematic Analysis
9. Falsification Criteria
10. Related Work
11. Discussion (includes Birefringence Consistency Check)
12. Limitations and Future Directions
13. Conclusions (includes Data & Code Availability)
14. Acknowledgments
Appendices A–K (Notation, Parameters, Galaxy Spin, Likelihood, Nieh-Yan, Rotation, Error Analysis, Dimensions, Reproducibility, Claims)

---

## Summary

The manuscript is ready for external scientific audit. All frozen results are correctly reflected, all figures and tables are present and current, and the Track C v2 birefringence analysis has been integrated with conservative framing. The only remaining gaps are the two pending MCMC dataset combinations (planck_only, planck_bao), which are clearly marked as [PENDING] in the text.

**PDF path:** `/Users/houstongolden/Desktop/CODE_2026/bigbounce/arxiv/main.pdf`
**Version:** v1.6.0-preaudit
**Pages:** 35
**Figures:** 11
**Tables:** 13
**Citations:** ~60 unique references
