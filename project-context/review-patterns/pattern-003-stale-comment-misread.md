# Pattern 003 — Stale `%`-comment misread as paper body

**First seen**: P1A v1.0.128 era (pre-true95; Grok-B1 read legacy title comment)
**Severity**: high (premise-failure: reviewer is reading the wrong content)
**Frequency**: 6 occurrences (P1A R1, P4 R1, P5 R8 GRO-B1, P1B R4 GRO-B5, P1B R6 GRO-B1, P1B R7 GRO-B1)
**Detection**: Reviewer cites text from the .tex file that DOES NOT APPEAR in
the compiled PDF, OR cites lines in the preamble / above `\begin{document}`.
**Prevention**: Strip stale title-comment / legacy-version comments from .tex
preamble. Keep all review-log content in companion `.md` files, not in `%` blocks.

## What it looks like

> GRO-B1 (BLOCKER): The abstract still labels the result a "perturbation-
> transparency theorem"; this overclaim must be retitled.

When investigated: the reviewer was reading a `%`-prefix comment containing the
v1.0.128 legacy title, not the current abstract. Compiled PDF has zero such
text.

Or:

> GRO-B1 (BLOCKER): The §IX "no environmental dependence" framing is overclaim.

When investigated: the cited text was inside a `% v0.1.38 audit-log block
(R-multi-round5 GRO-m2 closure)` — i.e. a comment, not rendered.

## Truth-audit verdict

Premise-FAILED (or FALSIFIED on premise). The cited text does not exist in
the compiled PDF.

## Examples observed

- P1A pre-true95: GRO-B1 read v1.0.128 legacy title comment block as abstract
- P4 R1 GRO-n1: flagged 380-line review-log preamble (`%` comments) as "paper content"
- P5 R8 GRO-B1: read `%`-comment audit-blocks at lines 1-290 as abstract/§I content (explicit "premise FALSIFIED" verdict)
- P1B R4 GRO-B5: preamble audit log flagged as paper body
- P1B R6 GRO-B1 / R7 GRO-B1: persistent reflag of audit log comments as preamble content
- P1B R5 GRO-B6: paper-is-running-changelog complaint based on audit-log comments

## Root cause

Reviewers receive the .tex source (not just the PDF). LLM reviewers don't
reliably distinguish `%`-prefix LaTeX comments from rendered content,
especially when the comment block is long (~200-380 lines) or labeled with
section-like headers.

## Pre-review check

Before dispatching .tex to a vendor:

1. Run `grep -n '^%' paper.tex | wc -l` and report comment-line count.
2. Assert that no `%`-comment line contains the words "BLOCKER", "MAJOR",
   "MINOR", "STALE", "FALSIFIED", "VERIFIED" — these belong only in companion
   `.md` review-log files (pattern 014).
3. Strip the preamble audit-log block before dispatch (or send only the PDF).
4. If review-log MUST be retained in .tex for revision-history transparency,
   wrap the block in `\iffalse ... \fi` so it is parser-skipped and doesn't
   confuse text-based diff/review tools either.
5. Alternative: keep audit-log in `paper-{N}-review-log.md` and reference it
   from the .tex via a single in-text comment line, e.g.
   `% Review log: see project-context/peer-reviews/2026-06-01_*.md`
