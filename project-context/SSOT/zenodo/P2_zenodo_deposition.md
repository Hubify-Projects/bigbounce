# Zenodo Deposition Record — P2
## Paper: Testing the Matter Bounce with Primordial Non-Gaussianity

**Version:** v1.7.60 (submission version; v1.7.61 is a ship-mode body-text pass — use whichever is current at submission)
**Prepared:** 2026-06-13 (HD-11 DO-NOW directive)

---

## 1. Title

Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook

---

## 2. Authors

| Name | Email | Affiliation |
|------|-------|-------------|
| Houston Golden | houston@hubify.com | Independent Researcher, Los Angeles, California, USA |

---

## 3. Description (Abstract)

A matter-dominated contracting phase preceding a nonsingular bounce produces a minimally parameterized local-type non-Gaussianity fnl_local = -35/8 = -4.375 (Cai et al. 2009), in the scalar-only matter-bounce class defined by stated assumptions — in particular: no prolonged post-bounce inflation, negligible fermion-sourced torsion during contraction, and faithful third-order bispectrum transmission through the bounce. We forecast tests of this prediction with SPHEREx (launched March 2025, primary survey through ~2027, first PNG-suitable release expected ~2028) and the proposed MegaMapper via scale-dependent bias and the galaxy bispectrum. We audit the Cai et al. bispectrum, establishing via the in-in operator identity that their intermediate epsilon-order decomposition is exactly half the full result, fixing -35/8 as the correct Planck-convention normalization. We quantify the template mismatch between the matter-bounce and local templates: a local estimator recovers 84%-88% of the bounce signal across noise-weighting schemes. The Heinrich et al. multi-tracer galaxy bispectrum forecast achieves sigma(fnl_local) ~ 0.7. After template-mismatch correction we obtain bispectrum-only 5.2-5.5 sigma at fnl = -35/8, reducing to a realistic ~2.6-5 sigma after the systematic budget (mismatch, epsilon-correction, polynomial-null-space scatter, photometric-z degradation, PNG-bias marginalization, and relativistic projection). A closed-form Bayesian comparison validated across three independent 10^5-realization Monte Carlo ensembles finds that a SPHEREx detection near fnl = -4.375 favors the bounce over tuned multifield competitors at Bayes factor BF ~ 9-14. MegaMapper could reach sigma(fnl) ~ 0.5 ideally, projecting an illustrative 3-7 sigma envelope. A SPHEREx null would disfavor the quasi-dust matter bounce benchmark at the same ~2.6-5 sigma post-systematic-budget level as a detection.

---

## 4. Keywords

- primordial non-Gaussianity
- matter bounce
- bouncing cosmology
- SPHEREx
- bispectrum
- MegaMapper
- scale-dependent bias
- fnl forecast
- template mismatch
- Bayes factor
- cosmology
- large-scale structure

---

## 5. License

**CC-BY-4.0** (Creative Commons Attribution 4.0 International)

*Existing Zenodo Release Checklist at `research/focused_paper_source_integration/ZENODO_RELEASE_CHECKLIST.md` specifies CC-BY-4.0 for both code and paper.*

---

## 6. Related Identifiers

| Relation | Identifier | Note |
|----------|-----------|------|
| isSupplementedBy | arXiv:XXXX.XXXXX | **PLACEHOLDER — insert real arXiv ID after submission** |
| isPartOf | arXiv:XXXX.XXXXX (P1A) | ECH no-go companion — insert P1A arXiv ID |
| isPartOf | arXiv:XXXX.XXXXX (P1B) | MCMC companion — insert P1B arXiv ID |
| isReferencedBy | arXiv:XXXX.XXXXX (P3) | Multi-survey anomaly catalog (multi-tracer fnl context) |

---

## 7. File Manifest

Files Houston should upload to Zenodo:

**Paper source files:**

| File | Path | Description |
|------|------|-------------|
| `paper2_arxiv_v1.7.60.tar.gz` | `research/focused_paper_source_integration/paper2_arxiv_v1.7.60.tar.gz` | **PRIMARY — arXiv submission tarball** |
| `02_full_draft.pdf` | `research/focused_paper_source_integration/02_full_draft.pdf` | Compiled PDF |
| `02_full_draft.tex` | `research/focused_paper_source_integration/02_full_draft.tex` | LaTeX source |
| `focused_paper_refs.bib` | `research/focused_paper_source_integration/focused_paper_refs.bib` | Bibliography |

**Figure files:**

