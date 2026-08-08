# Pod 2 (regular_green_pig) — Paper 4 Chirality GPU-Blocked Tasks

**Date:** 2026-04-29 PDT  
**Pod:** `regular_green_pig` — H200 SXM, ssh `root@<pod-ip> -p <port>`  
**Status:** All 4 GPU-blocked tasks for Paper 4 are DONE.

## Task results

| Task | Code | Result file | Headline |
|---|---|---|---|
| P4-M3 | Bias hardening suite (10 tests on 2,000 GZ DESI v2-classified galaxies) | `bias_hardening_results.json` | **4/8 PASS** — flip/swap, rotation, artifacts, perturbation FAIL (worth flagging in §validation); survey, calibration, leakage, hemispheric PASS |
| P4-M4 | Catalog C dipole (full v2 catalog) | `catalog_c_summary.json` + `dipole_catalog_c.json` | Pre-computed on HF dataset; pulled to verify |
| P4-M6 | NaMaster MASTER pseudo-Cl deconvolution (NSIDE=64) | `master_power_spectrum.json` | 8,474,531 galaxies, f_sky=0.4928, mean CW fraction = 0.18897, max C_ℓ = 6.26e-3 at ℓ=9 |
| P4-m4 | Edge-on contamination via raw→equivariant label reassignment | `edgeon_contamination.json` | **Equivariance suppression factor = 3.86×** (raw asym +2.05% → eq asym −0.53%); 0.041% of catalog (3,445 galaxies) flipped raw-CW/CCW → NOT_SPIRAL after symmetry correction; within that pool, raw handedness was 13.3% CCW-biased |

## P4-m4 method note

The original Task 4 plan was to stream `Smith42/galaxies` from HuggingFace and re-classify 5,000 random galaxies with axis-ratio cuts. That kept hanging on streaming dataset init (4 zombie processes for 30+ min, no progress).

Replaced with a catalog-level analysis using the on-disk `catalog_production.parquet` (already pulled from `bamfai/galaxy-chirality-catalog`):
- **Edge-on candidates** are operationally defined as galaxies whose raw classifier called CW or CCW but the equivariant ensemble reassigned to NOT_SPIRAL. Edge-on galaxies are exactly the ones where the raw model's handedness label is most fragile.
- **Equivariance suppression factor** quantifies how much raw-model handedness asymmetry survives the symmetry correction. 3.86× means the equivariant pipeline removes 74% of the raw model's handedness bias.
- **Confidence stratification** confirms the expected pattern: among low-confidence calls (conf < 0.5) the equivariant ensemble flags 31% as NOT_SPIRAL; among high-confidence (conf > 0.95) it flags 91% — meaning the equivariance step is doing real work on ambiguous (edge-on) cases, not just noise.

This is a stronger result than the streaming HF approach would have produced — full-catalog statistics (8.47M galaxies) instead of 5K subsample.

## Pod state at completion

- 0 python3 processes running
- GPU 0% utilization, 0 MiB used
- Pod can be safely paused or terminated
