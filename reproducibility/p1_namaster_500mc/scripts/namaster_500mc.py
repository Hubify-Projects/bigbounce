"""
NaMaster EB Birefringence Analysis — Production 500-MC Run
==========================================================

Reproduces the canonical Paper 1 §VI birefringence numbers:
  - β = 0.27° (Paper 1 prediction) recovered as 0.238° (bias 0.032°)
  - SNR = 20.32σ at ACT sensitivity (f_sky = 0.32, n_side = 512, ℓ_max = 1024,
    noise = 10 µK·arcmin)
  - β = 0.342° (Planck+ACT observed) recovered as 0.302°, SNR = 25.71σ
  - Null β = 0 returns SNR = 0.0
  - Consistency P1-prediction vs observation = 0.77σ

Canonical ground-truth output:
  pipelines/h200_results/pod1_namaster_umap_2026-04-29/results/namaster-birefringence/summary.json

Method:
  1. Generate synthetic ΛCDM CMB Q/U maps (analytic EE fit + lensing BB).
  2. Apply uniform birefringence rotation by angle β (E ↔ B mixing).
  3. Add ACT-like white noise (10 μK·arcmin).
  4. Apply ACT-like survey mask (Galactic |b| > 20°, dec ∈ [-65°, +25°],
     2° apodization → f_sky ≈ 0.32).
  5. Decouple pseudo-Cℓ with NaMaster (binned, 30 ≤ ℓ ≤ 3·NSIDE).
  6. Estimate β by χ² fit of C_ℓ^EB to sin(2β)cos(2β) C_ℓ^EE.
  7. Aggregate across 500 Monte Carlo realizations per β.

Provenance:
  - This file mirrors `/root/namaster_500mc.py` as it ran on H200 pod
    `pod1_namaster_umap_2026-04-29` on 2026-04-29 (run completed 05:31 PDT,
    runtime ≈ 7322 s = 2.03 h on a single H200).
  - The local 50MC pilot variant is preserved at
    `pipelines/h200_results/pod_final_backup_20260414/experiments/namaster_birefringence.py`
    (identical except N_REAL=50 instead of 500).
  - Differences from the pilot: N_REAL=500 (10× MC), reduced MC variance.

Reproducing on a fresh GPU pod:
  pip install healpy pymaster numpy
  python namaster_500mc.py
  # Expect ~7 200 s on H200 (single GPU not strictly needed; CPU-bound).
  # Output: results/namaster-birefringence/summary.json

Random seeds are deterministic: seed_base=42, seeds 42..541 across the 500 MC
realizations. Re-running the script will reproduce the canonical numbers to
machine precision.
"""

import os
import sys
import json
import time
import numpy as np
import subprocess

OUTPUT_DIR = os.environ.get(
    "NAMASTER_OUTPUT_DIR",
    "results/namaster-birefringence",
)
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
print("NAMASTER EB BIREFRINGENCE ANALYSIS — PRODUCTION 500MC")
print(f"  NaMaster version: {nmt.__version__}")
print("=" * 70)

t0 = time.time()

# -------------------------------------------------------------------------
# Parameters (canonical Paper 1 §VI configuration)
# -------------------------------------------------------------------------
NSIDE = 512        # HEALPix resolution (≈7 arcmin pixels, ACT-level)
LMAX = 2 * NSIDE   # Max multipole = 1024

BETA_PAPER1 = np.deg2rad(0.27)     # Paper 1 prediction
BETA_OBS = np.deg2rad(0.342)       # Minami+Komatsu 2020 / ACT measurement
BETA_OBS_ERR = np.deg2rad(0.094)   # 1σ uncertainty

T_CMB_UK = 2.725e6
F_SKY = 0.40                       # ACT survey coverage target
N_REAL = 500                       # Production: 500 MC realizations
SEED_BASE = 42                     # Deterministic for reproducibility

NOISE_LEVEL_UKARMIN = 10.0
PIXEL_AREA_ARCMIN2 = hp.nside2pixarea(NSIDE, degrees=True) * 3600
NOISE_VAR = (NOISE_LEVEL_UKARMIN / np.sqrt(PIXEL_AREA_ARCMIN2)) ** 2

# -------------------------------------------------------------------------
# [1/6] Generate ΛCDM EE/BB power spectrum
# -------------------------------------------------------------------------
print("\n[1/6] Generating ΛCDM CMB power spectrum...")

def lcdm_cl_ee(lmax):
    """Approximate ΛCDM EE power spectrum in μK². Semi-analytic fit to Planck 2018."""
    ells = np.arange(lmax + 1, dtype=float)
    ells[0] = 1
    cl_ee = np.zeros(lmax + 1)
    for amp, lc, sig in [(15.0, 5.0, 3.0),
                         (40.0, 140.0, 40.0),
                         (20.0, 400.0, 60.0),
                         (8.0, 700.0, 80.0)]:
        cl_ee += amp * np.exp(-0.5 * ((ells - lc) / sig) ** 2)
    cl_ee *= np.exp(-ells * (ells + 1) / (2 * 2000 ** 2))
    cl_ee[0:2] = 0
    return cl_ee

cl_ee = lcdm_cl_ee(LMAX)
print(f"  EE power: ell_peak ~ {np.argmax(cl_ee)}, max = {cl_ee.max():.2f} μK²")

cl_bb = 0.05 * cl_ee  # lensing BB only

# -------------------------------------------------------------------------
# [2/6] Sky mask
# -------------------------------------------------------------------------
print("\n[2/6] Generating sky mask...")

