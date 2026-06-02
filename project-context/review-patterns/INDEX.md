# BigBounce Review-Pattern Catalog

Codified failure modes observed across 19 cross-vendor R-rounds on 6 papers
(P1A/P1B/P2/P3/P4/P5) plus 1 external 3-reviewer round on P1A (2026-06-02).
Every external/direct-vendor R-round must be pre-screened against these
patterns BEFORE dispatch, per the [[feedback-review-learning-loop]]
standing directive.

Catalog is consumed by `/paper-pre-review-check` skill.

## Patterns

| ID | Title | Severity | Freq |
|----|-------|----------|------|
| 001 | [Perplexity citation confabulation (real-arXiv-flagged-fake)](pattern-001-perplexity-citation-confab.md) | high | 38 |
| 002 | [Dataset attribution drift across closures](pattern-002-dataset-attribution-drift.md) | high | 6 |
| 003 | [Stale `%`-comment misread as paper body](pattern-003-stale-comment-misread.md) | high | 6 |
| 004 | [Buried §pathc_caveats closure not surfaced](pattern-004-buried-closure-restate.md) | medium | 14 |
| 005 | [Overclaim language (first/novel/load-bearing/publication-grade)](pattern-005-overclaim-language.md) | medium | 9 |
| 006 | [Companion paper self-cite missing in-prep hedge](pattern-006-companion-paper-hedge.md) | medium | 7 |
| 007 | [Reviewer arithmetic confabulation (number/sign wrong)](pattern-007-reviewer-arithmetic-confab.md) | high | 4 |
| 008 | [Closure introduces N+1 regression](pattern-008-closure-introduced-regression.md) | high | 5 |
| 009 | [GPT fallback (gpt-4o) low-rigor generic BLOCKERs](pattern-009-gpt-fallback-low-rigor.md) | medium | 30+ |
| 010 | [Grok convergent-silence signal (shrinking output)](pattern-010-grok-convergent-silence.md) | informational | 8 |
| 011 | [Confabulated bib survives many rounds till Perplexity catches](pattern-011-confabulated-bib-survives-first-draft.md) | high | 4 |
| 012 | [Perplexity web-search misses recent arXiv (within ~6mo)](pattern-012-perplexity-web-search-miss.md) | medium | 20+ |
| 013 | [Perplexity catches real issue but proposes wrong fix](pattern-013-perplexity-counter-proposal-may-be-wrong.md) | high | 5 |
| 014 | [Review-log content left in `%`-comment block](pattern-014-text-comment-not-stripped-after-review.md) | medium | 4 |
| 015 | [Gemini billing-failure skip (vendor-side outage, not paper-side)](pattern-015-gemini-billing-skip.md) | informational | 19 |
| 016 | [Wide-net reflagging at exit boundary (volume increases as substance vanishes)](pattern-016-exit-boundary-wide-net-reflag.md) | informational | 3 |
| 017 | [Review-log artifacts in BODY prose (not %-comments)](pattern-017-review-log-in-body-prose-DRAFT.md) (draft) | high | 9 (P1A v1A.0.35-36) |
| 018 | [Internal R-rounds converge on "clean" while editorial artifacts persist](pattern-018-internal-rounds-blind-to-editorial-DRAFT.md) (draft) | high (meta) | 1 case (P1A 8-round cycle) |

## Cross-pattern observations

- **Citation-forensics yield is monotonically declining**: P1A produced 5 real
  attribution closures in round-2, then 1, 0, 0, 0 across rounds 3-6. P5 produced
  2 real bib fixes in round-3, then 0 thereafter. Real defects exhaust fast.
- **GPT-4o (fallback from gpt-5)** never produced a VERIFIED closure across any
  paper after round-1 of any paper. Pattern 009 covers this.
- **Perplexity is the only reviewer that produced VERIFIED citation closures**
  after round 1. It is also the largest single source of FALSIFIED claims.
- **Grok-4 is the best convergent-silence signal** — explicit "no new findings"
  return correlates with 3-round-clean exit on P2, P3.
- **The Eskilt2022b dataset attribution thread** (P1B rounds 1-7) is the
  cleanest case study of pattern 002+008 (drift through 3 closures: PR3 wrong →
  PR4/NPIPE → PR3 regression → PR4/NPIPE final via repo cross-check).

## How to add a new pattern

When a new R-round surfaces a finding that does NOT match any of the 16
catalogued patterns, AND the same shape appears in ≥2 distinct findings
across rounds, create `pattern-NNN-<kebab>.md` following the schema in the
existing files and append a row to the table above. Skill
`/paper-pre-review-check` picks up new patterns automatically by globbing
`pattern-*.md`.
