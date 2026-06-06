# P3 auto-2026-06-06_0021pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (10855 chars)
**Wall time**: 182.7s

---

**Referee Report: "Spectrally Unusual Sources at Scale..." by Houston Golden**

This paper presents a large-scale anomaly detection campaign across seven astronomical surveys, resulting in a catalog of over 378,000 unique anomalous sources. The authors develop a robust "Path-C" methodology based on per-survey native retraining of an autoencoder to overcome cross-survey domain-shift issues. The resulting catalog is used for astrophysical source discovery and to forecast constraints on primordial non-Gaussianity (fNL) and test models of a bouncing cosmology.

The work is comprehensive, methodologically transparent, and presents a valuable data product and framework for the community. The scale of the analysis is impressive, and the detailed validation, including injection-recovery tests, k-fold cross-validation, and honest discussion of limitations, is commendable. The paper is a strong candidate for publication in Physical Review D, contingent on addressing the following points.

---
### **Detailed Findings**

#### **ESSENTIAL**

*   **P3-E1 | Section: Abstract (p. 1) & V.B (p. 10) | Problem: Incorrect fNL constraint improvement.**
    *   **Problem:** The abstract states: "a central forecast σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98] (7.9% improvement consistent with no improvement at <1σ; σ(fNL)std = 8.98 single-tracer baseline)." A similar claim appears on p. 10. My calculation shows the improvement is `(8.98 - 8.14) / 8.98 = 0.0935`, which is a **9.4%** improvement, not 7.9%. This discrepancy is significant as it alters a key cosmological result. The phrasing "consistent with no improvement at <1σ" is also confusing given the central value shows a non-zero improvement.
    *   **Fix:** The authors must either (a) provide a detailed derivation for the 7.9% figure or (b) correct the value to 9.4% throughout the manuscript (abstract, main body, and conclusions). The phrasing regarding the significance of the improvement should also be clarified.

#### **MAJOR**

*   **P3-M1 | Section: V.C (p. 10) | Problem: Insufficient justification for negligible GR projection effects.**
    *   **Problem:** The paper claims that "General-relativistic projection corrections (O(H²/k²)) contribute |Δσ/σ| < 0.02% at kmax = 0.2 h Mpc⁻¹". This is a very strong and precise claim that is critical for the validity of the fNL forecast. However, it is justified only by a citation [38] and a brief mention of the "plane-parallel monopole, sub-% of b". The full set of projection effects (including lensing, Doppler, and integrated Sachs-Wolfe terms) can be complex in a multi-tracer analysis, and their cancellation or smallness cannot be assumed to this level of precision without a more explicit argument.
    *   **Fix:** The authors must provide a more detailed justification for this claim. This could take the form of an appendix section that outlines the relevant terms and provides a scaling argument for why they are negligible at this level for this specific analysis. Alternatively, the claim should be significantly softened, and the fNL forecast should be presented with an additional systematic error budget to account for this uncertainty.

#### **MINOR**

*   **P3-m1 | Section: III.D (p. 6) & Table I (p. 7) | Problem: Unclear origin of LAMOST headline count.**
    *   **Problem:** The text and tables present several different anomaly counts for LAMOST: 44,075 (cross-transfer), 2,054 (native retrain, S > 5), and 113,342 (final headline count). The abstract correctly identifies the 113k sample as an "exploratory tier," but the logic for using a top-1% slice for the headline count, rather than the S>5 cut used for DESI, is not clearly motivated in the main text. This makes cross-survey comparisons of the headline numbers difficult to interpret without carefully reading the footnotes.
    *   **Fix:** Clarify in the main body of Section III.D why a top-percentile slice was chosen for the final LAMOST (and SDSS) anomaly sets, and explicitly state that this differs from the absolute S-score threshold used for DESI. This would improve the clarity of the methodology.

