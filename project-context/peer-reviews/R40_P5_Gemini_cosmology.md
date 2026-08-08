# P5 R40 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` md5=7bb73989 pages=32
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 134.3s

---

## Referee Report: P5-R40

**Manuscript Title:** Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample
**Author:** Houston Golden
**Recommendation:** MAJOR REVISIONS

---

### General Comments

This manuscript presents a detailed and comprehensive search for an environmental dependence of spiral galaxy chirality using data from the DESI Data Release 1. The primary analysis is anchored on the DESIVAST void catalog, supported by a secondary analysis using a T-Web cosmic-web classifier. The author performs an extensive suite of null tests, including sensitivity sweeps of algorithm parameters, redshift and density stratifications, and cross-checks against other environmental classifiers. The headline result is a null detection: no statistically significant evidence for environment-dependent chirality is found beyond a known, catalog-wide systematic monopole offset.

The work is statistically thorough, and the author demonstrates a commendable commitment to robustness and reproducibility. The sheer number of cross-checks and the careful treatment of statistical uncertainties are strengths of the paper.

However, the manuscript suffers from several critical issues that preclude its acceptance in Physical Review D in its current form. These include an essential dependency on an unpublished companion paper, a potential sign error in the core methodology, excessive length for the presented result, and a lack of clarity in the abstract. The paper has the potential to be a valuable contribution to the literature, but only after substantial revisions to address the points detailed below.

---

### Detailed Findings

#### ESSENTIAL Revisions

**P5-E1: Critical Dependency on Unpublished Work**
*   **Section:** Throughout, starting with Abstract (p. 1) and II (p. 3).
*   **Problem:** The entire analysis is predicated on the "8,474,531-galaxy chirality catalog of Paper IV [3] (in preparation)". Key inputs, including the per-galaxy chirality labels (CW/CCW) and the crucial catalog-wide monopole offset (Δf_cw = -0.0026), are imported from this unpublished work. A reader cannot evaluate the validity of the inputs or the systematic offset that is central to the interpretation of the results. A paper submitted to PRD must be self-contained. Citing an "in preparation" manuscript for the foundational dataset and its primary systematic is unacceptable.
*   **Required Fix:** The manuscript cannot be published until Paper IV is, at a minimum, publicly available on the arXiv. The reference must be updated to a valid arXiv ID. Furthermore, this paper must summarize the essential methodology of Paper IV regarding classifier training, test-time augmentation, and the determination of the monopole offset, so it can be understood without needing to read the companion paper in its entirety.

**P5-E2: Sign Mismatch in Tidal Tensor Definition**
*   **Section:** IV.A, step 9 (p. 5) and footnote `a` (p. 2).
*   **Problem:** There is a sign inconsistency in the definition of the tidal tensor. Footnote `a` (p. 2) gives the standard real-space definition `T_ij = ∂²Φ/∂x_i∂x_j`. In step 9 (p. 5), the paper states the Fourier-space Poisson equation as `Φ(k) = -δ_k/k²` and the tidal tensor as `T_ij(k) = +k_i k_j δ_k/k²`.
    Assuming a Fourier convention `∂/∂x → ik`, the second derivative is `∂_i ∂_j → (ik_i)(ik_j) = -k_i k_j`. Therefore, the Fourier-space tidal tensor should be `T_ij(k) = -k_i k_j Φ(k) = -k_i k_j (-δ_k/k²) = +k_i k_j δ_k/k²`. The paper's equation `T_ij(k) = +k_i k_j δ_k/k²` appears correct under this convention. However, the text then states "the committed implementation... applies exactly this sign, matching the title-footnote convention". The title-footnote convention is `T_ij = ∂²Φ/∂x_i∂x_j`, which is the deformation tensor, not the tidal tensor `T_ij = -∂²Φ/∂x_i∂x_j`. The sign of the eigenvalues is critical for classifying environments (voids have 0 positive eigenvalues, clusters have 3). The text claims the resulting volume fractions are standard, which suggests the code is correct, but the description is confusing and potentially erroneous.
*   **Required Fix:** Clarify the precise definition of the tensor being used (tidal vs. deformation). State the definition consistently in real space and Fourier space, ensuring all signs are correct. Explicitly state the expected signs of the eigenvalues for each cosmic-web environment under the chosen definition. Remove the ambiguous reference to the "title-footnote convention".

#### MAJOR Revisions

**P5-M1: Excessive Length and Structure**
*   **Section:** Entire manuscript.
*   **Problem:** At 32 pages, the paper is excessively long for what is ultimately a null result. While the robustness checks are valuable, many of them could be significantly summarized in the main text and detailed in appendices. For example, the extensive discussion of the z-shell corrected classifier (Sec. IX.A, p. 22-23) and the ASTRA EDR cross-validation (Sec. X, p. 26) are secondary checks that add considerable length. The current structure buries the primary DESIVAST result (Sec. VIII) after the secondary T-Web analysis (Sec. VI).
*   **Required Fix:**
    1.  Restructure the paper to present the primary DESIVAST analysis (Sec. VIII) *before* the secondary T-Web analysis (Sec. VI).
    2.  Drastically shorten the main text. Aim for a maximum of 15 pages for the main body.
    3.  Move detailed discussions of secondary cross-checks (e.g., Tempel FoF, ASTRA EDR, z-shell correction) to an appendix, retaining only a concise summary of the method and result in the main text.
    4.  The paper should be focused on the main result and its most direct and powerful robustness tests.

