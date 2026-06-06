# P1B auto-2026-06-06_0021pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (2846 chars)
**Wall time**: 119.1s

---

**Referee Report on "Technical Verification Companion to the ECH Spin-Torsion Program: ACDM+Neff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model"**

This paper presents technical verification for three distinct cosmological analyses intended to support a companion paper on Einstein-Cartan-Holst (ECH) cosmology. The analyses include: (1) a `ΛCDM+ΔNeff` MCMC analysis as a null test, (2) a `NaMaster` pipeline validation for cosmic birefringence, and (3) a consistency check of a spectator Axion-Like Particle (ALP) model with observed birefringence data.

The paper's strength lies in its careful and transparent scoping of each analysis, clearly stating what is and is not being claimed. The numerical work appears to be sound, and the authors are commendably forthright about the limitations of their results, such as the fine-tuning required in the spectator-ALP model.

However, the paper suffers from significant structural and presentational issues that must be addressed before it can be considered for publication in Physical Review D. The introduction of an entirely separate `w0-wa` analysis without proper framing is highly confusing, and the inclusion of what appears to be an internal review artifact (Table III) is inappropriate for a peer-reviewed publication.

The following is a list of required revisions.

---

### ESSENTIAL

*   **P1B-E1: Un-introduced `w0-wa` Analysis (Sec III, p. 3-4, Table II, p. 4, Sec V.B, p. 6)**
    *   **Problem:** The paper's abstract and introduction outline three specific analyses. However, starting on page 3, the text abruptly begins discussing a fourth analysis: a `w0-wa` model fit to DESI DR2 and other data, with results presented in Table II. This analysis is never introduced, and its discussion is confusingly interwoven with the `ΛCDM+ΔNeff` analysis. This makes the paper's narrative extremely difficult to follow.
    *   **Fix:** The authors must restructure the paper. They have two options:
        1.  Remove the `w0-wa` analysis (Table II and all associated text) entirely, as it is outside the stated scope of the paper.
        2.  Elevate the `w0-wa` analysis to a fourth, fully-fledged topic. This would require rewriting the abstract and introduction to include it, and creating a dedicated section for its methods, results, and discussion, completely separate from the `ΛCDM+ΔNeff` section.

*   **P1B-E2: Internal Review Artifact (Table III, p. 10)**
    *   **Problem:** Table III, "Claims classification for this companion paper," appears to be an internal tracking document. It lists claims and their verification status. This is not appropriate content for a formal scientific publication.
    *   **Fix:** Remove Table III entirely.

### MAJOR

*   **P1B-M1: Fragmented MCMC Discussion (Sec III, p. 2-3 & p. 4)**
    *   **Problem:** The discussion of the primary `ΛCDM+ΔNeff` MCMC analysis is split. The main results are in Section III and Table I, but a detailed and important consistency check (`MB-H0` joint-posterior offset check) is located on page 4, following the out-of-place Table II.
    *   **Fix:** Consolidate all discussion related to the `ΛCDM+ΔNeff` MCMC run into Section III. The `MB-H0` offset check should be moved from page 4 into Section III to create a coherent analysis.

*   **P1B-M2: Crucial Caveats Buried in Footnotes (Sec VI, p. 7 & App C, p. 9)**
    *   **Problem:** The spectator-ALP analysis contains a critical caveat: to remain a "spectator" and not dominate the universe's energy density, the model requires a `~25x` fine-tuning of the initial misalignment angle `θi` relative to its natural prior range. This significantly impacts the interpretation of the result's "naturalness." This crucial information is confined to footnotes (footnote 4 on page 7 and footnote 5 on page 9).
    *   **Fix:** This disclosure is a key part of the physical interpretation of the result. It must be moved from the footnotes into the main body of Section VI. The text should explicitly state that while the model *can* accommodate the observed signal, it requires significant fine-tuning to do so while satisfying the "spectator" condition.

*   **P1B-M3: Confusing Sample Count in Figure Caption (Fig 1, p. 5)**
    *   **Problem:** The caption for Figure 1 states "119,617 post-burnin samples, getdist-thinned from 176,240 raw". However, footnote 1 (page 2) calculates the post-burnin count as `~123,368`. A separate footnote on page 3 explains the 119,617 number is due to additional `getdist` effective-sample weighting. This is confusing for the reader.
    *   **Fix:** Simplify the caption of Figure 1. For example: "Full-tension MCMC corner plot (119,617 plotted samples). The samples are thinned from the full post-burnin chain for visualization; see text for details." The detailed reconciliation of sample counts can remain in a footnote or the main text but should not create ambiguity in the figure caption itself.

### MINOR

