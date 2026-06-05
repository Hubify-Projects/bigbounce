# P5 auto-2026-06-05_1617pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (9653 chars)
**Wall time**: 172.8s

---

## Referee Report on "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals"

This paper presents a comprehensive search for an environmental dependence of spiral galaxy chirality by cross-matching a large chirality catalog with the DESI Data Release 1. The authors employ multiple cosmic-web classification schemes (V-Web, DESIVAST, Tempel+ FoF, ASTRA) and perform a wide array of statistical tests and robustness checks. The primary conclusion is a null result: spiral galaxy handedness is found to be statistically independent of large-scale structure environment, once a small, global, catalog-wide monopole (attributed to classifier systematics in a companion paper) is accounted for.

The analysis is exceptionally thorough. The use of multiple, independent classifiers and datasets (DESI, SDSS) provides strong validation for the conclusions. The detailed investigation of potential systematics, including survey geometry, tracer-program selection, and redshift-space distortions, is exemplary. The paper correctly identifies the DESIVAST-anchored analysis on a large, clean void sample as the most robust constraint.

However, the manuscript suffers from several critical procedural issues that must be addressed before it can be considered for publication in Physical Review D. The scientific analysis appears sound, but its foundations are not currently verifiable.

### ESSENTIAL Revisions

**P5-E1: Futuristic Manuscript and Reference Dating**
*   **Location:** Page 1 (author block) and Page 20 (Bibliography).
*   **Problem:** The manuscript is dated "June 4, 2026". Several key references that the analysis compares against are also given futuristic publication years: Rincón et al. [13] is cited as (2025), while Ullah et al. [11] and Zapata-Zuluaga et al. [12] are cited as (2026). This is not permissible.
*   **Fix:** The manuscript date must be corrected to the date of submission. All reference dates must be corrected to their actual publication or arXiv submission dates. If a paper is a 2024 preprint, it should be cited as such.

**P5-E2: Foundational Reliance on Unpublished Work**
*   **Location:** Abstract, Section II (p. 2), Section III A (p. 2), and throughout.
*   **Problem:** The entire analysis is predicated on the chirality labels and the crucial catalog-monopole offset (Δfcw = -0.0026) derived in "Paper IV" [3]. This reference is cited as "companion work, not yet peer-reviewed" and "in preparation". Similarly, reference [4] is "in preparation". A paper submitted to PRD must be self-contained and its results verifiable. As it stands, the primary input data for this work is unavailable to the reader or referee, making an independent verification of the results impossible. The conclusions of this paper are meaningless without the validation of Paper IV's claims.
*   **Fix:** This paper cannot be published until Paper IV [3] is publicly available, at minimum as a preprint on a service like arXiv. The reference must be updated to point to the public preprint. The same applies to any other load-bearing "in preparation" manuscripts.

### MAJOR Revisions

**P5-M1: Clarification of Statistical Formula and Application**
*   **Location:** Section V (p. 4) and various tables.
*   **Problem:** The paper defines the significance as `σ_from_half = (ncw - 0.5N) / (0.5*sqrt(N))`. This is the standard z-score in the large-N limit where the binomial variance `N*p*(1-p)` is approximated by `N*0.5*0.5`. While this is generally acceptable for p ≈ 0.5, it is more precise to use the standard error `sqrt(p*(1-p)/N)`, yielding `σ = (p - 0.5) / sqrt(p*(1-p)/N)`. My re-calculation of the cluster-class sigma (-4.66σ) required the latter, more precise formula.
*   **Fix:** The authors should explicitly state which formula is used for the final quoted sigma values. For clarity and precision, it is recommended to use the `p*(1-p)` variance throughout. If the approximation is used, the authors should briefly justify it and ensure all reported values are consistent with it.

### MINOR Revisions

