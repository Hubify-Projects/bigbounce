# P4 R10v3p1 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (9928 chars)
**Wall time**: 143.2s

---

## Referee Report on "Survey-Scale Galaxy Chirality with Equivariant TTA..."

This paper presents a detailed analysis of galaxy chirality using a large dataset of 3.2 million spiral galaxies from the DESI Legacy Surveys. The authors construct a new, bias-hardened catalog and use it to search for a cosmological dipole in the spin-handedness of galaxies. The headline result is a null detection of the `l=1` dipole, consistent with statistical isotropy. The paper also performs a detailed diagnostic analysis of a statistically significant residual found on a specific survey mask, convincingly arguing that it is a systematic artifact arising from the interplay between a small classifier monopole and the survey geometry, rather than a cosmological signal.

The methodology is rigorous and state-of-the-art, employing a Vision Transformer classifier, test-time equivariant averaging to suppress biases, and a formal power spectrum analysis using the MASTER algorithm. The authors are commendably careful in their analysis, declaring an estimator hierarchy, performing an extensive suite of null and systematic tests, and clearly distinguishing between parity-even (isotropy-breaking) and parity-odd (parity-violating) observables. The public release of the catalog, model, and analysis scripts is a significant contribution to the field and sets a high standard for reproducibility.

The paper is well-written and the conclusions are well-supported by the presented evidence. However, several revisions are required to improve clarity, correct minor numerical inconsistencies, and strengthen key arguments before the paper can be considered for publication in Physical Review D.

---

### Findings

#### ESSENTIAL

**P4-E1 | Abstract, p. 1 | Incorrect Table Reference**
*   **Problem:** The abstract states: "see Table II for the mapping of each result to its null." Table II details the global CW fraction across different catalog tiers. The correct table that maps the headline estimators to their respective nulls is Table I.
*   **Fix:** Change the reference from "Table II" to "Table I" in the abstract.

#### MAJOR

**P4-M1 | Section VI.B, p. 6 | Unclear Exclusion Claim**
*   **Problem:** The text claims the present null result disfavors "the Shamir ~3% amplitude class by a factor of ~6-12." The paper establishes a 3σ detection threshold at a dipole amplitude of A ≈ 0.75%. A 3% signal is 4 times this 3σ threshold (3 / 0.75 = 4), not 6-12 times. This phrasing is confusing. The exclusion should be stated in terms of the statistical significance at which a 3% signal is ruled out, or as an upper limit on the amplitude compared to the 3% claim.
*   **Fix:** Rephrase this sentence to provide a clear, statistically grounded exclusion. For example, state the upper limit on the dipole amplitude from the present analysis and compare it to the 3% claim, or calculate the sigma-level at which a 3% signal would have been detected and is therefore ruled out.

**P4-M2 | Table II, p. 4 | Inconsistent Deviation Calculation**
*   **Problem:** The "Dev. (σ)" column in Table II appears to contain minor but consistent calculation errors. For Catalog C, the deviation for `p=0.4974` with `N=3,201,160` and `σ_bin=0.000279` is `(0.4974 - 0.5) / 0.000279 = -9.32σ`, not -9.5σ as reported. Similar small discrepancies exist for Catalogs A (28.3σ vs. 28.8σ) and B (14.3σ vs. 14.6σ). For a precision cosmology paper, these values must be exact.
*   **Fix:** Recompute and correct all values in the "Dev. (σ)" column of Table II. If a non-standard formula was used, it must be stated and justified.

**P4-M3 | Section VI.A, p. 6 | Undefined Dilution Factor**
*   **Problem:** The text mentions a "GZ1-dilution factor ~0.63" used to relate the empirical detection threshold to an underlying "true" threshold. The origin of this 0.63 value is not explained or cited. Simple calculations based on the quoted GZ1 cross-match accuracy (69.91%) or the binary CW/CCW accuracy (93.2%) do not yield this number.
*   **Fix:** Provide a clear derivation or a specific citation for the "GZ1-dilution factor ~0.63".

#### MINOR

