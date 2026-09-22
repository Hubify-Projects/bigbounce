# REPRODUCIBILITY MANIFEST — `row16-indomain-d180`
### directive Q2, lane `bb-LS10-indomain-d180`, 2026-09-22

Manifest identifier: **`row16-indomain-d180`**. Everything needed to reproduce
the in-domain `d(θ)` and the dilution bound `D` from nothing but this repository
and public endpoints.

## 1. External data sources (pinned)

| source | pin | what it supplies | access |
|---|---|---|---|
| `Smith42/galaxies` (HF dataset) | revision `bdd1b063a9a22874a79a4363aa9fb6a2b356a4c2`, config `v1.0`, `data/train-*` | the 512×512 px grz DESI Legacy DR8 cutouts the released catalogue's inference ran on — provenance table entry A1 | public; `HF_TOKEN` from `.env.local` used for rate limits only |
| `bamfai/galaxy-chirality-v2` (HF model) | revision `237d021c451d75cf86a875e86d4de498b74e2f12`, file `chirality_model_v2_best.pt`, md5 `6f36e97c45a127b0d05ca4fb7f30f636`, 88,046,038 B | the released ViT-S/16 + head checkpoint, `val_acc = 0.9369` | public |
| `pipelines/p2_chirality/apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet` | in repo | the released catalogue's own labels, `primary_hc`, `raw_flip_qc_unsafe`, coordinates (8,474,531 rows) | local |
| `pipelines/p2_chirality/outputs/canonical_provenance/e2e_fullrun/e2e_shards/` | in repo, 192 parquets | the 2026-07-11 full-catalogue in-domain re-run used as control C1 | local |
| `https://www.legacysurvey.org/viewer/jpeg-cutout` | — | 180 diagnostic cutouts for the pixel-scale measurement only | public, no auth |

## 2. APIs used

* HuggingFace Hub HTTP range reads via `huggingface_hub.HfFileSystem` +
  `pyarrow.parquet.ParquetFile.read_row_group` — **individual parquet row groups
  only**, never a file download.
* HuggingFace Hub `hf_hub_download` for the 88 MB checkpoint (the only file
  fetched whole).
* Legacy Survey viewer cutout service (post-hoc diagnostic only).

## 3. Exact scripts, in order

```
# 0. pre-registration (must be committed first)             -> f45c9d1b
# 1. control C1, catalogue scale, local only, ~5 s
python3 pipelines/p4prime_chirality_test/row16_indomain_d180_2026_09_22/c1_e2e_catalogue_agreement.py
# 2. streaming rotation inference, resumable, ~47 min
#    (RUN_SECONDS caps one invocation; re-run until "complete": true)
RUN_SECONDS=480 python3 pipelines/p4prime_chirality_test/row16_indomain_d180_2026_09_22/run_indomain_rotations.py
# 3. controls C2/C3 + the d(theta)/D table, ~3 s
python3 pipelines/p4prime_chirality_test/row16_indomain_d180_2026_09_22/s1_indomain_dilution.py
# 4. post-hoc pixel-scale diagnostic, ~3 min
python3 pipelines/p4prime_chirality_test/row16_indomain_d180_2026_09_22/posthoc_pixel_scale.py
```

`HF_TOKEN` must be exported (`set -a; source .env.local; set +a`). Deterministic:
row-group plan `rng(20260922)`, bootstrap `rng(20260922)`; the forward passes are
deterministic given the checkpoint.

## 4. Compute venue and cost

| | |
|---|---|
| Venue | **local Apple-silicon, `torch` MPS backend** — no RunPod, no GPU rental |
| Money cost | **$0** |
| Wall clock, inference | 46.9 min for 40,000 galaxies × 8 forward passes = 320,000 passes (≈ 224 passes/s) |
| Wall clock, everything else | C1 5 s · analysis 3 s · pixel-scale diagnostic 3.1 min |
| Network | **4.54 GB** streamed (400 row groups × ~11.3 MB) + 88 MB checkpoint + ~10 MB diagnostic cutouts |
| **Disk written** | **0 image bytes.** Total on-disk products of this lane: 3.8 MB (probabilities + JSON + text). The 88 MB checkpoint lands in the shared `~/.cache/huggingface` |
| Free-disk floor | 5 GB, checked every row group; never approached (11.0–11.4 GB free throughout) |
| Reproduction on a fresh machine | ~50 min wall clock, 4.6 GB transfer, < 150 MB disk, $0 |

