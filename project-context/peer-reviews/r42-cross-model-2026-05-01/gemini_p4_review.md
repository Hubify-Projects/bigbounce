---
model: gemini-3.1-pro-preview
paper: p4
paper_title: Galaxy Chirality Catalog (Paper 4)
pdf_path: /Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/chirality_catalog_paper.pdf
date: 2026-05-01
prompt_tokens: 9590
completion_tokens: 2087
total_tokens: 16446
review_type: cross-model adversarial peer review
reviewer: Google Gemini (cross-model check vs Anthropic Claude pipeline)
---

## Summary verdict
MAJOR REVISION: The catalog construction is impressive, but the statistical argument dismissing the $2.75\sigma$ dipole via NaMaster deconvolution is mathematically contradictory, and the uncorrected rotational bias is not tested against spatially varying survey systematics.

## BLOCKERS (paper cannot ship as-is)

- **B-1: Mathematically impossible NaMaster deconvolution logic**
- Section IV.C, Table IV, and Footnote 5
- Defect: The author claims the raw pseudo-$C_1$ has a $2.75\sigma$ significance "relative to 1,000 Monte Carlo null realizations" (Table IV), but that after MASTER deconvolution the significance drops to $-0.12\sigma$. MASTER deconvolution is a linear matrix operation ($C_{deconv} = M^{-1} C_{pseudo}$). If the data is a $2.75\sigma$ outlier relative to *masked* MC nulls in pseudo-space, it must remain an outlier in deconvolved space unless the variance is entirely dominated by off-diagonal mode-coupling from higher multipoles (which is false for white noise). Footnote 5 reveals the truth: the pipeline used the wrong $N$ (including non-spirals) for the analytical shot-noise subtraction, artificially suppressing the noise floor and creating a fake $2.75\sigma$ excess. 
- What would fix it: Remove the contradictory narrative about "mode coupling" inflating the signal. Recompute the pseudo-$C_\ell$ and deconvolved $C_\ell$ using the correct $N_{spiral}$ for both the data and the 1,000 MC nulls. Report the empirical p-value directly from the MC ensemble without relying on botched analytical shot-noise subtractions.

- **B-2: Unconstrained spatially-varying rotational bias**
- Sec III.D, Sec IV.B, and Table V
- Defect: The author explicitly admits that "Rotational orientation dependence... is not eliminated" and causes a $9.5\sigma$ monopole. The DESI Legacy Survey has spatially varying PSF ellipticity and scan directions. The $Z_2$ (horizontal flip) TTA does not commute with arbitrary rotations; if the classifier is sensitive to the alignment of the galaxy with the local PSF, this will project into a spurious dipole. Table V's broad sky regions average out local scan-direction correlations and are insufficient to rule this out.
- What would fix it: Cross-correlate the Catalog C CW fraction map directly with the DESI Legacy PSF ellipticity and position angle maps. Prove that the CW fraction is independent of local survey orientation to $<0.1\%$.

## MAJOR concerns (must address before resubmission)

- **M-1: Circularity in Catalog B calibration**
- Sec III.F
- Defect: Catalog B (Platt-calibrated) is fit against CE-ResNet consensus labels, which the author admits "inherits any systematic bias present in the CE-ResNet reference catalog." Releasing a catalog calibrated against a competitor's model, while claiming it is suitable for "ML downstream tasks," pollutes the literature with correlated systematics.
- What would fix it: Calibrate Catalog B against the independent Galaxy Zoo 1 labels (which the author already cross-matched in Sec II.B), or explicitly deprecate Catalog B for any cosmological parity tests.

- **M-2: Edge-on contamination math assumes rotational invariance**
- Sec VI.D
- Defect: The author claims edge-on galaxies ($b/a < 0.3$) merely "dilute sensitivity" because the TTA procedure assigns them exactly equal CW/CCW probabilities. This is only true if the edge-on galaxy is perfectly symmetric under horizontal reflection. If an edge-on galaxy is aligned diagonally due to survey scan direction, its horizontal reflection has the opposite diagonal alignment. A rotationally biased classifier will not output symmetric probabilities for these two orientations.
- What would fix it: Evaluate the equivariant CW fraction specifically for the $b/a < 0.3$ subsample in Catalog C. If it deviates from 0.5000, the TTA is failing on rotated edge-on disks, and this leakage must be quantified.

## MINOR concerns (should fix, won't block)

