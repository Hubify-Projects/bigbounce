# P5 INT-X-P5 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` md5=e446dfce pages=33
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 118.3s

---

## Referee Report: P5-INT-X-P5

**To the Editor of Physical Review D,**

This manuscript, "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample," presents a detailed statistical analysis searching for a correlation between the observed chirality of spiral galaxies and their large-scale structure environment. The authors use a large dataset derived from DESI Data Release 1 and a previously compiled chirality catalog. The primary conclusion is a null result: no statistically significant environmental dependence is found, after accounting for a known, small, catalog-wide systematic monopole offset in the chirality classifier. The analysis is extensive, including multiple environmental classifiers (T-Web, DESIVAST voids, Tempel+2014 FoF), a wide range of robustness checks, and a careful treatment of statistical uncertainties and look-elsewhere effects.

The paper demonstrates a high level of technical competence and a commitment to reproducibility, with extensive cross-checks and detailed appendices. The work is thorough and the statistical methods are generally sound. However, there are several foundational issues that must be addressed before the paper can be considered for publication in Physical Review D. The most critical of these are the reliance on an unpublished "in preparation" companion paper for the primary input data and a flawed construction of the theoretical toy model in Appendix A.

Below is a detailed list of findings.

---

### ESSENTIAL Revisions

**P5-E1: Foundational Reliance on an Unpublished ("in preparation") Manuscript**
*   **Section:** Throughout, starting on Page 1 (Abstract) and Page 3 (Sec. II).
*   **Problem:** The entire analysis is predicated on the galaxy chirality catalog from "Paper IV [3] (in preparation)". Key inputs, including the per-galaxy CW/CCW labels and the crucial -0.26 pp classifier-monopole offset, are taken as given from this unpublished source. A manuscript submitted to PRD must be self-contained and its foundations must be verifiable. Relying on an "in preparation" paper for the primary data input and its core systematic calibration is not acceptable. The claims of Paper IV are load-bearing for every statistical test in this manuscript.
*   **Required Fix:** The authors must, at a minimum, ensure that Paper IV is publicly available on the arXiv before this manuscript can be published. The manuscript should be updated to cite the arXiv preprint. Ideally, for a result of this scope, the companion paper should have already passed peer review. The current "in preparation" status is a hard barrier to publication.

**P5-E2: Flawed Construction of Parity-Odd EFT Operator**
*   **Section:** Page 30, Appendix A.
*   **Problem:** The toy EFT operator proposed, `L_parity ∝ g_φ (∇iφ) (∇jρ/ρbg) (L·∇ρ)`, is not a rotationally invariant scalar and therefore cannot serve as a valid Lagrangian density term. The angular momentum `L` is a pseudovector, and the density gradient `∇ρ` is a polar vector. Their dot product, `L·∇ρ`, is a pseudoscalar. The term `(∇iφ)` is a polar vector. The overall expression is not a scalar. The text claims the form is "manifestly rotationally-invariant," which is incorrect. While presented as a "toy," even a schematic operator used to frame the observational bounds must respect fundamental symmetries.
*   **Required Fix:** The operator must be reconstructed to be a proper parity-odd scalar. For example, if `φ` is a pseudoscalar field, a valid term could be `L_parity ∝ g_φ * φ * (L·∇ρ)`. Alternatively, if `φ` is a scalar, one could construct a term like `L_parity ∝ g_φ * (L · (∇φ × ∇ρ))`. The current formulation is physically incorrect and must be replaced.

---

### MAJOR Revisions

**P5-M1: Post-Hoc Selection of the Primary Analysis Path**
*   **Section:** Page 1 (Abstract), Page 7 (Sec. V B).
*   **Problem:** The authors commendably and transparently declare that the choice of the DESIVAST-anchored analysis as "primary" was made post-hoc. However, this introduces a significant "garden of forking paths" issue that is not fully mitigated by the declaration. While the scientific justifications (larger sample size, peer-reviewed void catalog) are sound, the statistical integrity of the final p-values and significance statements is weakened. The abstract presents the DESIVAST result as the headline, which could be misleading without a prominent upfront caveat.
*   **Required Fix:** The abstract and conclusions must be rephrased to more strongly reflect the exploratory nature of the analysis that results from the post-hoc path selection. The authors should state that while a comprehensive set of tests yielded no significant signal, the lack of a pre-registered analysis plan means the results should be interpreted as setting bounds within the specific frameworks tested, rather than a single definitive null test. The "Analysis-tree declaration" (Table II) is excellent practice but does not erase the issue.

