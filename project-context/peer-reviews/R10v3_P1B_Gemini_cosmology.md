# P1B R10v3 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API)
**Wall time**: 66.2s

---

Here is a referee report for the provided paper.

***

## Referee Report for "Technical Verification Companion to the ECH Spin-Torsion Program..."

**Manuscript ID:** [Assigned by journal]
**Author:** Houston Golden
**Journal:** Physical Review D

This paper presents three technical verification analyses intended as a companion to a separate work on Einstein-Cartan-Holst (ECH) spin-torsion cosmology. The analyses are: (1) a standard ΛCDM+ΔNeff MCMC analysis using stock CAMB to serve as a null-consistency test; (2) a Monte Carlo validation of a NaMaster pseudo-Cℓ pipeline for cosmic birefringence; and (3) a consistency check of cosmic birefringence data with a spectator axion-like particle (ALP) model.

The author is commendably careful in scoping the paper, repeatedly emphasizing what is *not* being claimed (e.g., not a test of a specific torsion theory, not a competitive sky detection, not a distinctive ECH prediction). The disclosures regarding fine-tuning and model limitations are transparent and appropriate. The underlying numerical work appears to be sound.

However, the manuscript suffers from significant structural disorganization and a misleading presentation of the ALP analysis, which prevent it from being acceptable for publication in its current form. The paper requires major revisions to improve its logical flow and to accurately represent the results of the ALP MCMC analysis.

### Summary of Findings

**Essential Revisions (must be addressed for acceptance):**
*   The presentation of the spectator ALP analysis is misleading. The MCMC analysis primarily samples a dark-energy ALP parameter space, while the spectator case corresponds to a fine-tuned region. The section title, abstract, and main text must be revised to reflect this distinction accurately.
*   The paper's structure is disorganized. The results of a `w0wa` analysis are introduced abruptly within the section dedicated to the ΔNeff analysis and are scattered across multiple sections. The paper must be restructured to present the cosmological fits in a logical, consolidated manner.

**Major Revisions (significant changes required):**
*   The language used to describe the `w0wa` tension with ΛCDM should be moderated. While the numerical departure is large, the author correctly notes that Bayesian evidence cannot be computed from the MCMC chains. The claims should be framed more cautiously.

**Minor Revisions (recommended for clarity and correctness):**
*   The sample count reported in the caption for Figure 1 needs clarification.
*   Typographical errors in the references must be corrected.
*   A sentence referring to a previous erroneous calculation should be removed.

Detailed comments are provided below.

---

### Detailed Findings

#### ESSENTIAL

**P1B-E1: Misleading framing of the Spectator ALP analysis**
*   **Location:** Section VI (p. 6-7), Appendix C (p. 9), Abstract (p. 1).
*   **Problem:** The analysis is presented as a "Spectator ALP Consistency Check". However, Appendix C (footnote 5) and the main text (footnote 4) reveal that the spectator regime (Ωα ≪ 1) requires a fine-tuned initial misalignment angle θi ~ 0.1. The MCMC analysis uses a uniform prior on θi ∈ [0.5, 2], which almost exclusively samples the dark-energy ALP regime where the ALP's energy density is non-negligible (Ωα ~ 1). The appendix note "Posterior samples at θi ≥ 0.5 correspond to the dark-energy-ALP regime... and should be reinterpreted as samples of a DE-ALP rather than a spectator ALP" confirms this. Therefore, titling the section and framing the result as a *spectator* ALP check is inaccurate. The consistency is only present in a fine-tuned corner of the parameter space that is not representative of the reported posterior.
*   **Required Fix:**
    1.  Rename Section VI to something more accurate, such as "Cosmic Birefringence from an Axion-Like Particle".
    2.  Revise the abstract to clarify that the model explored is a general ultra-light ALP, and that consistency with a *spectator* ALP requires a ~25x fine-tuning of the initial condition, which is not reflected in the MCMC priors.
    3.  The main text of Section VI must be rewritten to bring the distinction between the spectator and dark-energy ALP regimes front and center. The discussion of the MCMC results should explicitly state that the posterior is dominated by DE-ALP models, and the implications for the spectator case should be discussed in that context.

