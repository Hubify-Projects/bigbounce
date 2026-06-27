# P2 R54 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/R54_P2/02_full_draft.pdf` md5=e87fdb7c pages=28
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 150.7s

---

## Referee Report for "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook"

This paper presents a detailed sensitivity forecast for testing the matter-bounce cosmological scenario using upcoming large-scale structure surveys, primarily SPHEREx. The central prediction of the quasi-dust matter bounce is a local-type non-Gaussianity with `f_NL = -35/8`. The authors perform a comprehensive "recast" of existing SPHEREx forecasts, accounting for the template mismatch between the bounce bispectrum and the standard local template, performing a detailed analysis of a polynomial null space, and constructing a systematic error budget. The paper also provides a Bayesian model comparison to quantify the discriminating power against inflationary alternatives.

The technical analysis is, for the most part, exceptionally thorough. The authors have carefully recomputed key quantities, validated them across different methods (e.g., Fisher overlap, injection-recovery), and transparently documented their systematic budget. The resolution of the factor-of-two discrepancy in the literature between the Cai et al. and Li et al. results via an explicit operator-algebra argument in Appendix A is a valuable contribution. The numerical calculations appear to be robust and reproducible.

However, the paper requires significant revision to meet the standards of Physical Review D, primarily concerning a critical process error and the overall length and structure.

### ESSENTIAL

*   **P2-E1:** **All Pages:** A reviewer metadata block appears at the end of the submitted manuscript text (after page 28).
    *   **Problem:** The text `[REVIEWER METADATA — NOT PART OF THE PAPER — DO NOT FLAG AS ARTIFACTS] Paper tag: P2 | Round: R54 | Pages: 28 Round context (not in paper): R54 convergence-confirmation [END REVIEWER METADATA]` is present in the submitted file. This is internal review-process information and absolutely cannot appear in a manuscript intended for publication.
    *   **Required fix:** This block and any other non-manuscript text must be removed entirely. This is a critical process failure that must be rectified before the manuscript can be considered further.

### MAJOR

*   **P2-M1:** **Overall Structure:** The paper is 28 pages long, which is excessive for a sensitivity recast. While the analysis is detailed, the presentation is not as concise as it could be for a PRD article.
    *   **Problem:** The main narrative is diluted by extensive numerical validation and self-consistency checks that, while important, could be streamlined or moved to appendices. For example, the detailed step-by-step verification of the Bayes factor approximation in Section VI.C is overly pedagogical for a research article. The main text should present the results and their justification, with the fine details of the numerical machinery reserved for appendices or supplementary material.
    *   **Required fix:** The authors should significantly condense the manuscript to a target length of approximately 20-22 pages.
        1.  The detailed breakdown of the Bayes factor numerical checks (Section VI.C.b) should be summarized in a sentence or two, stating that the closed-form result was validated against approximations in the relevant limits, with the full derivation in an appendix if necessary.
        2.  The prose throughout the paper should be tightened.
        3.  The discussion in Section IX.D on the joint `(f_NL, n_fNL)` forecast, while a useful cross-check, is a subordinate analysis. Its detailed reporting, including the re-derivation of the `σ_marg` formula, could be shortened and its "subordinate" status emphasized even more strongly to avoid distracting from the paper's primary bispectrum-only forecast.

### MINOR

*   **P2-m1:** **Section II.A, Page 3, Eq. (2):** There is a potential sign confusion in the definition of `B_NL`.
    *   **Problem:** The text consistently refers to a *negative* non-Gaussianity, `f_NL = -35/8`. However, Eq. (2) shows `B_NL` approaching a *positive* value, `+35/8`. While `f_NL` and `B_NL` are not necessarily identical, their relation is not explicitly defined, and the opposite sign is confusing for the reader.
    *   **Required fix:** Clarify the relationship between `B_NL` as defined in Eq. (2) and the canonical nonlinearity parameter `f_NL`. If `B_NL` is defined to be positive, state this explicitly and define `f_NL = -B_NL` (or similar) to connect to the standard convention.

*   **P2-m2:** **Section VI, Pages 14-15:** The presentation of the Bayes factor results could be clearer.
    *   **Problem:** The abstract and main text headline a Bayes factor of `BF ≈ 9-14` which is based on the noise-weighted `r ≈ 0.84` template mismatch. However, the primary results in Table II are presented for the `r -> 1` (no mismatch) case, with the rebooking to `r ≈ 0.84` described in prose and footnotes. This forces the reader to connect multiple pieces of information to reconstruct the headline result, increasing the risk of misinterpretation.
    *   **Required fix:** Add a column or a separate table that explicitly shows the Bayes factors under the headline `r ≈ 0.84` assumption. This would make the connection between the main table and the abstract's claims direct and unambiguous. The current "Worked example" is helpful but is not a substitute for a clear tabular presentation of the main result.

*   **P2-m3:** **Section IV, Page 9, Eq. (7):** The scaling check for the non-Gaussian covariance is heuristic.
    *   **Problem:** The paper correctly states that Eq. (7) is a "heuristic primordial-field scaling check" and not a full galaxy-covariance derivation. However, the conclusion that the fractional shift is `≤ 5 × 10⁻⁴` is a strong statement based on this heuristic.
    *   **Required fix:** While a full re-derivation is rightly stated as beyond the scope, the authors should slightly soften the language around the final number. For instance, stating that the heuristic check "suggests the effect is at the sub-percent level, well below other systematics, justifying the use of the f_NL=0 Fisher matrix as a baseline," would be more appropriate than quoting a firm upper bound.

*   **P2-m4:** **Table IV, Page 20:** The "Combination rule" column could be more precise.
    *   **Problem:** The symbol `⊕` is used to denote "addition in quadrature" for the denominator, but for the `b_φ` rows, the text says "Fisher widening / baseline replacement". This is not an addition in quadrature.
    *   **Required fix:** For the `b_φ` rows, change the combination rule to "Replace `σ_base` with `σ_new`" or similar. This avoids confusion with the GR rows where quadrature addition is actually performed.

### NIT (Nitpicks)

*   **P2-N1:** **Abstract, Page 1:** The phrase "the exclusion arithmetic is symmetric" is slightly informal.
    *   **Problem:** While the meaning is clear, the phrasing is not typical for a formal abstract.
    *   **Required fix:** Consider rephrasing to "the significance of an exclusion limit is symmetric with that of a detection."

## Summary recommendation
**MAJOR REVISIONS**

The paper presents a high-quality, thorough, and valuable forecast for testing the matter-bounce scenario. The technical work, particularly the analysis of the polynomial null space and the resolution of the Cai/Li discrepancy, is excellent and at the level expected for PRD. The calculations are transparent and appear correct. However, the inclusion of reviewer metadata is an essential process error that must be fixed. Furthermore, the paper's excessive length obscures its key contributions and should be significantly reduced to improve its impact and readability. Once these structural and procedural issues are addressed, the paper will represent a strong contribution to the literature.