# AI-Enhanced Cosmological Discovery Pipelines

## Hardened Roadmap v2

| | |
|---|---|
| **Created** | 2026-03-24 |
| **Updated** | 2026-03-24 — hardened with 12-gate publication standards |
| **Author** | Houston Golden |
| **Status** | Ready for execution |

---

> **Mission:** We are not just building AI models. We are building audited, survey-scale scientific extraction pipelines that turn existing cosmological archives into calibrated catalogs, validated anomaly products, and improved tracer sets for present-day cosmology.

---

## Why Now

The core bounce theory is as strong as it can get without external validation. The biggest remaining opportunity is on the **data side**: AI-enhanced pipelines that analyze existing large cosmological datasets to discover new objects, produce novel catalogs, and extract signals that standard methods miss.

These pipelines produce **standalone scientific contributions** — catalogs, anomaly maps, tracer databases — that the community can use regardless of bounce physics. Some directly strengthen the f_NL measurement. Others open entirely new discovery space.

---

## The Pattern to Follow

Paz's pipeline worked because it followed a specific order:

```
huge archive
  → right scientific object representation
    → real + synthetic supervision
      → task-matched model
        → archive-scale inference
          → candidate catalog
            → validation against known classes + follow-up
```

Our chirality pipeline follows the same structure: real survey-scale data, explicit class structure, external benchmarks, bias audits, calibration, production post-processing.

**That same rigor is the master standard for all five pipelines.**

---

## Build Order

| Priority | Pipeline | Feeds f_NL? | Standalone paper? | Sessions |
|:--------:|----------|:-----------:|:-----------------:|:--------:|
| **1** | **B — DESI Spectral Anomaly Miner** | Yes (high-bias tracers) | Yes (DESI DR1 is new) | 3–5 |
| **2** | **E — Time-Domain Transient Finder** | Yes (QSO enrichment) | Yes (Paz-style) | 4–6 |
| **3** | **A — CMB Anomaly Hunter** | Indirect | Yes (if anomalies found) | 2–4 |
| **4** | **C — Polarization Feature Extractor** | Indirect (birefringence) | Yes (if scale-dependent) | 4–6 |
| **5** | **D — Cross-Survey Anomaly Correlator** | Indirect | Yes (new methodology) | 2–3 on top of A–C |

B and E feed f_NL directly. A and C are more validation-heavy. D depends on the others being mature.

---

## Public Datasets Available Now

| Dataset | Size | Contents | Pipelines |
|---------|-----:|---------|:---------:|
| Planck PR3/PR4 | ~50 GB | Full-sky CMB T/Q/U, 9 frequencies | A, C, D |
| ACT DR6 | ~20 GB | High-res CMB, 19,000 deg² | A, C, D |
| DESI DR1 | ~100 GB | 18M+ spectroscopic targets | B, D |
| Legacy Surveys DR10 | ~100 TB | 2B objects, g/r/z/W1/W2 imaging | B, D, E |
| unWISE / unTimely | ~50 GB | 2B IR sources, 32 time-domain epochs | E, D |
| SPHEREx first all-sky | TBD | First spectrophotometric all-sky | Future |
| Gaia DR3 | ~1 TB | 1.8B stars, astrometry + spectrophotometry | E, D |

---

## 12-Gate Publication Standard

Every pipeline must pass **all 12 gates** before any result is called real.

### Gate 1 — Scientific Object Definition

Each pipeline defines a specific scientific object, not raw data:

| Pipeline | Scientific Object |
|----------|------------------|
| A | **Anomaly patch** — localized CMB region inconsistent with ΛCDM + foregrounds + noise |
| B | **Spectral residual object** — DESI spectrum with high reconstruction error after artifact control |
| C | **Polarization feature object** — map patch with EB/BB/rotation signal departing from null |
| D | **Multi-survey anomaly object** — sky position flagged by 2+ independent anomaly detectors |
| E | **Light curve object** — unTimely source with variability inconsistent with all standard classes |

If the object is fuzzy, the pipeline drifts into AI slop.

### Gate 2 — Benchmark Reproduction

Reproduce at least one known result before claiming anything new:

- Known cluster catalog recovery (A)
- Known spectral class recovery (B)
- Known EB null (C)
- Known variable class recovery (E)

**No benchmark reproduction = no trust.**

### Gate 3 — Synthetic / Injected Signals

Every pipeline needs injections — synthetic anomalies, injected point sources, synthetic spectra with known features, injected polarization rotations, synthetic light curves. **Non-negotiable.**

