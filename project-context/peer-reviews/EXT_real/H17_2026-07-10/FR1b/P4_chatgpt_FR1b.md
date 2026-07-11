(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Sections III B and IV C, definition of the “primary” sample: the p
eq
	​

>0.6 cut retains only 949,584 of 3,201,160 classified spirals and is exactly the point at which the reported real-space significance collapses from z≃4.0−4.3 to z=0.41. A commit containing both the cut and estimator is not an independent preregistration, and the manuscript explicitly justifies 0.6 using the observed transition in the significance sweep. The primary sample must be selected from independent validation information or a genuinely blinded protocol; otherwise the headline null is vulnerable to outcome-dependent selection. 

ext_P4_FR1b

[MAJOR] Section II B and Appendix B, classifier validation: 66.5% of the training labels are CE-ResNet pseudo-labels, while the nominal 93.7% validation accuracy comes from a random split of this mixed label set and therefore largely measures reproduction of pseudo-labels rather than physical chirality accuracy. The independent GZ1 agreement is only 69.91% with κ=0.40, and no representative DESI-wide validation resolves the confusion matrix jointly in position, depth, seeing, morphology, magnitude, and imaging leg. A global or two-leg confusion matrix cannot exclude a spatially varying error field that either creates or cancels a dipole.

[MAJOR] Sections V and VI B and Appendix D, comparison with a 1.7% physical dipole: the claimed z≃−7.6 disfavor is inconsistent with the manuscript’s own classifier-dilution model. Using its stated full-sample transfer factor g=0.398, a physical A=0.017 dipole would appear in the classifier-output field with A
obs
	​

≃0.00677, not 0.017; with A
best
	​

=0.00455 and σ
boot
	​

=0.00163, the corresponding discrepancy is only about −1.4σ, not −7.6σ. Likewise, the observed-label A
95
	​

=1.0%−1.5% corresponds to a physical threshold of approximately 2.5%−3.8% under the same mapping, so the lower 1.7% Shamir amplitude is not demonstrated to be “unmissable.” If 1.7% is instead defined directly in the classifier-output field, it is not a physical-sky comparison between the two pipelines.

[MAJOR] Section IV C, primary null distribution: randomly permuting A
p
	​

 among pixels assumes exchangeability, although Var(A
p
	​

) varies strongly with N
spiral
	​

(p), depth, morphology, and classifier quality. Uniform-pixel least squares makes this heteroskedasticity directly relevant. The per-galaxy shuffle cross-check preserves pixel counts but still destroys spatially correlated classification errors, intrinsic spin correlations, and survey-dependent confusion. The primary inference should use a binomial or galaxy-level likelihood with the exposure counts, spatial nuisance terms, and a covariance model that preserves angular correlations.

[MAJOR] Appendix D, block-bootstrap WLS “exclusion”: Figure 10 explicitly shows a bootstrap distribution around the observed estimate, not a sampling distribution generated under A
ref
	​

=0.017, so (A
best
	​

−A
ref
	​

)/σ
boot
	​

 is not a calibrated hypothesis-test statistic. The fitted amplitude is a positive norm of three coefficients, the alternative has an unspecified axis, and nuisance parameters are composite. In addition, resampling ∼7
∘
 blocks cannot by itself establish the covariance of a global ℓ=1 mode when the data exhibit coherent low-ℓ residuals. A likelihood-ratio or simulation-based test under injected reference dipoles, with axes and nuisances profiled or marginalized, is required.

[MAJOR] Sections IV C–IV D, unresolved non-null structure: the unthresholded catalog gives a z≃4.2−4.4 real-space dipole, while the harmonic analyses give z≃7 residuals. The proposed imaging-plus-morphology model reproduces only about 53% of the residual amplitude, leaving roughly 47% unexplained. The eight diagnostic “anchors” make a survey origin plausible but do not establish it: the cross-spectrum is only suggestive, the template closure is incomplete, and several diagnostics use different samples or estimators. An unexplained coherent residual cannot be removed from the scientific inference merely by designating that channel “diagnostic.”

[MAJOR] Section IV D, use of A
50
	​

 and A
95
	​

: a recovery-probability threshold is not an upper limit on a real signal or systematic, and being below A
50
	​

 does not imply that a component is harmless or cannot partially cancel another dipole. The manuscript also compares the full-catalog harmonic residual, converted to 0.695%, with the high-confidence real-space threshold A
50
	​

=0.75%, despite repeatedly stating that recovery thresholds are estimator- and sample-specific. Its own full-sample real-space calibration gives A
95
	​

≃0.63%, so the same 0.695% quantity is not below that matched sample’s quoted threshold.

[MAJOR] Table V, Appendix A, and Section VII, MASTER estimator inconsistency: the manuscript alternates between a “canonical” +3.64σ result and a “canonical” +7.93σ result, with different fields, monopole subtraction, weighting, permutation construction, and coupling treatment. Increasing the Monte Carlo count from 500 to 10
4
 cannot account for this change; they are materially different estimators, not confirmations of one result. One field definition, mask, weighting, subtraction convention, and null must be fixed and all robustness calculations rerun under it.

[MAJOR] Section III D and Appendix B, equivariance of the quantity actually analyzed: Equation (2) guarantees Z
2
	​

 equivariance of soft scores, but the dipole uses hard argmax labels, and 21.4% of labels change between Z
2
	​

 and D
4
	​

 TTA in the reported holdouts. Stability of the mean soft probability does not demonstrate stability of the hard-label sky map. Moreover, 59,515 high-confidence rows have reconstructed flip-pass probabilities outside [0,1] because raw and equivariant columns came from inconsistent inference passes. The production catalog should be regenerated from a single auditable pass, and the primary sky analysis should be repeated with D
4
	​

 TTA or a genuinely rotation-equivariant architecture.

[MAJOR] Section VI A, GZ1-human-only cross-check: the 46,017-object sample has an estimated A
50
	​

 of several percent and therefore has essentially no power to test the sub-percent structure relevant to the headline result or a 1.7% physical dipole. The quoted sensitivity is obtained by approximate N
−1/2
 scaling rather than injection on the actual sparse footprint, and GZ1 winding labels themselves have known handedness biases. This test is a useful coarse corroboration but does not establish that the high-precision null is independent of pseudo-label inheritance.

[MAJOR] Data Availability and the preregistration/reproducibility claims: the manuscript relies on numerous external JSON arrays and scripts on a mutable live branch, while the immutable tag, exact commit hashes, Zenodo archive, and DOI are still placeholders to be created later. Load-bearing claims—including sample pre-specification, bootstrap percentiles, injection curves, and estimator conventions—cannot be independently verified from the submitted record. The complete frozen archive must exist before review of the quantitative claims can be completed.

[MINOR] Section VI C, theoretical interpretation: the manuscript states that cosmic-birefringence and Chern–Simons scenarios would generically produce or align a galaxy-morphology dipole, while also acknowledging that no transfer function from those theories to projected spiral winding is derived. The model-specific discussion should be removed or reduced to a clearly speculative motivation; the present analysis sets no quantitative constraint on those theories.

[MINOR] Title and abstract, sample size: “in 8.5 million DESI galaxies” is misleading because the primary estimator uses 949,584 selected spirals, while the secondary WLS fit uses 3,201,160 spirals; 8.47 million is the parent image catalog including 5.27 million objects classified as non-spirals. The title and abstract should state the primary analysis sample explicitly.

[MINOR] Section VI B and Table VIII, Monte Carlo precision: 100 injections per amplitude and a 0.5-percentage-point grid near the A
95
	​

 transition are insufficient for a falsification threshold used throughout the conclusions. For example, 91/100 recovery at 1.0% does not statistically establish that the true recovery probability is below 95%. Binomial confidence intervals, substantially larger ensembles, and a finer adaptive amplitude grid are required.

(3) No—the manuscript currently supports only the narrow statement that one post-selected high-confidence classifier-output sample has a null real-space dipole, not the broader claim of a calibrated cosmological null or exclusion of percent-level physical chirality dipoles.
