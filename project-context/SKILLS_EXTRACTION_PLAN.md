# SKILLS EXTRACTION PLAN — bigbounce → global / science / hubify-labs

**Author:** synthesis pass on existing repo state (Claude, 2026-05-26)
**Inputs catalogued:**
- `~/.claude/CLAUDE.md` (global)
- `~/Desktop/CODE_2025/CLAUDE.md` (parent project)
- `bigbounce/CLAUDE.md` (current project)
- `bigbounce/AGENT_RULES.md` (63 KB — the most-load-bearing file)
- `bigbounce/AGENTS.md` (23 KB)
- `bigbounce/site/AGENTS.md`
- `project-context/` (15 deep-dive workflow specs read in full)
- `MEMORY.md` (50+ feedback/project memories)

**Output:** a partitioned skill library — what becomes a skill, what stays in `CLAUDE.md`, what's global vs. science-specific vs. bigbounce-only vs. hubify-labs-platform.

---

## 1. Design rules for the skill library

Before listing the skills, the design constraints (so each skill follows the same shape and Claude/Codex/Cursor can all discover them):

1. **One skill = one job.** A skill that "compiles a paper and syncs the site and updates SSOT" is three skills.
2. **Every skill has a one-line trigger.** Written in the imperative ("when X happens, run Y") — no ambiguity about when to invoke.
3. **Every skill names its inputs + hard gates.** A skill that "passes" without machine-checkable criteria is not done — see AGENT_RULES.md §2.5.
4. **Skills live where they apply.** Global rules in `~/.claude/skills/`; science rules in `~/.claude/skills/science/`; bigbounce-only in `bigbounce/.claude/skills/`; hubify-labs platform skills in the hubify-labs repo.
5. **`SKILL.md` per skill** with frontmatter (name, description, trigger, scope) — the description is the routing hook in future sessions, so it must be specific.
6. **No skill silently does destructive work.** Anything that pushes, force-pushes, stops a pod, deletes data, or flips prod must require an explicit "go" — see `feedback_never_flip_prod_unverified.md`.
7. **`CLAUDE.md` becomes thin.** Project context (what this repo IS) stays; protocols (HOW to do work) move into skills and are referenced by name.

---

## 2. What `CLAUDE.md` should keep (and what to move out)

### KEEP in `bigbounce/CLAUDE.md` (project-specific facts, ~80 lines max)

- **Research stance** — "bounce-model agnostic; goal = beat inflation, not defend ECH" (1 paragraph)
- **CRITICAL RESEARCH DIRECTIVE** — never publish failure; always propose next direction (1 paragraph)
- **Paper status pointer** — "always check `project-context/SSOT/index.md` first" (1 paragraph)
- **Live site URL** (1 line)
- **Author contact** (1 block)
- **Drive-to-100 loop notice** — if active, where to find loop log (1 paragraph)
- **Top-level repo map** — `arxiv/`, `pipelines/`, `reproducibility/`, `research/`, `site/` (1 table, ~15 lines)
- **Pointer to AGENT_RULES.md** as the source of truth for protocols
- **Pointer to the skill index** below

### MOVE OUT of `CLAUDE.md` (becomes skills or skill references)

These are all currently inline in `bigbounce/CLAUDE.md` and bloat it:
- Paper version dictionaries (P1A v1A.0.35, P1B v1B.0.22, …) → already redundant with SSOT; replace with one-line "see SSOT/index.md"
- Compile commands, revtex4-2 rules, figure handling → `science/paper-compile-revtex` skill
- Website sync protocol (HUGE block) → `bigbounce/site-sync` skill
- Peer review filing convention → `science/peer-review-file` skill
- Prompt history protocol (HUGE block) → `global/prompt-history` skill
- All the "skill routing" bullet lists → reduce to "see the skill index; route by name"
- GPU inference playbook details → `science/gpu-dataloader` skill
- The whole "stat results" paragraph (NaMaster, NANOGrav numbers) → that belongs in SSOT, not here

### KEEP / MOVE in `~/.claude/CLAUDE.md` (global)

KEEP:
- "Search before building" (Layer 1/2/3 knowledge) — short, universally applicable
- "AI effort compression" table — useful framing, low cost
- "Long-running tasks: don't give up" — universal directive
- The /latex-audit standing-rule sentence (because it applies to every project, not just bigbounce)
- Hubify CLI pointer

MOVE OUT (already covered):
- The "skill routing" section duplicates what each skill's own description will surface

### KEEP in `AGENT_RULES.md`

