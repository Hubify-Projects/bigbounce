# Pi Agent Study — indydevdan's multi-agent CLI

**Date:** 2026-04-08
**Status:** Research for Hubify Labs terminal integration
**Primary source:** https://github.com/disler/pi-vs-claude-code (665 stars, TypeScript, updated 2026-03-11)
**Upstream:** https://github.com/badlogic/pi-mono (Mario Zechner's monorepo, MIT)
**Website:** https://shittycodingagent.ai (yes, really — domain donated by exe.dev)
**npm:** `@mariozechner/pi-coding-agent`

---

## TL;DR

- **Pi is not indydevdan's project.** Pi is built by **Mario Zechner (badlogic)**, a standalone open-source TypeScript coding agent CLI published on npm as `@mariozechner/pi-coding-agent` and distributed as the `pi-mono` monorepo. IndyDevDan (Daniel "disler" Pace) built `pi-vs-claude-code` — a showcase repo of 16 TypeScript extensions that demonstrate multi-agent orchestration, safety auditing, and UI customization on top of Pi. The real architecture lives in Mario's code; Dan's contribution is the applied patterns (subagent-widget, agent-team, tilldone, damage-control).
- **Pi and Claude Code are not rivals in the way Houston thinks.** Pi is a *minimal harness* (~200-token system prompt, 4 tools: read/write/edit/bash) designed to be extended in-process via TypeScript. Claude Code is a *batteries-included product* (~10K-token system prompt, 10+ tools, native sub-agents, MCP, IDE integrations). They can absolutely coexist: Pi's `subagent-widget.ts` uses `spawn("pi", args)` to fork child Pi processes for sub-agents, and there is nothing stopping Pi from spawning `claude --print` instead (or vice versa). Dan's repo even ships a `cross-agent.ts` extension that scans `.claude/agents/` directories to let Pi consume Claude Code's agent definitions.
- **For Hubify Labs, the recommendation is: Claude Code as the primary reasoning engine, Pi-style patterns as the borrowed vocabulary, neither tool runs in the Labs platform's runtime.** Hubify Labs should ship its own Convex-native agent orchestrator that *looks* like Pi's TUI (dispatcher dashboard, live widgets, tilldone gating) and *delegates* reasoning to `claude --print --output-format stream-json`. We do not install Pi as a dependency. We steal the UX primitives (differential rendering, status widgets, lead/worker dashboard, color-coded activity feed) and implement them in our own React/Convex stack. This is the same pattern Pi itself uses to spawn sub-agents: headless subprocess, JSONL streaming, live UI overlay.

---

## Repo Identification

**How I found it.** The user said "indydevdan ui-agents Pi." GitHub search for `indydevdan` redirects to `disler` (Daniel Pace, YouTube handle IndyDevDan). His repo list includes:

| Repo | Stars | Relevance |
|------|------:|-----------|
| `disler/pi-vs-claude-code` | 665 | **Primary** — the extension showcase |
| `disler/claude-code-hooks-multi-agent-observability` | — | Backend sync pattern (Bun/SQLite/Vue dashboard) |
| `disler/big-3-super-agent` | 295 | Gemini + OpenAI + Claude Code multi-provider |
| `disler/single-file-agents` | 433 | Self-contained Python agents |
| `disler/nano-agent` | 199 | MCP server, small-scale agents |
| `disler/bowser` | 214 | Browser automation via composable skills |
| `disler/the-library` | 311 | Meta-skill for distributing agentics |
| `disler/infinite-agentic-loop` | — | Parallel agent orchestration via slash command |
| `disler/indydevtools` | — | Older opinionated agent toolbox |

None of Dan's repos are named `ui-agents` or `pi-agent` exactly — the thing Houston has been calling "ui-agents Pi" is the `pi-vs-claude-code` repo, which is a collection of TypeScript extensions for Mario Zechner's Pi agent. The ui-agents association likely comes from `disler/bowser` (an agentic browser automation / UI testing system).

