# Tasks — handoff acceptance

## Objective

Prove the Phase 0 MVP: two machines operate one Big Bounce lab safely from the pushed `ops/handoff/` package before enabling any multi-lab behavior.

## Active

- [ ] **HO-002 — One-lab coordination acceptance:** while the live review loop is idle or explicitly handed off, verify lease claim/renew/release, heartbeat `machineId`, git synchronization, and collision-free shared-state writes. (source: 2026-07-13 handoff prompt)
- [ ] **CMUX-002 — Fresh post-reset mirrored read-only A/B:** after the Claude allowance resets, launch a new clean, bounded task envelope through the Codex GPT-5.6 Sol high and Claude Opus 4.8 high orchestrator teams; reveal only after both fresh-run results submit, then compare quality, latency, and coordination without allowing either team to mutate BigBounce. The first diagnostic run was inconclusive. Clean run `20260714T000136Z-024658000-bfee86cfcc83` launched from a clean snapshot with verified four-workspace topology and every Codex trust gate bypassed; Codex sealed its result, but Claude hit its weekly subscription limit before submission, so nothing was revealed and there is no winner. (source: 2026-07-13 CMUX continuation)

## Blocked

- **HO-B01 — Browser/manifest ownership:** live M41 owns the headed browser and review manifest; acceptance must not claim the lease or write browser/ledger state until M41 is idle or explicitly handed off.
- **HO-B02 — Hubify verification:** Hubify CLI is unauthenticated, so Hubify-backed lab/status claims cannot yet be independently verified.
- **HO-B03 — Shared-stack sync:** the machine-sync/shared configuration repo is dirty/conflicted; do not pull, overwrite, or sync it until ownership is reconciled.
- **CMUX-B01 — Mutation/coordination gate:** keep CMUX dogfood read-only until You.md provides atomic work claims, heartbeats, overlap detection, and isolated worktrees. The current sealed-result contract is cooperative process isolation, not an adversarial same-OS-user security boundary.
- **CMUX-B02 — Claude comparison allowance:** Claude Opus 4.8 could not submit the clean-run result because the weekly subscription limit was reached; the CLI reports reset at **2026-07-15 07:00 America/Los_Angeles**. This legacy run predates deadline-aware contracts and has no deadline, so it cannot be retroactively marked expired; its lone Codex result remains sealed and unrevealed. Use a fresh envelope after reset rather than declaring a winner from this run.

## Done

- [x] **HO-001 — Receiving-machine bootstrap:** Codex acceptance run reached `READY` with 21 PASS / 2 WARN / 0 FAIL; warnings are Hubify authentication and per-machine reviewer-login confirmation. (source: 2026-07-13 handoff prompt)
- [x] **HO-003 — Portability acceptance:** this Codex receiving session loaded the repository instructions, mapped host-specific gaps, and completed bootstrap/tool hardening without hidden Claude context. (source: 2026-07-13 handoff prompt)
- [x] **HO-004 — Close bootstrap gaps:** TinyTeX and exact SDK detection fixed; `.env.example` now covers every BigBounce local key name; isolated lease/cron regression tests pass. (source: 2026-07-13 Claude report)
- [x] **CMUX-001 — Local mirrored launcher and hardened evaluation contract:** the separate `learning-cmux-with-agents` lab now has subscription-authenticated mirrored teams, immutable task/repository snapshot binding, Codex project-trust bypass, atomic one-way seal/reveal, a transactional four-workspace topology gate with scoped rollback, deadline/timeout adjudication, fail-closed mutation, and **19 passing tests**. Local commits remain intentionally unpushed because `origin` is IndyDevDan's upstream repository rather than Houston's fork. (sources: 2026-07-13 CMUX prompts and acceptance runs)
- [x] Handoff/ops commits `e730850b`, `de4750f3`, and `27596c56` exist, are reachable from `main`, and are pushed; M40 adjudication `df8d89a3` is also pushed. (verified 2026-07-13 13:52 PT)
- [x] Current repo is synchronized with `origin/main` at `b93528b6`; the prior lease/heartbeat acceptance evidence remains recorded. (verified 2026-07-13 16:15 PT)

## Phase 0 completion criteria

- A second machine reaches bootstrap `READY` with secrets restored without exposure.
- Lease and heartbeat behavior is exercised during an explicit idle/handoff window.
- Both machines converge on the same git commit and Convex deployment without browser, manifest, ledger, or site-state collisions.
- Codex can resume from repository instructions alone; all remaining warnings and host-specific gaps are recorded.
- Houston accepts the two-machine one-lab workflow.

## Gated — not active

- **Phase 1:** second orchestrator (Codex), same lab; requires Phase 0 green plus Houston approval.
- **Phase 2:** two blind labs on the bounded P4 end-to-end mirror-flip target with seal/reveal, `labId`, and site support; requires Phase 1 green and tested scaffolding.
- **Phase 3:** open-source Lab C; requires a successful two-lab blind/reveal/corroboration cycle.

## Watchpoints

- MVP first: do not implement `labId`, site lab views, lab branches, or seal/reveal tooling during Phase 0.
- Git is the sync bus, Convex is shared live state, and only the lease holder may drive browser/verdict/ledger writes.
- Preserve current M41, prompt-history, and generated-skill working-tree ownership; do not fold those files into handoff acceptance work.
- CMUX lab code lives in `/Users/houstongolden/Desktop/CODE_YOU/learning-cmux-with-agents`; do not push its local branch to the configured upstream `origin` without first adding a Houston-owned fork.
- The live mirrored run is an evaluation lane only: no review manifest, SSOT, site, Convex, lease, or source mutation is authorized by CMUX participation.
- A single sealed result is not a comparison outcome. Never reveal or name a winner until the same fresh-run contract has accepted both arms; do not retroactively expire a legacy contract that has no deadline.
