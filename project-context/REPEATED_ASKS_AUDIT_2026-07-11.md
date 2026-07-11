# Repeated-Asks Audit — every reminder class + automation plan (2026-07-11)

Triggered by Houston, 2026-07-11: *"why am i still repeating myself this shit after
months?! … please audit my whole claude history and prompt history and everything
for this project and find all the gaps and things im constantly repeating myself on
that should be proper crons or even daemons or something or routines or skills."*

**Method.** Read `project-context/prompts.md`, all 32 session transcripts under
`~/.claude/projects/.../*.jsonl` (filtered to Houston's own user messages,
frustration/reminder markers), the 18 distilled `memory/*.md` feedback entries, and
`ACCELERATION_LOG_2026-07-10.md`. 14 distinct strong human reminder events isolated
(June 26 → July 11); clustered into the classes below. Live-state probes run against
crontab, launchd, git hooks, and the tool inventory to set each item's current state.

**Headline finding.** The single most-repeated class — *the loop/cron dies and I
have to notice and restart it* — is **still UNFIXED as of this audit**, and its live
root cause was found: the launchd tick is stuck skipping on a stale lock.

---

## Live-state probe results (2026-07-11)

| Probe | Result |
|-------|--------|
| `crontab -l` | empty (1 blank line) — no user cron |
| launchd agents | `com.bigbounce.cron-tick` **loaded but status `-`** (not running); `com.bigbounce.caffeinate` running (PID live) |
| cron-tick plist | fires `Minute:7` hourly, `RunAtLoad=false`, invokes `~/Library/Application Support/bigbounce/bigbounce-cron-tick.sh` |
| `launchd.err` | `.../scripts/bigbounce-cron-tick.sh: Operation not permitted` (TCC/path artifact from an earlier plist rev) |
| Last real tick log | `tick-20260710-020704.log` (~33h before audit) |
| `cron-logs/skips.log` | **every hourly tick from 2026-07-10 13:15 → 2026-07-11 00:07 logged `lock race — skipping`** |
| `/tmp/bigbounce-cron.lock` stale-reclaim | 90-min reclaim not clearing the lock → permanent skip loop = "no cron going" |
| pre-push hook | present (`site_freshness_check.sh` gate) — stale-surface class fix is live |
| verdict-gap trajectory chart | **absent** from `site/src/data/` (only `reviewTimeline.ts`) |
| sha-traceable skills-chart | not automated (manual `skillsSeries` + `ACCELERATION_LOG`) |

---

## Repeated-ask classes

### 1. Loop/cron dies; I have to notice and restart it  — **UNFIXED (root cause found)**
- **First:** 2026-06-28. **Count:** ≥5 (06-28, 06-30, 07-09 ×2, 07-11) — the #1 class.
- Verbatim 06-28: *"why have you stopped? you are supposed to have a cron loop that
  fires every 30mins … and continues improving the papers … until all papers have no
  major or minor blockers."*
- Verbatim 07-11: *"whas goin on now you stopped no cron going why am i still having to
  remind you this when you should always have the cron running never stopping."*
- **Wants:** a durable, self-healing 24/7 loop that never needs a human restart, survives
  reboot/context-exhaustion, and self-terminates a hung tick.
- **State:** A launchd tick exists (`com.bigbounce.cron-tick`) but is **effectively dead** —
  stuck in an hourly `lock race — skipping` loop on a stale `/tmp/bigbounce-cron.lock`
  since ~2026-07-10 13:00; the 90-min stale-lock reclaim is not clearing it. Earlier the
  plist also hit `Operation not permitted` (TCC). No watchdog verifies the tick actually
  runs. **FIXED-BY:** partial infra only (`bigbounce-cron-tick.sh`, caffeinate agent).
  **UNFIXED:** liveness/self-heal.
- **Automation that kills the class:** a **watchdog daemon** (separate launchd agent,
  1–5 min interval) that (a) reclaims a stale lock older than the max tick duration,
  (b) asserts a heartbeat file was touched within N minutes and force-restarts the tick
  if not, (c) alerts (Convex activity row + local notification) on repeated failure so a
  dead loop surfaces *to me*, never to Houston. *(A parallel agent is implementing this.)*