**P5-M2: Redshift-Space Distortions (RSD) Not Carried to Abstract/Conclusion**
*   **Section:** Page 29 (Sec. XIII), and its omission from Page 1 (Abstract) and Page 30 (Conclusions).
*   **Problem:** The authors correctly identify in the Limitations section that the entire analysis is performed in redshift space, and that this induces anisotropic distortions in the tidal tensor field that are not captured by a simple scalar displacement argument. This is a critical caveat. The headline result is a "fixed-redshift-space statement." This limitation is significant enough that it must be stated alongside the main conclusion in the abstract and the conclusion section, not buried in the limitations.
*   **Required Fix:** Add a sentence to the abstract and the opening of the conclusion section explicitly stating that the analysis is conducted in redshift space and the results are therefore a constraint on the redshift-space environmental dependence of chirality. For example: "This null is a fixed-redshift-space statement; all classifications and tests inherit redshift-space distortion effects."

---

### MINOR Revisions

**P5-m1: Abstract is Overly Dense and Long**
*   **Section:** Page 1 (Abstract).
*   **Problem:** The abstract is exceptionally long and packed with a very large number of numerical results, including multiple p-values, σ-values, and sample sizes for secondary analyses. While detailed, it is difficult to parse and obscures the top-level message. A PRD abstract should be concise and focus on the primary result and its main qualifications.
*   **Required Fix:** Shorten and streamline the abstract. Focus on the headline DESIVAST result, the consistent null from the T-Web check, the key finding that deviations are explained by the classifier monopole, and the main caveats (RSD, post-hoc selection). Move the detailed statistics for secondary tests (e.g., the full breakdown of T-Web per-class fractions and σ-values) to the main body.

**P5-m2: Data Availability and Archiving**
*   **Section:** Page 31 (Appendix C).
*   **Problem:** The use of a version-tagged GitHub repository is excellent for reproducibility. However, for long-term archival purposes and to ensure the exact version of the code and data remains permanently accessible, a persistent DOI is the standard.
*   **Required Fix:** The authors should create a permanent archival snapshot of the specified GitHub repository tag (e.g., using Zenodo, which integrates with GitHub) and add the resulting DOI to the manuscript.

**P5-m3: Uncomputed Comparison in Abstract**
*   **Section:** Page 1 (Abstract).
*   **Problem:** The abstract states: "The quoted σ_from_half values scale as √n at fixed fractional offset and are therefore not mutually comparable across classes of different n." This is a correct and important statistical point. However, it is immediately followed by a list of these non-comparable values without any effect-size metric or monopole-subtracted residual that *would* be comparable. This juxtaposition is confusing for the reader.
*   **Required Fix:** Either remove the list of raw σ values from the abstract or, preferably, replace them with the monopole-subtracted residuals from Table XII, which *are* comparable and more directly support the paper's main thesis.

---

### NIT (Nitpicks)

**P5-N1: Future Date on Manuscript**
*   **Section:** Page 1.
*   **Problem:** The paper is dated "June 28, 2026".
*   **Required Fix:** Correct the date to the current submission date.

---

## Summary recommendation

**MAJOR REVISIONS**

This is a substantial and carefully executed piece of work that performs a valuable null test for new physics. The authors' attention to statistical detail, robustness checks, and reproducibility is commendable and sets a high standard. However, the two ESSENTIAL issues identified—the reliance on an unpublished "in preparation" manuscript for the core data and the physically incorrect formulation of the toy EFT operator—are absolute bars to publication in its current form. Furthermore, the MAJOR issues concerning the post-hoc analysis design and the downplaying of redshift-space effects in the abstract and conclusion need to be addressed to ensure the paper's claims are appropriately qualified.

I am confident that the authors can address these points. The underlying analysis appears solid, and the paper will be a strong candidate for publication in Physical Review D once these foundational and structural issues are resolved.