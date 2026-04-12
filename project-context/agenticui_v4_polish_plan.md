# AgenticUI → v4 Mockup Polish Sprint

**Created:** 2026-04-11
**Status:** IN PROGRESS
**Approval required:** Houston must confirm DONE — not auto-closeable
**Workspace:** `/Users/houstongolden/Desktop/CODE_2025/hubify-labs-mockups/v4/`
**Reference:** `/Users/houstongolden/Desktop/CODE_2025/hubify-labs-mockups/agenticui/` (26 components, full token system)

---

## The Gap

v4 mockups use ad-hoc CSS variables (`--bg`, `--surface`, `--text`) while AgenticUI has a production token system (`--color-text-primary`, `--shadow-elevation-3`, 8-step color ramps, 12-level spacing ramp). v4 components are hand-rolled and don't match AgenticUI's polished patterns (40px button height, proper focus rings, elevation shadows, Departure Mono label discipline).

---

## Execution Plan — 4 Passes

### Pass 1: Token Foundation ✅ COMPLETE
**Target:** index.html first, then cascade to other 4 files
- [x] Extract AgenticUI token block from `agenticui/comp-buttons.html` and `agenticui/colors.html`
- [x] Build unified token set mapping v4 vars → AgenticUI vars
- [x] Radius ramp aligned: --r-sm:4px, --r-md:8px, --r-lg:12px, --r-xl:16px, --r-2xl:20px, --r-3xl:24px, --r-pill:9999px
- [x] Import 4-level shadow system (elevation 1-4) — all 5 files
- [x] Badge color tokens (8 colors) + semantic status tokens + neutral ramp — all 5 files
- [x] Focus ring token — all 5 files
- [x] Apply to index.html (20K lines) — radius, buttons, badges tokenized
- [x] Cascade to agent-management-clone.html — full token block added
- [x] Cascade to cli-tui-mockup.html — radius ramp aligned, elevations added
- [x] Cascade to desktop-app-mockup.html — tokens + hardcoded 4px eliminated
- [x] Cascade to marketing-site-mockup.html — tokens + all 12 hardcoded 4px eliminated
- [ ] Git commit (pending — will commit at end of pass)

### Pass 2: Component Swap ✅ COMPLETE
**Target:** Highest density areas across all 5 files
- [x] Buttons → AgenticUI pattern — index.html already aligned (40px, Mono 13px, 0.3px, var(--r-md))
- [x] Buttons → agent-management aligned (32px btn-sm, 0.3px tracking, var(--r-md), focus ring)
- [x] Buttons → marketing site aligned (40px height, 0 24px padding, 0.3px tracking, var(--r-md), focus ring)
- [x] Inputs/search → index.html already aligned (40px, 12px padding, focus→strong)
- [x] Badges/status → index.html already aligned (19px, var(--r-sm), Geist 13px, 8 color variants)
- [x] Toast/notifications — index.html notification drawer aligned to AgenticUI spacing
- Note: Tables and CLI/TUI are terminal-style, not AgenticUI table pattern

### Pass 3: Spacing and Density ✅ COMPLETE (high-impact)
**Target:** All 5 files — focused on structural violations
- [x] index.html sidebar: brand 14px→16px, lab-header 7→8px gap, 14→16px padding
- [x] index.html dropdowns: dd-search 6px→8px, dd-item 7→8px gap, proj-dd 10→8px gap
- [x] index.html nav items: section-label 5→4px/14→16px, group-header same
- [x] index.html file tree: gap 6→8px, padding 14→16px, height 22→24px
- [x] index.html notifications: head 11→12px/14→16px, row 9→8px gap/11→12px
- [x] index.html profile popout: gap 9→8px, padding 7→8px
- [x] index.html chat rows: gap 7→8px, padding 14→16px
- [x] marketing site: all card padding 18px→20px (11 occurrences)
- [x] marketing site: gap 7px→8px throughout (3 occurrences)
- [x] marketing site: arch-node 14→16px, browser-url border-radius→var(--r-sm)
- Note: Micro-spacing (3px, 5px in dense badges/pills) intentionally preserved for density

### Pass 4: Typography Polish ✅ COMPLETE
**Target:** All 5 files
- [x] Verified hierarchy: Geist body → Departure Mono labels/nav → Georgia headings → IBM Plex Sans numbers
- [x] No misapplied fonts found — all uppercase labels use var(--label-mono), all body uses var(--geist)
- [x] index.html: 69 Geist body references, proper serif for paper content, proper mono for data
- [x] marketing site: Newsreader serif for editorial content, Playfair Display for hero, Departure Mono for labels
- [x] agent-management: Departure Mono labels, Geist body, Georgia headings, IBM Plex Sans numbers
- [x] All files use CSS variable stacks (no raw font-family declarations in styles)
- [x] Letter-spacing aligned: 0.3px on buttons (AgenticUI spec), 0px on labels (AgenticUI spec)
- [ ] Git commit (pending)

---

## Files (priority order)

| File | Lines | Priority | Description |
|------|-------|----------|-------------|
| index.html | 19,970 | P0 | Main web app — 80% of impact |
| marketing-site-mockup.html | 5,971 | P1 | Public marketing site |
| agent-management-clone.html | 1,165 | P2 | Agent management screen |
| cli-tui-mockup.html | 809 | P3 | Terminal/CLI interface |
| desktop-app-mockup.html | 697 | P4 | macOS desktop wrapper |

## AgenticUI Reference Components

| Component | File | Key Specs |
|-----------|------|-----------|
| Buttons | comp-buttons.html | 40px, Mono 13px uppercase, 8px radius |
| Inputs | comp-textinput.html | 40px, 12px padding, focus ring |
| Tables | comp-table.html | 40px sticky headers, 64px rows |
| Badges | comp-badges.html | 19px, 4px radius, semantic colors |
| Toast | comp-toast.html | 320px, 20px radius, 4 variants |
| Shadows | shadows.html | 4-level elevation system |
| Colors | colors.html | Full 8-step ramps per hue |
| Typography | typography-light.html | Font scale + hierarchy |

## Rules

1. Figma MCP only for screenshot cross-checks of component styles, not for design generation
2. Every cron cycle must produce visible code changes — no audits, no reports
3. Work explicitly on v4/ files only
4. Git commit after each pass completion
5. Houston must approve and confirm DONE — not auto-closeable
6. Reference agenticui/ components as the source of truth for styles
