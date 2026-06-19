# P5 D1 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` md5=401a73f9 pages=32
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 170.8s

---

**Referee Report on "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample"**

This manuscript presents a detailed and rigorous search for an environmental dependence of spiral galaxy chirality using data from the DESI Data Release 1. The authors cross-match a large, 8.5M-galaxy chirality catalog with DESI spectroscopic redshifts and perform a comprehensive analysis using multiple cosmic-web classification schemes (T-Web, DESIVAST, Tempel+ FoF, ASTRA) and numerous statistical tests. The primary finding is a null result: no statistically significant evidence for an environmental dependence of spiral handedness is found, once a previously identified catalog-wide systematic monopole is accounted for.

The analysis is exceptionally thorough, featuring an impressive suite of robustness checks, including sensitivity sweeps of analysis hyperparameters, cross-validation against independent classifiers, and stress tests against observational systematics like the survey selection function and redshift-space distortions. The authors are transparent about the analysis choices and limitations. The quality of the investigation and the strength of the presented evidence are high.

However, there are several issues that must be addressed before the manuscript can be considered for publication in Physical Review D. The most critical of these is the reliance on an unpublished companion paper for the primary data inputs and systematic corrections.

**ESSENTIAL Revisions**

*   **P5-E1: Reliance on an unpublished companion paper (Paper IV).**
    *   **Section/Page:** Throughout, starting with Abstract (p. 1), Sec. I (p. 3), and Sec. II (p. 3).
    *   **Problem:** The manuscript's analysis is critically dependent on "Paper IV [3] (in preparation)". Specifically, the source chirality catalog itself and the crucial "-0.26 pp monopole offset" are taken from this unpublished work. A published paper must be self-contained and its results verifiable from the cited literature. Relying on an "in preparation" manuscript for the foundational data and a key systematic correction is unacceptable for a journal of PRD's standard.
    *   **Fix:** The manuscript must be made self-contained. The authors must either:
        1.  Wait for Paper IV to be accepted and published (or at least available on arXiv) and update the citation accordingly.
        2.  Incorporate the essential methodological details of the chirality classification and the derivation of the monopole systematic from Paper IV into the present manuscript, for example, in an appendix. This appendix must be sufficiently detailed for a reader to understand how the inputs to the current analysis were generated and validated.

**MAJOR Revisions**

*   **P5-M1: Use of internal version-history and audit-trail language.**
    *   **Section/Page:** Sec. II (p. 3).
    *   **Problem:** The text contains distracting and inappropriate details about the internal version history of a companion paper. The sentence, "an earlier harmonic-space subsample-mask MASTER-deconvolved l = 1 statistic was withdrawn in Paper IV v1.0.166 after a provenance audit traced its mask to a synthetic footprint," is an example of internal bookkeeping that does not belong in a formal publication. It confuses the reader and undermines the authority of the final, presented result.
    *   **Fix:** Remove all such language regarding withdrawn statistics, version numbers, and internal audits of companion papers. The manuscript should simply state and use the final, stable results from its sources.

*   **P5-M2: Statistical test on non-disjoint samples.**
    *   **Section/Page:** Sec. VI.D (p. 12, "Filament-class within-class decomposition").
    *   **Problem:** The manuscript reports a `|z| ≈ 2.1` two-sample test result for the bright-vs-dark filament subsamples. However, it is stated that the test is computed at the "row level" where "the bright and dark splits are not disjoint in unique TARGETIDS." A standard two-sample z-test requires independent samples. Applying it to overlapping samples invalidates the calculation of the standard error and thus the z-score and p-value. While the author commendably flags this as a caveat, presenting a flawed statistic for one of the most notable "residual structures" in the paper is a significant weakness.
    *   **Fix:** The per-class bright-vs-dark analysis must be re-performed on a sample of unique, disjoint galaxies. If this is not possible due to sample size, the current flawed result should be removed and replaced with a more qualitative statement, or at a minimum, be much more strongly caveated and demoted from its current prominence.

*   **P5-M3: Abstract clarity and accessibility.**
    *   **Section/Page:** Abstract (p. 1).
    *   **Problem:** The abstract is exceptionally dense, technical, and laden with jargon and specific numerical results that are difficult to parse without having read the entire paper. While precision is important, the primary goal of an abstract is to be a clear, accessible summary of the work's motivation, main result, and significance. The current version is closer to a technical summary for experts who are already familiar with the project.
    *   **Fix:** Rewrite the abstract to improve clarity and flow. Start with a broader statement of the physical question being addressed. Focus on the main conclusion (a robust null result) and its implications. Defer the bulk of the specific sample sizes, p-values, and sigma-values for individual sub-tests to the main text, retaining only the most critical top-level numbers that establish the result's significance (e.g., the final DESIVAST contrast and the overall constraint).

**MINOR Revisions**

*   **P5-m1: Unusual "Robustness" section.**
    *   **Section/Page:** p. 2.
    *   **Problem:** The "Robustness" section at the beginning of the paper acts as a second, more detailed abstract. This is an unconventional structure and makes the introduction to the paper feel repetitive.
    *   **Fix:** Consider restructuring this section. The information is valuable, but it could be more effectively integrated into the main results sections (e.g., Sec. VIII, IX) or summarized more briefly in the main conclusion (Sec. XV).

*   **P5-m2: Typo/clarification in tidal tensor definition.**
    *   **Section/Page:** Sec. IV.A, Step 9 (p. 5).
    *   **Problem:** The text describing the tidal tensor calculation contains a minor typo: "Tidal tensor: Tij(k) = -kikj(k)". This should likely be `Tij(k) = -kikj Φ(k)`. The subsequent sentence correctly derives the final expression, but the initial statement is confusing.
    *   **Fix:** Correct the typo to `Tij(k) = -kikj Φ(k)` for clarity.

**NIT (Cosmetic)**

*   **P5-N1: Manuscript Title.**
    *   **Section/Page:** Title (p. 1).
    *   **Problem:** The title is excessively long and descriptive.
    *   **Fix:** Consider shortening the title. For example: "Environmental Dependence of Spiral Chirality: A Null Result from DESI DR1 using Voids and the Cosmic Web".

## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, comprehensive, and statistically rigorous paper that presents a significant null result on the environmental dependence of galaxy chirality. The level of detail, transparency, and the sheer number of robustness checks are exemplary. The work provides a strong constraint for any cosmological model that predicts such a dependence.

However, the manuscript cannot be published in its current form due to its critical reliance on an "in preparation" companion paper (Paper IV) for its fundamental data and systematic corrections. This is an essential flaw that violates the requirement for a paper to be self-contained and its results reproducible from the available literature. Once this and the other major points listed above are thoroughly addressed, the manuscript will be a very strong candidate for publication in Physical Review D.