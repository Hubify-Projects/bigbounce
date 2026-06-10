# P5 2026-06-04_R6clean — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 69.3s

---

**Referee Report on "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals" by H. Golden**

**General Comments**

This manuscript presents a detailed and comprehensive search for an environmental dependence of spiral galaxy chirality using DESI DR1 data. The core of the analysis is a null test, comparing the fraction of clockwise (CW) spirals in different large-scale structure environments (voids, walls, filaments, clusters). The author employs multiple cosmic-web classifiers (V-Web, DESIVAST, Tempel+2014 FoF, ASTRA) and a wide array of statistical tests and robustness checks to validate the primary finding: there is no evidence for an environment-dependent chirality signal at the sensitivity level of the current data.

The paper's main strengths are its statistical rigor, the careful treatment of systematics, and the use of multiple independent datasets and algorithms to confirm the result. The primary analysis, anchored on the publicly available and peer-reviewed DESIVAST void catalog, is particularly strong and provides the most compelling evidence for the paper's conclusion. The interpretation of observed statistical fluctuations in terms of a global, environment-independent classifier monopole (imported from a companion paper, "Paper IV") is applied consistently and appears well-justified by the data.

However, the manuscript has several significant issues that must be addressed before it can be considered for publication in Physical Review D. The most critical is its heavy reliance on an unpublished, un-refereed companion paper for its entire quantitative error framework. Additionally, the paper's structure and length obscure the main result, and the treatment of certain theoretical aspects, such as redshift-space distortions and the effective field theory mapping, requires refinement.

The following is a detailed list of required revisions.

---
**List of Findings**

**ESSENTIAL**

*   **P5-E1: Foundational Reliance on an Un-refereed Companion Paper (Paper IV)**
    *   **Section:** Throughout, starting from Abstract and Sec. II (p. 2).
    *   **Problem:** The entire quantitative analysis and interpretation of this manuscript (P5) is predicated on results from "Paper IV" [3], which is described as "a companion work by the same author, currently in preparation and not yet peer reviewed." Specifically, the value of the catalog-wide monopole offset (Δf_CW = -0.0026) is taken as a direct input to calculate the predicted deviation `σ_pred` (Eq. 1) and to perform the crucial monopole-subtraction analysis (e.g., Sec. VIII F, Table X). A peer-reviewed paper cannot be fundamentally based on un-reviewed, unavailable work. While P5 does an excellent job showing the data is *consistent* with this monopole, it does not derive it independently.
    *   **Required Fix:** The manuscript must be made self-contained. The author should perform an analysis on the DESI DR1 matched sample to derive the global monopole offset directly from this dataset, treating it as a nuisance parameter. The analysis should then proceed using this internally-derived value. Alternatively, Paper IV must be made publicly available (e.g., on arXiv) and its relevant results summarized in an appendix in the present manuscript, so that its methods and conclusions can be scrutinized as part of this review. As it stands, the core premise of the paper is unverifiable.

**MAJOR**

*   **P5-M1: Paper Length and Narrative Structure**
    *   **Section:** Entire manuscript.
    *   **Problem:** For a null result, the paper is excessively long (20 pages) and the narrative is convoluted. It jumps between the V-Web analysis (which is shown to be limited by small sample sizes and systematics), the primary DESIVAST analysis, and several other cross-checks. This structure buries the lede: the clean, high-statistics null result from the DESIVAST catalog. The V-Web analysis, with its tiny void sample (n=428) and systematics, receives disproportionate attention in the main body of the text.
    *   **Required Fix:** The paper must be significantly restructured and shortened. I recommend the following structure:
        1.  **Main Text (target length: 5-7 pages):** Focus exclusively on the primary, most robust analysis. This should be the DESIVAST-anchored test (Sec. VIII). This section is the core contribution and presents a clean, compelling null result on a large, well-defined sample.
        2.  **Appendices:** Move all secondary and supporting analyses to appendices. This includes: the detailed V-Web analysis (Sec. VI-VII), the Tempel+2014 cross-check (Sec. IX A), the ASTRA cross-check (Sec. X), and the discussion of other concurrent literature (Sec. IX B). This would dramatically improve the clarity and impact of the main result, while preserving the valuable robustness checks for the interested reader.

