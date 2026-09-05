#!/usr/bin/env python3
"""Row 16 step (ii): 20k-scale: pixel-level parity-injection test through the
PRODUCTION equivariant pipeline (Z2 / 2-fold flip test-time-averaging,
matching pipelines/p2_chirality/equivariant_postprocess.py exactly —
NOT the raw single-pass forward used by the N=500 pilot, and NOT a full
D4 8-way average, which is a different diagnostic (d4_tta_holdout.py)
not used by the released Catalog C / the paper's residual-bias number).

Key computational identity (verified analytically, exploited here for
speed): the production TTA construction
    eq_cw(img)  = (p_cw(img) + p_ccw(flip(img))) / 2
    eq_ccw(img) = (p_ccw(img) + p_cw(flip(img))) / 2
is EXACTLY antisymmetric under a global mirror flip of a single image:
    eq_cw(flip(img)) = eq_ccw(img)   (exact swap, no re-inference needed)
So for each galaxy we only need ONE forward-pass pair (orig, flip) —
computed once — and can then analytically evaluate ANY injected-flip
assignment (which galaxies are externally pre-mirrored before the
production pipeline sees them) by swapping eq_cw<->eq_ccw for the
selected subset. This turns an O(N x n_fractions x n_seeds) inference
job into an O(N) one, with the f/seed grid handled by closed-form
reweighting + resampling over which N*f galaxies are selected.
"""
import io
import json
import time
from pathlib import Path

import numpy as np
import pandas as pd
import requests
import timm
import torch
import torch.nn as nn
from torchvision import transforms
from huggingface_hub import hf_hub_download
from PIL import Image

HERE = Path(__file__).parent
IMG_SIZE = 224
BATCH = 64
CACHE_DIR = HERE / "cutout_cache_scale20k"
OUT_PATH = HERE / "scale20k_pairs.parquet"
CKPT_EVERY = 500


class Head(nn.Module):
    def __init__(self):
        super().__init__()
        self.h = nn.Sequential(
            nn.LayerNorm(384), nn.Linear(384, 512), nn.GELU(), nn.Dropout(0.3),
            nn.Linear(512, 256), nn.GELU(), nn.Dropout(0.2), nn.Linear(256, 3),
        )

    def forward(self, x):
        return self.h(x)


def load_model(device):
    ckpt_path = hf_hub_download(
        repo_id="bamfai/galaxy-chirality-v2",
        filename="chirality_model_v2_best.pt",
        revision="237d021c451d75cf86a875e86d4de498b74e2f12",
    )
    state = torch.load(ckpt_path, map_location="cpu", weights_only=True)
    encoder = timm.create_model("vit_small_patch16_224", pretrained=False, num_classes=0)
    head = Head()
    encoder.load_state_dict(state["enc"])
    head.load_state_dict(state["head"])
    encoder.eval().to(device)
    head.eval().to(device)
    return encoder, head


TFM = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])


def download_one(row, cache_dir):
    p = cache_dir / f"{row['dr8_or_hf_id'] if 'dr8_or_hf_id' in row else row.name}.jpg"
    return p


def get_image(idx, url, cache_dir):
    p = cache_dir / f"{idx}.jpg"
    if not p.exists():
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        p.write_bytes(r.content)
    return Image.open(p).convert("RGB")


def main(limit=None):
    t0 = time.time()
    CACHE_DIR.mkdir(exist_ok=True)
    sample = pd.read_parquet(HERE / "scale20k_sample.parquet")
    if limit:
        sample = sample.iloc[:limit].reset_index(drop=True)
    n = len(sample)
    print(f"[{time.time()-t0:.1f}s] N={n} target", flush=True)

    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    encoder, head = load_model(device)
    print(f"[{time.time()-t0:.1f}s] model loaded on {device}", flush=True)

    # Resume from checkpoint if present
    done_rows = []
    done_idx = set()
    if OUT_PATH.exists() and limit is None:
        prev = pd.read_parquet(OUT_PATH)
        done_rows = prev.to_dict("records")
        done_idx = set(prev["idx"].tolist())
        print(f"[{time.time()-t0:.1f}s] resuming: {len(done_idx)} already done", flush=True)

    results = list(done_rows)
    n_fail = 0
    batch_orig, batch_flip, batch_meta = [], [], []

    def flush():
        nonlocal batch_orig, batch_flip, batch_meta
        if not batch_orig:
            return
        bo = torch.stack(batch_orig).to(device)
        bf = torch.stack(batch_flip).to(device)
        with torch.no_grad():
            po = torch.softmax(head(encoder(bo)), dim=1).cpu().numpy()
            pf = torch.softmax(head(encoder(bf)), dim=1).cpu().numpy()
        for i, meta in enumerate(batch_meta):
            results.append({
                "idx": meta["idx"],
                "ra": meta["ra"], "dec": meta["dec"],
                "class_eq_catalog": meta["class_eq_catalog"],
                "p_cw_orig": float(po[i, 0]), "p_ccw_orig": float(po[i, 1]), "p_ns_orig": float(po[i, 2]),
                "p_cw_flip": float(pf[i, 0]), "p_ccw_flip": float(pf[i, 1]), "p_ns_flip": float(pf[i, 2]),
            })
        batch_orig, batch_flip, batch_meta = [], [], []

    for idx, row in sample.iterrows():
        if idx in done_idx:
            continue
        try:
            img = get_image(idx, row["image_url"], CACHE_DIR)
            t_orig = TFM(img)
            t_flip = TFM(img.transpose(Image.FLIP_LEFT_RIGHT))
        except Exception as e:
            n_fail += 1
            continue
        batch_orig.append(t_orig)
        batch_flip.append(t_flip)
        batch_meta.append({"idx": int(idx), "ra": float(row["ra"]), "dec": float(row["dec"]),
                            "class_eq_catalog": row["class_eq"]})
        if len(batch_orig) >= BATCH:
            flush()
            if len(results) % CKPT_EVERY < BATCH:
                pd.DataFrame(results).to_parquet(OUT_PATH)
                elapsed = time.time() - t0
                rate = (len(results) - len(done_idx)) / elapsed if elapsed > 0 else 0
                eta = (n - len(results)) / rate if rate > 0 else float("inf")
                print(f"[{elapsed:.1f}s] {len(results)}/{n} done | {rate:.2f} img/s | fail={n_fail} | ETA {eta/60:.1f}min", flush=True)

    flush()
    pd.DataFrame(results).to_parquet(OUT_PATH)
    elapsed = time.time() - t0
    print(f"[{elapsed:.1f}s] DONE: {len(results)}/{n} pairs computed, {n_fail} failed, saved {OUT_PATH}", flush=True)
    return elapsed, len(results)


if __name__ == "__main__":
    import sys
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else None
    main(limit)
