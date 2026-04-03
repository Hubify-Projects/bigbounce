#!/usr/bin/env python3
"""
Enhanced DESI DR1 Full-Scale GPU Inference — 45-Column Catalog
==============================================================

Processes ALL 17.65M DESI DR1 spectra and saves every object (not just
anomalies above threshold) with 45 columns per row: autoencoder scores,
128-dim latent vectors, redrock pipeline classifications, FIBERMAP
photometry, SCORES signal-to-noise, and derived columns.

Output: Parquet files in batches of ~500K rows (~3-5 GB total).

Key differences from 13_desi_dr1_gpu_inference.py:
  1. Saves ALL objects (every spectrum gets a row)
  2. Opens redrock-*.fits alongside coadd-*.fits for pipeline z, spectype
  3. Extracts 128-dim latent vector from encoder
  4. Computes peak residual wavelength (which pixel has max error)
  5. Computes residual kurtosis (spike vs broad deviation)
  6. Extracts FIBERMAP columns (MORPHTYPE, fluxes, EBV, parallax, etc.)
  7. Extracts SCORES columns (MEDIAN_COADD_SNR_B/R/Z, TSNR2_*)
  8. Computes derived columns (colors, is_point_source, is_star_candidate,
     classification, discovery_potential)
  9. Saves to Parquet (or CSV fallback)
 10. Batched output (~500K rows per file) to limit memory
 11. Checkpoint file after every healpix pixel for resume

Usage:
  python enhanced_18M_inference.py --model-path best_model_47k.pt

Expected runtime: ~6-8 hours on H200 (download-limited)
Expected output: ~3.2 GB in Parquet format
"""

import numpy as np
import torch
import torch.nn as nn
from astropy.io import fits
import urllib.request
import re
import os
import json
import time
import argparse
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# Try to import pyarrow for Parquet output; fall back to CSV
try:
    import pyarrow as pa
    import pyarrow.parquet as pq
    HAS_PARQUET = True
except ImportError:
    HAS_PARQUET = False
    print("WARNING: pyarrow not installed — output will be CSV (larger files)")

try:
    from scipy.stats import kurtosis as scipy_kurtosis
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False
    print("WARNING: scipy not installed — residual_kurtosis will be NaN")


# ===========================================================================
# Model definition (must match trained checkpoint exactly)
# ===========================================================================

class BigAE(nn.Module):
    """Spectral autoencoder: 496 downsampled channels -> 128-dim latent."""
    def __init__(self, n_in=496, n_lat=128):
        super().__init__()
        self.enc = nn.Sequential(
            nn.Linear(n_in, 512), nn.BatchNorm1d(512), nn.ReLU(), nn.Dropout(0.15),
            nn.Linear(512, 256), nn.BatchNorm1d(256), nn.ReLU(), nn.Dropout(0.1),
            nn.Linear(256, 128), nn.ReLU(),
            nn.Linear(128, n_lat),
        )
        self.dec = nn.Sequential(
            nn.Linear(n_lat, 128), nn.ReLU(),
            nn.Linear(128, 256), nn.BatchNorm1d(256), nn.ReLU(), nn.Dropout(0.1),
            nn.Linear(256, 512), nn.BatchNorm1d(512), nn.ReLU(), nn.Dropout(0.15),
            nn.Linear(512, n_in),
        )

    def forward(self, x):
        return self.dec(self.enc(x))

    def encode(self, x):
        """Return the 128-dim latent representation."""
        return self.enc(x)


# ===========================================================================
# Spectral helpers
# ===========================================================================

# DESI arm wavelength ranges (Angstroms) — used for peak residual mapping
# B: 3600–5800 A  (2751 pixels, downsampled to 171.9 -> 172 bins)
# R: 5760–7620 A  (2326 pixels, downsampled to 145.4 -> 145 bins)
# Z: 7520–9824 A  (2881 pixels, downsampled to 180.1 -> 179 bins)
# Total downsampled: 172 + 145 + 179 = 496

B_WAVE_START, B_WAVE_END, B_NBINS = 3600.0, 5800.0, 172
R_WAVE_START, R_WAVE_END, R_NBINS = 5760.0, 7620.0, 145
Z_WAVE_START, Z_WAVE_END, Z_NBINS = 7520.0, 9824.0, 179

def _build_wavelength_grid():
    """Build the 496-element approximate wavelength grid (bin centers)."""
    b = np.linspace(B_WAVE_START, B_WAVE_END, B_NBINS, endpoint=False) + (B_WAVE_END - B_WAVE_START) / B_NBINS / 2
    r = np.linspace(R_WAVE_START, R_WAVE_END, R_NBINS, endpoint=False) + (R_WAVE_END - R_WAVE_START) / R_NBINS / 2
    z = np.linspace(Z_WAVE_START, Z_WAVE_END, Z_NBINS, endpoint=False) + (Z_WAVE_END - Z_WAVE_START) / Z_NBINS / 2
    return np.concatenate([b, r, z])

WAVE_GRID = _build_wavelength_grid()  # shape (496,)


def downsample(arr, factor=16):
    """Downsample spectral axis by averaging groups of `factor` pixels."""
    n = arr.shape[-1] // factor * factor
    return arr[..., :n].reshape(*arr.shape[:-1], -1, factor).mean(axis=-1)


