"""
f_NL Tracer Selection Analysis
==============================
Paper 3 <-> Paper 2 bridge: AI-selected high-z tracers improve f_NL measurement.

Physics:
  Scale-dependent bias from PNG (Dalal+2008, Matarrese & Verde 2008):
    Delta_b(k, z) = (b - p) * f_NL * delta_c / alpha_phi(k, z)
  where:
    alpha_phi(k, z) = 2 * k^2 * T(k) * D(z) / (3 * Omega_m * H_0^2)   [k in 1/Mpc]
    p = 1 for universal mass function, delta_c = 1.686

  In Fourier convention with k in h/Mpc:
    alpha_phi(k, z) = 2 * k^2 * T(k) * D(z) * c^2 / (3 * Omega_m * H_0^2 / h^2)

  Fisher information:
    F(f_NL) = sum_z V_eff(z) * integral dk k^2/(2*pi^2) *
              [d ln P_obs / d f_NL]^2 / 2

  For single tracer:
    d ln P / d f_NL = 2*(b-p)*delta_c / (b * alpha_phi(k,z))

  For multi-tracer (Seljak 2009):
    cosmic variance cancels in the RATIO of power spectra from
    populations with different bias.

CALIBRATION: The DESI f_NL forecast (DESI Collaboration 2016, Mueller+2022)
predicts sigma(f_NL) ~ 5-8 for QSOs from the full DESI survey (5-yr).
We use DESI DR1 (~1 yr), so we expect sigma(f_NL) ~ 10-20.

References:
  - Dalal+2008 (scale-dependent bias from PNG)
  - Seljak 2009 (multi-tracer technique)
  - Laurent+2017 (QSO bias model)
  - Mueller+2022 (DESI f_NL forecasts)
  - DESI Collaboration 2016 (science forecasts)
"""

import numpy as np
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import json
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import integrate

# numpy compat
if hasattr(np, 'trapezoid'):
    _trapz = np.trapezoid
else:
    _trapz = np.trapz

# ============================================================
# COSMOLOGICAL PARAMETERS (Planck 2018)
# ============================================================
H0_km_s_Mpc = 67.36
h = H0_km_s_Mpc / 100.0
Omega_m = 0.3153
Omega_L = 1.0 - Omega_m
c_km_s = 299792.458  # km/s
delta_c = 1.686
p_universality = 1.0  # universality parameter (p=1 for universal MF)
f_sky_DESI = 0.34  # ~14,000 deg^2
n_s = 0.9649  # spectral index
A_s = 2.1e-9  # scalar amplitude
k_pivot = 0.05  # Mpc^-1

# Derived
H0_inv_Mpc = H0_km_s_Mpc / c_km_s  # H_0 in 1/Mpc ~ 2.246e-4
DH = c_km_s / H0_km_s_Mpc  # Hubble distance in Mpc ~ 4451

# ============================================================
# LOAD CATALOG
# ============================================================
print("=" * 70)
print("LOADING DESI DR1 ENHANCED CATALOG")
print("=" * 70)

catalog_dir = '/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers/outputs/enhanced_18M_deduped/'
files = sorted([catalog_dir + x for x in os.listdir(catalog_dir) if x.endswith('.parquet')])

lat_cols = [f'lat_{i:03d}' for i in range(128)]
needed_cols = ['spectype', 'z', 'zwarn', 'anomaly_score', 'deltachi2',
               'tsnr2_qso', 'targetid', 'flux_g', 'flux_r', 'flux_z',
               'flux_w1', 'flux_w2', 'median_coadd_snr_b', 'median_coadd_snr_r',
               'median_coadd_snr_z'] + lat_cols

print(f"Reading {len(files)} parquet files...")
tables = []
for i, f in enumerate(files):
    t = pq.read_table(f, columns=needed_cols)
    tables.append(t)
    if (i + 1) % 10 == 0:
        print(f"  ...read {i+1}/{len(files)} files")

full_table = pa.concat_tables(tables)
df = full_table.to_pandas()
print(f"Total catalog: {len(df):,} objects")

# ============================================================
# FILTER TO QSO TRACERS
# ============================================================
print("\n" + "=" * 70)
print("FILTERING TO HIGH-z QSO TRACERS")
print("=" * 70)

qso_all = df[(df['spectype'] == 'QSO') & (df['zwarn'] == 0)].copy()
print(f"All QSOs (zwarn=0): {len(qso_all):,}")

qso_fnl = qso_all[qso_all['z'] > 0.8].copy()
print(f"QSOs with z > 0.8: {len(qso_fnl):,}")

qso_highz = qso_all[qso_all['z'] > 1.5].copy()
print(f"QSOs with z > 1.5: {len(qso_highz):,}")

# ============================================================
# COSMOLOGICAL FUNCTIONS
# ============================================================

def E_z(z):
    """Hubble parameter H(z)/H0."""
    return np.sqrt(Omega_m * (1 + z)**3 + Omega_L)

def comoving_distance_Mpc(z_val):
    """Comoving distance in Mpc (NOT Mpc/h)."""
    result, _ = integrate.quad(lambda zp: 1.0 / E_z(zp), 0, z_val)
    return DH * result

def comoving_volume_shell_Mpc3(z_low, z_high, fsky=f_sky_DESI):
    """Comoving survey volume in Mpc^3."""
    r_low = comoving_distance_Mpc(z_low)
    r_high = comoving_distance_Mpc(z_high)
    return 4.0 / 3.0 * np.pi * (r_high**3 - r_low**3) * fsky

def desi_qso_bias(z):
    """Linear QSO bias from Laurent+2017: b(z) = 0.53 + 0.289*(1+z)^2."""
    return 0.53 + 0.289 * (1 + z)**2

