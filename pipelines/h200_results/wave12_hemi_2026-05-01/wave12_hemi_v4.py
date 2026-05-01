#!/usr/bin/env python
"""
Wave 12 hemisphere look-elsewhere null v4 — GPU-accelerated.

Goal: tighten precision floor from 1/501 (v3) to 1/10001 by running N_MC=10,000
on H200 GPU. Keeps HEMI matrix on GPU, batches permutations on GPU.

Output: /workspace/r42_wave12_hemi/results.json + max_null.npy
"""
import os
import json
import time
import numpy as np
import pandas as pd
import healpy as hp
import torch

# ---------------- Config ----------------
CATALOG = "/workspace/r42_b20/chirality_catalog/catalog_production.parquet"
OUTDIR  = "/workspace/r42_wave12_hemi"
NSIDE_DIR = 8
N_MC = 10_000
BATCH = 100   # per-batch permutations on GPU
SEED = 42
os.makedirs(OUTDIR, exist_ok=True)

np.random.seed(SEED)
torch.manual_seed(SEED)

device = torch.device("cuda")
print(f"[init] torch={torch.__version__} cuda={torch.cuda.is_available()} dev={torch.cuda.get_device_name(0)}", flush=True)
print(f"[init] N_MC={N_MC} BATCH={BATCH} NSIDE_DIR={NSIDE_DIR} SEED={SEED}", flush=True)

t0 = time.time()
print(f"[load] reading catalog: {CATALOG}", flush=True)
df = pd.read_parquet(CATALOG, columns=["ra", "dec", "class_eq"])
print(f"[load] total rows: {len(df):,}", flush=True)

