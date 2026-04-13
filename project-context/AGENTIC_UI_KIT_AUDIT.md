# AgenticUI Kit Audit — Phase 1

**Created:** 2026-04-09
**Source:** `https://www.figma.com/design/SjPhSVKTbtE35Xh7PNsmNA/HG--AGENTIC-DESIGN-SYSTEM--v1.1-`
**fileKey:** `SjPhSVKTbtE35Xh7PNsmNA`
**Extracted by:** Claude via Figma MCP (`use_figma` plugin API + `get_design_context`)
**Status:** ALL 27 COMPONENTS EXTRACTED · MISC + TYPOGRAPHY confirmed · Phase 24 complete · STYLE TESTER + PLAYGROUND pending (showcase pages, low priority)
**Account:** houston@bamf.ai, Pro + Full seat (200 calls/day)
**Companion:** `AGENTIC_UI_REVAMP_PLAN.md` (canonical plan)

---

## Executive summary — what this kit actually is

**It is NOT a single-accent minimalist kit.** It is a **token-driven dual-mode design system** with:
- 7 variable collections (MODE, COLORS, SPACING, TYPOGRAPHY, BORDER RADIUS, STROKE, THEMES)
- **Full LIGHT + DARK semantic theming** via mode switching (the MODE collection has 75 semantic tokens that alias into raw ramps)
- 9-ramp color system (8 color ramps × 8 shades + 9-step neutral ramp) = ~73 raw color tokens
- 15 text styles built on 4 font families (**Geist body**, **New York Large headings**, **Departure Mono labels**, **JetBrains Mono code**)
- 7 effect styles including 4 elevations + focus ring + destructive focus ring + switch shadow
- 3 border-radius modes (DEFAULT / SHARP / ROUNDED) — pick one at file level
- 37 spacing tokens (PADDING scale + ICONS scale + BREAKS + PAGE MARGINS)
- 27 component categories across 130+ variants
- 5 showcase pages (COLORS, TYPOGRAPHY, STYLE TESTER, PLAYGROUND, MISC)

**Key insight for the merge:** The MODE collection is the semantic layer. We already have Cabinet cream + cocoa + sage tokens — we just need to REPLACE the LIGHT mode aliases with Cabinet values while adopting the full structure. The DARK mode can adopt AgenticUI's defaults as-is (Cabinet has no strong dark mode).

---

## Full page map (from `figma.root.children`)

**Top-level pages (6 real + 3 dividers):**

| Page | nodeId | Status |
|---|---|---|
| COLORS | `6:6` | ✅ extracted |
| TYPOGRAPHY | `2003:4067` | ✅ extracted — Phase 24: 7 CSS vars added to :root, wired to .tbl/.btn |
| STYLE TESTER | `4145:17200` | pending (showcase only) |
| PLAYGROUND | `230:839` | pending (too large to parse, skipped) |
| COMPONENTS (header) | `6:7` | — |
| MISC | `178:121` | ✅ extracted — Phase 22: PULSATING-DOT · LOADING-DOTS · SKELETON shimmer |

**Component sub-pages (27):**

| Component | pageId | Main frame | Type |
|---|---|---|---|
| Avatars | `39:13` | `179:17313` | COMPONENT_SET |
| Badges | `123:391` | `124:2898` | COMPONENT_SET |
| Breadcrumbs | `123:380` | `549:163` | COMPONENT_SET |
| Buttons | `123:393` | `147:2305` | COMPONENT_SET (1996×1440 — big variant grid) |
| Chat | `833:15476` | `4127:18971` | FRAME (chat input) |
| Checkbox | `123:396` | `4067:1119` | FRAME |
| Code block | `4124:7084` | `4126:5640` (simple) / `4125:5282` (advanced) | FRAME |
| Dropdown | `4084:4148` | `4084:4545` | FRAME |
| File upload | `833:15459` | `4028:6200` | FRAME |
| Helper text | `4066:7038` | `4066:7445` | FRAME |
| Icons | `179:662` | `179:868` | FRAME (4080×5354 — giant icon grid) |
| Menu | `554:1261` | `558:659` | COMPONENT_SET |
| Modal | `4091:6571` | `4092:1582` | FRAME |
| Navbar | `123:375` | `230:699` | COMPONENT_SET |
| Pagination | `123:376` | `716:3790` | COMPONENT_SET |
| Progress | `4072:6976` | `4072:6991` / `4072:7836` slider | FRAME |
| Radio button | `123:397` | `124:2977` | COMPONENT_SET |
| Search | `337:6059` | `338:6162` | COMPONENT_SET |
| Switch | `814:72` | `814:110` | COMPONENT_SET |
| Stepper | `833:15458` | `4001:1347` | FRAME |
| Tabs | `123:390` | `4056:1314` | FRAME (Tab group) |
| Table | `123:395` | 10 cell-type COMPONENT_SETs | COMPONENT_SETs |
| Text Area | `2003:3794` | `4092:1380` | FRAME |
| Text Input | `123:394` | `761:20738` | COMPONENT_SET |
| Toast | `2003:4066` | `4008:197` | FRAME |
| Tooltip | `2001:2432` | `2001:2681` | COMPONENT_SET |

