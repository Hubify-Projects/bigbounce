# Mac Mini Research Node Plan

**Date:** 2026-06-16
**Status:** Context/spec checkpoint only. No paper edits, GPU runs, pod actions, live SMS hooks, or generated artifacts were changed.
**Source:** Houston's 2026-06-16 Part 2 brain dump routing memo and the BigBounce/Hubify handoff prompt.

## Purpose

The Mac mini research node is a persistent local coordination machine for BigBounce and Hubify science-stack work. It should make local agents, prompts, logs, project context, and owner-facing status easier to keep in sync.

It is not a scientific source of truth. BigBounce paper status stays canonical in `project-context/SSOT/`, paper text stays canonical in the relevant `.tex` sources, and compute work stays governed by existing queue, drive-to-100, compile, audit, and truth-audit protocols.

## Verified Smoke Check

Run from `/Users/houstongolden/Desktop/CODE_2025/bigbounce` on 2026-06-16:

| Check | Result |
|---|---|
| `git status --short --branch` | Worktree already noisy before this checkpoint; docs-only changes are scoped separately. |
| SSOT read | `project-context/SSOT/README.md`, `index.md`, `queue.md`, and drive-to-100 log were read before edits. |
| `hubify status` | CLI import/spinner crashes fixed in Hubify commits `aa5dd910` and `94fd9344`; auth restored on 2026-06-16 and live status returns for active lab `Local-LLM` (`local-llm`). |
| Claude Code | Present: `/opt/homebrew/bin/claude`, version `2.1.153 (Claude Code)`. |
| Codex | Present: `/Users/houstongolden/.nvm/versions/node/v22.20.0/bin/codex`, version `codex-cli 0.130.0`. |
| Hubify CLI | Present as npm/global symlink; `hubify status`, `hubify lab info`, and `hubify labs` now return live authenticated output, but Hubify app research data is not current BigBounce research state. |
| OpenClaw CLI | `openclaw` command not found. Verify package/repo path before using it as a runner. |
| Hermes CLI | `hermes` command not found. Verify package/repo path before using it as a runner. |
| Pi CLI | `pi` command not found globally. `.pi` directories exist in sibling repos, but `@mariozechner/pi-coding-agent` is not installed globally. |
| Repo map | `bigbounce`, `youmd`, `h-computer`, `hubify`, `badapp`, and `myo` directories are present under `/Users/houstongolden/Desktop/CODE_2025/`. |

### Hubify CLI Status

Original blocker recorded by this checkpoint:

```text
Error: Cannot find package '/Users/houstongolden/Desktop/CODE_2025/hubify/cli/node_modules/ink/index.js' imported from /Users/houstongolden/Desktop/CODE_2025/hubify/cli/dist/index.js
Did you mean to import "ink/build/index.js"?
code: 'ERR_MODULE_NOT_FOUND'
Node.js v22.20.0
```

Follow-up repair on 2026-06-16:

- Hubify commit `aa5dd910 fix(cli): lazy-load TUI dependencies` changed the CLI build so TUI-only Ink dependencies stay in a lazy chunk instead of loading during every command.
- Hubify commit `94fd9344 fix(cli): avoid spinner import hang` removed the remaining `ora` startup/runtime hang from the CLI command path.
- After these fixes, `hubify --help`, `hubify status`, and the Hubify health env-audit return promptly.
- `hubify auth login` was attempted twice and the auth URLs were opened locally, but both device flows timed out waiting for browser authorization. The latest failed code was `CMJX-6HGC`.
- Third auth attempt succeeded on 2026-06-16 with code `RTW6-E8D9`; token saved to `~/.hubify-labs/config`.
- Current live authenticated checks:

```text
hubify labs -> Local-LLM [local-llm] active
hubify lab info -> Lab ID m97bz5fgqc4j1jxf0vz789sajs8534nn
hubify status -> 0 experiments, 0 papers, 0 surveys, 0 anomalies, 0 agents, 0 pods
```

The active authenticated lab is currently empty (`Local-LLM`), and Houston clarified on 2026-06-16 that Hubify app research data is out of date because recent research work has been happening directly in the `bigbounce` repo and on `bigbounce.hubify.app`. The Mac mini node must not infer BigBounce science state from Hubify app/CLI lab data. Use BigBounce local context, SSOT files, and `bigbounce.hubify.app` as the current research surfaces.

