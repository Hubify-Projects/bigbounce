# P5 R10v3 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API)
**Wall time**: 62.3s

---

**Referee Report for "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals"**

This paper presents a comprehensive search for an environmental dependence of spiral galaxy chirality using a large dataset derived from DESI Data Release 1. The authors cross-match a new, large chirality catalog with DESI spectroscopic redshifts to classify galaxies into cosmic-web environments using several different algorithms. The primary conclusion is a null result: spiral chirality is found to be statistically independent of environment, once a previously identified catalog-wide monopole bias is accounted for. The analysis is extensive, including numerous robustness checks and cross-validations against different classifiers and data subsets.

While the work is thorough and the conclusion is potentially important, the paper suffers from several structural and methodological issues that must be addressed before it can be considered for publication. The reliance on an unpublished companion paper for the primary data product is a critical flaw, and the paper's structure obscures the most robust results.

---

### Detailed Findings

#### ESSENTIAL

*   **P5-E1** | **Page 1, Metadata** | **Future Date**
    *   **Problem:** The paper is dated "June 4, 2026". This is a future date.
    *   **Required Fix:** Correct the date to the current submission date.

*   **P5-E2** | **Page 1, Abstract** | **Misleading Abstract Structure and Headline Result**
    *   **Problem:** The abstract and the paper's "headline result" (Section VI A) are framed around the V-Web cosmic-web classification. However, the paper itself demonstrates that the V-Web void classification is severely limited by small sample size (n=428) and contaminated by survey-edge artifacts at low redshift (Section VIII A shows 0% concordance with the superior DESIVAST void catalog). The most robust and compelling result in the paper is the DESIVAST-anchored analysis (Section VIII), which uses a peer-reviewed void catalog and a ~130x larger void sample. Leading with the weaker, flawed analysis is misleading.
    *   **Required Fix:** Rewrite the abstract and restructure the paper to present the DESIVAST-anchored analysis as the primary result. The V-Web analysis should be presented as a secondary, supporting cross-check that covers a larger redshift range but with significant, stated caveats. The abstract's headline must be the DESIVAST result.

#### MAJOR

*   **P5-M1** | **Throughout** | **Critical Dependency on Unpublished Work**
    *   **Problem:** The entire analysis is predicated on the 8.47M-galaxy chirality catalog from "Paper IV" [3], which is cited as "companion work, not yet peer-reviewed" and "in preparation". This makes the present paper impossible to properly evaluate, as the source of the fundamental data (the CW/CCW labels) is not available. Key properties of this catalog, such as the classifier architecture, training data, and the origin of the "-0.0026" monopole offset, are asserted without proof.
    *   **Required Fix:** The paper cannot be published in its current state. The authors must, at a minimum, provide a copy of Paper IV to the referees. The preferred solution is to incorporate the essential methodological details of the chirality classification and monopole determination from Paper IV into an appendix of the present manuscript, making it self-contained.

*   **P5-M2** | **Page 5, Section V B** | **Post-Hoc "Primary Path" Designation and Paper Structure**
    *   **Problem:** The author explicitly states that the choice of the "primary" analysis path (DESIVAST) was made post-hoc. This "garden of forking paths" approach weakens the statistical power of the conclusion. The paper's structure, which presents the V-Web analysis first and in more detail before revealing its flaws and switching to the "primary" DESIVAST analysis, is confusing and narratively weak.
    *   **Required Fix:** Restructure the paper as suggested in P5-E2. The DESIVAST analysis (Section VIII) should be moved up to become the main results section (e.g., Section VI). The current Section VI (V-Web) should be moved later and framed as a secondary analysis. This restructuring resolves the post-hoc justification issue by presenting the most robust analysis first.

*   **P5-M3** | **Page 2, Abstract & Page 8, Section VI.d** | **Downplaying of a Significant Residual Signal**
    *   **Problem:** The analysis uncovers a statistically significant (joint |z| ≈ 3.4σ) sign-flip in the chirality fraction for the filament class between the BGS-bright (σ = -2.80) and tracer-dark (σ = +2.85) samples. The abstract presents a clean null result, but the body states this is a "real residual structure". While the authors plausibly argue it may stem from selection-function systematics, this is a non-trivial feature of the data that contradicts a simple "no environmental dependence" conclusion.
    *   **Required Fix:** The abstract and conclusion must be revised to be more nuanced. They should explicitly mention this 3.4σ tension, state the authors' interpretation (likely systematics), and acknowledge that it is a feature requiring future follow-up. The current framing, which buries this result and presents an unqualified null, is an oversimplification.

