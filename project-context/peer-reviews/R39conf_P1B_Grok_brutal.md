# P1B R39conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/paper1b_mcmc_companion.pdf` md5=06410d7c pages=20
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 96.9s

---

**Referee Report**

**P1B-E1 (ESSENTIAL)**  
Section: Abstract-equivalent summary (p. 1, first paragraph)  
Problem: The headline claim “Both frozen dataset combinations find ΔN_eff consistent with zero (−0.020 ± 0.169 full-tension; +0.058 ± 0.179 Planck+BAO+SN)” is presented without the explicit qualifier that this is a stock-CAMB proxy run containing *no* ECH Boltzmann modifications. The same paragraph later states the run “does not verify the spin-torsion theory module itself.”  
Required fix: Insert the sentence “This is a null-consistency test of an unmodified Boltzmann solver; it supplies no constraint on the ECH sector” immediately after the quoted numbers.

**P1B-E2 (ESSENTIAL)**  
Section: p. 1 (Scope of the validation) and p. 6 (Scope note)  
Problem: The NaMaster pipeline-recovery bias (Δβ̂ = −0.032° to −0.040°) is reported next to the published 3.6σ Planck/ACT value (0.342° ± 0.094°) without a standing “not directly comparable” clause at every juxtaposition. The text contains only one such disclaimer (p. 2).  
Required fix: Add the explicit non-comparability statement in the abstract-level summary and again in every results paragraph that places the two numbers in the same sentence.

**P1B-M1 (MAJOR)**  
Section: p. 1 and p. 10 (Spectator-ALP consistency check)  
Problem: The paper concludes that the observed β ≈ 0.27° “is not a distinctive ECH prediction” because the identical signal appears in GR + spectator ALP. This is an admission that the central birefringence result supplies no discriminating power for the ECH framework. The manuscript therefore contains no positive evidence that the ECH sector is required by any datum.  
Required fix: Either (a) remove the birefringence section or (b) demonstrate a quantitative, ECH-specific prediction that differs from the GR+ALP case at >3σ.

**P1B-M2 (MAJOR)**  
Section: p. 2 (Scope of this paper) and entire §III  
Problem: The MCMC analysis uses unmodified CAMB; the text repeatedly states “No custom CAMB modifications are solved.” The only new parameter (ΔN_eff) is already part of the public Boltzmann suite. No ECH-specific degree of freedom is sampled. The section therefore reports a standard ΛCDM extension already explored in the literature.  
Required fix: Provide at least one ECH-derived modification to the Boltzmann hierarchy that is actually implemented and sampled, or reclassify the paper as a pure technical-methods note.

**P1B-M3 (MAJOR)**  
Section: p. 20 (Table I) and p. 4 (text)  
Problem: The one-sided 95 % upper limits on ΔN_eff (0.31 and 0.40) are obtained by post-processing the renormalized CDF after discarding the negative tail. This procedure is not the standard Planck convention and is not compared with the published Planck one-sided limits on extra relativistic species.  
Required fix: Recompute the limits with the exact Planck likelihood pipeline or demonstrate numerical equivalence.

**P1B-N1 (MINOR)**  
Section: p. 1 (Dated: June 13, 2026)  
Problem: Future date on a manuscript under review.  
Required fix: Correct to actual submission or preprint date.

**P1B-N2 (MINOR)**  
Section: Multiple figure captions (Figs. 1–4)  
Problem: Axis labels and units are present but the color-bar scaling for the 2-D posteriors in Fig. 1 is never stated.  
Required fix: Add explicit normalization statement.

**P1B-N3 (NIT)**  
Section: p. 2 (“Scope of the validation”)  
Problem: Redundant phrasing “the test confirms the algebraic pseudo-C_ℓ E → B deconvolution under MASTER mode coupling, NOT the physical separation…”  
Required fix: Remove the capitalized “NOT” for house style.

**Additional observations**  
- The manuscript is 20 pages long yet explicitly disclaims every cosmological claim that would normally justify a PRD article.  
- All load-bearing numerical results (ΔN_eff, H_0, β̂_NaMaster, β_ALP) are either (a) recovered from public codes without modification or (b) shown to be reproducible by standard GR + ALP.  
- No standalone ECH prediction is tested; every positive statement is accompanied by a scope limitation that removes its relevance to the ECH framework.

## Summary recommendation
**REJECT**

The paper is a technical-methods companion that (i) performs no ECH-specific calculation, (ii) repeatedly states that its results do not constrain the theory it claims to verify, and (iii) presents no new cosmological observable or parameter constraint beyond what is already obtainable with public Boltzmann codes and standard ALP Lagrangians. Under PRD’s threshold for a standalone research article, these deficiencies are fatal.