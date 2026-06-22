---
name: bigbounce-revision-tracker
version: 0.1.0
description: |
  Bigbounce-specific specialization of /revision-tracker-update. Binds the schema
  to project-context/peer-reviews/REVISION_TRACKER.md and to the 6-paper layout
  (P1A, P1B, P2, P3, P4, P5). Same workflow as the global skill but tied to this
  repo's file paths.
triggers:
  - bigbounce revision tracker
  - update peer review tracker bigbounce
---

# /bigbounce-revision-tracker — bigbounce peer-review tracker

**Source:** AGENT_RULES.md §4.5; `revision-tracker-update` (global parent)
**Scope:** bigbounce-only
**Trigger:** after every peer-review round closes in this repo

## What this skill does

Same workflow as `/revision-tracker-update` but bound to:

- **File**: `project-context/peer-reviews/REVISION_TRACKER.md`
- **Paper IDs**: P1A, P1B, P2, P3, P4, P5
- **Round file naming**: `project-context/peer-reviews/YYYY-MM-DD_HHMMtz_R{N}_{p-tag}_{vendor}.md`

## Schema (bigbounce-specific)

```markdown
# REVISION_TRACKER.md

## R28 — P1B v1B.0.22 — 2026-05-26

**Vendors:** gpt55, gemini25pro, grok4, perplexity-sonar, deepseek-v32
**Verdict:** 3 BLOCKER closed / 7 MAJOR closed / 2 MINOR open / 1 INCORRECT/STALE
**Bundle commit:** abc1234 — `chore(R28-stamp): bump paperVersion+date across 6 papers`
**SSOT update:** `SSOT/paper-1B/status.md` ✅

| # | Severity | Vendor | Section | Finding | Status | Commit |
|---|----------|--------|---------|---------|--------|--------|
| 1 | BLOCKER | gpt55 | §III.B | Equation 12 derivation step missing | CLOSED | def5678 |
| 2 | MAJOR | grok4 | abstract | Over-claim on σ(f_NL) detection significance | CLOSED | def5678 |
| 3 | … | … | … | … | … | … |
```

## Per-paper trackers

The master `REVISION_TRACKER.md` covers all papers. Per-paper detail lives in:
- `SSOT/paper-N/status.md` — close-the-gap list per paper
- `project-context/peer-reviews/<round-files>.md` — full per-round reviews

## Bigbounce paper IDs

| ID | Paper title | Canonical .tex |
|----|-------------|----------------|
| P1A | Spin-Torsion ECH No-Go | `arxiv/paper1a_ech_nogo.tex` |
| P1B | MCMC Companion | `arxiv/paper1b_mcmc_companion.tex` |
| P2 | f_NL Forecast | `research/focused_paper_source_integration/02_full_draft.tex` |
| P3 | Anomaly Catalog | `pipelines/p3_anomaly_engine/paper3_draft.tex` |
| P4 | Chirality Catalog | `pipelines/p2_chirality/chirality_catalog_paper.tex` |
| P5 | DESI Chirality | `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` |

## Hard gates

- [ ] Round file naming follows convention exactly
- [ ] All 6 paper IDs used consistently (P1A not "paper-1a" or "p1A")
- [ ] Cross-reference to `SSOT/paper-N/status.md` for close-the-gap detail
- [ ] Bundle commit hash recorded

## Related
- /revision-tracker-update — global parent
- /cross-vendor-r-round — produces round files
- /peer-review-truth-audit — must run BEFORE updating tracker
- /ssot-update — companion SSOT update
