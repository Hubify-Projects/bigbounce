# P1B R37conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.65.pdf` md5=bac8d620 pages=20
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 157.1s

---

Referee Report for PRD Manuscript
======================================

**Manuscript ID:** [Assigned by user]
**Title:** Technical Verification Companion to the ECH Spin-Torsion Program: ACDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model
**Author(s):** Houston Golden

This paper presents three technical analyses that serve as verification material for a companion paper (Paper I(a)) on Einstein-Cartan-Holst (ECH) spin-torsion cosmology. The analyses are: (1) a stock-CAMB MCMC analysis of the ΛCDM+ΔNeff model, serving as a null test; (2) a Monte Carlo validation of a NaMaster-based pseudo-Cℓ pipeline for cosmic birefringence; and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper is exceptionally well-written, rigorous, and transparent. The author demonstrates a clear understanding of the subtleties of the analyses, carefully distinguishing between pipeline validation and physical measurement, and between model accommodation and model prediction. The scope of each analysis is clearly defined, and the limitations are stated upfront. The level of detail provided for reproducibility, including explicit discussion of software versions, code configurations, and even prior bugs in analysis artifacts, is exemplary and sets a high standard for the field.

Despite the excellent quality of the manuscript, several revisions are required to meet the publication standards of Physical Review D, primarily concerning the paper's self-containedness and the systematic reporting of effect sizes.

### ESSENTIAL Revisions

*   **P1B-E1: Standalone Readability (Sec. I, p. 2)**
    *   **Problem:** The paper is presented as a "technical verification companion" to Paper I(a) [1]. While this is its function, it must be sufficiently self-contained to be understood by a reader without immediate access to the companion. The introduction states that Paper I(a) "closes the minimal-ECH parameter space as a dark-energy scenario," but it does not explain *why* that closure motivates these three specific numerical checks (a ΔNeff proxy, a birefringence pipeline test, and a spectator-ALP model).
    *   **Required Fix:** Add 2-3 sentences to the introduction (Sec. I) that briefly summarize the key findings of Paper I(a) and explicitly link them to the necessity of the three analyses presented here. For example, explain what aspect of the ECH structural closure motivates a test for an extra radiation-like degree of freedom (ΔNeff), and why cosmic birefringence is a relevant observable to test in this context. This will provide the necessary motivation and allow the paper to be read and understood on its own merits.

### MAJOR Revisions

*   **P1B-M1: Uncomputed Quantitative Claims (Various)**
    *   **Problem:** The paper is generally excellent at quantifying its claims, but in a few instances, it uses qualitative descriptors where a number would be more precise and is readily available from the analysis.
    *   **Required Fix:**
        1.  **Page 10, fn. 5:** The text states that a systematic on Δφ/fa is "well below the ~30% prior-width envelope". Please quantify "well below". For example, state that the systematic is "~3%, an order of magnitude smaller than the prior-width uncertainty".
        2.  **Page 11, MCMC parameter estimation paragraph:** The text states that "wrapped images carry negligible likelihood". While this is certainly true for a posterior confined to |β| ≤ 0.7°, please quantify this. A simple estimate of the distance in σ to the first wrapped image (at β+90°) would suffice to demonstrate how negligible the likelihood is.

*   **P1B-M2: Systematic Reporting of Effect Sizes (Various)**
    *   **Problem:** The paper reports statistical significances (in units of σ) for various tensions and detections, which is standard. However, for a methods-focused paper, it is crucial to also report the physical effect size associated with the significance. This gives a complete picture of the practical importance of the deviation.
    *   **Required Fix:** For each major statistical significance reported, ensure the corresponding physical effect size is also clearly stated.
        1.  **Sec. IV, p. 6:** The `3.6σ` birefringence signal from Eskilt & Komatsu [5] should be accompanied by its effect size, the angle `β = 0.342°`. While this is done, the link should be made more systematic.
        2.  **Sec. III & Table II, p. 4 & 19:** The provisional `+4.3σ` and `-3.6σ` departures in the `w0-wa` plane are a key result of that exploratory section. The text should explicitly state the physical effect sizes: a deviation from `w0=-1` of `Δw0 = +0.188` and a non-zero `wa = -0.667`. These are very large effects and should be highlighted as such.

### MINOR Revisions

*   **P1B-m1: Future/Unusual Dates (Various)**
    *   **Problem:** The paper is dated "June 13, 2026". This should be changed to the date of submission. Several references ([4], [16], [18], [19]) are listed with publication years of (2025) or (2024), which are in the future relative to the typical timeframe of current submissions.
    *   **Required Fix:** Change the paper's date to the submission date. For the references, please verify the publication status. If they are not yet published, it is standard to write "to be published" or simply list the arXiv preprint year.

*   **P1B-m2: Subjective Terminology (Sec. III, p. 3)**
    *   **Problem:** The phrase "publication-quality convergence" is used. This is subjective.
    *   **Required Fix:** Replace this with the quantitative metric used. The paper later uses the Gelman-Rubin statistic `R-1`, so the text should state the quantitative threshold met, e.g., "converged with a Gelman-Rubin statistic R-1 < 0.01 for all sampled parameters".

*   **P1B-m3: Citation of Eskilt & Komatsu [5] (Sec. IV, p. 6)**
    *   **Problem:** The text and footnote 3 do an excellent job clarifying the use of the published PR3+WMAP9 result (`β = 0.342° ± 0.094°`) versus the updated PR4/NPIPE version in the public code repository. However, the abstract and main text repeatedly use the `3.6σ` headline figure derived from the published PR3 analysis.
    *   **Required Fix:** For maximum clarity, ensure that every mention of the `3.6σ` result is explicitly tied to the PR3+WMAP9 analysis, as is done in the abstract. This avoids any potential confusion for readers familiar with the updated PR4/NPIPE data.

### Nitpicks (Cosmetic)

*   **P1B-N1: Typo (Sec. XVI, p. 16):** In the "Likelihood stack" section, the text reads "Chain-to-number maар". This should be "Chain-to-number map".
*   **P1B-N2: Spacing in Filenames (Various):** In several places, there are spaces in filenames that are likely not present in the actual files (e.g., p. 3, fn 1: "COUNT_EXPLANATION. md"; p. 5: "spin torsion.input.yaml"). Please check and correct these.
*   **P1B-N3: Ambiguous Notation (Sec. VIII, p. 8, fn. 4):** The expression `20.32fsky/0.32` is slightly ambiguous. Please clarify with parentheses, e.g., `20.32 * (fsky/0.32)`.

## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality, rigorous, and transparent manuscript that is well-suited for publication in Physical Review D. The author's careful attention to detail, scope, and reproducibility is commendable. The recommendation for "Major Revisions" is primarily driven by the need to make the paper self-contained by providing essential context from its companion paper (P1B-E1). The other major points regarding quantification and effect sizes are intended to bring the entire manuscript up to the exemplary standard set by the best parts of the paper. Once these points are addressed, the paper will represent a valuable and robust contribution to the literature on cosmological data analysis.