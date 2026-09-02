# ARCHITECTURE — bigbounce review-program

The full system that turns a compiled paper PDF into a verified, source-cited
verdict on the live All-A grid. This doc is the map; canonical state lives in
SSOT / the scistack SKILL.md / DISPOSITIONS / Convex (see `README.md`).

---

## 1. Component map

```
                        ┌──────────────────────── SCHEDULING LAYER ────────────────────────┐
                        │  in-session cron (Claude Code, session-only, */20)                │
                        │  launchd com.bigbounce.cron-tick  ── App Support/…-cron-tick.sh   │
                        │  launchd com.bigbounce.loopwatchdog (15min) ─ loop_watchdog.sh    │
                        │  launchd com.bigbounce.caffeinate (keep-awake, -i)                │
                        │  LOOP_HEARTBEAT.json  ⇄  watchdog: stale>45m ⇒ headless recovery  │
                        └──────────────────────────────────┬───────────────────────────────┘
                                                            │ each tick
                                                            ▼
        ┌───────────────────────────────────── SUBMISSION LAYER ─────────────────────────────────────┐
        │  wave_submit.sh <round> <PAPER:reviewer>…    (PER-LEG ISOLATION — no set -e across legs)     │
        │      └─▶ ext_submit.sh <PAPER> <reviewer> <round> [pdf]   — one leg / invocation             │
        │           guards (all sha-cited, all in ext_submit):                                         │
        │             · stale pre-send /c/ URL rejected .................... 3fb1ffd9                  │
        │             · dispatch always terminates OK-or-FAIL ............... a08dd750                  │
        │             · ChatGPT poll 120s + sidebar content-liveness ....... 02d68a8f                  │
        │             · OK REQUIRES non-empty chat URL (else die) .......... 80914698                  │
        │             · composer-scoped attachment-token verify ............ 854acb99                  │
        │           writes → EXT_real/H17_2026-07-10/manifest.jsonl  (URL-at-submit, per leg)          │
        └───────────────────────────────────────────┬───────────────────────────────────────────────┘
                                                     │ manifest rows: submitted-<...>
                                                     ▼
        ┌───────────────────────────────────── HARVEST LAYER ────────────────────────────────────────┐
        │  ext_harvest.sh <round>   — visit each chat URL, extract w/ reviewer selectors               │
        │      gates before a row flips to "harvested" (2f5efb53):                                     │
        │        substance (min-length, not a prompt-echo stub / 0-byte)                               │
        │        duplicate  (not the prior leg's raw)                                                  │
        │        paper-signature provenance (raw carries THIS paper's signatures, not another's)       │
        │      real verdict ⇒ harvested (raw .md + .png saved) · dead ⇒ FAILED-dead · else "cooking"   │
        └───────────────────────────────────────────┬───────────────────────────────────────────────┘
                                                     │ raw .md + .png per leg
                                                     ▼
        ┌─────────────────────────────────── ADJUDICATION LAYER ─────────────────────────────────────┐
        │  ledger_match.py <raw> <P>    fingerprint pre-triage vs DISPOSITIONS/<P>.md (MATCHED/UNMATCHED)│
        │      └─▶ Opus strict adjudicator(s)  — read EVERY raw + screenshot VERBATIM (directive I4)     │
        │           truth-audit each finding: VERIFIED / FALSIFIED / STALE / OUT-OF-SCOPE / OPINION      │
        │           I4 no-raw-no-verdict · source-cited disposition · never fake ACCEPT                 │
        │           provenance: signature-grep confirms the raw is this paper before any verdict         │
        └───────────────────────────────────────────┬───────────────────────────────────────────────┘
                                                     │ verdict + (genuinelyNew? → close first)
                                                     ▼
        ┌──────────────────────────────────── RECORDING LAYER ───────────────────────────────────────┐
        │  post_verdict.sh <paper> <label> <rec> <maj> <min> <raw>   (cd02c991)                        │
        │      externalReviews:upsertByLabelDate → latest-per-EXT-reviewer by _creationTime DESC        │
        │      cap = 50 + Σ{grok,chatgpt,gemini} { ACCEPT 16.7 · MINOR 12 · MAJOR 6 · REJECT 0 }        │
        │      → papers:setReadinessCap                                                                 │
        │  record_wave.sh <paper> <wave> <date> <gNew> <streak> <oComp> <oVenue> "<verdicts>" [note]   │
        │      → readinessMetrics:recordWave (idempotent on paper+wave; clobber-guard skips auto-call   │
        │        when a rich verdict row already exists) · verdict "failed" = chart GAP, never a zero   │
        │      INT legs post under label <wave>-INT-<vendor> (029cb689) so they never displace EXT rows │
        └───────────────────────────────────────────┬───────────────────────────────────────────────┘
                                                     │ Convex tables now current
                                                     ▼
        ┌────────────────────────────────────── SITE LAYER ──────────────────────────────────────────┐
        │  live-status.ts · reviewTimeline.ts · SSOT/*.md  = mirrors of Convex (Convex is truth)        │
        │  /reviews All-A verdict grid (CURRENT column, newest-left) — the terminal criterion surface   │
        │  site_freshness_check.sh (ccd593c1) — pre-push hook: banner/skills/board/versions vs Convex    │
        └────────────────────────────────────────────────────────────────────────────────────────────┘

        ┌──────────────────── SCIENCE-CLOSURE LAYER (when a finding is genuinely-new) ───────────────┐
        │  directive_g.sh <P> <ver> "<changelog>"  — full PDF hygiene chain:                          │
        │    verify tex version+date · leak-gate grep · compile (pdflatex 2-pass +bibtex) ·           │
        │    mirror byte-identical to every served path + versioned aliases ·                         │
        │    paperVersions:bump + read-back verify (compile md5 == served md5 == Convex md5)           │
        │  directive I6 — regenerate every FIGURE IMAGE that renders a corrected value (PNG-baked)     │
        └────────────────────────────────────────────────────────────────────────────────────────────┘

        ┌──────────────────────────── INT BATTERY ────────────────┐   ┌──────────── BACKUP LAYER ───────────┐
        │  int_wave.sh <P> — subscription + API legs in parallel:  │   │  backup-3plus before any destructive │
        │   OpenAI = Codex/ChatGPT SUBSCRIPTION, API keys unset;    │   │  op; RunPod data ⇒ local + HF + B2    │
        │   Grok + Gemini use their APIs. Every leg saves its raw. │   │  (+Convex metadata). ALWAYS, not just │
        │   OpenAI API review dispatch is permanently forbidden.  │   │  before-stop (directive E).           │
        └──────────────────────────────────────────────────────────┘   └──────────────────────────────────────┘
```

