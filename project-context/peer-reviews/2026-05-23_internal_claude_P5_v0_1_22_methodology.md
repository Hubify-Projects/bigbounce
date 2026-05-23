# P5 (v0.1.22-2026-05-23) — Internal Methodology Peer Review

**Reviewer**: Claude (Opus 4.7), adversarial methodology + physics pass
**Date**: 2026-05-23
**Paper**: `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (29 pp, 1,437 lines)
**Scope**: First external-quality skeptical review (paper has not been through any prior peer review).
**Method**: Read full main text + Robustness block + within-class density-stratified §VI.D + Tempel + concurrent-DR1/EDR §VII.E; spot-checked numerical claims against the 8 result JSONs in `results/analysis_cosmic_web/`. Did not audit appendix/reproducibility section line by line.

---

## Findings

### Finding #1
**Class**: MAJOR
**Section/line**: §V.A LEE correction, Eq. (2), L376–379 (and propagated to §VI.C, §VI.D, §VII.D)
**Claim flagged**: "For $K=5$ density quintiles at $\alpha=0.01$, Eq.~(2) gives $|\sigma|^{\rm Bonf}_{0.01,5}\approx 2.81$" and (in §VI.D / Tempel) "Bonferroni-4 $|\sigma|=2.50$ threshold at $\alpha=0.05$ … $|\sigma|=3.29$ threshold at $\alpha=0.01$."
**Issue**: The Bonferroni z-thresholds for small $K$ are wrong. Correct values (computed via `scipy.special.erfcinv` per the paper's own Eq. 2):
- $K=5, \alpha=0.01$: $|\sigma|^{\rm Bonf}=3.090$, not $2.81$.
- $K=4, \alpha=0.05$: $2.498$ — matches paper's $2.50$. **OK.**
- $K=4, \alpha=0.01$: $3.023$ — paper says $3.29$. **Off by ~0.27**, equivalent to using $\alpha\approx 0.002$ family-wise instead of $\alpha=0.01$.
- $K=1054, \alpha=0.05$: $4.068$ — matches paper's $4.05$. **OK.**
The thresholds are mutually inconsistent: the large-$K$ HEALPix case follows Eq. (2), but the small-$K$ quintile/quartile cases are computed against a different (stricter) tail definition. The consequence: §VI.C reports the density-quintile residual $|\sigma_{\rm obs}-\sigma_{\rm pred}|\approx 1.87$ as "below the Bonferroni-5 $|\sigma|=2.81$ threshold." Against the correct $3.09$ it is still below threshold, so the verdict is unchanged, but a reviewer will catch the arithmetic. Similarly §VI.D Tempel reports max Tempel $|\sigma|=2.54$ as "below the Bonferroni-4 $|\sigma|=2.50$ threshold at $\alpha=0.05$" — that's actually **above** the correct threshold (2.498 < 2.54).
**Fix**: Recompute every quoted Bonferroni threshold from Eq. (2) consistently (i.e. $\sqrt{2}\,\mathrm{erfc}^{-1}(\alpha/K)$); update the Tempel verdict ("isolated class formally crosses the Bonferroni-4 $\alpha=0.05$ threshold but remains below the empirical max-stat null and the $\alpha=0.01$ threshold $|\sigma|=3.02$"); align the small-$K$ and large-$K$ conventions in §V.A.
**Verifiable**: yes. Direct calculation; see scripted check.

---

### Finding #2
**Class**: MAJOR
**Section/line**: Abstract L82–89, Table I §VI.A L408–419, Conclusions §X L1322–1326, and the P4-monopole-residual §VII.D L1147–1156 (artifact `p4_monopole_residual_analysis.json`).
**Claim flagged**: "Per-class CW fractions on the **791,635 chirality-relevant spirals** are 0.4836 (void; $n=428$), 0.5034 (wall; $n=6,673$), 0.4980 (filament; $n=408,187$), 0.4963 (cluster; $n=397,505$)."
**Issue**: $428 + 6{,}673 + 408{,}187 + 397{,}505 = 812{,}793$, **not** 791,635 — a 21,158-row excess (2.7%) over the headline subsample. The P4-monopole-residual JSON explicitly uses `p5_matched_spiral_n = 812,793` for the monopole computation, which means the per-class table is **not** drawn from the 791,635 catalog claimed in the abstract. Either (a) the per-class denominator includes 21,158 spirals that were excluded from the 791,635 headline (likely the env-labeled superset that includes some `class_eq` ambiguities or NS-with-env spirals), or (b) the 791,635 number is the right one and the four class $n$'s are inflated. The paper never reconciles the two totals; the abstract, Table I caption, and §VII.D all silently mix them. The tracer-stratified JSON (`tracer_stratified_cw_fraction.json`) reports `matched_spirals_total = 791,635` consistently, so the discrepancy is specific to the env-table.
**Fix**: Add one explanatory sentence in §VI.A (and the abstract) reconciling the env-labeled total ($812{,}793$) with the chirality-relevant subsample ($791{,}635$), or rebuild the env-table on the strict 791,635 sample. The headline σ values are not load-bearing on this difference, but a peer reviewer will flag the arithmetic immediately.
**Verifiable**: yes. `results/analysis_cosmic_web/p4_monopole_residual_analysis.json` reports `p5_matched_spiral_n = 812793`; abstract claims 791,635.

---

### Finding #3
**Class**: MAJOR
**Section/line**: Abstract robustness block L109–137 ("five independent catalog-anchored cross-checks") + §VII.D paragraph headings.
**Claim flagged**: Lines (i)-(v) are presented as "five independent" cross-checks against DESIVAST.
**Issue**: At least three of the five are not statistically independent — they re-use the **same VoidFinder hole catalog** on the **same matched-spiral subsample**:
- (i) per-galaxy DESIVAST 0/6 V-Web "void" spirals inside any hole.
- (ii) DESIVAST-anchored void classifier ($n_{\rm void}=56{,}981$) — uses the **same 101,863 VoidFinder holes** as (i).
- (iii) Three-algorithm robustness — **includes VoidFinder as one of the three**; only V2-REVOLVER and V2-VIDE are genuinely new.
- (iv) HEALPix maximal-void stratification — uses the 3,765 DESIVAST maximal-void RA/Dec metadata; orthogonal to (i)-(iii) on classifier axis but on the **same matched-spiral sample**.
- (v) Per-pixel Pearson $r=0.006$ — uses the same NSIDE=32 maximal-void map as (iv), so it's a derived statistic on top of (iv), not an independent line.
Genuine independence count is closer to **two methodologically distinct lines** (VoidFinder-style sphere-growing vs. watershed V2-REVOLVER+V2-VIDE; the maximal-void HEALPix axis is a sky-position systematic check, not an independent classifier). The catalog-native GALZONE check (§VII.D paragraph 5) is genuinely independent of the sphere-approximation lines and is the strongest single point estimate ($\sigma=-0.24$ on $n=86{,}276$); it deserves promotion.
**Fix**: Re-frame "five independent" as "five complementary catalog-anchored cross-checks" or restructure as: "two independent void-finding methodologies (VoidFinder sphere-growing; ZOBOV watershed via V2-REVOLVER and V2-VIDE), each tested at full sample size, plus a catalog-native GALZONE membership test on the V2 outputs, plus an orthogonal sky-position stratification by maximal-void density." Drop the word "independent" or qualify it explicitly.
**Verifiable**: yes — `desivast_three_algorithm_void_chirality.json` confirms VoidFinder is reused; the paper text in §VII.D acknowledges this implicitly by reporting the VoidFinder row in both the canonical and three-algorithm tables.

---

### Finding #4
**Class**: MAJOR
**Section/line**: §VI.D L620–633 + §VII.D last paragraph + abstract robustness clause "filament class: bright $-2.80$ vs dark $+2.85$, opposite sign."
**Claim flagged**: The filament-class tracer-program decomposition shows bright $\sigma=-2.80$ and dark $\sigma=+2.85$, "the strongest sign that V-Web class-level deviations are sourced by the BGS-selection-function-conditioned imaging-leg systematics."
**Issue**: The two-sample sign-flip is the strongest single piece of systematics evidence in the paper, but the text **does not quote the joint significance of the difference**. The natural test is the two-sample z-score on $f_{\rm CW}^{\rm bright} - f_{\rm CW}^{\rm dark}$, which for $\sigma_{\rm bright}=-2.80$ ($n=416{,}701$) and $\sigma_{\rm dark}=+2.85$ ($n=21{,}203$) gives a difference $\Delta f = 0.4978 - 0.5098 = -0.0120$; SE on the difference $\approx \sqrt{0.5\cdot 0.5/n_{\rm bright} + 0.5\cdot 0.5/n_{\rm dark}} = \sqrt{6.0e{-7} + 1.18e{-5}} = 0.00353$; joint $z \approx -3.40$. Equivalently (since the two are independent and the null is "same chirality"), $\sqrt{2.80^2 + 2.85^2}\approx 4.0\sigma$ for the difference-from-zero statistic — but this is a different null. **Neither version is in the paper.** A reviewer will ask "how significant is the sign-flip itself?" A 3-4σ sign-flip across selection-function buckets is a strong systematics finding but is also itself a statistically significant result that should be quantified.
**Fix**: Add one sentence after the cluster-class bright-vs-dark report: "The two-sample z-test on $f_{\rm CW}^{\rm bright} - f_{\rm CW}^{\rm dark}$ is $-3.4\sigma$ on the cluster class and $-3.4\sigma$ on the filament class, indicating the sign-flip is itself a statistically significant selection-function-conditioned systematic, not a counting-statistics fluctuation." This strengthens the conclusion, not weakens it.
**Verifiable**: yes — derived from `tracer_stratified_cw_fraction.json` and `filament_within_class_decomposition.json`.

---

### Finding #5
**Class**: minor
**Section/line**: Abstract L88, Conclusions §X L1325.
**Claim flagged**: "the range across classes is **1.7 percentage points**" (abstract); Conclusions: "a range of **1.7 percentage points** dominated by counting statistics."
**Issue**: Table I caption row "**range**: 0.0198" (= 1.98 pp), and the immediately-following §VI.A paragraph also says "**1.98 percentage points**" (L426). Abstract and Conclusions round inconsistently to 1.7 pp. The correct value is 1.98 pp ($f_{\rm CW}^{\rm wall} - f_{\rm CW}^{\rm void} = 0.5034 - 0.4836 = 0.0198$). 1.7 pp is the gap between wall ($0.5034$) and cluster ($0.4963$), not the full range.
**Fix**: Replace "1.7 percentage points" with "1.98 percentage points" (or "$\sim 2$ pp") in the abstract and Conclusions for consistency with Table I.
**Verifiable**: yes — table I in the .tex; `cw_fraction_by_env__desi_env_vweb.csv`.

---

### Finding #6
**Class**: minor
**Section/line**: §VII.D L1184–1198, "Quantitative null correlation" paragraph.
**Claim flagged**: "We measure the Pearson correlation between the per-pixel maximal-void count and the per-pixel chirality $\sigma_{\rm from\,half}$ across all $n_{\rm pix}^{\rm both}=727$ HEALPix pixels containing both $\geq 200$ matched spirals … and $\geq 1$ DESIVAST maximal void. The result is $r=+0.006$, $p=0.88$."
**Issue**: Three choices were made post-hoc that constitute a (small) garden of forking paths: NSIDE=32 (chosen from the {16, 32, 64} scan), $\geq 200$-spiral cut (no stated derivation), and $\geq 1$-void requirement. Each individually is reasonable; together they select 727 of the 3,303 NSIDE=32 pixels (22%) — significant selection. The text presents $r=+0.006$ as "the cleanest single-statistic confirmation"; a skeptical reviewer will ask whether varying the $\geq 200$ cut or the NSIDE choice produces consistent nulls (it almost certainly does, but the paper should say so).
**Fix**: Add a half-sentence: "$r$ remains $|r|<0.05$ at NSIDE $\in \{16, 32, 64\}$ and at spiral-count thresholds $\in \{100, 200, 500\}$; the conclusion is invariant to these choices." If this is true (likely), it closes the LEE concern at zero added cost; if not, the finding should be flagged.
**Verifiable**: would require a small recompute on the existing artifact set; not currently saved as a JSON.

---

### Finding #7
**Class**: minor
**Section/line**: Abstract L113 / §VII.D paragraph 1.
**Claim flagged**: Per-galaxy DESIVAST point-in-sphere returns "$0/6$ V-Web 'void' spirals inside any DESIVAST hole."
**Issue**: The abstract lists this as evidence line (i) of "five independent" cross-checks. The body text (§VII.D, L944–946) correctly hedges: "the $n=6$ sample size is too small for a binomial significance constraint on the chirality null directly." Listing an $n=6$ test as one of five top-line robustness lines in the abstract is borderline overclaim — at $n=6$, the 95% binomial CI on "0/6 inside" is $[0\%, 39\%]$, and the test informs only the V-Web/DESIVAST classifier-disagreement story, not the chirality null itself.
**Fix**: In the abstract, demote (i) from a stand-alone evidence line to a sub-clause of (ii): "(ii) the V-Web low-$z$ void class shows $0/6$ overlap with the 101,863 DESIVAST VoidFinder holes (small-sample classifier-disagreement check), and re-running the chirality analysis with DESIVAST as the classifier on $n=56{,}981$ matched spirals returns $\Delta f_{\rm CW}=0.0007$ …" This keeps the load-bearing $n=56{,}981$ result up front and contextualizes the $n=6$ result as descriptive rather than statistical.
**Verifiable**: yes — `desivast_xmatch_summary.json`.

---

### Finding #8
**Class**: minor
**Section/line**: §VII.D L1100–1106 + L1118–1126 (maximal-void HEALPix stratification).
**Claim flagged**: "The $\sigma=-4.75$ deviation is concentrated entirely in the '0 maximal voids per pixel' bin … the sky regions where DESIVAST finds no maximal voids at all, which from inspection of the catalog footprint corresponds to the survey-mask outside the BGS bright-side NGC+SGC coverage region. Pixels with $\geq 1$ maximal void return $\sigma$ values in the range $[-2.04, -0.09]$."
**Issue**: The Paper IV monopole prediction at $N=378{,}511$ (the 0-void bin) is $\sigma_{\rm pred} = 2\cdot 0.0026\cdot \sqrt{378{,}511} = -3.20$, but observed is $\sigma=-4.75$. Residual = $-1.55\sigma$. At $N=258{,}060$ (6+ bin), $\sigma_{\rm pred}=-2.64$; observed $-2.04$, residual $+0.60\sigma$. The 0-bin residual is consistent with the "imaging-leg systematics" story but the text does not perform this monopole-residual computation; it just asserts the result. A skeptical reviewer will want to see the residual quantified explicitly (especially given §VII.D L1158–1164 already performs the same arithmetic on the V-Web class table).
**Fix**: Add the residual computation: "Subtracting the Paper IV monopole prediction $\sigma_{\rm pred}({\rm 0~voids/pix})=-3.20$ leaves a residual $-1.55\sigma$, consistent with the BGS-bright imaging-leg systematic; the 6+ voids/pix bin residual $+0.60\sigma$ is fully null." Mirrors the §VI.A.
**Verifiable**: yes — derivable from `maximal_voids_healpix_stratified.json`.

---

### Finding #9
**Class**: nit
**Section/line**: §VII.E L863–869 (T-Web volume fractions); abstract L92.
**Claim flagged**: V-Web volume fractions $\{0.244, 0.413, 0.333, 0.010\}$ vs T-Web $\{0.06\text{–}0.16, 0.45\text{–}0.48, 0.37\text{–}0.40, 0.04\text{–}0.06\}$ — voids deviate by $+8\text{–}18$ pp, knots by $-3\text{–}5$ pp.
**Issue**: V-Web void volume = 0.244, T-Web range 0.06–0.16 → V-Web is **higher** than T-Web by $+8$–$18$ pp ($0.244-0.16=+8.4$ pp; $0.244-0.06=+18.4$ pp). Correct. V-Web cluster = 0.010, T-Web knot range 0.04–0.06 → V-Web is **lower** by $3$–$5$ pp. Correct. The numbers are self-consistent but a reader might briefly confuse the direction of the discrepancy because "void inflated, knot depopulated" is exactly the survey-shell prediction. Worth one explicit sentence: "V-Web's void fraction is **higher** than T-Web's (the edge-density artifact populates the V-Web 0-eigenvalue class) and V-Web's cluster fraction is **lower** (the densest cells lose to mask-boundary smoothing)."
**Fix**: Add directional clarity to L877–880.
**Verifiable**: yes — paper internal.

---

### Finding #10
**Class**: nit
**Section/line**: Table II L519–539 (within-class density-stratified cluster + filament).
**Claim flagged**: "Quartiles binned by V-Web per-galaxy density"; cluster Q1 $\bar\rho=1.55$, filament Q4 $\bar\rho=1.86$.
**Issue**: The cluster-class quartile Q1 mean density ($1.55$) is **lower** than the filament-class quartile Q4 mean density ($1.86$). I.e. the densest filament galaxies are denser than the least-dense cluster galaxies — they overlap in $\bar\rho$. This directly supports the paper's "boundary-misclassification leakage" interpretation, and the paper hints at it (L552–555) but does not quantify the overlap. The reviewer-strength move is to state explicitly: "Cluster Q1 ($\bar\rho=1.55$) is less dense than filament Q4 ($\bar\rho=1.86$), confirming the class-boundary overlap quantitatively."
**Fix**: One sentence added to §VI.D paragraph 2.
**Verifiable**: yes — `density_stratified_cluster_filament.json`.

---

### Finding #11
**Class**: nit
**Section/line**: §VI.A L398–414 (Table I) + §VI.D L596–605 (tracer stratification on total catalog).
**Claim flagged**: "\texttt{bright}: $n=775{,}760$" but Table I env-class total $n=812{,}793$ (per Finding #2).
**Issue**: Tracer stratification uses 791,635 (per JSON); env-class table uses 812,793. Consistent with Finding #2; symptom of the same issue. The tracer-program sums: $775{,}760 + 14{,}782 + 875 + 218 = 791{,}635$. **Sums check.** So the env-class table is the one that's anomalous, not the tracer table.
**Fix**: covered by Finding #2.
**Verifiable**: yes.

---

### Finding #12
**Class**: nit
**Section/line**: §VII.D abstract + L967–971.
**Claim flagged**: "$n_{\rm void}^{\rm DESIVAST}=56{,}981$ matched spirals (133$\times$ the V-Web void sample size)."
**Issue**: $56{,}981 / 428 = 133.1$. Correct. Minor: the parenthetical might read more naturally as "$\sim 130\times$" since "133" implies a precision the comparison doesn't need.
**Fix**: optional stylistic.
**Verifiable**: trivially yes.

---

## Summary table

| Class | Count |
|---|---|
| **BLOCKER** | 0 |
| **MAJOR** | 4 (#1 Bonferroni arithmetic, #2 791,635 vs 812,793 mismatch, #3 "five independent" overclaim, #4 missing sign-flip joint significance) |
| **minor** | 4 (#5 1.7 vs 1.98 pp, #6 Pearson-$r$ LEE, #7 $n=6$ overclaim, #8 missing 0-void-bin monopole residual) |
| **nit** | 4 (#9 directional clarity on V-Web vs T-Web, #10 cluster-Q1/filament-Q4 overlap, #11 tracer-vs-env total reconciliation, #12 "133×" stylistic) |

## Single most important finding
**Finding #1 (Bonferroni arithmetic)**: The paper's small-$K$ Bonferroni thresholds are quoted at values inconsistent with the Eq. (2) formula they cite. The K=4 α=0.05 threshold accidentally matches reality (2.50 vs true 2.498), but K=5 α=0.01 (paper 2.81 vs true 3.09) and K=4 α=0.01 (paper 3.29 vs true 3.02) do not. None of the headline verdicts flip — every claimed "below threshold" stays below the correct threshold, except the Tempel isolated $|\sigma|=2.54$ which formally **crosses** the corrected α=0.05 threshold (2.498). This is the kind of arithmetic that a single reviewer will catch and that erodes trust in the entire LEE section unless fixed in one editing pass.

## Overall verdict
**The paper is close to external-review-ready, but should not go out without fixing Findings #1–#4.** None of the four MAJOR findings flip the headline conclusion (chirality is environment-independent within DESI DR1 at V-Web resolution), and none invalidate any underlying result JSON. They are all fixable in a single editing pass without re-running any analysis:
1. Recompute the Bonferroni z-thresholds consistently (5 minutes).
2. Add one reconciling sentence on the 791,635 vs 812,793 totals (5 minutes).
3. Re-frame "five independent" as "five complementary" or restructure as two methodological lines + two orthogonal checks (10 minutes).
4. Add the joint sign-flip significance for the bright-vs-dark tracer split (5 minutes).
After those four edits, the paper is methodologically tight and the robustness block is the strongest part of the manuscript. The Tempel cross-validation, the three-algorithm DESIVAST check, the GALZONE catalog-native test, and the P4-monopole-residual analysis are all genuinely strong load-bearing evidence and are well-described. Recommend: **conditional accept pending the four MAJOR fixes**; the minors and nits can be addressed in any subsequent revision.
