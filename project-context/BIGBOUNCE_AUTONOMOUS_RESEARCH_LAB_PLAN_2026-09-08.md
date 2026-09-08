# BigBounce autonomous-research lab plan

**Status:** implementation-ready integration plan; documentation and contracts
only

**Date:** 2026-09-08

**Canonical program authority:** `ops/PLAN.md`

**Machine-readable contract:**
`project-context/BIGBOUNCE_AUTONOMOUS_LAB_CONTRACT_V1.json`

## Goal

Make BigBounce the bounded scientific proof case for Hubify's direction:
**reproducible labs for autonomous research, with human steering**. Automation
may propose, execute, observe, pause, and package a run. It does not own the
scientific question, alter a preregistered run silently, accept a claim, or
publish.

This plan recovers Houston's 2026-09-08 prompt and translates it into one
low-cost pilot. It does not change any paper, readiness score, provider
schedule, compute resource, or public claim.

## Evidence snapshot

Repository evidence and live-provider observations are deliberately separate.
Neither category implies end-to-end acceptance.

### Repository evidence

| Fact | Evidence | Meaning |
|---|---|---|
| Local `main` and `origin/main` began aligned at `e6095704` | `git rev-list --left-right --count origin/main...HEAD` returned `0 0` before this plan | Clean provenance base, not scientific acceptance |
| The manifest corpus has 124 experiment manifests and 3 program manifests | `python3 tools/validate_repro_manifests.py` on 2026-09-08 | Structural validation passed with 0 errors and 12 unregistered-manifest warnings |
| 112 experiment manifests are marked `runnable-now` | Current JSON manifest inventory | Declared source state; not proof that every run succeeds today |
| BigBounce already defines a one-way Hubify import boundary | `project-context/HUBIFY_REPRO_IMPORT_SPEC_2026-08-05.md` | Hubify consumes pinned JSON and never writes science state back |
| Vision, next-science selection, convergence budgets, lineage, drift audits, and reproducibility gates are already governed | `project-context/VISION.md`, `project-context/NEXT_SCIENCE_LEDGER.md`, and `project-context/HUBIFY_RESEARCH_GOVERNANCE_2026-09-02.md` | The autonomous-lab contract extends existing governance; it does not replace it |
| `p2-vertex-check` is an offline, CPU-only, zero-estimated-cost reproducibility target with exact expected rational outputs | `reproducibility/manifests/experiments/p2-vertex-check.json` | Suitable bounded pilot; no pilot was run in this planning task |
| The checked-in Hubify release envelope currently drifts from the site P1B version | Latest `hubify-release-envelope` workflow failure inspected 2026-09-08 | Existing projection defect; unrelated to scientific truth and not fixed here |

Manifest rollups remain authoritative for program budgets. A simple sum across
experiment estimates is not a program budget because manifests can overlap or
be grouped differently.

### Live-provider observations

| Observation on 2026-09-08 | Evidence | Boundary |
|---|---|---|
| No local BigBounce cron entry or loaded `com.bigbounce.*` launch agent was found | `crontab -l`, `launchctl list`, and `~/Library/LaunchAgents` inspection | Local machine only |
| The lab lease is expired | `tools/lab_lease.sh status` | No current writer lease proven |
| GitHub's P1B watchdog schedule is enabled, but its intent is inactive with a `$0.01` hourly and total cap | GitHub workflow list, repository variables, and latest successful watchdog log | The observed run performed `action:none`; this does not prove future runs cannot change |
| RunPod status returned `Pod not found or API error` | `python3 research/runpod_cloud.py status` with local environment loaded | Ambiguous: no active pod was proven, but provider reachability was not proven either |
| Current Hubify lab/agent/cost state could not be verified | `hubify` was absent from `PATH`; a known built CLI failed on a missing dependency | Treat Hubify live state as unknown; do not infer it from repository files |
| Available disk fell below 500 MiB during planning, then recovered above 2 GiB externally | `df -h /` | No task-owned cache existed to remove; execution stays gated on a fresh preflight |

Houston separately authorized pausing legacy Hubify AIOS schedules after an
audit confirms their exact identity and shows they are unrelated to the active
Hubify project. That authorization belongs to the Hubify owning lane. This
BigBounce task did not identify such a schedule, and it did not pause, enable,
or modify any schedule. The active P1B GitHub watchdog is a separate BigBounce
workflow and must not be conflated with the legacy Hubify AIOS schedule.

## Ownership and non-duplication contract

