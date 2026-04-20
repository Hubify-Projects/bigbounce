#!/usr/bin/env python3
"""
Planck SMICA Native CMB Autoencoder RETRAIN — P3-PATHC-CMB-NATIVE-RETRAIN
========================================================================
Rebuilds the CMB convolutional autoencoder at Path-C scale:
  * 200K training patches (previous: 20K) with galactic-plane mask |b| >= 20 deg
  * Planck SMICA_2048 R3.00 full-sky temperature map (monopole + dipole removed)
  * 64 x 64 patches, 10 deg x 10 deg FoV (matches pipelines/pipeline_a_cmb design)
  * Longer schedule: up to 150 epochs, patience=25, ReduceLROnPlateau(patience=10)
  * GATE: reconstruction of a 5x-noise planted-anomaly set >= 50 % recovered at
    the 99th-percentile MSE threshold on clean validation patches.

Architecture (unchanged, reuses pipeline_a_cmb/cmb_autoencoder.py design):
  Encoder: Conv2d(1,16,3,s2,p1)-BN-ReLU -> Conv2d(16,32,3,s2,p1)-BN-ReLU ->
           Conv2d(32,64,3,s2,p1)-BN-ReLU -> Flatten -> Linear(64*8*8, 128)
  Decoder: Linear(128, 64*8*8)-ReLU -> reshape(64,8,8) ->
           ConvT(64,32,3,s2,p1,op1)-BN-ReLU ->
           ConvT(32,16,3,s2,p1,op1)-BN-ReLU ->
           ConvT(16, 1,3,s2,p1,op1)-Tanh
  Latent: 128   Loss: MSE

Why this retrain: the existing CMB run in Paper 3 Table 1 (20K patches,
val_loss unpublished) was QC-flagged because the small patch budget missed
key large-scale anomaly classes (cold spot scale hemispherical asymmetry).
200K patches at |b| >= 20 deg cover >30 % of the sky with ~10 patches per
square degree, restoring sensitivity to degree-scale features.

Output: /workspace/bigbounce_scan/outputs/cmb_native/
  best_cmb_native.pt                    - best state_dict
  training_losses.json                  - train + val curves
  injection_recovery.json               - gate results
  cmb_native_patches.npy                - stacked 200K x 64 x 64 float32
  cmb_native_metadata.json              - per-patch (glon, glat, b, raw_std)

Runs alongside sdss_native_rescore + lamost_native_rescore on the same A100
(re-scores are download-bound, GPU idle between batches -> CMB training
fills the idle windows without contention).

Budget: ~8h training + 1h patch-extraction + 0.5h gate = ~10h pod time
        ~= $12 at $1.19/h.  Fire #83 kickoff.
"""
import os
import sys
import json
import time
import argparse
import urllib.request
import numpy as np

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader, random_split

import healpy as hp
import warnings
warnings.filterwarnings('ignore')


# -------------------------------------------------------------------- constants
GAL_CUT_DEG      = 20.0
PATCH_DEG        = 10.0
PATCH_PIX        = 64
CMB_FIELD        = 0
N_PATCHES        = 200_000          # Path-C target (10x previous)
LATENT_DIM       = 128
BATCH_SIZE       = 128              # A100 handles this easily for 64x64
EPOCHS_MAX       = 150
PATIENCE_ES      = 25
PATIENCE_LR      = 10
LR_INIT          = 1e-3
VAL_FRAC         = 0.15
SEED             = 42

# Gate — Path C injection-recovery criterion
INJECT_N         = 500              # how many planted anomalies
INJECT_AMP       = 5.0              # 5x noise amplitude
GATE_RECOVERY    = 0.50             # >= 50 % of plants above 99th-pct clean MSE
GATE_PCTL        = 99.0

SMICA_URL = ("https://irsa.ipac.caltech.edu/data/Planck/release_3/"
             "all-sky-maps/maps/component-maps/cmb/"
             "COM_CMB_IQU-smica_2048_R3.00_full.fits")


# --------------------------------------------------------------------- download
def download_smica(dest):
    print(f'Downloading SMICA map -> {dest}', flush=True)
    req = urllib.request.Request(SMICA_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=300) as resp, open(dest, 'wb') as f:
        total = int(resp.headers.get('Content-Length', 0))
        got = 0
        t0 = time.time()
        while True:
            chunk = resp.read(1 << 20)
            if not chunk: break
            f.write(chunk); got += len(chunk)
            if total:
                pct = 100 * got / total
                mb_s = got / (1 << 20) / max(time.time() - t0, 0.01)
                print(f'  {got/(1<<20):.0f}/{total/(1<<20):.0f} MB ({pct:.1f}%) {mb_s:.1f} MB/s', end='\r', flush=True)
        print(flush=True)
    size = os.path.getsize(dest)
    if size < 50 * (1 << 20):
        os.remove(dest); raise RuntimeError(f'Download too small: {size}')
    print(f'Downloaded {size/(1<<20):.1f} MB', flush=True)


