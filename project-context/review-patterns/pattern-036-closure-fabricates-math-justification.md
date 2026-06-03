# Pattern 036 — Closure round fabricates a math/derivation justification instead of verifying it

**First seen**: P2 R3 closure of GEM-m1 ("basis justification gap") added a fabricated
"exactly six orbits / complete S3-symmetric set" justification at L225 + audit-trail
L43-46. Caught 6 rounds later by P2 R9 Gemini-M1 — 32 reviewer-passes missed it.
**Severity**: critical (a wrong derivation looks self-consistent to surface reviewers
because the closure prose internally justifies itself)
**Frequency**: 1 confirmed (P2). Watch for cross-paper occurrence next pattern-mine cycle.
**Detection**: a closure round responds to a "justification gap" finding by ADDING
math/derivation prose (orbit count, coefficient, symmetry argument, partition count,
representation-theory claim) rather than by either (a) citing an external derivation
or (b) re-running the derivation in-house and writing the verified result.
**Prevention**: when a closure inserts ANY new math claim, the closure MUST cite a
specific external source (paper + equation) OR include the derivation in an appendix.
Phrases like "yields exactly N" / "follows from / by symmetry" without a citation
or in-line derivation are red flags.

## Why it's the worst kind of regression

Pattern-008 covers closures that introduce *factual* errors caught the next round.
Pattern-036 is the *math* variant — and it's worse because:

1. Math claims look authoritative; reviewers without the in-house derivation can't
   easily falsify a phrase like "exactly six orbits" without doing the enumeration.
2. The closure prose internally cross-references itself, so the falsified justification
   appears to support the actual basis (which may itself be correct).
3. Each subsequent round of vendors reads the fabricated justification as part of the
   established paper state, so they miss it the same way the closure author missed it.

In the P2 case, the underlying 6-monomial basis is in fact the correct
matter-bounce-vertex restricted subset (Cai:2009fn Eq. 37). The science was fine. The
fabricated *completeness* claim at the closure layer was the only bug. But that bug
sat in the paper for 6 rounds.

## What it looks like

R3 finding: "Basis justification is missing — why these 6 monomials, not others?"

R3 closure (wrong): inserts at L225 —
> "The six-monomial basis is the *complete* set of fully S3-symmetric degree-9
> monomials in three wavenumbers; enumerating ordered partitions of 9 into three
> nonnegative parts and quotienting by S3 yields exactly six orbits, so the basis
> is fixed by symmetry."

The fabricated claim: 12 orbits, not 6. The phrase "yields exactly six" was invented
by the closure author to justify what was already there.

R9 (6 rounds later) Gemini-M1: "L225 claims complete S3-symmetric basis with exactly
six orbits, but enumeration gives 12 orbits — omitted: (8,1,0), (7,1,1), (6,2,1),
(5,3,1), (4,4,1), (3,3,3)."

## How to fix when caught

1. Read the closure round's edit + the round-N finding it was responding to.
2. If the closure added a math claim, verify the math claim independently.
3. If false, do NOT silently rewrite. Acknowledge the regression in the audit trail
   AND in the section commentary. (P2 v1.7.43 audit trail L43-46 follows this.)
4. Rewrite the section honestly — typically as "restricted subset selected by
   [physics criterion]" rather than as "complete set". Cite the physics criterion.

## How to prevent

`/never-fabricate-derivation` (proposed sibling skill): before any closure prose
edit that contains a math symbol, an orbit count, a partition count, a coefficient,
or a symmetry-argument verb ("yields", "follows from", "by counting", "by symmetry"),
the closure must:

- Cite a specific external reference (paper + equation), OR
- Include the derivation in an appendix, OR
- Limit the closure to phrasing-only changes (no new math content)

Add this to `/paper-pre-review-check`: regex sweep for closure-added math claims
without citations, flag for human review before committing.

## Cross-pattern interaction

- **Pattern-008 (closure-introduced regression)** is the broader parent — pattern-036
  is the math/derivation specialization.
- **Pattern-018 (mandatory pre-review)** would have caught this if the pre-review
  ran a derivation-verification step.
- **Pattern-031 (severity under-classification)** — vendor reviewers in R3-R8 did
  see L225 but didn't flag it as substantive because the prose looked authoritative.

## Mining note

If a second instance appears in a different paper at the next pattern-mine cycle,
promote the prevention layer to a hard gate inside `/paper-pre-review-check` and
`/bigbounce-post-bump-sync`.
