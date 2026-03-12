# BigBounce Paper-1 MCMC Clean Restart — Phased Execution Plan

## Phased Launch Strategy

### Phase 1: Infrastructure Setup (Day 0)

**Duration:** ~1 hour

1. Create network volume `bigbounce-paper1-canonical` (75 GB)
2. Provision RTX A6000 pod on-demand, attach network volume
3. Verify pod has SSH access, confirm vCPU/RAM allocation
4. Clone bigbounce repo to `/workspace/bigbounce/`
5. Install dependencies: cobaya, camb, healpy, getdist, planck likelihoods
6. Upload warm-start covmats from local snapshot
7. Create directory structure per storage design
8. Generate fresh Cobaya YAML configs for all datasets
9. Verify CAMB + Planck likelihoods work with a quick test evaluation

---

### Phase 2: Launch full_tension Canonical (Day 0, after setup)

**Priority:** HIGHEST — this is the paper's anchor result

- Launch 4 chains for `full_tension` delta-Neff model
- Each chain uses warm-start covmat from gpu_run_snapshot_20260305_0824
- Verify all 4 chains producing samples within first 30 minutes
- Set up hourly backup script
- Set up off-pod rsync from local machine
- Expected daily burn: $7.92/day (A6000 at $0.33/hr)

---

### Phase 3: Launch Remaining Canonical Datasets (Day 1)

**Condition:** full_tension chains verified healthy

- Launch 4 chains each for: planck_only, planck_bao, planck_bao_sn
- All delta-Neff model
- Uses same pod (chains share CPU resources)
- Total chains running: 16 delta-Neff chains
- May need to stagger if vCPU count is too low (e.g., run 8 at a time)

---

### Phase 4: Launch LCDM Controls (Day 3-5)

**Condition:** Canonical chains stable and accumulating samples

- Launch 4 chains per dataset for LCDM model
- Can run on same pod or a second pod if CPU-constrained
- LCDM converges faster (6 vs 7 sampled parameters)
- Lower priority — only needed for model comparison, not the main result

---

### Phase 5: Convergence Monitoring (Ongoing)

- Daily convergence checks (R-hat, ESS, drift)
- Track freeze gate progress for each dataset
- Adjust chain scheduling if needed

---

### Phase 6: Science Freeze (Day 10-15 target for full_tension)

- When full_tension passes all 8 freeze gates, freeze those chains
- Generate final posterior, create getdist plots
- Continue other datasets

---

## Pod Management Strategy

### Single Pod Approach (preferred if vCPUs >= 16)

- Run all 16 canonical chains on one A6000 pod
- Add LCDM chains later or on a second pod
- Simpler to manage, single backup target

### Dual Pod Approach (if vCPUs < 12)

- Pod 1: full_tension + planck_bao_sn (highest priority datasets)
- Pod 2: planck_only + planck_bao + LCDM controls
- Daily burn: $15.84/day (2 x $7.92)

---

## Expected Timeline

| Milestone                        | Optimistic | Realistic | Conservative |
|----------------------------------|-----------|-----------|--------------|
| Infrastructure ready             | Day 0     | Day 0     | Day 0        |
| full_tension chains running      | Day 0     | Day 0     | Day 1        |
| All 16 canonical chains running  | Day 1     | Day 2     | Day 3        |
| LCDM controls launched           | Day 3     | Day 5     | Day 7        |
| full_tension useful diagnostics  | Day 3     | Day 5     | Day 7        |
| full_tension near 6/8 gates      | Day 7     | Day 10    | Day 14       |
| full_tension science freeze      | Day 10    | Day 14    | Day 20       |
| All canonical datasets frozen    | Day 14    | Day 20    | Day 30       |
| LCDM controls sufficient         | Day 14    | Day 18    | Day 25       |

---

## Daily Burn Rate

| Scenario              | Pods | Cost/hr          | Cost/day       | $1000 runway |
|-----------------------|------|------------------|----------------|-------------|
| Single A6000          | 1    | $0.33            | $7.92          | 126 days    |
| Single A6000 + NV     | 1    | $0.33 + $0.07 NV | $9.60          | 104 days    |
| Dual A6000 + NV       | 2    | $0.73            | $17.52 + NV    | 55 days     |
| A6000 + RTX 6000 Ada  | 2    | $1.07            | $25.68 + NV    | 38 days     |

Note: Network volume cost is ~$0.07/GB/month = ~$5.25/month for 75GB, negligible vs pod cost.

---

## Decision Points

1. **After Phase 2 verification (Day 0):** Confirm vCPU count. If < 12, plan for dual pod.
2. **After Day 3:** Review chain throughput. If < 500 samples/day/chain, consider upgrading to RTX 6000 Ada.
3. **After Day 7:** First convergence milestone check. full_tension should show R-hat < 0.05.
4. **After Day 14:** If full_tension not near freeze, evaluate whether to extend or pivot.
