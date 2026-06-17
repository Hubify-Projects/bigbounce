# Vercel Open Agents — Research Notes

**Repo:** https://github.com/vercel-labs/open-agents
**Reviewed:** 2026-04-13
**Verdict:** SKIP fork, steal patterns. Deep Vercel lock-in, 5hr sandbox timeout, thin agent wrapper.

## What It Is

Vercel's open-source reference implementation for cloud-hosted coding agents. Full Next.js 16 app (not a library). "Claude Code but in the cloud with a web UI."

## Tech Stack

- Next.js 16.2.1, Vercel AI SDK ^6, Bun, Drizzle ORM + Neon Postgres, Upstash Redis
- `@vercel/sandbox` for cloud VMs (snapshot/hibernate/resume)
- `workflow` SDK for durable execution (survives deploys, cold starts)
- Default model: claude-opus-4.6, also supports GPT-5.4, o4-mini, Gemini

## Architecture

```
Web UI (Next.js) → Durable Workflow (Vercel SDK) → Cloud Sandbox (VM)
```

Key design: agent runs OUTSIDE the sandbox. Interacts via tools (readFile, writeFile, exec). Sandbox can hibernate/snapshot/resume independently.

## Agent System

- 11 tools (read, write, edit, grep, glob, bash, task, todo, ask_user, skill, web_fetch) — mirrors Claude Code exactly
- 3 subagents: Explorer (read-only, haiku), Executor (full tools, haiku), Design (UI-focused, opus)
- Subagents are fire-and-forget, cannot ask user questions
- Skills are markdown-based (SKILL.md + YAML frontmatter), no MCP

## Why We Skip

1. **Vercel lock-in**: Sandbox, workflows, auth, DB branching all Vercel-proprietary. No Docker/Fly/RunPod sandbox implementation exists.
2. **5-hour hard timeout** on sandbox VMs. Research workloads need days.
3. **Agent logic is thin**: Tools are `sandbox.readFile/writeFile/exec` wrappers. The "intelligence" is prompt engineering, not code.
4. **No MCP support**: Skills are markdown, not protocol-based.
5. **Our system is more sophisticated**: Orchestrator/lead/worker hierarchy, cross-model peer review, persistent Fly machines, Claude Code CLI integration.

## Patterns Worth Stealing

### 1. Sandbox Interface Abstraction
Clean contract for any execution environment:
```typescript
interface Sandbox {
  readFile(path): Promise<string>
  writeFile(path, content): Promise<void>
  stat(path): Promise<StatResult>
  exec(command, opts?): Promise<{stdout, stderr, exitCode}>
  execDetached?(command): Promise<void>  // for dev servers
  snapshot?(): Promise<void>
  getState?(): Promise<SandboxState>
  stop(): Promise<void>
}
```
We could implement this for Fly machines + RunPod pods. Uniform tool interface regardless of compute backend.

### 2. Durable Workflow Lifecycle
```
provisioning → active → hibernating → hibernated → restoring → active
```
- Lease-based coordination (`compareAndSetChatActiveStreamId`)
- Snapshot on hibernate, resume from snapshot
- 30min inactivity timeout → auto-hibernate (we'd want longer)
- Race condition handling for concurrent streams

### 3. Per-Model Behavioral Overlays
System prompt auto-tunes based on model family:
- Claude: emphasize todo/task tracking
- GPT: emphasize completion persistence (don't stop early)
- Gemini: emphasize conciseness
- GPT-5.4: anti-verbosity control

This is a good pattern for our multi-model peer review system.

### 4. Subagent Registry
Subagents defined with: model, system prompt, tool whitelist, step limit.
Fire-and-forget — parent gets summary. Clean separation of concerns.

## Comparison Table

| Dimension | Open Agents | Hubify Labs (planned) |
|-----------|-------------|----------------------|
| Execution | Vercel cloud VMs (5hr max) | Fly machines + RunPod (persistent) |
| Agent runtime | Vercel durable workflows | Claude Code CLI + custom orchestrator |
| Multi-agent | 3 subagents (explorer/executor/design) | Orchestrator/lead/worker + cross-model review |
| Sandbox | @vercel/sandbox (proprietary) | Docker on Fly / RunPod pods |
| Lock-in | High (Vercel-only) | Low (self-hostable) |
| MCP | No | Yes (planned) |
| Local-first | No | Yes (desktop + CLI) |
| Research workloads | No (5hr limit) | Yes (persistent compute) |
