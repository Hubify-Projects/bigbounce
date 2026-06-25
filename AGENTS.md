# AGENTS.md — bigbounce (Codex / any-agent entry point)

This is the **bigbounce cosmology paper-review program**: 6 physics papers driven
to publication through an iterative internal + external peer-review loop, with a
public Next.js lab site (https://bigbounce.hubify.app) kept in sync after every
round. If you are an AI coding agent (Codex, Claude Code, Cursor, …) picking this
up, read these IN ORDER before touching anything:

1. **`project-context/AGENT_ONBOARDING.md`** — the operational runbook: new-machine
   bootstrap, the R→D→P internal+external review loop, how to run one round, how to
   sync the site after every round, and the hard-won gotchas. **START HERE.**
2. **`CLAUDE.md`** — routing table + standing directives (Claude Code auto-loads it).
3. **`AGENT_RULES.md`** — the methodology bible (full spec).

## Ground truth
- Canonical paper status: **`project-context/SSOT/`** + **Convex** — never a `.tex`
  comment, `papers.ts`, or site HTML.
- ⚠️ **State as of 2026-06-21: IN-REVISION (readiness 92).** An external review
  found open BLOCKER/MAJOR/MINOR revisions. Do not claim done or submit. P0 =
  intake those findings, truth-audit, close, re-review, re-sync the site.

## The 6 papers (current paths — there is no single `main.tex`)
| # | Source .tex |
|---|---|
| P1A | `arxiv/paper1a_ech_nogo.tex` |
| P1B | `arxiv/paper1b_mcmc_companion.tex` |
| P2 | `research/focused_paper_source_integration/02_full_draft.tex` |
| P3 | `pipelines/p3_anomaly_engine/paper3_draft.tex` |
| P4 | `pipelines/p2_chirality/chirality_catalog_paper.tex` |
| P5 | `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` |

## The site
**Next.js 16 + Convex**, in `site/` (deploys from `main` via Vercel). The old
static HTML is deprecated under `/old/`. Source of site data: `site/src/data/`
(`papers.ts`, `live-status.ts`, `reviewTimeline.ts`). The site reads paper
readiness live from Convex.

## Non-negotiables (full list in CLAUDE.md / AGENT_RULES.md / the agent memory dir)
- Truth-audit every review finding BEFORE closing it. Never fabricate a derivation.
- Update the live site (`reviewTimeline.ts` + `papers.ts` + SSOT + Convex) in the
  SAME COMMIT as every review round. Deploy = `git push origin main`.
- The auto-commit cron commits locally but does NOT push — push manually.
- Convex: the site reads the deployment in `NEXT_PUBLIC_CONVEX_URL`; change live
  state via `npx convex dev --once`, not `npx convex deploy`.
- Skills live in `~/.claude/scistack/` (clone `Hubify-Projects/scistack`, run
  `bin/sync-to-claude.sh`). Secrets: `cp .env.example .env.local` and fill in.

## Research tooling
Multi-model research helpers live in `research/` + `tools/` (the review engine is
`tools/v3_native_pdf_review.py`; literature/data/reasoning helpers in
`research/`). API keys load from `.env.local`. See `AGENT_ONBOARDING.md` §2.

The site is the scoreboard. Keep it honest and current after every round.
