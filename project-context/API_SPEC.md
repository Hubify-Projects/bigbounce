# Hubify Labs — API Specification (REST + GraphQL)

**Status:** SPEC IN PROGRESS · Category D of `BUILD_READINESS_CHECKLIST.md`
**Author:** Houston Golden + Claude
**Date locked:** 2026-04-08
**Linked from:** PRD §43 (placeholder · TBD), `BUILD_READINESS_CHECKLIST.md` Category D
**OpenAPI YAML:** `project-context/api-spec.openapi.yaml` (TBD — separate file once locked)

---

## 0. The premise

This document is the **canonical contract** for everything that talks to the Hubify Labs platform. It is consumed by:

- The web app (`hubify-labs.com`) — uses REST + WebSockets
- The macOS desktop app (Tauri shell, see `DESKTOP_APP_SPEC.md`) — uses REST + WebSockets
- The CLI tool (`hubify`, see `CLI_SPEC.md` TBD) — uses REST
- The MCP server (see `MCP_SERVER_SPEC.md` TBD) — uses REST internally
- External integrations (webhooks, third-party agents) — use REST + webhooks
- AI agents inside the platform — use a thin internal Convex client OR the same REST endpoints

**The API is REST-first** with GraphQL as a secondary surface for read-heavy queries that benefit from field selection and graph traversal. Every REST endpoint has a GraphQL equivalent; not every GraphQL query has a REST equivalent.

---

## 1. Versioning

**URL path versioning.** All endpoints are under `/v1/...`. Future major versions get `/v2/...`. Backwards-incompatible changes require a major version bump. Additive changes (new fields, new endpoints) ship under the existing version.

**Why URL path versioning** (not header-based):
- Simpler for CLI / curl debugging
- Visible in browser dev tools
- Easy to route different versions to different deployments
- Industry standard for REST APIs (Stripe, GitHub, Twilio, etc.)

**Deprecation policy:** when a `/v1` endpoint is deprecated, it returns a `Sunset` header with the deprecation date and a `Link` header pointing to the `/v2` replacement. Deprecated endpoints work for at least 12 months after the announcement.

---

## 2. Authentication

### 2.1 Token format

**JWT (HS256)** signed with a per-environment secret. Token payload:

```json
{
  "iss": "hubify-labs",
  "sub": "user_<id>",          // user ID, OR "agent_<name>" for agent tokens
  "aud": "hubify-labs/api",
  "iat": 1712606400,
  "exp": 1712692800,            // 24h default expiration
  "jti": "<unique token id>",   // for revocation
  "scope": ["lab:bigbounce-hubify:rw", "lab:dark-energy:r"],  // per-lab scopes
  "type": "user" | "agent" | "service"
}
```

**Three token types:**
1. **User tokens** — issued via OAuth login flow. 24h expiration. Refresh via `/v1/auth/refresh`.
2. **Agent tokens** — issued by the lab orchestrator to its sub-agents. Per-agent scoped. No refresh — rotated by orchestrator on a daily schedule.
3. **Service tokens** — long-lived (90d) tokens for CI / cron / external integrations. Created via dashboard, manually revocable.

### 2.2 Auth endpoints

```
POST   /v1/auth/login            Login (OAuth callback handler)
POST   /v1/auth/refresh          Refresh an expiring token
DELETE /v1/auth/logout           Revoke current token
GET    /v1/auth/whoami           Return current user/agent/service info
POST   /v1/auth/tokens           Issue a new service token (admin only)
GET    /v1/auth/tokens           List service tokens
DELETE /v1/auth/tokens/:id       Revoke a service token
```

### 2.3 OAuth providers (v1)

- **GitHub** (default — every user has a GitHub account)
- **Google** (secondary — for non-GitHub users)
- **Magic link via email** (fallback — for users without OAuth)

OAuth flow uses standard authorization code grant with PKCE for the desktop app.

### 2.4 Per-lab scopes

