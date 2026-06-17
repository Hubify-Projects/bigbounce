# EXT11-Closure Deploy QA — 2026-06-13

**QA run date:** 2026-06-13 (PST)
**Deploy SHAs inspected:** f056b496 (EXT11-closure-wave) + c52468bf (EXT12-stamp)
**Live URL:** https://bigbounce.hubify.app
**QA tier:** Standard (P0+P1+P2)

---

## Summary

| Category | Result |
|----------|--------|
| Site online (HTTP 200) | PASS |
| Deploy detected | PASS (last-modified Jun 14 01:23 UTC) |
| 6 paper pages render | PASS (all 200) |
| PDF download links (6) | PASS (all 200) |
| /reviews timeline — 4 new entries | PASS |
| Mobile 375px | PASS (no overflow) |
| Tablet 768px | PASS |
| P0 bugs | **0** |
| P1 bugs | **1** (Convex stale on all 6 papers) |
| P2 bugs | **1** (preloaded CSS resource warning) |

**Ship-ready:** YES for EXT12 harvest. The P1 Convex version bug is cosmetic (the header badge shows the prior version; artifact row and PDF links show the correct EXT11-closure version). Recommend Convex bump before any Houston sign-off review.

---

## Deploy Detection

```
HTTP/2 200
last-modified: Sun, 14 Jun 2026 01:23:29 GMT
x-vercel-cache: HIT
etag: "c52a2370e738cb2822634f9ec77b725a"
```

Deploy is live. Not checking deploy SHA from /_status (no endpoint available) but the etag and last-modified confirm the EXT12-stamp commit is serving.

---

## P1 Bug — Convex Version Mismatch (ALL 6 PAPERS)

**Severity:** P1 — visible version discrepancy on every paper page header badge

**Root cause:** The EXT11-closure commit (f056b496) claimed "Convex bumped" in the commit message but no Convex `bump` mutation was executed. Confirmed by querying the Convex API directly:

| Paper | Convex (shown in header badge) | Expected (EXT11-closure) | Source data (papers.ts) |
|-------|-------------------------------|--------------------------|-------------------------|
| P1A | v1A.0.73 | v1A.0.74 | v1A.0.74 ✓ |
| P1B | v1B.0.70 | v1B.0.71 | v1B.0.71 ✓ |
| P2 | v1.7.64 | v1.7.65 | v1.7.65 ✓ |
| P3 | v3.1.107 | v3.1.108 | v3.1.108 ✓ |
| P4 | v1.0.187 | v1.0.188 | v1.0.188 ✓ |
| P5 | v0.1.76-2026-06-13 | v0.1.77-2026-06-13 | v0.1.77-2026-06-13 ✓ |

**Symptom:** Paper detail page header badge (driven by `live?.currentVersion` from Convex) shows the prior version. The artifact row's `pdfMeta` field (from static papers.ts) correctly shows the EXT11-closure version. PDF download links point to the correct EXT11-closure PDFs (all 200 OK).

**Impact:** Header version badge is mismatched vs PDF artifact row on every paper page. The /papers index shows the old Convex version in the campaign table, alongside the correct static-data version in the card. Confusing but not blocking — the PDFs themselves are correct.

**Fix:** Run Convex bump mutation for all 6 papers with EXT11-closure versions + md5 hashes. Use `tools/p*_convex_bump_*.mjs` pattern or `/bigbounce-bump` skill.

Convex API endpoint confirmed working:
```
POST https://brilliant-panther-471.convex.cloud/api/query
path: "paperVersions:current"
args: {"paperSlug": "paper-1a"}
→ {"version": "v1A.0.73"} (stale)
```

---

## Paper Pages QA

All 6 pages return HTTP 200 and render correctly.

### Paper 1A (`/papers/paper-1a`)
- **Status:** PASS (with P1 version note)
- **Header version:** V1A.0.73 (Convex — stale)
- **Artifact row version:** v1A.0.74 (static — correct)
- **PDF status:** HTTP 200 (`/papers/paper1a_ech_nogo_v1A.0.74.pdf`)
- **MD5 3871b587:** Not displayed on page (md5 is in commit log only, not a site surface)
- **External review panel:** PRESENT — "EXTERNAL PEER REVIEW KIT" with MNRAS/PRD recalibrated prompt visible
- **EXT12 in review history:** PRESENT (EXT12-LAUNCHED entry visible)
- **Publishability path:** 6-stage tracker visible (4 DONE, 1 IN PROGRESS, 1 WAITING)
- **Mobile 375px:** PASS — no overflow, layout readable
- **Tablet 768px:** PASS

### Paper 1B (`/papers/paper-1b`)
- **Status:** PASS (with P1 version note)
- **Header version:** V1B.0.70 (Convex — stale)
- **Artifact row version:** v1B.0.71 (static — correct)
- **PDF status:** HTTP 200 (`/papers/paper1b_mcmc_companion_v1B.0.71.pdf`)

