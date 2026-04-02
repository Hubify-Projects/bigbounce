# Active Pods & Pipelines — Live Status

**Last updated:** 2026-04-02
**Only 1 pod running. All others stopped.**

---

## Pod: H200 — Multi-Survey Anomaly Research Queue
| Field | Value |
|-------|-------|
| **Pod ID** | `7zong4jdj46yjp` (unnecessary_plum_mandrill) |
| **SSH** | `root@103.196.86.169 -p 34546 -i ~/.ssh/id_ed25519` |
| **Machine** | NVIDIA H200 (143 GB VRAM) |
| **Pipeline** | Research Queue — 10 experiments |
| **Monitor** | `research_monitor.sh` (local, checks every 15 min) |
| **Cost** | $3.59/hr |

### Completed Experiments
| # | Experiment | Spectra/Sources | Anomalies | Runtime | Backed Up |
|---|-----------|----------------|-----------|---------|-----------|
| 1 | SDSS DR18 | 2,304,830 | 77,905 (3.4%) | 2.8h | Yes (1.8GB) |
| 2 | eROSITA DR1 X-ray | 930,203 | 9,303 (top 1%) | 8 sec | Yes |
| 8 | NANOGrav 15yr | — | — | Local | γ=3.0 at 0.33σ |

### Running
| # | Experiment | Total | Progress | ETA |
|---|-----------|-------|----------|-----|
| 3 | LAMOST DR10 | 11.4M spectra | Downloading tarballs (~9/1177) | ~12-24h |

### Queued (scripts deployed on H200)
| # | Experiment | Est. Hours | Est. Cost |
|---|-----------|-----------|-----------|
| 4 | Planck CMB full-sky | 8h | $50 |
| 5 | NEOWISE variability | 48h | $300 |
| 6 | Gaia DR3 epoch | 96h | $500 |
| 7 | ACT DR6 CMB | 8h | $50 |
| 9 | SDSS × DESI cross-match | 2h | $0 |
| 10 | Super-resolution | 48h | $200 |

## Historical Pod 1: H200 Beast — DESI DR1 (COMPLETE, POD STOPPED)
**Result:** 18M spectra processed, 195,829 anomalies found (1.08%). Pod `rtv8cegaw1618r` is stopped.

---

## Pod 2: H100 — 8.47M Galaxy Chirality Catalog
| Field | Value |
|-------|-------|
| **Pod ID** | `ulfxypratod4vr` (preferred_green_cephalopod) |
| **SSH** | `root@64.247.201.47 -p 10778 -i ~/.ssh/id_ed25519` |
| **Machine** | NVIDIA H100 (80 GB), 208 CPU cores, 2 TB RAM |
| **Pipeline** | Pipeline 2 — Galaxy chirality classification |
| **Script** | `/workspace/run_v2_smith42.py` |
| **Log** | `/workspace/smith42.log` |
| **Progress** | 3,486,955/8,470,000 galaxies (41.1%), shard 79/192 |
| **Rate** | ~40 galaxies/sec |
| **ETA** | ~36 hours from last check |
| **Dataset** | Smith42/galaxies (8.47M galaxy images) |

**What this produces:** The largest bias-audited galaxy handedness (CW/CCW/NOT_SPIRAL) catalog ever created. v2 model: 93.7% accuracy, 8/8 bias tests passed, equivariant CW fraction = 0.5012.

---

## Pod 3: RTX A4000 — w0-wa Quintom MCMC -- CONVERGED
| Field | Value |
|-------|-------|
| **Pod ID** | `fn19oivkjowmq4` (electronic_indigo_bison) |
| **SSH** | `root@157.157.221.30 -p 24859 -i ~/.ssh/id_ed25519` |
| **Machine** | RTX A4000 (16 GB), 32 CPU cores, 124 GB RAM |
| **Pipeline** | MCMC — w0-wa CPL dark energy test |
| **Script** | `cobaya-run cobaya_w0wa_quintom_test.yaml` |
| **Log** | `/workspace/mcmc_w0wa.log` |
| **Chains** | `/workspace/chains/w0wa_quintom/spin_torsion.1.txt` |
| **Progress** | **CONVERGED** — 50,900 accepted samples, R-1 < 0.01 |
| **Rate** | ~30 accepted/min |
| **Data** | Planck 2018 NPIPE + SDSS DR16 BAO + Pantheon+ |

**Final result:** w0 = -0.871 +/- 0.060, wa = -0.542 +/- 0.245, P(quintom-B) = 98.6%. Independently confirms DESI DR2 w-crossing at 2.3 sigma. Chains frozen and backed up.

---

## Pod 4: CPU — Pipeline B Local Batch Processing
| Field | Value |
|-------|-------|
| **Pod ID** | `kqo1b4e4igycra` (vertical_plum_starfish) |
| **SSH** | `root@157.157.221.29 -p 29268 -i ~/.ssh/id_ed25519` |
| **Machine** | 32 CPU cores, 124 GB RAM (no GPU) |
| **Pipeline** | Pipeline B — DESI spectral batch processing (local/CPU version) |
| **Script** | `/dev/shm/bigbounce/pipeline_B/scripts/12b_batch_local.py` |
| **Progress** | 540/2,888 pixels (19%), 368K spectra, 36,254 anomalies |
| **Rate** | ~6 spectra/sec (CPU-bound, much slower than H200) |
| **Uptime** | 42+ hours |

**What this is:** Earlier/slower version of the same DESI anomaly pipeline, running CPU-only. The H200 pod is doing this 150x faster. This pod may be redundant now that the H200 is running.

---

## Pod 5: bigbounce-dr1-a100 (Provisioning)
| Field | Value |
|-------|-------|
| **Pod ID** | `4s3iruhwqu4y3w` |
| **Status** | RUNNING but runtime=null (still provisioning or stuck) |

---

## Backup Locations

| Location | What's there | Last updated |
|----------|-------------|-------------|
| **Local disk** | All chains, scripts, figures, anomaly catalog | 2026-03-26 |
| **GitHub** | Committed and pushed (main) | 2026-03-26 |
| **Backblaze B2** | MCMC chains + scripts + figures | 2026-03-26 |
| **HuggingFace** | `bamfai/bigbounce-mcmc` (private dataset), `bamfai/desi-spectral-anomaly-detector` (model) | 2026-03-26 |
| **RunPod pods** | Live data on each pod | Running |

---

## Quick Check Commands

```bash
# H200 DESI DR1 progress
ssh root@205.196.17.44 -p 10789 -i ~/.ssh/id_ed25519 "tail -5 /workspace/desi_dr1/dr1_log.txt"

# H100 chirality progress
ssh root@64.247.201.47 -p 10778 -i ~/.ssh/id_ed25519 "tail -5 /workspace/smith42.log"

# MCMC progress
ssh root@157.157.221.30 -p 24859 -i ~/.ssh/id_ed25519 "tail -5 /workspace/mcmc_w0wa.log"

# Pipeline B CPU progress
ssh root@157.157.221.29 -p 29268 -i ~/.ssh/id_ed25519 "tail -5 /dev/shm/bigbounce/batch_log.txt"
```
