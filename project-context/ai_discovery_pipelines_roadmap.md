# AI-Enhanced Cosmological Discovery Pipelines — Roadmap

**Created:** 2026-03-24
**Author:** Houston Golden
**Status:** FUTURE — ideas preserved for development

---

## Context

The core bounce theory is now as strong as it can get without external validation (Cai confirmation or specialist in-in integral). The biggest remaining opportunity is on the DATA side: building AI-enhanced pipelines that analyze existing large cosmological datasets to discover new objects, produce novel catalogs, and extract signals that standard methods miss.

These pipelines go beyond "proving bounce" — they produce standalone scientific contributions (catalogs, anomaly maps, feature databases) that the community can use regardless of bounce physics. Some directly strengthen the f_NL measurement by finding better tracers. Others open entirely new discovery space.

---

## What Still Strengthens the Core Research

### Theory side (diminishing returns now)

| Task | Impact | Difficulty | Worth it? |
|------|--------|-----------|-----------|
| Email Cai for confirmation | Upgrades 92% → ~99% | Easy | **Yes — just send it** |
| Full in-in integral from scratch | Independent derivation | Multi-month specialist | No — polynomial proof is sufficient |
| PolySpec full pipeline | Estimator-grade r | 1-2 sessions | Medium value — 3 methods already agree |
| Exact ε correction | Narrows [1-8%] to a point | Needs all-vertex cancellation | Low — within σ regardless |

### Data side (high value, untapped)

| Task | Impact | Status |
|------|--------|--------|
| DESI catalog + enhanced tracers (F2) | Real data product | Design only |
| NaMaster miscalibration-marginalized β | Closes the 0.08° gap properly | Done at basic level |
| Higher-res frequency consistency | Tests cosmological origin | Done at NSIDE=256 |

---

## What's Available in Public Data RIGHT NOW

| Dataset | Size | What's in it | AI opportunity |
|---------|------|-------------|---------------|
| **Planck PR3/PR4 maps** | ~50 GB | Full-sky CMB T/Q/U at 9 frequencies | Anomaly detection, foreground mining, polarization artifacts |
| **ACT DR6** | ~20 GB | High-resolution CMB over 19,000 deg² | Small-scale anomalies, SZ clusters, lensing features |
| **DESI DR1** | ~100 GB | 18M+ spectroscopic targets | Rare object discovery, spectral anomalies, redshift outliers |
| **Legacy Surveys DR10** | ~100 TB (images) | 2B objects, g/r/z/W1/W2 | Morphological anomalies, rare transients, unclassified objects |
| **unWISE / unTimely** | ~50 GB | 2B IR sources, 32 time-domain epochs | Variable objects, IR transients, moving objects |
| **SPHEREx first all-sky** | TBD | First spectrophotometric all-sky survey | Entirely new parameter space |
| **Gaia DR3** | ~1 TB | 1.8B stars with astrometry + spectrophotometry | Kinematic anomalies, stellar streams, dark companions |

---

## Five Concrete AI Pipeline Concepts

### Pipeline A: CMB Anomaly Hunter

**Goal:** Train a model to identify statistically unusual patches in Planck/ACT maps that might indicate new physics or uncharacterized systematics.

**Method:**
1. Generate thousands of simulated CMB patches from known cosmology (CAMB + noise)
2. Train a CNN or vision transformer to distinguish "standard" from "anomalous"
3. Apply to real Planck/ACT patches
4. Rank by anomaly score
5. Characterize the top anomalies: known foreground? Instrument artifact? Or genuinely unexplained?

**What it could find:**
- Cold/hot spots beyond the Cold Spot
- Asymmetry signatures
- Non-Gaussian features missed by standard bispectrum estimators
- Foreground residuals that affect birefringence/bispectrum measurements
- SZ clusters or point sources below catalog thresholds

**Connection to bounce:** If the bounce imprints specific non-Gaussian patterns (the shape we now know precisely), a matched-filter anomaly detector could find them in the map before SPHEREx.

**Novelty:** "AI-driven CMB anomaly catalog" — no one has done a systematic ML anomaly scan of Planck patches at this scale.

**Compute:** RunPod GPU for training CNN/ViT; CPU for inference and map processing. ~2-4 sessions to build.

**Paper potential:** Standalone discovery paper if interesting anomalies are found.

---

### Pipeline B: Spectral Anomaly Miner in DESI (RECOMMENDED FIRST)

**Goal:** Find spectroscopically unusual objects in DESI DR1 that don't fit any standard template.

**Method:**
1. Build a baseline spectral autoencoder on the full DESI spectroscopic sample
2. Objects with high reconstruction error are "anomalous"
3. Cluster the anomalies by type
4. Cross-match with imaging (Legacy Surveys), variability (unTimely), and X-ray/radio catalogs
5. Characterize: new QSO types? Unusual emission lines? Gravitational lens candidates? Unknown class?

