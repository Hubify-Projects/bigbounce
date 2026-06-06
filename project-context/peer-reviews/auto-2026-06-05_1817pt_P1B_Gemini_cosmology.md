# P1B auto-2026-06-05_1817pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 128.7s

---

## Referee Report for Manuscript by H. Golden

**Title:** Technical Verification Companion to the ECH Spin-Torsion Program: ACDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model

This manuscript presents three technical analyses intended as a companion to a primary paper on Einstein-Cartan-Holst (ECH) cosmology. The analyses include: (1) a stock-CAMB MCMC analysis of the ΛCDM+ΔNeff model as a proxy for new radiation-like physics, (2) a Monte Carlo validation of a NaMaster-based pipeline for measuring cosmic birefringence, and (3) a consistency check of the observed birefringence signal with a spectator axion-like particle (ALP) model.

The paper is generally well-scoped, with the author taking care to explicitly state the limitations of each analysis. The MCMC proxy and pipeline validation are straightforward and appear to be correctly executed. The ALP consistency check contains a valuable analysis but also reveals a significant fine-tuning problem and a methodological issue in the MCMC setup. However, the manuscript suffers from a severe structural problem concerning an un-introduced analysis, as well as other issues that must be addressed before it can be considered for publication in Physical Review D.

### ESSENTIAL Revisions

**P1B-E1: Un-introduced and Misplaced `w₀wₐ` Analysis**
*   **Location:** Abstract, Introduction, Sec. III (p. 3), Table II (p. 4), Sec. V (p. 6), Conclusions (p. 8).
*   **Problem:** The paper's abstract and introduction frame the work as documenting three specific analyses. However, starting on page 3, the text abruptly introduces results from a fourth analysis—a `w₀wₐ` dark energy model fit to DESI DR2 and other data. This analysis is never formally introduced, its motivation is unclear in the context of the other three topics, and its results are scattered confusingly throughout the paper. Table II is dedicated to it, Section V incorrectly points to it, and the Conclusions section confusingly frames it as "Forward" work despite its results being presented as a main finding. This makes the paper's structure and narrative incoherent.
*   **Required Fix:** The author must choose one of two options:
    1.  **Remove the `w₀wₐ` analysis entirely.** This would make the paper consistent with its stated scope in the abstract and introduction.
    2.  **Fully integrate the `w₀wₐ` analysis.** This requires rewriting the abstract, introduction, and overall structure to present it as a fourth, motivated analysis. Its purpose and connection to the ECH program must be made explicit. The current disjointed presentation is unacceptable.

**P1B-E2: Methodological Inconsistency in ALP MCMC Prior**
*   **Location:** Sec. VI (p. 7, fn. 4) and Appendix C (p. 9, fn. 5).
*   **Problem:** The paper presents an "ALP-MCMC" to check the consistency of a *spectator* ALP model with birefringence data. However, the MCMC samples the initial misalignment angle `θᵢ` from a uniform prior on [0.5, 2]. As explicitly and commendably disclosed in footnotes 4 and 5, the spectator condition (`Ωₐ << 1`) is only satisfied in the "sub-natural sliver `θᵢ ~ 0.1`," which requires a `~25x` fine-tuning relative to the prior midpoint. This means the MCMC was run almost entirely outside the parameter space corresponding to the physical model it claims to be testing. The posterior samples overwhelmingly correspond to a dark-energy ALP (`Ωₐ ~ 1`), not a spectator ALP. Presenting these results as a consistency check for a "spectator-ALP" is misleading.
*   **Required Fix:** The author must correct this methodological flaw. Either:
    1.  Re-run the MCMC analysis with a physically motivated prior that enforces the spectator condition (e.g., a prior on `θᵢ` centered in the `~0.1` region).
    2.  Re-frame the entire analysis. The "spectator" language must be removed, and the section should be presented as a constraint on a dark-energy ALP model. The current presentation, which claims to test one model while sampling the parameter space of another, is not permissible.

**P1B-E3: Inappropriate "Claims Classification" Table**
*   **Location:** Table III (p. 10).
*   **Problem:** Table III, titled "Claims classification for this companion paper," lists the paper's own claims and assigns them a "Status" such as "Verified," "Omitted," or "Cited." This table reads like an internal project management checklist and is entirely inappropriate for a peer-reviewed scientific publication. The verification of claims is the purpose of the paper's content and the peer-review process itself, not something to be asserted in a summary table.
*   **Required Fix:** Remove Table III entirely.

