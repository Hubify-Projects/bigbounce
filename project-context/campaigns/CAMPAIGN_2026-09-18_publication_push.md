# Goal plan: BigBounce publication push — every paper to its maximum agent-reachable readiness, site synced, live monitoring

**Opened:** 2026-09-18 22:40 PT · **Campaign director:** Claude Code session `code-you-2d` (Fable 5.1) · **Repo:** `Hubify-Projects/bigbounce` main (single checkout, 77 GB; no worktrees) · **Lab lease:** `code-you-2d-MacBookAir24GB`, 240-min TTL, renewed by the monitor lane.
**Authorization (Houston, 2026-09-18):** "launch multiple new sessions with dedicated lanes to continue progressing and monitoring to ensure we keep all researching moving forward full steam ahead towards 95-100% publication ready and update the bigbounce.hubify.app site and everything too both new and old and current in progress". Houston also asked that lane sessions appear as named Claude Code sessions.

## Acceptance

Readiness semantics (Directive-P, `SSOT/queue.md`): **95 = every agent gate done; 100 only via Houston's literal `APPROVE`; there is no 96.** So the campaign's job is to (a) put every non-frozen paper at 95 with a fresh exact-version confirmation, (b) advance pre-R papers through their permitted rounds, (c) do the decided science that unblocks stopped papers, (d) deliver Houston one sign-off packet per paper, and (e) keep every public surface truthful.

| # | Criterion | Evidence |
|---|---|---|
| A1′ | P4′ (P4P) v4P.0.7 exact-version INT confirmation board (P4/P5 standalone are superseded per lineage) run, truth-audited, 0 genuinely-new-real open; SSOT + Convex + site updated same commit | Evidence: `SSOT/paper-4p/status.md` confirm row; Convex `externalReviews` rows; `git log` |
| A2′ | A3M (Track A flagship) R9 exact-v3M.0.24 INT board run, truth-audited, real items closed, version bumped with directive-G hygiene; R2 stop lifted because ledger row 19 is CLOSED | Evidence: `SSOT/paper-a3m/status.md`; `research/track_a3_multichannel/paper/main.tex` version; served PDF md5 == Convex md5 |
| A3 | P-SU R2 (the one permitted board, D-PSU-1) run + closed; decision recorded CLOSED/OPEN | Evidence: `SSOT/paper-su/status.md` |
| A4 | P1N D-round (design/visual) and P-round (packaging: arXiv tarball standalone-compiled, mirrors md5-matched, artifact links resolve) complete; cap raised only by real ladder stage | Evidence: `SSOT/paper-1n/status.md`; tarball under `SSOT/arxiv_tarballs/`; `/latex-audit` + `/artifact-link-verify` output |
| A5 | DROPPED — merge already landed as P1N (PAPER_LINEAGE_2026-08-05 §a) | Evidence: lineage file |
| A6 | DROPPED — ledger #19 CLOSED 2026-09-04 (D-A3-14, `research/track_a3_multichannel/row19_lambda/`) | Evidence: ledger row 19 |
| A7 | Anomaly flagship: defended selected sample + validation contract + taxonomy + named follow-up set + manuscript skeleton assembled from the completed phase-3-v2 landing | Evidence: `project-context/PHASE3_V2_LANDING_2026-09-03.md` successor doc; `pipelines/p1_highz_tracers/` artifacts; draft `.tex` |
| A8 | Site truthfulness: A3M readiness inconsistency (75 vs ~95) reconciled to Convex; papers.ts/live-status.ts/reviewTimeline.ts/SSOT index top board/repro manifests match Convex for all 11 blocks; `/reviews`, `/research`, `/publish`, `/timeline`, `/learn` reflect this campaign; freshness gate PASS; deployed URLs curl 200 and show the new state | Evidence: `tools/site_freshness_check.sh --report` PASS; watcher curl log; commit hashes |
| A9 | One Houston sign-off packet per 95-paper (P2, P1A, P4, P1B, P5) refreshed to current hashes, plus the exact list of Houston-only actions | Evidence: `project-context/HOUSTON_SIGNOFF_PACKET_2026-09-19.md` |
| A10 | Live monitoring: campaign board updated on every lane transition; disk-free and lease heartbeats every 15 min; Hubify lab tasks per lane; activity-feed event on open and close | Evidence: `## Log` below; `hubify tasks`; Convex activityFeed |

## Sequence

