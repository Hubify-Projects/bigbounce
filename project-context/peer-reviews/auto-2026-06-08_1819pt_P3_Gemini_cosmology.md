# P3 auto-2026-06-08_1819pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (11401 chars)
**Wall time**: 168.4s

---

## Referee Report on "Spectrally Unusual Sources at Scale..."

This paper presents a large-scale anomaly detection survey across seven astronomical archives, resulting in a catalog of over 378,000 unique anomalies. The authors apply the BigAE autoencoder framework, develop a "Path-C" native retraining protocol to handle cross-survey artifacts, and perform extensive internal validation. The work's primary contributions are the catalog itself, the methodological lessons learned from the multi-survey application (particularly the LAMOST training-bias artifact), and a set of secondary cosmological applications, including a forecast for primordial non-Gaussianity (fNL) constraints and a consistency check with NANOGrav data.

The scale of the catalog and the rigor of the cross-survey validation are commendable. The distinction between "SIMBAD-unmatched" and "genuinely novel" is particularly important and well-articulated. The methodological lessons provide valuable guidance for future large-scale machine learning applications in astronomy.

However, the paper suffers from several significant errors and presentational issues, particularly in the cosmological application section, that must be addressed before it can be considered for publication in Physical Review D. The calculations for the fNL Fisher forecast are incorrect, and the primary results table is exceptionally confusing.

### ESSENTIAL Revisions

**P3-E1: Incorrect Fisher Forecast Calculation and Error Propagation (Abstract p.1, Sec. V B p.11, Table IV p.14, Conclusion p.14)**

The paper's central cosmological forecast for σ(fNL) contains significant errors in its calculation and the reporting of its uncertainty.

*   **Problem 1 (Incorrect 1σ envelope):** In Section V B (p. 11), the paper computes a central forecast of σ(fNL) = 8.14 based on the empirical bias `ajk = 0.19 ± 0.65`. It then claims a "1σ envelope" of `[3.92, 8.98]`. This is incorrect. Propagating the 1σ uncertainty on `a` (i.e., evaluating at `a = 0.19 ± 0.65`) using the paper's own formula `1/σ(fNL)² = Fo + ca²` (with `Fo = 1/8.98²` and `c = 0.0747`) yields:
    *   At `a_upper = 0.19 + 0.65 = 0.84`, σ(fNL) = 3.92.
    *   At `a_lower = 0.19 - 0.65 = -0.46`, σ(fNL) = 5.95.
    The correct 1σ envelope derived from propagating the uncertainty on `a` is therefore approximately `[3.92, 5.95]`. The quoted upper bound of 8.98 is the no-improvement baseline (i.e., `a=0`), which is not the correct upper bound of the 1σ error bar. This error is repeated in the abstract, Table IV, and the conclusions.
*   **Problem 2 (Incorrect Percentage Improvement):** The abstract, Section V B, and conclusions all claim a "7.9% improvement" for the central forecast. The correct calculation is `(σ_baseline - σ_forecast) / σ_baseline = (8.98 - 8.14) / 8.98 = 9.35%`. The quoted 7.9% is incorrect.

*   **Required Fix:** The authors must re-calculate the 1σ envelope for σ(fNL) by correctly propagating the uncertainty on the measured bias parameter `a`. They must also correct the percentage improvement calculation. These corrected numbers must be updated in the abstract, Section V B, Table IV, and the conclusions. The text must clearly state how the envelope was calculated.

**P3-E2: Confusing and Misleading Presentation in Table I (p.6)**

Table I is the central summary of the paper's results, but its structure is deeply confusing and actively hinders understanding. The main body of the table presents numbers from the initial "cross-transfer" scan, which the paper itself identifies as flawed and superseded. The final, primary results (the "Path-C" native-retrained counts) are relegated to a single summary row at the bottom and a series of dense, cross-referencing footnotes.

*   **Problem:** A reader looking at the table will see, for example, that the SDSS and LAMOST anomaly counts are 77,905 and 44,075, respectively. The text and footnotes explain that these are not the final science-grade results and that the native retraining led to massive "rate compression" (a factor of ~6500 for SDSS). Yet, other footnotes state that the *number* of anomalies for the final catalog was kept the same (as a top-percentile slice). This is a critical methodological detail that is completely obscured by the table's layout. The primary results of the paper should not be buried in footnotes while superseded diagnostic numbers occupy the main table.

