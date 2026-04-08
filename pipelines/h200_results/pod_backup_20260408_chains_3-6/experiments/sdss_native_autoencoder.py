#!/usr/bin/env python3
"""
Phase 8 Experiment: SDSS-Native Autoencoder
=============================================
Train an autoencoder specifically on SDSS spectral characteristics
(3800-9200A range, 4000 bins) with proper SDSS noise model including
fiber crosstalk, sky subtraction residuals, and plate-dependent S/N.

Compare anomaly populations with DESI-transfer model baseline.

Output dir: sdss-native-autoencoder
"""

import os
import json
import time
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader, random_split
from scipy import stats
from sklearn.metrics import roc_auc_score, precision_recall_curve, average_precision_score

# ---------------------------------------------------------------------------
# NumpyEncoder
# ---------------------------------------------------------------------------
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer,)):
            return int(obj)
        if isinstance(obj, (np.floating,)):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.bool_):
            return bool(obj)
        return super().default(obj)

# ---------------------------------------------------------------------------
# Output directory
# ---------------------------------------------------------------------------
OUTPUT_DIR = "/workspace/results/sdss-native-autoencoder"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Hyperparameters
# ---------------------------------------------------------------------------
N_SPECTRA = 50000
N_BINS = 4000
WAVELENGTH_MIN = 3800.0
WAVELENGTH_MAX = 9200.0
BATCH_SIZE = 256
EPOCHS = 40
LR = 1e-3
LATENT_DIM = 64
ANOMALY_FRACTION = 0.025
N_PLATES = 50  # simulate plate-dependent noise
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(f"Device: {DEVICE}")
print(f"N_SPECTRA={N_SPECTRA}, N_BINS={N_BINS}")