AGENT_RULES.md stays as the **methodology bible**. It's already long, structured by §, and skills should _reference_ § numbers rather than duplicate their content. The skill is the executable; AGENT_RULES is the spec.

---

## 3. Skill catalog — partitioned by scope

Each skill below has: name (kebab-case), home, trigger, inputs, hard gates, source spec.

---

### Tier A — GLOBAL skills (apply to any project, live in `~/.claude/skills/`)

These are not science-specific. They encode Houston's standing directives that hold across every project he works on.

#### A1. `prompt-history` — verbatim Houston-message saver
- **Trigger:** every substantive Houston message (strategic direction, feature request, design feedback, brain dump, pushback, course-correction)
- **Action:** append verbatim to `project-context/prompt-history.md` BEFORE doing the work
- **Gate:** message appears in file with `**HH:MM PT — <context>**` blockquote prefix
- **Source:** AGENT_RULES.md §9; `feedback_eat_the_frog.md` (related); CLAUDE.md "Prompt History Log"
- **Note:** must run BEFORE the work, not after. Compaction can hit mid-turn.

#### A2. `memory-write` — auto-memory frontmatter writer
- **Trigger:** Houston states a preference, correction, validated approach, or rule used 3+ times
- **Action:** write `name`/`description`/`type` frontmatter file + index it in `MEMORY.md`
- **Gate:** new file passes frontmatter schema; index line ≤150 chars; no duplicate of existing memory
- **Source:** AGENT_RULES.md §10; user-instruction "auto memory" block

#### A3. `env-local-discovery` — credential / path resolver
- **Trigger:** before asking Houston for any API key, dataset path, URL, or credential
- **Action:** grep all `.env.local` files under `~/Desktop/CODE_2025/`, then web-search official-docs URLs, then check sibling repos
- **Gate:** at least 3 search locations attempted; if escalation needed, escalation message names what was tried
- **Source:** AGENT_RULES.md §2.10; `feedback_never_defer_path_discovery.md`; `reference_env_local_secrets.md`

#### A4. `backup-3plus` — 3+ location backup guard
- **Trigger:** before any destructive operation (stop pod, rm -rf, delete data, kill long process, git reset --hard)
- **Action:** verify artifact exists in ≥3 of: local disk / GitHub / HuggingFace / Backblaze B2 / Convex
- **Gate:** 3 distinct backups confirmed before destructive action runs; otherwise abort + report
- **Source:** AGENT_RULES.md §2.8; `feedback_backup_everything.md`

#### A5. `hardest-path-first` — Path C as default
- **Trigger:** when presenting options to Houston for fixing/building anything
- **Action:** lead with the most-complete path (retrain, full MCMC, full rebuild) as "Recommended"; only label alternatives as weaker
- **Gate:** "easy path" never framed as "also reasonable"; cost called out explicitly; no hidden downgrade to caveat
- **Source:** AGENT_RULES.md §2.2; `feedback_default_hardest_path.md`; `feedback_more_not_less.md`

#### A6. `no-future-work-defer` — "future work" as code smell
- **Trigger:** when about to write "future work", "leave to future", "in preparation", "will be presented", "next step" (in code, docs, papers, or Houston-facing chat)
- **Action:** classify as DO-NOW / SIMULATE-AUGMENT-NOW / TRULY-BLOCKED; only the last is acceptable
- **Gate:** every deferral has a recorded class + rationale; default class is DO-NOW
- **Source:** AGENT_RULES.md §2.3, §6.6; `feedback_future_work_do_now.md`
- **Note:** has a science-specific cousin (`science/future-work-audit-paper`) that greps a .tex.

#### A7. `no-permission-loop` — never ask "want me to proceed"
- **Trigger:** at end of any work turn where Houston asked for something substantive
- **Action:** finish the work; do NOT close with "want me to proceed?" or "should I…?"
- **Gate:** turn ends with action taken or specific genuine blocker, never with a permission-request
- **Source:** AGENT_RULES.md §2.1; `feedback_no_permission_loop.md`; `feedback_no_questions_full_hard_fix.md`

#### A8. `parallel-subagents` — independent-task fan-out
- **Trigger:** ≥2 tasks with no shared file writes and no data dependency
- **Action:** issue them in one message as parallel `Agent` calls; serialize only on true write-conflict
- **Gate:** independent tasks measurably run in parallel; shared-file writes go through orchestrator merge
- **Source:** AGENT_RULES.md §5.2; `feedback_parallel_subagents.md`

