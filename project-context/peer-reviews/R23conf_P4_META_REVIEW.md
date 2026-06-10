# P4 R23conf — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 383.4s

---

Meta-review for “Survey-Scale Galaxy Chirality with Equivariant TTA …”

This meta-review highlights issues that none of the five prior referees appear to have caught. I focus on blind spots that commonly slip through: hidden conditioning in nulls, cross-reference inconsistencies, calibration/sensitivity conflation, and end-to-end arithmetic/logic chains.

P4-META-E1
Severity: ESSENTIAL
Section/page: Sec. IV C.a (p.6) and Methods hierarchy/Table I (p.4)
Why missed: Other referees queried weighting choices and null comparability in the harmonic channel, but did not examine the primary real-space null construction itself.
Specific problem: The primary real-space dipole null is built by “randomly permut[ing] per-pixel asymmetry values Ap across the in-mask pixels” with a uniform-pixel-weight LS fit. This null ignores the strong heteroskedasticity of Ap (Var[Ap] ≈ 1/Nspiral(p)) across the mask and breaks the native correlation between Ap and per-pixel Nspiral(p). With uniform pixel weights, high-variance pixels contribute equally to the dipole fit in both data and null, but the pixel-permutation null scrambles the variance–geometry coupling in a way that a per-galaxy label-shuffle would not. This can miscalibrate the null width and thus p = 0.30.
Required fix: Recompute the real-space dipole significance under a per-galaxy label-shuffle null (preserving Nspiral(p) and its noise properties) and, ideally, with variance-aware weights (e.g., inverse-variance or count weighting). Report side-by-side: z_moment and empirical rank p for (i) pixel-permutation null (current), (ii) per-galaxy label shuffle, and (iii) variance-aware regression. State any change in p and A50/A95.

P4-META-E2
Severity: ESSENTIAL
Section/page: Sec. VI A.b (p.10), Table V (p.10)
Why missed: Reviewers checked columns/rounding but not the conditioning on dipole-axis orientation for the injection experiment.
Specific problem: The real-space injection–recovery test (Table V) does not specify the distribution of injection axes. On a patchy fsky ≈ 0.49 footprint with strong anisotropy, detection efficiency P(σ > 3) depends sensitively on the dipole orientation. The table quotes a single probability per amplitude (e.g., A50 ≈ 0.75%), but does not state whether this is an average over random axes, a worst-/best-case axis, or a fixed axis, making the quoted sensitivity not generally interpretable.
Required fix: Define the axis protocol (uniform over the sphere, fixed, or a grid) and report: (a) axis-averaged P(σ > 3), (b) 16–84% range across axes, and (c) the worst-/best-case axis performance at each A. If resources are limited, add a small spot-check (e.g., 10 random axes) to quantify orientation spread. Clarify that the falsification criterion is axis-averaged (or otherwise).

P4-META-E3
Severity: ESSENTIAL
Section/page: Sec. IV A (p.4), Fig. 6 (p.8), Appendix B.e/Table VIII (p.13)
Why missed: Prior reviews discussed peq definitions but not the glaring probability–accuracy mismatch and its implications for “HC” selection.
Specific problem: The classifier’s probability calibration is severely inconsistent with its external accuracy. The catalog-wide mean max-class probability is 0.951 with median 0.9997, yet the three-class accuracy vs independent GZ1 labels is only 58.7% and the spiral-chirality accuracy 69.91%. This indicates extreme overconfidence. Nevertheless, key analyses condition on peq thresholds (peq > 0.6/0.8/0.9) to define “high confidence” spiral subsamples and to quote sensitivity. Using uncalibrated, overconfident probabilities to define HC cuts undermines the interpretability of those cuts and of the derived injection floors.
Required fix: Calibrate the equivariant probabilities (Catalog C) against an external validation set (e.g., Platt/temperature scaling on a held-out GZ1 subset) and report reliability curves (ECE/Brier). Redefine HC cuts using calibrated probabilities or quantiles of empirical accuracy. Recompute Table V on the redefined HC sample, or explicitly caveat that peq is not probabilistically calibrated and report calibration diagnostics.

