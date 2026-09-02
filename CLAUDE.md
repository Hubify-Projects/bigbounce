# CLAUDE.md — bigbounce

> **APPROVED PUBLICATION ARCHITECTURE — 2026-08-04:** Read
> `project-context/PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md` before paper,
> site, archive, endorsement, or submission work. Use the three-program map.
> Current P3 is an integrated supporting release, not a standalone paper; P5
> is a standalone AJ companion. Never restore the old six-equal-candidates
> framing.

## Ops center

Program architecture, plan, and runbooks live in `ops/` (canonical home; indexes,
does not duplicate). `ops/ARCHITECTURE.md` = system + data-flow + invariants;
`ops/PLAN.md` = mission/terminal-criteria/phases/decision-log; `ops/RUNBOOK.md` =
per-tick commands + recovery plays. Paper status stays canonical in
`project-context/SSOT/`; round protocol in the scistack `bigbounce-r-round/SKILL.md`.

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

**A — Convex is the live site.** After EVERY round, write true state to Convex via public HTTP API (`POST https://brilliant-panther-471.convex.cloud/api/mutation`): `paperVersions:bump`, `rRounds:create`, `externalReviews:upsertByLabelDate` (real verdicts; enum `accept|minor-revisions|major-revisions|reject|pending`; source `internal-stage3`), `activityFeed:add`, `papers:setReadinessCap` (96/98/99 per phase). Data writes need no `npx convex deploy`. Static `papers.ts`/SSOT do NOT reach the live site. Full protocol in `/bigbounce-site-sync`. **Readiness caps update the moment a ladder stage completes (R→96, D→98, P→99) — stale caps are dishonest data; Convex is the ONLY readiness source and every static mirror (live-status.ts, papers.ts, ProgressViz) updates in the same bundle (2026-07-07 lesson: site sat at reset-era 76-80 + a July-3 banner while papers were ladder-99).**

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
- **Claude/Anthropic = DISABLED for the active BigBounce campaign.** Do not call
  Anthropic APIs, spawn Claude Code subscription reviewers, or count historical
  Claude outputs toward a current board. Preserve any legacy output only as
  nonconforming diagnostic evidence.
