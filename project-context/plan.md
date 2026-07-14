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

## Active CMUX dogfood track

This parallel evaluation track does not advance the Phase 0 handoff gates or authorize BigBounce writes.

1. **Done:** harden the local subscription-first mirrored launcher in `learning-cmux-with-agents` with project-trust bypass, atomic one-way seal/reveal, transactional four-workspace topology gating and scoped rollback, deadline/timeout adjudication, and 19 passing tests.
2. **Inconclusive evidence only:** the first diagnostic run did not establish a valid model comparison.
3. **Latest clean attempt:** run `20260714T000136Z-024658000-bfee86cfcc83` launched from a clean snapshot, verified the complete topology, and bypassed every Codex trust gate. Codex submitted one sealed result; Claude reached its weekly subscription limit before submitting. No result was revealed and no winner exists. This legacy run predates deadline-aware contracts and has no deadline, so it cannot be retroactively expired.
4. **Now:** wait for the Claude allowance reset at **2026-07-15 07:00 America/Los_Angeles**, then start a fresh clean envelope and run both GPT-5.6 Sol high and Claude Opus 4.8 high arms from the same bound snapshot.
5. Capture both fresh sealed outputs, reveal only after dual submission, and compare quality, latency, and coordination behavior using the recorded run artifacts.
6. Keep all mutation disabled until You.md atomic claims, heartbeats, overlap detection, and isolated worktrees are implemented and acceptance-tested.
7. Keep the lab commits local until a Houston-owned fork is configured; the current `origin` is IndyDevDan's upstream repository.

## Gates

- **Now — Phase 0:** two machines, one lab. This is the only active phase.
- **Pending — Phase 1:** Codex as a second orchestrator in the same lab; requires Phase 0 green and Houston approval.
- **Pending — Phase 2:** two independent labs on the bounded P4 mirror-flip reproduction with blind seal/reveal and corroboration; requires Phase 1 green plus tested `exchange/`, `labId`, and site support.
- **Pending — Phase 3:** open-source Lab C; requires one successful two-lab blind/reveal/corroboration cycle.

## Recovery notes

- Last prompt-history reconciliation: 2026-07-13 16:15 PT.
- Source reviewed: 2026-07-13 handoff prompt/Claude report, Codex repository-state acceptance audit, and CMUX prompts at 14:49, 15:38, 15:56, and 16:14 PT.
- Verified baseline: `main` and `origin/main` at `b93528b6`; handoff commits remain reachable and pushed. Lease/heartbeat evidence is retained from the earlier acceptance audit.
- Active blockers: M41 browser/manifest ownership, unauthenticated Hubify CLI, dirty/conflicted machine-sync shared repo.
- CMUX boundary: launcher hardening is locally green at 19 tests; the first diagnostic was inconclusive and the clean rerun has only an unrevealed Codex seal because Claude hit its weekly limit. Next action is a fresh post-reset read-only A/B; mutation remains gated on You.md atomic coordination; lab `origin` is upstream.