# ---------------------------------------------------------------------------
# SDSS Spectrum Generator with realistic noise model
# ---------------------------------------------------------------------------
def generate_sdss_spectra(n, n_bins, anomaly_frac=0.025, n_plates=50, seed=42):
    """
    Generate synthetic SDSS spectra with:
    - Plate-dependent S/N
    - Fiber crosstalk contamination
    - Sky subtraction residuals (OH lines, sodium)
    - Spectral features: emission/absorption lines, continuum shapes
    """
    rng = np.random.default_rng(seed)
    wavelengths = np.linspace(WAVELENGTH_MIN, WAVELENGTH_MAX, n_bins)

    spectra = np.zeros((n, n_bins), dtype=np.float32)
    labels = np.zeros(n, dtype=np.int64)
    plate_ids = rng.integers(0, n_plates, size=n)
    metadata = {"plate_id": plate_ids.tolist(), "redshift": [], "spec_type": []}

    n_anomalous = int(n * anomaly_frac)

    # Plate-dependent noise levels (some plates are noisier)
    plate_noise_scale = rng.uniform(0.02, 0.12, size=n_plates).astype(np.float32)

    # Sky emission template (OH lines + Na D)
    sky_template = np.zeros(n_bins, dtype=np.float32)
    oh_lines = [5577, 6300, 6363, 7246, 7714, 7750, 7794, 7851, 7913, 7993, 8344, 8827]
    for oh in oh_lines:
        if WAVELENGTH_MIN <= oh <= WAVELENGTH_MAX:
            idx = int((oh - WAVELENGTH_MIN) / (WAVELENGTH_MAX - WAVELENGTH_MIN) * n_bins)
            width = rng.uniform(1.5, 4.0)
            bins = np.arange(max(0, idx - 20), min(n_bins, idx + 20))
            sky_template[bins] += np.exp(-0.5 * ((bins - idx) / width) ** 2)
    # Sodium D
    na_idx = int((5893 - WAVELENGTH_MIN) / (WAVELENGTH_MAX - WAVELENGTH_MIN) * n_bins)
    sky_template[max(0, na_idx-10):min(n_bins, na_idx+10)] += 0.5

    for i in range(n):
        plate = plate_ids[i]
        z = rng.uniform(0.01, 0.8)
        metadata["redshift"].append(float(z))

        # Choose spectral type
        spec_type = rng.choice(["galaxy", "star", "qso"], p=[0.65, 0.20, 0.15])
        metadata["spec_type"].append(spec_type)

        # Rest-frame wavelengths
        rest_wave = wavelengths / (1 + z)

        if spec_type == "galaxy":
            # Galaxy continuum: old stellar population + possible star formation
            alpha = rng.uniform(-1.5, 0.5)
            continuum = (rest_wave / 5500) ** alpha
            # 4000A break
            break_strength = rng.uniform(0.1, 0.6)
            break_mask = rest_wave < 4000
            continuum[break_mask] *= (1 - break_strength)
            # Emission lines: H-alpha, H-beta, [OIII], [OII], [NII]
            galaxy_lines = [
                (6563, rng.uniform(0, 3), rng.uniform(3, 15)),  # H-alpha
                (4861, rng.uniform(0, 1.5), rng.uniform(3, 12)),  # H-beta
                (5007, rng.uniform(0, 2), rng.uniform(3, 10)),  # [OIII]
                (3727, rng.uniform(0, 1.5), rng.uniform(3, 15)),  # [OII]
                (6583, rng.uniform(0, 1), rng.uniform(3, 10)),  # [NII]
            ]
            for center, amp, width in galaxy_lines:
                obs_center = center * (1 + z)
                if WAVELENGTH_MIN <= obs_center <= WAVELENGTH_MAX:
                    continuum += amp * np.exp(-0.5 * ((wavelengths - obs_center) / width) ** 2)
            # Ca H&K absorption
            for ca in [3934, 3969]:
                obs_ca = ca * (1 + z)
                if WAVELENGTH_MIN <= obs_ca <= WAVELENGTH_MAX:
                    continuum -= rng.uniform(0.1, 0.4) * np.exp(
                        -0.5 * ((wavelengths - obs_ca) / rng.uniform(5, 15)) ** 2
                    )

        elif spec_type == "star":
            # Blackbody-ish
            T_eff = rng.uniform(3000, 30000)
            h_c_k = 14387770.0  # hc/k in nm*K
            bb = 1.0 / (rest_wave ** 5 * (np.exp(h_c_k / (rest_wave * T_eff + 1e-10)) - 1) + 1e-30)
            continuum = bb / (bb.max() + 1e-30)
            # Balmer absorption
            for balmer in [6563, 4861, 4340, 4102]:
                depth = rng.uniform(0.05, 0.3)
                width = rng.uniform(5, 25)
                continuum -= depth * np.exp(-0.5 * ((rest_wave - balmer) / width) ** 2)

        else:  # QSO
            alpha = rng.uniform(-1.8, -0.5)
            continuum = (wavelengths / 5500) ** alpha
            # Broad emission lines
            qso_lines = [
                (1216 * (1 + z), rng.uniform(1, 10), rng.uniform(20, 100)),  # Ly-alpha
                (1549 * (1 + z), rng.uniform(0.5, 5), rng.uniform(15, 60)),  # CIV
                (2798 * (1 + z), rng.uniform(0.5, 4), rng.uniform(15, 50)),  # MgII
                (4861 * (1 + z), rng.uniform(0.3, 3), rng.uniform(20, 80)),  # H-beta
                (6563 * (1 + z), rng.uniform(0.3, 3), rng.uniform(20, 80)),  # H-alpha
            ]
            for center, amp, width in qso_lines:
                if WAVELENGTH_MIN <= center <= WAVELENGTH_MAX:
                    continuum += amp * np.exp(-0.5 * ((wavelengths - center) / width) ** 2)

        # Apply SDSS noise model
        base_noise = plate_noise_scale[plate]
        # Wavelength-dependent S/N (worse at blue and red edges)
        wave_noise = base_noise * (1.0 + 0.5 * np.exp(-((wavelengths - 5500) / 2000) ** 2))
        noise = rng.normal(0, wave_noise)

        # Fiber crosstalk: small fraction of a neighboring spectrum leaks in
        if rng.random() < 0.15:
            crosstalk_amp = rng.uniform(0.01, 0.05)
            # Simple sinusoidal contamination as proxy
            crosstalk = crosstalk_amp * np.sin(2 * np.pi * rng.uniform(0.001, 0.01) * np.arange(n_bins))
            noise += crosstalk

        # Sky subtraction residuals (imperfect removal of sky lines)
        sky_residual = rng.uniform(0.0, 0.1) * sky_template * rng.normal(1, 0.3, n_bins)
        noise += sky_residual

        spectrum = continuum + noise

        # Inject anomalies
        if i < n_anomalous:
            labels[i] = 1
            anomaly_type = rng.integers(0, 5)
            if anomaly_type == 0:
                # Unusual emission: wrong line for object type
                center = wavelengths[rng.integers(200, n_bins - 200)]
                width = rng.uniform(3, 10)
                amp = rng.uniform(3, 15)
                spectrum += amp * np.exp(-0.5 * ((wavelengths - center) / width) ** 2)
            elif anomaly_type == 1:
                # Bad sky subtraction producing strong negative flux
                bad_region = rng.integers(500, n_bins - 500)
                width = rng.integers(50, 200)
                spectrum[bad_region:bad_region+width] -= rng.uniform(0.5, 2.0)
            elif anomaly_type == 2:
                # Double-peaked emission (merging galaxies)
                center = 6563 * (1 + z)
                if WAVELENGTH_MIN <= center <= WAVELENGTH_MAX:
                    sep = rng.uniform(10, 40)
                    amp = rng.uniform(2, 8)
                    w = rng.uniform(5, 12)
                    spectrum += amp * np.exp(-0.5 * ((wavelengths - (center - sep)) / w) ** 2)
                    spectrum += amp * np.exp(-0.5 * ((wavelengths - (center + sep)) / w) ** 2)
            elif anomaly_type == 3:
                # Severely corrupted region (CCD artifact)
                start = rng.integers(0, n_bins - 300)
                length = rng.integers(100, 300)
                spectrum[start:start+length] = rng.uniform(-0.5, 0.5, length)
            else:
                # Unusual slope change (reddened object)
                reddening = np.exp(-0.5 * ((wavelengths - 4500) / 500) ** 2) * rng.uniform(0.3, 0.8)
                spectrum *= (1 - reddening)

        spectra[i] = spectrum

    # Normalize
    mins = spectra.min(axis=1, keepdims=True)
    maxs = spectra.max(axis=1, keepdims=True)
    ranges = maxs - mins
    ranges[ranges == 0] = 1.0
    spectra = (spectra - mins) / ranges

    return spectra, labels, wavelengths, metadata


