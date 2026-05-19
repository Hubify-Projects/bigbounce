#!/usr/bin/env python3
"""
P4 D4-TTA partial-harvest — process whatever's already cached from the v1.0.117
N=10K seed=42 sample (DESI Sky Viewer throttling made the full 10K download
impractical; collapse to ~2,400 cutouts at 45s/cutout).

Drops the download phase entirely; uses only cutouts already present in
~/.cache/p4_d4_tta from the killed v1.0.117 N=10K run. Output:
d4_tta_holdout_partial_results.json (does NOT overwrite v1.0.71 baseline
nor the future-full v1.0.117 output).
"""
from __future__ import annotations
import json, time, os, hashlib, sys
from pathlib import Path
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import timm
from PIL import Image
from torchvision import transforms
from huggingface_hub import hf_hub_download

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
OUT = REPO / "pipelines/p2_chirality/outputs/canonical_provenance"
CACHE = Path.home() / ".cache/p4_d4_tta"
N_SAMPLE = 10_000  # same as v1.0.117 sample, but we only process what's cached
SEED = 42
BATCH = 32


class ChiralityHead(nn.Module):
    def __init__(self):
        super().__init__()
        self.h = nn.Sequential(
            nn.LayerNorm(384),
            nn.Linear(384, 512),
            nn.GELU(),
            nn.Dropout(0.0),
            nn.Linear(512, 256),
            nn.GELU(),
            nn.Dropout(0.0),
            nn.Linear(256, 3),
        )

    def forward(self, x):
        return self.h(x)


def build_model(ckpt_path, device):
    state = torch.load(ckpt_path, map_location=device, weights_only=False)
    backbone = timm.create_model("vit_small_patch16_224", pretrained=False, num_classes=0)
    backbone.load_state_dict(state["enc"], strict=False)
    head = ChiralityHead()
    head.load_state_dict(state["head"], strict=False)

    class Wrapped(nn.Module):
        def __init__(self, b, h):
            super().__init__()
            self.backbone = b
            self.head = h
        def forward(self, x):
            feat = self.backbone.forward_features(x)
            if feat.ndim == 3:
                feat = feat[:, 0]
            return self.head(feat)

    return Wrapped(backbone, head).to(device).eval()


def apply_d4(img, op):
    if op == 0: return img
    if op == 1: return img.rotate(90, resample=Image.BICUBIC)
    if op == 2: return img.rotate(180, resample=Image.BICUBIC)
    if op == 3: return img.rotate(270, resample=Image.BICUBIC)
    if op == 4: return img.transpose(Image.FLIP_LEFT_RIGHT)
    if op == 5: return img.transpose(Image.FLIP_LEFT_RIGHT).rotate(90, resample=Image.BICUBIC)
    if op == 6: return img.transpose(Image.FLIP_LEFT_RIGHT).rotate(180, resample=Image.BICUBIC)
    if op == 7: return img.transpose(Image.FLIP_LEFT_RIGHT).rotate(270, resample=Image.BICUBIC)


def perm_for_op(op):
    return [0, 1, 2] if op < 4 else [1, 0, 2]


