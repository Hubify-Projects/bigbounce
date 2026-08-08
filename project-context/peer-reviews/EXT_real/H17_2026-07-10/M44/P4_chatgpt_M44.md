(1) VERDICT: MAJOR REVISIONS. 

ext_P4_M44

(2) ISSUES:

[MAJOR] Sections III B and IV C—selection of the primary p
eq
	​

>0.6 sample is not convincingly pre-specified. A commit containing both the threshold and the estimator is not an independent preregistration, particularly when no frozen tag or time-stamped analysis plan exists. The manuscript also motivates 0.6 as the first cut at which the z≃4 full-sample excess disappears, which is an outcome-dependent rationale. The authors must either document an independently frozen, pre-unblinding selection rule based solely on external validation data or treat the confidence-cut scan as a multiple-analysis problem and incorporate it into the reported inference.

[MAJOR] Abstract, Sections V and VI B—the claimed sub-percent sensitivity is calibrated only in the post-classification label field, not for a physical galaxy-chirality dipole. The injections are applied after image classification, not-spiral triage, the confidence cut, and spatially varying classification errors. The full-catalog mirror test verifies the algebraic flip equivariance imposed by Eq. (2), but it does not measure the transfer of a population-level physical dipole through morphology, image quality, class selection, and the confidence-dependent confusion matrix. Consequently, A
50
	​

 and A
95
	​

 are observed-label detection efficiencies and do not establish that a genuine physical Shamir-scale signal would have been detected.

[MAJOR] Appendix D and Section VI B—the z≃−7.6 “clean 1.7% dipole” disfavor is internally inconsistent with the manuscript’s own dilution factor. The paper gives g=2a−1=0.398. If A
ref
	​

=0.017 denotes an underlying physical dipole, its expected observed amplitude is approximately 0.017×0.398=0.0068, not 0.017. Relative to A
best
	​

=0.00455 and σ
boot
	​

=0.00163, this is only about 1.4σ, before any additional edge-on dilution, rather than 7.6σ. Likewise, the stated observed-label A
95
	​

=1.0%−1.5% corresponds to roughly 2.5%−3.8% physically under the stated transfer factor. If A
ref
	​

 instead denotes Shamir’s estimator-level observed asymmetry, no transfer equivalence between Ganalyzer and this classifier has been established. The assertion that omitting classifier dilution makes the exclusion “conservative” is therefore backwards.

[MAJOR] Section IV C—the primary estimator and pixel-permutation null do not provide a valid likelihood for the survey. Uniformly weighting A
p
	​

 gives equal influence to pixels with very different galaxy counts and hence strongly different binomial variances. Permuting A
p
	​

 among pixels assumes exchangeability despite variations in N
spiral
	​

, depth, PSF, morphology, confidence, and footprint position. The per-galaxy shuffle preserves counts but still assumes spatially exchangeable classification errors and removes any intrinsic spin covariance. A defensible primary analysis should use a per-galaxy or per-pixel binomial likelihood, an explicit selection/confusion model, nuisance templates fixed before fitting, and a spatial covariance treatment appropriate to clustered galaxies.

[MAJOR] Sections IV C–D—the argument that the unresolved harmonic residual is below the recovery threshold mixes incompatible samples and estimators. The 0.695% harmonic residual is measured on the full Catalog C sample, but it is compared to the p
eq
	​

>0.6 real-space thresholds A
50
	​

≃0.75% and A
95
	​

>1%. The manuscript itself reports full-sample real-space thresholds A
50
	​

≃0.36% and A
95
	​

≃0.63%, as well as a full-sample z≃4.2−4.4 dipole. Under that like-for-like calibration, 0.695% is not below the recovery threshold. Moreover, a recovery-efficiency threshold is not an upper limit on the cosmological content of an observed residual. The statements that the direct real-space estimator “registers none” and that the open 47% cannot affect the conclusion are therefore unsupported.

[MAJOR] Appendix C—the hemisphere look-elsewhere results are statistically inconsistent. The manuscript reports a maximum local value of 3.05σ, a direct global max-statistic result p
LEE
	​