- **m-1: Claiming a sensitivity floor below the systematic floor**
- Sec VI.C, Eq. 6
- Defect: The author claims a "minimum detectable dipole of 0.2%". However, the catalog has a known, uncorrected systematic monopole of 0.26% ($9.5\sigma$). It is physically meaningless to claim a sensitivity floor lower than your systematic error floor unless you can rigorously prove the systematic has strictly zero dipole projection (which B-2 shows is not proven).
- What would fix it: Revise the sensitivity claim to reflect the systematic floor, or add a strict caveat that the 0.2% is a statistical Poisson limit, not a systematic-inclusive limit.

- **m-2: Overly conservative look-elsewhere correction**
- Sec IV.D
- Defect: Applying a Bonferroni correction to 650 hemisphere directions is statistically inappropriate because the hemispheres heavily overlap (highly correlated test statistics). This artificially weakens the significance of the $3.05\sigma$ peak, making the null result look stronger than it is.
- What would fix it: Use an empirical Monte Carlo threshold for the maximum-over-directions statistic, or use the Euler characteristic for Gaussian random fields on a sphere.

## Statistics / methodology audit
*   **Is the chosen statistic the right one?** Pseudo-$C_\ell$ is correct for cut-sky dipole searches, but the analytical shot-noise subtraction is fundamentally broken by using the wrong $N$ (Footnote 5).
*   **Are error bars consistent?** Mostly frequentist (Poisson/binomial). However, there is tension between the bootstrap CI and analytical Poisson in Sec IV.B that is glossed over.
*   **Are look-elsewhere corrections applied?** Yes, but incorrectly (Bonferroni on highly correlated spatial data).
*   **Are MCMC convergence diagnostics reported?** N/A.
*   **Are systematic uncertainties quantified?** Hand-waved. The $9.5\sigma$ monopole is dismissed as "spatially uniform" without a rigorous spatial correlation test against survey properties (PSF, seeing, depth).
*   **Are claimed detection significances reproducible?** No. The drop from $2.75\sigma$ to $-0.12\sigma$ via a linear deconvolution matrix is mathematically impossible if the MC nulls were treated identically and the variance was empirical.

## Cosmology / physics sanity check
*   No conflict with Planck 2018, ACT DR6, or DESI BAO. The observable is highly specific to late-time galaxy morphology.
*   The connection to Einstein-Cartan-Holst gravity (Sec VI.F) is highly speculative and borders on marketing. The author correctly caveats that there is no falsifiable quantitative prediction, which saves the section from being a blocker, but it adds little physics value.
*   The assumption that parity violation would be scale-independent or dipole-only is a strong prior. If the signal is tied to local tidal fields (as in Motloch & Pen), it would appear in higher multipoles. The $\ell=2-5$ check is good, but should be emphasized over the pure dipole.

## Reproducibility
*   Data products, code, and chains are published on HuggingFace and GitHub with pinned versions.
*   A competent grad student could reproduce the pipeline, but they would immediately find the $N_{gal}$ vs $N_{spiral}$ bug in the NaMaster script documented in Footnote 5.
*   Software versions and random seeds are pinned.

## What an Anthropic-Claude review would have missed
*   **The NaMaster linear algebra contradiction:** Claude typically accepts the author's narrative that "mode coupling inflates the signal" and "deconvolution fixes it." An adversarial physicist knows that if you measure significance relative to *masked* Monte Carlo nulls, the mode coupling is already in the nulls. A linear matrix multiplication cannot erase a $2.75\sigma$ outlier.
*   **The geometric loophole in TTA:** Claude sees "equivariant averaging" and assumes the bias is gone. But the TTA only uses horizontal flips ($Z_2$). It does not use rotations. Claude would miss that spatially varying PSF rotation + rotationally biased classifier = spurious dipole, completely bypassing the $Z_2$ TTA defense.
*   **Sycophancy on "Conservative" limits:** Claude will praise the author for rounding 0.14% up to 0.2% as "conservative." An adversarial reviewer notes that the systematic error (0.26% monopole) is *larger* than the claimed sensitivity (0.2%), making the 0.2% claim physically meaningless.

## Bottom line for the author
Your catalog scale and TTA implementation are excellent, but your statistical defense of the null result is currently resting on a botched NaMaster noise subtraction and an unverified assumption about rotational bias. You cannot use a linear deconvolution to explain away a $2.75\sigma$ anomaly if your nulls are also masked; you must fix the $N_{spiral}$ bug in your shot-noise math. Furthermore, because your TTA does not enforce rotational equivariance, you must explicitly cross-correlate your chirality maps with DESI PSF ellipticity/position angle maps to prove your $9.5\sigma$ monopole isn't projecting into a dipole. Fix the math, run the PSF cross-correlation, and this will be a definitive paper.