#### A9. `loop-model-routing` — Sonnet body / Opus judgment / Haiku polling
- **Trigger:** at every cron-loop tick or autonomous wakeup
- **Action:** default to Sonnet 4.6 high-effort; escalate to Opus only on contested judgment (peer-review triage, claim verification, brain-dump synthesis); use Haiku for poll loops
- **Gate:** model chosen matches task class; escalations logged
- **Source:** AGENT_RULES.md §8.1; `feedback_loop_model_routing.md`

#### A10. `never-flip-prod-unverified` — visual production gate
- **Trigger:** before changing `vercel.json buildCommand` / `outputDirectory`, before publishing, before flipping any production hosting config
- **Action:** walk every nav page in a real browser at desktop + mobile, light + dark; verify zero 404, hamburger works, every link resolves
- **Gate:** all nav pages visually verified at all breakpoints before commit
- **Source:** AGENT_RULES.md §2.11; `feedback_never_flip_prod_unverified.md`; `feedback_vercel_deploy_workflow.md`

#### A11. `done-means-done` — anti-false-completion
- **Trigger:** before marking any task complete
- **Action:** require (a) ≥2 test-fix iterations, (b) real data (not stubs), (c) verified against spec/mockup, (d) audited the way the gap was originally found
- **Gate:** "done" = "holy shit"; never "good enough"
- **Source:** AGENT_RULES.md §2.5; `feedback_never_falsely_done.md`; `feedback_stub_tracking.md`

#### A12. `commit-message-atomic` — conventional commits with task prefix
- **Trigger:** every commit
- **Action:** use specific prefix: `feat(drive-to-100): fire #N — …`, `chore(R{N}-stamp): …`, `feat(paper-N v…): …`, `fix(site-sync): …` — never "updates" or generic
- **Gate:** commit messages are bisectable and grep-able; no anonymous "wip" / "updates"
- **Source:** AGENT_RULES.md §7.4, §4.2; CLAUDE.md global "Commit style" (bisect commits)

---

### Tier B — SCIENCE skills (research/papers/compute, live in `~/.claude/skills/science/` once promoted)

These apply across **any scientific research project**, not just bigbounce. They're the highest-value extractions.

#### B1. `houston-method-v2` — 9-step experiment completion protocol
- **Trigger:** when an experiment/analysis/pipeline produces raw results
- **Action:** drive through RUN → QC → ANALYZE → INTERPRET → CONNECT → SYNC → EXPAND → BACKUP → COMPLETE; emit `checkpoint.json` at end
- **Gate:** every step executed; QC pass before ANALYZE; ≥5 new tasks generated in EXPAND; 3-location backup before COMPLETE
- **Source:** `project-context/houston-method-v2.md`; AGENT_RULES.md §3; `feedback_houston_method.md`

#### B2. `qc-gate` — automated quality-control checks
- **Trigger:** immediately after Step 1 (RUN) of houston-method-v2 produces output
- **Action:** run 7 canonical checks (null coords, training quality, cluster degeneracy, score explosion, spatial concentration, empty output, NaN/Inf); emit structured `qc_status` JSON
- **Gate:** all checks PASS → PROCEED; any FAIL → mark needs-rerun; never silently advance
- **Source:** AGENT_RULES.md §3 Step 2

#### B3. `future-work-audit-paper` — Principle 10 grep+classify
- **Trigger:** before a paper is marked arXiv-ready; before closing every R-round
- **Action:** grep .tex for 30+ trigger phrases; classify each hit DO-NOW / SIMULATE-AUGMENT / TRULY-BLOCKED; record in SSOT `paper-N/status.md`
- **Gate:** zero unresolved DO-NOW remains; only TRULY-BLOCKED items survive
- **Source:** AGENT_RULES.md §6.6, §2.3; `project-context/houston-method-v2.md` Principle 10

#### B4. `cross-vendor-r-round` — 5-vendor OpenRouter peer review
- **Trigger:** paper at ≥85% readiness; before declaring "external-review-ready"
- **Action:** dispatch full .tex to GPT-5.5, Gemini-2.5-pro, Grok-4, Perplexity sonar-pro, DeepSeek-v3.2 via OpenRouter; collect findings as 5 .md files
- **Gate:** every finding classified BLOCKER/MAJOR/MINOR + classified FACT/OPINION/HALLUCINATION; truth-audit table written before any closure work begins
- **Source:** AGENT_RULES.md §4.4; `feedback_peer_review_truth_audit_protocol.md`; `feedback_cross_model_peer_review.md`