### MAJOR Revisions

**P1B-M1: Prominence of the ALP Fine-Tuning Caveat**
*   **Location:** Sec. VI (p. 7, fn. 4) and Conclusions (p. 8).
*   **Problem:** The analysis reveals that explaining the observed birefringence signal with a spectator ALP requires a `~25x` fine-tuning of the initial misalignment angle `θᵢ`. This is a critical weakness of the model's "naturalness" and a major physical takeaway of that section. While the author is transparent about this in footnotes and a brief mention in the conclusions, its significance warrants a more prominent discussion in the main body of Section VI. Hiding such a crucial result in a footnote is insufficient.
*   **Required Fix:** Move the core content of footnote 4 into the main text of Section VI. The paragraph should explicitly discuss the tension between the "natural" parameter space and the sub-region required for spectator status, and what this `~25x` fine-tuning implies for the viability of the model.

### MINOR Revisions

**P1B-m1: Inconsistent MCMC Sample Count in Figure 1 Caption**
*   **Location:** Fig. 1 Caption (p. 5) and fn. 1 (p. 2).
*   **Problem:** The caption for Figure 1 states it shows "119,617 post-burnin samples, getdist-thinned from 176,240 raw". However, footnote 1 on page 2 calculates the post-burnin (30%) sample count as `176,240 * 0.7 ≈ 123,368`. A brief explanation for the discrepancy is buried in the main text on page 3 ("additional getdist effective-sample weight-based thinning"). This is confusing for the reader.
*   **Required Fix:** Clarify the sample count directly in the Figure 1 caption. For example: "119,617 effective post-burnin samples, obtained after a 30% burn-in cut (123,368 samples) and additional getdist weight-based thinning."

**P1B-m2: Incorrect Table Reference in Section V.B**
*   **Location:** Sec. V.B (p. 6).
*   **Problem:** The text states, "The χ² goodness-of-fit decomposition (BAO, CMB, SN, and total contributions) is reported in Table II". This is incorrect. Table II contains results for the `w₀wₐ` analysis. The ΔNeff analysis results are in Table I, which does not contain a χ² decomposition.
*   **Required Fix:** Correct this sentence. If a χ² decomposition for the ΔNeff run is available, it should be added to Table I. If not, the sentence should be removed.

**P1B-m3: Minor Numerical Typos**
*   **Location:** p. 4.
*   **Problem:** The text states: "The full-tension chain returns H₀ = 67.69 ± 1.06 km/s/Mpc with ΔNeff = -0.02 ± 0.17". Table I gives these values as H₀ = 67.68 ± 1.06 and ΔNeff = -0.020 ± 0.169.
*   **Required Fix:** Correct the numerical values in the text on page 4 to match Table I precisely.

### NITs (Nitpicks)

**P1B-N1: Internal Revision Language**
*   **Location:** p. 3.
*   **Problem:** The text includes the phrase "An earlier count erroneously quoted '98.6% quintom-B' weight". This kind of language, which refers to previous internal drafts or errors, is not professional and should not appear in a final manuscript.
*   **Required Fix:** Remove this phrase. Simply state the current result from the converged chain.

**P1B-N2: Manuscript Date**
*   **Location:** p. 1.
*   **Problem:** The manuscript is dated "2026-06-03 PDT".
*   **Required Fix:** Change the date to the current submission date.

## Summary recommendation
**MAJOR REVISIONS**

This manuscript provides several useful technical verifications. The author's commitment to clearly scoping the analyses and disclosing limitations is commendable. However, the paper is critically undermined by severe structural problems, most notably the incoherent inclusion of an entire analysis that is not properly introduced or motivated. Furthermore, the ALP consistency check suffers from a major methodological flaw where the MCMC explores a parameter space inconsistent with the physical model being claimed. These essential issues, along with the inappropriate inclusion of an internal "claims" table, must be fully resolved before the manuscript can be reconsidered for publication. If the author can restructure the paper logically and correct the methodology of the ALP analysis, the resulting work could be a valuable companion to their main research program.