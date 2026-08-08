# SMS/iMessage -> You.md -> BigBounce Proposal Schema

**Date:** 2026-06-16
**Status:** Spec only. No Sendblue account, webhook, You.md API route, BigBounce paper file, pod, queue row, h.computer feed item, Notion page, or external write was changed.
**Source:** Houston's 2026-06-16 Part 2 Apple Watch/iMessage brain dump and the Mac mini research-node plan.

## Goal

Capture long Apple Watch, iMessage, SMS, voice-dictation, run, drive, and late-night thought streams without losing ideas, while keeping BigBounce protected from accidental paper edits, stale Hubify state, or live compute actions.

The system should turn noisy mobile notes into:

1. A raw immutable transcript artifact.
2. A deduped normalized transcript.
3. Project-routed idea/task proposals.
4. BigBounce-specific research-node proposals that require approval before any repo write, paper edit, queue mutation, pod launch, or external write.

## Ownership Boundary

| Layer | Owner | Responsibility |
|---|---|---|
| Capture transport | Sendblue/iMessage/SMS bridge | Receive message chunks and webhook metadata. |
| Raw memory and routing | You.md | Store raw transcript, dedupe repeated messages, segment ideas, classify projects, preserve provenance, create proposals, and keep audit logs. |
| BigBounce intake | BigBounce project context | Accept approved proposals as markdown/context artifacts only until a human or authorized agent explicitly promotes them. |
| Owner-facing display | h.computer | Show approved research-node status cards or pending proposal summaries. |
| Science truth | BigBounce repo + `bigbounce.hubify.app` | Remain canonical for current paper/research status. |
| Excluded by default | Hubify app/CLI lab state | Do not infer BigBounce research status from Hubify until an explicit refresh/sync is designed and verified. |

## Session Model

A capture session groups many short watch/SMS chunks into one coherent artifact.

Suggested session triggers:

- Explicit starts: `Workout transcript`, `BigBounce note`, `Research run`, `Idea dump`, `Drive notes`.
- Implicit starts: burst of messages from the same sender within a configurable window, such as 90 minutes.
- Explicit ends: `done`, `end workout`, `end transcript`, `save this`, `route this`.
- Implicit ends: no new chunk for a configurable idle window, such as 20 minutes for active workouts or 60 minutes for late-night notes.

Duplicate handling is required because Apple Watch/iMessage voice dictation can produce repeated messages. Dedupe should preserve the raw originals, then mark duplicates in the normalized layer instead of deleting evidence.

## Raw Capture Event

Each inbound chunk should be stored before interpretation.

```json
{
  "schema": "bigbounce.mobile_capture.raw_event.v1",
  "event_id": "raw_2026-06-16T08-20-31Z_0001",
  "received_at": "2026-06-16T08:20:31Z",
  "transport": "sendblue",
  "channel": "imessage",
  "sender": {
    "label": "Houston",
    "phone_hash": "sha256:...",
    "device_hint": "apple_watch_ultra"
  },
  "session_hint": "workout_transcript",
  "text_raw": "OK remember to add send blue.com API...",
  "attachments": [],
  "provider_metadata": {
    "message_id": "provider-message-id",
    "thread_id": "provider-thread-id"
  },
  "privacy": {
    "contains_secret": false,
    "contains_health_data": true,
    "contains_paper_claim": false
  }
}
```

Raw event rules:

- Store exactly what arrived, including transcription errors.
- Never put raw phone numbers, API keys, or bearer tokens into project docs.
- Preserve provider message IDs for dedupe and audit.
- Treat health/fitness context as private by default.

## Normalized Session Artifact

You.md should compile raw chunks into a normalized session before routing.

```json
{
  "schema": "youmd.capture_session.v1",
  "session_id": "cap_2026-06-16_run_001",
  "title": "Run notes: BigBounce, You.md, h.computer, Fantasy.is",
  "started_at": "2026-06-16T07:20:00Z",
  "ended_at": "2026-06-16T09:00:00Z",
  "source": {
    "transport": "sendblue",
    "channel": "imessage",
    "device_hint": "apple_watch_ultra"
  },
  "raw_event_ids": ["raw_2026-06-16T08-20-31Z_0001"],
  "dedupe": {
    "strategy": "exact_and_near_duplicate",
    "duplicates_found": 1,
    "duplicate_event_ids": ["raw_2026-06-16T08-20-42Z_0002"]
  },
  "transcript_raw_ref": "youmd://raw/cap_2026-06-16_run_001.md",
  "transcript_normalized": "Remember to add Sendblue API capture so Apple Watch messages can become agent-routed notes...",
  "idea_segments": [
    {
      "segment_id": "seg_001",
      "summary": "Use Apple Watch iMessage/SMS as the easiest mobile capture path for agents.",
      "project_hints": ["youmd", "bigbounce", "badapp", "myo", "h-computer"],
      "confidence": 0.82,
      "source_event_ids": ["raw_2026-06-16T08-20-31Z_0001"]
    }
  ]
}
```

## Project Routing Record

Routing is classification, not execution.

