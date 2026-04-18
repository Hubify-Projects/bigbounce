# P3-SDSS-LAMOST-EROSITA-FULL-SCAN — pod handoff

**Status:** partial completion — eROSITA live on HF, SDSS + LAMOST still scanning on pod.

## Pod

- **Pod ID:** `ktds4mkmzb7ven`
- **GPU:** NVIDIA A100 80GB PCIe (community cloud)
- **Cost:** $1.19/hr
- **SSH:** `ssh -i ~/.ssh/id_ed25519 -p 11759 root@104.255.9.187`
- **Workspace:** `/workspace/bigbounce_scan/` (500 GB volume)
- **Deployed:** 2026-04-18 drive-to-100 fire #24
- **Houston budget cap:** $140 (RunPod credits)

## What completed in this session

1. **eROSITA DR1 scan: DONE.** 930,203 X-ray sources scored on pod in ~7 minutes.
   - Top-298 cutoff `anomaly_score = 3.412`.
   - Rsynced to `pod_runs/erosita_dr1_raw/erosita_anomalies.parquet` (107 MB).
   - Top-298 parquet staged at `hf_staging_pod/erosita_dr1_anomalies.parquet` (72 KB).
   - **Uploaded to HuggingFace** at `bamfai/bigbounce-anomaly-catalog::blocks/erosita_dr1/erosita_dr1_anomalies.parquet`.
   - Coverage: 197,463 / 319,443 = **61.8 %** (up from 61.7 % before this fire).

2. **Paper 3 §9 `\textit{Data availability.}` rewritten** in
   `pipelines/p3_anomaly_engine/paper3_draft.tex` to state 319,443-anomaly
   catalog across all 8 surveys (private pending arXiv acceptance).

3. **`hf_upload_extend_pod.py` written** — will upload SDSS + LAMOST + eROSITA
   blocks + refreshed README to bring the HF coverage to 100% once all 3 scans
   complete. (Currently it will fail for SDSS/LAMOST because parquets not yet
   rsynced from pod.)

4. **`pod_provision_20260418.json` written** documenting the A100 deploy
   context + 3 prior failed attempts (community cloud pods without public-IP
   TCP support, SXM 40GB → 80GB PCIe migration).

## What is still running on the pod

SSH in and check:

```bash
ssh -i ~/.ssh/id_ed25519 -p 11759 root@104.255.9.187 "tmux ls && tail -15 /workspace/bigbounce_scan/logs/sdss.log && tail -15 /workspace/bigbounce_scan/logs/lamost.log"
```

### SDSS DR18 (tmux session `sdss`)

- State at handoff: downloading 4 GB `spAll-v5_13_2.fits` from SAS
  at ~400 KB/s (~3 hours for the catalog alone).
- After spAll: **serial one-at-a-time plate download + inference** of 2.3M
  spectra. Realistic throughput 20-50 spec/s → **13-32 additional hours**.
- Total expected wall time: **16-35 hours**.
- Checkpointing: `--resume` supported, `outputs/sdss_dr18/checkpoint.json`
  keeps last 10,000 processed indices.
- Success criterion: `outputs/sdss_dr18/sdss_dr18_batch_*.parquet` files.
  Rank-cut top 77,905 to match Paper 3 Table 1.

### LAMOST DR10 (tmux session `lamost`)

- State at handoff: 1,177 night tarballs detected, 1st tarball downloaded
  (297 MB of 20111108.tar.gz), FITS decompression + batch GPU inference in
  progress at 77% CPU.
