# P1B INT-X-P1B — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=d013792f pages=22
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 69.4s

---

**Referee Report (Adversarial)**

**Paper:** Technical Verification Companion to the ECH Spin-Torsion Program… (P1B)

**Journal bar:** Physical Review D (high). The paper is a 22-page technical companion whose core contribution is three verification exercises, each explicitly labeled “NOT a spin-torsion theory test / NOT a sky detection / NOT a model-preference result.” This framing already signals that the manuscript is largely a methods audit rather than a physics result. At PRD length and depth, that is difficult to justify.

**Findings**

**P1B-E1 (ESSENTIAL)**  
Section I (p. 2) and abstract (p. 1): “This run uses stock CAMB with ΔN_eff as a free parameter and carries no torsion modifications to the Boltzmann equations.”  
The entire ΔN_eff MCMC section is therefore a generic radiation-proxy test. The abstract nevertheless leads with “ECH Spin-Torsion Program.” The mismatch between title framing and actual content is not resolved by repeated “not a theory module” disclaimers.  
**Fix:** Retitle or rewrite the abstract and introduction so the scope is stated in the first paragraph; remove “ECH Spin-Torsion” from the title if no ECH-specific module is exercised.

**P1B-E2 (ESSENTIAL)**  
Abstract (p. 1) and Sec. III (p. 3): “the ΔN_eff extension does not reduce the residual ~3.6σ tension.”  
The 3.6σ figure is taken from the literature (Eskilt & Komatsu 2022) for β, not for H_0. The H_0 tension numbers in Table I are 2.6σ (full-tension) and 2.0σ (Planck+BAO+SN) relative to the DES-Y3 prior. The abstract therefore mis-states the tension being discussed.  
**Fix:** Remove the 3.6σ claim from the abstract or replace it with the correct, self-contained H_0 tension values computed in this work.

**P1B-E3 (ESSENTIAL)**  
Sec. IV (p. 7–10) and Fig. 3: The NaMaster pipeline-recovery test is performed on synthetic CMB-only skies. The text repeatedly states “not a competitive sky detection” and “the β–α degeneracy … is absent by construction.”  
A 500-realization Monte-Carlo exercise whose only purpose is to recover an injected angle on foreground-free maps is a code-validation test, not a scientific result. At 8 pages it is disproportionate.  
**Fix:** Reduce to a one-page methods appendix or move to supplementary material.

**P1B-M1 (MAJOR)**  
Sec. VI and Table IV (p. 13–17): The spectator-ALP posterior is reported only after imposing Ω_a < 0.01 (13 % of the mass). The “spectator-safe” verdict rests on this cut. No justification is given for why Ω_a < 0.01 is the physically motivated threshold rather than, e.g., Ω_a < 0.05 or a Bayes-factor cut.  
**Fix:** Provide a quantitative motivation for the cut or report the full posterior without the cut.

**P1B-M2 (MAJOR)**  
Table II (p. 6) and Sec. III (p. 4–5): The w_0w_a chain is presented with explicit overlap-inflation caveats, yet the table still quotes means and “vs ΛCDM” columns. The text states that a proper model-comparison (ΔAIC/BIC/ln B) is deferred.  
Presenting numerical values while simultaneously declaring them “not quotable” is internally inconsistent.  
**Fix:** Either remove the table or move it to an appendix labeled “exploratory, overlap-uncorrected.”

**P1B-M3 (MAJOR)**  
Abstract (p. 1) and Sec. II (p. 2): The manuscript is labeled a “companion paper” to Paper I(a). Multiple load-bearing statements (“the 13 logically independent structural barriers,” “the perturbation-transparency theorem,” f_NL = −35/8) are imported by citation only. The standalone-reader test fails.  
**Fix:** Either make the present paper self-contained or reduce its scope to pure technical verification that does not rely on results from the companion.

**P1B-N1 (MINOR)**  
Multiple instances of “R7”, “R8”, internal run labels, and “reproducibility/…” paths appear in figure captions and footnotes. These are version-control artifacts.  
**Fix:** Remove all internal bookkeeping strings from the published PDF.

**P1B-N2 (MINOR)**  
Fig. 1 caption (p. 8) states “119,617 post-burnin samples … 176,240 raw.” The arithmetic 176 240 − (burn-in fraction) does not exactly match the quoted post-burn-in number once the two frozen chains are added. Minor rounding inconsistency.  
**Fix:** Correct the arithmetic or state the exact burn-in cut used.

**P1B-NIT1–NIT3**  
Minor typographic issues (duplicate “the the”, axis-label font size in Fig. 4, inconsistent use of “full-tension” vs “full tension”).

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript is a careful but over-long technical audit whose three main exercises are each explicitly disclaimed as “not a test of the ECH theory.” The combination of (i) title/abstract framing that promises ECH spin-torsion results, (ii) heavy reliance on an unseen companion paper, (iii) an 8-page pipeline-validation exercise on synthetic skies, and (iv) internal contradictions in the presentation of the w_0w_a and spectator-ALP posteriors places the paper below the current PRD threshold for a standalone methods or verification article. A substantially shortened version focused on one cleanly scoped verification task, with all scope limitations moved into the first paragraph, could be reconsidered.