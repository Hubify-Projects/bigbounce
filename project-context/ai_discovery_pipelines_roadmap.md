# AI-Enhanced Cosmological Discovery Pipelines — Hardened Roadmap v2

**Created:** 2026-03-24
**Updated:** 2026-03-24 (hardened with 12-gate publication standards)
**Author:** Houston Golden
**Status:** FUTURE — ideas preserved for development

---

## Mission Statement

> We are not just building AI models. We are building audited, survey-scale scientific extraction pipelines that turn existing cosmological archives into calibrated catalogs, validated anomaly products, and improved tracer sets for present-day cosmology.

---

## Context

The core bounce theory is now as strong as it can get without external validation (Cai confirmation or specialist in-in integral). The biggest remaining opportunity is on the DATA side: building AI-enhanced pipelines that analyze existing large cosmological datasets to discover new objects, produce novel catalogs, and extract signals that standard methods miss.

These pipelines go beyond "proving bounce" — they produce standalone scientific contributions (catalogs, anomaly maps, feature databases) that the community can use regardless of bounce physics. Some directly strengthen the f_NL measurement by finding better tracers. Others open entirely new discovery space.

---

## Gold Standard: The Pattern to Follow

The kid's (Paz) pipeline was rigorous because it followed this order:

**huge archive → right scientific object representation → real + synthetic supervision → task-matched model → archive-scale inference → candidate catalog → validation against known classes / follow-up**

Our chirality pipeline is getting strong because it now has the same ingredients: real survey-scale data, explicit class structure, external benchmark catalogs, bias audits, calibration, production post-processing.

That same rigor is now the **master standard** for Pipelines A–E.

---

## 12-Gate Publication Standard

Every pipeline must pass ALL 12 gates before any result is called real.

### Gate 1: Scientific Object Definition

Do not model raw data generically. Each pipeline must define the actual scientific object:
- anomaly patch (Pipeline A)
- spectral residual object (Pipeline B)
- polarization feature object (Pipeline C)
- multi-survey anomaly object (Pipeline D)
- time-domain light curve object (Pipeline E)

If the "object" is fuzzy, the pipeline will drift into AI slop.

### Gate 2: Benchmark Reproduction First

Before claiming a new model helps, reproduce at least one known baseline:
- known cluster catalog recovery
- known variable class recovery
- known spectral class recovery
- known EB null
- known Planck/ACT anomaly benchmark if relevant

**No benchmark reproduction = no trust.**

### Gate 3: Synthetic / Injected Signal Suite

Every pipeline needs injections:
- synthetic anomalies
- injected point sources / SZ / non-Gaussian features
- synthetic spectra with known line weirdness
- injected polarization rotations / defects
- synthetic multi-survey coincidences
- synthetic variable light curves

**Non-negotiable.**

### Gate 4: Null Tests

Run the exact pipeline on:
- scrambled sky positions
- shuffled labels
- phase-scrambled maps
- time-shuffled light curves
- metadata-only baselines
- random controls

The model must fail cleanly on nonsense.

### Gate 5: Holdout Validation

Never rely on random train/test only. Use:
- survey holdouts
- sky-region holdouts
- time holdouts
- instrument holdouts
- redshift holdouts
- quality-regime holdouts

This is how you catch hidden leakage.

### Gate 6: Selection-Function / Nuisance Audit

Every pipeline must test whether it is secretly learning:
- depth
- dust
- seeing
- PSF
- stellar density
- sky footprint
- detector quirks
- scan strategy
- redshift completeness
- background gradients

**This is the biggest place most astronomy ML fails.**

### Gate 7: Calibration, Not Just Accuracy

Every score must mean something. Require:
- reliability diagrams
- ECE (Expected Calibration Error)
- Brier score
- confidence-stratified precision
- abstention curves

A discovery catalog without calibrated uncertainty is weak.

### Gate 8: External Comparison

