# P4 R57 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/R57_P4/chirality_catalog_paper.pdf` md5=5ddefa62 pages=23
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 213.8s

---

## Referee Report

**Paper ID:** P4
**Round:** R57
**Journal:** Physical Review D

This paper presents a comprehensive analysis of galaxy chirality using a new catalog of 8.47 million galaxies from the DESI Legacy Surveys, of which 3.2 million are classified as spirals. The authors employ a Vision Transformer with a rigorous Test-Time Averaging (TTA) procedure to enforce flip-equivariance, a critical step for mitigating instrumental and classifier biases. The primary scientific result is a null detection of a real-space chirality dipole, consistent with statistical isotropy. The paper's main contributions are the large, publicly released catalog and an exceptionally thorough treatment of potential systematic effects, including a novel quantification of a "monopole-mask leakage" channel.

The analysis is conducted with a very high level of rigor. The authors carefully define an analysis hierarchy, distinguishing between primary cosmological estimators and secondary diagnostic tests. They are commendably transparent about the different null hypotheses and statistical conventions used for different estimators, repeatedly warning the reader not to compare significance values that are not on the same statistical footing. The systematic analysis is multi-pronged and convincing, culminating in a robust null result for the primary observable and a clear attribution of diagnostic signals to understandable systematics. The work represents a significant step forward in the search for cosmic parity violation through galaxy morphology.

The paper is well-structured, and the claims in the abstract are meticulously supported by the detailed analysis in the body and appendices. The methodology is sound, and the results are presented with appropriate caveats. The following points should be addressed before publication.

---
### Findings

#### ESSENTIAL

*   **P4-E1:** **Section: V.A (p. 12), XIV.B (p. 14).** **Problem:** The paper makes a strong claim of excluding the "Shamir ~3% amplitude class" by a factor of ~5-12. This is based on comparing the pipeline's best-fit WLS template amplitude (0.32%) to Shamir's reported range (1.7%-4.0%). However, the paper also correctly states, "We do not claim a frequentist exclusion of Shamir's Ganalyzer estimator: a likelihood-level exclusion requires a matched-footprint Ganalyzer reanalysis under his pipeline + cuts (not performed here)." These two statements are in tension. An "exclusion by a factor of X" implies a formal exclusion, which the authors admit has not been performed. **Required fix:** The language must be softened to reflect the comparison of results from two different pipelines, not a formal exclusion. Rephrase to state that the results are inconsistent by a factor of ~5-12, and that this inconsistency is likely due to uncorrected systematics in the previous analysis, as demonstrated by the monopole-leakage channel in this work. Remove the word "excluded" in this context. For example, change "The Shamir ~3% amplitude class is excluded by a factor of ~5-12" to "The present null result is in tension with the previously claimed ~3% amplitude by a factor of ~5-12".

#### MAJOR

*   **P4-M1:** **Section: Appendix D.g (p. 20), Table X.** **Problem:** Table X reports z-values for the three imaging-leg fraction templates (BASS+MzLS, DECALS, DES). The text correctly notes that these templates are nearly collinear and that their individual coefficients and errors are not meaningful. Reporting large, meaningless z-values in the table is highly misleading to any reader who does not parse the accompanying text with extreme care. **Required fix:** In Table X, replace the numerical z-values for the three `leg` templates with "—" or "N/A". Add a note to the table caption explicitly stating that these values are not meaningful due to template collinearity, as explained in the text.

#### MINOR

*   **P4-m1:** **Section: Abstract (p. 1), III.A (p. 3).** **Problem:** The term "moment-z" is used in the abstract and elsewhere. While it is defined in the text as a "moment-ratio", this is slightly non-standard terminology that may cause confusion. **Required fix:** For clarity, especially in the abstract, consider a more descriptive phrase. For example, "the equivariant-catalog high-confidence dipole fit... gives a significance of +0.41σ (as a moment-ratio against the... null)". This is a minor suggestion for improved readability.
*   **P4-m2:** **Section: IV.C.α (p. 8).** **Problem:** The sentence "since A_obs < A_95,nq, and is a descriptive estimator-level bound used in no scientific conclusion), gives A_95,nq = 6.8 × 10−3..." is awkwardly phrased. The parenthetical is confusingly placed. **Required fix:** Rephrase for clarity. For example: "This observed amplitude is smaller than the 95th percentile of the null distribution, A_95,nq = 6.8 × 10−3. We note that A_95,nq is a descriptive, estimator-level bound and is not used to draw any scientific conclusions."
*   **P4-m3:** **Section: Table III Caption (p. 11).** **Problem:** The caption contains the important statement: "The permutation null is heavy-tailed relative to Gaussian at low l, so z_mom and the Gaussian-equivalent of rank p need not agree." This is a key statistical point that justifies the use of empirical rank-p values. **Required fix:** This point is important enough to merit a brief mention in the main body text (e.g., in Section IV.C) where the dipole significance is first discussed, not just in a table caption.
*   **P4-m4:** **Section: Data Availability (p. 22) and Title Page (p. 1).** **Problem:** The paper is dated "June 26, 2026", and the repository commit hash is associated with "June 2026". This is clearly a placeholder for the submission date. While this is common practice for pre-prints, it can be confusing. **Required fix:** Before publication, update this date to the actual date of submission or acceptance. This is a pro-forma check.

#### NIT

*   **P4-N1:** **Section: II.A (p. 2).** **Problem:** The text reads "DECALS (d<+32°)", where 'd' is likely an OCR or typo for the Greek letter delta (δ) representing declination. **Required fix:** Replace 'd' with 'δ'.
*   **P4-N2:** **Section: III.A (p. 3).** **Problem:** The bulleted list describing the three significance conventions is excellent. **Required fix:** Consider enclosing this list in a formal, numbered "Definition" block to give it more prominence, as it is a cornerstone of the paper's rigorous methodology. This is a stylistic suggestion.

---
## Summary recommendation

**MAJOR REVISIONS**

This is an excellent paper that performs a rigorous and comprehensive analysis. The quality of the systematic checks, the transparency of the methodology, and the careful presentation of the results are of a very high standard suitable for publication in Physical Review D. The primary reason for the "MAJOR REVISIONS" recommendation is to correct the language regarding the "exclusion" of previous results (P4-E1), which in its current form overstates the formal statistical claim. The other points, particularly P4-M1, are important for preventing misinterpretation of the detailed results. Once these issues are addressed, the paper will be a valuable contribution to the field.