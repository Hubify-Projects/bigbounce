# BigBounce Codex account handoff — 2026-07-16

## Durable objective

Drive all six BigBounce papers through honest internal and external
non-Anthropic multi-model review, truth-audited closure, re-review,
PDF/version/SSOT/Convex/API/site synchronization, and evidence-backed 95–99%
publication readiness (accepted or minor-revisions-only), documenting every
process acceleration without fabricating or overstating results.

This objective remains active. It is not complete: several scientific,
archive, external-validation, and human/editorial gates remain open.

## Exact resume point

- Repository: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce`
- Branch: `main`
- Remote HEAD after the latest handoff commit: `1e81d4e6`
- Latest pushed change: `chore(reviews): conserve subscription usage by default`
- P1B v2B.0.8 exact-PDF confirmation is recorded in
  `project-context/peer-reviews/INT_v3/ROUND_2026-07-16-P1B-v2B.0.8-EXACTPDF-cf7ede29-JORS-NONANTHROPIC-CONFIRM/`.
- Direct Grok and Gemini legs completed; no new executable defect was found by
  the truth audit. The Codex leg was deliberately interrupted (exit 130) to
  conserve quota and is recorded as absent, never treated as a pass.
- P1B readiness remains 56 because the archive/editorial gate is unresolved;
  no acceptance or 95–99% claim is authorized.

## Provider and usage policy (temporary cost mode)

- OpenAI review/orchestration: Codex CLI authenticated through the active
  ChatGPT subscription only. Do not use `OPENAI_API_KEY` or OpenAI API review
  routes.
- Until the dedicated account is verified, routine review waves default to
  direct Grok/xAI and Gemini API legs as a temporary quota-protection measure.
  This is not a permanent research restriction and does not remove Codex from
  the architecture.
- Opt in for a normal wave with `--with-codex`, or use `--codex-only` for a
  subscription-only arbitration. Example:

  ```bash
  tools/int_wave.sh P4 "next exact-PDF residual board"
  tools/int_wave.sh --with-codex P4 "high-risk arbitration"
  ```

- After account verification, restore Codex as the normal leg without editing
  the research logic:

  ```bash
  export BIGBOUNCE_CODEX_SUBSCRIPTION_ENABLED=1
  ```

  The direct-provider legs remain independently available, and the routing can
  be changed back to quota-conservation mode at any time.

- Terra/Luna are preferred for bounded delegated work only when the runtime
  actually exposes those routes. Never label a pane/persona as a vendor leg
  without a raw provider receipt.
- The prior measured lower bound was ~44.3M BigBounce-related tokens; account
  quota percentages are not exposed locally, so any percentage estimate is
  explicitly approximate.

## Account-switch procedure

1. Finish or interrupt any active Codex CLI process and verify no review wave is
   running: `pgrep -af 'codex|int_wave'`.
2. Preserve this repository state; do not reset or clean unrelated worktree
   files. Confirm `git status --short` and `git log -1 --oneline`.
3. Authenticate the dedicated ChatGPT account in the Codex CLI using the
   normal interactive login flow. Do not place credentials in the repository,
   `.env.local`, or this handoff.
4. Verify the subscription route with a bounded harmless command and save only
   non-secret metadata/receipt. Do not launch a full science wave until the
   route is confirmed.
5. Re-open this file, `project-context/AGENT_ONBOARDING.md`, `CLAUDE.md`,
   `AGENT_RULES.md`, `project-context/tasks.md`, and `project-context/plan.md`.
6. Run the regression check:

   ```bash
   python3 -m unittest tools.tests.test_no_openai_api_review
   ```

7. Start with a direct-provider-only exact-PDF wave. Use Codex only for a
   declared high-risk arbitration after the direct evidence is retained.

## You.md / local stack state

`youmd status` currently reports a healthy local bundle (`~/.you`), 316/316
skills installed, Secret Vault metadata available, and project context rooted
at this repository. The remote bundle is ahead and the local shared-agent repo
is dirty/conflicted; therefore no automatic `you sync`, shared-repo pull, or
config overwrite was performed during this handoff. Resolve that ownership
conflict before running the full machine-sync workflow.

Safe post-login checks (metadata only; never print secrets):

```bash
youmd status
youmd sync                 # only after reviewing shared-repo conflict state
you machine verify
~/.agent-shared/bin/env-key-audit.py --root ~/Desktop/CODE_YOU
```

Use the You.md Secret Vault for any account-backed environment restoration;
never copy or commit `.env.local` values. The account change affects Codex
authentication, not the project’s provider receipts or scientific evidence.

## Next scientific actions

1. Resolve the P1B archive/editorial gate and retain the corresponding evidence.
2. Run the next exact-PDF direct Grok/Gemini residual board for the highest-value
   unclosed paper (P4/P5/P3 according to current SSOT), with strict preflight.
3. Truth-audit findings; for every real blocker/major or recurrent minor, add a
   regression rule and sweep all six papers before re-review.
4. Complete page-counted historical PDF retention and two-mirror verification.
5. Only after all exact boards and gates close, perform the atomic PDF/version/
   claims/SSOT/Convex/API/site release and governed browser QA.

## Non-negotiable honesty gates

Missing or interrupted legs remain absent. Wrong/stale PDFs, invalid commits,
archive gaps, unavailable DOI/external validation, and unresolved human/editorial
requirements remain visible blockers. Do not claim publication readiness from a
reviewer vote or from a new account login alone.