- **OpenAI INT leg = Codex CLI / ChatGPT subscription only — NEVER the OpenAI API.** Run it with `OPENAI_API_KEY` and `CODEX_API_KEY` unset so authentication cannot silently switch away from the subscription. This applies on every host, including Claude Code: use a Codex CLI worker for the independent OpenAI perspective.
- **Grok/XAI INT leg = XAI API.** **Gemini INT leg = Gemini API** (2026-07-05 status: all stored Gemini API keys 403/billing-blocked — Gemini's INT perspective is covered via browser EXT until Houston supplies a billing-enabled key; never fail the round on it).
- **The INT verdict matrix MUST always report ALL available vendor columns (host subscription agent + OpenAI-via-Codex-subscription + Grok [+ Gemini when key works]) — NEVER summarize INT as one column alone. API legs are xAI/Grok and Google/Gemini only; every API-vendor MAJOR gets the same per-finding source-cited truth-audit as EXT findings.**
- **Perplexity is OPTIONAL** (not part of the core INT/EXT set; assess adding later). Do NOT make it a required key; do NOT fail the pipeline on its absence/quota.
- `tools/v3_native_pdf_review.py` must NOT require `ANTHROPIC_API_KEY`,
  `OPENAI_API_KEY`, or `PERPLEXITY_API_KEY`; its active direct APIs are
  Gemini/Grok plus optional Perplexity.

**I2 — INT API failures NEVER stop EXT.** EXT (browser) reviews are independently valuable and must run regardless of any INT API billing/quota problem. Do EXT first if needed, then continue policy-compliant INT work. Never let an INT infra failure become an excuse to skip EXT.

**I3 — Why INT still matters:** EXT reviewers (browser ChatGPT/Grok/Gemini) do NOT get the full history, source code, data, and context. INT (with the full repo + context as source-of-truth) is the complement that catches what EXT can't. Run BOTH.

**I4 — EXT reviews are mandatory + VERIFIABLE + HEADED.** You know how to run the browser EXT (done hundreds of times) — never ask how. Run ChatGPT + Grok + Gemini in Houston's visible gstack browser. **Every leg MUST save the COMPLETE raw reviewer response text + a screenshot** to `project-context/peer-reviews/EXT_real/`; the orchestrator READS + verifies each raw response before recording any verdict. Never record a verdict from a label alone. A leg that produced no output is FAILED, not a verdict.
  - **HEADED BROWSER IS MANDATORY FOR EXT (2026-07-05, permanent — never repeat this mistake).** The gstack `browse` tool defaults to a **HEADLESS** browser, which CANNOT do the EXT review: it cannot pass ChatGPT's Cloudflare bot-check, cannot complete Google/Gemini OAuth, and reliably loses/crashes reviewer sessions; cookie-import into headless is flaky and does NOT substitute. Before ANY EXT sweep you MUST switch to the HEADED browser: `B=~/.claude/skills/gstack/browse/dist/browse; $B cleanup; $B connect` — `connect` launches a headed Chromium with the gstack extension (port 34567, real Chrome, `Mode: headed`) Houston can see + log into. Confirm `Mode: headed` + healthy, have Houston sign into any logged-out reviewer in that headed window, THEN run the sweep. If sessions drop mid-round, reconnect headed (`$B connect`) — never fall back to headless or fake a verdict off a login-wall. `$B disconnect` returns to headless after the EXT round. This is the `/connect-chrome` skill. Houston should never have to remind you to use the headed browser.
  - **Gemini EXT:** log in via **houston@bamf.com** Google account (Ultra plan, higher limits) — already in the gstack browser. It has **Deep Research + Deep Think** via the `+` icon.
  - **ChatGPT EXT:** currently **Extended Thinking Pro**; **Deep Research** also available.
  - **Deep Research / Deep Think** give richer EXT content but take much longer — run them **every other EXT round** (or when a paper is near-converged and worth the deep pass), not every round.

**I5 — Self-improvement is standing:** document every review-process learning here + in the scistack review skills (`~/.claude/scistack/`) as it happens. "We gotta do better" — no repeat of the same mistake.

**I6 — Figure-image propagation after ANY numeric correction (HARD GATE).** After ANY numeric-value correction, the propagation sweep MUST include regenerating every FIGURE IMAGE that renders the value — a text grep CANNOT see values baked into PNGs/PDF figures. Inventory every `\includegraphics` in the paper and check each figure for the corrected value; regenerate each stale figure (prefer the committed generator script; else recreate via matplotlib; else patch the label), re-mirror byte-identical to all served figure paths, and VERIFY by rendering the figure page of the recompiled PDF (not a filename check). Trap (2026-07-06): P1A Fig-1 `fig_theory_map.png` carried the superseded matter-bounce `f_NL=-35/8` through TWO review rounds after the v110 text sweep moved the body uniformly to `-35/16` — the stale value lived only inside the PNG. Fixed in v1A.0.112. Also encoded in canonical spec §4 (directive-G hygiene).

---

## Standing directive (2026-07-16 — Houston explicit): N — CLAUDE-STACK ROUTING, CODEX PAUSED

Houston (verbatim): "i don't want you using codex that is why i resumed this
here in claude instead bc i was burning too much usage on codex and needed
fresh prespective and usage window here in claude" and "use claude and claude
code/cmux per the rules etc use fable 5 or opus-4-8 for the orchestrator and
the other smaller/faster/cheaper models for workers/leads via terminal/cmux etc
which should be documented and cover both our internal reviews and external
api/cli reviews etc etc".

This SUPERSEDES directive I1's "Claude/Anthropic = DISABLED" and every
"OpenAI-perspective-via-Codex-CLI" routing rule, for as long as it stands:

- **Codex/OpenAI = PAUSED entirely** (quota protection). Never invoke the
  `codex` CLI, never pass `--with-codex` to `tools/int_wave.sh`, never set
  `BIGBOUNCE_CODEX_SUBSCRIPTION_ENABLED=1`. OpenAI API remains forbidden. A
  missing Codex leg is recorded as **absent**, never faked or back-filled.
- **Orchestrator** = Claude Fable 5 (or Opus 4.8): planning, truth-audits,
  scientific judgment, integration, acceptance.
- **Workers/leads** = smaller/faster/cheaper Claude models via Claude Code
  subagents / terminal / CMUX: Sonnet for bounded execution (edits, recompiles,
  mirrors, packaging), Haiku for polling/watchers, per `/loop-model-routing`.
  CMUX stays READ-ONLY for BigBounce until You.md atomic claims, heartbeats,
  overlap detection, and isolated worktrees are acceptance-tested.
- **INT review board legs** = (1) Claude reviewer subagent — Opus-tier,
  exact-PDF-bound, de-biased referee prompt, full raw report saved to
  `project-context/peer-reviews/INT_v3/...` before any verdict is recorded —
  plus (2) direct Grok/xAI API and (3) direct Gemini API legs, each with raw
  receipts. Verdict matrix reports every attempted leg; failed legs stay FAILED.
- **EXT** (headed-browser ChatGPT/Grok/Gemini) is unchanged in principle but
  ChatGPT-subscription EXT legs should not be burned without Houston's go.
- All integrity rules unchanged and absolute: exact SHA-256 binding, venue
  binding, truth-audit before closure, never fake an ACCEPT, never fabricate,
  no readiness uplift without current exact-artifact evidence.

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


## Standing directive (2026-07-09 — permanent): J — LITERAL 0/0/0 BAR + NEVER-IDLE LOOP

Houston explicit, final: the program exit bar is LITERAL **0 MAJOR / 0 MINOR / 0 REJECT from
every reviewer** (INT Claude-subagent/OpenAI/Grok/Gemini + EXT ChatGPT/Grok/Gemini) on every
paper. Directive-H and "0 genuinely-new findings" are honesty tools, NOT exit conditions.
**The loop never idles:** every cron tick runs live improvement work on every paper below the
bar — EXT rounds on some papers while INT closure/science runs on the others, in parallel,
always. A paper whose open-item list closes re-tests immediately. Orchestrator = Fable 5
(planning only); all subagents = Opus. "Idle — exit condition holds" is banned while any
verdict word is below ACCEPT. Houston must never have to re-ask.

## Standing directive (2026-07-10 — Houston explicit): K — TWO-CLEAN-WAVES EXIT

Houston's words: "keep the loop going until two clean waves then prep arXiv wave-1."
This SUPERSEDES directive J's literal 0/0/0 verdict-word bar as the loop exit
condition. Exit = two CONSECUTIVE full waves (every reviewer leg we have access
to, every paper) in which the truth-audit finds **0 genuinely-new findings** —
every finding fingerprint-matches a canonical disposition (DISPOSITIONS/<P>.md).
A genuinely-new finding on ANY paper resets that paper's clean-wave count (found
items are closed with real edits/science first, then re-tested). Integrity rules
unchanged: never fake an ACCEPT, never fabricate, every leg saves its raw before
any verdict is recorded, dispositions stay source-cited. On exit: finalize the
wave-1 arXiv kit (bundles re-verified against final versions, walkthrough
current) and report to Houston for submission clicks. H17F+H17G were clean, but
P2's verified Claude re-run then surfaced genuinely-new presentation items —
P2's count reset; the clock restarts after v1.7.112 closes them.