# ------------------------------------------------------------- patch extraction
def generate_positions(n, gal_cut_deg, seed):
    rng = np.random.default_rng(seed)
    pos = []
    budget = n * 20
    tries = 0
    while len(pos) < n and tries < budget:
        cos_t = rng.uniform(-1, 1)
        theta = np.arccos(cos_t)
        phi = rng.uniform(0, 2 * np.pi)
        b = 90.0 - np.degrees(theta)
        if abs(b) >= gal_cut_deg:
            pos.append((theta, phi))
        tries += 1
    return pos


def extract_one(cmb_map, theta, phi, patch_deg, patch_pix):
    lon_deg = np.degrees(phi)
    lat_deg = 90.0 - np.degrees(theta)
    reso = patch_deg * 60.0 / patch_pix
    arr = hp.gnomview(cmb_map, rot=(lon_deg, lat_deg), reso=reso,
                      xsize=patch_pix, ysize=patch_pix,
                      return_projected_map=True, no_plot=True)
    return np.array(arr, dtype=np.float64)


def normalize(p):
    if hasattr(p, 'filled'):
        p = np.array(p.filled(np.nan))
    valid = ~np.isnan(p)
    if valid.sum() < p.size * 0.9:
        return None
    mu = np.nanmean(p); sd = np.nanstd(p)
    if sd < 1e-30: return None
    p = (p - mu) / sd
    p[~valid] = 0.0
    # Path-C defensive clip (lesson from fires #80, #81, #82)
    if not np.isfinite(p).all(): return None
    if np.abs(p).max() > 100.0: return None
    np.clip(p, -10.0, 10.0, out=p)
    return p.astype(np.float32)


def build_patch_bank(smica_path, out_dir, n_patches=N_PATCHES,
                    patch_deg=PATCH_DEG, patch_pix=PATCH_PIX, seed=SEED):
    patches_path = os.path.join(out_dir, 'cmb_native_patches.npy')
    meta_path    = os.path.join(out_dir, 'cmb_native_metadata.json')
    if os.path.exists(patches_path) and os.path.exists(meta_path):
        print(f'Reusing existing patch bank: {patches_path}', flush=True)
        return patches_path, meta_path

    print(f'Loading SMICA map {smica_path}', flush=True)
    t0 = time.time()
    cmb = hp.read_map(smica_path, field=CMB_FIELD, dtype=np.float64)
    cmb = hp.remove_dipole(cmb, verbose=False)
    print(f'  NSIDE={hp.get_nside(cmb)}, {time.time()-t0:.0f}s', flush=True)

    positions = generate_positions(n_patches, GAL_CUT_DEG, seed)
    print(f'Generated {len(positions)} positions (|b|>={GAL_CUT_DEG})', flush=True)

    patches, meta = [], []
    n_rej = 0; t0 = time.time()
    for i, (theta, phi) in enumerate(positions):
        try:
            raw = extract_one(cmb, theta, phi, patch_deg, patch_pix)
            norm = normalize(raw)
            if norm is None:
                n_rej += 1; continue
            patches.append(norm)
            meta.append({
                'idx': len(patches) - 1,
                'glon_deg': float(np.degrees(phi)),
                'glat_deg': float(90.0 - np.degrees(theta)),
                'raw_std': float(np.nanstd(raw)),
            })
        except Exception:
            n_rej += 1
        if (i + 1) % 5000 == 0:
            rate = (i + 1) / max(time.time() - t0, 0.01)
            eta = (len(positions) - i - 1) / rate / 60
            print(f'  {i+1}/{len(positions)} ({rate:.0f}/s, ETA {eta:.0f}m, '
                  f'kept {len(patches)}, rej {n_rej})', flush=True)

    arr = np.stack(patches, axis=0)
    print(f'Saving {arr.shape} -> {patches_path}', flush=True)
    np.save(patches_path, arr)
    with open(meta_path, 'w') as f:
        json.dump(meta, f)
    return patches_path, meta_path


# ------------------------------------------------------------------- model + ds
class CMBPatchDS(Dataset):
    def __init__(self, arr):
        if arr.ndim == 3:
            arr = arr[:, None, :, :]
        self.arr = arr
    def __len__(self): return len(self.arr)
    def __getitem__(self, i): return torch.from_numpy(self.arr[i])


