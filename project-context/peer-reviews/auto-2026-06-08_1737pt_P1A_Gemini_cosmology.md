# P1A auto-2026-06-08_1737pt — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 128.7s

---

**Referee Report for PRD Manuscript**

**Manuscript ID:** [Assigned by user context: P1A]
**Title:** Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
**Author:** Houston Golden

This paper investigates four potential channels through which Einstein-Cartan-Holst (ECH) gravity could source late-time dark energy. It concludes that all four channels fail at the amplitude level, a result termed "channel-level closure." The central theoretical result is a "perturbation-transparency theorem," which states that for canonical scalar matter, the Holst sector is dynamically inert and decouples from scalar and tensor perturbations. The paper also discusses surviving, mechanism-independent predictions of a broader "bounce cosmology" class, namely a non-Gaussianity signature (`f_NL = -35/8`) and cosmic birefringence (`β ≈ 0.27°`).

While the perturbation-transparency theorem is a clear and potentially useful result, the main framework of the paper, which is the assessment of dark energy routes, is built on a foundation that is not physically consistent. The connection between the ECH sector and a late-time vacuum energy relies on a phenomenological ansatz involving an operator with an incorrect mass dimension. This fundamental flaw invalidates the primary narrative and conclusions of the paper regarding dark energy. Therefore, the manuscript in its current form is not suitable for publication in Physical Review D.

---
### Detailed Findings

#### ESSENTIAL

**P1A-E1: Fundamentally Flawed Dark Energy Ansatz (Sec. II A 2, Appendix B; Pages 6, 20)**
*   **Problem:** The entire connection between the ECH bounce and late-time dark energy rests on a "phenomenological on-shell scaling ansatz." The proposed parity-odd operator in Eq. (6) has an off-shell mass dimension of +1. As explicitly acknowledged in Appendix B, this is three units of mass short of the dimension +4 required for a term in a local Lagrangian density in 4D spacetime. The author's attempts to remedy this by labeling it an "on-shell scaling" or by suggesting the coefficient could be modified to `α M_Pl^3 / M` are not valid procedures in effective field theory. An operator's dimension is fundamental. Building a detailed analysis of dark energy on an operator that cannot be part of a local action renders the entire exercise physically meaningless.
*   **Required Fix:** This is a fatal flaw in the paper's central premise. All sections and conclusions that depend on this ansatz—including the calculation of `N_tot ≈ 92`, the inflationary suppression factor `D_inf`, the discussion of fine-tuning, and the "structural tension" in Sec. XIV D—must be removed. The paper cannot be published with this unphysical foundation.

**P1A-E2: Over-reliance on Unpublished Work (Throughout)**
*   **Problem:** The paper repeatedly cites manuscripts "in preparation" for crucial, load-bearing results. Examples include:
    *   [2] H. Golden, `f_NL = -35/8` Forecast... (The entire SPHEREx forecast for the key surviving prediction).
    *   [6] H. Golden, Cobaya MCMC + NaMaster... (All MCMC results, `ΔN_eff` constraints, and ALP parameter fitting).
    *   [23] H. Golden, Galaxy Chirality at Scale... (The observational null result for galaxy spin asymmetry).
    *   [46] H. Golden, Spectrally Unusual Sources... (NANOGrav model comparison).
*   **Required Fix:** A manuscript submitted to PRD must be self-contained or rely on publicly available work (published or on the arXiv). All claims and numerical results must be verifiable. The paper must be revised to derive these results internally or cite existing, accessible literature. Citing one's own future work for the paper's primary observational context is not acceptable.

**P1A-E3: Internal Contradiction on Torsion Survival (Sec. II C 1; Page 7)**
*   **Problem:** The paper's dark energy mechanism requires a bounce-era torsion signature to survive until today, albeit diluted by `D_inf`. However, the "Reheating thermal-reset barrier" paragraph on page 7 presents a compelling physical argument for why this cannot happen. It correctly states that torsion is algebraic and tracks the fermion axial current `J_5`. During reheating, the universe thermalizes, and any coherent `⟨J_5⟩` from the bounce is washed out, leading to `⟨Torsion⟩ ≈ 0`. This thermodynamic argument directly invalidates the premise of the `D_inf` calculation. The paper cannot simultaneously use this thermal-reset argument to support its "perturbation transparency" conclusion while ignoring that it falsifies its own dark energy mechanism.
*   **Required Fix:** This internal contradiction must be resolved. Given the strength of the thermal-reset argument, the logical conclusion is that the dark energy mechanism is non-viable for this reason as well, reinforcing the need to remove it from the manuscript.

#### MAJOR

**P1A-M1: Unclear Scope and Contribution (Abstract, Introduction; Pages 1, 3)**
*   **Problem:** The abstract and introduction are exceptionally dense with jargon (e.g., "channel-level amplitude closure," "amplitude-budget granularity") and fail to clearly state the paper's single, solid contribution. The main narrative is about closing dark energy routes, but this analysis is based on the flawed premise identified in P1A-E1. The truly valuable result—the perturbation-transparency theorem—is buried. The paper reads as a sweeping but unsupported framework rather than a focused theoretical result.
*   **Required Fix:** The paper should be completely restructured around the perturbation-transparency theorem (Sec. X). This result is clean, derivable, and has clear implications. A new, concise abstract and introduction should state this theorem as the main result, explain its proof, and discuss its implications (i.e., that ECH effects in scalar-driven cosmology are confined to non-perturbative channels or require new non-minimal couplings/matter). The flawed dark energy analysis should be removed. The recommended maximum page count for a paper focused on this single theorem would be 5-7 pages.

