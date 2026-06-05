# P5 R10v3 — v3 native-PDF cross-vendor SYNTHESIS

**Reviewers**: Claude_brutal, Gemini_cosmology, Grok_brutal, OpenAI_methodology, Perplexity_citations
**Total findings (across all reviewers)**: 35
**Distinct consensus groups**: 5

## Per-reviewer finding counts

| Reviewer | ESSENTIAL | MAJOR | MINOR | NIT |
|----------|-----------|-------|-------|-----|
| Claude_brutal | 0 | 0 | 0 | 0 |
| Gemini_cosmology | 0 | 0 | 0 | 0 |
| Grok_brutal | 0 | 0 | 0 | 0 |
| OpenAI_methodology | 6 | 5 | 12 | 0 |
| Perplexity_citations | 0 | 0 | 0 | 0 |

---

## Consensus-grouped findings (most reviewers first)

### `table_ii` — ESSENTIAL — **CONSENSUS** (2 reviewers)

Reviewers: Grok_brutal, OpenAI_methodology

- **[Grok_brutal/P5-E4/UNKNOWN]**: **P5-E4** (Table II + Fig. 2, p. 5)   The void bin (\(n=428\)) yields \(\sigma = -0.68\) and is stated to be “statistical noise.” The paper nevertheless headlines the four-class range (1.98 pp) as the primary result. The void bin is counting-statistics limited and survey-edge contaminated; its inclusion in the headline range is not justified and inflates the apparent dynamic range.
- **[Grok_brutal/P5-E6/UNKNOWN]**: **P5-E6** (Section VI.A and Table II, p. 5)   The primary headline result rests on a single V-Web run (\(R_s=25\,{\rm Mpc}/h\), \(\lambda_{\rm th}=0\)). All other runs are labeled “secondary.” No pre-registered analysis plan is referenced, and the choice of the canonical cell is justified only post hoc by sample size. This constitutes an undeclared forking-path problem.
- **[OpenAI_methodology/P5-E1/ESSENTIAL]**: P5-E1 Sec. VI A, p. 5, Table II  vs. Sec. VII, p. 10, Table VI   • Problem Canonical class-range is quoted two different ways:     – Table II and text give range = 0.0198 (→ 1.98 percentage points).     – Table VI line (Rs=25, λth=0) gives 0.165 “percentage points”.     Both cannot be true; 0.165 pp would correspond to Δf≈0.00165, an order of magnitude smaller than the earlier 0.0198.   • Fix Re-compute and make the canonical range consistent everywhere; update all downstream statements that use the 0.165/0.22 numbers (sec. VII discussion and Fig. 5).

### `sigma_mixing` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P5-E6/ESSENTIAL]**: P5-E6 Throughout (e.g. Abstract, Sec. VI D)   • Problem σ values from different null procedures (binomial Z, permutation max-stat, Bonferroni thresholds) are juxtaposed without the explicit “not directly comparable” reminder required by the policy (see reviewer instruction #7).   • Fix Every place where a binomial Z is written next to a permutation p-value or Bonferroni threshold must add a clause making the distinction explicit.  ------------------------------------------------------------------------

### `duplicate_phrase` — MINOR — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P5-m6/MINOR]**: P5-m6 Duplicate phrase p. 11 line 1: “per-galaxy cross-match of the V-Web void-class matched-spiral subsample”.

### `companion,future_date` — UNKNOWN — _single-reviewer_ (1 reviewer)

Reviewers: Grok_brutal

- **[Grok_brutal/P5-N3/UNKNOWN]**: **P5-N3** (References)   Paper IV is cited as “not yet peer-reviewed.” A submitted manuscript cannot rest its central systematic correction on an unpublished companion; the dependence must be made explicit or the reference updated.  ## Summary recommendation **REJECT**  The manuscript presents a null result whose central claim (no detectable environment dependence at the \(\sim25\,{\rm Mpc}/h\) scale) is already bounded by the monopole reported in the still-unpublished Paper IV. The present work adds only a large number of secondary cross-checks whose statistical power is limited by the tiny V…

## Other findings (29)

