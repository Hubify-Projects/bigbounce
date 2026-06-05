# P1B auto-2026-06-05_1617pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 158.0s

---

## Referee Report on "Technical Verification Companion to the ECH Spin-Torsion Program..."

This paper presents three technical verification analyses intended to support a companion paper on Einstein-Cartan-Holst (ECH) cosmology. The analyses cover: (1) an MCMC analysis of the ΛCDM+ΔNeff model as a proxy for new radiation-like physics, (2) a validation of a NaMaster-based pipeline for measuring cosmic birefringence, and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper demonstrates a high level of technical competence in its individual calculations, provides excellent reproducibility materials, and is commendably careful in scoping its claims and noting important caveats. However, the manuscript in its present form suffers from a critical structural flaw that mixes results from different analyses, rendering sections of the paper incoherent. Additionally, the interpretation of the ALP analysis requires significant clarification. For these reasons, the paper requires major revisions before it can be considered for publication in Physical Review D.

### Summary of Findings

**ESSENTIAL**

*   **P1B-E1 (Sec III, V; pp. 3, 4, 6): Structural Confusion Between MCMC Analyses.** The paper's narrative is critically flawed by the conflation of two separate MCMC analyses: the advertised ΛCDM+ΔNeff analysis (results in Table I) and an unadvertised `w0wa` analysis (results in Table II).
    *   **Problem:** The "Physics interpretation" section on page 3 abruptly begins discussing the `w0wa` posterior, which has not been introduced. Section V ("Cosmological Fits and Model Comparison") incorrectly claims that the χ² decomposition for the ΛCDM+ΔNeff run is reported in Table II, which actually corresponds to the `w0wa` run. The text on page 4 mixes discussion of results from both tables, making the arguments impossible to follow. The `w0wa` analysis is not mentioned in the abstract or introduction's list of the paper's three documented analyses.
    *   **Required Fix:** The author must fundamentally restructure the paper. The recommended solution is to remove the `w0wa` analysis and Table II from the main body to keep the paper focused on its three advertised topics. The analysis can be briefly mentioned in the "Forward" section of the conclusion, as is already done. This requires removing all `w0wa`-related discussion from Sections III and V and deleting Table II. Alternatively, if the author wishes to include it as a main result, the abstract, introduction, and overall structure must be rewritten to properly incorporate it as a fourth distinct analysis, with its methodology and results presented in a new, self-contained section.

**MAJOR**

*   **P1B-M1 (Sec VI, Appendix C; pp. 7, 9): Misleading Interpretation of the ALP Analysis.** The paper presents an ALP consistency check, but the distinction between the parameter space sampled by the MCMC and the specific "spectator" ALP regime is not made sufficiently clear in the main text.
    *   **Problem:** The MCMC analysis uses a prior on the initial misalignment angle of θᵢ ∈ [0.5, 2]. As correctly stated in footnote 5 (p. 9), this parameter range corresponds to an ALP that would behave as dark energy, not a simple spectator field. The true spectator regime (Ω_a ≪ 1) requires θᵢ ~ 0.1, which is outside the sampled prior range and requires a ~25x fine-tuning. The abstract and main text emphasize the "spectator" model, but the MCMC results presented are not actually for that model.
    *   **Required Fix:** The main text of Section VI must be revised to state this critical distinction clearly. It should be made explicit that the MCMC posterior primarily constrains a dark-energy ALP model, and that interpreting this result in the context of a *spectator* ALP requires the significant fine-tuning disclosed in the footnotes. The abstract's framing should also be reviewed for clarity on this point.

*   **P1B-M2 (pp. 2, 3, 5): Inconsistent MCMC Sample Counts.** The number of post-burn-in samples for the full-tension ΛCDM+ΔNeff chain is reported inconsistently throughout the manuscript.
    *   **Problem:** Footnote 1 (p. 2) implies a post-burn-in count of 123,368. The text on p. 3 gives the number 123,129. The caption for Figure 1 (p. 5) states the plot uses 119,617 thinned samples. While these differences may have valid explanations (e.g., thinning for plotting), the lack of a clear, consistent accounting is confusing.
    *   **Required Fix:** The author must reconcile these numbers. State a single, definitive post-burn-in sample count for the analysis. In one location (e.g., the footnote where the calculation is first shown), clearly explain any subsequent thinning or weighting that leads to different numbers being used for plots or effective sample size calculations.

**MINOR**

*   **P1B-m1 (Sec VI, fn. 4; p. 7): Typo in ALP Energy Density Formula.** The formula for the ALP backreaction fraction contains a typo.
    *   **Problem:** Footnote 4 gives the scaling `Ωα ~ ... (m² f² / H³ M²₁) θ²`. The Hubble parameter in the denominator should be squared.
    *   **Required Fix:** Correct the formula to `Ωα ~ (m² f_a² / (H_0² M_pl²)) θ_i²` or similar, consistent with the standard definition of Ω_a = ρ_a / ρ_crit.

*   **P1B-m2 (p. 6): Opaque Calculation of Pipeline Bias Dependence.** The text describes the NaMaster pipeline bias as having a "~12% amplitude-dependent component," but the origin of this number is not explained.
    *   **Problem:** The text states the bias changes from 0.032° to 0.040° as the injected signal changes. It is not clear how "12%" is derived from these numbers.
    *   **Required Fix:** Add a brief clarification or parenthetical showing how the 12% figure is calculated to improve transparency.

*   **P1B-m3 (p. 3): Internal Review Language.** The text contains phrases that appear to be remnants of an internal drafting or review process.
    *   **Problem:** Phrases like "An earlier count erroneously quoted..." and "prior caveat promised a Savage-Dickey ratio..." are inappropriate for a final publication.
    *   **Required Fix:** Remove this language and present the final, corrected analysis directly.

*   **P1B-m4 (Bibliography; p. 10): Errors in Bibliography.** The bibliography contains formatting errors and missing information.
    *   **Problem:** For example, reference [20] (Torrado & Lewis) is missing the publication year and has a duplicated entry number ("05 (057), 057").
    *   **Required Fix:** The entire bibliography should be carefully proofread and corrected to ensure all entries are accurate and consistently formatted according to PRD style.

**NIT**

*   **P1B-N1 (Sec IV; p. 5): Generic Section Title.** The title for Section IV is overly generic.
    *   **Problem:** "DATA METHODS: CMB E-B ANALYSIS" does not fully capture that the section is a specific validation of the NaMaster pipeline.
    *   **Required Fix:** Consider a more descriptive title, such as "NaMaster Pipeline Validation for Birefringence Analysis."

### Summary recommendation
**MAJOR REVISIONS**

The paper contains valuable technical work and demonstrates a commitment to reproducibility and careful scoping that is commendable. However, the essential structural flaw (P1B-E1) that conflates two separate analyses makes key sections of the paper incorrect and unreadable. This issue must be resolved before the paper can be properly evaluated. Furthermore, the major clarifications required for the ALP analysis (P1B-M1) are necessary to ensure the results are not misinterpreted. Once these fundamental issues are addressed, the paper has the potential to be a useful technical companion worthy of publication.