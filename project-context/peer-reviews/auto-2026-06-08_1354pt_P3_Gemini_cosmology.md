# P3 auto-2026-06-08_1354pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (2674 chars)
**Wall time**: 134.6s

---

## Referee Report: "Spectrally Unusual Sources at Scale..."

This paper presents a large-scale anomaly detection analysis across seven astronomical surveys, resulting in a catalog of 378,280 unique anomalies. The authors apply an autoencoder framework, develop a "Path-C" protocol involving native retraining to mitigate cross-survey artifacts, and perform extensive validation. The work culminates in two cosmological applications: a multi-tracer Fisher forecast for primordial non-Gaussianity (fNL) and a consistency check of the matter-bounce scenario using NANOGrav data.

The scale of the analysis is impressive, and the methodological rigor is commendable. The authors' transparent handling of failure modes—specifically the LAMOST training-bias and the cross-transfer issues with SDSS and CMB data—is a major strength of the work. The resulting catalog is a significant contribution to the field. The cosmological applications, while not yielding new detections, are well-motivated and appropriately analyzed as forecasts and consistency checks.

The paper is generally well-written and suitable for publication in Physical Review D, pending revisions to address the following points.

---
### ESSENTIAL Revisions

**P3-E1**
*   **Section/Page:** IV B, page 9
*   **Problem:** The text reports the result of a spatial uniformity test as "χ² = 3.76". The preceding numbers are "χ² = 143,936, dof = 38,329". The value 3.76 is the reduced chi-squared, χ²/dof.
*   **Fix:** Change the text to explicitly state this, for example: "...significantly non-uniform (χ² = 143,936 for dof = 38,329, giving a reduced χ² of χ²/dof ≈ 3.76)...".

**P3-E2**
*   **Section/Page:** V b, page 11
*   **Problem:** The paper claims a "central 7.9% improvement" in the fNL constraint, from a baseline of σ(fNL)std = 8.98 to a forecast of σ(fNL) = 8.14. The calculation of this percentage is unclear and appears inconsistent with standard definitions. A standard relative improvement calculation, 1 - (σ_new / σ_old), yields 1 - (8.14 / 8.98) ≈ 9.4%. An improvement in constraining power (proportional to 1/σ²) would be (σ_old² / σ_new²) - 1 ≈ 21.8%. The source of the 7.9% figure is not obvious and must be clarified. While the main physical conclusion—that the improvement is not statistically significant (<1σ)—is correct and well-stated, the headline percentage must be reproducible.
*   **Fix:** Provide the explicit formula used to calculate the 7.9% improvement, or correct the value to match a standard definition (e.g., 9.4%) and adjust the text accordingly.

---
### MAJOR Revisions

None.

---
### MINOR Revisions

**P3-m1**
*   **Section/Page:** Abstract, page 1
*   **Problem:** The abstract reports the Savage-Dickey factor as `BMB/SMBHB = 7.1×10³`. The body of the paper (Section VI A, page 12) reports the more precise value `7.14×10³`.
*   **Fix:** Ensure consistency between the abstract and the main text. Using the more precise value `7.14×10³` in the abstract is recommended.

**P3-m2**
*   **Section/Page:** II B b, page 2 and Table IV, page 13
*   **Problem:** The text states that of 546 unique objects in the 5-fold validation union, "399 (73%) appear in all five folds". The precise percentage is 399/546 ≈ 73.1%. While minor, precision is important in a methodological paper. This is repeated in Table IV, item (g).
*   **Fix:** Report the value as 73.1% or use a tilde (e.g., ~73%) to indicate rounding.

**P3-m3**
*   **Section/Page:** Table I, page 7, footnote ||
*   **Problem:** The footnote states "The Path-C per-survey native counts... sum to 388,493". The sum of the native counts listed in the text and table is: DESI 195,829 + SDSS 77,905 (native slice) + LAMOST 113,342 (native slice) + eROSITA 298 + Planck 200 + Gaia 500 + NEOWISE 419 = 388,493. This is correct. However, the SDSS and LAMOST counts used here are the *top-percentile slices* of the native re-scores, not the full anomaly catalogs from the native re-scores. The text in §III C and §III D clarifies this, but the footnote could be slightly more precise to avoid ambiguity.
*   **Fix:** Consider a minor rephrasing in the footnote, such as "The Path-C per-survey native anomaly *counts used for deduplication* (DESI S>5, top-percentile slices for SDSS/LAMOST, etc.) sum to 388,493...". This is a minor point of clarity.

