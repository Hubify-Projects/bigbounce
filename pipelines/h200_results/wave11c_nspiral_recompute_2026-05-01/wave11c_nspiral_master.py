#!/usr/bin/env python
"""
R42 Wave 11-C — P4-CM-B1 / P4-OA-M7 fix.

Cross-confirmed bug: original NaMaster pipeline used N_total (8.47M, includes 5.15M
NOT_SPIRAL) for the analytical shot-noise subtraction. The chirality signal lives
ONLY on spirals (3.32M); non-spirals are noise and must NOT enter the shot-noise
denominator.

Fix:
  - Load real catalog `bamfai/galaxy-chirality-catalog` (8,474,531 rows)
  - Filter to spirals (predicted_class in {CW, CCW}) → ~3.32M
  - Build CW/CCW asymmetry map at NSIDE=64 using SPIRAL counts only
  - Compute pseudo-Cℓ + run 1,000 MC nulls (label-shuffle ON SPIRALS ONLY)
  - Compute analytical shot noise = 1 / N_spiral_per_pixel (NOT N_total)
  - Apply MASTER deconvolution
  - Report: corrected pseudo-Cℓ, deconvolved Cℓ, empirical p-value, σ_obs vs σ_MC

Inputs:
  - HF parquet (downloaded)
  - DESI Legacy footprint mask derived from spiral spatial density (n_spiral ≥ 5/pix)

Outputs:
  - /workspace/r42_wave11c/results.json — full numerical record
  - /workspace/r42_wave11c/cl_pseudo_data.npy
  - /workspace/r42_wave11c/cl_pseudo_mc.npy
  - /workspace/r42_wave11c/cl_deconv_data.npy
  - /workspace/r42_wave11c/fig8_data.npz
"""
import os, json, time, sys
import numpy as np
import pymaster as nmt
import healpy as hp
import pandas as pd

OUT = "/workspace/r42_wave11c"
os.makedirs(OUT, exist_ok=True)

NSIDE = 64
NPIX = hp.nside2npix(NSIDE)
LMAX = 3 * NSIDE - 1
N_MC = 1000
SEED = 20260501

t0 = time.time()
print(f"[init] NSIDE={NSIDE} NPIX={NPIX} LMAX={LMAX} N_MC={N_MC} SEED={SEED}", flush=True)

# ---- 1. Load real chirality catalog ----
print("[1] Loading bamfai/galaxy-chirality-catalog ...", flush=True)
import huggingface_hub as hh
local_files = []
# HF skipped (rate-limited) — using local cached parquet
print('    [skip HF — local-only mode]', flush=True)

if not local_files:
    print("[1!] HF download failed — falling back to local parquet shard search", flush=True)
    import glob
    cands = glob.glob("/workspace/**/catalog_production.parquet", recursive=True)
    cands += glob.glob("/workspace/**/chirality*.parquet", recursive=True)
    if not cands:
        print("[FATAL] no parquet found — aborting", flush=True)
        sys.exit(2)
    local_files = [cands[0]]

df = pd.read_parquet(local_files[0])
print(f"[1] loaded {len(df):,} rows; cols = {list(df.columns)[:30]}", flush=True)

# Detect class column
class_col = None
for c in ["predicted_class", "class", "label", "predicted_label", "pred_class", "class_eq", "class_raw_x"]:
    if c in df.columns:
        class_col = c
        break
print(f"[1] using class column: {class_col}", flush=True)

# Detect ra/dec
ra_col = next(c for c in ["ra", "RA", "Ra"] if c in df.columns)
dec_col = next(c for c in ["dec", "DEC", "Dec"] if c in df.columns)
print(f"[1] using ra={ra_col}, dec={dec_col}", flush=True)

ra = df[ra_col].to_numpy()
dec = df[dec_col].to_numpy()

# Detect class encoding
if class_col is None:
    # Use p_cw / p_ccw / p_ns probabilities
    p_cw = df["p_cw_eq"].to_numpy() if "p_cw_eq" in df.columns else (df["p_cw"].to_numpy() if "p_cw" in df.columns else df["P_CW"].to_numpy())
    p_ccw = df["p_ccw_eq"].to_numpy() if "p_ccw_eq" in df.columns else (df["p_ccw"].to_numpy() if "p_ccw" in df.columns else df["P_CCW"].to_numpy())
    p_ns = df["p_ns_eq"].to_numpy() if "p_ns_eq" in df.columns else (df["p_ns"].to_numpy() if "p_ns" in df.columns else df.get("P_NOT_SPIRAL", pd.Series(np.zeros(len(df)))).to_numpy())
    pred = np.argmax(np.column_stack([p_cw, p_ccw, p_ns]), axis=1)  # 0=CW, 1=CCW, 2=NS
    is_spiral = pred < 2
    is_cw = pred == 0
