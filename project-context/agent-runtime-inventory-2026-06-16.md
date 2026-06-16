# Agent Runtime Inventory

**Date:** 2026-06-16
**Scope:** Mac mini research-node preparation for BigBounce-adjacent automation.
**Status:** Read-only inventory. No agents were launched, no packages were installed, no BigBounce paper/pod/queue authority was granted.

## Summary

Only Claude Code, Codex, and Hubify are runnable from the current shell. OpenClaw, Hermes, and Pi have local configuration or methodology artifacts, but no global executable was found in `PATH`.

This means OpenClaw, Hermes, and Pi are not approved BigBounce runners yet. They may be studied or dry-run on isolated toy tasks later, but they must not touch BigBounce paper sources, SSOT rows, pod commands, arXiv artifacts, or public-site research state until an explicit adapter and approval gate exists.

## Command Inventory

| Command | Current result | Safe interpretation |
|---|---|---|
| `claude` | `/opt/homebrew/bin/claude` | Installed. May remain a primary high-judgment local runner under existing BigBounce rules. |
| `codex` | `/Users/houstongolden/.nvm/versions/node/v22.20.0/bin/codex` | Installed. Good for scoped docs/code execution with repo guardrails. |
| `hubify` | `/Users/houstongolden/.nvm/versions/node/v22.20.0/bin/hubify` | Installed and auth restored, but Hubify app lab data is not current BigBounce research truth. |
| `openclaw` | Not found | Not runnable from this shell. Do not assign BigBounce work. |
| `hermes` | Not found | Not runnable from this shell. Do not assign BigBounce work. |
| `pi` | Not found | Not runnable from this shell. Existing `.pi` configs are not enough to execute work. |

Global package scan found `@openai/codex@0.130.0`; it did not show global OpenClaw, Hermes, or Pi packages.

## Local Evidence

### OpenClaw

Found gstack/OpenClaw artifacts:

- `/Users/houstongolden/.claude/skills/gstack/openclaw/`
- `/Users/houstongolden/.claude/skills/gstack/.openclaw/`
- `/Users/houstongolden/.agents/skills/gstack/openclaw/`
- `/Users/houstongolden/.agents/skills/gstack/.openclaw/`
- `/Users/houstongolden/gbrain/openclaw.plugin.json`
- `/Users/houstongolden/gbrain/test/e2e/bench-vs-openclaw/`

Key finding: gstack treats OpenClaw as a host with generated methodology artifacts. The gstack setup script says OpenClaw integration uses a different model where OpenClaw spawns Claude Code sessions natively via ACP; gstack provides methodology artifacts, not a full skill installation. The host config expects CLI command `openclaw`, but no such executable is currently available.

Safe next step: locate or install the actual OpenClaw CLI outside BigBounce, then run a toy read-only task in a scratch repo. Do not run OpenClaw against BigBounce until the executable, logs, permissions, and rollback model are documented.

### Hermes

Found gstack/Hermes artifacts:

- `/Users/houstongolden/.claude/skills/gstack/.hermes/`
- `/Users/houstongolden/.claude/skills/gstack/hosts/hermes.ts`

Key finding: gstack has a Hermes host adapter that rewrites tool names for Hermes (`terminal`, `read_file`, `patch`, `delegate_task`) and points generated skills at `.hermes/skills/gstack`. The host config expects CLI command `hermes`, but no such executable is currently available.

Safe next step: locate the Hermes Agent repo/package and verify its command path on a scratch task only. Do not give Hermes BigBounce paper, pod, queue, or publication authority.

### Pi

Found `.pi` directories:

- `/Users/houstongolden/.pi`
- `/Users/houstongolden/Desktop/CODE_2025/bamfaiapp/.pi`
- `/Users/houstongolden/Desktop/CODE_2025/bamfaiapp-next/.pi`
- `/Users/houstongolden/Desktop/CODE_2025/ceo-agents/.pi`
- `/Users/houstongolden/Desktop/CODE_2025/hubify/.pi`
- `/Users/houstongolden/Desktop/CODE_2025/lead-agents/.pi`
- `/Users/houstongolden/Desktop/CODE_2025/ui-agents/.pi`

Sample config families seen by filename/key names only:

- `hubify/.pi/hubify-labs/config.yaml` and `start.sh`
- `ceo-agents/.pi/ceo-agents/ceo-and-board-configuration*.yaml`
- `lead-agents/.pi/multi-team/*config.yaml`
- `ui-agents/.pi/settings.json`

Key finding: Pi-style project/team configurations exist in sibling repos, especially Hubify and agent-team experiments, but the `pi` command is not globally available from this shell.

Safe next step: treat Pi as an orchestration/design reference until its runtime command is found. If tested, use an isolated toy prompt and a scratch working directory. Do not run Pi in BigBounce.

## BigBounce Authority Boundary

These runtimes are not authorized to:

- edit `arxiv/`, `pipelines/**` paper sources, generated PDFs, tarballs, or site paper artifacts;
- mutate `project-context/SSOT/**` except through the existing BigBounce SSOT protocol;
- launch, stop, or inspect paid compute/pods outside the existing RunPod/queue rules;
- update `bigbounce.hubify.app`, GitHub, arXiv, Hubify app data, Slack, Notion, or other external systems;
- infer research status from Hubify app/CLI lab rows.

They may be used later only after a bounded adapter is written that specifies:

1. exact executable path and version;
2. allowed working directory;
3. allowed file globs;
4. denied file globs;
5. logging/audit output;
6. timeout and stop behavior;
7. human approval gate for any external write or expensive compute;
8. toy-task smoke test result.

## Recommended Next Step

Do not install or run these agents inside BigBounce yet. The next useful research-node implementation slice is the SMS/iMessage capture proposal schema, because it can be designed as a local, no-live-runs artifact that routes to BigBounce SSOT proposals without granting runtime authority.
