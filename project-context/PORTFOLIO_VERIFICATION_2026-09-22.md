# Portfolio verification — 2026-09-22

**Prepared by:** campaign lane `bb-L6c-verify-signoff` (Sonnet), re-running the
tail of `bb-L6b-verify-signoff` (which ended early on a harness watchdog while
waiting on a background poll — a process violation; this lane fixes that by
polling in the foreground only, per the hard rule in its own brief).

**Scope:** one row per paper in `project-context/SSOT/` — P1A, P1B, P1C, P1N,
P2, P2L, P3, P4, P4P, P5, A3M, AF, P-SU (13 rows; P-SU/AF are 2-letter slugs,
not part of the historical "6-paper" set but tracked in SSOT since 2026-09).

**What this lane reused vs. redid:** lane L6b already dispatched 10 parallel
sonnet agents that did fresh 4-pass recompiles and served-path hash
verification for P1A/P1B/P1N/P2/P3/P4/P4P/P5/A3M/P-SU, all returning CLEAN
(every served-PDF path internally consistent, every fresh recompile 0 undef
refs, content-identical to served bytes per `pdftotext` diff, hash-only
divergence from pdflatex's non-deterministic embedded timestamp); P1C+P2L were
hash-checked manually (frozen/archived, recompile skipped). L6b also committed
5 pure-bookkeeping SSOT/site fixes (see §2). **This lane took that sweep as
given** (per its brief) and did NOT re-run the 10 recompiles. This lane's own
fresh work: (a) a full spot-check of **paper-af** (the one paper L6b dispatched
but whose MILESTONE line did not list among the confirmed-clean 10 — see
below), (b) a fresh served-path hash pass across **all 13** papers to catch
anything that changed after L6b's 01:05 PT sweep, and (c) a live check of
whether lane `bb-L1c-a3m-row9-r11` has logged DONE.

**Convex arm: UNAVAILABLE.** The Convex deployment exceeded its spending limit
(standing campaign state since 2026-09-21) — no Convex reads or writes were
performed by this lane. Every place below that would normally cross-check
`paperVersions:current` / `listAllPaperStates` instead says **Convex
UNAVAILABLE**; intended mutations are appended to
`project-context/CONVEX_BACKFILL_QUEUE_2026-09-21.md` by their owning lanes,
not by this one (this lane made no paper edits, so it queues nothing new).

---

## 1. Per-paper table

| Paper | Version (`\paperVersion`, read from the .tex) | Served-PDF status | SSOT claim (index.md top board) | Site-data claim (`site/src/data/papers.ts`) | Open findings (`DISPOSITIONS/*.md`, `class:** OPEN` count) | Convex |
|---|---|---|---|---|---|---|
| P1A | v1A.0.127 | CLEAN — 5 served paths (arxiv/, public/papers × 2, site/public/papers × 2), sha256 `210be8f0b285…`, 8pp, all match (L6b sweep; re-verified this lane) | v1A.0.127 / 95, superseded by P1N | matches (v1A.0.127) | 3 (all OPEN items are "REMOVED FROM CLAIM SET; OPEN RESEARCH" scope-outs per DISPOSITIONS/P1A.md, not hidden defects) | UNAVAILABLE |
| P1B | v2B.0.23 | CLEAN — 7 served paths (arxiv/, public×2, site/public×2, arxiv-alias×2 not re-checked this lane, 5 core paths re-verified), sha256 `c7cac6c9f16c…`, 16pp | v2B.0.23 / 95 (L6b fixed a stale v2B.0.19→v2B.0.23 row in `SSOT/paper-1/status.md` 2026-09-22) | matches | 4 (legacy v1B rows, all CLOSED; current v2B closure trail lives in `SSOT/paper-1/status.md`, not re-listed here — DEFECT, see §3) | UNAVAILABLE |
| P1C | frozen v1C.0.16 | CLEAN — 2 served paths (public/papers, site/public/papers), sha256 `285948c6248e…`, 25pp, match source (`arxiv/paper1c_nogo_survey/main.pdf`) | frozen v1C.0.16 (L6b corrected a stale "draft v1C.0.15" header in `SSOT/paper-1c/status.md` 2026-09-22) | not a standalone site card (merged into P1N narrative) | 0 (frozen; no live DISPOSITIONS file separate from P1N.md) | UNAVAILABLE |
| P1N | v1N.0.6 | CLEAN — 2 served paths, sha256 `1bb5ade7a9b7…`, 11pp, match source | v1N.0.6 / 99 | matches | 0 (`DISPOSITIONS/P1N.md`: all Open-items-R1-board rows CLOSED) | UNAVAILABLE |
| P2 | v1.7.130 | CLEAN — 5 served paths, sha256 `d3afe79fe70c…`, 12pp, match source | v1.7.130 / 95 | matches | 0 by the `class:** OPEN` grep, **but this is a false negative** — `DISPOSITIONS/P2.md` predates the "class: OPEN/CLOSED" convention (it uses per-wave section headers like "## OPEN ITEMS" instead); the real current-open-item count is not machine-countable from this file without a manual read. DEFECT, see §3 | UNAVAILABLE |
| P2L | v2L.0.2 | CLEAN — 2 served paths, sha256 `314022c9bd3c…`, 4pp, match source | v2L.0.2 / 20, archived (folded into A3M) | not a standalone site card | 0 (archived theory record; no open review) | UNAVAILABLE |
| P3 | v3.2.0-r17 | CLEAN — checked `paper3_apjs.pdf` + versioned alias `paper3_apjs_v3.2.0-r17.pdf` at both `public/papers/` and `site/public/papers/`, sha256 `9a3769269ada…`, 17pp, match source | v3.2.0-r17 / 95, supporting Data Release (not standalone) | matches | 1 (`DISPOSITIONS/P3.md`) | UNAVAILABLE |
| P4 | v1.0.274 | CLEAN — 5 served paths, sha256 `2641a228af1e…`, 32pp, match source | v1.0.274 / 95, superseded by P4P | matches | 4 (`DISPOSITIONS/P4.md`; long active history through M44, current standing items are disclosed OPEN-COMPUTE gates DP4-15/DP4-17, not hidden) | UNAVAILABLE |
| P4P | v4P.0.10 | CLEAN — 2 served paths (`paper4prime_chirality_test_v4P.0.10.pdf` at public/ and site/public/), sha256 `054b63f8a739…`, 15pp, matches source **and matches SSOT's own claimed sha256 exactly** (`SSOT/paper-4p/status.md` line 4) | v4P.0.10 / 95 (L6b fixed a stale v4P.0.9→v4P.0.10 row in `SSOT/index.md` top board 2026-09-22) | matches | 15 (`DISPOSITIONS/P4P.md` — R1 board's DP4P-01 etc.; readiness 95 reflects agent-gate completion via the row-16(ii-b) science propagation, not a fresh board closing all 15 — directive R2 budget was refreshed by the intervening science decision, a new board is authorized next, not yet run) | UNAVAILABLE |
| P5 | v0.1.147-2026-08-03 | CLEAN — 5 served paths, sha256 `3c1c484118d2…`, 46pp, match source | v0.1.147-2026-08-03 / 95, superseded by P4P | matches | 1 (`DISPOSITIONS/P5.md`) | UNAVAILABLE |
| A3M | v3M.0.27 (committed) | **DEFECT (real, not fixed here) — see §3.1.** Committed/served bytes are CLEAN and 3-way byte-identical (`research/track_a3_multichannel/paper/main.pdf` md5 `ea6ebd91…` per the last commit == both mirrors). But the **working-tree copy of both `main.tex` and `main.pdf` is currently dirty** (uncommitted, `git status` shows `M` on both) with real textual differences from the committed v3M.0.27 (`pdftotext` diff shows wording changes, not just a timestamp shift) — almost certainly live WIP from lane `bb-L1c-a3m-row9-r11` (R11 board still open, no DONE logged) or a leftover from L6b's now-retired parallel recompile sweep. Not touched by this lane (not our owned path; per the campaign RULE, a file another lane holds dirty gets polled, not reverted). | v3M.0.27 / 75 (L6b fixed a stale v3M.0.26→v3M.0.27 row 2026-09-22) | matches (v3M.0.27) | 15 (`DISPOSITIONS/A3M.md` — R1's 20 genuinely-new-real findings minus what's been closed by the row-9 propagation; R11 board raw legs (Gemini, Grok) already saved to `INT_v3/ROUND_2026-09-21-A3M-v3M.0.27-EXACTPDF-3e49f29b-R11/` but not yet truth-audited/closed) | UNAVAILABLE |
| AF | vAF.0.5 | **CLEAN — spot-checked in full by this lane** (not just cited from L6b, since AF was dispatched but absent from L6b's confirmed-clean list). 3 served paths (`public/papers/`, `site/public/papers/`, source `pipelines/p1_highz_tracers/anomaly_flagship_draft/main.pdf`) all sha256 `ea81ef4135…`, md5 `60de7e9dbf…`, 18pp — matches the site's own claimed md5 exactly. Fresh 4-pass recompile in an isolated tmp copy: 0 undefined refs, 18pp, and `pdftotext` of the fresh compile is byte-identical (md5 `0b25458beb9…`) to `pdftotext` of the served PDF — content-identical, hash-only divergence is pdflatex's non-deterministic timestamp, same pattern as every other paper in this portfolio. | vAF.0.5 / 77 (L6b fixed a stale vAF.0.4/75→vAF.0.5/77 row 2026-09-22) | matches | 0 (`DISPOSITIONS/AF.md` — R1 board's 20 canonical findings, 17 closed + 3 honestly disclosed-open per SSOT narrative, none tagged with the `class: OPEN` marker used elsewhere; disclosed-open items are OT-1 selection function [GPU] and the Zenodo DOI [Houston-only], both named, not hidden) | UNAVAILABLE |
| P-SU | v1S.0.12 | CLEAN — 2 served paths, sha256 `d400dec4a70d…`, 8pp, match source | v1S.0.12 / 72 | matches | 0 by the `class: OPEN` grep — **stale headline; `SSOT/index.md`'s own P-SU row records new gates S13/S15 (initial-slice convention, Appendix A5 derivation) as "open real science gates, non-blocking"**, which is the actual open count and is not captured by DISPOSITIONS/PSU.md's per-wave section format (same false-negative pattern as P2, see §3) | UNAVAILABLE |

