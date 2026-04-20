#!/usr/bin/env python3
"""Path-C CMB native re-score (fire #96).

Loads the fire-#95 native-retrained CMB autoencoder (`best_cmb_native.pt`,
val_loss 0.4437, injection-recovery 100% at 5x noise) and the 2x10^5 masked
Planck SMICA patch tensor (`cmb_native_patches.npy`), runs forward-pass
inference in batches, computes per-patch reconstruction MSE as the anomaly
score, and writes:

  outputs/cmb_native/cmb_native_all_scores.parquet   # full 200K x (idx, glon, glat, raw_std, anomaly_score)
  outputs/cmb_native/cmb_native_anomalies.parquet    # top-200 by anomaly score (matches Paper 3 Table 1 canonical CMB count)
  outputs/cmb_native/rescore_summary.json            # headline numbers + threshold stats

Architecture matches `cmb_native_retrain.py` CMBAutoencoder exactly:
  Conv2d(1,16,3,s2,p1)-BN-ReLU -> Conv2d(16,32,3,s2,p1)-BN-ReLU ->
  Conv2d(32,64,3,s2,p1)-BN-ReLU -> Flatten -> Linear(64*8*8, 128)
  Linear(128, 64*8*8)-ReLU -> reshape(64,8,8) ->
  ConvT(64,32,3,s2,p1,op1)-BN-ReLU -> ConvT(32,16,...) -> ConvT(16,1,3,s2,p1,op1)-Tanh

Path-C exit criterion #3: native anomaly set published alongside cross-transfer
200-patch set in Paper 3 Table 1.
"""
import json, os, time
from pathlib import Path
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
import pyarrow as pa
import pyarrow.parquet as pq

WORK = Path(os.environ.get("WORK", "/workspace/bigbounce_scan"))
OUT = WORK / "outputs" / "cmb_native"
CKPT = OUT / "best_cmb_native.pt"
PATCHES = OUT / "cmb_native_patches.npy"
META = OUT / "cmb_native_metadata.json"
BATCH = int(os.environ.get("BATCH", "256"))
TOPN = int(os.environ.get("TOPN", "200"))  # Paper 3 Table 1 canonical CMB anomaly count


class CMBAutoencoder(nn.Module):
    def __init__(self, latent=128):
        super().__init__()
        self.encoder_conv = nn.Sequential(
            nn.Conv2d(1, 16, 3, 2, 1), nn.BatchNorm2d(16), nn.ReLU(True),
            nn.Conv2d(16, 32, 3, 2, 1), nn.BatchNorm2d(32), nn.ReLU(True),
            nn.Conv2d(32, 64, 3, 2, 1), nn.BatchNorm2d(64), nn.ReLU(True),
        )
        self.encoder_fc = nn.Sequential(nn.Flatten(), nn.Linear(64*8*8, latent))
        self.decoder_fc = nn.Sequential(nn.Linear(latent, 64*8*8), nn.ReLU(True))
        self.decoder_conv = nn.Sequential(
            nn.ConvTranspose2d(64, 32, 3, 2, 1, 1), nn.BatchNorm2d(32), nn.ReLU(True),
            nn.ConvTranspose2d(32, 16, 3, 2, 1, 1), nn.BatchNorm2d(16), nn.ReLU(True),
            nn.ConvTranspose2d(16, 1,  3, 2, 1, 1), nn.Tanh(),
        )

    def forward(self, x):
        h = self.encoder_conv(x)
        z = self.encoder_fc(h)
        d = self.decoder_fc(z).view(-1, 64, 8, 8)
        return self.decoder_conv(d), z


