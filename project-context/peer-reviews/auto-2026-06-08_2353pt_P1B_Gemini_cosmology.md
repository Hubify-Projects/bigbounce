# P1B auto-2026-06-08_2353pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 201.7s

---

## Referee Report on "Technical Verification Companion to the ECH Spin-Torsion Program..."

**Manuscript ID:** [Assigned by journal]
**Author:** Houston Golden
**Date:** 2026-06-08

### Summary of the Paper
This manuscript serves as a technical companion to a primary paper on Einstein-Cartan-Holst (ECH) cosmology. It documents three distinct numerical analyses:
1.  A Markov Chain Monte Carlo (MCMC) analysis of the ΛCDM+ΔNeff model using stock CAMB, presented as a null-consistency test for an extra radiation-like degree of freedom.
2.  A validation of a NaMaster-based pseudo-Cℓ pipeline for measuring cosmic birefringence, using Monte Carlo simulations to quantify the pipeline's recovery bias.
3.  A consistency check of published birefringence measurements with a spectator axion-like particle (ALP) model.

The paper is commendably clear about the scope and limitations of each analysis, carefully distinguishing between pipeline validation and sky detection, and between model-consistency checks and unique theoretical predictions.

### General Comments
The manuscript provides valuable technical verification for its companion paper. The methodology is generally sound, and the author is transparent about the limitations of the analyses, which is a significant strength. However, there are several issues related to the structure, clarity of key claims, and correctness of specific calculations that must be addressed before the paper can be considered for publication in Physical Review D. The most significant issues are the confusing presentation of a w0wa analysis, which reports a >4σ tension with ΛCDM but is buried within a section on ΔNeff, and the misleading framing of the "spectator" ALP analysis, where the chosen parameter priors are inconsistent with the spectator assumption.

### Findings

---
**ESSENTIAL REVISIONS**
---

**P1B-E1: Misleading Structure and Buried Results of the w0wa Analysis**
*   **Location:** Section III (p. 3) and Section V (p. 6), Table II (p. 4).
*   **Problem:** Section III is titled "Stock-CAMB ΛCDM+ΔNeff MCMC". However, the second half of this section ("Physics interpretation (Table II)") and the entirety of Table II are dedicated to a completely different analysis of a w0wa dark energy model. This w0wa analysis finds a significant departure from ΛCDM (wo departs by +4.3σ, wa by -3.6σ). This is a major physics result in its own right, but it is presented as a side-note to the null result of the ΔNeff proxy test. This structure is extremely confusing and diminishes the impact of what appears to be a significant finding. The connection between the ΔNeff proxy test and the w0wa test is not made clear, and they should not be conflated in the same section.
*   **Required Fix:** The paper must be restructured. The w0wa analysis should be presented in its own dedicated section, separate from the ΛCDM+ΔNeff analysis. The abstract and introduction should be updated to reflect that the paper presents *two* cosmological parameter analyses with distinct conclusions: a null result for ΔNeff and a significant tension with ΛCDM from a w0wa model. The motivation for and interpretation of the w0wa result (e.g., as a test of quintom models) should be clearly and separately articulated.

**P1B-E2: Inconsistent Framing of the "Spectator ALP" Analysis**
*   **Location:** Section VI (p. 7), Abstract (p. 1), Appendix C (p. 9), Footnote 6 (p. 10).
*   **Problem:** The analysis in Section VI is repeatedly referred to as a "Spectator-ALP consistency check". However, the spectator status of the ALP requires the initial misalignment angle to be small (θi << 1), as correctly disclosed in footnote 5 (p. 7), which states the spectator-consistent regime is θi ~ 0.1. Despite this, the MCMC analysis uses a uniform prior of θi ∈ [0.5, 2] (Appendix C). This prior explicitly *excludes* the spectator regime and primarily samples the "dark-energy-ALP" regime where the ALP's energy density is non-negligible. The clarification that this is the case is buried in footnote 6 on the final page of the paper. This is insufficient. The current framing is misleading; the analysis does not primarily test a spectator ALP.
*   **Required Fix:**
    1.  The title of Section VI must be changed from "Spectator ALP Consistency Check" to something more accurate, such as "Light ALP Model Consistency Check".
    2.  The abstract's description of this analysis must be revised to remove the "spectator" label or to clarify that the model spans both spectator and dark-energy-like regimes.
    3.  The crucial information in footnote 6 must be moved into the main body of Section VI. The text must explicitly state that the chosen prior largely corresponds to a dark-energy ALP, and discuss the implications of the posterior results in that context. The fine-tuning required to enter the true spectator regime must be highlighted in the main text, not just a footnote.

