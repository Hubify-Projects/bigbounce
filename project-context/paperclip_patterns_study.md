## Paperclip Patterns Study — for Hubify Labs

**Date:** 2026-04-08
**Status:** Inspiration / pattern extraction, NOT a fork plan
**Source:** https://github.com/paperclipai/paperclip
**Branch studied:** `master` (commit time of writing: 2026-04 era)

---

## TL;DR

Five things Hubify Labs should steal in priority order:

1. **The wakeup-coordinator + heartbeat-run model.** Every "agent does work" event in paperclip funnels through a single `enqueueWakeup()` function that writes one row to `agent_wakeup_requests` and one row to `heartbeat_runs`. There is no other path to spawn an agent. This makes coalescing, budget enforcement, restart recovery, and audit logging trivially correct.
2. **Atomic checkout via single-row UPDATE WHERE.** Two agents racing to claim the same task is resolved by a `UPDATE issues SET ... WHERE id = ? AND status IN (?) AND (assignee_agent_id IS NULL OR ... ) AND (execution_run_id IS NULL OR ...)`. The loser gets `409 Conflict` and is told never to retry. No locks, no leases, no Redis.
3. **Comments as the universal communication channel.** No DMs, no chat rooms, no Slack-channel-per-agent. Every status update, question, finding, and handoff is a comment on an issue, surfaced via `@AgentName` mentions that automatically wake the mentioned agent.
4. **Activity log as a unified, append-only event stream.** A single `activity_log` table records `(actorType, actorId, action, entityType, entityId, agentId, runId, details)`. Combined with `heartbeat_run_events` (per-run timeline) and live-pushed `LIVE_EVENT_TYPES`, you get a Linear-quality activity feed without designing one.
5. **`tickTimers()` is the only "standup" pattern.** Paperclip has no all-hands meetings or standup ceremony. It has a worker that periodically iterates over agents and calls `enqueueWakeup(agentId, { source: "timer", reason: "interval_elapsed" })`. The standup IS the heartbeat. Sync points are emergent from the wakeup graph.

The rest of this document drills into each of these and quotes the actual code.

---

## Repo Overview

**What is paperclip?** A Node.js + React control plane for "AI agent companies". You define an org chart of agents (CEO, CTO, engineers, etc.), give them goals, and they wake on a schedule, claim issues from a backlog, do work, and comment on each other's tasks. It treats agent runtimes (Claude Code, Codex, Cursor, OpenClaw, generic process/HTTP) as **adapters** that all conform to one `agent-run/v1` protocol.

**Stack.** Express REST API on the server, React + Vite UI, Drizzle ORM with PostgreSQL (PGlite embedded for local dev), pnpm workspaces. Schemas are defined in `packages/db/src/schema/*.ts`, shared types/validators in `packages/shared/src/`, server services in `server/src/services/*.ts`, REST routes in `server/src/routes/*.ts`.

**Architecture in one paragraph.** Every domain entity is **company-scoped**. The unit of work is an `issue`. Each issue has a single assignee (agent or user). Agents don't run continuously — they run in **heartbeats**, short execution windows triggered by one of four wakeup sources (`timer | assignment | on_demand | automation`). All wakeups go through a single `enqueueWakeup()` coordinator which writes to `agent_wakeup_requests` (a DB-backed queue with coalescing) and creates a `heartbeat_runs` row. A worker loop (`startNextQueuedRunForAgent` + `claimQueuedRun`) atomically transitions queued runs to running and invokes the agent's adapter. Adapters emit status updates, log chunks, and token usage via hooks. When the adapter exits, the executor finalizes the run, updates the agent's runtime state, and pushes live events over a per-company websocket. Cross-agent communication happens entirely through issue comments and `@AgentName` mentions, which themselves trigger wakeups.

---

## 1. Task Management Model

### 1.1 The `issues` schema (verbatim)

Source: `packages/db/src/schema/issues.ts`

```ts
export const issues = pgTable(
  "issues",
  {
    id: uuid("id").primaryKey().defaultRandom(),
    companyId: uuid("company_id").notNull().references(() => companies.id),
    projectId: uuid("project_id").references(() => projects.id),
    projectWorkspaceId: uuid("project_workspace_id").references(() => projectWorkspaces.id, { onDelete: "set null" }),
    goalId: uuid("goal_id").references(() => goals.id),
    parentId: uuid("parent_id").references((): AnyPgColumn => issues.id),
    title: text("title").notNull(),
    description: text("description"),
    status: text("status").notNull().default("backlog"),
    priority: text("priority").notNull().default("medium"),
    assigneeAgentId: uuid("assignee_agent_id").references(() => agents.id),
    assigneeUserId: text("assignee_user_id"),
    checkoutRunId: uuid("checkout_run_id").references(() => heartbeatRuns.id, { onDelete: "set null" }),
    executionRunId: uuid("execution_run_id").references(() => heartbeatRuns.id, { onDelete: "set null" }),
    executionAgentNameKey: text("execution_agent_name_key"),
    executionLockedAt: timestamp("execution_locked_at", { withTimezone: true }),
    createdByAgentId: uuid("created_by_agent_id").references(() => agents.id),
    createdByUserId: text("created_by_user_id"),
    issueNumber: integer("issue_number"),
    identifier: text("identifier"),
    originKind: text("origin_kind").notNull().default("manual"),
    ...
```

Key observations:

- **Single assignee.** Either `assigneeAgentId` or `assigneeUserId`, never both. There is no concept of "team owners" or co-assignees.
- **Goal ancestry.** `goalId`, `projectId`, and `parentId` form a chain so an agent reading a leaf task can walk up to the company goal. This is what paperclip means by "goal-aware execution".
- **Two run pointers.** `checkoutRunId` is who currently owns the checkout. `executionRunId` is the live heartbeat run executing it. They start identical and diverge only when adopting a stale checkout (a "tilldone"-style takeover — see §3).
- **`executionAgentNameKey`.** A normalized cached agent-name string used to detect "the same agent is racing for an issue under a different DB id" (e.g. recreated after a hire).
- **`originKind`** is `manual` or `routine_execution`. This is how routine-spawned issues (paperclip's cron-driven "standups") are linked back to the routine that created them.

### 1.2 Status enum (verbatim)

Source: `packages/shared/src/constants.ts`

```ts
export const ISSUE_STATUSES = [
  "backlog",
  "todo",
  "in_progress",
  "in_review",
  "done",
  "blocked",
  "cancelled",
] as const;
export type IssueStatus = (typeof ISSUE_STATUSES)[number];

export const ISSUE_PRIORITIES = ["critical", "high", "medium", "low"] as const;

export const ISSUE_ORIGIN_KINDS = ["manual", "routine_execution"] as const;

export const ISSUE_RELATION_TYPES = ["blocks"] as const;
```

The lifecycle is documented in `docs/api/issues.md`:

```
backlog -> todo -> in_progress -> in_review -> done
                       |              |
                    blocked       in_progress
```

That is the entire state machine. No "ready for review", no "needs design", no per-team customization. The simplicity is the point.

### 1.3 Task assignment / routing

There is **no router**. Tasks are assigned by:

1. A human (board operator) creates an issue with `assigneeAgentId` set.
2. A manager-tier agent (CEO, CTO) creates a subtask via `POST /api/companies/:companyId/issues` with `parentId` set, choosing the assignee themselves.
3. An agent self-assigns via `POST /api/issues/:id/checkout` (only allowed on `todo`/`backlog`/`blocked`/`in_review`).

The "routing logic" lives in **the CEO agent's prompt**, not the server. Here is the entire routing rule set, verbatim from `server/src/onboarding-assets/ceo/AGENTS.md`:

```md
## Delegation (critical)

You MUST delegate work rather than doing it yourself. When a task is assigned to you:

1. **Triage it** -- read the task, understand what's being asked, and determine which department owns it.
2. **Delegate it** -- create a subtask with `parentId` set to the current task, assign it to the right direct report, and include context about what needs to happen. Use these routing rules:
   - **Code, bugs, features, infra, devtools, technical tasks** → CTO
   - **Marketing, content, social media, growth, devrel** → CMO
   - **UX, design, user research, design-system** → UXDesigner
   - **Cross-functional or unclear** → break into separate subtasks for each department, or assign to the CTO if it's primarily technical with a design component
   - If the right report doesn't exist yet, use the `paperclip-create-agent` skill to hire one before delegating.
3. **Do NOT write code, implement features, or fix bugs yourself.** Your reports exist for this. Even if a task seems small or quick, delegate it.
```

The router is a markdown file. The agent reads it on every wake.

### 1.4 Atomic checkout

Source: `server/src/services/issues.ts`, around line 1786. This is the entire conflict-resolution mechanism for two agents racing for the same task.

```ts
const updated = await db
  .update(issues)
  .set({
    assigneeAgentId: agentId,
    assigneeUserId: null,
    checkoutRunId,
    executionRunId: checkoutRunId,
    status: "in_progress",
    startedAt: now,
    updatedAt: now,
  })
  .where(
    and(
      eq(issues.id, id),
      inArray(issues.status, expectedStatuses),
      or(isNull(issues.assigneeAgentId), sameRunAssigneeCondition),
      executionLockCondition,
    ),
  )
  .returning()
  .then((rows) => rows[0] ?? null);

if (updated) {
  const [enriched] = await withIssueLabels(db, [updated]);
  return enriched;
}

// ... otherwise re-read and either return self-owned or throw 409
throw conflict("Issue checkout conflict", {
  issueId: current.id,
  status: current.status,
  assigneeAgentId: current.assigneeAgentId,
  checkoutRunId: current.checkoutRunId,
  executionRunId: current.executionRunId,
});
```

The validator is dead simple:

```ts
// packages/shared/src/validators/issue.ts
export const checkoutIssueSchema = z.object({
  agentId: z.string().uuid(),
  expectedStatuses: z.array(z.enum(ISSUE_STATUSES)).nonempty(),
});
```

The agent passes `expectedStatuses: ["todo", "backlog", "blocked", "in_review"]` and the DB enforces it. No locks, no leases, no Redis. The agent contract from `docs/guides/agent-developer/task-workflow.md`:

> **Rules:**
> - Always checkout before working
> - Never retry a 409 — pick a different task
> - If you already own the task, checkout succeeds idempotently

### 1.5 Task dependencies

Source: `packages/db/src/schema/issue_relations.ts`

```ts
export const issueRelations = pgTable(
  "issue_relations",
  {
    id: uuid("id").primaryKey().defaultRandom(),
    companyId: uuid("company_id").notNull().references(() => companies.id),
    issueId: uuid("issue_id").notNull().references(() => issues.id, { onDelete: "cascade" }),
    relatedIssueId: uuid("related_issue_id").notNull().references(() => issues.id, { onDelete: "cascade" }),
    type: text("type").$type<"blocks">().notNull(),
    createdByAgentId: uuid("created_by_agent_id").references(() => agents.id, { onDelete: "set null" }),
    createdByUserId: text("created_by_user_id"),
    createdAt: timestamp("created_at", { withTimezone: true }).notNull().defaultNow(),
    updatedAt: timestamp("updated_at", { withTimezone: true }).notNull().defaultNow(),
  },
```

Only **one** relation type exists: `"blocks"`. Hierarchy is via `issues.parentId`. There is no "depends on", no "subtask of", no "duplicate of". The `ISSUE_RELATION_TYPES = ["blocks"] as const` line deliberately constrains this.

When a blocker resolves, paperclip auto-wakes the dependents. From `server/src/routes/issues.ts` around line 1499:

```ts
const becameDone = existing.status !== "done" && issue.status === "done";
if (becameDone) {
  const dependents = await svc.listWakeableBlockedDependents(issue.id);
  for (const dependent of dependents) {
    addWakeup(dependent.assigneeAgentId, {
      source: "automation",
      triggerDetail: "system",
      reason: "issue_blockers_resolved",
      payload: {
        issueId: dependent.id,
        resolvedBlockerIssueId: issue.id,
        blockerIssueIds: dependent.blockerIssueIds,
      },
      ...
```

And similarly for parent issues whose children all completed (lines 1526–1552). The dependency graph is "live" — completing a task fans out wakeups to anyone who was waiting on it.

### 1.6 Task completion and verification

Completion is on the honor system: an agent calls `PATCH /api/issues/:id { status: "done", comment: "..." }` and the server accepts it. Verification is delegated to the **execution policy** system, which is paperclip's mechanism for cross-agent code review.

Source: `packages/shared/src/types/issue.ts`

```ts
export interface IssueExecutionStage {
  id: string;
  type: IssueExecutionStageType;       // "review" | "approval"
  approvalsNeeded: 1;                  // literally locked to 1
  participants: IssueExecutionStageParticipant[];
}

export interface IssueExecutionPolicy {
  mode: IssueExecutionPolicyMode;      // "normal" | "auto"
  commentRequired: boolean;
  stages: IssueExecutionStage[];
}

export interface IssueExecutionState {
  status: IssueExecutionStateStatus;   // "idle" | "pending" | "changes_requested" | "completed"
  currentStageId: string | null;
  currentStageIndex: number | null;
  currentStageType: IssueExecutionStageType | null;
  currentParticipant: IssueExecutionStagePrincipal | null;
  returnAssignee: IssueExecutionStagePrincipal | null;
  completedStageIds: string[];
  lastDecisionId: string | null;
  lastDecisionOutcome: IssueExecutionDecisionOutcome | null;
}
```

When an agent marks an issue `done`, the `applyIssueExecutionPolicyTransition` function (in `server/src/services/issue-execution-policy.ts`) runs the policy state machine. If a review stage exists, the issue is reassigned to the reviewer and moved to `in_review` instead of `done`. The reviewer can then either:

- Comment with `{ status: "done" }` → stage marked `approved`, advance to next stage or fully complete
- Comment with `{ status: "in_progress" }` → stage marked `changes_requested`, return to original assignee

Crucially, paperclip enforces that **only the active reviewer can advance the stage**:

```ts
// server/src/services/issue-execution-policy.ts:231
if (currentStage && input.issue.status === "in_review") {
  if (!principalsEqual(existingState?.currentParticipant ?? null, actor)) {
    if (requestedStatus && requestedStatus !== "in_review") {
      throw unprocessable("Only the active reviewer or approver can advance the current execution stage");
    }
    return { patch };
  }
```

And approving requires a comment:

```ts
if (requestedStatus === "done") {
  if (!input.commentBody?.trim()) {
    throw unprocessable("Approving a review or approval stage requires a comment");
  }
```

Each decision is persisted in `issue_execution_decisions`:

```ts
// packages/db/src/schema/issue_execution_decisions.ts
export const issueExecutionDecisions = pgTable(
  "issue_execution_decisions",
  {
    id: uuid("id").primaryKey().defaultRandom(),
    companyId: uuid("company_id").notNull().references(() => companies.id),
    issueId: uuid("issue_id").notNull().references(() => issues.id, { onDelete: "cascade" }),
    stageId: uuid("stage_id").notNull(),
    stageType: text("stage_type").notNull(),
    actorAgentId: uuid("actor_agent_id").references(() => agents.id),
    actorUserId: text("actor_user_id"),
    outcome: text("outcome").notNull(),
    body: text("body").notNull(),
    createdByRunId: uuid("created_by_run_id").references(() => heartbeatRuns.id, { onDelete: "set null" }),
    ...
```

This gives a permanent, linkable record of "agent X reviewed issue Y at run Z and said this".

### 1.7 Comments and threads

Source: `packages/db/src/schema/issue_comments.ts`

```ts
export const issueComments = pgTable(
  "issue_comments",
  {
    id: uuid("id").primaryKey().defaultRandom(),
    companyId: uuid("company_id").notNull().references(() => companies.id),
    issueId: uuid("issue_id").notNull().references(() => issues.id),
    authorAgentId: uuid("author_agent_id").references(() => agents.id),
    authorUserId: text("author_user_id"),
    createdByRunId: uuid("created_by_run_id").references(() => heartbeatRuns.id, { onDelete: "set null" }),
    body: text("body").notNull(),
    createdAt: timestamp("created_at", { withTimezone: true }).notNull().defaultNow(),
    updatedAt: timestamp("updated_at", { withTimezone: true }).notNull().defaultNow(),
  },
```

Notable choices:

- **Flat list, no threading.** Comments are not nested. There is no `parentCommentId`. A "thread" is just the comment list ordered by `createdAt`.
- **`createdByRunId`.** Every comment knows which heartbeat run wrote it. This is what makes "show me everything agent X said in run Z" trivially queryable.
- **Author is XOR.** Either `authorAgentId` or `authorUserId`, never both.
- **Trigram body search** — `bodySearchIdx` uses `gin_trgm_ops`, so the entire conversation history is fuzzy-searchable.

There is **no DM, channel, or chat-room concept** anywhere in the schema. All inter-agent communication is comments on shared issues.

---

## 2. Activity Feed and Agent Communication

### 2.1 The unified activity log

Source: `packages/db/src/schema/activity_log.ts`

```ts
export const activityLog = pgTable(
  "activity_log",
  {
    id: uuid("id").primaryKey().defaultRandom(),
    companyId: uuid("company_id").notNull().references(() => companies.id),
    actorType: text("actor_type").notNull().default("system"),  // "agent" | "user" | "system"
    actorId: text("actor_id").notNull(),
    action: text("action").notNull(),
    entityType: text("entity_type").notNull(),
    entityId: text("entity_id").notNull(),
    agentId: uuid("agent_id").references(() => agents.id),
    runId: uuid("run_id").references(() => heartbeatRuns.id),
    details: jsonb("details").$type<Record<string, unknown>>(),
    createdAt: timestamp("created_at", { withTimezone: true }).notNull().defaultNow(),
  },
  (table) => ({
    companyCreatedIdx: index("activity_log_company_created_idx").on(table.companyId, table.createdAt),
    runIdIdx: index("activity_log_run_id_idx").on(table.runId),
    entityIdx: index("activity_log_entity_type_id_idx").on(table.entityType, table.entityId),
  }),
);
```

This is **one table** that records every mutation in the entire system. The shared type:

```ts
// packages/shared/src/types/activity.ts
export interface ActivityEvent {
  id: string;
  companyId: string;
  actorType: "agent" | "user" | "system";
  actorId: string;
  action: string;
  entityType: string;
  entityId: string;
  agentId: string | null;
  runId: string | null;
  details: Record<string, unknown> | null;
  createdAt: Date;
}
```

The list query (`server/src/services/activity.ts`) supports filtering by `agentId`, `entityType`, `entityId`. That's it. The Activity page in the UI is a single SELECT against this table, ordered by `createdAt DESC`. No materialized views, no event sourcing, no Kafka.

The standard action names (from `doc/spec/agent-runs.md` §13.2) are:

```
wakeup.requested
wakeup.coalesced
heartbeat.started
heartbeat.finished
heartbeat.failed
heartbeat.cancelled
runtime_state.updated
issue.checked_out
issue.commented
issue.status_changed
```

### 2.2 Per-run timeline (`heartbeat_run_events`)

Source: `packages/db/src/schema/heartbeat_run_events.ts`

```ts
export const heartbeatRunEvents = pgTable(
  "heartbeat_run_events",
  {
    id: bigserial("id", { mode: "number" }).primaryKey(),
    companyId: uuid("company_id").notNull().references(() => companies.id),
    runId: uuid("run_id").notNull().references(() => heartbeatRuns.id),
    agentId: uuid("agent_id").notNull().references(() => agents.id),
    seq: integer("seq").notNull(),
    eventType: text("event_type").notNull(),
    stream: text("stream"),    // "system" | "stdout" | "stderr"
    level: text("level"),      // "info" | "warn" | "error"
    color: text("color"),
    message: text("message"),
    payload: jsonb("payload").$type<Record<string, unknown>>(),
    createdAt: timestamp("created_at", { withTimezone: true }).notNull().defaultNow(),
  },
```

Two-tier separation:

- **`activity_log`** = company-wide audit trail, one row per *mutation*, low cardinality, infinite retention.
- **`heartbeat_run_events`** = per-run microtimeline (lifecycle, status pings, structured events), `bigserial` because there are tons, ordered by `seq` per run. Full stdout/stderr go to a separate `RunLogStore` (filesystem or S3), not to Postgres.

This is the "cheap-DB-events + expensive-blob-store" split. The doc spells it out (`doc/spec/agent-runs.md` §12.2):

> 1. Persist full stdout/stderr stream to configured `RunLogStore`.
> 2. Persist only lightweight run metadata/events in Postgres (`heartbeat_runs`, `heartbeat_run_events`).
> 3. Persist bounded `stdout_excerpt` and `stderr_excerpt` in Postgres for quick diagnostics.

### 2.3 Live event types (websocket push)

Source: `packages/shared/src/constants.ts`

```ts
export const LIVE_EVENT_TYPES = [
  "heartbeat.run.queued",
  "heartbeat.run.status",
  "heartbeat.run.event",
  "heartbeat.run.log",
  "agent.status",
  "activity.logged",
  "plugin.ui.updated",
  "plugin.worker.crashed",
  ...
] as const;
```

The websocket envelope from the spec:

```json
{
  "eventId": "uuid-or-monotonic-id",
  "companyId": "uuid",
  "type": "heartbeat.run.status",
  "entityType": "heartbeat_run",
  "entityId": "uuid",
  "occurredAt": "2026-02-17T12:00:00Z",
  "payload": {}
}
```

One channel per company: `GET /api/companies/:companyId/events/ws`. Auth is either board session or agent API key (company-bound). The UI subscribes once and receives every relevant update. If the socket drops, the client falls back to short polling.

### 2.4 Color coding

Status colors are part of the adapter protocol, not the UI. Source: `doc/spec/agent-runs.md` §6:

```ts
type StatusColor = "neutral" | "blue" | "green" | "yellow" | "red";

interface AdapterHooks {
  status?: (update: { message: string; color?: StatusColor }) => Promise<void>;
  log?: (event: { stream: "stdout" | "stderr" | "system"; chunk: string }) => Promise<void>;
  usage?: (usage: TokenUsage) => Promise<void>;
  event?: (eventType: string, payload: Record<string, unknown>) => Promise<void>;
}
```

Five colors, period. The adapter pushes a `{ message, color }` object during execution, the executor persists it as a `heartbeat_run_events` row with `color` set, and the UI renders the latest one as the agent's current status pill.

### 2.5 @-mention extraction (the entire algorithm)

Source: `server/src/services/issues.ts:2309`

```ts
findMentionedAgents: async (companyId: string, body: string) => {
  const re = /\B@([^\s@,!?.]+)/g;
  const tokens = new Set<string>();
  let m: RegExpExecArray | null;
  while ((m = re.exec(body)) !== null) {
    const normalized = normalizeAgentMentionToken(m[1]);
    if (normalized) tokens.add(normalized.toLowerCase());
  }

  const explicitAgentMentionIds = extractAgentMentionIds(body);
  if (tokens.size === 0 && explicitAgentMentionIds.length === 0) return [];
  const rows = await db.select({ id: agents.id, name: agents.name })
    .from(agents).where(eq(agents.companyId, companyId));
  const resolved = new Set<string>(explicitAgentMentionIds);
  for (const agent of rows) {
    if (tokens.has(agent.name.toLowerCase())) {
      resolved.add(agent.id);
    }
  }
  return [...resolved];
},
```

A regex, a set, a join against the agents table, return ids. The mention triggers a wakeup by the route handler at `server/src/routes/issues.ts:1478`:

```ts
for (const mentionedId of mentionedIds) {
  if (actor.actorType === "agent" && actor.actorId === mentionedId) continue;
  addWakeup(mentionedId, {
    source: "automation",
    triggerDetail: "system",
    reason: "issue_comment_mentioned",
    payload: { issueId: id, commentId: comment.id },
    requestedByActorType: actor.actorType,
    requestedByActorId: actor.actorId,
    contextSnapshot: {
      issueId: id,
      taskId: id,
      commentId: comment.id,
      wakeCommentId: comment.id,
      wakeReason: "issue_comment_mentioned",
      source: "comment.mention",
    },
  });
}
```

Two important rules baked in:

1. **An agent mentioning itself does NOT wake itself** (avoids loops).
2. **Mentions are deduped via the `wakeups` Map** (a single comment with `@A @A @B` produces two wakeups, not three).

The agent guide in `docs/guides/agent-developer/comments-and-communication.md` adds the social rules:

> - **Don't overuse mentions** — each mention triggers a budget-consuming heartbeat
> - **Don't use mentions for assignment** — create/assign a task instead
> - **Mention handoff exception** — if an agent is explicitly @-mentioned with a clear directive to take a task, they may self-assign via checkout

---

## 3. Multi-Agent Coordination

### 3.1 The wakeup coordinator (the heart of the system)

Source: `server/src/services/heartbeat.ts:3613`

```ts
async function enqueueWakeup(agentId: string, opts: WakeupOptions = {}) {
  const source = opts.source ?? "on_demand";
  const triggerDetail = opts.triggerDetail ?? null;
  const contextSnapshot: Record<string, unknown> = { ...(opts.contextSnapshot ?? {}) };
  const reason = opts.reason ?? null;
  const payload = opts.payload ?? null;
  ...
  const agent = await getAgent(agentId);
  if (!agent) throw notFound("Agent not found");
  ...
  const budgetBlock = await budgets.getInvocationBlock(agent.companyId, agentId, {
    issueId,
    projectId,
  });
  if (budgetBlock) {
    await writeSkippedRequest("budget.blocked");
    throw conflict(budgetBlock.reason, {
      scopeType: budgetBlock.scopeType,
      scopeId: budgetBlock.scopeId,
    });
  }

  if (
    agent.status === "paused" ||
    agent.status === "terminated" ||
    agent.status === "pending_approval"
  ) {
    throw conflict("Agent is not invokable in its current state", { status: agent.status });
  }
```

Every code path that wants to spawn agent work — assignment hooks, comment-mention hooks, blocker-resolved hooks, parent-completion hooks, child completion hooks, the timer, the on-demand API, the routine scheduler — calls **this one function**. There is no other entrypoint.

The function then enters a `db.transaction` that does three things atomically:

1. `SELECT ... FOR UPDATE` on the issue row (if a target issue exists), so no two enqueues race.
2. Look up any active execution run on that issue and decide the outcome:
   - `coalesced` — same agent, same task, just merge the context snapshot into the existing run
   - `deferred_issue_execution` — different agent, hold the wakeup until the current execution finishes
   - `queued` — fresh wakeup, insert `agent_wakeup_requests` row + `heartbeat_runs` row both `queued`
3. Update the wakeup row with the new run id and exit the transaction.

Then `startNextQueuedRunForAgent(agent.id)` is called to actually start the queued run.

### 3.2 Coalescing (same-agent same-task)

Source: `server/src/services/heartbeat.ts:3829`

```ts
if (isSameExecutionAgent && !shouldQueueFollowupForCommentWake) {
  const mergedContextSnapshot = mergeCoalescedContextSnapshot(
    activeExecutionRun.contextSnapshot,
    enrichedContextSnapshot,
  );
  const mergedRun = await tx
    .update(heartbeatRuns)
    .set({
      contextSnapshot: mergedContextSnapshot,
      updatedAt: new Date(),
    })
    .where(eq(heartbeatRuns.id, activeExecutionRun.id))
    .returning()
    .then((rows) => rows[0] ?? activeExecutionRun);

  await tx.insert(agentWakeupRequests).values({
    companyId: agent.companyId,
    agentId,
    source,
    triggerDetail,
    reason: "issue_execution_same_name",
    payload,
    status: "coalesced",
    coalescedCount: 1,
    ...
  });

  return { kind: "coalesced" as const, run: mergedRun };
}
```

If the same agent is already running on the same task, the new wakeup is folded into the existing run. The wakeup request itself is still inserted (with `status: "coalesced"` and `coalescedCount: 1`) so the audit log preserves "this was requested" even though no new run was spawned.

### 3.3 Deferral (different-agent same-task)

```ts
const deferredPayload = {
  ...(payload ?? {}),
  issueId,
  [DEFERRED_WAKE_CONTEXT_KEY]: enrichedContextSnapshot,
};

const existingDeferred = await tx
  .select()
  .from(agentWakeupRequests)
  .where(
    and(
      eq(agentWakeupRequests.companyId, agent.companyId),
      eq(agentWakeupRequests.agentId, agentId),
      eq(agentWakeupRequests.status, "deferred_issue_execution"),
      sql`${agentWakeupRequests.payload} ->> 'issueId' = ${issue.id}`,
    ),
  )
  ...
```

If another agent is currently running on the issue, the new wakeup is parked with `status: "deferred_issue_execution"`. When the current run finishes, paperclip checks for deferred wakeups against that issue and promotes them. This is the "queue behind whoever holds the lock" pattern, done with a status enum instead of an actual lock.

### 3.4 Atomic claim — `claimQueuedRun()`

Source: `server/src/services/heartbeat.ts:2165`

```ts
async function claimQueuedRun(run: typeof heartbeatRuns.$inferSelect) {
  if (run.status !== "queued") return run;
  const agent = await getAgent(run.agentId);
  if (!agent) {
    await cancelRunInternal(run.id, "Cancelled because the agent no longer exists");
    return null;
  }
  if (agent.status === "paused" || agent.status === "terminated" || agent.status === "pending_approval") {
    await cancelRunInternal(run.id, "Cancelled because the agent is not invokable");
    return null;
  }

  ...
  const claimed = await db
    .update(heartbeatRuns)
    .set({
      status: "running",
      startedAt: run.startedAt ?? claimedAt,
      updatedAt: claimedAt,
    })
    .where(and(eq(heartbeatRuns.id, run.id), eq(heartbeatRuns.status, "queued")))
    .returning()
    .then((rows) => rows[0] ?? null);
  if (!claimed) return null;
```

The same `UPDATE WHERE status = "queued"` pattern as issue checkout. If two workers try to claim the same run, one wins and the other gets `null`. No locks.

After claiming, the `executionRunId` is **lazily** stamped onto the issue:

```ts
// Fix A (lazy locking): stamp executionRunId now that the run is actually running,
// not at queue time. Guard is idempotent — safe if called more than once.
const claimedIssueId = readNonEmptyString(parseObject(claimed.contextSnapshot).issueId);
if (claimedIssueId) {
  const claimedAgent = await getAgent(claimed.agentId);
  await db
    .update(issues)
    .set({
      executionRunId: claimed.id,
      executionAgentNameKey: normalizeAgentNameKey(claimedAgent?.name),
      executionLockedAt: claimedAt,
      updatedAt: claimedAt,
    })
    .where(
      and(
        eq(issues.id, claimedIssueId),
        eq(issues.companyId, claimed.companyId),
        or(isNull(issues.executionRunId), eq(issues.executionRunId, claimed.id)),
      ),
    );
}
```

This avoids the common bug where a queued run that never starts holds a lock against newcomers.

### 3.5 Failure recovery — restart sweep

From the spec, `doc/spec/agent-runs.md` §12.4 ("Restart recovery"):

> On server startup:
>
> 1. Find stale `queued`/`running` runs.
> 2. Mark as `failed` with `error_code=control_plane_restart`.
> 3. Set affected non-paused/non-terminated agents to `error` (or `idle` based on policy).
> 4. Emit recovery events to websocket and activity log.

This is implemented as `reapOrphanedRuns` in heartbeat.ts (returned from the service factory). It runs once on boot and never again.

### 3.6 The "tilldone" pattern — adopting a stale checkout

Paperclip does NOT have an explicit "lead takes over from failed worker" tier. Instead, it has **stale-lock adoption**, which is functionally similar. From `server/src/services/issues.ts` around line 1855:

```ts
if (
  checkoutRunId &&
  current.assigneeAgentId === agentId &&
  current.status === "in_progress" &&
  current.checkoutRunId &&
  current.checkoutRunId !== checkoutRunId
) {
  const adopted = await adoptStaleCheckoutRun({
    issueId: id,
    actorAgentId: agentId,
    actorRunId: checkoutRunId,
    expectedCheckoutRunId: current.checkoutRunId,
  });
  if (adopted) {
    const row = await db.select().from(issues).where(eq(issues.id, id)).then((rows) => rows[0] ?? null);
    if (!row) throw notFound("Issue not found");
    const [enriched] = await withIssueLabels(db, [row]);
    return enriched;
  }
}
```

The scenario: agent A's previous heartbeat run crashed mid-task. The issue still has `checkoutRunId = (dead run id)`. When agent A wakes again on heartbeat run B and tries to checkout the same issue with `expectedStatuses: ["in_progress"]`, paperclip notices the same agent owns it, the previous run is no longer alive, and adopts the lock. The agent docs spell this out (`docs/api/issues.md`):

> **Re-claiming after a crashed run:** If your previous run crashed while holding a task in `in_progress`, the new run must include `"in_progress"` in `expectedStatuses` to re-claim it.

This is the closest paperclip has to "tilldone". There is no separate lead-tier worker that picks up after failed ICs. **The same agent retries itself on its next heartbeat**, and the system makes that retry safe via lock adoption. If the agent itself is permanently failing, escalation is on the human board operator (or, in practice, on the CEO agent on its own next heartbeat noticing the stuck issue).

### 3.7 Escalation logic

There is no `escalate()` function. Escalation is **prompted behavior**, encoded in the agent prompt files. From `server/src/onboarding-assets/default/AGENTS.md` (the entire prompt for any non-CEO agent):

```md
You are an agent at Paperclip company.

Keep the work moving until it's done. If you need QA to review it, ask them. If you need your boss to review it, ask them. If someone needs to unblock you, assign them the ticket with a comment asking for what you need. Don't let work just sit here. You must always update your task with a comment.
```

That's the entire IC agent prompt. The escalation rule is "if blocked, reassign the ticket to your boss with a comment". The boss is found via the `agents.reportsTo` column:

```ts
// packages/db/src/schema/agents.ts
reportsTo: uuid("reports_to").references((): AnyPgColumn => agents.id),
```

And surfaced to the agent via:

```ts
// packages/shared/src/types/agent.ts
export interface AgentChainOfCommandEntry {
  id: string;
  name: string;
  role: AgentRole;
  title: string | null;
}

export interface AgentDetail extends Agent {
  chainOfCommand: AgentChainOfCommandEntry[];
  access: AgentAccessState;
}
```

Every heartbeat starts with `GET /api/agents/me` and the response includes `chainOfCommand`, so the agent always knows its boss without having to query.

The CEO agent has its own escalation rule:

```md
- If the board asks you to do something and you're unsure who should own it, default to the CTO for technical work.
- You must always update your task with a comment explaining what you did (e.g., who you delegated to and why).
```

And:

```md
- Never look for unassigned work -- only work on what is assigned to you.
- Never cancel cross-team tasks -- reassign to the relevant manager with a comment.
```

Escalation = "set a different `assigneeAgentId` and write a comment". The DB doesn't enforce hierarchy, the prompts do.

### 3.8 Failed-agent handling

When a heartbeat run fails:

1. The adapter throws or exits non-zero.
2. The run is marked `failed` with the captured error in `heartbeat_runs.error`.
3. The wakeup request is updated to `failed` via `setWakeupStatus(run.wakeupRequestId, "failed", ...)`.
4. `finalizeAgentStatus` is called. If `runningCount === 0` and outcome is failed/timed_out, the agent moves to `error`. If outcome is succeeded/cancelled, it goes to `idle`.

Source: `server/src/services/heartbeat.ts:2243`

```ts
async function finalizeAgentStatus(
  agentId: string,
  outcome: "succeeded" | "failed" | "cancelled" | "timed_out",
) {
  const existing = await getAgent(agentId);
  if (!existing) return;

  if (existing.status === "paused" || existing.status === "terminated") {
    return;
  }

  const isFirstHeartbeat = !existing.lastHeartbeatAt;

  const runningCount = await countRunningRunsForAgent(agentId);
  const nextStatus =
    runningCount > 0
      ? "running"
      : outcome === "succeeded" || outcome === "cancelled"
        ? "idle"
        : "error";
```

An agent in `error` state is **still eligible for new wakeups** — it isn't paused, just flagged. The next heartbeat (timer or assignment) will try again. There is no exponential backoff, no retry counter. Repeated failures are visible in the activity log and the human is expected to intervene.

There is one specific retry path: `processLossRetryCount` on `heartbeat_runs` and `retryOfRunId`, used when the host process is unexpectedly killed (e.g. server restart, OOM). The new run links to the old via `retryOfRunId` and increments `processLossRetryCount`. This is bounded so an infinite OOM loop doesn't spend the budget.

---

## 4. Standups / Sync Patterns

### 4.1 Routines: paperclip's cron-driven coordination

Paperclip has no "all-hands meeting" pattern. The closest analog is **routines** — scheduled, idempotent work assignments to a specific agent. Source: `packages/db/src/schema/routines.ts`

```ts
export const routines = pgTable(
  "routines",
  {
    id: uuid("id").primaryKey().defaultRandom(),
    companyId: uuid("company_id").notNull().references(() => companies.id, { onDelete: "cascade" }),
    projectId: uuid("project_id").notNull().references(() => projects.id, { onDelete: "cascade" }),
    goalId: uuid("goal_id").references(() => goals.id, { onDelete: "set null" }),
    parentIssueId: uuid("parent_issue_id").references(() => issues.id, { onDelete: "set null" }),
    title: text("title").notNull(),
    description: text("description"),
    assigneeAgentId: uuid("assignee_agent_id").notNull().references(() => agents.id),
    priority: text("priority").notNull().default("medium"),
    status: text("status").notNull().default("active"),
    concurrencyPolicy: text("concurrency_policy").notNull().default("coalesce_if_active"),
    catchUpPolicy: text("catch_up_policy").notNull().default("skip_missed"),
    variables: jsonb("variables").$type<RoutineVariable[]>().notNull().default([]),
    ...
    lastTriggeredAt: timestamp("last_triggered_at", { withTimezone: true }),
    lastEnqueuedAt: timestamp("last_enqueued_at", { withTimezone: true }),
    ...
  },
```

A routine has an `assigneeAgentId`, a title/description, variables, and policies. It is paired with one or more triggers:

```ts
export const routineTriggers = pgTable(
  "routine_triggers",
  {
    id: uuid("id").primaryKey().defaultRandom(),
    companyId: uuid("company_id").notNull().references(() => companies.id, { onDelete: "cascade" }),
    routineId: uuid("routine_id").notNull().references(() => routines.id, { onDelete: "cascade" }),
    kind: text("kind").notNull(),                  // "cron" | "webhook"
    label: text("label"),
    enabled: boolean("enabled").notNull().default(true),
    cronExpression: text("cron_expression"),
    timezone: text("timezone"),
    nextRunAt: timestamp("next_run_at", { withTimezone: true }),
    lastFiredAt: timestamp("last_fired_at", { withTimezone: true }),
    publicId: text("public_id"),
    secretId: uuid("secret_id").references(() => companySecrets.id, { onDelete: "set null" }),
    signingMode: text("signing_mode"),
    replayWindowSec: integer("replay_window_sec"),
    ...
  },
```

When a trigger fires (cron or webhook), paperclip writes a `routineRuns` row:

```ts
export const routineRuns = pgTable(
  "routine_runs",
  {
    id: uuid("id").primaryKey().defaultRandom(),
    companyId: uuid("company_id").notNull().references(() => companies.id, { onDelete: "cascade" }),
    routineId: uuid("routine_id").notNull().references(() => routines.id, { onDelete: "cascade" }),
    triggerId: uuid("trigger_id").references(() => routineTriggers.id, { onDelete: "set null" }),
    source: text("source").notNull(),
    status: text("status").notNull().default("received"),
    triggeredAt: timestamp("triggered_at", { withTimezone: true }).notNull().defaultNow(),
    idempotencyKey: text("idempotency_key"),
    triggerPayload: jsonb("trigger_payload").$type<Record<string, unknown>>(),
    linkedIssueId: uuid("linked_issue_id").references(() => issues.id, { onDelete: "set null" }),
    coalescedIntoRunId: uuid("coalesced_into_run_id"),
    failureReason: text("failure_reason"),
    completedAt: timestamp("completed_at", { withTimezone: true }),
    ...
```

…and creates an issue with `originKind: "routine_execution"`. The `linkedIssueId` and `originKind` form a unique index:

```ts
// from issues.ts
openRoutineExecutionIdx: uniqueIndex("issues_open_routine_execution_uq")
  .on(table.companyId, table.originKind, table.originId)
  .where(
    sql`${table.originKind} = 'routine_execution'
      and ${table.originId} is not null
      and ${table.hiddenAt} is null
      and ${table.executionRunId} is not null
      and ${table.status} in ('backlog', 'todo', 'in_progress', 'in_review', 'blocked')`,
  ),
```

This enforces "at most one open issue per routine execution at a time" — i.e., if the routine fires twice and the first issue is still open, the second fire doesn't spawn a duplicate.

**This is paperclip's standup mechanism.** A "Daily standup at 9am" = a routine assigned to the CEO with a `cron_expression: "0 9 * * *"` trigger. When it fires, an issue called "Daily standup" appears in the CEO's inbox, the CEO wakes, reads its reports' status from the issue tracker, and writes a comment summarizing. There is no special "meeting" or "sync" data type. The all-hands is just an issue.

### 4.2 The timer (the closest thing to a global tick)

Source: `server/src/services/heartbeat.ts:4440`

```ts
tickTimers: async (now = new Date()) => {
  const allAgents = await db.select().from(agents);
  let checked = 0;
  let enqueued = 0;
  let skipped = 0;

  for (const agent of allAgents) {
    if (agent.status === "paused" || agent.status === "terminated" || agent.status === "pending_approval") continue;
    const policy = parseHeartbeatPolicy(agent);
    if (!policy.enabled || policy.intervalSec <= 0) continue;

    checked += 1;
    const baseline = new Date(agent.lastHeartbeatAt ?? agent.createdAt).getTime();
    const elapsedMs = now.getTime() - baseline;
    if (elapsedMs < policy.intervalSec * 1000) continue;

    const run = await enqueueWakeup(agent.id, {
      source: "timer",
      triggerDetail: "system",
      reason: "heartbeat_timer",
      requestedByActorType: "system",
      requestedByActorId: "heartbeat_scheduler",
      contextSnapshot: {
        source: "scheduler",
        reason: "interval_elapsed",
        now: now.toISOString(),
      },
    });
    if (run) enqueued += 1;
    else skipped += 1;
  }

  return { checked, enqueued, skipped };
},
```

That is the entire timer-driven scheduler. A worker calls `tickTimers()` on a short interval (every few seconds), it iterates over all active agents, and for each one whose `intervalSec` has elapsed, it enqueues a `timer` wakeup. The interval is **per-agent**, not global. The agent's heartbeat policy lives in `agents.runtimeConfig.heartbeat`:

```json
{
  "heartbeat": {
    "enabled": true,
    "intervalSec": 300,
    "wakeOnAssignment": true,
    "wakeOnOnDemand": true,
    "wakeOnAutomation": true,
    "cooldownSec": 10
  }
}
```

There is no `dailyStandupAt: "09:00"` field. Cron-style scheduling lives in routines, not in agents.

### 4.3 What there is no concept of

Explicitly missing from paperclip:

- No "meeting" or "sync" entity
- No "channel" or "room"
- No "mention everyone" / `@channel` semantics
- No shared whiteboard or live-edit doc (documents are per-issue and revisioned, not collaborative)
- No notification settings, no inbox preferences
- No "office hours" or "available" window for an agent

The model is uncompromisingly **issue-centric**. If you want two agents to meet, you create an issue, assign it to one of them, and have them ping the other.

---

## 5. Cross-Agent Reviews

### 5.1 Execution policy = code review built into the issue

The full mechanism is in `server/src/services/issue-execution-policy.ts`. The high-level pattern:

1. An issue can have an `executionPolicy` with one or more `stages`. Each stage has a `type` (`"review"` or `"approval"`) and a list of `participants` (any mix of agent ids and user ids).
2. When the assignee marks the issue `done`, `applyIssueExecutionPolicyTransition` runs.
3. If there is a pending stage, the issue is moved to `in_review` and reassigned to the stage participant. The original assignee is saved as `returnAssignee`.
4. The reviewer can:
   - Approve via `PATCH ... { status: "done", comment: "..." }` — only valid if commentBody is non-empty. The next stage (if any) receives the issue. If no next stage, the issue is finally `done`.
   - Request changes via `PATCH ... { status: "in_progress", comment: "..." }` — the issue returns to `returnAssignee` with state `changes_requested`.
5. Each decision is persisted in `issue_execution_decisions`, tying actor + outcome + comment + run id.

The state transitions (verbatim from `server/src/services/issue-execution-policy.ts:201`):

```ts
export function applyIssueExecutionPolicyTransition(input: TransitionInput): TransitionResult {
  const patch: Record<string, unknown> = {};
  const existingState = parseIssueExecutionState(input.issue.executionState);
  const currentAssignee = assigneePrincipal(input.issue);
  const actor = actorPrincipal(input.actor);
  const explicitAssignee = assigneePrincipal(input.requestedAssigneePatch);
  const currentStage = input.policy ? findStageById(input.policy, existingState?.currentStageId) : null;
  const requestedStatus = input.requestedStatus;

  if (!input.policy) {
    if (existingState) {
      patch.executionState = null;
      if (input.issue.status === "in_review" && existingState.returnAssignee) {
        patch.status = "in_progress";
        Object.assign(patch, patchForPrincipal(existingState.returnAssignee));
      }
    }
    return { patch };
  }

  ...
  if (currentStage && input.issue.status === "in_review") {
    if (!principalsEqual(existingState?.currentParticipant ?? null, actor)) {
      if (requestedStatus && requestedStatus !== "in_review") {
        throw unprocessable("Only the active reviewer or approver can advance the current execution stage");
      }
      return { patch };
    }

    if (requestedStatus === "done") {
      if (!input.commentBody?.trim()) {
        throw unprocessable("Approving a review or approval stage requires a comment");
      }
      const approvedState = buildCompletedState(existingState, currentStage);
      ...
```

This is a tiny state machine but it gives you Linear-quality multi-stage code review with arbitrary reviewer composition (single reviewer, two reviewers, design + eng, etc.) inside the same `issues` table. No PR system needed.

### 5.2 Citations between agents

There is no formal "agent X cited agent Y's work" relation. Citations are markdown:

```md
- Approval: [ca6ba09d](/approvals/ca6ba09d-b558-4a53-a552-e7ef87e54a1b)
- Pending agent: [CTO draft](/agents/66b3c071-6cb8-4424-b833-9d9b6318de0b)
- Source issue: [PC-142](/issues/244c0c2c-8416-43b6-84c9-ec183c074cc1)
```

(from `docs/guides/agent-developer/comments-and-communication.md`)

The agent prompt instructs: "Use concise markdown with ... Links to related entities when available." The UI parses these links and renders them as rich pills, but there's no schema-level "citation" or "reference" type. The trigram-indexed `body` text makes search across all comments fast enough that informal references are findable.

### 5.3 Approval workflows (separate from review)

There is a separate `approvals` table for **governance** (not code review). Used for things like "CEO requested to hire a new agent → board must approve". From `packages/db/src/schema/approvals.ts` (909 bytes, very small) and `issue_approvals.ts` linking approvals to issues. The agent heartbeat protocol (`docs/guides/agent-developer/heartbeat-protocol.md`) tells agents:

> ### Step 2: Approval Follow-up
>
> If `PAPERCLIP_APPROVAL_ID` is set, handle the approval first:
>
> ```
> GET /api/approvals/{approvalId}
> GET /api/approvals/{approvalId}/issues
> ```
>
> Close linked issues if the approval resolves them, or comment on why they remain open.

Approvals are passed to the agent **via env var** at heartbeat time, so the agent's first action on wake is checking whether it was woken because a board member approved/rejected something it requested.

### 5.4 Cross-agent run linking

The `heartbeat_runs.contextSnapshot` jsonb is the universal "how was this run triggered" record. When the @-mention path fires a wakeup, the snapshot includes:

```ts
contextSnapshot: {
  issueId: id,
  taskId: id,
  commentId: comment.id,
  wakeCommentId: comment.id,
  wakeReason: "issue_comment_mentioned",
  source: "comment.mention",
},
```

So a run on agent B can be traced back to "comment X by agent A on issue Y", and the activity log entry for that comment links back to run X. This forms a directed graph of inter-agent causality without needing a separate "edges" table. The `activity.runsForIssue()` query in `server/src/services/activity.ts:63` reconstructs it:

```ts
runsForIssue: (companyId: string, issueId: string) =>
  db
    .select({...})
    .from(heartbeatRuns)
    .where(
      and(
        eq(heartbeatRuns.companyId, companyId),
        or(
          sql`${heartbeatRuns.contextSnapshot} ->> 'issueId' = ${issueId}`,
          sql`exists (
            select 1
            from ${activityLog}
            where ${activityLog.companyId} = ${companyId}
              and ${activityLog.entityType} = 'issue'
              and ${activityLog.entityId} = ${issueId}
              and ${activityLog.runId} = ${heartbeatRuns.id}
          )`,
        ),
      ),
    )
```

"Show me every heartbeat run that touched this issue" is a single query that joins via either `contextSnapshot` or `activity_log.runId`.

---

## 6. Architecture Decisions Worth Borrowing for Hubify Labs

These are ranked by leverage / "what would most improve our current setup". For each: **what** it is, **where** it lives in source, **why** it matters.

### 6.1 The single `enqueueWakeup()` chokepoint

**What.** Every code path that wants an agent to do work — assignment hooks, comment-mention hooks, blocker-resolved hooks, parent-completion hooks, child-completion hooks, the timer, the on-demand API, the routine scheduler — calls one function.

**Where.** `server/src/services/heartbeat.ts:3613`, function `enqueueWakeup(agentId, opts)`.

**Why.** Coalescing, deferral, budget checks, paused-agent gating, audit logging, and idempotency are all handled in one place. Hubify Labs' current research-pipeline orchestration has many entrypoints (cron jobs, manual scripts, GPU pods, retry loops). Funneling them through one `enqueueExperiment()`-style function would let us add cost guards and dedup once and have it apply everywhere.

### 6.2 DB-backed wakeup queue with explicit status enum

**What.** A `agent_wakeup_requests` table with `status: queued | deferred_issue_execution | claimed | coalesced | skipped | completed | failed | cancelled`. Every request to do work writes a row, regardless of outcome. Coalesced requests still get a row (with `status: coalesced` and `coalescedCount: 1`) so the audit trail is complete.

**Where.** `packages/db/src/schema/agent_wakeup_requests.ts` and `WAKEUP_REQUEST_STATUSES` in `packages/shared/src/constants.ts`.

**Why.** This is the "everything is a row, even the things that didn't happen" pattern. It makes "why didn't agent X run when I expected it to?" a single SELECT against the wakeup-requests table filtered by reason. For Hubify Labs, this maps directly to "every experiment that was queued, even if it was skipped because of QC failure or budget — keep the row, with the reason." We currently lose those events.

### 6.3 Atomic checkout via `UPDATE WHERE`

**What.** `UPDATE issues SET status = 'in_progress', assignee_agent_id = $1, checkout_run_id = $2 WHERE id = $3 AND status IN ($4) AND (assignee_agent_id IS NULL OR ...) AND (execution_run_id IS NULL OR ...)`. Returns 1 row on win, 0 rows on loss. No locks, no Redis.

**Where.** `server/src/services/issues.ts:1786` (the update) and `:1888` (the conflict throw).

**Why.** Hubify Labs has multiple concurrent workers (H200 pod, local scripts, conductors) and we currently rely on tmux session names + manual "is anyone running this" checks. Replacing that with `UPDATE experiments SET status = 'in_progress' WHERE id = ? AND status IN ('queued', 'failed') RETURNING *` and treating an empty result as "someone else got it" would be safer and DB-only.

### 6.4 Two-tier event storage: cheap audit log + expensive blob store

**What.** `activity_log` is one row per mutation, low cardinality, infinite retention. `heartbeat_run_events` is per-run microtimeline, `bigserial` PK, append-only. Full stdout/stderr go to a separate `RunLogStore` (filesystem or S3).

**Where.** `packages/db/src/schema/activity_log.ts`, `packages/db/src/schema/heartbeat_run_events.ts`, and the `RunLogStore` interface in `doc/spec/agent-runs.md` §6.3.

**Why.** Hubify Labs currently dumps everything to log files in the pod and never queries them. Adopting paperclip's split — one cheap table for "who did what, when, on what entity" + one append-only table for "during run X, here's the timeline" + a blob store for raw output — gives us a queryable activity feed for free, without making Postgres the bottleneck.

### 6.5 Single-channel websocket per company with typed events

**What.** One websocket per company. Eight event types. Auto-fallback to polling on disconnect.

**Where.** `LIVE_EVENT_TYPES` in `packages/shared/src/constants.ts`, transport spec in `doc/spec/agent-runs.md` §11.

**Why.** Our research dashboard currently polls. A single `GET /api/research/events/ws` channel that pushes `{type: "experiment.completed", entityId: "..."}` events would let all our pages update live without 30s reload delays.

### 6.6 `@AgentName` regex extraction for triggering wakeups

**What.** The entire @-mention system is one regex (`/\B@([^\s@,!?.]+)/g`), one set, and a join against the `agents` table. Mentions auto-wake the mentioned agent. The agent NEVER wakes itself. Mentions are deduped via a Map keyed by agent id.

**Where.** `server/src/services/issues.ts:2309` (`findMentionedAgents`) and `server/src/routes/issues.ts:1478` (the wakeup loop).

**Why.** This is the lightest-weight, highest-leverage inter-agent communication primitive in the codebase. For Hubify Labs, we could let an experiment script write a comment like `"@cobaya-runner please re-run this with twice the chains"` to a shared issue and have a worker auto-pick it up.

### 6.7 Goal ancestry exposed to every agent on every wake

**What.** Every issue has `parentId`, `goalId`, `projectId`. The Issue type carries `ancestors?: IssueAncestor[]` — the full chain back to the root, plus `project` and `goal` objects. When an agent calls `GET /api/issues/:id`, it gets the entire context for free.

**Where.** `packages/shared/src/types/issue.ts:33` (the `IssueAncestor` interface).

**Why.** Hubify Labs research tasks lose context across sessions. If every experiment record carried `parentExperimentId`, `pipelineId`, `goalId` (e.g. "publish paper 2"), an agent picking up a task could walk the chain and immediately know why the work matters.

### 6.8 Lightweight markdown agent prompts as the routing layer

**What.** Routing rules ("technical → CTO, marketing → CMO") live in a single markdown file (`server/src/onboarding-assets/ceo/AGENTS.md`) loaded fresh on every CEO heartbeat. There is **no router** in code.

**Where.** `server/src/onboarding-assets/ceo/AGENTS.md` (54 lines) and the loader in `server/src/services/default-agent-instructions.ts`.

**Why.** Hubify Labs has growing agent infra and is tempted to build "smart routing" code. Paperclip's bet is that agents are smart enough to follow markdown rules. A markdown file is a lot easier to iterate on than a TypeScript router, especially when the routing rules are themselves judgment calls. We should have a `coordinator-agent.md` instead of a TypeScript scheduler.

### 6.9 Task as the universal coordination primitive

**What.** Standups, reviews, hires, blockers, cross-team handoffs, research pipelines — everything is an `issue` with the same lifecycle, the same comment thread, the same audit trail. There are no parallel data types for "meeting" or "request" or "handoff".

**Where.** Everywhere. The repo has `issues`, `issue_comments`, `issue_attachments`, `issue_documents`, `issue_relations`, `issue_execution_decisions`, `issue_approvals`, `issue_labels`, `issue_inbox_archives`, `issue_read_states`, `issue_work_products`. There is no `meetings` or `requests` table.

**Why.** This is the most counterintuitive and most powerful idea in paperclip. We currently distinguish between "experiment", "pipeline run", "GPU pod task", "paper draft", "wiki edit". Collapsing everything to `task` (with `kind`/`origin_kind` discriminating) would let one Activity feed and one queue manage all of it.

### 6.10 Routines for all scheduled work, not a separate cron file

**What.** Cron-driven automation lives in the database (`routines` + `routine_triggers` + `routine_runs`), not in a Kubernetes cron job or a `crontab`. Each routine fires by creating an issue with `originKind: "routine_execution"`, which is how the rest of the system sees it.

**Where.** `packages/db/src/schema/routines.ts`.

**Why.** Hubify Labs has scattered scheduling: bash crons on the pod, Netlify scheduled functions, GitHub Actions, manual `nohup`. Putting all of it in one DB-backed routines table with a `cron_expression` column and an `assigneeAgentId` would mean the same UI that shows research issues also shows scheduled runs and their failures. The unique-index trick on `originKind = 'routine_execution'` (see §4.1) prevents duplicate-fire bugs for free.

---

## What NOT to Borrow

A few paperclip choices don't fit Hubify Labs and we should explicitly avoid:

1. **The heavy `pnpm` + `Drizzle` + `PGlite` stack.** Paperclip is a control-plane product for end users to deploy. Hubify Labs is a research lab. We don't need embedded Postgres, multi-company isolation, or company-secret-versioning. SQLite or a single Postgres + Convex tables is enough.

2. **The org-chart fixation.** Paperclip models companies with `agents.reportsTo` and `chainOfCommand`. For research, the "chain of command" is "Houston → everything", and over-engineering hierarchy adds friction. Keep the agent table flat.

3. **The execution-policy / multi-stage approval system.** Useful for governance ("CEO must approve hires") but overkill for research where most "approvals" are Houston commenting on a result. Adopt the *idea* of stage-tracked review, but don't import the whole state machine.

4. **The plugin/adapter manager.** Paperclip supports loading external adapters via `~/.paperclip/adapter-plugins.json`. Hubify Labs is much more cohesive — one Anthropic API key, a few tools, one repo. Skip the plugin layer.

5. **The board/agent permission split with JWTs.** Paperclip's `agent_api_keys` (hashed at rest) + bearer-JWT-per-request system is appropriate for a multi-tenant SaaS. For Hubify Labs, a single shared `.env` is fine.

6. **`agent_runtime_state` for resumable session ids per `(agent, taskKey)`.** This is paperclip's resume-Claude-Code-session magic. Hubify Labs research sessions don't need that level of resume — most experiments are fire-and-forget or fully scripted. We can use a simpler "last_session_id per agent" if needed.

7. **The "everything must be a paperclip company" assumption.** Paperclip insists every entity is `companyScoped`. We have one project — don't replicate the company-id-on-every-row pattern.

---

## References

All quoted code and docs are from `https://github.com/paperclipai/paperclip` on branch `master`.

**Schemas (all under `packages/db/src/schema/`):**
- `issues.ts` — https://raw.githubusercontent.com/paperclipai/paperclip/master/packages/db/src/schema/issues.ts
- `agents.ts` — https://raw.githubusercontent.com/paperclipai/paperclip/master/packages/db/src/schema/agents.ts
- `issue_comments.ts` — https://raw.githubusercontent.com/paperclipai/paperclip/master/packages/db/src/schema/issue_comments.ts
- `activity_log.ts` — https://raw.githubusercontent.com/paperclipai/paperclip/master/packages/db/src/schema/activity_log.ts
- `heartbeat_runs.ts` — https://raw.githubusercontent.com/paperclipai/paperclip/master/packages/db/src/schema/heartbeat_runs.ts
- `heartbeat_run_events.ts` — https://raw.githubusercontent.com/paperclipai/paperclip/master/packages/db/src/schema/heartbeat_run_events.ts
- `issue_relations.ts` — https://raw.githubusercontent.com/paperclipai/paperclip/master/packages/db/src/schema/issue_relations.ts
- `issue_execution_decisions.ts` — https://raw.githubusercontent.com/paperclipai/paperclip/master/packages/db/src/schema/issue_execution_decisions.ts
- `agent_wakeup_requests.ts` — https://raw.githubusercontent.com/paperclipai/paperclip/master/packages/db/src/schema/agent_wakeup_requests.ts
- `routines.ts` — https://raw.githubusercontent.com/paperclipai/paperclip/master/packages/db/src/schema/routines.ts

**Shared types and constants (`packages/shared/src/`):**
- `constants.ts` — https://raw.githubusercontent.com/paperclipai/paperclip/master/packages/shared/src/constants.ts
- `types/issue.ts` — https://raw.githubusercontent.com/paperclipai/paperclip/master/packages/shared/src/types/issue.ts
- `types/heartbeat.ts` — https://raw.githubusercontent.com/paperclipai/paperclip/master/packages/shared/src/types/heartbeat.ts
- `types/agent.ts` — https://raw.githubusercontent.com/paperclipai/paperclip/master/packages/shared/src/types/agent.ts
- `types/activity.ts` — https://raw.githubusercontent.com/paperclipai/paperclip/master/packages/shared/src/types/activity.ts
- `validators/issue.ts` — https://raw.githubusercontent.com/paperclipai/paperclip/master/packages/shared/src/validators/issue.ts

**Server services (`server/src/services/`):**
- `heartbeat.ts` — https://raw.githubusercontent.com/paperclipai/paperclip/master/server/src/services/heartbeat.ts (158K, the wakeup coordinator + executor)
- `issues.ts` — https://raw.githubusercontent.com/paperclipai/paperclip/master/server/src/services/issues.ts (88K, includes `checkout`, `findMentionedAgents`)
- `activity.ts` — https://raw.githubusercontent.com/paperclipai/paperclip/master/server/src/services/activity.ts
- `issue-execution-policy.ts` — https://raw.githubusercontent.com/paperclipai/paperclip/master/server/src/services/issue-execution-policy.ts
- `issue-assignment-wakeup.ts` — https://raw.githubusercontent.com/paperclipai/paperclip/master/server/src/services/issue-assignment-wakeup.ts

**Routes:**
- `routes/issues.ts` — https://raw.githubusercontent.com/paperclipai/paperclip/master/server/src/routes/issues.ts (mention loop at 1471, checkout route at 1603)

**Specs and docs:**
- `doc/spec/agent-runs.md` — https://raw.githubusercontent.com/paperclipai/paperclip/master/doc/spec/agent-runs.md (the Agent Runs Subsystem Spec, 756 lines)
- `doc/spec/agents-runtime.md` — https://raw.githubusercontent.com/paperclipai/paperclip/master/doc/spec/agents-runtime.md
- `docs/guides/agent-developer/heartbeat-protocol.md` — https://raw.githubusercontent.com/paperclipai/paperclip/master/docs/guides/agent-developer/heartbeat-protocol.md
- `docs/guides/agent-developer/task-workflow.md` — https://raw.githubusercontent.com/paperclipai/paperclip/master/docs/guides/agent-developer/task-workflow.md
- `docs/guides/agent-developer/comments-and-communication.md` — https://raw.githubusercontent.com/paperclipai/paperclip/master/docs/guides/agent-developer/comments-and-communication.md
- `docs/guides/agent-developer/how-agents-work.md` — https://raw.githubusercontent.com/paperclipai/paperclip/master/docs/guides/agent-developer/how-agents-work.md
- `docs/guides/board-operator/activity-log.md` — https://raw.githubusercontent.com/paperclipai/paperclip/master/docs/guides/board-operator/activity-log.md
- `docs/api/issues.md` — https://raw.githubusercontent.com/paperclipai/paperclip/master/docs/api/issues.md

**Agent prompt assets (`server/src/onboarding-assets/`):**
- `default/AGENTS.md` — https://raw.githubusercontent.com/paperclipai/paperclip/master/server/src/onboarding-assets/default/AGENTS.md
- `ceo/AGENTS.md` — https://raw.githubusercontent.com/paperclipai/paperclip/master/server/src/onboarding-assets/ceo/AGENTS.md
- `ceo/HEARTBEAT.md` — https://raw.githubusercontent.com/paperclipai/paperclip/master/server/src/onboarding-assets/ceo/HEARTBEAT.md
- `ceo/SOUL.md` — https://raw.githubusercontent.com/paperclipai/paperclip/master/server/src/onboarding-assets/ceo/SOUL.md

**Top-level repo files:**
- `README.md` — https://raw.githubusercontent.com/paperclipai/paperclip/master/README.md
- `AGENTS.md` (top-level contributor guide) — https://raw.githubusercontent.com/paperclipai/paperclip/master/AGENTS.md
