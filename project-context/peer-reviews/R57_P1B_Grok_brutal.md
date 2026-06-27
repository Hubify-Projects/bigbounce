# P1B R57 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/private/tmp/R57_P1B/paper1b_mcmc_companion.pdf` md5=653da036 pages=22
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 self-critique (1013 chars)
**Wall time**: 258.8s

---

**Referee Report**

**Paper:** Technical Verification Companion to the ECH Spin-Torsion Program: \(\Lambda\)CDM+\(\Delta N_{\rm eff}\) MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model (P1B)

**Journal target:** Phys. Rev. D (high bar for methods/numerical cosmology papers)

**Findings**

**P1B-E1 (ESSENTIAL)**  
Section I (p. 2) and abstract (p. 1): The paper repeatedly states it is “NOT a spin-torsion theory module,” “NOT a competitive sky detection,” and “NOT a distinctive ECH prediction.” The entire contribution is therefore a set of null-consistency checks on stock CAMB + a standard ALP model. No derivation or test of any ECH-specific Boltzmann modification appears. Required fix: either (a) add the actual ECH-modified equations and rerun the chains, or (b) re-title and re-scope the manuscript as a pure technical-methods note with no cosmology-theory framing.

**P1B-E2 (ESSENTIAL)**  
Abstract (p. 1) and §III (p. 3): The headline numbers 309,189 frozen samples and \(\Delta N_{\rm eff} = -0.020 \pm 0.169\) (full-tension) are reported as a “compatibility check.” The text simultaneously declares the run uses unmodified CAMB and therefore “does not verify the spin-torsion theory module.” The abstract claim is therefore stronger than the body supports. Required fix: remove all theory-interpretation language from the abstract and title; the numbers test only stock \(\Lambda\)CDM+\(\Delta N_{\rm eff}\).

**P1B-E3 (ESSENTIAL)**  
§IV (p. 7–10) and Fig. 3: The NaMaster pipeline-recovery bias is measured on foreground-free synthetic skies. The paper then states the observed 0.040° worst-case bias “is carried forward as the observed NaMaster pipeline bias.” No propagation of this bias into the final \(\beta\) uncertainty budget or any real-sky systematic test is shown. Required fix: either demonstrate the bias on end-to-end simulations that include realistic foregrounds and the exact PR3/PR4 masks, or downgrade the claim to “internal pipeline validation only.”

**P1B-M1 (MAJOR)**  
Abstract + §VI (p. 12–15): The spectator-ALP consistency check uses a scan prior that explicitly requires \(\theta_i \lesssim 0.1\) (25× fine-tuning relative to the natural midpoint) to remain inside the “spectator-safe” region. The paper acknowledges this is “not free of misalignment-prior tuning.” No quantitative assessment of prior volume or Occam penalty is provided. Required fix: add a proper Bayesian evidence ratio between the tuned spectator corner and the untuned ALP model.

**P1B-M2 (MAJOR)**  
Table I (p. 5) and §V (p. 11): Two frozen chains are combined (176 k + 133 k samples) yet the text notes a 0.04\(\sigma\) shift when the low-ℓ likelihood is swapped. No reweighting or importance-sampling correction is applied before quoting the headline posteriors. Required fix: either reweight or demonstrate that the shift is negligible for all reported parameters at the quoted precision.

**P1B-M3 (MAJOR)**  
Fig. 1 and Table I: The \(\Delta N_{\rm eff}\) posterior is stated to be “consistent with zero.” The one-sided 95 % upper limit is given as 0.31 only after discarding the negative tail and renormalizing. The paper does not show the untruncated posterior or the effect of the physical \(\Delta N_{\rm eff} \ge 0\) prior on the \(H_0\) tension metric. Required fix: present both the truncated and untruncated limits and recompute the tension metric under each.

**P1B-N1 (MINOR)**  
p. 1 header: “Dated: June 26, 2026” is a future date. Replace with the actual submission or revision date.

**P1B-N2 (MINOR)**  
Multiple sections contain long “What is NOT in this paper” and “Scope of the validation” disclaimers. These are appropriate for a technical note but inflate length; condense to a single paragraph.

**P1B-NIT**  
Several figure captions and footnotes contain internal reproducibility paths and commit hashes. Move to a Data Availability paragraph; they are not needed in captions.

**Summary recommendation**  
**REJECT**

The manuscript is a purely technical null-consistency exercise performed with unmodified public codes on synthetic skies. It explicitly disclaims any test of the ECH spin-torsion framework it purports to support, relies on a heavily tuned spectator-ALP prior for its only “positive” result, and presents pipeline-validation biases as observational systematics without end-to-end propagation. These are fatal scope and methodology mismatches for Phys. Rev. D. A substantially revised, narrowly scoped technical note limited to the NaMaster bias measurement on controlled simulations could be reconsidered, but the present document does not meet the journal’s standards for either novelty or rigor.

---

## PASS 2 — self-critique findings (what initial review missed)

[P1B-m1]  
p. 5, Table I caption: the text states that the full-tension \(S_8=0.814\pm0.008\) “is consistent with the naive two-Gaussian combination … (0.827±0.010 @ 0.814±0.009; agreement at the 0.01σ level).” The quoted values differ by 0.013; the naive quadrature sum of uncertainties is \(\sqrt{0.010^2+0.009^2}\approx0.0135\), giving \(\approx0.96\sigma\). The stated “0.01σ” figure is therefore an arithmetic typo (most likely intended “1.0σ” or “0.1σ”).

[P1B-N3]  
p. 1 (header) and p. 4: the date “June 26, 2026” appears in the title block while the text refers to “the iter2 \(w_0w_a\) chain” and to a 500-MC run performed “(April 2026)”. These future dates are internally inconsistent with any plausible submission timeline and should be corrected to actual calendar dates.

No other arithmetic mismatches, figure-caption/body discrepancies, dimensional inconsistencies, broken cross-references, or unsupported novelty claims were identified beyond the issues already catalogued in the original review.