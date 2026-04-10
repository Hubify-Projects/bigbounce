# AgenticUI Revamp Plan — Canonical

**Created:** 2026-04-09 (post-compaction recovery save)
**Status:** ALL 27 COMPONENTS EXTRACTED (Phases 3–26). Phase 57 complete: Compute pods (`.compute-pod` → `chatAbout` pod status, `.soon` pods → "coming soon" context) + `#view-compute .provider-card` wired. Phase 56 complete: Papers view pre-submission checklist `tr` rows → `openSidepeek('paper', n)` (parses "P1 v2.2.1" → n=1); venue `.provider-card` in papers → paper sidepeek via `.provider-spend`; `.pr-round` items → `chatAbout` publish-loop round; `#view-costs .tbl tbody tr` (category rows only, guard skips pre-wired rows) → `chatAbout` cost breakdown. Phase 55 complete: Kanban cards (`.kanban-card`) → detect `EXP-xxx` in title → `openSidepeek('experiment')`, else `chatAbout`; `.kanban-card .owner` spans → agent sidepeek with `stopProp`; `.task-list-row` → same EXP/task routing; `#view-tasks .act-row/.act-agent/.hi` → full activity feed wiring (Phase 48 only covered `#view-comms`); `.task-detail .review-line .agent` + `.comment-author` → agent sidepeek. Phase 54 complete: Backup matrix rows + dossier stat cells. Phase 53 complete: Dossier `.dos-row` routing. Phase 52 complete: Remaining `.tl-item` and `.tl-actor`. Phase 51 complete: Fig cards, wiki entries, dir-row body clicks. Phase 50 complete: Survey table rows in overview + dataset rows in data view → Phase 50 wires `#view-overview .tbl tbody tr` → `openSidepeek('survey', id)` where id = "DESI DR1" etc. (survey name + release, name-only if release is "—"); `#view-data .tbl tbody tr` → `chatAbout` with dataset name + survey + type context. Phase 49 complete: Alerts view — `.alert-row` cards → `chatAbout` alert (child buttons already have `stopPropagation`); resolved `.timeline .tl-item` rows → `chatAbout`; `.tl-actor` spans → `openSidepeek('agent', name)` skipping 'system'/'runpod'; `tbody tr` in 30-day history table → `chatAbout`. Phase 48 complete: Comms activity feed — `.act-agent` spans → `openSidepeek('agent', name)` (skip 'system'); `.hi` spans type-detected: T-xxx → `openSidepeek('task', id)`, EXP-xxx → `openSidepeek('experiment', id)`, `standup.morning` → standup renderer, agent name patterns → agent renderer; `.act-row` full rows → `chatAbout` with timestamp + agent + message context. Phase 47 complete: Standups view fully interactive — .standup-row (complete → standup renderer, scheduled → chatAbout), .tl-item 6 transcript history rows → standup renderer, .comment-author 6 names → agent sidepeek with e.stopPropagation. Phase 46 complete: Agent org-chart fully clickable — DOMContentLoaded delegation on all 22 .org-node:not(.director), reads .org-node-name text, routes to openSidepeek('agent', name); agents with registry entries show full 10-tab detail, others fall back to AGENT_DEFAULTS via Object.assign. Phase 45 complete: Wiki + cross-lab card header actions — bounce model discrimination "cross-lab share →" now `chatAbout()` with full 5-model discrimination table context (7/7 score, §22 contribution); "browse global →" in cross-lab knowledge card now `navTo('comms')`. Phase 44 complete: Settings labs + contributions + pipeline-parent — "view all →" in contributions card now `navTo('contributions')`; pipeline-parent p2-chirality-catalog → `chatAbout()` with pipeline status; 5 Settings lab sharing rows (3 outbound + 2 inbound grants) all → `chatAbout()` with per-row scope/access/date context. Phase 43 complete: Chats view toast() → chatAbout() sweep — all 20 remaining `toast()` chat-row onclick attributes in `view-ideas` replaced with `chatAbout(scope, title, context)`: Lab chats (ACT DR6 QC strategy + Paper 1 round 5 review), Project chats (8: P1 tracer purification, P3 anomaly engine, P4 PTA Bayes, Pipeline 1 cross-match, P2 chirality, DESI×eROSITA, WP4 Fisher forecast, WP5 galaxy spin), Papers chats (10: Paper 1 round 4 review + PRD submission plan, Paper 2 f_NL derivation + SPHEREx 4.38σ + PRL submit, Paper 3 anomaly scope + QC section + tracer bias §5, Paper 4 chirality + MNRAS submission). Each context string preloads exact BigBounce data: sigma values, experiment IDs, survey counts, QC failure reasons, submission targets. 0 `toast()` calls remain in the Chats view. Phase 42 complete: Costs + graph interactions — (A) 9 provider rows in view-costs now `chatAbout()` with per-provider spend context (month/today/cap/% used/agent name); (B) `.gnc-conn-row` delegation wired — "click any row to inspect" now routes by `data-group`: experiment→experiment renderer (with known-ID guard falling back to EXP-049), Paper→paper renderer, contribution→contribution renderer by label prefix, agent→agent renderer, else chatAbout(). Phase 41 complete: Research nav fix + skill catalog upgrade — (A) `navTo('research')` → `navTo('overview')`: Research section header was pointing to non-existent `view-research`, silently failing on click; now correctly routes to `view-overview`; (B) `openSkillDetail(cmd, desc)` global function added after `chatAbout` — wraps `chatAbout()` with skill-scoped context; (C) `.skill-row` delegation in DOMContentLoaded: nullifies all 150+ inline `toast()` onclick attrs via `row.onclick=null`, replaces with `openSkillDetail()` reads from `.sk-cmd`+`.sk-desc`; covers Skills/Workflows/Databases/Formats catalog views. Phase 40 complete: Profile view and sidebar chat interactions wired — (A) `.pinned-lab` cards (4) now open lab renderer via delegation: reads `.pinned-lab-name` text → `openSidepeek('lab', name)` (all 4 names — bigbounce/chirality/pta-gw/quantum-gw — exist in lab renderer); (B) `#view-profile .profile-row` delegation: rows with `.profile-row-num` open paper renderer (keys '1'–'4'), rows without num open contribution renderer via `_resolveContribKey()` substring map (13-entry key map covering all 12 contribution rows + fallback); (C) 8 sidebar `.sb-chat-row` onclick attributes upgraded from `toast('Resuming chat: ...')` to `chatAbout(scope, title, context)` with real scope IDs and rich context strings; total ~24 dead click targets eliminated. Phase 39 complete: task interaction layer fixed — (A) T-102 added to task renderer: EXP-055 ACT DR6 retrain (epoch 3/10, val_loss 0.61, in_progress 30%, comments from anomaly-worker, history showing QC retry after val_loss=22420 failure); (B) kanban-card delegation fixed — was hardcoded to always open T-104, now uses `_resolveTaskId()` with a 10-key title-to-T-ID map covering EXP-055→T-102, EXP-054→T-104, EXP-053→T-103, Paper 1 v2.2.1/f_NL rewrite→T-101, EXP-057→T-105, fig08→T-106, Disk cleanup→T-107, alignment check→T-108; "Promote" cards open agent detail instead; (C) task-list-row delegation added — same `_resolveTaskId()` helper shared between kanban and list modes. Phase 38 complete: added two missing `detailRenderers` entries that showed "No renderer for type: X" error when clicked — (A) `comm-event` renderer: 4-entry registry (xlab-1/2/3/4) covering all cross-lab comm gateway cards in `view-comms`; each entry has direction, peer lab, type, body, context, thread history, lab relationship stats, and action buttons (Accept/Review/Decline for inbound; View/Follow-up/Archive for outbound); (B) `idea` renderer: handles `/promote` slash command (`chat-promote-current` key) + any future `.idea-row` title keys; shows viability score bars (4 dimensions averaged), suggested project goal with accent-border blockquote, and Promote/Note/Dismiss action buttons; both renderers use string concatenation to avoid nested backtick issues. Phase 37 complete: (A) survey table routing bug fixed — overview `.tbl tbody tr` clicks now map short names (DESI/SDSS/LAMOST/eROSITA/Gaia/NEOWISE/ACT/Planck CMB) to full survey renderer keys via `view-overview` case in generic table click handler; (B) pipeline status strip added to overview — 3 `run-exp-card` entries (P1 at 67%, P3 at 100%, P4 at 100%) each with `.ps-step-row` inline step indicators (✓ done / ● active / dim todo), progress bar, and `openProjectDetail()` onclick; (C) CSS: `.ps-step-row`, `.ps-done`, `.ps-active`, `.ps-todo`, `.ps-sep` added after `.run-exp-log`. Phase 36 complete: figure renderer rebuilt — 21-entry registry keyed by exact `.fig-name`/`.fig-hero-title` strings (all 4 paper groups: Paper 1 figs 1-8, Paper 2 figs 1-4, Paper 3 figs 1-6, Paper 4 figs 1-3); each entry has title/res/size/tool/updated/paper/script/data/caption fields; uses string concatenation (not template literal) to avoid nested backtick issues. Task renderer rebuilt — 7-entry registry (T-101, T-103, T-104, T-105, T-106, T-107, T-108) keyed by T-xxx IDs seen in activity feed; each task has priority/status/pct/owner/exp/reviewers/comments/history; exp section links to experiment detail; conditional Stop vs Completed action button; "Chat about this" action preloads task context. Phase 35 complete: contribution renderer rebuilt with 16-entry registry (all real BigBounce contributions); "All contributions" table rows wired with onclick; per-contribution novelty audit trail, adjacent papers, re-review status, "Chat about this" action. Phase 34 complete: experiment detail renderer expanded — EXP-047/048/049 added (were falling back to EXP-054 data), EXP-052 corrected (Gaia→Legacy DR10 cross-match), per-experiment `logs` field with realistic tail log content, conditional Stop/Re-run actions, "Chat about this" action. Phase 33 complete: merged duplicate keydown handlers (two conflicting document.addEventListener('keydown') handlers replaced with single canonical handler, capture=true; fixes double-fire bugs on ⌘B/⌘J/⌘`/⌘1/2/3; ⌘P now opens cmdPalette only; added ? shortcut, ⌘W, improved Esc, improved ⌘`); updated ⌘P Settings row to "Command palette (alias)"; added ? and ⌘W rows to Settings keyboard shortcuts section. Committed.
**Owner:** Houston + Claude
**Supersedes:** none yet (merges Cabinet light-mode work + new AgenticUI kit)

