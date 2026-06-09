# P4 auto-2026-06-09_1042pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (10378 chars)
**Wall time**: 202.5s

---

**Referee Report on "Survey-Scale Galaxy Chirality with Equivariant TTA..."**

This paper presents a detailed analysis of the large-scale distribution of spiral galaxy chirality using 8.47 million galaxies from the DESI Legacy Surveys. The primary scientific result is a null detection of a cosmological dipole in the chirality asymmetry. The authors perform an exceptionally thorough analysis of potential systematic effects, demonstrating that a small, uniform classifier bias (a monopole) can couple with the patchy survey footprint to create a spurious, statistically significant dipole signal in naive estimators. The paper's main contribution is both the robust null result and the detailed methodology for controlling these systematics, which serves as a valuable guide for future, similar studies.

The overall scientific approach is sound and the conclusions are well-supported by a comprehensive suite of null tests and diagnostic analyses. The use of equivariant test-time averaging, the pre-declared analysis hierarchy, and the detailed investigation of the "monopole-mask leakage" channel are all exemplary. However, the manuscript contains several significant errors and points of confusion that must be addressed before it can be considered for publication in Physical Review D.

## Findings

### ESSENTIAL

**P4-E1: Abstract + Sec. III A (Page 1, 3) — Inconsistent and unclear statistical significance of the canonical-mask residual.**
*   **Problem:** The abstract reports the "post-MASTER canonical-mask direct-MC residual is +3.64σ". However, the parenthetical text immediately following this claim is contradictory and confusing: "(z = Δ/σ_null moment-ratio; empirical rank p_mc = 0.030, i.e. ≈1.9σ Gaussian-equivalent; 500-MC binomial per-pixel-shuffle null)". An empirical p-value of 0.030 (from 15/500 in Sec. VII.b) corresponds to a one-sided significance of approximately 1.88σ, not 3.64σ. The term "moment-ratio" for `z` is non-standard and its definition is not provided. It is unclear how a significance of +3.64σ is derived if the empirical rank from the stated null distribution gives ≈1.9σ. This ambiguity undermines a key secondary result of the paper that is discussed at length.
*   **Required Fix:** The author must clarify the precise definition of the +3.64σ statistic. If it is not a direct significance in standard deviation units of the null distribution, this must be stated explicitly and the non-standard definition of `z` must be provided and justified. The abstract and all mentions of this result must be rewritten to be statistically unambiguous, clearly distinguishing between the moment-ratio value and the empirical significance derived from the null simulations. The most transparent approach would be to report the empirical p-value and its Gaussian-equivalent significance as the primary result of that test.

### MAJOR

**P4-M1: Sec. IV B + Table II (Page 4, 5) — Significant numerical error in global CW fraction significance.**
*   **Problem:** Table II reports that for Catalog C (equivariant), the global CW fraction `cw/(cw+ccw)` is `0.4974 ± 0.000279`. The table then reports the deviation from 0.5 as `Dev. (σ) = 9.5`. A direct calculation yields `(0.4974 - 0.5) / 0.000279 = -9.32σ`. The reported value is incorrect in both sign and magnitude. The text in Sec. IV B on page 4 also quotes the incorrect `9.5σ` value. This is a significant error in a key diagnostic table.
*   **Required Fix:** Correct the `Dev. (σ)` value for Catalog C in Table II to `-9.3` (or the precise value). Correct the corresponding text on page 4 that refers to this `9.5σ` value. Re-verify all other calculated values in this table.

### MINOR

**P4-m1: Title Page + Sec. Data Availability (Page 1, 13) — Future dating.**
*   **Problem:** The paper is dated "June 2026" and the data availability section lists a release tag of "v2026.04". This is inappropriate for a journal submission.
*   **Required Fix:** The date should be changed to the date of submission. The release tag should be a current or past version.

