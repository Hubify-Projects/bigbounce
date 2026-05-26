# P5 Track B — Pod launch runbook

The Zel'dovich-reconstruction V-Web rerun (§sec:limitations follow-up
referenced in P5 v0.1.27) is now scripted end-to-end. All artifacts are
on disk and committed; launching the pod is mechanical.

## Compute estimate

- pyrecon Zel'dovich per tracer: ~1–3 h CPU (4 tracers, can run serially
  since each holds the full NGC+SGC catalog + randoms in memory ~10 GB)
  → 4–12 h total CPU time.
- V-Web N=1024 at R_s=8 Mpc/h: ~30–90 min CPU + 60–80 GB peak RAM.
- Total wall: ~6–14 h on a single H200 SXM (251 GB RAM, 24 vCPU, $4.39/hr)
  or a CPU-only pod with ≥96 GB RAM (cheaper if available).

## Steps

### 1. Launch pod via RunPod web UI

(GraphQL `podFindAndDeployOnDemand` works but the schema for the right
GPU/CPU type IDs varies; web UI is faster.)

Recommended: **H200 SXM** template Houston has used before
(`runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04`). Confirmed
working schema fields: `vcpuCount=24`, `memoryInGb=251`,
`gpuCount=1` (GPU unused; FFT-bound work). Container disk 60 GB, volume
disk 100 GB at `/workspace`.

### 2. SSH in + rsync scripts and the matched-spiral parquet

```bash
# From laptop, replace POD_HOST + PORT from RunPod console
rsync -avz -e "ssh -p $PORT" \
    pipelines/p5_desi_chirality/env_finder/ \
    root@$POD_HOST:/workspace/env_finder/

# matched-spiral parquet (1.3 GB) is needed for the per-env analysis post-V-Web
rsync -avz -e "ssh -p $PORT" \
    pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet \
    root@$POD_HOST:/workspace/
```

### 3. Run bootstrap in tmux

```bash
ssh -p $PORT root@$POD_HOST
tmux new -s p5_track_b
bash /workspace/env_finder/pod_bootstrap.sh 2>&1 | tee /workspace/p5_track_b.log
# Detach: Ctrl-b d
```

### 4. Pull results back when done

```bash
rsync -avz -e "ssh -p $PORT" \
    root@$POD_HOST:/workspace/p5_track_b_output/ \
    pipelines/p5_desi_chirality/results/track_b_recon/
```

### 5. Integrate paper §sec:recon_robustness

After pulling results, the local agent should:

1. Run the per-env chirality analysis on the new env catalog
   (modify `scripts/08_analysis_cosmic_web.py --env <new-recon-env-parquet>`).
2. Compare per-class cw_fraction between the redshift-space V-Web (R_s=25)
   and the reconstructed V-Web (R_s=8) on the same matched-spiral subset.
3. Add §sec:recon_robustness section to `paper/p5_desi_chirality.tex`
   with the new 2×N panel: 4 env classes × (redshift-space vs reconstructed).
4. Recompile, mirror PDF to 3 locations, update SSOT.
5. Commit as `feat(p5-v0.1.28): Zel'dovich-reconstruction V-Web at R_s=8 Mpc/h — 8th positive evidence line`.

## Why we can't just do this on the laptop

- N=1024 V-Web on the full 14.6M DESI DR1 sample peaks at ~60–80 GB RAM
  (laptop has 32 GB).
- pyrecon needs ~10 GB per tracer for the full NGC+SGC catalog + 4 random
  files; doable on laptop but slow (no parallel tracer compute).
- DESI DR1 LSS catalogs are ~20–30 GB; pod has volume storage out of
  the box.

## Why this isn't on the critical path for sign-off

The §Limitations text (committed in v0.1.27) already says the headline
null is robust to RSD at R_s=25 because the Kaiser+FoG displacement
σ_v/(aH) ≈ 5–8 Mpc/h is 3–5× smaller than the smoothing scale. The
reconstructed-position rerun is a robustness panel that strengthens the
paper but is not a sign-off blocker. The 7 positive evidence lines
already in P5 v0.1.27 are sufficient for first arXiv submission per
AGENT_RULES §4.4.1. Track B adds the 8th evidence line as a follow-up
robustness panel.
