# P2 R57 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/R57_P2/02_full_draft.pdf` md5=7df88149 pages=28
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 168.4s

---

## Referee Report for Manuscript [Paper ID Redacted]

**Title:** Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook

This paper presents a detailed sensitivity forecast for testing the matter-bounce cosmological scenario using primordial non-Gaussianity. The authors recast existing forecasts for the SPHEREx and the proposed MegaMapper surveys to constrain the specific prediction `f_NL = -35/8`. The work includes a thorough analysis of the template mismatch between the matter-bounce bispectrum and the standard local template, a comprehensive systematic budget, and a Bayesian model comparison against inflationary alternatives.

The paper is exceptionally well-written, methodologically sound, and transparent about its assumptions and limitations. The level of rigor in the analysis of the bispectrum shape, the polynomial null space, the systematic error budget, and the Bayesian statistics is very high and meets the standards for publication in Physical Review D. The authors are careful to distinguish between optimistic, realistic, and conservative forecasts, and they clearly separate distinct observational channels (bispectrum vs. scale-dependent bias). The resolution of the factor-of-two discrepancy in the literature regarding the predicted `f_NL` value is a valuable contribution.

I have identified one major point and several minor points that should be addressed before publication.

---
### ESSENTIAL Findings
None.

### MAJOR Findings

**ID:** P2-M1
*   **Section/Page:** Abstract, Page 1
*   **Problem:** The abstract presents the main forecast for SPHEREx as a "realistic ~2.6-5σ" detection significance. While the body of the paper provides an excellent and detailed breakdown of how this range is derived, the lower end of this range (2.6σ) requires more context at the abstract level. A 2.6σ result constitutes statistical "evidence" but is not a discovery, and a measurement at this level would still be consistent with a null result at the p ≈ 0.01 level. For a headline result in the abstract, simply stating the significance range is insufficient without providing the reader with the corresponding effect size or measurement uncertainty.
*   **Required Fix:** The abstract should be revised to include the practical meaning of a detection at the lower end of the realistic sensitivity range. For example, after quoting the `2.6-5σ` range, add a parenthetical statement clarifying the implied constraint, such as "(corresponding to a measurement of `f_NL ≈ -4.4 ± 1.7` at the conservative endpoint)". This provides crucial context for the reader to interpret the practical power of the experiment.

### MINOR Findings

**ID:** P2-N1
*   **Section/Page:** Section V (MegaMapper Forecast), Page 11
*   **Problem:** The text states that the MegaMapper forecast uses a template-mismatch factor `r = 0.84-0.88`. This range is slightly different from the canonical range `r ∈ [0.829, 0.876]` established in Section III B (Eq. 6, page 8) which spans all physically motivated noise-weighting schemes. While the numerical impact is negligible, using inconsistent ranges for the same physical parameter can cause confusion.
*   **Required Fix:** The authors should use the canonical `r ∈ [0.829, 0.876]` range for the MegaMapper forecast to maintain consistency with the rest of the paper. Alternatively, if there is a specific reason to use a different range for MegaMapper (e.g., different expected noise properties), this should be explicitly justified.

**ID:** P2-N2
*   **Section/Page:** Section X (Conclusion), Page 23
*   **Problem:** The conclusion restates the key result that the bounce-vs-inflation gauge-frame amplitude ratio is `≈ 290`. This number depends on the slow-roll prediction `f_NL^inf ≈ 0.015`, which in turn depends on the spectral index `n_s`. While this is detailed in the introduction, the conclusion would be more self-contained if this dependency was briefly reiterated.
*   **Required Fix:** Add a brief parenthetical note stating the assumed `n_s` value when quoting the `≈ 290` ratio in the conclusion, for example: "...the bounce-vs-inflation gauge-frame amplitude ratio is therefore `|f_NL^bounce,gauge|/|f_NL^inf,gauge| ≈ 290` (for `n_s ≈ 0.965`), with the bounce prediction opposite in sign."

**ID:** P2-N3
*   **Section/Page:** Data and Code Availability, Page 24
*   **Problem:** The text contains the placeholder "Zenodo (DOI inserted at submission)".
*   **Required Fix:** This is a standard note, but please ensure this placeholder is replaced with the final, active DOI for the archived code and data in the final version of the manuscript.

### NIT Findings

**ID:** P2-N4
*   **Section/Page:** Appendix A.1, Page 27
*   **Problem:** The text references a reproducibility notebook with the filename `appendix _A1_wick_doubling.py`. The leading underscore in the filename appears to be a minor typo.
*   **Required Fix:** Please correct the filename to `appendix_A1_wick_doubling.py` for consistency and clarity.

---
## Summary recommendation

**MAJOR REVISIONS**

The paper is of very high quality and represents a significant and timely contribution to cosmology. The analysis is thorough, rigorous, and transparent. The major revision requested is to improve the communication of the main result in the abstract by providing essential context on the effect size, which is crucial for the proper interpretation of the forecast. The minor points are straightforward to address. Once these revisions are made, the manuscript will be an excellent candidate for publication in Physical Review D.