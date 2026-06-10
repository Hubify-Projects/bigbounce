# P4 R23conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v167.pdf` md5=b236c8d9 pages=17
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (2405 chars)
**Wall time**: 196.1s

---

Here is a referee report for the submitted manuscript.

---

## Referee Report: "Survey-Scale Galaxy Chirality with Equivariant TTA..."

**Manuscript ID:** [Not provided, using P4 as placeholder]

This paper presents a new, large catalog of galaxy chirality classifications for 8.47 million galaxies from the DESI Legacy Surveys DR8. The authors use a Vision Transformer with a novel Test-Time Equivariant Averaging (TTA) method to mitigate systematic biases. The primary scientific result is a null detection of a real-space chirality dipole, consistent with cosmological isotropy. The paper also provides a detailed investigation of systematic effects, identifying and quantifying a "monopole-mask leakage" channel that can produce spurious signals in harmonic-space analyses.

The work is methodologically rigorous, and the resulting catalog is a significant contribution to the field. The analysis of systematics is exceptionally thorough, particularly the transparent handling of a withdrawn result from a previous version of the manuscript. The distinction between parity-even (dipole) and parity-odd (monopole, even-l) observables is correctly handled. The paper is well-written and the conclusions are strongly supported by the analysis.

While the paper is of high quality and suitable for publication in Physical Review D, I have identified several points that require clarification and correction to meet the journal's standards. My recommendations are detailed below.

### Findings

#### ESSENTIAL

**P4-E1: Abstract (Page 1)**
*   **Problem:** The abstract presents a confusing and seemingly contradictory statement regarding the significance of the harmonic-space residual: "...systematics-attributed residuals (+3.64σ moment-z, ≈1.9σ Gaussian-equivalent, canonical mask...)". A result cannot be both +3.64σ and ≈1.9σ. The text body (e.g., Conclusion c, pg. 11) clarifies that the +3.64σ is derived from the moments of the null distribution, while the ≈1.9σ is the Gaussian-equivalent significance corresponding to the empirical Monte-Carlo p-value (p_MC = 0.030). The current phrasing in the abstract is misleading.
*   **Required Fix:** The abstract must be rephrased for clarity. I suggest: "...residuals (significant at +3.64σ relative to null moments; empirical p=0.030, corresponding to a 1.9σ Gaussian-equivalent significance on the canonical mask)..." or similar wording that clearly separates the moment-based significance from the empirical-rank-based significance.

#### MAJOR

**P4-M1: Table III vs. Main Text (Page 8)**
*   **Problem:** There is a significant discrepancy between the `l=1` significance reported for the canonical mask in Table III (+7.93σ) and the value used throughout the text as the primary harmonic-space diagnostic (+3.64σ). The text attributes the +3.64σ value to a specific analysis choice (monopole subtraction, detailed in Appendix A.c), which is crucial for the monopole-mask leakage interpretation. However, Table III is generated using a different field convention ("Ap with galaxy-weighted mask-mean subtraction") which yields the much higher +7.93σ. Presenting the +7.93σ result in the main summary table while the entire systematics discussion revolves around the +3.64σ result is confusing and undermines the narrative clarity.
*   **Required Fix:** The author must reconcile this. The recommended solution is to make Table III consistent with the main analysis thread. Either replace the "canonical, unapod." rows in Table III with the results from the +3.64σ analysis (i.e., the post-monopole-subtraction field) or, if both conventions must be shown, add a clear footnote to the table explaining the difference and explicitly stating that the +3.64σ value is the one subject to the detailed systematics analysis in Appendix D.

**P4-M2: WLS Fit Discrepancy (Table IX, Page 15)**
*   **Problem:** In Table IX, which details the crucial WLS template fit, the z-score for the `dipole ŷ` component is listed as -43.3. However, a direct calculation from the provided best-fit (`â = -4.52 × 10⁻³`) and naive error (`σ_naive = 1.0 × 10⁻⁴`) yields `z = -45.2`. This is a discrepancy of over 4% in a key result. While this may be due to rounding in the displayed numbers, the difference is large enough to require verification.
*   **Required Fix:** The author must verify the calculations for all z-scores in Table IX and correct any inconsistencies between the `â`, `σ_naive`, and `z` columns.

#### MINOR

**P4-m1: Typo in Conclusions (Page 11)**
*   **Problem:** In Conclusion (c), the text reads: "yields direct canonical - +3.64σ". The hyphen before the plus sign appears to be a typo.
*   **Required Fix:** Remove the stray hyphen. The text should read "yields a direct canonical-mask C_l value of +3.64σ" or similar.

**P4-m2: Jargon in Abstract (Page 1)**
*   **Problem:** The word "dispositioned" in "...dispositioned by an eight-anchor systematic battery..." is jargon.
*   **Required Fix:** Replace with a more standard term like "assessed," "analyzed," or "investigated."

