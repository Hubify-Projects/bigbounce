#!/usr/bin/env python3
"""
Planck CMB Full-Sky Patch Anomaly Detection.
Train autoencoder on CMB temperature patches, find anomalous regions.

Uses Planck 2018 SMICA CMB map (NSIDE=2048, downgraded to 256 for speed).
Extracts patches via disc-query (fast), scores with conv autoencoder on GPU.
"""
import numpy as np, torch, torch.nn as nn, os, json, time, urllib.request
try:
    import healpy as hp
except ImportError:
    print("Installing healpy...")
    os.system("pip install healpy")
    import healpy as hp
try:
    import pyarrow as pa, pyarrow.parquet as pq
    HAS_PARQUET = True
except:
    HAS_PARQUET = False

# Settings
NSIDE = 256  # Downgrade from 2048 — fast extraction, still good resolution
PATCH_SIZE = 64  # 64x64 pixel patches
LATENT_DIM = 32
N_PATCHES = 20000

class CMB_AE(nn.Module):
    """Convolutional autoencoder for CMB patches."""
    def __init__(self, patch_size=64, latent_dim=32):
        super().__init__()
        self.enc = nn.Sequential(
            nn.Conv2d(1, 16, 3, stride=2, padding=1), nn.BatchNorm2d(16), nn.ReLU(),
            nn.Conv2d(16, 32, 3, stride=2, padding=1), nn.BatchNorm2d(32), nn.ReLU(),
            nn.Conv2d(32, 64, 3, stride=2, padding=1), nn.BatchNorm2d(64), nn.ReLU(),
            nn.Conv2d(64, 128, 3, stride=2, padding=1), nn.BatchNorm2d(128), nn.ReLU(),
            nn.Flatten(),
            nn.Linear(128 * (patch_size // 16) ** 2, latent_dim),
        )
        self.dec_fc = nn.Linear(latent_dim, 128 * (patch_size // 16) ** 2)
        self.dec = nn.Sequential(
            nn.ConvTranspose2d(128, 64, 4, stride=2, padding=1), nn.BatchNorm2d(64), nn.ReLU(),
            nn.ConvTranspose2d(64, 32, 4, stride=2, padding=1), nn.BatchNorm2d(32), nn.ReLU(),
            nn.ConvTranspose2d(32, 16, 4, stride=2, padding=1), nn.BatchNorm2d(16), nn.ReLU(),
            nn.ConvTranspose2d(16, 1, 4, stride=2, padding=1),
        )
        self.ps = patch_size // 16

    def encode(self, x):
        return self.enc(x)

    def decode(self, z):
        x = self.dec_fc(z).view(-1, 128, self.ps, self.ps)
        return self.dec(x)

    def forward(self, x):
        return self.decode(self.encode(x))


def download_planck_map(out_dir):
    """Download Planck 2018 SMICA CMB map."""
    fits_path = os.path.join(out_dir, 'COM_CMB_IQU-smica_2048_R3.00_full.fits')
    if os.path.exists(fits_path):
        return fits_path
    url = 'http://pla.esac.esa.int/pla/aio/product-action?MAP.MAP_ID=COM_CMB_IQU-smica_2048_R3.00_full.fits'
    print(f'Downloading Planck SMICA map...')
    print(f'  URL: {url}')
    try:
        urllib.request.urlretrieve(url, fits_path)
        print(f'  Downloaded: {os.path.getsize(fits_path) / 1e6:.1f} MB')
        return fits_path
    except Exception as e:
        print(f'  PLA download failed: {e}')
        url2 = 'https://irsa.ipac.caltech.edu/data/Planck/release_3/all-sky-maps/maps/component-maps/cmb/COM_CMB_IQU-smica_2048_R3.00_full.fits'
        try:
            urllib.request.urlretrieve(url2, fits_path)
            print(f'  Downloaded from IRSA: {os.path.getsize(fits_path) / 1e6:.1f} MB')
            return fits_path
        except Exception as e2:
            print(f'  IRSA download also failed: {e2}')
            return None


def extract_patches(cmb_map, nside, patch_size, n_total):
    """Extract random patches via fast disc-query pixel indexing."""
    patches = []
    positions = []
    npix = hp.nside2npix(nside)
    rot = hp.Rotator(coord=["C", "G"])

    np.random.seed(42)
    chosen = 0
    attempts = 0
    max_attempts = n_total * 5
    n_need = patch_size * patch_size

    # Disc radius to capture enough pixels for a patch_size x patch_size grid
    resol_rad = hp.nside2resol(nside)
    disc_radius = resol_rad * patch_size * 0.6

    while chosen < n_total and attempts < max_attempts:
        pix = np.random.randint(0, npix)
        theta, phi = hp.pix2ang(nside, pix)

        # Galactic plane cut
        gal_result = rot(np.array([theta]), np.array([phi]))
        gal_b = 90.0 - np.degrees(float(gal_result[0]))
        if abs(gal_b) < 20:
            attempts += 1
            continue

        # Get pixels in disc around this position
        vec = hp.ang2vec(theta, phi)
        disc_pix = hp.query_disc(nside, vec, disc_radius)

        if len(disc_pix) < n_need:
            attempts += 1
            continue

        vals = cmb_map[disc_pix[:n_need]]
        if not np.all(np.isfinite(vals)):
            attempts += 1
            continue

        patch = vals.reshape(patch_size, patch_size).astype(np.float32)
        patches.append(patch)
        ra = np.degrees(phi)
        dec = 90.0 - np.degrees(theta)
        positions.append((float(ra), float(dec)))
        chosen += 1
        if chosen % 2000 == 0:
            print(f"  {chosen:,} patches extracted...")
        attempts += 1

    return np.array(patches), positions


def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'Device: {device}')

    out_dir = '/workspace/bigbounce/outputs/planck_cmb'
    os.makedirs(out_dir, exist_ok=True)

    # Download Planck map
    fits_path = download_planck_map(out_dir)
    if fits_path is None:
        print("ERROR: Could not download Planck map")
        return

    # Read and downgrade
    print(f'Reading Planck SMICA map...')
    cmb_map = hp.read_map(fits_path, field=0)
    orig_nside = hp.get_nside(cmb_map)
    if orig_nside != NSIDE:
        print(f'  Downgrading from NSIDE={orig_nside} to {NSIDE}...')
        cmb_map = hp.ud_grade(cmb_map, NSIDE)
    print(f'  Map shape: {cmb_map.shape}, NSIDE={NSIDE}')

    # Convert to uK if needed
    if np.std(cmb_map[cmb_map != hp.UNSEEN]) < 1e-3:
        cmb_map *= 1e6
        print(f'  Converted to uK')

    # Remove monopole and dipole
    cmb_map = hp.remove_monopole(cmb_map)
    cmb_map = hp.remove_dipole(cmb_map)

    # Extract patches
    print(f'\nExtracting {N_PATCHES:,} patches ({PATCH_SIZE}x{PATCH_SIZE})...')
    patches, positions = extract_patches(cmb_map, NSIDE, PATCH_SIZE, N_PATCHES)
    print(f'  Extracted: {len(patches):,} valid patches')

    if len(patches) < 1000:
        print("WARNING: Fewer patches than expected, continuing anyway...")

    # Normalize patches
    for i in range(len(patches)):
        p = patches[i]
        patches[i] = (p - np.mean(p)) / (np.std(p) + 1e-10)

    # Train autoencoder
    model = CMB_AE(PATCH_SIZE, LATENT_DIM).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3, weight_decay=1e-5)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=50)

    n_train = int(0.8 * len(patches))
    idx = np.random.permutation(len(patches))
    train_patches = torch.tensor(patches[idx[:n_train]]).unsqueeze(1).to(device)
    val_patches = torch.tensor(patches[idx[n_train:]]).unsqueeze(1).to(device)

    BATCH = 256
    EPOCHS = 50
    best_val = float('inf')
    patience = 10
    no_improve = 0

    print(f'\nTraining CMB_AE: {PATCH_SIZE}x{PATCH_SIZE} -> {LATENT_DIM}')
    print(f'Train: {n_train:,}, Val: {len(patches) - n_train:,}')

    t0 = time.time()
    for epoch in range(EPOCHS):
        model.train()
        perm = torch.randperm(n_train, device=device)
        epoch_loss = 0
        n_batches = 0
        for i in range(0, n_train, BATCH):
            batch = train_patches[perm[i:i+BATCH]]
            recon = model(batch)
            loss = nn.functional.mse_loss(recon, batch)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
            n_batches += 1
        scheduler.step()

        model.eval()
        with torch.no_grad():
            val_recon = model(val_patches[:2000])
            val_loss = nn.functional.mse_loss(val_recon, val_patches[:2000]).item()

        if (epoch+1) % 5 == 0:
            print(f'  Epoch {epoch+1}: train={epoch_loss/n_batches:.6f}, val={val_loss:.6f}')

        if val_loss < best_val:
            best_val = val_loss
            no_improve = 0
            torch.save(model.state_dict(), os.path.join(out_dir, 'cmb_ae_model.pt'))
        else:
            no_improve += 1
            if no_improve >= patience:
                print(f'  Early stopping at epoch {epoch+1}')
                break

    train_time = time.time() - t0
    print(f'\nTraining done: {train_time:.1f}s, best val: {best_val:.6f}')

    # Score all patches
    model.load_state_dict(torch.load(os.path.join(out_dir, 'cmb_ae_model.pt'), weights_only=True))
    model.eval()

    print('Scoring all patches...')
    all_patches_tensor = torch.tensor(patches).unsqueeze(1).to(device)
    all_scores = []
    all_latents = []

    with torch.no_grad():
        for i in range(0, len(patches), BATCH):
            batch = all_patches_tensor[i:i+BATCH]
            recon = model(batch)
            latent = model.encode(batch)
            scores = torch.mean((batch - recon)**2, dim=(1,2,3))
            all_scores.append(scores.cpu().numpy())
            all_latents.append(latent.cpu().numpy())

    scores = np.concatenate(all_scores)
    latents = np.concatenate(all_latents)

    # Build output
    rows = []
    for i in range(len(patches)):
        rows.append({
            'ra': positions[i][0],
            'dec': positions[i][1],
            'anomaly_score': float(scores[i]),
            'patch_mean': float(np.mean(patches[i])),
            'patch_std': float(np.std(patches[i])),
        })

    if HAS_PARQUET:
        pq.write_table(pa.Table.from_pylist(rows), os.path.join(out_dir, 'planck_cmb_anomalies.parquet'))

    # Summary
    threshold = np.percentile(scores, 99)
    n_anom = int(np.sum(scores > threshold))
    top20_idx = np.argsort(scores)[-20:][::-1]

    summary = {
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'n_patches': len(patches),
        'patch_size': PATCH_SIZE,
        'nside': NSIDE,
        'latent_dim': LATENT_DIM,
        'train_time_s': train_time,
        'best_val_loss': best_val,
        'n_anomalies_top1pct': n_anom,
        'threshold_99pct': float(threshold),
        'top_20': [
            {
                'rank': k+1,
                'ra': positions[int(i)][0],
                'dec': positions[int(i)][1],
                'score': float(scores[int(i)]),
            }
            for k, i in enumerate(top20_idx)
        ]
    }

    with open(os.path.join(out_dir, 'planck_cmb_summary.json'), 'w') as f:
        json.dump(summary, f, indent=2)

    print(f'\nTop 10 anomalous CMB patches:')
    for item in summary['top_20'][:10]:
        print(f"  #{item['rank']}: RA={item['ra']:.2f} DEC={item['dec']:.2f} score={item['score']:.4f}")

    print(f'\n{"="*60}')
    print(f'COMPLETE: {len(patches):,} CMB patches scored, {n_anom} anomalies')
    print(f'{"="*60}')

if __name__ == '__main__':
    main()
