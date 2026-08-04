# P3 public-ID recovery technical package receipt — v3.2.0-r17

Audited 2026-08-03. This evidence-bounded correction closes four exact-final
Codex findings without changing catalog membership: viewer captures are now
path/hash/status-bound; the 2,287 exclusions use their explicit 2,468-row
positional-parent denominator; the second `TARGETID` pass states its actual
tie keys; and checkpoint resume binds content hashes of all three inputs.

| Item | Binding |
|---|---|
| Source | `paper3_apjs.tex` · SHA-256 `2d5d56957ab73a3c24b2fdfab29c131384cd2964bea6847e80e7cccac78d7256` |
| Canonical / served PDF | pdfTeX build · SHA-256 `f587ba2449332b0be444281629b5d6cb994098acf7e9492e8ffa9b0676f31589` · MD5 `d19835c1c85c2425e3ad9f33078b51b5` · 496,563 bytes · 17 pages |
| Official class | `aastex702.cls` (AASTeX 7.0.2) · SHA-256 `0ee51ff72a4d0b608a1885e87cddad4bcb41efacb852889de97637671c74d8ad` |
| Exact source tar | `paper3_apjs_arxiv_v3.2.0-r17.tar.gz` · SHA-256 `c2d6f211d073b6d0c72e53d94c5b82f7aeb0017d3dc833520b3f2af992973beb` |

## Verification

`tools/directive_g.sh P3 v3.2.0-r17` passed source-version/date, leak gate,
pdfTeX compilation, retention before mirror, six byte-identical mirrors, and
Convex current-version read-back (row `k57ajj69vmt4nwpwekn8b3vcr18btxfs`).
The canonical PDF and every served r17 mirror have the canonical SHA-256 above.

The public-viewer replay passed all 20 target retrievals. Its machine-readable
audit now binds every retained PNG by repository-relative path, SHA-256, byte
size, and visual status; 18 are visually checked rendered spectrum/coordinate
captures, while `P3-DESI-000004` and `P3-DESI-000047` are hash-identical blank
captures. The r2 primary-release manifest and the r7 aggregate bundle were
rebuilt: its independent validator passes 181 rows × 43 columns, 170 core + 11
lower-confidence rows, and 2,267 warned auxiliary rows.

## LaTeX audit

The canonical log has 0 fatal errors, 0 undefined references/citations, and 0
overfull hboxes. All 8 declared `\artifact{}` targets exist. Every rendered
page (1–17) was visually reviewed: title block, text, tables, figures,
appendices, and audit matrix are legible with no clipping, overlap, or column
intrusion.

This is a public-ID recovery technical/data-note package only, not a core-six
paper, a replacement anomaly-science paper, a submission, or a readiness-status
change.
