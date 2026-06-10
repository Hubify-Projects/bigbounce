# P5 R27conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.58.pdf` md5=6ffcd714 pages=27
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 131.8s

---

## Referee Report: Environmental Dependence of Spiral Chirality (P5)

This paper presents a detailed investigation into the potential dependence of spiral galaxy chirality on the large-scale structure environment. The authors cross-match a large catalog of spiral galaxies with classified handedness against the DESI DR1 redshift catalog. They employ multiple cosmic-web classifiers (primarily a tidal-tensor method called V-Web and the DESIVAST void catalog) and perform a comprehensive suite of null tests and robustness checks. The headline result is a null detection: spiral chirality, once corrected for a previously identified catalog-wide monopole bias, shows no statistically significant dependence on whether a galaxy resides in a void, wall, filament, or cluster.

The analysis is exceptionally thorough, exploring sensitivity to classifier hyperparameters, redshift, projected density, and sky position. The authors are commendably transparent about methodological choices, potential systematics, and limitations, including the post-hoc designation of the primary analysis path and the impact of redshift-space distortions (RSDs).

While the underlying analysis appears sound and the conclusion is likely robust, the manuscript in its current form has several issues that preclude publication in Physical Review D. The issues range from an essential structural dependency on an unpublished work to the unprofessional inclusion of internal review history, which must be addressed.

### Findings

#### ESSENTIAL

*   **P5-E1: Critical Dependency on Unpublished Work (Throughout, e.g., Abstract, Sec. II)**
    *   **Problem:** The entire analysis is predicated on inputs from "Paper IV [3] (companion work, not yet peer-reviewed)". Specifically, the chirality catalog itself and, more critically, the catalog-wide monopole offset (`Δf_cw = -0.0026`) are taken as given. This monopole is subtracted from all environment-class measurements to test for a *residual* environmental signal. Without the full methodology and validation of this monopole from Paper IV, the central quantitative claims of this paper (e.g., the monopole-subtracted residuals in Table X and the `σ_pred` calculations) are unverifiable. A paper submitted to PRD must be self-contained.
    *   **Fix:** The authors must either (1) incorporate the essential methodological details of the classifier and the derivation and validation of the monopole offset into an appendix of the present manuscript, or (2) wait to submit this paper until Paper IV is, at minimum, accepted for publication and publicly available on arXiv. The current state of dependency is unacceptable.

#### MAJOR

*   **P5-M1: Inclusion of Internal Review Artifacts and "Changelog" Text (Throughout)**
    *   **Problem:** The manuscript is littered with phrases that appear to be remnants of an internal review process or a "changelog" from a previous draft. This is highly unprofessional for a journal submission. Examples include:
        *   Page 2: "...an earlier harmonic-space subsample-mask MASTER-deconvolved l = 1 statistic was withdrawn in Paper IV v1.0.166 after a provenance audit..."
        *   Page 10: "An earlier draft quoted filament bright/dark n of 416,701/21,203... and are withdrawn in favor of the declared-parent recompute..."
        *   Page 11: "An earlier draft of this table reported per-cell ranges... those values are withdrawn in favor of the declared-parent recompute below."
        *   Page 21: "An earlier draft quoted an overlap of 110,586; that join... is withdrawn..." and "An earlier draft compared the Tempel overlap... that comparison... is withdrawn."
        *   Page 16: "An earlier draft reported n_void = 86,276 / 64,514... The corrected per-cap join values above supersede them..."
        *   Page 17: "An earlier draft attributed the excess to a 'relaxed env-label confidence filter'... replaces that description."
        *   Page 24: "An earlier draft of this summary stated the bright/dark split agreed 'within ±0.001'; that statement was stale and is corrected here..."
    *   **Fix:** The authors must perform a thorough proofread and remove all such text. The paper should present the final, definitive analysis without reference to its own version history.

*   **P5-M2: Excessive Length for a Null Result (Overall Structure)**
    *   **Problem:** At 27 pages, the paper is overly long for what is fundamentally a null result. While the thoroughness is appreciated, the narrative is diluted by the sheer number of secondary cross-checks presented in the main text. The core contribution is the DESIVAST-anchored null test and the V-Web hyperparameter robustness sweep. Other tests (Tempel FoF, ASTRA EDR, detailed z-shell corrections) are valuable but secondary.
    *   **Fix:** The paper should be significantly restructured and condensed. I recommend a target of 15-18 pages for the main text. The primary analysis (DESIVAST) and the main supporting analysis (V-Web Phase 2 sweep) should form the core of the paper. The Tempel, ASTRA, and detailed z-shell/geometry-footprint correction sections (§IX.B, §IX.C, §X, parts of §IX.A) should be heavily summarized in the main text and their detailed descriptions moved to an appendix. This will create a more focused and impactful paper.

