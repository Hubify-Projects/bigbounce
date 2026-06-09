# P4 R-v166-c1 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (3483 chars)
**Wall time**: 162.2s

---

## Referee Report: P4

**Paper ID:** P4
**Title:** Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)
**Journal:** Physical Review D

This paper presents a large-scale analysis of galaxy chirality using 3.2 million spiral galaxies from the DESI Legacy Surveys. The primary methodological contribution is the use of equivariant Test-Time Averaging (TTA) to produce a bias-hardened catalog. The main scientific results are a null detection of a real-space chirality dipole and a template-based exclusion of a specific dipole model. The paper also provides a detailed investigation of systematic effects, identifying a "monopole-mask leakage" channel that can produce spurious dipole-like signals, and presents a thorough analysis of a residual signal that is attributed to systematics.

The analysis is comprehensive and the methodological rigor, particularly regarding systematic controls and the transparent handling of a withdrawn result from a prior version, is commendable. The paper sets a high standard for future work in this area. However, several issues related to data presentation and numerical consistency must be addressed before the paper can be accepted for publication.

### Findings

#### ESSENTIAL

*   **P4-E1 | Section IV A, Figure 3 | Page 6**
    *   **Problem:** The pie chart in Figure 3, titled "Catalog C composition," displays galaxy counts and percentages that are inconsistent with the values for Catalog C provided in the text (Section IV A, page 5).
        *   Figure 3 shows: CW = 1,687,069 (19.9%), CCW = 1,634,726 (19.3%), Not-Spiral = 5,152,736 (60.8%).
        *   Text on page 5 states for Catalog C: CW = 1,592,107 (18.78%), CCW = 1,609,053 (18.99%), NS/edge-on = 5,273,371 (62.23%).
    *   **Required Fix:** The figure must be regenerated with the correct data for Catalog C to match the text, or the caption must be corrected to specify which catalog (e.g., Catalog A) the figure represents. This is a critical data presentation error that could confuse the reader about the final catalog's properties.

#### MAJOR

*   **P4-M1 | Section IV B, Table II | Page 5**
    *   **Problem:** The "Dev. (σ)" column in Table II for Catalog C is listed as `9.5`. However, a direct calculation using the provided values `cw/(cw + ccw) = 0.4974` and `σ = 0.000279` yields `(0.4974 - 0.5) / 0.000279 ≈ -9.32`. The sign of the deviation is incorrect in the table. The text on page 5 ("The Catalog C residual (9.5σ from 0.5000, Table II)...") and page 13 ("...measured spatially-uniform CW-bias residual of 0.26% (9.5σ)...") propagates this error.
    *   **Required Fix:** Correct the value in Table II to `-9.5`. The corresponding text in the paper must also be corrected to reflect the negative sign of the deviation. If the absolute value is intended, the column header should be changed to `|Dev.| (σ)` and this should be applied consistently. Given the other entries are signed, a signed value is the expected and more informative convention.

#### MINOR

*   **P4-m1 | Section IV D, Table IV | Page 8**
    *   **Problem:** There is a numerical discrepancy in the z-score for the "Pre-MASTER pseudo-C<sup>(l=1)</sup>" statistic. Using the provided Data (1.696 × 10<sup>-2</sup>) and Null mean and standard deviation (1.685 ± 0.007) × 10<sup>-2</sup>, the z-score is calculated as `(1.696 - 1.685) / 0.007 ≈ 1.57`. The table reports `z = +1.68`. This ~7% difference should be resolved.
    *   **Required Fix:** Please re-calculate the z-score and correct the value in Table IV. The authors should also briefly clarify whether the quoted uncertainty on the null is the standard deviation of the null distribution or the standard error on the mean of the N=500 realizations, as this affects the interpretation of the z-score.

*   **P4-m2 | Abstract | Page 1**
    *   **Problem:** The sentence structure "...8.47M sources, 471049 high-confidence per-spiral after p<sub>eq</sub> > 0.9" is slightly ambiguous. The qualifier "per-spiral" seems to apply to the 471,049 count, but its placement is awkward.
    *   **Required Fix:** Rephrase for clarity. For example: "...(from 8.47M total sources), including 471,049 high-confidence spirals with p<sub>eq</sub> > 0.9)."

*   **P4-m3 | Abstract | Page 1**
    *   **Problem:** The sentence "the canonical-mask residual is interpretation (ii) systematic, not a primordial detection" is grammatically awkward.
    *   **Required Fix:** Rephrase for better readability. For example: "the canonical-mask residual is interpreted as a systematic effect (interpretation (ii)), not as a primordial detection."

#### NIT

