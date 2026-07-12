# INT API Review — P5 v0.1.123-2026-07-12 — openai (gpt-5.5)
paper: P5  version: v0.1.123-2026-07-12  model: gpt-5.5
modality: native-PDF (Files API input_file)
UTC: 2026-07-12T08:24:50.632643Z  |  latency: 48.7s  |  attempt: 1
usage: {"input_tokens": 75362, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 1961, "output_tokens_details": {"reasoning_tokens": 516}, "total_tokens": 77323}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

VERDICT: MAJOR REVISIONS

ISSUES:

1. [MAJOR] Abstract/Headline and §XV: The manuscript’s main result is not stated with a stable, single statistical interpretation; it alternates among a preferred-row bound, a Bonferroni-5 null, a ≈0.9 pp systematic envelope, and a 1.1 pp simultaneous Bonferroni interval. The authors must decide which quantity is the primary result and use one consistent bound/sign convention throughout.

2. [MAJOR] §V B / “primary” designation: The primary DESIVAST path is explicitly post-hoc, yet the manuscript repeatedly uses language such as “strictly quotable,” “primary,” and “headline” in a way that can be read as confirmatory. This must be reframed as an exploratory analysis unless a genuine timestamped analysis plan exists.

3. [MAJOR] §VIII B / DESIVAST footprint-restricted estimand: The “footprint” control is an author-constructed angular–radial hole-union proxy, not the DESIVAST/BGS selection function or random-catalog mask. The claimed same-selection-function control is therefore not established; either construct a proper DESI/DESIVAST randoms-based control or substantially weaken the claim.

4. [MAJOR] §VIII / void-membership definition: The VoidFinder “any-hole” point-in-sphere membership is a permissive author approximation, while the catalog-native memberships are available only for the V2 watershed catalogs. The paper treats these as a single Bonferroni family, but their estimands are not equivalent. The authors need a cleaner definition of the primary void membership and a transparent explanation of what physical population each row probes.

5. [MAJOR] §VIII / RSD treatment: The first-order Zel’dovich/Hamaus-profile “RSD reconstruction” is not a re-derived void catalog and is applied only to the unrestricted secondary contrast, not the stated primary footprint-restricted estimand. It cannot justify the strong language used about bounding DESIVAST RSD systematics; the claim must be weakened or the primary estimand must be reconstructed consistently.

6. [MAJOR] Appendix A / classifier-label interpretation: The classifier accuracy floor, pseudo-label provenance, and possible environment-dependent label errors remain central limitations. The de-attenuation from classifier-labelled chirality to physical chirality assumes symmetric errors and uses a small/underpowered void-stratified GZ1 overlap. The physical-chirality bound should be presented as highly model- and classifier-dependent, not as a robust constraint for model builders.

7. [MAJOR] §II, §XIII, Appendix A / dependence on Paper IV: The present paper depends on a concurrently submitted catalog paper with placeholder arXiv identifiers. For a PRD submission, the companion catalog, trained weights, immutable data snapshot, and label-validation documentation must be available and citable at review time, or the present paper is not independently refereeable.

8. [MAJOR] Appendix D/E / reproducibility: The manuscript relies heavily on GitHub artifact IDs, pending Zenodo DOI, and internal JSON outputs. A real submission must provide stable archived data/code references, clear scripts sufficient to reproduce the tables from public inputs, and remove “pending” DOI language before acceptance.

9. [MAJOR] §IV, §VI, §VII, §IX / T-Web analysis: The T-Web classifier is acknowledged to be severely affected by the DESI radial/angular selection function, with randoms-weighting reassigning ∼73% of matched galaxies and changing the void volume fraction by ≈23×. The T-Web results should be demoted further or moved to an appendix; as written they occupy excessive narrative space and may confuse readers about what result is actually load-bearing.

10. [MAJOR] §V / statistics and multiplicity: The multiplicity treatment is fragmented. Bonferroni-5, Bonferroni-9, empirical max-statistics, descriptive tests, and post-hoc scans are mixed throughout. The paper needs one compact statistical-analysis section defining all tested families, their nulls, and which intervals/p-values are inferential versus descriptive.

11. [MAJOR] §VIII B, Table XI, §XII B: The systematic-error budget is not rigorously justified as a quadrature combination of independent terms. Several terms are correlated membership/geometry variants rather than independent Gaussian-like errors. The ≈0.9 pp “envelope” should be called a sensitivity summary unless independence and calibration are demonstrated.

12. [MAJOR] Overall presentation: The manuscript is far too long, repetitive, and internally defensive for a PRD article. Much of the abstract and introduction reads like a response to anticipated referee objections rather than a scientific paper. The text should be reduced drastically, with secondary diagnostics and artifact bookkeeping moved to appendices or supplementary material.

13. [MINOR] Title and abstract: “DESIVAST Three-Algorithm Void Null Test on 57,081 DESI DR1 Spirals” is clearer than the current overloaded title, but the abstract should be shortened by at least a factor of 5 and should avoid terms such as “strictly quotable,” “honest,” and “model-builders should use.”

14. [MINOR] §IV A: The unit convention for comoving distances is explained at excessive length in a footnote. Retain only the convention and a sanity check.

15. [MINOR] §V / notation: The notation σfrom half, σpred, σvs monopole, z∆ is useful but visually cumbersome. Standardize notation and avoid reporting several σ-like quantities in the same table unless all are used in inference.

16. [MINOR] Figures 6 and 8: The Mollweide figures are visually hard to interpret and one page image appears overcrowded/overprinted. Improve readability, color bars, masks, and captions.

17. [MINOR] §IX B / Tempel comparison: The Tempel FoF richness mapping to T-Web classes is approximate and should not be described as cross-validation in a strong sense; call it a consistency check.

18. [MINOR] Appendix B: The speculative EFT mapping is not needed for the observational result and is not theoretically mature. It should be removed or placed in clearly non-refereed supplementary discussion.

19. [MINOR] References: Several citations are placeholders, companion manuscripts, preprints, or “in preparation.” These should be minimized and replaced with stable references where possible.

20. [MINOR] Acknowledgments / AI-assisted methodology: The AI disclosure is acceptable in principle, but it is overly promotional and should be shortened to a factual statement of tool use and author responsibility.

The central claim that the classifier-labelled DESIVAST void/non-void CW fraction shows no statistically significant dependence in DESI DR1 is broadly supported by the reported counts, but the stronger physical-chirality, systematic-bound, and confirmatory-significance interpretations are not yet adequately supported.