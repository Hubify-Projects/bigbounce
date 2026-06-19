# CLAUDE.md — bigbounce

## Review-round site sync (STANDING, Houston 2026-06-11)

EVERY review round — internal (R-round, conf sweep, patch wave) AND external
(EXT round, gap-mine, closure wave, skill upgrade) — MUST add a timeline entry
to `site/src/data/reviewTimeline.ts` (+ extend `externalVerdictRounds`/
`gapSeries`/`skillsSeries` when the round produces those data) IN THE SAME
COMMIT BUNDLE as the round's artifacts. Houston tracks the program via
/reviews; a round that isn't on the timeline didn't happen. Every skill-upgrade
(new pattern, prompt rule, tool, protocol fix) gets its own kind:"skill-improvement"
entry. No batching, no deferring.

## Paper status — ALWAYS check SSOT first

Canonical status lives in `project-context/SSOT/`. Read in this order BEFORE any paper-related work:

1. `project-context/SSOT/index.md` — cross-paper dashboard (one-line per paper, readiness %, gaps)
2. `project-context/SSOT/paper-N/status.md` — per-paper detail + close-the-gap section
3. `project-context/SSOT/queue.md` — open tasks, owners, machine-checkable criteria

Do NOT rely on `CURRENT_STATUS.md`, `wiki/entities/paper-*.md`, or site HTML for paper status. Those mirror SSOT, never drive it.

`project-context/SSOT/drive-to-100.md` may have an active autonomous cron loop — check "Loop log" + exit criteria before doing parallel work on the same queue rows.

---

## CRITICAL RESEARCH DIRECTIVE

Never suggest "write up the results and publish" or "document the barriers as a paper" as a next step. After negative results, always propose the next research direction that could yield a positive discovery. Treat barriers as constraints that narrow the search space, not as conclusions. Continue researching until genuine positive results are found.

## Research stance

Bounce-model agnostic. Goal: prove bounce cosmology beats ΛCDM + inflation, not prove one specific bounce model. See `project-context/bounce_portfolio_strategy.md`.

## Author

- **Houston Golden** — houston@hubify.com
- **Site:** https://bigbounce.hubify.app
- **GitHub:** https://github.com/Hubify-Projects/bigbounce

---

## Protocols → skills, not inline

All recurring workflows are skills under `~/.claude/scistack/` (consolidated 2026-06-02).
Discover via `~/.claude/scistack/INDEX.md` or `~/.claude/skills/INDEX.md`.
Bigbounce-specific skills live at `~/.claude/scistack/astrostack/` (formerly in `bigbounce/.claude/skills/`).
Read `AGENT_RULES.md` for the methodology bible.

**Quick-pointer routing:**

| Trigger | Skill(s) to invoke |
|---------|---------------------|
| Compile a paper | `/paper-compile-revtex` → `/latex-audit` → `/artifact-link-verify` |
| Close an R-round | `/cross-vendor-r-round` → `/peer-review-truth-audit` → `/cascaded-r-rounds` |
| Run the design/visual round (96→98) | `/paper-design-round` (D-round: visual PDF pass; runs after R-rounds converge) |
| Run the final packaging round (98→99) | `/paper-packaging-round` (P-round: tarball + mirrors + artifact links + arXiv kit) |
| Bundle the round commit | `/pdf-restamp-bundle` |
| Run an experiment | `/houston-method-v2` (drives QC → analyze → expand → backup) |
| Update the website | `/bigbounce-site-sync` (same-commit dual sync: HTML + Next.js) |
| Bump a paper version | `/bigbounce-version-bump` + `/bigbounce-paper-pdf-mirror` |
| Replace a quantitative claim | `/bigbounce-claims-table-sync` |
| Drive-to-100 cron tick | `/drive-to-100-fire` |
| Update SSOT | `/ssot-update` |
| GPU inference | `/gpu-dataloader-pattern` + `/runpod-lifecycle` |
| Idle GPU | `/idle-gpu-rescue` |
| Before stopping pod | `/pod-backup-before-stop` (extends `/backup-3plus`) |
| Find an API key | `/env-local-discovery` (never ask Houston before checking) |
| Save Houston's message | `/prompt-history` (BEFORE the work, not after) |
| Save a new preference | `/memory-write` |
| Before closure commit (math claim diff) | `/never-fabricate-derivation` (pattern-036 prevention; hard gate inside `/paper-pre-review-check`) |
| Scistack housekeeping (end of session) | `/scistack-self-update` (sync + index + git status against `~/.claude/scistack`) |