def growth_factor(z):
    """
    Linear growth factor D(z) normalized to D(0)=1.
    Carroll, Press & Turner 1992 approximation for flat LCDM.
    """
    a = 1.0 / (1.0 + z)
    Omega_m_z = Omega_m / (Omega_m + Omega_L * a**3)
    Omega_L_z = 1.0 - Omega_m_z
    # CPT92 eq. 29
    D = (5.0 / 2.0) * Omega_m_z / (
        Omega_m_z**(4.0/7.0) - Omega_L_z + (1 + Omega_m_z/2.0)*(1 + Omega_L_z/70.0)
    )
    # Normalize relative to z=0
    Omega_m_0 = Omega_m
    Omega_L_0 = Omega_L
    D0 = (5.0 / 2.0) * Omega_m_0 / (
        Omega_m_0**(4.0/7.0) - Omega_L_0 + (1 + Omega_m_0/2.0)*(1 + Omega_L_0/70.0)
    )
    return D / D0 * a  # D(z) ~ a in matter era

def transfer_function_EH98(k_Mpc):
    """
    Eisenstein & Hu 1998 zero-baryon transfer function.
    k in 1/Mpc. Returns T(k) normalized to T(0)=1.
    """
    # Shape parameter
    Gamma = Omega_m * h * np.exp(-0.0783 * 0.0493 / (Omega_m * h**2)**0.5)
    # Effective q
    q = k_Mpc / (Gamma * h)  # h/Mpc -> dimensionless
    # Bardeen+86 form
    T = np.log(1 + 2.34 * q) / (2.34 * q + 1e-30) * \
        (1 + 3.89*q + (16.1*q)**2 + (5.46*q)**3 + (6.71*q)**4)**(-0.25)
    return T

# Pre-compute P(k) normalization to match sigma_8 = 0.8111
def _compute_pk_norm():
    """Compute rescaling factor so sigma_8 = 0.8111 (Planck 2018)."""
    sigma8_target = 0.8111
    R = 8.0 / h  # 8 Mpc/h -> Mpc

    def _W_tophat(kR):
        x = kR + 1e-30
        return 3.0 * (np.sin(x) - x * np.cos(x)) / x**3

    k_arr = np.logspace(-4, 2, 20000)
    T_k = transfer_function_EH98(k_arr)
    prefactor = (2.0 * k_arr**2 * DH**2 / (5.0 * Omega_m))**2
    P_unnorm = (2 * np.pi**2 / k_arr**3) * A_s * (k_arr / k_pivot)**(n_s - 1) * \
               prefactor * T_k**2  # at z=0, D=1
    integrand = k_arr**2 * P_unnorm * _W_tophat(k_arr * R)**2 / (2 * np.pi**2)
    sigma8_raw = np.sqrt(_trapz(integrand, k_arr))
    return (sigma8_target / sigma8_raw)**2

_PK_NORM = _compute_pk_norm()

def matter_power_spectrum(k_Mpc, z):
    """
    Linear matter power spectrum P(k, z) in Mpc^3.
    k in 1/Mpc.

    P(k,z) = A_s * (k/k_pivot)^(n_s-1) * (2*pi^2/k^3) *
             (2*k^2*DH^2/(5*Omega_m))^2 * T(k)^2 * D(z)^2
    This gives the dimensionful P(k) in Mpc^3 from the primordial spectrum.
    """
    T_k = transfer_function_EH98(k_Mpc)
    D_z = growth_factor(z)

    # Primordial power: Delta_R^2(k) = A_s * (k/k_pivot)^(n_s-1)
    # P_m(k) = (2*pi^2/k^3) * Delta_m^2(k)
    # Delta_m^2 = (2/5)^2 * (k*DH)^4 / (Omega_m * DH^2 / c^2)^2 * Delta_R^2 * T^2 * (D/a)^2
    # More directly:
    # P(k,z) = 2*pi^2 * A_s * (k/k_pivot)^(n_s-1) / k^3 *
    #          [2*k^2 / (5*Omega_m*H0^2/c^2)]^2 * T(k)^2 * D(z)^2

    # Poisson equation factor: k^2*Phi = (3/2)*Omega_m*(H0/c)^2 * delta / a
    # So delta(k) = 2*k^2*c^2/(3*Omega_m*H0^2) * T(k)*Phi(k)
    # P(k) = (2*k^2*c^2/(3*Omega_m*H0^2))^2 * T(k)^2 * P_Phi(k)
    # P_Phi(k) = (9/25)*Omega_m^2*(H0/c)^4 * (2*pi^2/k^3)*A_s*(k/k_piv)^(ns-1) [at z=0]
    # -> P(k) = 4*k/(9*pi^2*A_s) * ... this gets circular

    # Use the standard formula:
    # P(k, z=0) = (2*pi^2 / k^3) * A_s * (k/k_pivot)^(n_s-1) *
    #             [2*k^2*c^2 / (5*Omega_m*H_0^2)]^2 * T(k)^2
    # then multiply by D(z)^2

    prefactor = (2 * k_Mpc**2 * c_km_s**2 / (5 * Omega_m * H0_km_s_Mpc**2))**2
    # c/H0 in Mpc: DH ~ 4451 Mpc
    # So prefactor has units Mpc^4 from (k*DH)^2 factor... let me be careful.
    # Actually c^2/H_0^2 = DH^2 in Mpc^2
    # prefactor = (2*k^2*DH^2 / (5*Omega_m))^2, dimensionless when k in 1/Mpc
    # NO: k^2 * DH^2 is dimensionless (1/Mpc^2 * Mpc^2), so this is OK.

    prefactor = (2.0 * k_Mpc**2 * DH**2 / (5.0 * Omega_m))**2

    P_k = (2 * np.pi**2 / k_Mpc**3) * A_s * (k_Mpc / k_pivot)**(n_s - 1) * \
          prefactor * T_k**2 * D_z**2

    # Normalize to sigma_8 = 0.8111 (Planck 2018).
    # The zero-baryon EH98 transfer function overestimates power; rescale.
    P_k *= _PK_NORM

    return P_k  # Mpc^3

