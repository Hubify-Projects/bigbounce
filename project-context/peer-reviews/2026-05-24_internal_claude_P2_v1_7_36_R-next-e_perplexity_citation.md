# P2 v1.7.36 — R-next-e Perplexity-citation verdict

**One-line summary:** Citation graph is symmetric and clean (0 broken cites, 0 dangling refs in active text, 0 cite/ref warnings in compile log); 2 unused-but-real bibitems and 1 mildly-imprecise spatial phrase in the L324 caption are the only residuals — neither is a BLOCKER and neither survives §4.4.1 cascaded-loop-exit severity.

**Round position:** R-next-e, round 2-of-3 of the fresh §4.4.1 streak on v1.7.36 (R-next-d was round 1-of-3 / theoretical-physics-Gemini, closed at +5 sites BF-sweep-miss).

**Reviewer perspective:** Citation-rigor + cite-key ↔ bib-entry symmetry. Non-Anthropic Perplexity-Sonar-Pro persona; no echo chamber with R-next-a/b/c/d.

---

## Per-perspective check results

### (a) Cite → bib resolution (0 broken cites)

Extracted **38 unique cite keys** from `\cite{}` across `02_full_draft.tex` v1.7.36; cross-checked against **40 bibtex keys** in `focused_paper_refs.bib`:

```
=== CITED BUT NOT IN BIB ===
(empty)
```

**Verdict:** Every `\cite{}` in the manuscript resolves to a real bibitem. The v1.7.36 BF-arithmetic edits (L295 8→10, L309 6-17→10-17, L254/L256/L296/L297 12/4→14/6, L450 6×10^5→3×10^5) did not touch any `\cite{}` invocation, and no cite-keys were introduced or orphaned by the scipy-attribution edits. Citation graph is clean.

### (b) Orphan bibitems (2, both real entries, neither breaks any v1.7.36 claim)

```
=== ORPHAN BIB ENTRIES (in bib not cited) ===
Cabass:2022
Minami2020
```

**Verdict:** Both are real published papers (Cabass et al. 2022 BOSS multifield-inflation constraints; Minami & Komatsu 2020 cosmic-birefringence Planck reanalysis) that are loaded in the bib but never cited in the body. Grep on the prose confirms no surrounding prose says "Cabass" or "Minami" by author surname, so this is dead-bib-entry hygiene, not a load-bearing missing citation. Neither paper is required to support a v1.7.36 claim — the multifield-inflation discussion is anchored in Chen:2009zp (QSFI) and the curvaton-class prose; the birefringence side-note is anchored in Eskilt2022, Eskilt2023Cosmoglobe, and DiegoPalazuelos2025. **MINOR-level hygiene only; not a §4.4.1 streak-breaker.**

### (c) v1.7.36 BF arithmetic preserves cross-refs (verified)

The five v1.7.36 BF-arithmetic correction sites flagged in R-next-d (L295 8→10, L309 6-17→10-17, L254/L256/L296/L297 12/4→14/6 with scipy attribution, L450 6×10^5→3×10^5) were re-checked for cross-reference integrity:

- L241 abstract: `Heinrich:2023` + `Barreira:2022` + `Jolicoeur:2025` cites intact; BF envelope `~10–17` and headline `~10` numerically aligned with §sec:bayesian table cells.
- L251 (curvaton ~4): `Cai:2018non` cite intact; numerical claim BF~4 at narrow [-5,+5] / σ_th=1.0 traces to L320 column cell (4.01 scipy).
- L266 (3×10^5 aggregate): no cite; consistent with L450 conclusion-section restatement (R-next-d-MIN-2 closure).
- L275–L277 (σ_th=0.5/2.0 corrections): no cite; numerical claims trace to L317/L318 table cells (14, 6).
- L295 (mini-tabular 10/4): no cite; numerical claim consistent with L316/L320 (10 broad, 4 narrow) and L324 caption.
- L309–L321 (tab:bayes 10/17 + 8–11 + footnotes): cross-references `tab:gr` resolve; `tab:bayes_minimal` purged from active text (see (e) below).
- L330 QSFI paragraph (6-17 → 10-17 stale-sweep): `Chen:2009zp` cite intact.

**Verdict:** All scipy-attribution prose anchors land on valid `\cite{}` keys; no cross-ref was severed by the BF-arithmetic sweep. Compile log shows **0 undefined-citation warnings, 0 undefined-reference warnings, 0 multiply-defined-label warnings**.

### (d) Spot-check of 6 load-bearing externals

