# P5 — ChatGPT (Pro Extended) — FINAL ROUND
- paper: P5 (DESI chirality)
- version: v0.1.102
- model: ChatGPT Pro Extended (chatgpt.com)
- timestamp: 2026-07-07T03:28:26Z
- chat_url: https://chatgpt.com/c/6a4c70c2-14b8-83e8-aa9c-87759e6e7c45

## RAW VERBATIM RESPONSE

(1) VERDICT: REJECT.

(2) ISSUES:

[MAJOR] Section II / Appendix A, dependence on Paper IV: the chirality labels and monopole calibration are imported from a companion paper with placeholder arXiv identifiers, and the present manuscript cannot be independently refereed unless the full catalog, trained weights, validation splits, label-generation procedure, and immutable archive are available and citable at submission; the appendix summary is not a substitute for a refereed or fully inspectable source. 

final_P5

[MAJOR] Appendix A / label validity: the stated independent binary CW/CCW accuracy floor is only 69.91%, implying severe dilution of any true chirality-environment signal, but the quoted ∆fCW limits are not corrected for this dilution and no environment-stratified human-label validation is supplied; an observed 0.5 pp null is not a 0.5 pp bound on true chirality unless label errors are demonstrated to be environment-independent.

[MAJOR] Section V B / “primary” DESIVAST path: the primary analysis is explicitly designated post hoc, after many classifiers and stratifications were explored; the manuscript’s claim that this bounds the garden-of-forking-paths problem is inadequate, especially because the tightest quoted bound is selected from correlated void-definition choices without a pre-data plan.

[MAJOR] Sections IV, VI, VII, IX A / T-Web classifier: the canonical T-Web environment labels are not physically reliable as cosmic-web classes because the density field is built from a strongly radially selected DESI sample with a global mean density and no initial random-catalog selection correction; the later BGS-randoms-weighted rebuild reassigns roughly three quarters of matched spirals and collapses the void volume fraction, showing that the original T-Web labels mostly encode survey selection rather than environment.

[MAJOR] Section VI A / T-Web void bin: the headline T-Web void class contains only 428 chirality-relevant spirals, and only 6 overlap the DESIVAST z ≤ 0.24 void regime, with 0/6 inside DESIVAST holes; this makes the T-Web void result scientifically uninformative and unsuitable as a meaningful “secondary tidal-tensor cross-check.”

[MAJOR] Section VIII / DESIVAST void membership: the primary DESIVAST analysis uses fixed redshift-space point-in-sphere membership against published void holes and does not rerun the void finder under perturbed or reconstructed positions; the reported FoG Monte Carlo perturbs galaxy positions while holding the void catalog fixed, so it cannot quantify the dominant systematic of void-boundary and void-catalog reconstruction uncertainty.

[MAJOR] Sections VIII B and XII B / quoted ∼0.5 pp bound: the bound combines counting statistics with only a partial membership systematic and explicitly omits classifier error, environment-dependent classification bias, cross-match purity, void-catalog covariance, and survey-mask systematics; it should not be presented as an exclusion-level physical bound.

[MAJOR] Sections V, VI, VIII / independence assumptions: binomial, Jeffreys, χ², and two-proportion z-tests treat galaxies as independent Bernoulli trials, but the data are spatially clustered, share imaging/calibration systematics, include overlapping void definitions, and in some tables include duplicated TARGETIDs; block bootstrap, jackknife over sky regions, or mock-based covariance is required.

[MAJOR] Sections VI D, XI / target-program and imaging systematics: the bright/dark split shows a ∼2σ sign flip and the catalog monopole is bright-program dominated, but the analysis does not convincingly separate target-selection, imaging-leg, morphology, redshift, and environment effects; this is a direct threat to an environment-null claim because environment class and target program are demonstrably not independent.

[MAJOR] Sections IX B and X / external classifier cross-checks: the Tempel and ASTRA comparisons are described as supporting robustness, but their footprints, redshift ranges, class definitions, and sample sizes differ strongly from the main analysis, and ASTRA/T-Web per-galaxy class agreement is poor; these checks do not validate the main environment labels.

[MAJOR] Sections XII B and Appendix B / theory motivation: the paper admits that no published bounce or inflation model predicts the tested environment-dependent chirality signal, and the toy EFT operator is explicitly not derived, not gauge-invariant as formulated, and not converted into a quantitative prediction; this makes the PRD-level fundamental-physics motivation too weak for the strength of the presentation.

[MINOR] Abstract / Introduction: the manuscript repeatedly states that the result is “environment-independence,” but the evidence supports only “no detected dependence within stated, systematics-limited sensitivity”; the stronger wording should be removed throughout.

[MINOR] Abstract and Sections VI–VIII: the text is excessively long, defensive, and packed with caveats, which obscures the actual analysis; a PRD submission should move most audit-trail material to supplementary material and present a clean primary analysis.

[MINOR] Tables IX–XI / DESIVAST counts: the manuscript alternates between k=20 and exact membership counts and between hole-union, maximal-sphere, sphere-PIS, and GALZONE definitions; these should be reorganized so that each estimator has one unambiguous parent sample, membership rule, and systematic interpretation.

[MINOR] Figures 6 and 8 / visual presentation: the figure captions and embedded labels are difficult to read and in places visually cluttered; these figures are not publication-quality for PRD without redrawing and clearer separation of map panels and legends.

[MINOR] Appendix D–E / artifact availability: artifact IDs such as [A1]–[A30] are not a substitute for complete URLs, checksums, versioned archives, and exact commands; the manuscript should include a single reproducibility table with immutable DOI, commit hash, and command-line regeneration recipe.

(3) The central claim is supported only in the narrow sense that the submitted tables show no statistically significant DESIVAST void/non-void CW-fraction difference in the analyzed catalog, but it is not supported as the broader, systematics-limited claim of environment-independent spiral chirality at the quoted precision.
