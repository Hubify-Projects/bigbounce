# P4 auto-2026-06-08_1520pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (10872 chars)
**Wall time**: 161.3s

---

## Referee Report: P4

**To the Editor of Physical Review D,**

This manuscript, "Survey-Scale Galaxy Chirality with Equivariant TTA...", presents a detailed analysis of galaxy chirality using a large dataset of 3.2 million spiral galaxies from the DESI Legacy Surveys. The primary scientific result is a null detection of a cosmological dipole in the chirality distribution, a parity-even observable. The authors employ modern machine learning techniques (a Vision Transformer with Test-Time Averaging) and conduct an exceptionally thorough investigation of systematic effects. The identification and quantification of a "monopole-mask leakage" channel as an explanation for previously reported signals in other analyses is a significant contribution to the field. The work is methodologically rigorous, and the public release of the catalog, model, and code is commendable.

The paper is well-structured and the conclusions are well-supported by the analysis presented. However, there are several essential and major issues that must be addressed before the manuscript can be considered for publication. These include the presence of future dates and internal-review language, a recurring and critical sign error in the reporting of a key systematic, and several inconsistencies in tables that hinder verifiability.

I recommend **MAJOR REVISIONS**. The scientific core of the paper is strong, but the current manuscript does not meet the high standards of rigor and clarity expected for Physical Review D.

---

### Detailed Findings

#### ESSENTIAL

*   **P4-E1 (Page 1, Metadata):** The paper is dated "June 2026". This is a future date and must be corrected to the date of submission.
    *   **Problem:** `(Dated: June 2026)`
    *   **Fix:** Replace with the current date.

*   **P4-E2 (Page 9, Data Availability):** The data release tag is given a future date, "v2026.04". This is an error and must be corrected.
    *   **Problem:** `Release tag: v2026.04.`
    *   **Fix:** Correct the release tag to reflect the actual version at the time of publication.

*   **P4-E3 (Page 4, Sec. IV D):** The text contains language referring to the paper's own revision history ("earlier paper versions"). This is inappropriate for a formal publication.
    *   **Problem:** `...were interpreted in earlier paper versions as mask-geometric leakage...`
    *   **Fix:** Rephrase to remove the self-reference. For example: "These signals could be misinterpreted as mask-geometric leakage of the global 9.5σ monopole."

*   **P4-E4 (Page 4, Footnote 1):** The footnote contains language referring to a "previous wording" of the manuscript, which is internal-review content.
    *   **Problem:** `The previous wording "Binomial(ntotal, pglobal)" PCW was ambiguous...`
    *   **Fix:** Remove the reference to previous versions. State the clarification directly. For example: "To avoid ambiguity, we clarify that the generative null draws from the per-pixel spiral count (Nspiral(p)), not the total galaxy count (N(p)all)."

#### MAJOR

*   **P4-M1 (Page 4, Table II & Page 9, Data Availability):** There is a persistent and critical sign error in the reported global CW fraction residual for the final Catalog C. Table II reports the deviation as "9.5" σ, while the calculation `(0.4974 - 0.5) / 0.000279` yields **-9.5σ**. The text on page 4 ("9.5σ from 0.5000") and the Data Availability section on page 9 ("CW-bias residual of 0.26% (9.5σ)") repeat this error. The sign is physically meaningful, indicating a slight CCW excess, and must be reported correctly throughout the manuscript.
    *   **Problem:** The sign of the deviation for Catalog C is incorrect in Table II and in all mentions in the text.
    *   **Fix:** Change "9.5" to "-9.5" in Table II. Change "9.5σ" to "-9.5σ" on page 4. Change "0.26% (9.5σ)" to "-0.26% (-9.5σ)" on page 9. Ensure consistency across the entire manuscript.

*   **P4-M2 (Page 5, Table III):** This table is not verifiable as presented. The significance of the bandpower measurements is given, but the mean of the null distribution, `<C_null>`, is not provided. The significance is defined as `(C_obs - <C_null>) / std(C_null)`. The table provides `C_obs` (as `Ce`) and `std(C_null)` (as `σ_null`), but omits `<C_null>`. Without this value, the stated significance cannot be independently checked.
    *   **Problem:** The `Significance (σ)` column cannot be verified without the mean of the null power spectrum for each bandpower.
    *   **Fix:** Add a column to Table III for `<C_null>` for each bandpower so that the significance calculation is transparent and verifiable.

