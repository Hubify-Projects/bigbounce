# Hubify Labs — Design System & Brand

**Version:** 1.0 | **Date:** 2026-04-07
**Companion to:** `HUBIFY_LABS_PRD.md`, `HUBIFY_LABS_UI_SPEC.md`

---

## 1. Design Philosophy

**Black, white, grayscale. Monospace for everything that matters. Cursor IDE meets Bloomberg Terminal meets v0.app.**

The interface is a research IDE. The user is a director, not a clicker. Every pixel earns its place. Color is a tool, not decoration.

### Reference Aesthetic
- **Cursor IDE** — left sidebar with file tree, center editor, right AI chat panel. All grayscale. Minimal chrome.
- **v0.app** — center content + live preview, monospace everywhere, terminal feel
- **Linear** — sophisticated dark mode, restrained color, perfect typography
- **Vercel dashboard** — quiet, data-dense, no decoration
- **Bloomberg Terminal** — keyboard-driven, data over chrome

### Anti-references
- Notion (too playful, too colorful)
- Vercel marketing site (too "designed")
- Any SaaS dashboard with rounded cards and gradients
- Anything using emoji as icons

---

## 2. Color Palette

### Backgrounds (5 levels of gray)
```css
--bg:        #0a0a0a;  /* Pure black-ish base */
--surface:   #0f0f0f;  /* Sidebar, panels */
--surface-2: #161616;  /* Card backgrounds */
--surface-3: #1c1c1c;  /* Hover states */
--surface-4: #232323;  /* Active states, inputs */
```

### Borders (3 levels)
```css
--border:        #1f1f1f;  /* Default panel borders */
--border-strong: #2a2a2a;  /* Hover, focus borders */
--border-bright: #3a3a3a;  /* Active borders */
```

### Text (4 levels)
```css
--text-bright: #fafafa;  /* Primary text, headings, key data */
--text:        #c5c5c5;  /* Body text */
--text-muted:  #707070;  /* Secondary text, labels */
--text-dim:    #404040;  /* Tertiary text, placeholders */
```

### Accent (use SPARINGLY)
```css
--accent:      #ffffff;  /* Primary action — pure white on dark */
--accent-soft: #2a2a2a;  /* Selected backgrounds */
```

### Status colors (only for status indicators, NEVER decoration)
```css
--green:    #4ade80;  /* Success, complete, connected, active */
--green-bg: #0d2818;
--amber:    #f59e0b;  /* Warning, queued, attention */
--amber-bg: #2a1f0a;
--red:      #ef4444;  /* Error, failed, critical */
--red-bg:   #2a0f0f;
```

**Rule:** No blue. No purple. No teal. Status colors only on dots, pills, and badges. The rest of the UI is pure grayscale.

---

## 3. Typography

### Fonts
```css
--mono:  'JetBrains Mono', 'SF Mono', Menlo, monospace;  /* Primary — code, data, IDs, monospace UI */
--sans:  'Inter', -apple-system, sans-serif;             /* UI labels, headings */
--serif: 'Newsreader', Georgia, serif;                   /* Paper content ONLY */
```

### Scale (compact, dense)
```
10px - micro labels (uppercase, letterspaced)
11px - secondary metadata, timestamps
12px - default UI text
13px - body text, primary content
14px - subheadings
16px - section headings
20px - page headings
28px - hero headings (Director greeting)
```

### Weights
```
300 - thin (rare, large display only)
400 - regular (default body)
500 - medium (emphasized text, links)
600 - semibold (headings, important data)
700 - bold (rare, only for very strong emphasis)
```

### Letter spacing
```
default - 0
labels  - 0.06em (uppercase)
brand   - 0.02em
mono    - 0
```

---

## 4. Layout Architecture

### 4.0 Layout Flexibility Rules

The default layout is sidebar + chat (left) + preview (right). **The chat panel is repositionable** by the user via 4 modes:

1. **Left** (default) — `[sidebar][chat][preview]`
2. **Right** — `[sidebar][preview][chat]`
3. **Bottom** (stacked) — `[sidebar][preview]` with `[chat]` docked below the preview, like Cursor's integrated terminal
4. **Hidden** — fully collapsed, with a small floating tab on the edge to bring it back

**Required UI controls** (all must actually work — no dead clicks):
- Position dropdown in the chat header with mini-preview icons of each layout
- Floating "show chat" tab when hidden, on the appropriate edge
- Keyboard shortcuts: `⌘1` left, `⌘2` right, `⌘3` bottom, `⌘J` toggle hidden
- Settings page exposes "default chat position" as a saved user preference