See `project-context/bigbounce-source-of-truth-contract-2026-06-16.md` for the active source-of-truth contract.
See `project-context/agent-runtime-inventory-2026-06-16.md` for the OpenClaw/Hermes/Pi runtime inventory and authority boundary.
See `project-context/mcp-config-inventory-2026-06-16.md` for the MCP/API surface inventory across BigBounce, You.md, h.computer, Hubify, and global agent configs.

## Agent And Runtime Inventory

| Runner/tool | Intended role | Current state | Safe next step |
|---|---|---|---|
| Claude Code | Primary high-judgment reasoning, paper/review synthesis, local coding sessions. | Installed and versioned. | Keep as primary reasoning runner for science judgment and final truth-audit decisions. |
| Codex | Local coding and docs/context execution runner. | Installed and versioned. | Use for scoped implementation, validation, and repo-context updates. |
| OpenClaw | Possible agent/runtime pattern or runner. | Command not found; gstack/OpenClaw methodology artifacts exist under shared skill roots and gbrain has an OpenClaw plugin manifest. | Locate actual CLI before any run; first test must be isolated toy work, not BigBounce. |
| Hermes Agent | Possible local research/agent runner. | Command not found; gstack/Hermes host artifacts exist under shared skill roots. | Locate actual CLI before any run; first test must be isolated toy work, not BigBounce. |
| Pi Agent | UI/orchestration inspiration or isolated subprocess runner. | Command not found globally; `.pi` config dirs exist in sibling repos including Hubify, agent-team, and BAMF projects. | Treat as design/config evidence only until runtime command is found; no BigBounce authority. |
| Hubify CLI | Tooling/status integration candidate, not current BigBounce research source of truth. | Import/spinner crashes fixed; auth restored; active lab is `Local-LLM` and currently empty. | Do not wire BigBounce research status to Hubify app data until the intended BigBounce lab/sync path is explicitly refreshed. |
| Browser automation | QA/status inspection and local UI checks. | Available via existing local agent/browser stack, but no browser work was needed for this docs-only checkpoint. | Keep for site QA and h.computer owner-facing status surfaces, not for live compute. |
| MCP/local stack configs | Connect BigBounce, You.md, h.computer, Hubify, and optional host adapters. | Not changed in this checkpoint. | Inventory local MCP configs separately before mutating them. |

