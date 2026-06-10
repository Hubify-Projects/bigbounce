# P3 auto-2026-06-08_1144pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (2609 chars)
**Wall time**: 142.9s

---

## Referee Report on "Spectrally Unusual Sources at Scale..."

This paper presents a large-scale anomaly detection campaign across seven astronomical surveys, resulting in a catalog of 378,280 unique anomalies. The BIGAE autoencoder framework is used, and a "Path-C" native retraining protocol is developed to overcome cross-survey domain-shift issues. The resulting catalog is used for two illustrative cosmological applications: forecasting constraints on primordial non-Gaussianity (`f_NL`) and testing the consistency of a matter-bounce model with NANOGrav 15-yr data.

The scale of the catalog and the methodological rigor, particularly the transparent discussion of initial failures and the "Path-C" rebuild, are commendable. The distinction between database coverage and genuine novelty is handled correctly. The cosmological applications are presented with appropriate caution, emphasizing their nature as forecasts or consistency checks rather than detections.

However, the paper requires significant revision before it can be considered for publication in Physical Review D. The primary concerns relate to the paper's structure and length, the depth of the cosmological analysis, and several key points of clarity that are essential for a PRD audience.

---

### ESSENTIAL Revisions

**P3-E1 | Section V, Abstract | Page 1, 10 | Ambiguous notation for `f_NL` constraint**
- **Problem:** The paper uses `(fNL)` and `σ(fNL)` interchangeably to refer to the *forecasted 1σ uncertainty* on `f_NL`. For example, the abstract states "a central forecast (fNL) = 8.14". This is highly misleading, as `f_NL` is the parameter itself, while the forecast is for its uncertainty, `σ(f_NL)`. A reader could easily misinterpret this as a measurement of `f_NL`.
- **Fix:** Replace all instances of `(fNL)` or `fNL` that refer to the uncertainty with the explicit notation `σ(f_NL)`. For example, the abstract should read "gives a central forecast `σ(f_NL)` = 8.14". This must be corrected in the abstract, Section V, Table VII, and any other relevant location.

**P3-E2 | Section V.B | Page 10 | Insufficient justification for GR projection effect calculation**
- **Problem:** The systematics section for the `f_NL` forecast is extremely brief. The claim that general-relativistic projection corrections "contribute |Δσ/σ| < 0.02% at kmax = 0.2 h Mpc⁻¹" is presented without derivation or a direct citation supporting this specific number. The parenthetical "(plane-parallel monopole, sub-% of b; §VID (e))" is insufficient for a PRD paper.
- **Fix:** Provide a derivation or a specific citation (e.g., to an equation in Yoo et al. [38] or Bonvin & Durrer [39]) that directly supports this quantitative claim. The authors must show how the effect scales and why it is negligible for this specific tracer sample and analysis.

**P3-E3 | Table I Footnotes | Page 7 | Overly dense and critical footnotes**
- **Problem:** Table I contains a series of extremely long and dense footnotes (particularly `†`, `‡`, `||`, `§`). These footnotes contain essential methodological details, including the definition of different thresholding schemes, the justification for native retrains, details of the deduplication, and cross-validation results. This information is critical to understanding the paper's core results and should not be relegated to fine print.
- **Fix:** Move the essential methodological details from the footnotes of Table I into the main body of the text (e.g., Section II.D or Section III). The table caption and footnotes should be reserved for concise clarifications directly related to the table's columns.

**P3-E4 | Abstract | Page 1 | Clarity of cosmological results**
- **Problem:** While the body of the paper is generally careful, the abstract could be misinterpreted. The phrasing "7.9% improvement consistent with no improvement at <1σ" is slightly awkward. The NANOGrav result is a consistency check, not a detection of bounce-compatible physics.
- **Fix:** Reword the abstract to be unambiguously clear that the cosmological results are not detections. For the `f_NL` result, state clearly that the forecast improvement is not statistically significant. For the NANOGrav result, state that the matter-bounce spectral index is "consistent with the posterior at the 1.13σ level" and that this does not constitute a detection.

### MAJOR Revisions

