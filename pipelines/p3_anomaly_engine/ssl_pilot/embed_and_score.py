#!/usr/bin/env python3
"""Row12 pilot: embed + anomaly-score the staged 1M-object pilot corpus AND
the 1,244-object v2 recovery reference set through the trained masked-
spectrum transformer.

Anomaly score = mean reconstruction MSE over a FIXED evaluation mask (the
deterministic 40%-stride mask, not a fresh random mask per object, so
scores are comparable across objects) -- see `train_ssl_model.py`'s
docstring for why this is the same reconstruction-error family as the
archived BigAE's score.

Outputs one Parquet catalog with columns:
    targetid, target_ra, target_dec, survey, program, healpix,
    ssl_anomaly_score, ssl_embedding (128-dim pooled latent, list<float32>)
"""
from __future__ import annotations

import argparse
import glob
import importlib.util
from pathlib import Path

import numpy as np
import torch
import pyarrow as pa
import pyarrow.parquet as pq

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("train_ssl_model", HERE / "train_ssl_model.py")
train_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(train_mod)


def fixed_mask(n_obj: int, seed: int, mask_ratio: float, device) -> torch.Tensor:
    rng = np.random.default_rng(seed)
    n_mask = max(1, int(round(mask_ratio * train_mod.N_PATCHES)))
    mask = torch.zeros(n_obj, train_mod.N_PATCHES, dtype=torch.bool)
    idx = rng.choice(train_mod.N_PATCHES, size=n_mask, replace=False)  # SAME patches masked for every object
    mask[:, idx] = True
    return mask.to(device)


def score_batch(model, x, mask, device):
    b = x.shape[0]
    patches = x.view(b, train_mod.N_PATCHES, train_mod.PATCH)
    emb = model.patch_embed(patches) + model.pos_embed
    emb_masked = torch.where(mask.unsqueeze(-1), model.mask_token.expand(b, train_mod.N_PATCHES, -1), emb)
    latent = model.encoder(emb_masked)
    recon = model.head(latent)
    per_obj_mse = ((recon - patches) ** 2)[mask].view(b, -1).mean(dim=1)
    pooled = model.encoder(emb).mean(dim=1)  # unmasked pooled embedding
    return per_obj_mse.detach().cpu().numpy(), pooled.detach().cpu().numpy()


def load_table(shard_glob: str, extra_cols: list[str]) -> dict:
    paths = sorted(glob.glob(shard_glob))
    cols = ["targetid", "target_ra", "target_dec", "survey", "program", "healpix", "flux"] + extra_cols
    data = {c: [] for c in cols}
    for p in paths:
        t = pq.read_table(p)
        present = [c for c in cols if c in t.column_names]
        for c in present:
            data[c].extend(t.column(c).to_pylist())
    return data


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--checkpoint", type=Path, required=True)
    ap.add_argument("--pilot-shard-glob", required=True)
    ap.add_argument("--v2-flux", type=Path, required=True)
    ap.add_argument("--output-pilot-scores", type=Path, required=True)
    ap.add_argument("--output-v2-scores", type=Path, required=True)
    ap.add_argument("--mask-ratio", type=float, default=0.4)
    ap.add_argument("--eval-seed", type=int, default=999)
    ap.add_argument("--batch-size", type=int, default=2048)
    args = ap.parse_args()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    ckpt = torch.load(args.checkpoint, map_location=device)
    cfg = ckpt["config"]
    model = train_mod.MaskedSpectrumTransformer(
        d_model=cfg["d_model"], n_layers=cfg["n_layers"], n_heads=cfg["n_heads"], d_ff=cfg["d_ff"]
    ).to(device)
    model.load_state_dict(ckpt["model_state"])
    model.eval()

    def run(data: dict, score_key: str):
        X = np.asarray(data["flux"], dtype=np.float32)
        n = X.shape[0]
        scores = np.zeros(n, dtype=np.float32)
        embeddings = np.zeros((n, cfg["d_model"]), dtype=np.float32)
        with torch.no_grad():
            for start in range(0, n, args.batch_size):
                xb = torch.from_numpy(X[start : start + args.batch_size]).to(device)
                mask = fixed_mask(xb.shape[0], args.eval_seed, args.mask_ratio, device)
                s, e = score_batch(model, xb, mask, device)
                scores[start : start + xb.shape[0]] = s
                embeddings[start : start + xb.shape[0]] = e
        return scores, embeddings

    print("scoring pilot corpus...", flush=True)
    pilot = load_table(args.pilot_shard_glob, [])
    pilot_scores, pilot_emb = run(pilot, "ssl_anomaly_score")
    table = pa.table(
        {
            "targetid": pa.array(pilot["targetid"], type=pa.int64()),
            "target_ra": pa.array(pilot["target_ra"], type=pa.float64()),
            "target_dec": pa.array(pilot["target_dec"], type=pa.float64()),
            "survey": pa.array(pilot["survey"], type=pa.string()),
            "program": pa.array(pilot["program"], type=pa.string()),
            "healpix": pa.array(pilot["healpix"], type=pa.int64()),
            "ssl_anomaly_score": pa.array(pilot_scores.tolist(), type=pa.float64()),
            "ssl_embedding": pa.array(pilot_emb.tolist(), type=pa.list_(pa.float32())),
        }
    )
    args.output_pilot_scores.parent.mkdir(parents=True, exist_ok=True)
    pq.write_table(table, args.output_pilot_scores)
    print(f"wrote {len(pilot['targetid'])} pilot scores -> {args.output_pilot_scores}")

    print("scoring v2 reference objects...", flush=True)
    v2_t = pq.read_table(args.v2_flux)
    v2 = {c: v2_t.column(c).to_pylist() for c in v2_t.column_names}
    v2_scores, v2_emb = run(v2, "ssl_anomaly_score")
    v2_table = pa.table(
        {
            "targetid": pa.array(v2["targetid"], type=pa.int64()),
            "target_ra": pa.array(v2["target_ra"], type=pa.float64()),
            "target_dec": pa.array(v2["target_dec"], type=pa.float64()),
            "survey": pa.array(v2["survey"], type=pa.string()),
            "program": pa.array(v2["program"], type=pa.string()),
            "healpix": pa.array(v2["healpix"], type=pa.int64()),
            "ssl_anomaly_score": pa.array(v2_scores.tolist(), type=pa.float64()),
            "anomaly_score_v2": pa.array(v2["anomaly_score_v2"], type=pa.float64()),
        }
    )
    args.output_v2_scores.parent.mkdir(parents=True, exist_ok=True)
    pq.write_table(v2_table, args.output_v2_scores)
    print(f"wrote {len(v2['targetid'])} v2 scores -> {args.output_v2_scores}")


if __name__ == "__main__":
    main()
