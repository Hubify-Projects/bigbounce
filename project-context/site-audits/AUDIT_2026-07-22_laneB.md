# Site Audit — Lane B — 2026-07-22

Scope: paper.html, papers/paper-1a.html, papers/paper-1b.html, papers/paper-2.html,
papers/paper-3.html, papers/paper-4.html, papers/paper-5.html, figures.html,
predictions.html. Checked against built HTML in `site/out/` AND live spot-checks
at https://bigbounce.hubify.app (cache-busted). AUDIT ONLY — nothing changed.

Canonical truth used: P1A v1A.0.126 (md5 6ade40c14049a316eabf21e67dc10072) /
P1B v2B.0.14 (3f5c161224d1cf62a6a467fe34f5ba09) / P2 v1.7.127
(881cbc062656849beee4609996ae2351) / P3 v3.2.0-r12 (37fdd322f06be11d8384ff505114afa8)
/ P4 v1.0.270 (904414a10de8ddba9f7aca99be3f6fb1) / P5 v0.1.142-2026-07-22
(a70307b01058d3688bc69758847d414f).

## Summary counts

- P0: 1
- P1: 2
- P2: 2
- Clean checks (no finding): version chip/pdfMeta/href consistency (6/6 papers),
  local PDF md5 match (6/6), DOI resolution (6/6 DOIs 302→200), f_NL/P4-catalog
  number consistency, design/layout pass on P4 page.

---

## P0

### 1. Live P4 PDF download is broken — serves the site shell instead of the paper

- **Route:** papers/paper-4.html (both "Read PDF" and "Download PDF" buttons)
- **Finding:** The href `/papers/chirality_catalog_paper_v1.0.270.pdf` — which is
  correct and matches the version chip (v1.0.270) and the pdfMeta md5
  (904414a10de8ddba9f7aca99be3f6fb1) on the page — returns **HTTP 200 with
  `content-type: text/html; charset=utf-8`** on the live site (146KB, the SPA
  index shell), not the 34MB PDF. A reader clicking either button on the live
  page gets the homepage, not the paper.
  - The unversioned alias `chirality_catalog_paper.pdf` and the previous
    version `chirality_catalog_paper_v1.0.269.pdf` (stale) both serve correctly
    as `application/pdf` live — only the newest v1.0.270 file is missing from
    the live deploy.
  - Locally, `site/out/papers/chirality_catalog_paper_v1.0.270.pdf` exists and
    its md5 matches canonical exactly (verified via `md5 -q`), so this is a
    **deploy-sync gap**, not a source/content bug — the last static deploy to
    Vercel predates the v1.0.270 PDF mirror, or the CLI trimmed-deploy path
    (per project memory: "CLI static deploy of trimmed site/out is the working
    path" since Vercel git integration is dead on the 50GB repo) dropped this
    34MB file.
- **Evidence:**
  ```
  curl -sI https://bigbounce.hubify.app/papers/chirality_catalog_paper_v1.0.270.pdf?cb=...
    HTTP/2 200
    content-type: text/html; charset=utf-8      <- WRONG, should be application/pdf
  curl -sI https://bigbounce.hubify.app/papers/chirality_catalog_paper_v1.0.269.pdf?cb=...
    HTTP/2 200
    content-type: application/pdf                <- old version, works fine
  local: site/out/papers/chirality_catalog_paper_v1.0.270.pdf md5 = 904414a10de8ddba9f7aca99be3f6fb1 (MATCHES canonical)
  ```
- **Fix:** Re-run the CLI static deploy (per the working deploy path noted in
  project memory `bigbounce-vercel-deploy-fix-2026-07-16`) so
  `site/out/papers/chirality_catalog_paper_v1.0.270.pdf` (and the unversioned
  alias) actually lands on the live Vercel deployment. Verify post-deploy with
  `curl -sI .../chirality_catalog_paper_v1.0.270.pdf` returns
  `content-type: application/pdf` and md5 of the downloaded body equals
  904414a10de8ddba9f7aca99be3f6fb1. This is exactly the class of failure
  `/bigbounce-site-sync` and `/site-cohesion-sweep` are meant to catch — worth
  adding a live-md5 check (not just HTTP 200) to that sweep, since a 200 with
  wrong content-type currently passes a naive status check.

---

## P1

### 2. figures.html figure-source captions are stale for 5 of 6 papers

- **Route:** figures.html (built + live, both confirmed stale)
- **Source file:** `site/src/data/figures.ts`
- **Finding:** Every figure caption's `"source": "Paper N · vX.Y.Z"` string cites
  an older version than canonical, for every paper except P1A (no figures) and
  presumably needs a same pass whenever any of these bump again:

  | Paper | figures.ts shows | Canonical current |
  |---|---|---|
  | P1B | v2B.0.13 (3 captions) | v2B.0.14 |
  | P2 | v1.7.126 (2 captions) | v1.7.127 |
  | P3 | v3.2.0-r11 (12 captions) | v3.2.0-r12 |
  | P4 | v1.0.269 (11 captions) | v1.0.270 |
  | P5 | v0.1.141-2026-07-16 (9 captions) | v0.1.142-2026-07-22 |

  Confirmed live via `curl https://bigbounce.hubify.app/figures` — identical
  stale strings appear in production.
- **Evidence:** `grep -n '"source": "Paper' site/src/data/figures.ts` — lines
  33/41/49 (P1B v2B.0.13), 87/95 (P2 v1.7.126), 133–221 (P3 v3.2.0-r11, 12
  hits), 331–411 (P4 v1.0.269, 11 hits), 433–497 (P5 v0.1.141-2026-07-16, 9
  hits).
- **Fix:** Bulk-update the `"source"` strings in `site/src/data/figures.ts` to
  the current version tags, then rebuild + redeploy. This is a recurring class
  of drift (figures.ts is a separate data file from papers.ts and isn't
  touched by the normal per-paper version-bump flow) — worth adding a
  figures.ts version-string check to `/bigbounce-version-bump` or
  `/site-cohesion-sweep` so every paper bump also greps/patches figures.ts.

### 3. P1A and P1B have no clickable Zenodo DOI link — DOI only appears as plain text

- **Route:** papers/paper-1a.html, papers/paper-1b.html
- **Source file:** `site/src/data/papers.ts` — `artifacts` arrays for
  `paper-1a` (~lines 126–141) and `paper-1b` (~lines 179–206)
- **Finding:** P2, P3, and P4 each have a dedicated clickable artifact button
  labeled "Zenodo DOI" linking to `https://doi.org/10.5281/zenodo....`. P1A and
  P1B do not — their published DOIs (P1A: 10.5281/zenodo.21481838; P1B:
  10.5281/zenodo.21481753 software + 10.5281/zenodo.21481842 manuscript) are
  mentioned only as unlinked plain text inside the `pdfMeta` prose paragraph.
  A reader cannot click through to either DOI from these two pages, even
  though both DOIs are confirmed live/published (resolve 302→200 via
  doi.org). P5 correctly has no DOI artifact yet since none is published for
  P5 — that one is not a finding.
- **Evidence:** `grep -oE 'https://doi.org/10.5281/zenodo\.[0-9]+' papers/paper-1a.html papers/paper-1b.html` returns nothing; same grep on paper-2/3/4.html returns the expected DOI URLs.
- **Fix:** Add `{ label: "Zenodo DOI", href: "https://doi.org/10.5281/zenodo.21481838", kind: "secondary", external: true }` to P1A's `artifacts` array, and two entries (manuscript + software) to P1B's, matching the pattern already used for P2/P3/P4.

---

## P2 (minor / informational)

### 4. P1B remainingWork text cites "v2B.0.13 Archive paragraph" as the DOI's home

- **Route:** papers/paper-1b.html
- **Source:** `site/src/data/papers.ts` line 173
- **Finding:** The remainingWork bullet says the DOIs are "cited in the
  v2B.0.13 Archive paragraph" — current version is v2B.0.14. This reads as a
  historical reference (when the DOI paragraph was first added) rather than a
  claim about the current version, so it is not misleading on a careful read,
  but it is easy to misread as a version-currency error. Low priority —
  optionally reword to "the Archive paragraph (present since v2B.0.13,
  current v2B.0.14)" for clarity next time this file is touched.

