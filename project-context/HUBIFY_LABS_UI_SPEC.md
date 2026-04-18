# Hubify Labs — UI/UX Design Specification

**Note on fixture text (2026-04-18 fire #33):** This spec contains mockup-wireframe strings such as "Quintom MCMC: P(quintom-B) = 84.3%", "Anomalies: 328,448", and "eROSITA 9,303" (used as example seeded UI content). These are intentionally-frozen mockup fixtures, not fact claims. Live paper status: [`SSOT/index.md`](SSOT/index.md). Current canonical: quintom-B is a theoretical channel only per Paper 1 §VII.H (zero free w0-wa samples; "P(quintom-B) = 98.6%" retracted fire #25); 319,443 anomalies across 8 surveys (Paper 3 §1); eROSITA DR1 = 298 BigAE top-cut (Paper 3 Table 1).

**Version:** 1.0 | **Date:** 2026-04-07
**Companion to:** `HUBIFY_LABS_PRD.md`

---

## Design Philosophy

**Terminal-native, research-first, minimal chrome.**

The interface should feel like mission control for a research lab — not a SaaS dashboard. Think NASA flight control, not Notion. Dark backgrounds, monospace text, data-dense panels, zero decoration. Every pixel either shows data or accepts input.

**Aesthetic references:**
- Bloomberg Terminal (data density, keyboard-driven)
- htop/btop (real-time system monitoring)
- LazyGit (TUI git client, keyboard-first)
- Karpathy's autoresearch terminal output
- The indydevdan lead-agents TUI (Nuclear UI pattern)

---

## 1. CLI/TUI Design

### 1.1 Color Palette

```
Background:    #0d1117  (GitHub dark)
Surface:       #161b22  (panel backgrounds)
Border:        #30363d  (subtle borders)
Text primary:  #e6edf3  (bright white)
Text muted:    #7d8590  (gray)
Accent green:  #3fb950  (success, active, running)
Accent amber:  #d29922  (warning, queued)
Accent red:    #f85149  (error, critical, failed)
Accent blue:   #58a6ff  (info, links, highlights)
Accent purple: #bc8cff  (agent names, special)
```

### 1.2 Typography

```
Primary:     JetBrains Mono (all TUI text)
Fallback:    Menlo, Monaco, Consolas
Tab width:   2 spaces
Line height: 1.4 (terminal default)
```

### 1.3 Main TUI Layout (4 panels)

```
+============================================================================+
|  HUBIFY LABS  |  3 labs  |  1 active  |  $12.40 today  |  1 pod  |  08:42 |
+================================+==========================================+
|                                |                                          |
|  CHAT                          |  LAB: bigbounce                          |
|  ----                          |  Status: ACTIVE  |  Phase: 9             |
|                                |                                          |
|  houston > what happened       |  +-- GPU Pod: H200 (sleepy_blush_crane)  |
|  overnight?                    |  |   GPU: 87%  |  VRAM: 42/143 GB       |
|                                |  |   Exp: neowise_fullsky (48h est)      |
|  orch > 3 experiments passed:  |  |   Cost: $42.30  |  ETA: 14h           |
|  - cross-correlation 4.1s     |  |                                       |
|  - redshift tomography 47s    |  +-- Papers                              |
|  - quintom P(qB)=84.3%        |  |   P1: Ready  P2: Ready                |
|                                |  |   P3: 95%    P4: 85%                  |
|  houston > deploy phase 9      |  |                                       |
|                                |  +-- Experiments: 53 complete            |
|  orch > Delegating to          |  |   Anomalies: 328,448                  |
|  Infrastructure Lead...        |  |   Surveys: 15 scanned                 |
|                                |  |                                       |
|  infra > Creating H200 pod.   |  +-- Backups                             |
|  Estimated cost: $172 for      |  |   Local: 2h ago  |  GH: 4h ago        |
|  48h. Budget OK ($208 left).  |  |   HF: 1d ago     |  B2: 3d ago         |
|                                |  |                                       |
|  > _                           |  +-- Credits: $847  (~236h remaining)    |
|                                |                                          |
+================================+==========================================+
|  TASKS                                     |  ALERTS                      |
|  ----- [4 active, 2 complete, 1 queued]    |  ------                      |
|  * Deploy NEOWISE full-sky    Infra Lead   |  ! Pod disk 92% full  12m    |
|  * Write Phase 9 scripts      Research Ld  |  ! Credits < 48h     1h     |
|  v Back up overnight results  Backup Agt   |                              |
|  v Update site stat cards     Site Updater |                              |
|  o Compile Paper 3 PDF        Writing Lead |                              |
|  o Cross-match NEOWISE x Gaia Analysis Ld  |                              |
|  o Peer review Paper 2        Skeptic Agt  |                              |
+============================================+==============================+
```

### 1.4 Panel Descriptions

**Top Bar** (1 line, always visible)
```
HUBIFY LABS  |  {lab_count} labs  |  {active_count} active  |  ${daily_cost} today  |  {pod_count} pod(s)  |  {time}
```
Color-coded: lab names green=active, amber=queued, gray=paused.

**Chat Panel** (left, 60% width)
- Human input at bottom with `> ` prompt
- Agent responses with role prefix in purple: `orch >`, `research-lead >`, `infra >`
- Scrollable history
- Supports markdown-lite (bold, code blocks, lists)
- `/` commands: `/status`, `/queue`, `/pods`, `/papers`, `/costs`, `/labs`

**Lab Status Panel** (right, 40% width)
- Tree view of current lab state
- GPU pod status with live progress bar
- Paper status with readiness %
- Experiment count + anomaly count
- Backup status with time-since-last
- RunPod credit balance + hours remaining
- Switchable between labs with `Tab` or `/lab <slug>`

**Tasks Panel** (bottom-left, 60% width)
- TillDone task list from the orchestrator
- Status icons: `*` = in-progress, `v` = done, `o` = queued
- Agent assignment shown
- Count summary in header

**Alerts Panel** (bottom-right, 40% width)
- Unacknowledged alerts sorted by severity
- `!` prefix for warnings, `!!` for critical
- Time-since-created
- Press `a` to acknowledge, `r` to resolve

### 1.5 Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Tab` | Cycle focus between panels |
| `Ctrl+L` | Switch lab (dropdown) |
| `Ctrl+P` | Quick command palette |
| `Ctrl+S` | Toggle sidebar (lab status) |
| `Ctrl+T` | Toggle tasks panel |
| `Ctrl+A` | Toggle alerts panel |
| `Ctrl+Q` | Quit (with confirmation) |
| `Enter` | Send chat message |
| `Up/Down` | Chat history |
| `PgUp/PgDn` | Scroll chat |
| `a` | Acknowledge selected alert |
| `r` | Resolve selected alert |

### 1.6 Alternative Views (switchable via `/` commands)

**Queue View** (`/queue`)
```
+============================================================================+
|  EXPERIMENT QUEUE — bigbounce  |  53 complete  |  3 running  |  5 queued   |
+============================================================================+
|  #  | Phase | Name                      | Status    | GPU-h | Cost   | QC  |
|-----|-------|---------------------------|-----------|-------|--------|-----|
|  54 | 9     | neowise_fullsky           | RUNNING   | 12.3  | $44.17 | --  |
|  55 | 9     | gaia_full_epoch           | QUEUED    | ~96   | ~$345  | --  |
|  56 | 10    | paper3_compile            | QUEUED    | ~2    | ~$7    | --  |
|  57 | 10    | paper4_figures            | QUEUED    | ~4    | ~$14   | --  |
|  --- completed (53) --------------------------------------------------------|
|  53 | P1    | p1_fnl_recompute          | COMPLETE  | 0.1   | $0.36  | OK  |
|  52 | P1    | p1_qso_classifier         | COMPLETE  | 0.2   | $0.72  | OK  |
|  51 | OB5   | fisher_forecast_spherex   | COMPLETE  | 0.01  | $0.04  | OK  |
|  ...                                                                        |
+============================================================================+
```

**Costs View** (`/costs`)
```
+============================================================================+
|  COST DASHBOARD — All Labs                                                  |
+============================================================================+
|  TODAY        |  THIS WEEK   |  THIS MONTH  |  ALL TIME    |  BALANCE     |
|  $12.40      |  $87.20      |  $412.60     |  $847.30     |  $847.00     |
+============================================================================+
|  Lab           | GPU-hrs | LLM Cost | GPU Cost | Total   | Experiments   |
|----------------|---------|----------|----------|---------|---------------|
|  bigbounce     | 124.3   | $23.40   | $389.20  | $412.60 | 53            |
|  (planned)     |   --    |    --    |    --    |    --   |  --           |
+============================================================================+
|  MODEL USAGE                                                                |
|  Claude Opus 4.6:    12.4M tokens  ($18.60)  — orchestrator, leads        |
|  Claude Sonnet 4.6:   8.2M tokens  ($3.28)   — workers                    |
|  Claude Haiku 4.5:    2.1M tokens  ($0.21)   — QC, backup, GPU mgr       |
|  OpenRouter fallback:  0.3M tokens  ($0.12)   — 2 fallback events         |
+============================================================================+
```

**Papers View** (`/papers`)
```
+============================================================================+
|  PAPERS — bigbounce                                                         |
+============================================================================+
|  #  | Title                              | Version | Pages | Status      |
|-----|------------------------------------|---------|-------|-------------|
|  1  | Spin-Torsion Cosmology             | v2.2.0  |  24   | READY       |
|  2  | f_NL Forecast                      | v1.3.0  |  12   | READY       |
|  3  | DESI DR1 Anomaly Catalog           | v1.0    |  ~35  | 95% (ApJS)  |
|  4  | Galaxy Chirality Catalog           | v1.0    |  ~20  | 85% (MNRAS) |
+============================================================================+
|  Actions: [c]ompile PDF  |  [v]iew PDF  |  [s]ubmit to arXiv  |  [e]dit  |
+============================================================================+
```

---

## 2. Web App Design

### 2.1 Purpose

The web app is for **monitoring and oversight** — not primary interaction. Houston uses the CLI/TUI for commands; the web app is what you check from your phone, share with collaborators, or project on a second monitor.

### 2.2 Technology

- **Next.js 15** (App Router, React Server Components)
- **Tailwind CSS** (dark mode default, terminal aesthetic)
- **Convex client** (real-time subscriptions)
- **shadcn/ui** components (minimal, customized to terminal style)

### 2.3 Color Palette (matches TUI)

```css
:root {
  --bg:           #0d1117;
  --surface:      #161b22;
  --border:       #30363d;
  --text:         #e6edf3;
  --text-muted:   #7d8590;
  --green:        #3fb950;
  --amber:        #d29922;
  --red:          #f85149;
  --blue:         #58a6ff;
  --purple:       #bc8cff;
}
```

### 2.4 Typography

```css
--font-mono:  'JetBrains Mono', 'Fira Code', monospace;
--font-sans:  'Inter', -apple-system, sans-serif;
--font-serif: 'Newsreader', Georgia, serif;  /* for paper content only */
```

**Primary:** JetBrains Mono for all data, stats, agent output
**Secondary:** Inter for UI labels, navigation, descriptions
**Paper content:** Newsreader for rendered paper text (academic feel)

### 2.5 Page Layout

```
+============================================================================+
|  [HUBIFY LABS]  |  Dashboard  |  Labs  |  Costs  |  Alerts  |  Settings   |
+============================================================================+
|                                                                             |
|  [Page Content]                                                             |
|                                                                             |
+============================================================================+
```

- **Nav:** Top horizontal bar, dark background, monospace text
- **Content:** Full-width, no sidebar (data-dense, not app-like)
- **Footer:** None (wastes space)

### 2.6 Pages

#### Dashboard (`/`)

The homepage. Shows all labs at a glance.

```
+============================================================================+
|  HUBIFY LABS DASHBOARD                                     $12.40 today    |
+============================================================================+
|                                                                             |
|  +--[ bigbounce ]--------------------+  +--[ (create new lab) ]---------+  |
|  | Status: ACTIVE     Phase: 9       |  |                               |  |
|  | Experiments: 53    Anomalies: 328K|  |  + Create New Lab              |  |
|  | Papers: 4 (2 ready)              |  |                               |  |
|  | GPU: H200 87% ($42 today)        |  +-------------------------------+  |
|  | Last: cross-correlation 4.1s     |                                      |
|  +-----------------------------------+                                      |
|                                                                             |
|  RECENT ACTIVITY                                                            |
|  ----------------------------------------------------------------           |
|  08:14  bigbounce  QSO classifier: 12,920 high-z QSOs recovered            |
|  08:02  bigbounce  Cross-correlation: SDSS x LAMOST 4.1s                   |
|  07:45  bigbounce  Redshift tomography: rate rises with z at 47s            |
|  07:10  bigbounce  Quintom MCMC: P(quintom-B) = 84.3%                      |
|  06:27  bigbounce  Multi-modal joint: 212 hidden anomalies found            |
|  ----------------------------------------------------------------           |
|                                                                             |
|  UNRESOLVED ALERTS (2)                                                      |
|  !! Pod disk 92% full — bigbounce H200    12 min ago    [Acknowledge]       |
|  !  Credits < 48h remaining              1 hour ago    [Acknowledge]       |
|                                                                             |
+============================================================================+
```

#### Lab Detail (`/labs/[slug]`)

Deep view of one lab. 4 tabs: Overview | Experiments | Papers | Knowledge.

**Overview tab:**
```
+============================================================================+
|  BIGBOUNCE — Spin-Torsion Cosmology Research                               |
+============================================================================+
|  [Overview]  [Experiments]  [Papers]  [Knowledge]                           |
+============================================================================+
|                                                                             |
|  KEY RESULTS                                                                |
|  +--------+  +--------+  +--------+  +--------+  +--------+  +--------+   |
|  | -35/8  |  | 0.27d  |  |  27.6  |  | 2.28x  |  | 328K+  |  | 12,920 |  |
|  | f_NL   |  | beta   |  | Bayes  |  | bias   |  | anom.  |  | QSOs   |  |
|  +--------+  +--------+  +--------+  +--------+  +--------+  +--------+   |
|                                                                             |
|  GPU STATUS                                                                 |
|  Pod: sleepy_blush_crane (H200 SXM)                                        |
|  [=========================>          ] 65%  neowise_fullsky                |
|  GPU: 87%  |  VRAM: 42/143 GB  |  ETA: 14h  |  Cost: $42.30               |
|                                                                             |
|  EXPERIMENT PHASES                                                          |
|  Phase 1: RE-RUN ............ [##########] 6/6  COMPLETE                    |
|  Phase 2: VALIDATION ........ [##########] 6/6  COMPLETE                    |
|  Phase 3: CROSS-SURVEY ...... [##########] 6/6  COMPLETE                    |
|  Phase 4: SCIENCE ........... [##########] 5/5  COMPLETE                    |
|  Phase 5: NEW SURVEYS ....... [##########] 4/4  COMPLETE                    |
|  Phase 6: X-RAY/SPACE ....... [##########] 3/3  COMPLETE                    |
|  Phase 7: SPECULATIONS ...... [##########] 3/3  COMPLETE                    |
|  Phase 8: ADVANCED ML ....... [##########] 3/3  COMPLETE                    |
|  Phase 9: FULL-SCALE ........ [=====>    ] 1/2  RUNNING                     |
|  Phase 10: PAPERS ........... [          ] 0/2  QUEUED                      |
|  Pipeline 1: f_NL ........... [======>   ] 3/5  IN PROGRESS                 |
|                                                                             |
|  SURVEYS SCANNED (15)                                                       |
|  +----------+--------+----------+--------+                                  |
|  | DESI     | 195,829| SDSS     | 77,905 |                                 |
|  | LAMOST   | 44,075 | eROSITA  |  9,303 |                                 |
|  | Planck   |    193 | ACT      |    200 |                                 |
|  | NEOWISE  |    444 | Gaia     |  5,000 |                                 |
|  | BOSS     |    500 | DES      |    --- |                                 |
|  | VLASS    |    --- | LOFAR    |  1,000 |                                 |
|  | JWST     |    500 | Chandra  |    800 |                                 |
|  | XMM      |  1,000 |          |        |                                 |
|  +----------+--------+----------+--------+                                  |
|                                                                             |
+============================================================================+
```

**Experiments tab:** Filterable table of all experiments with phase, status, cost, QC.

**Papers tab:** Paper cards with compile/view/submit actions.

**Knowledge tab:** Searchable wiki with entity/concept/comparison types.

#### Costs (`/costs`)

Real-time cost tracking across all labs. Charts for daily/weekly/monthly trends. Per-model breakdown. Budget alerts.

#### Alerts (`/alerts`)

Alert management: acknowledge, resolve, filter by severity/lab/source.

#### Settings (`/settings`)

Global config: model defaults, budget limits, backup schedule, notification preferences.

---

## 3. Shared Design Patterns

### 3.1 Stat Cards

Used in both TUI and web to show key metrics:

```
TUI version:
+--------+
| -35/8  |
| f_NL   |
+--------+

Web version:
+------------------+
|     -35/8        |
|  f_NL prediction |
|  parameter-free  |
+------------------+
```

### 3.2 Progress Bars

```
TUI: [=========================>          ] 65%  neowise_fullsky
Web: Same, but with hover tooltip showing ETA and cost
```

### 3.3 Activity Feed

```
Timestamp  Lab          Event                                  Agent
08:14      bigbounce    QSO classifier: 12,920 QSOs recovered  Analysis Lead
08:02      bigbounce    Cross-correlation: 4.1s SDSS x LAMOST  Analysis Lead
07:45      bigbounce    Redshift tomography: rate rises at 47s  Statistics Agent
```

### 3.4 Agent Avatars

Each agent level gets a distinct icon:
- Orchestrator: `[O]` / diamond icon
- Lead: `[L]` / square icon
- Worker: `[W]` / circle icon

Color by role:
- Research: blue
- Analysis: green
- Writing: purple
- Infrastructure: amber

### 3.5 Status Indicators

```
Running:    * (green pulse)
Complete:   v (green check)
Failed:     x (red X)
QC Fail:    ! (amber warning)
Queued:     o (gray circle)
Paused:     - (gray dash)
```

---

## 4. Responsive Behavior

### TUI
- Minimum: 100 columns x 30 rows
- Panels collapse gracefully at narrow widths
- Chat panel always visible (primary interaction)
- Status panel hides first, then tasks, then alerts

### Web
- Desktop: Full 4-panel layout
- Tablet: Stack panels vertically
- Mobile: Single-column, most important data first
- Real-time Convex subscriptions work on all sizes

---

## 5. Interaction Flow Examples

### "Run overnight experiments"

**TUI:**
```
houston > run overnight batch
orch > Delegating to Research Lead for experiment design...
research-lead > Based on Pipeline 1 results (12,920 QSOs), I recommend:
  1. NEOWISE full-sky scan (48h, $172)
  2. Gaia full epoch photometry (96h, $345)
  3. Paper 3 compile with new f_NL results
  Estimated total: $524, 7 days GPU time.
  Deploy all to queue? [y/n]
houston > y, but use a new pod — current one has disk issues
orch > Infrastructure Lead: creating new H200 pod...
infra > Pod created: eager_coral_orca (H200 SXM, $3.59/hr)
  SSH: root@198.51.100.42 -p 22344
  Deploying 48 experiment scripts...
  Starting NEOWISE full-sky...
  Queue: 3 experiments chained.
  Budget guardian: $524 within weekly limit ($500). Tight. Alert at 90%.
orch > Overnight batch deployed. GPU active. Good night, Houston.
```

### "What happened last night?"

**TUI:**
```
houston > what happened overnight?
orch >
  OVERNIGHT REPORT (10:14 PM - 8:42 AM):
  =============================================
  Experiments:  3 completed, 0 failed
  GPU hours:    9.7h ($34.83)
  Key results:
    - Cross-correlation: SDSS x LAMOST at 4.1s (anomalies trace real structure)
    - Redshift tomography: anomaly rate rises with z at 47s (genuine high-z populations)
    - Quintom reanalysis: P(quintom-B) drops from 98.6% to 84.3% with DR2 mock
  Alerts:
    - Pod disk at 92% (needs cleanup or new pod)
    - Credits < 48h at current spend rate
  Website: Updated with 3 new stat cards + activity entries
  Backups: All results on local + GitHub
```

---

## 6. Mockup Generation Plan

To create interactive skeleton mockups before building:

### TUI Mockup
- Use Python `rich` or `textual` library
- Single `.py` file that renders the 4-panel layout with fake data
- Keyboard navigation between panels
- Run with: `python3 hubify-labs-tui-mockup.py`

### Web Mockup
- Single `index.html` file with inline CSS (dark theme)
- Fake data matching BigBounce stats
- All panels visible, no JavaScript needed for initial review
- Run with: `open hubify-labs-web-mockup.html`

Both mockups should be created in `~/Desktop/CODE_2025/hubify-labs-mockups/` (separate from all existing projects) for Houston to review before any real implementation begins.

---

*This design spec ensures visual alignment before a single line of platform code is written. Review the mockups, approve the aesthetic, then build with confidence.*
