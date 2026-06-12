# P3 R34conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.97.pdf` md5=4de854dd pages=28
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 169.5s

---

## Referee Report: Spectrally Unusual Sources at Scale...

This paper presents a large-scale anomaly detection campaign across seven major astronomical surveys, resulting in a catalog of over 378,000 unique anomalies. The authors apply an autoencoder framework (BIGAE) to a combined dataset of 37.3 million sources, perform extensive cross-validation and methodological checks, and explore cosmological applications using the resulting catalog, including constraints on primordial non-Gaussianity (fNL) and consistency checks with NANOGrav results.

The scale of the analysis is impressive, and the paper's commitment to transparency regarding methodological failures (e.g., the LAMOST training bias, the ACT cross-transfer failure, the eROSITA score-axis irreproducibility) is commendable. The detailed self-correction and careful qualification of results, such as the distinction between SIMBAD-unmatched fractions and genuine novelty, and the proper handling of the noisy fNL bias measurement, meet the high standards of rigor expected for Physical Review D.

However, the manuscript in its current form contains several issues that must be addressed before it can be considered for publication. These range from placeholder values and internal development artifacts that are unacceptable in a final publication, to issues of clarity that hinder readability and reproducibility. The core scientific analysis appears sound, but the presentation requires significant revision.

### ESSENTIAL Revisions

These issues must be resolved for the paper to be publishable.

**P3-E1: Placeholder Date**
-   **Section/Page:** Abstract, p. 1
-   **Problem:** The paper is dated "(Dated: June 2026)". This is a placeholder and is unprofessional.
-   **Fix:** Replace with the correct submission date.

**P3-E2: Internal File Paths**
-   **Section/Page:** Multiple instances.
    -   p. 3, §II B α: "pipelines/p3\_anomaly\_engine/recovered\_pod\_scripts/"
    -   p. 6, §III A: "pipelines/p3\_anomaly\_engine/ext3\_b2\_targettype\_recount.json"
    -   p. 11, §III E: "pipelines/p3\_anomaly\_engine/r24conf\_erosita\_axis\_sweep.json"
    -   p. 12, §IV A: "pipelines/p3\_anomaly\_engine/ext3\_fm2\_planck\_top200\_train\_overlap.json"
    -   p. 13, §IV A/B: "pipelines/p3\_anomaly\_engine/pathc\_dedup/r23conf\_dedup\_audits.json"
    -   p. 15, §IV C: "pipelines/p3\_anomaly\_engine/pathc\_dedup/r23conf\_dedup\_audits.json" (duplicate)
    -   p. 22, Appendix A: "pipelines/p3\_anomaly\_engine/DATA\_RELEASE\_MANIFEST.md"
-   **Problem:** These are internal, non-resolvable file paths from the authors' development environment. They are not valid for a public release and break reproducibility.
-   **Fix:** Replace all such paths with proper, persistent URLs to the specific files or code snippets in the public data repository (e.g., GitHub, Zenodo). The Data Availability section should point to the root of the repository, and these in-text links should point to the specific artifacts.

**P3-E3: Version History Language in Final Text**
-   **Section/Page:** Multiple instances.
    -   p. 1, Abstract: "an earlier draft quoted 264,938/264,738 from headline-minus-LAMOST subtraction arithmetic"
    -   p. 6, Fig. 2 Caption: "Cross-transfer baseline... (superseded by the Path-C native catalog)"
    -   p. 13, §IV B: "An earlier draft quoted 38,330 pixels with χ² = 3.76; that artifact's pixel-selection and variance model could not be recovered from the committed analysis tree, and the figure is withdrawn in favor of the reproducible recompute above."
-   **Problem:** Language referring to "earlier drafts," "superseded" results, or "withdrawn" figures is inappropriate for an archival publication. The paper should present the final, definitive analysis, not a log of its own development.
-   **Fix:** Remove all such phrases. The text should be rewritten to present the final state of the analysis directly. For example, instead of saying a figure was withdrawn, simply do not include it. Instead of mentioning what an earlier draft quoted, state the final, correct numbers and methodology.

### MAJOR Revisions

These issues represent significant flaws in the current manuscript that require substantial changes.

**P3-M1: Undefined Core Acronym**
-   **Section/Page:** Abstract (p. 1), Method (p. 2)
-   **Problem:** The core autoencoder framework, "BIGAE," is used throughout the paper, starting in the abstract, but is never defined.
-   **Fix:** Provide the full name for the BIGAE acronym upon its first use.

**P3-M2: Placeholder in Key Computational Table**
-   **Section/Page:** Table VI, p. 23
-   **Problem:** In the "Train time (s)" column for "Planck CMB", the value is `_t`. The corresponding footnote explains that the wall-clock time was not preserved in the run logs. While the transparency is appreciated, a placeholder in a summary table of the final paper is not acceptable. This is the primary native model for the Planck analysis.
-   **Fix:** Either re-run the training to get a reproducible time or, if that is impossible, replace the placeholder with "N/A" or similar and ensure the footnote clearly states why the value is unavailable. The text should also acknowledge this missing provenance information.

