# RUNBOOK — bigbounce review-program operations

Operational procedures. The round-level protocol is canonical in
`~/.claude/scistack/astrostack/bigbounce-r-round/SKILL.md`; this doc is the
day-to-day command sheet + recovery playbooks. All paths repo-relative to
`/Users/houstongolden/Desktop/CODE_YOU/bigbounce`.

---

## 1. Per-tick protocol (exact commands)

```bash
cd /Users/houstongolden/Desktop/CODE_YOU/bigbounce

# 0. REMOTE LEASE GATE — never drives from local LEASE.json.
MACHINE_ID="${BIGBOUNCE_MACHINE_ID:-$(hostname -s)}"
if tools/lab_lease.sh holds "$MACHINE_ID"; then
  tools/lab_lease.sh renew "$MACHINE_ID" 45
  DRIVER=1
elif tools/lab_lease.sh claim "$MACHINE_ID" 45; then
  DRIVER=1
else
  DRIVER=0   # fail closed: INT/compute/docs only; no browser/adjudication/verdict writes
fi

# Heartbeat always attributes the tick and role to this machine.
python3 - "$MACHINE_ID" "$DRIVER" <<'PY'
import datetime, json, sys
role = "driver" if sys.argv[2] == "1" else "lease-free"
json.dump({"lastTickUTC": datetime.datetime.now(datetime.timezone.utc).isoformat(),
           "source": "orchestrator", "machineId": sys.argv[1], "role": role,
           "note": "manual tick"}, open("project-context/LOOP_HEARTBEAT.json", "w"), indent=2)
open("project-context/LOOP_HEARTBEAT.json", "a").write("\n")
PY

# 0a. STATE-CHECK — additional same-machine/agent overlap defense.
git log --oneline -5                 # recent commits by another owner?
git status                           # files changing underneath you?
# If a concurrent driver is detected → YIELD (harvest + post_verdict still safe;
# do NOT drive the browser, do NOT commit a competing bundle, do NOT push).

# 1. Read canonical state FIRST (never trust site HTML / static files).
sed -n '1,40p' project-context/SSOT/index.md
curl -s https://brilliant-panther-471.convex.cloud/api/query \
  -H 'content-type: application/json' \
  -d '{"path":"readinessMetrics:listWaves","args":{}}' | tail -c 2000

# 2. DRIVER ONLY: ensure HEADED browser for EXT. Skip steps 2-7 when DRIVER=0;
# run a bounded INT API / compute / reproducibility / disjoint-docs task instead.
[ "$DRIVER" -eq 1 ] || { tools/int_wave.sh P3; exit $?; }
B=~/.claude/skills/gstack/browse/dist/browse; $B cleanup; $B connect
# Confirm Mode: headed. Renew the lease every ~20 min during a long driver phase.

# 3. Place the wave (per-leg isolation — one leg failing never stops the chain).
tools/wave_submit.sh M40 P4:grok P4:chatgpt P2:grok P2:chatgpt

# 4. Harvest (substance/duplicate/paper-signature gates run inside).
tools/ext_harvest.sh M40

# 5. Fingerprint pre-triage per raw, then Opus adjudicates (reads EVERY raw+png).
tools/ledger_match.py project-context/peer-reviews/EXT_real/H17_2026-07-10/M40/<raw>.md P4
#   → truth-audit written to EXT_real/H17_2026-07-10/M40/<P>_truth_audit_M40.md

# 5a. If a finding is GENUINELY-NEW: close it with a real edit/science, then:
tools/directive_g.sh P4 1.0.241 "close <finding> — <one-line changelog>"

# 6. Record verdicts + cap, then the wave row.
tools/post_verdict.sh P4 M40-Grok major-revisions 1 4 <raw-path>
tools/record_wave.sh P4 M40 2026-07-13 0 13 0 0 \
  "Grok:EXT:major-revisions,ChatGPT:EXT:reject,Gemini:EXT:failed" "0 genuinely-new"

# 7. Mirror surfaces in the SAME commit, run the freshness gate, push.
#    edit site/src/data/{live-status.ts,reviewTimeline.ts} + SSOT/*
tools/site_freshness_check.sh --report
git add -A && git commit -m "feat(M40-EXT): adjudicate P4/P2 — 0 genuinely-new …"
git pull --rebase && git push          # pre-push hook re-runs the freshness gate
```

The lease commands fetch `origin/main`, validate the remote JSON, and use an
isolated temporary git index plus `commit-tree`/`--force-with-lease` CAS. They
never pull/rebase/stash, stage files, move `HEAD`, or alter the current worktree.
Any fetch, parse, or CAS uncertainty fails closed into lease-free mode.

INT battery (run alongside EXT on the other papers): `tools/int_wave.sh P3` —
OpenAI + Grok native-PDF + Gemini(if key) + Claude subscription (ANTHROPIC_API_KEY
UNSET). Every leg saves its raw; a verdict matrix prints at the end.

---

## 2. Wave placement via wave_submit

