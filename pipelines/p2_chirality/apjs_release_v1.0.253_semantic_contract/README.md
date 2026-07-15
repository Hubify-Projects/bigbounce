# P4 Catalog C semantic contract (Paper IV v1.0.253)

This bundle independently re-runs every declared row-level semantic gate over
the exact public Catalog C release. It does not rebuild the catalog and makes no
claim that the three softmax ranking scores are calibrated probabilities.

The bootstrap entrypoint avoids maintaining a second copy of the scientific
validator. It downloads the validator, its machine schema, and its imported
primary-null reproducer from immutable BigBounce Git commit
`5ec77d8b2f348f1b939627b8d24b20784ae93bee`, verifies all
three files byte-for-byte, downloads the complete v1.0.244 release inventory named by
the immutable provider receipt, verifies every file's byte count and SHA-256,
and invokes the pinned validator in `--validate-only` mode.

```bash
python -m pip install numpy pyarrow
python validate_p4_catalog_c_semantics_v1_0_253.py \
  --work-dir ./p4-semantic-audit \
  --receipt ./my-semantic-receipt.json
```

The download is approximately 405 MB. Validation streams 8,474,531 rows and
uses a temporary disk-backed SQLite primary-key table for the unique-object-ID
gate. Existing files are verified and reused; `--force-download` replaces them.

The gates cover non-null unique object IDs, ICRS coordinate ranges, allowed
labels, finite and bounded structural softmax scores, score simplex and maximum
consistency, deterministic argmax label semantics, derived spiral and primary
selection flags, all declared aggregate counts, quarantine reason codes, the
quarantine do-not-use invariant, and exact row-level equality between quarantine
IDs and primary rows marked `raw_flip_qc_unsafe=True`, including per-row HC-flag
agreement. `SEMANTIC_VALIDATION_RECEIPT.json` records the preceding full scan;
the strengthened row-equivalence gates require a fresh full scan before publication.

`SEMANTIC_CONTRACT.json` is the authoritative machine-readable binding. The
provider receipt is pinned at `e535b26247c892971963be6029435544cf29d19b` and
the release payload at `db11023306ab4eed1d7727670bd78e127b7af17a`.