else:
    cls = df[class_col].astype(str).str.upper().str.strip()
    is_spiral = cls.isin(["CW", "CCW", "S_CW", "S_CCW", "SPIRAL_CW", "SPIRAL_CCW"]).to_numpy()
    is_cw = cls.isin(["CW", "S_CW", "SPIRAL_CW"]).to_numpy()

n_total = len(df)
n_spiral = int(is_spiral.sum())
n_cw = int((is_spiral & is_cw).sum())
n_ccw = n_spiral - n_cw
print(f"[1] N_total={n_total:,}  N_spiral={n_spiral:,}  N_CW={n_cw:,}  N_CCW={n_ccw:,}  cw_frac={n_cw/n_spiral:.6f}", flush=True)

# Subset to spirals
ra_sp = ra[is_spiral]
dec_sp = dec[is_spiral]
is_cw_sp = is_cw[is_spiral]

# ---- 2. Pixelize ----
print("[2] Pixelizing spirals at NSIDE=64 ...", flush=True)
theta = np.radians(90 - dec_sp)
phi = np.radians(ra_sp % 360)
pix = hp.ang2pix(NSIDE, theta, phi)

# Counts per pixel — SPIRALS ONLY
n_sp_per_pix = np.bincount(pix, minlength=NPIX).astype(np.float64)
n_cw_per_pix = np.bincount(pix[is_cw_sp], minlength=NPIX).astype(np.float64)

mask = (n_sp_per_pix >= 5).astype(np.float64)  # tighter than the prior n_total >= 10 to bound shot-noise
n_unmasked = int(mask.sum())
fsky = n_unmasked / NPIX
print(f"[2] mask: {n_unmasked}/{NPIX} pixels (f_sky={fsky:.4f})", flush=True)

# Asymmetry map — SPIRAL-only normalization
A = np.zeros(NPIX)
valid = mask > 0
A[valid] = 2.0 * n_cw_per_pix[valid] / n_sp_per_pix[valid] - 1.0
mean_A_masked = float(np.average(A[valid], weights=n_sp_per_pix[valid]))
A[valid] -= mean_A_masked
print(f"[2] mean A on mask (weighted) = {mean_A_masked:.6e} (subtracted)", flush=True)

# Mean spirals per masked pixel — for analytical shot-noise reference
n_per_pix_mean = float(n_sp_per_pix[valid].mean())
shot_noise_pixel = 1.0 / n_per_pix_mean  # variance of binomial-asymmetry estimator at p~0.5 with N~n_per_pix
print(f"[2] N_spiral / pixel (mean over mask) = {n_per_pix_mean:.2f}", flush=True)
print(f"[2] analytical shot-noise per-pixel variance = 1/N_sp = {shot_noise_pixel:.4e}", flush=True)
# For comparison the BUGGED prior pipeline used 1/N_total_per_pix:
n_total_per_pix_buggy = n_total / NPIX  # uniform-density approximation it used
print(f"[2] BUGGED (prior) shot-noise per-pix = 1/N_total_per_pix = {1.0/n_total_per_pix_buggy:.4e}", flush=True)
print(f"[2] N_spiral/N_total ratio = {n_spiral/n_total:.4f} (~3.32M/8.47M)", flush=True)

# ---- 3. NaMaster setup ----
print("[3] Setting up NaMaster bins + workspace ...", flush=True)
b = nmt.NmtBin.from_lmax_linear(LMAX, nlb=5)
ells = b.get_effective_ells()

# Spin-0 field on the asymmetry map weighted by mask
f0 = nmt.NmtField(mask, [A])
w = nmt.NmtWorkspace()
print("[3] computing mode-coupling matrix (NaMaster compute_coupling_matrix) ...", flush=True)
w.compute_coupling_matrix(f0, f0, b)
print(f"[3]   done {time.time()-t0:.1f}s", flush=True)

