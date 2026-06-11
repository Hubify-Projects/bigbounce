# Security + Disaster-Recovery Audit — 2026-06-11

Scope: secret scan (bigbounce full git history + private trees), agent-instruction-file
backup coverage, restore story. All secret values in this file are redacted to
prefix + first chars + `…REDACTED`. No full secret appears anywhere in this document.

---

## Part 1 — Secret scan verdicts

Scanners: gitleaks/trufflehog not installed → manual `git log -S` pickaxe per key prefix
(full 2,224-commit history), deep `git log -p` grep over risky paths
(`tools/`, `h200_scripts/`, `recovered_pod_scripts/`, `*config*`, `*secret*`, `*.env*`),
`git grep` at HEAD, and recursive grep of live trees.
Patterns: `sk-ant-`, `sk-proj-`, `sk-[40+]`, `AIza`, `xai-`, `pplx-`, `ghp_`,
`github_pat_`, `rpa_`, `hf_[30+]`, `VERCEL_*=`, `BEGIN * PRIVATE KEY`,
`Bearer [30+]`, `password=`/`token=` long values.

| Location | Exposure | Verdict | Notes |
|---|---|---|---|
| `bigbounce` full history (2,224 commits) | PUBLIC repo | **CLEAN** | All pickaxe hits are docs/placeholders (`rpa_xxx_your_key`, redaction-pattern docs) or binary PDF byte coincidences (`xai-`, `hf_`). No real key values. |
| `bigbounce` HEAD + untracked worktree | PUBLIC | **CLEAN** | `.env`/`.env.local` never committed (verified via `git log --all -- .env*`: zero commits). Untracked files clean. |
| `~/.claude/scistack` | private | **CLEAN** | Only hit: `extensions/scientific-agent-skills/.../tests/test_redact.py` — fake test fixtures (`ghp_thesecret123…`, `sk-ant-xxx…`). |
| `~/agent-stack-backup` | private repo | **CLEAN** | Rescanned after coverage extension — still clean. |
| `~/Desktop/CODE_2025/hubify` | private repo | **CLEAN** | Worktree scan clean; 2 unpushed commits scanned clean before backup-branch push. |
| `~/.claude/skills` (symlink-following) | local | **CLEAN** | Only hits: `gstack/test/brain-sync.test.ts` + `redact-engine.test.ts` — fake fixtures for the redaction engine. |
| `~/.agent-shared` | local | **CLEAN** | No matches. |
| **Local git remote URLs** (`.git/config`) of `ceo-agents`, `lead-agents`, `ui-agents` | **LOCAL ONLY — never committed, never pushed** | **FOUND** | A live GitHub fine-grained PAT is embedded in the `origin` URL of all three disler clones: `github_pat_11ABZY…REDACTED`. Provider: GitHub. Not in any repo file, not in backup scope. |

### Rotate-list / required actions

1. **GitHub PAT `github_pat_11ABZY…REDACTED`** — embedded in 3 local `.git/config` remote
   URLs. Exposure is local-disk only (no commit, no push), so rotation is *recommended
   hygiene*, not emergency: rotate the PAT in GitHub settings, then re-set remotes to plain
   HTTPS URLs and let the macOS credential helper hold the token:
   `git -C <repo> remote set-url origin https://github.com/disler/<repo>.git`
2. **History rewrite needed: NO** — for any repo. Zero secrets in any committed history.
3. Optional: `brew install gitleaks` and add a pre-push hook on bigbounce (public repo).

---

## Part 2 — Instruction-file inventory + backup coverage

201 agent-instruction artifacts found (CLAUDE.md / AGENTS.md / SKILL.md / .cursorrules /
INDEX.md across `~/Desktop/CODE_2025`, `~/.claude`, `~/.agent-shared`, `~/.codex`, `~/.cursor`).

### By backing repo (push state at audit time)

| Class | Count | Detail |
|---|---|---|
| BACKED-PUSHED | 113 | gstack (55), scistack (20), bigbounce (5), youmd, myo, bamfaiapp, badapp, bamfos, bamfsite, foldermd, hubifycode, tipnes-ai, creator.new-old, disler clones, etc. — all `ahead=0` |
| BACKED-UNPUSHED → **pushed during audit** | 8 | `bamfaiapp-next` (1 commit → pushed to main), `hubify` (2 commits → see below) |
| BACKED-UNPUSHED → **flagged, not pushed** | 6 | `hubify-aios` (archived repo; its `origin` mis-points at the NEW `houstongolden/hubify.git` — pushing would pollute the live repo; fix remote before any push) |
| UNBACKED → **now covered by agent-stack-backup** | 81 | `~/.codex/AGENTS.md` + `~/.codex/skills/`, `~/.cursor/skills-cursor/` + `~/.cursor/skills/`, non-symlinked `~/.claude/skills/*` (qa, browse, ship, …), `~/.agent-shared/AGENTS.md`, `~/.claude/CLAUDE.md`, `CODE_2025/CLAUDE.md`, `packaging-to-figma/CLAUDE.md`, `CODE_2025/.dev-skills/` |

### hubify special case (private productization repo)

Local clone had 2 unpushed commits but `origin/main` is **1,059 commits ahead** (work is
happening on another machine/agent). A plain push was correctly rejected. The 2 local-only
commits (`77aab7a`, `e957181` — N.9 CLI bundle fix) are now safe on remote branch
**`backup/local-main-2026-06-11`**. Action for Houston: on this Mac,
`git pull --rebase` (or fresh clone) to catch up; the backup branch can be merged or
cherry-picked if N.9 isn't already upstream.

### sync-backup.sh coverage added (committed + pushed, repo is PRIVATE)

- ALL `~/.claude/projects/*/memory` dirs (8 projects; previously bigbounce only)
- `~/.codex/AGENTS.md` + `~/.codex/skills/` (explicitly NEVER `auth.json`/`config.toml` — they hold credentials)
- `~/.cursor/skills-cursor/` + `~/.cursor/skills/`
- `~/Desktop/CODE_2025/.dev-skills/`
- `packaging-to-figma/CLAUDE.md` → `project-claude-md/`

Backup run `357f5d3` committed and pushed (`ahead=0` verified). Post-run secret rescan
of the backup repo: CLEAN.

---

## Part 3 — One-command restore story

On a fresh Mac:

```bash
git clone git@github.com:houstongolden/agent-stack-backup.git ~/agent-stack-backup
```

That restores: global CLAUDE.md, CODE_2025 CLAUDE.md, all non-repo skills, codex/cursor
instruction surfaces, agent-shared, dev-skills, and all 8 project memories. Then clone the
self-remoted repos (scistack, gstack, bigbounce, hubify, youmd, …) per
`~/agent-stack-backup/MANIFEST.md`, and run `~/.claude/scistack/bin/sync-to-claude.sh` +
`~/Desktop/CODE_2025/sync-agent-configs.sh` to rebuild symlinks/mirrors. Secrets are
intentionally NOT in any backup — restore `.env.local` files from the credential manager.
