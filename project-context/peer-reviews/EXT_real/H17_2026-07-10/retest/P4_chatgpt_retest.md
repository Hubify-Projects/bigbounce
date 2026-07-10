(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Section IV C, “Pre-registration of the 0.6 cut”: the confidence threshold is outcome-determining—the reported dipole changes from z≃4.0–4.3 for the full/p
eq
	​

≤0.5 selections to z=0.41 for p
eq
	​

>0.6. A commit in the authors’ own mutable repository, without a frozen time-stamped archive, documented blinding, or an independent analysis registration, does not establish prospective pre-specification; moreover, the manuscript explicitly justifies 0.6 by the observed transition in the dipole statistic. The primary selection must be defined from external validation before inspecting the sky result, or the full threshold scan must be incorporated into the inference. 

h17b_P4

[MAJOR] Section III D and Appendix B, rotational invariance: the production classifier is made reflection-equivariant but not rotation-invariant, even though chirality is invariant under in-plane rotations. The manuscript reports that 21.4% of hard argmax labels change between Z
2
	​

 and D
4
	​

 averaging and that the hard-label CW fraction shifts by −1.35% and +2.11% in two small tests—larger than the claimed 0.75% sensitivity floor. Since the cosmological estimator uses hard argmax labels, the approximately 2,000-object checks do not bound orientation-dependent bias at the required sub-percent level; production-scale D
4
	​

 or continuously rotation-equivariant inference is required.

[MAJOR] Sections II and VI B, physical transfer calibration: the independent chirality accuracy is only 69.91%, approximately 19% of human-labeled spirals are triaged into “not spiral,” the confidence scores are strongly miscalibrated, and the primary cut retains only about 30% of predicted spirals. The injection-recovery analysis begins after classification by modifying the observed hard-label field; it does not propagate a signal through the images, classifier, not-spiral triage, confidence cut, or spatially varying depth/PSF/morphology response. Consequently, A
50
	​

 and A
95
	​

 are efficiencies of an observed-label estimator, not calibrated limits on a physical galaxy-chirality dipole.

[MAJOR] Abstract, Table I, and Appendix D, the z≃−7.6 “clean 1.7% dipole” disfavor statistic: this result is inconsistent with the manuscript’s own dilution model. Using its stated g=0.398, a true 1.7% physical dipole would produce an observed-label amplitude of approximately 0.398×1.7%=0.68%; compared with 0.455%±0.163%, the difference is about 1.4σ, not 7.6σ. If 1.7% is instead treated as an already-classified amplitude in this pipeline, it cannot be directly compared with the output of Shamir’s different classifier and selection. The claim that ignoring classifier dilution is “conservative” is backwards.

[MAJOR] Appendix D, statistical construction of the z≃−7.6 result: subtracting a reference amplitude from the bootstrap standard deviation of the positive-definite dipole norm is not a calibrated hypothesis test. The dipole amplitude has a non-Gaussian distribution, the signal direction is unspecified, and the bootstrap distribution is centered on the observed estimate rather than generated under A=A
ref
	​

. A valid comparison requires signal-injected realizations or a likelihood profiling the three dipole components, direction, survey covariance, and nuisance parameters under the reference model.

[MAJOR] Section IV D, treatment of the unresolved harmonic residual: the assertion that the unmodeled residual “does not affect” the main result because it lies below A
95
	​

 is invalid. A
95
	​

 is a detection-efficiency threshold, not an upper bound on systematic bias, and an additive systematic dipole can cancel a physical dipole as well as enhance it. The manuscript’s repeated claim that inherited or survey-correlated structure can only move the estimator away from null is false for vector-valued dipoles.

[MAJOR] Section IV D, quantitative “53% explained / 47% remaining” claim: the reported fraction is computed by subtracting scalar amplitudes despite a stated alignment of only cosθ≃0.84. With ∣a
obs
	​

∣=6.95×10
−3
 and ∣a
sys
	​

∣=3.75×10
−3
, the residual vector has magnitude

∣a
obs
	​

∣
2
+∣a
sys
	​

∣
2
−2∣a
obs
	​

∣∣a
sys
	​

∣cosθ
	​

≃4.3×10
−3
,

about 62% of the observed amplitude; the modeled component parallel to the observation is only about 45%. The stated 47% remainder and all bounds derived from it are therefore numerically incorrect.

[MAJOR] Sections IV C–IV D, Table V, and Appendix A, unresolved estimator conflict: the same catalog produces a 0.41σ real-space result, 7.28σ and 7.93σ harmonic results, and a separate 3.64σ canonical result. Different masks, weights, fields, and nulls can change sensitivity, but they do not make measurements of the same low-ℓ sky structure logically independent. The manuscript alternately describes the 3.64σ and 7.93σ calculations as a recomputation of the same canonical field and as different field conventions. A common-sample, common-mask simulation study with the cross-estimator covariance is required before the harmonic anisotropy can be dismissed as irrelevant to the real-space null.

[MAJOR] Appendix D, “eight-anchor” systematics attribution: this is not a statistical model comparison. The diagnostics are correlated, several use only 50–200 Monte Carlo realizations, no joint likelihood or multiplicity correction is supplied, and some tests only exclude narrow artifact variants. In particular, comparing standardized values such as σ
ℓ=2
	​

>σ
ℓ=1
	​

 is not a test of whether the raw joint spectrum is inconsistent with an injected dipole, and a 2.89σ cross-spectrum feature from 200 permutations is insufficient for categorical attribution.

[MAJOR] Appendix D, nuisance-marginalized WLS claim: the displayed nine-template design is exactly rank-deficient and does not contain the depth, PSF, extinction, or per-galaxy morphology variables that the text later says were jointly marginalized. The 24-template extension adds imaging-leg–confidence interactions, not a full conditional depth/morphology calibration, while the separate forward model is not part of the bootstrap likelihood. Calling the resulting fit “joint nuisance-marginalized” and promoting it to a primary cosmological estimator is unsupported.

[MAJOR] Section IV C, null calibration: permutation of pixel asymmetries assumes exchangeability despite large variations in pixel counts, depth, morphology, and classifier reliability. The per-galaxy label-shuffle cross-check preserves pixel totals but still destroys spatially varying confusion rates and confidence-dependent selection. Because both the predicted-spiral mask and the p
eq
	​

 cut depend on the classifier and imaging conditions, a valid null must condition on those quantities or use survey/image-level mocks with the complete selection function.

[MAJOR] Section VI B, sensitivity and exclusion language: the quoted A
95
	​

 is an axis-averaged 3σ recovery probability based on only 100 injections per amplitude and a coarse amplitude grid; it is neither a confidence interval nor a direction-independent upper limit. On this highly anisotropic footprint, a physical exclusion requires component-level covariance or completeness as a function of dipole direction, including the least-sensitive directions. The ten-axis spot check at one amplitude is inadequate.

[MAJOR] Section VI A, GZ1-human-only cross-check: with N≃4.6×10
4
, the manuscript itself estimates sensitivity only at several-percent amplitudes, and those thresholds are extrapolated by N
−1/2
 scaling rather than measured on the actual GZ1 footprint. This test therefore cannot establish independence from pseudo-label inheritance at the sub-percent scale of the headline result. The same section also contains a unit error by describing A
95
	​

, which is already defined in A
p
	​

 units, as a percentage in f
CW
	​

 requiring an additional factor of two.

[MAJOR] Sections IV C, IV E, and Appendix E, interpretation of the low-confidence signal: confidence selection changes the galaxy population in redshift, apparent size, surface brightness, morphology, and survey depth. The disappearance of the signal above p
eq
	​

=0.6 is therefore not by itself evidence that the lower-confidence result is instrumental; a physical signal confined to a different redshift or morphology population would behave similarly. The high- and low-confidence samples must be matched or reweighted in observable properties before this distinction can be made.

[MAJOR] Section VI C, theory interpretation: without a transfer function from primordial parity-violating physics to projected spiral-arm morphology, the manuscript cannot claim that cosmic birefringence or gravitational Chern-Simons models generically predict this observable, nor that the reported recovery threshold constrains those theories. These statements should be removed unless an explicit model calculation is supplied.

[MINOR] Data Availability: the analysis is tied to a live repository branch, while the immutable release, exact commit hashes, checksums, and Zenodo DOI are promised only for the future. This is inadequate for an analysis whose claims rely on commit chronology, thousands of unprinted simulation products, and distinctions between several closely related estimator implementations.

[MINOR] Title and abstract: “8.5 million DESI galaxies” is the parent image catalog, whereas the claimed primary cosmological result uses 949,584 high-confidence predicted spirals; the full predicted-spiral sample is 3,201,160. These three sample sizes must be distinguished prominently, and the uncalibrated z≃−7.6 statistic should not be foregrounded.

[MINOR] Presentation: the manuscript repeatedly restates caveats and conclusions while retaining contradictory descriptions of samples, field conventions, units, and estimator status. A publishable version would require substantial condensation and a single fixed analysis table defining, for every claimed result, the exact sample, mask, field, weighting, null, and inferential meaning.

(3) The central claim is supported only as a descriptive non-detection in the selected high-confidence hard-label map, not as a calibrated constraint on the underlying physical galaxy-chirality dipole.