**P4-m2: Throughout — Clarity of multiple estimators.**
*   **Problem:** The paper introduces a large number of estimators for the dipole/l=1 power, each with a different significance (e.g., raw pre-MASTER `+6.48σ`, monopole-preserving pre-MASTER `+4.31σ`, canonical-mask post-MASTER `+3.64σ`, headline subsample-mask MASTER `-0.122σ`, real-space `+0.43σ`). While the text explains them individually, their interrelation is complex and can be difficult for the reader to track.
*   **Required Fix:** Add a small paragraph or a summary table early in the Results section (Sec. IV) that explicitly defines and contrasts these key estimators. This should clarify which mask is used for each, whether it is pre/post-MASTER, whether it is pre/post-monopole subtraction, and what systematic it is designed to test. This would greatly improve the readability and impact of the paper.

**P4-m3: Figure 8 Caption (Page 9) — Misleading caption.**
*   **Problem:** The caption for Figure 8 states: "The post-MASTER residual is +3.64σ...". However, the plot itself clearly shows the *pre-MASTER* pseudo-C_l power and demonstrates how it is almost perfectly reproduced by the *pre-MASTER* monopole-only generative null. The plot does not show the post-MASTER residual.
*   **Required Fix:** Rewrite the caption to accurately describe the content of the plot, which is the successful reproduction of the *pre-MASTER* power by the monopole-leakage null. The mention of the post-MASTER residual should be removed or clearly contextualized as a separate result not depicted in the figure.

### NIT

**P4-N1: Abstract (Page 1) — Awkward phrasing.**
*   **Problem:** The phrase "471 049 high-confidence per-spiral after p_cw>0.9" is slightly awkward.
*   **Required Fix:** Suggest rephrasing to "471,049 high-confidence spirals with p_cw > 0.9" or similar.

**P4-N2: Table I (Page 4) — Potentially misleading p-value.**
*   **Problem:** In the headline summary table, the "hemisphere LEE (MC)" estimator is listed with a significance of `p_LEE < 10^-4`. This is a very strong rejection of the random-label null and could be misinterpreted as a detection. The text in Appendix C correctly explains that this significance vanishes after a look-elsewhere effect (LEE) correction.
*   **Required Fix:** To avoid misinterpretation, add a footnote to this entry in Table I that explicitly states the value is pre-LEE correction and that the post-LEE significance is < 1σ, directing the reader to Appendix C for the full discussion.

## Summary recommendation

**MAJOR REVISIONS**

The paper presents a high-quality, rigorous analysis that makes a valuable contribution to the field by establishing a strong null result for the galaxy chirality dipole and, more importantly, by documenting a critical systematic effect. The work is of a standard appropriate for Physical Review D. However, the identified issues, particularly the inconsistent statistical reporting of a key residual (P4-E1) and the significant numerical error in a main table (P4-M1), are too severe for the paper to be accepted in its current form. Once these essential and major points are thoroughly addressed, the paper should be suitable for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated review, incorporating the new findings from the second, more rigorous pass.

================================================================
**Referee Report on "Survey-Scale Galaxy Chirality with Equivariant TTA..."**

This paper presents a detailed analysis of the large-scale distribution of spiral galaxy chirality using 8.47 million galaxies from the DESI Legacy Surveys. The primary scientific result is a null detection of a cosmological dipole in the chirality asymmetry. The authors perform an exceptionally thorough analysis of potential systematic effects, demonstrating that a small, uniform classifier bias (a monopole) can couple with the patchy survey footprint to create a spurious, statistically significant dipole signal in naive estimators. The paper's main contribution is both the robust null result and the detailed methodology for controlling these systematics, which serves as a valuable guide for future, similar studies.

The overall scientific approach is sound and the conclusions are well-supported by a comprehensive suite of null tests and diagnostic analyses. The use of equivariant test-time averaging, the pre-declared analysis hierarchy, and the detailed investigation of the "monopole-mask leakage" channel are all exemplary. However, the manuscript contains several significant errors and points of confusion that must be addressed before it can be considered for publication in Physical Review D.

## Findings

### ESSENTIAL

