# BigBounce SSOT — cross-paper close-the-gap queue

**Prioritized, tagged task queue to drive every paper to true 100 %.** One task per row. Each task is scoped to close a specific percentage-point gap in a specific paper (or program-wide).

Last authoritative update: 2026-04-17

## Legend

- **Priority** — `P0` now · `P1` this week · `P2` before submission · `P3` after submission / polish
- **Owner** — `agent` (this session or future agent) · `pod` (H200/H100 compute required) · `Houston` (decision) · `site` (frontend edit only)
- **Blocker of** — which paper this gates
- **% closed** — how much of the paper's remaining gap this task closes on completion
- **Status** — `[ ]` open · `[~]` in progress · `[x]` done · `[!]` blocked (with reason)

---

## P0 — do now

| ID | Title | Owner | Paper | % closed | Status | Notes |
|---|---|---|---|---:|---|---|
| `P1-SSOT-SWEEP` | Forensic sweep on Paper 1 (Spin-Torsion) → produce verified `paper-1/status.md` | agent | P1 | sets baseline | [ ] | Same pattern as P3/P4 sweeps (Explore subagent + verification greps) |
| `P2-SSOT-SWEEP` | Forensic sweep on Paper 2 (f_NL Forecast) → produce verified `paper-2/status.md` | agent | P2 | sets baseline | [ ] | Same pattern as P3/P4 |
| `P3-A` | TIC 374313355 periodicity analysis (TESS archival light curve + Lomb-Scargle) | pod | P3 | 0.05 % | [ ] | Uses existing ZTF-anomaly periodicity code |
| `P3-B` | Deep cross-match of top-100 DESI + 203 eROSITA + BAL-QSO against NED / VizieR / Gaia-XP | agent | P3 | 0.1 % | [ ] | Reclassify "uncatalogued" → "archival-identified" vs "truly uncatalogued"; probably shrinks novel count 20–40 % |
| `P4-DIPOLE-JSON-REBUILD` | Re-emit non-truncated `outputs/dipole/summary.json` (current one crashed at L366 after `consistent_with_null:`) | pod | P4 | 0.5 % | [ ] | Either rerun on-pod or reconstruct from existing log |

## P1 — this week

| ID | Title | Owner | Paper | % closed | Status | Notes |
|---|---|---|---|---:|---|---|
| `P3-C` | Fisher-forecast σ(γ) for NANOGrav 20yr / EPTA DR3 / SKA-P1 given current posterior | agent | P3 | 0.05 % | [ ] | Addresses §6 "continued monitoring" deferral with a concrete when-decisive figure |
| `P3-PDF-CANON` | Delete or rebuild `arxiv/paper3_anomaly_catalog.tex` + `.pdf` from the pipelines copy | agent | P3 | 0.3 % | [ ] | Canonical .tex is `pipelines/p3_anomaly_engine/paper3_draft.tex` |
| `P3-PDF-RECOMPILE` | Recompile Paper 3 PDF on-pod with today's date + SSOT cross-check | pod | P3 | 0.3 % | [ ] | Requires texlive on H200; ~15 min |
| `P4-PDF-CANON` | Pick `pipelines/p2_chirality/chirality_catalog_paper.tex` as canonical; delete or rebuild arxiv/ copy | agent | P4 | 0.5 % | [ ] | Two .tex files have diverged |
| `P4-PDF-RECOMPILE` | Recompile Paper 4 PDF on-pod with today's date + SSOT cross-check | pod | P4 | 0.5 % | [ ] | |
| `P4-PAPER2-XREF` | Fix two stale wordings in `pipelines/p2_chirality/paper2_chirality_section.tex` | agent | P4+P2 | 0.3 % | [ ] | Companion section still cites old numbers |
| `P3-SITE-SYNC` | Update `index.html`, `paper.html`, `activity.html`, `figures.html`, `data-explorer.html` to reflect Paper 3 SSOT numbers | site | P3 | 0.1 % | [ ] | Part of aggregate `P-SITE-FULL-SYNC` |
| `P4-SITE-SYNC` | Same for Paper 4 SSOT numbers | site | P4 | 0.3 % | [ ] | Part of aggregate `P-SITE-FULL-SYNC` |
| `P3-HF-UPLOAD` | Publish aggregated 319,443-anomaly catalog to HuggingFace `bamfai/bigbounce-anomaly-catalog` with CC-BY-4.0 | agent | P3 | 0.05 % | [ ] | Paper §9 data-availability needs live link before arXiv |
| `P4-HF-DOI` | Pin HF `bamfai/galaxy-chirality-catalog` version + add DOI / versioned URL to Paper 4 data-availability statement | agent | P4 | 0.2 % | [ ] | |
| `P3-XREF` | Audit Paper 3 cross-references against Paper 2 f_NL forecast + Paper 4 dipole infrastructure | agent | P3 | 0.05 % | [ ] | |
| `P4-LSST-LINE-REVIEW` | Houston reviews paper4 L913 "Future surveys (Rubin LSST)" line on final PDF read — confirm TRULY BLOCKED | Houston | P4 | 0.2 % | [ ] | If it's not blocked per Principle 10 it becomes a new task |
| `P-MEMORY-SYNC` | Add MEMORY.md entry for SSOT directory + update existing entries that reference old paper-N-status.md paths | agent | ALL | 0 % | [ ] | One-time housekeeping after restructure lands |

