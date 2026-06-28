# P2 INT-X-P2 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=8d67f8a1 pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 122.9s

---

## Referee Report on "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook"

This paper presents a sensitivity recast of the upcoming SPHEREx survey and the proposed MegaMapper project for a specific matter-bounce cosmological model that predicts a local-type non-Gaussianity of `f_NL = -35/8`. The authors take existing Fisher forecasts for the standard local template and apply a series of corrections to account for the template mismatch with the bounce model, as well as a comprehensive budget of systematic effects. The paper also includes a Bayesian model comparison and a new, independent Fisher forecast for the joint constraints on `f_NL` and its running, `n_fNL`.

The scientific content of the paper is substantial and the analysis is, for the most part, thorough. The authors have carefully considered a wide range of theoretical and observational issues, including a detailed analysis of the bounce bispectrum's polynomial structure, a definitive resolution of a factor-of-two discrepancy in the literature, and a well-motivated systematics budget. The new joint `(f_NL, n_fNL)` forecast is a valuable, original contribution.

However, the paper in its current form suffers from significant structural and presentational issues that obscure its key contributions and make it difficult to follow. The framing of the paper as a "recast" is not entirely accurate, given the inclusion of new, independent calculations. The paper is also excessively long for its primary message, and the presentation of key results, particularly the Bayes factors, is convoluted.

The paper has the potential to be a valuable contribution to the literature, but it requires significant revision to meet the standards of Physical Review D.

### Summary recommendation
**MAJOR REVISIONS**

The paper should be accepted only after the authors have addressed the essential and major points listed below. The primary tasks are to restructure the paper to clearly distinguish between the "recast" and the "new analysis" components, to significantly shorten and tighten the manuscript, and to improve the clarity and directness of the presentation of the main quantitative results.

---
### Detailed Findings

#### ESSENTIAL

**P2-E1: Abstract and Introduction — Misleading Framing of the Joint Fisher Analysis**
*   **Section:** Abstract (p. 1), Introduction (p. 3)
*   **Problem:** The abstract and introduction frame the entire paper as a "sensitivity recast." However, the paper contains a significant new result: a full joint Fisher matrix computation for `(f_NL, n_fNL)` using the scale-dependent bias (SDB) channel. The abstract's description of this is contradictory, first calling it a "heuristic primordial-field scaling check" and then stating it "has now been computed by a joint scale-dependent-bias Fisher." This new computation, which finds a significant 2.0-4.6x degradation of the SDB `f_NL` constraint, is a major, original finding, not a recast. Burying it and misrepresenting its nature is a serious structural flaw.
*   **Required Fix:** The abstract and introduction must be rewritten to clearly and accurately represent the paper's dual contributions: (1) a sensitivity recast of the SPHEREx *bispectrum* forecast, and (2) a new, independent joint Fisher forecast for `(f_NL, n_fNL)` from the *scale-dependent bias* channel. The new result should be highlighted as such.

**P2-E2: Abstract and Body — Inconsistent Significance Range**
*   **Section:** Abstract (p. 1), Sec. IV (p. 10), Fig. 2 (p. 11)
*   **Problem:** The abstract states the "realistic" forecast range is `~2.6-5σ`. This is repeated in the body and Figure 2 caption. However, the optimistic end of the range, derived from the template-corrected baseline, is consistently calculated as `5.2-5.5σ` (e.g., Abstract, p. 1; Sec. IV, p. 9). The `5σ` appears to be an incorrect rounding or a typo. The full post-systematic range spans from the conservative floor of `~2.6σ` (Table IV) to the optimistic ceiling of `~5.5σ` (Table IV, baseline row).
*   **Required Fix:** Correct the upper end of the realistic significance range from `5.0σ` to `5.5σ` in all instances (abstract, main body, figure captions) to be consistent with the paper's own calculations. The range should be stated as `~2.6-5.5σ`.

#### MAJOR

**P2-M1: Paper Structure and Length**
*   **Section:** Entire manuscript
*   **Problem:** At 29 pages, the paper is excessively long for a work whose primary stated goal is a sensitivity recast. The core logic of the recast (applying a template mismatch factor `r` and a systematics budget) is straightforward. The extensive discussions in Sec. II (null-space analysis) and Sec. VI (Bayesian comparison) are overly detailed for the main text and detract from the paper's flow.
*   **Required Fix:** The paper must be significantly condensed. I recommend a target length of 15-18 pages for the main text.
    *   Streamline Sec. II.A: Move the detailed discussion of the monomial basis, SVD analysis, and null-space scan to an appendix. The main text should simply state the result (`r = 0.85 ± 0.13`, `rcos > 0.97`) and its implication (a systematic uncertainty).
    *   Condense Sec. VI.C: The lengthy "Numerical self-consistency check" and the detailed walkthrough of the Bayes factor formula should be moved to an appendix. The main text should present the final results and their physical interpretation.
    *   The prose throughout the paper should be tightened to be more direct and concise.

