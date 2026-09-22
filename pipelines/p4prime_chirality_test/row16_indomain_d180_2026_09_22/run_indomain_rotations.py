#!/usr/bin/env python3
"""Inference stage — exact 90-degree rotations of the IN-DOMAIN images, through
the exact released preprocessing and the exact released checkpoint.

Pre-registration: PREREGISTRATION_2026-09-22.md (committed f45c9d1b, BEFORE this
ran). Sample, statistic, controls and decision rule are fixed there.

Images: Smith42/galaxies @ bdd1b063a9a22874a79a4363aa9fb6a2b356a4c2, config
v1.0 (`data/train-*`) -- the files pipelines/p2_chirality/run_eq_fast.py:37 read
to build the released catalogue. 512x512 px RGB JPEG.

Disk is the binding constraint on this machine (~10 GB free, other lanes
running), so nothing is downloaded: row groups are pulled individually by HTTP
range read (HfFileSystem + pyarrow), decoded in memory, inferred, and dropped.
The only artifact written is the probability array.

For theta in {0, 90, 180, 270} (closed under negation mod 360):

    A_theta = TFM( Rot_theta( I   ) )
    B_theta = TFM( Rot_theta( M I ) )        M = FLIP_LEFT_RIGHT

with TFM and the checkpoint loader imported verbatim from
../row16_pa_parity_transfer/run_pa_transfer_inference.py. Rotations are PIL
transposes: lossless pixel permutations of a square image, no interpolation.

Output: indomain_probs.npz -- dr8_id (str, N), probs (float32, N x 2 x 4 x 3)
indexed [galaxy, kind(0=A,1=B), angle, class(cw,ccw,ns)], plus the row-group
manifest and the streamed-byte count.
"""
import io
import json
import os
import shutil
import sys
import time
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np
import pyarrow.parquet as pq
import torch
from PIL import Image
from huggingface_hub import HfFileSystem

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "row16_pa_parity_transfer"))
from run_pa_transfer_inference import TFM, load_model, BATCH  # noqa: E402

OUT = HERE / "indomain_probs.npz"
MANIFEST = HERE / "stream_manifest.json"

REPO = "Smith42/galaxies"
REV = "bdd1b063a9a22874a79a4363aa9fb6a2b356a4c2"
SHARDS = list(range(0, 192, 10))          # 20 shards, evenly spaced over 192
RG_PER_SHARD = 20                         # 20 row groups each -> 400 rg, 40,000 galaxies
SEED = 20260922
ANGLES = [0, 90, 180, 270]
_ROT = {0: None, 90: Image.Transpose.ROTATE_90,
        180: Image.Transpose.ROTATE_180, 270: Image.Transpose.ROTATE_270}
MIN_FREE_GB = 5.0                         # pre-registered abort floor
MAX_WALL_S = 90 * 60                      # pre-registered abort floor (cumulative)
CKPT_EVERY_RG = 20
# Per-invocation cap only: the harness runs foreground commands with a 10-min
# ceiling, so each invocation exits cleanly on a checkpoint and the next one
# resumes. This is bookkeeping, not a change to the pre-registered budget.
PER_RUN_S = float(os.environ.get("RUN_SECONDS", "480"))


def free_gb():
    return shutil.disk_usage(HERE).free / 1e9


def plan():
    """Deterministic row-group plan, seeded, fixed by the pre-registration."""
    rng = np.random.default_rng(SEED)
    return [(s, int(r)) for s in SHARDS
            for r in np.sort(rng.choice(442, RG_PER_SHARD, replace=False))]


