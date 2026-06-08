# P3 auto-2026-06-08_1632pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (5151 chars)
**Wall time**: 147.1s

---

## Referee Report for "Spectrally Unusual Sources at Scale..."

**To the Editor of Physical Review D,**

This manuscript by Houston Golden presents a large-scale anomaly detection search across seven astronomical surveys, resulting in a catalog of 378,280 unique anomalies. The work has two primary aims: the discovery of rare astrophysical objects and the application of these objects as tracers for cosmological measurements, specifically for primordial non-Gaussianity (`f_NL`) and the stochastic gravitational-wave background.

The scale of the analysis is impressive, and the resulting catalog is potentially a valuable community resource. The authors have clearly invested significant effort in validation, including cross-validation, out-of-distribution tests, and injection-recovery simulations. The paper also provides important methodological lessons on the pitfalls of applying machine learning models across different datasets (domain shift), highlighted by the LAMOST training-bias and SDSS cross-transfer artifacts.

However, the manuscript in its current form has several essential and major flaws that prevent its publication in Physical Review D. The most critical issue is the inconsistent application of the authors' own quality control protocol, where results from surveys that fail key validation gates are retained in the primary catalog. The presentation is also frequently confusing, mixing final results with superseded diagnostics and using non-standard language and statistical descriptions. The paper requires a significant structural revision to clearly separate validated results from exploratory ones and to improve clarity and rigor.

My detailed findings are listed below.

---

### Detailed Findings

#### ESSENTIAL REVISIONS (Paper cannot be accepted without these fixes)

**P3-E1: Inconsistent Application of Validation Gates and Retention of Failed Results**
*   **Location:** Abstract (p. 1), Section IID (p. 3), Section III (pp. 3-6), Figure 7 (p. 13)
*   **Problem:** The "Path-C rebuild" protocol includes a crucial injection-recovery gate (Step 5), which the authors state is a core part of their methodology. However, three of the six point-source surveys—LAMOST, Gaia, and eROSITA—explicitly **FAIL** this gate at the 5σ level (Fig. 7 shows recovery rates of 5.8%, 5.2%, and 1.2% respectively, far below the 50% PASS threshold). The authors attempt to re-brand this failure as "FAIL-with-diagnostic," which is not a standard or acceptable practice. A validation failure is a failure. The abstract further compounds this by recommending a ~265,000 object subset that excludes the LAMOST "exploratory tier," yet the headline number of 378,280 and the main analysis include these unvalidated objects. This fundamentally undermines the credibility of a significant fraction of the catalog.
*   **Required Fix:**
    1.  The paper must be restructured to draw a hard line between validated and unvalidated/exploratory results. The surveys that passed all validation gates (DESI, SDSS, NEOWISE, and arguably Planck) should form the basis of the main paper and its primary scientific claims.
    2.  The results from LAMOST, Gaia, and eROSITA must be moved to an appendix and clearly labeled as exploratory, with strong caveats about their reliability due to the failed validation.
    3.  The abstract, introduction, and conclusions must be rewritten to reflect this separation. The headline anomaly count should be based only on the fully validated surveys. The term "FAIL-with-diagnostic" must be removed and replaced with a simple "FAIL."

**P3-E2: Inconsistent Anomaly Thresholding Across Surveys**
*   **Location:** Section IIB (p. 2), Table I footnotes (p. 7)
*   **Problem:** The definition of an "anomaly" is not uniform across the surveys. DESI uses a fixed `S > 5.0` cut. SDSS and LAMOST use a top-1% percentile slice (`S ≥ 0.1060` and `S ≥ 0.4613`, respectively). Planck, Gaia, and NEOWISE also use a top-1% selection. eROSITA uses a "data-driven Isolation Forest score-knee threshold." This heterogeneity makes it impossible to compare anomaly rates between surveys and complicates the physical interpretation of the combined catalog. The footnote in Table I reveals that a strict `S > 5` cut on SDSS would yield only 12 sources, not the 77,905 reported in the headline count. This is a critical detail that demonstrates the non-equivalence of the thresholds, and it is unacceptably buried in a footnote.
*   **Required Fix:**
    1.  This methodological inconsistency must be highlighted as a major limitation in the abstract and main body, not just in footnotes.
    2.  The authors must provide a strong justification for not using a uniform thresholding scheme (e.g., a consistent percentile cut across all surveys).
    3.  The dramatic difference in the SDSS anomaly count between the `S > 5` cut (12 objects) and the top-1% cut (77,905 objects) must be discussed in the main text as a key finding related to the cross-survey domain shift.

**P3-E3: Unprofessional Manuscript Metadata**
*   **Location:** Page 1, under author list.
*   **Problem:** The paper is dated "(Dated: June 2026)". This is a placeholder or a severe typo and is unprofessional for a journal submission.
*   **Required Fix:** Correct the date to the submission date.

#### MAJOR REVISIONS (Significant revision required)