### 2. Stale public site surfaces (banner / reviews board / skills chart / versions) — **FIXED**
- **First:** 2026-06-30. **Count:** ≥5 (06-30, 07-07 ×2, 07-08, 07-11).
- Verbatim 07-11: *"on the top of the overview page … it shows the last status update was
  3 days ago bro wtf … and doesn't even reflect … the paper merger that had been recommended."*
- Verbatim 07-08: *"i am not seeing ANY new reviews on the …/reviews page and the last one
  from yesterday still just shows almost all rejected and major issues."*
- **Wants:** every derived surface always reflects true current state, same commit as the round.
- **State:** **FIXED-BY** `tools/site_freshness_check.sh` + `.git/hooks/pre-push` gate
  (sha `0c263178`, 2026-07-10): banner-vs-latest-wave, skillsSeries-vs-latest-lesson-commit,
  board-vs-manifest, versions-vs-Convex all machine-checked and block a push while stale.
  Directive A + `feedback_stale_surface_root_cause`. **Residual:** the gate only runs at
  push; it must ALSO run each cron tick (belongs with the watchdog) so drift is caught
  between pushes. Mark **PARTIALLY** on cron-tick coverage.

### 3. Self-improvement is untracked / possibly faked — **PARTIALLY**
- **First:** 2026-06-26. **Count:** ≥3 (06-26, 07-09, 07-11).
- Verbatim 07-11: *"maybe you are faking it after the fact i dont know no way to verify or
  trace our actual improvements at each review round … you still make the same mistakes and
  haven't solved the root problems."*
- Verbatim 06-26: *"please remember to update your own instructions and prompts and skills …
  so i do not have to remind you about any of this ever again."*
- **Wants:** every claimed process-improvement is real, dated, and traceable to a commit.
- **State:** `ACCELERATION_LOG_2026-07-10.md` + `skillsSeries` capture improvements, and the
  CLAUDE.md rule requires a `kind:"skill-improvement"` timeline entry per upgrade. But entries
  are **hand-written and not sha-stamped** — exactly the "no way to trace" gap.
  **PARTIALLY.** Fix: a `skillsSeries`/self-improvement generator that derives each entry from
  git history (commit sha + file path + timestamp), so backfills come from git only and every
  chart point is clickable to its introducing commit. Enforce via the freshness gate.

### 4. Verdict-gap trend visibility — **UNFIXED**
- **First:** 2026-07-11. **Count:** 1 explicit, but elevated by Houston to *the* headline metric.
- Verbatim: *"the new gaps ledger that matters more than the INT/EXT gaps ledger is basically
  closing the gap on each round … from rejection/major closer and closer to minor/accepted."*
- **Wants:** lead every report + a site chart with the per-paper × per-reviewer verdict score
  (REJECT=0 → ACCEPT=3) trajectory across rounds, with rigor-event annotations.
- **State:** captured in `feedback_verdict_gap_headline` + `readinessMetrics` groundwork
  (`record_wave.sh`/`post_verdict.sh`, sha `6f4180cf`), but **no trajectory chart exists** in
  `site/src/data/` and loop reports don't yet lead with it. **UNFIXED.**
  Fix: `verdictTrajectory.ts` data + a site chart; loop-report template leads with gap delta.

### 5. Unacceptable ETA / "weeks-to-months" / do-it-now — **PARTIALLY**
- **First:** 2026-07-07. **Count:** 2 (07-07, plus the 07-07 companion-paper thread).
- Verbatim: *"weeks to months is not acceptable we need to get these done ASAP … wtf? why do
  we need to write additional companion papers now?"*
- **Wants:** no open-ended human-scale estimates; collapse work to the loop or name the exact
  Houston-gated blocker (arXiv click, API key, human referee) — nothing vaguer.
- **State:** the two-category gate + `feedback_verifiable_review_reset` do route to explicit
  Houston-gated blockers, but there is **no standing ETA-honesty gate** in report generation.
  **PARTIALLY.** Fix: a report-lint rule banning "weeks/months/future" without an attached
  named blocker owner (self-improvement, disallow vague deferral — directive parallels
  `/no-future-work-defer`).

### 6. Papers-merge status not surfaced — **UNFIXED**
- **First:** 2026-07-11. **Count:** 1 (embedded in the stale-banner complaint).
- Verbatim: *"doesn't even reflect that we have … the paper merger that had been recommended."*
- **Wants:** the reviewer-recommended P1B→P1A merge (and any merge decisions) reflected on the
  site + SSOT.
