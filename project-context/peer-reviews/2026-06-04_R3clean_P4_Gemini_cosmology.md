# P4 2026-06-04_R3clean — Physical Review D cosmology-physics referee

**Model**: `gemini-2.5-pro`
**Input format**:  [NATIVE PDF — Gemini sees rendered document]
**Wall time**: 59.0s

---

**Referee Report on Paper P4**

**Report Date:** June 4, 2024

This paper presents a detailed analysis of galaxy chirality using a large dataset of 3.2 million spiral galaxies from the DESI Legacy Surveys. The authors develop a pipeline using a Vision Transformer (ViT) classifier and apply a Test-Time Averaging (TTA) procedure to enforce flip-equivariance, a crucial step for mitigating systematic biases. The primary scientific result is a null detection of a chirality dipole (an ℓ=1 axial-vector mode), which constrains isotropy-breaking effects in the late universe. The paper also provides a quantitative model for how a classifier monopole can leak into a spurious dipole signal through non-uniform survey geometry and demonstrates that a residual signal on a specific survey footprint is consistent with a depth/morphology-correlated systematic, not a primordial cosmological signal.

The analysis is exceptionally thorough, and the authors are careful to distinguish between different types of observables and systematic effects. The correct identification of the dipole as a parity-even, isotropy-breaking observable (as opposed to a direct parity-violation test) and the monopole as the parity-odd observable is a significant strength and a point of clarity often missing in the literature. The multi-stage null-testing and systematics-characterization framework is rigorous.

However, the paper in its current form is not suitable for publication. It is excessively long and structured more like an internal technical report than a scientific paper for a peer-reviewed journal. The core scientific narrative is obscured by an overwhelming amount of detail, internal-facing language, and a lack of clear separation between the main results and supporting diagnostics. The work is scientifically sound and important, but it requires substantial restructuring to be accessible and meet the standards of the journal.

## Summary of Findings

### ESSENTIAL

**P4-E1: Paper Length and Structure (Throughout)**
*   **Problem:** At 56 pages, the paper is far too long for a methods/catalog paper in PRD. The main scientific results are buried in a vast amount of supporting detail, making the paper difficult to read and its core contributions hard to discern. The narrative flow is frequently interrupted by deep dives into pipeline specifics, alternative null tests, and justifications that belong in an appendix.
*   **Fix:** The paper must be substantially restructured and shortened. I recommend a target length of 15-20 pages for the main text. The main text should contain: Abstract, Introduction, a concise summary of Data and Methods, the main Results (the null dipole and the interpretation of the canonical-mask residual), a focused Discussion of the implications (including the theoretical context from Sec. VI G), and Conclusions. All other material—including the detailed bias hardening suite, extended multi-null battery tests, specific NaMaster configurations, detailed injection recovery sweeps, and long tables of per-bin results—should be moved to appendices.

**P4-E2: Unprofessional Language and Internal Artifacts (Throughout)**
*   **Problem:** The paper is replete with language and artifacts that are inappropriate for a formal publication. This includes references to the manuscript's own version history, justifications framed as responses to prior reviews, and explicit paths to internal code and data artifacts. This undermines the paper's authority and professionalism.
    *   Examples:
        *   (Abstract, p. 1) "The catalog (3.2 M spirals), model weights..., and all reproducibility scripts are publicly released under the immutable release tag paper4-v1.0.153."
        *   (Methods, p. 6) "...the hierarchy below was fixed at v1.0.76 of this manuscript (after the first round of catalogue results)..."
        *   (Discussion, p. 35) "(Earlier drafts also cited a ∆ = −1.35% argmax CW-fraction shift... This manuscript retracts this as fragile-argmax sample noise...)"
        *   (Throughout) Frequent references to specific `.json` files in the main prose.
*   **Fix:** All such internal-facing language, version tags, commit hashes, file paths, and narrative about the paper's own evolution must be removed from the manuscript. References to data and code should be consolidated in a "Data Availability" section and cited appropriately. The paper should be presented as a finished scientific work, not a log of its own development.

### MAJOR

**P4-M1: Narrative Clarity (Throughout)**
*   **Problem:** While the underlying analysis is logical, the presentation of the argument is convoluted. The reader has to piece together the main thread from many different sections, tables, and long footnotes. The distinction and relationship between the three key numbers in the abstract (`-0.12σ`, `+0.43σ`, `+3.64σ`) are complex, and the paper takes too long to build the case for why one is the headline null and the other is a diagnostic systematic.
*   **Fix:** As part of the restructuring (P4-E1), the main text should be rewritten to present a clear, linear narrative. For example: 1) State the scientific goal (measure the chirality dipole). 2) Show the raw data is contaminated by systematics (the raw dipole). 3) Explain the methods used to correct for systematics (TTA and MASTER). 4) Present the corrected, null result (the `-0.12σ` and `+0.43σ` nulls). 5) Transparently report the remaining diagnostic residual (`+3.64σ`) and present the evidence that it is also a systematic, not a cosmological signal. This logical flow should be the backbone of the main text.

### MINOR

**P4-m1: Future Date (Title Block, p. 1)**
*   **Problem:** The paper is dated "June 4, 2026".
*   **Fix:** Change the date to the current submission date.

**P4-m2: Overly Long Footnotes (e.g., Table II, p. 9)**
*   **Problem:** Several footnotes are extremely long and contain essential details about the analysis that are difficult to parse in that format. For example, footnote 'b' on Table II (p. 9) is a dense paragraph detailing multiple follow-up calculations and referencing other artifacts. This information is crucial for understanding the post-MASTER results.
*   **Fix:** Integrate the essential content of long footnotes into the main text or move it to an appendix. Footnotes should be reserved for brief, ancillary comments.

**P4-m3: Duplicate Phrasing (Sec. VI F, p. 42)**
*   **Problem:** A duplicate phrase appears in the text: "this closes the mask-definition mask-definition robustness question".
*   **Fix:** Correct the sentence to read: "this closes the mask-definition robustness question". Check for other similar typographical errors.

### NIT

**P4-N1: Abstract Readability (Abstract, p. 1)**
*   **Problem:** The abstract is very dense and packed with numerical results and technical terms. While accurate, it may be difficult for a non-specialist to quickly grasp the paper's main takeaway.
*   **Fix:** Consider slightly simplifying the language in the abstract to emphasize the main finding more directly: a null result for the cosmological dipole, achieved after rigorously identifying and removing multiple layers of systematic contamination. The specific σ-values are important but could be presented in a slightly more streamlined way.

## Summary recommendation

**MAJOR REVISIONS**

This paper represents a significant and rigorous contribution to the search for cosmological anisotropies through galaxy morphology. The analysis is of high quality, and the theoretical framing is sound. The primary result—a null detection of the chirality dipole—is well-supported and an important benchmark for the field. However, the paper is not publishable in its current state due to severe issues with its length, structure, and tone. It reads like a technical note for internal review rather than a polished scientific article. The authors must undertake a major restructuring to separate the core results from the extensive supporting material and must remove all internal-facing commentary and artifacts. If these extensive presentational issues are addressed, the paper will be a valuable and impactful publication.