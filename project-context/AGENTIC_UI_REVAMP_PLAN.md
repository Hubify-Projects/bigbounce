# AgenticUI Revamp Plan — Canonical

**Created:** 2026-04-09 (post-compaction recovery save)
**Status:** Phase 3 component merge COMPLETE (2026-04-10). All 9 AgenticUI components extracted + CSS applied to index.html: Text Input · Badge · Toast · Menu · Button · Search Input · Dropdown · Tooltip · Progress. Phase 4 next: wire new CSS classes into actual HTML markup (replace ad-hoc inline styles with canonical classes), then Phase 5 surface parity (marketing-site, desktop, cli-tui where applicable).
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
