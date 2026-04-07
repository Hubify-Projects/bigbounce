#!/usr/bin/env python3
"""
Planck CMB Lensing × Anomaly Cross-Correlation
===============================================
Cross-correlate anomaly sky positions with CMB lensing convergence map.

If anomalies preferentially live in high-convergence regions, they trace
large-scale structure — and we can extract galaxy bias b_g from the
cross-power spectrum amplitude. If b_g differs from standard DESI QSO
bias (~2.5), anomalies may represent a distinct tracer population with
independent cosmological information.

Pipeline:
  1. Load anomaly positions (RA, Dec) from DESI outputs
  2. Load or generate CMB lensing convergence map (HEALPix NSIDE=256)
  3. Pixelize anomaly density into HEALPix map
  4. Compute angular cross-power spectrum C_l^{kappa×g} in 20 ell-bins
  5. Fit galaxy bias b_g from amplitude
  6. Compare with standard DESI QSO bias

If real data unavailable: synthetic 195K positions + synthetic lensing map
with realistic power spectrum.

Output: planck-lensing-xcorr/
"""

import json
import os
import sys
import time
import numpy as np
import pandas as pd
from datetime import datetime, timezone
from pathlib import Path
from scipy import stats

import torch
from torch.utils.data import DataLoader, TensorDataset

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/workspace/bigbounce/outputs/planck-lensing-xcorr"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

NSIDE = 256
NPIX = 12 * NSIDE ** 2
ELL_MIN = 10
ELL_MAX = 1000
N_ELL_BINS = 20


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer,)):
            return int(obj)
        if isinstance(obj, (np.floating,)):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.bool_):
            return bool(obj)
        return super().default(obj)


# ═══════════════════════════════════════════════════════
# HEALPix utilities (no healpy dependency)
# ═══════════════════════════════════════════════════════

def try_import_healpy():
    """Try to import healpy, return None if unavailable."""
    try:
        import healpy as hp
        return hp
    except ImportError:
        return None


def radec_to_thetaphi(ra, dec):
    """Convert RA/Dec (degrees) to healpy theta/phi (radians)."""
    theta = np.radians(90.0 - dec)
    phi = np.radians(ra)
    return theta, phi


def simple_ang2pix(nside, theta, phi):
    """Simplified ring-scheme angle-to-pixel. Uses healpy if available."""
    hp = try_import_healpy()
    if hp is not None:
        return hp.ang2pix(nside, theta, phi)
    # Fallback: approximate pixel assignment
    npix = 12 * nside * nside
    # z = cos(theta)
    z = np.cos(theta)
    # Ring index (approximate)
    za = np.abs(z)
    tt = np.mod(phi, 2 * np.pi) / (np.pi / 2)
    pixels = np.zeros(len(theta), dtype=np.int64)
    # Polar caps
    polar = za > 2.0 / 3.0
    equatorial = ~polar
    if polar.any():
        tp = tt[polar]
        zp = z[polar]
        ntt = np.floor(tp).astype(int)
        ntt = np.clip(ntt, 0, 3)
        tmp = nside * np.sqrt(3.0 * (1.0 - za[polar]))
        jp = np.clip(np.floor(tmp * (tp - ntt)).astype(int) + 1, 1, nside)
        jr = np.clip(np.floor(tmp).astype(int) + 1, 1, nside)
        north = zp > 0
        pix_n = 2 * jr[north] * (jr[north] - 1) + jp[north] - 1
        pix_s = npix - 2 * jr[~north] * (jr[~north] + 1) + jp[~north] - 1
        idx_polar = np.where(polar)[0]
        pixels[idx_polar[north]] = np.clip(pix_n, 0, npix - 1)
        pixels[idx_polar[~north]] = np.clip(pix_s, 0, npix - 1)
    if equatorial.any():
        te = tt[equatorial]
        ze = z[equatorial]
        jp = np.floor(nside * (0.5 + te / 4.0 - ze * nside * 3.0 / (8.0 * nside))).astype(int)
        jr = np.floor(nside * (ze + 2.0 / 3.0) * 3.0 / 4.0).astype(int) + nside
        ring_pix = 4 * nside
        ncap = 2 * nside * (nside - 1)
        pix_e = ncap + (jr - nside) * ring_pix + np.clip(jp, 0, ring_pix - 1)
        pixels[np.where(equatorial)[0]] = np.clip(pix_e, 0, npix - 1)
    return pixels


# ═══════════════════════════════════════════════════════
# Data Loading
# ═══════════════════════════════════════════════════════

