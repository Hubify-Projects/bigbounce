#!/usr/bin/env python3
"""
Equivariant Post-Processing: Produce Catalog C from v2 inference catalog.

For each galaxy in chirality_catalog_v2_full.parquet, re-streams the image from
HuggingFace GZ DESI, runs inference on both the original and its horizontal flip,
and averages predictions using test-time equivariant averaging:

    eq_cw  = (p_cw_orig  + p_ccw_flip) / 2
    eq_ccw = (p_ccw_orig + p_cw_flip)  / 2
    eq_ns  = (p_ns_orig  + p_ns_flip)  / 2

This exploits the physical symmetry: a CW galaxy flipped horizontally becomes CCW,
and vice versa.  The NOT_SPIRAL class is self-symmetric under reflection.

Input:  /workspace/analysis3_outputs/chirality_catalog_v2_full.parquet
Model:  /workspace/analysis3_outputs/chirality_model_v2_best.pt
Output: /workspace/analysis3_outputs/chirality_catalog_production.parquet

Expected runtime: ~140 hours on H100 at ~33 img/s (doubled from v2 due to flip).
Checkpoints every 250K galaxies; resumes from latest checkpoint.
"""

import os
import sys
import time
import json
import threading

import numpy as np
import torch
import torch.nn as nn
import timm
from torchvision import transforms
from datasets import load_dataset
import pandas as pd

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
OUTPUT_DIR = "/workspace/analysis3_outputs"
RAW_CATALOG = f"{OUTPUT_DIR}/chirality_catalog_v2_full.parquet"
MODEL_PATH = f"{OUTPUT_DIR}/chirality_model_v2_best.pt"
OUT_PATH = f"{OUTPUT_DIR}/chirality_catalog_production.parquet"
CKPT_PREFIX = "eq_ckpt_"
BS = 64
CKPT_EVERY = 250_000
HB_INTERVAL = 60  # heartbeat every 60 seconds
CLASS_NAMES = ["CW", "CCW", "NOT_SPIRAL"]

# Ensure HuggingFace authentication
HF_TOKEN = os.environ.get("HF_TOKEN")
if HF_TOKEN:
    print(f"HF_TOKEN set ({len(HF_TOKEN)} chars)", flush=True)
else:
    print("WARNING: HF_TOKEN not set — may fail on gated datasets", flush=True)

# ---------------------------------------------------------------------------
# Model definition (must match training architecture exactly)
# ---------------------------------------------------------------------------
class Head(nn.Module):
    def __init__(self):
        super().__init__()
        self.h = nn.Sequential(
            nn.LayerNorm(384),
            nn.Linear(384, 512),
            nn.GELU(),
            nn.Dropout(0.3),
            nn.Linear(512, 256),
            nn.GELU(),
            nn.Dropout(0.2),
            nn.Linear(256, 3),
        )

    def forward(self, x):
        return self.h(x)


class ChiralityModel(nn.Module):
    def __init__(self, encoder, head):
        super().__init__()
        self.encoder = encoder
        self.head = head

    def forward(self, x):
        return self.head(self.encoder(x))


