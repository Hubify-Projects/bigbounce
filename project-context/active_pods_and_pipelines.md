# Active Pods & Pipelines — Live Status

**Last updated:** 2026-03-26
**DO NOT TERMINATE ANY PODS without explicit user approval.**

---

## Pod 1: H200 Beast — DESI DR1 Spectral Anomaly Inference -- COMPLETE
| Field | Value |
|-------|-------|
| **Pod ID** | `rtv8cegaw1618r` (defeated_harlequin_lemming) |
| **SSH** | `root@205.196.17.44 -p 10789 -i ~/.ssh/id_ed25519` |
| **Machine** | NVIDIA H200 (143 GB VRAM), 192 CPU cores, 3 TB RAM |
| **Pipeline** | Pipeline B — DESI DR1 GPU inference |
| **Script** | `/workspace/desi_dr1/run_dr1_parallel.py` |
| **Log** | `/workspace/desi_dr1/dr1_log.txt` |
| **Progress** | **COMPLETE** — 18M spectra processed, 195,829 anomalies found (1.08%) |
| **Rate** | 889 spectra/sec (peak) |
| **Anomaly rate** | 1.08% |
| **Dataset** | DESI DR1 full spectroscopic catalog (~18M spectra) |

**Result:** Survey-scale anomaly catalog from ALL DESI DR1 spectra. 195,829 anomalies found. 99.8% absent from SIMBAD. 0% known QSOs. Galaxies 19x more anomalous than QSOs. Model published on HuggingFace. Anomaly Explorer page live on website.

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
