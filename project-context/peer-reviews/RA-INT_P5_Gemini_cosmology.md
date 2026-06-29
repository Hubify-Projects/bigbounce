# P5 RA-INT — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` md5=eab9162e pages=34
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 170.2s

---

Referee Report on "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample"

This manuscript presents a detailed statistical analysis searching for a correlation between the observed chirality (handedness) of spiral galaxies and their large-scale structure environment, using data from the DESI Data Release 1. The primary method involves cross-matching a large catalog of galaxy chiralities with DESI redshifts, classifying the environment using the T-Web tidal-tensor method, and performing a primary cross-check using the DESIVAST void catalog. The authors report a null result, finding no evidence for an environmental dependence of spiral chirality beyond a previously identified, catalog-wide systematic monopole offset in the chirality classifier. The analysis is exceptionally thorough, featuring an extensive suite of robustness checks, cross-validations against multiple classifiers, and a transparent discussion of systematics and limitations.

While the technical execution of the analysis is of a very high standard, there are several issues, one of which is essential, that must be addressed before the paper can be considered for publication in Physical Review D.

### ESSENTIAL Revisions

**P5-E1: Reliance on an In-Preparation Manuscript for Primary Data and Systematics**
*   **Section:** Throughout, but critically in Sec. I (p. 3), Sec. II (p. 3), Sec. III A (p. 4), and Table I (p. 4).
*   **Problem:** The entire analysis is predicated on two crucial inputs from "Paper IV [3] (in preparation)": (1) the per-galaxy CW/CCW chirality labels, and (2) the value of the catalog-wide classifier-monopole offset (`Afcw = -0.0026`), which is treated as a known systematic. The central argument of the present manuscript is that all observed environmental signals are projections of this monopole. Without access to Paper IV, the reader cannot scrutinize the methodology used to generate the chirality labels or the evidence supporting the existence and value of the monopole. A peer-reviewed paper cannot be fundamentally dependent on unpublished, unavailable work. This violates the principle that a paper must be self-contained and its results verifiable.
*   **Fix:** The manuscript cannot be published until Paper IV is publicly available, at minimum as a preprint on a service such as arXiv. The reference [3] must be updated to point to this public version. The authors should also consider summarizing the key aspects of the classifier and monopole determination from Paper IV more extensively in an appendix to make the present work more self-contained.

### MAJOR Revisions

**P5-M1: Abstract is Overly Dense and Technical**
*   **Section:** Abstract (p. 1).
*   **Problem:** The abstract is written more like a technical summary for experts than an accessible overview for a general Physical Review D readership. It is saturated with jargon (e.g., "post-TTA equivariant", "monopole-referenced tests", "omnibus 4 × 2 homogeneity test"), specific internal sample names ("DESIVAST primary", "T-Web secondary"), and a barrage of statistical values. A reader not already deeply familiar with the analysis would struggle to extract the main scientific result and its significance.
*   **Fix:** Rewrite the abstract to be more concise and focused on the high-level scientific question, the main result, and its implications. Start with the physical motivation. State the primary result (no environmental dependence found) and the key statistic (e.g., the void-vs-non-void contrast `Afcw = +0.0007 ± 0.0022`). Briefly mention the robustness of this null result across different methods and scales, but defer the exhaustive list of statistical tests to the main text. The abstract should be understandable to a physicist who is not an expert in cosmic-web classification or galaxy morphology.

**P5-M2: Unclear Scoping of "Largest Test" Claim**
*   **Section:** Sec. VIII B (p. 18).
*   **Problem:** The paper states, "This DESIVAST-anchored re-analysis is, within this custom chirality catalog and the DESI DR1/DESIVAST matched-sample construction used here, the largest matched-sample environmental-dependence test of spiral chirality we are aware of...". While the careful internal caveats ("within this custom... construction") are good, this claim of "largest" is difficult to verify and depends heavily on the specific definition of the test. Is it largest by number of spirals with environmental labels? By volume? By number of void spirals?
*   **Fix:** The claim should be made more precise and directly verifiable. For example: "With 56,981 spirals in DESIVAST-defined voids, this analysis provides the largest sample of void-resident spirals tested for chiral bias to date." Avoid general "largest test" claims and instead focus on the specific, quantifiable aspect that is unprecedented.

