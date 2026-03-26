# Next Research Paths — Complete Inventory

**Created:** 2026-03-26
**Purpose:** Single source of truth for ALL planned research paths, pipelines, computations, and ideas. Ranked by novelty, feasibility, and impact.

---

## TIER 1: In Progress (actively running or nearly complete)

### 1.1 Enhanced 18M DESI DR1 Catalog
- **Status:** RUNNING on H200 (36%, ~20 hours remaining)
- **What:** 45-column catalog of ALL 17.9M DESI spectra with latent vectors, redshifts, photometry
- **Novel?** YES — first autoencoder-scored catalog of full DESI DR1
- **Next:** Pull completed batches, aggregate analysis, community release
- **Paper:** Part of Paper 3 (anomaly catalog) or standalone Paper 5

### 1.2 Galaxy Chirality Catalog (8.47M)
- **Status:** RUNNING on H100 (82%, ~10 hours remaining)
- **What:** CW/CCW/NOT_SPIRAL classification of 8.47M galaxies, bias-audited
- **Novel?** YES — largest bias-audited handedness catalog (40x Shamir)
- **Next:** Complete inference, generate calibrated tier, parity analysis
- **Paper:** Standalone chirality paper

### 1.3 Paper 3: Anomaly Catalog
- **Status:** Draft v0.1 exists (2,800 words), needs spectral inspection + injection/recovery
- **What:** "195,829 Spectral Anomalies from DESI DR1" for ApJS
- **Novel?** YES — scale (90x prior), cross-reference (6 databases), galaxy 20x finding
- **Next:** Spectral inspection of top 50, artifact rejection, injection test
- **Remaining gaps:** B-dominant investigation, actual DESI spectrum plots, architecture docs

---

## TIER 2: Ready to Execute (scripts/data exist, just need to run)

### 2.1 Planck CMB Lensing × Anomaly Cross-Correlation
- **Status:** NOT STARTED — planning only
- **What:** Cross-correlate 195K anomaly positions with Planck CMB lensing convergence map
- **Novel?** YES — nobody has done this with AI-detected spectral anomalies
- **Why it matters:** If anomalies correlate with CMB lensing → they're real extragalactic sources at specific redshifts (independent artifact rejection). If not → possible instrumental artifacts.
- **Data needed:** Planck PR4 lensing convergence map (public, ~1GB download)
- **Compute:** Local Python, ~2 hours
- **Impact:** HIGH — independent validation of anomaly catalog + potential angular power spectrum measurement
- **Paper:** Strengthens Paper 3

### 2.2 NANOGrav Proper Spectral Fit
- **Status:** Preliminary (γ=3 comparison done, proper fit not done)
- **What:** Fit NANOGrav 15-year free-spectrum data with matter-bounce induced GW template
- **Novel?** PARTIALLY — the γ comparison is novel, the fit adds rigor
- **Data needed:** NANOGrav 15-year data products (public)
- **Compute:** Local Python, ~1 hour
- **Impact:** MEDIUM — strengthens the NANOGrav consistency claim
- **Paper:** Could be standalone short paper or section in Paper 1

### 2.3 SDSS DR18 Anomaly Scan (Cross-Validation)
- **Status:** BLOCKED (SDSS API still down)
- **What:** Run same autoencoder methodology on 5M SDSS spectra
- **Novel?** YES — cross-survey validation of anomaly detection methodology
- **Why it matters:** If same anomaly types/rates appear in SDSS → methodology is robust and survey-independent
- **Compute:** Need to retrain autoencoder on SDSS spectral format, then H200 inference
- **Impact:** HIGH for methodology validation
- **Paper:** Strengthens Paper 3 or standalone methodology paper

### 2.4 Full Cross-Match of ALL 195K (remaining databases)
- **Status:** Top 1K-10K done for 6 databases. SDSS and full 195K still pending.
- **What:** Cross-match entire 195K against all catalogs at full depth
- **Compute:** CDS bulk xMatch when service recovers, or individual TAP queries (~days)
- **Impact:** CRITICAL for honest discovery claims
- **Blocker:** CDS bulk service down, SDSS API down

