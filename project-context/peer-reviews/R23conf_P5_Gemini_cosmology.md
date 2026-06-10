# P5 R23conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.52.pdf` md5=cc7c3390 pages=24
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 149.5s

---

## Referee Report on "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across 791,635 DR1 Matched Spirals"

This manuscript presents a detailed and multi-faceted search for an environmental dependence of spiral galaxy chirality using data from the DESI Data Release 1. The authors cross-match a large catalog of spiral galaxies with classified handedness against several environmental classifiers, including a tidal-tensor (V-Web) method run on the full DESI spectroscopic sample and, most importantly, the publicly released DESIVAST void catalog. The primary finding is a null result: the fraction of clockwise (CW) spirals does not show any statistically significant variation across different cosmic-web environments (voids, walls, filaments, clusters) beyond a small, previously reported global monopole offset in the chirality catalog itself. The analysis is exceptionally thorough, including numerous robustness checks, sensitivity analyses, and cross-validations against independent methods and datasets.

The work is of high quality and the level of rigor is commendable. The authors are transparent about their methodology, limitations, and the post-hoc designation of their primary analysis path. The conclusion—a strong null result that places observational bounds on certain classes of parity-violating cosmological models—is well-supported by the extensive evidence presented.

However, the manuscript requires significant revisions before it can be considered for publication in Physical Review D. The primary issues are the inclusion of extensive "draft history" prose, which is inappropriate for a formal publication, and the paper's length and structure, which could be improved to better highlight the main results.

### ESSENTIAL Revisions

**P5-E1: Removal of internal draft history and "withdrawn" results.**
*   **Location:** Throughout the manuscript, particularly Sections VI, VII, VIII, IX, XI, and Appendix B.
*   **Problem:** The paper is replete with phrases like "An earlier draft quoted...", "those values were computed on an unfiltered... and are withdrawn", "that statement was stale and is corrected here", and "replaces that description". This narrative of the paper's own revision history is unprofessional and confusing. A scientific paper should present the final, correct analysis and results, not a log of its own development. This must be removed in its entirety.
*   **Required Fix:** The authors must rewrite all sections to remove any mention of previous, incorrect, or superseded analyses from earlier drafts. The paper should be a clean presentation of the final, validated results. Below is a non-exhaustive list of instances that must be removed/rewritten:
    *   p. 9, §VI C: "An earlier draft quoted filament bright/dark n... those values were computed on an unfiltered nearest-label join... and are withdrawn..."
    *   p. 10, §VII: "An earlier draft of this table reported per-cell ranges... those values are withdrawn..."
    *   p. 10, §VII: "An earlier draft quoted |σ| = 11.32... that population belonged to the withdrawn unfiltered nearest-label join..."
    *   p. 15, §VIII F: "An earlier draft attributed the excess to a 'relaxed env-label confidence filter'; the join-multiplicity diagnosis above... replaces that description."
    *   p. 17, §IX B: "An earlier draft quoted an overlap of 110,586; that join omitted the matched-primary deduplication filter and is withdrawn..."
    *   p. 18, §IX C: "An earlier draft compared the Tempel overlap against the V-Web classes of the full matched sample... that comparison... is withdrawn."
    *   p. 20, §XI: "An earlier draft of this summary stated the bright/dark split agreed 'within ±0.001'; that statement was stale and is corrected here..."
    *   p. 23, Appendix B: "...the superseded unfiltered-join version is retained alongside as prefilter_legacy."

### MAJOR Revisions

**P5-M1: Paper length and structure.**
*   **Location:** Overall structure, primarily Sections IX and X.
*   **Problem:** At 24 pages, the paper is overly long for what is ultimately a (very robust) null result. The main text contains a large number of secondary and tertiary cross-checks that, while demonstrating the thoroughness of the work, dilute the impact of the primary analysis and make the paper difficult to navigate. The most powerful and novel result is the DESIVAST-anchored analysis in Section VIII.
*   **Required Fix:** I strongly recommend restructuring the paper to improve focus and readability. The main text should present the primary analysis paths: the headline V-Web result (Section VI), the crucial V-Web robustness and sensitivity checks (Section VII, and the z-shell correction from IX.A), and the primary DESIVAST-anchored result (Section VIII). The other valuable but secondary cross-validations should be moved to an appendix. This would include:
    *   The Tempel+2014 FoF cross-validation (Section IX.B).
    *   The concurrent-literature DR1/EDR cross-validation (Section IX.C).
    *   The ASTRA EDR per-object cross-validation (Section X).
    This restructuring would likely shorten the main body of the paper by 3-4 pages, creating a more focused and impactful article while preserving the full scope of the authors' commendable validation work in an appendix.

### MINOR Revisions

**P5-m1: Clarification of the σ statistic.**
*   **Location:** p. 4, Section V.
*   **Problem:** The primary statistic is named `σ_from_half` and the text describes it as "the signed deviation from 0.5 σ_from_half", which is circular and potentially confusing. The formula provided, `(ncw - 0.5N)/(0.5*sqrt(N))`, is a standard z-score for a binomial proportion test against the null hypothesis p=0.5.
*   **Required Fix:** Rephrase the description for clarity and consider renaming the statistic to simply `σ` or `z`. For example: "...we report the observed CW fraction... and the signed deviation from the parity-null hypothesis (p=0.5), σ, calculated as a standard z-score..." This would improve clarity without changing the substance of the calculation.

### NIT (Cosmetic)

**P5-N1: Title length.**
*   **Location:** p. 1, Title.
*   **Problem:** The title is exceptionally long and detailed. While accurate, it reads more like a summary from an abstract.
*   **Required Fix:** Consider a shorter, more concise title that captures the essence of the work. For example: "A Test of the Environmental Dependence of Spiral Galaxy Chirality in DESI Data Release 1" or "A Null Search for Environment-Dependent Spiral Chirality at V-Web Scales in DESI DR1". The extensive details are better placed in the abstract.

**P5-N2: Abstract footnote.**
*   **Location:** p. 1, Abstract, footnote 'a'.
*   **Problem:** The footnote correctly states that the raw σ values are not comparable across bins of different sizes. This is a critical point for the correct interpretation of the headline numbers.
*   **Required Fix:** While its placement in a footnote is acceptable, the authors might consider if this point can be integrated more directly into the abstract text to prevent any misinterpretation by a casual reader. This is a minor suggestion, as the authors handle this point rigorously in the main text.

## Summary recommendation
**MAJOR REVISIONS**

This manuscript represents a significant and high-quality body of work. The analysis is rigorous, comprehensive, and the conclusions are strongly supported. It has the potential to be a definitive statement on the environmental dependence of spiral chirality at the scales probed. However, the manuscript in its current form is not suitable for publication. The pervasive inclusion of internal draft history is a serious flaw that must be rectified. Furthermore, the paper would benefit significantly from restructuring to improve its focus and readability. Once these essential and major revisions are addressed, the paper should be an excellent candidate for publication in Physical Review D.