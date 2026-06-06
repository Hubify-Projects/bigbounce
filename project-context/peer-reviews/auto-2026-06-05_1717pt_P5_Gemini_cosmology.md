# P5 auto-2026-06-05_1717pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (13092 chars)
**Wall time**: 180.0s

---

## Referee Report on "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals"

This paper presents a detailed investigation into the potential correlation between spiral galaxy chirality and large-scale structure environment, using a cross-match between a new galaxy chirality catalog and the DESI Data Release 1. The primary result is a null detection: after accounting for a catalog-wide systematic offset (a "classifier monopole"), no statistically significant dependence of spiral handedness on cosmic-web environment (void, wall, filament, cluster) is found. The analysis is supported by an extensive suite of robustness checks, including the use of multiple environment classifiers, sensitivity tests of analysis parameters, and various data stratifications to isolate potential systematics.

While the core analysis is thorough and the approach to systematics is commendable, the manuscript in its current form has several essential and major issues that preclude its publication in Physical Review D. The paper requires major revisions to address these concerns.

---

### ESSENTIAL Revisions

**P5-E1: Dependency on Unpublished, Non-Peer-Reviewed Work**
*   **Location:** Abstract (p. 1), Introduction (p. 2), Section II (p. 2), Bibliography (p. 20)
*   **Problem:** The entire analysis is predicated on the galaxy chirality catalog from "Paper IV" [3], which is repeatedly cited as a "companion work, not yet peer-reviewed" and "in preparation". The validity, quality, and systematic properties of this input catalog are fundamental to every result in this manuscript. Basing a PRD paper entirely on an unpublished and unreviewed dataset is not acceptable.
*   **Fix:** This manuscript can only be properly reviewed if Paper IV is submitted concurrently to a peer-reviewed journal (ideally as a companion paper to the same journal) and made available to the referee. Alternatively, the author must provide a full description of the catalog generation, validation, and systematic characterization within this paper, likely in an extensive appendix.

**P5-E2: Placeholder and Future-Dated References**
*   **Location:** Bibliography (p. 20), various citations throughout.
*   **Problem:** The bibliography contains multiple references with future publication years (e.g., 2025, 2026) and what appear to be placeholder or future-dated arXiv identifiers (e.g., 2604.XXXX, 2411.XXXX). For example, [11], [12], and [13] are all cited with future dates. This is not permissible in a formal submission.
*   **Fix:** The author must update all references with their correct, current publication status, DOIs, and arXiv identifiers. If a work is a preprint, it should be cited as such with the correct date. If it is not yet public, it cannot be cited in this manner.

**P5-E3: Misleading Statement on Parity Violation**
*   **Location:** Introduction, p. 2, paragraph 1.
*   **Problem:** The text states that Paper IV finds a global CW fraction "consistent with parity at ~ 1σ". However, the numbers provided (`0.4974 ± 0.000279`) correspond to a `(0.4974 - 0.5) / 0.000279 = -9.3σ` deviation from parity. The text later clarifies this is treated as a "classifier-monopole offset", but the initial statement is factually incorrect and highly misleading.
*   **Fix:** Rephrase this sentence to be accurate from the outset. For example: "Paper IV [3] ... establishes a global CW fraction of 0.4974 ± 0.000279. While this represents a >9σ deviation from parity, it is demonstrated to be a spatially uniform classifier-monopole offset rather than a cosmological signal. The present paper tests for environmental variations around this global offset."

**P5-E4: Incorrect Statistical Threshold Calculations**
*   **Location:** Section V A (p. 4), Section VII (p. 9)
*   **Problem:** Several calculations of Bonferroni-corrected significance thresholds are incorrect.
    1.  On p. 4, for K=1054 HEALPix pixels at α=0.05, the threshold `|σ|_Bonf` is given as ~4.05. My calculation yields ~4.60.
    2.  On p. 9, for the Phase 2 sweep with K=9 cells at α=0.05, the threshold `|σ|_Bonf` is given as ~3.02. My calculation yields ~2.77 (for a two-sided test). The value 3.02 corresponds to a different significance level.
*   **Fix:** The author must systematically review and correct all statistical threshold calculations throughout the manuscript. The exact definition being used (e.g., one-sided vs. two-sided test) must be explicitly stated and consistently applied. These corrections may alter the interpretation of whether certain marginal signals cross the significance threshold.