The token's `scope` array lists which labs the bearer can access and at what permission level:

| Scope | Meaning |
|---|---|
| `lab:<slug>:r` | Read-only access to the named lab |
| `lab:<slug>:rw` | Read-write access |
| `lab:<slug>:admin` | Admin access (can change Lab Sharing settings, delete the lab, etc.) |
| `org:hubify-labs:admin` | Org-wide admin (Houston only — manages all labs) |
| `agent:<name>:invoke` | Can invoke this agent in any lab the agent is registered to |

The Lab Sovereignty Rule (PRD §40.11) is enforced at the auth layer: an agent's token cannot have `lab:lab_b:rw` if the agent belongs to lab_a. Cross-lab tokens are read-only by hard rule.

---

## 3. REST endpoint inventory

This is the locked endpoint inventory for v1. Every endpoint:
- Returns JSON
- Uses standard HTTP status codes
- Follows the error response format in §5
- Is rate-limited per §4

### 3.1 Labs

```
GET    /v1/labs                                   List labs the bearer has access to
POST   /v1/labs                                   Create a new lab (mutates GitHub org via internal hubify orchestrator)
GET    /v1/labs/:slug                             Get lab metadata
PATCH  /v1/labs/:slug                             Update lab metadata (mission, north star, director)
DELETE /v1/labs/:slug                             Delete a lab (admin only, soft-delete with 30-day recovery)
GET    /v1/labs/:slug/sharing                     Get the lab's sharing settings (per PRD §40.11)
PATCH  /v1/labs/:slug/sharing                     Update sharing settings
POST   /v1/labs/:slug/transfer                    Transfer ownership to another user (admin only)
```

### 3.2 Projects (research threads inside a lab)

```
GET    /v1/labs/:slug/projects                    List projects in the lab
POST   /v1/labs/:slug/projects                    Create a new project (typically via chat-graduation, see §3.6)
GET    /v1/labs/:slug/projects/:id                Get project metadata + auto-maintained Overview
PATCH  /v1/labs/:slug/projects/:id                Update project metadata (goal, deliverable, measurable)
DELETE /v1/labs/:slug/projects/:id                Archive a project (soft-delete)
GET    /v1/labs/:slug/projects/:id/overview       Get the auto-maintained Project Overview page (per PRD §40.12)
GET    /v1/labs/:slug/projects/:id/papers         List papers associated with this project (M:M, see §3.7)
POST   /v1/labs/:slug/projects/:id/papers         Associate a paper with this project (with role: primary/contributing/derivative)
DELETE /v1/labs/:slug/projects/:id/papers/:paperId  Remove an association
```

### 3.3 Pipelines (multi-step experiment sequences)

```
GET    /v1/labs/:slug/projects/:id/pipelines      List pipelines in a project
POST   /v1/labs/:slug/projects/:id/pipelines      Create a new pipeline
GET    /v1/labs/:slug/pipelines/:id               Get pipeline detail (steps, output, current state)
PATCH  /v1/labs/:slug/pipelines/:id               Update pipeline metadata
POST   /v1/labs/:slug/pipelines/:id/run           Trigger the pipeline (runs each step in order)
POST   /v1/labs/:slug/pipelines/:id/steps         Add a step to the pipeline
PATCH  /v1/labs/:slug/pipelines/:id/steps/:stepId Update a step
DELETE /v1/labs/:slug/pipelines/:id/steps/:stepId Remove a step
```

### 3.4 Experiments (atomic compute work)

```
GET    /v1/labs/:slug/experiments                 List experiments (all projects, paginated)
POST   /v1/labs/:slug/experiments                 Create a new experiment spec
GET    /v1/labs/:slug/experiments/:id             Get experiment detail (config, status, results, cost)
PATCH  /v1/labs/:slug/experiments/:id             Update experiment spec (only if status=draft)
POST   /v1/labs/:slug/experiments/:id/dispatch    Dispatch the experiment (runs §41 routing logic)
POST   /v1/labs/:slug/experiments/:id/cancel      Cancel a running experiment
GET    /v1/labs/:slug/experiments/:id/logs        Stream experiment logs (SSE)
GET    /v1/labs/:slug/experiments/:id/results     Get experiment results JSON
POST   /v1/labs/:slug/experiments/:id/promote     Promote results to a contribution (creates a contribution row)
```

