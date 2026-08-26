# Anomaly flagship selected-sample decision — 2026-08-26

## Decision

The first new-generation characterization sample is the deterministic
post-dedup **`anomaly_score >= 8.0`** slice of the completed AUG-011 clean
rerun. It contains **3,810 TARGETIDs**. This is a characterization cohort,
not a discovery list and not a claim that every row is astrophysical.

## Evidence and rule

`build_flagship_sample.py --describe` re-verified all 36,634 shard receipts,
bound the completed summary to contract payload
`6699d09ff886f74dab6608bd70a70b73b7a34afabc436d365c69f16a95ac5edf`, and
replayed the prescribed last-row-wins deduplication over 28,425,963 raw rows.
The resulting universe has 27,547,223 unique TARGETIDs. The fixed candidate
ladder in the runbook yielded 52,188 at >=5, 27,180 at >=6, 3,810 at >=8, and
337 at >=10.

The >=8 rule was selected from that pre-listed ladder because it defines the
extreme 0.0138% tail while leaving a tractable, non-historical-count-tuned
cohort for external-catalog validation and taxonomy. It is deliberately
different from both the completed generation's >=5 summary convention and the
historical 2,145-row score/SNR slice. No quality filter was applied because
the AUG-011 shard schema has no SNR field; the later enrichment gate supplies
per-band SNR before any physical interpretation.

The >=10 subset (337 rows) is a nested priority-review tier only. It is not a
second catalog and does not justify discovery language.

## Materialized, bound artifact

The selection replay emitted a 3,810-row Parquet file with SHA-256
`00bf453e864a2fda93ef6d72cd351984c4b8f43975d9962b65d168901ee1b852` and a
manifest binding all 36,634 receipt hashes, the parent catalog, the contract,
and the completed summary. Both were uploaded to the authenticated **private**
rerun archive together with the bound summary on 2026-08-26. This is a backup
and provenance checkpoint, not a public data release or a citable deposit.

## Still required before manuscript claims

1. Enrich the selected rows with verified coordinates, per-band SNR, and
   latent features.
2. Run fail-closed SIMBAD/NED cross-matches and taxonomy on the enriched
   output.
3. Independently validate any named object before treating it as notable.
4. Assemble the ApJS manuscript and create a public immutable data release.