**P5-E5: Typo in DESI DR1 Input Size**
*   **Location:** Abstract, p. 1.
*   **Problem:** The abstract states the DESI DR1 redshift catalog has "16.4 × 10⁹ ZWARN=0 input rows". This is 16.4 billion, which is three orders of magnitude too large. The correct number is approximately 16.4 million.
*   **Fix:** Correct 10⁹ to 10⁶.

### MAJOR Revisions

**P5-M1: Speculative and Non-Rigorous EFT Appendix**
*   **Location:** Appendix A, p. 19.
*   **Problem:** Appendix A presents a "toy EFT mapping" of the observational bound. The author correctly admits that the proposed operator is not rotationally or gauge-invariant and is merely a "heuristic parametrization". This level of speculation and lack of rigor is not suitable for an appendix in a PRD paper, which should contain robust technical derivations. It detracts from the solidity of the main observational result.
*   **Fix:** This appendix should be removed. The author can briefly mention the goal of connecting such null results to fundamental theory in the main discussion section, but this specific "toy model" is not sufficiently developed for inclusion.

**P5-M2: Internal Metadata/Nomenclature in Text**
*   **Location:** Section VIII F, p. 12.
*   **Problem:** The section is titled "Cross-survey P4-monopole-residual analysis" and discusses the "P5 matched-spiral catalog monopole". The tags "P4" and "P5" appear to be internal project names or paper tags (the reviewer metadata block confirms "P5" is the tag for this paper) that have leaked into the manuscript. This is unprofessional and confusing for the reader.
*   **Fix:** Remove all internal jargon like "P4" and "P5". Refer to the catalogs and concepts by their descriptive names (e.g., "the Paper IV catalog", "the matched-spiral subsample used in this work").

### MINOR Revisions

**P5-N1: Incomplete Sentence**
*   **Location:** Section VIII F, p. 12, end of paragraph.
*   **Problem:** The sentence "All four V-Web classes fall within |σ_vs_monopole| <" is incomplete. The value is given in Table X on the next page as 1.15.
*   **Fix:** Complete the sentence with the value, e.g., "...fall within |σ_vs_monopole| < 1.15."

**P5-N2: Inconsistent Calculation of Predicted Sigma**
*   **Location:** Section VI A, p. 5.
*   **Problem:** The predicted sigma for the filament class is given as `σ_pred(filament) ≈ -3.16`. A direct calculation using the provided numbers (`Δfcw = -0.0026`, `n=408187`) yields `σ_pred ≈ -3.32`. The value for the cluster class, however, is calculated correctly.
*   **Fix:** Re-calculate and correct the value for `σ_pred(filament)`.

**P5-N3: Opaque Statement in Logistic Regression**
*   **Location:** Section VI B, p. 6.
*   **Problem:** The text mentions a logistic regression with "no significant intercept (0.000652)". This is ambiguous. The value of the intercept is given, but "no significant" should be supported by a p-value or confidence interval.
*   **Fix:** Clarify the statement by providing the p-value for the intercept term.

**P5-N4: Unprofessional Notation**
*   **Location:** Section IX A, p. 14.
*   **Problem:** The text includes the notation `(√ within spec)`. This is informal and not appropriate for a scientific publication.
*   **Fix:** Replace this with standard prose, e.g., "(a concordance well within the 0.2 pp requirement)".

**P5-N5: Incomplete URL**
*   **Location:** Section III B, p. 3.
*   **Problem:** The URL provided for the DESI DR1 zcatalog points to a directory, not a specific file.
*   **Fix:** Update the URL to be more specific if possible, or clarify that it is a directory containing the relevant data products.

### NIT (Cosmetic)

**P5-T1: Typo in Abstract**
*   **Location:** Abstract, p. 1.
*   **Problem:** The text reads "none reach 30 after look-elsewhere correction".
*   **Fix:** Change "30" to "3σ".

**P5-T2: Editorializing in Filename**
*   **Location:** Section III B, p. 3.
*   **Problem:** The file is referred to as "canonical zall-pix-iron.fits". The word "canonical" is an editorialization.
*   **Fix:** Refer to the file by its official name, `zall-pix-iron.fits`.

---

## Summary recommendation

**MAJOR REVISIONS**

