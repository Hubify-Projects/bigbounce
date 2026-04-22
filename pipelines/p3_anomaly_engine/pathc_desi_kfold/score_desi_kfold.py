#!/usr/bin/env python3
"""
DESI 5-Fold Scoring Driver — P3-PATHC-DESI-KFOLD (criterion #4)
================================================================
For each of the 5 fold checkpoints produced by `train_desi_kfold.py`, score
the full DESI DR1 catalog and write one parquet per fold with columns
(source_id, ra, dec, anomaly_score). These 5 parquets are the input to
`aggregate_kfold.py`, which computes the cross-fold Jaccard stability metric
that gates Path-C criterion #4.

See `desi_kfold_plan.md` Step 3 for the full protocol.

Launch (on pod, after train_desi_kfold.py produces 5 fold_k/best.pt):
    cd /workspace/bigbounce_scan
    python3 pipelines/p3_anomaly_engine/pathc_desi_kfold/score_desi_kfold.py \\
        --checkpoints-dir /workspace/bigbounce_scan/outputs/desi_kfold \\
        --full-catalog-shards /workspace/bigbounce_scan/outputs/desi/full_dr1_shards \\
        --metadata-parquet /workspace/bigbounce_scan/outputs/desi/dr1_metadata.parquet \\
        --output-dir /workspace/bigbounce_scan/outputs/desi_kfold/scores \\
        --batch-size 8192 --num-workers 16

Expected wall-clock: ~25 min per fold × 5 folds = ~2.1 GPU-h on A100.
Resume-friendly: fold_{k}_scores.parquet files already present are skipped.

Input schema:
- `--full-catalog-shards` directory of .npy files, each shape (n_shard, 496)
  with spectra already pre-processed to the same 496-bin BigAE input format
  used during training. Shards must be sorted for deterministic row order.
- `--metadata-parquet` single parquet with per-row metadata aligned to the
  concatenated-shard row order. Required columns: source_id, ra, dec.

Output schema (per fold):
- `fold_{k}_scores.parquet` with columns (source_id: str, ra: float64,
  dec: float64, anomaly_score: float32).
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset


# ============================================================
# BigAE — identical to the published DESI architecture
# (mirrors train_desi_kfold.py L38-55)
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


def load_full_catalog(shard_dir: Path) -> np.ndarray:
    """Load the full preprocessed DR1 catalog from per-shard .npy files."""
    shards = sorted(shard_dir.glob('*.npy'))
    if not shards:
        raise SystemExit(f'no shards found under {shard_dir}')
    parts = [np.load(s) for s in shards]
    X = np.concatenate(parts, axis=0).astype(np.float32)
    # Sanitize — mirror the training driver's NaN/Inf handling.
    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
    print(f'[load] {len(X):,} spectra from {len(shards)} shards')
    return X


def load_metadata(metadata_path: Path, n_expected: int) -> pd.DataFrame:
    meta = pd.read_parquet(metadata_path)
    required = {'source_id', 'ra', 'dec'}
    missing = required - set(meta.columns)
    if missing:
        raise SystemExit(f'metadata parquet missing columns: {sorted(missing)}')
    if len(meta) != n_expected:
        raise SystemExit(
            f'metadata row count {len(meta):,} != spectra row count {n_expected:,} — '
            f'shard/metadata row order must match exactly'
        )
    return meta[['source_id', 'ra', 'dec']].reset_index(drop=True)


def score_one_fold(
    fold_id: int,
    ckpt_path: Path,
    X: np.ndarray,
    meta: pd.DataFrame,
    out_path: Path,
    batch_size: int,
    num_workers: int,
    device: torch.device,
) -> dict:
    """Load a fold checkpoint and score the full catalog."""
    if out_path.exists():
        print(f'[fold {fold_id}] {out_path.name} exists, skipping')
        df = pd.read_parquet(out_path)
        return {
            'fold_id': fold_id,
            'output': str(out_path),
            'n_rows': int(len(df)),
            'status': 'skipped_existing',
        }

    t0 = time.time()
    model = BigAE(n_in=X.shape[1], n_lat=128).to(device)
    state = torch.load(ckpt_path, map_location=device)
    model.load_state_dict(state)
    model.eval()

    # GPU inference playbook rule (CLAUDE.md): DataLoader num_workers=16
    # pin_memory=True prefetch_factor=4 for 32x speedup over serial.
    X_tensor = torch.from_numpy(X).float()
    ds = TensorDataset(X_tensor)
    loader = DataLoader(
        ds,
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers,
        pin_memory=(device.type == 'cuda'),
        prefetch_factor=4 if num_workers > 0 else None,
    )

    scores = np.empty(len(X), dtype=np.float32)
    cursor = 0
    with torch.no_grad():
        for (xb,) in loader:
            xb = xb.to(device, non_blocking=True)
            pred = model(xb)
            # Anomaly score = per-row reconstruction MSE (matches the scoring
            # convention used throughout Paper 3's anomaly pipeline).
            row_mse = ((pred - xb) ** 2).mean(dim=1).cpu().numpy()
            n = len(row_mse)
            scores[cursor:cursor + n] = row_mse
            cursor += n
    assert cursor == len(X), f'row count mismatch: scored {cursor} of {len(X)}'

    out_df = meta.copy()
    out_df['anomaly_score'] = scores
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_df.to_parquet(out_path, index=False)

    stats = {
        'fold_id': fold_id,
        'checkpoint': str(ckpt_path),
        'output': str(out_path),
        'n_rows': int(len(out_df)),
        'score_p50': float(np.median(scores)),
        'score_p99': float(np.percentile(scores, 99)),
        'score_p99_9': float(np.percentile(scores, 99.9)),
        'score_max': float(np.max(scores)),
        'wall_time_s': float(time.time() - t0),
        'status': 'scored',
    }
    print(
        f'[fold {fold_id}] DONE {len(out_df):,} rows  '
        f'p50={stats["score_p50"]:.4f}  p99={stats["score_p99"]:.4f}  '
        f'max={stats["score_max"]:.2f}  ({stats["wall_time_s"]:.0f}s)'
    )
    return stats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--checkpoints-dir', type=Path, required=True,
                    help='directory with fold_{0..4}/best.pt from train_desi_kfold.py')
    ap.add_argument('--full-catalog-shards', type=Path, required=True,
                    help='directory of .npy shards covering the full DR1 catalog')
    ap.add_argument('--metadata-parquet', type=Path, required=True,
                    help='parquet aligned to shard row order with source_id, ra, dec')
    ap.add_argument('--output-dir', type=Path, required=True,
                    help='destination for fold_{k}_scores.parquet')
    ap.add_argument('--n-folds', type=int, default=5)
    ap.add_argument('--batch-size', type=int, default=8192)
    ap.add_argument('--num-workers', type=int, default=16,
                    help='DataLoader workers — 16 is the CLAUDE.md GPU-playbook value')
    args = ap.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'[main] device={device}  torch={torch.__version__}')

    X = load_full_catalog(args.full_catalog_shards)
    meta = load_metadata(args.metadata_parquet, n_expected=len(X))

    results = []
    for fi in range(args.n_folds):
        ckpt = args.checkpoints_dir / f'fold_{fi}' / 'best.pt'
        if not ckpt.exists():
            raise SystemExit(f'missing checkpoint: {ckpt}')
        out_path = args.output_dir / f'fold_{fi}_scores.parquet'
        res = score_one_fold(
            fold_id=fi, ckpt_path=ckpt, X=X, meta=meta, out_path=out_path,
            batch_size=args.batch_size, num_workers=args.num_workers, device=device,
        )
        results.append(res)

    summary = {
        'task': 'P3-PATHC-DESI-KFOLD (criterion #4) — scoring phase',
        'n_folds': args.n_folds,
        'n_rows_scored': int(len(X)),
        'batch_size': args.batch_size,
        'num_workers': args.num_workers,
        'per_fold': results,
    }
    with open(args.output_dir / 'scoring_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)
    print(f'[main] wrote {args.output_dir}/scoring_summary.json  '
          f'({args.n_folds} folds × {len(X):,} rows each)')


if __name__ == '__main__':
    main()
