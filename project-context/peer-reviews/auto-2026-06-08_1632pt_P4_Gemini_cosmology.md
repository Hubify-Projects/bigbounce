# P4 auto-2026-06-08_1632pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (3379 chars)
**Wall time**: 129.5s

---

**Referee Report for Physical Review D**

**Manuscript Title:** Survey-Scale Galaxy Chirality with Equivariant TTA: A -0.122σ Subsample-Mask l=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)
**Author:** Houston Golden

This paper presents a detailed analysis of galaxy chirality using 3.2 million spiral galaxies from the DESI Legacy Surveys. The primary scientific result is a null detection of a cosmological dipole (l=1) in the chirality asymmetry map, with a headline significance of -0.122σ on a carefully chosen subsample. The authors identify and quantify a significant systematic effect—a "monopole-mask leakage channel"—where a small, uniform classifier bias (a monopole) couples with the patchy survey geometry to create a spurious, large-scale dipole-like feature in naive analyses. A +3.64σ residual on a "canonical mask" is investigated thoroughly and attributed to this and other survey systematics, not a cosmological signal.

The analysis is comprehensive, employing modern machine learning techniques (Vision Transformer), careful bias mitigation (Test-Time Averaging), and a sophisticated statistical analysis using the MASTER algorithm. The authors are commendably transparent about potential systematics, their analysis hierarchy, and the limitations of their data and methods. The distinction between the parity-even dipole observable and true parity-violating physics is correctly and clearly maintained.

While the scientific approach is sound and the conclusions are likely robust, the manuscript in its current form contains several issues ranging from minor typos to significant methodological ambiguities and signs of being an incomplete work. These must be addressed before the paper can be considered for publication in Physical Review D.

---

### ESSENTIAL Revisions

**P4-E1: Incomplete/Draft-State Language**
*   **Location:** Page 4, Section IV.D and Footnote 1.
*   **Problem:** The manuscript contains language that indicates it is a work-in-progress, which is unacceptable for a peer-reviewed submission.
    *   Page 4, Sec IV.D: "The canonical-mask direct-MC l=1 value of +3.64σ and the local hemisphere maximum of 3.05σ were interpreted in earlier paper versions as mask-geometric leakage..."
    *   Page 4, Footnote 1: "The previous wording ... was ambiguous... A parallel rerun on N(p)all-trial draws is in queue for the canonical-mask sensitivity-budget recompute."
*   **Required Fix:** All references to "earlier paper versions," "previous wording," or work that is "in queue" must be removed. The paper must present a complete, self-contained, and final analysis. If the "in queue" analysis is critical, the paper should not have been submitted until it was complete. If it is not critical, the sentence should be removed.

**P4-E2: Inconsistent Column in Summary Table**
*   **Location:** Page 4, Table I.
*   **Problem:** The column header is "σ", implying all values are significances in standard deviations. However, two rows contain values that are not sigmas:
    *   (iv) hemisphere LEE (MC): "p_LEE ≤ 10⁻⁴" is a p-value.
    *   (vi) injection floor: "50%-rec-3σ at A=0.75%" is a sensitivity limit description.
*   **Required Fix:** The column must be consistent. Either rename the column to something more general like "Result" or convert all entries to a consistent metric (e.g., convert the p-value to an equivalent sigma). The sensitivity limit should be moved to the caption or a separate column, as it is not a measurement.

---

### MAJOR Revisions

**P4-M1: Ambiguity/Error in Training Loss Function**
*   **Location:** Page 7, Appendix B, Equation (B1).
*   **Problem:** The flip-equivariance consistency loss term is given as `L = L_CE + λ * (1/N) * Σ ||p(x_i) - S p(x_i)||^2`, where `S` is the permutation matrix swapping CW and CCW channels. As written, this loss term simplifies to `2λ * (p_cw - p_ccw)^2` for each galaxy, which would train the classifier to be maximally uncertain (`p_cw = p_ccw`) for all inputs. This cannot be correct. The standard formulation for such a loss compares the prediction on a transformed input to the transformed prediction on the original input, i.e., `||p(flip(x_i)) - S p(x_i)||^2`.
*   **Required Fix:** The authors must clarify this crucial methodological point. If the equation is a typo and the standard formulation was used, the equation and its description must be corrected. If the equation as written was actually used, the authors must provide a strong justification for this highly unconventional choice and demonstrate that it achieves the desired effect without destroying the classifier's performance.

**P4-M2: Confusing Presentation of the +3.64σ Residual**
*   **Location:** Abstract (Page 1), Conclusions (Page 6), and throughout the text.
*   **Problem:** The paper frequently leads with the "+3.64σ" value for the canonical-mask residual, only to immediately qualify it as a non-Gaussian, systematics-attributed signal with an empirical rank p-value corresponding to ~1.9σ. This presentation is confusing and potentially misleading, as it highlights a large sigma value that the authors' own analysis invalidates as a meaningful detection significance.
*   **Required Fix:** Rephrase the presentation to avoid ambiguity. For example, state clearly that the residual shows a +3.64σ deviation from the mean of a simple permutation null, but that this null is inappropriate. Then state that a more robust analysis of its empirical rank yields a p-value of 0.030, corresponding to a ~1.9σ fluctuation, and that further tests confirm its systematic origin. The abstract and conclusions should reflect this more nuanced and accurate summary.

