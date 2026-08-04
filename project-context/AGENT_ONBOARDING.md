# AGENT ONBOARDING — run the bigbounce scientific paper-review loop on any machine

**You are** a Claude Code or Codex agent picking up Houston's bigbounce cosmology
paper program on a (possibly new, always-on) machine. This file is your single
entry point. Read it top to bottom once, then keep the loop going.

**The mission:** publish the strongest coherent research portfolio, organized
by scientific question rather than an inherited count. Six candidate packages
are preserved, but current P3 and P5 are under editorial review and the missing
DESI anomaly-discovery science must be reconciled. Keep the public lab site
(https://bigbounce.hubify.app) honest and synchronized after approved rounds.

> **CURRENT STATE (2026-08-03): PUBLICATION-ARCHITECTURE HOLD.** Read
> `project-context/PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md` first. The six
> Directive-P candidate states are preserved as technical evidence, not as an
> instruction to submit six equal papers. Do not submit, seek endorsements,
> mint new P4/P5 records, or push a six-equal-papers site framing until Houston
> approves or revises the map. Current P3 is a technical public-ID recovery
> output, not the missing anomaly-discovery paper.
>
> **HOW to run any bounded further round:** the canonical spec is
> `~/.claude/scistack/astrostack/bigbounce-r-round/SKILL.md` (all-vendor INT matrix,
> headed-browser EXT save-then-advance, per-finding truth-audit, directive-G, gate H).
> If any doc disagrees with it, the canonical spec wins. Never fake an ACCEPT; never
> fabricate; every verdict traceable to raw text.
---

## ▶︎ When Houston says "START EVERYTHING UP"
Run this, then begin the loop:
```bash
# refresh everything that travels across machines
git -C ~/Desktop/CODE_YOU/bigbounce pull --ff-only
git -C ~/.claude/scistack pull --ff-only && ~/.claude/scistack/bin/sync-to-claude.sh
git -C ~/.agent-shared pull --ff-only && ~/.agent-shared/bin/sync-agent-shared.sh
~/.agent-shared/bin/restore-claude-memory.sh        # rehydrate durable preferences
# secrets: restore .env.local from the You.md Secret Vault (16 projects / 451 vars) — or password manager
you env vault pull --restore --root ~/Desktop/CODE_YOU --map-existing --existing-only --skip-agent-auth || echo "⚠️ fill .env.local from .env.example manually"
# (optional, interactive) register the repos in You.md projects — run once at a terminal, accept the 2 prompts:
#   for d in ~/Desktop/CODE_YOU/bigbounce ~/.claude/scistack ~/.agent-shared; do (cd "$d" && youmd project init); done
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
git clone https://github.com/Hubify-Projects/bigbounce.git ~/Desktop/CODE_YOU/bigbounce  # canonical path (memory restore is path-keyed)
# Legacy CODE_2025 compatibility (never overwrite an existing checkout):
mkdir -p ~/Desktop/CODE_2025
[ -e ~/Desktop/CODE_2025/bigbounce ] || ln -s ~/Desktop/CODE_YOU/bigbounce ~/Desktop/CODE_2025/bigbounce
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
- **`tools/v3_native_pdf_review.py <pdf> <round_label> <paper_tag> "<context>"`** — fires API reviews at Gemini, Grok, and optional Perplexity, with 2-pass self-critique. The OpenAI perspective is supplied by the authenticated Codex CLI/ChatGPT subscription, **never the OpenAI API**. Anthropic/Claude is disabled for the active campaign.
- **Vendor SDK deps** the active tool needs (beyond `requirements.txt`): `pip install openai google-generativeai`; the OpenAI SDK is used only as a protocol client pinned to xAI/Perplexity base URLs. Grok uses `pdftoppm` (poppler). Keys come from `.env.local` (`source` it before running; never print values).
- **Skills that wrap the loop** (all in `~/.claude/scistack/hubstack/`):
  `/cross-vendor-r-round` → `/peer-review-truth-audit` → `/bigbounce-truth-audit` → `/bigbounce-close` (R-round science);
  `/paper-design-round` (D-round visual) → `/paper-packaging-round` + `/site-cohesion-sweep` (P-round);
  `/r-round-finding-archive` → `/r-round-pattern-mine` → `/paper-pre-review-check` (the self-improving loop).

---

## 3. The round ladder (R → D → P) and readiness
Papers climb a phase ladder; the **readiness number is computed in `convex/papers.ts`** from open findings, ceilinged per phase:

| Phase | What it attacks | Skill | Ceiling |
|---|---|---|---|
| **R-round** | science correctness (INT all-vendor matrix + EXT headed-browser referee) | **`/bigbounce-r-round`** (canonical; wraps `/cross-vendor-r-round` INT + `/external-review-browser-loop` EXT) | 96 |
| **D-round** | visual/camera-ready presentation (read RENDERED pages) | `/paper-design-round` | 98 |
| **P-round** | packaging: tarball, mirrors, HF/GitHub/Zenodo artifacts, site cohesion | `/paper-packaging-round` + `/site-cohesion-sweep` | 99 |
| sign-off | Houston only — records the final 1% | — | 100 |

**INT vs EXT:** INT = a round *you* run (multi-model via the tool). EXT = a fresh-referee round (Houston pastes the live PDF + the on-page prompt into ChatGPT/Grok/Gemini, OR `/external-review-browser-loop`). **Houston's EXT rounds reliably catch what INT misses** — never declare done on INT alone. Every finding goes through `/peer-review-truth-audit` BEFORE any closure (reviewers over-call on stale/mislabeled artifacts; ~half are FALSIFIED).

---

## 4. Run ONE round end-to-end (the core cycle)

> **THE canonical, always-current spec for HOW to run an INT/EXT round is the
> `/bigbounce-r-round` skill** (`~/.claude/scistack/astrostack/bigbounce-r-round/SKILL.md`), subject to Houston's permanent override that OpenAI review uses Codex CLI/ChatGPT subscription only, never API billing.
> It is the single source of truth for: INT vendor legs (OpenAI via Codex
> CLI/ChatGPT subscription with API keys
> unset; Grok API; Gemini API-when-billed-else-browser) + the ALL-VENDOR INT verdict
> matrix; EXT (headed browser ChatGPT+Grok+Gemini, raw text + screenshot
> saved-then-verified per leg); per-finding source-cited truth-audit; directive-G
> PDF hygiene; Convex/site/SSOT/timeline sync; and the directive-H convergence
> gate. Read it before running a round; the summary below is orientation only.

1. **Pick the paper(s) + the canonical PDF** (resolve via `SSOT/paper-N/status.md`; PDFs live in `arxiv/`, `pipelines/p2_chirality/`, `pipelines/p3_anomaly_engine/`, `pipelines/p5_desi_chirality/paper/`, `research/focused_paper_source_integration/`). Recompile+mirror FIRST if the served PDF lags the source.
2. **INT** (§1 of `/bigbounce-r-round`): OpenAI via authenticated Codex CLI/ChatGPT subscription + Grok API + Gemini API (when billed; otherwise browser EXT). OpenAI API billing and Anthropic/Claude are disabled. Report every available active vendor column.
3. **EXT** (§2): headed browser (`$B cleanup && $B connect`, confirm `Mode: headed`) → ChatGPT + Grok + Gemini (houston@bamf.com Ultra); NEVER skip ChatGPT; save raw verbatim + screenshot per leg to `project-context/peer-reviews/EXT_real/` the instant each completes.
4. **Truth-audit** every INT and EXT non-minor finding → source-cited disposition (patterns 061-066: disclosed-re-flag / scope / referee-variance / GENUINELY-NEW-REAL → close). Use a fresh policy-compliant high-judgment agent per paper. NO fabricated derivations (`/never-fabricate-derivation`); verify every real computation before applying.
5. **Close** VERIFIED-NEW-REAL items with bounded execution workers: edit `.tex`, directive-G hygiene (bump version+date, recompile `latexmk -pdf` 0 undef-refs, `/latex-audit`, mirror byte-identical to ALL served paths, three-way md5 check), Convex sync.
6. **Re-review** (cascade) until the directive-H gate holds per `/cascaded-r-rounds`; run `/review-integrity-audit` (GENUINE not ENGINEERED) before declaring converged.
7. **Archive + pattern-mine** (self-improving loop). **Sync the site SAME COMMIT** (§5).

Model routing: use the active frontier Codex director for truth-audits/judgment,
policy-compliant Codex workers for bounded edits/recompiles/packaging, and fan
out one owner per non-overlapping paper. Anthropic/Claude is disabled.

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
2. **Two DIFFERENT bigbounce-named Convex projects exist — don't confuse them:**
   - **`brilliant-panther-471`** (project `bigbounce-e6d13`, the *dev* deployment) = **THE canonical research/paper DB for THIS repo.** It holds papers, paperVersions, rRounds, externalReviews, findings, mcmcStatus, pods, galaxies, models, analytics, activityFeed — i.e. ALL the live research data. `NEXT_PUBLIC_CONVEX_URL` + `CONVEX_DEPLOYMENT` point here. This is where the loop writes and the site reads.
   - **`scintillating-cow-269`** (project `bigbounce`, *prod*) = the OLDER, now-repurposed **Hubify LAB-platform backend** (labs/experiments/standups/GatewaySessions + an `api_keys` table + env vars). The paper loop does NOT use it — **never write paper data here.** It's a valuable archive (backed up daily); leave it alone.
   - **No deploy key is needed for the loop.** Data writes go over the public HTTP API (`POST https://brilliant-panther-471.convex.cloud/api/mutation`) — no key. To change *functions/schema* (e.g. the readiness ceiling in `convex/papers.ts`): `npx convex login` once, then **`npx convex dev --once`** (pushes to the dev deployment the site reads). `npx convex deploy` (no) would target `bigbounce-e6d13`'s empty *prod*, which the site does NOT read — don't use it. A `CONVEX_DEPLOY_KEY` is only for headless CI deploys and is optional.
   - **Readiness is COMPUTED from open findings, not hand-set** (`feedback_readiness_oscillation`). Move 92→96 by running the loop (intake EXT → truth-audit → close → re-review), NOT by editing/deploying a number.
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
3. Continue R→D→P until convergent-clean, then surface the Houston gates (ORCID public flip `0009-0008-5616-5994`, sign-off, arXiv submit P4→P1A→P1B→P3→P2→P5, mint DOIs).
4. Keep the site current after every single round. That's the job.
