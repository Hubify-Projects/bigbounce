# Tasks

## Active

- [ ] Reconcile the divergent local and `origin/main` histories before publishing this checkpoint. Do not force-push, reset, rebase, or discard the local context commits. (observed: 2026-08-05 18:00 PT)
- [ ] Run the final independent confirmation spot-check for Paper 1B before raising its 98% readiness; preserve the current honesty language and SSOT evidence trail. (source: `project-context/SSOT/index.md`, EXT19 status)

## Done

- [x] Captured the cross-machine handoff request, migrated the legacy prompt log to `prompts.md`, and created a resumable main-branch context checkpoint. (source: 2026-08-05 17:45 PT)

## Watchpoints

- Read `project-context/SSOT/index.md`, the relevant per-paper status file, and `project-context/SSOT/queue.md` before touching paper work.
- Do not claim a PDF, scientific, or site validation that was not actually run during the resumed work.
- Local environment backup files contain secrets and remain outside Git; use the encrypted environment-vault workflow to restore them on another machine.
- At the handoff fetch, `origin/main...HEAD` was 1,574 commits behind / 2 local commits ahead. A normal fast-forward merge was correctly refused.
