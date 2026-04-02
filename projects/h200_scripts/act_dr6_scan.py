#!/usr/bin/env python3
"""
ACT DR6 CMB Anomaly Scan + Cosmic Birefringence Measurement.

Downloads ACT DR6 polarization maps (Q, U Stokes at 150 GHz) from the
LAMBDA archive, cuts the sky into ~1-degree patches, runs autoencoder
anomaly detection on each patch, and computes the cosmic birefringence
angle beta = 0.5 * arctan(2*C_EB / (C_EE - C_BB)).

Science goal: test the bounce prediction beta = 0.27 deg by finding the
EB correlation signal in the patch ensemble.

Estimated runtime: ~8h on H200.
Output: parquet + JSON summary in outputs/
"""

import numpy as np
import torch
import torch.nn as nn
import os
import json
import time
import traceback
import urllib.request
import urllib.error

try:
    import pyarrow as pa
    import pyarrow.parquet as pq
    HAS_PARQUET = True
except ImportError:
    HAS_PARQUET = False
    print("WARNING: no pyarrow — results will be JSON only")

try:
    import healpy as hp
    HAS_HEALPY = True
except ImportError:
    HAS_HEALPY = False
    print("WARNING: no healpy — falling back to flat-sky extraction")

# ─── Model ────────────────────────────────────────────────────────────────────

class BigAE(nn.Module):
    """
    BigAE adapted for CMB patch inputs.
    Input: flattened [Q, U] patch pair  →  n_in pixels
    Latent: 128-dim bottleneck
    """
    def __init__(self, n_in=496, n_lat=128):
        super().__init__()
        self.enc = nn.Sequential(
            nn.Linear(n_in, 512), nn.BatchNorm1d(512), nn.ReLU(), nn.Dropout(0.15),
            nn.Linear(512, 256), nn.BatchNorm1d(256), nn.ReLU(), nn.Dropout(0.1),
            nn.Linear(256, 128), nn.ReLU(),
            nn.Linear(128, n_lat),
        )
        self.dec = nn.Sequential(
            nn.Linear(n_lat, 128), nn.ReLU(),
            nn.Linear(128, 256), nn.BatchNorm1d(256), nn.ReLU(), nn.Dropout(0.1),
            nn.Linear(256, 512), nn.BatchNorm1d(512), nn.ReLU(), nn.Dropout(0.15),
            nn.Linear(512, n_in),
        )

    def forward(self, x):
        return self.dec(self.enc(x))

    def encode(self, x):
        return self.enc(x)


# ─── Constants ────────────────────────────────────────────────────────────────

SCRIPT_DIR   = os.path.dirname(os.path.abspath(__file__))
OUT_DIR      = os.path.join(SCRIPT_DIR, 'outputs', 'act_dr6')
TEMP_DIR     = os.path.join(SCRIPT_DIR, 'temp', 'act_dr6')

# ACT DR6 map URLs — publicly released on LAMBDA (NASA)
# Full-mission coadd at 150 GHz, f090/f150 IQU maps
# https://lambda.gsfc.nasa.gov/product/act/actpol_dr6_lensing_maps_get.html
# We download the DR6 lensing + polarization products:
ACT_BASE = "https://lambda.gsfc.nasa.gov/data/suborbital/ACT/ACT_dr6/"
MAP_FILES = [
    # Primary: DR6 150 GHz IQU map (FITS, Healpix Nside=2048)
    "maps/act_dr6_pa5_f150_night_set0_iqu_map_srcfree.fits",
    "maps/act_dr6_pa5_f150_night_set1_iqu_map_srcfree.fits",
    # Mask
    "masks/act_dr6_pa5_f150_night_mask.fits",
]

# Fallback: smaller test maps released separately
FALLBACK_URLS = [
    "https://lambda.gsfc.nasa.gov/data/suborbital/ACT/ACT_dr6/maps/"
    "act_dr6_pa5_f150_night_set0_iqu_map_srcfree.fits",
]

# Patch parameters
PATCH_SIZE_DEG = 1.0       # degrees per side
NSIDE_WORK     = 512       # Healpix resolution for patch extraction
N_PIX_PER_SIDE = 16        # pixels per patch side at Nside=512 (1 deg / ~0.115 deg/pix ≈ 8 pix — round up to 16)
N_PIX_PATCH    = N_PIX_PER_SIDE * N_PIX_PER_SIDE   # 256 pixels per Q map
N_IN           = N_PIX_PATCH * 2                    # 512 = Q + U concatenated
ANOMALY_THRESH = 5.0       # MSE threshold for anomaly flag

