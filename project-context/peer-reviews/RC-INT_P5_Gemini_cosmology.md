# P5 RC-INT — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` md5=91742098 pages=34
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 174.7s

---

## Referee Report on "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample"

This paper presents a detailed statistical analysis of spiral galaxy chirality as a function of large-scale structure environment, using data from the DESI Data Release 1. The authors cross-match a large catalog of spiral galaxy chiralities with the DESI redshift catalog and perform a cosmic-web classification using the T-Web tidal-tensor method. The primary result is a null detection: the fraction of clockwise (CW) spiral galaxies does not show a statistically significant dependence on environment (void, wall, filament, or cluster). This null result is subjected to an extensive and impressive battery of robustness checks, including a re-analysis using the DESIVAST void catalog (which provides a much larger void sample), sensitivity tests of the T-Web hyperparameters, and cross-validations against other environment classifiers and literature results.

The analysis is exceptionally thorough, and the methodology is transparently documented, with excellent provisions for reproducibility. The conclusion that there is no evidence for an environmental dependence of spiral chirality at the sensitivity of this dataset is well-supported by the presented evidence. However, there are several issues that must be addressed before the paper can be considered for publication in Physical Review D.

### Findings

#### ESSENTIAL

**P5-E1: Dependence on an "in preparation" companion paper (Paper IV)**
*   **Location:** Abstract (p. 1), Section I (p. 3), Section II (p. 3), Table I (p. 4), and throughout.
*   **Problem:** The entire analysis is predicated on the per-galaxy chirality labels and the global monopole offset value derived in "Paper IV," which is cited as "[3] (in preparation)". A core input to a Physical Review D article cannot be an unpublished, un-refereed manuscript. While the authors are commended for summarizing the key inputs in Table I and independently verifying the monopole value on their matched subsample, this does not substitute for a peer-reviewed and publicly available source for the fundamental data (the chirality labels). The scientific conclusions of this paper are not self-contained and cannot be fully verified by the reader.
*   **Fix:** The paper cannot be published until Paper IV is, at a minimum, publicly available on a preprint server (e.g., arXiv) with its full methodology detailed, and preferably accepted for publication. The reference [3] must be updated to a citable source.

#### MAJOR

**P5-M1: Uncomputed Quantitative Claims and Effect Sizes**
*   **Location:** Abstract (p. 2), Section XII.C (p. 12), Section XIII.d (p. 13).
*   **Problem:** The paper reports many statistically significant results (or nulls) using σ, χ², and p-values, but sometimes lacks a measure of practical significance or effect size. For example, the text notes the T-Web class and target program are not independent with a χ² of 4933 (p ≪ 10⁻³⁰⁰), but correctly follows up with a small Cramér's V of 0.078. This is excellent practice and should be applied more consistently. The bright-vs-dark sign-flip is reported with a two-sample |z| ≈ 2.1, but the practical difference in fcw (e.g., 0.4976 vs 0.5069 for filament) should be stated alongside the significance to ground the finding.
*   **Fix:** For every key statistical test, especially those involving large sample sizes where even tiny effects can be statistically significant (e.g., the bright/dark split, the T-Web vs. program contingency test), ensure that an appropriate effect size (e.g., Δfcw in percentage points, Cramér's V, Cohen's d) is reported directly alongside the significance test result (χ², z, p-value). This has been done well in some places but should be universal.

#### MINOR

**P5-m1: Table V Residual Sign Error**
*   **Location:** Section XI.D (p. 11), Table V (p. 11).
*   **Problem:** In Table V, the column for the residual `σ_obs - σ_pred` appears to have a sign error for quintile 3. The observed value is `σ_obs` = -3.94 and the predicted is `σ_pred` = -2.07. The residual should be -3.94 - (-2.07) = -1.87. The table lists this value as 1.87. The text on p. 10 correctly refers to the *absolute* residual as 1.87, but the table column is not labeled as an absolute value.
*   **Fix:** Correct the value for quintile 3 in the `σ_obs - σ_pred` column of Table V to -1.87.

**P5-m2: Citation of Future-Dated Preprints**
*   **Location:** Section IX.C (p. 26), Section X (p. 26), References [11], [12], [13].
*   **Problem:** The paper cites several preprints with a year of "2026" or "2025" (e.g., Ullah et al. 2026, Zapata-Zuluaga et al. 2026, Rincón et al. 2025). While these are likely placeholders for the expected year of publication, it is unconventional. The standard is to cite the year the preprint appeared on arXiv.
*   **Fix:** Update the years in the citations and the reference list to match the year the work first appeared as a preprint. For example, Rincón et al. [13] is arXiv:2411.00148, so it should be cited as (2024).

**P5-m3: Inconsistent σ Notation**
*   **Location:** Abstract (p. 1), Table IV (p. 9), and throughout.
*   **Problem:** The paper uses `σ` to denote the binomial z-score (e.g., `σ_from_half`). However, in physics literature, `σ` is also commonly used for standard deviation or significance in Gaussian terms (e.g., a "3σ detection"). While the paper defines its usage, the abstract reports values like "-2.61σ" and "-4.66σ", which could be misinterpreted.
*   **Fix:** Consistently use the more explicit `z` or `z-score` notation (e.g., `z_from_half`) instead of `σ` when reporting the binomial test statistic, especially in the abstract and headline results. Alternatively, ensure the first use in the abstract explicitly defines `σ` as the one-sample binomial z-score. The current `σ_from_half` is clear, but the shorthand `σ` is less so.

#### NIT

**P5-N1: Minor Typographical Errors and Inconsistencies**
*   **Location:** Page 1, Abstract.
*   **Problem:** The text states "The quoted σ_from_half values scale as √n at fixed fractional offset and are therefore not mutually comparable across classes of different n." The symbol for √n is rendered as `n`.
*   **Fix:** Correct the symbol to √n.

*   **Location:** Page 2, Robustness section.
*   **Problem:** The text states "the two catalog-native GALZONE contrasts give |Δfcw| ≤ 0.0037 (V2-REVOLVER catalog-native Δ = -0.0037, |zσ| = 1.25, p = 0.21...". The notation `|zσ|` is unusual. It should likely be `|z_Δ|` or simply `|z|`.
*   **Fix:** Standardize the notation for the z-score of the contrast, e.g., to `|z_Δ|`.

*   **Location:** Page 30, Conclusions.
*   **Problem:** The text lists the canonical run fractions as `{0.484, 0.503, 0.498, 0.496}`. The value for filament (0.498) is missing a trailing zero compared to other values in the paper (e.g., 0.4980 in the abstract).
*   **Fix:** Ensure consistent precision in quoted numbers throughout the manuscript (e.g., 0.4980).

### Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, rigorous, and valuable paper that provides a strong constraint on the environmental dependence of spiral galaxy chirality. The authors have performed an exhaustive set of tests to validate their null result, and the level of transparency and reproducibility is exemplary. However, the critical dependence on an unpublished and un-refereed companion paper (Paper IV) for the primary data is a disqualifying issue for publication in Physical Review D at this time.

Therefore, I recommend **Major Revisions**. The paper should be held until reference [3] is publicly available and citable. Once this essential condition is met, the other minor corrections can be easily addressed, and the paper will represent a significant and robust contribution to the field.