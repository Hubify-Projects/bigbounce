# P1B R29 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.55.pdf` md5=b776a111 pages=17
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 69.3s

---

**Referee Report**

**P1B-E1 (ESSENTIAL, Sec. I, p. 2)**  
The opening paragraph and §I repeatedly state that the stock-CAMB \(\Lambda\)CDM+\(\Delta N_{\rm eff}\) run is “Not a spin-torsion theory module” and “does not verify the spin-torsion theory module itself.” The entire 17-page document is therefore a null-consistency check on a proxy that the authors themselves declare cannot test the central claim of the ECH program. Required fix: either (a) supply the actual modified Boltzmann solver and rerun the headline chains with it, or (b) re-title and re-scope the manuscript as an internal technical note rather than a PRD companion paper.

**P1B-E2 (ESSENTIAL, Abstract p. 1 & Sec. III p. 3)**  
Abstract asserts “Both frozen dataset combinations find \(\Delta N_{\rm eff}\) consistent with zero.” The full-tension posterior is \(-0.020\pm0.169\); the Planck+BAO+SN posterior is \(+0.065\pm0.17\). These intervals are formally consistent with zero, but the paper never reports a Savage-Dickey density ratio or \(\ln B\) at the \(\Lambda\)CDM point. The claim is therefore an unquantified statement of “consistency,” not a model-comparison result. Required fix: compute and quote the Bayes factor (or state that it is deferred and remove the sentence from the abstract).

**P1B-E3 (ESSENTIAL, Sec. IV p. 6–8 & Fig. 3)**  
The NaMaster pipeline-recovery bias is reported as \(\Delta\hat\beta=-0.032^\circ\) (\(\beta_{\rm inj}=0.27^\circ\)) and \(-0.040^\circ\) (worst-case). The text simultaneously claims this bias “is carried forward as the NaMaster systematic floor.” No propagation of this floor into the final birefringence significance (3.9\(\sigma\) combined) is performed. The headline significance is therefore uncalibrated. Required fix: fold the measured 0.040° systematic into the inverse-variance combination and re-quote the significance.

**P1B-E4 (ESSENTIAL, Sec. VI p. 10–12)**  
The spectator-ALP consistency check is performed with a fixed \(C_{a\gamma}=8\) and a continuous prior on \(\theta_i\) that explicitly requires \(\theta_i\sim0.1\) (a \(\sim25\times\) fine-tuning relative to the natural midpoint \(\theta_i=0.5\)). The text states this tuning “is required regardless of whether the underlying cosmology is a bounce or \(\Lambda\)CDM.” The result is therefore not a prediction of the ECH framework but an existence proof that a tuned ALP can fit the data. Required fix: either remove the claim that the result is “consistent with the ECH framework” or demonstrate that the required tuning arises dynamically from the Holst sector.

**P1B-M1 (MAJOR, p. 1–17 throughout)**  
The manuscript is 17 pages long yet contains no new cosmological parameter constraint, no new sky measurement, and no modified Boltzmann code. All quantitative results are either (a) recovery of published Planck/ACT numbers or (b) pipeline null tests. PRD does not publish technical verification notes of this length. Recommended maximum length after cuts: 6–8 pages.

**P1B-M2 (MAJOR, Sec. II p. 2 & Table I)**  
The two frozen chains differ by the presence/absence of the SHOES \(M_B\) anchor and DES-Y3 \(S_8\) Gaussian prior. The text never quantifies the tension between these two dataset combinations (e.g., parameter-shift statistic or suspiciousness). The reader cannot judge whether the two “frozen” posteriors are compatible before they are averaged.

**P1B-M3 (MAJOR, Fig. 1 & Table I)**  
Corner plot and Table I report \(\Delta N_{\rm eff}\) posteriors whose 95 % upper limits are quoted under two different conventions (two-sided vs one-sided). The paper never states which convention is used for the quoted “\(\Delta N_{\rm eff}<0.31\)” limit, rendering the number non-reproducible.

**P1B-N1 (MINOR, p. 3 footnote 1)**  
Burn-in and thinning choices are documented only in footnotes and repository files. The main text must contain a one-paragraph “MCMC convergence protocol” subsection with explicit \(R-1\), ESS, and burn-in fraction for every chain.

**P1B-N2 (MINOR, multiple locations)**  
Phrases such as “the same birefringence field arises in standard GR with an identical ALP” appear verbatim in Sec. I and again in Sec. VI. Remove the duplication.

**P1B-NIT1–NIT3**  
Minor typographic issues (repeated “canonical canonical-mask” in one figure file name reference, inconsistent use of “full-tension” vs “full tension,” axis label “\(\log_{10}(m_a/{\rm eV})\)” missing parentheses on p. 11) are cosmetic.

## Summary recommendation
**REJECT**

The manuscript is a lengthy technical appendix whose central analyses are explicitly declared by the authors to be incapable of testing the physical model they purport to support. The only quantitative results are either null recoveries of existing data or a tuned spectator-field fit that requires a 25-fold fine-tuning the authors themselves flag as non-generic. No Bayes factor, no calibrated systematic budget on the birefringence angle, and no self-contained demonstration that the ECH framework predicts the observed signal are provided. The paper therefore fails the minimum threshold for a PRD methods or companion article.