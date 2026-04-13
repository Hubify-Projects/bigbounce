# Vibe Coding Patterns — Reference Library

**Date:** 2026-04-07
**Status:** Stub — background agent extending
**Purpose:** Catalog patterns from production vibe-coding implementations to mine for Hubify Labs' agent-driven code generation feature.

---

## Source Repos

### 1. OSS Vibe Coding Platform (Vercel official example)
- **Live demo:** https://oss-vibe-coding-platform.vercel.app
- **Source:** https://github.com/vercel/examples/tree/main/apps/vibe-coding-platform
- **Stack:** Next.js + Vercel AI SDK + Vercel Sandbox + AI Gateway + Fluid Compute
- **Why:** This is the canonical reference for the exact pattern Hubify Labs wants — user types prompt, agent builds full-stack app, output streams back live, sandbox executes code securely.

### 2. Coding Agent Template (Vercel Labs)
- **Source:** https://github.com/vercel-labs/coding-agent-template
- **Notable:** Supports Claude Code as a coding agent
- **Why:** Lower-level template showing the agent-runner harness pattern and tool-use protocols.

---

## Architectural summary

The two repos take very different approaches to "vibe coding" and each is worth mining separately:

| Dimension | vibe-coding-platform | coding-agent-template |
|---|---|---|
| **Agent loop** | AI SDK `streamText` with tools, runs in Next.js API route | Next.js `after()` block runs a CLI (`claude`, `codex`, `cursor`…) inside sandbox via `sandbox.runCommand` |
| **Who writes files** | The LLM calls a `generateFiles` tool; host streams files into sandbox via `sandbox.writeFiles` | The CLI (e.g. Claude Code) writes files directly inside the sandbox |
| **Sandbox lifetime** | Per-session, ~10 min default, max 45 min, single sandbox reused per chat | Per-task, 5 min to 5 hours, optional keep-alive for follow-ups |
| **State** | Client-side Zustand store + AI SDK `useChat` | Postgres (Neon) — tasks, messages, logs, sandboxes all persisted |
| **Auth** | None for demo (botid only) | Full OAuth (GitHub/Vercel) + per-user API keys, encrypted at rest |
| **Preview** | Live iframe of `sandbox.domain(port)` | Sandbox URL surfaced in UI when keep-alive is on |

vibe-coding-platform is the better reference for **"chat → generated app → live preview"**. coding-agent-template is the better reference for **"task → clone real repo → agent edits files → commit PR"**.

---

## Sandbox lifecycle

### 1. Creation

**vibe-coding-platform** creates sandboxes from the agent's own tool call — the LLM decides when to spin one up. Source: `apps/vibe-coding-platform/ai/tools/create-sandbox.ts` (lines 28-56):

```ts
execute: async ({ timeout, ports }, { toolCallId }) => {
  writer.write({ id: toolCallId, type: 'data-create-sandbox', data: { status: 'loading' } })
  try {
    const sandbox = await Sandbox.create({ timeout: timeout ?? 600000, ports })
    writer.write({
      id: toolCallId,
      type: 'data-create-sandbox',
      data: { sandboxId: sandbox.sandboxId, status: 'done' },
    })
    return `Sandbox created with ID: ${sandbox.sandboxId}.\nYou can now upload files, run commands, and access services on the exposed ports.`
  } catch (error) { /* ... */ }
}
```

Key choices:
- **Timeout clamped** to `min(600000).max(2700000)` ms — i.e. 10 min to 45 min. Defaults to 10 min.
- **Ports declared up-front** at `create` time — you can't add ports later. Max 2 ports.
- **No pre-loaded template** — sandbox is bare Amazon Linux 2023 (see system prompt below).
- **No teamId/projectId/token in code** — vibe-coding-platform relies on default env-based auth. The SDK picks up `VERCEL_*` envs implicitly.

**coding-agent-template** creates sandboxes from a host function (not an LLM tool). Source: `lib/sandbox/creation.ts` (lines 75-99):

```ts
const timeoutMs = config.timeout
  ? parseInt(config.timeout.replace(/\D/g, '')) * 60 * 1000
  : 60 * 60 * 1000 // Default 1 hour
const defaultPorts = config.ports || [3000, 5173]

const sandboxConfig = {
  teamId: process.env.SANDBOX_VERCEL_TEAM_ID!,
  projectId: process.env.SANDBOX_VERCEL_PROJECT_ID!,
  token: process.env.SANDBOX_VERCEL_TOKEN!,
  timeout: timeoutMs,
  ports: defaultPorts,
  runtime: config.runtime || 'node22',
  resources: { vcpus: config.resources?.vcpus || 4 },
}
let sandbox: Sandbox
sandbox = await Sandbox.create(sandboxConfig)
```

Key choices:
- **Explicit team/project/token** passed per call (supports multi-tenant Vercel deployments).
- **Default 1 hour** timeout (vs 10 min in vibe-coding-platform).
- **Both Next.js and Vite ports** exposed by default (`[3000, 5173]`).
- **4 vCPU** resource grant, `node22` runtime.

### 2. Reuse & single-sandbox discipline

vibe-coding-platform enforces **one sandbox per chat session**. From the system prompt in `app/api/chat/prompt.md`:

> 🟠 **Single Sandbox Reuse:** Use only one sandbox per session unless explicitly reset by the user.
> - Only one sandbox can be created per session—reuse this sandbox throughout unless the user specifically requests a reset.

The LLM tracks sandbox state in its own context — there's no server-side registry. Subsequent tool calls (`runCommand`, `generateFiles`, `getSandboxURL`) take a `sandboxId` parameter and re-hydrate the sandbox via `Sandbox.get({ sandboxId })`.