def flux_to_mag(flux):
    """Convert nanomaggy flux to AB magnitude. Returns NaN for flux <= 0."""
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.where(flux > 0, 22.5 - 2.5 * np.log10(flux), np.nan)


def compute_color(flux_a, flux_b):
    """Compute magnitude color = mag_a - mag_b from fluxes."""
    mag_a = flux_to_mag(flux_a)
    mag_b = flux_to_mag(flux_b)
    return mag_a - mag_b


# ===========================================================================
# Classification and discovery potential (rule-based triage)
# ===========================================================================

def classify_object(score, spectype, zwarn, w1w2, morphtype, z_val, parallax,
                    snr_b, snr_r, snr_z, gr, rz):
    """
    Rule-based classification for triage.

    Returns (classification_str, discovery_potential_str).
    """
    # Default
    classification = "NORMAL"
    potential = "LOW"

    is_anomalous = score > 5.0
    is_highly_anomalous = score > 10.0

    # Low S/N check — anomalies that are just noisy data
    min_snr = min(
        snr_b if np.isfinite(snr_b) else 999,
        snr_r if np.isfinite(snr_r) else 999,
        snr_z if np.isfinite(snr_z) else 999,
    )
    if min_snr < 1.0 and is_anomalous:
        return "LOW_SNR_ARTIFACT", "LOW"

    # Star candidate
    is_star = (parallax > 0.5) if np.isfinite(parallax) else False
    is_psf = (morphtype == b'PSF' or morphtype == 'PSF') if morphtype is not None else False

    if is_star and is_anomalous:
        classification = "ANOMALOUS_STAR"
        potential = "MEDIUM"
        if is_highly_anomalous:
            potential = "HIGH"
        return classification, potential

    # AGN / QSO candidate (W1-W2 > 0.8 is Stern et al. criterion)
    is_agn_colors = (w1w2 > 0.8) if np.isfinite(w1w2) else False
    if is_agn_colors and is_anomalous:
        classification = "ANOMALOUS_AGN_CANDIDATE"
        potential = "HIGH"
        if is_highly_anomalous:
            potential = "VERY_HIGH"
        return classification, potential

    # Pipeline says QSO but our model finds it anomalous
    if spectype in (b'QSO', 'QSO') and is_anomalous:
        classification = "ANOMALOUS_QSO"
        potential = "HIGH"
        if is_highly_anomalous and zwarn == 0:
            potential = "VERY_HIGH"
        return classification, potential

    # Pipeline says GALAXY
    if spectype in (b'GALAXY', 'GALAXY') and is_anomalous:
        classification = "ANOMALOUS_GALAXY"
        potential = "MEDIUM"
        if is_highly_anomalous:
            potential = "HIGH"
        if is_highly_anomalous and zwarn == 0:
            potential = "VERY_HIGH"
        return classification, potential

    # Pipeline says STAR but we don't see parallax
    if spectype in (b'STAR', 'STAR') and not is_star and is_anomalous:
        classification = "MISCLASSIFIED_STAR?"
        potential = "HIGH"
        return classification, potential

    # High anomaly but unclassified
    if is_highly_anomalous:
        classification = "UNCLASSIFIED_ANOMALY"
        potential = "HIGH"
        if zwarn == 0:
            potential = "VERY_HIGH"
        return classification, potential

    if is_anomalous:
        classification = "MILD_ANOMALY"
        potential = "MEDIUM"
        return classification, potential

    # Pipeline failure (not anomalous but ZWARN > 0)
    if zwarn > 0:
        classification = "PIPELINE_UNCERTAIN"
        potential = "LOW"
        return classification, potential

    return classification, potential


# ===========================================================================
# FITS column extraction helpers (handle missing columns gracefully)
# ===========================================================================

def safe_col(table, colname, idx, default=np.nan):
    """Extract a value from a FITS table column, returning default if missing."""
    try:
        if colname in table.dtype.names:
            val = table[colname][idx]
            # Handle bytes strings
            if isinstance(val, (bytes, np.bytes_)):
                return val.decode('utf-8', errors='replace').strip()
            return val
        return default
    except Exception:
        return default


def safe_col_array(table, colname, default_val=np.nan):
    """Extract an entire column as a numpy array, filling with default if missing."""
    try:
        if colname in table.dtype.names:
            arr = np.array(table[colname])
            # Handle bytes columns -> decode
            if arr.dtype.kind == 'S' or arr.dtype.kind == 'U':
                return arr
            return arr.astype(np.float64) if arr.dtype.kind in ('f', 'i', 'u') else arr
        return None
    except Exception:
        return None


# ===========================================================================
# Core processing: one healpix pixel -> list of row dicts
# ===========================================================================

