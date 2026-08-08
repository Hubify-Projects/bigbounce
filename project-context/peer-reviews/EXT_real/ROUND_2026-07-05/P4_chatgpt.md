# EXT Review — P4 × ChatGPT
- paper: P4
- version: v1.0.212
- reviewer: ChatGPT
- model: Pro Extended
- timestamp: 2026-07-06T19:18:37Z
- chat_url: https://chatgpt.com/c/6a4bfe28-9ef4-83e8-bdc4-13680b0525de
- pdf: /tmp/round_P4.pdf

## Raw verbatim response

(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Abstract / Secs. III B–IV D — The manuscript’s declared “primary” analysis is not a stable analysis hierarchy: the high-confidence real-space dipole uses only peq > 0.6 spirals, while another “primary” exclusion uses the full Catalog C, and the full/unthresholded real-space sample gives a z ≈ 4.2–4.4 excess. Reclassifying the inconvenient full-sample and harmonic excesses as “systematics-attributed” without a validated generative correction is not sufficient for a PRD-level null result.

[MAJOR] Sec. II B / Appendix B — The classifier is not validated to the precision required for a sub-percent cosmological anisotropy claim. The independent GZ1 chirality agreement is only 69.91% with κ = 0.40, the three-class GZ1 accuracy is 58.7%, and 66.5% of training labels derive from CE-ResNet pseudo-labels; this makes the catalog a noisy model-derived label field, not an independently calibrated chirality measurement at the claimed sensitivity.

[MAJOR] Secs. IV A–IV C — The confidence threshold peq > 0.6 is not statistically justified as a pre-specified selection. The manuscript says the threshold is “fixed a priori” because it appears in a generator script, but no time-stamped preregistration or blinded analysis protocol is provided, and the threshold is exactly where the significant low-confidence excess disappears. A confidence-cut sweep does not remove the selection problem; it shows that the conclusion depends on discarding a large, systematic-bearing part of the data.

[MAJOR] Secs. III A, IV C, IV D, Appendix A — The null distributions are inadequate for the claimed cosmological inference. Pixel permutation destroys sky-depth, footprint, seeing, morphology, and classifier-response correlations; per-galaxy label shuffling preserves counts but randomizes away exactly the spatially coherent classifier/systematic structures under investigation. These nulls can diagnose non-randomness, but they cannot establish absence of a cosmological dipole in the presence of survey-correlated classifier bias.

[MAJOR] Secs. IV C–IV D / Table IV — The manuscript contains large positive harmonic residuals, including MASTER ℓ = 1 diagnostics at approximately +7σ, while asserting a null cosmological result. The claim that these are merely diagnostic systematics is not demonstrated quantitatively: the forward model explains only about 52–54% of the residual amplitude and leaves roughly 47% open. An unexplained low-ℓ residual of this size is incompatible with presenting a clean null result.

[MAJOR] Appendix D / Table XII / Fig. 10 — The block-bootstrap WLS “z ≈ −18” exclusion of a clean 1.7% dipole is not a calibrated exclusion. It compares a fitted amplitude after nuisance-template regression to a chosen reference amplitude using a bootstrap over observed residuals, while not fully propagating classifier uncertainty, pseudo-label inheritance, morphology-dependent label failure, or a simultaneous cosmological-plus-systematics likelihood. It should not be used as a primary cosmological exclusion statistic.

[MAJOR] Sec. VI B / Table VII — The injection-recovery sensitivity floor is not an end-to-end sensitivity calibration. The injections are applied at the catalog/map-label level, not through image generation, classifier inference, confidence selection, pseudo-label bias, morphology triage, and survey-depth response. Therefore A50 ≈ 0.75% and A95 ∈ (1.0%, 1.5%] are estimator-level toy sensitivities, not defensible falsification thresholds for real galaxy chirality signals.

[MAJOR] Secs. I, VI C — The physical interpretation is overstated. The observable is projected apparent arm winding, not a deprojected spin vector, and the manuscript itself states that the ℓ = 1 channel is parity-even rather than a direct parity-violation test. The paper nevertheless frames the result in terms of parity and cosmological axial-vector sectors without a transfer function from primordial or late-time physics to the projected morphology-channel observable.

[MAJOR] Appendix E — Edge-on and morphology contamination remain a serious uncontrolled label-noise channel. The manuscript finds 15.8% of classified spirals have b/a < 0.3, yet treats the effect mainly as sensitivity dilution by appealing to soft-probability equivariance, while the actual estimator uses hard argmax labels. The caveat that hard argmax can reintroduce bias is acknowledged but not resolved with an independent morphology-controlled validation.

[MAJOR] Appendix C — The hemisphere look-elsewhere result is internally mischaracterized. A direct-MC max-statistic result pLEE ≤ 10−4 rejects the random-label null; calling this “no directional hemispheric asymmetry survives” is incorrect unless a quantitative systematic model is fitted and subtracted. The manuscript instead asserts systematic attribution.

[MAJOR] Data Availability — The reproducibility state is not acceptable for a refereed result of this complexity. The paper relies on many artifact paths, a live main branch, and a promised future DOI. A PRD submission needs an immutable archive with exact commit, scripts, configuration, random seeds, null arrays, catalog version, and all tables/figures reproducible from that archive at submission time.

[MINOR] Abstract and Results presentation — The abstract is overloaded with caveats, mutually non-comparable significances, parenthetical qualifications, and artifact-level details. This obscures the actual claims and makes the paper read like a response document rather than a scientific article.

[MINOR] Tables I–V / Sec. III A — The manuscript repeatedly reports σ values from different nulls, masks, fields, weights, and run sizes while warning that they are not comparable. This is formally acknowledged but still confusing; the presentation should be reorganized so that each estimator has a single declared statistic, single null, and single role.

[MINOR] Sec. V — The comparison with Shamir is not a rigorous likelihood comparison. The manuscript correctly notes that a matched Ganalyzer reanalysis is required, but it still repeatedly describes “tension” and “disfavoring” in ways that invite overinterpretation.

[MINOR] Appendix B — The bias-hardening tests are weak relative to the claimed precision. Tests such as “CW/CCW balance 50 ± 10%” and “>30% at max p > 0.9” are far too coarse for a sub-percent anisotropy analysis and should not be presented as strong validation.

(3) The central claim of a robust null real-space chirality dipole is not supported by the evidence presented, because the null depends on a selected high-confidence subset while significant unthresholded and harmonic low-ℓ residuals remain only partially explained by demonstrated systematics. 

round_P4
