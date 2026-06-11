---
pattern_id: 051
status: active
first_seen: EXT2/R29 (2026-06-10 — both rounds' dominant new-finding class)
papers_observed: [P1A, P1B, P2, P3, P5]
proposed_by: EXT2 gap-mine 2026-06-10
---

# pattern-051: closure-introduced regression

**Description**: Fix waves create new defects — patched math carries fresh errors (P1A R29 pair-exchange sign error, P2 dimensionally-broken OOM bounds), half-applied sweeps leave contradictory surfaces (P3 eROSITA de-scope caption-vs-body, P5 terminology half-sweep), and closure artifacts themselves are wrong (P1B units-README mislabeling a column-permutation bug). ~40% of genuinely-new EXT2 findings were regressions from our own EXT1/R29 closures.

**Evidence**: EXT2 audits: P1A 6 new (2 closure-introduced), P1B 4 (CORRECTED.json reintroduction), P2 6 (App A convention from abstract rewrite), P3 body-vs-caption leak, P5 stale "strong robustness" survivor.

**Prevention** (the closure-wave protocol, mandatory for every fix agent):
1. SWEEP-COMPLETENESS: any terminology/label/de-scope change greps ALL occurrences of the old form before declaring done; report the residual count explicitly.
2. SELF-DIFF REGRESSION CHECK: after edits, re-read every changed hunk ±2 paragraphs (git diff) hunting contradictions with adjacent claims.
3. NEW-MATH GATE: any added equation/derivation/OOM bound gets an immediate dimensional + limiting-case self-check written into the agent's report (never "added bound" without the check).
4. CLOSURE-ARTIFACT VERIFICATION: a closure that creates an artifact (README, JSON, manifest) must verify the artifact's CONTENT empirically (e.g. from chains/data), not restate the reviewer's hypothesis.
5. The next internal round explicitly diffs against the closure commit and reviews CHANGED REGIONS FIRST.