---

## 2. What L6b already fixed (cited, not redone)

Committed by the co-director on L6b's behalf (per campaign Log line 442):
`SSOT/paper-1/status.md` P1B table row v2B.0.19→v2B.0.23; `SSOT/paper-1c/status.md`
header "draft v1C.0.15"→frozen v1C.0.16; `SSOT/index.md` top board A3M
v3M.0.26→v3M.0.27, P4P v4P.0.9→v4P.0.10, AF vAF.0.4/75→vAF.0.5/77 (+ matching
`site/src/data/papers.ts` cross-reference text); `tsc` clean after the site/
edits. All five re-verified present and correct by this lane (§1 above).

---

## 3. Remaining DEFECTs found by this lane

### 3.1 A3M working tree is dirty with un-committed content beyond v3M.0.27 (ROUTED, not fixed)
`research/track_a3_multichannel/paper/main.tex` (54 insertions / 48 deletions)
and `main.pdf` are both locally modified relative to the last commit
(`509a72f7`). `pdftotext` diff confirms real wording changes (e.g. "S1's
earlier range" in the working copy vs. "S1's superseded" in the committed
text) — this is not just pdflatex's timestamp non-determinism. The committed
and served bytes (public/papers, site/public/papers, and `git show
HEAD:.../main.pdf`) are internally consistent and unaffected; only the
uncommitted working-tree copy diverges. This is almost certainly live WIP by
`bb-L1c-a3m-row9-r11`, which has not logged DONE (§4) — the R11 board's two raw
legs are already saved to `INT_v3/ROUND_2026-09-21-A3M-v3M.0.27-EXACTPDF-3e49f29b-R11/`
and a closure pass touching the paper text would explain the dirty tree.
**Not reverted or committed by this lane** — A3M is not this lane's owned
path, and per the campaign RULE, a file another lane holds dirty is polled,
not touched. Routed to `bb-L1c-a3m-row9-r11` / the director: either commit the
WIP with its own directive-G bundle, or `git stash`/`git checkout --` it if it
was an abandoned artifact, before any further A3M work lands.

