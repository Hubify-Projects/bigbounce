# BigBounce Source-of-Truth Contract

**Date:** 2026-06-16
**Status:** Active context contract for agents working on BigBounce-adjacent automation.
**Trigger:** Houston clarified that Hubify app research data is out of date; current BigBounce research has been happening directly in the `bigbounce` repo and on `bigbounce.hubify.app`.

## Contract

Current BigBounce research truth lives in:

1. The local repository at `/Users/houstongolden/Desktop/CODE_2025/bigbounce`.
2. The BigBounce SSOT files under `project-context/SSOT/`.
3. The canonical paper sources and generated artifacts tracked by the BigBounce repo.
4. The public BigBounce site at `https://bigbounce.hubify.app` as the current reader-facing mirror/status surface.

Do not use Hubify app/CLI lab data as BigBounce research truth unless a future task explicitly refreshes or syncs that surface from the BigBounce repo. The current authenticated Hubify CLI lab is `Local-LLM` (`local-llm`) and is empty; that is a tooling/auth check, not BigBounce status.

## Source Hierarchy

| Tier | Surface | Role | Conflict rule |
|---|---|---|---|
| 1 | `project-context/SSOT/index.md`, `project-context/SSOT/paper-N/status.md`, `project-context/SSOT/queue.md` | Operational research status, readiness, gates, queue rows, paper-by-paper state. | Wins over all downstream mirrors. If stale against observed repo state, fix the SSOT in the same scoped commit. |
| 2 | Canonical paper sources and reproducibility artifacts in the repo | Claims, numbers, versions, figures, scripts, PDFs, tarballs. | Wins for claim verification. Update SSOT and mirrors when this changes. |
| 3 | `site/src/data/live-status.ts`, `site/src/data/papers.ts`, review timeline data, site public artifacts | BigBounce site build inputs and public status mirror. | Must mirror SSOT/source state. If site data differs from SSOT/source, treat as drift to repair. |
| 4 | `https://bigbounce.hubify.app` | Current public surface Houston and readers inspect. | Use as the live public mirror and QA target, not as the authoring source for paper claims. |
| Excluded | Hubify app/CLI lab data such as `hubify status`, `hubify lab info`, `hubify labs` | Tooling/integration candidate only. | Never infer BigBounce research status from this until an explicit BigBounce-to-Hubify refresh/sync is designed and verified. |

## Current Live Check

Checked on 2026-06-16:

- `https://bigbounce.hubify.app` returned HTTP 200 from Vercel.
- The public site response was last modified on 2026-06-16 and rendered the BigBounce research app.
- The public site displayed a live status banner and paper table, including the June 14, 2026 status snapshot and paper readiness rows.
- This public site surface is BigBounce-owned and distinct from the stale Hubify app lab data exposed by the authenticated `hubify` CLI.

## Agent Rules

- Before any paper, site-status, review, arXiv, or research-node work, read `CLAUDE.md`, `AGENTS.md`, `project-context/SSOT/README.md`, `project-context/SSOT/index.md`, the relevant `paper-N/status.md`, and `project-context/SSOT/queue.md`.
- For paper claims, never rely on Hubify app lab rows, `hubify status`, or the empty `Local-LLM` lab.
- For public-site QA, use `bigbounce.hubify.app` plus the local `site/` source files.
- For source-of-truth updates, commit SSOT, paper/source artifacts, and site mirror updates together when the work changes research status.
- For mobile/SMS/You.md/h.computer research-node ideas, route inbound notes to proposals first. They may reference BigBounce SSOT state, but they must not mutate papers, launch pods, publish artifacts, or update external services without the existing BigBounce approval gates.

## Practical Routing

| Ask | Read first | Allowed output |
|---|---|---|
| "What is current BigBounce status?" | `project-context/SSOT/index.md`, `site/src/data/live-status.ts`, `https://bigbounce.hubify.app/status` | A status summary that names whether it came from repo SSOT, site mirror, or both. |
| "Update the public site" | SSOT plus `site/src/data/*` | Same-commit site data/source update, then visual/public QA. |
| "Create h.computer research-node status cards" | This contract, SSOT, You.md/h.computer context | Proposal or read-only status hook sourced from BigBounce SSOT/site, not Hubify app lab data. |
| "Sync BigBounce into Hubify" | This contract plus explicit Houston approval | A separate sync plan with one-way source mapping from BigBounce repo/site into Hubify, never silent inference from stale app state. |

## Non-Goals

- This note does not update scientific claims.
- This note does not refresh Hubify app/lab research data.
- This note does not authorize any paper edits, pod work, arXiv submission, or external write.
- This note does not change the SSOT protocol; it clarifies the boundary between current BigBounce research surfaces and stale Hubify app data.
