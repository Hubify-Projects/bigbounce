#!/usr/bin/env python3
"""
R42 B21 batch-size scaling sweep — sustained H200 workload.

Loads the real chirality_v2 ViT-Small + 3-layer MLP head and runs a
batch-size sweep at 4M synthetic images per batch size. Produces the
throughput-vs-batch-size curve that pins down the cached-logit B20
infrastructure's optimal batch on H200 SXM hardware.

Sweep:
  batch_sizes = [128, 256, 512, 1024, 2048]
  N_per_batch = 4_000_000   # 20M total forward passes
  fp16, no grad, eval mode
  Captures per-batch throughput, GPU memory, and per-batch logit stats.

Expected runtime: 30-50 min sustained at ~99 percent GPU utilization.

Output:
  /workspace/r42_pod_a_outputs/B21_batchsize_sweep.json
  /workspace/r42_pod_a_outputs/B21_running_log.csv
"""
import os, json, time
import numpy as np
import torch
import torch.nn as nn
import timm

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
OUT = "/workspace/r42_pod_a_outputs"
os.makedirs(OUT, exist_ok=True)

print(f"[{time.strftime('%H:%M:%S')}] R42 B21 BATCH-SIZE SWEEP starting", flush=True)
print(f"  device={DEVICE}  torch={torch.__version__}  timm={timm.__version__}", flush=True)
if torch.cuda.is_available():
    print(f"  gpu={torch.cuda.get_device_name(0)}  free={torch.cuda.mem_get_info()[0]/1e9:.1f}GB", flush=True)


class ChiralityHead(nn.Module):
    def __init__(self, in_dim=384, hidden_dims=(512, 256), n_classes=3, dropout=0.1):
        super().__init__()
        self.h = nn.Sequential(
            nn.LayerNorm(in_dim),
            nn.Linear(in_dim, hidden_dims[0]),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dims[0], hidden_dims[1]),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dims[1], n_classes),
        )
    def forward(self, x):
        return self.h(x)

CKPT = "/workspace/analysis3_outputs/chirality_model_v2_best.pt"
ck = torch.load(CKPT, map_location="cpu", weights_only=False)
encoder = timm.create_model("vit_small_patch16_224", pretrained=False, num_classes=0)
encoder.load_state_dict(ck["enc"])
head = ChiralityHead(in_dim=384, n_classes=ck.get("n_classes", 3))
head.load_state_dict(ck["head"])
encoder = encoder.to(DEVICE).half().eval()
head = head.to(DEVICE).half().eval()
print(f"  ckpt val_acc={ck.get('val_acc'):.4f} epoch={ck.get('epoch')}", flush=True)


BATCHES = [128, 256, 512, 1024, 2048]
N_PER = 4_000_000
torch.manual_seed(42); np.random.seed(42)

results = {"per_batch": {}, "model": {
    "encoder": "vit_small_patch16_224",
    "head": "LN+MLP[384->512->256->3]",
    "ckpt": CKPT,
    "val_acc": float(ck.get("val_acc", 0)),
}}

csv_log = open(f"{OUT}/B21_running_log.csv", "w", buffering=1)
csv_log.write("ts,batch,iter,total_fwd,wall_s,img_per_sec,gpu_mem_gb\n")