*   **P5-M2: Treatment of Redshift-Space Distortions (RSDs)**
    *   **Section:** Primarily Sec. XIII (p. 18), but relevant to Sec. IV-VII.
    *   **Problem:** The V-Web classification is performed on galaxy positions in observed redshift space. The paper correctly notes in the Limitations (Sec. XIII) that the dominant RSD effect is anisotropic eigenvalue deformation, not just scalar displacement, and that a proper treatment requires a field-level reconstruction. However, this critical caveat is mentioned only at the very end of the paper. The entire V-Web analysis (Sec. IV-VII) is presented without this context.
    *   **Required Fix:** Acknowledge the redshift-space nature of the V-Web analysis upfront in Sec. IV. A concise version of the discussion currently in Sec. XIII should be moved to Sec. IV to properly frame the V-Web results and their intrinsic systematic uncertainties from the outset. This also reinforces the decision to designate the DESIVAST analysis (which is argued to be largely RSD-immune) as the primary path.

*   **P5-M3: Abstract Clarity and Focus**
    *   **Section:** Abstract (p. 1).
    *   **Problem:** The abstract is dense and follows the convoluted structure of the main paper. It gives nearly equal weight to the V-Web analysis and the DESIVAST analysis, despite the paper demonstrating that the former is statistically weak and artifact-dominated, while the latter provides the controlling constraint.
    *   **Required Fix:** Rewrite the abstract to reflect the proposed new structure of the paper. It should lead with the primary, strongest result from the DESIVAST-anchored analysis (the null result on 56,981 void spirals). Then, briefly mention that this result is supported by several cross-checks, including a V-Web analysis, which is consistent despite its own limitations.

**MINOR**

*   **P5-m1: Toy EFT Mapping in Appendix A**
    *   **Section:** Appendix A (p. 19).
    *   **Problem:** The toy operator presented, `L_parity ⊃ g_ϕ (∇_i ϕ) (∇_i ρ/ρ_bg) (L̂ · ẑ)`, contains the term `(L̂ · ẑ)`, which is explicitly not rotationally invariant and depends on an arbitrary coordinate system choice. The text acknowledges this, calling it "shorthand for a rotationally-invariant pseudoscalar," but this is imprecise for a theoretical physics journal.
    *   **Required Fix:** Replace the problematic term with a proper pseudoscalar that can be constructed from the physical vectors available, for example `(L̂ · ∇ρ)`. While the appendix is speculative, its formulation should adhere to basic physical principles. The author should also consider whether this appendix adds sufficient value to warrant its inclusion, as it is highly schematic.

*   **P5-m2: Future Date in Manuscript**
    *   **Section:** Title block (p. 1).
    *   **Problem:** The paper is dated "June 4, 2026".
    *   **Required Fix:** Correct the date to the current submission date.

*   **P5-m3: Clarification of the 3.4σ Filament Signal**
    *   **Section:** Abstract (p. 2) and Sec. VI D (p. 7).
    *   **Problem:** The paper finds a `|z| ≈ 3.4σ` difference between bright and dark samples in the filament class and interprets it as a selection-function systematic. The argument for this interpretation is plausible (correlation between V-Web class and target program, signal only in the bright sample). However, this is the most significant "signal" in the paper, and dismissing it requires a very clear and strong argument.
    *   **Required Fix:** In the abstract, explicitly state that this 3.4σ deviation is interpreted as a non-astrophysical systematic and that the primary analysis is constructed to be insensitive to it. In the main text (Sec. VI D), slightly strengthen the argument by emphasizing that a genuine cosmological signal would be expected to appear in both the BGS-bright and LRG/ELG/QSO-dark populations, which trace the same underlying large-scale structure.

**NIT**

*   **P5-N1: Immutable Revision Hash in Text**
    *   **Section:** Sec. II (p. 2).
    *   **Problem:** The text mentions the HuggingFace catalog revision `paper4-v1.0.122`. While excellent for reproducibility, this level of detail is better suited for a footnote or the data availability appendix, rather than the main prose.
    *   **Required Fix:** Consider moving the specific revision hash to a footnote to improve readability.

---
## Summary recommendation
**MAJOR REVISIONS**

This paper presents a valuable and robust null result that provides an important empirical upper bound on the environmental dependence of cosmic parity violation. The analysis is comprehensive and the author has been careful to perform numerous cross-checks. However, the paper in its current form is not acceptable for publication. The foundational reliance on an unpublished and unavailable companion paper is a critical flaw that violates the principles of peer review. Furthermore, the paper's length and structure obscure its primary contribution, and key theoretical caveats are not presented with sufficient prominence. If the author can satisfactorily address the essential and major issues outlined above—primarily by making the analysis self-contained and by significantly restructuring the manuscript to focus on the strongest result—the paper will represent a solid contribution to the field.