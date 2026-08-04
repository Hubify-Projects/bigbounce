# DESI clean-rerun contract

This is a scaffold for a **new** DESI DR1 BigAE generation. It deliberately
does not restore or silently replace either historical generation:

- `historical-original-17_651_065`: 195,829 `S>5` rows;
- `historical-enhanced-22_504_897`: 249,905 `S>5` rows, summary-only.

`clean_rerun_contract.py` fails closed unless all four run inputs are sealed:

1. a model whose SHA-256, byte size, and required 496→128 BigAE state-dict
   tensors are verified;
2. inference source whose SHA-256 and byte size are locked;
3. an input manifest with the DESI DR1 `iron` revision, immutable zcatalog
   checksum, `TARGETID`, and a HEALPix coadd locator/inventory checksum;
4. a calibration artifact whose held-out validation MSE mean/std and the
   training, validation, and fit-code hashes are sealed.

The script never downloads data or runs inference. The worker that writes a
scored Parquet shard must call `record-receipt`; this records row count, schema,
file SHA, calibration/contract hash, and an atomic resume checkpoint. `verify-
receipts` rechecks them. `summarize-after-dedup` streams receipts-backed shards
through SQLite, keeping the **last** occurrence in lexical shard then row order,
and only then calculates the threshold count.

Create a real input manifest from this shape (placeholder hashes are rejected):

```json
{
  "manifest_version": "desi-dr1-clean-rerun-input/v1",
  "source_revision": "iron",
  "catalog_url": "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/zall-pix-iron.fits",
  "catalog_checksum_url": "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/redux_iron_zcatalog_v1.sha256sum",
  "catalog_sha256": "<verified 64-hex digest>",
  "targetid_column": "TARGETID",
  "spectrum_locator": {
    "type": "desi_dr1_iron_healpix",
    "base_url": "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/healpix/",
    "algorithm": "resolve TARGETID in frozen zcatalog inventory, then fetch its coadd"
  },
  "locator_inventory_sha256": "<verified 64-hex digest>"
}
```

Use a calibration artifact with `status: "sealed"`, score definition
`mean_mse_over_per_spectrum_median_abs_flux_normalized_496_bins`, fit scope
`held_out_training_validation_split`, positive `mse_std`, and the three
required SHA-256 references. No absent, inferred, or historical normalization
is accepted.

Example contract build (no network or scan):

```sh
python3 pipelines/p1_highz_tracers/clean_rerun_contract.py build-contract \
  --model best_model_47k.pt \
  --inference-code pipelines/p1_highz_tracers/outputs/enhanced_18M/enhanced_18M_inference.py \
  --input-manifest /secure-run/input-manifest.json \
  --calibration /secure-run/calibration.json \
  --output /secure-run/run-contract.json
```

Run `compare-generations` only after a new post-dedup summary exists. Its output
is explicitly a comparison record, not reconciliation or validation of either
historical count.
