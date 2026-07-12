# INT API Review — P3APJS v3.1.156-apjs — openai (gpt-5.5)
paper: P3APJS  version: v3.1.156-apjs  model: gpt-5.5
modality: native-PDF (Files API input_file)
UTC: 2026-07-12T16:24:43.531762Z  |  latency: 56.2s  |  attempt: 1
usage: {"input_tokens": 64627, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 2955, "output_tokens_details": {"reasoning_tokens": 1034}, "total_tokens": 67582}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

1. [MAJOR] Title/Abstract/Table 1/Table 2 — The headline accounting is too convoluted and still internally confusing: 36.76M, 36.93M, 37.29M, “37.3M,” 274,353, 268,519, 377,482, 387,695, 319,443, and several excluded/quarantined tiers are all introduced. For an ApJS catalog paper, the title and abstract must state one primary released product, one primary input denominator, and one primary validation tier, with all other historical/exploratory products clearly moved to secondary tables or appendices.

2. [MAJOR] §3 and Abstract — The phrase “validated catalog-grade” is not justified as a uniform label. DESI, SDSS, and Planck have some form of detector-sensitivity test, but NEOWISE has only a mask-geometry QA test that passes by construction, and Planck is an in-sample fixed-count patch selection. The manuscript should rename the tier or split it into detector-validated, geometry-QA, and exploratory products, rather than presenting all 268,519 as equivalently validated.

3. [MAJOR] §3.1/Table 3 — The DESI catalog is dominated by non-primary science-target spectra: the manuscript states that ≈98.7% of DESI anomaly clusters lie on sky/filler/non-primary spectra and 86% have TARGET=0. These are not obviously “sources” in the astrophysical catalog sense. The released product must distinguish observations/fiber spectra from astrophysical objects, and the headline point-source count should not include sky/calibration/filler spectra unless their astrophysical source identity is demonstrated.

4. [MAJOR] §2.2/§2.4/Data Availability — Reproducibility is not yet sufficient for ApJS publication. The manuscript repeatedly refers to local paths, exited pods, unreleased checkpoints, lost production parquets, “will be public” releases, and a DOI to be inserted later. The referee cannot verify the catalog. At review time, the machine-readable tables, schemas, model weights, dedup scripts, manifests, hashes, and exact command-line reproduction instructions must be public or supplied to the journal.

5. [MAJOR] §2.2/§3.5/§3.7 — The Gaia synthetic fallback and irreproducible eROSITA score axis reveal serious pipeline-provenance failures. Although the manuscript now excises those tiers, ApJS requires confidence that the retained tiers were not similarly affected. Provide a concise provenance audit table for every retained input file, including archive query, row counts, checksums, failure rates, and proof that no synthetic or fallback products enter DESI/SDSS/LAMOST/Planck/NEOWISE.

6. [MAJOR] §2.2/§2.4/Table 2 — The thresholds are heterogeneous and partly arbitrary: DESI uses S>5, SDSS headline uses a fixed-size continuity slice, LAMOST uses top 1%, Planck/NEOWISE use fixed top counts, and eROSITA was a top-298 cap. This is acceptable only if the catalog is explicitly a ranked outlier data product, not an estimate of anomaly incidence. Remove or heavily qualify “anomaly rate” columns where fixed-count thresholds are used.

7. [MAJOR] §6.4/Fig. 10 — The injection-recovery validation is not yet adequate as a catalog-completeness characterization. The planted signal families are narrow and survey-specific, NEOWISE is not a sensitivity test, DESI fails for narrow single-pixel lines until ≥15σ, SDSS passes only marginally at 64%, LAMOST/eROSITA fail, and false-positive/purity estimates are weak. The paper should present validation as sensitivity to specific planted morphologies, not general anomaly validation.

8. [MAJOR] §3.1/§6.4 — DESI robustness relies partly on short-trained proxy models that fail the paper’s own validation-loss gate, plus a production ensemble whose raw full-catalog score products are not available. This must be simplified and made auditable: either provide the production scores/checkpoints and rerun scripts, or reduce the strength of the DESI robustness claim.

