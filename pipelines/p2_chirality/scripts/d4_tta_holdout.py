#!/usr/bin/env python3
"""
P4 D4-TTA holdout — LOCAL Apple Silicon MPS run.

Closes CG-C-5 / GM-C-1 / GR-C-2: quantifies the rotational-variance
contribution that the paper's 2-fold flip TTA (Z2 only) leaves on the
table vs the full D4 (8-fold) test-time augmentation.

Architecture (matches bamfai/galaxy-chirality-v2):
  - backbone: ViT-Small/16 (timm vit_small_patch16_224, embed_dim=384)
    loaded from state['enc']
  - head: 4-Linear MLP (384 -> 512 -> 256 -> 3) with LayerNorm + dropout
    loaded from state['head']

D4 mapping: rotations preserve CW/CCW; flips swap CW<->CCW.
After each transform, permute output probs back to the original
(CW, CCW, NS) frame before averaging.
"""
from __future__ import annotations
import json, time, os, hashlib, sys, io
from pathlib import Path
import urllib.request, urllib.error
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import timm
from PIL import Image
from torchvision import transforms
from concurrent.futures import ThreadPoolExecutor, as_completed
from huggingface_hub import hf_hub_download

REPO = Path("/Users/houstongolden/Desktop/CODE_2025/bigbounce")
OUT = REPO / "pipelines/p2_chirality/outputs/canonical_provenance"
CACHE = Path.home() / ".cache/p4_d4_tta"
CACHE.mkdir(parents=True, exist_ok=True)
N_SAMPLE = 2000
SEED = 42
BATCH = 32
DL_WORKERS = 4


class ChiralityHead(nn.Module):
    """Match the bamfai head: keys h.0/h.1/h.4/h.7 are the parametric layers."""
    def __init__(self):
        super().__init__()
        # h.0 = LayerNorm(384), h.1 = Linear(384,512),
        # h.4 = Linear(512,256), h.7 = Linear(256,3).
        # The intermediate indices are activation+dropout (no parameters).
        self.h = nn.Sequential(
            nn.LayerNorm(384),          # 0
            nn.Linear(384, 512),        # 1
            nn.GELU(),                  # 2 (no params)
            nn.Dropout(0.0),            # 3 (no params)
            nn.Linear(512, 256),        # 4
            nn.GELU(),                  # 5
            nn.Dropout(0.0),            # 6
            nn.Linear(256, 3),          # 7
        )

    def forward(self, x):
        return self.h(x)


def build_model(ckpt_path: Path, device: torch.device) -> nn.Module:
    state = torch.load(ckpt_path, map_location=device, weights_only=False)
    enc_state = state["enc"]
    head_state = state["head"]

    backbone = timm.create_model("vit_small_patch16_224", pretrained=False, num_classes=0)
    miss, unx = backbone.load_state_dict(enc_state, strict=False)
    print(f"  backbone missing={len(miss)} unexpected={len(unx)}", flush=True)

    head = ChiralityHead()
    miss, unx = head.load_state_dict(head_state, strict=False)
    print(f"  head missing={len(miss)} unexpected={len(unx)}", flush=True)

    class Wrapped(nn.Module):
        def __init__(self, backbone, head):
            super().__init__()
            self.backbone = backbone
            self.head = head
        def forward(self, x):
            feat = self.backbone.forward_features(x)
            # ViT features: take CLS token (first token).
            if feat.ndim == 3:
                feat = feat[:, 0]
            return self.head(feat)

    return Wrapped(backbone, head).to(device).eval()


def apply_d4(img: Image.Image, op: int) -> Image.Image:
    if op == 0:   return img
    if op == 1:   return img.rotate(90, resample=Image.BICUBIC)
    if op == 2:   return img.rotate(180, resample=Image.BICUBIC)
    if op == 3:   return img.rotate(270, resample=Image.BICUBIC)
    if op == 4:   return img.transpose(Image.FLIP_LEFT_RIGHT)
    if op == 5:   return img.transpose(Image.FLIP_LEFT_RIGHT).rotate(90, resample=Image.BICUBIC)
    if op == 6:   return img.transpose(Image.FLIP_LEFT_RIGHT).rotate(180, resample=Image.BICUBIC)
    if op == 7:   return img.transpose(Image.FLIP_LEFT_RIGHT).rotate(270, resample=Image.BICUBIC)
    raise ValueError(op)


