# P3 R24conf — Claude brutal-referee
**Reviewer**: `Claude_brutal`
**Model**: `claude (in-session, subscription)`
**Input PDF**: `site/public/papers/paper3_anomaly_catalog_v3.1.81.pdf` md5=aa791276 pages=24
**Input format**: NATIVE PDF (in-session Read) + pass-2 self-critique

---

## Pass-1 findings (native PDF read, 24 pages, two-column revtex)

### P3-E1 — Title still advertises "Path-C Unique" + "Native-Trained Novelty Fractions" without the headline scope qualifier
**Severity**: Editorial (referee would call MAJOR, but factually defensible)
**Where**: title page, p.1
**Issue**: The title reads "378,280 Path-C Unique Anomalies and Native-Trained Novelty Fractions from 37.3 Million Sources and Map Patches." A neutral astro-ph reader will parse "Native-Trained Novelty Fractions" as a per-survey novelty fraction reported on the native-retrained pool. The actual genuine-novelty fraction in the abstract (17.8%) is computed from the **cross-transfer-era** DESI top-1,000 against CDS X-Match, not from each survey's native-retrained anomaly list. The 58.8% SIMBAD-unmatched figure is also pooled-cross-transfer (§IV A). Recommend either (a) softening to "Native-Retrained Catalog and Cross-Match Novelty Fractions" or (b) adding a one-sentence abstract footnote clarifying that the 17.8% novelty is the DESI top-1,000 CDS X-Match figure rather than a survey-wide native rate.
**Status**: OPEN — author choice; not a blocker but a near-certain reviewer hit.

### P3-M1 — "264,938 = DESI+SDSS+eROSITA+Planck+Gaia+NEOWISE" footnote is opaque without an SDSS-tier disclosure
**Severity**: MAJOR
**Where**: abstract (p.1, "recommended catalog-grade subset is ∼265,000 unique entries (264,938 …)"); §IV C dedup math (p.11).
**Issue**: Recomputing the recommended subset:
- 195,829 (DESI) + 77,905 (SDSS native continuity slice) + 113,342 (LAMOST) + 298 (eROSITA) + 200 (Planck) + 500 (Gaia) + 419 (NEOWISE) = **388,493** ✓ (matches §IV C)
- 388,493 − 113,342 (drop LAMOST exploratory) − 10,213 (7-way dedup) = **264,938** ✓
- 264,938 − 200 (drop Planck map patches) = **264,738** ✓

The arithmetic is internally consistent **but the abstract footnote does not disclose which SDSS tier is being counted into 264,938**. A reviewer who instead uses the SDSS top-1% score-knee (19,253, footnote ♡) gets 264,938 − (77,905 − 19,253) = 206,286, which contradicts the abstract. Recommend a one-clause disclosure in the abstract footnote: "(SDSS contribution: 77,905-object native continuity slice; using the 19,253-object SDSS top-1% slice instead would shift the recommended subset to ~206,000)" so the multi-tier SDSS bookkeeping the paper already documents in Table I footnote ♡ is propagated to the headline subset count.
**Status**: OPEN — strongly recommended fix.

### P3-M2 — Single-tracer baseline σ(f_NL)=8.98 vs Fig.11 baseline 16.85 is reconciled in the App-C "Normalization note" but not in §V
**Severity**: MAJOR (clarity, not factual)
**Where**: §V Fisher forecast (p.14): σ_std=8.98. Fig.11 (p.20): "Baseline single-tracer (σ(f_NL)=16.85)" with App-C "Normalization note" that explicitly says the two are on different normalizations.
**Issue**: A referee not reading every appendix footnote will see two different "baselines" — 8.98 in the abstract and §V, and 16.85 in the Fig.11 dashed line — and will flag a 2× discrepancy. The App-C "Normalization note" is the right disclosure but is buried after Table VII. Recommend pulling that one sentence ("the σ(f_NL)=16.85 dense-limit baseline of Fig.11 is on a 5-tracer P(k) normalization distinct from the §V 7-bin σ_std=8.98; only relative quantities transfer") into either §V near Eq. above 8.14, or into the Fig.11 caption body, not the appendix.
**Status**: OPEN — referee-clarity fix.

