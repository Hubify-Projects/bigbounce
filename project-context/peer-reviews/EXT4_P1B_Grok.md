# EXT4 P1B — Grok Heavy (in-thread delta round 4)
**Chat**: https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=33f977da-4a3e-44b6-a6e4-599ae00d5c3e
**PDF**: paper1b_mcmc_companion_v1B.0.58.pdf (74e0cc28) · harvested 2026-06-11 15:56 PT · loc 33f977da
---
Thought for 15s

Referee Report: Paper 1B v1B.0.58 (revision of v1B.0.57)
MNRAS / PRD / JCAP target
Date: 11 June 2026

1. CLOSURE VERIFICATION (from v1B.0.57 report)

Original BLOCKERS (v1B.0.57): None → CLOSED (none existed).

Original MAJORS (v1B.0.57): None (prior report already recommended ACCEPT after the four MINORS) → CLOSED (N/A).

Original MINORS (v1B.0.57) – all four now verified CLOSED (complete and correct):

Data and Code Availability p. 12 (JSON bug disclosure): Now explicitly states the CORRECTED.json was “regenerated directly from the raw chains” with embedded provenance and S8 recomputation. CLOSED.
HuggingFace datasets paragraph: Direct URLs provided (with DOI assignment pending at submission); pinned to v1B.0.58 via CHANGELOG.md. CLOSED.
Sec. III p. 3 (one-sided ∆N_eff limits): Phrasing tightened and cross-referenced to raw-chain verification. CLOSED.
Table IV caption: Now ties “Internally verified” status explicitly to the v1B.0.58 version-stamp commit. CLOSED.

No PARTIAL, NOT ADDRESSED, or REGRESSION issues. All findings from the previous round are fully resolved.

2. FRESH PASS (new findings only)

I have re-read the full revised PDF end-to-end (all 19 pages of v1B.0.58). The manuscript is now at an exceptionally high standard of transparency and self-consistency. Every prior comment has been actioned with precision (raw-chain regeneration statements, PR3/PR4 scoping clarification, exploratory w0wa reframing, updated HuggingFace URLs, and CORRECTED.json provenance). No new BLOCKERS or MAJORS.

MINORS (polish only – extremely minor)

Data and Code Availability p. 12 (HuggingFace paragraph): The URLs are now live and correctly formatted, but the sentence “DOI assignment is pending (identifiers will be inserted at submission)” appears in both the main text and the Appendix A repeat. This creates a redundant forward-reference that could be misread as incomplete at preprint stage.
Proposed fix: Consolidate to a single sentence in the main Data and Code Availability section only: “HuggingFace dataset URLs (DOI assignment pending at journal submission) are listed in Appendix A and recorded in CHANGELOG.md under v1B.0.58.”
Abstract footnote a (PR3/PR4 disambiguation): The new clarification is welcome and precise, but the phrase “the ALP MCMC uses only the scalar Gaussian summary likelihood … and does not depend on the PR3/PR4 map-level distinction” is technically accurate yet slightly repetitive with the main-text footnote on p. 9.
Proposed fix: Trim the abstract footnote to “(the ALP MCMC uses only the scalar Gaussian summary likelihood β = 0.342° ± 0.094° and is insensitive to the PR3/PR4 map-level distinction except through the provenance of that summary value)” and retain the fuller explanation on p. 9.
Sec. VII p. 11 (exploratory w0wa cross-check): The new sentence is helpful, but “Exploratory w0wa cross-check” appears only in the conclusions while the full caveat (queued SN-overlap chains) is in Sec. III(e). A reader skimming conclusions may miss the qualification.
Proposed fix: Add a parenthetical cross-reference: “…an exploratory, overlap-uncorrected test of the quintom-B scenario [19] (see Sec. III(e) for the queued SN-overlap control chains).”
Table IV p. 19 (Claims Classification note): The note is excellent but the phrase “a public tagged release pinning all of these artifacts to a single immutable snapshot is pending” could be tightened for journal style.
Proposed fix: Change to “(a public tagged GitHub release and HuggingFace DOI snapshot pinning all artifacts to v1B.0.58 is pending at journal submission; see Data and Code Availability).”

These are purely editorial and do not affect any scientific claim, numerical result, or reproducibility statement.

3. UPDATED RECOMMENDATION

ACCEPT (after the four minor polish items above).

The paper has moved decisively to full publishability. All prior comments have been resolved with exemplary transparency, and the new changes (raw-chain provenance, PR3/PR4 scoping, exploratory w0wa framing) further strengthen an already outstanding technical companion. It is now ready for immediate publication in MNRAS/PRD/JCAP. I do not require re-review.
