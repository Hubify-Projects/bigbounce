# Site Audit — Lane C — 2026-07-22

Scope: data-explorer.html, anomaly-explorer.html, galaxy-explorer.html,
activity.html, explained.html, glossary.html, docs.html, articles.html,
surveys.html, contributions.html, speculations.html, search.html,
visualize.html, chat.html, old.html, 404.html. Checked against built HTML in
`site/out/` AND live spot-checks at https://bigbounce.hubify.app (cache-busted
navigations + fresh-tab reproductions, 2026-07-23 session). AUDIT ONLY —
nothing changed.

Canonical truth used: P1A v1A.0.126 / P1B v2B.0.14 / P2 v1.7.127 /
P3 v3.2.0-r12 / P4 v1.0.270 / P5 v0.1.142-2026-07-22; DOIs P1A …21481838,
P1B …21481842 + software …21481753, P2 …21461881, P3 …21461888, P4 …21461899;
ORCID 0009-0008-5616-5994 only; f_NL −35/16 canonical; forbidden-as-current:
−35/8 (outside historical context), "378,280", "949,584 High-Confidence" as
current framing, dataset counts contradicting the 890,069 quality-controlled
catalog.

## Summary counts

- P0: 3
- P1: 3
- P2: 2
- Clean checks (no finding): glossary.html (f_NL, birefringence, MCMC, PBH
  entries all match canonical values, -35/8 not present); explained.html body
  science content (f_NL = -35/16 correctly stated); data-explorer.html's
  repeated -35/8 references are all explicitly and correctly annotated
  "SUPERSEDED"/"superseded single-ordering convention" — proper historical
  framing, not a violation; no lorem-ipsum/TODO/FIXME/placeholder strings
  found in any of the 16 files; no broken internal `href` targets found by
  static link-resolution sweep of all 16 built pages; surveys.html,
  articles.html, speculations.html, docs.html, activity.html, visualize.html
  carry no forbidden numbers, no stale version strings, no ORCID/DOI content
  to check.

---

## P0

### 1. old.html (`/old`) is an infinite client-side redirect loop — page is permanently blank on the live site

- **Route:** /old (live) — also reachable via `/old/index.html`
- **Finding:** Navigating to https://bigbounce.hubify.app/old renders nothing
  but the topbar chrome; the main content area is completely empty,
  indefinitely. Network trace shows the tab issuing a continuous, never-ending
  stream of `GET /old → 200` and `GET /old/index.html.txt?_rsc=... → 200`
  requests (dozens captured within a few seconds, still climbing when the tab
  was closed) — a genuine infinite navigation loop, not a slow load. The same
  blank result occurs navigating directly to `/old/index.html`, and that
  second navigation attempt was outright rejected by the browser
  ("denied or failed") consistent with a redirect-loop abort.
- **Root cause (confirmed in source):** `site/src/app/old/page.tsx` is a Next
  App Router page that does `redirect("/old/index.html")`. Meanwhile
  `vercel.json` has `{"rewrites": [{"source": "/old", "destination":
  "/old/index.html"}]}` and `"cleanUrls": true`. cleanUrls strips the
  `.html` off `/old/index.html` back to `/old/index`... which Vercel/Next then
  resolves back into the `/old` App Router page, which redirects to
  `/old/index.html` again — a loop. The real legacy content is present and
  correct in the build (`site/out/old/index.html` is byte-identical,
  73,012 bytes, to `site/public/old/index.html`), so this is purely a
  routing/redirect misconfiguration, not missing content.
- **Evidence:** live network capture (repeating `/old` and
  `/old/index.html.txt` requests, 2026-07-23 session); `site/src/app/old/page.tsx`
  line 4 (`redirect("/old/index.html")`); `vercel.json` rewrites block; byte
  count match between `site/out/old/index.html` and `site/public/old/index.html`
  (both 73012 bytes).