| File | Path |
|------|------|
| `fig1_shape_function.png` | `research/focused_paper_source_integration/fig1_shape_function.png` |
| `fig2_survey_comparison.png` | `research/focused_paper_source_integration/fig2_survey_comparison.png` |
| `fig3_kmin_cliff.png` | `research/focused_paper_source_integration/fig3_kmin_cliff.png` |
| `fig4_decision_thresholds.png` | `research/focused_paper_source_integration/fig4_decision_thresholds.png` |
| `fig5_inflation_comparison.png` | `research/focused_paper_source_integration/fig5_inflation_comparison.png` |

**Analysis scripts and JSON artifacts (per ZENODO_RELEASE_CHECKLIST.md):**

| File | Path | Description |
|------|------|-------------|
| `null_space_analysis.py` | `research/focused_paper_source_integration/null_space_analysis.py` | 10,000-sample null-space scan |
| `c9g_bf_table_recompute.py` | `research/focused_paper_source_integration/c9g_bf_table_recompute.py` | BF table recompute |
| `c9k_gr_continuous_marginalization.py` | `research/focused_paper_source_integration/c9k_gr_continuous_marginalization.py` | Continuous sigma_GR marginalization |
| `c9l_sigma_theory_continuous_marginalization.py` | `research/focused_paper_source_integration/c9l_sigma_theory_continuous_marginalization.py` | Continuous sigma_theory marginalization |
| `appendix_A1_wick_doubling.py` | `research/focused_paper_source_integration/appendix_A1_wick_doubling.py` | Symbolic in-in commutator verification |
| `c9g_bf_table_recompute.json` | `research/focused_paper_source_integration/outputs/c9g_bf_table_recompute.json` | BF output |
| `c9h_nullspace_significance_propagation.json` | `research/focused_paper_source_integration/outputs/c9h_nullspace_significance_propagation.json` | Null-space significance |
| `c9i_epsilon_ratio_check.json` | `research/focused_paper_source_integration/outputs/c9i_epsilon_ratio_check.json` | Epsilon ratio check |
| `c9j_bf_template_rescale.json` | `research/focused_paper_source_integration/outputs/c9j_bf_template_rescale.json` | Template-mismatch BF |
| `c9k_gr_continuous_marginalization.json` | `research/focused_paper_source_integration/outputs/c9k_gr_continuous_marginalization.json` | GR marginalization output |
| `c9l_sigma_theory_continuous_marginalization.json` | `research/focused_paper_source_integration/outputs/c9l_sigma_theory_continuous_marginalization.json` | Theory marginalization output |
| `c8_fnl_running_fisher.json` | `research/focused_paper_source_integration/outputs/c8_fnl_running_fisher.json` | SDB Fisher output |

**Manifest count: 4 paper files + 5 figures + 12 scripts/JSONs = 21 files total**

*All scripts and JSON artifacts confirmed on-disk at `research/focused_paper_source_integration/` and `research/focused_paper_source_integration/outputs/`. Phase3_fisher_overlap.json mentioned in ZENODO_RELEASE_CHECKLIST.md — check `outputs/` directory; not found in initial listing but may exist under a variant name.*

---

## 8. Communities

- `astrophysics`
- `cosmology-and-nongalactic-astrophysics`

---

## 9. Funding

**None** — Independent research, no grant funding.

---

## 10. Version

`v1.7.60` (or `v1.7.61` if the ship-mode body-text pass was committed as a new version)

*See `ZENODO_RELEASE_CHECKLIST.md` — it references tag `paper2-v1.7.49`; update to `paper2-v1.7.60` (current submission version) before creating the GitHub release tag.*

---

## 11. Click-Publish Steps

1. **Log into zenodo.org** → click "New upload".
2. **Drop files:** drag in `paper2_arxiv_v1.7.60.tar.gz` + `02_full_draft.pdf` + all analysis scripts and JSON artifacts listed in section 7 above (zip the scripts+JSONs into `p2_analysis_code.zip` for convenience).
3. **Paste metadata:** Title, Description, Keywords, License (CC-BY-4.0), Authors, Communities from sections 1-9. Set Upload type = "Publication" → "Preprint".
4. **Reserve DOI:** click "Reserve DOI" — insert the minted DOI at the "DOI inserted at submission" placeholder in the paper source before the final compile. Also run step 1 of `ZENODO_RELEASE_CHECKLIST.md` (create GitHub release tag `paper2-v1.7.60` to trigger auto-import).
5. **Publish:** click "Publish". Insert the minted arXiv ID into P3's `DATA_RELEASE_MANIFEST.md` header and P5's companion-reference markers.
