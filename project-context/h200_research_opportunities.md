# H200 Research Opportunities & Next Steps

**Created:** 2026-03-26
**Budget context:** Up to $250-500/day for 1-2 weeks ($1,750-$7,000 total)
**H200 specs:** 192 cores, 3TB RAM, 143GB VRAM, 300TB storage, ~$3-5/hr

---

## CURRENTLY RUNNING

### 1. Enhanced 18M DESI DR1 Catalog
- **Status:** 44% (7.9M/17.9M), ~16 hours remaining
- **Cost so far:** ~$50
- **Output:** 45-column Parquet catalog, first of its kind
- **When done:** Aggregate stats, pattern discovery, anomaly density map

### 2. Galaxy Chirality 8.47M
- **Status:** 86.5% (7.3M/8.47M), ~8 hours remaining on H100
- **Cost so far:** ~$40
- **Output:** Largest bias-audited handedness catalog (40x prior work)

---

## NEXT STEPS ON EXISTING RUNS (when they finish)

### On the 18M catalog:
1. **Anomaly density vs survey density map** — are anomalies uniformly distributed or clustered? (2 hours, free/local)
2. **Redshift-resolved anomaly classification** — use pipeline z values to resolve the three wavelength clusters (7600Å, 3600Å, 9440Å) (2 hours, free/local)
3. **Latent space clustering** — t-SNE/UMAP on the 128-dim latent vectors to find anomaly families (4 hours, local)
4. **Score vs ZWARN analysis** — are our anomalies the same objects the pipeline flagged? Or different? (1 hour, free/local)
5. **Anomaly rate as function of redshift** — does the 0.75% galaxy anomaly rate change with z? (1 hour, free/local)
6. **Photometric color analysis** — g-r vs W1-W2 color-color diagram for anomalies vs normals (1 hour, free/local)

### On the chirality catalog:
1. **Parity asymmetry test** — is CW/CCW ratio consistent with 50/50 or does it show a dipole? (4 hours, local)
2. **Spatial dipole search** — fit for a preferred axis in the CW-CCW asymmetry (8 hours, local)
3. **Redshift tomography** — split into z-bins and check if asymmetry evolves with redshift (4 hours, local)
4. **Cross-correlation with anomaly catalog** — are chirality outliers also spectral anomalies? (2 hours, local)

---

## NEW H200 RUNS: BOUNCE COSMOLOGY (directly supports Papers 1-2)

### B1. DESI f_NL Tracer Optimization ($15-25, 6 hours)
- **What:** Filter the 18M catalog for optimal f_NL tracer selection
- **How:** Select objects at z > 1.5 with high clustering bias (W1-W2 > 0.8, QSO-type), compute effective bias profile b(z), forecast σ(f_NL) improvement over standard DESI QSO catalog
- **Novel?** YES — AI-optimized tracer selection for PNG
- **Bounce value:** Directly improves our flagship f_NL prediction testability

### B2. Planck Lensing × Anomaly Cross-Correlation ($5-10, 2 hours)
- **What:** Cross-correlate anomaly positions with Planck CMB lensing convergence
- **How:** Download Planck PR4 kappa map, compute angular cross-power spectrum C_ℓ^{κ×anomaly}, compare with theory
- **Novel?** YES — nobody has cross-correlated AI anomalies with CMB lensing
- **Bounce value:** Independent bias measurement for f_NL forecasting

### B3. NANOGrav Spectral Template Fit ($5, 1 hour)
- **What:** Fit NANOGrav free-spectrum data with matter-bounce GW template
- **How:** Download NANOGrav 15yr data products, compute χ² for bounce vs SMBH vs strings
- **Novel?** YES — first proper template fit (we only compared γ values so far)
- **Bounce value:** Strengthens the NANOGrav consistency claim

---

## NEW H200 RUNS: ANOMALY PIPELINE ENHANCEMENT ($50-150)

### A1. Second Autoencoder on Anomalies ($20-30, 8 hours)
- **What:** Train a second BigAE on the 195K anomalies. Find anomalies-within-anomalies.
- **How:** Use anomalies as training data, then score them against this new model. Objects anomalous relative to OTHER anomalies are the most extreme.
- **Novel?** YES — recursive anomaly detection
- **Impact:** Isolates the ~1,000 most scientifically interesting objects from the 195K

### A2. Injection/Recovery with Real Model ($10-15, 4 hours)
- **What:** Run the injection/recovery test with the actual BigAE (not the proxy)
- **How:** Upload synthetic unusual spectra to H200, run through BigAE, measure completeness
- **Why:** Current proxy gives 33% — real model expected 70-90%. Required for Paper 3.
- **Impact:** CRITICAL for publication credibility

### A3. Download + Analyze ALL 195K Spectra ($30-50, 12 hours)
- **What:** Download the actual DESI FITS spectra for ALL 195K anomalies (not just top 50)
- **How:** Batch download from DESI archive, extract flux arrays, compute per-pixel residuals
- **Output:** Full spectral catalog with reconstruction overlays for every anomaly
- **Impact:** Enables automated emission line identification, artifact rejection at scale

### A4. SDSS Cross-Validation ($15-25, 8 hours)
- **What:** Retrain autoencoder on SDSS spectral format, run on 5M SDSS spectra
- **How:** Adapt BigAE for SDSS wavelength grid, train on SDSS DR18, score all 5M
- **Novel?** YES — cross-survey validation of anomaly methodology
- **Impact:** If same anomaly types/rates → methodology is survey-independent

### A5. Multi-Resolution Autoencoder ($20-30, 8 hours)
- **What:** Train autoencoder at multiple downsampling levels (8x, 16x, 32x, 64x)
- **How:** Same architecture, different input sizes (992, 496, 248, 124 bins)
- **Why:** Some anomalies might only be visible at high resolution (narrow lines) while others need broad context (continuum shape)
- **Novel?** YES — multi-scale anomaly detection on spectra

