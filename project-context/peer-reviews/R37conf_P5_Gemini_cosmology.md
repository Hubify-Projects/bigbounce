# P5 R37conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.72.pdf` md5=544b6af2 pages=32
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 130.2s

---

## Referee Report: P5

**Title:** Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample

**Manuscript ID:** P5

---

This manuscript presents a detailed investigation into the potential environmental dependence of spiral galaxy chirality using data from the DESI Data Release 1 and a companion chirality catalog. The primary conclusion is a null result: no statistically significant correlation between galaxy handedness and large-scale structure environment (voids, walls, filaments, clusters) is found, beyond a known catalog-wide systematic and statistical noise. The analysis employs multiple environmental classifiers (V-Web, DESIVAST, Tempel FoF, ASTRA) and a variety of statistical tests to establish the robustness of this null finding.

While the underlying analysis appears to be computationally rigorous and the author has performed numerous valuable cross-checks, the manuscript in its current form is not suitable for publication in Physical Review D. It suffers from two essential flaws—a critical dependency on an unpublished companion paper and the inclusion of extensive internal version-history prose—as well as major issues with length and clarity. These must be addressed before the paper can be reconsidered.

---

### Detailed Findings

#### ESSENTIAL

**P5-E1: Critical Dependency on Unpublished Work (Paper IV)**
*   **Section/Page:** Abstract (p. 1), Section II (p. 3), and throughout.
*   **Problem:** The entire analysis is predicated on the chirality catalog and key results (specifically, the classifier-monopole systematic) from "Paper IV [3] (companion work, not yet peer-reviewed)". A core principle of peer-reviewed literature is that a manuscript must be self-contained and its foundations verifiable. Basing a paper's primary data input and the interpretation of its main result on a work that is not available to the referees or the public is unacceptable. The claims of Paper IV are treated as established facts (e.g., "the known Paper IV catalog-wide classifier-monopole systematic," "Paper IV establishes the catalog-wide CW-fraction monopole as a classifier-residual bias"), but they cannot be verified.
*   **Required Fix:** The manuscript cannot be published until Paper IV is, at a minimum, publicly available on a preprint server like arXiv and preferably accepted for publication. All load-bearing claims from Paper IV must be summarized with sufficient detail (e.g., methods, sample size, key statistical results) within this manuscript for the argument to be self-contained. The current presentation outsources the validity of this paper's core premise.

**P5-E2: Pervasive Internal-History and Draft-Evolution Language**
*   **Section/Page:** Throughout the manuscript. This is a recurring issue that severely undermines the professionalism and finality of the work.
*   **Problem:** The text is littered with phrases that describe the evolution of the analysis, corrections of previous errors, and superseded results from "earlier drafts." This language is appropriate for an internal collaboration note or a lab notebook, but not for a formal scientific publication. It forces the reader to parse the history of the project rather than focusing on the final, definitive results, and it erodes confidence in the presented work by highlighting past mistakes and withdrawn claims.
*   **Examples (non-exhaustive):**
    *   p. 2: "The joint two-sample z-test on the bright-vs-dark fcw difference is |z| ≈ 2.10... the z is approximate (§VID)" followed by "An earlier draft quoted filament bright/dark n of 416,701/21,203 with a 3.4σ two-sample split; those values... are withdrawn" (p. 12).
    *   p. 3: "an earlier harmonic-space subsample-mask MASTER-deconvolved l = 1 statistic was withdrawn in Paper IV v1.0.166 after a provenance audit..."
    *   p. 13: "An earlier draft of this table reported... those values are withdrawn in favor of the declared-parent recompute below."
    *   p. 13: "An earlier draft quoted σ = 11.32... that population belonged to the withdrawn unfiltered nearest-label join..."
    *   p. 16: "An earlier draft reported n_void = 86,276 / 64,514... those values reproduce exactly only under a zone-indexing defect... The corrected per-cap join values above supersede them..."
    *   p. 20: "An earlier draft attributed the excess to a 'relaxed env-label confidence filter'; the join-multiplicity diagnosis above... replaces that description."
    *   p. 24: "An earlier draft quoted an overlap of 110,586; that join... is withdrawn."
    *   p. 27: "An earlier draft of this summary stated the bright/dark split agreed 'within ±0.001'; that statement was stale and is corrected here."
    *   p. 31: "...the superseded unfiltered-join version is retained alongside as prefilter_legacy."
*   **Required Fix:** **All** such language must be excised from the manuscript. The paper should present only the final, correct, and relevant analysis and results. The history of how the author arrived at these results is not relevant to the reader. The text must be rewritten to be a direct, authoritative statement of the work performed.

#### MAJOR

