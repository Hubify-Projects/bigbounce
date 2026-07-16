# Plan — exact-artifact publication campaign

## Goal

Reach honest publication readiness across the six canonical papers by closing
real science findings first, reviewing immutable exact PDFs at the correct
venues, and synchronizing public state only after the evidence agrees. Optimize
wall-clock time through independent lanes, deterministic compute parallelism,
and artifact-addressed review reuse without weakening scientific gates.

## Account handoff checkpoint

The dedicated Codex subscription handoff is documented in
`project-context/BIGBOUNCE_CODEX_ACCOUNT_HANDOFF_2026-07-16.md`. On resume,
verify authentication and the no-OpenAI-API routing regression before any new
wave. The current direct-provider default is temporary quota protection. Once
the new account passes verification, set
`BIGBOUNCE_CODEX_SUBSCRIPTION_ENABLED=1` to restore Codex as a normal review
leg; no scientific gates or evidence contracts change.

## Current execution order

1. Compile the accumulated review taxonomy into a canonical machine-readable HubStack preflight engine and a BigBounce all-six-paper adapter. Bind every PASS receipt to source commit, source/PDF hashes, registry hash, and rule-catalog hash.
2. Run the proactive portfolio sweep before any new review dispatch. Close latent known-pattern defects in independent paper lanes and rerun the transitive claim/artifact/cross-paper dependency gates after every closure.
3. Execute the true scientific critical path in parallel: corrected P1B physical-spectrum production; P2 transfer/covariance or explicit venue-scope decision; P1A/P3 archives; P4/P5 dependency freeze and release closure.
4. Freeze each passing manuscript into a content-addressed packet containing paper ID, version, exact source/PDF paths, SHA-256, page count, source commit, target venue/article type, prompt ID, allowed context, and the exact portfolio-preflight receipt.
5. Run fresh exact-PDF panels only as residual-novelty confirmation. Provider routing per CLAUDE.md directive N (2026-07-16): Codex/OpenAI PAUSED entirely; panels = Claude reviewer subagent (Opus-tier, exact-PDF-bound, raw report saved) + direct Grok/xAI and Gemini API legs. Preserve raw reports and normalize findings into the append-only truth ledger.
6. For every truth-audited NEW-REAL blocker/major or recurrent minor, add or strengthen an executable regression fixture, sweep all six papers, close confirmed defects, and apply the content-hash stop rule instead of chasing favorable verdict words.
7. Archive every compiled PDF immutably, then run the atomic claims/version/PDF/SSOT/Convex/API/site release chain and governed browser QA.

## PDF History Backfill Status — 2026-07-14

- Complete Git PDF inventory is written at `project-context/pdf-archive/manifests/2026/07/20260714T235000Z-history-inventory-20260714-history.json`: 1,356 reachable PDF object/path rows, 1,094 high-confidence six-paper manuscript rows, and 262 explicit unclassified rows.
- Page-counted backfill is staged because the full 1,094-row pass is expensive. Use `tools/pdf_version_retention.py --history-backfill --history-offset <n> --history-limit <m>` in bounded chunks.
- First page-counted proof tranche is `project-context/pdf-archive/manifests/2026/07/20260715T004000Z-history-backfill-0104-0108-20260714-history.json`: five P4 manuscript rows, zero errors, verified object/reference hardlinks, page counts 22, 24, 25, 22, 21.
- Do not treat fast history inventory or interrupted fast chunks as complete page-counted retention. Full completion requires chunked page-counted manifests plus offsite mirror verification.

## Implemented and queued accelerations

- **Implemented:** parallel non-overlapping paper lanes; exact-PDF SHA binding; P3 checkpoint-product reuse; P1B bounded two-job compute cap; venue-fit boards kept separate from correctness boards.
- **In progress:** P1B deterministic inner parallelism with serial scientific-field equality; P1A/P3/P4/P5 closures.
- **Next tooling lane:** one canonical six-paper registry plus content-addressed review-packet generator and fail-closed tests; migrate stale path/venue maps in `int_wave.sh`, `int_api_review_2026-07-08.py`, and `directive_g.sh` incrementally.
- **Immediate architecture correction:** the 2026-07-15 audit found 70+ documented review patterns but only a handful enforced by `tools/check_new_patterns.sh`. Implement one executable HubStack learning-loop engine, one BigBounce adapter, packet-bound preflight receipts, and measured known-pattern escape/closure-regression rates before another review wave.
- **Deliberately deferred:** Snakemake/DVC migration and broad workflow rewrites during the submission push; they add churn without shortening the present critical path.

## Scientific gates that acceleration cannot bypass