---

## NEW H200 RUNS: BROADER ASTROPHYSICS ($100-300)

### C1. Super-Resolution Training ($50-100, 2-4 days)
- **What:** Train AI to upscale Legacy Survey cutouts to HST/JWST resolution
- **How:** Download paired ground/space images from COSMOS + CEERS fields (~100K pairs), train ESRGAN/diffusion model
- **Output:** Model that generates enhanced images for any Legacy Survey position
- **Novel?** YES — first ground→space super-resolution for astronomy at scale
- **Impact:** HIGH visibility, applied to our 195K anomalies for visual discovery

### C2. Emission Line Finder ($30-50, 12 hours)
- **What:** Train a specialized model to identify and measure emission lines in DESI spectra
- **How:** Build training set from SDSS emission line catalogs (known lines), train CNN to detect line wavelength + width + flux
- **Applied to:** ALL 18M DESI spectra or the 195K anomalies
- **Output:** Automated emission line catalog with redshifts, line ratios, AGN diagnostics
- **Novel?** Partially — similar to existing spectral fitting codes but at scale with ML
- **Impact:** Provides astrophysical interpretation for every anomaly

### C3. Photometric Redshift Improvement ($25-40, 8 hours)
- **What:** Use our autoencoder latent vectors as features for improved photo-z estimation
- **How:** Train a regression head on the 128-dim latent representation → spectroscopic z
- **Novel?** YES — autoencoder-derived features for photo-z
- **Impact:** If latent vectors encode redshift information, this is a publishable methodological contribution

### C4. Galaxy Merger Finder ($30-50, 12 hours)
- **What:** Fine-tune image classifier to find merging/interacting galaxies in Legacy Survey
- **How:** Use labeled merger catalogs (SDSS Galaxy Zoo mergers) as training data, apply to Legacy Survey cutouts of our anomalies
- **Why:** Many spectral anomalies could be merger-driven (double nuclei, tidal features, unusual kinematics)
- **Novel?** Partially — merger finding is done but connecting to spectral anomalies is new

### C5. Full-Sky Anomaly Density Map ($20-30, 8 hours)
- **What:** Once 18M catalog complete, compute anomaly rate per HEALPix pixel and compare with foreground maps (dust, stellar density, exposure time)
- **How:** Divide anomaly count by total count per pixel, correlate with Planck dust, Gaia stellar density
- **Novel?** YES — spatial analysis of anomaly rate at survey scale
- **Impact:** Either confirms uniformity (no systematics) or reveals structure (real or systematic)

### C6. Spectral Anomaly Taxonomy ($40-60, 1-2 days)
- **What:** Use the 128-dim latent vectors from all 195K anomalies to build an unsupervised taxonomy
- **How:** UMAP embedding → HDBSCAN clustering → identify distinct anomaly families → characterize each family by typical spectrum, redshift, morphology
- **Output:** "There are N distinct types of spectral anomaly in DESI DR1, characterized by..."
- **Novel?** YES — first unsupervised spectral taxonomy at this scale
- **Paper:** Standalone or major section of Paper 3

---

## MULTIPLE H200 MACHINES (if scaling up)

With 2-3 H200s running simultaneously ($10-15/hr total):

### M1. Full DESI DR1 Spectral Download + Re-scoring (2 H200s, 24-48 hours, $200-400)
- Download ALL 18M spectra as raw flux arrays (not just scores)
- Re-run autoencoder at 8x resolution (992 bins instead of 496)
- Save full reconstruction + residual for every spectrum
- Enable per-pixel anomaly localization at scale

### M2. Parallel Cross-Survey Anomaly Detection (3 H200s, 48 hours, $300-500)
- H200 #1: DESI DR1 (done/running)
- H200 #2: SDSS DR18 (5M spectra, retrained autoencoder)
- H200 #3: LAMOST DR10 (20M spectra, Chinese spectroscopic survey)
- Cross-reference anomalies across 3 independent surveys
- Objects anomalous in 2+ surveys are the strongest candidates

### M3. Real-Time DESI DR2 Readiness (1 H200, ongoing)
- When DESI DR2 drops (~2026-2027): be first to run anomaly detection
- Pre-train updated autoencoder, pre-compute healpix index
- Process full DR2 within days of release
- "First AI anomaly catalog of DESI DR2" — massive citation potential

---

## COST SUMMARY

| Category | Runs | Est. Cost | Timeline |
|----------|------|-----------|----------|
| Currently running | 2 | $90 spent | 8-16h remaining |
| Next steps (local) | 10 | Free | This week |
| Bounce cosmology (H200) | 3 | $25-40 | 1-2 days |
| Anomaly enhancement (H200) | 5 | $95-170 | 1 week |
| Broader astrophysics (H200) | 6 | $195-330 | 1-2 weeks |
| Multi-H200 scale-up | 3 | $500-900 | 2-4 weeks |
| **TOTAL** | **29** | **$905-1,530** | **2-4 weeks** |

All within the $250-500/day budget over 1-2 weeks.

---

## WHAT PRODUCES THE MOST NOVEL SCIENCE PER DOLLAR

1. **Spectral taxonomy via UMAP clustering** ($40-60) — defines NEW object classes
2. **Second autoencoder on anomalies** ($20-30) — finds the most extreme objects
3. **Super-resolution training** ($50-100) — highest visibility, most shareable
4. **Injection/recovery with real model** ($10-15) — REQUIRED for publication
5. **Cross-survey SDSS validation** ($15-25) — proves methodology is robust
6. **Latent space photo-z** ($25-40) — novel ML methodology contribution
