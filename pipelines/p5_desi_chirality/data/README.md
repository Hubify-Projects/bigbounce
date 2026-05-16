# P5 data directory

All data files in this directory are **derived caches** of external
catalogs. They are .gitignored. Recreate them by running:

```bash
python ../scripts/01_fetch_p4_catalog.py
python ../scripts/02_fetch_desi_dr1.py
```

| File | Source | Size | Notes |
|------|--------|------|-------|
| `p4_chirality.parquet` | HF `bamfai/galaxy-chirality-catalog@paper4-v1.0.90` / `catalog_production.parquet` | ~600 MB | 8,474,531 rows. Read-only. Do not edit. |
| `desi_zall.parquet` | DESI DR1 `zall-pix-iron.fits` converted to parquet | ~2-3 GB | ~22.5M rows. Cosmetic columns dropped during conversion (see `02_fetch_desi_dr1.py`). |
| `desi_lss/` | DESI DR1 LSS VAC (BGS/LRG/ELG/QSO) | TBD | One sub-dir per target class. |
| `desi_env/` | Environmental attributes (filament/void/density) | TBD | **Currently empty.** Blocker logged in `../reports/00_audit.md`. |

## Provenance

Every fetch script writes a `*_provenance.json` sidecar with: source URL,
SHA-256, fetch timestamp, expected vs observed row count. Do not delete
the sidecars.