**P1A-M2: Misleading Presentation of "Surviving" Predictions (Abstract, Sec. XIII; Pages 1, 17)**
*   **Problem:** The paper presents `f_NL = -35/8` and `β ≈ 0.27°` as key "surviving" predictions. However, the text repeatedly clarifies that these are *not* predictions of the ECH model being studied but are generic to the "matter-bounce class" or "GR+ALP-class." This is confusing. The paper's main body is dedicated to showing ECH *fails* to produce observable signatures (in DE and perturbations), so highlighting these other predictions gives a misleading impression of the ECH model's viability.
*   **Required Fix:** The discussion of these predictions should be clearly separated from the ECH analysis. It should be stated upfront that the paper's ECH analysis yields null results, and that for context, other models in the broader bounce/ALP landscape *do* have testable predictions, which are then briefly described. The current framing conflates the two.

**P1A-M3: Hand-Waving Derivation of Suppression Factor (Sec. II C 1; Page 6-7)**
*   **Problem:** The derivation of the `(T_reh / M_GUT)^(3/2)` prefactor in Eq. (11) is justified on grounds of "dimensional-analysis aesthetic" and a "phenomenological phase-space ansatz." This is not a rigorous derivation. A first-principles calculation would require a proper matching of the operator between the GUT-scale and reheating-scale theories, including thermal effects, which the author admits has not been done.
*   **Required Fix:** This derivation is not sufficiently rigorous for PRD. As it is part of the flawed dark energy framework, it should be removed along with the rest of that analysis.

#### MINOR

**P1A-m1: Confusing Constraint Catalog (Sec. IX, Table II; Pages 12, 14)**
*   **Problem:** The abstract and text refer to "13 logically-independent" constraints but also to "14 historical catalog entries," because Barrier 8 is subsumed by Barrier 14. This is unnecessarily confusing.
*   **Required Fix:** The list should be presented simply as 13 independent constraints. Barrier 8 can be mentioned in the text as an observational consequence of the more fundamental Barrier 14, but it should not be listed as a separate item in the main catalog or count.

**P1A-m2: Inappropriate Future Dating (Page 1)**
*   **Problem:** The manuscript is dated "June 8, 2026 PDT." This is unconventional and unprofessional. It also creates bizarre inconsistencies with citations to papers from 2024 and 2025.
*   **Required Fix:** The date should be changed to the actual date of submission.

**P1A-m3: Inconsistent Sigma Values in Table I (Page 4)**
*   **Problem:** The footnote for the `f_NL` forecast in Table I states: "6.3-5σ realistic after full systematic budget... under Heinrich+2024 σ(fNL) ≈ 0.7". The calculation `f_NL / σ(f_NL) = (35/8) / 0.7 = 4.375 / 0.7 ≈ 6.25`. The range "3-5σ" is mentioned in the main text (Sec. VII), while "6.3-5σ" is in the footnote. This is inconsistent and the degradation from 6.25σ to 3-5σ is not fully justified with a calculation.
*   **Required Fix:** Provide a single, well-justified forecast range and show the calculation for the degradation due to systematics. As this relies on an unpublished work, this point is secondary to P1A-E2.

**P1A-m4: Figure 2 Caption (Page 5)**
*   **Problem:** The caption for Figure 2 correctly states that the scaling ansatz is "not derived from the ECH action." This is an admission of the fatal flaw.
*   **Required Fix:** This figure illustrates the unphysical nature of the dark energy mechanism and should be removed from the paper.

#### NIT

**P1A-N1: Footnote `a` Placement (Page 1)**
*   **Problem:** The footnote `a` at the end of the abstract begins "This Bianchi-identity vanishing is distinct from — and should". The sentence is cut off. The full text appears at the bottom of page 2.
*   **Required Fix:** This appears to be a typesetting error. The full footnote should appear on page 1, or the footnote on page 1 should be removed and the text on page 2 should be a regular footnote.

---
### Summary recommendation

**REJECT**

The manuscript is recommended for rejection. Its primary claim—to perform a "channel-level closure" of dark energy routes in ECH gravity—is based on a physically inconsistent and dimensionally incorrect ansatz. This fatal flaw invalidates the majority of the paper's analysis, including the central "structural tension" argument.

The paper does contain a valid and interesting result: the perturbation-transparency theorem for the Holst term in the presence of canonical scalar matter. This is a rigorous and useful finding. I strongly encourage the author to extract this theorem and its proof (currently in Sec. X), write a new, concise manuscript focused solely on this result and its implications, and submit it for publication. A short, focused paper on this topic would be a valuable contribution to the literature. The current manuscript, however, is unsalvageable due to its reliance on an unphysical premise.