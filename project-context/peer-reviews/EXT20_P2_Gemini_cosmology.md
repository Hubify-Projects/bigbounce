# P2 EXT20 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=dbcc5834 pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 192.6s

---

**Referee Report on "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook"**

**Manuscript ID:** [Assigned by editor]
**Author:** Houston Golden
**Journal:** Physical Review D

## General Comments

This manuscript presents a detailed sensitivity forecast for testing the matter-bounce cosmological scenario using upcoming data from the SPHEREx and proposed MegaMapper surveys. The primary observable is the local-type primordial non-Gaussianity parameter, `f_NL`, for which the quasi-dust matter bounce predicts a specific value of `f_NL = -35/8`. The work is structured as a "sensitivity recast," taking baseline forecast numbers from the literature (primarily Heinrich et al. 2024 for the SPHEREx bispectrum) and applying a series of carefully quantified corrections for effects specific to the matter-bounce template.

The paper's main contributions are:
1.  A thorough analysis of the template mismatch between the matter-bounce bispectrum and the standard local template, including a novel treatment of the underdetermination in the bounce bispectrum's polynomial coefficients.
2.  A definitive resolution of a factor-of-two discrepancy in the literature regarding the predicted `f_NL` value, which the author traces to a missing time-ordering in one calculation, firmly establishing `f_NL = -35/8` as the correct physical prediction in the Planck convention.
3.  A detailed systematic budget, translating the template mismatch and other uncertainties (e.g., from the PNG bias parameter `b_phi` and relativistic projections) into a realistic detection significance range for SPHEREx.
4.  A comprehensive Bayesian model comparison, quantifying the statistical power of SPHEREx to discriminate the matter bounce from inflationary alternatives.

The manuscript is exceptionally well-researched, methodologically rigorous, and transparent about its assumptions and limitations. The analyses of the polynomial null space, the in-in formalism in Appendix A, and the Bayesian framework are particularly strong. The author has taken great care to validate calculations, cross-check results, and explain subtle but important details (e.g., the possibility of `r > 1`, the different behavior of various `f_NL` estimators under systematic effects, and the precise bookkeeping for the Bayes factors).

Despite the high quality of the work, I have identified one major issue in a key summary table that requires correction, along with several minor points for improvement. I recommend publication in Physical Review D after these issues have been addressed.

## Summary Recommendation
**MAJOR REVISIONS**

The paper is a strong candidate for publication, but a significant error in the calculation of a key systematic effect in Table IV must be corrected. This table is central to the paper's headline significance forecast, and the error as it stands understates the impact of the `e-correction` uncertainty by an order of magnitude. Once this and other minor points are addressed, the paper will represent a valuable and robust contribution to the field.

---
## Detailed Findings

### ESSENTIAL Revisions

(None)

### MAJOR Revisions

**P2-M1: Incorrect effect size for e-correction in systematic budget**
*   **Section/Page:** Table IV, Page 20.
*   **Problem:** The row "e-correction" lists the effect on the detection significance as "`≤ 0.1σ effect`". This appears to be a significant miscalculation. The body of the paper (Sec. VIII.B, p. 21) correctly derives that the `e-correction` from the `n_s` consistency relation implies a theoretical range for the signal `f_NL ∈ [-4.35, -4.02]`. This is a range of width `0.33` around the central value of `-4.375`. The impact on the significance is a corresponding uncertainty or shift, which can be estimated as `|Δf_NL| * r / σ ≈ 0.33 * 0.84 / 0.7 ≈ 0.4σ`. This is substantially larger than the quoted `≤ 0.1σ`. The table's value understates this theoretical uncertainty, which is one of the core physical uncertainties of the model prediction.
*   **Required Fix:** The author must re-calculate the impact of the 0.6-8% uncertainty in `f_NL` on the detection significance and update the "e-correction" row in Table IV accordingly. The text should also be checked for consistency with the corrected value. The combination rule is listed as "add. quadrature (±δf_NL)", which implies an uncertainty on the numerator. The table should perhaps report this as a range on the final significance (e.g., `5.2-5.5σ` becomes `(5.2-5.5)±0.4σ` or similar), rather than a single number, and the text should clarify how this "distributional contribution" is to be interpreted in the context of the cumulative budget.

