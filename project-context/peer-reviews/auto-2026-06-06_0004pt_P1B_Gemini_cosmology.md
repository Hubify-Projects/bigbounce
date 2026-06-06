# P1B auto-2026-06-06_0004pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 114.2s

---

## Referee Report for Manuscript [P1B]

**Title:** Technical Verification Companion to the ECH Spin-Torsion Program: ACDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model

**Authors:** Houston Golden

---

### General Comments

This manuscript presents three distinct technical analyses intended to support a companion paper on Einstein-Cartan-Holst (ECH) cosmology. The analyses are: (1) a stock-CAMB MCMC analysis of the ΛCDM+ΔNeff model as a proxy for new radiation-like degrees of freedom, (2) a Monte Carlo validation of a NaMaster pseudo-Cℓ pipeline for cosmic birefringence, and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper is exceptionally well-scoped, with the authors taking great care to state the precise limitations of each analysis. The distinction between a direct test of a theory, a proxy test, a pipeline validation, and a model-consistency check is clearly maintained throughout. The numerical work appears to be sound, and my spot-checks of the calculations presented were successful. The transparency regarding methodology, data, code availability, and model caveats (such as the fine-tuning required in the spectator-ALP scenario) is commendable and sets a high standard for reproducibility. The inclusion of a "Claims Classification" table is a novel and welcome feature.

While the overall quality of the work is high, I have identified several points that require revision before the manuscript can be considered for publication in Physical Review D. The most significant of these concerns the integration and motivation of a fourth analysis (on the `w0-wa` model), which currently feels disconnected from the main narrative.

---

### Findings

#### MAJOR

*   **P1B-M1: Integration of the `w0-wa` Analysis**
    *   **Location:** Section III (p. 3) and Section V.B (p. 6), Table II (p. 4).
    *   **Problem:** The paper's title and abstract frame the work around three specific analyses (ΔNeff proxy, NaMaster recovery, ALP check). However, a significant portion of the text (end of Sec. III, Table II, parts of Sec. V) is dedicated to a fourth analysis of a `w0-wa` dark energy model, which finds a >4σ departure from ΛCDM. This analysis feels disconnected from the other three and its relevance to the ECH program is not sufficiently established. The text mentions it is "consistent with the bounce / pre-Big-Bang scenario," but this link is asserted rather than derived or explained in detail. This makes the `w0-wa` results appear as a standalone discovery claim shoehorned into a verification paper.
    *   **Required Fix:** The authors must either:
        1.  Significantly strengthen the connection between the `w0-wa` analysis and the ECH spin-torsion program discussed in the companion paper (Paper I(a)). This would require more than a single sentence of motivation.
        2.  Restructure the paper to explicitly frame it as presenting four analyses, and update the title and abstract accordingly.
        3.  Alternatively, given that this is a "Technical Verification Companion," the authors could consider removing the `w0-wa` analysis and presenting it separately in a more appropriate context, which would streamline the focus of the current manuscript.

#### MINOR

*   **P1B-m1: Discrepant Sample Counts in Figure 1 Caption**
    *   **Location:** Page 5, Figure 1 caption and Footnote 1 on page 3.
    *   **Problem:** The text and footnotes refer to several different sample counts for the same MCMC run (e.g., 176,240 raw, 123,368 post-burn-in, 119,617 getdist-thinned). While this is explained across multiple footnotes, it is confusing for the reader. The caption for Figure 1 uses the "getdist-thinned" number, which is the least intuitive of the set.
    *   **Required Fix:** Consolidate the explanation of sample counts. The caption for Figure 1 should state the post-burn-in sample count before thinning (123,129 for this specific chain subset) and then mention that the plot shows a getdist-thinned representation of these samples for visual clarity. This makes the connection to the analysis statistics more direct.

*   **P1B-m2: Missing Appendix B**
    *   **Location:** Page 9.
    *   **Problem:** The appendix section jumps from Appendix A to Appendix C. Appendix B is missing.
    *   **Required Fix:** Re-label the appendices sequentially (A, B, C...). "Claims Classification" should be Appendix B, and "ALP-MCMC Sampled Parameters..." should be Appendix C.

*   **P1B-m3: Acknowledgment of AI Assistant**
    *   **Location:** Page 8, Acknowledgments.
    *   **Problem:** The manuscript acknowledges the use of "Claude (Anthropic) as an AI research assistant." While transparency is good, the use of AI in manuscript preparation is a new and evolving area. The journal may have specific policies regarding this.
    *   **Required Fix:** The authors should ensure this acknowledgment complies with the editorial policies of Physical Review D. This is a note for the authors and the editor to confirm. No change is required if it is compliant.

#### NIT (Nitpicks & Typos)

*   **P1B-N1: Typo in Birefringence Equation**
    *   **Location:** Page 7, Equation (3).
    *   **Problem:** The equation uses the symbol `ΟΕΜ`. This is almost certainly a typo for the fine-structure constant, `αEM`.
    *   **Required Fix:** Replace `ΟΕΜ` with `αEM`.

*   **P1B-N2: Inconsistent σ Notation**
    *   **Location:** Page 1, Abstract.
    *   **Problem:** The abstract reports the Eskilt & Komatsu result as `β = 0.342° ±0.094° (3.60)`. The symbol `σ` is used for the standard deviation, but the significance is given as `3.60` without the `σ` symbol. This is a minor inconsistency.
    *   **Required Fix:** For clarity, write as `(3.6σ)`. This is done correctly elsewhere in the paper (e.g., page 7, eq. 4).

*   **P1B-N3: Footnote Reference Formatting**
    *   **Location:** Page 1, Abstract.
    *   **Problem:** The footnote reference `[2, 3];ª` is awkwardly formatted.
    *   **Required Fix:** The footnote marker `a` should appear directly after the citation, e.g., `[2, 3]ª`.

*   **P1B-N4: Awkward Phrasing in Footnote 1**
    *   **Location:** Page 2, Footnote 1.
    *   **Problem:** The sentence "...post-burnin samples remain across both frozen chains (convergence_summary.json)." is slightly awkward. The filename in parentheses is not standard academic style.
    *   **Required Fix:** Rephrase to something like: "...post-burn-in samples remain across both frozen chains, as detailed in the convergence summary files."

---

### Summary recommendation

**MINOR REVISIONS**

This is a high-quality technical paper characterized by careful methodology, clear scoping, and a laudable commitment to transparency and reproducibility. The core analyses are sound and well-presented. The primary reason for not recommending immediate acceptance is the need to better integrate or separate the `w0-wa` analysis, which currently disrupts the narrative flow of the paper. Once this structural issue is addressed and the minor corrections are made, the manuscript will be a strong candidate for publication in Physical Review D.