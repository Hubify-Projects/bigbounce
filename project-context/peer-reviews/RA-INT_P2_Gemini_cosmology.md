# P2 RA-INT — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=8dabb71b pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 174.4s

---

### **Referee Report: P2**

**To the Editor of Physical Review D,**

I have reviewed the manuscript "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook" by Houston Golden. The paper presents a detailed sensitivity recast for testing the matter-bounce scenario's prediction of fNL = -35/8 using upcoming data from SPHEREx and the proposed MegaMapper. The core of the work is the application of a template-mismatch correction to an existing SPHEREx forecast, supplemented by a comprehensive systematic budget, a Bayesian model comparison, and a discussion of related observables.

The paper is exceptionally thorough and demonstrates a high level of rigor in its analysis, particularly in resolving a factor-of-two discrepancy in the literature regarding the predicted fNL value and in quantifying the template mismatch. However, its length (29 pages) is substantial for what is ultimately a "sensitivity recast" rather than a new, independent forecast. Several areas require significant revision to meet the standards of Physical Review D, primarily concerning the clarity of the systematic budget's application, the justification for certain methodological choices, and the need to streamline the presentation.

Below is a detailed list of findings.

---

### **Detailed Findings**

#### **ESSENTIAL**

**P2-E1: Abstract-Body Mismatch in Systematic Budget Application (Abstract-Last Drift Sweep)**
*   **Section/Page:** Abstract (p. 1) vs. Sec. IV (p. 9) and Sec. VII (p. 15)
*   **Problem:** The abstract presents a "realistic ~2.6-5.5σ" range. The body and Table IV (p. 20) clarify this is a "scoping sensitivity envelope under an additive-quadrature heuristic systematic budget, not a joint-covariance forecasted measurement precision". The abstract omits this crucial qualification, potentially misleading readers into interpreting the range as a rigorous, joint-Fisher forecast. The distinction between a heuristic envelope and a formal precision forecast is fundamental.
*   **Fix:** The abstract must be revised to include the same caveat as the body. It should explicitly state that the realistic range is a "scoping sensitivity envelope" based on an "additive-quadrature heuristic" and that a "full bispectrum joint Fisher over the systematic nuisances is not performed here." This is non-negotiable for PRD-level precision.

**P2-E2: Ambiguous Provenance of the SDB Fisher Forecast**
*   **Section/Page:** Abstract (p. 1) and Sec. IX.D (p. 22)
*   **Problem:** The abstract mentions a "joint scale-dependent-bias (SDB) Fisher matrix for (fNL, nfNL) (c8_fnl_running_fisher.json, Planck 2018, CAMB 1.6.6)". This implies a new computation is performed in this paper. Section IX.D confirms this is a "new galaxy-covariance Fisher computation". However, the paper's primary framing is as a "sensitivity recast". Presenting a new, independent Fisher forecast as a "subordinate cross-check" within a recast paper is confusing and undersells the new work while also diluting the paper's main focus. The contribution is not clearly delineated.
*   **Fix:** The authors must decide on the paper's primary contribution.
    1.  If it is the **recast**, the new SDB forecast should be moved to an appendix or a separate, shorter publication. The main text should only refer to its conclusions as needed.
    2.  If the paper is presenting **both** a recast and a new forecast, the abstract and introduction must be rewritten to frame it as a dual-contribution paper. The current structure, which buries the new computation deep in the discussion section, is unacceptable.

**P2-E3: Inconsistent Comparison of Significance Values**
*   **Section/Page:** Table IV (p. 20), caption.
*   **Problem:** The caption states: "its 6.25σ figure is not directly comparable to the template-corrected 5.2-5.5σ headline because it uses a distinct null procedure (no template-mismatch correction applied)." While this is a correct and necessary qualification, the "Naive uncorrected" value is still presented in the same table as the other values, inviting comparison. This is a recurring issue; different stages of the analysis (naive, template-corrected, post-systematics) produce sigma values that are not on equal footing.
*   **Fix:** The "Naive uncorrected" row should be removed from Table IV entirely. The caption's text is sufficient to explain why it's not a valid starting point. The value can be mentioned in the main text with the same qualification, but its inclusion in a consolidated budget table is misleading. This principle applies elsewhere: any side-by-side presentation of sigmas from different analysis stages must be heavily caveated *at the point of presentation*.

#### **MAJOR**

**P2-M1: Justification for Additive-Quadrature Systematic Budget**
*   **Section/Page:** Sec. VII (p. 15) and Table IV (p. 20)
*   **Problem:** The paper combines all systematic uncertainties in quadrature (`σ_eff = sqrt(σ_base^2 + Σ σ_i^2)`). The text acknowledges this is a "transparent scoping heuristic, not a joint multi-tracer marginalized Fisher". However, it also notes that correlations, particularly the `b1-fNL-nfNL` degeneracy, can "loosen rather than tighten the constraint". Using a simple quadrature sum, which assumes uncorrelated errors, is a significant simplification. While a full joint Fisher is stated to be beyond the scope, the choice of this specific heuristic over others (e.g., linear addition for a conservative bound) is not sufficiently justified.
*   **Fix:** The authors must provide a stronger justification for using additive quadrature. They should discuss the expected signs of the dominant correlations and explain why this choice is a reasonable approximation. They should also compute and present the result under a more conservative assumption (e.g., linear addition of errors for the dominant systematics) to demonstrate the robustness of their "realistic" envelope. The text in Sec. VII acknowledging the `b1-b_phi-fNL` degeneracy is good but needs to be more central to the justification of the heuristic.

