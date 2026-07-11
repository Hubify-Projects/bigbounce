# INT API Review — P4 v1.0.235 — openai (gpt-5.5)
paper: P4  version: v1.0.235  model: gpt-5.5
modality: native-PDF (Files API input_file)
UTC: 2026-07-11T02:31:04.091659Z  |  latency: 57.5s  |  attempt: 1
usage: {"input_tokens": 62065, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 1806, "output_tokens_details": {"reasoning_tokens": 516}, "total_tokens": 63871}
PARSED VERDICT: REJECT

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: REJECT.

(2) ISSUES:

1. [MAJOR] Secs. III B, IV C, VI B — The declared “primary” result is defined on a high-confidence subsample containing only about 30% of the classified spirals, while the unthresholded catalog gives a significant dipole-like excess; the manuscript attributes this entirely to systematics, but does not provide a pre-analysis, image-level, selection-function model showing that the confidence cut cannot remove or suppress a real sky-dependent signal.

2. [MAJOR] Sec. VI B — The injection–recovery study injects signals only into the already-classified hard CW/CCW labels, not into images passed through the classifier, not spiral triage, confidence selection, and sky-dependent confusion; therefore the quoted A50 and A95 thresholds are thresholds for an observed-label map, not for a physical galaxy-chirality dipole, and the manuscript repeatedly overstates them as cosmological sensitivity/falsification thresholds.

3. [MAJOR] Secs. II, IV A, Appendix B — The classifier validation is inadequate for the claimed sub-percent cosmological inference: the independent GZ1 chirality accuracy is only 69.91%, the softmax outputs are strongly miscalibrated, 66.5% of training labels are CE-ResNet pseudo-labels, and the human-only GZ1 cross-check is explicitly insensitive to sub-percent amplitudes; this does not establish that spatially varying classifier confusion is below the claimed signal floor.

4. [MAJOR] Secs. III A–IV D, Tables II–V — The statistical framework is not coherent. Multiple incompatible nulls, masks, field definitions, weights, sample selections, and σ conventions are used, with values ranging from +0.41σ to +7.93σ and a block-bootstrap “z ≈ −7.6”; the manuscript repeatedly states these are not comparable, but nevertheless uses them jointly to support a single cosmological conclusion.

5. [MAJOR] Sec. IV D and Appendix D — The harmonic channel shows highly significant low-ℓ residuals, including +7σ-level MASTER diagnostics, and the proposed systematic explanation is incomplete: the forward model explains only about 53% of the ℓ = 1 residual amplitude, leaving an explicitly unresolved ∼47%; this is not sufficient to dismiss the residuals while simultaneously claiming sub-percent sensitivity.

6. [MAJOR] Sec. IV C — The primary real-space null uses an isotropic pixel-permutation null that does not naturally preserve the spatially varying shot noise, survey depth, morphology distribution, and confidence-selection function of the data; the label-shuffle cross-check helps but is still a shuffle of the model’s own outputs and does not test inherited or survey-correlated classifier errors.

7. [MAJOR] Secs. III B, IV D, Appendix D — The block-bootstrap WLS “exclusion” of a clean 1.7% dipole is not a calibrated frequentist or Bayesian exclusion, is performed on a different sample from the primary high-confidence estimator, and uses a spatial covariance model whose adequacy is not demonstrated; it should not be presented as a primary cosmological estimator.

8. [MAJOR] Secs. V–VII — The comparison with Shamir is overstated. The authors correctly note that no matched Ganalyzer reanalysis is performed, but still claim strong amplitude-level tension and “would have been detected” statements under their pipeline; this is not a like-for-like likelihood comparison and should be substantially toned down or removed.

9. [MAJOR] Appendix B and Data Availability — The released catalog contains a nontrivial flip-identity/probability reconstruction QC problem affecting 2.9% of rows and 59,515 high-confidence rows; although the authors state that excluding them does not change one statistic, this raises concerns about pipeline provenance and requires a clean regenerated catalog before publication-level inference.

10. [MAJOR] Secs. IV B, VI C — The manuscript conflates or shifts between parity-even dipole language, parity-odd monopole language, morphology chirality, projected handedness, and angular-momentum interpretation. The connection to parity-violating sectors is speculative and lacks the transfer function the text acknowledges is required.

11. [MAJOR] Throughout — The manuscript is excessively long, internally repetitive, and contains many artifact-path assertions rather than transparent statistical derivations. A PRD submission must present a concise, reproducible analysis with a small number of well-defined estimators, not a sprawling audit log.

12. [MINOR] Abstract and Conclusions — The abstract contains too many numerical diagnostics from different null procedures and is difficult to parse; it should state one primary estimator, one sample, one null, and one conclusion.

13. [MINOR] Sec. IV C — The dipole direction quoted for a null result should either be omitted or clearly relegated to a non-result, since the axis is unconstrained under the null.

14. [MINOR] Tables II–V — The tables mix quantities with different normalizations, fields, and nulls; they should be split into primary cosmological results and non-primary diagnostic checks, with no shared “σ” column across incommensurable statistics.

15. [MINOR] Data Availability — The manuscript says the archival Zenodo DOI and exact commit hashes will be inserted later; for review and reproducibility, the frozen code/catalog/artifact version must be available at submission.

16. [MINOR] Figures 4, 7, 8, 9 — Several figures show visually or statistically significant structures while captions state they are systematics; the figures need clearer separation between diagnostic and primary plots, and should avoid reinforcing contradictory interpretations.

17. [MINOR] Sec. II and Appendix B — The training/validation description is confusing, especially the augmentation accounting and overlap with GZ1/CE-ResNet; it should be simplified and accompanied by a clear data-flow diagram.

(3) The central claim is only partially supported: the selected high-confidence real-space estimator is consistent with null, but the broader claim of a robust sub-percent cosmological null/exclusion is not supported by the present statistical and classifier-systematics treatment.