This paper presents a potentially valuable and robust null result that could serve as an important empirical constraint on parity-violating physics. The author's approach of performing a deep dive into systematics and conducting an exhaustive set of cross-checks is a significant strength. However, the manuscript is critically undermined by its complete reliance on an unpublished, non-peer-reviewed input catalog (Paper IV) and the presence of numerous placeholder/future-dated references, which is unacceptable for a formal submission. Furthermore, several incorrect statistical calculations cast doubt on the quantitative interpretation of the results.

Before this paper can be considered for publication in Physical Review D, the author must, at a minimum, resolve the provenance of the input catalog (P5-E1), correct all references (P5-E2), fix the misleading statements about parity (P5-E3), and systematically correct all statistical calculations (P5-E4). The other major and minor points should also be addressed to bring the manuscript up to the required standard of quality and professionalism. If these essential and major issues are thoroughly addressed, the revised manuscript could be a solid contribution to the field.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the review you just wrote on this paper:

================================================================
## Referee Report on "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals"

This paper presents a detailed investigation into the potential correlation between spiral galaxy chirality and large-scale structure environment, using a cross-match between a new galaxy chirality catalog and the DESI Data Release 1. The primary result is a null detection: after accounting for a catalog-wide systematic offset (a "classifier monopole"), no statistically significant dependence of spiral handedness on cosmic-web environment (void, wall, filament, cluster) is found. The analysis is supported by an extensive suite of robustness checks, including the use of multiple environment classifiers, sensitivity tests of analysis parameters, and various data stratifications to isolate potential systematics.

While the core analysis is thorough and the approach to systematics is commendable, the manuscript in its current form has several essential and major issues that preclude its publication in Physical Review D. The paper requires major revisions to address these concerns.

---

### ESSENTIAL Revisions

**P5-E1: Dependency on Unpublished, Non-Peer-Reviewed Work**
*   **Location:** Abstract (p. 1), Introduction (p. 2), Section II (p. 2), Bibliography (p. 20)
*   **Problem:** The entire analysis is predicated on the galaxy chirality catalog from "Paper IV" [3], which is repeatedly cited as a "companion work, not yet peer-reviewed" and "in preparation". The validity, quality, and systematic properties of this input catalog are fundamental to every result in this manuscript. Basing a PRD paper entirely on an unpublished and unreviewed dataset is not acceptable.
*   **Fix:** This manuscript can only be properly reviewed if Paper IV is submitted concurrently to a peer-reviewed journal (ideally as a companion paper to the same journal) and made available to the referee. Alternatively, the author must provide a full description of the catalog generation, validation, and systematic characterization within this paper, likely in an extensive appendix.

**P5-E2: Placeholder and Future-Dated References**
*   **Location:** Bibliography (p. 20), various citations throughout.
*   **Problem:** The bibliography contains multiple references with future publication years (e.g., 2025, 2026) and what appear to be placeholder or future-dated arXiv identifiers (e.g., 2604.XXXX, 2411.XXXX). For example, [11], [12], and [13] are all cited with future dates. This is not permissible in a formal submission.
*   **Fix:** The author must update all references with their correct, current publication status, DOIs, and arXiv identifiers. If a work is a preprint, it should be cited as such with the correct date. If it is not yet public, it cannot be cited in this manner.

**P5-E3: Misleading Statement on Parity Violation**
*   **Location:** Introduction, p. 2, paragraph 1.
*   **Problem:** The text states that Paper IV finds a global CW fraction "consistent with parity at ~ 1σ". However, the numbers provided (`0.4974 ± 0.000279`) correspond to a `(0.4974 - 0.5) / 0.000279 = -9.3σ` deviation from parity. The text later clarifies this is treated as a "classifier-monopole offset", but the initial statement is factually incorrect and highly misleading.
*   **Fix:** Rephrase this sentence to be accurate from the outset. For example: "Paper IV [3] ... establishes a global CW fraction of 0.4974 ± 0.000279. While this represents a >9σ deviation from parity, it is demonstrated to be a spatially uniform classifier-monopole offset rather than a cosmological signal. The present paper tests for environmental variations around this global offset."

