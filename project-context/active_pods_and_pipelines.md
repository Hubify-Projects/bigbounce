# Active Pods & Pipelines — Live Status

**Last updated:** 2026-04-03 UTC
**ALL 10 EXPERIMENTS COMPLETE. Queue finished. H200 GPU is now idle — pod can be stopped to save $3.59/hr.**

---

## Pod: H200 — Multi-Survey Anomaly Research Queue — COMPLETE
| Field | Value |
|-------|-------|
| **Pod ID** | `7zong4jdj46yjp` (unnecessary_plum_mandrill) |
| **SSH** | `root@103.196.86.169 -p 34546 -i ~/.ssh/id_ed25519` |
| **Machine** | NVIDIA H200 (143 GB VRAM) |
| **Pipeline** | Research Queue — 10 experiments — ALL DONE |
| **Status** | IDLE — stop pod to save $3.59/hr |

### Completed Experiments (All 10)
| # | Experiment | Spectra/Sources | Anomalies | Runtime | Backed Up |
|---|-----------|----------------|-----------|---------|-----------|
| 1 | DESI DR1 (previous run) | 18,700,000 | 195,829 (1.08%) | Previous | Yes |
| 2 | SDSS DR18 | 2,304,830 | 77,905 (3.4%) | 2.8h | Yes (1.8GB) |
| 3 | eROSITA DR1 X-ray | 930,203 | 9,303 (top 1%) | 8 sec | Yes |
| 4 | LAMOST DR10 | 11,418,594 | 44,075 (0.39%) | 18.3h | Yes |
| 5 | Planck CMB | 20,000 patches | 200 (1%) | 10s training | Yes |
| 6 | Gaia DR3 | 50,000 variables | 500 (1%) | ~1 min | Yes |
| 7 | ACT DR6 | 20,000 patches | 200 (1%) | ~5 min (+20 min download) | Yes |
| 8 | NEOWISE | 43,500 sources | 436 (1%) | ~5 min | Yes |
| 9 | NANOGrav 15yr | 13 freq bins | γ=3.20±0.42 consistency | Local | Yes |
| — | SDSS×DESI cross-match | — | 3 matches (z≈5.27 QSO) | Local | Yes |

**Grand totals: ~33.5M sources/spectra scored, ~328,448 anomalies across 8 surveys + 1 GW consistency check.**

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
| **Local disk** | All chains, anomaly catalogs, scripts, figures, h200 results | 2026-04-03 |
| **GitHub** (main) | Full repo, committed results | Push after each session |
| **Backblaze B2** | MCMC chains + scripts + figures | 2026-04-03 |
| **HuggingFace** | `bamfai/bigbounce-mcmc`, `bamfai/desi-spectral-anomaly-detector` | 2026-04-03 |
| **Convex** | Chirality catalog C (8.47M rows) | 2026-03-28 |
| **RunPod H200** | All results backed up — pod idle, ready to stop | 2026-04-03 |

---

## Quick Check Commands

```bash
# H200 — all experiments complete; stop the pod via RunPod console to save $3.59/hr
# Final backup all results to local (if not already done):
scp -P 34546 -i ~/.ssh/id_ed25519 -r root@103.196.86.169:/workspace/bigbounce/outputs/ ./pipelines/h200_results/
```
