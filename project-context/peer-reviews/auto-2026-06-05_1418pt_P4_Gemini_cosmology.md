# P4 auto-2026-06-05_1418pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (4192 chars)
**Wall time**: 130.8s

---

**Referee Report: PRD Manuscript [P4]**

**Title:** Survey-Scale Galaxy Chirality with Equivariant TTA: A -0.122σ Subsample-Mask l=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)

This paper presents a new, large-scale analysis of galaxy chirality using 3.2 million spiral galaxies from the DESI Legacy Surveys. The primary scientific result is a null detection of a cosmological dipole in the spin-handedness of these galaxies. The authors perform a rigorous and multi-faceted analysis, with a particular focus on identifying and mitigating systematic effects. They convincingly demonstrate that a previously reported class of dipole signal can be explained by a leakage of a global monopole (a small, uniform bias in classification) into the dipole mode via the survey mask geometry. The analysis is thorough, employing modern machine learning techniques, equivariant averaging to reduce bias, and a comprehensive suite of null tests and systematic checks.

The methodology is sound and the conclusions are, for the most part, well-supported by the presented evidence. The paper represents a significant contribution to the field. However, several issues must be addressed before the manuscript can be considered for publication in Physical Review D.

---

### ESSENTIAL Revisions

**P4-E1 | General | Page 1**
*   **Problem:** The paper is dated "June 2026". This is a placeholder and is unacceptable for a submitted manuscript.
*   **Fix:** The date must be corrected to the current submission date.

### MAJOR Revisions

**P4-M1 | Methods / Data | Page 3, Sec. III (Note)**
*   **Problem:** The text states: "Note: 67.6% of training labels derive from CE-ResNet predictions". This is a critical detail that significantly impacts the interpretation of the work's independence. The classifier is predominantly learning to reproduce the labels from the model in Jia et al. [7], rather than learning from independent, human-labeled ground truth. This is currently understated in a "Note".
*   **Fix:** This limitation must be discussed more prominently. It should be mentioned in the abstract and expanded upon in the main body (e.g., Introduction and/or Discussion). The paper should be framed more explicitly as an extension and systematic-hardening of a methodology trained on pre-existing machine-generated labels, rather than a fully independent measurement from first principles.

**P4-M2 | Results / Table II | Page 4, Sec. IV.B**
*   **Problem:** In Table II, for Catalog C (equivariant), the `Excess (%)` is `-0.26` but the `Dev. (σ)` is given as `9.5`. A negative excess must correspond to a negative deviation. A recalculation `(0.4974 - 0.5) / 0.000279` yields approximately `-9.3σ`. The value in the table has both a sign error and a magnitude discrepancy. The text in Sec. IV.B also refers to this as a "9.5σ" residual, which is misleading.
*   **Fix:** Correct the sign and value of the deviation for Catalog C in Table II to `~-9.3`. Update the text in Sec. IV.B and anywhere else this value is quoted to reflect the correct sign and value (e.g., "a -9.3σ monopole residual").

**P4-M3 | Results / Table III | Page 5**
*   **Problem:** The `Significance (σ)` values for the bandpowers (rows 2-7, `leff=4` and higher) are not reproducible from the information provided in the table. The table provides `C_ell` and `C_null` (presumably the mean of the null simulations), but not the standard deviation of the null (`σ_null`) required to compute the significance via `(C_ell - <C_ell>_null) / σ_null`.
*   **Fix:** Add a column to Table III for `σ_null` for each bandpower, so that the reported significance values can be independently verified. Alternatively, clarify precisely how the significance is calculated from the given columns.

### MINOR Revisions

**P4-m1 | Abstract | Page 1**
*   **Problem:** The phrasing "a -0.122σ Subsample-Mask l=1 Null" is slightly awkward.
*   **Fix:** Suggest rephrasing for clarity, for example: "A null result for the l=1 dipole on a subsample mask (-0.122σ)".

**P4-m2 | Abstract | Page 1**
*   **Problem:** The abstract states the analysis was performed on a "subsample mask (n=5,547,858, fsky = 0.659)". This number `n` refers to the total weighted galaxy count on the map (including non-spirals), not the number of spirals (3.2M). This could be confusing to the reader.
*   **Fix:** Clarify this in the abstract. For example: "...on a survey-depth-weighted map constructed from 3.2M spirals (total weighted source count n=5.5M)..." or similar phrasing.

**P4-m3 | Formatting | Pages 1-2**
*   **Problem:** The text of the Introduction (Section I) is split, with the second half appearing at the top of page 2 before Section II begins.
*   **Fix:** Consolidate the Introduction onto page 1 or ensure the section break is logical.

### NITPICKS (Cosmetic)

**P4-N1 | Table III | Page 5**
*   **Problem:** The column header `C_null` is ambiguous. It likely refers to the mean of the null simulations, `<C_ell>_null`.
*   **Fix:** For clarity, consider renaming the column header to `<C_ell>_null` or `mean(C_null)`.

