# P2 RC-INT — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=5e23ad4c pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 152.3s

---

As a referee for Physical Review D, I have completed a thorough review of the manuscript "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook." The paper presents a detailed sensitivity recast of the SPHEREx forecast for a specific matter-bounce model predicting `f_NL = -35/8`. The analysis is comprehensive, including a careful audit of the theoretical prediction, quantification of template mismatch, a detailed systematic budget, and a Bayesian model comparison. The authors are commendably transparent about the limitations of their analysis, particularly regarding the heuristic nature of the systematic budget and the underlying physical assumptions.

However, the manuscript requires significant revisions to meet the standards of Physical Review D. The primary issues relate to the structure and focus, the prominence of critical caveats, and the inclusion of speculative, tangential analyses. The current structure buries key results in a lengthy discussion, and the main narrative is diluted by a detailed secondary analysis that would be better placed in an appendix.

Below is a detailed list of findings and required corrections.

## Referee Report

### ESSENTIAL

**P2-E1: Abstract & Conclusion Must State the Primary Physical Caveat**
*   **Section:** Abstract (p.1), Sec. II C (p.6), Conclusion (p.24)
*   **Problem:** The entire forecast rests on "assumption (d): faithful third-order bispectrum transmission through the bounce." The body of the paper (Sec. II C, p.6) is commendably honest that this is "the weakest link of the present derivation," as it is verified only at linear order and supported by a non-rigorous estimate at cubic order. The abstract correctly includes this caveat. However, the Conclusion (Sec. X) omits it entirely. A reader looking only at the introduction and conclusion would miss the single most important theoretical uncertainty underpinning the entire paper.
*   **Required Fix:** The Conclusion must be revised to include a clear, concise statement reiterating that the entire forecast is conditional on the unverified assumption of faithful cubic-order transfer through the bounce, citing this as the primary theoretical weakness. This is essential for a balanced summary of the work's implications.

### MAJOR

**P2-M1: Manuscript Structure and Length**
*   **Section:** Entire manuscript, particularly Sec. IX.D (p.22-23)
*   **Problem:** At 29 pages, the paper is excessively long for a sensitivity recast. The narrative is significantly diluted by the detailed, "methodologically distinct" joint `(f_NL, n_fNL)` scale-dependent-bias (SDB) Fisher forecast presented in Sec. IX.D. The paper itself correctly frames this as a "subordinate cross-check on the scale dependence, not a competitor to the bispectrum-only headline." However, it occupies substantial space in the main discussion, introducing a new Fisher matrix, different redshift bins, and a complex degeneracy analysis that distracts from the primary bispectrum result.
*   **Required Fix:**
    1.  Move the detailed derivation and discussion of the joint `(f_NL, n_fNL)` SDB Fisher forecast (most of Sec. IX.D) to a dedicated appendix.
    2.  In the main body (Discussion), retain only a summary paragraph stating the key result: that the `f_NL-n_fNL` degeneracy degrades the SDB-only constraint, reinforcing the importance of the bispectrum channel. This will shorten the paper, improve its focus, and clarify the hierarchy of the results for the reader. The main text should focus squarely on the bispectrum recast.

**P2-M2: Heuristic Systematic Budget vs. Joint Covariance**
*   **Section:** Abstract (p.1), Sec. VII (p.16), Table IV (p.20)
*   **Problem:** The paper's headline "realistic" significance range (2.6-5.5σ) is derived from a systematic budget (Table IV) where individual systematic contributions are added in quadrature. The paper correctly calls this an "additive-quadrature heuristic" and "not a joint-covariance forecasted measurement precision." In contrast, the subordinate SDB analysis *does* use a joint Fisher matrix and finds that correlations significantly *loosen* the constraints (a 2.0-4.6x degradation). This strongly suggests that the quadrature-addition for the primary bispectrum channel may be optimistic. While the paper is honest about the methodology, the potential weakness of the headline result needs to be emphasized more strongly.
*   **Required Fix:** The abstract and conclusion must more forcefully state that the headline systematic budget for the primary bispectrum channel is heuristic and does not account for potential correlations between systematic parameters (e.g., `b_1`, `b_φ`, GR projection effects), which were shown to be important in the SDB channel. This is a critical clarification of the result's robustness.

**P2-M3: Tangential Parity-Odd Discussion (Cosmic Birefringence)**
*   **Section:** Sec. X.E.a (p.24)
*   **Problem:** The paragraph on cosmic birefringence is speculative and tangential. Primordial non-Gaussianity from the scalar bispectrum is a parity-even observable. Cosmic birefringence is a parity-odd observable. While a bounce *model* could be constructed to produce both, the paper presents no such model, nor does it establish any predictive link between `f_NL = -35/8` and a specific birefringence angle `β`. This section reads as an unrelated "consistency check" that adds no rigor to the main `f_NL` forecast. It is poor practice to mix parity sectors without a firm theoretical motivation.
*   **Required Fix:** Remove the cosmic birefringence paragraph (Sec. X.E.a) entirely. The paper's focus is on the scalar bispectrum, and this detour weakens its coherence.

