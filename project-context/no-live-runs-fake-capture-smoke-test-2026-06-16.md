# No-Live-Runs Fake Capture Smoke Test

**Date:** 2026-06-16  
**Status:** Local fixture/spec only. No Sendblue webhook, iMessage bridge, You.md write, h.computer push, BigBounce repo automation, paper edit, queue mutation, pod action, or external write was performed.

## Goal

Provide a fully local smoke-test fixture for the proposed mobile-capture flow:

`SMS/iMessage/voice note -> You.md raw/normalized capture -> BigBounce proposal artifact -> optional h.computer status card`

This test is intentionally **non-executing**. It exists so future agents can validate schema shape, routing boundaries, and expected outputs before any live transport is wired.

## Fixture File

Machine-readable fixture:

- `project-context/fixtures/research-node/no-live-runs-fake-capture-smoke-test-2026-06-16.json`

The fixture bundles:

1. one raw inbound event
2. one duplicate inbound event
3. one normalized capture session
4. one project route decision
5. one BigBounce proposal artifact
6. one h.computer status event
7. expected assertions

## Smoke-Test Assertions

The fixture is considered valid when a future parser or reviewer confirms:

1. Duplicate detection finds exactly one duplicate raw event.
2. BigBounce is routed as `proposal`, not direct execution.
3. Hubify is explicitly blocked as a current research-status source.
4. The resulting BigBounce output is a `workflow_spec` proposal under `project-context/`.
5. The h.computer card is read-only and does not grant repo or external-write authority.
6. No live actions are listed.

## Recommended Dry-Run Procedure

When future implementation begins, the first smoke test should remain local:

1. Load the fixture JSON.
2. Validate each object against the documented schemas.
3. Confirm dedupe and routing outputs match the `expected_assertions`.
4. Write any parsed output to a temporary or ignored location only.
5. Stop before any webhook registration, API call, MCP write, or repo mutation beyond docs.

## Failure Cases To Catch Early

- duplicate chunks become separate BigBounce tasks
- BigBounce paper/source authority is inferred from raw capture text
- Hubify app/CLI lab state is used as the BigBounce truth source
- h.computer event payload includes implicit action permission
- phone metadata or secrets leak into user-facing summaries

## Why This Exists

Houston's voice-memo workflow needs a realistic local artifact that future agents can test against without:

- sending messages
- spending money
- launching compute
- touching paper files
- mutating queues
- publishing anything externally

This fixture is the smallest safe bridge between the capture schema and later implementation.

## Relationship To Other Docs

- Schema source: `project-context/sms-imessage-youmd-bigbounce-proposal-schema-2026-06-16.md`
- Status-card source: `project-context/h-computer-research-node-status-event-shape-2026-06-16.md`
- Context plan: `project-context/mac-mini-research-node-2026-06-16.md`

## Non-Goals

- This is not a live webhook contract.
- This is not a production You.md import.
- This is not a test runner.
- This is not approval to create external automations.
