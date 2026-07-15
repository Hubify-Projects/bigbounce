# Tasks — publication-readiness campaign

## Objective

Drive all six canonical papers through exact-artifact, venue-correct,
non-Anthropic multi-model review; truth-audit and close every real finding;
then synchronize PDFs, versions, SSOT, Convex, API, and the public site without
overstating readiness. The previous handoff/CMUX tracks remain preserved below
but are not the current scientific critical path.

## Active

- [ ] **PUB-001 — Close active science revisions:** finish P1A v1A.0.120, P1B exact-window robustness, P3 r5, P4 portability/provenance closure, and P5 AJ-oriented structural closure with reproducible evidence and full PDF audits. (source: 2026-07-13 19:28 PT; 2026-07-14 10:39 PT)
- [ ] **PUB-002 — Re-review exact immutable PDFs:** run fresh Codex/ChatGPT-subscription, Grok, and Gemini boards against the correct journal/article type; retain raw reports, exact PDF SHA-256, source commit, prompt hash, provider/model, and normalized truth-audit. The OpenAI perspective is Codex CLI authenticated by ChatGPT subscription with OpenAI API credentials unset — never separately billed OpenAI API. Grok/xAI and Gemini direct-provider API legs are allowed. No Anthropic/Claude leg in this campaign. Re-review only after a reader-visible content-hash change, except one declared independent confirmation of a high-risk closure. (source: 2026-07-13 19:28 PT; 2026-07-14 readiness-regression audit)
- [ ] **PUB-003 — Implement safe acceleration controls:** centralize the six-paper registry, generate content-addressed review packets, fail closed on stale/wrong PDFs or ambiguous commits, separate science gates from workflow gates, and add deterministic bounded inner parallelism only where serial-equivalence tests pass. (source: 2026-07-14 10:39 PT)
- [ ] **PUB-004 — Atomic release synchronization:** only after the exact boards close, update paper mirrors, version data, claims tables, SSOT, Convex/API, review timeline, and site in the same bisected release sequence; then perform browser QA and push `main`. (source: 2026-07-13 19:28 PT)
- [ ] **PUB-005 — Immutable PDF history:** retain every paper PDF under a version-and-PST-timestamped immutable name with source commit, SHA-256, page count, build command, and review references in an append-only manifest; verify the canonical archive plus two mirrors before cleanup. Never delete the only copy of any historical PDF. (source: 2026-07-14 PDF-retention mandate)
  - 2026-07-14/15 progress: current/future six-paper snapshot retention is gated through Directive-G; full Git PDF history inventory exists at `project-context/pdf-archive/manifests/2026/07/20260714T235000Z-history-inventory-20260714-history.json` with 1,356 reachable PDF object/path rows, 1,094 high-confidence manuscript rows, and 262 explicit unclassified rows. Fast historical byte materialization now covers offsets 0-1357 with no gaps across 49 `history-backfill-fast-*` manifests, processed 1,095 classified manuscript rows, created 837 new SHA-256 objects and 843 new refs, and reported zero row errors. Archive state after verification: 1,097 objects, 1,106 refs, 0 bad hardlinks. Remaining work is full page-counted tranche completion plus two independent mirrors.
- [ ] **PUB-006 — Normalize readiness instrumentation:** separate stable scientific/reproducibility/venue/release/human gates from the raw reviewer-verdict distribution; migrate historical EXT11/EXT17 and exact-artifact rows without relabeling provider verdicts; mark wrong/stale/missing legs invalid rather than scoring them. (source: 2026-07-14 readiness-regression audit)
- [ ] **PUB-007 — Compile review learning into mandatory prevention:** replace the prose-only archive→mine→preflight loop with one canonical HubStack engine, a machine-readable rule catalog, a BigBounce all-six-paper adapter, content-addressed PASS receipts bound into review packets, and learning-efficiency metrics. Every truth-audited NEW-REAL blocker/major or recurrent minor must add or strengthen an executable regression gate and sweep all six papers before another review wave. (source: 2026-07-15 15:24 PT recursive-improvement mandate)

