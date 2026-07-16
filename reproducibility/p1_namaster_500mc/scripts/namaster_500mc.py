"""
NaMaster EB Birefringence Analysis — Production 500-MC Run
==========================================================

Recomputes the Paper 1 §VI birefringence validation using the exact
NaMaster bandpower-window operator.  The pre-2026-07-14 result evaluated the
theory at effective-ell bin centres; that approximation is retained only in
the superseded-results directory and is not used here.

Historical output (superseded by the physical-spectrum audit):
  pipelines/h200_results/pod1_namaster_umap_2026-04-29/results/namaster-birefringence/summary.json

Method:
  1. Generate synthetic ΛCDM CMB Q/U maps from pinned raw CAMB lensed
     EE/BB spectra (microkelvin-squared C_ell, never D_ell).
  2. Apply uniform birefringence rotation by angle β (E ↔ B mixing).
  3. Add ACT-like white noise (10 μK·arcmin).
  4. Apply a synthetic HEALPix native-coordinate latitude window
     (|lat| > 20° and -65° < lat < +25° in the same native frame,
     2° apodization → f_sky ≈ 0.32). This is not a Galactic/equatorial
     or survey-footprint mask.
  5. Decouple pseudo-Cℓ with NaMaster (binned, 30 ≤ ℓ ≤ 3·NSIDE).
  6. Estimate β by fitting the fully rotated [EE,EB,BE,BB] theory after
     contraction through the identical NaMaster bandpower-window tensor.
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
realizations. Set NAMASTER_SMOKE=1 for a bounded NSIDE=128, LMAX=256,
N_REAL=1 diagnostic run that writes to a caller-selected output directory.
"""

