# AGENT ONBOARDING — run the bigbounce scientific paper-review loop on any machine

**You are** a Claude Code or Codex agent picking up Houston's bigbounce cosmology
paper program on a (possibly new, always-on) machine. This file is your single
entry point. Read it top to bottom once, then keep the loop going.

**The mission:** drive 6 physics papers (P1A, P1B, P2, P3, P4, P5) to
publication-ready through an iterative internal + external peer-review loop,
fixing every finding, and keeping the public lab site (https://bigbounce.hubify.app)
perfectly in sync after every round.

> ⚠️ **CURRENT STATE (2026-06-21): IN-REVISION, not done.** Houston ran an
> external review using the live PDFs + the exact per-paper prompts on the site
> and found **open BLOCKER / MAJOR / MINOR revisions** across the papers. The
> readiness is rolled back to **92** to reflect this. **Your P0 is to intake those
> findings** (Houston will paste them, or they'll be in `project-context/peer-reviews/`),
> truth-audit them, and run the closure loop. Do NOT claim any paper is done or
> submit anything until the loop re-converges AND Houston signs off.

---

## ▶︎ When Houston says "START EVERYTHING UP"
Run this, then begin the loop:
```bash
# refresh everything that travels across machines
git -C ~/Desktop/CODE_2025/bigbounce pull --ff-only
git -C ~/.claude/scistack pull --ff-only && ~/.claude/scistack/bin/sync-to-claude.sh
git -C ~/.agent-shared pull --ff-only && ~/.agent-shared/bin/sync-agent-shared.sh
~/.agent-shared/bin/restore-claude-memory.sh        # rehydrate durable preferences
# secrets: restore .env.local from the You.md Secret Vault (16 projects / 451 vars) — or password manager
you env vault pull --restore --root ~/Desktop/CODE_2025 --map-existing --existing-only --skip-agent-auth || echo "⚠️ fill .env.local from .env.example manually"
# (optional, interactive) register the repos in You.md projects — run once at a terminal, accept the 2 prompts:
#   for d in ~/Desktop/CODE_2025/bigbounce ~/.claude/scistack ~/.agent-shared; do (cd "$d" && youmd project init); done
```
Then: read `project-context/SSOT/index.md` (top banner = current state) → **intake Houston's latest external-review findings** (newest EXT round in `project-context/peer-reviews/` or he pastes them) → run the next R/D/P round (§4) → sync the site same-commit (§5) → `git push`. That's the loop. Keep going until it reconverges + Houston signs off. **At the end of a working session, run `~/.agent-shared/bin/backup-claude-memory.sh` + commit/push agent-shared** so any new memories travel.

## 0. The 3 files that define everything
1. **`CLAUDE.md`** (repo root) — routing table + standing directives. Auto-loads for Claude Code.
2. **`AGENT_RULES.md`** (repo root) — the methodology bible (the full spec).
3. **This file** — the operational runbook. (Codex: also read `AGENTS.md`, which points here.)

Canonical paper status lives in **`project-context/SSOT/`** and **Convex** — never trust a number in a `.tex` comment, `papers.ts`, or the site HTML over those.

---

## 1. New-machine bootstrap (one-time)
```bash
# 1. Repos  (bigbounce is PUBLIC; scistack + agent-shared are PRIVATE — run `gh auth login` first)
git clone https://github.com/Hubify-Projects/bigbounce.git ~/Desktop/CODE_2025/bigbounce  # KEEP THIS PATH (memory restore is path-keyed)
git clone https://github.com/Hubify-Projects/scistack.git ~/.claude/scistack               # the science SKILLS (hubstack + astrostack)
git clone https://github.com/houstongolden/agent-shared.git ~/.agent-shared                # global CLAUDE.md (symlinked) + shared skills + your agent MEMORY
# (gstack skills come with the Claude Code install; see ~/.claude/skills/)

# 2. Skills + global config + memory
~/.claude/scistack/bin/sync-to-claude.sh && ~/.claude/scistack/bin/build-index.sh   # expose /paper-design-round, /cross-vendor-r-round, etc.
~/.agent-shared/bin/sync-agent-shared.sh                                            # shared skills + link global ~/.claude/CLAUDE.md → agent-shared/AGENTS.md
~/.agent-shared/bin/restore-claude-memory.sh                                        # rehydrate Houston's 100+ durable preference memories (NOT in any other sync)
cp ~/.agent-shared/agent-config/claude-settings.reference.json ~/.claude/settings.json   # optional: same plugins / youmd MCP / high-effort

# 3. Toolchain
brew install --cask mactex-no-gui      # or basictex; needs pdflatex, latexmk, bibtex
brew install poppler                    # pdftoppm/pdftotext/pdfinfo (used by the review tool + audits)
brew install bun node                   # site (Next.js 16 + Convex)
pip install -r requirements.txt         # python review tooling (see §2 for the full vendor-SDK list)
cd site && bun install && cd ..
npm i -g convex                          # Convex CLI (npx convex works too)

# 4. Secrets — fill the template, NEVER commit the result
cp .env.example .env.local              # then paste real keys (Houston has them / password manager)
```
For the *generic* cross-machine skill/stack/env sync, the skill is **`/machine-sync`** (and `/agent-stack-sync` for shared multi-agent config). Use it; this section is the bigbounce-specific delta.

---

## 2. The review tooling (the engine of the loop)
- **`tools/v3_native_pdf_review.py <pdf> <round_label> <paper_tag> "<context>"`** — fires a TRUE native-PDF review at 4 vendors (OpenAI o3, Gemini 2.5 Pro, Grok 4 [rasterized], Perplexity [text+web]), 2-pass self-critique, writes `project-context/peer-reviews/<round>_<tag>_<vendor>.md`. The **Anthropic/Claude leg is skipped by default** (key often credit-exhausted) — supply it with a Claude Code **Opus sub-agent** reviewer instead (this is the standing pattern; see `feedback_claude_reviewer_via_subagent`).
- **Vendor SDK deps** the tool needs (beyond `requirements.txt`): `pip install openai google-generativeai`. `anthropic` is in requirements. Grok uses `pdftoppm` (poppler). Keys come from `.env.local` (`source` it before running; never print values).
- **Skills that wrap the loop** (all in `~/.claude/scistack/hubstack/`):
  `/cross-vendor-r-round` → `/peer-review-truth-audit` → `/bigbounce-truth-audit` → `/bigbounce-close` (R-round science);
  `/paper-design-round` (D-round visual) → `/paper-packaging-round` + `/site-cohesion-sweep` (P-round);
  `/r-round-finding-archive` → `/r-round-pattern-mine` → `/paper-pre-review-check` (the self-improving loop).

---

## 3. The round ladder (R → D → P) and readiness
Papers climb a phase ladder; the **readiness number is computed in `convex/papers.ts`** from open findings, ceilinged per phase:

| Phase | What it attacks | Skill | Ceiling |
|---|---|---|---|
| **R-round** | science correctness (INT multi-model + EXT referee) | `/cross-vendor-r-round` | 96 |
| **D-round** | visual/camera-ready presentation (read RENDERED pages) | `/paper-design-round` | 98 |
| **P-round** | packaging: tarball, mirrors, HF/GitHub/Zenodo artifacts, site cohesion | `/paper-packaging-round` + `/site-cohesion-sweep` | 99 |
| sign-off | Houston only — records the final 1% | — | 100 |

**INT vs EXT:** INT = a round *you* run (multi-model via the tool). EXT = a fresh-referee round (Houston pastes the live PDF + the on-page prompt into ChatGPT/Grok/Gemini, OR `/external-review-browser-loop`). **Houston's EXT rounds reliably catch what INT misses** — never declare done on INT alone. Every finding goes through `/peer-review-truth-audit` BEFORE any closure (reviewers over-call on stale/mislabeled artifacts; ~half are FALSIFIED).

---

## 4. Run ONE round end-to-end (the core cycle)
1. **Pick the paper(s) + the canonical PDF** (resolve via `SSOT/paper-N/status.md`; PDFs live in `arxiv/`, `pipelines/p2_chirality/`, `pipelines/p3_anomaly_engine/`, `pipelines/p5_desi_chirality/paper/`, `research/focused_paper_source_integration/`).
2. **Dispatch** INT (the tool, 4 vendors, background) + spawn Opus sub-agent reviewers (the Claude leg; for D-rounds they must READ THE RENDERED PDF PAGES AS IMAGES, not the .tex).
3. **Truth-audit** every finding → VERIFIED / FALSIFIED / STALE / OUT-OF-SCOPE / OPINION (one Opus agent per paper).
4. **Close** the VERIFIED-OPEN ones (Sonnet agents): edit `.tex` (NO fabricated derivations — `/never-fabricate-derivation`), bump version, recompile (`latexmk -pdf`), `/latex-audit`, verify 0 undef refs.
5. **Re-review** (cascade) until convergent-clean per `/cascaded-r-rounds`.
6. **Archive + pattern-mine** the findings (self-improving loop).
7. **Sync the site SAME COMMIT** (§5).

Model routing: **Opus** for truth-audits/judgment/closure-decisions; **Sonnet** for well-specified edits/recompiles/packaging; fan out one agent per paper in parallel.

---

## 5. Update the site after EVERY round (non-negotiable, SAME COMMIT)
Houston tracks the program via the live site's /reviews + /status pages. A round that isn't on the site **didn't happen**.
- **`site/src/data/reviewTimeline.ts`** — add a timeline entry for the round (+ extend `externalVerdictRounds`/`gapSeries` when relevant). Every skill upgrade gets a `kind:"skill-improvement"` entry.
- **`site/src/data/papers.ts`** + **`live-status.ts`** — version, pages, pdfMeta, readiness, artifacts[]. Keep strings ONE LINE.
- **`project-context/SSOT/`** — `index.md` (top dashboard comment), `paper-N/status.md`, `queue.md`.
- **Convex** — `npx convex run papers:bump...` so the live per-paper readiness recomputes.
- **Mirror PDFs** to `site/public/papers/` (canonical + versioned filenames; md5-verify).
- **Rebuild the arXiv tarball** (`/bib-tarball-rebuild`) into `project-context/SSOT/arxiv_tarballs/`; standalone-compile-verify.
- Skills that do this in one shot: `/bigbounce-post-bump-sync`, `/bigbounce-site-sync`, `/bigbounce-paper-pdf-mirror`.

**Deploy = `git push origin main`** → Vercel auto-builds. Always `curl` a new versioned PDF + the homepage afterward to confirm 200.

---

## 6. Operational gotchas (hard-won — read these or repeat my mistakes)
1. **The context-sync cron auto-commits the working tree every ~2 min but NEVER pushes.** `git status` can look clean even right after you edit (it's in an earlier cron commit). Verify edits by grepping the file on disk, and **`git push` manually** to deploy. Check `git rev-list --count origin/main..HEAD` before declaring shipped. (`project_context_sync_cron_no_push` memory.)
2. **Convex has TWO deployments; the SITE reads the one in `NEXT_PUBLIC_CONVEX_URL` = `brilliant-panther-471` (the "dev" one).** `npx convex deploy` targets a DIFFERENT prod deployment the site does NOT read. To change live readiness/functions, edit `convex/papers.ts` then **`npx convex dev --once`** (pushes to the deployment the site reads). `npx convex run ...` (no `--prod`) also targets that one.
3. **Figure regen desync:** figure scripts often write to `figures/` but the `.tex` `\includegraphics` reads from `paper/` — sync regenerated PNGs into the tex's dir or the fix never reaches the PDF (`dpattern-figure-dir-desync`). Always pdftoppm + visually confirm regenerated figures landed.
4. **pdftotext review artifacts:** vendor reviewers fed extracted text hallucinate "broken equations / truncated labels / missing subscripts" that are fine in the rendered PDF. Truth-audit against the RENDER, not the text dump.
5. **HF token = the `bamfai` account** (not `Hubify` org). Public datasets/models live under `bamfai/`. Paper reproducibility datasets: `bamfai/p1b-{alp-chains,mcmc-diagnostics,namaster-artifacts}`, `bamfai/bigbounce-anomaly-catalog`, `bamfai/galaxy-chirality-catalog`, model `bamfai/galaxy-chirality-v2`.
6. **Readiness is computed, not hand-set** — change it via findings or the ceiling in `convex/papers.ts`, not by editing a number. Cap at 99 (sign-off=100); roll BACK after every round that finds issues (`feedback_readiness_oscillation`).

---

## 7. Standing rules (the non-negotiables — full list in CLAUDE.md / AGENT_RULES.md / the memory dir)
- Truth-audit BEFORE closure; never fabricate a derivation; take critiques seriously (full hard fix, not caveat-dodge).
- Never claim N4 novelty (ceiling N3). PST timestamps. revtex4-2. `\artifact{}` macro for repo paths; `table*`/`figure*` for wide content.
- Same-commit site sync; atomic conventional commits; commit autonomously when verified.
- No "future work" deferrals (do-now); no permission-loops; backup 3+ locations before destructive ops.
- The agent memory dir (`~/.claude/projects/.../memory/MEMORY.md` + files) holds Houston's durable preferences — read it.

---

## 8. Pick up the loop NOW
1. Read `SSOT/index.md` (dashboard) + this file's CURRENT STATE banner.
2. **Intake Houston's 2026-06-21 external-review findings** (he'll provide them, or check `project-context/peer-reviews/` for the newest EXT round). Truth-audit → close → re-review → site-sync.
3. Continue R→D→P until convergent-clean, then surface the Houston gates (ORCID public flip `0009-0008-3617-8729`, sign-off, arXiv submit P4→P1A→P1B→P3→P2→P5, mint DOIs).
4. Keep the site current after every single round. That's the job.
