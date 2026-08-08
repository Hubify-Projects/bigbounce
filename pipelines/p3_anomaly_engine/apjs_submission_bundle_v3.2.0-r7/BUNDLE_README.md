# P3 ApJS submission bundle v3.2.0-r7

This directory is the definitive checksum-bound submission unit for the P3
catalog manuscript.  It binds, without relabeling, four frozen products:

1. `primary_release/`: the 181-row, 43-column primary Parquet release v3.2.0-r2.
   Its authoritative contract retains all 181 coordinate associations while
   distinguishing 170 `coordinate_consistent_le_0p1arcsec` core rows from 11
   `positional_match_gt_0p1_le_1arcsec` lower-confidence rows.  Neither tier is
   an object-identity proof or a purity estimate.
2. `warned_auxiliary/`: the 2,267-row warning-bearing global-primary auxiliary
   product v3.2.0-r5.  It is secondary and is not part of the primary catalog.
3. `aas_machine_readable_table/`: the AAS v3.2.0-r4 `tab3.tsv`, an exact typed
   serialization of the 181 x 43 primary Parquet table, plus its dictionary,
   manifest, and builder.  Its AAS digital-asset DOI is pending and is not
   claimed here.
4. `science_controls/` and `coordinate_lineage/`: the r6 association controls,
   original-member sensitivity, and SHA-bound code/data evidence showing that
   historical DESI anomaly `ra`/`dec` were copied from coadd FIBERMAP
   `TARGET_RA`/`TARGET_DEC` before cluster means were computed.  This recovers
   coordinate-field lineage, not the unavailable production object-to-spectrum
   mapping or anomaly-score preprocessing.

`BUNDLE_MANIFEST.json` records the role, source path, byte size, and SHA-256 of
every payload. `SHA256SUMS` additionally binds the manifest and this README.
Run `../scripts/validate_p3_apjs_r7_submission_bundle.py` from any directory to
validate the complete contract.
