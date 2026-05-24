# R9 Cross-Model Verification Review — P5 v0.1.29

**Date:** 2026-05-24
**Reviewer:** Internal Claude (Anthropic-default + DeepSeek-statistical-archaeology + Perplexity-citation-rigor)
**Paper:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` v0.1.29-2026-05-24, 29 pp / 1,517 lines
**Prior rounds:** R1–R8 (R8 found 3 MAJOR + 2 minor → broke 4-clean streak)
**Mode:** R9 is a cross-model verification round — (a) Anthropic verification of R8 closures, (b) DeepSeek-statistical-archaeology + Perplexity-citation-rigor sweep.

---

## (a) Verification of the 5 R8 closures landed in v0.1.29

| # | R8 closure | Location | Verdict |
|---|---|---|---|
| 1 | Abstract "statistically independent" → quantified sensitivity floor | Abstract lines 82–87 | **PASS** — "no environment dependence above the sensitivity floor … ~0.2 pp for V-Web filament/cluster (n ≳ 4×10⁵) and ~5 pp for V-Web void (n=428)" present and quantitative. |
| 2 | Tempel promoted to load-bearing; DESIVAST demoted | Abstract lines 112–122 | **PASS** — "filament-class concordance 0.026 pp; this is the load-bearing external-classifier validation" and DESIVAST quartet now flagged "methodologically correlated by construction because they reuse the same matched-spiral subsample". |
| 3 | Bright-vs-dark sign-flip reframed | Abstract lines 148–158 | **PASS** — filament class joint z ≈ 3.4σ called "consistent with BGS-selection-function origin"; cluster joint z ≈ 0.5σ explicitly labeled "sample-size-limited (n_dark=4,234) and does not independently confirm or refute". |
| 4 | §VII.D P4-monopole arithmetic reconciliation 9.5σ→4.62σ | Lines 1187–1199 | **PASS, with one precision caveat (minor #1 below).** Verified: 2·0.0026·√791,635 = 4.6266 ≈ 4.62σ ✓. 9.5σ ⇒ N_P4 ≈ 3.34M (matches Paper IV ~3.2M spirals) ✓. Observed 5.00σ ⇒ Δ_P5 = 0.00281 ⇒ 8.0% larger than Δ_P4 = 0.0026 ✓ (actually 7.7% but "~8%" defensible). |
| 5 | §VIII.B bounce-vs-inflation reframed to upper bound | Lines 1319–1332 | **PASS** — "does not currently discriminate … the null instead establishes an observational upper bound that any future parity-violating model proposing an environment-dependent chirality signature must respect." Cleanly removes the "consistent with both" framing. |

**All 5 R8 closures verified arithmetically + textually correct.** No regressions detected.

---

## (b) DeepSeek-statistical-archaeology + Perplexity-citation-rigor sweep

### Finding 1 — MINOR (statistical-archaeology, misleading precision)

**Claim:** "σ_pred^P5 = 2·0.0026·√791,635 ≈ 4.62σ" (line 1192–1193).

**Issue:** Δf_CW^P4 = -0.0026 is implicitly only 2 significant figures (Paper IV gives 0.4974 ± 0.000279 ⇒ Δ ∈ [-0.00288, -0.00232] at 1σ). Quoting σ_pred to 3 sig fig (4.62σ) propagates spurious precision from a 2-sig-fig input. Sensitivity check:
- Δ = 0.0025 → σ_pred = 4.45
- Δ = 0.0026 → σ_pred = 4.63
- Δ = 0.0027 → σ_pred = 4.81

The reconciliation conclusion (Δ_P5 ≈ 0.0028, "~8% larger") is robust to this, but the headline "≈ 4.62σ" should read **"≈ 4.6σ"** to match input precision. Below MAJOR threshold but a textbook DeepSeek-class catch on misleading precision.

**Fix:** s/4.62\sigma/4.6\sigma/ in §VII.D. Two-character edit.

### Finding 2 — MINOR (statistical-archaeology, metric inconsistency)

**Claim:** Sensitivity floors in the abstract — "~0.2 pp for V-Web filament/cluster (n ≳ 4×10⁵) and ~5 pp for V-Web void (n=428)" (lines 85–87).

**Issue:** The two floor values use *different metrics*:
- Filament/cluster ~0.2 pp ≈ the Paper IV catalog-monopole offset (0.26 pp). I.e. "floor = systematic monopole."
- Void ~5 pp ≈ 2× the 1σ counting noise at n=428 (1σ = 2.42 pp; 2σ = 4.83 pp). I.e. "floor = ~2σ statistical."

Naming both "the sensitivity floor" without acknowledging that the binding floor changes from systematic-dominated (filament/cluster) to statistical-dominated (void) is the kind of slippage a referee would flag. Defensible but inconsistent metric across the same sentence.

**Fix:** One-clause addition: "...where the binding floor is the Paper IV catalog-monopole (filament/cluster) and counting statistics (void)."

### Finding 3 — MINOR (citation rigor, bibliography metadata)

**Claim:** Abstract cites "four DESIVAST-anchored re-projections" using **three** algorithms (VoidFinder + V2-REVOLVER + V2-VIDE) from **one** DESIVAST catalog (`DESIVAST2025`, Douglass et al. 2025, ApJ 982, 38).

**Issue:** Bibliography is internally consistent — one Douglass+2025 entry covers all three algorithms within the same DESIVAST data release, so a single bibitem is correct. But two subtle citation-rigor points a Perplexity-style reviewer would catch:

1. The Douglass+2025 DESIVAST entry uses author list "S. B. Douglass et al." — the published ApJ 982, 38 (2025) lists Zaidouni, Bao, & Douglass as first three authors with Douglass as PI on the catalog release. Verify first-author convention against ApJ record (this may already be correct; flagging for sanity-check, not asserting wrong).
2. `TWebDESI2026` and `ASTRADESI2026` bibitems (lines 1498–1507) are cited as DESI Collaboration / Zapata-Zuluaga et al. but I don't see either invoked in the text of v0.1.29 — they may be orphaned (used in earlier draft, retained after restructure). Quick `grep '\\cite{TWebDESI2026\\|ASTRADESI2026}'` would confirm.

**Fix:** (1) cross-check ApJ 982, 38 first-author order; (2) prune orphaned bibitems if unused.

---

## (c) Single sharpest critique

**Finding 1 (the 4.62σ misleading-precision)** is the sharpest, because R8's closure #4 was the headline arithmetic reconciliation — the entire credibility of "8% residual explained by BGS-bright weighting" depends on the σ_pred value, and quoting it to 3 sig fig when the input is 2 sig fig invites a "your 5.00σ–4.62σ residual is just rounding noise" pushback from an external statistical referee. Trivial fix (drop one digit), high credibility return.

---

## (d) §4.4.1 streak-attempt readiness

**R9 finding count:** 0 BLOCKER + 0 MAJOR + 3 minor + 0 nit.

**§4.4.1 threshold:** 0 BLOCKER + 0 MAJOR + ≤2 minor.

**Verdict: NOT QUITE READY for a fresh streak attempt — 3 minor exceeds the ≤2 minor bar by exactly one.** Two of the three minors (Finding 1 misleading precision, Finding 2 metric inconsistency) are sub-5-minute textual fixes; Finding 3 is a 2-minute orphan-bibitem grep. After landing v0.1.30 with these three fixes, the next R-round should cleanly hit §4.4.1 and re-open the streak. The paper's headline science is solid; this is final-mile polish.

**Recommendation:** Land all three fixes in a single v0.1.30 commit, recompile (mandatory post-compile visual audit per global protocol), then attempt R10 for §4.4.1 streak re-entry.
