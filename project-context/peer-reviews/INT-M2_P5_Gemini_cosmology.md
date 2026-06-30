# P5 INT-M2 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` md5=503d4e5b pages=34
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (11835 chars)
**Wall time**: 140.6s

---

## Referee Report on "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample"

This paper presents a detailed investigation into the potential dependence of spiral galaxy chirality on large-scale structure environment, using data from the DESI Data Release 1. The authors perform two main analyses: a "secondary" test using a T-Web tidal-tensor classifier on a large sample of ~784k spirals, and a "primary" test focusing on a ~57k spiral sample within voids identified by the DESIVAST catalog. The headline result is a null detection of any environmental dependence, with observed variations in the clockwise (CW) fraction being consistent with a previously identified catalog-wide systematic monopole and statistical counting noise. The analysis is exceptionally thorough, with an extensive suite of robustness checks, systematic tests, and cross-validations against other classifiers and methodologies.

The work is of high quality and the statistical treatment is rigorous. The authors are commendably transparent about potential issues, such as the post-hoc designation of the primary analysis path and the presence of systematics related to survey selection functions. The paper's main conclusion—that there is no evidence for environment-dependent chirality at the sensitivity of DESI DR1—is well-supported by the presented evidence.

However, there are several issues that must be addressed before the paper can be considered for publication in Physical Review D. The most critical of these is the reliance on an "in preparation" companion paper for the core data inputs and systematic corrections.

### Summary of Findings

**ESSENTIAL (1):**
-   **P5-E1:** The paper is not self-contained due to its critical dependence on an unpublished companion paper ("Paper IV") for its primary data (chirality labels) and its main systematic correction (the classifier monopole).

**MAJOR (2):**
-   **P5-M1:** The abstract presents a list of raw, sample-size-dependent σ-values that the main text explicitly and correctly states are not mutually comparable, which is misleading.
-   **P5-M2:** The paper's length (34 pages) is excessive for a null-result measurement paper, potentially obscuring the main, high-impact findings.

**MINOR (1):**
-   **P5-m1:** The publication date is set to the future (June 28, 2026), which should be corrected.

---
### Detailed Findings

#### ESSENTIAL

**P5-E1: Critical dependence on an unpublished companion paper**
-   **Section:** Throughout, starting with Abstract (p. 1) and most explicitly in Sec. II (p. 3) and Sec. III.A (p. 4).
-   **Problem:** The analysis fundamentally relies on two inputs from "Paper IV [3] (in preparation)": (1) the per-galaxy chirality labels (`class_eq`), and (2) the value of the catalog-wide classifier-monopole offset (`Afcw = -0.0026`), which is the primary systematic the paper corrects for. A core principle of scientific publication is that a paper must be self-contained and its results verifiable. As Paper IV is not available on a preprint server or otherwise published, it is impossible for a referee or reader to assess the validity of the input catalog or the derivation of the key systematic. While Table I provides a summary, it is not a substitute for a methodological description of the classifier architecture, training, validation, and the monopole's discovery and characterization. This makes the present work's claims fundamentally unverifiable.
-   **Required Fix:** The paper cannot be published in its current state. The authors must choose one of two options:
    1.  Wait to submit this manuscript until Paper IV is publicly available (e.g., posted to arXiv).
    2.  Incorporate a new, self-contained appendix into the present manuscript that provides the essential methodological details from Paper IV. This appendix must be sufficient for a reader to understand how the chirality labels were generated and how the monopole offset was derived and validated, without needing to consult the external work.

#### MAJOR

**P5-M1: Misleading presentation of non-comparable statistics in the abstract**
-   **Section:** Abstract (p. 1).
-   **Problem:** The abstract reports per-class CW fractions and their associated σ-deviations from a 50/50 parity null: "0.4980 (filament; n=408,187, -2.61σ), 0.4963 (cluster; n=397,505, -4.66σ), 0.5034 (wall; n=6,673, +0.55σ), and 0.4836 (void; n=428, -0.68σ)". However, the main text correctly states on p. 7 (§V): "Because `σ_from_half` grows as `sqrt(N)` at fixed fractional offset, raw σ values are not comparable across bins of different N; only the monopole-subtracted residuals are." The abstract thus violates the paper's own stated rule of statistical comparison. Presenting these raw σ-values side-by-side invites the reader to incorrectly compare their magnitudes (e.g., to conclude that the cluster signal is "stronger" than the filament one), when the paper's core argument is that these are all just sample-size-weighted projections of the same monopole.
-   **Required Fix:** The abstract should be revised to present statistics that are directly comparable. The authors should replace the list of raw `σ_from_half` values with the monopole-subtracted residuals (`σ_vs_monopole`), as presented in Table XIII (p. 21). For example, the abstract could state that after subtracting the catalog-wide monopole, the residual significance for all four T-Web classes is less than 1.15σ, demonstrating no additional environmental dependence. This would be a more accurate and powerful summary of the paper's finding.

