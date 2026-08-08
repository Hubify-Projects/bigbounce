---
pattern_id: spattern-dead-hf-link
status: seeded
first_seen: P1-2026-06-19
proposed_by: site-cohesion-sweep 2026-06-19
---

# spattern-dead-hf-link — HuggingFace dataset or model link returns 404 / 403

## Defect

A paper's detail page, data-explorer page, or `papers.ts` record links a
HuggingFace dataset or model that returns HTTP 404 (repo deleted / renamed),
HTTP 403 (gated without the correct token), or a page that shows no matching
card/version. The link exists in the paper's external-artifacts list but the
resource is unreachable to a reader.

## How to detect

- Extract every HuggingFace URL from `papers.ts` artifact lists and from
  rendered paper detail pages.
- `curl -L -o /dev/null -w "%{http_code}" <url>` — any non-200 response is a
  hit. Also check that the HF repo card exists and the version/commit hash on
  the card matches the paper.

## Fix

- If the dataset/model is unpublished: flag as a Houston/publish-day gate
  (see `spattern-unpublished-hf-dataset`).
- If renamed: update the URL in `papers.ts` and in the paper's `\artifact{}`
  macro, recompile, re-mirror PDF.
- If deleted: restore via HF dataset restore UI or reupload; update URL once live.
