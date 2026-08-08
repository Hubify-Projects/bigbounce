# P2 D2 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=4667e9e2 pages=28
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (8599 chars)
**Wall time**: 199.4s

---

**Referee Report on "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook"**

**Manuscript ID:** [Not provided, using placeholder]
**Journal:** Physical Review D

## Summary

This manuscript presents a comprehensive and timely forecast for testing the matter bounce cosmological scenario using upcoming measurements of primordial non-Gaussianity (PNG) from the SPHEREx survey. The work is divided into three main parts: (1) a critical audit of the theoretical prediction for local-type non-Gaussianity (`f_NL = -35/8`) in the matter bounce model, which convincingly resolves a factor-of-two discrepancy in the literature; (2) a detailed sensitivity recast of SPHEREx forecasts, quantifying the impact of template mismatch and a wide range of systematic effects; and (3) a robust Bayesian model comparison to assess the discriminating power between the bounce scenario and inflationary alternatives.

The paper is exceptionally thorough, methodologically sound, and transparent about its assumptions and limitations. The audit of the theoretical prediction is a valuable contribution in its own right. The forecast is one of the most detailed to date for this specific model, with a careful treatment of systematics that leads to a realistic and well-motivated sensitivity range. The Bayesian analysis is sophisticated and validated with multiple cross-checks.

The manuscript is well-written and clearly structured. Its conclusions are well-supported by the detailed calculations presented. The work is of high quality and represents a significant contribution to the field. It is well-suited for publication in Physical Review D after addressing one essential correction and a few minor points.

## Recommendation

**MAJOR REVISIONS**

The recommendation for Major Revisions is based on a single but essential correction required for a key equation in the paper. Once this and other minor points are addressed, the manuscript should be suitable for publication.

---

## Detailed Findings

### ESSENTIAL

*   **P2-E1: Sign error in core prediction equation**
    *   **Section/Page:** Sec. II A, p. 3, Eq. (2)
    *   **Problem:** Equation (2) describes the squeezed limit of the nonlinearity parameter `B_NL` and states that it approaches `35/8`. This is inconsistent with the main claim of the paper, which is a *negative* non-Gaussianity `f_NL = -35/8`. The text throughout the paper (e.g., "large, negative... non-Gaussianity" on p. 2), the benchmark values in Table I (p. 5), and the plot in Figure 1 (p. 5) all correctly use a negative value. The positive sign in Eq. (2) is a significant error in the presentation of the model's core prediction.
    *   **Fix:** The arrow in Equation (2) must be corrected to `→ -35/8` to be consistent with the rest of the manuscript and the cited literature.

### MAJOR

*(No findings classified as MAJOR.)*

### MINOR

*   **P2-M1: Float placement of key systematic budget table**
    *   **Section/Page:** Table IV appears on p. 20, but is first referenced in the abstract (p. 1) and Sec. IV (p. 10).
    *   **Problem:** Table IV, the "Consolidated Systematic Budget," is arguably the most important table for understanding the paper's headline significance range of `2.6-5σ`. Its placement on page 20, far from its first substantive discussion on page 10 and its summary on page 18, disrupts the flow of the argument. A reader following the derivation of the main result must jump ahead 10 pages to see the breakdown.
    *   **Fix:** Move Table IV to appear closer to its first main discussion, for example, on page 18 where Section VIII.E ("Consolidated Systematic Budget") begins.

*   **P2-M2: Unconventional dating of the manuscript and references**
    *   **Section/Page:** Throughout, e.g., paper date (p. 1), references [18], [32], [35].
    *   **Problem:** The manuscript is dated "June 19, 2026," and several citations refer to future years and arXiv preprints from 2025 and 2026. While this is a consistent stylistic choice, it is highly unconventional for a research paper and may cause confusion for readers regarding the timeliness of the work and the status of the cited preprints.
    *   **Fix:** It is strongly recommended to re-date the manuscript to the actual submission date and update the publication years of the cited works to reflect their preprint dates (e.g., "arXiv:2311.13082 (2023)"). This would align the paper with standard academic practice.

*   **P2-M3: Explicit definition of `B_NL` vs. `f_NL`**
    *   **Section/Page:** Sec. II A, p. 3.
    *   **Problem:** The manuscript uses both `B_NL` (in Eq. 2) and `f_NL` (in the text) to refer to the local non-Gaussianity parameter. While the relationship is standard for experts (`B_local = (6/5)f_NL^local`), its omission can cause confusion, especially given the sign issue in Eq. (2). The abstract introduces the standard local template normalization `B^local(k_1,k_2,k_3) = (6f_NL^local/5)[...]`, but this connection is not reiterated in the main text where `B_NL` first appears.
    *   **Fix:** Add a brief sentence in Sec. II A explicitly stating the relationship between the shape function `B_NL` being calculated and the standard parameter `f_NL` that is being constrained, for instance by referencing the local-template normalization given in the abstract.

