# P4 auto-2026-06-06_0021pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (4931 chars)
**Wall time**: 153.4s

---

Here is a complete referee report for the submitted manuscript.

***

## Referee Report: "Survey-Scale Galaxy Chirality with Equivariant TTA..."

**Manuscript ID:** P4
**Journal:** Physical Review D

This paper presents a detailed analysis of galaxy chirality using a large dataset of 3.2 million spiral galaxies from the DESI Legacy Surveys. The authors construct a new catalog using a Vision Transformer classifier and perform a multi-estimator search for a cosmological dipole signal. The headline result is a null detection of the l=1 dipole, consistent with statistical isotropy. The authors also identify and quantify a significant systematic effect—monopole-mask leakage—which they argue can explain previous reports of positive detections in the literature. A +3.64σ residual on a specific "canonical mask" is investigated in detail and convincingly attributed to survey-related systematics rather than a primordial signal.

The scientific analysis is exceptionally thorough, employing a hierarchy of estimators, multiple null tests, and a comprehensive suite of systematic checks. The distinction between the parity-even dipole and parity-odd monopole/even-l modes is correctly handled, a critical point often overlooked in this field. The work represents a significant contribution to the search for violations of statistical isotropy.

However, the manuscript in its current form contains numerous numerical inconsistencies, unclear presentations, and placeholder artifacts that must be addressed before it can meet the publication standards of Physical Review D. The required revisions are substantial.

### Summary of Findings

**ESSENTIAL (Must be fixed for acceptance)**

*   **P4-E1 (Sec II.B, p. 2):** The total number of training images is stated as 26,636. However, the sum of the listed sources (6,637 from GZ1 + 17,153 from CE-ResNet + 2,000 synthetic) is 25,790. This discrepancy of 846 images must be resolved.
*   **P4-E2 (Table II, p. 4):** The "Dev. (σ)" column contains values inconsistent with a standard binomial error calculation.
    *   For Tier C, `(0.4974 - 0.5) / 0.000279 = -9.32σ`, not 9.5σ as reported.
    *   For Tier A, `(0.5079 - 0.5) / 0.000279 = 28.32σ`, not 28.8σ.
    *   For Tier B, `(0.504 - 0.5) / 0.000279 = 14.34σ`, not 14.6σ.
    The calculation or the reported values must be corrected. The text on p. 4 ("9.5σ from 0.5000") propagates this error.
*   **P4-E3 (Sec IV.B, p. 4):** The text states: "The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant -0.53%". These percentage values do not match the "Excess (%)" column in Table II (+0.79% for raw, -0.26% for equivariant). The text and table must be made consistent.
*   **P4-E4 (Table I, p. 4):** The column header is "σ", but the content is inconsistent.
    *   Row (iv) reports a p-value (`P_LEE ≤ 10^-4`), not a significance in units of σ. This should be converted to a sigma value for consistency or the column header must be changed.
    *   Row (vi) reports a sensitivity threshold ("50%-rec-3σ at A=0.75%"), which is not a measurement. This does not belong in a column of measured significances. The table structure needs to be revised for clarity.
*   **P4-E5 (Table III, p. 5):** The column header `C_null × 10^6 (sr)` is highly misleading. The text on p. 4 indicates that for l=1, the null mean is `1.546e-6` and the standard deviation is `0.429e-6`. The table reports `0.429` in this column, which is clearly the standard deviation (`σ_null`), not the mean (`C_null`). The table must be corrected to include columns for both the mean of the null simulations and their standard deviation, or the header must be explicitly changed to `σ_null`. This ambiguity makes the reported significances for `leff > 1` impossible to verify.
*   **P4-E6 (Multiple Locations):** The manuscript contains future dates, which are unacceptable for publication.
    *   (Abstract, p. 1): "(Dated: June 2026)"
    *   (Data Availability, p. 9): "Release tag: v2026.04"
    These must be replaced with the correct submission/release dates.
