# Active Pods & Pipelines — Live Status

**Last updated:** 2026-04-02 19:15 UTC
**Only 1 pod running (H200). All 10 others EXITED (confirmed via API).**
**Auto-chain deployed:** LAMOST → Planck CMB (tmux session `autochain`)

---

## Pod: H200 — Multi-Survey Anomaly Research Queue
| Field | Value |
|-------|-------|
| **Pod ID** | `7zong4jdj46yjp` (unnecessary_plum_mandrill) |
| **SSH** | `root@103.196.86.169 -p 34546 -i ~/.ssh/id_ed25519` |
| **Machine** | NVIDIA H200 (143 GB VRAM) |
| **Pipeline** | Research Queue — 10 experiments |
| **Monitor** | `research_monitor.sh` v3 (local, checks every 15 min, auto-starts next experiment, auto-backs up) |
| **Cost** | $3.59/hr |

### Completed Experiments
| # | Experiment | Spectra/Sources | Anomalies | Runtime | Backed Up |
|---|-----------|----------------|-----------|---------|-----------|
| 1 | SDSS DR18 | 2,304,830 | 77,905 (3.4%) | 2.8h | Yes (1.8GB) |
| 2 | eROSITA DR1 X-ray | 930,203 | 9,303 (top 1%) | 8 sec | Yes |
| 8 | NANOGrav 15yr | — | — | Local | γ=3.0 at 0.33σ |

### Completed
| # | Experiment | Spectra/Sources | Anomalies | Runtime |
|---|-----------|----------------|-----------|---------|
| 3 | LAMOST DR10 | 11,418,594 | 44,075 (0.39%) | 18.3h | 

### Full Queue Runner (tmux session `queue`, auto-sequential, started 22:10 UTC Apr 2)
| Order | # | Experiment | Est. Hours | Script | Status |
|-------|---|-----------|-----------|--------|--------|
| 1 | 4 | Planck CMB full-sky | 8h | `planck_cmb_scan.py` | **RUNNING** |
| 2 | 7 | ACT DR6 CMB | 4h | `act_dr6_scan.py` | Queued |
| 3 | 5 | NEOWISE variability | 2-8h | `neowise_scan.py` | Queued |
| 4 | 6 | Gaia DR3 epoch | 2-8h | `gaia_epoch_scan.py` | Queued |
| 5 | 9 | SDSS × DESI cross-match | 1h | `sdss_desi_crossmatch.py` | Queued |
| 6 | 10 | Super-resolution | 2h | `superres_scan.py` | Queued |
| 10 | Super-resolution | 48h | $200 |

## Historical Pod 1: H200 Beast — DESI DR1 (COMPLETE, POD STOPPED)
**Result:** 18M spectra processed, 195,829 anomalies found (1.08%). Pod `rtv8cegaw1618r` is stopped.

---

## Historical Pod 2: H100 — Galaxy Chirality Catalog (COMPLETE, EXITED)
**Pod ID:** `ulfxypratod4vr` (preferred_green_cephalopod) — **EXITED** (confirmed via API 2026-04-02)
**Result:** 8,474,531 galaxies classified (CW/CCW/NOT_SPIRAL). 93.7% accuracy, 8/8 bias tests passed. CW/(CW+CCW)=0.4974, dipole=0.43σ (null). Catalog published to HuggingFace + Convex + B2.

## Historical Pod 3: RTX A4000 — w0-wa MCMC (CONVERGED, EXITED)
**Pod ID:** `fn19oivkjowmq4` (electronic_indigo_bison) — **EXITED** (confirmed via API 2026-04-02)
**Result:** w0 = -0.871 ± 0.060, wa = -0.542 ± 0.245, P(quintom-B) = 98.6%. 50,900 samples, R-1 < 0.01. Chains frozen and backed up.

## Historical Pod 4: CPU — Pipeline B (SUPERSEDED, EXITED)
**Pod ID:** `kqo1b4e4igycra` (vertical_plum_starfish) — **EXITED** (confirmed via API 2026-04-02)
Superseded by H200 which completed DESI DR1 150x faster.

## Historical Pod 5: bigbounce-dr1-a100 (NEVER STARTED, EXITED)
**Pod ID:** `4s3iruhwqu4y3w` — **EXITED** (confirmed via API 2026-04-02). Never provisioned successfully.

---

## Backup Locations

| Location | What's there | Last updated |
|----------|-------------|-------------|
| **Local disk** | All chains, anomaly catalogs, scripts, figures, h200 results | 2026-04-02 |
| **GitHub** (main) | Full repo, committed results | Push after each session |
| **Backblaze B2** | MCMC chains + scripts + figures | 2026-03-26 (needs refresh) |
| **HuggingFace** | `bamfai/bigbounce-mcmc`, `bamfai/desi-spectral-anomaly-detector` | 2026-03-26 (needs refresh) |
| **Convex** | Chirality catalog C (8.47M rows) | 2026-03-28 |
| **RunPod H200** | Live data — LAMOST running, Planck auto-chained | Active |

---

## Quick Check Commands

```bash
# H200 — check LAMOST / auto-chain progress
ssh root@103.196.86.169 -p 34546 -i ~/.ssh/id_ed25519 "tail -5 /workspace/bigbounce/lamost_h200.log"
ssh root@103.196.86.169 -p 34546 -i ~/.ssh/id_ed25519 "tail -5 /workspace/bigbounce/autochain.log"
ssh root@103.196.86.169 -p 34546 -i ~/.ssh/id_ed25519 "tmux ls"

# H200 — backup all results to local
scp -P 34546 -i ~/.ssh/id_ed25519 -r root@103.196.86.169:/workspace/bigbounce/outputs/ ./pipelines/h200_results/
```
