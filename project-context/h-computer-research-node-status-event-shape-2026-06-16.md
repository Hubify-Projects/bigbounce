# h.computer Research-Node Status Event Shape

**Date:** 2026-06-16  
**Status:** Drafted for docs-only Mac mini research-node setup. No live h.computer push, MCP write, webhook, BigBounce paper file, SSOT row, pod, or external system was changed.

## Purpose

Define the approved event shape that BigBounce-adjacent research-node work may emit for **read-only owner-facing status cards** in h.computer.

This event shape is intentionally narrow:

- It may summarize approved BigBounce status context.
- It may link to local BigBounce source files or public BigBounce site surfaces.
- It must not become a second science source of truth.
- It must not trigger live actions by itself.

Canonical BigBounce truth remains:

1. `project-context/SSOT/`
2. canonical source/artifact files in the local `bigbounce` repo
3. `https://bigbounce.hubify.app` as the public mirror

Hubify app/CLI lab data remains excluded from current BigBounce research-status inference.

## Design Rules

1. **Read-only by default.** h.computer may render cards, badges, and timelines from these events, but not infer permission to mutate BigBounce.
2. **Approved input only.** The event may only be emitted from a reviewed BigBounce context artifact, SSOT state, or public-site QA observation.
3. **Human-legible provenance.** Every event must say what source it came from.
4. **No hidden authority transfer.** Receiving an event does not authorize paper edits, queue mutations, pod actions, or Hubify writes.
5. **No stale Hubify mirroring.** Event producers must not populate BigBounce status fields from Hubify app/CLI lab rows.

## Event Kinds

Recommended initial event kinds:

- `context_checkpoint` — a docs-only milestone such as inventory/spec completion
- `proposal_ready` — a new BigBounce proposal artifact is ready for Houston review
- `proposal_blocked` — a proposal is blocked on approval, missing context, or a boundary rule
- `status_mirror_check` — repo SSOT and public site were compared and summarized
- `runtime_boundary_notice` — a runner or tool is explicitly not approved for BigBounce authority

Do not introduce action-oriented kinds such as `launch_pod`, `publish_site`, or `edit_paper` in this event stream.

## Canonical Schema

```json
{
  "schema": "bigbounce.research_node.status_event.v1",
  "event_id": "bb_status_2026-06-16T18-40-00Z_context_checkpoint",
  "created_at": "2026-06-16T18:40:00Z",
  "producer": {
    "system": "bigbounce",
    "surface": "project-context",
    "actor": "local_agent",
    "mode": "docs_only"
  },
  "kind": "context_checkpoint",
  "title": "Research-node docs lane completed",
  "summary": "Approved docs now cover source-of-truth boundaries, runner inventory, MCP boundaries, capture proposal schema, h.computer status events, a no-live-runs smoke-test fixture, and the review-method protocol draft.",
  "priority": "normal",
  "project": "bigbounce",
  "source_of_truth": {
    "contract_ref": "project-context/bigbounce-source-of-truth-contract-2026-06-16.md",
    "source_tier": "project-context",
    "source_refs": [
      "project-context/FINAL_TASK_LISTS.md",
      "project-context/mac-mini-research-node-2026-06-16.md"
    ],
    "public_mirror_refs": [
      "https://bigbounce.hubify.app"
    ]
  },
  "status_payload": {
    "scope": "research_node_setup",
    "state": "complete",
    "details": [
      "No live runs started",
      "No paper or SSOT readiness state changed",
      "h.computer is display-only for this lane"
    ]
  },
  "approval": {
    "event_reviewed": true,
    "review_basis": "local docs review",
    "allows_external_write": false,
    "allows_repo_mutation": false
  },
  "ui_hints": {
    "card_style": "checkpoint",
    "badge": "Docs Only",
    "expand_refs_by_default": true
  }
}
```

## Required Fields

| Field | Meaning | Rule |
|---|---|---|
| `schema` | Versioned event contract | Must remain explicit and stable. |
| `event_id` | Unique event identity | Should encode timestamp and kind. |
| `created_at` | Emission timestamp | UTC ISO 8601. |
| `producer` | Where this came from | Must identify system, surface, actor, and mode. |
| `kind` | Event class | Must be one of the approved kinds above. |
| `title` / `summary` | Human-readable owner feed text | Must be concise and non-hypey. |
| `source_of_truth` | Provenance bundle | Must name the contract and source refs. |
| `status_payload` | Renderable card body | Keep focused on state, not speculation. |
| `approval` | Authority boundary | Defaults must be non-mutating. |

## Optional Fields

Use only when helpful:

- `paper_refs` — exact paper IDs when a card concerns one paper
- `queue_refs` — queue rows or task IDs
- `site_check` — public mirror status such as `http_status: 200`
- `blocked_by` — explicit blocker list
- `expires_at` — when a temporary status should be hidden or refreshed

## Prohibited Fields

Do not include:

- raw phone numbers
- API keys, bearer tokens, webhook secrets, or env values
- paper-claim deltas not grounded in SSOT or source files
- action instructions that look like implicit approval
- Hubify lab-derived status summaries presented as BigBounce truth

## Emission Gate

An h.computer status event may be proposed when all are true:

1. The underlying information already exists in BigBounce-local context, SSOT, or the public site.
2. The summary can be expressed without mutating research state.
3. The event explicitly says whether it is docs-only, proposal-only, or a mirror check.
4. The event does not bypass BigBounce approval gates.

## Example Event Types

### 1. Context checkpoint

Use when a docs-only setup slice is complete.

### 2. Proposal ready

Use when a normalized capture session has already been routed to a BigBounce proposal artifact and the next step is Houston review.

### 3. Runtime boundary notice

Use when a tool such as Pi, Hermes, or OpenClaw is discovered to be unavailable or unapproved, so Houston can see the constraint in h.computer without that tool gaining authority.

## Relationship To You.md

You.md remains the right system for:

- raw capture storage
- dedupe
- idea segmentation
- project routing
- proposal state
- audit logs

h.computer should consume only the summarized status event, not the full raw transcript.

## First Local Fixture Pairing

The no-live-runs fixture at `project-context/fixtures/research-node/no-live-runs-fake-capture-smoke-test-2026-06-16.json` includes a sample `h_computer_status_event` object compatible with this schema.

## Non-Goals

- This spec does not authorize live h.computer API calls.
- This spec does not define a bidirectional control channel from h.computer into BigBounce.
- This spec does not change paper status, SSOT readiness, or site data.
