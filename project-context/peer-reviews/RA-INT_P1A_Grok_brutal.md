# P1A RA-INT — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=b5197dc0 pages=32
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 82.3s

---

**Referee Report (Adversarial Review — PRD Standards)**

**P1A-E1 (ESSENTIAL, Sec. I/p. 3–4 and throughout)**  
The paper is not a standalone document. Load-bearing numerical results (MCMC posteriors for \(H_0\), \(\Delta N_\text{eff}\), \(\sigma_8\), \(\beta_\text{obs}\), Fisher forecasts for \(f_\text{NL}\), NaMaster pipeline validation) are repeatedly imported from “Paper I(b)”, “Paper II”, and works “in preparation [6]”. Examples: p. 2 (“ACDM+\(\Delta N_\text{eff}\) MCMC verification… documented separately”), Table II, p. 15 (LiteBIRD forecast), and the entire Sec. XIII. A reader cannot audit the central claims without those unavailable manuscripts. Required fix: all quantitative results must be either reproduced or removed; the paper must stand alone.

**P1A-E2 (ESSENTIAL, Abstract-equivalent text on p. 1 and Sec. X)**  
Abstract-level claim (“the central result is a perturbation-transparency result… Holst sector therefore decouples from all scalar/tensor perturbation equations”) is materially stronger than the body. The result is explicitly restricted to “canonical scalar matter” excluding fermions, propagating torsion, Immirzi field, non-minimal sectors, and boundary terms (explicitly stated p. 2 and Sec. X.A). The abstract sentence does not carry these scope limitations. Required fix: rewrite the lead claim to match the calibrated body statement exactly.

**P1A-E3 (ESSENTIAL, p. 1, 11–14 and Sec. IV)**  
Title and Sec. IV claim “Channel-Level Closure of Four Minimal… Routes.” The text immediately qualifies that this is not an operator-level closure, omits the Jackiw–Pi term and the parity-odd four-fermion partner of R1, and treats the parity-odd operator mass dimension as an ansatz rather than a derivation (p. 2, Appendix B). The title therefore overstates the result. Required fix: retitle to reflect the actual limited scope.

**P1A-E4 (ESSENTIAL, p. 3–4, Table II, Sec. III.A)**  
Multiple \(\beta\) measurements (WMAP+Planck \(0.342^\circ\pm0.094^\circ\), ACT DR6 \(0.215^\circ\pm0.074^\circ\)) are presented side-by-side without the explicit qualifier “not directly comparable” at every juxtaposition. The paper itself notes different null procedures and masks. This violates the explicit instruction on non-comparable sigmas.

**P1A-M1 (MAJOR, p. 2 and Appendix B)**  
The parity-odd operator (Eq. 6) is assigned off-shell mass dimension +1 instead of the required +4. The paper repeatedly labels this an “ansatz, not a derivation.” All amplitude-budget closures and the \(\rho_\Lambda\) identification rest on this ansatz. The no-go conclusions are therefore conditional on an unproven scaling assumption whose violation would reopen the channels.

**P1A-M2 (MAJOR, p. 1–2, 24–25)**  
Paper length is ~32 pages (per metadata) for a purely negative result (“all four routes closed at channel level”) whose positive content is two class-level predictions already known to be ECH-independent (\(f_\text{NL}=-35/8\) and spectator-ALP birefringence). PRD expects substantially tighter presentation for such scope.

**P1A-M3 (MAJOR, Sec. IX, Table III)**  
Fourteen “barriers” are listed, yet the text acknowledges that several (B5, B6, B7, B9, B13) are general naturalness or equilibrium arguments that apply to any bounce model, not ECH-specific. The catalog therefore inflates the appearance of ECH-specific obstructions.

**P1A-M4 (MAJOR, p. 15 and Sec. IV.D)**  
Route 4 is closed by a “naturalness/explanatory-deficit objection” rather than an amplitude mismatch. This is an aesthetic criterion, not a dynamical no-go, and is inconsistent with the amplitude-budget standard applied to R1–R3.

**P1A-N1 (NIT, p. 1)**  
Future date “(Dated: June 28, 2026)” appears in the header. Cosmetic.

**P1A-N2 (NIT)**  
Minor typographic duplication risk (“canonical canonical-mask” style) not observed in the rendered text, but the repeated phrase “not a derivation” appears in nearly identical wording on p. 2, 7, 13, 14.

**Additional audit notes**  
- All \(\sigma\) claims for \(f_\text{NL}\) (2.6–5\(\sigma\)) are imported from Paper II; no internal recomputation possible.  
- Figure 1 and Table III are useful but the “structurally closed” red dashed lines rely on the same ansatz flagged in E1/M1.  
- Bibliography entries for companion works lack arXiv IDs or DOIs, preventing traceability.  
- No duplicate phrases or internal review tags (“R7”, superseded, etc.) were found in the rendered PDF.

## Summary recommendation  
**REJECT**

The manuscript cannot be evaluated under PRD standards because it is not self-contained, its headline claims exceed the documented scope and rest on an explicit phenomenological ansatz rather than derivation, and multiple quantitative results are imported from unavailable “in-preparation” companions. Even after those issues are hypothetically cured, the remaining contribution is a lengthy catalog of conditional no-gos whose positive predictions are already known to be mechanism-independent. The paper should be condensed to a short letter or withdrawn.