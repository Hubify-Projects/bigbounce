# Galaxy Spin Chirality Classification — Future Pipeline Plan

Status: PLANNING (future work, not used in Paper 1)
Created: 2026-03-06

## Objective

Build an object-level galaxy chirality (CW/CCW) classification pipeline using
vision models, producing a catalog large enough (100k-1M galaxies) for
per-redshift-bin dipole fitting.

This is explicitly **future work** — Paper 1 uses published aggregate CW/CCW
counts from Shamir (2012, 2022, 2024) for the A(z) fit.

---

## 1. Candidate Datasets

### Galaxy Zoo 2 (Willett et al. 2013) — CW/ACW votes available
- **Source:** https://data.galaxyzoo.org/ or SDSS CasJobs
- **Size:** ~240,000 galaxies with morphology votes
- **CW/ACW question:** YES — "In which direction do the spiral arms rotate?"
- **Redshift range:** z < 0.25 (SDSS spectroscopic)
- **Advantage:** Has the exact CW/ACW vote fractions needed
- **Limitation:** Low-z only, SDSS footprint

### Galaxy Zoo DECaLS (Walmsley et al. 2022) — spiral ID only
- **Source:** Zenodo DOI 10.5281/zenodo.4573248
- **Size:** ~314,000 galaxies (92,960 in volunteer catalog, 314k in auto catalog)
- **CW/ACW question:** NO — classifies winding tightness, not direction
- **Redshift range:** z < 0.15 (DECaLS photometric)
- **Advantage:** Already downloaded and processed
- **Limitation:** Cannot provide chirality labels directly

### SDSS DR17 Imaging
- **Source:** SDSS SkyServer / SciServer
- **Size:** Millions of galaxy images
- **CW/ACW:** Not labeled — requires classification model
- **Redshift range:** z < 0.7 (spectroscopic for bright galaxies)
- **Advantage:** Massive scale
- **Limitation:** Requires training a classifier

### DESI Bright Galaxy Survey (BGS)
- **Source:** DESI Legacy Surveys imaging
- **Size:** ~10M galaxy images in DR10
- **CW/ACW:** Not labeled — requires classification model
- **Redshift range:** z < 0.4 (spectroscopic from DESI)
- **Advantage:** Largest spectroscopic galaxy survey
- **Limitation:** No public data release yet for spectroscopic redshifts

### Euclid VIS Imaging (future)
- **Expected:** 2027-2028 data releases
- **Size:** ~1B galaxies imaged
- **Advantage:** Space-based resolution, low PSF systematics
- **Limitation:** Not yet available

---

## 2. Proposed Architecture

### Option A: Fine-tuned Vision Transformer (ViT)

1. **Base model:** DINOv2 (ViT-L/14) pretrained on natural images
2. **Fine-tuning data:** Galaxy Zoo 2 CW/ACW labeled galaxies (~40k spirals)
3. **Augmentation:** Parity augmentation (mirror + label swap) to eliminate classifier bias
4. **Output:** Binary classification (CW vs ACW) with calibrated probabilities
5. **Expected accuracy:** ~92-95% on GZ2 test set (based on similar work)

### Option B: CNN with ResNet backbone

1. **Base model:** ResNet-50 pretrained on ImageNet
2. **Fine-tuning:** Same GZ2 training set
3. **Architecture:** Standard transfer learning with frozen early layers
4. **Expected accuracy:** ~90-93%

### Option C: Vision-Language Model (VLM) zero-shot

1. **Model:** GPT-4o, Claude Opus 4.6, or Gemini 2.0 with vision
2. **Approach:** Zero-shot classification with structured prompt
3. **No training required** — evaluate on GZ2 test set first
4. **Expected accuracy:** Unknown — needs evaluation
5. **Advantage:** No training infrastructure needed
6. **Limitation:** API cost at scale (~$0.01/image, ~$10k for 1M galaxies)

