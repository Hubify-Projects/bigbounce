# Publish-Drive Handoff Prompt — 2026-08-11

Paste the prompt in the block below into a **new Claude Code session** at
`~/Desktop/CODE_YOU/bigbounce`. It is self-contained: it syncs main, creates a
branch, makes the session define an explicit goal contract, and drives every
remaining agent-side work stream until the whole program is publish-ready on
the site, with only Houston-gated clicks left.

---

```
You are the BigBounce publish-drive orchestrator (Fable 5 / Opus). Your mission:
drive ALL remaining agent-side research, review, packaging, and site work to
publish-ready, so the only remaining items are Houston-gated (sign-offs,
endorsement emails, portal submit clicks).

STEP 0 — SYNC (do first, no exceptions):
- git checkout main && git pull origin main (origin = Hubify-Projects/bigbounce;
  ignore the broken `upstream` remote). Verify clean tree, 0 ahead/behind.
- Create working branch: git checkout -b publish-drive/2026-08 (push it and
  merge back to main at every coherent milestone — other machines sync via main;
  never let this branch drift more than a day from main).
- Verify loop infra: no stale crons fighting you; check for concurrent drivers
  (recent commits, changing files) before driving anything.

STEP 1 — LOAD CONTEXT (read in this exact order, before any work):
1. CLAUDE.md (all standing directives — N, M-AMENDED, P, Q, G, I4, J/K/L history)
2. ops/PLAN.md, then project-context/PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md
3. project-context/paper_registry.json
4. project-context/SSOT/index.md (top visible board only), SSOT/queue.md
5. Per-paper SSOT/paper-*/status.md for anything you touch
6. project-context/prompts.md (last ~10 entries) + project-context/tasks.md

STEP 2 — CREATE THE GOAL (explicit, before executing):
Define a goal contract and record it in BOTH the task tracker (TaskCreate: one
parent goal + one task per work stream below) AND a new section at the top of
project-context/SSOT/queue.md titled "Publish-drive goal 2026-08". Terminal
criterion: every work stream below shows DONE with cited evidence, the site
(bigbounce.hubify.app) truthfully shows the current state of every program, and
the remaining-items list contains ONLY Houston-gated actions, each with a ready
packet. Commit the goal contract before starting execution.

STEP 3 — WORK STREAMS (run in parallel with subagents; never idle):

A. AUG-011 ANOMALY FLAGSHIP (highest science value):
   Check RunPod pod tc291bka0r6fl3 (ssh -p 1349 root@193.183.22.56) — the
   36,634-group full scan started 2026-08-05 09:43Z at ~12 groups/min (~2 days
   ETA), so it should be COMPLETE. Harvest: verify-receipts →
   summarize-after-dedup → compare-generations → commit receipts + summary.
   /backup-3plus before anything destructive (local + HF
   bamfai/bigbounce-aug-011-clean-rerun + B2 aug-011-clean-rerun/). Then
   flagship phase 3: build the defensible selected sample + taxonomy, integrate
   with the P3 support release (v3.2.0-r17), and draft the flagship results
   section. If the pod died mid-scan, reconcile fail-closed from receipts
   (protocol proven 2026-08-05) and resume. Stop the pod ONLY after
   backup-3plus passes; per-hour cost is $0.17 so never panic-terminate.

B. P1C NO-GO SURVEY (arxiv/paper1c_nogo_survey/main.tex, v1C.0.16, R13 closed):
   Continue the R-round ladder per /bigbounce-r-round until 0 genuinely-new-real
   findings across active legs (Grok API + Gemini API + Claude Opus INT
   subagent; Codex/OpenAI stays PAUSED per directive N). Then D-round
   (/paper-design-round), P-round (/paper-packaging-round), registry + SSOT +
   Convex sync, target readiness 95. Every finding truth-audited source-cited;
   never fake an ACCEPT.

C. SIX-CANDIDATE FINAL-HASH CONFIRMATION (bounded, per SSOT):
   P1A/P1B/P2/P4/P5 + P3-support sit at 95 with post-board closures in the
   current PDFs. Run ONE bounded final-hash confirmation pass (exact SHA-256
   bound PDFs, active legs only). Genuinely-new-real regressions get closed and
   re-confirmed; re-flags/disclosed limitations get source-cited dispositions.
   This does NOT reopen an unbounded loop.

D. SITE + CONVEX TRUTH SYNC (every milestone, same commit bundle):
   Convex (brilliant-panther-471) is the live site: paperVersions / rRounds /
   externalReviews / readinessCap / activityFeed per /bigbounce-site-sync.
   Directive-G PDF hygiene on every paper change (version bump, recompile 0
   undef-refs, /latex-audit, byte-identical mirrors, 3-way md5). Timeline entry
   in site/src/data/reviewTimeline.ts for every round. After each site update:
   headed-browser visual QA of bigbounce.hubify.app (overview, papers, reviews,
   status, data-explorer) — fix stale/broken before calling done.

E. REPRODUCIBILITY MANIFESTS (directive Q2):
   Every program and every compute run (incl. AUG-011) gets a manifest: data
   sources + links, scripts, compute venue + cost, wall-clock. The lab is the
   flagship reproducible lab for Hubify. Q1: no mistake-narration in anything
   published — pure contributions only; process history stays in SSOT.

F. HOUSTON PACKET REFRESH (last step of each stream):
   Keep HOUSTON_VISUAL_REVIEW_PACKETS + the sign-off board current so Houston
   can walk P2 → P1A → P4 → P1B → P5 (that order) and say APPROVE per paper
   (95→100 only via his quote; /readiness-cap-99 spirit). Keep endorsement
   email drafts (codes: gr-qc HYEJ7S / astro-ph.IM L8TIPN→P1B / astro-ph.CO
   LRZHC4 / astro-ph.GA CLVMAQ) and CQG/JORS/PRD/ApJS/AJ portal kits current.
   Publishing-phase items never subtract from readiness (directive P).

OPERATING RULES:
- Model routing: you (Fable 5/Opus) orchestrate + judge; Sonnet subagents for
  bounded execution (edits, recompiles, mirrors, packaging, sweeps); Haiku for
  polling/watchers. Fan out parallel subagents per independent stream.
- Log every Houston message via /prompt-history BEFORE acting on it.
- Commit style: atomic, bisected, autonomous (no permission-asking); push +
  merge to main at every coherent milestone so all machines stay in sync.
- Integrity absolute: never fabricate, never fake a verdict, every review leg
  saves raw output before any verdict is recorded, no readiness uplift without
  current exact-artifact evidence.
- Never idle; if a stream blocks (e.g. pod unreachable), record the blocker
  with evidence and advance the other streams.
- End every response with Best Next Steps + the continue hook.

EXIT: post a final report mapping each work stream to its evidence (commits,
receipts, Convex rows, site URLs), and a short Houston-only checklist of the
remaining human clicks. Then keep a light verification loop until Houston
responds.
```

---

**Provenance:** Written at session close 2026-08-11 after full sync verification
(local main == origin/main, no open PRs, no unmerged branches, bigbounce-lab
also clean/synced). State basis: SSOT board 2026-08-03 (six candidates at 95),
queue.md 2026-08-05 (AUG-011 scan running), P1C R13 closed at v1C.0.16
(commits `2d445855`…`09ce16c9`).
