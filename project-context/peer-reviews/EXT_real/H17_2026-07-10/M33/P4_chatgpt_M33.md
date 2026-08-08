VERDICT: MAJOR REVISIONS

ISSUES:

[MAJOR] Abstract; Secs. II, VI B, and VII — the claimed end-to-end sensitivity to a physical chirality dipole is not demonstrated. The injection–recovery exercise injects a modulation only into the already classified hard-label field; it explicitly bypasses the ViT, the not-spiral triage, the confidence selection, and their spatially varying confusion. The later full-catalog mirror test verifies flip equivariance, but it is not a sky-dependent signal injection and therefore does not calibrate signal survival through those stages. Numerically, the manuscript’s own transfer factor g≃0.398 would map a physical 1.7% dipole to only ≃0.68% in the observed labels, below the quoted observed-label A
50
	​

≃0.75%; correspondingly, the observed-label A
95
	​

=1.0–1.5% maps to approximately 2.5–3.8% physically. Thus the statements that a “genuine Shamir-scale dipole would have been detected” and that classifier dilution is already folded into the recovery thresholds are not supported. A spatially varying, image-level injection through classification, triage, and the p
eq
	​

>0.6 selection is required, or all sensitivity claims must be restricted explicitly to the post-classification hard-label field. 

ext_P4_M33

[MAJOR] Sec. III B and Appendix D(g), especially Fig. 10 — the quoted z≃−7.6 is not a calibrated hypothesis test. The bootstrap distribution is constructed around the observed fitted amplitude, not under a data-generating model with A
ref
	​

=0.017, as the figure caption itself states. Moreover, the dipole amplitude is positive-definite, its sampling distribution is non-Gaussian near zero, and the dipole direction is an unspecified nuisance parameter. Subtracting A
ref
	​

 from the observed scalar amplitude and dividing by the bootstrap width therefore does not establish a 7.6-standard-deviation exclusion or a well-defined likelihood ratio. The authors should generate mock skies under fixed-amplitude dipoles over the full direction distribution, including the nuisance templates and selection function, or construct a joint likelihood for the three dipole components and profile or marginalize over direction. Until then, this statistic should not be designated a primary cosmological result.

[MAJOR] Sec. IV C — the primary confidence cut is inseparable from the result and is not adequately controlled as a selection choice. The unthresholded catalog and the p
eq
	​

≤0.5 cumulative selections give z≃4.0–4.4, while the result collapses to null at p
eq
	​

>0.6, after discarding roughly 70% of the classified spirals. A commit containing both the estimator and cut is not an independent preregistration record, and the stated rationale explicitly uses the observed transition at 0.6 to identify the “systematic tail.” The authors need either a genuinely external, time-stamped analysis protocol with the threshold chosen solely from independent validation data, or a statistical treatment of the cut scan and selection uncertainty. Most importantly, they must show with end-to-end injections that a real sky dipole is not preferentially removed by the confidence cut.

[MAJOR] Secs. II and VI A; Appendix B(d,h) — classifier validation is not sufficient for a sub-percent anisotropy measurement. The independently measured chirality accuracy is only 69.91%, the human-label test has a several-percent recovery floor and therefore cannot validate the headline sub-percent regime, and the science-cut differential-error confidence interval still permits errors at the several-10
−3
 level, comparable to the claimed sensitivity. The two imaging-leg split does not constrain RA-dependent or jointly depth/PSF/morphology-dependent error variation within each leg. In addition, changing from Z
2
	​

 to D
4
	​

 averaging changes 21.4% of argmax labels on the reported test samples, which is substantial for an observable that should be invariant under image rotation. The paper needs a representative, sky-stratified human-labeled validation set, results for the actual p
eq
	​

>0.6 science sample, and a quantitative rotation-invariance test or production-level rotation averaging.

[MAJOR] Sec. IV C — the primary randomization null does not constitute a realistic cosmological measurement likelihood. Permuting pixel asymmetries assumes exchangeability despite large variations in N
spiral
	​

(p), depth, morphology, and classification quality. The per-galaxy label-shuffle cross-check preserves pixel counts, but it still randomizes away spatially correlated classifier and survey errors and therefore tests random labels rather than the full null hypothesis relevant to the data. The primary inference should use a generative model that preserves the observed selection function and spatially varying confusion, with a covariance model validated on simulations. The paper should report the fitted dipole-vector components with their covariance and a frequentist confidence region or posterior upper limit; A
50
	​

 and A
95
	​

 recovery probabilities are not confidence limits on the measured amplitude.