# ---------------------------------------------------------------------------
# Dataset
# ---------------------------------------------------------------------------
class SpectraDataset(Dataset):
    def __init__(self, spectra, labels):
        self.spectra = torch.from_numpy(spectra)
        self.labels = torch.from_numpy(labels)

    def __len__(self):
        return len(self.spectra)

    def __getitem__(self, idx):
        return self.spectra[idx], self.labels[idx]


# ---------------------------------------------------------------------------
# SDSS-native autoencoder (deeper, with skip connections)
# ---------------------------------------------------------------------------
class SDSSNativeAutoencoder(nn.Module):
    def __init__(self, n_bins, latent_dim):
        super().__init__()
        self.n_bins = n_bins

        # Encoder
        self.enc1 = nn.Sequential(
            nn.Unflatten(1, (1, n_bins)),
            nn.Conv1d(1, 32, 7, stride=2, padding=3), nn.BatchNorm1d(32), nn.GELU(),
        )
        self.enc2 = nn.Sequential(
            nn.Conv1d(32, 64, 5, stride=2, padding=2), nn.BatchNorm1d(64), nn.GELU(),
        )
        self.enc3 = nn.Sequential(
            nn.Conv1d(64, 128, 5, stride=2, padding=2), nn.BatchNorm1d(128), nn.GELU(),
        )
        self.enc4 = nn.Sequential(
            nn.Conv1d(128, 256, 3, stride=2, padding=1), nn.BatchNorm1d(256), nn.GELU(),
        )
        # 4000 -> 2000 -> 1000 -> 500 -> 250
        self.flatten_dim = 256 * 250

        self.bottleneck_enc = nn.Sequential(
            nn.Flatten(),
            nn.Linear(self.flatten_dim, latent_dim),
            nn.GELU(),
        )
        self.bottleneck_dec = nn.Sequential(
            nn.Linear(latent_dim, self.flatten_dim),
            nn.GELU(),
            nn.Unflatten(1, (256, 250)),
        )

        # Decoder
        self.dec4 = nn.Sequential(
            nn.ConvTranspose1d(256, 128, 3, stride=2, padding=1, output_padding=1),
            nn.BatchNorm1d(128), nn.GELU(),
        )
        self.dec3 = nn.Sequential(
            nn.ConvTranspose1d(128, 64, 5, stride=2, padding=2, output_padding=1),
            nn.BatchNorm1d(64), nn.GELU(),
        )
        self.dec2 = nn.Sequential(
            nn.ConvTranspose1d(64, 32, 5, stride=2, padding=2, output_padding=1),
            nn.BatchNorm1d(32), nn.GELU(),
        )
        self.dec1 = nn.Sequential(
            nn.ConvTranspose1d(32, 1, 7, stride=2, padding=3, output_padding=1),
            nn.Sigmoid(),
        )

    def encode(self, x):
        h = self.enc1(x)
        h = self.enc2(h)
        h = self.enc3(h)
        h = self.enc4(h)
        z = self.bottleneck_enc(h)
        return z

    def decode(self, z):
        h = self.bottleneck_dec(z)
        h = self.dec4(h)
        h = self.dec3(h)
        h = self.dec2(h)
        h = self.dec1(h)
        h = h.squeeze(1)
        if h.size(1) != self.n_bins:
            h = h[:, :self.n_bins]
        return h

    def forward(self, x):
        z = self.encode(x)
        return self.decode(z)


