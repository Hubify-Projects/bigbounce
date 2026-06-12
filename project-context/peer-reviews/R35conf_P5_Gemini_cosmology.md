# P5 R35conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.68.pdf` md5=8f7957f4 pages=31
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (3018 chars)
**Wall time**: 191.6s

---

Here is a complete referee report for the submitted manuscript.

***

## Referee Report: "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across 791,635 DR1 Matched Spirals"

This manuscript presents a detailed statistical analysis searching for a correlation between the chirality (handedness) of spiral galaxies and their large-scale structure environment, using data from the DESI Data Release 1. The primary analysis path is a cross-match between a new 8.5M-galaxy chirality catalog (from a companion paper, "Paper IV") and the DESIVAST void catalog. This is supported by a secondary analysis using a V-Web tidal-tensor cosmic-web classifier run on the full DESI DR1 spectroscopic sample. The author performs an extensive suite of null tests and robustness checks, including sensitivity to classifier hyperparameters, redshift, projected density, sky position, and target selection program. The main conclusion is a null result: no statistically significant evidence for environment-dependent chirality is found, beyond a known, small, catalog-wide systematic monopole offset in the chirality classifier.

The paper is exceptionally thorough in its methodology, statistical treatment, and exploration of potential systematic effects. The transparency regarding post-hoc analysis choices, corrections of errors from previous internal drafts, and explicit statement of limitations is commendable and sets a high standard for reproducibility and rigor. The primary result, anchored on the peer-reviewed DESIVAST void catalog, is robustly established.

However, there are several issues that must be addressed before the paper can be considered for publication in Physical Review D. The most critical is the heavy reliance on an unpublished, non-peer-reviewed companion paper for essential inputs.

### ESSENTIAL Revisions

**P5-E1: Reliance on Unpublished Companion Paper**
*   **Section:** Throughout, starting with Abstract (p. 1) and II (p. 3).
*   **Problem:** The entire analysis is predicated on the galaxy chirality labels and the catalog-wide "classifier-monopole systematic" (Δfcw ≈ -0.0026) derived in "Paper IV [3] (companion work, not yet peer-reviewed)". A core principle of peer review is that a manuscript must be self-contained and its claims verifiable. Basing the primary analysis of this paper on inputs and systematic corrections from an unpublished work is not acceptable. The reader cannot assess the validity of the chirality labels or the justification for treating the monopole as a correctable systematic without access to the peer-reviewed Paper IV.
*   **Required Fix:** The paper cannot be published in its current state. The author must choose one of two paths:
    1.  Wait for Paper IV to be accepted for publication and update the citation accordingly.
    2.  Make the present manuscript self-contained. This would require adding a new section or appendix that summarizes the essential methods of Paper IV, including: the classifier architecture, the training and validation process, the test-time augmentation procedure, and the evidence supporting the conclusion that the -0.26 pp offset is a classifier systematic rather than a cosmological signal.

### MAJOR Revisions

**P5-M1: Sign Errors in Key Robustness Claims**
*   **Section:** Robustness (p. 2).
*   **Problem:** The dense "Robustness" section on page 2 contains at least two sign errors in its summary of key results, which undermines confidence in the summary.
    1.  `"returns f_cw^void = 0.4964 vs f_cw^non-void = 0.4971, Δfcw = f_cw^void – f_cw^non-void = +0.0007"`
        The calculation `0.4964 - 0.4971` yields **-0.0007**, not +0.0007.
    2.  `"V2-REVOLVER catalog-native Δ = -0.0037"`
        The body text in §VIII D (p. 18) gives `f_void = 0.4992` and `f_non-void = 0.4955` for this sample. The stated sign convention for this contrast is `Δfcw = f_void - f_non-void`. The calculation `0.4992 - 0.4955` yields **+0.0037**, not -0.0037.
*   **Required Fix:** Carefully re-verify every number and sign convention in the "Robustness" summary on page 2. This section is nearly as dense as the abstract and must be flawless. Consider moving this detailed summary from the introduction to a dedicated summary table in the results or an appendix to improve readability.

**P5-M2: Confusing Statistical Formula and Threshold Derivation**
*   **Section:** V.A Look-elsewhere (LEE) correction (p. 6).
*   **Problem:** The derivation of the Bonferroni-corrected significance threshold is confusing. Equation (2) for `|σ|_Bonf` uses `erfc⁻¹`, which is typically related to one-sided tail probabilities. However, the subsequent calculations (e.g., `|σ|_Bonf ≈ 3.09` for K=5, α=0.01) correspond to a two-sided test. A reader attempting to reproduce the threshold from the given formula would be confused.
*   **Required Fix:** Clarify the statistical formula. Either correct Eq. (2) to be explicitly for a two-sided test (e.g., by using `α/(2K)` in the argument) or, more simply, define the threshold using the inverse of the standard normal cumulative distribution function, `Φ⁻¹(1 - α/(2K))`, which is unambiguous. Ensure the text and calculations are consistent with the corrected formula.

### MINOR Revisions

**P5-m1: Internal Draft Artifacts**
*   **Section:** Throughout (e.g., p. 3, p. 12, p. 13, p. 24).
*   **Problem:** The paper contains numerous references to "an earlier draft," "withdrawn" values, and superseded results. While the transparency is commendable, this is language appropriate for an internal audit trail or response to referees, not for a final published manuscript. It distracts from the main narrative.
*   **Required Fix:** Remove all such references (e.g., "An earlier draft quoted...", "those values are withdrawn in favor of...", "an earlier preprint version cited..."). The final paper should present the final, correct analysis and values. The provenance and history can be maintained in the public code repository.