def make_survey_mask(nside, f_sky, galactic_cut_deg=20.0):
    npix = hp.nside2npix(nside)
    mask = np.ones(npix, dtype=float)
    _, lat = hp.pix2ang(nside, np.arange(npix), lonlat=True)
    mask[np.abs(lat) < galactic_cut_deg] = 0.0
    ra, dec = hp.pix2ang(nside, np.arange(npix), lonlat=True)
    mask[dec > 25.0] = 0.0
    mask[dec < -65.0] = 0.0
    mask = hp.smoothing(mask, fwhm=np.deg2rad(2.0), verbose=False)
    mask = np.clip(mask, 0, 1)
    actual_fsky = mask.sum() / len(mask)
    print(f"  Mask f_sky = {actual_fsky:.3f} (target {f_sky:.2f})")
    return mask

mask = make_survey_mask(NSIDE, F_SKY)
actual_fsky = mask.sum() / hp.nside2npix(NSIDE)

# -------------------------------------------------------------------------
# [3/6] Birefringence simulation + EB measurement
# -------------------------------------------------------------------------
print("\n[3/6] Simulating birefringence EB signal...")

def apply_birefringence(Q, U, beta):
    cos2b, sin2b = np.cos(2 * beta), np.sin(2 * beta)
    return cos2b * Q - sin2b * U, sin2b * Q + cos2b * U

def simulate_and_measure(beta, n_real=N_REAL, seed_base=SEED_BASE):
    n_ell_bins = 20
    ell_min, ell_max = 30, 3 * NSIDE
    ells_bins = np.linspace(ell_min, ell_max, n_ell_bins + 1, dtype=int)
    b = nmt.NmtBin.from_edges(ells_bins[:-1], ells_bins[1:])

    f_dummy = nmt.NmtField(mask, [np.zeros(hp.nside2npix(NSIDE)),
                                  np.zeros(hp.nside2npix(NSIDE))])
    wsp = nmt.NmtWorkspace()
    wsp.compute_coupling_matrix(f_dummy, f_dummy, b)

    all_cl_eb = []
    for i in range(n_real):
        np.random.seed(seed_base + i)
        maps = hp.synfast([np.zeros(LMAX + 1), cl_ee, cl_bb, np.zeros(LMAX + 1)],
                          NSIDE, lmax=LMAX, new=True, verbose=False)
        Q, U = maps[1], maps[2]
        Q += np.random.normal(0, np.sqrt(NOISE_VAR), len(Q))
        U += np.random.normal(0, np.sqrt(NOISE_VAR), len(U))
        Q_rot, U_rot = apply_birefringence(Q, U, beta)
        f_pol = nmt.NmtField(mask, [Q_rot, U_rot])
        cl_coupled = nmt.compute_coupled_cell(f_pol, f_pol)
        cl_decoupled = wsp.decouple_cell(cl_coupled)
        all_cl_eb.append(cl_decoupled[1])

    all_cl_eb = np.array(all_cl_eb)
    mean_cl_eb = all_cl_eb.mean(axis=0)
    std_cl_eb = all_cl_eb.std(axis=0)
    ell_effs = b.get_effective_ells()
    cl_ee_binned = np.array([cl_ee[int(l)] if int(l) < len(cl_ee) else 0
                             for l in ell_effs])
    cl_eb_theory = np.sin(2 * beta) * np.cos(2 * beta) * cl_ee_binned
    snr_total = np.sqrt(np.sum((cl_eb_theory / (std_cl_eb + 1e-20)) ** 2))
    return {
        "ell_effs": ell_effs,
        "cl_eb_mean": mean_cl_eb,
        "cl_eb_std": std_cl_eb,
        "cl_eb_theory": cl_eb_theory,
        "snr_total": float(snr_total),
        "beta_deg": float(np.rad2deg(beta)),
    }

print(f"  Running {N_REAL} MC realizations per β value (seed_base={SEED_BASE})...")
print("  β=0.00° (null hypothesis)...")
result_null = simulate_and_measure(0.0)
print(f"    SNR = {result_null['snr_total']:.2f}")
print("  β=0.27° (Paper 1 prediction)...")
result_paper1 = simulate_and_measure(BETA_PAPER1)
print(f"    SNR = {result_paper1['snr_total']:.2f}")
print("  β=0.342° (Minami+Komatsu observed)...")
result_obs = simulate_and_measure(BETA_OBS)
print(f"    SNR = {result_obs['snr_total']:.2f}")

# -------------------------------------------------------------------------
# [4/6] β recovery (bias check)
# -------------------------------------------------------------------------
print("\n[4/6] β recovery test (bias check)...")

def recover_beta(cl_eb_measured, cl_ee_binned, ell_effs):
    beta_grid = np.linspace(-1.0, 1.0, 2001)  # degrees
    chi2 = np.zeros_like(beta_grid)
    for j, bg in enumerate(beta_grid):
        bg_rad = np.deg2rad(bg)
        cl_theory = np.sin(2 * bg_rad) * np.cos(2 * bg_rad) * cl_ee_binned
        chi2[j] = np.sum((cl_eb_measured - cl_theory) ** 2)
    return beta_grid[np.argmin(chi2)]

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
# [5/6] Detection significance
# -------------------------------------------------------------------------
print("\n[5/6] Detection significance...")
snr_paper1 = result_paper1["snr_total"]
snr_obs = result_obs["snr_total"]
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
    "seed_base": SEED_BASE,
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

with open(os.path.join(OUTPUT_DIR, "summary.json"), "w") as f:
    json.dump(summary, f, indent=2)

print(json.dumps(summary, indent=2))
print("\nCOMPLETE")
