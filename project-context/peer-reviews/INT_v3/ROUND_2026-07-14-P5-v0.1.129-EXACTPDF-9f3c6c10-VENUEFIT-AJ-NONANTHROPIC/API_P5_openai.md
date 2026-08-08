# INT API Review — P5 v0.1.129-2026-07-14 — openai (gpt-5.5)
paper: P5  version: v0.1.129-2026-07-14  model: gpt-5.5
provenance: commit=f4c26f81  pdf=pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf  sha256=9f3c6c1043331d67463198ff9d1061f0fd4a90eb1a7235035c8801110669cdc8
modality: native-PDF (Files API input_file)
UTC: 2026-07-14T17:34:40.208767Z  |  latency: 69.2s  |  attempt: 1
usage: {"input_tokens": 67099, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 3063, "output_tokens_details": {"reasoning_tokens": 1917}, "total_tokens": 70162}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

1. [MAJOR] Appendix C / Appendix D, reproducibility: the analysis rests on a “release candidate,” with no immutable public tag/DOI and with some artifact links stated to be pending; a real submission must provide a frozen, public, independently retrievable code/data archive for all numbers in the paper.

2. [MAJOR] Sections II, XIII, Appendix A, dependence on Paper IV: the per-galaxy chirality labels and classifier-monopole calibration come from a companion manuscript “in preparation”; unless Paper IV is accepted/co-reviewed and its catalog, weights, training data provenance, and validation are fully available, the present paper’s input labels cannot be adequately refereed.

3. [MAJOR] Section VIII B/E, primary DESIVAST “footprint-restricted” estimand: the footprint is an author-constructed union of hole-sphere angular discs and radial spans, not the published BGS/DESIVAST angular/radial selection mask or DESI randoms; the manuscript therefore overstates this as a same-selection-function control.

4. [MAJOR] Section VIII, VoidFinder membership definition: the headline VoidFinder void sample uses an author-defined any-hole point-in-sphere membership, not an official per-galaxy VoidFinder membership; the maximal-sphere and GALZONE variants shift the contrast by amounts comparable to the quoted statistical scale, so the primary result should either use a catalog-native membership/selection parent or be explicitly framed as definition-dependent.

5. [MAJOR] Sections V B and XV, post-hoc primary designation and multiplicity: declaring DESIVAST as primary after exploring many classifiers/stratifications is transparently acknowledged, but Bonferroni-5 over only the five DESIVAST definitions does not make the resulting interval or “bound” confirmatory; all exclusion/bound language should be removed or made strictly exploratory.

6. [MAJOR] Sections III, VI, VIII F, sample accounting: the manuscript alternates among 791,635 unique chirality-relevant matches, 812,793 row-level environment-labeled entries, 783,820 unique environment-matched spirals, 678,945 low-z spirals, and 145,789 GALZONE rows; the primary parent sample and all duplicate/coadd handling must be made unambiguous in one place and used consistently.

7. [MAJOR] Section VIII and XIII, RSD treatment: the fixed-void-geometry Monte Carlo and first-order void-outflow displacement do not constitute a full redshift-space-to-real-space reconstruction or a rerun of the void finder, so claims that RSD effects are “bounded” at the quoted precision should be weakened to sensitivity checks only.

8. [MAJOR] Sections IV, VI, VII, IX, T-Web analysis: the T-Web labels are shown to be highly selection-function dependent and unstable under randoms weighting/shell correction; this material should be greatly shortened and clearly demoted to a diagnostic, because it does not provide a reliable independent cosmic-web environmental classification.

9. [MAJOR] Sections V, VIII B, statistical uncertainty: most reported intervals are independent-binomial or conditional label-shuffle calculations, while classifier systematics and survey-selection residuals are spatially correlated; the cluster bootstrap over nearest DESIVAST regions is useful but too narrow to justify the broader uncertainty claims, especially for the headline contrast.

10. [MAJOR] Section VIII B, GALZONE adjusted analysis: the released GALZONE-parent covariate/overlap-weighted analysis appears to be the closest to a catalog-native selection-controlled result, but it is not the headline; the manuscript must justify this hierarchy or promote the catalog-native adjusted result to the primary result.

11. [MAJOR] Appendix A, classifier-label interpretation: the manuscript correctly avoids a physical-handedness claim, but the label-error/dilution discussion remains insufficient to exclude environment-dependent misclassification at the sub-percent level; the title, abstract, and conclusions should consistently say “classifier-labelled chirality” and avoid implying a physical chirality constraint.

12. [MINOR] Section III B, DESI matching: inclusion of SPECTYPE==QSO rows in a galaxy-chirality cross-match needs justification or removal, even if the effect is numerically small.

13. [MINOR] Section IV, units and notation: the text alternates between “Mpc/h” and “h⁻¹ Mpc,” and uses symbols such as ρ̄ for log-density quantities; standardize notation to avoid ambiguity.

14. [MINOR] Tables/figures/captions: many captions are several paragraphs long and contain methodological caveats better placed in the text; shorten captions and move detailed caveats to a methods or appendix section.

15. [MINOR] Overall presentation: the manuscript is far too long and internally repetitive for the narrow null result; a publishable version should focus on the DESIVAST analysis, with T-Web/Tempel/ASTRA material compressed to concise robustness checks.

16. [MINOR] References and acknowledgments: provide the standard DESI DR1 citation and collaboration acknowledgment language, and replace “in preparation” or pending 2026 references with stable citations where possible.

(3) The central claim is supported only in the narrow exploratory sense that the currently defined, classifier-labelled DESIVAST redshift-space void/non-void contrasts are consistent with zero, but it is not yet supported as a robust selection-function-matched or physical-handedness constraint.