*   **Required Fix:** Restructure Table I completely. The main table body must present the final, canonical "Path-C" native-retrained results for each survey. This should include the number of sources, the final anomaly count, the final rate, and the threshold used. The initial "cross-transfer" numbers should be moved to a separate diagnostic table in an appendix or, if they must be included, presented in a clearly subordinate way (e.g., in parentheses or a separate column explicitly labeled "Initial Cross-Transfer Diagnostic"). The footnotes must be simplified and integrated into the main caption where possible.

### MAJOR Revisions

**P3-M1: Inconsistent Reporting of DESI Anomaly Rate (Sec. III A, p.4)**

There is a contradiction in the description of the DESI anomaly selection.

*   **Problem:** The text in Section III A states: "The headline 195,829 DESI anomaly count is the top-1% score-cut of the full 22.5-M-spectrum scan...". A few lines later, it states the model "identifies 195,829 anomalies above the S > 5.0 threshold, an anomaly rate of 0.87%." A top-1% cut is not the same as a 0.87% rate from an absolute threshold cut. The number `195,829 / 22,504,897` is indeed 0.87%.

*   **Required Fix:** The authors must clarify the exact selection criteria for the 195,829 DESI anomalies. The phrase "top-1% score-cut" should be removed if the selection was based on the `S > 5.0` threshold, as the numbers suggest. This should be made consistent throughout the text.

### MINOR Revisions

**P3-m1: Ambiguous Caption for Fisher Forecast Sensitivity Table (Table VII, p.16)**

The caption for Table VII is not sufficiently clear about the calculation method.

*   **Problem:** The caption states that the values are "derived by linear scaling from the fiducial full 7-bin Fisher result at a = 0.15". While the resulting percentage improvement is indeed linear in `a`, the value of σ(fNL) itself is not. The calculation relies on a linear approximation of the *improvement*, which is then applied to the baseline σ.

*   **Required Fix:** The caption should be clarified to state that the table is based on a linear approximation of the fractional improvement in σ(fNL), i.e., `σ(a) ≈ σ(0) * (1 - k*a)`.

**P3-m2: Duplicate Table Content (p.4 and p.16)**

Table VI, "DESI DR1 anomaly classification by spectral-arm dominance," appears on page 16 in the appendix section, but the exact same information (all numbers and categories) is already presented in the main body text of Section III A on page 4.

*   **Problem:** This is redundant.

*   **Required Fix:** Remove Table VI from the appendix. The presentation in the main text is sufficient.

### NITs

**P3-N1: Date of Publication (Abstract, p.1)**

*   **Problem:** The paper is dated "(Dated: June 2026)". This is presumably a placeholder but should be corrected.
*   **Required Fix:** Update the date to the current submission date.

## Summary recommendation

**MAJOR REVISIONS**

This paper presents a valuable and substantial contribution in the form of a very large, multi-survey anomaly catalog. The methodological work, particularly the handling of cross-survey domain shift and the extensive validation, is a key strength. However, the paper is marred by serious and fundamental errors in the cosmological Fisher forecast, a primary application highlighted in the abstract and conclusions. For a journal with the standards of Physical Review D, such numerical errors in a key physics analysis are not acceptable. Furthermore, the main results table is structured in a way that is confusing to the point of being misleading. While the core cataloging effort appears sound, the paper requires a major overhaul of its cosmological calculations and data presentation before it can be accepted for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated referee report, incorporating the new findings from the second, more rigorous review.

================================================================
## Referee Report on "Spectrally Unusual Sources at Scale..."

This paper presents a large-scale anomaly detection survey across seven astronomical archives, resulting in a catalog of over 378,000 unique anomalies. The authors apply the BigAE autoencoder framework, develop a "Path-C" native retraining protocol to handle cross-survey artifacts, and perform extensive internal validation. The work's primary contributions are the catalog itself, the methodological lessons learned from the multi-survey application (particularly the LAMOST training-bias artifact), and a set of secondary cosmological applications, including a forecast for primordial non-Gaussianity (fNL) constraints and a consistency check with NANOGrav data.

The scale of the catalog and the rigor of the cross-survey validation are commendable. The distinction between "SIMBAD-unmatched" and "genuinely novel" is particularly important and well-articulated. The methodological lessons provide valuable guidance for future large-scale machine learning applications in astronomy.

However, the paper suffers from several significant errors and presentational issues, particularly in the cosmological application section, that must be addressed before it can be considered for publication in Physical Review D. The calculations for the fNL Fisher forecast are incorrect, the primary results table is exceptionally confusing, and the manuscript contains numerous broken cross-references and internal inconsistencies.

### ESSENTIAL Revisions

**P3-E1: Incorrect Fisher Forecast Calculation and Error Propagation (Abstract p.1, Sec. V B p.11, Table IV p.14, Conclusion p.14)**

