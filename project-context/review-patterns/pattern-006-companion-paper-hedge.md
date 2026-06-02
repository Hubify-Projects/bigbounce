# Pattern 006 — Companion paper self-cite missing in-prep hedge

**First seen**: P1A R-multi-true95 (PER-B1 `Golden2026P2` flagged fictional)
**Severity**: medium (real prose-strength problem; closes in 1 edit)
**Frequency**: 7 (P1A R1 PER-B1/M1/M2/M3, P5 R1 PER-M3, P5 R3 GRO-m1, P5 R5 GRO-m1)
**Detection**: any `\cite{X}` where the bib key matches the paper's own author
prefix (`Golden2026*`, `golden_chirality_*`, `golden_fnl_*`) without an
adjacent parenthetical hedge.
**Prevention**: every self-reference to a companion paper MUST carry an
"(in preparation)" or "(submitted)" hedge at first use.

## What it looks like

> PER-B1 (BLOCKER, mis-graded as MAJOR): `Golden2026P2` is not discoverable
> in arXiv/ADS; either fictional or in-prep but unmarked.

> PER-M3 (MAJOR, VERIFIED): Papers II/IV used as established external
> literature; needs explicit "companion work" labeling.

## Truth-audit verdict

When the bbl already has `(in preparation)` label, FALSIFIED (Perplexity
search can't see the unposted preprint, but the bib entry is honest). When
the in-text usage implies external citability, VERIFIED.

## Examples observed

- P1A R1 PER-B1/M1/M2/M3 FALSIFIED: all 4 `Golden2026P{1b,2,3,4}` bbl entries
  ALREADY had `(in preparation)` labels. CLOSED PER-M3 was the genuine prose
  fix: "are from that companion" → "are drawn from the companion internal
  MCMC analysis (Paper I(b), *in preparation*); they are documented internally
  rather than as externally citable arXiv-posted numbers"
- P5 R1 PER-M3 VERIFIED: "(companion work, currently in preparation and not
  yet peer reviewed)" added at first use of Paper IV (§I) and Paper II (§XI.A)
- P5 R3 GRO-m1 VERIFIED: "(companion work, not yet peer-reviewed)" added to
  abstract first cite (line 222)
- P5 R5 GRO-m1 OPINION (already closed)
- P5 R6 PER-B6 STALE: golden_chirality_2026 already labeled

## Root cause

Citation-forensics reviewers (Perplexity) can't resolve in-prep companions
via web search; they report "not discoverable". They are correct that the
external reader can't verify the companion, so the prose must hedge.

## Pre-review check

For every paper:

```bash
# 1. Find all \cite{} keys matching the paper's author prefix
egrep -o '\\cite\{[^}]*\}' paper.tex | grep -i '\bgolden\|\b<paper_author_prefix>'
# 2. For each, check first in-text use has hedge:
for cite in $matching_keys; do
    first_use_line=$(grep -n "\\cite{$cite}" paper.tex | head -1)
    context=$(sed -n "${first_use_line}p" paper.tex)
    echo "$context" | grep -qE '(in preparation|submitted|companion|forthcoming)' \
        || echo "FAIL: $cite first use missing hedge"
done
# 3. Check bbl entry has "(in preparation)" label
grep "\\bibitem{$cite}" -A 5 paper.bbl | grep -qE '(in preparation|in prep|submitted)'
```

Standardize on the phrase `(companion work, in preparation, not yet peer-reviewed)`
at first in-text use. Bbl entries should carry the same phrase as part of the
author/title block.