≤10
−4
, and a Bonferroni estimate corresponding to less than 1σ. These cannot all characterize the same test without a much clearer definition of the local statistic and its null distribution. In addition, Bonferroni control does not require independent tests; it is valid, though often conservative, under arbitrary dependence. The complete per-realization maximum-statistic distribution and the corresponding local and global empirical p-values should be reported.

[MAJOR] Sections III A, IV C–D, and Table V—the harmonic “σ” values are misleading and highly null-procedure dependent. For example, z
mom
	​

=7.31 is accompanied by empirical p=6×10
−4
, approximately 3.2σ Gaussian-equivalent, while the 3.64 standardized score has p=0.030, approximately 1.9σ. These quantities should not be described as 7.3σ and 3.6σ significances. More seriously, the nominally related canonical ℓ=1 calculations change from +3.64 to +7.93 when the field convention and shuffle procedure change. Declaring them “not comparable” does not resolve the fact that the inferred anomaly is dominated by analysis convention. One physical null, one declared data vector, and empirical tail probabilities should be used.

[MAJOR] Sections II and VI A and Appendix B—the independence and spatial-confusion controls do not support the headline precision. Since 66.5% of the training labels are CE-ResNet pseudo-labels and the independent GZ1 chirality accuracy is only 69.91%, inherited survey structure is a central uncertainty. The GZ1-human-only test has an estimated A
50
	​

≃3.4% and A
95
	​

≃4.5%−6.8%, so it cannot validate the sub-percent result. The two-leg confusion analysis also leaves confidence intervals of approximately 0.6−1.4 percentage points, comparable to the claimed sensitivity, does not resolve RA-dependent variation within a leg, and conditions away the potentially chirality-dependent not-spiral triage. A spatially varying inherited bias can also oppose and partially cancel a real dipole; it need not only add power, contrary to the manuscript’s argument.

[MAJOR] Sections III D and Appendix B—the demonstrated rotation instability is not adequately controlled. The finding that 21.4% of per-galaxy argmax labels change between Z
2
	​

 and D
4
	​

 test-time averaging is large. Because cutouts have a fixed sky orientation and survey PSF, depth, and scan properties vary across the footprint, rotational non-equivariance can couple directly to sky position. Stability of the mean probability on two samples of only about 2,000 objects does not bound a sub-percent dipole. The primary catalog should use a rotation-equivariant architecture or full rotation averaging, or the authors must demonstrate on the full science sample that rotational response has negligible low-ℓ projection.

[MAJOR] Sections IV C, Appendix A, Table XVI, and Data Availability—mask bookkeeping and reproducibility are not yet internally consistent. Section IV C states that 3,200,420 spirals are inside the N
spiral
	​

≥10 mask and 740 are outside it, whereas Table XVI reports an in-mask count of 3,201,160. The term “canonical footprint” is also used both for the N
spiral
	​

≥10 mask and for the N
all
	​

≥1 apodized footprint. In addition, 2.9% of rows exhibit a raw/equivariant pipeline-pass mismatch, and the archival DOI and exact immutable commit hashes are still placeholders while the analysis points to a mutable main branch. These discrepancies must be resolved with a frozen release, machine-readable estimator specifications, checksums, and independently reproducible headline numbers.

[MINOR] Section IV D—the 99.32% monopole–mask “explanation” is overstated. It is obtained from an un-monopole-subtracted field on a cut sky, where leakage of a large monopole into pseudo-C
1
	​

 is expected. This does not establish a mechanism for earlier real-space or Ganalyzer measurements, which used different estimators, footprints, and selections. The result is a pipeline diagnostic and should not be presented as explaining prior literature without a matched reanalysis.

[MINOR] Section VI C and the Conclusions—the theoretical and comparative interpretation exceeds what is derived. The assertions that cosmic birefringence or gravitational Chern–Simons models would generically produce a galaxy-morphology dipole are unsupported without a galaxy-formation transfer function. Similarly, the quoted factor 3.7−8.8 tension with Shamir and the statement that a future detection would “falsify this null” are not meaningful without matched redshift, morphology, footprint, selection, and estimator definitions. These claims should be removed or sharply restricted.

(3) The central claim is not supported at the advertised physical, sub-percent level; only the narrower statement that the selected high-confidence observed-label sample is consistent with a zero dipole is presently supported.
