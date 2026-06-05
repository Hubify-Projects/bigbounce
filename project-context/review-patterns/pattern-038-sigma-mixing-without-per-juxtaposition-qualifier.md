---
pattern_id: 038
status: active
first_seen: R10v3p1 / autoloop fire 1 cross-paper diff (2026-06-05)
papers_observed: [P1A, P1B, P2, P3, P4, P5]
finding_count: 6 (one per paper, universal)
proposed_by: r-round-pattern-mine 2026-06-05 (auto-detected by tools/v3_autoloop_summary.py)
severity: ESSENTIAL (downgradable to MAJOR if abstract has a single clear disclaimer at the start)
prevention_action: per-table caption + per-paragraph qualifier audit
---

# Pattern 038 — σ values from different nulls juxtaposed without per-juxtaposition qualifier

## Symptom

When a paper presents multiple σ values derived from different null procedures (e.g., per-pixel-shuffle vs isotropic bootstrap vs binomial monopole-only), reviewers almost always flag any table, paragraph, or figure caption where two such σ appear side-by-side without an explicit "not directly comparable" qualifier.

A single sentence at the top of the abstract noting "σ values are not directly comparable" is **insufficient** — PRD reviewers demand the qualifier at every juxtaposition.

Cross-paper occurrence (autoloop R10v3p1, 2026-06-05):
- P1A, P1B, P2, P3, P4, P5 — all 6 papers had a `sigma_mixing` finding flagged by at least one reviewer. P4 had it as a 4-vendor CONSENSUS.

## Root cause

Authors mentally treat σ as a unitless statistical scale. Reviewers know that σ derived from procedure A is a different physical quantity than σ derived from procedure B — they only become comparable under specific Gaussian-equivalent rescaling, which the authors rarely show.

## Detection

```bash
# Find tables that list σ values without "not directly comparable" in the caption
awk '/begin\{table\}/,/end\{table\}/' <paper.tex> | grep -c "sigma\|σ" >> /tmp/sigma_count
# If any table caption has 2+ σ rows without "not directly comparable" → flag
```

In synthesis: any consensus_key matching `r"\bsigma values?\b.*\bnot.*comparable"` should appear in EVERY table caption that lists σ from ≥2 nulls.

## Prevention

- Add a footnote macro `\sigmadisclaimer{}` that expands to "σ values in this row/table are not directly comparable across rows; see Table I for the mapping of each result to its null."
- Add a pre-compile check to `/paper-pre-review-check`: count σ symbols in each table; if ≥2, require the disclaimer to appear in the caption.
- In every paragraph that juxtaposes two σ values, append the disclaimer parenthetically.

## Related
- [[pattern-039-cross-reference-bug-in-abstract]] — abstract references wrong table for null mapping
- [[paper-pre-review-check]] — runtime gate