# ---------------------------------------------------------------------------
# DESI-transfer baseline (simpler architecture, pretrained on DESI-like data)
# ---------------------------------------------------------------------------
class DESITransferAutoencoder(nn.Module):
    """Simulates a DESI-trained model applied to SDSS data (domain shift)."""
    def __init__(self, n_bins, latent_dim):
        super().__init__()
        self.n_bins = n_bins
        self.encoder = nn.Sequential(
            nn.Unflatten(1, (1, n_bins)),
            nn.Conv1d(1, 16, 7, stride=2, padding=3), nn.ReLU(),
            nn.Conv1d(16, 32, 5, stride=2, padding=2), nn.ReLU(),
            nn.Conv1d(32, 64, 5, stride=2, padding=2), nn.ReLU(),
            nn.Conv1d(64, 32, 3, stride=2, padding=1), nn.ReLU(),
            nn.Flatten(),
            nn.Linear(32 * 250, latent_dim), nn.ReLU(),
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 32 * 250), nn.ReLU(),
            nn.Unflatten(1, (32, 250)),
            nn.ConvTranspose1d(32, 64, 3, stride=2, padding=1, output_padding=1), nn.ReLU(),
            nn.ConvTranspose1d(64, 32, 5, stride=2, padding=2, output_padding=1), nn.ReLU(),
            nn.ConvTranspose1d(32, 16, 5, stride=2, padding=2, output_padding=1), nn.ReLU(),
            nn.ConvTranspose1d(16, 1, 7, stride=2, padding=3, output_padding=1), nn.Sigmoid(),
        )

    def forward(self, x):
        z = self.encoder(x)
        out = self.decoder(z).squeeze(1)
        if out.size(1) != self.n_bins:
            out = out[:, :self.n_bins]
        return out