#### B5. `cascaded-r-rounds` — convergence loop until clean
- **Trigger:** after `cross-vendor-r-round` closure
- **Action:** recompile + re-dispatch; loop until 3+ of 5 vendors return convergent silence with zero regression of prior closures, zero new BLOCKERs, ≤1-2 polish-tier MAJORs
- **Gate:** §4.4.1 exit criteria green
- **Source:** AGENT_RULES.md §4.4.1

#### B6. `peer-review-truth-audit` — per-finding evidence verification
- **Trigger:** any external (or internal multi-model) peer review arrives
- **Action:** build a finding-by-finding table: claim / cited source / on-disk verification / verdict (CORRECT, INCORRECT/STALE, MISLABELED, OUT-OF-SCOPE)
- **Gate:** every finding has a verdict + an artifact path before any closure work
- **Source:** `feedback_peer_review_truth_audit_protocol.md` (STANDING DIRECTIVE 2026-05-15)

#### B7. `revision-tracker-update` — peer-review tracker maintenance
- **Trigger:** after every peer-review round closes
- **Action:** update `project-context/peer-reviews/REVISION_TRACKER.md` with BLOCKER/MAJOR/MINOR + resolution commit hash; file the round as `YYYY-MM-DD_HHMMtz_description.md`
- **Gate:** every issue tracked from open to closed
- **Source:** AGENT_RULES.md §4.5

#### B8. `pdf-restamp-bundle` — single-commit recompile+mirror+SSOT
- **Trigger:** every revision round that touches any paper's .tex / .bib / data / figure
- **Action:** bundle (a) `\paperVersion` + `\paperTimestamp` + `\date{}` bump, (b) pdflatex→bibtex→pdflatex→pdflatex with 0 undef, (c) pypdf-verify page 1, (d) mirror PDF to all publish paths, (e) site metadata refresh, (f) SSOT refresh, (g) single commit `chore(R{N}-stamp): …`
- **Gate:** 8-item verification checklist passes; single atomic commit
- **Source:** AGENT_RULES.md §4.2; Principle 13 (`houston-method-v2.md`); `feedback_pdf_recompile_protocol.md`

#### B9. `latex-overflow-audit` (already exists as global `/latex-audit`)
- Already a global skill — keep as-is; document that it satisfies AGENT_RULES.md §4.7.
- **Source:** existing skill + AGENT_RULES.md §4.7; `feedback_pdf_visual_formatting.md`; `feedback_pdf_formatting_audit.md`

#### B10. `artifact-link-verify` — `\artifact{}` URL checker
- **Trigger:** before closing any R-round with embedded `\artifact{…}` macros
- **Action:** extract URIs from PDF; verify each path exists on `main` at the committed SHA; check `/blob/` vs `/tree/` for files vs dirs
- **Gate:** zero 404s on resolved URLs; correct `/blob/` vs `/tree/`
- **Source:** AGENT_RULES.md §4.7.1

#### B11. `bib-tarball-rebuild` — clean arXiv submission tarball
- **Trigger:** before any arXiv submission
- **Action:** parse .tex `\cite{}` and .bbl entries; reconcile; rebuild tarball from scratch in `/tmp` with only referenced figures; smoke-test re-extract + recompile
- **Gate:** .bbl matches .tex; tarball recompiles standalone with 0 undef
- **Source:** AGENT_RULES.md §7.2 "stale .bbl failure mode"

#### B12. `ssot-update` — atomic SSOT writes
- **Trigger:** verified new result, claim/artifact mismatch found, "close-the-gap" item completed, .tex canonical location change, downstream surface sync
- **Action:** update `SSOT/paper-N/status.md` + `SSOT/queue.md` + `SSOT/index.md` headline in the same commit
- **Gate:** index headline matches per-paper status; queue.md owners + machine-checkable criteria present; freshness ≤7 days
- **Source:** AGENT_RULES.md §6; `project_ssot_structure.md` memory; SSOT/README.md

#### B13. `drive-to-100-fire` — autonomous loop tick
- **Trigger:** cron `*/20 * * * *` while drive-to-100 active; OR manual fire
- **Action:** read plan doc, pick highest-priority open task, execute one atomic step, single commit `feat(drive-to-100): fire #N — …`, append loop log
- **Gate:** one commit per fire; exit criteria checked at start; loop self-terminates when all met
- **Source:** AGENT_RULES.md §7; `project_drive_to_100.md`

#### B14. `readiness-cap-99` — honest oscillation enforcement
- **Trigger:** any time a paper readiness % is written to any surface
- **Action:** cap at 95% until clean self-review + clean cross-vendor + Houston sign-off; rise to 99% only after both; only Houston awards 100%
- **Gate:** no paper at 100% without Houston sign-off; oscillation backward on new MAJORs
- **Source:** AGENT_RULES.md §4.3; `feedback_99_pct_readiness_cap.md`; `feedback_readiness_oscillation.md`