SEARCH_PATHS = [
    Path("/workspace/bigbounce/outputs/desi-dr1"),
    Path("/workspace/bigbounce/pipelines/h200_results/desi_dr1"),
    Path("/workspace/bigbounce/outputs"),
]


def load_anomaly_positions():
    """Load RA/Dec of anomalies."""
    print("  Searching for anomaly positions...")
    for sp in SEARCH_PATHS:
        if not sp.exists():
            continue
        for pattern in ["*anomal*.csv", "*catalog*.csv", "*scores*.csv",
                        "*anomal*.parquet"]:
            for f in sorted(sp.glob(pattern)):
                try:
                    df = pd.read_parquet(f) if f.suffix == ".parquet" else pd.read_csv(f, nrows=200000)
                    if "ra" in df.columns and "dec" in df.columns:
                        ra = df["ra"].values
                        dec = df["dec"].values
                        valid = np.isfinite(ra) & np.isfinite(dec)
                        print(f"  Found: {f} ({valid.sum()} positions)")
                        scores = df["anomaly_score"].values if "anomaly_score" in df.columns else None
                        return ra[valid], dec[valid], scores[valid] if scores is not None else None, str(f)
                except Exception:
                    continue
    return None, None, None, None


def load_lensing_map():
    """Load Planck lensing convergence map."""
    hp = try_import_healpy()
    lensing_paths = [
        Path("/workspace/bigbounce/data/planck/COM_Lensing-Szdeproj_4096_R3.00/MV/dat_klm.fits"),
        Path("/workspace/bigbounce/data/planck_lensing.fits"),
        Path("/workspace/data/planck_lensing_kappa.fits"),
    ]
    if hp is not None:
        for lp in lensing_paths:
            if lp.exists():
                try:
                    kappa = hp.read_map(lp)
                    if hp.get_nside(kappa) != NSIDE:
                        kappa = hp.ud_grade(kappa, NSIDE)
                    print(f"  Loaded lensing map: {lp}")
                    return kappa, str(lp)
                except Exception as e:
                    print(f"  Error loading {lp}: {e}")
    return None, None


def generate_synthetic_lensing_map(nside=256):
    """Generate synthetic lensing convergence map with realistic power spectrum."""
    print(f"  Generating synthetic lensing map (NSIDE={nside})")
    np.random.seed(123)
    npix = 12 * nside * nside
    lmax = 3 * nside - 1

    # Realistic CMB lensing power spectrum: C_l^{kappa kappa} ~ l^2 * C_l^{phi phi}
    # Approximate: C_l^kk ~ A * l^0.5 * exp(-l/500) for l > 2
    ells = np.arange(lmax + 1, dtype=float)
    cl_kk = np.zeros(lmax + 1)
    cl_kk[2:] = 1e-7 * (ells[2:] / 100.0) ** 0.5 * np.exp(-ells[2:] / 800.0)

    hp = try_import_healpy()
    if hp is not None:
        kappa = hp.synfast(cl_kk, nside, verbose=False)
        return kappa, "synthetic_healpy"

    # Fallback: generate correlated Gaussian random field on the sphere
    # Use spherical harmonic approach approximated via FFT on theta/phi grid
    kappa = np.random.normal(0, np.sqrt(cl_kk.sum() / npix), npix).astype(np.float64)
    # Smooth with approximate beam
    return kappa, "synthetic_approximate"


def generate_synthetic_positions(n_objects=195000, bias=2.5, kappa_map=None):
    """Generate synthetic anomaly positions correlated with lensing map."""
    print(f"  Generating synthetic positions: {n_objects} objects, bias={bias}")
    np.random.seed(42)

    if kappa_map is not None:
        # Probability proportional to 1 + bias * kappa
        prob = 1.0 + bias * kappa_map
        prob = np.clip(prob, 0.01, None)
        prob /= prob.sum()
        # Draw pixel indices
        pixels = np.random.choice(len(kappa_map), size=n_objects, p=prob)
        # Convert pixels to RA/Dec
        hp = try_import_healpy()
        if hp is not None:
            theta, phi = hp.pix2ang(NSIDE, pixels)
        else:
            # Approximate: uniform sampling within pixel
            theta = np.arccos(1 - 2 * pixels / len(kappa_map))
            phi = 2 * np.pi * (pixels % (4 * NSIDE)) / (4 * NSIDE)
        ra = np.degrees(phi)
        dec = 90.0 - np.degrees(theta)
    else:
        # DESI-like footprint
        ra = np.random.uniform(100, 280, n_objects)
        dec = np.random.uniform(-20, 80, n_objects)

    scores = np.exp(np.random.normal(3.0, 1.5, n_objects))
    return ra, dec, scores