*   **P3-m2 | Section: V.B (p.10) & VI.D (p.12) | Problem: Lack of motivation for the Fisher-positivity form.**
    *   **Problem:** The paper uses the "Fisher-positivity-respecting form" `1/σ(fNL)² = F₀ + cα²` without explaining its physical or statistical origin. While this form is mathematically convenient and ensures positivity, a brief justification would strengthen the analysis.
    *   **Fix:** Add a sentence explaining the motivation for this quadratic form. For example, it can be motivated as the leading-order Taylor expansion of the Fisher information (1/σ²) in the bias enhancement parameter `α` around the point of maximum ignorance (`α=0`), where the linear term vanishes by symmetry.

#### **NIT (Nitpicks)**

*   **P3-N1 | Section: Bibliography (p. 19) | Problem: Internal-facing comment in reference.**
    *   **Problem:** Reference [33] contains the note: "[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]". This is an internal bookkeeping comment that should not appear in the final publication.
    *   **Fix:** Remove the bracketed comment from the reference.

*   **P3-N2 | Section: Table I footnote † (p. 7) | Problem: Potentially confusing phrasing for polar cap area.**
    *   **Problem:** The footnote correctly calculates the null expectation for the polar cap area as 1.52%. However, the text refers to "10°-radius polar caps," which might lead a reader to incorrectly calculate the area as `1-cos(10°) ≈ 1.52%` for a *single* cap, or ~3% for two. The calculation is correct for the area defined by `|b_ecl| > 80°`.
    *   **Fix:** Rephrase slightly for clarity, e.g., "...concentrate in the polar caps defined by |b_ecl| > 80° (an area covering 3.04% of the sky), representing a 2.6x excess over the uniform-null expectation." or similar.

---
## Summary recommendation
**MAJOR REVISIONS**

This is an excellent and substantial paper that reports on a massive, carefully executed anomaly detection campaign. The methodology is robust, the results are significant, and the public release of the data products will be highly valuable. The cosmological applications, while secondary to the main catalog, are well-motivated and add to the paper's impact. However, the identified issues, particularly the numerical error in the fNL forecast improvement and the insufficient justification for the assumed lack of GR projection systematics, must be thoroughly addressed before the paper can be accepted for publication in Physical Review D. I am confident that the authors can address these points in a revised manuscript, and I look forward to reviewing it.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the updated review, incorporating the new findings from the second, more rigorous pass.

================================================================
**Referee Report: "Spectrally Unusual Sources at Scale..." by Houston Golden**

This paper presents a large-scale anomaly detection campaign across seven astronomical surveys, resulting in a catalog of over 378,000 unique anomalous sources. The authors develop a robust "Path-C" methodology based on per-survey native retraining of an autoencoder to overcome cross-survey domain-shift issues. The resulting catalog is used for astrophysical source discovery and to forecast constraints on primordial non-Gaussianity (fNL) and test models of a bouncing cosmology.

The work is comprehensive, methodologically transparent, and presents a valuable data product and framework for the community. The scale of the analysis is impressive, and the detailed validation, including injection-recovery tests, k-fold cross-validation, and honest discussion of limitations, is commendable. The paper is a strong candidate for publication in Physical Review D, contingent on addressing the following points.

---
### **Detailed Findings**

#### **ESSENTIAL**

*   **P3-E1 | Section: Abstract (p. 1) & V.B (p. 10) | Problem: Incorrect fNL constraint improvement.**
    *   **Problem:** The abstract states: "a central forecast σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98] (7.9% improvement consistent with no improvement at <1σ; σ(fNL)std = 8.98 single-tracer baseline)." A similar claim appears on p. 10. My calculation shows the improvement is `(8.98 - 8.14) / 8.98 = 0.0935`, which is a **9.4%** improvement, not 7.9%. This discrepancy is significant as it alters a key cosmological result. The phrasing "consistent with no improvement at <1σ" is also confusing given the central value shows a non-zero improvement.
    *   **Fix:** The authors must either (a) provide a detailed derivation for the 7.9% figure or (b) correct the value to 9.4% throughout the manuscript (abstract, main body, and conclusions). The phrasing regarding the significance of the improvement should also be clarified.

