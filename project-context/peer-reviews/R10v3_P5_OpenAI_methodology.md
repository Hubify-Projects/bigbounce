# P5 R10v3 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `o3-2025-04-16`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high
**Wall time**: 51.1s

---

Referee report on ‘Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test …’ (P5, 20 pp)

I have audited every numerical claim, the statistical procedures, and the internal arithmetic.  Below I list all issues that must be corrected before the manuscript can be considered for publication.

Legend  
ESSENTIAL = show-stopper, must be fixed  
MAJOR  = serious, but in-principle fixable without new data  
MINOR  = should be addressed, but does not block acceptance  
NIT   = cosmetic / wording / typographical


------------------------------------------------------------------------
ESSENTIAL FINDINGS
------------------------------------------------------------------------

P5-E1 Sec. VI A, p. 5, Table II  vs. Sec. VII, p. 10, Table VI  
• Problem Canonical class-range is quoted two different ways:  
  – Table II and text give range = 0.0198 (→ 1.98 percentage points).  
  – Table VI line (Rs=25, λth=0) gives 0.165 “percentage points”.  
  Both cannot be true; 0.165 pp would correspond to Δf≈0.00165, an order of magnitude smaller than the earlier 0.0198.  
• Fix Re-compute and make the canonical range consistent everywhere; update all downstream statements that use the 0.165/0.22 numbers (sec. VII discussion and Fig. 5).

P5-E2 Sec. VII, p. 10, statement “per-cell range … never exceeds 0.22 percentage points (max 0.0022 at Rs=25, λth=0.3)”  
• Problem 0.22 percentage points is 0.0022 in f.  The text writes both 0.22 and 0.0022 in the same sentence as if identical.  
• Fix Adopt one consistent unit (either f-units or pp) and propagate through the manuscript.

P5-E3 Sec. VIII F, p. 13, Table X and surrounding text  
• Problem The “monopole” baseline f_P5_CW is estimated from the *same* 812 793 galaxies that are then tested class-by-class.  This induces a correlation:  
    Var(f_class – f_total) = Var(f_class) + Var(f_total) – 2 Cov(…)  
  The reported σ_vs monopole treats f_total as error-free, thereby under-estimating σ by ≈√(1 – n_class/N_tot).  
• Fix Either (i) treat f_P5_CW as an external parameter (use Paper IV value with its quoted uncertainty) or (ii) include the covariance term.  All σ_vs monopole values, and every inference that no class exceeds |σ|≈1.1, must be recomputed.

P5-E4 Sec. V, Eq. (1) and repeated use throughout  
• Problem The Paper IV monopole offset Δf_CW = –0.0026 itself has a quoted uncertainty (0.000279 in Paper IV).  Nowhere is this propagated when predicted σ_pred values are compared to observed σ.  
• Fix Add the 6 % fractional uncertainty of Δf to the σ_pred error budget (or quote 1σ bands) every time σ_obs–σ_pred is used as a significance diagnostic.

P5-E5 Sec. XI, p. 18 (RSD caveat)  
• Problem The V-Web field is built in redshift space but the paper ultimately claims a 0.1 %–level null.  The text gives only an order-of-magnitude argument (σ_v/aH ≲5 Mpc h⁻¹) without any quantitative propagation into Δf_CW.  
• Fix Either (a) rerun the V-Web classification on a Kaiser/FOG-corrected reconstruction, or (b) provide a numerical Monte-Carlo showing that plausible RSD shifts (<5 Mpc h⁻¹) change the class fractions by ≪0.001 in f_CW.  A verbal estimate is not sufficient at 10⁻³ precision.

