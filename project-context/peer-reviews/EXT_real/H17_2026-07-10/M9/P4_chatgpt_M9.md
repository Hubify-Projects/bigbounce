(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

[MAJOR] Sections III B and IV C, primary-sample definition: the p
eq
	​

>0.6 cut removes roughly 70% of the classified spirals and changes the real-space result from z≃4.3 without the cut to z=0.41. A commit on a mutable repository is a provenance record, not an independently time-stamped preregistration, and the stated rationale for the threshold explicitly uses the observed location of the excess in confidence space. The authors must either document a genuinely pre-unblinding protocol or include the confidence-threshold choice in the statistical inference and model the unthresholded excess rather than dismissing it post hoc as systematic. 

ext_P4_M9

[MAJOR] Sections II and VI A and Appendix B, spatially varying classification error: the external GZ1 chirality accuracy is only 69.91%, while the science-cut CW↔CCW error-asymmetry interval and imaging-leg intervals are of the same order as the claimed sub-percent sensitivity. The GZ1 overlap is not demonstrated to be representative of the full DESI sample in depth, morphology, redshift, or footprint, and the manuscript explicitly leaves the finer RA/depth/PSF/morphology-dependent confusion field unresolved. Such an error field can either create a dipole or cancel a real one; the repeated assertion that inherited classifier structure necessarily biases away from null and therefore makes the result conservative is not generally valid.

[MAJOR] Section VI B and Table VIII, injection–recovery interpretation: the injections are made directly into the observed hard-label field and bypass the image classifier, not-spiral triage, confidence selection, and spatially dependent confusion matrix. Mirroring every image and confirming that the TTA output swaps CW and CCW tests protocol equivariance, not the response to an astrophysical chirality dipole. Consequently, A
50
	​

 and A
95
	​

 are estimator-power thresholds in label space, not physical galaxy-dipole thresholds, and they do not presently justify the abstract’s statement that a genuine Shamir-scale physical dipole would necessarily have been detected.

[MAJOR] Section IV C, primary null construction: permuting A
p
	​

 among pixels assumes exchangeability even though the pixel counts—and therefore the binomial variances—vary by orders of magnitude across the footprint. Uniform-pixel least squares compounds this heteroscedasticity. The per-galaxy shuffle is a better check but still assumes a spatially uniform labeling response. The primary result should be obtained from a binomial likelihood or equivalent count-level estimator with the mask and selection function retained, and calibrated using conditional simulations that preserve the observed N
spiral
	​

(p) and allowed spatial variations in classification performance.

[MAJOR] Sections IV C, VI B, and VII, absence of a statistical limit: z=0.41 and a rank p=0.31 establish only that this estimator does not reject its chosen null. The reported A
50
	​

 and A
95
	​

 are power/completeness thresholds and explicitly have no confidence coverage. A paper whose central result is a null measurement must provide a frequentist confidence region or posterior for the dipole vector and amplitude, including the unknown axis and nuisance parameters, or refrain from presenting detection-efficiency thresholds as constraints on the allowed signal.

[MAJOR] Appendix D and Table XV, claimed z≃−7.6 disfavoring of a 1.7% dipole: this statistic is formed by subtracting a fixed amplitude from the observed best-fit positive-definite amplitude and dividing by the width of a bootstrap distribution centered on the observed data. It is not a sampling distribution under A
ref
	​

=0.017, does not account for the composite alternative over dipole directions, and is not guaranteed Gaussian. In addition, nuisance templates on a partial footprint can absorb an injected cosmological dipole, but no transfer-function or injection test through the WLS nuisance fit is shown. This quantity cannot be treated as a second “primary” cosmological exclusion without simulation-calibrated hypothesis testing.

[MAJOR] Section IV D and Appendix D, unresolved harmonic signal: the manuscript reports highly significant low-ℓ residuals while the imaging-plus-morphology forward model reproduces only about 53% of the ℓ=1 amplitude. The argument that the remaining amplitude is below the real-space A
50
	​

 and therefore cannot affect the conclusion is invalid: a sub-A
50
	​

 signal is not excluded, and the manuscript’s own harmonic injections report very high detection probability at comparable amplitudes. Evidence for survey systematics and excess ℓ=2 power does not exclude a cosmological ℓ=1 component coexisting with those systematics. A joint signal-plus-systematics likelihood is required, or the conclusion must be limited strictly to the selected real-space estimator.

[MAJOR] Sections III A and IV D, Table V, and Appendix A, mutually inconsistent harmonic results: the canonical unapodized analysis is reported as +3.64σ with p
MC
	​

=0.030 in one implementation and +7.93σ with rank p=3×10
−4
 in another. Increasing the Monte Carlo count alone cannot produce this change, and a constant rescaling from A
p
	​

 to A
p
	​

/2 should leave z invariant. The manuscript invokes different mean-subtraction and field conventions but does not provide a transparent one-to-one reconciliation. One locked estimator, identical data vector, identical mean subtraction, and an independent implementation check are needed.

[MAJOR] Appendix C, hemisphere look-elsewhere calculation: the reported local maximum of 3.05σ, direct-MC look-elsewhere value p
LEE
	​

≤10
−4
, and statement that a Bonferroni correction reduces the result below 1σ are mutually incompatible unless the quoted “3.05σ” refers to a different statistic or null distribution than stated. The local statistic, maximum statistic, null ensembles, and empirical exceedance counts must be defined and recomputed consistently.

[MAJOR] Data Availability and Appendix B, catalog integrity and reproducibility: 2.9% of catalog rows—and 6.3% of the primary high-confidence sample—have raw/equivariant probability combinations that imply reconstructed probabilities outside [0,1] by as much as 0.09. Calling this a separate-pass mismatch does not resolve the inconsistency in a catalog advertised as a community resource. The affected probability columns should be regenerated from a single inference pass or removed, and all headline analyses should be rerun on the corrected catalog. Acceptance also requires an immutable release, exact commit hashes, checksums, and an archival DOI rather than artifacts referenced through a mutable live branch.

[MAJOR] Section VI C, theoretical interpretation: the statements that cosmic birefringence or gravitational Chern–Simons effects would generically generate a late-time galaxy-morphology dipole, and that the measured floor constrains such scenarios, are unsupported without a transfer function connecting those theories to projected spiral handedness. These paragraphs should be reduced to qualitative motivation unless an explicit physical model and quantitative response calculation are supplied.

[MINOR] Section VI A and the amplitude-convention discussion contain a factor-of-two inconsistency: A
95
	​

 is elsewhere defined as the full dipole amplitude and numerically equal to the A
p
	​

 amplitude, yet it is described as “1.5% in f
CW
	​

 units” and “3×10
−2
 in A
p
	​

 units.” The manuscript also calls a 52–54% modeled fraction a “minority.” All A, A
p
	​

, and f
CW
	​

−1/2 conventions and every percentage comparison require a complete numerical audit.

[MINOR] Appendix B and Table XI, training/validation provenance: the manuscript does not demonstrate object-level deduplication across the GZ1 and CE-ResNet sources, exclusion of related images from opposite sides of the train/validation split, or why training-only flip augmentation adds only 826 images to a training set of more than 20,000. These details are necessary to assess leakage, and the 93.7% validation accuracy should not be emphasized as independent accuracy when most supervision consists of pseudo-labels.

[MINOR] Sections IV B and V, attribution and comparison with prior work: the global monopole is labeled a classifier artifact without a decisive control separating classifier, imaging, sample-selection, and human-label effects. Likewise, reproducing monopole–mask leakage in this pipeline does not attribute signals from a distinct Ganalyzer estimator and different cuts. Both claims should be recast as pipeline-specific possible mechanisms pending a matched-footprint reanalysis.

[MINOR] Organization throughout: the manuscript is excessively repetitive, repeatedly redefines which values are “primary,” and mixes measurement, diagnostic, completeness, and exclusion statistics in ways that obscure rather than clarify their logical status. It should be substantially shortened, with one fixed primary estimator, one fixed null, one amplitude convention, a formal limit, and a separate compact section for non-primary diagnostics.

(3) The central claim is supported only in the narrow estimator-conditional sense that the selected high-confidence hard-label map shows no significant real-space dipole; it is not yet supported as a survey-wide physical null at the stated sub-percent sensitivity.
