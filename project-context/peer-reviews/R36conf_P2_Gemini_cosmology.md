# P2 R36conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.58.pdf` md5=6b3c9b5e pages=27
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 168.3s

---

**Referee Report on "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook"**

**Manuscript ID:** [Assigned by journal]
**Author:** Houston Golden
**Date:** [Current Date]

This paper presents a detailed sensitivity forecast for testing the matter bounce scenario using upcoming data from the SPHEREx survey, with an outlook towards the proposed MegaMapper experiment. The primary focus is on the distinctive prediction of local-type non-Gaussianity, `f_NL = -35/8`. The author recasts existing SPHEREx forecasts to account for the specific shape of the matter bounce bispectrum, quantifies a range of systematic uncertainties, and performs a Bayesian model comparison against inflationary alternatives. A key contribution is the resolution of a factor-of-two discrepancy in the predicted `f_NL` value found in the literature.

The paper is well-structured, the analysis is comprehensive, and the claims are generally well-supported by detailed calculations. The transparency regarding corrections from previous analyses and the careful treatment of assumptions are commendable. The resolution of the `f_NL = -35/8` vs. `-35/16` ambiguity in Appendix A is a valuable contribution to the field. However, there is one major point concerning the Bayesian analysis that requires clarification before the manuscript can be considered for publication. Several minor revisions are also recommended to improve clarity.

---

### **MAJOR REVISIONS**

*   **P2-M1: Ambiguity in Bayes Factor Bookkeeping Calculation**
    *   **Location:** Section VI.a, Page 14
    *   **Problem:** The subsection "Template-mismatch bookkeeping of the Bayes factors" describes how the Bayes factors are adjusted to account for the template mismatch `r < 1`. The text states that the `r -> 1` envelope of `BF ~ 10-17` "correspondingly reads ~9-14 in strict bounce-amplitude bookkeeping". However, the method for this "rebooking" is not explained. The reduction is described as "modest," but the calculation is not reproducible from the information given. It is unclear how the factor `r` is incorporated into the Bayes factor calculation of Eq. (8). For instance, is the likelihood evaluated at a shifted prediction `r * f_bounce`, or is the effective `sigma` of the experiment rescaled? These different procedures are not equivalent and would lead to different results.
    *   **Required Fix:** The author must explicitly state the methodology used to calculate the adjusted Bayes factors. This should include the precise formula and a clear statement of what is being assumed about the mock observation and the model prediction in the likelihood function. For example, if the mock data is centered at `f_NL = -35/8`, the likelihood for the bounce model should be evaluated at `r * (-35/8)`, which would introduce a penalty. This needs to be made transparent to the reader.

---

### **MINOR REVISIONS**

*   **P2-m1: Ambiguous Phrasing in Abstract**
    *   **Location:** Abstract, Page 1
    *   **Problem:** The sentence "a curvaton-natural [-5, +5] competitor narrows this to BF ~ 4-7" could be misinterpreted as a narrowing of the previously stated `BF ~ 9-14` range. The intended meaning is that `BF ~ 4-7` is the result *against* this different, narrower competitor prior.
    *   **Required Fix:** Rephrase for clarity. Suggestion: "Against a more physically motivated curvaton-natural competitor prior of [-5, +5], the corresponding Bayes factor is BF ~ 4-7."

*   **P2-m2: Missing Explicit Calculation for "All-Combined" Significance**
    *   **Location:** Section IV, Page 9
    *   **Problem:** The text introduces the "realistic range" of `~2.6-5 sigma` and states the lower endpoint reflects the "all-combined cumulative budget," which includes GR projection and `b_phi` marginalization. While the ingredients are discussed in the paper, the explicit calculation combining them to arrive at `~2.6 sigma` is not shown in this section.
    *   **Required Fix:** For reader convenience and clarity, add a brief, explicit calculation demonstrating how the various systematic effects are combined to produce the `~2.6 sigma` lower bound. This would involve specifying the assumed `sigma_GR` and the effective `sigma(f_NL)` after `b_phi` marginalization, and then applying them in quadrature along with the template mismatch factor `r`.

*   **P2-m3: Convoluted Phrasing of Bayes Factor Range**
    *   **Location:** Section VI, Page 12
    *   **Problem:** The sentence "The recommended-to-theoretical-maximum range ~ 10-17 quoted in the abstract as the r -> 1 bookkeeping endpoint... therefore brackets the recommended baseline (theory = 1.0, lower bound) and the delta-prior maximum (upper bound)..." is dense and difficult to parse.
    *   **Required Fix:** Simplify the language to state the results more directly. Suggestion: "The Bayes factor for the recommended `sigma_theory=1.0` prior is ~10, while the theoretical maximum (using a delta prior) is ~17. This defines a range of ~10-17, which corresponds to the ideal `r=1` scenario."

---

### **NITPICKS (Cosmetic)**

*   **P2-N1: Overloaded Symbol `sigma`**
    *   **Location:** Page 4 (and throughout)
    *   **Problem:** The symbol `sigma` is used for both standard deviation (e.g., `sigma(f_NL)`) and for the singular values of a matrix (`sigma_1, sigma_2, ...`).
    *   **Required Fix:** While the context prevents serious confusion, consider using a different symbol for the singular values (e.g., `s_i`) to improve readability.

*   **P2-N2: Confusing Reference in Table III Caption**
    *   **Location:** Table III, Page 18
    *   **Problem:** The caption states: "the no-GR cell (7.0) coincides with the narrow-broad sweep BF ~ 7 -> 17 at the delta bounce prior reported in the prose of §VI". This phrasing is slightly confusing, as it seems to equate a single value (7.0) with a range (7-17).
    *   **Required Fix:** Rephrase for clarity. Suggestion: "The no-GR cell value of 7.0 (against the narrow `[-5,+5]` competitor) is the lower end of the BF ~ 7-17 range discussed in §VI, which spans from the narrow to the broad competitor prior."

---

## Summary recommendation

**MAJOR REVISIONS**

The manuscript represents a substantial and high-quality piece of work that will be of significant interest to the cosmology community. The analysis is thorough, and the clarification of the `f_NL` prediction for the matter bounce is a valuable service. The paper is almost ready for publication in Physical Review D. However, the lack of a clear, reproducible description of the Bayes factor "rebooking" procedure under template mismatch is a significant omission that must be addressed. Once this major point is resolved and the minor suggestions for improving clarity are incorporated, the paper will meet the high standards of the journal.