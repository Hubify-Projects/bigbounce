# R42 — Adversarial Multi-Agent Peer Review (2026-04-30 onward)

**Status:** OPEN — accepting reviewer submissions
**Master log:** [`../master/2026-04-30_R42_master.md`](../master/2026-04-30_R42_master.md)
**Index:** [`../README.md`](../README.md)

## What gets dropped here

Individual reviewer files for R42, one per (LLM × paper) pair. Filename convention:

```
r42_{reviewer}_{paper}_{date}.md
```

Examples:
- `r42_chatgpt-deepthink_paper1_2026-04-30.md`
- `r42_grok-heavy_cross-paper_2026-04-30.md`
- `r42_gemini-deep_paper3_2026-04-30.md`
- `r42_perplexity_paper2_2026-05-01.md`

## Workflow

1. Houston pastes new peer-review feedback → save here as the matching reviewer/paper file.
2. Each finding gets classified (BLOCKER / MAJOR / MINOR / REJECTED-AS-WRONG) and rolled into the master log table.
3. Each BLOCKER + MAJOR opens a row in `../../SSOT/queue.md`.
4. Fix queue executes end-to-end (Principle 12 — no laziness, no deferral).
5. Round closes with the standing PDF restamp bundle (Principle 13).
