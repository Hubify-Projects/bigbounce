---
pattern_id: spattern-pdf-404-or-old-version
status: seeded
first_seen: P1-2026-06-19
proposed_by: site-cohesion-sweep 2026-06-19
---

# spattern-pdf-404-or-old-version — Linked PDF is missing or is an older version

## Defect

The PDF linked from a paper detail page, the papers list, or `site/public/papers/`
either returns HTTP 404 (file not deployed) or resolves but is an older version
(md5 does not match the canonical PDF from the most recent bump). A reader
downloads the wrong PDF.

## How to detect

- Canonical PDF md5 comes from `papers.ts` or the SSOT version-pin (pattern-047).
- `curl -L -o /tmp/test.pdf <pdf-url> && md5sum /tmp/test.pdf` — compare against
  canonical md5. Non-200 status or md5 mismatch = hit.
- Check BOTH the versioned filename (`paper_vX.Y.Z.pdf`) AND the canonical
  filename (`paper.pdf`) — both must resolve and be byte-identical.

## Fix

- Run `/bigbounce-paper-pdf-mirror` to re-sync the PDF from the canonical
  source into `site/public/papers/` with correct filenames.
- Push and verify with `curl -I` post-deploy.
- If the versioned filename is missing: add it in the same mirror commit.
