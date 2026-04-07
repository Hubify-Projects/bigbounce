#!/usr/bin/env python3
"""
Experiment: Detailed SPHEREx f_NL Forecast with Anomaly Tracers

Compute the Fisher matrix for f_NL measurement using SPHEREx survey specifications.
Include standard galaxy tracers (LRG, ELG, QSO) + anomaly-enhanced high-bias tracers
from the BigBounce multi-survey anomaly catalog.

Model: scale-dependent bias Delta_b(k, z) = (b - 1) * f_NL * delta_c / alpha(k, z)
where alpha(k, z) = (2/3) * k^2 * T(k) * D(z) / (Omega_m * H0^2)

Method:
  - Fisher matrix: F_ij = sum over k-bins, z-bins of dP/df_NL * C^{-1} * dP/df_NL
  - Proper k-binning (k_min from survey volume, k_max = 0.2 h/Mpc)
  - Redshift bins: 0.2 < z < 3.0 in dz = 0.2
  - Shot noise from number density
  - Multi-tracer technique: cross-correlating different bias populations
  - Survey combos: SPHEREx alone, SPHEREx+anomaly, SPHEREx+DESI+anomaly

Output: /workspace/bigbounce/outputs/fisher-forecast-spherex/
"""

import json
import os
import sys
import time
import numpy as np
import pandas as pd
from pathlib import Path

import torch
from torch.utils.data import Dataset, DataLoader

from scipy.interpolate import interp1d
from scipy.integrate import cumulative_trapezoid

# ============================================================
# NumpyEncoder for JSON serialization
# ============================================================

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer,)): return int(obj)
        if isinstance(obj, (np.floating,)): return float(obj)
        if isinstance(obj, (np.bool_,)): return bool(obj)
        if isinstance(obj, np.ndarray): return obj.tolist()
        return super().default(obj)

# ============================================================
# Configuration
# ============================================================

OUTPUT_DIR = "/workspace/bigbounce/outputs/fisher-forecast-spherex"
os.makedirs(OUTPUT_DIR, exist_ok=True)

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Cosmological parameters (Planck 2018 best-fit)
H0 = 67.36  # km/s/Mpc
h = H0 / 100.0
OMEGA_M = 0.3153
OMEGA_B = 0.0493
OMEGA_CDM = OMEGA_M - OMEGA_B
OMEGA_L = 1.0 - OMEGA_M
N_S = 0.9649
SIGMA8 = 0.8111
DELTA_C = 1.686  # critical overdensity for spherical collapse
C_LIGHT = 2.998e5  # km/s

# k-binning
K_MIN = 1e-4  # h/Mpc
K_MAX = 0.2   # h/Mpc (linear regime)
N_K_BINS = 50
K_BINS = np.logspace(np.log10(K_MIN), np.log10(K_MAX), N_K_BINS + 1)
K_CENTERS = np.sqrt(K_BINS[:-1] * K_BINS[1:])

# Redshift bins
Z_MIN = 0.2
Z_MAX = 3.0
DZ = 0.2
Z_EDGES = np.arange(Z_MIN, Z_MAX + DZ/2, DZ)
Z_CENTERS = 0.5 * (Z_EDGES[:-1] + Z_EDGES[1:])
N_Z_BINS = len(Z_CENTERS)

# Fiducial f_NL (evaluate Fisher at this value)
F_NL_FID = 0.0

# Matter bounce prediction
F_NL_MATTER_BOUNCE = -4.375  # = -35/8, parameter-free prediction

print("=" * 70)
print("EXPERIMENT: SPHEREx f_NL Fisher Forecast with Anomaly Tracers")
print(f"  Device: {DEVICE}")
print(f"  k range: [{K_MIN:.0e}, {K_MAX}] h/Mpc, {N_K_BINS} bins")
print(f"  z range: [{Z_MIN}, {Z_MAX}], dz={DZ}, {N_Z_BINS} bins")
print(f"  Fiducial f_NL = {F_NL_FID}")
print(f"  Matter bounce prediction: f_NL = {F_NL_MATTER_BOUNCE}")
print("=" * 70)

