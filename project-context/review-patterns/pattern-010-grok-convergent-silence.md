# Pattern 010 — Grok convergent-silence signal (shrinking output)

**First seen**: P3 R2 (first explicit "PAPER-GRO-0: No new findings")
**Severity**: informational (positive signal — paper is converging)
**Frequency**: 8 (P3 R2/R3, P4 R2, P2 R2/R3, P1B R3 contraction, P5 R6-R8)
**Detection**: Grok-4 output length shrinks across rounds on a converging
paper (typical drop: 4KB → 1.8KB). Best signal: explicit "No new findings"
return text.
**Prevention**: track Grok output length round-over-round; treat
sustained-low or explicit-zero output as the strongest convergent-silence
indicator.

## What it looks like

R1 Grok report: 6 findings, ~4KB output, detailed reasoning per finding.
R2 Grok report: 0 findings, ~1.8KB output, single line "PAPER-GRO-0: No new
blocker- or major-grade findings survive the convergent-silence filter."
R3 Grok report: 0 findings explicit, or 2 polish nits, ~1.5KB output.

## Truth-audit verdict

Not a finding; a meta-signal. Use to inform the cascaded-r-rounds exit
decision.

## Examples observed

- **P3 R2 GRO-0**: explicit zero findings; R3 GRO-0 confirmed; 3-clean exit.
- **P4 R2**: Grok still found 5 items but all STALE; R3 Grok 0 findings.
- **P2 R2**: Grok explicit "No new findings" (clean exit at R3).
- **P1B**: Grok findings count R1=6, R2=3, R3=2, R4=6, R5-R7=6 (volume
  rebounded because reviewer started flagging in-source audit comments — see
  pattern 014).
- **P5 R6/R7/R8**: Grok output stable at 6 findings but all STALE/OPINION
  (volume rebound at exit boundary — see pattern 016).

## Root cause

Grok-4 brutal-honesty persona is the most literal: it scores claims against
on-disk text and shrinks output when it can't find new defects. Other
personas (GPT methodology, Perplexity citations) maintain consistent
output volume regardless of paper state.

## Pre-review check

Track these metadata per round:
- Grok output byte size
- Grok finding count
- Grok BLOCKER count specifically
- Whether output contains the literal "No new findings" or "PAPER-GRO-0"

Three consecutive rounds with (BLOCKER count == 0) AND (output size < 70%
of round-1 baseline) is a strong cascaded-loop exit indicator on its own —
even if GPT/Perplexity volume hasn't dropped.

Combine with pattern 009 (GPT volume is uninformative) and pattern 012
(Perplexity volume is uninformative): **Grok is the load-bearing
convergence signal**.

For dashboards / cron loops: emit `grok_output_bytes` and `grok_blocker_count`
as round telemetry alongside vendor-status / wall-time.