### P3-M3 — 9.4% improvement is recomputed-consistent but the de-biased result σ=8.98 with "no improvement" needs to be the headline number, not just a parenthetical
**Severity**: MAJOR
**Where**: abstract; §V; §VII conclusion item 5.
**Issue**: Arithmetic check: (8.98−8.14)/8.98 = 9.354% → 9.4% ✓ . The paper is honest in §V that "the de-biased amplitude max(0, 0.19² − 0.65²) = 0 returns the single-tracer baseline σ(f_NL)=8.98 exactly (no improvement)." This is the correct, statistically defensible result. The abstract and §VII headline still lead with "9.4% improvement consistent with no improvement at <1σ." The current phrasing is not wrong, but a brutal referee will say: if the de-biased estimate is exactly 8.98, lead with **8.14_{−4.22}^{+0.84} (single-tracer-consistent)** and put 9.4% in a parenthetical, not the other way around. Recommend an abstract rephrase: "σ(f_NL) = 8.14 (1σ envelope [3.92, 8.98]; de-biased point estimate returns the single-tracer baseline 8.98 — central value is a forecast pending higher-S/N follow-up, not a detection." This is the same content, just non-promotional.
**Status**: OPEN — referee will catch this even if it's all in the body already.

### P3-M4 — NANOGrav Bayes factor B_MB/SMBHB = 7.14×10³ called "decisive" without an explicit prior dependence statement at the headline level
**Severity**: MAJOR
**Where**: abstract ("Savage-Dickey B_MB/SMBHB = 7.1×10³"); §V A (p.14); §VII item 5.
**Issue**: Recomputing: B_MB/free = 3.23, B_SMBHB/free = 4.52×10⁻⁴ → ratio = 3.23/4.52e-4 = 7,146 → 7.14×10³ ✓, log₁₀ = 3.854 ✓. The σ-test arithmetic also checks: (3.0 − 2.567)/0.382 = 1.133σ ✓; (4.33 − 2.567)/0.382 = 4.615σ ✓. **However**, the headline phrasing "Savage-Dickey B_MB/SMBHB = 7.1×10³" without "under γ-uniform prior on [0,7]" attached to the abstract claim invites the standard referee objection that Savage-Dickey is prior-sensitive and the flat γ∈[0,7] prior is a uniform-prior modeling choice. The full disclosure is in §V A and App. E (`flat priors γ ∈ [0,7]`) but the abstract should attach the same qualifier in one parenthetical. Also: the SMBHB γ=4.33 value [Sesana 2016 / Burke-Spolaor 2019] is a sample-mean across a heterogeneous SMBHB population literature; a referee will want a one-line note that the 4.61σ tension assumes γ=4.33 as a sharp prediction rather than a population-level expectation with intrinsic scatter.
**Status**: OPEN — abstract qualifier + one-line SMBHB-population caveat needed.

### P3-M5 — "17.8% genuine novelty" is a top-1,000 score-stratum point estimate; abstract carries the Wilson ±1.2% in body but not in abstract
**Severity**: MAJOR (referee-flag near-certainty)
**Where**: abstract, p.1 ("genuine novelty fraction of ∼17.8% (single-sample point estimate at the top-1,000 score stratum; full-catalog rate empirically untested)"); §IV A (p.10).
**Issue**: The paper does the right thing in §IV A — "Wilson 68% binomial interval (17.8% ± 1.2%)" and "the genuine novelty fraction is substantially smaller than the SIMBAD-unmatched population." The abstract gives the point estimate without the Wilson CI. Recommend "∼17.8% (Wilson 68% CI ±1.2%; single-sample, top-1,000 stratum only)" in the abstract — the body number is already there and is correctly stated, this is a no-cost upgrade that pre-empts the inevitable referee comment.
**Status**: OPEN — trivial fix, large referee-deflection value.

### P3-m1 — 6500× SDSS rate compression rests on a S>5 → 12-source comparison that needs a stronger framing in the abstract
**Severity**: MINOR
**Where**: abstract ("∼6500× SDSS rate compression"); §III C; Table I footnote ‡.
**Issue**: 77,905 / 12 = 6,492 ≈ 6500 ✓. But the comparison numerator (77,905 at S≥0.1060) and denominator (12 at S>5) use **different thresholds** — this is the catalog-calibration-domain-shift diagnostic the paper wants to highlight, not an apples-to-apples rate compression. The body discloses it ("only 12 sources at S>5 vs. cross-transfer 77,905"), but the abstract reader will mis-read 6500× as a same-threshold compression. Recommend "21.5× LAMOST rate compression at S>5 and a ~6500× SDSS catalog-calibration-domain-shift diagnostic (S>5 native re-score yields only 12 of 77,905 cross-transfer sources)" in the abstract.
**Status**: OPEN.

