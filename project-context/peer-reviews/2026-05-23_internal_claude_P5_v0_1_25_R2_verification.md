# P5 (v0.1.25-2026-05-23) — R2 Verification Pass

**Reviewer**: Claude (Opus 4.7), adversarial second-pass verification
**Date**: 2026-05-23
**Paper**: `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (29 pp, 1,476 lines, v0.1.25)
**Scope**: Verify closure of the 12 prior findings (MAJORs #1–#4, minors #5–#8, nits #9–#12) from the v0.1.22 review, plus second-pass adversarial sweep for any NEW findings.
**Method**: Full re-read of abstract + §V.A LEE + §VI.A Headline + §VI.D within-class + §VII.D DESIVAST + §VII.E T-Web/ASTRA/Tempel + Conclusions. Independent arithmetic recompute of Bonferroni z-thresholds (`scipy.special.erfcinv`), bright-vs-dark joint two-sample z-test from `tracer_stratified_cw_fraction.json` and `filament_within_class_decomposition.json`, row totals (428+6,673+408,187+397,505 vs. 791,635), monopole residuals at maximal-void HEALPix bins.

---

## Verification of prior findings

| # | Class | Issue | v0.1.25 status | Verdict |
|---|---|---|---|---|
| 1 | MAJOR | Bonferroni z-thresholds wrong | K=5 α=0.01 → 3.09 (L386), K=4 α=0.01 → 3.02 (L588, L864), K=4 α=0.05 → 2.50 retained (L570, L862), K=1054 α=0.05 → 4.05 retained (L388); Tempel σ=2.54 reframed (L861–864) as "formally just crossing 2.498 by 0.04σ but well below empirical max-stat null and α=0.01 threshold" | **CLOSED CORRECTLY**. All four thresholds match my independent recompute via `sqrt(2)*erfcinv(α/K)` to 0.01. Tempel verdict-reframe is honest and avoids overclaim. |
| 2 | MAJOR | 791,635 vs 812,793 row-total mismatch | Reconciliation sentence added at §VII.D P4-monopole paragraph (L1161–1166): "the 21,158-row excess over the 791,635-spiral headline subsample is the small population of CW/CCW spirals whose env classification carries through to the V-Web class table despite being excluded from the high-confidence chirality headline sample at the $p_{\rm cls\_eq}^{\max}$ cut" | **PARTIALLY CLOSED** — see new Finding #N1 below. Arithmetic is reconciled, but the verbal explanation is self-contradictory (if excluded from the high-confidence chirality sample, they should not have a CW/CCW label) and not placed in the abstract or §VI.A where the mismatch first surfaces. |
| 3 | MAJOR | "Five independent" overclaim | Abstract L109 changed to "four complementary catalog-anchored cross-checks against the concurrently-released DESIVAST DR1 BGS void catalog (genuinely independent methodologically across the VoidFinder sphere-growing vs. ZOBOV watershed axes; the per-galaxy and HEALPix-stratified tests reuse the same matched-spiral subsample by design)"; n=6 demoted to sub-clause of (i); items renumbered (i)–(iv) | **CLOSED CORRECTLY**. The qualifier is now explicit. However the §VII.D body text at L1138 still reads "This is a **fifth** independent line of evidence" — see new Finding #N2 below. |
| 4 | MAJOR | Missing sign-flip joint z | Abstract L141–146 adds: "The joint two-sample z-test on the bright-vs-dark $f_{\rm CW}$ difference is $|z|\approx 3.4\sigma$ on both the cluster and filament classes…" | **PARTIALLY CLOSED**. The filament-side claim verifies independently: from `filament_within_class_decomposition.json` (bright n=416,701, σ=−2.7993, f=0.49783; dark n=21,203, σ=+2.8500, f=0.50979), my recompute gives Δf=−0.011955, SE=0.003520, **z=−3.396**. Matches paper. **The cluster-side claim is unverifiable from the on-disk artifacts**: there is no `cluster_within_class_decomposition.json` analogue, and `tracer_stratified_cw_fraction.json` reports tracer-program splits on the *entire* matched sample, not on the cluster-class subsample. See new Finding #N3 below. |
| 5 | minor | 1.7 vs 1.98 pp | Abstract L88: "the range across classes is $1.98$ percentage points"; Conclusions L1364: "a range of $1.98$ percentage points" | **CLOSED CORRECTLY**. |
| 6 | minor | Pearson-r LEE / forking paths | §VII.D L1232–1237: "The result is robust to the NSIDE choice and spiral-count threshold: $|r|<0.05$ at NSIDE $\in\{16,32,64\}$ and spiral-count cuts $\in\{100,200,500\}$ (verified by reanalysis on the same artifact set)" | **CLOSED CORRECTLY**. Note the parenthetical "verified by reanalysis on the same artifact set" implies an unsaved numerical check; should ideally be persisted as a JSON sidecar (nit, not blocking — see new Finding #N5). |
| 7 | minor | n=6 overclaim | Abstract L118–120: n=6 demoted to a parenthetical inside (i) "($\sim 130\times$ the V-Web void sample size, supplemented by an $n=6$ per-galaxy classifier-disagreement check showing $0/6$ V-Web 'void' spirals fall inside any of the $101{,}863$ DESIVAST VoidFinder holes at $z\le 0.24$)" | **CLOSED CORRECTLY**. |
| 8 | minor | Missing 0-void-bin monopole residual | §VII.D L1145–1156 adds the residual computation: σ_pred(0-voids)=−3.20, observed −4.75, residual −1.55σ; 6+: σ_pred=−2.64, observed −2.04, residual +0.60σ | **CLOSED CORRECTLY**. My independent recompute confirms σ_pred=2·(−0.0026)·√378,511 = −3.199 and 2·(−0.0026)·√258,060 = −2.642. Matches paper to 0.01. |
| 9 | nit | T-Web directional clarity | §VII.E L890–894: "V-Web's void fraction is *higher* than T-Web's by +8–18 pp… and V-Web's cluster fraction is *lower* than T-Web's knot fraction by 3–5 pp… Both directions match the survey-shell systematic prediction exactly" | **CLOSED CORRECTLY**. |
| 10 | nit | Cluster-Q1/Filament-Q4 overlap | §VI.D L563–567: "cluster Q1 ($\bar\rho=1.55$) is *less dense* than filament Q4 ($\bar\rho=1.86$), so the densest filament galaxies are in fact denser than the least-dense cluster galaxies — the two classes overlap in $\bar\rho$ at the $\lambda_{\rm th}=0$ boundary by construction" | **CLOSED CORRECTLY**. |
| 11 | nit | Tracer-vs-env total reconciliation | Same fix as #2 (the tracer-vs-env arithmetic is the same surface). | Covered by #2; see N1 below. |
| 12 | nit | "133×" stylistic | Abstract L118 "$\sim\!130\times$"; §VII.D L987 "$\boldsymbol{\sim\!130\times}$" | **CLOSED CORRECTLY** at both sites. |

**12-finding closure score: 9 fully closed, 2 partial (#2 / #4 cluster-side), 1 closed-by-reference (#11). No prior verdict has been silently reverted; the structural edits are coherent.**

---

## New findings (second-pass)

### Finding #N1
**Class**: minor
**Section/line**: §VII.D L1160–1166 (P4-monopole-residual paragraph) — and the *absence* of equivalent reconciliation in the abstract / §VI.A.
**Claim flagged**: "the $21{,}158$-row excess over the $791{,}635$-spiral headline subsample is the small population of CW/CCW spirals whose env classification carries through to the V-Web class table despite being **excluded from the high-confidence chirality headline sample at the $p_{\rm cls\_eq}^{\max}$ cut**"
**Issue**: As written this is self-contradictory. The reconciliation says the 21,158 spirals are (a) CW/CCW-labelled AND (b) excluded from the 791,635 high-confidence chirality sample. The 791,635 number is *defined* in the abstract L73–75 as "unambiguous post-TTA equivariant CW or CCW label" spirals — i.e. spirals with a CW/CCW label *are* the 791,635 sample. The 21,158 extras therefore cannot be "CW/CCW spirals excluded by the $p_{\rm cls\_eq}^{\max}$ cut" — if they were excluded by the cut, they would carry an `NS`/low-confidence label, not a CW/CCW one, in which case they are not chirality-relevant and should be excluded from the env-table that reports `n_CW` per class. The numbers themselves are consistent (per-class `n` sums to 812,793 and per-class `n_CW` sums to 404,111 = 49.72% — same f_CW as the 791,635 tracer file reports), which suggests the 21,158 extras come from a *different* selection axis — likely the high-confidence cut on the env *label* (some matched spirals lack a V-Web env label and were excluded from the 791,635 headline but reappear after a relaxed env-label re-classification used by the cosmic-web pipeline). The reconciliation sentence has the right denominator-arithmetic but the wrong causal story.
**Fix**: Reword: "The $21{,}158$-row excess (812,793 − 791,635 = 2.7%) is the population of CW/CCW-labelled spirals whose V-Web env-class assignment passes a relaxed env-label-confidence cut used by the cosmic-web pipeline but is excluded from the 791,635-spiral chirality-relevant headline subsample by a stricter env-class-uncertainty filter. The per-class $f_{\rm CW}$ values on the 812,793 superset match the 791,635-spiral monopole $0.4972$ to 4 decimals (per-class $n_{\rm CW}$ sums: $404{,}111/812{,}793 = 0.49719$), so the headline conclusion is invariant." Also: surface a one-sentence version of this in the abstract or §VI.A, where the table denominator first surfaces, rather than burying it 800 lines later in §VII.D.
**Verifiable**: yes — my recompute confirms 404,111/812,793 = 0.49719 = f_CW from tracer file on 791,635.

---

### Finding #N2
**Class**: minor
**Section/line**: §VII.D L1138 — the maximal-void HEALPix paragraph closes with "This is a **fifth** independent line of evidence that the catalog-level $-5\sigma$ headline tracks survey-mask geometry rather than environment density"
**Claim flagged**: "fifth independent line"
**Issue**: The abstract was correctly retitled "four complementary cross-checks" (Finding #3 closure), but the §VII.D body text at L1138 still self-numbers as "a fifth independent line of evidence". This is a stale cross-reference left over from the v0.1.22 "five independent" framing. It directly contradicts the abstract's "four complementary" qualifier and undermines the closure of Finding #3.
**Fix**: Replace "a fifth independent line of evidence" with "an additional orthogonal sky-position stratification" or "a fourth catalog-anchored cross-check (sky-position stratification)" to align with the abstract's enumeration. While editing, double-check §VII.D paragraph headings (`\paragraph{...}`) for any other (i)-(v) → (i)-(iv) renumbering misses.
**Verifiable**: trivially yes — direct text grep.

---

### Finding #N3
**Class**: minor (borderline MAJOR if the cluster-side numbers cannot be reproduced)
**Section/line**: Abstract L141–146 + §VI.D L600–620 (cluster-class tracer-program stratification paragraph).
**Claim flagged**: "The joint two-sample z-test on the bright-vs-dark $f_{\rm CW}$ difference is $|z|\approx 3.4\sigma$ on **both the cluster and filament classes**"
**Issue**: The filament-side z=−3.40 verifies independently from `filament_within_class_decomposition.json` (bright n=416,701 σ=−2.7993, dark n=21,203 σ=+2.8500 → z=−3.396). **The cluster-side claim is not independently verifiable from any on-disk artifact**: the only tracer-stratified JSON is `tracer_stratified_cw_fraction.json` which reports the tracer split on the *entire* 791,635-spiral matched sample (bright n=775,760, σ=−5.25; dark n=14,782, σ=+1.25), not on the cluster-class subsample (n=397,505). §VI.D quotes the *catalog-level* bright/dark figures but never tabulates the cluster-class restriction. The abstract claim "both the cluster and filament classes" therefore lacks a load-bearing JSON. Either (a) a `cluster_within_class_decomposition.json` exists but was not committed to `pipelines/p5_desi_chirality/results/analysis_cosmic_web/`, or (b) the cluster-side z=3.4σ figure was inferred by symmetry from the filament-side without an explicit per-class recompute on the cluster subsample. A reviewer will ask for the artifact.
**Fix**: Persist a `cluster_within_class_decomposition.json` companion to the existing filament version (cluster-class bright/dark n + f_CW + σ + joint two-sample z), reference it explicitly at §VI.D paragraph "Tracer-program stratification" (L600–620), and either (i) link it from the abstract L141–146 claim or (ii) qualify the abstract claim to read "$|z|\approx 3.4\sigma$ on the filament class with a comparable-magnitude cluster-class sign-flip (see §VI.D)." Without the artifact, the cluster-side z is a load-bearing unverified claim.
**Verifiable**: would require the cluster-stratified JSON, which currently does not exist in the repo.

---

### Finding #N4
**Class**: nit
**Section/line**: §VII.D L1161 P4-monopole residual paragraph header sentence: "$f_{\rm CW}^{\rm P5} = 0.4972$ ($-5.07\sigma$ on $n = 812{,}793$ env-labeled spirals…)"
**Claim flagged**: "$-5.07\sigma$ on $n=812{,}793$"
**Issue**: With f_CW=0.49719 and n=812,793, σ_from_half = (0.49719 − 0.5)/(0.5/√812,793) = −5.07 ✓. But the same paragraph references the 791,635-spiral chirality headline subsample (and the tracer file `overall_sigma_from_half = −5.00` on 791,635). So the paper carries two near-identical headline σ values (−5.00 on 791,635; −5.07 on 812,793) that arise from the same underlying f_CW=0.4972 monopole at slightly different n. This is correct but easy to misread as "the monopole strengthens with more spirals" rather than "we have two denominators floating around." Worth one sentence of clarification.
**Fix**: At L1160–1166, add: "The same monopole $f_{\rm CW}=0.4972$ shows up as $-5.00\sigma$ on the 791,635-spiral headline subsample and $-5.07\sigma$ on the 812,793-spiral env-labeled superset (Table I); the two $\sigma$ values are sample-size-scaled projections of the same underlying offset."
**Verifiable**: trivially yes.

---

### Finding #N5
**Class**: nit
**Section/line**: §VII.D L1232–1237 (Pearson-r robustness clause closing Finding #6 from the v0.1.22 round).
**Claim flagged**: "$|r| < 0.05$ at NSIDE $\in \{16, 32, 64\}$ and spiral-count cuts $\in \{100, 200, 500\}$ (**verified by reanalysis on the same artifact set**)"
**Issue**: The parenthetical implies a 3×3=9-cell robustness grid was actually computed but the JSON is not persisted. A reviewer will ask "where's the grid?" and the answer should be a one-line companion artifact. This is a Houston-Method-v2 violation in a small way: the claim is in the paper but the reproducibility receipt is verbal.
**Fix**: Persist a one-page `voids_vs_chirality_robustness_grid.json` with the 9 (NSIDE, cut)-cell Pearson r values + n_pix_both per cell + p-value per cell, and add an `\artifact{}` reference at L1237. 5 minutes of compute on the existing per-pixel f_CW + maximal-void-count CSVs.
**Verifiable**: yes — derivable from existing per-pixel artifacts.

---

### Finding #N6
**Class**: nit
**Section/line**: §VI.A L451 — there is a missing paragraph break: "\end{figure} The negative $\sigma$ values in filament and cluster…" runs the figure environment directly into body text on the same line.
**Claim flagged**: text run-on across the figure float.
**Issue**: Cosmetic LaTeX hygiene. The body sentence that begins "The negative $\sigma$ values…" should start on its own line after `\end{figure}` to avoid a hanging space and to render correctly with `\indent` in the next paragraph. Most renderers handle this gracefully (revtex4-2 is tolerant) but it is below the project's PDF-formatting bar.
**Fix**: Insert a blank line between `\end{figure}` and "The negative".
**Verifiable**: yes — trivial.

---

## Summary

| Class | Prior round closures | New findings |
|---|---|---|
| BLOCKER | 0 | 0 |
| MAJOR | 4 prior; 2 closed fully (#1, #3 modulo N2), 2 partial (#2, #4) | 0 |
| minor | 4 prior; all closed | 3 (#N1 missing-clarity in row-total reconciliation; #N2 stale "fifth independent"; #N3 unverifiable cluster-side z=3.4σ artifact) |
| nit | 4 prior; all closed | 3 (#N4 dual-denominator clarification; #N5 missing robustness-grid JSON; #N6 figure float run-on) |

**Total new findings: 6** (0 BLOCKER, 0 MAJOR, 3 minor, 3 nit).

**Single most important new finding**: **#N3** — the abstract's load-bearing "$|z|\approx 3.4\sigma$ on both the cluster and filament classes" claim is independently verifiable only on the filament side from `filament_within_class_decomposition.json`; no equivalent cluster-class artifact is committed. Either persist a `cluster_within_class_decomposition.json` or qualify the abstract to attribute the joint significance to the filament class only with a "comparable-magnitude cluster-class sign-flip" sub-clause.

**Overall verdict**: The v0.1.22 → v0.1.25 edits are tight, arithmetic-clean, and close the headline review concerns. The remaining issues are second-order: a stale "fifth independent" cross-reference (N2), a self-contradictory but numerically-correct row-total reconciliation sentence (N1), and a missing companion JSON for the cluster-side joint z-test (N3). None of the new findings flip any conclusion or invalidate any artifact; all three minors are 5–15 minute editing fixes plus one 5-minute artifact persist. **Per AGENT_RULES §4.4.1 cascaded-loop-exit criterion (≤1–2 polish MAJORs acceptable for the first R-round), the paper is R-round-clean at this resolution.** Recommend: close N1 and N2 in a single edit pass; persist the N3 cluster-class artifact (or qualify the abstract); N4–N6 can ride the next compile.
