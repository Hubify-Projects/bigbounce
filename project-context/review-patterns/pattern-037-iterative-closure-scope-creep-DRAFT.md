---
pattern_id: 037
status: draft
first_seen: external_v1.0.149_P4 (2026-06-04)
papers_observed: [P4, P3]
finding_count: 3
proposed_by: r-round-pattern-mine 2026-06-04
promotion_candidate: false
---

# Pattern 037 — Iterative-closure scope creep (paper grows past target scope)

## Root cause

Each R-round closure adds a paragraph, table, or subsection to address a finding. Nothing is ever restructured or removed. After N rounds the paper is **N × (avg-closure-size)** pages longer than it started. Reviewers eventually flag the paper as "too comprehensive" or "too long", and the paper fails journal editorial gates on length grounds.

## Canonical instance

P4 "Galaxy Chirality Catalog": started as ~20 pages (v1.0.75, 2026-05-15), grew to 57 pages (v1.0.151, 2026-06-04) across 151 versions and ~25 R-rounds. ChatGPT-REJECT M9 + Grok-MAJOR both flagged "Shorten and restructure. Supplement = null batteries, derivations, version history." The same closure loop that hardened the science grew the paper past PRD/MNRAS editorial norms (~20–35pp typical).

P3 "Multi-Survey Anomaly Catalog": similarly grew from ~20pp to 50pp (v3.1.73) across 73+ versions.

## Detection rule

```bash
# In /paper-pre-review-check — run before every external submission
pages=$(pdfinfo "$PDF" 2>/dev/null | grep Pages | awk '{print $2}')
if [ "$pages" -gt 40 ]; then
  echo "WARN: $PDF is $pages pages — exceeds P90 for astro-ph (40pp). Review appendix restructure before submission."
fi
if [ "$pages" -gt 50 ]; then
  echo "ERROR: $PDF is $pages pages — above P99 for astro-ph. Mandatory restructure: move systematics + derivations to appendix before external review."
fi
```

## What to do when triggered

1. **Identify main-text boundary**: headline result + key methods + primary systematics claim + conclusions = target ≤20pp main text.
2. **Demote to appendix**: full null battery tables, all intermediate derivations, per-leg/per-conf breakdowns, extended injection sweeps, version history prose.
3. **Move to GitHub/Zenodo**: full JSON artifacts, scripts, MC seeds — cite as release tag, not inline table.
4. **Do NOT add new content in a closure round** until scope is restored to target range.

## Prevention

Add to `/paper-pre-review-check`:
- Run `pdfinfo` page count; WARN >40pp, ERROR >50pp.
- On first trigger, invoke `/paper-restructure-to-appendix` (skill to be created) before proceeding with any closure content.

## Frequency by paper (estimated)

| Paper | Start pp | Current pp | Versions | Pattern fires |
|-------|----------|------------|----------|---------------|
| P4 | ~20 | 57 | 151 | 1 (confirmed external) |
| P3 | ~20 | 50 | 73 | 0 (not externally flagged yet) |
| P1A | ~15 | 20 | 40 | 0 (within range) |
| P1B | ~10 | 12 | 42 | 0 (within range) |
| P2 | ~18 | 23 | 43 | 0 (within range) |
| P5 | ~15 | 21 | 44 | 0 (within range) |

## Related patterns

- [[pattern-018-internal-rounds-blind-to-editorial]] — internal rounds can't see length/scope issues
- [[pattern-030-round-to-round-regression-drift]] — scope creep is the structural analogue of content regression