### MINOR

**P2-m1: Inconsistent Terminology for `f_NL`**
*   **Section:** Throughout, e.g., Abstract (p.1), Conclusion (p.24)
*   **Problem:** The paper uses `f_NL^local`, `f_NL^local`, `f_NL`, and `f_NL` interchangeably. While the context often clarifies the meaning, PRD standards require precision. The matter-bounce template is *local-type* but not perfectly local. The forecast uses a *local-template* estimator.
*   **Required Fix:** Standardize the notation. I suggest:
    *   `f_NL^local` for the parameter of the pure local template.
    *   `f_NL^bounce` for the amplitude of the matter-bounce signal (whose squeezed limit is -35/8).
    *   `σ(f_NL^local)` for the forecasted uncertainty on the local-template amplitude.
    This should be applied consistently throughout the abstract, body, tables, and figures. The abstract currently uses `f_NL^local = -35/8`, which is imprecise; it should state that the bounce model predicts a signal with this squeezed-limit amplitude.

**P2-m2: Recomputation of Abstract/Headline Values**
*   **Section:** Abstract (p.1), Sec. IV (p.9), Table IV (p.20)
*   **Problem:** The abstract quotes a "realistic ~2.6-5.5σ" range. The 5.5σ ceiling corresponds to the optimistic, no-systematics case. The 2.6σ floor corresponds to the most pessimistic, all-systematics-combined case. Calling the entire range "realistic" is slightly misleading. The 5.5σ value is explicitly pre-systematics.
*   **Required Fix:** Rephrase in the abstract to be more precise. For example: "After template-mismatch correction we obtain a bispectrum-only significance of 5.2-5.5σ, which reduces to a realistic envelope of ~2.6-5.5σ after including a heuristic budget for systematics..." This clarifies that the upper end of the range is the pre-systematics value.

**P2-m3: Table II Caption Clarity**
*   **Section:** Table II (p.16)
*   **Problem:** The caption is dense and contains several nested calculations and explanations. The sentence beginning "The promoted abstract headline BF ≈ 9-14 applies the noise-weighted r = 0.84 rebooking..." is crucial but hard to parse. The distinction between the `r→1` endpoint values in the table and the `r=0.84` values in the headline needs to be exceptionally clear.
*   **Required Fix:** Restructure the caption of Table II for clarity. Use bullet points or a separate note to explain the rebooking from the tabled `r→1` values to the abstract's `r=0.84` headline values. For example: "Note: The headline Bayes factor range of BF ≈ 9-14 quoted in the abstract is derived by applying the noise-weighted template mismatch factor `r=0.84` to the `r→1` values in this table (e.g., the recommended row 1 value of ~10 becomes ~9.2)."

### NIT

**P2-N1: Typo in Equation Reference**
*   **Section:** Abstract (p.1)
*   **Problem:** The abstract states: "We audit the Cai et al. bispectrum, establishing via the in-in operator identity i<[ζ³, L]) = -2Im(ζ³L) (verified symbolically; Appendix A.1) that their intermediate e-order decomposition (Eqs. 34-36, single time-ordering) is exactly half the full result..." This is a key finding of the paper's audit. However, the reference is to Appendix A.1, while the explicit derivation and discussion of the `-2Im` identity is in the main text of Appendix A and equation (A3) on page 26.
*   **Required Fix:** Change the reference in the abstract from "Appendix A.1" to simply "Appendix A" or "Eq. (A3)" for precision.

**P2-N2: Typo in Squeezed Limit Definition**
*   **Section:** Sec. II.A (p.3)
*   **Problem:** The text defines the squeezed limit: "where k = k2 ≈ k3 denotes the hard-mode scale and k1 ≪ k is the squeezed (long-wavelength) mode."
*   **Required Fix:** The `≈` symbol is imprecise. It should be `k=k2=k3` in the idealized limit. Change to "where `k=k2=k3` denotes the hard-mode scale..." for clarity.

**P2-N3: Typo in B_NL definition**
*   **Section:** Sec. VIII.B (p.8)
*   **Problem:** The text contains the phrase `|ABNL|/|Bueeze|`.
*   **Required Fix:** Correct the typo to `|ΔB_NL|/|B_NL^squeeze|` or similar, consistent with the context.

## Summary recommendation

**MAJOR REVISIONS**

This manuscript represents a substantial and valuable piece of work. The authors have performed a careful and self-critical recast, which is a service to the community. The transparency regarding assumptions and methodological limitations is a major strength. However, the paper in its current form is not suitable for publication in PRD due to significant issues with its structure, length, and the clarity of its core message. The key SDB analysis, while valuable, clutters the main narrative and should be moved to an appendix. The main physical caveat of the analysis needs to be present in the conclusion, and the discussion of unrelated parity-odd physics should be removed. Once these structural and clarity issues are addressed, the paper will be a strong candidate for publication.