**P5-M2: Unclear and Overly Dense Abstract**
*   **Section:** Abstract (p. 1).
*   **Problem:** The abstract is a dense list of numerical results that is nearly unreadable. It fails to provide a clear, high-level summary of the paper's motivation, methods, and conclusions. It reads more like a technical summary or a list of table entries. For instance, the detailed breakdown of σ values and p-values for multiple sub-tests is inappropriate for an abstract.
*   **Required Fix:** Rewrite the abstract completely. It should be a single, concise paragraph that:
    1.  States the physical question being investigated.
    2.  Briefly describes the primary dataset and method (e.g., "We cross-match a catalog of 8.5M galaxies with measured spin chirality against DESI DR1 redshifts, using the DESIVAST void catalog to define environments for 56,981 spirals.").
    3.  States the main finding clearly and concisely (e.g., "We find no evidence for an environmental dependence of spiral chirality. The CW/CCW fraction in voids (0.4964) is statistically indistinguishable from that in denser environments (0.4971), with a difference of 0.07 ± 0.22 percentage points.").
    4.  Briefly mentions the scope of robustness checks and the main conclusion (e.g., "This null result is robust against variations in cosmic-web classification algorithms, smoothing scales, and observational systematics, placing a new observational constraint on models of parity violation in the early universe.").

**P5-M3: Misleading Presentation of Residuals in Table IV**
*   **Section:** VI.C, Table IV (p. 10).
*   **Problem:** The final column is labeled `σ_obs - σ_pred`, implying a signed residual. However, the value for Quintile 3 is given as `1.87`, whereas the calculation is `σ_obs - σ_pred = -3.94 - (-2.07) = -1.87`. The table is reporting the absolute value of the residual without stating so. This is misleading. The abstract correctly reports this as `|σ_obs - σ_pred| = 1.87`.
*   **Required Fix:** Either change the column header to `|σ_obs - σ_pred|` or report the correct signed values in the table. Consistency with the abstract and clarity in the table are paramount.

**P5-M4: Speculative and Non-Rigorous Appendix A**
*   **Section:** Appendix A (p. 30).
*   **Problem:** This appendix presents a "Toy EFT mapping" of the observational bound. The author correctly includes numerous, strong caveats, admitting the proposed operator is not rotationally or gauge invariant and is merely a "coordinate-aligned schematic". While the intention to connect with theory is good, this appendix lacks the rigor expected for PRD. Presenting a physically inconsistent operator, even as a toy model, detracts from the observational solidity of the main paper.
*   **Required Fix:** Remove Appendix A. The main text can briefly state that the null result provides an empirical upper bound for any future model-building in this area, without introducing a speculative and flawed operator.

#### MINOR Revisions

**P5-m1: Typo in Data Cuts**
*   **Section:** III.B (p. 3).
*   **Problem:** The text states quality cuts include `0.01 ≤ x ≤ 4`. The variable for redshift is universally `z`. The abstract uses `z` correctly.
*   **Required Fix:** Change `x` to `z`.

**P5-m2: Inconsistent Precision for Input Row Count**
*   **Section:** Abstract (p. 1) vs. III.B (p. 3).
*   **Problem:** The abstract quotes "16.36 × 10⁶ ZWARN=0 input rows", while the body gives the more precise "16,361,731 rows".
*   **Required Fix:** Use the precise number from the body in the abstract, or explicitly state that the abstract value is an approximation (e.g., "~16.4 million").

**P5-m3: Uncomputed Effect Size for Contingency Test**
*   **Section:** Abstract (p. 2, Robustness) and VI.A (p. 12).
*   **Problem:** The paper reports a highly significant contingency test result: `χ² = 4932, 3 d.o.f., log10 p ≈ -1069`. As required, it also reports the effect size, Cramér's V = 0.078, and correctly interprets this as "a small effect". However, the abstract on page 2 reports a similar test (`χ² = 4932, 3 d.o.f., log10 p ≈ -1069, Cramér's V = 0.078`) but the interpretation is slightly different. The abstract on page 1 does not report the effect size for the `χ² = 3.55` test.
*   **Required Fix:** Ensure that for every statistically significant χ² test, the effect size (Cramér's V) is reported and interpreted in both the abstract and the body. For the non-significant test (χ²=3.55), no effect size is needed. The interpretation of the significant test should be consistent.

#### NITs

**P5-N1: Future Date on Manuscript**
*   **Section:** Title page (p. 1).
*   **Problem:** The manuscript is dated "June 13, 2026".
*   **Required Fix:** Correct the date to the submission date.

**P5-N2: Internal File Paths in Text**
*   **Section:** Abstract (p. 1) and elsewhere.
*   **Problem:** The text contains internal-looking file paths, e.g., `pipelines/p2_chirality/`. While these may point to public repositories, they should be formatted as proper citations or footnotes.
*   **Required Fix:** Replace raw paths with formal references or footnotes explaining where to find the data/code.

---

### Summary Recommendation

**MAJOR REVISIONS**

The paper represents a significant amount of careful work and provides a valuable null result on a topic of cosmological interest. The statistical analysis is thorough and the author has gone to great lengths to check for robustness. However, the manuscript is not ready for publication. The absolute dependence on an "in preparation" paper for its core data and systematics is a critical flaw that must be rectified. Additionally, the potential sign error in the methodology, the excessive length, and the poorly written abstract are major obstacles. I recommend that the paper be reconsidered for publication only after these essential and major issues have been thoroughly addressed. If the author can successfully revise the manuscript, it will be a solid and useful contribution.