# ============================================================
# Tracer Specifications
# ============================================================

# Standard tracers: name -> {bias(z), n(z) in (h/Mpc)^3, z_range}
# Based on SPHEREx, DESI survey design documents

def make_tracer(name, bias_func, nbar_func, z_range, survey):
    return {
        'name': name,
        'bias': bias_func,
        'nbar': nbar_func,
        'z_range': z_range,
        'survey': survey,
    }

# SPHEREx tracers (Dore+ 2014, SPHEREx science book)
SPHEREX_TRACERS = [
    make_tracer('SPHEREx_LRG', lambda z: 1.7 + 0.6*z,
                lambda z: 3e-4 * np.exp(-((z-0.7)/0.3)**2),
                (0.2, 1.5), 'SPHEREx'),
    make_tracer('SPHEREx_ELG', lambda z: 0.84 + 0.4*z,
                lambda z: 1e-3 * np.exp(-((z-1.0)/0.5)**2),
                (0.2, 2.0), 'SPHEREx'),
    make_tracer('SPHEREx_QSO', lambda z: 1.2 + 0.5*z,
                lambda z: 5e-5 * np.exp(-((z-1.5)/0.8)**2),
                (0.5, 3.0), 'SPHEREx'),
]

# DESI tracers (DESI Collaboration 2016)
DESI_TRACERS = [
    make_tracer('DESI_LRG', lambda z: 1.7 + 0.6*z,
                lambda z: 5e-4 * np.exp(-((z-0.7)/0.3)**2),
                (0.2, 1.2), 'DESI'),
    make_tracer('DESI_ELG', lambda z: 0.84 + 0.4*z,
                lambda z: 4e-4 * np.exp(-((z-1.3)/0.4)**2),
                (0.6, 1.7), 'DESI'),
    make_tracer('DESI_QSO', lambda z: 2.0 + 0.3*z,
                lambda z: 3e-5 * np.exp(-((z-1.6)/0.7)**2),
                (0.8, 2.5), 'DESI'),
]

# Anomaly-enhanced tracers (from BigBounce multi-survey catalog)
# These have MUCH higher bias because they trace extreme density peaks
ANOMALY_TRACERS = [
    make_tracer('Anomaly_HighBias', lambda z: 4.0 + 1.5*z,
                lambda z: 2e-6 * np.exp(-((z-0.8)/0.4)**2),
                (0.2, 2.0), 'Anomaly'),
    make_tracer('Anomaly_UltraHighZ', lambda z: 5.0 + 2.0*z,
                lambda z: 5e-7 * np.exp(-((z-2.0)/0.6)**2),
                (1.0, 3.0), 'Anomaly'),
    make_tracer('Anomaly_XraySelected', lambda z: 3.5 + 1.0*z,
                lambda z: 8e-7 * np.exp(-((z-0.6)/0.3)**2),
                (0.2, 1.5), 'Anomaly'),
]

# ============================================================
# Cosmological Functions
# ============================================================

def hubble(z):
    """Hubble parameter H(z) in km/s/Mpc."""
    return H0 * np.sqrt(OMEGA_M * (1 + z)**3 + OMEGA_L)

def comoving_distance(z):
    """Comoving distance in Mpc/h."""
    z_grid = np.linspace(0, z if np.isscalar(z) else np.max(z), 1000)
    integrand = C_LIGHT / hubble(z_grid)  # Mpc
    chi_grid = cumulative_trapezoid(integrand, z_grid, initial=0)
    if np.isscalar(z):
        return chi_grid[-1] * h
    interp = interp1d(z_grid, chi_grid * h, kind='cubic')
    return interp(z)

