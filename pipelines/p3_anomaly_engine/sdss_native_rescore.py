#!/usr/bin/env python3
"""
SDSS DR18 Native BigAE RE-SCORE — P3-PATHC-SDSS-NATIVE-RETRAIN (close-out phase)
================================================================================
Scores the full 1.93M-candidate SDSS DR18 quality-cut set with the natively
trained BigAE (best_sdss_native.pt, val_loss=0.0311 gate PASS from fire #80).

This is the second half of Path C criterion #1. Training done fire #80 on a
300K random sample; this pass re-scores EVERY quality-cut spectrum so Paper 3
Table 1's SDSS row can be rebuilt from native (not cross-transfer) anomaly
scores, and the SDSS-native anomaly set uploaded to HuggingFace.

Pipeline:
  1. Load spAll-v5_13_2.fits, apply SAME quality cut as the training script
     (ZWARNING==0, SN_MEDIAN>2, SPECPRIMARY==1, CLASS in {STAR,GALAXY,QSO}) →
     ~1,928,673 candidates.
  2. Load best_sdss_native.pt onto cuda:0 in eval mode.
  3. Stream through candidates: ThreadPoolExecutor(64) downloads lite-spec FITS,
     preprocesses to 496-bin DESI-grid median-normalized float32 vector.
  4. Buffer 4096 preprocessed vectors + their (plate,mjd,fiberid,ra,dec,z,class)
     metadata → move to GPU → forward pass → per-spectrum MSE = anomaly_score.
  5. Append batch to parquet under outputs/sdss_native/scores/batch_NNNNN.parquet
     via pyarrow. Resumable: each completed batch logs its index to
     processed_batches.txt; re-runs skip completed batches and resume from the
     first unprocessed candidate.
  6. After full pass: concatenate all batch parquets, rank by anomaly_score,
     write top-rank file outputs/sdss_native/sdss_native_anomalies_top_N.parquet
     where N = paper-3 Table 1 canonical 77,905 (for direct comparison).

Run:
    python3 sdss_native_rescore.py --workers 64 --batch-size 4096

The pod keeps its existing 60 training-shard files untouched (they are the
training sample; this script does an independent full-candidate pass).
"""

import argparse
import json
import os
import random
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
import torch
import torch.nn as nn
from astropy.io import fits

# ============================================================
# Config
# ============================================================
DESI_WMIN, DESI_WMAX = 3600.0, 9800.0
N_BINS = 496
DOWNLOAD_BASE = "https://data.sdss.org/sas/dr18/spectro/sdss/redux/v5_13_2/spectra/lite"

DEFAULTS = dict(
    spall_path="/workspace/bigbounce_scan/temp/sdss/spAll-v5_13_2.fits",
    model_path="/workspace/bigbounce_scan/outputs/sdss_native/best_sdss_native.pt",
    output_dir="/workspace/bigbounce_scan/outputs/sdss_native/scores",
    raw_cache_dir="/workspace/bigbounce_scan/temp/sdss_native/rescore_raw",
    workers=64,
    batch_size=4096,
    gpu_batch=4096,
    seed=20260419,
    top_n=77905,
)


# ============================================================
# BigAE — must match training architecture exactly
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
# Preprocessing — same as retrain script, with defensive clipping
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
    url = f"{DOWNLOAD_BASE}/{plate:04d}/spec-{plate:04d}-{mjd}-{fiberid:04d}.fits"
    local = Path(cache_dir) / f"spec-{plate:04d}-{mjd}-{fiberid:04d}.fits"
    if not local.exists():
        import urllib.request
        req = urllib.request.Request(url, headers={"User-Agent": "bigbounce-pathc-rescore/1.0"})
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
        if arr.std() < 1e-3:
            return None
        # Defensive outlier rejection / clipping (learned from LAMOST fire #80)
        if np.abs(arr).max() > 100.0:
            return None
        np.clip(arr, -10.0, 10.0, out=arr)
        return arr
    except Exception:
        return None
    finally:
        try:
            local.unlink(missing_ok=True)
        except Exception:
            pass


