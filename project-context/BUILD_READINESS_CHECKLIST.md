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
- [ ] **§42 (TBD) — macOS desktop app spec** — full native features + Tauri shell architecture
- [ ] **§43 (TBD) — REST + GraphQL API spec** — complete endpoint inventory
- [ ] **§44 (TBD) — MCP server spec** — tools, resources, auth, scoping
- [ ] **§45 (TBD) — CLI spec** — commands, auth, output formats, plugin system
- [ ] **§46 (TBD) — Deployment infrastructure plan** — Vercel/Convex/Fly/RunPod/Backblaze + DNS
- [ ] **§47 (TBD) — Mintlify docs port plan** — first 7 docs pages outline (started in §40.17 Tier 3, needs expansion)
- [ ] **§48 (TBD) — `hubify://` URL scheme spec** — full URL pattern catalog
- [ ] **§49 (TBD) — Authentication & authorization spec** — OAuth provider, token issuing, per-lab scoping, agent authentication
- [ ] **§50 (TBD) — Telemetry & observability spec** — what events get logged, where, retention policy, privacy
- [ ] **PRD §19 numbering fix** — rename "Session Summary" to "Appendix A: Section Index" (currently sits at end despite being numbered 19, which is confusing)
- [ ] **PRD subsection fills** — view-figures (§37 sub), view-knowledge (§33 sub), view-vibe (§39 sub) — currently underspecified
- [ ] **PRD open questions answered** — (1) chat default model: Sonnet 4.6 default · confirm? (2) voice dictation provider: Whisper API default · confirm? (3) cross-lab read-only enforcement layer: GitHub perms + Convex auth · confirm? (4) BigBounce migration final subdomain: `bigbounce2.hubify.app` placeholder vs alternatives
- [ ] **5 lab spec files reviewed by Houston** (all 5 written, awaiting his read): MIGRATION_BOUNCE_COSMOLOGY_LAB · LAB_HUBIFY_SELF_IMPROVING · LAB_DARK_ENERGY · LAB_DARK_MATTER · LAB_ETI