### Gate 4 — Null Tests

Run the pipeline on scrambled sky positions, shuffled labels, phase-scrambled maps, time-shuffled light curves, metadata-only baselines, random controls. The model must **fail cleanly on nonsense.**

### Gate 5 — Holdout Validation

Never random train/test only. Use survey holdouts, sky-region holdouts, time holdouts, instrument holdouts, redshift holdouts, quality-regime holdouts.

### Gate 6 — Selection-Function / Nuisance Audit

Test whether the model secretly learns depth, dust, seeing, PSF, stellar density, sky footprint, detector quirks, scan strategy, redshift completeness, or background gradients. **This is where most astronomy ML fails.**

### Gate 7 — Calibration

Every score must mean something: reliability diagrams, ECE, Brier score, confidence-stratified precision, abstention curves. A catalog without calibrated uncertainty is weak.

### Gate 8 — External Comparison

Compare against known catalogs, alternative methods, literature benchmarks, and simple baselines. If the model can't beat or explain a simpler method, that matters.

### Gate 9 — Human Review Loop

Top anomalies, high-confidence novel candidates, disagreement sets, and calibration failures get human audit. Not the whole archive — just the decision boundary.

### Gate 10 — Catalog Schema + Provenance

Every output object needs: unique ID, probabilities/scores, QC flags, provenance, survey source, version, model version, processing notes. If you can't release a clean catalog, the pipeline isn't mature.

### Gate 11 — Red-Team Report

Every pipeline gets a "why this might be wrong" document: likely leakage routes, astrophysical confounders, instrument/systematic confounders, what would falsify the claim.

### Gate 12 — Claim Taxonomy

Standard status ladder — nothing jumps levels:

```
IDEA → PROTOTYPE → BASELINE_REPRODUCED → INJECTION_VALIDATED
  → NULL_VALIDATED → ROBUSTNESS_PARTIAL → ROBUSTNESS_PASSED
    → CATALOG_READY → PAPER_READY
```

---

## Pipeline Standards Card

**Required before starting any pipeline.** One page with:

| Field | Description |
|-------|-------------|
| Scientific object | What exactly is being detected/classified? |
| Benchmark to reproduce | Which known result proves the pipeline works? |
| Injection plan | What synthetic signals get injected and recovered? |
| Null test plan | What scrambled/shuffled controls are run? |
| Holdout plan | What spatial/temporal/survey splits are used? |
| Nuisance audit | What metadata correlations are tested? |
| External comparison | What catalogs or methods are compared against? |
| Catalog schema | What fields does every output object have? |
| Fail conditions | What would make this pipeline's results untrustworthy? |
| Claim language limits | What can and cannot be said from the results? |

---

## Pipeline A — CMB Anomaly Hunter

> Train a model to identify statistically unusual patches in Planck/ACT maps that might indicate new physics or uncharacterized systematics.

### Method

1. Generate thousands of simulated CMB patches (CAMB + beam + anisotropic noise + foreground residuals)
2. Train CNN or vision transformer to score anomalousness
3. Apply to real Planck/ACT patches at multiple scales
4. Rank by anomaly score; classify by anomaly family
5. Characterize top anomalies against known foreground/systematic families

### Anomaly Families (Gate 1)

- Cold/hot spots beyond the Cold Spot
- Point-source residuals below catalog thresholds
- SZ-like compact decrements
- Non-Gaussian blob patterns
- Anisotropic residual textures
- Parity-odd features

### Simulation Realism

Simulations must include: ΛCDM realizations, beam convolution, mask effects, anisotropic noise, foreground residuals, component-separation artifacts, realistic patch boundaries.

### Benchmark (Gate 2)

Recover known SZ clusters, strong point sources, known problematic residual regions, Cold Spot-like features.

### Critical Null

Phase-scrambled and Gaussianized maps — "anomalies" must collapse.

### Claim Standard

No "new physics anomaly" unless it survives mask changes, frequency splits, is not explained by known families, and is significant relative to realistic simulation ensembles.

### Output

| Catalog | Contents |
|---------|----------|
| **CMB anomaly catalog** | Anomaly type, score, likely explanation, follow-up priority |
| **Systematic-risk map** | Regions flagging potential contamination for other analyses |

### Compute & Timeline

RunPod GPU for CNN/ViT training; CPU for inference. **2–4 sessions.**

---

## Pipeline B — DESI Spectral Anomaly Miner ⭐ RECOMMENDED FIRST

