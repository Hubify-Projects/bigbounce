#!/usr/bin/env python3
"""
Phase 8 Experiment: Multi-Modal Cross-Survey Joint Training
=============================================================
Train a joint autoencoder on DESI spectra (32 PCA components) +
photometric colors (SDSS ugriz + WISE W1W2 = 5 colors) = 37 dims.

Find anomalies that are normal in spectra-only OR photometry-only but
anomalous in the joint space. Tests whether cross-modal information
reveals hidden anomalies.

Output dir: multi-modal-joint
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
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, average_precision_score

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
OUTPUT_DIR = "/root/results/multi-modal-joint"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Hyperparameters
# ---------------------------------------------------------------------------
N_OBJECTS = 30000
N_SPECTRAL_PCA = 32
N_COLORS = 5  # u-g, g-r, r-i, i-z, W1-W2
N_FEATURES = N_SPECTRAL_PCA + N_COLORS  # 37
BATCH_SIZE = 256
EPOCHS = 50
LR = 1e-3
LATENT_DIM = 16
ANOMALY_FRACTION = 0.03
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(f"Device: {DEVICE}")
print(f"N_OBJECTS={N_OBJECTS}, N_FEATURES={N_FEATURES} (spectral={N_SPECTRAL_PCA}, colors={N_COLORS})")

# ---------------------------------------------------------------------------
# Synthetic multi-modal data generator
# ---------------------------------------------------------------------------
def generate_multimodal_data(n, anomaly_frac=0.03, seed=42):
    """
    Generate synthetic objects with correlated spectral PCA + photometric colors.

    Normal objects have consistent spectral-photometric correlations.
    Anomalies break the cross-modal correlation in specific ways.
    """
    rng = np.random.default_rng(seed)

    n_anom = int(n * anomaly_frac)
    labels = np.zeros(n, dtype=np.int64)
    anomaly_types = np.full(n, "normal", dtype="U30")

    # Object types with different spectral/photometric properties
    obj_types = rng.choice(["elliptical", "spiral", "starburst", "agn", "star"],
                           size=n, p=[0.25, 0.30, 0.15, 0.15, 0.15])

    # Type-specific mean spectral PCA components (32-dim)
    type_means = {
        "elliptical": rng.standard_normal(N_SPECTRAL_PCA) * 0.3 + np.array([2, -1, 0.5] + [0]*(N_SPECTRAL_PCA-3)),
        "spiral":     rng.standard_normal(N_SPECTRAL_PCA) * 0.3 + np.array([0, 1, -0.5] + [0]*(N_SPECTRAL_PCA-3)),
        "starburst":  rng.standard_normal(N_SPECTRAL_PCA) * 0.3 + np.array([-1, 2, 1] + [0]*(N_SPECTRAL_PCA-3)),
        "agn":        rng.standard_normal(N_SPECTRAL_PCA) * 0.3 + np.array([1, 0, 2] + [0]*(N_SPECTRAL_PCA-3)),
        "star":       rng.standard_normal(N_SPECTRAL_PCA) * 0.3 + np.array([-2, -1, -1] + [0]*(N_SPECTRAL_PCA-3)),
    }

    # Type-specific photometric colors: [u-g, g-r, r-i, i-z, W1-W2]
    type_colors = {
        "elliptical": np.array([1.8, 0.9, 0.4, 0.2, 0.0]),
        "spiral":     np.array([1.2, 0.6, 0.3, 0.15, -0.1]),
        "starburst":  np.array([0.5, 0.2, 0.1, 0.05, 0.3]),
        "agn":        np.array([0.8, 0.4, 0.3, 0.2, 0.8]),
        "star":       np.array([1.0, 0.5, 0.25, 0.12, -0.05]),
    }

    # Cross-modal correlation: first 3 PCA components predict colors
    # This is the key relationship the joint model should learn
    color_from_pca_weights = rng.standard_normal((N_COLORS, 3)) * 0.3

    spectral_pca = np.zeros((n, N_SPECTRAL_PCA), dtype=np.float32)
    colors = np.zeros((n, N_COLORS), dtype=np.float32)

    for i in range(n):
        otype = obj_types[i]

        # Spectral PCA: type mean + noise (decreasing variance for higher components)
        pca_noise_scale = np.exp(-np.arange(N_SPECTRAL_PCA) * 0.15) * 0.5
        spec = type_means[otype] + rng.normal(0, pca_noise_scale)
        spectral_pca[i] = spec.astype(np.float32)

        # Colors: type mean + correlated component from PCA + noise
        color_base = type_colors[otype]
        color_correlated = color_from_pca_weights @ spec[:3]
        color_noise = rng.normal(0, 0.1, N_COLORS)
        colors[i] = (color_base + color_correlated + color_noise).astype(np.float32)

    # -----------------------------------------------------------------------
    # Inject anomalies: objects that look normal in ONE modality but break
    # the cross-modal correlation
    # -----------------------------------------------------------------------
    for i in range(n_anom):
        labels[i] = 1

        atype = rng.integers(0, 4)
        if atype == 0:
            # Spectral-normal, color-anomalous: normal spectrum but wrong colors
            anomaly_types[i] = "color_mismatch"
            # Keep spectrum normal but assign colors from wrong type
            wrong_type = rng.choice([t for t in type_colors if t != obj_types[i]])
            colors[i] = (type_colors[wrong_type]
                         + rng.normal(0, 0.1, N_COLORS)).astype(np.float32)

        elif atype == 1:
            # Color-normal, spectral-anomalous: right colors but unusual spectrum
            anomaly_types[i] = "spectral_outlier"
            # Inject anomalous high-order PCA components (unusual fine structure)
            spectral_pca[i, 5:15] += rng.uniform(2, 5, 10).astype(np.float32) * rng.choice([-1, 1], 10)

        elif atype == 2:
            # Cross-modal break: both look individually plausible but violate
            # the spectral-photometric correlation
            anomaly_types[i] = "cross_modal_break"
            # Flip the sign of the correlated color component
            spec = spectral_pca[i]
            anti_correlated = -color_from_pca_weights @ spec[:3] * 2
            colors[i] += anti_correlated.astype(np.float32)

        else:
            # Hybrid anomaly: subtle in both modalities
            anomaly_types[i] = "hybrid_subtle"
            spectral_pca[i, :5] += rng.normal(0, 1.5, 5).astype(np.float32)
            colors[i] += rng.normal(0, 0.3, N_COLORS).astype(np.float32)

    return spectral_pca, colors, labels, anomaly_types, obj_types


# ---------------------------------------------------------------------------
# Dataset
# ---------------------------------------------------------------------------
class MultiModalDataset(Dataset):
    def __init__(self, spectral, colors, labels):
        self.joint = torch.from_numpy(
            np.concatenate([spectral, colors], axis=1)
        )
        self.spectral = torch.from_numpy(spectral)
        self.colors = torch.from_numpy(colors)
        self.labels = torch.from_numpy(labels)

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return self.joint[idx], self.spectral[idx], self.colors[idx], self.labels[idx]


# ---------------------------------------------------------------------------
# Joint Autoencoder (spectral PCA + colors)
# ---------------------------------------------------------------------------
class JointAutoencoder(nn.Module):
    def __init__(self, n_spectral, n_colors, latent_dim):
        super().__init__()
        n_input = n_spectral + n_colors

        self.encoder = nn.Sequential(
            nn.Linear(n_input, 128), nn.BatchNorm1d(128), nn.GELU(), nn.Dropout(0.1),
            nn.Linear(128, 64), nn.BatchNorm1d(64), nn.GELU(), nn.Dropout(0.1),
            nn.Linear(64, 32), nn.BatchNorm1d(32), nn.GELU(),
            nn.Linear(32, latent_dim),
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 32), nn.BatchNorm1d(32), nn.GELU(),
            nn.Linear(32, 64), nn.BatchNorm1d(64), nn.GELU(), nn.Dropout(0.1),
            nn.Linear(64, 128), nn.BatchNorm1d(128), nn.GELU(), nn.Dropout(0.1),
            nn.Linear(128, n_input),
        )

    def forward(self, x):
        z = self.encoder(x)
        return self.decoder(z)


# ---------------------------------------------------------------------------
# Spectral-only Autoencoder
# ---------------------------------------------------------------------------
class SpectralAutoencoder(nn.Module):
    def __init__(self, n_spectral, latent_dim):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(n_spectral, 64), nn.BatchNorm1d(64), nn.GELU(),
            nn.Linear(64, 32), nn.BatchNorm1d(32), nn.GELU(),
            nn.Linear(32, latent_dim),
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 32), nn.BatchNorm1d(32), nn.GELU(),
            nn.Linear(32, 64), nn.BatchNorm1d(64), nn.GELU(),
            nn.Linear(64, n_spectral),
        )

    def forward(self, x):
        return self.decoder(self.encoder(x))


# ---------------------------------------------------------------------------
# Photometry-only Autoencoder
# ---------------------------------------------------------------------------
class PhotometryAutoencoder(nn.Module):
    def __init__(self, n_colors, latent_dim):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(n_colors, 16), nn.BatchNorm1d(16), nn.GELU(),
            nn.Linear(16, 8), nn.BatchNorm1d(8), nn.GELU(),
            nn.Linear(8, latent_dim),
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 8), nn.BatchNorm1d(8), nn.GELU(),
            nn.Linear(8, 16), nn.BatchNorm1d(16), nn.GELU(),
            nn.Linear(16, n_colors),
        )

    def forward(self, x):
        return self.decoder(self.encoder(x))


# ---------------------------------------------------------------------------
# Training
# ---------------------------------------------------------------------------
def train_model(model, train_loader, val_loader, epochs, model_name, input_key):
    """
    input_key: 'joint', 'spectral', or 'colors' to select correct tensor from batch
    """
    optimizer = torch.optim.AdamW(model.parameters(), lr=LR, weight_decay=1e-4)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs)
    criterion = nn.MSELoss()

    key_idx = {"joint": 0, "spectral": 1, "colors": 2}[input_key]
    history = {"train_loss": [], "val_loss": []}
    best_val = float("inf")

    for epoch in range(epochs):
        model.train()
        losses = []
        for batch in train_loader:
            x = batch[key_idx].to(DEVICE)
            recon = model(x)
            loss = criterion(recon, x)
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            losses.append(loss.item())

        model.eval()
        val_losses = []
        with torch.no_grad():
            for batch in val_loader:
                x = batch[key_idx].to(DEVICE)
                recon = model(x)
                val_losses.append(criterion(recon, x).item())

        train_loss = np.mean(losses)
        val_loss = np.mean(val_losses)
        history["train_loss"].append(float(train_loss))
        history["val_loss"].append(float(val_loss))
        scheduler.step()

        if val_loss < best_val:
            best_val = val_loss
            try: torch.save(model.state_dict(), os.path.join(OUTPUT_DIR, f"{model_name}_best.pt"))
            except Exception as _e: print(f"[warn] checkpoint save failed: {_e}", flush=True)

        if (epoch + 1) % 10 == 0 or epoch == 0:
            print(f"  [{model_name}] Epoch {epoch+1}/{epochs} | train={train_loss:.6f} val={val_loss:.6f}")

    return history, best_val


def compute_errors(model, loader, input_key):
    key_idx = {"joint": 0, "spectral": 1, "colors": 2}[input_key]
    model.eval()
    errors, labels_all = [], []
    with torch.no_grad():
        for batch in loader:
            x = batch[key_idx].to(DEVICE)
            lab = batch[3]
            recon = model(x)
            mse = ((recon - x) ** 2).mean(dim=1).cpu().numpy()
            errors.append(mse)
            labels_all.append(lab.numpy())
    return np.concatenate(errors), np.concatenate(labels_all)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()

    # -----------------------------------------------------------------------
    # Generate data
    # -----------------------------------------------------------------------
    print("\n=== Generating 30K multi-modal objects ===")
    spectral_pca, colors, labels, anomaly_types, obj_types = generate_multimodal_data(
        N_OBJECTS, ANOMALY_FRACTION
    )
    print(f"  Spectral PCA shape: {spectral_pca.shape}")
    print(f"  Colors shape: {colors.shape}")
    print(f"  Anomalies: {labels.sum()} ({100*labels.mean():.1f}%)")

    # Count anomaly types
    atype_counts = {}
    for at in np.unique(anomaly_types):
        atype_counts[at] = int((anomaly_types == at).sum())
    print(f"  Anomaly types: {atype_counts}")

    # Standardize features
    scaler_spec = StandardScaler()
    scaler_color = StandardScaler()
    spectral_scaled = scaler_spec.fit_transform(spectral_pca).astype(np.float32)
    colors_scaled = scaler_color.fit_transform(colors).astype(np.float32)

    dataset = MultiModalDataset(spectral_scaled, colors_scaled, labels)
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
    # Train all three models
    # -----------------------------------------------------------------------
    print("\n=== Training Joint Autoencoder (37-dim) ===")
    joint_model = JointAutoencoder(N_SPECTRAL_PCA, N_COLORS, LATENT_DIM).to(DEVICE)
    n_params_joint = sum(p.numel() for p in joint_model.parameters())
    print(f"  Joint params: {n_params_joint:,}")
    hist_joint, best_joint = train_model(joint_model, train_loader, val_loader, EPOCHS, "joint", "joint")

    print("\n=== Training Spectral-Only Autoencoder (32-dim) ===")
    spec_model = SpectralAutoencoder(N_SPECTRAL_PCA, LATENT_DIM).to(DEVICE)
    n_params_spec = sum(p.numel() for p in spec_model.parameters())
    print(f"  Spectral params: {n_params_spec:,}")
    hist_spec, best_spec = train_model(spec_model, train_loader, val_loader, EPOCHS, "spectral", "spectral")

    print("\n=== Training Photometry-Only Autoencoder (5-dim) ===")
    photo_model = PhotometryAutoencoder(N_COLORS, min(LATENT_DIM, 4)).to(DEVICE)
    n_params_photo = sum(p.numel() for p in photo_model.parameters())
    print(f"  Photometry params: {n_params_photo:,}")
    hist_photo, best_photo = train_model(photo_model, train_loader, val_loader, EPOCHS, "photometry", "colors")

    # -----------------------------------------------------------------------
    # Compute reconstruction errors
    # -----------------------------------------------------------------------
    print("\n=== Computing reconstruction errors ===")
    # [patched] skip load — checkpoint save unreliable on this PyTorch 2.4.1 build
    # [patched] skip load — checkpoint save unreliable on this PyTorch 2.4.1 build
    # [patched] skip load — checkpoint save unreliable on this PyTorch 2.4.1 build

    err_joint, lab = compute_errors(joint_model, full_loader, "joint")
    err_spec, _ = compute_errors(spec_model, full_loader, "spectral")
    err_photo, _ = compute_errors(photo_model, full_loader, "colors")

    # -----------------------------------------------------------------------
    # Thresholds (95th percentile of normal)
    # -----------------------------------------------------------------------
    normal = lab == 0
    thresh_joint = np.percentile(err_joint[normal], 95)
    thresh_spec = np.percentile(err_spec[normal], 95)
    thresh_photo = np.percentile(err_photo[normal], 95)

    anom_joint = err_joint > thresh_joint
    anom_spec = err_spec > thresh_spec
    anom_photo = err_photo > thresh_photo

    # KEY METRIC: anomalous in joint but normal in BOTH single modalities
    joint_only = anom_joint & ~anom_spec & ~anom_photo
    # Normal in joint but anomalous in at least one single modality
    single_only = ~anom_joint & (anom_spec | anom_photo)

    print(f"\n  Thresholds - joint: {thresh_joint:.6f}, spec: {thresh_spec:.6f}, photo: {thresh_photo:.6f}")
    print(f"  Joint flagged:      {anom_joint.sum()}")
    print(f"  Spectral flagged:   {anom_spec.sum()}")
    print(f"  Photometry flagged: {anom_photo.sum()}")
    print(f"  JOINT-ONLY (hidden anomalies): {joint_only.sum()}")
    print(f"  Single-only (missed by joint): {single_only.sum()}")

    # -----------------------------------------------------------------------
    # AUC scores
    # -----------------------------------------------------------------------
    auc_joint = roc_auc_score(lab, err_joint)
    auc_spec = roc_auc_score(lab, err_spec)
    auc_photo = roc_auc_score(lab, err_photo)

    ap_joint = average_precision_score(lab, err_joint)
    ap_spec = average_precision_score(lab, err_spec)
    ap_photo = average_precision_score(lab, err_photo)

    # Combined single-modality score
    err_spec_norm = (err_spec - err_spec[normal].mean()) / (err_spec[normal].std() + 1e-12)
    err_photo_norm = (err_photo - err_photo[normal].mean()) / (err_photo[normal].std() + 1e-12)
    err_combined_single = np.maximum(err_spec_norm, err_photo_norm)
    auc_combined_single = roc_auc_score(lab, err_combined_single)

    print(f"\n  AUC - Joint: {auc_joint:.4f}, Spectral: {auc_spec:.4f}, Photo: {auc_photo:.4f}")
    print(f"  AUC - Combined single: {auc_combined_single:.4f}")
    print(f"  AP  - Joint: {ap_joint:.4f}, Spectral: {ap_spec:.4f}, Photo: {ap_photo:.4f}")
    print(f"  Joint AUC improvement over best single: {auc_joint - max(auc_spec, auc_photo):+.4f}")

    # -----------------------------------------------------------------------
    # Per anomaly-type detection rates
    # -----------------------------------------------------------------------
    print("\n=== Per anomaly-type detection rates ===")
    per_type_detection = {}
    for atype in ["color_mismatch", "spectral_outlier", "cross_modal_break", "hybrid_subtle"]:
        mask = anomaly_types == atype
        if mask.sum() == 0:
            continue
        n_type = int(mask.sum())
        det_joint = int((anom_joint & mask).sum())
        det_spec = int((anom_spec & mask).sum())
        det_photo = int((anom_photo & mask).sum())
        det_joint_only = int((joint_only & mask).sum())

        per_type_detection[atype] = {
            "count": n_type,
            "detected_joint": det_joint,
            "detected_spectral": det_spec,
            "detected_photometry": det_photo,
            "joint_only": det_joint_only,
            "joint_rate": det_joint / n_type if n_type > 0 else 0,
            "spectral_rate": det_spec / n_type if n_type > 0 else 0,
            "photometry_rate": det_photo / n_type if n_type > 0 else 0,
        }
        print(f"  {atype}: n={n_type}, joint={det_joint} ({100*det_joint/n_type:.0f}%), "
              f"spec={det_spec} ({100*det_spec/n_type:.0f}%), "
              f"photo={det_photo} ({100*det_photo/n_type:.0f}%), "
              f"joint_only={det_joint_only}")

    # -----------------------------------------------------------------------
    # Cross-modal correlation analysis
    # -----------------------------------------------------------------------
    print("\n=== Cross-modal correlation (spec error vs photo error) ===")
    corr_all = np.corrcoef(err_spec, err_photo)[0, 1]
    corr_normal = np.corrcoef(err_spec[normal], err_photo[normal])[0, 1]
    corr_anom = np.corrcoef(err_spec[lab == 1], err_photo[lab == 1])[0, 1] if (lab == 1).sum() > 1 else 0.0
    print(f"  Correlation (all): {corr_all:.4f}")
    print(f"  Correlation (normal): {corr_normal:.4f}")
    print(f"  Correlation (anomalous): {corr_anom:.4f}")

    # -----------------------------------------------------------------------
    # Save results
    # -----------------------------------------------------------------------
    results_df = pd.DataFrame({
        "index": np.arange(N_OBJECTS),
        "label": lab,
        "anomaly_type": anomaly_types,
        "obj_type": obj_types,
        "err_joint": err_joint,
        "err_spectral": err_spec,
        "err_photometry": err_photo,
        "anom_joint": anom_joint.astype(int),
        "anom_spectral": anom_spec.astype(int),
        "anom_photometry": anom_photo.astype(int),
        "joint_only": joint_only.astype(int),
        "single_only": single_only.astype(int),
    })
    try:

        results_df.to_csv(os.path.join(OUTPUT_DIR, "all_errors.csv"), index=False)

    except Exception as _e: print(f"[warn] csv write failed: {_e}", flush=True)

    # Joint-only anomalies (the key finding)
    joint_only_df = results_df[results_df["joint_only"] == 1].sort_values("err_joint", ascending=False)
    try:

        joint_only_df.to_csv(os.path.join(OUTPUT_DIR, "joint_only_anomalies.csv"), index=False)

    except Exception as _e: print(f"[warn] csv write failed: {_e}", flush=True)

    # Hidden anomalies: true anomalies caught ONLY by joint model
    hidden_true = results_df[(results_df["joint_only"] == 1) & (results_df["label"] == 1)]
    try: hidden_true.to_csv(os.path.join(OUTPUT_DIR, "hidden_true_anomalies.csv"), index=False)
    except Exception as _e: print(f"[warn] csv write failed: {_e}", flush=True)
    print(f"\n  Hidden true anomalies (joint-only & labeled): {len(hidden_true)}")

    elapsed = time.time() - t0

    summary = {
        "experiment": "Phase 8: Multi-Modal Cross-Survey Joint Training",
        "n_objects": N_OBJECTS,
        "n_spectral_pca": N_SPECTRAL_PCA,
        "n_colors": N_COLORS,
        "n_features_total": N_FEATURES,
        "latent_dim": LATENT_DIM,
        "anomaly_fraction_injected": ANOMALY_FRACTION,
        "n_anomalies_injected": int(labels.sum()),
        "anomaly_type_counts": atype_counts,
        "joint_model": {
            "n_params": n_params_joint,
            "best_val_loss": best_joint,
            "auc": auc_joint,
            "average_precision": ap_joint,
            "n_flagged": int(anom_joint.sum()),
            "threshold": float(thresh_joint),
            "training_history": hist_joint,
        },
        "spectral_model": {
            "n_params": n_params_spec,
            "best_val_loss": best_spec,
            "auc": auc_spec,
            "average_precision": ap_spec,
            "n_flagged": int(anom_spec.sum()),
            "threshold": float(thresh_spec),
            "training_history": hist_spec,
        },
        "photometry_model": {
            "n_params": n_params_photo,
            "best_val_loss": best_photo,
            "auc": auc_photo,
            "average_precision": ap_photo,
            "n_flagged": int(anom_photo.sum()),
            "threshold": float(thresh_photo),
            "training_history": hist_photo,
        },
        "comparison": {
            "auc_combined_single": auc_combined_single,
            "joint_auc_improvement": float(auc_joint - max(auc_spec, auc_photo)),
            "joint_only_count": int(joint_only.sum()),
            "single_only_count": int(single_only.sum()),
            "hidden_true_anomalies": len(hidden_true),
            "cross_modal_correlation_all": float(corr_all),
            "cross_modal_correlation_normal": float(corr_normal),
            "cross_modal_correlation_anomalous": float(corr_anom),
        },
        "per_type_detection": per_type_detection,
        "runtime_seconds": elapsed,
        "device": str(DEVICE),
    }

    try:
        with open(os.path.join(OUTPUT_DIR, "summary.json"), "w") as f:
            json.dump(summary, f, indent=2, cls=NumpyEncoder)
        print("Summary JSON saved")
    except Exception as _e:
        print(f"[warn] json save failed: {_e}", flush=True)
        print(json.dumps(summary, indent=2, cls=NumpyEncoder))

    print(f"\nResults saved to {OUTPUT_DIR}")
    print(f"Runtime: {elapsed:.1f}s")
    print("COMPLETE")


if __name__ == "__main__":
    main()