**P5-M2: Excessive length for a null-result paper**
-   **Section:** Entire manuscript.
-   **Problem:** The paper is 34 pages long. While the thoroughness of the cross-checks is a strength, the sheer volume of text and the proliferation of secondary and tertiary tests risk obscuring the primary result. The core findings are contained in the T-Web analysis (Sec. VI), the DESIVAST analysis (Sec. VIII), and the key robustness checks (e.g., Phase 2 sweep, Sec. VII; selection-correction, Sec. IX.A). Many of the other cross-checks (e.g., against Tempel+2014, ASTRA EDR) confirm the null but are based on smaller, less clean, or less relevant samples.
-   **Required Fix:** The authors should consider restructuring the paper to improve clarity and impact. A recommended structure would be:
    1.  A focused main paper (suggested max length: 15-18 pages) that presents the primary DESIVAST result and the main supporting T-Web analysis, including the most critical robustness checks (Phase 2 sweep, sky-position null, density-quintile null, and the redshift-shell selection correction).
    2.  An extensive appendix that contains the less critical cross-validations (Tempel, ASTRA, concurrent literature), detailed tables, and further systematic explorations. This would make the primary argument much easier to follow while still preserving the valuable depth of the authors' investigation for the dedicated reader.

#### MINOR

**P5-m1: Future publication date**
-   **Section:** Title block (p. 1).
-   **Problem:** The paper is dated "June 28, 2026". This is presumably a placeholder.
-   **Required Fix:** Update the date to the current submission date.

---
### Final Assessment

The analytical work in this paper is of a very high standard. The authors have performed a comprehensive and statistically rigorous search for an environmental dependence of spiral chirality. The systematic checks are exemplary, particularly the way the authors trace potential signals back to known survey properties (selection functions, boundary effects) and the classifier's intrinsic monopole. The paper's conclusion is robustly supported.

However, the procedural issue of relying on an unpublished companion paper (P5-E1) is a critical barrier to publication. The misleading presentation of statistics in the abstract (P5-M1) also needs to be rectified.

## Summary recommendation
**MAJOR REVISIONS**

I recommend Major Revisions. The paper is potentially acceptable for publication in Physical Review D, but only after the authors have made the work self-contained by either waiting for the publication of Paper IV or by integrating its essential methods into this manuscript. Furthermore, the abstract must be revised to present statistically comparable quantities, and the authors should strongly consider restructuring the paper to improve its conciseness and impact. Once these issues are addressed, the paper will represent a significant and robust contribution to the field.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated review, incorporating the new findings from the second, more detailed pass.

================================================================
## Referee Report on "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample"

This paper presents a detailed investigation into the potential dependence of spiral galaxy chirality on large-scale structure environment, using data from the DESI Data Release 1. The authors perform two main analyses: a "secondary" test using a T-Web tidal-tensor classifier on a large sample of ~784k spirals, and a "primary" test focusing on a ~57k spiral sample within voids identified by the DESIVAST catalog. The headline result is a null detection of any environmental dependence, with observed variations in the clockwise (CW) fraction being consistent with a previously identified catalog-wide systematic monopole and statistical counting noise. The analysis is exceptionally thorough, with an extensive suite of robustness checks, systematic tests, and cross-validations against other classifiers and methodologies.

The work is of high quality and the statistical treatment is rigorous. The authors are commendably transparent about potential issues, such as the post-hoc designation of the primary analysis path and the presence of systematics related to survey selection functions. The paper's main conclusion—that there is no evidence for environment-dependent chirality at the sensitivity of DESI DR1—is well-supported by the presented evidence.

However, there are several issues that must be addressed before the paper can be considered for publication in Physical Review D. The most critical of these is the reliance on an "in preparation" companion paper for the core data inputs and systematic corrections.

### Summary of Findings