**What it could find:**
- Rare QSO populations useful for PNG (high-bias tracers we're missing)
- Unusual galaxy types at high redshift
- Gravitational lens candidates
- Objects with redshift discrepancies (interesting for cosmology)
- Emission-line objects that challenge standard galaxy evolution models

**Connection to bounce:** Better high-z tracers directly improve f_NL constraints. Finding new high-bias populations could tighten σ(f_NL) before SPHEREx.

**Novelty:** "First systematic spectral anomaly catalog from DESI DR1" — the data is brand new.

**Compute:** RunPod GPU for autoencoder training; CPU for cross-matching. ~3-5 sessions to build.

**Paper potential:** Strong — DESI DR1 is the hottest new dataset in cosmology.

---

### Pipeline C: Polarization Feature Extractor

**Goal:** Use a fine-tuned model to extract subtle polarization signals from CMB maps that standard estimators might miss.

**Method:**
1. Train on simulated polarization maps with injected signals (birefringence, cosmic strings, defects, patchy reionization)
2. Fine-tune to detect specific signatures at different angular scales
3. Apply to real Planck/ACT polarization data
4. Score each patch for different signal types
5. Produce a "polarization feature catalog" ranked by signal type and confidence

**What it could find:**
- Birefringence at different angular scales (scale-dependent rotation)
- B-mode anomalies beyond lensing
- Cosmic string or defect signatures in polarization
- Patchy reionization signals
- Systematic artifacts that contaminate standard analyses

**Connection to bounce:** The ALP birefringence prediction (β = 0.27°) might have scale dependence that a standard uniform-rotation estimator misses. A scale-dependent analysis could be more sensitive.

**Novelty:** "AI-extracted multi-scale polarization feature catalog from Planck and ACT."

**Compute:** RunPod GPU for training; already have Planck maps on the pod. ~4-6 sessions.

**Paper potential:** High if scale-dependent birefringence is found.

---

### Pipeline D: Cross-Survey Anomaly Correlator

**Goal:** Find objects/regions that are anomalous in MULTIPLE datasets simultaneously — the intersection of CMB anomalies, galaxy survey anomalies, and IR anomalies at the same sky position.

**Method:**
1. Run anomaly detectors independently on CMB (Planck/ACT), optical (Legacy/DESI), and IR (unWISE)
2. Cross-match by sky position
3. Objects/regions that are anomalous in 2+ surveys are the most interesting
4. Characterize: is the multi-survey anomaly explained by a known physical process, or genuinely new?

**What it could find:**
- Galaxy clusters with unusual SZ + optical + IR properties
- Foreground regions that contaminate multiple cosmological measurements
- Cosmic voids with unexpected properties
- Regions where the ISW effect is anomalous
- Objects that are unusual in spectral, morphological, AND variability space simultaneously

**Connection to bounce:** A bounce would produce correlated signatures across scales — the bispectrum affects both CMB and LSS. Regions where both the CMB and galaxy distribution are anomalous in the same direction could be indirect evidence.

**Novelty:** "First multi-survey AI anomaly correlation catalog."

**Compute:** Requires outputs from Pipelines A-C. ~2-3 sessions on top of those.

**Paper potential:** Very high — multi-survey anomaly correlation is an unexplored methodology.

---

### Pipeline E: Time-Domain Cosmological Transient Finder (RECOMMENDED SECOND)

**Goal:** Use unTimely's 32 IR epochs to find objects that change in ways that no standard astrophysical model predicts.

**Method:**
1. Build light-curve feature vectors for all ~2B unWISE sources across 32 epochs
2. Train a variability classifier (known variable types: QSOs, RR Lyrae, eclipsing binaries, etc.)
3. The "none of the above" category is the science gold
4. Cross-match with optical (Legacy), spectroscopic (DESI), and X-ray (eROSITA) catalogs
5. Rank by "unexplainedness"

**What it could find:**
- Changing-look AGN (cosmologically useful high-bias tracers)
- Tidal disruption events at unusual redshifts
- IR transients with no optical counterpart (dusty, high-z, or genuinely new)
- Objects that appeared or disappeared between WISE epochs (very rare)
- Microlensing events from dark matter substructure

**Connection to bounce:** Variable QSOs at high z are the best tracers for PNG. Finding more of them directly improves our f_NL sensitivity.

**Novelty:** This is exactly the "Paz-style" discovery pipeline — a Caltech student found 1.5M variable objects in NEOWISE. We can do the same with better models.

**Compute:** RunPod GPU for classifier training; CPU for feature engineering on 2B sources. ~4-6 sessions.

**Paper potential:** Strong standalone discovery paper. The Paz precedent shows this can get major attention.

---

## Recommended Build Order

| Priority | Pipeline | Why first? |
|----------|---------|-----------|
| **1** | **B (DESI spectral anomalies)** | Directly feeds f_NL. DESI DR1 is new. Autoencoder methodology is well-understood. |
| **2** | **E (unTimely transients)** | Directly feeds f_NL via better tracers. "Paz-style" discovery potential. |
| **3** | **A (CMB anomaly hunter)** | Maps already on pod. Connects to birefringence + bispectrum work. |
| **4** | **C (polarization features)** | Higher novelty but harder validation. Scale-dependent birefringence is speculative. |
| **5** | **D (cross-survey correlator)** | Requires outputs from A-C. Highest ceiling but most complex. |

---

## Standards for All Pipelines

Every pipeline follows the same validation framework as our existing work:
1. **Baseline first** — reproduce known catalogs/classifications before claiming improvements
2. **Injection/recovery** — inject known signals, verify recovery
3. **Null tests** — run on scrambled/shuffled data, verify no false positives
4. **Holdout validation** — spatial/temporal splits, not random splits
5. **Bias audit** — test for correlations with survey artifacts (depth, seeing, dust, stars)
6. **Model card** — document every trained model with architecture, training data, limitations
7. **Honest reporting** — if the ML doesn't help, say so and keep the baseline

---

## Connection to the Bigger Research Program

These pipelines transform the BigBounce program from:
> "A theoretical prediction waiting for SPHEREx"

To:
> "An active observational research program producing novel catalogs, discovering new objects, and improving the sensitivity of current data to the bounce prediction — while also contributing standalone astrophysical discoveries."

This is the difference between a speculative theory paper and a research program that produces data products the community uses.
