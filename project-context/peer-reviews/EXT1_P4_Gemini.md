# EXT1 P4 — Gemini 3.5 Thinking referee report
**Provider**: gemini.google.com web app · model **3.5 Thinking**
**Chat**: https://gemini.google.com/app/8340abb820aada09
**PDF**: chirality_catalog_paper_v171.pdf (md5 2f0317c4) · **Harvested**: 2026-06-10T17:25 PDT

---

Gemini said
Referee Report

Journal: Monthly Notices of the Royal Astronomical Society (MNRAS)

Manuscript Title: Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)

Author: Houston Golden (Independent Researcher)   
PDF

1. Recommendation

Minor Revisions. This manuscript presents an exceptionally rigorous, large-scale galaxy chirality analysis that provides crucial methodology and bias controls for future studies in cosmic isotropy. By introducing the largest chirality-labeled galaxy catalog to date (8.47 million galaxies, including 3.2 million spirals) , the author systematically deconstructs previous literature claims of a large-scale cosmic chirality dipole. The introduction of flip-equivariant test-time averaging (TTA) combined with a comprehensive 8-anchor systematic analysis sets a high standard for data hygiene in morphological cosmology. The paper is suitable for publication after addressing the minor clarifications and structural refinements detailed below.  
PDF
+ 4

2. Blockers (Must Fix Before Publication)

No terminal blockers remain. The author has proactively performed a thorough provenance audit that successfully identified and neutralized a major catalog tracking error present in an earlier iteration of the analysis. The subsequent structural rearrangement prioritizing the robust real-space estimator ensures that the load-bearing conclusions of the paper remain accurate and fully supported by version-controlled on-disk artifacts.  
PDF
+ 3

3. Majors (Should Fix)
Section IV.C / Appendix D — Optimizing the Block-Bootstrap Super-Pixel Scale

Issue: The joint nuisance-marginalized fit utilizes a block-bootstrap configuration at NSIDE=8 (yielding 440 super-pixels) to validate the spatial coherence of mapping residuals. While this approach successfully inflates the error bounds from the naive weighted least-squares (WLS) baseline, the manuscript lacks an explicit optimization analysis or justification for choosing NSIDE=8 as the primary block size over alternatives like NSIDE=4 or NSIDE=16.  
PDF
+ 1

Proposed Fix: Provide a brief sensitivity narrative or table demonstrating how the bootstrap variance σ(A
dipole
	​

) behaves across a small range of super-pixel resolutions. This will confirm that the chosen scale effectively captures the typical angular extent of the underlying depth and footprint systematics (e.g., DECaLS brick boundaries or imaging leg configurations).  
PDF

4. Minors (Polish)
Appendix B (Page 16) — Clarification of T7 Calibration Proxy Inversion

Issue: In the discussion of the bias-hardening suite, the author notes that when the T7 calibration proxy is restricted to equivariant-class spirals, the mean flip-swap error ordering unexpectedly inverts (0.698 for high confidence vs. 0.464 for low confidence). The text attributes this to the raw/equivariant class-disagreement subpopulation, but a sentence providing more physical or architectural intuition would greatly aid readability.  
PDF

Proposed Fix: Add a brief explanatory phrase clarifying how borderline spiral configurations or subtle asymmetric pixel patterns disproportionately influence this subpopulation during the horizontal flip evaluation.  
PDF

Section IV.A (Page 5) — Out-of-the-Box Calibration Warning

Issue: The text carefully cautions that the max-class probabilities derived from the pipeline are strongly overconfident relative to external truth (e.g., Galaxy Zoo 1 cross-matches).  
PDF

Proposed Fix: Add a brief explicit recommendation in the text alerting community users that if they intend to employ the soft probabilities for downstream probabilistic models, they should first implement formal calibration steps (e.g., temperature scaling or Platt scaling) rather than treating the raw values as strict frequentist confidence intervals.

5. Strengths

Unprecedented Scale and Coverage: The work compiles the largest chirality-labeled galaxy catalog to date, leveraging 8,474,531 galaxies from the DESI Legacy Imaging Surveys DR8 to extract 3,201,160 equivariant-classified spirals. This expands upon previous convolutional neural network (CNN) scales by a factor of 1.6.  
PDF
+ 1

