# INT API Review — P3APJS v3.1.157-apjs — openai (gpt-5.5)
paper: P3APJS  version: v3.1.157-apjs  model: gpt-5.5
modality: native-PDF (Files API input_file)
UTC: 2026-07-12T17:52:49.186662Z  |  latency: 51.2s  |  attempt: 1
usage: {"input_tokens": 64767, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 2802, "output_tokens_details": {"reasoning_tokens": 938}, "total_tokens": 67569}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

1. [MAJOR] Abstract/title/§3/§7 headline catalog definition: the manuscript still does not present a clean, stable definition of the released catalog. It alternates among 268,519 “validated,” 377,482 “inclusive,” 377,282 point-source, 387,695 survey-level detections, 319,443 cross-transfer baseline, and several process-volume denominators; the eROSITA and Gaia tiers are simultaneously tabulated and excluded, while LAMOST is known to fail validation but remains in the inclusive headline. ApJS requires one unambiguous primary catalog, with any failed/exploratory addenda clearly separated from the main machine-readable product.

2. [MAJOR] §3 three-tier structure and §6.4 validation: the term “validated catalog-grade” is overextended. DESI is validated only for broad/extended anomalies, SDSS for a continuum-dip injection, Planck for synthetic Gaussian-bump patches, and NEOWISE only for a mask-geometry QA test that passes by construction; LAMOST fails injection recovery but remains in the inclusive count. The manuscript must either define a uniform validation standard or rename these tiers as heterogeneous “anomaly-candidate” products with explicit per-object validation flags.

3. [MAJOR] §2.2–§2.4 and Data Availability reproducibility: several essential production artifacts are missing or described as unrecovered/lost, including raw production score parquets, some pod-side feature tables, exact Gaia production preprocessing, the Planck native checkpoint/tensor for full held-out re-inference, and the eROSITA production score axis. For an ApJS catalog/data-release paper, the end-to-end catalog-generation path must be reproducible from archived inputs, code, model weights, containers/environments, and immutable checksums, not only partially reconstructed from surviving artifacts.

4. [MAJOR] §3.5 eROSITA: the eROSITA component has an irreproducible production score axis and 1.2% injection recovery, yet is still discussed prominently and appears in Table 2. If excluded from all counts, it should be removed from the main catalog tables and moved to an appendix or separate addendum with no implication of catalog-grade status.

5. [MAJOR] §3.7 Gaia: the discovery that the Gaia tier was a synthetic-placeholder fallback is serious. The manuscript handles this transparently, but it also raises concern about pipeline safeguards and provenance auditing for all other surveys. The paper should include a concise, formal provenance-audit table for every retained input file, query, row count, and failure mode.

6. [MAJOR] §3.1 DESI science-target recount: the principal DESI result is dominated by sky/filler/non-primary spectra, with only 2,468 science-target anomaly clusters, ≈0.92× the Liang et al. benchmark. The title, abstract, and conclusions still emphasize process-volume multipliers that are likely to be misread as science-catalog gains. The manuscript should foreground the like-for-like result and demote the full-instrument-stream multipliers.

7. [MAJOR] §3.3 SDSS thresholding: the SDSS “77,905” tier is a fixed-size continuity slice, while the native top-1% is 19,253 and strict S>5 gives only 12 objects. This makes the SDSS contribution to the headline catalog threshold-dependent and not physically motivated. The authors must justify why the continuity slice, rather than the native score-knee or S>5 set, is included in the primary catalog.

8. [MAJOR] §3.4 LAMOST: LAMOST is explicitly a failed blue-excess training-bias artifact with 5.8% injection recovery, but it contributes ∼113,000 objects to the inclusive 377,482 total. A failed tier should not be part of a headline catalog total unless the headline is explicitly “all candidates including failed-systematics tiers,” which would be inappropriate as the main ApJS deliverable.

9. [MAJOR] §3.6 Planck: the Planck tier consists of CMB map patches, not sources, selected partly in-sample and scored on a raw MSE axis rather than canonical S. Combining these with point-source catalogs in a single headline number is conceptually confusing. The Planck patch catalog should be a separate data product with separate validation and not counted with point-source anomalies except in a clearly labeled “all data products” total.

