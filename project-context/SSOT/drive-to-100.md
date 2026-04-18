# Drive-to-100 — Automated Completion Plan

**Created:** 2026-04-17
**Owner:** agent (autonomous loop) + Houston (final review)
**Cadence:** every 20 min via `CronCreate` until exit criteria met
**Exit condition:** all 4 papers at 100 % in `SSOT/index.md` · public site deployed on `main` · Houston-reviewable at https://bigbounce.hubify.app

---

## Goal

Drive every open item in `SSOT/queue.md` to done, sync the public site, deploy to Vercel, and confirm all four papers read as 100 % in `SSOT/index.md`. Self-terminate when the exit criteria below are all green.

## Exit criteria (all must be true to stop the cron)

1. `SSOT/index.md` headline table shows **100 %** for Paper 1, Paper 2, Paper 3, Paper 4.
2. `SSOT/queue.md` has **zero P0 open rows** and **zero P1 open rows**.
3. `arxiv/main.pdf` recompiled, ≥2 MB, 0 undefined refs — Paper 1.
4. `public/papers/paper2_fnl_forecast.pdf` exists, linked from `paper.html` — Paper 2.
5. `public/papers/paper3_anomaly_catalog.pdf` exists — Paper 3.
6. `public/papers/chirality_catalog_paper.pdf` recompiled with LSST projection line — Paper 4.
7. Site badges on `index.html` + `paper.html` read `100%` for all four papers.
8. `git status` clean on `main`; last commit pushed to `origin/main`; Vercel deploy succeeded.
9. `project-context/prompt-history.md` captures this loop's final status.

## Per-paper remaining work

### Paper 1 (99.9 → 100 %)
- `P1-LINE-299-WORDSMITH` — replace `(amplitude and shape TBD)` at L299 of `arxiv/main.tex`. [agent, 15 min]
- `P1-FIGURES-VERIFY` — verify all `\includegraphics{}` resolve. [agent]
- `P1-CORNER-PLOTS` — `.tex` already has §IV corner figure; pod recompile needed. [pod]
- `P1-PDF-RECOMPILE` — on-pod recompile; drop into `arxiv/main.pdf`. [pod]
- `P1-WIKI-SYNC` — `wiki/entities/paper-1-*.md` → pointer-only. [agent]
- `P1-TARBALL` — arXiv tarball + clean revtex smoke-test. [agent]

### Paper 2 (99 → 100 %)
- `P2-COMPILE-POD` — recompile after revtex4-2 conversion; ≥2 MB, 0 undefined refs, 6 figs. [pod]
- `P2-XREF-AUDIT` — confirm `\cite{Golden:2026framework}` + Paper 3 implicit xref. [agent]
- `P2-WIKI-POINTER` — rewrite stale `paper-2-fnl-forecast.md` → pointer. [agent]
- `P2-CURRENT-STATUS-SYNC` — update `CURRENT_STATUS.md` Paper 2 row. [agent]
- `P2-PDF-PUBLISH` — copy to `public/papers/paper2_fnl_forecast.pdf`, link from `paper.html`. [agent, after pod]
- `P2-TARBALL` — arXiv tarball (tex + bbl + 6 figs + bphi.pdf). [agent]

### Paper 3 (99.5 → 100 %)
- `P3-A` — TIC 374313355 Lomb-Scargle periodicity (uses existing ZTF code). [pod]
- `P3-B` — deep cross-match top-100 DESI + 203 eROSITA + BAL-QSO vs NED/VizieR/Gaia-XP. [agent]
- `P3-C` — Fisher-forecast σ(γ) for NANOGrav 20yr / EPTA DR3 / SKA-P1. [agent]
- `P3-PDF-CANON` — delete or rebuild `arxiv/paper3_anomaly_catalog.tex`. [agent]
- `P3-PDF-RECOMPILE` — on-pod recompile from `pipelines/p3_anomaly_engine/paper3_draft.tex`. [pod]
- `P3-HF-UPLOAD` — publish 319,443 anomaly catalog to HF `bamfai/bigbounce-anomaly-catalog`. [agent]
- `P3-XREF` — audit vs Paper 2 + Paper 4. [agent]

### Paper 4 (99.5 → 100 %)
- `P4-PDF-RECOMPILE` — on-pod with LSST projection line. [pod]
- `P4-HF-DOI` — pin HF `bamfai/galaxy-chirality-catalog` version + DOI in data-availability. [agent]
- `P4-LSST-LINE-REVIEW` — Houston review of L913 on final PDF. [Houston]

### Cross-paper + site + housekeeping
- `P-MEMORY-SYNC` — add MEMORY.md SSOT entry. [agent]
- `P-LEGACY-STATUS-CLEAN` — `CURRENT_STATUS.md` becomes mirror of `index.md`. [agent]
- `P-FREEZE-WIKI` — all `wiki/entities/paper-*.md` pointer-only. [agent]
- Final Vercel deploy confirmation.

## Loop protocol (every 20 min fire)

Each cron fire runs this loop:

1. `cd /Users/houstongolden/Desktop/CODE_2025/bigbounce`
2. Read `SSOT/drive-to-100.md` (this file) + `SSOT/queue.md` + `SSOT/index.md`.
3. **Check exit criteria.** If all green: (a) commit a CLOSED marker in this file, (b) call `CronDelete` on the loop's job ID (stored in `SSOT/drive-to-100.cron.json` after first fire), (c) append a `## Houston-reviewable` note to `SSOT/index.md` with the deploy URL, (d) halt.
4. Otherwise: pick the highest-priority open task this fire can do without a pod (agent + site tasks first; mark pod tasks as `[!] waiting-on-pod` when no session is active).
5. Do the task. Commit with `feat/chore/docs:` prefix + task ID. Push to `origin/main`.
6. Update `SSOT/queue.md` (move row to Completed section with commit hash). Update `SSOT/index.md` headline % if a paper ticked up. Update this file's "Last loop ran" line.
7. If a task uncovered a new task, add it to `SSOT/queue.md` at correct priority.
8. If nothing agent-doable is left and only pod tasks remain: mark this file `## BLOCKED-ON-POD` with exact pod commands needed, keep cron running at 20-min (so once pod finishes out-of-band the next fire will pick up the site-sync follow-ups).

## Task selection order each fire

Priority (first match wins):
1. Any `P0` open row with `owner = agent` or `site`.
2. Any `P1` open row with `owner = agent` or `site`.
3. Any site-sync follow-up made possible by a pod task that finished since last fire (detect via file mtimes in `public/papers/` and `arxiv/`).
4. Housekeeping (`P-MEMORY-SYNC`, `P-FREEZE-WIKI`, `P-LEGACY-STATUS-CLEAN`).
5. Pod-owned tasks → emit a `POD NEEDED` note into this file, do nothing else this fire.

## Safety

- Never force-push. Never touch `main` history.
- Every loop iteration = atomic commit. No multi-task commits.
- If `git status` is dirty from a user edit, skip this fire, leave a note in this file, and retry next fire.
- If a test or compile would take > 20 min, kick off in background and continue.

---

## Loop log

_Appended each fire. Most recent first._

- **2026-04-17 — T0 (initial):** plan doc created, cron scheduled. Awaiting first fire.