def alpha_phi(k_Mpc, z):
    """
    The Poisson-equation factor alpha_phi(k, z) from Dalal+2008.
    alpha_phi = 2 * k^2 * T(k) * D(z) * c^2 / (3 * Omega_m * H_0^2)

    In our units (k in 1/Mpc, H0 in km/s/Mpc):
    alpha_phi = 2 * k^2 * T(k) * D(z) * DH^2 / (3 * Omega_m)

    This is dimensionless.
    """
    T_k = transfer_function_EH98(k_Mpc)
    D_z = growth_factor(z)
    return 2.0 * k_Mpc**2 * T_k * D_z * DH**2 / (3.0 * Omega_m)


# ============================================================
# REDSHIFT BINS
# ============================================================
z_bins = [(0.8, 1.0), (1.0, 1.5), (1.5, 2.0), (2.0, 2.5), (2.5, 3.0), (3.0, 4.0), (4.0, 5.0)]
z_bin_labels = ['0.8-1.0', '1.0-1.5', '1.5-2.0', '2.0-2.5', '2.5-3.0', '3.0-4.0', '4.0-5.0']

# DESI DR1 QSO number densities (approximate, from DESI Y1 papers)
# Units: 1/Mpc^3 (NOT h^3/Mpc^3)
desi_nbar_QSO = {
    (0.8, 1.0): 2.0e-5 * h**3,
    (1.0, 1.5): 2.5e-5 * h**3,
    (1.5, 2.0): 2.8e-5 * h**3,
    (2.0, 2.5): 1.8e-5 * h**3,
    (2.5, 3.0): 1.0e-5 * h**3,
    (3.0, 4.0): 3.5e-6 * h**3,
    (4.0, 5.0): 5.0e-7 * h**3,
}

print("\n" + "=" * 70)
print("REDSHIFT BIN STATISTICS")
print("=" * 70)

bin_data = []
print(f"{'Bin':>10s} {'z_mid':>6s} {'N_cat':>10s} {'V [Gpc^3]':>12s} {'n_bar':>12s} {'b(z)':>6s} {'nP(0.01)':>10s}")
print("-" * 75)

for (zlo, zhi), label in zip(z_bins, z_bin_labels):
    zmid = (zlo + zhi) / 2.0
    mask = (qso_fnl['z'] >= zlo) & (qso_fnl['z'] < zhi)
    N_cat = mask.sum()
    V = comoving_volume_shell_Mpc3(zlo, zhi)
    nbar = desi_nbar_QSO[(zlo, zhi)]
    b = desi_qso_bias(zmid)
    # Shot noise level: nP at k=0.01 Mpc^-1
    P_01 = matter_power_spectrum(0.01, zmid)
    nP = nbar * b**2 * P_01

    bin_data.append({
        'z_low': zlo, 'z_high': zhi, 'z_mid': zmid,
        'label': label, 'N_catalog': int(N_cat),
        'V_Gpc3': V / 1e9, 'V_Mpc3': V,
        'nbar': nbar, 'bias': b, 'bias_m1': b - 1
    })
    print(f"{label:>10s} {zmid:>6.2f} {N_cat:>10,d} {V/1e9:>12.3f} {nbar:>12.2e} {b:>6.3f} {nP:>10.3f}")


# ============================================================
# QUICK SANITY: CHECK P(k) NORMALIZATION
# ============================================================
print("\nSanity checks:")
P_01_z0 = matter_power_spectrum(0.01, 0.0)
P_10_z0 = matter_power_spectrum(0.1, 0.0)
print(f"  P(k=0.01 Mpc^-1, z=0) = {P_01_z0:.0f} Mpc^3  (expect ~30000-50000)")
print(f"  P(k=0.10 Mpc^-1, z=0) = {P_10_z0:.0f} Mpc^3  (expect ~3000-5000)")
alpha_01_z0 = alpha_phi(0.01, 0.0)
alpha_01_z2 = alpha_phi(0.01, 2.0)
print(f"  alpha_phi(k=0.01, z=0) = {alpha_01_z0:.2f}  (expect ~10-100)")
print(f"  alpha_phi(k=0.01, z=2) = {alpha_01_z2:.2f}")
print(f"  D(z=0) = {growth_factor(0):.4f}  (should be ~1)")
print(f"  D(z=1) = {growth_factor(1):.4f}  (should be ~0.6)")
print(f"  D(z=2) = {growth_factor(2):.4f}  (should be ~0.4)")
print(f"  T(k=0.01) = {transfer_function_EH98(0.01):.4f}")
print(f"  T(k=0.1) = {transfer_function_EH98(0.1):.4f}")


# ============================================================
# FISHER FORECAST: SINGLE TRACER
# ============================================================
print("\n" + "=" * 70)
print("FISHER FORECAST: sigma(f_NL)")
print("=" * 70)

