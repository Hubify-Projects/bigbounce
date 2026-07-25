# Pattern 078 — A companion's status goes stale the moment it is archived

**Class:** cross-paper-consistency
**First observed:** 2026-07-20/21 (P5 → P4), re-fired 2026-07-24 (P5 → P2, P2 → P1A)
**Enforcement:** EXECUTABLE — `tools/verify_companion_status.py`, wired into
`tools/bigbounce_preflight.py` as the `companion-status` portfolio validator, so a
stale companion claim fail-closes review dispatch exactly like any other preflight
failure. Ledger: `project-context/companion-status-ledger.json`. Regression tests:
`tools/tests/test_verify_companion_status.py`.

## Observation

The six papers cite each other as companions. Every companion description is
written once, at the time the companion is unpublished, and then never revisited.
As each companion is archived with a resolvable DOI, every OTHER paper's
description of it silently becomes false — the manuscripts keep saying "in
preparation", "forthcoming", "not yet a verified public preprint", or
"[arXiv:XXXX.XXXXX --- ID inserted at coordinated submission]" about a document
that is now permanently archived and citable.

Two properties make this class survive ordinary review:

1. **It is a NEGATIVE-space defect.** Nothing in the paper changed. The world
   changed. Diff-driven review never looks at it, and the author-agent that
   published the companion is not the author-agent that maintains the citing
   paper.
2. **It lives in the BIBLIOGRAPHY, not the prose.** Every instance found so far
   sat in a `.bib` entry's `journal`/`note` field or in an inline `\bibitem`
   title. Sweeps written as `.tex`-body greps are structurally blind to it. On
   2026-07-24 a lane closed this exact defect in P5's body text and left an
   untouched instance ten lines away in the same file's bibliography.

Firings to date, all caught by accident rather than by a gate:

| Citing paper | Location | Described | Reality at the time |
|---|---|---|---|
| P5 | body prose (multiple sites) | P4 "companion manuscript in preparation" | archived 2026-07-20, DOI 10.5281/zenodo.21461899 |
| P5 | `\bibitem{golden_fnl_2026}` | P2 "in preparation; manuscript in preparation" | archived 2026-07-20, DOI 10.5281/zenodo.21461881 |
| P2 | `focused_paper_refs.bib` → rendered Ref. [14] | P1A `journal = "(in preparation)"` | archived 2026-07-22, DOI 10.5281/zenodo.21481838 |
| P1A | `arxiv/references.bib` (latent, uncited) | five companions "posted concurrently on arXiv [arXiv:XXXX.XXXXX]" | no paper in the portfolio has an arXiv ID |

## Sub-pattern 078b — the stale citation carries a RETRACTED value

The P5 → P2 bibliography entry did not only misstate availability. Its title
carried `f_NL = -35/8`, the value P2 itself spends an appendix disowning (P2's
result is `-35/16`). That upgrades the class from presentation to **correctness**:
one of our own papers cited a companion by a number the companion explicitly
retracts. A referee who follows the citation finds the contradiction immediately.

Beware the symmetric error: `-35/8` legitimately appears in historical and
comparative discussion ("the result corrects the unreproduced printed −35/8
literature value" of Cai et al. 0903.0631). That usage is CORRECT and must be
preserved. Only an occurrence presented as the companion's own current result is
a defect.

## Rule

1. Publishing any companion is a **portfolio-wide event**. In the same wave that
   mints a DOI, sweep every other paper's live source — body prose, `.bib`
   sources, generated `.bbl`, and every `\bibitem` field — and re-point each
   description at the archived record.
2. **Cite what actually resolves.** Use the archived record's exact title, its
   version DOI, its concept DOI, its deposit date, and its license. The archived
   title often differs from the in-repo working title (P1A's and P2's both do),
   and using the in-repo title is how a superseded value survives in a citation.
3. **Never upgrade the claim.** A Zenodo deposit is a public permanent archive.
   It is NOT peer review and NOT an arXiv preprint. Every rewritten reference
   must keep saying so. Over-correcting this defect into "published" is a worse
   defect than the staleness.
4. **Statements that are still true stay.** P5 has no DOI; no paper in the
   portfolio has an arXiv identifier; no paper has been refereed. Those
   statements are accurate and must never be "fixed."
5. Historical `%` comments, `\begin{comment}` blocks, and `\iffalse` blocks are
   the changelog. They record what was true then and are never edited.

## Enforcement (why this entry is not prose-only)

`tools/verify_companion_status.py` parses each of the six papers' LIVE source
(comments and comment environments stripped), extracts every bibliography surface
— inline `\bibitem` blocks plus every live-cited entry of every resolved `.bib`
and `.bbl` — and cross-references them against
`project-context/companion-status-ledger.json`. It fails when:

- **`companion-status`** — a live reference to a companion that HAS a published
  DOI carries an unpublished-status phrase, or a bibliography entry for such a
  companion does not print the DOI.
- **`superseded-value`** — a live reference to a companion states a value that
  companion has superseded, with no legitimate-attribution marker on the line.

Both rules are ledger-driven, so **filling in P5's `published_doi` after the
deposit is published arms every check for P5 with no code edit**, and retiring a
future value is a data edit. The ledger validator itself refuses to accept a
peer-review or arXiv-preprint phrase into the status list, so the gate can never
be turned into a lever for overclaiming.

Run it standalone with `python3 tools/verify_companion_status.py`; it runs
automatically inside `python3 tools/bigbounce_preflight.py run --receipt <path>`.
