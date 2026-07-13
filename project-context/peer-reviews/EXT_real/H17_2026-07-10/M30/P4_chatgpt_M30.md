# P4 (chirality catalog) — ChatGPT EXT review — round M30

- Reviewer: ChatGPT (project: big-bounce-book), Physical Review D referee prompt
- Chat URL: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a54e89d-95b4-83e8-a395-cd71c17b2b07
- Attached PDF: ext_P4_M30.pdf
- Harvested: 2026-07-13 (recovered from silent-exit orphan; send landed server-side, review completed)
- VERDICT: MAJOR REVISIONS

## Raw reviewer response (verbatim)

```
(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

[MAJOR] Sections III B and IV C, primary-sample definition — The headline null depends on the p
eq
	​

>0.6 cut, which retains only 949,584 of 3.20×10
6
 classified spirals, while the unthresholded catalog gives a 4.2–4.4σ dipole. The cut lies precisely at the transition between the significant and null regimes. A commit in the same evolving analysis repository is not an independent preregistration, especially when no frozen tag or timestamped analysis plan existed; the threshold must either be justified solely from external validation before examining sky statistics, or the confidence scan and associated selection freedom must enter the inference. 

ext_P4_M30

[MAJOR] Abstract, Section VI B, and Conclusions, physical sensitivity — The injection–recovery exercise injects a dipole into the already classified hard-label field; it does not propagate a physical chirality signal through the classifier, the not-spiral triage, or the confidence selection. Thus A
50
	​

≃0.75% and A
95
	​

∈(1.0%,1.5%] are observed-label thresholds, not physical galaxy-chirality thresholds. Using the manuscript’s own transfer factor g≃0.398, these correspond approximately to physical amplitudes of 1.9% and 2.5%–3.8%, respectively, contradicting the repeated claim that a genuine 1.7% physical dipole would have been recovered with near-unit probability.

[MAJOR] Section VI B, claimed “image-level end-to-end” validation — Mirroring every image and verifying that equivariant TTA swaps CW and CCW tests implementation symmetry; it is not an end-to-end injection of a small, spatially varying population dipole. It does not measure the response of spiral selection, confidence cuts, morphology-dependent failures, or sky-dependent confusion to a physical change in the CW/CCW population. A genuine end-to-end calibration requires injecting controlled sky-dependent chirality perturbations before classification, or constructing and validating a spatially conditioned transfer matrix.

[MAJOR] Section IV C, real-space estimator and null — Uniformly fitting pixel asymmetries and permuting A
p
	​

 between pixels assumes exchangeability despite large variations in N
spiral
	​

(p), depth, morphology, and label quality. The per-galaxy shuffle is a useful check but still conditions on the potentially biased observed labels and does not supply a physical covariance model. The primary analysis should use an individual-galaxy or binomial-count likelihood with the actual selection function, heteroscedastic noise, spatial covariance, and survey-systematic nuisance fields included explicitly.

[MAJOR] Sections III A, IV C, and VI B, significance calibration — Quantities called “σ” are often only moment ratios and are demonstrably not Gaussian significances: for example, z=7.31 accompanies rank p=6×10
−4
, and z=3.64 accompanies p=0.030. These should not be quoted as 7.3σ and 3.6σ detection-equivalent results. The injection criterion z
moment
	​

>3 is likewise uncalibrated; Table VIII already gives approximately a one-percent exceedance rate at nearly zero injection, far larger than a nominal one-sided 3σ false-positive rate. Recovery must be defined using empirical null quantiles at a fixed Type-I error, with enough null realizations to resolve that tail.

[MAJOR] Appendix D and the claimed z≃−7.6 exclusion — The block bootstrap is centered on the observed estimate and is not a sampling distribution generated under A
ref
	​

=0.017. Computing (A
best
	​

−A
ref
	​

)/σ
boot
	​

 for the positive-definite dipole amplitude, with an unspecified signal direction and incompletely modeled nuisances, is not a calibrated hypothesis test or confidence interval. Since the manuscript itself concedes this, the statistic cannot be designated a “primary cosmological estimator.” A profile likelihood, posterior, or signal-injection test under A
ref
	​

, including direction and nuisance marginalization, is required.

[MAJOR] Sections IV C–IV E and Appendix D, unresolved non-null structure — The full catalog has a 4σ-level real-space excess, the MASTER channels have highly significant empirical departures from their random-label nulls, and the hemisphere maximum rejects that null at p
LEE
	​

≤10
−4
. Labeling these channels “diagnostic” does not statistically reconcile them with the selected-sample null. Moreover, the forward model accounts for only about 53% of the harmonic residual amplitude, leaving approximately 47% explicitly unexplained. Until a joint model shows that the same survey effects produce these observations while preserving recovery of an injected physical dipole, the defensible conclusion is only “no significant dipole in the selected high-confidence estimator,” not a general null chirality dipole.

[MAJOR] Sections II, VI A, and Appendix B, classifier validation and spatially varying errors — The independent GZ1 comparison gives only 69.91% chirality accuracy and 58.7% three-class accuracy, while the softmax outputs are severely overconfident. The two-leg confusion analysis leaves confidence-interval widths of order 0.6 percentage points in the science sample, comparable to the amplitudes being constrained, and cannot exclude RA-dependent or finer depth/morphology-dependent differential errors within a leg. Such errors can either create or cancel a dipole; they are not necessarily conservative. A representative independent labeled set and a spatially resolved confusion/selection model must be propagated into the dipole likelihood.

[MAJOR] Section III D and Appendix B, rotational dependence — Production inference averages only the identity and one horizontal reflection, whereas the manuscript reports that 21.4% of hard argmax labels change between Z
2
	​

 and D
4
	​

 averaging on the tested samples. Because the science statistic uses hard labels rather than mean soft probabilities, the small change in mean P
CW
	​

 does not establish rotational stability of the estimator. Full-catalog D
4
	​

 inference, or a much stronger position-angle-, PSF-, and imaging-leg-stratified validation, is needed.

[MAJOR] Section VI A, human-label-only cross-check — The GZ1-only test has only 4.6×10
4
 objects and an estimated A
50
	​

 near 3.4%, with A
95
	​

 of roughly 4.5%–6.8%; those sensitivities are themselves obtained by simple N
−1/2
 scaling rather than direct injection. It therefore cannot test the sub-percent pseudo-label-inheritance problem relevant to the headline sample. Statements that this test “establishes” or “confirms” independence of the sub-percent null must be replaced by the narrower statement that it excludes only much larger human-label dipoles.

[MAJOR] Sections IV D, VII, and Appendix A, inconsistent harmonic implementations — The manuscript reports +3.64 and +7.93 moment-z values for canonical unapodized ℓ=1 analyses, alternately describing the latter as a recomputation of the same field and as a distinct estimator with different coupling and subtraction conventions. A constant field rescaling cannot change z, and increasing the null ensemble alone should not produce such a factor-of-two shift. A controlled, side-by-side calculation with identical field, mask, monopole subtraction, weights, coupling matrix, binning, and randomizations is necessary before either result can support the systematic interpretation.

[MAJOR] Sections IV D, VI A–VI C, and Conclusions, misuse of recovery thresholds as bounds — A
50
	​

 and A
95
	​

 are detection-efficiency crossings, not confidence limits on the amplitude in the observed data. They cannot justify statements that an unresolved component “must lie below” a given amplitude, that the harmonic remainder is statistically bounded, or that a future measurement would “falsify this null.” The paper needs a coverage-calibrated upper limit under a stated signal-plus-systematics model, or all bound, ceiling, exclusion, and falsification language must be removed.

[MINOR] Section VI C, theoretical interpretation — The discussion of cosmic birefringence and Chern–Simons gravity suggests that these mechanisms would generically produce a galaxy-morphology dipole, but no transfer calculation is supplied. The manuscript should restrict itself to the measured projected-morphology observable and avoid model constraints until a quantitative galaxy-formation transfer function is derived.

[MINOR] Data Availability and Appendix B, release integrity and presentation — The archival DOI and immutable commit are still placeholders, and 2.9% of catalog rows—including 6.3% of the high-confidence sample—are affected by inconsistent raw/equivariant inference passes producing reconstructed probabilities outside [0,1]. The public catalog should be regenerated from a single consistent inference pass and frozen before publication. The manuscript should also be substantially shortened: repeated estimator hierarchies, disclaimers, internal artifact paths, and multiple inconsistent significance conventions currently obscure rather than clarify the scientific argument.

(3) The central claim is not supported as stated: the analysis supports only a null result for one confidence-selected observed-label estimator, not a physically calibrated null or exclusion of a 1.7% galaxy-chirality dipole.
```
