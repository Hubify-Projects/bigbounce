#!/usr/bin/env python3
"""
Phase 8 Experiment: DESI Re-scan with Vision Transformer Architecture
======================================================================
Replace convolutional autoencoder with a Transformer-based anomaly detector
for spectral data. Generate 50K synthetic DESI-like spectra (4000 wavelength
bins). Architecture: patch embedding (patch_size=50, 80 patches), 4-layer
Transformer encoder (dim=128, 4 heads), reconstruction decoder.

Compare reconstruction error distributions between Transformer and baseline
autoencoder. Flag objects anomalous to one but not the other.

Output dir: desi-transformer
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
from sklearn.metrics import roc_auc_score

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
OUTPUT_DIR = "/root/results/desi-transformer"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Hyperparameters
# ---------------------------------------------------------------------------
N_SPECTRA = 50000
N_BINS = 4000
PATCH_SIZE = 50
N_PATCHES = N_BINS // PATCH_SIZE  # 80
D_MODEL = 128
N_HEADS = 4
N_LAYERS = 4
BATCH_SIZE = 256
EPOCHS_TRANSFORMER = 30
EPOCHS_AUTOENCODER = 30
LR = 1e-3
ANOMALY_FRACTION = 0.02
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(f"Device: {DEVICE}")
print(f"N_SPECTRA={N_SPECTRA}, N_BINS={N_BINS}, PATCH_SIZE={PATCH_SIZE}, N_PATCHES={N_PATCHES}")

# ---------------------------------------------------------------------------
# Synthetic DESI spectrum generator
# ---------------------------------------------------------------------------
def generate_desi_spectra(n, n_bins, anomaly_frac=0.02, seed=42):
    """Generate synthetic DESI-like spectra with realistic features."""
    rng = np.random.default_rng(seed)
    wavelengths = np.linspace(3600, 9800, n_bins)  # DESI wavelength range

    spectra = np.zeros((n, n_bins), dtype=np.float32)
    labels = np.zeros(n, dtype=np.int64)  # 0=normal, 1=anomalous

    n_anomalous = int(n * anomaly_frac)

    for i in range(n):
        # Continuum: power-law with random slope
        alpha = rng.uniform(-2.0, 0.5)
        continuum = (wavelengths / 5500.0) ** alpha

        # Add emission lines (random subset)
        n_lines = rng.integers(2, 8)
        for _ in range(n_lines):
            center = rng.uniform(3800, 9500)
            width = rng.uniform(5, 40)
            amplitude = rng.uniform(0.1, 3.0)
            continuum += amplitude * np.exp(-0.5 * ((wavelengths - center) / width) ** 2)

        # Add absorption features
        n_abs = rng.integers(1, 5)
        for _ in range(n_abs):
            center = rng.uniform(3800, 9500)
            width = rng.uniform(10, 60)
            depth = rng.uniform(0.05, 0.5)
            continuum -= depth * np.exp(-0.5 * ((wavelengths - center) / width) ** 2)

        # Noise: Poisson-like + readout
        noise_level = rng.uniform(0.01, 0.08)
        noise = rng.normal(0, noise_level, n_bins)
        spectrum = continuum + noise

        # Inject anomalies
        if i < n_anomalous:
            labels[i] = 1
            anomaly_type = rng.integers(0, 4)
            if anomaly_type == 0:
                # Broad absorption trough (BAL-like)
                center = rng.uniform(4000, 8000)
                width = rng.uniform(200, 800)
                depth = rng.uniform(0.3, 0.9)
                spectrum -= depth * np.exp(-0.5 * ((wavelengths - center) / width) ** 2)
            elif anomaly_type == 1:
                # Unusual emission spike
                center = rng.uniform(4000, 9000)
                width = rng.uniform(2, 8)
                amplitude = rng.uniform(5.0, 20.0)
                spectrum += amplitude * np.exp(-0.5 * ((wavelengths - center) / width) ** 2)
            elif anomaly_type == 2:
                # Flux discontinuity
                break_bin = rng.integers(500, 3500)
                spectrum[break_bin:] *= rng.uniform(0.3, 0.7)
            else:
                # High-frequency periodic artifact
                freq = rng.uniform(0.05, 0.2)
                spectrum += 0.3 * np.sin(2 * np.pi * freq * np.arange(n_bins))

        spectra[i] = spectrum

    # Normalize each spectrum to [0, 1]
    mins = spectra.min(axis=1, keepdims=True)
    maxs = spectra.max(axis=1, keepdims=True)
    ranges = maxs - mins
    ranges[ranges == 0] = 1.0
    spectra = (spectra - mins) / ranges

    return spectra, labels, wavelengths


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
# Transformer Autoencoder
# ---------------------------------------------------------------------------
class PatchEmbedding(nn.Module):
    def __init__(self, patch_size, d_model):
        super().__init__()
        self.proj = nn.Linear(patch_size, d_model)
        self.pos_emb = nn.Parameter(torch.randn(1, N_PATCHES, d_model) * 0.02)

    def forward(self, x):
        # x: (B, N_BINS) -> (B, N_PATCHES, patch_size)
        B = x.size(0)
        x = x.view(B, N_PATCHES, PATCH_SIZE)
        x = self.proj(x)  # (B, N_PATCHES, d_model)
        x = x + self.pos_emb
        return x


class TransformerAutoencoder(nn.Module):
    def __init__(self, n_bins, patch_size, d_model, n_heads, n_layers):
        super().__init__()
        self.patch_embed = PatchEmbedding(patch_size, d_model)

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model, nhead=n_heads, dim_feedforward=d_model * 4,
            dropout=0.1, activation='gelu', batch_first=True
        )
        self.encoder = nn.TransformerEncoder(encoder_layer, num_layers=n_layers)

        # Bottleneck
        self.bottleneck = nn.Sequential(
            nn.Linear(d_model, d_model // 2),
            nn.GELU(),
            nn.Linear(d_model // 2, d_model),
        )

        # Decoder: project patches back to patch_size
        decoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model, nhead=n_heads, dim_feedforward=d_model * 4,
            dropout=0.1, activation='gelu', batch_first=True
        )
        self.decoder = nn.TransformerEncoder(decoder_layer, num_layers=2)
        self.output_proj = nn.Linear(d_model, patch_size)

    def forward(self, x):
        # Encode
        patches = self.patch_embed(x)         # (B, 80, 128)
        encoded = self.encoder(patches)        # (B, 80, 128)
        bottleneck = self.bottleneck(encoded)  # (B, 80, 128)

        # Decode
        decoded = self.decoder(bottleneck)     # (B, 80, 128)
        out = self.output_proj(decoded)        # (B, 80, 50)
        out = out.reshape(x.size(0), -1)       # (B, 4000)
        return out


# ---------------------------------------------------------------------------
# Convolutional Autoencoder (baseline)
# ---------------------------------------------------------------------------
class ConvAutoencoder(nn.Module):
    def __init__(self, n_bins):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Unflatten(1, (1, n_bins)),
            nn.Conv1d(1, 32, kernel_size=7, stride=2, padding=3),
            nn.ReLU(),
            nn.Conv1d(32, 64, kernel_size=5, stride=2, padding=2),
            nn.ReLU(),
            nn.Conv1d(64, 128, kernel_size=5, stride=2, padding=2),
            nn.ReLU(),
            nn.Conv1d(128, 64, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
        )
        # After 4 stride-2 convolutions: 4000 -> 2000 -> 1000 -> 500 -> 250
        self.bottleneck = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64 * 250, 256),
            nn.ReLU(),
            nn.Linear(256, 64 * 250),
            nn.ReLU(),
            nn.Unflatten(1, (64, 250)),
        )
        self.decoder = nn.Sequential(
            nn.ConvTranspose1d(64, 128, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.ReLU(),
            nn.ConvTranspose1d(128, 64, kernel_size=5, stride=2, padding=2, output_padding=1),
            nn.ReLU(),
            nn.ConvTranspose1d(64, 32, kernel_size=5, stride=2, padding=2, output_padding=1),
            nn.ReLU(),
            nn.ConvTranspose1d(32, 1, kernel_size=7, stride=2, padding=3, output_padding=1),
            nn.Sigmoid(),
        )

    def forward(self, x):
        encoded = self.encoder(x)
        bottleneck = self.bottleneck(encoded)
        decoded = self.decoder(bottleneck)
        decoded = decoded.squeeze(1)
        # Ensure output matches input size
        if decoded.size(1) != x.size(1):
            decoded = decoded[:, :x.size(1)]
        return decoded


# ---------------------------------------------------------------------------
# Training loop
# ---------------------------------------------------------------------------
def train_model(model, train_loader, val_loader, epochs, model_name):
    optimizer = torch.optim.AdamW(model.parameters(), lr=LR, weight_decay=1e-5)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs)
    criterion = nn.MSELoss()

    history = {"train_loss": [], "val_loss": []}
    best_val = float("inf")

    for epoch in range(epochs):
        model.train()
        train_losses = []
        for batch, _ in train_loader:
            batch = batch.to(DEVICE)
            recon = model(batch)
            loss = criterion(recon, batch)
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            train_losses.append(loss.item())

        model.eval()
        val_losses = []
        with torch.no_grad():
            for batch, _ in val_loader:
                batch = batch.to(DEVICE)
                recon = model(batch)
                loss = criterion(recon, batch)
                val_losses.append(loss.item())

        train_loss = np.mean(train_losses)
        val_loss = np.mean(val_losses)
        history["train_loss"].append(train_loss)
        history["val_loss"].append(val_loss)
        scheduler.step()

        if val_loss < best_val:
            best_val = val_loss
            try: torch.save(model.state_dict(), os.path.join(OUTPUT_DIR, f"{model_name}_best.pt"))
            except Exception as _e: print(f"[warn] checkpoint save failed: {_e}", flush=True)

        if (epoch + 1) % 5 == 0 or epoch == 0:
            print(f"  [{model_name}] Epoch {epoch+1}/{epochs} | train={train_loss:.6f} val={val_loss:.6f}")

    return history, best_val


# ---------------------------------------------------------------------------
# Compute per-sample reconstruction errors
# ---------------------------------------------------------------------------
def compute_recon_errors(model, loader):
    model.eval()
    errors = []
    labels_all = []
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

    print("\n=== Generating 50K synthetic DESI spectra ===")
    spectra, labels, wavelengths = generate_desi_spectra(N_SPECTRA, N_BINS, ANOMALY_FRACTION)
    print(f"  Spectra shape: {spectra.shape}, Anomalies: {labels.sum()} ({100*labels.mean():.1f}%)")

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
    # Train Transformer autoencoder
    # -----------------------------------------------------------------------
    print("\n=== Training Transformer Autoencoder ===")
    transformer = TransformerAutoencoder(N_BINS, PATCH_SIZE, D_MODEL, N_HEADS, N_LAYERS).to(DEVICE)
    n_params_t = sum(p.numel() for p in transformer.parameters())
    print(f"  Transformer params: {n_params_t:,}")
    hist_t, best_t = train_model(transformer, train_loader, val_loader, EPOCHS_TRANSFORMER, "transformer")

    # -----------------------------------------------------------------------
    # Train Conv autoencoder (baseline)
    # -----------------------------------------------------------------------
    print("\n=== Training Conv Autoencoder (baseline) ===")
    conv_ae = ConvAutoencoder(N_BINS).to(DEVICE)
    n_params_c = sum(p.numel() for p in conv_ae.parameters())
    print(f"  Conv AE params: {n_params_c:,}")
    hist_c, best_c = train_model(conv_ae, train_loader, val_loader, EPOCHS_AUTOENCODER, "conv_ae")

    # -----------------------------------------------------------------------
    # Compute reconstruction errors on full dataset
    # -----------------------------------------------------------------------
    print("\n=== Computing reconstruction errors ===")
    # [patched] skip load — checkpoint save unreliable on this PyTorch 2.4.1 build
    # [patched] skip load — checkpoint save unreliable on this PyTorch 2.4.1 build

    err_t, lab = compute_recon_errors(transformer, full_loader)
    err_c, _ = compute_recon_errors(conv_ae, full_loader)

    # -----------------------------------------------------------------------
    # Anomaly thresholds (95th percentile of normal errors)
    # -----------------------------------------------------------------------
    normal_mask = lab == 0
    thresh_t = np.percentile(err_t[normal_mask], 95)
    thresh_c = np.percentile(err_c[normal_mask], 95)

    anom_t = err_t > thresh_t
    anom_c = err_c > thresh_c

    # Objects flagged by Transformer but NOT Conv AE
    transformer_only = anom_t & ~anom_c
    # Objects flagged by Conv AE but NOT Transformer
    conv_only = ~anom_t & anom_c
    # Both
    both = anom_t & anom_c

    print(f"\n  Transformer threshold (95%ile): {thresh_t:.6f}")
    print(f"  Conv AE threshold (95%ile):     {thresh_c:.6f}")
    print(f"  Transformer-only anomalies:     {transformer_only.sum()}")
    print(f"  Conv-only anomalies:            {conv_only.sum()}")
    print(f"  Both anomalies:                 {both.sum()}")

    # -----------------------------------------------------------------------
    # AUC scores (using injected labels)
    # -----------------------------------------------------------------------
    auc_t = roc_auc_score(lab, err_t)
    auc_c = roc_auc_score(lab, err_c)
    # Combined score: average of normalized errors
    err_t_norm = (err_t - err_t.mean()) / (err_t.std() + 1e-12)
    err_c_norm = (err_c - err_c.mean()) / (err_c.std() + 1e-12)
    err_combined = (err_t_norm + err_c_norm) / 2
    auc_combined = roc_auc_score(lab, err_combined)

    print(f"\n  AUC Transformer: {auc_t:.4f}")
    print(f"  AUC Conv AE:     {auc_c:.4f}")
    print(f"  AUC Combined:    {auc_combined:.4f}")

    # -----------------------------------------------------------------------
    # KS test: are the error distributions different?
    # -----------------------------------------------------------------------
    ks_stat, ks_p = stats.ks_2samp(err_t, err_c)
    print(f"\n  KS test (Transformer vs Conv errors): stat={ks_stat:.4f}, p={ks_p:.2e}")

    # -----------------------------------------------------------------------
    # Error statistics
    # -----------------------------------------------------------------------
    err_stats = {
        "transformer": {
            "mean": float(np.mean(err_t)),
            "std": float(np.std(err_t)),
            "median": float(np.median(err_t)),
            "p95": float(np.percentile(err_t, 95)),
            "p99": float(np.percentile(err_t, 99)),
        },
        "conv_ae": {
            "mean": float(np.mean(err_c)),
            "std": float(np.std(err_c)),
            "median": float(np.median(err_c)),
            "p95": float(np.percentile(err_c, 95)),
            "p99": float(np.percentile(err_c, 99)),
        },
    }

    # -----------------------------------------------------------------------
    # Save top anomalies
    # -----------------------------------------------------------------------
    top_k = 200
    top_t_idx = np.argsort(err_t)[-top_k:][::-1]
    top_c_idx = np.argsort(err_c)[-top_k:][::-1]

    top_anomalies_df = pd.DataFrame({
        "index": np.arange(N_SPECTRA),
        "label": lab,
        "err_transformer": err_t,
        "err_conv_ae": err_c,
        "anom_transformer": anom_t.astype(int),
        "anom_conv_ae": anom_c.astype(int),
        "transformer_only": transformer_only.astype(int),
        "conv_only": conv_only.astype(int),
    })
    try: top_anomalies_df.to_csv(os.path.join(OUTPUT_DIR, "all_reconstruction_errors.csv"), index=False)

    except Exception as _e: print(f"[warn] csv write: {_e}", flush=True)

    # Transformer-only anomalies detail
    t_only_df = top_anomalies_df[top_anomalies_df["transformer_only"] == 1].copy()
    t_only_df = t_only_df.sort_values("err_transformer", ascending=False)
    try: t_only_df.to_csv(os.path.join(OUTPUT_DIR, "transformer_only_anomalies.csv"), index=False)

    except Exception as _e: print(f"[warn] csv write: {_e}", flush=True)

    c_only_df = top_anomalies_df[top_anomalies_df["conv_only"] == 1].copy()
    c_only_df = c_only_df.sort_values("err_conv_ae", ascending=False)
    try: c_only_df.to_csv(os.path.join(OUTPUT_DIR, "conv_only_anomalies.csv"), index=False)

    except Exception as _e: print(f"[warn] csv write: {_e}", flush=True)

    elapsed = time.time() - t0

    # -----------------------------------------------------------------------
    # Summary JSON
    # -----------------------------------------------------------------------
    summary = {
        "experiment": "Phase 8: DESI Transformer Anomaly Detector",
        "n_spectra": N_SPECTRA,
        "n_bins": N_BINS,
        "patch_size": PATCH_SIZE,
        "n_patches": N_PATCHES,
        "d_model": D_MODEL,
        "n_heads": N_HEADS,
        "n_layers": N_LAYERS,
        "anomaly_fraction_injected": ANOMALY_FRACTION,
        "n_anomalies_injected": int(labels.sum()),
        "transformer": {
            "n_params": n_params_t,
            "best_val_loss": best_t,
            "auc": auc_t,
            "n_flagged": int(anom_t.sum()),
            "error_stats": err_stats["transformer"],
            "training_history": hist_t,
        },
        "conv_ae": {
            "n_params": n_params_c,
            "best_val_loss": best_c,
            "auc": auc_c,
            "n_flagged": int(anom_c.sum()),
            "error_stats": err_stats["conv_ae"],
            "training_history": hist_c,
        },
        "comparison": {
            "auc_combined": auc_combined,
            "ks_statistic": ks_stat,
            "ks_pvalue": ks_p,
            "transformer_only_count": int(transformer_only.sum()),
            "conv_only_count": int(conv_only.sum()),
            "both_count": int(both.sum()),
            "threshold_transformer": float(thresh_t),
            "threshold_conv_ae": float(thresh_c),
        },
        "runtime_seconds": elapsed,
        "device": str(DEVICE),
    }

    try:
        with open(os.path.join(OUTPUT_DIR, "summary.json"), "w") as f:
            json.dump(summary, f, indent=2, cls=NumpyEncoder)
    except Exception as _e:
        print(f"[warn] json save failed: {_e}", flush=True)
        print(json.dumps(summary, indent=2, cls=NumpyEncoder))

    print(f"\nResults saved to {OUTPUT_DIR}")
    print(f"Runtime: {elapsed:.1f}s")
    print("COMPLETE")


if __name__ == "__main__":
    main()