class CMBAutoencoder(nn.Module):
    def __init__(self, latent=LATENT_DIM):
        super().__init__()
        self.encoder_conv = nn.Sequential(
            nn.Conv2d(1, 16, 3, 2, 1), nn.BatchNorm2d(16), nn.ReLU(True),
            nn.Conv2d(16, 32, 3, 2, 1), nn.BatchNorm2d(32), nn.ReLU(True),
            nn.Conv2d(32, 64, 3, 2, 1), nn.BatchNorm2d(64), nn.ReLU(True),
        )
        self.encoder_fc = nn.Sequential(nn.Flatten(), nn.Linear(64*8*8, latent))
        self.decoder_fc = nn.Sequential(nn.Linear(latent, 64*8*8), nn.ReLU(True))
        self.decoder_conv = nn.Sequential(
            nn.ConvTranspose2d(64, 32, 3, 2, 1, 1), nn.BatchNorm2d(32), nn.ReLU(True),
            nn.ConvTranspose2d(32, 16, 3, 2, 1, 1), nn.BatchNorm2d(16), nn.ReLU(True),
            nn.ConvTranspose2d(16, 1,  3, 2, 1, 1), nn.Tanh(),
        )
    def encode(self, x): return self.encoder_fc(self.encoder_conv(x))
    def decode(self, z):
        h = self.decoder_fc(z).view(-1, 64, 8, 8)
        return self.decoder_conv(h)
    def forward(self, x):
        z = self.encode(x); return self.decode(z), z


# --------------------------------------------------------------------- training
def train(patches_path, out_dir, device):
    arr = np.load(patches_path).astype(np.float32)
    print(f'Loaded patches {arr.shape}', flush=True)
    ds = CMBPatchDS(arr)
    n_val = int(len(ds) * VAL_FRAC); n_tr = len(ds) - n_val
    tr, va = random_split(ds, [n_tr, n_val],
                          generator=torch.Generator().manual_seed(SEED))
    tr_loader = DataLoader(tr, batch_size=BATCH_SIZE, shuffle=True,
                           num_workers=4, pin_memory=True)
    va_loader = DataLoader(va, batch_size=BATCH_SIZE, shuffle=False,
                           num_workers=4, pin_memory=True)

    model = CMBAutoencoder().to(device)
    n_params = sum(p.numel() for p in model.parameters())
    print(f'Model params: {n_params:,}', flush=True)

    opt = optim.Adam(model.parameters(), lr=LR_INIT)
    sched = optim.lr_scheduler.ReduceLROnPlateau(opt, 'min', 0.5, patience=PATIENCE_LR)
    crit = nn.MSELoss()

    model_path = os.path.join(out_dir, 'best_cmb_native.pt')
    losses = {'train': [], 'val': [], 'best_val': float('inf'), 'best_epoch': 0}
    no_imp = 0

    for ep in range(1, EPOCHS_MAX + 1):
        t0 = time.time()
        model.train(); tr_loss = 0.0
        for xb in tr_loader:
            xb = xb.to(device, non_blocking=True)
            recon, _ = model(xb)
            loss = crit(recon, xb)
            opt.zero_grad(); loss.backward(); opt.step()
            tr_loss += loss.item() * xb.size(0)
        tr_loss /= n_tr

        model.eval(); va_loss = 0.0
        with torch.no_grad():
            for xb in va_loader:
                xb = xb.to(device, non_blocking=True)
                recon, _ = model(xb)
                va_loss += crit(recon, xb).item() * xb.size(0)
        va_loss /= n_val

        losses['train'].append(tr_loss)
        losses['val'].append(va_loss)
        sched.step(va_loss)

        if va_loss < losses['best_val']:
            losses['best_val'] = va_loss
            losses['best_epoch'] = ep
            no_imp = 0
            torch.save(model.state_dict(), model_path)
        else:
            no_imp += 1

        print(f'  epoch {ep:3d}/{EPOCHS_MAX}  tr={tr_loss:.6f}  va={va_loss:.6f}  '
              f'best={losses["best_val"]:.6f}@ep{losses["best_epoch"]}  '
              f'[{time.time()-t0:.0f}s, no_imp={no_imp}]', flush=True)

        with open(os.path.join(out_dir, 'training_losses.json'), 'w') as f:
            json.dump(losses, f, indent=2)

        if no_imp >= PATIENCE_ES:
            print(f'Early stop at ep {ep} (no improvement {PATIENCE_ES})', flush=True)
            break

    return model_path, losses


