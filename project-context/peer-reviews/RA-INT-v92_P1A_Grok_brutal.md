# P1A RA-INT-v92 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=7488bd1c pages=36
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 89.2s

---

**Referee Report**

**Paper:** Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter (Houston Golden)

**Journal target:** Physical Review D

**Date of report:** (current)

I have examined every page, equation, table, figure, and caption in the rendered PDF. The following findings are exhaustive.

### ESSENTIAL findings (paper cannot be accepted without fixes)

**P1A-E1** (Abstract, p. 1; Sec. I, p. 3)  
The abstract states quantitative results (e.g., “the central result is a perturbation-transparency result”, “four enumerated routes … are amplitude-suppressed”) while the body repeatedly qualifies every quantitative claim as conditional on an on-shell scaling ansatz whose off-shell mass dimension is +1 rather than +4 (explicitly admitted in Sec. II C and Appendix B). No abstract sentence carries the required caveat.  
**Required fix:** Rewrite abstract to state only what is actually proved at the stated level of rigor; remove all numerical suppression factors unless they are derived without the ansatz.

**P1A-E2** (entire manuscript; especially Secs. IV, IX, X, Table III)  
The paper is not self-contained. Every load-bearing numerical result (MCMC posteriors, Fisher forecasts, \(\sigma(f_{NL})\), birefringence amplitudes, \(\Delta N_{\rm eff}\)) is imported from “Paper I(b)”, “Paper II”, or works “in preparation” [2,6]. The standalone-reader test fails for any reader who cannot access the companions. PRD requires a complete argument within one manuscript.  
**Required fix:** Either absorb all necessary derivations or remove all quantitative claims that depend on unpublished material.

**P1A-E3** (p. 1, “Dated: June 30, 2026”)  
A submission date in the future is present in the rendered PDF. This is an internal artifact indicating the manuscript is not finalized.  
**Required fix:** Remove or correct the date.

**P1A-E4** (Sec. II C, Eq. (6); Appendix B)  
The parity-odd operator is assigned an off-shell mass dimension +1 and promoted to a “phenomenological on-shell scaling ansatz.” All four route closures and the perturbation-transparency claim rest on this ansatz. No derivation from the ECH action is provided. This is not an EFT result.  
**Required fix:** Either derive the operator with correct dimension or reclassify the entire work as an exploratory ansatz study.

**P1A-E5** (Sec. X, Eqs. (21)–(23); Bianchi-identity argument)  
The “perturbation-transparency” theorem reduces to the algebraic Bianchi identity \(R_{\mu[\nu\rho\sigma]}=0\) on a torsion-free connection (\(T=0\)). This is textbook and holds for any torsion-free theory; the paper presents it as a novel ECH-specific result. The distinction from the Pontryagin term is noted but does not salvage novelty.  
**Required fix:** Remove all language claiming a new theorem; cite the standard identity.

### MAJOR findings

**P1A-M1** (Sec. IV, Table III)  
All four “no-go” closures are order-of-magnitude amplitude estimates (factors of \(10^{-60}\), \(10^{-70}\), etc.) obtained by plugging Planck-scale numbers into the ansatz. No explicit loop calculation or renormalization-group flow is performed. These are not rigorous exclusions.

**P1A-M2** (Sec. IX, Table IV; 14 “barriers”)  
The 14 mechanism-class constraints mix genuine dynamical obstructions with generic naturalness or classification arguments that apply to any modified-gravity model. Several (B5, B6, B7, B9, B13) are not ECH-specific. The catalog therefore overstates the paper’s novelty.

**P1A-M3** (Fig. 1, Table I)  
Figure 1 and Table I present a “bounce-mechanism → observable-prediction map” whose arrows rely on the same ansatz and on companion MCMC chains. The figure is not self-contained and the numerical entries cannot be recomputed from the displayed material.

**P1A-M4** (Sec. XIII, “surviving ECH-independent class tests”)  
The two “surviving” predictions (\(f_{NL}=-35/8\) and spectator-ALP \(\beta\approx0.27^\circ\)) are explicitly stated to be properties of the broader matter-bounce class or of any GR+ALP setup. They are therefore not predictions of the ECH framework. Advertising them as ECH tests is misleading.

**P1A-M5** (length)  
The manuscript is 36 pages for a channel-level ansatz study whose central theorem is standard. PRD typically expects \(\leq20\) pages for such a scope.

### MINOR / NIT findings (selected)

**P1A-m1** (p. 2, “PACS numbers: … 95.36.+x”) — outdated PACS; use Physics Subject Headings.  
**P1A-m2** (Eq. (2)) — \(\gamma_{\rm SU(2)}\approx0.274\) is scheme-dependent; the paper acknowledges this but still uses it as a fixed input.  
**P1A-m3** (multiple locations) — repeated use of “in preparation [2,6]” as load-bearing citations violates PRD citation policy for unpublished work.

### Summary recommendation

**REJECT**

The manuscript fails the most basic PRD requirements: it is not self-contained, its central quantitative claims rest on an admitted phenomenological ansatz rather than a derivation, its headline “theorem” is a textbook identity, and the submission contains an impossible future date. Even after removing the date and companions, the remaining content would be a short exploratory note, not a 36-page PRD article. The work does not meet the journal’s standards for rigor or completeness.