| Surface | Owns | Must not own |
|---|---|---|
| **BigBounce repository** | Scientific question, `VISION.md`, next-science ledger, program/paper lineage, run parameters, code/input/output provenance, QC evidence, results, interpretations, reproducibility manifests, and SSOT readiness | Cross-project identity, generic runtime UI, or reusable platform implementation |
| **AstroStack** | BigBounce-specific execution adapters and methods: Houston Method checkpoints, reproducibility runners, review gates, RunPod lifecycle safety, PDF/site synchronization | BigBounce results or claims; generic Hubify product features; You.md identity |
| **HubStack** | Reusable scientific workflow/governance primitives, learning-loop semantics, import conventions, and platform-facing research contracts | BigBounce-specific facts, paper status, or duplicate AstroStack skills |
| **Hubify** | Persistent lab product, imported run cards, Captain views, run orchestration, and cross-project portfolio projection | Authoritative BigBounce truth or direct writes into BigBounce science state |
| **You.md / You Runtime** | Human identity and preferences; machine/session/goal routing; approval, interrupt, resume, cost, blocker, and checkpoint telemetry | Scientific truth, claim adjudication, paper readiness, or mutation of preregistered parameters |

Rules:

1. BigBounce emits versioned, content-addressed records. Other systems store
   references and projections, not competing scientific records.
2. Hubify imports only a pinned BigBounce commit plus supported schema version.
   Unsupported versions fail closed. Hubify never writes back into BigBounce.
3. You Runtime may observe and steer a run through event references. It may not
   convert runtime telemetry into scientific evidence or change parameters
   without creating a new run revision.
4. AstroStack implements BigBounce-specific execution once. HubStack may
   generalize a proven primitive later, with no copied skill implementation.
5. A public or product projection is downstream. It cannot raise SSOT readiness
   or authorize publication.

## Governed run lifecycle

1. **Select:** bind the proposed work to a ranked next-science ledger item or a
   named reproducibility manifest.
2. **Propose:** create an immutable proposal envelope: source commit, manifest
   hash/version, parameters, expected outputs, verification rule, environment,
   budget, deadline, and allowed side effects.
3. **Preflight:** validate paths/hashes, provider access, free disk, writer
   lease, schedule conflicts, secrets by presence only, and output ownership.
4. **Approve:** record the Captain decision against the exact proposal hash.
5. **Execute:** run only the approved command and allowed provider actions.
6. **Observe:** emit redacted heartbeat events and bounded checkpoints without
   duplicating result data.
7. **Steer:** accept `pause`, `resume`, `stop`, `reprioritize`, or
   `request-explanation`. A parameter-changing instruction forks a new proposal
   and returns to approval.
8. **QC and verify:** evaluate the preregistered rule and capture the exact
   evidence hashes. Tool success is not verification success.
9. **Interpret and connect:** attach the result to the scientific ledger with an
   evidence grade and honest limitations. This remains BigBounce-owned work.
10. **Checkpoint and commit:** persist the run receipt and permitted artifacts
    atomically in BigBounce; record timing, cost, findings, generated tasks, and
    backup locations.
11. **Project:** Hubify and You Runtime ingest the committed receipt by source
    reference. Projection failures do not mutate the source.
12. **Accept:** record four independent booleans:
    `run_succeeded`, `verification_passed`, `claim_accepted`, and
    `captain_accepted`. No earlier state implies a later one.

## Approval and budget policy

### Allowed without a new Houston approval

- Read-only inventory, validation, status, and dry-run commands.
- Offline local CPU reproduction explicitly named in an approved pilot with a
  `$0.00` external-spend cap, no external writes, and task-owned outputs.
- Pause or stop when a safety/budget condition fires.

### Exact-run Captain approval required

- Any paid API, model, cloud compute, storage, or data transfer.
- Any external provider mutation, schedule enable/disable/change, or new data
  egress.
- Any change to a preregistered parameter, expected output, verification rule,
  source commit, or environment after approval.
- Any resume after the deadline or budget envelope expires.

### Explicit Houston approval required

- Scientific claim acceptance, readiness change, paper edit, submission,
  publication, external communication, account/billing change, destructive
  operation, or permanent schedule change.

Every paid-run envelope must include currency, provider, expected charge, hard
maximum, rate assumptions, deadline, permitted actions, stop condition, grace
period, and output-backup gate. Missing or unobservable spend fails closed. The
runner must pause/terminate before exceeding the hard maximum; a forecast or
provider UI estimate is not a receipt.

## Required evidence and checkpoints

Each proposal/receipt/checkpoint carries:

- globally unique run and proposal IDs;
- BigBounce source commit, manifest path/version/hash, code paths, input hashes,
  environment fingerprint, and exact command digest;
- Captain identity, decision, timestamp, proposal hash, and allowed actions;
- machine/session/agent identity and writer lease;
- start/update/end timestamps, current phase, progress denominator, and next
  checkpoint;
- estimated, accrued, and final cost plus provider receipts or `unknown`;
- stdout/stderr and output artifact hashes with redaction status;
- QC result, preregistered verification result, evidence grade, limitations,
  generated tasks, and three backup locations when durable artifacts exist;
- all steer events with actor, timestamp, reason, old/new proposal reference,
  and whether scientific parameters changed;
- the four distinct acceptance booleans above.

You Runtime may render these fields, alert on deadlines/caps, and relay allowed
steering. It must link back to the BigBounce receipt for evidence and display
unknown live-provider state as unknown.

## Low-cost pilot: `bb-pilot-p2-vertex-check-v1`