**MISC page frames:**
- `587:3511` DEMO PAGE HEADER
- `338:6698` Cursor blink animation (COMPONENT_SET)
- `678:1996` LOADER LIGHT / `683:2107` LOADER DARK
- `713:2805` LOADER SMALL LIGHT / `714:2955` LOADER SMALL DARK
- `761:23192` Skeleton loading animation
- `146:1787` AGENTIC UI LOGO
- `4004:93` PULSATING-DOT (for AI thinking)
- `4030:7034` Loading animation
- `4092:1131` SCROLL FADE

---

## 1. COLORS — raw ramps (from COLORS variable collection)

All values resolved from `figma.variables.getLocalVariablesAsync()`.

### 1.1 Neutral ramp (9 steps)

| Token | Hex | RGB |
|---|---|---|
| `NEUTRAL/Neutral 100` | `#FFFFFF` | 255,255,255 |
| `NEUTRAL/Neutral 200` | `#F7F7F7` | 247,247,247 |
| `NEUTRAL/Neutral 300` | `#E5E5E5` | 229,229,229 |
| `NEUTRAL/Neutral 400` | `#E0E0E0` | 224,224,224 |
| `NEUTRAL/Neutral 500` | `#8F8F8F` | 143,143,143 |
| `NEUTRAL/Neutral 600` | `#616161` | 97,97,97 |
| `NEUTRAL/Neutral 700` | `#363636` | 54,54,54 |
| `NEUTRAL/Neutral 800` | `#191919` | 25,25,25 |
| `NEUTRAL/Neutral 900` | `#000000` | 0,0,0 |

### 1.2 Color ramps (8 ramps × 8 steps = 64 tokens)

| | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 |
|---|---|---|---|---|---|---|---|---|
| **Red** | #FFF5F5 | #FFDEDE | #FFA0A0 | #FF5C5C | #F02D2D | #D50B0B | #570303 | #2A0303 |
| **Green** | #F6FEF6 | #E0FAE0 | #A6F0A5 | #4CE160 | #3CC14E | #288034 | #1B561A | #0C310D |
| **Blue** | #F5F9FF | #D4E5FE | #84B4FB | #4D93FC | #0968F6 | #0049B8 | #002A69 | #19133A |
| **Orange** | #FFF9F5 | #FFEAD3 | #FFC382 | #FF8806 | #EC7303 | #C15100 | #562501 | #2F1604 |
| **Yellow** | #FFFCF5 | #FFF8D5 | #FFE58A | #FFBD14 | #EEBB04 | #855F00 | #553B06 | #312102 |
| **Purple** | #F6F5FE | #E2DDFD | #AD9EFA | #836BFF | #583AEE | #3B1FC6 | #271A68 | #20092B |
| **Teal** | #F7FDFD | #D7F4F6 | #8EDFE5 | #44CCD5 | #1BBFCA | #006F93 | #07465A | #04252F |
| **Pink** | #FEF6FA | #FCDCEC | #F79CC8 | #F155A0 | #DE458E | #A51359 | #4B112D | #360606 |

**Note on Yellow 100:** Variable shows `#FFFCF5` (resolved) but earlier `get_design_context` showed `#FFFFF5` on the showcase. Small discrepancy — trust the variable value `#FFFCF5`.

---

## 2. MODE collection — semantic tokens with LIGHT + DARK aliases

This is the **critical** token layer. 75 semantic tokens, each aliased to a different raw color per mode.