This is the load-bearing document for the final UI revamp phase of Hubify Labs. Read this FIRST after any compaction. Everything else follows from here.

---

## 1. What changed on 2026-04-09

Houston purchased **AgenticUI Figma v1.1** — a premium private design kit that is token-driven, anti-bloat, optimized for LLM consumption, and built on PascalCase component names + lowercased variant values. He wants this to merge into the existing Cabinet-inspired light-mode work, NOT replace it.

The previous UI phase (Cabinet audit → cream/cocoa/sage light mode → sage accent → collapsible sidebar → right-pane core views → no sidepeeks for core content) is preserved. AgenticUI adds component-level discipline on top.

## 2. Hard constraints (Houston's direct quotes and directives)

1. **"keep the soft beige natural vibe accent"** — Cabinet cream/cocoa/sage palette stays as the brand. No full black/white. No rainbow. Sage `#5fb88a` is brand identity unchanged across themes.
2. **"don't want you to totally destroy everything we have built"** — merge, don't rewrite. Salvage and repurpose existing mockups.
3. **Light mode is default** — dark mode is a toggle, light is home. Cabinet scheme is the identity.
4. **No sidepeeks for core pages** — right-pane views are the default. Sidepeeks only for ephemeral peek-and-close. (Memory: `feedback_sidepeek_philosophy.md`)
5. **"keep the current web/desktop/marketing site mockups as they are now — and maybe create a new separate system for this next phase going forward"** — backup v2-sage as-is, build v3-agentic alongside, both must open perfectly side-by-side.
6. **"save that audit/details in a file in project-context as the start of a new file that will supersede the ui/ux branding stuff"** — THIS file + `AGENTIC_UI_KIT_AUDIT.md` once access is fixed.
7. **"take this next big prompt with a super-slight grain of salt since the claude who wrote the prompt is not you and doesn't have any context"** — the outside-Claude "Agentic UI Master Agent Prompt" is reference material, not doctrine. Houston's directives override it.
8. **All three surfaces stay equivalent** — Web, Desktop (Tauri wrapper), CLI TUI are all full IDEs. (Memory: `feedback_surfaces_vs_get.md`)
9. **"whip up a quick one shot view for me to confirm it works"** — prove Figma MCP round-trip works before any big extraction work.

## 3. Figma access — THE BLOCKER

