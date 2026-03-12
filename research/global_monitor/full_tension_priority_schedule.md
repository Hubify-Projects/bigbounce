# Full-Tension Priority Schedule — Decision Memo

**Date:** 2026-03-11 02:30 UTC
**Decision:** SWITCH TO PRIORITY-FIRST SCHEDULE — EXECUTED

---

## Problem

24 chains (4 datasets × 6 chains) running on 32 vCPUs caused severe oversubscription:
- Load average: **116** on 32 cores (3.6x oversubscribed)
- OMP_NUM_THREADS=5 × 24 chains = 120 requested threads on 32 cores
- Each chain effectively got ~1.3 vCPUs despite requesting 5
- Full_tension throughput: **1,925 accepted samples/hr**

## Decision

Stop all non-full_tension chains. Focus all 32 vCPUs on 6 full_tension chains.

## Throughput Comparison

### Scenario A: 24 chains across 4 datasets (PREVIOUS)

| Dataset | Samples/hr | Per-chain/hr | Notes |
|---------|-----------|-------------|-------|
| full_tension | 1,925 | 321 | Anchor result |
| planck_bao_sn | 1,017 | 170 | Lower priority |
| planck_only | 933 | 156 | Lower priority |
| planck_bao | 907 | 151 | Lower priority |
| **Total** | **4,782** | **199 avg** | 3.6x CPU oversubscribed |

### Scenario B: 6 full_tension chains only (CURRENT)

| Dataset | Samples/hr | Per-chain/hr | Notes |
|---------|-----------|-------------|-------|
| full_tension | **14,940** | **2,490** | 5 real OMP threads per chain |
| others | 0 (paused) | — | Preserved on disk |

**Speedup for full_tension: 7.8x** (14,940 vs 1,925 samples/hr)
**Per-chain speedup: 7.8x** (2,490 vs 321 accepted/hr)
**Load average: 41** (down from 116) — healthy for 32 cores

### Note on Chain 06

Chain 06 shows ~5-7x higher throughput than chains 01-05. This is likely due to
Cobaya's drag sampler: with `oversample_power: 0.4`, the fast nuisance parameters
are oversampled relative to the slow cosmological parameters. Chain 06 may have
reached a state with very efficient fast-block proposals. The key science metric
(ESS for H0, ΔNeff) depends on slow-block acceptance rate, not total sample count.

## Optimal OMP_NUM_THREADS

With 6 chains on 32 vCPUs:
- OMP_NUM_THREADS=5: Uses 30/32 cores. Good utilization with 2 cores free for OS/backup.
- **This was already set at launch.** No change needed — the chains automatically benefit
  from reduced contention now that the other 18 chains are stopped.

## Time-to-Freeze Estimates

### Science freeze requirements for full_tension:
1. R̂-1 < 0.01 for H0
2. R̂-1 < 0.01 for ΔNeff
3. R̂-1 < 0.02 for τ
4. ESS > 2,000 for H0, ΔNeff
5. ESS > 1,000 for τ
6. No drift > 0.1σ
7. GetDist validation passes

### Scenario A (24 chains, as was)

| Milestone | Estimate |
|-----------|---------|
| 40,000 raw full_tension samples | ~21 hours |
| R-hat convergence to < 0.01 | 4-6 days |
| ESS > 2,000 for H0/ΔNeff | 4-6 days |
| **Full_tension science freeze** | **4-6 days** |

### Scenario B (6 focused chains, current)

| Milestone | Estimate |
|-----------|---------|
| 40,000 raw full_tension samples | **~3 hours** |
| R-hat convergence to < 0.01 | **2-3 days** |
| ESS > 2,000 for H0/ΔNeff | **2-3 days** |
| **Full_tension science freeze** | **2-3 days** |

**Time savings: ~2-3 days** for the anchor result.

## Preserved Chain Data

All paused chain outputs preserved on persistent network volume:

| Dataset | Samples at Pause | Status |
|---------|-----------------|--------|
| planck_bao_sn | 501 | Stopped, data preserved |
| planck_only | 447 | Stopped, data preserved |
| planck_bao | 454 | Stopped, data preserved |

These can be resumed later with `cobaya-run --resume` using their existing
checkpoints and learned covmats. No data is lost.

Pre-stop backup saved: `snapshots/chains_2026-03-11_0229.tar.gz` (608 KB)

## Active Chains

| Chain | PID | Dataset | Status |
|-------|-----|---------|--------|
| full_tension/chain_01 | 1393 | full_tension | **RUNNING** |
| full_tension/chain_02 | 1397 | full_tension | **RUNNING** |
| full_tension/chain_03 | 1401 | full_tension | **RUNNING** |
| full_tension/chain_04 | 1409 | full_tension | **RUNNING** |
| full_tension/chain_05 | 1417 | full_tension | **RUNNING** |
| full_tension/chain_06 | 1425 | full_tension | **RUNNING** |

## Paused Chains

| Dataset | Chains | PIDs | Samples | Resume Strategy |
|---------|--------|------|---------|----------------|
| planck_bao_sn | 01-06 | killed | 501 | `cobaya-run --resume` after full_tension freeze |
| planck_only | 01-06 | killed | 447 | `cobaya-run --resume` after planck_bao_sn |
| planck_bao | 01-06 | killed | 454 | `cobaya-run --resume` after planck_only |

## Phased Schedule

| Phase | Dataset | Chains | Start | Est. Duration |
|-------|---------|--------|-------|---------------|
| **1 (NOW)** | full_tension | 6 | Day 0 | 2-3 days to freeze |
| 2 | planck_bao_sn | 6 | After Phase 1 | 2-3 days |
| 3 | planck_only + planck_bao | 12 | After Phase 2 | 3-4 days |

Total time to all 4 datasets frozen: **7-10 days** (vs 10-15 days with parallel schedule).

## Scientific Cleanliness

This schedule is **more** scientifically clean than the parallel approach:
- No CPU contention artifacts (consistent per-sample timing)
- Better proposal learning (Cobaya can learn proposal covariance faster with consistent evaluation speed)
- Cleaner chain mixing (no OS scheduling jitter from oversubscription)
- Each dataset gets dedicated resources during its phase
