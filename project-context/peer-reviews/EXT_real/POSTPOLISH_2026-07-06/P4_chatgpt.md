# EXT POSTPOLISH 2026-07-06 — P4 — ChatGPT

- **Provider:** ChatGPT (Pro), Big Bounce Book project
- **Model/effort:** Pro Extended
- **Chat URL:** https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a4ca4ce-c1d8-83e8-b036-4b5cdad81f3d
- **PDF:** P4_v1.0.219.pdf (md5 54118d50f6768507e4e22ec5611cf33b)
- **Harvested:** 2026-07-07
- **Thought for:** 7m 38s
- **Parsed verdict (from response):** REJECT

## Raw verbatim response

(1) VERDICT: REJECT.
(2) ISSUES:

[MAJOR] Secs. III B/IV C/title/abstract — the central "8.5 million DESI galaxies" null claim is not the measurement actually used for the headline null: the primary real-space result uses only the high-confidence peq>0.6 subsample with 949,584 spirals, about 30% of the 3,201,160 classified spirals, while the unthresholded full in-mask sample yields a significant z≈4.2–4.4 dipole that is then reclassified as a systematic. This is not acceptable without a blinded, externally fixed sample definition and a primary result stated as "in the high-confidence subsample," not "in 8.5 million galaxies."

[MAJOR] Secs. III B/IV C — the claimed pre-specification of peq>0.6 is not adequate. A Git commit containing the same estimator and threshold is not a pre-registration record in the statistical sense, and the text explicitly justifies 0.6 because it is the lowest threshold that removes the depth-correlated excess. That makes the primary null vulnerable to selection on the outcome/systematic structure.

[MAJOR] Secs. III B/IV C/IV D/VII — the paper declares strongly non-null ℓ=1 harmonic results and hemisphere results to be "diagnostic" by fiat rather than by a coherent likelihood. The manuscript reports +3.64σ, +7.28σ/+7.13σ, +7.93σ, and pLEE≤10^-4 residuals, then asserts they do not bear on the cosmological conclusion because the real-space estimator is primary. A PRD-level analysis must instead provide a single statistical model explaining why these ℓ=1-sensitive observables reject the shuffle/null hypotheses while the chosen real-space estimator is privileged.

[MAJOR] Sec. IV D/Appendix D — the systematics attribution is incomplete. The forward model explains only about 53% of the observed ℓ=1 residual and leaves roughly 47% as an "open item," yet the manuscript treats the residual as safely non-cosmological and non-load-bearing. An unexplained low-ℓ residual in the same observable family cannot be dismissed while claiming a robust null.

[MAJOR] Secs. II/IV A/Appendix B — classifier validation is insufficient for sub-percent cosmology. The catalog-wide mean confidence is 0.951 while independent GZ1 three-class accuracy is only 58.7% and spiral-chirality accuracy is 69.91%; precision/recall values are modest. The assertion that overconfidence "cannot bias" the dipole because hard labels are used is not demonstrated for spatially varying misclassification coupled to depth, seeing, morphology, or survey leg.

[MAJOR] Secs. II/VI A — the training-label independence problem remains material. The paper states that 66.5% of training labels derive from CE-ResNet predictions and that validation partly measures agreement with CE-ResNet; the GZ1-human-only check has only 46,017 high-confidence spirals, a factor of about 21 below the headline HC sample, and cannot validate sub-percent spatial systematics in the full DESI footprint.

[MAJOR] Sec. VI B — the sensitivity and falsification thresholds are not strong enough for the claims made. The A50≈0.75% and A95∈(1.0%,1.5%] thresholds are estimator- and cut-specific, are based on coarse injected amplitudes, and the manuscript admits the "true-underlying" threshold is roughly 1.88% under an approximate symmetric-error model. This does not support broad "sub-percent" cosmological sensitivity without stronger classifier-error propagation.

[MAJOR] Appendix D/Table XIII — the block-bootstrap WLS "z≈−18" exclusion is over-weighted rhetorically. The design matrix is rank-deficient before nuisance handling, the statistic is explicitly not a calibrated detection significance, and it tests only a clean dipole template under a particular spatial bootstrap model. It should not be presented as a primary exclusion on the same footing as a cosmological likelihood.

[MAJOR] Sec. V/Sec. VI C/VII — the comparison with Shamir is not publication-ready. The manuscript repeatedly states "amplitude-level tension" and not a frequentist exclusion, yet also uses phrases such as "disfavors," "would be unmissable," and "no-dipole-at-ℓ=1 verdict" while comparing different classifiers, footprints, selections, and estimators. A matched-footprint reanalysis or a much more limited claim is required.

[MAJOR] Appendix C/Table I — the statement "No directional hemispheric asymmetry survives look-elsewhere control" is internally inconsistent with the reported direct-MC max-statistic pLEE≤10^-4, which is a rejection of the random-label max-statistic null. The subsequent systematics interpretation may be plausible, but the claim as written is false.

[MAJOR] Data Availability/Appendix B — reproducibility is not at PRD archival standard. The manuscript relies on a live main branch, says the immutable snapshot and Zenodo DOI have not yet been deposited, and reports a raw/equivariant pipeline-pass mismatch affecting 2.9% of rows and 59,515 HC rows. Even if the headline number is unchanged after filtering, the production catalog and analysis artifacts must be frozen and internally consistent before review.

[MINOR] Secs. III A–VII — the presentation is excessively complex and repeatedly explains that σ values are incomparable rather than reducing the analysis to a clean statistical hierarchy. A PRD paper should remove diagnostic overgrowth, move most artifact-level provenance to supplemental material, and present one primary likelihood or estimator family with consistent notation.

[MINOR] Sec. VI C — the parity discussion should be shortened and sharply separated from the measurement. The paper correctly says the ℓ=1 chirality dipole is parity-even and not a direct parity-violation test, but the surrounding comparisons to parity-violating sectors invite overinterpretation without a transfer function.

(3) The central claim is supported only in the narrow sense that the preselected high-confidence real-space estimator gives a null result; the manuscript does not support the broader claim of a robust null chirality dipole in the full 8.5M-galaxy catalog because significant low-ℓ residuals, sample-selection dependence, classifier systematics, and incomplete residual modelling remain unresolved.
