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
| Integrity gate before convergence | `/review-integrity-audit` (runs inside `/cascaded-r-rounds`; see Lesson F) |
| Sweep the live site for cohesion/staleness | `/site-cohesion-sweep` (final gate of P-round; checks version strings, HF/GitHub/DOI links, PDF mirrors, explorer data, broken images/links across all surfaces) |
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

## Standing directives (2026-06-26 session — permanent)

Five rules Houston kept having to re-state; encoded here as hard gates:

**A — Convex is the live site.** After EVERY round, write true state to Convex via public HTTP API (`POST https://brilliant-panther-471.convex.cloud/api/mutation`): `paperVersions:bump`, `rRounds:create`, `externalReviews:upsertByLabelDate` (real verdicts; enum `accept|minor-revisions|major-revisions|reject|pending`; source `internal-stage3`), `activityFeed:add`, `papers:setReadinessCap` (96/98/99 per phase). Data writes need no `npx convex deploy`. Static `papers.ts`/SSOT do NOT reach the live site. Full protocol in `/bigbounce-site-sync`.

**B — Per-paper convergence loop.** One owner-agent per paper: INT (multi-vendor+Opus) + EXT (browser) each round → truth-audit verdict-first (patterns 061-064; NEVER fake ACCEPT; never close without source-cited verdict; never fabricate math) → close real items → recompile (0 undef-refs) + `/latex-audit` → Convex+site update → commit. ~30-min heartbeat. Exit gate: 0 new VERIFIED items across ALL 6 papers AND 0 external MAJOR in a full round.

**C — Browser visual QA.** After any site/Convex update: gstack headed browser QA of bigbounce.hubify.app (overview, papers, reviews, data-explorer). Confirm data current+accurate+legible+appealing; fix/flag stale or broken before calling done. Part of every `/bigbounce-site-sync` run.

**D — EXT sweep hardening.** Fresh chats only (never reuse `/c/<id>`). Write manifest per-leg immediately. Per-leg poll cap ~8 polls/10 min then harvest-or-FAILED. Hard ~45-min overall budget; sweep self-terminates. See `/external-review-browser-loop`.

**E — RunPod ALWAYS-backup.** Never single-source pod data. Before any stop AND end of every session AND every ~2hr compute milestone: mirror to local + HuggingFace + Backblaze B2 (+ Convex metadata). Not just before-stop — ALWAYS. See `/pod-backup-before-stop` + `/backup-3plus`.

**F — Independent integrity audit.** After each closure wave, BEFORE declaring convergence, run `/review-integrity-audit`: a separate Opus agent (skeptical stance, NOT told the convergence conclusion) checks (1) INT+EXT prompts hold consistent high journal-referee bar with NO verdict-severity steering; (2) a sample of FALSIFIED/OPINION/OUT-OF-SCOPE dismissals verified against source; (3) papers don't headline the more-favorable of multiple values. Verdict: GENUINE vs ENGINEERED. If ENGINEERED: fix before convergence. Template: `project-context/peer-reviews/INTEGRITY_AUDIT_2026-06-26.md`. Triggered by 2026-06-26 audit catching mild self-favoring bias in EXT prompts + value headlining.

**G — Mandatory per-round PDF hygiene.** Every round that changes a paper MUST, in the SAME bundle: (1) bump `.tex` `\paperVersion` (patch) + `\date`/`\paperTimestamp` to today; (2) recompile (0 undef-refs); (3) re-mirror new PDF to ALL served paths (site/public/papers/ versioned+aliases, public/papers/, source dir) byte-identical; (4) Convex `paperVersions:bump` with REAL new md5/pages; (5) verify served-file md5 == Convex md5 == fresh-compile md5, and page 1 shows new version+date. Committing .tex WITHOUT this = stale served PDFs + reviewers seeing old content (2026-06-26 failure). HARD GATE. Full protocol in `/bigbounce-site-sync`.

---

## Standing directive (2026-07-01 — permanent)

