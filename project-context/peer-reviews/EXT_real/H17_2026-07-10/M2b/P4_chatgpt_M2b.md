(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Section VI B, Table VIII, and the abstract—The quoted A
50
	​

 and A
95
	​

 sensitivities are not calibrated “3σ” detection thresholds. The manuscript explicitly establishes that the positive-definite dipole-amplitude null is non-Gaussian and that moment-z does not map to tail probability, but injection recovery is nevertheless scored by (A
rec
	​

−⟨A
null
	​

⟩)/σ
null
	​

>3. With only 1000 null realizations, the nominal one-sided 3σ tail cannot be resolved reliably. Moreover, the injection begins in the final hard-label map, downstream of the image classifier, not-spiral triage, confidence cut, and spatially varying confusion matrix. Thus these numbers are neither controlled-false-alarm thresholds nor end-to-end sensitivities to a physical chirality dipole, and the abstract’s statement that a genuine Shamir-scale signal “would have been detected” does not follow. 

ext_P4_M2b

[MAJOR] Appendix D and Table XV—the z≃−7.6 “clean 1.7% dipole” disfavor is not a valid physical-signal exclusion. The WLS fit is performed on the full, lower-accuracy catalog, yet A
ref
	​

=0.017 is compared directly with the observed-label amplitude without applying the manuscript’s own classifier transfer factor. Using its stated g=2a−1=0.398, a physical 1.7% dipole would produce approximately 0.017g=0.0068 in the observed labels, not 0.017; relative to the fitted 0.00455 and σ
boot
	​

=0.00163, this is only about a 1.4σ difference. Omitting attenuation is anti-conservative for excluding a true signal, contrary to the text. In addition, a bootstrap distribution of the positive-definite fitted norm around the observed data is not a calibrated sampling distribution under A=A
ref
	​

; signal-injected simulations or a likelihood for the three dipole components and nuisance parameters are required.

[MAJOR] Sections III B and IV C—the declared analysis hierarchy is internally contradictory and insufficiently pre-specified. The manuscript calls p
eq
	​

>0.6 the “single primary science sample,” while simultaneously elevating a full-catalog WLS fit to primary status. The claimed preregistration consists only of a Git commit that also defines the estimator, with no frozen, independently timestamped analysis plan. The threshold is then justified because the measured excess collapses precisely between 0.5 and 0.6. That is outcome-dependent sample selection unless demonstrated otherwise; a confidence-cut scan does not remove the associated trials factor. The cut must be fixed using independent validation data, or the full cut-selection procedure must be included in the null inference.

[MAJOR] Section IV C—the primary pixel-permutation null is not statistically valid for the survey map. Per-pixel asymmetries are heteroskedastic because N
spiral
	​

(p), depth, morphology, and confidence vary strongly across the footprint, so they are not exchangeable under arbitrary pixel permutation. The per-galaxy label shuffle is preferable but still destroys spatially correlated classifier errors, intrinsic spin correlations, and survey-correlated residuals; the injection simulations similarly assume independent binomial labels. This can substantially understate the variance and overstate sensitivity. A binomial or multinomial object-level likelihood with the actual selection function and a spatial covariance model, or a block-based null applied to the exact high-confidence sample, is needed.

[MAJOR] Section III D and Appendix B—the production classifier is not rotation invariant at the level used by the estimator. Chirality should remain unchanged under in-plane rotations, yet the production pipeline averages only over a reflection pair, and 21.4% of hard argmax labels change between Z
2
	​

 and D
4
	​

 TTA on the tested samples. The reported stability of the mean soft probability at the 1.6×10
−3
 level does not control a dipole made from hard labels. Spatial changes in galaxy position angle, PSF anisotropy, or morphology could therefore induce a directional label bias. The full production catalog should use rotational TTA/equivariance, or the authors must provide a map-level bound on the resulting dipole well below the claimed sensitivity.

[MAJOR] Sections II and VI A and Appendix B—the independent validation does not establish sub-percent directional accuracy. The model-free GZ1 test has an admitted A
95
	​

 sensitivity of roughly 4.5–6.8%, so it cannot validate the headline 0.75–1.5% regime. The leg-stratified confusion analysis constrains differential errors only to approximately 0.6 percentage points in the science cut and 1.4 percentage points in one leg, already comparable to the claimed signal scale, and it is blind to RA-dependent or finer spatial structure within each leg. The broad bias-test thresholds in Table XII are likewise orders of magnitude too loose for sub-percent cosmology, while the flip-swap test is algebraically guaranteed by construction. A sufficiently large, independently and mirror-randomized human-labeled validation set spanning the full footprint is required.

[MAJOR] Sections IV C–IV D—the statistically significant full-catalog structure cannot simply be removed from the scientific inference by declaring it “diagnostic.” The unthresholded real-space estimator gives z≃4.0–4.3, the harmonic channel gives small empirical tail probabilities, and approximately 47% of the post-MASTER amplitude remains unexplained. The assertion that this remainder “does not affect” the null because it lies below A
50
	​

 or A
95
	​

 is logically invalid: a detection-efficiency threshold is not an upper confidence limit, and a signal below A
50
	​

 is not thereby absent. The same-sample real-space, harmonic, and template estimators need to be analyzed in one coherent likelihood with systematic components rather than assigned different scientific roles after producing discrepant outcomes.

[MAJOR] Section III A, Table V, and Conclusion VII c—the manuscript repeatedly reports moment-standardized deviations as “σ” despite demonstrating that the nulls are strongly non-Gaussian. For example, p=0.030 is approximately 1.88 Gaussian σ, not 3.64σ, while p=6.0×10
−4
 is approximately 3.24σ, not 7.31σ. The canonical results also move from +3.64 to +7.93 under analyses both described as canonical; changing the number of Monte Carlo draws cannot explain such a shift, and the differing field, subtraction, and null conventions must be reconciled rather than presented as parallel “σ” values. Exact empirical p-values and calibrated confidence levels should replace moment-z significance language throughout.

[MAJOR] Appendix D and Tables VII and XV—the claimed nuisance marginalization and systematic attribution are incomplete. The primary nine-template WLS design contains dipole components, imaging-leg fractions, density, density squared, and a constant; it does not jointly include the PSF, depth, extinction, or actual morphology fields invoked in the text. The later 53% forward model is a separate point fit and is not propagated through the block-bootstrap inference. The design is also exactly rank deficient before an ad hoc leg removal. Consequently, the “eight-anchor” battery does not provide a closed systematic budget, and several anchors merely reject particular alternatives rather than positively identify the residual. A single full-rank joint model with template uncertainties and spatial covariance is required.

[MAJOR] Sections VI A and Appendix D—the assertion that survey-correlated bias can only move the estimate away from zero is false. An additive systematic dipole is a vector and may align or anti-align with a physical dipole; it can therefore enhance, reduce, or cancel the measured amplitude. Likewise, depth-, morphology-, confidence-, and pseudo-label-dependent terms are not demonstrated to have a sign-definite “toward-null” effect. The claimed conclusion that their combined worst case cannot hide a 1.7% signal is unsupported without simultaneous marginalization over their amplitudes and directions.

[MAJOR] Section IV C, Appendix A, Table XVI, and Data Availability contain unresolved reproducibility inconsistencies. Section IV C states that 3,200,420 spirals are inside the canonical mask and 740 are outside it, whereas Table XVI reports all 3,201,160 as in-mask. Appendix A also alternates between calling N
spiral
	​

≥10 and N
all
	​

≥1 the canonical footprint. These are not harmless bookkeeping differences because the masks enter every estimator and covariance. In addition, the submission points to a mutable live main branch and still contains placeholders for the archival DOI and exact commit hashes. The exact catalog, masks, code, random seeds, null arrays, and provenance files must be frozen in an immutable archive before the results can be evaluated reproducibly.

[MAJOR] Section V and the abstract—the quantitative comparison with Shamir is not justified. Equality of amplitude units does not imply equality of estimator response: the samples differ in footprint, redshift and morphology selection, classification accuracy, not-spiral handling, and spatial transfer function. The 99.32% pre-MASTER reproduction is largely the expected projection of an unsubtracted constant field through this manuscript’s own mask and does not demonstrate that another pipeline’s real-space statistic suffered the same effect. The claimed factor-of-3.7–8.8 tension and the assertion that the literature-scale signal would be unmissable should be removed unless a matched-footprint, matched-selection reanalysis is performed.

[MAJOR] Section VI C—the connection to fundamental parity-violating physics is unsupported. The measured ℓ=1 observable is explicitly parity-even, and no transfer function is derived from cosmic birefringence, chiral primordial tensors, or Chern-Simons gravity to projected spiral-arm winding. Statements that these mechanisms would generically produce or align a morphology dipole, and that the reported sensitivity constrains them, therefore do not follow from the analysis. This section should be removed or replaced by a concrete model calculation.

[MINOR] Appendix B—the claimed lower bounds on Expected Calibration Error subtract the catalog-wide mean confidence from accuracies measured on the GZ1 cross-match; Jensen’s inequality gives that bound only when confidence and accuracy are evaluated on the same sample with the same weighting. The assertion that recalibration cannot alter hard labels is also true only for a common monotone transformation, not for class-dependent multiclass calibration, which can change class ordering and sample membership.

[MINOR] The manuscript is excessively repetitive and uses inconsistent terminology for “primary,” “diagnostic,” “exclusion,” “disfavor,” “bound,” and “recovery threshold.” The title and abstract also foreground 8.5 million galaxies although the declared real-space science result uses 949,584 spirals. A substantial rewrite is needed to state one estimator, one sample, one calibrated null, and one appropriately limited physical conclusion.

(3) No—the manuscript supports only the narrow statement that the selected high-confidence hard-label map is unexceptional under its own randomization null, not the central physical claim of a sub-percent cosmological dipole constraint or a robust exclusion of a Shamir-scale signal.