- Format: `tools/wave_submit.sh <round> <PAPER:reviewer> [<PAPER:reviewer> …]`, e.g. `tools/wave_submit.sh M41 P5:grok P5:chatgpt P1U:grok`.
- Papers: `P1U P2 P3 P4 P5`; reviewers: `grok chatgpt gemini`.
- `--dry-run` prints the planned legs + summary path WITHOUT driving the browser.
- Each leg runs in its own subshell — one leg's death cannot orphan a sibling (the M25/M34 compound-chain loss class). Exit 0 = all OK, 1 = any FAILED.
- Deep Research / Deep Think (via the `+` icon) give richer content but take much longer — run them **every other round** or on a near-converged paper, not every round.

---

## 3. Recovery playbooks

| Situation | Play |
|-----------|------|
| **Dead chat** (FAILED-dead, no verdict) | Single retry with a FRESH chat next tick; a FAILED leg is a chart GAP (`verdict:failed`), never a zero. Do not re-use a `/c/<id>`. |
| **Wrong-PDF attach** | The composer-scoped attachment-token gate (854acb99) catches mismatch/absence pre-send and re-uploads once or dies. If a wrong-attach leg still landed, discard the raw (INVALID) and re-place the leg; enumerate same-era chats + match on the `ext_<PAPER>_<ROUND>` token (titles don't disambiguate same-venue papers). |
| **Silent landing** (send landed but tab still on old `/c/`, misread as rate-limit) | Sidebar content-liveness fallback (02d68a8f) detects the review by CONTENT (a sidebar chat containing our prompt), 120s poll. After ~2 repeated "infra failures", LOOK at the page (headed read-only diagnostic) before accepting the hypothesis. |
| **Stalled adjudicator / loop stall** | Launch a FRESH agent that **audits Convex FIRST** (`externalReviews:list` + `readinessMetrics:listWaves`) to see what's already recorded, so it does NOT double-post a verdict or re-drive a landed leg. Then resume from the first unrecorded step. |
| **Concurrent driver detected** | YIELD: `harvest` + `post_verdict.sh` stay safe; do not drive the browser, do not commit a competing bundle, do not push. `git pull --rebase` before any later push. |
| **Transient Convex freshness-gate failure** | The freshness Convex read has a bounded retry (ccd593c1) — re-run the push; a single network blip no longer blocks a clean bundle. |
| **Freshness gate blocks a genuinely-non-surface commit** | `FRESHNESS_SKIP=1 git push` ONLY when the commit truly touches no surface (e.g. a docs-only/tooling commit). Never use it to push a real round bundle past a real staleness — fix the surface. |
| **Watchdog fired (loop DOWN)** | `LOOP_HEARTBEAT.json` was stale >45m; the launchd watchdog ran a headless recovery tick (fresh heartbeat + freshness fix + harvest of submitted-unharvested manifests). Check `project-context/LOOP_WATCHDOG_LOG.md` for what it did, then resume. |
| **Loop watchdog script edited** | Re-deploy the runtime copy: `cp tools/loop_watchdog.sh "$HOME/Library/Application Support/bigbounce/loop_watchdog.sh"` (launchd has no ~/Desktop TCC grant; the repo file is canonical source only). |
| **Cron tick script edited** | Re-deploy the canonical source: `cp tools/bigbounce_cron_tick.sh "$HOME/Library/Application Support/bigbounce/bigbounce-cron-tick.sh"`. The canonical tick auto-claims/renews the remote lease, stamps `machineId`, and routes non-holders to lease-free work. |

---

## 4. Troubleshooting table (symptom → cause → play)

| Symptom | Cause | Play |
|---------|-------|------|
| Manifest row banked OK but empty chat URL | pre-856 empty-URL path | fixed by 80914698 (OK now REQUIRES a non-empty URL); if seen, treat the leg as FAILED + re-place |
| Two legs point at the same `/c/` URL | ChatGPT stale pre-send URL race | 3fb1ffd9 rejects a `/c/` equal to the pre-send URL; re-place the mis-attributed legs |
| ChatGPT leg sent, then no OK/FAIL/manifest row | `set -e` swallowed a benign trailing status | fixed by a08dd750 (dispatch always terminates OK-or-FAIL); re-run the leg |
| Wrong readiness cap after a harvest | `post_verdict` selected a stale row by insertion order | fixed by cd02c991 (`_creationTime` DESC); re-run `post_verdict` |
| Rich multi-reviewer wave row overwritten to one verdict, streak zeroed | `record_wave` auto-call clobber | fixed by cd02c991 clobber-guard; `record_wave.sh` is the authoritative writer — re-post it |
| INT leg displaced the EXT cap row | reviewerLabel collision (bare "Grok") | post INT under `<wave>-INT-<vendor>` (029cb689) |
| Adjudicator recorded a verdict off a prompt-echo / 0-byte / other-paper raw | harvest label trusted before content check | substance/dup/signature gates (2f5efb53) + directive-I4 verbatim read; verdict:failed for a no-output leg |
| Corrected number still shows in the paper | value baked into a figure PNG | directive I6 — regenerate every figure that renders the value; verify by rendering the figure page (not a filename check) |
| Site banner / skills chart / board stale | surface not mirrored from Convex | `site_freshness_check.sh --report`, fix the flagged surface, re-commit (Convex is truth) |

---

*Round protocol, selectors, upload paths, dated lessons → the canonical scistack
SKILL.md. Failure-class deep-dive + shas → `project-context/PROCESS_AUDIT_2026-07-14.md`.*