### NIT (Nitpicks)

*   **P2-N1: Clarification on `r` uncertainty sources**
    *   **Section/Page:** Abstract (p. 1) and Sec. II/III (p. 4, 8).
    *   **Problem:** The paper introduces two different uncertainties on the template mismatch factor `r`: a `±0.13` scatter from the polynomial null space (p. 4) and a `±0.02` range from different observational noise-weighting schemes (p. 8). The abstract mentions both sources but could be slightly clearer in distinguishing them.
    *   **Fix:** The paper does a good job of distinguishing these in the main text (e.g., footnote 2 on p. 5). No change is strictly required, but the authors might consider a minor rephrasing in the abstract to make the distinction between "polynomial coefficient uncertainty" and "noise-weighting scheme uncertainty" even more explicit for the casual reader. The current text is acceptable as is.

---

## Final Assessment

This is an excellent paper that performs a valuable service to the cosmology community by both clarifying a key theoretical prediction and providing a robust, detailed forecast for testing it. The analysis is rigorous and the presentation is exceptionally clear and honest about its limitations. The essential correction is straightforward to implement. I look forward to seeing this work published.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated referee report, incorporating the findings from the "fresh eyes" review.

================================================================
**Referee Report on "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook"**

**Manuscript ID:** [Not provided, using placeholder]
**Journal:** Physical Review D

## Summary

This manuscript presents a comprehensive and timely forecast for testing the matter bounce cosmological scenario using upcoming measurements of primordial non-Gaussianity (PNG) from the SPHEREx survey. The work is divided into three main parts: (1) a critical audit of the theoretical prediction for local-type non-Gaussianity (`f_NL = -35/8`) in the matter bounce model, which convincingly resolves a factor-of-two discrepancy in the literature; (2) a detailed sensitivity recast of SPHEREx forecasts, quantifying the impact of template mismatch and a wide range of systematic effects; and (3) a robust Bayesian model comparison to assess the discriminating power between the bounce scenario and inflationary alternatives.

The paper is exceptionally thorough, methodologically sound, and transparent about its assumptions and limitations. The audit of the theoretical prediction is a valuable contribution in its own right. The forecast is one of the most detailed to date for this specific model, with a careful treatment of systematics that leads to a realistic and well-motivated sensitivity range. The Bayesian analysis is sophisticated and validated with multiple cross-checks.

The manuscript is well-written and clearly structured. Its conclusions are well-supported by the detailed calculations presented. The work is of high quality and represents a significant contribution to the field. It is well-suited for publication in Physical Review D after addressing the required corrections.

## Recommendation

**MAJOR REVISIONS**

The recommendation for Major Revisions is based on an essential correction required for a core prediction equation and a significant error in a key figure. Once these and other minor points are addressed, the manuscript should be suitable for publication.

---

## Initial Review Findings

*   **P2-E1: Sign error in core prediction equation**
    *   **Section/Page:** Sec. II A, p. 3, Eq. (2)
    *   **Problem:** Equation (2) describes the squeezed limit of the nonlinearity parameter `B_NL` and states that it approaches `35/8`. This is inconsistent with the main claim of the paper, which is a *negative* non-Gaussianity `f_NL = -35/8`. The text throughout the paper (e.g., "large, negative... non-Gaussianity" on p. 2), the benchmark values in Table I (p. 5), and the plot in Figure 1 (p. 5) all correctly use a negative value. The positive sign in Eq. (2) is a significant error in the presentation of the model's core prediction.
    *   **Fix:** The arrow in Equation (2) must be corrected to `→ -35/8` to be consistent with the rest of the manuscript and the cited literature.

*   **P2-M1: Float placement of key systematic budget table**
    *   **Section/Page:** Table IV appears on p. 20, but is first referenced in the abstract (p. 1) and Sec. IV (p. 10).
    *   **Problem:** Table IV, the "Consolidated Systematic Budget," is arguably the most important table for understanding the paper's headline significance range of `2.6-5σ`. Its placement on page 20, far from its first substantive discussion on page 10 and its summary on page 18, disrupts the flow of the argument. A reader following the derivation of the main result must jump ahead 10 pages to see the breakdown.
    *   **Fix:** Move Table IV to appear closer to its first main discussion, for example, on page 18 where Section VIII.E ("Consolidated Systematic Budget") begins.

