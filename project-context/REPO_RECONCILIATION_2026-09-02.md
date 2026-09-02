# Repo reconciliation — 2026-09-02

Scope: bigbounce + hubify. Non-destructive audit + cleanup. No pushes, no
force operations, no `git add -A`, no stash/reset that discards work.

## bigbounce (`/Users/houstongolden/Desktop/CODE_YOU/bigbounce`, branch `main`)

### 1. upstream/main divergence — brought forward

`upstream/main` (houstongolden/bigbounce) carried one commit not on
`origin/main`: `54057420` "Append 2026-08-28 cosmology research watch brief",
which appended a weekly-brief section (136 lines) to
`project-context/COSMOLOGY_RESEARCH_WATCH.md` that main's copy was missing.
Diffed the two versions (`git show upstream/main:...` vs the on-disk file);
main was byte-identical through line 160 and simply missing the append.
Appended the missing section (no merge commit; plain file edit + commit).

- **Disposition:** brought forward.
- **Commit:** `f4478028` — `docs: bring 2026-08-28 cosmology research watch
  brief from upstream/main (54057420)`
- upstream/main and origin/main otherwise remain divergent (origin/main is
  ~17+ commits ahead of the merge-base `54f10325`); no other upstream-only
  commits were found or needed.

### 2. Stale monolith retirement

