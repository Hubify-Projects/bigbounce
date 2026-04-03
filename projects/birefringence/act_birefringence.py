#!/usr/bin/env python3
"""
ACT DR6 Cosmic Birefringence Measurement.

Cosmic birefringence is a rotation of CMB polarization by angle beta, caused by
coupling of photons to an axion-like particle (ALP) field. This rotates E-modes
into B-modes, producing a non-zero EB cross-spectrum.

The exact estimator (derived from polarization-plane rotation (Q+iU) -> e^{2i*beta}*(Q+iU)):
    beta = (1/4) * arctan(2 * sum(C_EB) / sum(C_EE - C_BB))

Note: many papers quote "0.5 * arctan(...)" — that formula applies to a different
convention where the angle is measured from the Fourier-space angle, not the
polarization plane. The factor 1/4 is correct when birefringence is defined as
rotation of the polarization plane (the physical definition). Derivation:
  For a pure-E sky rotated by beta:
    C_EE = C_EE^true * cos^2(2*beta)
    C_BB = C_EE^true * sin^2(2*beta)
    C_EB = C_EE^true * cos(2*beta)*sin(2*beta) = C_EE^true * (1/2)*sin(4*beta)
  => 2*C_EB/(C_EE-C_BB) = sin(4*beta)/cos(4*beta) = tan(4*beta)
  => beta = (1/4) * arctan(2*C_EB/(C_EE-C_BB))

Bounce cosmology ALP prediction: beta = 0.27 deg
Observed (Dixon+2022, Minami+Komatsu 2020): beta = 0.342 +/- 0.094 deg (3.6 sigma)

Usage:
    # Simulation test (run locally):
    python act_birefringence.py --mode sim --beta_inject 0.27

    # ACT DR6 on H200 pod:
    python act_birefringence.py --mode act --input /workspace/act_dr6/act_dr6_TT.fits

    # Planck SMICA (if available locally):
    python act_birefringence.py --mode planck --input /path/to/COM_CMB_IQU-smica_2048_R3.00_full.fits

References:
    - Dixon et al. 2022, MNRAS
    - Minami & Komatsu 2020, Prog. Theor. Exp. Phys.
    - ACT DR6: Madhavacheril et al. 2024
"""

import argparse
import json
import os
import sys
import time

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# ─────────────────────────────────────────────────────────────────────────────
# Physical constants and reference values
# ─────────────────────────────────────────────────────────────────────────────

BETA_BOUNCE_PRED = 0.27        # degrees — bounce cosmology ALP prediction
BETA_OBSERVED    = 0.342       # degrees — Dixon+2022 / Minami+Komatsu 2020
BETA_OBS_ERR     = 0.094       # degrees — 1-sigma uncertainty

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))


# ─────────────────────────────────────────────────────────────────────────────
# Flat-sky E/B decomposition
# ─────────────────────────────────────────────────────────────────────────────

def qu_to_eb_flat(Q, U, pixel_size_rad=None):
    """
    Convert Q, U Stokes maps to E and B mode maps using flat-sky Fourier transform.

    On a flat sky with Fourier wavevector (l_x, l_y), the angle phi_l = arctan2(l_y, l_x).
    The spin-2 rotation gives:
        E(l) =  Q(l) * cos(2*phi_l) + U(l) * sin(2*phi_l)
        B(l) = -Q(l) * sin(2*phi_l) + U(l) * cos(2*phi_l)

    Parameters
    ----------
    Q, U : 2-D arrays of shape (ny, nx)
    pixel_size_rad : float or None
        Pixel size in radians. If None, angular frequencies are in pixel units.

    Returns
    -------
    E_lm, B_lm : 2-D complex arrays (Fourier-space)
    lx, ly     : 2-D frequency grids (same shape), in radians^-1 if pixel_size_rad given
    """
    ny, nx = Q.shape

    # 2-D FFT (numpy convention: zero-frequency in upper-left corner)
    Q_l = np.fft.fft2(Q)
    U_l = np.fft.fft2(U)

    # Frequency grids in pixel units, then shifted to have zero at centre
    lx_1d = np.fft.fftfreq(nx)   # cycles per pixel
    ly_1d = np.fft.fftfreq(ny)
    lx, ly = np.meshgrid(lx_1d, ly_1d)

    if pixel_size_rad is not None:
        # Convert to radians^-1  (multiply by 2pi/pixel_size to get rad^-1)
        lx = lx * (2 * np.pi / pixel_size_rad)
        ly = ly * (2 * np.pi / pixel_size_rad)

    phi_l = np.arctan2(ly, lx)    # polarization angle in Fourier space
    cos2 = np.cos(2 * phi_l)
    sin2 = np.sin(2 * phi_l)

    E_l = Q_l * cos2 + U_l * sin2
    B_l = -Q_l * sin2 + U_l * cos2

    return E_l, B_l, lx, ly