# ---------------------------------------------------------------- injection gate
def injection_recovery(model_path, patches_path, out_dir, device,
                       n_inject=INJECT_N, amp=INJECT_AMP,
                       pctl=GATE_PCTL, gate=GATE_RECOVERY):
    print('=' * 60, flush=True)
    print(f'INJECTION-RECOVERY GATE: {n_inject} plants @ {amp}x noise', flush=True)
    arr = np.load(patches_path).astype(np.float32)
    n_val = int(len(arr) * VAL_FRAC)
    rng = np.random.default_rng(SEED)
    idx = rng.permutation(len(arr))
    val_idx = idx[:n_val]
    val = arr[val_idx][:, None, :, :]

    # Plant anomalies: 5x-noise gaussian bump (sigma=8 pix ~= 1.25 deg) on a
    # random subset of val patches, leave rest clean.
    inject_ids = rng.choice(len(val), size=n_inject, replace=False)
    planted = val.copy()
    yy, xx = np.meshgrid(np.arange(PATCH_PIX), np.arange(PATCH_PIX), indexing='ij')
    for j in inject_ids:
        cy = rng.integers(16, 48); cx = rng.integers(16, 48)
        bump = amp * np.exp(-((yy - cy) ** 2 + (xx - cx) ** 2) / (2 * 8.0 ** 2))
        sign = rng.choice([-1.0, 1.0])
        planted[j, 0] += sign * bump.astype(np.float32)

    model = CMBAutoencoder().to(device)
    model.load_state_dict(torch.load(model_path, map_location=device, weights_only=True))
    model.eval()

    def mse_score(batch):
        out = []
        with torch.no_grad():
            for k in range(0, len(batch), 512):
                xb = torch.from_numpy(batch[k:k+512]).to(device)
                recon, _ = model(xb)
                m = ((recon - xb) ** 2).mean(dim=(1, 2, 3)).cpu().numpy()
                out.append(m)
        return np.concatenate(out)

    clean_scores   = mse_score(val)
    planted_scores = mse_score(planted)
    thr = np.percentile(clean_scores, pctl)
    plant_mse = planted_scores[inject_ids]
    recovered = int((plant_mse > thr).sum())
    recov_frac = recovered / n_inject
    gate_pass = recov_frac >= gate

    result = {
        'n_inject': n_inject,
        'amp_sigma': amp,
        'clean_mse_p50': float(np.median(clean_scores)),
        'clean_mse_p99': float(np.percentile(clean_scores, 99)),
        'threshold_pctl': pctl,
        'threshold_value': float(thr),
        'planted_mse_p50': float(np.median(plant_mse)),
        'planted_mse_min': float(plant_mse.min()),
        'planted_mse_max': float(plant_mse.max()),
        'recovered': recovered,
        'recovery_fraction': float(recov_frac),
        'gate_required': gate,
        'gate_pass': bool(gate_pass),
    }
    with open(os.path.join(out_dir, 'injection_recovery.json'), 'w') as f:
        json.dump(result, f, indent=2)
    print(f'  clean  p50={result["clean_mse_p50"]:.4e}  p99={result["clean_mse_p99"]:.4e}', flush=True)
    print(f'  plant  p50={result["planted_mse_p50"]:.4e}', flush=True)
    print(f'  thr    p{pctl}={thr:.4e}', flush=True)
    print(f'  RECOVERED {recovered}/{n_inject} ({recov_frac:.1%})  '
          f'GATE {"PASS" if gate_pass else "FAIL"} (>={gate:.0%})', flush=True)
    return result


# ---------------------------------------------------------------------- driver
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out_dir', default='/workspace/bigbounce_scan/outputs/cmb_native')
    ap.add_argument('--smica_path',
                    default='/workspace/bigbounce_scan/data/COM_CMB_IQU-smica_2048_R3.00_full.fits')
    ap.add_argument('--skip_train', action='store_true')
    ap.add_argument('--skip_gate', action='store_true')
    args = ap.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)
    os.makedirs(os.path.dirname(args.smica_path), exist_ok=True)

    if not os.path.exists(args.smica_path):
        download_smica(args.smica_path)

    patches_path, _ = build_patch_bank(args.smica_path, args.out_dir)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'Device: {device}', flush=True)

    model_path = os.path.join(args.out_dir, 'best_cmb_native.pt')
    if not args.skip_train:
        model_path, _ = train(patches_path, args.out_dir, device)

    if not args.skip_gate:
        injection_recovery(model_path, patches_path, args.out_dir, device)

    print('\nCMB_NATIVE_RETRAIN DONE', flush=True)


if __name__ == '__main__':
    main()
