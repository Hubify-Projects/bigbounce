# P1A R23conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.50.pdf` md5=6208734b pages=23
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 176.3s

---

**Referee Report for Manuscript [P1A]**
**Title:** Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Author:** Houston Golden

This paper presents two main results concerning Einstein-Cartan-Holst (ECH) gravity. The first is a "perturbation-transparency theorem," which states that for canonical scalar matter, the Holst sector decouples from scalar and tensor perturbations, leaving them identical to those in standard GR. The second is a claimed "channel-level closure" of four potential routes for ECH to source late-time dark energy.

The perturbation-transparency theorem is a clear, well-derived, and valuable result. The proof, based on the vanishing of torsion for a scalar source and the subsequent vanishing of the Holst term via the Bianchi identity, is elegant and correct. This is a publishable contribution.

However, the second part of the paper, concerning the closure of dark-energy routes, suffers from severe foundational issues. The entire dark-energy mechanism rests on a phenomenological "on-shell scaling ansatz" that is dimensionally inconsistent from the perspective of a standard local effective field theory. The paper acknowledges this in an appendix, but this weakness is so central that it undermines the primary claims about closing dark-energy channels. Furthermore, the paper presents a powerful, physical "thermal-reset" argument that independently closes the proposed dark-energy channel, yet this argument is not given prominence. Several quantitative arguments, particularly regarding the inflationary scaling of physical modes, are unclear and appear to be incorrect.

The paper requires major revisions to address these fundamental problems. The robust perturbation-transparency result should be the focus, while the speculative dark-energy analysis must be significantly re-scoped and its foundational weaknesses stated more prominently in the main text.

## Detailed Findings

### ESSENTIAL

**P1A-E1: Foundational Dimensional Inconsistency of the Proposed Dark-Energy Operator**
*   **Location:** Sec. II A 2 (p. 6), Fig. 2 (p. 5), Appendix B (p. 21)
*   **Problem:** The core parity-odd operator proposed to source dark energy, given in Eq. (6), leads to an action with mass dimension -3, not the required dimensionless quantity. The Lagrangian density `L_odd` is stated to have mass dimension +1. The action `S = ∫ d^4x L_odd` therefore has `[S] = +1 - 4 = -3`. Appendix B explicitly confirms the operator has off-shell mass dimension +1, "three units short of the required +4" for a Lagrangian density. The paper's resolution is to invoke a "phenomenological on-shell scaling ansatz" (Eq. B2), which is not a derivation and violates standard EFT principles.
*   **Fix:** The paper cannot be published with a central claim based on a dimensionally inconsistent action treated as a fundamental theory. The authors must:
    1.  Make it unequivocally clear in the abstract and introduction that the entire dark-energy analysis is a speculative, phenomenological exercise based on an operator that does not fit within a standard local EFT framework.
    2.  Revise the paper to heavily de-emphasize the "closure" claims, as they are predicated on this flawed starting point. The perturbation-transparency theorem should become the paper's primary result.

**P1A-E2: Incomplete and Erroneous Text**
*   **Location:** Abstract (p. 1), Sec. X Footnote 3 (p. 16), Page 2 Footnote
*   **Problem:**
    1.  The abstract contains a sentence fragment: "This Bianchi-identity vanishing is distinct from — and should".
    2.  The footnote on page 2 and footnote 3 on page 16 contain internal review history: "Earlier versions of this manuscript erroneously identified the two...". This is inappropriate for a final publication.
*   **Fix:**
    1.  Complete the sentence in the abstract.
    2.  Remove all references to "earlier versions" or other internal manuscript history. The footnote should state the physical distinction directly without referring to past errors.

**P1A-E3: Incorrect Inflationary Scaling Argument**
*   **Location:** Abstract (p. 1), Sec. XIV D (p. 20), Sec. I (p. 3)
*   **Problem:** The paper argues that `N_tot > 60` e-folds erases the matter-bounce `fNL` signal for SPHEREx-accessible modes. The quantitative justification given is that a comoving scale `k_SPHEREX` is pushed to a physical scale `k_phys ~ e^32 k_SPHEREX` at the bounce, where the exponent is derived from `N_tot - N_exit ≈ 32`. This scaling appears incorrect. The physical momentum of a comoving mode `k` evolves as `p(t) = k/a(t)`. The ratio of physical momentum at the bounce to that at CMB horizon exit (`N_exit` e-folds after the bounce) should be `p_bounce / p_exit = a_exit / a_bounce = e^(N_exit)`. The paper's use of `N_tot - N_exit` seems to refer to the number of e-folds *after* horizon exit, which determines how super-horizon the mode becomes, not its physical scale at the bounce.
*   **Fix:** The authors must re-derive this scaling argument from first principles. The current derivation is confusing and likely incorrect, undermining the "Structural Tension" claim, which is presented as a key result.

### MAJOR

