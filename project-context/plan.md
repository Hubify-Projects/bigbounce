<<<<<<< HEAD
# Plan

## Goal

Resume BigBounce from a truthful, clean main-branch checkpoint on another machine without losing the canonical SSOT workflow or leaking local environment material.

## Steps

1. Reconcile local main with `origin/main` under an explicit history-resolution decision; the handoff fetch found the histories divergent, so `git merge --ff-only` correctly refused to proceed.
2. Read `project-context/SSOT/index.md`, the affected paper's `status.md`, and `project-context/SSOT/queue.md` before selecting work.
3. Resume with Paper 1B's final independent confirmation spot-check; if any paper source changes, follow the required compile, visual LaTeX audit, artifact-link verification, SSOT, and same-commit site-sync protocols.
4. Preserve all evidence and use the highest-priority unblocked SSOT queue item after the confirmation work.

## Recovery Notes

- Last prompt-history audit: 2026-08-05 17:45 PT
- Current code delta: none beyond the context checkpoint. No paper, PDF, site, or API change was made during this handoff.
- Environment backups are local secret-bearing artifacts, not source control. Restore them through the encrypted environment-vault workflow.
- Fetch evidence: `origin/main...HEAD` = 1,574 commits remote-only / 2 commits local-only. No merge, rebase, reset, force-push, or alternate-branch push was performed.
=======
# BigBounce recovery plan

**You.md/project-context entry point · reconciled 2026-08-04**

The canonical executable plan is [`../ops/PLAN.md`](../ops/PLAN.md). This file
is the compact recovery map for a newly resumed agent or a You.md context sync;
it must not become a second planning authority.

## Recover in this order

1. Read [`../ops/PLAN.md`](../ops/PLAN.md) for the current phase and priorities.
2. Read [`PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md`](PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md)
   for the approved scientific-purpose map and editorial decisions.
3. Read [`paper_registry.json`](paper_registry.json) for the six preserved
   candidate identities, paths, and provisional venues.
4. Read [`SSOT/index.md`](SSOT/index.md), then the relevant
   `SSOT/paper-*/status.md`, for current versions and honest limitations.
5. Read [`SSOT/queue.md`](SSOT/queue.md) for executable work.
6. Read [`peer-reviews/REVISION_TRACKER.md`](peer-reviews/REVISION_TRACKER.md)
   and the linked truth audits only when review evidence is needed.
7. Compare Convex and `site/src/data/` against the SSOT before making a public
   status claim.

## Current objective

Ship the approved three-program map—bounce theory, DESI anomaly discovery, and
galaxy chirality—with primary science separated from theory notes, software,
technical data products, and companions. Preserve all finished candidate
packages while removing the old six-equal-papers framing.

The immediate scientific task is to reconcile the surviving original DESI
anomaly artifacts and claims. Current P3 r17 is the integrated supporting
public-ID/provenance release, not the anomaly flagship. P5 is a standalone AJ
companion to P4.

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
>>>>>>> origin/main
