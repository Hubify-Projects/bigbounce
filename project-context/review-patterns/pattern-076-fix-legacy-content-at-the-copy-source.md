# Pattern 076 — Embedded legacy content must be fixed at the copy source

**Class:** content-pipeline
**First observed:** 2026-07-23 (galaxy-explorer quarantine framing reverted by prebuild copy)

## Observation
The modern explorer routes inline legacy HTML that a prebuild script copies
from repo-root sources into site/public/old/. Edits made to the copied files
were silently overwritten on the next build — the fix "landed" and then
un-landed.

## Rule
Before editing any asset under a directory populated by a build step, trace the
copy pipeline (grep package.json pre* scripts) and edit the SOURCE. Verify the
fix survives a clean rebuild, not just the working tree.
