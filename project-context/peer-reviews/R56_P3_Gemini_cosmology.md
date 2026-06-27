# P3 R56 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/R56_P3/paper3_draft.pdf` md5=08baa6e5 pages=30
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (8341 chars)
**Wall time**: 180.3s

---

Here is a complete referee report for the submitted paper.

---

## Referee Report: P3-R56

**Paper:** Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches

This paper presents a large-scale anomaly detection analysis across seven astronomical surveys, resulting in a catalog of over 378,000 unique anomalous sources. The work is notable for its scale, its multi-survey "native retrain" methodology, and its transparent and rigorous validation framework. The authors apply the resulting catalog to two cosmological problems: constraining primordial non-Gaussianity (f_NL) and testing bouncing cosmology predictions against NANOGrav data.

The paper is exceptionally thorough, well-written, and intellectually honest. The authors take great care to document not only the successes but also the failures of their methodology (e.g., the LAMOST training bias, the ACT cross-transfer failure, the irreproducibility of the eROSITA score axis). The distinction between large "headline" numbers and more carefully defined "like-for-like" comparisons is made explicit and is crucial for a correct interpretation of the results. The cosmological applications are presented with a commendable level of caution, correctly identifying null results and highlighting important caveats. The appendices provide extensive documentation that is essential for reproducibility.

The work represents a significant contribution to the field of astronomical anomaly detection and provides a valuable public data product. The methodological lessons, particularly regarding training bias and cross-survey validation, are of broad importance. While the paper is of very high quality, a few points should be addressed before publication.

---

### Findings

#### ESSENTIAL

*   **P3-E1: Artifact in Date**
    *   **Section/Page:** 1 (Title block)
    *   **Problem:** The paper is dated "(Dated: June 26, 2026)". This is a future date and is clearly a placeholder or artifact.
    *   **Fix:** Replace the date with the correct submission or acceptance date.

#### MAJOR

*   **P3-M1: Ambiguous Presentation in Main Summary Table (Table I)**
    *   **Section/Page:** 7 (Table I)
    *   **Problem:** Table I, the primary summary of the survey results, is confusingly structured. The `N_anom` column presents a mix of final "Path-C" native-retrained counts (for DESI) and initial "cross-transfer" counts (e.g., for LAMOST and SDSS) that are explicitly superseded in the text and footnotes. A reader looking only at the table would get an incorrect impression of the final catalog's composition (e.g., seeing 44,075 LAMOST anomalies instead of the final 113,342). The footnotes are required to understand the canonical results, which is not ideal for a central table.
    *   **Fix:** Revise Table I to exclusively show the final, canonical "Path-C" anomaly counts for all surveys in the main `N_anom` column. The superseded cross-transfer counts, which are valuable for demonstrating the methodological improvement, should be moved to a separate column explicitly labeled "Cross-transfer count (baseline)" or handled entirely within the footnotes. The primary table columns should reflect the final state of the primary data product.

*   **P3-M2: Self-Admitted Reproducibility Gaps for Gaia and eROSITA**
    *   **Section/Page:** 3 (§II B), 11 (§III E)
    *   **Problem:** The paper states that the exact data preprocessing script for the Gaia DR3 catalog was not recovered and its specification is "lineage-inferred" from a successor script. Similarly, the primary score axis for the eROSITA catalog was found to be irreproducible from any committed artifact, with the official data product being a fixed membership list. While the authors are commendably transparent about these issues, they represent significant limitations on the utility and robustness of these two catalog components. The "exploratory" flag mentioned in the conclusions is appropriate, but the severity of these findings warrants emphasis.
    *   **Fix:** No change to the analysis is required, as the authors have handled this correctly by flagging the results. However, in the main body text for the Gaia and eROSITA sections (§III G and §III E), please add a sentence at the beginning of each section explicitly stating the reproducibility limitation and directing the reader to the detailed discussion (e.g., "The Gaia component of this catalog is considered exploratory due to an irreproducible preprocessing specification, as detailed in §II B."). This ensures a reader focusing on a specific survey cannot miss this critical caveat.

#### MINOR

*   **P3-m1: Weak Bound on General Relativistic Projection Effects**
    *   **Section/Page:** 18 (§V C, Systematics)
    *   **Problem:** The paper bounds the impact of GR projection corrections on the f_NL forecast as `|Δσ/σ| < 0.02%`. The text notes this is "an internal order-of-magnitude bound from the (H/k)^2 suppression at the Fisher-weighted scales, not an external-literature value". While this effect is expected to be sub-dominant, for a paper in PRD, relying on an internal, un-derived order-of-magnitude estimate is a minor weakness.
    *   **Fix:** Either provide a brief derivation of this bound in an appendix or, preferably, replace the internal estimate with a citation to a standard result in the literature that computes these effects for a similar survey configuration (e.g., [39], [40], [41]).

