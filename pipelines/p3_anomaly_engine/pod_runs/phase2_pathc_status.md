# Phase 2 Path C pod watchdog log

_Appended each fire. Most recent snapshot at top._

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
