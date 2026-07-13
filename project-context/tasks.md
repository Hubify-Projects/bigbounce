# Tasks — handoff acceptance

## Objective

Prove the Phase 0 MVP: two machines operate one Big Bounce lab safely from the pushed `ops/handoff/` package before enabling any multi-lab behavior.

## Active

- [ ] **HO-002 — One-lab coordination acceptance:** while the live review loop is idle or explicitly handed off, verify lease claim/renew/release, heartbeat `machineId`, git synchronization, and collision-free shared-state writes. (source: 2026-07-13 handoff prompt)

## Blocked

- **HO-B01 — Browser/manifest ownership:** live M41 owns the headed browser and review manifest; acceptance must not claim the lease or write browser/ledger state until M41 is idle or explicitly handed off.
- **HO-B02 — Hubify verification:** Hubify CLI is unauthenticated, so Hubify-backed lab/status claims cannot yet be independently verified.
- **HO-B03 — Shared-stack sync:** the machine-sync/shared configuration repo is dirty/conflicted; do not pull, overwrite, or sync it until ownership is reconciled.

## Done

- [x] **HO-001 — Receiving-machine bootstrap:** Codex acceptance run reached `READY` with 21 PASS / 2 WARN / 0 FAIL; warnings are Hubify authentication and per-machine reviewer-login confirmation. (source: 2026-07-13 handoff prompt)
- [x] **HO-003 — Portability acceptance:** this Codex receiving session loaded the repository instructions, mapped host-specific gaps, and completed bootstrap/tool hardening without hidden Claude context. (source: 2026-07-13 handoff prompt)
- [x] **HO-004 — Close bootstrap gaps:** TinyTeX and exact SDK detection fixed; `.env.example` now covers every BigBounce local key name; isolated lease/cron regression tests pass. (source: 2026-07-13 Claude report)
- [x] Handoff/ops commits `e730850b`, `de4750f3`, and `27596c56` exist, are reachable from `main`, and are pushed; M40 adjudication `df8d89a3` is also pushed. (verified 2026-07-13 13:52 PT)
- [x] Current repo is synchronized with `origin/main` at `df8d89a3`; the lab lease is free and the heartbeat records `machineId`. (verified 2026-07-13 13:52 PT)

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
