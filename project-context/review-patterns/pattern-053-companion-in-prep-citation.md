---
pattern_id: 053
status: active
first_seen: R39conf-batch-truth-audit (2026-06-13)
papers_observed: [P1A, P1B, P5]
finding_count: 6  # ≥2 reviewers × 3 papers
proposed_by: r-round-pattern-mine 2026-06-13
---

# pattern-053: companion in-prep citation leak

**Description**: In-prep companion paper citations leak across multiple papers as body-text honorifics ("in preparation", "companion paper", "companion Paper~II"), creating reader-visible forward-references to unpublished work. This is distinct from the bibliography entry itself (which is correctly formatted with `\cite{Golden2026P*}` for forward arXiv ordering). The problem is when the body TEXT announces the companion status — external reviewers object to prose that leans on unpublished companions as load-bearing support.

**Evidence (R39conf)**:
- P1A line 681 region: companion paper referenced in prose with "in preparation" honorific; the result it supports is asserted as established rather than self-contained.
- P1B Table IV footnote: "companion Paper~II (in preparation)" used to defer a benchmark definition.
- P5 abstract + §VI: "companion (in preparation)" cited at a load-bearing claim in the abstract; self-contained argument not provided.

**Resolution**:
1. Drop "in preparation" honorifics from body text. `\cite{Golden2026P*}` for forward arXiv ordering is fine; the prose honorific is not.
2. For load-bearing numbers that come FROM a companion: either inline the derivation/result OR replace with a public anchor (arXiv preprint, public dataset, or explicit labeled-assumption tag).
3. Table "Verified Value" columns that source from a companion → rename "Reference value" and cite the public source.
4. The companion may appear in the References section as `in prep.` — this is acceptable; body-text usage as a load-bearing citation is not.

**Detection rule (mechanical)**:
```bash
grep -nE "(in preparation|companion (paper|work)|companion Paper~[IVX]+)" <tex> | grep -v '^[0-9]*:%'
```
False positives: legitimate bibliography entries (lines containing `\bibitem` or inside `\begin{thebibliography}`) — those are allowed. Flag only body-text hits.

**Severity**: medium (becomes high if the companion citation is the only support for a headline claim)

**Cross-reference**: pattern-006 (companion paper self-cite missing in-prep hedge) covers the opposite direction — pattern-006 requires the hedge in bib; this pattern-053 requires the hedge be REMOVED from body prose.
