# BigBounce PDF retention archive

This directory is the append-only byte archive for the six canonical paper
PDFs. It complements the mutable served mirrors and Git history; it does not
replace either one.

## Snapshot all six papers

Run this immediately before any compile/mirror operation that can replace a
canonical or served PDF:

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

## Current limitations / integration gate

`tools/directive_g.sh` currently overwrites mutable mirrors with `cp -f`. The
retention command must become its mandatory pre-compile/pre-mirror gate after
active concurrent paper edits settle. Until then, operators must run the
snapshot command explicitly. GitHub is not an independent immutable archive;
the manifests and objects should also be mirrored to versioned object storage
or a DOI archive without changing their paths or hashes.
