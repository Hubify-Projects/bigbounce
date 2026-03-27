# Pipeline A: CMB Anomaly Hunter

Unsupervised anomaly detection in Planck CMB temperature maps using a convolutional autoencoder. The pipeline extracts sky patches, trains an autoencoder to learn the statistical structure of the CMB, and flags patches with high reconstruction error as anomalies.

## Scientific Motivation

The CMB is the oldest observable light in the universe. In standard LCDM + inflation, the temperature fluctuations are nearly Gaussian random fields. A bounce cosmology can imprint distinctive signatures:

- **Pre-bounce perturbation remnants** — if perturbations survive the bounce, they may leave localized non-Gaussian features or unusual spatial correlations that differ from inflationary predictions.
- **Parity violations** — spin-torsion coupling during the bounce preferentially generates one handedness, potentially producing cold/hot spot asymmetries or anomalous patterns in specific multipole ranges.
- **Scale-dependent features** — the bounce transition introduces a characteristic scale (the bounce energy scale) that could appear as localized features in specific angular size ranges.
- **Known CMB anomalies** — several existing anomalies (Cold Spot, hemispherical asymmetry, quadrupole-octopole alignment, parity asymmetry) lack satisfying inflationary explanations. A bounce cosmology may naturally produce some of these.

An autoencoder trained on "typical" CMB patches will assign high reconstruction error to patches that deviate from the learned norm. This is model-agnostic: it can discover anomalies without assuming a specific theoretical template.

## What Anomalies to Expect

The autoencoder will likely flag:

1. **The Cold Spot** (l ~ 209, b ~ -57) — a well-known ~10 deg cold region in the southern sky, significant at ~3 sigma. If the autoencoder independently identifies it, that validates the method.
2. **SZ clusters** — the Sunyaev-Zel'dovich effect from galaxy clusters creates localized temperature decrements. These should appear as point-like anomalies.
3. **Foreground residuals** — despite SMICA component separation, some Galactic foreground leakage may remain near the mask boundary.
4. **Point sources** — bright radio or infrared sources not fully subtracted.
5. **Novel features** — patches with unusual morphology, unexpected temperature gradients, or non-Gaussian structures that don't match known sources.

The scientifically interesting anomalies are in category 5. Categories 1-4 serve as validation that the pipeline is working correctly.

## Data

### Planck SMICA CMB Temperature Map

**File:** `COM_CMB_IQU-smica_2048_R3.00_full.fits`
**Size:** ~2.2 GB
**NSIDE:** 2048 (50,331,648 pixels)
**Resolution:** ~1.7 arcmin per pixel

Download from one of:

```bash
# IRSA (NASA)
wget "https://irsa.ipac.caltech.edu/data/Planck/release_3/all-sky-maps/maps/component-maps/cmb/COM_CMB_IQU-smica_2048_R3.00_full.fits"

# Planck Legacy Archive (ESA)
wget "https://pla.esac.esa.int/pla/aio/product-action?MAP.MAP_ID=COM_CMB_IQU-smica_2048_R3.00_full.fits" -O COM_CMB_IQU-smica_2048_R3.00_full.fits
```

Place the file in this directory (`pipelines/pipeline_a_cmb/`) or specify its path with `--map_file`.

## Pipeline Steps

### Step 1: Extract Patches

```bash
python extract_patches.py \
  --map_file COM_CMB_IQU-smica_2048_R3.00_full.fits \
  --n_patches 1000 \
  --patch_deg 10 \
  --patch_pixels 64 \
  --output_dir outputs
```

This will:
1. Load the full-sky NSIDE=2048 HEALPix map
2. Remove monopole and dipole
3. Generate 1000 random sky positions avoiding the Galactic plane (|b| < 20 deg)
4. Extract 10 deg x 10 deg patches using gnomonic (tangent-plane) projection
5. Downsample each patch to 64x64 pixels (~9.4 arcmin/pixel)
6. Normalize each patch (subtract mean, divide by std)
7. Save as `outputs/cmb_patches.npy` (shape: N x 64 x 64, float32)

