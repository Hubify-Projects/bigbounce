# P2 INT-M2 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=79edd4cc pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 123.0s

---

## Referee Report for "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook"

**Paper ID:** P2
**Journal:** Physical Review D

### Summary of the Paper

This paper presents a detailed sensitivity forecast for testing the matter-bounce cosmological scenario using upcoming data from the SPHEREx survey, with an additional outlook for the proposed MegaMapper survey. The primary observable is the local-type primordial non-Gaussianity parameter, `f_NL`, which is predicted to have a specific, large, negative value (`f_NL = -35/8`) in the minimally parameterized scalar-only matter-bounce class.

The work is framed as a "sensitivity recast" of an existing SPHEREx multi-tracer galaxy bispectrum forecast by Heinrich et al. (2024). The authors' main contributions are:
1.  A thorough audit of the theoretical prediction `f_NL = -35/8`, resolving a factor-of-two discrepancy in the literature in favor of the Cai et al. (2009) result.
2.  A detailed quantification of the template mismatch (`r ≈ 0.84`) between the matter-bounce bispectrum and the standard local template, and its effect on the forecast sensitivity.
3.  An analysis of a polynomial null space in the bispectrum shape, concluding that it introduces a manageable `±0.13` scatter in the mismatch factor `r`.
4.  A comprehensive systematic budget, combining the template mismatch with other effects (e-corrections, GR projection, PNG bias uncertainty) in an additive-quadrature heuristic, leading to a final realistic significance envelope of `2.6-5.5σ` for SPHEREx.
5.  A Bayesian model comparison, finding that a SPHEREx detection would favor the bounce over tuned multifield inflationary models with a Bayes factor of `BF ≈ 9-14`.
6.  A new, independent, joint Fisher forecast for `(f_NL, n_fNL)` from the scale-dependent bias (SDB) channel, which serves as a subordinate cross-check and highlights the `f_NL-n_fNL` degeneracy.

The paper is exceptionally thorough, transparent about its assumptions and limitations, and provides extensive cross-checks and reproducibility materials. The analysis is of high quality and the conclusions are well-supported by the calculations presented.

### Detailed Findings

#### ESSENTIAL
No findings are classified as ESSENTIAL. The paper is of very high quality and ready for publication after minor revisions.

#### MAJOR

**P2-M1: Heuristic Nature of the Consolidated Systematic Budget**
*   **Section/Page:** VII (p. 15), IV (p. 20, Table IV), Abstract (p. 1)
*   **Problem:** The paper's headline realistic significance range (`2.6-5.5σ`) is derived from a consolidated systematic budget where individual contributions are combined via additive quadrature (e.g., `σ_eff^2 = σ_base^2 + σ_syst^2`). The paper is commendably transparent about this, calling it a "transparent scoping heuristic" and noting that a "joint multi-tracer marginalized Fisher" is not performed for the full bispectrum. However, given that degeneracies between parameters (e.g., `b_1`, `b_φ`, `f_NL`) can either tighten or loosen constraints, this heuristic remains the largest single methodological weakness of the headline forecast. The paper's own SDB analysis in Sec. IX.D shows that the `b_1-f_NL-n_fNL` correlations *loosen* the SDB constraint by a large factor (4.6x), demonstrating the importance of a full covariance treatment.
*   **Fix:** While a full joint bispectrum Fisher analysis is beyond the scope of this recast, the paper should add a sentence in the abstract and in the introduction to Section VII explicitly stating that the additive-quadrature combination assumes uncorrelated systematic contributions and that the true joint constraint could be weaker (or stronger, though less likely based on the SDB result) than the quoted envelope. This would further strengthen the paper's already honest self-assessment. For example, in the abstract, modify "...these systematics are combined additively in quadrature, so the realistic 2.6-5.5σ range is a scoping sensitivity envelope..." to "...these systematics are combined in quadrature, assuming they are uncorrelated; the realistic 2.6-5.5σ range is therefore a scoping sensitivity envelope...".

#### MINOR

**P2-m1: Finalization of Data/Code Repository DOI**
*   **Section/Page:** Data and Code Availability (p. 25)
*   **Problem:** The text states that the code is archived at Zenodo with "(DOI inserted at submission)".
*   **Fix:** Please ensure the final Zenodo DOI is included in the camera-ready version of the paper.