*   **P5-M3: Post-Hoc Analysis Path Designation (Sec. V.B)**
    *   **Problem:** The authors commendably admit that "a single a priori preregistered analysis plan was not filed; the choice of which classifier to report as 'primary' is therefore made post-hoc". While this transparency is laudable, it is a significant methodological weakness that opens the door to the "garden of forking paths". The justification for choosing DESIVAST as primary (RSD insensitivity) is sound, but this choice and its justification should be presented upfront in the introduction or methods, not buried in a subsection.
    *   **Fix:** Elevate the discussion of the primary/secondary analysis choice to the introduction. State clearly that multiple analyses were performed and that the DESIVAST-anchored test was chosen as primary for specific, physically-motivated reasons (i.e., its robustness to RSDs compared to the V-Web method), which should be briefly explained there. This reframes the choice as a reasoned, post-hoc decision rather than an arbitrary one.

#### MINOR

*   **P5-m1: Redshift-Space Distortions in V-Web Analysis (Sec. XIII)**
    *   **Problem:** The authors correctly identify in the Limitations section that the V-Web analysis uses redshift-space positions, and that the dominant effect is "anisotropic eigenvalue deformation," which is not captured by a simple scalar displacement check. This is a crucial point that significantly limits the V-Web results. However, this caveat is not sufficiently emphasized when the V-Web results are first presented.
    *   **Fix:** In Section VI, where the headline V-Web results are presented, the authors should add a sentence or footnote explicitly stating that these results are derived from a redshift-space analysis and are subject to unquantified RSD effects, with a forward reference to the detailed discussion in Section XIII. This ensures the reader properly contextualizes the V-Web results from the outset.

*   **P5-m2: Toy EFT Model (Appendix A)**
    *   **Problem:** The toy EFT model in Appendix A is so heavily caveated ("toy parametrization," "not a derived constraint," "breaks rotational invariance," "not... a covariant EFT operator") that its utility is questionable. It risks being misinterpreted or over-interpreted despite the authors' warnings.
    *   **Fix:** The authors should consider removing Appendix A entirely. The observational bounds presented in the main text stand on their own. If they wish to retain it, they should add a sentence stating why such a schematic model is useful despite its profound theoretical limitations.

*   **P5-m3: Bibliography Inaccuracies (References)**
    *   **Problem:** There are errors in the bibliography. For example, Ref. [11] (Ullah et al.) is cited with a future year and an incorrectly formatted arXiv ID: "preprint (2026), arXiv:2604.02463". The correct ID is likely arXiv:2404.02463.
    *   **Fix:** The authors must carefully check all references for correctness, particularly for preprints, ensuring years and arXiv IDs are accurate.

#### NIT

*   **P5-N1: Future Date (Page 1)**
    *   **Problem:** The paper is dated "June 2026".
    *   **Fix:** Correct the date to the date of submission.

*   **P5-N2: V-Web/T-Web Nomenclature (Title, Sec. IV.A)**
    *   **Problem:** The authors state they use the Hahn 2007 tidal-tensor (T-Web) recipe but retain the "V-Web" label for historical reasons. The title itself uses both: "T-Web (Hahn 2007) Tidal-Tensor Cross-Check" and "A DESIVAST Three-Algorithm Test". This is slightly confusing.
    *   **Fix:** For clarity, consider consistently using "tidal-tensor classifier (T-Web)" throughout the text, while noting in the methods that this is sometimes referred to as V-Web in the literature.

### Summary recommendation

**MAJOR REVISIONS**

The paper presents a comprehensive and statistically rigorous null test for the environmental dependence of spiral galaxy chirality. The depth of the robustness checks is a significant strength. However, the manuscript is not yet acceptable for publication in Physical Review D. The critical reliance on an unpublished companion paper (P5-E1) is an essential flaw that must be rectified. Furthermore, the manuscript requires a thorough professional cleanup to remove extensive internal review artifacts (P5-M1) and a significant restructuring to improve focus and reduce its excessive length (P5-M2). If the authors can address these major points, particularly the dependency on Paper IV, the resulting manuscript would represent a valuable contribution to the field.