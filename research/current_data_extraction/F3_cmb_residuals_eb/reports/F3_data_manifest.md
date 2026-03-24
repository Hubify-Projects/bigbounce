# F3 Data Manifest

**Date:** 2026-03-23
**Status:** REGISTRY COMPLETE, DOWNLOADS NOT STARTED

---

## Required Map Products

### Planck PR3 (2018 Legacy Release)

| File | URL Base | Size | Purpose | Priority |
|------|----------|------|---------|----------|
| COM_CMB_IQU-smica_2048_R3.00_full.fits | pla.esac.esa.int/.../ | ~300 MB | Component-separated T/Q/U map | REQUIRED |
| COM_CMB_IQU-nilc_2048_R3.00_full.fits | pla.esac.esa.int/.../ | ~300 MB | Alternative component separation | REQUIRED |
| COM_Mask_CMB-common-Mask-Int_2048_R3.00.fits | pla.esac.esa.int/.../ | ~50 MB | Common intensity mask | REQUIRED |
| COM_Mask_CMB-common-Mask-Pol_2048_R3.00.fits | pla.esac.esa.int/.../ | ~50 MB | Common polarization mask | REQUIRED |
| HFI_SkyMap_100-field_2048_R3.01_full.fits | pla.esac.esa.int/.../ | ~600 MB | 100 GHz frequency map (I/Q/U) | FOR ROBUSTNESS |
| HFI_SkyMap_143-field_2048_R3.01_full.fits | pla.esac.esa.int/.../ | ~600 MB | 143 GHz frequency map | FOR ROBUSTNESS |
| HFI_SkyMap_217-field_2048_R3.01_full.fits | pla.esac.esa.int/.../ | ~600 MB | 217 GHz frequency map | FOR ROBUSTNESS |

**Source:** Planck Legacy Archive (PLA): https://pla.esac.esa.int/
**Mirror:** IRSA: https://irsa.ipac.caltech.edu/data/Planck/release_3/

### Planck PR3 Beam / Transfer Functions

| File | Purpose |
|------|---------|
| HFI_RIMO_Beams_R3.01.fits | Beam window functions per frequency |
| COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE_R3.01.txt | Published C_ℓ for comparison |

### ACT DR6 (if accessible)

| File | URL Base | Size | Purpose |
|------|----------|------|---------|
| ACT DR6 coadded maps | act.princeton.edu / LAMBDA | ~1 GB | Higher-resolution T/Q/U |
| ACT DR6 masks | LAMBDA | ~100 MB | Footprint masks |
| ACT DR6 beam files | LAMBDA | ~10 MB | Beam transfer functions |

**Note:** ACT DR6 products may require specific access procedures. Check LAMBDA for current availability.

### Simulations (for null tests)

| Dataset | Size | Purpose |
|---------|------|---------|
| FFP10 CMB realizations (subset) | ~10 GB for 100 sims | Null tests, injection recovery |
| Gaussian white noise sims | Generated locally | Additional null tests |

---

## Software Dependencies

| Package | Version | Purpose | Install |
|---------|---------|---------|---------|
| healpy | ≥1.16 | HEALPix map I/O and operations | pip install healpy |
| NaMaster | ≥2.0 | Pseudo-Cℓ estimation with purification | pip install pymaster |
| numpy | ≥1.24 | Numerical computation | pip install numpy |
| scipy | ≥1.10 | Statistical tests | pip install scipy |
| matplotlib | ≥3.7 | Plotting | pip install matplotlib |
| astropy | ≥5.3 | FITS file handling | pip install astropy |

---

## Verification Protocol

Before any analysis:
1. Download files from official source (PLA or LAMBDA)
2. Verify file sizes match PLA catalog
3. Verify NSIDE = 2048 for maps
4. Verify map ordering (RING vs NESTED) matches expectations
5. Check for NaN/INF pixels outside mask
6. Record download date and exact URL

---

## Download Script (to be created)

```bash
# F3_download_maps.sh
# This script downloads the required Planck PR3 products
# Run on RunPod CPU pod with sufficient disk space (>20 GB)
```

Status: Script NOT YET WRITTEN. Will be created in F3.1.

---

## Gating

- Downloads must complete successfully before F3.2
- File verification must pass before F3.2
- NaMaster must install and import cleanly before F3.2
- Null simulations must be generated before F3.2
