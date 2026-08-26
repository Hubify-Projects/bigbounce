# Anomaly flagship enrichment preflight — 2026-08-26

## Verified inputs

- Selected sample: 3,810 rows at `anomaly_score >= 8.0`, bound to the completed AUG-011 contract and all 36,634 shard receipts.
- Archived BigAE checkpoint: present locally and SHA-256 verified against the sealed contract (`f5266ba4…63885f07`).
- Local free space: 161 GiB at preflight. The enrichment implementation deletes each coadd after scoring and writes resumable per-group outputs.
- Required DESI DR1 `iron` zcatalog: public, byte-addressable, and 22,371,272,640 bytes. It was staged on 2026-08-26 in the persistent local dataset cache and its SHA-256 exactly matches the sealed contract: `2d95ad99361039b556c402b49e0e7c84df5f00106dc5731d44476a58b128b49b`.

## Bounded downstream scope

The selected rows span **3,128 unique `(survey, program, healpix)` coadd groups**. Enrichment must re-fetch and run the contract-bound inference once per group, retain only the selected targets, and fail closed if its raw MSE does not reproduce the scan's stored `mean_mse` for every output row.

This is not a rescan of 36,634 groups and does not change the selected sample. It is the required validation bridge that supplies coordinates, per-band SNR, residual diagnostics, and 128 latent features for cross-match and taxonomy.

## Execution decision

Do not start a paid RunPod pod yet. The public zcatalog has now been staged and checksum-verified in a non-temporary cache. Run the enrichment script with its checkpoint/audit-log contract. A local run is technically possible but may be network- and CPU-bound over 3,128 groups. If local throughput is unsuitable, the exact same checkpointed command can be moved to a bounded RunPod volume; that is the first downstream compute action that may require credits.

## Local transport observation — 2026-08-26

The first local enrichment incarnation checkpointed 57 groups, then hung in the archived downloader's TLS read for a 214,104,960-byte coadd. The archived inference/model source remains untouched and checksum-bound. Commit `9d35c039` replaced only the enrichment wrapper's transport with an atomic, 120-second socket-timeout downloader; its focused phase-3 tests and all manifest validation pass.

The official DESI endpoint delivered a sampled 1 MiB range at roughly **124 KB/s** from this machine. At that observed rate, serial local transfer is not a viable completion route for 3,128 groups. The restarted run remains checkpointed and safe, but a bounded GPU/CPU host with materially better archive throughput (or an approved official mirror) is now the practical execution gate. RunPod inventory currently shows no active pods; no new paid compute has been started.

## Portable partial checkpoint — 2026-08-26

The first 57 completed group shards, their checkpoint, audit log, and a SHA-256-bound resume manifest are preserved in the existing private dataset archive at `phase3/2026-08-26/partial-enrichment-s8/`. The archive holds 60 files: 57 Parquet shards plus `checkpoint.json`, `audit.jsonl`, and `partial_enrichment_resume_manifest.json`. It is explicitly marked partial and is not a candidate catalogue or public release. A faster host must restore this bundle alongside the immutable S8 sample/manifest, exact contract/model, and checksum-verified zcatalog, then rerun the identical enrichment command.

## Completion evidence

The gate closes only when the enrichment manifest binds the selected-sample SHA, contract SHA, zcatalog SHA, every completed group, and a zero-skipped final merge. Cross-match, taxonomy, named-object validation, public archival release, and manuscript drafting remain separate gates.