# ═══════════════════════════════════════════════════════
# Cross-Power Spectrum
# ═══════════════════════════════════════════════════════

def compute_overdensity_map(ra, dec, nside=256, scores=None):
    """Convert anomaly positions to HEALPix overdensity map."""
    theta, phi = radec_to_thetaphi(ra, dec)
    pixels = simple_ang2pix(nside, theta, phi)
    npix = 12 * nside * nside

    # Count map (or score-weighted)
    if scores is not None:
        count_map = np.zeros(npix, dtype=np.float64)
        np.add.at(count_map, pixels, scores)
    else:
        count_map = np.bincount(pixels, minlength=npix).astype(np.float64)

    # Mask empty pixels (outside survey footprint)
    occupied = count_map > 0
    mean_count = count_map[occupied].mean() if occupied.any() else 1.0

    # Overdensity: delta = n/nbar - 1
    delta = np.zeros(npix, dtype=np.float64)
    delta[occupied] = count_map[occupied] / mean_count - 1.0

    # Apply simple mask
    mask = occupied.astype(np.float64)
    f_sky = mask.sum() / npix

    print(f"  Overdensity map: {occupied.sum()} occupied pixels, f_sky={f_sky:.3f}")
    return delta, mask, f_sky


def compute_cross_power_spectrum(map1, map2, mask, nside=256, n_bins=20,
                                  ell_min=10, ell_max=1000):
    """Compute angular cross-power spectrum C_l using pseudo-Cl."""
    hp = try_import_healpy()

    if hp is not None:
        # Apply mask
        m1 = map1 * mask
        m2 = map2 * mask
        f_sky = mask.sum() / len(mask)

        # anafast for cross-spectrum
        lmax = min(3 * nside - 1, ell_max + 100)
        cl_cross = hp.anafast(m1, m2, lmax=lmax)
        cl_auto1 = hp.anafast(m1, lmax=lmax)
        cl_auto2 = hp.anafast(m2, lmax=lmax)

        # Correct for f_sky
        cl_cross /= f_sky
        cl_auto1 /= f_sky
        cl_auto2 /= f_sky
    else:
        # Approximate: use pixel-space correlation
        lmax = min(3 * nside - 1, ell_max + 100)
        npix = len(map1)
        f_sky = mask.sum() / npix

        # FFT-based approximate power spectrum
        # Treat the maps as 1D signals for a rough estimate
        m1 = map1 * mask
        m2 = map2 * mask
        n = len(m1)
        fft1 = np.fft.rfft(m1)
        fft2 = np.fft.rfft(m2)
        raw_cross = np.real(fft1 * np.conj(fft2)) / n
        raw_auto1 = np.abs(fft1) ** 2 / n
        raw_auto2 = np.abs(fft2) ** 2 / n

        # Map FFT frequencies to approximate ell values
        freqs = np.fft.rfftfreq(n, d=1.0 / (2 * np.sqrt(npix)))
        ells_approx = freqs * 2 * np.pi
        cl_cross = np.interp(np.arange(lmax + 1), ells_approx[:lmax+1],
                              raw_cross[:lmax+1]) / max(f_sky, 0.01)
        cl_auto1 = np.interp(np.arange(lmax + 1), ells_approx[:lmax+1],
                              raw_auto1[:lmax+1]) / max(f_sky, 0.01)
        cl_auto2 = np.interp(np.arange(lmax + 1), ells_approx[:lmax+1],
                              raw_auto2[:lmax+1]) / max(f_sky, 0.01)

    # Bin into ell-bins
    ell_edges = np.logspace(np.log10(ell_min), np.log10(ell_max), n_bins + 1)
    ell_centers = np.sqrt(ell_edges[:-1] * ell_edges[1:])

    cl_binned = np.zeros(n_bins)
    cl_err = np.zeros(n_bins)
    n_modes = np.zeros(n_bins)

    ells = np.arange(len(cl_cross))
    for i in range(n_bins):
        in_bin = (ells >= ell_edges[i]) & (ells < ell_edges[i + 1])
        if in_bin.sum() > 0:
            cl_binned[i] = np.mean(cl_cross[in_bin])
            # Knox formula error estimate
            delta_ell = ell_edges[i + 1] - ell_edges[i]
            ell_c = ell_centers[i]
            n_modes[i] = f_sky * (2 * ell_c + 1) * delta_ell
            if n_modes[i] > 0:
                auto1_bin = np.mean(cl_auto1[in_bin])
                auto2_bin = np.mean(cl_auto2[in_bin])
                cl_err[i] = np.sqrt(
                    (cl_binned[i] ** 2 + auto1_bin * auto2_bin) / max(n_modes[i], 1)
                )

    return ell_centers, cl_binned, cl_err, n_modes