**H — Recalibrated convergence gate.** The paper-convergence gate is RECALIBRATED (Houston explicit decision 2026-07-01). A paper is CONVERGED when: (1) **Grok ACCEPTs AND Gemini ACCEPTs** (0 MAJOR, 0 minor) — real external ACCEPT from the two calibrated referees is still required; AND (2) **every ChatGPT MAJOR is truth-audited as non-real** with a source-cited verdict (already-addressed re-flag / scope misread / referee variance, per patterns 061-064 + `/review-integrity-audit`). ChatGPT's literal ACCEPT is NO LONGER required. Rationale: across RS5→RS6→RS7→RS8 the de-biased ChatGPT referee oscillated reject↔major-revisions on unchanged, honestly-scoped content (P1A reject→major→reject→major on the same paper) while Grok+Gemini gave accept/minor — a maximally-harsh LLM referee's structural floor (it flags *some* major on any real manuscript, even published PRD papers), so the old all-3-ACCEPT gate was an unreachable asymptote, not a quality signal. Loop now drives toward Grok+Gemini ACCEPT (close their minors/majors — moderate + addressable) while dispositioning each ChatGPT major to a non-real verdict. Readiness cap 96 = Grok+Gemini ACCEPT + all ChatGPT majors dispositioned non-real. STILL never fake an ACCEPT, never dismiss a ChatGPT major without a source-cited verdict, never fabricate. This SUPERSEDES the "all 3 reviewers ACCEPT" exit gate wherever it appears in loop prompts.

**H-refined — pattern-066 convergence (Houston explicit 2026-07-01).** The operative convergence test is **"0 genuinely-new real findings"**, NOT a literal single-sweep ACCEPT from any reviewer. A paper is CONVERGED when a fresh external sweep surfaces zero genuinely-new real findings across ALL three reviewers on truth-audit — i.e. every MAJOR/minor from every reviewer is dispositioned as EITHER (a) a source-cited re-flag of already-addressed/disclosed content, OR (b) an honestly-disclosed out-of-scope limitation. Rationale: RS9→RS10 showed even GROK (the "moderate" reviewer) flips MINOR→MAJOR on unchanged/improved content, re-flagging the already-closed GZ1-only independence + disclosed anchor battery + echoed Shamir caveat — referee variance is UNIVERSAL (pattern-066), so demanding a literal ACCEPT from noisy LLM referees is itself asymptotic. Operationally each sweep: truth-audit EVERY finding → genuinely-new real ones MUST be closed in-paper → re-flags/disclosed-limitations are dispositioned with a source-cited verdict → a paper with 0 genuinely-new real findings left is CONVERGED (readiness 96) regardless of the literal verdict word. Integrity stays hard: never fake an accept, never disposition a finding non-real without a source-cited verdict, never fabricate to make a finding go away. This refines readiness cap 96 = "0 genuinely-new real findings across all 3 reviewers, all majors dispositioned."

---

## Standing directive (2026-07-03 — permanent): INT/EXT review routing — NEVER fake, NEVER skip, NEVER fail on the wrong thing

Houston caught (2026-07-03) that recent "reviews" were EXT sub-agent reports with **no raw reviewer text captured** (unverifiable), that ChatGPT was silently dropped, and that INT was skipped entirely. Hard rules going forward:

**I1 — INT reviewer routing (the big one):**
- **Claude/Anthropic INT leg = the running Claude Code agent itself, on Houston's subscription — NEVER the Anthropic API.** You ARE Claude Code running on it. NEVER ask Houston for an Anthropic API key, NEVER "fail" an INT leg because the Anthropic API is disabled. Run the Claude leg as a Claude Code sub-agent (or the main loop) reading the full paper + source + context. If a round is instead being run inside Codex/another agent, that agent is the "Claude-equivalent" leg via its own subscription — use it, not the OpenAI API.
- **OpenAI INT leg = OpenAI API** (o3/gpt) when running inside Claude Code; or the Codex agent when the round runs there.
- **Grok/XAI INT leg = XAI API.** **Gemini INT leg = Gemini API** (2026-07-05 status: all stored Gemini API keys 403/billing-blocked — Gemini's INT perspective is covered via browser EXT until Houston supplies a billing-enabled key; never fail the round on it).
- **The INT verdict matrix MUST always report ALL vendor columns (Claude-subagent + OpenAI + Grok [+ Gemini when key works]) — NEVER summarize INT as the Claude column alone (2026-07-05 lesson: doing so overstated 'INT 6/6 ACCEPT'). API legs MUST use the best input modality (OpenAI native-PDF via Files API; note modality per leg) — pdftotext is a degraded fallback and must be labeled as such. Every API-vendor MAJOR gets the same per-finding source-cited truth-audit as EXT findings.**
- **Perplexity is OPTIONAL** (not part of the core INT/EXT set; assess adding later). Do NOT make it a required key; do NOT fail the pipeline on its absence/quota.
- `tools/v3_native_pdf_review.py` must NOT require ANTHROPIC_API_KEY or PERPLEXITY_API_KEY, and must route the Claude leg to a Claude Code sub-agent, not the API.

**I2 — INT API failures NEVER stop EXT.** EXT (browser) reviews are independently valuable and must run regardless of any INT API billing/quota problem. Do EXT first if needed, then INT via Claude Code sub-agents. Never let an INT infra failure become an excuse to skip EXT.

**I3 — Why INT still matters:** EXT reviewers (browser ChatGPT/Grok/Gemini) do NOT get the full history, source code, data, and context. INT (with the full repo + context as source-of-truth) is the complement that catches what EXT can't. Run BOTH.

**I4 — EXT reviews are mandatory + VERIFIABLE + HEADED.** You know how to run the browser EXT (done hundreds of times) — never ask how. Run ChatGPT + Grok + Gemini in Houston's visible gstack browser. **Every leg MUST save the COMPLETE raw reviewer response text + a screenshot** to `project-context/peer-reviews/EXT_real/`; the orchestrator READS + verifies each raw response before recording any verdict. Never record a verdict from a label alone. A leg that produced no output is FAILED, not a verdict.
  - **HEADED BROWSER IS MANDATORY FOR EXT (2026-07-05, permanent — never repeat this mistake).** The gstack `browse` tool defaults to a **HEADLESS** browser, which CANNOT do the EXT review: it cannot pass ChatGPT's Cloudflare bot-check, cannot complete Google/Gemini OAuth, and reliably loses/crashes reviewer sessions; cookie-import into headless is flaky and does NOT substitute. Before ANY EXT sweep you MUST switch to the HEADED browser: `B=~/.claude/skills/gstack/browse/dist/browse; $B cleanup; $B connect` — `connect` launches a headed Chromium with the gstack extension (port 34567, real Chrome, `Mode: headed`) Houston can see + log into. Confirm `Mode: headed` + healthy, have Houston sign into any logged-out reviewer in that headed window, THEN run the sweep. If sessions drop mid-round, reconnect headed (`$B connect`) — never fall back to headless or fake a verdict off a login-wall. `$B disconnect` returns to headless after the EXT round. This is the `/connect-chrome` skill. Houston should never have to remind you to use the headed browser.
  - **Gemini EXT:** log in via **houston@bamf.com** Google account (Ultra plan, higher limits) — already in the gstack browser. It has **Deep Research + Deep Think** via the `+` icon.
  - **ChatGPT EXT:** currently **Extended Thinking Pro**; **Deep Research** also available.
  - **Deep Research / Deep Think** give richer EXT content but take much longer — run them **every other EXT round** (or when a paper is near-converged and worth the deep pass), not every round.

**I5 — Self-improvement is standing:** document every review-process learning here + in the scistack review skills (`~/.claude/scistack/`) as it happens. "We gotta do better" — no repeat of the same mistake.

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