### MINOR Revisions

**P2-m1: Justification of polynomial coefficient basis**
*   **Section/Page:** Section II.A, Footnote 1, Page 3.
*   **Problem:** Footnote 1 provides a crucial justification for the choice of polynomial basis and the inability to directly transplant coefficients from Cai et al. [10]. However, it validates a key claim ("The resulting transformation matrix is full-rank (rank 6, verified numerically via `c9i_epsilon_ratio_check.json`)") by pointing to a code artifact. While the provision of code is commendable, the paper itself should be self-contained.
*   **Required Fix:** State the result of the verification explicitly in the footnote. For example, mention the singular values of the transformation matrix or other metrics that demonstrate its full-rank nature, without requiring the reader to run the associated code.

**P2-m2: Clarification of Bayes factor table structure**
*   **Section/Page:** Table II, Page 15.
*   **Problem:** Table II is structured in two parts: a 2x2 grid at the top and a different 5-row table at the bottom. While the extensive caption explains the relationship, the visual layout is confusing. The bottom table seems to be the primary result, with the top table being a subset or a different view.
*   **Required Fix:** Consider restructuring Table II for clarity. Perhaps merge them or present them as Table IIa and Table IIb with clearer titles. At a minimum, the title of the bottom table should be more descriptive than "Bounce prior choice". For example: "Bayes Factor Sensitivity to Bounce and Competitor Priors".

**P2-m3: Overly detailed table captions**
*   **Section/Page:** Table II (p. 15) and Table III (p. 18).
*   **Problem:** The captions for these tables are extremely long, containing detailed explanations, calculation steps, and cross-references that belong more properly in the main text or footnotes. While the detail is appreciated, it makes the tables difficult to parse quickly.
*   **Required Fix:** Shorten the captions to contain only information essential for interpreting the table itself. Move the detailed derivations, justifications, and discussions of how abstract numbers are derived to the main text body, and have the caption refer back to the relevant section.

**P2-m4: Scope of joint (f_NL, n_fNL) analysis**
*   **Section/Page:** Section IX.D, Page 22.
*   **Problem:** This section introduces a joint forecast using a scale-dependent bias (SDB) analysis, which is based on a different dataset subset and Fisher matrix than the paper's primary bispectrum forecast. The author does an excellent job of flagging this distinction to avoid confusion. However, the placement in the "Discussion" section and the framing as a "stronger discriminator" could still lead a reader to misinterpret it as a primary result.
*   **Required Fix:** To further reinforce the channel hierarchy, consider renaming the subsection from "Joint (f_NL, n_fNL) Forecast as a Stronger Discriminator" to something like "Complementary Constraints from Scale-Dependence of `f_NL`". This reframes it as an auxiliary check rather than a competing headline forecast.

### NITs (Cosmetic)

**P2-N1: Author email address**
*   **Section/Page:** Page 2.
*   **Problem:** The author's contact email, `houston@hubify.com`, appears to be a non-institutional, potentially commercial or temporary, address.
*   **Required Fix:** The author should consider providing a more permanent or academic contact address if one is available.

**P2-N2: Meta-commentary in text**
*   **Section/Page:** Section IX.D, Page 23.
*   **Problem:** The paragraph beginning "Channel hierarchy and sub-labeling note" is written as direct instruction to the reader on how to interpret the paper's structure. This is slightly unconventional for a formal research paper.
*   **Required Fix:** The information is useful, but it could be rephrased more organically into the surrounding text. For example, instead of "This subsection... reports the joint... analysis as a subordinate discriminator," one could write "The joint scale-dependent-bias analysis provides a subordinate, complementary discriminator to the primary bispectrum channel."