# ═══════════════════════════════════════════════════════
# Galaxy Bias Fitting
# ═══════════════════════════════════════════════════════

def fit_galaxy_bias(ell_centers, cl_cross, cl_err, cl_kk_theory=None):
    """Fit galaxy bias b_g from cross-power spectrum amplitude."""
    # C_l^{kg} = b_g * C_l^{kk} (in linear bias approximation)
    # If we don't have theory C_l^{kk}, estimate from the cross-spectrum shape

    if cl_kk_theory is None:
        # Use approximate theory: C_l^kk ~ A * (l/100)^0.5 * exp(-l/800)
        cl_kk_theory = 1e-7 * (ell_centers / 100.0) ** 0.5 * np.exp(-ell_centers / 800.0)

    # Weighted least squares: b_g = sum(w * cl_cross / cl_kk) / sum(w)
    valid = (cl_err > 0) & (cl_kk_theory > 0) & np.isfinite(cl_cross)
    if valid.sum() < 3:
        return None, None

    w = 1.0 / cl_err[valid] ** 2
    ratio = cl_cross[valid] / cl_kk_theory[valid]
    b_g = np.sum(w * ratio) / np.sum(w)
    b_g_err = 1.0 / np.sqrt(np.sum(w))

    return float(b_g), float(b_g_err)


# ═══════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════

