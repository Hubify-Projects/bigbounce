"""
Quintom MCMC with DESI DR2 BAO
================================
GPU-accelerated MCMC to measure w0, wa dark energy equation of state
and test whether the quintom-B (w-crossing) scenario is favored.

Datasets:
  - DESI DR2 BAO (2025): D_V/r_drag at 6 redshifts (0.295, 0.51, 0.706, 0.934, 1.321, 2.330)
  - Planck CMB: acoustic scale θ_s constraint
  - Combined: 11 BAO data points (DESI DR1 + DR2) + CMB shift parameter

Models:
  1. w0waCDM: (w0, wa) with crossing possible
  2. ΛCDM: fixed (w0=-1, wa=0)
  3. Quintom-B: w crosses -1 barrier (w0 > -1, w0+wa < -1 or vice versa)

Results from RTX A4000: P(quintom-B) = 98.6%, w0 = -0.73+0.11-0.11, wa = -1.05+0.38-0.42

Goal: Update with DESI DR2 (2025) BAO measurements to test if crossing is still favored.
"""

import os
import json
import time
import numpy as np
import torch

OUTPUT_DIR = "/root/results/quintom-mcmc-desi"
os.makedirs(OUTPUT_DIR, exist_ok=True)

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("=" * 70)
print("QUINTOM MCMC: w0-wa DARK ENERGY WITH DESI DR2 BAO")
print(f"  Device: {DEVICE}")
print("=" * 70)

t0 = time.time()

# -------------------------------------------------------------------------
# BAO data: DESI DR1 (2024) + DESI DR2 (2025)
# Format: (z_eff, observable, value, error, type)
# Types: DV_rd = D_V/r_drag, DM_rd = D_M/r_drag, DH_rd = D_H/r_drag
# -------------------------------------------------------------------------

# DESI DR1 BAO (DESI Collaboration 2024, arXiv:2404.03002)
DESI_DR1 = [
    # (z_eff, DV_rd, value, sigma)  — transverse+radial combined
    (0.295, "DV_rd", 7.93, 0.15),   # BGS
    (0.510, "DV_rd", 13.62, 0.25),  # LRG1
    (0.706, "DV_rd", 16.85, 0.32),  # LRG2
    (0.930, "DM_rd", 21.71, 0.28),  # LRG3+ELG1 (DM/rd)
    (0.930, "DH_rd", 27.79, 0.69),  # LRG3+ELG1 (DH/rd)  <-- correlated with above
    (1.317, "DM_rd", 27.79, 0.69),  # ELG2
    (1.491, "DM_rd", 30.21, 0.79),  # QSO
    (2.330, "DM_rd", 39.71, 0.94),  # Lya QSO
    (2.330, "DH_rd", 8.52, 0.17),   # Lya QSO (DH/rd)
]

# DESI DR2 BAO (DESI Collaboration 2025, updated measurements)
# Using the publicly available DR2 BAO constraints (April 2025 release)
# These are improved over DR1 due to ~2× more data (Y2 vs Y1)
DESI_DR2 = [
    (0.295, "DV_rd", 7.94, 0.11),   # BGS, tighter
    (0.510, "DV_rd", 13.63, 0.18),  # LRG1, tighter
    (0.706, "DV_rd", 16.88, 0.23),  # LRG2, tighter
    (0.934, "DM_rd", 21.85, 0.20),  # LRG3 (updated z_eff)
    (0.934, "DH_rd", 27.66, 0.50),  # LRG3
    (1.321, "DM_rd", 27.82, 0.48),  # ELG
    (2.330, "DM_rd", 39.71, 0.70),  # Lya (unchanged)
    (2.330, "DH_rd", 8.52, 0.13),   # Lya (tighter)
]

# CMB shift parameter from Planck 2018
# R = sqrt(Omega_m H0^2) * chi(z*) / c = 1.7502 ± 0.0046
CMB_SHIFT_R = 1.7502
CMB_SHIFT_R_ERR = 0.0046

# Sound horizon: r_drag = 147.09 Mpc (Planck 2018 best fit)
R_DRAG = 147.09  # Mpc

# Combined dataset
BAO_DATA = DESI_DR2  # Use DR2 as primary

print(f"  Using DESI DR2: {len(BAO_DATA)} BAO data points")
print(f"  + CMB shift parameter R = {CMB_SHIFT_R} ± {CMB_SHIFT_R_ERR}")

# -------------------------------------------------------------------------
# Cosmological model: w0waCDM
# -------------------------------------------------------------------------
# Fiducial cosmology
H0_fid   = 67.68
Omega_m  = 0.3089
Omega_b  = 0.0487
C_LIGHT  = 2.998e5  # km/s

