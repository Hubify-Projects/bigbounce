#!/usr/bin/env python3
"""Row 16(ii-b) inference stage — PA-restoring parity transfer.

Pre-registration: PREREGISTRATION_2026-09-19.md (committed 12248d70 BEFORE
this script was run).

For every cached Legacy DR9 cutout I of the row 16(ii) N=20k sample, computes
the raw 3-class softmax of the committed classifier on

    A_phi = Resize224( CenterCrop106( Rotate_phi( I   ) ) )
    B_phi = Resize224( CenterCrop106( Rotate_phi( M I ) ) )     M = mirror

for phi in {0,45,90,135,180,225,270,315} deg. Those 16 forward passes per
galaxy are everything the analysis stage needs, because the centre crop is
mirror-symmetric, so M.CenterCrop.Rotate_phi = CenterCrop.Rotate_{-phi}.M and
the production equivariant triple at rotation phi is

    eq_cw (X_phi) = ( p_cw (A_phi) + p_ccw(B_-phi) ) / 2      X = normal galaxy
    eq_ccw(X_phi) = ( p_ccw(A_phi) + p_cw (B_-phi) ) / 2
    eq_ns (X_phi) = ( p_ns (A_phi) + p_ns (B_-phi) ) / 2
    eq_cw (Y_phi) = ( p_cw (B_phi) + p_ccw(A_-phi) ) / 2      Y = parity-flipped,
    eq_ccw(Y_phi) = ( p_ccw(B_phi) + p_cw (A_-phi) ) / 2          PA restored
    eq_ns (Y_phi) = ( p_ns (B_phi) + p_ns (A_-phi) ) / 2

with the angle grid closed under negation mod 360, as pre-registered.

Exact rotations (0/90/180/270) use PIL transposes so the phi=0 and phi=180
positive controls are bit-exact; 45/135/225/315 use bicubic.

Output: pa_transfer_probs.npz with `idx` (int32, N) and `probs`
(float32, N x 2 x 8 x 3) indexed [galaxy, kind(0=A,1=B), angle, class(cw,ccw,ns)].
"""
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import timm
import torch
import torch.nn as nn
from PIL import Image
from huggingface_hub import hf_hub_download
from torchvision import transforms

HERE = Path(__file__).parent
PILOT = HERE.parent / "injection_pilot"
CACHE = PILOT / "cutout_cache_scale20k"
SAMPLE = PILOT / "scale20k_sample.parquet"
OUT = HERE / "pa_transfer_probs.npz"

REPO_ID = "bamfai/galaxy-chirality-v2"
CKPT = "chirality_model_v2_best.pt"
REV = "237d021c451d75cf86a875e86d4de498b74e2f12"

ANGLES = [0, 45, 90, 135, 180, 225, 270, 315]
CROP = 106            # 106*sqrt(2)/2 = 74.95 <= 75 => no out-of-frame pixels
IMG_SIZE = 224
BATCH = 128
CKPT_EVERY = 2000     # galaxies


class Head(nn.Module):
    def __init__(self):
        super().__init__()
        self.h = nn.Sequential(
            nn.LayerNorm(384), nn.Linear(384, 512), nn.GELU(), nn.Dropout(0.3),
            nn.Linear(512, 256), nn.GELU(), nn.Dropout(0.2), nn.Linear(256, 3),
        )

    def forward(self, x):
        return self.h(x)


TFM = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

_EXACT = {0: None, 90: Image.Transpose.ROTATE_90,
          180: Image.Transpose.ROTATE_180, 270: Image.Transpose.ROTATE_270}


def rotate(img, phi):
    """PIL counter-clockwise rotation by phi deg; exact for multiples of 90."""
    phi = phi % 360
    if phi in _EXACT:
        op = _EXACT[phi]
        return img if op is None else img.transpose(op)
    return img.rotate(phi, resample=Image.BICUBIC, expand=False)


def prep(img, phi):
    r = rotate(img, phi)
    w, h = r.size
    left, top = (w - CROP) // 2, (h - CROP) // 2
    return TFM(r.crop((left, top, left + CROP, top + CROP)))


def load_model(device):
    path = hf_hub_download(repo_id=REPO_ID, filename=CKPT, revision=REV)
    state = torch.load(path, map_location="cpu", weights_only=True)
    enc = timm.create_model("vit_small_patch16_224", pretrained=False, num_classes=0)
    head = Head()
    enc.load_state_dict(state["enc"])
    head.load_state_dict(state["head"])
    enc.eval().to(device)
    head.eval().to(device)
    return enc, head


def main(limit=None):
    t0 = time.time()
    sample = pd.read_parquet(SAMPLE)
    idx_all = [i for i in range(len(sample)) if (CACHE / f"{i}.jpg").exists()]
    if limit:
        idx_all = idx_all[:limit]
    n = len(idx_all)
    print(f"[{time.time()-t0:.1f}s] N={n} cached cutouts of {len(sample)} sampled", flush=True)

    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    enc, head = load_model(device)
    print(f"[{time.time()-t0:.1f}s] model {REPO_ID}@{REV[:8]} on {device}", flush=True)

    probs = np.full((n, 2, len(ANGLES), 3), np.nan, dtype=np.float32)
    start = 0
    if OUT.exists() and limit is None:
        prev = np.load(OUT)
        if prev["idx"].tolist() == idx_all:
            probs = prev["probs"]
            done = int(prev["n_done"])
            start = done
            print(f"[{time.time()-t0:.1f}s] resuming at galaxy {start}/{n}", flush=True)

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
        for a, phi in enumerate(ANGLES):
            buf.append(prep(img, phi))
            meta.append((g, 0, a))
            buf.append(prep(mimg, phi))
            meta.append((g, 1, a))
            if len(buf) >= BATCH:
                flush()
        if (g + 1) % CKPT_EVERY == 0:
            flush()
            np.savez_compressed(OUT, idx=np.array(idx_all, dtype=np.int32),
                                probs=probs, n_done=g + 1, angles=np.array(ANGLES))
            el = time.time() - t0
            rate = (g + 1 - start) / el
            print(f"[{el:.1f}s] {g+1}/{n} galaxies | {rate:.1f} gal/s "
                  f"| {rate*16:.0f} img/s | ETA {(n-g-1)/rate/60:.1f} min", flush=True)

    flush()
    np.savez_compressed(OUT, idx=np.array(idx_all, dtype=np.int32),
                        probs=probs, n_done=n, angles=np.array(ANGLES))
    assert not np.isnan(probs[:n]).any(), "NaN left in probability array"
    print(f"[{time.time()-t0:.1f}s] DONE {n} galaxies x {len(ANGLES)} angles x 2 kinds "
          f"= {n*len(ANGLES)*2} forward passes -> {OUT}", flush=True)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else None)