**P4-m1 | Abstract, p. 1 | Ambiguous Sample Size**
*   **Problem:** The abstract mentions the headline result comes from a mask with "n=5,547,858". This number is significantly larger than the 3.2 million spirals and could be confusing to the reader. While Table I clarifies this is a weighted count of all galaxies used for depth estimation, the abstract would benefit from this clarification.
*   **Fix:** Briefly clarify in the abstract that `n=5,547,858` is a survey-depth-weighted galaxy count, not the number of spiral galaxies in the analysis. For example: "...on the strict-superset subsample mask (using a depth map from n=5,547,858 total galaxies, fsky = 0.659)..."

**P4-m2 | Table I, p. 4 | Inconsistent Estimator Reporting**
*   **Problem:** In Table I, estimators (i), (ii), (iii), and (v) report a significance in units of σ. Estimator (iv), "hemisphere LEE (MC)", reports a p-value (`p_LEE ≤ 10^-4`). This is inconsistent. The text and Appendix C clarify that the pre-LEE significance is 3.05σ. For consistency and clarity, the table should report this pre-correction sigma value.
*   **Fix:** Change the entry for estimator (iv) in Table I to report the pre-LEE significance of +3.05σ. A footnote can be added to direct the reader to Appendix C for the discussion of the look-elsewhere effect correction.

**P4-m3 | Section IV.B, p. 4 | Mismatch with Corrected Table II Value**
*   **Problem:** The text states "The Catalog C residual (9.5σ from 0.5000, Table II)". This value is based on the likely incorrect value in Table II (see finding P4-M2).
*   **Fix:** Update this value to match the corrected calculation for Table II (which should be 9.32σ).

**P4-m4 | Page 1, Date | Future Date**
*   **Problem:** The paper is dated "June 2026". This is presumably a placeholder.
*   **Fix:** Update the date to the current submission date.

#### NIT

**P4-N1 | Appendix D, p. 8 | Typo in WLS fit result**
*   **Problem:** The text describing the WLS fit states: "the interpretation (i) reference amplitude 1.7% at z = -264.5 from the naive WLS posterior". The `z` here appears to be a z-score or significance, not a redshift. Using the symbol `z` is potentially confusing in a cosmology context.
*   **Fix:** Replace `z` with `σ` or "z-score" to avoid ambiguity with redshift. For example: "...with a significance of σ = -264.5...".

---

## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, methodologically robust paper that presents an important null result for the cosmic dipole in galaxy chirality. The analysis is thorough, and the authors' careful treatment of systematics is exemplary. The paper is a strong candidate for publication in Physical Review D. However, the identified issues, particularly the numerical inconsistencies in a key table and the unclear justification for the claimed exclusion of previous results, must be addressed. Once these major and minor points are corrected, the paper will meet the high standards of the journal.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated review, incorporating the new findings from the second, more rigorous pass.

================================================================
## Referee Report on "Survey-Scale Galaxy Chirality with Equivariant TTA..."

This paper presents a detailed analysis of galaxy chirality using a large dataset of 3.2 million spiral galaxies from the DESI Legacy Surveys. The authors construct a new, bias-hardened catalog and use it to search for a cosmological dipole in the spin-handedness of galaxies. The headline result is a null detection of the `l=1` dipole, consistent with statistical isotropy. The paper also performs a detailed diagnostic analysis of a statistically significant residual found on a specific survey mask, convincingly arguing that it is a systematic artifact arising from the interplay between a small classifier monopole and the survey geometry, rather than a cosmological signal.

The methodology is rigorous and state-of-the-art, employing a Vision Transformer classifier, test-time equivariant averaging to suppress biases, and a formal power spectrum analysis using the MASTER algorithm. The authors are commendably careful in their analysis, declaring an estimator hierarchy, performing an extensive suite of null and systematic tests, and clearly distinguishing between parity-even (isotropy-breaking) and parity-odd (parity-violating) observables. The public release of the catalog, model, and analysis scripts is a significant contribution to the field and sets a high standard for reproducibility.