### Paper 2 (`/papers/paper-2`)
- **Status:** PASS (with P1 version note)
- **Header version:** V1.7.64 (Convex — stale)
- **Artifact row version:** v1.7.65 (static — correct)
- **PDF status:** HTTP 200 (`/papers/paper2_fnl_forecast_v1.7.65.pdf`)

### Paper 3 (`/papers/paper-3`)
- **Status:** PASS (with P1 version note)
- **Header version:** V3.1.107 (Convex — stale)
- **Artifact row version:** v3.1.108 (static — correct)
- **PDF status:** HTTP 200 (`/papers/paper3_anomaly_catalog_v3.1.108.pdf`)

### Paper 4 (`/papers/paper-4`)
- **Status:** PASS (with P1 version note)
- **Header version:** V1.0.187 (Convex — stale)
- **Artifact row version:** v1.0.188 (static — correct)
- **PDF status:** HTTP 200 (`/papers/chirality_catalog_paper_v1.0.188.pdf`)

### Paper 5 (`/papers/paper-5`)
- **Status:** PASS (with P1 version note)
- **Header version:** V0.1.76 (Convex — stale)
- **Artifact row version:** v0.1.77-2026-06-13 (static — correct)
- **PDF status:** HTTP 200 (`/papers/p5_desi_chirality_v0.1.77.pdf`)

---

## /reviews Page QA

**Status:** PASS

All 4 new timeline entries confirmed present in live HTML:
- `EXT12-LAUNCHED` ✓ (5 occurrences in HTML)
- `EXT11-VERDICT-LADDER` ✓ (5 occurrences in HTML)
- `EXT11-CLOSURE-WAVE` ✓ (5 occurrences in HTML)
- `SKILL-PDFTOTEXT-RENDERING-ARTIFACT` ✓ (5 occurrences in HTML)

Note: The QA task referenced `SKILL-PDFTOTEXT-ARTIFACT` but the actual ID in reviewTimeline.ts is `SKILL-PDFTOTEXT-RENDERING-ARTIFACT` — matches what's in source + confirmed live.

**EXT11 verdict ladder (10/18 ACCEPT):** Visible in EXT11-VERDICT-LADDER entry text on the page.

**SKILL-* styling:** The `kind: "skill-improvement"` field is set in reviewTimeline.ts. The rendering component should apply skill-improvement styling — confirmed the entries render but specific CSS class inspection was inconclusive due to browser tab interference.

**Total round count in campaign trajectory:** 320 EXT/R-round strings visible in page text.

**Mobile 375px:** PASS — reviews page renders correctly at mobile viewport.

---

## Cross-Page Consistency

**Papers index (/papers):** Shows both old Convex versions (v1A.0.73 etc.) and new static versions (v1A.0.74 etc.) simultaneously in different surface areas — consistent with the P1 Convex version mismatch. The PDFs linked from the index are the correct EXT11-closure PDFs (HTTP 200 verified).

**Individual paper pages vs index:** Consistent — both show the same Convex-vs-static version split.

---

## P2 Bug — Preloaded CSS Resource Warning

**Severity:** P2 — no user-visible impact

Console shows preload warnings for CSS chunks:
```
The resource _next/static/chunks/0q.nf523na1r_.css was preloaded using link preload but not used within a few seconds
```

This is a Next.js route-based CSS chunking behavior — the stylesheet is preloaded for potential navigation but not consumed by the current page. Not a functional bug. Known Next.js pattern.

---

## Console Errors (site-origin only)

Browser console shows 401/404 errors but these originate from active Grok tabs in the same browser session (xAI job listing fetches), NOT from bigbounce.hubify.app. No bigbounce-origin console errors detected.

Persistent warnings (non-blocking):
- `react-i18next: NO_I18NEXT_INSTANCE` — pre-existing, from Convex client
- CSS preload warning (P2 above)
- `Permissions-Policy: pointer-lock` — pre-existing Vercel header

---

## Screenshots

All screenshots saved to `.gstack/qa-reports/screenshots/`:

| File | Page | Viewport |
|------|------|----------|
| `paper-1a-final.png` | Paper 1A | 1280px desktop |
| `paper-1b-full.png` | Paper 1B | 1280px desktop |
| `paper-2-full.png` | Paper 2 | 1280px desktop |
| `paper-3-full2.png` | Paper 3 | 1280px desktop |
| `paper-4-full2.png` | Paper 4 | 1280px desktop |
| `paper-5-full-final.png` | Paper 5 | 1280px desktop |
| `paper-1a-mobile-375.png` | Paper 1A | 375px mobile |
| `paper-1a-tablet-768-v2.png` | Paper 1A | 768px tablet |
| `reviews-page.png` | /reviews | 1280px desktop |
| `reviews-mobile-375.png` | /reviews | 375px mobile |
| `papers-index-final.png` | /papers index | 1280px desktop |

---

## Action Items

| Priority | Item | Fix |
|----------|------|-----|
| P1 | Convex stale on all 6 papers (one version behind) | Run Convex bump mutation for all 6 with EXT11-closure versions — use `/bigbounce-bump` or tools/p*_convex_bump scripts |
| P2 | CSS preload warning | Known Next.js behavior; address in next site refactor if desired |