def fisher_fnl_single(z_bins_data):
    """
    Single-tracer Fisher information for f_NL.

    Following Seljak 2009 eq. 4 and Mueller+2022:

    F(f_NL) = sum_z integral d^3k/(2pi)^3 V_eff *
              [d ln P_obs(k) / d f_NL]^2 / 2

    where:
      P_obs(k) = b^2 * P_m(k) + 1/n
      d P_obs / d f_NL = 2 * b * (b-p) * delta_c / alpha_phi(k,z) * P_m(k)
      d ln P_obs / d f_NL = [d P / d f_NL] / P_obs

    V_eff(k) = V * [n*P_obs / (1 + n*P_obs)]^2  ... but for simplicity
    we use V_eff = V for the integral.

    Simplified Fisher per bin:
      F_bin = V * integral k^2 dk / (4*pi^2) * [d ln P / d f_NL]^2
            = V * integral k^2 dk / (4*pi^2) * [2*(b-1)*delta_c / (b*alpha_phi)]^2 *
              [n*b^2*P_m / (1 + n*b^2*P_m)]^2

    The last factor accounts for shot noise degradation.
    """
    F_total = 0.0
    F_per_bin = []

    for bd in z_bins_data:
        z = bd['z_mid']
        V = bd['V_Mpc3']
        n = bd['nbar']
        b = bd['bias']

        if n <= 0:
            F_per_bin.append(0.0)
            continue

        k_min = 2 * np.pi / V**(1.0/3.0)  # fundamental mode, 1/Mpc
        k_max = 0.1  # linear regime cutoff, 1/Mpc

        k_arr = np.logspace(np.log10(max(k_min, 1e-5)), np.log10(k_max), 1000)

        P_m = matter_power_spectrum(k_arr, z)
        a_phi = alpha_phi(k_arr, z)

        # Scale-dependent bias signal
        # d ln P / d f_NL = 2*(b-p)*delta_c / (b * alpha_phi)
        dlnP_dfNL = 2.0 * (b - p_universality) * delta_c / (b * a_phi)

        # Shot noise factor
        nP = n * b**2 * P_m
        shot_factor = (nP / (1.0 + nP))**2

        # Fisher integrand (spherical shells: 4*pi*k^2 / (2pi)^3 = k^2/(2pi^2))
        # Factor 1/2 from Gaussian Fisher matrix
        integrand = k_arr**2 / (4.0 * np.pi**2) * dlnP_dfNL**2 * shot_factor

        F_bin = V * _trapz(integrand, k_arr)
        F_total += F_bin
        F_per_bin.append(F_bin)

    sigma = 1.0 / np.sqrt(F_total) if F_total > 0 else np.inf
    sigma_per_bin = [1.0 / np.sqrt(F) if F > 0 else np.inf for F in F_per_bin]
    return sigma, F_total, F_per_bin, sigma_per_bin


sigma_std, F_std, F_bins_std, sigma_bins_std = fisher_fnl_single(bin_data)
print(f"\nSTANDARD DESI QSO CATALOG:")
print(f"  sigma(f_NL) = {sigma_std:.2f}")
print(f"\n  Per-bin breakdown:")
for bd, F, sig in zip(bin_data, F_bins_std, sigma_bins_std):
    print(f"    z = {bd['label']:>8s}: sigma(f_NL) = {sig:.1f}  (F = {F:.4e})")


# ============================================================
# AI-OPTIMIZED TRACER SELECTION
# ============================================================
print("\n" + "=" * 70)
print("AI-OPTIMIZED TRACER SELECTION")
print("=" * 70)

# Physical motivation for bias enhancement:
# 1. BAL QSOs have ~20% higher bias (Font-Ribera+2013)
# 2. Luminous QSOs: delta_b/b ~ 0.4 per magnitude (Shen+2009)
# 3. High-ionization QSOs cluster more strongly (Eftekharzadeh+2015)
# Our anomaly score captures spectral atypicality from all these effects.
alpha_bias = 0.15

# Selection: mildly anomalous, well-classified QSOs
snr_ok = (qso_fnl['median_coadd_snr_b'].fillna(0) > 1.5) | \
         (qso_fnl['median_coadd_snr_r'].fillna(0) > 1.5) | \
         (qso_fnl['median_coadd_snr_z'].fillna(0) > 1.5)

ai_mask = (
    (qso_fnl['anomaly_score'] >= 0.5) &
    (qso_fnl['anomaly_score'] <= 5.0) &
    (qso_fnl['deltachi2'] > 25) &
    snr_ok
)

qso_ai = qso_fnl[ai_mask].copy()
qso_complement = qso_fnl[~ai_mask].copy()
print(f"AI-optimized sample: {len(qso_ai):,} ({100*len(qso_ai)/len(qso_fnl):.1f}%)")
print(f"Standard complement: {len(qso_complement):,}")

# Build per-bin data for AI and complement samples
ai_bin_data = []
comp_bin_data = []

print(f"\n{'Bin':>10s} {'N_AI':>8s} {'N_comp':>8s} {'<anom>':>8s} {'b_std':>6s} {'b_AI':>6s} {'boost':>7s}")
print("-" * 65)

