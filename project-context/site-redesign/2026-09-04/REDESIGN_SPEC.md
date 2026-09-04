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