import os
import sys
import json
import time
import numpy as np
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.environ.get(
    "NAMASTER_OUTPUT_DIR",
    os.path.join(SCRIPT_DIR, "..", "results", "physical_spectrum_v2"),
)
if (
    os.path.exists(os.path.join(OUTPUT_DIR, "summary.json"))
    and os.environ.get("NAMASTER_OVERWRITE") != "1"
):
    raise FileExistsError(
        f"refusing to overwrite existing result at {OUTPUT_DIR}; choose a new "
        "NAMASTER_OUTPUT_DIR (preferred) or set NAMASTER_OVERWRITE=1 explicitly"
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
check_install("camb==1.6.6", "camb")

import healpy as hp
import pymaster as nmt

from windowed_rotation import (
    build_rotation_response,
    recover_beta_deg,
    rotate_eb_spectra,
    validate_window_equivalence,
    windowed_bandpowers,
)
from physical_spectra import load_camb_lensed_spectra
from multipole_contract import bandpower_edges

print("=" * 70)
print("NAMASTER EB BIREFRINGENCE ANALYSIS — PRODUCTION 500MC")
print(f"  NaMaster version: {nmt.__version__}")
print("=" * 70)

t0 = time.time()

# -------------------------------------------------------------------------
# Parameters (canonical Paper 1 §VI configuration)
# -------------------------------------------------------------------------
SMOKE_MODE = os.environ.get("NAMASTER_SMOKE") == "1"
NSIDE = int(os.environ.get("NAMASTER_NSIDE", "128" if SMOKE_MODE else "512"))
LMAX = int(os.environ.get("NAMASTER_LMAX", str(2 * NSIDE)))

BETA_PAPER1 = np.deg2rad(0.27)     # Paper 1 prediction
BETA_OBS = np.deg2rad(0.342)       # Minami+Komatsu 2020 / ACT measurement
BETA_OBS_ERR = np.deg2rad(0.094)   # 1σ uncertainty

T_CMB_UK = 2.725e6
F_SKY = 0.40                       # ACT survey coverage target
N_REAL = int(os.environ.get("NAMASTER_NREAL", "1" if SMOKE_MODE else "500"))
SEED_BASE = 42                     # Deterministic for reproducibility

NOISE_LEVEL_UKARMIN = 10.0
PIXEL_AREA_ARCMIN2 = hp.nside2pixarea(NSIDE, degrees=True) * 3600
NOISE_VAR = (NOISE_LEVEL_UKARMIN / np.sqrt(PIXEL_AREA_ARCMIN2)) ** 2

# -------------------------------------------------------------------------
# [1/6] Generate ΛCDM EE/BB power spectrum
# -------------------------------------------------------------------------
print("\n[1/6] Generating ΛCDM CMB power spectrum...")

cl_ee, cl_bb, spectrum_metadata = load_camb_lensed_spectra(LMAX)
print(
    "  Raw CAMB lensed spectra: "
    f"C_140^EE={cl_ee[140]:.6e} μK², "
    f"D_140^EE={spectrum_metadata['validation']['d_ell_ee_at_ell_check_uK2']:.6f} μK²"
)
print(f"  EE SHA-256: {spectrum_metadata['sha256']['cl_ee_raw_uK2']}")
print(f"  BB SHA-256: {spectrum_metadata['sha256']['cl_bb_raw_uK2']}")

# -------------------------------------------------------------------------
# [2/6] Sky mask
# -------------------------------------------------------------------------
print("\n[2/6] Generating sky mask...")

def make_native_latitude_window(nside, f_sky, latitude_cut_deg=20.0):
    """Synthetic window in one HEALPix native coordinate frame.

    ``hp.pix2ang(..., lonlat=True)`` supplies one native longitude/latitude
    pair. No coordinate rotation is applied, so the two latitude conditions
    below must not be interpreted as Galactic latitude plus equatorial
    declination or as an ACT/other survey footprint.
    """
    npix = hp.nside2npix(nside)
    mask = np.ones(npix, dtype=float)
    _, lat = hp.pix2ang(nside, np.arange(npix), lonlat=True)
    mask[np.abs(lat) < latitude_cut_deg] = 0.0
    mask[lat > 25.0] = 0.0
    mask[lat < -65.0] = 0.0
    mask = hp.smoothing(mask, fwhm=np.deg2rad(2.0), verbose=False)
    mask = np.clip(mask, 0, 1)
    actual_fsky = mask.sum() / len(mask)
    print(f"  Mask f_sky = {actual_fsky:.3f} (target {f_sky:.2f})")
    return mask

mask = make_native_latitude_window(NSIDE, F_SKY)
actual_fsky = mask.sum() / hp.nside2npix(NSIDE)

n_ell_bins = int(os.environ.get("NAMASTER_NBINS", "6" if SMOKE_MODE else "20"))
ells_bins = bandpower_edges(
    nside=NSIDE, lmax=LMAX, n_bins=n_ell_bins, ell_min=30
)
bandpower_bin = nmt.NmtBin.from_edges(ells_bins[:-1], ells_bins[1:])
f_dummy = nmt.NmtField(
    mask,
    [np.zeros(hp.nside2npix(NSIDE)), np.zeros(hp.nside2npix(NSIDE))],
    lmax=LMAX,
)
workspace = nmt.NmtWorkspace()
workspace.compute_coupling_matrix(f_dummy, f_dummy, bandpower_bin)
rotation_response = build_rotation_response(workspace, cl_ee, cl_bb)
window_equivalence_max_abs = validate_window_equivalence(
    workspace, rotation_response, BETA_PAPER1
)
if not np.isfinite(window_equivalence_max_abs) or window_equivalence_max_abs > 1e-10:
    raise RuntimeError(
        "NaMaster window contraction failed equivalence check: "
        f"max_abs={window_equivalence_max_abs:.6e}"
    )
print(
    "  Exact bandpower-window response verified against "
    f"decouple(couple(theory)); max|delta|={window_equivalence_max_abs:.3e}"
)

# -------------------------------------------------------------------------
# [3/6] Birefringence simulation + EB measurement
# -------------------------------------------------------------------------
print("\n[3/6] Simulating birefringence EB signal...")

def apply_birefringence(Q, U, beta):
    cos2b, sin2b = np.cos(2 * beta), np.sin(2 * beta)
    return cos2b * Q - sin2b * U, sin2b * Q + cos2b * U

def simulate_and_measure_all(betas, n_real=N_REAL, seed_base=SEED_BASE):
    """Measure all betas from one identical-seed noisy map per realization.

    Uniform Q/U rotation commutes with the scalar mask.  We therefore rotate
    the four coupled spectra algebraically, which is numerically identical to
    constructing a new rotated field but requires only one spherical harmonic
    transform per realization.  ``windowed_rotation.rotate_eb_spectra`` is
    regression-tested against the direct field route.
    """
    betas = [float(beta) for beta in betas]
    all_cl_eb = {beta: [] for beta in betas}
    for i in range(n_real):
        np.random.seed(seed_base + i)
        maps = hp.synfast([np.zeros(LMAX + 1), cl_ee, cl_bb, np.zeros(LMAX + 1)],
                          NSIDE, lmax=LMAX, new=True, verbose=False)
        Q, U = maps[1], maps[2]
        Q += np.random.normal(0, np.sqrt(NOISE_VAR), len(Q))
        U += np.random.normal(0, np.sqrt(NOISE_VAR), len(U))
        f_pol = nmt.NmtField(mask, [Q, U], lmax=LMAX)
        cl_coupled = nmt.compute_coupled_cell(f_pol, f_pol)
        for beta in betas:
            rotated_coupled = rotate_eb_spectra(cl_coupled, beta)
            all_cl_eb[beta].append(workspace.decouple_cell(rotated_coupled)[1])

    ell_effs = bandpower_bin.get_effective_ells()
    cl_eb_null_theory = windowed_bandpowers(rotation_response, 0.0)[1]
    results = {}
    for beta in betas:
        ensemble = np.asarray(all_cl_eb[beta])
        mean_cl_eb = ensemble.mean(axis=0)
        std_cl_eb = ensemble.std(axis=0)
        cl_eb_theory = windowed_bandpowers(rotation_response, beta)[1]
        snr_total = np.sqrt(
            np.sum(((cl_eb_theory - cl_eb_null_theory) /
                    (std_cl_eb + 1e-20)) ** 2)
        )
        results[beta] = {
            "ell_effs": ell_effs,
            "cl_eb_mean": mean_cl_eb,
            "cl_eb_std": std_cl_eb,
            "cl_eb_theory": cl_eb_theory,
            "all_cl_eb": ensemble,
            "snr_total": float(snr_total),
            "beta_deg": float(np.rad2deg(beta)),
        }
    return results

print(f"  Running {N_REAL} MC realizations per β value (seed_base={SEED_BASE})...")
print("  Joint identical-seed ensemble: β=0.00°, 0.27°, 0.342°...")
joint_results = simulate_and_measure_all([0.0, BETA_PAPER1, BETA_OBS])
result_null = joint_results[0.0]
print(f"    SNR = {result_null['snr_total']:.2f}")
result_paper1 = joint_results[BETA_PAPER1]
print(f"    SNR = {result_paper1['snr_total']:.2f}")
result_obs = joint_results[BETA_OBS]
print(f"    SNR = {result_obs['snr_total']:.2f}")

# -------------------------------------------------------------------------
# [4/6] β recovery (bias check)
# -------------------------------------------------------------------------
print("\n[4/6] β recovery test (bias check)...")

beta_recovered_paper1 = float(
    recover_beta_deg(result_paper1["cl_eb_mean"], rotation_response)
)
beta_recovered_obs = float(
    recover_beta_deg(result_obs["cl_eb_mean"], rotation_response)
)
beta_recovered_null = float(
    recover_beta_deg(result_null["cl_eb_mean"], rotation_response)
)
beta_per_real_paper1 = recover_beta_deg(
    result_paper1["all_cl_eb"], rotation_response
)

print(f"  Input β=0.270°, recovered β={beta_recovered_paper1:.3f}°")
print(f"  Input β=0.342°, recovered β={beta_recovered_obs:.3f}°")
print(f"  Input β=0.000°, recovered β={beta_recovered_null:.3f}°")

bias_paper1_signed = beta_recovered_paper1 - 0.270
bias_paper1 = abs(bias_paper1_signed)
beta_scatter_paper1 = float(np.std(beta_per_real_paper1, ddof=1)) if N_REAL > 1 else None
beta_mean_se_paper1 = (
    beta_scatter_paper1 / np.sqrt(N_REAL) if beta_scatter_paper1 is not None else None
)
print(f"  Bias on Paper 1 value: {bias_paper1_signed:+.4f}°")
if beta_scatter_paper1 is not None:
    print(
        f"  Per-realization beta scatter: {beta_scatter_paper1:.4f}°; "
        f"MC mean SE: {beta_mean_se_paper1:.4f}°"
    )

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
    "run_mode": "bounded_smoke" if SMOKE_MODE else "production",
    "physical_spectra": spectrum_metadata,
    "theory_operator": "NmtWorkspace.get_bandpower_windows exact tensor contraction",
    "window_shape": list(rotation_response["window_shape"]),
    "window_equivalence_max_abs": window_equivalence_max_abs,
    "software": {
        "numpy": np.__version__,
        "healpy": hp.__version__,
        "pymaster": nmt.__version__,
    },
    "paper1_prediction_deg": 0.27,
    "observed_value_deg": 0.342,
    "observed_error_deg": 0.094,
    "results": {
        "beta_paper1": {
            "input_beta_deg": 0.27,
            "recovered_beta_deg": float(beta_recovered_paper1),
            "bias_deg": float(bias_paper1),
            "signed_bias_deg": float(bias_paper1_signed),
            "per_realization_beta_std_deg": beta_scatter_paper1,
            "mc_mean_standard_error_deg": beta_mean_se_paper1,
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

np.savez_compressed(
    os.path.join(OUTPUT_DIR, "bandpowers.npz"),
    ell_eff=result_paper1["ell_effs"],
    input_cl_ee_raw_uK2=cl_ee,
    input_cl_bb_raw_uK2=cl_bb,
    null=result_null["all_cl_eb"],
    beta_0p270=result_paper1["all_cl_eb"],
    beta_0p342=result_obs["all_cl_eb"],
    theory_null=result_null["cl_eb_theory"],
    theory_0p270=result_paper1["cl_eb_theory"],
    theory_0p342=result_obs["cl_eb_theory"],
)

print(json.dumps(summary, indent=2))
print("\nCOMPLETE")
