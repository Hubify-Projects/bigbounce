# P5 auto-2026-06-08_1354pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (13326 chars)
**Wall time**: 187.0s

---

## Referee Report on "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals"

This paper presents a detailed investigation into the potential dependence of spiral galaxy chirality on large-scale structure environment, using data from DESI DR1 cross-matched with a new, large-scale chirality catalog. The primary method involves classifying galaxies into cosmic-web environments (void, wall, filament, cluster) and testing for variations in the clockwise (CW) fraction. The author performs an extensive set of null tests and robustness checks, including using multiple environment finders (V-Web, DESIVAST, Tempel+ FoF, ASTRA), and stratifying the data by redshift, density, sky position, and galaxy type. The main conclusion is a null result: after accounting for a small, catalog-wide systematic offset (monopole), no significant evidence for an environment-dependent chirality signal is found at the sensitivity of the current data.

The analysis is comprehensive and the author demonstrates a strong command of potential observational systematics. The multi-layered approach to robustness, particularly the primary analysis anchored on the peer-reviewed DESIVAST void catalog, is a significant strength. However, the manuscript in its current form contains several essential errors, inconsistencies, and questionable scientific practices that preclude its publication in Physical Review D without substantial revision.

### ESSENTIAL Revisions

**P5-E1: Reliance on Unpublished, Un-reviewed Primary Data Source**
*   **Section:** Throughout, e.g., Abstract (p. 1), Section II (p. 2)
*   **Problem:** The entire analysis is predicated on the galaxy chirality catalog from "Paper IV [3]", which is repeatedly described as a "companion work, not yet peer-reviewed" and "in preparation". A manuscript submitted for publication cannot be fundamentally dependent on data and core results (like the monopole offset) from a source that is not publicly available or has not undergone any peer review. This prevents the reader and reviewer from verifying the most basic inputs to the present analysis.
*   **Required Fix:** Paper IV must be made publicly available, at a minimum as a preprint on a service like arXiv, before this manuscript can be seriously considered for publication. The reference [3] must be updated to point to this public version.

**P5-E2: Fundamental Misstatement of Input Parity Violation Signal**
*   **Section:** II, p. 2
*   **Problem:** The text states: "Paper IV [3] ... establishes the global mixture in the post-test-time-augmentation equivariant classifier as a CW fraction of 0.4974 ± 0.000279, consistent with parity at ~1σ." This is incorrect. A deviation of `(0.4974 - 0.5)` with an uncertainty of `0.000279` corresponds to a `( -0.0026 / 0.000279) ≈ 9.3σ` deviation from parity. This is a highly significant inconsistency, not a `~1σ` one. The author likely confuses the monopole measurement with the dipole measurement (which is later quoted as a null result). This sentence, as written, fundamentally misrepresents the starting point of the analysis.
*   **Required Fix:** The sentence must be rewritten to accurately reflect the statistical significance of the monopole. For example: "...a CW fraction of 0.4974 ± 0.000279, which represents a ~9.3σ deviation from a perfect parity-symmetric mixture. Paper IV argues this offset is a classifier-level systematic bias (monopole), not a cosmological signal."

**P5-E3: Inconsistent and Impossible Sample Sizes**
*   **Section:** VI D, subsection c, p. 7
*   **Problem:** The text reports results for a "filament-class tracer-program decomposition". It quotes a sample size of `n = 21,203` for "filament dark". However, in the preceding subsection (b), the total "dark" sample (LRG, ELG, QSO) across all environments is given as `n = 14,782`. It is impossible for a subset (dark galaxies in filaments) to be larger than the total set.
*   **Required Fix:** The author must find the source of this error and report the correct sample sizes. All associated calculations must be verified with the corrected numbers.

**P5-E4: Incorrect Signs in Key Results Table**
*   **Section:** VIII, Table VIII, p. 12
*   **Problem:** The `Δfcw` column in Table VIII reports the difference in CW fraction between void and non-void galaxies for three different DESIVAST algorithms. Re-calculating these values from the `f_void` and `f_non-void` columns reveals that all three signs in the `Δfcw` column are incorrect.
    *   VoidFinder: `0.4964 - 0.4971 = -0.0007` (Table says `+0.0007`)
    *   V2-REVOLVER: `0.4986 - 0.4967 = +0.0019` (Table says `-0.0019`)
    *   V2-VIDE: `0.4971 - 0.4970 = +0.0001` (Table says `-0.0001`)
    This level of carelessness in a central results table is unacceptable.
*   **Required Fix:** Correct the signs in the `Δfcw` column of Table VIII.