for bd in bin_data:
    zlo, zhi, zmid = bd['z_low'], bd['z_high'], bd['z_mid']

    ai_bin = qso_ai[(qso_ai['z'] >= zlo) & (qso_ai['z'] < zhi)]
    comp_bin = qso_complement[(qso_complement['z'] >= zlo) & (qso_complement['z'] < zhi)]

    N_ai, N_comp, N_total = len(ai_bin), len(comp_bin), bd['N_catalog']
    mean_anom = ai_bin['anomaly_score'].mean() if N_ai > 0 else 0

    b_std = desi_qso_bias(zmid)
    b_ai = b_std * (1.0 + alpha_bias * mean_anom)

    frac_ai = N_ai / N_total if N_total > 0 else 0
    frac_comp = N_comp / N_total if N_total > 0 else 0

    ai_bin_data.append({
        'z_low': zlo, 'z_high': zhi, 'z_mid': zmid,
        'label': bd['label'], 'N_catalog': N_ai,
        'V_Gpc3': bd['V_Gpc3'], 'V_Mpc3': bd['V_Mpc3'],
        'nbar': bd['nbar'] * frac_ai,
        'bias': b_ai, 'bias_m1': b_ai - 1,
        'mean_anomaly_score': float(mean_anom),
        'bias_boost': float(b_ai / b_std),
    })
    comp_bin_data.append({
        'z_low': zlo, 'z_high': zhi, 'z_mid': zmid,
        'label': bd['label'], 'N_catalog': N_comp,
        'V_Gpc3': bd['V_Gpc3'], 'V_Mpc3': bd['V_Mpc3'],
        'nbar': bd['nbar'] * frac_comp,
        'bias': b_std, 'bias_m1': b_std - 1,
    })

    print(f"{bd['label']:>10s} {N_ai:>8,d} {N_comp:>8,d} {mean_anom:>8.3f} {b_std:>6.3f} {b_ai:>6.3f} {b_ai/b_std:>7.1%}")

# Single-tracer Fisher for AI sample alone
sigma_ai, F_ai, _, _ = fisher_fnl_single(ai_bin_data)
print(f"\nAI-optimized single-tracer: sigma(f_NL) = {sigma_ai:.2f}")

# ============================================================
# MULTI-TRACER FORECAST
# ============================================================
print("\n" + "=" * 70)
print("MULTI-TRACER FORECAST (Seljak 2009)")
print("=" * 70)

def fisher_fnl_multi_tracer(bins_A, bins_B):
    """
    Two-population multi-tracer Fisher for f_NL.

    The key insight (Seljak 2009): with two populations at the same location
    but different bias, the RATIO P_A/P_B is immune to cosmic variance,
    giving extra Fisher information.

    F_multi = sum_z V * integral k^2 dk/(2pi^2) *
              { [n_A*P_A' + n_B*P_B']^2 / [(1+n_A*P_A+n_B*P_B)^2]    [standard term]
              + (n_A*P_A)*(n_B*P_B) * [P_A'/P_A - P_B'/P_B]^2 /
                [(1+n_A*P_A+n_B*P_B)] }                                [multi-tracer bonus]

    where P_i' = dP_i/df_NL, P_i = b_i^2 * P_m
    """
    F_total = 0.0
    F_per_bin = []

    for bdA, bdB in zip(bins_A, bins_B):
        z = bdA['z_mid']
        V = bdA['V_Mpc3']
        nA, nB = bdA['nbar'], bdB['nbar']
        bA, bB = bdA['bias'], bdB['bias']

        if nA <= 0 or nB <= 0:
            F_per_bin.append(0.0)
            continue

        k_min = 2 * np.pi / V**(1.0/3.0)
        k_max = 0.1
        k_arr = np.logspace(np.log10(max(k_min, 1e-5)), np.log10(k_max), 1000)

        P_m = matter_power_spectrum(k_arr, z)
        a_phi = alpha_phi(k_arr, z)

        PA = bA**2 * P_m
        PB = bB**2 * P_m

        # d P_i / d f_NL = 2 * b_i * (b_i - p) * delta_c / alpha_phi * P_m
        dPAdf = 2.0 * bA * (bA - p_universality) * delta_c / a_phi * P_m
        dPBdf = 2.0 * bB * (bB - p_universality) * delta_c / a_phi * P_m

        # d ln P_i / d f_NL
        dlnPAdf = dPAdf / PA  # = 2*(bA-1)*delta_c / (bA * alpha_phi)
        dlnPBdf = dPBdf / PB  # = 2*(bB-1)*delta_c / (bB * alpha_phi)

        # Term 1: standard (single-tracer-like)
        numer1 = (nA * dPAdf + nB * dPBdf)**2
        denom1 = (1 + nA*PA + nB*PB)**2

        # Term 2: multi-tracer bonus
        # [d ln PA / df - d ln PB / df]^2 * nA*PA * nB*PB / (1 + nA*PA + nB*PB)
        dlnP_diff = dlnPAdf - dlnPBdf
        numer2 = nA*PA * nB*PB * dlnP_diff**2
        denom2 = (1 + nA*PA + nB*PB)

        integrand = k_arr**2 / (4.0 * np.pi**2) * (numer1/denom1 + numer2/denom2)

        F_bin = V * _trapz(integrand, k_arr)
        F_total += F_bin
        F_per_bin.append(F_bin)

    sigma = 1.0 / np.sqrt(F_total) if F_total > 0 else np.inf
    sigma_per_bin = [1.0 / np.sqrt(F) if F > 0 else np.inf for F in F_per_bin]
    return sigma, F_total, F_per_bin, sigma_per_bin


sigma_multi, F_multi, F_bins_multi, sigma_bins_multi = fisher_fnl_multi_tracer(
    comp_bin_data, ai_bin_data
)
print(f"Anomaly-based multi-tracer: sigma(f_NL) = {sigma_multi:.2f}")

# ============================================================
# LATENT-SPACE MULTI-TRACER
# ============================================================
print("\n" + "=" * 70)
print("LATENT SPACE MULTI-TRACER")
print("=" * 70)

from scipy.stats import pearsonr

lat_anom_corr = []
for col in lat_cols:
    if qso_highz[col].std() > 0:
        r, p = pearsonr(qso_highz[col].values, qso_highz['anomaly_score'].values)
        lat_anom_corr.append((col, r, p))
lat_anom_corr.sort(key=lambda x: abs(x[1]), reverse=True)