P4-META-E4
Severity: ESSENTIAL
Section/page: Table I, row (i) (p.4) vs. Sec. IV C.a (p.6)
Why missed: Reviewers checked other table inconsistencies but not this mask-status mismatch for the primary estimator.
Specific problem: Table I lists Mask = “none” for the primary real-space dipole, but Sec. IV C.a clearly states the fit is performed on pixels with Nspiral(p) ≥ 10 (the canonical mask). This is a material cross-reference inconsistency for the headline estimator.
Required fix: Correct Table I row (i) to “canonical mask (Nspiral ≥ 10), fsky = 0.49005” (or the exact value used) and include Nmap-weighted if applicable. Confirm that the quoted +0.43σ, p = 0.30 are indeed on that mask.

P4-META-M1
Severity: MAJOR
Section/page: Sec. IV D/Table IV (p.8) and surrounding text
Why missed: One reviewer questioned N = 500 precision, but not the statistical handling of the “99.32%” figure itself.
Specific problem: The “99.32% reproduction” claim for the monopole+mask generative null reports the per-realization scatter (±0.40 percentage points) but not the uncertainty on the mean reproduction fraction (SE ≈ 0.40/√500 ≈ 0.018 pp). It is ambiguous whether the 99.32% is a mean-of-ratios or ratio-of-means; the two are not equivalent under skew. Without a clear estimator definition and CI, “reproduces 99.3%” overstates precision.
Required fix: Specify whether you average (C1,null / C1,data) per realization or take ⟨C1,null⟩/C1,data. Quote the standard error of the mean (or a bootstrap CI) on the reproduction percentage. If mean-of-ratios is used, justify it and show it agrees with ratio-of-means within stated uncertainty.

P4-META-M2
Severity: MAJOR
Section/page: Sec. III C (p.4–5), Sec. IV E (p.9), Appendix B.d (p.13)
Why missed: Others suggested adding vertical-flip TTA, but not the logical redundancy between TTA-imposed equivariance and the flip-consistency loss/metric used for validation.
Specific problem: The paper both enforces flip-equivariance by 2-fold TTA (“flip-swap correlation = 1.000 by construction”) and also uses a flip-equivariance consistency loss during training and a flip-swap test (T1) as a bias-hardening “pass.” If equivariance is enforced at inference by averaging, T1 does not test a property of the trained model—it tests the post-processed protocol and is tautologically satisfied. This blurs what T1 validates.
Required fix: Clarify that T1 is a protocol implementation check (guards against code defects), not a scientific bias test of the learned model. If you wish to demonstrate inherent model equivariance (independent of TTA), report T1 before TTA (single-pass predictions) as well.

P4-META-M3
Severity: MAJOR
Section/page: Appendix A/Table VI (p.12), Sec. IV C.b (p.6–7)
Why missed: Prior reviews flagged fsky bookkeeping elsewhere but not this normalization subtlety.
Specific problem: f_eff,sky is defined using means over the full sky with unnormalized integer weights Wp (Nall or Nspiral). In the pseudo-Cℓ context, the usual definition normalizes weights to [0,1] or uses sums over in-mask pixels (Σw)^2/(Σw^2 Npix) consistently. Using global-sky means with large-integer weights can make f_eff,sky depend on pixel size and absolute count scale. The reported values (e.g., 0.452 for Wp = Nall) are therefore hard to interpret and compare across masks and apodizations.
Required fix: State explicitly the normalization convention for W and f_eff,sky, and report the alternative, mask-restricted (Σp∈mask w)^2/(Σp∈mask w^2) version. Ensure the chosen convention matches the one NaMaster uses internally when computing coupling/debiasing.