**P5-E5: Use of Future-Dated and "In Preparation" References**
*   **Section:** Throughout, e.g., p. 1, p. 10, p. 15, p. 20
*   **Problem:** The paper is dated "June 2026". Several key references are cited with future years (e.g., Rincón et al. 2025 [13], Ullah et al. 2026 [11], Zapata-Zuluaga et al. 2026 [12]). Others are "in preparation" ([3], [4]). This is not standard academic practice. A submitted paper must rely on the existing, verifiable body of literature at the time of submission.
*   **Required Fix:** The date of the paper must be corrected to the submission date. All references must be updated to their current, correct status (e.g., "ApJ, in press", "arXiv:xxxx.xxxxx", etc.). If a source is not yet public, it cannot be a load-bearing citation.

### MAJOR Revisions

**P5-M1: Inconsistent Calculation of Predicted Sigma**
*   **Section:** VI A, p. 6
*   **Problem:** The paper predicts the expected sigma deviation due to the monopole for the filament class: `σ_pred(filament) ≈ -3.16`. However, a direct calculation using the provided formula (`σ_pred = 2 * Δfcw * √N`) with `Δfcw = -0.0026` and `N = 408,187` yields `σ_pred ≈ -3.32`. This is a ~5% discrepancy. Furthermore, the text claims this is "within order-unity" of the observed `σ_obs = -2.61`, but the residual is `~0.7σ`, which is not negligible. The prediction for the cluster class, however, is correct.
*   **Required Fix:** The author must verify this calculation and correct the text. The interpretation of the residual should be revisited if the discrepancy remains.

**P5-M2: Incorrect Bonferroni Threshold Calculation**
*   **Section:** VII A, p. 9
*   **Problem:** The paper calculates a Bonferroni threshold for a Phase 2 sweep with `K=9` tests at `α=0.05`, claiming `|σ|_Bonf,9 ≈ 3.02`. My recalculation using the standard formula (`sqrt(2) * erfc^-1(α/K)`) yields `|σ|_Bonf,9 ≈ 2.77`. This is a non-trivial difference in a statistical threshold.
*   **Required Fix:** The author must re-calculate the Bonferroni threshold and correct the value in the text.

**P5-M3: Inconsistent Concordance Value**
*   **Section:** IX A (p. 14) and Figure 7 (p. 16)
*   **Problem:** The text and Figure 7 caption claim a "filament-class concordance" of `0.026 pp` between the Tempel+ and V-Web classifiers. However, the `fcw` values given in Table II (`0.4980` for V-Web filament) and Table XI (`0.4982` for Tempel filament_like) have a difference of `0.0002`, which is `0.02 pp`. The value `0.026 pp` appears to be a persistent typo.
*   **Required Fix:** Correct this value in the text (e.g., Abstract, p. 14) and in the caption of Figure 7.

### MINOR Revisions

**P5-m1: Ambiguous Uncertainty Quoted in Abstract**
*   **Section:** Abstract, p. 1
*   **Problem:** The abstract states the statistical uncertainty for the V-Web void bin is `~5pp`. This is confusing. The 1σ statistical error (`sqrt(p(1-p)/n)`) is ~2.4pp. A 2σ interval would span ~9.6pp. The source of the `~5pp` figure is unclear and potentially misleading.
*   **Required Fix:** Clarify this statement. It is better to quote the 1σ error or a standard confidence interval (e.g., 95% CI).

**P5-m2: Inconsistent Precision in Abstract**
*   **Section:** Abstract, p. 1
*   **Problem:** The abstract quotes the monopole offset as `~0.2pp`, while the body consistently uses the more precise `0.26pp` (from `Δfcw = -0.0026`). Given the precision of the rest of the abstract, the more precise value should be used.
*   **Required Fix:** Change `~0.2pp` to `0.26pp` in the abstract.

**P5-m3: Uncertainty on Monopole Offset**
*   **Section:** Throughout, e.g., Section V (p. 4)
*   **Problem:** The analysis treats the monopole offset `Δfcw = -0.0026` from Paper IV as a fixed, perfectly known value when calculating `σ_pred` and residuals. However, this value must have its own uncertainty (`±0.000279` as implied on p. 2). This uncertainty is not propagated into the analysis of the environmental dependence.
*   **Required Fix:** The author should acknowledge this and briefly discuss how the uncertainty on `Δfcw` would affect the `σ_vs_monopole` residuals. For example, it would add a systematic error floor to the comparison.

### NITs

