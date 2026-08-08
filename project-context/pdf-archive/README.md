# BigBounce PDF retention archive

This directory is the append-only byte archive for the six canonical paper
PDFs. It complements the mutable served mirrors and Git history; it does not
replace either one.

## Snapshot all six papers

Use the direct command for a complete six-paper baseline or an explicit manual
snapshot. Normal per-paper publication runs are retained automatically by
`tools/directive_g.sh` as described below.

```bash
python3 tools/pdf_version_retention.py
```

The command reads each source PDF once and creates:

- one immutable object at `objects/sha256/<prefix>/<sha256>.pdf` for each
  distinct byte sequence;
- one immutable, human-readable hard link under `refs/<paper-ID>/` whose name
  includes paper ID, manuscript version, Pacific timestamp, and short SHA-256;
- one unique JSON manifest under `manifests/YYYY/MM/`, recording paper ID,
  manuscript version, UTC and Pacific timestamps, SHA-256, MD5, page count,
  byte size, source paths, optional repeatable build command/review round, Git
  HEAD/blob/staged/unstaged state, and legacy-path recoverability.

Existing objects are verified and deduplicated. Existing objects and manifests
are never overwritten; corruption or a manifest-name collision fails closed.
Use `--dry-run` to inspect the proposed manifest without writing anything, or
`--paper P3` for a bounded single-paper snapshot.

The first contract-complete baseline is
`manifests/2026/07/20260714T204234Z-baseline-v3-20260714.json`. Earlier v1/v2
manifests are retained as an append-only implementation audit trail; they do
not contain the final page-count plus human-readable-hard-link contract.

## Directive-G integration gate — CLOSED

In normal mode, `tools/directive_g.sh` now calls
`tools/pdf_version_retention.py --paper "$PAPER"` after the compile/log audit
succeeds and before any served mirror or Convex mutation. The call records a
deterministic build description and `directive-g/<review-profile>/<paper>/<version>`
review identifier, validates the returned paper/version/metadata receipt,
prints the immutable manifest path, and fails closed before mirror discovery if
retention or receipt validation fails.

`--verify-only` explicitly skips the retention call, so validation runs do not
create archive objects, references, or manifests. They also retain the existing
no-remirror/no-Convex-mutation behavior.

The remaining release limitation is independent durability: GitHub is not an
immutable archive. Manifests and objects should also be copied byte-for-byte to
versioned object storage or a DOI archive without changing their paths or
hashes.

## Archive-then-remove retention (served orphans)

`tools/verify_pdf_mirror_integrity.py` classifies every git-tracked PDF under a
served root. Some orphans it finds are dispositioned `archive-then-remove` in
`project-context/paper_registry.json` because their bytes exist at **no**
version-pinned path — `snapshot` cannot reach them, since it is bound to the six
canonical manuscripts.

```bash
python3 tools/pdf_version_retention.py --retire-archive --dry-run
python3 tools/pdf_version_retention.py --retire-archive
```

The mode reads each such served path's exact bytes, fails closed if they do not
match the md5 the registry recorded, retains one object per distinct SHA-256
plus a `refs/<identified-paper>/` hard link, re-reads both and proves them
byte-for-byte, and writes a `...-retire.json` manifest listing every served path
that shared those bytes with its Git provenance. Only after that manifest exists
may the served copies be removed — AGENT_RULES §2.8 and `PUB-005`.

The first run was
`manifests/2026/07/20260725T024720Z-retire-orphans-20260724-retire.json`:
13 served paths, 5 distinct P1-LEGACY documents (33, 34, 34, 24, and 10 pages),
all five objects and references newly created and verified.

## Historical Git backfill

Historical retention is intentionally split into inventory and materialized
tranches:

```bash
python3 tools/pdf_version_retention.py --history-inventory --history-skip-page-count
python3 tools/pdf_version_retention.py --history-backfill --history-skip-page-count --history-offset 500 --history-limit 25
python3 tools/pdf_version_retention.py --history-backfill --history-offset 500 --history-limit 25
```

The inventory ledger
`manifests/2026/07/20260714T235000Z-history-inventory-20260714-history.json`
enumerates every reachable Git PDF object/path row and classifies only
high-confidence six-paper manuscript paths for materialization. Its initial
coverage was 1,356 Git PDF object/path rows: 1,094 classified manuscript rows
and 262 visible but unclassified rows. The unclassified rows are not silently
discarded; they are retained in the ledger with reasons such as figure/render
artifact, archive self-reference, ambiguous paper hint, or no paper hint.

The first page-counted materialization proof was
`manifests/2026/07/20260715T004000Z-history-backfill-0104-0108-20260714-history.json`.
It verifies five historical P4 manuscript rows with SHA-256, MD5, source Git
blob, first-seen commit/timestamp, archive object path, hard-linked reference,
and page counts. A separate verifier checked all five references point to the
recorded object bytes and reported page counts 22, 24, 25, 22, and 21.

The first full historical byte materialization was completed in chunked fast
mode on 2026-07-14/15 with run IDs matching
`history-backfill-fast-*`. Those manifests cover row offsets 0 through 1357
with no gaps, processed 1,095 classified manuscript rows, created 837 new
objects and 843 new references, and reported zero row errors. The archive then
contained 1,097 SHA-256 objects and 1,106 human-readable refs, with all 1,106
refs verified as hard links to matching objects.

Fast materialization records SHA-256 identity and first-seen Git provenance but
sets `page_counts_recorded=false`. Full page-count completion remains the next
bounded archive job: rerun `--history-backfill` without
`--history-skip-page-count` in small chunks to add page-counted manifests. The
archive objects and refs are already content-addressed, so those page-count
tranches should deduplicate existing bytes rather than create another copy.
