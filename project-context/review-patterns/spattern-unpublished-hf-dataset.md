---
pattern_id: spattern-unpublished-hf-dataset
status: seeded
first_seen: P1-2026-06-19
proposed_by: site-cohesion-sweep 2026-06-19
---

# spattern-unpublished-hf-dataset — Paper links a HuggingFace dataset/model that is still private

## Defect

The paper (or site artifact list) references a HuggingFace dataset or model
that exists but is set to private, so any unauthenticated reader lands on a
"This repository does not exist or is private" page. The paper cannot be fully
reproduced until the resource is made public.

## How to detect

- Fetch every HF URL listed in `papers.ts` artifact lists WITHOUT authentication
  (no `HF_TOKEN` header). HTTP 401 or a "private" HF page = hit.
- Cross-check the paper's Data Availability section: if it promises public
  access, a private repo is a BLOCKER for submission.

## Fix

- Make the HF dataset/model public in HuggingFace UI.
- OR if not yet ready for public release: mark as a publish-day hard gate in
  SSOT/queue.md and flag the paper's readiness as capped until resolved.
- Update `papers.ts` artifact visibility flag after going public.