### 2.5 DESI Spectra Download + Visual Inspection (Top 50)
- **Status:** Analysis exists from band residuals, but actual DESI spectra NOT downloaded
- **What:** Download the raw FITS spectra for top 50 anomalies, plot flux vs wavelength with autoencoder reconstruction overlay
- **Novel?** Required for publication — not optional
- **Compute:** Download ~50 FITS files from DESI archive, Python plotting
- **Impact:** CRITICAL — we cannot publish without knowing what the spectra look like

---

## TIER 3: Planned (needs development work before execution)

### 3.1 Second Autoencoder on Anomalies (Anomaly-within-Anomaly)
- **Status:** IDEA — not started
- **What:** Train a SECOND autoencoder on the 195K anomalies themselves. Objects that are anomalous AMONG anomalies are the most extreme outliers.
- **Novel?** YES — recursive anomaly detection at survey scale
- **Why it matters:** The current 195K includes artifacts and mildly unusual objects. A second-level model could isolate the truly novel objects.
- **Compute:** GPU training (~4 hours), inference on 195K (~30 min)
- **Impact:** MEDIUM-HIGH — could identify the most scientifically interesting objects

### 3.2 LLM Deep Analysis of Top 100
- **Status:** Rule-based analysis done. LLM analysis NOT done.
- **What:** Use Claude/GPT-4o API to analyze each of top 100 with full context (band residuals + Legacy Survey image + cross-match results + DESI metadata)
- **Novel?** The LLM analysis itself isn't novel. The SCALE + CONTEXT is.
- **Compute:** ~$5-15 API cost, ~1 hour
- **Impact:** MEDIUM — produces the most readable and insightful object descriptions

### 3.3 Injection/Recovery Test
- **Status:** NOT DONE — required for Paper 3 publication
- **What:** Inject known unusual spectra (BAL QSOs, double-peaked emitters, etc.) into DESI format. Run through autoencoder. Measure recovery rate.
- **Novel?** Standard methodology requirement
- **Compute:** Local Python, ~4 hours
- **Impact:** CRITICAL for publication — reviewers will demand this

### 3.4 B-Dominant Investigation
- **Status:** NOT DONE — required for Paper 3
- **What:** 44K anomalies (23%) have B-band dominant residuals. Is this a blue-end calibration artifact or genuine? Check correlation with fiber number, observation date, airmass, moon phase.
- **Compute:** Need DESI observation metadata (from FIBERMAP in the enhanced 18M catalog)
- **Impact:** CRITICAL — if B-dominant = artifact, our anomaly count drops from 195K to ~150K

### 3.5 Anomaly Density vs Survey Density Map
- **Status:** NOT DONE — enabled by enhanced 18M catalog
- **What:** Compare anomaly RATE per sky region vs total survey density. Uniform rate → no spatial signal. Non-uniform → systematic or physical cause.
- **Compute:** Once 18M catalog complete, ~2 hours local
- **Impact:** HIGH — either confirms isotropy or reveals spatial structure

---

## TIER 4: Future (needs significant development or new data)