#### B15. `paper-compile-revtex` — revtex4-2 standard compile
- **Trigger:** when compiling any paper in this lab
- **Action:** enforce `[aps,prd,twocolumn,…]{revtex4-2}` preamble; `\cite{}` not `\citep{}`; tables in `ruledtabular`; figures co-located; pdflatex 4-pass
- **Gate:** style matches across all 6 papers; PDF ≥ figure-count threshold; 0 undef refs
- **Source:** AGENT_RULES.md §4.1; CLAUDE.md "Paper Compilation"; `feedback_revtex_papers.md`

#### B16. `gpu-dataloader-pattern` — 32× speedup template
- **Trigger:** any large-scale image / data inference on GPU
- **Action:** `DataLoader(num_workers=16, pin_memory=True, prefetch_factor=4, batch_size=512)`; refuse serial PIL, ProcessPoolExecutor, HF streaming
- **Gate:** GPU utilization >80%; per-shard checkpoint written; benchmark logged
- **Source:** `project-context/gpu-inference-playbook.md`; AGENT_RULES.md §5.1; `feedback_gpu_dataloader.md`

#### B17. `runpod-lifecycle` — pod create/SSH/stop/start/terminate
- **Trigger:** any RunPod pod operation
- **Action:** use `python3 research/runpod_cloud.py` commands (status, ssh, setup, push-keys, stop, start, terminate)
- **Gate:** pod state verifiable; data persists across stop/start; only `terminate` destroys
- **Source:** AGENTS.md "GPU Compute"; AGENT_RULES.md §5.1; `feedback_runpod_sdk_unreliable.md` (use REST GraphQL, not SDK)

#### B18. `idle-gpu-rescue` — auto-queue when nvidia-smi == 0%
- **Trigger:** GPU utilization 0% for >5 minutes
- **Action:** check queue → research directions → propose new experiments → spin up + queue next chain; always keep N+1 chains queued
- **Gate:** GPU never sits idle >5 min with budget available
- **Source:** AGENT_RULES.md §2.9; `feedback_idle_gpu_proactive.md`; `feedback_gpu_idle.md`

#### B19. `pod-backup-before-stop` — SCP-before-shutdown
- **Trigger:** before stopping any RunPod pod
- **Action:** SCP all results to local; verify file count + sizes; only then stop
- **Gate:** results in 3+ locations before stop command runs
- **Source:** AGENT_RULES.md §2.8

#### B20. `multi-model-reasoning-router` — 7-LLM task dispatch
- **Trigger:** research question that benefits from specialized reasoning or consensus
- **Action:** route via keyword (math_rigor→DeepSeek R1, multimodal→Gemini, writing→Claude Opus, reasoning→GPT, literature→Perplexity, fast→Grok, multi→OpenRouter); optionally do `multi_query` for consensus
- **Gate:** routing decision logged; consensus pulled from ≥3 models when verifying claims
- **Source:** `RESEARCH_ARCHITECTURE.md` §2.1 (`reasoning_router.py`, 300 lines, 100% reusable)

#### B21. `literature-unified-search` — ADS + S2 + arXiv + Perplexity
- **Trigger:** topic-based discovery, claim verification, citation graph traversal
- **Action:** unified search across all four sources; return dict keyed by source
- **Gate:** ≥3 sources hit per query; cache 24h
- **Source:** `RESEARCH_ARCHITECTURE.md` §2.2 (`literature_search.py`, 200 lines, 100% reusable)

#### B22. `alphaxiv-search` / `alphaxiv-ask` / `alphaxiv-code` / `alphaxiv-annotations`
- **Trigger:** native arXiv operations (search, Q&A on paper, repo code reading, community annotations)
- **Action:** call AlphaXiv API per the spec; idempotent + cacheable
- **Gate:** rate-limited (free: 100/day search, 50 ask, 200 code); auth via `ALPHAXIV_API_KEY`
- **Source:** `project-context/ALPHAXIV_SKILL_SPEC.md`
- **Note:** these are 4 sibling skills; spec is already written, just needs implementation.

#### B23. `wolfram-deepseek-verify` — equation cross-check
- **Trigger:** equation verification, dimensional consistency, sign-error check
- **Action:** Wolfram for symbolic; DeepSeek-R1 for reasoning; cross-check with a third model for consensus
- **Gate:** ≥2 models agree before claim recorded; disagreements logged
- **Source:** `RESEARCH_ARCHITECTURE.md` §2.3 (`computation.py`, 252 lines, 100% reusable)