*   **P2-M2: Unconventional dating of the manuscript and references**
    *   **Section/Page:** Throughout, e.g., paper date (p. 1), references [18], [32], [35].
    *   **Problem:** The manuscript is dated "June 19, 2026," and several citations refer to future years and arXiv preprints from 2025 and 2026. While this is a consistent stylistic choice, it is highly unconventional for a research paper and may cause confusion for readers regarding the timeliness of the work and the status of the cited preprints.
    *   **Fix:** It is strongly recommended to re-date the manuscript to the actual submission date and update the publication years of the cited works to reflect their preprint dates (e.g., "arXiv:2311.13082 (2023)"). This would align the paper with standard academic practice.

*   **P2-M3: Explicit definition of `B_NL` vs. `f_NL`**
    *   **Section/Page:** Sec. II A, p. 3.
    *   **Problem:** The manuscript uses both `B_NL` (in Eq. 2) and `f_NL` (in the text) to refer to the local non-Gaussianity parameter. While the relationship is standard for experts (`B_local = (6/5)f_NL^local`), its omission can cause confusion, especially given the sign issue in Eq. (2). The abstract introduces the standard local template normalization `B^local(k_1,k_2,k_3) = (6f_NL^local/5)[...]`, but this connection is not reiterated in the main text where `B_NL` first appears.
    *   **Fix:** Add a brief sentence in Sec. II A explicitly stating the relationship between the shape function `B_NL` being calculated and the standard parameter `f_NL` that is being constrained, for instance by referencing the local-template normalization given in the abstract.

*   **P2-N1: Clarification on `r` uncertainty sources**
    *   **Section/Page:** Abstract (p. 1) and Sec. II/III (p. 4, 8).
    *   **Problem:** The paper introduces two different uncertainties on the template mismatch factor `r`: a `±0.13` scatter from the polynomial null space (p. 4) and a `±0.02` range from different observational noise-weighting schemes (p. 8). The abstract mentions both sources but could be slightly clearer in distinguishing them.
    *   **Fix:** The paper does a good job of distinguishing these in the main text (e.g., footnote 2 on p. 5). No change is strictly required, but the authors might consider a minor rephrasing in the abstract to make the distinction between "polynomial coefficient uncertainty" and "noise-weighting scheme uncertainty" even more explicit for the casual reader. The current text is acceptable as is.

---

## Additional Findings from Rigorous Re-review

A second, more detailed pass of the manuscript was conducted to check for issues commonly missed in an initial review, such as arithmetic consistency, internal cross-references, and figure-text agreement. This process confirmed the exceptional quantitative rigor of the paper—all numerical claims in the abstract and tables were successfully re-derived from the provided inputs. However, it also revealed the following new issues:

### MAJOR

*   **P2-M4: Figure 5 is misleading regarding a key systematic**
    *   **Section/Page:** Figure 5, p. 17.
    *   **Problem:** In both panels of Figure 5, the red dashed line representing the SPHEREx bispectrum constraint is plotted as perfectly flat, indicating it is independent of the PNG bias (`b_φ`) uncertainty. This directly contradicts the figure caption and the main text (Sec. VII.B, p. 16), which correctly state that the constraint is not independent and degrades by O(20-50%) when `b_φ` universality is relaxed. The plot thus visually misrepresents the robustness of the paper's primary channel to a key systematic.
    *   **Fix:** The red dashed lines in Figure 5 must be redrawn to reflect the degradation described in the text. For example, in the left panel, `σ(f_NL)` should rise from 0.7 at a 20% prior to ~0.9-1.05 at higher uncertainties. The right panel should show the corresponding drop in significance.

### MINOR

*   **P2-m5: Incorrect internal cross-reference**
    *   **Section/Page:** Sec. IV, p. 9.
    *   **Problem:** In the discussion of DBI inflation, the text defers a discussion of the "joint (f_NL, n_fNL) subsection" to §VI. However, the relevant joint forecast is actually presented in §IX.D (p. 21). This is a minor navigational error for the reader.
    *   **Fix:** Change the cross-reference from §VI to §IX.D.

---

## Final Assessment

This is an excellent paper that performs a valuable service to the cosmology community by both clarifying a key theoretical prediction and providing a robust, detailed forecast for testing it. The analysis is rigorous and the presentation is exceptionally clear and honest about its limitations. The required corrections are straightforward to implement. I look forward to seeing this work published.