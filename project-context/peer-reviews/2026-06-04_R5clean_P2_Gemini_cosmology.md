# P2 2026-06-04_R5clean — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 62.3s

---

## Referee Report on "Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook"

This paper presents a detailed forecast for testing the matter bounce scenario using primordial non-Gaussianity constraints from the upcoming SPHEREx survey, with an outlook towards the proposed MegaMapper experiment. The authors perform a comprehensive analysis, including a critical audit of the theoretical prediction for the non-Gaussianity parameter `fNL`, a first-time quantification of the template mismatch between the bounce signal and the standard local template, and a Bayesian model comparison against inflationary alternatives. The work is timely and addresses an important question in early universe cosmology.

The paper's strengths are its thoroughness in identifying and quantifying theoretical and systematic uncertainties, the careful clarification of a factor-of-two ambiguity in the literature regarding the predicted `fNL` value, and the robust validation of its results. The analysis of the underdetermined polynomial coefficients and the resulting uncertainty is a novel and important contribution.

However, the manuscript in its current form contains several issues that must be addressed before it can be considered for publication. These range from essential corrections involving the removal of internal review artifacts and misleading comparisons, to major revisions needed to make the paper a self-contained scientific contribution.

### ESSENTIAL

*   **P2-E1 (Various pages): Presence of internal review artifacts and version history.**
    *   **Problem:** The manuscript contains text that is clearly part of an internal review or version control process, which is inappropriate for a submitted paper.
        *   Page 18, Appendix A: "the cross-model peer-review concern (R42 Gemini 3.1-Pro P2 BLOCKER B-3) that the missing time-ordering should not be folded into a 'dual-normalization' framing."
        *   Page 18, Conclusion: "the prior conclusion-paragraph figure '> 6×105' was an aggregation error retired in §VI"
    *   **Required Fix:** All such internal comments, tags, and version history notes must be removed from the manuscript. The text should be written as a final, public-facing scientific document.

*   **P2-E2 (Page 16, Sec. IX.D): Misleading comparison of different Fisher forecasts.**
    *   **Problem:** Section IX.D, "Joint (fNL, nfNL) Forecast as a Stronger Discriminator," introduces a second, distinct Fisher analysis based on scale-dependent bias (SDB). The results of this analysis (e.g., a ~9.9σ detection of `fNL`) are presented alongside the paper's primary, bispectrum-based forecast (3–5σ). The paper correctly states that the two forecasts are different, but the comparison is fundamentally misleading. The SDB forecast is described as "idealized" and relies on inputs from a "companion-artifact Fisher-input release" which is not part of this paper. This compares a realistic, systematics-degraded forecast (the paper's main result) with an idealized, unverified forecast. Presenting the ~9.9σ figure so prominently gives undue weight to a result that is not substantiated within this work and is not on the same footing as the main forecast.
    *   **Required Fix:** The quantitative results of the joint SDB analysis (`σ(nfNL) = 0.086`, `ρ = 0.966`, the ~9.9σ detection significance, the 6.1x improvement) must be removed from the main body of the paper. This analysis should be framed strictly as a motivation for future work. The entire discussion needs to be significantly downplayed to avoid confusing the reader about what the primary, defensible forecast of this paper is. The headline result of the paper is the 3-5σ bispectrum forecast, and this should not be overshadowed by a speculative, idealized calculation.

### MAJOR

*   **P2-M1 (Abstract, Page 16): Deferral of results to a "companion artifact".**
    *   **Problem:** The paper repeatedly refers to a "companion artifact" where the full Fisher inputs and results for the joint (fNL, nfNL) analysis are located. A scientific paper submitted for publication must be self-contained. It is unacceptable to quote specific numerical results (like `σ(nfNL) = 0.086`) in the main text while deferring the entire methodology and validation for those results to an external document. This prevents the reader and referee from being able to assess the validity of the claims.
    *   **Required Fix:** The paper must be made self-contained. The authors have two options: (1) Remove all specific quantitative results from the joint (fNL, nfNL) analysis and refer to it only qualitatively as a promising future direction. (2) Include a summary of the methodology and key inputs for the joint analysis in an appendix of this paper, sufficient for the reader to understand how the results were derived. The current approach of quoting numbers without justification is not acceptable. The abstract, in particular, must be rewritten to remove the awkward phrasing about this deferred release.

### MINOR

*   **P2-m1 (Page 14, Table III): Redundant "sanity row" in table.**
    *   **Problem:** The final row of Table III, "Corrected (10% residual; sanity row)", is described as a "no-op sanity row" and is numerically identical to the "Ideal (no GR)" row. This is redundant and confusing.
    *   **Required Fix:** Remove this row from the table. The point that a 10% residual correction is negligible can be made in the table's caption or the main text.

*   **P2-m2 (Page 7): Filename in main prose.**
    *   **Problem:** The text reads: "...the per-realization spread from phase3_fisher_overlap.json is wider...". This appears to be a raw filename from the analysis code.
    *   **Required Fix:** Rephrase this to be more professional, for example: "...the spread across individual realizations in our Fisher analysis is wider...".

*   **P2-m3 (Abstract): Awkward phrasing regarding future releases.**
    *   **Problem:** The abstract contains the sentence: "...is deferred to a companion artifact and the specific numerical significance is not quoted here in the abstract until that release lands)." This is self-referential and inappropriate for a formal scientific abstract.
    *   **Required Fix:** Remove this sentence and ensure the abstract summarizes the content *of this paper* only.

*   **P2-m4 (Page 17, Sec. E): Lack of clarity on observable parity.**
    *   **Problem:** The "Caveats" section discusses cosmic birefringence as a complementary test. While this is interesting, `fNL` from the scalar bispectrum is a parity-even observable, whereas cosmic birefringence is parity-odd. This is a fundamental distinction.
    *   **Required Fix:** Add a sentence to this paragraph to explicitly state that cosmic birefringence is a parity-odd observable, making it a test of different physics (e.g., a coupling to a pseudoscalar) and thus truly complementary to the parity-even `fNL` channel.

### NIT (Nitpick/Suggestion)

*   **P2-N1 (Overall): Paper Length.**
    *   **Problem:** At 22 pages, the paper is on the longer side for a forecast paper. The content is valuable, but the narrative flow could be improved by moving some of the more technical details to appendices.
    *   **Required Fix (Suggestion):** The authors could consider moving the detailed discussion of the null-space sampling (from Sec. II) and some of the validation steps (e.g., from Sec. III.B) into appendices. This could help shorten the main text to a more standard ~18-20 pages, improving readability.

*   **P2-N2 (Page 9, Fig. 3): Minor figure inconsistency.**
    *   **Problem:** The figure caption states "SPHEREX 1σ error bar shown in blue," but the figure itself has no legend entry for the blue error bar.
    *   **Required Fix (Suggestion):** Add a legend to the plot to explicitly label the SPHEREx error bar for clarity.

## Summary recommendation
**MAJOR REVISIONS**

This paper represents a significant and high-quality body of work that will be a valuable contribution to the field. The authors have done an excellent job in carefully analyzing the theoretical prediction for `fNL` in matter bounce cosmology and translating it into a robust forecast for SPHEREx. However, the manuscript is marred by the inclusion of internal review artifacts and, more seriously, by a misleading presentation of an idealized forecast whose details are not included in the paper. These issues must be fully addressed. Once the essential and major revisions are completed, the paper should be suitable for publication in Physical Review D.