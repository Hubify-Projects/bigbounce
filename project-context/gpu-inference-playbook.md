# GPU Inference Playbook: Lessons from the 8.47M Galaxy Chirality Pipeline

**Date:** 2026-03-28
**Author:** Houston Golden + Claude
**Hardware:** NVIDIA H200 (143GB VRAM), 176 CPU cores, 1.7TB RAM

## The 32x Speedup: What We Learned

We processed 8.47M galaxy images through a ViT-Small model with equivariant post-processing (2 forward passes per image). Our first approach took **29 minutes per shard** (44K images). After optimization, we got it to **~65 seconds per shard** — a **32x speedup**.

### What DIDN'T work (lessons learned the hard way)

| Approach | Time/shard | Why it failed |
|----------|-----------|---------------|
| Serial PIL decode + small batch (BS=128) | 29 min | GPU idle 95% of the time waiting for CPU |
| `ProcessPoolExecutor` (32 workers) | 27 min | Serializing PIL images across process boundaries is expensive |
| Streaming from HuggingFace | 35/s | Network-bound, can't batch, iterator dies after 1 shard |
| `load_dataset` non-streaming | Crashes | Tries to load entire dataset into RAM |
| Larger batch size alone (BS=512) | 27 min | Didn't help because CPU decode was the bottleneck, not GPU |

### What WORKED: torch DataLoader with forked workers

```python
from torch.utils.data import Dataset, DataLoader

class ShardDataset(Dataset):
    def __init__(self, dataframe, transform):
        self.df = dataframe
        self.tfm = transform

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        img = Image.open(io.BytesIO(row['image']['bytes']))
        return str(row['dr8_id']), self.tfm(img), self.tfm(img.transpose(Image.FLIP_LEFT_RIGHT))

loader = DataLoader(
    dataset,
    batch_size=512,       # Large batch — fill the GPU
    num_workers=16,       # Fork-based parallelism — shared memory, no serialization
    pin_memory=True,      # Pre-stage tensors in pinned CPU memory for fast GPU transfer
    prefetch_factor=4,    # Pre-decode 4 batches ahead while GPU processes current
)
```

**Why this works:**
1. `num_workers=16` forks 16 processes that share the parent's memory (copy-on-write). No serialization of image data across process boundaries.
2. `pin_memory=True` puts decoded tensors in pinned (page-locked) memory, enabling async CPU→GPU transfer.
3. `prefetch_factor=4` decodes 4 future batches while the GPU processes the current one — the CPU and GPU work simultaneously.
4. `batch_size=512` fully utilizes the GPU (H200 has 143GB VRAM, model uses ~2GB, batch uses ~1.5GB).

### The key insight

**The bottleneck in large-scale image inference is almost NEVER the GPU.** It's CPU-side image decoding and data transfer. The torch DataLoader with forked workers is the canonical solution because:

- Fork-based multiprocessing shares the parent's data (no pickle/serialize overhead)
- Pin memory + prefetch creates a pipeline where CPU and GPU work simultaneously
- The GPU never waits for data

## Cookbook: Applying This to Any Dataset

### Step 1: Download data to local disk first
```python
from huggingface_hub import hf_hub_download
path = hf_hub_download(repo_id="...", filename="shard.parquet", ...)
df = pd.read_parquet(path)
```
Never stream from network during inference. Always download first.

### Step 2: Wrap in a Dataset
```python
class MyDataset(Dataset):
    def __init__(self, df, transform):
        self.df = df
        self.tfm = transform
    def __len__(self): return len(self.df)
    def __getitem__(self, idx):
        # Decode image, apply transform, return tensor
        ...
```

### Step 3: DataLoader with the magic settings
```python
loader = DataLoader(
    dataset,
    batch_size=512,          # As large as GPU can handle
    num_workers=16,          # ~10-25% of CPU cores
    pin_memory=True,         # Always for GPU inference
    prefetch_factor=4,       # 2-8 depending on decode cost
    persistent_workers=False # Set True if reusing loader across epochs
)
```

### Step 4: Non-blocking GPU transfer
```python
for batch in loader:
    x = batch.to(device, non_blocking=True)  # Async transfer
    with torch.no_grad():
        output = model(x)
```

### Step 5: Process shard-by-shard for large datasets
- Download 1 shard → read parquet → DataLoader → save results → delete shard → next
- Save per-shard checkpoint files for crash recovery
- Clean caches periodically (`gc.collect()`, `torch.cuda.empty_cache()`)

## Performance Reference

| Dataset size | Images/shard | Time/shard | Total time | Hardware |
|-------------|-------------|-----------|-----------|----------|
| 8.47M (Smith42/galaxies) | 44,139 | ~65s | ~3.5h | H200 |
| 8.47M (same, 2x forward) | 44,139 | ~65s | ~3.5h | H200 |

### Scaling rules of thumb
- **GPU time scales linearly** with batch count: halve batch_size → 2x GPU time
- **Decode time scales inversely** with num_workers (up to ~16-32, then diminishing)
- **Download time is fixed** per shard (~15-30s for 5GB on RunPod)
- **Total = max(decode_time, gpu_time) + download_time** (they pipeline)

## Common Pitfalls

1. **Don't use `ProcessPoolExecutor` for images** — it serializes data across process boundaries. Use `DataLoader` which uses fork().
2. **Don't stream from HuggingFace during inference** — download the shard first, then process from local disk.
3. **Don't read 5GB parquets with `pd.read_parquet` and iterate rows** — this is 10x slower than wrapping in a Dataset.
4. **Don't forget `pin_memory=True`** — without it, CPU→GPU transfer blocks the pipeline.
5. **Don't set num_workers too high** — 16-32 is optimal; more causes context-switch overhead.
6. **Don't hold all shards in memory** — process one at a time, save results, delete, next.
7. **Always save per-shard checkpoints** — if the process dies at shard 150/192, you resume from 150, not 0.

## Files

- Fast equivariant script: `pipelines/p2_chirality/run_eq_dataloader.py`
- Original slow script: `pipelines/p2_chirality/run_eq_fast.py` (for comparison)
- Smith42 inference: `pipelines/p2_chirality/run_v2_smith42.py`
