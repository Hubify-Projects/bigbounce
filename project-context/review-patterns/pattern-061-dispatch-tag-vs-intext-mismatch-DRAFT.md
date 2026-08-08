---
pattern_id: 61
status: draft
first_seen: R52 (2026-06-26)
papers_observed: [P1A, P1B, P4, P5]
finding_count: 6
proposed_by: r-round-pattern-mine 2026-06-26
---

# pattern-061: dispatch-tag-vs-intext-mismatch

**Description**: The dispatch brief / orchestrator summary carries a vendor recommendation
label that does not match the vendor's own in-text Recommendation line. The mismatch can
run in either direction: the dispatch may be HARSHER than the in-text verdict (P4: o3
dispatch "REJECT", in-text "MAJOR REVISIONS") or SOFTER (P1A/P1B/P5: OpenAI+Gemini
dispatch "accept", in-text "MAJOR REVISIONS").

**Root cause**: The orchestrator extraction step reads a top-level tag from the reviewer
output rather than the explicit "Recommendation:" line inside the body. The two can
diverge when a reviewer's cover-note or JSON wrapper uses a coarser category than the
nuanced text inside.

**Evidence (R52)**:
- P4: OpenAI/o3 dispatch tag "REJECT"; body says "MAJOR REVISIONS" — truth-audit: FALSE POSITIVE (o3 itself recomputed all scalars as correct).
- P1A: OpenAI labeled "accept" by dispatch; in-text: "MAJOR REVISIONS."
- P1A: Gemini labeled "accept" by dispatch; in-text: "MAJOR REVISIONS."
- P1B: OpenAI labeled "accept→MAJOR" (mismatch noted in the truth-audit header).
- P5: OpenAI labeled "accept" by dispatch; in-text: "MAJOR REVISIONS."
- P5: Gemini labeled "accept" by dispatch; in-text: "MAJOR REVISIONS."

**Why it matters**: Harsher-than-in-text dispatch labels cause the truth-audit to begin
with a REJECT framing that artificially pressures the auditor toward accepting the
REJECT. Softer-than-in-text labels cause genuine MAJOR signals to be wave-through as
ACCEPTs without per-finding triage.

**Detection rule (mechanical)**:
```bash
# After collecting vendor reports, grep each report body for the
# explicit Recommendation line and compare to the dispatch tag:
grep -i "recommendation:" <report.md> | head -5
# The dispatch tag must match this line, not the cover/wrapper label.
```

**Prevention**:
1. The orchestrator extraction step must read the **in-text Recommendation line** (regex: `Recommendation:\s*(ACCEPT|MINOR|MAJOR|REJECT)`), not the wrapper tag.
2. Truth-audit preamble must print both the dispatch label and the parsed in-text label side-by-side as a sanity check.
3. If the two disagree, use the in-text line as authoritative and flag the mismatch.

**Example sites**:
- P4 R52: dispatch "REJECT" / in-text "MAJOR REVISIONS" for OpenAI/o3.
- P5 R52: dispatch "accept" / in-text "MAJOR REVISIONS" for OpenAI and Gemini.

**Severity**: high — a REJECT dispatch from a false positive costs hours of unnecessary triage; a soft dispatch lets real MAJORs slip.