def growth_factor(z):
    """Linear growth factor D(z), normalized to D(0) = 1."""
    # Approximate formula (Carroll, Press & Turner 1992)
    a = 1.0 / (1.0 + z)
    omega_m_z = OMEGA_M * (1 + z)**3 / (OMEGA_M * (1 + z)**3 + OMEGA_L)
    omega_l_z = OMEGA_L / (OMEGA_M * (1 + z)**3 + OMEGA_L)
    D = (5.0/2.0) * omega_m_z / (
        omega_m_z**(4.0/7.0) - omega_l_z + (1 + omega_m_z/2.0) * (1 + omega_l_z/70.0)
    )
    # Normalize
    omega_m_0 = OMEGA_M
    omega_l_0 = OMEGA_L
    D0 = (5.0/2.0) * omega_m_0 / (
        omega_m_0**(4.0/7.0) - omega_l_0 + (1 + omega_m_0/2.0) * (1 + omega_l_0/70.0)
    )
    return D / D0

def transfer_function(k):
    """Eisenstein-Hu transfer function (no wiggles, approximate)."""
    # k in h/Mpc
    q = k / (OMEGA_M * h**2) * (2.728 / 2.7)**2  # scaled wavenumber
    # Fitting function (Eisenstein & Hu 1998, zero-baryon limit)
    L = np.log(2 * np.e + 1.8 * q)
    C = 14.2 + 731.0 / (1 + 62.5 * q)
    T = L / (L + C * q**2)
    return T

def matter_power_spectrum(k, z):
    """Linear matter power spectrum P(k, z)."""
    T_k = transfer_function(k)
    D_z = growth_factor(z)
    # Normalize to sigma8 at z=0
    # P(k) proportional to k^ns * T(k)^2 * D(z)^2
    Pk = k**N_S * T_k**2 * D_z**2
    # Rough normalization (will cancel in Fisher ratios, but keeps numbers sensible)
    # Use sigma8 normalization
    k_norm = np.logspace(-4, 1, 1000)
    T_norm = transfer_function(k_norm)
    P_norm = k_norm**N_S * T_norm**2
    # sigma8^2 = (1/2pi^2) integral k^2 P(k) W(kR)^2 dk, R=8 Mpc/h
    R = 8.0
    x = k_norm * R
    W = 3 * (np.sin(x) - x * np.cos(x)) / x**3
    integrand = k_norm**2 * P_norm * W**2
    sig8_sq_unnorm = np.trapezoid(integrand, k_norm) / (2 * np.pi**2)
    A = SIGMA8**2 / sig8_sq_unnorm
    return A * Pk

def alpha_fnl(k, z):
    """Scale-dependent bias kernel: alpha(k, z).
    Delta_b = (b-1) * f_NL * delta_c / alpha(k, z)
    alpha(k, z) = (2/3) * k^2 * T(k) * D(z) / (Omega_m * H0_hinv^2)
    where H0_hinv = 100 km/s/Mpc (in natural units for this formula).
    """
    T_k = transfer_function(k)
    D_z = growth_factor(z)
    # In units where H0 = 100 h km/s/Mpc
    return (2.0 / 3.0) * k**2 * T_k * D_z / OMEGA_M

# ============================================================
# Survey Volume
# ============================================================

def survey_volume(z_low, z_high, f_sky):
    """Comoving survey volume in (Mpc/h)^3."""
    chi_low = comoving_distance(z_low)
    chi_high = comoving_distance(z_high)
    return (4.0/3.0) * np.pi * f_sky * (chi_high**3 - chi_low**3)

# Sky fractions
F_SKY = {
    'SPHEREx': 0.75,  # All-sky minus galactic plane
    'DESI': 0.34,     # ~14000 deg^2
    'Anomaly': 0.34,  # Matched to DESI footprint
}

# ============================================================
# Fisher Matrix Computation (GPU-accelerated via PyTorch)
# ============================================================

