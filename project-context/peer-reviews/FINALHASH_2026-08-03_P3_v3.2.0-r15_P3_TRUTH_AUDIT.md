# P3 FINALHASH truth audit — 2026-08-03

**Bound PDF:** `paper3_apjs.pdf`, SHA-256
`793575f5705c421a3c75bfa2fe66b9f3c07aed327a2a75e01f835f952aee47ef`.

## Vendor outcomes

- **Gemini, Grok, and Perplexity:** all unavailable before review dispatch. Each
  reviewer artifact records `PortfolioError: portfolio receipt is stale` while
  rebuilding its review packet, so no provider read or made a scientific finding
  about the bound P3 PDF.

The round-level receipt check accepted the supplied receipt before dispatch; the
subsequent packet-level guard failed. The failure is recorded as an execution
state, not interpreted as evidence about the paper.

## Truth audit

There are no vendor scientific findings to adjudicate. The bound SHA-256 matches
the requested P3 final candidate. No source or package claim was changed here.

**Genuinely-new-real defects:** none observed (all reviewers unavailable).
**Reopen decision:** no scientific reopen; rerun only after the packet preflight
guard is made consistent with the receipt-bound final state.

## Recovered Gemini full-PDF leg — FINALHASH2

**Raw report:** `FINALHASH2_2026-08-03_P3_v3.2.0-r15_P3_Gemini_cosmology.md`.
Gemini 3.1 Pro preview reviewed the exact 17-page bound PDF with packet
`0ca9e4b728607de633deed432ceaa98ac1ff91b6fe425a61dc7204b07ebc5ab2`;
its self-critique reported no additional findings.

| Gemini finding | Truth-audit disposition |
|---|---|
| 1. Version/audit language | Existing venue/editorial issue, not a new integrity defect. The r10 exact-PDF board already recorded version-tag proliferation as a minor and the current source supplies an explicit component-version key. The retained tags identify frozen data, auxiliary, bundle, and manuscript surfaces; an editor may ask for shortening, but no claim is false. |
| 2. r10 Zenodo versus r15 | Existing, explicitly honest human publishing gate. Data Availability says the DOI binds r10 bytes and subsequent versions must be added; the r15 portal kit repeats that fact. It is not evidence that r15 bytes were misidentified, and cannot be repaired by invented DOI metadata. |
| 3. Length, paths, commands, hashes | Existing DP3-16 venue/style opinion. The cited material is reproducibility evidence for an ApJS catalog; whether to move it to a deposit is an editorial choice, not a newly found scientific or provenance error. |
| 4. Effect sizes/tests for warning-table medians | Misapplied to an explicitly descriptive comparison. The source calls it descriptive, disclaims selection-probability/bias inference, and does not use it as a significance claim. |
| 5. BigAE/canonical-S undefined | Stale re-flag. Section 2.1 now specifies the frozen `S>5` selection, immutable commit, 496-to-128 BigAE lineage, five-seed reconstruction-MSE score, and the unrecoverable-normalization boundary; this is the bounded closure required by the earlier P3 r4 audit. |
| 6. “essentially” at the seed coordinate | Falsified as uncomputed. The adjacent text gives median target-to-cluster separation `0.00127 arcsec`, zero min/median/90th-percentile original-member separation, and the deterministic centroid mechanism. |
| 7. “associated most directly with fit discrimination” | **Genuinely new, minor wording issue.** The listed medians/IQRs support a descriptive contrast, but “most directly” ranks associations without a stated association metric. It should be softened to a descriptive observation or supplied with a declared metric in a later editorial-only pass. |

**Recovered-leg verdict:** one genuinely-new-real **minor** wording issue; zero
new scientific, catalog-integrity, arithmetic, or provenance defects. **Reopen
decision:** no readiness/science reopen. Record the optional wording closure for
the next explicitly authorized P3 editorial revision; do not alter this exact
final-hash source in this audit pass.
