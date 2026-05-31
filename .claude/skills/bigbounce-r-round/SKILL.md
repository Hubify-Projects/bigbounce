---
name: bigbounce-r-round
description: Fire a direct-vendor adversarial peer-review round on a Bigbounce paper. Uses tools/cross_vendor_review_direct.py (Anthropic NOT included per feedback_cross_model_peer_review no-echo-chamber rule; vendors = OpenAI/Google/Grok/Perplexity). Writes the round + each reviewer's findings to Convex via the bigbounce MCP so they appear in /bigbounce-status as open findings ready for truth-audit + closure. No more OpenRouter excuse (direct vendor keys live in youmd/.env.local per feedback_no_openrouter_excuse).
---

# /bigbounce-r-round <paper-slug>

End-to-end direct-vendor R-round. Replaces the manual `python tools/cross_vendor_review_direct.py ... ; manually-read-output ; manually-write-findings-to-Convex` chain with one skill.

## Usage

```
/bigbounce-r-round paper-1b
/bigbounce-r-round paper-3 --label R-direct-v3 --context "verify v3.1.69 retracted-Fisher-form scrub held"
```

## Behavior

1. Resolve paper slug → current version + .tex path via `bigbounce_get_paper`.
2. Generate round label `YYYY-MM-DD_R-direct-vN` (auto-increment N).
3. Call `r_rounds.create` mutation → get round ID.
4. Spawn `python tools/cross_vendor_review_direct.py <texPath> <label> <PaperTag> <context>` — runs 4 vendors in parallel.
5. For each `project-context/peer-reviews/<label>_<tag>_R-round_direct_*.md` output, parse the H2-section findings and call `findings.create` mutation per finding.
6. Print summary: N findings landed; next step is `/bigbounce-truth-audit` on each.

## Anti-pattern guards

- If the previous R-round on this paper version has open findings not yet truth-audited, refuses to start a new round (avoids accumulating un-audited findings).
- Anthropic NOT included as a reviewer (would be Claude reviewing Claude-assisted prose — no echo chamber).
- DeepSeek excluded until Houston provides a direct API key (currently only OpenRouter; YouMD .env.local has no DEEPSEEK_API_KEY).
