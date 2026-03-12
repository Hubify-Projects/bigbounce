# Phase 3 Decision Report — Paper Preparation Workflow

**Date:** 2026-03-11 ~18:15 UTC
**Status:** All 7 steps complete

---

## Step 1: full_tension Result Validation — PASS

- Recomputed all statistics from frozen chain files
- Cross-checked against `full_tension_physical_parameters.md` — 7/7 exact match
- Triangle plot and 1D posteriors visually confirmed with correct parameter mapping
- All convergence gates verified (9/9 pass, worst R-1 = 0.001)
- **Report:** `research/final_paper_prep/full_tension_result_validation.md`

## Step 2: Final Parameter Table Template — DONE

- Template with full_tension values filled, placeholders for 3 pending datasets
- Includes dataset specifications, formatting notes, ΛCDM reference values
- **File:** `research/final_paper_prep/final_parameter_table_template.md`

## Step 3: Publication-Quality Figures — DONE (4 new figures)

| Figure | File | Description |
|--------|------|-------------|
| Convergence diagnostics | `paper/figures/full_tension_final_convergence.png` | R-hat and ESS vs samples (3 key params) |
| ESS growth curves | `paper/figures/full_tension_final_ess_growth.png` | All 7 parameters, targets marked |
| Correlation heatmap | `paper/figures/full_tension_final_correlation.png` | 7×7 weighted correlation matrix |
| Dataset comparison | `paper/figures/cosmology_dataset_comparison_draft.png` | H0, dNeff, S8 panels with placeholders |

Plus existing figures from previous session:
- `paper/figures/full_tension_triangle.png` — 7-parameter triangle plot
- `paper/figures/full_tension_posteriors.png` — 1D marginalized posteriors

### Notable findings from new figures:
- **H0-dNeff correlation:** r = 0.95 (very strong positive), confirming the expected degeneracy
- **dNeff-Omega_m:** r = -0.57 (moderate negative)
- **S8 is weakly correlated** with most parameters (r < 0.3 except sigma8)
- All ESS curves cross their targets well before the final sample count

## Step 4: Cross-Dataset Comparison Figure — DONE

- 3-panel draft (H0, dNeff, S8) with full_tension data
- Pending datasets shown as gray placeholder markers
- SH0ES and DES Y3 reference bands included
- Ready to drop in planck_bao_sn values when frozen
- **File:** `paper/figures/cosmology_dataset_comparison_draft.png`

## Step 5: Dataset Explorer Update — DONE

- Added `mcmc_full_tension_frozen` entry to `public/data/dataset_catalog.json`
- Includes full metadata: 175,545 samples, 6 chains, checksum, parameter preview
- Total datasets: 33

## Step 6: planck_bao_sn Monitoring — RUNNING

| Metric | Value |
|--------|-------|
| Chains alive | 6/6 (8 cobaya processes) |
| Total samples | 4,484 |
| Throughput | ~6,958 accepted/hr |
| Bottleneck | delta_neff ESS (75/2000) |
| Estimated freeze | 2026-03-12 11:00-14:00 UTC (~17h) |

Preliminary delta_neff = +0.071 (vs full_tension -0.020). The positive shift is expected when removing H0 and S8 tension priors. This early estimate is unreliable.

## Decisions & Recommendations

1. **Do not edit manuscript yet.** Wait for planck_bao_sn to freeze.
2. **Next check-in:** ~6h from now (2026-03-12 00:00 UTC) for better planck_bao_sn projections.
3. **planck_only resumption:** After planck_bao_sn freezes (~Mar 12 afternoon). Estimated planck_only freeze: ~Mar 14.
4. **Pod status:** Running fine at $1.12/hr. Cost since last check: ~$0.72 (0.6h). Total run cost estimate for planck_bao_sn: ~$19 (17h).
5. **All frozen artifacts intact.** No modifications to full_tension data.

## Complete Figure Inventory

| File | Type | Status |
|------|------|--------|
| `paper/figures/full_tension_triangle.png/pdf` | Triangle plot | Final |
| `paper/figures/full_tension_posteriors.png/pdf` | 1D posteriors | Final |
| `paper/figures/full_tension_final_convergence.png` | Convergence | Final |
| `paper/figures/full_tension_final_ess_growth.png` | ESS growth | Final |
| `paper/figures/full_tension_final_correlation.png` | Correlations | Final |
| `paper/figures/cosmology_dataset_comparison_draft.png` | Dataset comparison | Draft (needs planck_bao_sn) |
| `paper/figures/fig_dneff_viability_draft.png/pdf` | dNeff viability | Draft (needs planck_bao_sn) |