def compute_power_spectra(E_l, B_l, lx, ly, l_bins=None):
    """
    Compute angular power spectra C_EE, C_BB, C_EB as a function of multipole l.

    Bins the 2-D Fourier plane into annular l-bins.

    Parameters
    ----------
    E_l, B_l : 2-D complex arrays
    lx, ly   : 2-D frequency grids (radians^-1)
    l_bins   : 1-D array of bin edges (radians^-1). If None, uses 50 log-spaced bins.

    Returns
    -------
    l_centers : 1-D array of bin centres
    C_EE, C_BB, C_EB : 1-D power spectrum arrays
    """
    ny, nx = E_l.shape
    npix = nx * ny

    l_abs = np.sqrt(lx**2 + ly**2).ravel()

    # Power spectral densities (normalize by number of pixels)
    EE = (np.abs(E_l)**2 / npix).ravel()
    BB = (np.abs(B_l)**2 / npix).ravel()
    EB = (E_l * np.conj(B_l) / npix).ravel()

    l_min_nonzero = l_abs[l_abs > 0].min()
    l_max = l_abs.max()

    if l_bins is None:
        l_bins = np.logspace(np.log10(l_min_nonzero * 1.01),
                             np.log10(l_max * 0.99), 51)

    l_centers = 0.5 * (l_bins[:-1] + l_bins[1:])
    C_EE = np.zeros(len(l_centers))
    C_BB = np.zeros(len(l_centers))
    C_EB = np.zeros(len(l_centers), dtype=complex)

    for i, (lo, hi) in enumerate(zip(l_bins[:-1], l_bins[1:])):
        mask = (l_abs >= lo) & (l_abs < hi)
        if mask.sum() == 0:
            continue
        C_EE[i] = EE[mask].mean()
        C_BB[i] = BB[mask].mean()
        C_EB[i] = EB[mask].mean()

    return l_centers, C_EE, C_BB, C_EB.real


def estimate_beta(C_EE, C_BB, C_EB, weights=None):
    """
    Estimate birefringence angle beta from power spectra.

    Uses the exact bandpower estimator:
        beta = (1/4) * arctan(2 * sum(w * C_EB) / sum(w * (C_EE - C_BB)))

    Derivation: for a pure-E sky rotated by birefringence angle beta,
        C_EB = C_EE^true * (1/2)*sin(4*beta)
        C_EE - C_BB = C_EE^true * cos(4*beta)
    so  2*C_EB/(C_EE-C_BB) = tan(4*beta)  =>  beta = (1/4)*arctan(...)

    Note: the factor is 1/4, not 1/2. A factor of 1/2 would recover 2*beta.

    Parameters
    ----------
    C_EE, C_BB, C_EB : 1-D arrays
    weights : 1-D array or None (uniform if None)

    Returns
    -------
    beta_rad : float, birefringence angle in radians
    beta_deg : float, birefringence angle in degrees
    """
    if weights is None:
        weights = np.ones_like(C_EE)

    num = np.sum(weights * C_EB)
    den = np.sum(weights * (C_EE - C_BB))

    if den == 0:
        return 0.0, 0.0

    # Factor 1/4: see module docstring for full derivation
    beta_rad = 0.25 * np.arctan2(2 * num, den)
    beta_deg = np.degrees(beta_rad)
    return beta_rad, beta_deg


