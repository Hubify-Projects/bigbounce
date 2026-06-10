# P1A R27conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.55.pdf` md5=5dc099dc pages=25
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (2951 chars)
**Wall time**: 165.7s

---

**Referee Report for Physical Review D**

**Manuscript ID:** [Assigned by journal]
**Title:** Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Author:** Houston Golden

This paper presents a systematic assessment of four minimal Einstein-Cartan-Holst (ECH) channels as sources for late-time dark energy. The author concludes that all four channels fail at the amplitude or naturalness level under stated assumptions. The central results are a "perturbation-transparency" theorem for canonical scalar matter within ECH gravity and a catalog of 13 structural constraints that collectively close the enumerated dark-energy routes. The paper also discusses surviving, mechanism-independent predictions of the broader bouncing-cosmology paradigm, namely a specific non-Gaussianity signature (`f_NL = -35/8`) and cosmic birefringence from a spectator axion-like particle.

The paper contains two significant and valuable contributions. The perturbation-transparency theorem (Sec. X) is a clear and rigorous result, demonstrating that for canonical scalar matter, the Holst sector decouples from all scalar and tensor perturbation equations of motion. This cleanly separates standard GR-like perturbative observables from non-perturbative parity-odd channels where new physics could be tested. Secondly, the systematic catalog of constraints ("barriers") and the detailed closure arguments for the four routes (Sec. IV, IX) represent a thorough and useful contribution to the literature on ECH and bounce cosmology.

However, the manuscript suffers from a fundamental flaw in its theoretical framework concerning the generation of dark energy, along with several other issues that require substantial revision. The dark-energy mapping relies on a phenomenological operator with an off-shell mass dimension of +1, which violates the principles of local 4D effective field theory. While the author is transparent about this being an "ansatz," this does not make it physically tenable as presented. The paper must be significantly reframed to be acceptable for publication in Physical Review D.

Below is a detailed list of required revisions.

---

### ESSENTIAL Revisions

**P1A-E1: Fundamentally Unsound Operator (Sec. II A 2, Appendix B, p. 1, 6, 23)**
*   **Problem:** The entire dark-energy mechanism presented rests on the parity-odd operator in Eq. (6), which the author correctly identifies as having a naive mass dimension of +1. A local Lagrangian density in four dimensions must be constructed from operators of mass dimension +4. The "on-shell scaling ansatz" presented in Appendix B (`ρ_bounce ~ (α/M) M_Pl^3`) is an ad-hoc insertion of mass scales to fix the dimensionality of the final energy density, not a derivation. This procedure lacks physical justification and is inconsistent with the principles of effective field theory.
*   **Fix:** The paper cannot be published in its current form, where this operator is presented as a viable, albeit phenomenological, route to dark energy. The manuscript must be fundamentally reframed. The author should present this finding as a powerful no-go result: i.e., that attempts to generate a parity-odd vacuum energy term within this minimal framework lead to dimensionally inconsistent operators, highlighting the extreme difficulty of the task. The focus should shift entirely to the robust results: the perturbation-transparency theorem and the systematic closure of the *standard* routes. The dimension +1 operator should be presented as a failed attempt, not a central part of the framework.

**P1A-E2: Internal Review Artifacts (p. 2, 18)**
*   **Problem:** The manuscript contains comments that appear to be from the author's internal version control or review process. These are inappropriate for a journal submission.
    *   Page 2, footnote: "Earlier versions of this manuscript erroneously identified the two..."
    *   Page 18, footnote 4: "An earlier version of this manuscript misidentified the Holst dual contraction with the Pontryagin density."
*   **Fix:** Remove all such internal-facing comments from the manuscript. The paper should present the final, corrected arguments without referring to its own revision history.

