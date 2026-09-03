# Account separation — research (BigBounce + Hubify) on its own Claude account

Decision (Houston, 2026-09-03): run BigBounce and Hubify from a separate
Claude account so business/coding usage never stalls the research loop.

## What needs no migration (on disk / in git / external)
- Repos + `project-context/` (SSOT, VISION, NEXT_SCIENCE_LEDGER, handoffs,
  next-session prompts, CLAUDE.md directives, dispositions, review raws).
- `~/.claude/CLAUDE.md`, `~/.claude/skills/`, `~/.claude/scistack/`, gstack,
  You.md — filesystem, shared by every account on this machine.
- Project auto-memory: `~/.claude/projects/-Users-houstongolden-Desktop-CODE-YOU-bigbounce/memory/`
  (keyed by project path, not account).
- `.env.local` secrets; Convex, Vercel, GitHub, HF, B2, RunPod, Zenodo.

## What is account-bound
- Usage limits (the reason for the switch).
- Chat transcripts / `--resume` of old sessions — start cold from the
  next-session prompt; never paste old transcripts.
- Plan tier → model availability (Fable/Opus/Sonnet). Match the tier.
- Claude Code login on this machine (one login per config dir).

## Setup (one time)
Option A — shared config, switch logins: run `/login` in Claude Code when
switching accounts. Skills and memory stay shared automatically.

Option B (recommended) — parallel accounts, one config dir each:
```bash
mkdir -p ~/.claude-research
for d in skills scistack projects plugins; do ln -s ~/.claude/$d ~/.claude-research/$d; done
cp ~/.claude/CLAUDE.md ~/.claude-research/CLAUDE.md   # or symlink
CLAUDE_CONFIG_DIR=~/.claude-research claude            # log in with the research account
```
Add an alias (e.g. `alias claude-research='CLAUDE_CONFIG_DIR=~/.claude-research claude'`).
Verify on first launch: `CLAUDE.md` loaded, memory index present (`MEMORY.md`
pointers visible), skills listed, `bash bin/bigbounce-ready.sh` READY.

## First research session on the new account
1. `cd ~/Desktop/CODE_YOU/bigbounce && git pull --ff-only`
2. Paste `project-context/NEXT_SESSION_PROMPT_2026-09-03.md`.
3. Confirm the orchestrator reads `VISION.md` + `NEXT_SCIENCE_LEDGER.md` first
   (directive R) and applies directive N-AMENDED routing.

## Rule going forward
Git is the only handoff channel between accounts: every session ends with
`SESSION_HANDOFF_<date>.md`, the ledger, and the next-session prompt updated
and pushed. Business/coding work stays on the other account; do not mix.

## Status 2026-09-03 — Option B is SET UP on this Mac (orchestrator did it)
- `~/.claude-research/` created; symlinks → `~/.claude/{skills,scistack,projects,plugins,commands,settings.json}` and `CLAUDE.md → ~/.agent-shared/AGENTS.md`. No credentials in it yet (fresh login required). Smoke: `CLAUDE_CONFIG_DIR=~/.claude-research claude --version` → 2.1.258; memory index and 191 skills visible through the symlinks.
- `alias claude-research='CLAUDE_CONFIG_DIR=$HOME/.claude-research claude'` appended to `~/.zshrc` (open a new terminal or `source ~/.zshrc`).
- Your current login in `~/.claude` is untouched; both accounts can run at the same time. No logout, no Codex needed.

## When to switch (the good stopping point)
Switch after the phase-3 landing lane in the current session reports the pod
EXITED and the close-out is pushed (this session's final message says
"pod stopped"). Until then the current session owns the pod; starting the
research account earlier is harmless but would duplicate the watcher.

## The three commands you run (once)
```bash
source ~/.zshrc
cd ~/Desktop/CODE_YOU/bigbounce && git pull --ff-only
claude-research
```
Inside: `/login` with the research account (browser opens; sign in to the NEW
account). Then paste `project-context/NEXT_SESSION_PROMPT_2026-09-03.md`.
First-session checks: it should mention reading `VISION.md` and the ledger
first, `bin/bigbounce-ready.sh` should print READY, and `/memory` (or the
memory index in the system prompt) should list this project's memories.
For the business account keep using plain `claude` as before.
