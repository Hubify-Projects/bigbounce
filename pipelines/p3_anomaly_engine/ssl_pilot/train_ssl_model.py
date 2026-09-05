#!/usr/bin/env python3
"""Row12 pilot: train a small masked-spectrum transformer (<=20M params) on
the staged 496-bin normalized DESI DR1 science-target flux arrays.

Design (committed, seeded, deterministic):
  - Input: 496-bin flux vector, patchified into 31 patches of 16 bins.
  - Each patch linearly projected to `d_model`; a learned [MASK] embedding
    replaces masked patches (BERT/MAE-style); sinusoidal positional
    encoding added.
  - A small pre-norm Transformer encoder (`n_layers` layers, `n_heads`
    heads) processes the (masked) patch sequence.
  - A linear head reconstructs the ORIGINAL (unmasked) 16-bin patch value
    for every masked position; loss = MSE over masked patches only
    (standard masked-autoencoder objective).
  - Random masking ratio `mask_ratio` (default 0.4) applied fresh each
    forward pass (different mask each epoch/step -- not a fixed split).
  - Anomaly score (used downstream by embed_and_score.py) = per-object
    mean reconstruction MSE over masked patches, i.e. the model's
    surprise at this spectrum's shape -- same family of statistic as the
    archived BigAE's `mean_mse` reconstruction-error score, but produced
    by a model that was pretrained self-supervised rather than a fixed
    autoencoder with a pre-set architecture.

All hyperparameters + the seed are written to `--config-output` alongside
the checkpoint so the run is fully reproducible.
"""
from __future__ import annotations

import argparse
import glob
import json
import math
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
import pyarrow.parquet as pq

N_BINS = 496
PATCH = 16
N_PATCHES = N_BINS // PATCH  # 31


class MaskedSpectrumTransformer(nn.Module):
    def __init__(self, d_model=128, n_layers=4, n_heads=4, d_ff=256, dropout=0.1):
        super().__init__()
        self.d_model = d_model
        self.patch_embed = nn.Linear(PATCH, d_model)
        self.mask_token = nn.Parameter(torch.zeros(1, 1, d_model))
        pos = torch.zeros(N_PATCHES, d_model)
        position = torch.arange(0, N_PATCHES, dtype=torch.float32).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        pos[:, 0::2] = torch.sin(position * div_term)
        pos[:, 1::2] = torch.cos(position * div_term)
        self.register_buffer("pos_embed", pos.unsqueeze(0))

        layer = nn.TransformerEncoderLayer(
            d_model=d_model, nhead=n_heads, dim_feedforward=d_ff, dropout=dropout,
            batch_first=True, norm_first=True,
        )
        self.encoder = nn.TransformerEncoder(layer, num_layers=n_layers)
        self.head = nn.Linear(d_model, PATCH)

    def forward(self, x, mask_ratio=0.4):
        # x: (B, N_BINS) -> patches (B, N_PATCHES, PATCH)
        b = x.shape[0]
        patches = x.view(b, N_PATCHES, PATCH)
        emb = self.patch_embed(patches) + self.pos_embed

        n_mask = max(1, int(round(mask_ratio * N_PATCHES)))
        mask = torch.zeros(b, N_PATCHES, dtype=torch.bool, device=x.device)
        for i in range(b):
            idx = torch.randperm(N_PATCHES, device=x.device)[:n_mask]
            mask[i, idx] = True

        emb_masked = torch.where(mask.unsqueeze(-1), self.mask_token.expand(b, N_PATCHES, -1), emb)
        latent = self.encoder(emb_masked)  # (B, N_PATCHES, d_model)
        recon = self.head(latent)  # (B, N_PATCHES, PATCH)

        return recon, patches, mask, latent

    def embed(self, x):
        """Full (unmasked) forward pass for downstream embedding extraction."""
        b = x.shape[0]
        patches = x.view(b, N_PATCHES, PATCH)
        emb = self.patch_embed(patches) + self.pos_embed
        latent = self.encoder(emb)
        return latent.mean(dim=1)  # (B, d_model) pooled embedding


def count_params(model: nn.Module) -> int:
    return sum(p.numel() for p in model.parameters())


