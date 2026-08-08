# MCP Config Inventory

**Date:** 2026-06-16
**Status:** Read-only inventory. No MCP configs, API keys, paper files, pods, queues, or live research state were changed.
**Purpose:** Map the local MCP/API surfaces that touch BigBounce, You.md, h.computer, and Hubify without confusing stale Hubify app data with current BigBounce research truth.

## Source-Of-Truth Boundary

Houston clarified on 2026-06-16 that current BigBounce research work has been happening directly in the local `bigbounce` repo and on `bigbounce.hubify.app`. Hubify app/CLI research data is out of date unless an explicit refresh/sync path is designed and verified.

Current BigBounce truth surfaces:

- Local repo: `/Users/houstongolden/Desktop/CODE_2025/bigbounce`
- BigBounce SSOT/context files under `project-context/SSOT/`
- Paper source/artifact files in the repo
- Live companion site: `bigbounce.hubify.app`

Excluded from current BigBounce science-status inference:

- Hubify app lab data
- Hubify CLI active lab status
- Generic Hubify MCP tool output
- h.computer BigBounce cards unless they are explicitly sourced from approved BigBounce status events

## Inventory Table

| Surface | Local config / entrypoint | Tools / capability | Current state | Boundary |
|---|---|---|---|---|
| BigBounce MCP | `.claude/mcp_servers.json` -> `node ./mcp/bigbounce-mcp/dist/index.js` with env key `CONVEX_URL` | 11 paper-orchestration tools: list/get papers, findings, truth-audit, close finding, version bump, Path-C caveats, pods, external-review prompt, tasks | Config exists, but `mcp/bigbounce-mcp/dist/index.js` is currently missing. The package requires `npm install && npm run build` before the configured command can start. | Treat as a local data-model/MCP implementation candidate. Do not use it as current science truth until it is rebuilt and reconciled with the BigBounce SSOT plus `bigbounce.hubify.app`. |
| You.md CLI MCP | `youmd mcp`; source supports `--json` and host installs for Claude, Codex, and Cursor | Local CLI registry includes identity, project context, YouStack manifest/capabilities, stack routing/smoke, memories, private context, source add, context links, remote status, skills, activity log | CLI is installed globally as `youmd` v0.8.0. The local source also exposes web proxy routes at `/.well-known/mcp.json` and `/api/v1/mcp`. | Best owner for identity, memory, raw capture, mobile/SMS intake, dedupe, project routing, proposal state, and agent activity logs. |
| You.md hosted MCP | `src/app/.well-known/mcp.json/route.ts` and `src/app/api/v1/mcp/route.ts` proxy to `CONVEX_SITE_URL` | Hosted registry includes API-key scoped tools such as `whoami`, `get_agent_brief`, `get_identity`, `ask_public_profile`, `search_profiles`, `get_my_identity`, `get_my_stacks`, `get_repo_file`, `search_memories`, and `report_skill_outcome` | Available in source; no live call was made in this inventory. | Public/private identity API and hosted agent context surface. Use Bearer-key scopes; do not route paper mutations through hosted profile tools. |
| h.computer public MCP | `src/routes/api/public/mcp.ts`; auth via `X-H-Api-Key`; server name `h.computer` | 23 tools: `push_status`, `queue_blog_idea`, journal CRUD/recompile/list, `get_now`, `get_feed`, `get_project`, `search_youmd`, `get_blog`, `get_papers`, `get_journal`, `get_stats`, unified `search`, Folder.md read/write/search, BadFit fitness/activity/best-effort tools | Route exists and uses `mcp-tanstack-start`, Supabase server APIs, You.md public data, Folder.md, and BadFit. No live calls were made. | Owner-facing personal computer/status/control surface. It can display BigBounce status cards, but only from approved BigBounce events; it is not canonical science state. |
| Hubify MCP | Global Claude config has `hubify: hubify mcp`; Hubify package `@hubify/mcp-server@0.2.0`; CLI has `hubify mcp --health` | Hubify docs describe 48 tools after setup, including lab, experiment, pod, and task surfaces | Health check resolves the local server path and `CONVEX_URL`; `HUBIFY_LAB_SLUG` is missing, so the health audit fails that env requirement. Auth is restored, but active lab is `Local-LLM` and empty. | Tooling/app integration only. Do not infer BigBounce research status from Hubify app/CLI/MCP until the intended BigBounce lab/sync path is explicitly refreshed. |
| Global Claude MCP config | `~/.claude/mcp.json` | Contains `hubify` server entry | Read-only inspection only. | Global agent config. BigBounce project-specific authority should come from repo context and explicit env setup, not global defaults. |
| Global Cursor MCP config | `~/.cursor/mcp.json` | Includes design/deploy/external servers plus a `youmd` entry pointing at local You.md CLI dist | Some entries include inline credentials or token-like args. Values were not copied into this doc. | Treat as sensitive. Do not mirror inline secrets into project docs; prefer env-backed configuration. |
| Codex plugin temp MCPs | `~/.codex/.tmp/plugins/.../.mcp.json` | Plugin-provided transient MCP entries | Discovered only as local metadata. | Not BigBounce project authority. |

## Proposed Data Flow

Use a proposal-first chain:

1. **SMS/iMessage or Sendblue:** capture raw transcript chunks from phone/watch runs, drives, and voice-note sessions.
2. **You.md:** store raw memory, dedupe duplicate message chunks, segment by idea, route to projects, and create proposed task/context artifacts.
3. **BigBounce:** receive approved research-task proposals or context updates only. Paper edits still require SSOT, queue, compile, LaTeX visual audit, and truth-audit protocols.
4. **h.computer:** display owner-facing BigBounce research-node cards from approved status events and provide control affordances for Houston.
5. **Hubify:** remain excluded from current BigBounce science status unless a dedicated refresh/sync task reconciles Hubify data with the BigBounce repo and `bigbounce.hubify.app`.

## Immediate Risks

- BigBounce `.claude/mcp_servers.json` currently points at a missing built file: `mcp/bigbounce-mcp/dist/index.js`.
- BigBounce MCP README calls Convex the canonical source of truth, but Houston's 2026-06-16 correction makes the current truth local `bigbounce` plus `bigbounce.hubify.app` until a sync plan is verified.
- Hubify MCP health is missing `HUBIFY_LAB_SLUG`, and the authenticated active lab is empty.
- Global Cursor MCP config contains sensitive inline credential-style values; do not paste, copy, or mirror them into project docs.
- h.computer MCP has write-capable owner tools (`push_status`, `queue_blog_idea`, journal edits, Folder.md writes). BigBounce-related writes should be proposal-gated and sourced from approved BigBounce status events.

## Safe Next Setup Tasks

1. Build or deliberately disable the BigBounce MCP command before asking Claude/Codex/Cursor to auto-load it.
2. Decide whether BigBounce MCP should read from repo SSOT/site artifacts, Convex, or both, then update the README wording to match the current source-of-truth contract.
3. Define the SMS/iMessage -> You.md -> BigBounce proposal schema before wiring Sendblue or any live mobile capture.
4. Define the h.computer research-node status event shape as read-only display by default.
5. Only after that, consider a Hubify refresh/sync design that explicitly proves whether any Hubify lab data should re-enter the BigBounce research workflow.