The paper's central cosmological forecast for σ(fNL) contains significant errors in its calculation and the reporting of its uncertainty.

*   **Problem 1 (Incorrect 1σ envelope):** In Section V B (p. 11), the paper computes a central forecast of σ(fNL) = 8.14 based on the empirical bias `ajk = 0.19 ± 0.65`. It then claims a "1σ envelope" of `[3.92, 8.98]`. This is incorrect. Propagating the 1σ uncertainty on `a` (i.e., evaluating at `a = 0.19 ± 0.65`) using the paper's own formula `1/σ(fNL)² = Fo + ca²` (with `Fo = 1/8.98²` and `c = 0.0747`) yields:
    *   At `a_upper = 0.19 + 0.65 = 0.84`, σ(fNL) = 3.92.
    *   At `a_lower = 0.19 - 0.65 = -0.46`, σ(fNL) = 5.95.
    The correct 1σ envelope derived from propagating the uncertainty on `a` is therefore approximately `[3.92, 5.95]`. The quoted upper bound of 8.98 is the no-improvement baseline (i.e., `a=0`), which is not the correct upper bound of the 1σ error bar. This error is repeated in the abstract, Table IV, and the conclusions.
*   **Problem 2 (Incorrect Percentage Improvement):** The abstract, Section V B, and conclusions all claim a "7.9% improvement" for the central forecast. The correct calculation is `(σ_baseline - σ_forecast) / σ_baseline = (8.98 - 8.14) / 8.98 = 9.35%`. The quoted 7.9% is incorrect.

*   **Required Fix:** The authors must re-calculate the 1σ envelope for σ(fNL) by correctly propagating the uncertainty on the measured bias parameter `a`. They must also correct the percentage improvement calculation. These corrected numbers must be updated in the abstract, Section V B, Table IV, and the conclusions. The text must clearly state how the envelope was calculated.

**P3-E2: Confusing and Misleading Presentation in Table I (p.6)**

Table I is the central summary of the paper's results, but its structure is deeply confusing and actively hinders understanding. The main body of the table presents numbers from the initial "cross-transfer" scan, which the paper itself identifies as flawed and superseded. The final, primary results (the "Path-C" native-retrained counts) are relegated to a single summary row at the bottom and a series of dense, cross-referencing footnotes.

*   **Problem:** A reader looking at the table will see, for example, that the SDSS and LAMOST anomaly counts are 77,905 and 44,075, respectively. The text and footnotes explain that these are not the final science-grade results and that the native retraining led to massive "rate compression" (a factor of ~6500 for SDSS). Yet, other footnotes state that the *number* of anomalies for the final catalog was kept the same (as a top-percentile slice). This is a critical methodological detail that is completely obscured by the table's layout. The primary results of the paper should not be buried in footnotes while superseded diagnostic numbers occupy the main table.

*   **Required Fix:** Restructure Table I completely. The main table body must present the final, canonical "Path-C" native-retrained results for each survey. This should include the number of sources, the final anomaly count, the final rate, and the threshold used. The initial "cross-transfer" numbers should be moved to a separate diagnostic table in an appendix or, if they must be included, presented in a clearly subordinate way (e.g., in parentheses or a separate column explicitly labeled "Initial Cross-Transfer Diagnostic"). The footnotes must be simplified and integrated into the main caption where possible.

**P3-E3: Incorrect Fisher Forecast Envelope for Gold+Silver Sample (Sec V B p.11, Table IV p.14)**

The error in calculating the 1σ envelope is repeated for the high-confidence Gold+Silver QSO subset.

*   **Problem:** The paper reports a central forecast of `σ(fNL)GS = 1.95` with a 1σ envelope of `[0.94, 8.98]`. While the lower bound is calculated correctly from `a_upper = 1.83 + 2.03 = 3.86`, the upper bound is not. The value at `a_lower = 1.83 - 2.03 = -0.2` is `σ(fNL) ≈ 8.06`. The paper again incorrectly uses the no-improvement baseline (8.98) as the upper bound of the error bar.

*   **Required Fix:** Correct the 1σ envelope for the Gold+Silver sample forecast in Section V B and Table IV by properly propagating the lower-bound uncertainty on `a`.

### MAJOR Revisions

**P3-M1: Inconsistent Reporting of DESI Anomaly Rate (Sec. III A, p.4)**

There is a contradiction in the description of the DESI anomaly selection.