def bootstrap_beta(Q, U, pixel_size_rad, n_bootstrap=500, l_bins=None, seed=42):
    """
    Bootstrap uncertainty on beta by re-sampling pixels with replacement.

    For large maps this is expensive; use block-bootstrap (split map into 16 tiles).

    Returns
    -------
    beta_deg     : float, point estimate
    sigma_deg    : float, bootstrap 1-sigma
    beta_samples : 1-D array of bootstrap beta values (degrees)
    """
    # Point estimate
    E_l, B_l, lx, ly = qu_to_eb_flat(Q, U, pixel_size_rad)
    l_c, C_EE, C_BB, C_EB = compute_power_spectra(E_l, B_l, lx, ly, l_bins)
    _, beta_deg = estimate_beta(C_EE, C_BB, C_EB)

    # Block bootstrap: divide map into tiles, resample tiles
    ny, nx = Q.shape
    n_tiles_x = 4
    n_tiles_y = 4
    n_tiles = n_tiles_x * n_tiles_y
    tile_ny = ny // n_tiles_y
    tile_nx = nx // n_tiles_x

    tiles_Q = []
    tiles_U = []
    for iy in range(n_tiles_y):
        for ix in range(n_tiles_x):
            q_tile = Q[iy*tile_ny:(iy+1)*tile_ny, ix*tile_nx:(ix+1)*tile_nx]
            u_tile = U[iy*tile_ny:(iy+1)*tile_ny, ix*tile_nx:(ix+1)*tile_nx]
            tiles_Q.append(q_tile)
            tiles_U.append(u_tile)

    rng = np.random.default_rng(seed)
    beta_samples = np.zeros(n_bootstrap)

    for b in range(n_bootstrap):
        idx = rng.integers(0, n_tiles, size=n_tiles)
        # Stitch resampled tiles back into a map
        Q_boot = np.zeros_like(Q[:n_tiles_y*tile_ny, :n_tiles_x*tile_nx])
        U_boot = np.zeros_like(U[:n_tiles_y*tile_ny, :n_tiles_x*tile_nx])
        k = 0
        for iy in range(n_tiles_y):
            for ix in range(n_tiles_x):
                Q_boot[iy*tile_ny:(iy+1)*tile_ny, ix*tile_nx:(ix+1)*tile_nx] = tiles_Q[idx[k]]
                U_boot[iy*tile_ny:(iy+1)*tile_ny, ix*tile_nx:(ix+1)*tile_nx] = tiles_U[idx[k]]
                k += 1

        E_b, B_b, lx_b, ly_b = qu_to_eb_flat(Q_boot, U_boot, pixel_size_rad)
        _, CEE_b, CBB_b, CEB_b = compute_power_spectra(E_b, B_b, lx_b, ly_b, l_bins)
        _, beta_b = estimate_beta(CEE_b, CBB_b, CEB_b)
        beta_samples[b] = beta_b

    sigma_deg = np.std(beta_samples)
    return beta_deg, sigma_deg, beta_samples, (l_c, C_EE, C_BB, C_EB)


# ─────────────────────────────────────────────────────────────────────────────
# Map loaders
# ─────────────────────────────────────────────────────────────────────────────

def load_act_dr6(filepath):
    """
    Load ACT DR6 IQU map from FITS file.
    Expected shape: (3, 10320, 43200)  — I=data[0], Q=data[1], U=data[2]
    Pixel scale: ~30 arcsec = 30/3600 * pi/180 rad
    """
    from astropy.io import fits
    print(f"Loading ACT DR6 from {filepath} ...")
    with fits.open(filepath, memmap=True) as hdul:
        hdr = hdul[0].header
        data = hdul[0].data
        Q = np.array(data[1], dtype=np.float64)
        U = np.array(data[2], dtype=np.float64)
        print(f"  Map shape: {Q.shape}, dtype: {Q.dtype}")

    # ACT DR6 pixel scale ~30 arcsec
    cdelt = abs(hdr.get("CDELT2", 30.0 / 3600.0))  # degrees per pixel
    pixel_size_rad = np.radians(cdelt)
    print(f"  Pixel scale: {np.degrees(pixel_size_rad)*3600:.1f} arcsec")

    # Replace NaN/inf with zero (masked pixels)
    Q = np.nan_to_num(Q, nan=0.0, posinf=0.0, neginf=0.0)
    U = np.nan_to_num(U, nan=0.0, posinf=0.0, neginf=0.0)

    return Q, U, pixel_size_rad


