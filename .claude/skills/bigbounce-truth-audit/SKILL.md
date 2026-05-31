---
name: bigbounce-truth-audit
description: Apply truth-audit verdict (VERIFIED / FALSIFIED / STALE / OUT-OF-SCOPE / OPINION) to an open Bigbounce R-round finding via the bigbounce MCP, per feedback_peer_review_truth_audit_protocol. REQUIRED before /bigbounce-close. The MCP enforces verdict-first ordering — closing a finding without a verdict is rejected at the mutation layer. Evidence string MUST cite a .tex line / artifact / paper section that justifies the verdict.
---

# /bigbounce-truth-audit <findingId> <verdict> <evidence>

Implements the truth-audit step from `feedback_peer_review_truth_audit_protocol`: reviewers over-call severity on stale / mislabeled / missing artifacts, so every finding gets a verdict-first audit before closure work.

## Verdicts

- **VERIFIED** — reviewer's claim is accurate. Real-action closure needed (or genuine-deferral with explicit Houston OK).
- **FALSIFIED** — reviewer's claim is wrong (e.g. cited line doesn't exist, or arithmetic the reviewer flagged is actually correct). Close with `--method=truth-audit-falsified`.
- **STALE** — claim was true earlier but already closed in a prior version. Close with `--method=truth-audit-falsified` referencing the prior closure commit.
- **OUT-OF-SCOPE** — beyond what THIS paper claims; valid critique but doesn't apply.
- **OPINION** — stylistic / preference, not a defect. Close with `--method=truth-audit-falsified`.

## Usage

```
/bigbounce-truth-audit finding:k57z8h2 VERIFIED "L310 has 'σfnl = 8.27' as live body text matching the retracted form — fix needed"
/bigbounce-truth-audit finding:abc123 FALSIFIED "Reviewer claimed Eq.5 dimensional mismatch; grep shows the units balance per §III.B derivation"
/bigbounce-truth-audit finding:def456 STALE "Closed in v3.1.56 commit 12e79434; reviewer reading stale prompt"
```
