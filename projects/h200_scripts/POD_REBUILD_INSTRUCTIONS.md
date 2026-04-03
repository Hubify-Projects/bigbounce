# H200 Pod Rebuild Instructions

If the current pod dies or needs replacement, follow these steps to get back to full operation.

## 1. Launch New Pod

- **GPU:** NVIDIA H200 (143 GB VRAM)
- **CPU:** 192 cores minimum
- **RAM:** 1 TB+
- **Storage:** 1 TB+ network volume
- **Image:** RunPod PyTorch (any recent version with CUDA)
- **Cost:** ~$3.59/hr

Via RunPod API:
```python
import runpod
runpod.api_key = "YOUR_KEY"  # From .env.local RUNPOD_API_KEY
pod = runpod.create_pod(name="bigbounce-h200", gpu_type_id="NVIDIA H200 SXM", 
                        image_name="runpod/pytorch:2.1.0-py3.10-cuda11.8.0-devel-ubuntu22.04",
                        volume_in_gb=500)
```

## 2. Install Dependencies

```bash
ssh root@<IP> -p <PORT> -i ~/.ssh/id_ed25519
pip install healpy pyarrow pandas astropy scikit-learn umap-learn hdbscan matplotlib
```

## 3. Upload Scripts and Model

```bash
# From local machine:
scp -P <PORT> -i ~/.ssh/id_ed25519 -r projects/h200_scripts/*.py root@<IP>:/workspace/bigbounce/
scp -P <PORT> -i ~/.ssh/id_ed25519 projects/h200_scripts/pod_backup/best_model_47k.pt root@<IP>:/workspace/bigbounce/
scp -P <PORT> -i ~/.ssh/id_ed25519 projects/h200_scripts/pod_backup/enhanced_18M_inference.py root@<IP>:/workspace/bigbounce/
```

## 4. Upload Data (if not on network volume)

The DESI DR1 data and previous results need to be re-downloaded or restored:
- SDSS anomaly batches: `pipelines/h200_results/sdss_dr18/sdss_batch_*.parquet`
- LAMOST batches: download via `lamost_scan_v2.py`
- eROSITA: download via `erosita_scan.py`
- Planck SMICA map: auto-downloads in `planck_cmb_scan.py`

## 5. Launch Queue

```bash
ssh root@<IP> -p <PORT> -i ~/.ssh/id_ed25519
cd /workspace/bigbounce
nohup bash run_phase2_queue.sh > /dev/null 2>&1 &
nohup bash watchdog_loop.sh > /dev/null 2>&1 &
```

## Script Inventory

### Phase 1 — Completed Survey Scans
| Script | Survey | Status |
|--------|--------|--------|
| `enhanced_18M_inference.py` | DESI DR1 (18M spectra) | DONE |
| `sdss_dr18_scan.py` / `run_sdss_scan.py` | SDSS DR18 (2.3M spectra) | DONE |
| `lamost_scan_v2.py` | LAMOST DR10 (11.4M spectra) | DONE |
| `erosita_scan.py` | eROSITA DR1 (930K sources) | DONE |
| `planck_cmb_scan.py` | Planck CMB (20K patches) | DONE |
| `act_dr6_scan.py` | ACT DR6 (20K patches) | DONE |
| `neowise_scan.py` | NEOWISE (43.5K sources) | DONE |
| `gaia_epoch_scan.py` | Gaia DR3 (50K variables) | DONE |
| `superres_scan.py` | Super-resolution (10K input) | DONE |
| `sdss_desi_crossmatch.py` | SDSS×DESI cross-match | DONE (partial) |

### Phase 2 — Analysis Experiments (GPU-intensive)
| Script | What | GPU Use |
|--------|------|---------|
| `anomaly_taxonomy.py` | UMAP+HDBSCAN on 50K latent vectors | Heavy (cuML GPU) |
| `planck_lensing_crosscorr.py` | CMB lensing × anomaly cross-power | Medium (healpy) |
| `photoz_from_latent.py` | Photo-z MLP training on latent vectors | Heavy (PyTorch) |
| `emission_line_finder.py` | Classify anomalies by spectral features | Light (sklearn) |
| `anomaly_density_map.py` | Full-sky anomaly rate analysis | Light (healpy) |

### Support Scripts
| Script | Purpose |
|--------|---------|
| `best_model_47k.pt` | Trained spectral autoencoder (47K params) |
| `h200_experiments.py` | Original experiment runner |
| `injection_recovery_real.py` | Model injection/recovery test |
| `run_phase2_queue.sh` | Phase 2 queue runner |
| `watchdog_loop.sh` | Auto-restart watchdog |

## Monitoring

```bash
# Check queue progress
ssh root@<IP> -p <PORT> -i ~/.ssh/id_ed25519 "cat /workspace/bigbounce/phase2_queue.log"

# Check GPU usage
ssh root@<IP> -p <PORT> -i ~/.ssh/id_ed25519 "nvidia-smi"

# Check all experiment status
ssh root@<IP> -p <PORT> -i ~/.ssh/id_ed25519 "for d in taxonomy planck_lensing photoz_latent emission_lines density_map; do echo \$d:; cat /workspace/bigbounce/outputs/\$d/checkpoint.json 2>/dev/null || echo 'not started'; done"
```
