---
status: confirmed
proposed_by: r-round-pattern-mine
proposed_date: 2026-05-08
confirmed_date: 2026-06-02
review_target: catalog
source: CCAI-cluster-pattern-020 CCAI-cross-paper-bibkey-blindness
severity_class: meta
---

# Pattern 032 — CCAI cross-paper bibkey / value / cite-anchor blindness

**First seen**: CCAI cluster 2026-05-08 — 4 distinct cross-paper drifts in
single OOOOO round (B1 gamma, M3 Heinrich, M12 Munchmeyer, M13 Cai).
None caught by any CCAI per-paper agent.
**Severity**: high (every multi-paper campaign has these drifts; CCAI
topology guarantees they are invisible)
**Frequency**: 4 distinct cross-paper drifts in one round; structural
prediction is that every multi-paper campaign accumulates these

**Detection**: per-paper CCAI sub-agents do NOT see companion-paper
artifacts. Cross-paper drift (bibkey, value, anchor) is structurally
invisible to CCAI topology. Detection requires a 5th cross-paper-
consistency reviewer OR a programmatic grep across all .tex / .bib files.

## What it looks like

> OOOOO-B1 (BLOCKER, cross-paper): "P1A bibitem `Cai:2024` refers to
> arXiv:2401.12345 (Cai+Wang 2024 PRD). P2 bibitem `Cai2024` (same key shape,
> different capitalization) refers to arXiv:2403.99999. The same surname-year
> is used to cite TWO different papers across companion papers. External
> reviewer will not know which is which."

> OOOOO-M3 (MAJOR, cross-paper): "Heinrich+2023 is cited in P1A as JCAP
> 2024 and in P3 as JCAP 2023. Same paper, different journal-year stamp."

## Truth-audit verdict

VERIFIED in all 4 instances. Cross-paper grep trivially confirms.

## Examples observed

(See "Frequency" list above.) Pattern is structurally invisible to any
single-paper review topology.

## Root cause

CCAI sub-agents are scoped per-paper. The orchestrator does not pass
cross-paper context. A bibkey-or-value drift between P1A and P2 is
invisible to:
1. CCAI agent reviewing P1A only
2. CCAI agent reviewing P2 only
3. Any cross-vendor reviewer reviewing one paper at a time

Only a cross-paper consistency check or an external reviewer who reads
all companion papers catches it.

## Pre-review check

```bash
# Step 1: bibkey collision check across all .tex/.bib in the campaign
grep -hE '^\\bibitem\{[^}]+\}' arxiv/*.bbl pipelines/*/paper*.bbl research/*/*.bbl \
  | sort | uniq -c | sort -rn | head -50
# Any bibkey appearing in 2+ papers must point to the SAME (Author, Year,
# arXiv, Journal). Grep both papers to verify the citation strings match.

# Step 2: value-drift check for shared survey/dataset numerics
#   (Planck 2018, ACT DR6, DESI DR2 sample sizes; H0; σ_8; n_s; etc)
for survey in "Planck 2018" "ACT DR6" "DESI DR2" "WMAP" "SDSS DR17"; do
  echo "=== $survey ==="
  grep -rn "$survey" arxiv/*.tex pipelines/*/paper*.tex research/*/*.tex \
    | grep -oE "[0-9]+[\.,][0-9]+" | sort -u
done
# Any survey whose cited numerics differ across papers needs reconciliation.

# Step 3: anchor / section-reference drift
#   companion-paper citations like `\cite{Golden2026P2}` — verify the
#   referenced section / equation actually exists in the target paper at
#   the current version
```

Operational rule: add a "5th CCAI agent role" or run this cross-paper
grep at the START of every multi-paper R-round, BEFORE per-paper agents
fire. Findings from this step have priority because they affect multiple
papers.

`/bigbounce-claims-table-sync` skill addresses the value-drift side;
this pattern adds the bibkey-drift side.

## Related patterns

- Pattern 031 (self-review severity under-classification) — sibling: 031
  is severity blindness; 032 is coverage blindness
- Pattern 002 (dataset attribution drift) — within-paper version of the
  same problem; 032 is the cross-paper version
- Pattern 034 (multi-agent same-vendor no diversity) — explains why
  adding more CCAI agents doesn't fix this
- `/bigbounce-claims-table-sync` — implements the value-drift detection
  and propagation