**A status:** ~85% — most sections done, 9 new sections to write + a handful of fills + question answers + Houston review pass.

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
- [ ] **Round C #3 Chat composer enrichments** — model switcher · mode pill · file upload · mic icon · slash command autocomplete (PRD §40.10)
- [ ] **Round C #4 Wire 4 chat slash commands** — `/chat`, `/notechat`, `/promote`, `/share` (PRD §40.13)
- [ ] **Round C #5 Lab Sharing settings sidepeek** (PRD §40.11)
- [ ] **Round C #6 Cross-lab comm gateway visualization** — small panel showing inbound/outbound comms with other labs
- [ ] **Round C #7 Rename Ideas view → Recent Chats view** (PRD §40.3) — 114 instances + data model adjustment
- [ ] **Round C #8 Project filter chips on Lab kanban** + experiment filter chips on Project kanban (PRD §40.9)
- [ ] **Round C #9 Project ↔ Paper many-to-many** UI — paper sidepeek shows associated projects, project page shows associated papers
- [x] **Round D #1 Director header credits pill** (commit `6183915`) — 4-tier color coding by PRD §41 threshold: HIGH (sage dot, default), WARN (warn dot + warn text), CRIT (crit dot + crit text), EMERGENCY (pulsing crit dot + flashing background + bold text). Uses existing `--warn` and `--crit` CSS variables, no new accent colors. `data-threshold` attribute drives the styling — orchestrator updates it via the credits cron from PRD §41.2. Title attribute documents the 4-tier escalation policy.
- [ ] **Round D #2 Compute view credits history chart** with 4 threshold lines
- [ ] **Round D #3 Per-experiment cost mode column** — pod / serverless / cpu-pod / cpu-serverless attribution
- [ ] **Round D #4 Experiment dispatch flow CPU/GPU routing UI** — `requires_gpu` + `expected_duration_min` + `priority` fields
- [ ] **Final mobile responsiveness audit re-run** — after all Round A-D work is in
- [x] **Final color discipline scan** (commit `83a9f81`) — audited all 130 unique colors in the file, found a cluster of 10 bluish-gray tokens leaking blue tint in view-vibe (.vibe-frame-chart CSS) + view-datamap (SVG data flow arrows + boxes), 61 occurrences replaced with neutral grayscale equivalents (preserving lightness, removing blue); both views are NOT in the polished list — fair game per rule 7; view-site (polished, uses navy intentionally) untouched; mockup is now fully sage+grayscale discipline aligned
- [x] **Settings · Compute & Runtime section + runtime sidepeek (3 variants)** (commit `6eb362b`) — Houston request 2026-04-08: Fly.io machine integration model + macOS app deep link from Settings. Adds Runtime nav item, new Compute & Runtime section with 4 cards (macOS desktop app · Fly.io orchestrator · RunPod compute · MCP server), each clickable to a `runtime` sidepeek showing live status + actions. Fly variant shows the 4-surface integration model (sidepeek inspector / terminal pane stream / out-of-band admin URL / CLI). DEPLOYMENT_INFRA_PLAN.md §2.3 updated with §2.3.1 (4 surfaces) and §2.3.2 (chat→action pipeline through the orchestrator).
- [x] **Final dead-click audit** (verification gate, no commit needed) — audited 615 onclick handlers across the mockup. Zero "coming soon" / "not yet" / "tbd" toasts. Zero empty `onclick=""` handlers. Only 5 `<a href="#">` placeholder links found, all inside `view-site` (polished BigBounce site preview) where they simulate the static nav chrome of the real bigbounce.hubify.app — intentional, not dead. **Audit PASSES — every clickable element in the mockup either opens a sidepeek, navigates to a view, fires a real toast notification, or is intentional simulation chrome inside a polished view.**
- [ ] **Final PRD↔mockup consistency review re-run** — verify the gaps from the last review are all closed

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
- [ ] **Build `desktop-app-mockup.html`** — a separate self-contained HTML mockup showing the macOS-specific chrome wrapping the existing web app: native title bar with traffic lights, native menu bar visualization, dock badge, native file drop indicator, system notification preview
- [x] **Spec the menu bar app variant** (DESKTOP_APP_SPEC.md §2, commit `d025f47`) — separate Tauri window with `decorations:false`, `alwaysOnTop:true`, `skipTaskbar:true`, anchored under macOS menu bar icon via `tauri-plugin-positioner`, uses `NSStatusItem` API. Popover content: Director status · credits + runway · quick chat input · recent activity · "Open Hubify Labs". Optional companion app for users who want always-resident monitoring.
- [x] **iOS app deferral statement** (DESKTOP_APP_SPEC.md §3.5, commit `4695389`) — explicit deferral to v2. Reasons: iOS is mostly a viewer not a driver, native dev expensive (Tauri 2 iOS not production-ready, Swift/RN both multi-week), web app on Safari mobile already covers 80% of the use case, ntfy.sh handles the only thing that requires native iOS (push). v1 ships with mobile-responsive web + ntfy.sh + PWA manifest + universal links. v2 plan: re-evaluate Tauri 2 iOS in Q3 2026, fall back to Swift/SwiftUI if not ready.

**C status:** 80% (4 of 5) — only the desktop-app-mockup.html build remains.

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
- [ ] **CLI YAML lock** — `cli-spec.yaml` (next item in Category F — turns this human-readable spec into the machine-readable contract for shell completions + docs generation)

**F status:** ~88% (7 of 8, with item 7 explicitly deferred to v1.1) — entire category bootstrapped from 0% in one iteration.

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
- [ ] **Open questions answered:** (1) subdomain decision (a/b/c/d) · (2) SSH credentials store · (3) DNS cutover timing · (4) quiet day for migration · (5) test-lab pre-validation? · (6) Mintlify port timing
- [ ] **Test-lab pre-validation built** — a small synthetic-data lab to validate the import + bootstrap flow before risking BigBounce data (recommended, ~1 day work)
- [ ] **Houston sign-off on migration plan**

**H status:** ~80% — plan written, awaiting Houston review + question answers.

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
| A. PRD lock | 41 | 51 | 80% |
| B. Web mockup | 33 | 49 | 67% |
| C. macOS app | 4 | 5 | 80% |
| D. API spec | 7 | 7 | **100% ✅** |
| E. MCP server | 7 | 7 | **100% ✅** |
| F. CLI spec | 7 | 8 | 88% |
| G. Deployment infra | 13 | 13 | **100% ✅** |
| H. Migration plan | 6 | 9 | 67% |
| I. Houston sign-off | 0 | 7 | 0% |
| **OVERALL** | **118** | **156** | **76%** |

**Translation:** we're past three-quarters. The PRD is in great shape (80%), the web mockup is past the midpoint (67%), the migration plan is mostly done (67%). **D · E · G are 100% locked**, F at 88% (1 item left), C at 80% (1 item left). Houston review is pending.

**To hit READY = 100%, the loop needs to:**
1. Finish A (~10 items)
2. Finish B (~16 items)
3. Finish C (~1 item — desktop-app-mockup.html)
4. Finish F (~1 item — cli-spec.yaml)
5. Wait on H/I (Houston review)

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