def process_healpix(coadd_path, redrock_path, model, device, batch_size=8192):
    """
    Process one healpix pixel: extract all 45 columns per object.

    Parameters
    ----------
    coadd_path : str
        Path to the downloaded coadd-*.fits file.
    redrock_path : str or None
        Path to the downloaded redrock-*.fits file (None if download failed).
    model : BigAE
        Loaded autoencoder model (on GPU).
    device : torch.device
        CUDA device.
    batch_size : int
        GPU batch size for inference.

    Returns
    -------
    n_objects : int
        Number of spectra processed.
    rows : list of dict
        One dict per object with all 45 columns.
    """
    sp = fits.open(coadd_path, memmap=True)
    fm = sp['FIBERMAP'].data
    n_obj = len(fm)

    # ---- 1. Build downsampled, normalized input array ----
    b_flux = sp['B_FLUX'].data
    r_flux = sp['R_FLUX'].data
    z_flux = sp['Z_FLUX'].data

    # Actual number of downsampled bins per arm (may vary slightly per file)
    b_ds = downsample(b_flux)
    r_ds = downsample(r_flux)
    z_ds = downsample(z_flux)
    n_b = b_ds.shape[1]
    n_r = r_ds.shape[1]
    n_z = z_ds.shape[1]

    flux = np.hstack([b_ds, r_ds, z_ds]).astype(np.float32)
    flux = np.nan_to_num(flux, nan=0, posinf=0, neginf=0)

    # Per-spectrum normalization
    med = np.median(np.abs(flux), axis=1, keepdims=True)
    med = np.where(med > 0, med, 1.0)
    X = np.clip(flux / med, -10, 10)

    # ---- 2. GPU inference: scores, latent vectors, reconstruction ----
    model.eval()
    all_scores = []
    all_latent = []
    all_recon = []

    with torch.no_grad():
        for i in range(0, n_obj, batch_size):
            batch = torch.from_numpy(X[i:i + batch_size]).to(device)
            # Encode to get latent vectors
            latent = model.encode(batch)
            # Decode from latent to get reconstruction
            recon = model.dec(latent)
            # Reconstruction error per spectrum
            residuals = (batch - recon) ** 2
            scores = torch.mean(residuals, dim=1)

            all_scores.append(scores.cpu().numpy())
            all_latent.append(latent.cpu().numpy())
            all_recon.append(recon.cpu().numpy())

    scores_arr = np.concatenate(all_scores)          # (n_obj,)
    latent_arr = np.concatenate(all_latent)           # (n_obj, 128)
    recon_arr = np.concatenate(all_recon)             # (n_obj, 496)

    # ---- 3. Per-band residuals, worst band, peak residual wavelength, kurtosis ----
    abs_residuals = np.abs(X - recon_arr)  # (n_obj, 496)

    rB = np.mean(abs_residuals[:, :n_b], axis=1)
    rR = np.mean(abs_residuals[:, n_b:n_b + n_r], axis=1)
    rZ = np.mean(abs_residuals[:, n_b + n_r:], axis=1)

    # Worst band per object
    band_arr = np.stack([rB, rR, rZ], axis=1)  # (n_obj, 3)
    worst_idx = np.argmax(band_arr, axis=1)
    worst_band = np.array(['B', 'R', 'Z'])[worst_idx]

    # Peak residual wavelength: which downsampled bin has the highest |residual|?
    peak_idx = np.argmax(abs_residuals, axis=1)  # (n_obj,)
    # Map bin index to approximate wavelength using the grid
    total_bins = abs_residuals.shape[1]
    # Use actual file bins for wavelength mapping
    wave_grid_file = np.concatenate([
        np.linspace(B_WAVE_START, B_WAVE_END, n_b, endpoint=False) + (B_WAVE_END - B_WAVE_START) / n_b / 2,
        np.linspace(R_WAVE_START, R_WAVE_END, n_r, endpoint=False) + (R_WAVE_END - R_WAVE_START) / n_r / 2,
        np.linspace(Z_WAVE_START, Z_WAVE_END, n_z, endpoint=False) + (Z_WAVE_END - Z_WAVE_START) / n_z / 2,
    ])
    # Clamp indices just in case
    peak_idx_clamped = np.clip(peak_idx, 0, len(wave_grid_file) - 1)
    peak_wave = wave_grid_file[peak_idx_clamped]

    # Residual kurtosis
    if False and HAS_SCIPY:  # DISABLED for speed
        # scipy.stats.kurtosis with Fisher=True (excess kurtosis, normal=0)
        residual_vec = X - recon_arr  # signed residuals
        kurtosis_arr = scipy_kurtosis(residual_vec, axis=1, fisher=True)
    else:
        kurtosis_arr = np.full(n_obj, np.nan)

    # ---- 4. Redrock columns ----
    z_arr = np.full(n_obj, np.nan)
    zerr_arr = np.full(n_obj, np.nan)
    zwarn_arr = np.full(n_obj, -1, dtype=np.int64)
    spectype_arr = np.full(n_obj, '', dtype='U20')
    subtype_arr = np.full(n_obj, '', dtype='U40')
    deltachi2_arr = np.full(n_obj, np.nan)

    if redrock_path and os.path.exists(redrock_path):
        try:
            rr = fits.open(redrock_path, memmap=True)
            rr_data = rr['REDSHIFTS'].data
            # Redrock has one row per TARGETID, same order as FIBERMAP in coadd
            # Match by TARGETID to be safe
            rr_tids = rr_data['TARGETID']
            fm_tids = fm['TARGETID']

            # If same length and same order (common case), direct assign
            if len(rr_tids) == n_obj and np.all(rr_tids == fm_tids):
                z_arr = rr_data['Z'].astype(np.float64)
                zerr_arr = rr_data['ZERR'].astype(np.float64)
                zwarn_arr = rr_data['ZWARN'].astype(np.int64)
                for j in range(n_obj):
                    st = rr_data['SPECTYPE'][j]
                    su = rr_data['SUBTYPE'][j]
                    spectype_arr[j] = st.decode('utf-8').strip() if isinstance(st, bytes) else str(st).strip()
                    subtype_arr[j] = su.decode('utf-8').strip() if isinstance(su, bytes) else str(su).strip()
                deltachi2_arr = rr_data['DELTACHI2'].astype(np.float64)
            else:
                # Build lookup by TARGETID
                rr_lookup = {int(tid): idx for idx, tid in enumerate(rr_tids)}
                for j in range(n_obj):
                    tid = int(fm_tids[j])
                    if tid in rr_lookup:
                        ri = rr_lookup[tid]
                        z_arr[j] = float(rr_data['Z'][ri])
                        zerr_arr[j] = float(rr_data['ZERR'][ri])
                        zwarn_arr[j] = int(rr_data['ZWARN'][ri])
                        st = rr_data['SPECTYPE'][ri]
                        su = rr_data['SUBTYPE'][ri]
                        spectype_arr[j] = st.decode('utf-8').strip() if isinstance(st, bytes) else str(st).strip()
                        subtype_arr[j] = su.decode('utf-8').strip() if isinstance(su, bytes) else str(su).strip()
                        deltachi2_arr[j] = float(rr_data['DELTACHI2'][ri])
            rr.close()
        except Exception as e:
            # Redrock read failed — columns stay as defaults
            pass

    # ---- 5. FIBERMAP columns ----
    targetid_arr = fm['TARGETID'].astype(np.int64)
    ra_arr = safe_col_array(fm, 'TARGET_RA')
    if ra_arr is None:
        ra_arr = np.zeros(n_obj)
    dec_arr = safe_col_array(fm, 'TARGET_DEC')
    if dec_arr is None:
        dec_arr = np.zeros(n_obj)

    # Morphtype (string column)
    morphtype_raw = safe_col_array(fm, 'MORPHTYPE')
    morphtype_arr = np.full(n_obj, '', dtype='U10')
    if morphtype_raw is not None:
        for j in range(n_obj):
            v = morphtype_raw[j]
            morphtype_arr[j] = v.decode('utf-8').strip() if isinstance(v, bytes) else str(v).strip()

    # Flux columns
    flux_g = safe_col_array(fm, 'FLUX_G')
    flux_r = safe_col_array(fm, 'FLUX_R')
    flux_z_phot = safe_col_array(fm, 'FLUX_Z')
    flux_w1 = safe_col_array(fm, 'FLUX_W1')
    flux_w2 = safe_col_array(fm, 'FLUX_W2')

    # Other FIBERMAP columns
    ebv_arr = safe_col_array(fm, 'EBV')
    parallax_arr = safe_col_array(fm, 'PARALLAX')
    gaia_g_arr = safe_col_array(fm, 'GAIA_PHOT_G_MEAN_MAG')
    sersic_arr = safe_col_array(fm, 'SERSIC')
    shape_r_arr = safe_col_array(fm, 'SHAPE_R')
    coadd_numexp_arr = safe_col_array(fm, 'COADD_NUMEXP')
    coadd_exptime_arr = safe_col_array(fm, 'COADD_EXPTIME')
    mean_fiber_ra_arr = safe_col_array(fm, 'MEAN_FIBER_RA')
    mean_fiber_dec_arr = safe_col_array(fm, 'MEAN_FIBER_DEC')

    # ---- 6. SCORES extension columns ----
    snr_b_arr = np.full(n_obj, np.nan)
    snr_r_arr = np.full(n_obj, np.nan)
    snr_z_arr = np.full(n_obj, np.nan)
    tsnr2_qso_arr = np.full(n_obj, np.nan)
    tsnr2_elg_arr = np.full(n_obj, np.nan)
    tsnr2_lrg_arr = np.full(n_obj, np.nan)
    tsnr2_bgs_arr = np.full(n_obj, np.nan)

    try:
        if 'SCORES' in [ext.name for ext in sp]:
            sc = sp['SCORES'].data

            # Check alignment: if SCORES has TARGETID, verify order matches
            aligned = True
            if 'TARGETID' in sc.dtype.names:
                sc_tids = sc['TARGETID']
                if len(sc_tids) != n_obj or not np.all(sc_tids == targetid_arr):
                    aligned = False
            elif len(sc) != n_obj:
                aligned = False

            if aligned:
                # Extract each SCORES column, keeping defaults if column is absent
                score_cols = {
                    'MEDIAN_COADD_SNR_B': 'snr_b',
                    'MEDIAN_COADD_SNR_R': 'snr_r',
                    'MEDIAN_COADD_SNR_Z': 'snr_z',
                    'TSNR2_QSO': 'tsnr2_qso',
                    'TSNR2_ELG': 'tsnr2_elg',
                    'TSNR2_LRG': 'tsnr2_lrg',
                    'TSNR2_BGS': 'tsnr2_bgs',
                }
                for fits_name, local_name in score_cols.items():
                    tmp = safe_col_array(sc, fits_name)
                    if tmp is not None:
                        if local_name == 'snr_b': snr_b_arr = tmp
                        elif local_name == 'snr_r': snr_r_arr = tmp
                        elif local_name == 'snr_z': snr_z_arr = tmp
                        elif local_name == 'tsnr2_qso': tsnr2_qso_arr = tmp
                        elif local_name == 'tsnr2_elg': tsnr2_elg_arr = tmp
                        elif local_name == 'tsnr2_lrg': tsnr2_lrg_arr = tmp
                        elif local_name == 'tsnr2_bgs': tsnr2_bgs_arr = tmp
    except Exception:
        pass

    # ---- 7. Derived columns ----
    # Fill None arrays with nan defaults
    def ensure_arr(a, n):
        if a is None:
            return np.full(n, np.nan, dtype=np.float64)
        return a.astype(np.float64)

    flux_g_f = ensure_arr(flux_g, n_obj)
    flux_r_f = ensure_arr(flux_r, n_obj)
    flux_z_f = ensure_arr(flux_z_phot, n_obj)
    flux_w1_f = ensure_arr(flux_w1, n_obj)
    flux_w2_f = ensure_arr(flux_w2, n_obj)
    parallax_f = ensure_arr(parallax_arr, n_obj)
    ebv_f = ensure_arr(ebv_arr, n_obj)
    gaia_g_f = ensure_arr(gaia_g_arr, n_obj)
    sersic_f = ensure_arr(sersic_arr, n_obj)
    shape_r_f = ensure_arr(shape_r_arr, n_obj)
    mean_fiber_ra_f = ensure_arr(mean_fiber_ra_arr, n_obj)
    mean_fiber_dec_f = ensure_arr(mean_fiber_dec_arr, n_obj)
    snr_b_f = snr_b_arr.astype(np.float64)
    snr_r_f = snr_r_arr.astype(np.float64)
    snr_z_f = snr_z_arr.astype(np.float64)
    tsnr2_qso_f = tsnr2_qso_arr.astype(np.float64)
    tsnr2_elg_f = tsnr2_elg_arr.astype(np.float64)
    tsnr2_lrg_f = tsnr2_lrg_arr.astype(np.float64)
    tsnr2_bgs_f = tsnr2_bgs_arr.astype(np.float64)
    # coadd_numexp and coadd_exptime
    coadd_numexp_f = ensure_arr(coadd_numexp_arr, n_obj)
    coadd_exptime_f = ensure_arr(coadd_exptime_arr, n_obj)

    gr_color = compute_color(flux_g_f, flux_r_f)
    rz_color = compute_color(flux_r_f, flux_z_f)
    w1w2_color = compute_color(flux_w1_f, flux_w2_f)

    is_point_source = np.array([m == 'PSF' for m in morphtype_arr], dtype=bool)
    is_star_candidate = np.array([
        (parallax_f[j] > 0.5 if np.isfinite(parallax_f[j]) else False) or
        (gr_color[j] < 0.5 and rz_color[j] < 0.3 if np.isfinite(gr_color[j]) and np.isfinite(rz_color[j]) else False)
        for j in range(n_obj)
    ], dtype=bool)

    # Classification & discovery potential
    # OPTIMIZED: skip classification in hot loop, do in post-processing
    classification_arr = np.full(n_obj, "UNCLASSIFIED", dtype='U30')
    potential_arr = np.full(n_obj, "TBD", dtype='U10')
    if False:  # DISABLED for speed — classify in post-processing
        c, p = classify_object(
            score=float(scores_arr[j]),
            spectype=spectype_arr[j],
            zwarn=int(zwarn_arr[j]),
            w1w2=float(w1w2_color[j]) if np.isfinite(w1w2_color[j]) else np.nan,
            morphtype=morphtype_arr[j],
            z_val=float(z_arr[j]) if np.isfinite(z_arr[j]) else np.nan,
            parallax=float(parallax_f[j]) if np.isfinite(parallax_f[j]) else np.nan,
            snr_b=float(snr_b_f[j]) if np.isfinite(snr_b_f[j]) else np.nan,
            snr_r=float(snr_r_f[j]) if np.isfinite(snr_r_f[j]) else np.nan,
            snr_z=float(snr_z_f[j]) if np.isfinite(snr_z_f[j]) else np.nan,
            gr=float(gr_color[j]) if np.isfinite(gr_color[j]) else np.nan,
            rz=float(rz_color[j]) if np.isfinite(rz_color[j]) else np.nan,
        )
        classification_arr[j] = c
        potential_arr[j] = p

    sp.close()

    # ---- 8. Assemble into list of dicts ----
    rows = []
    for j in range(n_obj):
        row = {
            # Autoencoder columns (8)
            'anomaly_score': float(scores_arr[j]),
            'rB': float(rB[j]),
            'rR': float(rR[j]),
            'rZ': float(rZ[j]),
            'worst_band': worst_band[j],
            'peak_residual_wavelength': float(peak_wave[j]),
            'residual_kurtosis': float(kurtosis_arr[j]),
            # Latent vector stored as 128 separate columns
        }
        # Latent dimensions as lat_000 ... lat_127
        for d in range(128):
            row[f'lat_{d:03d}'] = float(latent_arr[j, d])

        row.update({
            # Redrock columns (6)
            'z': float(z_arr[j]),
            'zerr': float(zerr_arr[j]),
            'zwarn': int(zwarn_arr[j]),
            'spectype': spectype_arr[j],
            'subtype': subtype_arr[j],
            'deltachi2': float(deltachi2_arr[j]),
            # FIBERMAP columns (17)
            'targetid': int(targetid_arr[j]),
            'target_ra': float(ra_arr[j]),
            'target_dec': float(dec_arr[j]),
            'morphtype': morphtype_arr[j],
            'flux_g': float(flux_g_f[j]),
            'flux_r': float(flux_r_f[j]),
            'flux_z': float(flux_z_f[j]),
            'flux_w1': float(flux_w1_f[j]),
            'flux_w2': float(flux_w2_f[j]),
            'ebv': float(ebv_f[j]),
            'parallax': float(parallax_f[j]),
            'gaia_phot_g_mean_mag': float(gaia_g_f[j]),
            'sersic': float(sersic_f[j]),
            'shape_r': float(shape_r_f[j]),
            'coadd_numexp': int(coadd_numexp_f[j]),
            'coadd_exptime': float(coadd_exptime_f[j]),
            'mean_fiber_ra': float(mean_fiber_ra_f[j]),
            'mean_fiber_dec': float(mean_fiber_dec_f[j]),
            # SCORES columns (7)
            'median_coadd_snr_b': float(snr_b_f[j]),
            'median_coadd_snr_r': float(snr_r_f[j]),
            'median_coadd_snr_z': float(snr_z_f[j]),
            'tsnr2_qso': float(tsnr2_qso_f[j]),
            'tsnr2_elg': float(tsnr2_elg_f[j]),
            'tsnr2_lrg': float(tsnr2_lrg_f[j]),
            'tsnr2_bgs': float(tsnr2_bgs_f[j]),
            # Derived columns (7)
            'gr_color': float(gr_color[j]),
            'rz_color': float(rz_color[j]),
            'w1w2_color': float(w1w2_color[j]),
            'is_point_source': bool(is_point_source[j]),
            'is_star_candidate': bool(is_star_candidate[j]),
            'classification': classification_arr[j],
            'discovery_potential': potential_arr[j],
        })
        rows.append(row)

    return n_obj, rows