**P1A-E3: Use of Future Dates and Pre-emptive Citations (p. 1, 3, 13)**
*   **Problem:** The paper is dated "June 10, 2026 PDT" and makes claims based on anticipated future results, such as "DESI 2024-2025 BAO results" (p. 3). While pre-prints on arXiv sometimes use future dates for conference proceedings, a submission to a peer-reviewed journal must be based on the state of knowledge and publicly available data at the time of submission.
*   **Fix:** The date must be corrected to the submission date. All claims and citations must be based on existing, publicly accessible work. If the DESI results are not yet public, the language must be changed to a forecast or hypothetical (e.g., "If future surveys like DESI were to find...").

---

### MAJOR Revisions

**P1A-M1: Weak Justification for Prefactor in Dilution Formula (Sec. II C 1, p. 7)**
*   **Problem:** In Eq. (11), the inflationary dilution factor `D_inf` includes a prefactor `(T_reh / M_GUT)^(3/2)`. The justification for the `3/2` power is described as a "dimensional-analysis aesthetic" and a "phenomenological phase-space ansatz." This is insufficient for a rigorous theoretical paper. While the exponential term dominates the fine-tuning, this prefactor is part of a central equation and its form should be physically derived or much more strongly motivated.
*   **Fix:** Provide a more rigorous derivation for this prefactor, perhaps from integrating a thermal fermion distribution against the relevant operator. If a full derivation is beyond the scope, the limitations of this ansatz must be discussed in greater detail, including how alternative powers would affect the conclusions.

**P1A-M2: Contradictory Figure Element (Fig. 1, p. 4)**
*   **Problem:** In Figure 1, the box for "Ekpyrotic" cosmology is confusing and contradictory. The arrow states "produces ECH; permitted," but the text below the box states "structurally closed (this paper)." This cannot be simultaneously true. The paper's main text does not provide a closure argument for the ekpyrotic scenario.
*   **Fix:** Correct the "Ekpyrotic" entry in Figure 1 to be unambiguous. If the paper does not close this channel, the "structurally closed" label must be removed. The relationship between Ekpyrosis and ECH should be clarified.

---

### MINOR Revisions

**P1A-m1: Awkward Phrasing of Constraint Count (Abstract, Intro, p. 1, 3)**
*   **Problem:** The paper repeatedly uses the convoluted phrase "14 constraints... 13 logically-independent with B8 subsumed by B14." This is confusing for the reader.
*   **Fix:** State clearly that there are 13 independent constraints. The fact that an older, heuristic argument (B8) is now superseded by a rigorous theorem (B14) can be explained once in the main text (Sec. IX) rather than being repeated in the abstract and introduction.

**P1A-m2: Unclear Footnote in Executive Summary Table (Table I, p. 4)**
*   **Problem:** In Table I, the footnote `†` attached to the `f_NL` forecast reads "Reparameterized as sensitivity to Ntot; not solved." This is cryptic. It is unclear what is "not solved."
*   **Fix:** Rewrite the footnote for clarity. Explain what is meant by this reparameterization and what problem remains unsolved.

**P1A-m3: Numerical Discrepancy in Forecast Significance (Sec. VII, p. 13)**
*   **Problem:** Footnote 3 on page 13 states that `f_NL = -4.375` with `σ(f_NL) ≈ 0.7-1.0` corresponds to a "3-5σ realistic" significance. The calculation yields `4.375/1.0 = 4.375σ` and `4.375/0.7 ≈ 6.25σ`. The range should be stated as `~4-6σ`.
*   **Fix:** Correct the stated significance range to reflect the numbers provided.

---

### NIT (Cosmetic)

**P1A-N1: Density of Text (Throughout)**
*   **Problem:** The paper is extremely dense, with long paragraphs and extensive use of parenthetical clauses. This can make it difficult to follow the main logical thread.
*   **Fix:** Consider breaking up some of the longest paragraphs. While not essential, improving the readability would strengthen the paper's impact.

---

## Summary recommendation

**MAJOR REVISIONS**

