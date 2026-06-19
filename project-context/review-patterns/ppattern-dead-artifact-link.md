---
pattern_id: ppattern-dead-artifact-link
status: seeded
first_seen: P1-2026-06-19
papers_observed: []
proposed_by: paper-packaging-round 2026-06-19
---

# ppattern-dead-artifact-link — \artifact{} or repo URL in paper does not resolve

## Defect

A link in the paper — `\artifact{}` macro, `\url{}`, or a GitHub/Zenodo URL —
resolves to a 404, 401, 410, or redirects to a wrong resource on the committed
default branch. The paper ships with a broken reproducibility anchor. Readers
and referees who click the link find nothing.

Common causes: file moved or renamed after the paper was written; branch changed
from `main` to `master` (or vice versa); file deleted in a cleanup commit; Zenodo
DOI not yet minted; GitHub URL uses `/blob/` for a directory (should be `/tree/`).

## How to detect

Run `/artifact-link-verify` before every P-round close:
```bash
# Extract all URLs from the .tex
grep -ohE 'https?://[^\s}\\]+' paper.tex > urls.txt

# Curl-check each
while read url; do
    code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
    [ "$code" != "200" ] && echo "DEAD $code $url"
done < urls.txt
```

Also check `\artifact{}` paths resolve on the committed default branch HEAD.

## Fix

For each dead link:
- If the file moved: update the URL in the paper to the new path.
- If not yet committed: commit the file to the repo at the stated path.
- If Zenodo DOI not yet minted: mint the release and update the URL.
- If `/blob/` vs `/tree/` mismatch: fix to `/tree/` for directories.
- Rerun `/artifact-link-verify` and confirm 200 on every URL before P-round close.
