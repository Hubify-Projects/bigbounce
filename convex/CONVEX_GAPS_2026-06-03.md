# Convex schema/query gaps — 2026-06-03

Audit follow-up to the site/API sweep landed in commit `5b57a60d`. Five gaps
surfaced at the Convex layer; three were closed in this commit and two are
flagged for Houston with proposed schema migrations below.

## Closed in this commit

### Gap #2 — `novelty` field on `papers` (CLOSED, schema-only)

`/never-claim-n4` standing directive requires every paper to self-cap at
N1/N2/N3. Convex had no field for it, so the cap lived only in review
prompts and was easy to miss.

Schema change (`convex/schema.ts`):

```ts
novelty: v.optional(v.union(
  v.literal("N1"),
  v.literal("N2"),
  v.literal("N3")
)),
```

The enum **rejects N4 at the database layer** — a stray
`setNovelty(slug=p1a, novelty="N4")` is impossible to commit because the
union literal does not include N4. Documented in
`project-context/SSOT/novelty-tiers.md`.

New mutation `papers:setNovelty(slug, novelty)` lets Houston pick the tier
per-paper. The detail page (`site/src/app/papers/[slug]/page.tsx`) renders
a `Novelty: N3` chip next to the focus areas heading when set.

**Not populated yet** — all six papers leave `novelty` null until Houston
picks. Proposed defaults (commit body — Houston flips):

| Paper | Proposed | Rationale |
|------|----------|-----------|
| P1A  | N3 | First-of-kind ECH no-go structure |
| P1B  | N2 | MCMC companion methodology paper |
| P2   | N3 | First f_NL forecast from this technique |
| P3   | N3 | First systematic multi-survey anomaly engine |
| P4   | N3 | Largest galaxy chirality catalog to date |
| P5   | N3 | First end-to-end DESI environmental dependence test |

### Gap #3 — `papers:getPaperState` sort tiebreaker bug (CLOSED)

`getPaperState` sorted versions by `datestamp.localeCompare` only.
When P1B bumped v1B.0.40 → v1B.0.41 on the same day, the page detail
view picked v1B.0.40 (arbitrary tie-break) while the dashboard (which uses
`listAllPaperStates`, already fixed) correctly picked v1B.0.41.

Fix: mirror the `listAllPaperStates` tiebreaker (createdAt desc) into both
`getPaperState` AND `getExternalReviewPrompt` (same bug in both):

```ts
versions.sort((a, b) => {
  const d = b.datestamp.localeCompare(a.datestamp);
  if (d !== 0) return d;
  return (b.createdAt ?? 0) - (a.createdAt ?? 0);
});
```

### Gap #4 — Detail page `focusAreas` hardcoded (CLOSED)

`papers.focusAreas` already existed in Convex but the detail page
hardcoded a `focus: Record<string, string[]>` block at L327. Drift waiting
to happen.

Fix:
- `papers:listAllPaperStates` now returns `focusAreas` (and `novelty`).
- `site/src/lib/livePapers.ts` `LivePaperState` type extended.
- `site/src/app/papers/[slug]/page.tsx` renders a new `Focus areas` card
  driven by `live?.focusAreas`. The old hardcoded `focus` object is gone.
  `ExternalReviewPanel` now receives the same `focusAreas` array — single
  source of truth.

## Documented for Houston (not closed)

### Gap #1 — No `notables` or `externalReviews` tables

Each paper has informal "notable results" bullets + external-review
metadata (referee report source, dates, severity counts) that currently
live in `project-context/peer-reviews/` markdown and `papers.ts` static
arrays. Suggest a schema migration:

