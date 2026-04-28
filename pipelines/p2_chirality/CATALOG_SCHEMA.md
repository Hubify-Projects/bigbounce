# Production Chirality Catalog Schema

## Overview

The chirality pipeline produces three catalog tiers from Galaxy Zoo DESI imaging.
This document specifies the **production catalog (Catalog C)**, which is the
recommended output for all cosmology science analyses.

## Catalog Tiers

| Tier | Name | Description | Use Case |
|------|------|-------------|----------|
| A | Raw | Direct v2 model output, no post-processing | Ablation studies, model diagnostics |
| B | Calibrated | Platt-calibrated probabilities (bias=1.58, temp=4.65) | ML downstream tasks, transfer learning |
| C | Production | Equivariant-averaged, QC-flagged | Cosmology science (dipole tests, parity analyses) |

All three tiers share the same row set (one row per Galaxy Zoo DESI object).
Catalog C is a strict superset of the information in A and B: it carries both the
raw and equivariant columns so that users can reproduce calibration checks without
needing a separate file.

## File Format

- **Format:** Apache Parquet (Snappy compression)
- **Filename convention:** `chirality_catalog_c_v{VERSION}_{YYYYMMDD}.parquet`
- **Estimated size:** ~400 MB for the full Galaxy Zoo DESI footprint (~8M rows),
  ~50 MB for the spiral-only subset (~1M rows with `is_spiral == True`)
- **Row ordering:** Sorted by `(ra, dec)` ascending to enable efficient spatial
  queries and deterministic reproducibility

## Column Definitions

| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| `id_str` | string | No | Galaxy Zoo DESI identifier (unique primary key) |
| `ra` | float64 | No | Right ascension in degrees (J2000, ICRS) |
| `dec` | float64 | No | Declination in degrees (J2000, ICRS) |
| `p_cw_raw` | float32 | No | Raw model probability of clockwise spiral morphology |
| `p_ccw_raw` | float32 | No | Raw model probability of counter-clockwise spiral morphology |
| `p_ns_raw` | float32 | No | Raw model probability of not-spiral morphology |
| `p_cw_eq` | float32 | No | Equivariant-averaged probability of clockwise spiral |
| `p_ccw_eq` | float32 | No | Equivariant-averaged probability of counter-clockwise spiral |
| `p_ns_eq` | float32 | No | Equivariant-averaged probability of not-spiral |
| `class_raw` | string | No | Raw classification label: `CW`, `CCW`, or `NOT_SPIRAL` |
| `class_eq` | string | No | Equivariant classification label: `CW`, `CCW`, or `NOT_SPIRAL` |
| `confidence_raw` | float32 | No | Maximum probability from the raw model (i.e., `max(p_cw_raw, p_ccw_raw, p_ns_raw)`) |
| `confidence_eq` | float32 | No | Maximum probability from the equivariant model (i.e., `max(p_cw_eq, p_ccw_eq, p_ns_eq)`) |
| `is_spiral` | bool | No | `True` if `class_eq != NOT_SPIRAL` (convenience flag for spiral-only cuts) |
| `qc_flag` | int | No | Quality-control flag: `0` = good, `1` = low confidence, `2` = edge case |

### Probability Triplet Invariants

For every row the following hold exactly:

- `p_cw_raw + p_ccw_raw + p_ns_raw = 1.0` (to float32 precision)
- `p_cw_eq + p_ccw_eq + p_ns_eq = 1.0` (to float32 precision)
- `class_raw = argmax(p_cw_raw, p_ccw_raw, p_ns_raw)`
- `class_eq = argmax(p_cw_eq, p_ccw_eq, p_ns_eq)`

### QC Flag Definitions

| Value | Label | Criteria |
|-------|-------|----------|
| 0 | Good | `confidence_eq >= 0.6` and no edge-case trigger |
| 1 | Low confidence | `confidence_eq < 0.6` |
| 2 | Edge case | Raw and equivariant classifications disagree, OR the object lies within 5 arcsec of a bright star, OR the equivariant averaging changed the winning class |