**P5-m2: Inconsistent Use of "p-value"**
*   **Section:** Abstract (p. 1) and VI.A (p. 7).
*   **Problem:** The abstract reports `p = 0.31` for the omnibus homogeneity test. The text in §VI.A also reports `p = 0.31`. However, the abstract also reports `p=0.61/0.135/0.413` for HEALPix scans, which are clearly look-elsewhere corrected p-values from a permutation test. The `p=0.31` is an asymptotic p-value from the χ² distribution. These are different types of statistics.
*   **Required Fix:** For clarity, distinguish between asymptotic p-values and empirical p-values from permutation tests. For example, label the latter as `p_shuffle` or `p_empirical`.

### NITs (Cosmetic)

**P5-N1: Typo in Variable Name**
*   **Section:** III.B DESI Data Release 1 (p. 3).
*   **Problem:** The text specifies a redshift cut `0.01 ≤ x ≤ 4`.
*   **Required Fix:** The variable for redshift is `z`. Change `x` to `z`.

**P5-N2: Figure Axis Label**
*   **Section:** Figure 8 (p. 22).
*   **Problem:** The color bar label in the bottom panel reads "Chirality σfrom half per-pixel (nspirals ≥ 200, z ≤ 0.24)". The subscript "from half" is part of the variable name `σ_from half` defined in the text.
*   **Required Fix:** For clarity and professionalism, render the subscript properly in the label, e.g., "Chirality σ<sub>from half</sub> per pixel...".

***

## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, statistically rigorous, and impressively thorough manuscript that presents a strong null result on an important cosmological question. The level of detail in the robustness checks and the transparency of the author are exemplary. The work is well-suited for publication in Physical Review D.

However, the manuscript in its current form cannot be accepted due to its foundational reliance on an unpublished and non-peer-reviewed companion paper (Paper IV). This is an essential issue that must be resolved. Additionally, several sign errors in the introductory summary and a confusing statistical formula require correction. Once these major issues are addressed, the paper will represent a significant and robust contribution to the field.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from a more rigorous second review of the manuscript.

***

### ADDITIONAL MAJOR Revisions

**P5-M1 (Update): Additional Sign Errors in Introductory Summary**
*   **Section:** Robustness (p. 2).
*   **Problem:** A detailed re-computation of the values in the "Robustness" summary paragraph on page 2 has confirmed the two sign errors identified in the initial review and uncovered a third.
    1.  (Confirmed) `Δfcw = f_cw^void – f_cw^non-void = +0.0007`. Calculation: `0.4964 - 0.4971 = -0.0007`.
    2.  (Confirmed) `V2-REVOLVER catalog-native Δ = -0.0037`. Calculation from §VIII D: `0.4992 - 0.4955 = +0.0037`.
    3.  **(New Finding)** `V2-VIDE catalog-native Δ = +0.0019`. Calculation from §VIII D: `0.4972 - 0.4991 = -0.0019`.
    The presence of three distinct sign errors in this critical summary paragraph severely undermines the reader's confidence in the paper's attention to detail.
*   **Required Fix:** This reinforces the original Major Revision. The entire paragraph must be meticulously re-verified against the results in the main body of the paper. Every number, sign, and statistical convention must be checked and corrected.

### ADDITIONAL MINOR Revisions

**P5-m3: Systematic Cross-Reference Error**
*   **Section:** Abstract (p. 1), §VI.A (p. 7), §IX.B (p. 24).
*   **Problem:** The manuscript repeatedly cites a non-existent section, `§VIII F`, when referring to the number of matched spirals without an environment row or the reconciliation of row counts. The correct section containing this information is `§IX F`.
*   **Required Fix:** Correct all instances of the `§VIII F` cross-reference to point to the correct section, `§IX F`.

**P5-m4: Potentially Unclear Abstract Cross-Reference**
*   **Section:** Abstract (p. 1).
*   **Problem:** The abstract states that the V-Web void class is "dominated by survey-edge artifacts (see §IX C)". While §IX C does mention that edge-density artifacts inflate the void class in a comparison to another work, the most direct and compelling evidence for this claim within this paper comes from the 0/6 disagreement between V-Web and DESIVAST void labels discussed in §VIII A.
*   **Required Fix:** Consider changing this cross-reference to `§VIII A` to point the reader to the most direct internal evidence for the claim.

**P5-m5: Inconsistent Terminology for Void Definitions**
*   **Section:** Robustness (p. 2) vs. §VIII.C (p. 18).
*   **Problem:** The "Robustness" section on p. 2 refers to "three sphere-PIS contrasts" and "two catalog-native GALZONE contrasts" for the DESIVAST robustness check. However, the main text in §VIII.C refers to the first set of tests as "point-in-sphere test[s]". While "PIS" is likely an abbreviation for "point-in-sphere," this acronym is not defined anywhere and its sudden appearance in the introduction is jarring.
*   **Required Fix:** Define the acronym "PIS" on its first use or, preferably, use the full, clear term "point-in-sphere" consistently throughout the manuscript.