**P5-E4: Incorrect Statistical Threshold Calculations**
*   **Location:** Section V A (p. 4), Section VII (p. 9)
*   **Problem:** Several calculations of Bonferroni-corrected significance thresholds are incorrect.
    1.  On p. 4, for K=1054 HEALPix pixels at α=0.05, the threshold `|σ|_Bonf` is given as ~4.05. My calculation yields ~4.60.
    2.  On p. 9, for the Phase 2 sweep with K=9 cells at α=0.05, the threshold `|σ|_Bonf` is given as ~3.02. My calculation yields ~2.77 (for a two-sided test). The value 3.02 corresponds to a different significance level.
*   **Fix:** The author must systematically review and correct all statistical threshold calculations throughout the manuscript. The exact definition being used (e.g., one-sided vs. two-sided test) must be explicitly stated and consistently applied. These corrections may alter the interpretation of whether certain marginal signals cross the significance threshold.

**P5-E5: Typo in DESI DR1 Input Size**
*   **Location:** Abstract, p. 1.
*   **Problem:** The abstract states the DESI DR1 redshift catalog has "16.4 × 10⁹ ZWARN=0 input rows". This is 16.4 billion, which is three orders of magnitude too large. The correct number is approximately 16.4 million.
*   **Fix:** Correct 10⁹ to 10⁶.

### MAJOR Revisions

**P5-M1: Speculative and Non-Rigorous EFT Appendix**
*   **Location:** Appendix A, p. 19.
*   **Problem:** Appendix A presents a "toy EFT mapping" of the observational bound. The author correctly admits that the proposed operator is not rotationally or gauge-invariant and is merely a "heuristic parametrization". This level of speculation and lack of rigor is not suitable for an appendix in a PRD paper, which should contain robust technical derivations. It detracts from the solidity of the main observational result.
*   **Fix:** This appendix should be removed. The author can briefly mention the goal of connecting such null results to fundamental theory in the main discussion section, but this specific "toy model" is not sufficiently developed for inclusion.

**P5-M2: Internal Metadata/Nomenclature in Text**
*   **Location:** Section VIII F, p. 12.
*   **Problem:** The section is titled "Cross-survey P4-monopole-residual analysis" and discusses the "P5 matched-spiral catalog monopole". The tags "P4" and "P5" appear to be internal project names or paper tags (the reviewer metadata block confirms "P5" is the tag for this paper) that have leaked into the manuscript. This is unprofessional and confusing for the reader.
*   **Fix:** Remove all internal jargon like "P4" and "P5". Refer to the catalogs and concepts by their descriptive names (e.g., "the Paper IV catalog", "the matched-spiral subsample used in this work").

### MINOR Revisions

**P5-N1: Incomplete Sentence**
*   **Location:** Section VIII F, p. 12, end of paragraph.
*   **Problem:** The sentence "All four V-Web classes fall within |σ_vs_monopole| <" is incomplete. The value is given in Table X on the next page as 1.15.
*   **Fix:** Complete the sentence with the value, e.g., "...fall within |σ_vs_monopole| < 1.15."

**P5-N2: Inconsistent Calculation of Predicted Sigma**
*   **Location:** Section VI A, p. 5.
*   **Problem:** The predicted sigma for the filament class is given as `σ_pred(filament) ≈ -3.16`. A direct calculation using the provided numbers (`Δfcw = -0.0026`, `n=408187`) yields `σ_pred ≈ -3.32`. The value for the cluster class, however, is calculated correctly.
*   **Fix:** Re-calculate and correct the value for `σ_pred(filament)`.

**P5-N3: Opaque Statement in Logistic Regression**
*   **Location:** Section VI B, p. 6.
*   **Problem:** The text mentions a logistic regression with "no significant intercept (0.000652)". This is ambiguous. The value of the intercept is given, but "no significant" should be supported by a p-value or confidence interval.
*   **Fix:** Clarify the statement by providing the p-value for the intercept term.

**P5-N4: Unprofessional Notation**
*   **Location:** Section IX A, p. 14.
*   **Problem:** The text includes the notation `(√ within spec)`. This is informal and not appropriate for a scientific publication.
*   **Fix:** Replace this with standard prose, e.g., "(a concordance well within the 0.2 pp requirement)".

**P5-N5: Incomplete URL**
*   **Location:** Section III B, p. 3.
*   **Problem:** The URL provided for the DESI DR1 zcatalog points to a directory, not a specific file.
*   **Fix:** Update the URL to be more specific if possible, or clarify that it is a directory containing the relevant data products.

