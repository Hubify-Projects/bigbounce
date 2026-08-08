# P1B INT-X-P1B — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=d013792f pages=22
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 142.7s

---

## Referee Report: Technical Verification Companion to the ECH Spin-Torsion Program

This paper presents three technical analyses intended as a verification companion for a primary work (Paper I) on the Einstein-Cartan-Holst (ECH) spin-torsion cosmology. The analyses are: (1) a stock-CAMB MCMC run for a ΛCDM+ΔNeff model, serving as a null test for extra radiation; (2) a Monte Carlo validation of a NaMaster pseudo-Cℓ pipeline for measuring cosmic birefringence; and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper is exceptionally thorough, methodologically rigorous, and transparent about the scope and limitations of each analysis. The author consistently and correctly distinguishes between pipeline validation figures and sky-detection significance, and between model accommodation and model prediction. The level of detail provided for reproducibility is commendable. The core analyses are sound and meet the high standards of Physical Review D.

However, several issues require significant revision before the paper can be accepted for publication. The most critical points concern the standalone readability of the manuscript, which relies heavily on a companion paper not yet available, and the presentation of a key diagnostic result (the `w₀wₐ` cross-check) which, despite strong caveats, may still be misinterpreted.

### ESSENTIAL Findings

None.

### MAJOR Findings

**ID: P1B-M1**
*   **Section/Page:** Throughout, starting on p. 1 (Abstract) and p. 2 (Sec. I).
*   **Problem:** The paper is presented as a "companion" to "Paper I(a) [1]". The citation for [1] is a placeholder: "H. Golden, ..., (2026), companion paper, posted concurrently on arXiv." This makes the present manuscript not self-contained. The motivation for the specific analyses, the definition of the ECH framework, and the context for the "no-go program" are all deferred to this unavailable reference. A reader cannot evaluate the relevance or completeness of the technical verifications without access to the primary paper they are meant to support. While common for companion papers submitted simultaneously, for the archival record, the paper must be readable on its own terms.
*   **Required Fix:** The introduction must be expanded to provide the minimal necessary context from Paper I for a reader to understand the purpose and significance of the three analyses presented here. This should include a concise, self-contained summary of:
    1.  The specific prediction or scenario from ECH that motivates the ΔNeff proxy test.
    2.  The specific ECH prediction (or lack thereof) related to birefringence that motivates the spectator-ALP consistency check.
    3.  The structural results from Paper I that these numerical checks are intended to verify or contextualize.
    This can be done in a new subsection (e.g., "Summary of the ECH Framework and Motivation from Paper I") without requiring a full reproduction of the companion paper.

**ID: P1B-M2**
*   **Section/Page:** p. 4 (Sec. III.a) and p. 6 (Table II).
*   **Problem:** The paper discusses a `w₀wₐ` analysis and correctly states in multiple places that due to an uncorrected overlap in supernova samples (DES-Y5 x Pantheon+), "no σ-distance or significance from ACDM is quotable." This is an appropriate and necessary caveat. However, the text and Table II still present posterior constraints like `w₀ + wₐ = -1.4788 ± 0.1485` and `w_pivot = -0.952 ± 0.019`. Presenting a central value and a 1σ error bar for a parameter invites the reader to compute a significance, even if the text warns against it. For example, `( -1 - (-0.952) ) / 0.019 ≈ 2.5σ`. This presentation undermines the force of the caveat and creates an internal tension in the manuscript's claims. The recent removal of explicit sigma-distances was a correct step, but the presentation of error bars on the parameters themselves still implies a level of statistical confidence that the paper itself states is invalid.
*   **Required Fix:** To be fully consistent with the "no significance is quotable" caveat, the `w₀wₐ` results in the main text and in Table II should be reported as central values only, with the error bars removed. The text should explicitly state that the posterior widths are artificially narrowed by the likelihood product and are therefore not reported. Alternatively, the authors could report medians and 95% credible intervals, which are less prone to interpretation as a Gaussian significance, but the first option is strongly preferred for clarity and consistency. The discussion should focus solely on the direction of the posterior shift (the "quintom-B direction"), which the paper argues is plausible, rather than the "width" of that posterior.