def load_planck_smica(filepath):
    """
    Load Planck SMICA IQU HEALPix map and project to flat sky.
    Assumes full-sky HEALPix FITS file with columns I, Q, U.
    """
    import healpy as hp
    from astropy.io import fits

    print(f"Loading Planck SMICA from {filepath} ...")
    data, hdr = hp.read_map(filepath, field=(0, 1, 2), verbose=False)
    Q_hp = data[1]
    U_hp = data[2]

    nside = hp.get_nside(Q_hp)
    print(f"  NSIDE={nside}, Npix={len(Q_hp)}")

    # Project a ~20x20 degree patch around the north Galactic pole to flat sky
    # Use gnomonic projection
    ra0, dec0 = 180.0, 89.0   # degrees (near NGP, low foreground)
    patch_size_deg = 20.0
    npix_side = 512
    pixel_size_deg = patch_size_deg / npix_side
    pixel_size_rad = np.radians(pixel_size_deg)

    # Build RA/Dec grid for the patch
    ra_arr  = ra0  + (np.arange(npix_side) - npix_side/2) * pixel_size_deg
    dec_arr = dec0 + (np.arange(npix_side) - npix_side/2) * pixel_size_deg
    RA, DEC = np.meshgrid(ra_arr, dec_arr)

    theta = np.radians(90.0 - DEC.ravel())
    phi   = np.radians(RA.ravel())
    pix   = hp.ang2pix(nside, theta, phi)

    Q = Q_hp[pix].reshape(npix_side, npix_side)
    U = U_hp[pix].reshape(npix_side, npix_side)
    Q = np.nan_to_num(Q, nan=0.0)
    U = np.nan_to_num(U, nan=0.0)

    print(f"  Extracted {npix_side}x{npix_side} patch, pixel={pixel_size_deg*60:.1f} arcmin")
    return Q, U, pixel_size_rad


# ─────────────────────────────────────────────────────────────────────────────
# Simulation mode — inject known beta and recover it
# ─────────────────────────────────────────────────────────────────────────────