### 2.1 BACKGROUND tokens

| Token | LIGHT alias | LIGHT hex | DARK alias | DARK hex |
|---|---|---|---|---|
| `BACKGROUND/Primary` | Neutral 100 | #FFFFFF | Neutral 900 | #000000 |
| `BACKGROUND/Secondary` | Neutral 200 | #F7F7F7 | Neutral 800 | #191919 |
| `BACKGROUND/Tertiary` | Neutral 400 | #E0E0E0 | Neutral 600 | #616161 |
| `BACKGROUND/Accent` | Blue 500 | #0968F6 | Blue 400 | #4D93FC |
| `BACKGROUND/Attention` | Red 600 | #D50B0B | Red 400 | #FF5C5C |
| `BACKGROUND/Success` | Green 500 | #3CC14E | Green 300 | #A6F0A5 |
| `BACKGROUND/Disabled` | Neutral 300 | #E5E5E5 | Neutral 600 | #616161 |
| `BACKGROUND/Elevated` | Neutral 100 | #FFFFFF | Neutral 800 | #191919 |
| `BACKGROUND/Secondary On Elevated` | Neutral 200 | #F7F7F7 | Neutral 900 | #000000 |

### 2.2 CONTENT tokens

| Token | LIGHT hex | DARK hex |
|---|---|---|
| `CONTENT/Primary` | #191919 (n800) | #F7F7F7 (n200) |
| `CONTENT/Secondary` | #616161 (n600) | #8F8F8F (n500) |
| `CONTENT/Disabled` | #E0E0E0 (n400) | #363636 (n700) |
| `CONTENT/Accent` | #002A69 (Blue 700) | #4D93FC (Blue 400) |
| `CONTENT/Attention` | #570303 (Red 700) | #FFA0A0 (Red 300) |
| `CONTENT/Success` | #288034 (Green 600) | #A6F0A5 (Green 300) |

### 2.3 BORDER tokens

| Token | LIGHT hex | DARK hex |
|---|---|---|
| `BORDER/Strong` | #000000 (n900) | #FFFFFF (n100) |
| `BORDER/Medium` | #8F8F8F (n500) | #616161 (n600) |
| `BORDER/Subtle` | #E5E5E5 (n300) | #363636 (n700) |
| `BORDER/Accent` | #0968F6 (Blue 500) | #4D93FC (Blue 400) |
| `BORDER/Attention` | #D50B0B (Red 600) | *Red-dark* |
| `BORDER/Success` | #3CC14E (Green 500) | *Green-dark* |
| `BORDER/Disabled` | #E5E5E5 | #363636 |

### 2.4 LINK token

| Token | LIGHT | DARK |
|---|---|---|
| `LINK/Default` | #0049B8 (Blue 600) | #4D93FC (Blue 400) |

### 2.5 INPUT state overlays (transparent) — IMPORTANT for interactive states

| Token | LIGHT | DARK |
|---|---|---|
| `INPUT/Hover (Dark)` | `rgba(0,0,0,0.06)` | `rgba(255,255,255,0.08)` |
| `INPUT/Pressed` | `rgba(0,0,0,0.08)` | `rgba(255,255,255,0.12)` |
| `INPUT/Selected` | `rgba(0,0,0,0.12)` | `rgba(255,255,255,0.16)` |
| `INPUT/Focus` | `rgba(0,0,0,0.04)` | `rgba(255,255,255,0.08)` |

### 2.6 OVERLAY

| Token | LIGHT | DARK |
|---|---|---|
| `OVERLAY/Background` | `rgba(0,0,0,0.03)` | `rgba(0,0,0,0.64)` |

**Observation:** Light-mode overlay is nearly invisible (3%). Dark-mode overlay is heavy (64%). This is a deliberate choice — light mode sidepeeks/drawers use the elevation shadow as the depth cue, not a dim overlay.

---

## 3. TYPOGRAPHY system — 15 text styles

All resolved from `getLocalTextStylesAsync()` and the TYPOGRAPHY variable collection.

### 3.1 Font families (from variables)

| Token | Value |
|---|---|
| `family/Body` | **Geist** |
| `family/Labels, Links` | **Departure Mono** |
| `family/Headings` (inferred) | **New York Large** |
| `family/Code` (inferred) | **JetBrains Mono** |

### 3.2 Weight aliases