> Find spectroscopically unusual objects in DESI DR1 that don't fit any standard template, with a branch producing PNG-optimized high-bias tracers.

### Method

1. Build baseline spectral autoencoder on full DESI spectroscopic sample
2. Rank by reconstruction error (anomaly score)
3. Cluster anomalies by type
4. Cross-match with Legacy Surveys imaging, unTimely variability, X-ray/radio
5. Produce two catalogs: anomalies + PNG tracers

### Reconstruction Baselines (Gate 2)

Start with PCA → classical autoencoder → denoising autoencoder → transformer only if it materially improves retrieval.

### Spectral Preprocessing

Consistent wavelength grids, bad-pixel handling, flux scaling, SNR handling, sky-line masking. Sloppy preprocessing = meaningless anomalies.

### Anomaly Families (post-detection clustering)

| Family | Examples |
|--------|----------|
| Emission-line weirdos | Double-peaked, offset, unusual ratios |
| Broad-line oddities | Unusual BAL, changing-look candidates |
| Redshift mismatch | Spectroscopic z disagrees with photo-z |
| Lens candidates | Multiple redshift systems in one fiber |
| Artifacts | Bad sky subtraction, truncation, reduction glitches |

### Benchmark (Gate 2)

Recover known rare classes: unusual-line QSOs, BAL objects, known lens candidates, strong redshift failures, reduction artifacts.

### Artifact Audit (Gate 6)

Verify the model is not just finding low-SNR junk, bad sky subtraction, truncated spectra, or reduction glitches.

### Tracer Utility Branch

Second output score: **PNG tracer utility potential** — high-z, high-bias, clean spectrum → directly feeds f_NL work.

### Claim Standard

Paper must say: baseline reproduced, anomaly classes validated, artifact contamination quantified, high-z tracer subset identified, catalog released.

### Output

| Catalog | Contents |
|---------|----------|
| **DESI spectral anomaly catalog** | Object ID, anomaly score, family, cross-match info, QC flags |
| **DESI high-bias tracer candidates** | Tracer utility score, redshift, bias proxy, purity estimate |

### Compute & Timeline

RunPod GPU for autoencoder; CPU for cross-matching. **3–5 sessions.**

### Paper Potential

**Strong** — DESI DR1 is the hottest new dataset in cosmology.

---

## Pipeline C — Polarization Feature Extractor

> Extract subtle polarization signals from CMB maps using task-specific models, producing a multi-scale polarization feature catalog.

### Method

1. Train on simulated polarization maps with injected signals
2. Separate task-specific heads (not one vague extractor)
3. Apply to real Planck/ACT Q/U data
4. Score each patch for each signal type
5. Produce polarization feature catalog

### Task-Specific Heads

| Head | Target Signal |
|------|--------------|
| Uniform birefringence | Constant EB rotation |
| Scale-dependent rotation | ℓ-dependent β(ℓ) |
| Cosmic strings / defects | Linear discontinuities in polarization |
| Patchy reionization | Large-scale B-mode patches |
| Foreground / systematic | Dust, beam mismatch, miscalibration |

### Null-First Discipline

Before real maps: EB null on simulations, injected rotation recovery, miscalibration nuisance recovery, dropped-frequency robustness.

### Systematics-Aware Training

Include injected nuisance: angle miscalibration, polarized dust mismatch, beam mismatch, masking artifacts.

### Claim Standard

No "scale-dependent birefringence" unless nulls pass, miscalibration is modeled, feature survives frequency/mask changes, injected rotations recover without bias.

### Output

| Product | Contents |
|---------|----------|
| **Polarization feature catalog** | Patch ID, signal type scores, confidence, systematic risk |
| **Rotation-likelihood map** | Sky map of β probability at multiple angular scales |
| **Systematic-risk map** | Regions where systematic alternatives are plausible |

### Compute & Timeline

RunPod GPU for training; Planck maps already on pod. **4–6 sessions.**

---

## Pipeline D — Cross-Survey Anomaly Correlator

> Find objects/regions that are anomalous in multiple datasets simultaneously — the intersection that random coincidence cannot explain.

### Method

1. Run calibrated anomaly detectors independently on CMB, optical/spectroscopic, and IR surveys
2. Cross-match by sky position with angular tolerance
3. Score multi-survey coincidences against expected false-match rate
4. Characterize physically

### Prerequisites

Requires **calibrated outputs from Pipelines A, B, C, and/or E**. Do not correlate raw uncalibrated rankings.

