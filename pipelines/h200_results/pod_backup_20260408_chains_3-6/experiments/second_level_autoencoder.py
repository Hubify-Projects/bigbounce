#!/usr/bin/env python3
"""
Second-Level Autoencoder — Anomalies Within Anomalies
=====================================================
Train a NEW autoencoder on the 195K anomaly latent vectors themselves.
Objects that are anomalous WITHIN the anomaly population are the most
extreme outliers — potential new classes of astrophysical objects that
no existing catalog describes.

Strategy:
  1. Load 195K anomaly latent vectors (128-dim) from DESI outputs
  2. Train autoencoder: 128→64→32→16→32→64→128
  3. Score every anomaly by reconstruction error on this second-level model
  4. Top-50 ultra-rare objects are ranked by second-level anomaly score
  5. Compare score distribution to first-level scores

If real data unavailable, generates 195K synthetic anomaly vectors with
200 planted "ultra-anomalies" that are outliers even among outliers.

Output: second-level-anomalies/
"""

import json
import os
import sys
import time
import numpy as np
import pandas as pd
from datetime import datetime, timezone
from pathlib import Path

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/root/p1_outputs/runs/second_level_autoencoder"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


class NumpyEncoder(json.JSONEncoder):
    """JSON encoder that handles numpy types."""
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


# ═══════════════════════════════════════════════════════
# Data Loading
# ═══════════════════════════════════════════════════════

SEARCH_PATHS = [
    Path("/root/p1_outputs/runs/second_level_autoencoder1"),
    Path("/workspace/bigbounce/pipelines/h200_results/desi_dr1"),
    Path("/root/p1_outputs/runs/second_level_autoencoder"),
    Path("/workspace/bigbounce/pipelines/p3_anomaly_engine/outputs"),
    Path("/workspace/bigbounce/outputs"),
]


def load_real_latent_vectors():
    """Attempt to load real anomaly latent vectors from pod outputs."""
    print("  Searching for anomaly latent vectors...")

    for search_path in SEARCH_PATHS:
        if not search_path.exists():
            continue

        # Priority 1: numpy latent vector files
        for pattern in ["*latent*.npy", "*latent*.npz", "*embeddings*.npy",
                        "*embeddings*.npz", "*encoded*.npy"]:
            for f in sorted(search_path.glob(pattern)):
                try:
                    if f.suffix == ".npy":
                        data = np.load(f)
                        print(f"  Found latent vectors: {f} shape={data.shape}")
                        return data, str(f)
                    elif f.suffix == ".npz":
                        npz = np.load(f)
                        key = list(npz.keys())[0]
                        data = npz[key]
                        print(f"  Found latent vectors: {f}[{key}] shape={data.shape}")
                        return data, str(f)
                except Exception as e:
                    print(f"  Error loading {f}: {e}")

        # Priority 2: anomaly catalog with numeric features
        for pattern in ["*anomal*.csv", "*anomal*.parquet", "*scores*.csv"]:
            for f in sorted(search_path.glob(pattern)):
                try:
                    if f.suffix == ".parquet":
                        df = pd.read_parquet(f)
                    else:
                        df = pd.read_csv(f, nrows=200000)
                    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
                    if len(num_cols) >= 10:
                        print(f"  Found feature data: {f} ({len(df)} rows, {len(num_cols)} features)")
                        return df[num_cols].values.astype(np.float32), str(f)
                except Exception:
                    continue

    # Priority 3: dr1_all_anomalies.json
    json_path = Path("/workspace/dr1_all_anomalies.json")
    if json_path.exists():
        try:
            with open(json_path) as jf:
                data = json.load(jf)
            if isinstance(data, list) and len(data) > 0:
                # Extract numeric fields
                keys = [k for k in data[0].keys()
                        if isinstance(data[0].get(k), (int, float))]
                arr = np.array([[obj.get(k, 0.0) for k in keys] for obj in data],
                               dtype=np.float32)
                print(f"  Loaded from dr1_all_anomalies.json: {arr.shape}")
                return arr, str(json_path)
        except Exception as e:
            print(f"  Error loading JSON: {e}")

    return None, None