# ===========================================================================
# Batch I/O: write accumulated rows to Parquet (or CSV)
# ===========================================================================

def save_batch(rows, batch_idx, output_dir):
    """
    Write a list of row dicts to disk as Parquet (preferred) or CSV.

    Returns the output file path.
    """
    if not rows:
        return None

    if HAS_PARQUET:
        fpath = os.path.join(output_dir, f'desi_dr1_catalog_batch_{batch_idx:04d}.parquet')
        # Build pyarrow table from list of dicts
        # Group columns to define schema
        cols = {}
        for key in rows[0].keys():
            vals = [r[key] for r in rows]
            if key in ('targetid', 'zwarn', 'coadd_numexp'):
                cols[key] = pa.array(vals, type=pa.int64())
            elif key in ('is_point_source', 'is_star_candidate'):
                cols[key] = pa.array(vals, type=pa.bool_())
            elif key in ('worst_band', 'spectype', 'subtype', 'morphtype',
                          'classification', 'discovery_potential'):
                cols[key] = pa.array(vals, type=pa.string())
            else:
                # All floats
                cols[key] = pa.array(vals, type=pa.float32())

        table = pa.table(cols)
        pq.write_table(table, fpath, compression='zstd')
    else:
        # CSV fallback
        fpath = os.path.join(output_dir, f'desi_dr1_catalog_batch_{batch_idx:04d}.csv')
        import csv
        with open(fpath, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)

    return fpath