[MAJOR] Secs. IV C–D and VII — the statistically non-null harmonic result remains quantitatively unresolved. The empirical harmonic-tail probabilities are of order 10
−3
, while the imaging-plus-morphology forward model accounts for only about 53% of the reported ℓ=1 amplitude and leaves approximately 47% explicitly unexplained. The argument that this remainder is harmless because it lies below A
50
	​

 or A
95
	​

 is invalid: recovery thresholds are detection probabilities, not bounds on the cosmological content of an observed mode, and the harmonic estimator is itself reported to have substantially better recovery at these amplitudes. A mixture of cosmological dipole and survey systematic has not been excluded. The authors should apply the harmonic estimator to the same p
eq
	​

>0.6 sample and mask as the primary real-space estimator and perform a joint, same-field consistency analysis before assigning the residual wholly to systematics. 

ext_P4_M33

[MAJOR] Sec. III A, Table V, and the Conclusions — “σ” is used in a materially misleading way for strongly non-Gaussian nulls. For example, the reported moment ratio z=7.31 has empirical p=6×10
−4
, while z=3.64 has p=0.030; neither has the tail probability conventionally implied by “7.3σ” or “3.6σ.” These quantities should be called standardized moment ratios, not significances in standard-deviation units, and empirical p-values with Monte Carlo uncertainty should be the primary reporting convention. The large shift between the several “canonical” values 3.64, 7.93, and related variants also requires one fixed field, mask, subtraction, and null definition rather than multiple convention-dependent results sharing the same label.

[MAJOR] Sec. VI A and Appendix D — the claim that inherited or survey-correlated bias can only push the estimator away from zero, making the null conservative, is incorrect. A spatially coherent additive bias is a vector in dipole space and can add to, rotate, or partially cancel a genuine sky dipole depending on its direction; multiplicative depth-dependent dilution can likewise suppress different sky regions unequally. The manuscript’s statement that the tested nuisance channels all move the result “toward null” is not established by the presented regressions. The two headline estimators are also not statistically independent, because both use the same classifier outputs and substantially overlapping sky data. A joint nuisance model is required before cancellation of a physical signal can be excluded.

[MAJOR] Secs. II A and III D — the manuscript lacks an essential image-parity and WCS-orientation audit. Because CW and CCW are interchanged by reflection but not by rotation, the analysis requires proof that the Smith42 cutouts have a common parity convention across BASS, MzLS, DECaLS, and the DES overlap. A survey-dependent WCS determinant or cutout-generation reflection could create or erase precisely the signal under study, and pixel-space horizontal TTA would not repair inconsistent parity conventions between survey regions. The authors should document the astrometric orientation and parity of every imaging branch and validate the full ingestion pipeline using synthetic spirals of known handedness.

[MAJOR] Data Availability and Appendices B–D — the analysis is not yet tied to an immutable, internally consistent release. The manuscript points to a mutable live main branch, states that the archival DOI and exact commit hashes will be inserted later, and acknowledges a raw/equivariant inference-pass mismatch producing unphysical reconstructed probabilities for a non-negligible subset. That catalog should be repaired and the affected analyses rerun, rather than merely distributing a flag. Several internal bookkeeping statements also require reconciliation, including the reported 3,200,420 versus 3,201,160 canonical-mask spiral counts and the description of per-galaxy morphology regression as both completed and future work. Acceptance requires a frozen catalog, code snapshot, checksums, and a single reproducible table of sample and mask counts. 

ext_P4_M33

[MINOR] Appendix B(g) — the stated ECE lower bounds are not calculated consistently. Jensen’s inequality applies when mean confidence and mean accuracy are evaluated on the same sample, but the manuscript compares the catalog-wide mean winning confidence with accuracy measured on the GZ1 cross-match. The confidence mean, accuracy, and reliability bins must all be recomputed on the identical matched sample; a conventional reliability diagram and class-conditional calibration statistics should replace the present bound.

[MINOR] Appendix C(c) — the look-elsewhere discussion contains a statistical error and needs reconciliation. Bonferroni control does not require independent tests; it remains valid under arbitrary dependence, although it can be conservative. The empirical claim p
LEE
	​

≤10
−4
 for a maximum whose quoted local standardized value is only 3.05 also needs a transparent definition of the per-direction statistic, the max-statistic normalization, and Monte Carlo convergence tests before it can be used as evidence for a coherent systematic.

The central claim is supported only in the narrow sense that the chosen p
eq
	​

>0.6 hard-label map is consistent with no real-space dipole under the stated randomization tests, not yet as a physical cosmological null or as an exclusion of a Shamir-scale dipole.
