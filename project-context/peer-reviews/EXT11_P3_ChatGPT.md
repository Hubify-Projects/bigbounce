# EXT11 Harvest — P3 — ChatGPT

- Provider: ChatGPT
- Model/Effort: Pro Extended
- Chat URL: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc617-2480-83e8-bf48-cc78a7bce891
- PDF md5: 17c9296b (paper3_anomaly_catalog_v3.1.107_17c9296b.pdf)
- Harvested: 2026-06-13 17:17 PDT

---

## Headline Verdict: MINOR REVISIONS (very close to accept)

This is now very close to acceptability. No need for major scientific rework. The main EXT10 scientific/numerical closures are substantially addressed. Would move to ACCEPT after two small but non-style corrections: one wording inconsistency about "catalog-grade" survey validation, and one clarification/correction to the new NANOGrav prior-sensitivity table.

## EXT10 Items Status

- **Data/product release:** Still open as a publication-production condition (not scientific rework). Replace future-tense text with live DOI before journal publication.
- **DESI top-1% wording:** Closed. S>5 fixed-threshold, 195,829 anomalies, 0.87% of 22.5M-spectrum scan.
- **378,280 headline stratification:** Mostly closed; see new wording issue below.
- **Cramér's V arithmetic:** Closed. Value now ~0.0064.
- **Fisher-positivity caveat:** Closed. Paper now consistently uses 1/σ²(f_NL) = F₀ + cα², central σ(f_NL)=8.14, envelope [3.92,8.98].
- **NANOGrav robustness table:** Addressed, but see New Item 2.
- **eROSITA/Gaia schema/provenance flags:** Mostly closed.

## New Items Introduced by Closures

### New Item 1 — "catalog-grade" validation wording internally inconsistent (MINOR, fix required)

The abstract now says the 269,117 catalog-grade point-source subset is "derived from the six surveys that pass injection-recovery and native-retrain validation." But the manuscript also states that eROSITA and Gaia fail the 5σ injection-recovery gate.

**Proposed fix:** Replace that abstract phrase with:
> "the recommended non-LAMOST point-source subset is therefore 269,117 unique entries, with per-survey validity flags distinguishing DESI/SDSS/Planck/NEOWISE validated components from the eROSITA membership-only and Gaia exploratory components."

Alternatively, if "catalog-grade" is retained, define exactly which surveys qualify and do not say all six pass injection recovery.

### New Item 2 — Table IX prior-sensitivity arithmetic/definition needs clarification (MINOR, fix required)

Table IX says all quantities are obtained from the fiducial γ∈[0,7] chain by prior re-weighting, but B_{MB/SMBHB} varies strongly with prior width while B_{MB/free} is nearly constant — this behavior needs explanation. For a standard Savage-Dickey comparison using the same flat γ prior with both fixed γ values inside the tested prior range, the ratio should largely reduce to a posterior-density ratio and should not vary strongly merely because the uniform prior width changes.

**Proposed fix:** Either correct Table IX using a consistent Savage-Dickey density-ratio convention, or add one sentence explaining exactly why the ratio changes under the stated re-weighting procedure. This is a small numerical/method-definition correction, not a major scientific rework.

## Bottom Line

MINOR REVISIONS. The EXT10 scientific closures are largely successful. Accept-ready once the catalog-grade validation wording and Table IX prior-sensitivity definition are corrected, with the live DOI/release update handled as a publication-production condition.
