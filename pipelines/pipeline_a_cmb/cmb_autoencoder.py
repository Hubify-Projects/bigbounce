#!/usr/bin/env python3
"""
Pipeline A — CMB Anomaly Hunter: Convolutional Autoencoder
===========================================================

Trains a convolutional autoencoder on 64x64 CMB temperature patches
extracted by extract_patches.py. Anomalous patches are identified by
their high reconstruction error (MSE), indicating features the
autoencoder's compressed representation cannot capture — i.e., patterns
that deviate from the statistical norm of the CMB.

Architecture:
  Encoder: Conv2d(1,16,3,s2,p1) -> BN -> ReLU
           Conv2d(16,32,3,s2,p1) -> BN -> ReLU
           Conv2d(32,64,3,s2,p1) -> BN -> ReLU
           Flatten -> Linear(64*8*8, 128)

  Decoder: Linear(128, 64*8*8) -> Reshape(64,8,8)
           ConvTranspose2d(64,32,3,s2,p1,op1) -> BN -> ReLU
           ConvTranspose2d(32,16,3,s2,p1,op1) -> BN -> ReLU
           ConvTranspose2d(16,1,3,s2,p1,op1)  -> Tanh

  Latent dimension: 128
  Loss: MSE (mean squared error)

Usage:
  python cmb_autoencoder.py --patches outputs/cmb_patches.npy [--epochs 100] [--batch_size 32]

  # Anomaly detection only (from a trained model):
  python cmb_autoencoder.py --patches outputs/cmb_patches.npy --detect_only --model outputs/autoencoder_best.pt
"""

import os
import sys
import argparse
import json
import time
from datetime import datetime
from pathlib import Path

import numpy as np

try:
    import torch
    import torch.nn as nn
    import torch.optim as optim
    from torch.utils.data import Dataset, DataLoader, random_split
except ImportError:
    print("ERROR: PyTorch is required. Install with:")
    print("  pip install torch torchvision")
    print("  (or use a RunPod GPU pod with PyTorch pre-installed)")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Dataset
# ---------------------------------------------------------------------------
class CMBPatchDataset(Dataset):
    """Dataset of normalized CMB patches."""

    def __init__(self, patches_file: str):
        self.patches = np.load(patches_file).astype(np.float32)
        # Shape: (N, H, W) — add channel dimension -> (N, 1, H, W)
        if self.patches.ndim == 3:
            self.patches = self.patches[:, np.newaxis, :, :]
        print(f"  Loaded {len(self.patches)} patches, shape: {self.patches.shape}")

    def __len__(self):
        return len(self.patches)

    def __getitem__(self, idx):
        return torch.from_numpy(self.patches[idx])


# ---------------------------------------------------------------------------
# Model
# ---------------------------------------------------------------------------
class CMBAutoencoder(nn.Module):
    """
    Convolutional autoencoder for 64x64 single-channel CMB patches.

    Encoder compresses 64x64 -> 32x32 -> 16x16 -> 8x8 with increasing
    channel depth, then flattens to a 128-dim latent vector.

    Decoder reverses the process.
    """

    def __init__(self, latent_dim: int = 128):
        super().__init__()
        self.latent_dim = latent_dim

        # Encoder
        self.encoder_conv = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=3, stride=2, padding=1),   # 64 -> 32
            nn.BatchNorm2d(16),
            nn.ReLU(inplace=True),

            nn.Conv2d(16, 32, kernel_size=3, stride=2, padding=1),  # 32 -> 16
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),

            nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1),  # 16 -> 8
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
        )

        self.encoder_fc = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64 * 8 * 8, latent_dim),
        )

        # Decoder
        self.decoder_fc = nn.Sequential(
            nn.Linear(latent_dim, 64 * 8 * 8),
            nn.ReLU(inplace=True),
        )

        self.decoder_conv = nn.Sequential(
            nn.ConvTranspose2d(64, 32, kernel_size=3, stride=2, padding=1, output_padding=1),  # 8 -> 16
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),

            nn.ConvTranspose2d(32, 16, kernel_size=3, stride=2, padding=1, output_padding=1),  # 16 -> 32
            nn.BatchNorm2d(16),
            nn.ReLU(inplace=True),

            nn.ConvTranspose2d(16, 1, kernel_size=3, stride=2, padding=1, output_padding=1),   # 32 -> 64
            nn.Tanh(),  # output in [-1, 1] range (matches normalized patches)
        )

    def encode(self, x):
        h = self.encoder_conv(x)
        z = self.encoder_fc(h)
        return z

    def decode(self, z):
        h = self.decoder_fc(z)
        h = h.view(-1, 64, 8, 8)
        x_recon = self.decoder_conv(h)
        return x_recon

    def forward(self, x):
        z = self.encode(x)
        x_recon = self.decode(z)
        return x_recon, z


