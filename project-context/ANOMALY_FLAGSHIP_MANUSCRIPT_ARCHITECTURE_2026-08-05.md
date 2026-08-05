# Anomaly flagship manuscript architecture

**Draft for Houston · 2026-08-05 · execution-plan step "Anomaly manuscript
architecture" (`PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md`, step 2)**

This document is derived from `ANOMALY_SCIENCE_CLAIM_INVENTORY_2026-08-03.md`
(the "Recommended flagship scope," "Claim-by-claim audit," and "Required
closure gates" sections), the reset doc's survey-discovery program row, and
`SSOT/queue.md` item 3 (AUG-011, the clean rerun now running). No number below
was invented for this document — every historical figure is lifted from the
inventory, every AUG-011 figure is lifted from queue item 3, and every
new-generation quantity that does not exist yet is marked **PLACEHOLDER**.

It does not itself contain new science. It is the skeleton the manuscript gets
written into once AUG-011's remaining phases land.

## 0. What changed since the inventory

The inventory's fallback route ("rerun a clean DESI survey") is the route
Houston chose and it is now executing: AUG-011 sealed its contract 2026-08-05
(commit `568a33bf`) and is mid-scan. That means this architecture is written
against the fallback route, not the preferred route — **the primary sample is
the new sealed-contract generation, not the 2,145/1,127 historical slice.**
The historical slice remains real, preserved, and useful, but only as a
comparison set, per the inventory's own instruction that the old products
"become historical comparison sets rather than the new paper's primary
sample."

## 1. Research question

> What astrophysical candidate populations survive a reproducible,
> public-ID-first, SNR-aware filtering and external-catalog follow-up of the
> sealed-contract AUG-011 clean rerun of the DESI DR1 `iron` autoencoder scan,
> and which of those candidates are supported well enough to report as
> candidates rather than discoveries?

This is the inventory's preferred-route question (`ANOMALY_SCIENCE_CLAIM_INVENTORY_2026-08-03.md`,
"Recommended flagship scope") with one substitution: "a survey-scale DESI
autoencoder scan" becomes "the sealed-contract AUG-011 clean rerun," because
the enhanced-catalog parent that the preferred route depended on could not be
restored (inventory, "Restoration gate result — 2026-08-04").

## 2. Primary deliverables

### (a) New-generation post-dedup scored catalog, with sealed provenance chain

The primary deliverable is not a bare score table — it is the table plus its
receipts, because the entire rebuild exists to fix the provenance failure that
sank the original manuscript. The provenance chain to publish:

- official DESI DR1 `iron` zcatalog SHA-256 `2d95ad99361039b556c402b49e0e7c84df5f00106dc5731d44476a58b128b49b`;
- 36,634-group locator inventory (hash `f3299a31…`);
- sealed two-stage PPS calibration: `mse_mean 0.8771` / `mse_std 1.3605`,
  stability gate PASSED at deviation `0.0054` against bound `0.0481`;
- run contract binding archived model SHA-256 `f5266ba4…` (the same
  `best_model_47k.pt` verified byte-identical across four local copies and the
  live Hugging Face revision `8100e0933242e5e74df912cb1414d922cd60596e`) and
  inference code hash `3e7efb24…`;
- public-ID-first filter: group-targetids export (hash `013990ca…`) agreeing
  with the inventory on all 36,634 groups / 28,425,963 rows;
- per-group JSON audit line for every scored group (`kept`, `surplus_dropped`,
  `zcat_missing_from_coadd`), not just the groups that dropped rows;
- shard-level receipts (11,200 shards receipt-verified intact as of the
  2026-08-05 incident reconciliation — 0 bad, 0 orphans).

The catalog is the `summarize-after-dedup` output: last-TARGETID-occurrence
deduplication in lexical shard-then-row order, streamed through SQLite. **Row
count is PLACEHOLDER** — the scan is still running (queue item 3: "FULL SCAN
RUNNING since 2026-08-05 09:43Z," observed rate ~12 groups/min → ~2 days
wall-clock as of that entry).

### (b) Filtered candidate slice — PLACEHOLDER thresholds