def main():
    print("=" * 70)
    print("PLANCK CMB LENSING x ANOMALY CROSS-CORRELATION")
    print("=" * 70)
    t_start = time.time()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"\n  Device: {device}")

    # Load lensing map
    print("\n[1/5] Loading CMB lensing convergence map...")
    kappa_map, lensing_source = load_lensing_map()
    if kappa_map is None:
        kappa_map, lensing_source = generate_synthetic_lensing_map(nside=NSIDE)
    print(f"  Lensing source: {lensing_source}")
    print(f"  Kappa stats: mean={kappa_map.mean():.6f}, std={kappa_map.std():.6f}")

    # Load anomaly positions
    print("\n[2/5] Loading anomaly positions...")
    ra, dec, scores, pos_source = load_anomaly_positions()
    data_source = "real"
    if ra is None:
        print("  No real positions — generating synthetic (bias=2.5)")
        ra, dec, scores = generate_synthetic_positions(
            n_objects=195000, bias=2.5, kappa_map=kappa_map
        )
        pos_source = "synthetic"
        data_source = "synthetic"
    print(f"  Positions: {len(ra)} objects")
    print(f"  RA range: [{ra.min():.1f}, {ra.max():.1f}]")
    print(f"  Dec range: [{dec.min():.1f}, {dec.max():.1f}]")

    # Build overdensity map
    print("\n[3/5] Building anomaly overdensity map...")
    delta_g, mask, f_sky = compute_overdensity_map(ra, dec, nside=NSIDE, scores=None)

    # Also build score-weighted version
    delta_g_weighted = None
    if scores is not None:
        delta_g_weighted, _, _ = compute_overdensity_map(ra, dec, nside=NSIDE, scores=scores)

    # Cross-power spectrum
    print("\n[4/5] Computing angular cross-power spectrum...")
    ell_centers, cl_cross, cl_err, n_modes = compute_cross_power_spectrum(
        kappa_map, delta_g, mask, nside=NSIDE,
        n_bins=N_ELL_BINS, ell_min=ELL_MIN, ell_max=ELL_MAX
    )

    # Also with score-weighted map
    cl_weighted = None
    if delta_g_weighted is not None:
        _, cl_weighted, cl_weighted_err, _ = compute_cross_power_spectrum(
            kappa_map, delta_g_weighted, mask, nside=NSIDE,
            n_bins=N_ELL_BINS, ell_min=ELL_MIN, ell_max=ELL_MAX
        )

    # Detection significance
    # SNR per bin and cumulative
    snr_per_bin = np.where(cl_err > 0, cl_cross / cl_err, 0)
    snr_cumulative = np.sqrt(np.sum(snr_per_bin ** 2))

    print(f"\n  Cross-power spectrum results:")
    print(f"  {'ell':>8s} {'C_l^{kg}':>12s} {'error':>12s} {'SNR':>8s}")
    print(f"  {'-'*44}")
    for i in range(N_ELL_BINS):
        print(f"  {ell_centers[i]:8.1f} {cl_cross[i]:12.4e} {cl_err[i]:12.4e} {snr_per_bin[i]:8.2f}")
    print(f"\n  Cumulative SNR: {snr_cumulative:.2f}")

    # Fit galaxy bias
    print("\n[5/5] Fitting galaxy bias...")
    b_g, b_g_err = fit_galaxy_bias(ell_centers, cl_cross, cl_err)

    if b_g is not None:
        print(f"  Galaxy bias: b_g = {b_g:.3f} +/- {b_g_err:.3f}")
        print(f"  Standard DESI QSO bias: ~2.5")
        if b_g_err > 0:
            deviation = abs(b_g - 2.5) / b_g_err
            print(f"  Deviation from QSO bias: {deviation:.1f}sigma")
    else:
        print("  Could not fit galaxy bias (insufficient valid bins)")

    # Null test: random positions
    print("\n  Running null test (random positions)...")
    ra_null = np.random.uniform(ra.min(), ra.max(), len(ra))
    dec_null = np.random.uniform(dec.min(), dec.max(), len(ra))
    delta_null, mask_null, _ = compute_overdensity_map(ra_null, dec_null, nside=NSIDE)
    _, cl_null, cl_null_err, _ = compute_cross_power_spectrum(
        kappa_map, delta_null, mask_null, nside=NSIDE,
        n_bins=N_ELL_BINS, ell_min=ELL_MIN, ell_max=ELL_MAX
    )
    snr_null = np.sqrt(np.sum(np.where(cl_null_err > 0, cl_null / cl_null_err, 0) ** 2))
    print(f"  Null test SNR: {snr_null:.2f} (should be ~1)")
    print(f"  Signal/Null ratio: {snr_cumulative / max(snr_null, 0.01):.1f}x")

    # Save
    total_time = time.time() - t_start

    power_spectrum_table = []
    for i in range(N_ELL_BINS):
        row = {
            "ell_center": float(ell_centers[i]),
            "cl_cross": float(cl_cross[i]),
            "cl_error": float(cl_err[i]),
            "snr": float(snr_per_bin[i]),
            "n_modes": float(n_modes[i]),
            "cl_null": float(cl_null[i]),
        }
        if cl_weighted is not None:
            row["cl_weighted"] = float(cl_weighted[i])
        power_spectrum_table.append(row)

    summary = {
        "experiment": "planck_lensing_xcorr",
        "description": "CMB lensing x anomaly angular cross-power spectrum",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "data_source": data_source,
        "lensing_source": lensing_source,
        "position_source": pos_source,
        "n_anomalies": int(len(ra)),
        "healpix_nside": NSIDE,
        "f_sky": float(f_sky),
        "ell_range": [ELL_MIN, ELL_MAX],
        "n_ell_bins": N_ELL_BINS,
        "results": {
            "cumulative_snr": float(snr_cumulative),
            "galaxy_bias": float(b_g) if b_g is not None else None,
            "galaxy_bias_error": float(b_g_err) if b_g_err is not None else None,
            "desi_qso_bias_reference": 2.5,
            "bias_deviation_sigma": float(abs(b_g - 2.5) / b_g_err) if b_g is not None and b_g_err and b_g_err > 0 else None,
        },
        "null_test": {
            "snr_null": float(snr_null),
            "signal_to_null_ratio": float(snr_cumulative / max(snr_null, 0.01)),
        },
        "power_spectrum": power_spectrum_table,
        "kappa_map_stats": {
            "mean": float(kappa_map.mean()),
            "std": float(kappa_map.std()),
            "min": float(kappa_map.min()),
            "max": float(kappa_map.max()),
        },
        "total_time_s": float(total_time),
        "device": str(device),
    }

    with open(OUTPUT_DIR / "lensing_xcorr_summary.json", "w") as f:
        json.dump(summary, f, indent=2, cls=NumpyEncoder)

    ps_df = pd.DataFrame(power_spectrum_table)
    ps_df.to_csv(OUTPUT_DIR / "cross_power_spectrum.csv", index=False)

    np.save(OUTPUT_DIR / "anomaly_overdensity_map.npy", delta_g)
    np.save(OUTPUT_DIR / "survey_mask.npy", mask)

    print(f"\n  Saved to: {OUTPUT_DIR}")
    print(f"  Total time: {total_time:.1f}s")

    print("\n" + "=" * 70)
    print("COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