**P3-M1 | Entire Paper | Page 1-20 | Paper structure, scope, and length**
- **Problem:** The paper is 20 pages long and combines a detailed data-processing/methods paper with two distinct cosmological applications. For PRD, the focus should be on the physical results. The extensive discussion of the data pipeline, survey-specific results, and methodological lessons, while valuable, makes the paper overly long and dilutes the focus. The cosmological applications feel somewhat disconnected from the main effort of catalog creation.
- **Fix:** The authors should strongly consider restructuring. A recommended approach is to shorten the main paper to focus on the key results and one primary application (e.g., the `f_NL` forecast), moving much of the detailed survey-by-survey analysis and pipeline validation to appendices. Alternatively, this work could be split into a primary catalog/methods paper for a journal like ApJS and a shorter, more focused cosmology paper for PRD. As it stands, the paper is too long for its cosmological contribution.

**P3-M2 | Section V.C | Page 10 | `f_NL` systematics analysis is too shallow**
- **Problem:** The systematics section for the `f_NL` forecast is inadequate for a cosmology paper in PRD. It states "The forecast assumes zero observational systematics (fiber-assignment, photo-z, foreground)" and then briefly discusses nuisance parameters. This dismisses several critical, potentially dominant, systematics. For anomaly-selected objects, the impact of assembly bias, non-linear bias, and the spatial modulation of the selection function (e.g., due to fiber collisions or seeing variations) could be significant.
- **Fix:** Expand this section considerably. The authors must discuss the potential impact of the most relevant observational and astrophysical systematics. While a full mitigation is beyond the scope of this forecast, a quantitative estimate of their potential magnitude relative to the statistical uncertainty is required. For example, how does the DESI fiber assignment incompleteness mentioned in Section III.A propagate into the two-point function and the bias measurement?

**P3-M3 | Section II.B | Page 2 | Heterogeneity of anomaly thresholds**
- **Problem:** The paper uses at least four different types of thresholds to define anomalies across the surveys: an absolute `S > 5.0` cut (DESI), a percentile cut (LAMOST, Gaia), a data-driven knee-finding cut (eROSITA), and a fixed top-1% selection (Planck, NEOWISE). This methodological heterogeneity makes it difficult to interpret the combined catalog as a uniform sample. While the paper acknowledges this, the impact on cross-survey analysis and the physical interpretation of anomaly rates is not sufficiently discussed.
- **Fix:** Add a dedicated paragraph in the discussion (Section VI) on the implications of this heterogeneity. How does this affect the interpretation of the relative anomaly rates between surveys? Does this introduce a selection bias in the sample of multi-survey anomalies? The authors should justify why this approach is sufficient for the science goals presented.

### MINOR Revisions

**P3-m1 | Abstract | Page 1 | Definition of "catalog-grade" subset**
- **Problem:** The abstract mentions a "recommended catalog-grade subset is ~265,000 unique objects". The composition of this subset (DESI + SDSS + eROSITA + Gaia + NEOWISE) is clear, but the rationale for excluding LAMOST is only explained deep in the text as a "methodological lesson".
- **Fix:** Briefly add the reason for the LAMOST exclusion in the abstract, e.g., "(excluding the LAMOST exploratory tier due to a training-bias artifact)".

**P3-m2 | Section IV.A | Page 9 | In-text reference to figure**
- **Problem:** The text states "The aggregate SIMBAD-unmatched fraction (Fig. 5) is 58.8%". However, Figure 5 shows the per-survey fractions and a dashed line for the aggregate, but the value "58.8%" is not easily read from the figure itself.
- **Fix:** Add the aggregate value (58.8%) as a text label next to the dashed line in Figure 5 for clarity.

**P3-m3 | Section III.C | Page 5 | Ambiguous acronym "AE" in figure caption**
- **Problem:** The caption for a referenced but missing figure (Figure ??) states: `Panel labels report the per-arm Z-arm sub-score rz (printed as “AE” for legacy compatibility)`. The acronym "AE" is not defined and its connection to `rz` is unclear without prior knowledge.
- **Fix:** Define the acronym or use a more descriptive term. For example: "...Z-arm sub-score `rz` (labeled as Anomaly-z, AE_z, for legacy compatibility)...". (Assuming this is what it means).

**P3-m4 | Bibliography [33] | Page 19 | Internal note in bibliography**
- **Problem:** The entry for Heinrich et al. [33] contains an internal note: "[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]". This is an author-side bookkeeping note and is not appropriate for a published paper.
- **Fix:** Remove this internal note from the bibliographic entry.