This manuscript in its current form is not acceptable for publication in Physical Review D due to its reliance on a dimensionally inconsistent operator at the core of its proposed dark-energy mechanism. However, the paper contains other results of significant value, most notably the perturbation-transparency theorem and the comprehensive catalog of constraints on minimal ECH models. These results are rigorous, well-presented, and worthy of publication.

Therefore, I recommend that the paper undergo major revisions. The author should reframe the manuscript to focus on the robust no-go theorems and the perturbation-transparency result. The dimensionally-flawed operator should be presented not as a viable ansatz, but as an illustration of the severe challenges facing ECH-based dark energy models. If the paper is revised to remove its reliance on this unsound theoretical construct and address the other points listed above, it would constitute a strong and valuable contribution to the field.

---

## PASS 2 — self-critique findings (what initial review missed)

Here are the additional findings from the second, more rigorous review.

================================================================
### ADDITIONAL FINDINGS (Second Pass)

**P1A-E4: Dimensional Inconsistency in PGT Coupling (Sec. IX A, p. 14)**
*   **Problem:** Equation (18), which underpins "Barrier 1: Mass-Coupling Lock," is dimensionally inconsistent as written. The effective coupling `g_eff` is presented as a dimensionless quantity, but the expression `1/(M_Pl t₃)` does not yield a dimensionless result based on the standard units for the quadratic-torsion coupling `t₃` in the PGT Lagrangian. The subsequent scaling argument `√t₃ ~ m_T⁻¹` also fails to resolve this.
*   **Fix:** The derivation of the mass-coupling lock for ultralight torsion must be revisited to ensure dimensional consistency. If the argument cannot be made dimensionally sound, Barrier 1 must be retracted, reducing the count of independent constraints.

**P1A-E5: Incorrect Cross-Reference in Abstract (p. 1)**
*   **Problem:** The abstract states that missing operators are acknowledged in "Sec. IV and Sec. XI." While Section IV does this correctly, Section XI discusses a "Hybrid Dark-Energy Loophole" and does not mention the missing operators (e.g., Jackiw-Pi term).
*   **Fix:** The reference to Section XI in the abstract must be removed or corrected.

---

**P1A-M3: Significant Underestimate of Forecast Significance (Sec. VII, p. 13)**
*   **Problem:** Footnote 3 on page 13 provides the inputs for the SPHEREx `f_NL` forecast: `f_NL = -4.375` and `σ(f_NL) ≈ 0.7-1.0`. The text then claims this corresponds to a "3-5σ realistic" significance. The actual calculation yields a range of `4.375/1.0 = 4.375σ` to `4.375/0.7 ≈ 6.25σ`. The paper's `3-5σ` range is a substantial underestimate of the constraining power of the test according to its own numbers.
*   **Fix:** Correct the significance range to `~4.4-6.3σ` (or similar, depending on the precise definition of the range) to accurately reflect the input values.

---

**P1A-m4: Flawed Explanation in Figure Caption (Fig. 3, p. 7)**
*   **Problem:** The caption for Figure 3 contains a dimensionally incorrect and confusing explanation for a numerical value. It states that a dimensionless ratio is obtained by "dividing by 3H₀² ≈ 2.1," which is nonsensical as `3H₀²` has units of `[mass]²`.
*   **Fix:** Remove the flawed explanation and provide a correct, dimensionally sound calculation for the claimed contribution of cosmic rotation to the energy density.

**P1A-m5: Stale Data in Figure (Fig. 1, p. 4)**
*   **Problem:** Figure 1 displays a value for the PTA spectral index (`γ = 3.20 ± 0.42`) that the main text (p. 18, Sec. G) explicitly identifies as an outdated value from a "pre-real-KDE draft," which has been superseded by a newer analysis (`γ = 2.567 ± 0.382`).
*   **Fix:** Update Figure 1 to use the final, correct value for the PTA measurement to ensure consistency with the main text.