**P3-M1: Confusing Presentation in Summary Table (Table I)**
*   **Location:** Table I (p. 7)
*   **Problem:** The main summary table is extremely confusing. The `N_anom` column reports the initial "cross-transfer" counts, which are explicitly stated to be superseded and, in the case of SDSS and LAMOST, are severe artifacts. The final, canonical numbers are not in the main table rows but are described in dense footnotes. This forces the reader to piece together the final results from the fine print, while the table itself displays misleading numbers.
*   **Required Fix:** Restructure Table I to show the final, canonical "Path-C" native-retrained anomaly counts for each survey in the main rows. The superseded "cross-transfer" baseline numbers should be moved to a separate diagnostic table in the appendix.

**P3-M2: Non-Standard and Confusing `f_NL` Forecast Presentation**
*   **Location:** Abstract (p. 1), Section Vb (p. 11)
*   **Problem:** The paper reports the `f_NL` forecast as `σ(f_NL) = 8.14` with a "1σ envelope [3.92, 8.98]". This is not a standard statistical presentation. As my own calculation confirms, this "envelope" is not a 1σ confidence interval on the value of `σ(f_NL)`. Instead, it represents the *range* of possible central values for `σ(f_NL)` when the bias parameter `a` is varied within its 1σ uncertainty (`a = 0.19 ± 0.65`). This is a forecast on a forecast, and calling it a "1σ envelope" is highly misleading.
*   **Required Fix:** Rephrase this result clearly. For example: "Using the measured bias enhancement `a_jk = 0.19 ± 0.65`, we forecast a constraint of `σ(f_NL) = 8.14`. The 1σ uncertainty on `a_jk` implies a range of possible constraints `σ(f_NL) ∈ [3.92, 8.98]`, where the lower bound corresponds to the `+1σ` value of `a_jk`."

**P3-M3: Inappropriate Language in Table IV**
*   **Location:** Table IV (p. 13)
*   **Problem:** Table IV, "Path-C residual caveats," reads like an internal issue-tracking document, not a formal scientific table. Phrases like "All ten items are closed (C = resolved in paper...)" are inappropriate for a peer-reviewed publication.
*   **Required Fix:** Rewrite the table content in standard academic prose, or, preferably, remove the table and integrate its points as a clear, itemized list within the main text of Section VID ("Path-C Rebuild Residual Caveats").

**P3-M4: Ambiguous Planck CMB Validation Status**
*   **Location:** Section IIIF (p. 6)
*   **Problem:** The authors state that the native Planck convolutional autoencoder "converged at val_loss = 0.4437 (criterion (a) FAIL, but criterion (b) PASS: 500/500 = 100% injection-recovery...)". It is not immediately obvious that passing the injection-recovery test is sufficient to completely override a failure on the validation loss criterion.
*   **Required Fix:** Provide a more detailed justification for why this mixed result is considered an overall PASS for the Planck analysis. Explain the physical meaning of the high validation loss and why the perfect injection recovery provides sufficient confidence to proceed.

#### MINOR REVISIONS (Address but paper can proceed)

**P3-m1: Figure 1 Caption and Content**
*   **Location:** Figure 1 (p. 4)
*   **Problem:** The main sky map shows the "cross-transfer baseline" distribution (319,443 anomalies), which is superseded. The primary result of the paper is the final 378,280 unique anomalies after the Path-C rebuild.
*   **Required Fix:** The main figure should show the spatial distribution of the final, canonical 378,280 anomalies. The baseline map can be moved to an appendix as a diagnostic. The caption must be updated accordingly.

**P3-m2: Clarification of `f_NL` Systematics**
*   **Location:** Section Vc (p. 11)
*   **Problem:** The text states the `f_NL` forecast "assumes zero observational systematics." While this is a common practice for forecasts, it is a strong assumption.
*   **Required Fix:** Briefly state in the abstract that the `f_NL` forecast is systematics-free to ensure this important caveat is not missed.

**P3-m3: Duplicate Phrase**
*   **Location:** Section IID, step 6 (p. 3)
*   **Problem:** The text reads "union-find friends-of-friends".
*   **Required Fix:** Change to "union-find algorithm" or "friends-of-friends algorithm".

#### NIT-PICKS (Cosmetic)

**P3-N1: Citation Year Continuity Note**
*   **Location:** Bibliography, ref [33] (p. 19)
*   **Problem:** The entry for Heinrich et al. contains an explanatory note: "[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]". This is internal bookkeeping and should not appear in the final reference list.
*   **Required Fix:** Remove the explanatory note from the reference.

---

## Summary recommendation

**MAJOR REVISIONS**

This paper represents a substantial and valuable effort to create a multi-survey anomaly catalog. The work contains important scientific findings and methodological lessons for the community. However, it is currently undermined by the inconsistent application of its own validation protocol, the retention of data from failed quality checks in the primary results, and a confusing presentation that mixes final numbers with superseded artifacts.

For the paper to be acceptable for publication in Physical Review D, the authors must perform a major restructuring to rigorously separate the validated catalog from the exploratory components. The claims in the abstract and conclusions must be revised to reflect only what has been robustly demonstrated. With these significant revisions to improve rigor and clarity, the manuscript has the potential to be an important contribution to the field.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from the second, more rigorous review of the paper.