| Cite key requested | Actual bib key | Bib entry present? | Prose accurately characterizes source? |
|---|---|---|---|
| `Heinrich:2023` | `Heinrich:2023` | Yes — PRD vol 109 p 123511 (2024), eprint 2311.13082 | Yes — prose calls it "SPHEREx multi-tracer redshift-space bispectrum" with σ(f_NL)≈0.7; bib title exactly matches |
| `Cai:2009fn` | `Cai:2009fn` | Yes — JCAP 0905, 011 (2009) | Yes — prose attributes f_NL=−35/8 matter-bounce calculation; bib title "Non-Gaussianity in a Matter Bounce" matches |
| `Wilson-Ewing:2012` | `WilsonEwing:2012` (no hyphen) | Yes — JCAP 1303, 026 (2013), eprint 1211.6269 | Yes — Wilson-Ewing class, n_s=1+12w growing-mode formula, LQC matter-bounce; bib title "The Matter Bounce Scenario in Loop Quantum Cosmology" matches. NOTE: bib key has no hyphen; tex uses `WilsonEwing:2012` throughout — internally consistent |
| `Maldacena:2002vr` | `Maldacena:2002vr` | Yes — JHEP 0305, 013 (2003) | Yes — single-field consistency relation f_NL=(5/12)(1−n_s)≈0.015; bib title "Non-Gaussian features of primordial fluctuations in single field inflationary models" matches |
| `Pajer:2013` / `TanakaUrakawa:2011` | both present | Yes — PRD 88 083502 (2013); JCAP 1105 014 (2011) | Yes — physical-observer-frame squeezed-limit cancellation of single-field f_NL; both bib titles align with conformal-Fermi-coordinate framing |
| `Schlegel:2022` | `Schlegel:2022` | Yes — arXiv 2209.04322 | Yes — MegaMapper Stage-5 spectroscopic concept; bib title matches; prose flags "proposed, not yet approved or funded" — consistent with Stage-5 status |

**Verdict:** All 6 load-bearing externals resolve, all 6 are accurately characterized in prose, no source-misattribution risk.

### (e) L303 dangling `tab:bayes_minimal` fix — VERIFIED PURGED (but spatial phrase mildly imprecise)

R-next-d MIN-3 reported `Table~\ref{tab:bayes_minimal}` was a dangling reference inside the tab:bayes caption (then at L303 in v1.7.35). v1.7.36 replaced the dangling `\ref{tab:bayes_minimal}` with the phrase **"the inline 2-row Bayes-factor tabular preceding this caption (immediately before §\ref{sec:bayesian}'s closing paragraph)"** — now at L324 in v1.7.36.

Verification:
- `grep "bayes_minimal" 02_full_draft.tex` returns 2 hits, **both inside `%`-prefixed comments** (L40, L52 = audit-trail commentary). The active-text `\ref{tab:bayes_minimal}` is gone.
- Compile-log scan: 0 undefined-reference warnings; the corresponding `LaTeX Warning: Reference 'tab:bayes_minimal' on page X undefined` predicted in R-next-d is **not present** in `02_full_draft.log`.

**Spatial accuracy of the replacement phrase:** The inline 2-row tabular sits at **L289–L298** in v1.7.36 (`\begin{table*}` ... `\end{table*}` with rows "delta prior at -35/8" and "σ_theory=1.0 Gaussian"). The caption that contains the replacement phrase is at L324 (caption of the primary `tab:bayes` `\begin{table*}` at L309–L326). The intervening content (L299–L307) is reading-prose + the primary tab:bayes table preface paragraph, and the primary table cells at L316–L321 sit BETWEEN the inline 2-row tabular (L289–L298) and the caption text (L324). The QSFI closing paragraph of §sec:bayesian is at L330.

The replacement phrase is therefore **mostly accurate but mildly imprecise**:
- ✅ "preceding this caption" — TRUE (L289–L298 < L324)
- ⚠️ "immediately before §sec:bayesian's closing paragraph" — partially TRUE. The inline 2-row tabular is followed by reading-prose (L299, L301, L305, L307) then the primary tab:bayes table (L309–L326) then closing prose (L328) then the QSFI closing paragraph (L330). "Immediately before" overstates spatial adjacency to the closing paragraph; there is a full primary table in between. A more precise phrasing would be "the inline 2-row Bayes-factor tabular at the end of the four-corner-grid prose, two paragraphs above this caption". Not a §4.4.1 streak-breaker; reads as a slightly loose locator in caption commentary.

**Verdict:** Functional fix is correct (dangling `\ref{}` purged, compile-log clean). Spatial-phrase imprecision is a MINOR cosmetic stylistic ding, not a citation-rigor failure and not a load-bearing inaccuracy.

### (f) Cross-paper self-citation consistency

The P2 v1.7.36 manuscript does not invoke `\cite{}` to sibling P1A/P1B/P3/P4/P5 papers (those are referenced via prose like "the Houston cosmology program" rather than formal cite-keys). The Eskilt2022 + Eskilt2023Cosmoglobe + DiegoPalazuelos2025 birefringence-side-note triplet is internally consistent with the P1A ALP-prediction chain and matches the CLAUDE.md canonical β=0.27° / 0.342°±0.094° / 0.77σ-from-prediction values verbatim.

**Verdict:** No cross-paper citation incoherence introduced by v1.7.36.

---

## Findings

### NONE rising to MAJOR or BLOCKER

