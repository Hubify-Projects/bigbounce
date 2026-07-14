# INT API Review — P4 v1.0.240 — openai (gpt-5.5)
paper: P4  version: v1.0.240  model: gpt-5.5
modality: native-PDF (Files API input_file)
UTC: 2026-07-14T07:16:51.842555Z  |  latency: 73.1s  |  attempt: 1
usage: {"input_tokens": 62358, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 2412, "output_tokens_details": {"reasoning_tokens": 999}, "total_tokens": 64770}
PARSED VERDICT: REJECT

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: REJECT

(2) ISSUES:

1. [MAJOR] Secs. III B, IV C, VI B, VII — The stated “primary” null is measured on the high-confidence subsample with \(p_{\rm eq}>0.6\) and \(N=949{,}584\), not on the advertised 3.2 million spirals or 8.5 million galaxies; the unthresholded Catalog C sample gives a reported \(z\simeq 4.0\)–4.4 dipole-like excess, which is then dismissed as a low-confidence systematic without a quantitative nuisance model sufficient to justify replacing the full-sample result by the selected-sample null.

2. [MAJOR] Secs. IV C–IV D, Appendix D — The manuscript reports large harmonic residuals, including \(+7.28\sigma\), \(+7.93\sigma\), and \(+3.64\sigma\) values depending on mask/null convention, but classifies them as “diagnostic systematics” while leaving \(\sim 47\%\) of the \(\ell=1\) residual explicitly unexplained; this is not an adequate basis for a sub-percent cosmological null claim.

3. [MAJOR] Secs. III A, III B, IV C, Tables I–V — The statistical framework is not coherent: multiple non-equivalent nulls, masks, weights, field definitions, and significance conventions are used, while the manuscript repeatedly warns that the reported \(\sigma\)’s are not comparable; nevertheless, these same quantities are combined rhetorically to support one scientific conclusion.

4. [MAJOR] Secs. II B, VI A, Appendix B — The chirality labels are not independently validated at the accuracy needed for the claimed sensitivity: 66.5% of the training labels are CE-ResNet pseudo-labels, the independent GZ1 chirality accuracy is only 69.91% with \(\kappa=0.40\), and the GZ1-human-only null has \(A_{95}\sim 4.5\)–6.8%, far too weak to test the sub-percent inherited-structure concern.

5. [MAJOR] Secs. IV A, Appendix B — The classifier probabilities are severely miscalibrated, with top-label ECE lower bounds of \(\gtrsim 0.25\)–0.36, yet the primary selection is a hard cut on these uncalibrated probabilities; monotone recalibration does not solve the issue because spatially varying confidence selection can itself generate or remove dipole power.

6. [MAJOR] Secs. IV C, VI B — The injection–recovery analysis injects signals into the observed hard-label field, not into images followed by classification, triage, confidence selection, and spatially varying confusion; therefore \(A_{50}\) and \(A_{95}\) are detection thresholds for the classifier-output map, not for physical galaxy chirality.

7. [MAJOR] Sec. IV D, Appendix D — The block-bootstrap WLS “exclusion” of a clean 1.7% dipole at \(z\simeq -7.6\) is not a calibrated frequentist exclusion, is performed on the full Catalog C field rather than the high-confidence primary sample, does not propagate the \(p_{\rm eq}>0.6\) selection function, and relies on a template/covariance model whose adequacy is not demonstrated.

8. [MAJOR] Secs. IV D, VII — The monopole–mask leakage calculation reproduces 99.32% only of a pre-MASTER pseudo-\(C_\ell\) quantity constructed with a different field convention, while the post-MASTER residual remains highly significant; using this to contextualize or disfavor previous claims is therefore not justified.

9. [MAJOR] Secs. V, VI C, VII — The comparison with Shamir’s results is over-interpreted: the manuscript alternates between caveats that no matched Ganalyzer likelihood is performed and strong statements that a Shamir-scale signal “would have been detected” or is in “3.7–8.8× tension”; without matched selection, estimator, redshift, and labeling pipelines, this is only a qualitative comparison.

10. [MAJOR] Secs. I, VI C — The physical interpretation is too weak for the advertised PRD framing: the paper correctly states that the \(\ell=1\) chirality dipole is parity-even and that no transfer function to primordial parity-violating sectors is derived, so the connection to parity-violating cosmology remains speculative rather than a quantitative constraint.

11. [MAJOR] Appendix B, Data Availability — The catalog contains a documented raw/equivariant pipeline-pass mismatch affecting 2.9% of rows and 59,515 high-confidence rows; the assertion that this is harmless for hard-argmax dipoles is plausible but not sufficient for a precision catalog release without a fully regenerated, internally consistent catalog.

12. [MAJOR] Secs. IV C, Appendix E — The confidence-cut sweep shows a sharp transition from \(z\simeq 4\) at cuts \(\le 0.5\) to null at \(p_{\rm eq}>0.6\), exactly where the selected sample changes; this is evidence that the result is selection-function dominated, and the manuscript does not provide a likelihood or nuisance model marginalizing over that selection.

13. [MINOR] Throughout — The manuscript is excessively long, repetitive, and difficult to audit; many caveats are repeated multiple times, while the actual statistical model underlying the claimed null is obscured.

14. [MINOR] Tables I–VI, Appendix A — The notation for \(A\), \(A_p\), \(f_{\rm CW}-0.5\), pseudo-\(C_\ell\), MASTER-decoupled \(C_\ell\), and field normalizations changes across tables; although some conversions are explained, the presentation is too error-prone for a precision null result.

15. [MINOR] Data Availability — The reproducibility record is not publication-ready: the Zenodo DOI and immutable commit hashes are deferred to future submission, while the paper relies heavily on live repository artifacts.

16. [MINOR] Acknowledgments — The extensive AI-assisted methodology statement is acceptable in principle, but it heightens rather than reduces the need for a concise, independently reproducible statistical specification in the paper itself.

(3) The central claim is not supported as a physical or cosmological null dipole measurement; the manuscript demonstrates only that one selected high-confidence classifier-output subsample is consistent with a dipole null under particular permutation tests.