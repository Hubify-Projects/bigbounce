# EXT21 P3 Grok — chat: https://grok.com/c/326b54ed-df2a-40db-a70a-4b580d6d49c5

Referee Report: MNRAS / PRD / JCAP
Manuscript: Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches
Author: Houston Golden
Date of report: 26 June 2026
Recommendation: MINOR REVISIONS

The manuscript presents the largest multi-survey autoencoder anomaly detection campaign to date, applying the BigAE framework (with a well-motivated Path-C native-retrain protocol) to ~37.3 million sources/patches across DESI DR1, SDSS DR18, LAMOST DR10, eROSITA DR1, Planck, Gaia DR3 and NEOWISE. After 7-way 5″ positional deduplication the headline catalog contains 378,280 unique entries (378,080 point sources + 200 Planck map patches). The work includes per-survey validation (k-fold Jaccard, OOD Jaccard, injection-recovery at multiple amplitudes), transparent documentation of failure modes (LAMOST training-bias artifact, eROSITA score-axis irreproducibility, Gaia low cross-validation stability), a genuine-novelty estimate (~17.8 % for the DESI top-1 000 via CDS X-Match against 18 all-sky catalogs), three spectroscopically confirmed DESI×SDSS cross-matches (including one new BAL QSO at z ≈ 0.86), and cautious cosmological applications (multi-tracer fNL forecast consistent with no improvement; NANOGrav 15-yr free-spectrum consistency check with γ = 2.567 ± 0.382).

The paper is ambitious in scope, methodologically careful, and unusually transparent about limitations and exploratory tiers. The Path-C protocol (native retrain + multi-gate validation) is a clear methodological contribution that future large-scale anomaly searches should adopt. Reproducibility artefacts (committed pod scripts, training logs, deduplication audits) and the planned public release of catalog, weights and scripts are exemplary.

No load-bearing scientific claim is unsupported, no critical control is missing, and core results are reproducible from the committed artefacts once the membership-list framing for eROSITA is accepted. The issues identified below are matters of clarity, scope emphasis and minor editorial polish rather than fundamental scientific rework.

BLOCKERS
None.

MAJORS

DESI scope and interpretation of headline numbers (Abstract; §III A; Table II).
The headline 195 829 DESI anomalies (S > 5) and the ~73× benchmark claim refer to the full 22.5 M-spectrum stream, of which only ~1.3 % (2 468 clusters at 1″) coincide with primary science-target bitmasks (BGS/LRG/ELG/QSO/MWS). The science-target-restricted recount is ~0.9× the Liang et al. benchmark, not 73×. The text already performs and reports this recount (Table II), but the abstract and early sections still foreground the full-stream 195 k / 73× figures.
Fix: In the abstract and §I / §III A opening paragraphs, explicitly state the two headline numbers side-by-side and direct readers to the catalog-grade point-source subset (269 117) and the science-target recount for any claim about "largest anomaly catalog relative to prior science-target searches". Add one sentence in the abstract: "Of these, only ~1.3 % coincide with primary science-target spectra; the science-target-restricted DESI subset is comparable in size to the largest previous single-survey catalog."

eROSITA reproducibility framing (Abstract; §III E; Table I footnote; Table IV).
The production SBigAE score axis is irreproducible on any of 16 tested monotone rescalings and the IsolationForest axis; the committed selection is the n = 298 membership list (top-298 of the raw-score artefact). The paper is transparent and correctly adopts the "membership-list-is-canonical" stance, with high internal cross-validation stability (81.5 %). However, the abstract and Table I still quote a 0.03 % rate and a threshold (0.259) that cannot be recovered.
Fix: In the abstract and Table I caption, change the eROSITA entry to read "298 (membership-list only; score axis non-reproducible — see §III E)" and remove the numerical rate cell or mark it clearly as non-data-driven. In §III E add a one-sentence user warning: "Downstream analyses requiring a reproducible per-object score should operate on the committed raw-score artefact or the membership list; the published SBigAE values are not recoverable."

MINORS

Abstract / Table I. The two catalog-grade numbers (269 317 total unique vs 269 117 point-source) are correctly distinguished in the body but the abstract compresses them. Add the parenthetical "(269 117 point sources after dropping 200 Planck patches)" already present in the body to the abstract for immediate clarity.