**The actual Pi project** (not Dan's) is Mario Zechner's `pi-mono` monorepo at https://github.com/badlogic/pi-mono. It contains seven packages:

| Package | Purpose |
|---------|---------|
| `@mariozechner/pi-ai` | Unified multi-provider LLM API (OpenAI, Anthropic, Google, 20+ providers) |
| `@mariozechner/pi-agent-core` | Agent runtime, tool calling, state management |
| `@mariozechner/pi-coding-agent` | The `pi` CLI itself — interactive coding agent |
| `@mariozechner/pi-tui` | Terminal UI library with differential rendering |
| `@mariozechner/pi-mom` | Slack bot that delegates to pi |
| `@mariozechner/pi-web-ui` | Web components for chat interfaces |
| `@mariozechner/pi-pods` | CLI for vLLM GPU pod deployment |

**Language:** TypeScript (95.9%), minor JavaScript. Runs on Bun (≥1.3.2) and Node.js.
**License:** MIT (broad commercial and personal use).
**Installation:** `npm install -g @mariozechner/pi-coding-agent`, then run `pi`.
**Last meaningful activity:** Maintainer on an "OSS weekend" hiatus through April 13 2026 for internal refactoring.

---

## What Pi Is

Pi is a **minimal terminal coding harness** built on the philosophy "if I don't need it, it won't be built." It ships with a ~200-token system prompt (vs. Claude Code's ~10K), four tools (`read`, `write`, `edit`, `bash`), and a plugin architecture based on in-process TypeScript extensions loaded via `jiti` at runtime. The agent itself is the thing that's supposed to write new tools — Pi explicitly rejects MCP because it treats the skill ecosystem as a failure mode.

Pi runs in four modes:

1. **Interactive** — full terminal UI with editor, footer, and history
2. **Print / JSON** — `pi --print` for non-interactive scripting with `stream-json` output
3. **RPC** — bidirectional JSONL protocol for cross-language process integration (26+ commands)
4. **SDK** — embed in TypeScript applications via `createAgentSession()`

The minimal SDK pattern looks like this (file: `packages/coding-agent/examples/sdk/01-minimal.ts`):

```typescript
import { createAgentSession } from "@mariozechner/pi-coding-agent";

const { session } = await createAgentSession();

session.subscribe((event) => {
  if (event.type === "message_update" && event.assistantMessageEvent.type === "text_delta") {
    process.stdout.write(event.assistantMessageEvent.delta);
  }
});

await session.prompt("What files are in the current directory?");
```

That's it. The SDK auto-discovers skills, extensions, and tools from `./` and `~/.pi/agent`, picks a model from settings, and streams text deltas. For more control, the `06-extensions.ts` example shows how extensions are wired in:

```typescript
const resourceLoader = new DefaultResourceLoader({
  additionalExtensionPaths: ["./my-logging-extension.ts", "./my-safety-extension.ts"],
  extensionFactories: [
    (pi) => {
      pi.on("agent_start", () => {
        console.log("[Inline Extension] Agent starting");
      });
    },
  ],
});
```

The `pi` object passed to extension factories is the central API surface — `pi.on()` for events, `pi.registerTool()` for tools, `pi.registerCommand()` for slash commands, `pi.ui.*` for rendering.

**Philosophy quote from Armin Ronacher's Pi blog post** (https://lucumr.pocoo.org/2026/1/31/pi/):

> Pi is a minimal coding agent... with the shortest system prompt of any agent that I'm aware of. Only four core tools: Read, Write, Edit, and Bash. [Pi's] design prioritizes self-extension over downloading pre-built tools. Rather than relying on external skill markets, the agent itself writes code to extend its capabilities.

Ronacher also notes that **OpenClaw** (Peter Norvig's recent project) is built on Pi components, so Pi is being used as a foundational library for at least one production-ish system besides `pi-coding-agent` itself.

---

## Multi-Agent Patterns

This is the bulk of what Houston cares about. Pi ships with NO native sub-agent support — the COMPARISON.md file is explicit:

> **Sub-Agents:** Claude Code: Native Task tool (7 parallel). Pi Agent: Extension-based (separate processes).

But Dan's `pi-vs-claude-code` repo implements three multi-agent patterns as extensions. Each is worth studying carefully.

### 1. `subagent-widget.ts` — fire-and-forget background subprocess

This is the simplest pattern: the user types `/sub <task>` and a background `pi` subprocess is spawned, with a live-updating widget rendered in the main TUI showing progress.

**Spawning mechanism** (file: `extensions/subagent-widget.ts`):

```typescript
const { spawn } = require("child_process");
// Spawns: spawn("pi", [...args], { stdio: ["ignore", "pipe", "pipe"] })
```

The stdin is ignored; stdout and stderr are piped back and parsed line-by-line as JSON events. Each event mutates the widget's render state:

- `message_update` with `text_delta` — appended to `state.textChunks`
- `tool_execution_start` — increments `state.toolCount`
- An interval timer ticks `state.elapsed` every 1000ms

**Widget rendering**:

```typescript
import { Container, Text } from "@mariozechner/pi-tui";
import { DynamicBorder } from "@mariozechner/pi-coding-agent";

// ...

ctx.ui.setWidget(key, renderFn);  // register/update widget
```

The widget shows status icons (`● running`, `✓ done`, `✗ failed`), a task preview, elapsed time, and a tool call count. Theme colors are applied through `theme.fg("accent", text)`, `theme.fg("success", text)`, etc.

**Four tools registered:** `subagent_create`, `subagent_continue`, `subagent_remove`, `subagent_list`.
**Four slash commands:** `/sub`, `/subcont`, `/subrm`, `/subclear`.

This is literally how Pi spawns child Pi processes. It would work identically with `claude --print --output-format stream-json` — the only thing you'd need to change is the JSON schema for parsing events.

### 2. `agent-team.ts` — dispatcher/specialist pattern with live grid dashboard

This is the pattern Houston wants. The dispatcher agent has NO codebase access — all its tools are disabled except `dispatch_agent`:

```typescript
pi.registerTool({
  name: "dispatch_agent",
  parameters: Type.Object({
    agent: Type.String({ description: "Agent name (case-insensitive)" }),
    task: Type.String({ description: "Task description for the agent" }),
  }),
  async execute(_toolCallId, params, _signal, onUpdate, ctx) {
    const { agent, task } = params;
    // delegates to dispatchAgent() function
  }
});

// Critical: only dispatch_agent is allowed at the top level
pi.setActiveTools(["dispatch_agent"]);
```

The dispatcher's system prompt is dynamically constructed with the team roster and rules:

> NEVER try to read, write, or execute code directly — you have no such tools. ALWAYS use dispatch_agent to get work done.

**Agents are defined in markdown files** with YAML frontmatter in any of these paths:

- `agents/*.md`
- `.claude/agents/*.md` (note: compatible with Claude Code's agent directory!)
- `.pi/agents/*.md`

The parser extracts metadata:

```typescript
interface AgentDef {
  name: string;
  description: string;
  tools: string;          // comma-separated tool list
  systemPrompt: string;   // content after frontmatter
  file: string;
}

const frontmatter: Record<string, string> = {};
for (const line of match[1].split("\n")) {
  const idx = line.indexOf(":");
  if (idx > 0) {
    frontmatter[line.slice(0, idx).trim()] = line.slice(idx + 1).trim();
  }
}
```

**Team rosters** are defined in `.pi/agents/teams.yaml`:

```yaml
team-name:
  - agent-name-1
  - agent-name-2
```

Only members of the active team become dispatch targets.

**Specialist spawning** uses the same subprocess pattern as subagent-widget, but with per-agent arguments:

```typescript
const proc = spawn("pi", args, {
  stdio: ["ignore", "pipe", "pipe"],
  env: { ...process.env },
});
```

With args:
- `--mode json` — streaming JSON events
- `--tools <tool-whitelist>` — restricted to the agent's declared tools
- `--session <file>` — persistent session file for memory
- `-c` — continue existing session if it exists
- final argument: the task string

**Per-specialist state**:

```typescript
interface AgentState {
  status: "idle" | "running" | "done" | "error";
  task: string;
  toolCount: number;
  elapsed: number;
  lastWork: string;        // last output line
  contextPct: number;      // token usage %
  sessionFile: string | null;
  runCount: number;
}
```

**The grid dashboard** is the visual pattern Houston has been asking about. It renders agent cards with:
- Status indicator (`○` idle, `●` running, `✓` done, `✗` error)
- Elapsed time
- Context usage as a 5-block visualization bar
- Current task or last work output

Grid columns auto-size based on agent count:
- 1-3 agents: one column per agent
- 4+ agents: 2-3 columns depending on terminal width
- User override: `/agents-grid <1-6>`

**Commands:**
- `/agents-team` — select active team from `teams.yaml`
- `/agents-list` — show loaded agents, statuses, session files, run counts
- `/agents-grid N` — set dashboard column count

### 3. `agent-chain.ts` — sequential pipeline with variable substitution

This is the simplest orchestration pattern. Chains are defined in `.pi/agents/agent-chain.yaml`:

```yaml
chain-name:
  description: "Human-readable description"
  steps:
    - agent: agent-name
      prompt: "Task with $INPUT and $ORIGINAL placeholders"
    - agent: another-agent
      prompt: "Next step using previous output"
```

Execution is a simple sequential loop:

```javascript
const resolvedPrompt = step.prompt
  .replace(/\$INPUT/g, input)
  .replace(/\$ORIGINAL/g, originalPrompt);
```

- `$INPUT` — output from previous step (or original task for step 1)
- `$ORIGINAL` — never changes; always the user's initial prompt
- If any step's exit code ≠ 0, the pipeline halts with an error

This is a flat sequence — no branching, no parallelism, no retry. It's the "bash pipeline for agents" primitive.

### 4. `pi-pi.ts` — meta-agent with parallel research experts

The repo also ships a `pi-pi.ts` extension that spawns multiple specialists in parallel (ext-expert, theme-expert, tui-expert) to research Pi framework documentation. Each expert has its own session file and tool whitelist. Results are aggregated for the user. This is a variant of agent-team with parallel execution, specifically for meta-tasks about Pi itself.

---

## Claude Code Integration

This is the core question. Let me answer it directly.

**Does Pi use Claude Code internally?** No. Pi has its own agent runtime (`pi-agent-core`), its own model abstraction (`pi-ai`, supporting 20+ providers), and its own TUI (`pi-tui`). It does not depend on Anthropic's SDK, does not shell out to `claude`, and does not use any Claude Code infrastructure.

**Does Claude Code use Pi internally?** Absolutely not. Claude Code is closed-source and built by Anthropic.

**Can they interoperate?** Yes, in three ways:

### A) Pi's `cross-agent.ts` consumes Claude Code agent definitions

From the `cross-agent.ts` source: the extension scans `.claude/`, `.gemini/`, and `.codex/` directories in both project and home folders on the `session_start` event, then registers:
- Claude Code commands as `/name` slash commands
- Claude Code skills as `/skill:name` commands
- Other agents as discoverable `@name` references

This is **one-directional resource aggregation**. Pi reads Claude Code's filesystem artifacts and re-exposes them in its own runtime. It does not invoke `claude`. There is no bidirectional IPC.

### B) Pi can spawn Claude Code as a subprocess (and vice versa)

Nothing in `subagent-widget.ts` is Pi-specific except the JSON schema for parsing events. The spawn call:

```typescript
spawn("pi", args, { stdio: ["ignore", "pipe", "pipe"] })
```

...could trivially be:

```typescript
spawn("claude", ["--print", "--output-format", "stream-json", task],
      { stdio: ["ignore", "pipe", "pipe"] })
```

Claude Code's `--print` mode with `stream-json` output emits a well-documented JSONL event stream (tool_use, text_delta, message_stop) that maps cleanly onto Pi's widget state machine. Every Pi orchestration pattern (subagent-widget, agent-team, agent-chain) could swap in Claude Code as the worker with minor JSON schema changes.

Conversely, Claude Code's Task tool can invoke any binary via its bash tool, so Claude Code can call `pi --print` as a headless worker for tasks where Pi's extensibility is useful.

### C) Shared Agent Skills standard

Both Pi (via `cross-agent.ts`) and Claude Code follow the Agent Skills standard for distributing skills as markdown files with frontmatter. Skills written for one tool work in the other. This is the deepest level of "integration" — a shared filesystem convention, not runtime IPC.

**What Pi does that Claude Code doesn't:**
- ~200-token system prompt vs ~10K (more context for actual work)
- 20+ providers natively vs Anthropic-centric
- In-process TypeScript hooks (25+ events) vs out-of-process shell hooks
- Session JSONL tree with branching/forking vs linear conversation
- Full TUI customization (custom header, footer, widgets, overlays, editors)
- Unified thinking levels across all capable models
- RPC mode for cross-language integration
- `pi -e <path.ts>` ephemeral extension loading (no install)

**What Claude Code does that Pi doesn't:**
- Native sub-agents with permission inheritance (Pi requires extensions + subprocess)
- Native MCP support (Pi rejects MCP by design)
- Plan mode (read-only exploration)
- IDE integrations (VS Code, JetBrains, Cursor)
- Web/mobile/desktop surfaces (claude.ai/code, native apps)
- Enterprise SSO, MFA, audit logs, sandboxing (5 modes)
- Built-in glob, WebSearch, WebFetch, NotebookEdit tools
- Plugin marketplace with enterprise allowlists
- Opus 4.6 with extended thinking and the deepest reasoning available
- `permission_asked` / `subagent_lifecycle` / `teammate_idle` hooks

They are not drop-in replacements. Claude Code is a product; Pi is a library you program against.

---

## TUI / Activity Feed

Houston's "color-coded activity feed" question is about how Pi renders multiple concurrent agent outputs without the terminal becoming an illegible mess. The answer is `pi-tui`, and it's a real differential-rendering TUI library — not Ink (React), not Rich (Python), not Bubble Tea (Go). It's purpose-built.

**pi-tui core features:**

- **Three-strategy differential rendering** — updates only changed content
- **Synchronized output via CSI 2026** — atomic screen updates, no flicker
- **Component interface**: `render(width)` returns string arrays, plus `handleInput()` and `invalidate()`
- **Focusable interface** with IME positioning via `CURSOR_MARKER`
- **Overlay system** — anchored, positioned overlays with sizing flexibility
- **Theme support** with 51 color tokens, hot-reloadable JSON themes

**Exported components:**

| Component | Purpose |
|-----------|---------|
| `TUI` | Root container managing all components |
| `Container` | Groups child components |
| `Box` | Padding and background |
| `Text` | Multi-line text with word wrapping |
| `TruncatedText` | Single-line truncation |
| `Input` | Single-line text input |
| `Editor` | Multi-line with autocomplete and scrolling |
| `SelectList`, `SettingsList` | List components |
| `Spacer`, `Image`, `Loader`, `Markdown` | Utility |
| `ProcessTerminal` | Terminal abstraction |

**How the footer is drawn** (file: `extensions/minimal.ts`):

```typescript
pi.ui.setFooter((ctx) => ({
  dispose() { /* cleanup */ },
  invalidate() { /* refresh */ },
  render(width) {
    const model = ctx.model?.id ?? "unknown";
    const pct = ctx.getContextUsage();
    const filled = Math.round(pct / 10);
    const bar = "#".repeat(filled) + "-".repeat(10 - filled);
    const left = theme.fg("dim", ` ${model}`);
    const right = theme.fg("dim", `[${bar}] ${Math.round(pct)}% `);
    // center-pad to width
    return [composedLine];
  }
}));
```

Note the API: `pi.ui.setFooter()` takes a **function returning an object with `render(width)` that returns an array of strings**. The strings contain embedded ANSI codes via `theme.fg("colorName", text)`. Width is passed so the renderer can justify content. `visibleWidth()` and `truncateToWidth()` handle ANSI-aware length calculations.

**Widgets** (for the agent-team dashboard and subagent cards):

```typescript
ctx.ui.setWidget(key, renderFn)  // register/update
ctx.ui.notify(message, type)     // toast notifications
```

Widgets render above or below the editor, persistent across turns. The agent-team grid dashboard is multiple widgets in a grid layout. Each widget renders its own status bar, context percentage, and last-work line.

**Streaming vs frame rendering.** Pi streams incrementally: every `message_update` or `tool_execution_*` event triggers an `invalidate()` on the widget, which calls `render(width)` and emits only the diff to the terminal via CSI 2026 synchronized output. This is why multiple sub-agent cards can update concurrently without tearing or flicker.

**Handling multiple agent outputs in one terminal.** The pattern is: a single root TUI, a grid container holding N agent cards (widgets), and N background subprocesses each writing JSONL to stdout. The extension parses each subprocess's stream and routes updates to the corresponding widget. The differential renderer handles the rest. This is exactly what the agent-team.ts grid dashboard does.

---

## Tilldone Pattern

Houston has referenced "tilldone" multiple times. Here's what it actually is.

**tilldone is NOT a lead/worker takeover pattern.** It's a *self-discipline* gating mechanism for a single agent. The extension forces the agent to declare a task list before it can use any tool except the tilldone tool itself, and it nudges the agent at `agent_end` if tasks remain incomplete.

**Source** (file: `extensions/tilldone.ts`):

The extension implements a three-state lifecycle per task:

```
idle → inprogress → done
```

Only one task can be `inprogress` at a time; if the agent starts a new task, any previously in-progress tasks auto-demote to `idle`.

**Task state**:

```typescript
interface Task {
  id: number;
  text: string;
  status: "idle" | "inprogress" | "done";
}

// Extension state
{
  tasks: Task[];
  nextId: number;
  listTitle?: string;
  listDescription?: string;
  nudgedThisCycle: boolean;
}
```

**Blocking gate** (on `tool_call` event):

The extension intercepts every `tool_call` event. If `toolName !== "tilldone"` and there are no tasks (or no active task), the extension returns `{ block: true, reason: "..." }` forcing the agent to create and activate a task first.

**Auto-nudge on agent_end**:

```typescript
pi.on("agent_end", async (event, ctx) => {
  if (hasIncompleteTasks() && !state.nudgedThisCycle) {
    state.nudgedThisCycle = true;
    // inject a custom "tilldone-nudge" message back into the agent
  }
});
```

This effectively loops the agent until all tasks are done or the user intervenes. It's "keep going until done" as a policy layer.

**Session recovery via branch reconstruction**:

```typescript
// On session_start, session_switch, session_fork, session_tree:
for (const entry of ctx.sessionManager.getBranch()) {
  if (entry.type === "tool_call" && entry.toolName === "tilldone") {
    // extract task/nextId/title from tool results
  }
}
```

State is reconstructed from the JSONL session tree on every session event. No external persistence — tilldone state lives in the conversation history itself.

**UI surfaces:**
- Footer: persistent progress indicator (e.g., `[3/7] doing thing`)
- Widget: current task card above editor
- Status line: compact task name
- `/tilldone` slash command: overlay with full task list

**What tilldone is NOT:**
- Not lead/worker failover
- Not parallel agent orchestration
- Not a retry loop for failed tools
- Not inter-agent task delegation
- Not connected to the subagent-widget or agent-team extensions (those are separate)

**The "failure recovery" Houston has in mind** (lead agent takes over when worker fails) is not tilldone. That would be a new extension. You could implement it easily by combining agent-team's dispatcher pattern with a `tool_execution_end` hook that detects `exitCode ≠ 0` and re-dispatches to a different specialist — but no shipped extension does this.

---

## Sync to Backend

Pi does **not** emit events to a database or webhook out of the box. All state lives in local JSONL session files (`~/.pi/agent/sessions/`) and in-memory extension state. Extensions run in-process, so there's no network layer.

**But** the event system is the integration point. Every pi extension can hook into the 25+ events and push them anywhere:

```typescript
pi.on("tool_execution_start", async (event, ctx) => {
  await fetch("https://labs.hubify.app/api/agent-events", {
    method: "POST",
    body: JSON.stringify({
      runId: currentRunId,
      type: "tool_start",
      toolName: event.toolName,
      timestamp: Date.now(),
    }),
  });
});
```

You could build a 50-line extension that mirrors every interesting event to Convex. The event types Pi exposes (from the PI_VS_OPEN_CODE.md comparison):

- **Input**: `input` (intercept, transform, block user prompts)
- **Agent lifecycle**: `agent_start`, `before_agent_start`, `agent_end`
- **Tool lifecycle**: `tool_call` (before exec, blockable), `tool_execution_start`, `tool_execution_update`, `tool_execution_end`
- **Messages**: `message_update` (with `text_delta` sub-events), `message_end`
- **Session**: `session_start`, `session_switch`, `session_fork`, `session_before_fork`, `session_tree`
- **Bash**: `BashSpawnHook` (modify command/cwd/env before spawn)
- **Context**: `context` (access all messages for filtering/pruning)
- **Model**: `model_select` (react to mid-session model switches)

**Dan's `claude-code-hooks-multi-agent-observability` repo** implements exactly this pattern for Claude Code (not Pi, but the architecture is identical):

> **Data Flow:** Claude Agents → Hook Scripts → HTTP POST → Bun Server → SQLite → WebSocket → Vue Client

Components:
1. **Hook scripts** in `.claude/hooks/` (Python via `uv`) — intercept Claude Code events, POST to server
2. **Bun server** on port 4000 — `POST /events`, `GET /events/recent`, `WS /stream`, SQLite with WAL mode
3. **Vue 3 frontend** on port 5173 — real-time dashboard via WebSocket

For Pi, the equivalent is **an extension that POSTs events to your backend**. For Hubify Labs, swap SQLite for Convex and Vue for the existing React dashboard. The pattern is the same: hook → HTTP → DB → WebSocket → UI.

**Convex integration sketch** for Pi:

```typescript
// extensions/convex-mirror.ts
import { ConvexHttpClient } from "convex/browser";

export default function(pi: ExtensionAPI) {
  const convex = new ConvexHttpClient(process.env.CONVEX_URL!);

  pi.on("tool_execution_start", async (event, ctx) => {
    await convex.mutation("agentEvents:logToolStart", {
      runId: ctx.sessionId,
      toolName: event.toolName,
      ts: Date.now(),
    });
  });

  pi.on("agent_end", async (event, ctx) => {
    await convex.mutation("agentEvents:logAgentEnd", {
      runId: ctx.sessionId,
      exitCode: event.exitCode,
      ts: Date.now(),
    });
  });
}
```

One file. `pi -e extensions/convex-mirror.ts` and every Pi session streams to Convex.

---

## Recommendation for Hubify Labs

Here's my honest take, broken down by where each tool fits.

### Use Claude Code as the primary reasoning engine

Claude Code is the strongest single-agent tool Anthropic ships. It has Opus 4.6 extended thinking, the 1M context window, the best tool-calling accuracy, and — critically for Hubify Labs — it ships in a form factor Hubify already uses daily. Houston is the primary user; Houston uses Claude Code; therefore Claude Code is the default worker in Hubify Labs's agent pool.

In the Labs platform's agent hierarchy (per PRD §3), Claude Code fills the **specialist / worker** role for anything requiring deep reasoning:
- Code review
- Plan generation
- Root-cause analysis
- Content drafting
- Deep research

We invoke it as `claude --print --output-format stream-json <task>` from a subprocess. The JSONL event stream is parsed and routed to the Labs activity feed in Convex, same pattern as Dan's observability repo.

### Do NOT install Pi as a dependency

Pi is an excellent piece of software. But installing it creates three problems:

1. **Two config surfaces to maintain.** Pi has its own model registry, auth storage, session manager, extension loader, theme system, and prompt template engine. We'd be learning Pi's abstractions to get the benefits, when we could write 50 lines of our own.

2. **TypeScript extensions run in Pi's runtime, not ours.** Pi extensions are loaded via jiti in Bun/Node. Hubify Labs is a Convex + React web app. There's a runtime boundary. Integrating Pi means either shelling out to `pi` as a subprocess (in which case we only use Pi as a subprocess spawner, which is wasteful since we could spawn `claude` directly) or embedding the Pi SDK (which pulls in the 7-package monorepo and all its dependencies).

3. **Pi's philosophy is "YOLO by default."** Pi has no sandboxing, no permission dialogs, no deny-first access control. Those are all extensions you bolt on (`damage-control.ts`, `purpose-gate.ts`). For Hubify Labs where users run agents from a web UI, safety has to be native — not an opt-in extension.

### Steal Pi's UX primitives

The real value in the `pi-vs-claude-code` repo isn't the code — it's the *patterns*. Specifically:

| Pi pattern | What to borrow | Where it lives in Labs |
|------------|----------------|------------------------|
| **subagent-widget** live cards | Background task cards in the activity feed, updating in real time | `<AgentCard />` React component driven by Convex subscriptions |
| **agent-team grid dashboard** | The "run dashboard" UI showing N concurrent agents with status, elapsed time, context %, last action | `/runs/:runId` page with grid layout |
| **Dispatcher/specialist pattern** | Primary reasoning agent (Claude Code) dispatches to specialist agents (other Claude Code instances, or cheaper models for grunt work) | Convex function `dispatchSpecialist()` that spawns a worker subprocess and streams events back |
| **agent-chain.yaml** | Sequential pipelines defined as config, not code | `labs-chain.yaml` in each project repo, parsed by the Labs scheduler |
| **tilldone task gating** | Task list declared up front, agent blocked from other work until tasks are complete | `tasks` table in Convex, `toolCall` middleware that checks active tasks before allowing non-task tools |
| **damage-control safety rules** | Regex-based bash command blocking, path-based access control | Labs security middleware that wraps all bash tool calls |
| **purpose-gate session intent** | Force users to declare session intent before the agent starts | Labs onboarding flow: "What are you trying to do?" modal before the first run |
| **Differential rendering (CSI 2026)** | Not applicable (we're web, not terminal) — but the *idea* of atomic widget updates maps to React's batched state updates | React `useTransition` for activity feed updates |
| **Color tokens (51 theme colors)** | The palette vocabulary: `accent`, `success`, `error`, `warning`, `dim`, `muted` | Extend Labs design tokens to match Pi's palette for terminal parity |
| **cross-agent directory scanning** | Auto-discover `.claude/agents/*.md` files in user projects | Labs agent registry that reads project agents on first run |

### The concrete architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Hubify Labs UI                        │
│  (React, Convex subscriptions, design system tokens)    │
│                                                          │
│  ┌──────────┐  ┌──────────────────┐  ┌──────────────┐  │
│  │ Task     │  │ Run Dashboard    │  │ Activity     │  │
│  │ Gating   │  │ (grid of cards)  │  │ Feed (live)  │  │
│  │ (tilldone│  │ [agent-team]     │  │ [subagent-   │  │
│  │ -like)   │  │                  │  │  widget-like]│  │
│  └──────────┘  └──────────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
                         ▲  ▲
               Convex mutations  Convex subscriptions
                         │  │
┌─────────────────────────────────────────────────────────┐
│           Convex Backend (tables + functions)           │
│                                                          │
│  tables: runs, agents, events, tasks, artifacts         │
│  functions: dispatchAgent, logEvent, updateTaskStatus   │
└─────────────────────────────────────────────────────────┘
                         ▲
                     HTTP POST
                         │
┌─────────────────────────────────────────────────────────┐
│              Labs Agent Runner (Node subprocess)        │
│                                                          │
│  For each agent dispatch:                               │
│    spawn("claude", ["--print", "--output-format",      │
│                     "stream-json", task])              │
│    parse JSONL → POST events to Convex                  │
│    on exit → mark run done                              │
│                                                          │
│  Safety layer:                                          │
│    regex-block destructive bash (damage-control)        │
│    enforce path allowlist                               │
│    log every tool call to Convex                        │
└─────────────────────────────────────────────────────────┘
                         ▲
               spawn subprocesses
                         │
┌─────────────────────────────────────────────────────────┐
│   Claude Code specialists  │  Optional: Pi workers      │
│   (the reasoning engine)   │  (for ultra-cheap tasks)   │
└─────────────────────────────────────────────────────────┘
```

### Why Claude Code specifically, not Pi, as the worker

1. **Context efficiency.** Claude Code's 10K system prompt is offset by Opus 4.6's 1M context, so effective working memory is massive. Pi's 200-token prompt is a premature optimization when context is this cheap.
2. **Reasoning depth.** Opus 4.6 extended thinking is the highest-reasoning model publicly available. No Pi config beats this.
3. **Houston's muscle memory.** Houston already has `.claude/agents/`, `.claude/commands/`, CLAUDE.md files everywhere. Pi's `cross-agent.ts` proves these are reusable — but we might as well use Claude Code directly.
4. **Native sub-agents with permission inheritance.** Claude Code's Task tool does in 1 call what Pi's agent-team.ts does in 300 lines.
5. **MCP.** Houston already uses MCP servers (Figma, etc). Claude Code is native; Pi rejects it.
6. **One binary to manage.** `claude` is installed. Pi would be another install, another auth, another config.

### Where Pi might still earn a place

There are two narrow cases where Pi is worth considering:

1. **Cheap-worker tier.** If Hubify Labs ever needs to run bulk, low-reasoning tasks (file reformatting, regex replaces, doc linting) against a cheap model (Groq, Gemini Flash, local Ollama), Pi's 20+ provider support and minimal overhead is actually ideal. You'd use Pi in RPC mode for these workers, and Claude Code for anything requiring reasoning. This is the "right tool for the job" split.

2. **Custom TUI for terminal power users.** If Hubify ever ships a dedicated terminal companion app (not the web Labs UI), `pi-tui` is a genuinely impressive differential-rendering library and Pi's extension model would let us build exactly the multi-agent dashboard Houston wants in a few hundred lines. But this is a v3 concern, not v1.

For v1 of Hubify Labs: **Claude Code is the worker, Convex is the backend, React is the UI, and Pi's patterns are the vocabulary.** Don't install Pi.

---

## What NOT to Borrow

Some things in Pi don't fit Hubify Labs and should be left behind.

1. **YOLO-by-default safety posture.** Pi ships with no sandboxing. For a multi-user web platform, this is unacceptable. Labs must be deny-first like Claude Code's enterprise mode.

2. **JSONL session branching / forking.** Pi's session tree with fork/switch is a power-user feature that adds massive UI complexity. Labs runs should be linear conversations with a clean restart button — not a git-like tree.

3. **Ephemeral extensions (`pi -e <path>`).** Running arbitrary TypeScript from disk is fine for a local CLI but a supply-chain nightmare for a hosted platform. Labs extensions should be reviewed, versioned, and deployed through Convex functions — not loaded from arbitrary paths at runtime.

4. **The "agent writes its own tools" philosophy.** Pi's whole thing is "ask the agent to extend itself." In a hosted multi-tenant platform, that's a sandbox escape vector. Labs tool definitions are static, code-reviewed, and ship with the platform.

5. **Markdown agent files with YAML frontmatter scattered across directories.** Pi reads `agents/*.md`, `.claude/agents/*.md`, `.pi/agents/*.md` — this decentralization is fine for a single-user CLI but becomes a registry hell in a hosted product. Labs should have a single Convex `agents` table.

6. **Terminal-only surface.** Pi has zero web/mobile story. Labs is web-first. We render widgets in React, not ANSI.

7. **In-process TypeScript hooks.** Pi's killer feature is that extensions run in the same runtime as the agent loop, with zero serialization overhead. In Labs, the agent runner is a Node subprocess and the UI is a React app backed by Convex. We have serialization overhead regardless — there's no benefit to in-process.

8. **The `pi-pi.ts` meta-agent pattern.** Cute, but we don't need an agent to research Pi's own documentation. Skip.

9. **`session-replay.ts` timeline overlay.** Replacing it with a Convex-backed history view in the Labs UI is trivial and better.

10. **Name collisions.** The phrase "Pi" is overloaded in this ecosystem: Mario's Pi, `pi-mono`, `@mariozechner/pi-coding-agent`, the npm namespace `@mariozechner/pi-*`, Armin's OpenClaw uses Pi, the `pi-pi.ts` meta-agent, and the website `shittycodingagent.ai`. Don't use the name "Pi" for anything in Hubify Labs — call it what it is (Labs Runner, Labs Dispatch, whatever).

---

## Practical Next Steps for Houston

If Houston wants to prototype the Labs agent runner borrowing from Pi's patterns, here's the concrete sequence:

1. **Read three files in full** (worth 30 min):
   - https://raw.githubusercontent.com/disler/pi-vs-claude-code/main/extensions/subagent-widget.ts
   - https://raw.githubusercontent.com/disler/pi-vs-claude-code/main/extensions/agent-team.ts
   - https://raw.githubusercontent.com/disler/pi-vs-claude-code/main/extensions/tilldone.ts

2. **Look at Dan's observability repo** to see the exact hook-to-backend pattern for Claude Code (this is the closest working reference to what Labs needs):
   - https://github.com/disler/claude-code-hooks-multi-agent-observability
   - Specifically `apps/server/` (Bun + SQLite + WebSocket) and `.claude/hooks/` (Python event senders)

3. **Try Pi locally for a day** just to feel the differential-rendering dashboard and the agent-team grid:
   ```bash
   npm install -g @mariozechner/pi-coding-agent
   git clone https://github.com/disler/pi-vs-claude-code
   cd pi-vs-claude-code && bun install
   just ext-agent-team
   ```
   Houston will learn more from 30 minutes of using the dashboard than from any amount of reading.

4. **Prototype the Labs runner** as a Node process that spawns `claude --print --output-format stream-json <task>`, parses JSONL events, mirrors them to Convex. Start with one agent, no grid. Add the grid dashboard as a React component when the single-agent flow works.

5. **Decide on the task gating model early.** Tilldone is opinionated — the agent can't use other tools until tasks are declared. If Hubify Labs adopts this, it becomes the central UX constraint. If not, you get a free-form agent. I'd recommend tilldone-style for Labs because it gives the activity feed structure.

6. **Do NOT use Pi's tool signatures as Labs's tool signatures.** Pi's minimalism (4 tools) is the wrong choice for Labs. Use Claude Code's full tool suite (read, write, edit, bash, glob, grep, WebFetch, WebSearch, NotebookEdit) and let Labs extensions add more.

---

## References

### Primary source
- [disler/pi-vs-claude-code](https://github.com/disler/pi-vs-claude-code) — Dan's extension showcase
- [disler/pi-vs-claude-code/COMPARISON.md](https://github.com/disler/pi-vs-claude-code/blob/main/COMPARISON.md) — 12-category feature comparison
- [disler/pi-vs-claude-code/PI_VS_OPEN_CODE.md](https://github.com/disler/pi-vs-claude-code/blob/main/PI_VS_OPEN_CODE.md) — architectural comparison vs OpenCode
- [disler/pi-vs-claude-code/extensions/subagent-widget.ts](https://github.com/disler/pi-vs-claude-code/blob/main/extensions/subagent-widget.ts)
- [disler/pi-vs-claude-code/extensions/agent-team.ts](https://github.com/disler/pi-vs-claude-code/blob/main/extensions/agent-team.ts)
- [disler/pi-vs-claude-code/extensions/agent-chain.ts](https://github.com/disler/pi-vs-claude-code/blob/main/extensions/agent-chain.ts)
- [disler/pi-vs-claude-code/extensions/tilldone.ts](https://github.com/disler/pi-vs-claude-code/blob/main/extensions/tilldone.ts)
- [disler/pi-vs-claude-code/extensions/damage-control.ts](https://github.com/disler/pi-vs-claude-code/blob/main/extensions/damage-control.ts)
- [disler/pi-vs-claude-code/extensions/cross-agent.ts](https://github.com/disler/pi-vs-claude-code/blob/main/extensions/cross-agent.ts)
- [disler/pi-vs-claude-code/extensions/minimal.ts](https://github.com/disler/pi-vs-claude-code/blob/main/extensions/minimal.ts)
- [disler/pi-vs-claude-code/extensions/tool-counter.ts](https://github.com/disler/pi-vs-claude-code/blob/main/extensions/tool-counter.ts)

### Upstream Pi project (Mario Zechner)
- [badlogic/pi-mono](https://github.com/badlogic/pi-mono) — monorepo
- [pi-mono/packages/coding-agent/README.md](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/README.md)
- [pi-mono/packages/coding-agent/examples/sdk](https://github.com/badlogic/pi-mono/tree/main/packages/coding-agent/examples/sdk) — SDK examples 01-13
- [pi-mono/packages/coding-agent/examples/extensions](https://github.com/badlogic/pi-mono/tree/main/packages/coding-agent/examples/extensions) — 20+ extension examples
- [pi-mono/packages/tui](https://github.com/badlogic/pi-mono/tree/main/packages/tui) — terminal UI library with differential rendering
- [@mariozechner/pi-coding-agent on npm](https://www.npmjs.com/package/@mariozechner/pi-coding-agent)
- [shittycodingagent.ai](https://shittycodingagent.ai) — Pi's official website

### Related repos by IndyDevDan (disler)
- [disler/claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability) — Bun + SQLite + Vue observability dashboard for Claude Code
- [disler (IndyDevDan) on GitHub](https://github.com/disler) — full repo list
- [disler/bowser](https://github.com/disler/bowser) — browser automation with composable skills
- [disler/big-3-super-agent](https://github.com/disler/big-3-super-agent) — Gemini + OpenAI + Claude multi-provider
- [disler/infinite-agentic-loop](https://github.com/disler/infinite-agentic-loop) — parallel agent orchestration via slash command
- [disler/the-library](https://github.com/disler/the-library) — meta-skill for distributing agentics
- [disler/nano-agent](https://github.com/disler/nano-agent) — MCP server for small agents

### External commentary
- [Armin Ronacher — "Pi: The Minimal Agent Within OpenClaw"](https://lucumr.pocoo.org/2026/1/31/pi/) — Armin describes his own Pi usage and how OpenClaw is built on Pi components
- [Pi | Real Python AI Coding Tools reference](https://realpython.com/ref/ai-coding-tools/pi/) — third-party explainer
- [badlogic/pi-mono packages/coding-agent README](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/README.md) — full Pi docs
- [dabit3/gist How to Build a Custom Agent Framework with PI: The Agent Stack Powering OpenClaw](https://gist.github.com/dabit3/e97dbfe71298b1df4d36542aceb5f158)

### Alternative Pi implementations
- [badlogic/pi-mono](https://github.com/badlogic/pi-mono) — official TypeScript (canonical)
- [Dicklesworthstone/pi_agent_rust](https://github.com/Dicklesworthstone/pi_agent_rust) — Rust port, zero unsafe code
- [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) — fork with LSP, subagents, browser tools