# ---------------------------------------------------------------------------
# Training
# ---------------------------------------------------------------------------
def train_autoencoder(
    patches_file: str,
    output_dir: str = "outputs",
    epochs: int = 100,
    batch_size: int = 32,
    lr: float = 1e-3,
    latent_dim: int = 128,
    val_frac: float = 0.15,
    patience: int = 15,
    device: str = "auto",
):
    """Train the autoencoder and save the model + loss curves."""

    print("=" * 70)
    print("PIPELINE A — CMB ANOMALY HUNTER: AUTOENCODER TRAINING")
    print("=" * 70)

    # Device
    if device == "auto":
        if torch.cuda.is_available():
            device = "cuda"
        elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
            device = "mps"
        else:
            device = "cpu"
    print(f"\n  Device: {device}")

    os.makedirs(output_dir, exist_ok=True)

    # ------------------------------------------------------------------
    # 1. Load data
    # ------------------------------------------------------------------
    print(f"\n[1/4] Loading patches from {patches_file}")
    dataset = CMBPatchDataset(patches_file)

    n_val = int(len(dataset) * val_frac)
    n_train = len(dataset) - n_val
    train_set, val_set = random_split(
        dataset, [n_train, n_val],
        generator=torch.Generator().manual_seed(42),
    )
    print(f"  Train: {n_train}, Val: {n_val}")

    train_loader = DataLoader(train_set, batch_size=batch_size, shuffle=True, num_workers=0)
    val_loader = DataLoader(val_set, batch_size=batch_size, shuffle=False, num_workers=0)

    # ------------------------------------------------------------------
    # 2. Build model
    # ------------------------------------------------------------------
    print(f"\n[2/4] Building autoencoder (latent_dim={latent_dim})")
    model = CMBAutoencoder(latent_dim=latent_dim).to(device)

    n_params = sum(p.numel() for p in model.parameters())
    print(f"  Parameters: {n_params:,}")

    optimizer = optim.Adam(model.parameters(), lr=lr)
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(
        optimizer, mode="min", factor=0.5, patience=7, verbose=True
    )
    criterion = nn.MSELoss()

    # ------------------------------------------------------------------
    # 3. Train
    # ------------------------------------------------------------------
    print(f"\n[3/4] Training for up to {epochs} epochs (patience={patience})")
    train_losses = []
    val_losses = []
    best_val_loss = float("inf")
    epochs_no_improve = 0
    best_epoch = 0

    model_path = os.path.join(output_dir, "autoencoder_best.pt")

    t0 = time.time()

    for epoch in range(1, epochs + 1):
        # --- Train ---
        model.train()
        epoch_loss = 0.0
        for batch in train_loader:
            batch = batch.to(device)
            recon, z = model(batch)
            loss = criterion(recon, batch)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item() * batch.size(0)

        train_loss = epoch_loss / n_train

        # --- Validate ---
        model.eval()
        val_loss_sum = 0.0
        with torch.no_grad():
            for batch in val_loader:
                batch = batch.to(device)
                recon, z = model(batch)
                loss = criterion(recon, batch)
                val_loss_sum += loss.item() * batch.size(0)

        val_loss = val_loss_sum / n_val

        train_losses.append(train_loss)
        val_losses.append(val_loss)

        scheduler.step(val_loss)

        # Early stopping
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            best_epoch = epoch
            epochs_no_improve = 0
            torch.save(model.state_dict(), model_path)
        else:
            epochs_no_improve += 1

        if epoch % 10 == 0 or epoch == 1 or epochs_no_improve == 0:
            elapsed = time.time() - t0
            print(
                f"  Epoch {epoch:4d}/{epochs}  "
                f"train_loss={train_loss:.6f}  val_loss={val_loss:.6f}  "
                f"best={best_val_loss:.6f} (ep{best_epoch})  "
                f"[{elapsed:.0f}s]"
            )

        if epochs_no_improve >= patience:
            print(f"\n  Early stopping at epoch {epoch} (no improvement for {patience} epochs)")
            break

    total_time = time.time() - t0
    print(f"\n  Training complete in {total_time:.1f}s")
    print(f"  Best val loss: {best_val_loss:.6f} at epoch {best_epoch}")
    print(f"  Model saved: {model_path}")

    # Save loss curves
    loss_data = {
        "train_losses": train_losses,
        "val_losses": val_losses,
        "best_epoch": best_epoch,
        "best_val_loss": best_val_loss,
    }
    loss_path = os.path.join(output_dir, "training_losses.json")
    with open(loss_path, "w") as f:
        json.dump(loss_data, f, indent=2)

    # ------------------------------------------------------------------
    # 4. Anomaly detection
    # ------------------------------------------------------------------
    print(f"\n[4/4] Computing reconstruction errors for anomaly detection")
    model.load_state_dict(torch.load(model_path, weights_only=True))
    anomalies = detect_anomalies(model, dataset, device, output_dir)

    return model, anomalies