**P4-N2 | Table I | Page 4**
*   **Problem:** The significance for estimator (iv) `hemisphere LEE (MC)` is given as `PLEE ≤ 10^-4`. This is a p-value, not a sigma value. While acceptable, it is inconsistent with the other rows which report `σ`.
*   **Fix:** Consider converting this to an approximate Gaussian-equivalent sigma for consistency, or add a note clarifying that it is a p-value.

---

## Summary recommendation
**MAJOR REVISIONS**

The paper presents a high-quality, rigorous analysis that is a valuable contribution to the literature on cosmological parity and isotropy. The authors' careful treatment of systematics is commendable and provides a strong null result for the galaxy chirality dipole. The framework for identifying and nulling the monopole-mask leakage channel is particularly compelling.

However, the manuscript requires major revisions before it can be accepted. The reliance on another machine-learning model for the majority of the training data is a significant caveat that must be addressed with greater prominence. Furthermore, a critical table contains a sign error in a key result (Table II), and another (Table III) is missing the information required to reproduce the stated significances. These issues, along with the essential correction of the manuscript date, must be resolved. Once these revisions are made, the paper should be suitable for publication in Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from the second, more rigorous review.

---
### ADDITIONAL FINDINGS

**P4-M4 | Abstract / Results | Page 1, Sec. VII**
*   **Problem:** There is a significant inconsistency in the reported significance of the canonical-mask residual. The abstract, Table I, and other sections report this as `+3.64σ`. However, the abstract also states that the empirical rank p-value from 500 Monte Carlo simulations is `pmc = 0.030`, which corresponds to a one-sided Gaussian-equivalent significance of only `~1.9σ`. The main text (Sec. VII.b) confirms `pmc = 15/500 = 0.030`. The `+3.64σ` value appears to be derived from a "moment-ratio" (analytic variance estimate), which is in strong tension with the more robust, non-parametric empirical rank. It is misleading to headline the much larger significance value when the direct empirical test shows it to be far less significant.
*   **Fix:** The authors must resolve this discrepancy. They should either justify why the moment-ratio significance is more appropriate than the empirical one, or (preferably) revise the abstract and main text to consistently use the more conservative and empirically-grounded `~1.9σ` (from p=0.03) significance for this secondary, systematics-attributed result.

**P4-M5 | Abstract / Discussion | Page 1, Sec. VI.A**
*   **Problem:** The falsification criterion is stated inconsistently. The abstract proposes that "A future survey detecting a chirality dipole at σ>5 with full amplitude ≥ 0.75% ... would falsify the present null." However, the main text in Sec. VI.A and Sec. VII.d derives this `A ≈ 0.75%` value as the "empirical 50%-recovery-at-3σ threshold". A 3σ threshold for detection does not imply that a 5σ detection is required for falsification.
*   **Fix:** The falsification criterion in the abstract must be made consistent with the analysis in the body of the paper. A `σ>3` detection at this amplitude would already be in significant tension with the null result. The abstract should be corrected to state `σ>3` or the authors must justify the higher `σ>5` bar.

**P4-M6 | Data Availability | Page 9**
*   **Problem:** The description of the final data product in the "Data Availability" section contains a critical sign error. It states: "The released catalog labels carry a measured spatially-uniform CW-bias residual of 0.26% (9.5σ)". According to Table II, the equivariant Catalog C has `fcw = 0.4974`, which is an excess of counter-clockwise (CCW) galaxies. This corresponds to a residual of `-0.26%`, not `+0.26%`. This error misrepresents the nature of the small residual bias in the final public catalog. This sentence also repeats the incorrect `9.5σ` value.
*   **Fix:** Correct the sign of the residual bias to `-0.26%` and the significance to `~-9.3σ` in this section to accurately describe the released data.

**P4-m4 | Results / Table II | Page 4**
*   **Problem:** The `Dev. (σ)` values for Catalog A and Catalog B in Table II appear to have minor arithmetic errors.
    *   For Catalog A, `(0.5079 - 0.5) / 0.000279 ≈ 28.3σ`, not 28.8σ.
    *   For Catalog B, `(0.504 - 0.5) / 0.000279 ≈ 14.3σ`, not 14.6σ.
*   **Fix:** Recompute and correct these values in Table II.

**P4-m5 | Introduction | Page 2, Sec. I**
*   **Problem:** The text claims the measured null result is "inconsistent in amplitude with Shamir's claimed ~3% signal by a factor of ~ 6-12". This factor is not justified by the numbers presented. The paper's 3σ sensitivity limit is `A ≈ 0.75%`. Comparing this to a 3% signal gives a factor of `3 / 0.75 = 4`.
*   **Fix:** The authors should either provide the calculation that leads to a factor of 6-12 or revise the text to state the more straightforward factor of ~4.

**P4-N3 | Abstract | Page 1**
*   **Problem:** The abstract contains a minor cross-referencing error. It attributes the analysis of the `+3.64σ` residual and the cross-spectrum result to "Sec. IV D". While the monopole leakage concept is in Sec. IV D, the detailed systematic analysis and the cross-spectrum result (`r=-0.65`) are located in Appendix D.
*   **Fix:** Correct the cross-reference in the abstract to point to Appendix D for the detailed systematic analysis.