| Token | Value |
|---|---|
| `weight/Regular` | Regular |
| `weight/Medium` | Medium |
| `weight/Bold` | Bold |

### 3.3 Line-height scale

| Token | Value |
|---|---|
| `line-height/Tiny Text` | 15px |
| `line-height/Small Text` | 18px |
| `line-height/Regular Text` | 24px |
| `line-height/Large Text` | 28px |
| `line-height/Huge Text` | 40px |
| `line-height/Titles` | 80px |
| `line-height/Website Heading` | 100px |

### 3.4 Text styles (the actual styles applied to text nodes)

| Style | Family | Weight | Size | Line-height | Letter-spacing |
|---|---|---|---|---|---|
| `SYSTEM/Heading/h1` | New York Large | Regular | 32px | 40px | -0.3px |
| `SYSTEM/Heading/h2` | New York Large | Medium | 20px | 24px | 0 |
| `SYSTEM/Heading/h3` | New York Large | Medium | 18px | 24px | 0 |
| `SYSTEM/Body/md/regular` | **Geist** | Regular | 16px | 24px | 0 |
| `SYSTEM/Body/md/bold` | Geist | Medium | 16px | 24px | 0 |
| `SYSTEM/Body/sm/regular` | Geist | Regular | 14px | 18px | 0 |
| `SYSTEM/Body/sm/bold` | Geist | Medium | 14px | 18px | 0 |
| `SYSTEM/Body/xs/regular` | Geist | Regular | 13px | 15px | 0 |
| `SYSTEM/Body/xs/bold` | Geist | Medium | 13px | 15px | 0 |
| `SYSTEM/Label/md/regular` | **Departure Mono** | Regular | 12px | 18px | 0.3px |
| `SYSTEM/Label/md/underline` | Departure Mono | Regular | 12px | 18px | 0.3px |
| `SYSTEM/Label/sm/regular` | Departure Mono | Regular | 10px | 18px | 0 |
| `SYSTEM/Code/md` | **JetBrains Mono** | Regular | 12px | 18px | 0 |
| `BUTTON/Label/md/regular` | Departure Mono | Regular | 13px | 15px | 0 |
| `BUTTON/Label/sm/regular` | Departure Mono | Regular | 10px | 11px | 0 |

