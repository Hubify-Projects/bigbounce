# P1A D2 — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=fad68a47 pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (3677 chars)
**Wall time**: 183.5s

---

Referee Report for manuscript P1A

**Title:** Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Author:** Houston Golden

This paper investigates four potential channels within the minimal Einstein-Cartan-Holst (ECH) framework as sources for late-time dark energy. It concludes that all four channels are "closed" (i.e., ruled out) under a set of stated assumptions. The primary reasons for closure are amplitude suppression, parity violation constraints, and a naturalness objection related to the cosmological constant problem. The paper's main positive result is a "perturbation-transparency" theorem, demonstrating that for canonical scalar matter, the Holst sector of ECH gravity decouples from scalar and tensor perturbations at all orders, rendering its effects invisible in standard cosmological observables like the CMB power spectra and bispectrum. The paper also highlights a structural tension between the number of e-folds required for a hypothetical ECH dark-energy mechanism and the survival of a key observational signature of matter-bounce models (`f_NL`).

The paper is comprehensive and commendably transparent about its assumptions and limitations. The perturbation-transparency result is rigorous and an important clarification for the ECH framework. The analysis closing the various dark-energy routes is systematic. However, the paper suffers from several major issues that prevent its acceptance in its current form. The most significant are its reliance on results from inaccessible companion papers and the non-rigorous, phenomenological nature of the central dark-energy mechanism it sets out to test.

A recommendation of **MAJOR REVISIONS** is made. The specific points to be addressed are detailed below.

### ESSENTIAL Revisions

**P1A-E1: Standalone Readability and Reliance on Companion Papers (ESSENTIAL)**
*   **Location:** Throughout, but particularly Sec. IV (p. 4), Table IV (p. 27), and various footnotes.
*   **Problem:** The paper is not self-contained, in violation of journal policy. It repeatedly cites companion papers that are "in preparation" or "posted concurrently" ([2], [6], [23], [46]) for load-bearing information. For example, the cosmological parameters in Table IV (`H₀`, `ΔN_eff`, etc.) are sourced from an internal MCMC analysis detailed in [6]. The detailed `f_NL` forecast is deferred to [2]. While the author claims the paper's main structural arguments do not depend on these specific numerical values, their inclusion makes large parts of the discussion (e.g., regarding cosmological tensions) unverifiable. A referee cannot and should not have to take such results on faith.
*   **Fix:** All results necessary to support the claims made in this manuscript must be included, derived, and explained within this manuscript, or cited from a work that is publicly available on a preprint server (e.g., arXiv) or in a peer-reviewed journal. Placeholder citations to "in preparation" works are unacceptable. The authors must either integrate the relevant methods and results into this paper (e.g., in an appendix) or remove the claims that rely on them.

**P1A-E2: Manuscript Date (ESSENTIAL)**
*   **Location:** Page 1.
*   **Problem:** The manuscript is dated "June 19, 2026," a date in the future.
*   **Fix:** The date must be corrected to the date of submission.

### MAJOR Revisions