## Standing directive (2026-07-11 — Houston explicit): L — ACCEPT-BAR RESTORED, OPEN-COMPUTE CAMPAIGN

Houston (verbatim): "shouldn't the bar be that all papers are pushed to Accepted
by all reviewers." Directive K's two-clean-waves bar is a CHECKPOINT, not the
finish line — it proved 0-genuinely-new-findings, but the program target returns
to ALL-ACCEPT from every reviewer leg. The path is NOT more text waves (verdict
words oscillate on unchanged content — measured) and NEVER prompting tricks or
watered-down claims. The path is CLOSING THE OPEN-COMPUTE/VENUE LEDGER with real
science: P4 image-level end-to-end classifier injection (GPU/RunPod) + per-pixel
confusion + generative null; P2 channel-native Fisher via an adopted covariance
surrogate + full cubic in-in transmission + Zenodo DOI; P3 uniform end-to-end
held-out re-inference (RunPod) + ApJS venue variant; P5 Zel'dovich RSD
reconstruction + higher-N environment confusion; P1U regulated NJL gap equation.
Each closure: real computation, committed artifacts, integrated honestly, full
re-test wave. Waves continue to MEASURE movement (never to farm verdicts).
RunPod authorized per existing directives (backup-3plus applies). Integrity
rules unchanged and absolute.

