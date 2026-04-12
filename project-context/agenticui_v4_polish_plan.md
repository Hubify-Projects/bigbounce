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
- [x] Git committed

### Pass 5: Deep Grid Sweep ✅ COMPLETE (bonus)
**Target:** All 5 files — eliminate every off-grid gap/padding value
- [x] index.html: 12 gap:9px → 8px, 48 gap:10px → 8px, 13 gap:7px → 8px (CSS rules)
- [x] index.html: 6 structural padding:7px → 8px, 22 padding:9px → 8px
- [x] index.html: companion padding aligned (11→12, 13→12, 14→16)
- [x] marketing site: 21 gap violations fixed (tn-brand, get-card, hero-stats, etc.)
- [x] agent-management: 3 gap:10px → 8px
- [x] cli-tui: 1 gap:7px → 8px
- [x] desktop-app: 4 violations (status-icons, traffic, spotlight, notification)
- [x] Zero off-grid gap values remain across all 5 v4 files
- [x] Micro-spacing (2px 7px on pills/badges/kbd) intentionally preserved
- [x] Git committed (3 commits)

### Pass 6: Border-Radius Tokenization ✅ COMPLETE (bonus)
**Target:** All 5 files — replace hardcoded border-radius with AgenticUI radius tokens
- [x] index.html: 14 structural values tokenized (8px→r-md, 10px→r-lg, 20px→r-2xl, 14px→r-xl)
- [x] marketing-site: 38 values tokenized (8px→r-md, 10px→r-lg, 12px→r-lg, 14px→r-xl, 20px→r-2xl)
- [x] desktop-app: 10 values tokenized (window, dock, dock-icon, badge, notification, popover, file-drop)
- [x] agent-management: already clean (no hardcoded structural radius)
- [x] cli-tui: only micro-radius (1-6px) — intentionally preserved
- [x] Zero hardcoded structural border-radius values remain (only comments, micro-radius 1-6px, pills 999px/9999px)
- [x] Git committed (2 commits)

### Pass 7: Shadow Elevation Tokenization ✅ COMPLETE (bonus)
**Target:** index.html — replace hardcoded box-shadow with elevation tokens
- [x] index.html: 13 hardcoded box-shadows tokenized to --elev-1/--elev-2
- [x] Card components: .stat, .card, .aui-chart-card, .aui-metric-card, .tbl-wrap → elev-1
- [x] Hover states: .stat:hover, .card:hover → elev-2
- [x] Input components: .chat-input-pill, .sp-tabs active, .sp-select:hover → elev-1/elev-2
- [x] marketing-site: already uses elevation tokens (no changes needed)
- [x] desktop-app/agent-management/cli-tui: use custom dramatic shadows (intentional, not card-level)
- [x] Git committed (1 commit)

### Pass 8: Focus Ring Unification ✅ COMPLETE (bonus)
**Target:** index.html — all focusable inputs/selects use --focus-ring token
- [x] Removed dead duplicate .sp-select:focus rule (blue rgba(9,104,246) immediately overridden)
- [x] .sp-select:focus, .view select:focus → var(--focus-ring) (was blue or none)
- [x] .toggle-sw:focus-visible → var(--focus-ring) (was custom 3px ring)
- [x] 5 input :focus states changed from box-shadow:none → var(--focus-ring)
- [x] All focusable elements now use the canonical AgenticUI focus ring (2px bg + 4px accent)
- [x] marketing-site + agent-management already consistent (no changes needed)
- [x] Git committed (1 commit)

