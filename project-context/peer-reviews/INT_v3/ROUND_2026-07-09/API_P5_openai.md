# INT API Review — P5 v0.1.121-2026-07-11 — openai (gpt-5.5)
paper: P5  version: v0.1.121-2026-07-11  model: gpt-5.5
modality: native-PDF (Files API input_file)
UTC: 2026-07-11T15:03:01.343273Z  |  latency: 40.2s  |  attempt: 1
usage: {"input_tokens": 75246, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 1742, "output_tokens_details": {"reasoning_tokens": 516}, "total_tokens": 76988}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

1. [MAJOR] §II, Appendix A, §XIII / dependence on Paper IV labels: the entire analysis rests on a concurrently submitted, placeholder-cited chirality catalog (“arXiv:XXXX.XXXXX”), whose classifier, training labels, calibration, and systematic error model are not independently reviewed here; PRD cannot assess the main result until the catalog paper, catalog version, trained weights, and immutable DOI are available and citable.

2. [MAJOR] §V B / post-hoc primary designation and trials accounting: the manuscript repeatedly states that the DESIVAST path was chosen post-hoc, yet still presents “primary” bounds and model-building constraints; this is acceptable only as exploratory, but the text often reads as an exclusion/constraint, and the “few-dozen trial” accounting is qualitative rather than a formally defined analysis family.

3. [MAJOR] §VIII B, §VIII E / DESIVAST control sample and footprint: the “footprint-restricted” control is not an official DESIVAST/BGS selection mask or random-catalog completeness match, but a constructed union of hole angular discs and radial ranges; therefore statements such as “same-selection-function” and “clean same-footprint estimand” are too strong unless a DESI randoms/BGS completeness-matched control or explicit IPW/matched-control regression is performed.

4. [MAJOR] §VIII A–E / void membership definition: the main VoidFinder membership uses an author-constructed point-in-sphere union of holes, while the catalog-native membership exists only for V2 GALZONE; this mixes physically different estimands, and the quoted “Bonferroni-5” family should not be presented as five comparable void definitions without clearer separation between official catalog-native membership and approximate sphere-proxy membership.

5. [MAJOR] §VIII, Table XI / systematic error budget: the advertised ≈0.9 pp “honest envelope” is an ad hoc quadrature of correlated excursions, counting intervals, membership perturbations, footprint choices, confidence cuts, and geometry variants; no covariance model or nuisance-parameter framework justifies treating these as independent Gaussian-like terms, so this number should be demoted or replaced by a transparent sensitivity table without a single combined bound.

6. [MAJOR] §IV, §VI, §VII, §IX A / T-Web analysis: the manuscript itself demonstrates that the canonical T-Web labels are dominated by DESI radial selection and survey-shell geometry, with randoms-weighting reassigning ~73% of galaxies and collapsing the void volume by ~23×; the T-Web results should therefore be much more sharply demoted or moved to an appendix, and no physical interpretation should rely on them.

7. [MAJOR] §XII B, Appendix A / physical chirality de-attenuation: converting the classifier-label bound to a physical chirality bound using a single symmetric-error factor from a GZ1 overlap is not robust, especially given possible environment-, morphology-, redshift-, surface-brightness-, and inclination-dependent classifier errors; the ≈2.26 pp physical bound should be framed as an illustrative estimate, not a model-builder constraint.

8. [MAJOR] §VI B, §VIII B / lack of covariate-adjusted DESIVAST test: the manuscript acknowledges that the appropriate robustness test is a logistic/IPW or matched-control regression including redshift, magnitude, morphology, confidence, imaging leg, and sky, but defers it; for the claimed primary DESIVAST result, this is a necessary analysis rather than a future item.

9. [MAJOR] Abstract, §XII, §XV / overstatement of model implications: the data support at most a redshift-space null for classifier-labelled chirality in the adopted DESIVAST splits; claims about constraining bounce-chirality couplings, parity-violation amplitudes, or Shamir-scale effects should be substantially softened or removed from the headline.

10. [MAJOR] Appendix B / speculative EFT mapping: the toy non-covariant, gauge-dependent operator is explicitly not derived from the data or a consistent EFT; it is inappropriate for the main article and should be removed or placed in clearly non-refereed supplementary material.

11. [MINOR] Abstract and throughout / excessive length and repetition: the abstract and main text are far too long, contain many caveats repeated multiple times, and obscure the actual statistical result; the paper should be shortened drastically around one primary DESIVAST table, one systematic table, and appendices for diagnostics.

12. [MINOR] §III–IV / notation and unit clarity: the manuscript uses Mpc/h and h⁻¹ Mpc language inconsistently in places; all distances, void radii, grid cells, and smoothing scales should be reported with one unambiguous convention.

13. [MINOR] §V / permutation details: NMC = 1000 gives coarse p-value resolution for several quoted second/third decimals; either increase permutations for headline LEE values or round p-values consistently to the Monte Carlo precision.

14. [MINOR] Figures 6 and 8 / presentation quality: the HEALPix figures appear visually cluttered and in one case have overlapping labels/color bars; these need revision for publication-quality readability.

15. [MINOR] Appendix D–E / reproducibility claims: repository tags, DOI, and arXiv placeholders must be replaced by immutable public archival links before acceptance; statements like “DOI to be minted at acceptance” are not acceptable as final data availability.

(3) The central claim is supported only in the narrow sense that, conditional on the Paper IV labels and the adopted DESIVAST redshift-space membership definitions, there is no statistically significant void/non-void dependence of the classifier-labelled CW fraction, but the stronger physical and model-building claims are not yet supported.