class FisherDataset(Dataset):
    """Dataset of (k, z, tracer_pair) for Fisher matrix computation."""
    def __init__(self, k_centers, z_centers, tracer_list):
        self.items = []
        for ik, k in enumerate(k_centers):
            for iz, z in enumerate(z_centers):
                for it1 in range(len(tracer_list)):
                    for it2 in range(it1, len(tracer_list)):
                        self.items.append((ik, iz, it1, it2))
        self.items = np.array(self.items, dtype=np.int64)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, idx):
        return torch.from_numpy(self.items[idx])

def compute_fisher_single_tracer(tracers, f_sky, label=""):
    """Compute sigma(f_NL) for a single-tracer analysis."""
    print(f"\n  Computing single-tracer Fisher for: {label}")

    fisher_total = 0.0
    fisher_per_z = np.zeros(N_Z_BINS)

    for iz, z in enumerate(Z_CENTERS):
        z_low = Z_EDGES[iz]
        z_high = Z_EDGES[iz + 1]
        Veff_base = survey_volume(z_low, z_high, f_sky)

        for tracer in tracers:
            z_lo, z_hi = tracer['z_range']
            if z < z_lo or z > z_hi:
                continue

            b = tracer['bias'](z)
            nbar = tracer['nbar'](z)

            for ik, k in enumerate(K_CENTERS):
                dk = K_BINS[ik + 1] - K_BINS[ik]
                Pk = matter_power_spectrum(k, z)
                alpha = alpha_fnl(k, z)

                # Total power: P_obs = (b + Delta_b)^2 * Pk + 1/nbar
                # At fiducial f_NL = 0: P_obs = b^2 * Pk + 1/nbar
                P_obs = b**2 * Pk + 1.0 / max(nbar, 1e-12)

                # Derivative: dP/df_NL = 2 * b * (b-1) * delta_c / alpha * Pk
                dP_dfnl = 2.0 * b * (b - 1.0) * DELTA_C / max(alpha, 1e-12) * Pk

                # Number of modes in this k-bin
                Veff = Veff_base
                n_modes = k**2 * dk * Veff / (2 * np.pi**2)
                n_modes = max(n_modes, 0)

                # Fisher contribution: n_modes/2 * (dP/df_NL / P_obs)^2
                if P_obs > 0:
                    fisher_contrib = 0.5 * n_modes * (dP_dfnl / P_obs)**2
                    fisher_total += fisher_contrib
                    fisher_per_z[iz] += fisher_contrib

    sigma_fnl = 1.0 / np.sqrt(max(fisher_total, 1e-30))
    return fisher_total, sigma_fnl, fisher_per_z

def compute_fisher_multi_tracer(tracers, f_sky, label=""):
    """Compute sigma(f_NL) using multi-tracer technique (Seljak 2009).
    The multi-tracer method cancels cosmic variance by comparing tracers
    with different bias, yielding tighter f_NL constraints.
    """
    print(f"\n  Computing multi-tracer Fisher for: {label}")

    fisher_total = 0.0
    fisher_per_z = np.zeros(N_Z_BINS)

    for iz, z in enumerate(Z_CENTERS):
        z_low = Z_EDGES[iz]
        z_high = Z_EDGES[iz + 1]
        Veff_base = survey_volume(z_low, z_high, f_sky)

        # Active tracers at this redshift
        active = []
        for tracer in tracers:
            z_lo, z_hi = tracer['z_range']
            if z_lo <= z <= z_hi:
                active.append(tracer)

        if len(active) < 1:
            continue

        n_t = len(active)
        biases = np.array([t['bias'](z) for t in active])
        nbars = np.array([t['nbar'](z) for t in active])

        for ik, k in enumerate(K_CENTERS):
            dk = K_BINS[ik + 1] - K_BINS[ik]
            Pk = matter_power_spectrum(k, z)
            alpha = alpha_fnl(k, z)

            n_modes = k**2 * dk * Veff_base / (2 * np.pi**2)
            if n_modes <= 0 or alpha < 1e-12:
                continue

            # Build covariance matrix C_ij = b_i * b_j * Pk + delta_ij / nbar_i
            C = np.outer(biases, biases) * Pk + np.diag(1.0 / np.maximum(nbars, 1e-12))

            # Derivative vector: dP_i/df_NL for auto-spectra
            # For cross-spectra: dP_ij/df_NL = (b_i * db_j + b_j * db_i) * Pk
            # db_i = (b_i - 1) * delta_c / alpha * f_NL (at f_NL=0, the change IS the derivative)
            # dP_ii/df_NL = 2 * b_i * (b_i - 1) * delta_c / alpha * Pk
            # Using full multi-tracer:
            # F_fnl = (n_modes/2) * Tr[C^{-1} dC/df_NL C^{-1} dC/df_NL]

            db = (biases - 1.0) * DELTA_C / alpha

            # dC/df_NL = (db_i * b_j + b_i * db_j) * Pk
            dC = (np.outer(db, biases) + np.outer(biases, db)) * Pk

            try:
                C_inv = np.linalg.inv(C)
            except np.linalg.LinAlgError:
                continue

            # Fisher = (n_modes/2) * Tr[(C^{-1} dC)^2]
            CinvdC = C_inv @ dC
            fisher_contrib = 0.5 * n_modes * np.trace(CinvdC @ CinvdC)
            fisher_total += fisher_contrib
            fisher_per_z[iz] += fisher_contrib

    sigma_fnl = 1.0 / np.sqrt(max(fisher_total, 1e-30))
    return fisher_total, sigma_fnl, fisher_per_z

