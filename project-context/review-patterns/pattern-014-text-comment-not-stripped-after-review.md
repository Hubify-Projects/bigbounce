# Pattern 014 — Review-log content left in `%`-comment block triggers misread

**First seen**: P4 R1 GRO-n1 (380-line review-log preamble flagged)
**Severity**: medium (related to pattern 003 but specific to review-log content)
**Frequency**: 4 (P4 R1, P5 R8 GRO-B1, P1B R4-R7 GRO preamble audit-log
flag in 4 consecutive rounds)
**Detection**: a `%`-comment line in the .tex contains words like "BLOCKER",
"MAJOR", "MINOR", "STALE", "FALSIFIED", "VERIFIED", "R{N}-", "GRO-", "PER-",
"GPT-".
**Prevention**: keep all review-log content in companion `.md` files only.
The .tex must not embed reviewer-output verbatim.

## What it looks like

```latex
% =====================================================
% v1B.0.34 (R-multi-round4): PER4-B2 closure
% BLOCKER → VERIFIED: Eskilt dataset PR3 → PR4/NPIPE
% Verified via github.com/LilleJohs/Cosmic_Birefringence
% Round-3 closure (PR3) was a regression; restored PR4/NPIPE.
% =====================================================
```

This block is invisible in the compiled PDF, but the .tex source is sent
to the reviewer, who reads it as paper body.

> GRO-B5 (round 4-7): "Paper-is-a-running-changelog" complaint about the
> preamble audit-log block; reviewer wants the .tex hygiene cleaned up.

> P5 R8 GRO-B1: read `%`-comment audit-blocks at lines 1-290 as
> abstract/§I content (explicit "premise FALSIFIED" verdict).

## Truth-audit verdict

OPINION (the audit-log will be stripped at arXiv bundle stage). But the
reviewer's confusion costs audit time every round.

## Examples observed

- **P4 R1 GRO-n1**: 380-line review-log preamble triggered misread.
- **P5 R8 GRO-B1**: `%`-comments at lines 1-290 (audit-log blocks for all
  prior round closures) misread as abstract/§I content. Marked
  OUT-OF-SCOPE / premise-FALSIFIED.
- **P1B R4/R5/R6/R7 GRO**: preamble audit-log block reflagged 4 consecutive
  rounds. The closure protocol is "strip at arXiv bundle stage", but the
  block persists in main-branch .tex and keeps drawing reviewer attention.
- **P1B R5 GRO-B6 / R6 GRO-B6 / R7 GRO-B6**: "delete repetitive null-consistency
  check phrasing" — actually a comment-block misread combined with a
  pattern-003 false-positive.

## Root cause

The repo's review protocol bakes the round-by-round audit log into the .tex
preamble for revision-history transparency. This is good for git history but
bad for reviewer experience because the reviewer's prompt asks them to find
issues in the .tex source.

## Pre-review check

Before any R-round dispatch:

1. **Assert**: no `%`-comment line in the .tex contains any of these
   markers:
   ```
   BLOCKER MAJOR MINOR STALE FALSIFIED VERIFIED OPINION
   R[1-9]+- GRO- PER- GPT- GEM-
   "round 1" "round 2" "round 3" "round 4" "round 5"
   ```
2. **Move all review-log content** from the .tex to
   `project-context/peer-reviews/<round-label>_P<N>_synthesis.md` (where it
   belongs). Leave a single one-line pointer in the .tex:
   ```latex
   % Review log: see project-context/peer-reviews/*_P{N}_synthesis.md
   ```
3. **Alternative**: wrap the audit-log block in `\iffalse ... \fi` so it's
   parser-skipped and text-search-quiet.
4. **Strip at PDF-mirror stage**: when mirroring to site/public/papers,
   send only the PDF (not the .tex) so reviewers using the public site can't
   confuse the comment block with paper body.

Standing rule: **review-log content lives in .md files, not .tex
comments.** Even revision-history transparency can be served by a single
`.tex` line pointing at the per-round .md file in
`project-context/peer-reviews/`.
