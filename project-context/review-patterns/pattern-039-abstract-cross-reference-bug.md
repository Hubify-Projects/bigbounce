---
pattern_id: 039
status: active
first_seen: R10v3p1 / autoloop fire 1 cross-paper diff (2026-06-05)
papers_observed: [P1A, P1B, P3, P4, P5]
finding_count: 5 (5/6 papers)
proposed_by: r-round-pattern-mine 2026-06-05 (auto-detected by tools/v3_autoloop_summary.py)
severity: ESSENTIAL (cross-references in load-bearing abstract text)
prevention_action: latex \ref{} integrity audit per compile
---

# Pattern 039 — Abstract cross-references (Table II / Table IV) that don't match content

## Symptom

The abstract or introduction makes a forward reference like "see Table II for the mapping" or "Table IV shows...". When the reviewer follows the reference, Table II/IV is a different table than expected.

Most damaging instance (P4 R10v3p1, 4-vendor consensus): Abstract reads "see Table II for the mapping of each result to its null." Table II is the CW-fraction table; the null mapping is in Table I.

Cross-paper occurrence (autoloop R10v3p1, 2026-06-05):
- `table_ii` consensus key: P1A, P1B, P3, P4, P5 (5/6)
- `table_iv` consensus key: P1A, P3, P4 (3/6)

## Root cause

When tables are renumbered (e.g., a new table inserted before existing Table II), only the `\label` and `\ref` are auto-updated by LaTeX. Hardcoded "Table II" or "Table IV" prose references in the abstract / introduction do NOT auto-update.

## Detection

```bash
# Find hardcoded Roman numeral table references
grep -E "Table\s+I+V?I*\b|Tabel\s+\d|Table\s+\d+" <paper.tex> | grep -v "\\\\ref"
# Each hit should be replaced with \ref{tab:name}
```

```bash
# Cross-check: for every "Table X" prose reference, verify it points to the intended content
grep -E "Table\s+I+V?I*" <paper.tex>
```

## Prevention

- **Mandatory `\ref{tab:label}` for every table reference.** Banish hardcoded Roman numerals from prose.
- Add a pre-compile check to `/paper-pre-review-check`: grep for `Table\s+I+V?I*` (Roman numeral) prose references; flag each.
- In every R-round, manually walk the first three table references in the abstract + introduction.

## Related
- [[pattern-038-sigma-mixing-without-per-juxtaposition-qualifier]] — the most common reason an abstract refers to a Table
- [[paper-pre-review-check]] — runtime gate
