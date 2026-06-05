# P1A auto-2026-06-05_1617pt — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 61.7s

---

**Referee Report for P1A (Physical Review D)**

**P1A-E1 (ESSENTIAL)**  
Section I, p. 3 (lead paragraph after title block): “the 14 constraints … close those routes at amplitude-budget granularity.”  
The paper repeatedly states it performs only a *channel-level* (amplitude-budget) closure under “stated assumptions,” explicitly disclaims a full operator-level partition of the parity-odd sector, and defers the Jackiw–Pi term and the parity-odd four-fermion partner of Route 1 to “a follow-up operator-level analysis.” A PRD paper cannot claim “closure” while simultaneously declaring the calculation incomplete. Required fix: either remove the word “closure” from the title/abstract/lead paragraphs or supply the missing operator-level calculation.

**P1A-E2 (ESSENTIAL)**  
Appendix B, p. 19, Eq. (B1) and surrounding text: the leading parity-odd operator is assigned off-shell mass dimension +1 and is promoted to a Planck-scale mapping only via an on-shell “scaling ansatz.” The paper itself labels this “not a derivation.” A dimensionally inconsistent operator cannot be the foundation of a no-go theorem that is advertised as rigorous. Required fix: either derive a dimension-4 operator or retract the claim that the four routes are closed inside a controlled EFT.

**P1A-E3 (ESSENTIAL)**  
Abstract-level claims (title page and p. 3) quote \(f_{\rm NL}=-35/8\) and \(\beta\approx0.27^\circ\) as “surviving predictions.” Both numbers originate from the *matter-bounce* class (scalar-only \(w=0\) contraction) or from a spectator ALP, respectively; the text explicitly states they are “not derived from the ECH action” and survive only because they are mechanism-independent. A reader cannot trace either number to an ECH calculation performed in this manuscript. Required fix: remove both numbers from any summary paragraph or demonstrate an explicit ECH derivation.

**P1A-E4 (ESSENTIAL)**  
Section IV and Table II, p. 13: the 14 “logically independent” barriers include Barrier 8 (parity-even interaction) and Barrier 14 (perturbation transparency). Both are direct consequences of the same torsion-elimination map already used for Barriers 1–7. The counting therefore double-counts the same algebraic step. The claim of 13–14 independent constraints is false.

**P1A-M1 (MAJOR)**  
The manuscript is 21 pages long (plus two companion papers “in preparation”). The actual new result is a set of amplitude-level no-go arguments plus one perturbative transparency theorem. PRD length guidelines are routinely violated by papers whose core contribution fits in <12 pages. Required fix: condense to a focused Letter or Short Article or justify the length with a complete operator-level calculation.

**P1A-M2 (MAJOR)**  
All numerical forecasts (\(\sigma(f_{\rm NL})\approx0.7\), LiteBIRD \(\sigma(\beta)\approx0.03^\circ\), SPHEREx \(k\)-range mapping) are taken from external Fisher matrices or from companion Paper II. The present text performs no independent forecast. A methods paper cannot advertise quantitative observational reach without performing or reproducing the forecast.

**P1A-M3 (MAJOR)**  
Figure 1 (p. 4) draws a red dashed “structurally closed (this paper)” box around the ECH/torsion node while the caption and text simultaneously state that Route 4 remains open at the operator level. The figure is therefore misleading.

**P1A-M4 (MAJOR)**  
The paper cites >20 “in preparation” or “companion” works for MCMC chains, NaMaster validation, ALP fitting, and the full operator basis. A standalone PRD article must be self-contained; dependence on unpublished manuscripts violates PRD policy on reproducibility.

**P1A-N1 (MINOR)**  
Page 2 date stamp “Dated: June 2, 2026 PDT” is a future date relative to any plausible submission. Cosmetic only, but indicates version-control sloppiness.

**P1A-N2 (MINOR)**  
Multiple instances of “we do not claim a full operator-basis closure” appear verbatim in the abstract, introduction, and conclusion. Repetitive hedging language should be consolidated.

**P1A-NIT1**  
Table I caption contains a footnote marker “b” whose text is split across two lines with an awkward line break; purely typographic.

**Summary recommendation**  
REJECT

The manuscript advertises a “channel-level closure” of four dark-energy routes inside minimal ECH gravity, yet (i) the central operator is dimensionally invalid and treated as an ansatz, (ii) the advertised numerical predictions are not derived from the ECH sector, (iii) the counting of “14 independent barriers” double-counts the same algebraic step, and (iv) the work is explicitly incomplete, delegating the actual operator-level calculation and all observational forecasts to unpublished companion papers. These defects are fatal for a PRD article. A drastically shortened, self-contained no-go note that removes all quantitative forecasts and correctly labels its scope as “amplitude-level obstructions under a phenomenological scaling ansatz” might be reconsiderable, but the present manuscript does not meet that standard.