#### B24. `astro-data-access` — MAST + Gaia + VizieR + NED
- **Trigger:** astronomy archive queries
- **Action:** unified functions for JWST/HST/TESS (MAST), Gaia DR3 (ADQL), VizieR by ID, NED redshifts
- **Gate:** result is structured dict; async for large Gaia queries
- **Source:** `RESEARCH_ARCHITECTURE.md` §2.4 (`data_access.py`, 289 lines, 95% reusable)

#### B25. `mmu-dataset-loader` — HF Multimodal Universe streamer
- **Trigger:** load large astro dataset for inference/analysis
- **Action:** stream 100TB MMU datasets, or AstroML built-ins, or Polymathic foundation models
- **Gate:** streaming respects per-shard memory; VRAM requirements met
- **Source:** `RESEARCH_ARCHITECTURE.md` §2.5 (`dataset_loaders.py`, 263 lines, 80% reusable)

#### B26. `bounce-portfolio-track-gate` — A/B/C/D track viability
- **Trigger:** before opening any new research branch
- **Action:** apply 4-question test: new physics? plausible tiny scale? distinctive prediction? failure publishable? — fail any → don't open
- **Gate:** all 4 YES, or branch is rejected
- **Source:** `project-context/bounce_portfolio_strategy.md`; AGENT_RULES.md §11.3
- **Note:** bounce-specific framing, but the 4-question pattern generalizes.

---

### Tier C — BIGBOUNCE skills (lab/project-specific, live in `bigbounce/.claude/skills/`)

These are coupled to **this** repo's HTML pages, paper list, and SSOT layout.

#### C1. `bigbounce-site-sync` — root HTML + Next.js dual sync
- **Trigger:** any paper result, MCMC chain, figure, version, or branch state change
- **Action:** identify affected pages (index.html, paper.html, activity.html, data-explorer.html, explained.html, glossary.html, etc.) AND mirror updates into `site/` (Next.js); commit in same atomic commit as SSOT
- **Gate:** all pages with changed numbers updated in same commit; both legacy HTML and Next.js site touched; `feedback_site_sync_same_commit.md` honored
- **Source:** CLAUDE.md "WEBSITE SYNC PROTOCOL"; AGENT_RULES.md §5.3-5.4; `feedback_website_sync.md`; `project_site_routing.md`

#### C2. `bigbounce-version-bump` — paperVersion + version.json
- **Trigger:** publication-worthy change to any of the 6 papers
- **Action:** bump `\paperVersion` + `\paperTimestamp` + `\date{}` + `version.json` in same commit; semver rules (patch/minor/major)
- **Gate:** all 4 items synchronized; pypdf-verified page 1 reflects new values
- **Source:** AGENTS.md "Versioning"; AGENT_RULES.md §4.2

#### C3. `bigbounce-paper-pdf-mirror` — publish PDF to all 2 paths
- **Trigger:** after `pdf-restamp-bundle`
- **Action:** copy compiled PDF to `public/papers/` AND `site/public/` (or wherever the Next.js site mounts it)
- **Gate:** PDF appears at all hosting paths; site references resolve
- **Source:** AGENTS.md "Publishing PDFs"

#### C4. `bigbounce-claims-table-sync` — claims-table consistency
- **Trigger:** any quantitative claim in a paper changes
- **Action:** grep every HTML page and every `.tex` for the old number; update everywhere in one commit
- **Gate:** zero stale instances of the old number in repo; claims-table on index.html matches paper abstract
- **Source:** CLAUDE.md "When research results change"

#### C5. `bigbounce-revision-tracker` — peer-review tracker (specialization of B7)
- Same as `revision-tracker-update` but binds to `project-context/peer-reviews/REVISION_TRACKER.md` schema.

---

### Tier D — HUBIFY LABS PLATFORM skills (live in the hubify-labs repo, NOT here)

These are skill-shaped patterns from the project-context docs that target the Hubify Labs product, not bigbounce research. Listed for completeness so they don't get extracted into the wrong place.

#### D1. `k-dense-manifest-sync` — weekly upstream skill sync
- **Source:** `project-context/K_DENSE_SKILLS_AUDIT.md`
- 102-skill default catalog, GitHub Actions Sunday 02:00 PT, per-lab `lab.toml` overrides.

#### D2. `subagent-widget` — fire-and-forget subprocess card UX
- **Source:** `project-context/pi_agent_study.md`
- Spawn `claude` / `pi` subprocess, parse JSONL events, render live status card.

