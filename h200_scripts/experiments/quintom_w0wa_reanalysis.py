#!/usr/bin/env python3
"""
Deep Analysis Experiment: w0-wa Quintom Reanalysis with DESI DR2 Mock
=====================================================================
Run a fresh MCMC on the w0-wa CPL dark energy parameterization using mock
DESI DR2 BAO + Planck CMB + Pantheon+ SN Ia data. Compute:
  - P(quintom-B) = P(w0 > -1 AND w0 + wa < -1)  [phantom crossing]
  - Phantom crossing redshift z_c = -1 - w0/wa
  - Comparison with our existing result P(quintom-B) = 98.6%
  - Forecast tightening with DR2 volume (3x DR1)

Science question: Does the dark energy equation of state cross w = -1 (phantom
divide)? Quintom-B models (w crosses from w>-1 to w<-1) naturally arise in
bounce cosmology but are forbidden in single-field LCDM.

Method:
  - CPL parameterization: w(a) = w0 + wa*(1-a)
  - Mock data: BAO distances (6 z-bins), CMB shift parameter R, SN Ia mu(z)
  - emcee MCMC: 32 walkers x 20000 steps (640K total samples)
  - Flat priors: w0 in [-2, 0], wa in [-3, 2], Omega_m in [0.1, 0.5], H0 in [60, 80]

Output: /workspace/bigbounce/outputs/quintom-w0wa-reanalysis/
"""

import json
import os
import sys
import time
import numpy as np
import pandas as pd
from pathlib import Path
from scipy.integrate import quad
from scipy.optimize import minimize
from datetime import datetime, timezone

import torch
from torch.utils.data import Dataset, DataLoader
import emcee

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

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/workspace/bigbounce/outputs/quintom-w0wa-reanalysis"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# MCMC config
N_WALKERS = 32
N_STEPS = 20000
N_BURN = 5000
N_DIM = 4  # w0, wa, Omega_m, H0

# Fiducial cosmology (quintom-B: crosses phantom divide)
FIDUCIAL = {
    "w0": -0.85,   # w0 > -1 today
    "wa": -0.65,   # w0 + wa = -1.50 < -1 at high z
    "Omega_m": 0.3111,
    "H0": 67.68,
}

# Flat priors
PRIOR_RANGES = {
    "w0": (-2.0, 0.0),
    "wa": (-3.0, 2.0),
    "Omega_m": (0.1, 0.5),
    "H0": (60.0, 80.0),
}

C_KMS = 299792.458

print("=" * 70)
print("DEEP ANALYSIS: w0-wa Quintom Reanalysis with DESI DR2 Mock")
print("=" * 70)
print(f"Output: {OUTPUT_DIR}")
print(f"Fiducial: w0={FIDUCIAL['w0']}, wa={FIDUCIAL['wa']}, "
      f"Omega_m={FIDUCIAL['Omega_m']}, H0={FIDUCIAL['H0']}")
print(f"MCMC: {N_WALKERS} walkers x {N_STEPS} steps = {N_WALKERS * N_STEPS:,} samples")
print()

# ============================================================
# Cosmological distance functions
# ============================================================

def E_z(z, w0, wa, Omega_m):
    """Hubble parameter E(z) = H(z)/H0 for CPL dark energy."""
    a = 1.0 / (1.0 + z)
    Omega_de = 1.0 - Omega_m
    # w(a) = w0 + wa*(1-a), integrated: rho_de ~ a^{-3(1+w0+wa)} * exp(-3*wa*(1-a))
    de_factor = a**(-3 * (1 + w0 + wa)) * np.exp(-3 * wa * (1 - a))
    return np.sqrt(Omega_m * (1 + z)**3 + Omega_de * de_factor)


def comoving_distance(z, w0, wa, Omega_m, H0, n_steps=500):
    """Comoving distance in Mpc."""
    z_arr = np.linspace(0, z, n_steps)
    dz = z / n_steps if n_steps > 1 else 1
    E_arr = np.array([E_z(zi, w0, wa, Omega_m) for zi in z_arr])
    integrand = 1.0 / E_arr
    return (C_KMS / H0) * np.trapz(integrand, z_arr)


