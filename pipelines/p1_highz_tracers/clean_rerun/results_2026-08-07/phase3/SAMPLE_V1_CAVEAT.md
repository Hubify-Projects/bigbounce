# SAMPLE-V1 (provenance under review: possible sky-fiber contamination — negative TARGETIDs)

Confirmed on landing (2026-09-03): of 3,810 rows in `flagship_sample_s8_enriched.parquet`,
**3,232 (84.8%)** have negative `targetid` values (range down to ~-8.26e8). In DESI
convention negative TARGETIDs are reserved for non-astrophysical fibers (sky fibers,
bad-fiber placeholders, etc.), so a majority-negative-TARGETID sample is a real
provenance flag, not noise.

Per coordinator instruction (2026-09-03): pod 8ofv5d4ynu7hku is **NOT** being stopped
pending contamination verification. All phase-3 artifacts below (flagship_sample_s8*,
flagship_sample_s8_enriched*, flagship_crossmatch_*, flagship_wise*, flagship_taxonomy*,
enrich_audit.jsonl, enrich_checkpoint.json) are landed and backed up as **SAMPLE-V1**
with this caveat attached. No ledger #8 paper-vs-release decision is recorded yet —
recovery-benchmark numbers below are reported as-is, pending the coordinator's
contamination verdict.
