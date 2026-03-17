# Next-Phase Execution Memo

**Date:** 2026-03-12
**Manuscript version:** v1.5.0
**PDF:** Compiled successfully (34 pages, 0 undefined references)

---

## 1. Is planck_only still running healthily?

**YES.** All 6 chains are alive (PIDs 8165-8170), actively writing samples at ~128 samples/chain/hour (~765 total/hour). Cobaya logs are error-free. Checkpoints are current.

However, **the local backup is ~22 hours stale**. An rsync pull should be run to bring the local copy up to date. The on-pod hourly backup (cron tarball + SHA256) is functioning but lives on the same /workspace volume — not true offsite protection.

**Action needed:** Run a periodic rsync (e.g., every 6-12 hours) to maintain a local backup.

---

## 2. What is the best current ETA to freeze?

**~2026-03-19** (approximately 6-7 days from chain start on 2026-03-12 19:58 UTC).

Current state: 2,360 samples, worst R̂−1 = 0.71, min ESS = 45. Need R̂−1 < 0.01 and ESS > 2,000. At current throughput (~765 samples/hour), reaching ~120,000+ samples should take ~155-165 hours total.

This is consistent with the planck_bao_sn experience (~133K samples to convergence in a similar timeframe).

---

## 3. What exact prompt should we run once planck_only is ready?

When the monitoring script shows all 9 freeze gates passing, execute:

```
Execute the planck_only freeze workflow per:
research/global_monitor/planck_only_freeze_ready_checklist.md

Steps:
1. Verify all 9 freeze gates pass
2. Create frozen artifact pack on pod
3. SHA256 checksums + MANIFEST
4. Tarball
5. Rsync to local
6. Verify checksums locally
7. Stop chains
8. Resume planck_bao (6 chains)
9. Update master_cosmology_results_table.md
10. Generate 3-dataset comparison figures
11. Fill [PENDING: planck_only] markers in manuscript
12. Recompile PDF on pod
13. Update REVISION_TRACKER.md
```

---

## 4. After planck_only freezes, should we update manuscript, resume planck_bao, or both?

**Both in parallel:**

1. **Resume planck_bao immediately** after planck_only freeze is verified. planck_bao has 469 samples already and will need ~6-7 days to converge.

2. **Update manuscript with planck_only results** while planck_bao runs:
   - Fill the 3 [PENDING: planck_only] markers
   - Generate 3-dataset comparison figures
   - Update results narrative
   - Bump version to v1.6.0
   - Recompile PDF

3. **Do NOT wait for planck_bao** to start the referee-style review. The 3-dataset manuscript (full_tension + planck_bao_sn + planck_only) is substantive enough for an internal review pass.

---

## 5. What is the minimum remaining work before a serious referee-style review?

### Blocking (must complete before review):
1. **planck_only freeze + manuscript integration** (~7 days)
2. **PDF compilation** — DONE (v1.5.0 compiled on pod, 34 pages)
3. **All [PENDING: planck_only] markers filled** — after freeze

### Non-blocking (can proceed in parallel):
4. **planck_bao freeze + integration** — adds a 4th dataset but not required for review
5. **Corner plots / GetDist posteriors** — can generate on demand
6. **Final cross-dataset comparison** — needs all 4 datasets

### Recommended review timeline:
- **~March 19-20:** planck_only freezes → update manuscript to v1.6.0
- **~March 20-21:** Internal referee-style review of 3-dataset manuscript
- **~March 26-27:** planck_bao freezes → update manuscript to v1.7.0
- **~March 28-30:** Final review + arXiv submission prep

---

## Summary of Deliverable Locations

| Deliverable | Path |
|-------------|------|
| Compiled PDF | `arxiv/main.pdf` |
| Compilation script | `arxiv/compile_on_pod.sh` |
| Overleaf ZIP script | `arxiv/make_overleaf_zip.sh` |
| Compile readiness report | `research/final_paper_prep/latex_compile_readiness.md` |
| Compile log | `research/final_paper_prep/latex_compile_log.txt` |
| Pending marker audit | `research/final_paper_prep/pending_marker_audit.md` |
| Planck_only status | `research/global_monitor/planck_only_status_latest.{txt,json}` |
| Backup audit | `research/global_monitor/planck_only_backup_audit.txt` |
| Freeze checklist | `research/global_monitor/planck_only_freeze_ready_checklist.md` |
| Manuscript update summary | `research/final_paper_prep/manuscript_update_summary_v1.md` |
| Revision tracker | `project-context/peer-reviews/REVISION_TRACKER.md` |

---

## Immediate Action Items

1. **Now:** Pull a fresh rsync of planck_only chains to local backup
2. **Every 12h:** Re-run monitoring script to track convergence progress
3. **~March 19:** Check freeze gates — if passing, execute freeze workflow
4. **After freeze:** Resume planck_bao + update manuscript in parallel