## Standing directive (2026-07-12 — Houston explicit): M — ALL-A GRID IS THE TERMINAL CRITERION

Houston (verbatim): "goal continues until all papers are accepted by all models
and that is visually shown on the site on this grid with all A across all models
and papers 100% that is the objective criteria that is the only thing that will
satisfy the goal." The CURRENT column of the verdict grid on /reviews must show
ACCEPT for every paper × every reviewer leg. Nothing less exits the loop; the
cron NEVER stops and NO paper's work pauses until then. Always parallel work on
all 5 papers, every tick. The honest levers (in proven order of effect): real
compute/science closures; venue matching (P3-ApJS flip PROVEN — ApJS-framed
reviews are legitimate reviews of the same science); full presentation overhauls
targeting the REJECT raws' own words (PRD abstract format, de-duplication,
consolidation — editorial rigor is in-scope, watering down science is NOT);
closing every minor-list every round. Site reviews/status update with every
commit; the grid renders newest rounds on the LEFT. Integrity rules absolute
and unchanged: never fake an ACCEPT, never prompt-game, every leg saves its raw.

## Standing directive (2026-07-23 — Houston explicit): M-AMENDED — ALL-A GRID OVER ACTIVE LEGS

Houston (verbatim): "amend directive M to the legs we actually run." Directive
M's terminal criterion is amended: the CURRENT column of the /reviews grid must
show ACCEPT for every paper × every **ACTIVE** reviewer leg — under directive N
that is **Grok API, Gemini API, and the Claude Opus INT leg**. The
OpenAI/ChatGPT column is EXCLUDED from the criterion while directive N's pause
stands: its historical cells remain displayed (annotated frozen, never deleted,
never faked), and it rejoins the criterion automatically if Houston re-enables
an OpenAI leg. The /reviews all-A meter counts active legs only and must say
so. All integrity rules unchanged: never fake an ACCEPT, never prompt-game,
every leg saves its raw before any verdict is recorded.

## Standing directive (2026-07-23 — Houston explicit): P — PUBLICATION-READINESS COMPOSITION

Houston (verbatim core): "the venue/submission should be a separate step not
factored into the readiness for publishing - same with my independent human
review … my own final personal review … the last 1-5% … if I mark it as ready
and good it will be 100% readiness for publishing and then go on to the next
steps of actually getting them published which includes the venue / submission
/ endorsements."

**Publication readiness** (the single headline % per paper) is composed ONLY of:
science closure (25) + evidence & reproducibility (25) + automated review
convergence (25) + packaging & PDF hygiene (20) + **Houston's final personal
review (5)**. A paper with the four agent gates complete sits at **95** and
reaches **100 only via Houston's explicit per-paper sign-off** (quote recorded
in SSOT, /readiness-cap-99 unchanged in spirit: 100 requires his words).

**Publishing phase (separate, NOT in the score):** arXiv endorsement, venue
selection/submission clicks, journal peer review, and independent human
scientific review. These are tracked as next-phase steps on /status and
/publish and must never subtract from publication readiness.

