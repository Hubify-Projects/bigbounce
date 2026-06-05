# P3 auto-2026-06-05_1617pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 159.6s

---

## Referee Report: "Spectrally Unusual Sources at Scale..." by Houston Golden

This paper presents a large-scale anomaly detection campaign across seven astronomical surveys, resulting in a catalog of over 378,000 unique anomalous sources. The authors apply a consistent autoencoder framework (BIGAE), develop a "Path-C" native retraining protocol to mitigate cross-survey artifacts, and perform extensive internal and external validation. The work culminates in two cosmological applications: a forecast for primordial non-Gaussianity (f_NL) constraints using the anomaly catalog as a new tracer population, and a consistency check of the matter-bounce scenario against NANOGrav data.

The scale of the catalog and the methodological rigor of the "Path-C" rebuild are commendable. The clear documentation of failure modes (e.g., LAMOST training bias, ACT cross-transfer) is a strength and provides valuable lessons for the community. The cosmological applications, while preliminary, demonstrate the potential scientific utility of the catalog beyond source discovery.

However, the paper contains several numerical inconsistencies, unclear derivations, and methodological discrepancies that must be resolved before it can be considered for publication in Physical Review D. The most significant issues relate to the derivation of key summary statistics in the abstract and the internal consistency of the f_NL forecast calculation.

---

### Detailed Findings

#### ESSENTIAL

**P3-E1 | Abstract, Page 1**
*   **Problem:** The abstract states, "the recommended catalog-grade subset is ~265,000 unique objects (DESI + SDSS + EROSITA + Gaia + NEOWISE), which excludes the LAMOST exploratory tier (~113,000 objects retained...)." This number is not clearly derived or verifiable from the information presented in the paper.
    *   The sum of native, pre-deduplication counts for these five surveys from Table I, footnote `||` is: 195,829 (DESI) + 77,905 (SDSS) + 298 (eROSITA) + 500 (Gaia) + 419 (NEOWISE) = 274,951.
    *   Subtracting the full LAMOST native count (113,342) from the total native sum (388,493) gives 275,151.
    *   It is unclear how deduplication among these specific five surveys would reduce the count from ~275,000 to ~265,000. The total deduplication across all seven surveys is only 10,213 objects.
*   **Required Fix:** The authors must provide a precise derivation for the ~265,000 figure, showing the starting numbers and the effect of deduplication for this specific subset. If this cannot be done robustly, the number should be removed from the abstract or replaced with a more transparently derived value (e.g., the sum of native counts, ~275,000).

#### MAJOR

**P3-M1 | Abstract (p. 1), Section V (p. 10), Conclusions (p. 14)**
*   **Problem:** The paper repeatedly claims a "7.9% improvement" in the `σ(f_NL)` constraint from the multi-tracer analysis. My calculation based on the provided numbers yields a different result.
    *   The baseline is the single-tracer `σ(f_NL)std = 8.98`.
    *   The new central forecast is `σ(f_NL) = 8.14`.
    *   The fractional improvement is `(8.98 - 8.14) / 8.98 = 0.84 / 8.98 = 0.0935`, which is a **9.4%** improvement, not 7.9%.
*   **Required Fix:** The authors must re-calculate this value and correct it throughout the manuscript (abstract, main text, and conclusions). If their 7.9% figure is correct, they must show the calculation that produces it.