**P2-M2: Overstated Precision of the Null-Space Scatter**
*   **Section/Page:** Abstract (p. 1) and Sec. II (p. 4)
*   **Problem:** The abstract quotes a null-space scatter of "±0.13 in r". Section II clarifies this is basis-dependent: "the quoted scatter should therefore be read as indicative of the null-space spread under this stated convention rather than as a calibrated, basis-independent uncertainty." The abstract omits this crucial caveat. Quoting a number to two decimal places implies a precision that the body text itself disclaims.
*   **Fix:** The abstract must qualify this number. For example: "...with an indicative basis-dependent scatter of ±0.13 in r...". The body should also emphasize that other valid basis choices could yield different scatter values, reinforcing that this is an estimate of the magnitude of the effect, not a precise error bar.

**P2-M3: Paper Length and Structure**
*   **Section/Page:** Entire manuscript (29 pages)
*   **Problem:** The paper is excessively long for a sensitivity recast. The core results—the template mismatch factor `r` and its application to the Heinrich et al. forecast—could be presented much more concisely. The manuscript includes extensive reviews, multiple cross-checks, a new SDB forecast, and a detailed Bayesian analysis that, while rigorous, bloats the page count and obscures the primary message.
*   **Fix:** The paper must be significantly restructured and shortened, aiming for a length closer to 12-15 pages for the main body.
    *   Move the detailed derivation of the Cai/Li discrepancy (currently in Appendix A and Sec. II.C) and the symbolic verification into a more comprehensive appendix. The main text should only summarize the conclusion.
    *   Move the new SDB joint (fNL, nfNL) forecast to an appendix or a separate paper (see P2-E2).
    *   Condense the multiple cross-checks of the template overlap `r` (l-space Fisher, injection-recovery) into a single summary paragraph in the main text, with details in an appendix.
    *   The Bayesian comparison (Sec. VI) is valuable but overly detailed. The main text should present the final Bayes factor table and its interpretation, moving the detailed discussion of the formula, prior sensitivity, and numerical checks to an appendix.

**P2-M4: Ambiguity in the `r` factor application**
*   **Section/Page:** Abstract (p. 1)
*   **Problem:** The abstract states: "`r` is applied as a shape-weighted degradation to the Heinrich et al. baseline rather than recomputed as an independent cross-Fisher matrix, making this a sensitivity recast rather than an independent forecast." This is a clear and accurate statement. However, it also says "Only the noise-weighted r ≈ 0.83 enters the SPHEREx significance". This is confusing. Does `r` degrade the signal (`fNL -> r * fNL`) or inflate the error (`σ -> σ/r`)? Equation (5) on page 8 shows `σ(f_bounce) = σ(f_local)/r`, which is an error inflation. The abstract should be equally precise.
*   **Fix:** Rephrase the abstract to be explicit about how `r` is applied. For example: "...degrading the effective significance by inflating the local-template uncertainty σ(f_NL^local) to σ(f_NL^bounce) = σ(f_NL^local)/r." This clarifies the mechanism.

#### **MINOR**

**P2-m1: Inconsistent `rcos` bounds**
*   **Section/Page:** Sec. IV (p. 4)
*   **Problem:** The text states "The shape cosine exceeds 0.97 for all 10,000 samples at radius 50 (rcos = 0.985 ± 0.007)". A few lines below, it says "The rcos > 0.97 bound applies specifically to the radius-50 scan... the rcos > 0.95 bound is the conservative floor confirmed across the full multi-radius convergence test". This is slightly confusing.
*   **Fix:** Clarify this by combining the statements. E.g., "The shape cosine exceeds 0.97 for all 10,000 samples in our fiducial radius-50 scan (mean rcos = 0.985 ± 0.007). A conservative floor of rcos > 0.95 holds across all scan radii tested (10-500), confirming the shape stability is not an artifact of our fiducial volume."

**P2-m2: Unclear Provenance of `b_phi` Marginalization**
*   **Section/Page:** Abstract (p. 1)
*   **Problem:** The abstract mentions "PNG-bias bφ marginalization" as part of the systematic budget. However, the imported Heinrich et al. forecast (Ref [6]) does *not* marginalize over `b_phi` as a free parameter; it fixes it via a universality relation. The text in Sec. IV and VII clarifies this, but the abstract implies it was part of the baseline forecast.
*   **Fix:** The abstract should be clearer. State that the degradation comes from *relaxing the assumption* of a fixed universality relation for `b_phi` and marginalizing over it, which widens the uncertainty.

