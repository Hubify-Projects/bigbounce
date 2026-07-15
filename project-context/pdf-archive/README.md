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

## Historical Git backfill — staged

Historical retention is intentionally split into inventory and materialized
tranches:

```bash
python3 tools/pdf_version_retention.py --history-inventory --history-skip-page-count
python3 tools/pdf_version_retention.py --history-backfill --history-offset 104 --history-limit 5
```

The inventory ledger
`manifests/2026/07/20260714T235000Z-history-inventory-20260714-history.json`
enumerates every reachable Git PDF object/path row and classifies only
high-confidence six-paper manuscript paths for materialization. Its initial
coverage was 1,356 Git PDF object/path rows: 1,094 classified manuscript rows
and 262 visible but unclassified rows. The unclassified rows are not silently
discarded; they are retained in the ledger with reasons such as figure/render
artifact, archive self-reference, ambiguous paper hint, or no paper hint.

The first page-counted materialization proof is
`manifests/2026/07/20260715T004000Z-history-backfill-0104-0108-20260714-history.json`.
It verifies five historical P4 manuscript rows with SHA-256, MD5, source Git
blob, first-seen commit/timestamp, archive object path, hard-linked reference,
and page counts. A separate verifier checked all five references point to the
recorded object bytes and reported page counts 22, 24, 25, 22, and 21.

Full page-counted history backfill remains a staged archive job. Use
`--history-offset` and `--history-limit` in small chunks; non-dry-run
`--history-backfill` is required to record page counts and fails if
`--history-skip-page-count` is supplied. Fast inventory is acceptable for
coverage planning, but it is not a substitute for the page-counted backfill
manifests.
