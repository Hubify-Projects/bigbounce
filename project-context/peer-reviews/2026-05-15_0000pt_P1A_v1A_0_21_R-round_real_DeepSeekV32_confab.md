# P1A_v1A_0_21 R-round — REAL cross-vendor — DeepSeek-V3.2 confabulation-hunter

**Model**: `deepseek/deepseek-v3.2` (via OpenRouter)
**Round**: 2026-05-15_0000pt
**Wall time**: 38.3s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=23444, completion=1119, total=24563

---

## PAPER-DEE-B1
**BLOCKER** – Abstract, Conclusions, Sec. 13 (Surviving Tests)  
**Issue:** The headline claim `f_NL = -35/8` is presented as a mechanism-independent, parameter-free prediction of the “matter-bounce class.” However, the companion paper P2 v1.7.29 (referenced in the ROUND CONTEXT) has scoped this claim to the “scalar-only w=0 matter-bounce class” with an explicit assumption excluding fermion-bound contributions. P1A does not acknowledge this critical scoping, creating a major inconsistency. The claim’s provenance is unclear—there is no reference to a JSON/script/dataset that produces this exact number from first principles or from a reproducible calculation within the paper’s own framework.  
**Fix:** Explicitly align with P2’s scoping in the abstract, conclusions, and Sec. 13. Add a footnote or citation to P2 detailing the `f_NL = -35/8` derivation’s assumptions and provide a traceable source (e.g., a script in the reproducibility repository) that computes this value from the cubic action.

## PAPER-DEE-M1
**MAJOR** – Sec. 4.1 (Route 1 / NJL), Sec. 9 (Barrier 8)  
**Issue:** The paper incorrectly characterizes the Hehl-Datta torsion-induced four-fermion term as “parity-even” (Eq. 4, Table 2, Barrier 8 description). The canonical result `(¯ψ γ^a γ^5 ψ)^2` is a pseudoscalar (parity-odd) invariant. This mischaracterization undermines the parity-based amplitude-suppression argument for Route 1 and the logic of Barrier 8.  
**Fix:** Correct all references to the parity character of the NJL term to “parity-odd.” Re-evaluate the amplitude-suppression argument to ensure it does not rely on the erroneous parity-even claim.

## PAPER-DEE-M2
**MAJOR** – Sec. 4.2 (Route 2 / one-loop), Appendix B  
**Issue:** The dimensional handling of the parity-odd operator is inconsistent. The text states the operator has naive dimension `+1` (Appendix B) but earlier uses `(α/M) M_Pl^3` (dimension `+2`) and `[(α/M) M_Pl] M_Pl^4` (dimension `+4`) interchangeably. The one-loop suppression ratio `Δθ_one‑loop/Δθ_obs` in Sec. 4.2 is presented as a dimensionless number, but its derivation involves a dimensionally inconsistent combination of `H_0`, `M_Pl`, and `α/M`.  
**Fix:** Re-derive the one-loop suppression ratio with consistent dimensional analysis. Clarify in Appendix B the exact on-shell scaling that yields `ρ_Λ ∼ (α/M) M_Pl^3` vs. `ρ_Λ ∼ [(α/M) M_Pl] M_Pl^4` and justify the choice.

## PAPER-DEE-M3
**MAJOR** – Sec. 9 (Barrier Catalog), Abstract  
**Issue:** The paper claims “13 logically-independent mechanism-class constraints” but acknowledges that Barrier 8 is an observational consequence of the perturbation-transparency theorem (Barrier 14). Listing them separately “for historical mechanism-class completeness” is misleading and inflates the count. The abstract’s “13 barriers” and the barrier table’s 14 entries create confusion.  
**Fix:** Unambiguously state the number of independent barriers (13) and remove Barrier 8 from the table or demote it to a sub-item of Barrier 14. Update the abstract to reflect the correct count.

## PAPER-DEE-minor1
**minor** – Sec. 12.1 (Inflationary Suppression), Sec. 2.3  
**Issue:** The number `N_tot ≈ 92` is presented as a fitted parameter critical to the dark-energy scale, but its provenance is opaque. The derivation involves the prefactor `(T_reh/M_GUT)^(3/2)`, which the text admits is an order-of-magnitude estimate “not calculated from a thermal partition function.” There is no reference to a script or dataset that computes `92` from the input parameters.  
**Fix:** Provide a traceable calculation (e.g., a Python script in the reproducibility repository) that takes `α/M`, `T_reh`, `M_GUT`, and `ρ_Λ` as inputs and outputs `N_tot`. Clearly label the result as sensitive to the prefactor’s OOM uncertainty.

## PAPER-DEE-nit1
**nit** – Bibliography  
**Issue:** The ROUND CONTEXT instructs a “bib metadata audit for fused-arXiv-ID issues.” While no fused IDs are obvious in the provided bib entries (the sample text cuts off before the bibliography), the instruction should be explicitly acknowledged as performed.  
**Fix:** Add a brief note confirming the bibliography has been checked against the Shamir/Jia/CaiBrandenberger pattern and no fused IDs were found in P1A’s bib (as distinct from the prior catches in P4 and P2).