Compare against:
- known catalogs
- alternative methods
- literature benchmarks
- simple baselines

If your fancy model cannot beat or at least explain a simpler method, that matters.

### Gate 9: Human Review Loop

Top candidates, disagreements, and failures must be human-audited. Not the whole archive — but:
- top anomalies
- high-confidence novel candidates
- disagreement sets
- calibration failures

### Gate 10: Catalog Schema + Provenance

Every output object needs:
- unique ID
- probabilities / scores
- QC flags
- provenance
- survey source
- version
- model version
- processing notes

If you cannot release a clean catalog, the pipeline is not mature.

### Gate 11: Red-Team Report

Every pipeline gets a "why this might be wrong" report. That should include:
- likely leakage routes
- astrophysical confounders
- instrument/systematic confounders
- what would falsify the claim

### Gate 12: Claim Taxonomy

Standard status ladder:
- `IDEA`
- `PROTOTYPE`
- `BASELINE_REPRODUCED`
- `INJECTION_VALIDATED`
- `NULL_VALIDATED`
- `ROBUSTNESS_PARTIAL`
- `ROBUSTNESS_PASSED`
- `CATALOG_READY`
- `PAPER_READY`

**Nothing jumps from "good looking" to "paper-ready."**

---

## Pipeline Standards Card (Required Before Starting)

Before starting any new pipeline, create a one-page card with:
- Scientific object
- Known benchmark to reproduce
- Synthetic injection plan
- Null test plan
- Holdout plan
- Nuisance/leakage audit
- External comparison target
- Final catalog schema
- Fail conditions
- Claim language limits

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

## Pipeline A: CMB Anomaly Hunter

**Goal:** Train a model to identify statistically unusual patches in Planck/ACT maps that might indicate new physics or uncharacterized systematics.

**Scientific object:** Anomaly patch — a localized region of the CMB sky with statistical properties inconsistent with the fiducial ΛCDM + known foregrounds + instrument noise model.

### Method
1. Generate thousands of simulated CMB patches from known cosmology (CAMB + noise)
2. Train a CNN or vision transformer to distinguish "standard" from "anomalous"
3. Apply to real Planck/ACT patches
4. Rank by anomaly score
5. Characterize the top anomalies: known foreground? Instrument artifact? Or genuinely unexplained?

### What it could find
- Cold/hot spots beyond the Cold Spot
- Asymmetry signatures
- Non-Gaussian features missed by standard bispectrum estimators
- Foreground residuals that affect birefringence/bispectrum measurements
- SZ clusters or point sources below catalog thresholds

### Connection to bounce
If the bounce imprints specific non-Gaussian patterns (the shape we now know precisely), a matched-filter anomaly detector could find them in the map before SPHEREx.

### Hardening Requirements

**Do not train on "standard vs anomalous" too vaguely.** Define anomaly families:
- cold/hot spots
- point-source residuals
- SZ-like compact decrements
- non-Gaussian blob patterns
- anisotropic residual textures
- parity-odd injected templates

**Simulation realism must be brutal.** Simulations need:
- ΛCDM realizations
- beam
- mask effects
- anisotropic noise
- foreground residuals
- component-separation artifacts
- realistic patch boundaries

**Use retrieval, not just anomaly scores.** For each high-scoring patch, output:
- top similar simulated failure mode
- likely class
- uncertainty
- neighboring patch context

**Benchmark on known objects first.** Can the model recover:
- known SZ clusters
- strong point sources
- known problematic residual regions
- Cold Spot-like features

**Critical null:** Run on phase-scrambled and Gaussianized maps and make sure "anomalies" collapse.

### Claim Standard

No claim of "new physics anomaly" unless:
- it survives mask changes
- it survives frequency splits
- it is not explained by known foreground/systematic families
- it is significant relative to realistic simulation ensembles

### Output
- **CMB anomaly catalog** with anomaly type, score, likely explanation, and follow-up priority
- **Systematic-risk map** flagging regions that may contaminate other analyses