# ============================================================
# Candidate selection — SAME cut as training
# ============================================================
def select_candidates(spall_path):
    print(f"[select] Loading spAll from {spall_path}...", flush=True)
    with fits.open(spall_path, memmap=True) as hdul:
        t = hdul[1].data
        n = len(t)
        print(f"[select]   rows: {n:,}", flush=True)
        cols = set(t.dtype.names)
        zw = t["ZWARNING"]
        sn_col = "SN_MEDIAN_ALL" if "SN_MEDIAN_ALL" in cols else (
            "SN_MEDIAN" if "SN_MEDIAN" in cols else None)
        if sn_col is None:
            sn = np.full(n, 99.0, dtype=np.float32)
        else:
            sn = t[sn_col]
            if sn.ndim > 1:
                sn = sn.max(axis=1)
        klass = np.array([c.strip() for c in t["CLASS"]])
        specprim = t["SPECPRIMARY"]
        mask = (zw == 0) & (sn > 2.0) & (specprim == 1) & np.isin(klass, ["STAR", "GALAXY", "QSO"])
        idx = np.where(mask)[0]
        print(f"[select]   candidates after quality cuts: {len(idx):,}", flush=True)

        plate = t["PLATE"][idx].astype(np.int32)
        mjd = t["MJD"][idx].astype(np.int32)
        fiber = t["FIBERID"][idx].astype(np.int32)
        ra = t["RA"][idx].astype(np.float64) if "RA" in cols else np.full(len(idx), np.nan)
        dec = t["DEC"][idx].astype(np.float64) if "DEC" in cols else np.full(len(idx), np.nan)
        # Redshift column name varies: Z_NOQSO or Z
        z_col = "Z" if "Z" in cols else ("Z_NOQSO" if "Z_NOQSO" in cols else None)
        z = t[z_col][idx].astype(np.float32) if z_col is not None else np.full(len(idx), np.nan, dtype=np.float32)
        klass_sel = klass[idx]

    # Deterministic order — sort by plate then mjd then fiber for reproducibility
    order = np.lexsort((fiber, mjd, plate))
    plate, mjd, fiber, ra, dec, z, klass_sel = (
        plate[order], mjd[order], fiber[order], ra[order], dec[order], z[order], klass_sel[order])
    print(f"[select]   ordered by (plate,mjd,fiberid); first record:"
          f" plate={plate[0]} mjd={mjd[0]} fiberid={fiber[0]}", flush=True)
    return plate, mjd, fiber, ra, dec, z, klass_sel


# ============================================================
# Score streaming loop
# ============================================================
def processed_batch_ids(output_dir):
    p = Path(output_dir) / "processed_batches.txt"
    if not p.exists():
        return set()
    with open(p) as f:
        return {int(x) for x in f.read().split() if x.strip().isdigit()}


def mark_batch_done(output_dir, batch_id):
    p = Path(output_dir) / "processed_batches.txt"
    with open(p, "a") as f:
        f.write(f"{batch_id}\n")


def write_batch_parquet(output_dir, batch_id, rows):
    """rows: list of dicts with scalar values."""
    table = pa.Table.from_pylist(rows)
    path = Path(output_dir) / f"batch_{batch_id:06d}.parquet"
    pq.write_table(table, path, compression="snappy")
    return path