*   **P4-M3 (Page 4, Table I):** The table mixes different types of quantities in the "σ" column, which is misleading. Row (iv) reports a p-value (`PLEE ≤ 10^-4`) and row (vi) reports a sensitivity threshold, not a measurement significance.
    *   **Problem:** The "σ" column contains quantities that are not standard-deviation significances.
    *   **Fix:** For row (iv), convert the p-value to an equivalent Gaussian sigma (e.g., `>3.7σ`) and state this in the table, or change the column header to be more general (e.g., "Significance"). For row (vi), this information does not belong in this table as it is not a measurement. Move the injection floor result to the table caption or the main text.

*   **P4-M4 (Page 4, Sec. IV B):** The text quotes asymmetry suppression factors that are not derivable from the provided tables.
    *   **Problem:** `The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant -0.53% demonstrates...`
    *   **Fix:** The values in Table II are +0.79% (raw) and -0.26% (equivariant). The author must either correct the text to use the values from Table II or provide the source/derivation for the "+2.05%" and "-0.53%" figures. All numbers in the text must be consistent with the tables.

#### MINOR

*   **P4-m1 (Page 3, Sec. IV A):** There are minor rounding discrepancies in the reported percentages for the catalog statistics.
    *   **Problem:** `CW 1,592,107 (18.78%)` should be 18.79%. `spiral total Nspiral = 3,201,160 (37.78%)` should be 37.77%.
    *   **Fix:** Re-calculate and correct the percentages to two decimal places.

*   **P4-m2 (Page 3, Sec. III A):** The significance of the real-space dipole is given as a unitless number, which is inconsistent with other entries.
    *   **Problem:** `(Adipole = 0.43, p = 0.30)`
    *   **Fix:** For clarity and consistency with the abstract and Table I, write this as `+0.43σ`.

*   **P4-m3 (Page 5, Footnote):** There is a minor typo in the footnote.
    *   **Problem:** `sub-0.10 effect`
    *   **Fix:** This should likely be `sub-0.1σ effect`. Please clarify or correct.

*   **P4-m4 (Page 6, Sec. VII):** The list formatting in the conclusions is incorrect.
    *   **Problem:** The first item is labeled `α.`
    *   **Fix:** Change to standard lettering, e.g., `a.` or `1.`

*   **P4-m5 (Page 7, Appendix B):** Equation (B1) is mathematically incomplete.
    *   **Problem:** `L = LCE + λ * (1/N) * sum ||p(xi) – Sp(xi)||^2`
    *   **Fix:** Add the summation index and limits, e.g., `sum_{i=1 to N}`.

#### NIT

*   **P4-N1 (Page 1, Title):** The title is exceptionally long and reads more like a summary. While descriptive, a more concise title would be more conventional for PRD. This is a suggestion for the author's consideration.
*   **P4-N2 (Page 1, PACS numbers):** The PACS numbers are somewhat dated. The author might consider updating them or removing them, as they are optional in many journals now. `98.62.Ai` (Origin... of the elements) seems particularly ill-suited.

---

## Summary recommendation

**MAJOR REVISIONS**

The paper presents a high-quality, thorough, and important null result in the search for cosmological isotropy breaking. The systematic analysis is a model for future work in this area. However, the manuscript is marred by several errors, including incorrect signs on key results, unverifiable tables, and inappropriate internal-review language. These issues must be comprehensively addressed to bring the paper up to the standard required for publication in Physical Review D. I am confident that the authors can address these points in a revised manuscript, which I would be willing to review.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the report with the additional findings from the second, more rigorous review.

================================================================
## Referee Report: P4

**To the Editor of Physical Review D,**

This manuscript, "Survey-Scale Galaxy Chirality with Equivariant TTA...", presents a detailed analysis of galaxy chirality using a large dataset of 3.2 million spiral galaxies from the DESI Legacy Surveys. The primary scientific result is a null detection of a cosmological dipole in the chirality distribution, a parity-even observable. The authors employ modern machine learning techniques (a Vision Transformer with Test-Time Averaging) and conduct an exceptionally thorough investigation of systematic effects. The identification and quantification of a "monopole-mask leakage" channel as an explanation for previously reported signals in other analyses is a significant contribution to the field. The work is methodologically rigorous, and the public release of the catalog, model, and code is commendable.

The paper is well-structured and the conclusions are well-supported by the analysis presented. However, there are several essential and major issues that must be addressed before the manuscript can be considered for publication. These include the presence of future dates and internal-review language, a recurring and critical sign error in the reporting of a key systematic, and several inconsistencies and arithmetic errors in tables that hinder verifiability and undermine confidence in the reported results.