**P4-E1: Abstract + Sec. III A (Page 1, 3) — Inconsistent and unclear statistical significance of the canonical-mask residual.**
*   **Problem:** The abstract reports the "post-MASTER canonical-mask direct-MC residual is +3.64σ". However, the parenthetical text immediately following this claim is contradictory and confusing: "(z = Δ/σ_null moment-ratio; empirical rank p_mc = 0.030, i.e. ≈1.9σ Gaussian-equivalent; 500-MC binomial per-pixel-shuffle null)". An empirical p-value of 0.030 (from 15/500 in Sec. VII.b) corresponds to a one-sided significance of approximately 1.88σ, not 3.64σ. The term "moment-ratio" for `z` is non-standard and its definition is not provided. It is unclear how a significance of +3.64σ is derived if the empirical rank from the stated null distribution gives ≈1.9σ. This ambiguity undermines a key secondary result of the paper that is discussed at length.
*   **Required Fix:** The author must clarify the precise definition of the +3.64σ statistic. If it is not a direct significance in standard deviation units of the null distribution, this must be stated explicitly and the non-standard definition of `z` must be provided and justified. The abstract and all mentions of this result must be rewritten to be statistically unambiguous, clearly distinguishing between the moment-ratio value and the empirical significance derived from the null simulations. The most transparent approach would be to report the empirical p-value and its Gaussian-equivalent significance as the primary result of that test.

### MAJOR

**P4-M1: Sec. IV B + Table II (Page 4, 5) — Significant numerical error in global CW fraction significance.**
*   **Problem:** Table II reports that for Catalog C (equivariant), the global CW fraction `cw/(cw+ccw)` is `0.4974 ± 0.000279`. The table then reports the deviation from 0.5 as `Dev. (σ) = 9.5`. A direct calculation yields `(0.4974 - 0.5) / 0.000279 = -9.32σ`. The reported value is incorrect in both sign and magnitude. The text in Sec. IV B on page 4 also quotes the incorrect `9.5σ` value. This is a significant error in a key diagnostic table.
*   **Required Fix:** Correct the `Dev. (σ)` value for Catalog C in Table II to `-9.3` (or the precise value). Correct the corresponding text on page 4 that refers to this `9.5σ` value. Re-verify all other calculated values in this table.

**P4-M2: Figure 3 vs. Sec IV A (Page 6, 4) — Inconsistent galaxy counts.**
*   **Problem:** Figure 3, a pie chart titled "Catalog C composition," displays the breakdown of galaxy classifications. The counts shown in the figure (e.g., CW: 1,687,069; CCW: 1,634,726) are in direct contradiction with the counts given for Catalog C in the main text in Section IV A (CW: 1,592,107; CCW: 1,609,053). This strongly suggests the figure is a stale result from a different catalog version (e.g., Catalog A or B) and does not represent the data being discussed.
*   **Required Fix:** Replace Figure 3 with a corrected version that accurately reflects the Catalog C counts as stated in the text.

**P4-M3: Sec. IV B + Table II (Page 5) — Stale numbers in body text.**
*   **Problem:** The text at the end of Section IV B on page 5 states: "The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant -0.53% demonstrates the dominance of the equivariant TTA processing." These percentage values are inconsistent with the "Excess (%)" values reported in Table II for Catalog A (raw: +0.79%) and Catalog C (equivariant: -0.26%). The values in the table give a suppression factor of `0.79 / 0.26 ≈ 3.0`, not 3.86. The text appears to contain stale numbers from a previous version of the analysis.
*   **Required Fix:** Update the text on page 5 to use the correct excess values from Table II and recalculate the corresponding suppression factor.

### MINOR

**P4-m1: Title Page + Sec. Data Availability (Page 1, 13) — Future dating.**
*   **Problem:** The paper is dated "June 2026" and the data availability section lists a release tag of "v2026.04". This is inappropriate for a journal submission.
*   **Required Fix:** The date should be changed to the date of submission. The release tag should be a current or past version.