def distance_modulus(z, w0, wa, Omega_m, H0):
    """Distance modulus mu = 5*log10(d_L/10pc)."""
    d_C = comoving_distance(z, w0, wa, Omega_m, H0)
    d_L = d_C * (1 + z)  # luminosity distance in Mpc
    return 5 * np.log10(d_L) + 25  # Mpc -> pc conversion


def angular_diameter_distance(z, w0, wa, Omega_m, H0):
    """Angular diameter distance in Mpc."""
    d_C = comoving_distance(z, w0, wa, Omega_m, H0)
    return d_C / (1 + z)


def sound_horizon_rd():
    """Approximate sound horizon at drag epoch in Mpc (fixed for simplicity)."""
    return 147.09  # Planck 2018 value


def dV_over_rd(z, w0, wa, Omega_m, H0):
    """Volume-averaged distance D_V(z)/r_d for BAO."""
    d_C = comoving_distance(z, w0, wa, Omega_m, H0)
    d_A = d_C / (1 + z)
    H_z = H0 * E_z(z, w0, wa, Omega_m)
    D_V = (d_A**2 * C_KMS * z / H_z)**(1.0 / 3.0)
    return D_V / sound_horizon_rd()


def cmb_shift_parameter(w0, wa, Omega_m, H0):
    """CMB shift parameter R = sqrt(Omega_m) * d_C(z*) / (c/H0), z*=1089."""
    z_star = 1089.0
    d_C = comoving_distance(z_star, w0, wa, Omega_m, H0)
    return np.sqrt(Omega_m) * H0 * d_C / C_KMS

# ============================================================
# Mock data generation (DESI DR2 + Planck + Pantheon+)
# ============================================================

class MockDataGenerator:
    """Generate mock cosmological data for MCMC fitting."""

    def __init__(self, fiducial, dr2_factor=3.0, seed=42):
        self.fid = fiducial
        self.rng = np.random.default_rng(seed)
        self.dr2_factor = dr2_factor  # DR2 has ~3x DR1 volume

    def generate_bao_data(self):
        """Mock BAO D_V/r_d at 6 redshift bins (DESI DR2-like)."""
        z_bao = np.array([0.295, 0.510, 0.706, 0.930, 1.317, 2.330])

        # Fiducial D_V/r_d values
        dv_fid = np.array([dV_over_rd(z, self.fid["w0"], self.fid["wa"],
                                       self.fid["Omega_m"], self.fid["H0"]) for z in z_bao])

        # DR1-like errors: ~1-3% per bin
        # DR2: errors shrink by ~1/sqrt(3) due to 3x volume
        dr1_frac_errors = np.array([0.020, 0.015, 0.012, 0.015, 0.020, 0.025])
        dr2_frac_errors = dr1_frac_errors / np.sqrt(self.dr2_factor)

        sigma_bao = dv_fid * dr2_frac_errors
        dv_obs = dv_fid + self.rng.normal(0, sigma_bao)

        return z_bao, dv_obs, sigma_bao

    def generate_cmb_data(self):
        """Mock CMB shift parameter R (Planck-like)."""
        R_fid = cmb_shift_parameter(self.fid["w0"], self.fid["wa"],
                                     self.fid["Omega_m"], self.fid["H0"])
        sigma_R = 0.0065  # Planck precision
        R_obs = R_fid + self.rng.normal(0, sigma_R)
        return R_obs, sigma_R

    def generate_sn_data(self):
        """Mock SN Ia distance moduli (Pantheon+-like, 1700 SNe)."""
        z_sn = np.logspace(np.log10(0.01), np.log10(2.3), 40)  # 40 binned points

        mu_fid = np.array([distance_modulus(z, self.fid["w0"], self.fid["wa"],
                                             self.fid["Omega_m"], self.fid["H0"]) for z in z_sn])

        # Statistical + systematic errors
        sigma_sn = 0.10 + 0.03 * z_sn  # grows slightly with z
        mu_obs = mu_fid + self.rng.normal(0, sigma_sn)

        return z_sn, mu_obs, sigma_sn