I recommend **MAJOR REVISIONS**. The scientific core of the paper is strong, but the current manuscript does not meet the high standards of rigor and clarity expected for Physical Review D.

---

### Detailed Findings

#### ESSENTIAL

*   **P4-E1 (Page 1, Metadata):** The paper is dated "June 2026". This is a future date and must be corrected to the date of submission.
    *   **Problem:** `(Dated: June 2026)`
    *   **Fix:** Replace with the current date.

*   **P4-E2 (Page 9, Data Availability):** The data release tag is given a future date, "v2026.04". This is an error and must be corrected.
    *   **Problem:** `Release tag: v2026.04.`
    *   **Fix:** Correct the release tag to reflect the actual version at the time of publication.

*   **P4-E3 (Page 4, Sec. IV D):** The text contains language referring to the paper's own revision history ("earlier paper versions"). This is inappropriate for a formal publication.
    *   **Problem:** `...were interpreted in earlier paper versions as mask-geometric leakage...`
    *   **Fix:** Rephrase to remove the self-reference. For example: "These signals could be misinterpreted as mask-geometric leakage of the global 9.5σ monopole."

*   **P4-E4 (Page 4, Footnote 1):** The footnote contains language referring to a "previous wording" of the manuscript, which is internal-review content.
    *   **Problem:** `The previous wording "Binomial(ntotal, pglobal)" PCW was ambiguous...`
    *   **Fix:** Remove the reference to previous versions. State the clarification directly. For example: "To avoid ambiguity, we clarify that the generative null draws from the per-pixel spiral count (Nspiral(p)), not the total galaxy count (N(p)all)."

#### MAJOR

*   **P4-M1 (Page 4, Table II & Page 9, Data Availability):** There is a persistent and critical sign error in the reported global CW fraction residual for the final Catalog C. Table II reports the deviation as "9.5" σ, while the calculation `(0.4974 - 0.5) / 0.000279` yields **-9.5σ**. The text on page 4 ("9.5σ from 0.5000") and the Data Availability section on page 9 ("CW-bias residual of 0.26% (9.5σ)") repeat this error. The sign is physically meaningful, indicating a slight CCW excess, and must be reported correctly throughout the manuscript.
    *   **Problem:** The sign of the deviation for Catalog C is incorrect in Table II and in all mentions in the text.
    *   **Fix:** Change "9.5" to "-9.5" in Table II. Change "9.5σ" to "-9.5σ" on page 4. Change "0.26% (9.5σ)" to "-0.26% (-9.5σ)" on page 9. Ensure consistency across the entire manuscript.

*   **P4-M2 (Page 5, Table III):** This table is not verifiable as presented. The significance of the bandpower measurements is given, but the mean of the null distribution, `<C_null>`, is not provided. The significance is defined as `(C_obs - <C_null>) / std(C_null)`. The table provides `C_obs` (as `Ce`) and `std(C_null)` (as `σ_null`), but omits `<C_null>`. Without this value, the stated significance cannot be independently checked.
    *   **Problem:** The `Significance (σ)` column cannot be verified without the mean of the null power spectrum for each bandpower.
    *   **Fix:** Add a column to Table III for `<C_null>` for each bandpower so that the significance calculation is transparent and verifiable.

*   **P4-M3 (Page 4, Table I):** The table mixes different types of quantities in the "σ" column, which is misleading. Row (iv) reports a p-value (`PLEE ≤ 10^-4`) and row (vi) reports a sensitivity threshold, not a measurement significance.
    *   **Problem:** The "σ" column contains quantities that are not standard-deviation significances.
    *   **Fix:** For row (iv), convert the p-value to an equivalent Gaussian sigma (e.g., `>3.7σ`) and state this in the table, or change the column header to be more general (e.g., "Significance"). For row (vi), this information does not belong in this table as it is not a measurement. Move the injection floor result to the table caption or the main text.

*   **P4-M4 (Page 4, Sec. IV B):** The text quotes asymmetry suppression factors that are not derivable from the provided tables.
    *   **Problem:** `The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant -0.53% demonstrates...`
    *   **Fix:** The values in Table II are +0.79% (raw) and -0.26% (equivariant). The author must either correct the text to use the values from Table II or provide the source/derivation for the "+2.05%" and "-0.53%" figures. All numbers in the text must be consistent with the tables.

*   **P4-M6 (Page 2, Sec I & Page 6, Sec VI B):** The claim that this work disfavors the Shamir ~3% signal by a factor of 6-12 is potentially misleading. The factor appears to be derived by comparing the 3% signal to the theoretical Fisher floor (~0.3%), not the empirically demonstrated 3σ sensitivity limit (0.75%). A comparison to the 3σ limit yields a factor of 4. The authors should clarify the basis of this comparison or revise the factor to be more conservative.

