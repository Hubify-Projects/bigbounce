---
status: draft
proposed_by: r-round-pattern-mine
proposed_date: 2026-06-02
review_target: Houston
---

# Pattern 018 — Internal R-rounds converge on "clean" while editorial artifacts persist

**First seen**: P1A 2026-06-02 external round vs P1A internal R-rounds 1-8
(8 internal rounds, 0 VERIFIED on pattern-017-shape body-prose artifacts;
external round 1 catches 9 distinct sites as BLOCKER/MAJOR)
**Severity**: high (meta-pattern; explains why a paper can hit
"3-consecutive-clean-rounds exit" and still be unfit for submission)
**Frequency**: 1 confirmed case (P1A 8-round internal cycle); structural
prediction is that any paper that has run cascaded internal-only R-rounds
without an external editorial check has the same blind spot
**Detection**: meta — measure the gap between
`(internal_verified_count over last 3 rounds)` and
`(external_verified_count when an external reviewer first sees the paper)`.
If external introduces ≥3 new VERIFIED findings on issues internal rounds
had visibility on, the internal protocol has a systematic blind spot.

## What it looks like

P1A internal R-round telemetry (from ALL-FINDINGS.json,
2026-06-01_R-multi-round2 through round8):

| Round | Surface | VERIFIED | Pattern-017-shape catches |
|-------|---------|----------|---------------------------|
| R2    | 102     | 11       | 0                         |
| R3    | ~60     | 5        | 0                         |
| R4    | ~50     | 2        | 0                         |
| R5    | ~40     | 1        | 0                         |
| R6    | 18      | 0        | 0                         |
| R7    | 17      | 0        | 0                         |
| R8    | 17      | 0        | 0                         |

Cascaded loop exited per AGENT_RULES §4.4.1 ("3 consecutive 0-VERIFIED rounds").
Paper labeled "ready for arXiv".

Then external 3-reviewer round on the SAME PDF:

| Reviewer | Recommendation | Findings | Pattern-017-shape catches |
|----------|----------------|----------|---------------------------|
| Grok     | MAJOR REVISIONS | 12       | 0 (not Grok's focus)       |
| Gemini   | MAJOR REVISIONS | 5        | 9 sites in 1 BLOCKER       |
| ChatGPT  | REJECT          | 29       | 9 sites in 1 MAJOR (M9)    |

Two of three external reviewers identified the same 9 review-log artifacts
that NONE of 8 internal rounds caught. ChatGPT issued a REJECT
recommendation in part because of these.

## Truth-audit verdict

VERIFIED. The meta-claim is observable in the ALL-FINDINGS.json telemetry.

## Root cause

Internal R-round vendors (Grok-4-brutal, GPT-methodology, Perplexity citation
forensics, Gemini billing-skip — when working) are configured by their
prompts to find:

- Physics errors
- Citation confabulations
- Dimensional inconsistencies
- Scope overclaims
- Companion-paper hedge violations

They are NOT configured to flag **editorial hygiene** — leftover review-log
prose, version-history sentences, multi-vendor framing — because that
content reads as "scratchpad" or "transparency text" to a domain-physics
reviewer. Their truth-audit verdict on pattern-014-comment-block findings
has historically been OPINION ("will be stripped at arXiv bundle stage"),
which trained the system to ignore the entire class.

An external reviewer reading the manuscript as a journal submission has the
opposite default: any text in the body that doesn't read as journal-style
prose is a defect. Gemini's blunt verdict — "the manuscript is currently in
an unpublishable state due to a total breakdown in editorial hygiene" —
captures the gap.

## Why cascaded loops + truth-audit + multi-vendor did not close this

- **Cascaded loops** (AGENT_RULES §4.4.1) measure "0 VERIFIED for N rounds"
  as the exit signal. If the failure mode is one nobody is detecting,
  cascading more rounds only confirms the silence.
- **Truth-audit** classifies findings AFTER they're raised. It doesn't
  generate findings the reviewers don't raise.
- **Multi-vendor** is bounded by the union of what the vendors flag. If all
  vendors share the same blind spot (editorial hygiene), the union still
  has the blind spot.

This is a coverage gap, not a measurement-noise gap.

## Pre-review check

Standing rule: **`/paper-pre-review-check` is MANDATORY pre-flight before
ANY external submission** (arXiv, journal, sharing with a frontier-model
reviewer outside the internal direct-vendor cycle). This is the prevention
layer the internal cycle structurally cannot provide.

The skill must check:

1. **Pattern-014** (`%`-comment review-log)
2. **Pattern-017** (BODY-prose review-log) — new, separate grep
3. **Pattern-005** (overclaim language) — passive check
4. **Pattern-006** (companion-paper hedge) — passive check
5. **Editorial-hygiene grep bundle** (covered by 014 + 017): no "BLOCKER",
   "MAJOR", "MINOR", "VERIFIED", "STALE", "FALSIFIED" anywhere in the
   compiled .tex body OR comment block.

Operational rule:
```
IF paper passed internal cascaded-loop exit
AND paper has NOT passed /paper-pre-review-check
THEN paper is NOT ready for external review.
```

## Houston-mandated implication

Per `feedback_review_learning_loop` standing directive: external review must
flow through learning-loop. Pattern 018 makes the **pre-review-check
mandatory gate** part of that loop, not optional.

Update `~/.claude/skills/paper-pre-review-check/SKILL.md` workflow:

- Run pattern-014 grep (anchored on `^%`)
- Run pattern-017 grep (body, no `^%` anchor) — separately reported
- Surface every match
- `--strict` mode: any pattern-014 OR pattern-017 match → BLOCK external
  submission until cleared

## Related patterns

- **Pattern 014** + **Pattern 017** — the two specific cases this
  meta-pattern explains
- **Pattern 016** (exit-boundary reflag-bloom) — describes the
  inside-the-loop signal that the internal cycle is exhausted, but does
  NOT address the editorial-coverage gap
- **Pattern 015** (Gemini billing-skip) — Gemini was the most-likely
  reviewer to flag editorial hygiene; consistent billing failures across
  internal rounds were a contributing factor. Restoring Gemini in the
  internal cycle would partially (not fully) close the gap.