**Dispatch payload** (per PRD §41):
```json
{
  "requires_gpu": true,
  "gpu_type": "H100" | "H200" | "A100" | null,
  "cpu_only": false,
  "expected_duration_min": 45,
  "priority": "low" | "med" | "high" | "critical",
  "checkpoint_interval_min": 10,
  "max_cost_usd": 25,
  "preferred_mode": "pod" | "serverless" | "auto"  // default auto, lets §41 routing decide
}
```

### 3.5 Files

```
GET    /v1/labs/:slug/files/*path                 Read a file (returns content + metadata)
PUT    /v1/labs/:slug/files/*path                 Write/create a file
DELETE /v1/labs/:slug/files/*path                 Delete a file
PATCH  /v1/labs/:slug/files/*path                 Move/rename a file (provide new_path in body)
GET    /v1/labs/:slug/files/*path?type=tree       List directory contents (when path is a dir)
POST   /v1/labs/:slug/files/upload                Multipart upload for binary files
GET    /v1/labs/:slug/files/*path?download=1      Force download (sets Content-Disposition)
```

**File path scoping:** the `:slug` in the URL must match a lab the bearer has access to. The server rejects path traversal (`../`) and absolute paths.

### 3.6 Chats (per PRD §40.7, §40.13)

```
GET    /v1/labs/:slug/chats                       List recent chats (defaults to last 20, paginated)
POST   /v1/labs/:slug/chats                       Create a new chat (with optional initial message)
GET    /v1/labs/:slug/chats/:id                   Get chat metadata + message history
DELETE /v1/labs/:slug/chats/:id                   Delete a chat
POST   /v1/labs/:slug/chats/:id/messages          Post a new message to the chat
GET    /v1/labs/:slug/chats/:id/messages          List messages (paginated)
POST   /v1/labs/:slug/chats/:id/promote           Trigger chat-to-project graduation (per PRD §40.6)
POST   /v1/labs/:slug/chats/:id/notechat          Save chat to Notes (per PRD §40.8 — `/notechat` slash command)
PATCH  /v1/labs/:slug/chats/:id                   Update chat metadata (title, mode, project association)
```

**Chat modes** (the `mode` field on a chat):
- `default` — orchestrator can take action (dispatch experiments, write files, etc.)
- `chat` — no-action mode (orchestrator can suggest but not act, per `/chat` and `/preresearch`)

### 3.7 Papers

```
GET    /v1/labs/:slug/papers                      List papers in the lab
POST   /v1/labs/:slug/papers                      Create a new paper (typically tied to a project)
GET    /v1/labs/:slug/papers/:id                  Get paper metadata + LaTeX source + compiled PDF
PATCH  /v1/labs/:slug/papers/:id                  Update paper metadata (title, version, target journal)
POST   /v1/labs/:slug/papers/:id/compile          Trigger LaTeX compile on a RunPod CPU pod
POST   /v1/labs/:slug/papers/:id/publish-loop     Trigger the 5-round publish-ready loop (per PRD §37)
GET    /v1/labs/:slug/papers/:id/projects         List projects associated with this paper (M:M)
POST   /v1/labs/:slug/papers/:id/projects         Associate a project with the paper
GET    /v1/labs/:slug/papers/:id/figures          List figures
POST   /v1/labs/:slug/papers/:id/figures          Add a figure
GET    /v1/labs/:slug/papers/:id/refs             Get the bibliography
PATCH  /v1/labs/:slug/papers/:id/refs             Update references.bib
```

### 3.8 Notes