The paper is well-written and the conclusions are well-supported by the presented evidence. However, several revisions are required to improve clarity, correct minor numerical inconsistencies, and strengthen key arguments before the paper can be considered for publication in Physical Review D.

---

### Findings

#### ESSENTIAL

**P4-E1 | Abstract, p. 1 | Incorrect Table Reference**
*   **Problem:** The abstract states: "see Table II for the mapping of each result to its null." Table II details the global CW fraction across different catalog tiers. The correct table that maps the headline estimators to their respective nulls is Table I.
*   **Fix:** Change the reference from "Table II" to "Table I" in the abstract.

#### MAJOR

**P4-M1 | Section VI.B, p. 6 | Unclear Exclusion Claim**
*   **Problem:** The text claims the present null result disfavors "the Shamir ~3% amplitude class by a factor of ~6-12." The paper establishes a 3σ detection threshold at a dipole amplitude of A ≈ 0.75%. A 3% signal is 4 times this 3σ threshold (3 / 0.75 = 4), not 6-12 times. This phrasing is confusing. The exclusion should be stated in terms of the statistical significance at which a 3% signal is ruled out, or as an upper limit on the amplitude compared to the 3% claim.
*   **Fix:** Rephrase this sentence to provide a clear, statistically grounded exclusion. For example, state the upper limit on the dipole amplitude from the present analysis and compare it to the 3% claim, or calculate the sigma-level at which a 3% signal would have been detected and is therefore ruled out.

**P4-M2 | Table II, p. 4 | Inconsistent Deviation Calculation**
*   **Problem:** The "Dev. (σ)" column in Table II appears to contain minor but consistent calculation errors. For Catalog C, the deviation for `p=0.4974` with `N=3,201,160` and `σ_bin=0.000279` is `(0.4974 - 0.5) / 0.000279 = -9.32σ`, not -9.5σ as reported. Similar small discrepancies exist for Catalogs A (28.3σ vs. 28.8σ) and B (14.3σ vs. 14.6σ). For a precision cosmology paper, these values must be exact.
*   **Fix:** Recompute and correct all values in the "Dev. (σ)" column of Table II. If a non-standard formula was used, it must be stated and justified.

**P4-M3 | Section VI.A, p. 6 | Undefined Dilution Factor**
*   **Problem:** The text mentions a "GZ1-dilution factor ~0.63" used to relate the empirical detection threshold to an underlying "true" threshold. The origin of this 0.63 value is not explained or cited. Simple calculations based on the quoted GZ1 cross-match accuracy (69.91%) or the binary CW/CCW accuracy (93.2%) do not yield this number.
*   **Fix:** Provide a clear derivation or a specific citation for the "GZ1-dilution factor ~0.63".

**P4-M4 | Table III, p. 5 | Missing Uncertainty Column**
*   **Problem:** The significance values for the bandpowers in Table III cannot be verified because the uncertainty on the null power spectrum, `σ(C_l^null)`, is not provided. This information is essential for reproducibility and for understanding the results.
*   **Fix:** Add a column to Table III for `σ_null` for each bandpower, allowing independent verification of the "Significance (σ)" column.

#### MINOR

**P4-m1 | Abstract, p. 1 | Ambiguous Sample Size**
*   **Problem:** The abstract mentions the headline result comes from a mask with "n=5,547,858". This number is significantly larger than the 3.2 million spirals and could be confusing to the reader. While Table I clarifies this is a weighted count of all galaxies used for depth estimation, the abstract would benefit from this clarification.
*   **Fix:** Briefly clarify in the abstract that `n=5,547,858` is a survey-depth-weighted galaxy count, not the number of spiral galaxies in the analysis. For example: "...on the strict-superset subsample mask (using a depth map from n=5,547,858 total galaxies, fsky = 0.659)..."

**P4-m2 | Table I, p. 4 | Inconsistent Estimator Reporting**
*   **Problem:** In Table I, estimators (i), (ii), (iii), and (v) report a significance in units of σ. Estimator (iv), "hemisphere LEE (MC)", reports a p-value (`p_LEE ≤ 10^-4`). This is inconsistent. The text and Appendix C clarify that the pre-LEE significance is 3.05σ. For consistency and clarity, the table should report this pre-correction sigma value.
*   **Fix:** Change the entry for estimator (iv) in Table I to report the pre-LEE significance of +3.05σ. A footnote can be added to direct the reader to Appendix C for the discussion of the look-elsewhere effect correction.