P4-META-M4
Severity: MAJOR
Section/page: Sec. IV B (p.5), “spatial uniformity across 7 slabs”
Why missed: Others asked for numeric reporting, but not the core assumption underlying the conclusion.
Specific problem: The claim that the Catalog C monopole “is spatially uniform across 7 equatorial coordinate slabs” is used to argue it cannot induce a real-space dipole. However, a uniform-in-RA slab test is not invariant to the survey’s highly anisotropic mask; a constant offset coupled to varying slab completeness can still bias a dipole fit (especially with uniform pixel weights). Without reporting slab-by-slab counts/weights or masking, the “uniformity” statement is weaker than implied.
Required fix: Provide per-slab fCW ± σ and the corresponding Nspiral (or weighted means) and demonstrate that the uniformity conclusion is robust under mask-weighted slab statistics (or use equal-area/equal-weight partitioning). Alternatively, show directly that adding a constant monopole to randomized Ap realizations does not bias the real-space dipole estimator.

P4-META-m1
Severity: MINOR
Section/page: Sec. VII a (p.11), injection through MASTER vs real-space
Why missed: Others focused on canonical/apodized inconsistencies, not on estimator-mixing in sensitivity claims.
Specific problem: The Conclusions use a harmonic-channel injection–recovery completeness (e.g., P(≥3σ) = 0.92 at Ap = 0.5%) to argue the channel would be “unmissable,” then use a real-space injection floor (A50 ≈ 0.75%) as the “consistency boundary.” Mixing floors across different estimators (with different nulls and weights) conflates distinct sensitivities.
Required fix: Separate estimator-specific sensitivity floors (real-space vs MASTER) and avoid using one channel’s completeness to argue about the other’s detection power. Provide a short mapping (or an explicit caveat) if you retain both.

P4-META-m2
Severity: MINOR
Section/page: Sec. IV D footnote 1 (p.6–7)
Why missed: Others checked numbers but not the modeling assumption behind independence.
Specific problem: The monopole+mask generative null assumes pixelwise independent Binomial(Nspiral(p), pglobalCW). Real data have spatially correlated morphology/PSF/depth fields; independence can underestimate null variance for low-ℓ power and overstate “percent reproduced.” You allude to coherent low-ℓ residuals elsewhere, but not here.
Required fix: Acknowledge this limitation and, if feasible, add a correlated generative null (e.g., draw pCW from a slowly varying Gaussian process constrained by depth/PSF templates) to show robustness of the “≈99.3%” conclusion.

P4-META-n1
Severity: NIT
Section/page: Abstract (p.1), Sec. I (p.1–2)
Why missed: Others debated language, not the global claim framing.
Specific problem: “The headline scientific result is a real-space chirality dipole consistent with null” is clear; however, later the text repeatedly uses “systematics-attributed residuals” without a compact definition. For a non-specialist, it is not obvious what “systematics-attributed” operationally means (diagnostic-only channel? excluded from cosmological inference?).
Required fix: Define once (Methods or Significance conventions) what qualifies as “systematics-attributed,” e.g., “channels that (i) rely on patchy, depth-weighted footprints and (ii) fail ≥2 of the eight diagnostics; these are excluded from cosmological inference and used solely for systematics diagnosis.”

Meta-review recommendation
MAJOR REVISIONS

Given the union of all six reviews, there are multiple essential/major blockers: (i) internal inconsistency and bookkeeping around the harmonic-channel/canonical-mask numbers, (ii) presence of version-history/audit prose in the main text, (iii) ambiguous/possibly mis-specified nulls (especially for the primary real-space estimator), (iv) lack of axis-conditioning in real-space injection–recovery, and (v) severe probability miscalibration feeding into “high-confidence” selection and sensitivity claims. My confidence that the paper could survive external PRD referee rounds after addressing these points is moderate-to-high, because the core scientific result (a real-space null) is likely robust; however, the statistical framing and reporting must be tightened substantially to meet PRD standards.