```
GET    /v1/labs/:slug/notes                       List notes (paginated, by group: daily/prompts/snippets/links/evergreen)
POST   /v1/labs/:slug/notes                       Create a new note
GET    /v1/labs/:slug/notes/:filename             Get a note (full content)
PATCH  /v1/labs/:slug/notes/:filename             Update a note (full content replacement)
DELETE /v1/labs/:slug/notes/:filename             Delete a note
POST   /v1/labs/:slug/notes/:filename/star        Star/unstar a note (toggles favorite)
GET    /v1/labs/:slug/notes/search                Full-text search across notes
```

### 3.9 Agents

```
GET    /v1/labs/:slug/agents                      List agents in the lab
GET    /v1/labs/:slug/agents/:name                Get agent detail (10-tab content per PRD §34)
PATCH  /v1/labs/:slug/agents/:name                Update agent metadata (only via Houston or orchestrator)
POST   /v1/labs/:slug/agents/:name/invoke         Invoke the agent with a payload
POST   /v1/labs/:slug/agents/:name/wake           Wake an idle agent
POST   /v1/labs/:slug/agents/:name/sleep          Sleep an active agent
GET    /v1/labs/:slug/agents/:name/episodes       List recent episodes (last 50)
GET    /v1/labs/:slug/agents/:name/learnings      Get the operational learnings JSONL
POST   /v1/labs/:slug/agents/:name/learnings      Append a new learning (agents only)
GET    /v1/labs/:slug/agents/:name/diff           Get the diff for the current agent version
POST   /v1/labs/:slug/agents                      Create a new agent (orchestrator / Houston only)
```

### 3.10 Memory

```
GET    /v1/labs/:slug/memory/search               Search the lab's memory layer (4-layer per PRD §20)
POST   /v1/labs/:slug/memory/save                 Save a new memory entry
GET    /v1/labs/:slug/memory/by-layer/:layer      Get all entries from a specific layer (user/agent/lab/global)
DELETE /v1/labs/:slug/memory/:id                  Delete a memory entry
```

### 3.11 Contributions (with N-score per PRD §22)

```
GET    /v1/labs/:slug/contributions               List contributions (filtered by N-score)
POST   /v1/labs/:slug/contributions               Create a new contribution
GET    /v1/labs/:slug/contributions/:id           Get contribution detail (audit history, reviews)
PATCH  /v1/labs/:slug/contributions/:id           Update contribution metadata
POST   /v1/labs/:slug/contributions/:id/review    Trigger a re-review (e.g., 7-day or 30-day re-review)
GET    /v1/labs/:slug/contributions/:id/audits    Get the full novelty audit history
```

### 3.12 Compute (per PRD §24, §41)

```
GET    /v1/compute/credits                        Get current RunPod credit balance + 24h burn + projected runway
GET    /v1/compute/pods                           List active pods (across all labs the bearer can access)
POST   /v1/compute/pods                           Provision a new pod (per PRD §41 routing rules)
GET    /v1/compute/pods/:id                       Get pod detail
DELETE /v1/compute/pods/:id                       Stop a pod (graceful kill with checkpoint flush)
POST   /v1/compute/pods/:id/restart               Restart a stopped pod
GET    /v1/compute/serverless                     List serverless endpoints
POST   /v1/compute/serverless                     Create a new serverless endpoint
POST   /v1/compute/serverless/:id/invoke          Invoke a serverless endpoint
GET    /v1/compute/dispatch                       Get the dispatch decision tree status (current routing per §41)
```

### 3.13 Cross-lab comms (per PRD §40.11 — the gateway)

```
POST   /v1/comms/send                             Send a comm-event to another lab's orchestrator
GET    /v1/comms/inbox                            Get the current lab's inbox of comm-events
GET    /v1/comms/inbox/:id                        Get a specific comm-event detail
POST   /v1/comms/inbox/:id/accept                 Accept a comm-event suggestion (applies the suggested change)
POST   /v1/comms/inbox/:id/reject                 Reject a comm-event
GET    /v1/comms/sent                             Get sent comm-events from this lab
```

