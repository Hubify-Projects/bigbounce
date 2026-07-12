#!/usr/bin/env python3
"""
OPEN-COMPUTE directive-L, P4 #1 recurring MAJOR closure (image-level end-to-end).

The paper's chirality dilution factor is g = 2a - 1 = 0.398 (a = 0.6991),
inferred from the GZ1 human-vs-classifier confusion matrix. The recurring
reviewer MAJOR: injection-recovery is performed on the HARD-LABEL healpix
field only; nothing traverses the ACTUAL ViT classifier at the image level,
so there is no end-to-end (image -> classifier -> label) chirality transfer
function.

The cleanest possible image-level chirality injection is a MIRROR FLIP: a
left-right flip of a real galaxy image is a physically exact chirality
inversion (CW <-> CCW) that requires NO synthetic image generation. Under a
perfectly parity-equivariant classifier, flipping the image would flip the
predicted class with probability 1. The MEASURED probability that the class
flips is the end-to-end image-level chirality transfer function, which we
compare against the paper's assumed hard-label dilution g = 0.398.

Definitions (per pair = original image + its horizontal mirror):
  - "flip-recovered": original predicted CW/CCW AND mirror predicted the
    OPPOSITE spiral class (CW->CCW or CCW->CW). This is the deterministic
    parity response the paper's g assumes.
  - transfer function T = P(flip detected | original is a confident spiral)
    over CW/CCW-original pairs.
  - We also report a signed effective g_img derived from the flip-confusion
    matrix, analogous to g = 2a - 1.

Model: bamfai/galaxy-chirality-v2 (ViT-Small/16 + 3-class head, val_acc 0.937).
Images: mwalmsley/gz_desi (HF streaming), the same source used for production
inference (run_v2_inference.py).

Preprocessing matches run_v2_inference.py EXACTLY:
  Resize(224,224) -> ToTensor -> Normalize(ImageNet).

Output artifact:
  pipelines/p2_chirality/outputs/canonical_provenance/e2e_mirror_flip_transfer_function.json
"""
from __future__ import annotations

import os
import sys
import json
import time
import argparse
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
import timm
from PIL import Image
from torchvision import transforms
from datasets import load_dataset
from huggingface_hub import hf_hub_download

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "outputs" / "canonical_provenance" / "e2e_mirror_flip_transfer_function.json"
CLASS_NAMES = ["CW", "CCW", "NS"]


def build_model(device):
    tok = os.environ.get("HF_TOKEN")
    ckpt_path = hf_hub_download(
        "bamfai/galaxy-chirality-v2", "chirality_model_v2_best.pt",
        repo_type="model", token=tok,
    )
    ckpt = torch.load(ckpt_path, map_location="cpu", weights_only=True)

    class Head(nn.Module):
        def __init__(self):
            super().__init__()
            self.h = nn.Sequential(
                nn.LayerNorm(384), nn.Linear(384, 512), nn.GELU(), nn.Dropout(0.3),
                nn.Linear(512, 256), nn.GELU(), nn.Dropout(0.2), nn.Linear(256, 3),
            )

        def forward(self, x):
            return self.h(x)

    encoder = timm.create_model("vit_small_patch16_224", pretrained=False, num_classes=0)
    head = Head()
    encoder.load_state_dict(ckpt["enc"])
    head.load_state_dict(ckpt["head"])

    class Model(nn.Module):
        def __init__(self, e, h):
            super().__init__()
            self.e = e
            self.h = h

        def forward(self, x):
            return self.h(self.e(x))

    model = Model(encoder, head).to(device).eval()
    return model, float(ckpt.get("val_acc", float("nan"))), ckpt_path


TFM = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])


def to_rgb(img):
    if not isinstance(img, Image.Image):
        img = Image.fromarray(np.asarray(img))
    return img.convert("RGB")