- [ ] **HO-002 — One-lab coordination acceptance:** while the live review loop is idle or explicitly handed off, verify lease claim/renew/release, heartbeat `machineId`, git synchronization, and collision-free shared-state writes. (source: 2026-07-13 handoff prompt)
- [ ] **CMUX-002 — Fresh post-reset mirrored read-only A/B:** after the Claude allowance resets, launch a new clean, bounded task envelope through the Codex GPT-5.6 Sol high and Claude Opus 4.8 high orchestrator teams; reveal only after both fresh-run results submit, then compare quality, latency, and coordination without allowing either team to mutate BigBounce. The first diagnostic run was inconclusive. Clean run `20260714T000136Z-024658000-bfee86cfcc83` launched from a clean snapshot with verified four-workspace topology and every Codex trust gate bypassed; Codex sealed its result, but Claude hit its weekly subscription limit before submission, so nothing was revealed and there is no winner. The next clean run must exercise the new pre-create route gate: one completed subscription-authenticated launch-time turn per unique provider/model/effort route, with typed invalidation and zero workspaces on failure. This is not completed-turn proof for every interactive session, later quota, or final submission. (source: 2026-07-13 CMUX continuation)

## Blocked

- **HO-B01 — Browser/manifest ownership:** live M41 owns the headed browser and review manifest; acceptance must not claim the lease or write browser/ledger state until M41 is idle or explicitly handed off.
- **HO-B02 — Hubify verification:** Hubify CLI is unauthenticated, so Hubify-backed lab/status claims cannot yet be independently verified.
- **HO-B03 — Shared-stack sync:** the machine-sync/shared configuration repo is dirty/conflicted; do not pull, overwrite, or sync it until ownership is reconciled.
- **CMUX-B01 — Mutation/coordination gate:** keep CMUX dogfood read-only until You.md provides atomic work claims, heartbeats, overlap detection, and isolated worktrees. Every run-owned surface now has a process-enforced target-repository write denial, but this is not hostile isolation against the same OS user or independently launched raw-CMUX processes; a stronger broker/identity boundary remains required.
- **CMUX-B02 — Claude comparison allowance:** Claude Opus 4.8 could not submit the clean-run result because the weekly subscription limit was reached; the CLI reports reset at **2026-07-15 07:00 America/Los_Angeles**. This legacy run predates deadline-aware contracts and has no deadline, so it cannot be retroactively marked expired; its lone Codex result remains sealed and unrevealed. Use a fresh envelope after reset rather than declaring a winner from this run.

## Done

- [x] **CMUX-003 — Audit model-routing efficiency and provider authenticity:** OpenRouter category ranks were confirmed as usage/spend popularity, not capability scores; live cmux was GPT-5.6 Sol-only (high/medium/low), with no Terra/Luna/Grok/Gemini runtime evidence. The audit also found that the then-current BigBounce INT pipeline made separately billed direct OpenAI/xAI/Gemini native-PDF calls. That finding triggered the corrected standing policy: OpenAI review now uses Codex CLI/ChatGPT subscription only with API credentials unset; direct Grok/xAI and Gemini calls remain allowed. Recommended routing is Sol/Fable for director checkpoints, Terra for leads, Luna/mini/spark for mechanical workers/pollers, and real Grok/Gemini calls as independent reviewers. (source: 2026-07-14 12:10 PT; corrected 2026-07-14)
- [x] **HO-001 — Receiving-machine bootstrap:** Codex acceptance run reached `READY` with 21 PASS / 2 WARN / 0 FAIL; warnings are Hubify authentication and per-machine reviewer-login confirmation. (source: 2026-07-13 handoff prompt)
- [x] **HO-003 — Portability acceptance:** this Codex receiving session loaded the repository instructions, mapped host-specific gaps, and completed bootstrap/tool hardening without hidden Claude context. (source: 2026-07-13 handoff prompt)
- [x] **HO-004 — Close bootstrap gaps:** TinyTeX and exact SDK detection fixed; `.env.example` now covers every BigBounce local key name; isolated lease/cron regression tests pass. (source: 2026-07-13 Claude report)
- [x] **CMUX-001 — Local mirrored launcher and hardened evaluation contract:** code commit `fb815f8` and documentation commit `be65a6f` in the separate `learning-cmux-with-agents` lab add a fail-closed provider-route gate before any CMUX create: one subscription-authenticated completed turn per unique provider/model/effort route, alternate API/cloud environment scrubbing, an exact sentinel bound to the absolute executable digest, hash-only `0444` receipts, and typed pre-release invalidation with zero workspaces on failure. Existing per-surface caller-bound provider-auth/short-liveness receipts, immutable snapshot binding, atomic seal/reveal, target-repository write denial, process-group cleanup, and deadline adjudication remain. **37 tests pass.** This is route-level launch-time proof—not completed-turn proof for every interactive session, later quota, final submission, or hostile same-user isolation. Houston's fork is configured as local remote `fork`, `remote.pushDefault=fork`, branch `codex/youmd-cmux-lab` is pushed, and draft PR `https://github.com/houstongolden/learning-cmux-with-agents/pull/1` targets the fork's `main`; `origin` remains IndyDevDan's upstream repository. (sources: 2026-07-13 CMUX prompts and acceptance runs)
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

