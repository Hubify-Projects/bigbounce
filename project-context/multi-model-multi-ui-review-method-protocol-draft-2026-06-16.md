# Multi-Model / Multi-UI Review Method Protocol Draft

**Date:** 2026-06-16  
**Status:** Candidate workflow-paper draft only. No paper claims, reviewer verdicts, PDFs, tarballs, queues, pods, or public artifacts were changed.

## Working Title

**Multi-Model / Multi-UI Review as an Adversarial Quality-Control Protocol for AI-Assisted Research**

## Status Claim

This is a **workflow hypothesis**, not an established research result.

The BigBounce campaign suggested that using multiple model families across multiple interaction surfaces may make reviewer failure modes less correlated and may reduce the chance that one self-reinforcing agent loop can grade its own work too generously. That observation is promising, but not yet proven.

Any future paper or method note must keep that honesty upfront.

## Core Hypothesis

Compared with a single-model or single-UI review loop, a review stack that combines:

1. multiple model families,
2. multiple interaction surfaces,
3. source-grounded truth audits, and
4. closure agents separated from reviewers

will produce a higher rate of real finding discovery, a lower rate of closure drift, and a more legible audit trail.

## Definitions

| Term | Meaning |
|---|---|
| `model diversity` | Reviewers come from different model families or vendors rather than one lineage. |
| `UI diversity` | Reviewers are prompted through different interfaces or orchestration surfaces rather than one repeated chat loop. |
| `truth audit` | A separate step that verifies whether a finding is real against source files and artifacts. |
| `closure agent` | An execution agent that fixes only verified findings. |
| `review stack` | The full set of reviewer prompts, interfaces, truth-audit rules, and closure mechanics used for one round. |

## Candidate Protocol

### Phase 1: Freeze The Artifact Under Review

- Identify the exact source files, version, and rendered artifact under review.
- Record hashes, commit ID, or equivalent provenance.
- Ban silent artifact swaps mid-round.

### Phase 2: Independent Review Fan-Out

- Dispatch the same artifact to several reviewer models.
- Use at least two distinct UI surfaces where practical.
- Keep prompts semantically aligned but not copy-pasted if surface constraints differ.
- Require each reviewer to cite concrete locations and proposed fixes.

### Phase 3: Normalize Findings

- Collect findings into a shared ledger.
- Deduplicate near-identical findings.
- Separate factual allegations from stylistic counter-proposals.
- Mark ambiguous items for truth audit rather than immediate closure.

### Phase 4: Truth Audit

- Verify every substantive finding against the actual source artifact.
- Classify each item, for example:
  - `verified`
  - `partially verified`
  - `stale`
  - `false positive`
  - `editorial counter-proposal`
- Preserve why a finding was accepted or rejected.

### Phase 5: Closure

- A separate execution lane fixes only verified or intentionally accepted items.
- No reviewer should mark its own finding resolved without a source-grounded check.
- Rebuild or re-render any affected artifacts.

### Phase 6: Confirmation Round

- Re-run review on the updated artifact.
- Track whether prior finding classes reappear.
- Require at least one clean or convergent confirmation round before elevating readiness.

## Candidate Minimum Reviewer Stack

For a first formalized method paper, the protocol should describe reviewer diversity in capability terms rather than locking to specific vendors:

- one long-context reviewer
- one skeptical methodology reviewer
- one citation or web-grounded reviewer when current-source checks matter
- one closure/consistency reviewer that focuses on regressions and drift

UI diversity could include:

- terminal-native coding/review agent
- web-chat or hosted research UI
- local tool-orchestrated pipeline

The paper should say explicitly that the benefit being tested is **heterogeneity**, not brand prestige.

## Proposed Metrics

Track per round:

- total findings
- verified findings
- false-positive rate
- closure-regression rate
- duplicate-finding rate across reviewers
- time to close verified findings
- clean-round count required to converge
- reviewer-overlap matrix by finding class

Useful comparative studies:

- single-model / single-UI baseline
- multi-model / single-UI
- single-model / multi-UI
- multi-model / multi-UI

## BigBounce-Derived Evidence To Preserve

If this becomes a paper, the BigBounce campaign should be treated as the motivating case study, not as proof by anecdote.

Evidence worth preserving:

- review rounds and timestamps
- source/version hashes
- truth-audit classifications
- closure commits
- repeat-finding patterns
- cases where one reviewer family caught something others missed
- cases where UI changes appeared to alter reviewer strictness or independence

## Threats To Validity

The honesty section should explicitly discuss:

- prompt non-equivalence across interfaces
- reviewer contamination from prior context
- selection bias in which rounds were preserved
- operator steering effects
- model updates over time
- cost/latency tradeoffs
- publication bias toward dramatic catches

## Minimal Artifact Ledger

A serious protocol draft should preserve, per round:

```text
artifact_id
source_commit
rendered_artifact_hash
reviewer_id
model_family
ui_surface
prompt_template_id
finding_count
truth_audit_outcomes
closure_commit
confirmation_round_id
```

## Suggested Paper Structure

1. Motivation
2. Why single-loop review is failure-prone
3. Protocol definition
4. BigBounce case-study dataset
5. Metrics and evaluation design
6. Ablations
7. Threats to validity
8. Operational guidance and cost envelope
9. Limitations and non-claims

## Operational Rules For Future Use

- Reviewers do not get merge authority.
- Closure agents do not invent new reviewer claims during closure.
- Truth audit is the only place that converts findings into factual decisions.
- Public readiness changes require a clean confirmation pass, not just a patch wave.

## Non-Claims

This draft does **not** claim:

- that multi-model review is always better
- that multi-UI diversity alone guarantees independence
- that BigBounce results are generalizable without ablation
- that any particular vendor stack is required

## Next Research Step

If Houston wants this formalized later, the next step is to assemble a compact dataset of preserved review rounds and truth-audit outcomes from BigBounce into a method-note evidence bundle without changing any current paper or site artifact.
