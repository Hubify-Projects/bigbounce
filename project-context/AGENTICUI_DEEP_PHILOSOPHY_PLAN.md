# AgenticUI Deep Design Philosophy Plan

**Created:** 2026-04-09
**Owner:** Houston + Claude
**Purpose:** Supersedes the component-level Phase 8 plan. This is the architectural redesign plan — workspace shell, data hierarchy, interaction philosophy, and design system discipline — derived from deep Figma extraction.

---

## What we've been doing wrong

Phase 3–8 applied AgenticUI components **on top of** our existing structure. We changed button radii, added pagination, swapped stepper pills. But the SHELL — how the workspace is laid out, how panels relate, how information hierarchy works — is still v2-era. Houston is right that the changes look minor. They ARE minor. The Figma is telling us to go deeper.

---

## What AgenticUI actually teaches (design philosophy layer)

### 1. Chat is the primary surface — everything else is context

From Figma node `4127:18971` (Chat Input):
- The input box is **128px tall** with `border-radius: 20px` — it's a SOFT, WELCOMING pill, not a tight input bar
- Left button: attachment (contextual actions)
- Right buttons: voice → send. When text is filled, the **send button becomes a solid black 40px circle** — the darkest element on screen
- Drag-and-drop: the input becomes a `dashed 1px border` drop zone — showing file upload is native to the conversation
- The overall container sits on `--surface-secondary (#f7f7f7)` background with `elevation-4` — it floats above the page

**Implication for us:** Our chat input bar is narrow, cramped, and uses a simple textarea. It should be the most premium-feeling element in the entire app. When you're talking to the orchestrator, it should feel like commanding a research facility.

### 2. The icon system is a coherent language — not decorative

From the Figma icons page (`179:868` — 4080×5354px frame with hundreds of icons):
- All icons are 16px or 20px, consistent weight (~1.5px stroke)
- Naming: `Icons/Magic-wand--filled`, `Icons/Chevron--left`, `Icons/Add` — functional, descriptive
- Icon buttons are always 40×40px circle for primary, 24–32px for toolbar
- **No emojis ever** — every visual affordance is an SVG icon

**Implication for us:** Our sidebar has mixed icon sizes and some emoji-style characters. We should audit every icon and ensure uniform 16px/20px sizing in consistent 40px touch targets.

### 3. Elevation system creates spatial depth — use it deliberately

From all extracted components:
- `elevation-1`: 1px border + 1pt shadow (surface, cards)
- `elevation-2`: 3-layer shadow, mid-range (modals, popovers)
- `elevation-3`: 6-layer shadow (dropdowns, menus)
- `elevation-4`: heavy 6-layer + spread shadow (command palette, chat input)

**Implication for us:** The chat input needs `elevation-4`. The command palette (cmdK) needs `elevation-4`. Cards need `elevation-1`. Right now we're using box-shadow inconsistently.

### 4. Typography is a HIERARCHY SYSTEM, not just a font choice