**P5-M3: Effect Size for Key Residual Signal**
*   **Section:** Sec. VI D (p. 12), Sec. XI (p. 28).
*   **Problem:** The paper identifies the bright-vs-dark target-program split as the "most notable residual structure" (`|z| ≈ 2.1` for filament class, `|z| = 1.95` for the whole catalog). While the statistical significance is given, the practical significance (effect size) is not always at the forefront. The `0.81 pp` difference is mentioned, but the discussion of the `χ² = 4933` test for program-vs-environment dependence (p. 13) correctly notes the large sample size drives the significance, and reports a small Cramér's V of 0.078. This excellent practice should be applied consistently.
*   **Fix:** When introducing the bright-vs-dark split as the main residual, immediately state the small effect size (the `0.81 pp` difference in `fcw`). This properly frames the "statistically significant" `z`-score as corresponding to a physically small effect, which reinforces the paper's overall null conclusion.

### MINOR Revisions

**P5-m1: Awkward Statistical Notation**
*   **Section:** Throughout, e.g., Sec. V (p. 6).
*   **Problem:** The notation `σ_from_half` is used for the standard one-sample binomial z-score against a null of p=0.5. While defined correctly, the name is non-standard and clunky. Similarly, `σ_vs_monopole` is descriptive but long.
*   **Fix:** Consider using more standard notation. For `σ_from_half`, simply using `z` or `σ` and stating in the text that it's the deviation from parity (p=0.5) would be clearer. For the monopole-subtracted residual, a notation like `Δσ = σ_obs - σ_pred` could be defined once and used thereafter. This is a suggestion for clarity; the current notation is not incorrect, merely awkward.

**P5-m2: Verification of V2-REVOLVER Native Contrast**
*   **Section:** Abstract (p. 1) and Sec. VIII D (p. 20).
*   **Problem:** The abstract quotes `Afcw <= 0.004 with |zo| <= 1.25 (p >= 0.21), Table XI`. Table XI (p. 20) shows the sphere-PIS results, not the catalog-native results. The native results are described in the text of Sec. VIII D (p. 20). The V2-REVOLVER native contrast has `z_Δ = -1.25` and `p_Δ = 0.21`. The `Afcw` is `-0.0037`. The absolute value of the contrast is `0.0037`, which is indeed `<= 0.004`. The citation is slightly confusing.
*   **Fix:** In the abstract, clarify the link between the numbers. E.g., "...robust across all five DESIVAST void-finders (e.g., V2-REVOLVER catalog-native `Afcw = -0.0037`, `|z_Δ| = 1.25`, `p = 0.21`; see Sec. VIII D), with all contrasts satisfying `|Afcw| <= 0.004`." This makes the provenance of the example numbers explicit.

**P5-m3: Dimensionality of Tidal Tensor Footnote**
*   **Section:** Sec. I (p. 3, footnote a).
*   **Problem:** The footnote defines `T_ij = ∂²Φ/∂x_i∂x_j`. This is correct. It then says "the Hahn 2007 recipe, sometimes called the T-Web variant". Hahn et al. 2007 actually use the deformation tensor, which is the tidal tensor normalized by the expansion rate, making it dimensionless. The text here uses the unnormalized (and dimensionful) tidal tensor.
*   **Fix:** This is a minor point of nomenclature, as the classification only depends on the sign of the eigenvalues relative to a threshold, which is unaffected by a positive definite normalization. However, for precision, the authors could state: "We use the unnormalized tidal tensor `T_ij = ∂²Φ/∂x_i∂x_j`, whose eigenvalue signs correspond to those of the dimensionless deformation tensor used in Hahn et al. 2007."

### NIT-PICKING

**P5-N1: Date Format**
*   **Section:** Title page (p. 1).
*   **Problem:** The date is given as "June 28, 2026". This is presumably a placeholder for the submission date, but it is in the future.
*   **Fix:** Replace with the actual submission date.

## Summary recommendation

**MAJOR REVISIONS**

This is a methodologically impressive and exceptionally rigorous paper that presents a strong null result on an important physical question. The level of detail, transparency about post-hoc choices, and the sheer number of robustness checks are commendable and set a high standard for future work in this area. The reproducibility infrastructure is exemplary.

However, the paper cannot be published in its current form due to its critical dependence on an "in-preparation" companion paper (Paper IV) for its primary data and systematic calibration. This is a fundamental issue of verifiability. The recommendation for **MAJOR REVISIONS** is therefore contingent on Paper IV being made publicly available on arXiv. Once that condition is met, the authors should also address the other major points, primarily by rewriting the abstract for clarity and accessibility. If Paper IV is not made available, the paper would have to be rejected. Assuming the authors can meet these requirements, the revised manuscript will represent a significant and valuable contribution to the literature.