*   **P4-M7 (Page 3, Sec II B):** The accounting of training set labels is inconsistent. The sum of the three sources (6,637 + 17,153 + 2,000 = 25,790) does not match the stated total (26,636). Furthermore, the claimed percentage of labels from CE-ResNet (67.6%) does not match the calculation from either total (66.5% or 64.4%). These numbers must be corrected for consistency.

*   **P4-M8 (Page 4, Table II):** The `Dev. (σ)` column is not correctly calculated from the other columns in the table. For all three tiers, the calculation `(fcw - 0.5) / σ` yields a result that differs from the value in the table by 2-3%. This column must be re-calculated and corrected.

*   **P4-M9 (Page 5, Table III):** The bandpower results for `leff > 1` are internally inconsistent. Attempting to reconstruct the mean of the null distribution, `<C_null>`, from the provided `C_obs`, `σ_null`, and `Significance` leads to unphysical negative values for the power spectrum. This indicates a significant error in the table's values or their definitions. The table is unverifiable and incorrect as it stands and must be fully revised.

*   **P4-M10 (Page 5, Table IV):** The z-score for the "Pre-MASTER pseudo-C(l=1)" statistic is miscalculated. The data `(1.696e-2)`, null mean `(1.685e-2)`, and null std `(0.007e-2)` yield `z = +1.57`, not `+1.68` as reported. This calculation must be corrected.

#### MINOR

*   **P4-m1 (Page 3, Sec. IV A):** There are minor rounding discrepancies in the reported percentages for the catalog statistics.
    *   **Problem:** `CW 1,592,107 (18.78%)` should be 18.79%. `spiral total Nspiral = 3,201,160 (37.78%)` should be 37.77%.
    *   **Fix:** Re-calculate and correct the percentages to two decimal places.

*   **P4-m2 (Page 3, Sec. III A):** The significance of the real-space dipole is given as a unitless number, which is inconsistent with other entries.
    *   **Problem:** `(Adipole = 0.43, p = 0.30)`
    *   **Fix:** For clarity and consistency with the abstract and Table I, write this as `+0.43σ`.

*   **P4-m3 (Page 5, Footnote):** There is a minor typo in the footnote.
    *   **Problem:** `sub-0.10 effect`
    *   **Fix:** This should likely be `sub-0.1σ effect`. Please clarify or correct.

*   **P4-m4 (Page 6, Sec. VII):** The list formatting in the conclusions is incorrect.
    *   **Problem:** The first item is labeled `α.`
    *   **Fix:** Change to standard lettering, e.g., `a.` or `1.`

*   **P4-m5 (Page 7, Appendix B):** Equation (B1) is mathematically incomplete.
    *   **Problem:** `L = LCE + λ * (1/N) * sum ||p(xi) – Sp(xi)||^2`
    *   **Fix:** Add the summation index and limits, e.g., `sum_{i=1 to N}`.

*   **P4-m6 (Page 5, Sec V A):** The text states the "maximum regional asymmetry is 0.32%". This value is not defined or derived anywhere else in the manuscript. A source or calculation for this number should be provided.

*   **P4-m7 (Page 7, Appendix B):** The text claims a "1.2 pp asymmetry" in the classifier contributes to the raw CW excess. This is confusing. The raw excess in Catalog A is 0.79%. The relationship between the "1.2 pp" value and the catalog excess needs to be clarified.

#### NIT

*   **P4-N1 (Page 1, Title):** The title is exceptionally long and reads more like a summary. While descriptive, a more concise title would be more conventional for PRD. This is a suggestion for the author's consideration.
*   **P4-N2 (Page 1, PACS numbers):** The PACS numbers are somewhat dated. The author might consider updating them or removing them, as they are optional in many journals now. `98.62.Ai` (Origin... of the elements) seems particularly ill-suited.

---

## Summary recommendation

**MAJOR REVISIONS**

The paper presents a high-quality, thorough, and important null result in the search for cosmological isotropy breaking. The systematic analysis is a model for future work in this area. However, the manuscript is marred by several errors, including incorrect signs on key results, unverifiable and arithmetically inconsistent tables, and inappropriate internal-review language. These issues must be comprehensively addressed to bring the paper up to the standard required for publication in Physical Review D. I am confident that the authors can address these points in a revised manuscript, which I would be willing to review.