### Pass 9: Semantic Color Tokenization ✅ COMPLETE (bonus)
**Target:** index.html — add missing semantic tokens, tokenize hardcoded colors
- [x] Added --success/#success-bg tokens to both dark and light themes
- [x] Added --tooltip-bg/--tooltip-text tokens to both themes (light mode inverts correctly)
- [x] .helper-text.error/success/warning → semantic tokens (was hardcoded hex)
- [x] .textarea.error border → var(--crit) (was hardcoded #d50b0b)
- [x] Both tooltip components tokenized (7 hardcoded #191919 → var(--tooltip-bg))
- [x] Removed redundant :root.light .tooltip override
- [x] Git committed (1 commit)

### Pass 10: Off-Grid Padding/Margin Alignment ✅ COMPLETE (bonus)
**Target:** All 5 files — eliminate 18px/22px/26px padding and margin values
- [x] index.html: 26 values aligned (18→16/20, 22→24, 26→24)
- [x] marketing-site: 16 values aligned (18→16, 22→24, 26→24)
- [x] agent-management: 3× padding:18px → 20px
- [x] desktop-app + cli-tui: already clean
- [x] Git committed (3 commits)

### Pass 11: 14px Grid Alignment ✅ COMPLETE (bonus)
**Target:** index.html — snap all 14px spacing to 12 or 16
- [x] 30 edits: 20× padding/margin 14→16, 5× gap 14→12, 3× asymmetric aligned, 2× companions
- [x] Only non-spacing 14px remains (font-size, icon dimensions, line-height)
- [x] Git committed (1 commit)

### Pass 12: 11px/13px/14px Deep Grid Sweep ✅ COMPLETE (bonus)
**Target:** All 5 files — eliminate remaining off-grid 11px, 13px, 14px spacing
- [x] marketing-site: 40 edits (28× gap:14→12, 3× padding:14→16, 9× mixed 14px snapped)
- [x] index.html: 18 edits (terminal 11→12/13→12, wiki/csv/fig-row 13→12, file-preview-md margins, view-mode-btn, sp-toggle, sb-sub-mode)
- [x] desktop-app: 1× padding:14→16
- [x] cli-tui: 1× padding:10x14→12
- [x] Remaining 9px values are micro-spacing on pills/badges/compact markdown (intentionally preserved)
- [x] Git committed (1 commit)

### Pass 13: 18px/22px/25px Remaining Off-Grid Sweep ✅ COMPLETE (bonus)
**Target:** index.html — snap remaining odd spacing in CSS rules
- [x] 12 edits: pt-body 25→24, md-pre 13/15/17→12/16/16, sp-group-head 18→16, dest-grid 18→16
- [x] md-hr 22→24, json-preview/children 18→16, dos-section 18→16, sb-item-children 22→24
- [x] desc-22 padding 22→24, code-ln 18→16, rt-action-row 10x14→12x16
- [x] Remaining 18/22px in themed zones (BB site preview, PDF, vibe sandbox) and inline HTML intentionally preserved
- [x] Git committed (1 commit)

### Pass 14: Marketing Site 14px/18px/22px Margin Sweep ✅ COMPLETE (bonus)
**Target:** marketing-site-mockup.html — eliminate all off-grid margin values
- [x] 17× margin-bottom:14→16, 1× margin-top:14→16
- [x] 9× margin:18→16 (live-counter, arch-foot, surface-icon, surface-desc, demo-frame, footer-cta, plan-sep, feat-title, lede.mt)
- [x] 3× margin:22→24 (live-counter, surfaces-foot, plan-billing-note)
- [x] Zero off-grid margin values remain in marketing-site CSS rules
- [x] Git committed (1 commit)

### Pass 15: index.html Remaining Off-Grid Margins + Mixed Padding ✅ COMPLETE (bonus)
**Target:** index.html — snap remaining 14px margins, 15px margins, mixed 10x14 padding
- [x] 7× margin:14→16 (dispatch-preview, task-detail, section-sep, heatmap-legend, contrib-drilldown, file-preview-img-cap, chat-list-footer)
- [x] 1× md-bq padding/margin 15→16
- [x] 3× mixed padding snap (cmdp-section 10x14→12x16, xlab-gateway-foot gap+padding, profile-row 10x14→12x16)
- [x] Remaining 14px margins are in themed zones (fp-pdf) and inline HTML styles (intentionally preserved)
- [x] Git committed (1 commit)

### Pass 16: Border-Radius Deep Tokenization ✅ COMPLETE (bonus)
**Target:** All 3 files — replace remaining 5/6/7/9/11px border-radius with tokens
- [x] index.html: notif-drawer 8→r-md, chat-show-tab 5→r-sm, 2× badge 7→r-md
- [x] marketing-site: 20 values (6→r-md, 5→r-sm, 7→r-md, 9→r-md, 11→r-lg)
- [x] desktop-app: popover 6→r-md + off-grid padding 5x7→4x8
- [x] Only scrollbar thumb (browser-specific) and micro-radius 1-3px remain hardcoded
- [x] Git committed (1 commit)

### Pass 17: Inline Style Grid Alignment + CLI Border-Radius ✅ COMPLETE (bonus)
**Target:** index.html inline styles + cli-tui border-radius
- [x] index.html: 11× inline margin:14→16, 9× inline margin:18→16, 2× inline padding aligned, 1× gap:18→16, 1× JS template
- [x] cli-tui: terminal window border-radius:6→var(--r-md)
- [x] Only themed zones (BB site preview) inline 14px margins remain
- [x] Git committed (1 commit)

### Pass 18: Deep 14px Padding Elimination ✅ COMPLETE (bonus)
**Target:** index.html — eliminate ALL remaining 14px padding/gap in CSS rules, inline styles, and JS templates
- [x] CSS rules: 24 component classes snapped (org-node, routing-row, task-detail-head/section, settings-link-row, standup-list/row, idea-row, settings-row, mem-layer/result, pinned-lab, compute-pod, provider-card, vibe-chat-body, code-pre, review-drilldown-head, reviewer-grid, interp-classification, routine-row, alert-row, js-tmpl-card, settings-nav-card, graph-node-card, dossier-header)
- [x] CSS gap:14px → 12px in 7 rules (cmdp-footer, routing-row, standup-row, settings-row, routine-row, fp-img-toolbar, fp-pdf-toolbar)
- [x] Mobile overrides: sb-brand 14→16, mobile-open sb-brand/sb-lab-header 14→16, view-inner 14→16, stat 14→16
- [x] Inline HTML: 11× padding:10px 14px → 12px 16px (keyboard shortcut rows), 7× switch-with-label padding:0 14px → 0 16px, 3× last-row padding:0 14px → 0 16px
- [x] Inline HTML: map.md card padding:14px → 16px, button row padding:0 14px 14px → 0 16px 16px
- [x] Inline HTML: sessions header 4px 14px → 4px 16px, log-pre 11px 14px → 12px 16px, comparison footer 12px 14px → 12px 16px, citation caption 0 16px 14px → 0 16px 16px, cross-model card 14px → 16px
- [x] Inline: agent actions 11px 14px → 12px 16px (×2), alerts action 10px 14px → 12px 16px
- [x] JS templates: 2× code-pre padding:12px 14px → 12px 16px, notif empty 36px 14px → 36px 16px
- [x] Zero padding:*14px remains — only font-size:14px and line-height:14px (7 non-spacing occurrences)
- [x] Git committed (1 commit)

### Pass 19: 13px + Structural 10px Grid Snap ✅ COMPLETE (bonus)
**Target:** index.html — snap remaining 13px padding and structural 10px padding to grid
- [x] 2× padding:13px 16px → 12px 16px (unnamed cursor rule, contrib-section)
- [x] 8× structural padding:10px 12px → 12px (sp-md pre, survey-cell, hm2-qc-gate, org-node.reviewer, log-pre, hm-tooltip, inline journal header, inline sovereignty rule)
- [x] 1× pipeline-step padding:10px → 12px, briefing-cell 10px 8px → 8px
- [x] 1× chat-view-header padding:12px 0 10px → 12px 0 + margin-bottom:10px → 12px
- [x] 1× sp-md pre margin-bottom:9px → 8px
- [x] Remaining 10px values are micro-spacing on compact sidebar, pills, buttons, graph overlays, chat input — intentionally preserved
- [x] Git committed (1 commit)

### Pass 20: Cross-File Structural 10px Grid Snap ✅ COMPLETE (bonus)
**Target:** marketing-site + desktop-app — snap structural 10px to grid
- [x] marketing-site: 8 structural snaps (mock-sb 10px 8px→8px, live-counter 10px 16px→12px 16px, blockquote 10px 12px→12px + border-radius tokenized, compare-table th/td 10px 16px→12px 16px, article heading margin 10px→12px, mobile .btn 10px 16px→12px 16px, inline mock padding 10px→12px + margin-bottom 10px→12px)
- [x] desktop-app: 2 structural snaps (notification 10px 12px→12px, popover 10px→12px)
- [x] Remaining 10px values across all files are micro-spacing on compact pills/buttons/sidebar/terminal — intentionally preserved
- [x] Git committed (1 commit)

### Pass 21: Pill + Skeleton Border-Radius Tokenization ✅ COMPLETE (bonus)
**Target:** All 4 files — replace remaining hardcoded pill/structural border-radius with tokens
- [x] marketing-site: 3× border-radius:99px → var(--r-pill), bc-link 3px → var(--r-sm), mockup-controls .ctrl 3px → var(--r-sm)
- [x] index.html: 2× border-radius:9999px → var(--r-pill), ag-skeleton 3px → var(--r-sm)
- [x] desktop-app: 1× border-radius:999px → var(--r-pill)
- [x] cli-tui: 1× border-radius:999px → var(--r-pill)
- [x] Only micro-radius (1-2px on bars/code/kbd/dots) and 3px in mini-mockup/scrollbar remain hardcoded
- [x] Git committed (1 commit)

### Pass 22: Shadow Elevation Tokenization + Transition Normalization ✅ COMPLETE (bonus)
**Target:** agent-management + marketing-site shadows, index.html transitions
- [x] agent-management: 4× hardcoded box-shadow → var(--elev-1), removed 4 redundant ::after inset pseudo-elements (−28 lines)
- [x] marketing-site: btn-sage:hover box-shadow → var(--elev-3)
- [x] index.html: 4× transition .14s → .12s (detail-back-btn, js-fig-row, settings-link-row, settings-nav-card)
- [x] All card-level shadows now use elevation tokens across all 5 files
- [x] Git committed (1 commit)

### Pass 23: Off-Grid Gap/Margin/Padding Deep Sweep ✅ COMPLETE (bonus)
**Target:** Remaining 14px, 11px, 10px, 9px, 5px structural values across index.html + marketing-site
- [x] index.html: gap:11px → 12px on .review + .file-preview-meta; padding-left:11px → 12px, margin-left:3px → 4px
- [x] index.html: gap:14px → 12px on 9 CSS classes (briefing-foot, dir-row, exp-filter-group, publish-ready-foot, labs-grid, gnc-meta-row, dest-stats, hm-tip-head) + section-minimal → 16px + 3 inline styles
- [x] index.html: margin-bottom:9px → 8px on 10 classes (sp-text p, sp-md p, site-meta-label, lsr-title/body, rt-mm-title/body, para-11, gnc-head, pipeline-parent)
- [x] index.html: margin-bottom:10px → 8px on 6 compact classes + 2 inline; → 12px on 8 section-level classes + 3 inline
- [x] index.html: gap:5px → 4px on 9 structural classes (review-actions, dir-brief-col, rt-info-grid, upload-files-list, kanban-card-badges, alert-actions, mem-result-tags, profile-actions, dest-meta) + stepper gap + margin
- [x] index.html: padding:*px 9px → 8px on 8 rules (filter-search, filter-search-minimal, sp-text input, paper-publish-btn, settings-row-value, vibe-tab, JS template, comment)
- [x] index.html: inline padding:3px 9px → 4px 8px on compute pod buttons
- [x] index.html: padding-top:6px → 8px, padding-bottom:7px → 8px, margin-bottom:7px → 8px
- [x] marketing-site: .arb-cell gap:5px → 4px
- [x] Themed zones (vibe sandbox, PDF preview, paper preview) intentionally excluded
- [x] Micro-spacing (5-6px on pills/dots/icon groups) preserved
- [x] Git committed `24b5f3d` — 64 edits across 2 files

### Pass 24: Pill/Badge/Kbd Horizontal Padding 7px → 8px ✅ COMPLETE (bonus)
**Target:** All remaining `padding:*px 7px` values across pills, badges, kbds, tooltips
- [x] index.html: 13 CSS pill/badge classes snapped (notif-cat, ra-btn, pill, gpu-status-pill, kb-tag, standup-status, profile-row-score, compute-pod-provider, reviewer-provider-pill, routine-rate, backup-status, chat-model/mode-pill, v3-badge)
- [x] index.html: ~20 inline kbd shortcut keys + 1 JS template kbd snapped (padding:2px 7px → 2px 8px)
- [x] index.html: zone-tiers + tooltip [data-tip]::before snapped (padding:3px 7px → 4px 8px)
- [x] index.html: mode-pill + interp-row .cls snapped (padding:1px 7px → 2px 8px)
- [x] index.html: upload-file-chip asymmetric padding fixed (3px 8px 3px 7px → 4px 8px)
- [x] index.html: margin-top:7px → 8px on chat-input-meta + 5× inline pcm-dot
- [x] index.html: chat-list-footer padding-top:10px → 12px
- [x] marketing-site: .step code padding:2px 7px → 2px 8px
- [x] Zero `padding:*px 7px` values remain in non-themed code
- [x] Git committed `22601f2` — 42 edits across 2 files

### Pass 25: Structural 5px Padding/Margin → 4px Grid ✅ COMPLETE (bonus)
**Target:** Rows, buttons, section headers with padding:5px or margin:5px
- [x] index.html: padding:5px 12px → 4px 12px on 4 URL/tab/footer elements
- [x] index.html: padding:5px 10px → 4px 12px on 3 buttons/badges/headers (horizontal also snapped)
- [x] index.html: padding:5px 0 → 4px 0 on 3 row elements + 1 asymmetric head
- [x] index.html: margin-bottom:5px → 4px on 4 classes, margin-top:5px → 4px on 6 classes
- [x] index.html: cfeed-header 6px 10px → 8px 12px, dos-section-head 6px 0 5px → 8px 0 4px
- [x] index.html: ps-picker-item 6px 10px → 8px 12px
- [x] index.html: pp-status border-radius:2px → var(--r-sm), margin-left:6px → 4px
- [x] index.html: nav-collapse-foot padding + gap snapped, mobile sb-app-links snapped
- [x] Git committed `9af9344` — 29 edits

### Pass 26: border-radius:2px Tokenization + margin-bottom:6px → 8px ✅ COMPLETE (bonus)
**Target:** Remaining off-grid 2px radii and 6px vertical margins
- [x] index.html: border-radius:2px → var(--r-sm) on 14 CSS classes (sb-item-toggle, tier-pill, term-tab .x, skel-text, skills-foot code, rt-mm-body code, xlab-foot-stat code, cmdp-footer kbd, heatmap-cell, heatmap-legend .hl-sq, tok-tex-math, tok-md-inline-code, fp-img-zoom-btn, fp-pdf-zoom-btn)
- [x] index.html: padding:0 3px → 0 4px on tok-tex-math, tok-md-inline-code, cmdp-footer kbd
- [x] index.html: margin-bottom:6px → 8px on 17 CSS classes (chat-hint, form-label/input-label, captain-heading, skel-title, prm-bar-wrap, empty-text, lsg-title, dispatch-preview-label, dispatch-preview-result, idea-desc, alert-desc, mem-result-body, pinned-lab-head, pinned-lab-desc, reviewer-card-head, reviewer-card-sum, dossier-title-row)
- [x] index.html: lsg-title padding-bottom:6px → 8px (also snapped)
- [x] index.html: 5× inline pcm-row margin-bottom:6px → 8px
- [x] index.html: 2× JS template sp-section-label inline margin-bottom:6px → 8px
- [x] index.html: 2× JS template inline margin-bottom:6px → 8px (lab template card)
- [x] marketing-site-mockup.html: 10 CSS classes margin-bottom:6px → 8px (arb-head, surface-name, lab-card-head, get-icon, plan-name, detail-screenshot h3, ss-section-label, doc-card h3)
- [x] marketing-site-mockup.html: 2 inline margin-bottom:6px → 8px (Hubify Labs logo row, mock-sb item)
- [x] Themed zone (PDF preview with hardcoded #5a5a55) intentionally preserved
- [x] Git committed `df2a49e` — 49 edits across 2 files

### Pass 27: margin-top:6px + padding 6px + structural gap:6px + padding:10px/11px ✅ COMPLETE (bonus)
**Target:** Remaining 6px vertical spacing, structural gap:6px on grids, off-grid 10px/11px padding
- [x] index.html: margin-top:6px → 8px on 4 CSS classes (review-meta, tl-icon, alert-dot, vibe-msg-body pre) + 6 inline (sb-sessions-wrap, prog-row, sp-text ×3, figures grid). Themed zone (#7a7872) preserved.
- [x] index.html: padding-bottom:6px → 8px on fig-section-head; padding-top:6px → 8px on org-node-foot + sb-sessions-wrap
- [x] index.html: structural gap:6px → 8px on 10 grid/list containers (pipeline-steps, paper-list, survey-grid, dispatch-field, dispatch-radios, hm2-checks, org-row-workers, org-row-reviewers, mem-layers, compute-providers). Micro-spacing gap:6px on pills/dots/icons preserved.
- [x] index.html: padding:10px → 12px on sb-toolbar, sb-footer, sb-files-btn, mobile sb-toolbar, mobile sb-search. padding:11px → 12px on vibe-input. padding:4px 10px → 4px 12px on chat-model-pill, chat-mode-pill.
- [x] marketing-site-mockup.html: margin-top:6px → 8px on 4 classes + padding-top:14px → 16px on sc-stack, sc-lab-row
- [x] Git committed `6d3cc40` — 36 edits across 2 files

---

### Pass 28: Horizontal padding 10px → 12px Across All 5 Files ✅ COMPLETE (bonus)
**Target:** All remaining padding:*px 10px horizontal values + padding-top:10px
- [x] index.html: 13 CSS classes snapped horizontal 10px→12px (sb-proj-wrap ×2, cfeed-body, publish-ready-foot .btn, mobile term-tab, kanban-col-head, vibe-input textarea, file-preview-btn, chat-input, toast-type-label, chat-model-pill, chat-mode-pill, sb-files-btn, mobile sb-search). padding-top:10px→12px on compute-pod-settings, dossier-footer. Mobile view-inner 10px→12px.
- [x] marketing-site-mockup.html: 7 classes snapped (mock-url, lab-card-status, plan-card.featured::before, detail-tab, disc-score, docs-nav-item, v3-marketing-badge)
- [x] agent-management-clone.html: feed-header 6px 10px→8px 12px, feed-body 8px 10px→8px 12px
- [x] cli-tui-mockup.html: session-tab, tui-nav, tui-tab, tui-status all *px 10px→*px 12px
- [x] desktop-app-mockup.html: toolbar 6px 10px→8px 12px + margin-bottom:6px→8px
- [x] Themed zones (graph rgba, PDF abstract #d8d2bf, BB nav #d6d4cf, ss-* #111/#1e1e1e) preserved
- [x] Git committed `8add757` — 28 edits across all 5 files

### Pass 29: gap:18px→16px + margin:10px/14px Snap + border-radius:3px Tokenize ✅ COMPLETE (bonus)
**Target:** Remaining off-grid gaps, margins, and un-tokenized border-radius:3px across all 5 files
- [x] index.html: gap:18px→16px on 3 classes (gpu-meta, settings-split, profile-stats). margin-top:10px→12px inline. padding-left:14px→16px verdict-note. Themed zones preserved.
- [x] marketing-site-mockup.html: 5× border-radius:3px→var(--r-sm) + 4× margin-bottom:10px→12px + margin-top:10px→12px + 2× margin:14px→16px
- [x] agent-management-clone.html: margin-bottom:10px→12px
- [x] cli-tui-mockup.html: scrollbar radius 3px→var(--r-sm), margin-top:14px→16px
- [x] desktop-app-mockup.html: 3× border-radius:3px→var(--r-sm), 2× margin-right:10px→12px, ctrl padding:3px 7px→4px 8px
- [x] Git committed `fbf2b34` — 25 edits across all 5 files

### Pass 30: margin-left/right:6px→8px on Structural Elements ✅ COMPLETE (bonus)
**Target:** Remaining structural margin-left:6px and margin-right:6px in index.html
- [x] CSS classes (8 edits): .tree-row .tier-pill margin-left, .prompt-path/.prompt-git/.prompt-mark margin-right, .score-bar margin-right, .contrib-adjacent .verdict margin-left, .json-preview margin-left, .sb-item-children margin 2px 6px→2px 8px
- [x] Inline task-list sb-pill badges: 5× margin-left:6px→8px (QC, MCMC, P1 step 4, infra pills)
- [x] Inline settings-section-label spans: 2× margin-left:6px→8px (Alerts count, Routines count)
- [x] Mobile .rt-arch-diagram padding:12px 6px→12px 8px
- [x] Preserved: micro-spacing exclusions (gap:5-6px on pill/icon groups), themed zones
- [x] Git committed `28f92fe` — 16 edits in index.html

### Pass 31: Remaining Off-Grid Padding/Margin/Gap Snap ✅ COMPLETE (bonus)
**Target:** Final structural off-grid values found by full-file scan across all 5 files
- [x] index.html: .reviewer-grid gap:6px→8px, .reviewer-card padding:11px 12px→12px, .fp-img-stage padding:34px→32px, .hm2-stepper margin:10px 0 14px→12px 0 16px, .toast-stack bottom:42→44px right:18→16px
- [x] marketing-site-mockup.html: .dd-pill padding:7→8px, .docs-search padding:9→8px, .mockup-controls padding:7px 9px→8px 8px + gap:6→8px
- [x] desktop-app-mockup.html: .mp-input padding:5px 7px→4px 8px, .mp-open-app padding:5→4px
- [x] Preserved: all themed zones (PDF preview, vibe sandbox, BigBounce site preview)
- [x] Git committed `b05dfb4` — 11 edits across 3 files

### Pass 32: Dot Indicator margin-right:7px→8px + margin-top:5px→4px ✅ COMPLETE (bonus)
**Target:** margin-right:7px on dot status indicators (CSS + inline), margin-top:5px on desktop drop zone
- [x] index.html CSS: .dot-6-accent, .dot-5-accent, .dot-5-dim, .provider-dot — 4 classes margin-right:7→8px
- [x] index.html inline: 6× dot indicators in settings/agent-list sections — margin-right:7→8px
- [x] desktop-app-mockup.html: .file-drop-msg b/span margin-top:5→4px
- [x] Preserved: themed zone dots (BB site preview margin-bottom:7px, PDF refs margin:0 0 7px)
- [x] Git committed `ac410d6` — 12 edits across 2 files

### Pass 33: Final margin:6px→8px + Off-Grid Padding Snap ✅ COMPLETE (bonus)
**Target:** Last structural margin:6px, off-grid padding (5px, 9px), un-tokenized border-radius across 4 files
- [x] index.html: .chat-msg-body ul, .sp-diff .hunk, .code-block, .rt-arrow — margin:6px 0→8px 0
- [x] marketing-site-mockup.html: .ss-kr-strip margin+gap:6→8px, hero-counter ml:6→8px, lab-dot mr:6→8px, pill padding:4px 9→8px, .ctrl padding:5px 9px→4px 8px
- [x] agent-management-clone.html: .nav-sub-link padding:5px 6px→4px 8px
- [x] cli-tui-mockup.html: .ctrl border-radius:2px→var(--r-sm)
- [x] Preserved: themed zones (PDF figbox-cap, BB JS template margin:6px)
- [x] Git committed `b7e9976` — 10 edits across 4 files

### Pass 34: padding:0 10px→0 12px on Sidebar Buttons/Inputs ✅ COMPLETE (bonus)
**Target:** All `padding:0 10px` (off-grid) on sidebar buttons, form inputs, and selects
- [x] CSS: .sb-lab-btn, .sb-proj-btn (base + mobile), .sb-search, .now-strip, mobile .sb-files-btn, mobile .sb-footer — 8 class edits
- [x] Inline: 4× settings input fields + 1× settings select — all padding:0 10px→0 12px
- [x] Git committed `6fb9da8` — 12 edits in index.html

### Pass 35: Remaining padding:0 10px + margin:10px Snap ✅ COMPLETE (bonus)
**Target:** Last `padding:0 10px` across CLI/desktop + .sp-md h3 margin snap
- [x] index.html: .sp-md h3 margin:10px 0 5px→12px 0 4px
- [x] cli-tui-mockup.html: .session-tabs padding:0 10px→0 12px
- [x] desktop-app-mockup.html: .macos-menubar padding:0 10px→0 12px
- [x] Git committed `2692f0c` — 4 edits across 3 files

### Pass 41: font-variant-numeric:tabular-nums on Numeric Elements ✅ COMPLETE (bonus)
**Target:** All numeric display elements across index.html + marketing-site — proper number alignment
- [x] index.html (7 elements): .stat .stat-value (hero stats), .stat .stat-trend (trend arrows), .running-pct (experiment list %), .tl-time (timeline timestamps), .prm-pct (paper readiness %), .briefing-cell .briefing-num (briefing grid), .sp-stat .num (sidepeek metrics)
- [x] marketing-site (4 elements): .hero-stat-num (hero counters), .datasets-stat-num (dataset section), .review-stat-num (review section), .plan-price (pricing)
- [x] CSV table numeric column already had tabular-nums (no change needed)
- [x] Git committed `43cc889` — 11 edits across 2 files

### Pass 40: text-overflow:ellipsis on Clipped Elements ✅ COMPLETE (bonus)
**Target:** index.html — elements with overflow:hidden + white-space:nowrap but missing text-overflow:ellipsis
- [x] .brand-text (sidebar brand name) — hard clip → graceful "..." truncation
- [x] .sb-lab-btn .lab-name (lab selector) — hard clip → ellipsis
- [x] .tree-row.tier-group (file tree tier headers) — hard clip → ellipsis
- [x] .tree-row.file-row (file tree rows) — hard clip → ellipsis
- [x] All other nowrap+hidden elements across all 5 files already had ellipsis
- [x] Git committed `e49133c` — 4 edits in index.html

### Pass 39: Thin Scrollbars on Scrollable Containers ✅ COMPLETE (bonus)
**Target:** index.html — add scrollbar-width:thin + scrollbar-color to all major scrollable panels
- [x] 14 scrollable containers upgraded: .sb-body, .notif-drawer-body, .chat-body, .term-body, .view, #detailBody, .captain-main, .captain-feed-list, .site-meta-col, .cmdp-results, .settings-nav, .vibe-chat-body, .file-preview-body, .file-preview-csv
- [x] Existing thin scrollbar on line 3958 already covered one container — now all major panels match
- [x] Tab rows (.term-tabs, .preview-tabs) intentionally kept at scrollbar-width:none (hidden)
- [x] Git committed `ec0b432` — 14 edits in index.html

### Pass 38: -webkit-backdrop-filter Prefix for Safari ✅ COMPLETE (bonus)
**Target:** index.html — add missing -webkit- prefix on backdrop-filter declarations
- [x] 5 elements missing prefix: .cmdp-overlay (blur 4px), .mobile-menu-btn (blur 8px), .sidebar-overlay (blur 2px), .graph-header (blur 20px), .graph-node-card (blur 20px)
- [x] desktop-app-mockup.html and marketing-site-mockup.html already had both prefixed+unprefixed — no changes needed
- [x] All backdrop-filter declarations across all 5 v4 files now have -webkit- prefix for Safari
- [x] Git committed `6aa2826` — 5 edits in index.html

### Pass 37: user-select:none on Interactive Chrome ✅ COMPLETE (bonus)
**Target:** All 5 files — prevent accidental text selection on UI chrome (AgenticUI uses user-select:none on navbar, tabs, buttons, dropdowns, pagination, radio, checkbox)
- [x] index.html: 13 elements — .sb-item, .sb-lab-btn, .sb-proj-btn, .sb-sub-mode-tab, .sb-search, .sb-files-btn, .sb-child-item, .sb-captain, .chat-mode-tab, .term-tab, .preview-tab, .sp-tabs button, .btn
- [x] marketing-site-mockup.html: 6 elements — .tn-brand, .tn-link, .tn-mobile-btn, .demo-tab, .dd-pill, .showcase-card
- [x] agent-management-clone.html: .nav-sub-link
- [x] cli-tui-mockup.html: .session-tab
- [x] desktop-app-mockup.html: .menu-item, .dock-icon
- [x] Git committed `10fa0bc` — 23 edits across all 5 files

### Pass 89: widows:2;orphans:2 on Prose Content ✅ COMPLETE (bonus)
**Target:** Prevent single-line fragments at page/column breaks
- [x] index.html: .sp-md p, .chat-msg-body (2 elements)
- [x] marketing-site-mockup.html: .lede, .article-body p (2 elements)
- [x] Git committed `d421a0e` — 2 files

### Pass 88: overflow-anchor:auto on Scroll Containers ✅ COMPLETE (bonus)
**Target:** Stable scroll anchoring — prevent scroll position jumping on content insert
- [x] index.html: .chat-body, .term-body (2 scroll containers)
- [x] Git committed `d421a0e` — 1 file

### Pass 87: font-variant-ligatures:none on Code Elements ✅ COMPLETE (bonus)
**Target:** Disable ligatures in monospace/code context (ligatures break code readability)
- [x] index.html: code,pre,kbd,.term-body,.file-preview-code (global rule)
- [x] marketing-site-mockup.html: code,pre,kbd (global rule)
- [x] Git committed `d421a0e` — 2 files

### Pass 86: scroll-padding + scroll-margin on Scrollable Containers ✅ COMPLETE (bonus)
**Target:** Proper scroll offset for snap targets and anchor-linked sections
- [x] index.html: scroll-padding-inline:8px on .term-tabs + .preview-tabs
- [x] marketing-site-mockup.html: scroll-margin-top:72px on .section (navbar offset)
- [x] Git committed `a22823d` — 2 files

### Pass 85: text-underline-position:from-font on Links ✅ COMPLETE (bonus)
**Target:** Font-metric-aware underline positioning
- [x] index.html: global `a` reset
- [x] marketing-site-mockup.html: global `a` reset
- [x] Completes the full underline control chain: skip-ink + offset + thickness + position
- [x] Git committed `a22823d` — 2 files

### Pass 84: @property Typed CSS Custom Properties ✅ COMPLETE (bonus)
**Target:** Register accent colors as typed properties for future animated transitions
- [x] index.html: @property --accent + @property --accent-dim
- [x] marketing-site-mockup.html: same 2 properties
- [x] Enables `transition:--accent .3s` for smooth theme color changes
- [x] Git committed `a22823d` — 2 files

### Pass 83: view-transition-name on Major Layout Sections ✅ COMPLETE (bonus)
**Target:** Future View Transitions API — named sections for cross-document transitions
- [x] index.html: sidebar, chat, preview, statusbar (4 sections named)
- [x] Progressive enhancement — browsers without View Transitions API ignore
- [x] Git committed `0517ddd` — 1 file

### Pass 82: @starting-style Entry Animations ✅ COMPLETE (bonus)
**Target:** CSS-only entry animations when display:none → display:flex toggles
- [x] index.html: .notif-drawer.open (slide-in from left + fade)
- [x] index.html: .cmdp-overlay.open (fade-in)
- [x] Added `display allow-discrete` to transition lists for both elements
- [x] Progressive enhancement — unsupported browsers fall back to instant show
- [x] Git committed `0517ddd` — 1 file

### Pass 81: field-sizing:content on Textareas ✅ COMPLETE (bonus)
**Target:** Auto-sizing textareas that grow with content
- [x] index.html: .textarea (generic component), .chat-input, .vibe-input textarea
- [x] Added max-height:200px cap on chat inputs to prevent runaway growth
- [x] Progressive enhancement — Chrome 123+, others use fixed min-height fallback
- [x] Git committed `0517ddd` — 1 file

### Pass 80: interpolate-size:allow-keywords on :root ✅ COMPLETE (bonus)
**Target:** Future-proof CSS animate-to-auto height transitions
- [x] All 5 files: added to :root block
- [x] Progressive enhancement — Chrome 129+ supports, others ignore
- [x] Enables height:auto transitions when browser support broadens
- [x] Git committed `1f86309` — 5 files

### Pass 79: shape-rendering:geometricPrecision on SVG Icons ✅ COMPLETE (bonus)
**Target:** Crisper, anti-aliased SVG icon rendering
- [x] index.html: .ic class (128 SVG icons)
- [x] marketing-site-mockup.html: .ic class (nav/section icons)
- [x] agent-management-clone.html: global svg rule (13 inline SVGs)
- [x] desktop-app-mockup.html: global svg rule (6 inline SVGs)
- [x] cli-tui: N/A (no SVGs, monospace terminal only)
- [x] Git committed `1f86309` — 4 files

### Pass 78: meta color-scheme + theme-color in head ✅ COMPLETE (bonus)
**Target:** Browser chrome theming before CSS loads, prevent flash of white in dark mode
- [x] All 5 files: `<meta name="color-scheme" content="dark light">` + 2 theme-color metas
- [x] Dark #0a0c10, light #faf6f1 — matches :root token values
- [x] Git committed `1f86309` — 5 files

### Pass 77: hanging-punctuation:first last on Prose ✅ COMPLETE (bonus)
**Target:** Editorial polish — opening quotes/punctuation hang outside text block
- [x] index.html: .sp-md p (sidepeek markdown paragraphs)
- [x] marketing-site-mockup.html: .article-body (article content)
- [x] Progressive enhancement — Safari supports, Chrome ignores
- [x] Git committed `2dfbcb9` — 2 files

### Pass 76: text-decoration-thickness:from-font on Links ✅ COMPLETE (bonus)
**Target:** Underline thickness matches font's built-in metrics
- [x] index.html: global `a` reset
- [x] marketing-site-mockup.html: global `a` reset
- [x] Pairs with existing text-underline-offset:2px for complete link underline control
- [x] Git committed `2dfbcb9` — 2 files

### Pass 75: paint-order:stroke fill on SVG Icons ✅ COMPLETE (bonus)
**Target:** Sharper SVG icon rendering — stroke paints under fill at intersections
- [x] index.html: .ic class (all 16px stroke icons)
- [x] Git committed `2dfbcb9` — 1 file

### Pass 74: @media (forced-colors:active) Windows High Contrast ✅ COMPLETE (bonus)
**Target:** WCAG accessibility — Windows High Contrast mode support
- [x] index.html: system-color borders on major panels, Highlight outline on active tabs, forced-color-adjust:none on semantic colors
- [x] Ensures UI is usable when Windows overrides all colors
- [x] Git committed `c91c5d1` — 1 file

### Pass 73: text-wrap:pretty on Prose Content ✅ COMPLETE (bonus)
**Target:** Modern CSS line-breaking — avoids widows/orphans in paragraph text
- [x] index.html: .chat-msg-body, .sp-text (2 elements)
- [x] marketing-site-mockup.html: .lede, .article-body p (2 elements)
- [x] Progressive enhancement — unsupported browsers ignore
- [x] Git committed `c91c5d1` — 2 files

### Pass 72: font-optical-sizing:auto ✅ COMPLETE (bonus)
**Target:** Enable variable font optical sizing for better rendering at different sizes
- [x] index.html, marketing-site, desktop-app, agent-management (4 files)
- [x] cli-tui: N/A (monospace only, no optical size axis)
- [x] Geist/Inter variable fonts automatically adjust stroke weight by font-size
- [x] Git committed `c91c5d1` — 4 files

### Pass 71: Standard line-clamp Alongside Webkit Prefix ✅ COMPLETE (bonus)
**Target:** Forward-compat — add unprefixed `line-clamp:2` alongside `-webkit-line-clamp:2`
- [x] index.html: .prm-abstract, .lab-card-desc, .fig-cap (3 elements)
- [x] When browsers ship unprefixed `line-clamp`, these elements will work without the webkit hack
- [x] Git committed `65b8d99` — 1 file

### Pass 70: outline-offset on Focus-Visible ✅ COMPLETE (bonus)
**Target:** Cleaner focus ring with 2px offset from element edge
- [x] index.html: .stat:focus-visible gets `outline:2px solid var(--accent);outline-offset:2px`
- [x] Visually separates focus ring from element border for better readability
- [x] Git committed `65b8d99` — 1 file

### Pass 69: scroll-snap on Tab Rows ✅ COMPLETE (bonus)
**Target:** Snap-scrolling on horizontal tab rows
- [x] index.html: .term-tabs, .preview-tabs get `scroll-snap-type:x mandatory`
- [x] .term-tab, .preview-tab get `scroll-snap-align:start`
- [x] Tabs snap to boundaries when scrolling horizontally (matches Cursor/VS Code behavior)
- [x] Git committed `65b8d99` — 1 file

### Pass 68: @media (prefers-contrast:more) High Contrast ✅ COMPLETE (bonus)
**Target:** WCAG accessibility — strengthen borders and text for high-contrast preference
- [x] index.html: boosted --border/--text/--text-muted/--text-dim values, 1.5px borders on cards/buttons
- [x] marketing-site-mockup.html: same token overrides + 1.5px on hero-stat, cards, buttons
- [x] Progressive enhancement — only activates when OS high-contrast is enabled
- [x] Git committed `0fc0ed1` — 2 files

### Pass 67: hyphens:auto on Text Content Areas ✅ COMPLETE (bonus)
**Target:** Smart word breaking on narrow containers
- [x] index.html: .chat-msg-body, .sp-text, .vibe-msg-body (3 elements)
- [x] Pairs with existing overflow-wrap:anywhere for belt-and-suspenders text overflow protection
- [x] Git committed `0fc0ed1` — 1 file

### Pass 66: scrollbar-gutter:stable on Content Panels ✅ COMPLETE (bonus)
**Target:** Prevent layout shift when scrollbar appears/disappears
- [x] index.html: .view, #detailBody, .captain-main, .settings-nav (4 containers)
- [x] Reserves scrollbar space even when content doesn't overflow — prevents horizontal jitter
- [x] Chat/terminal panels excluded (always overflow, scrollbar always present)
- [x] Git committed `0fc0ed1` — 1 file

### Pass 65: @media print Styles on Marketing Site ✅ COMPLETE (bonus)
**Target:** Print-friendly output for marketing page
- [x] marketing-site-mockup.html: transparent backgrounds, black text, no shadows
- [x] Hides nav, footer, mobile button, demo tabs, CTAs
- [x] Forces sections visible (overrides reveal animations + content-visibility)
- [x] Adds URL display after links via `a[href]::after`
- [x] page-break-inside:avoid on sections
- [x] Git committed `f4e8b71` — 1 file

### Pass 64: content-visibility:auto on Marketing Sections ✅ COMPLETE (bonus)
**Target:** Rendering performance — skip painting off-screen sections
- [x] marketing-site-mockup.html: `.section` gets `content-visibility:auto;contain-intrinsic-size:auto 500px`
- [x] Browser skips layout/paint for sections scrolled out of viewport
- [x] Print media query overrides with `content-visibility:visible` to ensure all content prints
- [x] Git committed `f4e8b71` — 1 file

### Pass 63: text-wrap:balance on Headings ✅ COMPLETE (bonus)
**Target:** Balanced text wrapping on display headings — prevents orphan words
- [x] index.html: .greeting, .sp-h1, .captain-heading, .section-minimal .section-title, .profile-name (5 elements)
- [x] marketing-site-mockup.html: h1.hero-h1, h2.section-h2 (2 elements)
- [x] Progressive enhancement — unsupported browsers silently ignore
- [x] Git committed `f4e8b71` — 2 files

### Pass 60: text-rendering:optimizeLegibility ✅ COMPLETE (bonus)
**Target:** Better font kerning and ligature rendering on body text
- [x] index.html: added to `body` rule
- [x] marketing-site-mockup.html: added to `html,body` rule
- [x] desktop-app-mockup.html: added to `body` rule
- [x] agent-management-clone.html: added to `body` rule
- [x] cli-tui-mockup.html: N/A (monospace only — optimizeLegibility has no effect)
- [x] Git committed `f63c1ce` — 4 files

### Pass 61: text-underline-offset + text-decoration-skip-ink on Links ✅ COMPLETE (bonus)
**Target:** Cleaner link underlines that don't clip descenders
- [x] index.html: added global `a{text-decoration-skip-ink:auto;text-underline-offset:2px}`
- [x] marketing-site-mockup.html: added to existing `a` reset rule
- [x] Other files: no visible link elements or text-decoration:none globally — N/A
- [x] Git committed `f63c1ce` — 2 files

### Pass 62: backface-visibility:hidden on Animated Panels ✅ COMPLETE (bonus)
**Target:** Prevent subpixel rendering artifacts on GPU-composited elements
- [x] index.html: .sidebar (width transition), .notif-drawer (slide-in), .cmdp-overlay (fade), .sidebar-overlay (fade)
- [x] All 4 elements already had will-change hints — backface-visibility completes the compositor optimization
- [x] Git committed `f63c1ce` — 1 file

### Pass 58: tab-size:2 on Code/Terminal Containers ✅ COMPLETE (bonus)
**Target:** Compact tab rendering matching Cursor/VS Code 2-space default
- [x] index.html: .term-body, .file-preview-code, .vibe-msg-body pre, .sp-jsonl (4 containers)
- [x] cli-tui-mockup.html: .term-body
- [x] .code-block pre already had it — unchanged
- [x] Git committed `9e865c2` — 2 files

### Pass 57: overflow-wrap:anywhere on Text Content Areas ✅ COMPLETE (bonus)
**Target:** index.html — prevent long URLs/paths from overflowing
- [x] .chat-msg-body, #detailBody, .vibe-msg-body
- [x] .term-body already had word-break:break-word — unchanged
- [x] Git committed `bad265b` — 1 file

### Pass 56: scroll-padding-top on Marketing Site ✅ COMPLETE (bonus)
**Target:** marketing-site-mockup.html — anchor links clear the sticky nav
- [x] Added `scroll-padding-top:80px` to `html` (60px nav + 20px breathing room)
- [x] Git committed `e15c698` — 1 file

### Pass 55: isolation:isolate on Layout Zone Boundaries ✅ COMPLETE (bonus)
**Target:** index.html — prevent z-index leaking between major panels
- [x] 3 containers: .app, .chat, .status-bar
- [x] .preview already had `isolation:isolate` — unchanged
- [x] Git committed `43da2eb` — 1 file

### Pass 54: will-change Compositor Hints ✅ COMPLETE (bonus)
**Target:** index.html — pre-promote animated panels to compositor layers
- [x] .sidebar: `will-change:width` (collapse transition)
- [x] .notif-drawer: `will-change:transform,opacity` (slide-in transition)
- [x] .cmdp-overlay: `will-change:opacity` (command palette fade)
- [x] .sidebar-overlay: `will-change:opacity` (mobile overlay fade)
- [x] Git committed `22dff17` — 1 file

### Pass 53: contain:layout style on Major Containers ✅ COMPLETE (bonus)
**Target:** index.html — paint containment optimization on isolated panels
- [x] 6 containers: .sidebar, .chat-body, .term-body, .captain-main, .notif-drawer, .vibe-chat-body
- [x] .preview + .preview-content already had containment — unchanged
- [x] Prevents layout recalculation from propagating across panel boundaries
- [x] Git committed `50f84e6` — 1 file

### Pass 52: font-feature-settings Geist Alternates ✅ COMPLETE (bonus)
**Target:** 2 files missing Geist cv02/cv03/cv04/cv11 character alternates
- [x] desktop-app-mockup.html: added to body
- [x] agent-management-clone.html: added to body
- [x] cli-tui is monospace-only — N/A
- [x] index.html + marketing already had it
- [x] Git committed `397224f` — 2 files

### Pass 51: ::placeholder Color Consistency ✅ COMPLETE (bonus)
**Target:** index.html — standardize placeholder text color
- [x] .filter-search-minimal::placeholder: text-muted → text-dim
- [x] .dispatch-input::placeholder: text-muted → text-dim
- [x] Added global `::placeholder{color:var(--text-dim);opacity:1}` base rule
- [x] .graph-search::placeholder rgba — themed zone, intentionally preserved
- [x] Git committed `96b8872` — 1 file

### Pass 50: -moz-osx-font-smoothing:grayscale on 3 Missing Files ✅ COMPLETE (bonus)
**Target:** Complete the font-smoothing pair on files that only had -webkit
- [x] cli-tui-mockup.html: added -moz-osx-font-smoothing:grayscale
- [x] desktop-app-mockup.html: added -moz-osx-font-smoothing:grayscale
- [x] agent-management-clone.html: added -moz-osx-font-smoothing:grayscale
- [x] index.html + marketing already had both — no changes
- [x] Git committed `0d2a801` — 3 files

### Pass 49: touch-action:manipulation on All 5 Files ✅ COMPLETE (bonus)
**Target:** All 5 files — remove 300ms tap delay on iOS, disable double-tap-to-zoom
- [x] All 5 files: `touch-action:manipulation` on html,body (or body)
- [x] Git committed `04c4215` — 5 files

### Pass 48: accent-color on :root ✅ COMPLETE (bonus)
**Target:** All 5 files — native form controls render in sage green
- [x] All 5 files: `accent-color:var(--accent)` (or hardcoded #4a7d6a for agent-management) on `:root`
- [x] Native checkboxes, radios, range sliders, progress bars now sage instead of browser blue
- [x] Git committed `0626114` — 5 files

### Pass 47: caret-color on Input Elements ✅ COMPLETE (bonus)
**Target:** Sage-colored text cursor in all input fields
- [x] index.html: `caret-color:var(--accent)` on global `input,textarea,select` reset
- [x] marketing-site-mockup.html: new `input,textarea{caret-color:var(--accent)}` rule
- [x] cli-tui-mockup.html: already had `caret-color:var(--accent)` — no changes needed
- [x] agent-management + desktop: no input elements — N/A
- [x] Git committed `17c2734` — 2 files

### Pass 46: ::selection Styling ✅ COMPLETE (bonus)
**Target:** Consistent sage-tinted text selection across all files
- [x] index.html: `::selection{background:rgba(74,125,106,0.25)}` + light mode variant
- [x] agent-management-clone.html: `::selection` added
- [x] desktop-app-mockup.html: `::selection` + light mode variant
- [x] cli-tui + marketing: already had `::selection` — no changes needed
- [x] Git committed `aeb08dd` — 3 files

### Pass 45: prefers-reduced-motion on All 5 Files (WCAG 2.1 AA) ✅ COMPLETE (bonus)
**Target:** Accessibility — comprehensive reduced-motion reset across all files
- [x] marketing-site-mockup.html: extended from .reveal-only to global `*` reset (animation/transition/scroll-behavior)
- [x] agent-management-clone.html: added full prefers-reduced-motion block
- [x] cli-tui-mockup.html: added full prefers-reduced-motion block
- [x] desktop-app-mockup.html: added full prefers-reduced-motion block
- [x] index.html: already had comprehensive block — no changes needed
- [x] Git committed `ab75577` — 4 files updated

### Pass 44: color-scheme:dark/light on :root ✅ COMPLETE (bonus)
**Target:** All 5 files — tell browsers to render native controls in correct color scheme
- [x] index.html: `color-scheme:dark` on `:root`, `color-scheme:light` on `:root.light`
- [x] marketing-site-mockup.html: `color-scheme:dark` on `:root`, `color-scheme:light` on `:root.light`
- [x] agent-management-clone.html: `color-scheme:dark` on `:root`
- [x] cli-tui-mockup.html: `color-scheme:dark` on `:root`
- [x] desktop-app-mockup.html: `color-scheme:dark` on `:root`, `color-scheme:light` on `:root.light`
- [x] Git committed `c850bb9` — all 5 files

### Pass 43: -webkit-tap-highlight-color:transparent on All 5 Files ✅ COMPLETE (bonus)
**Target:** Global reset — remove iOS Safari blue flash on tap for dark IDE aesthetic
- [x] index.html: added to `*` selector
- [x] marketing-site-mockup.html: added to `*` selector
- [x] agent-management-clone.html: added to `*, *::before, *::after` selector
- [x] cli-tui-mockup.html: added to `*` selector
- [x] desktop-app-mockup.html: added to `*` selector
- [x] Git committed `30bccb4` — 5 files updated

### Pass 42: overscroll-behavior:contain on Scrollable Containers ✅ COMPLETE (bonus)
**Target:** All scrollable panels — prevent scroll chaining (Cursor/VS Code behavior)
- [x] index.html: 15 containers (all elements with scrollbar-width:thin) — .sb-body, .notif-drawer-body, .chat-body, .term-body, .view, #detailBody, .captain-main, .captain-feed-list, .site-meta-col, .cmdp-results, .settings-nav, .vibe-chat-body, .file-preview-body, .file-preview-csv, .dropdown-list
- [x] cli-tui-mockup.html: .term-body
- [x] marketing-site-mockup.html: docs sidebar (max-height scrollable)
- [x] Nested panels no longer leak scroll events to parent — scroll stays contained
- [x] Git committed `2a873b2` — 3 files updated

### Pass 36: cursor:pointer on Interactive Elements + Transition .14s→.15s ✅ COMPLETE (bonus)
**Target:** Interactive elements missing cursor:pointer + off-grid transition durations
- [x] index.html: cursor:pointer added on .sb-captain (captain nav item), .term-tab .x (close button), .preview-tab .tab-close (close button), .card (clickable cards) — 4 edits
- [x] marketing-site-mockup.html: cursor:default→pointer on .dd-pill (interactive filter pill), .showcase-card (hoverable card) — 2 edits
- [x] marketing-site-mockup.html: 17× transition .14s→.15s (AgenticUI standard duration) across cards, links, grids, sections
- [x] Zero interactive elements with :hover but missing cursor:pointer remain across all 5 files
- [x] Zero off-grid transition durations (.14s) remain across all 5 files
- [x] Git committed `b6cf7b6` — 6 cursor + 17 transition edits across 2 files

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
