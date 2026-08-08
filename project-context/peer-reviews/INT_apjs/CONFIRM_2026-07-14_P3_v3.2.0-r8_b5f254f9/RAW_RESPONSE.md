VERDICT: ACCEPT

EXACT ARTIFACT

Commit: `d155eb27488b271be12942b1a1be8b3c39dd24f4`  
Source SHA-256: `2b9a5fd356e49ae7a9939cbf8e9197379bef71b1f66a0e364e0de41ae416d10b`  
PDF SHA-256: `b5f254f92b10bda43b687f07c5f58b828a6f7dc70d98c08f9e9b609edbba08b0`  
Page count: 16  
Visual inspection: YES—all 16 exact-PDF renders individually inspected; no clipping, overlap, gutter crossing, or illegibility affecting the three checks.

CLOSURE MATRIX

| Check | Result | Exact evidence |
|---|---|---|
| Packaging | PASS | Frozen Git tree contains 41 bundle files: 38 manifest payloads plus `BUNDLE_MANIFEST.json`, `BUNDLE_README.md`, and `SHA256SUMS`. Direct Git-object validation checked all 38 payloads against manifest path, size, and SHA-256 with zero failures. Newly tracked copies: `coordinate_lineage/desi_dr1_anomalies.parquet` — 10,514,503 bytes, `0a36b8d6dfb8086c2c417885c99689d7a75b416dad1b030db56477baf103ec65`; `primary_release/desi_dr1_science_anomaly_candidates_v3.2.0-r2.parquet` — 58,038 bytes, `25f06752e0f1e9c0ddcde32e74fc0a82e8c2518a8fb24bf910c21e10ce988b03`; `warned_auxiliary/desi_dr1_warned_global_primary_aux_v3.2.0-r5.parquet` — 352,155 bytes, `e370f0ae6ec3f4dc3e24b443e2f9ee53a35b105341ef838f15067b6faea1e57c`. Manifest hash is `e59710a1c4f88fc816257d1441ae3eb69d954828c180a8541a1aa8f1c855007a`. Validator emitted `status: PASS`; clean-tree receipt records 41/41 validation PASS. |
| 0.1-arcsec provenance | PASS | Source lines 291–303 state that the 1″ radius was fixed before inspecting the quality cohort, retains all 181 associations, and that the 0.1″ boundary was “introduced post hoc as a descriptive quality tier,” is “not a predeclared selection cut,” and does not alter catalog membership. The statement is legible on rendered page 4. |
| 181=170+11 | PASS | Source lines 48–54 and 291–303 explicitly preserve 181 total associations partitioned into 170 at or below 0.1″ and 11 between 0.1″ and 1″. The title, abstract, Section 3.4, release description, and conclusion agree. Validator output independently reports `primary_rows: 181`, `core_rows: 170`, and `lower_confidence_rows: 11`. |

IN-SCOPE BLOCKERS: NONE

DUPLICATE/OUT-OF-SCOPE NOTES

- The previously noted page-5 float flow and substantial whitespace on pages 13–15 persist but are presentation-only, legible, and non-blocking.
- The validator’s separate temporary-directory wrapper self-check was sandbox-blocked after the primary validator emitted PASS; this is environment-only. The exact frozen Git-object audit independently verified all 38/38 manifest payloads and 41/41 committed bundle files.