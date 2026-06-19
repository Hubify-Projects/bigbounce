# P2 D1 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=99e6426c pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 221.3s

---

**Referee Report on "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook"**

This paper presents a detailed forecast for testing the matter bounce cosmological scenario using primordial non-Gaussianity signatures in upcoming large-scale structure surveys, primarily SPHEREx. The authors perform a sensitivity recast of existing forecasts, focusing on the specific local-type non-Gaussianity prediction `f_NL = -35/8` from the quasi-dust matter bounce model. The work includes a comprehensive analysis of the template mismatch between the bounce bispectrum and the standard local template, a detailed systematic budget, and a Bayesian model comparison to assess the discriminating power against inflationary alternatives.

The paper is exceptionally thorough, well-structured, and rigorously argued. The authors demonstrate a deep understanding of the theoretical underpinnings of the bounce model, the subtleties of non-Gaussianity estimation in large-scale structure, and the potential observational systematics. The resolution of the factor-of-two discrepancy in the literature regarding the predicted `f_NL` value is a significant contribution in itself and is handled with admirable clarity in Appendix A. The figures and tables are clear, informative, and provide an excellent summary of the paper's key results. The provision of analysis code and data artifacts for reproducibility is commendable.

While the paper is of very high quality and suitable for publication in Physical Review D, I have identified a few points that require revision to further strengthen the manuscript and ensure its conclusions are presented with maximum clarity and appropriate caveats.

## Summary of Findings

### ESSENTIAL

**P2-E1: Abstract-Body Consistency on Bayes Factor.**
*   **Section/Page:** Abstract (p. 1) and §VI.C (p. 14).
*   **Problem:** The abstract reports the main Bayes factor result as `BF ≈ 9-14`. The body and Table II caption explain that this range is derived by applying a "noise-weighted r ≈ 0.84 rebooking" to the `r→1` endpoint values of `BF ~ 10-17`. While this logic is sound and well-explained in the body, presenting the rebooked range as the primary finding in the abstract is slightly indirect. The abstract should more clearly state the result for the recommended prior first, and then the theoretical maximum from which the range is constructed, to avoid any potential ambiguity for the reader. The current phrasing `BF ≈ 9... up to BF ≈ 14` could be misinterpreted, as the `14` comes from the delta-prior maximum, not the recommended prior.
*   **Fix:** Rephrase the abstract to state the recommended-prior result first, then the theoretical maximum, and clarify that the headline range applies a consistent template-mismatch correction. For example: "A SPHEREx detection... favors the bounce over tuned multifield competitors at Bayes factor BF ≈ 9 (for a recommended Gaussian bounce prior and broad multifield competitor, after template-mismatch correction), with the preference rising to BF ≈ 14 at the theoretical maximum (a delta-function bounce prior)." This more accurately reflects the logic presented in the main text.

### MAJOR

**P2-M1: Prominence of Systematic Combination Method.**
*   **Section/Page:** Abstract (p. 1), §VII (p. 16-17), Table IV (p. 20).
*   **Problem:** The paper combines systematic uncertainties (e.g., from `b_φ` and GR projections) using additive quadrature. This is described in Table IV's caption and mentioned in Sec IIC as a "transparent scoping choice". However, this method ignores potential correlations between systematic effects and is an approximation to a full joint Fisher matrix analysis where all nuisance parameters are marginalized over simultaneously. While this is acceptable for a forecast paper, the limitations of this approach should be stated more prominently in the main text to properly contextualize the "realistic" and "conservative" significance forecasts.
*   **Fix:** Add a sentence in the main text of Section VII (e.g., at the beginning of the section or where the budget is first introduced) explicitly stating that the systematic contributions are combined in quadrature as a scoping estimate, and that a full joint analysis could yield a tighter or looser constraint depending on the unknown covariance between the nuisance parameters. This is crucial for managing reader expectations about the precision of the forecast.

**P2-M2: Quantification of Non-Local Shape Losses.**
*   **Section/Page:** §IV (p. 10).
*   **Problem:** The paper correctly identifies a key caveat: "...potential additional losses from the non-local tails of the bounce shape in the bispectrum estimator covariance are not modeled." This is an important unquantified systematic. The analysis relies on the amplitude degradation factor `r` (from projection onto the local template) and argues that projection noise is small based on the high value of `r_cos`, but it does not estimate the potential increase in the estimator's variance due to the shape mismatch.
*   **Fix:** The authors should provide at least an order-of-magnitude estimate for this effect. A full calculation is not required, but a scaling argument or reference to analogous results in the literature would significantly strengthen the analysis. For instance, the authors could argue that the fractional increase in variance is of order `1-r^2` or `1-r_cos^2`, and show that this is subdominant to other systematics in the budget. Adding such an estimate, properly caveated, is necessary for a complete systematic assessment.

### MINOR

**P2-m1: Terminology for Forecast Tiers.**
*   **Section/Page:** Throughout, e.g., Abstract (p. 1), Figure 2 (p. 11).
*   **Problem:** The paper uses several tiers of forecasts: "optimistic", "realistic", and "conservative" (or "all-combined conservative"). The distinction between "realistic" and "conservative" is at times ambiguous without referring back to the precise definitions in the text. The "realistic" range `~2.6-5σ` appears to be an envelope spanning from the most conservative floor up to a moderately degraded scenario, which is not immediately intuitive from the label.
*   **Fix:** Consider refining the terminology for clarity. For instance, "post-systematics envelope" might be more descriptive than "realistic range". While the text provides the necessary definitions, crisper labels would improve readability. This is a suggestion for improvement.

**P2-m2: Citation for Spherical Collapse Threshold.**
*   **Section/Page:** §III.A (p. 7).
*   **Problem:** The text introduces the spherical-collapse threshold `δ_c ≈ 1.686` without a citation. While this is a textbook value, a canonical reference should be provided for completeness and rigor.
*   **Fix:** Add a standard citation for the value of `δ_c`.

### NIT

**P2-N1: Multiplication Symbol in Table IV.**
*   **Section/Page:** Table IV Caption (p. 20).
*   **Problem:** The caption contains the expression `Significance = |f_NL| x r / σ_eff`. The symbol for multiplication `x` should be replaced with the standard LaTeX command `\times` for clarity and proper typesetting.
*   **Fix:** Change `x` to `\times`.

**P2-N2: Phrasing of SPHEREx Launch Date.**
*   **Section/Page:** Abstract (p. 1), §IX.A (p. 21).
*   **Problem:** The paper, dated June 2026, states SPHEREx "launched March 2025". This future-perfect tense can be awkward.
*   **Fix:** It is recommended to use phrasing that is robust to minor schedule changes, such as "scheduled for launch in early 2025" or "expected to launch in 2025".

## Summary recommendation
**MAJOR REVISIONS**

The paper is of high quality and presents a valuable and timely forecast. The analysis is deep, careful, and transparent. The recommendation for Major Revisions is based on the need to address the points above, particularly P2-E1, P2-M1, and P2-M2. Sharpening the abstract's claims to directly match the derivation, clarifying the limitations of the systematic combination method more prominently, and providing an estimate for unmodeled covariance losses are necessary steps to ensure the paper meets the highest standards of rigor. I am confident that the authors can address these points effectively, and I look forward to reviewing the revised manuscript.