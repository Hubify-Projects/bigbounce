# Branch and worktree consolidation record — 2026-08-03

**Purpose.** Topology evidence, disposition rationale, and the completed
consolidation receipt. The canonical research state remains `main` plus
SSOT/Convex.

## Completed outcome — 2026-08-03

- `main`, `origin/main`, and `upstream/main` all resolve to
  `2be3964b22301b2408f74945a2c169843de6c033`.
- Archival merge `556b8454` makes every formerly divergent local/remote branch
  tip reachable from `main` without applying any superseded branch tree over
  the current canonical tree. This preserves unique P1-unification, cubic
  bounce, architecture, legacy-site, and RunPod history for later selective
  review.
- All non-`main` branches were removed from both GitHub remotes after ancestry
  verification. All eight obsolete local branches and their two clean linked
  worktrees were removed after the same verification.
- The personal fork's stalled pack upload was replaced by a fast-forward
  GitHub ref update; no force update was used.
- Open GitHub pull requests remained zero. The five untracked local skill
  mirrors remain deliberately untouched because Scistack is canonical and
  three local copies are stale or divergent.

The remaining sections preserve the **pre-action snapshot and analysis** that
justified this outcome. References to preserving branches/worktrees below are
historical guardrails, not current state.

## Snapshot and remotes

| Item | Evidence |
| --- | --- |
| Canonical local/Origin head at snapshot | `main` = `origin/main` = `41bcb15ba18549fda984b16c7aabc6add7d78283`; `git rev-list --left-right --count origin/main...HEAD` = `0 0` |
| `origin` | `https://github.com/Hubify-Projects/bigbounce.git`; `origin/HEAD -> origin/main` |
| `upstream` | `https://github.com/houstongolden/bigbounce.git`; cached `upstream/main` = `41749e5c`; `main...upstream/main` = `3754 6` (diverged, never merge blindly) |
| GitHub | `gh pr list --state open` returned none; repository Issues are disabled |
| Tags | 126; newest safety tag is `safety/pre-hubify-lab-2026-07-23` at `702c0488` |

The root worktree was intentionally not cleaned: `project-context/prompts.md`
is modified and the five `.agents/skills/bigbounce-*` directories below are
untracked.  They are outside this record's commit.

## Refs already contained by `main`

The following had zero commits in `main..<ref>` at the snapshot.  They are
historical pointers, not merge candidates: local
`ca-round-closure-2026-07-09` (`52639606`),
`dround-final-polish-p4-p2` (`39f380e5`, upstream gone),
`p1a-fierz-lemma-proof` (`6fb3a1e6`),
`realwork-retest-p2-p3-closure-2026-07-07` (`43bd1448`, upstream gone), and
`worktree-agent-a8486efdcbf3f911f` (`617940ec`).  The equivalent contained
origin refs are `ca-round-closure-2026-07-09`,
`claude/hubify-bounce-research-impact-ipbxef`,
`claude/paper-editing-checklist-011CV1bWpmKWiFGRBzLiVYhr`, `p3-desi-injrec`,
`squad/literature-review-big-bounce-cosmology`,
`w1-ext-adjudication-2026-07-11`, and
`worktree-agent-a8486efdcbf3f911f`.

## Non-contained work: do not merge whole branches

All comparisons use `git cherry -v main <ref>` and blob checks against `main`.
`+` means no patch-identical commit on main; it is not evidence that the change
is scientifically valid or still desired.

| Ref / unique commit(s) | Classification versus `main` | Safe disposition |
| --- | --- | --- |
| `worktree-agent-ae5e7eab3fb9e3fda` / `cdaced92` | **Genuinely unique patch.** P1 unification proposal; `MERGE_PROPOSAL.md`, `paper1_unified.tex`, and PDF exist on main but differ. The canonical program still names separate P1A/P1B sources. | Preserve linked worktree; accept only after an SSOT-level decision to unify P1 and an exact-artifact review. |
| `merge/p1-unified` / `8d3d82ba` | **Genuinely unique patch, evolved paths.** Fierz script and two review artifacts exist on main but all blobs differ; no patch-equivalent commit. | Science/code review and a bounded cherry-pick or manual port; never merge this old branch wholesale. |
| `origin/research/cubic-bounce-transmission-p2` / `aaf43f19`, `4ee1fc5f` | `aaf43f19` is **patch-equivalent/already integrated** (`git cherry` `-`). `4ee1fc5f` is **genuinely unique**: seven `research/cubic_bounce_transmission/` files are absent from main. | Archive the integrated paper/mirror commit; independently truth-audit the remaining calculation before selectively importing code/results and regenerating current P4 artifacts. |
| `origin/claude/audit-product-architecture-2wbGX` / `7335973a..c7a8b8aa` | **Partly equivalent, partly evolved.** `HUBIFY_HANDOFF.md` and both audit receipts are byte-identical on main; `RESEARCH_ARCHITECTURE.md` differs. | Keep for documentation comparison; port only deltas still relevant to current architecture. |
| `origin/claude/scientific-paper-revisions-011CV2bvaDdmDRPD8mTUS3Mm` / `dad47f4f` | **Unique patch but operationally superseded.** It changes deprecated `index.html`/`bigbounce-md.html`, whose current blobs differ. | Do not merge; retain as historical reference unless legacy static hosting is explicitly revived. |
| `origin/claude/verify-runpod-queue-ViFqr` / `ebc56521` | **Genuinely unique patch, evolved paths.** The three RunPod/monitor files exist but differ and have no patch-equivalent commit. | Review independently for current credentials, backup policy, and scheduler compatibility; selectively port only tested improvements. |