**P1A-M1: Prominence of a Weak Argument Over a Strong One**
*   **Location:** Sec. VII (p. 7), Sec. XII A (p. 17)
*   **Problem:** The paper presents a compelling physical argument for the closure of the DE channel: the "Reheating thermal-reset barrier" (p. 7). Since torsion is algebraic and tracks the fermion axial current `<J^5>`, any coherent bounce-era torsion is erased when reheating creates a thermal, unpolarized plasma where `<J^5> = 0`. This is a robust, model-independent argument. However, the paper gives far more prominence to the complicated, model-dependent, and fine-tuning-sensitive bookkeeping involving `N_tot ≈ 92`.
*   **Fix:** The thermal-reset argument should be elevated to the primary argument for closing the DE channel. It is much more physically grounded and less dependent on the problematic dimensional ansatz. The `N_tot` discussion should be presented as a secondary, consistency-check argument, with its heavy dependence on the ansatz made clear.

**P1A-M2: Unclear Scope and Justification in Figure 1**
*   **Location:** Fig. 1 (p. 4)
*   **Problem:** The figure caption and diagram make strong, unsupported claims.
    1.  An arrow from "Ekpyrotic" to "ECH / torsion" is labeled "produces ECH". This is a non-trivial statement that requires a citation or derivation.
    2.  The "Ekpyrotic" mechanism is marked as "structurally closed (this paper)". It is not clear why this paper, which focuses on ECH, would be closing ekpyrotic models. This claim is outside the paper's stated scope and is not justified in the text.
*   **Fix:** Remove the "produces ECH" label unless it can be robustly justified and cited. Remove the "structurally closed" claim for the Ekpyrotic model, as it is not demonstrated in this work. The figure should focus only on the mechanisms and observables directly analyzed in the paper.

**P1A-M3: Overly Complicated and Potentially Redundant "Barrier" Catalog**
*   **Location:** Sec. IX (p. 12-15)
*   **Problem:** The paper introduces a catalog of 14 "barriers". While systematic, this section makes the paper unnecessarily long and difficult to read. Many of these barriers are either standard concepts in cosmology (e.g., attractor sensitivity, Liouville's theorem) or are direct consequences of the arguments made in Sec. IV.
*   **Fix:** Restructure the paper to remove Sec. IX as a standalone list. The relevant constraints should be integrated directly into the discussion of the four routes in Sec. IV where they apply. This would make the paper more concise and the line of argument clearer.

### MINOR

**P1A-N1: Inconsistent/Unconventional Notation**
*   **Location:** Abstract (p. 1), Sec. I (p. 3)
*   **Problem:** The notation `ΥΒΙ/(ΥΒΙ + 1)` is used for a coefficient. `Υ` is typically the Immirzi parameter `γ`. The subscript `BI` is not standard (perhaps Barbero-Immirzi?). The use of `V` in `VB1` on page 3 appears to be a typo.
*   **Fix:** Clarify the notation. If it is simply the Immirzi parameter `γ`, use the standard symbol. Define the subscript `BI`.

**P1A-N2: Poorly Phrased Question in Summary Table**
*   **Location:** Table I (p. 4)
*   **Problem:** The question "Ho/08 tension resolution?" is unclear. It is likely a typo for `H_0` or `S_8`. The result given (`H_0=67.68±1.06`) is consistent with Planck, so it does not "resolve" the `H_0` tension with SH0ES; it "recovers ΛCDM", as the table states.
*   **Fix:** Rephrase the question for clarity, e.g., "Impact on cosmological tensions?".

**P1A-N3: Sloppy Notation in Action Principle**
*   **Location:** Eq. (5) (p. 6)
*   **Problem:** The form-language action in Eq. (5) uses sloppy notation. `€IJK` appears to be the Levi-Civita symbol, not a form, and the indices do not seem to balance correctly for a 4-form integrand.
*   **Fix:** Rewrite the equation using standard differential form notation to ensure it represents a well-defined 4-form to be integrated over spacetime.

### NIT

**P1A-T1: OCR Error in Density Unit**
*   **Location:** Sec. I (p. 3)
*   **Problem:** The text reads `pcrit ~ 0.27-0.41 pp1`. This is likely an OCR error for `ρ_pl` (Planck density).
*   **Fix:** Correct `pp1` to `ρ_pl`.

## Summary recommendation

**MAJOR REVISIONS**

The manuscript in its current form is not acceptable for publication in Physical Review D. It contains a valuable and well-supported result—the perturbation-transparency theorem for ECH gravity with scalar matter. However, this is combined with a highly speculative and foundationally flawed analysis of dark energy. The proposed dark-energy mechanism relies on a dimensionally inconsistent operator, which is a critical failure from an EFT perspective. Before the paper can be reconsidered, the authors must perform a major restructuring. The focus should be shifted to the robust perturbation-transparency result. The dark-energy analysis must be presented with full transparency about its phenomenological and dimensionally problematic nature, and the stronger physical "thermal-reset" argument should be given precedence over the complex and model-dependent `N_tot` bookkeeping. The numerous other issues detailed above, including the incorrect scaling argument and inappropriate manuscript-history remarks, must also be thoroughly addressed.