BATCH_SIZE     = 1024
MAX_PATCHES    = 500_000   # safety cap

# ─── Download helpers ─────────────────────────────────────────────────────────

def download_with_retry(url, dest, n_retries=5, timeout=120):
    if os.path.exists(dest) and os.path.getsize(dest) > 10_000:
        return True
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    for attempt in range(n_retries):
        try:
            print(f"  Downloading {os.path.basename(dest)} (attempt {attempt+1}/{n_retries})...")
            urllib.request.urlretrieve(url, dest)
            if os.path.getsize(dest) > 10_000:
                print(f"  Done: {os.path.getsize(dest)/1e6:.1f} MB")
                return True
            else:
                print(f"  File suspiciously small ({os.path.getsize(dest)} bytes), retrying...")
                os.remove(dest)
        except (urllib.error.URLError, Exception) as e:
            print(f"  Attempt {attempt+1} failed: {e}")
            if attempt < n_retries - 1:
                time.sleep(10 * (attempt + 1))
    return False


def fetch_act_maps():
    """Try to download ACT DR6 maps; fall back to smaller test datasets."""
    downloaded = []
    for relpath in MAP_FILES:
        url  = ACT_BASE + relpath
        dest = os.path.join(TEMP_DIR, os.path.basename(relpath))
        ok   = download_with_retry(url, dest)
        if ok:
            downloaded.append(dest)
        else:
            print(f"  WARN: could not download {relpath}")

    if not downloaded:
        # Try direct LAMBDA fallback URL
        print("  Primary downloads failed — trying fallback LAMBDA URL...")
        for url in FALLBACK_URLS:
            dest = os.path.join(TEMP_DIR, os.path.basename(url))
            if download_with_retry(url, dest):
                downloaded.append(dest)
                break

    return downloaded


# ─── Patch extraction ─────────────────────────────────────────────────────────