10. [MAJOR] §2.2/§3/Table 2 score definitions: the manuscript uses multiple incompatible score axes—canonical S, DESI cross-transfer S, native S, raw MSE, raw eROSITA rank score, IsolationForest score, and display-only scores. These are repeatedly caveated but still appear together in tables and figures. The catalog needs a strict schema with one score-axis field per survey, units, calibration denominator, threshold definition, and “not comparable across surveys” metadata.

11. [MAJOR] §4.1 novelty: the manuscript correctly notes that SIMBAD-unmatched is not novelty, but figures and text still present “SIMBAD novelty fraction” language. The only defensible novelty estimate is the DESI top-1000 18-catalog cross-match result, and even that is a high-score-stratum point estimate. All SIMBAD-only “novelty” language should be replaced by “SIMBAD-unmatched.”

12. [MAJOR] §4.2 spatial analysis: the χ² spatial-uniformity test is dominated by survey footprint geometry and is not scientifically interpretable without selection functions. It should be removed or relegated to a diagnostic appendix; the main text should instead provide per-survey footprint-aware sky-density summaries or no spatial-uniformity claim.

13. [MAJOR] §4.3 deduplication/cross-matching: the fixed 5″ union-find dedup is serviceable for a first catalog but not fully justified across sub-arcsecond spectroscopy, NEOWISE’s larger PSF, and CMB patches. The paper needs a clearer association model, per-survey astrometric uncertainties, and a catalog flag distinguishing physical cross-identifications from bookkeeping merges.

14. [MAJOR] §5–§5.1 cosmological applications: the fNL and NANOGrav sections are not central to the catalog, yield no detection or improvement, and substantially distract from the ApJS catalog/methods contribution. They should be shortened drastically, moved to an appendix, or removed; the main paper should focus on the released catalog and validation.

15. [MAJOR] §6.3 limitations: several limitations are severe enough to require action before publication, not merely disclosure: unweighted MSE, sky/filler dominance, lack of architecture diversity for spectroscopic tiers, incomplete injection-recovery morphology coverage, and nonuniform validation gates. The revised paper should show how these limitations propagate into per-object reliability flags and recommended-use tiers.

16. [MINOR] Figures 2–4 and Table 4: several figures/tables show cross-transfer or obsolete diagnostic products rather than the final Path-C catalog. These should be clearly labeled as historical diagnostics or moved to appendices to avoid confusion.

17. [MINOR] Table 2 and footnotes: the table is overburdened with long explanatory footnotes and mixed inclusion/exclusion logic. Split it into at least three tables: retained validated catalog, exploratory/failed addenda, and historical cross-transfer diagnostics.

18. [MINOR] Writing style throughout: the manuscript repeatedly says “read once,” “to preclude misreading,” “honest limitation,” and similar defensive phrases. These should be replaced with concise technical statements.

19. [MINOR] LaTeX/text artifacts: there are numerous typographic and parsing artifacts, including “Nanom,” broken hyphenation, stray symbols, inconsistent use of “z-scored,” and malformed references to paths. These require copyediting before publication.

20. [MINOR] Data Availability: the pinned HuggingFace release and checksums are valuable, but ApJS readers need a compact data dictionary: column names, units, null conventions, coordinate frames, score-axis definitions, validation flags, survey-membership flags, and example loading code.

21. [MINOR] AI-assisted methodology statement: disclosure is appropriate, but the statement is too long and promotional. It should be shortened to the factual role of AI tools, human verification, and provenance safeguards.

22. [MINOR] References: several references are incomplete, future-dated, or not in final ApJS/AAS style; verify all bibliographic metadata and remove claims depending on unpublished or nonessential sources.

(3) Yes—the central idea of a released multi-survey anomaly-candidate catalog is appropriate for ApJS and appears potentially publishable, but the present manuscript does not yet support the stronger claim of a uniformly validated catalog-grade multi-survey anomaly catalog.