`origin/merge/p1-unified` duplicates local `merge/p1-unified`; and
`origin/worktree-agent-ae5e7eab3fb9e3fda` duplicates the linked-worktree head.

## Linked worktrees

| Path | Branch / head | Snapshot cleanliness | Disposition |
| --- | --- | --- | --- |
| repository root | `main` / `41bcb15b` | modified prompt file plus five untracked skill dirs | Preserve; this map must not absorb those changes. |
| `.claude/worktrees/agent-a8486efdcbf3f911f` | `worktree-agent-a8486efdcbf3f911f` / `617940ec` | clean; fully contained by main | Do not remove until its owner confirms no active process uses it. |
| `.claude/worktrees/agent-ae5e7eab3fb9e3fda` | `worktree-agent-ae5e7eab3fb9e3fda` / `cdaced92` | clean; one unique P1 proposal commit | Preserve pending the P1 scope decision. |

## Untracked local skill mirrors

These are untracked local copies of canonical Scistack skills under
`~/.claude/scistack/astrostack/`; Scistack is the source of truth.  Do not
delete or commit them as a second canonical implementation.

| Directory | SHA-256 relation to canonical `SKILL.md` | Provenance and disposition |
| --- | --- | --- |
| `bigbounce-paper-pdf-mirror` | identical: `20e8aa9e...a065b4` | Generated/local mirror of canonical source; retain locally or regenerate via Scistack sync, but do not version here. |
| `bigbounce-revision-tracker` | identical: `820f8679...ad110d` | Generated/local mirror; same disposition. |
| `bigbounce-claims-table-sync` | differs: local `f0837e65...8af2`, canonical `705b2427...093d` | Local copy only swaps `CLAUDE.md` for `AGENTS.md` in source references. Noncanonical; reconcile upstream only through Scistack's skill-governance process. |
| `bigbounce-site-sync` | differs: local `ee7f0b5e...c1854`, canonical `7dbbb03d...a53e7` | Local copy omits the canonical Convex HTTP/API and directive-G PDF-hygiene sections. Treat as stale/unsafe; do not use or commit it. |
| `bigbounce-version-bump` | differs: local `a7cb8e63...9c59f`, canonical `53f505fb...4ec` | Local copy omits the provenance/artifact-crosscheck gate. Treat as stale/unsafe; do not use or commit it. |

## Later consolidation and archive/delete gate

1. Pause concurrent writers and capture a fresh `git status`, `git worktree
   list`, and remote-ref snapshot.  First preserve the root's independent
   prompt/skill changes in their own reviewed commit or a separately named
   worktree; do not combine them with branch consolidation.
2. From current `origin/main`, create an integration branch per surviving item
   and use only selective cherry-picks/manual ports.  For scientific/PDF work,
   pass truth-audit, compile, directive-G mirror/md5 checks, SSOT/Convex/site
   sync, and review before integration.
3. A contained ref may be archived/deleted only when (a)
   `git merge-base --is-ancestor <ref> main` succeeds, (b) it has an immutable
   archive tag or a reachable main commit, (c) no open PR references it, and
   (d) `git worktree list` has no linked checkout of it.  Require clean status
   from any affected worktree and owner confirmation before removing a path.
4. A non-contained ref may be archived/deleted only after every unique commit
   is either integrated and verified or preserved by an immutable archive tag,
   its acceptance/rejection is recorded in SSOT or this record, its remote
   reference is rechecked, and the linked-worktree conditions in step 3 hold.
