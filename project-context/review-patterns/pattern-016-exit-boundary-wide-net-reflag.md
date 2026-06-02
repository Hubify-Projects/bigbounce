# Pattern 016 — Wide-net reflagging at exit boundary (volume increases as substance vanishes)

**First seen**: P5 R8 (17 surface findings vs R7's 7, 0 VERIFIED in both)
**Severity**: informational (positive signal at the cascaded-loop boundary)
**Frequency**: 3 (P5 R7→R8 7→17 surface volume increase, P1B R5/R6/R7 reflag-bloom, P1A R5/R6 18-finding rounds with 0 VERIFIED)
**Detection**: total surface-finding count climbs while VERIFIED count stays
0 for 2+ consecutive rounds.
**Prevention**: track (surface_findings, verified_count) tuple per round;
sustained (high, 0) is the exit-boundary signal AGENT_RULES §4.4.1 predicts.

## What it looks like

| Round | Surface findings | VERIFIED |
|-------|-------------------|----------|
| R6    | 3                 | 0        |
| R7    | 7                 | 0        |
| R8    | 17                | 0        |

Surface findings jumped 2.4× round-over-round, but VERIFIED stayed at zero.
Reviewers are reflagging in larger volume as substantive defects vanish —
the literal "scraping the bottom" pattern.

## Truth-audit verdict

Not a finding; a meta-signal. Indicates cascaded-loop exit is at hand
(cf. AGENT_RULES §4.4.1: "convergent silence ≥3 of 4 vendors with reflag-
only output for 2 consecutive rounds").

## Examples observed

- **P5 R6→R7→R8**: 3 → 7 → 17 surface findings, 0 → 0 → 0 VERIFIED. Counter
  hit 3/3 at R8, cascaded loop exit fired.
- **P1B R4→R5→R6→R7**: 18 → 18 → 18 → 17 surface findings (stable volume,
  not reflag-bloom), but VERIFIED count R4=1, R5=0, R6=0, R7=0. Counter hit
  3/3 at R7, exit fired.
- **P1A R4→R5→R6**: 16 → 18 → 18 surface findings, 0 → 0 → 0 VERIFIED.
  Counter hit 3/3 at R6, exit fired.

## Root cause

LLM reviewers under a "find issues" prompt produce N findings even when no
real issues remain. As real issues exhaust, reviewers reach for ever-smaller
polish/preference/stylistic asks. The surface volume can actually INCREASE
as reviewers reach further down the priority stack.

This is a known LLM-reviewer artifact: the prompt asks for findings; the
model produces findings; the model can't honestly return "0 findings" except
when the persona explicitly permits it (which Grok does via "PAPER-GRO-0" —
pattern 010, but GPT/Perplexity rarely do).

## Pre-review check

Track these telemetry per round:

- `surface_findings_count`: total findings raised by all reviewers
- `verified_count`: findings that survive truth-audit
- `verified_ratio`: verified_count / surface_findings_count
- `surface_growth`: surface_findings_round_N / surface_findings_round_{N-1}

Exit-boundary signal:

```
3 consecutive rounds with:
  verified_count == 0 AND
  (surface_findings_count > 0 — i.e. not vendor-failure)
  AND no novel BLOCKER/MAJOR after truth-audit
→ cascaded-loop exit per AGENT_RULES §4.4.1
```

Bonus signals:
- `surface_growth > 1.5` AND `verified_count == 0` → strong exit-boundary
- Grok convergent-silence (pattern 010) AND `verified_count == 0` for 2
  rounds → near-certain exit boundary

When the exit boundary fires, do NOT schedule additional R-rounds without a
substantive .tex change. Further rounds are pure overhead at this stage and
will continue to produce reflag-bloom output with 0 VERIFIED.