**P1A-M1: Framing of the Phenomenological Dark-Energy Ansatz (MAJOR)**
*   **Location:** Abstract (p. 1), Sec. I (p. 3), Sec. II C (p. 7), Appendix B (p. 26).
*   **Problem:** The entire investigation into ECH as a source of dark energy hinges on a "phenomenological on-shell scaling ansatz." As the paper correctly and honestly states, the underlying parity-odd operator (Eq. 6) has an off-shell mass dimension of +1, not the +4 required for a valid term in a local effective field theory Lagrangian. The "fix" is to assume that on-shell evaluation at the Planck-scale bounce supplies the missing three powers of mass. This assumption is the weakest link in the paper's argument. While the paper's conclusion is to "close" these routes, the current framing (including the paper's title) gives undue prominence to a mechanism that is not derived from the fundamental theory. Furthermore, the paper itself provides a powerful physical argument (the "reheating thermal-reset barrier," Sec. II C 1, p. 9) that would erase any such bounce-era remnant, effectively invalidating the mechanism from the start.
*   **Fix:** The paper should be substantially restructured to reflect the relative rigor of its conclusions. The robust, well-derived results—the perturbation-transparency theorem (Sec. X) and the structural tension between `N_tot` and `f_NL` survival (Sec. XIV D)—should be the primary focus of the paper, presented upfront in the abstract and introduction. The "closure of four dark-energy routes" should be framed as a secondary consequence, with the non-rigorous nature of the ansatz emphasized from the outset. The title should be revised to better reflect this focus, for example by prioritizing "Perturbation Transparency in Einstein-Cartan-Holst Gravity".

**P1A-M2: Inconsistent `f_NL` Forecast Significance (MAJOR)**
*   **Location:** Abstract (p. 1), Sec. VII (p. 15), Footnote 6 (p. 15).
*   **Problem:** The paper quotes a "2.6-5σ" realistic significance for the SPHEREx forecast of `f_NL = -35/8`. The derivation of this range is opaque and appears inconsistent across different parts of the text. Footnote 6 on page 15 states that the degraded sensitivity is `σ(f_NL) ≈ 1.0`, which for a signal of `f_NL = -4.375` implies a significance of ~4.4σ. The footnote mentions an "optimistic" range of `~5-5.5σ` and a "realistic" range of `2.6-5σ`, but does not provide a clear, step-by-step derivation for the 2.6σ lower bound.
*   **Fix:** The authors must provide a clear, transparent derivation for the full range of quoted significances. This should include the assumptions about systematics (e.g., GR projection, photo-z degradation, bias uncertainty) that lead to the different values in the range, allowing the reader to understand the origin of the "2.6σ" figure.

### MINOR Revisions

**P1A-m1: Heuristic Dilution Pre-factor (MINOR)**
*   **Location:** Sec. II C 1 (p. 8), Eq. (11).
*   **Problem:** The dilution factor `D_inf` includes a pre-factor `(T_reh / M_GUT)^(3/2)` which is justified on grounds of "dimensional-analysis aesthetic" rather than a physical calculation. The paper correctly notes that the exponential term `exp[-3N_tot]` is dominant.
*   **Fix:** Given the acknowledged lack of rigor, the authors should consider either removing this pre-factor and working only with the robust exponential scaling, or providing a more physical, albeit order-of-magnitude, argument for its inclusion (e.g., from a simple phase-space estimate).

**P1A-m2: Definition of "Closure" (MINOR)**
*   **Location:** Introduction (p. 3).
*   **Problem:** The term "closure" or "closed" is used frequently to mean a theoretical channel is ruled out or constrained to be phenomenologically unviable. While the meaning is generally clear from context, it is jargon that may not be universally understood.
*   **Fix:** Add a sentence in the introduction explicitly defining what is meant by "channel-level closure" in the context of this paper (e.g., "a channel is considered 'closed' if its predicted observable effects are suppressed by many orders of magnitude relative to current observational bounds, or if the mechanism requires fine-tuning analogous to the cosmological constant problem it purports to solve.").

### NITs (Cosmetic)

**P1A-N1: Non-academic Affiliation/Email (NIT)**
*   **Location:** Page 1, Page 2.
*   **Problem:** The author is listed as an "Independent Researcher" and the contact email is a non-academic, commercial domain. This is unusual for PRD.
*   **Fix:** This is a note for the editorial office, which may have its own policies. No action is required from the author unless requested by the editor.

**P1A-N2: Companion Paper Citation Style (NIT)**
*   **Location:** Bibliography (p. 28-29).
*   **Problem:** Several companion papers are cited with the year "(2026)" and a description, but no arXiv identifier.
*   **Fix:** Upon resubmission, if these papers are available on the arXiv as stated, the citations should be updated to include the proper identifiers.

## Summary recommendation

**MAJOR REVISIONS**

This manuscript contains the seeds of a valuable contribution to the cosmology literature. The perturbation-transparency theorem is a clear, rigorous, and useful result for anyone working with ECH gravity. The structural tension argument is also a powerful, physically-motivated constraint. However, the paper in its current form is not acceptable. The framing over-sells a dark-energy analysis that is based on a non-rigorous ansatz, and its critical dependence on results from inaccessible companion papers makes it unverifiable. The authors must perform a significant revision to make the paper self-contained and to restructure the narrative to focus on its most robust and defensible conclusions. If these major issues can be satisfactorily addressed, the revised manuscript would likely be suitable for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the second-pass review, incorporating new findings as requested.

================================================================
Referee Report for manuscript P1A (Second Pass)

This report contains new findings from a second, more detailed review, in addition to the points raised in the initial report. Findings from the first report are not repeated unless expanded upon.

### MAJOR Revisions

**P1A-M3: Incorrect Internal Cross-Reference in Abstract (MAJOR)**
*   **Location:** Abstract (p. 1).
*   **Problem:** The abstract states: "we acknowledge missing operators (...) explicitly in Sec. IV and Sec. XI." While Section IV's scope paragraph does mention this, Section XI ("The Hybrid Dark-Energy Loophole") does not. Section XI is dedicated to discussing the addition of a `w₀wₐ` dark energy component. The primary discussion of the paper's limited operator basis is in the "Scope and limitations" paragraph of Section I (p. 3). This incorrect cross-reference in the abstract is a significant navigational error that misdirects the reader from the outset.
*   **Fix:** The cross-reference in the abstract must be corrected to point to the correct section(s) where the scope and limitations of the operator basis are discussed (e.g., Sec. I).

### NITs (Cosmetic)

**P1A-N3: Minor Figure-Text Discrepancy (NIT)**
*   **Location:** Figure 5 (p. 18) and Appendix B (p. 26).
*   **Problem:** Figure 5 displays the fine-tuning score for ΛCDM with a bar extending to 10¹²⁰ on the x-axis. However, the text (e.g., Appendix B) and the caption refer to the canonical value of the hierarchy as ~10¹²², which is the more precise number.
*   **Fix:** For consistency, the label on the bar in Figure 5 should be updated to match the text, or the graphical representation adjusted.

## Re-evaluation and Confirmation of Initial Report

The second pass confirms the validity and importance of the issues raised in the initial review.

*   **Arithmetic and Internal Consistency:** The paper's arithmetic is generally sound where it can be checked (e.g., significance calculations for `β`, `ρ_e` estimation). However, the central inconsistency regarding the `f_NL` forecast significance (**P1A-M2**) remains. The paper quotes a `σ(f_NL) ≈ 1.0` which implies a ~4.4σ detection, yet the abstract and body repeatedly use a "2.6-5σ" range without deriving the 2.6σ lower bound. This remains a major point of opacity.
*   **Dimensional Analysis:** The dimensional inconsistency of the core parity-odd operator (Eq. 6) is an intentional, and explicitly acknowledged, feature of the paper's "phenomenological ansatz". The second pass confirms that the paper is transparent about this fundamental weakness. This reinforces the recommendation in **P1A-M1** that the paper's narrative should be restructured to de-emphasize this non-rigorous mechanism and instead highlight the robust results (the perturbation-transparency theorem).
*   **Cross-References and Comparability:** The paper is commendably careful in distinguishing between different null hypotheses when comparing `σ` values (**E-class issues**). However, the discovery of a clear cross-referencing error in the abstract (**P1A-M3**) lowers confidence in the manuscript's overall polish.

The conclusion remains the same: the manuscript requires **MAJOR REVISIONS**. The core issues of making the paper self-contained (**P1A-E1**), correcting the date (**P1A-E2**), reframing the narrative around its robust conclusions (**P1A-M1**), and clarifying the `f_NL` forecast (**P1A-M2**) are essential for the paper to be considered for publication. The newly identified cross-reference error (**P1A-M3**) must also be corrected.