`arxiv/main.tex` / `main.pdf` / `main.bbl` (untracked, gitignored) /
`main_arxiv_submission.tar.gz` were the June-2026 v2.3.18 unified monolith,
still carrying the superseded `f_NL = -35/8` matter-bounce value (the rest of
the repo moved to `-35/16` in the v110 text sweep — directive I6). The
registered, actively-maintained P1A source is `arxiv/paper1a_ech_nogo.tex`
(`project-context/paper_registry.json`). Its own submission tooling
(`README-SUBMISSION.txt`, `make_overleaf_zip.sh`, `compile_on_pod.sh` — all
titled/scoped to the monolith's "Geometric Dark Energy from Spin-Torsion
Cosmology" framing) was retired alongside it rather than repointed, since
every active paper now has its own tarball-based submission workflow (see
`arxiv/submission_tarballs/`).

- **Disposition:** `git mv` into `arxiv/_retired/` with a `README.md`
  explaining the retirement and pointing at the registered P1A source and
  `PORTFOLIO_DECISION_2026-09-02.md` §1.
- **Commit:** `2d93d0e4` — `chore(arxiv): retire stale v2.3.18 monolith
  main.tex to arxiv/_retired/`

### 3. Active-tooling reference audit

Grepped `tools/ bin/ scripts/ project-context/paper_registry.json
project-context/draft_paper_registry.json site/src/ README.md
RESUME_PROJECT_HERE.md projects.json paper.html activity.html versions.html
ssot.html data-explorer.html ~/.claude/scistack/` for `arxiv/main\.(tex|pdf)`.

| File | Hit | Action |
|---|---|---|
| `README.md` (compile-instructions example + "Adding a New Review" step 3) | `arxiv/main.tex`/`main.pdf`/`main.log` used as the worked example | **Fixed** — now uses `arxiv/paper1a_ech_nogo.tex` (registered P1A) and cites `paper_registry.json`; notes the monolith is retired |
| `~/.claude/scistack/hubstack/publishing/bib-tarball-rebuild/SKILL.md` | every code example hardcoded `arxiv/main.tex`/`main.bbl` | **Fixed** — parametrized to `$STEM` placeholder, instructs reading the registered stem from `paper_registry.json`. Committed in the scistack repo (`55b065e`) |
| `~/.claude/scistack/hubstack/learning-loop/peer-review-truth-audit/SKILL.md` | one illustrative table row cited `pdftotext arxiv/main.pdf` | **Fixed** — genericized to `arxiv/$PAPER.pdf`. Committed in the scistack repo (`55b065e`) |
| `RESUME_PROJECT_HERE.md` (`arxiv/main.tex` in a 4-paper-era table) | hit | **Left as-is** — file is explicitly self-labeled "frozen April 2026 machine-transfer snapshot... kept for historical reference only" with a banner pointing to SSOT for current truth |
| root `paper.html` (download-link `arxiv/main.pdf`/`main.tex`) | hit | **Left as-is** — part of the static root site; `netlify.toml` has `[[redirects]] from="/*" to="/404.html"`, i.e. this surface is wholesale dead/superseded by the Next.js `site/`. README.md's own outdated-section banner (line 69) independently confirms these root HTML files are deprecated |
| root `ssot.html`, `versions.html`, `activity.html`, `data-explorer.html` | multiple hits, mostly dated R-round log entries + a couple of "canonical source" status-table cells | **Left as-is** — same dead static-root-site reasoning as `paper.html`; the log entries are also historical record of rounds that genuinely ran against `main.tex` at the time |
| `projects.json` (`paper_file` array) | hit | **Left as-is** — unmaintained since 2026-03-29 (still shows the old 4-paper framing and `f_NL=-35/8`); part of the same dead static dashboard, out of scope to revive |
| `tools/`, `bin/`, `scripts/`, `site/src/`, both paper-registry JSONs | — | **No hits** |

- **Commit (bigbounce):** `a657dbb0` — `chore(review-tooling): point every
  active default at registered paper sources, not the retired monolith`
- **Commit (scistack, separate repo):** `55b065e`

No hit was left undecided; every one above has an explicit reasoned
disposition.

## hubify (`/Users/houstongolden/Desktop/CODE_YOU/hubify`, branch `main`)

`git fetch --all --prune` clean. Working tree clean, 0 stashes, 0 worktrees
besides the primary checkout.

### Branches

| Branch | Type | Disposition |
|---|---|---|
| `recovery/heuristic-franklin-uncommitted-20260826` (local) | single commit `7d45ecc7` "wip(recovery): preserve uncommitted Hubify module removals", 2026-08-26 | **Deleted (local only)**. The commit is a pure-deletion snapshot (49 files, 9,721 deletions, 0 insertions) of `modules-registry/{adversarial-review,backup-3plus,paper-pipeline,reproduce-verify}`, two `labs-registry/*.yaml` files, `postcss.config.mjs`, `turbo.json`, `.polish-allowed-known` — an in-progress uncommitted removal that was snapshotted before some prior reset/recovery. Verified every one of those paths still exists intact on current `main` (2026-09-02 HEAD), well after the 2026-08-26 snapshot and after `a67b80db` "chore(git): consolidate recovered Hubify focus-input branch" (2026-08-26) landed — i.e. the removal was abandoned, never applied, and holds no unique work relative to main. `git branch -D` used locally (git warned it wasn't merged to HEAD, which is expected since it's a deletion-only branch — the warning is about branch-ancestry bookkeeping, not lost content, given the content audit above). The remote copy `origin/recovery/heuristic-franklin-uncommitted-20260826` was **not** touched/deleted (no push, no remote branch deletion). |
| `dependabot/npm_and_yarn/mcp-server/{convex-1.45.0, dotenv-17.4.2, modelcontextprotocol/sdk-1.30.0, types/node-26.4.0, typescript-7.0.2}` (remote only) | 5 branches | **Left alone**, recorded as pending PRs (not merged): `gh pr list --state open` confirms all 5 are open PRs — #38 (convex 1.35.1→1.45.0), #39 (dotenv 16.6.1→17.4.2), #40 (@modelcontextprotocol/sdk 1.29.0→1.30.0), #41 (@types/node 22.19.17→26.4.0), #42 (typescript 5.9.3→7.0.2), all opened 2026-09-01. No merge action taken per instructions. |

### Worktrees / stashes / uncommitted changes

None found — clean tree, single worktree, empty stash list.

## Items I could not decide

None. Every branch/worktree/stash/uncommitted item and every active-tooling
hit above got an explicit, reasoned disposition.