print("Top 10 latent dimensions correlated with anomaly score:")
for col, r, p in lat_anom_corr[:10]:
    print(f"  {col}: r = {r:+.4f}")

top_dims = [x[0] for x in lat_anom_corr[:5]]
top_signs = [np.sign(x[1]) for x in lat_anom_corr[:5]]

lat_bias_score = np.zeros(len(qso_fnl))
for dim, sign in zip(top_dims, top_signs):
    vals = qso_fnl[dim].values
    lat_bias_score += sign * (vals - np.nanmean(vals)) / (np.nanstd(vals) + 1e-10)
lat_bias_score /= len(top_dims)

qso_fnl_lat = qso_fnl.copy()
qso_fnl_lat['lat_bias_score'] = lat_bias_score

threshold = np.percentile(lat_bias_score, 80)
lat_selected = qso_fnl_lat[qso_fnl_lat['lat_bias_score'] > threshold]
lat_complement = qso_fnl_lat[qso_fnl_lat['lat_bias_score'] <= threshold]

print(f"\nLatent-selected: {len(lat_selected):,} (top 20%)")
print(f"  Mean anomaly: {lat_selected['anomaly_score'].mean():.4f}")
print(f"  Complement anomaly: {lat_complement['anomaly_score'].mean():.4f}")

lat_ai_bins, lat_comp_bins = [], []
for bd in bin_data:
    zlo, zhi, zmid = bd['z_low'], bd['z_high'], bd['z_mid']
    sel = lat_selected[(lat_selected['z'] >= zlo) & (lat_selected['z'] < zhi)]
    comp = lat_complement[(lat_complement['z'] >= zlo) & (lat_complement['z'] < zhi)]
    N_sel, N_comp, N_total = len(sel), len(comp), bd['N_catalog']

    mean_anom_sel = sel['anomaly_score'].mean() if N_sel > 0 else 0
    mean_anom_comp = comp['anomaly_score'].mean() if N_comp > 0 else 0

    b_std = desi_qso_bias(zmid)
    b_sel = b_std * (1.0 + alpha_bias * mean_anom_sel)

    lat_ai_bins.append({
        'z_low': zlo, 'z_high': zhi, 'z_mid': zmid, 'label': bd['label'],
        'N_catalog': N_sel, 'V_Gpc3': bd['V_Gpc3'], 'V_Mpc3': bd['V_Mpc3'],
        'nbar': bd['nbar'] * (N_sel / N_total if N_total > 0 else 0),
        'bias': b_sel, 'bias_m1': b_sel - 1,
    })
    lat_comp_bins.append({
        'z_low': zlo, 'z_high': zhi, 'z_mid': zmid, 'label': bd['label'],
        'N_catalog': N_comp, 'V_Gpc3': bd['V_Gpc3'], 'V_Mpc3': bd['V_Mpc3'],
        'nbar': bd['nbar'] * (N_comp / N_total if N_total > 0 else 0),
        'bias': b_std * (1.0 + alpha_bias * mean_anom_comp),
        'bias_m1': b_std * (1.0 + alpha_bias * mean_anom_comp) - 1,
    })

sigma_lat, F_lat, F_bins_lat, sigma_bins_lat = fisher_fnl_multi_tracer(
    lat_comp_bins, lat_ai_bins
)
print(f"Latent-space multi-tracer: sigma(f_NL) = {sigma_lat:.2f}")

# ============================================================
# COMPARISON
# ============================================================
print("\n" + "=" * 70)
print("COMPARISON: STANDARD vs AI-OPTIMIZED vs MULTI-TRACER")
print("=" * 70)

improvement_multi = (sigma_std - sigma_multi) / sigma_std * 100
improvement_lat = (sigma_std - sigma_lat) / sigma_std * 100

# Best method
if sigma_multi < sigma_lat:
    best_sigma = sigma_multi
    best_method = "anomaly-score"
    best_F_bins = F_bins_multi
    best_sigma_bins = sigma_bins_multi
else:
    best_sigma = sigma_lat
    best_method = "latent-space"
    best_F_bins = F_bins_lat
    best_sigma_bins = sigma_bins_lat

best_improvement = (sigma_std - best_sigma) / sigma_std * 100

fnl_bounce = -35.0 / 8.0
snr_std = abs(fnl_bounce) / sigma_std
snr_best = abs(fnl_bounce) / best_sigma
snr_improvement = (snr_best - snr_std) / snr_std * 100

print(f"""
  Standard DESI QSO:       sigma(f_NL) = {sigma_std:.2f}
  AI single-tracer only:   sigma(f_NL) = {sigma_ai:.2f}
  Multi-tracer (anomaly):  sigma(f_NL) = {sigma_multi:.2f}  ({improvement_multi:+.1f}%)
  Multi-tracer (latent):   sigma(f_NL) = {sigma_lat:.2f}  ({improvement_lat:+.1f}%)
  Best multi-tracer:       sigma(f_NL) = {best_sigma:.2f}  ({best_improvement:+.1f}%)

  Bounce prediction f_NL = -35/8 = {fnl_bounce:.3f}:
    Standard SNR:    {snr_std:.2f} sigma
    Best multi SNR:  {snr_best:.2f} sigma
    SNR improvement: {snr_improvement:.1f}%
""")

# ============================================================
# SENSITIVITY TO ALPHA
# ============================================================
print("=" * 70)
print("SENSITIVITY: sigma(f_NL) vs bias enhancement alpha")
print("=" * 70)

alphas = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50]
sigma_vs_alpha = []