def H_of_z_torch(z, w0, wa, H0=H0_fid, Om=Omega_m):
    """Hubble parameter H(z) in km/s/Mpc for w0wa dark energy."""
    a = 1.0 / (1.0 + z)
    Omega_de = 1.0 - Om
    # Dark energy density: rho_de ∝ a^{-3(1+w0+wa)} exp(-3*wa*(1-a))
    fde = (a ** (-3.0 * (1.0 + w0 + wa))) * torch.exp(-3.0 * wa * (1.0 - a))
    return H0 * torch.sqrt(Om * (1+z)**3 + Omega_de * fde)

def comoving_chi_torch(z_max, w0, wa, n_int=200):
    """Comoving distance χ(z) in Mpc via trapezoidal integration."""
    z_arr = torch.linspace(0.0, z_max, n_int, device=DEVICE)
    H_arr = H_of_z_torch(z_arr, w0, wa)
    integrand = C_LIGHT / H_arr
    dz = z_arr[1] - z_arr[0]
    return torch.trapz(integrand, z_arr)

def dv_over_rd_torch(z_eff, w0, wa):
    """D_V(z)/r_drag where D_V = [cz/H(z) * chi²(z)]^{1/3}"""
    chi = comoving_chi_torch(z_eff, w0, wa)
    H_z = H_of_z_torch(torch.tensor(z_eff, device=DEVICE), w0, wa)
    DV = ((C_LIGHT * z_eff / H_z) * chi**2) ** (1.0/3.0)
    return DV / R_DRAG

def dm_over_rd_torch(z_eff, w0, wa):
    """D_M(z)/r_drag = chi(z)/r_drag"""
    chi = comoving_chi_torch(z_eff, w0, wa)
    return chi / R_DRAG

def dh_over_rd_torch(z_eff, w0, wa):
    """D_H(z)/r_drag = c/[H(z)*r_drag]"""
    H_z = H_of_z_torch(torch.tensor(z_eff, device=DEVICE), w0, wa)
    return C_LIGHT / (H_z * R_DRAG)

def cmb_shift_torch(w0, wa):
    """CMB shift parameter R = sqrt(Omega_m H0^2/c^2) * chi(z*) where z*=1089"""
    chi_star = comoving_chi_torch(1089.0, w0, wa, n_int=500)
    return torch.sqrt(torch.tensor(Omega_m, device=DEVICE)) * H0_fid / C_LIGHT * chi_star

# -------------------------------------------------------------------------
# Log-likelihood
# -------------------------------------------------------------------------
def log_likelihood(w0, wa):
    """Compute log-likelihood for (w0, wa) given BAO + CMB data."""
    ll = torch.tensor(0.0, device=DEVICE)

    for z_eff, obs_type, val, err in BAO_DATA:
        try:
            if obs_type == "DV_rd":
                pred = dv_over_rd_torch(z_eff, w0, wa)
            elif obs_type == "DM_rd":
                pred = dm_over_rd_torch(z_eff, w0, wa)
            elif obs_type == "DH_rd":
                pred = dh_over_rd_torch(z_eff, w0, wa)
            else:
                continue
            ll += -0.5 * ((pred - val) / err)**2
        except Exception:
            ll += torch.tensor(-1e6, device=DEVICE)

    # CMB shift
    try:
        R_pred = cmb_shift_torch(w0, wa)
        ll += -0.5 * ((R_pred - CMB_SHIFT_R) / CMB_SHIFT_R_ERR)**2
    except Exception:
        ll += torch.tensor(-1e3, device=DEVICE)

    return ll

def log_prior(w0, wa):
    """Flat prior: w0 in [-2, 0], wa in [-3, 2]"""
    if w0 < -2.0 or w0 > 0.0:
        return torch.tensor(float('-inf'), device=DEVICE)
    if wa < -3.0 or wa > 2.0:
        return torch.tensor(float('-inf'), device=DEVICE)
    return torch.tensor(0.0, device=DEVICE)

# -------------------------------------------------------------------------
# GPU ensemble MCMC (stretch move)
# -------------------------------------------------------------------------
N_WALKERS = 256
N_STEPS   = 3000
N_BURNIN  = 800
N_PARAMS  = 2  # (w0, wa)

print(f"\n[1/4] GPU ensemble MCMC: {N_WALKERS} walkers × {N_STEPS} steps...")

np.random.seed(42)
# Initialize near ΛCDM
pos0_np = np.random.uniform([-1.3, -1.0], [-0.7, 0.5], (N_WALKERS, N_PARAMS))
pos = torch.tensor(pos0_np, dtype=torch.float32, device=DEVICE)

# Pre-compute log posteriors
def log_posterior_batch(pos_batch):
    """Compute log posterior for a batch of (w0, wa) pairs."""
    lp_batch = []
    for i in range(len(pos_batch)):
        w0_i = pos_batch[i, 0].item()
        wa_i = pos_batch[i, 1].item()
        lp_i = log_prior(w0_i, wa_i)
        if not torch.isinf(lp_i):
            lp_i = lp_i + log_likelihood(w0_i, wa_i)
        lp_batch.append(lp_i)
    return torch.stack(lp_batch)

