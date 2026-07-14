# INT API Review — P4 v1.0.241 — openai (gpt-5.5)
paper: P4  version: v1.0.241  model: gpt-5.5
provenance: commit=4420453d2ae3614bc08bd22eec9454df3b3546b5  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=d6eded1df29da5d2ccf6acb1e04277876289ae1547a1b8a3d2fda819ae7097f2
modality: native-PDF (Files API input_file)
UTC: 2026-07-14T10:20:40.143453Z  |  latency: 72.6s  |  attempt: 1
usage: {"input_tokens": 61279, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 2040, "output_tokens_details": {"reasoning_tokens": 516}, "total_tokens": 63319}
PARSED VERDICT: REJECT

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: REJECT.

(2) ISSUES:

1. [MAJOR] Title/Abstract/central claim: The paper advertises “a null chirality dipole in 8.5 million DESI galaxies,” but the stated primary cosmological result is obtained only after a classifier-confidence cut leaving 949,584 spirals, while the full Catalog C field shows significant low-ℓ residuals, including an unthresholded real-space excess at \(z\simeq 4.2\) and MASTER \(\ell=1\) residuals at \(z\simeq 7\). The title and abstract therefore overstate what is actually demonstrated.

2. [MAJOR] Secs. III–IV, estimator hierarchy: The manuscript contains too many non-equivalent estimators, masks, weights, nulls, field definitions, and significance conventions, with repeated warnings that the quoted significances are not comparable. This makes the statistical interpretation opaque and prevents a clean PRD-level inference. A single primary likelihood or estimator with a fully specified covariance and systematic model is needed.

3. [MAJOR] Sec. IV C / Sec. III B, primary sample selection: The \(p_{\rm eq}>0.6\) “pre-registration” claim is not adequate for a publication-level blind analysis. It appears to be a code-commit record rather than an externally fixed analysis plan, and the chosen cut is precisely where the reported systematic excess disappears. The confidence cut is also based on uncalibrated classifier scores known to correlate with depth/morphology, so the selection function itself is a central systematic, not a harmless robustness choice.

4. [MAJOR] Secs. IV C–D, treatment of significant harmonic residuals: The paper reports persistent MASTER \(\ell=1\) and low-\(\ell\) excesses at high nominal significance, then classifies them as systematics without a quantitative joint nuisance model capable of propagating those residuals into the primary real-space estimator. The later “cross-estimator stress test” explicitly shows that the residual can change the fitted real-space amplitude, so the dismissal is not yet justified.

5. [MAJOR] Sec. IV D / Appendix D, systematics attribution: The “eight-anchor” systematic battery is suggestive but not a substitute for a generative systematic likelihood. Many anchors use small MC ensembles, template regressions with incomplete templates, or qualitative criteria. The conclusion that the residual is survey-correlated rather than cosmological is plausible, but not demonstrated at the level required to support the strong null and comparison claims.

6. [MAJOR] Sec. II / Appendix B, classifier independence and accuracy: Since 66.5% of the training labels come from CE-ResNet pseudo-labels and the independent GZ1 chirality accuracy is only 69.91% with \(\kappa=0.40\), the classifier is not a precision chirality measurement. The human-only GZ1 null has only \(N\simeq 4.6\times10^4\) and percent-level sensitivity, so it cannot validate the sub-percent claims made with the learned catalog.

7. [MAJOR] Sec. VI B, injection-recovery calibration: The main injection-recovery tests inject signals into the observed hard-label field, not into galaxy images or a physical morphology model passed through the classifier, confidence selection, and not_spiral triage. The manuscript acknowledges this limitation, but still uses the resulting \(A_{50}\), \(A_{95}\), and \(g=0.398\) mappings in ways that invite physical interpretation. The physical sensitivity is therefore not established.

8. [MAJOR] Secs. V–VII, comparison with Shamir claims: The manuscript repeatedly states amplitude-level tension with Shamir’s reported signals but does not perform a matched-footprint, matched-selection, matched-estimator Ganalyzer comparison. Given the strong dependence of the result on classifier, cuts, masks, and estimator conventions, the comparison should be substantially weakened or removed.

9. [MAJOR] Sec. VI C, relation to parity violation: The discussion of parity-violating sectors is not sufficiently grounded. The paper correctly notes that the \(\ell=1\) chirality dipole is parity-even, but then still discusses constraints on parity-violating early-universe scenarios without deriving a transfer function. These statements are speculative and should not be presented as constraints.

10. [MAJOR] Secs. IV–VII, statistical language: The manuscript mixes moment-\(z\), empirical-rank \(p\), bootstrap \(z\), MASTER null significances, detection efficiencies, and “falsification thresholds” in a way that is confusing and sometimes misleading. In particular, “\(z\simeq -7.6\)” for an observed-label template, “+7.28σ” harmonic residuals, and “+0.41σ” primary null are repeatedly juxtaposed despite being non-commensurate.

11. [MAJOR] Appendix D, WLS template fit: The 9-template WLS design is explicitly rank deficient because the leg templates are collinear with the constant. Although pseudoinverse and leg-drop checks are reported, the individual nuisance coefficients and naive errors are meaningless, and the resulting template-disfavor statistic is not a calibrated exclusion. This should not be a load-bearing result.

12. [MAJOR] Data availability/reproducibility: The manuscript relies heavily on repository artifacts and “committed” JSON outputs, but the archival DOI, immutable release tag, and exact code/data hashes are not yet supplied. For a result whose credibility rests on many implementation details, this is not acceptable at submission.

13. [MINOR] Manuscript structure: The paper is excessively long, repetitive, and internally defensive. Many caveats appear multiple times, sometimes with slightly different numerical values or conventions. A PRD submission should be reorganized around one primary analysis, one systematic model, and a small number of essential appendices.

14. [MINOR] Figures and captions: Several captions are far too long and contain interpretive text that belongs in the main body. Some figures also mix conventions, e.g. \(f_{\rm CW}\) versus \(A_p\), in ways that increase the risk of misreading.

15. [MINOR] Terminology: Terms such as “pre-registration,” “falsification boundary,” “physical exclusion,” “diagnostic,” and “primary” are used in nonstandard or shifting ways. The manuscript should adopt conventional statistical terminology and reserve “exclusion” for a calibrated likelihood or confidence construction.

16. [MINOR] Catalog claims: The catalog may be useful, but the manuscript should clearly separate catalog release/ML methodology from cosmological inference. The present text interweaves these aims and thereby weakens both.

17. [MINOR] AI-assisted methodology statement: The disclosure is welcome, but the manuscript should not rely on AI-adversarial-review language as a substitute for concise methodological validation. The scientific claims must stand independently of the development process.

(3) The central claim is not supported in its present form because a null result for one confidence-selected estimator is not sufficient to justify the broader “null chirality dipole in 8.5 million galaxies” claim in the presence of unresolved significant low-\(\ell\) systematics and incomplete physical calibration.