# Paper-1 MCMC Clean Restart: Hardware Decision Memo

**Date:** 2026-03-11 (updated from initial 2026-03-10 planning)
**Project:** BigBounce Paper-1 — Cobaya MCMC verification run
**Status:** DECIDED AND DEPLOYED

---

## Final Decision: CPU5 Compute-Optimized

| Spec | Value |
|------|-------|
| **Type** | CPU5 Compute-Optimized |
| **vCPUs** | 32 |
| **RAM** | 64 GB spec (124 GB actual) |
| **Cost** | $1.12/hr ($26.88/day) |
| **Datacenter** | EUR-IS-1 (Iceland, Secure Cloud) |
| **Network Volume** | 150 GB attached at /workspace |
| **Pod ID** | `83ubwlcdk0gat2` |

## Why CPU5 Over GPU Pods

The Cobaya + CAMB + Planck likelihood workload is **CPU-bound**. GPU VRAM provides no benefit.

### Provisioning Experience (2026-03-11)

| Machine | Result |
|---------|--------|
| RTX A6000 (US-TX-3) | Not available |
| RTX 6000 Ada (US-TX-3) | Not available |
| L40S (US-TX-3, with NV) | Created but **never started** (3 attempts, 20+ min each) |
| L40S (US-TX-3, no NV) | Created but **never started** |
| RTX A6000 (secure, any DC) | Created but **never started** |
| **CPU5 (EUR-IS-1)** | **Started instantly** |

GPU pod infrastructure was unreliable across multiple datacenters. CPU pods started immediately.

### Comparison

| Factor | CPU5 ($1.12/hr) | RTX A6000 ($0.33/hr) | RTX 6000 Ada ($0.74/hr) |
|--------|-----------------|---------------------|------------------------|
| vCPUs | 32 (guaranteed) | 9-16 (varies) | 10-128 (varies widely) |
| GPU | None (not needed) | 48 GB (wasted) | 48 GB (wasted) |
| Availability | Instant | Limited/stuck | Limited/stuck |
| MCMC throughput | HIGH | LOW-MEDIUM | VARIABLE |

### Observed Performance

With 24 chains running (6 per dataset, OMP_NUM_THREADS=5):
- ~7,100 accepted samples/hour across all 24 chains
- Burn-in completed in <30 seconds (warm-start covmats)
- All 24 chains producing useful samples from step 1
- Projected: **full_tension science freeze in 5-8 days**

### Budget Impact

| Scenario | Daily cost | Days to freeze | Total cost |
|----------|-----------|---------------|------------|
| CPU5 (actual) | $26.88 | 8-12 est. | $215-322 |
| RTX A6000 (theoretical) | $7.92 | 15-25 est. | $119-198 |

CPU5 costs more per day but converges faster. Total cost comparable.
With $1,000 budget: 37 days runway — comfortable margin.

## Runner-Up

**RTX A6000** at $0.33-0.49/hr — cheaper per hour but:
- Only 9-16 vCPUs with current RunPod allocations
- GPU pods had infrastructure issues during provisioning (March 2026)
- Would be reconsidered if CPU5 availability drops

## Previous Planning (Superseded)

The initial planning from 2026-03-10 evaluated GPU options extensively.
Those plans are archived in `relaunch_plan.md` and `relaunch_budget_model.csv`.
The CPU-first approach was adopted based on the user's direction and confirmed
by the provisioning experience above.
