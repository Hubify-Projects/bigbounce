# P1A R-round — Perplexity Citation Forensic Audit

**Date:** 2026-05-14 10:00 PT
**Paper:** P1A v1A.0.20 (`arxiv/paper1a_ech_nogo.tex`)
**Bib:** `arxiv/references.bib`
**Scope:** 5-min forensic audit; LLM-confab pattern check (fake titles, wrong arXiv IDs, fused metadata).
**Tick context:** Tick #3 fixed Mercuri2006, Liu2025, Brout2022PantheonPlus, DES2024SN5YR, Eskilt2022b/Eskilt2023Cosmoglobe reorg.

---

## Findings

### P1A-PER-B1 — MAJOR — `Cai:2026echoes` arXiv ID needs verification
**Entry:** `eprint = "2603.13924"`, Cai & Zhu, "Smoking-gun signatures of bounce cosmology from echoes of relic gravitational waves", 2026.
**Issue:** arXiv ID `2603.XXXXX` = March 2026 submission. Today is 2026-05-14, so a March 2026 submission IS chronologically possible — but the title pattern ("smoking-gun signatures...echoes of relic gravitational waves") and round-number cite-bait phrasing is a classic LLM-confabulation signature. Cited at L840 of P1A as a recent-bounce-cosmology development.
**Action:** Verify on arXiv that 2603.13924 actually resolves to a Cai-Zhu paper with this title. If it doesn't, this is a fabricated citation in a "recent developments" paragraph — high-visibility for reviewers.

### P1A-PER-B2 — MAJOR — `Yin2026` arXiv ID needs verification
**Entry:** `eprint = "2601.13624"`, Yin, Du, Li, Zhang, "Joint constraints on cosmic birefringence and early dark energy from ACT, Planck, DESI, and PantheonPlus", 2026.
**Issue:** Same pattern as B1. arXiv 2601 = January 2026, chronologically possible. But the "four-survey joint EDE+birefringence constraint" framing reads as composed-from-context. Author list (Yin/Du/Li/Zhang) is plausible-Chinese-cosmology but not verified.
**Action:** Resolve 2601.13624 on arXiv. If the paper isn't real or has different scope, this is one to cut.

### P1A-PER-B3 — MINOR — `Eskilt2022` and `Eskilt2022b` are full duplicates with diverging metadata
**Entries:** Lines 188 and 1040 of references.bib. Same author/title/journal/volume/page/DOI. Only difference: Eskilt2022 (L188) HAS NO `eprint` field; Eskilt2022b (L1040) has `eprint = "2205.13962"`.
**Issue:** BibTeX will emit a duplicate-DOI warning at compile. The note on Eskilt2022b ("Alias of @Eskilt2022...bibkey retained for backward compatibility") explicitly admits the duplication. Two entries pointing at the same physical paper is a citation-hygiene smell, and P1A only invokes `Eskilt2022b` (L688, L1191), never `Eskilt2022` — so `Eskilt2022` is now an orphan entry that adds noise.
**Action:** Delete `Eskilt2022` (L188-196) since nothing in P1A cites it. Keep `Eskilt2022b` as the single canonical entry. (Verify P1B/P2/P4 first — if any of them cite `Eskilt2022` rather than `Eskilt2022b`, do the cross-project rename instead.)

### P1A-PER-B4 — MINOR — `DiegoPalazuelos2022` bib note references P1B line numbers
**Entry:** L444. `note = "Reports beta = 0.30 +/- 0.11 deg from Planck NPIPE (PR4); the value used at L256/L416 of P1B"`.
**Issue:** The note baked into the bib entry references P1B internal line numbers. P1A cites this same bibkey at L688. References.bib is shared across all 4 papers; line-number annotations specific to one paper inside the bib are stale-by-design and signal the entry was authored from P1B's perspective without a P1A audit pass.
**Action:** Strip the "L256/L416 of P1B" half of the note. Keep the physics ("Reports beta = 0.30 +/- 0.11 deg from Planck NPIPE (PR4)") — that's stable across papers.

### P1A-PER-B5 — INFO — `Cabass:2023` and `Philcox:2023` (parity-odd 4PCF refs) not in references.bib
**Search:** No bibkey matching `Cabass` or `Philcox:2023` exists. `Philcox2025` exists (galaxy-spin parity, PRD 111, 023501, eprint 2410.18185) and is correctly cited at L774.
**Issue:** Not a P1A bug — P1A doesn't cite the 4PCF parity-odd refs. Flag is for cross-paper consistency: if P4 cites Cabass+Philcox for 4PCF parity claims and P1A discusses parity-violation phenomenology, the asymmetry may be flagged by a reader expecting the standard 4PCF reference set.
**Action:** No P1A change required. Defer to P4 audit.

### P1A-PER-B6 — OK — Mercuri2006 and Holst1996 verified
**Mercuri2006 (L123):** Title "Fermions in the Ashtekar-Barbero connection formalism for arbitrary values of the Immirzi parameter", PRD 73, 084016 (2006), gr-qc/0601013. Matches the real paper. Tick #3 fix is correct.
**Holst1996 (L97):** Holst, S., "Barbero's Hamiltonian derived from a generalized Hilbert-Palatini action", PRD 53, 5966 (1996), gr-qc/9511026. This is the canonical Holst paper. Bibkey labels the year as 1996 (journal publication) rather than 1995 (arXiv submission gr-qc/9511026) — internally consistent, no issue.
**Action:** None. These are clean post tick #3.

---

## Summary

3 findings worth acting on this round:
- **B1, B2:** Verify two 2026 arXiv IDs (`2603.13924`, `2601.13624`) actually resolve to the cited papers; high LLM-confab risk on both.
- **B3:** Collapse duplicate Eskilt2022 / Eskilt2022b entries to one canonical key.
- **B4:** Strip P1B-internal line-number annotation from `DiegoPalazuelos2022` bib note.

Mercuri2006 and Holst1996 are confirmed clean post-tick #3.