1. Director: plan (this file), lease, peer discovery (session `bigbounce-aa` messaged 22:38 PT), spawn lanes as named `claude -p` sessions, Hubify tasks, activity event.
2. Lanes L1–L6 run in parallel (isolated files, see below). Only shared writes: `site/src/data/{papers,live-status,reviewTimeline}.ts`, `SSOT/index.md`, `SSOT/queue.md` — each lane edits only its own paper's block/rows, re-reads before each edit, `git add` explicit paths only, never `-A`.
3. L7 site lane runs continuously, integrating after each lane's commit; it is the only lane allowed to touch nav, `/reviews`, `/publish`, `/research` pages.
4. Monitor lane renews the lease, watches disk, checks lane liveness, appends heartbeats here.
5. Director reviews each lane's report against its criterion, dispositions it, pushes (freshness gate must PASS), verifies deployed URLs, closes.

## Parallel lanes (corrected 22:55 PT after lineage check — PAPER_LINEAGE_2026-08-05.md: P1A→P1N merge already landed; P5 folded into P4′; P2′ Letter folded into A3M 2026-09-02; ledger #19 already CLOSED)

| Lane | Session name | Model | Owns (exclusive writes) | Criterion |
|---|---|---|---|---|
| L1 | bb-L1-a3m-r9 | opus (+1 Fable sub-agent for the flagship referee/adjudication leg) | `research/track_a3_multichannel/paper/`, `SSOT/paper-a3m`, A3M Convex rows, A3M PDF mirrors | A2′: A3M R9 exact-v3M.0.24 INT board run now that row 19 is CLOSED (the R2 stop condition is met); truth-audit; close real items; bump; directive-G |
| L2 | bb-L2-psu-r2 | sonnet (opus sub-agent for truth-audit) | `arxiv/paper_su_criterion/`, `SSOT/paper-su` | A3: the one permitted R2 board (D-PSU-1) on exact v1S.0.8; then decision CLOSED/OPEN |
| L3 | bb-L3-p1n-dp | sonnet | `arxiv/paper1bc_ech_note/`, `SSOT/paper-1n`, its tarball | A4: D-round + P-round on v1N.0.5 |
| L4 | bb-L4-p4p-confirm | sonnet (opus sub-agent for truth-audit) | `pipelines/p4prime_chirality_test/paper/`, `SSOT/paper-4p` | A1′: exact-v4P.0.7 INT confirmation board + packaging check for Houston sign-off |
| L5 | bb-L5-anomaly-flagship | opus | `pipelines/p1_highz_tracers/` (new subdirs only), new flagship draft dir | A7 |
| L6 | bb-L6-signoff-packets | sonnet | `project-context/HOUSTON_SIGNOFF_PACKET_2026-09-19.md` | A9 (must present the lineage reconciliation: which of P2/P1A/P4/P1B/P5 are still sign-off candidates vs superseded by P1N/P4P/A3M — Houston's call, stated plainly) |
| L7 | bb-L7-site-sync | sonnet | `site/**`, `index.html`/old static pages, stale SSOT "current section" headers for paper-a3m/su/1n/2l (versions vs tex), `SSOT/index.md` top board, freshness gate | A8 |
| LM | bb-LM-monitor | haiku | this file's `## Log` (append only), lease renew, disk watch, lane liveness | A10 |

Dropped: P1C→P1A merge (already landed as P1N), P2L R1 (archived into A3M), ledger #19 derivation (CLOSED 2026-09-04, `research/track_a3_multichannel/row19_lambda/`), P4/P5 standalone confirms (superseded by P4P).
Concurrency caps: Fable ≤1 (inside L1), Opus ≤2 (L1, L5), Sonnet unbounded, Haiku watcher.
## Closure

Campaign closes when every A-criterion has its evidence line in the log, origin/main == local, freshness gate PASS, deployed site verified, lease released, Hubify tasks moved to review/done, and a closing activity-feed event posted. Houston-only residue (APPROVE ×5, arXiv endorsement D4, ORCID D5, journal portal clicks) is listed in the sign-off packet, not carried as agent work.

## Log
- 2026-09-18 22:40 PT · director · plan written; lease claimed; Hubify campaign task created; peer session bigbounce-aa queried

- 2026-09-18 22:55 PT · director · lineage check corrected the lane table (see Parallel lanes); peer bigbounce-aa confirmed idle/no ownership; spawning lanes as named `claude -p` sessions, logs in ~/.claude/state/bb-campaign-2026-09-18/
