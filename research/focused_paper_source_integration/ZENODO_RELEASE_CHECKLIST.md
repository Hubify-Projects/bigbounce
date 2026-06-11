# Zenodo Release Checklist — P2 (Testing the Matter Bounce with Primordial Non-Gaussianity)

**Action:** Houston must mint the Zenodo DOI via the GitHub–Zenodo webhook before arXiv submission.  
**Repo:** https://github.com/Hubify-Projects/bigbounce  
**Release tag to create:** `paper2-v1.7.49` (or the version at submission time)

---

## Files to include in the release archive

### Core analysis scripts (in `research/focused_paper_source_integration/`)
- `null_space_analysis.py` — 10,000-sample null-space scan; produces r = 0.85 ± 0.13 and r_cos distributions
- `c9g_bf_table_recompute.py` + output JSON — closed-form Bayes factor recompute (Table III)
- `c9k_gr_continuous_marginalization.py` + output JSON — continuous σ_GR marginalization (BF = 6.0)
- `c9l_sigma_theory_continuous_marginalization.py` + output JSON — continuous σ_theory marginalization (BF = 8.8/3.6)
- `appendix_A1_wick_doubling.py` — symbolic verification of −2 Im commutator identity

### Named JSON artifacts (in `research/focused_paper_source_integration/outputs/` or scripts/)
- `c9h_nullspace_significance_propagation.json` — per-sample 16th–84th percentile 4.4–6.2σ
- `c9i_epsilon_ratio_check.json` — ε-ratio basis check; verifies Cai coefficients not transplantable
- `c9j_bf_template_rescale.py` + output JSON — template-mismatch BF bookkeeping
- `phase3_fisher_overlap.json` — ℓ-space Fisher-overlap output (r = 0.878 ± 0.012)

### SDB Fisher script (in `h200_scripts/experiments/` or `research/focused_paper_source_integration/scripts/`)
- `c8_fnl_running_fisher.py` — joint (f_NL, n_fNL) SDB Fisher; produces σ(n_fNL) = 0.295/0.596

### Paper source
- `02_full_draft.tex` (the compiled source)
- `focused_paper_refs.bib`
- All figure PNGs: `fig1_shape_function.png`, `fig2_survey_comparison.png`, `fig3_kmin_cliff.png`, `fig4_decision_thresholds.png`, `fig5_inflation_comparison.png`
- `02_full_draft.pdf` (compiled PDF)

---

## Zenodo metadata

- **Title:** Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Sensitivity Recast and Forecasts, with a MegaMapper Outlook
- **Authors:** Houston Golden
- **Description:** Analysis code, Monte Carlo scripts, and shape-function evaluation routines for P2. Includes null-space scan, Bayes factor recompute, template overlap, and SDB Fisher scripts.
- **License:** CC-BY-4.0 (code) / CC-BY-4.0 (paper)
- **Keywords:** primordial non-Gaussianity, matter bounce, SPHEREx, bispectrum, bouncing cosmology
- **Related publication:** arXiv:XXXX.XXXXX (insert at submission)

---

## Steps

1. Create GitHub release `paper2-v1.7.49` (tag the commit at submission time)
2. Zenodo auto-imports the release via the connected GitHub webhook (https://zenodo.org/account/settings/github/)
3. Edit the Zenodo draft: add metadata above, confirm file list
4. Publish → copy the DOI (format: `10.5281/zenodo.XXXXXXX`)
5. Replace "DOI inserted at submission" placeholder in `02_full_draft.tex` Data and Code Availability section with the minted DOI
6. Recompile the paper and update the arXiv submission package

---

## Paper text placeholder (already inserted in 02_full_draft.tex)

> "…available at \url{https://github.com/Hubify-Projects/bigbounce/tree/main/research/} and archived at Zenodo (DOI inserted at submission)."

Replace "DOI inserted at submission" with the actual DOI before submitting to arXiv.