def simulate_qu_map(beta_inject_deg, npix=512, pixel_size_arcmin=1.5,
                    l_peak=1000, seed=0):
    """
    Generate a simulated Q/U map with a known birefringence angle injected.

    Physics convention (Minami & Komatsu 2020):
    Birefringence rotates the polarization plane by beta, which in terms of
    Stokes parameters means (Q+iU)_obs = exp(2i*beta) * (Q+iU)_true, giving:
        Q_obs = Q_true * cos(2*beta) - U_true * sin(2*beta)
        U_obs = Q_true * sin(2*beta) + U_true * cos(2*beta)
    In Fourier space, this mixes E/B as:
        E_obs = E_true * cos(2*beta) - B_true * sin(2*beta)
        B_obs = E_true * sin(2*beta) + B_true * cos(2*beta)
    For a pure-E sky this gives C_EB > 0 for beta > 0, and the estimator
    beta = 0.5 * arctan(2*C_EB / (C_EE - C_BB)) correctly recovers beta.

    Procedure
    ---------
    1. Draw Gaussian random E and B fields from fiducial power spectra.
    2. Apply birefringence rotation in Fourier space (above equations).
    3. Convert back to Q/U and inverse FFT.

    Parameters
    ----------
    beta_inject_deg : float
        Known birefringence angle in degrees (positive = CCW rotation).
    npix : int
        Number of pixels per side.
    pixel_size_arcmin : float
        Pixel size in arcminutes.
    l_peak : float
        Peak multipole for the fiducial EE power spectrum (in rad^-1 units).
    seed : int

    Returns
    -------
    Q, U : 2-D arrays
    pixel_size_rad : float
    """
    rng = np.random.default_rng(seed)
    beta_rad = np.radians(beta_inject_deg)

    pixel_size_rad = np.radians(pixel_size_arcmin / 60.0)

    # Frequency grids (rad^-1)
    lx_1d = np.fft.fftfreq(npix, d=pixel_size_rad)
    ly_1d = np.fft.fftfreq(npix, d=pixel_size_rad)
    lx, ly = np.meshgrid(lx_1d, ly_1d)
    l_abs = np.sqrt(lx**2 + ly**2)
    phi_l = np.arctan2(ly, lx)
    cos2  = np.cos(2 * phi_l)
    sin2  = np.sin(2 * phi_l)

    # Fiducial EE power spectrum: Gaussian peak around l_peak
    C_EE_fid = np.exp(-0.5 * ((l_abs - l_peak) / (l_peak / 3))**2)
    C_EE_fid[l_abs == 0] = 0.0

    # Small lensing B-mode contamination (~1% of EE at peak)
    C_BB_fid = 0.01 * C_EE_fid

    # Draw complex Gaussian realisations of the TRUE (unrotated) fields
    amp_E = np.sqrt(0.5 * C_EE_fid) * (rng.standard_normal((npix, npix))
                                        + 1j * rng.standard_normal((npix, npix)))
    amp_B = np.sqrt(0.5 * C_BB_fid) * (rng.standard_normal((npix, npix))
                                        + 1j * rng.standard_normal((npix, npix)))

    # Apply birefringence: polarization-plane rotation by beta
    #   E_obs = E*cos(2b) - B*sin(2b)
    #   B_obs = E*sin(2b) + B*cos(2b)
    E_obs = amp_E * np.cos(2 * beta_rad) - amp_B * np.sin(2 * beta_rad)
    B_obs = amp_E * np.sin(2 * beta_rad) + amp_B * np.cos(2 * beta_rad)

    # Convert observed E/B -> Q/U in Fourier space
    #   Q(l) = E(l)*cos(2*phi_l) - B(l)*sin(2*phi_l)
    #   U(l) = E(l)*sin(2*phi_l) + B(l)*cos(2*phi_l)
    Q_l = E_obs * cos2 - B_obs * sin2
    U_l = E_obs * sin2 + B_obs * cos2

    # Inverse FFT to real space.
    # numpy: ifft2(fft2(x)) = x exactly — no extra scaling needed.
    # The *npix was incorrect (though it cancels in the power-spectrum ratios,
    # it inflates the map values and makes block-bootstrap discontinuities larger).
    Q = np.fft.ifft2(Q_l).real
    U = np.fft.ifft2(U_l).real

    return Q.astype(np.float64), U.astype(np.float64), pixel_size_rad


# ─────────────────────────────────────────────────────────────────────────────
# Plotting
# ─────────────────────────────────────────────────────────────────────────────