*   **P1B-m1: Typo in Birefringence Equation (Eq. 3, p. 7)**
    *   **Problem:** Equation (3) contains the undefined term "OEM". Based on the context and a re-derivation of the result, this is almost certainly a typo for the fine-structure constant, `α_EM`.
    *   **Fix:** Correct "OEM" to `α_EM` in Equation (3).

*   **P1B-m2: Acknowledgment of AI Assistant (Acknowledgments, p. 8)**
    *   **Problem:** The acknowledgment of "Claude (Anthropic) as an AI research assistant" is highly unusual. While the transparency is noted, it is unclear if this aligns with the journal's policies.
    *   **Fix:** The authors should verify this acknowledgment against Physical Review D's editorial policies on authorship and contributions. The editor should also weigh in on its appropriateness.

*   **P1B-m3: Future Dating of Manuscript (p. 1)**
    *   **Problem:** The paper is dated "2026-06-03 PDT".
    *   **Fix:** The date should be corrected to the date of submission.

### NIT

*   **P1B-N1: Parameter Listing in Table I (Table I, p. 3)**
    *   **Problem:** Table I lists both `σ8` and `S8` as separate parameters. While the values are consistent with the standard `S8 = σ8 * (Ωm/0.3)^0.5` relation, it is slightly unusual to list both.
    *   **Fix:** This is not an error, but for clarity, the authors could add a note to the caption clarifying that `S8` is a derived parameter.

---

## Summary recommendation

**MAJOR REVISIONS**

The paper presents a set of well-defined and carefully executed technical analyses. The authors' transparency regarding the scope and limitations of their work is a significant strength. However, the paper is currently undermined by severe structural problems, primarily the confusing and un-introduced `w0-wa` analysis that disrupts the flow of the paper. Additionally, the inclusion of an internal review table is unacceptable for publication. Once the paper is restructured to present its analyses in a clear, logical sequence, and critical information is moved from footnotes to the main text, it will represent a solid contribution worthy of publication in Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from a "fresh eyes" re-review of the paper.

---

### NEW FINDINGS

### MAJOR

*   **P1B-M4: MCMC Priors Inconsistent with "Spectator" Claim (Sec VI & App C)**
    *   **Problem:** The analysis in Section VI is consistently framed as a "Spectator-ALP consistency check." A spectator field, by definition, must have a negligible energy density compared to the background. However, Appendix C and its associated footnote 5 (p. 9) reveal a critical flaw in this framing. The MCMC analysis was performed using a uniform prior on the initial misalignment angle `θi ∈ [0.5, 2]`. As the author correctly notes in the footnotes, this parameter range corresponds to a "dark-energy-ALP regime" where the ALP's energy density is comparable to the critical density (`Ωα ~ 1`). The true spectator regime (`Ωα << 1`) requires `θi ~ 0.1`, a region of parameter space that is entirely excluded by the chosen prior. Therefore, the MCMC analysis presented does not test a spectator ALP model. It tests a dark-energy ALP model. The paper's central claim in this section—that a *spectator* ALP is consistent with observations—is not supported by the simulation that was actually run.
    *   **Fix:** This is a fundamental misrepresentation of the analysis performed. The authors must either:
        1.  Re-run the entire ALP MCMC analysis with a prior that is actually consistent with the spectator condition (e.g., a uniform or log-uniform prior centered on `θi ~ 0.1`).
        2.  Completely re-frame the analysis. This would involve changing the title of Section VI, and rewriting the abstract and conclusions to state that a *dark-energy* ALP model is consistent with the birefringence signal. The discussion of "spectator-status" and its associated fine-tuning would need to be recast accordingly. Given the paper's context, the first option is strongly preferred.

### MINOR

*   **P1B-m4: Ambiguous Citation for Headline Birefringence Value (p. 1, 6, 7)**
    *   **Problem:** The key observational constraint used throughout the paper, `β = 0.342° ± 0.094° (3.6σ)`, is cited to Eskilt & Komatsu [2]. Footnote `a` attempts to clarify that this value is from the "published PR3+WMAP9 joint analysis." However, the abstract of the published PRD version of reference [2] reports a different headline value (`β = 0.30° ± 0.11°`). The value used in this manuscript appears to be from an earlier arXiv preprint or a secondary analysis within the paper that is not the final, highlighted result. This makes it difficult for a reader to trace and verify this crucial input number.
    *   **Fix:** The citation must be made more precise. The authors should specify exactly where this value can be found (e.g., "see Table X of [2]," or "as reported in v2 of arXiv:2205.13962," or "the PR3+WMAP9 analysis detailed in Sec. Y of [2]").