def main():
    t0 = time.time()
    fs = HfFileSystem(token=os.environ.get("HF_TOKEN"))
    jobs = plan()

    done_keys, dr8, probs_list, streamed, wall_prev = [], [], [], 0, 0.0
    if OUT.exists():
        prev = np.load(OUT, allow_pickle=True)
        done_keys = [tuple(k) for k in prev["done_keys"].tolist()]
        dr8 = prev["dr8_id"].tolist()
        probs_list = [prev["probs"]]
        streamed = int(prev["streamed_bytes"])
        wall_prev = float(prev["wall_s_total"]) if "wall_s_total" in prev else 0.0
        print(f"[{time.time()-t0:.0f}s] resuming: {len(done_keys)}/{len(jobs)} row groups, "
              f"{len(dr8)} galaxies", flush=True)
    todo = [j for j in jobs if j not in done_keys]

    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    enc, head = load_model(device)
    print(f"[{time.time()-t0:.0f}s] model @237d021c on {device}; "
          f"{len(todo)} row groups to stream; free disk {free_gb():.1f} GB", flush=True)

    # One ParquetFile handle per (thread, shard): a pyarrow ParquetFile over an
    # fsspec stream holds a single file position, so two threads calling
    # read_row_group() on the same handle would interleave seeks. Thread-local
    # handles cost one extra footer read per thread per shard and are safe.
    _tl = threading.local()

    def pf(shard):
        h = getattr(_tl, "handles", None)
        if h is None:
            h = _tl.handles = {}
        if shard not in h:
            p = f"datasets/{REPO}@{REV}/data/train-{shard:05d}-of-00192.parquet"
            h[shard] = pq.ParquetFile(fs.open(p, "rb"))
        return h[shard]

    def fetch(job):
        s, r = job
        return job, pf(s).read_row_group(r)

    def save():
        np.savez_compressed(
            OUT,
            dr8_id=np.array(dr8),
            probs=np.concatenate(probs_list, 0) if len(probs_list) > 1 else probs_list[0],
            done_keys=np.array(done_keys, dtype=np.int32),
            angles=np.array(ANGLES),
            streamed_bytes=np.int64(streamed),
            wall_s_total=np.float64(wall_prev + time.time() - t0),
        )
        if len(probs_list) > 1:
            probs_list[:] = [np.concatenate(probs_list, 0)]

    aborted = None
    # Bounded prefetch: ThreadPoolExecutor.map() would submit all 400 fetches at
    # once (and shutdown(wait=True) would then insist on completing every one of
    # them before the process could exit on the per-invocation cap), so the
    # window is kept explicitly at PREFETCH row groups.
    PREFETCH = 3
    with ThreadPoolExecutor(max_workers=PREFETCH) as pool:
        pending = [pool.submit(fetch, j) for j in todo[:PREFETCH]]
        nxt = PREFETCH
        while pending:
            job, tbl = pending.pop(0).result()
            if nxt < len(todo):
                pending.append(pool.submit(fetch, todo[nxt])); nxt += 1
            if free_gb() < MIN_FREE_GB:
                aborted = f"free disk {free_gb():.1f} GB < {MIN_FREE_GB} GB floor"
                for f_ in pending:
                    f_.cancel()
                break
            if wall_prev + time.time() - t0 > MAX_WALL_S:
                aborted = (f"cumulative wall clock {(wall_prev+time.time()-t0)/60:.0f} min > "
                           f"{MAX_WALL_S/60:.0f} min pre-registered budget")
                for f_ in pending:
                    f_.cancel()
                break
            if time.time() - t0 > PER_RUN_S:
                print(f"[{time.time()-t0:.0f}s] per-invocation cap reached; checkpointing and exiting "
                      f"({len(done_keys)}/{len(jobs)} row groups). Re-run to resume.", flush=True)
                for f_ in pending:
                    f_.cancel()
                break
            imcol = tbl.column("image").to_pylist()
            ids = tbl.column("dr8_id").to_pylist()
            streamed += sum(len(x["bytes"]) for x in imcol)
            buf, meta = [], []
            n0 = len(dr8)
            for gi, rec in enumerate(imcol):
                im = Image.open(io.BytesIO(rec["bytes"])).convert("RGB")
                mi = im.transpose(Image.FLIP_LEFT_RIGHT)
                for ai, th in enumerate(ANGLES):
                    op = _ROT[th]
                    for kind, base in ((0, im), (1, mi)):
                        buf.append(TFM(base if op is None else base.transpose(op)))
                        meta.append((n0 + gi, kind, ai))
            del imcol, tbl
            block = np.full((len(ids), 2, len(ANGLES), 3), np.nan, dtype=np.float32)
            outp = []
            for i in range(0, len(buf), BATCH):
                x = torch.stack(buf[i:i + BATCH]).to(device)
                with torch.no_grad():
                    outp.append(torch.softmax(head(enc(x)), dim=1).float().cpu().numpy())
            p = np.concatenate(outp, 0)
            for j, (g, kind, ai) in enumerate(meta):
                block[g - n0, kind, ai, :] = p[j]
            assert not np.isnan(block).any()
            probs_list.append(block)
            dr8.extend(ids)
            done_keys.append(job)
            if len(done_keys) % CKPT_EVERY_RG == 0:
                save()
                el = time.time() - t0
                print(f"[{el:.0f}s] {len(done_keys)}/{len(jobs)} row groups | {len(dr8)} galaxies "
                      f"| {streamed/1e9:.2f} GB streamed | free {free_gb():.1f} GB "
                      f"| ETA {(len(jobs)-len(done_keys))*el/max(len(done_keys),1)/60:.0f} min", flush=True)

    save()
    man = {
        "preregistration": "PREREGISTRATION_2026-09-22.md (commit f45c9d1b)",
        "dataset": f"{REPO}@{REV} config v1.0 (data/train-*), 512x512 RGB JPEG",
        "model": "bamfai/galaxy-chirality-v2 chirality_model_v2_best.pt @237d021c451d75cf86a875e86d4de498b74e2f12",
        "preprocessing": "Resize((224,224)) -> ToTensor -> Normalize(ImageNet), NO crop; "
                         "rotations are lossless PIL transposes of the 512x512 square",
        "plan": {"shards": SHARDS, "row_groups_per_shard": RG_PER_SHARD, "seed": SEED,
                 "row_groups_planned": len(jobs)},
        "row_groups_completed": len(done_keys),
        "n_galaxies": len(dr8),
        "forward_passes": len(dr8) * 8,
        "streamed_bytes": streamed,
        "streamed_gb": streamed / 1e9,
        "image_bytes_written_to_disk": 0,
        "device": str(device),
        "wall_clock_s": wall_prev + time.time() - t0,
        "complete": len(done_keys) == len(jobs),
        "free_disk_gb_at_end": free_gb(),
        "aborted": aborted,
    }
    MANIFEST.write_text(json.dumps(man, indent=2))
    print(json.dumps({k: v for k, v in man.items() if k != "plan"}, indent=2))


if __name__ == "__main__":
    main()
