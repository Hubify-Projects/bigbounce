# P5 2026-06-04_R4fixed — Physical Review D cosmology-physics referee

**Model**: `google/gemini-2.5-pro` [FALLBACK from gemini-2.5-pro]
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 89.8s

---

## Referee Report: P5 (2026-06-04_R4fixed)

This paper presents a search for an environmental dependence of spiral galaxy chirality by cross-matching a new, large chirality catalog with DESI DR1. The environment is primarily classified using a V-Web tidal tensor analysis on the full DR1 spectroscopic sample, with a more robust, "primary" analysis focused on voids defined by the public DESIVAST catalog. The paper reports a null result, concluding that spiral chirality is independent of large-scale structure environment, with observed deviations being consistent with a catalog-wide monopole bias and statistical noise.

The analysis is comprehensive, including multiple environment classifiers, numerous null tests, and a detailed treatment of potential systematics. The distinction between a primary (DESIVAST-anchored) and secondary (V-Web) analysis path is a notable strength, allowing the author to ground the main conclusion on the most robust part of the analysis while still exploring the full dataset. The reproducibility standards are exceptionally high.

However, the paper has several essential and major issues that must be addressed before it can be considered for publication in Physical Review D. The most critical is its reliance on an unpublished, non-peer-reviewed companion paper for its primary dataset and a key systematic correction.

### ESSENTIAL

*   **P5-E1 (Throughout): Dependency on unpublished work.** The entire analysis is built upon the chirality catalog and the catalog-monopole correction from "Paper IV [3]," which is described as a "companion work, not yet peer-reviewed" and "currently in preparation." A published paper cannot be fundamentally dependent on data and core systematic corrections from a manuscript that is not publicly available and has not undergone peer review. The validity of the central assumption—that the catalog-wide `∆f_CW` is a classifier bias and not astrophysical—is established in Paper IV, but a referee for the present paper cannot verify this.
    *   **Required fix:** Paper IV must be, at a minimum, publicly available (e.g., on arXiv) and submitted for peer review. The referee must be given access to it to properly evaluate the current manuscript. The results of Paper IV must be sufficiently robust to support the claims made in this paper.

*   **P5-E2 (Sec. IX, p. 14; Ref. [3], [4]): Internal review artifacts in references.** The references for the companion papers [3] and [4] are given as internal file paths: `pipelines/p2_chirality/chirality_catalog_paper.tex` and `research/focused_paper_source_integration/02_full_draft.tex`. This is unacceptable for a publication.
    *   **Required fix:** Replace these internal paths with proper citations (e.g., "in preparation," or preferably an arXiv identifier).

*   **P5-E3 (Header): Version history artifact in header.** The header of the paper contains the string `ROUND: 2026-06-04_R4fixed`. This is an internal versioning tag.
    *   **Required fix:** Remove this internal versioning string from the manuscript.

### MAJOR

*   **P5-M1 (Overall Structure): Suboptimal narrative structure.** The paper presents the secondary, V-Web analysis (Sec. VI) before the primary, DESIVAST-anchored analysis (Sec. VIII). However, Sec. VIII.A demonstrates that the V-Web void classification is highly unreliable at low redshift (0/6 V-Web voids are in DESIVAST voids), and the V-Web void sample is statistically very weak (n=428). This structure forces the reader to first process a significant result (cluster at -4.7σ), digest the argument that it's a systematic, and only then discover that the void analysis it's compared against is flawed. The paper's strongest and most convincing evidence comes from the DESIVAST analysis.
    *   **Required fix:** Restructure the paper to present the primary, DESIVAST-anchored analysis (currently Sec. VIII) first. This is the most robust result and should be the foundation of the paper's narrative. The V-Web analysis should then be presented as a secondary, all-sky cross-check, with its limitations (especially regarding the void class and RSDs) stated upfront.

*   **P5-M2 (Abstract; Sec. VI.D.c, p. 8): Understatement of the 3.4σ filament signal.** The abstract claims "no evidence for environment-dependent chirality," but later mentions a `|z| ≈ 3.4σ` difference in `f_CW` between bright and dark target samples within the filament class. While the paper correctly flags this as a complex residual that cannot be cleanly partitioned between systematics and astrophysics, a 3.4σ effect is "evidence" that requires more prominence than it is given. The main "no evidence" claim feels too strong when such a signal is present in a major subsample.
    *   **Required fix:** The abstract and conclusions must be rephrased to more accurately reflect this finding. For example, state that while the primary DESIVAST-anchored analysis shows a clear null result for void environments, a significant (`>3σ`) systematic or potentially astrophysical signal is detected when stratifying the V-Web filament class by target selection program, which requires future investigation. The headline claim of "no evidence" should be softened to "no evidence in the primary void-based analysis, but with a significant residual found in a secondary analysis."

