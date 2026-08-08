# INT API POST-POLISH (native-PDF) — P3 v3.1.140 — openai (gpt-5.5)
PAPER: P3  |  VERSION: v3.1.140  |  MODEL: gpt-5.5
MODALITY: native-pdf (Files API purpose=user_data + Responses input_file)
UTC: 2026-07-07T07:06:30.760780+00:00  |  latency: 40.7s
USAGE: {"input_tokens": 58458, "input_tokens_details": {"cached_tokens": 0}, "output_tokens": 1695, "output_tokens_details": {"reasoning_tokens": 516}, "total_tokens": 60153}
PARSED VERDICT: REJECT

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: REJECT.

(2) ISSUES:

1. [MAJOR] Abstract / §III / §VII, “268,519 validated sources” and “validated subset is real”: the manuscript does not establish catalog-grade astrophysical validity for the headline set. Most validation gates test algorithmic stability or response to highly idealized injected signals, not whether the selected objects are genuine astrophysical anomalies; DESI is dominated by non-primary science targets, NEOWISE passes only a mask-geometry QA by construction, and Planck entries are CMB patches rather than sources.

2. [MAJOR] §III A, DESI headline count: the paper’s largest component, 195,829 DESI anomalies, is a full fiber-stream selection in which ∼98.7% of deduplicated clusters do not match primary science-class targets. This severely undercuts the presentation of the result as an astronomical source catalog and makes the large process-scale multipliers misleading despite later caveats.

3. [MAJOR] §II B / Table I, anomaly-score definitions and thresholds: the catalog combines heterogeneous and partly arbitrary selection rules—DESI S > 5, SDSS fixed-size “continuity slice,” LAMOST top-1%, Planck fixed top-200, NEOWISE fixed top-1%, eROSITA top-298 membership—with per-survey non-comparable score scales. The headline count is therefore not a well-defined statistical anomaly sample.

4. [MAJOR] §II B / §III E, provenance and reproducibility: the eROSITA score axis is admitted to be irreproducible, Gaia was discovered to be synthetic and removed, tabular scalers were fit on full samples, and many central numerical claims depend on repository artifacts that are only said to be released later. A PRD submission cannot rely on unavailable external JSON files and future data release for validation of the central results.

5. [MAJOR] §VI D, injection-recovery validation: the injection tests are not sufficiently representative of the anomaly classes claimed. DESI narrow-line sensitivity fails below ≥15σ; LAMOST and eROSITA fail; NEOWISE is not a detector-sensitivity test; and Planck uses artificial Gaussian-bump injections in standardized patches. These tests do not justify the broad statement that the 268,519-object subset is “validated.”

6. [MAJOR] §III F / §IV C, mixing point sources and CMB map patches: the catalog combines point-source detections with 200 Planck CMB sky patches and applies positional deduplication language across physically different entities. This is inappropriate for a “source catalog” and should not be included in the same headline count without a separate, fully justified statistical treatment.

7. [MAJOR] §IV A, novelty assessment: the claimed 17.8% “genuine novelty fraction” is measured only for the DESI top-1,000 against a selected catalog list and is explicitly not survey-wide. The manuscript repeatedly juxtaposes this with SIMBAD-unmatched fractions, which are database-coverage diagnostics, not discovery statistics; the discovery/novelty claims are therefore overstated.

8. [MAJOR] §V, multi-tracer fNL application: the cosmological result is explicitly a null result. The empirical bias α = 0.19 ± 0.65 is consistent with zero, the de-biased estimate gives no improvement, and the quoted central σ(fNL) = 8.14 is a noise-driven convex mapping. This does not constitute a PRD-level cosmological constraint and should not be part of the headline motivation.

9. [MAJOR] §V A / Appendix E, NANOGrav analysis: the KDE free-spectrum refit with factorized bins is not a full PTA likelihood analysis, and the Bayes-factor comparison is only against an idealized circular SMBHB spectral index while environmentally modified SMBHB models can match γ ∼ 2.5–3. The “decisive” Bayes-factor language is therefore potentially misleading and not a robust cosmological inference.

10. [MAJOR] §II D / §VI D, validation gates: the pass/fail thresholds are described as heuristic engineering choices rather than statistically motivated criteria. Since survey inclusion and the headline catalog depend on these gates, the lack of pre-defined statistical justification is a central methodological weakness.

11. [MAJOR] §IV C, cross-survey matches: only 637 multi-survey coincidences are found, and the DESI×SDSS match expectation is comparable to random positional matches before spectroscopic inspection. The sparse cross-survey overlap does not provide strong validation of the catalog as a coherent multi-survey anomaly product.

12. [MINOR] Presentation throughout: the manuscript is excessively long, with repeated caveats, footnotes, and bookkeeping reconciliations that obscure rather than clarify the scientific result. A journal submission should separate a concise paper from pipeline audit documentation.

13. [MINOR] Figures 3, 4, and 8: several plotted score axes are historical cross-transfer or display-only values, not catalog scores. This is confusing and risks misinterpretation; figures should use only final catalog quantities or be moved to a methods appendix.

14. [MINOR] §VII / Data availability: “will be publicly released with the arXiv posting” is insufficient for review of a data-product paper. The catalog, model weights, scripts, hashes, and exact artifacts needed to reproduce headline numbers must be available to referees at submission.

(3) One sentence: The central claim that the manuscript delivers a robust, catalog-grade set of 268,519 validated astronomical anomaly sources is not supported by the evidence presented.