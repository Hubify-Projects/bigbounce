# INT API Review — P3 v3.1.155 — openai (gpt-5.5)
paper: P3  version: v3.1.155  model: gpt-5.5
modality: native-PDF (Files API input_file)
UTC: 2026-07-11T16:50:28.788269Z  |  latency: 40.8s  |  attempt: 1
usage: {"input_tokens": 64111, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 62208}, "output_tokens": 1878, "output_tokens_details": {"reasoning_tokens": 516}, "total_tokens": 65989}
PARSED VERDICT: REJECT

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: REJECT

(2) ISSUES:

1. [MAJOR] Abstract / §III “validated catalog-grade subset of 268,519”: The word “validated” is not justified uniformly; DESI is validated only for broad/extended injected residuals, SDSS only for one continuum-dip morphology, Planck for artificial Gaussian bumps, and NEOWISE only by a mask-geometry QA test that is explicitly not a detector-sensitivity test.

2. [MAJOR] Abstract / §III A headline count: The headline 268,519 count is largely a process-volume artifact rather than an astrophysical catalog result; the manuscript itself states that only 2,468 DESI clusters are on validated science targets and that ≈98.7% of raw DESI clusters are sky/filler/non-primary spectra, so the title and abstract substantially overstate the scientific yield.

3. [MAJOR] §III A DESI validation: The DESI catalog is scored in-sample over a data set containing the training spectra, while the full production re-inference needed to demonstrate per-object held-out robustness is unavailable; the k-fold checks are acknowledged to use short-trained proxy models that fail the paper’s own validation-loss gate, so they cannot support catalog-grade validation of the released 22.5M scan.

4. [MAJOR] §VI D(i) DESI injection-recovery: The injection-recovery test does not validate the released anomaly selection function; it uses synthetic broad/extended plants on re-pulled spectra, a “cleanest 5%” substrate and a thresholding protocol that may not represent the real anomaly population, while narrow-line recovery fails until ≥15σ.

5. [MAJOR] §III C SDSS count: The SDSS headline 77,905 is an arbitrary fixed-size continuity slice, not a native anomaly threshold; the native top-1% is 19,253 and strict S>5 gives only 12, so using 77,905 in the validated headline catalog is not scientifically motivated.

6. [MAJOR] §III D / §VI A LAMOST: The LAMOST tier is acknowledged to fail injection-recovery and to be dominated by a 98% blue-excess training-bias artifact, yet it remains in the inclusive 377,482 count; this makes the inclusive catalog scientifically heterogeneous and unsuitable as a coherent anomaly catalog.

7. [MAJOR] §III E eROSITA: The eROSITA score axis is declared irreproducible, the injection-recovery rate is 1.2%, and the tier is excluded from counts, but it is still discussed as a “membership addendum” with astrophysical highlights; this is not a reliable scientific product without a reproducible scoring pipeline and validated sensitivity.

8. [MAJOR] §II B preprocessing: For tabular surveys, scalers are fit on the full sample, including validation and tails; the manuscript admits this can affect validation MSE and extreme-tail ranking, and only eROSITA receives a partial robustness check, leaving NEOWISE unquantified.

9. [MAJOR] §II D / Data availability: Several key artifacts are stated to reside on exited pods or are not in the public release, while the paper repeatedly relies on future public release “with arXiv posting” or “at submission”; a submission cannot ask referees to accept reproducibility claims for unavailable raw scores, checkpoints, tensors, and feature tables.

10. [MAJOR] §IV A novelty fraction: The claimed 17.8% “genuine novelty” is based only on the DESI top-1,000 and is explicitly not survey-wide; it is inappropriate to use this as a general catalog discovery-rate figure, especially when SIMBAD-unmatched rates are shown to overstate novelty dramatically.

11. [MAJOR] §IV B spatial analysis: The χ² spatial non-uniformity test is dominated by survey footprints and selection functions that are not modeled; therefore the quoted significance has no interpretable astrophysical meaning and should not appear as a catalog validation statistic.

12. [MAJOR] §V fNL application: The multi-tracer forecast is not a PRD-level cosmological result: the measured bias enhancement is α=0.19±0.65, consistent with zero; the de-biased result gives no improvement; the QSO-candidate sample lacks spectroscopic redshifts; and the forecast assumes systematics and selection functions that are not demonstrated.

13. [MAJOR] §V A NANOGrav application: The NANOGrav analysis is disconnected from the anomaly catalog and uses a simplified factorized KDE free-spectrum likelihood rather than a full timing likelihood; the Bayes-factor comparison against a fixed circular-SMBHB spectral index is not a meaningful model comparison against realistic SMBHB populations and should not be presented as a substantive cosmological result.

14. [MAJOR] Scope for Physical Review D: The central deliverable is an astronomical ML anomaly catalog, not a theoretical or phenomenological particle/cosmology result; the cosmological sections explicitly make no detection and no robust constraint, so the manuscript is poorly matched to PRD.

15. [MINOR] Throughout / score notation: The manuscript uses multiple incompatible score axes—canonical S, raw MSE, production score-knee axes, IF raw scores, display scores—and repeatedly notes that values are not cross-survey comparable; this makes tables and figures difficult to interpret and invites misquotation.

16. [MINOR] Tables I–II / count bookkeeping: The many totals—36.76M, 36.93M, 37.29M, 268,519, 377,482, 387,695, 319,443—are heavily footnoted and internally confusing; the manuscript needs a much simpler accounting table and should remove quarantined/excised tiers from headline narrative.

17. [MINOR] Figures 2–4 and 8: Several figures are historical cross-transfer baselines or use display/non-catalog scores, but are visually prominent; these should be moved to appendices or regenerated using the final native catalog products.

18. [MINOR] §Acknowledgments AI-assisted methodology: The statement that results were verified by AI agents is not a substitute for independent reproducibility; the paper should emphasize conventional provenance, tests, and public artifacts rather than agentic workflow claims.

(3) The central claim is not supported: the manuscript demonstrates a large heterogeneous reconstruction-outlier processing exercise, but not a uniformly validated, reproducible, catalog-grade anomaly sample or a meaningful PRD-level cosmological result.