#### **MAJOR**

*   **P3-M1 | Section: V.C (p. 10) | Problem: Insufficient justification for negligible GR projection effects.**
    *   **Problem:** The paper claims that "General-relativistic projection corrections (O(H²/k²)) contribute |Δσ/σ| < 0.02% at kmax = 0.2 h Mpc⁻¹". This is a very strong and precise claim that is critical for the validity of the fNL forecast. However, it is justified only by a citation [38] and a brief mention of the "plane-parallel monopole, sub-% of b". The full set of projection effects (including lensing, Doppler, and integrated Sachs-Wolfe terms) can be complex in a multi-tracer analysis, and their cancellation or smallness cannot be assumed to this level of precision without a more explicit argument.
    *   **Fix:** The authors must provide a more detailed justification for this claim. This could take the form of an appendix section that outlines the relevant terms and provides a scaling argument for why they are negligible at this level for this specific analysis. Alternatively, the claim should be significantly softened, and the fNL forecast should be presented with an additional systematic error budget to account for this uncertainty.

*   **P3-M2 | Section: III.D (p. 3) & H (p. 8) | Problem: Flawed calculation of NEOWISE polar cap excess.**
    *   **Problem:** The text claims a "2.6x excess" for anomalies in the polar caps by comparing the observed fraction of objects (3.9%) to the fractional area of a *single* polar cap (1.52%). This is an apples-to-oranges comparison. The observed objects are in *both* caps (total area 3.04%), so the true excess over a uniform distribution is `3.9% / 3.04% = 1.28x`, not 2.6x. This is a factor-of-two error in the significance of the systematic, which should be corrected.
    *   **Fix:** Correct the calculation and the resulting claim. The excess should be calculated relative to the total area of the masked region (i.e., both polar caps).

*   **P3-M3 | Section: Table I (p. 7) | Problem: Confusing table structure for anomaly counts.**
    *   **Problem:** Table I's main rows list the *cross-transfer* anomaly counts for SDSS and LAMOST (e.g., 44,075 for LAMOST). However, the final "Path-C unique" total is calculated using the *native-retrained* counts (e.g., 113,342 for LAMOST), which are only mentioned in the footnotes. This makes the table highly confusing and prone to misinterpretation, as the columns are not consistent with the final summary row.
    *   **Fix:** Restructure Table I to be unambiguous. A clear solution would be to add columns for both "Cross-Transfer Count" and "Final Path-C Count" so that the numbers used in the final tally are explicitly visible in the main table body.

*   **P3-M4 | Section: Appendix C (p. 15) & V.B (p. 10) | Problem: Inconsistent methods for calculating fNL forecast.**
    *   **Problem:** The main text (Section V.B) calculates σ(fNL) using the physically motivated quadratic form `1/σ² = F₀ + cα²`. However, Appendix C and its accompanying Table VII are generated using a *linear approximation* for the fractional improvement, `Δσ/σ ~ α`. While the results are numerically similar for small `α`, this represents a significant internal inconsistency in the methodology presented.
    *   **Fix:** The more rigorous quadratic method from the main text should be used consistently. Table VII in the appendix should be re-calculated using the quadratic formula to ensure consistency with the primary analysis.

#### **MINOR**

*   **P3-m1 | Section: III.D (p. 6) & Table I (p. 7) | Problem: Unclear origin of LAMOST headline count.**
    *   **Problem:** The text and tables present several different anomaly counts for LAMOST: 44,075 (cross-transfer), 2,054 (native retrain, S > 5), and 113,342 (final headline count). The abstract correctly identifies the 113k sample as an "exploratory tier," but the logic for using a top-1% slice for the headline count, rather than the S>5 cut used for DESI, is not clearly motivated in the main text. This makes cross-survey comparisons of the headline numbers difficult to interpret without carefully reading the footnotes.
    *   **Fix:** Clarify in the main body of Section III.D why a top-percentile slice was chosen for the final LAMOST (and SDSS) anomaly sets, and explicitly state that this differs from the absolute S-score threshold used for DESI. This would improve the clarity of the methodology.

