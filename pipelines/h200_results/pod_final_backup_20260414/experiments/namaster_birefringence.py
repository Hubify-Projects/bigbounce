"""
NaMaster EB Birefringence Analysis — Independent Validation of β=0.27°
======================================================================
Uses the NaMaster pseudo-Cl framework to independently measure the EB
cross-power spectrum expected from ALP cosmic birefringence at β=0.27°.

Method:
  1. Generate synthetic CMB Q/U Stokes maps with known E-mode power
  2. Apply birefringence rotation by β (E→B mixing)
  3. Measure EB power spectrum using NaMaster with proper binning + mask
  4. Compare recovered β against input β
  5. Quantify detection significance for β=0.27° (Paper 1 value)
  6. Also test β=0.342° ± 0.094° (observed ACT+Planck value)

Scientific context:
  - ALP birefringence rotates CMB polarization: Q+iU → (Q+iU)e^{2iβ}
  - This mixes E-modes into B-modes: C_l^EB = sin(2β) cos(2β) C_l^EE
  - For small β: C_l^EB ≈ 2β * C_l^EE
  - Paper 1 prediction: β = 0.27° matches observed 0.342±0.094°
  - NaMaster provides unbiased power spectrum estimation accounting for masks

Key result to validate: does β=0.27° produce a statistically detectable
EB signal above noise at ACT-level sensitivity?
"""

import os
import sys
import json
import time
import numpy as np
import subprocess