# ============================================================
# Likelihood and MCMC
# ============================================================

class W0WaLikelihood:
    """Combined BAO + CMB + SN Ia likelihood for w0-wa."""

    def __init__(self, bao_data, cmb_data, sn_data):
        self.z_bao, self.dv_obs, self.sigma_bao = bao_data
        self.R_obs, self.sigma_R = cmb_data
        self.z_sn, self.mu_obs, self.sigma_sn = sn_data

    def log_prior(self, theta):
        w0, wa, Omega_m, H0 = theta
        for val, (lo, hi) in zip(theta, PRIOR_RANGES.values()):
            if val < lo or val > hi:
                return -np.inf
        return 0.0

    def log_likelihood(self, theta):
        w0, wa, Omega_m, H0 = theta

        try:
            # BAO
            chi2_bao = 0.0
            for i, z in enumerate(self.z_bao):
                dv_pred = dV_over_rd(z, w0, wa, Omega_m, H0)
                chi2_bao += ((dv_pred - self.dv_obs[i]) / self.sigma_bao[i])**2

            # CMB shift parameter
            R_pred = cmb_shift_parameter(w0, wa, Omega_m, H0)
            chi2_cmb = ((R_pred - self.R_obs) / self.sigma_R)**2

            # SN Ia (with nuisance parameter M marginalized analytically)
            mu_pred = np.array([distance_modulus(z, w0, wa, Omega_m, H0) for z in self.z_sn])
            delta_mu = mu_pred - self.mu_obs
            w_sn = 1.0 / self.sigma_sn**2

            # Analytic marginalization over absolute magnitude M
            A = np.sum(w_sn * delta_mu)
            B = np.sum(w_sn)
            C = np.sum(w_sn * delta_mu**2)
            chi2_sn = C - A**2 / B + np.log(B / (2 * np.pi))

            return -0.5 * (chi2_bao + chi2_cmb + chi2_sn)

        except (ValueError, RuntimeWarning, OverflowError):
            return -np.inf

    def log_posterior(self, theta):
        lp = self.log_prior(theta)
        if not np.isfinite(lp):
            return -np.inf
        ll = self.log_likelihood(theta)
        if not np.isfinite(ll):
            return -np.inf
        return lp + ll

# ============================================================
# Chain analysis dataset (for DataLoader-based post-processing)
# ============================================================

class ChainDataset(Dataset):
    """Dataset wrapping MCMC chain for batch analysis."""
    def __init__(self, chain):
        self.chain = torch.from_numpy(chain.astype(np.float32))

    def __len__(self):
        return len(self.chain)

    def __getitem__(self, idx):
        return self.chain[idx]

# ============================================================
# Run MCMC
# ============================================================

print("Generating mock data...")
mock_gen = MockDataGenerator(FIDUCIAL, dr2_factor=3.0)
bao_data = mock_gen.generate_bao_data()
cmb_data = mock_gen.generate_cmb_data()
sn_data = mock_gen.generate_sn_data()

print(f"  BAO: {len(bao_data[0])} z-bins, errors {100*bao_data[2].min():.2f}-{100*bao_data[2].max():.2f}%")
print(f"  CMB: R = {cmb_data[0]:.4f} +/- {cmb_data[1]:.4f}")
print(f"  SN Ia: {len(sn_data[0])} binned points, z = {sn_data[0][0]:.3f} - {sn_data[0][-1]:.3f}")

likelihood = W0WaLikelihood(bao_data, cmb_data, sn_data)