### Key Controls

- **Sky-position nulls:** randomize positions to estimate false coincidence
- **Selection-effect modeling:** survey depth varies by region
- **Control populations:** compare anomaly-anomaly matches against random-sky, normal-object, and matched-depth controls

### Anomaly Tuple Schema

Each match stores: anomaly scores by survey, object types, angular separation, counterpart confidence, likely known explanation.

### Claim Standard

No "multi-survey anomaly" unless coincidence exceeds expectations from random alignment, footprint overlap, selection bias, and known object classes.

### Output

| Catalog | Contents |
|---------|----------|
| **Cross-survey anomaly coincidence catalog** | Tuple of survey anomaly scores, false-match probability, physical characterization |

### Compute & Timeline

Requires Pipeline A–C outputs. **2–3 sessions** on top of those.

### Paper Potential

**Very high** — multi-survey anomaly correlation is an unexplored methodology.

---

## Pipeline E — Time-Domain Cosmological Transient Finder ⭐ RECOMMENDED SECOND

> Use unTimely's 32 IR epochs to find objects whose variability is inconsistent with all standard astrophysical models, with a branch producing PNG-optimized QSO tracers.

### Method

1. Build light-curve feature vectors for ~2B unWISE sources across 32 epochs
2. Train variability classifier on known types
3. Flag "none of the above" as science candidates
4. Cross-match with Legacy, DESI, eROSITA
5. Produce two catalogs: anomalies + PNG tracers

### Light-Curve Object (Gate 1)

Not just epoch vectors. Each object stores: flux per epoch, uncertainty, cadence gaps, quality flags, variability features (amplitude, timescale, asymmetry, color change), contextual colors from cross-match.

### Known-Class Benchmark (Gate 2)

| Class | Recovery Target |
|-------|----------------|
| QSOs | Known spectroscopic QSOs from DESI |
| RR Lyrae | Known from Gaia/ZTF |
| Eclipsing binaries | Known from Kepler/TESS cross-match |
| AGN | Known from X-ray catalogs |
| Moving objects | Known asteroids/TNOs |

### Synthetic Injection (Gate 3)

Inject: changing-look AGN, long-timescale drifts, dusty transients, appearing/disappearing sources, cadence-challenged signals.

### Artifact Rejection (Gate 6)

Critical risks: blending, moving-object confusion, image subtraction failures, detector artifacts, low-SNR fluctuations.

### Explainability

For each "none of the above" source: best known-class mismatch, why it's out-of-distribution, cross-survey context.

### Tracer Utility Branch

Second output: **high-z tracer usefulness score** — variable QSOs at z > 1.5 with high effective bias.

### Claim Standard

Paper says: known classes recovered, artifact contamination quantified, crossmatched follow-up context added, tracer-enrichment subset produced.

### Output

| Catalog | Contents |
|---------|----------|
| **Time-domain anomaly catalog** | Source ID, anomaly score, best-match class, OOD reason, cross-match |
| **Variability-selected cosmology tracers** | Tracer utility score, redshift, variability class, bias proxy |

### Compute & Timeline

RunPod GPU for classifier; CPU for feature engineering on 2B sources. **4–6 sessions.**

### Paper Potential

**Strong** standalone discovery paper. The Paz precedent shows this gets attention.

---

## What Still Strengthens the Core Bounce Research

### Theory (diminishing returns)

| Task | Impact | Difficulty | Worth it? |
|------|--------|:----------:|:---------:|
| Email Cai | 92% → ~99% confidence | Easy | **Yes** |
| Full in-in integral | Independent derivation | Multi-month | No — polynomial proof sufficient |
| PolySpec pipeline | Estimator-grade r | 1–2 sessions | Medium |
| Exact ε correction | Narrows [1–8%] | All-vertex cancellation | Low |

### Data (high value, untapped)

| Task | Impact | Status |
|------|--------|--------|
| DESI catalog + enhanced tracers | Real data product | Design only |
| Miscalibration-marginalized β | Closes 0.08° gap | Done at basic level |
| Frequency consistency at high res | Tests cosmological origin | Done at NSIDE=256 |

---

## How This Transforms the Research Program

**Before these pipelines:**
> A theoretical prediction waiting for SPHEREx.

**After these pipelines:**
> An active observational research program producing novel catalogs, discovering new objects, and improving the sensitivity of current data to the bounce prediction — while also contributing standalone astrophysical discoveries that the community uses regardless of bounce physics.
