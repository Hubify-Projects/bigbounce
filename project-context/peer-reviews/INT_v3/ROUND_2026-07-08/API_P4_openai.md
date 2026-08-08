# INT API Review — P4 v1.0.223 — openai (gpt-5.5)
paper: P4  version: v1.0.223  model: gpt-5.5
modality: native-PDF (Files API input_file)
UTC: 2026-07-08T16:57:00.376507Z  |  latency: 82.0s  |  attempt: 1
usage: {"input_tokens": 55043, "input_tokens_details": {"cached_tokens": 0}, "output_tokens": 2676, "output_tokens_details": {"reasoning_tokens": 1034}, "total_tokens": 57719}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

1. [MAJOR] Abstract / Secs. III–IV: the paper’s central statistical hierarchy is not convincing because the real-space dipole, WLS template fit, MASTER pseudo-\(C_\ell\), hemisphere scan, injection tests, and monopole-leakage simulations use different samples, masks, weights, fields, and nulls, yet are combined rhetorically into one “null” conclusion without a unified likelihood or covariance model.

2. [MAJOR] Sec. IV C primary real-space dipole: the pixel-permutation null is not a sufficient cosmological null for a patchy, depth-dependent survey with heteroscedastic pixel noise and spatially varying classifier reliability; it destroys spatial correlations and does not propagate survey systematics or classifier misclassification in a physically justified way.

3. [MAJOR] Secs. II, IV A, VI A: the classifier validation is inadequate for a sub-percent cosmological dipole claim. The independent GZ1 chirality agreement is only \(69.91\%\), the three-class accuracy is \(58.7\%\), and the GZ1-human-only check has \(N\simeq4.6\times10^4\), with an admitted sensitivity floor of several percent, so it cannot validate the claimed sub-percent null.

4. [MAJOR] Secs. II, VI A: the dependence on CE-ResNet pseudo-labels is not resolved. Since \(66.5\%\) of training labels come from CE-ResNet, the resulting catalog is not independent of previous machine labels, and label-shuffle/permutation nulls of the model’s own outputs cannot test inherited survey-correlated biases. The GZ1-only test is useful but far too small to close this loophole at the stated amplitude.

5. [MAJOR] Sec. IV C confidence cut: the \(p_{\rm eq}>0.6\) primary selection is not demonstrated to be a genuinely blinded or externally optimized cut. The unthresholded and low-confidence samples show \(z\simeq4\) excesses, and the manuscript then declares the \(p_{\rm eq}>0.6\) sample primary. A commit hash is not a substitute for a pre-analysis plan, and the selection function induced by this cut is not propagated into the cosmological inference.

6. [MAJOR] Secs. IV C–D / Appendix D: highly significant harmonic residuals, including \(+7.28\sigma\), \(+7.93\sigma\), and \(+3.64\sigma\), are dismissed as systematics without a complete quantitative model. The manuscript admits that the forward model explains only about \(53\%\) of the \(\ell=1\) residual amplitude, leaving \(\sim47\%\) unexplained; this cannot be used simultaneously as evidence for systematics and as support for a precise cosmological null.

7. [MAJOR] Sec. IV D: the statement that the unexplained harmonic residual “cannot be a coherent cosmological dipole” because it lies below the real-space \(A_{50}\) recovery floor is logically invalid. Being below a 50%-recovery threshold means the estimator has poor power there; it does not exclude or classify the residual as non-cosmological.

8. [MAJOR] Secs. IV D, VI B, VII: the WLS “\(z\simeq-18\)” disfavoring of a clean 1.7% dipole is overstated. The block bootstrap does not appear to propagate classifier-label uncertainty, spatially varying selection, morphology-dependent misclassification, or model mismatch, and the manuscript itself says this is not a calibrated detection significance. It should not be featured in the abstract as a quasi-exclusion statistic.

9. [MAJOR] Secs. IV–VII: the comparison with Shamir is not rigorous. The manuscript repeatedly claims “tension” at factors of \(7\)–\(18\), but no matched-footprint, matched-selection, matched-estimator reanalysis is performed. The amplitude-unit conversions between \(f_{\rm CW}\) deviations and \(A_p\) are also used inconsistently enough that the comparison is not publication-ready.

10. [MAJOR] Title / Secs. III C–D: the phrase “Equivariant Deep Learning” is misleading. The ViT architecture is not intrinsically equivariant; flip equivariance is imposed by test-time averaging. The title and abstract should distinguish architectural equivariance from post-processing equivariant symmetrization.

11. [MAJOR] Sec. IV A / Appendix B: the manuscript states that overconfident probabilities “cannot bias the dipole amplitude or direction” because only hard labels are used. This is too strong: spatially varying confidence, purity, and class-dependent failure modes can bias hard-label maps even if probabilities are not used directly.

12. [MAJOR] Appendix E: the edge-on contamination argument is incomplete. The claim that equivariant averaging makes edge-on contamination a pure dilution relies on symmetry of the soft probabilities, but the analysis uses hard argmax labels and admits borderline argmax instability; the later empirical tests help but do not fully propagate this uncertainty into the dipole covariance.

13. [MAJOR] Secs. III–IV / Appendix A: the definitions of field, mask, weighting, and monopole subtraction change across estimators. Some rows use \(A_p\), others \(A_p/2\), some use \(N_{\rm all}\) weights, others binary weights, and some subtract different monopoles. This prevents straightforward physical comparison and makes the reported \(\sigma\) values difficult to audit.

14. [MAJOR] Sec. VI B: the injection-recovery calibration is not sufficient as a cosmological sensitivity claim because injections are applied to the existing label/count field under simplified binomial assumptions and do not inject through the image-level classifier, morphology distribution, depth-dependent selection, or inherited label-bias pipeline.

15. [MINOR] Abstract / Sec. I: the manuscript is far too long and defensive, with many caveats, artifact paths, and internal-review language embedded in the main text. It should be rewritten as a conventional paper with a compact main analysis and reproducibility material moved to a stable supplement.

16. [MINOR] Data Availability: live GitHub paths, branch-dependent artifacts, and non-archived repository states are not acceptable as final reproducibility handles. A frozen DOI-bearing archive must exist before publication.

17. [MINOR] Tables I–V: the repeated warnings that \(\sigma\) values are “not comparable” are necessary because the analysis is fragmented, but they also make the presentation confusing. A single primary estimator table with one null, one sample, and one covariance model would be clearer.

18. [MINOR] Figures 4, 7, 8, 9: several figures mix visual diagnostics with significance annotations from different nulls. Captions should avoid placing incommensurable \(\sigma\) values in visually adjacent contexts.

19. [MINOR] Sec. VI C: the discussion of parity-violating sectors is accurate in noting that the \(\ell=1\) chirality dipole is not a direct parity-violation observable, but the connection to PRD-relevant fundamental physics remains weak without a transfer model.

20. [MINOR] Acknowledgments / AI-assisted methodology: the disclosure is welcome, but the manuscript should not rely on AI-generated “adversarial review” language as evidence of robustness; only reproducible statistical tests should be cited.

(3) The narrow claim that the selected high-confidence real-space estimator gives a null result is plausibly supported, but the broader claim of a robust sub-percent cosmological chirality-dipole null and strong amplitude-level tension with previous work is not yet supported.