# Initialize walkers near fiducial
print(f"\nInitializing {N_WALKERS} walkers...")
rng = np.random.default_rng(42)
p0 = np.array([FIDUCIAL["w0"], FIDUCIAL["wa"], FIDUCIAL["Omega_m"], FIDUCIAL["H0"]])
scatter = np.array([0.05, 0.1, 0.01, 0.5])
initial_pos = p0 + scatter * rng.normal(size=(N_WALKERS, N_DIM))

# Clip to prior bounds
for i, key in enumerate(PRIOR_RANGES):
    lo, hi = PRIOR_RANGES[key]
    initial_pos[:, i] = np.clip(initial_pos[:, i], lo + 0.001, hi - 0.001)

# Run emcee
print(f"\nRunning emcee MCMC: {N_WALKERS} walkers x {N_STEPS} steps...")
t_mcmc_start = time.time()

sampler = emcee.EnsembleSampler(N_WALKERS, N_DIM, likelihood.log_posterior)

# Run with progress tracking
for i, sample in enumerate(sampler.sample(initial_pos, iterations=N_STEPS)):
    if (i + 1) % 2000 == 0 or i == 0:
        accept_rate = np.mean(sampler.acceptance_fraction)
        print(f"  Step {i+1}/{N_STEPS} | acceptance: {accept_rate:.3f}")

t_mcmc = time.time() - t_mcmc_start
print(f"\nMCMC completed in {t_mcmc:.1f}s ({t_mcmc/60:.1f} min)")
print(f"Mean acceptance fraction: {np.mean(sampler.acceptance_fraction):.3f}")

# ============================================================
# Chain analysis
# ============================================================

print("\nAnalyzing chains...")

# Discard burn-in and flatten
flat_chain = sampler.get_chain(discard=N_BURN, flat=True)
n_samples = len(flat_chain)
print(f"Post-burn-in samples: {n_samples:,}")

# Use DataLoader for batch computation of derived quantities
chain_dataset = ChainDataset(flat_chain)
chain_loader = DataLoader(chain_dataset, batch_size=10000, num_workers=4,
                           pin_memory=True, shuffle=False)

# Compute derived quantities in batches
all_w0 = []
all_wa = []
all_weff = []
all_z_cross = []
all_is_quintom_b = []

for batch in chain_loader:
    w0_b = batch[:, 0].numpy()
    wa_b = batch[:, 1].numpy()

    # Effective w at z=0.5
    a_05 = 1.0 / 1.5
    w_eff = w0_b + wa_b * (1 - a_05)

    # Phantom crossing redshift: w(z_c) = -1 -> w0 + wa*(1 - 1/(1+z_c)) = -1
    # -> z_c such that w0 + wa*z_c/(1+z_c) = -1
    # For w0 > -1 and w0+wa < -1: z_c = -(1+w0)/(w0+wa+1) when wa != 0
    with np.errstate(divide='ignore', invalid='ignore'):
        denom = wa_b
        z_c = np.where(np.abs(denom) > 1e-10,
                       -(1 + w0_b) / denom,
                       np.nan)
        z_c = np.where((z_c > 0) & (z_c < 10), z_c, np.nan)

    # Quintom-B: w0 > -1 AND w0 + wa < -1 (crosses phantom divide from above)
    is_qb = (w0_b > -1) & ((w0_b + wa_b) < -1)

    all_w0.append(w0_b)
    all_wa.append(wa_b)
    all_weff.append(w_eff)
    all_z_cross.append(z_c)
    all_is_quintom_b.append(is_qb)

w0_samples = np.concatenate(all_w0)
wa_samples = np.concatenate(all_wa)
weff_samples = np.concatenate(all_weff)
z_cross_samples = np.concatenate(all_z_cross)
is_quintom_b = np.concatenate(all_is_quintom_b)
om_samples = flat_chain[:, 2]
h0_samples = flat_chain[:, 3]

# ============================================================
# Key results
# ============================================================

print(f"\n{'='*70}")
print("POSTERIOR RESULTS")
print(f"{'='*70}")

