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
4. Otherwise: pick the highest-priority open task (agent + site tasks first).
5. Do the task. Commit with `feat/chore/docs:` prefix + task ID. Push to `origin/main`.
6. Update `SSOT/queue.md` (move row to Completed section with commit hash). Update `SSOT/index.md` headline % if a paper ticked up. Update this file's "Last loop ran" line.
7. If a task uncovered a new task, add it to `SSOT/queue.md` at correct priority.
8. **If nothing agent-doable is left and only pod tasks remain: do NOT stop — deploy a pod.** See "Pod-deploy escalation" below. Houston's instruction (2026-04-17 fire #5): "if pod needed dont stop just deploy a pod."

## Pod-deploy escalation

When only pod-owned tasks remain in `queue.md`:

1. **Check the pod-deploy prerequisite chain:**
   - `runpodctl` installed? (`which runpodctl`)
   - API key present? (`$RUNPOD_API_KEY` env var, or `~/.runpod/config.toml`, or `gh secret get RUNPOD_API_KEY` if stored in GH)
   - SSH key: `~/.ssh/id_ed25519` (verified present 2026-04-17)
2. **If all present** → launch pod with the recipe at `arxiv/compile_on_pod.sh` (which installs `texlive-publishers` + `texlive-latex-extra` and runs `pdflatex -interaction=nonstopmode` twice on each `.tex`). Batch all three outstanding V2 recompiles (P1, P3, P4) + `P3-FISHER-FULL` + `P3-A` TESS periodicity into a single pod session, ≤60 min, ≤ $4 on an H200.
3. **If any prerequisite missing** → emit a `## POD DEPLOY BLOCKER` section in this file with:
   - The exact command Houston needs to paste (install `runpodctl` + export API key), OR
   - A note that Houston should run `/deploy-pod` if a higher-level skill exists.
   Keep the cron running — next fire will retry after Houston unblocks.
4. **While pod is running** — subsequent fires pull `~/.claude/pod-drive-to-100.log` from the pod via `rsync` to check progress; fold results back into SSOT when complete.

No fire may `return early` because "only pod work remains." Either deploy, or file a precise blocker that Houston can act on in one paste.

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

## POD DEPLOY BLOCKER — Houston, one paste unblocks everything