### MINOR Findings

**ID: P1B-m1**
*   **Section/Page:** p. 7, Eskilt & Komatsu disambiguation (footnote 3).
*   **Problem:** The footnote provides an excellent and necessary clarification regarding the Planck data release (PR3 vs. PR4/NPIPE) used in the Eskilt & Komatsu (2022) analysis and the public code. However, the main text simply states it uses the "Eskilt-Komatsu joint WMAP+Planck summary likelihood (β = 0.342° ± 0.094° [5])".
*   **Required Fix:** To ensure the provenance is clear in the main text, add a brief parenthetical clarification directly after the citation, e.g., "(using the published PR3+WMAP9 value; see fn. 3 for data release details)". This makes the main text more robust for readers who may not read footnotes carefully.

**ID: P1B-m2**
*   **Section/Page:** p. 15, ALP dark-energy fraction Ωα.
*   **Problem:** The text states: "Marginalizing H₀ over the Planck 1σ interval shifts Ωα by ≤ 3% (Ωα ∝ H₀⁻²), well below the statistical uncertainty of the Ωα < 0.01 cut." The scaling `Ωα ∝ H₀⁻²` is not immediately obvious from Eq. (9), which has `H₀²` in the numerator (`ρ_crit,0`) and a complex `z_osc` dependence in the denominator, where `z_osc` itself depends on `H(z)`.
*   **Required Fix:** Briefly justify the `H₀⁻²` scaling or provide a more complete expression. From Eq. (9), `ρ_crit,0 = 3H₀²M_Pl²`. From Eq. (7), for heavy axions where `z_osc` is large, `H(z_osc) ≈ H₀√Ω_m(1+z_osc)³ ≈ mₐ/3`, so `(1+z_osc)³ ≈ mₐ²/ (9H₀²Ω_m)`. This would make `Ωα ∝ H₀² / (1+z_osc)³ ∝ H₀⁴`. For light axions where `z_osc ≤ 0`, the denominator is constant, so `Ωα ∝ H₀⁻²`. The text should clarify which regime leads to the stated scaling and confirm it is the relevant one for the marginalization.

**ID: P1B-m3**
*   **Section/Page:** p. 17, Data and Code Availability.
*   **Problem:** The text provides a GitHub link and identifies the paper version with a tag (`v1B.0.80`) and commit hash (`b22f8cc9`). This is excellent practice.
*   **Required Fix:** The author should ensure that this specific tag and commit hash are finalized and pushed to the public repository before publication, and that they will remain permanently accessible. This is a verification check, not a required text change, but it is crucial for the paper's archival value.

### NIT-PICKS (Cosmetic)

**ID: P1B-N1**
*   **Section/Page:** p. 1, Abstract.
*   **Problem:** The sentence "both are MC pipeline-recovery figures, not sky-measurement systematics, and are not directly comparable to each other's published sky significances" is slightly awkward.
*   **Required Fix:** Suggest rephrasing for clarity, e.g., "both are pipeline-recovery metrics derived from Monte Carlo simulations, not systematics of the sky measurement, and are therefore not directly comparable to published on-sky detection significances."

**ID: P1B-N2**
*   **Section/Page:** p. 5, Table I caption.
*   **Problem:** The file path `reproducibility/cosmology/c13_s8_desy3_overlay.json` is included directly in the caption. While useful for reproducibility, it is unconventional for a journal publication.
*   **Required Fix:** Consider moving the explicit file path to Appendix A (Reproducibility Materials) and referring to it from the caption, e.g., "(see Appendix A for artifact details)".

## Summary recommendation

**MAJOR REVISIONS**

This is a high-quality technical paper characterized by careful methodology, rigorous analysis, and exemplary transparency. The work is valuable and suitable for publication in Physical Review D. However, the revisions classified as "MAJOR" are necessary to ensure the paper is self-contained and that its results are presented in a way that is fully consistent with the stated caveats, particularly regarding the supernova analysis. Once these points are addressed, the paper will be a strong contribution to the literature on cosmological data analysis methods.