*   **P5-M3 (Sec. VII.A, p. 9): Incorrect claim about sensitivity floor.** The paper claims: "across nine (Rs , λth ) cells, the maximum per-cell inter-class fCW range is below the per-class counting-statistics floor". This is incorrect. The maximum range is 0.22 percentage points. The 1σ counting statistics uncertainty (`1/(2√n)`) for the filament and cluster classes (n ~ 4e5) is ~0.08 pp. The observed range is therefore ~2.75x larger than the statistical floor for these dominant classes. The statement is only true for the low-n wall and void classes.
    *   **Required fix:** Correct this statement. The argument for robustness should be rephrased. The key point is that the range is small in absolute terms and the per-class deviations are consistent with the monopole, not that the range is smaller than the statistical uncertainty of every class.

### MINOR

*   **P5-m1 (Sec. V, p. 4): Ambiguous description of null hypotheses.** The text states: "For hypothesis tests we run two complementary nulls: (i) a label-shuffle permutation that preserves positions but destroys any handedness signal; (ii) a position-shuffle that preserves labels but scrambles positions." However, the subsequent text and driver descriptions only seem to refer to the label-shuffle null. The role and results of the "position-shuffle" null are not clearly described or presented.
    *   **Required fix:** Clarify whether the position-shuffle null was used. If so, describe its purpose and results. If not, remove the mention of it to avoid confusion.

*   **P5-m2 (Appendix A, p. 20): Suboptimal formulation of toy EFT operator.** The appendix introduces a toy operator `L_parity ⊃ g_ϕ (∇_i ϕ) (∇_i ρ/ρ_bg) (L̂ · ẑ)`. The author correctly identifies that the `(L̂ · ẑ)` term breaks rotational invariance and is just a schematic. However, this is unnecessarily sloppy. A rotationally invariant pseudoscalar could easily be constructed and used for the schematic, for example `L̂ · ∇ρ`.
    *   **Required fix:** Replace the `(L̂ · ẑ)` term with a more physically appropriate, rotationally invariant pseudoscalar (e.g., `L̂ · ∇ρ` or `L̂ · ∇ϕ`), while retaining the important caveats about it being a toy model in a specific gauge.

*   **P5-m3 (Abstract): Presentation of σ values.** The abstract reports a -4.66σ deviation for the cluster class. While this is immediately qualified as tracking the catalog monopole, presenting a raw significance of this magnitude in the abstract can be misleading to readers who skim.
    *   **Required fix:** Consider reporting the residual significance after monopole subtraction (i.e., `σ_vs_monopole` from Table X, which is -1.11) in the abstract for the V-Web classes. This would more directly support the paper's main conclusion. Alternatively, keep the raw sigma but add the predicted sigma in parentheses, e.g., "-4.66σ (vs. -3.28σ predicted from monopole)".

*   **P5-m4 (Sec. X, p. 17): Confusing sentence about future VAC.** The text states: "...the closest currently available substitute for the full-DR1 environmental VAC discussed in §XIII." Section XIII mentions that a full-DR1 VAC is not yet published, but it doesn't discuss it in a way that this sentence clearly refers back to.
    *   **Required fix:** Rephrase for clarity, for example: "...the closest substitute for a future, full-DR1 environmental value-added catalog (VAC)."

### NIT (Nitpicks)

*   **P5-N1 (Sec. IX, p. 14; Refs. [11], [12], [13]): Futuristic publication dates.** References [11], [12], and [13] have publication years of 2026 and 2025. While these may be placeholders for forthcoming articles, they should be formatted as "in press" or simply list the arXiv preprint year if the journal publication is not yet finalized.
    *   **Required fix:** Correct the years on these references to reflect their current status (e.g., the year of the arXiv preprint).

*   **P5-N2 (Sec. X, p. 17): Internal-sounding jargon.** The phrase "within this campaign" sounds like internal collaboration jargon.
    *   **Required fix:** Rephrase to something more formal, such as "in this analysis" or "in this work."

## Summary recommendation
**MAJOR REVISIONS**

This paper tackles an interesting question with a powerful new dataset and a rigorous, multi-pronged analysis. The author's transparency regarding potential issues (e.g., the "garden of forking paths," limitations of V-Web) and the high standard of reproducibility are commendable. The primary DESIVAST-anchored analysis provides a strong null result for the environmental dependence of chirality in cosmic voids. However, the paper in its current form is not acceptable for publication. The absolute dependence on an unpublished and non-peer-reviewed companion paper (Paper IV) for the core dataset is an essential flaw that must be rectified. Furthermore, the paper's structure weakens its narrative, and the abstract and conclusions do not fully and accurately represent the complexity of the findings, particularly the 3.4σ signal found in the secondary analysis. After these major revisions are completed, the paper should be re-reviewed.