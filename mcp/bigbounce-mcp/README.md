# bigbounce-mcp

Local MCP server exposing Bigbounce paper-orchestration state to Claude Code, Codex, Cursor, or any other MCP-aware agent. Phase 2 of the data-model rebuild ([DATA_MODEL_ARCHITECTURE.md](../../project-context/DATA_MODEL_ARCHITECTURE.md)).

## What it does

11 tools that bridge Convex (canonical source of truth) ↔ agent tool calls. No more hand-editing 5+ unsynced files per paper closure; one MCP call writes to Convex, the site re-renders on subscription.

| Tool | Purpose |
|---|---|
| `bigbounce_list_papers` | Cross-paper dashboard with computed-readiness state |
| `bigbounce_get_paper` | Full state for one paper |
| `bigbounce_list_open_findings` | R-round work queue |
| `bigbounce_truth_audit_finding` | Apply truth-audit verdict (VERIFIED/FALSIFIED/STALE/OUT-OF-SCOPE/OPINION) — required before close |
| `bigbounce_close_finding` | Atomic finding closure with explicit closureStatus enum |
| `bigbounce_bump_paper_version` | Atomic .tex version bump → site re-renders |
| `bigbounce_list_pathc_caveats` | Per-paper deferral list |
| `bigbounce_close_pathc_caveat` | Close a caveat with explicit closureMethod enum (⚠️ flags caveat-as-closure anti-pattern) |
| `bigbounce_list_pods` | RunPod lifecycle + cost accounting |
| `bigbounce_get_external_review_prompt` | Dynamic copy/paste prompt for Houston's external review |
| `bigbounce_list_tasks` | Cross-paper open work queue |

## Install

```bash
cd mcp/bigbounce-mcp
npm install
npm run build
```

## Configure

The repo root has `.claude/mcp_servers.json` already wired. Set `CONVEX_URL` to your Convex deployment URL (after Phase 1 deploy lands):

```bash
export CONVEX_URL="https://your-deployment.convex.cloud"
```

(or put it in `bigbounce/.env.local` — the existing keys file).

## Tool catalog

See `src/index.ts` `TOOLS` array. Each entry has name, description, JSON-schema input, and handler. Tool descriptions are pulled into Claude Code's tool-discovery UI.

## Why MCP and not direct Convex calls

Three reasons:
1. **Tool-discovery for any agent.** Claude Code, Codex, Cursor all consume MCP. One server, multiple front-ends.
2. **Auth + transport boundary.** Agents call `bigbounce_close_finding` not raw Convex; server enforces the closureStatus enum + verdict-first ordering centrally.
3. **Future-proof.** Adding a new tool = one entry in `TOOLS` array. No agent-side schema synchronization.

## Phase 3 follow-up

Once this is deployed and tested, Phase 3 of the rebuild wraps these tools in higher-level skills (`/bigbounce-status`, `/bigbounce-r-round`, `/bigbounce-close`, etc.) in `bigbounce/.claude/skills/`. The skills auto-load with the project.