### 3.14 Webhooks (incoming)

```
POST   /v1/webhooks/runpod                        RunPod sends pod status updates here
POST   /v1/webhooks/github                        GitHub sends push/PR events here
POST   /v1/webhooks/openai                        OpenAI sends async API completions here (for peer-review-gpt)
POST   /v1/webhooks/anthropic                     Anthropic sends async completions here
POST   /v1/webhooks/vercel                        Vercel deploy status updates
```

### 3.15 Search (universal cmd-K backend)

```
GET    /v1/search?q=:query&type=:type             Universal search across the lab's entities (papers, experiments, agents, files, contributions, surveys, chats, notes, etc.) — backs the ⌘K palette in the UI
```

### 3.16 Standups (per PRD §27)

```
GET    /v1/labs/:slug/standups                    List standups (paginated)
GET    /v1/labs/:slug/standups/:id                Get standup transcript + action items
POST   /v1/labs/:slug/standups/trigger            Trigger an unscheduled standup (per `/standup-now` slash command)
GET    /v1/labs/:slug/standups/next               Get the next scheduled standup time
```

### 3.17 Routines (cron jobs per PRD §18)

```
GET    /v1/labs/:slug/routines                    List the lab's cron routines
GET    /v1/labs/:slug/routines/:id                Get routine detail (schedule, last fire, success rate)
POST   /v1/labs/:slug/routines                    Create a new routine
PATCH  /v1/labs/:slug/routines/:id                Update routine schedule
DELETE /v1/labs/:slug/routines/:id                Delete a routine
POST   /v1/labs/:slug/routines/:id/trigger        Trigger the routine immediately (out of schedule)
```

### 3.18 Backups (per PRD §6, §41)

```
GET    /v1/labs/:slug/backups                     List backup destinations
GET    /v1/labs/:slug/backups/:dest               Get backup destination detail
POST   /v1/labs/:slug/backups/:dest/sync          Trigger an immediate sync to this destination
GET    /v1/labs/:slug/backups/:dest/verify        Run an integrity check
GET    /v1/labs/:slug/backups/history             Get backup history (last 30 days)
```

### 3.19 Costs (per PRD §11, §41)

```
GET    /v1/labs/:slug/costs                       Get cost summary (today, MTD, projected)
GET    /v1/labs/:slug/costs/by-provider           Cost breakdown per provider (RunPod, Anthropic, OpenAI, etc.)
GET    /v1/labs/:slug/costs/history               30-day cost history (for the chart in the Costs view)
GET    /v1/labs/:slug/costs/top-experiments       Top N most expensive experiments
```

---

## 4. Rate limiting

**Per-token rate limits:**

| Token type | Limit |
|---|---|
| User (browser) | 600 req/min · 10K req/hour |
| Agent | 1200 req/min · 30K req/hour (agents are higher-throughput by design) |
| Service (CI/external) | 300 req/min · 5K req/hour |

**Per-endpoint overrides:**
- `/v1/files/*` — 60 writes/min (filesystem rate-limited)
- `/v1/experiments/*/dispatch` — 30/min (compute is expensive)
- `/v1/auth/login` — 10/min (anti-brute-force)

**Rate limit headers** (returned on every response):
```
X-RateLimit-Limit: 600
X-RateLimit-Remaining: 547
X-RateLimit-Reset: 1712607000
```

When the limit is hit, the server returns `429 Too Many Requests` with a `Retry-After` header.

---

## 5. Error response format (RFC 7807 Problem Details)

Every error response uses the RFC 7807 format. Example `404`:

```json
{
  "type": "https://hubify-labs.com/errors/not-found",
  "title": "Resource not found",
  "status": 404,
  "detail": "No experiment with ID exp_abc123 in lab bigbounce-hubify",
  "instance": "/v1/labs/bigbounce-hubify/experiments/exp_abc123"
}
```