def plot_results(l_centers, C_EE, C_BB, C_EB,
                 beta_deg, sigma_deg, beta_samples,
                 mode, output_path):
    """Generate diagnostic figure: power spectra + beta posterior."""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle(f"Cosmic Birefringence Analysis — {mode.upper()}", fontsize=13)

    # --- Panel 1: EE, BB, EB power spectra ---
    ax = axes[0]
    ax.loglog(l_centers, C_EE, color="#2166ac", label=r"$C^{EE}_\ell$", lw=2)
    ax.loglog(l_centers, C_BB, color="#d6604d", label=r"$C^{BB}_\ell$", lw=2)
    ax.loglog(l_centers, np.abs(C_EB), color="#4dac26", label=r"$|C^{EB}_\ell|$",
              lw=2, ls="--")
    ax.set_xlabel(r"$\ell$ (rad$^{-1}$)", fontsize=11)
    ax.set_ylabel(r"Power spectrum", fontsize=11)
    ax.set_title("Angular Power Spectra", fontsize=11)
    ax.legend(fontsize=10)
    ax.grid(True, which="both", alpha=0.3)

    # --- Panel 2: C_EB / (C_EE - C_BB) as function of l ---
    ax = axes[1]
    ratio = C_EB / (C_EE - C_BB + 1e-30)
    ax.semilogx(l_centers, ratio, color="#762a83", lw=1.5, alpha=0.8)
    beta_rad_pred = np.radians(BETA_BOUNCE_PRED)
    ax.axhline(0.5 * np.sin(4 * beta_rad_pred), color="orange",
               ls="--", lw=1.5, label=f"Prediction ({BETA_BOUNCE_PRED}°)")
    ax.axhline(0.0, color="k", ls=":", lw=1)
    ax.set_xlabel(r"$\ell$ (rad$^{-1}$)", fontsize=11)
    ax.set_ylabel(r"$C^{EB}_\ell \,/\, (C^{EE}_\ell - C^{BB}_\ell)$", fontsize=11)
    ax.set_title(r"EB Mixing Ratio", fontsize=11)
    ax.legend(fontsize=10)
    ax.grid(True, which="both", alpha=0.3)

    # --- Panel 3: Beta posterior from bootstrap ---
    ax = axes[2]
    bins = np.linspace(beta_deg - 5*sigma_deg, beta_deg + 5*sigma_deg, 50)
    ax.hist(beta_samples, bins=bins, density=True,
            color="#4393c3", alpha=0.7, label="Bootstrap samples")

    # Overlay Gaussian fit
    x = np.linspace(bins[0], bins[-1], 300)
    ax.plot(x, norm.pdf(x, beta_deg, sigma_deg), "k-", lw=2, label="Gaussian fit")

    # Reference lines
    ax.axvline(beta_deg, color="navy", lw=2, ls="-",
               label=f"Measured: {beta_deg:.3f}°")
    ax.axvline(BETA_BOUNCE_PRED, color="orange", lw=2, ls="--",
               label=f"Bounce pred: {BETA_BOUNCE_PRED}°")
    ax.axvline(BETA_OBSERVED, color="green", lw=2, ls="-.",
               label=f"Observed: {BETA_OBSERVED}°")
    # Shaded 1-sigma region around observed
    ax.axvspan(BETA_OBSERVED - BETA_OBS_ERR, BETA_OBSERVED + BETA_OBS_ERR,
               color="green", alpha=0.10, label=f"Obs 1σ band")

    ax.set_xlabel(r"$\beta$ (degrees)", fontsize=11)
    ax.set_ylabel("Probability density", fontsize=11)
    ax.set_title(r"Birefringence Angle $\beta$ Posterior", fontsize=11)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Tension label
    if sigma_deg > 0:
        tension_obs   = abs(beta_deg - BETA_OBSERVED) / BETA_OBS_ERR
        tension_pred  = abs(beta_deg - BETA_BOUNCE_PRED) / sigma_deg
        ax.text(0.97, 0.95,
                f"vs observed: {tension_obs:.2f}σ\nvs prediction: {tension_pred:.2f}σ",
                transform=ax.transAxes, ha="right", va="top",
                fontsize=9, bbox=dict(boxstyle="round", fc="white", alpha=0.8))

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Figure saved to {output_path}")


# ─────────────────────────────────────────────────────────────────────────────
# Main driver
# ─────────────────────────────────────────────────────────────────────────────

