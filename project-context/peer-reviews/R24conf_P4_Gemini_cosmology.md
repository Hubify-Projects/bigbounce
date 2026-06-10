# P4 R24conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v168.pdf` md5=90c4a8a3 pages=19
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 317.4s

---

## Referee Report on "Survey-Scale Galaxy Chirality with Equivariant TTA..."

**Manuscript ID:** [Assigned by Editor]
**Author:** Houston Golden
**Journal:** Physical Review D

This paper presents a search for a cosmological chirality dipole using a new, large catalog of 8.47 million galaxies from the DESI Legacy Surveys, of which 3.2 million are classified as spirals. The analysis employs a Vision Transformer with a novel bias-hardening technique called Test-Time Equivariant Averaging (TTA). The headline result is a null detection of a real-space chirality dipole, consistent with statistical isotropy. The paper's main contributions are (1) the creation and public release of the largest galaxy chirality catalog to date, (2) a robust null result for the chirality dipole at sub-percent sensitivity, and (3) a rigorous, multi-pronged methodology for identifying and mitigating observational and classifier-induced systematics.

The analysis is exceptionally thorough and transparent. The authors correctly identify the dipole as a parity-even, isotropy-breaking observable, distinct from a direct test of parity violation. The core of the paper is a masterclass in systematics control. The authors demonstrate that a small, uniform classifier bias (a monopole) couples with the non-uniform survey footprint to create a significant, but spurious, dipole-like signal in the spherical harmonic domain (the "monopole-mask leakage channel"). They quantify this effect with a generative null model that reproduces over 99% of the raw signal, thereby explaining it as a systematic artifact.

The primary cosmological estimators—a real-space dipole fit and a template-fit exclusion—are designed to be insensitive to this leakage channel and both yield null results. The headline real-space dipole significance is a statistically insignificant +0.41σ (p=0.31). The paper further provides a well-defined falsification criterion based on a detailed injection-recovery simulation, setting a 95% recovery threshold (A₉₅) for a dipole amplitude between 1.0% and 1.5%.

The transparency regarding the analysis pipeline, including the disclosure of corrected results from earlier versions and a withdrawn result traced to a software error, is commendable and builds significant confidence in the final conclusions. The public release of the catalog, model, and analysis code is a major contribution to the community and ensures the results are fully reproducible.

The paper is well-structured, the figures are clear and impactful (especially Fig. 7, which visually demonstrates the power of the TTA method), and the conclusions are strongly supported by the evidence presented. The work sets a new standard for rigor in this type of analysis. The following points should be addressed before publication.

---
### Findings

#### MAJOR

**P4-M1** | Section IV (multiple pages) | **Consolidation of `l=1` Estimators**
*   **Problem:** The paper analyzes several distinct `l=1` quantities: (1) the real-space dipole fit amplitude, (2) the pre-MASTER pseudo-Cₗ, (3) the post-MASTER pseudo-Cₗ on the canonical mask, and (4) the post-MASTER pseudo-Cₗ on the apodized footprint. The relationships between these quantities and their interpretation are critical to the paper's core argument but are spread across the main text, figure captions, and a crucial footnote (footnote 3 on p.17). This fragmentation makes it challenging for the reader to synthesize the full picture.
*   **Fix:** Add a small summary table or a dedicated paragraph in the main results section (e.g., at the end of Sec. IV.C or start of IV.D) that explicitly lists these different `l=1` observables. For each, it should state the measured value (e.g., +0.41σ, +6.48σ, +3.64σ, +7.28σ) and its final interpretation (e.g., "Primary cosmological constraint, null", "Systematic from monopole-mask leakage, pre-correction", "Systematic residual, post-correction", "Systematic diagnostic"). This would greatly improve the clarity and impact of the central argument.

**P4-M2** | Abstract & Section IV | **Reporting of Significance for Non-Gaussian Nulls**
*   **Problem:** The paper quotes significance values in units of "σ" (e.g., "+3.64σ moment-z") while also correctly noting that the underlying permutation nulls are heavy-tailed and non-Gaussian (e.g., Table III caption). For a non-Gaussian distribution, a "moment-z" value (data-mean)/std does not map to a p-value in the standard way, which can be misleading. The abstract mitigates this by also providing a "Gaussian-equivalent" sigma, but this practice is not used consistently throughout the text.
*   **Fix:** The authors should choose one of two options for consistency: (1) For every `z_mom` value quoted against a non-Gaussian null, also provide the empirical rank p-value (which is the more robust statistic, already computed) and the Gaussian-equivalent sigma. (2) Switch to primarily reporting the empirical rank p-value, which is unambiguous, and only mention the `z_mom` as a secondary descriptor. The current mix, where sometimes only `z_mom` is given, is potentially confusing.

#### MINOR

**P4-N1** | Page 6, Section C.a | **Informal Section Sub-heading**
*   **Problem:** The sub-heading "Confidence-threshold sensitivity disclosure:" reads like an internal note or a checklist item rather than formal scientific prose.
*   **Fix:** Rephrase to a more standard heading, such as "Sensitivity to Confidence Threshold" or "Dependence on Confidence Threshold".

**P4-N2** | Page 13, Appendix A, section d | **Informal Language in Provenance Note**
*   **Problem:** In the otherwise excellent provenance note, the phrase "produced by an uncommitted script" is slightly informal.
*   **Fix:** For improved formality, consider rephrasing to something like "produced by a script that was not part of the version-controlled analysis pipeline" or "an exploratory script not intended for production".

#### NIT

**P4-N3** | Page 1, Abstract | **Jargon "dispositioned"**
*   **Problem:** The word "dispositioned" is used twice in the abstract (e.g., "...sensitivity is dispositioned as a low-confidence-tail systematic..."). This is technical jargon and could be replaced with clearer language.
*   **Fix:** Suggest replacing "dispositioned as" with "identified as", "classified as", or "attributed to".

---
## Summary recommendation
**ACCEPT WITH MINOR CORRECTIONS**

This is an exemplary paper that makes a significant contribution to observational cosmology. The analysis is performed at an extremely high level of rigor, particularly with respect to systematics control and methodological transparency. The null result for the chirality dipole is robust and represents the most stringent constraint to date. The public data products and code are a valuable community resource. The paper is well-suited for publication in Physical Review D after the minor revisions listed above are addressed to further improve clarity.