9. [MAJOR] §3.4 — LAMOST fails injection recovery and is described as a 98% blue-excess training-bias artifact, yet it contributes ∼113,000 objects to the inclusive 377,482 count. For an ApJS catalog, failed-systematics tiers should not be included in the main catalog total; release LAMOST as a separate “failure-mode/exploratory” table and remove it from the primary count.

10. [MAJOR] §4.1 — The novelty discussion remains overinterpreted. The robust archival novelty estimate is only for the DESI top-1,000 and is explicitly an upper-bound-like high-score stratum estimate, not a survey-wide discovery fraction. The abstract/conclusions should avoid calling 17.8% the catalog discovery rate and should provide the full cross-match table, catalogs used, radii, local-density false-match estimates, and object-level match flags.

11. [MAJOR] §4.3 — Deduplication mixes different physical entities: DESI/SDSS/LAMOST spectra, NEOWISE infrared catalog entries, and Planck CMB map patches. A 5″ friends-of-friends rule is not physically meaningful for CMB patches and may be too small for WISE-like associations. The catalog must separate “object/source” deduplication from “sky-region/patch” products and justify per-survey association radii.

12. [MAJOR] §5/§5.1/Appendices C/E — The cosmology sections are not central to the ApJS catalog release and are not supported at the same level as the catalog. The fNL analysis yields no significant improvement, and the NANOGrav spectral-index exercise is essentially unrelated to the anomaly catalog. These sections should be shortened substantially, moved to an appendix, or removed to avoid distracting from the catalog/methods paper.

13. [MAJOR] Figures 2, 3, 4, 8, 9, 10 — Several figures show historical, cross-transfer, quarantined, display-only, or non-catalog score axes, while the released catalog uses different native scoring. This is confusing and risks misinterpretation. Main-text figures should show only released catalog products and canonical score definitions; historical/quarantined figures belong in appendices.

14. [MAJOR] Machine-readable catalog description — The manuscript lacks a clean ApJS-style data-product specification. Add a table defining every released column, unit, null convention, coordinate frame, score axis, validation flag, survey-membership flag, duplicate-cluster identifier, object/observation/patch type, and recommended-use flag.

15. [MINOR] §2.1/§2.2 — The architecture and preprocessing description is too verbose but still not fully standardized. Provide a concise configuration table per survey rather than long prose, and explicitly state which scalers are fit on train-only versus full-sample data.

16. [MINOR] §2.2 — Full-sample scaler fitting for tabular surveys introduces validation leakage. The manuscript discloses this, but the final release should either refit train-only scalers or mark affected scores as legacy/exploratory.

17. [MINOR] §3.5 — Since eROSITA is excluded from all counts and has an irreproducible production score axis, its long discussion should be moved to an appendix or shortened to a provenance note.

18. [MINOR] §3.8/Fig. 5 — The NEOWISE top anomaly appears optically saturated with diffraction spikes; the manuscript should be more cautious about treating it as an astrophysical infrared anomaly without artifact/bright-star contamination analysis.

19. [MINOR] §4.2 — The HEALPix χ² spatial-uniformity test is acknowledged as footprint-dominated and not scientifically interpretable. It should be removed from the main argument or replaced by per-survey footprint-normalized diagnostics.

20. [MINOR] §6.3 — Limitations are partly duplicated and overly long. Consolidate the limitation list and separate “catalog-use caveats” from “future methodological improvements.”

21. [MINOR] Writing/style throughout — The manuscript is overburdened with defensive parentheticals, “read once” instructions, repeated caveats, and process-volume explanations. A major editorial pass is needed to make the paper readable as an ApJS data release.

22. [MINOR] References — Several citations are future-dated, incomplete, or not standard bibliographic entries. Ensure all references are real, published/accepted/arXiv-accessible, and formatted in AAS style.

(3) The central claim—a released multi-survey autoencoder anomaly-candidate catalog—is appropriate for ApJS in principle, but it is not yet fully supported in the present manuscript because the primary catalog definition, validation tiers, provenance, and reproducibility package require major clarification and public verification.