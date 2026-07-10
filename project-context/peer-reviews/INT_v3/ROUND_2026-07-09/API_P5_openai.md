# INT API Review — P5 v0.1.117-2026-07-10 — openai (gpt-5.5)
paper: P5  version: v0.1.117-2026-07-10  model: gpt-5.5
modality: native-PDF (Files API input_file)
UTC: 2026-07-10T22:47:32.881864Z  |  latency: 36.0s  |  attempt: 1
usage: {"input_tokens": 74507, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 1555, "output_tokens_details": {"reasoning_tokens": 516}, "total_tokens": 76062}
PARSED VERDICT: REJECT

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: REJECT.

(2) ISSUES:

1. [MAJOR] Abstract/§II/App. A: the result depends critically on a concurrently submitted “Paper IV” with placeholder arXiv identifiers, unpublished classifier validation, and label provenance; this is not merely a citation-timing issue because the per-galaxy chirality labels are the fundamental observable, so the present manuscript is not independently refereeable to PRD standards.

2. [MAJOR] Abstract/§XII/App. A: the manuscript repeatedly moves between “classifier-labelled CW fraction” and “physical spiral chirality”; with a quoted 69.91% binary accuracy floor and no void/non-void environment-stratified confusion matrix, the claimed physical interpretation and de-attenuated ≈2.26 pp bound are not established.

3. [MAJOR] §V B/Abstract/Conclusions: the “primary” DESIVAST analysis is explicitly post-hoc, yet the manuscript phrases the outcome as a headline bound; the Bonferroni-5 treatment does not cure the larger garden-of-forking-paths problem because the analysis tree includes many correlated choices of footprint, membership, classifier confidence, void definition, and control sample.

4. [MAJOR] §VIII B/§VIII E: the primary DESIVAST footprint-restricted control is not a published DESIVAST/BGS selection mask but an author-defined angular–radial union of hole-sphere discs; therefore the void and non-void samples are not demonstrably matched in angular completeness, radial selection, fiber assignment, or imaging systematics.

5. [MAJOR] §VIII/§VIII C/§VIII D: the DESIVAST VoidFinder “membership” is an author-constructed point-in-sphere/hole-union proxy, while the manuscript alternates between k=20 approximate, exact k-unbounded, hole-union, maximal-sphere, sphere-PIS, and GALZONE definitions; these are not equivalent estimands, and the quoted single systematic envelope is not a rigorous marginalization over them.

6. [MAJOR] §IV/§IX A: the T-Web classification is shown by the authors’ own tests to be dominated by DESI radial selection and survey-shell artifacts, with randoms-weighting reassigning ∼73% of matched galaxies and collapsing the void volume fraction by ≈23×; consequently the T-Web analysis should not be presented as an environmental cross-check of comparable scientific weight.

7. [MAJOR] §VIII/§XIII: all environment assignments are in redshift space, and the manuscript acknowledges that anisotropic tidal-tensor eigenvalue deformation is not quantified; the RSD discussion is therefore insufficient for claims that model-builders can use the result as an environmental constraint, even with caveats.

8. [MAJOR] §XI/Table XI: the ≈0.9 pp “honest systematic envelope” is an ad hoc quadrature of heterogeneous excursions, many of which are correlated analysis-choice shifts rather than independent Gaussian systematic errors; it should not be quoted as an effective 2σ sensitivity without a statistical model.

9. [MAJOR] §VI D/§XI: target-program and imaging-leg residuals are not cleanly controlled; the manuscript finds a ∼2σ bright/dark sign flip and a highly significant T-Web-class–program association, but does not perform the needed end-to-end selection-function mock or a complete covariate-adjusted DESIVAST regression.

10. [MAJOR] §V/§VI/§VII: the permutation and look-elsewhere procedures are inconsistently scoped; some p-values are conditional on the observed global CW count, some scans are declared descriptive, some are Bonferroni-corrected, and the global trials factor across the full analysis tree is not controlled in a way that supports a quantitative bound.

11. [MINOR] Entire manuscript: the paper is far too long and repetitive for the stated null result, with extensive self-justifying text, duplicated caveats, and many secondary diagnostics that obscure the actual estimand.

12. [MINOR] Figures 6/8 and captions: the manuscript contains presentation-quality problems, including overlapping/unclear labels and inconsistent pixel-count descriptions, which should be corrected before any resubmission.

13. [MINOR] Appendix B: the speculative toy EFT mapping is non-covariant, not derived from the data, and inappropriate for the main scientific record of this observational null; it should be removed or relegated to clearly non-refereed supplementary material.

14. [MINOR] Data/code availability: repository tags, artifact IDs, and Zenodo DOI status are not sufficient substitutes for an archived, immutable, independently runnable data release at submission time.

(3) The central claim is supported only in the narrow sense that the author’s classifier-labelled DESIVAST void/non-void contrasts are statistically consistent with zero, but not as a robust PRD-level constraint on physical spiral chirality or parity-violating cosmology.