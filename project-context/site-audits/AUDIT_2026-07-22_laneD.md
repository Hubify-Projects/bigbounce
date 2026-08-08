# Site Audit — Lane D (Global Link/Asset/Meta Integrity)

**Date:** 2026-07-22/23
**Scope:** All 32 pages in `site/out/` (26 top-level `.html` + 6 `papers/paper-*.html`)
**Method:** Static extraction of every internal href/img/pdf across all 32 pages, resolved against `site/out/` on disk with cleanUrls semantics (`/x` → `x.html` or `x/index.html`); live spot-checks against `https://bigbounce.hubify.app` via curl; external-link sample (40, capped/deduped from 759 unique) via `curl -sI`.
**Status:** AUDIT ONLY — no files changed.

---

## Summary counts

| Category | Checked | Findings |
|---|---|---|
| Internal link 404 candidates | ~2,000+ hrefs across 32 pages | 11 unique broken targets (all on `reviews.html`) |
| Live spot-check (15 random + 11 suspicious) | 26 | 0 hard 404s — but site returns **soft-404 (HTTP 200)** for everything, masking real breakage (see P1) |
| Image/asset sweep | all `<img>`/`<source>` across 32 pages | 0 missing, 0 zero-byte |
| Zero-byte files anywhere in `site/out/` | 1,558 files | 0 |
| External links | 759 unique (714 github.com, 16 huggingface.co, 6 zenodo.org, 6 chatgpt.com, 6 gemini.google.com, 6 grok.com, 3 doi.org, 1 arxiv.org, 1 hubify.com) | **1 broken: `github.com/Hubify-Projects/scistack`** (whole repo 404s), hit via 7 unique commit-links / 21 total refs on `reviews.html` |
| Meta (title/description/viewport) | 32 pages | 0 missing; titles unique per real content page (404/_not-found/old share the default title by design — stub pages) |
| PDF surface (referenced `/papers/*.pdf`) | 19 unique local hrefs | **1 not live: `chirality_catalog_paper_v1.0.270.pdf`** — exists locally, 33.9MB, but live host serves soft-404 for it (P0, see below) |
| Nav consistency | 32 pages | Identical 22-link nav on all 31 real pages; `old.html` has no nav by design (legacy redirect stub → `/old/index.html`) |

---

## Findings

### P0