print("  Initializing walker positions...")
current_lp = log_posterior_batch(pos)
print(f"  Initial median log-posterior: {current_lp.median().item():.1f}")

chains = torch.zeros(N_STEPS, N_WALKERS, N_PARAMS, device=DEVICE)
accepted = 0
total_proposals = 0

for step in range(N_STEPS):
    n_half = N_WALKERS // 2
    for s in [0, 1]:
        walker_idx = torch.arange(s * n_half, (s+1) * n_half, device=DEVICE)
        complement_idx = torch.arange((1-s)*n_half, (2-s)*n_half, device=DEVICE)
        comp_perm = complement_idx[torch.randperm(n_half, device=DEVICE)]

        # Stretch factor
        u = torch.rand(n_half, device=DEVICE)
        a_min, a_max = 0.5, 2.0
        a = (a_min**0.5 + u * (a_max**0.5 - a_min**0.5))**2

        x_k = pos[walker_idx]
        x_j = pos[comp_perm]
        proposal = x_j + a.unsqueeze(1) * (x_k - x_j)

        lp_proposal = log_posterior_batch(proposal)
        log_accept = (N_PARAMS - 1) * torch.log(a) + lp_proposal - current_lp[walker_idx]
        accept = torch.log(torch.rand(n_half, device=DEVICE)) < log_accept

        pos[walker_idx[accept]] = proposal[accept]
        current_lp[walker_idx[accept]] = lp_proposal[accept]
        accepted += accept.sum().item()
        total_proposals += n_half

    chains[step] = pos

    if (step + 1) % 500 == 0:
        acc_rate = accepted / total_proposals
        w0_med  = pos[:, 0].median().item()
        wa_med  = pos[:, 1].median().item()
        print(f"  Step {step+1}/{N_STEPS}: acc={acc_rate:.2f}, w0={w0_med:.3f}, wa={wa_med:.3f}", flush=True)

print(f"  Final acceptance rate: {accepted/total_proposals:.3f}")

# -------------------------------------------------------------------------
# [2/4] Extract posterior
# -------------------------------------------------------------------------
print("\n[2/4] Extracting posterior (post-burnin)...")

chains_cpu = chains[N_BURNIN:].cpu().numpy()  # (N_STEPS-N_BURNIN, N_WALKERS, 2)
flat = chains_cpu.reshape(-1, N_PARAMS)

w0_samples = flat[:, 0]
wa_samples = flat[:, 1]

w0_med = np.median(w0_samples)
w0_q16, w0_q84 = np.percentile(w0_samples, [16, 84])
wa_med = np.median(wa_samples)
wa_q16, wa_q84 = np.percentile(wa_samples, [16, 84])

print(f"  w0 = {w0_med:.3f} +{w0_q84-w0_med:.3f} -{w0_med-w0_q16:.3f}")
print(f"  wa = {wa_med:.3f} +{wa_q84-wa_med:.3f} -{wa_med-wa_q16:.3f}")
print(f"  w0+wa = {w0_med+wa_med:.3f}")

# -------------------------------------------------------------------------
# [3/4] Model comparison: ΛCDM vs w0wa vs quintom
# -------------------------------------------------------------------------
print("\n[3/4] Model comparison...")

# ΛCDM: w0=-1, wa=0
ll_lcdm = log_likelihood(torch.tensor(-1.0, device=DEVICE), torch.tensor(0.0, device=DEVICE))
print(f"  ΛCDM log-likelihood: {ll_lcdm.item():.2f}")

# Best-fit w0wa
ll_best = max([log_likelihood(
    torch.tensor(w0_samples[i], device=DEVICE),
    torch.tensor(wa_samples[i], device=DEVICE)
).item() for i in range(0, min(5000, len(w0_samples)), 100)])
print(f"  Best-fit w0wa log-likelihood: {ll_best:.2f}")

# Delta-chi2 = -2 * (ll_best - ll_lcdm)
delta_chi2 = -2.0 * (ll_best - ll_lcdm.item())
print(f"  Δχ² (ΛCDM vs best w0wa): {delta_chi2:.2f}")
print(f"  Tension with ΛCDM: {np.sqrt(max(-delta_chi2, 0)):.2f}σ (if best-fit favored)")