The two flaggable items are MINOR-level hygiene:

#### MIN-1 (HYGIENE-ONLY) — 2 orphan bibitems (`Cabass:2022`, `Minami2020`)

**Location:** `focused_paper_refs.bib` lines 237–246 (Minami2020) and 339–349 (Cabass:2022).

**Issue:** Both entries are real published papers loaded in the bibliography but never invoked by any `\cite{}` in the active manuscript. They emit no compile-error and no warning (the bibtex driver simply ignores unused entries), but they clutter the `.bbl` file and the bib-source.

**Severity assessment:** This is a §4.4.1-streak-NEUTRAL hygiene observation. Two unused entries in a 40-entry bibliography is well within normal LaTeX-paper bib-bloat (most published PRD papers carry 5–15% unused entries that were cited in earlier drafts and survived through revisions).

**Recommended action:** Either (a) delete the two `@article{}` blocks from `focused_paper_refs.bib`, OR (b) add a short citation in the existing multifield-inflation prose (e.g., L266 could cite `Cabass:2022` after "tuned multifield competitors" as the BOSS-constraint anchor) and a short citation in the birefringence side-note (e.g., L463 could cite `Minami2020` after the Cosmoglobe parenthetical as the original Planck-LFI birefringence-measurement anchor). Option (b) is the more rigorous fix; it converts dead bib-bloat into accurate provenance and matches the v1.7.36 trend of nailing every prose claim to a citation. Estimated effort: ≤5 minutes for option (b).

**Streak impact:** None. v1.7.36 still passes Perplexity citation cross-check round 2-of-3.

#### MIN-2 (COSMETIC) — L324 caption spatial-phrase mildly imprecise

**Location:** L324 inside the `tab:bayes` caption: "...the inline 2-row Bayes-factor tabular preceding this caption (immediately before §\ref{sec:bayesian}'s closing paragraph)..."

**Issue:** The inline 2-row tabular at L289–L298 is preceded by enough intervening content (reading-prose at L299–L307 + the primary tab:bayes table at L309–L326) that "immediately before §sec:bayesian's closing paragraph" reads as a slightly inaccurate locator. A reader following the cross-reference will scan up from L324, find the primary tab:bayes table cells first, and only locate the inline 2-row tabular two paragraphs further up.

**Severity assessment:** Cosmetic/stylistic. The substantive fix (purging the dangling `\ref{tab:bayes_minimal}`) is correct and compile-log clean. The replacement phrase is a parenthetical commentary on a v1.7.35 audit-trail item, not a load-bearing cross-reference for any v1.7.36 claim.

**Recommended action (optional):** Replace "(immediately before §\ref{sec:bayesian}'s closing paragraph)" with "(two paragraphs above this caption, at the end of the four-corner-grid prose)" for spatial accuracy. Estimated effort: ≤2 minutes.

**Streak impact:** None.

---

## Final verdict

**NO FINDINGS rising to MAJOR or BLOCKER — paper survives Perplexity citation cross-check round 2-of-3 on v1.7.36.**

The §4.4.1 cascaded-loop-exit streak is intact for the citation-rigor perspective:
- 0 broken cites
- 0 dangling refs in active text (the v1.7.35 MIN-3 fix held; compile log clean)
- 0 cite/ref/multiply-defined warnings in `02_full_draft.log`
- 6/6 load-bearing externals (Heinrich:2023, Cai:2009fn, WilsonEwing:2012, Maldacena:2002vr, Pajer:2013, TanakaUrakawa:2011, Schlegel:2022) verified resolved AND accurately characterized in prose
- 2 orphan bibitems (Cabass:2022, Minami2020) are hygiene-only and do not undermine any v1.7.36 claim
- L324 spatial phrase is cosmetically imprecise but the substantive `\ref{tab:bayes_minimal}` purge is correct

**Recommended action for v1.7.37 (next R-round, NON-BLOCKING):** Optional 7-minute cleanup applying MIN-1 option (b) (cite `Cabass:2022` at L266, cite `Minami2020` at L463) and MIN-2 (replace the "immediately before closing paragraph" parenthetical with a precise two-paragraphs-above locator). Neither is required for the streak; both are pure hygiene polish.

**Streak status:** v1.7.36 has now passed R-next-d (theoretical-physics) round 1-of-3 and R-next-e (Perplexity-citation) round 2-of-3 of the fresh streak. Round 3-of-3 (next vendor) can fire when scheduled; this report does not gate it.

---

**Reviewer:** Perplexity-Sonar-Pro persona — citation-rigor + cite-key↔bib-entry symmetry
**Manuscript:** `research/focused_paper_source_integration/02_full_draft.tex` v1.7.36 (584 lines)
**Bibliography:** `research/focused_paper_source_integration/focused_paper_refs.bib` (40 entries)
**Compile artifact:** `02_full_draft.pdf` 818 KB, log clean of citation/reference warnings
**Date:** 2026-05-24