P5-E6 Throughout (e.g. Abstract, Sec. VI D)  
• Problem σ values from different null procedures (binomial Z, permutation max-stat, Bonferroni thresholds) are juxtaposed without the explicit “not directly comparable” reminder required by the policy (see reviewer instruction #7).  
• Fix Every place where a binomial Z is written next to a permutation p-value or Bonferroni threshold must add a clause making the distinction explicit.

------------------------------------------------------------------------
MAJOR FINDINGS
------------------------------------------------------------------------

P5-M1 Sec. VII, Fig. 5 heat-map and Table VI (Phase-2 sweep)  
The grid cell size is 25.9 h⁻¹ Mpc, identical to the Gaussian Rs=25 h⁻¹ Mpc smoothing.  With this choice the effective resolution is one grid cell, so changing Rs from 10→50 is largely cosmetic.  This undercuts the stated “hyper-parameter robustness”.  A higher-resolution grid (≥512³) or at least a test on 384³ should be shown.

P5-M2 Sec. VI A, void class n=428 – counting noise  
0.7 σ is called “uninformative”, yet later (Sec. VII) the same bin is included in the per-cell range statistic.  Either drop the void bin from the range calculation or quote range both with and without it.

P5-M3 Sec. IX A, Tempel cross-validation  
The mapping “Tempel multiplicity ≥20 ↔ V-Web cluster” is not justified; multiplicity is not a proxy for tidal eigen-value collapse in a thin shell survey.  At minimum, show the purity/completeness of this mapping on a simulation or drop the quantitative concordance claim (0.026 pp).

P5-M4 Permutation tests use N_MC = 1000 (Sec. V, p. 4)  
This sets a floor p_min ≈ 0.001.  Several p-values are quoted to 3 significant figures below 0.05 (e.g. p=0.135, 0.372).  With only 1000 draws, the third decimal is meaningless.  Quote two significant figures and add the ±0.001 Monte-Carlo uncertainty.

P5-M5 Sec. VIII D, “catalog-native V2” sample sizes  
n_void = 86 276, yet σ_void is reported as –0.24.  Re-computing with the given counts (CW not given) I cannot reproduce –0.24.  Provide the raw n_CW, n_total used.

------------------------------------------------------------------------
MINOR FINDINGS
------------------------------------------------------------------------

P5-m1 Equation (2), p. 4 – The erfc⁻¹ form implicitly assumes two-sided test; state this explicitly.

P5-m2 Table I (p. 3) lists “Leg DES 4,724”; footnote later says DES covers 5 deg² – supply reference or cut.

P5-m3 Page 9, Fig. 4 colour-bar units missing (“σ_from_half”).

P5-m4 Multiple places: “σ= −4.75” but Fig. 6 lower panel y-range only to ±4.5 – the pixel at –4.75 is clipped.

P5-m5 Page 12: “Δf_CW = 0.0007, statistically indistinguishable” – give the 1σ binomial error (~0.004).

P5-m6 Duplicate phrase p. 11 line 1: “per-galaxy cross-match of the V-Web void-class matched-spiral subsample”.

P5-m7 Section headings use Roman numerals but Appendix uses A/B; uniformise.

P5-m8 Reference [11] “in submission to MNRAS” – give arXiv number only.

------------------------------------------------------------------------
NITS
------------------------------------------------------------------------

P5-n1 Abstract: “∼130× larger” → give numbers once (56 981 vs 428).

P5-n2 Fig. 3 right panel: diamond markers not described in caption.

P5-n3 Typo p. 6: “decom￾positions” (split word).

P5-n4 p. 18 “Rubin-scale chirality classifier … would resolve sub-pixel …” – speculative; move to Outlook.

------------------------------------------------------------------------
## Summary recommendation
MAJOR REVISIONS

The core idea is sound, but the manuscript in its present form suffers from internal numerical inconsistencies (E1–E2), an incorrect treatment of correlated uncertainties (E3–E4), an un-quantified RSD systematics floor (E5), and inconsistent significance bookkeeping (E6).  These are methodological issues that must be fixed before the science claims can be trusted.  I therefore recommend **MAJOR REVISIONS**.