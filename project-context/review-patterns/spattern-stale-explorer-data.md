---
pattern_id: spattern-stale-explorer-data
status: seeded
first_seen: P1-2026-06-19
proposed_by: site-cohesion-sweep 2026-06-19
---

# spattern-stale-explorer-data — Explorer or data page shows counts/catalogs from an older run

## Defect

An interactive explorer (anomaly-explorer, galaxy-explorer, data-explorer,
visualize, or any catalog/data page) shows galaxy counts, anomaly counts,
detection statistics, or catalog entries that belong to an older analysis run
rather than the current version referenced by the paper. A reader drilling into
the explorer sees a different dataset than what the paper reports.

## How to detect

- Read the paper's canonical headline counts from SSOT (total galaxies, anomaly
  count, detection rate, etc.).
- Navigate the explorer page in a browser (headless + visual); extract the
  displayed counts/summary stats.
- Diff: any count that disagrees with the canonical record is a hit.
- Also check: does the explorer's "last updated" label or data timestamp match
  the current paper version's dataset date?

## Fix

Re-run the data pipeline to regenerate the explorer's backing JSON/Convex
records from the current catalog. Update the data-loader or the Convex table
so the explorer reflects the current paper's dataset. Coordinate with
`/bigbounce-site-sync` for the site-data update commit.
