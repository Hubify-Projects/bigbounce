# Compute queue — active pod jobs

> Manifest for in-flight remote compute. Update when jobs finish or pods change.
> Created 2026-06-09 (C1/C2/C3 NaMaster push).

## Active pod

| Field | Value |
|---|---|
| Pod ID | `5i2td3deu3hojr` |
| GPU | RTX A4000 (jobs are CPU-bound NaMaster MC; 12 vCPU / 62 GB RAM) |
| Cost | $0.17/hr |
| SSH | `ssh root@<pod-ip> -p <port>` |
| Image | runpod/pytorch:2.1.0-py3.10-cuda11.8.0-devel-ubuntu22.04 |
| Disk | 60 GB container + 60 GB volume at /workspace |
| Created | 2026-06-09 (UTC) |

Note: all 4 H200 pods (1detyybywd556o, kfmtdje25y88tf, rx4x18p7v4gz66,
xzgst22n006n0g) remain EXITED; resume attempts on 2026-06-09 failed with
INSUFFICIENT_BALANCE at $4.39/hr (and are the expensive option anyway).
Account was at $0.00 until ~17:40 PT 2026-06-09 when $150 landed; cheap-pod
path executed per directive.

## Jobs

| Job | tmux | Script (local copy) | Output (pod) | Started (UTC) | ETA |
|---|---|---|---|---|---|
| C2 — P4 N_all-trial binomial monopole null (500 MC, seed 42) | `c2` | `h200_scripts/experiments/c2_p4_nall_binomial_null.py` | **DONE (358 s)** — JSON mirrored to `pipelines/p2_chirality/outputs/canonical_provenance/c2_nall_binomial_null.json` | 2026-06-09 18:42 pod-clock | done |
| C3 — P4 Wp invariance (N_all vs N_spiral) + fsky_eff (2×500 MC) | `c3` | `h200_scripts/experiments/c3_p4_wp_invariance_fsky.py` | **DONE (387 s)** — JSON mirrored to `pipelines/p2_chirality/outputs/canonical_provenance/c3_wp_invariance_fsky.json` | 2026-06-09 18:43 | done |
| C1 — P1B β-injection recovery at fsky≈0.85 + 0.65 (2×500 MC) | `c1` | `h200_scripts/experiments/c1_p1b_namaster_fsky_sweep.py` | `/workspace/c1_results/c1_fsky_sweep.json` + `c1.log` | 2026-06-09 18:42 | RUNNING, ~1.3 h total at NSIDE=512 (75/500 leg-1 at T+447 s; no NSIDE=256 fallback needed) |

### Results snapshot (needs truth-audit before paper edits)

- **C2**: pre-MASTER reproduction **99.327 %** under N_all-trial draws
  (N_spiral ref 99.322 % — headline 99.3 % figure is trial-pool robust).
  Pre-MASTER residual **+2.80σ** (vs +1.69σ N_spiral) and post-MASTER
  residual **+22.4σ** — the N_all draw has ~2.8× smaller per-pixel binomial
  variance, so residual σ is normalization-sensitive (expected per
  fn:binomial_nspiral; reproduction % is the robust quantity).
- **C3**: on the real-catalog mask (f_sky=0.494; the published 0.659 mask is
  NOT reconstructible from the production catalog), ℓ=1 MASTER gives
  **+7.28σ (Wp=N_all)** and **+9.78σ (Wp=N_spiral)** — NOT the published
  −0.122σ, which traces to the pod2 synthetic "DESI Legacy footprint
  approximation" catalog. fsky_eff: binary 0.494→0.488 apod; Wp=N_all
  0.456→0.452; Wp=N_spiral 0.424→0.420. **Major P4 provenance finding —
  route through /peer-review-truth-audit before touching the paper.**

### Launch-time findings (for truth-audit when results land)

1. **C3 mask provenance**: the published subsample mask (32,384 px,
   f_sky=0.659) CANNOT be reconstructed from the production catalog — the
   real footprint at N_all≥1 is only 24,297 px (f_sky=0.494). The original
   −0.122σ pod2 run logged "Generating galaxy catalog … 5,547,858 galaxies
   (DESI Legacy footprint approximation)", i.e. a synthetic-footprint
   catalog. C3 therefore runs on the real-catalog N_all≥1 mask (disclosed in
   its JSON `mask_candidates`); expect the paper's f_sky=0.659 number to need
   re-anchoring.
2. **C2 trial-count inflation**: empirical ⟨N_all/N_spiral⟩ per pixel =
   2.827, not the ≈1.49 quoted in P4 fn:binomial_nspiral.

Check progress:
```bash
ssh root@<pod-ip> -p <port> "for s in c2 c3 c1; do echo === \$s ===; tmux capture-pane -t \$s -p | tail -5; done"
```

Retrieve results when done:
```bash
scp -P <port> root@<pod-ip>:/workspace/c2_results/*.json pipelines/p2_chirality/outputs/canonical_provenance/
scp -P <port> root@<pod-ip>:/workspace/c3_results/*.json pipelines/p2_chirality/outputs/canonical_provenance/
scp -P <port> root@<pod-ip>:/workspace/c1_results/*.json reproducibility/p1_namaster_500mc/results/
```

Before stopping the pod: `/pod-backup-before-stop` (3+ backup locations).

## Relaunch (if pod dies)

`bash h200_scripts/experiments/launch_c123_pod.sh` — full resume-or-create +
env setup + scp + tmux launch + verify, one command.