- Derivations and quantitative claims receive independent truth audits.
- Every review binds to an immutable exact PDF and declared venue/article type.
- Every PDF compile receives log, reference, URL/path, and all-page visual overflow inspection.
- Deterministic parallel compute must match the serial scientific fields exactly before use.
- Public readiness state is atomic and evidence-backed; absent credentials, DOI, archive, or external validation remain visible gates.
- Stable gate readiness and the raw reviewer distribution are separate instruments. Provider verdicts remain verbatim; wrong/stale/missing legs are gaps, not inferred scores.

## Paused legacy track

The handoff/CMUX Phase 0 material below is retained for recovery but is paused
while the publication campaign is the user-designated primary goal.

## Model-routing audit — 2026-07-14

- Keep GPT-5.6 Sol high as the primary director for architecture, novel science judgment, synthesis, and acceptance; use Fable 5 high as a blinded alternate/checkpoint director when the Claude subscription is available.
- Move routine team leads to GPT-5.6 Terra medium/high. Reserve Sol workers for contested derivations or failure-sensitive merges.
- Route bounded implementation, grep, formatting, QA, and polling to GPT-5.6 Luna, GPT-5.4 mini, or Codex Spark at low/medium effort; consider DeepSeek V4 Flash for isolated bulk triage where OpenRouter API use is appropriate and outputs are independently checked.
- Keep Grok and Gemini as real direct-provider/native-PDF reviewer legs with raw response and usage receipts. A CMUX pane name or persona prompt never counts as a vendor leg.
- Add response-resolved model IDs, request IDs, usage/cost fields, and provider-dispatch tests before treating model-routing telemetry as fully auditable.

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
8. **Published safely:** the Houston-owned fork is `https://github.com/houstongolden/learning-cmux-with-agents`; local remote `fork` points there, `origin` remains IndyDevDan's upstream repository, and `remote.pushDefault=fork`. Branch `codex/youmd-cmux-lab` is pushed to the fork with draft PR `https://github.com/houstongolden/learning-cmux-with-agents/pull/1` open against the fork's `main`.

## Gates

- **Now — Phase 0:** two machines, one lab. This is the only active phase.
- **Pending — Phase 1:** Codex as a second orchestrator in the same lab; requires Phase 0 green and Houston approval.
- **Pending — Phase 2:** two independent labs on the bounded P4 mirror-flip reproduction with blind seal/reveal and corroboration; requires Phase 1 green plus tested `exchange/`, `labId`, and site support.
- **Pending — Phase 3:** open-source Lab C; requires one successful two-lab blind/reveal/corroboration cycle.

## Recovery notes

- Last prompt-history reconciliation: 2026-07-15 15:35 PT.
- Current source prompts reviewed: the 2026-07-13 publication mandate, 2026-07-14 acceleration mandate, and 2026-07-15 recursive-prevention correction.
- Current hard boundary: no Anthropic/Claude calls; no public sync or readiness uplift until exact boards and truth audits close.

- Last prompt-history reconciliation: 2026-07-13 17:31 PT.
- Source reviewed: 2026-07-13 handoff prompt/Claude report, Codex repository-state acceptance audit, and CMUX prompts at 14:49, 15:38, 15:56, 16:14, and 17:31 PT.
- Verified baseline before this context update: `main` and `origin/main` at `55e0b0ad`; handoff commits remain reachable and pushed. Lease/heartbeat evidence is retained from the earlier acceptance audit.
- Active blockers: M41 browser/manifest ownership, unauthenticated Hubify CLI, dirty/conflicted machine-sync shared repo.
- CMUX boundary: commits `fb815f8` and `be65a6f` are green at 37 tests and are published on Houston's fork via `codex/youmd-cmux-lab`; draft PR `https://github.com/houstongolden/learning-cmux-with-agents/pull/1` targets the fork's `main`. Local `origin` remains upstream, while `fork` is the push target through `remote.pushDefault=fork`. Before any CMUX create, the launcher now requires one completed subscription-authenticated turn per unique provider/model/effort route, scrubs alternate API/cloud environment variables, binds an exact sentinel to the absolute executable digest, and publishes only hash-bound `0444` receipts; any route failure produces typed pre-release invalidation with zero workspaces. Existing caller-bound per-surface auth/liveness and target-repository write denial remain. This is route-level launch-time proof, not completed-turn proof for every interactive session, later quota, final submission, or hostile same-user isolation. The first diagnostic remains inconclusive and the clean rerun has only an unrevealed Codex seal because Claude hit its weekly limit. Next action is a fresh post-reset read-only A/B; mutation remains gated on You.md atomic coordination.