#### D3. `agent-team-grid` — N-agent dispatcher dashboard
- **Source:** `pi_agent_study.md`
- Grid layout, per-agent status/elapsed/context%, dispatcher-only-dispatches pattern.

#### D4. `tilldone-gating` — task-declaration gate
- **Source:** `pi_agent_study.md`
- Force agent to declare task list before tool use; block tool_calls if no active task.

#### D5. `damage-control-safety` — purpose-gate + scope-fence
- **Source:** `pi_agent_study.md`
- Block destructive ops outside declared scope; require purpose statement.

#### D6. `sandbox-lifecycle` — provision / hibernate / restore
- **Source:** `project-context/vibe_coding_patterns.md`; `research_vercel_open_agents.md`
- 4-tool agent (createSandbox / generateFiles / runCommand / getSandboxURL); per-session reuse; iframe-remount on URL change.

#### D7. `stream-json-parser` — Claude Code CLI event translator
- **Source:** `vibe_coding_patterns.md`
- Parse `claude --output-format stream-json` into UI status data-parts.

#### D8. `dual-model-gateway` — main + low-effort sub-model router
- **Source:** `vibe_coding_patterns.md`
- Route file-generation calls to cheap model, reasoning to expensive.

#### D9. `alphaxiv-skill` (already covered as B22 — same underlying spec, but here it's a Hubify Labs default skill).

#### D10. `houston-method-v2-as-product` — package B1 as a Hubify Labs "Last Mile" module
- **Source:** `feedback_last_mile_paper_completion.md`

---

## 4. Skill index file (proposed `~/.claude/skills/INDEX.md`)

A single index Claude/Codex/Cursor read at session start to discover skills by name. Replaces the inline skill-routing blocks in CLAUDE.md.

```
# Global skills (Tier A)
prompt-history — save every substantive Houston message verbatim before working
memory-write — append to MEMORY.md when Houston states a preference or rule
env-local-discovery — never ask for keys before grepping .env.local + docs
backup-3plus — verify 3 locations before any destructive op
hardest-path-first — lead with Path C, never frame easy as "also reasonable"
no-future-work-defer — classify every "future work" hit; default DO-NOW
no-permission-loop — never end a turn with "want me to proceed?"
parallel-subagents — fan independent tasks out in one message
loop-model-routing — Sonnet body / Opus judgment / Haiku polling
never-flip-prod-unverified — walk every page desktop+mobile before vercel.json edits
done-means-done — 2+ test-fix iterations, real data, audited
commit-message-atomic — feat(scope): … with task ID prefix

# Science skills (Tier B)
houston-method-v2 — 9-step experiment completion protocol
qc-gate — 7 automated quality checks before ANALYZE
future-work-audit-paper — grep .tex, classify each hit, gate at zero DO-NOW
cross-vendor-r-round — 5-vendor OpenRouter peer review
cascaded-r-rounds — convergence loop until §4.4.1 exit criteria green
peer-review-truth-audit — per-finding evidence table before any closure
revision-tracker-update — track BLOCKER/MAJOR/MINOR + commit hash
pdf-restamp-bundle — atomic recompile+mirror+SSOT in one commit
latex-overflow-audit — (existing) post-compile visual + log audit
artifact-link-verify — every \artifact{} URL resolves on main
bib-tarball-rebuild — clean arXiv tarball, .bbl matches .tex
ssot-update — atomic SSOT/index + paper-N/status + queue write
drive-to-100-fire — autonomous loop tick, one atomic step per fire
readiness-cap-99 — never 100% without Houston sign-off
paper-compile-revtex — revtex4-2 standard compile rules
gpu-dataloader-pattern — 32× speedup template (num_workers=16, pin_memory)
runpod-lifecycle — pod create/SSH/stop/start via runpod_cloud.py
idle-gpu-rescue — auto-queue work when nvidia-smi == 0%
pod-backup-before-stop — SCP before shutdown
multi-model-reasoning-router — 7-LLM task-aware dispatch
literature-unified-search — ADS + S2 + arXiv + Perplexity in one call
alphaxiv-{search,ask,code,annotations} — native arXiv ops, cacheable
wolfram-deepseek-verify — symbolic + reasoning equation cross-check
astro-data-access — MAST + Gaia + VizieR + NED
mmu-dataset-loader — HF Multimodal Universe streaming
bounce-portfolio-track-gate — 4-question test before new research branch

# bigbounce-only skills (Tier C, live in bigbounce/.claude/skills/)
bigbounce-site-sync — root HTML + Next.js dual sync in same commit
bigbounce-version-bump — paperVersion + paperTimestamp + date + version.json
bigbounce-paper-pdf-mirror — copy to all hosting paths
bigbounce-claims-table-sync — grep + replace every quantitative claim
bigbounce-revision-tracker — peer-reviews/REVISION_TRACKER.md upkeep
```