def run_batch_size(batch, n_imgs):
    print(f"\n[{time.strftime('%H:%M:%S')}] B21 batch={batch} n={n_imgs:,}", flush=True)
    torch.cuda.empty_cache()
    t0 = time.time()
    n_done = 0
    iter_done = 0
    logit_sum = np.zeros(3)
    logit_sumsq = np.zeros(3)
    class_counts = [0, 0, 0]
    max_conf_sum = 0.0
    peak_mem = 0
    with torch.no_grad():
        while n_done < n_imgs:
            n = min(batch, n_imgs - n_done)
            x = torch.randn(n, 3, 224, 224, device=DEVICE, dtype=torch.float16) * 0.3 + 0.5
            x.clamp_(0, 1)
            feat = encoder(x)
            logit = head(feat)
            pred = logit.argmax(dim=1)
            for cls in range(3):
                class_counts[cls] += int((pred == cls).sum().item())
            l_np = logit.float().cpu().numpy()
            logit_sum += l_np.sum(axis=0)
            logit_sumsq += (l_np ** 2).sum(axis=0)
            soft = np.exp(l_np - l_np.max(axis=1, keepdims=True))
            soft /= soft.sum(axis=1, keepdims=True)
            max_conf_sum += soft.max(axis=1).sum()
            n_done += n
            iter_done += 1
            mem = torch.cuda.memory_allocated() / 1e9
            if mem > peak_mem:
                peak_mem = mem
            if iter_done % 100 == 0:
                dt = time.time() - t0
                ips = n_done / dt
                csv_log.write(f"{time.strftime('%H:%M:%S')},{batch},{iter_done},{n_done},{dt:.1f},{ips:.0f},{mem:.2f}\n")
                print(f"    [{time.strftime('%H:%M:%S')}] batch={batch} iter={iter_done} n={n_done:,} ips={ips:.0f} mem={mem:.1f}GB", flush=True)
        torch.cuda.synchronize()
    wall = time.time() - t0
    return {
        "batch_size": batch,
        "n_images": n_done,
        "wall_s": wall,
        "img_per_sec": n_done / wall,
        "iters": iter_done,
        "peak_mem_gb": peak_mem,
        "frac_class_0": class_counts[0] / n_done,
        "frac_class_1": class_counts[1] / n_done,
        "frac_class_2": class_counts[2] / n_done,
        "logit_mean": (logit_sum / n_done).tolist(),
        "logit_std": np.sqrt(logit_sumsq/n_done - (logit_sum/n_done)**2).tolist(),
        "mean_max_conf": max_conf_sum / n_done,
    }

t_start = time.time()
for batch in BATCHES:
    res = run_batch_size(batch, N_PER)
    results["per_batch"][f"b{batch}"] = res
    print(f"  done batch={batch}: ips={res['img_per_sec']:.0f} peak_mem={res['peak_mem_gb']:.1f}GB wall={res['wall_s']:.1f}s", flush=True)

results["total_wall_s"] = time.time() - t_start
results["total_forward_passes"] = sum(r["n_images"] for r in results["per_batch"].values())
results["overall_img_per_sec"] = results["total_forward_passes"] / results["total_wall_s"]
results["computed_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
results["interpretation"] = (
    "B21 batch-size sweep at 4M synthetic images per batch on H200 SXM. "
    "Pins down the throughput-vs-batch-size curve for the cached-logit B20 "
    "infrastructure. Optimal batch is the one that saturates SM occupancy "
    "without spilling memory bandwidth -- expected to peak around 1024-2048 "
    "for ViT-Small at 224x224. The per-batch logit_mean entries should be "
    "identical (within FP32 rounding) across batch sizes since the same "
    "deterministic seed is used; deviations indicate batch-norm-like state "
    "mismatch (there should be none -- pure LN + GELU)."
)

out_path = f"{OUT}/B21_batchsize_sweep.json"
with open(out_path, "w") as fh:
    json.dump(results, fh, indent=2)
csv_log.close()

print(f"\n[{time.strftime('%H:%M:%S')}] B21 SWEEP DONE", flush=True)
print(f"  total: {results['total_forward_passes']:,} fwd, wall={results['total_wall_s']:.1f}s, "
      f"avg ips={results['overall_img_per_sec']:.0f}", flush=True)
for batch in BATCHES:
    r = results["per_batch"][f"b{batch}"]
    print(f"  batch={batch:5d}  ips={r['img_per_sec']:6.0f}  peak_mem={r['peak_mem_gb']:.1f}GB", flush=True)
print(f"  wrote {out_path}", flush=True)
