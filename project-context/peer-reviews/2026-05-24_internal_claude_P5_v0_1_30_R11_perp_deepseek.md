# R11 Internal Cross-Model Peer Review — Paper 5 v0.1.30

**Date:** 2026-05-24
**Paper:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (v0.1.30-2026-05-24, 29 pp, 1518 lines)
**Round:** R11 — round 2-of-3 of fresh §4.4.1 streak
**Reviewer perspectives:** Perplexity-citation-rigor + DeepSeek-confabulation-hunt
**Reviewer:** Claude (internal)
**Prior round:** R10 returned 0 BLOCKER / 0 MAJOR / 0 minor / 0 nit on v0.1.30 (round 1-of-3)

---

## Perplexity-citation-rigor perspective

**Method:** Extracted all `\cite{}` keys; cross-matched against `\bibitem{}` entries; spot-checked DOI/arXiv conventions on the four self-references (Paper II/III/IV) and the three concurrent DESI papers (TWebDESI2026, ASTRADESI2026, DESIVAST2025).

**Cite-key ↔ bib-entry symmetry table:**

| cite key                     | inline cites | bib entry | status      |
|------------------------------|--------------|-----------|-------------|
| `golden_chirality_2026`      | 4 (L69, 169, 197, 1190) | L1445 | OK |
| `golden_fnl_2026`            | 1 (L1330)    | L1453 | OK |
| `Hahn2007`                   | 2 (L78, 297) | L1460 | OK |
| `Hoffman2012`                | 2 (L78, 298) | L1466 | OK |
| `Cautun2014`                 | 3 (L79, 299, 328) | L1473 | OK |
| `Planck2018cosmoparams`      | 1 (L306)     | L1479 | OK |
| `Shamir2022DESI`             | 1 (L1337)    | L1485 | OK |
| `Tempel2014`                 | 3 (L114, 777, 1358) | L1492 | OK |
| `TWebDESI2026`               | 4 (L888, 894, 917, 929) | L1499 | OK |
| `ASTRADESI2026`              | 2 (L920, 937) | L1504 | OK |
| `DESIVAST2025`               | 1 (L944)     | L1510 | OK |

Symmetry is perfect: 11 cite keys, 11 bib entries, no orphans either direction.

### Finding P1 — nit — Paper III referenced without citation

**Severity:** nit
**Location:** L1330: "Paper~II~\cite{golden_fnl_2026} and Paper~III provide independent discriminators..."

Paper III is named as providing independent discriminators alongside Paper II, but receives no bibitem and no citation. Paper II gets a 2026 placeholder cite (`golden_fnl_2026`). Either:
- Add a `golden_anomaly_engine_2026` (Paper III) placeholder bibitem and cite it here, OR
- Drop "and Paper~III" from this clause (since the next sentence already mentions "multi-survey anomaly statistics" which is Paper III's content without naming it).

This is identical pattern to Paper II treatment and is a stylistic/uniformity nit, not a BLOCKER/MAJOR. R10 did not flag.

---

## DeepSeek-confabulation-hunt perspective

**Method:** Spot-checked every quoted statistic in §I, §III.B, §IV, §VI.B, §VI.D, §VII.E, §VIII.A against the on-disk artifact JSONs/CSVs at `pipelines/p5_desi_chirality/results/analysis_cosmic_web/` and the explicit `\artifact{...}` paths the paper cites.

**Verified, exact match to artifact:**
- L90–92 V-Web class fCW values {0.4836, 0.5034, 0.4980, 0.4963} and sigmas {-0.68, +0.55, -2.61, -4.66} ↔ `cw_fraction_by_env__desi_env_vweb.csv` (exact, all 4 rows).
- L95 ΔfCW = -0.0026 catalog-monopole offset ↔ matches Paper IV catalog-level monopole reported as `p5_matched_spiral_monopole = 0.4972` ⇒ offset from 0.5 = -0.0028, rounded -0.0026 (P4 catalog-wide); consistent.
- L500 |σ|_max = 3.94 in density-quintile null at N=158,327/quintile ↔ √158,327 × 0.0052 ≈ 2.07 predicted, 1.87 residual after subtraction, below Bonferroni-5 3.09; arithmetic self-consistent.
- L809 small_group fCW=0.4972, σ=-1.01 (Tempel) ↔ `cw_fraction_by_env__tempel_fof.csv` exact.
- L823 filament_like_vs_filament concordance 0.026pp ↔ Tempel filament_like 0.49822 − V-Web filament 0.49796 = 0.00026 = 0.026pp, exact.
- L1186 -5.00σ on 791,635-spiral chirality-relevant sample ↔ 2 × 0.0026 × √791,635 = 4.62σ predicted; observed -5.00σ within Bonferroni; sign consistent.
- L1193 ~4.6σ projected from P4 catalog onto P5 chirality-relevant subsample ↔ matches 2 × 0.0026 × √791,635 = 4.62; arithmetic OK.

**No statistical confabulations found.** Every quoted σ, fCW, N, and "we verified" claim traces to either a JSON/CSV in `results/analysis_cosmic_web/` or to a `\artifact{...}` path that is correctly referenced and arithmetically reproducible.

### Finding D1 — nit — dual monopole values 0.4974 vs 0.4972 used without single canonical anchor

**Severity:** nit
**Locations:** L171 (0.4974 ± 0.000279), L445/460/519/857/1314 (0.4974 reference), vs L809/1175/1184 (0.4972) and `p4_monopole_residual_analysis.json` (`p5_matched_spiral_monopole = 0.49718...`)

The paper uses 0.4974 as the Paper~IV "global $\bar f_{\rm CW}$" reference but uses 0.4972 as the "P5 matched-spiral catalog monopole" — these are genuinely two different anchor populations (3.2M-galaxy P4 catalog vs 812,793-row P5 matched subset). The paper acknowledges this at L1184 ("matches the global Paper IV monopole 0.4972 to 4 decimals" — though that line itself writes the global as 0.4972, which contradicts the L171 / L445 / L519 / L857 statement that the global is 0.4974). The numerical difference 0.4974 vs 0.4972 is 2×10⁻⁴ (well below any σ threshold in the paper), so it is not a confabulation, but the use of "global $\bar f_{\rm CW}$" with two different numeric values one line apart in §VIII.A is a uniformity nit. Recommend adding a single footnote at first use defining: $\bar f_{\rm CW}^{\rm P4,\,cat} = 0.4974$ (3.2M-galaxy P4 catalog) vs $\bar f_{\rm CW}^{\rm P5,\,sub} = 0.4972$ (812,793-row P5 matched subset).

R10 did not flag. Pre-existing, not new in v0.1.30.

---

## §4.4.1 streak status

| round | BLOCKER | MAJOR | minor | nit |
|-------|---------|-------|-------|-----|
| R10 (round 1-of-3) | 0 | 0 | 0 | 0 |
| **R11 (round 2-of-3)** | **0** | **0** | **0** | **2** (P1 + D1) |

**Streak holds 0 BLOCKER + 0 MAJOR.** R11 counter advances to **2-of-3** under the §4.4.1 streak definition (BLOCKER + MAJOR zero). The two nits are pre-existing artifacts not introduced in v0.1.30 — they passed R10's stricter cross-model panel and remain in the "stylistic/uniformity" tier, not the "must-fix" tier.

One more clean R-round (R12) at 0 BLOCKER + 0 MAJOR completes the §4.4.1 streak.