def main():
    t0 = time.time()
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[rescore] device={device} batch={BATCH}", flush=True)

    print(f"[rescore] loading patches: {PATCHES}", flush=True)
    patches = np.load(PATCHES, mmap_mode="r")
    N = patches.shape[0]
    print(f"[rescore] N={N} shape={patches.shape} dtype={patches.dtype}", flush=True)

    print(f"[rescore] loading metadata: {META}", flush=True)
    with open(META) as f:
        meta = json.load(f)
    assert len(meta) == N, f"metadata len {len(meta)} != N {N}"

    print(f"[rescore] loading checkpoint: {CKPT}", flush=True)
    ckpt = torch.load(CKPT, map_location=device, weights_only=False)
    state = ckpt["model"] if isinstance(ckpt, dict) and "model" in ckpt else ckpt
    model = CMBAutoencoder().to(device)
    model.load_state_dict(state)
    model.eval()

    scores = np.empty(N, dtype=np.float32)
    # ensure channel dim
    X = torch.from_numpy(np.ascontiguousarray(patches)).float()
    if X.ndim == 3:
        X = X.unsqueeze(1)  # (N,1,H,W)
    elif X.ndim == 4 and X.shape[1] != 1:
        X = X.permute(0, 3, 1, 2)
    ds = TensorDataset(X)
    loader = DataLoader(ds, batch_size=BATCH, shuffle=False, num_workers=0, pin_memory=(device == "cuda"))

    i = 0
    with torch.no_grad():
        for (xb,) in loader:
            xb = xb.to(device, non_blocking=True)
            rec, _ = model(xb)
            err = ((rec - xb) ** 2).mean(dim=(1, 2, 3))
            scores[i:i + err.shape[0]] = err.detach().cpu().numpy()
            i += err.shape[0]
            if i % (BATCH * 50) == 0:
                print(f"[rescore] {i}/{N}  rate={i/(time.time()-t0):.0f}/s", flush=True)
    print(f"[rescore] DONE {i}/{N}  elapsed={time.time()-t0:.1f}s", flush=True)

    idx = np.array([m["idx"] for m in meta], dtype=np.int64)
    glon = np.array([m["glon_deg"] for m in meta], dtype=np.float32)
    glat = np.array([m["glat_deg"] for m in meta], dtype=np.float32)
    raw_std = np.array([m["raw_std"] for m in meta], dtype=np.float32)

    tbl = pa.table({
        "idx": idx,
        "glon_deg": glon,
        "glat_deg": glat,
        "raw_std": raw_std,
        "anomaly_score": scores,
    })
    all_path = OUT / "cmb_native_all_scores.parquet"
    pq.write_table(tbl, all_path, compression="snappy")
    print(f"[rescore] wrote {all_path} ({N} rows)", flush=True)

    # top-N anomalies
    order = np.argsort(-scores)[:TOPN]
    top_tbl = pa.table({
        "idx": idx[order],
        "glon_deg": glon[order],
        "glat_deg": glat[order],
        "raw_std": raw_std[order],
        "anomaly_score": scores[order],
        "rank": np.arange(TOPN, dtype=np.int32),
    })
    top_path = OUT / "cmb_native_anomalies.parquet"
    pq.write_table(top_tbl, top_path, compression="snappy")
    print(f"[rescore] wrote {top_path} (top {TOPN})", flush=True)

    summary = {
        "n_patches": int(N),
        "topn": int(TOPN),
        "score_min": float(scores.min()),
        "score_max": float(scores.max()),
        "score_mean": float(scores.mean()),
        "score_median": float(np.median(scores)),
        "score_p99": float(np.percentile(scores, 99.0)),
        "score_p999": float(np.percentile(scores, 99.9)),
        "topn_min_score": float(top_tbl.column("anomaly_score").to_numpy().min()),
        "topn_max_score": float(top_tbl.column("anomaly_score").to_numpy().max()),
        "elapsed_s": float(time.time() - t0),
        "checkpoint": str(CKPT),
        "patches_src": str(PATCHES),
        "gate_ref": "injection_recovery.json (recovery_fraction=1.0 @ 5x noise, fire #95)",
    }
    with open(OUT / "rescore_summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"[rescore] summary: {json.dumps(summary, indent=2)}", flush=True)


if __name__ == "__main__":
    main()
