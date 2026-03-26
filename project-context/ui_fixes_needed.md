# UI Fixes Needed — 2026-03-26

## Critical Layout Bugs

### 1. data-explorer.html — BLANK PAGE
The data-explorer page shows only sidebar + empty content area. This likely broke when nav.js was updated — the page uses its own sidebar layout (`.explorer { display: flex; }`) and the injected nav.js sidebar is conflicting. The page's own hardcoded sidebar may have been overridden.

**Fix:** Check if nav.js is double-injecting a sidebar on top of data-explorer's built-in sidebar. The page has its own `.sidebar` class that conflicts with nav.js's sidebar.

### 2. anomaly-explorer.html — Double sidebar gap
Content is pushed right by a sidebar-width gap. The page loads `nav.js` (which injects a sidebar) but the main content doesn't account for it. Need to wrap content in the `.site-content` div that other pages use.

**Fix:** Add the `<div class="site-content">` wrapper around `<main>` like other pages have.

## Feature Requests (from user)

### 3. Replace modals with sidepeak/slideout panel
User prefers a right-side slideout panel instead of centered modal for anomaly details. More elegant, scalable as we add more content. Keep the same data (image, AI analysis, review notes) but in a slide-in panel.

### 4. Glossary/definitions inline on anomaly explorer
The glossary section was added to the HTML but may be below the fold. User wants:
- Score tier legend visible near the table
- Column definitions in a collapsible section
- Astronomy terms (AGN, QSO, etc.) as tooltips or a quick-reference sidebar
- Enhanced AI Analysis text with more detail on what each anomaly means

### 5. Enhanced AI Analysis on verified anomalies
For the objects confirmed as NOT in SIMBAD/NED:
- Add more detailed analysis of what each could be
- Add tags/labels (HIGH_Z_CANDIDATE, UNUSUAL_AGN, etc.)
- Look for patterns across anomalies
- What does the collective data tell us?
- Add significance context for each image

### 6. Methodology page accessible from nav
methodology-anomaly.html is now in the sidebar under data/ but needs testing.

## Batch Processing Status
- 36,700/195,829 (18.7%) anomalies classified and uploaded to Convex
- Script running in background, checkpointing every 10 min
- Will complete in ~5 more hours

## Bulk Cross-Match Status
- CDS services (xMatch, VizieR TAP, SIMBAD TAP) are globally down
- Script `bulk_cross_match_all.py` is ready to run when they recover
- Need to cross-match ALL 195K against: AllWISE, SIMBAD, Gaia DR3, SDSS DR16, Milliquas
- Currently only top 50-100 checked (SIMBAD: 0/100, NED: 3/50)
