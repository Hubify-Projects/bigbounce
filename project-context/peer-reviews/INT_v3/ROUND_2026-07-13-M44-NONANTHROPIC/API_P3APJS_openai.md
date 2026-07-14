# INT API Review — P3APJS v3.1.159-apjs — openai (gpt-5.5)
paper: P3APJS  version: v3.1.159-apjs  model: gpt-5.5
modality: native-PDF (Files API input_file)
UTC: 2026-07-14T07:16:51.850645Z  |  latency: 46.5s  |  attempt: 1
usage: {"input_tokens": 65162, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 1699, "output_tokens_details": {"reasoning_tokens": 516}, "total_tokens": 66861}
PARSED VERDICT: REJECT

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: REJECT.

(2) ISSUES:

1. [MAJOR] Title/Abstract/§3: the headline “validated catalog-grade subset of 268,519” is not supported by uniform validation; it mixes DESI/SDSS/Planck detector-sensitivity tests with NEOWISE geometry-only masking QA, while excluding eROSITA for irreproducibility and including threshold choices that are explicitly not homogeneous.

2. [MAJOR] §3.1/§6.4(i): the DESI headline dominates the catalog but is not reproducible object-by-object because most released identifiers are internal hashes and only ∼1.3% of rows are re-pullable; the paper therefore cannot substantiate the released 195,829-object DESI list at the level required for a catalog claim.

3. [MAJOR] §3.1/Table 3: the DESI “largest catalog” comparison is fundamentally not like-for-like; the manuscript itself shows that ∼98.7% of DESI anomaly clusters are non-primary science targets, reducing the science-target yield to 2,468, below the cited benchmark, so the process-volume multipliers are scientifically misleading despite repeated caveats.

4. [MAJOR] §2.2/Table 2/§3.3–§3.4: the anomaly thresholds are arbitrary and survey-dependent in a way that undermines the combined catalog: DESI uses S>5, SDSS uses a fixed-size continuity slice although native S>5 gives only 12 sources, LAMOST uses a top-1% tier despite failing injection recovery, and Planck/NEOWISE use predetermined top-percentile selections.

5. [MAJOR] §3.4/§6.1: LAMOST is explicitly diagnosed as a 98% blue-excess training-bias artifact with 5.8% injection recovery, yet it contributes ∼113,000 objects to the inclusive 377,482 total; this makes the inclusive catalog a mixture of validated anomalies and known failure modes rather than a scientifically usable anomaly catalog.

6. [MAJOR] §3.8/§6.4(ii): NEOWISE is counted in the “validated catalog-grade” subset although its “injection-recovery” test is acknowledged to pass by construction and validates only the ecliptic mask implementation, not anomaly-detector sensitivity.

7. [MAJOR] §3.5/Data Availability: the eROSITA score axis is admitted to be irreproducible, non-monotone with the committed raw score, and failed at 1.2% injection recovery; discussing rank-ordered “top anomalies” while excluding the tier from all counts leaves a confusing and scientifically weak provenance trail.

8. [MAJOR] §3.6/Table 7: the Planck CMB tier is selected in-sample from the scored training bank, the native checkpoint and full tensor are stated not to be in the public release, and the validation relies on a simplified Gaussian-bump injection; this is insufficient to support a physical CMB anomaly tier.

9. [MAJOR] §4.1: the novelty analysis is overinterpreted; the 17.8% “genuine novelty” fraction is measured only for the DESI top-1,000 against selected catalogs and is explicitly not a survey-wide rate, while the paper repeatedly reports much larger SIMBAD-unmatched fractions that are not discovery fractions.

10. [MAJOR] §5: the fNL application is not a physics result suitable for PRD; the empirical bias measurement is α=0.19±0.65, consistent with zero, the de-biased forecast returns exactly the single-tracer baseline, and the QSO-candidate sample lacks the redshift and selection-function characterization needed for a credible multi-tracer forecast.

11. [MAJOR] §5.1/Appendix E: the NANOGrav analysis compares a fixed matter-bounce spectral index to an idealized circular-orbit SMBHB reference using a factorized KDE free-spectrum likelihood and then acknowledges environmentally modified SMBHB models can give γ≈2.5–3; the quoted Bayes factor is therefore not evidence for bounce cosmology and is too model-incomplete for the claims made.

12. [MAJOR] §2.2/§6.3: the machine-learning validation is not adequate for catalog-grade astrophysical inference: tabular scalers are fit on full samples, some robustness checks use short-trained proxy models that fail the paper’s own validation-loss gate, architecture dependence is largely untested, and the unweighted MSE scorer is known to miss narrow lines below ≳15σ.

13. [MINOR] Throughout: the manuscript is excessively long, repetitive, and internally defensive, with many caveats embedded in captions and footnotes rather than a clear methodology/results structure.

14. [MINOR] Tables 1–2/Data Availability: the multiple denominators and totals—36.76M, 36.93M, 37.29M, 37.3M; 377,482, 378,280, 378,480—are difficult to audit and should be replaced by one unambiguous accounting table if resubmitted elsewhere.

15. [MINOR] Figures 3, 4, and 8: several plotted score axes are explicitly historical, cross-transfer, display-only, or non-catalog values; these figures risk misleading readers and should be separated from catalog-defining results.

(3) The central claim is not supported to PRD standards: the work demonstrates a large, heterogeneous reconstruction-outlier pipeline, but not a uniformly validated, reproducible astrophysical anomaly catalog or a credible cosmological result.