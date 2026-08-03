# BigBounce recovery plan

**You.md/project-context entry point · reconciled 2026-08-03**

The canonical executable plan is [`../ops/PLAN.md`](../ops/PLAN.md). This file
is the compact recovery map for a newly resumed agent or a You.md context sync;
it must not become a second planning authority.

## Recover in this order

1. Read [`../ops/PLAN.md`](../ops/PLAN.md) for the current phase and priorities.
2. Read [`paper_registry.json`](paper_registry.json) for the six current paper
   identities, paths, and venues.
3. Read [`SSOT/index.md`](SSOT/index.md), then the relevant
   `SSOT/paper-*/status.md`, for current versions and honest limitations.
4. Read [`SSOT/queue.md`](SSOT/queue.md) for executable work.
5. Read [`peer-reviews/REVISION_TRACKER.md`](peer-reviews/REVISION_TRACKER.md)
   and the linked truth audits only when review evidence is needed.
6. Compare Convex and `site/src/data/` against the SSOT before making a public
   status claim.

## Current objective

Reconcile repository truth and the live production projection, verify the six
final artifacts with a bounded final-hash acceptance pass, obtain Houston's
five-point per-paper sign-off, and enter journal submission. Current versions
are P1A v1A.0.127, P1B v2B.0.16, P2 v1.7.130, P3 v3.2.0-r14, P4 v1.0.272, and
P5 v0.1.146-2026-07-24.

The four agent gates are recorded as 95/95 under Directive P. Publishing gates
and independent human review are a separate phase; no submission or acceptance
is inferred. The final PDFs contain post-board closures, so perform only the
bounded final-hash confirmation described in `ops/PLAN.md`, not another broad
verdict-harvesting campaign.

## Working-tree and branch caution

- Preserve user-authored changes in `project-context/prompts.md`.
- Treat untracked `.agents/skills/bigbounce-*` directories as user-owned until
  their ownership and intended canonical home are resolved.
- `main` and `origin/main` were aligned at the start of the 2026-08-03 audit.
- Diff unmerged unified-P1/research/worktree branches before consolidation;
  branch age or obsolete framing is not proof that the branch has no unique
  content.

## Superseded planning surfaces

`SSOT/FINAL_PUBLISH_PLAN.md`, `SSOT/SHIP_DAY_BRIEFING.md`,
`SSOT/drive-to-100.md`, older queue sections, and the pre-2026-08-03 content
formerly in this file are historical evidence. They do not override
`ops/PLAN.md`, the registry, or the current SSOT board.