OUTPUT_DIR = "/root/results/namaster-birefringence"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------------------------------------------------
# Install NaMaster + healpy if needed
# -------------------------------------------------------------------------
def check_install(pkg, import_name=None):
    import_name = import_name or pkg
    try:
        __import__(import_name)
        return True
    except ImportError:
        print(f"Installing {pkg}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg, "-q"])
        return False

check_install("healpy")
check_install("pymaster", "pymaster")

import healpy as hp
import pymaster as nmt

print("=" * 70)
print("NAMASTER EB BIREFRINGENCE ANALYSIS")
print(f"  NaMaster version: {nmt.__version__}")
print("=" * 70)

t0 = time.time()

# -------------------------------------------------------------------------
# Parameters
# -------------------------------------------------------------------------
NSIDE = 512        # HEALPix resolution (≈7 arcmin pixels, ACT-level)
LMAX = 2 * NSIDE   # Max multipole

# ALP birefringence angle (radians)
BETA_PAPER1 = np.deg2rad(0.27)    # Our Paper 1 prediction
BETA_OBS = np.deg2rad(0.342)      # Minami+Komatsu 2020 / ACT measurement
BETA_OBS_ERR = np.deg2rad(0.094)  # 1σ uncertainty

# CMB parameters (Planck 2018 best-fit)
T_CMB_UK = 2.725e6  # μK
F_SKY = 0.40        # ACT survey coverage (~40% of sky)
N_REAL = 50         # Number of Monte Carlo realizations for noise bias

# Noise level (ACT-like, white noise in μK·arcmin)
NOISE_LEVEL_UKARMIN = 10.0  # μK·arcmin (conservative ACT-like)
PIXEL_AREA_ARCMIN2 = hp.nside2pixarea(NSIDE, degrees=True) * 3600  # arcmin²
NOISE_VAR = (NOISE_LEVEL_UKARMIN / np.sqrt(PIXEL_AREA_ARCMIN2))**2

# -------------------------------------------------------------------------
# [1/6] Generate CMB E-mode power spectrum (ΛCDM)
# -------------------------------------------------------------------------
print("\n[1/6] Generating ΛCDM CMB power spectrum...")

def lcdm_cl_ee(lmax):
    """Approximate ΛCDM EE power spectrum in μK². Semi-analytic fit."""
    ells = np.arange(lmax + 1, dtype=float)
    ells[0] = 1  # avoid div by zero
    # EE spectrum: peaks around ell~100-200
    # Approximate as sum of Gaussians matching Planck 2018
    cl_ee = np.zeros(lmax + 1)
    # TE/EE first peak at ell~140 (reionization bump at ell<10)
    amp1, l1, sig1 = 15.0, 5.0, 3.0      # reionization bump
    amp2, l2, sig2 = 40.0, 140.0, 40.0   # first acoustic peak
    amp3, l3, sig3 = 20.0, 400.0, 60.0   # second peak
    amp4, l4, sig4 = 8.0, 700.0, 80.0    # third peak
    for amp, lc, sig in [(amp1,l1,sig1),(amp2,l2,sig2),(amp3,l3,sig3),(amp4,l4,sig4)]:
        cl_ee += amp * np.exp(-0.5 * ((ells - lc)/sig)**2)
    # Damping tail
    cl_ee *= np.exp(-ells * (ells + 1) / (2 * 2000**2))
    cl_ee[0:2] = 0
    return cl_ee  # μK²

cl_ee = lcdm_cl_ee(LMAX)
print(f"  EE power: ell_peak ~ {np.argmax(cl_ee)}, max = {cl_ee.max():.2f} μK²")

# BB is tiny (lensing only, no primordial) — include as noise floor
cl_bb = 0.05 * cl_ee  # approximate lensing BB

# -------------------------------------------------------------------------
# [2/6] Generate sky mask (Galactic + point source)
# -------------------------------------------------------------------------
print("\n[2/6] Generating sky mask...")

def make_survey_mask(nside, f_sky, galactic_cut_deg=20.0):
    """Create a realistic survey mask combining galactic cut + apodization."""
    npix = hp.nside2npix(nside)
    mask = np.ones(npix, dtype=float)

    # Galactic latitude cut
    _, lat = hp.pix2ang(nside, np.arange(npix), lonlat=True)
    mask[np.abs(lat) < galactic_cut_deg] = 0.0

    # Declination cut (ACT covers δ ∈ [-60°, +20°] roughly)
    ra, dec = hp.pix2ang(nside, np.arange(npix), lonlat=True)
    mask[dec > 25.0] = 0.0
    mask[dec < -65.0] = 0.0

    # Smooth mask (apodize to avoid sharp edges)
    mask = hp.smoothing(mask, fwhm=np.deg2rad(2.0), verbose=False)
    mask = np.clip(mask, 0, 1)

    actual_fsky = mask.sum() / len(mask)
    print(f"  Mask f_sky = {actual_fsky:.3f} (target {f_sky:.2f})")
    return mask

mask = make_survey_mask(NSIDE, F_SKY)
actual_fsky = mask.sum() / hp.nside2npix(NSIDE)

# -------------------------------------------------------------------------
# [3/6] Simulate birefringence and measure EB signal
# -------------------------------------------------------------------------
print("\n[3/6] Simulating birefringence EB signal...")

def apply_birefringence(Q, U, beta):
    """Apply uniform cosmic birefringence rotation by angle beta."""
    cos2b, sin2b = np.cos(2*beta), np.sin(2*beta)
    Q_rot = cos2b * Q - sin2b * U
    U_rot = sin2b * Q + cos2b * U
    return Q_rot, U_rot

def simulate_and_measure(beta, n_real=N_REAL, seed_base=42):
    """
    Monte Carlo: generate n_real realizations of CMB+noise, apply
    birefringence, measure <C_l^EB> with NaMaster.
    Returns: mean EB spectrum, noise bias, signal-to-noise.
    """
    # NaMaster workspace: set up binning and fields
    # Use flat bandpower bins
    n_ell_bins = 20
    ell_min, ell_max = 30, 3 * NSIDE
    ells_bins = np.linspace(ell_min, ell_max, n_ell_bins + 1, dtype=int)
    b = nmt.NmtBin.from_edges(ells_bins[:-1], ells_bins[1:])

    # Workspaces (compute once, reuse)
    # Spin-2 field for polarization (Q, U)
    f_dummy = nmt.NmtField(mask, [np.zeros(hp.nside2npix(NSIDE)),
                                  np.zeros(hp.nside2npix(NSIDE))])
    wsp = nmt.NmtWorkspace()
    wsp.compute_coupling_matrix(f_dummy, f_dummy, b)

    all_cl_eb = []

    for i in range(n_real):
        np.random.seed(seed_base + i)

        # Synthesize Q/U maps from EE+BB spectrum
        # alm for spin-2: need TEB alms (T=0, E from cl_ee, B from cl_bb)
        cl_input = np.array([cl_ee, cl_bb, np.zeros(LMAX+1)])  # EE, BB, EB=0
        # synfast with spin-2
        maps = hp.synfast([np.zeros(LMAX+1), cl_ee, cl_bb, np.zeros(LMAX+1)],
                          NSIDE, lmax=LMAX, new=True, verbose=False)
        # maps[0]=T, maps[1]=Q, maps[2]=U
        Q, U = maps[1], maps[2]

        # Add noise
        Q += np.random.normal(0, np.sqrt(NOISE_VAR), len(Q))
        U += np.random.normal(0, np.sqrt(NOISE_VAR), len(U))

        # Apply birefringence
        Q_rot, U_rot = apply_birefringence(Q, U, beta)

        # NaMaster field
        f_pol = nmt.NmtField(mask, [Q_rot, U_rot])

        # Compute pseudo-Cl and decouple
        cl_coupled = nmt.compute_coupled_cell(f_pol, f_pol)
        cl_decoupled = wsp.decouple_cell(cl_coupled)

        # Extract EB spectrum (index 1 in EE/EB/BE/BB ordering for spin-2×spin-2)
        # cl_decoupled has shape (4, n_bins): EE, EB, BE, BB
        cl_eb = cl_decoupled[1]  # EB
        all_cl_eb.append(cl_eb)

    all_cl_eb = np.array(all_cl_eb)
    mean_cl_eb = all_cl_eb.mean(axis=0)
    std_cl_eb = all_cl_eb.std(axis=0)

    # Theoretical prediction: C_l^EB ≈ sin(2β)cos(2β) * C_l^EE ≈ 2β * C_l^EE for small β
    ell_effs = b.get_effective_ells()
    cl_ee_binned = np.array([cl_ee[int(l)] if int(l) < len(cl_ee) else 0
                             for l in ell_effs])
    cl_eb_theory = np.sin(2*beta) * np.cos(2*beta) * cl_ee_binned

    # SNR per bin
    snr_per_bin = mean_cl_eb / (std_cl_eb + 1e-20)

    # Total SNR via Fisher: sum_l (C_l^EB_theory)^2 / Var
    snr_total = np.sqrt(np.sum((cl_eb_theory / (std_cl_eb + 1e-20))**2))

    return {
        "ell_effs": ell_effs,
        "cl_eb_mean": mean_cl_eb,
        "cl_eb_std": std_cl_eb,
        "cl_eb_theory": cl_eb_theory,
        "snr_per_bin": snr_per_bin,
        "snr_total": float(snr_total),
        "beta_deg": float(np.rad2deg(beta)),
    }

# Run for β=0 (null), β=0.27° (Paper 1), β=0.342° (observed)
print(f"  Running {N_REAL} MC realizations per β value...")

print(f"  β=0.00° (null hypothesis)...")
result_null = simulate_and_measure(0.0, n_real=N_REAL)
print(f"    SNR = {result_null['snr_total']:.2f}")

print(f"  β=0.27° (Paper 1 prediction)...")
result_paper1 = simulate_and_measure(BETA_PAPER1, n_real=N_REAL)
print(f"    SNR = {result_paper1['snr_total']:.2f}")

print(f"  β=0.342° (Minami+Komatsu observed)...")
result_obs = simulate_and_measure(BETA_OBS, n_real=N_REAL)
print(f"    SNR = {result_obs['snr_total']:.2f}")

# -------------------------------------------------------------------------
# [4/6] β recovery test
# -------------------------------------------------------------------------
print("\n[4/6] β recovery test (bias check)...")

def recover_beta(cl_eb_measured, cl_ee_binned, ell_effs):
    """Simple maximum-likelihood β estimator from C_l^EB."""
    # For C_l^EB = sin(2β)cos(2β) C_l^EE
    # Minimize χ² over β using grid search
    beta_grid = np.linspace(-1.0, 1.0, 2001)  # degrees
    chi2 = np.zeros_like(beta_grid)
    for j, bg in enumerate(beta_grid):
        bg_rad = np.deg2rad(bg)
        cl_theory = np.sin(2*bg_rad) * np.cos(2*bg_rad) * cl_ee_binned
        chi2[j] = np.sum((cl_eb_measured - cl_theory)**2)
    beta_ml = beta_grid[np.argmin(chi2)]
    return beta_ml

ell_effs = result_paper1["ell_effs"]
cl_ee_binned = np.array([cl_ee[int(l)] if int(l) < len(cl_ee) else 0 for l in ell_effs])

beta_recovered_paper1 = recover_beta(result_paper1["cl_eb_mean"], cl_ee_binned, ell_effs)
beta_recovered_obs = recover_beta(result_obs["cl_eb_mean"], cl_ee_binned, ell_effs)
beta_recovered_null = recover_beta(result_null["cl_eb_mean"], cl_ee_binned, ell_effs)

print(f"  Input β=0.270°, recovered β={beta_recovered_paper1:.3f}°")
print(f"  Input β=0.342°, recovered β={beta_recovered_obs:.3f}°")
print(f"  Input β=0.000°, recovered β={beta_recovered_null:.3f}°")

bias_paper1 = abs(beta_recovered_paper1 - 0.270)
print(f"  Bias on Paper 1 value: {bias_paper1:.4f}°")

# -------------------------------------------------------------------------
# [5/6] Detection significance for Paper 1 prediction
# -------------------------------------------------------------------------
print("\n[5/6] Detection significance...")

# Compare EB signal from β=0.27° to noise level
# True SNR from NaMaster MC
snr_paper1 = result_paper1["snr_total"]
snr_obs = result_obs["snr_total"]

# Consistency: is our β=0.27° consistent with observed β=0.342±0.094°?
beta_diff_sigma = abs(0.27 - 0.342) / 0.094
print(f"  Paper 1 β=0.27° vs observed β=0.342°±0.094°:")
print(f"    Tension: {beta_diff_sigma:.2f}σ (< 1σ: excellent agreement)")
print(f"  SNR for β=0.27° (ACT-like, f_sky={actual_fsky:.2f}): {snr_paper1:.2f}σ")
print(f"  SNR for β=0.342° (ACT-like, f_sky={actual_fsky:.2f}): {snr_obs:.2f}σ")

# -------------------------------------------------------------------------
# [6/6] Summary
# -------------------------------------------------------------------------
elapsed = time.time() - t0
print(f"\n[6/6] Writing results... (elapsed {elapsed:.1f}s)")

summary = {
    "experiment": "NaMaster EB Birefringence Analysis",
    "nside": NSIDE,
    "lmax": LMAX,
    "f_sky": float(actual_fsky),
    "noise_level_ukarmin": NOISE_LEVEL_UKARMIN,
    "n_mc_realizations": N_REAL,
    "paper1_prediction_deg": 0.27,
    "observed_value_deg": 0.342,
    "observed_error_deg": 0.094,
    "results": {
        "beta_paper1": {
            "input_beta_deg": 0.27,
            "recovered_beta_deg": float(beta_recovered_paper1),
            "bias_deg": float(bias_paper1),
            "snr_namaster": float(snr_paper1),
            "snr_ratio_to_observed": round(snr_paper1 / max(snr_obs, 0.001), 3),
        },
        "beta_observed": {
            "input_beta_deg": 0.342,
            "recovered_beta_deg": float(beta_recovered_obs),
            "snr_namaster": float(snr_obs),
        },
        "beta_null": {
            "input_beta_deg": 0.0,
            "recovered_beta_deg": float(beta_recovered_null),
            "snr_namaster": float(result_null["snr_total"]),
        },
        "consistency_sigma": float(beta_diff_sigma),
    },
    "scientific_conclusion": (
        f"Paper 1 prediction beta=0.27 deg is {beta_diff_sigma:.2f}sigma consistent with "
        f"observed value 0.342+-0.094 deg. NaMaster analysis confirms SNR={snr_paper1:.2f} "
        f"for beta=0.27 at ACT sensitivity (f_sky={actual_fsky:.2f}). "
        f"Beta recovery bias = {bias_paper1:.4f} deg."
    ),
    "runtime_seconds": elapsed,
}

print("\n" + "=" * 70)
print("KEY RESULTS")
print("=" * 70)
print(f"  Paper 1 β=0.27° ← NaMaster SNR = {snr_paper1:.2f}σ")
print(f"  Observed β=0.342° ← NaMaster SNR = {snr_obs:.2f}σ")
print(f"  Tension (0.27 vs 0.342±0.094): {beta_diff_sigma:.2f}σ")
print(f"  β recovery bias: {bias_paper1:.4f}°")
print(f"  Scientific conclusion: {summary['scientific_conclusion'][:100]}...")

try:
    with open(os.path.join(OUTPUT_DIR, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)
except Exception as e:
    print(f"[warn] json save: {e}")

print(json.dumps(summary, indent=2))
print("\nCOMPLETE")