4 fonts, 4 distinct roles:
- **Geist** (16px regular): conversational body text, chat messages, descriptions
- **Departure Mono Semibold** (10–13px uppercase): labels, tabs, categories, pills — the "data layer"
- **JetBrains Mono**: code only, never for UI text
- **New York Large** (headings): section titles, page headers (we've been avoiding this — should use it sparingly)

The key insight: **Departure Mono is the visual glue of the information layer**. Every meta-label, every status, every category uses it. It's how you distinguish "data about data" from "the data itself."

**Implication for us:** We need a consistent audit — every `font-family:var(--label-mono)` should be used for ALL metadata labels. Geist for human-readable content. Never mix them in the same row.

### 5. Color discipline = only status deserves color

From the AgenticUI token system:
- **Neutral 100–900**: the entire UI lives here
- **Green accent**: success state, active indicators, primary action
- **Red**: destructive, error states
- **Orange/yellow**: warning
- **Blue**: info, links (AgenticUI default — we replace with sage)

The Figma never uses color for decoration. Color = information. If something is green, it's passing. If something is neutral, it's background.

**Implication for us:** Survey cells, pipeline steps, experiment statuses — some use sage for decoration, not information. Audit every use of `--accent` and ask: does this color MEAN something?

### 6. Interaction model: every element earns its state

AgenticUI uses 5 states consistently: `default | hover | focus | active | disabled`
- Default: minimal, calm. No box-shadow, no border-color change
- Hover: `border-medium` (0.5px → 1px or color change), subtle bg shift
- Focus: ring (2px, offset 1px)
- Active: inverted or elevated
- Disabled: 40% opacity, cursor:not-allowed

**Implication for us:** Our hover states are inconsistent. Some cards have hover, some don't. Some buttons have focus rings, others don't. Need a single interaction pattern applied everywhere.

### 7. Data layout philosophy: show hierarchy, not lists

The AgenticUI workspace design (from PLAYGROUND page context + component structure) reveals:
- **Tables**: not for displaying data — for comparing data. Every table needs sort, filter, search, pagination
- **Cards**: for entities (experiments, papers). Card = identity + status + quick action
- **Lists**: for sequential items (pipelines, steps). Use Stepper, not grid
- **Stat blocks**: for numbers at a glance. Always pairing a number with a label and a trend

**Implication for us:** The overview view shows stats + surveys + a live section. The surveys section is a grid of small cells. It should be a TABLE with sortable columns (Survey, Anomalies, %, Status, Last run). The experiments table is correct already — paginated, sortable. The pipeline view using Stepper is now correct.

---

## Phase 9 — Workspace Shell Redesign (the real work)

### 9.1 Chat input upgrade (CRITICAL — most visible change)

Current: `<textarea>` with a narrow bar at bottom, `border-radius: --r-xl (12px)`
Target: Full AgenticUI spec — `border-radius: 20px`, 128px min-height, left attachment button, right voice + send (send becomes solid black filled circle when text present)

CSS changes:
```css
.chat-input-box {
  border-radius: 20px;  /* was: var(--r-xl, 12px) */
  min-height: 96px;
  padding: 12px;
  box-shadow: var(--elev-2);
  border: 0.5px solid var(--border);
  background: var(--bg);
}
.chat-send-btn {
  width: 40px; height: 40px;
  border-radius: 50%;
  background: var(--text-bright);  /* black on light, white on dark */
  color: var(--bg);
}
.chat-send-btn.has-text { opacity: 1; }
.chat-send-btn:not(.has-text) { background: var(--surface-3); opacity: 0.5; }
```

### 9.2 Survey grid → proper Table

Current: `.survey-grid` with small cells (name, number, status)
Target: Full table with columns: Survey | Source Count | Anomalies | Rate | QC Status | Last Run

This transforms the overview from "decorative grid" to "actionable data view."

### 9.3 Section headers — consistent title + subtitle + actions pattern

Every view needs:
```
[section title] [section subtitle/count]                    [action buttons]
─────────────────────────────────────────────────────────
[content]
```

Currently inconsistent across views. Need a single `.view-header` pattern everywhere.

### 9.4 Command palette upgrade

The cmdK popup currently uses basic styling. AgenticUI cmdK (from button/keyboard shortcut component) should have:
- `elevation-4` shadow (the heaviest)
- 20px border-radius (matching the chat input)
- Departure Mono keyboard shortcut chips
- Category headers (Experiments / Papers / Agents / Settings / Actions)
- Keyboard shortcut display in every item

### 9.5 File upload as first-class

AgenticUI node `4028:6200` — file upload is a proper drag-drop zone. Our dispatch form has a text input for experiment name. It should also allow dropping notebooks, scripts, config files directly.

### 9.6 Text input upgrade (all inputs in the UI)

Current inputs: basic border + background
AgenticUI Text Input spec (node `761:20738`):
- 40px height
- `0.5px border`
- `r-md (8px)` border-radius (not 5px)
- Focus: border changes to `--border-strong`, 2px ring
- Helper text below every input
- Labels always in Departure Mono uppercase 10px

### 9.7 Modal → Command palette pattern

AgenticUI has a Modal component (`4092:1582`) but their philosophy strongly prefers the command palette (cmdK) pattern for system-level actions and right-panel slides for entity detail. We've already adopted "no modals," but the cmdK needs to be richer.

---

## Priority queue for Phase 9

1. **Chat input pill upgrade** — most visible, implements the #1 AgenticUI philosophy point
2. **Survey grid → table** — transforms the overview from decorative to functional
3. **All text inputs → AgenticUI spec** — uniform 40px height, r-md, focus ring, helper text
4. **Section headers — consistent pattern** — applies to all 10 views
5. **cmdK elevation-4 + keyboard chips** — makes the command palette feel like a premium tool
6. **Stat cards → card system** — upgrade the overview stat cards to full AgenticUI card spec
7. **View header breadcrumbs** — proj-scope bar already exists, needs .breadcrumb class applied
8. **File upload zone in dispatch form** — drag-drop script/config files
9. **Icon audit** — all sidebar icons at 16px, all toolbar icons at 20px, all touch targets 40px
10. **Interaction states audit** — hover, focus, active, disabled consistent everywhere

---

## Design tokens still missing from our implementation

From audit (not yet in our CSS):
- `--r-20: 20px` — for chat input specifically
- `font-size: 16px` for Geist body (we use 12.5–14px in chat — too small)
- `line-height: 24px` for Geist body (we use 1.7)
- `--input-height: 40px` — standard input height
- `--btn-icon-sm: 32px`, `--btn-icon-md: 40px` — icon button sizes
- `--focus-ring: 0 0 0 2px rgba(0,0,0,0.08)` — focus state ring

---

## Architecture decisions from AgenticUI philosophy

1. **Never display more than 10 items without pagination** — enforced
2. **Every data view is a table, not a grid** — survey grid → table
3. **Every entity has a card, not a row** — experiments could have a card view toggle
4. **Agent activity is always visible** — the "Live experiments" skeleton section is RIGHT — expand it
5. **Status = color, everything else = neutral** — strict color discipline
6. **Chat is always reachable** — dock philosophy (left/right/bottom) we have is correct
7. **Forms have helper text** — every input tells you what it's for and validates inline

---

## Node IDs for remaining Figma extraction (future sessions)

| Component | Node ID | Why |
|---|---|---|
| Text Input full spec | `761:20738` | All form inputs need this spec |
| Modal (for reference) | `4092:1582` | Even though we avoid modals, reference for cmdK panel |
| Icons page sample | `179:868` | Pick 10 icons to replace current SVG icons |
| Tabs full spec | `4056:1314` | Already implemented but need hover/active states |
| File upload | `4028:6200` | Dispatch form drag-drop |
| PULSATING-DOT | `4004:93` | Replace current thinking orb |
| Text Area | `4092:1380` | Multi-line dispatch field |

---

## North star: what Phase 9 completion looks like

Open the file. The FIRST thing you see (light mode default):
- Clean white sidebar with icon-only collapsed rail
- A full-width content area with proper section headers
- Bottom-docked chat area with a 20px-radius pill input, soft shadow, black send button
- The orchestrator's thinking shown with dots/asterisk, NOT a spinner
- Every table row has zebra subtle hover, sortable columns, row actions on hover
- Every status badge is color-coded (sage=pass, red=fail, orange=warn, neutral=queue)
- Every form input is 40px tall with Departure Mono labels and helper text

That's the target. Everything else follows.