Example reuse pattern from `apps/vibe-coding-platform/ai/tools/run-command.ts`:

```ts
let sandbox: Sandbox | null = null
try {
  sandbox = await Sandbox.get({ sandboxId })
} catch (error) {
  const richError = getRichError({ action: 'get sandbox by id', args: { sandboxId }, error })
  return richError.message
}
```

coding-agent-template has a small in-memory registry in `lib/sandbox/sandbox-registry.ts`:

```ts
const activeSandboxes = new Map<string, Sandbox>()

export function registerSandbox(taskId: string, sandbox: Sandbox): void {
  activeSandboxes.set(taskId, sandbox)
}

export async function killSandbox(taskId: string) {
  const sandbox = activeSandboxes.get(taskId)
  activeSandboxes.delete(taskId)
  try { await sandbox.stop() } catch { /* may already be stopped */ }
  return { success: true }
}
```

Important note from the same file: "Real persistence happens via sandboxId in database" — the registry is only for the current serverless execution. Across requests they rely on `Sandbox.get({ sandboxId })` plus a `sandboxId` column on the `tasks` table.

### 3. Cleanup and keep-alive

vibe-coding-platform has **no explicit shutdown** — sandboxes auto-expire after their timeout. The README even says: "Note: Vercel Sandbox automatically shuts down after timeout. No explicit shutdown method available in current SDK" (from `lib/sandbox/git.ts`).

coding-agent-template has two modes documented in `README.md`:

- **Keep Alive OFF**: sandbox shuts down immediately after task completes (`shutdownSandbox()` kills node/python/npm/yarn/pnpm processes and lets Vercel collect it).
- **Keep Alive ON**: sandbox stays alive for the remainder of the timeout so the user can send follow-up messages; the dev server auto-starts.

```ts
// lib/sandbox/git.ts — shutdownSandbox
export async function shutdownSandbox(sandbox?: Sandbox) {
  if (sandbox) {
    try {
      for (const proc of ['node', 'python', 'npm', 'yarn', 'pnpm']) {
        await runCommandInSandbox(sandbox, 'pkill', ['-f', proc])
      }
    } catch { /* best effort */ }
  }
  return { success: true }
}
```

**Takeaway:** neither repo does explicit reuse across users or sessions. Cost optimization is entirely via timeout clamping. For Hubify Labs, the right default is probably vibe-coding-platform's 10-minute single-sandbox-per-session, with coding-agent-template's keep-alive pattern as an optional "iterate mode".

---

## Streaming UI

### 1. Server-side stream writer

vibe-coding-platform uses the AI SDK's `createUIMessageStream` + `streamText` combo. Source: `apps/vibe-coding-platform/app/api/chat/route.ts`:

```ts
return createUIMessageStreamResponse({
  stream: createUIMessageStream({
    originalMessages: messages,
    execute: async ({ writer }) => {
      const result = streamText({
        ...getModelOptions(modelId, { reasoningEffort }),
        system: prompt,
        messages: await convertToModelMessages(/* ... */),
        stopWhen: stepCountIs(20),
        tools: tools({ modelId, writer }),
        onError: (error) => console.error('AI error', error),
      })
      result.consumeStream()
      writer.merge(result.toUIMessageStream({
        sendReasoning: true,
        sendStart: false,
        messageMetadata: () => ({ model: MODEL_NAMES[modelId] ?? modelId }),
      }))
    },
  }),
})
```

The `writer` is passed into every tool. Tools emit typed `data-*` parts in addition to their return values — that's how the UI gets progress updates without polluting the LLM's context.

### 2. Typed data parts for each tool

Every tool has a Zod schema in `ai/messages/data-parts.ts`:

```ts
export const dataPartSchema = z.object({
  'create-sandbox': z.object({
    sandboxId: z.string().optional(),
    status: z.enum(['loading', 'done', 'error']),
    error: errorSchema.optional(),
  }),
  'generating-files': z.object({
    paths: z.array(z.string()),
    status: z.enum(['generating', 'uploading', 'uploaded', 'done', 'error']),
    error: errorSchema.optional(),
  }),
  'run-command': z.object({
    sandboxId: z.string(),
    commandId: z.string().optional(),
    command: z.string(),
    args: z.array(z.string()),
    status: z.enum(['executing', 'running', 'waiting', 'done', 'error']),
    exitCode: z.number().optional(),
    error: errorSchema.optional(),
  }),
  'get-sandbox-url': z.object({
    url: z.string().optional(),
    status: z.enum(['loading', 'done']),
  }),
  'report-errors': z.object({
    summary: z.string(),
    paths: z.array(z.string()).optional(),
  }),
})
```

### 3. File-diff / file-generation streaming

The `generateFiles` tool is actually **a nested streamText call** — it uses structured output (`Output.object`) to stream a `files[]` array, and yields chunks as files complete. Source: `ai/tools/generate-files/get-contents.ts`:

```ts
const result = streamText({
  ...getModelOptions(params.modelId, { reasoningEffort: 'low' }),
  maxOutputTokens: 64000,
  system: 'You are a file content generator. You must generate files based on the conversation history and the provided paths. NEVER generate lock files...',
  messages: [ /* convo */, { role: 'user', content: `Generate the content of the following files...` }],
  output: Output.object({ schema: z.object({ files: z.array(fileSchema) }) }),
})

for await (const items of result.partialOutputStream) {
  if (!Array.isArray(items?.files)) continue
  // slice-by-2 trick: only emit files once the next one has started, guaranteeing tail is complete
  const files = items.files
    .slice(generated.length, items.files.length - 2)
    .map((file) => fileSchema.parse(file))
  if (files.length > 0) {
    yield { files, paths, written }
    generated.push(...files)
  }
}
```

