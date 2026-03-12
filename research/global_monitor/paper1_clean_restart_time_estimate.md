# Paper-1 Clean Restart — Time Estimate

**Date:** 2026-03-10
**Hardware:** RTX A6000 on-demand ($0.33/hr), ~10-16 vCPUs expected
**Warm-start:** Learned covmats from gpu_run_snapshot_20260305_0824

---

## Basis for Estimates

### Previous Run Performance (2026-03-04 to 2026-03-09)

The previous GPU run (RTX 6000 Ada, 128 vCPUs) achieved:
- **full_tension:** 63,531 samples in ~5 days = ~12,706 samples/day (28 chains → ~454/chain/day)
- **planck_only:** 25,345 samples in ~5 days = ~5,069 samples/day
- **planck_bao:** 25,246 samples in ~5 days = ~5,049 samples/day
- **planck_bao_sn:** 26,220 samples in ~5 days = ~5,244 samples/day
- Convergence state at shutdown: full_tension at 6/8 freeze gates, R̂-1(H0)=0.0036

### Adjustments for Clean Restart

1. **Fewer chains:** 4 per dataset (vs 7 before). Fewer chains = faster per-chain throughput but slower R-hat convergence (R-hat needs inter-chain comparison)
2. **Better covmats:** The 20260305 covmats have learned off-diagonal structure. Previous run started from diagonal covmats and had to learn them. Clean restart benefits from pre-learned proposals from step 1.
3. **Fewer vCPUs likely:** RTX A6000 probably gives ~10-16 vCPUs vs 128 on previous RTX 6000 Ada. This is the biggest slowdown factor.
4. **No chain1 drag:** Previous run had a lagging chain1 that hurt R-hat. 4 clean chains should converge more uniformly.

### vCPU Impact Model

With CAMB using OpenMP, each chain evaluation benefits from ~2-4 threads.
- 128 vCPUs / 28 chains = ~4.6 vCPUs per chain → fast CAMB evaluations (~1s each)
- 12 vCPUs / 16 chains = ~0.75 vCPUs per chain → severe contention → ~4-8s per evaluation
- 12 vCPUs / 4 chains = ~3 vCPUs per chain → reasonable (~1.5s per evaluation)

**Strategy:** Run datasets sequentially or in batches of 2, not all 16 chains simultaneously.
- Batch 1 (Days 0-5): full_tension (4 chains) — all CPU resources focused here
- Batch 2 (Days 3-7): Add planck_bao_sn (4 chains) — 8 chains total
- Batch 3 (Days 5+): Add remaining 2 datasets — 16 chains total

### Throughput Estimates (per chain, with warm covmat)

| Scenario | vCPUs/chain | Samples/chain/day | Notes |
|----------|-------------|-------------------|-------|
| 4 chains, 12 vCPUs | ~3 | ~800-1200 | Focus mode |
| 8 chains, 12 vCPUs | ~1.5 | ~400-700 | Split mode |
| 16 chains, 12 vCPUs | ~0.75 | ~200-400 | Contention |
| 4 chains, 16 vCPUs | ~4 | ~1000-1500 | Best case |

---

## Time to Key Milestones

### Convergence Requirements

For science freeze (all gates passed):
- Need R̂-1 < 0.01 for H0 and ΔNeff
- Need R̂-1 < 0.02 for τ
- Need ESS > 2000 for H0, ΔNeff; > 1000 for τ
- Need no drift > 0.1σ

With 4 chains, to get ESS > 2000 for the ensemble, each chain needs ~500+ effective samples.
Typical autocorrelation for CAMB MCMC: ESS ≈ N_samples / 10-20.
So each chain needs ~5,000-10,000 raw samples for ESS ≈ 500.

For 4 chains × 5,000 samples = 20,000 total samples minimum for initial convergence.
For 4 chains × 10,000 samples = 40,000 total for robust freeze-gate passing.

---

## Milestone Estimates

### 1. Time to Regain Lost Progress

Previous run had accumulated 236,622 total samples across all pods. The new run targets ~40,000 samples per dataset (4 chains × 10,000).

| | Optimistic | Realistic | Conservative |
|---|-----------|-----------|--------------|
| full_tension (focused, 4 chains) | 7 days | 10 days | 15 days |
| All 4 canonical datasets | 12 days | 18 days | 25 days |
| Rationale | High vCPU, fast CAMB | Moderate vCPU, batching | Low vCPU, contention |

### 2. Time to full_tension Near 6/8 Gates

Previous run reached 6/8 gates with ~62,080 cohort samples over 5 days (but with 7 chains on 128 vCPUs).

| | Optimistic | Realistic | Conservative |
|---|-----------|-----------|--------------|
| Days | 7 | 12 | 18 |
| Samples needed | ~20,000 | ~30,000 | ~40,000 |
| Rationale | Good covmat = fast mixing | Standard convergence | Slow mixing, fewer chains |

### 3. Time to full_tension Science Freeze (8/8 Gates)

| | Optimistic | Realistic | Conservative |
|---|-----------|-----------|--------------|
| Days | 10 | 15 | 22 |
| Total samples | ~30,000 | ~40,000 | ~60,000 |
| Daily cost | $7.92 | $7.92 | $7.92 |
| Total cost | $79 | $119 | $174 |

### 4. Time to All Canonical Datasets Frozen

| | Optimistic | Realistic | Conservative |
|---|-----------|-----------|--------------|
| Days | 14 | 22 | 35 |
| Total cost | $111 | $174 | $277 |

### 5. Time to ΛCDM Controls Sufficient

ΛCDM converges faster (1 fewer parameter). Can run concurrently with later canonical chains.

| | Optimistic | Realistic | Conservative |
|---|-----------|-----------|--------------|
| Days after launch | 12 | 18 | 28 |
| ΛCDM-specific days | 7 | 12 | 18 |

---

## Budget Summary

| Scenario | Total days | Pod cost | NV cost | Total |
|----------|-----------|----------|---------|-------|
| Optimistic (all done in 14 days) | 14 | $111 | $8 | $119 |
| Realistic (all done in 22 days) | 22 | $174 | $12 | $186 |
| Conservative (all done in 35 days) | 35 | $277 | $18 | $295 |

**With $1,000 budget, even the conservative estimate uses < 30% of funds.** This provides enormous safety margin for retries, upgrades, or additional verification runs.

---

## Risk Factors

| Risk | Impact | Mitigation |
|------|--------|------------|
| Low vCPU allocation (< 10) | 2x slower convergence | Add second pod or upgrade to 6000 Ada |
| CAMB numerical issues | Chain crashes, lost time | Auto-restart script, hourly backups |
| Pod preemption (if spot) | Data loss | Using on-demand, NOT spot |
| Cobaya version incompatibility | Config errors | Pin versions, test before launch |
| Planck likelihood download failure | Setup delay | Pre-download and cache |
| Poor mixing despite covmat | Slow R-hat convergence | Increase chains to 6, adjust proposal_scale |

---

## Key Insight

The clean restart with warm-start covmats and focused chain scheduling should reach full_tension science freeze in **10-15 days** at a cost of **$80-120**. This is well within the $1,000 budget and leaves room for the remaining datasets, ΛCDM controls, and any needed reruns.

The biggest uncertainty is the vCPU allocation on the A6000 pod. This will be resolved within the first hour of launch and the strategy adjusted accordingly.