**P5-M2: Emphasis on V-Web Classifier Failure at Low-z**
*   **Location:** Abstract (p. 1) and Section VIII A (p. 10).
*   **Problem:** The paper demonstrates a critical failure of the V-Web void-finding algorithm at low redshift (z < 0.24), where a cross-check reveals that 0 out of 6 V-Web-classified "void" spirals reside within a DESIVAST-defined void. This is attributed to survey-edge artifacts. This is a significant methodological finding of the paper in its own right. In the abstract, it is mentioned only parenthetically.
*   **Fix:** This finding should be stated more prominently in the abstract and discussion. It serves as a powerful justification for the choice of the DESIVAST analysis as the primary result and is a useful cautionary tale for applying cosmic-web finders to survey geometries that differ significantly from periodic boxes.

**P5-M3: Discussion of Mild Tension in Tempel+ Cross-Check**
*   **Location:** Section IX A (p. 13).
*   **Problem:** The cross-validation with the Tempel+2014 catalog is a strong feature. However, the `isolated` class (the analog to voids) shows an observed deviation of σ = -2.54. The paper's own framework predicts a deviation of σ_pred ≈ -1.26 from the propagated monopole. The observed value is twice the prediction. While this is not a statistically significant discrepancy (i.e., >3σ), it represents the largest residual tension in any of the cross-checks.
*   **Fix:** The authors should briefly acknowledge and comment on this factor-of-two difference in the text. It does not undermine the overall null conclusion but warrants a mention for completeness.

### Nitpicks (for consideration)

**P5-N1: Terminology for Multiple-Testing Correction**
*   **Location:** Section V A (p. 4).
*   **Problem:** The paper uses the term "Look-elsewhere (LEE) correction". While related, LEE is more commonly used when searching for a signal in a continuous parameter space (e.g., a resonance mass). For discrete bins (HEALPix pixels, density quintiles), the more standard term is "multiple-testing" or "multiple-comparisons" correction.
*   **Fix:** Consider replacing "Look-elsewhere (LEE) correction" with "Multiple-testing correction" for clarity.

**P5-N2: Speculative Nature of Appendix A**
*   **Location:** Appendix A (p. 19).
*   **Problem:** The toy EFT mapping is highly speculative, as the authors correctly and carefully point out by noting the operator is not derived, not rotationally invariant, and not gauge invariant.
*   **Fix:** The caveats are sufficient, but the authors might consider whether this appendix adds significant value or could be removed without detracting from the paper's core observational result. This is left to the authors' discretion.

## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, statistically rigorous paper that presents a compelling and robust null result. The breadth and depth of the robustness checks are commendable and set a high standard for this type of analysis. If the scientific content were the only criterion, it would be close to acceptance.

However, the procedural flaws are currently prohibitive. The reliance on an "in preparation" manuscript for the core dataset and its primary systematic calibration is a critical issue. Furthermore, the futuristic dating of the manuscript and its references must be corrected.

Therefore, I recommend **MAJOR REVISIONS**. The paper should be reconsidered for publication only after the essential fixes listed above are implemented, most importantly that the companion "Paper IV" is made publicly available on arXiv so that the inputs to this work can be independently scrutinized. Once these issues are resolved, the paper will represent a significant and valuable contribution to the field.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated review, incorporating the new findings from the second, more rigorous pass.

================================================================
## Referee Report on "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals"

This paper presents a comprehensive search for an environmental dependence of spiral galaxy chirality by cross-matching a large chirality catalog with the DESI Data Release 1. The authors employ multiple cosmic-web classification schemes (V-Web, DESIVAST, Tempel+ FoF, ASTRA) and perform a wide array of statistical tests and robustness checks. The primary conclusion is a null result: spiral galaxy handedness is found to be statistically independent of large-scale structure environment, once a small, global, catalog-wide monopole (attributed to classifier systematics in a companion paper) is accounted for.

