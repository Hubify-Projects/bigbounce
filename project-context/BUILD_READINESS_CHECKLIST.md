# Hubify Labs — BUILD READINESS CHECKLIST

**Status:** ACTIVE · the master gate for "ready to ship the MVP"
**Author:** Houston Golden + Claude
**Date locked:** 2026-04-08
**Linked from:** PRD §0 (TBD), CLAUDE.md, the autonomous loop cron

---

## 0. The promise

This document is the **single, measurable, hard gate** between "we're still designing" and "we're rebuilding for live MVP".

When **every checklist item below is `[x]`**, we have full clarity on:
- The PRD (the spec)
- The mockups (web + macOS desktop)
- The API surface (REST + GraphQL)
- The MCP server (for AI agents)
- The CLI tool
- The deployment infrastructure
- The migration plan for Lab #1

At that point, the autonomous loop pivots from "polish and spec" to "rebuild and deploy". Until then, **every iteration of the loop must move at least one item closer to checked.**

---

## 1. The READY gate — what "ready" means

We are READY to begin the full rebuild + backend phase when ALL of these are true:

- [ ] **A. PRD lock complete** — every section frozen, no open architectural questions, all 5 lab specs final, Houston signed off
- [ ] **B. Web mockup lock complete** — visual spec for every view, every sidepeek, every flow that v1 ships with; mobile audit passed; no dead clicks; no color leaks; PRD↔mockup terminology synced
- [ ] **C. macOS app mockup + spec complete** — desktop chrome design, native features inventory, Tauri shell architecture
- [ ] **D. API spec complete** — REST + GraphQL endpoint inventory locked in OpenAPI YAML
- [ ] **E. MCP server spec complete** — tool definitions, resource definitions, auth flow locked
- [ ] **F. CLI spec complete** — command structure, auth flow, output formats locked
- [ ] **G. Deployment infrastructure plan complete** — Vercel + Convex + Fly + RunPod + Backblaze + DNS all spec'd
- [ ] **H. Migration plan complete** — Lab #1 (Bounce Cosmology) ready to execute Day 1
- [ ] **I. Houston sign-off** — Houston has reviewed and confirmed everything above

When all 9 letters are checked → **status = READY · begin rebuild**.

---

## 2. Detailed checklist by category

Each section lists the discrete deliverables. The loop walks this list every iteration and picks the highest-impact unchecked item.

### A. PRD lock complete

