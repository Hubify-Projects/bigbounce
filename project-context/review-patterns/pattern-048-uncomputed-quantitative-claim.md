---
pattern_id: 048
status: active
first_seen: EXT1 (2026-06-10, first automated browser-tier external round)
papers_observed: [P1A, P1B, P2, P3, P4, P5]
proposed_by: EXT1 gap-mine 2026-06-10
---

# pattern-048: uncomputed-quantitative-claim

**Description**: Inequality/rate/robustness claims stated qualitatively where a number is checkable

**Evidence (EXT1)**: P1A F4 (Γ_washout>H no computation), P1A F10 (e^32 separation no transfer function), P2 F27 (fiducial-shift bound qualifier only), P5 F8/F25 (no effect size, no joint regression)

**Prevention**: Internal reviewers accept the author's qualitative confidence. Prompt rule — for every >, <, exceeds, dominates, negligible, robust-to claim: demand the number, the computation pointer, or an explicit labeled-assumption tag.