The analysis is exceptionally thorough. The use of multiple, independent classifiers and datasets (DESI, SDSS) provides strong validation for the conclusions. The detailed investigation of potential systematics, including survey geometry, tracer-program selection, and redshift-space distortions, is exemplary. The paper correctly identifies the DESIVAST-anchored analysis on a large, clean void sample as the most robust constraint.

However, the manuscript suffers from several critical procedural and numerical issues that must beaddressed before it can be considered for publication in Physical Review D. The scientific analysis appears sound, but its foundations are not currently verifiable and several key results contain numerical inconsistencies.

### ESSENTIAL Revisions

**P5-E1: Futuristic Manuscript and Reference Dating**
*   **Location:** Page 1 (author block) and Page 20 (Bibliography).
*   **Problem:** The manuscript is dated "June 4, 2026". Several key references that the analysis compares against are also given futuristic publication years: Rincón et al. [13] is cited as (2025), while Ullah et al. [11] and Zapata-Zuluaga et al. [12] are cited as (2026). This is not permissible.
*   **Fix:** The manuscript date must be corrected to the date of submission. All reference dates must be corrected to their actual publication or arXiv submission dates. If a paper is a 2024 preprint, it should be cited as such.

**P5-E2: Foundational Reliance on Unpublished Work**
*   **Location:** Abstract, Section II (p. 2), Section III A (p. 2), and throughout.
*   **Problem:** The entire analysis is predicated on the chirality labels and the crucial catalog-monopole offset (Δfcw = -0.0026) derived in "Paper IV" [3]. This reference is cited as "companion work, not yet peer-reviewed" and "in preparation". Similarly, reference [4] is "in preparation". A paper submitted to PRD must be self-contained and its results verifiable. As it stands, the primary input data for this work is unavailable to the reader or referee, making an independent verification of the results impossible. The conclusions of this paper are meaningless without the validation of Paper IV's claims.
*   **Fix:** This paper cannot be published until Paper IV [3] is publicly available, at minimum as a preprint on a service like arXiv. The reference must be updated to point to the public preprint. The same applies to any other load-bearing "in preparation" manuscripts.

### MAJOR Revisions

**P5-M1: Clarification of Statistical Formula and Application**
*   **Location:** Section V (p. 4) and various tables.
*   **Problem:** The paper defines the significance as `σ_from_half = (ncw - 0.5N) / (0.5*sqrt(N))`. This is the standard z-score in the large-N limit where the binomial variance `N*p*(1-p)` is approximated by `N*0.5*0.5`. While this is generally acceptable for p ≈ 0.5, it is more precise to use the standard error `sqrt(p*(1-p)/N)`, yielding `σ = (p - 0.5) / sqrt(p*(1-p)/N)`. My re-calculation of the cluster-class sigma (-4.66σ) required the latter, more precise formula.
*   **Fix:** The authors should explicitly state which formula is used for the final quoted sigma values. For clarity and precision, it is recommended to use the `p*(1-p)` variance throughout. If the approximation is used, the authors should briefly justify it and ensure all reported values are consistent with it.

**P5-M4: Arithmetic Errors in Table VIII**
*   **Location:** Table VIII (p. 12).
*   **Problem:** Several of the reported significance values (`σ_non-void`) do not follow from the provided sample sizes (`n`) and CW fractions (`fcw`). For example, for V2-REVOLVER, the non-void sample has n ≈ 576,034 and fcw = 0.4967, which yields σ ≈ -4.98. The table reports σ = -4.94. Similarly, for V2-VIDE, the non-void sample has n ≈ 597,591 and fcw = 0.4970, which yields σ ≈ -4.64, whereas the table reports -4.59.
*   **Fix:** The authors must re-calculate all derived values in Table VIII and correct the erroneous entries. These may be stale numbers from a previous version of the analysis.

### MINOR Revisions