*   **P4-E7 (Sec III.A, p. 3):** The notation for the real-space dipole is inconsistent. The text states `Adipole = 0.43`, while the abstract and Table I report `+0.43σ`. The text must be clarified to state that 0.43 is the significance in units of σ, not the dimensionless amplitude of the dipole itself.

**MAJOR (Significant revision required)**

*   **P4-M1 (Sec VI.B, p. 6):** The paper claims the null result disfavors the "Shamir ~3% amplitude class by a factor of ~6–12". This factor is not derived clearly. The paper's empirical 3σ sensitivity is 0.75%. A simple ratio `3% / 0.75%` gives a factor of 4. The text must provide an explicit calculation to justify the claimed factor of 6–12. This likely involves comparing the 3% amplitude to the 1σ sensitivity, but this must be stated.
*   **P4-M2 (Title, p. 1):** The title is excessively long and reads like an abstract. While descriptive, it is unwieldy and lacks the conciseness expected for a major journal. The authors should shorten it to focus on the main finding, e.g., "A Null Search for a Galaxy Chirality Dipole on 3.2 Million DESI Legacy Spirals and a Quantified Monopole-Mask Systematic".
*   **P4-M3 (Abstract, p. 1):** The presentation of the +3.64σ residual is confusing. The text reports this high sigma value but immediately qualifies it as "≈1.9σ Gaussian-equivalent" based on its empirical p-value. This suggests the null distribution is highly non-Gaussian. For clarity and to avoid misinterpretation, the abstract should lead with the more robust p-value or Gaussian-equivalent significance, and explain that the simple moment-ratio `Δ/σ_null` is inflated.

**MINOR (Address but paper can proceed)**

*   **P4-m1 (Table IV, p. 5):** The z-score for the "Pre-MASTER pseudo-C(l=1)" statistic is calculated as `(1.696 - 1.685) / 0.007 = 1.57`. The table reports `+1.68`. This minor discrepancy should be checked and corrected.
*   **P4-m2 (Sec II.B, p. 3):** The paper correctly notes that 67.6% of its training labels come from CE-ResNet, limiting its independence. While this is stated, the authors could briefly comment in the Discussion on how this might affect the results, e.g., by inheriting similar selection biases, even if the architectures differ.
*   **P4-m3 (Sec IV.B, p. 4):** The text states the global CW fraction monopole is a "classifier artifact". While this is the most likely explanation, it is a strong claim. It would be more precise to state that it is a non-cosmological signal attributed to a combination of training set bias and classifier properties.

**NIT (Cosmetic)**

*   **P4-N1 (Abstract, p. 1):** The phrase "high-confidence per-spiral after p_cw > 0.9" is slightly awkward. Suggest rephrasing to "high-confidence spirals (p_cw > 0.9)".
*   **P4-N2 (Sec I, p. 2):** The text states "Shamir (2020) [1] and Shamir (2022) [3] reported results with ~ 2-4% asymmetries". For clarity, specify if this is a per-bin or all-sky asymmetry amplitude.

***

## Summary recommendation

**MAJOR REVISIONS**

The paper presents a high-quality, rigorous analysis that is a valuable contribution to the field. The authors' careful work to identify and model systematic effects is commendable and provides a template for future studies. The primary scientific conclusion—a null result for the chirality dipole—is well-supported by multiple lines of evidence. However, the manuscript is currently compromised by several essential numerical errors and inconsistencies in key tables and text. These errors must be rectified, as they undermine the reader's confidence in the otherwise excellent analysis. Once these corrections are made, along with improvements to clarity and presentation as detailed above, the paper will be suitable for publication in Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated referee report, incorporating the new findings from the second, more rigorous review.

***

## Referee Report: "Survey-Scale Galaxy Chirality with Equivariant TTA..." (Second Pass)

**Manuscript ID:** P4
**Journal:** Physical Review D

This second review of the manuscript was conducted with a specific focus on numerical consistency, cross-referencing, and the integrity of the claims connecting the abstract, main body, and appendices. While the initial review praised the overall thoroughness of the analysis, this deeper examination has uncovered several additional essential and major issues that were previously missed. These new findings reinforce the initial recommendation for **MAJOR REVISIONS**. The manuscript contains critical errors in its presentation of key results that must be corrected.

