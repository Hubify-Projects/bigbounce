# P3 R10v3p1 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 134.6s

---

Referee Report for PRD Submission [P3]

**Title:** Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and Native-Trained Novelty Fractions from 37.3 Million Sources and Map Patches

The authors present a large-scale anomaly detection analysis across seven astronomical surveys, resulting in a catalog of over 378,000 unique anomalous sources. The work is methodologically detailed, transparently documenting the evolution from a flawed cross-transfer approach to a more robust native-retraining protocol ("Path-C"). The paper presents the resulting catalog, discusses methodological lessons, and explores applications including a search for high-redshift quasars and forecasts for cosmological parameter constraints.

The scale of the analysis is impressive, and the methodological rigor, particularly the documentation of failures (e.g., LAMOST training bias, ACT cross-transfer) and residual caveats, is commendable. The resulting data product is a significant contribution. However, the manuscript requires major revisions to address a persistent numerical error in a key cosmological forecast, remove several instances of internal-review language and placeholders, and improve its readiness for publication in a professional journal.

---
### Detailed Findings

#### ESSENTIAL

**P3-E1: Incorrect Cosmological Forecast Improvement**
*   **Location:** Abstract (p. 1), Section V.b (p. 10), Conclusion 5 (p. 14)
*   **Problem:** The paper repeatedly claims a "7.9% improvement" in the constraint on `f_NL` from the empirical bias measurement. The stated baseline is `σ(f_NL)_std = 8.98` and the new forecast is `σ(f_NL) = 8.14`. The fractional improvement in the standard deviation `σ` is calculated as `(σ_std - σ_new) / σ_std`. The correct calculation is `(8.98 - 8.14) / 8.98 = 0.84 / 8.98 ≈ 0.0935`, which is a **9.4% improvement**. The 7.9% figure is incorrect and appears in the abstract, the main body, and the conclusions, misrepresenting a key result.
*   **Required Fix:** Recompute this value and correct it in all three locations (Abstract, Section V.b, and Conclusion 5). If the 7.9% figure is derived via a different metric (e.g., related to Fisher information, `1/σ^2`), this metric must be explicitly defined and justified. Based on the context and the 6.1% improvement calculated for the fixed-`a` case, the metric appears to be fractional improvement in `σ`.

**P3-E2: Placeholder References in Text**
*   **Location:** Section II.A (p. 2)
*   **Problem:** The text contains unresolved placeholder references.
    *   "...architecture shown schematically in Fig. ??."
    *   "...computed over the blue... subsets (Fig. ??)."
*   **Required Fix:** Replace all instances of `??` with the correct figure numbers.

#### MAJOR

**P3-M1: Internal Review Artifact in Table I Footnote**
*   **Location:** Table I, footnote § (p. 7)
*   **Problem:** The footnote contains language that appears to be a remnant of an internal review process or a response to a previous referee. The phrase "...the earlier 'strict subset' framing is replaced with this exact 284/298 = 95.3% overlap" is not appropriate for a final publication. It breaks the formal tone and refers to a previous state of the manuscript that the reader has no context for.
*   **Required Fix:** Rewrite the footnote to present the final methodology and results directly, without referring to how it has changed from previous versions. For example: "The two anomaly detectors show strong agreement: 284 of the 298 canonical-S sources (95.3%) are also present in the top-9,303 sources identified by IsolationForest..."

**P3-M2: Inappropriate Data Availability Statement**
*   **Location:** Acknowledgments, "Data availability" paragraph (p. 14)
*   **Problem:** The data availability statement includes the phrase "(private pending arXiv acceptance; public upon acceptance)". This is logistical information for the editors and authors, not permanent text for the published article.
*   **Required Fix:** Remove this parenthetical phrase. The final version should simply state the location of the data.

**P3-M3: Internal Note in Bibliography**
*   **Location:** References, [33] (p. 19)
*   **Problem:** The bibliographic entry for Heinrich et al. contains an internal author note: "[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]". This is metadata related to the manuscript's preparation and is not part of a formal citation.
*   **Required Fix:** Remove the bracketed note and format the reference according to journal standards.

#### MINOR

**P3-m1: Paper Length and Structure**
*   **Location:** Entire manuscript
*   **Problem:** At 20 pages, the paper is long. While the detail is appreciated, the main contribution is the catalog and the methodology. The cosmological applications, while interesting, are secondary forecasts and analyses that add significant length. The extensive appendices, particularly the detailed MCMC documentation and the quarantined ACT scan, could potentially be streamlined.
*   **Required Fix:** The authors should consider whether the paper could be made more concise. One option is to move some of the more detailed derivations (e.g., Appendix E, F) to a public repository linked from the data release, summarizing the key results in the main text. This is a recommendation for improved impact and readability, not a requirement for acceptance.

#### NIT

**P3-N1: Future Dating**
*   **Location:** Abstract (p. 1) and References (p. 19)
*   **Problem:** The paper is dated "June 2026" and several references are to works from 2025 and 2026. While this is understood to be part of the fictional context of the submission, it is worth noting.
*   **Required Fix:** No fix required, assuming this is intentional for the exercise.

---
### Summary recommendation

**MAJOR REVISIONS**

This is a strong, methodologically sound paper presenting a valuable data product for the community. The authors' transparency regarding the process, including the documentation of failed approaches, is a model of good scientific practice. The paper is well-suited for publication in Physical Review D, given its connection to cosmological tracer populations. However, it cannot be accepted in its current form. The Essential and Major revisions listed above, particularly the correction of the `f_NL` forecast and the removal of all internal-review artifacts and placeholders, must be addressed before the manuscript can be reconsidered for publication. Once these issues are resolved, the paper will represent a significant and robust contribution.