**P3-m5 | Section I | Page 1 | Ambiguity in `f_NL` multi-tracer forecast**
- **Problem:** The introduction states a forecast from Heinrich et al. [33] as `σ(fNL) ≈ 0.7 bispectrum-only forecast`. The present paper uses the two-point function. This is a critical difference in methodology (power spectrum vs. bispectrum) that should be made explicit earlier and more clearly.
- **Fix:** In the introduction, clarify that the multi-tracer technique can be applied to different statistics, and that this work focuses on the two-point function, while other works (like [33]) have forecasted constraints from the bispectrum.

### NITs (Nitpicks)

**P3-N1 | Section II.A | Page 2 | Missing figure reference**
- **Problem:** The text states "...architecture shown schematically in Fig. ??."
- **Fix:** Correct the missing figure reference.

**P3-N2 | Section III.A | Page 4 | Missing figure reference**
- **Problem:** The text states "...subsets (Fig. ??)."
- **Fix:** Correct the missing figure reference.

**P3-N3 | Section V.A | Page 11 | Awkward phrasing**
- **Problem:** The phrase "Proper Savage-Dickey Bayes factors against the γ-uniform prior" is slightly awkward.
- **Fix:** Suggest rephrasing to "The Savage-Dickey Bayes factors, computed against a uniform prior on γ...".

---

## Summary recommendation

**MAJOR REVISIONS**

This paper presents a significant and valuable data product, accompanied by a commendably transparent methodological description. The work has the potential to be an important contribution. However, in its current form, it is not suitable for publication in Physical Review D. The combination of a lengthy methods paper with shallow cosmological analyses does not meet the journal's standards for depth and focus. The authors must undertake a major restructuring of the manuscript to either significantly deepen the cosmological analysis (including a much more thorough treatment of systematics) or shorten the paper to focus on a single, well-developed physical result, moving supplementary material to appendices. Additionally, several essential points of clarity, particularly regarding the notation and claims of the `f_NL` forecast, must be addressed. I recommend that the paper be reconsidered after these major revisions are implemented.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from a more rigorous re-examination of the paper.

---
### ADDITIONAL FINDINGS

**P3-E5 | Abstract, Section V.B | Page 1, 10 | Arithmetic error in `f_NL` forecast improvement**
- **Problem:** The paper claims that the central forecast `σ(f_NL) = 8.14` represents a "7.9% improvement" over the single-tracer baseline of `σ(f_NL)std = 8.98`. This is arithmetically incorrect. The fractional improvement, calculated as `(σ_std - σ_new) / σ_std`, is `(8.98 - 8.14) / 8.98 = 0.84 / 8.98 = 9.35%`. The 7.9% figure appears to be a stale number from a previous version of the analysis. This error is present in both the abstract and the main text and must be corrected.
- **Fix:** Recalculate and correct the percentage improvement for the `f_NL` forecast throughout the manuscript. The correct value is 9.4%.

**P3-m6 | Abstract, Table IV | Page 1, 13 | Contradictory description of `f_NL` forecast envelope**
- **Problem:** The uncertainty on the `f_NL` forecast is presented as a range, `[3.92, 8.98]`. The abstract describes this as a "1σ envelope", while the caption for Table IV (item i) describes it as a "95% envelope". These are contradictory statements (1σ vs. ~2σ). A check of the calculation in Section VI.D.(i) reveals that this range for `σ(f_NL)` is derived from propagating the 1σ uncertainty of the bias parameter `a`. Therefore, "1σ envelope" is the more accurate description.
- **Fix:** Make the description of the forecast envelope consistent throughout the paper. "1σ envelope" appears to be the correct term and should be used in all locations.

**P3-m7 | Section III.A, Appendix D | Page 4, 15 | Disconnected analysis of DESI anomalies**
- **Problem:** The main-text analysis of the 195,829 DESI anomalies (Section III.A) is limited to a coarse classification by spectral-arm dominance (e.g., "77.2% multi-band"). However, Appendix D and Figure 9 present a much more sophisticated and scientifically interesting classification into ten distinct astrophysical families (e.g., "High-z QSO", "Post-starburst") derived from UMAP clustering of the latent space. This is a significant result of the analysis that is effectively buried in an appendix and not mentioned in the main results section. This creates a confusing disconnect and undersells the paper's classification capabilities.
- **Fix:** Integrate the UMAP/HDBSCAN taxonomy into the main DESI results section (III.A). The breakdown of anomalies into these ten families is a more powerful result than the simple band-dominance statistics and should be a primary finding, not an afterthought in an appendix.