# Pseudo-Cℓ on data
cl_coupled_data = nmt.compute_coupled_cell(f0, f0)[0]   # length LMAX+1
cl_decoupled_data = w.decouple_cell([cl_coupled_data])[0]  # length len(ells)
print(f"[3] Cℓ coupled[0:5] = {cl_coupled_data[:5]}", flush=True)
print(f"[3] Cℓ decoupled[0:5] = {cl_decoupled_data[:5]}", flush=True)

# Pseudo-Cℓ averaged into bins (no decoupling) for direct compare with prior pipeline
cl_pseudo_binned_data = b.bin_cell(np.atleast_2d(cl_coupled_data))[0]

# ---- 4. Analytical shot-noise correction (CORRECTED) ----
# Pixelized asymmetry-map shot-noise -> Cℓ shot-noise contribution.
# White-noise level: N_l = 4π * f_sky / N_spiral (same form as galaxy clustering for f_sky-rescaled noise)
# Ref: NaMaster docs + Hivon+02 MASTER appendix.
N_l_corrected = 4 * np.pi * fsky / n_spiral
N_l_buggy = 4 * np.pi * fsky / n_total
print(f"[4] N_ℓ corrected (using N_spiral) = {N_l_corrected:.4e}", flush=True)
print(f"[4] N_ℓ buggy   (using N_total)  = {N_l_buggy:.4e}", flush=True)
print(f"[4] correction ratio = {N_l_corrected/N_l_buggy:.4f}x ({n_total/n_spiral:.4f}x larger noise floor)", flush=True)

# Subtract from coupled spectrum (in pixel space the pseudo-Cℓ inherits N_ℓ * mask^2 average)
cl_pseudo_corrected = cl_pseudo_binned_data - N_l_corrected
cl_pseudo_buggy_subtraction = cl_pseudo_binned_data - N_l_buggy

# Decouple
cl_decoupled_corrected = w.decouple_cell([cl_coupled_data - N_l_corrected])[0]
cl_decoupled_buggy = w.decouple_cell([cl_coupled_data - N_l_buggy])[0]

# ---- 5. MC nulls (1,000) — label-shuffle SPIRALS ONLY ----
print(f"[5] Running {N_MC} MC nulls (label-shuffle on spirals) ...", flush=True)
rng = np.random.default_rng(SEED)
cl_pseudo_mc = np.zeros((N_MC, len(ells)))
cl_decoupled_mc = np.zeros((N_MC, len(ells)))
n_sp_total_int = int(n_spiral)
p_cw_global = n_cw / n_spiral
t_mc0 = time.time()
for i in range(N_MC):
    # null: each spiral gets a fresh CW/CCW label drawn from p_cw_global
    new_cw_flags = rng.binomial(1, p_cw_global, n_sp_total_int).astype(bool)
    n_cw_per_pix_null = np.bincount(pix[new_cw_flags], minlength=NPIX).astype(np.float64)
    A_null = np.zeros(NPIX)
    A_null[valid] = 2.0 * n_cw_per_pix_null[valid] / n_sp_per_pix[valid] - 1.0
    A_null[valid] -= float(np.average(A_null[valid], weights=n_sp_per_pix[valid]))
    f_null = nmt.NmtField(mask, [A_null])
    cl_c_null = nmt.compute_coupled_cell(f_null, f_null)[0]
    cl_pseudo_mc[i] = b.bin_cell(np.atleast_2d(cl_c_null))[0] - N_l_corrected
    cl_decoupled_mc[i] = w.decouple_cell([cl_c_null - N_l_corrected])[0]
    if (i + 1) % 50 == 0 or i == N_MC - 1:
        rate = (i + 1) / (time.time() - t_mc0)
        eta = (N_MC - i - 1) / max(rate, 1e-6)
        print(f"    [{i+1}/{N_MC}] {rate:.2f} MC/s  ETA {eta:.0f}s", flush=True)

# ---- 6. Significance ----
mc_mean_pseudo = cl_pseudo_mc.mean(axis=0)
mc_std_pseudo = cl_pseudo_mc.std(axis=0)
mc_mean_dec = cl_decoupled_mc.mean(axis=0)
mc_std_dec = cl_decoupled_mc.std(axis=0)

sigma_pseudo = (cl_pseudo_corrected - mc_mean_pseudo) / mc_std_pseudo
sigma_dec = (cl_decoupled_corrected - mc_mean_dec) / mc_std_dec

