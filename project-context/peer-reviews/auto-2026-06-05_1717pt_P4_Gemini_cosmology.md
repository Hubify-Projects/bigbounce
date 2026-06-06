# P4 auto-2026-06-05_1717pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (5022 chars)
**Wall time**: 141.8s

---

Here is a complete referee report for the submitted paper.

***

## Referee Report for "Survey-Scale Galaxy Chirality with Equivariant TTA..."

This paper presents a search for a cosmological dipole in the chirality of spiral galaxies using a new catalog of 3.2 million spirals derived from 8.47 million DESI Legacy Survey images. The authors construct a deep-learning classifier (a Vision Transformer) and employ Test-Time Averaging (TTA) to enforce equivariance and mitigate systematic biases. The primary scientific result is a null detection of an l=1 dipole, reported as -0.122σ from a MASTER-deconvolved power spectrum analysis on a carefully selected subsample mask, and +0.43σ from a real-space dipole fit on the full catalog.

The paper also performs a detailed diagnostic analysis of a statistically significant (+3.64σ) l=1 residual found on a "canonical" survey mask. The authors present a comprehensive suite of systematic tests, ultimately attributing this residual to a combination of a small classifier monopole and the complex survey geometry (monopole-mask leakage), rather than a primordial signal. The analysis is exceptionally thorough, with a clear hierarchy of estimators, extensive bias-hardening tests for the classifier, and a robust framework for interpreting the results. The public release of the catalog, model, and analysis code is commendable.

The paper is well-written, the methodology is sound, and the conclusions are well-supported by the evidence presented. It represents a significant contribution to the field, providing both a new, large-scale dataset and a rigorous methodological blueprint for future searches of this kind. The work is suitable for publication in Physical Review D after addressing the following points.

---

### ESSENTIAL Revisions

**P4-E1**
*   **Section/Page:** Title Page / p. 1
*   **Problem:** The paper is dated "June 2026". This is a future date and must be an error.
*   **Fix:** Correct the date to the current submission date.

### MAJOR Revisions

**P4-M1**
*   **Section/Page:** IV. Results / Table III / p. 5
*   **Problem:** Table III, which presents the main angular power spectrum results, is missing a crucial column for the null-hypothesis mean power, `C_null`. The significance is defined as `(C_l - C_null) / σ_null`, but only `C_l` and `σ_null` are provided. While `C_null` is mentioned in the text on page 4 for the `l=1` single mode, it is not present in the table for any of the modes, making it impossible for the reader to verify the quoted significance values directly from the table.
*   **Fix:** Add a column for `C_null` to Table III for all listed modes and bandpowers. Ensure the values in the `Significance (σ)` column can be reproduced from the `C_l`, `C_null`, and `σ_null` columns.

### MINOR Revisions

**P4-m1**
*   **Section/Page:** Title Page / p. 1
*   **Problem:** The title is excessively long and reads more like a summary of the abstract. While descriptive, its length is unconventional for a journal article and reduces its impact.
*   **Fix:** Shorten the title to be more concise while still capturing the main contribution. A suggestion: "A Null Search for a Galaxy Chirality Dipole on 3.2 Million DESI Legacy Spirals with Equivariant TTA".

**P4-m2**
*   **Section/Page:** IV. B / Table II / p. 4
*   **Problem:** The `Dev. (σ)` column in Table II appears to have minor calculation inconsistencies. For Tier C, with `p = 0.4974` and `N = 3,201,160`, the binomial standard deviation is `σ_p = sqrt(p(1-p)/N) ≈ 0.000279`. The deviation from 0.5 is then `(0.4974 - 0.5) / 0.000279 ≈ -9.32σ`, not -9.5σ as reported. A similar small discrepancy exists for Tier A (calculation yields ~28.3σ vs. 28.8σ reported).
*   **Fix:** Please re-verify the calculations for the `Dev. (σ)` column. If the calculation is correct as stated, please clarify the source of the discrepancy (e.g., use of un-rounded numbers for `p`). If it is an error, correct the values in the table.

**P4-m3**
*   **Section/Page:** IV. D / Table IV / p. 5
*   **Problem:** The z-score for the `Pre-MASTER pseudo-C(l=1)` statistic appears to be miscalculated. Given Data = `1.696e-2` and Null = `(1.685 ± 0.007)e-2`, the z-score is `(1.696 - 1.685) / 0.007 = 1.57`. The table reports `z = +1.68`.
*   **Fix:** Please re-check this calculation and correct the value in the table.

**P4-m4**
*   **Section/Page:** Abstract / p. 1
*   **Problem:** The abstract mentions `n=5,547,858` for the MASTER analysis. While this is explained in the caption of Table I as `N_map_weighted`, it is potentially confusing in the abstract, as it does not correspond to the number of spiral galaxies.
*   **Fix:** Consider clarifying this in the abstract, for example: "...on the strict-superset subsample mask (effective weighted sample size n=5,547,858, f_sky = 0.659)...".

---

## Summary recommendation

**MAJOR REVISIONS**

