# P1A auto-2026-06-09_1042pt — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 80.4s

---

**Referee Report**

**Paper:** Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter (Houston Golden)

**Journal:** Physical Review D

**Finding classification key**  
- ESSENTIAL: fatal to acceptance in present form  
- MAJOR: requires substantial revision  
- MINOR: must be addressed  
- NIT: cosmetic

**P1A-E1 (ESSENTIAL)**  
Section I, p. 3 (abstract/intro block) and Sec. IV, pp. 8–11.  
The paper repeatedly claims “channel-level closure” of the four enumerated routes and states that “the 14 constraints … close those routes at amplitude-budget granularity.” However, the text explicitly qualifies this as holding only “under the stated assumptions,” only for “minimal channels rather than a complete diffeomorphism-invariant operator basis,” and only after excluding the Jackiw–Pi term \(R\wedge\tilde{R}\) and the parity-odd four-fermion partner of Route 1. No actual operator-level theorem is proved. The central claim is therefore an over-statement of what is demonstrated.  
**Required fix:** Rewrite every occurrence of “closure” to “amplitude-level no-go under the listed phenomenological restrictions and operator omissions.” Remove the phrase “channel-level closure” from the title and abstract.

**P1A-E2 (ESSENTIAL)**  
Abstract block (p. 3) and Sec. X, p. 15.  
The abstract states that “torsion vanishes at all perturbation orders” and that the Holst sector “decouples cleanly from scalar/tensor observables.” The only supporting argument given is the algebraic Bianchi identity on the Levi-Civita connection (\(T=0\)). This is a tree-level identity; it does not constitute a proof that the Holst term remains invisible at all loop orders once non-minimal fermion couplings or higher-curvature operators are restored. The claim exceeds what is shown.  
**Required fix:** Replace the all-orders statement with the precise, limited result actually proved in Sec. X.

**P1A-E3 (ESSENTIAL)**  
Sec. II C 2 (p. 6) and Appendix B (p. 21).  
The parity-odd operator (Eq. 6) is assigned naive mass dimension +1. The paper acknowledges that a dimension-+4 operator is required for a local EFT and treats the mapping \(\rho_\Lambda=\Xi M_P^4\) as an “on-shell scaling ansatz, not a derivation.” A dimensionally inconsistent operator cannot source a cosmologically relevant vacuum energy while remaining inside a controlled EFT. This is fatal to the dark-energy route analysis.  
**Required fix:** Either derive a consistent dimension-+4 completion or remove all claims that the operator sources late-time dark energy.

**P1A-M1 (MAJOR)**  
Sec. IV and Table I (p. 4).  
The four “routes” are closed only after the explicit omission of the Jackiw–Pi gravitational Chern–Simons term and its four-fermion partner. These operators are known in the literature to generate parity-odd effects at the same order as the Holst term. Their exclusion must be justified by a power-counting argument, not by fiat.  
**Required fix:** Provide a systematic operator classification up to dimension 6 that demonstrates why the omitted operators can be neglected.

**P1A-M2 (MAJOR)**  
Sec. XIII and Fig. 6 (p. 18).  
The two “surviving” predictions (\(f_\mathrm{NL}=-35/8\) and \(\beta\approx0.27^\circ\)) are stated to be “mechanism-independent” and “not derived from the ECH action.” Both are already present in the broader matter-bounce literature (Cai et al. 2011, etc.). The paper therefore does not predict any new observable that is distinctive to Einstein–Cartan–Holst gravity.  
**Required fix:** Either demonstrate a unique ECH signature or reframe the paper as a no-go result without positive observational claims.

**P1A-M3 (MAJOR)**  
Sec. II C 1 (p. 7) and Eq. (11).  
\(N_\mathrm{tot}\approx92\) is obtained by fitting the observed dark-energy scale after the fact. The paper itself calls this a “fitted parameter, not predicted.” All subsequent numerical claims that rely on this value (structural-tension argument, e-fold counting, etc.) are therefore post-dictions, not predictions.  
**Required fix:** Remove every sentence that presents \(N_\mathrm{tot}\approx92\) as a derived quantity.

**P1A-M4 (MAJOR)**  
Fig. 1 (p. 4) and Sec. IX.  
The diagram labels four routes “structurally closed (this paper)” while simultaneously drawing green arrows from “matter bounce” to the same observables. The visual claim that ECH is ruled out while the matter-bounce class survives is inconsistent with the text’s admission that the \(f_\mathrm{NL}\) prediction is not ECH-specific.  
**Required fix:** Redraw the figure so that the surviving predictions are unambiguously attributed to the broader bounce class, not to ECH.

**P1A-N1 (MINOR)**  
Throughout (e.g., pp. 2, 3, 6, 17).  
Frequent forward references to “Paper I(b)”, “Paper II”, “Paper III”, “Paper IV” (all “in preparation” or “companion”). PRD policy requires that the present manuscript be self-contained; results needed for the central argument must be published or supplied as appendices.  
**Required fix:** Move all essential MCMC and validation results into the present manuscript or publish the companions first.

**P1A-N2 (MINOR)**  
Sec. II A 2 (p. 6), Eq. (7).  
The one-loop estimate for \(\alpha/M\) is taken from an external reference and then treated as a free phenomenological parameter. The numerical value \(\sim10^{-21}\,\mathrm{GeV}^{-1}\) is never recomputed inside the paper.  
**Required fix:** Either recompute the coefficient or label it clearly as an external input.

**P1A-NIT1 (NIT)**  
Multiple instances of “this paper” in figure captions and section headings. Minor style issue.

**Length assessment**  
23 pages for a purely negative result whose positive predictions are not new constitutes excessive length. Recommended maximum: 12–14 pages after removal of redundant companion-paper material and the over-stated claims.

**Summary recommendation**  
**REJECT**

The manuscript does not establish a rigorous no-go theorem, relies on a dimensionally inconsistent operator treated as an ansatz, omits known parity-odd operators without justification, and presents two “surviving predictions” that are already present in the broader literature and are explicitly stated not to be derived from the ECH action. The central claim of “channel-level closure” is therefore not supported by the actual content. The paper would require a complete rewrite that limits itself to the narrow, technically correct perturbative-decoupling result proved in Sec. X before it could be reconsidered.