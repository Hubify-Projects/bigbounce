---
name: bigbounce-bump
description: Atomic Bigbounce paper version bump via the bigbounce MCP. Computes pdfMd5/pages/sizeBytes from the on-disk PDF, captures the current git HEAD as texCommit, and writes one paper_versions row to Convex. The site re-renders within seconds via Convex subscription — replaces the 5-file hand-edit (papers.ts version + lastUpdated + pdfMeta, live-status.ts version, .tex \date + \paperVersion). One command, one mutation, one commit.
---

# /bigbounce-bump <paper-slug> <new-version> [--changelog="..."]

Single atomic version bump. The structural fix for the "I forgot to update the site after pdflatex compile" drift Houston caught repeatedly.

## Usage

```
/bigbounce-bump paper-3 v3.1.70 --changelog="Five-α-grid Fisher refit landed; §pathc_caveats item (i) CLOSED via real computation."
```

## Behavior

1. Resolve paper slug → texPath, sitePdfPath via `bigbounce_get_paper`.
2. Read on-disk PDF at sitePdfPath; compute md5 + pages (via pdfinfo) + sizeBytes.
3. Resolve datestamp = today (ISO `YYYY-MM-DD`) unless `--date=...` override.
4. Resolve texCommit = `git rev-parse HEAD` from repo root.
5. Call `bigbounce_bump_paper_version` mutation.
6. Print the new paper state: computed-readiness, lastUpdated, etc.

## What this replaces

The previous flow (~6 manual edits per .tex bump):
1. Edit .tex `\date` line
2. Edit .tex `\paperVersion` macro
3. Compile via pdflatex (2-pass) + bibtex + pdflatex
4. Copy .pdf to site/public/papers/<slug>.pdf
5. Update site/src/data/papers.ts (version + lastUpdated + pdfMeta)
6. Update site/src/data/live-status.ts (version)
7. Sometimes update SSOT/paper-N/status.md

Post-bump: steps 1-4 still happen (the actual .tex + compile). Steps 5-7 collapse into the single mutation here.