- **Concrete fix:** Remove the Next App Router redirect page at
  `site/src/app/old/page.tsx` (or point it somewhere that isn't re-caught by
  the same rewrite) and let the `vercel.json` rewrite serve the static file
  directly — or drop the rewrite and let `cleanUrls` alone resolve `/old` to
  `/old/index.html` as a static asset without an intervening Next page/route
  at that same path. Whichever approach is chosen, verify with a fresh
  incognito/cache-busted load that `/old` returns the real legacy content in
  one hop, not a loop.
- **Note on the audit's item (5):** `/old` is correctly absent from the live
  site's primary nav (confirmed via full nav tree read), so it isn't being
  actively surfaced to readers — but it is linked to from
  `site/src/app/contributions/page.tsx:767` as `/old/contributions.html`
  (a *different*, working path — see Clean checks) and is a guessable/bookmarked
  URL from the old site era, so the infinite loop is still reachable and
  embarrassing to anyone who hits it.

### 2. chat.html (`/chat`) — "astro" chat does not work: pressing Enter never sends the message

- **Route:** /chat (live)
- **Finding:** The only input control on the page is a text box
  (`placeholder="ask astro..."`) with no visible Send button. Typing a message
  and pressing Enter does not submit anything: no network request to any
  chat/completion endpoint is ever fired (confirmed via full network-request
  capture — the only request seen was the unrelated legacy asset
  `/old/astro/chat-widget.js`), no response appears, no loading state, and the
  typed text is not cleared from the input. The feature is completely
  non-functional as shipped; a first-time visitor who asks "astro" anything
  gets silence.
- **Evidence:** live session on https://bigbounce.hubify.app/chat — filled
  the input via direct value-set + real click + `Return` keypress, then
  confirmed via `read_network_requests` that zero chat-API calls were made
  and via screenshot that the typed text remained un-sent in the input with no
  reply rendered in the transcript pane.
- **Concrete fix:** locate the chat page component (likely
  `site/src/app/chat/page.tsx` or a shared `Chat`/`Astro` component) and
  verify the `onKeyDown`/`onSubmit` handler is actually wired to a working
  fetch/completion call; add a visible Send button as a non-keyboard fallback;
  add a basic error/loading state so a broken backend is at least visible to
  the user instead of silent.

### 3. galaxy-explorer.html headlines the stale "949,584 high-confidence spirals" figure with no mention of the canonical 890,069 catalog

