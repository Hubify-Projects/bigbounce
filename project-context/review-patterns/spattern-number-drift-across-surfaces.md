---
pattern_id: spattern-number-drift-across-surfaces
status: seeded
first_seen: P1-2026-06-19
proposed_by: site-cohesion-sweep 2026-06-19
---

# spattern-number-drift-across-surfaces — Headline numbers disagree across site surfaces

## Defect

A key quantitative claim (significance, galaxy count, detection rate, anomaly
count, figure count, readiness percentage) is shown on multiple site surfaces
(paper detail page, papers list card, home dashboard, figures page, reviews page)
but the values disagree. One surface was updated after a paper bump and another
was not. A reader compares two pages and sees contradictory numbers.

## How to detect

- Extract the paper's canonical headline numbers from SSOT / `papers.ts`.
- Scrape each surface that displays numbers for this paper (detail, list, home,
  figures, reviews/timeline, explorer) and build a per-surface value table.
- Any surface with a value that differs from canonical (or from another surface)
  is a hit. Even a 0.1σ discrepancy counts.

## Fix

All site surfaces read from a single source: `papers.ts` / `live-status.ts` /
Convex. If numbers disagree it means one surface hard-codes a value instead of
reading from data. Find the hard-coded value, replace with the canonical data
reference, and update `papers.ts` to the current numbers. Single-commit fix
per `feedback_post_bump_full_sync`.
