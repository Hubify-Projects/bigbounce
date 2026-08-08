---
pattern_id: ppattern-cross-cite-submission-order
status: seeded
first_seen: P1-2026-06-19
papers_observed: []
proposed_by: paper-packaging-round 2026-06-19
---

# ppattern-cross-cite-submission-order — Paper cites companion arXiv ID that doesn't exist yet

## Defect

Paper A cites Paper B's arXiv ID (e.g. `arXiv:2506.XXXXX`) but Paper B has not
yet been submitted to arXiv. The citation resolves to a dead link in the
published version. Readers who click it get a 404. Referees flag it as a
fabricated citation (triggering pattern-001). The submission order must respect
the dependency graph.

## How to detect

```bash
# Find arXiv IDs cited in the paper
grep -ohE 'arXiv:[0-9]{4}\.[0-9]{4,5}' paper.tex paper.bbl > cited_arxiv.txt

# For each ID, check arXiv resolution
while read id; do
    code=$(curl -s -o /dev/null -w "%{http_code}" "https://arxiv.org/abs/${id#arXiv:}")
    [ "$code" != "200" ] && echo "NOT YET LIVE: $id"
done < cited_arxiv.txt
```

Also check for companion-paper citations that are self-authored
(`Golden2026P*`, `golden_*`) and resolve them against the current arXiv submission status.

## Fix

Before submitting Paper A:
1. Build the dependency graph: which papers does A cite by arXiv ID?
2. For each cited paper not yet on arXiv: submit it first (or replace the arXiv
   citation with `(in preparation)`).
3. Record the intended submission order in the P-round arXiv kit.

Canonical bigbounce order: P4 → P1A + P1B → P3 → P2 → P5 (cross-cite chain
goes in this direction; later papers cite earlier ones by real arXiv IDs).