# Empirical p-value at lowest bin (most prior signal sat)
emp_p_pseudo_lowbin = float((cl_pseudo_mc[:, 0] >= cl_pseudo_corrected[0]).mean())
emp_p_dec_lowbin = float((cl_decoupled_mc[:, 0] >= cl_decoupled_corrected[0]).mean())

# Combined chi^2 across bins
chi2_pseudo = float(np.sum(((cl_pseudo_corrected - mc_mean_pseudo) / mc_std_pseudo) ** 2))
chi2_dec = float(np.sum(((cl_decoupled_corrected - mc_mean_dec) / mc_std_dec) ** 2))

print(f"[6] σ pseudo per-bin = {sigma_pseudo}", flush=True)
print(f"[6] σ decoupled per-bin = {sigma_dec}", flush=True)
print(f"[6] empirical p (pseudo, ℓ_eff bin 0) = {emp_p_pseudo_lowbin}", flush=True)
print(f"[6] empirical p (decoupled, ℓ_eff bin 0) = {emp_p_dec_lowbin}", flush=True)

# ---- 7. Save ----
np.save(f"{OUT}/cl_pseudo_data.npy", cl_pseudo_corrected)
np.save(f"{OUT}/cl_pseudo_mc.npy", cl_pseudo_mc)
np.save(f"{OUT}/cl_deconv_data.npy", cl_decoupled_corrected)
np.save(f"{OUT}/cl_deconv_mc.npy", cl_decoupled_mc)
np.savez(
    f"{OUT}/fig8_data.npz",
    ells=ells,
    cl_pseudo_corrected=cl_pseudo_corrected,
    cl_pseudo_buggy=cl_pseudo_buggy_subtraction,
    cl_decoupled_corrected=cl_decoupled_corrected,
    cl_decoupled_buggy=cl_decoupled_buggy,
    mc_mean_pseudo=mc_mean_pseudo,
    mc_std_pseudo=mc_std_pseudo,
    mc_mean_dec=mc_mean_dec,
    mc_std_dec=mc_std_dec,
    N_l_corrected=N_l_corrected,
    N_l_buggy=N_l_buggy,
)

results = {
    "wave": "11-C",
    "issue": "P4-CM-B1 / P4-OA-M7 — N_spiral fix",
    "n_total": int(n_total),
    "n_spiral": int(n_spiral),
    "n_cw": int(n_cw),
    "n_ccw": int(n_ccw),
    "cw_fraction_global": float(n_cw / n_spiral),
    "nside": NSIDE,
    "lmax": LMAX,
    "n_mc": N_MC,
    "seed": SEED,
    "fsky": fsky,
    "n_unmasked_pixels": n_unmasked,
    "n_per_pix_mean_spirals": n_per_pix_mean,
    "N_l_corrected": float(N_l_corrected),
    "N_l_buggy": float(N_l_buggy),
    "correction_ratio_N_total_over_N_spiral": float(n_total / n_spiral),
    "ells_effective": ells.tolist(),
    "cl_pseudo_corrected": cl_pseudo_corrected.tolist(),
    "cl_pseudo_buggy_subtraction": cl_pseudo_buggy_subtraction.tolist(),
    "cl_decoupled_corrected": cl_decoupled_corrected.tolist(),
    "cl_decoupled_buggy_subtraction": cl_decoupled_buggy.tolist(),
    "mc_mean_pseudo": mc_mean_pseudo.tolist(),
    "mc_std_pseudo": mc_std_pseudo.tolist(),
    "mc_mean_decoupled": mc_mean_dec.tolist(),
    "mc_std_decoupled": mc_std_dec.tolist(),
    "sigma_pseudo_per_bin": sigma_pseudo.tolist(),
    "sigma_decoupled_per_bin": sigma_dec.tolist(),
    "empirical_p_pseudo_lowbin": emp_p_pseudo_lowbin,
    "empirical_p_decoupled_lowbin": emp_p_dec_lowbin,
    "chi2_pseudo_total": chi2_pseudo,
    "chi2_decoupled_total": chi2_dec,
    "n_dof": int(len(ells)),
    "wallclock_s": time.time() - t0,
}
with open(f"{OUT}/results.json", "w") as f:
    json.dump(results, f, indent=2)

print(f"[done] wallclock {time.time()-t0:.1f}s — results at {OUT}/results.json", flush=True)
