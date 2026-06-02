---
status: confirmed
proposed_by: r-round-pattern-mine
proposed_date: 2026-05-15
confirmed_date: 2026-06-02
review_target: catalog
source: P4-pattern-019 reproducibility-anchor-404
---

# Pattern 026 — Reproducibility-anchor URL returns 404 / 401 / 410

**First seen**: P4 v1.0.66 external 4-vendor round (2026-05-15) — B2, M12
flagged github.com/.../releases/tag/v1.0.66 URLs returning 404 (release tag
not pushed at submission time).
**Severity**: high (every external reviewer dead-ends; reproducibility
narrative collapses on first click)
**Frequency**: 4+ instances
- P4 v1.0.66: GitHub release-tag URLs 404 (B2, M12)
- P4 v1.0.66: HuggingFace dataset 401 Unauthorized (B23 in R42)
- P3 R42: Zenodo record URL stale (R2 audit)
- P5: arXiv companion-paper anchor 404 (intermittent across rounds)

**Detection**: WebFetch every URL in every .tex file. Status != 200 →
BLOCKER. Includes github.com/.../releases/tag/, github.com/.../tree/, github.com/.../blob/,
zenodo.org/record/, doi.org/, huggingface.co/datasets/, huggingface.co/models/.

## What it looks like

> P4 v1.0.66 B2 (Gemini Deep Research, REJECT-AND-RESUBMIT): "The 'Data and
> code availability' statement cites
> `https://github.com/Hubify-Projects/bigbounce/releases/tag/p4-v1.0.66`.
> This URL returns 404. The release tag is not pushed. Without this anchor,
> the paper's reproducibility claim is unverifiable; this is grounds for
> rejection at any reproducibility-aware journal."

## Truth-audit verdict

VERIFIED in all 4 instances. URLs in the .tex either had not been pushed
to GitHub yet (timing issue) or had been deleted in a later cleanup.

## Examples observed

(See "Frequency" list above.) Pattern is invisible to internal CCAI rounds
and to any PDF-only reviewer. Catchable only via WebFetch / curl during
pre-review.

## Root cause

Two write surfaces drift:
1. The .tex carries the URL the author intends.
2. The actual git remote does not yet have the release tag pushed (or
   GitHub release was deleted, or HF dataset was un-published).

There is no skill that verifies URLs in .tex resolve to 200 BEFORE
submission. Closure pipeline writes the URL, recompile pipeline embeds
it, mirror pipeline copies the PDF — none check that the URL works.

## Pre-review check

```bash
# Step 1: extract every URL from the .tex (and .bib)
grep -oE 'https?://[^ }"]+' <paper.tex> <paper.bbl> | sort -u > urls.txt

# Step 2: HTTP HEAD each URL, log non-200s
while read url; do
  code=$(curl -s -o /dev/null -w "%{http_code}" -L "$url")
  [ "$code" != "200" ] && echo "BLOCKER $code $url"
done < urls.txt

# Step 3: for github.com/.../releases/tag/, verify the tag exists via
#   `git ls-remote --tags origin <tag>` — release page can lag tag push
#   by minutes
# Step 4: for HF dataset/model, verify status is not "Gated" or "Private"
# Step 5: for Zenodo, verify the record has a published DOI
```

Standing rule: NO paper goes to external review until every URL in the
.tex AND .bib has returned 200 within the last 24 hours.

## Related patterns

- Pattern 021 (external-artifact-pdf-blind) — sibling: 026 is the
  HTTP-status side; 021 is the content-drift side. Same URL extraction,
  different check.
- Pattern 027 (headline-claim-without-on-disk-artifact) — sibling: 027
  is the on-disk version of 026 — file referenced from paper does not
  exist in the repo at the claimed path
- Pattern 011 (confabulated bib survives first draft) — citation-side
  404; 026 is artifact-side
