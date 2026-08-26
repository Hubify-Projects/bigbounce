# Anomaly flagship enrichment preflight — 2026-08-26

## Verified inputs

- Selected sample: 3,810 rows at `anomaly_score >= 8.0`, bound to the completed AUG-011 contract and all 36,634 shard receipts.
- Archived BigAE checkpoint: present locally and SHA-256 verified against the sealed contract (`f5266ba4…63885f07`).
- Local free space: 161 GiB at preflight. The enrichment implementation deletes each coadd after scoring and writes resumable per-group outputs.
- Required DESI DR1 `iron` zcatalog: public, byte-addressable, and 22,371,272,640 bytes; it is not currently staged locally.

## Bounded downstream scope

The selected rows span **3,128 unique `(survey, program, healpix)` coadd groups**. Enrichment must re-fetch and run the contract-bound inference once per group, retain only the selected targets, and fail closed if its raw MSE does not reproduce the scan's stored `mean_mse` for every output row.

This is not a rescan of 36,634 groups and does not change the selected sample. It is the required validation bridge that supplies coordinates, per-band SNR, residual diagnostics, and 128 latent features for cross-match and taxonomy.

## Execution decision

Do not start a paid RunPod pod yet. First stage and checksum the public zcatalog to a non-temporary cache, then run the enrichment script with its checkpoint/audit-log contract. A local run is technically possible but may be network- and CPU-bound over 3,128 groups. If local throughput is unsuitable, the exact same checkpointed command can be moved to a bounded RunPod volume; that is the first downstream compute action that may require credits.

## Completion evidence

The gate closes only when the enrichment manifest binds the selected-sample SHA, contract SHA, zcatalog SHA, every completed group, and a zero-skipped final merge. Cross-match, taxonomy, named-object validation, public archival release, and manuscript drafting remain separate gates.