### NIT (Cosmetic)

**P5-T1: Typo in Abstract**
*   **Location:** Abstract, p. 1.
*   **Problem:** The text reads "none reach 30 after look-elsewhere correction".
*   **Fix:** Change "30" to "3σ".

**P5-T2: Editorializing in Filename**
*   **Location:** Section III B, p. 3.
*   **Problem:** The file is referred to as "canonical zall-pix-iron.fits". The word "canonical" is an editorialization.
*   **Fix:** Refer to the file by its official name, `zall-pix-iron.fits`.

---

## Summary recommendation

**MAJOR REVISIONS**

This paper presents a potentially valuable and robust null result that could serve as an important empirical constraint on parity-violating physics. The author's approach of performing a deep dive into systematics and conducting an exhaustive set of cross-checks is a significant strength. However, the manuscript is critically undermined by its complete reliance on an unpublished, non-peer-reviewed input catalog (Paper IV) and the presence of numerous placeholder/future-dated references, which is unacceptable for a formal submission. Furthermore, several incorrect statistical calculations cast doubt on the quantitative interpretation of the results.

Before this paper can be considered for publication in Physical Review D, the author must, at a minimum, resolve the provenance of the input catalog (P5-E1), correct all references (P5-E2), fix the misleading statements about parity (P5-E3), and systematically correct all statistical calculations (P5-E4). The other major and minor points should also be addressed to bring the manuscript up to the required standard of quality and professionalism. If these essential and major issues are thoroughly addressed, the revised manuscript could be a solid contribution to the field.
================================================================

### Additional Findings from Second Review

The following issues were identified during a more detailed, second-pass review of the manuscript.

---

### ESSENTIAL Revisions

**P5-E6: Inconsistent Total Sample Size**
*   **Location:** Abstract (p. 1), Table II (p. 5), Figure 2 (p. 5), Figure 7 (p. 16), and multiple mentions in the text.
*   **Problem:** The manuscript is internally inconsistent regarding the size of the primary sample. The abstract, figure captions, and main text repeatedly quote a total "chirality-relevant" sample size of `n = 791,635`. However, the primary results table (Table II) and its corresponding figure (Fig 2) contain data for the four cosmic-web classes that sum to a total of `n = 812,793`. This discrepancy of 21,158 galaxies is significant and confusing. The explanation provided on p. 12 is opaque and appears to be a post-hoc justification, failing to clarify why the "headline" table uses a different sample size than the "headline" text.
*   **Fix:** The author must use one consistent sample for the headline analysis. All numbers in the abstract, text, tables, and figures must be updated to reflect this single, well-defined sample. If two different samples are indeed used for different purposes, their definitions and the reason for the difference must be stated clearly and upfront, not buried in a later section.

### MAJOR Revisions

**P5-M3: Arithmetic Discrepancies in Key Tables**
*   **Location:** Table III (p. 6), Table VIII (p. 12)
*   **Problem:** A re-computation of the statistical quantities in several tables reveals discrepancies.
    1.  **Table III:** The observed sigma values (`σ_obs`) for the projected-density quintiles do not precisely match the values calculated from the provided `fcw` and `N`. For example, for Quintile 3 (`fcw=0.4950`), the calculated `σ` is -3.98, while the table reports -3.94. While small, these discrepancies should be resolved.
    2.  **Table VIII:** The `Δfcw` column, which shows the difference in CW fraction between void and non-void galaxies for the three DESIVAST algorithms, appears to have the incorrect sign for all three entries if the natural definition `f_void - f_non-void` is assumed.
*   **Fix:** The author must perform a thorough check of all derived numerical values in all tables. Any discrepancies must be corrected. The definition of columns like `Δfcw` must be stated explicitly in the table caption (e.g., `Δfcw ≡ f_void - f_non-void`) and the values must match that definition.

### MINOR Revisions

**P5-N6: Incorrect Internal Cross-Reference**
*   **Location:** Section X, p. 17.
*   **Problem:** In the summary list of robustness checks, the text refers to the "DESIVAST per-galaxy cross-match, §IXB". The correct section describing this analysis is §VIII B.
*   **Fix:** Correct the cross-reference from §IXB to §VIII B.