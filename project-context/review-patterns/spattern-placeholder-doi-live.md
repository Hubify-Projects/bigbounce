---
pattern_id: spattern-placeholder-doi-live
status: seeded
first_seen: P1-2026-06-19
proposed_by: site-cohesion-sweep 2026-06-19
---

# spattern-placeholder-doi-live — Live site or paper shows a TODO/placeholder DOI or arXiv ID

## Defect

The live site or the deployed paper PDF shows a DOI, arXiv ID, or Zenodo link
that is a placeholder (`TODO`, `TBD`, `XXXX`, `0000.00000`, or a syntactically
valid but unresolvable identifier). The paper has been bumped and mirrored but
the DOI/arXiv submission step has not happened or has not been propagated back
into the site data. Closely related to `ppattern-unminted-doi-placeholder` but
caught at the live-site sweep stage rather than during the packaging round.

## How to detect

- Grep rendered HTML of every paper detail page and the papers list for known
  placeholder patterns: `TODO|TBD|XXXX|arXiv:0000|10\.0000/`.
- Fetch the paper PDF and grep for the same patterns in the title block.
- Attempt to resolve each non-placeholder DOI/arXiv ID via `curl`; any 404 is
  also a hit (minted but mis-typed).

## Fix

- If the DOI/arXiv ID has been assigned: update `papers.ts` with the real
  identifier, recompile the paper to embed it, re-mirror the PDF, push.
- If not yet assigned: flag as a Houston/publish-day hard gate in SSOT/queue.md;
  do NOT let the placeholder appear on the live site — hide the field until
  real.
