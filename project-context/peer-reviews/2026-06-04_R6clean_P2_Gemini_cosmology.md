# P2 2026-06-04_R6clean — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 60.1s

---

# Referee Report

**Paper:** Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook
**Manuscript ID:** [Assigned by editor]

This paper presents a comprehensive forecast for testing the matter bounce cosmological scenario using upcoming data from the SPHEREx survey. The primary observable is the local-type primordial non-Gaussianity (PNG), for which the quasi-dust matter bounce model predicts a specific value, fNL = -35/8. The author recasts existing SPHEREx forecasts, providing several original and significant contributions: (1) a detailed audit of the theoretical prediction, resolving a factor-of-two discrepancy in the literature; (2) the first quantitative calculation of the template mismatch between the bounce bispectrum and the standard local ansatz; (3) a thorough analysis of theoretical and systematic uncertainties; and (4) a detailed Bayesian model comparison against inflationary alternatives.

The paper is exceptionally well-researched, carefully argued, and transparent about its assumptions and limitations. The theoretical work, particularly in Appendix A, is of high quality and provides a valuable clarification for the community. The analysis is thorough, and the conclusions are well-supported by the evidence presented. The paper is a strong candidate for publication in Physical Review D after addressing the following points.

---

## Findings

### ESSENTIAL

**P2-E1: In-text Editing Artifact**
-   **Section/Page:** Section X (Conclusion), Page 18
-   **Problem:** The text contains what appears to be a leftover author's note or version-control comment: `(the prior conclusion-paragraph figure “> 6×105 ” was an aggregation error retired in §VI, indicates that...`
-   **Required Fix:** This sentence fragment must be removed or rewritten to be a complete, formal sentence appropriate for a published article.

### MAJOR

(None)

### MINOR

**P2-M1: Presentation of the Joint (fNL, nfNL) SDB Forecast**
-   **Section/Page:** Section IX.D, Page 16
-   **Problem:** This section introduces a second, distinct Fisher analysis for (fNL, nfNL) from scale-dependent bias (SDB), which yields a much higher idealized significance of ~9.9σ for fNL. The author has taken great care to state that this is an "illustrative idealized-Fisher internal-consistency check" and not a competing forecast with the paper's headline 3-5σ bispectrum result. However, the presence of this much larger number, even with caveats, could cause confusion for readers who may not appreciate the subtle distinction between the two analyses (bispectrum vs. multi-bin SDB) and their very different underlying assumptions and systematic vulnerabilities.
-   **Required Fix:** To minimize potential confusion, I recommend further de-emphasizing this result. The author could consider moving the detailed numerical discussion to an appendix or shortening it significantly, focusing only on the qualitative point that the nfNL=0 prediction provides an additional, powerful discriminator, without dwelling on the specific, highly idealized 9.9σ value. The current treatment is careful, but could be made more robust against misinterpretation.

**P2-M2: "Sanity Row" in Table III**
-   **Section/Page:** Table III, Page 14
-   **Problem:** The final row of Table III, "Corrected (10% residual; sanity row)", is unconventional. By construction, it is identical to the "Ideal" row at the given precision and is described as a "no-op sanity row". While its purpose is explained in the caption, its inclusion in the table itself is slightly confusing and adds clutter.
-   **Required Fix:** I suggest removing this row from the table. The point it makes—that a small, 10% residual contamination has a negligible impact—can be stated just as effectively in the caption or the main text, making the table cleaner and easier to interpret.

**P2-M3: Manuscript Date**
-   **Section/Page:** Title Block, Page 1
-   **Problem:** The paper is dated "June 4, 2026", which is a future date. While likely a placeholder, this should be corrected to the date of submission or revision.
-   **Required Fix:** Update the date to the current date of submission.

### NIT

**P2-N1: In-abstract Figure/Table Referencing**
-   **Section/Page:** Abstract, Page 1
-   **Problem:** The abstract uses the informal reference style "Fig. 6 / Table 3".
-   **Required Fix:** While not a major issue, for formal publication it would be better to rephrase to avoid direct figure/table callouts in the abstract, or to use a more standard phrasing if essential. For example, "...forecast under the local-template normalization (detailed in Table 3)...".

**P2-N2: Complexity of Table II Footnotes**
-   **Section/Page:** Table II, Page 11
-   **Problem:** The footnotes in Table II, particularly footnote 'a', contain complex cross-references to Table III and prose in other sections. This makes the table difficult to parse as a standalone element.
-   **Required Fix:** Consider simplifying the footnotes or restructuring the tables to make the logical flow more self-contained, if possible. For instance, the key information from the cross-reference could be briefly summarized directly in the footnote.

---

## Summary recommendation

**ACCEPT WITH MINOR CORRECTIONS**

This is an excellent and comprehensive paper that makes several valuable contributions to the field. It provides a robust and realistic forecast for testing the matter bounce model, clarifies an important theoretical ambiguity, and introduces new analysis (the template mismatch quantification and Bayesian comparison). The work is careful, scholarly, and transparent. The single essential correction is a minor text artifact. The other suggestions are aimed at improving clarity and presentation. The paper is a significant contribution and is well-suited for publication in Physical Review D.