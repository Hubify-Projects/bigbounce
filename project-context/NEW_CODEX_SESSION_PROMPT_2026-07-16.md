# Copy/paste prompt — BigBounce dedicated Codex account resume

```text
Resume the active BigBounce publication-readiness goal exactly as documented;
do not replace it with a narrower task:

Drive all six BigBounce papers through honest internal and external
non-Anthropic multi-model review, truth-audited closure, re-review,
PDF/version/SSOT/Convex/API/site synchronization, and evidence-backed 95–99%
publication readiness (accepted or minor-revisions-only), documenting every
process acceleration without fabricating or overstating results.

You are in /Users/houstongolden/Desktop/CODE_YOU/bigbounce on main. Before any
write or model dispatch, read in this order:

1. AGENTS.md
2. project-context/AGENT_ONBOARDING.md
3. CLAUDE.md
4. AGENT_RULES.md
5. project-context/BIGBOUNCE_CODEX_ACCOUNT_HANDOFF_2026-07-16.md
6. project-context/tasks.md and project-context/plan.md
7. project-context/SSOT/paper-{1,3,4,5}/status.md as relevant.

First verify the checkout and routing:

git status --short
git log -1 --oneline
python3 -m unittest tools.tests.test_no_openai_api_review
python3 tools/bigbounce_preflight.py run --receipt /tmp/bigbounce-preflight.json
python3 tools/bigbounce_preflight.py verify --receipt /tmp/bigbounce-preflight.json

Authenticate the dedicated Codex/ChatGPT subscription only through the normal
interactive Codex login. Never put authentication in this repository, logs, or
.env files. OpenAI API is forbidden for BigBounce reviews and orchestration.

Routing after dedicated-account verification:
- Restore normal Codex participation with
  export BIGBOUNCE_CODEX_SUBSCRIPTION_ENABLED=1
- Use Codex CLI subscription, direct Grok/xAI API, and direct Gemini API only
  as independently receipted legs. No Anthropic/Claude leg.
- Preserve raw receipts; absent/failed/wrong-PDF legs remain absent/failed.
- Do not re-review unchanged PDFs merely to seek a better verdict.

Prioritize actual gates, not more loops:
1. P4 v1.0.260: validate/publish the strict-primary provider overlay only after
   confirming the intended Hugging Face account/token and the external release
   decision. Then remote-byte-verify and run an exact-PDF residual board.
2. P5 v0.1.139: run the exact confirmation after its current four minor fixes;
   progress Paper IV independent provenance and the archive/DOI/editorial AJ
   gates.
3. P3 v3.2.0-r8: do not repeat an unchanged review; archive/DOI and human ApJS
   decisions are the remaining gates.
4. P1B: resolve its archive/editorial gate without overstating the positive
   exact-artifact evidence.

Before every review wave: bind exact source/PDF hashes, version, commit, venue,
prompt, and a current portfolio-preflight receipt. Truth-audit every finding;
turn every real blocker/major or recurrent minor into an executable regression
and sweep all six papers before the next wave. Compile, visually audit all PDF
pages, retain immutable PDFs, then synchronize claims/version/SSOT/Convex/site
atomically only when evidence supports it.

Delegation and CMUX:
- Use normal Codex subagents for independent, bounded, non-overlapping work
  (one write owner per file/manifest). Use inexpensive workers for mechanical
  checks and reserve the director for scientific judgment and integration.
- Do not create a multi-agent CMUX mutation swarm merely because it is
  available. The CMUX/You.md dogfood track is read-only until atomic work claims,
  heartbeats, overlap detection, and isolated worktrees are acceptance-tested.
- If CMUX is used for a bounded evaluation, follow the existing CMUX docs and
  keep it read-only against BigBounce; do not let a CMUX pane substitute for a
  provider receipt or mutate review/SSOT/Convex state.
- Check the active worktree and task ledger before delegation; do not duplicate
  another agent's active work. Commit only coherent, verified, bisected units
  and push main after the required site freshness checks.

Be honest about remaining external and human gates. Keep the full goal active;
do not claim 95–99% or acceptance until current evidence proves it.
```
