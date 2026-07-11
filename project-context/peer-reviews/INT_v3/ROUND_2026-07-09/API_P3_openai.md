# INT API Review — P3 v3.1.153 — openai (gpt-5.5)
paper: P3  version: v3.1.153  model: gpt-5.5
modality: native-PDF (Files API input_file)
UTC: 2026-07-11T15:03:01.281093Z  |  latency: 61.1s  |  attempt: 1
usage: {"input_tokens": 64111, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 2416, "output_tokens_details": {"reasoning_tokens": 830}, "total_tokens": 66527}
PARSED VERDICT: REJECT

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: REJECT.

(2) ISSUES:

1. [MAJOR] Overall scope and PRD relevance: The primary result is an astronomical machine-learning catalog, while the cosmological material in §V is explicitly secondary and yields no detection or constraint; this is not presently a Physical Review D physics result.

2. [MAJOR] Title/abstract/headline claim of “268,519 validated anomalies”: The word “validated” is used for heterogeneous and partly non-sensitivity tests; NEOWISE passes only a mask-geometry QA “by construction,” DESI validation is limited to broad/extended features, Planck uses fixed-count patch selection, and LAMOST/eROSITA are failed or excised tiers. This does not justify a uniform validated catalog-grade headline.

3. [MAJOR] Reproducibility is not demonstrated at submission standard: The manuscript repeatedly relies on repository artifacts, scripts, JSON files, model weights, HuggingFace tables, and Zenodo DOI “to be released” later; several key raw score products/checkpoints are stated to be lost or on exited pods. A PRD referee cannot verify the numerical claims from the manuscript alone or from citable public artifacts.

4. [MAJOR] Count accounting is excessively convoluted and internally unstable: The manuscript uses multiple denominators and totals—36.76M, 36.93M, 37.27M, 37.29M, 377,482, 268,519, 319,443, 387,695—depending on retained-native, read/scored, cross-transfer-inclusive, excised, exploratory, and validated definitions. This makes the headline “37.3 million” and “268,519” claims fragile and not transparently auditable.

5. [MAJOR] Thresholds are arbitrary and survey-dependent: DESI uses S>5, SDSS headline uses a fixed-size continuity slice of 77,905 despite native S>5 giving only 12 objects, Planck and NEOWISE use predetermined top-1% or top-200 cuts, eROSITA uses a top-298 membership list because its score axis is irreproducible, and LAMOST uses a failed top-1% exploratory tier. Consequently the quoted anomaly rates are not comparable physical or statistical rates.

6. [MAJOR] DESI result is dominated by non-science spectra: §III A states that ∼98.7% of raw DESI anomaly clusters are sky/filler/non-primary science spectra, and the like-for-like science-target yield is only 2,468 clusters, ≈0.92× the Liang et al. benchmark. This undercuts the advertised process-scale multipliers and the implication of a large science-catalog expansion.

7. [MAJOR] Validation tests do not establish purity or astrophysical reality: Injection-recovery tests show sensitivity to selected artificial morphologies, not that catalog entries are physical anomalies; visual inspection of the top 200 DESI objects and SIMBAD/NED absence are insufficient purity validation for hundreds of thousands of sources.

8. [MAJOR] DESI robustness evidence is weakened by proxy models and incomplete held-out inference: The k-fold models are described as short-trained and failing the paper’s validation-loss retain gate, and the released 22.5M catalog has not been re-inferred with a held-out production ensemble. The manuscript correctly discloses this, but then overstates the robustness of the DESI tier.

9. [MAJOR] eROSITA treatment is scientifically unusable as presented: The production score axis is admitted to be irreproducible and non-monotone relative to committed raw scores, the injection-recovery is 1.2%, and the tier is excised from counts; nevertheless it is repeatedly discussed as a notable source list and follow-up target set. This should not appear as a catalog result without a clean rerun.

10. [MAJOR] Gaia provenance failure indicates serious pipeline-control problems: A synthetic-placeholder Gaia table entered earlier versions of the analysis and had to be excised. This is not merely a removed tier; it raises broader concerns about pipeline safeguards, provenance validation, and whether analogous silent fallbacks or stale artifacts affect other tiers.

11. [MAJOR] Planck/CMB anomaly tier is not physically validated: The Planck top-200 are fixed-count reconstruction outliers in standardized patches, selected partly in-sample, with Gaussian-bump injection recovery that does not correspond to a well-defined cosmological or foreground anomaly class. The ACT comparison is quarantined and geometry-driven, so the CMB component has no demonstrated physical interpretation.

12. [MAJOR] Cosmological fNL application is not a meaningful constraint: The tracer sample is photometric/QSO-candidate based with no redshift cut, no calibrated selection function, no convincing bias measurement, and α=0.19±0.65 is consistent with zero; the stated “central” σ(fNL)=8.14 is noise-biased by construction and the de-biased result gives no improvement. This should not be presented as a PRD-level cosmological forecast beyond a toy exercise.

13. [MAJOR] NANOGrav analysis is oversimplified and overinterpreted: The KDE free-spectrum refit factorizes frequency bins and does not use the full timing likelihood; the Bayes factor compares matter-bounce γ=3 only to an idealized circular SMBHB γ=4.33 while acknowledging environmental SMBHB models can give γ≈2.5–3. The “decisive” language is therefore misleading for model selection.

14. [MAJOR] Statistical treatment of novelty is inadequate: The manuscript emphasizes SIMBAD-unmatched fractions while also acknowledging that these are database-coverage measures; the “17.8% genuine novelty” estimate is only a top-1000 DESI point estimate against selected catalogs, without a survey-wide selection model or local-depth completeness treatment.

15. [MAJOR] Spatial statistics are not interpretable: The HEALPix χ² test is dominated by survey footprints, selection functions, and tiling geometry, yet large significance values are reported. Without per-survey angular masks and completeness weights, these tests should not be used as evidence for or against astrophysical clustering.

16. [MAJOR] Methodological controls are insufficient for an anomaly catalog of this scale: There is no independent architecture comparison for the spectroscopic tiers, no noise-weighted reconstruction baseline, limited calibration of score distributions, and no end-to-end contamination model separating sky subtraction, fiber assignment, calibration residuals, stellar contaminants, and true astrophysical outliers.

17. [MINOR] Manuscript presentation is overly defensive and internally repetitive: Many caveats are repeated in the abstract, introduction, table notes, and conclusions, making the paper difficult to read and obscuring the actual scientific result.

18. [MINOR] Figures mix obsolete and current products: Several figures show cross-transfer baselines, display-only scores, removed Gaia/ACT historical material, or non-catalog scores; this is confusing and should be separated from the released catalog analysis.

19. [MINOR] Tables and captions are too long and contain essential methodological qualifications that should be in the main text: Table II footnotes in particular function as a parallel manuscript, making the result hard to audit.

20. [MINOR] Terminology such as “catalog-grade,” “validated,” “PASS,” “science result,” “process-volume,” and “genuine novelty” needs stricter definitions and consistent use throughout.

(3) The central claim is not supported: the manuscript demonstrates at most an internally generated multi-survey reconstruction-outlier candidate list, not a uniformly validated astrophysical anomaly catalog or a PRD-level cosmological result.