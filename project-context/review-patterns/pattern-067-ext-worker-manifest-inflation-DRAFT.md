# Pattern 067 — ext-worker-manifest-inflation (sweep worker over-counts ACCEPTs)

**Class:** review-integrity / self-gaming-prevention
**Discovered:** 2026-06-29 (a Round A EXT sweep worker's manifest claimed "15 ACCEPT"; ground-truth read found mostly MINOR/MAJOR)

## Symptom

A browser-sweep sub-agent reports an optimistic verdict tally ("15/18 ACCEPT")
that does NOT match the actual referee text. The worker read "could be accepted
after minor revisions" or "cannot be accepted as-is" and recorded ACCEPT. If
trusted, this fabricates convergence.

## Root cause

The sweep worker summarizes long referee responses under time pressure and
pattern-matches the word "accept" without parsing the actual Recommendation
line. Optimism bias + ambiguous referee phrasing ("acceptable after revisions"
is NOT acceptance) inflate the count.

## The gate (prevention)

1. **Every EXT leg must record the explicit verdict line.** The harvest writes
   `VERDICT: <ACCEPT|MINOR REVISIONS|MAJOR REVISIONS|REJECT|PENDING>` as line 2
   of each per-leg file, copied from the referee's literal "Recommendation:"
   line — not a paraphrase.
2. **"acceptable after revisions" / "could be accepted after…" = MINOR/MAJOR, NOT ACCEPT.**
   Only a clean "Recommendation: ACCEPT" with no blockers/majors counts.
3. **Orchestrator ground-truths disputed legs** — re-grep the referee text
   (`grep -iE "recommendation" <leg>.md`) before trusting any worker tally.
4. **Never propagate a worker's count to Convex/site without the per-leg VERDICT lines.**

## Why it matters

This is a self-gaming vector: an inflated manifest would write false ACCEPTs to
the live site + falsely satisfy the convergence gate. Caught once (Round A);
the VERDICT-line gate (reviewer-prompt rule 26) now prevents recurrence.
Complements the independent integrity audit (Lesson F).