**P1B-E2: Disorganized paper structure regarding cosmological fits**
*   **Location:** Section III (p. 3), Section V (p. 6), Table II (p. 4).
*   **Problem:** Section III is titled "Stock-CAMB ΛCDM+ΔNeff MCMC". However, midway through page 3, it abruptly switches to a detailed discussion of a separate `w0wa` analysis, referencing Table II. The results for the `w0wa` run are then mentioned again in Section V.B, and the ΔNeff results are also repeated there. This makes the paper's narrative difficult to follow and introduces redundancy.
*   **Required Fix:** The paper must be restructured for logical flow.
    1.  Section III should be dedicated *only* to the ΛCDM+ΔNeff MCMC analysis (Table I, Figure 1).
    2.  The `w0wa` analysis (Table II) should be moved entirely to Section V, "Cosmological Fits and Model Comparison".
    3.  Section V should be the single, consolidated location for presenting the results of *all* cosmological parameter estimations (both the ΔNeff and `w0wa` runs). This will eliminate redundancy and improve readability.

#### MAJOR

**P1B-M1: Overstated claim of tension for the `w0wa` model**
*   **Location:** Section III (p. 3), Section V.B (p. 6), Table II (p. 4).
*   **Problem:** The paper states that the `w0wa` posterior "disfavors... the LCDM point" and reports a "+4.3σ" departure for w0. While the calculation of the marginal departure is arithmetically correct, this language is very strong for a "marginal-tail posterior-extrapolation departure," especially since the author correctly states that a robust Bayesian evidence (ln B) cannot be calculated from these MCMC samples because the ΛCDM point is unsampled.
*   **Required Fix:** The language should be toned down. Instead of "disfavors," use more cautious phrasing like "shows a significant departure from" or "indicates a preference for a phantom-crossing model over ΛCDM, motivating a dedicated model comparison analysis." The text should emphasize that while the posterior is far from the ΛCDM point, a definitive model selection statement requires a nested sampling or thermodynamic integration analysis, which is deferred.

#### MINOR

**P1B-MI1: Unclear sample count for Figure 1**
*   **Location:** Figure 1 caption (p. 5), Footnote 1 (p. 2), and text on p. 3.
*   **Problem:** The number of samples for the corner plot is given as 119,617. The reconciliation of this number from the raw count of 176,240 is explained in three different places (footnote 1, a parenthetical remark on p. 3, and the caption itself). This is confusing.
*   **Required Fix:** Consolidate the explanation into a single, clear statement in the caption of Figure 1. For example: "Full-tension MCMC corner plot. The plot shows 119,617 samples, which result from post-burn-in removal (30%) and subsequent getdist effective-sample weight-based thinning of the 176,240 raw accepted samples."

**P1B-MI2: Typographical errors in references**
*   **Location:** References section (p. 9-10).
*   **Problem:** Several references to preprints contain apparent typos in the year or arXiv identifier format.
    *   Ref [3]: "arXiv preprint (2025), arXiv:2509.13654". The year is in the future and the arXiv ID format is incorrect.
    *   Ref [11]: "(2025), arXiv:2507.04265". Future year.
    *   Ref [12]: "(2025), arXiv:2503.14738". Future year.
*   **Required Fix:** The author must carefully check and correct all references, ensuring years and identifiers are accurate.

**P1B-MI3: Inappropriate internal-correction language**
*   **Location:** Section III, "Physics interpretation (Table II)" (p. 3).
*   **Problem:** The text contains the sentence: "An earlier count erroneously quoted '98.6% quintom-B' weight". This reads like a note from an internal draft or review process and is not appropriate for a formal scientific publication.
*   **Required Fix:** Remove this sentence. Simply state the current, correct findings from the converged chain.

#### NIT (Nitpick)

**P1B-N1: Ambiguous dataset label**
*   **Location:** Abstract (p. 1), Table I (p. 3), and throughout the text.
*   **Problem:** The label "full-tension" is used for the dataset combination that includes Planck, BAO, SN, SHOES H0, and DES Y3 S8. While not incorrect, it is less descriptive than it could be.
*   **Required Fix:** For improved clarity, consider using a more explicit label, such as "Planck+BAO+SN+H0+S8", at least upon first mention, to make the distinction from the "Planck+BAO+SN" run immediately obvious.

---

### Summary recommendation

**MAJOR REVISIONS**

This paper serves a useful purpose as a technical companion, and the author has clearly made an effort to be transparent about the scope and limitations of the analyses. The numerical work appears solid. However, the significant issues with the paper's structure and the misleading presentation of the ALP analysis must be thoroughly addressed before the manuscript can be considered for publication. If the author undertakes the essential and major revisions outlined above, the resulting manuscript would be a valuable and clear contribution to the literature.