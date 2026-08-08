---
pattern_id: spattern-stale-version-on-surface
status: seeded
first_seen: P1-2026-06-19
proposed_by: site-cohesion-sweep 2026-06-19
---

# spattern-stale-version-on-surface — Site surface shows an older paper version

## Defect

A site surface (paper detail page, papers list, home dashboard, figures page,
reviews/timeline, or explorer) displays a version string, headline number,
readiness percentage, or status label that belongs to an older version of the
paper rather than the canonical record in SSOT / `papers.ts` / Convex. Readers
see stale data even though the paper has been bumped.

## How to detect

- Load SSOT `paper-N/status.md` + `papers.ts` / `live-status.ts` to get the
  canonical `version`, `readiness`, and headline numbers.
- Fetch each site surface (detail page, list card, home blurb, explorer entry)
  and grep for the version string and key numbers.
- Any surface that disagrees with canonical → VERIFIED finding.

## Fix

Update `site/src/data/papers.ts` and `live-status.ts` to the current version +
numbers. Sync SSOT/index.md in the same commit per the post-bump full-sync
standing directive (`feedback_post_bump_full_sync`).