**Status (fire #5, 2026-04-17):** All four remaining V2 recompiles + P1 tarball rebuild + P3 Fisher-full are blocked on **zero** available compile surface. Loop confirmed:

| Surface | State | Blocker |
|---|---|---|
| Local `pdflatex` | not installed | `brew install --cask basictex` needs sudo password interactively |
| Local Docker TeX Live | Docker Desktop not running | Houston must click Docker.app once |
| RunPod CLI (`runpodctl`) | not installed, no brew formula | Official installer script `cli.runpod.net \| bash` requires sudo |
| Existing H200 pod `o76k3jfzbfh25e` at `205.196.19.52:11452` | **connection refused** — pod terminated | Need to launch a fresh pod |

**Paper 1 bbl is confirmed stale:** `arxiv/main.tex` cites 55 keys; `arxiv/main.bbl` only contains 58 bibitems but 17 are missing and 20 are unused. All 17 missing keys exist in `arxiv/references.bib` — `bibtex` just needs to re-run. This means **any tarball built right now would arXiv-reject**. Compile MUST run before tarball ships.

**One-paste unblock options (pick one):**

**Option A — launch Docker Desktop (fastest, no password):**
```bash
open -a Docker
# wait ~15s for daemon, then this agent can compile via:
# docker run --rm -v "$PWD/arxiv":/w -w /w texlive/texlive:latest \
#   bash -c "pdflatex -interaction=nonstopmode main && bibtex main && pdflatex -interaction=nonstopmode main && pdflatex -interaction=nonstopmode main"
```

**Option B — install runpodctl + paste API key:**
```bash
brew install curl jq
wget -qO- cli.runpod.net | sudo bash     # prompts for your sudo password
export RUNPOD_API_KEY="rpa_xxx_your_key"  # paste from https://www.runpod.io/console/user/settings
echo $RUNPOD_API_KEY >> ~/.zshrc
```

**Option C — install BasicTeX locally:**
```bash
brew install --cask basictex   # prompts for sudo password
eval "$(/usr/libexec/path_helper)"
sudo tlmgr update --self && sudo tlmgr install revtex
```

Once any one is done, the next cron fire will detect it (via `which` + `docker info`) and batch all four V2 recompiles + P3-FISHER-FULL in a single run.

---

## Loop log

_Appended each fire. Most recent first._

- **2026-04-17 — fire #7:** closed `P-LEGACY-STATUS-CLEAN`. Rewrote `project-context/CURRENT_STATUS.md` as pointer-only to SSOT (was 4-day-stale with Paper 2 "85 % science done", pod `sleepy_blush_crane` as active, Pipeline 1 steps table, H200 experiment roll-up, backup inventory, next-steps list — all of which now live in `SSOT/index.md` + per-paper `status.md` + `SSOT/queue.md` + per-pipeline docs + `MEMORY.md`). Added re-population-prohibited note so future agents don't re-mirror status content here. Compile surfaces re-checked this fire: still all blocked (pdflatex / runpodctl missing, Docker daemon off) — `POD DEPLOY BLOCKER` from fire #5 still in force. No paper % ticked up — legacy-status cleanup is 0 % paper credit by design.
- **2026-04-17 — fire #6:** closed `P-FREEZE-WIKI`. Rewrote 3 wiki entity files as pointer-only to SSOT: `paper-3-anomaly-catalog.md` (removed 9-row core-numbers table + connections dump), `paper-4-chirality.md` (removed 7-row core-numbers table), `pipeline-1-tracer-purification.md` (removed 6-row pipeline-steps table + 5-row constraint-status table + measured-improvements list — content was 11 days stale: said "Step 1 DONE, Steps 2-6 NOT STARTED" while CLAUDE.md / SSOT reflect Steps 1-5 complete). All 4 paper-*.md + 3 pipeline-*.md now route to SSOT. Compile surfaces re-checked this fire: still all blocked (BasicTeX / Docker / runpodctl / old pod) — `POD DEPLOY BLOCKER` section from fire #5 remains in force. Next fire will detect unblock and resume pod-dependent work. No paper % ticked up — wiki freeze is bookkeeping (0 % paper credit by design).
- **2026-04-17 — fire #5:** confirmed all compile surfaces blocked (local BasicTeX sudo, Docker daemon off, runpodctl missing, existing pod terminated). Ran standalone bbl integrity check via `/tmp/bib_check.py` and discovered Paper 1 bbl is 17 bibitems short vs live main.tex (all 17 keys DO exist in references.bib — bbl just needs bibtex re-run). Filed consolidated `POD DEPLOY BLOCKER` section above with three one-paste unblock options for Houston. Filed new queue task `P1-BBL-REGEN` (pod, blocks P1-TARBALL). No paper % ticked up; unblock cascades once Houston pastes one command.
- **2026-04-17 — fire #4:** closed P-MEMORY-SYNC. Refreshed `project_ssot_structure.md` with current SSOT layout (all 4 paper status files exist; added drive-to-100.md + drive-to-100.cron.json entries). Rewrote `project_papers_status.md` from stale 11-day-old mirror (Paper 2 v1.3.0, Paper 4 ~85 %) to pointer-only memory that refuses to quote %. Added new `project_drive_to_100.md` memory + index entry in `MEMORY.md`. No paper % ticked up — memory housekeeping has 0 % paper credit by design.
- **2026-04-17 — fire #3:** closed P3-C (Fisher-forecast σ(γ) for future PTAs). Produced scaling-only forecast note (`pipelines/p3_anomaly_engine/fisher_forecast_gamma_future_ptas.md`) with σ(γ)≈0.22 NG20yr, 0.16 EPTA DR3, 0.15 SKA-P1 against 3σ threshold σ(γ)≤0.44. Replaced Paper 3 §6 "continued monitoring" hand-wave with concrete paragraph. Added Siemens2013 + Rosado2015 bibitems. Filed `P3-FISHER-FULL` (pod) for the proper Fisher calculation. Triggers `P3-PDF-RECOMPILE-V2`. No paper % ticked up this fire — credit unlocks after recompile.
- **2026-04-17 — fire #2:** closed P3-PDF-CANON (verified pointer stub + mirror PDF) and P3-XREF (added 3 Golden companion bibitems — framework, fnl, chirality — plus 4 `\cite{}` calls at the f_NL=-35/8 theory line, the SPHEREx Fisher-forecast line, and the bias-calibration limitation). Filed `P3-PDF-RECOMPILE-V2` for the next pod session. No paper % ticked up — xref credit unlocks after recompile.
- **2026-04-17 — fire #1:** queue reconciliation — closed 13 rows in `queue.md` that were already marked ✓ in `index.md` (P1-FIGURES-VERIFY, P1-CORNER-PLOTS, P1-PDF-RECOMPILE, P1-WIKI-SYNC, P2-COMPILE-POD, P2-XREF-AUDIT, P2-WIKI-POINTER, P2-CURRENT-STATUS-SYNC, P2-PDF-PUBLISH, P2-TARBALL, P3-PDF-RECOMPILE, P4-PDF-RECOMPILE, P4-HF-DOI). Filed two V2 recompile follow-ups (P1/P4) for the §IV corner figure + LSST projection line inserts. P1-TARBALL marked `[~]` partial. No papers ticked up numerically this fire; reconciliation is bookkeeping, not % change.
- **2026-04-17 — T0 (initial):** plan doc created, cron scheduled. Awaiting first fire.
