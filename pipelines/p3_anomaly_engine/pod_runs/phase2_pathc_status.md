# Phase 2 Path C pod watchdog log

_Appended each fire. Most recent snapshot at top._

---

## 2026-04-20T07:15:00Z — fire #81 (P3-PATHC-SDSS-NATIVE-RETRAIN re-score kickoff)

**Pod:** `ktds4mkmzb7ven` (A100 80 GB PCIe, $1.19/h); GPU now busy (~60% util on 4096-batch forward every few minutes, idle between), 19 GB `/workspace` used.

**Task picked this fire:** Path C task-selection step 3 ("If any retrain completes → run post-retrain scoring"). Both SDSS + LAMOST native retrains finished fire #80, so both re-score jobs were open. Picked SDSS first because (a) 1.93M candidates vs 11.4M LAMOST → fastest path to first green criterion, (b) the `best_sdss_native.pt` at val_loss=0.0311 is the cleanest checkpoint we have, and (c) LAMOST blue-excess contamination verification needs separate logic that's better split into its own fire.

**Deliverable:** new script `pipelines/p3_anomaly_engine/sdss_native_rescore.py` (319 lines) — self-contained, resumable, batched GPU scoring pipeline. Design:

1. Load `best_sdss_native.pt` onto `cuda:0` in eval mode (same BigAE(496→128) architecture).
2. Re-apply the SAME spAll quality cut as training (`ZWARNING==0 & SN_MEDIAN>2 & SPECPRIMARY==1 & CLASS∈{STAR,GALAXY,QSO}`) → 1,928,673 candidates. Note: training sampled 300K of these; re-score does the FULL set (including the 300K trained on — in-sample is expected baseline and paper can note it).
3. Sort candidates by `(plate, mjd, fiberid)` for deterministic order across resumes.
4. For each batch of 4,096: `ThreadPoolExecutor(workers=64)` parallel-downloads lite-spec FITS from `data.sdss.org/.../redux/v5_13_2/spectra/lite/` (URL fixed fire #78), preprocesses on the fly (`np.interp` to 496-bin DESI grid, median-normalize, defensive `|x|>100` reject + `np.clip(-10,10)` learned from LAMOST fire #80), stacks successful specs → GPU → forward pass → per-spec MSE → writes `batch_NNNNNN.parquet` (8 cols: plate, mjd, fiberid, ra, dec, z, class, anomaly_score) + appends batch_id to `processed_batches.txt`.
5. After full pass, reads all batch parquets with pyarrow.dataset, concatenates + sorts by anomaly_score descending, writes two outputs: `sdss_native_all_scores.parquet` (all ~1.93M scored) and `sdss_native_anomalies_top_77905.parquet` (top-N matching Paper 3 Table 1 canonical SDSS count).

**Pre-flight:** verified pyarrow 23.0.1 + torch 2.1.0+cu118 on pod; uploaded script via scp.

**Launch verified end-to-end:**

- tmux session `sdss_native_rescore` created 2026-04-20T07:13:20Z
- Model load OK: `loaded model from /workspace/bigbounce_scan/outputs/sdss_native/best_sdss_native.pt`
- spAll parse OK: `rows: 3,958,000 → candidates: 1,928,673 → 471 batches × 4,096`
- First-record ordering sanity: `plate=3586 mjd=55181 fiberid=2` (first numeric plate with valid quality cut)
- **First batch completed**: `[score] batch 1/471 scored=4,096 success=4,096 failed=0 rate=13.7/s eta_h=39.1`
- **Parquet inspection** on pod (via python3 pyarrow read): shape (4096, 8), columns `[plate, mjd, fiberid, ra, dec, z, class, anomaly_score]`, first 3 rows all GALAXY with scores {0.059, 0.003, 0.004}, **batch statistics** `min=5.6e-4, median=0.018, max=0.925` — healthy long-tail distribution, no NaN/Inf, no blowups. This confirms: (a) the model forward is producing sensible MSE values (not near-zero collapse, not all saturated), (b) the preprocessing doesn't contain poisoned spectra (the clip-and-reject filter is doing its job), (c) pyarrow+snappy writes are correct.

**ETA @ 13.7 specs/s × 64 workers:** 1,928,673 spec / 13.7 = **~39 h** = ~1.6 days to full completion. Pod spend over that window: 39 × $1.19 = ~$46. Running total after this fire: ~$33 / $400 ceiling; at completion ~$79 / $400 — well within budget.

**What the first green criterion buys us:** once the top-77,905 anomaly parquet is written + blue-excess-style QC checks pass, we (a) have a native SDSS anomaly set to replace the cross-transfer reference in Paper 3 Table 1, (b) can start the HF upload which closes criterion #1 → green, (c) free up the pod for LAMOST re-score (fire #82) or parallel CMB retrain kickoff (fire #83) depending on disk/bandwidth headroom.

**Pod state after fire:** 1 active tmux (`sdss_native_rescore`), GPU periodically busy during batch forwards, 19 GB disk used. No other active jobs — LAMOST re-score will need its own tmux on fire #82 (independent scripts, no path collision).

**Path C exit criterion state after fire:**

| # | Criterion | Row % | Status |
|---|---|---|---|
| 1 | SDSS native retrain | 75 % | re-score IN PROGRESS 39h ETA (training DONE prior) |
| 2 | LAMOST native retrain | 50 % | re-score NOT STARTED (next fire target) |
| 3 | CMB native retrain | 0 % | not started |
| 4 | DESI 5-fold | 0 % | not started |
| 5 | NEOWISE ecliptic mask | 0 % | not started |
| 6 | Injection-recovery | 0 % | not started |
| 7 | 8-way dedup | 0 % | not started |
| 8-12 | integration/recompile/site | 0 % | not started |

**Budget delta this fire:** ~$1 (write+upload+launch+verify); running total ~$33 of $400 ceiling. Under cap.

**Files staged this fire** (1 atomic commit, `feat(phase2-pathc):` prefix):
- `pipelines/p3_anomaly_engine/sdss_native_rescore.py` (new, 319 lines)
- `project-context/SSOT/queue.md` (row bumped 50 % → 75 %)
- `project-context/SSOT/drive-to-100.md` (Loop log entry appended below)
- `pipelines/p3_anomaly_engine/pod_runs/phase2_pathc_status.md` (this snapshot)

Chronic Houston files (`HUBIFY_LABS_PRD.md`, `prompt-history.md`) untouched per protocol §7.

**Next fire (#82):** Pod watchdog first. If SDSS re-score is running healthily (expected yes, ~30-60 batches completed), launch LAMOST re-score (parallel tmux, same pod, independent paths). If SDSS re-score has stalled, diagnose before adding load. CMB native retrain kickoff (criterion #3, the hardest remaining) stays fire #83 target — it's GPU-heavy and would compete with re-scoring, so best deferred until at least one re-score is near completion.

---

## 2026-04-20T06:05:00Z — fire #80 (P3-PATHC-LAMOST-NATIVE-RETRAIN outlier-clipping FIX + triple gate PASS)

**Pod:** `ktds4mkmzb7ven` (A100 80 GB PCIe, $1.19/h)

**Three completion milestones this fire:**

| Task | Result | Artifact |
|---|---|---|
| SDSS native retrain | **gate PASS** val_loss=**0.0311** (epoch 17 early stop, 138 s) | `outputs/sdss_native/best_sdss_native.pt` (3.5 MB) |
| LAMOST native retrain (attempt 2) | **gate PASS** val_loss=**0.0329** (epoch 39, full 40) | `outputs/lamost_native/best_lamost_native.pt` (3.5 MB) |
| LAMOST cross-transfer §7.1 baseline | **COMPLETE** | 11,240,648 scored / 43,915 anom / 40 h |

**Debug trace — LAMOST attempt 1 gate FAIL → attempt 2 gate PASS:**

Attempt 1 log tail:
```
[train] epoch 11/40  train=6171143363  val=4627472384  best_val=4598493696
[train] early stop at epoch 11 (no improvement 5 epochs)
[train] DONE  best_val=4598493696.0000@epoch6  gate_FAIL(<=0.30)
```

Shard inspection on pod:
```python
X = np.load('shards/shard_00000.npy')  # (5000, 496)
X.min(), X.max()                       # -2.58e8, +3.05e8
(np.abs(X) > 1e6).sum()                # 241 pixels per shard
```

Root cause: raw LAMOST `FLUX` has cosmic-ray / dead-pixel / edge-artifact spikes at ±3×10^8 that survive median-normalize (median = body-of-spectrum ~ 1, but tails remain at 1e8). BigAE MSE on those tails explodes to 4.6 billion.

**Patch** (diff):

```python
# read_one_fitsgz — after resampled /= med:
+ if np.abs(resampled).max() > 100.0:
+     return None
+ np.clip(resampled, -10.0, 10.0, out=resampled)
```

```python
# load_all_shards — defensive filter+clip for existing shards:
+ row_max = np.abs(X).max(axis=1)
+ keep = (row_max <= 100.0) & np.isfinite(row_max)
+ X = X[keep]
+ np.clip(X, -10.0, 10.0, out=X)
```

Load-time filter output on attempt 2:

```
[load] filtered 300,000 -> 299,607 rows (rejected 393 with max|x|>100)
```

Only 393 / 300,000 rows (0.13 %) rejected — the "poison" was a handful of pathological spectra, not systemic.

**Attempt 2 training log (final epochs):**

```
[train] epoch 35/40  train=0.0364  val=0.0337  best_val=0.0337
[train] epoch 36/40  train=0.0360  val=0.0334  best_val=0.0337
[train] epoch 37/40  train=0.0361  val=0.0335  best_val=0.0334
[train] epoch 38/40  train=0.0356  val=0.0360  best_val=0.0334
[train] epoch 39/40  train=0.0354  val=0.0329  best_val=0.0334
[train] epoch 40/40  train=0.0354  val=0.0330  best_val=0.0329
[train] DONE  best_val=0.0329@epoch39  gate_PASS(<=0.30)
```

**Path C criterion state after this fire:**

| # | Criterion | Row % | Status |
|---|---|---|---|
| 1 | SDSS native retrain (val ≤ 0.30 + re-score 2.3M + HF upload) | 50 % | Training DONE. Re-score + HF upload remain. |
| 2 | LAMOST native retrain (val ≤ 0.30 + re-score 11.4M + blue-excess < 20 %) | 50 % | Training DONE. Re-score + blue-excess check + HF upload remain. |
| 3 | CMB native retrain | 0 % | Kickoff deferred to fire #81 |
| 4-12 | (unchanged) | — | — |

**Pod state:** zero active tmux. Workspace 19 GB / 482 GB free. Pod billable but idle — next fire should either kick off re-score jobs or CMB retrain.

**Budget:** ~$32 / $400 ceiling (~$4 this fire; includes ~2-3 h of idle A100 time while tmux sessions completed independently).

**Lesson captured:** Post-normalize extreme-outlier rejection belongs in the FIRST draft of any preprocessing pipeline for a new survey. Median-normalize passes 1e8-scale spikes straight through. Took one full gate-FAIL to diagnose — won't repeat this class of mistake on CMB.

**Next fire (#81):** Path C options (pick one per fire):
- Launch SDSS native re-score-all-2.3M (criterion #1 → green)
- Launch LAMOST native re-score-all-11.4M (criterion #2 → green)
- Kick off CMB native retrain (criterion #3)

Likely order: SDSS re-score (smallest, fastest to finish) → LAMOST re-score → CMB retrain kickoff. Pod idle now, so fire-#81 kickoff is cheap.

---

## 2026-04-19T08:40:00Z — fire #79 (P3-PATHC-LAMOST-NATIVE-RETRAIN kickoff)

**Pod:** `ktds4mkmzb7ven` (A100 80 GB PCIe, $1.19/h)
**Three tmux sessions now LIVE:**

| Session | Created | Status |
|---|---|---|
| `lamost_native` | 2026-04-19 08:37:38 UTC | **LIVE — P3-PATHC-LAMOST-NATIVE-RETRAIN** — fetched first night tar `20111123.tar.gz` (266 MB, 23.4 s, 11.4 MB/s), extract+decode phase in progress. Target 300 K spectra from 50 randomly-sampled nights seed=20260419. Target gate val_loss ≤ 0.30. |
| `sdss_native` | 2026-04-19 08:15:08 UTC | **LIVE — P3-PATHC-SDSS-NATIVE-RETRAIN** — 15,000/300,000 (5 %) downloaded @ 11.2 specs/s, 3 shards written, 0 failures. Healthy. |
| `lamost` (cross-transfer) | 2026-04-18 10:33:11 UTC | **RUNNING — §7.1 BASELINE PRESERVATION** — 540/1,177 nights scored, ETA 25.8 h. Untouched this fire per Houston directive. |

**Script deployed:** `/workspace/bigbounce_scan/lamost_native_retrain.py` (337 lines, committed to repo).

**Candidate selection:**
- 1,177 LAMOST DR10 LRS nights advertised at `http://www.lamost.org/dr10/v2.0/tar/lrs-fits/`
- Random-sampled 50 nights (seed=20260419 — distinct from SDSS's use of same seed for pipeline reproducibility within task; different sampling populations)
- First 5: 20111123, 20120516, 20121221, 20130504, 20130519

**Pipeline architecture:**
- Download one night tar at a time (single-threaded HTTP, polite for `lamost.org`)
- Extract in-memory + 16-thread parallel `gzip + astropy.io.fits` decode
- Resample FLUX+WAVELENGTH BINTABLE to 496-bin DESI grid via `np.interp` (matches cross-transfer `lamost_scan_v2.py` exactly)
- Median-normalize + reject flat/NaN/Inf
- Shard into 5,000-spec `.npy` chunks + per-spectrum CLASS string (FITS `CLASS` header: STAR/GALAXY/QSO)
- Delete tar after each night processed; `.processed_nights.txt` for resume
- Train `BigAE(496→128 latent)` same arch as SDSS native + DESI-trained

**Pre-deploy URL probe:** `curl -sL http://www.lamost.org/dr10/v2.0/tar/lrs-fits/20111024.tar.gz` returned HTTP 200 + real tarball. Unlike fire #78's SDSS URL surprise, this endpoint is identical to what the cross-transfer scan already uses successfully — no URL blocker expected.

**Isolation:** All artifacts under `temp/lamost_native/` + `outputs/lamost_native/`. Zero path collision with cross-transfer `lamost` tmux.

**Bandwidth budget observation:**
- SDSS native: ~2 MB/s
- LAMOST cross-transfer: ~2-3 MB/s sustained (25 nights/h × ~300 MB / 144 s/night)
- LAMOST native: ~11 MB/s burst during tar fetch, ~0 during extract phase
- All three fit comfortably within typical pod egress

**Disk projection:**
- SDSS native peak: ~600 MB shards + ~300 MB raw cache at any moment
- LAMOST native peak: ~300 MB tar + 600 MB shards
- Combined: < 2 GB peak; 482 GB free — safe

**ETA:** ~3-5 h tar download+extract + ~30 min training = **~4-5 h to first checkpoint**. Sooner than SDSS native's ~8 h because 50 tar fetches at ~25 s each = ~20 min of download, rest is CPU-bound extract/decode.

**Budget:** ~$28 / $400 (~$1 delta this fire).

**Next fire (#80):** Path C task selection order step 2 has one more "kickoff" left — `P3-PATHC-CMB-NATIVE-RETRAIN` (third and last native retrain). Fire #80 expected to kick that off unless SDSS / LAMOST download hits a new class of failure requiring intervention.

---

## 2026-04-19T08:20:00Z — fire #78 (P3-PATHC-SDSS-NATIVE-RETRAIN URL fix + re-launch)

**Pod:** `ktds4mkmzb7ven` (A100 80 GB PCIe, $1.19/h)

**Watchdog finding on fire #77's kickoff:**

```
[shard] progress 58,000/300,000 success=0 failed=58,000 rate=0.0/s
```

Every download 404-ing. Hit rate: **0 / 58,000**.

**Root cause:** `DOWNLOAD_BASE` hard-coded to `/redux/26/` (legacy BOSS/eBOSS path). DR18 legacy-survey spectra live under `RUN2D=v5_13_2` at `/redux/v5_13_2/`. spAll inspection confirmed 3,958,000/3,958,000 rows have `RUN2D=v5_13_2`.

**Empirical URL probe:**

| URL | HTTP | size |
|---|---|---|
| `/redux/v5_13_2/spectra/lite/3586/spec-3586-55181-0002.fits` | 200 | 218,880 bytes (real FITS) |
| `/redux/26/spectra/lite/3586/spec-3586-55181-0002.fits` | 404 | 0 bytes |

**Patch:** one-line change in `sdss_native_retrain.py`:

```python
- DOWNLOAD_BASE = "https://data.sdss.org/sas/dr18/spectro/sdss/redux/26/spectra/lite"
+ DOWNLOAD_BASE = "https://data.sdss.org/sas/dr18/spectro/sdss/redux/v5_13_2/spectra/lite"
```

**Re-launch sequence:**
1. `tmux kill-session -t sdss_native` (broken run)
2. Wiped empty shard + raw-cache dirs
3. `scp sdss_native_retrain.py` → pod
4. `tmux new-session -d -s sdss_native 'python3 -u sdss_native_retrain.py ...'`
5. Verified new run selects candidates + begins downloads

**Post-fix verification (log tail):**

```
[shard] progress 2,000/300,000 success=2,000 failed=0 rate=10.9/s
```

32-worker download sustained at 10.9 spectra/s, zero failures.

**Revised ETA:**
- Download: 300,000 / 10.9 = **~7.6 h** (prior fire-#77 estimate of 30–50 min was optimistic)
- Training on A100: **~30 min**
- Total to first checkpoint: **~8 h**

**Disk projection:** 300K × 218 KB = ~65 GB raw download pulled sequentially (unlinks after preprocess), shards peak ~600 MB total — well within 483 GB `/workspace` headroom.

**Budget delta:** ~$1 this fire (diagnostic SSH + relaunch). Running total ~$27 / $400 ceiling.

**Lesson captured:** Probe one URL with `curl -sI` before spinning up a 32-worker downloader on an unfamiliar SDSS `RUN2D`.

**Next fire (#79):** watchdog-only unless a new class of failure appears. Expect download phase to run through fires #79-#87 ( ~3 h × 3 fires/h cadence ≈ 9 fires × 20 min = 3 h between checkpoint… actually cron is `7,27,47` = every 20 min so 8 h ÷ 20 min = **~24 watchdog-only fires** before training starts). If training starts mid-fire, the fire after switches to val_loss-gate evaluation.

---

## 2026-04-19T07:56:36Z — fire #77 (P3-PATHC-SDSS-NATIVE-RETRAIN kickoff)

**Pod:** `ktds4mkmzb7ven` (A100 80 GB PCIe, $1.19/h)
**Tmux state after kickoff:**

| Session | Created | Status |
|---|---|---|
| `sdss_native` | 2026-04-19 07:56:36 UTC | **LIVE — P3-PATHC-SDSS-NATIVE-RETRAIN** — shard builder running with 32 parallel download workers, 300 K candidates (55.2 % GAL / 27.6 % QSO / 17.3 % STAR) to preprocess to `temp/sdss_native/shards/`. Target gate val_loss ≤ 0.30. |
| `lamost` | 2026-04-18 10:33:11 UTC | RUNNING — 520+/1177 nights, §7.1 cross-transfer baseline preserved. Untouched this fire. |
| `sdss` (old) | 2026-04-18 10:32:00 UTC | **KILLED this fire** — was stuck at "Step 2" for ~21 h. Path C native retrain replaces the cross-transfer scan entirely, so no §7 SDSS baseline is recoverable (acceptable: §7 will note "no SDSS cross-transfer output obtained"). |

**Script deployed:** `/workspace/bigbounce_scan/sdss_native_retrain.py` (467 lines, committed to repo at `pipelines/p3_anomaly_engine/sdss_native_retrain.py`).

**Bug caught + fixed mid-fire:** FITS `FITS_rec` objects don't support `.get()` dict-style fallback; patched to use `t.dtype.names` membership check + auto-reduce 4-vector-per-band SN into max-over-bands. Re-uploaded + relaunched successfully.

**Candidate selection diagnostics:**
- spAll total rows: 3,958,000
- After quality cuts (`ZWARNING==0 & SN_MEDIAN_ALL>2 & SPECPRIMARY==1 & CLASS∈{STAR,GALAXY,QSO}`): 1,928,673 candidates
- Random-sampled (seed=20260419) to target: 300,000
- Class mix: GALAXY 165,463 (55.2 %) / QSO 82,781 (27.6 %) / STAR 51,756 (17.3 %)

**ETA to first checkpoint:** ~1–1.5 h (30–50 min shard build + ~30 min training on A100).

**Budget snapshot:** ~$26 / $400 ceiling after this fire (~$1.20–1.80 incremental).

**Next fire (#78):** monitor `sdss_native` tmux + `sdss_native_retrain.log`; if training still in progress, watchdog-only fire. If training complete (val_loss gate PASS/FAIL known), either kick off LAMOST native retrain (Path C order step 2b) OR the SDSS re-score-all-2.3M step depending on whether gate passed.

---

## 2026-04-19T07:34:53Z — fire #76 (first Phase 2 Path C fire)

**Pod:** `ktds4mkmzb7ven` (A100 80GB PCIe, $1.19/hr)
**SSH:** `root@104.255.9.187:11759`
**Uptime:** 170 days, 14:40 (host — pod tmux sessions younger)
**Disk:** `/workspace` 500 GB total, 18 GB used (4 %), 483 GB free — ample for native-retrain checkpoints + LAMOST + SDSS training shards.
**GPU:** NVIDIA A100 80 GB PCIe, utilization 0 %, mem 1,755 / 81,920 MiB used.
**GPU idle caveat:** 0 % utilization because both tmux workloads are I/O-bound in their current phase (LAMOST FITS streaming from HTTP; SDSS stuck in catalog Step 2). This is NOT a native-retrain stall — no native-retrain job has been kicked off yet.

### tmux inventory (2 sessions, pre-existing from 2026-04-18)

| Session | Created | State | Role for Path C |
|---|---|---|---|
| `lamost` | 2026-04-18 10:33:11 | **RUNNING** — 520/1177 nights scored, 5,433,090 spectra, 15,957 anomalies, rate ~25 nights/h, ETA ~26.4 h to finish. Occasional "Compressed file ended before end-of-stream marker" warnings (FITS stream decode errors on individual nights — non-fatal, batch counter still advancing). | **PRESERVE as Paper 3 §7 "before / after native retrain" comparison baseline.** Cross-transfer (DESI-trained BigAE scored on LAMOST) output will be the "before" arm. Native LAMOST retrain (P3-PATHC-LAMOST-NATIVE-RETRAIN) will be the "after" arm. |
| `sdss` | 2026-04-18 10:32:00 | **STUCK** — last visible state is "Step 2: Processing 3,958,000 spectra..." with no subsequent batch lines. `tmux capture-pane` tail shows catalog loaded but no further stdout for ~21 h. Meets the drive-to-100.md Phase 2 "SDSS-NUDGE" trigger (no batch-progress line for 2+ hrs past catalog download). | **ACCEPT as no-§7-baseline-for-SDSS.** Since Path C replaces this scan entirely with P3-PATHC-SDSS-NATIVE-RETRAIN, recovering the stuck cross-transfer scan is not worth the pod hours. Next fire's SDSS native-retrain kickoff will run alongside or replace this tmux. Do NOT kill this fire — defer to the next fire's kickoff step, which will decide whether to reuse or replace the `sdss` tmux. |

### Cross-transfer scan preservation policy (per Houston Path C directive 2026-04-19)

- **LAMOST cross-transfer output:** preserve. Will be used as §7.1 "LAMOST before native retrain (98 % blue-excess contamination)" reference set.
- **SDSS cross-transfer output:** none (scan stuck, no parquet written). §7 SDSS comparison will be "no cross-transfer output was obtained; native-retrain anomaly set is the sole SDSS anomaly set" — still a valid comparison vs. the hypothetical DESI-trained cross-transfer expectation.
- **CMB cross-transfer output:** already on disk from prior runs (`pipelines/h200_results/injection-recovery/injection_recovery_summary.json` is the injection-recovery set). Will be the §7.3 "CMB before native retrain (0.33 % recovery at 99th pct)" reference.
- **NEOWISE cross-transfer output:** already on disk (436 anomalies, QC-fail ecliptic systematic). Will be the §7.4 "NEOWISE before ecliptic mask" reference.

### Budget snapshot

- Pod billed hours since launch 2026-04-18 ≈ 21 h × $1.19/h = **~$25** burn-to-date on ktds4mkmzb7ven (Phase 1 carryover + Phase 2 idle).
- Path C ceiling: $400 hard cap (Houston's 2026-04-19 directive; was $140 originally, Houston approved the higher ceiling via Path C choice).
- Budget headroom: ~$375 remaining for Path C native-retrain + k-fold + injection-recovery work.

### Fire-#76 decision

- Pod watchdog ✓ (this log).
- No new native-retrain kickoffs this fire — per Phase 2 Path C task selection order, kickoffs happen starting fire #77 (SDSS-NATIVE first, per "highest-value, smallest data volume" rule).
- LAMOST cross-transfer scan allowed to continue (§7 baseline).
- SDSS stuck tmux NOT killed this fire — defer to fire #77.
- Cron JSON updated from Phase-1 `91a7e38b` to Phase-2 Path C `9f44c29e`.

### Atomic commit this fire

Single commit: `chore(phase2-pathc): fire #76 pod watchdog — log snapshot + cron.json swap to 9f44c29e`. Files: `pipelines/p3_anomaly_engine/pod_runs/phase2_pathc_status.log` (new), `project-context/SSOT/drive-to-100.cron.json` (update), `project-context/SSOT/drive-to-100.md` (Loop log append).
