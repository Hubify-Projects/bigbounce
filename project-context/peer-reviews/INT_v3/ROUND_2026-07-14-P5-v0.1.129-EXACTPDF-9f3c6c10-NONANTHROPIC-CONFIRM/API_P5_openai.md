# INT API Review — P5 v0.1.129-2026-07-14 — openai (gpt-5.5)
paper: P5  version: v0.1.129-2026-07-14  model: gpt-5.5
provenance: commit=worktree  pdf=pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf  sha256=9f3c6c1043331d67463198ff9d1061f0fd4a90eb1a7235035c8801110669cdc8
modality: native-PDF (Files API input_file)
UTC: 2026-07-14T17:24:07.317622Z  |  latency: 48.4s  |  attempt: 1
usage: {"input_tokens": 67095, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 2236, "output_tokens_details": {"reasoning_tokens": 893}, "total_tokens": 69331}
PARSED VERDICT: REJECT

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: REJECT.

(2) ISSUES:

1. [MAJOR] Section XIII and Appendix C / dependence on Paper IV and unreleased artifacts: the manuscript’s input labels, classifier validation, monopole calibration, trained weights provenance, and even some claimed reproducibility artifacts depend on a “companion manuscript in preparation” and a “public tag pending”; this is not an acceptable evidentiary basis for a PRD submission unless the label catalog, weights, exact code tag, immutable archive/DOI, and Paper IV are independently reviewable at submission.

2. [MAJOR] Overall physics scope / PRD suitability: the paper repeatedly states that the result is not a physical-handedness constraint, not a real-space constraint, not a cosmological-model discriminator, and not evidence for environment independence; as written the result is primarily a post-hoc catalog-level null test of machine-classifier labels, with insufficient new physics content for PRD.

3. [MAJOR] Section V B / post-hoc primary definition and look-elsewhere accounting: the DESIVAST path is chosen after examining many environment classifiers, cuts, stratifications, and diagnostics, yet the formal family-wise claim is only Bonferroni-5 over DESIVAST definitions; this does not account for the data-dependent selection of DESIVAST as the “primary” path among the much larger analysis tree.

4. [MAJOR] Sections VIII B–VIII E / control-sample definition: the “footprint-restricted” non-void control is constructed from a union of void-hole angular discs and radial spans, not from the DESIVAST/BGS angular mask, DESI random catalogs, fiber-assignment completeness, or a matched selection function; therefore the quoted primary contrast is not demonstrably a clean same-selection void/non-void estimator.

5. [MAJOR] Sections VIII B, VIII D, and Table XIV / heterogeneous estimands: the five “Bonferroni-5” DESIVAST rows mix different parents, membership definitions, and sample sizes, including sphere point-in-sphere approximations on the full low-z matched set and catalog-native GALZONE joins on a much smaller valid parent; treating them as one primary estimator family obscures that they are not the same statistical estimand.

6. [MAJOR] Appendix A and Section XIII / classifier-label systematics: the claimed sub-percent environmental null is limited by possible environment-dependent classifier errors; the void-stratified human-label validation has a void-arm uncertainty of order ±3.7 pp, far larger than the quoted ∼0.2–0.6 pp contrasts, so the manuscript cannot support any statement beyond a highly conditional classifier-label non-detection.

7. [MAJOR] Sections VIII and XIII / redshift-space treatment: the DESIVAST “RSD robustness” tests displace galaxies and/or voids under simplified fixed-geometry or first-order models but do not rerun the void finder on reconstructed positions, while the T-Web anisotropic eigenvalue RSD channel is explicitly unquantified; the abstract and conclusions must not imply a robust environmental null beyond fixed redshift-space catalog assignments.

8. [MAJOR] Section IX A / T-Web implementation and selection function: the canonical T-Web field is built from unweighted redshift-space counts in a strongly radially varying DESI selection function, and the later randoms-weighted rebuild changes class assignments catastrophically; although labelled “secondary,” large parts of the manuscript still present T-Web results prominently and should be removed, compressed to an appendix, or fully reanalyzed with survey weights from the start.

9. [MAJOR] Sections V, VIII B, and Table XI / uncertainty presentation: the ≈0.96 pp “quadrature” combines counting intervals, correlated systematic excursions, geometry choices, membership perturbations, and definition changes without a probability model; despite caveats, its repeated use risks being read as an error budget or bound and should be removed or replaced by a formal nuisance-parameter/sensitivity analysis.

10. [MAJOR] Section VIII B / spatial covariance: the region-cluster bootstrap based on nearest DESIVAST maximal-void neighborhoods is not a convincing treatment of survey-scale covariance, angular systematics, or selection-function correlations; a jackknife over sky regions, DESI tiles, imaging legs, or random-catalog-defined regions would be more appropriate.

11. [MAJOR] Sections VI–XI / overextended diagnostics: the manuscript contains many marginal, post-hoc, and sometimes internally demoted analyses—T-Web, Tempel, ASTRA, HEALPix scans, density scans, target-program splits, RSD Monte Carlos, reconstruction estimates—that obscure the main result and create a severe trials-factor/narrative-selection problem; the paper should be reduced to one clearly specified DESIVAST analysis plus minimal robustness checks.

12. [MINOR] Abstract and Conclusions / wording: phrases such as “environment-independence headline,” “properly powered,” and “strongest exact catalog-native selection proxy” should be softened, because the analysis supports only a conditional non-detection for one classifier-label catalog under specified redshift-space assignments.

13. [MINOR] Tables X, XIII, and XIV / sign conventions and membership definitions: the sign of ∆fCW, exact versus k=20 membership, any-hole versus maximal-sphere membership, and footprint-restricted versus unrestricted controls are difficult to track; the paper needs one master table with a single sign convention, exact integer counts, parent definition, and membership rule for every quoted primary and sensitivity contrast.

14. [MINOR] Section III / cross-match validation: the shared Legacy imaging coordinate provenance makes the angular match almost deterministic, but the manuscript should still quantify false-match and duplicate-resolution rates using local source densities or randomized positions.

15. [MINOR] Appendix C / reproducibility statement: statements such as “public tag pending,” “links will resolve,” and “DOI planned” are not acceptable in a submitted version; all referenced artifacts must exist and be immutable before review.

16. [MINOR] Presentation / length and readability: the manuscript is far too long and internally repetitive for the narrow result; many caveats are stated multiple times, while the actual primary estimator is buried among secondary diagnostics.

(3) The central claim is supported only in the narrow conditional sense that the current public classifier labels show no statistically significant DESIVAST redshift-space void/non-void CW-fraction contrast, but the manuscript does not support a broader physical or real-space chirality-environment conclusion.