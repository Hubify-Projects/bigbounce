#!/usr/bin/env python3
"""
Production BigAE training at scale.
- 500K synthetic DESI-like spectra
- Larger model (4x params)
- 500 epochs
- Outputs: trained weights, anomaly scores, training curves
"""
import os, json, time
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from datetime import datetime

OUTPUT_DIR = "/root/p1_outputs/runs/bigae_production"
os.makedirs(OUTPUT_DIR, exist_ok=True)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Device: {device}")
print(f"Start: {datetime.now()}")

# Config
N_SPECTRA = 500_000
N_BINS = 4096
N_LATENT = 512
N_EPOCHS = 100
BATCH_SIZE = 4096
LR = 1e-3
ANOMALY_FRACTION = 0.01

print(f"\n=== Generating {N_SPECTRA:,} synthetic spectra ({N_BINS} bins) ===")
torch.manual_seed(42)
np.random.seed(42)

# Background: smooth continuum + emission lines
def gen_normal(n):
    wave = np.linspace(0, 1, N_BINS)
    cont = 1.0 + 0.3 * np.sin(2 * np.pi * 3 * wave) + 0.1 * np.random.randn(n, N_BINS)
    n_lines = 4
    for _ in range(n_lines):
        center = np.random.uniform(0.1, 0.9, n)[:, None]
        width = 0.01
        height = np.random.uniform(0.5, 2.0, n)[:, None]
        line = height * np.exp(-((wave[None, :] - center) / width) ** 2)
        cont += line
    return cont.astype(np.float32)

def gen_anomaly(n):
    base = gen_normal(n)
    # Inject extreme features
    for i in range(n):
        kind = np.random.choice(["broad", "sharp", "redshift"])
        if kind == "broad":
            c = np.random.uniform(0.2, 0.8)
            base[i] += 2 * np.exp(-((np.linspace(0,1,N_BINS) - c) / 0.1)**2)
        elif kind == "sharp":
            idx = np.random.randint(100, N_BINS-100)
            base[i, idx-5:idx+5] += 5
        else:
            base[i] = np.roll(base[i], np.random.randint(-200, 200))
    return base

n_anom = int(N_SPECTRA * ANOMALY_FRACTION)
n_norm = N_SPECTRA - n_anom
print(f"  Normal: {n_norm:,}, Anomalies: {n_anom:,}")

t0 = time.time()
X_norm = gen_normal(n_norm)
X_anom = gen_anomaly(n_anom)
X = np.concatenate([X_norm, X_anom])
y = np.concatenate([np.zeros(n_norm), np.ones(n_anom)])
perm = np.random.permutation(N_SPECTRA)
X = X[perm]; y = y[perm]
print(f"  Generated in {time.time()-t0:.1f}s")

# Normalize
X = (X - X.mean(axis=1, keepdims=True)) / (X.std(axis=1, keepdims=True) + 1e-8)
X_tensor = torch.from_numpy(X).float()

# Split train/val
n_val = int(0.1 * N_SPECTRA)
X_train, X_val = X_tensor[:-n_val], X_tensor[-n_val:]
y_train, y_val = y[:-n_val], y[-n_val:]

train_loader = DataLoader(TensorDataset(X_train), batch_size=BATCH_SIZE, shuffle=True, num_workers=4, pin_memory=True)
val_loader = DataLoader(TensorDataset(X_val), batch_size=BATCH_SIZE, shuffle=False, num_workers=4, pin_memory=True)

# Model: 4096 -> 1024 -> 512 -> 1024 -> 4096
class BigAE(nn.Module):
    def __init__(self, in_dim=N_BINS, latent=N_LATENT):
        super().__init__()
        self.enc = nn.Sequential(
            nn.Linear(in_dim, 2048), nn.GELU(), nn.Dropout(0.1),
            nn.Linear(2048, 1024), nn.GELU(), nn.Dropout(0.1),
            nn.Linear(1024, latent),
        )
        self.dec = nn.Sequential(
            nn.Linear(latent, 1024), nn.GELU(), nn.Dropout(0.1),
            nn.Linear(1024, 2048), nn.GELU(), nn.Dropout(0.1),
            nn.Linear(2048, in_dim),
        )
    def forward(self, x):
        z = self.enc(x)
        return self.dec(z), z