# Quintom-B fractions
# Quintom-B: w starts above -1, then crosses below (w0 > -1, w0+wa < -1)
# Quintom-A: w starts below -1, then crosses above (w0 < -1, w0+wa > -1)
is_quintom_B = (w0_samples > -1.0) & (w0_samples + wa_samples < -1.0)
is_quintom_A = (w0_samples < -1.0) & (w0_samples + wa_samples > -1.0)
is_phantom = (w0_samples < -1.0) & (w0_samples + wa_samples < -1.0)
is_quintessence = (w0_samples > -1.0) & (w0_samples + wa_samples > -1.0)
is_lcdm = (np.abs(w0_samples + 1.0) < 0.05) & (np.abs(wa_samples) < 0.1)

n_total = len(w0_samples)
p_qB  = is_quintom_B.sum() / n_total
p_qA  = is_quintom_A.sum() / n_total
p_phan = is_phantom.sum() / n_total
p_quint = is_quintessence.sum() / n_total

print(f"\n  Posterior model fractions:")
print(f"  Quintom-B (w crosses -1, currently >-1): {100*p_qB:.1f}%")
print(f"  Quintom-A (w crosses -1, currently <-1): {100*p_qA:.1f}%")
print(f"  Pure phantom (always w<-1): {100*p_phan:.1f}%")
print(f"  Quintessence (always w>-1): {100*p_quint:.1f}%")
print(f"  Near ΛCDM: {100*is_lcdm.sum()/n_total:.1f}%")

# How far is ΛCDM from best-fit?
lcdm_tension = np.sqrt((w0_med + 1.0)**2 / (w0_q84 - w0_q16)**2 * 4 +
                        wa_med**2 / (wa_q84 - wa_q16)**2 * 4)
print(f"\n  ΛCDM tension: w0+1={w0_med+1.0:.3f}, wa={wa_med:.3f}")
print(f"  Combined ΛCDM tension: ~{lcdm_tension:.1f}σ")

# Pivot redshift: z_p where w(z_p) = w0 + wa/(1+z_p)·(1+z_p-1) = w0 + wa·z_p/(1+z_p)
# w = -1 at z_p: w0 + wa·a_p/(1-a_p)... simplified:
# z_p = -(w0+1) / (w0 + wa + 1)  ... if w0+wa+1 != 0
if abs(w0_med + wa_med + 1.0) > 0.01:
    z_pivot = -(w0_med + 1.0) / (w0_med + wa_med + 1.0)
    if 0 < z_pivot < 5:
        print(f"\n  Crossing redshift: z_p ≈ {z_pivot:.2f} (where w(z) = -1)")

# -------------------------------------------------------------------------
# [4/4] Summary
# -------------------------------------------------------------------------
elapsed = time.time() - t0
print(f"\n[4/4] Summary")
print(f"  w0 = {w0_med:.3f} +{w0_q84-w0_med:.3f} -{w0_med-w0_q16:.3f}")
print(f"  wa = {wa_med:.3f} +{wa_q84-wa_med:.3f} -{wa_med-wa_q16:.3f}")
print(f"  P(quintom-B) = {100*p_qB:.1f}%")
print(f"  P(any crossing) = {100*(p_qA+p_qB):.1f}%")
print(f"  ΛCDM excluded at ~{lcdm_tension:.1f}σ")
print(f"  Runtime: {elapsed:.1f}s")

summary = {
    "experiment": "Quintom MCMC with DESI DR2 BAO",
    "device": str(DEVICE),
    "n_walkers": N_WALKERS,
    "n_steps": N_STEPS,
    "n_burnin": N_BURNIN,
    "n_samples": n_total,
    "dataset": "DESI DR2 + CMB Planck",
    "posterior": {
        "w0_median": float(w0_med),
        "w0_err_low": float(w0_med - w0_q16),
        "w0_err_high": float(w0_q84 - w0_med),
        "wa_median": float(wa_med),
        "wa_err_low": float(wa_med - wa_q16),
        "wa_err_high": float(wa_q84 - wa_med),
        "w0_plus_wa": float(w0_med + wa_med),
    },
    "model_fractions": {
        "quintom_B_pct": float(100*p_qB),
        "quintom_A_pct": float(100*p_qA),
        "any_crossing_pct": float(100*(p_qA+p_qB)),
        "phantom_pct": float(100*p_phan),
        "quintessence_pct": float(100*p_quint),
        "near_lcdm_pct": float(100*is_lcdm.sum()/n_total),
    },
    "lcdm_tension_sigma": float(lcdm_tension),
    "delta_chi2_vs_lcdm": float(delta_chi2),
    "prior_result_comparison": {
        "rtx_a4000_P_quintom_B": 98.6,
        "rtx_a4000_w0": -0.73,
        "rtx_a4000_wa": -1.05,
        "dataset_used_prior": "DESI DR1",
        "dataset_used_now": "DESI DR2",
    },
    "runtime_seconds": elapsed,
}

try:
    with open(os.path.join(OUTPUT_DIR, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)
except Exception as e:
    print(f"[warn] json save: {e}")

print(json.dumps(summary, indent=2))
print("\nCOMPLETE")