**Automated review convergence criterion (achievable by construction):**
converged = 0 genuinely-new-real findings outstanding across ACTIVE legs
(directive M-AMENDED: Grok API + Gemini API + Claude INT; paused legs excluded)
on the current exact PDFs, per directive H-refined truth-audit rules. Verdict
WORDS are diagnostic feedback, never the gate. Every finding still gets a
source-cited disposition; genuinely-new-real items still close before
convergence is claimed. Integrity rules unchanged and absolute.

## Standing directive (2026-08-05 — Houston explicit): Q — PURE-CONTRIBUTION PUBLICATION FRAMING + REPRODUCIBILITY-FIRST LAB

Houston's core points (verbatim source: project-context/prompt-history.md,
2026-08-05 entry):

- **Q1 — No mistake-narration in published works.** Papers/datasets/releases
  are presented in their pure form: the question, the method, the results, the
  contributions (equations, math, models, datasets). Never frame a published
  work around redoing/fixing our own earlier errors, lost data, or stale
  artifacts. A work whose thesis is "we didn't do X right, so this paper redoes
  X" is NOT a foundational publication unless the redo itself is genuinely
  novel science. Internal truth-audit history stays internal (SSOT,
  project-context) — it is process evidence, not paper content.
- **Q2 — Reproducibility manifests are mandatory.** Every research program AND
  every individual experiment/simulation/compute run gets a manifest: external
  data sources with links (HF/DESI/etc.), APIs used, exact scripts, compute
  venue (local = ~free vs RunPod GPU), reproduction cost estimate, and
  wall-clock time. The lab-level goal: BigBounce is the flagship reproducible
  lab for the Hubify platform; everything must be portable into Hubify and
  reproducible individually and holistically. The full-reproduction pass is
  the FINAL pre-publication test.
- **Q3 — Keep both site surfaces.** The Research Programs grouping AND a
  complete flat papers list page. Paper titles/descriptions must carry
  plain-English purpose labels (e.g. namaster-proof needs a clear subtitle),
  not jargon-only names.
- **Q4 — Nothing viable gets lost.** Any narrowing/split/retirement of a paper
  must preserve a documented disposition trail; periodically audit history for
  viable unpublished science (e.g. the no-go-pathways survey) and either
  resurrect it under a program or record explicitly why not.

## Standing directive (2026-09-02 — Houston explicit): R — VISION GOVERNANCE; REVIEW CONVERGENCE IS A GATE, NOT A PRODUCT

Root cause recorded in `project-context/PORTFOLIO_DECISION_2026-09-02.md` and
`PAPER_GENEALOGY_2026-09-02.md`: from 2026-03 to 07 the campaign optimized for
review convergence while the lab's own ranked next-science list went
unpursued and the lineup grew by splits/rescues. Houston: "allowing it to
derail research is clearly a major problem we want to solve." Rules:

- **R1 — Read the ledger first.** Every session starts with
  `project-context/VISION.md` and `project-context/NEXT_SCIENCE_LEDGER.md`
  and ends by updating the ledger. Running review rounds while the top
  ledger item is untouched requires a written reason in the session record.
- **R2 — Convergence budget.** At most two consecutive review rounds on a
  paper without an intervening science or scope decision; stop rounds when
  the remaining findings are genre/length/venue. Verdict words are never a
  goal (directive P stands).
- **R3 — Lineup changes are decisions.** Any split/merge/retire/rescope is
  recorded in `PAPER_LINEAGE` with the original claim beside the new claim.
- **R4 — Drift audit.** Re-run the vision-vs-lineup audit at any lineup change
  and at least every 30 days; commit the result.
- **R5 — Hubify inherits R1–R4** as platform rules
  (`HUBIFY_RESEARCH_GOVERNANCE_2026-09-02.md`).
- **R6 — Declared motivation, evidence-graded claims.** The lab's guiding bet
  is stated in `VISION.md`; every claim is stated at exactly its evidential
  strength and nulls are published as nulls.