*   **Problem:** The text in Section III A states: "The headline 195,829 DESI anomaly count is the top-1% score-cut of the full 22.5-M-spectrum scan...". A few lines later, it states the model "identifies 195,829 anomalies above the S > 5.0 threshold, an anomaly rate of 0.87%." A top-1% cut is not the same as a 0.87% rate from an absolute threshold cut. The number `195,829 / 22,504,897` is indeed 0.87%.

*   **Required Fix:** The authors must clarify the exact selection criteria for the 195,829 DESI anomalies. The phrase "top-1% score-cut" should be removed if the selection was based on the `S > 5.0` threshold, as the numbers suggest. This should be made consistent throughout the text.

**P3-M2: Inconsistent Methodology for Fisher Sensitivity (Sec V B p.11 vs. App C/Table VII p.16)**

The paper uses two different and inconsistent methods to calculate the relationship between the tracer bias `a` and the forecast `σ(fNL)`.

*   **Problem:** The main text (Sec V B) uses the correct quadratic formula `1/σ² = Fo + ca²`. However, Table VII in Appendix C, which is meant to show the sensitivity of the forecast to `a`, is generated using a "linear scaling" of the percentage improvement from the fiducial `a=0.15` case. This linear approximation is inaccurate and deviates significantly from the quadratic formula, especially for larger values of `a`. For example, at `a=0.5`, the table gives `σ=7.15` while the correct formula gives `σ=5.67`.

*   **Required Fix:** The authors must use a single, consistent methodology. Table VII should be re-calculated using the same quadratic formula presented in the main text. The caption and any related text must be updated to reflect this.

### MINOR Revisions

**P3-m1: Ambiguous Caption for Fisher Forecast Sensitivity Table (Table VII, p.16)**

The caption for Table VII is not sufficiently clear about the calculation method.

*   **Problem:** The caption states that the values are "derived by linear scaling from the fiducial full 7-bin Fisher result at a = 0.15". This phrasing is ambiguous and hides the fact that it is a linear approximation of the *improvement*, not of `σ(fNL)` itself.

*   **Required Fix:** This issue will be resolved by implementing the fix for P3-M2. The new caption for the re-calculated Table VII should simply state that the values are computed using the formula from Section V B.

**P3-m2: Duplicate Table Content (p.4 and p.16)**

Table VI, "DESI DR1 anomaly classification by spectral-arm dominance," appears on page 16 in the appendix section, but the exact same information (all numbers and categories) is already presented in the main body text of Section III A on page 4.

*   **Problem:** This is redundant.

*   **Required Fix:** Remove Table VI from the appendix. The presentation in the main text is sufficient.

**P3-m3: Broken Internal Cross-References (Table I p.6, Sec VI C p.12, Fig 7 p.13)**

The manuscript contains multiple broken or incorrect cross-references, indicating a lack of careful proofreading.

*   **Problem:** The Table I caption refers to footnote `‡`, which does not exist (it is likely a typo for `#`). More significantly, Section VI C and the Figure 7 caption both refer to a non-existent "§VID caveat (v)". The information these references point to appears to be in a footnote in Table I, but the pointer itself is broken.

*   **Required Fix:** The authors must perform a thorough check of all internal cross-references (`\ref`, `\cite`, etc.) and fix all broken or incorrect pointers.

### NITs

**P3-N1: Date of Publication (Abstract, p.1)**

*   **Problem:** The paper is dated "(Dated: June 2026)". This is presumably a placeholder but should be corrected.
*   **Required Fix:** Update the date to the current submission date.

**P3-N2: Ambiguous Terminology (Reduced Chi-squared) (Sec IV B p.9)**

*   **Problem:** The text reports a value for "χ²" (chi-squared) which is actually the reduced chi-squared (χ²/dof). The value is given as `x² = 3.76`, which is clearly not the total chi-squared of `143,936`.
*   **Required Fix:** Clarify the notation to be unambiguous, e.g., by using χ²_red, χ²/dof, or explicitly stating "reduced chi-squared".

## Summary recommendation

**MAJOR REVISIONS**

This paper presents a valuable and substantial contribution in the form of a very large, multi-survey anomaly catalog. The methodological work, particularly the handling of cross-survey domain shift and the extensive validation, is a key strength. However, the paper is marred by serious and fundamental errors in the cosmological Fisher forecast, a primary application highlighted in the abstract and conclusions. For a journal with the standards of Physical Review D, such numerical errors in a key physics analysis are not acceptable. Furthermore, the main results table is structured in a way that is confusing to the point of being misleading, and the manuscript suffers from a general lack of polish evidenced by numerous internal inconsistencies and broken references. While the core cataloging effort appears sound, the paper requires a major overhaul of its cosmological calculations and data presentation before it can be accepted for publication.