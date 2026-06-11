---
pattern_id: 043
status: draft
first_seen: R23conf
papers_observed: [P1B, P4]
finding_count: 2 (confirmed recurrences in one round)
proposed_by: r-round-pattern-mine 2026-06-09
---

# Pattern 043 — Invented-configuration narratives (DRAFT)

**Severity**: HIGH (the paper describes an analysis that was never run; reads as fabrication on audit).
**Shape**: Paper text describes an analysis CONFIGURATION (chain layout, sample counts, selection cuts) that matches NO committed artifact. Typically the narrative is reverse-engineered from a TRUE total or true headline number — the bottom-line is right, so every reviewer pass that checks only the headline arithmetic confirms it, while the configuration story underneath is invented from memory.

## Recurrence evidence (R23conf)

1. **P1B §VI ALP provenance**: text claimed "three benchmark configurations
   C=4/8/12 with 3,240 samples each" — a tidy symmetric story invented around
   the REAL committed total 9,720 = 2,160 (run1) + 6,840 (run2) + 720 (run3).
   3 × 3,240 = 9,720 exactly: the invented narrative was constructed to
   reproduce the true total. Closed in v1B.0.52 by rewriting §VI FROM the
   committed chains.
2. **P4 headline-null generator**: the committed null generator selected an
   effectively all-CW subsample via a `p_cw_eq > 0.6` cut that the paper's
   description of the null did not mention (and would not have endorsed).
   Paper narrative and committed config diverged; regeneration from the fixed
   generator moved the headline 0.43σ/p=0.30 → 0.41σ/p=0.31 (verdict
   unchanged, but only by luck of MC noise).

## Why reviewers miss it

Cross-vendor reviewers see only the PDF; the headline total/result is correct,
so arithmetic spot-checks pass. Only a repo-side diff of "configuration as
described" vs "configuration as committed" catches it. This is the
configuration-layer sibling of pattern-027 (no artifact) and pattern-036
(fabricated math): here the artifact exists, the number is right, the STORY is
wrong.

## Mechanical detection rule

For each configuration/sample-count claim in the .tex (regex anchors:
`configurations?`, `chains?`, `samples? each`, `N\s*=`, `selected (with|using)`):

1. Resolve the committed inventory: chain directories, generator scripts,
   `*.yaml` configs, catalog selection code.
2. Diff claim-by-claim: number of configs, per-config sample counts, selection
   predicates. ANY count or cut that appears in prose but in no committed
   artifact = firing.
3. Red flag heuristic: prose counts that are exact divisors of a true total
   (total/k for small k) — the signature of reverse-engineering.

## Prevention hook

- **Belongs in `/paper-pre-review-check`** (provenance gate) and
  `/never-fabricate-derivation` (extends pattern-036 prevention to
  configuration prose): configuration paragraphs must be GENERATED from the
  committed configs — read the yaml/script/chain headers and write the prose
  from them — never written from memory and back-checked only against totals.
- Closure rule: any closure touching a provenance paragraph must cite the
  committed artifact path in the audit trail.

## Related

- pattern-036 (closure fabricates math justification) — same fabrication class, math layer.
- pattern-027 (headline claim without on-disk artifact).
- pattern-002 (dataset attribution drift) — drift vs invention.

## Promotion criteria

≥2 more confirmed firings (R24conf+) → promote + add the config-diff gate to
`/paper-pre-review-check`.