def perm_for_op(op: int) -> list[int]:
    """Map model output (CW, CCW, NS) back to original frame.
    Ops 0-3 (identity + rotations): no permutation.
    Ops 4-7 (with horizontal flip): swap CW <-> CCW.
    """
    return [0, 1, 2] if op < 4 else [1, 0, 2]


def download_one(url_and_path, max_retries: int = 4):
    url, p = url_and_path
    if p.exists() and p.stat().st_size > 1000:
        return True
    delay = 0.5
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(
                url,
                headers={
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15 bigbounce-paper-arxiv",
                    "Accept": "image/jpeg, image/png, */*",
                },
            )
            with urllib.request.urlopen(req, timeout=20) as r:
                data = r.read()
            if len(data) < 500:
                time.sleep(delay)
                delay *= 2
                continue
            p.write_bytes(data)
            return True
        except urllib.error.HTTPError as e:
            if e.code in (429, 503, 502, 504):
                time.sleep(delay)
                delay *= 2
                continue
            return False
        except Exception:
            time.sleep(delay)
            delay *= 2
    return False


def main():
    t0 = time.time()
    print(f"[{time.time()-t0:.1f}s] D4-TTA LOCAL run, N={N_SAMPLE}, seed={SEED}", flush=True)

    rng = np.random.default_rng(SEED)

    print(f"[{time.time()-t0:.1f}s] Loading catalog from HF cache ...", flush=True)
    cat_path = hf_hub_download("bamfai/galaxy-chirality-catalog",
                                "catalog_production.parquet", repo_type="dataset")
    df = pd.read_parquet(cat_path)
    print(f"[{time.time()-t0:.1f}s] catalog: {len(df):,} rows", flush=True)
    spirals = df[df["class_eq"].isin(["CW", "CCW"])].reset_index(drop=True)
    print(f"[{time.time()-t0:.1f}s] spirals available: {len(spirals):,}", flush=True)
    idx = rng.choice(len(spirals), size=min(N_SAMPLE, len(spirals)), replace=False)
    sub = spirals.iloc[idx].reset_index(drop=True)
    print(f"[{time.time()-t0:.1f}s] sampled {len(sub)} spirals", flush=True)

    print(f"[{time.time()-t0:.1f}s] Downloading {len(sub)} cutouts (parallel x{DL_WORKERS}) ...", flush=True)
    jobs = []
    paths = []
    for i, url in enumerate(sub["image_url"].values):
        h = hashlib.md5(url.encode()).hexdigest()[:16]
        p = CACHE / f"{h}.jpg"
        paths.append(p)
        if not (p.exists() and p.stat().st_size > 1000):
            jobs.append((url, p))
    print(f"[{time.time()-t0:.1f}s]   {len(jobs)} to fetch ({len(sub)-len(jobs)} cached)", flush=True)
    failed = 0
    completed = 0
    if jobs:
        with ThreadPoolExecutor(max_workers=DL_WORKERS) as ex:
            futs = {ex.submit(download_one, j): j for j in jobs}
            for f in as_completed(futs):
                ok = f.result()
                completed += 1
                if not ok:
                    failed += 1
                if completed % 200 == 0:
                    print(f"[{time.time()-t0:.1f}s]   fetched {completed}/{len(jobs)} (fail={failed})", flush=True)
    print(f"[{time.time()-t0:.1f}s] download done: {failed} failures", flush=True)

    if torch.backends.mps.is_available():
        device = torch.device("mps")
    elif torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")
    print(f"[{time.time()-t0:.1f}s] device: {device}", flush=True)

    print(f"[{time.time()-t0:.1f}s] Building model from local cache ...", flush=True)
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

    print(f"[{time.time()-t0:.1f}s] Running D4 inference ({len(sub)} galaxies x 8 orientations) ...", flush=True)
    n = len(sub)
    probs_d4 = np.zeros((n, 8, 3), dtype=np.float32)
    skipped = np.zeros(n, dtype=bool)

    # Preload all images to RAM once (saves 7 reads per galaxy).
    print(f"[{time.time()-t0:.1f}s] Preloading {n} images into memory ...", flush=True)
    base_imgs = [None] * n
    for i, p in enumerate(paths):
        if p.exists() and p.stat().st_size > 1000:
            try:
                base_imgs[i] = Image.open(p).convert("RGB").copy()
            except Exception:
                skipped[i] = True
        else:
            skipped[i] = True
    n_loaded = n - int(skipped.sum())
    print(f"[{time.time()-t0:.1f}s]   loaded {n_loaded}/{n} (skipped {int(skipped.sum())})", flush=True)

    for op in range(8):
        t_op = time.time()
        for b_start in range(0, n, BATCH):
            b_end = min(n, b_start + BATCH)
            tensors = []
            idxs = []
            for i in range(b_start, b_end):
                if skipped[i] or base_imgs[i] is None:
                    continue
                try:
                    tensors.append(preprocess(apply_d4(base_imgs[i], op)))
                    idxs.append(i)
                except Exception:
                    skipped[i] = True
            if not tensors:
                continue
            batch = torch.stack(tensors).to(device)
            with torch.no_grad():
                logits = model(batch)
                probs = torch.softmax(logits, dim=1).cpu().numpy()
            perm = perm_for_op(op)
            for j, i in enumerate(idxs):
                probs_d4[i, op, :] = probs[j, perm]
        print(f"[{time.time()-t0:.1f}s]   op {op}: {time.time()-t_op:.1f}s", flush=True)

    valid_mask = ~skipped
    valid_n = int(valid_mask.sum())
    print(f"[{time.time()-t0:.1f}s] valid inferences: {valid_n}/{n}", flush=True)

    probs_z2 = probs_d4[:, [0, 4], :].mean(axis=1)
    probs_d4_avg = probs_d4.mean(axis=1)
    probs_c4 = probs_d4[:, :4, :].mean(axis=1)

    def cw_frac(probs):
        argmax = probs.argmax(axis=1)
        n_cw = ((argmax == 0) & valid_mask).sum()
        n_ccw = ((argmax == 1) & valid_mask).sum()
        return n_cw / max(n_cw + n_ccw, 1)

    pcw_z2 = float(cw_frac(probs_z2))
    pcw_d4 = float(cw_frac(probs_d4_avg))
    pcw_c4 = float(cw_frac(probs_c4))

    rot_std = probs_d4[:, :4, 0].std(axis=1)
    flip_std = probs_d4[:, [0, 4], 0].std(axis=1)
    d4_std = probs_d4[:, :, 0].std(axis=1)

    argmax_z2 = probs_z2[valid_mask].argmax(axis=1)
    argmax_d4 = probs_d4_avg[valid_mask].argmax(axis=1)
    flip_rate = (argmax_z2 != argmax_d4).mean()
    both_spiral = (argmax_z2 != 2) & (argmax_d4 != 2)
    cw_flip_rate = ((argmax_z2[both_spiral] == 0) != (argmax_d4[both_spiral] == 0)).mean() if both_spiral.sum() > 0 else 0.0

    p_cw_z2_mean = probs_z2[valid_mask][:, 0].mean()
    p_cw_d4_mean = probs_d4_avg[valid_mask][:, 0].mean()
    p_ccw_z2_mean = probs_z2[valid_mask][:, 1].mean()
    p_ccw_d4_mean = probs_d4_avg[valid_mask][:, 1].mean()

    print(f"\n=== RESULTS ===", flush=True)
    print(f"Sampled {N_SAMPLE} spirals; valid inferences: {valid_n}", flush=True)
    print(f"CW-fraction:", flush=True)
    print(f"  2-fold flip TTA (Z2):       {pcw_z2:.5f}", flush=True)
    print(f"  4-fold rotation TTA (C4):   {pcw_c4:.5f}", flush=True)
    print(f"  8-fold full D4 TTA:         {pcw_d4:.5f}", flush=True)
    print(f"  delta (Z2 -> D4): {(pcw_d4 - pcw_z2)*100:+.4f}%", flush=True)
    print(f"\nMean per-galaxy p_CW (TTA-averaged):", flush=True)
    print(f"  Z2: {p_cw_z2_mean:.4f}; D4: {p_cw_d4_mean:.4f}; delta {(p_cw_d4_mean - p_cw_z2_mean):+.5f}", flush=True)
    print(f"  Z2 p_CCW: {p_ccw_z2_mean:.4f}; D4 p_CCW: {p_ccw_d4_mean:.4f}", flush=True)
    print(f"\nPer-galaxy std of p_CW across orientations:", flush=True)
    print(f"  C4 rotation:   median={np.median(rot_std[valid_mask]):.4f}, p95={np.percentile(rot_std[valid_mask], 95):.4f}, max={rot_std[valid_mask].max():.4f}", flush=True)
    print(f"  Z2 flip-only:  median={np.median(flip_std[valid_mask]):.4f}, p95={np.percentile(flip_std[valid_mask], 95):.4f}", flush=True)
    print(f"  D4 full:       median={np.median(d4_std[valid_mask]):.4f}, p95={np.percentile(d4_std[valid_mask], 95):.4f}", flush=True)
    print(f"\nClass argmax flip rate Z2 -> D4: {flip_rate*100:.3f}%", flush=True)
    print(f"CW vs CCW flip rate (confident spirals): {cw_flip_rate*100:.3f}%", flush=True)

    out = {
        "version": "v1.0.71-d4-tta-holdout-local",
        "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "config": {
            "n_sampled": int(N_SAMPLE),
            "n_valid": valid_n,
            "n_skipped": int(skipped.sum()),
            "seed": SEED,
            "batch_size": BATCH,
            "device": str(device),
            "model_repo": "bamfai/galaxy-chirality-v2",
            "model_val_acc": 0.9368777275085449,
            "image_source": "DESI Legacy Sky Viewer ls-dr9 cutouts at native size 150 px",
            "preprocessing": "resize-then-center-crop to 224 + ImageNet mean/std normalization",
        },
        "cw_fraction": {
            "z2_2fold_flip": pcw_z2,
            "c4_4fold_rotation": pcw_c4,
            "d4_8fold_full": pcw_d4,
            "delta_z2_to_d4_pct": (pcw_d4 - pcw_z2) * 100,
        },
        "mean_per_galaxy_probs": {
            "p_cw_z2": float(p_cw_z2_mean),
            "p_cw_d4": float(p_cw_d4_mean),
            "p_ccw_z2": float(p_ccw_z2_mean),
            "p_ccw_d4": float(p_ccw_d4_mean),
        },
        "per_galaxy_std_across_orientations": {
            "c4_rotation": {
                "median": float(np.median(rot_std[valid_mask])),
                "p95": float(np.percentile(rot_std[valid_mask], 95)),
                "max": float(rot_std[valid_mask].max()),
            },
            "z2_flip": {
                "median": float(np.median(flip_std[valid_mask])),
                "p95": float(np.percentile(flip_std[valid_mask], 95)),
            },
            "d4_full": {
                "median": float(np.median(d4_std[valid_mask])),
                "p95": float(np.percentile(d4_std[valid_mask], 95)),
            },
        },
        "class_flip_rate": {
            "any_class_z2_to_d4_pct": float(flip_rate * 100),
            "cw_vs_ccw_among_confident_spirals_pct": float(cw_flip_rate * 100),
        },
        "interpretation": (
            "The paper's 2-fold flip TTA is Z2-equivariant by construction "
            "(symmetric in CW<->CCW). Full D4 (8-fold) TTA additionally "
            "averages over the 4 in-plane rotations. The delta_z2_to_d4_pct "
            "quantifies the residual rotational systematic NOT cancelled by "
            "Z2-flip TTA alone. The per-galaxy std of p_CW across rotations "
            "(c4_rotation) is the rotational-variance bound: small values "
            "mean ViT-Small is approximately rotation-invariant on DESI "
            "Legacy spirals and the paper's 2-fold restriction is safe; large "
            "values would mean residual systematics."
        ),
    }
    OUT.mkdir(parents=True, exist_ok=True)
    out_path = OUT / "d4_tta_holdout_results.json"
    out_path.write_text(json.dumps(out, indent=2))
    print(f"\nSaved -> {out_path}", flush=True)
    print(f"Total wall: {time.time()-t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