def extract_patches_healpy(q_map, u_map, mask=None, nside=NSIDE_WORK):
    """
    Divide the sphere into ~1-deg patches using Healpix pixels.
    Returns array of shape (N_patches, N_IN) = [Q_flat | U_flat].
    Each patch: N_PIX_PATCH contiguous Healpix neighbors.
    """
    import healpy as hp

    npix = hp.nside2npix(nside)
    # Degraded grid: use Nside=16 to define patch centres (~3.7 deg resolution)
    # Then extract Nside=512 pixels inside each low-res pixel
    nside_centres = 16   # ~220 patch centres
    npix_centres  = hp.nside2npix(nside_centres)

    patches_Q = []
    patches_U = []
    patch_meta = []   # (ra, dec, centre_pixel)

    for cpix in range(npix_centres):
        # Find all Nside=512 pixels inside this Nside=16 pixel
        sub_pixels = hp.nest2ring(nside,
                      hp.ring2nest(nside_centres, cpix) * (nside // nside_centres)**2
                      + np.arange((nside // nside_centres)**2))
        # Keep only unmasked pixels
        if mask is not None:
            valid = mask[sub_pixels] > 0.5
            sub_pixels = sub_pixels[valid]

        if len(sub_pixels) < N_PIX_PATCH // 2:
            continue

        # Sample or pad to exactly N_PIX_PATCH
        if len(sub_pixels) >= N_PIX_PATCH:
            idx = np.random.choice(len(sub_pixels), N_PIX_PATCH, replace=False)
            pix_sel = sub_pixels[idx]
        else:
            idx = np.random.choice(len(sub_pixels), N_PIX_PATCH, replace=True)
            pix_sel = sub_pixels[idx]

        q_patch = q_map[pix_sel].astype(np.float32)
        u_patch = u_map[pix_sel].astype(np.float32)

        # Skip if mostly zero / masked
        if np.sum(np.isfinite(q_patch) & (q_patch != 0)) < N_PIX_PATCH // 4:
            continue

        # Replace NaN/inf
        q_patch = np.where(np.isfinite(q_patch), q_patch, 0.0)
        u_patch = np.where(np.isfinite(u_patch), u_patch, 0.0)

        # Normalize by patch RMS
        rms = np.sqrt(np.mean(q_patch**2 + u_patch**2)) + 1e-12
        q_patch /= rms
        u_patch /= rms

        patches_Q.append(q_patch)
        patches_U.append(u_patch)

        theta, phi = hp.pix2ang(nside_centres, cpix)
        ra  = np.degrees(phi)
        dec = 90.0 - np.degrees(theta)
        patch_meta.append({'patch_id': int(cpix), 'ra': float(ra), 'dec': float(dec)})

    if not patches_Q:
        return np.zeros((0, N_IN), dtype=np.float32), []

    Q_arr = np.stack(patches_Q, axis=0)     # (N, 256)
    U_arr = np.stack(patches_U, axis=0)     # (N, 256)
    X     = np.concatenate([Q_arr, U_arr], axis=1)   # (N, 512)
    return X, patch_meta


def extract_patches_flat(q_map_2d, u_map_2d, header=None):
    """
    Flat-sky patch extractor for rectangular FITS maps.
    Cuts the map into non-overlapping N_PIX_PER_SIDE x N_PIX_PER_SIDE tiles.
    """
    h, w = q_map_2d.shape
    patches_Q = []
    patches_U = []
    patch_meta = []
    pid = 0

    for row in range(0, h - N_PIX_PER_SIDE + 1, N_PIX_PER_SIDE):
        for col in range(0, w - N_PIX_PER_SIDE + 1, N_PIX_PER_SIDE):
            q_patch = q_map_2d[row:row+N_PIX_PER_SIDE, col:col+N_PIX_PER_SIDE].astype(np.float32).ravel()
            u_patch = u_map_2d[row:row+N_PIX_PER_SIDE, col:col+N_PIX_PER_SIDE].astype(np.float32).ravel()

            if np.sum(np.isfinite(q_patch) & (q_patch != 0)) < N_PIX_PATCH // 4:
                pid += 1
                continue

            q_patch = np.where(np.isfinite(q_patch), q_patch, 0.0)
            u_patch = np.where(np.isfinite(u_patch), u_patch, 0.0)
            rms = np.sqrt(np.mean(q_patch**2 + u_patch**2)) + 1e-12
            q_patch /= rms
            u_patch /= rms

            patches_Q.append(q_patch)
            patches_U.append(u_patch)

            # Approximate sky coords from pixel position
            ra_approx  = col / w * 360.0
            dec_approx = 90.0 - row / h * 180.0
            patch_meta.append({'patch_id': pid, 'ra': float(ra_approx), 'dec': float(dec_approx)})
            pid += 1

    if not patches_Q:
        return np.zeros((0, N_IN), dtype=np.float32), []

    Q_arr = np.stack(patches_Q, axis=0)
    U_arr = np.stack(patches_U, axis=0)
    X     = np.concatenate([Q_arr, U_arr], axis=1)
    return X, patch_meta


# ─── Birefringence computation ─────────────────────────────────────────────────

def compute_birefringence_beta(q_patches, u_patches):
    """
    Estimate the cosmic birefringence angle beta from an ensemble of
    flat-sky [Q, U] patches using the pseudo-Cl estimator:

        beta = 0.5 * arctan(2 * C_EB / (C_EE - C_BB))

    where E and B modes are computed from Q, U via:
        E =  Q * cos(2*phi) + U * sin(2*phi)
        B = -Q * sin(2*phi) + U * cos(2*phi)

    For a flat patch we use the orientation angle of the patch center
    as a proxy for phi (standard flat-sky approximation).

    Returns beta in degrees.
    """
    N = q_patches.shape[0]
    if N < 10:
        return None

    # Build E and B from ensemble, using random phi orientation per patch
    # (realistic for all-sky ensemble average)
    rng = np.random.default_rng(42)
    phi = rng.uniform(0, np.pi, N)

    E_maps = ( q_patches * np.cos(2*phi)[:, None] + u_patches * np.sin(2*phi)[:, None])
    B_maps = (-q_patches * np.sin(2*phi)[:, None] + u_patches * np.cos(2*phi)[:, None])

    # Pseudo-Cl (mean power across patches)
    C_EE = float(np.mean(E_maps**2))
    C_BB = float(np.mean(B_maps**2))
    C_EB = float(np.mean(E_maps * B_maps))

    denom = C_EE - C_BB
    if abs(denom) < 1e-30:
        return None

    beta_rad = 0.5 * np.arctan2(2.0 * C_EB, denom)
    beta_deg = np.degrees(beta_rad)
    return beta_deg, C_EE, C_BB, C_EB


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    os.makedirs(OUT_DIR,  exist_ok=True)
    os.makedirs(TEMP_DIR, exist_ok=True)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print('='*60)
    print('ACT DR6 CMB ANOMALY SCAN + BIREFRINGENCE MEASUREMENT')
    print(f'Device: {device}')
    print('='*60)

    # ── Load or init model ──────────────────────────────────────────────────
    # CMB patch autoencoder: n_in=512 (256 Q + 256 U pixels)
    model = BigAE(n_in=N_IN, n_lat=128).to(device)

    # Try to load pretrained weights; train from scratch on the data if absent
    model_path = os.path.join(SCRIPT_DIR, 'best_model_47k.pt')
    if os.path.exists(model_path):
        try:
            # Pretrained model has n_in=496; CMB model has n_in=512 — load only shared layers
            state = torch.load(model_path, map_location=device, weights_only=True)
            missing, unexpected = model.load_state_dict(state, strict=False)
            print(f'Loaded pretrained weights (missing: {len(missing)}, unexpected: {len(unexpected)})')
        except Exception as e:
            print(f'Could not load pretrained weights ({e}) — training from scratch')
    else:
        print('No pretrained model found — will train on ACT data (unsupervised)')

    # ── Checkpoint ──────────────────────────────────────────────────────────
    ckpt_path = os.path.join(OUT_DIR, 'checkpoint.json')
    if os.path.exists(ckpt_path):
        with open(ckpt_path) as f:
            ckpt = json.load(f)
        total_scored   = ckpt.get('total_scored', 0)
        total_anomalies= ckpt.get('total_anomalies', 0)
        batch_idx      = ckpt.get('batch_idx', 0)
        done_files     = set(ckpt.get('done_files', []))
        print(f'Resuming from checkpoint: {total_scored:,} scored, {total_anomalies:,} anomalies')
    else:
        total_scored = total_anomalies = batch_idx = 0
        done_files   = set()

    # ── Download maps ───────────────────────────────────────────────────────
    print('Downloading ACT DR6 maps...')
    map_files = fetch_act_maps()
    if not map_files:
        print('FATAL: No ACT DR6 maps could be downloaded.')
        print('Please download manually from:')
        print('  https://lambda.gsfc.nasa.gov/product/act/actpol_dr6_lensing_maps_get.html')
        print('and place FITS files in:', TEMP_DIR)
        # Check for any manually placed FITS files
        import glob as glob_mod
        map_files = glob_mod.glob(os.path.join(TEMP_DIR, '*.fits'))
        if not map_files:
            print('No FITS files found in temp dir either. Exiting.')
            return

    print(f'Processing {len(map_files)} map file(s)...')

    row_buffer = []
    all_q_patches = []
    all_u_patches = []
    t0 = time.time()

    from astropy.io import fits as pyfits

    for map_file in map_files:
        if os.path.basename(map_file) in done_files:
            print(f'  Skipping (already done): {os.path.basename(map_file)}')
            continue

        print(f'  Processing: {os.path.basename(map_file)}')

        try:
            with pyfits.open(map_file, memmap=True) as hdul:
                # ACT IQU maps: HDU 0=I, HDU 1=Q, HDU 2=U (or all in HDU 0 with shape [3, npix])
                # Try various layouts
                q_map = u_map = mask_map = None

                if hdul[0].data is not None:
                    d = hdul[0].data
                    if d.ndim == 2 and d.shape[0] == 3:
                        # shape (3, npix) — IQU
                        q_map = d[1].astype(np.float32)
                        u_map = d[2].astype(np.float32)
                    elif d.ndim == 1:
                        # Healpix 1-D — check for separate Q/U extensions
                        if len(hdul) >= 3:
                            q_map = hdul[1].data.astype(np.float32).ravel()
                            u_map = hdul[2].data.astype(np.float32).ravel()
                        else:
                            # Single Stokes map (T or I) — skip
                            print('    Only intensity map found — skipping (need Q, U)')
                            continue
                    elif d.ndim == 2:
                        # Rectangular flat-sky (RADec)
                        if len(hdul) >= 3:
                            q_map = hdul[1].data.astype(np.float32)
                            u_map = hdul[2].data.astype(np.float32)
                        else:
                            print('    Flat-sky single map — assuming Q only, skipping')
                            continue

                # Try mask
                for ext in hdul:
                    if 'mask' in ext.name.lower() and ext.data is not None:
                        mask_map = ext.data.astype(np.float32).ravel()
                        break

                if q_map is None or u_map is None:
                    print('    Could not extract Q, U — skipping')
                    continue

                header = hdul[0].header

        except Exception as e:
            print(f'    Error reading {map_file}: {e}')
            traceback.print_exc()
            continue

        # Determine if Healpix or flat-sky
        is_healpix = (q_map.ndim == 1) and HAS_HEALPY

        if is_healpix:
            # Downgrade to working Nside if needed
            nside_orig = hp.npix2nside(len(q_map))
            if nside_orig > NSIDE_WORK:
                print(f'    Degrading Healpix from Nside={nside_orig} to Nside={NSIDE_WORK}...')
                q_map    = hp.ud_grade(q_map, NSIDE_WORK)
                u_map    = hp.ud_grade(u_map, NSIDE_WORK)
                if mask_map is not None and len(mask_map) == hp.nside2npix(nside_orig):
                    mask_map = hp.ud_grade(mask_map, NSIDE_WORK)

            print(f'    Extracting Healpix patches (Nside={NSIDE_WORK})...')
            X, patch_meta = extract_patches_healpy(q_map, u_map, mask=mask_map, nside=NSIDE_WORK)
        else:
            if q_map.ndim == 1:
                # Try to reshape square
                side = int(np.sqrt(len(q_map)))
                q_map = q_map[:side*side].reshape(side, side)
                u_map = u_map[:side*side].reshape(side, side)

            print(f'    Extracting flat-sky patches ({q_map.shape})...')
            X, patch_meta = extract_patches_flat(q_map, u_map, header=header)

        if X.shape[0] == 0:
            print('    No valid patches extracted — skipping')
            continue

        print(f'    Extracted {X.shape[0]:,} patches of shape {X.shape[1]}')

        # Accumulate Q, U separately for birefringence computation
        mid = X.shape[1] // 2
        all_q_patches.append(X[:, :mid])
        all_u_patches.append(X[:, mid:])

        # ── Train autoencoder on this data if no pretrained weights ─────────
        if not os.path.exists(model_path):
            print('    Training autoencoder on patches...')
            model.train()
            optimizer = torch.optim.Adam(model.parameters(), lr=1e-3, weight_decay=1e-5)
            n_train   = min(X.shape[0], 50_000)
            X_train   = torch.tensor(X[:n_train]).to(device)
            for epoch in range(20):
                perm    = torch.randperm(n_train)
                ep_loss = 0.0
                for bi in range(0, n_train, BATCH_SIZE):
                    xb = X_train[perm[bi:bi+BATCH_SIZE]]
                    optimizer.zero_grad()
                    loss = nn.functional.mse_loss(model(xb), xb)
                    loss.backward()
                    optimizer.step()
                    ep_loss += loss.item()
                if (epoch + 1) % 5 == 0:
                    print(f'      Epoch {epoch+1}/20, loss={ep_loss:.4f}')
            model.eval()

        # ── Inference ────────────────────────────────────────────────────────
        model.eval()
        dataset   = torch.utils.data.TensorDataset(torch.tensor(X))
        loader    = torch.utils.data.DataLoader(
            dataset,
            batch_size  = BATCH_SIZE,
            num_workers = 16,
            pin_memory  = True,
            prefetch_factor = 4,
        )

        scores_list  = []
        latents_list = []

        with torch.no_grad():
            for bi, (xb,) in enumerate(loader):
                xb    = xb.to(device, non_blocking=True)
                recon = model(xb)
                lat   = model.encode(xb)
                mse   = ((xb - recon)**2).mean(dim=1)
                scores_list.append(mse.cpu().numpy())
                latents_list.append(lat.cpu().numpy())

                if (bi + 1) % 50 == 0:
                    elapsed = time.time() - t0
                    done_b  = (bi + 1) * BATCH_SIZE
                    rate    = done_b / elapsed
                    print(f'    Batch {bi+1}: {done_b:,} patches @ {rate:.0f}/s')

        scores  = np.concatenate(scores_list, axis=0)
        latents = np.concatenate(latents_list, axis=0)

        # Build row buffer
        thresh_99 = float(np.percentile(scores, 99))
        for ki, meta in enumerate(patch_meta):
            if ki >= len(scores):
                break
            row = {
                'patch_id'     : int(meta['patch_id']),
                'ra'           : float(meta['ra']),
                'dec'          : float(meta['dec']),
                'anomaly_score': float(scores[ki]),
                'is_anomaly'   : bool(scores[ki] > ANOMALY_THRESH),
                'map_file'     : os.path.basename(map_file),
            }
            for j in range(128):
                row[f'lat_{j:03d}'] = float(latents[ki, j])
            row_buffer.append(row)

        total_scored    += len(patch_meta)
        total_anomalies += int(np.sum(scores > ANOMALY_THRESH))
        done_files.add(os.path.basename(map_file))

        print(f'    {len(patch_meta):,} patches scored, {int(np.sum(scores > ANOMALY_THRESH)):,} anomalies (threshold={ANOMALY_THRESH})')

        # Flush every 200K rows
        if len(row_buffer) >= 200_000 and HAS_PARQUET:
            table = pa.Table.from_pylist(row_buffer)
            out_path = os.path.join(OUT_DIR, f'act_batch_{batch_idx:04d}.parquet')
            pq.write_table(table, out_path, compression='zstd')
            print(f'  Flushed batch {batch_idx}: {len(row_buffer):,} rows → {out_path}')
            batch_idx  += 1
            row_buffer  = []
            with open(ckpt_path, 'w') as f:
                json.dump({
                    'done_files'    : list(done_files),
                    'total_scored'  : total_scored,
                    'total_anomalies': total_anomalies,
                    'batch_idx'     : batch_idx,
                }, f)

    # ── Final parquet flush ─────────────────────────────────────────────────
    if row_buffer and HAS_PARQUET:
        table    = pa.Table.from_pylist(row_buffer)
        out_path = os.path.join(OUT_DIR, f'act_batch_{batch_idx:04d}.parquet')
        pq.write_table(table, out_path, compression='zstd')
        print(f'Final flush: {len(row_buffer):,} rows → {out_path}')
        batch_idx += 1

    # ── Birefringence angle ─────────────────────────────────────────────────
    beta_result = None
    if all_q_patches:
        Q_all = np.concatenate(all_q_patches, axis=0)
        U_all = np.concatenate(all_u_patches, axis=0)
        print(f'\nComputing birefringence angle from {Q_all.shape[0]:,} patches...')
        bire = compute_birefringence_beta(Q_all, U_all)
        if bire is not None:
            beta_deg, C_EE, C_BB, C_EB = bire
            print(f'  beta = {beta_deg:.4f} deg  (predicted: 0.27 deg)')
            print(f'  C_EE={C_EE:.4e}  C_BB={C_BB:.4e}  C_EB={C_EB:.4e}')
            beta_result = {
                'beta_deg'            : float(beta_deg),
                'C_EE'                : float(C_EE),
                'C_BB'                : float(C_BB),
                'C_EB'                : float(C_EB),
                'predicted_bounce_deg': 0.27,
                'deviation_deg'       : float(abs(beta_deg - 0.27)),
                'n_patches_used'      : int(Q_all.shape[0]),
            }

    # ── Summary JSON ────────────────────────────────────────────────────────
    elapsed = time.time() - t0

    # Top 20 anomalies
    top20 = sorted(row_buffer + [], key=lambda r: r['anomaly_score'], reverse=True)[:20]
    top20_clean = [
        {k: v for k, v in r.items() if not k.startswith('lat_')}
        for r in top20
    ]
    for i, r in enumerate(top20_clean):
        r['rank'] = i + 1

    summary = {
        'timestamp'          : time.strftime('%Y-%m-%d %H:%M:%S'),
        'elapsed_hours'      : round(elapsed / 3600, 3),
        'n_map_files'        : len(done_files),
        'n_patches_scored'   : total_scored,
        'n_anomalies'        : total_anomalies,
        'anomaly_threshold'  : ANOMALY_THRESH,
        'anomaly_fraction'   : round(total_anomalies / max(total_scored, 1), 4),
        'birefringence'      : beta_result,
        'bounce_prediction_deg': 0.27,
        'n_parquet_batches'  : batch_idx,
        'top_20_anomalies'   : top20_clean,
    }

    summary_path = os.path.join(OUT_DIR, 'act_dr6_summary.json')
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f'\nSummary written to: {summary_path}')

    if beta_result:
        print(f'\nBIREFRINGENCE RESULT: beta = {beta_result["beta_deg"]:.4f} deg')
        print(f'  Bounce prediction: 0.27 deg')
        print(f'  Deviation: {beta_result["deviation_deg"]:.4f} deg')

    with open(ckpt_path, 'w') as f:
        json.dump({
            'done_files'    : list(done_files),
            'total_scored'  : total_scored,
            'total_anomalies': total_anomalies,
            'batch_idx'     : batch_idx,
            'status'        : 'COMPLETE',
        }, f)

    print(f'\n{"="*60}')
    print(f'COMPLETE: {total_scored:,} patches, {total_anomalies:,} anomalies, {elapsed/3600:.1f}h')
    print(f'{"="*60}')


if __name__ == '__main__':
    main()
