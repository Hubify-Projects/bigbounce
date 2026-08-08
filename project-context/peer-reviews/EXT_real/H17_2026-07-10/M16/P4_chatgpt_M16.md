(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

[MAJOR] Abstract; Secs. V A and VI B; Appendix D — the claimed sensitivity to a physical Shamir-scale dipole is internally inconsistent. The injection–recovery experiment injects a dipole into the already classified hard-label field and explicitly does not pass the signal through the classifier, the not spiral triage, or the confidence selection. Nevertheless, the manuscript compares its observed-label thresholds directly with a physical 1.7% chirality asymmetry. Using the manuscript’s own transfer factor g=2a−1=0.398, a true A=0.017 dipole would appear as A
obs
	​

≃0.0068, below the reported A
50
	​

=0.0075 and well below A
95
	​

=0.010–0.015. Likewise, applying this transfer to the WLS test changes the quoted statistic from (0.00455−0.017)/0.00163=−7.6 to approximately (0.00455−0.00677)/0.00163=−1.4, even before accounting for false-positive nonspirals. Thus the statements that a genuine 1.7% signal “would have been detected” and is strongly disfavored do not follow from the analysis. A sample-specific, full-confusion-matrix transfer or a genuine end-to-end image-level signal injection is required; otherwise these claims must be removed. 

ext_P4_M16

[MAJOR] Secs. III B and IV C — the p
eq
	​

>0.6 primary cut is not demonstrably pre-specified and appears outcome-dependent. The unthresholded catalog gives a nominal z≃4.2–4.4 dipole, while the result collapses to 0.41σ only after discarding roughly 70% of the classifier-selected spirals. The text then justifies 0.6 as the lowest cut that removes the z≃4 excess. A Git commit containing the cut is not a preregistration unless its existence and analysis protocol were independently timestamped before examination of the dipole; Git history can be rewritten, and the manuscript provides no blinded or externally archived record. The threshold must instead be selected using independent validation data or a spatially disjoint training region, or the cut scan must be incorporated into the inference. At minimum, the headline claim must be restricted to the 949,584-object selected subset, not “8.5 million DESI galaxies.”

[MAJOR] Secs. IV C–E, VI A, and Appendix D — the systematic attribution is incomplete, and the claimed direction of systematic bias is incorrect. The full sample has a nominal non-null real-space dipole and the harmonic analyses contain substantial low-ℓ residuals; the forward model explains only about 53% of the quoted ℓ=1 amplitude, leaving approximately 47% unresolved. A survey-correlated dipole is a vector and can either add to or cancel a cosmological dipole. The statements that inherited or depth-dependent biases necessarily increase power, make the null conservative, or cannot hide a real signal are therefore false without a joint vector nuisance model. The remaining component cannot be declared irrelevant merely because it lies below an A
50
	​

 detection threshold.

[MAJOR] Sec. III A; Tables V, VIII, and IX — “moment-z” is repeatedly presented as a significance although the null distributions are demonstrably non-Gaussian. For example, the manuscript associates z=3.64 with empirical p=0.030, and z=7.31 with p=6×10
−4
; these are not 3.64σ and 7.31σ significances in the conventional sense. This distinction is acknowledged but then ignored in the abstract, conclusions, and detection-efficiency claims. In particular, the injection threshold called “3σ” is defined using the null mean plus three standard deviations, not an empirical false-alarm probability. The recovery curves must be recomputed using an empirical-rank threshold corresponding to the desired type-I error, with substantially more than 1000 null realizations and confidence intervals from more than 100 injections per grid point.

[MAJOR] Secs. VI A–B — A
50
	​

 and A
95
	​

 are power thresholds, not upper limits or ceilings on an undetected signal. The manuscript repeatedly uses A
95
	​

 to bound inherited power, to state that an unresolved component is below an exclusion limit, and to formulate a falsification boundary, despite correctly noting elsewhere that A
95
	​

 has no confidence-interval coverage. A null observation plus a power curve does not by itself yield A<A
95
	​

. The paper needs a likelihood or Neyman construction for the dipole amplitude, including nuisance parameters and the positive-definite amplitude distribution, and should report an actual confidence or credible interval.

[MAJOR] Appendix D.g and Table XV — the block-bootstrap WLS statistic is not a calibrated test of a 1.7% dipole. The bootstrap samples the distribution around the observed map, not under the A
ref
	​

=0.017 hypothesis; the tested hypothesis has an unknown direction; the amplitude is positive-definite; and the covariance is anisotropic on the cut sky. Dividing the difference of two scalar amplitudes by the bootstrap standard deviation does not test the composite dipole hypothesis. The fit also uses the full, systematics-dominated catalog rather than the primary high-confidence sample, and its nuisance basis does not implement the claimed simultaneous confidence-, depth-, PSF-, and morphology-dependent confusion model. A valid test should inject vectors of fixed amplitude and varying direction through the complete analysis, or use a generalized likelihood with a three-component dipole covariance and profiled nuisance parameters. Until then, this statistic cannot be designated a primary cosmological result.

[MAJOR] Sec. II B, Sec. VI A, and Appendix B — the classifier validation is insufficient for a sub-percent cosmological measurement. Sixty-six percent of the training labels are CE-ResNet pseudo-labels; the independent three-class accuracy is only 58.7%; and the reported predicted-class precisions are approximately 0.54 for CW and 0.53 for CCW. The quoted 69.91% chirality accuracy conditions on true GZ1 spirals that the classifier also calls spiral, thereby excluding false-positive nonspirals and the full selection process relevant to the production catalog. The T
eq
	​

=0.9997 mirror result is algebraically guaranteed by the TTA construction and does not validate physical chirality sensitivity. The GZ1-human-only dipole is explicitly sensitive only at roughly 3%–7% amplitudes and therefore cannot establish independence at the sub-percent scale of the headline result. Independent, DESI-domain human labels distributed across the full footprint, including the DECaLS region where the strongest diagnostic excess occurs, are needed to measure spatially varying purity, completeness, and CW↔CCW confusion.

[MAJOR] Sec. IV C — the declared pixel-permutation null is not exchangeable. The variance of A
p
	​

 depends strongly on the per-pixel spiral count, while the survey depth and count distribution are spatially structured. Permuting A
p
	​

 between pixels therefore assigns high- and low-variance measurements to different directions and does not reproduce the null distribution of the fitted dipole. The per-galaxy/binomial null that preserves N
spiral
	​

(p) is more appropriate and should replace the pixel permutation as primary. Moreover, both shuffling schemes destroy any isotropic small-scale chirality correlations; those correlations must be measured and propagated because they affect the quoted recovery thresholds even if they do not turn the observed low significance into a detection.

[MAJOR] Sec. IV C–D, Appendix A, and Table V — the two “canonical” MASTER results are not reconciled. The same nominal canonical footprint is reported as +3.64 moment-z in the 500-realization computation and +7.93 in the 10,000-realization computation. Increasing the Monte Carlo sample alone cannot explain such a shift, and the manuscript itself states that the A
p
	​

 versus A
p
	​

/2 field rescaling leaves z invariant. The exact differences in map, monopole subtraction, weights, binning, coupling matrix, and null generator must be isolated in a single controlled comparison. There should be one canonical estimator, not several numerically incompatible quantities retained “for continuity.”

[MAJOR] Sec. IV D and Conclusions — the 99.32% pre-MASTER leakage result is overstated. That calculation intentionally analyzes an un-monopole-subtracted field while excluding ℓ=0 from the coupling problem; a large mask transform of the nearly 0.5 constant baseline is then expected. This demonstrates why the monopole must be removed or jointly deconvolved, but it does not establish a novel astrophysical systematic and cannot be used to explain or criticize earlier dipole analyses unless their precise estimators likewise retained the monopole. The discussion should separate this essentially deterministic mask effect from the genuinely unresolved post-subtraction/post-MASTER residual.

[MAJOR] Secs. II A and III D — the image-orientation parity of the input catalog is not audited. Because a reflection, unlike a rotation, reverses CW and CCW, the determinant of the cutout WCS transformation must have the same sign for every object and every imaging leg. The manuscript gives the pixel scale and cutout size but does not demonstrate that the third-party image-generation pipeline never mirrors images across BASS+MzLS, DECaLS, DES, or overlap regions. A catalog-wide WCS-parity audit, together with checks for duplicated astrophysical objects, overlap duplicates, and deblended components, is essential before interpreting any spatial chirality pattern.

[MAJOR] Secs. VI C–D — the cosmological interpretation exceeds what the measurement establishes. This is a two-dimensional, confidence-selected, classifier-label statistic with no redshift distribution, redshift-dependent selection function, or transfer from primordial parity-violating physics to projected galaxy morphology. A signal that changes sign with redshift, morphology, or selection quality can cancel in the projection. The assertions that cosmic birefringence or gravitational Chern–Simons physics would generically produce the measured morphology dipole are unsupported without a quantitative model and should be removed or clearly identified as speculation.

[MINOR] Appendix B.g — the claimed lower bound on calibration error is computed from incompatible samples. The catalog-wide mean confidence of 0.951 is compared with accuracy measured on the GZ1 cross-match; Jensen’s inequality yields an ECE lower bound only when confidence and accuracy averages are evaluated on the same objects. Reliability diagrams and ECE values should be computed directly on the disjoint held-out GZ1 sample, separately for the primary science cut.

[MINOR] Data Availability and presentation — the analysis is not yet frozen or adequately streamlined. The manuscript relies extensively on mutable main-branch artifacts, while the DOI and exact commit hashes are placeholders. An immutable archive containing the catalog, code, null arrays, masks, and configuration files is required before acceptance. The paper should also be substantially shortened: several caveats, significance conventions, independence arguments, and residual-attribution statements are repeated many times, while the genuinely load-bearing statistical model remains difficult to identify.

(3) The central claim is supported only as a null result for the selected p
eq
	​

>0.6 observed-label subset, not as a survey-wide physical null or as an exclusion of a 1.7% Shamir-scale dipole.