Common error types:

| Status | Type slug | When |
|---|---|---|
| 400 | `bad-request` | Malformed request body / missing required field |
| 401 | `unauthenticated` | No token / expired token |
| 403 | `forbidden` | Token lacks scope for this resource |
| 404 | `not-found` | Resource doesn't exist |
| 409 | `conflict` | Resource state prevents operation (e.g., editing a published paper) |
| 422 | `validation-failed` | Body validates against schema but business rules reject (e.g., experiment without `requires_gpu`) |
| 429 | `rate-limited` | Per-token or per-endpoint rate limit exceeded |
| 500 | `internal-error` | Server bug — log + alert |
| 502 | `upstream-failed` | Downstream service (RunPod, Convex, OpenAI) failed |
| 503 | `unavailable` | Server intentionally returning unavailable (maintenance) |

---

## 6. WebSocket / SSE for live updates

REST endpoints are request-response. Live updates use Server-Sent Events (SSE) or WebSockets:

**SSE (one-way streams from server to client):**
```
GET  /v1/labs/:slug/experiments/:id/logs    SSE stream of experiment log lines
GET  /v1/labs/:slug/comms/stream             SSE stream of new comm-events for this lab
GET  /v1/labs/:slug/activity/stream          SSE stream of the live activity feed
GET  /v1/labs/:slug/standups/stream          SSE stream of in-progress standup transcripts
GET  /v1/compute/credits/stream              SSE stream of credit balance changes (for the header pill)
```

**WebSockets** (two-way for chat sessions):
```
WS   /v1/labs/:slug/chats/:id/socket          WebSocket for live chat with the orchestrator
```

The chat WebSocket carries:
- User → server: typed messages, file attachments, voice transcripts
- Server → user: orchestrator responses (token-by-token streaming), tool call previews, dispatch confirmations

---

## 7. GraphQL (alternative surface for read-heavy queries)

GraphQL lives at a single endpoint:

```
POST /v1/graphql
```

The schema mirrors the REST inventory but allows field selection and graph traversal in a single round trip. Example query:

```graphql
query LabDashboard($slug: String!) {
  lab(slug: $slug) {
    name
    mission
    northStar
    director { name }
    projects(first: 5, orderBy: { lastActivity: DESC }) {
      id
      name
      goal
      deliverable
      papers {
        id
        title
        version
        ready
      }
      experiments(status: RUNNING) {
        id
        title
        progress
        cost
      }
    }
    credits {
      balance
      runwayHours
      threshold
    }
  }
}
```

**When to use GraphQL vs REST:**
- **REST** for everything by default (simpler, cacheable, easier for non-Hubify clients)
- **GraphQL** for the web app's complex dashboard queries (one round trip vs 5-10)
- **GraphQL** for the agent's `getLabContext()` calls (agents need a lot of context in one shot)

GraphQL is OPTIONAL for v1 — REST covers all use cases. GraphQL ships in v1.1 if dashboard performance demands it.

---

## 8. The OpenAPI YAML lock

The full machine-readable spec lives at:

```
project-context/api-spec.openapi.yaml
```

(This file is the next item in Category D — to be written after this human-readable spec is locked.)

The YAML enables:
- Auto-generated TypeScript client (`@hubify-labs/api-client`)
- Auto-generated Go / Python / Rust clients
- Auto-generated docs at `hubify-labs.com/docs/api-reference/...` (Mintlify-rendered)
- Auto-generated Postman collection
- API contract testing in CI

---

## 9. Out of scope for v1

These are explicitly NOT in v1 — added in v1.1+ as needed:

- ❌ Webhooks OUT (sending webhooks to external URLs) — only incoming for v1
- ❌ Batch operations (`POST /v1/batch`) — single-resource per request for v1
- ❌ Custom field projections on REST (use GraphQL instead)
- ❌ JSON-RPC alternative surface
- ❌ Server-side pagination cursors for all list endpoints — v1 uses offset+limit, cursors come in v1.1
- ❌ File versioning API (file history) — files are git-tracked, v1.1 adds an API surface for git history
- ❌ Audit log API (read-only access to audit events) — v1.1
- ❌ Multi-tenant API key management UI — Houston is the only tenant in v1

---

## 10. The next steps

After this spec is reviewed by Houston:

1. **Lock the OpenAPI YAML** — turn this human-readable spec into `api-spec.openapi.yaml` (the machine-readable contract)
2. **Generate the TypeScript client** — `@hubify-labs/api-client` package
3. **Stub the endpoints in Convex** — every endpoint above gets a Convex query/mutation/action
4. **Wire the web mockup to the live API** — replace mock data with real API calls
5. **Build the CLI** (Category F) on top of the same API
6. **Build the MCP server** (Category E) that wraps the API for AI agents

---

## 11. Open questions

1. **JWT vs opaque tokens** — JWT is the default. If we need easy revocation we can switch to opaque tokens with a revocation list. Lean: JWT + short expiration + refresh.
2. **Rate limiting backend** — Redis (separate service) vs Convex-native rate limiting? Default: Convex-native (no extra service).
3. **WebSocket framework** — Convex has built-in real-time queries that mostly replace WebSockets. Reconsider WebSockets only for the chat-streaming use case.
4. **GraphQL implementation** — Apollo Server vs urql vs Convex GraphQL adapter? Default: defer until v1.1, decide then.
5. **API gateway** — direct Convex HTTP routes vs Cloudflare Workers in front? Default: direct Convex for v1, add Cloudflare Workers later for caching + rate limiting if traffic demands it.
6. **CORS policy** — strict allowlist (web app + desktop app + CLI only) vs open (`*`)? Default: strict allowlist.
7. **API documentation hosting** — Mintlify subpath (`hubify-labs.com/docs/api-reference/...`) per the docs port plan in PRD §40.17 Tier 3.

---

## 12. What this spec stress-tests

Per the BUILD_READINESS framing, every spec file should call out what it stress-tests on the architecture:

- **The unified contract** — proves that one REST surface can serve the web app, desktop app, CLI, MCP server, and external integrations without per-client special cases
- **The Lab Sovereignty Rule (PRD §40.11)** at the auth layer — cross-lab tokens are read-only by hard rule
- **The §41 dispatch routing** as a first-class endpoint — `POST /v1/experiments/:id/dispatch` runs the routing tree
- **The credit monitoring loop** as a first-class endpoint — `GET /v1/compute/credits/stream` (SSE) feeds the header pill in real time
- **The publish-loop trigger** as a first-class endpoint — `POST /v1/papers/:id/publish-loop` invokes the 5-round loop from PRD §37
- **Cross-lab comms** as a first-class endpoint — `POST /v1/comms/send` is the only way Lab A can suggest changes to Lab B
- **Single-vendor compute (RunPod)** as a first-class assumption — every compute endpoint targets RunPod, no provider abstraction needed (per PRD §24 lock)

If this API spec ships and the YAML is generated successfully, the platform's contract layer is locked.

---

## 13. Status

**This file:** Category D item 1 of the BUILD_READINESS_CHECKLIST. Bootstraps Category D from 0% → ~70% in one shot:
- ✅ Item 1: Write API_SPEC.md (this file)
- ✅ Item 2: REST endpoint inventory (§3, 19 endpoint groups, ~85 endpoints)
- ⏸ Item 3: GraphQL schema (mentioned in §7, full schema TBD)
- ✅ Item 4: Auth & rate limiting policy (§2, §4)
- ✅ Item 5: Versioning policy (§1)
- ✅ Item 6: Error response format (§5, RFC 7807)
- ⏸ Item 7: OpenAPI YAML lock (next item — `api-spec.openapi.yaml`)

**5 of 7 Category D items checked off in this single iteration.**