```ts
// Per-paper short-form bullet items surfaced on the detail page
// (e.g. "1.7% f_CW formally excluded at ~18σ block-bootstrap"). Distinct
// from focusAreas (which target reviewers) — these are reader-facing.
papers_notables: defineTable({
  paperSlug: v.string(),
  ordinal: v.number(),                // display order
  bullet: v.string(),                 // short rendered string (supports MathText)
  citationKey: v.optional(v.string()), // FK to a future citations table
  createdAt: v.number(),
}).index("by_paper", ["paperSlug", "ordinal"]),

// External referee reports (Houston paste-in, ArXiv referees, journal
// referees). Distinct from r_rounds (which is for direct-vendor adversarial
// review). One row per report.
papers_externalReviews: defineTable({
  paperSlug: v.string(),
  source: v.union(
    v.literal("journal-referee"),
    v.literal("arxiv-endorser"),
    v.literal("houston-external-paste"),   // copy/paste from ChatGPT/Gemini etc
    v.literal("colleague-private")
  ),
  reviewerLabel: v.string(),               // e.g. "MNRAS referee #1" or "Gemini-2.5-pro paste"
  receivedAt: v.string(),                  // ISO date
  recommendation: v.optional(v.union(
    v.literal("ACCEPT"),
    v.literal("MINOR-REVISIONS"),
    v.literal("MAJOR-REVISIONS"),
    v.literal("REJECT")
  )),
  // Severity counts as reported by the reviewer (independent of our
  // truth-audit reclassification).
  blockerCount: v.number(),
  majorCount: v.number(),
  minorCount: v.number(),
  reportText: v.optional(v.string()),
  reportLink: v.optional(v.string()),      // GitHub/Drive link to full report
  associatedRoundId: v.optional(v.id("r_rounds")),  // when paste was processed via /cross-vendor-r-round
})
  .index("by_paper", ["paperSlug", "receivedAt"])
  .index("by_source", ["source", "receivedAt"]),
```

Populating these will require a one-shot seed script reading
`project-context/peer-reviews/findings-archive/` and the per-round
synthesis MDs. Roughly 30+ external reports across the six papers.

### Gap #5 — `papers.sitePdfPath` not atomically updated with `paperVersions:bump`

When the version bumps but `sitePdfPath` doesn't update in the same Convex
transaction, the detail page can show the new version chip with a stale
PDF link until a follow-up `papers:upsert` lands. This is the same class
of drift /bigbounce-bump exists to prevent at the workflow level — moving
it into the mutation closes it at the storage layer.

Proposed: extend the existing `paper_versions:bump` mutation
(in `convex/paperVersions.ts`) to accept an **optional** `sitePdfPath`
argument and patch `papers.sitePdfPath` in the same handler:

```ts
// inside paperVersions.bump handler, after inserting the new version row:
if (args.sitePdfPath && args.sitePdfPath !== paper.sitePdfPath) {
  await ctx.db.patch(paper._id, { sitePdfPath: args.sitePdfPath });
}
```

This is non-breaking (existing callers that don't pass `sitePdfPath`
behave as before). The /bigbounce-bump skill should be updated to always
pass the new path.

## Verification

- `npx convex dev --once` — passes (schema valid, functions compile).
- `cd site && npm run build` — passes (53/53 static pages, TypeScript clean).
- N4 rejection: enum literally doesn't admit it. No runtime test needed —
  the type system + Convex schema validator both reject `novelty: "N4"`
  before it reaches the handler.

## Files touched

- `convex/schema.ts` — added `papers.novelty` field
- `convex/papers.ts` — added `setNovelty` mutation; surfaced
  `focusAreas` + `novelty` in `listAllPaperStates`; fixed sort tiebreaker
  in `getPaperState` and `getExternalReviewPrompt`
- `site/src/lib/livePapers.ts` — extended `LivePaperState` type, plumbed
  the two new fields through the Convex fetch + static fallback
- `site/src/app/papers/[slug]/page.tsx` — replaced hardcoded `focus`
  object with Convex-driven `Focus areas` card + novelty chip
- `convex/CONVEX_GAPS_2026-06-03.md` — this doc
