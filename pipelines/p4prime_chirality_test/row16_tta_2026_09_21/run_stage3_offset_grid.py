#!/usr/bin/env python3
"""Step T stage-3 inference — the eight 22.5-degree-offset angles.

Pre-registration: PREREGISTRATION_2026-09-21.md sec."T1", committed BEFORE this
script was run.

Identical preprocessing, checkpoint pin, cutout cache and (A, B) pairing to the
row 16(ii-b) stage-1 run, at the angles that stage 1 does not cover:

    Phi' = {22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5} deg

closed under negation mod 360, as the equivariant bookkeeping requires. Stage 1
+ stage 3 together form a uniform 16-angle 22.5-degree grid on one
preprocessing, which is what makes the D4 TTA's parity transfer and the D8
TTA's label self-disagreement measurable at all (pre-registration sec."T0").

Galaxies are processed in the order of a SEEDED PERMUTATION so that a truncated
run is an unbiased subsample rather than the class-ordered prefix of the sample
file (the sample is 10,000 CW followed by 10,000 CCW). A hard 90-minute
wall-clock cap stops the run; whatever is complete at that point is what the
analysis uses, with its exact N reported.

Output: stage3_offset_probs.npz
    idx        int32  (N,)          same galaxy list, same order, as stage 1
    probs      float32 (N, 2, 8, 3) [galaxy, kind(0=A,1=B), angle, class(cw,ccw,ns)]
    done_mask  bool   (N,)          True where the 16 passes completed
    angles     float32 (8,)
    order      int32  (N,)          the seeded permutation actually used
"""
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "row16_pa_parity_transfer"))
from run_pa_transfer_inference import (  # noqa: E402  (same pin, same transform, same crop)
    CACHE, SAMPLE, BATCH, CROP, REPO_ID, REV, TFM, load_model,
)

HERE = Path(__file__).resolve().parent
OUT = HERE / "stage3_offset_probs.npz"
ANGLES = [22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5]
PERM_SEED = 20260921
CKPT_EVERY = 2000          # galaxies processed
WALL_CAP_S = 90 * 60       # pre-registered hard cap


def prep(img, phi):
    """Identical to stage 1's prep(), but every angle here is non-exact."""
    r = img.rotate(phi % 360, resample=Image.BICUBIC, expand=False)
    w, h = r.size
    left, top = (w - CROP) // 2, (h - CROP) // 2
    return TFM(r.crop((left, top, left + CROP, top + CROP)))


def main(limit=None):
    t0 = time.time()
    sample = pd.read_parquet(SAMPLE)
    idx_all = [i for i in range(len(sample)) if (CACHE / f"{i}.jpg").exists()]
    n = len(idx_all)
    order = np.random.default_rng(PERM_SEED).permutation(n).astype(np.int32)
    if limit:
        order = order[:limit]
    print(f"[{time.time()-t0:.1f}s] N={n} cached cutouts; processing "
          f"{len(order)} in seeded-permutation order (seed {PERM_SEED})", flush=True)

    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    enc, head = load_model(device)
    print(f"[{time.time()-t0:.1f}s] model {REPO_ID}@{REV[:8]} on {device}", flush=True)

    probs = np.full((n, 2, len(ANGLES), 3), np.nan, dtype=np.float32)
    done = np.zeros(n, dtype=bool)
    if OUT.exists():
        prev = np.load(OUT)
        if prev["idx"].tolist() == idx_all:
            probs, done = prev["probs"], prev["done_mask"]
            print(f"[{time.time()-t0:.1f}s] resuming with {int(done.sum())} galaxies done",
                  flush=True)

    buf, meta = [], []

    def flush():
        if not buf:
            return
        x = torch.stack(buf).to(device)
        with torch.no_grad():
            p = torch.softmax(head(enc(x)), dim=1).float().cpu().numpy()
        for k, (g, kind, a) in enumerate(meta):
            probs[g, kind, a, :] = p[k]
        buf.clear()
        meta.clear()

    def save(tag):
        flush()
        np.savez_compressed(OUT, idx=np.array(idx_all, dtype=np.int32), probs=probs,
                            done_mask=done, angles=np.array(ANGLES, dtype=np.float32),
                            order=order)
        el = time.time() - t0
        nd = int(done.sum())
        print(f"[{el:.1f}s] {tag} {nd}/{n} done | {nd/el:.1f} gal/s "
              f"| ETA {(len(order)-nd)/max(nd/el, 1e-9)/60:.1f} min", flush=True)

    processed = 0
    capped = False
    for g in order:
        g = int(g)
        if done[g]:
            continue
        if time.time() - t0 > WALL_CAP_S:
            capped = True
            print(f"[{time.time()-t0:.1f}s] WALL-CAP {WALL_CAP_S}s reached "
                  f"(pre-registered) - stopping", flush=True)
            break
        img = Image.open(CACHE / f"{idx_all[g]}.jpg").convert("RGB")
        mimg = img.transpose(Image.FLIP_LEFT_RIGHT)
        for a, phi in enumerate(ANGLES):
            buf.append(prep(img, phi))
            meta.append((g, 0, a))
            buf.append(prep(mimg, phi))
            meta.append((g, 1, a))
            if len(buf) >= BATCH:
                flush()
        done[g] = True
        processed += 1
        if processed % CKPT_EVERY == 0:
            save("ckpt")

    save("FINAL" if not capped else "CAPPED")
    nd = int(done.sum())
    assert not np.isnan(probs[done]).any(), "NaN left among galaxies marked done"
    print(f"[{time.time()-t0:.1f}s] DONE {nd} galaxies x {len(ANGLES)} angles x 2 kinds "
          f"= {nd*len(ANGLES)*2} forward passes -> {OUT}", flush=True)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else None)
