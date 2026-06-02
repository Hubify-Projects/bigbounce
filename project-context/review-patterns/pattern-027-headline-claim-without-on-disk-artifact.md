---
status: confirmed
proposed_by: r-round-pattern-mine
proposed_date: 2026-05-15
confirmed_date: 2026-06-02
review_target: catalog
source: P4-pattern-020 headline-claim-without-on-disk-artifact
---

# Pattern 027 — Headline numeric claim has no on-disk artifact (or artifact disagrees)

**First seen**: P4 v1.0.66 external — B3 flagged abstract claim "26,636
spiral galaxies in catalog" while the on-disk catalog .csv had 26,626 rows.
**Severity**: high (every quantitative headline must trace to an artifact;
disagreement is a load-bearing-result error)
**Frequency**: 5+ instances
- P4 v1.0.66 B3: abstract N = 26,636 vs catalog N = 26,626
- P4 R42 B22: paper 26,636 vs HF model card 26,626 (sibling instance)
- P1A: "f_NL forecast σ = 18" vs MCMC sample storage (intermittent across
  rounds)
- P3 R42: "100k OOD validation" headline vs no OOD artifact on disk (also
  pattern-023)
- P5: cosmic-web N counts in abstract vs catalog .fits row count

**Detection**: for every numerical claim in abstract/intro/headline-table/
caption, grep the cited artifact path on disk and verify the number matches.
Abstract claim X with on-disk artifact value Y ≠ X = BLOCKER.

## What it looks like

> P4 v1.0.66 B3 (ChatGPT REJECT-AND-RESUBMIT): "Abstract states 'a catalog
> of 26,636 spiral galaxies.' The cited catalog at pipelines/p2_chirality/
> chirality_catalog_v1.0.66.csv contains 26,626 rows (`wc -l` minus header).
> Either the abstract is wrong, the catalog is stale, or the cited path is
> wrong. This is the headline number of the paper."

## Truth-audit verdict

VERIFIED in 4 of 5 instances. The fifth (P3 100k OOD) collapsed into
pattern-023 (deferral with false-cost excuse) — the artifact didn't exist
because the operation hadn't been run.

## Examples observed

(See "Frequency" list above.)

## Root cause

Headline claims are written at closure-time and not re-verified against the
on-disk artifact. Often the artifact regenerates with a new N (after a row
filter, after a re-training, after a dedup step) but the abstract / intro
/ caption is not re-walked. Pattern-008 (closure-introduced regression) is
the broader family; pattern-027 is the specific case where the closure
moved the artifact but not the headline.

## Pre-review check

```bash
# Step 1: extract every numerical claim from abstract + intro + section
#   headers + figure captions + table captions
grep -nE '\b[0-9]+([\.,][0-9]+)*\b' <paper.tex> | head -50

# Step 2: for each "headline" number (catalog size, σ, redshift bin, sample
#   size), identify the on-disk artifact in pipelines/.../ or research/.../
#   and verify:
#     - .csv / .parquet / .fits row count
#     - .json metadata field
#     - notebook output cell
#   matches the paper claim.

# Step 3: any mismatch → BLOCKER. Closure is to fix abstract OR re-generate
#   artifact; NEVER hand-edit one without the other.
```

Standing rule: every numerical headline claim in any paper must carry an
inline comment with the artifact path:

```latex
% claim source: pipelines/p2_chirality/chirality_catalog_v1.0.66.csv (26626 rows)
We present a catalog of 26{,}626 spiral galaxies...
```

The `/bigbounce-claims-table-sync` skill enforces this across abstract +
intro + all paper-side AND site-side references when any claim changes.

## Related patterns

- Pattern 008 (closure-introduced regression) — parent: 027 is a specific
  case of 008 where the artifact moved but the headline didn't
- Pattern 021 (external-artifact-pdf-blind) — sibling: 021 is off-disk
  artifact drift; 027 is on-disk
- Pattern 026 (reproducibility-anchor-404) — sibling: 026 is artifact
  not reachable; 027 is artifact reachable but disagrees with paper
- `/bigbounce-claims-table-sync` skill — implements prevention layer