1. **category: PDF SURFACE | P0 | Live-deployed PDF missing for the current paper-4 version, referenced from 3 pages including the homepage**
   - **evidence:** `curl -sI https://bigbounce.hubify.app/papers/chirality_catalog_paper_v1.0.270.pdf` → `HTTP/2 200`, `content-type: text/html; charset=utf-8`, `content-length: 146321` (this is the site's soft-404/homepage fallback body, not the PDF). The file exists locally and correctly at `site/out/papers/chirality_catalog_paper_v1.0.270.pdf` (33,979,485 bytes, built 2026-07-23 00:42). By contrast the prior version `chirality_catalog_paper_v1.0.269.pdf` **is** live and byte-identical to the local copy (`content-length: 33979309`, `content-type: application/pdf`, matches local file size exactly). `index.html`, `paper.html`, and `papers/paper-4.html` all reference `v1.0.270.pdf` as the current link (confirmed both in the local build and in the live-served HTML — the HTML deploy succeeded, only the PDF binary failed to upload).
   - **fix:** Re-run the PDF mirror/deploy step for `chirality_catalog_paper_v1.0.270.pdf` to the live static host (Vercel CLI static deploy, per the known working path — git integration is dead on this 50GB repo). Verify with `curl -sI .../chirality_catalog_paper_v1.0.270.pdf` returns `content-type: application/pdf` and `content-length: 33979485` matching local, before closing. This is exactly the failure mode `/bigbounce-site-sync` and directive-G PDF hygiene are meant to catch — worth a spot-check pass across all recently-bumped PDFs (not just this one) since a partial deploy can silently drop a single large asset.

### P1

2. **category: EXTERNAL LINKS | P1 | `github.com/Hubify-Projects/scistack` does not exist/is not public — 21 dead links on reviews.html**
   - **evidence:** `curl -sI https://github.com/Hubify-Projects/scistack` → `404`. Same for all 7 unique commit URLs referenced (`000cd25`, `40fe0cc`, `71e4a5c`, `8a5ae11`, `a82bc5f`, `b570c78`, `c40ca88`), each 404. Contrast: `github.com/Hubify-Projects/bigbounce` and `github.com/Hubify-Projects` (org root) both return 200 — so this is specific to the `scistack` repo being private/nonexistent under that org, not a general GitHub outage. 21 total occurrences across `reviews.html` (e.g. `scistack 000cd25 (directive J)`, `scistack c40ca88 (leak gate)`, `scistack b570c78 (URL-at-submit)` link labels).
   - **fix:** Either make `Hubify-Projects/scistack` public (if it's meant to be an external-facing citation), or stop linking to it from public review-timeline entries and cite the corresponding bigbounce-repo artifact/commit instead (scistack skills are synced into this repo — a bigbounce-side citation likely exists). Cross-check with `/artifact-link-verify`.

3. **category: INTERNAL LINK SWEEP | P1 | 10 links on reviews.html point at raw repo paths that were never part of the built site (never resolve to real content, silently swallowed by the site's soft-404)**
   - **evidence:** hrefs found on `reviews.html`, none resolve to a file under `site/out/`:
     - `/project-context/review-patterns/pattern-009-gpt-fallback-low-rigor.md`
     - `/project-context/review-patterns/pattern-031-self-review-severity-underclassification.md`
     - `/project-context/review-patterns/pattern-051-closure-introduced-regression.md`
     - `/project-context/review-patterns/pattern-052-reraise-vindication.md`
     - `project-context/review-patterns/pattern-068-preemptive-rebuttal-hardening-DRAFT.md`
     - `project-context/review-patterns/pattern-062-stale-pdf-false-positive-DRAFT.md`
     - `project-context/review-patterns/pattern-061-dispatch-tag-vs-intext-mismatch-DRAFT.md`
     - `project-context/review-patterns/pattern-063-extraction-artifact-false-positive-DRAFT.md`
     - `project-context/review-patterns/pattern-064-grok-harsh-outlier-false-positive-DRAFT.md`
     - `~/.agent-shared/AGENTS.md` (a literal `~/` path used as an href — never resolves on the web at all)
     Live-checked all 10: every one returns `HTTP/2 200` with `content-type: text/html`, `content-length: 146321` and `<title>BigBounce — Spin-Torsion Cosmology</title>` — i.e. the site's Next.js static-export soft-404 fallback (same body served for a deliberately nonexistent test path). These are **not real, resolvable links**; they render as the homepage with no indication of failure to a clicking user.
   - **fix:** These are project-context markdown paths, most likely meant to be `github.com/Hubify-Projects/bigbounce/blob/main/project-context/review-patterns/...` links (the pattern used correctly elsewhere on the same page for other pattern docs) rather than bare site-relative paths. Rewrite each to the GitHub blob URL, and fix the literal `~/.agent-shared/AGENTS.md` (either drop the link or point it at the correct public mirror if one exists).

4. **category: PDF SURFACE / INTERNAL LINK SWEEP | P1 | `paper1_unified_v1U.0.1.pdf` referenced but never built**
   - **evidence:** `reviews.html` links `/papers/paper1_unified_v1U.0.1.pdf`. Directory listing of `site/out/papers/paper1_unified_v1U.0.*.pdf` starts at `.0.2.pdf` — `.0.1.pdf` was never generated/was pruned. Live-checked: `HTTP/2 200`, `text/html`, `content-length: 146321` — same soft-404 fallback as above.
   - **fix:** Correct the href to `paper1_unified_v1U.0.2.pdf` (the true earliest archived version) or remove the entry if v1U.0.1 never had a real deploy.

5. **category: WEBSITE INFRASTRUCTURE | P1 | Site returns HTTP 200 (soft-404) for every nonexistent path, indistinguishable from real content**
   - **evidence:** `curl -sI https://bigbounce.hubify.app/this-definitely-does-not-exist-xyz123` → `HTTP/2 200`, same `content-length: 146321`, same etag `"230b12f2b5cfa8acada572924d5a5660"`, same title as the 11 broken links above. This is a byproduct of the static Next.js export being served without server-side 404 routing on the current Vercel static-deploy path (per the known "Git integration dead, CLI static deploy of trimmed site/out" fix). It means **no automated crawler/monitor can detect a broken link by status code alone** — this audit only caught the above 11 by diffing against the actual file list in `site/out/`, and the deployed-PDF gap in finding #1 only because content-type/length gave it away.
   - **fix:** Not fixable by editing pages; this is a hosting/deploy-config issue. Worth flagging to whoever owns the Vercel static-export config: either restore a proper `404.html` status-code response (Vercel supports custom 404 handling for static exports via `vercel.json` routes/rewrites with `"status": 404`), or accept the soft-404 behavior but add this same local-file-list diffing step as a standing pre-deploy CI check (this audit's method) since curl-based link checkers alone will always report false-clean.

### P2

6. **category: META/HEAD | P2 | No `og:image`/`twitter:image` on any of the 32 pages**
   - **evidence:** `grep` for `og:image`/`twitter:image` content across all pages returned zero matches; `og:title`, `og:description`, `twitter:card`, `twitter:title`, `twitter:description` are all present and populated.
   - **fix:** Low-priority polish — add a default site-wide social card image (og:image/twitter:image) so shared links render a preview image instead of a blank/generic card.

7. **category: META/HEAD | P2 | No `robots.txt` or `sitemap.xml` in `site/out/`**
   - **evidence:** `find site/out -iname "robots.txt" -o -iname "sitemap*.xml"` → no results.
   - **fix:** Add both for SEO/crawler completeness, especially since #5 means crawlers can't distinguish real pages from soft-404s without a sitemap as ground truth.

### Clean (no action needed)

- **Nav/footer consistency:** all 31 real content pages share an identical 22-link nav (`/`, `/search`, `/explained`, `/surveys`, `/predictions`, `/paper`, `/reviews`, `/publish`, `/contributions`, `/data-explorer`, `/galaxy-explorer`, `/anomaly-explorer`, `/visualize`, `/figures`, `/glossary`, `/timeline`, `/articles`, `/speculations`, `/chat`, `/activity`, `/status`, `/docs`). `old.html` is a deliberate legacy redirect stub (`NEXT_REDIRECT → /old/index.html`) with no nav — by design, not a defect.
- **Image/asset sweep:** 0 missing, 0 zero-byte across all referenced images and all 1,558 files in `site/out/`.
- **Titles:** unique per real page; no accidental duplicates outside the three stub pages (404/_not-found/old) that intentionally inherit the default site metadata.
- **PDF surface, remaining 18 of 19 referenced PDFs:** all live, `200`, `application/pdf`, correct sizes.
- **External links, remaining 39 of 40 sampled** (doi.org ×3, zenodo.org ×6, huggingface.co ×16, arxiv.org, hubify.com, github.com pinned-commit blobs, tree links, commit shorthand links, main-branch blobs): all `200`.
- The 1,894 `<title>` tags found inside `reviews.html` are legitimate SVG `<title>` tooltip elements (inside `<rect>`/`<g>` verdict-grid cells) — valid, non-issue; not HTML `<title>` duplication.

---

## Sampling notes (per spec caps)

- External links: 759 unique found; spec caps live-checking at 40 — sample was weighted toward all doi.org/zenodo.org/huggingface.co/arxiv.org/hubify.com links (27, effectively 100% of those categories) plus a stratified sample of github.com (2 pinned-commit blobs, 4 short-commit links, 4 tree links, 3 repo-root links, remainder random main-branch blobs) to maximize category coverage within the cap. The 1 failure found (scistack) was in the stratified short-commit sample — recommend a full sweep of all 714 github.com links if time allows, since this sample size (40/759) leaves the bulk of main-branch blob links unchecked.
- Internal live spot-check: 15 random top-level/paper pages (all 200) + all 11 suspicious/irregular hrefs from the 404-candidate list (all soft-404'd, confirming the local-file-list method as ground truth over live-curl-status for this host).

## DISPOSITION 2026-07-22 (orchestrator)
P0 FIXED (P4 PDF live, md5-verified). P1s FIXED: 4 raw /project-context hrefs → GitHub blob URLs (reviews page); ~/.agent-shared + 2 tilde links neutralized; 7 dead scistack commit links unlinked (shas retained in prose); phantom paper1_unified_v1U.0.1.pdf → existing alias. P2: robots.txt + sitemap.xml (29 routes) added, live 200. og:image DEFERRED (needs asset design). Soft-404 DEFERRED (vercel.json; preview-verified pass queued).
