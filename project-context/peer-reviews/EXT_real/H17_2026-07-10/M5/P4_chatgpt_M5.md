(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Sections III B and IV C—definition of the primary sample is not demonstrably independent of the result. The headline +0.41σ result uses only the p
eq
	​

>0.6 subset of 949,584 spirals, whereas the unthresholded 3.2-million-spiral sample gives z≃4.2–4.4 and the [0.5,0.6) bin contains a significant excess. The manuscript explicitly motivates 0.6 as the first cut that removes this excess. A code commit made before the final manuscript is not an independently timestamped preregistration and does not establish that the cut was fixed before inspecting related spatial statistics. The threshold must be selected solely from held-out external validation, or the scan over thresholds, masks, estimators, and diagnostics must be incorporated into the inference; the full-sample result cannot simply be reclassified as “diagnostic” after inspection. The title is also misleading because the primary cosmological analysis uses fewer than one million spirals, not 8.5 million galaxies. 

ext_P4_M5

[MAJOR] Abstract, Sections V and VI B—the claimed sensitivity to a physical 1.7% dipole contradicts the manuscript’s own classifier-transfer calculation. The injections are made into the already-classified hard-label field, not into true galaxy chiralities or images. The paper estimates a transfer factor g=2a−1≃0.398; therefore a physical A=1.7% dipole would appear at only A
obs
	​

≃0.68%, below the quoted observed-label A
50
	​

≃0.75% and well below A
95
	​

>1.0%. Consequently, the statements that a genuine 1.7% Shamir-scale signal “would have been detected” and is disfavored at z≃−7.6 are not supported. Applying the same transfer to the WLS reference gives approximately 0.0068, only about 1.4σ
boot
	​

 above the reported 0.00455, not 7.6σ. A spatially resolved, uncertainty-propagated transfer function—or a genuinely end-to-end image-level population injection—is required.

[MAJOR] Sections IV D and VI A–B—the detection-efficiency thresholds are repeatedly misused as amplitude bounds. The manuscript correctly states that A
95
	​

 is a 95%-recovery threshold rather than a confidence upper limit, but later infers that the unexplained harmonic residual, any inherited pseudo-label dipole, and any cosmological contribution “must” lie below A
50
	​

 or A
95
	​

. That inference is invalid: failure to detect a signal with a test of limited power does not impose an upper bound on its amplitude. The paper needs a likelihood or confidence construction for the three dipole-vector components and a coverage-validated upper limit; null quantiles and power curves are not substitutes.

[MAJOR] Section IV C and Section VI B—the primary null and injection distributions assume exchangeability that the survey does not possess. Permuting pixel asymmetries ignores their count-dependent variances, while global per-galaxy label shuffles erase spatially varying classifier confusion, intrinsic spin correlations, galaxy clustering, and survey-correlated classification errors. The binomial injection backgrounds make the same independence assumption and therefore can substantially overstate sensitivity at low multipoles. The primary inference requires conditional randomization within relevant survey and morphology strata, a validated spatial covariance model, or realistic isotropic mock catalogs preserving both intrinsic correlations and the full selection/classification pipeline.

[MAJOR] Appendix D—the block-bootstrap WLS statistic is not a calibrated exclusion test and is not on the primary science sample. The quantity (
A
−0.017)/σ
boot
	​

 uses a bootstrap distribution centered on the observed estimate, not simulations generated under A=0.017; the dipole amplitude is positive and nonlinear, and its distribution need not be Gaussian. The WLS fit also uses the full Catalog C field rather than the p
eq
	​

>0.6 primary sample, does not propagate that selection function, and employs an exactly rank-deficient nuisance design. Moreover, the advertised “joint nuisance marginalization” does not contain a validated spatially varying classifier-confusion model. This result cannot serve as an independent primary cosmological exclusion without signal-conditioned simulations or a proper likelihood on the same declared science sample.

[MAJOR] Sections IV C–D and Appendix D—the unresolved full-sample and harmonic signals cannot be disposed of by declaring an estimator hierarchy. The full-sample real-space estimator rejects the random-label null, several harmonic analyses reject their nulls, and approximately 47% of the reported ℓ=1 residual amplitude remains unexplained. Different masks and weights explain why numerical significances differ, but they do not make the measurements scientifically unrelated: they probe the same underlying low-ℓ chirality field. A joint simulation must demonstrate how one physical dipole and the fitted systematics propagate through all channels. The assertion that unmodeled classifier or survey biases can only move the result away from zero is false for a vector dipole; an additive systematic can oppose and partially cancel a real signal.

[MAJOR] Section II and Appendices B and E—the classifier validation is insufficient for a sub-percent cosmological statement. Two thirds of the training labels are CE-ResNet pseudo-labels, so the 93.7% random-split validation accuracy largely measures agreement with the pseudo-label source. The independent GZ1 result gives only 69.91% chirality accuracy on the broader sample, and the available sky stratification is too coarse to exclude an RA-dependent or depth/morphology-dependent differential error at the relevant level. Test-time averaging guarantees flip-swap consistency of the output protocol but does not guarantee spatially unbiased hard labels on the observed, unpaired sky. Likewise, mirroring each image and recovering swapped TTA labels is largely tautological and is not an end-to-end injection of a population dipole through triage, confidence selection, and spatially varying confusion.

[MAJOR] Appendix C and the significance convention—the look-elsewhere and tail-probability results are internally inconsistent as presented. A local maximum reported as 3.05 moment-standard-deviations is assigned a direct-MC global p
LEE
	​

≤10
−4
, while a Bonferroni calculation is said to reduce it below 1σ. Bonferroni’s union bound does not require independent tests, contrary to the manuscript. The result may reflect a mismatch between the standardized local statistic and the maximized raw statistic, but that must be demonstrated explicitly with the empirical local tail probability and released max-statistic distribution. More generally, reporting +3.64σ when the empirical p-value is 0.030, or +7.93σ when the rank p-value is 3×10
−4
, is misleading; these quantities should be called moment-z values, with empirical p-values or Gaussian-equivalent significances used for inference.

[MAJOR] Sections IV C, VI A–B, and Table XV—the amplitude conventions are not consistently applied. The manuscript defines the full dipole amplitude A to equal the A
p
	​

=2(f
CW
	​

−1/2) dipole amplitude, and Table VIII uses that convention. Section VI A nevertheless describes A
95
	​

≤1.5% as being in “f
CW
	​

 units” and converts it to 3×10
−2
 in A
p
	​

 units. This is a factor-of-two inconsistency in the part of the paper used to set inherited-signal ceilings and compare with earlier work. Every amplitude, recovery threshold, residual, and literature comparison needs a single audited convention.

[MAJOR] Section IV D—the “99.32% monopole–mask leakage reproduction” is overinterpreted. This number is obtained for an un-monopole-subtracted field, for which projection of a nonzero constant through a patchy mask necessarily produces deterministic pseudo-C
ℓ
	​

 leakage. It does not explain the monopole-subtracted or MASTER-decoupled measurements, where the paper itself finds that the monopole-only model reproduces only about 12% of the power. It also cannot be used to explain or criticize earlier estimators unless their exact mean treatment, footprint, weighting, and estimator are reproduced. The broad methodological conclusions based on 99.32% should be removed or restricted to this specific uncorrected estimator.

[MAJOR] Section VI C—the claimed connection to fundamental parity-violating models is unsupported. The manuscript provides no transfer function from cosmic birefringence, chiral gravitational waves, or Chern–Simons gravity to projected spiral-arm winding, and the cited theories do not by themselves establish a galaxy-morphology dipole at the quoted level. Statements that such mechanisms would “generically” align galaxy angular momenta or that the present measurement constrains them must be deleted unless a quantitative model is supplied. The defensible result is an observational constraint on a survey- and classifier-defined projected morphology field.

[MAJOR] Data Availability—the numerical analysis is not frozen in a reviewable archival record. The manuscript points to a mutable live branch, says that the DOI and exact commit hashes will be supplied later, and relies extensively on internal artifact paths not contained in the paper. Before scientific review can be completed, the exact catalog, model checkpoint, scripts, null arrays, injection outputs, and figure inputs must be deposited under an immutable tag or DOI with checksums and an executable reproduction workflow.

[MINOR] Organization and presentation—the manuscript requires substantial compression and restructuring. The same caveats and numerical results are repeated many times, several incompatible field/mask/weight conventions are interleaved, and internal-development language such as “pod-deferred,” “anchor battery,” and “operative ceiling” obscures the statistical argument. A revised paper should state one primary sample, one primary likelihood, one amplitude convention, and one validated systematic model, with secondary diagnostics moved to a concise supplement.

(3) No—the manuscript shows that one selected high-confidence observed-label estimator is consistent with zero, but it does not support the broader physical null, sub-percent sensitivity, or exclusion claims.