# ===========================================================================
# Pixel mapper (same as original, enumerates all DR1 healpix pixels)
# ===========================================================================

def map_dr1_pixels():
    """
    Discover all healpix pixels in DESI DR1 main survey (dark + bright).

    Returns list of (survey, program, group_prefix, healpix_pixel).
    """
    base = 'https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/healpix/'
    all_pixels = []

    for survey in ['main']:
        for program in ['dark', 'bright']:
            url = base + survey + '/' + program + '/'
            try:
                req = urllib.request.urlopen(url, timeout=30)
                html = req.read().decode()
                groups = re.findall(r'href="(\d+)/"', html)
                print(f'  {survey}/{program}: {len(groups)} healpix groups')
                for g in groups:
                    try:
                        req2 = urllib.request.urlopen(url + g + '/', timeout=15)
                        html2 = req2.read().decode()
                        pixels = re.findall(r'href="(\d+)/"', html2)
                        for p in pixels:
                            all_pixels.append((survey, program, g, p))
                    except Exception as e:
                        print(f'    WARNING: failed to list {survey}/{program}/{g}: {e}')
            except Exception as e:
                print(f'  WARNING: failed to list {survey}/{program}: {e}')

    return all_pixels


def load_checkpoint(checkpoint_path):
    """Load checkpoint to determine which pixels have been processed."""
    if os.path.exists(checkpoint_path):
        with open(checkpoint_path, 'r') as f:
            return json.load(f)
    return {'processed_pixels': [], 'total_spectra': 0, 'total_rows_written': 0,
            'batch_idx': 0, 'elapsed_s': 0}


