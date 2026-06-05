# P5 2026-06-04_R5clean — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 65.0s

---

## Referee Report on "Environmental Dependence of Spiral Chirality..." (P5)

This paper presents a detailed statistical analysis searching for a correlation between the chirality of spiral galaxies and their large-scale structure environment, using data from DESI DR1. The authors cross-match a large, new chirality catalog with DESI redshifts and employ several cosmic-web classification schemes, primarily the tidal-tensor-based V-Web method and the void-catalog-based DESIVAST method. The main conclusion is a null result: spiral chirality is found to be statistically independent of environment at the sensitivity level of the current data, after accounting for a small, previously identified global systematic offset in the chirality catalog.

The analysis is comprehensive, featuring numerous robustness checks, sensitivity tests, and cross-validations against different classifiers and data subsets. The authors are commendably transparent about potential issues, such as the post-hoc designation of their primary analysis path and the presence of a residual systematic signal in a specific data subset. However, there are several critical issues that must be addressed before the paper can be considered for publication.

### ESSENTIAL

**P5-E1: Dependence on non-peer-reviewed work**
- **Location:** Abstract, Sec. II (p. 2), throughout.
- **Problem:** The entire analysis is critically dependent on "Paper IV" [3], which is cited as a "companion work, not yet peer-reviewed" and "in preparation." This external work provides two fundamental inputs: (1) the 8.47M-galaxy chirality catalog itself, and (2) the value of the catalog-wide monopole offset (∆f_CW = -0.0026), which is used throughout this paper to argue that observed deviations from parity are systematic, not environmental. The central claim of this paper—that there is no environmental signal beyond this monopole—is therefore unverifiable without access to a peer-reviewed and validated Paper IV.
- **Fix:** This paper cannot be accepted for publication until Paper IV is, at a minimum, accepted for publication or publicly available as a preprint with sufficient detail for its methods and results to be independently scrutinized. The status of reference [3] must be updated.

**P5-E2: Inadequate treatment of Redshift-Space Distortions (RSDs)**
- **Location:** Sec. VIII (p. 10), Sec. XIII (p. 18).
- **Problem:** The V-Web classification is performed on galaxy positions in observed redshift space. RSDs introduce anisotropic distortions into the density and peculiar velocity fields, which directly alters the tidal tensor and its eigenvalues, the core quantities used for classification. The current treatment of this effect in Section XIII is qualitative and insufficient for a precision analysis. The "scalar-displacement heuristic" (σ_v / (aH)) ignores the dominant anisotropic effects (Kaiser and Fingers-of-God), and the "order-of-magnitude boundary-crossing estimate" is not a substitute for a quantitative analysis. The claim in Section VIII that the primary DESIVAST analysis is "RSD-immune" is also a heuristic argument that needs to be demonstrated more robustly. An unquantified systematic from RSDs could potentially mask a small signal or mimic a null result.
- **Fix:** The authors must provide a more quantitative assessment of the impact of RSDs on their results. The recommended approach is to apply their full V-Web classification pipeline to realistic mock galaxy catalogs that include RSDs, and compare the resulting classifications and chirality statistics to a control run on the same mocks in real space. This would directly quantify the systematic uncertainty from RSDs. For the DESIVAST analysis, the claim of RSD immunity should be similarly tested using mocks.

### MAJOR

**P5-M1: Post-hoc definition of "primary" analysis and paper structure**
- **Location:** Sec. V B (p. 4-5), overall structure.
- **Problem:** The authors declare their "primary analysis path" (DESIVAST) *post-hoc* to mitigate the "garden-of-forking-paths" problem. While the transparency is appreciated, this significantly weakens the statistical claim. The paper's structure, which presents the V-Web analysis (Sec. VI) before revealing its flaws and introducing the "primary" DESIVAST analysis (Sec. VIII), reinforces the impression that the analysis path was chosen reactively. The primary test of a hypothesis should be established *a priori*.
- **Fix:** The paper must be restructured. The DESIVAST analysis, which the authors identify as their most robust and cleanest test, should be presented upfront as the main analysis of the paper. The V-Web analysis should then be presented as a supporting, full-sample study, with its limitations (e.g., the small and contaminated void sample, the bright/dark tension) clearly stated from the outset. The abstract and introduction should be revised to reflect this new structure, presenting a clear, pre-motivated analysis plan.

**P5-M2: Interpretation of the 3.4σ bright-vs-dark sign-flip**
- **Location:** Abstract (p. 1), Sec. VI D (p. 7).
- **Problem:** The paper reports a statistically significant (|z| ≈ 3.4σ) difference in the chirality signal between "bright" and "dark" galaxy samples within the filament class. This is dismissed as a non-astrophysical systematic related to the BGS selection function. However, the paper also shows that the environmental classification and target program are not independent (p < 10⁻¹⁰⁰⁰). This entanglement makes it difficult to cleanly partition the signal between a selection systematic and a potential astrophysical effect conditioned on galaxy type. Simply flagging this as a "real diagnostic for future follow-up" is insufficient, as it represents a significant unresolved tension in the current data that undermines the claim of a simple, global systematic.
- **Fix:** The authors need to provide a more compelling argument for why this signal is purely systematic. This could involve a more detailed model of the selection function's impact or further data splits that can help isolate the effect. The claim that the primary DESIVAST analysis is "insensitive" to this must be explicitly demonstrated, for instance by showing that the bright/dark split within the DESIVAST void/non-void samples does not produce a significant signal.