### Recommended: Option A (ViT) with Option C (VLM) as validation

Fine-tune a ViT on GZ2 labels, then use VLM on a subset to validate
agreement. This provides both scale and independent verification.

---

## 3. Pipeline Steps

```
Step 1: Training data preparation
  - Download Galaxy Zoo 2 labeled catalog
  - Select spirals with >70% CW or CCW vote fraction (gold standard)
  - Download corresponding SDSS cutout images (64x64 or 128x128 pixels)
  - Parity-augment: mirror each image and swap label
  - Split: 70% train, 15% val, 15% test

Step 2: Model training
  - Fine-tune ViT-L/14 (DINOv2) on GZ2 spiral CW/ACW labels
  - Train with parity augmentation
  - Validate on held-out test set
  - Target: >93% accuracy, <0.5% CW/CCW bias on symmetric test set

Step 3: Inference on target survey
  - Download SDSS/DECaLS/DESI galaxy images
  - Select spirals using GZ DECaLS vote fractions or trained spiral classifier
  - Run CW/ACW classifier on all spirals
  - Output: per-galaxy (galaxy_id, ra, dec, z, P_CW, P_CCW, label)

Step 4: Quality control
  - Check CW/CCW rates on symmetric subsamples (should be ~50/50)
  - Check CW/CCW rates vs magnitude, size, redshift (null tests)
  - Flag galaxies with uncertain classification (|P_CW - P_CCW| < 0.3)

Step 5: Dipole fitting
  - Bin by redshift (10-20 bins across z = 0.0-0.5)
  - Compute A_obs per bin
  - Fit A(z) = A0 (1+z)^{-p} exp(-qz) using hierarchical Bayesian model
  - Full directional dipole fit in spherical harmonics

Step 6: Null tests
  - Hemisphere split (N vs S)
  - Random axis rotation
  - Parity-augmented repeat (swap all labels, refit)
  - Magnitude-limited subsamples
```

---

## 4. Expected Scale

| Survey Target | N_spirals | z_range | Compute (GPU-hrs) |
|---------------|-----------|---------|-------------------|
| GZ2 training | ~40,000 | 0-0.25 | ~4 hrs (fine-tuning) |
| SDSS DR17 inference | ~200,000 | 0-0.4 | ~8 hrs (inference) |
| DECaLS inference | ~300,000 | 0-0.3 | ~12 hrs (inference) |
| DESI BGS (future) | ~1,000,000 | 0-0.4 | ~40 hrs (inference) |

Total compute: ~64 GPU-hours for 1.5M galaxy classifications.

---

## 5. Key Design Constraints

1. **Parity symmetry is mandatory.** Any classifier must be trained with parity
   augmentation (mirror + label swap) and validated on symmetric test sets to
   confirm <0.5% CW/CCW bias.

2. **Publication-quality requires null tests.** The Patel & Desmond (2024) null
   result demonstrates that selection effects can create spurious asymmetry.
   Comprehensive null tests are required.

3. **This is a separate paper.** The chirality classification pipeline and
   resulting dipole analysis should be a standalone publication, not folded
   into Paper 1.

4. **Paper 1 is agnostic to this pipeline.** Paper 1's A(z) fit uses published
   aggregate counts and treats the spin signal as contested. This pipeline
   would either confirm or refute the signal independently.

---

## 6. Relationship to Paper 1

Paper 1 (current):
- Uses published aggregate CW/CCW counts from Shamir (2024)
- 5 survey-level data points for A(z) fit
- Treats galaxy spin asymmetry as "contested anomaly"
- Does NOT claim object-level chirality classification

This future pipeline (Paper 3 or standalone):
- Would produce object-level CW/CCW labels for 100k-1M galaxies
- Would enable per-redshift-bin A(z) fitting with 10-20 bins
- Would independently test the Shamir claims
- Would either strengthen or refute the galaxy spin section of Paper 1
