# P1A auto-2026-06-08_2353pt — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 124.1s

---

**Referee Report**

**Paper:** Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter (Houston Golden)

**Journal target:** Physical Review D

I have examined every page, equation, table, figure, footnote, and reference in the rendered PDF. Below is a complete, unsoftened audit.

### ESSENTIAL findings (paper cannot be accepted without fixes)

**P1A-E1** (Abstract, p. 1; Sec. I, p. 3)  
The abstract states that the four routes “each fails at the amplitude level” and that the central result is a “perturbation-transparency theorem.” The body immediately qualifies both claims with “under stated assumptions,” “phenomenological on-shell scaling ansatz” (not a derivation), and “channel-level” rather than operator-level closure. The abstract does not contain these qualifiers.  
**Required fix:** Rewrite the abstract to state exactly what is proven under which ansatz; remove the word “theorem.”

**P1A-E2** (Abstract, p. 1; Sec. XIII, p. 18; Sec. XV, p. 19)  
The two “surviving” predictions advertised in the abstract (\(f_{NL}=-35/8\) and \(\beta\approx0.27^\circ\)) are explicitly stated in the body to be *not* predictions of ECH. \(f_{NL}\) is a property of the scalar-only matter-bounce class; \(\beta\) is a benchmark consistency point. The abstract presents them as if they are outputs of the present work.  
**Required fix:** Remove both numbers from the abstract or add an explicit sentence that neither is derived from the ECH framework.

**P1A-E3** (Sec. II C 2, p. 6; Appendix B, p. 20)  
The mass dimension of the parity-odd operator is assigned \(+1\) via an on-shell scaling ansatz whose only justification is “we treat this scaling explicitly as an ansatz, not a derivation.” All 13 “logically independent barriers” and the perturbation-transparency result rest on this assignment. No derivation or matching calculation is supplied.  
**Required fix:** Either derive the dimension from the action or relabel the entire barrier catalog as conditional on an unproven ansatz.

**P1A-E4** (Sec. IV, pp. 8–11; Table II, p. 14)  
The four-route “no-go” is performed at channel level after omitting the Jackiw–Pi term and the parity-odd four-fermion partner of Route 1. The paper states these operators are “not separately enumerated.” A complete operator-basis closure is therefore not demonstrated; the title and abstract nevertheless use the word “closure.”  
**Required fix:** Change title and all “closure” language to “partial channel-level exclusion under the listed omissions.”

**P1A-E5** (References throughout; e.g., [2], [6], [23])  
Multiple load-bearing results are cited to “companion works in preparation.” The \(f_{NL}\) forecast, the ALP MCMC, the galaxy-spin null result, and the \(\Delta N_{\rm eff}\) chains are all external. A standalone PRD paper cannot rest its central claims on unpublished manuscripts.  
**Required fix:** All cited numbers must either be derived in the present manuscript or removed.

### MAJOR findings

**P1A-M1** (Length)  
23 pages for a channel-exclusion argument that ultimately concludes the mechanism does not work and that the advertised observables are independent of it. PRD standard for a negative result of this type is substantially shorter. Recommended maximum: 12–14 pages.

**P1A-M2** (Sec. X, pp. 15–16)  
The “perturbation-transparency result” is shown only for canonical scalar matter with vanishing spin density and after setting \(T=0\). The proof is five lines long and uses the algebraic Bianchi identity. This is presented as a major theorem yet is a direct consequence of the assumptions already used to define the minimal framework. Over-claiming of novelty.

**P1A-M3** (Fig. 3, p. 13; Sec. XIV D, p. 19)  
The “structural tension” plot and the claim that \(N_{\rm tot}\approx92\) is “definitively erased” by \(N_{\rm tot}\gtrsim60\) rely on the same un-derived on-shell ansatz (E3). The figure is therefore not an independent result.

**P1A-M4** (Sec. I, p. 3; Sec. IV E, p. 11)  
The paper repeatedly states that it does *not* claim a full diffeomorphism-invariant operator basis. Yet the abstract and title are written in the language of closure. This internal contradiction must be resolved at the level of title and abstract.

### MINOR findings

**P1A-m1** (Table I, p. 4)  
Row “Testable prediction” lists \(f_{NL}=-35/8\) with footnote “class-level.” The table does not state that this is external to ECH.

**P1A-m2** (Footnote a, p. 2)  
The long footnote distinguishing the Bianchi identity from the Pontryagin density is necessary because an earlier version of the manuscript made exactly that error. The existence of the footnote is evidence of prior sloppiness.

**P1A-m3** (Fig. 1, p. 4)  
The diagram labels four routes “structurally closed (this paper)” while the text states that R1–R4 are closed only after additional omissions. Caption and figure are inconsistent.

### NITs

- Multiple instances of “in preparation” citations that should be removed or replaced.
- Over-use of the word “logically independent” for a list of 14 barriers that are not shown to be independent under any formal criterion.
- Inconsistent capitalization of “Holst” vs “holst.”

### Summary recommendation

**REJECT**

The manuscript does not deliver a self-contained, rigorous no-go theorem. Its central claims rest on (i) an explicit phenomenological ansatz for operator dimension that is never derived, (ii) a channel-level enumeration that omits known operators, and (iii) multiple key numerical results that are deferred to unpublished companion papers. The abstract misrepresents the status of the two “surviving” observables. These are not cosmetic issues; they are foundational. The paper would require a complete rewrite, removal of all external citations, and a properly derived operator dimension before it could be reconsidered at PRD standards.