**P4-m2: Throughout — Clarity of multiple estimators.**
*   **Problem:** The paper introduces a large number of estimators for the dipole/l=1 power, each with a different significance (e.g., raw pre-MASTER `+6.48σ`, monopole-preserving pre-MASTER `+4.31σ`, canonical-mask post-MASTER `+3.64σ`, headline subsample-mask MASTER `-0.122σ`, real-space `+0.43σ`). While the text explains them individually, their interrelation is complex and can be difficult for the reader to track.
*   **Required Fix:** Add a small paragraph or a summary table early in the Results section (Sec. IV) that explicitly defines and contrasts these key estimators. This should clarify which mask is used for each, whether it is pre/post-MASTER, whether it is pre/post-monopole subtraction, and what systematic it is designed to test. This would greatly improve the readability and impact of the paper.

**P4-m3: Figure 8 Caption (Page 9) — Misleading caption.**
*   **Problem:** The caption for Figure 8 states: "The post-MASTER residual is +3.64σ...". However, the plot itself clearly shows the *pre-MASTER* pseudo-C_l power and demonstrates how it is almost perfectly reproduced by the *pre-MASTER* monopole-only generative null. The plot does not show the post-MASTER residual.
*   **Required Fix:** Rewrite the caption to accurately describe the content of the plot, which is the successful reproduction of the *pre-MASTER* power by the monopole-leakage null. The mention of the post-MASTER residual should be removed or clearly contextualized as a separate result not depicted in the figure.

**P4-m4: Table III (Page 7) — Incomplete data for verification.**
*   **Problem:** Table III, which presents the angular power spectrum results, reports the measured `C_l`, the null standard deviation `σ_null`, and the final `Significance (σ)`. However, it omits the mean of the null distribution, `<C_null>`. Without this value, the significance `(C_l - <C_null>) / σ_null` cannot be independently verified by the reader.
*   **Required Fix:** Add a column for `<C_null>` to Table III so that all reported significance values are transparent and verifiable.

**P4-m5: Figure 5 Caption vs. Appendix A (Page 8, 10) — Contradictory mask definition.**
*   **Problem:** The definition of the canonical mask, which is critical for reproducibility, is inconsistent within the paper. The caption for Figure 5 states that the mask "requires N_spiral(p) ≥ 5 per pixel". However, Appendix A.c ("NaMaster configuration") states: "Mask: canonical Catalog C mask (pixels with ≥ 10 spirals)."
*   **Required Fix:** Resolve this contradiction and state the correct pixel count threshold consistently in all locations.

### NIT

**P4-N1: Abstract (Page 1) — Awkward phrasing.**
*   **Problem:** The phrase "471 049 high-confidence per-spiral after p_cw>0.9" is slightly awkward.
*   **Required Fix:** Suggest rephrasing to "471,049 high-confidence spirals with p_cw > 0.9" or similar.

**P4-N2: Table I (Page 4) — Potentially misleading p-value.**
*   **Problem:** In the headline summary table, the "hemisphere LEE (MC)" estimator is listed with a significance of `p_LEE < 10^-4`. This is a very strong rejection of the random-label null and could be misinterpreted as a detection. The text in Appendix C correctly explains that this significance vanishes after a look-elsewhere effect (LEE) correction.
*   **Required Fix:** To avoid misinterpretation, add a footnote to this entry in Table I that explicitly states the value is pre-LEE correction and that the post-LEE significance is < 1σ, directing the reader to Appendix C for the full discussion.

**P4-N3: Table II (Page 5) — Minor arithmetic inconsistencies.**
*   **Problem:** The `Dev. (σ)` values for Tiers A and B in Table II have small discrepancies between the reported values and a direct calculation from the other columns (e.g., for Tier A, 28.3 is calculated vs. 28.8 reported).
*   **Required Fix:** Re-calculate and correct these values to ensure full internal consistency of the table.

## Summary recommendation

**MAJOR REVISIONS**

The paper presents a high-quality, rigorous analysis that makes a valuable contribution to the field by establishing a strong null result for the galaxy chirality dipole and, more importantly, by documenting a critical systematic effect. The work is of a standard appropriate for Physical Review D. However, the identified issues, particularly the inconsistent statistical reporting of a key residual (P4-E1), significant numerical errors and stale results (P4-M1, P4-M2, P4-M3), are too severe for the paper to be accepted in its current form. Once these essential and major points are thoroughly addressed, the paper should be suitable for publication.