**Audit rule:** every icon click in the UI must DO something. Tooltips alone are not enough. If an icon has no real handler, either remove it or wire it up. Houston has explicitly called out dead-click icons as a regression.

### The Three Panels (Cursor model)

```
+----------------------------------------------------------+
|  TOP BAR (44px)                                           |
|  [Lab▾]  bigbounce › director         [⌘P] [⚙] [👤]      |
+--------+--------------------------------+----------------+
|        |                                |                 |
|  LEFT  |                                |   RIGHT         |
|  NAV   |       MAIN CONTENT             |   AGENT CHAT    |
|  220px |       (the active view)        |   380px         |
|        |                                |   (collapsible) |
|  Views |                                |                 |
|   ─    |                                |   Terminal +    |
|  Files |                                |   chat with     |
|        |                                |   orchestrator  |
|        |                                |                 |
+--------+--------------------------------+----------------+
|  STATUS BAR (24px)                                        |
+----------------------------------------------------------+
```

### Panel Specs

| Panel | Width | Resizable | Collapsible | Purpose |
|-------|-------|-----------|-------------|---------|
| **Top bar** | full × 44px | no | no | Lab selector + breadcrumb + global actions |
| **Left nav** | 220px (default) | yes | yes (Cmd+B) | Views list + file tree |
| **Main content** | flex | n/a | no | Active view content |
| **Right chat** | 380px (default) | yes | yes (Cmd+J) | Chat with orchestrator |
| **Status bar** | full × 24px | no | no | Keyboard hints + breadcrumbs |