### Scope

Reproduce the existing `p2-vertex-check` manifest locally, offline, and on CPU.
The expected exact outputs are:

- local: `f_NL = -35/16`
- equilateral: `f_NL = -255/128`

The pilot is intentionally narrow: maximum external spend `$0.00`, maximum
wall time 10 minutes, no paper or SSOT edits, no external provider writes, no
schedule changes, and outputs confined to a task-owned temporary directory plus
one committed redacted receipt.

### Safety gates

- Fresh free disk must be at least 2 GiB before execution and at least 1 GiB
  throughout.
- The worktree must be clean except for the explicitly approved pilot packet.
- The source commit and manifest hash must match the approved proposal.
- No existing writer lease or conflicting run may be active.
- Any failed/unknown gate blocks execution without consuming compute.

This planning task did **not** run the pilot because it was authorized for
documentation/contracts only and experienced a critical-disk warning.

### Pilot sequence

1. Generate and validate the proposal in dry-run mode.
2. Captain approves its exact hash.
3. Execute the manifest command in the task-owned temporary directory.
4. Emit start and phase heartbeats. Exercise one non-mutating steer event:
   `request-explanation`; do not alter parameters.
5. Hash stdout and verify both exact rational outputs.
6. Emit a receipt with `$0.00` spend, QC/verification results, limitations, and
   acceptance booleans.
7. Commit only the redacted proposal/receipt and source-contract updates.
8. Project the pinned receipt into Hubify and You Runtime separately; failure
   of either projection leaves BigBounce evidence intact.

### Objective acceptance

The pilot passes only if all are true:

1. proposal schema validates and its hash is stable across two dry runs;
2. source commit, manifest hash, command, inputs, outputs, and environment are
   present in the receipt;
3. Captain approval binds the exact proposal hash;
4. preflight proves disk, lease, schedule, and output-isolation gates;
5. external spend is exactly `$0.00` and no provider mutation occurs;
6. both exact rational outputs pass the preregistered verifier;
7. the explanation steer event is recorded and parameters remain unchanged;
8. no paper, SSOT readiness, publication state, or schedule changes;
9. BigBounce retains the canonical receipt while Hubify and You Runtime retain
   source references only;
10. a clean checkout can reproduce the same verifier result from the committed
    packet.

## Implementation lanes

### Lane 0 — contract closure (this change)

- Record the recovered prompt, plan, and machine-readable v1 contract.
- Link the work from the canonical plan and You.md recovery surface.
- Do not imply live-provider acceptance.

### Lane 1 — BigBounce/AstroStack runner

- Add a stdlib-only runner that reads an existing manifest, generates a stable
  proposal, performs preflight/dry-run, executes only after a matching approval,
  and emits a redacted receipt.
- Add unit tests for hash stability, approval mismatch, disk/lease/budget fail
  closure, parameter-change revisioning, and the P2 exact-output verifier.
- Keep BigBounce science in this repository; place reusable BigBounce-specific
  execution mechanics in AstroStack using the shared skill-governance process.

Proposed BigBounce paths:

- `tools/autonomous_lab_run.py`
- `tools/tests/test_autonomous_lab_run.py`
- `project-context/autonomous-lab/pilots/p2-vertex-check.v1.json`
- `project-context/autonomous-lab/receipts/` for committed redacted receipts

### Lane 2 — You Runtime steering adapter

- Read proposal/checkpoint/receipt events by immutable source reference.
- Implement approval, pause/resume/stop, request-explanation, cost alerts, and
  unknown-state display.
- Reject parameter-changing steer events unless they reference a newly approved
  proposal revision.

### Lane 3 — Hubify projection

- Extend the existing one-way version-gated importer for proposal/receipt run
  cards.
- Show evidence links, budget state, Captain decision, limitations, and the four
  independent acceptance booleans.
- Never provide a write-back path into BigBounce.

### Lane 4 — acceptance and generalization

- Run the pilot only after disk/runtime gates are healthy.
- Reproduce from a clean checkout, verify the two projections, and truth-audit
  the evidence packet.
- Generalize only proven reusable mechanics into HubStack; retain BigBounce
  specialization in AstroStack.

## Verification commands for the implementation packet

```bash
python3 tools/validate_repro_manifests.py
python3 -m unittest tools.tests.test_autonomous_lab_run -v
python3 tools/autonomous_lab_run.py propose \
  --manifest reproducibility/manifests/experiments/p2-vertex-check.json \
  --dry-run
git diff --check
```

The actual pilot command is intentionally omitted until the implementation
creates a validated proposal, obtains Captain approval, and rechecks the runtime
gates.

## Terminal criteria for this initiative

This initiative is complete only when the bounded pilot meets all ten acceptance
conditions, BigBounce holds the canonical receipt, Hubify and You Runtime render
the pinned projection without write-back, AstroStack and HubStack contain no
duplicated capability, budget/steer failure tests pass, and no scientific claim
or readiness state has changed without Houston's explicit approval.
