# full_tension Science Freeze Confirmation

**Date:** 2026-03-11 17:28 UTC
**Updated:** 2026-03-11 18:00 UTC (CORRECTED — off-by-one column mapping bug fixed)
**Status:** FROZEN — ALL GATES PASS (re-verified with correct column mapping)

---

## Freeze Summary

| Field | Value |
|-------|-------|
| **Dataset** | full_tension (Planck + BAO + SN + H0 + S8) |
| **Model** | LCDM + Delta_Neff |
| **Chains** | 6 |
| **Total accepted samples** | 175,545 |
| **Runtime** | ~15 hours (02:00 - 17:28 UTC, 2026-03-11) |
| **Pod** | `83ubwlcdk0gat2` (CPU5, 32 vCPU, EUR-IS-1) |
| **Network Volume** | `a9d3xb63bv` (bigbounce-paper1-canonical, 150 GB) |
| **Cobaya** | 3.6.1 |
| **CAMB** | 1.6.5 |

## Convergence Gates — 9/9 PASS

| Gate | Metric | Value | Target | Status |
|------|--------|-------|--------|--------|
| 1 | R-1 (H0) | 0.000629 | < 0.01 | **PASS** |
| 2 | R-1 (delta_neff) | 0.000517 | < 0.01 | **PASS** |
| 3 | R-1 (tau) | 0.000511 | < 0.02 | **PASS** |
| 4 | ESS (H0) | 5,513 | > 2,000 | **PASS** |
| 5 | ESS (delta_neff) | 4,832 | > 2,000 | **PASS** |
| 6 | ESS (tau) | 5,475 | > 1,000 | **PASS** |
| 7 | Drift (H0) | 0.051σ | < 0.1σ | **PASS** |
| 8 | Drift (delta_neff) | 0.069σ | < 0.1σ | **PASS** |
| 9 | Drift (tau) | 0.073σ | < 0.1σ | **PASS** |

GetDist Gelman-Rubin (worst R-1): 0.004470 — **PASS**

## Parameter Values (CORRECTED — full_tension anchor result)

**NOTE:** Original values were wrong due to off-by-one column mapping bug.
See `research/final_paper_prep/full_tension_parameter_mapping_audit.md` for full details.

| Parameter | Mean | Std | Unit |
|-----------|------|-----|------|
| H0 | 67.68 | 1.06 | km/s/Mpc |
| delta_neff | -0.019 | 0.169 | dimensionless |
| tau | 0.054 | 0.007 | dimensionless |
| sigma8 | 0.803 | 0.008 | dimensionless |
| omegam | 0.308 | 0.005 | dimensionless |
| ns | 0.965 | 0.006 | dimensionless |
| S8 | 0.814 | 0.008 | dimensionless |
| age | 13.82 | 0.17 | Gyr |

## Frozen Artifact Pack

| Location | Path |
|----------|------|
| **Network volume (primary)** | `/workspace/bigbounce/frozen/full_tension_20260311_1728/` |
| **Snapshot tarball (NV)** | `/workspace/bigbounce/snapshots/frozen_full_tension_20260311_1728.tar.gz` (26 MB) |
| **Local copy** | `reproducibility/cosmology/frozen/full_tension_20260311_1728/` |

### Pack Contents (71 files, 158.5 MB)

- `chains/` — 6 chain directories with all Cobaya output files
- `covmats/` — 4 warm-start covariance matrices
- `configs/` — config generator + seed file
- `diagnostics/` — convergence summary, parameter summary, freeze diagnostics (JSON)
- `plots/` — triangle plot, 1D posteriors, per-chain comparison (PNG + PDF)
- `tables/` — parameter summary table (Markdown)
- `MANIFEST.md` — complete metadata and file inventory
- `SHA256SUMS.txt` — checksums for all 69 data files

### Integrity Verification

- **69/69 files** checksum-verified between network volume and local copy
- Snapshot tarball SHA256: `0225e4876b448dd2bc6516bcd094a409dd13148c8db7a83864957fe97a379bb6`

## Backup Status

| Layer | Status |
|-------|--------|
| Network volume (survives pod termination) | Frozen pack + snapshot tarball present |
| On-volume hourly backups | 17 backups from 02:09-17:00 UTC |
| Local machine copy | Synced and checksum-verified |

## Next Steps

1. Resume `planck_bao_sn` chains (Phase 2)
2. Continue running until planck_bao_sn reaches convergence
3. Then resume `planck_only` + `planck_bao` (Phase 3)
4. Full_tension result is the anchor — do not modify
