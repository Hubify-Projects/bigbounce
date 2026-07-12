(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Abstract; Secs. V A, VI B; Appendix D—claimed sensitivity to a “genuine Shamir-scale” dipole. The manuscript’s injection tests add a dipole only after classification, whereas its own external validation gives a chirality transfer slope g≃0.398. A physical 1.7% dipole would therefore appear at only ∼0.68% in the observed-label field, below the quoted A
50
	​

≃0.75%, not above A
95
	​

. Likewise, comparing the WLS result with gA
ref
	​

, rather than the undiluted A
ref
	​

=0.017, would reduce the manuscript’s scalar discrepancy from z≃−7.6 to roughly −1.4. Thus the statements that a genuine Shamir-scale signal “would have been detected” and is strongly disfavored are inconsistent with the manuscript’s own classifier-dilution model. 

ext_P4_M1

[MAJOR] Sec. IV C—definition of the primary p
eq
	​

>0.6 sample. The headline null retains only 949,584 of 3.20 million classified spirals, while the unthresholded sample gives a 4.2–4.4σ dipole. The threshold is explicitly justified as the point where that excess disappears. The claimed preregistration is not independently established: a mutable Git commit containing both the cut and estimator, with no frozen tag or external timestamp, does not demonstrate that the choice preceded inspection of the result. A blinded holdout or a threshold fixed solely from external validation is required.

[MAJOR] Sec. IV C—pixel-permutation null. Permuting per-pixel asymmetries assumes exchangeability of pixels despite order-of-magnitude variations in galaxy count, depth, morphology, confidence, and noise variance. This is especially inappropriate when the paper’s central systematic is depth-dependent classifier behavior. The per-galaxy shuffle preserves pixel counts but still removes any spatially varying classifier bias by construction; therefore neither null tests the principal alternative to isotropy.

[MAJOR] Secs. II, VI A and Appendix B—external classifier validation. The quoted 69.91% chirality accuracy, κ=0.40, and severe probability miscalibration do not support a sub-percent physical measurement. Galaxy Zoo 1 is a different, non-representative population with known human winding biases, and the leg-stratified differential-error intervals remain at approximately 0.6–1.4 percentage points, comparable to or larger than the claimed sensitivity. The human-only dipole test has an estimated A
50
	​

∼3.4% and A
95
	​

∼4.5–6.8%, so it cannot validate the sub-percent conclusion.

[MAJOR] Secs. IV C–E and Appendix D—unresolved spatial systematics. The full sample, hemisphere statistic, and several harmonic estimators reject random-label nulls, while approximately 47% of the reported ℓ=1 residual remains unexplained. Declaring these channels “diagnostic” does not remove the inconsistency. A spatially varying differential classification error can either create or cancel a real dipole; the manuscript’s assertion that inherited or survey-correlated bias must make the null conservative is not generally correct.

[MAJOR] Appendix D—block-bootstrap WLS “primary exclusion.” Figure 10 is a bootstrap sampling distribution around the observed estimate, not a distribution generated under A
ref
	​

=0.017. Dividing A
best
	​

−A
ref
	​

 by its bootstrap width is therefore not a calibrated hypothesis test, particularly for a positive-definite amplitude with an unknown three-dimensional direction and fitted nuisance parameters. The manuscript acknowledges this but nevertheless assigns the result primary cosmological weight.

[MAJOR] Appendix D—nuisance marginalization is incomplete and inconsistently described. The principal 9-template WLS fit contains dipole components, imaging-leg fractions, density terms, and a constant; it does not jointly include the stated dominant PSF, depth, extinction, morphology, and confidence-dependent confusion fields. Elsewhere the paper describes this fit as jointly marginalizing depth and morphology, which is not supported by the listed design matrix. Separate forward models explaining only about 53% of the residual cannot substitute for a single correctly specified likelihood.

[MAJOR] Sec. VI B—injection–recovery calibration. The injections bypass the images, ViT classifier, not-spiral triage, confidence selection, and spatially varying confusion matrix. Consequently A
50
	​

 and A
95
	​

 are thresholds for an already-classified hard-label map, not for the physical galaxy-chirality dipole claimed in the title and abstract. A realistic end-to-end image-level injection, or a validated conditional response model over depth, PSF, morphology, and survey leg, is necessary.

[MAJOR] Secs. IV C, VI B and Conclusions—absence of a valid upper limit. A recovery probability is not a confidence interval. The paper explicitly states that A
95
	​

 has no frequentist coverage, yet repeatedly uses it as a ceiling, exclusion boundary, or falsification scale. A null result should provide the fitted dipole vector and covariance together with a systematics-marginalized confidence region or upper limit with demonstrated coverage.

[MAJOR] Secs. III A, IV C–D and Table V—use of “σ” for heavy-tailed nulls. The nominal canonical harmonic statistic is reported as +3.64σ with empirical p=0.030, and elsewhere as +7.93σ with empirical p=3×10
−4
. Those p-values correspond to approximately 1.9σ and 3.4σ Gaussian-equivalent significances, respectively. Calling moment ratios “σ” while emphasizing that the null is non-Gaussian is misleading; empirical p-values should be primary.

[MAJOR] Tables V–VI and Appendix A—multiple nominally canonical harmonic estimators. The manuscript gives materially different results for what is repeatedly called the canonical, unapodized ℓ=1 field, attributing the difference to changing field normalization, weighting, mean subtraction, and null construction. These are not merely different Monte Carlo sample sizes. One frozen estimator must be defined, and all variants should be presented only as robustness tests against that estimator.

[MAJOR] Secs. III B, IV C–E and Appendices C–E—multiplicity and analysis hierarchy. The study examines numerous catalog tiers, confidence cuts, masks, pixel thresholds, weights, apodizations, nulls, coordinate partitions, and directional scans. Declaring a preferred hierarchy after obtaining the results does not control researcher degrees of freedom. The final test must be evaluated on untouched data, or the global selection and multiplicity must be incorporated statistically.

[MAJOR] Secs. II A, III D and Appendix B—image-parity convention. The paper does not demonstrate that the cutout-generation pipeline has a uniform WCS parity and image orientation across BASS, MzLS, DECaLS, overlap regions, and bricks. Because a single image reflection reverses CW and CCW, an unnoticed parity change in the imaging or JPEG/cutout pipeline would be fatal. A catalog-wide WCS-determinant and cutout-orientation audit is required.

[MAJOR] Data Availability—reproducibility at submission. The analysis points to a live mutable branch, while the immutable tag, exact commit hashes, checksums, and Zenodo DOI are promised only for the future. The very large number of results referenced solely by internal artifact paths makes independent verification impossible from the submitted record. The frozen catalog, code, environment, null arrays, and provenance files must exist before review.

[MINOR] Sec. VI A—amplitude units. The statement A
95
	​

≲1.5% in “f
CW
	​

 units” corresponding to ≲3×10
−2
 in A
p
	​

 units contradicts the paper’s repeated definition that the full dipole amplitude A is numerically identical to the A
p
	​

 dipole amplitude. All amplitude conventions require a complete audit.

[MINOR] Title and abstract—sample size. The headline cosmological result is based on 949,584 selected spirals, not 8.5 million galaxies; 8.5 million is the parent classification catalog. The title and abstract should state the actual primary-analysis sample.

[MINOR] Sec. VI C—theory interpretation. Statements that cosmic birefringence or Chern–Simons gravity would generically produce a measurable galaxy-morphology dipole are speculative without the transfer function that the manuscript explicitly does not derive. These claims should be removed or clearly separated from the observational result.

[MINOR] Overall presentation. The manuscript is highly repetitive, repeatedly redefines which statistic is “primary,” and embeds extensive defensive commentary and repository paths in the scientific narrative. A substantial restructuring is needed so that the data vector, estimator, null, sample, and inferential claim can be identified unambiguously.

(3) No—the manuscript supports only that one selected high-confidence classifier-output map is compatible with its permutation null, not the stated physical/cosmological null dipole or the claimed exclusion of Shamir-scale signals.
