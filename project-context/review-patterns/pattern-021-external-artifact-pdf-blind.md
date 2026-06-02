---
status: confirmed
proposed_by: r-round-pattern-mine
proposed_date: 2026-04-30
confirmed_date: 2026-06-02
review_target: catalog
merges: [R42-NEW-021 external-artifact-contradicts-paper, P4-pattern-021 offsite-artifact-card-drift]
---

# Pattern 021 — External artifact contradicts paper (PDF-only reviewers blind)

**First seen**: P1 R42 R2 reviewer (the only reviewer with curl-access) flagged
four issues no other R42 reviewer could see.
**Severity**: high (BLOCKER-grade; invisible to all internal reviewers who
work from the PDF only)
**Frequency**: 6+ observed across 3 papers
- P1 R42: convergence_latest.csv R-hat contradicts "publication-quality" (B6)
- P4 R42: HuggingFace model card "26,626 galaxies" vs paper "26,636" (B22)
- P4+P3 R42: HF dataset 401 Unauthorized vs paper "publicly available" (B23)
- P2 R42: SPHEREx launched 2026-03 vs paper "first science 2028" (M7)
- P4 v1.0.66: HF dataset card schema drift vs paper methods (B4, B5)
- P4 v1.0.66: GitHub README pipeline commands drift vs paper algorithm

**Detection**: every cited external artifact (GitHub repo, HF dataset/model card,
Zenodo record, NASA-JPL launch status, survey timeline page) must be fetched
during pre-review and diffed against the paper claim.

## What it looks like

> R42 R2 B22: Paper says training set = 26,636 galaxies. HuggingFace model
> card at huggingface.co/Hubify/spiralnet states 26,626 galaxies. Either the
> card is stale OR the paper N is wrong. Diff is 10 — likely a 26,636-vs-
> 26,626 typo, but you cannot tell from the PDF.

> R42 R2 B23: Paper §IX states dataset "publicly available at huggingface.co/
> datasets/Hubify/spiralcat". HEAD on that URL returns 401 Unauthorized. The
> dataset is either private, deleted, or behind a gated-access flag.

> P4 v1.0.66 B4: HF dataset card README claims columns {ra, dec, p_cw, p_ccw,
> p_notspi}. paper §V.B Table 2 schema includes additional "confidence" and
> "morphology_class" columns. Card or paper is stale.

## Truth-audit verdict

VERIFIED in 5 of 6 cases; the sixth (P3 SPHEREx) was VERIFIED as a timeline
update that paper had not absorbed.

## Examples observed

(See "Frequency" list above.) Pattern is structurally invisible to any
reviewer who lacks live web/HTTP access — every Claude-Code internal sub-agent
fails, GPT/Gemini without browsing fails. Only Perplexity, Gemini-with-tools,
and reviewers Houston shares with externally have a chance.

## Root cause

Two write surfaces drift independently:
1. Paper .tex updated during closure
2. External card (HF/Zenodo/GH README) updated by a separate workflow
   (or NOT updated)

There is no skill that re-renders the cards from the paper, and no skill
that verifies the cards match the paper on every version bump.

## Pre-review check

```bash
# Step 1: extract every external URL from the .tex
grep -oE 'https?://[^ }"]+' <paper.tex> | sort -u > urls.txt

# Step 2: for each URL, fetch and diff vs paper claim
for url in $(cat urls.txt); do
  curl -sI "$url" | head -1     # status check
  curl -s "$url" | <extract relevant content>
  # Compare to paper claim for the same artifact
done

# Step 3: specifically for HF/Zenodo/DOI/release-tag URLs:
#   - WebFetch + content-hash compare to paper schema/N/methodology
#   - status != 200 → BLOCKER (covered also by pattern-026 anchor-404)
#   - card content drift vs paper → BLOCKER (this pattern)
```

Standing rule: NO paper goes to external review until ALL cited external
artifacts have been re-fetched within the last 24h and verified consistent.

## Related patterns

- Pattern 026 (reproducibility-anchor-404) — sibling: HTTP status side
  (404/401/410). Pattern 021 is the content-drift side; 026 is the
  existence side. Both run from the same URL-extraction list.
- Pattern 027 (headline-claim-without-on-disk-artifact) — sibling: on-disk
  side instead of off-disk side
- Pattern 002 (dataset attribution drift) — citation-string drift; pattern
  021 is artifact-content drift