def save_checkpoint(checkpoint_path, state):
    """Save checkpoint state."""
    # Write to temp file first, then rename (atomic on most filesystems)
    tmp = checkpoint_path + '.tmp'
    with open(tmp, 'w') as f:
        json.dump(state, f)
    os.replace(tmp, checkpoint_path)


# ===========================================================================
# Download helper with retry
# ===========================================================================

def download_file(url, dest, retries=3, timeout=60):
    """Download a file with retry. Returns True on success."""
    for attempt in range(retries):
        try:
            urllib.request.urlretrieve(url, dest)
            return True
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)  # exponential backoff
            else:
                return False
    return False


# ===========================================================================
# Main entry point
# ===========================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Enhanced DESI DR1 Full-Scale GPU Inference — 45-Column Catalog')
    parser.add_argument('--model-path', type=str, default='best_model_47k.pt',
                        help='Path to trained BigAE model checkpoint')
    parser.add_argument('--output-dir', type=str, default='outputs/enhanced_catalog',
                        help='Directory for output Parquet/CSV batches')
    parser.add_argument('--temp-dir', type=str, default='temp',
                        help='Directory for temporary FITS downloads')
    parser.add_argument('--batch-size', type=int, default=8192,
                        help='GPU inference batch size')
    parser.add_argument('--flush-every', type=int, default=500000,
                        help='Flush to disk every N rows (default 500K)')
    parser.add_argument('--max-pixels', type=int, default=0,
                        help='Limit number of healpix pixels (0 = all)')
    parser.add_argument('--parallel-downloads', type=int, default=4,
                        help='Number of parallel FITS downloads')
    parser.add_argument('--resume', action='store_true',
                        help='Resume from checkpoint if available')
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    os.makedirs(args.temp_dir, exist_ok=True)

    checkpoint_path = os.path.join(args.output_dir, 'checkpoint.json')

    # ---- Device setup ----
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print('=' * 70)
    print('ENHANCED DESI DR1 INFERENCE — 45-COLUMN CATALOG')
    print('=' * 70)
    print(f'Device:           {device}')
    if torch.cuda.is_available():
        print(f'GPU:              {torch.cuda.get_device_name(0)}')
        vram = torch.cuda.get_device_properties(0).total_memory / 1e9
        print(f'VRAM:             {vram:.1f} GB')
    print(f'Output dir:       {args.output_dir}')
    print(f'Parquet support:  {HAS_PARQUET}')
    print(f'Scipy support:    {HAS_SCIPY}')
    print(f'Flush every:      {args.flush_every:,} rows')
    print()

    # ---- Load model ----
    print(f'Loading model from {args.model_path} ...')
    model = BigAE(n_in=496, n_lat=128).to(device)
    state_dict = torch.load(args.model_path, map_location=device, weights_only=True)
    model.load_state_dict(state_dict)
    model.eval()
    print('Model loaded and set to eval mode.\n')

    # ---- Map all healpix pixels ----
    print('Mapping DESI DR1 healpix pixels ...')
    all_pixels = map_dr1_pixels()
    print(f'Total healpix pixels found: {len(all_pixels)}')
    est_spectra = len(all_pixels) * 650  # rough average per pixel
    print(f'Estimated spectra: ~{est_spectra / 1e6:.1f}M\n')

    if args.max_pixels > 0:
        all_pixels = all_pixels[:args.max_pixels]
        print(f'LIMITED to first {args.max_pixels} pixels\n')

    # ---- Load checkpoint if resuming ----
    ckpt = load_checkpoint(checkpoint_path) if args.resume else {
        'processed_pixels': [], 'total_spectra': 0,
        'total_rows_written': 0, 'batch_idx': 0, 'elapsed_s': 0,
    }
    processed_set = set(ckpt.get('processed_pixels', []))
    total_spectra = ckpt.get('total_spectra', 0)
    total_rows_written = ckpt.get('total_rows_written', 0)
    batch_idx = ckpt.get('batch_idx', 0)
    prior_elapsed = ckpt.get('elapsed_s', 0)

    if processed_set:
        print(f'RESUMING from checkpoint: {len(processed_set)} pixels already done, '
              f'{total_spectra:,} spectra, {total_rows_written:,} rows written, '
              f'batch_idx={batch_idx}\n')

    # ---- DESI base URL ----
    base_url = 'https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/healpix/'

    # ---- Processing loop ----
    row_buffer = []   # accumulate rows between flushes
    n_errors = 0
    n_skipped = 0
    t0 = time.time()

    for px_i, (survey, program, group, pixel) in enumerate(all_pixels):
        pixel_key = f'{survey}-{program}-{pixel}'

        # Skip already-processed pixels (resume support)
        if pixel_key in processed_set:
            n_skipped += 1
            continue

        # ---- Download coadd + redrock ----
        coadd_fname = f'coadd-{survey}-{program}-{pixel}.fits'
        redrock_fname = f'redrock-{survey}-{program}-{pixel}.fits'
        coadd_path = os.path.join(args.temp_dir, coadd_fname)
        redrock_path = os.path.join(args.temp_dir, redrock_fname)

        dir_url = f'{base_url}{survey}/{program}/{group}/{pixel}/'
        coadd_url = dir_url + coadd_fname
        redrock_url = dir_url + redrock_fname

        # Download both files (coadd is required, redrock is best-effort)
        coadd_ok = download_file(coadd_url, coadd_path)
        if not coadd_ok:
            n_errors += 1
            if (px_i + 1) % 100 == 0:
                print(f'  [{px_i + 1}/{len(all_pixels)}] SKIP (download failed): {pixel_key}')
            continue

        redrock_ok = download_file(redrock_url, redrock_path)

        # ---- Process ----
        try:
            n_obj, rows = process_healpix(
                coadd_path,
                redrock_path if redrock_ok else None,
                model, device, args.batch_size,
            )
            total_spectra += n_obj
            row_buffer.extend(rows)
        except Exception as e:
            n_errors += 1
            if (px_i + 1) % 50 == 0:
                print(f'  [{px_i + 1}/{len(all_pixels)}] ERROR processing {pixel_key}: {e}')
            traceback.print_exc()
        finally:
            # Always clean up FITS files
            if os.path.exists(coadd_path):
                os.remove(coadd_path)
            if os.path.exists(redrock_path):
                os.remove(redrock_path)

        # Track processed pixel
        processed_set.add(pixel_key)

        # ---- Flush to disk if buffer is large enough ----
        if len(row_buffer) >= args.flush_every:
            print(f'  Flushing {len(row_buffer):,} rows to batch {batch_idx:04d} ...')
            fpath = save_batch(row_buffer, batch_idx, args.output_dir)
            if fpath:
                total_rows_written += len(row_buffer)
                print(f'    -> {fpath} ({total_rows_written:,} total rows written)')
            batch_idx += 1
            row_buffer = []

            # Save checkpoint after flush
            elapsed = prior_elapsed + (time.time() - t0)
            save_checkpoint(checkpoint_path, {
                'processed_pixels': list(processed_set),
                'total_spectra': total_spectra,
                'total_rows_written': total_rows_written,
                'batch_idx': batch_idx,
                'elapsed_s': elapsed,
                'n_errors': n_errors,
            })

        # ---- Progress reporting ----
        n_done = px_i + 1 - n_skipped
        if n_done > 0 and n_done % 50 == 0:
            elapsed = time.time() - t0
            rate = total_spectra / elapsed if elapsed > 0 else 0
            pix_rate = n_done / elapsed if elapsed > 0 else 0
            remaining = len(all_pixels) - px_i - 1
            eta_h = remaining / pix_rate / 3600 if pix_rate > 0 else 0
            anom_count = sum(1 for r in row_buffer if r.get('anomaly_score', 0) > 5.0)
            print(f'  [{px_i + 1}/{len(all_pixels)}] '
                  f'{total_spectra:,} spectra | '
                  f'{total_rows_written + len(row_buffer):,} rows | '
                  f'{n_errors} errors | '
                  f'{rate:.0f} spec/s | '
                  f'ETA: {eta_h:.1f}h | '
                  f'buffer: {len(row_buffer):,}')

        # Save checkpoint after every pixel (lightweight JSON write)
        if n_done > 0 and n_done % 10 == 0:
            elapsed = prior_elapsed + (time.time() - t0)
            save_checkpoint(checkpoint_path, {
                'processed_pixels': list(processed_set),
                'total_spectra': total_spectra,
                'total_rows_written': total_rows_written,
                'batch_idx': batch_idx,
                'elapsed_s': elapsed,
                'n_errors': n_errors,
            })

    # ---- Final flush of remaining rows ----
    if row_buffer:
        print(f'\nFinal flush: {len(row_buffer):,} rows to batch {batch_idx:04d} ...')
        fpath = save_batch(row_buffer, batch_idx, args.output_dir)
        if fpath:
            total_rows_written += len(row_buffer)
            print(f'  -> {fpath}')
        batch_idx += 1

    # ---- Final checkpoint ----
    elapsed = prior_elapsed + (time.time() - t0)
    save_checkpoint(checkpoint_path, {
        'processed_pixels': list(processed_set),
        'total_spectra': total_spectra,
        'total_rows_written': total_rows_written,
        'batch_idx': batch_idx,
        'elapsed_s': elapsed,
        'n_errors': n_errors,
        'status': 'COMPLETE',
    })

    # ---- Summary ----
    print('\n' + '=' * 70)
    print('COMPLETE!')
    print('=' * 70)
    print(f'  Healpix pixels:     {len(processed_set):,}')
    print(f'  Total spectra:      {total_spectra:,}')
    print(f'  Rows written:       {total_rows_written:,}')
    print(f'  Output batches:     {batch_idx}')
    print(f'  Errors/skipped:     {n_errors}')
    print(f'  Elapsed:            {elapsed:.0f}s ({elapsed/3600:.1f}h)')
    print(f'  Rate:               {total_spectra/elapsed:.0f} spectra/sec' if elapsed > 0 else '')
    print(f'  Output directory:   {args.output_dir}')
    fmt = 'Parquet (zstd)' if HAS_PARQUET else 'CSV'
    print(f'  Output format:      {fmt}')
    print()

    # Print column count summary
    n_ae = 7          # anomaly_score, rB, rR, rZ, worst_band, peak_residual_wavelength, residual_kurtosis
    n_latent = 128    # lat_000 ... lat_127
    n_rr = 6          # z, zerr, zwarn, spectype, subtype, deltachi2
    n_fm = 17         # targetid, target_ra, target_dec, morphtype, flux_g/r/z/w1/w2, ebv, parallax, gaia_g, sersic, shape_r, coadd_numexp, coadd_exptime, mean_fiber_ra, mean_fiber_dec
    n_sc = 7          # snr b/r/z, tsnr2 qso/elg/lrg/bgs
    n_der = 7         # gr_color, rz_color, w1w2_color, is_point_source, is_star_candidate, classification, discovery_potential
    print(f'  Columns per row:    {n_ae + n_latent + n_rr + n_fm + n_sc + n_der}')
    print(f'    Autoencoder:      {n_ae}')
    print(f'    Latent vector:    {n_latent}')
    print(f'    Redrock:          {n_rr}')
    print(f'    FIBERMAP:         {n_fm}')
    print(f'    SCORES:           {n_sc}')
    print(f'    Derived:          {n_der}')


if __name__ == '__main__':
    main()