---

## 2. Data-flow — one wave's lifecycle

| # | Step | Command / actor | Artifact (path) |
|---|------|-----------------|-----------------|
| 1 | Place the wave | `tools/wave_submit.sh M40 P4:grok P4:chatgpt …` | per-leg logs; summary table |
| 2 | Submit each leg | `wave_submit` → `tools/ext_submit.sh` (headed gstack Chrome) | manifest row `submitted-…` + captured `/c/` URL in `project-context/peer-reviews/EXT_real/H17_2026-07-10/manifest.jsonl` |
| 3 | Harvest | `tools/ext_harvest.sh M40` | raw `.md` + `.png` per leg in `EXT_real/H17_2026-07-10/M40/`; manifest flips to `harvested` |
| 4 | Substance/dup/signature gates | inside `ext_harvest` (2f5efb53) | stub/0-byte/misfiled raws never reach a verdict |
| 5 | Fingerprint pre-triage | `tools/ledger_match.py <raw> <P>` | draft MATCHED/UNMATCHED table vs `DISPOSITIONS/<P>.md` |
| 6 | Adjudicate | Opus adjudicator reads every raw+png (I4) | truth-audit `EXT_real/H17_2026-07-10/M40/<P>_truth_audit_M40.md` |
| 6a | If genuinely-new | close with real edit/science → `tools/directive_g.sh <P> <ver>` | bumped `.tex`, mirrored PDFs, `paperVersions:bump` |
| 7 | Record verdict + cap | `tools/post_verdict.sh <P> <label> <rec> <maj> <min> <raw>` | Convex `externalReviews` + `papers:setReadinessCap` |
| 8 | Record wave row | `tools/record_wave.sh <P> M40 <date> <gNew> <streak> …` | Convex `readinessMetrics` (trajectory + ETA) |
| 9 | Mirror to surfaces | edit `site/src/data/live-status.ts`, `reviewTimeline.ts`, `SSOT/*` | same commit as the round |
| 10 | Freshness gate + push | `site_freshness_check.sh` pre-push hook (ccd593c1) | blocks push if any surface stale vs Convex |
| 11 | Grid render | Convex subscription → `/reviews` All-A grid | CURRENT column updates (newest-left) |

