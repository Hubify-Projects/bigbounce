# P5 auto-2026-06-09_1042pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 154.5s

---

## Referee Report on "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across 791,635 DR1 Matched Spirals"

This manuscript presents a detailed investigation into the potential dependence of spiral galaxy chirality on the large-scale structure environment, using data from the DESI Data Release 1 and a pre-existing chirality catalog. The authors perform a primary analysis using the V-Web tidal-tensor classifier to assign galaxies to cosmic-web environments {void, wall, filament, cluster} and test for variations in the clockwise (CW) fraction. The headline result is a null detection of environmental dependence, with observed variations being consistent with a previously reported catalog-wide monopole offset. The analysis is supported by an extensive set of robustness checks, including a sensitivity sweep of classifier parameters, null tests against redshift and density, and cross-validation against other environment finders (Tempel+2014 FoF, ASTRA) and a dedicated void catalog (DESIVAST).

The work is comprehensive and the number of systematic checks is impressive. The authors are careful to distinguish between their primary and secondary analysis paths and to properly account for statistical look-elsewhere effects. However, the manuscript in its current form contains several critical errors and relies on unverifiable inputs, which prevent it from being considered for publication in Physical Review D without substantial revision.

### ESSENTIAL Revisions

**P5-E1: Critical Errors in Primary Robustness Results (Table VIII)**
*   **Location:** Section VIII C, Page 12, Table VIII.
*   **Problem:** The signs of the key result, `Afcw` (defined as `f_void - f_non-void`), are incorrect for all three void-finding algorithms presented. My recalculations from the provided `f_void` and `f_non-void` values are:
    *   VoidFinder: `0.4964 - 0.4971 = -0.0007`. The table reports `+0.0007`.
    *   V2-REVOLVER: `0.4986 - 0.4967 = +0.0019`. The table reports `-0.0019`.
    *   V2-VIDE: `0.4971 - 0.4970 = +0.0001`. The table reports `-0.0001`.
    This is a fundamental error in the presentation of one of the paper's main robustness checks. The conclusion that `|Afcw| < 0.002` remains valid, but the errors undermine confidence in the analysis.
*   **Required Fix:** Correct all values in the `Afcw` column of Table VIII.

**P5-E2: Incorrect Value in Abstract**
*   **Location:** Abstract, Page 1.
*   **Problem:** The abstract states for the DESIVAST re-projection: "...returns `f_void = 0.4964` vs `f_non-void = 0.4971`, `Afcw = 0.0007`...". As established in P5-E1, the difference is `-0.0007`. The sign is incorrect in the abstract.
*   **Required Fix:** Correct the sign of `Afcw` in the abstract to `-0.0007`.

**P5-E3: Unacceptable Manuscript and Reference Dating**
*   **Location:** Page 1, and Bibliography (Page 20).
*   **Problem:** The manuscript is dated "June 2026". It proceeds to cite multiple references as published or preprinted in 2025 and 2026 (e.g., Rincón et al. 2025 [13], Ullah et al. 2026 [11], Zapata-Zuluaga et al. 2026 [12]). This is not permissible. Manuscripts must reflect the current date and cite works that are publicly available at the time of submission.
*   **Required Fix:** The manuscript date must be updated to the submission date. All references must be updated to their correct, current publication status. If these works are not yet public, they must be cited as "private communication" or "in preparation" and the current manuscript's claims cannot depend critically on their specific, unpublished results.

**P5-E4: Over-reliance on Unpublished Companion Work**
*   **Location:** Throughout the paper, starting with the Abstract and Introduction (e.g., reference [3]).
*   **Problem:** The entire analysis is predicated on the galaxy chirality catalog and the catalog-wide monopole offset (`Afcw = -0.0026`) from "Paper IV," which is cited as a "companion work, not yet peer-reviewed" and "in preparation." A result as sensitive as a null test for parity violation cannot be founded on an unverified, unavailable input catalog and its unpublished systematics analysis. The present manuscript is not self-contained and its results are not verifiable.
*   **Required Fix:** The methodology for the chirality classification and the derivation of the monopole offset must be sufficiently detailed within this manuscript (e.g., in an appendix) to make the current work self-contained and its results reproducible. Alternatively, publication of the present manuscript must wait until Paper IV has been accepted for publication in a peer-reviewed journal.

### MAJOR Revisions

