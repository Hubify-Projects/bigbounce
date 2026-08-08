# P4 DR8 per-galaxy morphology pull — running job status

**Authorized real compute (Houston 2026-07-02):** pull DR8 morphology (b/a,
fracdev, shape_r) for the 3.2M P4 spirals, extend the ℓ=1 forward model, and
measure whether imaging+morphology closes P4's ~46% un-modelled residual (the
imaging-only model reaches 54%).

## Data route (important — NOT the 780 GB sweep download)

The DESI Legacy **DR8 sweep HTTP server (portal.nersc.gov)** throttles this pod
to ~90 KB/s — a 780 GB pull would take days. Instead the identical per-galaxy
morphology is pulled from the **NOIRLab Astro Data Lab** table `ls_dr8.tractor`
(the catalog the sweeps are built from) via TAP, keyed by
`dr8_id = BRICKID_OBJID`.

- Anonymous DL **async / table-upload** = not permitted (needs a DL account).
- Anonymous DL **sync** bulk `WHERE brickid IN (...)` = 504 gateway timeout
  (returns millions of whole-brick rows through a 60 s gateway).
- **Working pattern** (exact-spiral fetch, tiny responses):
  ```sql
  SELECT brickid,objid,type,fracdev,shapedev_r,shapedev_e1,shapedev_e2,
         shapeexp_r,shapeexp_e1,shapeexp_e2
  FROM ls_dr8.tractor
  WHERE brickid IN (<=40 bricks)
    AND (brickid*30841.0 + objid) IN (<exact float keys>)
  ```
  40-brick batches → ~420 spirals/query in ~4 s, 0 waste. Validated:
  40-brick query returned 493/493 requested spirals; steady state ~54
  batches/min, **0 failures**.

## Running job (RunPod)

- **Pod:** `580dgszgib3ti4` (`bigbounce-p4-dr8morph`, RTX A4000, **112 vCPU,
  503 GB RAM, 60 GB disk**). SSH: `root@<pod-ip> -p <port>`
  (key `~/.ssh/id_ed25519`); RunPod proxy `580dgszgib3ti4-644119b0@ssh.runpod.io`.
- **tmux session:** `dlfinal` running `/workspace/dr8morph/pull_dr8_final.py`
  (`NWORK=5 BRICK_BATCH=40`). Resumable, self-terminating, heavy backoff.
- **ETA:** ~2.5 h for all 317,380 bricks / 7,935 batches.
- On ≥50 % match it **auto-runs** `systematic_l1_forward_model_dr8morph.py`.

## Files (pod)

| Path | What |
|------|------|
| `/workspace/dr8morph/pull_dr8_final.py` | the puller (exact-key sync pattern) |
| `/workspace/dr8morph/spiral_keys.parquet` | 3,201,160 spiral (BRICKID,OBJID,ra,dec) keys (regenerated from HF) |
| `/workspace/dr8morph/out/spiral_morphology.parquet` | **final morphology output** (written at DONE_PULL) |
| `/workspace/dr8morph/out/_dl_partial.parquet` | rolling checkpoint |
| `/workspace/dr8morph/out/_dl_done_batches.txt` | resume ledger |
| `/workspace/dr8morph/dlfinal.log` | pull log (grep `kept_cum`, `DONE_PULL`) |
| `/workspace/dr8morph/systematic_l1_forward_model_dr8morph.py` | extended forward model |
| `/workspace/dr8morph/out/systematic_l1_forward_model_dr8morph.json` | **the verdict** (extended fraction vs 54%) |

Repo copies of both scripts: `pipelines/p2_chirality/scripts/pull_dr8_datalab.py`
(sync helper) and `.../systematic_l1_forward_model_dr8morph.py`.

## Harvest (when DONE_PULL appears)

```bash
POD='ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -i ~/.ssh/id_ed25519 -p <port> root@<pod-ip>'
# 1. confirm complete
$POD 'grep DONE_PULL /workspace/dr8morph/dlfinal.log; cat /workspace/dr8morph/out/systematic_l1_forward_model_dr8morph.json | python3 -m json.tool | grep -A6 improvement'
# 2. pull artifacts back
scp -i ~/.ssh/id_ed25519 -P <port> root@<pod-ip>:/workspace/dr8morph/out/spiral_morphology.parquet pipelines/p2_chirality/outputs/
scp -i ~/.ssh/id_ed25519 -P <port> root@<pod-ip>:/workspace/dr8morph/out/systematic_l1_forward_model_dr8morph.json pipelines/p2_chirality/outputs/
# 3. ALWAYS-backup morphology to HF + B2 (Lesson E) so it never re-pulls
# 4. STOP the pod (NOT terminate):  podStop mutation for 580dgszgib3ti4
```

## Verdict decision (do NOT fabricate the fraction)

- **extended fraction ≥ ~70–80 %** → imaging+morphology closes the residual;
  fold updated number into P4, bump `v1.0.209 → v1.0.210` + directive-G PDF
  hygiene + FLAG bundle rebuild + Convex + site + SSOT + reviewTimeline.
- **partial** → report honestly, keep P4 at its 54 % imaging-only partial
  framing, the remainder stays a genuine open item. The extended fraction is
  whatever it measures.
