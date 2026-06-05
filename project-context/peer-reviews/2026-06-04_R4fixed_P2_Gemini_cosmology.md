# P2 2026-06-04_R4fixed — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 54.3s

---

## Referee Report for Paper P2

**Paper:** Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook
**Round:** 2026-06-04_R4fixed

This paper presents a detailed forecast for testing the matter bounce cosmological model using upcoming data from the SPHEREx survey. The primary contributions are (1) a thorough audit of the theoretical prediction for the non-Gaussianity parameter, `f_NL = -35/8`, including a resolution of a factor-of-two discrepancy in the literature; (2) the first quantification of the template mismatch between the matter bounce bispectrum and the standard local template; and (3) a systematic application of these findings to produce a realistic detection significance forecast, including a Bayesian model comparison.

The technical analysis of the bispectrum prediction, template overlap, and systematic effects is comprehensive and represents a valuable contribution to the field. However, the manuscript in its current form suffers from severe issues related to scope and unprofessional manuscript preparation that must be addressed before it can be considered for publication.

### ESSENTIAL Revisions

The following issues must be fully resolved for the paper to be acceptable.

**P2-E1: Removal of Unsubstantiated Forecasts (Section IX.D, Page 16)**
*   **Problem:** Section IX.D, "Joint (f_NL, n_fNL) Forecast as a Stronger Discriminator," presents a forecast (`~9.9σ`) for a joint analysis that is explicitly stated to be outside the scope of this paper. The text admits the required Fisher matrix inputs are "not yet on disk in this release" and that the full analysis "is deferred to a companion artifact." Presenting a high-significance result from an analysis that is not performed, documented, or reproducible within this work is unacceptable. It inflates the paper's claims with unauditable results and distracts from the paper's legitimate contributions.
*   **Fix:** Remove Section IX.D entirely. All references to this separate, joint `(f_NL, n_fNL)` analysis, its methodology, and its `~9.9σ` result must be removed from the manuscript, including from the abstract. The paper's headline results should be based solely on the analyses fully presented and documented within it (i.e., the bispectrum-only forecast).

**P2-E2: Removal of Internal Review Artifacts and Version History**
*   **Problem:** The manuscript is littered with internal notes, comments from a previous review cycle, and version-tracking artifacts. This is highly unprofessional and makes the paper unreadable as a final scientific document.
*   **Fix:** The authors must perform a thorough proofread and remove all such artifacts. Specific examples include, but are not limited to:
    *   **Page 2:** "the abstract previously gave only the central ~ 2.6σ; the upper-bound of the halved range is reported here for completeness"
    *   **Page 2:** "consistent with the conclusion-section restatement, §X; both numbers are reported because the convention-reversal halving applies independently of where in the systematic-budget chain the figure is quoted"
    *   **Page 7:** "the per-realization spread from `phase3_fisher_overlap.json` is wider"
    *   **Page 7:** "A re-derivation of the Heinrich Fisher matrix at the bounce-fiducial is a structural extension on the post-arXiv TODO"
    *   **Page 11 (Table II Caption):** The entire note beginning "Note: prior versions of this caption..." must be removed. The final table should simply present the final, correct numbers and a clean caption.
    *   **Page 18:** "the prior conclusion-paragraph figure “>6×10^5” was an aggregation error retired in §VI"
    *   **Page 18 (Appendix A):** "to address the cross-model peer-review concern (R42 Gemini 3.1-Pro P2 BLOCKER B-3)" — This is a particularly egregious inclusion of what appears to be an internal review-system tag.

### MAJOR Revisions

**P2-M1: Abstract Must Accurately Reflect Paper Content (Page 1)**
*   **Problem:** The abstract currently refers to the problematic joint `(f_NL, n_fNL)` analysis discussed in P2-E1: "A separate joint (f_NL, n_fNL) scale-dependent-bias Fisher analysis is discussed in §IX as an idealized-Fisher self-consistency check ... the specific numerical significance is not quoted here in the abstract until that release lands)." The abstract must summarize the work *presented in the paper*, not work that is deferred or incomplete.
*   **Fix:** Following the removal of Section IX.D (P2-E1), this sentence and any other reference to the joint `(f_NL, n_fNL)` analysis must be removed from the abstract. The abstract should be revised to focus on the paper's core, verifiable contributions: the bispectrum-only forecast, the template mismatch calculation, and the Bayesian comparison.

### MINOR Revisions

**P2-m1: Incorrect Date (Page 1)**
*   **Problem:** The paper is dated "June 4, 2026," a future date.
*   **Fix:** Correct the date to the current submission date.

**P2-m2: Redundant "Sanity Row" in Table (Page 14)**
*   **Problem:** In Table III, the row "Corrected (10% residual; sanity row)" is explicitly described in the caption as a "no-op sanity row" that is "by construction, equal to 'Ideal'". This adds clutter without providing new information.
*   **Fix:** Remove this redundant row from Table III and its corresponding explanation from the caption.

**P2-m3: Focus and Length**
*   **Problem:** At 22 pages, the paper is lengthy. While the core analysis is detailed, some sections feel ancillary to the main forecast. The discussion of cosmic birefringence (Section VII.E), while interesting context, is explicitly independent of the paper's forecasts and could be shortened to improve focus.
*   **Fix:** Consider significantly trimming or removing the cosmic birefringence discussion. The primary focus should be on the non-Gaussianity forecasts which are the paper's main subject.

**P2-m4: Unprofessional Filename Reference (Page 20)**
*   **Problem:** The text refers to a reproducibility notebook by its filename: "...is archived alongside the paper source as `appendix_A1_wick_doubling.py`."
*   **Fix:** Rephrase this to be more professional, for example: "A reproducibility notebook implementing this derivation is included in the supplementary materials."

### NITs

**P2-N1: Placeholder Email (Page 2)**
*   **Problem:** The corresponding author's email appears to be a placeholder (`houston@hubify.com`).
*   **Fix:** Provide a valid, professional contact email.

## Summary recommendation
**MAJOR REVISIONS**

The paper's core technical work, particularly the audit of the `f_NL = -35/8` prediction and the first-ever calculation of the bounce-local template mismatch (`r`), is a solid and valuable contribution. The subsequent application to SPHEREx forecasts is systematic and well-motivated. However, the manuscript is critically flawed by the inclusion of an unsubstantiated forecast from an entirely separate analysis (Sec IX.D) and by an unacceptable level of sloppiness, with numerous internal review notes left in the text. These issues undermine the paper's credibility and must be fully rectified. If the authors remove the unsubstantiated claims, thoroughly clean the manuscript of all internal artifacts, and refocus the abstract and conclusions on the work actually presented, the revised paper would likely be suitable for publication.