# P5 R53 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/private/tmp/R53_P5/p5_desi_chirality.pdf` md5=e294df9b pages=33
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 203.3s

---

## Referee Report: P5

**Report on "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample"**

This manuscript presents a detailed and rigorous search for an environmental dependence of spiral galaxy chirality using data from the DESI Data Release 1. The authors cross-match a large chirality catalog with DESI spectroscopic data, classify galaxies into cosmic-web environments using the T-Web tidal-tensor method and the DESIVAST void catalog, and perform a comprehensive suite of statistical tests. The headline conclusion is a null result: no evidence for environment-dependent chirality is found beyond a previously identified, catalog-wide systematic monopole offset. The analysis is exceptionally thorough, featuring numerous cross-checks, sensitivity analyses, and a commendable level of transparency regarding methodology and potential systematics.

Despite the high quality of the analysis, there are several issues that must be addressed before the paper can be considered for publication in Physical Review D. The most critical of these is the paper's foundational reliance on an unpublished companion paper.

### ESSENTIAL Revisions

**P5-E1: Foundational reliance on unpublished work (Paper IV)**
*   **Section/Page:** Throughout, e.g., Abstract (p. 1), Sec. I (p. 3), Sec. II (p. 3).
*   **Problem:** The entire analysis is predicated on data products from a companion paper, "Paper IV [3]", which is cited as "in preparation". Specifically, the per-galaxy chirality labels ({CW, CCW}) and the crucial catalog-wide monopole offset (Δf_cw = -0.0026) are imported from this unpublished work. The abstract states, "We cross-match the 8,474,531-galaxy chirality catalog of Paper IV [3] (in preparation...)", and Section II states, "Paper IV provides the per-galaxy CW/CCW labels we test here; we make no independent classification." A manuscript submitted to PRD must be self-contained and its results verifiable. Basing a primary analysis on a non-public, non-peer-reviewed catalog and its derived systematics is not acceptable.
*   **Fix:** The manuscript must be made self-contained. The author must either:
    1.  Integrate the essential methodology for generating the chirality labels and deriving the catalog-wide monopole offset into the present manuscript. This could be done in a dedicated methods section or an appendix. The description must be sufficient for the reader to understand how the labels were produced and how the systematic offset was quantified.
    2.  Alternatively, the author should wait to submit this manuscript until Paper IV is publicly available (e.g., on arXiv) and can be cited with a stable reference. The current "in preparation" status makes the foundation of this work unverifiable.

### MAJOR Revisions

**P5-M1: Paper structure and readability**
*   **Section/Page:** Abstract and "Robustness" section (pp. 1-2).
*   **Problem:** The abstract is followed by a "Robustness" section that functions as a second, even more detailed abstract. Together, they form a nearly two-page executive summary that is exceptionally dense with numerical results. This "firehose" of information at the beginning of the paper hinders readability and makes it difficult for the reader to grasp the main narrative thread before being overwhelmed with the details of every cross-check.
*   **Fix:** The paper's structure should be revised. The abstract should be a concise summary of the primary motivation, method, and result, as is standard. The content of the "Robustness" section on page 2 should be integrated into the main results sections (e.g., Sec. VI, Sec. VIII) where these robustness checks are discussed in full detail. This will improve the narrative flow and present the results in a more logical, less overwhelming sequence.

**P5-M2: Clarification of the bright/dark tracer systematic**
*   **Section/Page:** Sec. VI.D.b (p. 11), Sec. VI.D.c (p. 12).
*   **Problem:** The paper finds a significant systematic tied to the DESI target program, where the "bright" (BGS) and "dark" (LRG/ELG/QSO) samples show chirality deviations of opposite sign (e.g., filament class bright σ = -2.98 vs. dark σ = +1.61, a |z| ≈ 2.1 difference). The author argues this is likely due to BGS-selection-function-conditioned systematics. While this is a plausible and well-argued interpretation, the non-orthogonality of T-Web class and target program (Sec. VI.D.d) means a residual astrophysical signal cannot be definitively ruled out with the current analysis. The text correctly states it is a "residual structure that the current data do not allow us to cleanly partition".
*   **Fix:** While the primary DESIVAST analysis is shown to be robust to this issue, the discussion surrounding this systematic in the context of the T-Web analysis should be sharpened. The author should explicitly state that while a selection-effect origin is strongly favored, this ~2σ tension remains the most significant residual in the analysis and warrants specific follow-up in future work with larger "dark" samples. This would add valuable context and direction for future research.

### MINOR Revisions

**P5-N1: Inconsistent sample sizes in abstract**
*   **Section/Page:** Abstract (p. 1).
*   **Problem:** The abstract mentions two parent populations. The second is "(2) T-Web secondary: 783,820 unique chirality-relevant matched spirals with an environment row... carried on 812,793 environment-labeled survey-program coadd rows." A few lines later, the monopole is quoted for "n = 812,793 env-labeled rows". The per-class fractions are also given for this parent. However, the homogeneity test is later quoted for both the 812,793-row parent and the 783,820 unique-spiral subset. This is confusing for the reader.
*   **Fix:** For clarity, the abstract should consistently refer to one primary parent sample for the T-Web analysis (presumably the 812,793-row parent, as this is used for the main results) and briefly note that the conclusions are robust to using the unique-spiral subset.

**P5-N2: Toy EFT model framing**
*   **Section/Page:** Appendix A (p. 30).
*   **Problem:** The toy EFT mapping is a nice addition for connecting the observational null result to theory. However, the operator form `L_parity ~ g_phi (grad(phi)) (grad^2(rho)/rho_bg) (L . z_hat)` is highly specific. While the author provides excellent caveats about it being a toy model and not gauge-invariant, its specificity might be misinterpreted.
*   **Fix:** The author could slightly rephrase the introduction to this appendix to emphasize even more strongly that this operator is illustrative of the *type* of coupling being constrained, rather than a specific, well-motivated theoretical target. For instance, stating "We construct a schematic operator to illustrate how an observational bound on Δf_cw could translate to a bound on a parity-violating coupling..."

### NITs (Typos/Cosmetic)

**P5-T1: Dating of manuscript**
*   **Section/Page:** p. 1.
*   **Problem:** The date is given as "(Dated: June 18, 2026)". This is presumably a typo.
*   **Fix:** Correct the year to the current year of submission.

## Summary recommendation

**MAJOR REVISIONS**

This is a work of impressive rigor and transparency that presents a powerful null result on the environmental dependence of spiral chirality. The depth of the statistical analysis, the number of cross-checks performed, and the model of reproducibility are all exemplary. However, the paper in its current form cannot be accepted due to its foundational reliance on an unpublished and inaccessible companion paper (Paper IV) for its primary data (chirality labels) and key systematic calibration (the global monopole). This is an essential flaw that undermines the verifiability of the entire work.

Once the author has made the work self-contained by either incorporating the necessary methods from Paper IV or waiting for Paper IV to become publicly available, the manuscript will be a strong candidate for publication. The other requested revisions are aimed at improving the structure, readability, and clarity of the already excellent analysis.