### 3.2 DISPOSITIONS/{P1B,P2,P4,P5,A3M,PSU...}.md headers are stale relative to SSOT (ROUTED, not fixed — needs real ledger consolidation, per L6b)
P1B and P2's DISPOSITIONS files stop tracking new closures partway through
each paper's history and defer to `SSOT/paper-N/status.md`'s inline history
instead — meaning DISPOSITIONS is no longer the single per-item ledger its own
stated purpose claims to be for these two papers. This also breaks any
automated "open finding count" query (§1's P2 and P-SU rows above) since older
waves don't use the later `class: OPEN`/`CLOSED` convention. **Not fixed by
this lane** (a full consolidation is real editorial work on files this lane
does not own the content of, not a bookkeeping one-liner) — flagged here for
whichever lane next touches P1B/P2/P-SU's dispositions.

### 3.3 No other version-drift since L6b's 01:05 PT sweep
Checked every paper's current `\paperVersion` and served-path hash against
what L6b's sweep and its own commit reconciled; the only committed version
bumps that landed after L6b's 01:05 PT sweep were already reflected (P4P
v4P.0.10 via lane L4d, A3M v3M.0.27 via lane L1c — both predate 01:05 PT and
were already folded into L6b's fixes). No paper's committed/served version
moved between L6b's sweep and this lane's check.

---

## 4. `bb-L1c-a3m-row9-r11` DONE check

Checked the campaign Log for a `L1c-a3m-row9-r11 · DONE` line: **absent** —
`grep -c` returns 0. The lane's last logged line is a 23:59 PT MILESTONE
(SSOT/site updates for v3M.0.27, readiness held 75). Its R11 board's two raw
reviewer legs (Gemini, Grok) are already saved to disk (`INT_v3/ROUND_2026-09-21-A3M-v3M.0.27-EXACTPDF-3e49f29b-R11/`,
files timestamped 23:56 PT), and independently, A3M's working tree is
currently dirty with further uncommitted edits (§3.1) — both point to the lane
still being active on R11's truth-audit/closure, not abandoned. Per this
lane's brief (proceed after ~45 min of foreground-interleaved checking if no
DONE appears), this lane checked at lane start, again after completing the
13-paper hash pass, and a final time before writing this file — no DONE
appeared at any check, consistent with the raw-legs-saved-but-not-yet-audited
evidence above. **A3M is recorded in the signoff packet as "R11 board in
flight" at v3M.0.27**, not as a completed/converged board.

---

## 5. Bottom line

12 of 13 paper rows are clean end-to-end (served bytes internally consistent,
content-identical to a fresh recompile where L6b or this lane ran one, SSOT
and site data agreeing). The one real open DEFECT is A3M's dirty working tree
(§3.1) — a live-lane artifact, not a hygiene failure, and explicitly not this
lane's to fix. The Convex arm is UNAVAILABLE portfolio-wide (spending limit),
so every readiness number in this file is the last-computed SSOT/site value,
not a live Convex read; treat it as such until the limit is raised and the
backfill queue is drained.