def main():
    t0 = time.time()
    print(f"[{time.time()-t0:.1f}s] D4-TTA PARTIAL-HARVEST, N_target={N_SAMPLE}, seed={SEED}", flush=True)
    rng = np.random.default_rng(SEED)

    print(f"[{time.time()-t0:.1f}s] Loading catalog from HF cache ...", flush=True)
    cat_path = hf_hub_download("bamfai/galaxy-chirality-catalog",
                                "catalog_production.parquet", repo_type="dataset")
    df = pd.read_parquet(cat_path)
    spirals = df[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
    idx = rng.choice(len(spirals), size=min(N_SAMPLE, len(spirals)), replace=False)
    sub = spirals.iloc[idx].reset_index(drop=True)
    print(f"[{time.time()-t0:.1f}s] sampled {len(sub)} URLs from same-seed N=10K", flush=True)

    # Filter to cached-only
    paths = []
    cached_idx = []
    for i, url in enumerate(sub["image_url"].values):
        h = hashlib.md5(url.encode()).hexdigest()[:16]
        p = CACHE / f"{h}.jpg"
        if p.exists() and p.stat().st_size > 1000:
            paths.append(p)
            cached_idx.append(i)
    n_cached = len(paths)
    print(f"[{time.time()-t0:.1f}s] cached: {n_cached}/{len(sub)} = {100*n_cached/len(sub):.1f}% of target sample", flush=True)
    sub_cached = sub.iloc[cached_idx].reset_index(drop=True)

    if torch.backends.mps.is_available():
        device = torch.device("mps")
    elif torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")
    print(f"[{time.time()-t0:.1f}s] device: {device}", flush=True)

    ckpt = Path.home() / ".cache/huggingface/hub/models--bamfai--galaxy-chirality-v2/snapshots/369601033392d7ef4a53448727041bf3d86d55e4/chirality_model_v2_best.pt"
    if not ckpt.exists():
        ckpt = Path(hf_hub_download("bamfai/galaxy-chirality-v2", "chirality_model_v2_best.pt"))
    model = build_model(ckpt, device)

    preprocess = transforms.Compose([
        transforms.Resize(224),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    n = n_cached
    probs_d4 = np.zeros((n, 8, 3), dtype=np.float32)
    skipped = np.zeros(n, dtype=bool)
    print(f"[{time.time()-t0:.1f}s] Preloading {n} images ...", flush=True)
    base_imgs = [None] * n
    for i, p in enumerate(paths):
        try:
            img = Image.open(p).convert("RGB")
            base_imgs[i] = img
        except Exception:
            skipped[i] = True
    n_valid = int((~skipped).sum())
    print(f"[{time.time()-t0:.1f}s] valid: {n_valid}, skipped (PIL fail): {n - n_valid}", flush=True)

    print(f"[{time.time()-t0:.1f}s] Running D4 inference ...", flush=True)
    valid_idx = [i for i in range(n) if not skipped[i]]
    for op in range(8):
        tensors = []
        for vi in valid_idx:
            img_o = apply_d4(base_imgs[vi], op)
            tensors.append(preprocess(img_o))
        x = torch.stack(tensors).to(device)
        all_probs = []
        with torch.no_grad():
            for s in range(0, len(x), BATCH):
                batch = x[s:s+BATCH]
                logits = model(batch)
                p = torch.softmax(logits, dim=-1).cpu().numpy()
                all_probs.append(p)
        probs_op = np.concatenate(all_probs, axis=0)
        perm = perm_for_op(op)
        probs_op = probs_op[:, perm]
        for j, vi in enumerate(valid_idx):
            probs_d4[vi, op] = probs_op[j]
        print(f"[{time.time()-t0:.1f}s]   op {op}/8 done", flush=True)

    # Z2 = ops {0,4}; C4 = {0,1,2,3}; D4 = {0..7}
    probs_z2 = probs_d4[valid_idx][:, [0, 4]].mean(axis=1)
    probs_c4 = probs_d4[valid_idx][:, :4].mean(axis=1)
    probs_d4_full = probs_d4[valid_idx].mean(axis=1)

    cw_z2 = (probs_z2.argmax(axis=1) == 0).mean()
    cw_c4 = (probs_c4.argmax(axis=1) == 0).mean()
    cw_d4 = (probs_d4_full.argmax(axis=1) == 0).mean()
    delta_z2_d4_pct = 100.0 * (cw_z2 - cw_d4)

    result = {
        "version": "v1.0.117-d4-tta-holdout-partial-harvest",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "config": {
            "n_sampled_target": int(N_SAMPLE),
            "n_cached": int(n_cached),
            "n_valid": int(n_valid),
            "n_skipped_pil": int(n - n_valid),
            "seed": int(SEED),
            "batch_size": int(BATCH),
            "device": str(device),
            "image_source": "DESI Legacy Sky Viewer ls-dr9 cutouts at 150 px (DESI rate-limit truncated v1.0.117 N=10K to N=" + str(n_valid) + " cached-and-valid)",
        },
        "cw_fraction": {
            "z2_2fold_flip": float(cw_z2),
            "c4_4fold_rotation": float(cw_c4),
            "d4_8fold_full": float(cw_d4),
            "delta_z2_to_d4_pct": float(delta_z2_d4_pct),
        },
        "mean_per_galaxy_probs": {
            "p_cw_z2": float(probs_z2[:, 0].mean()),
            "p_ccw_z2": float(probs_z2[:, 1].mean()),
            "p_ns_z2": float(probs_z2[:, 2].mean()),
            "p_cw_d4": float(probs_d4_full[:, 0].mean()),
            "p_ccw_d4": float(probs_d4_full[:, 1].mean()),
            "p_ns_d4": float(probs_d4_full[:, 2].mean()),
        },
        "comparison_to_v1071_baseline": {
            "v1071_n_valid": 1558,
            "this_n_valid": int(n_valid),
            "v1071_cw_d4_8fold": 0.502106149957877,
            "v1071_delta_z2_to_d4_pct": -1.347935973041281,
            "scaling_ratio": float(n_valid) / 1558.0,
            "expected_statistical_power_tightening_factor": float((float(n_valid) / 1558.0) ** 0.5),
        },
        "notes": (
            "Partial-harvest from the v1.0.117 N=10K seed=42 sample. The DESI "
            "Legacy Sky Viewer rate-limited the full 10K download to a "
            "0.04 cutouts/sec asymptotic rate (200 cutouts per 5249s in the "
            "last poll window); the download was halted at "
            f"~{n_cached} cached / 10000 target ({100*n_cached/N_SAMPLE:.1f}%). "
            "This partial-harvest result uses ONLY the cached subset (no new "
            "downloads); inference completed locally on Apple Silicon MPS. "
            "The v1.0.71 baseline N=1,558 result is preserved as "
            "d4_tta_holdout_results.json; this artifact supersedes it as the "
            f"higher-N statistical-power reference (factor ~{(n_valid/1558)**0.5:.2f}x "
            "uncertainty tightening expected if the true population is independent of "
            "URL-hash partial-cache selection)."
        ),
    }

    out_path = OUT / "d4_tta_holdout_partial_results.json"
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"[{time.time()-t0:.1f}s] wrote {out_path}", flush=True)
    print(f"\n=== headline ===", flush=True)
    print(f"n_valid: {n_valid} (v1.0.71 baseline was 1,558)", flush=True)
    print(f"cw_fraction Z2: {cw_z2:.4f}", flush=True)
    print(f"cw_fraction C4: {cw_c4:.4f}", flush=True)
    print(f"cw_fraction D4: {cw_d4:.4f}", flush=True)
    print(f"delta Z2-D4: {delta_z2_d4_pct:.3f} pp", flush=True)


if __name__ == "__main__":
    main()