# ---------------------------------------------------------------------------
# Anomaly detection
# ---------------------------------------------------------------------------
def detect_anomalies(
    model: nn.Module,
    dataset: CMBPatchDataset,
    device: str,
    output_dir: str,
    top_k: int = 50,
    sigma_threshold: float = 3.0,
):
    """
    Compute per-patch reconstruction error and identify anomalies.

    An anomaly is a patch whose reconstruction error exceeds
    mean + sigma_threshold * std of all reconstruction errors.
    """

    model.eval()
    all_errors = []
    all_latents = []

    loader = DataLoader(dataset, batch_size=64, shuffle=False, num_workers=0)

    with torch.no_grad():
        for batch in loader:
            batch = batch.to(device)
            recon, z = model(batch)
            # Per-patch MSE
            mse = ((recon - batch) ** 2).mean(dim=(1, 2, 3))  # shape: (B,)
            all_errors.append(mse.cpu().numpy())
            all_latents.append(z.cpu().numpy())

    errors = np.concatenate(all_errors)
    latents = np.concatenate(all_latents)

    mean_err = errors.mean()
    std_err = errors.std()
    threshold = mean_err + sigma_threshold * std_err

    # Identify anomalies
    anomaly_mask = errors > threshold
    anomaly_indices = np.where(anomaly_mask)[0]

    # Also get top-K by error
    top_k_indices = np.argsort(errors)[-top_k:][::-1]

    print(f"\n  Reconstruction error statistics:")
    print(f"    Mean: {mean_err:.6f}")
    print(f"    Std:  {std_err:.6f}")
    print(f"    Threshold ({sigma_threshold}sigma): {threshold:.6f}")
    print(f"    Anomalies (>{sigma_threshold}sigma): {len(anomaly_indices)}")
    print(f"    Top-{top_k} highest errors:")

    # Load metadata if available
    metadata_path = os.path.join(output_dir, "patch_metadata.json")
    metadata = None
    if os.path.exists(metadata_path):
        with open(metadata_path) as f:
            metadata = json.load(f)

    anomaly_records = []
    for rank, idx in enumerate(top_k_indices[:20]):
        sigma_val = (errors[idx] - mean_err) / std_err
        record = {
            "rank": rank + 1,
            "patch_index": int(idx),
            "mse": float(errors[idx]),
            "sigma": float(sigma_val),
        }
        if metadata and idx < len(metadata):
            record["glon_deg"] = metadata[idx]["glon_deg"]
            record["glat_deg"] = metadata[idx]["glat_deg"]
            record["raw_std"] = metadata[idx]["raw_std"]

        anomaly_records.append(record)
        loc = ""
        if metadata and idx < len(metadata):
            loc = f"  (l={metadata[idx]['glon_deg']:.1f}, b={metadata[idx]['glat_deg']:.1f})"
        print(f"      #{rank+1}: patch {idx}  MSE={errors[idx]:.6f}  ({sigma_val:.1f}sigma){loc}")

    # Save results
    results = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "n_patches": len(errors),
        "mean_error": float(mean_err),
        "std_error": float(std_err),
        "sigma_threshold": sigma_threshold,
        "threshold": float(threshold),
        "n_anomalies": int(anomaly_mask.sum()),
        "anomaly_fraction": float(anomaly_mask.mean()),
        "top_anomalies": anomaly_records,
        "anomaly_indices": [int(i) for i in anomaly_indices],
    }

    results_path = os.path.join(output_dir, "anomaly_results.json")
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n  Results saved: {results_path}")

    # Save reconstruction errors and latent vectors
    np.save(os.path.join(output_dir, "reconstruction_errors.npy"), errors)
    np.save(os.path.join(output_dir, "latent_vectors.npy"), latents)
    print(f"  Saved: reconstruction_errors.npy ({errors.shape})")
    print(f"  Saved: latent_vectors.npy ({latents.shape})")

    # Save top anomaly patches for visual inspection
    if hasattr(dataset, "patches"):
        top_patches = dataset.patches[top_k_indices]
        np.save(os.path.join(output_dir, "top_anomaly_patches.npy"), top_patches)
        print(f"  Saved: top_anomaly_patches.npy ({top_patches.shape})")

    print("\n" + "=" * 70)
    print("ANOMALY DETECTION COMPLETE")
    print("=" * 70)

    return results


