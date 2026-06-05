
## Cluster: σ-value incommensurability (2026-06-04, external_v1.0.149_P4)

**Sources**: ChatGPT B5 (2026-06-04 external review P4)
**Summary**: Multiple null procedures (binomial shuffle, MASTER MC, density-stratified shuffle, max-stat MC, analytic Bonferroni/BH, WLS template fit) each produce a σ value. Paper presents them all as if they're on the same scale and narrates a combined "σ story" without clarifying that they have different baselines, different H₀, and different power. Reviewer says: "Define ONE primary cosmological null and ONE primary systematics-preserving null. Other results labelled diagnostics, not merged into σ story."

**Pattern overlap**: Pattern-029 covers the pre-registration gap (no declared primary). This finding is a *presentational* variant: the declared primary exists but the body prose treats all nulls as co-equal evidence.

**Threshold**: 1 source, 1 paper — does NOT qualify for pattern-NNN yet. Re-check after next P4 external round. If flagged again, promote to pattern-038.

**Detection**: `grep -n "σ\|sigma" | count` >30 instances in paper body referencing different null procedures with no "primary null declared" banner.
