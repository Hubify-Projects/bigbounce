# ops/ — bigbounce review-program operations center

This directory is the **canonical home for the program's architecture, plan, and
runbooks** — the map, not the territory. It **indexes and architects**; it does
**not** duplicate canonical state. Every fact about *where the papers actually
are* lives in the sources below; these docs link to them.

## What this program is

A continuous, self-improving peer-review loop that drives six bigbounce
cosmology papers (P1A/P1U, P1B, P2, P3, P4, P5) toward all-reviewer ACCEPT. Each
"wave" submits every paper's live PDF to internal API referees (Claude
subscription + OpenAI + Grok + Gemini) and external browser referees (ChatGPT +
Grok + Gemini), truth-audits every finding against a source-cited disposition
ledger, closes genuinely-new real defects with real edits/science, and syncs the
verdict grid + trajectory to the live site. The loop is autonomous (launchd cron
+ watchdog) and never idles while any verdict word is below ACCEPT.

## Where canon lives (do NOT restate it here — link to it)

| Canon | Location | Owns |
|-------|----------|------|
| Paper status | `project-context/SSOT/index.md` + `SSOT/paper-N/status.md` + `SSOT/queue.md` | readiness %, gaps, open tasks — read FIRST |
| Round protocol | `~/.claude/scistack/astrostack/bigbounce-r-round/SKILL.md` | THE R-round spec; INT/EXT flow, selectors, dated lessons |
| Dispositions | `project-context/peer-reviews/DISPOSITIONS/{P1U,P2,P3,P4,P5}.md` | every standing finding disposition + fingerprint |
| Live-site truth | Convex `brilliant-panther-471` (`externalReviews`, `readinessMetrics`, `paperVersions`, `papers`, `activityFeed`) | verdict grid, caps, trajectory — the ONLY readiness source |
| Failure-class catalog | `project-context/PROCESS_AUDIT_2026-07-14.md` | the 12-class blocker catalog + sha-cited kills |
| Directives A–M / I1–I6 | repo-root `CLAUDE.md` | the standing rules these docs operationalize |

## The four docs

- **[ARCHITECTURE.md](./ARCHITECTURE.md)** — full system architecture: component
  map (scheduling → submission → harvest → adjudication → recording → site →
  science-closure → INT → backup), one wave's data-flow with file paths at each
  step, the never-break invariants, and the concurrency model.
- **[PLAN.md](./PLAN.md)** — mission + the terminal-criteria stack (directives
  J→K→L→M), the current-state snapshot, the honest verdict-floor analysis, the
  four-phase plan, and the decision log.
- **[RUNBOOK.md](./RUNBOOK.md)** — operational procedures: the per-tick protocol,
  wave placement, recovery playbooks, and a symptom→cause→play troubleshooting
  table.

## How to use these docs

1. **"Where are we?"** → `SSOT/index.md` (never these docs, never site HTML).
2. **"How does the machine work?"** → `ARCHITECTURE.md`.
3. **"What's the plan / what's Houston-gated?"** → `PLAN.md`.
4. **"A wave broke / how do I run a tick?"** → `RUNBOOK.md`.
5. **"What's the exact round protocol / selector?"** → the scistack SKILL.md.

Never print secrets. `.env.local` is gitignored; use `/env-local-discovery`.
