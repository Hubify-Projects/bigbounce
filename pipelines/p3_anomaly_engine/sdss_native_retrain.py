#!/usr/bin/env python3
"""
SDSS DR18 Native BigAE Retrain — P3-PATHC-SDSS-NATIVE-RETRAIN
==============================================================
Trains a BigAE-class autoencoder natively on SDSS DR18 spectra (no cross-transfer
from the DESI-trained model). This is the quality-ceiling path under Houston's
Path C directive (2026-04-19): eliminate catalog-cross-calibration artifacts by
retraining on the target survey's own spectra.

Pipeline:
  1. Load spAll-v5_13_2.fits (already on pod at temp/sdss/spAll-v5_13_2.fits).
  2. Apply quality cuts: ZWARNING==0, SN_MEDIAN_ALL>2, CLASS in {STAR,GALAXY,QSO},
     SPECPRIMARY==1. Random-sample ~300K training candidates.
  3. Download + preprocess spectra in parallel (ThreadPoolExecutor, 32 workers).
     Each preprocessed spectrum = 496-bin DESI-grid resampled, median-normalized.
     Cache as shards of 5,000 under temp/sdss_native/shards/*.npy (resumable).
  4. Once >= 200K preprocessed spectra are on disk, train BigAE(n_in=496, n_lat=128)
     for up to 40 epochs with Adam lr=1e-3, MSE loss, 90/10 train/val split.
     Target: val_loss <= 0.30 (matches DESI BigAE's ~0.25 for comparability).
  5. Save best checkpoint to outputs/sdss_native/best_sdss_native.pt.
  6. Log per-epoch metrics to outputs/sdss_native/training_log.json.

Exit criteria gate (Path C #1): val_loss <= 0.30 AND at least one retrain attempt
completed. After training, a follow-up fire re-scores all 2.3M SDSS spectra with
the native model to produce the native SDSS anomaly set.

Run:
    python3 sdss_native_retrain.py --target-count 300000 --max-epochs 40

Resume-friendly: re-running skips shards already on disk.
"""

import argparse
import json
import os
import random
import time
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from astropy.io import fits

# ============================================================
# Config
# ============================================================
DESI_WMIN, DESI_WMAX = 3600.0, 9800.0
N_BINS = 496
SHARD_SIZE = 5000
DOWNLOAD_BASE = "https://data.sdss.org/sas/dr18/spectro/sdss/redux/v5_13_2/spectra/lite"

DEFAULTS = dict(
    spall_path="/workspace/bigbounce_scan/temp/sdss/spAll-v5_13_2.fits",
    shard_dir="/workspace/bigbounce_scan/temp/sdss_native/shards",
    spec_cache_dir="/workspace/bigbounce_scan/temp/sdss_native/raw_specs",
    output_dir="/workspace/bigbounce_scan/outputs/sdss_native",
    target_count=300000,
    max_epochs=40,
    batch_size=512,
    lr=1e-3,
    patience=5,
    val_frac=0.1,
    dl_workers=32,
    seed=20260419,
)


# ============================================================
# BigAE (same architecture as DESI-trained model)
# ============================================================
class BigAE(nn.Module):
    def __init__(self, n_in=496, n_lat=128):
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

    def forward(self, x):
        return self.dec(self.enc(x))


# ============================================================
# Spectrum preprocessing — SDSS -> 496-bin DESI grid, median-normalized
# ============================================================
def resample_to_desi(sdss_wave, sdss_flux, sdss_ivar=None):
    desi_wave = np.linspace(DESI_WMIN, DESI_WMAX, N_BINS)
    step = (DESI_WMAX - DESI_WMIN) / N_BINS
    resampled = np.zeros(N_BINS, dtype=np.float32)
    for i in range(N_BINS):
        lo, hi = desi_wave[i] - step / 2, desi_wave[i] + step / 2
        mask = (sdss_wave >= lo) & (sdss_wave < hi)
        if np.any(mask):
            if sdss_ivar is not None:
                w = sdss_ivar[mask].clip(min=0)
                if w.sum() > 0:
                    resampled[i] = np.average(sdss_flux[mask], weights=w)
                else:
                    resampled[i] = sdss_flux[mask].mean()
            else:
                resampled[i] = sdss_flux[mask].mean()
    nz = resampled[resampled != 0]
    if nz.size > 0:
        med = np.median(nz)
        if med > 0:
            resampled /= med
    return resampled