**P5-M1: Excessive Length and Lack of Focus**
*   **Section/Page:** Entire manuscript.
*   **Problem:** At 32 pages, the manuscript is excessively long for what is ultimately a null result. The core finding—that the DESIVAST-anchored void analysis shows no environmental dependence—is buried under a vast number of secondary, tertiary, and diagnostic cross-checks. While this diligence is commendable, it makes the paper difficult to read and obscures the primary contribution. The analysis path is convoluted, requiring an explicit "Analysis-tree declaration" (Table II) to navigate, which is a sign of overly complex presentation.
*   **Required Fix:** The manuscript requires significant restructuring and shortening. A recommended structure would be:
    1.  A concise main paper (suggested max ~12-15 pages) focusing on the primary result: the DESIVAST-anchored three-algorithm null test. This section should include the V-Web analysis as the main supporting cross-check.
    2.  Move the extensive secondary cross-validations (Tempel FoF, ASTRA EDR, detailed systematics splits, Phase 2 sweep details) and speculative discussions (Appendix A EFT toy model) to a comprehensive appendix or supplementary material. This would dramatically improve the readability and impact of the core result.

**P5-M2: Confusing "T-Web" vs. "V-Web" Nomenclature**
*   **Section/Page:** Title, Abstract, and throughout (e.g., footnote 'a' on p. 2).
*   **Problem:** The title refers to a "T-Web (Hahn 2007) Tidal-Tensor Cross-Check," but the body predominantly uses the term "V-Web." Footnote 'a' explains that the author uses the Hahn 2007 tidal-tensor recipe (often called T-Web) but retains the "V-Web" label for "backward compatibility with prior analyses." This is confusing for the reader. The V-Web of Hoffman et al. 2012 explicitly uses the velocity shear tensor, which is physically distinct from the tidal tensor from Poisson's equation. Using these terms interchangeably is imprecise and will cause confusion in the literature.
*   **Required Fix:** Standardize the nomenclature. Since the Hahn 2007 tidal-tensor method is used, the classifier should be consistently referred to as "T-Web" or "tidal-tensor classifier" throughout the manuscript. The "V-Web" label should be reserved for velocity-shear-based methods. The footnote should be rewritten to state this choice clearly, rather than justifying the use of an imprecise term.

#### MINOR

**P5-m1: Juxtaposition of Non-Comparable Statistics in Abstract**
*   **Section/Page:** Abstract, p. 1.
*   **Problem:** The abstract correctly states that "The quoted σ_from_half values scale as √n at fixed fractional offset and are therefore not mutually comparable across classes of different n." However, it then immediately presents a list of these non-comparable values: "-2.61σ (filament)... -4.66σ (cluster)... +0.55σ (wall)... -0.68σ (void)". While technically not a direct comparison, this presentation encourages the reader to make one.
*   **Required Fix:** Rephrase the abstract to avoid listing the raw σ values. Instead, summarize the finding qualitatively (e.g., "deviations in high-n classes are consistent with the catalog monopole, while low-n classes are dominated by counting noise") and refer to the body for the quantitative details.

**P5-m2: Speculative and Underdeveloped EFT Model**
*   **Section/Page:** Appendix A, p. 30.
*   **Problem:** Appendix A presents a "toy EFT mapping" that is explicitly acknowledged as schematic, not derived from foundational literature, and not a "derived constraint." While potentially interesting as a guide for future work, it adds length to an already long paper and is too speculative to be of significant value in its current form. It also contains caveats about rotational and gauge invariance that are not resolved.
*   **Required Fix:** This appendix should be significantly shortened or removed. If retained, it should be framed even more cautiously as a heuristic guide for theorists, but its inclusion in this observational paper is questionable.

#### NIT

**P5-N1: Typographical Error in Table VII**
*   **Section/Page:** Table VII, p. 15.
*   **Problem:** The first two rows of the table under the "Grid-unresolved" section are marked with a `†` symbol. However, there is no corresponding footnote `†` to explain its meaning.
*   **Required Fix:** Add the intended footnote or remove the `†` symbols.

---

### Summary recommendation

**MAJOR REVISIONS**

The manuscript presents a thorough and statistically robust null result that is a valuable contribution to the literature on cosmological parity violation. The author's diligence in performing a wide array of cross-checks is evident. However, the paper is not publishable in its current state. The essential requirement to remove all internal-facing "draft history" language and to resolve the critical dependency on the unpublished Paper IV must be met. Furthermore, a major restructuring is needed to shorten the paper and focus the main text on the primary result, moving extensive secondary analyses to an appendix. If the author can perform this comprehensive revision, the resulting manuscript would likely be suitable for publication.