Reviewer projects: Grok `grok.com/project/e6c9ce77…`, ChatGPT `chatgpt.com/g/g-p-6881c7f3…/project`, Gemini `gemini.google.com/u/1/app` (houston@bamf.com Ultra). Headed browser is MANDATORY for EXT (`$B connect`, `Mode: headed`).

---

## 3. Invariants (the never-break list)

1. **Never fake an ACCEPT.** No verdict word is recorded that a raw does not literally support.
2. **Every leg saves its raw + screenshot BEFORE any verdict is recorded** (directive I4). No raw ⇒ FAILED, never a verdict.
3. **Source-cited dispositions.** No finding is dismissed non-real without a citation to a `.tex` line / artifact / `DISPOSITIONS/<P>.md` id.
4. **Single browser driver.** Exactly one owner drives the headed Chrome window at a time (concurrent-driver yield, §4).
5. **Single ledger writer.** The orchestrator's `record_wave.sh` is the authoritative wave-row writer; `post_verdict`'s auto-call skips when a rich row exists (cd02c991).
6. **Caps are verdict-derived only.** Readiness = `50 + Σ per-reviewer score`; never hand-set (directive A / readiness-cap rules).
7. **Convex is live-site truth.** `live-status.ts` / `reviewTimeline.ts` / SSOT are mirrors; they never drive readiness.
8. **PROCESS-NIT rule.** A referee complaint about the review *process* (not the paper's science) is a PROCESS-NIT — dispositioned, never a paper defect and never a paper edit.
9. **Concurrent-driver yield.** A tick that detects another active owner (recent commits, files changing underneath) YIELDs: no browser drive, no competing commit/push. `harvest` + `post_verdict.sh` stay safe.
10. **Never fabricate to make a finding go away** (patterns 036, 061-064). A technically-specific claim that could be genuinely-new is re-derived, not hand-waved (e.g. P2 orbit double-counting was falsified by re-running `p2_vertex_check.py` + the Li et al. closed form).

---

## 4. Concurrency model

**Coexisting actors:**
- **Fable 5 orchestrator** — planning only: decides the tick, splits legs, resolves conflicts, accepts/rejects the bundle. Never does mechanical execution.
- **Opus adjudicators** — one per paper/leg; read raws, truth-audit, emit verdicts. Judgment-heavy, spawned in parallel.
- **Codex driver** — may independently drive the same papers. Detected via recent commits + files changing underneath, NOT a narrow `ps` grep (the 2026-07-12 root cause).

**Coexistence rules:**
- Hourly tick begins with a **STATE-CHECK**: is another owner active? If yes → **YIELD** (`harvest` + `post_verdict.sh` are still safe; do not drive the browser, do not commit a competing bundle, do not push).
- Exactly one browser-window owner at a time.
- `git pull --rebase` before every push.

**Stall recovery:** if an adjudicator or the whole loop stalls, a **fresh agent audits Convex FIRST** (the source of truth) before acting — it reconciles what's already recorded so it does not double-post a verdict or re-drive a leg that already landed. The launchd watchdog is the outer guarantee: a stale (`>45m`) `LOOP_HEARTBEAT.json` triggers a headless recovery tick that writes a fresh heartbeat, runs `site_freshness_check`, and harvests any submitted-unharvested manifests.

## Remote policy (recorded 2026-09-02)

- **`origin` = `github.com/Hubify-Projects/bigbounce` is canonical.** `main`
  tracks it; the pre-push freshness gate runs against it; every paper, the
  site, the Zenodo records, and the reproducibility manifests cite it (45
  citations as of 2026-09-02). All work is committed and pushed here first.
- **`upstream` = `github.com/houstongolden/bigbounce` is a fast-forward-only
  mirror** (Houston's original repo; both are public). It receives the same
  `main` after `origin`, never a different history. Nobody — human or agent —
  commits or pushes to it directly; if that happens (as with `54057420`, the
  2026-08-28 research-watch brief found only on upstream), the reconciliation
  step brings the commit into `origin` first, then re-mirrors.
- Divergence between the two is a defect to fix in the same session it is
  found (`REPO_RECONCILIATION_<date>.md`), because two public histories with
  different content undermine the provenance the papers cite.