The paper presents a high-quality, rigorous analysis that is well-suited for publication in Physical Review D. The scientific claims are robustly supported, and the methodological contributions are significant. The required revisions are primarily focused on improving clarity and correcting minor numerical inconsistencies in the tables to ensure the paper is fully transparent and reproducible. Once these issues are addressed, the paper will be a valuable addition to the literature.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the requested re-examination of the paper.

***

### Re-review with Fresh Eyes

A second, more detailed pass over the paper has revealed several additional issues requiring attention. The initial review correctly identified several key points, but a deeper dive into the arithmetic and internal consistency of the manuscript shows room for improvement in rigor and clarity. The new findings are detailed below.

---

### MAJOR Revisions

**P4-M2**
*   **Section/Page:** II. B. Training Labels / p. 2 & III. Methods / p. 3
*   **Problem:** There is a significant inconsistency in the reported numbers for the training set composition. Section II.B states the training labels are from three sources: (1) 6,637 from Galaxy Zoo 1, (2) 17,153 from CE-ResNet, and (3) 2,000 synthetic negatives. The sum of these components is 25,790. However, the text states, "The combined training set contains 26,636 images." This is a discrepancy of 846 images. Furthermore, the first paragraph of page 3 claims that "67.6% of training labels derive from CE-ResNet". Based on the provided numbers, this percentage is `17,153 / 26,636 = 64.4%` or `17,153 / 25,790 = 66.5%`. Neither calculation yields 67.6%. The precise composition of the training set is fundamental to the classifier's performance and potential biases. This discrepancy must be resolved.
*   **Fix:** Please verify and correct all numbers related to the training set composition. Ensure the sum of the components matches the stated total, and that all derived percentages are correct and reproducible from the numbers given in the text.

### MINOR Revisions

**P4-m5**
*   **Section/Page:** IV. B. Global CW Fraction / p. 4
*   **Problem:** The text claims a "3.86x asymmetry-suppression factor from raw +2.05% to equivariant -0.53%". These percentage values for raw and equivariant excess do not appear anywhere else in the manuscript. Table II, which summarizes these values, reports a raw excess of +0.79% (Tier A) and an equivariant excess of -0.26% (Tier C). The ratio of these values is `0.79 / 0.26 ≈ 3.0`. The numbers in the text appear to be stale values from a previous version of the analysis.
*   **Fix:** Correct the sentence to use the final, reported values from Table II, and update the calculated suppression factor accordingly.

**P4-m6**
*   **Section/Page:** Data Availability / p. 9
*   **Problem:** The description of the residual bias in the released catalog is ambiguous. It states: "The released catalog labels carry a measured spatially-uniform CW-bias residual of 0.26% (9.5σ)". However, Table II shows that for Catalog C, the CW fraction is 0.4974, which is a *deficit* of 0.26% relative to 0.5, and the significance is -9.5σ. Stating a "CW-bias residual of 0.26%" could be misinterpreted as an excess.
*   **Fix:** Clarify the text to remove ambiguity, for example: "...a CW-fraction of 0.4974, corresponding to a 0.26% deficit (-9.5σ)...".

**P4-m7**
*   **Section/Page:** I. Introduction / p. 2 & VI. B / p. 6
*   **Problem:** The paper claims that its null result disfavors the ~3% signal from Shamir et al. by a "factor of ~6-12". This factor seems overstated. The paper's empirical 50%-recovery-at-3σ sensitivity threshold is A=0.75%. Comparing a 3% signal to this threshold gives a factor of `3 / 0.75 = 4`. Comparing to the statistical-only Fisher floor of ~0.29% gives a factor of `3 / 0.29 ≈ 10.3`. The range 4-10 seems more appropriate and justifiable from the paper's own results.
*   **Fix:** Please either provide a clear justification for the 6-12 range or revise it to be more conservative and directly derivable from the sensitivity analysis presented (e.g., 4-10).

**P4-m8**
*   **Section/Page:** V. A. Shamir (2012, 2020, 2022) / p. 5
*   **Problem:** The text claims the current work is a "30x extension" of the methodological critique of Iye et al. (2021). Iye et al. re-examined Shamir's SDSS catalog, which contained ~1.28 x 10^5 spirals. The current catalog contains 3.2 x 10^6 spirals. The ratio is `3.2e6 / 1.28e5 = 25`. The "30x" figure is an overstatement.
*   **Fix:** Correct the extension factor to the more accurate value of 25x.

**P4-m9**
*   **Section/Page:** Appendix A.c / p. 7
*   **Problem (Suggestion for Clarity):** The appendix notes that for the canonical mask, monopole subtraction "increases σ from +1.85 to +3.64". This is a fascinating and important detail for understanding the nature of the +3.64σ systematic residual. It implies that the subtraction of the galaxy-weighted mean asymmetry reduces the variance of the null distribution more than it reduces the measured power. This point is somewhat buried in the appendix but is central to the paper's diagnostic argument.
*   **Fix (Suggestion):** Consider adding a brief sentence to the main text (e.g., in Section IV.D) to highlight and explain this effect. This would strengthen the main narrative by clarifying why the post-MASTER canonical-mask residual is so statistically significant while still being interpreted as a systematic.