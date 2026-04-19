#!/usr/bin/env python3
"""
LAMOST DR10 native BigAE retrain — P3-PATHC-LAMOST-NATIVE-RETRAIN

Drive-to-100 Phase 2 Path C task 2/7.

Pipeline
--------
1. Fetch LAMOST DR10 LRS per-night tar list from
   http://www.lamost.org/dr10/v2.0/tar/lrs-fits/
2. Randomly sample ~50 nights (seed=20260419) → ~300K spectra training pool.
3. For each sampled night:
     - download the night tarball (~325 MB avg) to /workspace/bigbounce_scan/temp/lamost_native/tars/
     - iterate members, preprocess each .fits.gz in-memory (gzip -> astropy),
       resample to 496-bin DESI grid (3600-9800 Å) via np.interp, median-normalize
     - stream preprocessed vectors into 5,000-spec shards on disk, tag per-spectrum CLASS
     - delete the tarball after processing (disk hygiene)
4. Once ≥ 50K shards cached, train BigAE(n_in=496, n_lat=128) on all shards — Adam lr=1e-3,
   batch=512, 90/10 train-val split, ≤ 40 epochs, patience=5, MSE reconstruction loss.
5. Output: `best_lamost_native.pt` + `training_log.json` with per-epoch val_loss; gate
   PASS if val_loss ≤ 0.30.

Design goals
------------
* Resumable: existing shards skipped on re-launch; tarballs already processed
  (present in `.processed_nights.txt`) skipped.
* Parallel-safe: does NOT touch the existing `lamost` tmux (cross-transfer §7.1
  baseline); uses an isolated `/workspace/bigbounce_scan/temp/lamost_native/`
  subtree so no path collision.
* Network-polite: one tarball at a time (single-threaded download), matches
  cross-transfer scan bandwidth profile.

Bugs-caught-before-launch log
-----------------------------
* SDSS sibling (fire #78) had /redux/26/ vs /redux/v5_13_2/ URL mismatch — we
  ALREADY use the cross-transfer scan's known-working `.lamost.org/dr10/v2.0/tar/lrs-fits/`
  base URL, so no analogous fix should be needed.
"""
from __future__ import annotations

import gzip
import io
import json
import random
import re
import tarfile
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from astropy.io import fits


# ============================================================
# Config
# ============================================================
WMIN, WMAX = 3600.0, 9800.0
N_BINS = 496
DESI_WAVE = np.linspace(WMIN, WMAX, N_BINS).astype(np.float32)
SHARD_SIZE = 5000
TAR_BASE = "http://www.lamost.org/dr10/v2.0/tar/lrs-fits"

DEFAULTS = dict(
    base_dir="/workspace/bigbounce_scan/temp/lamost_native",
    output_dir="/workspace/bigbounce_scan/outputs/lamost_native",
    target_count=300_000,
    num_nights=50,       # 50 × ~6_500 = ~325K spectra, head-truncated to target_count
    max_epochs=40,
    batch_size=512,
    lr=1e-3,
    patience=5,
    val_frac=0.1,
    extract_workers=16,  # threads for in-memory gzip+fits decode per tarball
    seed=20260419,
)


# ============================================================
# BigAE (identical to DESI-trained and SDSS native retrain)
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
# Preprocess one LAMOST spectrum (bytes of .fits.gz)
# ============================================================
def read_one_fitsgz(blob: bytes):
    try:
        decompressed = gzip.decompress(blob)
        with fits.open(io.BytesIO(decompressed), memmap=False) as h:
            if len(h) < 2 or h[1].data is None:
                return None
            hdr = h[0].header
            klass = str(hdr.get("CLASS", hdr.get("OBJTYPE", ""))).strip()
            tbl = h[1].data
            flux = np.array(tbl["FLUX"], dtype=np.float32).flatten()
            wave = np.array(tbl["WAVELENGTH"], dtype=np.float32).flatten()
            if len(flux) < 100 or len(wave) != len(flux):
                return None
            resampled = np.interp(DESI_WAVE, wave, flux, left=0, right=0).astype(np.float32)
            valid = resampled != 0
            if valid.sum() < 100:
                return None
            med = np.median(resampled[valid])
            if not (np.isfinite(med) and med > 0):
                return None
            resampled /= med
            if np.isnan(resampled).any() or np.isinf(resampled).any():
                return None
            if resampled.std() < 1e-3:
                return None
            return resampled, klass
    except Exception:
        return None


# ============================================================
# Night-list selection
# ============================================================
def fetch_night_list():
    req = urllib.request.Request(TAR_BASE + "/", headers={"User-Agent": "Mozilla/5.0 BigBounce/1.0"})
    html = urllib.request.urlopen(req, timeout=60).read().decode()
    tars = sorted(set(re.findall(r"(\d{8}\.tar\.gz)", html)))
    return tars