*   **P3-m2: Inconsistent Use of `N_anom` in Table I Footnotes**
    *   **Section/Page:** 7 (Table I, footnote #)
    *   **Problem:** Footnote # describes the LAMOST native re-score, stating "top-113,342; 21.5x rate reduction". The 21.5x reduction corresponds to the S>5 count changing from 44,075 to 2,054 (as stated in the abstract), not the 113,342 number. The footnote conflates the top-1% continuity slice (113,342) with the S>5 rate-reduction diagnostic (2,054). This could confuse a reader trying to reconcile the numbers.
    *   **Fix:** Clarify the footnote to distinguish between the two different thresholds. For example: "...LAMOST native re-score complete across 11,334,161 spectra... the released anomaly set is a top-1% slice containing 113,342 objects. The native retrain results in a 21.5x rate reduction at a fixed S>5 threshold (from 44,075 to 2,054), confirming the training-bias artifact."

#### NIT

*   **P3-N1: Missing Training Time for Planck Native Model**
    *   **Section/Page:** 24 (Table VI)
    *   **Problem:** In the "Train time (s)" column of Table VI, the entry for the Planck CMB native model is an underscore (`_t`). While the footnote explains the wall-clock time was not preserved, it would be better to state this explicitly in the table.
    *   **Fix:** Replace the underscore with "N/A" or "not recorded" for clarity.

---

## Summary recommendation

**MINOR REVISIONS**

This is an excellent and comprehensive paper that sets a new standard for methodological transparency in large-scale anomaly detection. The scientific results are significant, and the limitations are thoroughly documented and appropriately caveated. The work is well-suited for publication in Physical Review D. The recommended revisions are minor and are intended to improve the clarity of presentation and address small gaps in documentation, primarily in the main summary table. Once these points are addressed, the paper should be accepted.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is a complete referee report for the submitted paper.

---

## Referee Report: P3-R56

**Paper:** Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches

This paper presents a large-scale anomaly detection analysis across seven astronomical surveys, resulting in a catalog of over 378,000 unique anomalous sources. The work is notable for its scale, its multi-survey "native retrain" methodology, and its transparent and rigorous validation framework. The authors apply the resulting catalog to two cosmological problems: constraining primordial non-Gaussianity (f_NL) and testing bouncing cosmology predictions against NANOGrav data.

The paper is exceptionally thorough, well-written, and intellectually honest. The authors take great care to document not only the successes but also the failures of their methodology (e.g., the LAMOST training bias, the ACT cross-transfer failure, the irreproducibility of the eROSITA score axis). The distinction between large "headline" numbers and more carefully defined "like-for-like" comparisons is made explicit and is crucial for a correct interpretation of the results. The cosmological applications are presented with a commendable level of caution, correctly identifying null results and highlighting important caveats. The appendices provide extensive documentation that is essential for reproducibility.

The work represents a significant contribution to the field of astronomical anomaly detection and provides a valuable public data product. The methodological lessons, particularly regarding training bias and cross-survey validation, are of broad importance. While the paper is of very high quality, a few points should be addressed before publication.

---

### Findings

#### ESSENTIAL

*   **P3-E1: Artifact in Date**
    *   **Section/Page:** 1 (Title block)
    *   **Problem:** The paper is dated "(Dated: June 26, 2026)". This is a future date and is clearly a placeholder or artifact.
    *   **Fix:** Replace the date with the correct submission or acceptance date.

#### MAJOR

*   **P3-M1: Ambiguous Presentation in Main Summary Table (Table I)**
    *   **Section/Page:** 7 (Table I)
    *   **Problem:** Table I, the primary summary of the survey results, is confusingly structured. The `N_anom` column presents a mix of final "Path-C" native-retrained counts (for DESI) and initial "cross-transfer" counts (e.g., for LAMOST and SDSS) that are explicitly superseded in the text and footnotes. A reader looking only at the table would get an incorrect impression of the final catalog's composition (e.g., seeing 44,075 LAMOST anomalies instead of the final 113,342). The footnotes are required to understand the canonical results, which is not ideal for a central table.
    *   **Fix:** Revise Table I to exclusively show the final, canonical "Path-C" anomaly counts for all surveys in the main `N_anom` column. The superseded cross-transfer counts, which are valuable for demonstrating the methodological improvement, should be moved to a separate column explicitly labeled "Cross-transfer count (baseline)" or handled entirely within the footnotes. The primary table columns should reflect the final state of the primary data product.

*   **P3-M2: Self-Admitted Reproducibility Gaps for Gaia and eROSITA**
    *   **Section/Page:** 3 (§II B), 11 (§III E)
    *   **Problem:** The paper states that the exact data preprocessing script for the Gaia DR3 catalog was not recovered and its specification is "lineage-inferred" from a successor script. Similarly, the primary score axis for the eROSITA catalog was found to be irreproducible from any committed artifact, with the official data product being a fixed membership list. While the authors are commendably transparent about these issues, they represent significant limitations on the utility and robustness of these two catalog components. The "exploratory" flag mentioned in the conclusions is appropriate, but the severity of these findings warrants emphasis.
    *   **Fix:** No change to the analysis is required, as the authors have handled this correctly by flagging the results. However, in the main body text for the Gaia and eROSITA sections (§III G and §III E), please add a sentence at the beginning of each section explicitly stating the reproducibility limitation and directing the reader to the detailed discussion (e.g., "The Gaia component of this catalog is considered exploratory due to an irreproducible preprocessing specification, as detailed in §II B."). This ensures a reader focusing on a specific survey cannot miss this critical caveat.

#### MINOR

*   **P3-m1: Weak Bound on General Relativistic Projection Effects**
    *   **Section/Page:** 18 (§V C, Systematics)
    *   **Problem:** The paper bounds the impact of GR projection corrections on the f_NL forecast as `|Δσ/σ| < 0.02%`. The text notes this is "an internal order-of-magnitude bound from the (H/k)^2 suppression at the Fisher-weighted scales, not an external-literature value". While this effect is expected to be sub-dominant, for a paper in PRD, relying on an internal, un-derived order-of-magnitude estimate is a minor weakness.
    *   **Fix:** Either provide a brief derivation of this bound in an appendix or, preferably, replace the internal estimate with a citation to a standard result in the literature that computes these effects for a similar survey configuration (e.g., [39], [40], [41]).

*   **P3-m2: Inconsistent Use of `N_anom` in Table I Footnotes**
    *   **Section/Page:** 7 (Table I, footnote #)
    *   **Problem:** Footnote # describes the LAMOST native re-score, stating "top-113,342; 21.5x rate reduction". The 21.5x reduction corresponds to the S>5 count changing from 44,075 to 2,054 (as stated in the abstract), not the 113,342 number. The footnote conflates the top-1% continuity slice (113,342) with the S>5 rate-reduction diagnostic (2,054). This could confuse a reader trying to reconcile the numbers.
    *   **Fix:** Clarify the footnote to distinguish between the two different thresholds. For example: "...LAMOST native re-score complete across 11,334,161 spectra... the released anomaly set is a top-1% slice containing 113,342 objects. The native retrain results in a 21.5x rate reduction at a fixed S>5 threshold (from 44,075 to 2,054), confirming the training-bias artifact."

*   **P3-m3: Incorrect Section Reference in Abstract**
    *   **Section/Page:** 1 (Abstract)
    *   **Problem:** The abstract cites `§VIE` when discussing the size benchmark comparison to prior work. There is no section VIE. The correct section is `§VI E`, "Comparison with Prior Work".
    *   **Fix:** Correct the reference from `§VIE` to `§VI E`.

*   **P3-m4: Incorrect Reference Format in Fisher Forecast Section**
    *   **Section/Page:** 17 (§V B)
    *   **Problem:** The text states, "...from the 5-α refit of §VID caveat (i), inserting...". The reference `§VID` is to a section that contains a list of caveats. However, the caveats themselves are enumerated in Table V, not in the text of §VID. The reference should be to the table.
    *   **Fix:** Change the reference from `§VID caveat (i)` to `Table V, caveat (i)`.

#### NIT

*   **P3-N1: Missing Training Time for Planck Native Model**
    *   **Section/Page:** 24 (Table VI)
    *   **Problem:** In the "Train time (s)" column of Table VI, the entry for the Planck CMB native model is an underscore (`_t`). While the footnote explains the wall-clock time was not preserved, it would be better to state this explicitly in the table.
    *   **Fix:** Replace the underscore with "N/A" or "not recorded" for clarity.

---

## Summary recommendation

**MINOR REVISIONS**

This is an excellent and comprehensive paper that sets a new standard for methodological transparency in large-scale anomaly detection. The scientific results are significant, and the limitations are thoroughly documented and appropriately caveated. The work is well-suited for publication in Physical Review D. The recommended revisions are minor and are intended to improve the clarity of presentation and address small gaps in documentation, primarily in the main summary table. Once these points are addressed, the paper should be accepted.