# Enhanced 18M Re-Run Specification

**Purpose:** Extract maximum value from a single pass over all 17.65M DESI DR1 spectra.
**Estimated time:** ~6-8 hours on H200
**Output:** ~3-5 GB structured catalog (Parquet format)

---

## Columns to Extract Per Object (from coadd + redrock files)

### From autoencoder (our model)
| Column | Type | Description | Why it matters |
|--------|------|-------------|----------------|
| `anomaly_score` | float32 | Total reconstruction error (rB+rR+rZ) | Core anomaly metric |
| `rB` | float32 | B-band reconstruction error | Localizes anomaly to blue |
| `rR` | float32 | R-band reconstruction error | Localizes to red |
| `rZ` | float32 | Z-band reconstruction error | Localizes to near-IR |
| `worst_band` | char | Band with highest residual (B/R/Z) | Quick classification |
| `latent_vector` | float32[128] | Autoencoder latent representation | Enables clustering, t-SNE, neighbor search |
| `peak_residual_wavelength` | float32 | Wavelength (Å) of maximum per-pixel residual | WHERE in the spectrum the anomaly occurs |
| `residual_kurtosis` | float32 | Kurtosis of residual distribution | Sharp spike vs broad deviation |

### From DESI redrock (pipeline classifications)
| Column | Type | Description | Why it matters |
|--------|------|-------------|----------------|
| `z` | float64 | Pipeline redshift | Distance/epoch of object |
| `zerr` | float64 | Redshift uncertainty | Confidence in z |
| `zwarn` | int64 | Redshift warning flags | 0 = confident, >0 = suspect |
| `spectype` | string | Pipeline classification (STAR/GALAXY/QSO) | Compare with our anomaly class |
| `subtype` | string | Subtype (e.g., CV, BROADLINE) | Finer classification |
| `deltachi2` | float64 | Chi2 difference between best and 2nd-best fit | Classification confidence |

### From DESI FIBERMAP (targeting + photometry)
| Column | Type | Description | Why it matters |
|--------|------|-------------|----------------|
| `targetid` | int64 | Unique DESI identifier | Cross-reference key |
| `target_ra` | float64 | Right ascension | Position |
| `target_dec` | float64 | Declination | Position |
| `morphtype` | string | Legacy Survey morphology (PSF/REX/EXP/DEV/SER) | Point source vs extended |
| `flux_g` | float32 | g-band flux (nanomaggies) | Brightness + color |
| `flux_r` | float32 | r-band flux | Brightness + color |
| `flux_z` | float32 | z-band flux | Brightness + color |
| `flux_w1` | float32 | WISE W1 flux | IR brightness |
| `flux_w2` | float32 | WISE W2 flux | IR brightness |
| `ebv` | float32 | E(B-V) dust extinction | Foreground correction |
| `parallax` | float32 | Gaia parallax (if available) | Star identifier (parallax > 0) |
| `gaia_phot_g_mean_mag` | float32 | Gaia G magnitude | Cross-ref brightness |
| `sersic` | float32 | Sersic index | Galaxy profile shape |
| `shape_r` | float32 | Half-light radius (arcsec) | Object size |
| `coadd_numexp` | int16 | Number of exposures combined | Data quality |
| `coadd_exptime` | float32 | Total exposure time (s) | Data quality |
| `mean_fiber_ra` | float64 | Mean fiber RA across exposures | Astrometric precision |
| `mean_fiber_dec` | float64 | Mean fiber Dec | Astrometric precision |

### From DESI SCORES (signal-to-noise)
| Column | Type | Description | Why it matters |
|--------|------|-------------|----------------|
| `median_coadd_snr_b` | float32 | Median S/N in B-band | Data quality per band |
| `median_coadd_snr_r` | float32 | Median S/N in R-band | Data quality per band |
| `median_coadd_snr_z` | float32 | Median S/N in Z-band | Data quality per band |
| `tsnr2_qso` | float32 | Template S/N for QSO template | How well QSO template fits |
| `tsnr2_elg` | float32 | Template S/N for ELG template | How well ELG template fits |
| `tsnr2_lrg` | float32 | Template S/N for LRG template | How well LRG template fits |
| `tsnr2_bgs` | float32 | Template S/N for BGS template | How well BGS template fits |

### Derived columns (computed during processing)
| Column | Type | Description | Why it matters |
|--------|------|-------------|----------------|
| `gr_color` | float32 | g-r color (from fluxes) | Photometric classification |
| `rz_color` | float32 | r-z color | Photometric classification |
| `w1w2_color` | float32 | W1-W2 color | AGN/QSO identifier (W1-W2 > 0.8) |
| `is_point_source` | bool | morphtype == 'PSF' | Quick star/QSO flag |
| `is_star_candidate` | bool | parallax > 0.5 OR stellar colors | Galactic contamination flag |
| `classification` | string | Our rule-based class | From Pass 1 triage |
| `discovery_potential` | string | LOW/MEDIUM/HIGH/VERY_HIGH | Priority for follow-up |

---

## Total: ~45 columns per object × 17.65M objects

**Estimated output size:** ~3.2 GB in Parquet format (compressed)
**Estimated output size:** ~12 GB in CSV (uncompressed)

---

## What This Enables (that doesn't exist anywhere)

1. **Anomaly score for every DESI DR1 spectrum** — nobody has published this
2. **Latent space embeddings for 18M spectra** — enables unsupervised clustering at unprecedented scale
3. **Cross-comparison: autoencoder anomaly vs pipeline ZWARN** — are anomalies the same as pipeline failures? Or different?
4. **Color-anomaly correlation** — do spectrally anomalous objects have unusual photometric colors?
5. **Spatial anomaly map** — where on the sky are anomalies concentrated? Random or structured?
6. **Redshift-anomaly correlation** — are anomalies preferentially at high-z? Low-z? Mid-z?
7. **Morphology-anomaly correlation** — are anomalies more often point sources or extended?
8. **S/N-anomaly correlation** — critical systematic check: are anomalies just low-S/N spectra?

---

## Script Modifications Needed

The current `13_desi_dr1_gpu_inference.py` needs:
1. Also open the `redrock-*.fits` file for each healpix (same path, different prefix)
2. Save ALL objects (not just score > 5.0) — with the full column set above
3. Save latent vectors (add a forward hook to extract encoder output)
4. Compute peak residual wavelength from per-pixel reconstruction error
5. Output to Parquet format (smaller than JSON, column-oriented)
6. Save in batches of ~500K objects to avoid memory issues

---

## Community Value

This catalog would be the **first publicly available autoencoder-scored catalog of the entire DESI DR1**. Combined with the pipeline's own classifications, it creates a two-dimensional classification space:

```
                    Pipeline confident (ZWARN=0)    Pipeline uncertain (ZWARN>0)
                   ┌──────────────────────────────┬─────────────────────────────┐
  Normal spectrum  │  WELL-CLASSIFIED              │  PIPELINE FAILURE           │
  (score < 5)      │  (vast majority, ~17M)        │  (bad data, ~100K)          │
                   ├──────────────────────────────┼─────────────────────────────┤
  Anomalous        │  GENUINELY UNUSUAL            │  AMBIGUOUS                  │
  (score > 5)      │  (best discoveries, ~100K)    │  (needs manual review, ~50K)│
                   └──────────────────────────────┴─────────────────────────────┘
```

The "genuinely unusual" quadrant (high anomaly score + confident pipeline classification) is where the most scientifically interesting objects live — the pipeline THINKS it knows what they are, but our autoencoder says they're weird anyway.