def score_all(args):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[score] device={device}", flush=True)
    if torch.cuda.is_available():
        print(f"[score] GPU: {torch.cuda.get_device_name(0)}", flush=True)

    # Load model
    model = BigAE(n_in=N_BINS, n_lat=128).to(device)
    ckpt = torch.load(args.model_path, map_location=device)
    if isinstance(ckpt, dict) and "state_dict" in ckpt:
        model.load_state_dict(ckpt["state_dict"])
    else:
        model.load_state_dict(ckpt)
    model.eval()
    print(f"[score] loaded model from {args.model_path}", flush=True)

    Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    Path(args.raw_cache_dir).mkdir(parents=True, exist_ok=True)

    # Select candidates
    plate, mjd, fiber, ra, dec, z, klass = select_candidates(args.spall_path)
    n_total = len(plate)
    n_batches_total = (n_total + args.batch_size - 1) // args.batch_size
    print(f"[score] total candidates: {n_total:,} → {n_batches_total:,} batches of {args.batch_size}",
          flush=True)

    done = processed_batch_ids(args.output_dir)
    if done:
        print(f"[score] resume: {len(done):,} batches already scored; skipping", flush=True)

    t_start = time.time()
    n_success = 0
    n_failed = 0
    n_scored = 0

    for batch_id in range(n_batches_total):
        if batch_id in done:
            continue
        lo = batch_id * args.batch_size
        hi = min(lo + args.batch_size, n_total)
        batch_slice = slice(lo, hi)
        b_plate = plate[batch_slice]
        b_mjd = mjd[batch_slice]
        b_fiber = fiber[batch_slice]
        b_ra = ra[batch_slice]
        b_dec = dec[batch_slice]
        b_z = z[batch_slice]
        b_klass = klass[batch_slice]

        # Parallel download+preprocess
        def task(i):
            arr = fetch_and_preprocess(int(b_plate[i]), int(b_mjd[i]), int(b_fiber[i]),
                                        args.raw_cache_dir)
            return i, arr

        specs = [None] * len(b_plate)
        with ThreadPoolExecutor(max_workers=args.workers) as ex:
            futs = [ex.submit(task, i) for i in range(len(b_plate))]
            for fut in as_completed(futs):
                i, arr = fut.result()
                specs[i] = arr

        # Collect successful specs with their metadata indices
        idx_ok = [i for i, s in enumerate(specs) if s is not None]
        n_success += len(idx_ok)
        n_failed += len(b_plate) - len(idx_ok)

        if not idx_ok:
            mark_batch_done(args.output_dir, batch_id)
            continue

        X = np.stack([specs[i] for i in idx_ok]).astype(np.float32)
        X_t = torch.from_numpy(X).to(device)

        with torch.no_grad():
            # Inference in gpu-sized chunks in case batch > gpu_batch
            mses = []
            for j in range(0, X_t.shape[0], args.gpu_batch):
                xb = X_t[j:j + args.gpu_batch]
                xh = model(xb)
                per_spec_mse = ((xb - xh) ** 2).mean(dim=1).cpu().numpy()
                mses.append(per_spec_mse)
            scores = np.concatenate(mses).astype(np.float32)

        rows = []
        for k, i in enumerate(idx_ok):
            rows.append({
                "plate": int(b_plate[i]),
                "mjd": int(b_mjd[i]),
                "fiberid": int(b_fiber[i]),
                "ra": float(b_ra[i]),
                "dec": float(b_dec[i]),
                "z": float(b_z[i]),
                "class": str(b_klass[i]),
                "anomaly_score": float(scores[k]),
            })
        write_batch_parquet(args.output_dir, batch_id, rows)
        mark_batch_done(args.output_dir, batch_id)
        n_scored += len(rows)

        elapsed = time.time() - t_start
        rate = n_scored / max(1.0, elapsed)
        remaining = (n_total - (batch_id + 1) * args.batch_size) / max(1.0, rate)
        if (batch_id + 1) % 5 == 0 or batch_id < 3:
            print(f"[score] batch {batch_id+1}/{n_batches_total}  "
                  f"scored={n_scored:,} success={n_success:,} failed={n_failed:,} "
                  f"rate={rate:.1f}/s eta_h={remaining/3600:.1f}", flush=True)

    print(f"[score] DONE — scored={n_scored:,} success={n_success:,} "
          f"failed={n_failed:,} elapsed_h={(time.time()-t_start)/3600:.2f}", flush=True)


# ============================================================
# Final top-N anomaly-set builder — runs after scoring completes
# ============================================================
def build_anomaly_topn(output_dir, top_n):
    out = Path(output_dir)
    batch_files = sorted(out.glob("batch_*.parquet"))
    if not batch_files:
        print("[topn] no batch parquets found; skipping", flush=True)
        return
    print(f"[topn] reading {len(batch_files)} batch parquets...", flush=True)
    import pyarrow.dataset as ds
    dataset = ds.dataset([str(p) for p in batch_files], format="parquet")
    full = dataset.to_table().to_pandas()
    print(f"[topn] total scored rows: {len(full):,}", flush=True)
    full = full.sort_values("anomaly_score", ascending=False).reset_index(drop=True)
    top = full.head(top_n)
    top_path = out.parent / f"sdss_native_anomalies_top_{top_n}.parquet"
    pq.write_table(pa.Table.from_pandas(top), top_path, compression="snappy")
    print(f"[topn] wrote {top_path} ({len(top):,} rows, "
          f"min_score={top['anomaly_score'].min():.4f} "
          f"max_score={top['anomaly_score'].max():.4f})", flush=True)
    # Also write full ranked (may be large; keep for later cross-match)
    full_path = out.parent / "sdss_native_all_scores.parquet"
    pq.write_table(pa.Table.from_pandas(full), full_path, compression="snappy")
    print(f"[topn] wrote full ranked file {full_path} ({len(full):,} rows)", flush=True)


# ============================================================
# Main
# ============================================================
def main():
    p = argparse.ArgumentParser()
    for k, v in DEFAULTS.items():
        if isinstance(v, bool):
            p.add_argument(f"--{k.replace('_', '-')}", action="store_true", default=v)
        else:
            p.add_argument(f"--{k.replace('_', '-')}", type=type(v), default=v)
    p.add_argument("--topn-only", action="store_true", help="Skip scoring, just rank completed batches")
    args = p.parse_args()
    args.shard_dir = None  # unused here; kept for symmetry

    print(f"[main] config: {json.dumps(vars(args), default=str, indent=2)}", flush=True)

    if not args.topn_only:
        score_all(args)
    build_anomaly_topn(args.output_dir, args.top_n)


if __name__ == "__main__":
    main()