def stats(arr, name):
    med = np.median(arr)
    lo = np.percentile(arr, 16)
    hi = np.percentile(arr, 84)
    print(f"  {name:>12}: {med:.4f}  [{lo:.4f}, {hi:.4f}]  (68% CL)")
    return {"median": float(med), "lower_68": float(lo), "upper_68": float(hi),
            "mean": float(np.mean(arr)), "std": float(np.std(arr))}

w0_stats = stats(w0_samples, "w0")
wa_stats = stats(wa_samples, "wa")
om_stats = stats(om_samples, "Omega_m")
h0_stats = stats(h0_samples, "H0")
weff_stats = stats(weff_samples, "w_eff(z=0.5)")

# Quintom-B probability
P_quintom_B = float(np.mean(is_quintom_b))
P_quintom_B_err = float(np.sqrt(P_quintom_B * (1 - P_quintom_B) / n_samples))

# Crossing redshift
valid_zc = z_cross_samples[~np.isnan(z_cross_samples)]
if len(valid_zc) > 0:
    zc_med = float(np.median(valid_zc))
    zc_lo = float(np.percentile(valid_zc, 16))
    zc_hi = float(np.percentile(valid_zc, 84))
else:
    zc_med, zc_lo, zc_hi = np.nan, np.nan, np.nan

# LCDM comparison: distance from w0=-1, wa=0
dist_from_lcdm = np.sqrt((w0_samples + 1)**2 + wa_samples**2)
sigma_from_lcdm = float(np.median(dist_from_lcdm) / np.std(dist_from_lcdm))

print(f"\n  P(quintom-B) = {100*P_quintom_B:.1f}% +/- {100*P_quintom_B_err:.1f}%")
print(f"  (Existing result: 98.6%)")
print(f"  Crossing redshift z_c = {zc_med:.2f}  [{zc_lo:.2f}, {zc_hi:.2f}]")
print(f"  Distance from LCDM: {sigma_from_lcdm:.1f} sigma")

# Compare with DR1 result
improvement = (1 - P_quintom_B_err / 0.014) * 100  # DR1 error ~ 1.4%
print(f"\n  DR2 mock constraint tightening: {improvement:.0f}% vs DR1")

# ============================================================
# Also run DR1-equivalent for direct comparison
# ============================================================

print(f"\n{'='*70}")
print("COMPARISON: DR1 vs DR2 mock constraints")
print(f"{'='*70}")

mock_dr1 = MockDataGenerator(FIDUCIAL, dr2_factor=1.0, seed=99)
bao_dr1 = mock_dr1.generate_bao_data()
lik_dr1 = W0WaLikelihood(bao_dr1, cmb_data, sn_data)

print("Running DR1-equivalent MCMC (shorter: 10000 steps)...")
sampler_dr1 = emcee.EnsembleSampler(N_WALKERS, N_DIM, lik_dr1.log_posterior)

# Re-initialize
initial_pos_dr1 = p0 + scatter * rng.normal(size=(N_WALKERS, N_DIM))
for i, key in enumerate(PRIOR_RANGES):
    lo, hi = PRIOR_RANGES[key]
    initial_pos_dr1[:, i] = np.clip(initial_pos_dr1[:, i], lo + 0.001, hi - 0.001)

sampler_dr1.run_mcmc(initial_pos_dr1, 10000, progress=False)
chain_dr1 = sampler_dr1.get_chain(discard=3000, flat=True)

w0_dr1 = chain_dr1[:, 0]
wa_dr1 = chain_dr1[:, 1]
is_qb_dr1 = (w0_dr1 > -1) & ((w0_dr1 + wa_dr1) < -1)
P_qb_dr1 = float(np.mean(is_qb_dr1))

