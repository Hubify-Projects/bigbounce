# BigBounce Session Handoff — 2026-03-06 00:35 UTC

## COMPLETED: Report Truth Audit (DONE — 2026-03-06)

The non-destructive "report truth audit" of the global monitor is COMPLETE.

### What was done:
1. Audited global_status.py — classified every metric as host/infrastructure vs pod/job-level
2. SSHed into all 7 pods — collected ground-truth data (read-only)
3. ESS ETA predictions suppressed with LOW CONFIDENCE label (chains still in burn-in)
4. Verified backups were dry-run only — then created REAL backups on all 7 pods
5. Wrote corrected reports:
   - `research/global_monitor/global_status_corrected.txt`
   - `research/global_monitor/warnings_corrected.txt`

### Misleading metrics DOCUMENTED in corrected reports:
- CPU pod "uptime: 418 days" — HOST machine uptime, not container age
- GPU "disk: 479T / 46%" — shared cluster NFS mount, not pod storage
- CPU "disk: 50G / 6%" — pod overlay filesystem (IS pod-specific)
- GPU utilization 0% — expected, MCMC is CPU-bound
- CPU#2 "DOWN" in old report — was SSH timeout false alarm, pod is ALIVE
- ESS ETAs — SUPPRESSED until 48h+ of post-mixing data
- Backups — ALL 7 pods now have real tarballs (created 2026-03-06 00:27 UTC)

---

## Active Pod Inventory

### Paper 1 (MCMC — DO NOT TOUCH)

| Pod | ID | SSH | Processes | Role |
|-----|-----|-----|-----------|------|
| GPU | 47htajss1ng2ig | `ssh -i ~/.ssh/id_ed25519 -p 38115 root@195.26.233.79` | 32 cobaya | 28 chains (4 datasets × 7) |
| CPU#1 | m4xpnxzgokd93f | `ssh -i ~/.ssh/id_ed25519 -p 30194 root@157.157.221.30` | 16 cobaya | 16 chains (4 datasets × 4) |
| CPU#2 | eblghcn6u43wfk | `ssh -i ~/.ssh/id_ed25519 -p 40204 root@157.157.221.30` | 16 cobaya | 17 ΛCDM control chains |

**Chain file locations:**
- GPU: `/workspace/bigbounce/reproducibility/chains/*/spin_torsion.1.txt`
- CPU#1: `/workspace/bigbounce/reproducibility/cosmology/cpu_primary_run_20260305/chains/*/spin_torsion.1.txt`
- CPU#2: `/workspace/bigbounce/reproducibility/cosmology/cpu_secondary_suite_20260305/controls_lcdm/*/lcdm.1.txt`

**Monitor/freeze PIDs:**
- GPU: freeze=39713, monitor=36885
- CPU#1: freeze=5454, monitor=6594
- CPU#2: freeze=3283, monitor=4095

**Convergence (as of 00:22 UTC, 2026-03-06):**
- GPU Full Tension: H₀ R-hat-1=0.085, Ω_m=0.043, tau=0.704, ESS(H0)=88, ESS(dN)=66
- GPU Planck+BAO+SN: H₀ R-hat-1=0.229, tau=1.018
- GPU Planck+BAO: H₀ R-hat-1=0.368, tau=0.893
- GPU Planck Only: H₀ R-hat-1=0.334, tau=0.881, DRIFTING (H0 -0.35σ, dNeff -0.45σ)
- CPU#1: 16 chains, 260-333 samples/chain, convergence monitor running but no R-hat yet
- CPU#2: 16 LCDM chains, 270-408 samples/chain, no convergence data yet
- Publication targets: R-hat-1 < 0.01, ESS(H₀,ΔNeff) ≥ 2000, ESS(τ) ≥ 1000
- ESS ETAs: SUPPRESSED (LOW CONFIDENCE) — chains still in mixing/burn-in

**Backup status (as of 00:31 UTC, 2026-03-06):**
- GPU: 5.7 MB tarball at /workspace/bigbounce/reproducibility/backups/
- CPU#1: 810 KB tarball at .../cpu_primary_run_20260305/backups/
- CPU#2: 979 KB tarball at .../cpu_secondary_suite_20260305/backups/
- Paper 2 (all 4): backed up (705KB to 118MB)
- GPU frozen pack: full_tension FROZEN 2026-03-05 10:15 UTC (4.9 MB)

### Paper 2 (Research Tracks — First runs complete)

| Pod | ID | SSH | Python | Track |
|-----|-----|-----|--------|-------|
| Track A | bpou58tmt95jjb | `ssh -i ~/.ssh/id_ed25519 -p 22055 root@69.30.85.227` | python3.11 | WP4 ΔNeff microphysics |
| Track B | mz3srzbzxxv1yj | `ssh -i ~/.ssh/id_ed25519 -p 22157 root@69.30.85.228` | python3.11 | WP5 spin amplitude |
| Track C | pkysk4lbaqnhm0 | `ssh -i ~/.ssh/id_ed25519 -p 22183 root@69.30.85.244` | python3 | P7 CNN spin classifier |
| Track D | uktt3hghbs1djo | `ssh -i ~/.ssh/id_ed25519 -p 22128 root@69.30.85.234` | python3.11 | P6 CMB EB birefringence |

**First-run results:**
- Track A: Reheating (24k rows) + decay (32k rows) scans. Best ΔNeff~0.15 fits found.
- Track B: 100k MC samples, ε_PO=0.244 (68% CI: 0.14-0.38), 3 figures generated.
- Track C: Synthetic 2000 images, ResNet-18 10 epochs, test_acc=0.49 (expected ~random for synthetic).
- Track D: Tier 1 complete — β=0.358±0.025° (all), β=0.393±0.033° (independent), forest plot. Tier 2 not attempted.

**Framing constraints (user-specified):**
- Track A: "candidate microphysics realization" NOT first-principles derivation
- Track B: "phenomenological parity-odd tidal torque mapping" NOT torsion derivation
- Track C: "pipeline/data product" NOT cosmological measurement
- Track D: two-tier, NO independent EB detection claim

---

## Key Files

| File | Purpose |
|------|---------|
| `research/global_monitor/pod_registry.yaml` | All 7 pods with SSH, paths, PIDs |
| `research/global_monitor/global_status.py` | 845-line SSH-based status collector |
| `research/global_monitor/global_backup.py` | 452-line backup tarball creator |
| `research/global_monitor/global_artifact_index.py` | 481-line frozen pack scanner |
| `research/global_monitor/global_status_latest.txt` | Last status report (has known issues — see corrected) |
| `research/global_monitor/global_status_latest.json` | Machine-readable status (has known issues) |
| `research/global_monitor/global_status_corrected.txt` | Truth-audited corrected status report |
| `research/global_monitor/warnings_corrected.txt` | Truth-audited corrected warnings |
| `research/global_monitor/hourly_loop.sh` | Hourly cron (not yet started) |
| `research/paper2/*/MANIFEST.md` | Framing constraints per track |
| `project-context/FEATURE_REQUESTS.md` | All feature requests |
| `.env.local` | RunPod API key |

---

## RunPod Notes
- API key in `.env.local`: `RUNPOD_API_KEY=<REDACTED — see .env.local>`
- Pod creation fix: `volumeInGb: 0`, `cloudType: SECURE` (unquoted enum)
- Base image pods: python3 is 3.8 (no pip), use python3.11 for numpy/scipy
- Balance was ~$87 at $3.03/hr for Paper 1 only, now +4 more pods

## Author
Houston Golden is THE AUTHOR. AI agents are research assistants, not co-authors.
