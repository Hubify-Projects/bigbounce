# Stage A — full-catalog e2e mirror-pair sweep (RUN SUMMARY)

**Executed:** 2026-07-11 → 2026-07-12 (UTC) per `project-context/P4_E2E_INJECTION_PLAN.md` Stage A.
**Runner:** `pipelines/p2_chirality/scripts/e2e_mirror_flip_fullrun.py` (commit `afd4f73b`).
**NEVER-FABRICATE:** every number below is computed from the per-galaxy records; nothing steered.

## Infrastructure

| Item | Value |
|---|---|
| Pod | RunPod `0hh3humgpacgz1` (bigbounce-p4-e2e-mirror), A100 80GB PCIe, community, $1.19/hr |
| Why A100 | 4090 + A6000 community capacity unavailable at deploy time; A100 was the plan's primary option |
| Wall time | 10.45 h (incl. one OOM stall + recovery) |
| Cost | ≈ **$12.44** (cap $20) |
| Throughput | ~330–365 gal/s steady (above the 300 abort floor) |
| Status at end | Pod **STOPPED** (not terminated); `/workspace` volume retained |

**Incident (fixed in-run):** at shard 14 the container cgroup (125 GB limit, host shows 1 TB)
OOM-killed the parent silently (DataLoader fork-CoW heap growth + prefetch backlog +
per-shard full-summary rebuilds). Fix: process self-recycles every 10 shards under a
supervisor loop (fresh heap, resumable), prefetch 4→2, summary rebuild every 10 shards.
Zero further OOM kills across 19 supervisor passes. Zero data lost (per-shard checkpoints).

## Sample

- Source: `Smith42/galaxies` — all **192 shards**, the exact production imaging source of
  `catalog_production.parquet` (`run_eq_dataloader.py`). **8,474,531 galaxies**, 2 forward
  passes each (original + horizontal mirror) = **16,949,062 inferences** through the actual
  ViT (`bamfai/galaxy-chirality-v2`, val_acc 0.9369), preprocessing identical to production
  (`Resize(224,224) → ToTensor → Normalize(ImageNet)`).

## Headline results (RAW mode, argmax single pass)

| Quantity | Value |
|---|---|
| n pairs (original argmax CW/CCW) | 3,322,550 |
| **T_raw** (P(mirror flips CW↔CCW)) | **0.2303 ± 0.0002** |
| a_img (correct-flip fraction, spiral→spiral pool, n=2,799,470) | 0.2733 |
| **g_img = 2·a_img − 1** | **−0.4534** (paper's GZ1-derived g = **+0.398**) |

Confidence strata (original raw confidence):

| bin | n | T_raw |
|---|---|---|
| [0.0, 0.7) | 371,606 | 0.2613 ± 0.0007 |
| [0.7, 0.9) | 472,444 | 0.2391 ± 0.0006 |
| [0.9, 0.99) | 808,068 | 0.2071 ± 0.0005 |
| [0.99, 1.0] | 1,670,432 | 0.2320 ± 0.0003 |

Sky strata (via dr8_id ↔ catalog_production coords): North (dec≥0) T=0.2178 (n=2,071,471);
South (dec<0) T=0.2510 (n=1,251,079).

Confusion behavior: P(CW→CW under mirror)=0.631, P(CCW→CCW)=0.593 — the raw classifier's
spiral-class calls at catalog scale are dominantly **flip-invariant**; the flip channels are
nearly parity-symmetric (CW→CCW 0.2251 vs CCW→CW 0.2356). Catalog CW fraction (raw argmax)
0.5078.

## EQ mode (production Z₂-TTA — what the paper's dipole pipeline actually uses)

- n = 3,201,201 EQ-spiral originals; **T_eq = 0.99974**; antisymmetry max deviation **0.0**.
- Confirms end-to-end through the real weights that the production equivariant pipeline
  registers a physical chirality inversion with probability ~1 **by construction**
  (the ~2.6×10⁻⁴ shortfall is argmax ties). Identical to the pilot's finding.

## Honest interpretation notes (for the integration owner — NOT integrated here)

1. **Pilot discrepancy explained by sampling.** The local pilot (T_raw=0.650, g_img=+0.358,
   n=2,500) drew from `mwalmsley/gz_desi` **streaming**, which (known 1-shard bug/behavior)
   sees only the first shard — a non-representative, apparently bright/high-quality-dominated
   subsample. The full production catalog is dominated by faint marginal spirals; even the
   conf≥0.99 stratum shows T_raw=0.232 (pilot's stream showed 0.710). The full-catalog
   numbers supersede the pilot.
2. **What g_img=−0.45 does and does not mean.** RAW-mode T measures the parity-odd
   information content of single-pass argmax calls. It does NOT directly dilute the paper's
   dipole signal because the production labels are EQ (Z₂-TTA), for which the mirror
   response is exactly antisymmetric (T_eq≈1, verified). The paper's g=0.398 is a
   human-ground-truth (GZ1) accuracy calibration — a different, complementary quantity.
   How these map into the sensitivity statement (A₅₀/A₉₅ → true-amplitude) is Stage B +
   paper-integration work.
3. The N/S T_raw difference (0.218 vs 0.251) is a real stratification in parity-odd
   information content across imaging hemispheres — candidate systematic for Stage B.

## Artifacts + backup (backup-3plus)

| Location | Contents |
|---|---|
| Local (this dir) | `e2e_transfer_function_full.json` (final, md5 `925649b752ebaa077b52f98e36241556`), `e2e_shards/` 192 parquets (716,430,770 bytes, byte-verified vs pod), `run.log`, `supervisor.log` |
| HF `bamfai/galaxy-chirality-catalog` | `e2e_mirror_pairs.parquet` (8,474,531 rows, zstd), `e2e_transfer_function_full.json`, `e2e_fullrun_interim_checkpoint.tar.gz` (mid-run) |
| Backblaze B2 | `bigbounce/p4_e2e/{e2e_mirror_pairs.parquet, e2e_transfer_function_full.json, run.log}` |
| Pod volume (stopped) | `/workspace/e2e/` complete copy |

Per-galaxy schema: `dr8_id, p_{cw,ccw,ns}_raw, p_{cw,ccw,ns}_raw_mirror, p_{cw,ccw,ns}_eq,
class_raw, class_raw_mirror, class_eq, class_eq_mirror, conf_raw, eq_antisym_dev`.
Stage B (hybrid image→field injection-recovery) consumes these precomputed flip labels.
