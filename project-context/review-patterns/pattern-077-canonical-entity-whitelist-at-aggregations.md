# Pattern 077 — Canonical-entity whitelist at every aggregation point

**Class:** data-hygiene
**First observed:** 2026-07-23 ("7/8 papers" from junk doc-id rows + retired P1U + stale P1B exclusion)

## Observation
The ETA aggregation counted raw Convex document ids and the retired P1U as
papers while excluding P1B under reversed merge-era logic — producing "7/8
papers at the bar" directly above "the six papers," a reader-facing
contradiction assembled entirely from stale plumbing.

## Rule
Every aggregation that enumerates program entities (papers, legs, waves) must
filter through the canonical whitelist (P1A/P1B/P2/P3/P4/P5) at the point of
aggregation — not trust upstream rows. Retiring or un-merging an entity
requires a same-day sweep of every hardcoded inclusion/exclusion set
(grep for the entity id across convex/ and site/src).