**ESSENTIAL (1):**
-   **P5-E1:** The paper is not self-contained due to its critical dependence on an unpublished companion paper ("Paper IV") for its primary data (chirality labels) and its main systematic correction (the classifier monopole).

**MAJOR (2):**
-   **P5-M1:** The abstract presents a list of raw, sample-size-dependent σ-values that the main text explicitly and correctly states are not mutually comparable, which is misleading.
-   **P5-M2:** The paper's length (34 pages) is excessive for a null-result measurement paper, potentially obscuring the main, high-impact findings.

**MINOR (1):**
-   **P5-m1:** The publication date is set to the future (June 28, 2026), which should be corrected.

**NEW FINDINGS (from second review):**
-   **P5-N1 (Arithmetic):** The monopole-subtracted residuals (`σ_vs_monopole`) in Table XIII contain small but clear arithmetic inconsistencies relative to the input numbers provided.
-   **P5-N2 (Null Procedure Comparability):** Table XV juxtaposes `max|σ|` statistics from different classifiers in a way that is not directly comparable, as the underlying sample sizes differ.
-   **P5-N3 (Appendix vs. Main-Text Mismatch):** The chi-squared value for the T-Web class homogeneity test (3.55) quoted in the main text does not exactly match the value (3.46) calculated from the contingency table in Appendix B.

---
### Detailed Findings

#### ESSENTIAL

**P5-E1: Critical dependence on an unpublished companion paper**
-   **Section:** Throughout, starting with Abstract (p. 1) and most explicitly in Sec. II (p. 3) and Sec. III.A (p. 4).
-   **Problem:** The analysis fundamentally relies on two inputs from "Paper IV [3] (in preparation)": (1) the per-galaxy chirality labels (`class_eq`), and (2) the value of the catalog-wide classifier-monopole offset (`Afcw = -0.0026`), which is the primary systematic the paper corrects for. A core principle of scientific publication is that a paper must be self-contained and its results verifiable. As Paper IV is not available on a preprint server or otherwise published, it is impossible for a referee or reader to assess the validity of the input catalog or the derivation of the key systematic. While Table I provides a summary, it is not a substitute for a methodological description of the classifier architecture, training, validation, and the monopole's discovery and characterization. This makes the present work's claims fundamentally unverifiable.
-   **Required Fix:** The paper cannot be published in its current state. The authors must choose one of two options:
    1.  Wait to submit this manuscript until Paper IV is publicly available (e.g., posted to arXiv).
    2.  Incorporate a new, self-contained appendix into the present manuscript that provides the essential methodological details from Paper IV. This appendix must be sufficient for a reader to understand how the chirality labels were generated and how the monopole offset was derived and validated, without needing to consult the external work.

#### MAJOR

**P5-M1: Misleading presentation of non-comparable statistics in the abstract**
-   **Section:** Abstract (p. 1).
-   **Problem:** The abstract reports per-class CW fractions and their associated σ-deviations from a 50/50 parity null: "0.4980 (filament; n=408,187, -2.61σ), 0.4963 (cluster; n=397,505, -4.66σ), 0.5034 (wall; n=6,673, +0.55σ), and 0.4836 (void; n=428, -0.68σ)". However, the main text correctly states on p. 7 (§V): "Because `σ_from_half` grows as `sqrt(N)` at fixed fractional offset, raw σ values are not comparable across bins of different N; only the monopole-subtracted residuals are." The abstract thus violates the paper's own stated rule of statistical comparison. Presenting these raw σ-values side-by-side invites the reader to incorrectly compare their magnitudes (e.g., to conclude that the cluster signal is "stronger" than the filament one), when the paper's core argument is that these are all just sample-size-weighted projections of the same monopole.
-   **Required Fix:** The abstract should be revised to present statistics that are directly comparable. The authors should replace the list of raw `σ_from_half` values with the monopole-subtracted residuals (`σ_vs_monopole`), as presented in Table XIII (p. 21). For example, the abstract could state that after subtracting the catalog-wide monopole, the residual significance for all four T-Web classes is less than 1.15σ, demonstrating no additional environmental dependence. This would be a more accurate and powerful summary of the paper's finding.

