#!/usr/bin/env python3
"""Row 16(ii-b) addendum-A1 inference stage — exact 90-degree rotations through
the EXACT released preprocessing, with no crop and no interpolation.

Pre-registration addendum A1 (PREREGISTRATION_2026-09-19.md, commit 06cf6fbb),
committed before this ran.

For theta in {0, 90, 180, 270} (closed under negation mod 360) computes the raw
3-class softmax of the committed classifier on

    A_theta   = Resize224( Rot_theta( I   ) )
    B_theta   = Resize224( Rot_theta( M I ) )

using PIL transposes, so every rotation is a lossless pixel permutation of the
150x150 cutout and the preprocessing is byte-for-byte the committed one
(transforms.Resize((224,224)) + ToTensor + ImageNet normalise, exactly as in
injection_pilot/run_injection_scale20k.py). The production equivariant triple at
rotation theta then follows in closed form, since M.Rot_theta = Rot_-theta.M:

    eq_cw(X_theta) = ( p_cw(A_theta) + p_ccw(B_-theta) ) / 2      X = observed
    eq_cw(Y_theta) = ( p_cw(B_theta) + p_ccw(A_-theta) ) / 2      Y = parity-flipped

Output: nocrop_probs.npz with idx (int32, N) and probs (float32, N x 2 x 4 x 3),
indexed [galaxy, kind(0=A,1=B), angle, class(cw,ccw,ns)].
"""
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from PIL import Image

sys.path.insert(0, str(Path(__file__).parent))
from run_pa_transfer_inference import (  # noqa: E402  (same checkpoint pin, same transform)
    CACHE, SAMPLE, TFM, load_model, BATCH,
)

HERE = Path(__file__).parent
OUT = HERE / "nocrop_probs.npz"
ANGLES = [0, 90, 180, 270]
_ROT = {0: None, 90: Image.Transpose.ROTATE_90,
        180: Image.Transpose.ROTATE_180, 270: Image.Transpose.ROTATE_270}
CKPT_EVERY = 4000


def main(limit=None):
    t0 = time.time()
    sample = pd.read_parquet(SAMPLE)
    idx_all = [i for i in range(len(sample)) if (CACHE / f"{i}.jpg").exists()]
    if limit:
        idx_all = idx_all[:limit]
    n = len(idx_all)
    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    enc, head = load_model(device)
    print(f"[{time.time()-t0:.1f}s] N={n}, no-crop exact rotations {ANGLES} on {device}", flush=True)

    probs = np.full((n, 2, len(ANGLES), 3), np.nan, dtype=np.float32)
    start = 0
    if OUT.exists() and limit is None:
        prev = np.load(OUT)
        if prev["idx"].tolist() == idx_all:
            probs, start = prev["probs"], int(prev["n_done"])
            print(f"[{time.time()-t0:.1f}s] resuming at {start}/{n}", flush=True)

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

    for g in range(start, n):
        img = Image.open(CACHE / f"{idx_all[g]}.jpg").convert("RGB")
        mimg = img.transpose(Image.FLIP_LEFT_RIGHT)
        for a, th in enumerate(ANGLES):
            op = _ROT[th]
            for kind, base in ((0, img), (1, mimg)):
                r = base if op is None else base.transpose(op)
                buf.append(TFM(r))
                meta.append((g, kind, a))
            if len(buf) >= BATCH:
                flush()
        if (g + 1) % CKPT_EVERY == 0:
            flush()
            np.savez_compressed(OUT, idx=np.array(idx_all, dtype=np.int32),
                                probs=probs, n_done=g + 1, angles=np.array(ANGLES))
            el = time.time() - t0
            rate = (g + 1 - start) / el
            print(f"[{el:.1f}s] {g+1}/{n} | {rate:.1f} gal/s | ETA {(n-g-1)/rate/60:.1f} min", flush=True)

    flush()
    np.savez_compressed(OUT, idx=np.array(idx_all, dtype=np.int32),
                        probs=probs, n_done=n, angles=np.array(ANGLES))
    assert not np.isnan(probs).any(), "NaN left in probability array"
    print(f"[{time.time()-t0:.1f}s] DONE {n} galaxies x {len(ANGLES)} angles x 2 kinds "
          f"= {n*len(ANGLES)*2} forward passes -> {OUT}", flush=True)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else None)