**P5-N1: Informal Statistical Language**
*   **Section:** p. 2
*   **Problem:** The text uses phrases like `|z| ≈ 3.4σ`. While common, using `σ` as a unit for a z-score is informal.
*   **Required Fix:** Consider rephrasing to "a z-score of approximately 3.4". This is a stylistic suggestion.

## Summary recommendation

**MAJOR REVISIONS**

This paper presents a valuable and thorough null result on an interesting cosmological question. The breadth of the robustness checks is commendable, and the core conclusion appears to be sound, pending verification of the calculations. However, the manuscript is currently unacceptable for publication due to several essential errors, including a fundamental misstatement of the input signal from its source paper, impossible sample size reporting, sign errors in a key table, and an unacceptable reliance on unpublished and future-dated work.

The paper can be reconsidered for publication after the author has:
1.  Made the source catalog and methods of "Paper IV" publicly available.
2.  Corrected all identified numerical, logical, and sign errors.
3.  Updated all references to reflect their actual publication status at the time of resubmission.

Given the extensive and serious nature of these required corrections, the manuscript must undergo a full re-review upon resubmission.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated review, incorporating the findings from the second, more rigorous pass.

================================================================
## Referee Report on "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals"

This paper presents a detailed investigation into the potential dependence of spiral galaxy chirality on large-scale structure environment, using data from DESI DR1 cross-matched with a new, large-scale chirality catalog. The primary method involves classifying galaxies into cosmic-web environments (void, wall, filament, cluster) and testing for variations in the clockwise (CW) fraction. The author performs an extensive set of null tests and robustness checks, including using multiple environment finders (V-Web, DESIVAST, Tempel+ FoF, ASTRA), and stratifying the data by redshift, density, sky position, and galaxy type. The main conclusion is a null result: after accounting for a small, catalog-wide systematic offset (monopole), no significant evidence for an environment-dependent chirality signal is found at the sensitivity of the current data.

The analysis is comprehensive and the author demonstrates a strong command of potential observational systematics. The multi-layered approach to robustness, particularly the primary analysis anchored on the peer-reviewed DESIVAST void catalog, is a significant strength. However, the manuscript in its current form contains several essential errors, inconsistencies, and questionable scientific practices that preclude its publication in Physical Review D without substantial revision. A second, more detailed review has revealed additional errors of a similar nature, suggesting a systemic lack of care in the manuscript's preparation.

### ESSENTIAL Revisions

**P5-E1: Reliance on Unpublished, Un-reviewed Primary Data Source**
*   **Section:** Throughout, e.g., Abstract (p. 1), Section II (p. 2)
*   **Problem:** The entire analysis is predicated on the galaxy chirality catalog from "Paper IV [3]", which is repeatedly described as a "companion work, not yet peer-reviewed" and "in preparation". A manuscript submitted for publication cannot be fundamentally dependent on data and core results (like the monopole offset) from a source that is not publicly available or has not undergone any peer review. This prevents the reader and reviewer from verifying the most basic inputs to the present analysis.
*   **Required Fix:** Paper IV must be made publicly available, at a minimum as a preprint on a service like arXiv, before this manuscript can be seriously considered for publication. The reference [3] must be updated to point to this public version.

**P5-E2: Fundamental Misstatement of Input Parity Violation Signal**
*   **Section:** II, p. 2
*   **Problem:** The text states: "Paper IV [3] ... establishes the global mixture in the post-test-time-augmentation equivariant classifier as a CW fraction of 0.4974 ± 0.000279, consistent with parity at ~1σ." This is incorrect. A deviation of `(0.4974 - 0.5)` with an uncertainty of `0.000279` corresponds to a `( -0.0026 / 0.000279) ≈ 9.3σ` deviation from parity. This is a highly significant inconsistency, not a `~1σ` one. The author likely confuses the monopole measurement with the dipole measurement (which is later quoted as a null result). This sentence, as written, fundamentally misrepresents the starting point of the analysis.
*   **Required Fix:** The sentence must be rewritten to accurately reflect the statistical significance of the monopole. For example: "...a CW fraction of 0.4974 ± 0.000279, which represents a ~9.3σ deviation from a perfect parity-symmetric mixture. Paper IV argues this offset is a classifier-level systematic bias (monopole), not a cosmological signal."

**P5-E3: Inconsistent and Impossible Sample Sizes**
*   **Section:** VI D, subsection c, p. 7
*   **Problem:** The text reports results for a "filament-class tracer-program decomposition". It quotes a sample size of `n = 21,203` for "filament dark". However, in the preceding subsection (b), the total "dark" sample (LRG, ELG, QSO) across all environments is given as `n = 14,782`. It is impossible for a subset (dark galaxies in filaments) to be larger than the total set.
*   **Required Fix:** The author must find the source of this error and report the correct sample sizes. All associated calculations must be verified with the corrected numbers.

