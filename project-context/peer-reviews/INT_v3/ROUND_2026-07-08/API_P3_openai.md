# INT API Review — P3 v3.1.144 — openai (gpt-5.5)
paper: P3  version: v3.1.144  model: gpt-5.5
modality: native-PDF (Files API input_file)
UTC: 2026-07-08T16:55:38.729976Z  |  latency: 50.5s  |  attempt: 1
usage: {"input_tokens": 59595, "input_tokens_details": {"cached_tokens": 0}, "output_tokens": 2375, "output_tokens_details": {"reasoning_tokens": 929}, "total_tokens": 61970}
PARSED VERDICT: REJECT

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: REJECT

(2) ISSUES:

1. [MAJOR] Title/Abstract/§III “validated catalog-grade subset of 268,519”: the manuscript does not establish that these are catalog-grade astrophysical anomaly candidates. The DESI tier is dominated by non-primary science-target spectra, SDSS is an arbitrary continuity slice, Planck is an in-sample fixed-count patch ranking, and NEOWISE is validated only by a tautological mask-geometry test rather than detector sensitivity.

2. [MAJOR] §II B/Table I thresholding: the anomaly-selection criteria are ad hoc and heterogeneous across surveys. DESI uses S > 5, SDSS uses a fixed-size slice chosen to equal an earlier cross-transfer count, LAMOST uses top-1% despite failing injection recovery, Planck/NEOWISE use fixed top-1% counts, and eROSITA uses an irreproducible historical score axis before being excised. These are not comparable statistical detection thresholds.

3. [MAJOR] §III A DESI headline: the key DESI count is largely not a science-target anomaly catalog. The paper itself states that only 2,468 of 190,015 deduplicated DESI anomaly clusters match primary science-class targets, while ∼98.7% fall on sky/filler/secondary/calibration-like spectra. This severely undermines the catalog-grade and “largest anomaly catalog” framing.

4. [MAJOR] §II B/§VI D validation: the validation tests do not calibrate false positives or astrophysical reliability. Jaccard stability of a model’s top-1% list tests reproducibility of the ranking, not correctness; injection-recovery of artificial broad features does not validate real anomaly purity; and the narrow-line failure demonstrates a major unquantified incompleteness.

5. [MAJOR] §II B data leakage/provenance: tabular scalers are fit on the full sample including validation data, some production scripts are “recovered,” Gaia preprocessing is lineage-inferred, and eROSITA’s production score axis is explicitly irreproducible. This is incompatible with the claimed catalog-grade reproducibility standard.

6. [MAJOR] §III E eROSITA handling: the manuscript devotes substantial space to an eROSITA tier that fails injection recovery, has an irreproducible score axis, and is excluded from all counts. Its inclusion in tables, figures, novelty discussion, and follow-up recommendations creates confusion and weakens the claimed clean catalog definition.

7. [MAJOR] §III G Gaia handling: the fact that a synthetic-placeholder Gaia tier survived into prior catalog accounting indicates serious pipeline/provenance control failures. Merely excising it after audit does not by itself restore confidence in the remaining tiers without an external reproducibility audit.

8. [MAJOR] §III D/Table I LAMOST: LAMOST fails the injection-recovery gate and is identified as a 98% blue-excess training-bias artifact, yet it remains in the inclusive 377,482 count. The manuscript alternates between treating this as a methodological failure and using it to support scale claims.

9. [MAJOR] §III F Planck: the Planck CMB tier consists of fixed-count, in-sample autoencoder reconstruction outliers in standardized map patches, not demonstrated physical CMB anomalies. The held-out over-representation test is weak, assumes independent patches despite spatial correlations, and does not replace a proper held-out re-inference or foreground/noise-systematics analysis.

10. [MAJOR] §III H NEOWISE: the NEOWISE “PASS” is explicitly by construction: injected sources outside the mask are recovered by applying the same mask. This is a QA check of a coordinate cut, not validation of anomaly detection, and should not be included in a validated detector-sensitivity catalog.

11. [MAJOR] §IV A novelty: the genuine novelty fraction is measured only for the DESI top-1,000 and cannot support catalog-wide novelty statements. The SIMBAD-unmatched fractions are repeatedly shown despite being acknowledged as database-coverage artifacts; Fig. 6 also retains a historical denominator involving the removed Gaia tier, which is inappropriate for the final catalog.

12. [MAJOR] §IV C cross-survey matches: the claimed cross-survey validation is statistically weak. The DESI×SDSS raw matches are comparable to the estimated random expectation, and the three highlighted examples do not constitute meaningful validation of hundreds of thousands of candidates.

13. [MAJOR] §V cosmological applications: the fNL analysis yields no detected bias enhancement and no improvement after debiasing. The section is therefore not a PRD-level cosmological result and is disconnected from the catalog’s inadequately validated anomaly selection.

14. [MAJOR] §V A NANOGrav: the PTA analysis is an oversimplified spectral-index refit to factorized KDE free-spectrum products, not a full timing-likelihood model comparison. The decisive Bayes factor is only against a fixed circular SMBHB spectral index, which the manuscript itself acknowledges is a strawman relative to environmentally modified SMBHB models.

15. [MAJOR] Scope for Physical Review D: the primary deliverable is an astronomical/ML catalog, while the PRD-relevant cosmological material is explicitly secondary, null, and not a detection. The paper is therefore poorly matched to PRD unless the cosmological analysis is made central and substantially strengthened.

16. [MAJOR] Tables/Figures overall: many figures and table entries display historical cross-transfer baselines, removed Gaia material, quarantined ACT material, or excluded eROSITA quantities alongside final catalog values. This makes the final data product difficult to interpret and risks misleading readers.

17. [MAJOR] §II/§VI reproducibility claims: many results are asserted through repository artifacts, “will be released” statements, or pod-side histories rather than a self-contained reproducible analysis in the submission. For a catalog paper, the final frozen data products, scripts, hashes, and independent rerun checks must be available and stable at review time.

18. [MINOR] Writing/presentation: the manuscript is excessively caveated, repetitive, and internally defensive. Important definitions are buried in long footnotes, making the final catalog definition, validated subset, and count hierarchy unnecessarily hard to follow.

19. [MINOR] Notation: the anomaly score S, raw MSE, Planck MSE ranking, eROSITA raw score, IsolationForest score, and display scores are all used in close proximity. A compact score-axis table should replace the current scattered explanations.

20. [MINOR] Figures: several captions state that plotted quantities are historical, display-only, or non-catalog values. Such figures should be removed or moved to an appendix if they do not represent the final catalog.

(3) The central claim that the paper delivers a validated, catalog-grade set of 268,519 reconstruction-outlier sources is not supported by the evidence presented.