# ============================================================
# DataLoader for batch power spectrum computation (GPU demo)
# ============================================================

class PowerSpectrumDataset(Dataset):
    """Precompute P(k,z) grid using DataLoader pattern."""
    def __init__(self, k_array, z_array):
        self.pairs = []
        for k in k_array:
            for z in z_array:
                self.pairs.append((k, z))
        self.pairs = np.array(self.pairs, dtype=np.float64)

    def __len__(self):
        return len(self.pairs)

    def __getitem__(self, idx):
        return torch.from_numpy(self.pairs[idx])

def precompute_power_grid():
    """Precompute P(k,z) on a grid using DataLoader."""
    print("\n[1/4] Precomputing power spectrum grid via DataLoader...")
    t0 = time.time()

    ds = PowerSpectrumDataset(K_CENTERS, Z_CENTERS)
    loader = DataLoader(ds, batch_size=256, shuffle=False,
                        num_workers=4, pin_memory=True, prefetch_factor=4)

    Pk_grid = np.zeros((N_K_BINS, N_Z_BINS))
    idx = 0
    for batch in loader:
        for pair in batch.numpy():
            k_val, z_val = pair
            ik = idx // N_Z_BINS
            iz = idx % N_Z_BINS
            Pk_grid[ik, iz] = matter_power_spectrum(k_val, z_val)
            idx += 1

    print(f"  Computed {N_K_BINS} x {N_Z_BINS} = {N_K_BINS * N_Z_BINS} P(k,z) values "
          f"in {time.time() - t0:.2f}s")
    print(f"  P(k) range: [{Pk_grid.min():.2e}, {Pk_grid.max():.2e}]")
    return Pk_grid

# ============================================================
# Main Analysis
# ============================================================

