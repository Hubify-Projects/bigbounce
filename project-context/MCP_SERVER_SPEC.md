# Hubify Labs — MCP Server Specification

**Status:** SPEC IN PROGRESS · Category E of `BUILD_READINESS_CHECKLIST.md`
**Author:** Houston Golden + Claude
**Date locked:** 2026-04-08
**Linked from:** PRD §44 (placeholder · TBD), `BUILD_READINESS_CHECKLIST.md` Category E
**Depends on:** `API_SPEC.md` (Category D — locked 2026-04-08)
**Reference implementation:** TypeScript MCP SDK (`@modelcontextprotocol/sdk`)

---

## 0. The premise

The Hubify Labs MCP server is **the bridge between AI agents and the platform**. Every agent that participates in a Hubify Labs research workflow — whether it's the lab orchestrator running on Fly, a peer-review-gpt agent calling out to GPT-5, a CLI session running Claude Code locally, or an external researcher's IDE agent — speaks to the platform through this MCP server.

**MCP (Model Context Protocol)** is Anthropic's open standard for connecting LLMs to external systems. Spec: https://spec.modelcontextprotocol.io. The Hubify Labs MCP server implements this standard so it works out of the box with Claude Code, Claude Desktop, Cursor, VS Code with the MCP extension, and any future MCP-compatible client.

**Why MCP is load-bearing for Hubify Labs:**
- Houston runs Claude Code daily. Claude Code speaks MCP. If our platform doesn't expose an MCP server, Houston can't drive Hubify Labs from his existing workflow.
- The peer-review-gpt agent (and the other cross-provider reviewers) need a uniform way to read papers, write reviews, and post comm-events. MCP is that uniform way.
- Future external integrations — a researcher in another org wants their Claude Desktop to query a public Hubify Labs lab — get one well-known protocol, not a custom REST integration.