**Key insight:** Body is **Geist** (Vercel's sans). Labels/buttons use **Departure Mono** (a free pixel-grid mono by Departure Labs, distinctive technical feel). Headings use New York Large (Apple serif). Code blocks use JetBrains Mono. The Departure Mono choice is the single most distinctive visual decision in this kit — it gives every label + button an "AI-terminal" feel.

---

## 4. EFFECTS — 7 effect styles (shadows + focus rings)

All values resolved from `getLocalEffectStylesAsync()`.

### 4.1 Elevation shadows

```css
/* Shadows/elevation1 — card */
box-shadow:
  0 1px 2px 0 rgba(0,0,0,0.05),
  inset 0 -1px 0 0 rgba(0,0,0,0.10);

/* Shadows/elevation2 — dropdown */
box-shadow:
  0 8px 16px -8px rgba(0,0,0,0.04),
  0 6px 6px -3px rgba(0,0,0,0.04),
  0 3px 3px -1.5px rgba(0,0,0,0.04),
  0 1px 1px -0.5px rgba(0,0,0,0.04);

/* Shadows/elevation 3 — drawer (note the space in name) */
box-shadow:
  0 0 0 1px rgba(0,0,0,0.08),     /* hairline border */
  0 12px 12px 0 rgba(0,0,0,0.04),
  0 6px 6px 0 rgba(0,0,0,0.04),
  0 3px 3px 0 rgba(0,0,0,0.04),
  0 1px 1px -0.5px rgba(0,0,0,0.04);

/* Shadows/elevation 4 — modal */
box-shadow:
  0 0 0 1px rgba(0,0,0,0.08),     /* hairline border */
  0 16px 16px 0 rgba(0,0,0,0.04),
  0 12px 12px 0 rgba(0,0,0,0.04),
  0 6px 6px 0 rgba(0,0,0,0.04),
  0 3px 3px 0 rgba(0,0,0,0.04),
  0 1px 1px -0.5px rgba(0,0,0,0.04);
```

**Pattern:** every level stacks 4% rgba layers at increasing offsets. Level 3+ adds a hairline 8% border. Very soft, very Mac-native feeling.

### 4.2 Focus rings

```css
/* Components/Focus — default focus */
box-shadow:
  0 0 0 2px rgba(9,104,246,0.5),   /* blue-500 at 50% */
  0 0 0 1px rgba(255,255,255,1),   /* white separator */
  0 1px 2px 0 rgba(0,0,0,0.04),
  inset 0 -1px 0 0 rgba(0,0,0,0.10),
  inset 0 0 0 1px rgba(255,255,255,1);

/* Components/Destructive Focus */
box-shadow:
  0 0 0 2px rgba(255,92,92,0.5),   /* red-400 at 50% */
  0 0 0 1px rgba(255,255,255,1),
  0 1px 2px 0 rgba(0,0,0,0.04),
  inset 0 -1px 0 0 rgba(0,0,0,0.10),
  inset 0 0 0 1px rgba(255,255,255,1);
```

**Hallmark:** the focus ring has a WHITE spacer between the element and the colored ring. This is the classic Vercel / shadcn pattern for high-contrast focus visibility.

### 4.3 Switch toggle shadow

```css
/* Swtich/Toggle [sic — typo preserved in source] */
box-shadow:
  0 6px 6px 0 rgba(0,0,0,0.04),
  0 3px 3px 0 rgba(0,0,0,0.04),
  0 1px 1px 0 rgba(0,0,0,0.04),
  inset 1px 2px 3px 0 rgba(0,0,0,0.15);
```

---

## 5. SPACING system (partial — 17 of 37 tokens extracted)

From the SPACING variable collection. More values pending in a follow-up extraction.

| Token | Value |
|---|---|
| `PADDING/4` | 4px |
| `PADDING/12` | 12px |
| (more PADDING/N tokens expected: 8, 16, 20, 24, 32, 40, 48, 64, 96, 128) | pending |
| `ICONS/14` | 14px |
| `ICONS/16` | 16px |
| (more ICON sizes expected: 12, 20, 24, 32) | pending |
| `BREAKS/INSIDE PADDING` | 16px |
| `BREAKS/CONTENT BREAK` | 32px |
| `PAGE MARGINS/Margin L` | 48px |
| `PAGE MARGINS/Margin XL` | 56px |

---

## 6. BORDER RADIUS system — 3 modes

8 radius tokens × 3 modes:

| Mode | Behavior |
|---|---|
| **DEFAULT** | standard rounded feel |
| **SHARP** | probably 0 or 2px everywhere — brutalist |
| **ROUNDED** | probably 2x default — softer |

The kit lets you switch the entire file between radius modes at once. Specific values pending extraction.

---

## 7. PAINT STYLES — 22 (avatars + gradients)

From `getLocalPaintStylesAsync()`:
- `Avatars/01` through `Avatars/20` — 20 avatar background fill styles (colors TBD, likely gradient/image based)
- `Gradient/Shimmer` — linear gradient for skeleton loading
- `Gradient/Scrollfade (Light)` — linear gradient for edge fade masks

---

## 8. Cabinet × AgenticUI merge plan (Phase 2 preview)

### 8.1 Hard constraint mapping

| Area | AgenticUI LIGHT | Cabinet v2-sage | Phase 2 decision |
|---|---|---|---|
| `BACKGROUND/Primary` | `#FFFFFF` | `#faf6f1` (cream) | **Override AgenticUI → Cabinet cream** |
| `BACKGROUND/Secondary` | `#F7F7F7` | `#f3ede4` (cream-warm) | **Override → Cabinet warm cream** |
| `BACKGROUND/Tertiary` | `#E0E0E0` | `#e8dfd0` (cream-deeper) | **Override → Cabinet deeper cream** |
| `BACKGROUND/Elevated` | `#FFFFFF` | `#fbf8f3` | **Override → Cabinet elevated cream** |
| `CONTENT/Primary` | `#191919` | `#3b2f2f` (cocoa) | **Override → Cabinet cocoa** |
| `CONTENT/Secondary` | `#616161` | `#6b5a5a` (cocoa-muted) | **Override → Cabinet muted cocoa** |
| `BACKGROUND/Accent` (brand) | `#0968F6` (blue) | `#5fb88a` (sage) | **Override → Cabinet sage** |
| `BORDER/Accent` | `#0968F6` | `#5fb88a` | **Override → sage** |
| `CONTENT/Accent` | `#002A69` | `#2d5a42` (sage-dark) | **Override → sage dark** |
| `LINK/Default` | `#0049B8` | sage or cocoa | **Override → sage dark or cocoa** |
| `BORDER/Strong` | `#000000` | `#3b2f2f` (cocoa) | **Override → cocoa** |
| `BORDER/Medium` | `#8F8F8F` | `#a89887` (warm-gray) | **Override → warm gray** |
| `BORDER/Subtle` | `#E5E5E5` | `#e8dfd0` | **Override → cream-deeper** |
| `BACKGROUND/Success` | `#3CC14E` (pure green) | `#5fb88a` (sage) | **Override → sage** (merges with brand) |
| `BACKGROUND/Attention` | `#D50B0B` (pure red) | keep red-600 | **ADOPT AgenticUI red for errors only** |
| `OVERLAY/Background` | `rgba(0,0,0,0.03)` | `rgba(59,47,47,0.05)` | **Override → cocoa-tinted** |

### 8.2 Adopt wholesale

- **Typography scale** — adopt `SYSTEM/Body/{md,sm,xs}/{regular,bold}` sizing (16/24, 14/18, 13/15). Keep Newsreader serif for headings (Cabinet brand), swap Geist for Cabinet body (Inter or similar — flag for Houston).
- **Departure Mono for labels** — this is a DISTINCTIVE choice that gives the whole kit its AI-terminal feel. **ADOPT** for all labels + buttons across the Hubify Labs IDE. Replace JetBrains Mono labels with Departure Mono.
- **Elevation scale** — adopt all 4 levels exactly. Much better than Cabinet's single flat border.
- **Focus ring** — adopt the white-spacer + 2px blue/red ring pattern. Replace Cabinet's sage-halo focus.
- **INPUT state overlays** — adopt the rgba overlay pattern for hover/pressed/selected/focus. Cabinet currently hand-rolls each interactive state.
- **BORDER RADIUS system** — start in DEFAULT mode, let Houston try SHARP / ROUNDED variants.
- **Spacing scale** — adopt PADDING/{4,8,12,16,20,24,32,48,56} as the floor.

### 8.3 Reject or adapt

- **The 8 colored ramps** — ADOPT but use ONLY for status indicators, data viz, and anomaly badges. NOT for layout chrome. Non-sage colors are "earned" — they appear only to mark meaning (error, warning, info, success, and per-survey badges in the research IDE).
- **Pure-black text / white bg** — REJECT in favor of Cabinet's cream + cocoa. This is Houston's #1 brand constraint.
- **New York Large headings** — REJECT. Cabinet uses Newsreader serif which is on-brand for the research identity. Houston has explicit Newsreader preference for paper content.
- **Swtich/Toggle typo effect style** — adopt shadow but rename to `Switch/Toggle`.

---

## 9. Next extraction steps

**Phase 1 remaining:**
1. ✅ Full page map + node IDs
2. ✅ Color ramps (COLORS variable collection)
3. ✅ LIGHT + DARK semantic tokens (MODE variable collection)
4. ✅ Typography scale + 4 font families + 15 text styles
5. ✅ Effect styles (4 elevations + 2 focus rings + switch shadow)
6. [ ] Remaining SPACING tokens (17/37 extracted)
7. [ ] BORDER RADIUS tokens (0/8 extracted, 3 modes)
8. [ ] STROKE tokens (0/4 extracted)
9. [ ] THEMES collection (0/10 extracted)
10. [ ] Component variant definitions — Buttons (top priority), Text Input, Tabs, Badges, Navbar, Menu, Tooltip, Toast, Modal
11. [ ] DEMO frame screenshots for visual reference (optional)

**Phase 2 will use all of the above to produce a merged `style.css` token map that:**
- Preserves Cabinet cream/cocoa/sage identity
- Adopts AgenticUI's semantic token structure (BACKGROUND/*, CONTENT/*, BORDER/*, INPUT/*, OVERLAY/*)
- Adopts the 4 elevation shadows, focus ring pattern, spacing scale, and Departure Mono for labels
- Supports LIGHT (default) and DARK modes via CSS custom properties

---

## 10. CANONICAL VALUES — Extracted via Figma MCP 2026-04-09 (duplicated file)

**New fileKey:** `SjPhSVKTbtE35Xh7PNsmNA`
**URL:** `https://www.figma.com/design/SjPhSVKTbtE35Xh7PNsmNA/HG--AGENTIC-DESIGN-SYSTEM--v1.1-`
**Nodes audited:** `6:6` (COLORS page), `2004:902` (Colors frame), `2006:1686` (Shadows frame)

### 10.1 Elevation shadows — EXACT CSS values

```css
/* elevation1 = card
   DROP_SHADOW: #0000000D (0,1,r2,s0) + INNER_SHADOW: #0000001A (0,-1,r0,s0) */
--elev-1: 0 1px 2px rgba(0,0,0,.05), inset 0 -1px 0 rgba(0,0,0,.10);

/* elevation2 = dropdown
   4× DROP_SHADOW: #0000000A with negative spreads */
--elev-2: 0 8px 16px -8px rgba(0,0,0,.04), 0 6px 6px -3px rgba(0,0,0,.04),
          0 3px 3px -1.5px rgba(0,0,0,.04), 0 1px 1px -.5px rgba(0,0,0,.04);

/* elevation3 = drawer
   1px ring @8% + 4 depth layers */
--elev-3: 0 0 0 1px rgba(0,0,0,.08), 0 12px 12px rgba(0,0,0,.04),
          0 6px 6px rgba(0,0,0,.04), 0 3px 3px rgba(0,0,0,.04),
          0 1px 1px -.5px rgba(0,0,0,.04);

/* elevation4 = modal
   1px ring @8% + 5 depth layers */
--elev-4: 0 0 0 1px rgba(0,0,0,.08), 0 16px 16px rgba(0,0,0,.04),
          0 12px 12px rgba(0,0,0,.04), 0 6px 6px rgba(0,0,0,.04),
          0 3px 3px rgba(0,0,0,.04), 0 1px 1px -.5px rgba(0,0,0,.04);
```

**Cabinet light mode adaptation** (cocoa tint: rgba(59,47,47)):
```css
--elev-1: 0 1px 2px rgba(59,47,47,.05), inset 0 -1px 0 rgba(59,47,47,.08);
--elev-2: 0 8px 16px -8px rgba(59,47,47,.04), 0 6px 6px -3px rgba(59,47,47,.04),
          0 3px 3px -1.5px rgba(59,47,47,.04), 0 1px 1px -.5px rgba(59,47,47,.04);
--elev-3: 0 0 0 1px rgba(59,47,47,.07), 0 12px 12px rgba(59,47,47,.04),
          0 6px 6px rgba(59,47,47,.04), 0 3px 3px rgba(59,47,47,.04),
          0 1px 1px -.5px rgba(59,47,47,.04);
--elev-4: 0 0 0 1px rgba(59,47,47,.07), 0 16px 16px rgba(59,47,47,.04),
          0 12px 12px rgba(59,47,47,.04), 0 6px 6px rgba(59,47,47,.04),
          0 3px 3px rgba(59,47,47,.04), 0 1px 1px -.5px rgba(59,47,47,.04);
```

### 10.2 Label typography — EXACT values

| Token | Value | Source |
|---|---|---|
| `--ai-label-sz` | `12px` | Figma `size/Button` |
| `--ai-label-sz-tiny` | `13px` | Figma `size/Tiny` |
| `--ai-label-track` | `0.3px` | Figma `letter-spacing/spacious` |
| `--ai-label-lh` | `18px` | Figma `line-height/Small Text` |
| `--ai-label-lh-tiny` | `15px` | Figma `line-height/Tiny Text` |
| `--ai-label-track-tight` | `-0.3px` | Figma `letter-spacing/tight` |
| Font family | `'Departure Mono'` | `family/Labels, Links` |

### 10.3 Semantic surface tokens

| Figma token | Value | Cabinet equivalent |
|---|---|---|
| `--background/primary` | `#FFFFFF` | `:root.light --bg: #faf6f1` (keep Cabinet cream) |
| `--background/secondary` | `#F7F7F7` | `:root.light --surface: #fdfaf4` (keep Cabinet warm) |
| `--content/primary` | `#191919` | `:root.light --text-bright: #3b2f2f` (keep Cabinet cocoa) |
| `--content/secondary` | `#616161` | `:root.light --text: #5a4a3e` (keep Cabinet warm) |
| `--transparent-8%` | `rgba(0,0,0,0.08)` | Maps to elevation ring values |

### 10.4 Color ramps (COLORS page — full hex extraction)

**Neutral scale:**
| Shade | Hex |
|---|---|
| n100 | `#FFFFFF` |
| n200 | `#F7F7F7` |
| n300 | `#E5E5E5` |
| n400 | `#CCCCCC` |
| n500 | `#8F8F8F` |
| n600 | `#707070` |
| n700 | `#363636` |
| n800 | `#191919` |
| n900 | `#000000` |

**Green scale** (closest to Cabinet sage `#5fb88a` — note: AgenticUI green is more vivid/lime):
| Shade | Hex |
|---|---|
| g100 | `#F6FEF6` |
| g200 | `#E0FAE0` |
| g300 | `#A6F0A5` |
| g400 | `#4CE160` |
| g500 | `#3CC14E` |
| g600 | `#288034` |
| g700 | `#1B561A` |
| g800 | `#0C310D` |

**Decision: Cabinet sage `#5fb88a` does NOT map to AgenticUI green (too vivid/lime). Cabinet sage stays as-is as the brand accent.**

**Blue scale:**
| Shade | Hex |
|---|---|
| b100 | `#F5F9FF` |
| b200 | `#D4E5FE` |
| b300 | `#84B4FB` |
| b400 | `#4D93FC` |
| b500 | `#0968F6` |
| b600 | `#0049B8` |
| b700 | `#002A69` |
| b800 | `#19133A` |

---

## 11. TEXT INPUT — Canonical spec from Figma 761:20738 (extracted 2026-04-10)

### 11.1 Sizes

| Size | Height | Font size | Line height |
|---|---|---|---|
| md (default) | 40px | 14px | 18px |
| sm | 32px | 13px | 15px |

### 11.2 States

| State | Border | Background |
|---|---|---|
| default | `1px solid border/subtle (#e5e5e5)` | `background/primary (white/cream)` |
| hover | subtle border | `background/secondary (#f7f7f7)` |
| focus | `1px solid border/strong (black)` — NOT accent/sage | `background/primary` |
| error | `1px solid border/attention (#d50b0b)` | primary |
| success | `1px solid border/success (#288034)` | primary |
| disabled | subtle border, text = content/disabled (#e0e0e0) | primary |

### 11.3 Typography

- **Input text**: Geist 14px/18px (md), 13px/15px (sm), `color: content/primary` when filled
- **Placeholder**: same font, `color: content/secondary (#616161)` = `var(--text-dim)`
- **Label**: Departure Mono 12px, 0.3px letter-spacing, uppercase, muted default / bright on focus
- **Horizontal padding**: `12px`

### 11.4 Helper text

- Background: `background/secondary (#f7f7f7)`, border-radius: 8px, padding: 4px 8px, Geist 13px
- error: `#ffdede` bg, `#570303` text; success: `#e0fae0` bg, `#1b561a` text; warning: `#fff8d5` bg, `#855f00` text

---

## 12. BADGE — Canonical spec from Figma 124:2898 (extracted 2026-04-10)

### 12.1 Dimensions

- Both lg and sm: **19px tall**, `rounded` type ≈ 4px border-radius, `pill` = 999px
- Border=true: 1px solid; Border=false: no border

### 12.2 Color ramps applied to index.html

| Class | Light bg | Light text | Light border |
|---|---|---|---|
| `.badge-green` / `.badge-success` | sage tint | `#2e7d5a` | sage tint border |
| `.badge-red` / `.badge-error` | red tint | `var(--crit)` | red tint border |
| `.badge-yellow` / `.badge-warn` | yellow tint | `var(--warn)` | yellow tint border |
| `.badge-blue` / `.badge-info` | `rgba(9,104,246,.08)` | `#0049B8` | blue tint |
| `.badge-orange` | `rgba(236,115,3,.08)` | `#C15100` | orange tint |
| `.badge-purple` | `rgba(88,58,238,.08)` | `#3B1FC6` | purple tint |
| `.badge-teal` | `rgba(0,111,147,.08)` | `#006F93` | teal tint |
| `.badge-neutral` | `var(--surface-2)` | `var(--text-dim)` | `var(--border)` |

✅ Applied to index.html Phase 3 component merge (2026-04-10)