The new findings are listed below. They should be addressed in addition to all points raised in the initial review.

### Summary of New Findings (Not in Initial Report)

**ESSENTIAL (Must be fixed for acceptance)**

*   **P4-E8 (Sec III.B, p. 3):** The stated percentage of training labels derived from CE-ResNet (67.6%) is numerically inconsistent with the provided counts of training images. Given 17,153 CE-ResNet labels and a total of 25,790 (or 26,636) images, the percentage should be ~66.5% (or ~64.4%). This discrepancy, related to P4-E1, must be resolved.
*   **P4-E9 (Data Availability, p. 9):** The text reports a "CW-bias residual of 0.26% (9.5σ)". This is incorrect in two ways. First, based on Table II (Tier C, `fcw = 0.4974`), the excess is `0.4974 - 0.5 = -0.0026`, or **-0.26%**. The sign is wrong. Second, it repeats the likely erroneous 9.5σ value from Table II (see P4-E2), which should be -9.32σ. The final summary of the catalog's properties must be accurate.

**MAJOR (Significant revision required)**

*   **P4-M4 (Table III, p. 5):** The angular power spectrum results in Table III are incomplete and unverifiable. The table is missing a crucial column for the mean of the null simulations (`C_null_mean`) for each bandpower. The significance is defined as `(C_obs - C_null_mean) / σ_null`, but without `C_null_mean`, the results for `leff > 1` cannot be checked. A non-zero `C_null_mean` is expected from noise bias in any pseudo-C_l analysis. This column must be added to the table for the results to be scientifically valid and reproducible.
*   **P4-M5 (Sec VII.c, p. 6):** The conclusion contains a critical error that conflates two of the paper's main results. It states that MASTER deconvolution "independently collapses the pseudo-Ce to the canonical -0.122σ null." This is false. The **-0.122σ** result is for the **subsample mask**, which is the primary scientific null result. The result on the **canonical mask** is the **+3.64σ** systematic residual. The conclusion must be rewritten to accurately distinguish between these two separate findings.

**MINOR (Address but paper can proceed)**

*   **P4-m4 (Table I, p. 4):** The `Nmap weighted` column, described in the caption as a weight used for the NaMaster analysis, is inexplicably blank for the canonical mask estimators (rows iii, iv, v). Since row (iii) is a MASTER analysis, this value should be present. Please clarify or fill in the missing information.
*   **P4-m5 (Sec IV.D, p. 4):** The text refers to the "global 9.5σ monopole". As the global CW fraction is less than 0.5 (Table II), this is a monopole *deficit*. For clarity, the sign should be included (e.g., a -9.5σ monopole deficit), and the underlying numerical error (see P4-E2) should be corrected.
*   **P4-m6 (Appendix D.b, p. 8):** The significance of the l=1 mode on the canonical mask is reported here as `σ_l=1=+3.63`. This is slightly different from the `+3.64σ` value used consistently in the abstract and main text. This minor numerical inconsistency should be resolved for clarity.

**NIT (Cosmetic)**

*   **P4-N3 (Sec V.A, p. 5):** The text claims a "30x extension" in sample size. This factor appears to be calculated relative to a 2012 paper by Shamir. To avoid ambiguity, the specific work being used as the baseline for this comparison should be explicitly cited in the same sentence.

***

## Summary recommendation

**MAJOR REVISIONS**

This second, more detailed review confirms the initial assessment: the paper represents a methodologically strong and scientifically valuable contribution. However, it is currently undermined by a significant number of numerical errors, inconsistencies, and unclear presentations. The newly discovered errors, particularly the conflation of key results in the main conclusion (P4-M5) and the incomplete power spectrum table (P4-M4), are critical and must be addressed. The authors are urged to perform a thorough internal audit of all reported numbers and claims before resubmission. Once these comprehensive corrections are made, the manuscript will be a strong candidate for publication.