# ---------------------------------------------------------------------------
# Heartbeat thread
# ---------------------------------------------------------------------------
class Heartbeat:
    """Background thread that logs progress every HB_INTERVAL seconds."""

    def __init__(self):
        self.n_proc = 0
        self.n_total = 0
        self.n_err = 0
        self.t0 = time.time()
        self._stop = threading.Event()
        self._thread = threading.Thread(target=self._run, daemon=True)

    def start(self):
        self._thread.start()

    def stop(self):
        self._stop.set()
        self._thread.join(timeout=5)

    def _run(self):
        while not self._stop.wait(HB_INTERVAL):
            elapsed = time.time() - self.t0
            rate = self.n_proc / elapsed if elapsed > 0 else 0
            eta_h = (self.n_total - self.n_proc) / rate / 3600 if rate > 0 else float("inf")
            print(
                f"  [heartbeat] proc={self.n_proc:,}/{self.n_total:,} "
                f"| {rate:.1f} img/s | err={self.n_err} | ETA {eta_h:.1f}h",
                flush=True,
            )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 72, flush=True)
    print("EQUIVARIANT POST-PROCESSING: Catalog C Production", flush=True)
    print("=" * 72, flush=True)

    # ------------------------------------------------------------------
    # Step 1: Load raw catalog (for id_str lookup set)
    # ------------------------------------------------------------------
    print("\n[1] Loading raw v2 catalog...", flush=True)
    if not os.path.exists(RAW_CATALOG):
        print(f"  ERROR: {RAW_CATALOG} not found. Run v2 inference first.", flush=True)
        sys.exit(1)

    df_raw = pd.read_parquet(RAW_CATALOG)
    n_galaxies = len(df_raw)
    print(f"  Loaded {n_galaxies:,} galaxies from v2 catalog", flush=True)

    # Build lookup set of id_str for matching streamed images to catalog rows
    id_lookup = set(df_raw["id_str"].values)
    # Build dict for fast ra/dec retrieval
    raw_meta = df_raw.set_index("id_str")[["ra", "dec", "p_cw", "p_ccw", "p_ns"]].to_dict("index")
    print(f"  Built lookup index ({len(id_lookup):,} unique IDs)", flush=True)

    # ------------------------------------------------------------------
    # Step 2: Load model
    # ------------------------------------------------------------------
    print("\n[2] Loading v2 model...", flush=True)
    encoder = timm.create_model("vit_small_patch16_224", pretrained=False, num_classes=0)
    head = Head()

    ckpt = torch.load(MODEL_PATH, weights_only=True, map_location="cpu")
    encoder.load_state_dict(ckpt["enc"])
    head.load_state_dict(ckpt["head"])

    model = ChiralityModel(encoder, head).to(DEVICE).eval()
    print(f"  Model loaded (val_acc={ckpt.get('val_acc', 'N/A')})", flush=True)
    print(f"  Device: {DEVICE}", flush=True)

    # Image transform (same as training/inference)
    tfm = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ])

    # ------------------------------------------------------------------
    # Step 3: Check for resume from checkpoint
    # ------------------------------------------------------------------
    print("\n[3] Checking for checkpoint...", flush=True)
    resume_n = 0
    catalog = []

    ckpt_files = sorted([
        f for f in os.listdir(OUTPUT_DIR)
        if f.startswith(CKPT_PREFIX) and f.endswith(".parquet")
    ])
    if ckpt_files:
        latest_ckpt = ckpt_files[-1]
        try:
            df_ckpt = pd.read_parquet(f"{OUTPUT_DIR}/{latest_ckpt}")
            resume_n = len(df_ckpt)
            catalog = df_ckpt.to_dict("records")
            print(f"  Resuming from checkpoint: {latest_ckpt} ({resume_n:,} galaxies)", flush=True)
        except Exception as e:
            print(f"  Failed to load checkpoint {latest_ckpt}: {e}", flush=True)
            resume_n = 0
            catalog = []
    else:
        print("  No checkpoint found — starting fresh", flush=True)

    # Build set of already-processed IDs for resume
    processed_ids = set()
    if resume_n > 0:
        processed_ids = {r["id_str"] for r in catalog}
        print(f"  {len(processed_ids):,} IDs already processed", flush=True)

    # ------------------------------------------------------------------
    # Step 4: Stream GZ DESI and run equivariant inference
    # ------------------------------------------------------------------
    print(f"\n[4] Streaming GZ DESI for equivariant inference (BS={BS})...", flush=True)
    ds = load_dataset("mwalmsley/gz_desi", split="train", streaming=True)
    print("  Dataset iterator ready", flush=True)

    hb = Heartbeat()
    hb.n_total = n_galaxies
    hb.n_proc = resume_n
    hb.t0 = time.time()
    hb.start()

    t0 = time.time()
    n_streamed = 0
    n_proc = resume_n
    n_err = 0
    n_skip_not_in_catalog = 0

    # Batch accumulators
    batch_tensors = []  # original image tensors
    batch_meta = []     # metadata dicts

    # Track last checkpoint / progress count to avoid duplicates
    last_ckpt_count = resume_n
    last_progress_count = resume_n

    for row in ds:
        n_streamed += 1

        # Extract id_str
        id_str = str(row.get("id_str", ""))

        # Skip if not in our v2 catalog
        if id_str not in id_lookup:
            n_skip_not_in_catalog += 1
            continue

        # Skip if already processed (resume)
        if id_str in processed_ids:
            continue

        # Get image
        img = row.get("image")
        if img is None:
            n_err += 1
            continue

        try:
            tensor = tfm(img)
        except Exception:
            n_err += 1
            continue

        # Look up raw catalog metadata
        meta = raw_meta.get(id_str)
        if meta is None:
            n_err += 1
            continue

        batch_tensors.append(tensor)
        batch_meta.append({
            "id_str": id_str,
            "ra": meta["ra"],
            "dec": meta["dec"],
            "p_cw_raw": meta["p_cw"],
            "p_ccw_raw": meta["p_ccw"],
            "p_ns_raw": meta["p_ns"],
        })

        # Process batch when full
        if len(batch_tensors) >= BS:
            _process_batch(model, batch_tensors, batch_meta, catalog)
            n_proc += len(batch_tensors)
            hb.n_proc = n_proc
            hb.n_err = n_err
            batch_tensors = []
            batch_meta = []

            # Progress logging every 5K
            if n_proc >= last_progress_count + 5000:
                last_progress_count = (n_proc // 5000) * 5000
                elapsed = time.time() - t0
                rate = (n_proc - resume_n) / elapsed if elapsed > 0 else 0
                remaining = n_galaxies - n_proc
                eta_h = remaining / rate / 3600 if rate > 0 else float("inf")
                print(
                    f"    {n_proc:>10,}/{n_galaxies:,} | streamed={n_streamed:,} "
                    f"| {rate:.1f}/s | ETA {eta_h:.1f}h | err={n_err} skip={n_skip_not_in_catalog}",
                    flush=True,
                )

            # Checkpoint every CKPT_EVERY
            if n_proc >= last_ckpt_count + CKPT_EVERY:
                last_ckpt_count = (n_proc // CKPT_EVERY) * CKPT_EVERY
                ckpt_path = f"{OUTPUT_DIR}/{CKPT_PREFIX}{last_ckpt_count:08d}.parquet"
                pd.DataFrame(catalog).to_parquet(ckpt_path)
                print(f"    *** CHECKPOINT {n_proc:,} -> {ckpt_path} ***", flush=True)

    # Flush remaining batch
    if batch_tensors:
        _process_batch(model, batch_tensors, batch_meta, catalog)
        n_proc += len(batch_tensors)
        batch_tensors = []
        batch_meta = []

    hb.stop()
    elapsed_total = time.time() - t0

    # ------------------------------------------------------------------
    # Step 5: Build and save production catalog
    # ------------------------------------------------------------------
    print(f"\n[5] Building production catalog ({n_proc:,} galaxies)...", flush=True)

    df_prod = pd.DataFrame(catalog)

    if len(df_prod) == 0:
        print("  ERROR: No galaxies processed!", flush=True)
        sys.exit(1)

    # Derive class labels and confidence from raw and equivariant probabilities
    # Raw class
    raw_probs = df_prod[["p_cw_raw", "p_ccw_raw", "p_ns_raw"]].values
    raw_cls_idx = raw_probs.argmax(axis=1)
    df_prod["class_raw"] = [CLASS_NAMES[i] for i in raw_cls_idx]
    df_prod["confidence_raw"] = raw_probs.max(axis=1)

    # Equivariant class
    eq_probs = df_prod[["p_cw_eq", "p_ccw_eq", "p_ns_eq"]].values
    eq_cls_idx = eq_probs.argmax(axis=1)
    df_prod["class_eq"] = [CLASS_NAMES[i] for i in eq_cls_idx]
    df_prod["confidence_eq"] = eq_probs.max(axis=1)

    # Reorder columns to match spec
    col_order = [
        "id_str", "ra", "dec",
        "p_cw_raw", "p_ccw_raw", "p_ns_raw",
        "p_cw_eq", "p_ccw_eq", "p_ns_eq",
        "class_raw", "class_eq",
        "confidence_raw", "confidence_eq",
    ]
    df_prod = df_prod[col_order]

    df_prod.to_parquet(OUT_PATH, index=False)
    print(f"  Saved: {OUT_PATH} ({len(df_prod):,} rows)", flush=True)

    # ------------------------------------------------------------------
    # Step 6: Summary statistics
    # ------------------------------------------------------------------
    print(f"\n[6] Summary statistics", flush=True)

    n_total = len(df_prod)
    for label in ["raw", "eq"]:
        col = f"class_{label}"
        n_cw = (df_prod[col] == "CW").sum()
        n_ccw = (df_prod[col] == "CCW").sum()
        n_ns = (df_prod[col] == "NOT_SPIRAL").sum()
        n_spiral = n_cw + n_ccw
        cw_frac = n_cw / n_spiral if n_spiral > 0 else 0
        print(f"  [{label.upper()}] CW={n_cw:,} CCW={n_ccw:,} NS={n_ns:,} "
              f"CW/(CW+CCW)={cw_frac:.6f}", flush=True)

    # Reclassification statistics
    changed = (df_prod["class_raw"] != df_prod["class_eq"]).sum()
    print(f"  Reclassified by equivariant averaging: {changed:,} ({changed/n_total*100:.2f}%)", flush=True)

    # Mean confidence shift
    conf_shift = (df_prod["confidence_eq"] - df_prod["confidence_raw"]).mean()
    print(f"  Mean confidence shift (eq - raw): {conf_shift:+.4f}", flush=True)

    # Flip consistency: |p_cw_eq - p_ccw_eq| for spirals (should be more symmetric)
    spirals_eq = df_prod[df_prod["class_eq"].isin(["CW", "CCW"])]
    if len(spirals_eq) > 0:
        asym = (spirals_eq["p_cw_eq"] - spirals_eq["p_ccw_eq"]).abs().mean()
        print(f"  Mean |p_cw_eq - p_ccw_eq| for spirals: {asym:.4f}", flush=True)

    # Save summary JSON
    summary = {
        "n_total": int(n_total),
        "n_processed": int(n_proc),
        "n_errors": int(n_err),
        "n_streamed": int(n_streamed),
        "n_skip_not_in_catalog": int(n_skip_not_in_catalog),
        "runtime_hours": float(elapsed_total / 3600),
        "rate_per_sec": float((n_proc - resume_n) / elapsed_total) if elapsed_total > 0 else 0,
        "raw": {
            "n_cw": int((df_prod["class_raw"] == "CW").sum()),
            "n_ccw": int((df_prod["class_raw"] == "CCW").sum()),
            "n_ns": int((df_prod["class_raw"] == "NOT_SPIRAL").sum()),
        },
        "equivariant": {
            "n_cw": int((df_prod["class_eq"] == "CW").sum()),
            "n_ccw": int((df_prod["class_eq"] == "CCW").sum()),
            "n_ns": int((df_prod["class_eq"] == "NOT_SPIRAL").sum()),
        },
        "n_reclassified": int(changed),
        "mean_confidence_shift": float(conf_shift),
    }
    summary_path = f"{OUTPUT_DIR}/equivariant_postprocess_summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"  Summary: {summary_path}", flush=True)

    print(f"\n{'=' * 72}", flush=True)
    print(
        f"EQUIVARIANT POST-PROCESSING COMPLETE: {n_proc:,} galaxies | "
        f"{elapsed_total/3600:.1f}h | {changed:,} reclassified",
        flush=True,
    )
    print(f"  Output: {OUT_PATH}", flush=True)
    print(f"{'=' * 72}", flush=True)


def _process_batch(model, batch_tensors, batch_meta, catalog):
    """
    Run equivariant inference on a batch.

    For each image:
        - Forward pass on original  -> p_orig = [p_cw_orig, p_ccw_orig, p_ns_orig]
        - Forward pass on h-flipped -> p_flip = [p_cw_flip, p_ccw_flip, p_ns_flip]
        - Equivariant average:
            eq_cw  = (p_cw_orig  + p_ccw_flip) / 2
            eq_ccw = (p_ccw_orig + p_cw_flip)  / 2
            eq_ns  = (p_ns_orig  + p_ns_flip)  / 2
    """
    bt_orig = torch.stack(batch_tensors).to(DEVICE)
    bt_flip = torch.flip(bt_orig, [3])  # horizontal flip along width dimension

    with torch.no_grad():
        logits_orig = model(bt_orig)
        logits_flip = model(bt_flip)
        probs_orig = torch.softmax(logits_orig, dim=1).cpu().numpy()
        probs_flip = torch.softmax(logits_flip, dim=1).cpu().numpy()

    for i, meta in enumerate(batch_meta):
        p_cw_orig = probs_orig[i, 0]
        p_ccw_orig = probs_orig[i, 1]
        p_ns_orig = probs_orig[i, 2]

        p_cw_flip = probs_flip[i, 0]
        p_ccw_flip = probs_flip[i, 1]
        p_ns_flip = probs_flip[i, 2]

        # Equivariant averaging: flipping swaps CW <-> CCW, NS stays
        eq_cw = (p_cw_orig + p_ccw_flip) / 2.0
        eq_ccw = (p_ccw_orig + p_cw_flip) / 2.0
        eq_ns = (p_ns_orig + p_ns_flip) / 2.0

        catalog.append({
            "id_str": meta["id_str"],
            "ra": meta["ra"],
            "dec": meta["dec"],
            "p_cw_raw": meta["p_cw_raw"],
            "p_ccw_raw": meta["p_ccw_raw"],
            "p_ns_raw": meta["p_ns_raw"],
            "p_cw_eq": float(eq_cw),
            "p_ccw_eq": float(eq_ccw),
            "p_ns_eq": float(eq_ns),
        })


if __name__ == "__main__":
    main()