- **Route:** /galaxy-explorer (site/out + live)
- **Finding:** The page's top "Key Science Findings" summary reads:
  *"Comprehensive analysis of 8,474,531 galaxies — the largest galaxy
  chirality catalog ever produced. 100% coordinate match with GZ DESI Zenodo
  catalog. **949,584 high-confidence spirals** (confidence > 0.6)."* — and
  repeats "949,584" as the headline "High-confidence spirals" stat elsewhere
  on the same page. The string "890,069" (the canonical
  quality-controlled/strict catalog count used everywhere else in the
  program, e.g. in P4's own title "...890,069 Quality-Controlled
  High-Confidence DESI Spirals...") does not appear anywhere in
  `galaxy-explorer.html`. This is exactly the pattern the canonical truth
  table calls out as forbidden: "949,584 High-Confidence" presented as
  current framing, without reconciliation to 890,069.
- **Evidence:** `site/out/galaxy-explorer.html` —
  `grep -c "890,069"` → 0; `grep -o '.{100}949,584.{100}'` → three hits, all
  presenting 949,584 as the current/headline count with no strict-sample
  caveat.
- **Concrete fix:** `site/src/app/galaxy-explorer/page.tsx` — replace the
  headline stat with the strict 890,069 quality-controlled figure (matching
  the P2/P4 canonical framing used in search results and the paper titles
  themselves), or explicitly caveat 949,584 as the pre-QC "confidence > 0.6"
  superset vs. the 890,069-row strict sample actually used for the published
  dipole statistic.

---

## P1

### 4. anomaly-explorer.html hardcodes a stale Paper 3 version string (v3.2.0-r10 vs canonical v3.2.0-r12)

- **Route:** /anomaly-explorer (site/out + live)
- **Finding:** Visible body copy reads: *"What Paper 3 actually is — Paper 3
  (**v3.2.0-r10**, IN REVISION) is a public-ID recovery of a frozen historical
  DESI DR1 anomaly list..."*. Canonical current version is v3.2.0-r12. The
  string "r12" does not appear anywhere in the file.
- **Evidence:** `site/out/anomaly-explorer.html`.
- **Concrete fix:** `site/src/app/anomaly-explorer/page.tsx` — update the
  hardcoded version string, and ideally source it from the same live
  Convex/`papers.ts` data the rest of the site uses instead of a literal
  string, so it can't drift out of sync with future version bumps again.

### 5. data-explorer.html states the forbidden "~378,280 exploratory candidates" figure with no reconciliation to the 890,069 canonical catalog count

- **Route:** /data-explorer (site/out + live)
- **Finding:** Two places on the page state *"the candidate list holds
  ~378,280 exploratory candidates + 637 multi-survey clusters"* (correctly
  caveated as "exploratory pipeline candidates, NOT confirmed physical
  objects" — good practice — but the literal count itself is on the
  truth table's forbidden-strings list, and the page never references the
  890,069 quality-controlled figure to show a reader how the two numbers
  relate). Note this number describes Paper 3's raw exploratory candidate
  pool rather than Paper 2/4's QC'd chirality catalog, so it may be
  legitimately a different quantity — but as written the page gives a
  first-time reader no way to tell that, and the exact string is on the
  forbidden list regardless of context.
- **Evidence:** `site/out/data-explorer.html`,
  `grep -o '.{150}378,280.{150}'`.