---
### ADDITIONAL FINDINGS

#### ESSENTIAL REVISIONS

**P3-E4: Contradictory Definition of "Catalog-Grade" Subset**
*   **Location:** Abstract (p. 1)
*   **Problem:** The abstract defines a "recommended catalog-grade subset" of ~265,000 objects which explicitly includes Gaia and eROSITA. However, the same abstract states that both Gaia and eROSITA **FAIL** the injection-recovery validation gate. A result that fails a core validation test cannot be considered "catalog-grade." This is a major internal contradiction that undermines the paper's own quality standards.
*   **Required Fix:** The "recommended catalog-grade subset" must be redefined to include only those surveys that pass all validation gates (DESI, SDSS, NEOWISE). The abstract must be corrected to reflect this, and the rationale for excluding Gaia and eROSITA from the high-quality tier must be made explicit.

#### MAJOR REVISIONS

**P3-M5: Arithmetic Error in `f_NL` Forecast Improvement**
*   **Location:** Abstract (p. 1), Section Vb (p. 11)
*   **Problem:** The paper claims that the multi-tracer forecast `σ(f_NL) = 8.14` represents a "7.9% improvement" over the single-tracer baseline of `σ(f_NL)std = 8.98`. This is arithmetically incorrect. The fractional improvement is `(8.98 - 8.14) / 8.98 = 0.0935`, which is a **9.4%** improvement. This error appears in both the abstract and the main text.
*   **Required Fix:** Correct the calculated improvement from 7.9% to 9.4% throughout the manuscript.

**P3-M6: Inconsistent and Misleading Figure Caption (Figure 2)**
*   **Location:** Figure 2 (p. 5)
*   **Problem:** The caption for Figure 2 states that the plots for DESI and LAMOST are based on their "native" retrains. However, the anomaly count listed in the legend for LAMOST is 44,075, which is the superseded "cross-transfer" count from Table I, not the final native count of 113,342. This makes the figure's description of its own content unreliable and confusing.
*   **Required Fix:** The figure legend must be corrected to show the final, canonical anomaly counts for all surveys being plotted. The caption must be clarified to state unambiguously which version of the data (cross-transfer or native) is being plotted for each survey.

**P3-M7: Incorrect Internal Cross-References**
*   **Location:** Section II D (p. 3), Section III E (p. 6)
*   **Problem:** The manuscript contains incorrect internal cross-references that hinder navigation and understanding.
    1.  In Section II D, the text states that the cross-transfer scan is preserved in "§VIA". Section VI A is about the "LAMOST Training-Bias Lesson." The correct reference should be to Section III, where the survey-by-survey results are actually presented.
    2.  In Section III E, the cross-referencing for the eROSITA cross-validation stability is circular and confusing, with `§VID (f)` pointing to a table item which in turn points back to `§III E`.
*   **Required Fix:** Systematically check and correct all internal cross-references (`§` and `Table` references) throughout the manuscript to ensure they point to the correct sections and provide the information claimed.

#### MINOR REVISIONS

**P3-m4: Dimensionally Inconsistent Equation**
*   **Location:** Appendix E, Equation E1 (p. 15)
*   **Problem:** Equation E1, used for the NANOGrav analysis, is dimensionally inconsistent. It takes the logarithm of several quantities that have physical units (e.g., `f_yr`, `f_i`, `T_obs`) without explicit normalization by a reference value. While the normalization may be implicit in the analysis code, an equation presented in a physics paper must be formally correct.
*   **Required Fix:** Rewrite Equation E1 to be dimensionally consistent by explicitly showing the normalization of all dimensionful quantities (e.g., `log10(f_i / f_ref)`).

**P3-m5: Juxtaposition of Incommensurable `σ` Values**
*   **Location:** Abstract (p. 1), Section V vs. VI A
*   **Problem:** The abstract presents `σ` values from two very different statistical procedures side-by-side: the `+1.13σ` for the NANOGrav result is a parameter-shift significance derived from a Bayesian posterior of existing data, while the `σ(f_NL) = 8.14` is a Fisher forecast representing the expected 1σ sensitivity of a future experiment. Presenting these without qualification could mislead a reader into thinking they are comparable measures of statistical significance.
*   **Required Fix:** Add a brief qualifying phrase in the abstract to distinguish the nature of the two results, for example by referring to the `f_NL` result as a "forecasted sensitivity" and the NANOGrav result as a "consistency test against current data."

#### NIT-PICKS

**P3-N2: Notational Error in Abstract**
*   **Location:** Abstract (p. 1)
*   **Problem:** When reporting the `f_NL` forecast, the abstract gives the 1σ envelope for `(f_NL)` as `[3.92, 8.98]`. The quantity being constrained is the uncertainty, `σ(f_NL)`, not the parameter `f_NL` itself. The `σ` is missing.
*   **Required Fix:** Correct the notation in the abstract to `σ(f_NL)` ∈ `[3.92, 8.98]`.