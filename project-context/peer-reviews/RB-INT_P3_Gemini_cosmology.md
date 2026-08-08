# P3 RB-INT — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=b5565d8e pages=30
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (9709 chars)
**Wall time**: 158.4s

---

## Referee Report: P3-RB-INT

**Manuscript Title:** Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 269,317 Recommended-Tier (378,280 Total) Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches

**Recommendation:** MINOR REVISIONS

### Summary

This manuscript presents a large-scale, multi-survey anomaly detection campaign, resulting in a catalog of 378,280 unique anomalous sources and sky regions. The work is methodologically sophisticated, employing a per-survey native retraining protocol ("Path-C") to overcome the challenges of cross-domain transfer learning, which the authors demonstrate can lead to significant contamination. The paper is exceptionally well-documented, transparent about its limitations, and rigorous in its validation procedures, including k-fold cross-validation, out-of-distribution testing, and injection-recovery gates. The cosmological applications, particularly the constraints on primordial non-Gaussianity (fNL) and the consistency check of the NANOGrav signal with matter-bounce models, are presented with appropriate scientific caution, correctly distinguishing between forecasts, constraints, and detections. The distinction between database coverage (e.g., "SIMBAD-unmatched") and genuine, deep-catalog novelty is a crucial and well-executed aspect of the analysis.

The paper represents a significant contribution to the field and is well-suited for publication in Physical Review D. The required revisions are minor and primarily aimed at improving the clarity of presentation for some of the key summary results.

---

### Detailed Findings

#### MAJOR
*(No findings classified as MAJOR.)*

#### MINOR

**P3-M1 | Section III, Page 9, Table I | Clarity of the main summary table**
*   **Problem:** Table I, the primary summary of the survey results, is difficult to parse because the `N_anom` column mixes counts from the initial cross-transfer scan (for SDSS, LAMOST) with the final, canonical native-retrained counts (for DESI, etc.). A reader must synthesize information from multiple dense footnotes to understand the final composition of the catalog. For example, the LAMOST entry lists "44,075+", while the final catalog count used for the total is 113,342. This presentation obscures the final, most important results.
*   **Fix:** Revise Table I to improve clarity. I recommend the following structure: Create a new column for the final, canonical `N_anom` (Path-C native-retrained) counts that are used to compute the `Path-C unique` total. The initial cross-transfer counts, which serve as a crucial verification baseline, can be retained in a separate column labeled "Cross-transfer count (baseline)" or moved to the footnotes. This will allow a reader to see the final survey-by-survey contributions to the headline number at a glance.

**P3-M2 | Section II B, Page 8, Figure 3 | Incomplete visual comparison of score distributions**
*   **Problem:** The right panel of Figure 3 powerfully illustrates the "cross-transfer-to-native score-axis effect" for SDSS, showing how the native re-score compresses the extreme scores from the transfer-learning run. The caption notes that the LAMOST curve in the left panel is also from the pre-Path-C cross-transfer scan. However, the plot does not show the corresponding native-retrained distribution for LAMOST. This is a missed opportunity to visually demonstrate the effect of mitigating the "98% blue-excess" training-bias artifact, which is a central methodological lesson of the paper.
*   **Fix:** Add the native-retrained score distributions for both SDSS and LAMOST to Figure 3. This could be done with a new panel or by overlaying them on the existing plots (e.g., as a dashed line of the same color). This would provide a much stronger, self-contained visual summary of the impact and success of the Path-C native-retrain protocol.

#### NIT (Nit-pick/Cosmetic)

**P3-N1 | Section I, Page 1, Title Block | Future date**
*   **Problem:** The paper is dated "June 28, 2026". This is a placeholder and should be corrected to the submission date.
*   **Fix:** Update the date to the current date of submission.

**P3-N2 | Various locations | Use of "superseded"**
*   **Problem:** The paper uses the word "superseded" in several places (e.g., Fig. 2 caption, Table I footnotes) to describe how the native-retrained results replace the cross-transfer baseline. This is a form of version-history language that can be slightly confusing.
*   **Fix:** Rephrase to be more direct. For example, instead of "superseded by the Path-C native catalog", consider "The final Path-C catalog is derived from these native-retrained counts, which replace the initial cross-transfer results shown here for verification."

**P3-N3 | Section III E, Page 12, Table IV | Ambiguity of eROSITA score column**
*   **Problem:** The text correctly and commendably establishes that the eROSITA tier is a membership list only, with an irreproducible `S_BigAE` score axis. However, Table IV then presents a column `S_IF,raw` (raw Isolation Forest score). The caption explains this is "not a parallel catalog axis" but is included for mapping between detectors. This inclusion, even with the caveat, slightly undermines the "membership-list-only" framing and could cause confusion.
*   **Fix:** Consider removing the `S_IF,raw` column from Table IV to make the "membership-list-only" nature of the eROSITA tier unambiguous. If a reproducible score is desired, the raw, per-object reconstruction MSE from the autoencoder (Eq. 1) could be provided if that artifact is available and its axis is monotonic. Otherwise, omitting the score column entirely is the clearest option.