**P4-M3: Sign Error in Table II**
*   **Location:** Page 4, Table II.
*   **Problem:** For Catalog C (equivariant), the CW fraction is 0.4974, which is less than 0.5. The "Excess (%)" is correctly given as -0.26. However, the "Dev. (σ)" is given as 9.5 (a positive number). My calculation `(0.4974 - 0.5) / 0.000279` yields approximately -9.3σ. The sign is missing.
*   **Required Fix:** Correct the "Dev. (σ)" value for Catalog C to be negative, e.g., -9.5σ, to be consistent with the CW fraction and excess.

---

### MINOR Revisions

**P4-m1: Overly-long Title**
*   **Location:** Page 1, Title.
*   **Problem:** The title is excessively long and detailed, functioning more as a summary sentence than a title.
*   **Required Fix:** Shorten the title to be more concise while still capturing the main result. For example: "A Null Search for a Cosmological Chirality Dipole in 3.2 Million DESI Legacy Spiral Galaxies".

**P4-m2: Future Date on Manuscript**
*   **Location:** Page 1, Date.
*   **Problem:** The manuscript is dated "June 2026".
*   **Required Fix:** Correct the date to the submission date.

**P4-m3: Clarification of Exclusion Factor**
*   **Location:** Page 6, Section VI.B.
*   **Problem:** The text states that the null result disfavors the Shamir ~3% amplitude class "by a factor of ~6-12". The origin of this range is not immediately obvious from the stated sensitivity of 0.75%.
*   **Required Fix:** Briefly explain how this factor is derived. For example, by comparing the 3% amplitude to the 2σ or 3σ upper limit derivable from the paper's sensitivity analysis.

---

## Summary recommendation
**MAJOR REVISIONS**

The paper represents a substantial and high-quality analysis that, once revised, will be a valuable contribution to the literature. The authors' careful treatment of systematics is a model for this type of work. However, the presence of language indicating an unfinished analysis, a critical ambiguity in the description of the machine learning methodology, and several inconsistencies in the presentation of key results currently prevent the manuscript from meeting the publication standards of Physical Review D. I recommend that the paper be reconsidered after major revisions that address the points listed above.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from a more rigorous re-examination of the paper.

---
### NEW FINDINGS (Second Pass)

**P4-N1: Incomplete and Unverifiable Power Spectrum Table**
*   **Location:** Page 5, Table III.
*   **Problem:** This crucial table, which presents the angular power spectrum results, is incomplete and cannot be independently verified. The "Significance (σ)" column is calculated as `(C_l - mean(C_null)) / std(C_null)`. The table provides `C_l` and a column labeled `σ_null` (which is presumably `std(C_null)`), but it omits the essential `mean(C_null)` column. Without the mean of the null distribution for each bandpower, the significance values are unsubstantiated. An attempt to back-calculate the null mean from the other columns for the `l_eff=4` bandpower yields a negative (and therefore unphysical) value, suggesting a more fundamental error in the table's construction or labeling.
*   **Required Fix:** Add a column for `mean(C_null)` to Table III and ensure that all values are consistent, such that the significance can be re-calculated as `(C_l - mean(C_null)) / σ_null`.

**P4-N2: Inconsistent/Stale Numbers for Asymmetry Suppression**
*   **Location:** Page 4, Section IV.B.
*   **Problem:** The text makes a specific quantitative claim: "The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant -0.53% demonstrates the dominance of the equivariant TTA processing." However, Table II on the same page reports different values: a raw excess of +0.79% (for Catalog A) and an equivariant excess of -0.26% (for Catalog C). These two sets of numbers are mutually exclusive. This strongly suggests that one set is a stale value from a previous version of the analysis that was not updated, undermining confidence in the paper's internal consistency.
*   **Required Fix:** Reconcile the numbers in the text with those in Table II. The correct, final values must be used in both places, and the derived suppression factor must be updated accordingly.

**P4-N3: Arithmetic Error in Monopole-Leakage Table**
*   **Location:** Page 5, Table IV.
*   **Problem:** The z-score for the "Pre-MASTER pseudo-C(l=1)" statistic is reported as `z = +1.68`. However, recalculating from the provided data and null values gives `z = (1.696 - 1.685) / 0.007 = 0.011 / 0.007 ≈ 1.57`. This is a clear arithmetic error. While the difference is not large enough to change the qualitative conclusion, such errors are not acceptable in a final publication.
*   **Required Fix:** Correct the z-score in Table IV to the accurately calculated value.

**P4-N4: Unclear Terminology in Sensitivity Calculation**
*   **Location:** Page 6, Section VI.A.
*   **Problem:** The text derives the "Fisher Poisson floor at 3σ" as `~0.29%` starting from a value `σ(A/2) ≈ 0.048%`. This implies that the floor is on a "full amplitude" `A`, which is twice the dipole coefficient whose uncertainty is given. This use of `A/2` is non-standard and potentially confusing. A dipole's amplitude is typically defined directly from its spherical harmonic coefficients, and the relationship should be stated explicitly.
*   **Required Fix:** Clarify the definition of the dipole amplitude being constrained. For example, define the asymmetry map as `a(n) = A_dip * cos(θ)` and state whether the reported sensitivity `A` refers to `A_dip`. Avoid ambiguous intermediate terms like `A/2`.