**P5-m2: Emphasis on V-Web Classifier Failure at Low-z**
*   **Location:** Abstract (p. 1) and Section VIII A (p. 10).
*   **Problem:** The paper demonstrates a critical failure of the V-Web void-finding algorithm at low redshift (z < 0.24), where a cross-check reveals that 0 out of 6 V-Web-classified "void" spirals reside within a DESIVAST-defined void. This is attributed to survey-edge artifacts. This is a significant methodological finding of the paper in its own right. In the abstract, it is mentioned only parenthetically.
*   **Fix:** This finding should be stated more prominently in the abstract and discussion. It serves as a powerful justification for the choice of the DESIVAST analysis as the primary result and is a useful cautionary tale for applying cosmic-web finders to survey geometries that differ significantly from periodic boxes.

**P5-m3: Discussion of Mild Tension in Tempel+ Cross-Check**
*   **Location:** Section IX A (p. 13).
*   **Problem:** The cross-validation with the Tempel+2014 catalog is a strong feature. However, the `isolated` class (the analog to voids) shows an observed deviation of σ = -2.54. The paper's own framework predicts a deviation of σ_pred ≈ -1.26 from the propagated monopole. The observed value is twice the prediction. While this is not a statistically significant discrepancy (i.e., >3σ), it represents the largest residual tension in any of the cross-checks.
*   **Fix:** The authors should briefly acknowledge and comment on this factor-of-two difference in the text. It does not undermine the overall null conclusion but warrants a mention for completeness.

**P5-m5: Inconsistent "Filament Concordance" Value**
*   **Location:** Section IX A (p. 14) and Figure 7 caption (p. 16).
*   **Problem:** The text and figure caption claim a concordance of `|f_CW^Web - f_CW^Tempel| = 0.026 pp` for the filament class. However, a direct calculation from the values in Table II (fcw = 0.4980) and Table XI (fcw = 0.4982) yields a difference of 0.02 pp (or 0.013 pp using unrounded numbers). The quoted value of 0.026 pp is inconsistent with the primary data tables.
*   **Fix:** The authors must correct this value to be consistent with their data tables or explain the source of the discrepancy.

### Nitpicks (for consideration)

**P5-N1: Terminology for Multiple-Testing Correction**
*   **Location:** Section V A (p. 4).
*   **Problem:** The paper uses the term "Look-elsewhere (LEE) correction". While related, LEE is more commonly used when searching for a signal in a continuous parameter space (e.g., a resonance mass). For discrete bins (HEALPix pixels, density quintiles), the more standard term is "multiple-testing" or "multiple-comparisons" correction.
*   **Fix:** Consider replacing "Look-elsewhere (LEE) correction" with "Multiple-testing correction" for clarity.

**P5-N2: Speculative Nature of Appendix A**
*   **Location:** Appendix A (p. 19).
*   **Problem:** The toy EFT mapping is highly speculative, as the authors correctly and carefully point out by noting the operator is not derived, not rotationally invariant, and not gauge invariant.
*   **Fix:** The caveats are sufficient, but the authors might consider whether this appendix adds significant value or could be removed without detracting from the paper's core observational result. This is left to the authors' discretion.

## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, statistically rigorous paper that presents a compelling and robust null result. The breadth and depth of the robustness checks are commendable and set a high standard for this type of analysis. If the scientific content were the only criterion, it would be close to acceptance.

However, the procedural flaws are currently prohibitive. The reliance on an "in preparation" manuscript for the core dataset and its primary systematic calibration is a critical issue. Furthermore, the futuristic dating of the manuscript and its references must be corrected. Finally, several numerical values in key tables and figures are arithmetically inconsistent with the provided inputs, which undermines confidence in the results and must be fixed.

Therefore, I recommend **MAJOR REVISIONS**. The paper should be reconsidered for publication only after the essential and major fixes listed above are implemented. Most importantly, the companion "Paper IV" must be made publicly available on arXiv so that the inputs to this work can be independently scrutinized. Once these issues are resolved, the paper will represent a significant and valuable contribution to the field.