Analog of the historical 2,145-row rule (`anomaly_score > 3.0` and
`max_snr > 0.5`, per the inventory's claim table), rebuilt on the new score
distribution. **The exact thresholds are PLACEHOLDER and must be derived from
the new run's score distribution, never copied from the historical rule or
tuned to reproduce 2,145 rows.** Note the codebase also carries a distinct
`S>5` selection threshold used by `summarize-after-dedup` for
generation-comparison purposes (RUNBOOK step 13) — that is a different cut
than the silver-slice rule and the two must not be conflated in the
manuscript.

### (c) SIMBAD/NED cross-match + unmatched-candidate taxonomy, rebuilt on the new slice

Re-run of the cross-match/taxonomy machinery (historical implementations:
`pipelines/p1_highz_tracers/scripts/silver_crossmatch.py`,
`scripts/step2_crossmatch_full.py`, taxonomy clustering analog to
`projects/h200_scripts/anomaly_taxonomy.py`) against the new-generation
filtered slice from (b), not against the historical 2,145/1,127. Historical
family counts (10 families, 76 AGN, 27 post-starburst) are reported only as
comparison figures, per the claim-table's allowed wording.

### (d) Named follow-up demonstrations — method demonstrations only

NEOWISE variability, `z>6` QSO candidates, and latent-space photo-z are
reported **only as method demonstrations**, using the inventory's exact
allowed wording, and only from the historical runs unless/until they are
independently re-executed on the new slice:

- NEOWISE: "Sixteen of 283 examined candidates met the recorded NEOWISE
  variability criterion."
- `z>6` QSOs: "Twelve anomaly-selected spectra are DESI-pipeline `z>6` QSO
  candidates" — not "discoveries."
- Latent photo-z: "A supervised regressor on the historical latent vectors
  achieved `sigma_NMAD = 0.0279` on its recorded split" — never called
  unsupervised photo-z, and `lat_067` is reported only as "the largest
  feature importance in the recorded regressor," never a "neuron."

## 3. Section-by-section skeleton (ApJS style)

| Section | Content |
|---|---|
| Introduction | Research question (§1); why the original manuscript could not be revived (provenance/generation conflation, per the inventory's "Data generations that were being conflated"); why this paper is a clean rerun, not a restoration. |
| Data | DESI DR1 `iron`; public-ID-first contract (zcatalog SHA, locator inventory, group-targetids export); the public-ID-first filter rule and its audit-log honesty contract (per-group `kept`/`surplus_dropped`/`zcat_missing_from_coadd` line, fail-closed on >1% missing coadds or 0 zcatalog IDs for a group). |
| Method | Archived BigAE (`best_model_47k.pt`, 496→512→256→128, SHA-256-bound); sealed two-stage PPS calibration and its stability gate; scoring definition; explicit statement that this is a fresh scan with a sealed contract, not a reproduction of either historical generation. |
| Validation | Per-class injection-recovery with exact model+substrate named (retiring the historical "0% false positive / 10-1,377x enrichment" summary per the claim table); held-out reproduction; honest limitations including the historical DESI NNLS-proxy study's 33.4% overall completeness, reported as a substrate-specific prior result, not the new run's own number unless independently re-measured. |
| Candidate catalog + characterization | New-generation filtered slice (§2b) with its manifest: schema, selection code, row count, hashes, source-parent binding — this is inventory closure gate 3 applied to the new generation. |
| Taxonomy | Rebuilt families from the new-generation unmatched subset (§2c); historical 10-family/76-AGN/27-post-starburst breakdown appears only as a labeled historical comparison. |
| Notable objects | Inclusion criterion: named TARGETID + independently checked photometry/redshift (inventory gate 6). No object is promoted to "notable" on selection-pipeline output alone — this is the gate that retired the historical `z=5.65`/`W2=5.5 mag` headline object. |
| Comparison to historical generations | `compare-generations` tool output against the 195,829-row original and 249,905-row enhanced labels — comparison-only framing, explicitly never reconciliation, per the RUNBOOK and inventory language. |
| Data availability | Current P3 r17 integrated as the supporting public-ID/provenance release (per the reset doc's "integrated-P3 role" decision); Zenodo/HF plan for the new-generation catalog — **PLACEHOLDER** pending scan completion. |
| Conclusions | Restate what survived validation vs. what is retired/deferred; explicit "not in this paper" list matching §7. |

## 4. Claim-language contract

No planned headline claim may exceed the wording below until new evidence
upgrades it. Historical rows are lifted verbatim from the inventory's "Allowed
wording now" column. New-generation rows are PLACEHOLDER by construction —
they do not have allowed wording yet because they do not have numbers yet.

| Planned claim | Allowed wording now | Source |
|---|---|---|
| Historical enhanced catalog (22,504,897 rows, 128 latent dims) | "A completed historical enhanced run reports 22,504,897 rows and 128 latent features; restoration/reproduction is pending." | Inventory claim table |
| Historical frozen 195,829 `S>5` catalog | "The frozen original release contains 195,829 reconstruction-outlier candidates." Never merged with the 249,905 enhanced count. | Inventory claim table |
| Historical enhanced 249,905 `S>5` count | Do not headline or compare until the parent run is restored and the score definition is reconciled. | Inventory claim table |
| Historical 2,145-row filtered slice | "A historical filtered candidate slice contains 2,145 rows under the recorded score/SNR rule." | Inventory claim table |
| Historical 1,127 unmatched objects | "1,127 candidates are unmatched in the stated SIMBAD/NED cone searches." | Inventory claim table |
| Historical taxonomy (10 families, 76 AGN, 27 post-starburst) | "The pipeline groups the 1,127 candidates into 10 interpretable candidate families, including 76 IR-bright AGN candidates and 27 post-starburst candidates." | Inventory claim table |
| Historical 0% false-positive / 10-1,377x enrichment | Retired. Report per-class recovery and false-positive definitions directly, with the exact model and substrate named. | Inventory claim table |
| Historical `sigma(f_NL)` 9.5% improvement | "No defensible `f_NL` improvement is demonstrated." Removed from the anomaly headline. **`f_NL` stays OUT of this paper** unless a proper selection-function/survey-window analysis produces a nonzero, defensible result (closure gate 7). | Inventory claim table + closure gate 7 |
| Historical latent photo-z `sigma_NMAD = 0.028` | "A supervised regressor on the historical latent vectors achieved `sigma_NMAD = 0.0279` on its recorded split." Never called unsupervised photo-z. | Inventory claim table |
| `lat_067` "redshift neuron" | "`lat_067` had the largest feature importance in the recorded regressor." | Inventory claim table |
| Historical 16 IR-variable anomalies | "Sixteen of 283 examined candidates met the recorded NEOWISE variability criterion." | Inventory claim table |
| Historical `z=5.65` QSO, `W2=5.5 mag` | Retired until a named TARGETID and independently checked photometry/redshift support it. | Inventory claim table |
| Historical 12 `z>6` QSO candidates | "Twelve anomaly-selected spectra are DESI-pipeline `z>6` QSO candidates." Not "discoveries." | Inventory claim table |
| Historical exact per-object score reproducibility | State the successful bounded pipeline validation and the exact per-object reproduction failure together — never one without the other. | Inventory claim table |
| New-generation candidate count | **PLACEHOLDER.** No wording until `summarize-after-dedup` runs on the completed scan; never described as matching or targeting the historical 2,145. | AUG-011 status (queue item 3) |
| New-generation SIMBAD/NED-unmatched count and taxonomy | **PLACEHOLDER.** No wording until the new cross-match/taxonomy rerun (§2c) completes. | AUG-011 status (queue item 3) |

## 5. Dependency gates

What must exist, and where the tooling lives, before each section can be
drafted for real (not skeleton):

| Section | Gate | RUNBOOK / tooling path |
|---|---|---|
| Data | Full scan completion + receipt verification | `pipelines/p1_highz_tracers/clean_rerun/RUNBOOK.md` step 10 (full scan), step 12 (`clean_rerun_contract.py verify-receipts`) |
| Method | Sealed contract + calibration (already sealed, commit `568a33bf`) | `pipelines/p1_highz_tracers/clean_rerun_contract.py`; `clean_rerun_contract.md` |
| Validation | Per-class injection suite, exact model+substrate named (closure gate 5) | `pipelines/p1_highz_tracers/scripts/injection_recovery_test.py`, re-run against the new-generation slice, not the historical summary |
| Candidate catalog + characterization | `summarize-after-dedup` on the completed scan + new-slice threshold decision (§2b) | `clean_rerun_contract.py summarize-after-dedup` (RUNBOOK step 13) |
| Taxonomy | New-slice cross-match run + taxonomy rerun | `pipelines/p1_highz_tracers/scripts/silver_crossmatch.py` / `step2_crossmatch_full.py` analog; taxonomy clustering analog to `projects/h200_scripts/anomaly_taxonomy.py`, all re-run against §2b's output |
| Notable objects | Independent validation of any named high-redshift/physical candidate (closure gate 6) | Manual/independent photometry+redshift check per object; no automated tool substitutes for this gate |
| Comparison to historical generations | `compare-generations` on the new post-dedup summary | `clean_rerun_contract.py compare-generations` (RUNBOOK step 14) |
| Data availability | P3 r17 already exists (`pipelines/p3_anomaly_engine/FINAL_PACKAGE_RECEIPT_v3.2.0-r17_2026-08-03.md`); new-generation Zenodo/HF release plan | **PLACEHOLDER** — no new-generation archival deposit exists yet |
| Conclusions | All of the above | — |
| Any `f_NL` content anywhere | Selection-function + survey-window analysis with a nonzero, defensible result (closure gate 7) | Not started; content stays out of the paper until this gate closes |

## 6. Venue analysis

**ApJS.** ApJS explicitly exists for catalog and methods papers with large
public data products — this manuscript's primary deliverable (a scored
catalog with a sealed provenance chain, a filtered candidate slice, and a
rebuilt taxonomy) is exactly that genre. The project already has ApJS-format
precedent: the deprecated `paper3_draft.tex` and the current P3 supporting
release were both built to ApJS conventions (`APJS_PORTAL_SUBMISSION_KIT_*`,
`FINAL_PACKAGE_RECEIPT_*`), so the tooling and formatting habits transfer
directly. ApJS's page-length tolerance also suits a paper that must honestly
carry a long provenance/audit-trail section rather than compress it away.

**AJ.** AJ accepts catalog papers and instrument/survey-methodology results,
and the program already uses it for P5 as a standalone companion — but AJ
leans toward tighter, more observationally-anchored results with a clearer
single physical question, which fits P5's chirality-environment null better
than a methods-plus-catalog rebuild carrying its own provenance-recovery
narrative. Using AJ here would mean compressing the audit-trail material this
paper exists to make legible, which cuts against the paper's actual purpose.

**MNRAS.** MNRAS is a credible general venue for anomaly-detection catalog
papers and has broader international reach than the AAS journals, but it
lacks the specific "large public data product" institutional fit that ApJS
has, and the DESI/US-survey culture this program otherwise sits in (P3, P4)
already runs through AAS-family venues, so an MNRAS submission would be an
outlier in the portfolio without a corresponding scientific reason to leave
that ecosystem.

**Recommendation: ApJS.** It is the closest institutional fit for a
catalog-plus-method paper with a large public data product, it matches the
existing tooling/precedent already in the repo, and it keeps the anomaly
flagship in the same venue family as its own supporting data release (current
P3), which the reset doc already treats as integrated.

## 7. Honest-boundaries section — what this paper is NOT

- **Not a discovery paper.** No candidate — including the `z>6` QSO list or
  any NEOWISE-variable object — is reported as a confirmed discovery without
  independent validation (closure gate 6). Selection-pipeline output alone
  never promotes an object to "notable."
- **Not an anomaly-rate cosmology paper.** No population-level cosmological
  inference is drawn from the anomaly rate or candidate counts; the historical
  0% false-positive / 10-1,377x enrichment framing is retired outright, per
  the claim table.
- **`f_NL` stays OUT of this paper.** Per closure gate 7, no `f_NL` content —
  headline, forecast, or aside — appears anywhere in this manuscript unless a
  proper selection-function and survey-window analysis independently produces
  a nonzero, defensible result. The historical 9.5% `sigma(f_NL)` improvement
  claim is not a result and is not restated even as context.
- **Historical generations are comparison sets only, never reconciliation
  targets.** The 195,829-row frozen release and the 249,905-row enhanced
  count are formally unreconciled (inventory, "Restoration gate result"); the
  new AUG-011 generation is never tuned, truncated, or thresholded to match
  either historical count, and `compare-generations` output is presented as a
  comparison, never as validation of the new run or reconciliation of the old
  ones.
- **No unsupervised claims for supervised results.** The latent-space photo-z
  result is a supervised regressor trained on historical latent vectors, not
  an unsupervised or emergent capability, and `lat_067` is a feature-importance
  ranking, not a discovered "neuron."
- **No exact per-object score reproducibility claim for the historical
  generation.** Where the historical pipeline's bounded validation succeeded
  and its absolute per-object normalization failed, both facts are stated
  together, per the claim table — never the success alone.

## Status

This is architecture, not a drafted manuscript. Drafting begins section by
section as each row in §5 closes; §3-§4 are the binding skeleton and
claim-language contract for whoever (agent or Houston) writes prose into it.
