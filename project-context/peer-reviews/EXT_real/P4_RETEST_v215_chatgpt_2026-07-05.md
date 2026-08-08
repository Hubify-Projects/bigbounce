# P4 v1.0.215 EXT re-test — CHATGPT (record)

- Reviewer: ChatGPT (Pro, extended thinking)
- Date: 2026-07-05 (run 2026-07-06)
- PDF: /tmp/retest_P4_v215.pdf (976281 B)
- Chat URL: https://chatgpt.com/c/6a4c3bb0-712c-83e8-a6fe-eaf045d4a908
- Prompt: standard PRD referee prompt (verdict + [MAJOR]/[MINOR] issues + central-claim sentence)
- Verdict (verbatim from "(1) VERDICT:" line): **REJECT**
- Issue counts: 11 [MAJOR], 3 [MINOR]

## RAW VERBATIM RESPONSE

(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Secs. III B/IV C, “pre-specified” primary high-confidence cut: the central null depends on adopting peq > 0.6, while the unthresholded and peq ≤ 0.5 samples give z ≈ 4–4.4 excesses; a commit hash without a frozen public preregistration record is not sufficient to establish that this cut was fixed before inspecting the dipole/systematics behavior. 

retest_P4_v215

[MAJOR] Secs. IV C–IV D, treatment of the +7σ MASTER residuals: the manuscript declares large harmonic residuals “diagnostic only” and not cosmological, but they are measured from the same chirality field and remain at +7.28/+7.93σ under stated nulls; dismissing them requires a predictive nuisance model, not a post-hoc estimator hierarchy.

[MAJOR] Sec. IV D, residual-systematics attribution: the forward model explains only about 52–54% of the observed ℓ = 1 residual and explicitly leaves roughly 47% open, yet the manuscript still treats the residual as systematics-attributed; this is not adequate support for excluding a residual astrophysical or analysis-induced signal.

[MAJOR] Sec. II and Appendix B, classifier validity: 66.5% of the training labels are CE-ResNet pseudo-labels, the independent GZ1 chirality accuracy is only 69.91%, and the catalog probabilities are strongly overconfident; the downstream dipole analysis uses hard argmax labels without a full likelihood propagation of spatially varying misclassification.

[MAJOR] Secs. III A/IV C, null construction: pixel permutations and per-galaxy label shuffles destroy coherent sky structure by construction and therefore cannot test the dominant failure mode here, namely survey-correlated classifier errors tied to depth, PSF, morphology, imaging leg, or pseudo-label inheritance.

[MAJOR] Sec. VI A, GZ1-only rebuttal: the human-label-only test has N ≈ 46,000, roughly twenty times smaller than the headline high-confidence sample, so it cannot bound sub-percent dipoles at the claimed sensitivity; it is a useful sanity check but not a decisive independence test.

[MAJOR] Appendix D/Table XIII, block-bootstrap WLS “z ≈ −18” exclusion: the statistic is not a calibrated exclusion significance because the nuisance basis is incomplete, the design matrix is rank-deficient before repairs, classifier uncertainty is not included in the bootstrap covariance, and the fit uses a different sample/estimator from the primary high-confidence real-space null.

[MAJOR] Secs. IV D/V/VII, comparison with Shamir: the manuscript repeatedly argues amplitude-level tension with Shamir-class signals while acknowledging no matched-footprint Ganalyzer reanalysis was performed; this should be framed as a non-comparable pipeline result, not as substantive evidence against the earlier estimator.

[MAJOR] Sec. IV D/Table VI, monopole-mask leakage claim: reproducing 99.32% of the pre-MASTER pseudo-Cℓ power does not explain the post-MASTER residual, where the monopole-only null reportedly accounts for only about 12%; the manuscript overuses the pre-MASTER result to motivate broader conclusions.

[MAJOR] Secs. IV C/VI B/VII, sensitivity and falsification thresholds: A50, A95, harmonic completeness, moment-z, rank-p, and block-bootstrap z are defined under different samples, masks, weights, axis draws, and nulls; the manuscript says they are not interchangeable but still uses them together rhetorically to support one conclusion.

[MAJOR] Data Availability, reproducibility: many key claims depend on repository-internal artifact paths and a live main branch, while the manuscript states that the frozen archival snapshot and DOI are not yet deposited; this is insufficient for a PRD-level reproducibility claim.

[MINOR] Abstract and Sec. III A, presentation of significances: the abstract is overloaded with mutually non-comparable σ values and caveats, making the physical claim hard to parse and increasing the risk that readers misinterpret diagnostic residuals as detection significances.

[MINOR] Notation/units throughout Secs. IV–VII: the manuscript alternates between fCW-deviation units, Ap units, pseudo-Cℓ normalizations, and rescaled canonical/apodized field conventions; a single consolidated convention should be imposed before any comparison of amplitudes.

[MINOR] Appendix B/Table XI, bias-hardening tests: several tests are implementation or sanity checks rather than evidence of sub-percent bias control, especially T1, which is guaranteed by the TTA protocol; the table should not be presented as a strong bias audit.

(3) The narrow statement that the selected peq > 0.6 real-space dipole is consistent with its own permutation null is supported, but the broader central claim of a robust survey-scale cosmological null with controlled leakage and systematics is not supported by the evidence presented.