**One MCP server, many transports.** The same server logic exposes itself via:
- **stdio** (for local processes — Claude Code, Cursor)
- **SSE / streamable HTTP** (for remote clients — Claude Desktop, web agents)
- **WebSocket** (for the platform's own internal agent runtime on Fly)

---

## 1. The MCP primitives we expose

MCP defines four primitives a server can expose to a client:
1. **Tools** — functions the agent can call (read_file, dispatch_experiment, etc.)
2. **Resources** — readable data the agent can subscribe to (lab metadata, current pod status, etc.)
3. **Prompts** — reusable prompt templates the server provides (e.g., "review this paper" template)
4. **Sampling** (optional) — server can ask the client to run an LLM call on its behalf

Hubify Labs implements all four. The bulk of the surface is **tools** (~30) and **resources** (~15).

---

## 2. Tools (the agent's actions)

These are the functions agents can call. Every tool:
- Maps 1:1 to a REST endpoint from `API_SPEC.md` §3 (the MCP server is a thin wrapper around the API)
- Has a JSON schema for inputs and outputs
- Has a clear name + description that the LLM can read to decide when to call it
- Is per-lab scoped via the agent's token (per `API_SPEC.md` §2.4)
- Logs every invocation to the audit trail

### 2.1 File system tools (scoped to current lab)

```typescript
{
  name: "read_file",
  description: "Read a file from the current lab. Returns content + metadata. Path is relative to the lab root.",
  inputSchema: {
    type: "object",
    properties: {
      path: { type: "string", description: "Relative path within the lab, e.g. 'arxiv/main.tex' or 'projects/fnl-tracer-pipeline/goal.md'" },
      lab: { type: "string", description: "Optional lab slug. Defaults to the current lab from the agent's token scope." }
    },
    required: ["path"]
  }
}

{
  name: "write_file",
  description: "Write or create a file in the current lab. Overwrites existing files. Returns the new file's metadata.",
  inputSchema: {
    type: "object",
    properties: {
      path: { type: "string" },
      content: { type: "string" },
      lab: { type: "string" }
    },
    required: ["path", "content"]
  }
}

{
  name: "list_files",
  description: "List files in a directory within the current lab. Returns an array of file metadata (name, size, mtime, kind).",
  inputSchema: {
    type: "object",
    properties: {
      path: { type: "string", description: "Directory path. Use '/' for the lab root." },
      recursive: { type: "boolean", description: "Walk subdirectories. Default false." },
      lab: { type: "string" }
    },
    required: ["path"]
  }
}

{
  name: "delete_file",
  description: "Delete a file in the current lab. Audit-logged. Cannot delete from another lab.",
  inputSchema: {
    type: "object",
    properties: { path: { type: "string" }, lab: { type: "string" } },
    required: ["path"]
  }
}
```

### 2.2 Experiment dispatch tools (per PRD §41 routing)

```typescript
{
  name: "dispatch_experiment",
  description: "Dispatch an experiment to RunPod compute (Pods or Serverless, CPU or GPU). The platform's §41 routing logic decides which compute mode based on the spec. Returns a job handle for monitoring.",
  inputSchema: {
    type: "object",
    properties: {
      title: { type: "string" },
      project_id: { type: "string", description: "The project this experiment belongs to" },
      requires_gpu: { type: "boolean", description: "REQUIRED: does this task have a tensor in the hot path? Per PRD §41 Rule 1." },
      gpu_type: { type: "string", enum: ["H100", "H200", "A100", "A6000", null] },
      expected_duration_min: { type: "number", description: "Estimated wall-clock minutes. Used by §41 Rule 2 to choose Pod vs Serverless." },
      priority: { type: "string", enum: ["low", "med", "high", "critical"] },
      command: { type: "string", description: "The shell command to run" },
      working_dir: { type: "string", description: "Where to run it (absolute path on the pod)" },
      checkpoint_interval_min: { type: "number", description: "How often to checkpoint. Per PRD §41 Rule 4 (checkpoint discipline). Default 10." },
      max_cost_usd: { type: "number" }
    },
    required: ["title", "project_id", "requires_gpu", "expected_duration_min", "command"]
  }
}

{
  name: "experiment_status",
  description: "Get the current status of a dispatched experiment.",
  inputSchema: {
    type: "object",
    properties: { experiment_id: { type: "string" } },
    required: ["experiment_id"]
  }
}

{
  name: "experiment_logs",
  description: "Tail the last N lines of an experiment's logs.",
  inputSchema: {
    type: "object",
    properties: {
      experiment_id: { type: "string" },
      lines: { type: "number", description: "How many lines to return. Default 100, max 1000." }
    },
    required: ["experiment_id"]
  }
}

{
  name: "cancel_experiment",
  description: "Gracefully cancel a running experiment. Sends SIGTERM with 30-sec checkpoint window per PRD §41 Rule 4.",
  inputSchema: {
    type: "object",
    properties: { experiment_id: { type: "string" } },
    required: ["experiment_id"]
  }
}
```

### 2.3 Agent invocation tools

```typescript
{
  name: "invoke_agent",
  description: "Call another agent in the same lab. The target agent receives the payload as a comm-event in its inbox. Returns the comm-event ID for tracking.",
  inputSchema: {
    type: "object",
    properties: {
      target_agent: { type: "string", description: "The agent name, e.g. 'paper-lead' or 'peer-review-gpt'" },
      payload: { type: "object", description: "Free-form JSON payload" },
      reply_to: { type: "string", description: "Optional comm-event ID this is a reply to" }
    },
    required: ["target_agent", "payload"]
  }
}

{
  name: "list_agents",
  description: "List all agents available in the current lab. Returns name, role, model, status (busy/idle).",
  inputSchema: { type: "object", properties: { lab: { type: "string" } } }
}

{
  name: "agent_inbox",
  description: "Get the current agent's inbox of pending comm-events.",
  inputSchema: { type: "object" }
}
```

### 2.4 Cross-lab comms tools (per PRD §40.11 — the gateway)

```typescript
{
  name: "comm_send",
  description: "Send a comm-event to another lab's orchestrator. PER PRD §40.11 LAB SOVEREIGNTY RULE: cross-lab comms can SUGGEST changes but cannot directly write to the target lab's filesystem. The target lab's orchestrator decides whether to accept.",
  inputSchema: {
    type: "object",
    properties: {
      target_lab: { type: "string", description: "The slug of the destination lab" },
      target_agent: { type: "string", description: "Default 'orchestrator'" },
      payload: {
        type: "object",
        properties: {
          type: { type: "string", enum: ["suggestion", "learning_share", "file_delta_proposal", "info"] },
          subject: { type: "string" },
          body: { type: "string" },
          attachments: { type: "array", items: { type: "string" } }
        },
        required: ["type", "subject", "body"]
      }
    },
    required: ["target_lab", "payload"]
  }
}

{
  name: "comm_inbox_cross_lab",
  description: "Get the current lab's inbox of incoming cross-lab comm-events from other labs.",
  inputSchema: { type: "object" }
}
```

### 2.5 Memory tools (per PRD §20)

```typescript
{
  name: "memory_search",
  description: "Search the lab's 4-layer memory (user / agent / lab / global). Returns top-N matching entries with relevance scores.",
  inputSchema: {
    type: "object",
    properties: {
      query: { type: "string" },
      layer: { type: "string", enum: ["user", "agent", "lab", "global", "all"] },
      limit: { type: "number", description: "Max results. Default 10." }
    },
    required: ["query"]
  }
}

{
  name: "memory_save",
  description: "Save a new memory entry. Type determines which layer it lands in (user, feedback, project, reference).",
  inputSchema: {
    type: "object",
    properties: {
      type: { type: "string", enum: ["user", "feedback", "project", "reference"] },
      title: { type: "string" },
      body: { type: "string" }
    },
    required: ["type", "title", "body"]
  }
}
```

### 2.6 Contribution tools (per PRD §22 — N-score system)

```typescript
{
  name: "contribution_create",
  description: "Propose a new scientific contribution. The contribution starts at the agent's claimed N-score and goes through cross-model peer review (per PRD §29) before being promoted to validated.",
  inputSchema: {
    type: "object",
    properties: {
      title: { type: "string" },
      description: { type: "string" },
      claimed_n_score: { type: "number", enum: [0, 1, 2, 3], description: "N0-N3. N4 (flagship breakthrough) cannot be claimed by an agent — only externally validated." },
      project_id: { type: "string" },
      paper_refs: { type: "array", items: { type: "string" } },
      experiment_refs: { type: "array", items: { type: "string" } }
    },
    required: ["title", "description", "claimed_n_score", "project_id"]
  }
}
```

### 2.7 Note tools (per PRD §38 — the journal)

```typescript
{
  name: "note_save",
  description: "Save a markdown note to the journal. PER PRD §38 AGENT VISIBILITY CONTRACT: agents can save notes ONLY when explicitly requested by the user, never autonomously.",
  inputSchema: {
    type: "object",
    properties: {
      filename: { type: "string", description: "e.g. notes/2026-04-08.md or notes/prompts/idea.md" },
      content: { type: "string" },
      explicit_user_consent: { type: "boolean", description: "MUST be true. The agent confirms it has explicit user consent to save this note." }
    },
    required: ["filename", "content", "explicit_user_consent"]
  }
}

{
  name: "note_search",
  description: "Search Houston's journal notes by full-text query. Returns matching notes with snippets.",
  inputSchema: {
    type: "object",
    properties: { query: { type: "string" }, limit: { type: "number" } },
    required: ["query"]
  }
}
```

### 2.8 Chat tools (per PRD §40.7, §40.13)

```typescript
{
  name: "chat_message",
  description: "Post a message to a chat session. Per PRD §40.13, chats default to 'no-action mode' — the agent can suggest but not act unless the chat has been promoted to a project.",
  inputSchema: {
    type: "object",
    properties: {
      chat_id: { type: "string" },
      content: { type: "string" },
      mode: { type: "string", enum: ["default", "chat"], description: "'chat' = no-action mode (cannot trigger work). Default uses the chat's current mode." }
    },
    required: ["chat_id", "content"]
  }
}

{
  name: "chat_promote",
  description: "Trigger the chat-to-project graduation flow per PRD §40.6. Drafts a project spec from the chat and asks the user 'look good? (y/n)'. ONLY graduates if the orchestrator can write all 4 spec fields (goal, deliverable, measurable, mini-plan) — otherwise returns an error and asks for more shape.",
  inputSchema: {
    type: "object",
    properties: { chat_id: { type: "string" } },
    required: ["chat_id"]
  }
}
```

### 2.9 LaTeX + paper tools

```typescript
{
  name: "pdf_compile",
  description: "Trigger a LaTeX compile of a .tex file. Runs on a RunPod CPU pod (per PRD §41 Rule 1 — LaTeX is CPU work, not GPU). Returns a job handle.",
  inputSchema: {
    type: "object",
    properties: { tex_path: { type: "string", description: "Relative path to the .tex file in the lab" } },
    required: ["tex_path"]
  }
}

{
  name: "publish_loop_start",
  description: "Trigger the 5-round publish-ready loop on a paper (per PRD §37). The loop runs: mechanical QA → cross-model intellectual review → Houston Method retroactive sweep → final visual + format pass → arXiv package build.",
  inputSchema: {
    type: "object",
    properties: { paper_id: { type: "string" } },
    required: ["paper_id"]
  }
}
```

### 2.10 Compute tools (per PRD §24, §41)

```typescript
{
  name: "runpod_status",
  description: "Get the current RunPod credit balance, 24h burn rate, and projected runway in hours. Per PRD §41.2.",
  inputSchema: { type: "object" }
}

{
  name: "list_pods",
  description: "List all currently running pods registered to the lab.",
  inputSchema: { type: "object" }
}
```

### 2.11 Search tools (universal)

```typescript
{
  name: "search",
  description: "Universal search across the lab's entities (papers, experiments, agents, files, contributions, surveys, chats, notes). Backs the ⌘K palette in the UI.",
  inputSchema: {
    type: "object",
    properties: {
      query: { type: "string" },
      types: { type: "array", items: { type: "string", enum: ["paper", "experiment", "agent", "file", "contribution", "survey", "chat", "note"] }, description: "Filter to specific entity types. Default: all." },
      limit: { type: "number" }
    },
    required: ["query"]
  }
}
```

**Total tool count for v1: ~30 tools** across 11 categories.

---

## 3. Resources (the agent's readable data)

Resources are persistent or live data the agent can read and (for live ones) subscribe to. Unlike tools, resources don't take parameters — they're addressable by URI.

### 3.1 Lab metadata resources

```
lab://current/info                      → Lab metadata (mission, north star, director, project count)
lab://current/projects                  → List of all projects in the current lab
lab://current/projects/<id>             → Project detail (Project Overview page content)
lab://current/agents                    → List of all agents in the current lab
lab://current/agents/<name>             → Agent detail (10-tab content per PRD §34)
lab://current/papers                    → List of all papers
lab://current/papers/<id>               → Paper metadata + LaTeX source
lab://current/contributions             → List of contributions with N-scores
lab://current/datasets                  → List of datasets
lab://current/wiki                      → Wiki entries
lab://current/notes                     → List of notes (journal)
```

### 3.2 Live resources (subscribable streams)

```
live://current/activity                 → SSE stream of the activity feed (every comm-event, every experiment dispatch, every standup)
live://current/credits                  → SSE stream of credit balance changes
live://current/standups                 → SSE stream of in-progress standup transcripts
live://current/comms-inbox              → SSE stream of incoming cross-lab comm-events
live://current/experiments/<id>/logs    → SSE stream of a specific experiment's logs
```

### 3.3 Compute resources

```
compute://runpod/credits                → Current credit balance + burn + runway (snapshot)
compute://runpod/pods                   → List of running pods (snapshot)
compute://runpod/serverless             → List of serverless endpoints (snapshot)
```

**Total resources for v1: ~15 resources.**

---

## 4. Prompt templates

MCP servers can provide pre-written prompt templates that clients can use. Hubify Labs ships with these templates so any agent (Claude Code, Cursor, etc.) can drop them in and get consistent behavior:

### 4.1 Available prompts

```typescript
{
  name: "review_paper",
  description: "Generate a structured peer review of a paper using the Hubify Labs review format (verdict / critical / suggestions / prior work / FACT-OPINION-HALLUCINATION tags per PRD §29).",
  arguments: [
    { name: "paper_id", description: "The paper to review", required: true },
    { name: "perspective", description: "Reviewer mode: 'skeptic' / 'long-context' / 'contrarian' / 'fact-check'", required: false }
  ]
}

{
  name: "houston_method_post_experiment",
  description: "Run the Houston Method v2 8-step post-experiment protocol on a completed experiment (QC gate → scientific analysis → interpretation → cross-survey connection → site sync → queue expansion → backup → standup notes).",
  arguments: [
    { name: "experiment_id", description: "The experiment to analyze", required: true }
  ]
}

{
  name: "draft_chat_to_project",
  description: "Draft a chat-to-project graduation spec per PRD §40.6 (goal + deliverable + measurable + mini-plan). Reject if the chat can't fill all 4 fields.",
  arguments: [
    { name: "chat_id", description: "The chat to graduate", required: true }
  ]
}

{
  name: "standup_facilitate",
  description: "Run a synchronous standup with all agents in the lab. Pulls each agent's last 24h activity, asks for blockers, captures action items.",
  arguments: [
    { name: "type", description: "morning / midday / evening", required: true }
  ]
}

{
  name: "publish_ready_check",
  description: "Run a single round of the publish-ready loop on a paper (per PRD §37). Specify which round to run.",
  arguments: [
    { name: "paper_id", required: true },
    { name: "round", description: "1=mechanical_qa / 2=cross_model / 3=houston_method_sweep / 4=visual_format / 5=arxiv_package", required: true }
  ]
}

{
  name: "no_punt_check",
  description: "Scan a draft for the 7 'no future-research punt' trigger phrases per PRD §13.1. Return any matches with surrounding context so the author can rewrite them.",
  arguments: [
    { name: "draft_text", description: "Either inline draft text or a file path", required: true }
  ]
}
```

**Total prompts for v1: 6 templates** covering the most common multi-step research workflows.

---

## 5. Authentication & scoping

### 5.1 Token format

Same JWT format as `API_SPEC.md` §2.1. The MCP server validates the token and extracts:
- `sub` — the agent identity
- `scope` — the labs the agent can access
- `type` — user / agent / service

### 5.2 The Lab Sovereignty Rule at the MCP layer

Per PRD §40.11 (the HARD invariant): cross-lab tool calls obey strict rules.

| Tool | Cross-lab behavior |
|---|---|
| `read_file` | ✅ Allowed if the agent's token has at least `lab:<target>:r` scope |
| `list_files` | ✅ Same |
| `write_file` | ❌ NEVER allowed cross-lab. Returns `403 forbidden` with type `cross-lab-write-denied`. |
| `delete_file` | ❌ NEVER allowed cross-lab. |
| `dispatch_experiment` | ❌ NEVER allowed cross-lab — experiments dispatch into the lab that owns the agent. |
| `comm_send` | ✅ THIS is the cross-lab pattern — send a suggestion via the comms gateway, the destination orchestrator decides. |
| `note_save` | ❌ NEVER allowed cross-lab — notes are private to the lab. |

The rule is enforced at the MCP server layer BEFORE the underlying API call is made. Any cross-lab write attempt is rejected with a clear error message that the calling agent (and the LLM driving it) can read.

### 5.3 Per-tool permission checks

Each tool's handler does:
```typescript
async function handleReadFile(input, ctx) {
  const targetLab = input.lab || ctx.currentLab;
  if (!ctx.token.scopes.some(s => s === `lab:${targetLab}:r` || s === `lab:${targetLab}:rw` || s === `lab:${targetLab}:admin`)) {
    throw new MCPError("forbidden", `Token lacks read access to lab '${targetLab}'`);
  }
  // ... call the API endpoint
}
```

### 5.4 Audit logging

Every tool call is logged to `lab/audit/mcp-<agent-name>.jsonl` with:
```json
{
  "ts": "2026-04-08T15:30:00Z",
  "agent": "peer-review-gpt",
  "tool": "read_file",
  "input": { "path": "arxiv/main.tex" },
  "result": "success",
  "duration_ms": 47,
  "lab": "bigbounce-hubify"
}
```

Failed calls are logged with the error type. The audit log is append-only, never deleted, and is part of the lab's nightly backup to Backblaze B2.

---

## 6. Transport

The MCP server runs on three transports simultaneously:

### 6.1 stdio (for local processes)

Used by:
- Claude Code (when `claude --mcp-server hubify-labs`)
- Cursor (when configured in `~/.cursor/mcp.json`)
- VS Code MCP extension
- Any local CLI tool that wants to talk to the server

Configuration in the user's MCP client:
```json
{
  "mcpServers": {
    "hubify-labs": {
      "command": "hubify",
      "args": ["mcp", "serve", "--lab", "bigbounce-hubify"]
    }
  }
}
```

The CLI's `mcp serve` subcommand runs the MCP server in stdio mode and passes the lab scope from CLI args.

### 6.2 SSE / Streamable HTTP (for remote clients)

Used by:
- Claude Desktop (remote MCP server connection)
- Web-based agents
- The Hubify Labs platform's own agent runtime on Fly.io

Endpoint: `https://hubify-labs.com/v1/mcp/sse`

Auth: Bearer token in the `Authorization` header. The server reads the token, validates it, scopes the connection to the labs the token grants access to.

### 6.3 WebSocket (for the platform's internal agent runtime)

The Fly.io agent runtime (orchestrator + leads + workers) connects via WebSocket for lower latency on the comm-event flow. Same MCP protocol, just a different transport.

---

## 7. Error handling

All tool errors use the same RFC 7807 error format from `API_SPEC.md` §5, wrapped in MCP's standard error envelope:

```typescript
{
  isError: true,
  content: [{
    type: "text",
    text: JSON.stringify({
      type: "https://hubify-labs.com/errors/forbidden",
      title: "Cross-lab write denied",
      status: 403,
      detail: "Agent 'peer-review-gpt' (lab:bigbounce-hubify) cannot write to lab:dark-energy-lab. See PRD §40.11 Lab Sovereignty Rule.",
      instance: "/v1/labs/dark-energy-lab/files/notes/test.md"
    })
  }]
}
```

Common error types specific to MCP:
- `cross-lab-write-denied` (the Lab Sovereignty Rule)
- `tool-input-validation-failed`
- `agent-not-found`
- `experiment-spec-incomplete` (missing `requires_gpu` per PRD §41 Rule 1)
- `n4-not-claimable-by-agent` (tried to claim N4 contribution)

---

## 8. The MCP YAML lock

Just like the API has `api-spec.openapi.yaml`, the MCP server has:

```
project-context/mcp-server-spec.yaml
```

(This file is the next item in Category E — to be written after this human-readable spec is locked.)

The YAML enables:
- Auto-generated MCP server stub in TypeScript (`@hubify-labs/mcp-server`)
- Auto-generated type definitions for tool inputs/outputs
- MCP inspector / debugger compatibility (run the spec through `mcp-inspect` to validate)
- Documentation generation (each tool/resource/prompt becomes a docs page)

---

## 9. The `hubify mcp` CLI subcommand

The CLI (Category F, TBD) ships an `mcp` subcommand for easy server management:

```bash
hubify mcp serve --lab bigbounce-hubify          # Run the MCP server (stdio mode)
hubify mcp serve --lab bigbounce-hubify --sse    # Run in SSE mode on a local port
hubify mcp tools list                             # List all tools the server exposes
hubify mcp tools describe <tool-name>             # Show schema for a specific tool
hubify mcp resources list                         # List all resources
hubify mcp prompts list                           # List all prompt templates
hubify mcp test <tool-name> --input '{...}'       # Test-call a tool with sample input (validates auth + schema)
hubify mcp audit                                  # Tail the MCP audit log
```

This makes it trivial for Houston (or any researcher) to spin up an MCP server on their local machine and point Claude Code at it.

---

## 10. Out of scope for v1

- ❌ Sampling (the MCP primitive where the server asks the client to run an LLM call) — defer to v1.1, no current use case
- ❌ Resource subscriptions via the standard MCP `subscribe` method — v1 uses our own SSE streams instead
- ❌ Multi-tenant MCP server (one MCP server serves multiple users) — v1 is single-user (Houston), the multi-tenant story comes in v1.2
- ❌ MCP server federation (one Hubify Labs MCP server proxying tool calls to another lab's server) — v1 uses comm-send for cross-lab, federation is v1.2+
- ❌ Custom tool annotations (audience, dangerous, etc.) — v1.1
- ❌ MCP server discovery via mDNS — v1.1

---

## 11. The next steps

After this spec is reviewed by Houston:

1. **Lock the MCP YAML** — turn this human-readable spec into `mcp-server-spec.yaml` (the machine-readable contract)
2. **Generate the TypeScript stub** — `@hubify-labs/mcp-server` package with handler functions for each tool
3. **Implement the handlers** — each handler is a thin wrapper around the corresponding REST API endpoint from `API_SPEC.md`
4. **Wire to Claude Code** — Houston configures `~/.claude/mcp.json` to point to the local `hubify mcp serve` command
5. **First end-to-end test** — Houston asks Claude Code "what's the current credit balance and how many experiments are running?" and gets a real answer via `runpod_status` + `list_pods` tool calls

---

## 12. Open questions

1. **TypeScript SDK vs direct implementation** — use `@modelcontextprotocol/sdk` (official Anthropic SDK) or roll our own? Default: use the SDK (faster + maintained + spec-compliant).
2. **Resource update strategy** — push (server announces changes) vs pull (client polls)? Default: SSE streams for live resources, pull for snapshots. MCP supports both.
3. **MCP server hosting for the SSE transport** — Fly.io alongside the orchestrator vs separate Vercel function vs Convex HTTP route? Default: Convex HTTP route (simpler, single deployment).
4. **Tool descriptions tuning** — LLMs decide which tool to call based on the description text. Iterate after first usage.
5. **Audit log retention** — forever vs 90 days vs 1 year? Default: forever (audit is load-bearing for lab governance).

---

## 13. What this spec stress-tests

- **MCP as the universal agent surface** — proves that one server can serve Claude Code locally (stdio), Claude Desktop remotely (SSE), and the platform's own agents (WebSocket) without per-client special cases
- **The Lab Sovereignty Rule** at the MCP layer — cross-lab writes are blocked at the protocol boundary, not just the API
- **The §41 routing discipline** — `dispatch_experiment` requires `requires_gpu` as a hard input, agents cannot dispatch GPU work without thinking about it
- **The N-score discipline** — `contribution_create` rejects N4 claims at the protocol level, agents cannot self-promote
- **The note privacy contract** — `note_save` requires `explicit_user_consent: true`, agents cannot autonomously save notes
- **The chat no-action mode** — `chat_message` carries a mode field that the orchestrator respects, agents can't sneak actions into chats

If the MCP server ships and Houston can run `hubify mcp serve` from his terminal and have Claude Code drive Hubify Labs end-to-end, the agent integration layer is locked.

---

## 14. Status

**This file:** Category E item 1 of the BUILD_READINESS_CHECKLIST. Bootstraps Category E from 0% → ~85% in one shot:

- ✅ Item 1: Write MCP_SERVER_SPEC.md (this file)
- ✅ Item 2: Tool definitions (~30 tools across 11 categories)
- ✅ Item 3: Resource definitions (~15 resources, including 5 live SSE streams)
- ✅ Item 4: Prompt templates (6 templates for the most common workflows)
- ✅ Item 5: Auth flow (JWT + per-lab scoping + Lab Sovereignty Rule enforcement)
- ✅ Item 6: Audit logging (every tool call → `lab/audit/mcp-<agent>.jsonl`)
- ⏸ Item 7: MCP YAML lock — `mcp-server-spec.yaml` (next Category E iteration)

**6 of 7 Category E items checked off in this single iteration.**