For cosmology parity analyses, the recommended cut is `qc_flag == 0` and
`is_spiral == True`.

## Provenance

### Model

- **Architecture:** ViT-Small (`vit_small_patch16_224`, ImageNet-pretrained, last 6
  of 12 transformer blocks fine-tuned) with a custom 3-class classification head
  (LayerNorm -> 384->512 GELU d=0.3 -> 512->256 GELU d=0.2 -> 256->3 softmax)
- **Training data:** 26,626 images from Galaxy Zoo 1 (6,637 CW/CCW at >70% vote
  confidence), CE-ResNet high-confidence spirals (17,153), CE-ResNet non-spirals
  (846), and synthetic hard negatives (2,000 blank/noise/gradient images)
- **Training:** AdamW (head lr=3e-4, encoder lr=2e-5, weight decay=0.02), cosine
  annealing warm-restart (T_0=10, T_mult=2), batch size 64, early stopping
  patience 15, max 80 epochs. Flip-equivariance consistency loss (lambda=0.5)
  added to class-weighted cross-entropy.
- **Calibration (Catalog B):** Platt scaling with `bias = 1.58`, `temperature = 4.65`,
  fit against CE-ResNet consensus labels on a held-out overlap subset
- **Equivariant post-processing (Catalog C):** Each galaxy is classified under 2
  augmentations (original + horizontal reflection). The reflection swaps the CW/CCW
  labels. The 2 probability vectors are averaged to produce `p_*_eq`. This removes
  any orientation-dependent bias by construction.

### Input Imaging

- Smith42/galaxies dataset (DESI Legacy Imaging Surveys DR8, grz bands)
- 224x224 pixel stamps, 0.262 arcsec/pixel native scale

### Pipeline Scripts

| Step | Script | Output |
|------|--------|--------|
| Inference | `run_v2_inference.py` | Catalog A (raw) |
| Calibration | `calibrate_v2.py` | Catalog B (calibrated) |
| Equivariant averaging + QC | `real_zoobot_chirality.py` | Catalog C (production) |

## Recommended Usage

### For cosmology (dipole / parity / spin-correlation tests)

```python
import pandas as pd

cat = pd.read_parquet("chirality_catalog_c_v2_20260323.parquet")
spirals = cat[(cat["qc_flag"] == 0) & (cat["is_spiral"])]

# Use class_eq for CW/CCW assignment
# Use p_cw_eq / p_ccw_eq for probabilistic weighting
```

### For ML / transfer learning

Use Catalog B columns (`p_cw_raw`, `p_ccw_raw`, `p_ns_raw` after Platt
calibration applied externally) or train on the raw logits directly.

### For ablation / systematics studies

Compare Catalog A vs. Catalog C to quantify the impact of equivariant averaging.
The `class_raw` vs. `class_eq` disagreement rate is a direct measure of
orientation-dependent misclassification.

## Caveats

1. **Not a redshift catalog.** The catalog contains sky coordinates only. Redshifts
   must be obtained by cross-matching to a spectroscopic survey (DESI, SDSS, etc.)
   or a photo-z catalog. The `cross_survey_holdout.py` script demonstrates this
   workflow using the CE-ResNet external catalog.

2. **Equivariant averaging is not bias-free in the statistical sense.** It eliminates
   orientation bias but does not correct for morphological selection effects (e.g.,
   face-on spirals are easier to classify than edge-on ones). The `qc_flag` helps
   but does not fully mitigate this.

3. **Catalog completeness depends on the DESI Legacy Survey footprint.** Coverage
   is non-uniform: the galactic plane, bright-star masks, and survey-edge regions
   are underrepresented. Any large-scale analysis must account for the angular
   selection function.

4. **Float32 precision.** Probabilities are stored as float32 to keep file size
   manageable. For analyses requiring higher precision (e.g., extreme tails of the
   probability distribution), rerun inference in float64 mode.

5. **Version pinning.** Always record the catalog filename (including version and
   date) in any analysis script. The schema is stable within a major version but
   new QC flags or columns may be added in future versions.