Methodological Innovation via Equivariant TTA: By classifying each galaxy on both its original image and its horizontal reflection, the pipeline enforces a flip-swap correlation of exactly 1.000 by construction. This completely collapses the raw single-pass classifier chirality bias (shifting the global asymmetry deviation from +0.788% to a controlled -0.265%).  
PDF
+ 2

Exemplary Systematics Attribution: The deployment of an 8-anchor systematic battery—spanning quality-quartile stratifications, leg-proxy cross-power, and boundary-distance variance checks—convincingly isolates and neutralizing mask-geometric leakage channels.  
PDF
+ 2

6. Specific Scrutiny
Subsample-Mask −0.12σ MASTER-Deconvolved Null

The manuscript transparently details that a previously reported −0.12σ MASTER ℓ=1 null on a putative "strict-superset subsample mask" (n=5,547,858, f
sky
	​

=0.659) was traced during a provenance audit to an unversioned script operating on a synthetic catalog footprint. The author correctly withdrew this finding. Because the real-space dipole fit on the production catalog was pre-declared as the primary cosmological estimator, no scientific conclusions are compromised by this withdrawal .  
PDF
+ 4

Joint Nuisance-Marginalized Fit and Block-Bootstrap Over-Optimization

In Appendix D, the author performs a joint fit to a 9-template design matrix. A naive WLS regression yields a deceptive −264.5σ exclusion of a 1.7% dipole because it fails to account for the spatial coherence of the mapping residuals. By shifting to a block-bootstrap approach over 440 super-pixels at NSIDE=8, the author appropriately models the spatial covariance. This correctly inflates the error bounds to yield a robust, honest headline exclusion statistic of z≈−18.1.  
PDF
+ 4

Canonical-Mask +3.64σ Three-Interpretation Closure

The observed +3.64$\sigma$ moment-z residual (≈1.9σ Gaussian-equivalent) on the un-apodized canonical mask is subjected to an impressive multi-interpretation closure. Instead of over-interpreting this marginal deviation as cosmic parity violation, the author systematically disfavors a cosmological origin (interpretation i) by demonstrating that the signal is broadband low-ℓ structured (σ
ℓ=2
	​

=+4.73>σ
ℓ=1
	​

=+3.63) and undergoes a complete washout when stratified into quality quartiles. This leaves interpretation (ii)—a coherent depth/morphology systematic—as the favored explanation.  
PDF
+ 4

ℓ=2 Cross-Spectrum vs. Pixel-Density Proxy

The analysis of the cross-correlation coefficient (r
ℓ
	​

) between the chirality field A
p
	​

 and the total pixel-density field n
total
	​

(p) reveals a significant anti-alignment at the quadrupole scale (r
ℓ=2
	​

=−0.65 with z=−2.89). This diagnostic offers compelling empirical proof that the low-ℓ auto-spectrum excess is tightly coupled to local imaging depth and survey footprint geometry rather than tracking a genuine primordial signal.  
PDF
+ 4

MASTER-Decoupled Monopole-Only Null

The generative null framework utilizing 500 binomial realizations on the exact canonical mask demonstrates that a uniform global monopole couples to the patchy survey-mask geometry to reproduce 99.32% of the observed raw, pre-MASTER ℓ=1 power .  
PDF

Referee Note on Power Fractions: For clarity, a reader reviewing the pre-MASTER power spectrum might erroneously infer a large unexplained fractional component based on traditional residual scaling. However, the text's truth-audit confirms that 99.32% of the pre-MASTER power is explicitly accounted for by this leakage channel alone, leaving less than 1% unexplained prior to deconvolution. MASTER deconvolution substantially reduces this leakage, and the remaining post-MASTER canonical residual (+3.64$\sigma$) is thoroughly neutralized by the author's systematic templates.  
PDF
+ 3

Shamir 2020 vs. 2022 Literature Split

The manuscript accurately maps and addresses prior claims of cosmic parity asymmetry across different historical datasets. It correctly separates the findings and metrics of Shamir (2020) from the subsequent galaxy spin-direction alignment analyses on the DESI Legacy sample in Shamir (2022b). These entries are correctly paired with their valid preprint identifiers (arXiv:2007.16116 and arXiv:2208.13866, respectively) within the references section.  
PDF
+ 4




Thinking