The slice-by-2 trick guarantees the tail file is complete before emitting it. The UI gets two kinds of updates: "paths in flight" (`status: 'generating'`) shows filenames appearing in the file explorer, and "uploaded" (`status: 'uploaded'`) shows content available in the editor.

### 4. Preview iframe

Source: `components/preview/preview.tsx`:

```tsx
<Panel className={className}>
  <PanelHeader>
    {/* nav buttons + editable URL bar */}
  </PanelHeader>
  <div className="flex h-[calc(100%-2rem-1px)] relative">
    {currentUrl && !disabled && (
      <>
        <ScrollArea className="w-full">
          <iframe
            ref={iframeRef}
            src={currentUrl}
            className="w-full h-full"
            onLoad={handleIframeLoad}
            onError={handleIframeError}
            title="Browser content"
          />
        </ScrollArea>
        {isLoading && !error && (/* BarLoader overlay */)}
        {error && (/* "Try again" with ?t= cache-bust */)}
      </>
    )}
  </div>
</Panel>
```

The iframe `src` is just `sandbox.domain(port)` — Vercel Sandbox exposes publicly-reachable HTTPS URLs for each declared port. See next section.

### 5. Client-side state-sync

The Zustand store in `apps/vibe-coding-platform/app/state.ts` has a `useDataStateMapper()` hook that reads incoming stream parts and updates the store:

```ts
return (data: DataUIPart<DataPart>) => {
  switch (data.type) {
    case 'data-create-sandbox':
      if (data.data.sandboxId) setSandboxId(data.data.sandboxId)
      break
    case 'data-generating-files':
      if (data.data.status === 'uploaded') {
        addPaths(data.data.paths)
        addGeneratedFiles(data.data.paths)
      }
      break
    case 'data-run-command':
      if (data.data.commandId && (data.data.status === 'executing' || data.data.status === 'running')) {
        upsertCommand({ /* sandboxId, cmdId, command, args, background */ })
      }
      break
    case 'data-get-sandbox-url':
      if (data.data.url) setUrl(data.data.url, crypto.randomUUID())
      break
  }
}
```

This is the clean pattern: **one typed data-part per tool lifecycle stage**, client has a single switch that drives the store.

### 6. Streaming Claude Code CLI (coding-agent-template)

Because coding-agent-template doesn't use the AI SDK for the agent loop — it runs a CLI inside the sandbox — it parses `stream-json` output from Claude Code directly. Source: `lib/sandbox/agents/claude.ts`:

```ts
let fullCommand = `${envPrefix} claude --model "${modelToUse}" --dangerously-skip-permissions --output-format stream-json --verbose`
if (isResumed) fullCommand += sessionId ? ` --resume "${sessionId}"` : ` --resume`
fullCommand += ` "${instruction}"`

const captureStdout = new Writable({
  write(chunk, _encoding, callback) {
    for (const line of chunk.toString().split('\n')) {
      try {
        const parsed = JSON.parse(line.trim())
        if (parsed.type === 'assistant' && parsed.message?.content) {
          for (const block of parsed.message.content) {
            if (block.type === 'text') {
              accumulatedContent += block.text
              db.update(taskMessages).set({ content: accumulatedContent }).where(eq(taskMessages.id, agentMessageId))
            } else if (block.type === 'tool_use') {
              const { name, input = {} } = block
              let msg = ''
              if (name === 'Write' || name === 'Edit') msg = `Editing ${input.file_path || 'file'}`
              else if (name === 'Read') msg = `Reading ${input.file_path || 'file'}`
              else if (name === 'Bash') msg = `Running: ${(input.command || '').slice(0, 50)}`
              if (msg) accumulatedContent += `\n\n${msg}\n\n`
            }
          }
        } else if (parsed.type === 'result') {
          if (parsed.session_id) extractedSessionId = parsed.session_id
          isCompleted = true
        }
      } catch { /* not JSON */ }
    }
    callback()
  },
})
```

This is the pattern if you want to host **Claude Code itself** inside the sandbox: pipe its stdout into a Writable, parse each JSON line, and translate tool-use events into human-readable status messages that stream to the DB and down to the browser.

---

## Tool-use protocol

### vibe-coding-platform has exactly 4 tools

Source: `apps/vibe-coding-platform/ai/tools/index.ts`:

```ts
export function tools({ modelId, writer }: Params) {
  return {
    createSandbox: createSandbox({ writer }),
    generateFiles: generateFiles({ writer, modelId }),
    getSandboxURL: getSandboxURL({ writer }),
    runCommand: runCommand({ writer }),
  }
}
```

That's it. Four tools spin up the entire platform. Tool descriptions are stored as **separate markdown files** imported via raw-loader (`import description from './create-sandbox.md'`), which lets the prompts be large, versioned, and human-editable without polluting TS.

### Tool schemas (inputSchema in Zod)

- `createSandbox`: `{ timeout?: number (600k–2.7M ms), ports?: number[] (max 2) }`
- `runCommand`: `{ sandboxId, command (base cmd only), args?: string[], sudo?: boolean, wait: boolean }`
- `generateFiles`: `{ sandboxId: string, paths: string[] }` — LLM only sends file paths; contents are generated by a second LLM call inside the tool
- `getSandboxURL`: `{ sandboxId: string, port: number }`

### Stop condition

The agent loop stops after 20 steps, hard limit. Source: `app/api/chat/route.ts`:

```ts
const result = streamText({
  ...getModelOptions(modelId, { reasoningEffort }),
  system: prompt,
  messages: /* ... */,
  stopWhen: stepCountIs(20),
  tools: tools({ modelId, writer }),
  /* ... */
})
```

Plus, the system prompt hammers on **loop prevention** hard:

> CRITICAL RULES TO PREVENT LOOPS:
> 1. NEVER regenerate files that already exist unless the user explicitly asks you to update them
> 2. If an error occurs after file generation, DO NOT automatically regenerate all files
> 3. Track what operations you've already performed in the conversation and don't repeat them
> 4. If a command fails, analyze the error before taking action - don't just retry the same thing
> 5. When fixing errors, make targeted fixes rather than regenerating entire projects

And a persistence rule to force the model to keep going until the dev server actually runs:

> IMPORTANT - PERSISTENCE RULE:
> - When you fix one error and another error appears, CONTINUE FIXING until the application works
> - DO NOT stop after fixing just one error - keep going until the dev server runs successfully
> - Each error is a step closer to success - treat them as progress, not failures

### Feedback loop: how errors come back into the agent

Error reports from the client (e.g. lint/build errors surfaced by the error monitor) are mapped into user messages in `app/api/chat/route.ts`:

```ts
messages: await convertToModelMessages(
  messages.map((message) => {
    message.parts = message.parts.map((part) => {
      if (part.type === 'data-report-errors') {
        return {
          type: 'text',
          text:
            `There are errors in the generated code. This is the summary of the errors we have:\n` +
            `\`\`\`${part.data.summary}\`\`\`\n` +
            (part.data.paths?.length
              ? `The following files may contain errors:\n\`\`\`${part.data.paths?.join('\n')}\`\`\`\n`
              : '') +
            `Fix the errors reported.`,
        }
      }
      return part
    })
    return message
  })
),
```

This is the pattern: **client-side monitoring produces `data-report-errors` parts**, the server **reinjects them as text** on the next turn so the LLM sees them as user messages.

### Typical workflow as prescribed by the system prompt

From `app/api/chat/prompt.md`:

> 1. Create the sandbox, ensuring exposed ports are specified as needed.
> 2. Generate the initial set of application files according to the user's requirements.
> 3. Install dependencies with `pnpm install`
> 4. Start the dev server with `pnpm run dev`
> 5. IF ERRORS OCCUR: Fix them one by one until the server runs successfully
> 6. Retrieve a preview URL once the application is running successfully
> 7. Only then declare success to the user

### coding-agent-template: Claude Code's own tools, delegated

coding-agent-template hands off the whole tool-use protocol to whichever CLI it's running. For Claude specifically it uses `--dangerously-skip-permissions` and lets Claude Code use its native Write/Edit/Read/Glob/Bash/Grep toolset. The host only observes via `stream-json`.

This is a **strictly more powerful** pattern at the cost of running a full CLI inside every sandbox. For Hubify Labs the right choice depends on whether we want host-side control (vibe-coding-platform) or to delegate to Claude Code itself (coding-agent-template).

---

## Model gateway

### Gateway configuration

vibe-coding-platform wraps `@ai-sdk/gateway` with per-model options. Source: `ai/gateway.ts`:

```ts
const gateway = createGatewayProvider({ baseURL: process.env.AI_GATEWAY_BASE_URL })