**P2-M2: Presentation of New `(f_NL, n_fNL)` Result**
*   **Section:** Sec. VII (p. 16), Sec. VIII.D (p. 22)
*   **Problem:** As noted in P2-E1, the new joint Fisher analysis is a major contribution that is currently buried and poorly framed. It appears disjointly in the systematics section (Sec. VII) and the discussion (Sec. VIII.D), with the latter containing the crucial clarification of the "two distinct Fisher analyses."
*   **Required Fix:** Create a new, dedicated section for the joint `(f_NL, n_fNL)` SDB forecast. This section should clearly state the motivation, methodology (distinguishing it from the Heinrich et al. bispectrum forecast), and results (`σ_unmarg`, `σ_marg`, the `p` correlation, and the 2.0-4.6x degradation). This restructuring will properly highlight the new work and improve the paper's logical flow.

**P2-M3: Confusing Presentation of Bayes Factors**
*   **Section:** Sec. VI (p. 14-15), Table II (p. 16)
*   **Problem:** The presentation of the Bayesian results is unnecessarily confusing. Table II reports values for the `r -> 1` (no template mismatch) endpoint, while the abstract and main text quote the final, rebooked numbers for `r ≈ 0.84`. This requires the reader to constantly refer to the "template-mismatch bookkeeping" paragraph and perform mental calculations to connect the table to the headline results. This is not an acceptable presentation.
*   **Required Fix:** Table II must be revised to be the final word on the matter. It should directly report the physically relevant, rebooked Bayes factors for `r ≈ 0.84` (`σ_eff ≈ 0.83`). The `r -> 1` values can be included in parentheses or in a separate column labeled "pre-correction" if the authors feel it is essential, but the primary columns must show the final, headline-ready numbers. The accompanying text should be simplified accordingly.

#### MINOR

**P2-m1: Heuristic for Systematics Budget**
*   **Section:** Abstract (p. 1), Sec. VII (p. 15)
*   **Problem:** The abstract refers to an "additive-quadrature heuristic" without defining it. The reader has to wait until Sec. VII to understand that this means `σ_eff^2 = σ_base^2 + Σσ_syst^2`.
*   **Required Fix:** Briefly define the combination rule (addition in quadrature) in the abstract or introduction when the systematic budget is first mentioned to improve clarity.

**P2-m2: Provenance of Baseline Forecast**
*   **Section:** Abstract (p. 1), Sec. IV (p. 9)
*   **Problem:** The baseline forecast `σ(f_NL) ≈ 0.7` is the anchor for the entire recast. While it is cited correctly as coming from Heinrich et al. [6], this citation should be repeated more frequently to ensure the provenance is clear every time this crucial number is used.
*   **Required Fix:** Add the citation [6] immediately after the `σ(f_NL) ≈ 0.7` value is quoted in the abstract and at its first appearance in the main body sections to reinforce that this is an imported, not a derived, number.

**P2-m3: Data and Code Availability**
*   **Section:** Sec. X (p. 24)
*   **Problem:** The GitHub link points to the `main` branch. For a peer-reviewed publication, this is not sufficient for reproducibility, as the branch will continue to evolve.
*   **Required Fix:** The authors must create a tagged release on GitHub that corresponds to the version of the code used for the final paper. The link in the paper should point to this specific tag. The Zenodo DOI, which is correctly mentioned as pending, will then archive this specific version.

#### NIT (Nitpicks)

**P2-N1: Minor Grammatical Error**
*   **Section:** Abstract (p. 1)
*   **Problem:** "resolving the sign the additive-quadrature heuristic left open"
*   **Required Fix:** Change to "resolving the sign that the additive-quadrature heuristic left open".

**P2-N2: Figure 2 Caption Inconsistency**
*   **Section:** Fig. 2 Caption (p. 11)
*   **Problem:** The caption describes the "all-combined conservative endpoint 2.6-2.8σ" and gives a complex formula for `σ_eff`. This level of detail is excessive for a caption and belongs in the main text or Table IV notes.
*   **Required Fix:** Simplify the caption to describe what the bars represent without reproducing the calculation. Refer the reader to Sec. VII and Table IV for the detailed breakdown of the systematic budget.