def fetch_and_preprocess(plate, mjd, fiberid, cache_dir):
    """Download one SDSS lite spec, preprocess to 496-bin normalized flux."""
    url = f"{DOWNLOAD_BASE}/{plate:04d}/spec-{plate:04d}-{mjd}-{fiberid:04d}.fits"
    local = Path(cache_dir) / f"spec-{plate:04d}-{mjd}-{fiberid:04d}.fits"
    if not local.exists():
        import urllib.request
        req = urllib.request.Request(url, headers={"User-Agent": "bigbounce-pathc/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r, open(local, "wb") as f:
                f.write(r.read())
        except Exception:
            return None
    try:
        with fits.open(local, memmap=False) as hdul:
            data = hdul[1].data
            loglam = data["loglam"]
            wave = 10 ** loglam
            flux = data["flux"].astype(np.float32)
            ivar = data["ivar"].astype(np.float32)
        arr = resample_to_desi(wave, flux, ivar)
        if np.isnan(arr).any() or np.isinf(arr).any():
            return None
        # Reject flat / all-zero spectra
        if arr.std() < 1e-3:
            return None
        return arr
    except Exception:
        return None
    finally:
        # Free disk — we already have the preprocessed vector cached per-shard
        try:
            local.unlink(missing_ok=True)
        except Exception:
            pass


# ============================================================
# Step 1 — select training candidates from spAll
# ============================================================
def select_candidates(spall_path, target_count, seed):
    print(f"[select] Loading spAll from {spall_path}...")
    with fits.open(spall_path, memmap=True) as hdul:
        t = hdul[1].data
        n = len(t)
        print(f"[select]   rows: {n:,}")
        cols = set(t.dtype.names)
        zw = t["ZWARNING"]
        sn_col = "SN_MEDIAN_ALL" if "SN_MEDIAN_ALL" in cols else ("SN_MEDIAN" if "SN_MEDIAN" in cols else None)
        if sn_col is None:
            # Fallback: PLATESN2 is roughly comparable for plate-level quality; accept all
            print("[select]   WARN: no SN_MEDIAN_ALL or SN_MEDIAN column found; skipping S/N cut")
            sn = np.full(len(t), 99.0, dtype=np.float32)
        else:
            sn = t[sn_col]
            # SDSS v5_13_2 stores SN_MEDIAN as a 4-vector per plate (one per band); take max
            if sn.ndim > 1:
                sn = sn.max(axis=1)
        klass = np.array([c.strip() for c in t["CLASS"]])
        specprim = t["SPECPRIMARY"]
        mask = (zw == 0) & (sn > 2.0) & (specprim == 1) & np.isin(klass, ["STAR", "GALAXY", "QSO"])
        idx = np.where(mask)[0]
        print(f"[select]   candidates after quality cuts: {len(idx):,}")
        rng = np.random.default_rng(seed)
        if len(idx) > target_count:
            idx = rng.choice(idx, size=target_count, replace=False)
        plate = t["PLATE"][idx].astype(int)
        mjd = t["MJD"][idx].astype(int)
        fiber = t["FIBERID"][idx].astype(int)
        klass_sel = klass[idx]
    print(f"[select]   selected: {len(idx):,}")
    # Class balance diagnostic
    unique, counts = np.unique(klass_sel, return_counts=True)
    for u, c in zip(unique, counts):
        print(f"[select]     {u}: {c:,} ({100*c/len(idx):.1f}%)")
    return list(zip(plate, mjd, fiber, klass_sel))


# ============================================================
# Step 2 — parallel download + preprocess into shards
# ============================================================
def already_sharded_count(shard_dir):
    shard_dir = Path(shard_dir)
    shard_dir.mkdir(parents=True, exist_ok=True)
    total = 0
    for f in sorted(shard_dir.glob("shard_*.npy")):
        try:
            a = np.load(f, mmap_mode="r")
            total += a.shape[0]
        except Exception:
            continue
    return total


def build_shards(candidates, shard_dir, cache_dir, workers):
    shard_dir = Path(shard_dir)
    cache_dir = Path(cache_dir)
    shard_dir.mkdir(parents=True, exist_ok=True)
    cache_dir.mkdir(parents=True, exist_ok=True)

    existing = sorted(shard_dir.glob("shard_*.npy"))
    start_idx = len(existing)
    existing_count = already_sharded_count(shard_dir)
    print(f"[shard] existing shards: {start_idx}, existing spectra: {existing_count:,}")

    # Skip past candidates already in existing shards
    candidates = candidates[existing_count:]
    print(f"[shard] to-download: {len(candidates):,}")

    buffer = []
    buffer_classes = []
    shard_id = start_idx
    t_start = time.time()
    success = 0
    failed = 0

    def task(rec):
        p, m, f, k = rec
        arr = fetch_and_preprocess(p, m, f, cache_dir)
        return arr, k, (p, m, f)

    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(task, rec): rec for rec in candidates}
        for i, fut in enumerate(as_completed(futs)):
            arr, klass, pmf = fut.result()
            if arr is None:
                failed += 1
            else:
                buffer.append(arr)
                buffer_classes.append(klass)
                success += 1
            if len(buffer) >= SHARD_SIZE:
                shard_path = shard_dir / f"shard_{shard_id:05d}.npy"
                class_path = shard_dir / f"shard_{shard_id:05d}_class.npy"
                np.save(shard_path, np.stack(buffer).astype(np.float32))
                np.save(class_path, np.array(buffer_classes))
                print(f"[shard] wrote {shard_path.name} ({len(buffer)} specs) — total success={success:,} failed={failed:,} elapsed={time.time()-t_start:.0f}s")
                buffer = []
                buffer_classes = []
                shard_id += 1
            if (i + 1) % 2000 == 0:
                rate = success / max(1.0, time.time() - t_start)
                print(f"[shard] progress {i+1:,}/{len(candidates):,} success={success:,} failed={failed:,} rate={rate:.1f}/s")

    if buffer:
        shard_path = shard_dir / f"shard_{shard_id:05d}.npy"
        class_path = shard_dir / f"shard_{shard_id:05d}_class.npy"
        np.save(shard_path, np.stack(buffer).astype(np.float32))
        np.save(class_path, np.array(buffer_classes))
        print(f"[shard] wrote final {shard_path.name} ({len(buffer)} specs)")

    print(f"[shard] DONE — success={success:,} failed={failed:,} elapsed={time.time()-t_start:.0f}s")


# ============================================================
# Step 3 — train BigAE
# ============================================================
def load_all_shards(shard_dir):
    shard_dir = Path(shard_dir)
    parts = []
    for f in sorted(shard_dir.glob("shard_*.npy")):
        if f.name.endswith("_class.npy"):
            continue
        parts.append(np.load(f, mmap_mode="r"))
    if not parts:
        raise RuntimeError(f"No shards in {shard_dir}")
    return np.concatenate(parts, axis=0)


def train(args):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[train] device={device}")
    if torch.cuda.is_available():
        print(f"[train] GPU: {torch.cuda.get_device_name(0)}")

    data = load_all_shards(args.shard_dir)
    n = data.shape[0]
    print(f"[train] total spectra: {n:,} shape={data.shape}")
    if n < 50000:
        print(f"[train] WARN: only {n:,} spectra — quality will be degraded. Proceeding.")

    rng = np.random.default_rng(args.seed)
    perm = rng.permutation(n)
    n_val = int(n * args.val_frac)
    val_idx = perm[:n_val]
    train_idx = perm[n_val:]

    data_t = torch.from_numpy(np.ascontiguousarray(data)).float()
    train_t = data_t[train_idx]
    val_t = data_t[val_idx].to(device)
    print(f"[train] train={len(train_t):,} val={len(val_t):,}")

    model = BigAE(n_in=N_BINS, n_lat=128).to(device)
    opt = torch.optim.Adam(model.parameters(), lr=args.lr)
    loss_fn = nn.MSELoss()

    log = {
        "config": {k: (v if isinstance(v, (int, float, str, bool)) else str(v))
                   for k, v in vars(args).items()},
        "n_train": len(train_t),
        "n_val": len(val_t),
        "epochs": [],
        "best_val_loss": float("inf"),
        "best_epoch": None,
        "started_at": time.time(),
    }

    best_val = float("inf")
    best_state = None
    patience_ctr = 0
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    ckpt_path = out_dir / "best_sdss_native.pt"

    for epoch in range(args.max_epochs):
        model.train()
        perm_ep = torch.randperm(len(train_t))
        train_loss = 0.0
        n_seen = 0
        for i in range(0, len(train_t), args.batch_size):
            batch = train_t[perm_ep[i:i + args.batch_size]].to(device, non_blocking=True)
            opt.zero_grad()
            recon = model(batch)
            loss = loss_fn(recon, batch)
            loss.backward()
            opt.step()
            train_loss += loss.item() * batch.size(0)
            n_seen += batch.size(0)
        train_loss /= n_seen

        model.eval()
        with torch.no_grad():
            val_loss = 0.0
            for i in range(0, len(val_t), args.batch_size):
                batch = val_t[i:i + args.batch_size]
                recon = model(batch)
                val_loss += loss_fn(recon, batch).item() * batch.size(0)
            val_loss /= len(val_t)

        print(f"[train] epoch {epoch+1:02d}/{args.max_epochs}  train={train_loss:.4f}  val={val_loss:.4f}  best_val={best_val:.4f}")
        log["epochs"].append({"epoch": epoch + 1, "train_loss": train_loss, "val_loss": val_loss})

        if val_loss < best_val - 1e-4:
            best_val = val_loss
            best_state = {k: v.detach().cpu().clone() for k, v in model.state_dict().items()}
            torch.save(best_state, ckpt_path)
            log["best_val_loss"] = best_val
            log["best_epoch"] = epoch + 1
            patience_ctr = 0
            print(f"[train]   -> new best, saved to {ckpt_path}")
        else:
            patience_ctr += 1
            if patience_ctr >= args.patience:
                print(f"[train] early stop at epoch {epoch+1} (patience={args.patience})")
                break

        # Flush log every epoch
        with open(out_dir / "training_log.json", "w") as f:
            json.dump(log, f, indent=2)

    log["finished_at"] = time.time()
    log["duration_s"] = log["finished_at"] - log["started_at"]
    log["passes_gate_0p30"] = bool(log["best_val_loss"] <= 0.30)
    with open(out_dir / "training_log.json", "w") as f:
        json.dump(log, f, indent=2)
    print(f"[train] DONE — best_val={best_val:.4f} gate_0.30={'PASS' if best_val<=0.30 else 'FAIL'} duration={log['duration_s']:.0f}s")


# ============================================================
# Main
# ============================================================
def main():
    ap = argparse.ArgumentParser()
    for k, v in DEFAULTS.items():
        ap.add_argument(f"--{k.replace('_', '-')}", type=type(v), default=v)
    ap.add_argument("--skip-shard-build", action="store_true",
                    help="Skip download/preprocess phase; train on existing shards only.")
    ap.add_argument("--skip-train", action="store_true",
                    help="Only build shards; don't train yet.")
    args = ap.parse_args()

    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)

    print("=" * 70)
    print("SDSS DR18 NATIVE BIGAE RETRAIN — P3-PATHC-SDSS-NATIVE-RETRAIN")
    print("=" * 70)
    print(f"target_count={args.target_count:,}  max_epochs={args.max_epochs}  workers={args.dl_workers}")

    if not args.skip_shard_build:
        candidates = select_candidates(args.spall_path, args.target_count, args.seed)
        build_shards(candidates, args.shard_dir, args.spec_cache_dir, args.dl_workers)

    existing = already_sharded_count(args.shard_dir)
    print(f"[main] shards on disk represent {existing:,} preprocessed spectra")

    if args.skip_train:
        print("[main] --skip-train set; exiting.")
        return

    if existing < 50000:
        print(f"[main] only {existing:,} spectra — below minimum 50K floor. Exiting; re-run to continue downloads.")
        return

    train(args)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("[fatal]", traceback.format_exc())
        raise