### P3-m2 — Fig. 1 caption distinguishes "83-object gold-tier visualization set" from "116-object GOLD QSO-candidate confidence tier" but the rest of the paper still uses "gold" in both senses
**Severity**: MINOR
**Where**: Fig. 1 caption (p.2); §V cosmological-applications text (p.14, "GOLD (N=116)" and the 1,122 = 116 + 1,006 tier).
**Issue**: The disambiguation is explicit and correct. But the §VII conclusion item ("83-object gold-tier visualization set") never re-anchors the reader: a referee skimming the conclusion may double-count. Recommend a parenthetical reminder in §VII: "(distinct from the 116-object GOLD QSO-candidate confidence tier of §V)."
**Status**: OPEN — trivial.

### P3-m3 — Fig. 8 panel-(a,b) score annotations (3.2, 2.8) deliberately disclosed as figure-script values, but caption is dense
**Severity**: MINOR
**Where**: Fig. 8 caption (p.13).
**Issue**: The disclosure is correct ("the panel (a, b) annotations (3.2, 2.8) are not the catalog selection scores"). This was the R23 fix and is preserved. No action.
**Status**: CLOSED — deliberate per calibration; flagged only for completeness.

### P3-m4 — Table I "LAMOST 44,075 / Rate 0.39%" header row contradicts the §III D body text ("21.5× compression to 2,054 at S>5")
**Severity**: MINOR
**Where**: Table I (p.8); §III D (p.6, last full paragraph).
**Issue**: Table I LAMOST headline row reports **44,075** at the **cross-transfer** column (consistent with the "before/after" disclosure in §II D), with footnote † saying the Path-C native-retrained value is 113,342. The S>5 native count is 2,054 (the rate-compression diagnostic). A referee scanning Table I sees three different LAMOST numbers (44,075 / 113,342 / 2,054) and must follow three footnotes to reconcile. Recommend either (a) collapsing Table I to show only the Path-C native column with the cross-transfer column moved to an appendix table, or (b) adding a one-line summary row "LAMOST Path-C native S>5: 2,054 (rate-compression diagnostic, exploratory)" at the bottom of Table I.
**Status**: OPEN — readability fix.

### P3-N1 — eROSITA SIMBAD-unmatched 68% in Table I vs 100% in body for the top-298 IF-cross-validation pool
**Severity**: NIT
**Where**: Table I (p.8, "68%"); §IV A (p.10).
**Issue**: The 68% Table I figure is the survey-wide top-298 SIMBAD-unmatched fraction; the 100% archival ID rate in §IV A is for the **extended NED+VizieR** cross-match, not SIMBAD-only. The body is clear that these measure different things. No action required, but a sentence in Table I caption pointing to §IV A would help.
**Status**: OPEN — optional polish.

### P3-N2 — Page-1 abstract Bayes factor "7.1×10³" vs §V/Table-IV body value "7.14×10³"
**Severity**: NIT
**Where**: abstract (p.1, "7.1×10³"); §V A (p.14, "7.14×10³"); Table IV (d) (p.17, "7.14×10³"); §VII (p.17, "7.14×10³").
**Issue**: The abstract truncates to 7.1×10³ while the body retains 7.14×10³. Internally consistent to one-sig-fig, but a brutal referee will say "match the precision of the headline number to the body." Recommend abstract → 7.14×10³.
**Status**: OPEN — trivial.

### P3-N3 — App. F "388,693 − 10,213 = 378,480" sensitivity-check arithmetic vs the canonical 388,493 − 10,213 = 378,280
**Severity**: NIT
**Where**: App. F (p.20, "The 8-way-with-ACT dedup variant … would have produced 388,693 − 10,213 = 378,480 unique objects (+200 relative to the headline)").
**Issue**: Recomputing: 388,493 (canonical with Planck) + 200 (ACT add-in) = 388,693 ✓; 388,693 − 10,213 = 378,480 ✓; 378,480 − 200 (ACT) = 378,280 ✓. Arithmetic is correct. The sentence is dense — a reader has to do three additions in their head. No action required.
**Status**: CLOSED — verified.

### P3-N4 — `log_{10}A = −14.025 ± 0.380` posterior summary uses Gaussian-approximation σ for an "asymmetric 68% CI" report style elsewhere
**Severity**: NIT
**Where**: §V A and App. E.
**Issue**: γ is given with both ±0.382 (Gaussian) and ^{+0.291}_{-0.287} (asymmetric quantile); log₁₀A is given only as ±0.380 (Gaussian). For consistency, App. E should add the asymmetric-quantile summary for log₁₀A.
**Status**: OPEN — polish.

---