# ---------------------------------------------------------------------------
# Detection-only mode (load pretrained model)
# ---------------------------------------------------------------------------
def detect_only(
    patches_file: str,
    model_path: str,
    output_dir: str = "outputs",
    latent_dim: int = 128,
    device: str = "auto",
):
    """Load a pretrained model and run anomaly detection."""

    print("=" * 70)
    print("PIPELINE A — CMB ANOMALY HUNTER: DETECTION ONLY")
    print("=" * 70)

    if device == "auto":
        if torch.cuda.is_available():
            device = "cuda"
        elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
            device = "mps"
        else:
            device = "cpu"

    dataset = CMBPatchDataset(patches_file)
    model = CMBAutoencoder(latent_dim=latent_dim).to(device)
    model.load_state_dict(torch.load(model_path, map_location=device, weights_only=True))

    return detect_anomalies(model, dataset, device, output_dir)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Pipeline A: CMB patch autoencoder for anomaly detection"
    )
    parser.add_argument(
        "--patches", type=str, default="outputs/cmb_patches.npy",
        help="Path to extracted patches .npy file",
    )
    parser.add_argument(
        "--output_dir", type=str, default="outputs",
        help="Output directory",
    )
    parser.add_argument(
        "--epochs", type=int, default=100,
        help="Max training epochs (default: 100)",
    )
    parser.add_argument(
        "--batch_size", type=int, default=32,
        help="Batch size (default: 32)",
    )
    parser.add_argument(
        "--lr", type=float, default=1e-3,
        help="Learning rate (default: 1e-3)",
    )
    parser.add_argument(
        "--latent_dim", type=int, default=128,
        help="Latent space dimension (default: 128)",
    )
    parser.add_argument(
        "--device", type=str, default="auto",
        help="Device: auto, cuda, mps, or cpu",
    )
    parser.add_argument(
        "--detect_only", action="store_true",
        help="Skip training, only run anomaly detection with a saved model",
    )
    parser.add_argument(
        "--model", type=str, default="outputs/autoencoder_best.pt",
        help="Path to saved model (for --detect_only mode)",
    )

    args = parser.parse_args()

    if args.detect_only:
        detect_only(
            patches_file=args.patches,
            model_path=args.model,
            output_dir=args.output_dir,
            latent_dim=args.latent_dim,
            device=args.device,
        )
    else:
        train_autoencoder(
            patches_file=args.patches,
            output_dir=args.output_dir,
            epochs=args.epochs,
            batch_size=args.batch_size,
            lr=args.lr,
            latent_dim=args.latent_dim,
            device=args.device,
        )


if __name__ == "__main__":
    main()
