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
- [ ] **Round A item #5 toast positioning + density** — consistent corner stacking
- [ ] **Round A item #6 card padding audit** — pick one scale (12px vs 16px vs 20px vs 24px)
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
- [ ] **Round D #1 Director header credits pill** — `$29.35 · 47h runway` color-coded (per PRD §41)
- [ ] **Round D #2 Compute view credits history chart** with 4 threshold lines
- [ ] **Round D #3 Per-experiment cost mode column** — pod / serverless / cpu-pod / cpu-serverless attribution
- [ ] **Round D #4 Experiment dispatch flow CPU/GPU routing UI** — `requires_gpu` + `expected_duration_min` + `priority` fields
- [ ] **Final mobile responsiveness audit re-run** — after all Round A-D work is in
- [ ] **Final color discipline scan** — verify zero leaks anywhere
- [ ] **Final dead-click audit** — every clickable opens a sidepeek or navigates somewhere
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
- [ ] **Tauri shell architecture decision** — Tauri 2.x vs Electron vs native Swift. Tauri 2 default, Swift considered for the menu bar app variant.
- [ ] **Build `desktop-app-mockup.html`** — a separate self-contained HTML mockup showing the macOS-specific chrome wrapping the existing web app: native title bar with traffic lights, native menu bar visualization, dock badge, native file drop indicator, system notification preview
- [ ] **Spec the menu bar app variant** — a small `Hubify Labs` icon in the macOS menu bar that shows: live agent count · current Director status · quick chat input · "click to open full app". For users who want the platform always-resident.
- [ ] **iOS app deferral statement** — write a note in §42 about why iOS is deferred to v2 and what the rough timeline is

**C status:** 0% — entire category untouched.

### D. API spec complete

- [x] **Write `API_SPEC.md`** in `project-context/` (commit `eb3bcfd`) — comprehensive REST + GraphQL + auth + versioning + error format spec, ~500 lines · Category D bootstrap
- [x] **REST endpoint inventory** (in API_SPEC.md §3) — 19 endpoint groups · ~85 endpoints across labs · projects · pipelines · experiments · files · chats · papers · notes · agents · memory · contributions · compute · cross-lab comms · webhooks · search · standups · routines · backups · costs
- [ ] **GraphQL schema** — full schema TBD (mentioned in API_SPEC.md §7 with example query, full schema deferred to v1.1)
- [x] **Auth & rate limiting policy** (in API_SPEC.md §2 + §4) — JWT HS256 with 3 token types (user/agent/service) · per-lab scopes enforcing Lab Sovereignty Rule · 3-tier rate limits + per-endpoint overrides
- [x] **Versioning policy** (in API_SPEC.md §1) — URL path versioning (`/v1/...`) · 12-month deprecation policy · Sunset + Link headers
- [x] **Error response format** (in API_SPEC.md §5) — RFC 7807 Problem Details · 11 standard error type slugs
- [ ] **OpenAPI YAML lock** — `api-spec.openapi.yaml` (next item in Category D — turns this human-readable spec into the machine-readable contract)

**D status:** ~71% (5 of 7) — entire category bootstrapped from 0% in one iteration.

### E. MCP server spec complete

