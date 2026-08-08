# P2 R39conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/paper2_fnl_forecast.pdf` md5=406af9f8 pages=27
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 167.7s

---

## Referee Report: P2-R39conf

**Manuscript:** "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook"
**Author:** Houston Golden
**Journal:** Physical Review D

This paper presents a detailed sensitivity forecast for testing the matter-bounce cosmological scenario using upcoming large-scale structure surveys, primarily SPHEREx. The author recasts existing forecasts for local-type non-Gaussianity to the specific bispectrum shape predicted by the matter bounce, accounting for the template mismatch. The work includes a comprehensive analysis of systematic uncertainties, a Bayesian model comparison against inflationary alternatives, and a valuable clarification of a factor-of-two discrepancy in the literature regarding the predicted value of f_NL.

The paper is well-structured, the analysis is thorough, and the claims are generally well-supported by detailed calculations. The transparency regarding the scope (a recast, not a from-scratch forecast) and the limitations of certain calculations (e.g., heuristic checks, simplified systematic modeling) is commendable. The resolution of the Cai et al. vs. Li et al. discrepancy via the in-in formalism in Appendix A is a significant contribution in its own right.

However, there is one essential issue regarding the clarity and derivation of a headline result that must be addressed before the paper can be accepted. Several minor points are also noted.

---
### Detailed Findings

#### ESSENTIAL

*   **ID:** P2-E1
*   **Location:** Abstract (page 1) and multiple locations in the body (e.g., Sec. IV, page 10; Fig. 2 caption, page 10).
*   **Problem:** The paper repeatedly quotes a "realistic" detection significance range of `~2.6-5σ` for SPHEREx. The lower bound of `~2.6σ` is clearly and robustly derived in Table IV as the most pessimistic scenario, combining all considered systematics. However, the upper bound of `~5σ` is not clearly defined or derived from a "realistic" scenario. This value is very close to the *optimistic* baseline of 5.2-5.5σ, which by definition includes no systematic degradations. A "realistic" range should be bracketed by scenarios that both include some level of systematic treatment. Juxtaposing the most pessimistic number with a near-optimistic one is confusing and potentially misleading. The reader cannot determine what set of assumptions leads to the 5σ figure.
*   **Required Fix:** The author must explicitly define the physical scenario and assumptions that produce the `~5σ` upper end of the "realistic" range. This scenario should be included in the systematic budget analysis (e.g., in Table IV). If a robustly defined "realistic" scenario yielding `~5σ` cannot be produced, the range must be revised to one that is transparently derived from the paper's own analysis (e.g., `~2.6-4.3σ`, which would span the fully-degraded case to the `σ_GR=0.5` case). This clarification is essential for the integrity of the paper's primary quantitative conclusion.

#### MINOR

*   **ID:** P2-M1
*   **Location:** Abstract, page 1.
*   **Problem:** The abstract states: "a curvaton-natural [−5, +5] competitor narrows this to BF ≈ 4–7." The body text in Section VI, page 13, gives the corresponding numbers as "BF ~ 4 (theory = 1.0) and BF ~ 7 (delta)". While the numbers match, the abstract phrasing could be slightly clearer by specifying that the range corresponds to the two different bounce priors (recommended Gaussian vs. delta-prior maximum), not a range of uncertainty for a single scenario.
*   **Required Fix:** Consider rephrasing the abstract slightly for clarity, for example: "...a curvaton-natural [−5, +5] competitor gives Bayes factors from BF ≈ 4 (for the recommended bounce prior) to BF ≈ 7 (at the theoretical maximum)."

#### NIT (Nitpick/Cosmetic)

*   **ID:** P2-N1
*   **Location:** Data and Code Availability, page 23.
*   **Problem:** The text includes the placeholder `(DOI inserted at submission)`.
*   **Required Fix:** Ensure this placeholder is replaced with the actual Zenodo DOI upon acceptance, before final publication. This is standard procedure but worth noting.

---
### Audit of Figures and Tables

*   **Table I (page 5):** Correctly confirms benchmark values from the literature.
*   **Figure 1 (page 5):** Clearly illustrates the shape function and its squeezed-limit convergence. Consistent with Table I.
*   **Figure 2 (page 10):** Provides a useful summary of the detection significance across different scenarios. The labeling is clear. The figure's "realistic" bar reflects the `2.6-5σ` range flagged in P2-E1.
*   **Figure 3 (page 11):** A simple but effective visualization of the `f_NL` landscape, supporting the paper's core argument.
*   **Table II (page 14):** The table on Bayes factors is well-documented with extensive footnotes that clarify the origin of the numbers and the impact of different priors. All calculations re-computed from the text and formulas appear correct.
*   **Figure 4 (page 15):** Effectively demonstrates the different sensitivity of the SDB and bispectrum channels to the minimum accessible scale `k_min`.
*   **Figure 5 (page 16):** Effectively demonstrates the different sensitivity of the SDB and bispectrum channels to the `b_φ` prior.
*   **Table III (page 17):** Clearly shows the robustness of the Bayesian preference for the bounce model against parameterized GR contamination. Calculations appear correct.
*   **Table IV (page 19):** This is an excellent, transparent table that breaks down the systematic budget. All calculations were verified and found to be correct. It is the basis for the ESSENTIAL finding P2-E1, as it makes the origin of the 2.6σ clear but does not provide a corresponding origin for the 5σ.
*   **Figure 6 (page 21):** A helpful summary of the observational decision thresholds.
*   **Table V (page 27):** A clear and concise summary of the impact of the single- vs. full-time-ordering issue. Calculations are correct and highlight the importance of the Appendix A analysis.

---
## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, rigorous, and valuable paper that will be of significant interest to the cosmology community. Its careful recast of the matter-bounce sensitivity, detailed systematic analysis, and especially its definitive resolution of a key factor-of-two discrepancy in the literature are all strong contributions. The paper meets the high standards of Physical Review D in almost all respects.

The recommendation for "Major Revisions" is based solely on the ESSENTIAL finding (P2-E1) regarding the ambiguity of the headline `~2.6-5σ` realistic significance range. The primary result of a paper must be unambiguously defined and derived. Once this central point is clarified and the manuscript is revised accordingly, the paper should be suitable for publication. The author has already performed the necessary calculations in Table IV; the issue is one of presentation and definition of the "realistic" envelope. I expect that the author can address this straightforwardly.