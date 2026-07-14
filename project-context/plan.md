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

1. **Done:** harden the local subscription-first mirrored launcher in `learning-cmux-with-agents` through code commit `fb815f8` and documentation commit `be65a6f` (building on the earlier launcher commits): before any CMUX create, run one subscription-authenticated completed turn per unique provider/model/effort route with alternate API/cloud environment variables scrubbed; bind the check to an absolute executable digest and exact sentinel; publish only hash-bound `0444` receipts; retain caller-bound per-surface provider-auth/short-liveness receipts; and on any route failure publish typed pre-release invalidation with zero workspaces created. Target-repository write denial, atomic seal/reveal, process-group cleanup, and deadline adjudication remain in force. **37 tests pass.**
2. **Inconclusive evidence only:** the first diagnostic run did not establish a valid model comparison.
3. **Latest clean attempt:** run `20260714T000136Z-024658000-bfee86cfcc83` launched from a clean snapshot, verified the complete topology, and bypassed every Codex trust gate. Codex submitted one sealed result; Claude reached its weekly subscription limit before submitting. No result was revealed and no winner exists. This legacy run predates deadline-aware contracts and has no deadline, so it cannot be retroactively expired.
4. **Now:** wait for the Claude allowance reset at **2026-07-15 07:00 America/Los_Angeles**, then start a fresh clean envelope and run both GPT-5.6 Sol high and Claude Opus 4.8 high arms from the same bound snapshot.
5. Capture both fresh sealed outputs, reveal only after dual submission, and compare quality, latency, and coordination behavior using the recorded run artifacts.
6. Treat readiness evidence precisely: it proves one completed subscription-authenticated turn at launch time for each unique provider/model/effort route, plus provider-auth preflight and short process liveness for each interactive surface. It does not prove a completed turn for every interactive session, later quota availability, final result submission, or hostile isolation from the same OS user.
7. Keep all mutation disabled until You.md atomic claims, heartbeats, overlap detection, and isolated worktrees are implemented and acceptance-tested. The per-surface process boundary is not hostile isolation against the same OS user or independently launched raw-CMUX processes; that requires a stronger broker/identity boundary.
8. Keep the lab commits local until a Houston-owned fork is configured; the current `origin` is IndyDevDan's upstream repository.

## Gates

- **Now — Phase 0:** two machines, one lab. This is the only active phase.
- **Pending — Phase 1:** Codex as a second orchestrator in the same lab; requires Phase 0 green and Houston approval.
- **Pending — Phase 2:** two independent labs on the bounded P4 mirror-flip reproduction with blind seal/reveal and corroboration; requires Phase 1 green plus tested `exchange/`, `labId`, and site support.
- **Pending — Phase 3:** open-source Lab C; requires one successful two-lab blind/reveal/corroboration cycle.

## Recovery notes

- Last prompt-history reconciliation: 2026-07-13 17:31 PT.
- Source reviewed: 2026-07-13 handoff prompt/Claude report, Codex repository-state acceptance audit, and CMUX prompts at 14:49, 15:38, 15:56, 16:14, and 17:31 PT.
- Verified baseline before this context update: `main` and `origin/main` at `55e0b0ad`; handoff commits remain reachable and pushed. Lease/heartbeat evidence is retained from the earlier acceptance audit.
- Active blockers: M41 browser/manifest ownership, unauthenticated Hubify CLI, dirty/conflicted machine-sync shared repo.
- CMUX boundary: local unpushed commits `fb815f8` and `be65a6f` are green at 37 tests. Before any CMUX create, the launcher now requires one completed subscription-authenticated turn per unique provider/model/effort route, scrubs alternate API/cloud environment variables, binds an exact sentinel to the absolute executable digest, and publishes only hash-bound `0444` receipts; any route failure produces typed pre-release invalidation with zero workspaces. Existing caller-bound per-surface auth/liveness and target-repository write denial remain. This is route-level launch-time proof, not completed-turn proof for every interactive session, later quota, final submission, or hostile same-user isolation. The first diagnostic remains inconclusive and the clean rerun has only an unrevealed Codex seal because Claude hit its weekly limit. Next action is a fresh post-reset read-only A/B; mutation remains gated on You.md atomic coordination; lab `origin` is upstream.