model = BigAE().to(device)
n_params = sum(p.numel() for p in model.parameters())
print(f"\n=== Model: BigAE with {n_params:,} parameters ===")

optim = torch.optim.AdamW(model.parameters(), lr=LR, weight_decay=1e-5)
sched = torch.optim.lr_scheduler.CosineAnnealingLR(optim, T_max=N_EPOCHS)
loss_fn = nn.MSELoss()

print(f"\n=== Training {N_EPOCHS} epochs ===")
history = {"train": [], "val": [], "lr": [], "epoch_time": []}
best_val = float("inf")

for epoch in range(N_EPOCHS):
    t_ep = time.time()
    model.train()
    train_loss = 0
    n = 0
    for (x,) in train_loader:
        x = x.to(device, non_blocking=True)
        optim.zero_grad()
        recon, _ = model(x)
        loss = loss_fn(recon, x)
        loss.backward()
        optim.step()
        train_loss += loss.item() * x.size(0)
        n += x.size(0)
    train_loss /= n

    model.eval()
    val_loss = 0
    n = 0
    with torch.no_grad():
        for (x,) in val_loader:
            x = x.to(device, non_blocking=True)
            recon, _ = model(x)
            val_loss += loss_fn(recon, x).item() * x.size(0)
            n += x.size(0)
    val_loss /= n

    lr_now = optim.param_groups[0]["lr"]
    sched.step()
    et = time.time() - t_ep
    history["train"].append(train_loss)
    history["val"].append(val_loss)
    history["lr"].append(lr_now)
    history["epoch_time"].append(et)

    if val_loss < best_val:
        best_val = val_loss
        torch.save(model.state_dict(), os.path.join(OUTPUT_DIR, "best.pt"))

    if epoch < 3 or epoch % 5 == 0 or epoch == N_EPOCHS - 1:
        print(f"  Epoch {epoch+1:3d}/{N_EPOCHS}: train={train_loss:.5f} val={val_loss:.5f} best={best_val:.5f} lr={lr_now:.2e} [{et:.1f}s]")

print(f"\n=== Anomaly detection eval ===")
model.load_state_dict(torch.load(os.path.join(OUTPUT_DIR, "best.pt")))
model.eval()
all_scores = []
all_labels = []
loader = DataLoader(TensorDataset(X_tensor, torch.from_numpy(y).float()), batch_size=BATCH_SIZE, num_workers=4, pin_memory=True)
with torch.no_grad():
    for x, l in loader:
        x = x.to(device, non_blocking=True)
        recon, _ = model(x)
        scores = ((recon - x) ** 2).mean(dim=1).cpu().numpy()
        all_scores.append(scores)
        all_labels.append(l.numpy())
scores = np.concatenate(all_scores)
labels = np.concatenate(all_labels)

# AUC
from sklearn.metrics import roc_auc_score, average_precision_score
auc = roc_auc_score(labels, scores)
ap = average_precision_score(labels, scores)
print(f"  AUC: {auc:.4f}")
print(f"  AP: {ap:.4f}")
print(f"  Top-100 anomalies recovery: {labels[np.argsort(-scores)[:100]].sum():.0f}/100")

summary = {
    "experiment": "bigae_production",
    "n_spectra": N_SPECTRA,
    "n_bins": N_BINS,
    "n_latent": N_LATENT,
    "n_params": n_params,
    "n_epochs": N_EPOCHS,
    "batch_size": BATCH_SIZE,
    "lr": LR,
    "best_val_loss": best_val,
    "final_train_loss": train_loss,
    "final_val_loss": val_loss,
    "auc": float(auc),
    "ap": float(ap),
    "history": history,
    "device": str(device),
    "elapsed_seconds": sum(history["epoch_time"]),
}
with open(os.path.join(OUTPUT_DIR, "summary.json"), "w") as f:
    json.dump(summary, f, indent=2)

# Save anomaly scores
np.savez(os.path.join(OUTPUT_DIR, "scores.npz"), scores=scores, labels=labels)

print(f"\n=== COMPLETE: {datetime.now()} ===")
tot = sum(history["epoch_time"])
print(f"  Total elapsed: {tot:.1f}s")
print(f"  Saved: {OUTPUT_DIR}/summary.json")
