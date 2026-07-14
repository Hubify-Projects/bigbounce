# AGENTICS_MAP.md — External Connections + Agent-Roles Audit

> Complete map of every external service, agent role, data store, and liveness
> mechanism the bigbounce review/compute program depends on. **Secrets are
> referenced by env-var NAME only — never a value.** All keys live in
> `<repo-root>/.env.local` (gitignored); use `/env-local-discovery` before ever
> asking Houston for one.

---

## 1. External services

| Service | Purpose | Auth env-var NAME | Entry point (script / URL) | Failure mode |
|---|---|---|---|---|
| **Anthropic (Claude)** | INT review Claude leg — **but see §2: routed through the Claude Code SUBSCRIPTION, NOT this key** (directive I1). Key present for other tooling only. | `ANTHROPIC_API_KEY` | running Claude Code agent (`claude -p`, key unset) | Never fail an INT round on Anthropic API — the subscription agent IS the leg. |
| **OpenAI** | INT review through Codex CLI on Houston's ChatGPT subscription | none; `OPENAI_API_KEY` and `CODEX_API_KEY` are explicitly unset | `tools/int_wave.sh`, `tools/int_wave_apjs.sh` | unavailable subscription auth → leg visibly unavailable; never fall back to OpenAI API billing. |
| **Google Gemini** | INT review leg (2.5 Pro, native/inline PDF) | `GOOGLE_GEMINI_API_KEY` / `GOOGLE_AI_API_KEY` | `tools/cross_model_review_gemini.py` | Stored keys historically 403/billing-blocked → Gemini INT covered via browser EXT; never fail the round on it. |
| **xAI (Grok)** | INT review leg (Grok 4, image-rasterized PDF) | `XAI_API_KEY` | `tools/v3_native_pdf_review.py` | leg FAILED, round continues. |
| **OpenRouter** | multi-model fallback routing | `OPENROUTER_API_KEY` | review tooling | optional; not a hard dependency. |
| **Perplexity** | OPTIONAL citation-forensics leg (sonar text+web) | `PERPLEXITY_API_KEY` | `v3_native_pdf_review.py` (optional) | **never a required key; never fail the pipeline on its absence.** |
| **DeepSeek** | (removed from review battery — always timed out) | `DEEPSEEK_API_KEY` | — | not in active loop. |
| **Wolfram / DeepSeek verify** | symbolic math cross-check | `WOLFRAM_ALPHA_APP_ID` | `/wolfram-deepseek-verify` | optional verification. |
| **Convex** | **the live site backend** — all paper state, verdicts, readiness, activity | `CONVEX_DEPLOYMENT`, `CONVEX_URL`, `CONVEX_SITE_URL` (data writes need NO key) | HTTP API `POST https://brilliant-panther-471.convex.cloud/api/mutation` | stale surface if a round skips the write (directive A). |
| **Vercel** | Next.js site deploy → **bigbounce.hubify.app** | `VERCEL_OIDC_TOKEN`, `VERCEL_*` | `site/` → Vercel; `/never-flip-prod-unverified` before `vercel.json` edits | visual verify before prod flip. |
| **HuggingFace** | dataset + model backups (backup target #2) | `HF_TOKEN` / `HUGGINGFACE_TOKEN` | `bamfai/galaxy-chirality-catalog`, `bamfai/galaxy-chirality-v2` | one of 3 required backup sinks. |
| **Backblaze B2** | archival backup target #3 | (B2 creds in `.env.local`) | `pipelines/backup_runpod.sh`, `pipelines/p1_highz_tracers/scripts/sync_batches.sh` (`B2_BUCKET`, `b2://…`) | must be one of 3 confirmed sinks before any destructive op (`/backup-3plus`). |
| **RunPod** | GPU compute (A100) for image inference / large sweeps | `RUNPOD_API_KEY` + pod SSH coords (`POD_COBAYA_R43_V2_HOST/ID/PORT/SSH_DIRECT/SSH_PROXY`) | `/runpod-lifecycle`, `pipelines/backup_runpod.sh` | **STOP never terminate**; terminate typo destroys `/workspace`. See COMPUTE_ROUTING.md. |
| **NASA ADS / Semantic Scholar** | literature search | `NASA_ADS_API_KEY`, `SEMANTIC_SCHOLAR_API_KEY` | `/literature-unified-search` | optional research support. |
| **Firecrawl** | web scrape | `FIRECRAWL_API_KEY` | `/scrape` | optional. |
| **NOIRLab SPARCL** | public DESI-DR1 spectra archive (P3/P5 data) | none (public) | astro-data pulls | network-throttled; NOT a GPU dependency (see COMPUTE_ROUTING §3). |
| **arXiv / Zenodo** | submission targets | Houston-gated (manual) | `submissions/*/`, `tools/build_arxiv_tarball.sh`, `tools/insert_arxiv_ids.sh` | Houston clicks submit; agents only prep kits. |

---

## 2. Agent-role map

| Role | Model / surface | Responsibility | Hard rules |
|---|---|---|---|
| **Orchestrator** | session model (Fable 5, planning only — directive J) | plan, split lanes, synthesize, route; **never brute-force execution** | never idles while any verdict < ACCEPT; delegates all mechanical work. |
| **Opus adjudicators** | `model: "opus"` subagents | strict ledger-first truth-audit of every finding (patterns 061-066); GENUINE vs ENGINEERED integrity audit (`/review-integrity-audit`) | verdict-first ordering; source-cited disposition; NEVER fake ACCEPT / fabricate. |
| **Owner / closure agents** | Opus (one owner per paper) | close real items with real edits/science, recompile (0 undef-refs) + `/latex-audit`, directive-G PDF hygiene, Convex+site sync, commit | one owner per paper; ~30-min heartbeat. |
| **INT battery — OpenAI leg** | Codex CLI / ChatGPT SUBSCRIPTION with API keys unset | full-repo-context internal review | NEVER OpenAI API; unavailable subscription auth is visible and fails closed. |
| **INT battery — xAI leg** | XAI API (Grok, rasterized PDF) | internal review | per-finding source-cited truth-audit like EXT. |
| **INT battery — Gemini leg** | Gemini API when key works; else browser EXT | internal review | never fail round on billing block. |
| **INT battery — Claude leg** | **Claude Code SUBSCRIPTION via `claude -p` with `ANTHROPIC_API_KEY` UNSET** — the running agent itself, NEVER the API (directive I1) | internal review with full repo + source + context | NEVER ask Houston for an Anthropic API key; NEVER fail an INT leg on API-disabled. The subscription agent IS this leg. |
| **EXT browser legs** | **HEADED gstack Chromium** (`~/.claude/skills/gstack/browse/dist/browse connect`, port 34567, real Chrome, `Mode: headed`) | ChatGPT + Grok + Gemini live-PDF referee reviews | headless CANNOT pass Cloudflare / OAuth — headed MANDATORY (`/connect-chrome`). Fresh chat per leg, capture chat URL immediately, save raw text + screenshot **then verify before recording any verdict**. |
| — ChatGPT project | `https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/project` | Extended Thinking Pro / Deep Research (every other round) | login: Houston's account in headed window. |
| — Grok project | `https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1` | Grok Expert | fresh project chat per leg. |
| — Gemini | `https://gemini.google.com/u/1/app` | Ultra plan via **houston@bamf.com**; Deep Research + Deep Think via `+` | in-place send-verify; never navigate away after send. |
| **Codex concurrent driver** | separate agent (may run same papers) | may drive the same review loop | **remote lease first, STATE CHECK second** — only the fresh lease holder may drive browser/adjudication/verdict state. A non-holder stays INT/compute/tooling-only. Recent commits/files-changing remain defense in depth. Raw harvest is safe; `post_verdict.sh` is DRIVER-only. |

---

## 3. Data stores

**Repo paths**
- `project-context/SSOT/` — canonical paper status (`index.md`, `paper-N/status.md`, `queue.md`); read FIRST, mirrors never drive.
- `project-context/peer-reviews/DISPOSITIONS/<P>.md` — canonical finding dispositions (fingerprint-matched for clean-wave counting).
- `project-context/peer-reviews/EXT_real/<ROUND>_<date>/` — EXT contract: `manifest.jsonl` (one row per leg, written immediately) + `<PAPER>_<reviewer>.md` (raw verbatim) + `<PAPER>_<reviewer>.png` (screenshot). A leg with no output = FAILED, not a verdict.
- `project-context/peer-reviews/INT_api/<ROUND>_<date>/` + `INT_v3/` — INT API raw outputs.
- `project-context/peer-reviews/REVISION_TRACKER.md` — per-paper revision history.
- `submissions/<P*>/` — arXiv kits, `CAMPAIGN_STATUS.md`, `HUMAN_READ_BRIEFING.md`, `P3_VENUE_DECISION.md`.
- `project-context/LOOP_HEARTBEAT.json` — liveness beacon.

**Convex tables** (deployment `brilliant-panther-471`, dev; data via HTTP API no-key; code via `convex login` → `dev --once`, **never `deploy`**; never touch `scintillating-cow-269`):
`papers` · `paperVersions` · `externalReviews` · `readinessMetrics` · `activityFeed` · `rRounds` · `findings` · `reviews` · `pathcCaveats` · `pods` · `mcmcStatus` · `spectralResults` · `galaxies` · `figures` · `checklistItems` · `pipelineState` · `models` · `tasks` · `chatMessages`.
Canonical mutations per round: `paperVersions:bump` (real md5/pages), `rRounds:create`, `externalReviews:upsertByLabelDate` (source `internal-stage3`, enum `accept|minor-revisions|major-revisions|reject|pending`), `activityFeed:add`, `papers:setReadinessCap` (96/98/99). Wrappers: `tools/post_verdict.sh`, `tools/insert_arxiv_ids.sh`.

**External stores**
- **HuggingFace** `bamfai/galaxy-chirality-catalog`, `bamfai/galaxy-chirality-v2` — datasets + models + interim checkpoints.
- **Backblaze B2** `B2_BUCKET` (`b2://…`) — archival mirror.
- **/tmp staging** — arXiv tarball rebuild + standalone-compile verification (`tools/build_arxiv_tarball.sh`, `/bib-tarball-rebuild`).

---

## 4. Scheduling / liveness

Session crons are session-only, so launchd is the durability guarantee (directive: loop-never-dies):

| Mechanism | plist / file | Role |
|---|---|---|
| **Hourly cron tick** | `~/Library/LaunchAgents/com.bigbounce.cron-tick.plist` → `~/Library/Application Support/bigbounce/bigbounce-cron-tick.sh` | fires one improvement step; logs to `project-context/cron-logs/launchd.{out,err}`. |
| **Loop watchdog** | `com.bigbounce.loopwatchdog.plist` → `.../loop_watchdog.sh` (`StartInterval`) + `tools/loop_watchdog.sh` | restarts the loop if it dies; logs `/tmp/bigbounce_watchdog.log`. |
| **Caffeinate** | `com.bigbounce.caffeinate.plist` (`caffeinate -i`) | keeps the mac awake for long runs. |
| **Heartbeat** | `project-context/LOOP_HEARTBEAT.json` | liveness beacon; verify cron+watchdog+heartbeat at every session start. |
| **Freshness gate** | `tools/site_freshness_check.sh` | pre-push hook + cron tick; kills the stale-surface failure class. |

---

## 5. Hubify notes

- **hubify CLI** installed globally (`/opt/homebrew/bin/hubify`) — real lab data (`hubify status|experiments|papers|reviews|pods|costs|…`); run it, don't guess. **youmd CLI** at `~/.you/bin/youmd` — identity/context/sync overlay.
- **bigbounce.hubify.app** — the live Next.js site (Vercel), reads from Convex. The `/reviews` verdict grid (newest-left, CURRENT column) is the **terminal criterion**: exit only when 100% ACCEPT across all papers × reviewers (directive M).
- **Skill layer**: bigbounce-specific skills live at `~/.claude/scistack/astrostack/` (canonical R-round spec: `~/.claude/scistack/astrostack/bigbounce-r-round/SKILL.md`); shared science skills at `~/.claude/scistack/hubstack/`. Sync via `~/.claude/scistack/bin/sync-to-claude.sh`. Do NOT drop science skills into `~/.claude/skills/` or `<project>/.claude/skills/` directly.
