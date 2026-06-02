# Pattern 004 — Buried §pathc_caveats closure not surfaced

**First seen**: P3 R-multi-true95 (13/13 STALE because §pathc_caveats (a)-(j) not surfaced)
**Severity**: medium (wastes reviewer attention; doesn't introduce errors)
**Frequency**: 14 (P3 R1 all 13, P3 R2 all 6 GPT findings, P3 R3 GPT-B1 through B6, plus scattered)
**Detection**: Reviewer raises a concern that is verbatim addressed in
`§pathc_caveats`, `§sec:limitations`, or a deep `\footnote{}` — but reviewer
didn't grep for the section anchor.
**Prevention**: Every closed `§pathc_caveats` item should have a brief anchor
in the abstract or methods section so reviewers find it without grep.

## What it looks like

> GPT-B1 (BLOCKER): The 5-fold validation losses (0.76-4.91) do not meet the
> ≤0.30 production gate, so the rankings may not generalize.

When investigated: §pathc_caveats item (i) at L1083 contains verbatim:
> "Individual fold validation losses (range 0.76-4.91) do not meet the
> production-quality ≤0.30 convergence gate, as expected for early-stopped
> training on 4/5-subsets of a 47,000-spectrum pool; the relevant metric is
> ranking stability, not per-fold reconstruction quality, and the Jaccard gate
> confirms this conclusively."

The reviewer didn't grep for "5-fold" or "validation losses" before flagging.

## Truth-audit verdict

STALE every time — closure is on-disk, reviewer just didn't grep.

## Examples observed

- P3 R1 GRO-B1/B2/B3, GRO-M1/M2/M3, GPT-B1-B3, PER-B1-B3: 13/13 STALE because
  §pathc_caveats (a)-(j) closures weren't anchored in abstract
- P3 R2 GPT-B1-B6: same 5-fold val losses, SDSS cross-transfer, novelty
  fraction, etc. — all reflagged because §pathc_caveats not abstract-anchored
- P3 R3 GPT-R3-B1-B6: identical reflag for 3rd consecutive round
- P1A many rounds: structural-tension section labeled "(robustness check, not
  co-equal closure)" in title — reviewer asks for that exact label

## Root cause

LLM reviewers anchor on the abstract + section headers. If a substantive
closure lives only in a `§pathc_caveats` block at line 1000+ of a 1500-line
paper, reviewers won't see it.

## Pre-review check

For every paper:

1. Grep all `§pathc_caveats`, `§limitations`, deeply-nested `\footnote{}`
   closures.
2. For each, verify there is a one-line abstract anchor (e.g. "fold validation
   range explained in §pathc_caveats (i)") OR a "See §sec:foo for the full
   caveat" sentence in the section the reviewer is most likely to flag.
3. If the closure deals with a number (e.g. "σ(fNL)≈0.7"), make sure the
   number appears with a footnote pointer in the abstract.

For P3 specifically, the §pathc_caveats items (a)-(j) were closed in v3.1.65-70
but only the round-3 audit block surfaced them across the abstract; rounds 1
and 2 had 13/13 STALE because reviewers couldn't find them.