**P2-m3: Calculation Check in Table II**
*   **Section/Page:** Table II (p. 16)
*   **Problem:** The caption states "The recommended row 1 maps 9.8→9.2". Let's recompute. `σ_eff = 0.7 / 0.84 = 0.833`. The original BF is 9.80 (from text, p. 14). The new BF should be `BF_new ≈ BF_old * (σ_old / σ_new) = 9.8 * (0.7 / 0.833) = 8.23`. The table reports 9.2. The discrepancy comes from the fact that the approximation `B ≈ W / (sqrt(2π)σ_eff)` is only valid in the large-W limit. The full CDF formula must be used. The text on p. 14 confirms the number is correct according to the author's code: "Using scipy.stats.norm with σeff = 0.833 reproduces BF ≈ 9.2".
*   **Fix:** The caption of Table II should explicitly state that the rebooked values are calculated using the full CDF integral (Eq. 9) and that simple `1/σ_eff` scaling is not accurate.

**P2-m4: Figure 2 Caption Complexity**
*   **Section/Page:** Figure 2 (p. 11)
*   **Problem:** The caption for Figure 2 is extremely dense and contains complex calculations within the text (e.g., "effective σeff ranges from √0.9^2 + 1.0^2 = 1.35..."). This makes the caption difficult to parse.
*   **Fix:** Move the calculations and detailed explanations of the different bars into the main body text. The caption should be a concise summary of what the figure shows, e.g., "Detection significance for fNL = -35/8 for SPHEREx and MegaMapper under different analysis assumptions. Bars correspond to: (a) naive uncorrected, (b) optimistic template-corrected, (c) realistic post-systematics envelope, and (d) conservative floor. See Sec. IV and VII for detailed definitions."

**P2-m5: Citation Formatting**
*   **Section/Page:** Bibliography (p. 28-29)
*   **Problem:** Several pre-print citations are missing journal information for papers that have been published for years. Ref [37] (Euclid Collaboration) is cited as A&A 697, A1 (2025), which is in the future. This should be `(in press)` or similar.
*   **Fix:** The author should perform a thorough pass on the bibliography to update arXiv pre-prints with their published journal references where available and correct any formatting issues.

**P2-m6: Data Availability Section**
*   **Section/Page:** Data and Code Availability (p. 25)
*   **Problem:** The section lists several python script names (e.g., `c8_fnl_running_fisher.py`, `c9g_bf_table_recompute.py`). While providing the code is excellent, the description of what each script does is minimal. The Zenodo DOI is mentioned as "(DOI inserted at submission)", which is standard practice but should be checked before publication.
*   **Fix:** Briefly expand the description for each named artifact/script. For example: "`c9g_bf_table_recompute.py`: script to reproduce the Bayesian comparison results in Table III, including GR-degradation." This improves usability for anyone trying to reproduce the work.

#### **NIT**

**P2-N1: Date Formatting**
*   **Section/Page:** Title page (p. 1)
*   **Problem:** The date is "June 28, 2026". This is in the future.
*   **Fix:** Change the date to the actual submission date.

**P2-N2: Minor Typo**
*   **Section/Page:** Sec. IX.D (p. 22)
*   **Problem:** "it is a new galaxy-covariance Fisher compu-tation". The hyphenation in "computation" is incorrect due to a line break.
*   **Fix:** Correct the typesetting.

**P2-N3: Redundant Phrasing**
*   **Section/Page:** Sec. X (p. 24)
*   **Problem:** "this realistic range being a scoping sensitivity envelope under the additive-quadrature heuristic systematic budget of §VII, not a joint-covariance forecasted measurement precision, with no full bispectrum joint Fisher over the systematic nuisances performed here" - this is a very long and slightly repetitive sentence.
*   **Fix:** Shorten and clarify. E.g., "This realistic range is a scoping envelope derived from a heuristic, additive-quadrature systematic budget (§VII), not a formal measurement precision from a joint-covariance Fisher analysis (which was not performed)."

---

### **Summary Recommendation**

**MAJOR REVISIONS**

This is a work of impressive detail and rigor. The author's careful treatment of the template mismatch and the resolution of the Cai/Li discrepancy are valuable contributions to the literature. The Bayesian analysis is also thorough. However, the manuscript in its current form is not suitable for publication in Physical Review D.

The primary issues are its excessive length and convoluted structure, which obscure the main contributions. The paper attempts to be both a sensitivity recast and a platform for a new, independent forecast (the SDB analysis), leading to a loss of focus. Furthermore, the abstract and main body must be more carefully aligned, particularly in qualifying the nature of the systematic budget and the basis-dependence of key numerical results.

I recommend that the paper be accepted only after major revisions addressing the points listed above, with a strong emphasis on restructuring and shortening the manuscript to present its core findings more clearly and concisely. The author has performed high-quality work, and a revised, more focused manuscript would be a strong candidate for publication.