**P5-M3: Problematic Toy EFT Mapping**
- **Location:** Appendix A (p. 19).
- **Problem:** The toy operator presented in Appendix A, `L_parity ⊃ g_ϕ (∇_i ϕ) (∇_i ρ/ρ_bg) (L̂ · ẑ)`, is theoretically problematic. The `(L̂ · ẑ)` term explicitly breaks rotational invariance by selecting a fixed coordinate direction `ẑ`, which is unphysical. The text acknowledges this and other issues like gauge invariance but dismisses them by calling it a "toy parametrization." Presenting a fundamentally flawed operator, even with caveats, is misleading and adds little value. A proper pseudoscalar constructed from physical vectors (e.g., `L̂ · ∇ρ`) should have been used.
- **Fix:** The appendix should be either substantially revised to use a rotationally invariant pseudoscalar and a more careful discussion of gauge issues, or it should be removed entirely. As it stands, it detracts from the quality of the paper.

### MINOR

**P5-m1: Paper Length and Structure**
- **Location:** Entire paper.
- **Problem:** At 20 pages, the paper is lengthy for a null result. The narrative is complex, with numerous secondary analyses that, while thorough, can obscure the primary conclusion.
- **Fix:** In addition to the major restructuring suggested in P5-M1, the authors should consider moving some of the less central cross-validation studies (e.g., the detailed discussion of concurrent literature in Sec. IX B, or the ASTRA cross-check in Sec. X) into an appendix. This would streamline the main text and focus it on the core evidence for the null result. A target length of 15-16 pages for the main paper seems more appropriate.

**P5-m2: Clarity of σ-value comparisons**
- **Location:** Abstract and throughout.
- **Problem:** The paper reports many σ-values derived from different statistical tests (e.g., binomial deviation from parity, two-sample z-test). In the abstract, these are presented in rapid succession without explicitly stating the null hypothesis for each, which can be confusing for the reader.
- **Fix:** When reporting a significance value (σ), briefly state the null hypothesis being tested. For example, in the abstract, change "-2.61σ" to "-2.61σ from parity" and "|z| ≈ 3.4σ" to "|z| ≈ 3.4σ on the bright-vs-dark difference".

**P5-m3: Self-referential shorthand**
- **Location:** Sec. VIII F (p. 12), Sec. X (p. 16), Table X caption.
- **Problem:** The paper uses "P5" to refer to itself (e.g., "the primary P5 environment-independence claim"). This is unconventional and confusing.
- **Fix:** Replace all instances of "P5" as a self-reference with standard phrasing like "this work" or "the present paper."

**P5-m4: Citation of preprints**
- **Location:** Sec. IX B, Sec. X, References.
- **Problem:** The paper relies on several very recent (2026) preprints for cross-validation. While citing current work is appropriate, the non-peer-reviewed status of these works should be clearly stated.
- **Fix:** The authors have done this well for Ref. [11]. This practice should be applied consistently for all non-peer-reviewed citations used for validation, such as Ref. [12] (ASTRA).

### NIT

**P5-N1: Future date**
- **Location:** p. 1.
- **Problem:** The paper is dated "June 4, 2026".
- **Fix:** Correct the date to the actual date of submission.

**P5-N2: Unconventional symbol**
- **Location:** p. 14.
- **Problem:** The text "filament_like_vs_filament: 0.026 pp (✓ within spec)" uses a checkmark symbol (✓), which is not appropriate for a formal scientific publication.
- **Fix:** Rephrase this, for example: "...0.026 pp, which is well within the 0.2 pp concordance specification."

**P5-N3: Code-like variable name in caption**
- **Location:** Fig. 6 caption (p. 14).
- **Problem:** The caption uses the variable name `npix_both`.
- **Fix:** Rephrase to be more descriptive, e.g., "...across the 727 pixels that contain both..."

## Summary recommendation
**MAJOR REVISIONS**

The authors have performed an extensive and careful analysis of a large, modern dataset to test for an environmental dependence of spiral galaxy chirality. The work is thorough and the conclusion of a null result appears well-supported by the primary analysis. However, the paper in its current form has several significant flaws that prevent its acceptance. The critical dependence on a non-peer-reviewed companion paper and the inadequate quantitative treatment of redshift-space distortions are essential issues that must be fully resolved. Furthermore, the paper requires a major restructuring to present its analysis in a more logical, pre-motivated framework, and it must better address the 3.4σ tension found between bright and dark galaxy samples. If the authors can satisfactorily address these points, the revised manuscript will represent a solid and valuable contribution to the literature.