def sample_nights(all_tars, num_nights, seed):
    rng = random.Random(seed)
    return sorted(rng.sample(all_tars, k=min(num_nights, len(all_tars))))


# ============================================================
# Tarball download
# ============================================================
def download_with_retry(url, dest, max_retries=3):
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 BigBounce/1.0"})
            with urllib.request.urlopen(req, timeout=600) as r, open(dest, "wb") as f:
                while True:
                    chunk = r.read(131072)
                    if not chunk:
                        break
                    f.write(chunk)
            return True
        except Exception as e:
            print(f"[download] attempt {attempt+1} failed for {url}: {e}", flush=True)
            if attempt < max_retries - 1:
                time.sleep(5 * (attempt + 1))
    return False


# ============================================================
# Shard builder
# ============================================================
def already_sharded_count(shard_dir: Path):
    total = 0
    for f in sorted(shard_dir.glob("shard_*.npy")):
        try:
            a = np.load(f, mmap_mode="r")
            total += a.shape[0]
        except Exception:
            continue
    return total


def build_shards(nights, tars_dir: Path, shard_dir: Path, processed_file: Path,
                 target_count: int, extract_workers: int):
    shard_dir.mkdir(parents=True, exist_ok=True)
    tars_dir.mkdir(parents=True, exist_ok=True)

    existing_shards = sorted(shard_dir.glob("shard_*.npy"))
    shard_id = len(existing_shards)
    total_success = already_sharded_count(shard_dir)
    processed_nights = set()
    if processed_file.exists():
        processed_nights = set(processed_file.read_text().splitlines())
    print(f"[shard] resume state: {shard_id} shards, {total_success:,} spectra, "
          f"{len(processed_nights)} nights already processed", flush=True)

    buffer = []
    classes_buf = []
    t_start = time.time()

    for night_tar in nights:
        if night_tar in processed_nights:
            continue
        if total_success >= target_count:
            break
        url = f"{TAR_BASE}/{night_tar}"
        tar_path = tars_dir / night_tar
        t_net = time.time()
        if not download_with_retry(url, tar_path):
            print(f"[shard] SKIP {night_tar} (download failed)", flush=True)
            continue
        net_dt = time.time() - t_net
        size_mb = tar_path.stat().st_size / 1e6
        print(f"[shard] fetched {night_tar}  {size_mb:.1f} MB in {net_dt:.1f}s "
              f"({size_mb/max(net_dt,1e-6):.1f} MB/s)", flush=True)

        # Extract all .fits.gz blobs into memory, decode in parallel
        file_blobs = []
        try:
            with tarfile.open(tar_path, "r:gz") as tf:
                for m in tf.getmembers():
                    if not (m.isreg() and m.name.endswith(".fits.gz")):
                        continue
                    try:
                        fobj = tf.extractfile(m)
                        if fobj is None:
                            continue
                        file_blobs.append(fobj.read())
                    except Exception:
                        continue
        except Exception as e:
            print(f"[shard] tar read error on {night_tar}: {e}", flush=True)
            tar_path.unlink(missing_ok=True)
            continue

        n_this_night = 0
        with ThreadPoolExecutor(max_workers=extract_workers) as ex:
            futs = [ex.submit(read_one_fitsgz, b) for b in file_blobs]
            for fut in as_completed(futs):
                res = fut.result()
                if res is None:
                    continue
                arr, klass = res
                buffer.append(arr)
                classes_buf.append(klass)
                n_this_night += 1
                total_success += 1
                if len(buffer) >= SHARD_SIZE:
                    sp = shard_dir / f"shard_{shard_id:05d}.npy"
                    cp = shard_dir / f"shard_{shard_id:05d}_class.npy"
                    np.save(sp, np.stack(buffer).astype(np.float32))
                    np.save(cp, np.array(classes_buf, dtype=object))
                    buffer = []
                    classes_buf = []
                    shard_id += 1
                if total_success >= target_count:
                    break

        # Mark night processed + delete tar
        processed_nights.add(night_tar)
        processed_file.write_text("\n".join(sorted(processed_nights)))
        tar_path.unlink(missing_ok=True)
        elapsed = time.time() - t_start
        rate = total_success / max(elapsed, 1e-6)
        print(f"[shard] {night_tar}: +{n_this_night:,} specs  total={total_success:,}/{target_count:,}  "
              f"elapsed={elapsed:.0f}s  rate={rate:.1f} specs/s", flush=True)

    # Flush remaining buffer
    if buffer:
        sp = shard_dir / f"shard_{shard_id:05d}.npy"
        cp = shard_dir / f"shard_{shard_id:05d}_class.npy"
        np.save(sp, np.stack(buffer).astype(np.float32))
        np.save(cp, np.array(classes_buf, dtype=object))
    print(f"[shard] DONE: {total_success:,} spectra cached across {shard_id+1} shards", flush=True)
    return total_success


