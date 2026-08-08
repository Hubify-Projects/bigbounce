# Pattern 065 — static-site-data-staleness (Convex-live-but-static-files-stale)

**Class:** site-integrity / false-current-state
**Discovered:** 2026-06-30 (Houston caught the /reviews + /papers pages showing June-26 data after 3 rounds of work)

## Symptom

The live site shows STALE versions/dates/readiness/verdicts even though Convex
(the live DB) was updated correctly every round. The site looks current to the
operator (who checks Convex) but shows old data to the public.

## Root cause

The bigbounce Next.js site reads from BOTH Convex (live, server-component
queries) AND several **static build-time data files** that must be hand-updated
and committed:

- `site/src/data/papers.ts` — the /paper + /papers card data (version, pages, pdfMeta, PDF hrefs)
- `site/src/data/reviewTimeline.ts` — the /reviews timeline + verdict/gap/skills charts
- `site/src/data/live-status.ts` — the home header date + "Current Focus" narrative
- hardcoded prose inside `page.tsx` files (e.g. the reviews "campaign complete" panel)

Writing to Convex does NOT update these. A round that only writes Convex leaves
the static surfaces stale → the public sees old versions + old PDF links + false
"campaign complete" claims.

## The gate (prevention)

EVERY round that changes a paper or produces verdicts MUST, in the SAME commit bundle:
1. Convex mutations (paperVersions/externalReviews/activityFeed) — as before.
2. `site/src/data/papers.ts` — bump version/lastUpdated/pages/readiness/pdfMeta + repoint PDF hrefs to the new versioned pin.
3. Create the new versioned PDF pin in `site/public/papers/` (and `public/papers/`).
4. `site/src/data/reviewTimeline.ts` — add the round's timeline entry + extend externalVerdictRounds/gapSeries/skillsSeries.
5. `site/src/data/live-status.ts` — bump the date + narrative.
6. Grep for stale hardcoded prose in the relevant `page.tsx`.
7. Verify live after deploy: curl the page, assert the new version string is present and the old one is absent.

## Verify-after-deploy one-liner

```bash
curl -s https://bigbounce.hubify.app/paper | grep -c "v1A.0.89"   # new (>0)
curl -s https://bigbounce.hubify.app/paper | grep -c "v1A.0.80"   # old (==0)
```

This pattern is now a hard same-commit gate folded into /bigbounce-site-sync.
