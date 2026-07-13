# COMPUTE_ROUTING.md — Where Science Runs (Decision Doctrine)

> Distilled from what the bigbounce program actually did across P1–P5. The
> single most expensive mistake in scientific compute is provisioning a GPU for
> a job whose bottleneck is **not** FLOPs. **Before provisioning anything, ask:
> is the bottleneck compute, data-access, or provenance?** Only the first is a
> GPU problem.

---

## 1. Decision table — workload → venue

| Workload | Scale / character | Venue | Why | Calibration point |
|---|---|---|---|---|
| **Symbolic math / derivations / small numerics** | seconds–minutes, CPU | **Local CPU** | trivial FLOPs; latency to a pod exceeds runtime | NJL gap equation (`arxiv/scripts/njl_gap_equation_route1.py`); c15 channel-native Fisher (`research/focused_paper_source_integration/scripts/c15_channel_native_fisher.py`); P5 RSD bound (`pipelines/p5_desi_chirality/scripts/27_rsd_void_recon_bound.py`) |
| **Medium data sweeps** | ≤ ~1M rows | **Local CPU / Apple MPS** | fits in memory; pod round-trip + upload not worth it | P2/P4 meta-null sweeps |
| **GPU inference / training** OR **≥ ~5M-object sweeps** | millions of objects, real FLOP load, HF-streamable inputs | **RunPod A100** | GPU + `/gpu-dataloader-pattern` (32× via `num_workers=16, pin_memory, prefetch_factor=4, batch=512`) actually pays off | **P4 e2e mirror-flip full run: N=8,474,531 galaxies, A100, ≈ $12.44** (cap $20), inputs stream from HF at ~1000 obj/s |
| **Archive-bound jobs** | multi-day, network-throttled | **NOT a GPU job** — run on any CPU host, gated by download bandwidth | wall-clock is I/O, not FLOPs; a GPU idles while you wait on the archive | 22.5M-spectrum full DESI-DR1 re-pull from SPARCL — **archive-bound, multi-day, don't provision A100** (`P3_REINFERENCE_PLAN.md`, commit `e70e418e`) |

**The rule:** HF-streamable millions-of-objects inference → RunPod. Archive re-pull throttled by SPARCL/NOIRLab bandwidth → do NOT provision GPU; the pod would sit idle behind the network.

---

## 2. RunPod lifecycle rules

- **STOP, never TERMINATE.** A `terminate` typo destroys `/workspace` irrecoverably.
- **backup-3plus before every stop AND every ~2h milestone AND session-end** — not just before stop (directive E). Three confirmed sinks: **local disk + HuggingFace (`bamfai/*`) + Backblaze B2** (+ Convex metadata). `/backup-3plus` aborts the destructive action if fewer than 3 confirmed. Runner: `pipelines/backup_runpod.sh`.
- **Cost gates:** auto-proceed ≤ **$60**; Houston-gate above. (P4 e2e ran $12.44 under a self-imposed $20 cap.)
- **Skill pointers:** `/runpod-lifecycle` (provision/stop), `/gpu-dataloader-pattern` (the 32× loader — refuse serial PIL / per-image ProcessPoolExecutor / HF streaming in production), `/idle-gpu-rescue` (a provisioned-but-idle pod is money burning — rescue or stop it), `/pod-backup-before-stop`.
- **Pod coords** live in `.env.local` (`POD_COBAYA_R43_V2_*`); never single-source pod data.

---

## 3. Worked examples from the ledger

**DP3-15 — the canonical "looks like a GPU job, isn't" case.**
The P3 held-out re-inference (`pipelines/p3_anomaly_engine/dp3_15_heldout_reinference.py`) *appeared* to demand a GPU re-inference over the released 22.5M-object DESI anomaly catalog. Diagnosis first:
- **Compute?** The defensible held-out re-inference (5-seed ensemble on a 20,000-spectrum real SPARCL substrate) ran **`"device": "cpu (local)"`, `"wall_seconds": 9.8`** — trivial. No GPU needed.
- **Data-access?** A SPARCL probe showed only **49/500 = 9.8%** of real-tid rows resolve → only ~1.31% of the catalog is re-pullable; the remainder is **structurally bounded** by what the public archive exposes, not by compute.
- **Provenance?** The full 22.5M re-pull's input feature tensor was **pod-lost**; regenerating it is a multi-day, network-throttled SPARCL re-download — **archive-bound, not GPU-bound.**

Verdict recorded in the plan: **"COST-GATE DECISION: DO NOT PROVISION A RUNPOD POD."** The whole job was a 9.8s local CPU run plus a structural bound plus a provenance note — provisioning an A100 would have burned money on an idle GPU behind a throttled archive.

**Contrast — P4 e2e** legitimately went to A100: 8.47M-object forward-pass injection with HF-streamable inputs at ~1000 obj/s → real FLOP load, real 32× dataloader payoff, $12.44 well spent.

---

## 4. Cost ledger of past runs

| Run | Venue | Scale | Cost | Source |
|---|---|---|---|---|
| P4 e2e mirror-flip full run | RunPod A100 | 8,474,531 galaxies, 2 forward passes | **≈ $12.44** (cap $20) | `pipelines/p2_chirality/outputs/canonical_provenance/e2e_fullrun/RUN_SUMMARY.md` (runner commit `afd4f73b`) |
| P4 e2e pilot | local | mirror-flip transfer-function pilot | negligible | `pipelines/p2_chirality/outputs/canonical_provenance/e2e_mirror_flip_transfer_function.json` |
| DP3-15 held-out re-inference | **local CPU** | 5-seed ensemble on 20k SPARCL spectra, 9.8s | **$0.00** | `pipelines/p3_anomaly_engine/outputs/dp3_15_heldout_reinference.json` |
| P3 Stage-A SPARCL probe | local (network) | ~1 min | **$0.00** | `project-context/P3_REINFERENCE_PLAN.md` |
| P3 full 22.5M re-pull (declined) | would be archive-bound multi-day | 22.5M spectra | not run — do-not-provision | `P3_REINFERENCE_PLAN.md`, commit `e70e418e` |
| NJL gap eq / c15 Fisher / RSD bound | local CPU | symbolic + small numerics | negligible | `arxiv/scripts/`, `research/…/scripts/c15_…`, `pipelines/p5_…/scripts/27_rsd_…` |

**Takeaway:** the program's realized GPU spend on the open-compute science queue is dominated by the single justified $12.44 P4 run. Every other closure was CPU-local because the bottleneck was math, memory, or archive bandwidth — never FLOPs. Diagnose the bottleneck before you provision.
