VERDICT: MAJOR REVISIONS

ISSUES:

[MAJOR] Sections III B and IV C, claim that the p
eq
	​

>0.6 primary sample was pre-specified: this threshold is also the first cut at which the reported 4.0–4.3σ full-sample excess collapses, yet no independent preregistration, frozen tag, blinded protocol, or pre-unblinding purity–completeness criterion is provided. A repository commit containing both the estimator and cut does not independently establish that the choice preceded inspection of the sky statistic. The threshold scan must either be incorporated into the null/trials accounting or the sample must be defined from external validation alone. 

ext_P4_M35

[MAJOR] Section IV C, calibration of the primary null: uniformly permuting A
p
	​

 assumes exchangeable pixels despite strongly varying N
spiral
	​

(p), noise, depth, footprint geometry, and classification quality. The per-galaxy label shuffle preserves counts but still assumes a spatially invariant labeling mechanism and removes precisely the depth-, morphology-, and confidence-dependent biases that the manuscript later identifies. Agreement between two invalidly simplified nulls does not calibrate the p=0.31 test for the composite hypothesis “no cosmological dipole in the presence of survey systematics.” A conditional likelihood or forward simulation preserving the measured spatial selection and confusion structure is required.

[MAJOR] Sections IV C–E and Appendix D, unresolved non-null structure: the unthresholded real-space map gives 4.2–4.4σ, the hemisphere scan rejects the random-label null at p
LEE
	​

≤10
−4
, and the MASTER channel gives large moment-z residuals, while approximately 47% of the harmonic dipole amplitude remains unexplained by the proposed templates. Declaring these results “diagnostic” rather than “primary” is an analysis hierarchy, not evidence that they are non-cosmological or that the confidence cut has not attenuated a real signal. A joint model must predict all samples and estimators, preferably with an independent validation region, before a clean null can be claimed. 

ext_P4_M35

[MAJOR] Section VI B and Table VIII, injection–recovery claim: the injection is made into the already classified hard-label field and therefore bypasses the image classifier, the not-spiral triage, the confidence selection, and the spatially varying confusion matrix. The full-catalog mirror experiment verifies the algebraic equivariance of the TTA protocol; it is not an injection of a population-level chirality dipole through the complete measurement pipeline. Consequently, A
50
	​

 and A
95
	​

 characterize only the final observed-label estimator and cannot support the statement that a genuine physical Shamir-scale dipole would necessarily have been detected.

[MAJOR] Sections V and VI B and Appendix D, inconsistent treatment of classifier dilution: under the manuscript’s own transfer factor g≃0.398, a physical dipole of 1.7% would produce an observed-label amplitude of only about 0.68%, while the observed-space A
95
	​

=1.0–1.5% corresponds to a physical threshold of roughly 2.5–3.8%. Thus the lower end of the cited 1.7% range is not demonstrably above the physical detection threshold. Likewise, comparing A
best
	​

=0.455% directly with A
ref
	​

=1.7% while omitting the transfer function is not conservative; under the stated g, the discrepancy would be far smaller. The paper must distinguish latent physical amplitude, this classifier’s observed-label amplitude, and another pipeline’s measured amplitude. 

ext_P4_M35

[MAJOR] Appendix D(g), Table XV, and Fig. 10, z≃−7.6 “template disfavor”: the block-bootstrap distribution is centered on the observed estimate, not generated under A=A
ref
	​

; the dipole amplitude is positive-definite and non-Gaussian; and a dipole of fixed amplitude has an unknown direction that is not handled by the scalar statistic (A
best
	​

−A
ref
	​

)/σ
boot
	​

. This is not a calibrated hypothesis test. A three-component dipole likelihood, profiling or marginalizing over direction and nuisance parameters, with simulations generated under A
ref
	​

, is required. The fact that this fit uses the full catalog rather than the primary high-confidence selection is an additional mismatch.

[MAJOR] Section II and Appendix B, classifier validation and pseudo-label independence: 66.5% of the training labels come from CE-ResNet, while the purportedly independent GZ1 set is stated to be disjoint from the 6,637 GZ1 training objects but is not demonstrated to be disjoint from the CE-ResNet pseudo-labeled training images. The random train/validation split is also not spatially blocked. More importantly, the external chirality accuracy is only 69.91%, and the two-leg confusion analysis allows differential-error uncertainties of approximately 0.6–1.4 percentage points, comparable to or larger than the claimed sub-percent sensitivity. A truly held-out, spatially representative human-labeled validation set and a spatially resolved confusion model are needed; the assertion that errors can only dilute a signal is not established.

[MAJOR] Section VI A, interpretation of the GZ1-human-only cross-check: the manuscript itself estimates A
50
	​

≃3.4% and A
95
	​

≃4.5–6.8% for this sample. It therefore has essentially no power to validate the sub-percent headline result or to exclude sub-percent pseudo-label inheritance. It may be reported as a coarse consistency check against very large dipoles, but not as evidence that the high-precision null is model-independent.

[MAJOR] Sections III A and IV C, Table V, and Appendix A, inconsistent estimator and significance conventions: the nominally canonical ℓ=1 channel appears as +3.64 moment-z with empirical p=0.030 and as +7.93 moment-z with empirical p=3×10
−4
, after changes in field normalization, mean subtraction, weights, and Monte Carlo construction. Because the null is explicitly heavy-tailed, moment-z should not be presented as a Gaussian “sigma” significance; the empirical rank p is the calibrated quantity. One frozen estimator convention should be selected, and the large convention dependence must be explained rather than labeled non-comparable.

[MAJOR] Sections VI B–C and VII, absence of a statistical amplitude limit: A
95
	​

 is a detection-efficiency threshold, not a confidence or credible upper limit, yet the manuscript repeatedly uses it as a “bound,” “ceiling,” and basis for exclusion statements. A confidence interval or posterior for the dipole vector, with confidence selection and survey/classifier nuisance parameters included, is required. Claims about primordial parity-violating sectors and statements that a future detection would “falsify” this result should be removed or sharply limited until a physical transfer function and matched population definition exist.

[MINOR] Appendix B(g), calibration calculation: the proposed ECE lower bound compares the mean confidence of the entire 8.47-million-object catalog with the accuracy of a selected GZ1 cross-match. Jensen’s inequality provides that bound only when confidence and accuracy are evaluated on the same population. The calibration statistics must be recomputed entirely on the matched validation sample.

[MINOR] Data Availability and presentation: the analysis currently depends on a mutable main branch and a future DOI placeholder rather than an immutable archival release. The exact catalog, model, scripts, null arrays, and hashes must be frozen before publication. The manuscript also requires substantial compression and harmonization of the competing “canonical mask,” field-normalization, amplitude-unit, and significance conventions.

The central claim is not yet supported: the manuscript establishes only that the selected p
eq
	​

>0.6 hard-label map is non-significant under the authors’ own permutation test, not a robust sub-percent physical chirality-dipole null or exclusion of Shamir-scale signals.