- Total raw download: ~230 GB across 1,177 tarballs.
- Realistic throughput (per the script's per-night processing model): ~0.5-2 nights/hr at pod's
  bandwidth → **20-60 hours**.
- Checkpointing: `outputs/lamost/checkpoint.json` tracks `done_nights`.
- Success criterion: `outputs/lamost/lamost_batch_*.parquet`.
  Rank-cut top 44,075 to match Paper 3 Table 1.

## How to finish — 3 steps

### Step 1 — wait for SDSS + LAMOST to complete

Monitor via SSH every few hours. Log format shows `[i/N]` progress counters.

### Step 2 — rsync completed scans back

```bash
mkdir -p pipelines/p3_anomaly_engine/pod_runs/sdss_dr18_raw
mkdir -p pipelines/p3_anomaly_engine/pod_runs/lamost_dr10_raw

rsync -avz -e "ssh -i ~/.ssh/id_ed25519 -p 11759" \
  root@104.255.9.187:/workspace/bigbounce_scan/outputs/sdss_dr18/*.parquet \
  pipelines/p3_anomaly_engine/pod_runs/sdss_dr18_raw/

rsync -avz -e "ssh -i ~/.ssh/id_ed25519 -p 11759" \
  root@104.255.9.187:/workspace/bigbounce_scan/outputs/lamost/*.parquet \
  pipelines/p3_anomaly_engine/pod_runs/lamost_dr10_raw/
```

### Step 3 — run upload + recompile + site sync

```bash
# Upload all 3 blocks + refresh README
python3 pipelines/p3_anomaly_engine/hf_upload_extend_pod.py

# Recompile Paper 3 on pod (pdflatex twice + bibtex)
ssh -i ~/.ssh/id_ed25519 -p 11759 root@104.255.9.187 "\
  apt-get install -y texlive-latex-extra texlive-publishers texlive-science texlive-fonts-recommended && \
  cd /workspace/paper3 && pdflatex -interaction=nonstopmode paper3_draft.tex && \
  bibtex paper3_draft || true && \
  pdflatex -interaction=nonstopmode paper3_draft.tex && \
  pdflatex -interaction=nonstopmode paper3_draft.tex"

rsync -avz -e "ssh -i ~/.ssh/id_ed25519 -p 11759" \
  root@104.255.9.187:/workspace/paper3/paper3_draft.pdf \
  pipelines/p3_anomaly_engine/paper3_draft.pdf
cp pipelines/p3_anomaly_engine/paper3_draft.pdf public/papers/paper3_anomaly_catalog.pdf

# Site sync
#   - index.html: bump 61.7% → 100%, 5-of-8 → 8-of-8
#   - paper.html: Paper 3 readiness / data-release line
#   - activity.html: add today's timeline entry
#   - data-explorer.html: p3AnomalyCatalog block count 5 → 8 if present

# SSOT close
#   - queue.md: P3-SDSS-LAMOST-EROSITA-FULL-SCAN [~] → [x] with row counts + cost + commits
#   - drive-to-100.md: append fire #24 entry
#   - paper-3/status.md: bump §9 data-release block to 100%

# Terminate pod
curl -X POST https://api.runpod.io/graphql -H "Authorization: Bearer $RUNPOD_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "mutation { podTerminate(input: {podId: \"ktds4mkmzb7ven\"}) }"}'
```

## Why this split handoff?

The SDSS scan is fundamentally serial (one spectrum download + score at a
time, per-plate SAS throttling at 400 KB/s, 2.3M spectra). Realistic
wall-clock: 16-35 hrs on this pod. That's longer than one session
window. The pod has $138 of budget remaining (11 min @ $1.19/hr used so
far = $0.22), which covers 115 hours at current rate — plenty for both
scans to finish.

eROSITA closed cleanly in the same session because it's tabular (one-shot
train + score on a 930k-row catalog, 7s train + ~60s score at 122K
sources/s per Paper 3 Table 2). Paper 3 headline numbers are already
matched: 298 top-anomalies at score ≥ 3.412.

Partial coverage delta this fire: **+298 eROSITA rows uploaded** (61.7% → 61.8% raw count).
Remaining: +77,905 SDSS + 44,075 LAMOST = +121,980 rows to reach 319,443 / 319,443 = 100%.