**P4-m3 | Section IV.B, p. 4 | Mismatch with Corrected Table II Value**
*   **Problem:** The text states "The Catalog C residual (9.5σ from 0.5000, Table II)". This value is based on the likely incorrect value in Table II (see finding P4-M2).
*   **Fix:** Update this value to match the corrected calculation for Table II (which should be 9.32σ).

**P4-m4 | Page 1, Date | Future Date**
*   **Problem:** The paper is dated "June 2026". This is presumably a placeholder.
*   **Fix:** Update the date to the current submission date.

**P4-m5 | Section II.B, p. 3 | Inconsistent Training Set Size**
*   **Problem:** The text states the combined training set has 26,636 images. However, the sum of the three listed sources (GZ1: 6,637; CE-ResNet: 17,153; Synthetic: 2,000) is 25,790. This also makes the claim that 67.6% of labels derive from CE-ResNet incorrect (the calculated value is 66.5% based on the sum). This numerical discrepancy must be resolved.
*   **Fix:** Correct the total training set size and the derived percentage, or clarify the source of the discrepancy.

**P4-m6 | Section IV.B, p. 4 | Stale/Unreferenced Asymmetry Numbers**
*   **Problem:** The text claims a "3.86x asymmetry-suppression factor from raw +2.05% to equivariant -0.53%". These numbers do not appear in Table II or elsewhere in the paper and seem to contradict the values in Table II (+0.79% and -0.26% excess).
*   **Fix:** These numbers should be corrected to match the values reported in Table II, or be explicitly sourced if they refer to a different calculation.

**P4-m7 | Table IV, p. 5 | Minor Arithmetic Discrepancy**
*   **Problem:** The z-score for the "Hemisphere max|A|" statistic is calculated from the provided numbers as `(3.48 - 1.69) / 0.41 = 4.36`. The table reports `+4.42`. This should be corrected for consistency.
*   **Fix:** Recompute and correct the z-score in Table IV.

**P4-m8 | Table I & IV, p. 4-5 | Minor Arithmetic Discrepancy**
*   **Problem:** The z-score for the monopole+mask null (pre-MASTER pseudo-C) is calculated from the numbers in Table IV as `(1.696e-2 - 1.685e-2) / 0.007e-2 = 1.57`. The tables report `+1.68`. This should be corrected.
*   **Fix:** Recompute and correct this z-score in both Table I (estimator v) and Table IV.

#### NIT

**P4-N1 | Appendix D, p. 8 | Typo in WLS fit result**
*   **Problem:** The text describing the WLS fit states: "the interpretation (i) reference amplitude 1.7% at z = -264.5 from the naive WLS posterior". The `z` here appears to be a z-score or significance, not a redshift. Using the symbol `z` is potentially confusing in a cosmology context.
*   **Fix:** Replace `z` with `σ` or "z-score" to avoid ambiguity with redshift. For example: "...with a significance of σ = -264.5...".

**P4-N2 | Section VII, p. 6 | Ambiguous Novelty Claim**
*   **Problem:** The claim of having the "largest galaxy chirality catalog to date" is plausible but could be strengthened by a direct comparison.
*   **Fix:** To make the claim more concrete, explicitly compare the number of spiral galaxies in this work (3.2M) to the number in the most relevant previous works (e.g., Jia et al. 2023, which used 1.95M).

---

## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, methodologically robust paper that presents an important null result for the cosmic dipole in galaxy chirality. The analysis is thorough, and the authors' careful treatment of systematics is exemplary. The paper is a strong candidate for publication in Physical Review D. However, the identified issues, particularly the numerical inconsistencies in key tables, the unclear justification for the claimed exclusion of previous results, and the omission of essential data for result verification (Table III), must be addressed. Once these major and minor points are corrected, the paper will meet the high standards of the journal.