**P5-E4: Incorrect Signs in Key Results Table**
*   **Section:** VIII, Table VIII, p. 12
*   **Problem:** The `Δfcw` column in Table VIII reports the difference in CW fraction between void and non-void galaxies for three different DESIVAST algorithms. Re-calculating these values from the `f_void` and `f_non-void` columns reveals that all three signs in the `Δfcw` column are incorrect.
    *   VoidFinder: `0.4964 - 0.4971 = -0.0007` (Table says `+0.0007`)
    *   V2-REVOLVER: `0.4986 - 0.4967 = +0.0019` (Table says `-0.0019`)
    *   V2-VIDE: `0.4971 - 0.4970 = +0.0001` (Table says `-0.0001`)
    This level of carelessness in a central results table is unacceptable.
*   **Required Fix:** Correct the signs in the `Δfcw` column of Table VIII.

**P5-E5: Use of Future-Dated and "In Preparation" References**
*   **Section:** Throughout, e.g., p. 1, p. 10, p. 15, p. 20
*   **Problem:** The paper is dated "June 2026". Several key references are cited with future years (e.g., Rincón et al. 2025 [13], Ullah et al. 2026 [11], Zapata-Zuluaga et al. 2026 [12]). Others are "in preparation" ([3], [4]). This is not standard academic practice. A submitted paper must rely on the existing, verifiable body of literature at the time of submission.
*   **Required Fix:** The date of the paper must be corrected to the submission date. All references must be updated to their current, correct status (e.g., "ApJ, in press", "arXiv:xxxx.xxxxx", etc.). If a source is not yet public, it cannot be a load-bearing citation.

**P5-E6: Incorrect Sign in Abstract's Primary Robustness Result**
*   **Section:** Abstract, p. 1
*   **Problem:** The abstract states that the DESIVAST-anchored re-projection yields `Δfcw = 0.0007`. However, the data in Table VII (`f_void = 0.4964`, `f_non-void = 0.4971`) show the difference is `0.4964 - 0.4971 = -0.0007`. This sign error misrepresents a key robustness check in the abstract.
*   **Required Fix:** Correct the sign of this value in the abstract.

**P5-E7: Sign Errors in Residuals Table**
*   **Section:** VI C, Table III, p. 6
*   **Problem:** The final column of Table III reports the residual `σ_obs - σ_pred`. Re-calculating these values reveals two sign errors:
    *   Quintile 3: `-3.94 - (-2.07) = -1.87` (Table says `1.87`)
    *   Quintile 4: `-3.08 - (-2.07) = -1.01` (Table says `1.01`)
    The column header `|σ_obs - σ_pred|` is also inconsistent with the signed values presented.
*   **Required Fix:** Correct the signs for Quintiles 3 and 4. Clarify the column header (e.g., remove the absolute value bars).

**P5-E8: Contradictory Summary of Main Result**
*   **Section:** XII C, p. 17
*   **Problem:** In the discussion comparing to prior work, the text states the "per-environment CW fractions sit at ~0.497 with range ~0.2 percentage points across the four V-Web classes". This is a factor-of-10 error. The abstract, body, and conclusion correctly state the range is `1.98` percentage points. This misstatement fundamentally downplays the observed variance.
*   **Required Fix:** Correct this value from `~0.2 pp` to the correct `~1.98 pp`.

### MAJOR Revisions

**P5-M1: Inconsistent Calculation of Predicted Sigma**
*   **Section:** VI A, p. 6
*   **Problem:** The paper predicts the expected sigma deviation due to the monopole for the filament class: `σ_pred(filament) ≈ -3.16`. However, a direct calculation using the provided formula (`σ_pred = 2 * Δfcw * √N`) with `Δfcw = -0.0026` and `N = 408,187` yields `σ_pred ≈ -3.32`. This is a ~5% discrepancy. Furthermore, the text claims this is "within order-unity" of the observed `σ_obs = -2.61`, but the residual is `~0.7σ`, which is not negligible. The prediction for the cluster class, however, is correct.
*   **Required Fix:** The author must verify this calculation and correct the text. The interpretation of the residual should be revisited if the discrepancy remains.

**P5-M2: Incorrect Bonferroni Threshold Calculation**
*   **Section:** VII A, p. 9
*   **Problem:** The paper calculates a Bonferroni threshold for a Phase 2 sweep with `K=9` tests at `α=0.05`, claiming `|σ|_Bonf,9 ≈ 3.02`. My recalculation using the standard formula (`sqrt(2) * erfc^-1(α/K)`) yields `|σ|_Bonf,9 ≈ 2.77`. This is a non-trivial difference in a statistical threshold.
*   **Required Fix:** The author must re-calculate the Bonferroni threshold and correct the value in the text.

