# Pattern 079 — A served PDF outside the registered mirror set is invisible to directive G

**Class:** served-surface-integrity
**First observed:** 2026-07-24 (four independent accidental catches in one day)
**Enforcement:** EXECUTABLE — `tools/verify_pdf_mirror_integrity.py`, wired into
`tools/bigbounce_preflight.py` as the `pdf-mirror-integrity` portfolio validator, so a
stale served PDF or a stale site reference fail-closes review dispatch exactly like any
other preflight failure. Policy data: the `served_pdf_policy` and `companion_manuscripts`
blocks of `project-context/paper_registry.json`. Regression tests:
`tools/tests/test_verify_pdf_mirror_integrity.py`.

## Observation

Directive G is a **forward-only** guarantee. Per round, per paper, it takes the freshly
compiled PDF and pushes it out to that paper's *known* mirror paths, enumerated in
`tools/directive_g.sh` as `SERVED_ROOTS` × (canonical basename + registry
`served_aliases` + versioned alias). Every one of those targets is verified byte-identical.

Nothing walked the served tree in the other direction. A `.pdf` under `public/` or
`site/public/` that is not in *any* paper's registered mirror set is outside directive G's
universe entirely: it is never compared to anything, never re-mirrored, never noticed. It
keeps serving whatever bytes it had the day it was written. The registry's alias list is
the map, and directive G only ever walks the map — it never audits the territory.

The territory is much bigger than the map. Two concrete gaps:

- **`SERVED_ROOTS` is not the set of served roots.** It contains `public/papers` but not
  bare `public/`, and `site/public` but not `site/public/arxiv_v2` or `*/downloads`. A
  registered alias sitting one directory up from a mirror root is untouched forever.
- **A basename nobody claims is nobody's problem.** `paper3_draft.pdf`,
  `anomaly_catalog_paper.pdf`, `spin_torsion_paper1.pdf`, `bigbounce_latest.pdf` — all
  former canonical names of papers that were later renamed. Once the registry moved to
  the new name, the old file stopped being anyone's mirror and froze.

The symmetric failure lives on the reference side. `site/src/data/papers.ts` names the
served PDF by version-pinned filename. A version bump mirrors the new file correctly and
leaves `papers.ts` pointing at the previous one — the link resolves, returns HTTP 200, and
serves superseded science. **A link to a real-but-stale file is exactly as bad as a dead
one, and strictly harder to notice**, because every dead-link sweep passes.

Firings on 2026-07-24, all found by accident by four different agents:

| # | Instance | Real content | Why directive G missed it |
|---|---|---|---|
| 1 | `site/public/focused_paper_bounce_fnl_forecast.pdf` | P2 build from 2026-07-10 | alias present at a root outside the per-paper mirror set |
| 2 | `public/focused_paper_bounce_fnl_forecast.pdf` | P2 v1.7.110, superseded title | bare `public/` is not in `SERVED_ROOTS` |
| 3 | sibling leftovers reported alongside #2 | assorted retired lineages | basenames no paper claims |
| 4 | `site/src/data/papers.ts:314-315` | P3 pinned at `v3.2.0-r13` after r14 landed | forward direction only; no reference audit at all |

Four accidental catches is the signal, not the finding. A defect class that four
independent agents stumble into in one day has instances nobody stumbled into. The first
full reverse sweep found **31** orphan served PDFs and **stale references for 6 of 6
papers** in `papers.ts` (href, `version` field, and `pdfMeta` md5) plus 6 of 6 in
`live-status.ts` — the r13/r14 case was one visible corner of a systemic gap.

This is the mechanical root of Houston's single loudest, most-repeated complaint about
the program: the public site silently serving stale or inconsistent state.

## Sub-pattern 079b — retention is not the defect

`..._v1.7.126.pdf` and its ~1,050 siblings are **append-only evidence** under PUB-005 and
must never be deleted. A gate that flags retention as clutter will be turned off, and the
one after it will be too. The rule has to distinguish a version-pinned archive (correct,
permanent) from an unversioned served copy that has drifted (defect), and only ever fail
on the second. Retention must be cheap and quiet; drift must be loud.

