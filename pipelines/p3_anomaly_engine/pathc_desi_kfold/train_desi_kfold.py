#!/usr/bin/env python3
"""
DESI 5-Fold Training Driver — P3-PATHC-DESI-KFOLD (criterion #4)
================================================================
Trains 5 independent BigAE models on disjoint 80% folds of the published
DESI 47K training sample. Each fold's holdout (20%) is untouched during
training and used only for holdout-score reporting, which feeds the
cross-fold Jaccard analysis run by `aggregate_kfold.py`.

See `desi_kfold_plan.md` for the full protocol and gate criteria.

Launch (on pod, after SDSS + LAMOST native rescores finish):
    cd /workspace/bigbounce_scan
    python3 pipelines/p3_anomaly_engine/pathc_desi_kfold/train_desi_kfold.py \\
        --training-shards /workspace/bigbounce_scan/outputs/desi/training_shards \\
        --output-dir /workspace/bigbounce_scan/outputs/desi_kfold \\
        --n-folds 5 --max-epochs 40 --seed 20260420

Resume-friendly: fold_{k}/best.pt checkpoints that already exist are skipped.
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset


# ============================================================
# BigAE — identical to the published DESI architecture
# (see pipelines/p3_anomaly_engine/sdss_native_retrain.py L77-92)
# ============================================================
class BigAE(nn.Module):
    def __init__(self, n_in: int = 496, n_lat: int = 128):
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

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.dec(self.enc(x))


def load_training_spectra(shard_dir: Path) -> np.ndarray:
    """Load the published DESI 47K training sample from per-shard .npy files."""
    shards = sorted(shard_dir.glob('*.npy'))
    if not shards:
        raise SystemExit(f'no shards found under {shard_dir}')
    parts = [np.load(s) for s in shards]
    X = np.concatenate(parts, axis=0).astype(np.float32)
    # Reject any rows with NaN / Inf that slipped through preprocessing
    ok = np.isfinite(X).all(axis=1)
    X = X[ok]
    print(f'[load] {len(X):,} spectra from {len(shards)} shards (dropped {int((~ok).sum())} non-finite)')
    return X


def split_folds(n_rows: int, n_folds: int, seed: int) -> list[np.ndarray]:
    """Deterministic K-fold split over shuffled indices."""
    rng = np.random.default_rng(seed)
    idx = rng.permutation(n_rows)
    folds = np.array_split(idx, n_folds)
    return [f.copy() for f in folds]


def train_one_fold(
    fold_id: int,
    X: np.ndarray,
    train_idx: np.ndarray,
    holdout_idx: np.ndarray,
    out_dir: Path,
    max_epochs: int,
    batch_size: int,
    lr: float,
    patience: int,
    val_frac: float,
    device: torch.device,
    gate_val_loss: float,
) -> dict:
    """Train a single fold and return a result dict."""
    fold_dir = out_dir / f'fold_{fold_id}'
    fold_dir.mkdir(parents=True, exist_ok=True)
    ckpt_path = fold_dir / 'best.pt'
    log_path = fold_dir / 'training_log.json'
    if ckpt_path.exists() and log_path.exists():
        print(f'[fold {fold_id}] checkpoint exists, skipping')
        with open(log_path) as f:
            return json.load(f)

    # 90/10 train/inside-val split *within* train_idx
    rng = np.random.default_rng(20260420 + fold_id)
    shuf = rng.permutation(train_idx)
    n_val = max(1, int(val_frac * len(shuf)))
    inside_val_idx = shuf[:n_val]
    inside_train_idx = shuf[n_val:]

    X_tr = torch.from_numpy(X[inside_train_idx]).float()
    X_va = torch.from_numpy(X[inside_val_idx]).float()
    X_ho = torch.from_numpy(X[holdout_idx]).float()

    tr_ds = TensorDataset(X_tr)
    tr_loader = DataLoader(tr_ds, batch_size=batch_size, shuffle=True, num_workers=4, pin_memory=True)

    model = BigAE(n_in=X.shape[1], n_lat=128).to(device)
    opt = torch.optim.Adam(model.parameters(), lr=lr)
    loss_fn = nn.MSELoss()

    best_val = float('inf')
    best_epoch = -1
    bad_epochs = 0
    history = []
    t0 = time.time()

    for epoch in range(max_epochs):
        model.train()
        tr_losses = []
        for (xb,) in tr_loader:
            xb = xb.to(device, non_blocking=True)
            opt.zero_grad()
            pred = model(xb)
            loss = loss_fn(pred, xb)
            loss.backward()
            opt.step()
            tr_losses.append(float(loss.detach().cpu()))
        tr_loss = float(np.mean(tr_losses))

        model.eval()
        with torch.no_grad():
            va_pred = model(X_va.to(device))
            va_loss = float(loss_fn(va_pred, X_va.to(device)).cpu())
        history.append({'epoch': epoch, 'train_loss': tr_loss, 'val_loss': va_loss})
        print(f'[fold {fold_id}] epoch {epoch:03d}  train {tr_loss:.4f}  val {va_loss:.4f}')

        if va_loss < best_val:
            best_val = va_loss
            best_epoch = epoch
            torch.save(model.state_dict(), ckpt_path)
            bad_epochs = 0
        else:
            bad_epochs += 1
            if bad_epochs >= patience:
                print(f'[fold {fold_id}] early-stop at epoch {epoch} (best val={best_val:.4f} @ epoch {best_epoch})')
                break

    # Holdout report — reload best checkpoint + score the untouched fold
    model.load_state_dict(torch.load(ckpt_path, map_location=device))
    model.eval()
    with torch.no_grad():
        ho_pred = model(X_ho.to(device))
        ho_mse_per_row = ((ho_pred - X_ho.to(device)) ** 2).mean(dim=1).cpu().numpy()
    holdout_stats = {
        'n_holdout': int(len(holdout_idx)),
        'holdout_mse_p50': float(np.median(ho_mse_per_row)),
        'holdout_mse_p90': float(np.percentile(ho_mse_per_row, 90)),
        'holdout_mse_p99': float(np.percentile(ho_mse_per_row, 99)),
    }

    result = {
        'fold_id': fold_id,
        'n_inside_train': int(len(inside_train_idx)),
        'n_inside_val': int(len(inside_val_idx)),
        'n_holdout': int(len(holdout_idx)),
        'best_val_loss': float(best_val),
        'best_epoch': int(best_epoch),
        'gate_val_loss': gate_val_loss,
        'gate_pass': bool(best_val <= gate_val_loss),
        'holdout': holdout_stats,
        'wall_time_s': float(time.time() - t0),
        'history': history,
    }
    with open(log_path, 'w') as f:
        json.dump(result, f, indent=2)
    print(f'[fold {fold_id}] DONE best_val={best_val:.4f} gate_pass={result["gate_pass"]} '
          f'holdout_p99={holdout_stats["holdout_mse_p99"]:.4f} ({result["wall_time_s"]:.0f}s)')
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--training-shards', type=Path, required=True,
                    help='directory holding the published DESI 47K training .npy shards')
    ap.add_argument('--output-dir', type=Path, required=True,
                    help='destination for fold_{k}/best.pt + training_log.json')
    ap.add_argument('--n-folds', type=int, default=5)
    ap.add_argument('--max-epochs', type=int, default=40)
    ap.add_argument('--batch-size', type=int, default=512)
    ap.add_argument('--lr', type=float, default=1e-3)
    ap.add_argument('--patience', type=int, default=5)
    ap.add_argument('--val-frac', type=float, default=0.1)
    ap.add_argument('--seed', type=int, default=20260420)
    ap.add_argument('--gate-val-loss', type=float, default=0.30,
                    help='Path-C gate — same threshold as SDSS/LAMOST native retrains')
    args = ap.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'[main] device={device}  torch={torch.__version__}')

    X = load_training_spectra(args.training_shards)
    folds = split_folds(len(X), args.n_folds, args.seed)
    print(f'[main] {args.n_folds}-fold split: sizes={[len(f) for f in folds]}')

    results = []
    for fi, holdout_idx in enumerate(folds):
        train_idx = np.concatenate([folds[j] for j in range(args.n_folds) if j != fi])
        res = train_one_fold(
            fold_id=fi, X=X, train_idx=train_idx, holdout_idx=holdout_idx,
            out_dir=args.output_dir,
            max_epochs=args.max_epochs, batch_size=args.batch_size,
            lr=args.lr, patience=args.patience, val_frac=args.val_frac,
            device=device, gate_val_loss=args.gate_val_loss,
        )
        results.append(res)

    # Cross-fold summary
    summary = {
        'task': 'P3-PATHC-DESI-KFOLD (criterion #4) — training phase',
        'n_folds': args.n_folds,
        'seed': args.seed,
        'gate_val_loss': args.gate_val_loss,
        'per_fold': results,
        'best_val_mean': float(np.mean([r['best_val_loss'] for r in results])),
        'best_val_std': float(np.std([r['best_val_loss'] for r in results])),
        'all_folds_pass_gate': bool(all(r['gate_pass'] for r in results)),
    }
    with open(args.output_dir / 'training_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)
    print(f'[main] wrote {args.output_dir}/training_summary.json  '
          f'mean_val={summary["best_val_mean"]:.4f} ± {summary["best_val_std"]:.4f}  '
          f'all_pass={summary["all_folds_pass_gate"]}')


if __name__ == '__main__':
    main()