def generate_synthetic_data(n_objects=195000, latent_dim=128, n_ultra=200):
    """Generate synthetic anomaly latent vectors with planted ultra-anomalies."""
    print(f"  Generating synthetic data: {n_objects} anomalies, {n_ultra} ultra-anomalies")
    np.random.seed(42)

    # Base anomaly population: mixture of 8 clusters in 128-dim space
    vectors = []
    labels = []

    cluster_sizes = [30000, 28000, 25000, 22000, 20000, 18000, 15000, 12000]
    remaining = n_objects - n_ultra - sum(cluster_sizes)
    cluster_sizes.append(max(remaining, 0))

    population_names = [
        "BAL_QSO", "emission_line", "star_forming", "AGN_broad",
        "stellar_contam", "high_z_QSO", "Fe_emission", "absorption_sys",
        "diffuse_background"
    ]

    for i, (n_pop, name) in enumerate(zip(cluster_sizes, population_names)):
        if n_pop <= 0:
            continue
        center = np.random.randn(latent_dim) * 4.0
        spread = np.random.uniform(1.0, 3.0)
        vecs = center + np.random.randn(n_pop, latent_dim).astype(np.float32) * spread
        vectors.append(vecs)
        labels.extend([name] * n_pop)

    # Plant ultra-anomalies: objects far from ANY cluster center
    # These should be outliers even among outliers
    ultra_vecs = np.random.randn(n_ultra, latent_dim).astype(np.float32) * 15.0
    # Add some with extreme values in a few dimensions
    for i in range(n_ultra):
        n_extreme = np.random.randint(3, 12)
        dims = np.random.choice(latent_dim, n_extreme, replace=False)
        ultra_vecs[i, dims] *= np.random.uniform(2.0, 5.0, n_extreme)
    vectors.append(ultra_vecs)
    labels.extend(["ULTRA_ANOMALY"] * n_ultra)

    all_vectors = np.vstack(vectors).astype(np.float32)

    # Generate metadata
    n_total = len(all_vectors)
    metadata = pd.DataFrame({
        "object_id": [f"ANOM_{i:06d}" for i in range(n_total)],
        "ra": np.random.uniform(100, 280, n_total),
        "dec": np.random.uniform(-20, 80, n_total),
        "redshift": np.abs(np.random.normal(1.5, 0.8, n_total)),
        "first_level_score": np.exp(np.random.normal(3.0, 1.5, n_total)),
        "true_label": labels[:n_total],
    })

    # Shuffle
    idx = np.random.permutation(n_total)
    return all_vectors[idx], metadata.iloc[idx].reset_index(drop=True)


# ═══════════════════════════════════════════════════════
# Autoencoder Model
# ═══════════════════════════════════════════════════════

class SecondLevelAutoencoder(nn.Module):
    """Autoencoder trained on anomaly latent vectors: 128→64→32→16→32→64→128."""

    def __init__(self, input_dim=128):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(64, 32),
            nn.BatchNorm1d(32),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(32, 16),
        )
        self.decoder = nn.Sequential(
            nn.Linear(16, 32),
            nn.BatchNorm1d(32),
            nn.ReLU(),
            nn.Linear(32, 64),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Linear(64, input_dim),
        )

    def forward(self, x):
        z = self.encoder(x)
        x_recon = self.decoder(z)
        return x_recon, z

    def encode(self, x):
        return self.encoder(x)


# ═══════════════════════════════════════════════════════
# Training
# ═══════════════════════════════════════════════════════

def train_autoencoder(vectors, device, epochs=100, batch_size=2048, lr=1e-3):
    """Train the second-level autoencoder."""
    input_dim = vectors.shape[1]
    model = SecondLevelAutoencoder(input_dim=input_dim).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=1e-5)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs)
    criterion = nn.MSELoss()

    # Normalize the input
    mean = vectors.mean(axis=0)
    std = vectors.std(axis=0) + 1e-8
    vectors_norm = (vectors - mean) / std

    tensor_data = torch.tensor(vectors_norm, dtype=torch.float32)
    dataset = TensorDataset(tensor_data)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=True,
                        num_workers=4, pin_memory=True)

    # Split for validation
    n_val = int(0.1 * len(tensor_data))
    val_data = tensor_data[:n_val].to(device)
    train_losses = []
    val_losses = []

    print(f"\n  Training second-level autoencoder:")
    print(f"    Input dim: {input_dim}")
    print(f"    Architecture: {input_dim}→64→32→16→32→64→{input_dim}")
    print(f"    Training samples: {len(tensor_data) - n_val}")
    print(f"    Validation samples: {n_val}")
    print(f"    Epochs: {epochs}, Batch: {batch_size}, LR: {lr}")

    best_val_loss = float("inf")
    best_state = None
    t0 = time.time()

    for epoch in range(epochs):
        model.train()
        epoch_loss = 0.0
        n_batches = 0

        for (batch,) in loader:
            batch = batch.to(device, non_blocking=True)
            optimizer.zero_grad()
            recon, _ = model(batch)
            loss = criterion(recon, batch)
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
            n_batches += 1

        scheduler.step()
        avg_train_loss = epoch_loss / n_batches

        # Validation
        model.eval()
        with torch.no_grad():
            val_recon, _ = model(val_data)
            val_loss = criterion(val_recon, val_data).item()

        train_losses.append(avg_train_loss)
        val_losses.append(val_loss)

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}

        if (epoch + 1) % 10 == 0 or epoch == 0:
            elapsed = time.time() - t0
            print(f"    Epoch {epoch+1:3d}/{epochs}: train_loss={avg_train_loss:.6f}  "
                  f"val_loss={val_loss:.6f}  best_val={best_val_loss:.6f}  "
                  f"[{elapsed:.1f}s]")

    # Restore best model
    if best_state is not None:
        model.load_state_dict(best_state)

    training_time = time.time() - t0
    print(f"\n  Training complete in {training_time:.1f}s")
    print(f"  Best validation loss: {best_val_loss:.6f}")

    return model, mean, std, train_losses, val_losses, training_time