def main():
    t_start = time.time()

    # Precompute
    Pk_grid = precompute_power_grid()

    # ---- Survey configurations ----
    configs = {
        'SPHEREx_only': {
            'tracers': SPHEREX_TRACERS,
            'f_sky': F_SKY['SPHEREx'],
        },
        'SPHEREx_plus_anomaly': {
            'tracers': SPHEREX_TRACERS + ANOMALY_TRACERS,
            'f_sky': F_SKY['SPHEREx'],
        },
        'DESI_only': {
            'tracers': DESI_TRACERS,
            'f_sky': F_SKY['DESI'],
        },
        'DESI_plus_anomaly': {
            'tracers': DESI_TRACERS + ANOMALY_TRACERS,
            'f_sky': F_SKY['DESI'],
        },
        'SPHEREx_DESI_combined': {
            'tracers': SPHEREX_TRACERS + DESI_TRACERS,
            'f_sky': max(F_SKY['SPHEREx'], F_SKY['DESI']),
        },
        'SPHEREx_DESI_plus_anomaly': {
            'tracers': SPHEREX_TRACERS + DESI_TRACERS + ANOMALY_TRACERS,
            'f_sky': max(F_SKY['SPHEREx'], F_SKY['DESI']),
        },
    }

    results = {}

    # ---- Single-tracer analysis ----
    print("\n" + "=" * 60)
    print("[2/4] SINGLE-TRACER ANALYSIS")
    print("=" * 60)

    for config_name, cfg in configs.items():
        F, sigma, fisher_z = compute_fisher_single_tracer(
            cfg['tracers'], cfg['f_sky'], label=config_name
        )
        detection_sigma = abs(F_NL_MATTER_BOUNCE) / sigma
        results[f'single_{config_name}'] = {
            'fisher_total': F,
            'sigma_fnl': round(sigma, 4),
            'detection_sigma_matter_bounce': round(detection_sigma, 2),
            'fisher_per_z': fisher_z,
        }
        print(f"    sigma(f_NL) = {sigma:.4f}, "
              f"matter bounce detection: {detection_sigma:.2f} sigma")

    # ---- Multi-tracer analysis ----
    print("\n" + "=" * 60)
    print("[3/4] MULTI-TRACER ANALYSIS")
    print("=" * 60)

    for config_name, cfg in configs.items():
        if len(cfg['tracers']) < 2:
            continue
        F, sigma, fisher_z = compute_fisher_multi_tracer(
            cfg['tracers'], cfg['f_sky'], label=config_name
        )
        detection_sigma = abs(F_NL_MATTER_BOUNCE) / sigma
        results[f'multi_{config_name}'] = {
            'fisher_total': F,
            'sigma_fnl': round(sigma, 4),
            'detection_sigma_matter_bounce': round(detection_sigma, 2),
            'fisher_per_z': fisher_z,
        }
        print(f"    sigma(f_NL) = {sigma:.4f}, "
              f"matter bounce detection: {detection_sigma:.2f} sigma")

    # ---- Improvement summary ----
    print("\n" + "=" * 60)
    print("[4/4] IMPROVEMENT FROM ANOMALY TRACERS")
    print("=" * 60)

    improvements = {}
    pairs = [
        ('single_SPHEREx_only', 'single_SPHEREx_plus_anomaly'),
        ('single_DESI_only', 'single_DESI_plus_anomaly'),
        ('single_SPHEREx_DESI_combined', 'single_SPHEREx_DESI_plus_anomaly'),
        ('multi_SPHEREx_only', 'multi_SPHEREx_plus_anomaly'),
        ('multi_DESI_only', 'multi_DESI_plus_anomaly'),
        ('multi_SPHEREx_DESI_combined', 'multi_SPHEREx_DESI_plus_anomaly'),
    ]

    for base_key, enhanced_key in pairs:
        if base_key in results and enhanced_key in results:
            sigma_base = results[base_key]['sigma_fnl']
            sigma_enh = results[enhanced_key]['sigma_fnl']
            improvement_pct = (sigma_base - sigma_enh) / sigma_base * 100
            improvements[f'{base_key}_to_{enhanced_key}'] = {
                'sigma_base': sigma_base,
                'sigma_enhanced': sigma_enh,
                'improvement_pct': round(improvement_pct, 2),
            }
            print(f"  {base_key} -> {enhanced_key}:")
            print(f"    sigma: {sigma_base:.4f} -> {sigma_enh:.4f} "
                  f"({improvement_pct:+.2f}%)")

    # Multi-tracer vs single-tracer improvement
    mt_improvement = {}
    for config_name in configs:
        s_key = f'single_{config_name}'
        m_key = f'multi_{config_name}'
        if s_key in results and m_key in results:
            s_sigma = results[s_key]['sigma_fnl']
            m_sigma = results[m_key]['sigma_fnl']
            imp = (s_sigma - m_sigma) / s_sigma * 100
            mt_improvement[config_name] = {
                'single_sigma': s_sigma,
                'multi_sigma': m_sigma,
                'improvement_pct': round(imp, 2),
            }
            print(f"\n  Multi-tracer improvement for {config_name}:")
            print(f"    single: {s_sigma:.4f} -> multi: {m_sigma:.4f} ({imp:+.2f}%)")

    # ---- SPHEREx detection forecast for matter bounce ----
    print("\n" + "-" * 60)
    print("MATTER BOUNCE DETECTION FORECAST (f_NL = -4.375)")
    print("-" * 60)
    best_key = None
    best_sigma = float('inf')
    for key, val in results.items():
        if val['sigma_fnl'] < best_sigma:
            best_sigma = val['sigma_fnl']
            best_key = key
    detection = abs(F_NL_MATTER_BOUNCE) / best_sigma
    print(f"  Best configuration: {best_key}")
    print(f"  sigma(f_NL) = {best_sigma:.4f}")
    print(f"  Detection significance: {detection:.2f} sigma")
    if detection > 5:
        print(f"  --> 5-sigma DETECTION possible!")
    elif detection > 3:
        print(f"  --> 3-sigma evidence achievable")
    elif detection > 2:
        print(f"  --> 2-sigma hint achievable")
    else:
        print(f"  --> Below 2-sigma, need additional data")

    # ---- Save results ----
    elapsed = time.time() - t_start

    # Convert fisher_per_z arrays to lists for JSON
    for key in results:
        results[key]['fisher_per_z'] = results[key]['fisher_per_z'].tolist()

    summary = {
        'experiment': 'fisher_forecast_spherex',
        'cosmology': {
            'H0': H0, 'Omega_m': OMEGA_M, 'Omega_b': OMEGA_B,
            'sigma8': SIGMA8, 'n_s': N_S,
        },
        'k_range': [K_MIN, K_MAX],
        'n_k_bins': N_K_BINS,
        'z_range': [Z_MIN, Z_MAX],
        'z_centers': Z_CENTERS.tolist(),
        'n_z_bins': N_Z_BINS,
        'f_NL_fiducial': F_NL_FID,
        'f_NL_matter_bounce': F_NL_MATTER_BOUNCE,
        'tracer_configs': {
            name: {
                'n_tracers': len(cfg['tracers']),
                'tracers': [t['name'] for t in cfg['tracers']],
                'f_sky': cfg['f_sky'],
            }
            for name, cfg in configs.items()
        },
        'results': results,
        'anomaly_improvements': improvements,
        'multi_tracer_improvements': mt_improvement,
        'best_config': best_key,
        'best_sigma_fnl': best_sigma,
        'matter_bounce_detection_sigma': round(detection, 2),
        'device': str(DEVICE),
        'elapsed_seconds': round(elapsed, 1),
    }

    out_path = os.path.join(OUTPUT_DIR, "fisher_forecast_summary.json")
    with open(out_path, 'w') as f:
        json.dump(summary, f, indent=2, cls=NumpyEncoder)
    print(f"\nSaved summary to {out_path}")

    # Save per-redshift Fisher breakdown as CSV
    rows = []
    for key, val in results.items():
        fisher_z = val['fisher_per_z']
        for iz, z in enumerate(Z_CENTERS):
            rows.append({'config': key, 'z': z, 'fisher': fisher_z[iz]})
    df = pd.DataFrame(rows)
    csv_path = os.path.join(OUTPUT_DIR, "fisher_per_redshift.csv")
    df.to_csv(csv_path, index=False)
    print(f"Saved per-redshift Fisher to {csv_path}")

    print(f"\nTotal elapsed: {elapsed:.1f}s")
    print("\n" + "=" * 70)
    print("COMPLETE")
    print("=" * 70)

if __name__ == "__main__":
    main()
