(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Sections III B and IV C, “pre-specified” p
eq
	​

>0.6 primary sample: the cited code commit is not a prospective registration or an untouched holdout, and the manuscript explicitly justifies 0.6 as the first threshold at which the z≃4.0−4.3 excess at lower cuts disappears. This is outcome-dependent sample selection. The threshold scan must be incorporated into the inference, or the selection must be fixed using independent validation data before cosmological unblinding. 

h17_P4

[MAJOR] Sections II B, IV A, and VI A, classifier validity: 66.5% of the training labels are CE-ResNet pseudo-labels, the independent spiral-chirality accuracy is only 69.91%, the independent three-class accuracy is 58.7%, and the confidence scores are strongly overconfident. No confusion matrix is provided for the actual p
eq
	​

>0.6 science sample as a joint function of sky position, imaging leg, depth, PSF, morphology, and confidence. Consequently, the assertion that classification error merely dilutes a real dipole is unjustified; spatially varying asymmetric errors can create, suppress, or reverse a dipole. The N≃4.6×10
4
 human-only test is explicitly insensitive to the sub-percent regime and therefore does not validate the headline constraint.

[MAJOR] Section III D and Appendix B, equivariance claim: horizontal-flip averaging guarantees a soft-output mirror-swap identity, not rotational equivariance or stable hard labels. The reported 21.4% change in argmax labels between Z
2
	​

 and D
4
	​

 inference is substantial, while the D
4
	​

 tests use only two small, non-spatially stratified subsamples. Spatially varying PSF anisotropy and galaxy-position-angle distributions can therefore generate a sky-dependent hard-label bias. Production-scale D
4
	​

 inference or a genuinely rotation-equivariant classifier, followed by sky-stratified validation, is required.

[MAJOR] Section VI B and the abstract/conclusions, injection–recovery interpretation: the injections are made directly into the already selected hard-label CW/CCW field and bypass the image classifier, not-spiral triage, confidence cut, and spatially varying confusion. Thus A
50
	​

 and A
95
	​

 characterize only the observed classifier-output map. They are not physical galaxy-chirality sensitivity thresholds, contrary to the falsification and cosmological statements. The manuscript is internally inconsistent when it first says classifier dilution is “folded into” these floors and later correctly admits that the injections do not traverse the classifier. An image-level end-to-end injection or a validated conditional transfer model is necessary.

[MAJOR] Section VI B, “3σ” recovery criterion: the dipole amplitude is positive-definite, and the manuscript explicitly states that its moment-z statistic does not obey the Gaussian z-to-p mapping. Nevertheless, recovery is defined by moment z>3. The resulting A
50
	​

 and A
95
	​

 therefore do not correspond to a controlled 3σ false-alarm probability. Recovery must instead be defined against a pre-specified empirical null quantile or rank-p threshold.

[MAJOR] Section IV C, primary null calibration: permuting pixel asymmetries across the footprint assumes exchangeability, but the pixels have strongly varying galaxy counts, label quality, depth, and noise variance. This permutation destroys the association between variance and sky position. The per-galaxy shuffle preserves counts but still imposes a spatially constant label probability and deliberately removes the survey-correlated classifier structure that must be present under a realistic instrumental null. The observed confidence-cut dependence, significant hemisphere statistic, and large harmonic residuals demonstrate that exchangeability is not satisfied. A generative or hierarchical null containing spatially varying classification and selection effects is required.

[MAJOR] Sections IV C–D and Appendix D, incompatible low-ℓ results: the real-space and harmonic estimators are correlated measurements of the same sky label field, not logically independent experiments that can be made consistent merely by designating one “primary” and the other “diagnostic.” The full field exhibits highly significant non-random low-ℓ structure, and approximately 47% of the harmonic residual remains unexplained. The claim that this remainder is harmless because it lies below A
50
	​

 or A
95
	​

 is incorrect: recovery thresholds are power measures, not upper bounds on contamination or bias. A joint covariance and nuisance model must demonstrate that the same systematics cannot bias the real-space estimator.

[MAJOR] Appendix D, z≃−18 WLS claim: the block-bootstrap distribution is centered on the observed estimate; it is not a sampling distribution generated under A
ref
	​

, a likelihood-ratio test, or a calibrated confidence construction. The fit also reduces a three-component dipole with an unknown direction to a scalar-amplitude comparison and is performed on the full sample known to contain the low-confidence systematic. Moreover, the statement that ignoring classifier dilution makes the result conservative is backwards. Under the manuscript’s own g=0.398, an underlying A
ref
	​

=0.034 maps to an observed amplitude of approximately 0.0135, giving roughly z=−5.5, not −18, before other transfer uncertainties are included. This statistic cannot serve as a primary cosmological exclusion.

[MAJOR] Abstract and Sections V–VI, comparison with Shamir: the manuscript doubles Shamir’s quoted 1.7%–4.0% asymmetry to 3.4%–8.0% in A
p
	​

 units. The cited DESI analysis explicitly defines its asymmetry as (N
CW
	​

−N
CCW
	​

)/(N
CW
	​

+N
CCW
	​

), which is already identical to Eq. (3) of this manuscript; doubling is therefore unjustified unless the authors demonstrate that the particular quoted numbers instead denote f
CW
	​

−0.5. This apparent factor-of-two error propagates into A
ref
	​

=0.034, the z≃−18 claim, and the stated 7–18-fold tension. No matched footprint, redshift selection, object selection, or estimator comparison is performed in any case. 
arXiv

[MAJOR] Section IV D and Section V, 99.32% leakage claim: drawing a constant CW probability equal to the observed global monopole on the exact mask and measuring an unsubtracted pseudo-C
1
	​

 shows that this manuscript’s raw field contains the expected monopole–mask coupling. It does not establish that earlier Ganalyzer results arose from the same mechanism. Extending this pipeline-specific diagnostic to prior literature without a matched Ganalyzer reanalysis is unsupported.

[MINOR] Section VI C, theoretical interpretation: the manuscript admits that no transfer function has been derived from primordial parity-violating physics to projected galaxy morphology, yet states that cosmic birefringence and Chern–Simons scenarios would generically produce a morphology dipole and are bounded by this analysis. Those claims must be removed or supported by an explicit model and quantitative transfer calculation.

[MINOR] Scope, presentation, and reproducibility: the headline invokes 8.5 million galaxies although the primary dipole test uses 949,584 objects, while the second purported primary result uses a different 3.2-million-object sample. The manuscript is also excessively repetitive and presents several incompatible “σ” values for closely related channels. In addition, the Data Availability section says that the immutable release, exact commit hashes, and DOI will be supplied later; a live branch and internal artifact paths are not an adequate archival record for review or publication.

(3) The evidence supports only a null in the post-selected classifier-output field, not the claimed sub-percent null for the underlying cosmological galaxy-chirality dipole.
