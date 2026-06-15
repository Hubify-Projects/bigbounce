# P2 EXT19 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=dbcc5834 pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 198.4s

---

## Referee Report for PRD Submission

**Manuscript ID:** [Not provided, using internal designation P2]
**Title:** Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook
**Author:** Houston Golden

This paper presents a detailed forecast for testing the matter-bounce cosmological scenario using primordial non-Gaussianity. The primary prediction, a local non-Gaussianity parameter `f_NL = -35/8`, is confronted with the projected sensitivities of the SPHEREx and MegaMapper surveys. The work is framed as a "sensitivity recast" of existing survey forecasts, applying a rigorous analysis of the specific theoretical prediction, including template mismatch, theoretical uncertainties, and a comprehensive budget of observational systematics. The paper also provides a Bayesian model comparison to quantify the discriminating power against inflationary alternatives.

The manuscript is exceptionally thorough, well-structured, and transparent in its methodology and assumptions. The scientific contributions are significant, particularly:
1.  A careful resolution of a factor-of-two discrepancy in the literature regarding the predicted `f_NL` value, grounded in an explicit operator-algebra derivation.
2.  A novel and detailed quantification of the theoretical uncertainty arising from the underdetermined polynomial structure of the bounce bispectrum.
3.  A comprehensive and transparent systematic budget that traces the forecast significance from an idealized value down to a realistic, on-sky expectation.
4.  A robust Bayesian analysis that explores sensitivity to prior choices and provides a clear framework for model discrimination.

The paper is of high quality and is well-suited for publication in Physical Review D. The analysis is rigorous, the conclusions are well-supported by the calculations presented, and the paper makes a valuable contribution to the field by providing a clear and testable benchmark for upcoming cosmological surveys. I have only a few minor suggestions for improvement.

---
### Findings

#### MINOR

**ID: P2-N1**
*   **Section/Page:** II.A, page 3
*   **Problem:** The description of the monomial basis for the degree-9 polynomial `P` is quite technical and may be difficult to parse for readers not deeply familiar with bispectrum shape analysis. While the detail is valuable for experts, the main takeaway for the core argument is that a 6-parameter basis is used to represent a function constrained by 3 benchmark values, leading to a 3-dimensional null space.
*   **Required Fix:** Consider slightly restructuring the paragraph beginning "We adopt the bispectrum shape function..." to state the conclusion first (i.e., the existence and dimension of the null space) before detailing the specific monomial basis. This is a stylistic suggestion to improve readability, and the current text is not incorrect.

**ID: P2-N2**
*   **Section/Page:** VI.C, page 12
*   **Problem:** The text states, "The four-corner Bayes-factor prior grid reported in this section... is computed analytically via the closed-form Bayes-factor integration...; the Monte Carlo ensembles span only a subset of these corners...". This is clear, but the subsequent paragraph begins, "Each realization draws a mock `f_obs`... then computes the Bayes factor analytically...". It could be momentarily confusing whether the main results are from the MC or the direct analytic computation. The text does clarify this, but it could be made even more direct.
*   **Required Fix:** Suggest adding a sentence at the beginning of the "Quantitative Bayesian Comparison" section to explicitly state the hierarchy of methods. For example: "The primary results of this section are derived from a direct, analytic evaluation of the Bayes factor formula (Eq. 9). We validate this analytic approach and map its sensitivity to nuisance parameters using three independent Monte Carlo ensembles, as described below."

**ID: P2-N3**
*   **Section/Page:** Appendix A, page 25
*   **Problem:** The text states: "The `f_NL` constrained by the SPHEREx estimator and the `f_NL = -35/8` predicted by the matter bounce are therefore the same quantity, with no residual conversion factor between the appendix and survey normalizations." This is a key point, but the parenthetical derivation that follows (`B_ζ = ... = 6/5 f_NL P_ζ^2[...]`) is extremely dense.
*   **Required Fix:** The derivation within the parentheses is correct but hard to follow. Suggest expanding this into a few separate, displayed equations to make the mapping between the `Φ`-field normalization (`c=2`) and the `ζ`-field normalization (`6/5`) more transparent. This would strengthen the already excellent appendix.

---
## Summary recommendation

**ACCEPT WITH MINOR CORRECTIONS**

This is an exemplary theory/phenomenology paper. It is meticulously researched, transparent about its assumptions and limitations, and provides a clear, actionable forecast for a major upcoming survey. The authors have done an excellent job of anticipating and addressing potential points of confusion, such as the literature discrepancy in the `f_NL` value and the proper comparison of constraints from different observational channels. The quality of the analysis and the clarity of the presentation meet the high standards of Physical Review D. I recommend acceptance after the authors have had an opportunity to consider the minor points raised above.