export function getModelOptions(modelId: string, options?: { reasoningEffort?: 'low'|'medium'|'high' }): ModelOptions {
  if (modelId === Models.OpenAIGPT53Codex) {
    return {
      model: gateway(modelId),
      providerOptions: {
        openai: {
          include: ['reasoning.encrypted_content'],
          reasoningEffort: options?.reasoningEffort ?? 'low',
          reasoningSummary: 'auto',
          serviceTier: 'priority',
        } satisfies OpenAIResponsesProviderOptions,
      },
    }
  }
  if (modelId === Models.AnthropicClaudeSonnet46 || modelId === Models.AnthropicClaudeOpus46) {
    return {
      model: gateway(modelId),
      headers: { 'anthropic-beta': 'fine-grained-tool-streaming-2025-05-14' },
      providerOptions: { anthropic: { cacheControl: { type: 'ephemeral' } } },
    }
  }
  return { model: gateway(modelId) }
}
```

This is the clean spot to notice:
- **Anthropic fine-grained tool streaming** header is wired in centrally — every Claude call gets it.
- **OpenAI reasoning encryption + priority tier** is bundled for GPT-5.3 Codex.
- **Ephemeral prompt caching** for Claude is toggled via provider options here.

The `baseURL` env var lets the whole thing point at either Vercel AI Gateway or a custom gateway without code changes.

### Supported models enum

```ts
// ai/constants.ts
export enum Models {
  AnthropicClaudeOpus46 = 'anthropic/claude-opus-4.6',
  AnthropicClaudeSonnet46 = 'anthropic/claude-sonnet-4.6',
  OpenAIGPT53Codex = 'openai/gpt-5.3-codex',
  XaiGrok41Reasoning = 'xai/grok-4.1-fast-reasoning',
}
export const DEFAULT_MODEL = Models.AnthropicClaudeOpus46
```

Default is Claude Opus 4.6 — interesting signal, Vercel's own demo defaults to Claude for vibe coding.

### Per-task model selection

**Inside** the file-generation tool, they use a second model call with `reasoningEffort: 'low'` to keep cost down on the bulk code generation. Source: `ai/tools/generate-files/get-contents.ts`:

```ts
const result = streamText({
  ...getModelOptions(params.modelId, { reasoningEffort: 'low' }),
  maxOutputTokens: 64000,
  /* ... */
})
```

So the orchestrator uses the user-selected model at default effort, and the inner file-writer uses the same model family but at low reasoning effort. This is a cost-optimization pattern worth copying.

coding-agent-template uses a **totally different model for branch-name generation** — `openai/gpt-5-nano` via `generateText` in `lib/utils/branch-name-generator.ts`:

```ts
const result = await generateText({
  model: 'openai/gpt-5-nano',
  prompt,
  temperature: 0.3,
})
```

This is the "use a cheap model for dumb subtasks" pattern: title generation, branch names, commit messages all use `gpt-5-nano` while the main agent is Claude Code or whatever the user picked.

### Token/cost tracking

**Neither repo explicitly tracks tokens or cost.** vibe-coding-platform depends on AI Gateway's observability. coding-agent-template has a `MAX_MESSAGES_PER_DAY` rate limit (default 5) — that's the closest thing to cost control.

For Hubify Labs we'll need our own counter. The AI SDK's `result.usage` returns `{ promptTokens, completionTokens, totalTokens }` after a `streamText` resolves — that's the hook point.

---

## Authentication and credential brokering

### vibe-coding-platform: botid-only, no user auth

The demo has **no user accounts**. Only protection is bot detection at `app/api/chat/route.ts`:

```ts
export async function POST(req: Request) {
  const [checkResult, { messages, modelId = DEFAULT_MODEL, reasoningEffort }] =
    await Promise.all([checkBotId(), req.json() as Promise<BodyData>])
  if (checkResult.isBot) {
    return NextResponse.json({ error: `Bot detected` }, { status: 403 })
  }
  /* ... */
}
```

Secrets all live in env vars on the Vercel deployment. The Vercel Sandbox SDK picks up `VERCEL_*` creds implicitly.

### coding-agent-template: full auth, encrypted per-user API keys

Much richer model. Key details from README:

- **OAuth**: Sign in with GitHub or Vercel. `NEXT_PUBLIC_AUTH_PROVIDERS` env var chooses which are enabled.
- **JWE session tokens**: `JWE_SECRET` for encrypting session JWTs.
- **Per-user encrypted keys table**: `keys` table in Postgres, encrypted with a server-side `ENCRYPTION_KEY` (32-byte hex).
- **User-provided API keys take precedence over global env**: If a user adds their own Anthropic key, it's used instead of `process.env.ANTHROPIC_API_KEY`.

The credential-injection pattern into the sandbox is in `lib/sandbox/agents/index.ts`:

```ts
const originalEnv = {
  ANTHROPIC_API_KEY: process.env.ANTHROPIC_API_KEY,
  AI_GATEWAY_API_KEY: process.env.AI_GATEWAY_API_KEY,
  GH_TOKEN: process.env.GH_TOKEN,
  /* ... and others */
}
if (apiKeys?.ANTHROPIC_API_KEY) process.env.ANTHROPIC_API_KEY = apiKeys.ANTHROPIC_API_KEY
if (apiKeys?.AI_GATEWAY_API_KEY) process.env.AI_GATEWAY_API_KEY = apiKeys.AI_GATEWAY_API_KEY
if (githubToken) { process.env.GH_TOKEN = githubToken; process.env.GITHUB_TOKEN = githubToken }
try {
  /* ... run agent ... */
} finally {
  // Restore original environment variables
  process.env.ANTHROPIC_API_KEY = originalEnv.ANTHROPIC_API_KEY
  /* ... restore all ... */
}
```

This is a **process-level env mutation with restore-in-finally** pattern. It's ugly but it's compatible with CLIs that read from `process.env` on startup. NOT safe under concurrent requests — each serverless invocation gets its own process so it's fine at Vercel, would NOT be fine on a persistent server.

### GitHub auth into the sandbox

The repo URL itself is mutated to include the user's GitHub token. Source: `lib/sandbox/config.ts`:

```ts
export function createAuthenticatedRepoUrl(repoUrl: string, githubToken?: string | null): string {
  if (!githubToken) return repoUrl
  try {
    const url = new URL(repoUrl)
    if (url.hostname === 'github.com') {
      url.username = githubToken
      url.password = 'x-oauth-basic'
    }
    return url.toString()
  } catch {
    return repoUrl
  }
}
```

The URL becomes `https://<token>:x-oauth-basic@github.com/owner/repo.git` and is passed to `git clone` inside the sandbox. This is clean and standard — no need to SSH-key the sandbox.

### Claude CLI → AI Gateway config

The coolest credential pattern here is **Claude Code is authenticated against Vercel AI Gateway, not Anthropic direct**. Source: `lib/sandbox/agents/claude.ts`:

```ts
const apiKey = process.env.AI_GATEWAY_API_KEY
const baseUrl = 'https://ai-gateway.vercel.sh'
/* ... */
const configFileCmd = `mkdir -p $HOME/.config/claude && cat > $HOME/.config/claude/config.json << 'EOF'
{
  "api_key": "${apiKey}",
  "api_base_url": "${baseUrl}",
  "default_model": "${modelToUse}"
}
EOF`
const configFileResult = await runCommandInSandbox(sandbox, 'sh', ['-c', configFileCmd])
```

And at execution time:

```ts
const envPrefix = `ANTHROPIC_API_KEY="${aiGatewayKey}" ANTHROPIC_BASE_URL="${aiGatewayBaseUrl}"`
let fullCommand = `${envPrefix} claude --model "${modelToUse}" --dangerously-skip-permissions --output-format stream-json --verbose`
```

So Claude Code thinks it's hitting `api.anthropic.com` but the env vars route it through `ai-gateway.vercel.sh`. This gives Vercel centralized observability, rate-limiting, and the ability to swap model providers without touching the agent code. **For Hubify Labs this is probably the pattern we want.**

### Security rules (from AGENTS.md)

coding-agent-template has strict rules in `AGENTS.md`:

- **No dynamic values in any log statements** — logs are shown in the UI, so any `${variable}` could leak credentials, file paths, branch names. Static strings only.
- A `redactSensitiveInfo()` function as backup, patterns: `ANTHROPIC_API_KEY`, GitHub tokens (`ghp_`, `gho_`, `ghu_`, `ghs_`, `ghr_`), Bearer tokens, `SANDBOX_VERCEL_TOKEN`.
- Client-exposed env vars whitelist: only `NEXT_PUBLIC_AUTH_PROVIDERS` and `NEXT_PUBLIC_GITHUB_CLIENT_ID`.

Worth copying the **"static log strings only"** rule for Hubify Labs — once a log is shown to a user in a live UI, every log line is a potential leak.

---

## File system bridge

### vibe-coding-platform: LLM-generated, host-uploaded

Files never flow from a user's machine into the sandbox. The LLM decides what files to create, a nested `streamText` generates their contents, and the host uploads them via `sandbox.writeFiles`. Source: `ai/tools/generate-files/get-write-files.ts`:

```ts
return async function writeFiles(params: {
  written: string[]
  files: File[]
  paths: string[]
}) {
  const paths = params.written.concat(params.files.map((file) => file.path))
  writer.write({
    id: toolCallId,
    type: 'data-generating-files',
    data: { paths, status: 'uploading' },
  })
  try {
    await sandbox.writeFiles(
      params.files.map((file) => ({
        content: Buffer.from(file.content, 'utf8'),
        path: file.path,
      }))
    )
  } catch (error) { /* ... */ }
  writer.write({
    id: toolCallId,
    type: 'data-generating-files',
    data: { paths, status: 'uploaded' },
  })
}
```

Note: `sandbox.writeFiles` takes an array of `{ content: Buffer, path: string }`. No directories — Vercel Sandbox writes paths and creates parents automatically. All paths are **relative to the sandbox root**; the system prompt enforces "use only relative paths" because commands are stateless (no persistent `cd`).

### Persistence

**vibe-coding-platform has no persistence.** The file list is stored in a Zustand client store (`addGeneratedFiles`, `addPaths`). When the sandbox expires, everything is gone. There's no "save this app to my account" flow.

**coding-agent-template** clones a real GitHub repo into `/vercel/sandbox/project` at sandbox creation:

```ts
export const PROJECT_DIR = '/vercel/sandbox/project'

await runCommandInSandbox(sandbox, 'mkdir', ['-p', PROJECT_DIR])
await runCommandInSandbox(sandbox, 'git', ['clone', '--depth', '1', authenticatedRepoUrl, PROJECT_DIR])
```

And **persists by pushing to a Git branch** after the agent finishes. Source: `lib/sandbox/git.ts`:

```ts
export async function pushChangesToBranch(sandbox, branchName, commitMessage, logger) {
  const statusResult = await runInProject(sandbox, 'git', ['status', '--porcelain'])
  if (!statusResult.output?.trim()) return { success: true } // nothing to commit
  await runInProject(sandbox, 'git', ['add', '.'])
  await runInProject(sandbox, 'git', ['commit', '-m', commitMessage])
  const pushResult = await runInProject(sandbox, 'git', ['push', 'origin', branchName])
  return { success: true, pushFailed: !pushResult.success }
}
```

The branch name is **AI-generated** (via `openai/gpt-5-nano`) in a Next.js `after()` block so it doesn't block response. See the branch-name-generator quote earlier.

### Sync-back

- **vibe-coding-platform**: nothing. App lives only in sandbox.
- **coding-agent-template**: committed to a Git branch and a PR can be opened from the UI via `components/create-pr-dialog.tsx`.

For Hubify Labs' "build me a lab dashboard → commit to the lab repo" use case, coding-agent-template's pattern maps directly: clone the repo at sandbox creation, let the agent edit in-place, push to a feature branch, open a PR.

### Stateless shell caveat

Both repos warn heavily that **every `runCommand` is a fresh shell**. From the `run-command.md` system doc:

> Commands are stateless — each one runs in a fresh shell session with no memory of previous commands. You CANNOT rely on `cd`, but other state like shell exports or background processes from prior commands should be available.

`runInProject` in coding-agent-template works around this with an `sh -c 'cd /vercel/sandbox/project && …'` prefix on every command:

```ts
export async function runInProject(sandbox: Sandbox, command: string, args: string[] = []): Promise<CommandResult> {
  const escapeArg = (arg: string) => `'${arg.replace(/'/g, "'\\''")}'`
  const fullCommand = args.length > 0 ? `${command} ${args.map(escapeArg).join(' ')}` : command
  const cdCommand = `cd ${PROJECT_DIR} && ${fullCommand}`
  return await runCommandInSandbox(sandbox, 'sh', ['-c', cdCommand])
}
```

---

## Preview / output rendering

### URL construction

Source: `apps/vibe-coding-platform/ai/tools/get-sandbox-url.ts`:

```ts
execute: async ({ sandboxId, port }, { toolCallId }) => {
  writer.write({
    id: toolCallId,
    type: 'data-get-sandbox-url',
    data: { status: 'loading' },
  })
  const sandbox = await Sandbox.get({ sandboxId })
  const url = sandbox.domain(port)
  writer.write({
    id: toolCallId,
    type: 'data-get-sandbox-url',
    data: { url, status: 'done' },
  })
  return { url }
}
```

**`sandbox.domain(port)` is the one-line preview pattern.** Vercel Sandbox assigns a public HTTPS URL to every declared port. No reverse proxy, no tunneling, no iframe sandboxing wrappers. The iframe just points at this URL directly.

Constraints (from the system prompts):
- Ports **must** be declared at `Sandbox.create` time — you can't add ports later.
- Max 2 ports per sandbox.
- Port 8080 is reserved — "You can NEVER use port 8080 as it is reserved for internal applications."

### Dev server lifecycle inside sandbox

The system prompt prescribes:

> 1. Create the sandbox, ensuring exposed ports are specified as needed.
> 2. Generate the initial set of application files according to the user's requirements.
> 3. Install dependencies with `pnpm install`
> 4. Start the dev server with `pnpm run dev`
> 5. IF ERRORS OCCUR: Fix them one by one
> 6. Retrieve a preview URL once the application is running successfully

Dev server is started with `wait: false` so the `runCommand` returns immediately while the server runs in the background. HMR handles file changes:

> When running `pnpm dev` in a Next.js or Vite project, HMR can handle updates so generally you don't need to kill the server process and start it again after changing files.

This is the hot-reload pattern — just let the dev server keep running, let it see file changes from `sandbox.writeFiles` in later turns.

### Port auto-detection

coding-agent-template ships a neat helper in `lib/sandbox/port-detection.ts` that peeks at `package.json` via the GitHub API **before** creating the sandbox:

```ts
export async function detectPortFromRepo(repoUrl: string, githubToken?: string | null): Promise<number> {
  try {
    const [, owner, repo] = repoUrl.match(/github\.com[/:]([\w-]+)\/([\w-]+?)(\.git)?$/) || []
    if (!owner) return 3000
    const octokit = new Octokit({ auth: githubToken || undefined })
    const { data } = await octokit.repos.getContent({ owner, repo, path: 'package.json' })
    if ('content' in data && data.type === 'file') {
      const pkg = JSON.parse(Buffer.from(data.content, 'base64').toString('utf-8'))
      const hasVite = pkg.dependencies?.vite || pkg.devDependencies?.vite
      if (hasVite) return 5173
    }
    return 3000
  } catch { return 3000 }
}
```

Simple heuristic — is Vite in deps → expose 5173, otherwise expose 3000. Good pattern for "start sandbox with the right port without guessing".

### Iframe refresh strategy

When a new URL comes in, the store key is changed to force React to remount the iframe:

```tsx
// apps/vibe-coding-platform/app/preview.tsx
export function Preview({ className }: Props) {
  const { status, url, urlUUID } = useSandboxStore()
  return (
    <PreviewComponent
      key={urlUUID}
      className={className}
      disabled={status === 'stopped'}
      url={url}
    />
  )
}
```

And `setUrl(url, crypto.randomUUID())` in the store (from `state.ts`) — every URL update gets a fresh UUID, which becomes the iframe `key`, forcing remount.

---

## Concrete patterns to copy for Hubify Labs

These are the patterns we should literally copy-paste (with attribution) into the Hubify Labs orchestrator.

### 1. Four-tool agent: createSandbox / generateFiles / runCommand / getSandboxURL

**What:** The entire vibe-coding-platform agent has only four tools. Simple, powerful, complete.
**Where:** `apps/vibe-coding-platform/ai/tools/index.ts` (all 20 lines), plus the four files in `apps/vibe-coding-platform/ai/tools/{create-sandbox,generate-files,run-command,get-sandbox-url}.ts` (each ~50–250 lines).
**Why it matters for Hubify Labs:** This is the minimal viable tool surface area. We should start here and only add tools when the four-tool version proves insufficient. Resist the temptation to add `read_file` — the LLM should track its own file state from tool return values.

### 2. Typed data-parts per tool with Zod schemas

**What:** One Zod schema per tool lifecycle, streamed as `data-*` parts alongside the text stream. Client has a single `useDataStateMapper` switch that drives the Zustand store.
**Where:**
- Schema: `apps/vibe-coding-platform/ai/messages/data-parts.ts` (lines 1–34)
- Client mapper: `apps/vibe-coding-platform/app/state.ts` (lines 93–135, `useDataStateMapper`)
**Why it matters for Hubify Labs:** Gives us typed progress updates without polluting the LLM's context window with status text. The left-panel chat can show "uploading 3 files…" while the LLM is still streaming a separate text message. Our orchestrator chat needs this split.

### 3. Tool descriptions as separate `.md` files loaded via raw-loader

**What:** Each tool's description is in its own markdown file (e.g. `create-sandbox.md`) imported with `import description from './create-sandbox.md'`. `raw-loader` is in devDependencies; `markdown.d.ts` declares the `.md` module type.
**Where:**
- `apps/vibe-coding-platform/ai/tools/create-sandbox.md` (~45 lines)
- `apps/vibe-coding-platform/ai/tools/create-sandbox.ts` (line 7: `import description from './create-sandbox.md'`)
- `apps/vibe-coding-platform/markdown.d.ts`
**Why it matters for Hubify Labs:** Houston will iterate on tool prompts constantly. Having them as editable markdown files (instead of giant TS string literals) means non-engineers can edit prompts, diffs are readable in code review, and the prompts can be longer without cluttering the tool logic.

### 4. Anti-loop system prompt with explicit "PERSISTENCE RULE"

**What:** The main system prompt at `app/api/chat/prompt.md` has ~20 lines of explicit anti-loop rules ("NEVER regenerate files", "make targeted fixes", "keep track of what you've tried"), balanced against a PERSISTENCE RULE that forces the model to keep going until the dev server runs successfully.
**Where:** `apps/vibe-coding-platform/app/api/chat/prompt.md` (entire file, ~170 lines).
**Why it matters for Hubify Labs:** Vibe coding agents are prone to two failure modes: (a) regenerating the entire project on every error, and (b) giving up after the first error. The Vercel prompt solves both with explicit rules. We should copy the CRITICAL RULES and PERSISTENCE RULE sections nearly verbatim.

### 5. Dual-model gateway config: main model + low-effort sub-model for file generation

**What:** The orchestrator runs at user-selected reasoning effort, but `generateFiles` calls `getModelOptions(modelId, { reasoningEffort: 'low' })` internally. Separately, coding-agent-template uses `openai/gpt-5-nano` for branch names and titles.
**Where:**
- `apps/vibe-coding-platform/ai/gateway.ts` (the `getModelOptions` helper with provider-specific options)
- `apps/vibe-coding-platform/ai/tools/generate-files/get-contents.ts` line 40 (`reasoningEffort: 'low'`)
- `coding-agent-template/lib/utils/branch-name-generator.ts` lines 42–48 (`model: 'openai/gpt-5-nano'`)
**Why it matters for Hubify Labs:** File generation is the most expensive operation in a vibe-coding session (tens of thousands of output tokens). Dropping it to low reasoning effort on the same model, or to gpt-5-nano for dumb subtasks, is the cheapest cost optimization we can make. The gateway abstraction lets us do this without touching the agent code.

### 6. Claude Code inside the sandbox, authenticated through AI Gateway (`ANTHROPIC_BASE_URL` trick)

**What:** coding-agent-template installs Claude Code CLI inside the sandbox, then sets `ANTHROPIC_API_KEY=<gateway-key>` and `ANTHROPIC_BASE_URL=https://ai-gateway.vercel.sh`. Claude Code thinks it's hitting Anthropic direct but it's routed through AI Gateway.
**Where:**
- `coding-agent-template/lib/sandbox/agents/claude.ts` lines 74–100 (install + config file creation)
- `coding-agent-template/lib/sandbox/agents/claude.ts` lines 240–260 (env prefix on execution)
**Why it matters for Hubify Labs:** This is the single most important pattern for Hubify Labs if we want to ship "Claude Code building your app live". It gives us: (a) Claude Code's full native toolset (Read/Write/Edit/Glob/Bash/Grep), (b) centralized observability and rate-limiting via the gateway, (c) the ability to swap Anthropic→Bedrock→Vertex without changing sandbox code, and (d) per-user credential brokering because the gateway key can be rotated without redeploying sandboxes.