def run_analysis(Q, U, pixel_size_rad, mode, n_bootstrap=500, l_bins=None):
    """Full birefringence pipeline: E/B decomp -> power spectra -> beta -> bootstrap."""

    print(f"\n[{mode.upper()}] Map shape: {Q.shape}, "
          f"pixel size: {np.degrees(pixel_size_rad)*3600:.1f} arcsec")

    t0 = time.time()
    beta_deg, sigma_deg, beta_samples, (l_c, C_EE, C_BB, C_EB) = \
        bootstrap_beta(Q, U, pixel_size_rad, n_bootstrap=n_bootstrap, l_bins=l_bins)
    t1 = time.time()

    print(f"\n=== Results ({mode.upper()}) ===")
    print(f"  beta            = {beta_deg:.4f} +/- {sigma_deg:.4f} deg")
    print(f"  Bounce pred     = {BETA_BOUNCE_PRED:.4f} deg")
    print(f"  Observed signal = {BETA_OBSERVED:.4f} +/- {BETA_OBS_ERR:.4f} deg")

    if sigma_deg > 0:
        tension_obs  = abs(beta_deg - BETA_OBSERVED)  / np.sqrt(BETA_OBS_ERR**2 + sigma_deg**2)
        tension_pred = abs(beta_deg - BETA_BOUNCE_PRED) / sigma_deg
        print(f"  Tension vs observed  = {tension_obs:.2f}σ (combined)")
        print(f"  Tension vs pred      = {tension_pred:.2f}σ")

    print(f"  Bootstrap time  = {t1-t0:.1f}s  (N={n_bootstrap})")

    # Save numerical results
    results = {
        "mode":             mode,
        "beta_deg":         float(beta_deg),
        "sigma_deg":        float(sigma_deg),
        "beta_bounce_pred": BETA_BOUNCE_PRED,
        "beta_observed":    BETA_OBSERVED,
        "beta_obs_err":     BETA_OBS_ERR,
        "tension_vs_obs":   float(abs(beta_deg - BETA_OBSERVED)
                                  / np.sqrt(BETA_OBS_ERR**2 + sigma_deg**2))
                            if sigma_deg > 0 else None,
        "tension_vs_pred":  float(abs(beta_deg - BETA_BOUNCE_PRED) / sigma_deg)
                            if sigma_deg > 0 else None,
        "n_bootstrap":      n_bootstrap,
        "map_shape":        list(Q.shape),
        "pixel_size_arcmin": float(np.degrees(pixel_size_rad) * 60),
        "l_centers":        l_c.tolist(),
        "C_EE":             C_EE.tolist(),
        "C_BB":             C_BB.tolist(),
        "C_EB":             C_EB.tolist(),
        "beta_samples":     beta_samples.tolist(),
    }

    json_path = os.path.join(OUTPUT_DIR, f"birefringence_results_{mode}.json")
    with open(json_path, "w") as fh:
        json.dump(results, fh, indent=2)
    print(f"Results saved to {json_path}")

    fig_path = os.path.join(OUTPUT_DIR, f"birefringence_{mode}.png")
    plot_results(l_c, C_EE, C_BB, C_EB,
                 beta_deg, sigma_deg, beta_samples,
                 mode, fig_path)

    return results


def main():
    parser = argparse.ArgumentParser(
        description="ACT DR6 / Planck cosmic birefringence estimator")
    parser.add_argument("--mode", choices=["sim", "act", "planck"], default="sim",
                        help="Data source: sim (simulation), act (ACT DR6), planck (SMICA)")
    parser.add_argument("--input", default=None,
                        help="Path to input FITS file (required for act/planck modes)")
    parser.add_argument("--beta_inject", type=float, default=0.27,
                        help="[sim mode] Injected birefringence angle in degrees")
    parser.add_argument("--npix", type=int, default=512,
                        help="[sim mode] Map size in pixels per side")
    parser.add_argument("--pixel_arcmin", type=float, default=1.5,
                        help="[sim mode] Pixel size in arcminutes")
    parser.add_argument("--n_bootstrap", type=int, default=500,
                        help="Number of bootstrap resamples")
    parser.add_argument("--seed", type=int, default=42,
                        help="[sim mode] Random seed")

    args = parser.parse_args()

    print("=" * 60)
    print("  Cosmic Birefringence Estimator")
    print(f"  Mode: {args.mode}")
    print("=" * 60)

    if args.mode == "sim":
        print(f"\nGenerating simulated Q/U map with beta_inject = {args.beta_inject} deg ...")
        Q, U, pixel_size_rad = simulate_qu_map(
            beta_inject_deg=args.beta_inject,
            npix=args.npix,
            pixel_size_arcmin=args.pixel_arcmin,
            seed=args.seed,
        )
        print(f"  Q range: [{Q.min():.3e}, {Q.max():.3e}]")
        print(f"  U range: [{U.min():.3e}, {U.max():.3e}]")
        results = run_analysis(Q, U, pixel_size_rad, mode="sim",
                               n_bootstrap=args.n_bootstrap)

    elif args.mode == "act":
        if args.input is None:
            print("ERROR: --input required for ACT mode")
            sys.exit(1)
        Q, U, pixel_size_rad = load_act_dr6(args.input)
        results = run_analysis(Q, U, pixel_size_rad, mode="act",
                               n_bootstrap=args.n_bootstrap)

    elif args.mode == "planck":
        if args.input is None:
            print("ERROR: --input required for Planck mode")
            sys.exit(1)
        Q, U, pixel_size_rad = load_planck_smica(args.input)
        results = run_analysis(Q, U, pixel_size_rad, mode="planck",
                               n_bootstrap=args.n_bootstrap)

    print("\nDone.")
    return results


if __name__ == "__main__":
    main()