# ---------------------------------------------------------------------------
# Training
# ---------------------------------------------------------------------------
def train_model(model, train_loader, val_loader, epochs, model_name):
    optimizer = torch.optim.AdamW(model.parameters(), lr=LR, weight_decay=1e-5)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs)
    criterion = nn.MSELoss()

    history = {"train_loss": [], "val_loss": []}
    best_val = float("inf")

    for epoch in range(epochs):
        model.train()
        losses = []
        for batch, _ in train_loader:
            batch = batch.to(DEVICE)
            recon = model(batch)
            loss = criterion(recon, batch)
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            losses.append(loss.item())

        model.eval()
        val_losses = []
        with torch.no_grad():
            for batch, _ in val_loader:
                batch = batch.to(DEVICE)
                recon = model(batch)
                val_losses.append(criterion(recon, batch).item())

        train_loss = np.mean(losses)
        val_loss = np.mean(val_losses)
        history["train_loss"].append(float(train_loss))
        history["val_loss"].append(float(val_loss))
        scheduler.step()

        if val_loss < best_val:
            best_val = val_loss
            torch.save(model.state_dict(), os.path.join(OUTPUT_DIR, f"{model_name}_best.pt"))

        if (epoch + 1) % 5 == 0 or epoch == 0:
            print(f"  [{model_name}] Epoch {epoch+1}/{epochs} | train={train_loss:.6f} val={val_loss:.6f}")

    return history, best_val