Environment variables should be referenced by name only in docs. Relevant key names include `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `GOOGLE_AI_API_KEY`, `DEEPSEEK_API_KEY`, `XAI_API_KEY`, `OPENROUTER_API_KEY`, `PERPLEXITY_API_KEY`, `NASA_ADS_API_KEY`, `SEMANTIC_SCHOLAR_API_KEY`, `WOLFRAM_ALPHA_APP_ID`, `HUGGINGFACE_TOKEN`, `RUNPOD_API_KEY`, and provider-specific SMS/iMessage webhook secrets. Do not print or store values.

## Repository Map

| Path | Role in the node |
|---|---|
| `/Users/houstongolden/Desktop/CODE_2025/bigbounce` | BigBounce papers, SSOT, project context, queues, research scripts, and companion site. |
| `/Users/houstongolden/Desktop/CODE_2025/youmd` | Identity, memory, source catalog, mobile capture, project routing, YouStacks, API/MCP layer. |
| `/Users/houstongolden/Desktop/CODE_2025/h-computer` | Owner-facing status/feed/control surface for Houston's personal computer interface. |
| `/Users/houstongolden/Desktop/CODE_2025/hubify` | Hubify CLI and labs/science platform code; import/spinner crashes fixed and auth restored, but research data there may be stale relative to direct BigBounce work. |
| `/Users/houstongolden/Desktop/CODE_2025/badapp` | Fitness/workout transcript consumer for mobile capture sessions. |
| `/Users/houstongolden/Desktop/CODE_2025/myo` | Health/body/productivity consumer for routed capture where appropriate. |
| `/Users/houstongolden/.claude/scistack/` | Science-stack skills source of truth. |
| `/Users/houstongolden/.agent-shared/claude-skills/` | Shared non-science skills source of truth. |
| `/Users/houstongolden/.codex/skills/` | Codex skill mirror/cache. |

## Connection Contract

The Mac mini node should coordinate through a proposal-first contract:

1. **SMS/iMessage/Sendblue capture:** inbound notes are capture events only. They create raw transcript artifacts and proposed tasks, not direct paper edits, pod launches, deploys, or external writes.
2. **You.md:** owns raw memory, dedupe, segmentation, project routing, identity/context, approval state, and audit logs.
3. **BigBounce:** receives approved research-task proposals or context updates. Paper changes still follow SSOT, queue, compile, latex-audit, and truth-audit rules.
4. **h.computer:** can display owner-facing feed/status/control cards for the research node, but should not become the canonical science tracker.
5. **Hubify:** is a tooling/app integration surface only until explicitly refreshed. Do not infer BigBounce research status from Hubify app/CLI lab data; current research state lives in the local `bigbounce` repo and `bigbounce.hubify.app`.
6. **RunPod/GPU/pods:** only operate through existing BigBounce/Hubify protocols and queue authorization. Raw mobile capture never starts expensive compute.

Example dry-run capture, local only:

```text
source: fake_sms_transcript
text: "BigBounce note: test Pi only on a toy task first, and make h.computer show research-node status."
route: You.md raw artifact -> BigBounce task proposal + h.computer status-hook proposal
approval: required before any repo write or external action
```

## Safety And Approval Model

- Raw SMS/iMessage commands create tasks or proposals first.
- Expensive GPU runs require explicit approval or an existing authorized queue row.
- Paper edits require the relevant SSOT status file, queue check, compile, visual LaTeX audit, and truth-audit discipline.
- No paper claim strengthening happens without truth audit.
- No background agent starts work on a queue row already owned by drive-to-100 or another active agent.
- Secrets remain in local env files, password manager storage, or ignored files only.
- External writes to GitHub issues, Notion, project boards, CRM, Slack, h.computer feeds, or paper artifacts require an approval gate unless a bounded automation rule already exists.

## Pi Agent And Multi-Agent UI Evaluation

`project-context/pi_agent_study.md` concludes that Pi-style patterns are useful for Hubify Labs UI/orchestration design, while Claude Code and Codex may remain the primary reasoning engines.

For this node:

- Pi is not currently a verified runner because `pi` is not installed globally.
- Pi can inspire dispatcher dashboards, specialist subprocess cards, status widgets, and "till done" gating.
- Pi may become a subprocess specialist runner only after an isolated toy-task test.
- Do not route BigBounce paper, pod, queue, or publication-affecting work to Pi until its install path, tool boundaries, logs, and failure modes are documented.

## Multi-Model / Multi-UI Review Method Candidate

Houston's observation from the BigBounce campaign should be captured as a research/workflow candidate, not a proven claim:

> Multi-model plus multi-interface review appeared to produce stricter results and seemed harder for a single agent loop to game than one evaluator surface.

Candidate method components:

- Internal agent proposes, patches, or audits.
- External models review independently from fresh context.
- Multiple UI/tool surfaces reduce overfitting to one evaluator protocol.
- Disagreement creates findings, not automatic rejection.
- Closure agents patch only verified findings.
- Final truth audit verifies closures against source files, artifacts, and claim language.
- Reviewer-stack limitations are logged, such as missing vendor legs, expired credits, or substituted Claude Code sub-agent legs.

Research status: hypothesis and workflow pattern only. To become a paper or formal method, it needs a written protocol, dataset of review rounds, outcome metrics, ablation against single-model/single-UI review, and an honesty section on selection effects and agent incentives.

## First Live-Setup Tasks

Completed context gates:

1. Capture the direct BigBounce repo plus `bigbounce.hubify.app` source-of-truth contract before any Hubify app sync work.
2. Inventory local agent runtimes for Claude Code, Codex, Hubify, OpenClaw, Hermes, and Pi.
3. Inventory local MCP configs for BigBounce, You.md, h.computer, Hubify, and global agent configs.

Next setup tasks:

1. Define the SMS/iMessage -> You.md -> BigBounce task proposal schema.
2. Define an h.computer research-node status hook that consumes approved BigBounce status events only.
3. Add a no-live-runs smoke test that writes a fake capture event to local project context.
4. Draft the multi-model/multi-UI review-method paper protocol as a candidate workflow paper.