### 5. "Monopole significance ≈9.5σ (P5)" from the audit brief not found on-site

- **Route:** papers/paper-5.html, figures.html, predictions.html
- **Finding:** Could not locate any site-facing claim matching "monopole
  significance ≈9.5σ" tied to P5 — no occurrence of "monopole" anywhere in
  the P5 page, and no "9.5σ" tied to P5 in papers.ts. The only "monopole"
  hits found repo-wide are P4's open item "run the G4 monopole-mechanism
  injection" (unrelated significance number). This may be an internal
  SSOT/compute artifact not yet surfaced on the site, or the canonical-truth
  note may refer to a different (non-P5) context. Flagging as
  unable-to-verify rather than a contradiction — no stale/wrong number is
  currently displayed, there's simply no matching claim to check.

---

## Clean (no finding — confirmed correct)

- Version chip == pdfMeta version == download href version, all 6 papers,
  both `site/out/` build and live pages.
- All 6 canonical PDFs verified **locally** (`site/out/papers/*.pdf`) via
  `md5 -q`: P1A/P1B/P2/P3/P5 md5s match canonical exactly; P4 v1.0.270 md5
  also matches canonical exactly (33,979,485 bytes).
- Live PDF serving: P1A, P1B, P2, P3, P5 all return HTTP 200,
  `content-type: application/pdf`, and downloaded-body md5 exactly equal to
  canonical. (P4 is the sole live-serving failure — see P0 #1.)
- DOI resolution: all 6 canonical DOIs (P1A, P1B×2, P2, P3, P4) resolve
  302→200 via `curl -sIL https://doi.org/<doi>`.
- P4 numeric consistency spot-check: 890,069 / 887,472 / 819 (current
  CE-non-spiral count) / 826 & 846 (historical conflict values, correctly
  presented as resolved-historical, not current) all consistent between
  papers.ts prose and rendered HTML.
- f_NL = −35/16 = −2.1875 consistent across paper.html, papers/paper-2.html,
  and predictions.html; no stray −35/8 found outside historical framing.
- No false "pending" text found — the one "pending" hit on paper-4.html
  ("CE-ResNet component absent pending external re-provisioning") is an
  honest, currently-true disclosure, not stale copy.
- Design/layout pass (papers/paper-4 live screenshot): single outer content
  shell, chip/badge row for version/status metadata, no nested-border-stack
  pattern, clear typographic hierarchy — passes Houston's UI preference
  against boxes-within-boxes.

## DISPOSITION 2026-07-22 (orchestrator)
P0 FIXED: P4 v1.0.270 PDF now serves live, md5 == canonical 904414a1 (full referenced-PDF sync added to deploy recipe). P1s FIXED: figures captions current via Convex re-seed (r12/v0.1.142/v1.0.270/v1.7.127/v2B.0.14 live); P1A/P1B Zenodo DOI buttons added to papers.ts.
