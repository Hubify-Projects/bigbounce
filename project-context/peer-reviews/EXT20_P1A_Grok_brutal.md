# P1A EXT20 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=198cb994 pages=29
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 102.2s

---

**Referee Report for PRD**

**Manuscript:** Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter  
**Author:** Houston Golden  
**Date of report:** current

### ESSENTIAL findings (paper cannot be accepted without fixes)

**P1A-E1** (Title page, p. 1)  
Offending text: “(Dated: June 18, 2026)”.  
Problem: A submission date in the future is an internal artifact that should never appear in a journal manuscript.  
Required fix: Remove entirely.

**P1A-E2** (Abstract + Sec. I, IV, IX, X, XV; multiple pages)  
Offending text: Repeated citations to “Paper I(b) (in preparation) [6]”, “Paper II (in preparation) [2]”, “companion paper”, and statements that “MCMC verification … are documented separately (in preparation) [6]”.  
Problem: Load-bearing numerical results (posteriors, \(\Delta N_{\rm eff}\), \(\sigma(f_{\rm NL})\), \(\beta\) constraints, \(H_0\) values quoted in Table I and the abstract) are imported from documents that do not exist for a standalone reader. This violates PRD’s requirement that the argument be self-contained.  
Required fix: Either make the manuscript self-contained or withdraw it until the companion papers are public and citable with fixed arXiv numbers.

**P1A-E3** (Abstract, p. 1)  
Offending claim: “the four enumerated routes … are not proven to be a complete diffeomorphism-invariant operator basis … we acknowledge missing operators”.  
Problem: The abstract simultaneously asserts “channel-level closure” while admitting the enumeration is incomplete. The body never quantifies how many operators are omitted or demonstrates that the omitted operators cannot source the claimed signals.  
Required fix: Either prove completeness at the operator level or remove the word “closure” from the title and abstract.

**P1A-E4** (Abstract + Sec. X, p. 19)  
Offending claim: “the Holst dual contraction \(\epsilon^{\mu\nu\rho\sigma}R_{\mu\nu\rho\sigma}\) vanishes identically on the Levi-Civita connection (\(T=0\)) by the first (algebraic) Bianchi identity”.  
Problem: The Bianchi identity \(R_{[\mu\nu\rho]\sigma}=0\) holds for any torsion-free connection, but the paper presents it as a novel “perturbation-transparency result” specific to minimal ECH. No comparison is made to the existing literature on Holst-term decoupling in scalar-tensor perturbations.  
Required fix: Provide an explicit literature comparison or retract the claim of novelty.

**P1A-E5** (Table I + abstract)  
Offending entry: “\(f_{\rm NL}=-35/8\) (Paper II forecast\(^b\)) … Yes, class-level\(^c\)”.  
Problem: The numerical value \(-35/8\) and the associated Fisher forecast are never derived in the present manuscript; they are imported from an unpublished companion. The abstract presents this number as a “surviving testable prediction”.  
Required fix: Derive the number inside this paper or remove it from the abstract.

### MAJOR findings

**P1A-M1** (Sec. IV, pp. 11–14)  
All four “no-go” arguments rely on amplitude-budget comparisons that assume specific on-shell mass-dimension assignments (Appendix B) that are explicitly labeled “ansatz, not a derivation”. The paper never shows that relaxing the ansatz re-opens any route.  
Required fix: Either promote the scaling to a controlled EFT argument or state that the closures are ansatz-dependent.

**P1A-M2** (Sec. IX, Table II, p. 17)  
Fourteen “barriers” are listed; Barrier 8 (parity-even interaction) and Barrier 14 (perturbation transparency) are presented as independent when both ultimately trace to the same Bianchi-identity argument in Sec. X. This double-counting inflates the apparent number of logically independent constraints.  
Required fix: Merge or clearly label dependent barriers.

**P1A-M3** (Fig. 1 + caption, p. 5)  
The figure claims to show “structurally closed (this paper)” routes with dashed red lines, yet the caption and body admit that the closures are conditional on the scaling ansatz of Appendix B. The visual presentation is therefore misleading.  
Required fix: Add explicit “under ansatz X” labels on every closure arrow.

**P1A-M4** (Sec. V, p. 15)  
Galaxy-spin analysis is described as “confirmed null” on the basis of a DESI Legacy DR8 reanalysis whose details are deferred to “Paper IV [23]”. No quantitative dipole amplitude or significance is recomputed in the present text.  
Required fix: Provide the actual measured dipole value and its uncertainty inside this manuscript.

### MINOR findings

**P1A-m1** (Eq. 2, p. 6)  
\(\gamma_{\rm SU(2)}\approx0.274\) is adopted without propagating the scheme dependence discussed in the surrounding paragraph (\(\gamma_{\rm U(1)}\approx0.127\), DLM value 0.2375). The \(\pm0.037\) range is mentioned only in a footnote and never used in subsequent error budgets.

**P1A-m2** (Eq. 11, p. 8)  
The factor \((T_{\rm reh}/M_{\rm GUT})^{3/2}\) is introduced as a “matching coefficient” but is never derived from a first-principles reheating calculation; it is an order-of-magnitude placeholder.

**P1A-m3** (p. 2, PACS numbers)  
PACS 98.80.-k, 04.50.Kd, 04.60.Pp, 95.36.+x are listed, yet the paper contains no loop-quantum-gravity calculation that would justify 04.60.Pp.

### NIT findings

**P1A-N1** Multiple instances of “(in preparation)” and bracketed citation numbers that point to non-existent references.

**P1A-N2** Inconsistent use of “ECH” vs. “minimal-ECH” without a one-sentence definition on first use in the abstract.

**P1A-N3** Figure 5 bottom panel mixes “fine-tuning score” (orders of magnitude) with an arrow labeled “\(10^5\) residual (CC problem reparameterized, not solved)”. The arrow is not explained in the caption.

## Summary recommendation

**REJECT**

The manuscript is not a standalone, self-contained piece of research. Its central quantitative claims rest on unpublished companion papers, the abstract asserts “closure” while the body repeatedly disclaims completeness, and the manuscript carries an impossible future date. Until the work is made fully self-contained, the claimed closures are shown to be robust to the stated ansatz, and every load-bearing number is derived inside the present text, the paper does not meet PRD standards.