### 7. Stream-json parsing pattern for Claude Code's tool-use events

**What:** Claude Code's `--output-format stream-json --verbose` emits one JSON object per line. A Writable captures stdout, parses each line, translates tool-use events into human-readable status ("Editing app/page.tsx", "Running: pnpm install"), and streams them to Postgres via Drizzle — which becomes the UI feed.
**Where:** `coding-agent-template/lib/sandbox/agents/claude.ts` lines 272–380 (the `captureStdout` Writable and its handlers).
**Why it matters for Hubify Labs:** If we go with pattern #6 (Claude Code inside sandbox), this is how we get a live UI out of it. It's the translation layer between "raw CLI output" and "pretty chat message". We should copy this almost verbatim, adapting the tool-name-to-status-message mapping for any custom tools we add.

### 8. `sandbox.domain(port)` + iframe-remount-on-new-URL

**What:** Preview is a plain `<iframe src={sandbox.domain(port)}>`. When a new URL is set, the Zustand store also stores a fresh UUID, which becomes the iframe `key`, forcing a full React remount (bypassing cache).
**Where:**
- `apps/vibe-coding-platform/ai/tools/get-sandbox-url.ts` lines 28–45 (the `.domain(port)` call)
- `apps/vibe-coding-platform/app/state.ts` lines 70–72 (`setUrl` with UUID)
- `apps/vibe-coding-platform/app/preview.tsx` lines 10–18 (the `key={urlUUID}` trick)
**Why it matters for Hubify Labs:** This is the entire "live preview" pattern in ~30 lines. We don't need a reverse proxy, we don't need to tunnel, we don't need iframe sandboxing — Vercel Sandbox gives us a public HTTPS URL per port and we just point an iframe at it. The UUID-remount trick is the correct way to handle preview refresh after file changes.

---

## Hubify Labs application

These patterns will inform the Hubify Labs vibe-coding feature: "Houston types `build me a new lab dashboard for the X survey` and the orchestrator spins up a sandbox, generates code, runs it, shows preview, asks for approval, then commits to the lab repo."

The frontend for this lives in the Hubify Labs UI (left chat panel = vibe coding chat, right preview = live sandbox iframe). Same chat panel as the existing orchestrator chat — different mode/intent.

**Recommended architecture based on the two references:**

1. **Adopt vibe-coding-platform's 4-tool agent** as the core orchestrator for "create new app" flows (no repo yet).
2. **Adopt coding-agent-template's clone-edit-commit flow** for "edit existing Hubify Labs repo" flows — clone the repo, run Claude Code inside the sandbox via pattern #6, parse stream-json via pattern #7, push to a feature branch.
3. **Use AI Gateway centrally** via pattern #5, with Claude Opus 4.6 as the default orchestrator model and Claude Sonnet 4.6 at low reasoning effort as the "bulk file writer" sub-model.
4. **Copy the anti-loop system prompt** from vibe-coding-platform verbatim as a starting point.
5. **Store all tool progress as typed data-parts** (pattern #2) so the left-panel chat can show progress without cluttering the LLM context.
6. **Always expose port 3000 or 5173** via the auto-detection helper (coding-agent-template's `detectPortFromRepo`) and render a live iframe (pattern #8).

---

## References
- Vercel Sandbox SDK: https://vercel.com/docs/vercel-sandbox/sdk-reference
- Vercel Sandbox CLI: https://vercel.com/docs/vercel-sandbox/cli-reference
- Vercel Fluid Compute: https://vercel.com/docs/fluid-compute
- Vercel AI Gateway: https://vercel.com/docs/ai-gateway
- vibe-coding-platform source: https://github.com/vercel/examples/tree/main/apps/vibe-coding-platform
- coding-agent-template source: https://github.com/vercel-labs/coding-agent-template
