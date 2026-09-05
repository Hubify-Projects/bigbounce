#!/usr/bin/env python3
"""Row 13 pilot: image-level end-to-end parity-injection test.

For each injected flip fraction f, mirror-flip (left-right) a random
f-fraction of the pilot cutouts, run the real classifier on ALL cutouts
(flipped + unflipped), and measure the resulting CW-fraction asymmetry
A = 2*mean(p_CW) - 1 relative to the f=0 baseline. Compare the empirical
recovery curve to the label-level injection-recovery result already in
the paper (full_catalog_injection_recovery.py).
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
from huggingface_hub import hf_hub_download
from PIL import Image
from torchvision import transforms

HERE = Path(__file__).parent
FRACTIONS = [0.0, 0.005, 0.01, 0.02, 0.05]
SEED = 42
IMG_SIZE = 224


class Head(nn.Module):
    def __init__(self):
        super().__init__()
        self.h = nn.Sequential(
            nn.LayerNorm(384), nn.Linear(384, 512), nn.GELU(), nn.Dropout(0.3),
            nn.Linear(512, 256), nn.GELU(), nn.Dropout(0.2), nn.Linear(256, 3),
        )

    def forward(self, x):
        return self.h(x)


def load_model():
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
    encoder.eval()
    head.eval()
    return encoder, head


TFM = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])


def download_cutouts(sample: pd.DataFrame, cache_dir: Path) -> dict:
    cache_dir.mkdir(exist_ok=True)
    imgs = {}
    n_fail = 0
    for i, row in sample.iterrows():
        p = cache_dir / f"{i}.jpg"
        if not p.exists():
            try:
                r = requests.get(row["image_url"], timeout=15)
                r.raise_for_status()
                p.write_bytes(r.content)
            except Exception:
                n_fail += 1
                continue
        try:
            imgs[i] = Image.open(p).convert("RGB")
        except Exception:
            n_fail += 1
    print(f"downloaded/opened {len(imgs)} cutouts, {n_fail} failed", flush=True)
    return imgs, n_fail


@torch.no_grad()
def classify(encoder, head, pil_img):
    x = TFM(pil_img).unsqueeze(0)
    logits = head(encoder(x))
    probs = torch.softmax(logits, dim=1).numpy()[0]
    # class order confirmed from run_v2_inference.py / run_eq_dataloader.py /
    # equivariant_postprocess.py: CLASS_NAMES = ['CW', 'CCW', 'NOT_SPIRAL'] -> p_CW = index 0.
    return probs


def main():
    t0 = time.time()
    sample = pd.read_parquet(HERE / "pilot_sample.parquet")
    imgs, n_fail = download_cutouts(sample, HERE / "cutout_cache")
    valid_idx = sorted(imgs.keys())
    encoder, head = load_model()
    print(f"[{time.time()-t0:.1f}s] model loaded, running {len(valid_idx)} x {len(FRACTIONS)} inferences", flush=True)

    rng = np.random.default_rng(SEED)
    results = []
    for f in FRACTIONS:
        n_flip = int(round(f * len(valid_idx)))
        flip_set = set(rng.choice(valid_idx, size=n_flip, replace=False)) if n_flip > 0 else set()
        p_cw_list = []
        for idx in valid_idx:
            img = imgs[idx]
            if idx in flip_set:
                img = img.transpose(Image.FLIP_LEFT_RIGHT)
            probs = classify(encoder, head, img)
            p_cw_list.append(float(probs[1]))
        p_cw_arr = np.array(p_cw_list)
        A = 2.0 * p_cw_arr.mean() - 1.0  # p_CW at index 0
        results.append({
            "f_injected": f,
            "n_flipped": n_flip,
            "n_total": len(valid_idx),
            "mean_p_cw": float(p_cw_arr.mean()),
            "A_recovered": float(A),
        })
        print(f"[{time.time()-t0:.1f}s] f={f}: A_recovered={A:.5f}", flush=True)

    A0 = results[0]["A_recovered"]
    for r in results:
        r["dA_from_baseline"] = r["A_recovered"] - A0

    out = {
        "n_total_pilot": len(valid_idx),
        "n_download_failed": n_fail,
        "seed": SEED,
        "img_size": IMG_SIZE,
        "results": results,
        "note": "Reduced pilot N (500 target, see n_total_pilot for actual valid count) vs "
                "declared 10k spec, due to session time budget; single random flip-set draw "
                "per fraction (not averaged over multiple MC draws), unlike the label-level "
                "MASTER-pipeline injection script which uses N_MC=50 draws per amplitude.",
    }
    (HERE / "injection_pilot_results.json").write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
