(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

[MAJOR] Abstract; Secs. V and VI B — the claimed sensitivity to a “genuine” 1.7% dipole is internally inconsistent. The injection–recovery experiment inserts a dipole only into the post-classification hard-label field, whereas Sec. VI B gives a classifier transfer slope g≃0.398. Under the manuscript’s own mapping, a physical 1.7% dipole would therefore appear at only ≃0.68% in the observed labels, below the quoted A
50
	​

=0.75% and well below A
95
	​

=1.0%−1.5%; it is not established that such a signal would be “unmissable.” The mirror-flip run tests equivariance, not accuracy, not-spiral selection, or the transfer of a physical population dipole. Section VI A also switches inconsistently between f
CW
	​

 and A
p
	​

 units by a factor of two. A genuine image-level population injection through classification, triage, confidence selection, and map-making is required, or all physical/Shamir-scale exclusion language must be withdrawn. 

ext_P4_M11

[MAJOR] Sec. III B and Appendix D(g), Table XV — the z≃−7.6 block-bootstrap result is not a calibrated exclusion and should not be designated a primary cosmological estimator. It is obtained on the full Catalog C sample, including the low-confidence population that the paper itself shows produces a 4σ-level spatial excess. The bootstrap distribution is centered on the observed scalar, positive-definite amplitude rather than generated under A
ref
	​

=0.017; it does not profile over the unknown dipole direction with the anisotropic cut-sky covariance. Resampling nonexchangeable sky blocks with their original coordinates is also not demonstrated to reproduce the survey’s large-scale covariance. Most importantly, comparing a physical A
ref
	​

 directly with an observed-label amplitude while omitting dilution is anti-conservative, contrary to the manuscript’s statement. A simulation-calibrated vector likelihood under the alternative hypothesis is needed.

[MAJOR] Sec. IV C — the primary permutation null is not justified for these data. Permuting A
p
	​

 among pixels assumes exchangeability despite strongly varying N
spiral
	​

(p), confidence distributions, morphology mixtures, depth, PSF, and survey leg; it detaches each pixel’s noise variance from its count and observing conditions. The per-galaxy global label shuffle preserves counts but still assumes a spatially constant label/confusion process and removes precisely the correlated classifier systematics known to be present. A covariate-conditioned galaxy-level likelihood, conditional randomization within depth/confidence/morphology strata, or end-to-end survey simulations with spatial covariance are required to calibrate the quoted p=0.31.

[MAJOR] Secs. VI A and Appendix D — the claim that inherited or survey-correlated bias can only add power and therefore makes the null conservative is false. A dipolar systematic is a vector and may add to, rotate, or cancel a physical dipole depending on its direction; confidence-dependent selection may also attenuate a signal nonuniformly. Showing that several fitted templates correlate with the observed field does not establish the sign of every unmodeled component. The assertion that the combined nuisance channels “cannot manufacture the primary null from a hidden signal” requires a joint nuisance likelihood or injection into the measured residual fields.

[MAJOR] Sec. IV C — the p
eq
	​

>0.6 choice is not credibly demonstrated to be pre-specified. A commit containing the estimator is not an independent, immutable preregistration, and the selected threshold is exactly where the reported significance collapses from about 4σ to null while discarding roughly 70% of the classified spirals and changing the footprint. The 0.6-to-0.8 robustness sweep does not account for choosing the transition boundary after inspecting the data. The authors should document a timestamped blinded selection based solely on held-out validation information or include the cut scan in the inferential procedure.

[MAJOR] Sec. II B and Appendix B — classifier validation is inadequate for a sub-percent cosmological measurement. Two thirds of the training labels are CE-ResNet pseudo-labels, so the reported 93.7% internal accuracy largely measures reproduction of the pseudo-label source; the independent result is only 69.91% chirality accuracy with κ=0.40, and the three-class accuracy is 58.7%. The not-spiral class is trained from only 2,000 synthetic negatives, making spatially varying false-spiral contamination a serious concern. The leg-stratified differential-error intervals still allow errors of order 0.4%−1.4%, comparable to the entire claimed sensitivity range, and the analysis conditions on objects already predicted CW/CCW, omitting potentially chirality-dependent not-spiral triage. A blinded human-labeled validation sample representative of all survey legs, depths, PSFs, morphologies, and confidence ranges is needed.

[MAJOR] Secs. II, VI A — the GZ1-human-only test does not validate the headline sub-percent null. The manuscript’s own scaling gives this test A
50
	​

≃3.4% and A
95
	​

≃4.5%−6.8%. Its null result therefore excludes neither a sub-percent inherited classifier pattern nor the amplitudes relevant to the primary claim. It may be retained as a coarse independent check, but statements that it “establishes” that the vanishing dipole is not inherited from pseudo-labels must be substantially weakened.

[MAJOR] Sec. III D and Appendices B/E — flip equivariance is repeatedly conflated with unbiased chirality inference. The two-fold TTA guarantees only that mirroring swaps the soft CW/CCW outputs; it does not guarantee rotational stability, correct physical labels, equal CW/CCW error rates, or independence from detector orientation and survey conditions. The reported 21.4% Z2-to-D4 hard-label instability is directly relevant because the science estimator uses hard argmax labels. In addition, the raw/equivariant pipeline mismatch affects 2.9% of the catalog and 6.3% of the primary HC sample. The catalog should be regenerated through one deterministic inference path, and rotation/orientation response should be measured on the full primary sample as a function of sky position and observing conditions.

[MAJOR] Sec. IV D — the unresolved harmonic residual is dismissed by an invalid comparison. Only about 53% of its amplitude is forward-modeled, leaving approximately 47% explicitly unexplained. The full residual, A
p
	​

≃0.695%, is compared with the HC-sample A
50
	​

=0.75%, even though the harmonic field uses the full sample; the paper separately reports a full-sample A
95
	​

≃0.63%, below that residual. Moreover, a recovery threshold is not an upper limit and cannot establish that an unresolved component is noncosmological. The residual may be described as systematics-suspected, but not systematics-attributed without a closed model; a physical contribution below the primary estimator’s sensitivity remains allowed.

[MAJOR] Sec. VI B and Table VIII — the quoted A
95
	​

 bracket is statistically under-resolved and does not support a universal detectability statement. With only 100 injections per amplitude, the 91% recovery at 1.0% has a confidence interval that includes 95%, so the assertion A
95
	​

>1.0% is not established. The completeness is averaged over randomly drawn axes rather than reported for the least-sensitive fixed directions, and the injections omit the measured spatially correlated residuals and all upstream classification/selection effects. More simulations, confidence bands, and direction-dependent completeness are required.

[MAJOR] Appendix A, Table V, Sec. VII(c), and Appendix C — statistical significances are reported in a misleading and partly inconsistent manner. The manuscript calls standardized moment ratios “σ” even when the empirical null is strongly non-Gaussian: for example, z
mom
	​

=3.64 corresponds to empirical p=0.030, and z
mom
	​

=7.31 corresponds to p=6×10
−4
, not Gaussian 7.31σ. Empirical p-values should be the primary reported significance. The statement that Bonferroni correction assumes independent tests is mathematically incorrect; Bonferroni controls the family-wise error rate without an independence assumption. The disagreement between the direct-MC maximum-statistic result and the Gaussian-Bonferroni heuristic therefore requires an explicit audit of the statistic and null implementation.

[MAJOR] Secs. III–IV and Appendix A/Table XVI — masks, samples, and estimator definitions are internally inconsistent. The main text defines the canonical mask as N
spiral
	​

≥10, while Appendix A(d) calls the N
all
	​

≥1 footprint “canonical”; these contain 24,087 and 24,297 pixels, respectively. Sec. IV C states that 740 of the 3,201,160 spirals lie outside the canonical mask, whereas Table XVI reports all 3,201,160 as in-mask. The +3.64 and +7.93 canonical MASTER values also use different field constructions, mean subtractions, coupling implementations, and nulls, yet are sometimes described as a recomputation of the same field. A single authoritative table of sample membership, mask hashes, field definitions, weights, and nulls must replace the present inconsistent bookkeeping.

[MAJOR] Sec. II A — the parent-sample construction and selection function are insufficiently documented. The cutouts come from a third-party HuggingFace collection and coordinates are obtained by cross-matching to another catalog, but the match radius, ambiguity handling, duplicate/deblend rate, missing-coordinate rate, and uniqueness audit are not given. Because duplicated photometric objects have previously generated false chirality signals and the target precision is below one percent, uniqueness and cross-match validation must be demonstrated quantitatively.

[MAJOR] Sec. VI C — the claimed connection to primordial parity violation, cosmic birefringence, and Chern–Simons gravity is unsupported. No transfer function from these theories to projected late-time galaxy-arm winding is derived, no model parameter is constrained, and redshift evolution or cancellation is not treated. Statements that these mechanisms would generically produce the measured morphology dipole or preferentially align galaxy angular momenta should be removed or presented solely as speculative motivation.

[MINOR] Appendix B and Data Availability — reproducibility details remain incomplete. The stated 25,790-source manifest and 79.4/20.6 split imply roughly 20,467 training sources, but the post-augmentation training count is only 21,293, so “flip augmentation” adds just 826 examples; the exact class-conditional augmentation rule and object-level split should be given. The analysis presently points to a mutable live branch and a future DOI placeholder; acceptance should require a frozen archive, exact commit hashes, catalog checksum, and scripts sufficient to regenerate every primary table.

[MINOR] Throughout — the manuscript is excessively repetitive and obscures the inferential chain. Repeated declarations that diagnostics are “not detections” do not substitute for one coherent statistical model. The paper should be shortened substantially, retain one pre-specified primary estimator, report all amplitudes in one convention, and move obsolete or mutually incomparable harmonic variants to supplementary material.

(3) The central claim is supported only in the narrow sense that the chosen high-confidence observed-label estimator yields no significant dipole; the manuscript does not yet support a physical sub-percent null or the claimed detectability/exclusion of a true 1.7% dipole.
