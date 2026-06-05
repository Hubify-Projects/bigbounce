# P3 auto-2026-06-05_1418pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 127.1s

---

## Referee Report on "Spectrally Unusual Sources at Scale..."

This paper presents a large-scale, multi-survey anomaly detection campaign using an autoencoder framework. The authors apply their method to 37.3 million sources across seven astronomical archives, producing a catalog of over 378,000 unique anomalies. The work is notable for its scale and its careful, self-critical methodology, particularly the "Path-C rebuild" protocol which uses native retraining for each survey to overcome cross-transfer artifacts. The paper also presents forecasts for cosmological constraints on primordial non-Gaussianity (`f_NL`) and consistency checks with matter-bounce predictions for the nanohertz gravitational-wave background.

The paper is comprehensive, methodologically sound, and presents a valuable data product and set of scientific forecasts. The authors are commendably transparent about the limitations of their work and the residual caveats. However, several points require clarification and revision before the paper can be considered for publication in Physical Review D. The primary concerns relate to the clarity of the validation process for some surveys and the presentation of key results in summary tables.

### ESSENTIAL

*   **P3-E1: Overly-dense footnotes in Table I (Page 7)**
    *   **Problem:** Table I is the primary summary of the paper's results. However, a vast amount of critical methodological detail is relegated to extremely dense footnotes (especially footnotes `||`, `§`, and `‡`). This includes the different thresholding schemes used for different surveys, the distinction between the initial cross-transfer counts and the final canonical native-retrained counts, and the results of the validation gates. This information is essential for understanding the composition and reliability of the final catalog and should not be buried in fine print.
    *   **Fix:** This information must be moved into the main body of the text, likely in Section II.D ("Path-C Rebuild Methodology") or Section III ("Survey-by-Survey Results"). The table itself should be simplified to present the final, canonical results, with the text providing the necessary context and justification for the methods used for each survey.

*   **P3-E2: Unsupported precision on GR projection effect (Section V C, Page 10)**
    *   **Problem:** The paper claims that "General-relativistic projection corrections (O(H²/k²)) contribute |Δσ/σ| < 0.02% at k_max = 0.2 h Mpc⁻¹". This is a very precise claim. While the effect is expected to be small, the cited reference [38] (Yoo et al. 2009) provides the general formalism but does not contain this specific calculation for this specific tracer population.
    *   **Fix:** The authors must provide a brief derivation of this number in an appendix or cite a paper that performs this explicit calculation for a similar high-redshift, high-bias tracer sample.

### MAJOR

*   **P3-M1: Ambiguous validation status of photometric surveys (e.g., Section III E, Page 6)**
    *   **Problem:** The paper's validation framework is presented as a key strength, but its application to the photometric surveys is confusing. For eROSITA, the abstract and Section IID state it fails the injection-recovery gate ("FAIL-with-diagnostic at 5σ... eROSITA 1.2%"). However, other sections and footnotes praise its high cross-validation stability ("XV-stability 81.5% (gate FAIL at 5σ subspace injection, but highest XV-stability of any Path-C survey)"). This sends a mixed message. If the injection-recovery test is the canonical gate, it is unclear why surveys that fail it are retained in the final "catalog-grade" sample. The same ambiguity applies to Gaia.
    *   **Fix:** The authors must clarify the hierarchy of their validation metrics. Which test is decisive? If a survey fails the primary gate, what is the justification for its inclusion in the final catalog? The paper should explicitly state that the photometric survey anomaly catalogs are more exploratory due to these validation failures. The abstract and conclusions must accurately reflect this more nuanced status.

### MINOR

*   **P3-m1: Justification for the `f_NL` Fisher forecast form (Section V b, Page 10)**
    *   **Problem:** The paper uses the form `1/σ(f_NL)² = F₀ + c a²` for the Fisher forecast, calling it "Fisher-positivity-respecting". This term is not standard. While the quadratic form is physically motivated, a brief explanation is warranted.
    *   **Fix:** Add a sentence explaining why this quadratic form is chosen over, for example, a linear expansion in the bias enhancement `a`. For instance, "We adopt this quadratic form to ensure the forecast variance remains positive and to capture the leading-order dependence on the bias enhancement, which enters the power spectrum as `b²`."

*   **P3-m2: Jargon in systematics discussion (Section V C, Page 10)**
    *   **Problem:** The sentence "...δb is broken by the multi-tracer technique" is jargon.
    *   **Fix:** Rephrase for clarity. For example, "...the degeneracy between `f_NL` and the nuisance parameter δb can be broken by combining multiple tracers with different intrinsic biases."

*   **P3-m3: Use of two different anomaly detectors for eROSITA (Section III E, Page 6 & Table III, Page 8)**
    *   **Problem:** For eROSITA, the paper uses the main BigAE autoencoder to produce the canonical scores but uses a separate IsolationForest model for cross-validation. This is the only survey for which a different algorithm is introduced. The motivation for this is unclear.
    *   **Fix:** Briefly explain why IsolationForest was used for the eROSITA cross-validation instead of the main BigAE framework.

*   **P3-m4: Paper length (20 pages)**
    *   **Problem:** The paper is long and dense, which may hinder its accessibility. Some detailed material, while valuable, could be moved to streamline the main text.
    *   **Fix:** The authors should consider moving some of the more detailed derivations and documentation (e.g., the full MCMC provenance in Appendix E, the detailed taxonomy galleries in Appendix D) to supplementary online material.

*   **P3-m5: Confusing presentation of results in Table I (Page 7)**
    *   **Problem:** Table I presents the initial *cross-transfer* anomaly counts in the main columns. The final, canonical *native-retrained* counts, which are the primary result of the paper's improved methodology, are described only in the footnotes. This is misleading. For example, the LAMOST row lists 44,075 anomalies, while the final catalog actually contains 113,342 from this survey. This misrepresents the final catalog's composition in the main summary table.
    *   **Fix:** Revise Table I to show the final, canonical, native-retrained anomaly counts in the `N_anom` column. The initial cross-transfer counts should be moved to the footnotes or a separate column clearly labeled as a "before" diagnostic.

### NIT

*   **P3-N1: Future date (Page 1)**
    *   **Problem:** The paper is dated "(Dated: June 2026)".
    *   **Fix:** Correct to the current submission date.

*   **P3-N2: Unconventional author contact (Page 1)**
    *   **Problem:** The contact email `houston@hubify.com` is unconventional for a scientific publication.
    *   **Fix:** An institutional email address should be used.

*   **P3-N3: Non-standard footnote symbol in Table I (Page 7)**
    *   **Problem:** The footnote marker for SDSS DR18 is a degree symbol (`°`), which is non-standard and easily missed.
    *   **Fix:** Replace with a standard footnote symbol (e.g., a letter).

## Summary recommendation
**MAJOR REVISIONS**

This is a substantial and impressive piece of work that presents a valuable contribution to the field of astronomical data analysis and its application to cosmology. The methodological rigor, particularly the native-retraining protocol and the careful distinction between different types of novelty, is a major strength. The paper is well-written and the authors are commendably transparent about the limitations of their analysis.

However, the issues outlined above, particularly the lack of clarity regarding the validation of photometric surveys (P3-M1) and the confusing presentation of the main catalog counts in Table I (P3-m5, P3-E1), must be addressed before publication. These revisions are necessary to ensure that the final catalog's composition and reliability are clearly and accurately communicated to the reader. Once these points are satisfactorily resolved, the paper will be an excellent candidate for publication in Physical Review D.