def load_flux_matrix(shard_glob: str) -> tuple[np.ndarray, list[int]]:
    paths = sorted(glob.glob(shard_glob))
    if not paths:
        raise RuntimeError(f"no shards matched {shard_glob}")
    fluxes = []
    targetids = []
    for p in paths:
        t = pq.read_table(p, columns=["targetid", "flux"])
        fluxes.extend(t.column("flux").to_pylist())
        targetids.extend(t.column("targetid").to_pylist())
    return np.asarray(fluxes, dtype=np.float32), targetids


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--shard-glob", required=True)
    ap.add_argument("--output-checkpoint", type=Path, required=True)
    ap.add_argument("--config-output", type=Path, required=True)
    ap.add_argument("--seed", type=int, default=20260904)
    ap.add_argument("--d-model", type=int, default=128)
    ap.add_argument("--n-layers", type=int, default=4)
    ap.add_argument("--n-heads", type=int, default=4)
    ap.add_argument("--d-ff", type=int, default=256)
    ap.add_argument("--mask-ratio", type=float, default=0.4)
    ap.add_argument("--batch-size", type=int, default=1024)
    ap.add_argument("--lr", type=float, default=3e-4)
    ap.add_argument("--max-seconds", type=float, default=7200.0, help="hard wall-clock budget")
    ap.add_argument("--val-fraction", type=float, default=0.05)
    args = ap.parse_args()

    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    X, targetids = load_flux_matrix(args.shard_glob)
    n = X.shape[0]
    rng = np.random.default_rng(args.seed)
    perm = rng.permutation(n)
    n_val = max(1, int(n * args.val_fraction))
    val_idx, train_idx = perm[:n_val], perm[n_val:]
    X_train, X_val = X[train_idx], X[val_idx]

    model = MaskedSpectrumTransformer(
        d_model=args.d_model, n_layers=args.n_layers, n_heads=args.n_heads, d_ff=args.d_ff
    ).to(device)
    n_params = count_params(model)
    if n_params > 20_000_000:
        raise RuntimeError(f"model has {n_params} params, exceeds the 20M budget")

    opt = torch.optim.AdamW(model.parameters(), lr=args.lr)
    X_train_t = torch.from_numpy(X_train)
    X_val_t = torch.from_numpy(X_val).to(device)

    t0 = time.time()
    epoch = 0
    history = []
    n_train = X_train_t.shape[0]
    while time.time() - t0 < args.max_seconds:
        model.train()
        idx = torch.randperm(n_train)
        epoch_loss = 0.0
        n_batches = 0
        for start in range(0, n_train, args.batch_size):
            if time.time() - t0 > args.max_seconds:
                break
            batch_idx = idx[start : start + args.batch_size]
            xb = X_train_t[batch_idx].to(device)
            recon, patches, mask, _ = model(xb, mask_ratio=args.mask_ratio)
            loss = ((recon - patches) ** 2)[mask].mean()
            opt.zero_grad()
            loss.backward()
            opt.step()
            epoch_loss += loss.item()
            n_batches += 1
        model.eval()
        with torch.no_grad():
            recon_v, patches_v, mask_v, _ = model(X_val_t, mask_ratio=args.mask_ratio)
            val_loss = ((recon_v - patches_v) ** 2)[mask_v].mean().item()
        history.append({"epoch": epoch, "train_loss": epoch_loss / max(1, n_batches), "val_loss": val_loss,
                         "elapsed_s": time.time() - t0})
        print(f"epoch {epoch}: train_loss={epoch_loss / max(1, n_batches):.5f} val_loss={val_loss:.5f} "
              f"elapsed={time.time()-t0:.0f}s", flush=True)
        epoch += 1

    ckpt_config = {
        "d_model": args.d_model, "n_layers": args.n_layers, "n_heads": args.n_heads,
        "d_ff": args.d_ff, "mask_ratio": args.mask_ratio, "seed": args.seed,
    }
    args.output_checkpoint.parent.mkdir(parents=True, exist_ok=True)
    torch.save({"model_state": model.state_dict(), "config": ckpt_config}, args.output_checkpoint)

    config = {
        **{k: v for k, v in vars(args).items() if k not in ("output_checkpoint", "config_output")},
        "output_checkpoint": str(args.output_checkpoint),
        "n_params": n_params,
        "n_train": int(n_train),
        "n_val": int(n_val),
        "n_epochs_completed": epoch,
        "wall_clock_seconds": time.time() - t0,
        "history": history,
        "device": str(device),
        "architecture": "masked-spectrum-transformer",
        "n_bins": N_BINS,
        "patch_size": PATCH,
        "n_patches": N_PATCHES,
    }
    args.config_output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.config_output, "w") as fh:
        json.dump(config, fh, indent=2)
    print(f"DONE: {n_params} params, {epoch} epochs, {time.time()-t0:.0f}s -> {args.output_checkpoint}")


if __name__ == "__main__":
    main()