## Explicit all-clears (deliberately not flagged)

- **378,280 = 378,080 + 200 headline arithmetic**: verified ✓ (multiple sites).
- **Wilson 68% CI ±1.2% on 17.8% novelty**: 17.8% × (1 − 17.8%) / 1000 → σ ≈ 1.21%, 68% z ≈ 1, Wilson ±1.2% ✓.
- **Liang2023 comparison "141× / 73×"**: 378,080 / 2,685 = 140.8 → 141 ✓; 195,829 / 2,685 = 72.9 → 73 ✓.
- **NANOGrav σ tests**: 1.13σ ✓; 4.61σ ✓.
- **Bayes factor ratio**: 3.23 / 4.52×10⁻⁴ = 7146 ≈ 7.14×10³ ✓; log₁₀ = +3.85 ✓.
- **Fisher 9.4%**: (8.98 − 8.14)/8.98 = 9.35% ✓.
- **Fisher 6.1% fixed-α reference**: (8.98 − 8.43)/8.98 = 6.12% ✓.
- **Dedup compression 2.629% / 2.63%**: 10,213 / 388,493 = 2.629% ✓.
- **Gold + Silver tier 116 + 1,006 = 1,122**: ✓ (deliberate per calibration, R23 fix preserved).
- **77,905 UMAP input set**: deliberate, R23 closure verified.
- **f_NL = −35/8 = −4.375**: ✓.
- **June 2026 date, release-status, LAMOST tier retention, ACT quarantine**: deliberate per calibration — NOT flagged.
- **9.4%-vs-no-improvement framing**: present in body — flagged only as P3-M3 abstract-prominence issue, not a math error.

---

## Pass-2 self-critique (cross-check vs `pipelines/p3_anomaly_engine/paper3_draft.tex`)

Pass-2 re-grep of the source confirms:
- Every arithmetic claim flagged above resolves correctly against the .tex source (line 134 abstract block, line 559 Fisher §V, line 590 NANOGrav §V A, line 494 dedup §IV C, line 634 caveat (i), line 670 §VII).
- The 388,493 → 264,938 → 264,738 subset chain is verified end-to-end against §IV C (line 494) and the abstract (line 134).
- The two-baseline σ(f_NL) issue (P3-M2) is real: Fig.11 (App C, line ~816 region) explicitly distinguishes 16.85 from 8.98 with a "Normalization note" — the finding is that this disclosure is too deep, not that it's missing.
- The "decisive Bayes factor without prior-uniform qualifier in abstract" issue (P3-M4) — the body (line 590) and App E (line 864) explicitly state `flat priors γ ∈ [0,7]`, but the abstract (line 134) and §VII (line 670) do not re-attach the qualifier. Pass-2 confirms the finding.
- The SDSS-tier ambiguity in the abstract footnote (P3-M1) — the .tex (line 134) names "DESI + SDSS + eROSITA + Planck native + Gaia + NEOWISE" but does not specify which SDSS tier; pass-2 confirms this is a genuine abstract-clarity gap, not a math gap.

**Self-critique downgrades**: none. **Self-critique upgrades**: P3-M5 (Wilson CI in abstract) was initially MINOR; upgraded to MAJOR because external reviewers consistently flag headline novelty fractions without confidence intervals — this is a high-probability referee hit at near-zero fix cost.

No new findings surfaced in pass-2.

---

## Summary recommendation

v3.1.81 is materially improved over the R23 baseline: all four R23 closure items (9.4%-definition anchor, ACT caption quarantine, 77,905 UMAP input set, Fig-8 score-axis disclosure) are verified in place, the 116+1,006=1,122 gold/silver tier definitions are crisp, and the FoF dedup audit is documented. The numerical claim web (378,280 / 388,493 / 10,213 / 264,938 / 264,738 / 17.8% / 9.4% / 6.1% / 1.13σ / 4.61σ / 7.14×10³ / 141× / 73×) re-computes cleanly end-to-end.

The remaining findings are all **abstract/headline-clarity issues**, not factual errors: every single one of P3-E1, M1, M2, M3, M4, M5 is a "the body already says this correctly, but the abstract or §VII headline does not propagate the qualifier" pattern. None block submission. All six together would take ≲30 min to address and would deflect the most likely referee comments.

**Verdict**: ACCEPT WITH MINOR REVISIONS (referee terminology: "publish as is or with the editorial revisions listed").

**Counts line**: P3-E:1, P3-M:5, P3-m:4 (1 closed), P3-N:4 (1 closed); open = 1E + 5M + 3m + 3N = 12 open.
