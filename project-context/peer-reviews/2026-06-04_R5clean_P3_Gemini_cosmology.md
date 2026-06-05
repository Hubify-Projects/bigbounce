# P3 2026-06-04_R5clean — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 84.5s

---

**Referee Report on "Spectrally Unusual Sources at Scale..." (P3)**

This paper presents a large-scale anomaly detection campaign across seven astronomical surveys, resulting in a catalog of over 378,000 unique anomalies. The work details the "Path-C" methodology, which includes per-survey native model retraining to correct for significant cross-transfer artifacts. The paper then uses a subset of the resulting catalog to perform a multi-tracer forecast for primordial non-Gaussianity (fNL) and checks for consistency with pulsar-timing-array data under a specific bounce cosmology model.

The work represents a substantial and valuable contribution. The scale of the catalog is impressive, and the methodological lessons, particularly regarding the training-bias artifacts in LAMOST and the domain-shift inflation in SDSS, are of significant importance to the machine-learning and astronomy communities. The cosmological analysis is performed with theoretical care, correctly handling the limitations of Fisher forecasts and showing awareness of key theoretical issues like GR projection effects.

However, the paper requires significant revision before it can be considered for publication in Physical Review D. The primary issues relate to the paper's structure, clarity of presentation, and excessive length. The scientific content is strong, but it is obscured by a confusing and poorly organized manuscript.

## Detailed Findings

### ESSENTIAL

**P3-E1: Section III, Page 15, Table I**
*   **Problem:** Table I, the main summary table of the survey, is highly misleading. The primary `Nanom` column reports the initial, superseded "cross-transfer" anomaly counts. The final, canonical "Path-C native-retrained" counts, which are the main result of the paper, are not in the table and are only referenced in the footnotes and text. This design guarantees that a casual reader will misunderstand and cite the wrong numbers.
*   **Fix:** Redesign Table I to make the final, canonical results the primary entry. The "cross-transfer" baseline numbers should be moved to a separate column labeled "Initial Baseline (Superseded)" or removed to a separate diagnostic table in an appendix. The current presentation is unacceptable for a final publication.

### MAJOR

**P3-M1: Section VI D, Pages 26-30, "Path-C Rebuild Residual Caveats"**
*   **Problem:** This entire section is written like an internal changelog or a response to a previous round of reviews, not as a section of a scientific paper. It is a long, unstructured list of resolved issues, validation checks, and justifications that completely disrupts the narrative flow of the paper. It contains numerous instances of internal-review-style language (e.g., "CLOSED", "The fallback-plan... is no longer triggered", "No table restructure is required", references to "earlier paper versions"). This is inappropriate for a formal publication.
*   **Fix:** This section must be completely removed and its contents properly integrated elsewhere.
    *   Final validation results (e.g., Jaccard stability, injection-recovery curves) should be moved to the relevant parts of the Methods (Sec. II) or Results (Sec. III) sections.
    *   Detailed methodological justifications and extended discussions of specific tests (e.g., the plant morphology dependence, the Fisher positivity derivation) should be moved to an Appendix on Validation Details.
    *   All language that refers to the paper's own development process must be removed. The paper should present the final, static methodology and results.

**P3-M2: Overall Paper Length and Structure**
*   **Problem:** At 49 pages, the paper is excessively long for a methods and catalog paper in PRD. The core scientific contributions are diluted by repetitive discussions and poor organization, particularly in Section VI.
*   **Fix:** The paper must be significantly restructured and condensed. A target length of 25-30 pages for the main text and references would be more appropriate.
    *   Restructure Section VI as a concise "Discussion and Limitations" section.
    *   As noted in P3-M1, redistribute the content of the current Section VI D.
    *   Streamline the cosmological application section (Sec. V). The important discussion of the Fisher-positivity-respecting `α^2` form is presented multiple times (Abstract, Sec. V, Sec. VI D); it should be presented once clearly in the main analysis section.
    *   The extensive image galleries are appropriate for appendices but the main text must be more focused.

### MINOR

**P3-m1: Section V, Page 23, GR Projection Effects**
*   **Problem:** The paper states that `O(H^2/k^2)` GR projection corrections "must be deterministically subtracted from the template, not marginalized over". While correct, the analysis then proceeds with a forecast that omits these terms entirely. A later check in Sec. VI.D(e) finds the effect to be negligible (`<0.02%`) for the k-range considered.
*   **Fix:** The check for the impact of GR projection effects should be briefly mentioned in the main systematics discussion in Section V, rather than being buried in the "Residual Caveats" section. For example, after noting the terms are omitted, add a sentence like: "We have verified that for our analysis, which extends to `k_max = 0.2 h/Mpc`, the contamination from these terms to the `σ(fNL)` forecast is below 0.1%, justifying their omission in this forecast." This clarifies that the issue was considered and addressed.

**P3-m2: Section III C, Page 12, SDSS Native Catalog Count**
*   **Problem:** The paper chooses to publish a top-slice of the native SDSS anomaly catalog containing 77,905 objects, explicitly to match the count from the superseded cross-transfer analysis for "bookkeeping convenience". This is an arbitrary choice that mixes a physically-motivated native ranking with a count derived from a methodological artifact. It is confusing and undermines the clean result that only 12 objects pass the canonical `S > 5` threshold.
*   **Fix:** The authors should use a physically or statistically motivated threshold for the canonical SDSS native catalog (e.g., the 12 objects with `S > 5`, or a top-1% cut for consistency with other surveys). The "bookkeeping" choice should be abandoned. If they insist on retaining it, the justification needs to be much stronger than "convenience".

**P3-m3: Abstract, Page 2**
*   **Problem:** The phrase "the agreement is far tighter than 'within 1σ' would suggest" is too colloquial for a scientific abstract.
*   **Fix:** Rephrase to be more formal. For example: "...the empirical central value is only 0.06σ from the fiducial, indicating close agreement."

### NIT

**P3-n1: Section III F 0 b, Page 4**
*   **Problem:** There is a reference to "Section III F 0 b". This appears to be a typo or an internal section numbering that was not updated.
*   **Fix:** Correct the section reference. It likely refers to the part of Appendix F that discusses the cross-transfer ACT model.

## Summary recommendation

**MAJOR REVISIONS**

The paper presents a scientifically valuable dataset and a methodologically insightful analysis. The core contributions—the large-scale catalog, the resolution of major instrumental and domain-shift artifacts via native retraining, and the careful cosmological forecast—are significant. However, the manuscript in its current form is not acceptable. The confusing presentation of key results (Table I), the severe structural problems in the discussion section (Sec. VI D), and the excessive length obscure the paper's strengths. The authors must undertake a major restructuring and revision to improve clarity, focus, and readability before the paper can be published. The scientific content is sound, but the manuscript requires substantial editorial work.