```json
{
  "schema": "youmd.project_route.v1",
  "route_id": "route_cap_2026-06-16_run_001_bigbounce",
  "session_id": "cap_2026-06-16_run_001",
  "project": "bigbounce",
  "decision": "proposal",
  "confidence": 0.74,
  "reason": "Mentions Mac mini research node, BigBounce research status, multi-model review, and h.computer status cards.",
  "excluded_projects": [
    {
      "project": "hubify",
      "reason": "Hubify app research data is stale for current BigBounce state unless explicitly refreshed."
    }
  ],
  "requires_human_review": true,
  "allowed_next_artifacts": ["project-context proposal markdown", "task-list status note"],
  "blocked_next_actions": ["paper edit", "pod launch", "queue mutation", "Hubify lab write", "external publish"]
}
```

## BigBounce Proposal Artifact

BigBounce should receive proposals as markdown or structured JSON committed to project context, not direct paper changes.

```json
{
  "schema": "bigbounce.research_node.proposal.v1",
  "proposal_id": "bb_prop_2026-06-16_001",
  "created_at": "2026-06-16T09:05:00Z",
  "source_session_id": "cap_2026-06-16_run_001",
  "title": "Define Sendblue/iMessage capture for BigBounce research-node notes",
  "kind": "workflow_spec",
  "priority": "medium",
  "status": "proposed",
  "summary": "Use You.md to capture and dedupe Apple Watch/iMessage transcripts, then route BigBounce-relevant segments into approval-gated project-context proposals.",
  "proposed_changes": [
    {
      "target": "project-context",
      "action": "add_or_update_markdown",
      "path": "project-context/sms-imessage-youmd-bigbounce-proposal-schema-2026-06-16.md"
    }
  ],
  "science_impact": "none",
  "requires_truth_audit": false,
  "requires_latex_audit": false,
  "requires_queue_check": false,
  "requires_houston_approval": true,
  "blocked_actions": [
    "edit paper .tex",
    "change SSOT readiness",
    "launch RunPod",
    "write Hubify lab data",
    "publish to h.computer without approval"
  ],
  "promotion_checklist": [
    "Human or authorized agent reviews normalized transcript.",
    "Proposal is confirmed as BigBounce-relevant.",
    "No paper claim is strengthened without truth-audit.",
    "Any eventual paper edit follows SSOT, queue, compile, and latex-audit protocols."
  ]
}
```

## Classification Rules

Route to BigBounce when a segment mentions:

- BigBounce papers, cosmology, bounce research, paper readiness, arXiv, R-rounds, truth-audits, SSOT, RunPod, pods, reviewer loops, or `bigbounce.hubify.app`.
- Mac mini research-node setup for BigBounce.
- Multi-model/multi-UI review methodology derived from the BigBounce campaign.

Do not route directly to BigBounce when a segment is primarily about:

- Creator.new, BAMF.ai, BAMFOS, BAMF agency/admin, Fantasy.is, BadApp fitness product, Myo/Mayo health product, or personal brand h.computer site work.
- Generic You.md identity/memory improvements unless the segment includes an explicit BigBounce research-node use case.
- Hubify app research state without direct BigBounce repo or `bigbounce.hubify.app` grounding.

Ambiguous segments should become `needs_review` proposals in You.md, not BigBounce tasks.

## Approval Gates

| Action | Default gate |
|---|---|
| Save raw transcript in You.md | Allowed if user-owned channel and secrets are redacted from summaries. |
| Create normalized route/proposal | Allowed. |
| Add BigBounce project-context proposal markdown | Allowed after local agent review; commit as docs-only. |
| Update `FINAL_TASK_LISTS.md` context row | Allowed if status-only and no paper readiness changes are implied. |
| Edit paper `.tex`, figures, references, or tarballs | Requires BigBounce paper protocol, SSOT check, compile, and LaTeX audit. |
| Change paper readiness/status | Requires SSOT and truth-audit discipline. |
| Launch pods or expensive compute | Requires explicit approval or existing authorized queue row. |
| Publish h.computer status | Requires approved BigBounce status event. |
| Write to Hubify lab/app | Blocked until Hubify refresh/sync plan is explicitly approved. |
| Send to Notion, Slack, GitHub, CRM, or project boards | Requires explicit external-write approval unless a bounded automation rule already exists. |

## Minimal Dry-Run Fixture

Use this for a no-live-runs test before any Sendblue webhook exists:

```json
{
  "schema": "youmd.capture_session.fixture.v1",
  "session_id": "fixture_2026-06-16_bigbounce_sms",
  "chunks": [
    "Workout transcript: remember the Mac mini research node should route BigBounce notes through You.md first.",
    "Workout transcript: remember the Mac mini research node should route BigBounce notes through You.md first.",
    "Also h.computer can show status cards, but do not use stale Hubify app data for BigBounce."
  ],
  "expected": {
    "duplicates_found": 1,
    "routes": ["bigbounce", "youmd", "h-computer"],
    "blocked_routes": ["hubify_current_research_status"],
    "bigbounce_artifact_type": "proposal",
    "live_actions": []
  }
}
```

## Implementation Notes For Future Agents

- Prefer You.md as the durable capture and routing layer. BigBounce should not own the mobile webhook.
- Preserve raw transcripts even when normalized summaries are cleaner.
- Store raw and normalized artifacts separately so future agents can re-parse them as project boundaries become clearer.
- Keep phone numbers and provider secrets out of repo docs.
- Mark all generated BigBounce outputs as proposals until promoted by an approved workflow.
- Use `bigbounce.hubify.app` and the local repo for current BigBounce state; do not backfill from stale Hubify app data.