- **[Grok_brutal/P5-E1/UNKNOWN]**: **P5-E1** (Title page, p. 1)   Offending text: “(Dated: June 4, 2026)”.   Required fix: Remove or correct the future placeholder date. This is an internal drafting artifact that must not appear in a submitted manuscript.
- **[Grok_brutal/P5-E2/UNKNOWN]**: **P5-E2** (Abstract/summary paragraph, p. 1)   The opening block functions as the abstract yet contains no explicit statement of the primary null result or its statistical significance after all corrections. The abstract must be rewritten to state the headline quantitative claim (range of \(f_{CW}\) across four V-Web classes = 1.98 pp after monopole subtraction) and the final post-correction signi…
- **[Grok_brutal/P5-E3/UNKNOWN]**: **P5-E3** (Section V, p. 4 and throughout)   Multiple distinct null procedures (label-shuffle, position-shuffle, look-elsewhere empirical max-stat, Bonferroni) are reported side-by-side (e.g., \(\sigma = -2.61\), \(-4.66\), \(-0.68\)) without the mandatory qualifier “not directly comparable” at every juxtaposition. This is an ESSENTIAL violation of statistical reporting standards.
- **[Grok_brutal/P5-E5/UNKNOWN]**: **P5-E5** (Section VIII, p. 10)   The DESIVAST re-projection sample (\(n_{\rm void}=56{,}981\)) is advertised as “\(\sim130\times\) larger” than the V-Web void sample. The two samples are defined by entirely different algorithms; the factor-of-130 comparison is therefore meaningless and misleading.
- **[Grok_brutal/P5-M1/UNKNOWN]**: **P5-M1** (Length)   The manuscript is 20 pages for a pure null result whose quantitative content is a set of upper bounds already bounded by Paper IV’s monopole. Recommended maximum length after cuts: 8 pages (Letter) or 10 pages (Regular Article). All secondary cross-checks (Sections IX–X) should be moved to a data-release note or appendix.
- **[Grok_brutal/P5-M2/UNKNOWN]**: **P5-M2** (Fig. 3, p. 6)   The right-hand panel plots observed \(\sigma\) against the Paper IV monopole prediction. The caption claims “no quintile deviates … by more than \(\sim2\sigma\)”; the plotted residuals reach \(1.87\sigma\) (Q3). The caption is factually incorrect.
- **[Grok_brutal/P5-M3/UNKNOWN]**: **P5-M3** (Section IX.B, p. 14)   The T-Web comparison is performed on an EDR overlap of only 25 186 spirals. The paper claims “the two classifiers reach the same conclusion” while simultaneously reporting that per-galaxy environment labels disagree strongly. The statistical power of this test is insufficient to support the claim.
- **[Grok_brutal/P5-N1/UNKNOWN]**: **P5-N1** (Multiple tables)   Table captions repeatedly use “\(\sigma_{\rm from half}\)” without defining the exact half-sample split or confirming it is the same split used in Paper IV. Minor but must be standardized.
- **[Grok_brutal/P5-N2/UNKNOWN]**: **P5-N2** (Fig. 1, p. 4)   Pie-chart volume fractions are given to 0.1 % precision while the underlying grid is only \(256^3\) and the cluster fraction is 1.0 %. The displayed precision exceeds the counting uncertainty.
- **[OpenAI_methodology/P5-E2/ESSENTIAL]**: P5-E2 Sec. VII, p. 10, statement “per-cell range … never exceeds 0.22 percentage points (max 0.0022 at Rs=25, λth=0.3)”   • Problem 0.22 percentage points is 0.0022 in f.  The text writes both 0.22 and 0.0022 in the same sentence as if identical.   • Fix Adopt one consistent unit (either f-units or pp) and propagate through the manuscript.
- **[OpenAI_methodology/P5-E3/ESSENTIAL]**: P5-E3 Sec. VIII F, p. 13, Table X and surrounding text   • Problem The “monopole” baseline f_P5_CW is estimated from the *same* 812 793 galaxies that are then tested class-by-class.  This induces a correlation:       Var(f_class – f_total) = Var(f_class) + Var(f_total) – 2 Cov(…)     The reported σ_vs monopole treats f_total as error-free, thereby under-estimating σ by ≈√(1 – n_class/N_tot).   • F…
- **[OpenAI_methodology/P5-E4/ESSENTIAL]**: P5-E4 Sec. V, Eq. (1) and repeated use throughout   • Problem The Paper IV monopole offset Δf_CW = –0.0026 itself has a quoted uncertainty (0.000279 in Paper IV).  Nowhere is this propagated when predicted σ_pred values are compared to observed σ.   • Fix Add the 6 % fractional uncertainty of Δf to the σ_pred error budget (or quote 1σ bands) every time σ_obs–σ_pred is used as a significance diagno…
- **[OpenAI_methodology/P5-E5/ESSENTIAL]**: P5-E5 Sec. XI, p. 18 (RSD caveat)   • Problem The V-Web field is built in redshift space but the paper ultimately claims a 0.1 %–level null.  The text gives only an order-of-magnitude argument (σ_v/aH ≲5 Mpc h⁻¹) without any quantitative propagation into Δf_CW.   • Fix Either (a) rerun the V-Web classification on a Kaiser/FOG-corrected reconstruction, or (b) provide a numerical Monte-Carlo showing…
- **[OpenAI_methodology/P5-M1/MAJOR]**: P5-M1 Sec. VII, Fig. 5 heat-map and Table VI (Phase-2 sweep)   The grid cell size is 25.9 h⁻¹ Mpc, identical to the Gaussian Rs=25 h⁻¹ Mpc smoothing.  With this choice the effective resolution is one grid cell, so changing Rs from 10→50 is largely cosmetic.  This undercuts the stated “hyper-parameter robustness”.  A higher-resolution grid (≥512³) or at least a test on 384³ should be shown.
- **[OpenAI_methodology/P5-M2/MAJOR]**: P5-M2 Sec. VI A, void class n=428 – counting noise   0.7 σ is called “uninformative”, yet later (Sec. VII) the same bin is included in the per-cell range statistic.  Either drop the void bin from the range calculation or quote range both with and without it.
- **[OpenAI_methodology/P5-M3/MAJOR]**: P5-M3 Sec. IX A, Tempel cross-validation   The mapping “Tempel multiplicity ≥20 ↔ V-Web cluster” is not justified; multiplicity is not a proxy for tidal eigen-value collapse in a thin shell survey.  At minimum, show the purity/completeness of this mapping on a simulation or drop the quantitative concordance claim (0.026 pp).
- **[OpenAI_methodology/P5-M4/MAJOR]**: P5-M4 Permutation tests use N_MC = 1000 (Sec. V, p. 4)   This sets a floor p_min ≈ 0.001.  Several p-values are quoted to 3 significant figures below 0.05 (e.g. p=0.135, 0.372).  With only 1000 draws, the third decimal is meaningless.  Quote two significant figures and add the ±0.001 Monte-Carlo uncertainty.
- **[OpenAI_methodology/P5-M5/MAJOR]**: P5-M5 Sec. VIII D, “catalog-native V2” sample sizes   n_void = 86 276, yet σ_void is reported as –0.24.  Re-computing with the given counts (CW not given) I cannot reproduce –0.24.  Provide the raw n_CW, n_total used.  ------------------------------------------------------------------------
- **[OpenAI_methodology/P5-m1/MINOR]**: P5-m1 Equation (2), p. 4 – The erfc⁻¹ form implicitly assumes two-sided test; state this explicitly.
- **[OpenAI_methodology/P5-m2/MINOR]**: P5-m2 Table I (p. 3) lists “Leg DES 4,724”; footnote later says DES covers 5 deg² – supply reference or cut.
- **[OpenAI_methodology/P5-m3/MINOR]**: P5-m3 Page 9, Fig. 4 colour-bar units missing (“σ_from_half”).
- **[OpenAI_methodology/P5-m4/MINOR]**: P5-m4 Multiple places: “σ= −4.75” but Fig. 6 lower panel y-range only to ±4.5 – the pixel at –4.75 is clipped.
- **[OpenAI_methodology/P5-m5/MINOR]**: P5-m5 Page 12: “Δf_CW = 0.0007, statistically indistinguishable” – give the 1σ binomial error (~0.004).
- **[OpenAI_methodology/P5-m7/MINOR]**: P5-m7 Section headings use Roman numerals but Appendix uses A/B; uniformise.
- **[OpenAI_methodology/P5-m8/MINOR]**: P5-m8 Reference [11] “in submission to MNRAS” – give arXiv number only.  ------------------------------------------------------------------------ NITS ------------------------------------------------------------------------
- **[OpenAI_methodology/P5-n1/MINOR]**: P5-n1 Abstract: “∼130× larger” → give numbers once (56 981 vs 428).
- **[OpenAI_methodology/P5-n2/MINOR]**: P5-n2 Fig. 3 right panel: diamond markers not described in caption.
- **[OpenAI_methodology/P5-n3/MINOR]**: P5-n3 Typo p. 6: “decom￾positions” (split word).
- **[OpenAI_methodology/P5-n4/MINOR]**: P5-n4 p. 18 “Rubin-scale chirality classifier … would resolve sub-pixel …” – speculative; move to Outlook.  ------------------------------------------------------------------------ ## Summary recommendation
