# Convex paper_versions slug convention — DO NOT use "pX" shorthand

**TL;DR**: every `client.mutation(api.paperVersions.bump, { paperSlug: ... })`
call MUST use the long-form slug (`paper-1a`, `paper-1b`, `paper-2`, `paper-3`,
`paper-4`, `paper-5`). The shorthand (`p1a`, `p1b`, `p2`, `p3`, `p4`, `p5`)
silently writes to a dead key.

## Why this matters

`convex/papers.ts:249` `listAllPaperStates` (the query that feeds the homepage
"Paper state — live from Convex" table) looks up paper_versions by
`paper.slug = "paper-X"`:

```typescript
const versions = await ctx.db
  .query("paper_versions")
  .withIndex("by_paper", (q) => q.eq("paperSlug", paper.slug))  // "paper-X"
  .collect();
```

Rows inserted with `paperSlug: "pX"` are never read by this query. They still
get stored, but they're invisible to the homepage table — which means the
"Current versions" displayed publicly drift behind reality.

## How it was found (2026-06-08)

Houston pushed back: "the website and all the papers on the website don't seem
to be updated." The papers.ts version cards + the per-paper pages were current,
but the live-Convex Paper State table at the top of the homepage was stuck
showing P1B v1B.0.40 / P3 v3.1.72 / P4 v1.0.149 / P5 v0.1.43 (versions from
weeks earlier).

Direct query of `api.paperVersions.current` with the short-form slug returned
the latest versions, but `api.papers.listAllPaperStates` returned all-stale.
The mismatch was the slug form.

## What to do

**Going forward**: every Convex `paperVersions.bump` call uses
`paperSlug: "paper-X"`. Example: `paper-1b`, NOT `p1b`.

**Existing bump scripts** in this directory (`p1b_convex_bump_v1B042.mjs`,
`p2_convex_bump_v1_7_43.mjs`, `p3_convex_bump_v3_1_73.mjs`,
`p4_convex_bump_v1_0_150.mjs`, `p4_convex_bump_v1_0_151.mjs`,
`post_loadbearing_convex_bump_2026-06-08.mjs`) are preserved as point-in-time
historical artifacts but use the buggy short form. **Do not re-run them
as-is**; if you need to redo any of those bumps, copy the script and edit
the slug to the long form first (see
`post_loadbearing_convex_bump_2026-06-08_v2.mjs` and
`p2_convex_bump_v1_7_43_correctedslug.mjs` as canonical examples).

**The `/bigbounce-bump` skill** (at
`~/.claude/scistack/astrostack/bigbounce-bump/SKILL.md`) already documents
the long-form slug as the calling convention; it is not affected by this bug.