Why streamed rather than downloaded: one `Smith42/galaxies` train shard is
5.01 GB and the full train split is 2.19 TB (442 row groups of 100 rows per
shard, 192 shards). With ~10 GB free on the Data volume and other lanes running,
a single shard download would have taken the machine to 5 GB free. Row-group
range reads make the disk cost of an arbitrarily large sample zero.

## 5. Incidents, recorded

1. **Discarded checkpoint.** The first 8,000-galaxy run used one shared
   `ParquetFile` handle across prefetch threads. A pyarrow handle over an fsspec
   stream holds a single file position, so concurrent `read_row_group` calls
   could interleave seeks. The checkpoint was **deleted and the run restarted
   clean** with thread-local handles rather than shipped with a correctness
   caveat; no data from the racy version enters any number here.
2. **`ThreadPoolExecutor.map` submits every future immediately**, so
   `shutdown(wait=True)` would have insisted on completing all 400 fetches
   before the process could exit on its per-invocation cap. Replaced with an
   explicit 3-deep prefetch window.
3. **The shared HuggingFace cache was cleared twice mid-run** by another process
   on this machine (`.incomplete` blob vanished under `hf_hub_download`,
   `FileNotFoundError`). Recovered by re-fetching the checkpoint and asserting its
   md5 (`6f36e97c45a127b0d05ca4fb7f30f636`) before resuming; the resumable
   checkpoint meant no forward passes were lost.
4. **Recorded deviation from the pre-registration**: `posthoc_pixel_scale.py`
   fetches 180 Legacy Survey viewer cutouts (~10 MB). The pre-registration did
   not provide for new cutout downloads. It is labelled post-hoc in its own output
   and feeds no pre-registered statistic.

## 6. Artifact inventory (md5 as committed)

| file | bytes | md5 |
|---|---|---|
| `PREREGISTRATION_2026-09-22.md` | 9,696 | `558f3089dd80c2305a94c795b4e0624e` |
| `PROPAGATION_NOTE.md` | 11,733 | `aaebba4f836d854b81d18148a5c6d1d6` |
| `ROW16_INDOMAIN_D180_2026-09-22.md` | 12,710 | `bcebcf49f4888155ccb0ecf2e2422fc0` |
| `c1_e2e_catalogue_agreement.json` | 16,643 | `1cbc04a1662825342e3b5c3d78d0ac1b` |
| `c1_e2e_catalogue_agreement.py` | 4,674 | `c74972e32d10790475f678480bf2a63c` |
| `indomain_probs.npz` | 3,727,030 | `338895d80b3f0ae3bd1b44e1d52c401e` |
| `posthoc_pixel_scale.json` | 1,009 | `fd465c4d50155f2d84e6dd7d15144895` |
| `posthoc_pixel_scale.py` | 4,800 | `9232d12e2585841176471d3287464c5c` |
| `run_indomain_rotations.py` | 9,834 | `006f8354922db6d14e7928c29148ccf6` |
| `s1_indomain_dilution.json` | 6,914 | `aea202c21fbf44956dc36341c333b609` |
| `s1_indomain_dilution.py` | 9,947 | `6883264f0e2e60b7d8e0fe9de1f2381a` |
| `stream_manifest.json` | 1,093 | `0abeab0b3b5b58d546749166e0e75605` |

## 7. Holistic reproduction

This manifest is individually reproducible as above. Within the lab-level
reproduction pass it sits downstream of the P4′ catalogue release
(`p4_catalog_primary_safe_v1.0.244.parquet`) and of the 2026-07-11 `e2e_fullrun`,
and upstream of P4′'s §`sec:robustness_disclosure` dilution bound. It needs
neither a GPU nor a pod, so it can be re-run on any machine with ~5 GB of
transfer budget — which is the point: the number it produces is the one P4′
quotes as its physical-parity floor, and it should be cheap to re-check.