**No icon rail.** The left nav IS the navigation, with text labels and tree structure (like Cursor's file explorer + outline).

---

## 5. Component Inventory

### Top Bar Components
- **Brand mark** — `hubify.labs` in monospace, top-left
- **Lab selector** — dropdown showing current lab, click to switch
- **Breadcrumb** — `lab › section › subsection`
- **Search trigger** — opens command palette (Cmd+P)
- **Notifications** — bell icon with badge
- **Settings** — gear icon
- **Profile** — avatar circle

### Left Nav Components
- **Section headers** — uppercase 10px gray labels (RESEARCH, MANAGE, SYSTEM)
- **Nav items** — icon (16px Lucide) + label + optional badge + optional shortcut
- **Active state** — `surface-3` background, `text-bright` text, no left border accent
- **File tree** — collapsible folder structure below nav items
- **Footer** — connection status with green pulse

### Main Content Components
- **View header** — title + subtitle + actions row
- **Section labels** — small uppercase gray
- **Stat cards** — `surface` bg, 1px border, value + label + sub
- **Data tables** — sticky header, hoverable rows, monospace numerics
- **Cards** — bordered containers with header + body
- **Status pills** — uppercase, monospace, color by status
- **Progress bars** — 4px tall, accent color
- **Empty states** — centered icon + text, no decoration

### Right Chat Components
- **Lab indicator pill** — top of panel, shows active lab with green dot
- **Agent role tag** — current orchestrator/lead/worker name
- **Message thread** — author + timestamp + body, role-colored author names
- **Multi-line input** — bordered textarea, syntax hints below
- **Slash command popup** — appears on `/` keystroke
- **@ mention popup** — appears on `@` keystroke
- **# experiment popup** — appears on `#` keystroke

### Modal Components
- **Command palette** — center modal, search + results list, Cmd+P
- **Lightbox** — full-screen image viewer, prev/next nav
- **Slide panel** — right-side detail panel for drilldowns

---

## 6. Icon System

**No emoji. No emoji. NO EMOJI.**

Use **Lucide icons** (or hand-rolled SVG in the same style):
- 14px default for inline
- 16px for nav items
- 20px for section headers
- 1.75px stroke width
- Stroke only, no fill
- `currentColor` for theming

Common icons needed:
- `home`, `layout-dashboard`, `flask-conical`, `git-branch`, `file-text`, `image`, `database`, `book-open`, `users`, `message-square`, `kanban`, `lightbulb`, `dollar-sign`, `bell`, `settings`, `search`, `command`, `terminal`, `folder`, `file`, `chevron-right`, `chevron-down`, `plus`, `x`, `check`, `circle`, `dot`

---

## 7. Spacing Scale

```
2px  - tight gaps
4px  - inline gaps
6px  - small gaps
8px  - default gap
10px - medium gap
12px - section gaps
14px - card padding
16px - default padding
20px - section spacing
24px - large spacing
32px - view padding
48px - hero spacing
```

**Default padding:** 14px for cards, 16px for sections, 24px for views.

---

## 8. Border Radius

Be conservative — small radius, sharp edges feel premium.

```
3px - inputs, small chips
4px - buttons, small cards
6px - cards, panels (default)
8px - modals, large cards
10px - command palette, dialogs
```

**No fully rounded buttons. No pill buttons except status badges.**

---

## 9. Animation & Motion

- **150ms** for hover transitions
- **200ms** for view switches
- **300ms** for panel collapse/expand
- **Easing:** `cubic-bezier(0.16, 1, 0.3, 1)` (quick start, smooth end)
- **No bouncing.** No spring physics. Snappy and direct.
- **`prefers-reduced-motion`** disables all animations

### 9.1 Loading & Thinking — Claude Code CLI style ONLY

**HARD RULE: NEVER use loading spinners.** No `border-radius: 50%; animation: spin`. No `<svg class="spinner">`. No `Loading...` text. No "circle-of-dots-going-around". The platform uses Claude Code's CLI thinking pattern instead.

**The thinking block component** (the only allowed in-progress indicator in chat surfaces):

```
✽ Channelling… (3m 12s · ↓ 4.8k tokens · thought for 11s)
  ⎿  ▣ Active task description
     ◻ Pending task description
     ✔ Completed task description
     ✔ Another completed task
      … +3 deferred
```

**Required components:**

1. **Cosmic orb** (NOT a static asterisk) — a small 14×14px CSS animation that **rotates through 6+ visually distinct modes every 22-28 seconds** for variety and visual joy. Each mode is a custom CSS animation, all monochrome with the sage accent for active highlights:

   - **Saturn** — pulsing core dot + 2 counter-rotating elliptical rings (default — abstract alive Saturn vibe)
   - **Radar pulse** — concentric expanding rings, sonar ping
   - **Orbit** — central dot with a smaller satellite orbiting it
   - **Twinkle** — 4-pointed star with rotating arms (cosmic / star)
   - **Beaker** — vertical bubbling motion (science / chemistry vibe)
   - **Grid** — 3×3 pixelated cells lighting up in sequence (bit-art / data viz vibe)
   - More modes welcome: smile-nerd-face, satellite, telescope, atom, DNA helix, etc.

   Mode rotation is JS-driven via `rotateOrb()` swapping the parent class. Random jitter on the timer (24-30s window) so the cycle feels organic, not metronomic. **NEVER show the same mode forever** — variety is the entire point.

   **NEVER use:** a static asterisk `✽`, a generic CSS spinner, a bouncing dots loader, or anything you'd find in Bootstrap.

2. **Active verb that ROTATES every ~7 seconds** — NEVER static, NEVER plain "Thinking...". The verb is picked from one of two pools:

   **Contextual pool** (preferred when the orchestrator knows what it's doing):
   ```js
   routing:       ['Routing peer reviews…','Dispatching reviewers…','Sorting the mail…']
   reading:       ['Inhaling Paper 1…','Devouring papers…','Mining citations…']
   writing:       ['Inscribing…','Quill-scratching…','Penning revisions…']
   searching:     ['Spelunking arXiv…','Combing ADS…','Beachcombing for prior art…']
   experimenting: ['Igniting EXP-054…','Firing up the H200…','Provoking the data…']
   verifying:     ['Triangulating sources…','Sniff-testing claims…','Bringing the receipts…']
   reviewing:     ['Squinting skeptically…','Devil\'s-advocating…','Picking nits lovingly…']
   computing:     ['Crunching…','Number-wrangling…','Matrix-multiplying…','Convolving…']
   thinking:      ['Pondering deeply…','Cogitating quietly…','Mulling it over…','Ruminating cosmically…']
   ```

   **Witty/cute/nerdy fallback pool** (~50 phrases when no context):
   ```
   Channelling… Cultivating… Galivanting… Choreographing… Conjuring…
   Caffeinating… Triangulating… Percolating… Effervescing… Marinating…
   Synthesizing… Spelunking… Tessellating… Pondering… Hypothesizing…
   Calibrating… Telegraphing… Whittling… Cogitating… Cross-pollinating…
   Crystalizing… Effulging… Gestating… Imbibing… Mulling… Pirouetting…
   Quibbling… Rummaging… Smelting… Untangling… Beguiling… Concocting…
   Distilling… Ferreting… Hobnobbing… Incanting… Loitering productively…
   Noodling… Orchestrating… Plotting… Rifling stacks… Stirring the pot…
   Tinkering… Unspooling… Wrangling… Yarn-spinning… Zigzagging…
   Bamboozling… Cavorting… Dithering brilliantly…
   ```

   Routing: 60% chance contextual, 40% chance random pool — so users see both. Always present participle ending in `…` (not `...`).

   **NEVER:** "Thinking…", "Loading…", "Please wait…", "Processing…", "Working on it…". Generic verbs are forbidden.

3. **SUBTLE text shimmer on the verb only** — Cursor-style horizontal light sweep. **Houston explicitly said "less bright and less fast"** — do NOT crank these values back up:
   - Base: `var(--text-muted)` (#6a6a6a)
   - Peak: `var(--text)` (#aeaeae) — NOT `--text-bright` (too bright)
   - Cycle: 5.6s linear infinite — NOT 3.2s
   - Gradient peak width: tight (50%±8%) so the sweep is barely there

```css
.thinking-verb {
  background: linear-gradient(90deg,
    var(--text-muted) 0%, var(--text-muted) 42%,
    var(--text) 50%,
    var(--text-muted) 58%, var(--text-muted) 100%);
  background-size: 240% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: thinking-shimmer 5.6s linear infinite;
}
@keyframes thinking-shimmer {
  0%   { background-position: 240% 0; }
  100% { background-position: -240% 0; }
}
```

4. **Time + tokens + thought time** — `(3m 12s · ↓ 4.8k tokens · thought for 11s)` separated by middot, monospace, dimmer than the verb (`var(--text-dim)`).

5. **Box-drawing tree** — `⎿` for the indented children branch, exactly like Claude Code uses. Aligned with `display: grid; grid-template-columns: 14px 1fr`.

6. **Status glyphs:**
   - `◻` empty box for pending
   - `▣` filled box for in_progress
   - `✔` heavy check for completed (color: `--accent` sage green)
   - `✗` for failed/blocked (color: `--crit`)
   - `… +N completed` or `… +N deferred` for truncation footer

### 9.2 Custom braille loading (when an asterisk isn't enough)

If a non-chat surface needs a tiny loading indicator (e.g., file save, table refresh), use a custom braille animation. NEVER a generic spinner.

```css
.braille::after {
  content: '⠋';
  animation: braille-frames 1.1s steps(1, end) infinite;
}
@keyframes braille-frames {
  0%   { content: '⠋'; }
  11%  { content: '⠙'; }
  22%  { content: '⠹'; }
  33%  { content: '⠸'; }
  44%  { content: '⠼'; }
  55%  { content: '⠴'; }
  66%  { content: '⠦'; }
  77%  { content: '⠧'; }
  88%  { content: '⠇'; }
  100% { content: '⠏'; }
}
```

### 9.3 Streaming text chunks

Chat messages stream in like Claude Code — character-by-character or chunk-by-chunk, with a blinking caret at the end of the current incomplete line:

```css
.stream-cursor {
  display: inline-block;
  width: 6px;
  height: 13px;
  background: var(--text-bright);
  animation: stream-blink 1s steps(2, end) infinite;
}
@keyframes stream-blink {
  50% { opacity: 0; }
}
```

**NEVER ChatGPT-style:**
- No bubble that pops in fully formed
- No "typing..." indicator with three dots
- No avatar that "types"
- No fade-in animation for the message body

**ALWAYS Claude Code-style:**
- Plain monospace text
- Streaming caret while in-flight
- Tools/tasks shown as the indented tree below the verb
- Fixed alignment, no shifting layout

### 9.4 What's NOT allowed (audit checklist)

When reviewing any new UI work, reject anything matching:

- ❌ `border-radius: 50%; animation: spin` (any rotation-based loader)
- ❌ `<svg>` icons rotating endlessly
- ❌ Three-dot "typing" indicators (`<span>.</span><span>.</span><span>.</span>`)
- ❌ "Loading..." text without an active verb + meta
- ❌ Multiple loading indicators visible at the same time
- ❌ Skeleton screens that pulse uniformly (acceptable for first-paint of a TABLE; not for chat)
- ❌ Progress bars that fill linearly without real progress data
- ❌ Bouncing dots
- ❌ Spinning gears
- ❌ Anything that would feel at home in a Bootstrap 4 modal

---

## 10. Shadow & Depth

Almost no shadows. Dark UIs use border contrast for depth, not shadows.

The only shadow allowed:
```css
/* Floating elements (modals, dropdowns) */
box-shadow: 0 16px 48px rgba(0, 0, 0, 0.6);
```

---

## 11. PRD → UI Mapping

Every PRD section must have a corresponding UI surface. Audit:

| PRD Section | UI View | Component |
|---|---|---|
| 1. Hubify Repo Strategy | Settings → Repos | Repo list with status |
| 2. Lab Template | Files tab | File tree + folder structure |
| 3. Agent Hierarchy | Agents view | Agent cards + hierarchy tree |
| 4. Cross-Lab Sharing | Knowledge view | Shared datasets/learnings/templates lists |
| 5. GPU/Compute Pipeline | Pipelines + Experiments | Pipeline cards + experiment table |
| 6. Backup & Data Mgmt | Settings → Backups | Backup status table |
| 7. Website System | Site tab | Live preview iframe + deploy button |
| 8. CLI/TUI Spec | (the entire app) | This IS the spec |
| 9. Fly.io Deployment | Settings → Deploy | Fly machine list |
| 10. Failure Handling | Alerts view | Alert list with severity |
| 10.5. RunPod Safety Layer | Compute view | Pod cards + credit balance |
| 10.6. Token Limit Handling | Settings → Models | Model fallback config |
| 10.7. Hubify Architecture | Settings → Integration | Convex/GitHub/Fly status |
| 11. Cost Management | Costs view | Cost charts + breakdown |
| 12. Implementation Plan | Tasks view | Kanban board |
| 13. Houston Method v2 | (encoded into experiment lifecycle) | QC gates in Experiments view |
| 14. Technical Primitives | (under the hood, not UI) | n/a |
| 15. Security & Secrets | Settings → Secrets | Masked input list |
| 16. Monitoring & Observability | Director view | Live activity timeline |
| 17. Website Generation | Site tab | Site preview + edit subdomain |
| 18. Cron Schedule | Settings → Crons | Cron list with status |
| 19. Director Cockpit | Director view | Review queue + running + summary |
| 20. Ideas & Insights | Ideas view | Idea capture + AI analysis |

**Every PRD feature has a UI surface.** No orphan features.

---

## 12. Voice & Microcopy

- **Lowercase by default** in nav, breadcrumbs, status bar (`director`, `experiments`, `papers`)
- **Sentence case** for headings (`Good morning, Houston`, `Needs your review`)
- **UPPERCASE** only for status labels (`PASS`, `FAIL`, `RUNNING`)
- **Monospace** for IDs, paths, numbers, commands (`EXP-053`, `bigbounce/papers/`, `$412.60`)
- **No exclamation marks.** No "let's go", "amazing", "🎉".
- **Direct verbs** for buttons (`Approve`, `Modify`, `Reject` — not "Click to approve").
- **Numbers always exact** (`$12.40`, not "around $12").

---

## 13. Forbidden Patterns

- ❌ Rainbow accent colors (blue + green + amber + teal + purple all at once)
- ❌ Emoji in UI (only in user-typed messages)
- ❌ Gradients (except brand mark)
- ❌ Drop shadows on cards (use borders)
- ❌ Rounded pill buttons larger than 24px tall
- ❌ "Friendly" microcopy ("Hey there!", "Let's get started!")
- ❌ Stock illustrations or icons
- ❌ Generic placeholder text ("Lorem ipsum")
- ❌ Box-shadow glows
- ❌ Animated gradients
- ❌ Hover transforms (scale, rotate)
- ❌ Curved shapes / blob backgrounds
- ❌ Light mode (dark only — for now)

---

## 14. Success Criteria

The UI passes if:

1. **A researcher who has never used it can navigate to the Experiments table within 5 seconds**
2. **Every view has real BigBounce data, no placeholders**
3. **The terminal feels like the primary interaction surface, not an afterthought**
4. **Switching views feels instant (< 200ms)**
5. **Resizing panels feels smooth (60fps)**
6. **All keyboard shortcuts work (Cmd+P, Cmd+B, Cmd+J)**
7. **The whole thing looks like Cursor's cousin, not a SaaS dashboard**
8. **Houston can take a screenshot at any moment and feel proud to share it**

---

*This design system locks the visual direction. Every implementation decision references this doc.*
