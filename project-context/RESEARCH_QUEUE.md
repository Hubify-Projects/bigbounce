# Research Queue — Hubify Labs BigBounce Program

**Last updated: 2026-04-07**
**Scripts location:** `h200_scripts/experiments/`
**Results location:** `pipelines/h200_results/`

---

## COMPLETED EXPERIMENTS (Phases 1-8 + Novel)

### Phase 1: Re-run Broken Experiments (6 exp, COMPLETE)
| # | Experiment | Script | Result |
|---|-----------|--------|--------|
| 1 | Planck CMB masked | planck_cmb_masked.py | 193 anomalies, val_loss=0.14, galactic mask applied |
| 2 | ACT DR6 proper training | act_dr6_proper.py | 200 anomalies, val_loss=0.61, 100 epochs |
| 3 | NEOWISE ecliptic mask | neowise_ecliptic_mask.py | 444 anomalies, ecliptic mask applied |
| 4 | Gaia DR3 10x expansion | gaia_dr3_expanded.py | 5,000 anomalies from 500K sources, val_loss=0.004 |
| 5 | Super-resolution coord fix | superres_coord_fix.py | FAILED (KeyError: 'ra') |
| 6 | Taxonomy retuned | taxonomy_retuned.py | Per-survey UMAP models |

### Phase 2: Validation + QC (6 exp, COMPLETE)
| # | Experiment | Script | Result |
|---|-----------|--------|--------|
| 7 | Full SIMBAD/NED crossmatch | full_crossmatch.py | 479 known objects identified |
| 8 | Injection/recovery | injection_recovery.py | 4 recovery tests validated |
| 9 | Spatial clustering | spatial_clustering.py | 6 spatial clusters identified |
| 10 | Auto-inspection | auto_inspect.py | 225 top anomalies inspected |
| 11 | DESI taxonomy | desi_taxonomy.py | 10 clusters, ARI=0.956, NMI=0.962 |
| 12 | Score distributions | score_distributions.py | 7,955 score distribution analysis |

### Phase 3: Cross-Survey (6 exp, COMPLETE)
| # | Experiment | Script | Result |
|---|-----------|--------|--------|
| 13 | Planck×ACT crossmatch | planck_act_xmatch.py | 0 overlapping (independent detections) |
| 14 | DESI×eROSITA | desi_erosita_xmatch.py | 12 AGN candidates at 12σ |
| 15 | SDSS×LAMOST overlap | sdss_lamost_overlap.py | 30 overlapping anomalies |
| 16 | NEOWISE×ZTF | neowise_ztf.py | 8 cross-matches |
| 17 | eROSITA×NEOWISE | erosita_neowise.py | 0 matches |
| 18 | Multi-messenger stack | multi_messenger_stack.py | 40 multi-survey joint anomalies |

### Phase 4: Science Extraction (5 exp, COMPLETE)
| # | Experiment | Script | Result |
|---|-----------|--------|--------|
| 19 | f_NL bias validation | fnl_bias_validation.py | Bias enhancement = 2.28× |
| 20 | LAMOST as 3rd tracer | fnl_lamost_tracer.py | Multi-tracer improvement quantified |
| 21 | Threshold sweep | fnl_threshold_sweep.py | Optimal threshold = 5 |
| 22 | NANOGrav MCMC | nanograv_ptarcade.py | γ = 3.32 ± 0.37 |
| 23 | Combined PTA | nanograv_combined.py | Bayes factor = 27.6 (bounce > SMBHB), SMBHB excluded 2.7σ |

### Phase 5: New Surveys (4 exp, COMPLETE)
| # | Experiment | Script | Result |
|---|-----------|--------|--------|
| 24 | BOSS/eBOSS DR16 | boss_eboss.py | Complete |
| 25 | DES DR2 photometry | des_dr2.py | Complete |
| 26 | VLASS radio | vlass_radio.py | 77 ultra-steep-spectrum high-z candidates |
| 27 | LOFAR LoTSS DR2 | lofar_lotss.py | Complete |

### Phase 6: X-ray/Space (3 exp, COMPLETE)
| # | Experiment | Script | Result |
|---|-----------|--------|--------|
| 28 | JWST MAST | jwst_mast.py | 500 anomalies |
| 29 | Chandra CSC 2.1 | chandra_csc.py | 800 anomalies |
| 30 | XMM 4XMM-DR14 | xmm_newton.py | 1,000 anomalies |

### Phase 7: Speculations (3 exp, COMPLETE)
| # | Experiment | Script | Result |
|---|-----------|--------|--------|
| 31 | Dyson sphere search | dyson_sphere.py | Candidates identified |
| 32 | GW echo templates | gw_echo_ligo.py | Echo signatures modeled |
| 33 | FRB anomaly detection | frb_chime.py | FRB catalog analyzed |

### Phase 8: Advanced Architectures (3 exp, COMPLETE)
| # | Experiment | Script | Result |
|---|-----------|--------|--------|
| 34 | DESI transformer | desi_transformer.py | Transformer vs AE comparison |
| 35 | SDSS native autoencoder | sdss_native_autoencoder.py | SDSS-specific model |
| 36 | Multi-modal joint | multi_modal_joint.py | Spectral + photometric joint model |