LAMOST tier (§III D; Table I footnote ♠). The 113 342-object native top-1 % slice is correctly labelled exploratory and excluded from the catalog-grade 269 k subset. A single clarifying sentence in §VI A or the abstract would help: "Readers requiring a catalog-grade sample should use the 269 117-object point-source tier (DESI + SDSS native + eROSITA membership + Planck + Gaia + NEOWISE); the LAMOST tier is retained solely as a methodological demonstration."

Gaia preprocessing provenance (§II B; §III G). The 20-feature production script was not recovered; the specification is lineage-inferred from a 21-feature successor. This is already disclosed but should be flagged once more prominently in the Gaia subsection and in any table that quotes Gaia anomaly counts: "Gaia rates and rankings are best-available rather than fully scratch-reproducible."

Figure & table captions / footnotes. Several long footnotes (especially Table I ♡, ♠, §, ∥) contain essential methodological caveats. Consider moving the longest technical details to an appendix or supplementary note so the main tables remain readable; keep a short "see text / appendix" pointer in the caption.

Minor editorial / consistency.
– "Path-C unique" vs "Path-C native-retrained" terminology is used interchangeably in places; adopt one canonical phrase after first definition.
– A few figure panels (e.g., Fig. 3 right panel log-log dynamic range) would benefit from an explicit note that the extreme tail is a cross-transfer artefact eliminated by the native re-score.
– Reference list: confirm all arXiv IDs cited as "25xx/26xx.xxxxx" are correctly formatted for 2026-era preprints (minor).

Future-work / queued items. All explicitly labelled "queued", "pending higher S/N", "deferred to catalog release", or "companion data repository" items are appropriately scoped and do not require further action for acceptance.

STRENGTHS (selected; ≥3 required)

- Unprecedented scale + rigorous multi-survey protocol. 37.3 M sources processed; Path-C native-retrain + six-step validation (k-fold Jaccard ≥0.70/0.50 gates for DESI, injection-recovery for SDSS/Planck/NEOWISE, systematics masks, 7-way 5″ deduplication) sets a new standard for large-scale astronomical anomaly detection. The ~141× (catalog-grade point-source) increase over the previous single-survey benchmark is impressive even after scope reconciliation.

- Exceptional transparency and self-audit. Every major failure mode is quantified and labelled (LAMOST 98 % blue-excess training-bias artefact and 5.8 % injection-recovery; eROSITA score-axis irreproducibility; Gaia 41 % XV-stability → exploratory; Planck val-loss vs injection trade-off). Exploratory vs catalog-grade tiers are cleanly separated. This honesty materially increases the scientific value of the released catalog.

- Reproducibility infrastructure. Committed pod-provision JSONs, training logs, deduplication audits, scaler-refit robustness checks, and the explicit "membership-list-is-canonical" framing for eROSITA allow independent verification. The planned public release of catalog, model weights and scripts is best-practice.

- Astrophysical return. Three spectroscopically confirmed DESI×SDSS cross-matches (including a new uncatalogued BAL QSO at z ≈ 0.86), a quantified 17.8 % genuine-novelty fraction for the DESI top-1 000, and a clean high-z QSO candidate selection (Gunn-Peterson + Z-arm dominance) demonstrate immediate utility. The cosmological applications (fNL multi-tracer forecast with empirical αjk = 0.19 ± 0.65 and envelope; NANOGrav γ consistency check) are presented with appropriate caution and scoping.

- Methodological legacy. The Path-C rebuild protocol (native retrain + injection + Jaccard + deduplication) and the explicit documentation of cross-transfer failure modes provide a reusable template for future petabyte-scale surveys (LSST, Euclid, Roman, SKA).

Summary

This is a high-impact catalog paper whose core contribution — the largest, most rigorously validated multi-survey anomaly catalog yet produced, with full transparency on limitations — is sound. The two major points above are straightforward clarifications of scope and user guidance that can be addressed without new analysis. I recommend MINOR REVISIONS; once the abstract and eROSITA framing are tightened the manuscript will be suitable for MNRAS / PRD / JCAP.

I am happy to re-review a revised version.

Sincerely,
External Referee
