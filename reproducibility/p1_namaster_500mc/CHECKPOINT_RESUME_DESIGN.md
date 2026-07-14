# Exact-window battery checkpoint/resume design

Status: implemented 2026-07-14 after the original production processes had
exited. Production now runs one configuration per atomic shard, and completed
shards are skipped only after strict receipt validation.

## Required contract

1. One configuration per shard, selected with `--only-config NAME`.
2. Preserve the declared `N=500`, seeds 42--541, and exact bandpower-window
   operator. Resume logic must never silently reduce an ensemble.
3. Write each result to a same-directory temporary file, flush and `fsync`,
   then publish with `os.replace` so interruption cannot expose partial JSON.
4. Store configuration name, full configuration object, sample count, seed
   range, runtime, software versions, window-equivalence residual, result-file
   byte count, and SHA-256 in a small sidecar receipt.
5. On restart, skip a shard only after validating its JSON, receipt hash,
   configuration, exact `N`, and seed range. Invalid or incomplete shards are
   ignored and rerun at the same target path; atomic replacement prevents a
   partial JSON file from being treated as complete.
6. Merge only the exact expected configuration-name set; reject duplicates,
   omissions, mixed sample counts, mixed operators, or failed equivalence
   tolerances. Write the merged artifact atomically and record all child
   hashes.
7. Keep superseded effective-ell outputs untouched and explicitly labeled.

## Verification completed

- Atomic publication and receipt validation passed a temporary-file round trip.
- Both runners passed `N=1` CLI-routing smoke shards outside the repository;
  those diagnostics were removed and are not production evidence.
- The exact-window rotation/operator regression passed at maximum coupled-
  spectrum error `8.67e-19` and window-equivalence error `3.19e-16`.
- The merger fails closed while any of the exact nine `N=500` shards or their
  receipts are absent. Final child-hash verification and manuscript/manifest
  integration occur only after all shards publish.

This converts a multi-hour all-or-nothing pool into independently restartable
work without changing any numerical estimator or declared science count.