**P3-N4 | Section IV A, Page 14 | Inconsistent number of cross-matches**
*   **Problem:** The text states: "comparable to the 3 observed matches of §IV C (identified in the cross-transfer-era cross-match...)." A few sentences later, it reports a re-run on the final released catalogs which "yields 4 raw positional matches". The text should be internally consistent.
*   **Fix:** Update the first sentence to refer to the 4 matches found in the final catalog analysis, or clarify that the "3 matches" refers specifically to the set discussed in §IV C as case studies, while the total number of raw matches is 4.

---
## Summary recommendation

**MINOR REVISIONS**

This is an excellent and comprehensive paper that sets a high standard for methodological rigor in large-scale anomaly detection. The authors' transparency regarding provenance issues, careful validation, and conservative interpretation of results is exemplary. The work is a significant contribution and is highly suitable for publication. The recommended revisions are minor and are intended to enhance the clarity of the presentation of the final results, ensuring the paper's significant findings are as accessible as possible to the reader.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated referee report, incorporating findings from the "fresh eyes" re-review.

================================================================
## Referee Report: P3-RB-INT

**Manuscript Title:** Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 269,317 Recommended-Tier (378,280 Total) Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches

**Recommendation:** MINOR REVISIONS

### Summary

This manuscript presents a large-scale, multi-survey anomaly detection campaign, resulting in a catalog of 378,280 unique anomalous sources and sky regions. The work is methodologically sophisticated, employing a per-survey native retraining protocol ("Path-C") to overcome the challenges of cross-domain transfer learning, which the authors demonstrate can lead to significant contamination. The paper is exceptionally well-documented, transparent about its limitations, and rigorous in its validation procedures, including k-fold cross-validation, out-of-distribution testing, and injection-recovery gates. The cosmological applications, particularly the constraints on primordial non-Gaussianity (fNL) and the consistency check of the NANOGrav signal with matter-bounce models, are presented with appropriate scientific caution, correctly distinguishing between forecasts, constraints, and detections. The distinction between database coverage (e.g., "SIMBAD-unmatched") and genuine, deep-catalog novelty is a crucial and well-executed aspect of the analysis.

The paper represents a significant contribution to the field and is well-suited for publication in Physical Review D. The required revisions are minor and primarily aimed at improving the clarity and numerical consistency of the presentation for some of the key summary results.

---

### Detailed Findings

#### MAJOR

**P3-A1 | Abstract and Section I | Reconciliation of headline catalog counts**
*   **Problem:** The primary, headline numbers for the size of the validated/recommended catalog subsets are not reconcilable from the other numbers provided in the paper. The abstract introduces a "validated catalog-grade subset of ≥ 268,519 unique anomalies" and a "recommended tier" of "269,317 unique entries". However, no straightforward arithmetic using the total unique count (378,280) and the counts of the various exploratory tiers (LAMOST: 113,342; Gaia: 500; eROSITA: 298) can reproduce these numbers. For example, subtracting all exploratory components from the total unique count (`378,280 - 113,342 - 500 - 298`) yields 264,140, which matches neither headline figure. This numerical inconsistency in the paper's most prominent result is a critical issue for clarity and reproducibility.
*   **Fix:** The authors must clarify the exact definition of the "validated subset" and "recommended tier" and provide a clear, explicit calculation that allows a reader to derive the headline counts (≥ 268,519 and 269,317) from the total unique count and the per-survey component counts. This calculation should be presented prominently in the abstract or the introduction to resolve the ambiguity.

#### MINOR

**P3-M1 | Section III, Page 9, Table I | Clarity of the main summary table**
*   **Problem:** Table I, the primary summary of the survey results, is difficult to parse because the `N_anom` column mixes counts from the initial cross-transfer scan (for SDSS, LAMOST) with the final, canonical native-retrained counts (for DESI, etc.). A reader must synthesize information from multiple dense footnotes to understand the final composition of the catalog. For example, the LAMOST entry lists "44,075+", while the final catalog count used for the total is 113,342. This presentation obscures the final, most important results.
*   **Fix:** Revise Table I to improve clarity. I recommend the following structure: Create a new column for the final, canonical `N_anom` (Path-C native-retrained) counts that are used to compute the `Path-C unique` total. The initial cross-transfer counts, which serve as a crucial verification baseline, can be retained in a separate column labeled "Cross-transfer count (baseline)" or moved to the footnotes. This will allow a reader to see the final survey-by-survey contributions to the headline number at a glance.