**P5-M1: Dismissal of a >3σ Signal**
*   **Location:** Abstract (Page 1), Section VI D c (Page 7), and Section VIII (Page 8).
*   **Problem:** The analysis finds a statistically significant (`|z| ≈ 3.40`) sign-flip in the CW fraction between the bright and dark galaxy samples within the V-Web filament class. The authors argue this is a systematic effect related to the BGS selection function and pivot to the DESIVAST analysis as their primary, cleaner result. While this interpretation is plausible, dismissing a >3σ effect as a systematic requires a very high burden of proof. The current argument rests on a contingency test showing that V-Web class and target program are not independent (`p < 10^-1000`), but it does not demonstrate a clear mechanism by which this dependence generates a sign-flip of this magnitude.
*   **Required Fix:** Strengthen the argument for the systematic origin of the 3.4σ signal. This could involve, for example, a more detailed analysis showing how the specific properties of the BGS-bright selection function (e.g., imaging-leg dependencies) correlate with the V-Web filament environment to produce this effect. The current explanation is suggestive but not conclusive. The paper's headline conclusion of "no environment dependence" is weakened by the presence of this unexplained, significant signal.

### MINOR Revisions

**P5-m1: Numerical Discrepancy in Density Quintile Analysis**
*   **Location:** Section VI C, Page 6, Table III.
*   **Problem:** My recalculation of the `sigma_obs` values for the density quintiles, assuming N=158,327 per bin, yields slightly different results (e.g., -1.85 for Q1 vs. -1.94 in the table). This may be due to small variations in the number of galaxies per quintile.
*   **Required Fix:** Please verify the `sigma_obs` values in Table III. If the quintiles are not of exactly equal size, please state the N for each quintile.

**P5-m2: Inconsistent Samples in Cross-Validation**
*   **Location:** Section IX A, Page 13.
*   **Problem:** The "filament concordance" between the V-Web and Tempel+2014 classifiers compares the `fcw` from the full V-Web filament sample (n=408,187) to the `fcw` from the Tempel filament-like sample on the much smaller overlap subsample (n=14,317). A direct, like-for-like comparison would require computing the V-Web `fcw` on the same overlap subsample.
*   **Required Fix:** For a more robust comparison, compute and report the V-Web class `fcw` values on the 110,586-galaxy overlap sample and compare those directly to the Tempel+2014 results on that same sample.

**P5-m3: Inconsistent Precision in Abstract**
*   **Location:** Abstract, Page 1.
*   **Problem:** The abstract states the DESI DR1 redshift catalog has "16.4 x 10^6 ZWARN=0 input rows," while Table I gives the more precise number 16,361,731.
*   **Required Fix:** Use the more precise number from the analysis in the abstract or use consistent rounding (e.g., "~16.4 million").

### NITs (Cosmetic)

**P5-N1: Definition of "pp"**
*   **Location:** Abstract and throughout.
*   **Problem:** The abbreviation "pp" is used for "percentage points."
*   **Required Fix:** While its meaning is clear from context, it would be good practice to define it on first use for clarity.

**P5-N2: Terminology for Multiple Comparisons Correction**
*   **Location:** Abstract and Section V A.
*   **Problem:** The paper uses the term "look-elsewhere correction." This term is typically reserved for searches over a continuous parameter space. The corrections applied here (Bonferroni, max-stat Monte Carlo) are more accurately described as corrections for multiple comparisons or multiple testing.
*   **Required Fix:** Consider replacing "look-elsewhere correction" with "correction for multiple comparisons" for greater precision.

## Summary recommendation
**MAJOR REVISIONS**

The paper presents a very thorough and statistically sophisticated search for an environmental dependence of spiral chirality. The breadth of the cross-checks and null tests is a significant strength. However, the manuscript is marred by several essential-level flaws, including incorrect signs in key results (Table VIII and abstract), unacceptable future-dating of the manuscript and its references, and a critical dependency on an unpublished and unavailable companion paper (Paper IV). These issues make the work unverifiable in its current state. Furthermore, the dismissal of a 3.4σ signal as a systematic requires a more compelling demonstration.

Despite these serious problems, the underlying analysis appears to be of high quality and the topic is of interest. Therefore, I recommend Major Revisions. The authors must correct the numerical errors, fix the dating and referencing issues, and make the analysis self-contained by providing the necessary details from Paper IV. They must also substantially strengthen their argument regarding the 3.4σ filament-class signal. If these points are addressed satisfactorily, the paper could become a valuable contribution to the literature.