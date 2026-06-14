---
pattern_id: 055
status: active
first_seen: R39conf-batch-truth-audit (2026-06-13)
papers_observed: [P3, P4, P5]
finding_count: 9  # multiple reviewers × 3 papers; P3 dirtiest (§III + Table I footnotes)
proposed_by: r-round-pattern-mine 2026-06-13
---

# pattern-055: audit-artifact body leak

**Description**: Review-round process language leaks into compiled body text (NOT `%`-comments, which are correctly invisible to readers). Strings like version tags (`v1.3.2`, `— v0.9`), artifact filenames (`\artifact{results.json}`), internal gate verdicts (`gate-PASS`, `gate-FAIL`), closure-wave terminology (`Path-C rebuild`, `before/after diagnostic`, `superseded`), ticket IDs (`FB103-1`, `EXT12`, `R39conf`), and sentences like "An earlier run reported..." appear in the rendered PDF and are read by external reviewers as paper content. This is distinct from pattern-017 (review-log artifacts in body prose) — pattern-017 covers R-round closure language. Pattern-055 specifically captures the broader class of INTERNAL PROCESS artifacts that compile into the PDF body: version tags, JSON artifact paths, gate verdicts, ticket IDs, and diagnostic comparison prose.

**Evidence (R39conf)**:
- P3 §III + Table I footnotes: multiple instances of closure-wave prose ("An earlier run reported...", "before/after diagnostic" comparison table row, "Path-C rebuild result") visible in compiled PDF. Dirtiest paper in R39conf batch.
- P4 footnote 1: version tag `v1.0.151` appears in rendered footnote body (not just `\date{}`) alongside `\artifact{catalog_c_post_tta_dipole_summary.json}` rendered as a visible string.
- P4 Fig 8 caption: "gate-PASS (R37conf closure)" visible in figure caption text.
- P5 §VI prose: "EXT12 finding B5" and "superseded by Path-C rebuild" appear in paragraph text.

**Resolution**:
- Title block: `\date{<short>}` only — no version tags in `\date{}` beyond the date stamp.
- Body text: strip ALL of the following from compiled text (they may exist in `%`-comments or companion review-log files, never in rendered body):
  - Version tags: `v[0-9]+\.[0-9.]+` patterns, `— v[0-9.]+`
  - Artifact filenames: `\artifact{*.json}` rendered text, `outputs/`, `pipelines/`, `.parquet`, `.fits`
  - Gate verdicts: `gate-PASS`, `gate-FAIL`
  - Closure-wave terms: `Path-C rebuild`, `before/after diagnostic`, `superseded`, `closure-wave`
  - Ticket/round IDs: `FB[0-9]+-[0-9]+`, `EXT[0-9]+`, `R[0-9]+conf`, `R[0-9]+ closure`
  - Diagnostic comparison phrases: `An earlier run reported`, `prior draft`, `earlier version described`
- Each "earlier run" comparison must be replaced with either: the final number inline (no history), or a Methods footnote referencing the companion review-log (not the body).

**Detection rule (mechanical)**:
```bash
# Against compiled PDF text (pdftotext):
pdftotext -layout <pdf_path> - | grep -inE \
  "(v[0-9]+\.[0-9]+\.[0-9]+|— v[0-9]+|gate-(PASS|FAIL)|Path-C rebuild|before/after diagnostic|superseded|closure-wave|FB[0-9]+-[0-9]+|EXT[0-9]+|R[0-9]+conf|An earlier run reported|prior draft|earlier version(s)? described)"

# Against .tex source (catches things before compile, not anchored to ^%):
grep -nE "(v[0-9]+\.[0-9]+\.[0-9]+|gate-(PASS|FAIL)|Path-C rebuild|closure-wave|FB[0-9]+-[0-9]+|EXT[0-9]+|R[0-9]+conf|An earlier run reported|prior draft)" <tex> | grep -v '^[0-9]*:%'
```
False positives: legitimate physics variable names containing "v" followed by digits (e.g., `$v_{200}$`, `$v_{\rm esc}$`) — these are LaTeX-math-mode strings and will not match the `v[0-9]+\.[0-9]+` pattern without context. Also: `EXT` as an abbreviation in a different physics context — manually verify. `R[0-9]+conf` is extremely unlikely to be a physics symbol.

**Severity**: high (title/abstract-level version artifacts, gate verdicts visible in PDF); medium (body prose diagnostic comparisons)

**Cross-reference**: pattern-017 (review-log artifacts in body prose — R-round closure language) is the closest existing pattern. Pattern-055 extends the detection surface to cover version tags, artifact paths, gate verdicts, ticket IDs, and diagnostic comparison sentences that pattern-017's regex misses. Both checks MUST run separately. Closures for pattern-017 do NOT close pattern-055.
