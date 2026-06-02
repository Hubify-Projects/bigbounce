---
status: confirmed
proposed_by: r-round-pattern-mine
proposed_date: 2026-05-08
confirmed_date: 2026-06-02
review_target: catalog
source: CCAI-cluster-pattern-022 multi-agent-intra-round-convergence
severity_class: meta-architecture
---

# Pattern 034 — Same-vendor parallelism does not generate reviewer diversity

**First seen**: CCAI cluster 2026-05-08 to 2026-05-10 — empirical R43-R51
vs OOOOO round. 4 parallel Claude sub-agents per CCAI round produce ~4
findings. 4 different vendors (Anthropic / OpenAI / Gemini / Grok) on the
same paper produce ~50 findings. Ratio is 4:50 ≈ **12.5× amplification
from vendor diversity, ~0% from same-vendor parallelism.**
**Severity**: informational (meta-architecture rule, not a per-paper
finding)
**Frequency**: structural — every same-vendor parallel-agent setup has
this property by construction. Once measured, it's settled.

**Detection**: count distinct findings from N same-vendor parallel agents
vs from N different-vendor agents on the same paper. Ratio approaches 1
for same-vendor (no diversity gain) and N for different-vendor (full
diversity gain up to the union of vendor blind spots).

## What it looks like

CCAI rounds R43-R51 (9 rounds × 4 Claude sub-agents = 36 agent-invocations):
- Findings surfaced: ~4 per round, ~36 cumulative
- Unique findings (after dedup): ~12 — substantial overlap

OOOOO round (1 round × 4 different vendors = 4 agent-invocations):
- Findings surfaced: ~50
- Unique findings: ~45 — minimal overlap

The OOOOO round, with 1/9 the agent-invocations of CCAI, surfaced 12.5×
the BLOCKER+MAJOR findings.

## Truth-audit verdict

VERIFIED. This is a measurement, not a hypothesis. The 12.5× number is
the single most-important meta-finding of the 3-month retro pattern mine.

## Examples observed

- P3 + P2 OOOOO (2026-05-08) — the canonical measurement
- (predicted) every same-vendor parallel-review setup in the campaign

## Root cause

Parallel sub-agents from the same vendor share:
1. Training data
2. Reward-model preferences
3. System-prompt-shape biases
4. Decoding parameters and sampling defaults
5. Calibration on the same benchmark suite

Their findings are HIGHLY correlated. Adding more of them does not
expand the surface they explore. Diversity comes from cross-vendor:
different training distributions, different RLHF objectives, different
toolchains.

## Pre-review check

This pattern doesn't generate paper-side findings; it generates
**campaign-architecture** rules.

Operational rules:
1. Loop convergence exit gate must require **ALL** of:
   - (a) CCAI converged on the current version
   - (b) ≥1 cross-vendor round clean on the current version
   - (c) Houston sign-off
   Not just (a).

2. CCAI rounds are valid for **early-stage cleanup** (catching trivial
   mistakes cheaply with same-vendor parallelism), but they cannot
   substitute for cross-vendor review at the convergence boundary.

3. Cost-of-cross-vendor is ~$0.50 per paper per round via direct vendor
   APIs (per `/cross-vendor-r-round` skill); this is cheaper than the
   labor of writing a CCAI round. Default to cross-vendor.

4. When firing same-vendor parallel agents, explicit diversity prompts
   ("you are the math reviewer", "you are the citation reviewer") only
   partially separate their findings. Useful for triage; not a substitute
   for cross-vendor.

## Related patterns

- Pattern 031 (self-review severity under-classification) — sibling:
  severity side of the same-vendor blindness
- Pattern 032 (CCAI cross-paper blindness) — sibling: coverage side
- Pattern 018 (internal-rounds blind to editorial) — meta-parent:
  explains why internal-only convergence is not external-ready
- `/cross-vendor-r-round` — the canonical fix
- `/readiness-cap-99` — enforces (a)+(b)+(c) gate

## Campaign implication

Every readiness % claim of ≥95% on a paper that has NOT had a cross-vendor
round on its current version is implicitly accepting the 12.5× pipeline.
This is the formalization of `/readiness-cap-99` from the meta-architecture
side.