## Rule

1. **Every `.pdf` under a served root must be accounted for.** Exactly one of: a
   byte-identical current mirror of a registry paper or registered companion; a
   version-pinned immutable archive; a declared non-manuscript asset (figures); or an
   explicitly dispositioned retired entry. Anything else is a defect.
2. **Deleting a stale served copy is the default fix; adding it to the mirror set is the
   alternative.** Pick one and record it. Never leave the file with no owner. If the bytes
   exist at no version-pinned path, capture them with
   `tools/pdf_version_retention.py` *before* removing the served copy — the disposition for
   that case is `archive-then-remove`, not `remove`.
3. **A known orphan stays a failure until it is gone.** A `retired_served_pdfs` entry with
   disposition `remove` / `archive-then-remove` is a *recorded open defect*, not an
   exemption. Only `retain` passes. Cataloguing an orphan must never be a way to make it
   permanent.
4. **Every reference to a served PDF must resolve AND be current.** A version-pinned href
   in `papers.ts`/`live-status.ts` must point at bytes identical to the paper's canonical
   PDF. The `version` field and the `pdfMeta` md5 in the same record are the same claim in
   prose and must agree — a stale version label is the same lie, told twice.
5. **Historical link surfaces are exempt from currency, not from existence.**
   `reviewTimeline.ts` deliberately links past versions; those must keep resolving, which
   is another reason PUB-005 archives are never deleted.
6. **Version-pinned archives are audited for one thing only:** an archive named for a
   paper's *current* version must carry that version's bytes. Otherwise retention is left
   alone.

## Enforcement (why this entry is not prose-only)

`tools/verify_pdf_mirror_integrity.py` closes the loop from both ends. It enumerates every
**git-tracked** `.pdf` under the policy's `served_roots` (tracking is what keeps build
output and ignored trees out of scope), hashes each one, and classifies it against the
canonical PDFs read live from `project-context/paper_registry.json`. Then it parses each
declared site data source and checks every `/papers/*.pdf` reference for existence and,
on `current-paper-artifacts` surfaces, for currency.

Reverse-direction rules:

- **`unregistered-orphan-pdf`** — served, matches no current PDF, not version-pinned, no
  disposition.
- **`mirror-bytes-stale`** — the path uses a paper's canonical basename or a registered
  alias, but its bytes are not that paper's current PDF: directive G never reached it.
- **`retired-served-pdf-still-present`** — a dispositioned orphan is still served.
- **`stale-retired-entry`** / **`retired-entry-contradicts-current-mirror`** — the ledger
  itself has drifted from reality.
- **`archive-version-collision`** — an archive pinned to a paper's current version does not
  carry that version's bytes.

Forward-direction rules:

- **`site-reference-missing`** — a referenced served PDF does not exist.
- **`site-reference-stale`** — it exists but is a superseded build (the r13/r14 defect).
- **`site-version-field-stale`** / **`site-pdfmeta-md5-stale`** — the record's declared
  version or advertised md5 disagrees with the canonical source.

Everything is data-driven from `served_pdf_policy`, so **adopting an alias, adding a
paper, registering a companion manuscript, or dispositioning a retired file is a data
edit, never a code edit** — the same property that makes the pattern-078 ledger safe. The
policy validator refuses unsafe or non-normalized paths, refuses a retired path outside a
served root, refuses an unknown disposition, and refuses to retire a path that is
currently a live mirror.

Run it standalone with `python3 tools/verify_pdf_mirror_integrity.py`; it runs
automatically inside `python3 tools/bigbounce_preflight.py run --receipt <path>`, and its
result — including the `inventory_sha256` over the sorted `(path, md5)` list of the whole
served tree — is hash-bound into the portfolio receipt, so a served PDF cannot change
after a receipt is issued without invalidating it.
