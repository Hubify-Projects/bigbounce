# Manuscript Update Summary — v1.5.0

**Date:** 2026-03-12
**Previous version:** v1.3.0
**New version:** v1.5.0

---

## What Was Updated

### Abstract
- Replaced "236,622 samples, 64 chains" with frozen dataset specifics (175,545 full-tension + 132,949 Planck+BAO+SN)
- Added Monte Carlo sensitivity scan mention (100K samples, 10^120 → 10^5 reduction)

### Executive Summary (Table I)
- Added verification footnote linking to frozen chain results (H0=67.68/67.79)

### MCMC Configuration (Sec VII.B)
- Added Cobaya v3.6.1 verification details with frozen dataset counts
- Updated reproducibility URL to v1.5.0

### NEW: Independent Verification Results (Sec VII, new subsection)
- New `\subsection{Independent Verification Results}` with:
  - Table `\ref{tab:verification}`: Both frozen dataset parameter values
  - [PENDING] markers for planck_only and planck_bao
  - Narrative: ΔNeff consistent with zero in both datasets, H0 consistent with Planck ΛCDM
  - Two new figures inserted

### Fine-Tuning Discussion
- Added Monte Carlo scan quantification: 2.2% viable, Spearman |ρ_s| = 0.996 for N_tot
- Inserted `vacuum_scale_sensitivity.pdf` figure

### NEW: Limit Behavior and Internal Consistency (Discussion, new subsection)
- Table `\ref{tab:limits}`: 5 limit checks (all pass)
- Dimensional analysis summary: 10/12 consistent + 2 scaling ansatze noted

### Conclusions
- Updated observational context with frozen dataset results
- Updated fine-tuning paragraph with scan numbers

### Limitations (Sec XIII)
- Updated Fisher-matrix text: now notes full posteriors available from verification

### Future Directions (Sec XIV)
- Updated ΔNeff range: original 0.1–0.5 noted as unsupported by full posterior; frozen results cited

### Appendix B (Parameter Summary)
- Added footnotes linking original Fisher-matrix best-fit values to frozen verification values
- Added verification results paragraph below table

### Appendix K (Claims Classification)
- Updated H0 and σ8 entries with both original and verification values
- Updated ΔNeff from "≈0.3" to frozen verification values (both consistent with zero)
- Added verification rows

### Version References
- All `v1.3.0` → `v1.5.0` throughout (4 occurrences)
- `version.json` updated

---

## New Figures Added to arxiv/figures/

| Figure | Description |
|--------|-------------|
| `cosmology_dataset_comparison_two_frozen.pdf` | 3-panel: H0, ΔNeff, S8 comparison with reference bands |
| `fig_dneff_viability_two_frozen.pdf` | 2-panel: ΔNeff posteriors + normalized parameter shifts |
| `vacuum_scale_sensitivity.pdf` | 4-panel: Monte Carlo sensitivity scan |

---

## What's Still Pending

| Item | Status | When |
|------|--------|------|
| planck_only results | RUNNING | ~20-30h to convergence |
| planck_bao results | PAUSED | After planck_only freezes |
| Final 4-dataset comparison | Waiting | After all 4 freeze |
| Complete Appendix B table | Waiting | After all 4 freeze |
| PDF compilation | Blocked | No LaTeX installation on local machine |
| Corner plots from frozen chains | On demand | Can generate anytime |

---

## Validation Checks

- Braces: BALANCED
- begin/end pairs: 152/152 matched
- v1.3.0 remnants: 0
- [PENDING] markers: 3 (correct — planck_only × 2, planck_bao × 1)
- Figures: 10 total (3 new)
- Tables: 13 total (2 new)

---

## Deliverable Locations

| Deliverable | Path |
|-------------|------|
| Manuscript | `arxiv/main.tex` |
| Version tracking | `version.json` |
| Revision tracker | `project-context/peer-reviews/REVISION_TRACKER.md` |
| Theory claims guide | `research/final_paper_prep/theory_claims_do_and_do_not_support.md` |
| Integration note | `research/final_paper_prep/theory_results_integration_note.md` |
| Editing readiness memo | `research/final_paper_prep/manuscript_editing_readiness_after_two_frozen.md` |
| Master results table | `research/final_paper_prep/master_cosmology_results_table.md` |
| Update plan | `research/final_paper_prep/manuscript_update_plan_v1.md` |
| Frozen full_tension | `reproducibility/cosmology/frozen/full_tension_20260311_1728/` |
| Frozen planck_bao_sn | `reproducibility/cosmology/frozen/planck_bao_sn_20260312_1954/` |
| New figures | `arxiv/figures/{cosmology_dataset_comparison_two_frozen,fig_dneff_viability_two_frozen,vacuum_scale_sensitivity}.pdf` |