- Readiness is evidence, not a target to manufacture: never claim 95--99%, acceptance, or minor-only status until every exact-PDF board and residual gate supports it.
- Reviewer venue/article type is part of the review artifact. Keep PRD, CQG Note, AJ, ApJS, JCAP, or MNRAS boards separate; never relabel a verdict after the fact.
- Stop repeated review on unchanged content: after two valid independent waves on the same PDF hash yield zero genuinely new reader-visible findings, preserve the verdict spread and advance by stable gates. Never repeat solely to obtain a preferred verdict word.
- Acceleration may remove duplicate compute, stale-path risk, and repeated review work; it may not remove truth audits, reproducibility checks, independent review, or all-page PDF visual inspection.
- Review models are residual-novelty detectors, not the first-line linter. No new review packet may dispatch unless its exact source/PDF hash is bound to a current strict portfolio-preflight PASS receipt.
- Measure known-pattern escape rate, preflight interception precision/recall, closure-regression rate, claim-evidence coverage, and archive/catalog freshness; round count and favorable verdict volume are not convergence metrics.
- Current provider policy: OpenAI perspective via Codex CLI/ChatGPT subscription only, with API credentials unset — never OpenAI API billing. Grok/xAI and Gemini direct-provider calls are allowed. No Anthropic or Claude calls. A missing vendor leg is recorded as absent, never silently replaced or fabricated.
- Historical PDFs are append-only evidence. Alias paths may advance, but immutable versioned/timestamped PDFs and their manifests must remain retained.
- Do not publish partial readiness state. Public PDF/version/SSOT/Convex/API/site changes land only after their exact evidence packet is complete and mutually consistent.

- MVP first: do not implement `labId`, site lab views, lab branches, or seal/reveal tooling during Phase 0.
- Git is the sync bus, Convex is shared live state, and only the lease holder may drive browser/verdict/ledger writes.
- Preserve current M41, prompt-history, and generated-skill working-tree ownership; do not fold those files into handoff acceptance work.
- CMUX lab code lives in `/Users/houstongolden/Desktop/CODE_YOU/learning-cmux-with-agents`; push publication through Houston's `fork` remote (`remote.pushDefault=fork`), never directly to the upstream `origin`. Draft PR `https://github.com/houstongolden/learning-cmux-with-agents/pull/1` tracks `codex/youmd-cmux-lab` against the fork's `main`.
- The live mirrored run is an evaluation lane only: no review manifest, SSOT, site, Convex, lease, or source mutation is authorized by CMUX participation.
- A single sealed result is not a comparison outcome. Never reveal or name a winner until the same fresh-run contract has accepted both arms; do not retroactively expire a legacy contract that has no deadline.