## P2 — before submission

| ID | Title | Owner | Paper | % closed | Status | Notes |
|---|---|---|---|---:|---|---|
| `P3-D` | Ensemble anomaly detection (VAE + iForest + one-class SVM) on existing latent vectors → inter-model agreement column | pod | P3 | 0.05 % | [ ] | §7.3 #1. 2–3 wk on H200 |
| `P3-E` | Synthetic-anomaly injection + recovery for 7 non-DESI surveys | pod | P3 | 0.1 % | [ ] | §7.3 #2. ~2 wk each, parallelisable |
| `P3-F` | DESI B-dominant population (44,436 / 22.7 %) calibration-systematics audit | pod | P3 | 0.05 % | [ ] | §7.3 #3. ~2 wk |
| `P3-G` | Empirical Landy-Szalay w(θ) bias calibration for anomaly subsample (replaces α = 0.15 assumption) | pod | P3+P2 | 0.1 % | [ ] | §7.3 #4. Re-uses Paper 4 dipole infrastructure |
| `P3-H` | NANOGrav reforecast with inflated uncertainty from DR3 free-spectrum covariance | agent | P3 | 0.05 % | [ ] | §7.3 #5. ~1 wk |
| `P-SITE-FULL-SYNC` | Site-agent pass: run all P3-SITE-SYNC, P4-SITE-SYNC, and post-sweep P1/P2 variants together | site | ALL | ~1 % total | [ ] | See `index.md` aggregate surface-sync checklist |
| `P-ARXIV-P4` | Assemble Paper 4 tarball, fill arXiv form, submit, return ID | Houston | P4 | closes | [ ] | Do Paper 4 first (most self-contained) |
| `P-ARXIV-P3` | Same for Paper 3 | Houston | P3 | closes | [ ] | Follow ~24 h after Paper 4 |

## P3 — after submission / polish

| ID | Title | Owner | Paper | % closed | Status | Notes |
|---|---|---|---|---:|---|---|
| `P-MEMORY-AGENT-HOOKS` | Ensure `AGENTS.md` + `CLAUDE.md` routing tells every agent to check SSOT first on any paper-related prompt | agent | ALL | 0 % | [ ] | Partially done in this restructure commit; verify after 1 session cycle |
| `P-LEGACY-STATUS-CLEAN` | Rewrite `CURRENT_STATUS.md` as a mirror of `index.md` (single source of derived status) | agent | ALL | 0 % | [ ] | |
| `P-FREEZE-WIKI` | Confirm all `wiki/entities/paper-*.md` and `wiki/entities/pipeline-*.md` are pointer-only, no status content | agent | ALL | 0 % | [ ] | |
| `P-SSOT-CRON` | Add a weekly cron/agent check: "any SSOT file > 7 days stale → flag" | agent | ALL | 0 % | [ ] | Prevents drift |

---

## Completed (done in this session — 2026-04-17)

- `P4-DIPOLE-ARTIFACTS-LOCAL` — Copied dipole summary + figures + log from `pod_final_backup_20260414/` to `pipelines/p2_chirality/outputs/dipole/` · committed `6651dd5`
- `P4-REDSHIFT-BINS-INDEX` — Indexed the already-done `fcw_vs_redshift.csv` (20 bins) — stretch goal turned out done · part of `6651dd5`
- `P3-SSOT-SWEEP` — Forensic sweep on Paper 3 · produced `SSOT/paper-3/status.md` · commit `0c39a15`
- `P4-SSOT-SWEEP` — Forensic sweep on Paper 4 · produced `SSOT/paper-4/status.md` (pre-restructure: `paper4_chirality_status.md`) · earlier commit
- `P-SSOT-RESTRUCTURE` — Moved to `SSOT/` tree; added `README`, `index`, `queue`; pointer stubs kept at old paths — **this commit**
- `P-PRINCIPLE-10-CORRECTION-P3` — Corrected Paper 3 "zero future-work hits" claim after Houston pushback; 4 future-work-adjacent hits now classified DO-NOW / SIMULATE-AUGMENT-NOW — **this commit**

---

## How to work this queue

1. Pick the lowest-ID `P0` task whose dependencies are met.
2. Mark it `[~] in progress` when you start.
3. Execute; when done, flip to `[x]` and move the row to the Completed section with the commit hash.
4. If blocked, flip to `[!]` with a one-line reason.
5. When adding new tasks: insert them at the correct priority; ID them `P{paper}-{slug}` or `P-{program-slug}` for cross-paper.
6. Never delete a completed task row from the history. That's the record.