#### MINOR

*   **P5-m1** | **Page 19, Appendix A** | **Speculative EFT Mapping**
    *   **Problem:** Appendix A presents a "toy EFT mapping" that is highly speculative, not derived from any established theory, and not a result of the paper's analysis. The author includes many caveats, but its inclusion detracts from the paper's focus as a rigorous observational study.
    *   **Required Fix:** Recommend removing Appendix A to keep the paper focused. The content, if deemed essential, could be heavily condensed into a single, well-caveated paragraph in the Discussion section.

*   **P5-m2** | **Throughout** | **Citations to Future Publications**
    *   **Problem:** Several key references are to publications with future dates (e.g., Rincón et al. 2025 [13], Ullah et al. 2026 [11], Zapata-Zuluaga et al. 2026 [12]).
    *   **Required Fix:** For any cited work that is not yet published in a journal, the citation should point to the public arXiv preprint. Update the references accordingly.

*   **P5-m3** | **Page 15, Section IX B** | **Interchangeable Terminology**
    *   **Problem:** The text discusses "sheet" (from T-Web) and "wall" (from V-Web) as corresponding cosmic-web structures. While standard in the field, this can be confusing.
    *   **Required Fix:** Add a single sentence at the first point of comparison (e.g., in Section IX B) clarifying that "sheet" and "wall" refer to the same type of 2D structure.

*   **P5-m4** | **Page 3, Table I** | **Unclear Quantity Definition**
    *   **Problem:** The quantity "P99 separation" is listed. Its meaning is not explicitly defined.
    *   **Required Fix:** Clarify in the table caption or text that this is the 99th-percentile angular separation of matched pairs.

#### NIT

*   **P5-N1** | **Page 1, Abstract** | **Inconsistent Notation**
    *   **Problem:** The text states "none reach 30 after look-elsewhere correction".
    *   **Required Fix:** Write as "3σ" for consistency with standard notation used elsewhere in the paper.

*   **P5-N2** | **Page 2, Section I** | **Awkward Phrasing**
    *   **Problem:** The phrase "consistent with parity at ~ 1σ".
    *   **Required Fix:** Rephrase to "at the ~1σ level" or "within ~1σ".

*   **P5-N3** | **Page 11, Table VII Caption** | **Typo**
    *   **Problem:** "statistically indistinguish- able".
    *   **Required Fix:** Hyphenate: "statistically indistinguishable".

*   **P5-N4** | **Page 13, Section IX A** | **Typo in Multiplicity Cut**
    *   **Problem:** The bullet point for cluster_like states "multiplicity > 20". The preceding line for filament_like is "5 ≤ multiplicity < 20". This implies a gap. The source paper (Tempel et al. 2014) uses N ≥ 20 for clusters.
    *   **Required Fix:** Change "multiplicity > 20" to "multiplicity ≥ 20".

*   **P5-N5** | **Page 8, Section VII E** | **Typo**
    *   **Problem:** "max-|0|".
    *   **Required Fix:** This should be "max-|σ|".

*   **P5-N6** | **Page 17, Section XI** | **Typo**
    *   **Problem:** "pmaq".
    *   **Required Fix:** This should likely be "p_max" or "p_conf" depending on the variable name for the confidence threshold. Please clarify and correct.

*   **P5-N7** | **Page 18, Section XIII** | **Unit Formatting**
    *   **Problem:** "συ≤ 400 kms-1".
    *   **Required Fix:** Use proper formatting: "km s⁻¹".

---

## Summary recommendation

**MAJOR REVISIONS**

This paper presents a valuable and impressively thorough null result on the environmental dependence of galaxy chirality. The extensive suite of robustness checks, particularly the DESIVAST-anchored analysis and the cross-validation with ASTRA and Tempel+2014 classifiers, makes a strong case for the conclusion. However, the paper is critically hampered by its reliance on an unpublished work for its primary data, a confusing structure that foregrounds the weakest analysis, and an oversimplified summary that downplays a significant residual signal found in the data. The required revisions are substantial but will transform the manuscript into a robust, clear, and important contribution. Acceptance is contingent on the authors satisfactorily addressing the ESSENTIAL and MAJOR points listed above, most critically by making the paper self-contained and by restructuring it to lead with the strongest evidence.