**P3-M2 | Section V (p. 10) vs. Appendix C (p. 14)**
*   **Problem:** There is a significant inconsistency in the method used to calculate `σ(f_NL)` as a function of the bias enhancement factor `a`.
    *   Section V B uses the "Fisher-positivity-respecting form" `1/σ(f_NL)² = F₀ + c a²`. This is a non-linear (quadratic in `a`) relationship for the information `1/σ²`.
    *   Appendix C, Table VII is described as being derived by "linear scaling from the fiducial full 7-bin Fisher result at a = 0.15". This implies `σ(f_NL)` is treated as a linear function of `a`, which is only a first-order approximation and is inconsistent with the more robust formula in Section V.
    *   For example, using the formula from Section V with `F₀ = 1/8.98²` and `c = 0.0747`, `σ(f_NL)` at `a=0.20` is `1/sqrt(1/8.98² + 0.0747*0.2²) = 8.25`. This matches Table VII. However, at `a=0.50`, the formula gives `1/sqrt(1/8.98² + 0.0747*0.5²) = 6.99`, whereas Table VII lists `7.15`. The linear scaling approximation used for the table is inaccurate at larger `a`.
*   **Required Fix:** The authors must reconcile this. The preferred solution is to re-calculate all values in Table VII using the superior `1/σ² = F₀ + c a²` formula from the main text and remove the mention of "linear scaling". The methodology should be consistent throughout the paper.

#### MINOR

**P3-m1 | Table I, Page 7**
*   **Problem:** The footnotes to this table, particularly `†`, `‡`, `||`, and `§`, are extremely dense and contain a large amount of critical information that is difficult to parse. Key methodological details and results (e.g., the derivation of the final catalog count, definitions of different thresholds, cross-validation results) are buried here.
*   **Required Fix:** The authors should restructure this information. Move the most critical definitions and multi-step calculations into the main body text (e.g., in Section IID or the relevant survey-specific section). The footnotes should be reserved for brief, clarifying remarks. This will significantly improve the readability and transparency of the paper's core results.

**P3-m2 | Section III E, Page 6**
*   **Problem:** The text states for eROSITA: "XV-stability 81.5% (gate FAIL at 5σ subspace injection, but highest XV-stability of any Path-C survey)." This phrasing could be confusing. It correctly implies that the injection-recovery gate and the cross-validation stability are two different metrics, but it does not explicitly state why one leads to a FAIL while the other is a positive result.
*   **Required Fix:** Briefly clarify the distinction. For example: "The catalog fails the formal 5σ subspace injection-recovery gate (1.2% recovery). However, a separate cross-validation test on the anomaly-ranking stability yields 81.5%, the highest of any survey, suggesting the anomaly ranking itself is robust even if the specific injection test fails. The catalog is therefore retained with this diagnostic caveat."

**P3-m3 | Section I D, Page 3**
*   **Problem:** The phrase "reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository)" is redundant.
*   **Required Fix:** Remove the second instance of the phrase.

#### NIT

**P3-N1 | Abstract, Page 1**
*   **Problem:** The abstract reports the NANOGrav Savage-Dickey factor as `B_MB/SMBHB = 7.1×10³`. The value in the main text (Section V A, page 11) is `7.14×10³`.
*   **Required Fix:** Use a consistent number of significant figures in both places. `7.1×10³` or `7.14×10³` is acceptable, but they should match.

**P3-N2 | Bibliography, Page 19**
*   **Problem:** Reference [33] (Heinrich et al.) is listed with a publication year of 2024, but the BibTeX key is noted as `Heinrich2023` for "arXiv-submission-year continuity". This is unconventional and potentially confusing for citation software and readers.
*   **Required Fix:** While the explanation is provided in the text, the standard practice is to use the publication year in the key. Consider changing the key to `Heinrich2024` for consistency.

---

## Summary recommendation

**MAJOR REVISIONS**

This paper presents a valuable, large-scale anomaly catalog and a robust methodology for its creation. The work has clear potential for scientific impact, both in discovering rare objects and in cosmological applications. However, the manuscript in its current form suffers from critical numerical inconsistencies and a lack of clarity in the derivation of its headline results. The discrepancy in the `f_NL` forecast improvement and the inconsistent methods used to calculate it are particularly concerning for a submission to a physics journal. The paper cannot be accepted until these issues are thoroughly addressed. Once the authors have corrected the numerical claims and improved the clarity of the presentation, particularly regarding the contents of Table I, the paper will represent a strong contribution to the field.