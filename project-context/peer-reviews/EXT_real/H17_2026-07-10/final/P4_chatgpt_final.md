(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Secs. II, VI B, and VII—The quoted sensitivity is not a sensitivity to physical galaxy chirality. The injection–recovery analysis inserts a dipole only into the already-classified hard-label CW/CCW field; it does not propagate a signal through the images, ViT classifier, not-spiral triage, confidence selection, or spatially varying confusion matrix. Therefore A
50
	​

≃0.75% and A
95
	​

∈(1.0%,1.5%] are thresholds for the classifier-output field, not physical chirality limits. Nevertheless, the manuscript claims that a 1.7% cosmological dipole would be recovered. Using the manuscript’s own g
eff
	​

=0.398, a 1.7% physical dipole would produce only approximately 0.68% in the observed labels, below the stated A
50
	​

; the corresponding physical A
95
	​

 would be approximately 2.5–3.8%. The manuscript also contradicts itself on whether this dilution is “folded into” the injections. 

h17c_P4

[MAJOR] Sec. IV C—The primary p
eq
	​

>0.6 sample is not demonstrated to have been selected independently of the result. The full sample and cuts through p
eq
	​

=0.5 give z≃4.0–4.3, while the null appears only at p
eq
	​

≥0.6; the stated rationale for 0.6 is explicitly that it is the first threshold removing the excess. An internal Git commit, without an immutable public timestamped registration made before outcome inspection, is not evidence of prospective selection. The headline null is therefore conditional on discarding about 70% of the classified spirals using a depth-correlated score, with no model-selection correction or independently defined purity criterion.

[MAJOR] Appendix D and Table XV—The claimed z≃−7.6 disfavor of a 1.7% dipole is not a valid hypothesis test. It is obtained by subtracting a fixed positive amplitude from a positive-definite bootstrap amplitude estimate and dividing by the bootstrap width around the observed data; the bootstrap distribution is not generated under A=0.017, and the test does not profile over dipole direction. The design called “joint nuisance-marginalized” contains leg and density terms rather than the required depth-, PSF-, extinction-, morphology-, and confidence-dependent response, and its leg subspace is exactly rank-deficient. The manuscript itself concedes that the statistic is not calibrated, so it cannot serve as a primary cosmological exclusion.

[MAJOR] Sec. IV D—The accounting of the unexplained harmonic residual is mathematically incorrect. The fitted systematic vector has approximately 53% of the observed amplitude and cosθ≃0.84; the residual vector therefore has amplitude

1+0.53
2
−2(0.53)(0.84)
	​

≃0.63

of the observed vector, not 47%. The unexplained amplitude is consequently about 0.43%, not 0.32%. Moreover, the residual is measured on the full 3.2-million-spiral sample but is compared with the less sensitive 0.95-million-object high-confidence threshold. The manuscript’s own matching full-sample values are A
50
	​

≃0.36% and A
95
	​

≃0.63%; the full 0.695% residual exceeds that A
95
	​

, and the correctly computed unexplained component exceeds A
50
	​

. The assertion that the residual is safely below the relevant recovery threshold is therefore false. 

h17c_P4

[MAJOR] Secs. IV D and VI A—The argument that survey-correlated classifier bias can only add low-ℓ power and therefore makes the null conservative is wrong. A spatially varying systematic dipole is a vector and can anti-align with, partially cancel, or rotate a physical dipole. Consequently, neither the norm of the observed residual nor the null value obtained after a confidence cut bounds the magnitude of an underlying cosmological component. The unresolved coherent structure must be included in a joint generative likelihood or constrained with independent labels of comparable statistical power.

[MAJOR] Sec. IV C—The primary real-space estimator and its null are not statistically adequate. Uniform-pixel least squares ignores the strongly varying binomial variance, Var(A
p
	​

)∝1/N
p
	​

, while permuting A
p
	​

 among pixels destroys the observed relation between variance, depth, mask geometry, and confidence selection. The per-galaxy shuffle is a preferable check, but it still assumes spatial exchangeability of classifier errors, which the manuscript’s own depth- and confidence-dependent diagnostics contradict. A galaxy-level binomial or hierarchical spatial likelihood is required. In addition, the paper supplies no coverage-guaranteed confidence region or upper limit on the dipole vector; A
95
	​

 is a detection-power threshold and cannot be used as a parameter bound.

[MAJOR] Secs. IV C–D and Table V—The harmonic significance calibration is internally unresolved. The nominal canonical ℓ=1 measurement is reported as z=+3.64 with empirical p=0.030 and elsewhere as z=+7.93 with empirical p=3×10
−4
, under different shuffle constructions. This is not a harmless increase in Monte Carlo size; it shows material dependence on the null definition. Because the null distributions are explicitly heavy-tailed, the empirical ranks—not the moment ratios—are the calibrated significances. Repeatedly labeling these results “3.64σ” and “7.93σ” substantially overstates what the rank p-values imply. One predeclared field, null construction, and rank-based test must be used and justified. 

h17c_P4

[MAJOR] Sec. VI A and Appendix B, Table XIV—The human-label cross-check does not validate independence at the headline sensitivity. The GZ1-only sample has A
50
	​

≃3.4% and A
95
	​

≃4.5–6.8%, so it cannot detect sub-percent structure inherited from CE-ResNet pseudo-labels. The two-leg confusion analysis leaves differential-error bounds at roughly 0.6–1.4 percentage points and provides no RA-, depth-, PSF-, or morphology-conditioned confusion field. Statements that the human-label null “establishes” that the headline null is not inherited are therefore unsupported.

[MAJOR] Sec. VI B—The recovery thresholds are averaged over randomly drawn dipole axes on a highly anisotropic, approximately half-sky footprint. An exclusion of a dipole with unknown direction requires a direction-dependent likelihood or, at minimum, worst-case completeness over the sphere; an axis-averaged probability under an assumed isotropic prior does not establish that a signal “would have been detected.” The ten-axis check at one amplitude is insufficient. The absence of redshift-resolved tests further prevents extension of the projected aggregate null to redshift-dependent signals or direct comparison with differently selected earlier samples.

[MAJOR] Data Availability and Sec. IV C—The reproducibility and preregistration claims cannot be verified from the submitted record. The analysis repository is described as a mutable live main branch, while the frozen DOI, exact commit hashes, catalog snapshot, model checkpoint, and canonical null arrays are promised only for a future deposit. Nearly every quantitative result depends on external artifact paths rather than an immutable review package. Those materials must be frozen and supplied before the numerical claims can be assessed independently. 

h17c_P4

[MINOR] Appendix C—The look-elsewhere discussion contains a statistical error: Bonferroni control does not require independent tests; it remains valid under arbitrary dependence, although it can be conservative. With 10
4
 Monte Carlo realizations, the minimum resolvable rank p is approximately 10
−4
; reporting p≤10
−4
 without a finite-Monte-Carlo confidence bound is not justified, and the full maximum-statistic null distribution should be shown.

[MINOR] Secs. V and VI C—The external physical interpretation is unsupported. A monopole–mask calculation for this ViT classifier and footprint cannot explain results from a different Ganalyzer estimator and selection, and neither cosmic birefringence nor gravitational Chern–Simons theory yields a quantitative galaxy-morphology dipole without a derived transfer function. These statements should be removed or explicitly labeled as speculation rather than constraints.

(3) The central claim is not supported by the evidence presented because the analysis demonstrates only a null in an outcome-sensitive, confidence-selected classifier-output field, while the transfer to physical chirality and cancellation by unresolved spatial systematics remain uncalibrated.