**Readiness ladder** (hard gates, never skip a stage):
R-rounds converge → **96%** → D-round clean → **98%** → P-round bundle verified → **99%** → Houston sign-off → **100%**

Existing gstack skills that pair: `/latex-audit`, `/codex`, `/qa`, `/browse`, `/ship`, `/land-and-deploy`, `/canary`, `/investigate`, `/loop`, `/schedule`.

---

## Repo map

| Path | Purpose |
|------|---------|
| `arxiv/` | Paper sources (revtex4-2): P1A, P1B |
| `pipelines/p2_chirality/` | P4 source — galaxy chirality catalog |
| `pipelines/p3_anomaly_engine/` | P3 source — multi-survey anomaly catalog |
| `pipelines/p5_desi_chirality/paper/` | P5 source — DESI chirality |
| `research/focused_paper_source_integration/` | P2 source — f_NL forecast |
| `reproducibility/` | MCMC chains, Cobaya configs, gaps doc |
| `research/` | Active branches + dossier |
| `site/` | Next.js site (default at root, per `project_site_routing.md`) |
| `/old/` | Legacy static HTML, deprecated |
| `project-context/SSOT/` | Canonical paper status (read FIRST) |
| `project-context/peer-reviews/` | All review rounds + REVISION_TRACKER.md |
| `project-context/prompt-history.md` | Verbatim Houston brain dumps |

---

## Standing directives (non-negotiable)

All encoded as global skills under `~/.claude/scistack/hubstack/infra/` (symlinked into `~/.claude/skills/`):

- `/no-permission-loop` — never end with "want me to proceed?"
- `/hardest-path-first` — lead with Path C, alternatives labeled weaker
- `/no-future-work-defer` — classify every "future work" hit; default DO-NOW
- `/done-means-done` — real QA + real data + 2+ iterations
- `/backup-3plus` — 3 locations before any destructive op
- `/never-flip-prod-unverified` — visual check before vercel.json edits
- `/loop-model-routing` — Sonnet body / Opus judgment / Haiku polling
- `/parallel-subagents` — independent tasks → one-message parallel
- `/commit-message-atomic` — `feat(scope): …` / `chore(R{N}-stamp): …`
- `/readiness-cap-99` — 100% only with Houston's quote in SSOT

`AGENT_RULES.md` is the spec; the skills are the executables.

---

## Drive-to-100 loop (if active)

Cron `*/20 * * * *` fires `/drive-to-100-fire`. Each fire does ONE atomic step. See `project-context/SSOT/drive-to-100.md` for the plan + loop log.

Self-terminates when all 6 papers' exit criteria green AND Houston sign-off received in SSOT.

---

## .env.local

Secrets in `<repo-root>/.env.local` (gitignored). Includes `HF_TOKEN`, `OPENROUTER_API_KEY`, `ANTHROPIC_API_KEY`, `RUNPOD_API_KEY`, `VERCEL_*`, all pod SSH coords. Run `/env-local-discovery` before asking Houston for anything.

---

*Previous CLAUDE.md (380 lines) backed up to `project-context/CLAUDE.md.pre-slim-backup-2026-05-26`.*

<!-- convex-ai-start -->
This project uses [Convex](https://convex.dev) as its backend.

When working on Convex code, **always read `convex/_generated/ai/guidelines.md` first** for important guidelines on how to correctly use Convex APIs and patterns. The file contains rules that override what you may have learned about Convex from training data.

Convex agent skills for common tasks can be installed by running `npx convex ai-files install`.
<!-- convex-ai-end -->
