#!/usr/bin/env python3
"""Step P stage-4 inference — d(180) on the two smaller committed cutout caches.

Pre-registration: PREREGISTRATION_2026-09-21.md sec."P1", committed BEFORE this
script was run (git 712e9e7e).

The EXACT released preprocessing (Resize224 of the full 150 px cutout, no crop)
at theta in {0, 180} only -- lossless PIL transposes, no interpolation anywhere
-- for both kinds (A = I, B = M I), on the two cached samples the row 16(ii-b)
run did not use:

    cutout_cache_scale   5,000 galaxies (scale_sample.parquet,  seed 43, NSIDE=32)
    cutout_cache           500 galaxies (pilot_sample.parquet,  seed 42)

4 forward passes per galaxy. theta = 180 is the orientation that needs no
PA-uniformity argument at all (position angle is defined mod 180 deg), so this
is the assumption-free anchor of the row-16(ii-b) sec.4 dilution bound.

Output: stage4_<tag>_probs.npz  with idx (int32, N) and probs
(float32, N x 2 x 2 x 3) indexed [galaxy, kind(0=A,1=B), angle(0,180), class].
"""
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "row16_pa_parity_transfer"))
from run_pa_transfer_inference import (  # noqa: E402  (same checkpoint pin, same transform)
    BATCH, REPO_ID, REV, TFM, load_model,
)

HERE = Path(__file__).resolve().parent
PILOT = HERE.parent / "injection_pilot"
ANGLES = [0, 180]
CACHES = [("scale5k", PILOT / "cutout_cache_scale", PILOT / "scale_sample.parquet"),
          ("pilot500", PILOT / "cutout_cache", PILOT / "pilot_sample.parquet")]


def run_one(tag, cache, sample_path, device, enc, head):
    t0 = time.time()
    sample = pd.read_parquet(sample_path)
    idx_all = [i for i in range(len(sample)) if (cache / f"{i}.jpg").exists()]
    n = len(idx_all)
    out = HERE / f"stage4_{tag}_probs.npz"
    probs = np.full((n, 2, len(ANGLES), 3), np.nan, dtype=np.float32)
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

    for g in range(n):
        img = Image.open(cache / f"{idx_all[g]}.jpg").convert("RGB")
        mimg = img.transpose(Image.FLIP_LEFT_RIGHT)
        for a, th in enumerate(ANGLES):
            for kind, base in ((0, img), (1, mimg)):
                r = base if th == 0 else base.transpose(Image.Transpose.ROTATE_180)
                buf.append(TFM(r))
                meta.append((g, kind, a))
            if len(buf) >= BATCH:
                flush()
    flush()
    assert not np.isnan(probs).any(), f"NaN left in {tag}"
    np.savez_compressed(out, idx=np.array(idx_all, dtype=np.int32), probs=probs,
                        n_done=n, angles=np.array(ANGLES))
    el = time.time() - t0
    print(f"[{el:.1f}s] {tag}: {n} galaxies x {len(ANGLES)} angles x 2 kinds = "
          f"{n*len(ANGLES)*2} forward passes ({n/el:.1f} gal/s) -> {out.name}", flush=True)


def main():
    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    enc, head = load_model(device)
    print(f"model {REPO_ID}@{REV[:8]} on {device}", flush=True)
    for tag, cache, sample_path in CACHES:
        run_one(tag, cache, sample_path, device, enc, head)


if __name__ == "__main__":
    main()