- **Concrete fix:** `site/src/app/data-explorer/page.tsx` — either replace
  with the current canonical figure if this cell should reflect the
  890,069-row strict catalog, or add an explicit one-line disambiguation
  ("this is Paper 3's exploratory candidate pool, distinct from Paper 2/4's
  890,069-row quality-controlled chirality catalog") so the two numbers on
  the site never look like an unresolved contradiction to a reader who sees
  both pages.

### 6. Unknown/mistyped URLs return HTTP 200 and silently render the homepage instead of the 404 page

- **Route:** 404.html / any nonexistent path (live)
- **Finding:** Navigating to a deliberately nonexistent path
  (`/this-page-does-not-exist-audit-check`) returns HTTP 200 (confirmed via
  network status) and renders the full homepage — hero, live-dossier ticker,
  "Was there a bounce before the Big Bang?" — under the wrong URL, with
  `document.title` still "BigBounce — Spin-Torsion Cosmology" rather than the
  custom 404 page. A visitor who mistypes a link or follows a stale/broken
  internal link gets no signal that anything went wrong — they land on the
  homepage with no explanation, which reads as confusing rather than helpful
  and is a soft-404 that can also hurt SEO indexing of the real error state.
  (The custom 404 content does exist and build correctly at
  `site/out/404.html` — this is a live-routing/fallback issue, not a missing
  page.)
- **Evidence:** live `read_network_requests` showing
  `GET /this-page-does-not-exist-audit-check → 200`; `window.location.href`
  and `document.title` both confirming homepage content was served at the
  bad URL.
- **Concrete fix:** likely the same `vercel.json` rewrite/`cleanUrls`
  interaction implicated in finding #1 — verify the Vercel static-export
  deployment actually wires an unmatched-route fallback to
  `site/out/404.html` (Vercel's default behavior for a `next export`-style
  static site should do this automatically unless a catch-all rewrite is
  intercepting first); test with several random nonexistent paths after the
  fix.

---

## P2

### 7. Stale-looking static date-stamps on contributions.html and explained.html eyebrows

- **Routes:** /contributions ("APRIL 2026 · NOVELTY ACCOUNTING"),
  /explained ("NON-TECHNICAL EXPLAINER · JUNE 2026")
- **Finding:** Both pages carry a prominent static month/year eyebrick label
  well behind the current July 22–23, 2026 program state (papers have since
  advanced many versions: P1A alone is now v1A.0.126). Not factually
  incorrect — the underlying content on both pages is otherwise accurate and
  well-labeled — but a static "APRIL 2026" / "JUNE 2026" stamp reads as
  neglected/stale to a careful first-time reader scanning dates across the
  site, especially next to a homepage ticker stamped "July 22, 2026."
- **Concrete fix:** `site/src/app/contributions/page.tsx` and
  `site/src/app/explained/page.tsx` — either drop the static month/year
  label entirely or wire it to the page's actual last-substantive-edit date.

### 8. search.html — rapid keystrokes immediately after page load can trigger unrelated navigation instead of populating the search box (unconfirmed root cause, needs follow-up)

- **Route:** /search (live)
- **Finding:** When the search input was clicked and typed into
  immediately after a fresh page navigation (via coordinate click +
  simulated keystrokes), the keystrokes did not appear in the search box;
  instead, on two separate attempts (typing "chirality" and, separately,
  "fnl") the tab navigated away to `/publish` with no input actually
  entered. When the same input was instead targeted deterministically
  (explicit ref-based focus + programmatic value set), the search box worked
  correctly and returned accurate, canonical-consistent results (e.g.
  correctly surfaced "890,069 Quality-Controlled High-Confidence" in a P4
  result for a "chirality" query) — so the underlying search logic itself is
  sound. This looks like a hydration-timing race (keystrokes landing on a
  global handler before the input's own listener has attached, or before
  focus lands) rather than a hard functional bug, but it was reproducible
  twice in a row and is exactly the kind of thing a real visitor typing
  quickly on page-load could also hit, silently bouncing them to an
  unrelated page instead of searching.
- **Evidence:** live session on https://bigbounce.hubify.app/search,
  2026-07-23 — two reproductions of keystroke-triggers-navigation-to-/publish
  on freshly-loaded tabs, followed by a clean successful search once input
  was targeted deterministically.
- **Concrete fix:** not confirmed to a specific file — flag for a follow-up
  session to reproduce with real (non-automated) keyboard input and check
  whether a global keydown/command-palette listener on the shared layout
  (sidebar/topbar component) is capturing events before the search input's
  own handler, and whether it checks `e.target` before acting.

---

## Design/readability check (item 6)

No nested-border-stack layout violations observed in any of the 16 lane-C
pages at proper desktop width (1280px) — data-explorer's sidebar + table view
uses a single clean shell with row/divider structure, consistent with
Houston's stated design rules. (An earlier screenshot taken mid-viewport-resize
showed a garbled one-word-per-line narrow column; this was confirmed to be a
browser-pane resize-timing artifact, not a real site bug — the same page
rendered correctly once the viewport had actually settled at 1280px.)

## DISPOSITION 2026-07-22 (orchestrator)
P0s FIXED: /old redirect loop replaced with archive lander (0 redirects live); /chat honest offline state + dead site-wide bubble script removed (no /api/chat backend exists — verified incl. Convex probe 404); galaxy-explorer now frames 949,584 as pre-quarantine with 890,069 released (fixed at repo-root legacy source — prebuild copy overwrites site/public/old edits). P1s: anomaly-explorer r12; data-explorer 378,280 DISPOSITIONED NO-CHANGE (it denotes P3 exploratory pipeline candidates and is already heavily caveated as non-detection in-page; unrelated to P4's 890,069); soft-404 DEFERRED (needs vercel.json change — flagged for a preview-verified pass). P2 month stamp: explained → July 2026; APRIL stamp not found in current app source (legacy archive left as-is).