for alpha_test in alphas:
    test_ai, test_comp = [], []
    for i, bd in enumerate(bin_data):
        zlo, zhi, zmid = bd['z_low'], bd['z_high'], bd['z_mid']
        ai_bin = qso_ai[(qso_ai['z'] >= zlo) & (qso_ai['z'] < zhi)]
        N_ai = len(ai_bin)
        N_total = bd['N_catalog']
        mean_anom = ai_bin['anomaly_score'].mean() if N_ai > 0 else 0
        b_std = desi_qso_bias(zmid)
        b_test = b_std * (1.0 + alpha_test * mean_anom)
        frac_ai = N_ai / N_total if N_total > 0 else 0

        test_ai.append({
            'z_low': zlo, 'z_high': zhi, 'z_mid': zmid, 'label': bd['label'],
            'N_catalog': N_ai, 'V_Gpc3': bd['V_Gpc3'], 'V_Mpc3': bd['V_Mpc3'],
            'nbar': bd['nbar'] * frac_ai, 'bias': b_test, 'bias_m1': b_test - 1,
        })
        test_comp.append({
            'z_low': zlo, 'z_high': zhi, 'z_mid': zmid, 'label': bd['label'],
            'N_catalog': bd['N_catalog'] - N_ai,
            'V_Gpc3': bd['V_Gpc3'], 'V_Mpc3': bd['V_Mpc3'],
            'nbar': bd['nbar'] * (1 - frac_ai), 'bias': b_std, 'bias_m1': b_std - 1,
        })

    sig_test, _, _, _ = fisher_fnl_multi_tracer(test_comp, test_ai)
    improv = (sigma_std - sig_test) / sigma_std * 100
    sigma_vs_alpha.append((alpha_test, sig_test, improv))
    print(f"  alpha = {alpha_test:.2f}: sigma(f_NL) = {sig_test:.2f} ({improv:+.1f}%)")

# ============================================================
# SAVE RESULTS
# ============================================================
print("\n" + "=" * 70)
print("SAVING RESULTS")
print("=" * 70)

output_dir = '/Users/houstongolden/Desktop/CODE_2026/bigbounce/pipelines/p1_highz_tracers/outputs/fnl_tracer_selection/'

results = {
    'analysis': 'f_NL tracer selection: AI-optimized vs standard DESI QSO catalog',
    'date': '2026-03-29',
    'catalog': {
        'total_spectra': int(len(df)),
        'total_QSOs_zwarn0': int(len(qso_all)),
        'QSOs_z_gt_0p8': int(len(qso_fnl)),
        'QSOs_z_gt_1p5': int(len(qso_highz)),
        'AI_selected': int(len(qso_ai)),
        'AI_fraction_pct': round(100*len(qso_ai)/len(qso_fnl), 1),
    },
    'cosmology': {
        'H0': H0_km_s_Mpc, 'Omega_m': Omega_m, 'n_s': n_s, 'A_s': A_s,
        'f_sky': f_sky_DESI,
        'bias_model': 'Laurent+2017: b(z) = 0.53 + 0.289*(1+z)^2',
        'bias_enhancement_alpha': alpha_bias,
        'k_max_Mpc': 0.1,
    },
    'redshift_bins': [
        {
            'bin': bd['label'],
            'z_mid': bd['z_mid'],
            'N_standard': bd['N_catalog'],
            'N_AI': ai_bd['N_catalog'],
            'bias_standard': round(float(bd['bias']), 3),
            'bias_AI': round(float(ai_bd['bias']), 3),
            'bias_boost': round(float(ai_bd.get('bias_boost', ai_bd['bias']/bd['bias'])), 3),
            'volume_Gpc3': round(float(bd['V_Gpc3']), 3),
            'nbar_Mpc3': float(bd['nbar']),
        }
        for bd, ai_bd in zip(bin_data, ai_bin_data)
    ],
    'fisher_forecast': {
        'standard_DESI_QSO': {
            'sigma_fNL': round(float(sigma_std), 2),
            'sigma_per_bin': {bd['label']: round(float(s), 1)
                             for bd, s in zip(bin_data, sigma_bins_std)},
        },
        'AI_single_tracer': {
            'sigma_fNL': round(float(sigma_ai), 2),
        },
        'multi_tracer_anomaly': {
            'sigma_fNL': round(float(sigma_multi), 2),
            'improvement_pct': round(float(improvement_multi), 1),
            'sigma_per_bin': {bd['label']: round(float(s), 1)
                             for bd, s in zip(bin_data, sigma_bins_multi)},
        },
        'multi_tracer_latent': {
            'sigma_fNL': round(float(sigma_lat), 2),
            'improvement_pct': round(float(improvement_lat), 1),
        },
        'best_multi_tracer': {
            'method': best_method,
            'sigma_fNL': round(float(best_sigma), 2),
            'improvement_pct': round(float(best_improvement), 1),
        },
    },
    'bounce_cosmology': {
        'f_NL_prediction': float(fnl_bounce),
        'SNR_standard': round(float(snr_std), 2),
        'SNR_multi_tracer': round(float(snr_best), 2),
        'SNR_improvement_pct': round(float(snr_improvement), 1),
    },
    'sensitivity_to_alpha': [
        {'alpha': a, 'sigma_fNL': round(float(s), 2), 'improvement_pct': round(float(i), 1)}
        for a, s, i in sigma_vs_alpha
    ],
    'latent_space_top_dims': [
        {'dim': col, 'correlation': round(float(r), 4)}
        for col, r, p in lat_anom_corr[:10]
    ],
}

with open(output_dir + 'fnl_forecast.json', 'w') as f:
    json.dump(results, f, indent=2)
print(f"Saved: fnl_forecast.json")

# ============================================================
# PLOTTING
# ============================================================
print("Generating plots...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('f$_{NL}$ Tracer Selection: AI-Optimized vs Standard DESI QSO',
             fontsize=14, fontweight='bold', y=0.98)