**P4-m3: Typo in Figure Caption (Page 3)**
*   **Problem:** The caption for Figure 1 contains a stray hyphen: "that the ViT - Small classifier resolves".
*   **Required Fix:** Correct to "ViT-Small".

**P4-m4: Hemisphere Statistics Clarity (Table IV vs. Appendix C)**
*   **Problem:** Table IV reports a hemisphere max |A| significance of +4.42σ against the monopole-only generative null. Appendix C reports a maximum hemisphere asymmetry of 3.05σ against a label-shuffle null. While these are different tests, a reader might confuse them.
*   **Required Fix:** Add a brief sentence in the main text or a footnote to Table IV clarifying that this statistic is distinct from the label-shuffle hemisphere test described in Appendix C.

#### NIT (Cosmetic)

**P4-N1: Precision in Abstract (Page 1)**
*   **Problem:** The abstract quotes the WLS template fit exclusion as `z ≈ -18`. The value in Table IX is `-18.1`.
*   **Required Fix:** For consistency with the precision used elsewhere, consider using `-18.1` in the abstract.

**P4-N2: Footnote Placement (Page 6)**
*   **Problem:** Footnote 1 contains crucial details about the construction of the generative null. Its placement as a footnote reduces its visibility.
*   **Required Fix:** Consider integrating the core information from this footnote into the main paragraph of Section IV.D for better readability and emphasis.

**P4-N3: Figure 8 Clarity (Page 9)**
*   **Problem:** The caption for Figure 8 notes that the `l=5` excess shown in the plot is a statistical fluctuation not present in more robust runs. This makes the figure slightly misleading.
*   **Required Fix:** While the caption corrects the record, the author might consider regenerating the plot using the more robust "canonical battery" null results to provide a more accurate visual representation. If this is not feasible, the current caption is acceptable.

**P4-N4: Typo in Appendix D (Page 14)**
*   **Problem:** In section (h), the text reads "re is ill-defined".
*   **Required Fix:** It should be "r_l is ill-defined" to specify the multipole-dependent correlation coefficient.

**P4-N5: Footnote Elevation (Page 15)**
*   **Problem:** Footnote 3 provides a critical explanation of the "monopole-preserving" estimator and why its collapse on high-confidence cuts is a signature of systematics. This is a subtle and important point.
*   **Required Fix:** Consider elevating this explanation from a footnote into the main body of Appendix E to ensure it is not missed by the reader.

---

## Summary recommendation

**MINOR REVISIONS**

This is an excellent and comprehensive paper. The analysis is performed at a very high level of rigor, and the methodological contributions are valuable. The transparent reporting, especially regarding the withdrawn result, is commendable. The paper is a model for how to conduct a search for a subtle cosmological signal while carefully accounting for instrumental and analysis-induced systematics. The required revisions are primarily aimed at improving clarity and ensuring internal consistency between the text, tables, and abstract. Once these minor-to-major points are addressed, the paper will be a strong candidate for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the report of new findings from the second, more rigorous review.

---

### Additional Findings from Rigorous Re-review

My initial review identified the most critical issues. This second, more detailed pass confirms the overall high quality of the manuscript while uncovering a few additional minor points of rigor that should be addressed.

#### MINOR

**P4-m5: Arithmetic Precision in Table IX (Page 15)**
*   **Problem:** In addition to the major calculation error for `dipole ŷ` (finding P4-M2), several other z-scores in Table IX appear to be affected by inconsistent rounding. For example, for the `dipole ẑ` component, the inputs `â = -5.7 × 10⁻⁴` and `σ_naive = 2.8 × 10⁻⁴` give a ratio of `z = -2.0357...`, which should round to `-2.0`, not `-2.1`. While these are small differences, a key table presenting a central result should have fully consistent and reproducible arithmetic.
*   **Required Fix:** The author should re-calculate and verify all z-scores in Table IX to ensure they are the precise ratio of the `â` and `σ_naive` columns, rounded consistently.

**P4-m6: Confusing Internal Cross-References (Page 14)**
*   **Problem:** In Appendix D, the text makes several references back to the main body to connect specific systematic tests to the overall argument. In section (c), the text cites `Sec. IV D` for the "evidence-(b) discriminator". In section (i), it again cites `Sec. IV D` for "discriminator (c)". However, Section IV.D focuses specifically on the monopole-mask leakage generative null and does not contain these summary points. The intended reference appears to be the summary paragraph at the end of the main results section (page 8, just before the start of Section V), which synthesizes the findings from Appendix D.
*   **Required Fix:** The author should correct these cross-references in Appendix D to point to the correct location where the summary argument is made (e.g., "as summarized in Sec. IV...").

#### NIT (Cosmetic)

**P4-N6: Equation Numbering in Text (Page 14)**
*   **Problem:** In Appendix D, section (h), the definition of the cross-correlation coefficient `r_l` is given inline without an equation number. Given that other key definitions like `A_p` (Eq. 3) are numbered, it would improve clarity and future citability to number this equation as well.
*   **Required Fix:** Consider giving the definition of `r_l` its own numbered equation.