sp = df[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
n_sp = len(sp)
print(f"[load] spirals: {n_sp:,}", flush=True)
del df

ra  = sp["ra"].to_numpy(dtype=np.float64)
dec = sp["dec"].to_numpy(dtype=np.float64)
cw_label = (sp["class_eq"].to_numpy() == "CW").astype(np.float32)
del sp
print(f"[load] CW frac = {cw_label.mean():.6f}", flush=True)

# ---------------- Hemisphere matrix ----------------
ndirs = hp.nside2npix(NSIDE_DIR)
print(f"[hemi] ndirs={ndirs} (NSIDE_DIR={NSIDE_DIR})", flush=True)

# Direction unit vectors
dir_vecs = np.array(hp.pix2vec(NSIDE_DIR, np.arange(ndirs))).T   # (ndirs, 3)

# Galaxy unit vectors
theta_g = np.deg2rad(90.0 - dec)
phi_g   = np.deg2rad(ra)
gx = np.sin(theta_g) * np.cos(phi_g)
gy = np.sin(theta_g) * np.sin(phi_g)
gz = np.cos(theta_g)
gal_vecs = np.stack([gx, gy, gz], axis=1)   # (n_sp, 3)
del theta_g, phi_g, gx, gy, gz

print(f"[hemi] building HEMI matrix in chunks ({ndirs} x {n_sp:,}, uint8)...", flush=True)
HEMI = np.zeros((ndirs, n_sp), dtype=np.uint8)
chunk = 64
t_h = time.time()
for i in range(0, ndirs, chunk):
    j = min(i + chunk, ndirs)
    dots = dir_vecs[i:j] @ gal_vecs.T   # (chunk, n_sp)
    HEMI[i:j] = (dots >= 0.0).astype(np.uint8)
    if (i // chunk) % 4 == 0:
        print(f"[hemi]   dir {j}/{ndirs}  t={time.time()-t_h:.1f}s", flush=True)
del dir_vecs, gal_vecs
print(f"[hemi] HEMI built in {time.time()-t_h:.1f}s, size={HEMI.nbytes/1e9:.2f} GB", flush=True)

# n_total per direction (CPU then GPU)
n_total_per_dir = HEMI.sum(axis=1).astype(np.float64)   # (ndirs,)

# ---------------- Move to GPU ----------------
print(f"[gpu] moving HEMI to GPU as float32...", flush=True)
HEMI_GPU = torch.from_numpy(HEMI).to(device).to(torch.float32)   # (ndirs, n_sp)
print(f"[gpu] HEMI_GPU shape={tuple(HEMI_GPU.shape)} dtype={HEMI_GPU.dtype} VRAM~{HEMI_GPU.element_size()*HEMI_GPU.nelement()/1e9:.2f} GB", flush=True)
del HEMI   # free system RAM ASAP

cw_GPU = torch.from_numpy(cw_label).to(device).to(torch.float32)   # (n_sp,)
ntot_GPU = torch.from_numpy(n_total_per_dir).to(device).to(torch.float32)   # (ndirs,)
HEMI_T = HEMI_GPU.T   # (n_sp, ndirs)  — note: (B, n_sp) @ (n_sp, ndirs) = (B, ndirs)
print(f"[gpu] cw_GPU n_sp={cw_GPU.numel():,}  ntot_GPU shape={tuple(ntot_GPU.shape)}", flush=True)
print(f"[gpu] free VRAM: {torch.cuda.mem_get_info()[0]/1e9:.2f} GB / {torch.cuda.mem_get_info()[1]/1e9:.2f} GB", flush=True)

# ---------------- Observed asymmetry ----------------
n_cw_obs = (cw_GPU.unsqueeze(0) @ HEMI_T).squeeze(0).cpu().numpy()   # (ndirs,)
asym_obs = (2.0 * n_cw_obs - n_total_per_dir) / n_total_per_dir
A_obs = float(np.max(np.abs(asym_obs)))
i_obs = int(np.argmax(np.abs(asym_obs)))
print(f"[obs] max |asymmetry| = {A_obs:.6f} at dir idx={i_obs}", flush=True)

# ---------------- MC permutation null ----------------
print(f"[mc] starting N_MC={N_MC} (batch={BATCH})", flush=True)
max_null = np.zeros(N_MC, dtype=np.float64)
n_batches = N_MC // BATCH
t_mc = time.time()
mc_done = 0

for b in range(n_batches):
    # Generate B permutations on GPU: argsort of random numbers = random permutation
    rand_keys = torch.rand(BATCH, n_sp, device=device, dtype=torch.float32)
    perm_idx = torch.argsort(rand_keys, dim=1)   # (B, n_sp)
    del rand_keys
    # Gather labels per permutation
    labels_perm = torch.gather(cw_GPU.unsqueeze(0).expand(BATCH, -1), 1, perm_idx)   # (B, n_sp)
    del perm_idx
    # n_cw per direction: (B, n_sp) @ (n_sp, ndirs) = (B, ndirs)
    n_cw = labels_perm @ HEMI_T
    del labels_perm
    asym = (2.0 * n_cw - ntot_GPU.unsqueeze(0)) / ntot_GPU.unsqueeze(0)
    del n_cw
    max_per_perm = torch.max(torch.abs(asym), dim=1).values   # (B,)
    del asym
    max_null[b*BATCH:(b+1)*BATCH] = max_per_perm.cpu().numpy()
    del max_per_perm

    mc_done += BATCH
    if mc_done % 1000 == 0 or b == 0:
        elapsed = time.time() - t_mc
        rate = mc_done / elapsed if elapsed > 0 else 0
        eta = (N_MC - mc_done) / rate if rate > 0 else 0
        n_ge = int(np.sum(max_null[:mc_done] >= A_obs))
        print(f"[mc] {mc_done}/{N_MC}  elapsed={elapsed:.1f}s  rate={rate:.1f} MC/s  ETA={eta/60:.1f}min  n_ge_obs={n_ge}", flush=True)

mc_elapsed = time.time() - t_mc
print(f"[mc] done in {mc_elapsed:.1f}s ({N_MC/mc_elapsed:.1f} MC/s)", flush=True)

# ---------------- Stats ----------------
n_ge = int(np.sum(max_null >= A_obs))
p_lee = (n_ge + 1) / (N_MC + 1)
print(f"[result] N_MC={N_MC}  n_ge_obs={n_ge}  p_LEE = ({n_ge}+1)/({N_MC}+1) = {p_lee:.6g}", flush=True)
print(f"[result] precision floor = 1/{N_MC+1} = {1/(N_MC+1):.6g}", flush=True)

# ---------------- Save ----------------
np.save(os.path.join(OUTDIR, "max_null.npy"), max_null)

results = {
    "wave": "12",
    "version": "v4_gpu",
    "seed": SEED,
    "n_mc": N_MC,
    "batch": BATCH,
    "nside_dir": NSIDE_DIR,
    "ndirs": int(ndirs),
    "n_spirals": int(n_sp),
    "cw_fraction": float(cw_label.mean()),
    "A_obs": A_obs,
    "i_obs_dir": i_obs,
    "n_ge_obs": n_ge,
    "p_LEE": p_lee,
    "precision_floor": 1.0/(N_MC+1),
    "mc_seconds": mc_elapsed,
    "total_seconds": time.time() - t0,
    "device": torch.cuda.get_device_name(0),
}
with open(os.path.join(OUTDIR, "results.json"), "w") as f:
    json.dump(results, f, indent=2)

print(f"[done] wrote {OUTDIR}/results.json + max_null.npy", flush=True)
print(f"[done] total wall = {time.time()-t0:.1f}s", flush=True)