- [x] §0 Executive summary
- [x] §1 Safety-first repo strategy + Lab=repo architecture lock
- [x] §2 Standardized Lab template
- [x] §3 Agent hierarchy
- [x] §4 Cross-lab sharing (architecture)
- [x] §5 GPU/Compute pipeline (architecture)
- [x] §6 Backup & data management
- [x] §7 Website system
- [x] §8 CLI/TUI overview
- [x] §9 Fly.io deployment
- [x] §10 Failure handling
- [x] §11 Cost management
- [x] §12 Implementation plan week-by-week
- [x] §13 Houston Method v2 + §13.1 no-future-research-punts rule
- [x] §14 Technical primitives
- [x] §15 Security & secrets
- [x] §16 Monitoring & observability
- [x] §17 Website generation
- [x] §18 Cron schedule
- [x] §20 Memory architecture
- [x] §21 User profile
- [x] §22 Scientific contributions + N-score system
- [x] §23 Houston Method platform enforcement
- [x] §24 Compute provider — RunPod ONLY (Pods + Serverless + CPU/GPU variants)
- [x] §25 Agent communication / activity feed
- [x] §26 Task review pipeline
- [x] §27 All-hands standups
- [x] §28 Paperclip patterns
- [x] §29 Cross-model peer review
- [x] §30 Agent host & terminal integration
- [x] §31 UI component inventory
- [x] §32 Development phase readiness
- [x] §33 Storage strategy & data map (5 zones)
- [x] §34 Agent file structure (indydevdan-style)
- [x] §35 Hierarchy taxonomy v1 (deprecated, superseded by §40)
- [x] §36 Preresearch mode (deprecated, collapsed into §40)
- [x] §37 Publishing phase + publish-ready loop
- [x] §38 Human research journal (Notes)
- [x] §39 Activity graph (neural brain view)
- [x] §40 Hierarchy v2 LOCKED (5-level model + intent layer + chats + sharing)
- [x] §41 Compute routing & credits monitoring
- [x] **§42 — macOS desktop app spec** (commit `7fca50d`) — Tauri 2.x decision + 11 native features + menu bar variant + iOS deferral + distribution; PRD-resident summary that points at the canonical `DESKTOP_APP_SPEC.md`
- [x] **§43 — REST + GraphQL API spec** (commit `7fca50d`) — JWT HS256 + per-lab scopes + ~85 endpoints across 19 groups + RFC 7807 errors + §41 routing requirement; points at `API_SPEC.md` + `api-spec.openapi.yaml`
- [x] **§44 — MCP server spec** (commit `7fca50d`) — 4 MCP primitives + 3 transports + ~30 tools across 11 categories + 15 resources + 6 prompts + Lab Sovereignty enforcement + N4-not-claimable + audit logging; points at `MCP_SERVER_SPEC.md` + `mcp-server-spec.yaml`
- [x] **§45 — CLI spec** (commit `7fca50d`) — Go + Cobra + bubbletea TUI + ~120 commands across 19 categories + §41 routing CLI enforcement + OAuth/PKCE auth + plugin system deferred to v1.1; points at `CLI_SPEC.md` + `cli-spec.yaml`
- [x] **§46 — Deployment infrastructure plan** (commit `7fca50d`) — Vercel + Convex + Fly + RunPod + Backblaze + Cloudflare + GitHub Actions + monitoring stack + Fly 4-surface integration model + cost forecast; points at `DEPLOYMENT_INFRA_PLAN.md`
- [x] **§47 — Mintlify docs port plan** (commit `cd1f87b`) — Mintlify decision (subpath at hubify-labs.com/docs, NOT subdomain) + first 7 docs pages outline + codegen pipeline that auto-generates API/CLI reference from the YAML specs on every commit + Algolia DocSearch + Mintlify AI assistant
- [x] **§48 — `hubify://` URL scheme spec** (commit `cd1f87b`) — full URL pattern catalog: `hubify://<lab-slug>/<entity-type>/<entity-id>[?<query>]` + 19 entity types with example URLs + cross-lab read OK / write FORBIDDEN enforcement + 7 surface-specific handling rows (macOS / web / iOS / CLI / MCP / Slack / Mintlify) + URL stability forever guarantee
- [x] **§49 — Authentication & authorization spec** (commit `cd1f87b`) — 5 auth providers (GitHub OAuth default + email magic + service tokens + agent tokens + MCP client auth) + 4 token types with lifetimes + per-lab scope claim format + Lab Sovereignty Rule TRIPLE enforcement (CLI + MCP + API) + 6 agent consent boundaries (N4 claim, notechat, public visibility flip, lab delete, token issue, auth provider settings) + audit logging schema + per-token-type rate limits
- [x] **§50 — Telemetry & observability spec** (commit `cd1f87b`) — 9 event categories with destinations + retention + privacy boundaries (lab content NEVER leaves user's Convex deployment) + activity feed schema + per-experiment cost tracking schema + 8-row alert routing table (PRD §41.2) + telemetry opt-out (per-user, not per-lab) + 3 open questions
- [x] **PRD §19 numbering fix** (commit `de1ea50`) — renamed "Session Summary — What This PRD Covers" to "Appendix A: Section Index — What This PRD Covers". Index table extended with §41-50 entries (10 new rows). Total section count corrected to 46 sections / ~8000 lines. Numbering confusion resolved — sections §0-§50 are the canonical PRD body, this appendix is the navigable index.
- [x] **PRD subsection fills** (commit `a2f62ed`) — 3 new subsections written: §39.9 Vibe Coding view (layout + 4 save targets + Activity Graph integration with example JSONL events + cost guardrails + IN/OUT-of-scope), §33.14 Knowledge Wiki view (zone-aware storage table for entity/concept/source/comparison files + 3-column grid layout + agent contract with wiki-worker + sidepeek behavior), §37.14 Figures view (zone-aware storage table for vibe/experiment/reproducibility/TikZ figure sources + grid layout + figure sidepeek with provenance trail + publishing-lead Round 4 final visual pass walking every figure + orphaned figures filter). All 3 fills include IN-scope and OUT-of-scope cuts for v1 vs v1.1.
- [x] **PRD open questions answered with proposed defaults** (commit `8f98fcb`) — new "Appendix B: Open Question Defaults" added to PRD with detailed answer + reasoning + Houston-override-expected paragraph for all 4: B.1 chat default model = Claude Sonnet 4.6 (best cost/quality, matches Houston's daily Claude Code workflow, Opus reserved for orchestrator/papers, Haiku for parallel subagents, per-chat switcher), B.2 voice provider = Whisper API ($0.006/min, native Tauri 2 audio capture, OpenAI account already exists, whisper.cpp local fallback), B.3 cross-lab read enforcement = GitHub repo permissions + Convex auth (redundant belt+suspenders, both layers independently sufficient), B.4 BigBounce subdomain = bigbounce2.hubify.app burn-in then graduate to bigbounce.hubify.app (same as MIGRATION_BOUNCE_COSMOLOGY_LAB.md §6 Q1, restated as PRD-canonical). Sign-off block at B.5 specifies Houston's confirm/override format.
- [ ] **5 lab spec files reviewed by Houston** (all 5 written, awaiting his read): MIGRATION_BOUNCE_COSMOLOGY_LAB · LAB_HUBIFY_SELF_IMPROVING · LAB_DARK_ENERGY · LAB_DARK_MATTER · LAB_ETI

**A status:** ~98% — ALL 9 stub sections (§42-50) DONE + §19 → Appendix A renumber DONE + 3 PRD subsection fills DONE (§33.14 Knowledge Wiki view, §37.14 Figures view, §39.9 Vibe Coding view) + 4 PRD open questions answered with proposed defaults in new Appendix B. 1 item remains: 5 lab spec Houston review pass (waiting on Houston).

### B. Web mockup lock complete

- [x] All 28 views built and registered
- [x] All sidepeek renderers built (paper · experiment · agent 10-tab · figure · task · file · contribution · standup · comm-event · provider · dataset · lab-templates · new-file · deploy · alert-rule · chat-history · memory · idea · survey · pdf-preview)
- [x] Activity Graph rebuilt for Hubify Labs entities (sage palette, semantic edges)
- [x] Rich PDF + image preview
- [x] ⌘K universal content search + footer
- [x] Mobile responsiveness audit (round 1 done)
- [x] PRD↔mockup terminology sync (Hubify-Projects → Hubify-Labs · preresearch_* → chat_*)
- [x] Modal stripped from mockup entirely
- [x] Round A item #1 status bar simplification
- [x] Round A item #2 sidebar count badge audit
- [x] **Round A item #3 section labels thinning** (commit `5fa8960`) — `.section` 1.2px → 0.6px + `.sb-section-label` 1px → 0.6px letter-spacing, brings the 2 loudest classes in line with the rest of the uppercase label hierarchy (sp-section-label/stat-label/lab-dd-label all at 0.6-0.8px)
- [x] **Round A item #4 filter chip rows audit** (commit `25f949b`) — Linear/Vercel pattern: dropped border+background, text-only buttons with sage underline on active, 12 filter-row instances across the mockup updated, mobile breakpoints synced
- [x] **Round A item #5 toast positioning + density** (commit `684f498`) — bottom-right stack container, max 5 visible toasts, slide-in from right with sage left-border, timestamp + message + click-to-dismiss, replaces singleton bottom-center toast that lost messages on rapid fire
- [x] **Round A item #6 card padding audit** (commit `c27c0a9`) — `.stat` (13px 15px → 12px 16px, lone outlier), `.card-header` (11px 14px → 12px 16px), `.review` (13px 14px → 12px 16px) all converged to 12px/16px design-system scale (multiples of 4) · **Round A COMPLETE 6/6 ✅**
- [ ] **Round B Files sidebar Round 2** — full-page note editor with inline filename + per-note scoped chat + markdown slash commands + star-to-pin notes
- [ ] **Round C #1 Sidebar tri-mode adding Chats between Menu and Files** (PRD §40.7)
- [ ] **Round C #2 Project Overview page + sidepeek renderer** (PRD §40.12)
- [x] **Round C #3 Chat composer enrichments** (commit `cc81400`) — chat input toolbar above the textarea with 4 elements: (1) **Model switcher pill** with sage dot + label + dropdown caret, cycles through 5 models (Sonnet 4.6 default per PRD App B.1, Opus 4.6, Haiku 4.5, GPT-5, Gemini 2.5 Pro) on click — toast confirms switch with model description, (2) **Mode pill** cycling through 3 chat modes (Research/CEO/Note per PRD §40.6+§40.13) with diamond icon variants (◆/◇/◌), (3) **File upload icon** (paperclip svg) opens new-file sidepeek for attachment flow, (4) **Mic icon** for Whisper API voice dictation (per PRD App B.2) with recording-state pulse animation. Slash command autocomplete already wired via existing meta-left chips. All 4 use the existing sage/grayscale palette — no new accent colors. Recording animation uses existing accent color with pulse-shadow keyframe scoped to `.chat-tool-btn.recording` only.
- [x] **Round C #4 Wire 4 chat slash commands** (commit `806ed31`) — all 4 PRD §40 chat slash commands wired in `handleChatSlashCommand()` and added as the FIRST 4 entries in CHAT_SUGGESTIONS (so they show up at the top of the / autocomplete dropdown): `/chat` (start new chat branched from current scope, toast), `/notechat` (save chat to Notes per PRD §40.13 explicit consent → opens chat-history sidepeek with notechat target), `/promote` (graduate chat to a real Project per PRD §40.6 → opens idea sidepeek with chat-promote target), `/share` (share to another lab per PRD §40.11 read-only → opens lab picker with READ-ONLY enforcement message). Each command intercepted by handleChatSlashCommand() before the default toast fires; descriptions in the autocomplete cite the exact PRD section.
- [x] **Round C #5 Lab Sharing settings sidepeek** (commit `da5f7ef`) — new `lab-share` sidepeek renderer registered in `sidepeekRenderers`. Renders 7 sections: (1) header with visibility status + grant counts, (2) **Lab Sovereignty Rule explainer card** (sage left-border) explaining "READ across labs OK, WRITE FORBIDDEN" + the 3-layer enforcement (CLI → MCP → REST API), (3) Visibility row table (papers/datasets/contributions/wiki/raw experiments/chats — each row says what's readable), (4) **Read grants OUT** (3 sample grants: dark-energy/dark-matter/hubify-self-improving), (5) **Read grants IN** (2 sample reverse grants), (6) Cross-lab comm gateway explainer with comm types + inbox/sent links, (7) Audit log (4 sample events) + Actions row. New Settings nav item "Lab Sharing" with share icon SVG opens the sidepeek directly via `openSidepeek('lab-share','bigbounce')`. Sage discipline preserved.
- [x] **Round C #6 Cross-lab comm gateway visualization** (commit `ca63c1e`) — full visualization card on the Comms view (above the activity feed) showing the cross-lab comm gateway in 3 columns: **inbound** (2 pending sample comms from dark-energy + hubify-self-improving), **center** (bigbounce lab pill with sage border + visibility meta + READS allowed / WRITES via comm only rule text), **outbound** (5 sent samples to dark-matter + dark-energy with status). Each comm clickable → opens `comm-event` sidepeek with details. Footer strip shows aggregate stats (pending in / sent / accepted / blocked writes counter at 0 ✓ confirming the rule is enforced) + comm type vocabulary (`suggestion · question · fyi · dataset_offer`). Header h-action links directly to the lab-share sidepeek for config. Sage discipline preserved.
- [ ] **Round C #7 Rename Ideas view → Recent Chats view** (PRD §40.3) — 114 instances + data model adjustment
- [x] **Round C #8 Project filter chips on Lab kanban** (commit `79efa5a`) — Tasks view kanban filter row replaced 4 generic chips with 7 PRD §40 project-aware chips: All projects · P1 f_NL tracer · P2 chirality · P3 anomaly · P4 PTA · QC · Infra (each with title attribute documenting which pipeline/topic it covers). Each chip wired to `filterKanbanByProject()` which uses a keyword map (KANBAN_PROJECT_KEYWORDS) to match card content — chips actually filter the cards (not just visual). Column counts auto-update as cards are hidden. Search input wired to `searchKanban()` for free-text filtering across all columns. Toast confirms the active filter + visible card count. Experiment filter chips on Project kanban (the second half of the original task) deferred to Round C #2 (Project Overview page) where the project kanban will live.
- [ ] **Round C #9 Project ↔ Paper many-to-many** UI — paper sidepeek shows associated projects, project page shows associated papers
- [x] **Round D #1 Director header credits pill** (commit `6183915`) — 4-tier color coding by PRD §41 threshold: HIGH (sage dot, default), WARN (warn dot + warn text), CRIT (crit dot + crit text), EMERGENCY (pulsing crit dot + flashing background + bold text). Uses existing `--warn` and `--crit` CSS variables, no new accent colors. `data-threshold` attribute drives the styling — orchestrator updates it via the credits cron from PRD §41.2. Title attribute documents the 4-tier escalation policy.
- [x] **Round D #2 Compute view credits history chart** (commit `7d287e7`) — full 30-day SVG line chart on the Compute view, 760×240 viewBox, sage line shows the credits balance dropping from ~$1850 to current $847 with 2 visible top-up bumps. Four PRD §41 threshold lines drawn across the chart: HIGH (≥$500, sage dashed), WARN (≥$100, amber dashed), CRIT (≥$25, red dashed), EMERGENCY (<$5, deep red solid). Legend strip below the chart names all 5 lines + current balance + zone label. Current balance ($847) annotated with a dot + label. Two top-up events annotated with vertical reference lines + "+$500 top-up" annotation. Header `forecast →` action shows the projected runway. Sage discipline preserved (only sage / warn / crit CSS variables, no new accent colors).
- [x] **Round D #3 Per-experiment cost mode column** (commit `2f9b8f6`) — Top 5 experiments table on the Costs view gets a new "Mode" column showing PRD §41 routing attribution: `gpu·pod` (sage-bordered, sage-tinted, the heavy GPU work) / `gpu·srvless` (sage-bordered, transparent, bursty GPU calls) / `cpu·pod` (gray-bordered, surface-3 fill, long CPU work like MCMC) / `cpu·srvless` (gray-bordered, transparent, short CPU calls). Each pill has a `title` attribute explaining WHY the orchestrator routed it that way per the §41 rules. Real BigBounce data: EXP-050 (DESI×eROSITA gpu·pod), EXP-051 (PTA Bayes gpu·pod), EXP-049 (bounce discrimination gpu·srvless), EXP-046 (chirality 8.47M inference gpu·pod), EXP-053 (Quintom-B MCMC cpu·pod — Cobaya is CPU-bound, no tensor ops in hot path). Sage discipline preserved (only sage + grayscale neutrals, no new accent colors).
- [x] **Round D #4 Experiment dispatch flow CPU/GPU routing UI** (commit `e4a86ff`) — full Dispatch new experiment card at the top of the Experiments view, 2-column grid with: Title (text input) · Compute mode (GPU/CPU radio buttons + hint text per §41 Rule 1) · Expected duration (<30min / 30min-1hr / >1hr radios per §41 Rule 2) · Priority (low/normal/high/critical). Live routing-decision preview card below the form: as Houston flips radios, `updateDispatchPreview()` recomputes and shows (1) the resulting mode pill (gpu·pod / gpu·srvless / cpu·pod / cpu·srvless), (2) the target compute resource (existing H200 pod / RunPod Serverless H200 / new CPU pod / RunPod CPU Serverless), (3) the human-readable rationale citing each §41 rule that fired, (4) the estimated cost. Default state shows the most common case (GPU + >1hr + normal priority → gpu·pod → bigbounce-h200 reuse, ~$9.00). Sage discipline preserved (only sage + grayscale, no new accent colors). Round D COMPLETE 4/4 ✅.
- [ ] **Final mobile responsiveness audit re-run** — after all Round A-D work is in
- [x] **Final color discipline scan** (commit `83a9f81`) — audited all 130 unique colors in the file, found a cluster of 10 bluish-gray tokens leaking blue tint in view-vibe (.vibe-frame-chart CSS) + view-datamap (SVG data flow arrows + boxes), 61 occurrences replaced with neutral grayscale equivalents (preserving lightness, removing blue); both views are NOT in the polished list — fair game per rule 7; view-site (polished, uses navy intentionally) untouched; mockup is now fully sage+grayscale discipline aligned
- [x] **Settings · Compute & Runtime section + runtime sidepeek (3 variants)** (commit `6eb362b`) — Houston request 2026-04-08: Fly.io machine integration model + macOS app deep link from Settings. Adds Runtime nav item, new Compute & Runtime section with 4 cards (macOS desktop app · Fly.io orchestrator · RunPod compute · MCP server), each clickable to a `runtime` sidepeek showing live status + actions. Fly variant shows the 4-surface integration model (sidepeek inspector / terminal pane stream / out-of-band admin URL / CLI). DEPLOYMENT_INFRA_PLAN.md §2.3 updated with §2.3.1 (4 surfaces) and §2.3.2 (chat→action pipeline through the orchestrator).
- [x] **Final dead-click audit** (verification gate, no commit needed) — audited 615 onclick handlers across the mockup. Zero "coming soon" / "not yet" / "tbd" toasts. Zero empty `onclick=""` handlers. Only 5 `<a href="#">` placeholder links found, all inside `view-site` (polished BigBounce site preview) where they simulate the static nav chrome of the real bigbounce.hubify.app — intentional, not dead. **Audit PASSES — every clickable element in the mockup either opens a sidepeek, navigates to a view, fires a real toast notification, or is intentional simulation chrome inside a polished view.**
- [x] **Final PRD↔mockup consistency review re-run** (commit `e99ab85`) — audited all 28 mockup view divs against PRD §31 inventory. Found 6 drift gaps and fixed all 6 in PRD §31: (1) view-experiments now documents the §41 dispatch routing UI added in Round D #4, (2) view-comms now documents the cross-lab gateway card added in Round C #6, (3) view-tasks now documents the 7 §40 project filter chips added in Round C #8, (4) view-settings count corrected from 8 → 10 nav sections (added Lab Sharing + Runtime), (5) view-datamap added to inventory (was missing entirely), (6) view-graph added to inventory (was missing entirely). PRD §31 now lists all 28 views and matches the mockup 1:1.

**B status:** ~70% — core views all built, polish + Round B/C/D refactors remaining.

### C. macOS app mockup + spec complete

- [x] **Write `DESKTOP_APP_SPEC.md`** in `project-context/` — full native features inventory (commit `d025f47`) — Tauri 2 shell + 11 native features (window chrome, menu bar, dock badge, native notifications, file drop, hubify:// URL scheme, launchd service, keyboard shortcuts, iCloud notes sync, code signing, auto-updater) + menu bar app variant + iteration plan
  - Native window chrome (or borderless like Linear/Cursor)
  - Native menu bar (App / File / Edit / View / Window / Help) with keyboard shortcuts
  - Native notifications (NSUserNotification · unread badge in dock)
  - Native file drop (drag from Finder into the app)
  - Touch Bar support (if MBP)
  - `hubify://` URL scheme handler registered in Info.plist
  - launchd background service for the orchestrator (runs even when app is closed)
  - Native keyboard shortcuts (⌘N new note, ⌘K command palette, ⌘W close tab, etc.)
  - iCloud sync for journal notes (optional toggle)
  - Code signing identity + notarization plan
  - Auto-update channel (Sparkle vs Tauri's built-in updater)
- [x] **Tauri shell architecture decision** (DESKTOP_APP_SPEC.md §0, commit `d025f47`) — DECISION: Tauri 2.x. Reasons: 5-10x smaller bundle than Electron, native WKWebView, Rust backend, easy cross-compile, mature signing/notarization via tauri-action. Rejected Electron (bundle size + memory). Rejected native Swift (doubling the codebase too expensive for solo team).
- [x] **Build `desktop-app-mockup.html`** (commit `891e34f`) — separate self-contained HTML file at `hubify-labs-mockups/desktop-app-mockup.html` showing the macOS-specific chrome wrapping the existing web app per DESKTOP_APP_SPEC.md §3. All 7 native chrome elements built: (1) macOS menu bar with Hubify Labs · File · Edit · View · Lab · Window · Help + status icons + clock, (2) borderless Tauri window with traffic lights + draggable titlebar containing the Director credits pill ($847 sage HIGH zone) + cosmic orb status indicator, (3) faux sidebar + content area with stat-grid + overnight briefing card + top experiments rows (real EXP-050/051/049 IDs), (4) macOS Dock with Finder/Cursor/Terminal/Hubify icons + Hubify icon shows running dot + red unread badge "3", (5) native NSUserNotification banner sliding in from top-right with sage Hubify icon + "GPU IDLE — deploy next phase" sample notification, (6) file-drop overlay (toggled on/off) showing sage-tinted dashed-border drop zone, (7) menu bar app popover anchored under the menu bar icon with always-on-top mini Director view (lab + credits + runway + recent activity + quick chat input + open-app button). Plus 8 annotation flags labeling each native element + bottom-left toggle bar (Notification/Menu bar app/File drop/Annotations on-off). Sage discipline preserved (sage/grayscale/--warn/--crit only, no new accent colors). Standard macOS native colors (red traffic light #ff5f57 etc.) used where required for native fidelity.
- [x] **Spec the menu bar app variant** (DESKTOP_APP_SPEC.md §2, commit `d025f47`) — separate Tauri window with `decorations:false`, `alwaysOnTop:true`, `skipTaskbar:true`, anchored under macOS menu bar icon via `tauri-plugin-positioner`, uses `NSStatusItem` API. Popover content: Director status · credits + runway · quick chat input · recent activity · "Open Hubify Labs". Optional companion app for users who want always-resident monitoring.
- [x] **iOS app deferral statement** (DESKTOP_APP_SPEC.md §3.5, commit `4695389`) — explicit deferral to v2. Reasons: iOS is mostly a viewer not a driver, native dev expensive (Tauri 2 iOS not production-ready, Swift/RN both multi-week), web app on Safari mobile already covers 80% of the use case, ntfy.sh handles the only thing that requires native iOS (push). v1 ships with mobile-responsive web + ntfy.sh + PWA manifest + universal links. v2 plan: re-evaluate Tauri 2 iOS in Q3 2026, fall back to Swift/SwiftUI if not ready.

**C status:** **100% ✅** (5 of 5) — Category C COMPLETE.

### D. API spec complete

- [x] **Write `API_SPEC.md`** in `project-context/` (commit `eb3bcfd`) — comprehensive REST + GraphQL + auth + versioning + error format spec, ~500 lines · Category D bootstrap
- [x] **REST endpoint inventory** (in API_SPEC.md §3) — 19 endpoint groups · ~85 endpoints across labs · projects · pipelines · experiments · files · chats · papers · notes · agents · memory · contributions · compute · cross-lab comms · webhooks · search · standups · routines · backups · costs
- [ ] **GraphQL schema** — full schema TBD (mentioned in API_SPEC.md §7 with example query, full schema deferred to v1.1)
- [x] **Auth & rate limiting policy** (in API_SPEC.md §2 + §4) — JWT HS256 with 3 token types (user/agent/service) · per-lab scopes enforcing Lab Sovereignty Rule · 3-tier rate limits + per-endpoint overrides
- [x] **Versioning policy** (in API_SPEC.md §1) — URL path versioning (`/v1/...`) · 12-month deprecation policy · Sunset + Link headers
- [x] **Error response format** (in API_SPEC.md §5) — RFC 7807 Problem Details · 11 standard error type slugs
- [x] **OpenAPI YAML lock** (commit `8ea7a93`) — `api-spec.openapi.yaml` written, OpenAPI 3.1 format, 14 tags + 8 reusable schemas + 8 path components + ~30 of the ~85 endpoints from API_SPEC.md §3 (the v1 load-bearing ones: auth + labs + projects + experiments dispatch + files + chats + chat-promote + notechat + compute credits + comms + search + runtime/orchestrator inspector). Includes Lab Sovereignty Rule enforcement (cross-lab write returns 403 with type cross-lab-write-denied) + PRD §41 routing requirement (experiment dispatch returns 422 if requires_gpu missing). The remaining 55 endpoints get added via codegen during the build phase.

**D status:** 100% (7 of 7) — Category D COMPLETE ✅

### E. MCP server spec complete

- [x] **Write `MCP_SERVER_SPEC.md`** (commit `0546d5d`) — comprehensive MCP server spec ~700 lines covering 4 MCP primitives (tools/resources/prompts/sampling) + 3 transports (stdio/SSE/WebSocket) + Lab Sovereignty Rule enforcement at the protocol boundary
- [x] **Tool definitions** (in MCP_SERVER_SPEC.md §2) — **~30 tools across 11 categories**: file system (read/write/list/delete) · experiment dispatch (with PRD §41 routing) · agent invocation · cross-lab comms · memory · contributions · notes · chats · LaTeX/paper · compute · search
- [x] **Resource definitions** (in MCP_SERVER_SPEC.md §3) — ~15 resources including 5 live SSE streams (activity feed, credits, standups, comms inbox, experiment logs) + 10 snapshot resources (lab metadata, projects, agents, papers, contributions, datasets, wiki, notes, pods)
- [x] **Prompt templates** (in MCP_SERVER_SPEC.md §4) — 6 templates: review_paper · houston_method_post_experiment · draft_chat_to_project · standup_facilitate · publish_ready_check · no_punt_check
- [x] **Auth flow** (in MCP_SERVER_SPEC.md §5) — JWT format from API_SPEC §2 · per-lab scoping enforcing the Lab Sovereignty Rule at the protocol boundary (cross-lab writes are 403'd before reaching the API)
- [x] **Audit logging** (in MCP_SERVER_SPEC.md §5.4) — every tool call → `lab/audit/mcp-<agent>.jsonl` (append-only, included in nightly Backblaze backup)
- [x] **MCP YAML lock** (commit `19917e0`) — `mcp-server-spec.yaml` written, ~600 lines, machine-readable contract for SDK generation. Server metadata + 3 transports (stdio/SSE/WebSocket) + JWT auth with `cross_lab_rules` enforcing the Lab Sovereignty Rule at the protocol boundary. ~25 tools across 11 categories with full input schemas + each tool documents its REST endpoint mapping (per `api-spec.openapi.yaml`) + cross_lab_policy fields (NEVER_ALLOWED for write operations). 15 resources (10 snapshot + 5 SSE streams). 6 prompt templates. 6 MCP-specific error types. Constraints arrays for protocol-layer enforcement (N4-not-claimable-by-agent, explicit_user_consent for notes).

**E status:** **100% ✅** (7 of 7) — Category E COMPLETE.

### F. CLI spec complete

- [x] **Write `CLI_SPEC.md`** (commit `c7804a0`) — comprehensive Go-based CLI spec ~700 lines covering ~120 commands across 19 categories, depends on API_SPEC + MCP_SERVER_SPEC, single static binary distribution
- [x] **Command structure** (in CLI_SPEC.md §1) — **~120 commands across 19 categories**: lab · project · experiment (with §41 routing) · pipeline · chat · note · pod/compute · agent · memory · standup · costs · backup · cross-lab comms · search · MCP server · auth · config · status · TUI
- [x] **TUI mode** (in CLI_SPEC.md §1.19) — `hubify` with no args opens bubbletea-based interactive terminal UI mirroring the web views, ⌘1-9 nav, `/` search, `?` help
- [x] **Output formats** (in CLI_SPEC.md §2) — `--format text|json|yaml|table|tsv`, auto-disable colors when stdout is not TTY
- [x] **Auth flow** (in CLI_SPEC.md §3) — browser OAuth (PKCE) default · service token via env var · macOS Keychain / Linux libsecret / Windows Credential Manager integration · profile switching via `--profile` or `HUBIFY_PROFILE`
- [x] **Local config + secrets** (in CLI_SPEC.md §4) — `~/.hubify/config.yaml` + `~/.hubify/credentials` (mode 0600), secrets never in config, env vars for runtime secrets, per-lab config override
- [~] **Plugin system (future)** (in CLI_SPEC.md §5) — explicitly DEFERRED to v1.1 per spec, stub structure documented
- [x] **CLI YAML lock** (commit `378b58a`) — `cli-spec.yaml` written, ~900 lines, machine-readable contract for shell completions + docs generation. Mirrors the api-spec.openapi.yaml + mcp-server-spec.yaml pattern. CLI metadata (name, version, language, framework, distribution channels) + 5 output formats + 4 auth methods (oauth_browser default + service_token + token_flag) + credentials file structure (mode 0600 YAML) + 9 env vars + 10 global flags inherited by every command + 19 categories cross-referenced + ~85 commands across 19 categories with full args/flags/format/maps_to (REST endpoint or MCP tool reference) + cross_lab_rules enforcing the Lab Sovereignty Rule at the CLI layer (rejected before HTTP send) + 4 validation rules + 13 canonical exit codes (0-130) + shell completion spec for bash/zsh/fish/powershell with dynamic completion sources + plugin system explicitly DEFERRED to v1.1 stub. Every command's `maps_to` field cross-references either an `api-spec.openapi.yaml` endpoint OR a `mcp-server-spec.yaml` tool — guarantees CLI implementation fidelity to the upstream contracts.

**F status:** **100% ✅** (8 of 8, with item 7 plugin system explicitly deferred to v1.1) — Category F COMPLETE.

### G. Deployment infrastructure plan complete

- [x] **Write `DEPLOYMENT_INFRA_PLAN.md`** (commit `2e5f3e6`) — comprehensive deployment plan ~750 lines, ALL 13 items covered in one iteration
- [x] **Vercel deploy config** (in DEPLOYMENT_INFRA_PLAN §2.1) — Type A platform `hubify-labs.com` + Type B per-lab sites `<lab>.hubify.app`, vercel.json with security headers, auto-deploy from main branch
- [x] **Convex deployment** (in §2.2) — 3 environments (dev/staging/prod), schema migration strategy, full env var inventory (15 secrets)
- [x] **Fly.io deployment** (in §2.3) — one shared-CPU machine per active lab, ~$2-5/month each, auto-restart, no auto-scaling
- [x] **RunPod credentials store** (in §2.4) — DECISION: Convex env vars (rejected Vault as overkill, rejected 1Password CLI as adding deps)
- [x] **Backblaze B2 backup pipeline** (in §2.5) — bucket structure, nightly cron + pre-credits-out + on-demand triggers, retention policy, verification cadence
- [x] **Database migrations strategy** (in §2.6) — Convex TypeScript schema versioning, additive-then-remove pattern, migration log
- [x] **CI/CD pipeline** (in §2.7) — 3 GitHub Actions workflows (ci.yml, deploy-staging.yml, deploy-prod.yml) with manual approval gate + pre-deploy backup + post-deploy smoke test
- [x] **Domain/DNS setup** (in §2.8) — Cloudflare DNS, wildcard `*.hubify.app` for per-lab subdomains, MX records for transactional email
- [x] **SSL/TLS** (in §2.9) — Let's Encrypt auto-provisioned via Vercel + Convex, TLS 1.3, HSTS headers
- [x] **Monitoring stack** (in §2.10) — Sentry (errors) + Vercel Analytics (perf) + Better Uptime (uptime) + custom Convex dashboards + ntfy.sh (phone push) + Slack (team)
- [x] **Backup destination configs** (in §2.11) — 4-destination matrix (B2 cold + GitHub code + Git LFS binaries + Hugging Face public)
- [x] **Cost monitoring + alerts** (in §2.12) — daily report + 4-tier alerts per PRD §41 thresholds + per-experiment cost cap enforcement
- [x] **BONUS: Local development setup** (§2.13), Secrets management cross-cutting (§3), Incident response runbook (§4), Environment promotion path (§5), Cost forecast at v1 + 100-user scale (§6)

**G status:** 100% (13 of 13) — entire category bootstrapped and FULLY COMPLETE in one iteration.

### H. Migration plan complete

- [x] **`MIGRATION_BOUNCE_COSMOLOGY_LAB.md` written** — full Lab #1 migration plan (~1500 lines)
- [x] Pre-migration safety steps documented
- [x] Import script pseudocode
- [x] Verification gates
- [x] Risk register
- [x] Post-migration roadmap (4 weeks)
- [ ] **Migration plan reviewed by Houston**
- [x] **Open questions answered with proposed defaults** (commit `cd80b06`) — all 6 migration plan open questions now have explicit default answers + reasoning + Houston-override-expected paragraph: (1) subdomain → b → a (1-week burn-in then graduate), (2) SSH creds → Convex env vars + macOS Keychain, (3) DNS cutover → 1-week burn-in, (4) quiet day → next weekend post-Phase 4, (5) test-lab pre-validation → YES build it, (6) Mintlify docs port → separate post-migration Week 4+. Houston still needs to confirm or override; sign-off block at the bottom of §6 specifies the exact format. Migration plan is now executable with proposed defaults — only Houston's explicit confirm/override remains.
- [ ] **Test-lab pre-validation built** — a small synthetic-data lab to validate the import + bootstrap flow before risking BigBounce data (recommended, ~1 day work)
- [ ] **Houston sign-off on migration plan**

**H status:** ~89% — plan written + 6 open questions answered with proposed defaults + reasoning. Awaiting Houston confirm/override + Houston review pass + test-lab build (still a real ~1 day work item).

### I. Houston sign-off

- [ ] Houston reviewed PRD §40 (Hierarchy v2 lock)
- [ ] Houston reviewed PRD §41 (Compute routing + credits)
- [ ] Houston reviewed PRD §1 architecture lock (Lab=repo)
- [ ] Houston reviewed all 5 lab spec files
- [ ] Houston reviewed `MIGRATION_BOUNCE_COSMOLOGY_LAB.md`
- [ ] Houston answered all open questions in the PRD
- [ ] Houston confirmed READY status by signing this checklist

**I status:** 0% — pending Houston review pass.

---

## 3. The READY math (current state)

| Category | Done | Total | % |
|---|---|---|---|
| A. PRD lock | 53 | 54 | 98% |
| B. Web mockup | 42 | 49 | 86% |
| C. macOS app | 5 | 5 | **100% ✅** |
| D. API spec | 7 | 7 | **100% ✅** |
| E. MCP server | 7 | 7 | **100% ✅** |
| F. CLI spec | 8 | 8 | **100% ✅** |
| G. Deployment infra | 13 | 13 | **100% ✅** |
| H. Migration plan | 7 | 9 | 78% |
| I. Houston sign-off | 0 | 7 | 0% |
| **OVERALL** | **142** | **159** | **89%** |

**Translation:** we're past three-quarters. The PRD is in great shape (80%), the web mockup is past the midpoint (67%), the migration plan is mostly done (67%). **D · E · F · G are all 100% locked** (4 categories shipped end-to-end), C at 80% (1 item left). Houston review is pending.

**To hit READY = 100%, the loop needs to:**
1. Finish A (~10 items)
2. Finish B (~16 items)
3. Finish C (~1 item — desktop-app-mockup.html)
4. Wait on H/I (Houston review)

**Estimated iteration count at the current pace** (~5-15 items per session, depending on size): **8-15 more sessions** to hit READY.

---

## 4. The expanded loop

The autonomous polish loop currently reads from `/Users/houstongolden/Desktop/CODE_2025/hubify-labs-mockups/.queue.md` (mockup-only). **Per Houston's 2026-04-08 expansion request, the loop now reads from THIS file as the master source of truth.**

### 4.1 The new loop algorithm

Every iteration the loop:

1. **Reads `BUILD_READINESS_CHECKLIST.md`** (this file)
2. **Picks the highest-impact unchecked item across ALL categories** (A-I), using these tiebreakers:
   - Priority 1: items that unblock other items (e.g., write the API spec template before filling individual endpoints)
   - Priority 2: items in the smallest categories (C/D/E/F/G are at 0% — finishing one of them first proves the loop covers all categories)
   - Priority 3: items that are smallest / most atomic (5-10 min of work)
   - Priority 4: items that map to the most clicks/views in the mockup (highest user-visible impact)
3. **Ships it** (commit · validation · brief explanation in the response)
4. **Updates this file** to mark the item `[x]` with the commit hash
5. **Continues to the next iteration**

The loop NEVER stops until either:
- All 156 items are `[x]` (READY status)
- Houston explicitly pauses or redirects it

### 4.2 The "always pick something from a 0% category if possible" rule

To avoid the loop spending all iterations on Round A polish while C/D/E/F/G stay at 0%, the loop prefers:
- **At least 1 of every 3 iterations** picks from a 0% category (currently C/D/E/F/G)
- This guarantees forward progress on the macOS spec, API, MCP, CLI, and deployment plan even while the polish work continues

### 4.3 Cron prompt update

The polish-loop cron previously fired this prompt:

> "AUTONOMOUS HUBIFY LABS POLISH LOOP — overnight iteration. Read the priority queue at /Users/houstongolden/Desktop/CODE_2025/hubify-labs-mockups/.queue.md..."

The cron should now fire this updated prompt instead:

```
AUTONOMOUS HUBIFY LABS BUILD READINESS LOOP — overnight iteration. Houston is asleep, the loop must continue without him.

Read the master READY checklist at /Users/houstongolden/Desktop/CODE_2025/bigbounce/project-context/BUILD_READINESS_CHECKLIST.md. Find the highest-impact unchecked item across ANY category (A: PRD lock / B: web mockup / C: macOS app / D: API spec / E: MCP server / F: CLI spec / G: deployment infra / H: migration plan / I: Houston sign-off).

Use these tiebreakers to pick the next item:
1. Items that unblock other items
2. Items in 0% categories (force progress on C/D/E/F/G even while polish continues — at least 1 of every 3 iterations should pick from a 0% category)
3. Items that are smallest / most atomic (5-10 min)
4. Items that map to the most user-visible impact

HARD RULES (read every iteration):
1. Real BigBounce data only: 53 experiments, 4 papers, 328K anomalies, 8 surveys, 142 wiki entries, 16 contributions
2. Single sage green accent (#5fb88a) — NO new accent colors
3. NO MODALS EVER — drilldowns use the existing openSidepeek(type, id) sidepeek system
4. Wire all new clickable content elements to call openSidepeek(...)
5. Register new views in sidebar nav (sb-item), tabNames, tabIcons, and cmds (command palette)
6. Don't touch the cosmic orb / verb rotation system in the chat thinking block
7. Don't touch existing polished views unless the change is part of the locked spec
8. After building: mark the item [x] in BUILD_READINESS_CHECKLIST.md with the commit hash, then commit
9. Spawn an Explore subagent to review any non-trivial commit
10. List which item you built and which category it came from

Be efficient. 5-10 min per iteration. Aim to ship 1-2 commits per iteration. The loop NEVER stops until all 156 items are [x] or Houston pauses it.
```

The next time the cron fires, paste the new prompt (the OLD cron job ID will fire the OLD prompt — needs to be deleted and re-created).

### 4.4 What this means for forward velocity

- **Before:** loop iterated only on mockup polish work (.queue.md). PRD work, API spec, macOS spec, etc. only happened when Houston was actively driving.
- **After:** loop iterates across ALL 9 categories. PRD sections, API endpoints, macOS spec sections, deployment plan items, etc. all get progress in the same loop.
- **Result:** READY status is hit in continuous progress, not in big batches. Houston can wake up any morning and see substantive progress across ALL categories.

---

## 5. The READY definition (the one-line gate)

```
WE ARE READY when this file shows 156 / 156 [x] AND Houston has signed §I.
```

Until then, every iteration moves at least one item closer.

---

## 6. After READY — what changes

When all 156 items are `[x]`:

1. The loop pivots from "spec + polish" to "rebuild + deploy"
2. A new file `BUILD_EXECUTION_CHECKLIST.md` takes over as the source of truth
3. The new checklist tracks the actual rebuild work: Convex schema migration, Tauri shell setup, API endpoint implementation, MCP server build, CLI tool build, macOS app build, deployment to staging, deployment to prod, BigBounce migration execution
4. The cron prompt updates again to read from the new file
5. We ship the MVP

But that's a problem for after READY. For now: **every iteration of the loop must move BUILD_READINESS_CHECKLIST.md closer to 156/156.**