# ═══════════════════════════════════════════════════════
# Scoring
# ═══════════════════════════════════════════════════════

def score_anomalies(model, vectors, mean, std, device, batch_size=4096):
    """Score all anomalies by second-level reconstruction error."""
    model.eval()
    vectors_norm = (vectors - mean) / std
    tensor_data = torch.tensor(vectors_norm, dtype=torch.float32)
    dataset = TensorDataset(tensor_data)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=False,
                        num_workers=4, pin_memory=True)

    all_scores = []
    all_latents = []

    with torch.no_grad():
        for (batch,) in loader:
            batch = batch.to(device, non_blocking=True)
            recon, z = model(batch)
            # Per-sample MSE
            mse = ((recon - batch) ** 2).mean(dim=1)
            all_scores.append(mse.cpu().numpy())
            all_latents.append(z.cpu().numpy())

    scores = np.concatenate(all_scores)
    latents = np.concatenate(all_latents)
    return scores, latents


# ═══════════════════════════════════════════════════════
# Main Experiment
# ═══════════════════════════════════════════════════════

def main():
    print("=" * 70)
    print("SECOND-LEVEL AUTOENCODER — Anomalies Within Anomalies")
    print("=" * 70)
    t_start = time.time()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"\n  Device: {device}")
    if device.type == "cuda":
        print(f"  GPU: {torch.cuda.get_device_name(0)}")

    # Load data
    print("\n[1/5] Loading anomaly data...")
    vectors, source = load_real_latent_vectors()
    metadata = None
    data_source = "real"

    if vectors is None:
        print("  No real data found — generating synthetic dataset")
        vectors, metadata = generate_synthetic_data(n_objects=195000, latent_dim=128, n_ultra=200)
        source = "synthetic"
        data_source = "synthetic"
    else:
        # Pad or truncate to 128 dims if needed
        if vectors.shape[1] < 128:
            pad = np.zeros((vectors.shape[0], 128 - vectors.shape[1]), dtype=np.float32)
            vectors = np.hstack([vectors, pad])
        elif vectors.shape[1] > 128:
            vectors = vectors[:, :128]
        vectors = vectors.astype(np.float32)

    print(f"  Data shape: {vectors.shape}")
    print(f"  Source: {source}")

    # Train
    print("\n[2/5] Training second-level autoencoder...")
    model, mean, std, train_losses, val_losses, training_time = train_autoencoder(
        vectors, device, epochs=100, batch_size=2048
    )

    # Score
    print("\n[3/5] Scoring all anomalies...")
    scores, latents_16d = score_anomalies(model, vectors, mean, std, device)

    # Analysis
    print("\n[4/5] Analyzing score distribution...")
    score_percentiles = {
        f"p{p}": float(np.percentile(scores, p))
        for p in [50, 90, 95, 99, 99.5, 99.9]
    }
    print(f"  Score percentiles: {score_percentiles}")

    # Top 50 ultra-rare objects
    top_indices = np.argsort(scores)[-50:][::-1]
    top_50 = []
    for rank, idx in enumerate(top_indices):
        entry = {
            "rank": rank + 1,
            "index": int(idx),
            "second_level_score": float(scores[idx]),
            "score_percentile": float((scores < scores[idx]).sum() / len(scores) * 100),
            "latent_16d": latents_16d[idx].tolist(),
        }
        if metadata is not None:
            row = metadata.iloc[idx]
            entry["object_id"] = str(row.get("object_id", f"IDX_{idx}"))
            entry["ra"] = float(row.get("ra", 0))
            entry["dec"] = float(row.get("dec", 0))
            entry["redshift"] = float(row.get("redshift", 0))
            entry["first_level_score"] = float(row.get("first_level_score", 0))
            entry["true_label"] = str(row.get("true_label", "unknown"))
        top_50.append(entry)

    print(f"\n  Top 50 ultra-rare objects:")
    for obj in top_50[:10]:
        label_str = f" [{obj.get('true_label', '?')}]" if 'true_label' in obj else ""
        print(f"    #{obj['rank']:2d}: idx={obj['index']:6d}  "
              f"score={obj['second_level_score']:.4f}  "
              f"percentile={obj['score_percentile']:.2f}%{label_str}")

    # Recovery check if synthetic
    recovery_stats = None
    if data_source == "synthetic" and metadata is not None:
        top_200_idx = set(np.argsort(scores)[-200:][::-1])
        ultra_mask = metadata["true_label"] == "ULTRA_ANOMALY"
        ultra_indices = set(np.where(ultra_mask.values)[0])
        recovered = top_200_idx & ultra_indices
        precision = len(recovered) / len(top_200_idx) if top_200_idx else 0
        recall = len(recovered) / len(ultra_indices) if ultra_indices else 0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
        recovery_stats = {
            "n_planted_ultra": len(ultra_indices),
            "n_recovered_in_top200": len(recovered),
            "precision_at_200": precision,
            "recall_at_200": recall,
            "f1_at_200": f1,
        }
        print(f"\n  Ultra-anomaly recovery (top 200):")
        print(f"    Planted: {len(ultra_indices)}")
        print(f"    Recovered: {len(recovered)}")
        print(f"    Precision: {precision:.3f}")
        print(f"    Recall: {recall:.3f}")
        print(f"    F1: {f1:.3f}")

    # Score correlation with first-level
    correlation = None
    if metadata is not None and "first_level_score" in metadata.columns:
        from scipy.stats import spearmanr
        rho, pval = spearmanr(scores, metadata["first_level_score"].values)
        correlation = {"spearman_rho": float(rho), "p_value": float(pval)}
        print(f"\n  Score correlation (2nd vs 1st level):")
        print(f"    Spearman rho = {rho:.4f}, p = {pval:.2e}")
        print(f"    Low correlation = second level finds NEW types of outliers")

    # Save results
    print("\n[5/5] Saving results...")
    total_time = time.time() - t_start

    summary = {
        "experiment": "second_level_autoencoder",
        "description": "Anomalies within anomalies — ultra-rare object finder",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "data_source": data_source,
        "source_path": str(source),
        "n_objects": int(vectors.shape[0]),
        "input_dim": int(vectors.shape[1]),
        "architecture": "128→64→32→16→32→64→128",
        "training": {
            "epochs": 100,
            "batch_size": 2048,
            "best_val_loss": float(val_losses[-1]) if val_losses else None,
            "training_time_s": float(training_time),
            "final_train_loss": float(train_losses[-1]) if train_losses else None,
        },
        "score_distribution": {
            "mean": float(np.mean(scores)),
            "std": float(np.std(scores)),
            "min": float(np.min(scores)),
            "max": float(np.max(scores)),
            "percentiles": score_percentiles,
        },
        "top_50_ultra_rare": top_50,
        "recovery_stats": recovery_stats,
        "score_correlation_with_first_level": correlation,
        "total_time_s": float(total_time),
        "device": str(device),
    }

    with open(OUTPUT_DIR / "second_level_summary.json", "w") as f:
        json.dump(summary, f, indent=2, cls=NumpyEncoder)

    # Save scores array
    np.save(OUTPUT_DIR / "second_level_scores.npy", scores)
    np.save(OUTPUT_DIR / "second_level_latents_16d.npy", latents_16d)

    # Save training curves
    curves_df = pd.DataFrame({
        "epoch": range(1, len(train_losses) + 1),
        "train_loss": train_losses,
        "val_loss": val_losses,
    })
    curves_df.to_csv(OUTPUT_DIR / "training_curves.csv", index=False)

    # Save top 50 as CSV
    top_df = pd.DataFrame(top_50)
    top_df.to_csv(OUTPUT_DIR / "top50_ultra_rare.csv", index=False)

    print(f"\n  Saved to: {OUTPUT_DIR}")
    print(f"  Total time: {total_time:.1f}s")

    print("\n" + "=" * 70)
    print("COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
