---
name: bigbounce-site-sync
version: 0.1.0
description: |
  Dual sync of bigbounce HTML pages (index.html, paper.html, activity.html,
  data-explorer.html, explained.html, glossary.html, figures.html, etc.) AND the
  Next.js site/ subdirectory. Both must update in same commit as SSOT — never as
  follow-up. Site staleness ≥20 fires = red flag.
triggers:
  - update the site
  - sync the website
  - bigbounce site sync
---

# /bigbounce-site-sync — root HTML + Next.js dual sync

**Source:** CLAUDE.md "WEBSITE SYNC PROTOCOL"; AGENT_RULES.md §5.3-5.4; `feedback_website_sync.md`; `feedback_site_sync_same_commit.md`; `project_site_routing.md`
**Scope:** bigbounce-only
**Trigger:** any paper result, MCMC chain, figure, version, or branch state change

## What this skill does

Updates every public-facing page when bigbounce state changes. Houston tracks progress via the site, not the terminal — site staleness vs SSOT is how he loses orientation. Site update must commit ATOMICALLY with SSOT (`/ssot-update`).

## Affected page map

| Change | Pages to update |
|--------|-----------------|
| New experiment result | `index.html`, `activity.html`, `data-explorer.html`, `paper.html` if relevant |
| New MCMC chain | `data-explorer.html`, `paper.html`, status surfaces |
| New figure | `figures.html`, `index.html` if hero, `paper.html` |
| Paper version change | `paper.html`, `index.html` stat cards, `activity.html` entry |
| Branch open/close | `activity.html`, `index.html` if barrier/result count changes, `research/project_master_dossier/index.html` |
| Glossary / equation change | `glossary.html` |
| Barrier/result count | `index.html` stat cards, `research/project_master_dossier/index.html` |
| Quantitative claim change | grep + sweep every HTML page |

## Next.js mirror

The Next.js site lives at `site/` and is the new default at root per `project_site_routing.md` (2026-05-01). Legacy static HTML moved to `/old`. Every site-sync MUST hit the Next.js site primarily:

- `site/src/app/*/page.tsx` — Next.js pages
- `site/public/papers/*.pdf` — Next.js-served PDFs

If a change appears in `index.html` but not in `site/src/app/page.tsx`, the site is broken on the new default.

## Quick-sync trigger phrases

Houston commonly says:
- "update the site"
- "sync the website"
- "update the paper"

When you hear these, this skill is the answer.

## How to apply

1. **Identify what changed**: which numbers/figures/claims moved? `git diff HEAD~1` if just landed.
2. **Grep every HTML page** for the old number:
   ```bash
   grep -rn "<old-number>" --include="*.html" --include="*.tsx"
   ```
3. **Update each hit** to the new value.
4. **Update activity.html**: add a new timeline entry at the top with color (green=positive, red=closed, blue=active).
5. **Update Next.js mirror** in `site/src/app/...`.
6. **Commit + push** in same commit as the SSOT update — Vercel auto-deploys.

## Hard gates

- [ ] Every page showing the changed number is updated in the SAME commit as SSOT
- [ ] Both legacy `*.html` AND `site/src/app/*.tsx` updated
- [ ] Activity feed gets a new entry (chronological, top of list)
- [ ] Stat cards on index.html match SSOT/index.md
- [ ] Vercel deploy succeeds (check after push)

## Anti-patterns

- "I'll do the site update in a follow-up commit" → NO, Houston has flagged this repeatedly
- Updating root HTML but forgetting Next.js → site is broken on the new default
- Forgetting `activity.html` → no trail of what changed

## Related
- /ssot-update — must commit in same commit
- /readiness-cap-99 — % constraint on stat cards
- /never-flip-prod-unverified — visual verification before vercel.json edits
- /bigbounce-version-bump — version metadata cascade
- /bigbounce-claims-table-sync — sweep quantitative claims
