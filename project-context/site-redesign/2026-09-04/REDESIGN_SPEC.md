# BigBounce site redesign — specification

**Date:** 2026-09-04 · **Author:** design director lane (Claude) · **Target:** https://bigbounce.hubify.app (`site/`, Next.js App Router + Convex)
**Input:** `INVENTORY.md` (this directory) · `VISION.md` · `PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md` · `SSOT/index.md` · `SESSION_HANDOFF_2026-09-04.md`
**Status:** SPEC — decisive, implementation-ready. No `site/` file was modified while writing it.

## Plan header

| # | Section | State |
|---|---|---|
| 1 | Positioning | drafted |
| 2 | Information architecture + route table | drafted |
| 3 | Content model per page | drafted |
| 4 | Visual language | drafted |
| 5 | Components (keep / build / delete) | drafted |
| 6 | Implementation plan (Sonnet lanes) | drafted |
| 7 | Risks and what NOT to change | drafted |

**Governing rules this spec obeys (non-negotiable):** no boxes-within-boxes (bordered surfaces only for genuine
tools — code blocks, data tables, explorers); premium Vercel/Mintlify reading experience; form inputs never carry a
focus ring on the inner element (`focus-within` on the wrapper only); every paper/program carries a plain-English
purpose label (directive Q3); **Convex is the only readiness source** (directive A); explorers' root `.html` files are
canonical; `reviewTimeline.ts` schema and `tools/site_freshness_check.sh` contracts are preserved.

---

## 1. Positioning — what the site says in ten seconds

The site is the **public face of a reproducible cosmology lab**, not a paper archive and not a dashboard for its own
review machinery. One sentence carries it: *"Was the Big Bang the beginning? We test a nonsingular bounce against data
that exists now — and we publish the nulls."*

Three readers, three ten-second reads. The homepage must satisfy all three above the fold plus one scroll.

**A physicist** must get, in order: (a) the question and the concrete claim — the exact matter-contraction amplitude
`f_NL^local = −35/16`, transmitted through the bounce to `f_NL^after ∈ [−0.65, −0.50]`; (b) the three research tracks
as *questions*, not paper IDs; (c) the current evidence grade per result, including that Track A's PTA, PBH and
high-z-PNG channels are **measured nulls** and the LSS channel is reachable but not separable at SPHEREx sensitivity
(0.7–0.9σ); (d) one click to the PDF, the derivation, and the reproduction manifest. Jargon is allowed here but never
unglossed — every ID (`A3M`, `namaster-proof`, `ECH Note`, `DESIVAST`) shows a plain-English purpose line beside it.

**A journalist or curious non-specialist** must get: the question in plain English, the honest state ("no detection
yet; three channels ruled out; one still open"), and a visible route into `/explained`. They must never meet a raw
paper ID, a readiness percentage, or a reviewer verdict letter before they meet the science. The words "0/8 pass" and
"three nulls" must arrive already framed as *findings*, never as broken widgets.

**A Hubify platform visitor** must get: this is the flagship reproducible lab — 3 programs, ~55 experiment manifests,
44 runnable now, ≈$36 total estimated reproduction cost, every artifact addressed by DOI/HF/B2 link, an API and MCP
surface for agents. That is the platform proof, and it earns a first-class nav slot (`/reproduce`), not a footnote.

**Four positioning commitments the design must physically enforce.**

1. **Evidence grade is a visual primitive, not prose.** Every result carries one of four grades — `measured`,
   `derived`, `null`, `open` — rendered as a typographic label with its own tonal color, used identically on the
   homepage, track pages, paper pages and the status page. A null is a contribution: it gets the same weight and a
   calm slate tone, never an error red.
2. **Nulls are headlined, not buried.** The homepage says "three channels closed as nulls" as a *result count*, in the
   same type as any positive claim. This is directive R6 made visible.
3. **Review convergence is back-of-house.** Verdict letters, wave counts and reviewer names move off the primary
   surface into `/reviews`, which is explicitly labeled as internal QA evidence — a gate, never the product
   (directive R2). No verdict letter appears on the homepage or on a paper page's hero.
4. **Readiness is one number with one source.** A single Convex-fed publication-readiness percentage per work, with
   the composition (science 25 / evidence 25 / review convergence 25 / packaging 20 / Houston's sign-off 5) shown on
   hover or on `/status` only. Venue, endorsement and submission live in a separate "publishing" strip that never
   subtracts from the score (directive P).

**Voice.** Declarative, quantitative, unhedged about uncertainty. Sentence case everywhere. No exclamation, no
marketing verbs, no "revolutionary". The register of a good PRD abstract, one notch warmer.