**File:** `https://www.figma.com/design/ZjIGTHNBdAXglOYEDZAnd8/AGENTIC-DESIGN-SYSTEM--v1.1-?node-id=123-395`
- `fileKey`: `ZjIGTHNBdAXglOYEDZAnd8`
- Root nodeId to start audit: `123:395` (the landing node from Houston's URL)

**Authenticated user:** `houston@bamf.ai`, team "Houston Golden's team"
**Plan tier:** `starter`
**Seat type:** `view`

**Hard limit from Figma docs (`plans-access-and-permissions.md`):**
> Users on a Starter plan or with View or Collab seats can make up to 6 tool calls per month.

**Current error on all `get_metadata` / `get_variable_defs` / `get_design_context` calls:**
`"This figma file could not be accessed."`

**Most likely cause:** the AgenticUI kit was duplicated into a different account or was never duplicated into `houston@bamf.ai`'s team at all. Community files must be explicitly duplicated before MCP can reach them.

**Secondary cause:** 6-call monthly quota may already be exhausted from previous attempts.

### Three unblock paths (in order of ease)

1. **Duplicate the file into `houston@bamf.ai`'s team** — open the AgenticUI Figma URL while logged in as `houston@bamf.ai`, click "Duplicate" (or "Use this file"), confirm the copy appears in the team drafts/workspace. Then share the new URL (new fileKey).
2. **Upgrade Figma plan** — Pro + Full or Dev seat gives 200 calls/day (`10/min` rate limit). This is the correct long-term move since we'll pull this kit repeatedly.
3. **Manual export** — in Figma: right-click every frame → "Copy as PNG" + export variables as JSON + export component library as JSON. Dump into `project-context/agentic-ui-kit/` and I'll parse that without MCP.

**DO NOT make any more MCP calls to this file until Houston picks a path.** Every failed call still counts against the 6/month quota.

## 4. The outside-Claude "Master Agent Prompt" (reference, not doctrine)

The prompt Houston pasted was written by a Claude without any of our project context. Take it with a grain of salt — it assumes a greenfield project, it wants to generate components from scratch, and it doesn't know about our Cabinet work, sage brand, light-mode-first stance, or surfaces architecture.

**Useful parts to keep:**
- **Token mapping phase** → read Figma variables, normalize into CSS custom properties. Good discipline.
- **Lowercased variant values** (`lg`/`md`/`sm` not `Large`/`Medium`/`Small`). Good standard.
- **Unified state enum** (`default | hover | focus | active | disabled`). Good.
- **Unified `Selected` prop** instead of a dozen ad-hoc "isActive" booleans. Good.
- **Anti-bloat rule** — no icon libraries, use SVGR. Good match for our current inline-SVG discipline.
- **Storybook variant matrix** as a QA gate. Good.

**Parts to ignore or adapt:**
- Any instruction to wholesale replace existing components.
- Any instruction to scaffold a new project — we merge into `hubify-labs-mockups/`.
- Any instruction to use dark-first — we are light-first, Cabinet cream is home.
- Any instruction to strip "color" in favor of black/white — sage brand stays.

## 5. Mockup inventory (what we have now)

Directory: `/Users/houstongolden/Desktop/CODE_2025/hubify-labs-mockups/`

| File | State | LOC | Notes |
|---|---|---|---|
| `index.html` | v2-sage (current) | 15,751 | Web IDE. Cabinet light mode + sage accent. Collapsible sidebar, right-pane views, chat dock. The main artifact. |
| `desktop-app-mockup.html` | v2 | 527 | Tauri wrapper preview — iframes `index.html` inside native macOS chrome. |
| `cli-tui-mockup.html` | v2 | 475 | Terminal TUI mirror of the web IDE. |
| `marketing-site-mockup.html` | v2 | 5,223 | Public landing page. Light mode sync just landed. |
| `index-v1-broken.html.bak` | archive | 194,147 bytes | Old broken v1, keep for reference. |
| `index-v2-sage.html.bak` | v2 snapshot | 1.37 MB | **Created 2026-04-09 before revamp work. This is the golden v2 snapshot.** |

**All four mockups share the same CSS token scheme** — `--bg`, `--surface`, `--text-bright`, `--accent` (sage), `--ui` (Inter/SF Pro), `--mono` (JetBrains Mono), `--serif` (Newsreader).

## 6. Revamp plan (phased, executable once Figma is unblocked)

### Phase 0 — Access fix ✅ COMPLETE (2026-04-09)
- [x] Houston duplicated file into bamf.ai account
- [x] New fileKey: `SjPhSVKTbtE35Xh7PNsmNA`
- [x] Confirmed access: `get_metadata` + `get_design_context` both working
- [x] Full color ramps, shadow spec, label type tokens extracted to `AGENTIC_UI_KIT_AUDIT.md §10`

### Phase 1 — Full kit audit (saves `AGENTIC_UI_KIT_AUDIT.md`)
- [ ] `get_metadata` on root node — extract page structure, frame tree, component count
- [ ] `get_variable_defs` on root — pull every color, spacing, typography, shadow, radius token
- [ ] Walk frame tree, `get_design_context` on each major showcase frame (Buttons, Inputs, Cards, Nav, Modals…)
- [ ] Map every component to a normalized name (PascalCase), variant set (lowercase), states, sizes
- [ ] Save full audit to `project-context/AGENTIC_UI_KIT_AUDIT.md`
- [ ] Cross-reference against Cabinet tokens — note every conflict, gap, addition

### Phase 2 — Token merge (updates `style.css` / mockup inline CSS)
- [ ] For each AgenticUI token, decide: adopt / adapt / reject
- [ ] Preserve Cabinet cream/cocoa backgrounds and sage brand
- [ ] Adopt AgenticUI's spacing scale, radii, shadows, motion curves if they're better
- [ ] Adopt AgenticUI's type ramp if it's tighter
- [ ] Normalize all mockup tokens to match

### Phase 3 — Component merge ✅ COMPLETE (2026-04-09)
Order executed: Buttons → Badges → Inputs → Cards → Tabs → Toasts.
All sourced from Figma MCP. Cabinet brand preserved throughout. Departure Mono on labels/buttons, Geist on body/badges/inputs.

### Phase 4 — Surface sync ✅ COMPLETE (2026-04-09)
- [x] `v3/index.html` — all components applied (the main web IDE)
- [x] `v3/desktop-app-mockup.html` — full radius scale added to :root patch
- [x] `v3/cli-tui-mockup.html` — label-mono already present; terminal-only (chars for shapes)
- [x] `v3/marketing-site-mockup.html` — --r-sm/--r-2xl added, all other tokens already present

### Phase 5 — QA + sign-off ✅ COMPLETE (2026-04-09)
- [x] Light mode default + dark mode toggle both work
- [x] All clickable elements have hover/focus/active states
- [x] No sidepeek for core content
- [x] Sage accent rare and earned (primary btn, badge-success, active indicators only)
- [ ] Houston side-by-side review of v2-sage vs v3-agentic (open v3-compare.html)

### Phase 7 — Token QA sweep + remaining components (2026-04-09)
- [x] **Radius tokenization** — global sed sweep: 3px→--r-sm, 5px→--r-md, 8px→--r-lg, 9px→--r-pill, 4px→--r-sm, 6px→--r-md. Intentional exceptions preserved (7px toggle, 10px score badge, 2px micro chips, 50% circles, scrollbar, PDF page).
- [x] **Elevation tokenization** — `.proj-scope .ps-picker-menu`, `.cmdp`, `.hm-tooltip`, `.graph-node-card`, `.file-preview-img-frame` all switched to `var(--elev-*)` + `0.5px solid var(--border)`.
- [x] **Chat autocomplete** (`.chat-hint`) — upgraded to r-xl + 0.5px border + elev-3.
- [x] **Switch/Toggle** — Figma node 814:110 — rebuilt to spec: 29×16px pill (sm), 43×24px (lg), sage active bg, thumb circle same height, inset shadow on track, left↔right transition. `.toggle-sw-lg` variant added. Disabled state at 40% opacity.
- [x] **Checkbox** — Figma node 4067:1119 — 24×24px container, 16×16px box, r-sm, checked/indeterminate/disabled states, CSS ::after checkmark/dash. `.checkbox-row` + `.checkbox-label` + `.checkbox-sub` for inline label rows. Wired into Settings Cross-model review: 6-provider multi-select grid (GPT-4o ✓, Gemini 2.5 ✓, Perplexity ✓, Grok, Sonar Pro, o3-disabled).
- [x] **Tooltip** — Figma node 2001:2681 — `.tooltip-wrap` + `.tip` CSS class system (hover-reveal, all 4 positions). `[data-tip]` auto-tooltip via ::before/::after (no wrapper needed), dark bg #191919, Geist 12px, r-sm, caret arrow. Wired to 22 elements: all icon-btn toolbar buttons, sb-collapse-btn, sb-footer-btn, sb-action items.
- [x] **Progress bar** — Figma node 4072:6991 — AgenticUI barcode tick style: 1px bars + 2px gaps via `repeating-linear-gradient`, `--prog` CSS var drives fill, sage accent fill. Sizes: sm(4px)/default(6px)/lg(16px). Wired to all 3 pipeline cards, EXP-054 (67%), EXP-055 (30%), Director backup row (89%). Old 2px solid `.pipeline-progress-bar` replaced.
- [x] **Radio button** — Figma node 124:2977 — `appearance:none` 16×16px circle, `border:1px solid border-strong` unselected, `radial-gradient` sage inner dot (44%) + `border:1.5px solid accent` selected. `input[type="radio"].radio-input` standalone class + `.dispatch-radio input` wired to dispatch form. `.dispatch-radio` upgraded to Geist 12px / r-md / `gap:7px`.
- [x] **Search** — Figma node 338:6162 — sm: `h:32px`, `surface-2 bg`, `0.5px border`, `r-lg`, Geist 13px, SVG magnifier via CSS `background-image` (zero HTML changes). Focus: `bg→white`, `border→border-strong`, 2px ring. Applies to `.filter-search` + `.filter-search-minimal` — wires automatically to all 6 view header search inputs.
- [ ] Remaining inline style radii (in HTML, not CSS) — deferred, lower impact
- [ ] Houston side-by-side review

### Phase 7 STATUS: All planned components complete. ✅

### Phase 8 — Remaining unimplemented AgenticUI components ✅ COMPLETE (2026-04-09)
- [x] **Breadcrumbs** — proj-scope bar IS the breadcrumb (bigbounce › all projects › Experiments)
- [x] **Stepper** — node 4001:1347 — pill-shaped step indicators in all 3 pipeline cards
- [x] **Skeleton** — node 761:23192 — shimmer loading cards in overview Live experiments section
- [x] **Code block** — node 4126:5640 — syntax-highlighted blocks in chat messages (bash + python)
- [x] **File upload** — node 4028:6200 — drag-drop zone in dispatch form with file chips
- [x] **Pagination** — node 716:3790 — "10 of 53 experiments" + prev/next/page pills
- [x] **Helper text** — node 4066:7445 — helper text below dispatch form title input

### Phase 9 — Workspace Shell Redesign ✅ COMPLETE (2026-04-09)
Implements the AGENTICUI_DEEP_PHILOSOPHY_PLAN.md north star in full.

- [x] **9.1 Chat input pill** — 20px radius, floating, elev-2, send btn black when text present
- [x] **9.2 Survey grid → table** — 7 columns, sortable, all 8 surveys with real BigBounce data
- [x] **9.3 Text input spec** — 40px height, 0.5px border, r-lg, Departure Mono labels, helper text
- [x] **9.4 cmdK elevation-4** — r-3xl (20px), Geist 15px input, Departure Mono keyboard chips
- [x] **9.5 Stat cards** — 0.5px border, label-mono labels, hover bg, stat-trend badges, tabindex
- [x] **9.6 Section headers** — label-mono + action buttons (SSH/Manage, Refresh/All, New, Spawn/Config)
- [x] **9.7 Breadcrumbs** — proj-scope bar applied with .breadcrumb semantics to all relevant views
- [x] **9.8 File upload zone** — drag-drop in dispatch form, file chip list, JS handlers
- [x] **9.9 Icon audit** — .ic 14→16px, icon-btn/footer-btn 28→32px, --btn-icon-sm/md tokens
- [x] **9.10 Interaction states** — global disabled (40% opacity), expanded focus-visible, tabindex
- [x] **Sortable columns** — sortTbl() JS, ↕/↑/↓ indicators, default ID desc sort
- [x] **Row actions** — View/Re-run/Logs/Stop/Run now context buttons on all 10 experiment rows
- [x] **Color discipline** — pill-pass = sage (earned status), pill-run = neutral
- [x] **Typography** — chat-msg-body 14px/Geist (was 12.5px)
- [x] **Pulsating asterisk** — ✳ glyph with ast-pulse, replaces spinning orb
  → **REVERTED (2026-04-10)**: Cosmic orb restored. HTML `<div class="thinking-orb mode-saturn">` + `setInterval(rotateOrb,24000)` both back. The orb CSS (10 modes: SATURN/PULSE/ORBIT/TWINKLE/BEAKER/GRID/SATELLITE/ATOM/FACE/DNA) was already intact; Phase 9 had incorrectly disabled both the HTML and the JS interval.
- [x] **Status dot pulse** — dot.good has dot-pulse halo animation (active labs feel alive)

### Phase 10 — Button wiring + nav active fix ✅ COMPLETE (2026-04-10)

- [x] **Phase 4 button wiring** — All `dir-action-btn` HTML replaced with canonical `.btn` classes throughout Director view + Papers view:
  - `dir-action-btn primary` (approve, promote) → `.btn.btn-xs.btn-primary` (sage fill — earned confirmation)
  - `dir-action-btn primary` (open in editor) → `.btn.btn-xs.btn-ghost` (visible but not sage)
  - `dir-action-btn` (later, defer) → `.btn.btn-xs.btn-link` (least visual weight — dismissive)
  - `dir-action-btn danger` (deny) → `.btn.btn-xs.btn-danger` (red hover on danger)
  - Papers PDF buttons: emoji removed (`📄 Open PDF`→`Open PDF`), proper `.btn.btn-sm.btn-ghost/.btn-link` classes
- [x] **dir-chat-btn upgrade** — All 7 instances now compose with `.btn.btn-xs.btn-ghost dir-chat-btn`. CSS trimmed to just sage hover override (no duplicate base styles). "chat about this" renders in Departure Mono uppercase.
- [x] **Nav active indicator conflict** — Added `.nav-sub-links-track .sb-child-item.active::before{display:none!important}` to suppress old dot that was conflicting with the `../` + `■` active indicator.
- [x] **Section name typography** — `.dir-section-name` switched from `var(--mono)` to `var(--label-mono)` (Departure Mono). Section meta emoji `[💬]` removed.

### Phase 11 — Tabs + Chat Input spec upgrade ✅ COMPLETE (2026-04-10)

Figma calls: Tabs (4056:1314) + Chat Input (4127:18971).

- [x] **Preview tabs — underline style**: Replaced sagdot `::before` active indicator with `box-shadow:inset 0 -2px 0 var(--text-bright)`. Matches AgenticUI underline variant (active `border-b border-[var(--border/strong)]`). `::before{display:none}`.
- [x] **Sidebar mode tabs — segmented pill**: `.sb-mode` converted to pill tray with `background:var(--surface-2)`, `border-radius:var(--r-pill)`, `padding:4px`, `margin:0 10px 8px`. Individual `.sb-mode-tab` now `background:transparent; border:none; border-radius:var(--r-pill)`. Active tab: `background:var(--surface)` + `box-shadow:0 1px 2px rgba(0,0,0,.05),inset 0 -1px 0 rgba(0,0,0,.08)`. Perfectly matches AgenticUI segmented chip with raised active state.
- [x] **Chat input wrapper**: `chat-input-wrap` changed from `border-top + var(--surface)` to `background:var(--surface-2)` (no divider line) — matches Figma outer `bg-secondary` container.
- [x] **Chat action buttons**: `chat-act-btn` bumped from 32×32 to 40×40px, icons from 16×16 to 20×20 — matches Figma 40px circle spec.
- [x] **Chat pill hover**: Added `.chat-input-pill:hover{border-color:var(--border-strong)}` — matches Figma `border/medium` hover state.
- [x] **Textarea padding + lineHeight**: `padding:12px 14px 6px`, `line-height:24px`, `min-height:72px` — closer to Figma 8px all-around with 24px line height.
- [x] **Actions bar padding**: tightened `chat-input-actions` to `padding:4px 6px 8px` + `gap:4px` — snugger to match Figma.

### Phase 12 — TextArea spec + Settings input sweep ✅ COMPLETE (2026-04-10)

Figma calls: TextArea (4092:1380).

- [x] **Canonical `.textarea` class** — AgenticUI spec applied: `1px solid border/subtle`, `r-lg`, `12px padding`, `bg-primary (var(--bg))`, Geist 14px / 18px line-height, focus → `border-bright`, disabled → `surface-2 + opacity:.4`, error → `#d50b0b border`. `.textarea-error` for error helper text (pink bg `#ffdede`, red text).
- [x] **`.textarea-label`** — Departure Mono 12px uppercase 0.3px tracking (matches AgenticUI input label spec). Added as standalone class.
- [x] **Dispatch form label upgrade** — `.dispatch-field label` updated from `var(--mono)` to `var(--label-mono)` (Departure Mono), size 12px → 12px, tracking 0.6px → 0.3px. Now consistent with AgenticUI.
- [x] **Inline textareas replaced** — System prompt + Bio textareas in Agents/Settings view: inline styles removed, now use `.textarea` class (+ `style="min-height:..."` override only where needed). System prompt keeps `font-family:var(--mono)` per technical content convention.
- [x] **Settings panel input sweep** — All `input[type="text"]` within `.sp-text` and `.sp-row .v` upgraded via contextual CSS selectors. Full-width: `h:32px`, `r-lg`, `0.5px border`. Inline-row: `h:26px`, `r-md`, `0.5px border`. All use `bg-primary (var(--bg))`, Departure Mono labels, focus `border-bright`. Covers 10+ inputs across Chat History, Agent config, Notes, Profile, Terminal settings panels.

### Phase 13 — Inline style cleanup sweep ✅ COMPLETE (2026-04-10)

No Figma calls — all components now extracted. Focus: replace remaining inline styles with canonical classes.

- [x] **`.card-body-pad` class** — added CSS utility `padding:14px 16px`. Replaced all 11 inline `class="card-body" style="padding:14px 16px"` → `class="card-body card-body-pad"` via `replace_all`.
- [x] **`.chart-pad` class** — `padding:18px 16px 14px` for SVG chart wrappers. 2 instances replaced (`style="padding:18px 16px 14px"` → `class="chart-pad"`).
- [x] **`.content-pad` class** — `padding:14px` for generic content wrapper divs. 1 instance replaced.
- [x] **`.standup-list` padding** — moved `padding:14px` from inline style into CSS class. Removed from all `class="standup-list" style="padding:14px"` instances.
- [x] **Settings `<select>` elements** — 3 `<select>` with identical inline style removed. Now styled via `.sp-row .v select` contextual CSS (same spec as settings text inputs: `bg-primary`, `0.5px border`, `r-lg`, `h-32px`, mono font, focus `border-bright`, custom `-webkit-appearance:none`).
- [x] **`.sp-select` + contextual select CSS** — canonical CSS class added near `.sp-text input` rules.
- [x] **Compute management buttons** — 4 `.btn.btn-ghost` with `style="font-size:10px;padding:3px 9px"` replaced with `.btn.btn-xs.btn-ghost` (clean 24px canonical size).
- [x] **`.org-node-role` font-size** — `font-size:10px` moved from per-element inline style into CSS class definition. 4 elements cleaned up.

### Phase 23 — Pagination 32px + Switch hover/focus spec (2026-04-10) ✅ COMPLETE

Figma calls: `get_metadata(123:376)` Pagination · `get_metadata(814:72)` Switch.

**23A — Pagination component (AgenticUI 716:3790)**
- [x] **`.pg-btn`** — upgraded 26×26px → **32×32px**, `font-size:9px → 11px`, `border-radius:r-sm(3px) → r-md(5px)`, `gap:3px → 2px`
- [x] **`.pg-num`** — upgraded 26×26px → **32×32px**, `font-size:10px → 11px`, `border-radius:r-sm → r-md`
- [x] **`.pg-dots`** — upgraded 26×26px → **32×32px** (consistent sizing)
- [x] **Comment block** added: `/* ══ PAGINATION — AgenticUI 716:3790 · item 32×32px · simple 48h · numbered 64h ══ */`

**23B — Switch component (AgenticUI 814:110)**
- [x] **Thumb inset** — fixed 0-inset → **2px inset**: `top:2px;left:2px;width:12px;height:12px` (was `top:0;left:0;width:16px;height:16px`)
- [x] **On position** — `left:13px → left:15px` (29-12-2=15, correct for 2px inset)
- [x] **Border added** — `border:0.5px solid var(--border-strong)` when off; `border-color:var(--accent-dim)` when on
- [x] **Hover state** — `background:var(--surface-4);border-color:var(--border-bright)` (off), `filter:brightness(1.07)` (on). Guards: `:not(.disabled):not([disabled])`
- [x] **Focus ring** — `0 0 0 2px var(--bg), 0 0 0 4px var(--accent)` focus ring on `:focus-visible`
- [x] **lg thumb** — corrected 24×24 → **20×20px**, `on::after{left:21px}` (43-20-2=21, was 19)
- [x] **Comment block** added: `/* ══ SWITCH — AgenticUI 814:110 · sm 29×16 · lg 43×24 · thumb inset 2px ══ */`

### Phase 32 — ⌘N fix + org-chart delegation + experiment View buttons (2026-04-10) ✅ COMPLETE

No Figma calls.

**32A — ⌘N keyboard shortcut bug fix**
- [x] **Was**: `navTo('dispatch')` — no `view-dispatch` exists anywhere in the DOM. Silently fails.
- [x] **Root cause**: dispatch form is `.card.collapsible#dispatchFlowCard` inside `#view-experiments`, toggled via `.expanded` class.
- [x] **Fix**: `navTo('experiments'); setTimeout(()=>{ card.classList.add('expanded'); card.scrollIntoView({behavior:'smooth'}) }, 60)`
- [x] Settings row description updated: "Go to Experiments · open dispatch form"

**32B — Org-chart click delegation (22 agents)**
- [x] `.org-node` cards already had `cursor:pointer` and `:hover` border-color transition in CSS, but zero onclick handlers
- [x] Added `document.addEventListener('click', e=>{ const node = e.target.closest('.org-node'); ... openDetail('agent', name) })` — single handler covers all 22 nodes
- [x] Guard: skips if target is `button` or `a` inside node (prevents double-firing on inner actions)
- [x] Guard: skips if name === 'houston' (director = user, no agent detail needed)

**32C — Experiment table View/Logs buttons wired**
- [x] 9 buttons updated: EXP-047, 048, 049, 050, 051, 052, 053 → "View" calls `openDetail('experiment', id)`
- [x] EXP-054, 055 → "Logs" buttons call `openDetail('experiment', id)` (shows tail logs in detail view)
- [x] Re-run/Stop buttons kept as `toast()` (destructive actions — confirmation via toast is correct for mockup)
- [x] EXP-056 "Run now" kept as `toast()` (queued, not yet run)

**Committed:** Phase 32 changes committed alongside Phases 27-31 as batch commit `356a294` in hubify-labs-mockups.

---

### Phase 33 — Duplicate keydown handler merge + Settings shortcut rows (2026-04-10) ✅ COMPLETE

No Figma calls.

**Root cause:** Two separate `document.addEventListener('keydown', ...)` handlers existed on `document`. First (Phase 30, capture=true) had ⌘B/⌘J/⌘1/2/3/⌘` + ⌘P → `.sb-search.click()`. Second (pre-existing, bubble phase) also had ⌘B/⌘J/⌘1/2/3/⌘` + ⌘P → `openCmdPalette()`. Both fire since both are on `document` — capture fires before bubble, but both complete.

**Bugs fixed:**
- ⌘B toggleSidebar fires twice → sidebar flickers then ends up same state (net = no effect)
- ⌘J/⌘/ toggleChatVisible fires twice → chat hides then shows (net = no effect)
- ⌘` setChatMode fires twice → terminal toggle cancels itself (net = no effect)
- ⌘P fires `.sb-search.click()` AND `openCmdPalette()` simultaneously

**33A — Merged canonical keydown handler**
- [x] Replaced first handler with merged version (single `capture=true` handler)
- [x] Kept all unique features from both handlers
- [x] Added: `?` key → opens shortcuts help overlay (guards: not inside input/textarea/select)
- [x] Added: ⌘W → closes active file preview tab (guards: `fpActiveTab` defined and truthy)
- [x] Improved: ⌘` now shows chat panel first if `chatPos==='hidden'` before toggling mode
- [x] Improved: Esc now also closes `#labDD` and `#chatPosDD` dropdowns
- [x] Improved: ⌘P opens cmdPalette only (no more sidebar search click)

**33B — Deleted duplicate second handler**
- [x] Second handler body replaced with single comment: `// (duplicate keydown handler removed in Phase 33 — all shortcuts merged into canonical handler above)`

**33C — Settings keyboard shortcut rows updated/added**
- [x] ⌘P row: title → "Command palette (alias)", desc → "Same as ⌘K · Cursor/VSCode convention"
- [x] ⌘1/2/3 row: added `border-bottom:1px solid var(--border)` separator
- [x] New `?` row added: "Shortcuts help" / "Show keyboard shortcuts overlay · works outside text inputs"
- [x] New ⌘W row added: "Close file tab" / "Close active file preview tab · only fires when a tab is open"

**Committed:** Phase 33 committed in hubify-labs-mockups.

---

### Phase 34 — Experiment renderer data expansion (2026-04-10) ✅ COMPLETE

No Figma calls.

**Root cause:** Experiment detail renderer only had 6 entries (EXP-050—055). Clicking View on EXP-047/048/049 fell back to EXP-054 (Planck galactic mask) data — wrong experiment shown. EXP-052 was also wrong (showing Gaia DR3 10× expansion instead of Legacy DR10 cross-match).

**34A — Added EXP-047/048/049 with real BigBounce data**
- [x] **EXP-047** — eROSITA X-ray sweep · P3 · 930K sources · 9,303 anomalies · 73% novel vs NED/Simbad · 1h 8m · $12.80
- [x] **EXP-048** — SDSS DR18 QSO photometry · P3 · 2.3M spectra · 77,905 anomalies · 3.4% rate · QC: 98% blue-excess bias · 44m · $6.40
- [x] **EXP-049** — Bounce model discrimination · Branch · 5 models · matter bounce preferred 2.3σ · quintom-B viable · 1h 56m · $3.20

**34B — Fixed EXP-052**
- [x] Was: Gaia DR3 10× expansion (wrong survey, wrong result, wrong runtime)
- [x] Now: Legacy DR10 cross-match · P1 · DESI 195,829 anomalies × LS DR10 photometric · 6-band added · 8m · $1.80

**34C — Per-experiment logs field**
- [x] Added `logs:` field to all 9 experiments with realistic timestamped output
- [x] Renderer template now renders `${e.logs}` instead of hardcoded Planck log lines

**34D — Conditional actions bar**
- [x] Stop button only shown when `e.status === 'running'`; Re-run only when not running
- [x] Added "Chat about this" action that calls `chatAbout()` with full experiment context preloaded

**Committed:** Phase 34 committed in hubify-labs-mockups (`b5a0654`).

---

### Phase 31 — Shortcut bug fix + ⌘J/1/2/3 wiring + notif drawer fade (2026-04-10) ✅ COMPLETE

No Figma calls.

**31A — ⌘/ bug fix**
- [x] **Was**: `const cp=document.getElementById('chatPane');if(cp){const hidden=cp.classList.contains('pos-hidden');...}` — `#chatPane` doesn't exist, `pos-hidden` not used
- [x] **Fix**: `toggleChatVisible()` — already defined at line 14895, correctly checks `chatPos==='hidden'` and calls `setChatPos('left'/'hidden')`

**31B — ⌘J wired (matches existing "Hide chat (⌘J)" tooltip in header)**
- [x] `e.key==='j'` → `toggleChatVisible()` (same behavior as ⌘/)

**31C — ⌘1/2/3 wired (matches existing dropdown ⌘1/2/3 hints)**
- [x] `e.key==='1'` → `setChatPos('left')` — Left (default)
- [x] `e.key==='2'` → `setChatPos('right')` — Right
- [x] `e.key==='3'` → `setChatPos('bottom')` — Bottom

**31D — Notification drawer scroll-fade**
- [x] `.notif-drawer-body` → added `scroll-fade-y` class
- [x] All 6 scroll-fade containers now complete: sb-body, chat-body, vibe-chat-body, notif-drawer-body, settings-nav, (scroll-fade-x unused but ready)

**31E — Keyboard shortcuts section updated to 10 rows**
- [x] Added ⌘J (Hide chat) and ⌘1/⌘2/⌘3 (Chat position) rows
- [x] Last row (Focus search) gained `border-bottom` to match spacing pattern before new rows
- [x] ⌘1/2/3 displayed as 3 kbd chips on a single row

### Phase 30 — Theme button fix + Keyboard shortcuts + scroll-fade (2026-04-10) ✅ COMPLETE

No Figma calls.

**30A — Appearance section theme buttons fixed (critical bug)**
- [x] **Bug**: buttons called `document.documentElement.classList.remove/add('dark-mode')` — class that doesn't exist in CSS
- [x] **Fix**: buttons now call `classList.add/remove('light')` (correct class) + `localStorage.setItem('hubify-theme',...)` + `_updateThemeIcons(isLight)`
- [x] **System button**: uses `window.matchMedia('(prefers-color-scheme:light)').matches` to detect OS preference, removes localStorage key so future OS changes are followed
- [x] **`_updateThemeIcons` extended**: now also syncs `#theme-light-btn` and `#theme-dark-btn` class names — `_applySavedTheme()` runs this on init, so Settings buttons show correct active state on first load

**30B — vibe-chat-body scroll-fade**
- [x] **`vibe-chat-body`** — added `scroll-fade-bottom` class (sandbox chat panel fades into input)

**30C — Keyboard shortcuts settings section (21st settings section)**
- [x] **"Shortcuts" nav item** added between Terminal and Appearance (keyboard icon)
- [x] **Section content**: 7 shortcut rows using `<kbd>` chips (label-mono / surface-3 / border-strong / r-sm):
  - `⌘K` — Command palette
  - `⌘N` — New experiment (dispatch)
  - `⌘/` — Toggle chat
  - `` ⌘` `` — Toggle terminal
  - `⌘B` — Toggle sidebar
  - `⌘,` — Open settings
  - `⌘P` — Focus sidebar search
- [x] **All 7 shortcuts wired** in the existing `keydown` listener (extended from Esc-only):
  - `⌘K` → `openCmdPalette()`
  - `⌘N` → `navTo('dispatch')`
  - `⌘/` → toggle `setChatPos('hidden')` / `setChatPos('left')`
  - `` ⌘` `` → `setChatMode(chatMode==='term'?'chat':'term')`
  - `⌘B` → `toggleSidebar()`
  - `⌘,` → `navTo('settings')`
  - `⌘P` → `.sb-search` click
- [x] **Esc** also now closes command palette if open

### Phase 29 — Scroll fade wiring + Terminal settings section (2026-04-10) ✅ COMPLETE

No Figma calls — targeted wiring pass.

**29A — Scroll fade wiring**
- [x] **`.sb-body`** — added `scroll-fade-y` class. Sidebar nav list now fades at both top and bottom edges as user scrolls, indicating overflow content.
- [x] **`.chat-body`** — added `scroll-fade-bottom` class (bottom-only). Chat messages fade into the input bar at the bottom; top stays fully visible.

**29B — Settings nav default active fix**
- [x] **Profile** nav item promoted to default `active` state (was Models). Conventional settings UX: account/profile is shown first on open. Models item reverted to no `active` class.

**29C — Terminal settings section (20th settings section)**
- [x] **Terminal nav item** added between Notifications and Appearance (terminal `>_` icon)
- [x] **Terminal content section**: 5 settings rows + 2 switch-with-label rows:
  - Font family: `<select>` (JetBrains Mono selected / Fira Code / Cascadia / SF Mono / Menlo)
  - Font size: 4-button segmented (11 / **12** / 13 / 14) — 12 btn-primary
  - Shell: `/bin/zsh` display row
  - Scrollback buffer: 3-button (5K / **10K** / 50K) — 10K btn-primary
  - Cursor style: 3-button (Block / Bar / Underline) — Block btn-primary
  - Copy on select (ON), Bell sound (OFF) — both as switch-with-label rows

### Phase 28 — Settings nav sticky + Profile + Appearance sections (2026-04-10) ✅ COMPLETE

No Figma calls — polish pass on settings view.

**28A — Settings nav sticky rail**
- [x] **`.settings-nav`** — `overflow:hidden → overflow-y:auto`, added `position:sticky;top:16px;max-height:calc(100vh - 100px)`. Nav now sticks as user scrolls the right-pane content, scrolls itself if viewport is short.
- [x] **`scroll-fade-bottom`** class added to `.settings-nav` div in HTML — masks last items at bottom edge when nav overflows.

**28B — Profile settings section (first in nav + content)**
- [x] **Profile nav item** added as first item in settings nav (user icon, `scrollToSettingsSection(this,'Profile')`)
- [x] **Profile content section**: HG avatar initials (48px sage circle), 2×2 input grid (Display name / Email / Affiliation / Location), real BigBounce data (houston@hubify.com · Independent Researcher · Los Angeles, CA)
- [x] **Public profile row**: badge-success "Public" + description citing 328K anomalies / 4 papers / 53 experiments
- [x] **Researcher verification row**: "Verify →" ghost button with toast feedback

**28C — Appearance settings section (last in nav + content)**
- [x] **Appearance nav item** added as last item in settings nav (sun icon)
- [x] **Theme row**: 3-button segmented group (Light/Dark/System) — Light btn-primary by default, Dark toggles `dark-mode` class on `<html>`, System shows toast
- [x] **Accent color row**: locked sage #5fb88a swatch + label-mono hex display
- [x] **3 switch-with-label rows**: Reduce motion (OFF), Compact layout (OFF), Sidebar labels (ON)
- [x] Wires the Phase 25 `.switch-with-label` compound for all 3 rows

### Phase 27 — Scroll fade utility + Notifications settings section (2026-04-10) ✅ COMPLETE

No Figma calls — all 27 component spec pages exhausted. STYLE TESTER + PLAYGROUND are showcase-only.

**27A — Scroll Fade utility CSS (AgenticUI MISC 4092:1131)**
- [x] **`.scroll-fade-y`** — vertical mask-image gradient: `transparent 0 → #000 20px` top edge, `#000 calc(100%-20px) → transparent 100%` bottom edge
- [x] **`.scroll-fade-x`** — horizontal variant (left→right same pattern)
- [x] **`.scroll-fade-bottom`** — bottom-only fade: `#000 80% → transparent 100%` (for lists that overflow at bottom)
- [x] Placed after `.chat-divider-label` block, before `/* ══ PREVIEW ══ */` section comment

**27B — Notifications settings section (wires Phase 25 `.switch-with-label` compound)**
- [x] **"Notifications" nav item** added to Settings sidebar (bell SVG icon, after "Lab Operations")
- [x] **`settings-section` block** with 7 `.switch-with-label` rows using real BigBounce notification context:
  - `Experiment completed` (ON) — "when any run finishes — pass or fail"
  - `New anomaly result` (ON) — "DESI · SDSS · eROSITA · LAMOST sweep results"
  - `Credit threshold` (ON) — "warn at 20% remaining GPU credits"
  - `Cross-model review ready` (ON) — "GPT-4o / Gemini / Perplexity review complete"
  - `Paper readiness change` (ON) — "when paper crosses a readiness milestone"
  - `Daily standup transcript` (OFF) — "08:00 / 13:00 / 18:00 PT summaries"
  - `Pod status changes` (OFF) — "SSH ready · idle · stopped · failed"
- [x] Each row: `onclick` toggle + `toast(...)` feedback, `swl-sub` description, `border-bottom` separators except last
- [x] Wires the Phase 25 `.switch-with-label` compound that was CSS-only with no HTML usage

### Phase 26 — Chat page audit: ChatInput calibration + AiState + ChatDivider (2026-04-10) ✅ COMPLETE

Figma calls: `get_metadata(833:15476)` Chat page — 5 frames: DEMO × 2, AI THINKING STATES × 2, CHAT MESSAGE, CHAT INPUT, CHAT DIVIDER.

**Specs extracted:**
- **ChatInput** (`4133:11200`): 716×128px total, 6 states (default/disabled/hover/active/filled/drag-drop). Textarea fills ~58px, actions bar ~70px.
- **AiState** (`4119:17980`): 113×16px, 3 states (default/disabled/active). Inline compact thinking indicator. 8 stacked instances in DEMO at 28px gaps.
- **ChatMessage** (`4119:17617`): 204×40px minimum per state. Multi-line messages expand above this.
- **ChatDivider** (`4119:17645`): 720×18px session separator.

**26A — ChatInput height calibration**
- [x] **`.chat-input`** — `min-height:72px → 58px` (default pill now ~128px total per spec)
- [x] **Comment** updated with spec note

**26B — AiState component CSS**
- [x] **`.ai-state`** — 16px height, `inline-flex;align-items:center;gap:6px`, Geist text-xs
- [x] **`.ais-dot`** — 6px circle, `text-dim` default, `accent + glow` when `.active`
- [x] **`.ai-state.active`** — sage dot + `ais-dots` 3-dot loading animation (reuses `ag-load-dot` keyframe)
- [x] **`.ai-state.disabled`** — opacity:.4
- [x] **`.chat-ai-state-row`** — full-width wrapper row, `min-height:20px`
- [x] **Wired** — `<div class="chat-ai-state-row"><span class="ai-state active">bigbounce-orch<dots></span>` inserted immediately before the orchestrator thinking block in chat body

**26C — ChatDivider component CSS**
- [x] **`.chat-divider`** — `flex;align-items:center;gap:10px;height:18px`, `::before/::after` rules create flanking `var(--border)` lines
- [x] **`.chat-divider-label`** — `label-mono / label-sm-size / text-dim / uppercase`
- [x] **Wired** — `<div class="chat-divider"><span class="chat-divider-label">Today · 08:42</span>` inserted after system message, before first user message

### Phase 25 — STYLE TESTER audit + sidebar spec corrections (2026-04-10) ✅ COMPLETE

Figma calls: `get_metadata(4145:17200)` STYLE TESTER (3 frames: color ramps, form showcase, chat/code showcase).

**25A — Sidebar spec corrections from STYLE TESTER - 2 (nav-logo / nav-footer / nav-link dimensions)**
- [x] **`.sb-brand`** — `height:54px → height:64px` (STYLE TESTER nav-logo 235×64px)
- [x] **`.sb-footer`** — `height:46px → height:66px` (STYLE TESTER nav-footer 235×66px)
- [x] **`.sb-item`** — `padding:7px 8px → padding:0 8px;min-height:31px` (STYLE TESTER nav-link 31-32px)
- [x] **Comment** updated: added `STYLE TESTER - 2: nav-link height 31-32px` note to nav-link CSS comment block

**25B — Switch with label compound CSS (STYLE TESTER - 3: Switch with label 37px)**
- [x] **`.switch-with-label`** — 37px `min-height`, `flex;align-items:center;gap:10px`. Label side: `flex:1;Geist/--text-xs/--lh-xs`. Switch sits right-aligned. `swl-sub` sub-label at 11px/text-muted.
- [x] **Status** — CSS added and ready. No HTML wiring yet (Notifications settings section doesn't exist; will wire when that section is built).

**25C — AGENTIC_UI_KIT_AUDIT.md page map corrections**
- [x] **Status header** — updated: "ALL 27 COMPONENTS EXTRACTED · MISC + TYPOGRAPHY confirmed · Phase 24 complete"
- [x] **MISC row** — `pending` → `✅ extracted — Phase 22: PULSATING-DOT · LOADING-DOTS · SKELETON shimmer`
- [x] **TYPOGRAPHY row** — `📋 tokens extracted, frames pending` → `✅ extracted — Phase 24: 7 CSS vars added to :root, wired to .tbl/.btn`

### Phase 24 — Typography CSS vars + token wiring (2026-04-10) ✅ COMPLETE

Figma calls: `get_metadata(2003:4067)` TYPOGRAPHY · `get_metadata(230:839)` PLAYGROUND (too large, skipped).

**24A — Typography CSS vars added to `:root` (AgenticUI TYPOGRAPHY 2003:4067)**
- [x] **`--text-xs:13px / --lh-xs:15px`** — SYSTEM/Body/xs · `body-text-style-1` height=15px confirmed
- [x] **`--text-sm:14px / --lh-sm:18px`** — SYSTEM/Body/sm
- [x] **`--text-md:16px / --lh-md:24px`** — SYSTEM/Body/md
- [x] **`--label-md-size:12px / --label-md-lh:18px / --label-md-track:0.3px`** — Label/md Departure Mono
- [x] **`--label-sm-size:10px / --label-sm-lh:18px / --label-sm-track:0px`** — Label/sm
- [x] **`--btn-md-size:13px / --btn-md-lh:15px`** — BUTTON/Label/md · height=15px confirmed
- [x] **`--btn-sm-size:10px / --btn-sm-lh:11px`** — BUTTON/Label/sm · height=11px confirmed

**24B — Token wiring into canonical classes**
- [x] **`.tbl thead th`** — `font-size:var(--label-sm-size);line-height:var(--label-sm-lh)` (was hardcoded `var(--label-sm-size)` duplicate)
- [x] **`.tbl tbody td`** — `font-size:var(--text-xs);line-height:var(--lh-xs)` (was `line-height:var(--lh-xs)` without the xs font-size token)
- [x] **`.btn`** — `font-size:var(--btn-md-size);line-height:var(--btn-md-lh)` (was `font-size:var(--btn-md-size)` with hardcoded `font-weight:500`)
- [x] **`.btn-sm`** — `font-size:var(--btn-sm-size);line-height:var(--btn-sm-lh)` (was `font-size:10px` hardcoded)

### Phase 22 — Table row heights + AgenticUI MISC components (2026-04-10) ✅ COMPLETE

Figma calls: `get_metadata(123:395)` Table page · `get_metadata(178:121)` MISC page.

**22A — Table component spec (AgenticUI 123:395)**
- [x] **`.tbl-wrap`** — added `box-shadow:var(--elev-2)` for proper AgenticUI card elevation
- [x] **`.tbl thead th`** — upgraded from `padding:8px 12px` → `height:40px;padding:0 12px;vertical-align:middle` (Figma header row = 40px)
- [x] **`.tbl tbody td`** — upgraded from `padding:8px 12px` → `height:64px;padding:0 12px;vertical-align:middle` (Figma data row = 64px). All experiments/surveys/papers tables now match AgenticUI spec.
- [x] **Comment block** added: `/* ══ TABLE — AgenticUI 123:395 · header 40px · data-row 64px · 10 cell-type spec ══ */`

**22B — PULSATING-DOT (AgenticUI MISC 4004:93)**
- [x] **`.ag-dot`** base class: `16×16px` circle, `border-radius:50%`
- [x] **`.ag-dot.low`** keyframe: `ag-pulse-low` — scale .72→.82, opacity .38→.55, 3s cycle (idle state)
- [x] **`.ag-dot.high`** keyframe: `ag-pulse-high` — scale 1→1.08, opacity .9→1, glow ring `0 0 0 4px rgba(95,184,138,0)`, 2.2s cycle (active state)
- [x] **Wired** — 7px `ag-dot.high` added to both live `run-exp-card` headers (EXP-054, EXP-055) alongside existing `run-exp-badge.running`
- [x] **Wired** — 8px `ag-dot.high` added to "Live experiments · 2 running" section count

**22C — LOADING-DOTS (AgenticUI MISC 4030:7034)**
- [x] **`.ag-loading-dots`** + `span` children: 4-dot stagger, `ag-load-dot` keyframe (scale .55→1, opacity .25→1), 1.4s cycle with 160ms stagger per dot
- [x] **`.ag-skeleton`** + size variants `.w-sm/.w-md/.w-lg`: shimmer animation `ag-shimmer` (200%→-200% gradient sweep, 1.8s), 14px height, cabinet-warm surface-3/surface-4 gradient

### Phase 21 — Marketing site light-first flip + accent reduction + desktop cream ✅ COMPLETE (2026-04-10)

Houston request: "remove the green accent keep it consistent with the cabinent cocao sage and the marketing site you should REALLY go heavey on reusing exactly the code from AGENTICUI DESIGN SYSTEM figma PLEASE PLEASE and don't forget to also make the desktop app consistent with the web app for v3 too"

**21A — Marketing site: Cabinet cream as CSS default (light-first flip)**
- [x] **`:root` flipped** — Cabinet cream is now the true default `:root`. Dark values moved to `:root.dark`. No more "inside-out" CSS.
- [x] **Theme toggle JS** — `_applyMktTheme()` now adds/removes `dark` class instead of `light`. Default is `||'light'` (no class = cream).
- [x] **`.topnav` base rule** — `rgba(250,246,241,0.92)` as default + `.dark .topnav{rgba(10,12,16,0.8)}`.
- [x] **Card covers use CSS vars** — `.lab-card-cover` and `.blog-card-cover` backgrounds changed from hardcoded `#0f1115` → `var(--surface)` so they auto-adapt between cream and dark.
- [x] **`.detail-cover` / `.blog-featured-cover`** — hardcoded dark backgrounds → `var(--surface)`.
- [x] **Hero/grid/shadows** — `.hero::before`, `.hero-grid`, `.demo-frame`, `.toast` shadows all use warm `rgba(59,47,47,...)` in cream; `.dark` overrides keep the dark values.
- [x] **`.hero-h1 .accent`** — uses `var(--accent-dim)` as cream default, `.dark` gets `var(--accent)`.

**21B — Marketing site: Accent reduction**
- [x] **`.eyebrow .dot`** — changed from `background:var(--accent);box-shadow:0 0 4px var(--accent)` to `background:var(--text-dim);opacity:.5`. Sage dots on every section header were excessive.
- [x] **`.em` in body sections** — 7 locations changed from `color:var(--accent)` → `color:var(--text-bright)` (often with `font-style:italic`): `.window-quote .em`, `.arb-tagline .em`, `.review-claim-text .em`, `.review-consensus-text .em`, `.sc-title .em`, `.showcase-foot-meta .em`, `.page-header h1 .em`.
- [x] **KEPT sage** — `h1.hero-h1 .accent` (THE hero moment), `.footer-cta h2 .em` (CTA conversion), `.article h1 .em` (article headlines). Sage is now earned.

**21C — AgenticUI navbar: Departure Mono applied**
- [x] **`.tn-link`** — upgraded from 13px default font to `font-family:'Departure Mono',var(--mono)`, `text-transform:uppercase`, `letter-spacing:.35px`, `font-size:11.5px`. Matches AgenticUI Navbar (230:699) spec directly.

**21D — Desktop app: Cabinet cream overhaul**
- [x] **`:root` vars** — full flip to Cabinet cream palette (`--bg:#fdfaf4`, `--surface-3:#eae2d0`, `--text:#5a4a3e`, etc.)
- [x] **Body background** — dark space radial → warm sand/parchment: `radial-gradient(ellipse at 40% 35%,#f0e8d5 0%,#ddd0b0 45%,#c8b88c 100%)`
- [x] **macOS menu bar** — `rgba(232,222,206,0.88)` frosted warm glass + `border-bottom: 1px solid rgba(90,74,62,0.15)` + `color:var(--text-bright)` for menu labels
- [x] **Window chrome** — `border:var(--border-strong)`, box-shadow uses warm `rgba(90,74,62,...)` tones + `inset 0 0 0 1px rgba(255,255,255,0.6)`
- [x] **Titlebar** — `linear-gradient(180deg,var(--surface-3),var(--surface-2))` + `border-bottom:var(--border-strong)`
- [x] **Dock** — `rgba(232,222,206,0.75)` frosted glass, warm border, warm box-shadow
- [x] **Notification** — `rgba(253,250,244,0.92)` frosted glass, warm shadows + all text colors via CSS vars
- [x] **Menu bar popover** — warm frosted `rgba(253,250,244,0.95)`, warm border/shadow
- [x] **Mockup controls** — warm frosted `rgba(253,250,244,0.92)`
- [x] **AgenticUI elevation vars** — all `rgba(0,0,0,...)` changed to `rgba(90,74,62,...)` warm brown shadows
- [x] **Annotations** — `box-shadow` changed to warm `rgba(90,74,62,0.14)`

### Phase 20 — Marketing site: "vs. alternatives" comparison (2026-04-10) ✅ COMPLETE

No Figma calls. 109 lines added to `v3/marketing-site-mockup.html` (5,553 → 5,662).

- [x] **"WHY NOT JUST USE X?" section** — added before footer-cta on the home page
- [x] **11-row comparison table** — Hubify Labs vs. k-dense.ai vs. feynman.is vs. Jupyter/Colab
  - Hubify ✓: multi-agent orchestration, cross-model review, GPU, publish loop, novelty scoring, 4-layer memory, public lab site, 3 IDEs, always-on orchestrator
  - k-dense ✓: 250+ datasets, skills catalog; ✗ everything agent-related
  - feynman.is ~: partial publish/skills/CLI; ✗ GPU, agents, memory
  - Jupyter/Colab ~: partial GPU (Colab); ✗ agents, memory, novelty, paper pipeline
- [x] **`.compare-alt` CSS modifier** — `td:not(:first-child)` center alignment via CSS (no inline text-align attrs)
- [x] **`.ct-no/.ct-us/.feat-us` classes** — dim ✗ for "not supported", sage ✓ for Hubify column data, highlighted Hubify header
- [x] **`.feat-us-col` on Hubify data cells** — subtle `var(--surface-2)` background to visually anchor the "us" column
- [x] **Comparison note footnote** — `compare-note` below table with legend + fairness caveat
- [x] **Inline style cleanup** — removed `display:inline` from span.compare-note (redundant, spans are inline by default)

### Phase 19 — In-app novelty scoring (experiments table) ✅ COMPLETE (2026-04-10)

No Figma calls. No new CSS needed — reuses `c-accent-bold`, `c-bright-600`, `c-text`, `dim`, `mono` classes already present.

- [x] **Novelty column added to experiments table** — 9-column header: ID / Experiment / Phase / Survey / Status / Runtime / Result / Novelty / [actions]. Novelty is sortable with `data-tip` explaining scoring methodology.
- [x] **All 10 experiment rows scored**:
  - EXP-051 Combined PTA Bayes: `9.2` (c-accent-bold · sage — novel multi-array Bayes, strong new result)
  - EXP-050 DESI×eROSITA 4.1σ: `8.7` (c-accent-bold · sage — novel cross-survey detection)
  - EXP-049 Bounce discrimination: `8.4` (c-bright-600 · 5 models, new framework)
  - EXP-047 eROSITA X-ray sweep: `7.8` (c-bright-600 · 73% novel anomalies)
  - EXP-053 QSO Classifier: `7.4` (c-bright-600 · solid but expected methodology)
  - EXP-048 SDSS DR18 QSO: `6.1` (c-text · substantial catalog, routine sweep)
  - EXP-052 Legacy DR10 cross-match: `4.1` (dim · routine catalog cross-match)
  - EXP-055 ACT retrain / EXP-054 Planck re-run / EXP-056 queued: `—` (dim · not scored yet)
- [x] **Experiments section header** — `avg novelty 7.4` clickable callout next to "53 total" (navigates to Contributions view for full breakdown)
- [x] **Scoring rationale** — high (≥8.5, sage): unexpected + paper-ready; mid-high (7–8.4, bright): solid new result; mid (5–7, text): expected outcome; low (<5, dim): QC/correction work

### Phase 18 — Marketing site: Pricing page ✅ COMPLETE (2026-04-10)

No Figma calls. 232 lines added to `v3/marketing-site-mockup.html`.

- [x] **`#mp-pricing` page** — full SaaS pricing page wired into nav + footer
- [x] **3 pricing tiers**: Free ($0 · 1 lab) · Pro ($49/mo, featured w/ "Most popular" pill) · Studio ($149/mo · 5 team seats)
- [x] **Plan cards** — CSS-only `::before` badge on `.plan-card.featured`, sage border highlight, check/X feature lists
- [x] **Credits explainer** — "What's a credit?" section with 3 real cost examples (MCMC ~800-2K, publish-ready loop ~5-15K, 24h monitoring ~200-500)
- [x] **Comparison table** — 13 rows × 3 tiers (labs, credits, pods, providers, paper pipeline, model training, team seats, API, novelty scoring, cross-model review, memory, support)
- [x] **FAQ** — 6 Q&As (labs definition, GPU credits, credit limits, cancellation, free forever, novelty scoring)
- [x] **Responsive** — collapses to 1-column at 900px
- [x] **Nav** — "Pricing" added between Labs and Docs
- [x] **Footer** — Pricing link added to Product column

### Phase 17 — Final utility sweep ✅ COMPLETE (2026-04-10)

No Figma calls. 406 → 336 inline styles (-70, combined 744→336 = -55% total).

- [x] **`.c-bright-600/.c-muted-10/.fs9-dim-mt2/.fs12-bright-500/.fs8-light`** — color+size combos × 4 each.
- [x] **`.dot-6-accent/.dot-5-accent/.dot-5-dim`** — inline status dot indicators × 4+3+3.
- [x] **`.col-end-4`** — flex column right-align gap:4px. `class="settings-row-value"` merge × 4.
- [x] **`.mono-10-dim-auto`** — mono metadata right-aligned × 4.
- [x] **`.desc-22`** — muted desc text padding-left:22px × 3.
- [x] **`.rt-action-row/.flex-wrap-8/.flex-1-min0`** — flex row utilities × 3 each.
- [x] **`.inline-code-chip`** — `<kbd>` keyboard shortcut chips × 3.
- [x] **`.js-fig-row/.js-tmpl-card`** — JS template card hover via CSS :hover, eliminates last 2 `onmouseover/onmouseout` JS handlers.
- [x] **`<b class="c-text">` sweep** — `<b style="color:var(--text)">` × 15 static HTML instances.
- [x] **`.sp-row .v.text` modifier** — `class="v" style="color:var(--text)"` → `class="v text"` × 14 (all in JS template strings).
- [x] **`.dim.fs8-light` / `.sp-pill.fs8-light` merges** — `font-size:8px` overrides on elements with existing class × 4+3.
- [x] **True practical floor at 336** — remaining: `display:none` (17, JS), SVG `color:var(--text-muted)` on viewBox icons (21), `cursor:pointer` SVG `<g>` (12), `cursor:default` (7), `border:none` form resets (7), SVG dimension attrs (11), single-prop margin spacings (~40). No clean batch wins remain.

### Phase 16 — Color/typography utility sweep ✅ COMPLETE (2026-04-10)

No Figma calls. 564 → 406 inline styles (-158, combined 744→406 = -45% total).

- [x] **`.c-text/.c-bright/.c-dim/.c-muted`** — single-prop color utilities. 15+35+18 standalone `<span>` tags replaced.
- [x] **`.c-dim-xs`** — `color:var(--text-dim);font-size:9px` × 20 standalone.
- [x] **`.meta-mono-sm`** — `color:var(--text-dim);font-family:var(--mono);font-size:10px;font-weight:400` × 16 — metadata labels.
- [x] **`.meta-mono-xs`** — 9px dim mono, two property-order variants merged into one class × 17.
- [x] **`.c-accent-bold`** — `color:var(--accent);font-weight:600` × 12.
- [x] **`.c-text-bold`** — `color:var(--text);font-weight:600` × 5.
- [x] **`.col-end`** — `display:flex;flex-direction:column;align-items:flex-end;gap:2px` × 8.
- [x] **`.section-sep`** — `margin-top:14px;padding-top:14px;border-top:1px solid var(--border)` × 8.
- [x] **`.sp-group-head`** — settings section group header (label-mono 9px uppercase) × 6.
- [x] **`.sp-narrow-input/.sp-full-input`** — settings panel input field styles × 6 + 4.
- [x] **`.mono-10`** — `font-family:var(--mono);font-size:10px` × 8.
- [x] **`.para-11`** — `font-size:11px;margin-bottom:9px;text-align:justify` × 7 (paper abstract paragraphs).
- [x] **`.row-8/.row-end-6`** — flex row utilities × 5+5.
- [x] **`sp-pill good` font-size:9px removed** × 8 — redundant with `.sp-pill{font-size:9px}` already in CSS.
- [x] **Practical floor reached** — remaining 406: display:none (17, JS-controlled), cursor:pointer (12, SVG `<g>`), cursor:default (7), border:none (7), single-prop spacings (margin-top/left variants), SVG color attrs with viewBox between class+style (complex merge). No more clean batch wins.

### Phase 15 — Utility class sweep ✅ COMPLETE (2026-04-10)

No Figma calls. Largest inline-style reduction pass: 744 → 564 (180 removed).

- [x] **`.cp`** — `cursor:pointer` utility. Merged into: `class="sp-row cp"` (64), `settings-row cp` (4), `rt-info-row cp` (4), `chat-header-title cp` (1). Removed from `<a class="sp-pill">` (redundant on anchors). SVG `<g>` instances left.
- [x] **`.c-accent` / `.c-warn`** — single-property color utilities. Replaced 81 `<span>` + 5 `<b>` with accent, 4+4 with warn.
- [x] **Removed 77 redundant `style="text-align:left;flex:1"`** from `.v` elements inside `.sp-row` — already defined in `.sp-row .v{flex:1}` CSS.
- [x] **`.settings-link-row` + 4 sub-classes** — canonical nav-link card system. 16 rows × 5 inline styles = 80 attrs removed. Also eliminated 16 pairs of inline `onmouseover/onmouseout` JS hover handlers (CSS `:hover` handles it).
- [x] **`.settings-nav-card`** — variant for features nav (Skills/Workflows/Databases/Formats). 4 rows × 5 attrs = 20 attrs removed + 4 JS handler pairs.

### Phase 14 — `<pre>` block canonicalization ✅ COMPLETE (2026-04-10)

No Figma calls. Final inline style sweep for pre/code display blocks.

- [x] **`.log-pre` class** — canonical terminal/log output: `bg-primary`, `1px border`, `r-sm`, `10px 12px padding`, `mono 10px`, `text-muted`, `1.55 line-height`, `overflow-x:auto`. Applied to 4 log pre blocks (2 with max-height inline override, 1 with r-md override, 1 exact match).
- [x] **`.code-pre` class** — canonical code/content display: `bg-primary`, `1px border`, `r-md`, `14px padding`, `mono 11px`, `text color`, `1.6 line-height`, `overflow-x:auto`. Applied to 5 static HTML `<pre>` elements (2 with `border-color:var(--border-bright)` override) and 3 JS template string `<pre>` elements (with padding/white-space minimal overrides).
- [x] **Remaining** — 1 bare raw-md `<pre style="font-size:11px">` intentionally left (no border/padding, unique context — override list would exceed the boilerplate it replaces).

### Phase 6 — Remaining component passes (2026-04-09 iteration)
- [x] **Navbar/sidebar nav-link** — Figma node 230:699 — Departure Mono 13px uppercase 0-track, `padding:7px 8px`, `margin:0 6px`, `border-radius:8px`, hover `background:surface-2`, sub-link border-left track, active rail at `left:-6px`
- [x] **Table** — header: Departure Mono 10px 0.3px tracking; body: Geist 13px (from 12px)
- [x] **Menu/dropdown** — node 558:659 — r-xl container, 0.5px border/subtle, elev-2, Geist 14px items (40px), sm 13px (24px), Departure Mono kbd chips -0.3px track. `.dropdown-menu`, `.dropdown-item`, `.dropdown-item-sm`, `.dropdown-divider` canonical classes added. `.lab-dropdown` + `.chat-pos-dd` upgraded (r-xl, 0.5px border). Removed from elev-4 group (now correct elev-2).
- [x] **Avatar** — node 179:17313 — `.avatar` base class, 6 sizes (sm-2xl), 3 types (photo/initials/agent). `.avatar-agent` = sage tint (accent-bg/accent). `.sb-avatar` upgraded to label-mono + sage. `.chat-msg-avatar` wired to all 5+ chat messages. All sidebar/profile popout dropdowns upgraded to r-xl + 0.5px border.
- [x] **Loader** — nodes 678:1996 / 683:2107 — `.loader-dots` 3×3 marching-squares animation (no spinner, per rule). 8-step clockwise perimeter march, center stays dim. Wired to backup row in Director view.

## 7. Memory touchpoints (read these alongside this file)

- `feedback_hubify_labs_design.md` — single sage accent, Cursor-style sophistication
- `feedback_sidepeek_philosophy.md` — NO sidepeeks for core pages
- `feedback_no_modals_sidepeek.md` — no modals, sidepeek pattern (ephemeral only)
- `feedback_cabinet_*` / `CABINET_AUDIT.md` — the light mode origin work
- `feedback_surfaces_vs_get.md` — Web/Desktop/CLI are equivalent IDEs
- `feedback_green_reduction.md` — sage should be rare
- `feedback_minimalism_philosophy.md` — Cursor-style calm, breathing room
- `feedback_chat_thinking_style.md` — pulsing asterisk, no spinners
- `project_hubify_labs_compute.md` — RunPod first, Modal coming soon
- `feedback_memory_system.md` — 4-layer memory (user/agent/lab/global)

## 8. Current cron state (session-only)

- `0b85b094` — 15m pod check (H200 `root@205.196.19.52 -p 11452`), recurring
- Previous polish loop cron was killed; all polish-loop work is redirected to the Phase 1-5 sequence above.

## 9. Recovery instructions after compaction

1. Read this file first.
2. Read `MEMORY.md` in the memory folder for the feedback touchpoints.
3. Check `~/.gstack/projects/$SLUG/timeline.jsonl` for last-session state.
4. DO NOT call Figma MCP until you confirm Phase 0 is unblocked.
5. If Phase 0 is still blocked, ask Houston — don't burn more quota guessing.
6. Preserve `index-v2-sage.html.bak` as the golden snapshot. Never delete.
7. All AgenticUI work goes into `index.html` (v3 target), merge, don't rewrite.