### Novel Batch (4 exp, COMPLETE)
| # | Experiment | Script | Result |
|---|-----------|--------|--------|
| 37 | Second-level anomalies | second_level_autoencoder.py | Anomaly-within-anomaly detection |
| 38 | Spectral taxonomy deep | spectral_taxonomy_deep.py | Deep taxonomy classification |
| 39 | Planck lensing xcorr | planck_lensing_xcorr.py | Lensing cross-correlation |
| 40 | Multi-messenger 123σ | multi_messenger_stack.py | 123 objects at combined 123σ |

### Overnight Batches (4 batches, COMPLETE)
| Batch | Experiment | Result |
|-------|-----------|--------|
| 1 | Dyson sphere deep + FRB CHIME | Candidates + full catalog |
| 2 | Exoplanet atmospheres + SMBH JWST | Anomalous spectra + MCMC chains |
| 3 | Multi-modal joint training | Joint/photometry/spectral models |
| 4 | Anomaly cross-correlation | Correlation + significance matrices |

---

## PENDING EXPERIMENTS

### Phase 9: Full-Scale Scans (2 exp, ~$517)
| # | Experiment | Script | Est. Hours | Notes |
|---|-----------|--------|------------|-------|
| 41 | NEOWISE full (170B rows) | — | 72h | Full 10-year light curve scan |
| 42 | Gaia DR3 epoch (1.8B) | — | 72h | Full epoch photometry |

### Phase 10: Paper Compilation (2 exp, ~$22)
| # | Experiment | Script | Est. Hours | Notes |
|---|-----------|--------|------------|-------|
| 43 | Paper 3 final figures | — | 3h | Generate any remaining figures |
| 44 | Paper 4 final figures | — | 3h | Confusion matrix, training curves |

### Pipeline 1: f_NL Tracer Purification (NOT STARTED — highest priority novel work)
| Step | Task | Status |
|------|------|--------|
| 1 | Anomaly detection (BigAE) | COMPLETE |
| 2 | Cross-match with DESI clustering catalog | NOT STARTED |
| 3 | Classify tracers by bias properties | NOT STARTED |
| 4 | Validate bias enhancement (direct Landy-Szalay) | NOT STARTED |
| 5 | Re-measure σ(f_NL) with calibrated α | NOT STARTED |
| 6 | Write up for Paper 3 | NOT STARTED |

### Not Yet Deployed (need special dependencies)
| Experiment | Script | Dependency | Est. Hours |
|-----------|--------|------------|------------|
| NaMaster birefringence | birefringence_namaster.py | NaMaster install | 4h |
| Quintom MCMC | quintom_w0wa_reanalysis.py | Cobaya + CAMB | 48h |

### Future Experiment Ideas
| Experiment | Script | Priority | Notes |
|-----------|--------|----------|-------|
| Fisher forecast SPHEREx | fisher_forecast_spherex.py | HIGH | Refined f_NL forecast with calibrated tracers |
| Bias evolution | bias_evolution.py | MEDIUM | Redshift-dependent bias enhancement |
| Redshift tomography | redshift_tomography.py | MEDIUM | f_NL in redshift bins |
| Emission line finder | emission_line_finder.py | MEDIUM | Automated spectral line ID |
| Anomaly lightcurve sim | anomaly_lightcurve_sim.py | LOW | Simulated time-domain anomalies |
| Exoplanet atmospheres | exoplanet_atmos.py | LOW | JWST exoplanet spectra |
| SMBH JWST crossmatch | smbh_jwst.py | LOW | High-z SMBH candidates |
| ZTF DR21 | ztf_dr21.py | LOW | ZTF transient anomalies |
| Quintom w0wa reanalysis | quintom_w0wa_reanalysis.py | MEDIUM | Updated DESI DR2 BAO |

---

## HOW TO RUN ON A NEW POD

```bash
# 1. Create H200 SXM pod on RunPod ($3.59/hr)
# 2. SSH in:
ssh root@<IP> -p <PORT> -i ~/.ssh/id_ed25519

# 3. Clone repo:
git clone https://github.com/Hubify-Projects/bigbounce.git /workspace/bigbounce
cd /workspace/bigbounce

# 4. Install dependencies:
pip install torch numpy pandas scipy astropy scikit-learn umap-learn hdbscan emcee

# 5. Run experiments:
cd h200_scripts/experiments
python fnl_bias_validation.py    # or any script

# 6. Back up results:
scp -r /workspace/bigbounce/pipelines/h200_results/ user@local:/path/to/backup/
```

## BUDGET TRACKER

| Phase | Experiments | Actual Cost | Status |
|-------|------------|-------------|--------|
| 1 | 6 | ~$29 | COMPLETE |
| 2 | 6 | ~$36 | COMPLETE |
| 3 | 6 | ~$22 | COMPLETE |
| 4 | 5 | ~$244 | COMPLETE |
| 5 | 4 | ~$180 | COMPLETE |
| 6 | 3 | est. $100 | COMPLETE |
| 7 | 3 | est. $100 | COMPLETE |
| 8 | 3 | est. $187 | COMPLETE |
| Novel | 4 | incl. above | COMPLETE |
| Overnight | 4 | incl. above | COMPLETE |
| **Total spent** | **44** | **~$898** | |
| 9-10 (pending) | 4 | est. $539 | PENDING |
| Pipeline 1 | 5 steps | est. $50-100 | NOT STARTED |
| **Grand total** | **53** | **est. ~$1,537** | |