**P5-M2: Excessive length for a null-result paper**
-   **Section:** Entire manuscript.
-   **Problem:** The paper is 34 pages long. While the thoroughness of the cross-checks is a strength, the sheer volume of text and the proliferation of secondary and tertiary tests risk obscuring the primary result. The core findings are contained in the T-Web analysis (Sec. VI), the DESIVAST analysis (Sec. VIII), and the key robustness checks (e.g., Phase 2 sweep, Sec. VII; selection-correction, Sec. IX.A). Many of the other cross-checks (e.g., against Tempel+2014, ASTRA EDR) confirm the null but are based on smaller, less clean, or less relevant samples.
-   **Required Fix:** The authors should consider restructuring the paper to improve clarity and impact. A recommended structure would be:
    1.  A focused main paper (suggested max length: 15-18 pages) that presents the primary DESIVAST result and the main supporting T-Web analysis, including the most critical robustness checks (Phase 2 sweep, sky-position null, density-quintile null, and the redshift-shell selection correction).
    2.  An extensive appendix that contains the less critical cross-validations (Tempel, ASTRA, concurrent literature), detailed tables, and further systematic explorations. This would make the primary argument much easier to follow while still preserving the valuable depth of the authors' investigation for the dedicated reader.

#### MINOR

**P5-m1: Future publication date**
-   **Section:** Title block (p. 1).
-   **Problem:** The paper is dated "June 28, 2026". This is presumably a placeholder.
-   **Required Fix:** Update the date to the current submission date.

---
### NEW FINDINGS (from second, detailed review)

The following are less critical than the points above but should be addressed to ensure the paper's numerical accuracy and clarity.

**P5-N1: Arithmetic inconsistencies in Table XIII**
-   **Section:** Table XIII (p. 21).
-   **Problem:** The `σ_vs_monopole` column, which is central to the paper's argument about monopole subtraction, contains values that are arithmetically inconsistent with the other columns (`n`, `fcw - f_P5`) and the stated definition. For example, for the filament class, the calculated residual is +1.02σ, while the table reports +0.99σ. For the cluster class, the calculated residual is -1.13σ, while the table reports -1.11σ.
-   **Required Fix:** Please re-calculate all values in the `σ_vs_monopole` column of Table XIII and correct any discrepancies.

**P5-N2: Incomparable statistics in Table XV**
-   **Section:** Table XV (p. 28).
-   **Problem:** This table reports the `max|σ|` for three different classifiers on the EDR overlap sample. However, the class populations (`n`) differ significantly between classifiers. The maximum sigma for one classifier might come from a class with n~17k, while for another it might come from a class with n~3k. As the paper correctly argues elsewhere, these raw sigma values are not comparable.
-   **Required Fix:** While the main conclusion (no class exceeds the Bonferroni threshold) is the correct one to draw, the authors should consider removing the `max|σ|` column to avoid misleading juxtaposition, or add a footnote explicitly stating that these values are not mutually comparable.

**P5-N3: Chi-squared value mismatch**
-   **Section:** §VI.A (p. 8) and Appendix B (p. 31).
-   **Problem:** The main text quotes a Pearson chi-squared value of `χ² = 3.55` for the T-Web class homogeneity test. However, a direct recalculation from the integer counts provided in the contingency table (Table XVII) in Appendix B yields `χ² = 3.46`. While this difference does not affect the null conclusion (the p-value changes from 0.31 to 0.33), the inconsistency should be resolved.
-   **Required Fix:** Please verify the chi-squared calculation and ensure the value reported in the main text is consistent with the data in the appendix table.

---
### Final Assessment

The analytical work in this paper is of a very high standard. The authors have performed a comprehensive and statistically rigorous search for an environmental dependence of spiral chirality. The systematic checks are exemplary, particularly the way the authors trace potential signals back to known survey properties (selection functions, boundary effects) and the classifier's intrinsic monopole. The paper's conclusion is robustly supported.

However, the procedural issue of relying on an unpublished companion paper (P5-E1) is a critical barrier to publication. The misleading presentation of statistics in the abstract (P5-M1) also needs to be rectified.

## Summary recommendation
**MAJOR REVISIONS**

I recommend Major Revisions. The paper is potentially acceptable for publication in Physical Review D, but only after the authors have made the work self-contained by either waiting for the publication of Paper IV or by integrating its essential methods into this manuscript. Furthermore, the abstract must be revised to present statistically comparable quantities, and the authors should strongly consider restructuring the paper to improve its conciseness and impact. Finally, the minor numerical inconsistencies identified in the second review should be corrected. Once these issues are addressed, the paper will represent a significant and robust contribution to the field.