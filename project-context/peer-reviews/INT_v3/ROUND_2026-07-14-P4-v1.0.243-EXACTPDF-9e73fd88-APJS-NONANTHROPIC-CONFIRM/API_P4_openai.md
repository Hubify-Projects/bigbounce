# INT API Review — P4 v1.0.243 — openai (gpt-5.5)
paper: P4  version: v1.0.243  model: gpt-5.5
provenance: commit=36badcbdf498123413031aa0a9504127d48f2054  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=9e73fd888699058d421043b0dd2de5d37d2aeb36fe37e8dd1c0bf5409e947d19
packet: key=53abe400ce971869eb19fe9b8531ff82b4ad6b8b8210e404ddb1ccf31e707187  profile=APJS-CATALOG-METHODS
modality: native-PDF (Files API input_file)
UTC: 2026-07-14T19:08:18.031408Z  |  latency: 82.2s  |  attempt: 1
usage: {"input_tokens": 43904, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 2746, "output_tokens_details": {"reasoning_tokens": 1362}, "total_tokens": 46650}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

1. [MAJOR] Data Availability / reproducibility: the manuscript repeatedly relies on live-branch artifact paths, future Zenodo deposition, missing commit hashes, and non-archived provenance files; an ApJS catalog/methods paper needs an immutable catalog release, code release, environment specification, checksums, and exact executable provenance before acceptance.

2. [MAJOR] Sections III–IV / primary-analysis declaration: the primary HC cut peq > 0.6 is said to be “declared” but not externally preregistered or blinded, while several other cuts and samples are explored; the paper must either treat the result as exploratory or provide a clear trials/accounting rationale for why this sample/cut is the sole inferential target.

3. [MAJOR] Section IV C / primary null definition: the “isotropic pixel-permutation” null is not adequately justified for a highly inhomogeneous, heteroskedastic, count-weighted survey footprint; the primary dipole should be tested against nulls that preserve the per-pixel Nspiral, footprint, depth/seeing/morphology selection, and binomial shot noise, or the current null’s limitations must be quantified.

4. [MAJOR] Section IV C / dipole fitting: the primary real-space estimator appears effectively unweighted in Ap despite large per-pixel count variations; a binomial or inverse-variance weighted likelihood/fit, or a demonstration that the unweighted estimator has correct coverage under the DESI footprint and selection, is required.

5. [MAJOR] Catalog integrity / Appendix B / Data Availability: 2.9% of rows, including 59,515 HC rows, have reconstructed flip-pass probabilities outside [0,1] because of a raw/equivariant pipeline-pass mismatch; for a public catalog this should be corrected by rerunning/rebuilding the affected columns, not merely flagged, or the unsafe columns should be removed from the release.

6. [MAJOR] Sections III–IV and Appendix A/D / internal inconsistency of masks and sample counts: the manuscript quotes multiple incompatible canonical-mask pixel counts and related quantities, e.g. 23,682 HC pixels, 24,087 canonical pixels, 24,297 Nall ≥ 1 pixels, fsky = 0.49005, and other variants, without a clean mapping; every estimator must have one unambiguous mask, field, weighting, sample size, and artifact.

7. [MAJOR] Sections IV C–D / harmonic results: the MASTER results are confusing and partially contradictory, especially +3.64σ, +7.28σ, and +7.93σ values associated with similar “canonical” or ℓ = 1 language but different fields/nulls/run sizes; these diagnostics should be separated into a reproducible table with identical definitions, or removed from the main scientific narrative.

8. [MAJOR] Section IV D / monopole-mask leakage claim: the statement that prior pre-MASTER dipole claims are “therefore attributed” to the leakage channel overreaches, because the test is on this classifier, mask, and estimator, not on matched Ganalyzer/Shamir selections; this should be weakened to a demonstration of a possible leakage mechanism in the present pipeline.

9. [MAJOR] Sections II, IV A, VI A–B / label validation and transfer: the catalog is largely trained on CE-ResNet pseudo-labels and has only 69.91% independent GZ1 chirality accuracy; the spatially varying confusion model is explicitly open, so any sensitivity, recovery, or physical-amplitude discussion must remain strictly “observed-label” and should not imply calibrated constraints on true galaxy spin/chirality.

10. [MAJOR] Section IV A / probability calibration and HC selection: the argument that softmax miscalibration cannot bias the dipole is incomplete because peq defines a spatially varying selection function correlated with depth, morphology, and image quality; provide reliability/selection diagnostics versus magnitude, size, redshift proxy, seeing, depth, leg, and sky position, or avoid confidence-based inferential claims.

11. [MAJOR] Section VI B / injection-recovery: the injections modify hard labels or paired original/mirror choices rather than injecting physical image-level morphology through the full classifier and selection pipeline; the finite deterministic-axis fractions must not be described as recovery probabilities, thresholds, or sensitivity floors, and should be clearly demoted or moved to an appendix.

12. [MAJOR] Appendix D / WLS “z ≈ −7.6” diagnostic: this statistic is computed on a different full-sample field with a block-bootstrap sampling distribution and is repeatedly juxtaposed with the primary HC result; it should be removed from the abstract/main conclusions or presented only as an exploratory diagnostic with no “template disfavor” language unless a joint covariance model is supplied.

13. [MINOR] Title/abstract: the title and abstract are dominated by caveats and internal DP labels; they should state the catalog release, classifier construction, primary observed-label null result, and limitations in concise journal style.

14. [MINOR] Catalog description: provide a complete column schema, units, class definitions, recommended filters, flag meanings, example queries, and minimal reproducible code for regenerating the primary dipole from the public Parquet files.

15. [MINOR] Figures: several maps and galleries have small labels, dense captions, and mixed Ap versus fCW conventions; every figure should state the field, mask, sample, units, and color scale directly and consistently.

16. [MINOR] Notation: peq, Ap, A, fCW deviation, “full amplitude,” “observed-label,” “physical,” “canonical,” “HC-broad,” and “strict” are used heavily and sometimes redundantly; consolidate definitions in one notation table.

17. [MINOR] Text quality: the manuscript contains numerous internal artifact references, repeated caveats, and nonstandard labels such as DP4-15/16/17/21 that read like project-management notes rather than a journal article; move these to a reproducibility appendix or supplement.

18. [MINOR] Formatting: remove stray encoding artifacts, fix overfull captions, standardize class names such as not_spiral, and ensure all references, software citations, and dataset citations are complete and stable.

(3) The central claim—that the high-confidence observed-label real-space chirality dipole is consistent with the authors’ declared null—is plausibly supported, but the broader catalog, calibration, harmonic, injection-recovery, and physical-interpretation claims are not yet supported to ApJS publication standard.