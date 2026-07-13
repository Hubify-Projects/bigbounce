VERDICT: REJECT

ISSUES:

[MAJOR] Sec. IV C, definition of the primary p
eq
	​

>0.6 sample: the unthresholded catalog gives a z≃4.2−4.4 dipole, and the statistic collapses abruptly only when the cut reaches 0.6; because confidence is correlated with depth, morphology, angular size, and likely redshift, discarding the population carrying the signal does not establish that the signal is instrumental rather than selection-dependent astrophysics. A commit containing the cut is not a verifiable preregistration or blinding record, especially when the stated rationale for 0.6 is that it removes the observed excess; the threshold must be chosen from independent validation information, and the different-confidence populations must be matched or modeled jointly. 

ext_P4_M42

[MAJOR] Sec. VI B and the abstract, injection-recovery and the claim that a 1.7% dipole would be detected: the injections are made into the post-classification hard-label map, after the ViT, non-spiral triage, confidence selection, and spatially varying confusion have acted, so they do not calibrate sensitivity to a physical galaxy-chirality dipole. Under the manuscript’s own adopted transfer factor g=2a−1=0.398, the observed-label A
50
	​

=0.75% corresponds to a physical amplitude of about 1.88%, while A
95
	​

=1.0−1.5% corresponds to roughly 2.5−3.8%, before any further selection correction; consequently a physical 1.7% signal is not guaranteed to be detected. The full-catalog mirror-flip exercise is an equivariance identity imposed by the TTA construction, not an image-level population-dipole injection, and cannot repair this inconsistency.

[MAJOR] Sec. III A, Tables V and VIII, use of “σ” and recovery thresholds: the reported moment ratios are explicitly not Gaussian significances—the manuscript itself gives examples such as z=3.64 with empirical p=0.030, and z=7.93 with a much less extreme rank probability. Defining detection by “moment-z>3” therefore does not define a three-sigma false-alarm probability, so the quoted A
50
	​

, A
95
	​

, harmonic completeness, and falsification boundaries are not statistically calibrated. Recovery must instead be defined using an empirical critical value at a stated false-positive rate, with enough null simulations to resolve that tail.

[MAJOR] Appendix D, the z≃−7.6 WLS “clean-1.7%-dipole” disfavor: Fig. 10 is a bootstrap distribution around the observed estimate, not a sampling distribution under A
ref
	​

=0.017, and the scalar dipole amplitude is positive-definite with an unknown direction. The test also uses the full catalog containing the low-confidence population declared systematically contaminated, whereas the other primary estimator uses only the high-confidence sample; classifier dilution and the response of the nuisance regression are not propagated. In addition, no signal-injection study shows how much a true dipole is absorbed by the density, leg, confidence, and morphology-correlated templates on the cut sky. This quantity is not a calibrated hypothesis test and cannot serve as a primary cosmological exclusion.

[MAJOR] Secs. IV D and VI A, treatment of the unresolved low-ℓ residual: the manuscript forward-models only about 53% of the residual amplitude and leaves approximately 47%—about 0.32% in A
p
	​

—unexplained, while the full residual is about 0.70%. Declaring this harmless because it lies below A
50
	​

 is logically incorrect: a systematic below a detection threshold can still bias the fitted amplitude, alter coverage, or vectorially cancel a physical dipole. The repeated assertion that inherited or survey-correlated structure can only add power or move the estimator away from zero is false; coherent additive systematics can have either sign and phase. The residual must enter a nuisance covariance or joint likelihood rather than be removed from the error budget by a detectability argument.

[MAJOR] Sec. II and Appendix B, classifier validation at the claimed sub-percent precision: 66.5% of the training labels are CE-ResNet pseudo-labels, the internal random-split validation largely measures agreement with those labels, and the disjoint GZ1 chirality accuracy is only 69.91%. Table XIII also implies substantial non-spiral contamination among objects assigned CW or CCW, while Appendix E finds 15.8% edge-on contamination. The two-leg confusion analysis has differential-error confidence intervals of order 0.6−1.4 percentage points, comparable to or larger than the claimed signal scale, and does not constrain RA-dependent or finer depth/morphology-dependent errors. The GZ1-human-only test has A
95
	​

∼4.5−6.8%, so it cannot validate the sub-percent headline result.

[MAJOR] Sec. IV C, construction of the primary null: permuting pixel asymmetries assumes exchangeability despite strongly varying per-pixel counts and noise, while the global label shuffle preserves counts but not spatially varying class fractions, confidence distributions, morphology, or confusion matrices. Both procedures also erase intrinsic spatial spin correlations and therefore do not provide the covariance appropriate to a cosmological dipole measurement. The weighting/mask checks do not replace a covariance-aware likelihood or realistic null mocks incorporating the survey selection and spatially varying classification response.

[MAJOR] Sec. IV D, “99.32% monopole-mask leakage” and the comparison with earlier work: applying a patchy mask to an uncentered field with a nonzero mean necessarily generates nonzero pseudo-C
ℓ
	​

, so reproducing the un-subtracted ℓ=1 power with a constant-monopole simulation is largely a consequence of the estimator definition, not evidence for a new physical systematic. A proper real-space fit includes an intercept, and the manuscript’s own post-subtraction/post-MASTER residual remains non-null. This construction cannot be used to attribute results from Ganalyzer or other estimators to the same leakage channel without a matched-footprint, matched-selection reanalysis.

[MAJOR] Secs. VI B–C and the Conclusions, absence of a physical upper limit: the manuscript explicitly states that neither the null quantile nor A
95
	​

 is a confidence upper limit, and it supplies no likelihood or confidence region for the dipole vector after marginalizing classifier and survey systematics. Consequently the work does not presently yield a quantitative cosmological constraint, despite repeated claims of “sub-percent sensitivity,” tension with previous amplitudes, and implications for parity-violating sectors. The cosmic-birefringence and Chern-Simons discussion is especially speculative without the transfer function that the manuscript acknowledges is absent.

[MINOR] Data Availability and Appendix B: the analysis points to a mutable live branch, the DOI and exact frozen hashes are still placeholders, and the released catalog retains a sizeable subset with internally inconsistent raw/equivariant probability provenance. An immutable archive, corrected catalog, exact environment, and end-to-end reproduction of every headline number are required before publication.

[MINOR] Overall presentation: the manuscript is excessively repetitive and uses several incompatible field, mask, weighting, and null conventions while repeatedly calling different constructions “canonical”; values such as +3.64, +7.28, and +7.93 are consequently easy to misread despite extensive caveats. The paper should be substantially shortened and reorganized around one prespecified estimator, one sample, a calibrated likelihood, and a clearly separated set of diagnostics.

The central claim is not supported as a physical or cosmological null, nor as an exclusion of a Shamir-scale dipole, although the narrower descriptive statement that the selected p
eq
	​

>0.6 classifier-output sample has a low fitted real-space dipole statistic is supported.