- **State:** merge recommendation lives in `feedback_verifiable_review_reset` (P1B "not
  standalone → reviewer-unanimous merge into P1A") but **is not represented on any public
  surface.** **UNFIXED.** Fix: add a merge-status field to `papers.ts`/Convex + render it;
  add to the freshness gate's checklist.

### 7. Only 1 subagent working / underutilized parallelism — **UNFIXED**
- **First:** 2026-07-09. **Count:** 2 (07-09 ×2).
- Verbatim: *"i only see 1 subagent working and you aren't working on anything … whats going
  on bro this is unacceptable"*; *"you are not running any subagents or paper reviews or
  anything wtf."*
- **Wants:** the loop always fans out one owner-agent per below-bar paper in parallel (directive
  J never-idle), never sits on a single serial worker.
- **State:** fused-owner-loop pattern exists (ACCELERATION_LOG #1) and directive J mandates
  never-idle parallel fan-out, but **nothing enforces N-way utilization at tick time.**
  **UNFIXED.** Fix: the cron tick, when idle, must spawn one Opus owner per below-bar paper in a
  single message; a utilization assertion in the tick logs (and fails loud) if <N owners for N
  below-bar papers.

### 8. Unverifiable reviews / fabricated convergence — **FIXED**
- **First:** 2026-07-04. **Count:** ≥3 (07-04, 07-08, 07-09), the highest-stakes class.
- Verbatim 07-08: *"you have stopped and keep acting like the papers are all done!"*
- **Wants:** never fake an ACCEPT/converged; every EXT leg saves raw text + screenshot READ
  before any verdict; never drop ChatGPT; Claude INT = subscription subagent not API.
- **State:** **FIXED-BY** CLAUDE.md directives I1–I5 + `feedback_verifiable_review_reset` +
  `int_wave.sh`/`ext_submit.sh`/`ext_harvest.sh` (raw-save-then-verdict enforced) +
  `bigbounce-truth-audit` MCP (verdict-first ordering enforced at the mutation layer).
  Residual watch: keep the raw-save gate; no new automation required.

### 9. Browser / EXT flakiness (headed browser, Gemini throttle) — **PARTIALLY**
- **First:** 2026-07-06. **Count:** 2 (07-06 headed-browser reminder; 07-10 Gemini-throttle loss).
- Verbatim 07-06: *"please update skills/instructions … to always use the headed browser for
  this ext review process … i shouldnt have to remind you that."*
- **Wants:** never fall back to headless; never burn hours on a silently-throttled leg.
- **State:** headed-browser rule is now a hard gate (CLAUDE.md I4, `/connect-chrome`); ext scripts
  auto-`$B connect`-and-retry on crash (ACCELERATION_LOG #13). Gemini browser throttle demoted to
  1 attempt/day with send-verification. **PARTIALLY** — the true fix (billed Gemini API key) is
  **Houston-gated**, tracked as a standing bottleneck. No further automation possible on our side.

### 10. Readiness honesty / fake 99%/complete claims — **FIXED**
- **First:** 2026-07-07. **Count:** ≥2 (07-07 ×2).
- Verbatim: *"we have not properly passed the EXT reviews not even close"* (rejecting ladder-99).
- **Wants:** displayed readiness/"complete" tracks the LITERAL verdict board, never the internal
  recalibrated gate; Convex is the one source; static mirrors never drift.
- **State:** **FIXED-BY** directive A + `papers:setReadinessCap` (Convex single source) + the
  freshness gate checking displayed-vs-Convex; verification-complete vs review-passed displayed
  separately (`feedback_verifiable_review_reset` 07-07 lesson #2). `readiness-cap-99` skill caps
  100% behind a Houston quote.

### 11. Prompt-history logging discipline — **FIXED (gate not automated)**
- **First:** 2026-06-26. **Count:** 1 explicit + standing rule.
- Verbatim: *"the things ive been asking for in the prompts … which you should have saved to the
  prompt history."*
- **State:** `/prompt-history` skill + `project-context/prompts.md` are the standing mechanism;
  CLAUDE.md routes every brain-dump there BEFORE work. **FIXED** procedurally.
  Minor residual: no hard gate that a new Houston message was logged before the work commit — low
  priority; could be a pre-commit reminder.

### 12. Backup discipline (RunPod / HF / B2) — **FIXED**
- **First:** 2026-06-26 (directive E). **Count:** standing directive, no repeat frustration in-window.
- **State:** **FIXED-BY** directive E + `/backup-3plus` + `/pod-backup-before-stop`: always-backup
  (not just before stop) to local + HF + B2 + Convex metadata. No new frustration events found;
  keep as standing rule.

### 13. Commit/push cadence — **FIXED**
- **State:** global CLAUDE.md "commit autonomously + always bisect" + `/commit-message-atomic`.
  No repeated Houston reminder in-window. **FIXED.**

### 14. Site QA after updates — **FIXED (procedural)**
- **First:** 2026-06-26 (directive C). **Count:** folded into class 2.
- **State:** **FIXED-BY** directive C (headed browser visual QA after every site/Convex update) +
  the freshness gate. Procedural; the freshness gate now catches most staleness pre-QA.

### 15. Chart / figure readability & figures-on-paper-page — **PARTIALLY**
- **First:** ~2026-07 figures thread (prompts.md L122, L148). **Count:** 1–2.
- Verbatim: *"i don't like the level you have cut down on the figures … add back … a section that
  shows ALL FIGURES on the paper page … enlarge fonts and promote to figure*."*
- **State:** `figures.ts` + a figures page exist; font-enlarge/dedup handled per D-round.
  **PARTIALLY** — no standing gate that every accurate figure is surfaced on each paper page, and
  chart-readability (font sizes on trend charts) is not linted. Low urgency vs the loop classes.

### 16. INT↔EXT review-gap (the historic top bottleneck) — **FIXED**
- **First:** ~2026-06 (prompts.md L97–L109), months-long. **Count:** the single most-emphasized
  historical bottleneck.
- Verbatim: *"such a wide gap between … ChatGPT, Grok, Gemini … and what you are saying when you
  run the review … the biggest bottleneck … close that gap completely."*
- **State:** **FIXED-BY** native-PDF INT (`v3_native_pdf_review.py`, `int_wave.sh`), all-vendor
  INT matrix (directive I1), disposition ledgers, and pattern-066 calibration — INT now runs the
  same PDFs/prompts as EXT. Reconfirmed as the accel-era baseline.

---

## Ordered implementation queue (UNFIXED / PARTIAL, by recurrence × impact)

1. **Cron watchdog daemon** *(class 1 — highest recurrence × impact; parallel agent building it).*
   Separate launchd agent @1–5 min: reclaim stale `/tmp/bigbounce-cron.lock` > max-tick-age;
   assert a heartbeat file touched within N min else force-restart the tick; log + Convex-alert on
   repeated failure. Also fix the current stuck lock + the stale `Operation not permitted` plist path.
2. **Freshness gate on every cron tick** *(class 2/3 residual).* Invoke `site_freshness_check.sh`
   inside `bigbounce-cron-tick.sh` (not only at push); any stale surface is auto-fixed or the tick
   fails loud — drift never waits for the next push or for Houston.
3. **Sha-traceable self-improvement generator** *(class 3).* Script that regenerates `skillsSeries`
   / self-improvement timeline entries from git history (sha + path + commit timestamp); wire into
   the freshness gate so every chart point is verifiable and backfills come only from git.
4. **Verdict-gap trajectory chart + report-lead** *(class 4).* `site/src/data/verdictTrajectory.ts`
   (paper × reviewer × round, REJECT=0→ACCEPT=3, rigor-event annotations) + a site chart; loop-report
   template leads with per-paper + program gap delta vs prior round.
5. **Never-idle parallel-fan-out enforcement** *(class 7).* In the idle branch, the tick spawns one
   Opus owner per below-bar paper in a single message and logs a utilization assertion (fails loud if
   <N owners for N below-bar papers) — kills "only 1 subagent working."

*(Follow-ons, lower priority: 6. merge-status surface field + gate (class 6); 7. ETA-honesty
report-lint banning vague weeks/months without a named blocker (class 5); 8. figures-completeness
+ chart-readability gate on paper pages (class 15).)*

**DO NOT implement here** — the watchdog (queue #1) is owned by a parallel agent; the orchestrator
dispatches the remainder from this queue.