**P2-m2: Clarity on the SDB Fisher Calculation as a New Contribution**
*   **Section/Page:** Abstract (p. 1), Sec. IX.D (p. 22)
*   **Problem:** The paper primarily frames itself as a "recast". However, the joint `(f_NL, n_fNL)` SDB Fisher forecast (`c8_fnl_running_fisher.json`) is a new, independent calculation performed for this work. While the abstract correctly separates it as a "computed SDB result", the overall "recast" framing might slightly undersell this original contribution.
*   **Fix:** Consider adding a clarifying phrase in the abstract, e.g., "Separately, and as an independently computed result kept distinct from this bispectrum-only headline, *our new joint* scale-dependent-bias (SDB) Fisher matrix...". This is a minor suggestion to ensure the paper receives full credit for its original components.

**P2-m3: Verification of Artifact Availability**
*   **Section/Page:** Data and Code Availability (p. 25)
*   **Problem:** The paper lists numerous specific analysis artifacts (e.g., `c9h_nullspace_significance_propagation.json`, `phase3_bispectrum_shape_overlap.json`). The reproducibility of the paper hinges on these files being available and correctly named.
*   **Fix:** Please double-check that every named artifact in this section is present in the final repository, is clearly named, and is accompanied by a README file explaining its structure and how it was generated.

#### NIT (Nitpicks)

**P2-N1: Redundancy in Table II Caption**
*   **Section/Page:** Table II Caption (p. 16)
*   **Problem:** The caption contains the sentence: "The recommended `σ_theory = 1.0` headline of BF ~ 10 is approximately constant under the same GR variation." This is followed by: "'The ~ 17 row reports the delta-bounce-prior Bayes factor...". The first sentence seems to be a leftover thought that interrupts the flow. The GR variation for the recommended row is not shown in the table, making the statement difficult to verify from the table itself.
*   **Fix:** Suggest removing the sentence "The recommended `σ_theory = 1.0` headline of BF ~ 10 is approximately constant under the same GR variation." for improved clarity and flow, as the GR dependence is the subject of Table III.

### Verification of Calculations and Figures

*   **Abstract & Body Calculations:** All re-computed significance values, Bayes factors (from the provided formulas and parameters), and degradation factors were found to be consistent with the values quoted in the paper. The worked example for `BF ≈ 9.2` in Sec. VI is particularly helpful and was verified.
*   **Figure 1:** The plot of `B_NL` is clear, correctly labeled, and the plotted points match the values in Table I.
*   **Figure 2:** The bar chart accurately reflects the significance values derived and discussed in the text. The use of different styles for naive, optimistic, and realistic forecasts is effective.
*   **Figure 3:** A simple but effective visualization of the `f_NL` landscape.
*   **Figures 4 & 5:** These figures provide a compelling visualization of the fragility of the SDB channel with respect to `k_min` and `b_φ` uncertainty, correctly motivating the paper's focus on the more robust bispectrum channel.
*   **Figure 6:** The decision threshold plot is a clear and useful summary for the reader.
*   **Tables I-V:** All tables are exceptionally well-documented with detailed captions. The numbers are internally consistent and consistent with the main body text. Table IV, the consolidated systematic budget, is a model of transparency.

### Overall Assessment

This is an exemplary forecast paper. It is methodologically sound, intellectually honest, and meticulously executed. The authors clearly delineate between recast results and new calculations, are transparent about all assumptions and limitations (particularly the heuristic nature of the systematic budget), and provide a wealth of cross-checks and supporting material to bolster their claims. The audit of the `f_NL = -35/8` prediction and the detailed analysis of the template mismatch are significant contributions to the field. The paper is well-written, well-structured, and meets the high standards of Physical Review D.

## Summary recommendation

**ACCEPT WITH MINOR CORRECTIONS**

The paper is a high-quality, comprehensive, and valuable contribution. It provides a robust and transparent forecast for a key test of non-standard early universe cosmology. The recommended revisions are minor and are intended only to further clarify the methodological limitations and ensure the reproducibility materials are finalized. The paper is otherwise ready for publication.