**P3-M3: Overly Complex and Confusing Figure Caption**
-   **Section/Page:** Figure 2 Caption, p. 6
-   **Problem:** The caption for Figure 2 is excessively long and convoluted. It attempts to explain the complex relationship between the (superseded) cross-transfer baseline counts, the final Path-C counts, and the deduplication logic. This level of detail makes the caption nearly unreadable and buries the essential information about what the figure actually shows.
-   **Fix:** Drastically simplify the caption to describe only what is plotted in the figure (the spatial distribution of the *initial cross-transfer baseline*). Move the detailed discussion of count reconciliation and the relationship to the final Path-C catalog into the main body text of §III or §IV C, where it can be explained more clearly.

### MINOR Revisions

These issues should be addressed to improve the quality and clarity of the paper.

**P3-m1: Inconsistent Significance Level for `ajk`**
-   **Section/Page:** Abstract (p. 1) vs. Body (§V a, p. 16) vs. Conclusion (p. 21)
-   **Problem:** The significance of the empirical bias measurement `ajk = 0.19 ± 0.65` is described inconsistently.
    -   Abstract: `(<1σ from null)`
    -   Body (§V a): `consistent with zero at 0.29σ`
    -   Conclusion (Item 5): `(< 1σ from null)`
-   **Fix:** Use the most precise value (`0.29σ`) consistently in all three locations.

**P3-m2: Imprecise Mathematical Notation**
-   **Section/Page:** Equation (1), p. 3
-   **Problem:** The MSE equation is `MSE(x) = (1/N) * Σ(x - x_hat)^2`. The summation index `i` is missing from the terms inside the sum, i.e., `(x_i - x_hat_i)^2`.
-   **Fix:** Correct the equation to `MSE(x) = (1/N) * Σ_i (x_i - x_hat_i)^2`.

**P3-m3: Ambiguous Chi-squared Notation**
-   **Section/Page:** §IV B, p. 13
-   **Problem:** The text states "x² = 15.7". This is the reduced chi-squared (χ²/dof), not the total chi-squared (which is 376,713).
-   **Fix:** Use standard notation: `χ²/dof = 15.7` or `χ²_red = 15.7`.

**P3-m4: Unnecessary Internal Bookkeeping in Main Text**
-   **Section/Page:** §IV C, p. 15
-   **Problem:** The subsections "Friends-of-friends chain audit" and "Cluster-accounting reconciliation" are extremely detailed audits of the deduplication algorithm. While this information is valuable for deep reproducibility, it significantly disrupts the flow of the main cross-survey analysis.
-   **Fix:** Consider moving these two detailed subsections to an appendix. The main text can then summarize the outcome: that the FoF algorithm is behaving as expected without transitive chain bridging issues and that the cluster counts are internally consistent.

**P3-m5: Inconsistent Citation for Liang et al. Benchmark**
-   **Section/Page:** Abstract (p. 1) vs. Body (§III A, p. 5)
-   **Problem:** The abstract cites `[11]` as the "largest published single-survey anomaly catalog" which is used as the size benchmark throughout. However, §III A introduces a second paper by Nicolaou et al. `[12]` which is also a DESI anomaly search. The relationship and choice of benchmark are not immediately clear.
-   **Fix:** Briefly clarify in the introduction or abstract why Liang et al. `[11]` is chosen as the primary benchmark over other similar works.

### NIT (Cosmetic)

**P3-N1: Non-institutional Email Address**
-   **Section/Page:** p. 2
-   **Problem:** The corresponding author's email is `houston@hubify.com`, which appears to be a commercial/personal address rather than a standard academic or research institution address.
-   **Fix:** This is at the author's discretion, but using an institutional or dedicated research project email is standard practice for PRD.

**P3-N2: Unnecessary Implementation Jargon**
-   **Section/Page:** §II C, p. 4
-   **Problem:** The phrase "staging from HuggingFace to local-pod NVMe" is overly specific implementation jargon that adds little value for the reader.
-   **Fix:** Simplify to "dominated by FITS-file I/O" or similar.

## Summary recommendation
**MAJOR REVISIONS**

This paper presents a work of significant scope and value to the community. The authors have performed a massive analysis and have been laudably transparent about the complexities and limitations of their methods. The cosmological applications, while preliminary, are well-motivated and carefully executed.

However, the manuscript is marred by the inclusion of numerous artifacts from the development process, including placeholder values, internal file paths, and version-history-style comments. These are not acceptable for a final publication in a journal of PRD's stature. Additionally, several key points are obscured by overly dense captions or a lack of clear definitions.

The scientific content is strong, and the paper is on a clear path to acceptance. But it requires a thorough cleaning and polishing pass to bring the presentation up to the quality of the analysis itself. I recommend the paper for publication after these major revisions are addressed.