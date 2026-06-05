# P4 2026-06-04_1733pt — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 75.2s

---

## Referee Report for Paper P4

**Paper:** Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.12σ Subsample-Mask ℓ=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)

**Round:** 2026-06-04_1733pt

### Summary of the Paper

This paper presents a detailed analysis of galaxy chirality using a new catalog of 3.2 million spiral galaxies derived from DESI Legacy Survey data. The primary scientific result is a null detection of a large-scale angular dipole (ℓ=1) in the galaxy chirality field, which constrains isotropy-breaking axial-vector modes. The authors employ a Vision Transformer (ViT) classifier with a Test-Time Averaging (TTA) procedure to ensure output-level equivariance and mitigate instrumental bias.

The analysis is carefully structured. The headline null result (−0.12σ) is derived on a "subsample mask" designed to be robust against edge effects, using the MASTER formalism to decouple spherical harmonic modes. The paper then presents a thorough investigation of a statistically significant residual (+3.64σ) found on a more fragmented "canonical mask". Through an exhaustive series of diagnostic tests—including a generative null, a multi-null battery, and direct cross-correlations with survey depth proxies—the authors convincingly argue that this residual is not a primordial cosmological signal but rather a systematic effect arising from the coupling of a small, uniform classifier monopole with the patchy survey geometry.

The paper correctly distinguishes between the parity-EVEN ℓ=1 dipole observable (an anisotropy test, which is the paper's main focus) and parity-ODD observables (like the ℓ=0 monopole). The authors provide a detailed discussion of the theoretical implications, appropriately scoping their result as a direct constraint on the late-universe morphology channel, and noting that constraints on primordial physics require model-dependent transfer functions which are not derived here. The work includes extensive systematic checks, a public data and model release, and a clear falsification criterion for the claimed null result.

### General Comments

This is an exceptionally thorough and methodologically rigorous paper. The scientific analysis is of a very high standard. The authors demonstrate a deep understanding of the potential systematic effects and have gone to great lengths to quantify and mitigate them. The clear separation between the primary cosmological result (the null dipole) and the diagnostic analysis of the systematic residual is exemplary. The use of a "declared analysis hierarchy" and numerous summary tables greatly aids in navigating the complex set of results. The theoretical discussion in Section VI.G is precise and correctly frames the result within the context of fundamental physics, properly distinguishing between tests of isotropy and parity.

The scientific content of the paper is strong and warrants publication. However, the presentation requires significant revision. The paper's length is excessive for the journal, and it contains numerous artifacts from the internal review and versioning process that must be removed. My recommendation is for major revisions, focused almost exclusively on restructuring for length and cleaning the manuscript for publication.

---

### Findings

#### ESSENTIAL

**P4-E1: Paper Length and Structure**
*   **Section/Page:** Entire manuscript
*   **Problem:** At 57 pages, the paper is excessively long for a standard Physical Review D article, even for a detailed methods/catalog paper. The core scientific contribution is the null dipole result and the demonstration of the monopole-mask leakage channel as a significant systematic. While the exhaustive diagnostic investigation of the +3.64σ canonical-mask residual is excellent scientific work, its detailed, sequential presentation in the main text obscures the primary results and makes the paper difficult to read.
*   **Fix:** The paper must be significantly restructured and shortened to a more appropriate length (e.g., 20-25 pages for the main text). I recommend the following structure:
    1.  **Main Text:** Focus on the primary narrative: Introduction, Data and Methods (summarizing the classifier, TTA, and MASTER formalism), Core Results (the headline null dipole result on the subsample mask; the demonstration of the monopole-mask leakage channel; a summary of the multi-null battery concluding the canonical-mask residual is systematic), Comparison with Previous Work, Discussion, and Conclusions.
    2.  **Appendices:** Move the highly detailed, sequential deep-dives into the systematics to appendices. This includes the full breakdown of the signal-hunt diagnostics (Sec. IV.E), the detailed `wcw(θ)` analysis (Sec. IV.F), the per-leg systematics (Sec. IV.I), the full sensitivity floor derivation (Sec. VI.C), and the detailed robustness checks (Sec. VI.F). These sections are valuable for experts and reproducibility but are not essential for the main logical flow of the paper.

**P4-E2: Removal of Internal Review and Versioning Artifacts**
*   **Section/Page:** Throughout
*   **Problem:** The manuscript contains numerous phrases, footnotes, and version tags that are artifacts of the internal development and review process. These are unprofessional and must be removed before publication.
*   **Fix:** Perform a thorough search and remove all such artifacts. Examples include:
    *   Page 1, Date line: `(Dated: June 4, 2026 PDT — v1.0.151)`
    *   Page 2, Footnote: `...under the immutable release tag paper4-v1.0.151.`
    *   Page 9, Table II, footnote c: `Retraction note: earlier drafts additionally reported... This auxiliary metric is retracted...`
    *   Page 11, text: `( scope restoration the mean-probability invariance...`
    *   Page 21, text: `The N=500 simulation result is materially different from the the N=25 smoke estimate and supersedes it.`
    *   Page 39, text: `prior text in this paragraph compared...`
    *   Page 47, text: `The earlier the earlier-draft auxiliary claim... is retracted here...`
    *   General phrasing like "This test was added after the an earlier external review..." (p. 7) or "This addresses the... question raised in earlier review..." (p. 24) should be rephrased neutrally (e.g., "To formalize the interpretation..." and "This analysis confirms...").

#### MAJOR

(No major scientific issues were found. The science is sound.)

#### MINOR

**P4-M1: Duplicate Phrasing**
*   **Section/Page:** Page 43, Section "Estimator hierarchy"
*   **Problem:** There is a duplicated phrase: "...closes the mask-definition mask-definition robustness question..."
*   **Fix:** Correct the sentence to read: "...closes the mask-definition robustness question..." Please check for other similar instances.

**P4-M2: Clarify Future Date**
*   **Section/Page:** Page 1, Date line
*   **Problem:** The date of the paper is listed as "June 4, 2026". While this may be an internal convention, it is confusing for a public preprint or journal submission.
*   **Fix:** Change the date to the actual date of submission.

#### NIT

**P4-N1: Jargon in Footnote**
*   **Section/Page:** Page 9, Table II, footnote b
*   **Problem:** The footnote contains the phrase `(∼ 2.5σ family-corrected)`. While the meaning is understandable to an expert, "family-corrected" is slightly jargony.
*   **Fix:** Consider rephrasing for clarity, e.g., `(∼ 2.5σ after accounting for look-elsewhere effects)`. This is a minor point as the main text handles this well.

---

## Summary recommendation

**MAJOR REVISIONS**

The scientific analysis presented in this paper is of the highest quality. It is rigorous, transparent, and exceptionally thorough. The authors have produced a compelling null result for the galaxy chirality dipole and have performed a masterclass in identifying and quantifying a subtle but important systematic effect. The theoretical framing is precise and correct. For these reasons, the paper is a significant contribution and is certainly worthy of publication in Physical Review D.

However, the current presentation is not acceptable. The paper's extreme length (57 pages) buries the key results in a deluge of diagnostic detail, making it inaccessible to a broad audience. Furthermore, the manuscript is littered with internal versioning tags and review artifacts that must be removed. The required revisions are therefore major, but they are focused entirely on restructuring the paper for clarity and length and on professionalizing the manuscript for publication. The underlying scientific content is sound and does not require major revision. Once the paper is restructured as a main article with supporting appendices and cleaned of internal artifacts, it will be an excellent and impactful publication.