@torch.no_grad()
def classify_batch(model, pil_imgs, device):
    xs = torch.stack([TFM(im) for im in pil_imgs]).to(device)
    probs = torch.softmax(model(xs), dim=1).cpu().numpy()
    return probs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=2500, help="target CW/CCW-original pairs")
    ap.add_argument("--scan", type=int, default=40000, help="max raw galaxies to scan")
    ap.add_argument("--bs", type=int, default=64)
    ap.add_argument("--conf", type=float, default=0.0,
                    help="min original spiral confidence to count in transfer fn")
    args = ap.parse_args()

    device = torch.device(
        "mps" if torch.backends.mps.is_available()
        else ("cuda" if torch.cuda.is_available() else "cpu")
    )
    t0 = time.time()
    print(f"[{time.time()-t0:.1f}s] device={device}", flush=True)

    model, val_acc, ckpt_path = build_model(device)
    print(f"[{time.time()-t0:.1f}s] model loaded (val_acc={val_acc:.4f})", flush=True)

    ds = load_dataset("mwalmsley/gz_desi", split="train", streaming=True)
    print(f"[{time.time()-t0:.1f}s] dataset stream ready", flush=True)

    # confusion[orig_class][mirror_class], indices 0=CW 1=CCW 2=NS
    conf = np.zeros((3, 3), dtype=np.int64)
    # per-pair records restricted to CW/CCW originals
    n_pairs = 0            # CW/CCW originals seen
    n_flip_recovered = 0   # CW->CCW or CCW->CW
    n_stay_spiral_same = 0 # CW->CW or CCW->CCW (parity violation of expectation)
    n_to_ns = 0            # spiral original -> mirror NS
    n_scanned = 0
    conf_kept = 0          # originals passing --conf
    conf_kept_flip = 0

    orig_conf_list = []
    mirror_conf_list = []

    buf_orig, buf_mirror = [], []

    def flush(buf_orig, buf_mirror):
        nonlocal n_pairs, n_flip_recovered, n_stay_spiral_same, n_to_ns
        nonlocal conf_kept, conf_kept_flip
        if not buf_orig:
            return
        po = classify_batch(model, buf_orig, device)
        pm = classify_batch(model, buf_mirror, device)
        for i in range(len(buf_orig)):
            oc = int(po[i].argmax())
            mc = int(pm[i].argmax())
            if oc in (0, 1):  # original is a spiral
                conf[oc, mc] += 1
                n_pairs += 1
                orig_conf_list.append(float(po[i].max()))
                mirror_conf_list.append(float(pm[i].max()))
                flipped = (oc == 0 and mc == 1) or (oc == 1 and mc == 0)
                if flipped:
                    n_flip_recovered += 1
                elif mc == oc:
                    n_stay_spiral_same += 1
                elif mc == 2:
                    n_to_ns += 1
                if float(po[i].max()) >= args.conf:
                    conf_kept += 1
                    if flipped:
                        conf_kept_flip += 1

    for row in ds:
        n_scanned += 1
        if n_scanned > args.scan:
            break
        img = row.get("image")
        if img is None:
            continue
        try:
            im = to_rgb(img)
        except Exception:
            continue
        mir = im.transpose(Image.FLIP_LEFT_RIGHT)
        buf_orig.append(im)
        buf_mirror.append(mir)
        if len(buf_orig) >= args.bs:
            flush(buf_orig, buf_mirror)
            buf_orig, buf_mirror = [], []
        if n_pairs >= args.n:
            break
        if n_scanned % 2000 == 0:
            rate = n_scanned / max(time.time() - t0, 1e-6)
            T = n_flip_recovered / n_pairs if n_pairs else 0.0
            print(f"[{time.time()-t0:.1f}s] scanned={n_scanned:,} pairs={n_pairs:,} "
                  f"T={T:.3f} ({rate:.0f} gal/s)", flush=True)

    flush(buf_orig, buf_mirror)

    # Transfer function
    T = n_flip_recovered / n_pairs if n_pairs else float("nan")
    T_conf = conf_kept_flip / conf_kept if conf_kept else float("nan")

    # Effective image-level chirality accuracy under the flip test.
    # Among CW/CCW originals whose mirror is ALSO classified CW/CCW (the pool
    # the paper's symmetric-error g addresses), the fraction that flips
    # correctly is the image-level analogue of the per-class accuracy a.
    spiral_spiral = int(conf[0, 0] + conf[0, 1] + conf[1, 0] + conf[1, 1])
    correct_flip_ss = int(conf[0, 1] + conf[1, 0])
    a_img = correct_flip_ss / spiral_spiral if spiral_spiral else float("nan")
    g_img = 2 * a_img - 1 if spiral_spiral else float("nan")

    # Wilson-ish binomial std on T
    se_T = np.sqrt(T * (1 - T) / n_pairs) if n_pairs else float("nan")

    result = {
        "purpose": "end-to-end image-level chirality transfer function via mirror-flip injection through the ACTUAL ViT classifier",
        "model": "bamfai/galaxy-chirality-v2 (ViT-Small/16 + 3-class head)",
        "model_ckpt": str(ckpt_path),
        "model_val_acc": val_acc,
        "image_source": "mwalmsley/gz_desi (HF streaming) — same source as run_v2_inference.py",
        "preprocessing": "Resize(224,224)->ToTensor->Normalize(ImageNet) [matches run_v2_inference.py]",
        "device": str(device),
        "n_scanned": n_scanned,
        "n_pairs_cw_ccw_original": n_pairs,
        "flip_confusion_matrix_orig_to_mirror": {
            "rows_orig": CLASS_NAMES,
            "cols_mirror": CLASS_NAMES,
            "counts": conf.tolist(),
        },
        "n_flip_recovered_CWtoCCW_or_CCWtoCW": n_flip_recovered,
        "n_stayed_same_spiral_class": n_stay_spiral_same,
        "n_spiral_original_to_NS_mirror": n_to_ns,
        "transfer_function_T": T,
        "transfer_function_T_stderr": se_T,
        "transfer_function_T_conf_gate": {"min_orig_conf": args.conf, "value": T_conf, "n": conf_kept},
        "image_level_flip_accuracy_a_img_spiral_spiral_pool": a_img,
        "image_level_g_img_2a_img_minus_1": g_img,
        "paper_assumed_hard_label_g": 0.398,
        "paper_assumed_a": 0.6991,
        "orig_conf_mean": float(np.mean(orig_conf_list)) if orig_conf_list else float("nan"),
        "mirror_conf_mean": float(np.mean(mirror_conf_list)) if mirror_conf_list else float("nan"),
        "interpretation": (
            "T is the end-to-end probability that a physically exact chirality "
            "inversion (image mirror-flip) is registered by the ACTUAL classifier. "
            "T=1 => perfect parity equivariance; the paper's dilution g=2a-1 would "
            "then be a conservative lower bound set by human(GZ1)-label noise, not "
            "classifier noise. T<1 substantially => the classifier itself dilutes "
            "the chirality signal at the image level, and g must reflect the "
            "image-level a_img, not just the GZ1 cross-match a=0.6991."
        ),
        "runtime_sec": round(time.time() - t0, 1),
        "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2))
    print("\n" + "=" * 70, flush=True)
    print(f"pairs (CW/CCW original)      : {n_pairs:,}", flush=True)
    print(f"flip-recovered (CW<->CCW)    : {n_flip_recovered:,}", flush=True)
    print(f"transfer function T          : {T:.4f} +/- {se_T:.4f}", flush=True)
    print(f"image-level a_img (SS pool)  : {a_img:.4f}", flush=True)
    print(f"image-level g_img = 2a-1     : {g_img:.4f}   (paper assumes g=0.398)", flush=True)
    print(f"confusion (orig->mirror):\n{conf}", flush=True)
    print(f"wrote {OUT}", flush=True)


if __name__ == "__main__":
    main()
