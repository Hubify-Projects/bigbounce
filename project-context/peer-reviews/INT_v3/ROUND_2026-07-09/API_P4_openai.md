# INT API Review — P4 v1.0.237 — openai (gpt-5.5)
paper: P4  version: v1.0.237  model: gpt-5.5
modality: native-PDF (Files API input_file)
UTC: 2026-07-12T16:21:51.262751Z  |  latency: 89.9s  |  attempt: 1
usage: {"input_tokens": 61423, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 2654, "output_tokens_details": {"reasoning_tokens": 1034}, "total_tokens": 64077}
PARSED VERDICT: REJECT

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: REJECT

(2) ISSUES:

1. [MAJOR] Secs. III B, IV C, VI B, VII — Primary estimator and sample selection are not statistically justified: the manuscript declares the high-confidence \(p_{\rm eq}>0.6\) real-space estimator as “primary” precisely where the signal disappears, while the unthresholded catalog shows a \(z\simeq 4.2\) real-space excess and the harmonic channel shows \(z\simeq 7\) residuals. A git commit is not a credible pre-registration, and the confidence-cut selection function is not propagated into the covariance or into a joint likelihood.

2. [MAJOR] Secs. II, IV A, Appendix B — The chirality labels are insufficiently validated for the claimed cosmological use: 66.5% of the training labels are CE-ResNet pseudo-labels, the independent GZ1 chirality accuracy is only 69.91% with \(\kappa=0.40\), the three-class external accuracy is 58.7%, and the softmax scores are strongly miscalibrated. This is not adequate to claim sub-percent isotropy bounds without a spatially resolved, externally validated confusion model.

3. [MAJOR] Secs. III A, IV C, VI A — The permutation and label-shuffle nulls are not valid cosmological nulls for the dominant failure mode: they randomize the model’s own labels and therefore erase survey-correlated classifier bias, depth dependence, pseudo-label inheritance, and morphology-dependent selection effects. The manuscript acknowledges this limitation but then continues to use these nulls for headline sensitivity and consistency claims.

4. [MAJOR] Secs. IV C–D, Appendix D — The harmonic residuals are large, internally inconsistent, and not adequately modeled: the paper reports \(+3.64\sigma\), \(+7.28\sigma\), and \(+7.93\sigma\) low-\(\ell\) residuals under different conventions, then labels them “diagnostic” without providing a coherent joint statistical model. Declaring them non-primary does not remove the need to explain why a purported null catalog has highly significant low-\(\ell\) structure.

5. [MAJOR] Sec. IV D — The “47% open item” in the post-MASTER residual is fatal for the claimed systematics closure. The manuscript states that roughly half of the \(\ell=1\) residual amplitude is not explained by the imaging/morphology forward model, yet still attributes the residual to systematics and asserts it does not affect the null. That is not a demonstrated conclusion; it is an assumption.

6. [MAJOR] Secs. VI B, VII — The injection–recovery study is not end-to-end: injected signals are added to the observed hard-label CW/CCW map, not to galaxy images before classification, not through the not-spiral triage, and not through the \(p_{\rm eq}\) selection. Therefore the quoted \(A_{50}\simeq0.75\%\) and \(A_{95}\in(1.0\%,1.5\%]\) are estimator-level observed-label thresholds, not physical chirality-dipole sensitivity limits.

7. [MAJOR] Secs. V, VI C, VII — The comparison with Shamir is overstated. The manuscript repeatedly says it does not perform a matched Ganalyzer reanalysis, but nevertheless claims strong amplitude-level tension and that a Shamir-scale signal “would have been detected.” Because the estimators, selections, masks, classifiers, and definitions of samples differ, this comparison cannot support the stated level of inference.

8. [MAJOR] Appendix D — The block-bootstrap WLS “\(z\simeq-7.6\)” clean-dipole disfavor is not a calibrated exclusion. It is performed on the full Catalog C field rather than the declared high-confidence primary sample, uses an incomplete covariance model, does not include classifier uncertainty or the \(p_{\rm eq}\) selection function, and is then elevated to a primary cosmological claim. This is not acceptable as a PRD-level exclusion statistic.

9. [MAJOR] Appendix A, Table V, Sec. IV C — The MASTER analysis lacks a clean, stable field definition. The paper alternates between \(A_p\), \(f_{\rm CW}-0.5\), different masks, different weights \(W_p=N_{\rm all}\) and \(W_p=N_{\rm spiral}\), different monopole subtractions, and different null ensembles. These choices materially affect the reported significances and must be unified before any inference can be trusted.

10. [MAJOR] Sec. IV D, Appendix A — The claimed 99.32% monopole–mask leakage reproduction is demonstrated for an un-deconvolved, pre-MASTER, monopole-preserving pseudo-\(C_\ell\), whereas the problematic residuals remain after monopole subtraction and/or MASTER treatment. The result is interesting as a diagnostic but does not explain the main residuals.

11. [MAJOR] Secs. IV A, VI B, Appendix E — The treatment of morphology, inclination, and edge-on contamination is inadequate. The manuscript assumes equivariance converts edge-on contamination into pure dilution, but the science estimator uses hard argmax labels after a confidence cut, where nonlinear tie-breaking and depth-dependent morphology selection can generate spatial bias. The edge-on and morphology analyses are not sufficient to close this channel.

12. [MAJOR] Secs. II, VI A — The GZ1-human-only cross-check is too small and too insensitive to validate the headline sub-percent claim. The manuscript itself estimates \(A_{50}\approx3.4\%\) and \(A_{95}\approx4.5\)–\(6.8\%\) for this test, so it cannot rule out the sub-percent inherited or classifier-induced structure relevant to the main catalog.

13. [MAJOR] Secs. I, VI C — The cosmological framing is overextended. The paper acknowledges that the \(\ell=1\) observable is parity-even and that no transfer function to primordial parity-violating sectors is derived, yet it discusses constraints on cosmic birefringence, Chern–Simons gravity, and primordial chirality. These claims should be removed or sharply demoted.

14. [MINOR] Throughout — The manuscript is excessively long, repetitive, and self-contradictory in presentation. Many caveats are repeated multiple times, often with slightly different numbers or conventions, making it difficult to identify the actual analysis chain.

15. [MINOR] Tables I–III, V, VIII, IX — The paper uses many nonstandard significance conventions and mixes moment-\(z\), rank \(p\), Gaussian-equivalent language, bootstrap \(z\), and recovery probabilities. Even where caveats are stated, the presentation invites misinterpretation.

16. [MINOR] Data Availability — The reproducibility record is incomplete for publication: the Zenodo DOI and immutable release hash are not yet provided, while many claims rely on internal artifact paths rather than archival, citable data products.

17. [MINOR] Figures 4, 7, 8, 9 — The figures would benefit from clearer annotation of which sample, mask, field convention, and null correspond to each plotted statistic. At present the visual material reinforces rather than resolves the estimator-confusion problem.

(3) The narrow statement that the selected \(p_{\rm eq}>0.6\) hard-label real-space estimator is consistent with zero is plausible, but the manuscript does not support the broader central claim of a robust sub-percent cosmological null dipole or a reliable Shamir-scale falsification.