*   **P4-N1 | Title | Page 1**
    *   **Problem:** The title is exceptionally long and dense with technical terms.
    *   **Required Fix:** This is a suggestion for the authors' consideration. While descriptive, a more streamlined title might improve accessibility. This is not a required change.

*   **P4-N2 | Abstract | Page 1**
    *   **Problem:** The use of "z ≈ -18" to denote a significance level is a niche convention that may be misinterpreted as a redshift by some readers in the cosmology community.
    *   **Required Fix:** While likely acceptable, consider adding a brief parenthetical clarification, e.g., "(an 18σ exclusion significance)", or using more standard phrasing to avoid potential confusion.

*   **P4-N3 | Throughout**
    *   **Problem:** The notation for the pseudo-angular power spectrum varies between "pseudo-C<sub>e</sub>" and "pseudo-C<sub>l</sub>".
    *   **Required Fix:** Please use a consistent notation throughout the manuscript. "pseudo-C<sub>l</sub>" is more standard.

## Summary recommendation
**MAJOR REVISIONS**

The paper presents a high-quality, rigorous analysis that represents a significant step forward for galaxy chirality studies. The methodological innovations for bias mitigation and the depth of the systematic analysis are particular strengths. The transparent retraction of a previously reported result is a model of scientific integrity.

However, the paper is currently marred by a few significant errors in data presentation, including a figure (Fig. 3) and a key table (Table II) that contain values inconsistent with the main text. These errors must be corrected before the paper can be considered for publication. Once these and the other minor issues are addressed, the paper will be a very strong and valuable contribution to the literature.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the report on the second, more rigorous review of the paper.

================================================================
### Additional Findings from "Fresh Eyes" Review

Following the initial review, a more detailed check was performed, focusing on numerical consistency, cross-references, and the substantiation of claims, as per the journal's standards for rigor. This second pass revealed several new issues that require attention.

#### MAJOR

*   **P4-M2 | Section IV, Appendix D | Page 7**
    *   **Problem:** The summary of the systematic analysis on page 7 (and mentioned in the abstract) lists three key pieces of evidence disfavoring a real cosmological dipole. One of these is "(b) p<sub>eq</sub> quality-quartile washout (all four quartiles |σ| < 1)". This is presented as a crucial discriminator. However, the details of this "quality-quartile" analysis are not presented anywhere in the paper, including in Appendix D, which is supposed to contain the full systematic analysis. This constitutes an unsupported claim.
    *   **Required Fix:** The authors must add the full details of this analysis to Appendix D or another appropriate section. This should include the definition of the quartiles, the number of galaxies in each, the measured dipole significance, and the null procedure used. Without this, the claim must be removed from the abstract and the main text.

*   **P4-M3 | Section IV, Table III | Page 7**
    *   **Problem:** The "Significance (σ)" column in Table III is not verifiable from the other data presented in the table. A direct calculation of `C_l / σ_null` does not match the reported significance. For example, for `l_eff=4`, the calculation is `3.210 / 0.804 ≈ 3.99`, whereas the table reports `+6.097`. As confirmed by a calculation in the main text for the `l=1` mode, this is because the significance is calculated as `(C_l - mean(C_l,null)) / std(C_l,null)`, but the `mean(C_l,null)` is not provided in the table. This makes the table misleading and its primary results impossible to independently verify.
    *   **Required Fix:** The table must be reformatted to be self-contained and verifiable. The authors should add a column for the mean of the null distribution (`<C_l>_null`) for each bandpower. This will allow the reader to confirm the significance calculation and correctly interpret the results.

#### MINOR

*   **P4-m4 | Section IV B, Table II | Page 5**
    *   **Problem:** There is a small arithmetic inconsistency in the "Dev. (σ)" column for Catalog A. Using the provided values, the deviation is `(0.5079 - 0.5) / 0.000279 ≈ 28.32`. The table reports `28.8`. While the other rows are consistent within rounding, this value is off by ~2%.
    *   **Required Fix:** Please re-calculate and correct the "Dev. (σ)" value for Catalog A in Table II.

*   **P4-m5 | Section IV D, Figure 8 | Page 9**
    *   **Problem:** The caption for Figure 8 contains an incorrect internal cross-reference. It states that the post-MASTER residual of `+3.64σ` is from "(Table IV)". This value is not in Table IV; it is listed in Table I, row (iii).
    *   **Required Fix:** Correct the reference in the Figure 8 caption to point to Table I.

*   **P4-m6 | Appendix E, Footnote 2 | Page 13**
    *   **Problem:** Footnote 2 contains a typographical error in a cross-reference. It refers to "Sec. D", which is ambiguous.
    *   **Required Fix:** Please correct the reference to the full, standard format, e.g., "Sec. IV D".