**P5-M3: Inconsistent Concordance Value**
*   **Section:** IX A (p. 14) and Figure 7 (p. 16)
*   **Problem:** The text and Figure 7 caption claim a "filament-class concordance" of `0.026 pp` between the Tempel+ and V-Web classifiers. However, the `fcw` values given in Table II (`0.4980` for V-Web filament) and Table XI (`0.4982` for Tempel filament_like) have a difference of `0.0002`, which is `0.02 pp`. The value `0.026 pp` appears to be a persistent typo.
*   **Required Fix:** Correct this value in the text (e.g., Abstract, p. 14) and in the caption of Figure 7.

**P5-M4: Incorrect Internal Cross-Reference in Abstract**
*   **Section:** Abstract, p. 1
*   **Problem:** The abstract's discussion of the DESIVAST-anchored re-projection refers to "§IX B" for the `Δfcw` result. This result is derived and presented in §VIII B and Table VII.
*   **Required Fix:** Correct the cross-reference to point to §VIII B.

**P5-M5: Dangling Internal Cross-Reference**
*   **Section:** I, p. 2
*   **Problem:** The introduction refers to a "bounce-chirality coupling class (Sec. II)". Section II, "Relation to Paper IV", does not define or discuss this concept.
*   **Required Fix:** Either add the relevant discussion to Section II or remove/correct the reference.

### MINOR Revisions

**P5-m1: Ambiguous Uncertainty Quoted in Abstract**
*   **Section:** Abstract, p. 1
*   **Problem:** The abstract states the statistical uncertainty for the V-Web void bin is `~5pp`. This is confusing. The 1σ statistical error (`sqrt(p(1-p)/n)`) is ~2.4pp. A 2σ interval would span ~9.6pp. The source of the `~5pp` figure is unclear and potentially misleading.
*   **Required Fix:** Clarify this statement. It is better to quote the 1σ error or a standard confidence interval (e.g., 95% CI).

**P5-m2: Inconsistent Precision in Abstract**
*   **Section:** Abstract, p. 1
*   **Problem:** The abstract quotes the monopole offset as `~0.2pp`, while the body consistently uses the more precise `0.26pp` (from `Δfcw = -0.0026`). Given the precision of the rest of the abstract, the more precise value should be used.
*   **Required Fix:** Change `~0.2pp` to `0.26pp` in the abstract.

**P5-m3: Uncertainty on Monopole Offset**
*   **Section:** Throughout, e.g., Section V (p. 4)
*   **Problem:** The analysis treats the monopole offset `Δfcw = -0.0026` from Paper IV as a fixed, perfectly known value when calculating `σ_pred` and residuals. However, this value must have its own uncertainty (`±0.000279` as implied on p. 2). This uncertainty is not propagated into the analysis of the environmental dependence.
*   **Required Fix:** The author should acknowledge this and briefly discuss how the uncertainty on `Δfcw` would affect the `σ_vs_monopole` residuals. For example, it would add a systematic error floor to the comparison.

### NITs

**P5-N1: Informal Statistical Language**
*   **Section:** p. 2
*   **Problem:** The text uses phrases like `|z| ≈ 3.4σ`. While common, using `σ` as a unit for a z-score is informal.
*   **Required Fix:** Consider rephrasing to "a z-score of approximately 3.4". This is a stylistic suggestion.

## Summary recommendation

**MAJOR REVISIONS**

This paper presents a valuable and thorough null result on an interesting cosmological question. The breadth of the robustness checks is commendable, and the core conclusion appears to be sound, pending verification of the calculations. However, the manuscript is currently unacceptable for publication due to a large number of essential errors. These include a fundamental misstatement of the input signal from its source paper, impossible sample size reporting, a pattern of sign errors in key tables and the abstract, major numerical contradictions, and an unacceptable reliance on unpublished and future-dated work. The prevalence of these issues suggests the manuscript was not carefully checked before submission.

The paper can be reconsidered for publication after the author has:
1.  Made the source catalog and methods of "Paper IV" publicly available.
2.  Corrected all identified numerical, logical, and sign errors.
3.  Updated all references to reflect their actual publication status at the time of resubmission.
4.  Performed a thorough internal review of all numbers, claims, and cross-references in the manuscript.

Given the extensive and serious nature of these required corrections, the manuscript must undergo a full re-review upon resubmission.