---
### NIT (Cosmetic)

**P3-N1**
*   **Section/Page:** Title block, page 1
*   **Problem:** The date of the paper is listed as "(Dated: June 2026)".
*   **Fix:** Replace this placeholder with the actual submission date.

**P3-N2**
*   **Section/Page:** Abstract, page 1
*   **Problem:** The phrase "3 FAIL-with-diagnostic at 5σ" is slightly ambiguous. It means the injection-recovery test was performed with a 5σ amplitude signal and the result was FAIL, but it could be misread as the test failing at a 5σ significance level.
*   **Fix:** Suggest rephrasing for clarity, e.g., "...and 3 FAIL (at 5σ injection amplitude) with informative diagnostics...".

**P3-N3**
*   **Section/Page:** V b, page 11
*   **Problem:** The text states "the central 7.9% improvement is consistent with no improvement at <10;". The symbol should be a sigma (σ).
*   **Fix:** Correct the typo from "10" to "1σ".

---
## Summary recommendation

**MAJOR REVISIONS**

The paper represents a substantial and high-quality contribution. The scale of the catalog is unprecedented, and the methodological care taken to validate the results and transparently report failures sets a high standard. The cosmological applications are relevant and handled with appropriate caution. The required revisions are essential for ensuring the clarity, accuracy, and reproducibility of key quantitative claims but do not undermine the paper's core findings. Once the essential points regarding the χ² statistic and the fNL forecast improvement are addressed, the paper will be a strong candidate for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from a more rigorous re-examination of the paper.

---
### ADDITIONAL FINDINGS

**P3-M4**
*   **Section/Page:** IV A, page 9
*   **Problem:** The text makes a quantitative claim about the reduction of the novelty fraction: "Extended archival cross-matching reduces the headline novelty pool by a factor of ~5.6× relative to the SIMBAD-unmatched aggregate...". The numbers provided are a SIMBAD-unmatched aggregate of 58.8% and a genuine novelty fraction of 17.8%. A reduction "by a factor of X" implies the new value is the old value divided by X. However, 58.8% / 17.8% ≈ 3.3, not 5.6. The calculation 1 / 0.178 ≈ 5.6 suggests a possible but non-standard interpretation. As written, this key sentence summarizing the paper's novelty discovery rate is arithmetically inconsistent with the data presented.
*   **Fix:** Correct the factor to ~3.3×, or rewrite the sentence to clarify the intended calculation. For example: "The genuine novelty fraction (17.8%) is smaller by a factor of ~3.3 compared to the SIMBAD-unmatched fraction (58.8%)."

**P3-m4**
*   **Section/Page:** VI C, page 12
*   **Problem:** The text contains a broken cross-reference: "...(Gaia 41% stability, eROSITA 81.5%; §VID (v));...". There is no subsection `(v)` in Section VI D or a corresponding item in Table IV. The reference likely points to a subsection that was renumbered or removed during editing.
*   **Fix:** Locate the correct reference for the Isolation Forest cross-validation details (likely in a footnote to Table I or another part of Section VI D) and update the citation.

**P3-m5**
*   **Section/Page:** Appendix C 1, page 15
*   **Problem:** The text describes the effect of a shot-noise penalty on the `σ(fNL)` forecast with confusing signs. It states: "With a 15% Fisher-info penalty, σ(fNL) = 12.56 (+1.27% over the baseline-multi 12.72); with a 30% penalty, σ(fNL) = 13.35 (-4.97% vs. baseline-multi)." A penalty should increase `σ` (worsen the constraint).
    1.  For the 15% penalty, `σ` decreases from 12.72 to 12.56, which is an *improvement*, not the result of a penalty. The percentage change is `(12.56/12.72 - 1) * 100 ≈ -1.26%`. The text has the wrong sign.
    2.  For the 30% penalty, `σ` increases from 12.72 to 13.35, which is a worsening, as expected. The percentage change is `(13.35/12.72 - 1) * 100 ≈ +4.95%`. The text reports this as `-4.97%`, which has the wrong sign.
*   **Fix:** Review the calculations and clarify the text. Ensure that penalties correctly correspond to an increase in `σ` and that the signs of the percentage changes reflect this (e.g., a "+4.95% change in σ" or a "-4.95% change in constraining power").