### 4.1 Super-Resolution Image Enhancement
- **Status:** IDEA — detailed feasibility in future_plans_anomaly_pipeline.md
- **What:** Train AI to upscale Legacy Survey cutouts to HST/JWST resolution using paired training data from COSMOS/CEERS/JADES fields
- **Novel?** YES — no published ground→space super-resolution for astronomy at scale
- **Training data:** HST COSMOS (~100K paired images), JWST CEERS/JADES
- **Compute:** H200 training 2-4 days (~$50-100), inference 1 hour
- **Impact:** HIGH visibility, MEDIUM science (enhanced images aren't authoritative)
- **Paper:** Standalone methodology paper

### 4.2 Pipeline E: Time-Domain Transient Finder
- **Status:** NOT STARTED — queued in roadmap
- **What:** Use unTimely 32-epoch IR data to find objects with unusual variability
- **Novel?** YES — Paz-style discovery paper
- **Compute:** GPU training + 2B source feature extraction
- **Impact:** HIGH standalone, feeds Pipeline 1 with QSO candidates

### 4.3 Pipeline A: CMB Anomaly Hunter
- **Status:** NOT STARTED
- **What:** Train CNN/ViT to find anomalous patches in Planck/ACT CMB maps
- **Compute:** GPU training, CPU inference
- **Impact:** MEDIUM — depends on whether anomalies are found

### 4.4 Pipeline C: Polarization Feature Extractor
- **Status:** NOT STARTED
- **What:** AI-based search for scale-dependent birefringence in CMB polarization
- **Compute:** Planck/ACT Q/U maps
- **Impact:** HIGH if scale-dependent signal found

### 4.5 Quintom f_NL Rigorous Computation
- **Status:** Analytic argument complete, phantom analysis done
- **What:** Full numerical in-in integral through quintom bounce with phantom perturbations
- **Novel?** YES — no f_NL for any quintom bounce in literature
- **Compute:** Numerical integration, ~1 day of focused theory work
- **Impact:** VERY HIGH if f_NL confirmed = -35/8 (fills literature gap)
- **Paper:** Paper 4 (quintom f_NL + bounce-DE unification)

### 4.6 Euclid Spectral Anomaly Pipeline
- **Status:** FUTURE — Euclid data not yet public at scale
- **What:** Apply same autoencoder methodology to Euclid slitless spectroscopy (~30M galaxies)
- **Novel?** YES — first anomaly detection on Euclid spectroscopy
- **Impact:** VERY HIGH — Euclid is the next major survey after DESI

### 4.7 DESI Spectra for Bounce-Specific Signatures
- **Status:** IDEA
- **What:** Search DESI spectra specifically for objects at redshifts where f_NL = -35/8 creates maximal scale-dependent bias. Pre-identify the most useful SPHEREx tracers.
- **Compute:** Filter enhanced 18M catalog by redshift + bias, cross-match with SPHEREx survey plan
- **Impact:** MEDIUM — preparatory work for SPHEREx era

### 4.8 ACT DR6 Birefringence with AI-Improved Masks
- **Status:** IDEA (Pipeline C variant)
- **What:** Use autoencoder to identify contaminated regions in ACT polarization maps, re-measure β with cleaner masks
- **Novel?** YES — AI-assisted systematic control for CMB birefringence
- **Impact:** HIGH if measurement shifts significantly

---

## SUMMARY TABLE

| # | Path | Status | Novel? | Compute | ETA | Paper |
|---|------|--------|--------|---------|-----|-------|
| 1.1 | Enhanced 18M | RUNNING | YES | H200 | 20h | 3/5 |
| 1.2 | Chirality 8.47M | RUNNING | YES | H100 | 10h | Standalone |
| 1.3 | Paper 3 draft | IN PROGRESS | YES | Local | 4-6 weeks | 3 |
| 2.1 | Planck lensing × anomalies | READY | YES | Local 2h | This week | 3 |
| 2.2 | NANOGrav fit | READY | PARTIAL | Local 1h | This week | 1 |
| 2.3 | SDSS cross-validation | BLOCKED | YES | H200 | When API up | 3 |
| 2.4 | Full 195K cross-match | PARTIAL | YES | CDS/TAP | When CDS up | 3 |
| 2.5 | Spectral inspection top 50 | READY | REQUIRED | Local | This week | 3 |
| 3.1 | Second autoencoder | IDEA | YES | GPU 4h | 1-2 weeks | 3 |
| 3.2 | LLM top 100 analysis | READY | PARTIAL | $5-15 | This week | 3 |
| 3.3 | Injection/recovery | NOT DONE | REQUIRED | Local 4h | 1-2 weeks | 3 |
| 3.4 | B-dominant investigation | NOT DONE | REQUIRED | Local | After 18M | 3 |
| 3.5 | Anomaly density map | NOT DONE | YES | Local 2h | After 18M | 3 |
| 4.1 | Super-resolution | IDEA | YES | H200 2-4d | 1-2 months | Standalone |
| 4.2 | Pipeline E (variability) | NOT STARTED | YES | GPU | 1-2 months | Standalone |
| 4.3 | Pipeline A (CMB) | NOT STARTED | YES | GPU | 2-3 months | Standalone |
| 4.4 | Pipeline C (polarization) | NOT STARTED | YES | GPU | 2-3 months | Standalone |
| 4.5 | Quintom f_NL numerical | ANALYTIC DONE | YES | CPU 1d | 2-4 weeks | 4 |
| 4.6 | Euclid pipeline | FUTURE | YES | H200 | 6+ months | Standalone |
| 4.7 | DESI bounce tracers | IDEA | PARTIAL | Local | After 18M | 2 |
| 4.8 | ACT birefringence | IDEA | YES | GPU | 2-3 months | Standalone |