### Compute
RunPod GPU for training CNN/ViT; CPU for inference and map processing. ~2-4 sessions.

### Paper Potential
Standalone discovery paper if interesting anomalies are found.

---

## Pipeline B: Spectral Anomaly Miner in DESI (RECOMMENDED FIRST)

**Goal:** Find spectroscopically unusual objects in DESI DR1 that don't fit any standard template.

**Scientific object:** Spectral residual object — a DESI spectrum whose reconstruction error under a standard spectral model exceeds a calibrated threshold, after controlling for SNR and reduction artifacts.

### Method
1. Build a baseline spectral autoencoder on the full DESI spectroscopic sample
2. Objects with high reconstruction error are "anomalous"
3. Cluster the anomalies by type
4. Cross-match with imaging (Legacy Surveys), variability (unTimely), and X-ray/radio catalogs
5. Characterize: new QSO types? Unusual emission lines? Gravitational lens candidates? Unknown class?

### What it could find
- Rare QSO populations useful for PNG (high-bias tracers we're missing)
- Unusual galaxy types at high redshift
- Gravitational lens candidates
- Objects with redshift discrepancies (interesting for cosmology)
- Emission-line objects that challenge standard galaxy evolution models

### Connection to bounce
Better high-z tracers directly improve f_NL constraints. Finding new high-bias populations could tighten σ(f_NL) before SPHEREx.

### Hardening Requirements

**Start with reconstruction baselines:**
- PCA baseline
- classical autoencoder
- denoising autoencoder
- transformer/sequence model only if it materially improves retrieval

**Normalize spectra carefully.** If preprocessing is sloppy, anomaly results are meaningless. Require consistent:
- wavelength grids
- bad-pixel handling
- flux scaling
- SNR handling
- sky-line masking

**Define anomaly types after detection.** Do not just produce a ranked list. Cluster anomalies into:
- emission-line weirdos
- broad-line oddities
- redshift mismatch objects
- lens candidates
- calibration artifacts
- reduction failures

**Benchmark on known rare classes.** Can it recover:
- known quasars with unusual lines
- broad absorption line objects
- known lens candidates
- strong redshift failures
- reduction artifacts

**Artifact audit.** Make sure it is not just finding:
- low SNR junk
- bad sky subtraction
- truncated spectra
- reduction glitches

**Tracer utility branch.** Add a second score:
- not just anomalousness
- but **PNG tracer utility potential** so the output can directly feed the f_NL work

### Claim Standard

The paper should not just say "we found weird DESI spectra." It should say:
- baseline reproduced
- anomaly classes validated
- artifact contamination quantified
- high-z tracer subset identified
- catalog released

### Output
Two catalogs:
- **DESI spectral anomaly catalog**
- **DESI high-bias tracer candidate catalog** (directly feeds f_NL)

### Compute
RunPod GPU for autoencoder training; CPU for cross-matching. ~3-5 sessions.

### Paper Potential
Strong — DESI DR1 is the hottest new dataset in cosmology.

---

## Pipeline C: Polarization Feature Extractor

**Goal:** Use a fine-tuned model to extract subtle polarization signals from CMB maps that standard estimators might miss.

**Scientific object:** Polarization feature object — a map patch where the EB, BB, or rotation signal departs from the null (or uniform-rotation) expectation at a calibrated significance level, with systematic alternatives explicitly scored.

### Method
1. Train on simulated polarization maps with injected signals (birefringence, cosmic strings, defects, patchy reionization)
2. Fine-tune to detect specific signatures at different angular scales
3. Apply to real Planck/ACT polarization data
4. Score each patch for different signal types
5. Produce a "polarization feature catalog" ranked by signal type and confidence

### What it could find
- Birefringence at different angular scales (scale-dependent rotation)
- B-mode anomalies beyond lensing
- Cosmic string or defect signatures in polarization
- Patchy reionization signals
- Systematic artifacts that contaminate standard analyses

### Connection to bounce
The ALP birefringence prediction (β = 0.27°) might have scale dependence that a standard uniform-rotation estimator misses. A scale-dependent analysis could be more sensitive.

### Hardening Requirements

**Separate tasks.** Do not train one vague "feature extractor." Train task-specific heads for:
- uniform birefringence
- scale-dependent rotation
- cosmic strings / defects
- patchy reionization-like structure
- foreground/systematic classes

**Null-first discipline.** Before touching real maps:
- EB null on simulations
- injected rotation recovery
- miscalibration nuisance recovery
- dropped-frequency robustness

**Systematics-aware training.** Include injected nuisance structure:
- angle miscalibration
- polarized dust mismatch
- beam mismatch
- masking artifacts

**Frequency split logic.** No serious feature claim without checking frequency behavior.

**Map patch catalog.** Like Pipeline A, output patch-level objects, not just a final score.

### Claim Standard

No "scale-dependent birefringence" language unless:
- nulls are passed
- miscalibration nuisance is explicitly modeled
- the feature survives frequency and mask changes
- injected known rotations are recovered without bias

### Output
- **Polarization feature catalog**
- **Rotation-likelihood map**
- **Systematic-risk map**

### Compute
RunPod GPU for training; already have Planck maps on the pod. ~4-6 sessions.

### Paper Potential
High if scale-dependent birefringence is found.

---

## Pipeline D: Cross-Survey Anomaly Correlator

**Goal:** Find objects/regions that are anomalous in MULTIPLE datasets simultaneously — the intersection of CMB anomalies, galaxy survey anomalies, and IR anomalies at the same sky position.

**Scientific object:** Multi-survey anomaly object — a sky position or object where two or more independent anomaly detectors (from different surveys) both flag unusual behavior, at a rate exceeding the expected false-coincidence rate from random alignment and selection overlap.

### Method
1. Run anomaly detectors independently on CMB (Planck/ACT), optical (Legacy/DESI), and IR (unWISE)
2. Cross-match by sky position
3. Objects/regions that are anomalous in 2+ surveys are the most interesting
4. Characterize: is the multi-survey anomaly explained by a known physical process, or genuinely new?

### What it could find
- Galaxy clusters with unusual SZ + optical + IR properties
- Foreground regions that contaminate multiple cosmological measurements
- Cosmic voids with unexpected properties
- Regions where the ISW effect is anomalous
- Objects that are unusual in spectral, morphological, AND variability space simultaneously

### Connection to bounce
A bounce would produce correlated signatures across scales — the bispectrum affects both CMB and LSS. Regions where both the CMB and galaxy distribution are anomalous in the same direction could be indirect evidence.

### Hardening Requirements

**Require calibrated anomaly scores from A/B/C/E.** Do not correlate raw uncalibrated rankings.

**Use sky-position nulls.** Randomize positions to estimate false multi-survey coincidence rates.

**Model selection effects explicitly.** Some surveys are deeper in some regions. Coincidence rates are not uniform.

**Build anomaly tuples.** Each matched object/region should store:
- anomaly scores by survey
- object types
- angular separation
- counterpart confidence
- likely known explanation

**Use control populations.** Compare anomaly-anomaly matches to:
- random sky control
- normal-object control
- matched-depth control

### Claim Standard

No "multi-survey anomaly" claim unless coincidence exceeds what is expected from:
- random alignment
- footprint overlap
- selection bias
- known object classes

### Output
- **Cross-survey anomaly coincidence catalog** with expected false-match probability per entry

### Compute
Requires outputs from Pipelines A-C. ~2-3 sessions on top of those.

### Paper Potential
Very high — multi-survey anomaly correlation is an unexplored methodology.

---

## Pipeline E: Time-Domain Cosmological Transient Finder (RECOMMENDED SECOND)

**Goal:** Use unTimely's 32 IR epochs to find objects that change in ways that no standard astrophysical model predicts.

**Scientific object:** Time-domain light curve object — a source in the unTimely catalog whose multi-epoch IR flux variation is inconsistent with all standard variability classes (QSO, RR Lyrae, eclipsing binary, AGN, moving object) at a calibrated confidence level, after artifact rejection.

### Method
1. Build light-curve feature vectors for all ~2B unWISE sources across 32 epochs
2. Train a variability classifier (known variable types: QSOs, RR Lyrae, eclipsing binaries, etc.)
3. The "none of the above" category is the science gold
4. Cross-match with optical (Legacy), spectroscopic (DESI), and X-ray (eROSITA) catalogs
5. Rank by "unexplainedness"

### What it could find
- Changing-look AGN (cosmologically useful high-bias tracers)
- Tidal disruption events at unusual redshifts
- IR transients with no optical counterpart (dusty, high-z, or genuinely new)
- Objects that appeared or disappeared between WISE epochs (very rare)
- Microlensing events from dark matter substructure

### Connection to bounce
Variable QSOs at high z are the best tracers for PNG. Finding more of them directly improves our f_NL sensitivity.

### Hardening Requirements

**Build proper light-curve objects.** Not just epoch vectors. Include:
- flux
- uncertainty
- cadence gaps
- quality flags
- variability features
- contextual colors / crossmatches

**Known-class benchmark first.** Recover:
- QSOs
- RR Lyrae
- eclipsing binaries
- AGN
- moving objects if relevant
- common nuisance classes

**Synthetic injection.** Inject:
- changing-look AGN
- long-timescale drifts
- dusty transients
- appearing/disappearing sources
- cadence-challenged signals

**Artifact rejection.** Huge issue here:
- blending
- moving-object confusion
- image subtraction failures
- detector artifacts
- low-SNR fluctuations

**Explainability.** For each "none of the above" source, output:
- best known-class mismatch
- why it is out-of-distribution
- cross-survey context

**Tracer utility score.** Like B, assign:
- anomaly score
- **high-z tracer usefulness score**

### Claim Standard

Do not just say "we found unexplained IR transients." Say:
- known classes recovered
- artifact contamination quantified
- crossmatched follow-up context added
- tracer-enrichment subset produced

### Output
Two catalogs:
- **Time-domain anomaly catalog**
- **Variability-selected cosmology tracer catalog** (directly feeds f_NL)

### Compute
RunPod GPU for classifier training; CPU for feature engineering on 2B sources. ~4-6 sessions.

### Paper Potential
Strong standalone discovery paper. The Paz precedent shows this can get major attention.

---

## Recommended Build Order

| Priority | Pipeline | Why first? |
|----------|---------|-----------|
| **1** | **B (DESI spectral anomalies)** | Directly feeds f_NL. DESI DR1 is new. Autoencoder methodology is well-understood. |
| **2** | **E (unTimely transients)** | Directly feeds f_NL via better tracers. "Paz-style" discovery potential. |
| **3** | **A (CMB anomaly hunter)** | Maps already on pod. Connects to birefringence + bispectrum work. |
| **4** | **C (polarization features)** | Higher novelty but harder validation. Scale-dependent birefringence is speculative. |
| **5** | **D (cross-survey correlator)** | Requires outputs from A-C. Highest ceiling but most complex. |

That order is right because:
- B and E most directly feed f_NL
- A and C are more validation-heavy
- D depends on the others being mature

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

## Connection to the Bigger Research Program

These pipelines transform the BigBounce program from:

> "A theoretical prediction waiting for SPHEREx"

To:

> "An active observational research program producing novel catalogs, discovering new objects, and improving the sensitivity of current data to the bounce prediction — while also contributing standalone astrophysical discoveries."

This is the difference between a speculative theory paper and a research program that produces data products the community uses.