# ============================================================
# Training
# ============================================================
def load_all_shards(shard_dir: Path):
    arrs = []
    for f in sorted(shard_dir.glob("shard_*.npy")):
        if "_class" in f.name:
            continue
        arrs.append(np.load(f, mmap_mode=None))
    if not arrs:
        return None
    return np.concatenate(arrs, axis=0).astype(np.float32)


def train(X: np.ndarray, output_dir: Path, *, batch_size, lr, max_epochs, patience,
          val_frac, seed):
    output_dir.mkdir(parents=True, exist_ok=True)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[train] device={device}  X.shape={X.shape}", flush=True)

    rng = np.random.default_rng(seed)
    idx = rng.permutation(len(X))
    n_val = int(len(X) * val_frac)
    val_idx, tr_idx = idx[:n_val], idx[n_val:]
    X_tr = torch.from_numpy(X[tr_idx]).float()
    X_val = torch.from_numpy(X[val_idx]).float().to(device)

    model = BigAE(n_in=X.shape[1], n_lat=128).to(device)
    opt = torch.optim.Adam(model.parameters(), lr=lr)
    mse = nn.MSELoss()
    best_val = float("inf")
    best_epoch = -1
    bad = 0
    log = []

    for epoch in range(1, max_epochs + 1):
        model.train()
        perm = torch.randperm(len(X_tr))
        train_losses = []
        for i in range(0, len(X_tr), batch_size):
            b = X_tr[perm[i:i + batch_size]].to(device, non_blocking=True)
            opt.zero_grad()
            loss = mse(model(b), b)
            loss.backward()
            opt.step()
            train_losses.append(loss.item())
        model.eval()
        with torch.no_grad():
            vloss = mse(model(X_val), X_val).item()
        tl = float(np.mean(train_losses))
        print(f"[train] epoch {epoch:02d}/{max_epochs}  train={tl:.4f}  val={vloss:.4f}  "
              f"best_val={best_val:.4f}", flush=True)
        log.append(dict(epoch=epoch, train=tl, val=vloss))
        if vloss < best_val - 1e-4:
            best_val = vloss
            best_epoch = epoch
            bad = 0
            torch.save(model.state_dict(), output_dir / "best_lamost_native.pt")
        else:
            bad += 1
            if bad >= patience:
                print(f"[train] early stop at epoch {epoch} (no improvement {patience} epochs)", flush=True)
                break

    gate_pass = bool(best_val <= 0.30)
    result = dict(
        best_val=best_val, best_epoch=best_epoch,
        gate_threshold=0.30, gate_pass=gate_pass,
        n_total=int(len(X)), n_train=int(len(X_tr)), n_val=int(len(X_val)),
        log=log,
    )
    (output_dir / "training_log.json").write_text(json.dumps(result, indent=2))
    print(f"[train] DONE  best_val={best_val:.4f}@epoch{best_epoch}  "
          f"gate{'_PASS' if gate_pass else '_FAIL'}(<=0.30)", flush=True)
    return result


# ============================================================
# Main
# ============================================================
def main():
    cfg = DEFAULTS
    base = Path(cfg["base_dir"])
    tars_dir = base / "tars"
    shard_dir = base / "shards"
    processed_file = base / ".processed_nights.txt"
    output_dir = Path(cfg["output_dir"])
    base.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 70, flush=True)
    print("LAMOST DR10 NATIVE BIGAE RETRAIN — P3-PATHC-LAMOST-NATIVE-RETRAIN", flush=True)
    print("=" * 70, flush=True)
    print(f"target_count={cfg['target_count']:,}  num_nights={cfg['num_nights']}  "
          f"max_epochs={cfg['max_epochs']}  extract_workers={cfg['extract_workers']}", flush=True)

    print("[select] Fetching night-tar list from lamost.org...", flush=True)
    all_tars = fetch_night_list()
    print(f"[select]   total nights advertised: {len(all_tars)}", flush=True)
    nights = sample_nights(all_tars, cfg["num_nights"], cfg["seed"])
    print(f"[select]   sampled {len(nights)} nights (seed={cfg['seed']}):", flush=True)
    for n in nights[:5]:
        print(f"[select]     {n}", flush=True)
    print("[select]     ...", flush=True)

    total = build_shards(nights, tars_dir, shard_dir, processed_file,
                         target_count=cfg["target_count"],
                         extract_workers=cfg["extract_workers"])

    if total < 50_000:
        print(f"[main] ABORT training — only {total:,} spectra < 50K minimum", flush=True)
        return

    X = load_all_shards(shard_dir)
    if X is None or len(X) == 0:
        print("[main] ABORT — no shards loaded", flush=True)
        return
    if len(X) > cfg["target_count"]:
        X = X[: cfg["target_count"]]

    train(X, output_dir,
          batch_size=cfg["batch_size"], lr=cfg["lr"],
          max_epochs=cfg["max_epochs"], patience=cfg["patience"],
          val_frac=cfg["val_frac"], seed=cfg["seed"])


if __name__ == "__main__":
    main()
