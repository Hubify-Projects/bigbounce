# Manuscript-Editing Readiness Memo

**Date:** 2026-03-12
**Status:** Two datasets frozen, one running, one pending

---

## 1. Frozen Datasets

| Dataset | Freeze Date | Samples | Local Path |
|---------|------------|---------|------------|
| full_tension | 2026-03-11 17:28 UTC | 175,545 | `reproducibility/cosmology/frozen/full_tension_20260311_1728/` |
| planck_bao_sn | 2026-03-12 19:54 UTC | 132,949 | `reproducibility/cosmology/frozen/planck_bao_sn_20260312_1954/` |

Both verified: SHA256 checksums pass, R-hat < 0.002, ESS > 4,600.

## 2. Currently Running

| Dataset | Status | Samples | Started |
|---------|--------|---------|---------|
| planck_only | RUNNING | 458+ (resuming) | 2026-03-12 19:58 UTC |
| planck_bao | PAUSED | 469 | — |

planck_only is expected to need ~20-30 hours to reach convergence. planck_bao will be resumed after planck_only freezes.

## 3. Physical Parameter Values Safe to Quote

**YES — safe to quote now (two datasets):**

| Parameter | full_tension | planck_bao_sn | Safe? |
|-----------|-------------|---------------|-------|
| H0 | 67.68 ± 1.06 | 67.79 ± 1.09 | YES |
| delta_neff | -0.020 ± 0.169 | +0.065 ± 0.17 | YES |
| tau | 0.054 ± 0.007 | 0.056 ± 0.007 | YES |
| sigma8 | 0.803 ± 0.008 | 0.812 ± 0.009 | YES |
| omegam | 0.308 ± 0.005 | 0.312 ± 0.006 | YES |
| S8 | 0.814 ± 0.008 | 0.831 ± 0.018 | YES |

These values are final for full_tension and planck_bao_sn. They will not change.

**Caveat:** The planck_only and planck_bao columns are still pending. Final paper tables should leave space for these or note them as forthcoming.

## 4. Figures and Tables Ready for Manuscript

### Ready now:
- `paper/figures/vacuum_scale_sensitivity.pdf` — Theory audit: 4-panel sensitivity scan
- `paper/figures/cosmology_dataset_comparison_two_frozen.pdf` — 3-panel H0/dNeff/S8 comparison
- `paper/figures/fig_dneff_viability_two_frozen.pdf` — ΔNeff posteriors with SM/BBN/ACT constraints
- `research/final_paper_prep/master_cosmology_results_table.md` — Master results table (2/4 populated)

### Ready but will be updated:
- All comparison figures will gain planck_only and planck_bao data points once those freeze
- Results table will be completed

### Not yet created:
- Triangle/corner plots from frozen chains (can be generated on demand)
- Full GetDist 1D/2D posterior plots

## 5. Manuscript Sections Editable Now

| Section | Editable? | Notes |
|---------|-----------|-------|
| Abstract | PARTIAL | Can draft; final numbers will update when all datasets freeze |
| Introduction | YES | No dataset-specific numbers |
| Theory (Secs 2-4) | YES | Theory audit complete; framework validated |
| Fine-tuning discussion | YES | Sensitivity scan results are final |
| Dimensional consistency | YES | Audit complete (10/12 + 2 noted) |
| Limit behavior | YES | All 5 limits verified |
| MCMC methodology | YES | Same across all datasets |
| Results — full_tension | YES | Frozen, values final |
| Results — planck_bao_sn | YES | Frozen, values final |
| Results — planck_only | NO | Still running |
| Results — planck_bao | NO | Still paused |
| Cross-dataset comparison | PARTIAL | Can compare 2; final version needs all 4 |
| ΔNeff interpretation | PARTIAL | Core finding stable (consistent with SM); full comparison needs all datasets |
| Conclusions | PARTIAL | Main conclusions stable; quantitative summary needs all datasets |
| Figures | PARTIAL | Draft versions ready; final versions after all datasets |

## 6. What Must Wait

1. **planck_only freeze** (~20-30h from now) — then resume planck_bao
2. **planck_bao freeze** (~20-30h after that) — then final results
3. **Final cross-dataset comparison** — needs all 4 datasets
4. **Final abstract/conclusions** — needs all 4 datasets for complete quantitative summary
5. **Submission-ready PDF** — needs all figures finalized

## Recommendation

**Begin manuscript editing now** on:
- All theory sections (derivation, fine-tuning, limits, dimensional consistency)
- MCMC methodology section
- full_tension and planck_bao_sn results sections
- Draft the cross-dataset comparison framework (2/4 datasets as proof of concept)

Leave placeholder markers `[PENDING: planck_only]` and `[PENDING: planck_bao]` where needed.

## Theory Audit Integration Points

The following theory audit outputs are ready for manuscript integration:

1. **Derivation classification** (Tier 1/2/3) → new subsection or appendix material
2. **Fine-tuning improvement** (10^120 → 10^5) → Discussion section, with careful caveats about N_tot
3. **Vacuum sensitivity figure** → Figure in Results or Discussion
4. **Limit behavior table** → Appendix or inline table
5. **Dimensional consistency** → Methodology or Appendix

See `theory_results_integration_note.md` and `theory_claims_do_and_do_not_support.md` for detailed guidance.