*   **P3-m2 | Section: V.B (p.10) & VI.D (p.12) | Problem: Lack of motivation for the Fisher-positivity form.**
    *   **Problem:** The paper uses the "Fisher-positivity-respecting form" `1/σ(fNL)² = F₀ + cα²` without explaining its physical or statistical origin. While this form is mathematically convenient and ensures positivity, a brief justification would strengthen the analysis.
    *   **Fix:** Add a sentence explaining the motivation for this quadratic form. For example, it can be motivated as the leading-order Taylor expansion of the Fisher information (1/σ²) in the bias enhancement parameter `α` around the point of maximum ignorance (`α=0`), where the linear term vanishes by symmetry.

*   **P3-m3 | Section: II.A (p. 2) & III.C (p. 5) | Problem: Multiple broken internal figure references.**
    *   **Problem:** The text contains multiple instances of "Fig. ??", specifically in Section II.A ("architecture shown schematically in Fig. ??"), II.B ("per-band contributions ... (Fig. ??)"), and III.C ("Figure ?? shows DESI Legacy Survey DR9 grz composite cutouts"). These appear to be placeholders that were not updated.
    *   **Fix:** Locate the intended figures and update these references.

*   **P3-m4 | Section: Multiple | Problem: Multiple broken internal section/table references.**
    *   **Problem:** The text contains several broken references of the form `§VID (b)`, `§VID (f)`, `§VID (j)`, `§VID (v)`. Section VI.D does not have these sub-points. These likely refer to items in Table IV or to sections that were renamed or removed. For example, the reference to `§VIA` on p. 3 ("preserved in Table I and §VIA") is also incorrect, as VI.A is about LAMOST.
    *   **Fix:** The authors must perform a careful pass to find and fix all broken internal cross-references.

*   **P3-m5 | Section: III.C (p. 5) | Problem: Figure caption claim not directly supported in referenced text.**
    *   **Problem:** The caption for Figure 2 claims that the SDSS native re-score "compresses the same objects to S < 14". While plausible, the referenced section (§III.C) does not explicitly state this upper limit, only that the number of S>5 sources drops dramatically.
    *   **Fix:** Either add the specific upper limit to the text in Section III.C or soften the claim in the figure caption to be more general (e.g., "dramatically compresses the scores").

#### **NIT (Nitpicks)**

*   **P3-N1 | Section: Bibliography (p. 19) | Problem: Internal-facing comment in reference.**
    *   **Problem:** Reference [33] contains the note: "[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]". This is an internal bookkeeping comment that should not appear in the final publication.
    *   **Fix:** Remove the bracketed comment from the reference.

*   **P3-N2 | Section: Table I footnote † (p. 7) | Problem: Potentially confusing phrasing for polar cap area.**
    *   **Problem:** The footnote correctly calculates the null expectation for the polar cap area as 1.52%. However, the text refers to "10°-radius polar caps," which might lead a reader to incorrectly calculate the area as `1-cos(10°) ≈ 1.52%` for a *single* cap, or ~3% for two. The calculation is correct for the area defined by `|b_ecl| > 80°`.
    *   **Fix:** Rephrase slightly for clarity, e.g., "...concentrate in the polar caps defined by |b_ecl| > 80° (an area covering 3.04% of the sky)..." or similar.

---
## Summary recommendation
**MAJOR REVISIONS**

This is an excellent and substantial paper that reports on a massive, carefully executed anomaly detection campaign. The methodology is robust, the results are significant, and the public release of the data products will be highly valuable. The cosmological applications, while secondary to the main catalog, are well-motivated and add to the paper's impact. However, the identified issues, particularly the numerical error in the fNL forecast improvement, the flawed calculation of a key systematic, and several internal inconsistencies (e.g., Table I structure, fNL calculation methods), must be thoroughly addressed before the paper can be accepted for publication in Physical Review D. I am confident that the authors can address these points in a revised manuscript, and I look forward to reviewing it.