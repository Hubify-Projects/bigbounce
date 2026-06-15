# P1A EXT18 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=f1eab008 pages=29
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 116.8s

---

**Referee Report**

**Paper:** Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter (Houston Golden)

**Journal target:** Physical Review D

**Findings**

**P1A-E1** (ESSENTIAL)  
**Section:** Abstract (p. 1) + Sec. I (p. 3) + Sec. XV (p. 24)  
The abstract states that “the four enumerated routes … are not proven to be a complete diffeomorphism-invariant operator basis” yet immediately claims “channel-level closure.” The body (Sec. I, p. 3) repeats that the result is conditional on 14 barriers and an on-shell scaling ansatz (Appendix B). The abstract omits the phrase “under the stated assumptions” that appears in every body summary. This is a direct violation of the abstract–body consistency requirement.

**P1A-E2** (ESSENTIAL)  
**Section:** Abstract (p. 1) + Sec. IV (pp. 10–13) + Sec. IX (pp. 16–19)  
The abstract presents \(f_{NL}=-35/8\) as “the surviving testable prediction.” Body text (Sec. XIII, p. 23 and Sec. XIV D, p. 24) explicitly states this is a *class-level* (scalar-only \(w=0\) matter bounce) result, not an ECH-specific prediction, and is “not a distinctive ECH prediction.” The abstract therefore reports a stronger claim than the calibrated body statement.

**P1A-E3** (ESSENTIAL)  
**Section:** Throughout (e.g., p. 2, p. 4, p. 6, p. 10, p. 22)  
The argument is not self-contained. At least 12 load-bearing numerical results, MCMC posteriors, and pipeline validations are imported from “Paper I(b) (in preparation) [6]” and “Paper II (in preparation) [2]”. A standalone reader cannot verify \(H_0=67.68\pm1.06\), \(\Delta N_{\rm eff}\approx0\), the 2.6–5\(\sigma\) forecasts, or the \(\sigma(f_{NL})\approx0.7\) Fisher number without those documents. This violates PRD’s requirement that the paper be independently readable.

**P1A-E4** (ESSENTIAL)  
**Section:** Sec. II C (p. 7) + Appendix B (referenced but not shown)  
The central mapping \(\rho_\Lambda=\Xi M_{\rm Pl}^4\) is introduced as a “phenomenological on-shell scaling ansatz, not a derivation.” All subsequent closure statements rest on this ansatz. The abstract and title present the closure as a structural result rather than an ansatz-dependent statement.

**P1A-M1** (MAJOR)  
**Section:** Sec. X (pp. 19–20)  
The “perturbation-transparency” theorem is the only first-principles result. It is proved only for canonical scalar matter on a torsion-free background. The paper acknowledges that the result fails once fermions or non-minimal couplings are restored. The title and abstract give the impression of a general result for “scalar matter” while the actual domain is far narrower.

**P1A-M2** (MAJOR)  
**Section:** Table II (p. 17) + Sec. IX  
Fourteen “barriers” are listed. Barriers 5, 6, 7, 9, 10, 11, 13 are either logical consequences of the ansatz or statements about the absence of mechanisms, not derived dynamical obstructions. The paper counts them as “logically independent structural constraints,” inflating the apparent rigor.

**P1A-M3** (MAJOR)  
**Section:** Fig. 1 (p. 5) + Sec. IV  
The figure caption and text label four routes as “structurally closed (this paper).” The body repeatedly qualifies that R1–R3 closures assume explicit scaling or naturalness arguments and that R4 is closed by a “naturalness/explanatory-deficit objection rather than an amplitude no-go.” The visual therefore overstates what has been proved.

**P1A-M4** (MAJOR)  
**Section:** Sec. XIV A (p. 23)  
The paper lists its own limitations (phenomenological \(\alpha/M\), simplified inflation epoch, incomplete bounce-to-inflation transition). These limitations are not reflected in the abstract or the strength of the conclusions.

**P1A-N1** (MINOR)  
**Section:** Header (p. 1)  
Dated “June 13, 2026” — a future date relative to any current submission. Cosmetic but indicates possible preprint versioning issues.

**P1A-N2** (MINOR)  
**Section:** Multiple figure captions (Figs. 3–6)  
Axis labels and units are present but several panels mix “this work” curves with external data without explicit legend entries for every data source.

**Summary recommendation**  
**REJECT**

The manuscript fails the minimum requirements for a PRD theory paper: it is not self-contained, the abstract systematically overstates the strength and scope of the results relative to the calibrated body statements, and the central “closure” claim rests on an explicit phenomenological ansatz that is never promoted to a derivation. The only rigorous new result (the perturbation-transparency theorem) is narrow and already heavily caveated. The 29-page length is disproportionate to the actual advance once the companion-paper dependencies and ansatz dependence are acknowledged. The paper would require a complete rewrite as a shorter, self-contained letter focused solely on the transparency result before it could be reconsidered.