**P3-M2 | Section II B, Page 8, Figure 3 | Incomplete visual comparison of score distributions**
*   **Problem:** The right panel of Figure 3 powerfully illustrates the "cross-transfer-to-native score-axis effect" for SDSS, showing how the native re-score compresses the extreme scores from the transfer-learning run. The caption notes that the LAMOST curve in the left panel is also from the pre-Path-C cross-transfer scan. However, the plot does not show the corresponding native-retrained distribution for LAMOST. This is a missed opportunity to visually demonstrate the effect of mitigating the "98% blue-excess" training-bias artifact, which is a central methodological lesson of the paper.
*   **Fix:** Add the native-retrained score distributions for both SDSS and LAMOST to Figure 3. This could be done with a new panel or by overlaying them on the existing plots (e.g., as a dashed line of the same color). This would provide a much stronger, self-contained visual summary of the impact and success of the Path-C native-retrain protocol.

**P3-B1 | Section III C and Figure 3/8 Captions | Sourcing of SDSS native score compression**
*   **Problem:** The captions for Figure 3 and Figure 8 state that the SDSS native re-score compresses extreme anomaly scores to "S < 14". However, this specific numerical bound is not explicitly stated or derived in the referenced body text (§III C). While the qualitative point about compression is well-made, the quantitative claim should be sourced directly in the main text.
*   **Fix:** Add a sentence to the main text of Section III C that states and briefly explains the "S < 14" result for the native-retrained SDSS anomalies.

#### NIT (Nit-pick/Cosmetic)

**P3-N1 | Section I, Page 1, Title Block | Future date**
*   **Problem:** The paper is dated "June 28, 2026". This is a placeholder and should be corrected to the submission date.
*   **Fix:** Update the date to the current date of submission.

**P3-N2 | Various locations | Use of "superseded"**
*   **Problem:** The paper uses the word "superseded" in several places (e.g., Fig. 2 caption, Table I footnotes) to describe how the native-retrained results replace the cross-transfer baseline. This is a form of version-history language that can be slightly confusing.
*   **Fix:** Rephrase to be more direct. For example, instead of "superseded by the Path-C native catalog", consider "The final Path-C catalog is derived from these native-retrained counts, which replace the initial cross-transfer results shown here for verification."

**P3-N3 | Section III E, Page 12, Table IV | Ambiguity of eROSITA score column**
*   **Problem:** The text correctly and commendably establishes that the eROSITA tier is a membership list only, with an irreproducible `S_BigAE` score axis. However, Table IV then presents a column `S_IF,raw` (raw Isolation Forest score). The caption explains this is "not a parallel catalog axis" but is included for mapping between detectors. This inclusion, even with the caveat, slightly undermines the "membership-list-only" framing and could cause confusion.
*   **Fix:** Consider removing the `S_IF,raw` column from Table IV to make the "membership-list-only" nature of the eROSITA tier unambiguous. If a reproducible score is desired, the raw, per-object reconstruction MSE from the autoencoder (Eq. 1) could be provided if that artifact is available and its axis is monotonic. Otherwise, omitting the score column entirely is the clearest option.

**P3-N4 | Section IV A, Page 14 | Inconsistent number of cross-matches**
*   **Problem:** The text states: "comparable to the 3 observed matches of §IV C (identified in the cross-transfer-era cross-match...)." A few sentences later, it reports a re-run on the final released catalogs which "yields 4 raw positional matches". The text should be internally consistent.
*   **Fix:** Update the first sentence to refer to the 4 matches found in the final catalog analysis, or clarify that the "3 matches" refers specifically to the set discussed in §IV C as case studies, while the total number of raw matches is 4.

**P3-C1 | Appendix E, Page 26, Eq. E1 | Dimensional consistency of PTA likelihood**
*   **Problem:** Equation E1, representing the log-likelihood for the PTA analysis, appears to be dimensionally inconsistent. The argument of a logarithm must be dimensionless, but the terms on the right-hand side do not appear to cancel to a dimensionless quantity.
*   **Fix:** Please verify Equation E1 against the source implementation (`ceffyl` likelihood product). If the equation is transcribed correctly, please add a note clarifying the units of the terms (`p_i`, `A`, etc.) and how they combine to form a dimensionless argument. If it is incorrect, please provide the corrected, dimensionally consistent equation.

---
## Summary recommendation

**MINOR REVISIONS**

This is an excellent and comprehensive paper that sets a high standard for methodological rigor in large-scale anomaly detection. The authors' transparency regarding provenance issues, careful validation, and conservative interpretation of results is exemplary. The work is a significant contribution and is highly suitable for publication. The recommended revisions are intended to enhance the clarity and numerical consistency of the presentation of the final results, ensuring the paper's significant findings are as accessible as possible to the reader.