---

## 5. Slimmed `bigbounce/CLAUDE.md` (target structure)

Once the skills above exist, `CLAUDE.md` shrinks to roughly:

```markdown
# CLAUDE.md — bigbounce

## Paper status
ALWAYS read `project-context/SSOT/index.md` FIRST. Do not rely on this file or
any wiki/HTML page for paper status — SSOT is canonical.

## Research stance
Bounce-model agnostic. Goal is proving bounce cosmology beats inflation.
See `project-context/bounce_portfolio_strategy.md` for portfolio strategy.

## CRITICAL DIRECTIVE
Never publish failure. After negative results, propose next direction.

## Protocols (skills)
All protocols live as skills. Read `~/.claude/skills/INDEX.md` first.
Reference `AGENT_RULES.md` for spec.

Skill quick-pointers:
- Paper compile → /paper-compile-revtex + /latex-overflow-audit + /pdf-restamp-bundle
- Peer review → /cross-vendor-r-round + /peer-review-truth-audit + /cascaded-r-rounds
- Site update → /bigbounce-site-sync
- Experiment complete → /houston-method-v2 + /qc-gate + /ssot-update
- Drive-to-100 → /drive-to-100-fire (cron-driven)

## Repo map
| Path | Purpose |
|------|---------|
| arxiv/ | Paper sources (revtex4-2) |
| pipelines/ | p1..p5 production pipelines |
| reproducibility/ | MCMC chains, configs, gaps doc |
| research/ | Active branches + dossier |
| site/ | Next.js site (default at root) |
| /old | Legacy static HTML, deprecated |

## Drive-to-100 loop
If active, see `project-context/SSOT/drive-to-100.md` for loop log + plan.
Loop fires `*/20`. Read before parallel work on same queue rows.

## Contact
Author: Houston Golden — houston@hubify.com — bigbounce.hubify.app
```

That's ~50 lines. Everything else moves into a skill, gets referenced by name, and stops drifting.

---

## 6. Migration plan (no code yet — just the path)

A staged rollout, each stage independently committable.

**Stage 1 — Promote existing rules to skill stubs (no behavior change).**
Create `~/.claude/skills/INDEX.md` with the table above. For each skill, drop a `SKILL.md` stub that points to AGENT_RULES § number + project-context spec file. Houston can read the index and Claude can route by name. No new logic.

**Stage 2 — Implement the 5 highest-value science skills.**
B1 (houston-method-v2), B8 (pdf-restamp-bundle), B12 (ssot-update), B16 (gpu-dataloader-pattern), B4 (cross-vendor-r-round). These show up in every research session.

**Stage 3 — Slim `CLAUDE.md`.**
After Stage 2 lands, replace the bloated sections (compile rules, site sync, peer review, prompt history) with the one-line skill pointers shown in §5. AGENT_RULES.md stays unchanged as the spec.

**Stage 4 — Implement Tier A global skills.**
A1-A12 are short, mostly already encoded in memory. Promoting them to discoverable skills means Codex/Cursor/Pi see them too via agent-stack-sync.

**Stage 5 — Tier C bigbounce skills.**
Once Tier A+B exist, C1-C5 are thin specializations.

**Stage 6 — Tier D becomes Hubify Labs product surface.**
Ships as part of the Hubify Labs platform, not this repo.

---

## 7. Open questions for Houston

These are the calls I won't make unilaterally:

1. **Skill home — global vs. project-scoped.** I've assumed Tier A+B live in `~/.claude/skills/` (visible to every project via agent-stack-sync). Tier C lives in `bigbounce/.claude/skills/`. OK?
2. **Naming convention.** I've used kebab-case verbs (`pdf-restamp-bundle`, not `RestampPDFBundle`). OK?
3. **Implementation language.** gstack skills are bash + markdown. Should B1-B26 follow the same pattern, or do we want Python helpers under the hood (since most of the science work is Python anyway)?
4. **AGENT_RULES.md fate.** Keep as the spec bible, or fold into skill docs and retire? My recommendation: keep — skills are the executable, AGENT_RULES is the constitution.
5. **CLAUDE.md slimming — when.** I'd prefer to slim AFTER the top-5 skills land (Stage 2), so we don't lose protocol coverage in the interim. OK?

---

**End of plan.**