**Outputs:**
- `outputs/cmb_patches.npy` — normalized patch array
- `outputs/patch_metadata.json` — sky coordinates and raw statistics for each patch
- `outputs/extraction_summary.json` — run summary

### Step 2: Train Autoencoder

```bash
python cmb_autoencoder.py \
  --patches outputs/cmb_patches.npy \
  --epochs 100 \
  --batch_size 32 \
  --latent_dim 128 \
  --output_dir outputs
```

Requires PyTorch. On a GPU (RunPod H100), training completes in minutes. On CPU, allow ~30 min.

**Outputs:**
- `outputs/autoencoder_best.pt` — trained model weights
- `outputs/training_losses.json` — train/val loss curves
- `outputs/reconstruction_errors.npy` — per-patch MSE (shape: N)
- `outputs/latent_vectors.npy` — 128-dim latent representations (shape: N x 128)
- `outputs/anomaly_results.json` — anomaly rankings with sky coordinates
- `outputs/top_anomaly_patches.npy` — the 50 highest-error patches

### Step 3: Analyze Anomalies

After training, examine `outputs/anomaly_results.json` for the top anomalies. Cross-reference their sky positions (glon, glat) against:
- Known CMB anomalies (Cold Spot at l=209, b=-57)
- Planck SZ cluster catalog
- Planck point source catalogs (PCCS2)
- SIMBAD for any known astrophysical sources

Anomalies that do NOT match any known source are candidates for further investigation.

## Architecture Details

```
Input: (1, 64, 64) — single-channel normalized CMB patch

Encoder:
  Conv2d(1, 16, 3, stride=2, pad=1)  -> (16, 32, 32)  -> BN -> ReLU
  Conv2d(16, 32, 3, stride=2, pad=1) -> (32, 16, 16)  -> BN -> ReLU
  Conv2d(32, 64, 3, stride=2, pad=1) -> (64, 8, 8)    -> BN -> ReLU
  Flatten                             -> (4096)
  Linear(4096, 128)                   -> (128)          [latent vector]

Decoder:
  Linear(128, 4096)                   -> (4096)         -> ReLU
  Reshape                             -> (64, 8, 8)
  ConvT2d(64, 32, 3, stride=2, pad=1, opad=1) -> (32, 16, 16) -> BN -> ReLU
  ConvT2d(32, 16, 3, stride=2, pad=1, opad=1) -> (16, 32, 32) -> BN -> ReLU
  ConvT2d(16, 1,  3, stride=2, pad=1, opad=1) -> (1,  64, 64) -> Tanh

Output: (1, 64, 64) — reconstructed patch

Loss: MSE(input, output)
Parameters: ~660K
Latent dim: 128
```

## Connection to Bounce Cosmology

This pipeline is one component of a 5-pipeline AI archival discovery program (see `MEMORY.md`). Its specific role:

1. **Anomaly catalog** — Build a catalog of CMB patches that deviate from Gaussian random field expectations, ranked by reconstruction error.

2. **Template matching** — In a later phase, compare anomaly morphologies against theoretical templates for bounce-specific signatures (e.g., matter bounce f_NL = -35/8 bispectrum shape in real space).

3. **Parity analysis** — Examine whether anomalies show any parity asymmetry (more anomalies in even vs. odd multipole contributions), which would connect to the parity violation predicted by spin-torsion coupling.

4. **Cross-correlation with other pipelines** — Overlay CMB anomaly positions with Pipeline 2 (galaxy chirality) results to look for spatial correlations between CMB anomalies and galaxy spin asymmetries.

## Requirements

```
numpy
healpy >= 1.16
torch >= 2.0
astropy
```

## Directory Structure

```
pipelines/pipeline_a_cmb/
  ├── extract_patches.py      # Patch extraction from Planck map
  ├── cmb_autoencoder.py      # Autoencoder training + anomaly detection
  ├── README.md               # This file
  └── outputs/                # Generated data (gitignored)
      ├── cmb_patches.npy
      ├── patch_metadata.json
      ├── extraction_summary.json
      ├── autoencoder_best.pt
      ├── training_losses.json
      ├── reconstruction_errors.npy
      ├── latent_vectors.npy
      ├── anomaly_results.json
      └── top_anomaly_patches.npy
```