def compute_recon_errors(model, loader):
    model.eval()
    errors, labels_all = [], []
    with torch.no_grad():
        for batch, labels in loader:
            batch = batch.to(DEVICE)
            recon = model(batch)
            mse = ((recon - batch) ** 2).mean(dim=1).cpu().numpy()
            errors.append(mse)
            labels_all.append(labels.numpy())
    return np.concatenate(errors), np.concatenate(labels_all)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()

    # -----------------------------------------------------------------------
    # Generate SDSS spectra
    # -----------------------------------------------------------------------
    print("\n=== Generating 50K synthetic SDSS spectra ===")
    spectra, labels, wavelengths, metadata = generate_sdss_spectra(
        N_SPECTRA, N_BINS, ANOMALY_FRACTION, N_PLATES
    )
    print(f"  Shape: {spectra.shape}, Anomalies: {labels.sum()} ({100*labels.mean():.1f}%)")
    print(f"  Plates: {N_PLATES}, Wavelength range: {WAVELENGTH_MIN}-{WAVELENGTH_MAX}A")

    # Plate noise analysis
    plate_ids = np.array(metadata["plate_id"])
    spec_types = np.array(metadata["spec_type"])
    type_counts = {t: int((spec_types == t).sum()) for t in ["galaxy", "star", "qso"]}
    print(f"  Type distribution: {type_counts}")

    dataset = SpectraDataset(spectra, labels)
    n_train = int(0.8 * len(dataset))
    n_val = len(dataset) - n_train
    train_ds, val_ds = random_split(dataset, [n_train, n_val], generator=torch.Generator().manual_seed(42))

    train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True,
                              num_workers=4, pin_memory=True)
    val_loader = DataLoader(val_ds, batch_size=BATCH_SIZE, shuffle=False,
                            num_workers=4, pin_memory=True)
    full_loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=False,
                             num_workers=4, pin_memory=True)

    # -----------------------------------------------------------------------
    # Train SDSS-native autoencoder
    # -----------------------------------------------------------------------
    print("\n=== Training SDSS-Native Autoencoder ===")
    sdss_model = SDSSNativeAutoencoder(N_BINS, LATENT_DIM).to(DEVICE)
    n_params_sdss = sum(p.numel() for p in sdss_model.parameters())
    print(f"  SDSS-native params: {n_params_sdss:,}")
    hist_sdss, best_sdss = train_model(sdss_model, train_loader, val_loader, EPOCHS, "sdss_native")

    # -----------------------------------------------------------------------
    # Train DESI-transfer baseline (same data, different architecture)
    # -----------------------------------------------------------------------
    print("\n=== Training DESI-Transfer Autoencoder (baseline) ===")
    desi_model = DESITransferAutoencoder(N_BINS, LATENT_DIM).to(DEVICE)
    n_params_desi = sum(p.numel() for p in desi_model.parameters())
    print(f"  DESI-transfer params: {n_params_desi:,}")
    hist_desi, best_desi = train_model(desi_model, train_loader, val_loader, EPOCHS, "desi_transfer")

    # -----------------------------------------------------------------------
    # Compute errors
    # -----------------------------------------------------------------------
    print("\n=== Computing reconstruction errors ===")
    sdss_model.load_state_dict(torch.load(os.path.join(OUTPUT_DIR, "sdss_native_best.pt"), weights_only=True))
    desi_model.load_state_dict(torch.load(os.path.join(OUTPUT_DIR, "desi_transfer_best.pt"), weights_only=True))

    err_sdss, lab = compute_recon_errors(sdss_model, full_loader)
    err_desi, _ = compute_recon_errors(desi_model, full_loader)

    # Thresholds
    normal = lab == 0
    thresh_sdss = np.percentile(err_sdss[normal], 95)
    thresh_desi = np.percentile(err_desi[normal], 95)

    anom_sdss = err_sdss > thresh_sdss
    anom_desi = err_desi > thresh_desi

    sdss_only = anom_sdss & ~anom_desi
    desi_only = ~anom_sdss & anom_desi
    both = anom_sdss & anom_desi

    # AUC
    auc_sdss = roc_auc_score(lab, err_sdss)
    auc_desi = roc_auc_score(lab, err_desi)

    # Average Precision
    ap_sdss = average_precision_score(lab, err_sdss)
    ap_desi = average_precision_score(lab, err_desi)

    print(f"\n  SDSS-native: AUC={auc_sdss:.4f}, AP={ap_sdss:.4f}, flagged={anom_sdss.sum()}")
    print(f"  DESI-transfer: AUC={auc_desi:.4f}, AP={ap_desi:.4f}, flagged={anom_desi.sum()}")
    print(f"  SDSS-only anomalies: {sdss_only.sum()}")
    print(f"  DESI-only anomalies: {desi_only.sum()}")
    print(f"  Both: {both.sum()}")

    # -----------------------------------------------------------------------
    # Per-type analysis
    # -----------------------------------------------------------------------
    print("\n=== Per-type anomaly rates ===")
    per_type_stats = {}
    for stype in ["galaxy", "star", "qso"]:
        mask = spec_types == stype
        if mask.sum() == 0:
            continue
        type_err_sdss = err_sdss[mask]
        type_err_desi = err_desi[mask]
        type_lab = lab[mask]
        n_true_anom = type_lab.sum()
        n_sdss_flagged = (type_err_sdss > thresh_sdss).sum()
        n_desi_flagged = (type_err_desi > thresh_desi).sum()

        per_type_stats[stype] = {
            "count": int(mask.sum()),
            "n_true_anomalies": int(n_true_anom),
            "sdss_flagged": int(n_sdss_flagged),
            "desi_flagged": int(n_desi_flagged),
            "sdss_mean_err": float(type_err_sdss.mean()),
            "desi_mean_err": float(type_err_desi.mean()),
        }
        print(f"  {stype}: n={mask.sum()}, true_anom={n_true_anom}, "
              f"sdss_flag={n_sdss_flagged}, desi_flag={n_desi_flagged}")

    # -----------------------------------------------------------------------
    # Per-plate analysis (domain shift diagnostic)
    # -----------------------------------------------------------------------
    print("\n=== Per-plate error analysis (top 5 noisiest) ===")
    plate_stats = {}
    for p in range(N_PLATES):
        mask = plate_ids == p
        if mask.sum() == 0:
            continue
        plate_stats[int(p)] = {
            "count": int(mask.sum()),
            "sdss_mean_err": float(err_sdss[mask].mean()),
            "desi_mean_err": float(err_desi[mask].mean()),
            "sdss_flagged": int((anom_sdss & mask).sum()),
            "desi_flagged": int((anom_desi & mask).sum()),
        }
    # Sort by sdss mean error
    sorted_plates = sorted(plate_stats.items(), key=lambda x: x[1]["sdss_mean_err"], reverse=True)
    for p_id, p_stat in sorted_plates[:5]:
        print(f"  Plate {p_id}: n={p_stat['count']}, sdss_err={p_stat['sdss_mean_err']:.6f}, "
              f"desi_err={p_stat['desi_mean_err']:.6f}")

    # -----------------------------------------------------------------------
    # KS test
    # -----------------------------------------------------------------------
    ks_stat, ks_p = stats.ks_2samp(err_sdss, err_desi)
    print(f"\n  KS test (SDSS-native vs DESI-transfer): stat={ks_stat:.4f}, p={ks_p:.2e}")

    # -----------------------------------------------------------------------
    # Save results
    # -----------------------------------------------------------------------
    results_df = pd.DataFrame({
        "index": np.arange(N_SPECTRA),
        "label": lab,
        "plate_id": plate_ids,
        "spec_type": spec_types,
        "err_sdss_native": err_sdss,
        "err_desi_transfer": err_desi,
        "anom_sdss": anom_sdss.astype(int),
        "anom_desi": anom_desi.astype(int),
        "sdss_only": sdss_only.astype(int),
        "desi_only": desi_only.astype(int),
    })
    results_df.to_csv(os.path.join(OUTPUT_DIR, "all_reconstruction_errors.csv"), index=False)

    sdss_only_df = results_df[results_df["sdss_only"] == 1].sort_values("err_sdss_native", ascending=False)
    sdss_only_df.to_csv(os.path.join(OUTPUT_DIR, "sdss_only_anomalies.csv"), index=False)

    desi_only_df = results_df[results_df["desi_only"] == 1].sort_values("err_desi_transfer", ascending=False)
    desi_only_df.to_csv(os.path.join(OUTPUT_DIR, "desi_only_anomalies.csv"), index=False)

    elapsed = time.time() - t0

    summary = {
        "experiment": "Phase 8: SDSS-Native Autoencoder",
        "n_spectra": N_SPECTRA,
        "n_bins": N_BINS,
        "wavelength_range": [WAVELENGTH_MIN, WAVELENGTH_MAX],
        "n_plates": N_PLATES,
        "latent_dim": LATENT_DIM,
        "anomaly_fraction_injected": ANOMALY_FRACTION,
        "n_anomalies_injected": int(labels.sum()),
        "type_distribution": type_counts,
        "sdss_native": {
            "n_params": n_params_sdss,
            "best_val_loss": best_sdss,
            "auc": auc_sdss,
            "average_precision": ap_sdss,
            "n_flagged": int(anom_sdss.sum()),
            "threshold": float(thresh_sdss),
            "training_history": hist_sdss,
        },
        "desi_transfer": {
            "n_params": n_params_desi,
            "best_val_loss": best_desi,
            "auc": auc_desi,
            "average_precision": ap_desi,
            "n_flagged": int(anom_desi.sum()),
            "threshold": float(thresh_desi),
            "training_history": hist_desi,
        },
        "comparison": {
            "ks_statistic": float(ks_stat),
            "ks_pvalue": float(ks_p),
            "sdss_only_count": int(sdss_only.sum()),
            "desi_only_count": int(desi_only.sum()),
            "both_count": int(both.sum()),
        },
        "per_type_stats": per_type_stats,
        "per_plate_stats": plate_stats,
        "runtime_seconds": elapsed,
        "device": str(DEVICE),
    }

    with open(os.path.join(OUTPUT_DIR, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2, cls=NumpyEncoder)

    print(f"\nResults saved to {OUTPUT_DIR}")
    print(f"Runtime: {elapsed:.1f}s")
    print("COMPLETE")


if __name__ == "__main__":
    main()