- [x] **Write `MCP_SERVER_SPEC.md`** (commit `0546d5d`) — comprehensive MCP server spec ~700 lines covering 4 MCP primitives (tools/resources/prompts/sampling) + 3 transports (stdio/SSE/WebSocket) + Lab Sovereignty Rule enforcement at the protocol boundary
- [x] **Tool definitions** (in MCP_SERVER_SPEC.md §2) — **~30 tools across 11 categories**: file system (read/write/list/delete) · experiment dispatch (with PRD §41 routing) · agent invocation · cross-lab comms · memory · contributions · notes · chats · LaTeX/paper · compute · search
- [x] **Resource definitions** (in MCP_SERVER_SPEC.md §3) — ~15 resources including 5 live SSE streams (activity feed, credits, standups, comms inbox, experiment logs) + 10 snapshot resources (lab metadata, projects, agents, papers, contributions, datasets, wiki, notes, pods)
- [x] **Prompt templates** (in MCP_SERVER_SPEC.md §4) — 6 templates: review_paper · houston_method_post_experiment · draft_chat_to_project · standup_facilitate · publish_ready_check · no_punt_check
- [x] **Auth flow** (in MCP_SERVER_SPEC.md §5) — JWT format from API_SPEC §2 · per-lab scoping enforcing the Lab Sovereignty Rule at the protocol boundary (cross-lab writes are 403'd before reaching the API)
- [x] **Audit logging** (in MCP_SERVER_SPEC.md §5.4) — every tool call → `lab/audit/mcp-<agent>.jsonl` (append-only, included in nightly Backblaze backup)
- [ ] **MCP YAML lock** — `mcp-server-spec.yaml` (next item in Category E — turns this human-readable spec into the machine-readable contract for SDK generation)

**E status:** ~86% (6 of 7) — entire category bootstrapped from 0% in one iteration.

### F. CLI spec complete

- [ ] **Write `CLI_SPEC.md`**
- [ ] **Command structure** (the `hubify` CLI):
  - `hubify lab create <slug>` · `hubify lab list` · `hubify lab switch <slug>` · `hubify lab share <slug> --with <other-slug>`
  - `hubify project create <slug>` · `hubify project list` · `hubify project show <slug>`
  - `hubify experiment dispatch <spec.yaml>` · `hubify experiment list`
  - `hubify chat new` · `hubify chat resume <id>` · `hubify chat list`
  - `hubify note new [filename]` · `hubify note list` · `hubify note open <filename>`
  - `hubify pod status` · `hubify pod ssh` · `hubify pod kill <id>`
  - `hubify credits` (shows balance + runway)
  - `hubify standup` (trigger or view)
  - `hubify open <hubify://...>` (URL scheme handler)
  - `hubify auth login` · `hubify auth status`
  - `hubify config get/set <key>`
- [ ] **TUI mode** — `hubify` with no args opens an interactive TUI session (mirror of the web UI)
- [ ] **Output formats** — `--format text|json|table|yaml`
- [ ] **Auth flow** — OAuth via browser callback OR long-lived token via env var
- [ ] **Local config + secrets** — `~/.hubify/config.yaml` + `~/.hubify/credentials`
- [ ] **Plugin system (future)** — `hubify plugin install <name>` for community extensions
- [ ] **CLI YAML lock**

**F status:** 0% — entire category untouched.

### G. Deployment infrastructure plan complete

- [ ] **Write `DEPLOYMENT_INFRA_PLAN.md`**
- [ ] **Vercel deploy config** — the web app deployment
- [ ] **Convex deployment** — the backend (per-environment: dev, staging, prod)
- [ ] **Fly.io deployment** — the orchestrator agent host (one machine per active lab)
- [ ] **RunPod credentials store** — Convex env vars vs HashiCorp Vault vs 1Password CLI (default: Convex env vars per PRD §41 open question)
- [ ] **Backblaze B2 backup pipeline** — nightly cron + per-credit-threshold trigger per PRD §41
- [ ] **Database migrations strategy** — Convex schema versioning + migration scripts
- [ ] **CI/CD pipeline** — GitHub Actions: on push to main → run tests → deploy to Vercel + Convex + Fly
- [ ] **Domain/DNS setup** — `hubify-labs.com` (platform) + `<lab-slug>.hubify.app` (per-lab subdomains) via Cloudflare or Vercel DNS
- [ ] **SSL/TLS** — Let's Encrypt via Vercel/Cloudflare automatic
- [ ] **Monitoring stack** — Sentry for errors, Vercel Analytics for traffic, custom Convex dashboards for platform health
- [ ] **Backup destination configs** — Backblaze B2 + Hugging Face (public) + iCloud (selected dirs)
- [ ] **Cost monitoring + alerts** — per-tenant cost limits, alert thresholds, billing webhooks

**G status:** 0% — entire category untouched.

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
| B. Web mockup | 27 | 49 | 55% |
| C. macOS app | 1 | 5 | 20% |
| D. API spec | 5 | 7 | 71% |
| E. MCP server | 6 | 7 | 86% |
| F. CLI spec | 0 | 8 | 0% |
| G. Deployment infra | 0 | 13 | 0% |
| H. Migration plan | 6 | 9 | 67% |
| I. Houston sign-off | 0 | 7 | 0% |
| **OVERALL** | **86** | **156** | **55%** |

**Translation:** we're roughly halfway. The PRD is in great shape (80%), the web mockup is past the midpoint (51%), the migration plan is mostly done (67%). The 4 untouched categories — **macOS / API / MCP / CLI / Deployment** — are the biggest gaps, all at 0%. Houston review is pending.

**To hit READY = 100%, the loop needs to:**
1. Finish A (~10 items)
2. Finish B (~24 items)
3. **Start AND finish C/D/E/F/G** (~40 items across 5 categories — the bulk of remaining work)
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