---
**MAJOR REVISIONS**
---

**P1B-M1: Incorrect Calculation in Table II Footnote**
*   **Location:** Page 4, Table II, footnote b.
*   **Problem:** The footnote provides a formula and calculation to reproduce the uncertainty on wpivot, σ(wpivot) = ±0.0301. The calculation shown is: σ²_pivot = (0.0436)² + (0.3320)²(0.1864)² = (0.0301)². This is numerically incorrect. My re-computation yields sqrt[(0.0436)² + (0.3320)²(0.1864)²] ≈ 0.0757, which is a factor of 2.5 larger than the claimed value. The formula itself appears to be incorrect for the variance of a pivot parameter defined to decorrelate wo and wa.
*   **Required Fix:** The author must provide the correct formula for σ(wpivot) and a calculation that correctly reproduces the value of ±0.0301 given in the table. If the value in the table is incorrect, it must be corrected, and any conclusions based on it must be re-evaluated.

---
**MINOR REVISIONS**
---

**P1B-m1: Clarity on MCMC Sample Counts**
*   **Location:** Page 3 (footnote 1), Page 5 (Fig. 1 caption).
*   **Problem:** The number of samples for the full-tension chain is given as 176,240 (raw), 123,368 (post-burn-in), and 119,617 (getdist-thinned). While the information is present across footnotes and figure captions, it is disjointed. A reader might be confused about which sample count corresponds to the results in Table I and the plots.
*   **Required Fix:** Add a sentence in the main text of Section III clarifying the relationship between the raw, post-burn-in, and getdist-thinned effective sample counts, and state which count is used for generating the final posterior statistics in Table I.

**P1B-m2: Bibliography Formatting**
*   **Location:** Page 11, References.
*   **Problem:** Some references have minor formatting issues. For example, reference [20] for Cobaya lists the journal information as "Journal of Cosmology and Astroparticle Physics 05 (057), 057", which is redundant, and is missing the publication year (2021).
*   **Required Fix:** Please review the bibliography for completeness and correct formatting consistent with PRD style (e.g., include publication years, remove redundancies).

---
**NIT-PICKING**
---

**P1B-N1: Informal Language**
*   **Location:** Page 3, "Physics interpretation (Table II)".
*   **Problem:** The text states: "An earlier count erroneously quoted '98.6% quintom-B' weight". While the transparency is appreciated, this phrasing is somewhat informal for a journal publication.
*   **Required Fix:** Rephrase to be more formal, for example: "This result corrects an earlier, preliminary analysis which had suggested a higher statistical weight for this model."

### Summary recommendation

**MAJOR REVISIONS**

This manuscript provides a set of useful and carefully scoped technical validations. The author's transparency regarding the limitations of the work is a commendable strength. However, the paper cannot be accepted in its current form. The structural flaw of burying a significant >4σ result from a w0wa analysis within a section focused on a different model's null result is a critical issue that confuses the paper's core message. Furthermore, the framing of the "spectator ALP" analysis is misleading given the choice of MCMC priors, and this requires substantial clarification and reframing. Finally, the numerical error in a key table's footnote undermines confidence in the paper's technical precision. Once these essential and major issues have been thoroughly addressed, the paper will likely be suitable for publication in Physical Review D.