print(f"  DR1 mock: P(quintom-B) = {100*P_qb_dr1:.1f}%")
print(f"  DR2 mock: P(quintom-B) = {100*P_quintom_B:.1f}%")
print(f"  DR1 mock: sigma(w0) = {np.std(w0_dr1):.4f}")
print(f"  DR2 mock: sigma(w0) = {np.std(w0_samples):.4f}")
print(f"  Constraint improvement: {(1 - np.std(w0_samples)/np.std(w0_dr1))*100:.1f}% tighter")

# ============================================================
# Save results
# ============================================================

elapsed = time.time() - t_mcmc_start

results = {
    "experiment": "quintom_w0wa_reanalysis",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "elapsed_seconds": elapsed,
    "config": {
        "n_walkers": N_WALKERS,
        "n_steps": N_STEPS,
        "n_burn": N_BURN,
        "n_dim": N_DIM,
        "fiducial": FIDUCIAL,
        "prior_ranges": {k: list(v) for k, v in PRIOR_RANGES.items()},
        "dr2_volume_factor": 3.0,
    },
    "mcmc_diagnostics": {
        "n_samples_post_burnin": n_samples,
        "mean_acceptance_fraction": float(np.mean(sampler.acceptance_fraction)),
        "chain_shape": list(flat_chain.shape),
    },
    "posteriors": {
        "w0": w0_stats,
        "wa": wa_stats,
        "Omega_m": om_stats,
        "H0": h0_stats,
        "w_eff_z05": weff_stats,
    },
    "quintom_analysis": {
        "P_quintom_B": P_quintom_B,
        "P_quintom_B_error": P_quintom_B_err,
        "P_quintom_B_percent": f"{100*P_quintom_B:.1f}%",
        "existing_result_percent": "98.6%",
        "crossing_redshift_median": zc_med,
        "crossing_redshift_68CL": [zc_lo, zc_hi],
        "sigma_from_LCDM": sigma_from_lcdm,
    },
    "dr1_vs_dr2_comparison": {
        "P_quintom_B_dr1_mock": float(P_qb_dr1),
        "P_quintom_B_dr2_mock": float(P_quintom_B),
        "sigma_w0_dr1": float(np.std(w0_dr1)),
        "sigma_w0_dr2": float(np.std(w0_samples)),
        "sigma_wa_dr1": float(np.std(wa_dr1)),
        "sigma_wa_dr2": float(np.std(wa_samples)),
        "w0_improvement_pct": float((1 - np.std(w0_samples) / np.std(w0_dr1)) * 100),
        "wa_improvement_pct": float((1 - np.std(wa_samples) / np.std(wa_dr1)) * 100),
    },
    "interpretation": {
        "question": "Does dark energy cross the phantom divide (w = -1)?",
        "quintom_B_definition": "w0 > -1 AND w0 + wa < -1 (crossing from quintessence to phantom)",
        "bounce_connection": "Quintom-B requires violation of the null energy condition, which "
                              "is natural in bounce cosmology but forbidden in single-field LCDM",
        "if_P_high": "Strong evidence for phantom crossing -> supports bounce cosmology dark energy",
        "if_P_low": "LCDM-consistent -> dark energy constraint does not favor bounce",
        "dr2_forecast": "3x volume tightens w0 constraint, sharpening the quintom-B test",
    },
}

out_path = OUTPUT_DIR / "quintom_w0wa_summary.json"
with open(out_path, "w") as f:
    json.dump(results, f, cls=NumpyEncoder, indent=2)
print(f"\nSaved: {out_path}")

# Save chain samples for data explorer
chain_df = pd.DataFrame(flat_chain, columns=["w0", "wa", "Omega_m", "H0"])
chain_df["w_eff_z05"] = weff_samples
chain_df["is_quintom_B"] = is_quintom_b.astype(int)
chain_df["z_crossing"] = z_cross_samples

chain_path = OUTPUT_DIR / "w0wa_chain_samples.csv"
chain_df.to_csv(chain_path, index=False)
print(f"Saved: {chain_path} ({len(chain_df):,} samples)")

print("\n" + "=" * 70)
print("COMPLETE")
print("=" * 70)
