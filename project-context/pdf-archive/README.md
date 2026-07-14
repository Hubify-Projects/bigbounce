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
