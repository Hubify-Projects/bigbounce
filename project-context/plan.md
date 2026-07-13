# Plan — Phase 0 handoff acceptance

## Goal

Validate the pushed `ops/handoff/` package as a reproducible two-machine, one-lab MVP. Keep the live research loop safe and defer independent multi-lab architecture until the MVP is boring-reliable and Houston explicitly advances the phase.

## Execution order

1. Preserve live ownership: do not touch the M41 browser/manifest, claim the lease, or mutate shared research state during its active run.
2. On the receiving machine, follow `BOOTSTRAP_PROMPT.md`; restore prerequisites and secret key names safely; rerun `bootstrap.sh` until `READY` or every remaining gap is documented.
3. Resolve the shared-stack sync conflict before running `/machine-sync`; authenticate Hubify before treating Hubify status as verified.
4. During an explicit idle/handoff window, test lease denial/claim/renew/release/expiry plus heartbeat `machineId` and two-machine git/Convex convergence.
5. Start a fresh Codex session from repository instructions and verify it can resume the runbook without hidden Claude context.
6. Record acceptance evidence and ask Houston for Phase 0 sign-off.

## Gates

- **Now — Phase 0:** two machines, one lab. This is the only active phase.
- **Pending — Phase 1:** Codex as a second orchestrator in the same lab; requires Phase 0 green and Houston approval.
- **Pending — Phase 2:** two independent labs on the bounded P4 mirror-flip reproduction with blind seal/reveal and corroboration; requires Phase 1 green plus tested `exchange/`, `labId`, and site support.
- **Pending — Phase 3:** open-source Lab C; requires one successful two-lab blind/reveal/corroboration cycle.

## Recovery notes

- Last prompt-history reconciliation: 2026-07-13 13:57 PT.
- Source reviewed: current 2026-07-13 handoff prompt/Claude report plus Codex repository-state acceptance audit.
- Verified baseline: `main` and `origin/main` at `df8d89a3`; handoff commits reachable and pushed; lease free; heartbeat carries `machineId`.
- Active blockers: M41 browser/manifest ownership, unauthenticated Hubify CLI, dirty/conflicted machine-sync shared repo.