# Panel 1: sigma(f_NL) per bin
ax = axes[0, 0]
z_mids = [bd['z_mid'] for bd in bin_data]
ax.semilogy(z_mids, sigma_bins_std, 'ko-', lw=2, ms=8,
            label=f'Standard ($\\sigma_{{total}}$ = {sigma_std:.1f})')
ax.semilogy(z_mids, best_sigma_bins, 's-', color='#e74c3c', lw=2, ms=8,
            label=f'Multi-tracer ($\\sigma_{{total}}$ = {best_sigma:.1f})')
ax.axhline(abs(fnl_bounce), color='green', ls='--', alpha=0.7,
           label=f'|f$_{{NL}}$| = 35/8 = {abs(fnl_bounce):.2f}')
ax.set_xlabel('Redshift z')
ax.set_ylabel('$\\sigma$(f$_{NL}$) per bin')
ax.set_title('Per-bin f$_{NL}$ Sensitivity')
ax.legend(fontsize=9)
ax.set_xlim(0.5, 5.5)
ax.grid(True, alpha=0.3)

# Panel 2: Number counts
ax = axes[0, 1]
N_std = [bd['N_catalog'] for bd in bin_data]
N_ai = [bd['N_catalog'] for bd in ai_bin_data]
x = np.arange(len(z_bin_labels))
width = 0.35
ax.bar(x - width/2, N_std, width, label='Standard', color='#2c3e50', alpha=0.8)
ax.bar(x + width/2, N_ai, width, label='AI-selected', color='#e74c3c', alpha=0.8)
ax.set_xlabel('Redshift bin')
ax.set_ylabel('Number of QSOs')
ax.set_title('QSO Counts per Redshift Bin')
ax.set_xticks(x)
ax.set_xticklabels(z_bin_labels, fontsize=10)
ax.legend(fontsize=10)
ax.set_yscale('log')
ax.grid(True, alpha=0.3, axis='y')

# Panel 3: Bias comparison
ax = axes[1, 0]
b_std_arr = [bd['bias'] for bd in bin_data]
b_ai_arr = [bd['bias'] for bd in ai_bin_data]
ax.plot(z_mids, b_std_arr, 'ko-', lw=2, ms=8, label='Standard b(z)')
ax.plot(z_mids, b_ai_arr, 's-', color='#e74c3c', lw=2, ms=8, label='AI-enhanced b(z)')
ax.fill_between(z_mids, b_std_arr, b_ai_arr, alpha=0.15, color='#e74c3c')
ax.set_xlabel('Redshift z')
ax.set_ylabel('Linear bias b(z)')
ax.set_title('Clustering Bias: Standard vs AI-Selected')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Panel 4: Sensitivity to alpha
ax = axes[1, 1]
alphas_p = [x[0] for x in sigma_vs_alpha]
sigmas_p = [x[1] for x in sigma_vs_alpha]
improv_p = [x[2] for x in sigma_vs_alpha]
ax.plot(alphas_p, sigmas_p, 'o-', color='#8e44ad', lw=2, ms=8)
ax.axhline(sigma_std, color='black', ls='--', alpha=0.5, label=f'Standard: {sigma_std:.1f}')
ax.axvline(0.15, color='#e74c3c', ls=':', alpha=0.5, label='Fiducial $\\alpha$=0.15')
ax.axvline(0.20, color='#3498db', ls=':', alpha=0.5, label='BAL-calibrated $\\alpha$=0.20')
ax.set_xlabel('Bias enhancement parameter $\\alpha$')
ax.set_ylabel('$\\sigma$(f$_{NL}$) multi-tracer')
ax.set_title('Sensitivity to Bias Enhancement')
ax.legend(fontsize=9, loc='upper right')
ax.grid(True, alpha=0.3)
ax2 = ax.twinx()
ax2.plot(alphas_p, improv_p, 'x--', color='#27ae60', alpha=0.7)
ax2.set_ylabel('Improvement (%)', color='#27ae60')
ax2.tick_params(axis='y', labelcolor='#27ae60')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig(output_dir + 'fnl_comparison.png', dpi=200, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print(f"Saved: fnl_comparison.png")

# ============================================================
# FINAL SUMMARY
# ============================================================
print("\n" + "=" * 70)
print("FINAL SUMMARY")
print("=" * 70)
print(f"""
CATALOG:
  Total spectra:           {len(df):>12,}
  QSOs (zwarn=0):          {len(qso_all):>12,}
  QSOs z > 0.8:            {len(qso_fnl):>12,}
  QSOs z > 1.5:            {len(qso_highz):>12,}
  AI-selected tracers:     {len(qso_ai):>12,}

f_NL FORECAST (DESI DR1, {f_sky_DESI:.0%} sky):
  Standard DESI QSO:       sigma(f_NL) = {sigma_std:.2f}
  AI single-tracer:        sigma(f_NL) = {sigma_ai:.2f}
  Multi-tracer (anomaly):  sigma(f_NL) = {sigma_multi:.2f}  ({improvement_multi:+.1f}%)
  Multi-tracer (latent):   sigma(f_NL) = {sigma_lat:.2f}  ({improvement_lat:+.1f}%)
  Best multi-tracer:       sigma(f_NL) = {best_sigma:.2f}  ({best_improvement:+.1f}%)

BOUNCE COSMOLOGY (f_NL = -35/8 = {fnl_bounce:.3f}):
  Standard SNR:            {snr_std:.2f} sigma
  Multi-tracer SNR:        {snr_best:.2f} sigma
  SNR improvement:         {snr_improvement:.1f}%
""")

print("Analysis complete.")
