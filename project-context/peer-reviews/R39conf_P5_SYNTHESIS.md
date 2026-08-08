# P5 R39conf — v3 native-PDF cross-vendor SYNTHESIS

**Reviewers**: Claude_brutal, Gemini_cosmology, Grok_brutal, OpenAI_methodology, Perplexity_citations

## ⛔ ROUND DEGRADED — reviewer leg(s) FAILED: Claude_brutal, OpenAI_methodology
Failed legs are API errors, NOT zero-finding clean reviews. This round
MUST NOT count toward any clean-round counter; re-run after the failure
(e.g. API credit top-up) is resolved.
**Total findings (across all reviewers)**: 43
**Distinct consensus groups**: 7

## Per-reviewer finding counts

| Reviewer | ESSENTIAL | MAJOR | MINOR | NIT |
|----------|-----------|-------|-------|-----|
| Claude_brutal | 0 | 0 | 0 | 0 |
| Gemini_cosmology | 1 | 2 | 3 | 2 |
| Grok_brutal | 3 | 4 | 0 | 2 |
| OpenAI_methodology | 11 | 8 | 7 | 0 |
| Perplexity_citations | 0 | 0 | 0 | 0 |

---

## Consensus-grouped findings (most reviewers first)

### `companion` — ESSENTIAL — **CONSENSUS** (2 reviewers)

Reviewers: Gemini_cosmology, Grok_brutal

- **[Gemini_cosmology/P5-E1/ESSENTIAL]**: **P5-E1: Reliance on Unpublished Companion Work (Standalone-Reader Test)** *   **Section:** Throughout, starting with Abstract (p. 1) and Introduction (p. 3). *   **Problem:** The paper is critically dependent on "Paper IV [3]", which is described as a "companion work, not yet peer-reviewed" and "currently in preparation". This companion paper provides the foundational 8.47M-galaxy chirality catalog and, crucially, the characterization of the `-0.26 pp` classifier-monopole systematic. The entire analysis of the present manuscript is framed around testing for environmental variations *after* ac…
- **[Grok_brutal/P5-E1/ESSENTIAL]**: **P5-E1 (Section I, p. 3; also abstract p. 1)**   The headline null result is obtained only after subtracting a catalog-wide monopole offset \(\Delta f_{CW} \approx -0.0026\) whose value and uncertainty are taken directly from the unpublished companion Paper IV. The text explicitly states “Paper IV [3] (companion work, not yet peer-reviewed)”. A standalone reader cannot recompute or verify the central correction that converts every per-class residual into a null.   **Required fix**: Reproduce the monopole measurement inside this manuscript (or publish Paper IV first).

### `duplicate_phrase` — MINOR — **CONSENSUS** (2 reviewers)

Reviewers: Grok_brutal, OpenAI_methodology

- **[Grok_brutal/P5-N2/NIT]**: **P5-N2 (p. 2 footnote)**   The phrase “we use the tidal-tensor formulation \(T_{ij}=\partial^2\Phi/\partial x_i\partial x_j\) with \(\Phi\)” is repeated verbatim in the title footnote and again in the body; cosmetic duplication.    No internal-audit tags, version strings, or duplicate phrases of the form “canonical canonical” appear in the rendered pages. All tabulated \(\chi^2\), \(\sigma\), and \(p\)-values recompute correctly from the displayed counts within rounding.    **Summary recommendation**
- **[OpenAI_methodology/P5-N4/MINOR]**: **P5-N4  (Appendix A p. 29)** –  The toy EFT operator explicitly breaks rotational invariance.  Add one sentence clarifying it is schematic.  -------------------------------------------------------------------- NITS --------------------------------------------------------------------  - Duplicate phrase “canonical canonical” spotted once in §VI C.   - “monopole-referenced tests” appears both hyphenated and not.   - Reference [12] DOI missing.   - Several arXiv IDs lack the “arXiv:” prefix.  -------------------------------------------------------------------- ## Summary recommendation

### `sigma_mixing` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P5-E7/ESSENTIAL]**: **P5-E7  (§VII Table VII p. 15)** –  Three Rs = 10 Mpc h⁻¹ cells lie *below the 25.9 Mpc h⁻¹ grid spacing*, hence the quoted range and σ values combine incompatible resolutions.  Nevertheless those cells are used in the global Bonferroni-9 family.   *Fix:* Either discard the under-resolved cells from the sweep or rebuild them on a ≥512³ grid so that Rs ≥ 1.5 × cell size.  --------------------------------------------------------------------

### `table_ii` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: Grok_brutal

- **[Grok_brutal/P5-E2/ESSENTIAL]**: **P5-E2 (Table III p. 8; Fig. 3 p. 9; abstract p. 1)**   The void bin contains only 428 galaxies. The reported \(\sigma_{\rm from\,half} = -0.68\) is consistent with counting noise alone; the 95 % Jeffreys interval comfortably includes parity. No frequentist power calculation or Bayesian upper limit on an environment-dependent amplitude is supplied. The claim “no evidence for environmental dependence” is therefore driven by an under-powered subsample whose size is 130–2000× smaller than the filament/cluster bins.   **Required fix**: Quote explicit 95 % upper limits on any void-specific \(\Delt…
- **[Grok_brutal/P5-M2/MAJOR]**: **P5-M2 (Table II p. 8; §V p. 6)**   Nine Phase-2 cells are tested with a Bonferroni-9 threshold \(|\sigma| = 2.77\), yet the primary family (five DESIVAST estimators) already uses Bonferroni-5. The text never states whether the two families are disjoint or how the overall family-wise error rate is controlled when both are reported together.

### `audit_artifact` — MAJOR — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P5-M5/MAJOR]**: **P5-M5  (length)** –  31 pages plus copious path printouts is excessive for a *methods* null-result.  A focused PRD article should not exceed ~20 text pages.   *Fix:* Move the entire R39 “closure-wave” audit prose, path listings and version changelog to online supplementary material.  --------------------------------------------------------------------

### `table_iv` — MAJOR — _single-reviewer_ (1 reviewer)

Reviewers: Grok_brutal

- **[Grok_brutal/P5-M4/MAJOR]**: **P5-M4 (Fig. 5 p. 11; Table IV p. 10)**   All five density-quintile residuals lie within \(|\sigma_{\rm obs}-\sigma_{\rm pred}| < 2\) of the Paper-IV monopole prediction. The largest deviation (1.87) is still below the Bonferroni-5 threshold of 3.09, but the paper never converts this into an effect-size statement (e.g., maximum allowed fractional environmental modulation).

## Other findings (34)

- **[Gemini_cosmology/P5-M1/MAJOR]**: **P5-M1: Paper Structure and Length** *   **Section:** Overall structure. *   **Problem:** The paper is 31 pages long, which is excessive for a manuscript whose primary finding is a null result. The narrative flow is confusing. The secondary analysis using the V-Web classifier (Sec. VI) is presented in full before the declared primary analysis using the DESIVAST catalog (Sec. VIII). This buries th…
- **[Gemini_cosmology/P5-M2/MAJOR]**: **P5-M2: Missing Effect Size for Main Homogeneity Test** *   **Section:** Abstract (p. 1) and Sec. VIA (p. 7). *   **Problem:** The abstract and main text report the omnibus homogeneity test result as "null (χ² = 3.55, 3 d.o.f., p = 0.31)". While statistically null, this result lacks a measure of practical significance or effect size. For a contingency test, a metric like Cramér's V is standard an…
- **[Gemini_cosmology/P5-m1/MINOR]**: **P5-m1: Typo in Tidal Tensor Definition** *   **Section:** Footnote 'a' (p. 2). *   **Problem:** The tidal-tensor formulation is given as `T_ij = ∂²Φ/∂x_i dx_j`. The second partial derivative in the denominator is incorrect. *   **Fix:** Correct the expression to `T_ij = ∂²Φ/∂x_i ∂x_j`.
- **[Gemini_cosmology/P5-m2/MINOR]**: **P5-m2: Ambiguous `n_iz` Notation** *   **Section:** Abstract (p. 1) and Sec. VIIIB (p. 17). *   **Problem:** The abstract uses the notation `n_iz = 678,945` for the DESIVAST BGS coverage range. The subscript `iz` is not standard and its meaning ("in-z-range"?) is not immediately obvious. The same notation appears in the body. *   **Fix:** Define the notation explicitly on first use or replace it…
- **[Gemini_cosmology/P5-m3/MINOR]**: **P5-m3: Inconsistent `sigma` Notation for Two-Sample Tests** *   **Section:** Throughout, e.g., Sec. VIIID (p. 18) vs. Sec. VIIIB (p. 17). *   **Problem:** The paper uses `z_Δ` for the two-sample z-score in some places (e.g., Sec. VIIIB) and `z_Δ` in others (e.g., Table X). While the Greek letter is a typo, the use of `z` for a z-score can be confused with redshift `z`. *   **Fix:** Use a consist…
- **[Gemini_cosmology/P5-N1/NIT]**: **P5-N1: Date Format** *   **Section:** Title block (p. 1). *   **Problem:** The date is given as "(Dated: June 2026 ... )". This appears to be a placeholder for the future. *   **Fix:** Use the current date of submission.
- **[Gemini_cosmology/P5-N2/NIT]**: **P5-N2: Redundant Wording in Figure Caption** *   **Section:** Fig. 8 caption (p. 22). *   **Problem:** The caption states "...per-pixel chirality `σ_from_half` on the z < 0.24 matched-spiral subsample restricted to pixels with ≥ 200 spirals...". The phrase "matched-spiral subsample" is redundant given the context. *   **Fix:** Simplify to "...per-pixel chirality `σ_from_half` on spirals at z < 0…
- **[Grok_brutal/P5-E3/ESSENTIAL]**: **P5-E3 (p. 1 abstract & §II p. 3)**   The abstract and introduction present the monopole-subtracted residuals as the primary result, yet the monopole itself is imported from an external, unreviewed work. This violates the “standalone reader” requirement for a methods paper in PRD.
- **[Grok_brutal/P5-M1/MAJOR]**: **P5-M1 (entire manuscript, 31 pages)**   The article is excessively long for a null-result methods paper. Sections VII–IX largely repeat the same four-class homogeneity test under different stratifications. PRD articles of this type are typically ≤12–15 pages; the present length dilutes the central claim.
- **[Grok_brutal/P5-M3/MAJOR]**: **P5-M3 (§VI.B p. 7)**   The paper declares the DESIVAST VoidFinder path “primary” post hoc after seeing the data. No pre-registered analysis plan is referenced, and the multiplicity of possible primary choices is acknowledged only as a caveat rather than corrected for.
- **[Grok_brutal/P5-N1/NIT]**: **P5-N1 (multiple figure captions)**   Axis labels on Figs. 3, 5, 7, 8 omit explicit units for \(\sigma_{\rm from\,half}\) (should read “\(\sigma_{\rm from\,half}\) (binomial, relative to 0.5)”). Minor but required for PRD.
- **[OpenAI_methodology/P5-E1/ESSENTIAL]**: **P5-E1  (Abstract p. 1 & throughout)** –  Entire statistical calibration is taken from the *un-reviewed* “Paper IV” catalogue (classifier monopole Δf_CW = –0.0026).  All environment σ-values are interpreted *after subtracting this external bias*, yet the present paper never re-validates the bias on a control set nor propagates its own uncertainty into any test.   *Fix:* Either (i) demonstrate int…
- **[OpenAI_methodology/P5-E2/ESSENTIAL]**: **P5-E2  (§VI A p. 8, Table XVI p. 30)** –  The primary 4 × 2 homogeneity χ² is computed on 812 793 “env-labelled rows” that include 28 973 duplicated TARGETID entries (3.56 %).  Duplicate observations violate the i.i.d. assumption of Pearson χ².  The authors recompute on the deduplicated 783 820 galaxies but still present the inflated χ² (= 3.55) in the abstract.   *Fix:* Replace the headline χ² …
- **[OpenAI_methodology/P5-E3/ESSENTIAL]**: **P5-E3  (§V A p. 6)** –  Look-elsewhere (LEE) p-values are drawn from only N_MC = 1000 permutations, yet the manuscript quotes three-decimal probabilities (e.g. p = 0.135, 0.089).  At that resolution the Monte-Carlo SE is 0.009–0.015, i.e. one full digit is noise.   *Fix:* Increase to ≥10 000 draws, or round p to two decimals and give the MC standard error alongside.
- **[OpenAI_methodology/P5-E4/ESSENTIAL]**: **P5-E4  (§IV p. 5, many places)** –  The paper calls its own Hahn-2007 tidal-tensor implementation “V-Web”, whereas in the literature V-Web normally denotes the *velocity-shear* classifier (Hoffman+2012).  The present classifier is a *T-Web* variant.   *Fix:* Use consistent nomenclature (e.g. “T-Web (density-Hessian)”) everywhere and remove “V-Web” or clearly disclaim the re-definition once in th…
- **[OpenAI_methodology/P5-E5/ESSENTIAL]**: **P5-E5  (§VIII p. 16, §XIII p. 28)** –  Redshift-space distortions are *not* corrected.  The authors argue that σ_v/(a H) ≈ 5 Mpc h⁻¹ is “several times smaller than R_s” and hence harmless, but the Hessian eigenvalues are direction-dependent and can swap at class boundaries.  No quantitative bound on class-flip rate is given for the *full* z ≤ 2 range.   *Fix:* Provide a first-order FoG+Kaiser es…
- **[OpenAI_methodology/P5-E6/ESSENTIAL]**: **P5-E6  (multiple)** –  Internal repository paths, commit hashes and YAML filenames (e.g. “pipelines/p5_desi_chirality/outputs/17_v0151…”) appear literally in the prose.  These are not acceptable in a PRD article.   *Fix:* Move all reproducibility information to a Data-Availability appendix or Git tag, and strip paths from the narrative text.
- **[OpenAI_methodology/P5-M1/MAJOR]**: **P5-M1  (Abstract & §VI D)** –  The bright/dark target-program split shows a 0.81 pp difference (|z| = 1.95) which the paper calls “residual structure”.  No systematic error budget is propagated to the headline null.   *Fix:* Provide a quantified estimate of how this selection-function residual could leak into the environment bins or demonstrate that it cancels exactly.
- **[OpenAI_methodology/P5-M2/MAJOR]**: **P5-M2  (§V p. 5)** –  σ_from_half values (pure counting) and σ_vs_monopole residuals are interleaved in the text and figures; in several places (e.g. Fig. 5 caption) the distinction is not restated.   *Fix:* Each panel or table containing both statistics must label them explicitly and remind the reader they are *not comparable*.
- **[OpenAI_methodology/P5-M3/MAJOR]**: **P5-M3  (§IX B p. 25)** –  For the Tempel overlap the like-for-like filament comparison is stated as 0.29 pp, z = 0.49 but the manuscript does not show the actual integer counts that lead to 0.49σ.   *Fix:* Add a contingency table (as is already done for Tables XVI–XVII) so readers can verify the test.
- **[OpenAI_methodology/P5-M4/MAJOR]**: **P5-M4  (§IV A step 4 p. 5)** –  Repeat coadds are treated as separate density tracers in the CIC deposit.  The deduplicated rebuild shifts class volumes by ~0.7 pp but this difference is not folded into any uncertainty.   *Fix:* Quote final f_CW values with an additional ±0.0007 systematic or adopt the deduplicated field.
- **[OpenAI_methodology/P5-N1/MINOR]**: **P5-N1  (§V p. 6)** –  Eq. (1) omits a factor ½ inside the square root when written as σ_pred = 2 Δf_CW √N.  The text above correctly describes the derivation; please insert a note that 0.5 √N in the denominator has been absorbed.
- **[OpenAI_methodology/P5-N2/MINOR]**: **P5-N2  (Fig. 3 caption p. 9)** –  “97.8 % of common-mask cells …” should read 97.9 % per the text on the previous page.
- **[OpenAI_methodology/P5-N3/MINOR]**: **P5-N3  (§IX C p. 26)** –  “T-Web DR1 in-footprint volume fractions …” cites Ref.[11] ranges {0.06-0.16, …}.  The LRG sheet fraction in that work is actually 0.43, not 0.45–0.48.  Please update.
- **[OpenAI_methodology/P5-E8/ESSENTIAL]**: **P5-E8  (global – duplicates in all permutation tests)**   All Monte-Carlo nulls (LEE, sky maps, density scans, Phase-2 cells) resample the **812 793 “env-labelled rows”**, i.e. they treat the 28 973 repeated TARGETIDs as *independent* draws.  Because duplicates share the same chirality label the effective number of free bits is ≈3.6 % smaller, which inflates the null variance and makes every rep…
- **[OpenAI_methodology/P5-E9/ESSENTIAL]**: **P5-E9  (§VIII F, Fig. 8)** –  The Pearson test between “void density per pixel” and σ uses 727 pixels with ≥200 spirals **after random duplicates are kept** (see E8).  Removing duplicates drops the correlation from r = +0.006 to r = –0.022 (p = 0.64; I recomputed from the supplied parquet).  The change is small but proves the statistic moves when duplicate-inflation is removed.   *Fix:* redo the…
- **[OpenAI_methodology/P5-E10/ESSENTIAL]**: **P5-E10  (Eq. 2, §V A p. 6)** –  The Bonferroni threshold formula |σ|^Bonf = √2 erfc⁻¹(α/K)   is dimensionally correct only for **one-sided** Gaussian tails.  All thresholds (3.09, 4.05, 2.58, 2.77) are therefore *too low* for the stated *two-sided* control.  The correct two-sided threshold is   |σ| = √2 erfc⁻¹(α/2K).   For K = 5, α = 0.01 this gives 3.26 not 3.09; for K = 1054, α = 0.05 it gives…
- **[OpenAI_methodology/P5-E11/ESSENTIAL]**: **P5-E11  (Equation-units, §IV A step 2 footnote)** –  The conversion “χ[Mpc] × h → χ[h⁻¹ Mpc]” is opposite to standard cosmological convention.   1 h⁻¹ Mpc = (1/h) Mpc, therefore   χ[h⁻¹ Mpc] = χ[Mpc] / h (not × h).   The numeric “sanity value” χ(0.2)=570 h⁻¹ Mpc is therefore 30 % *too small*; the true value with Planck-2018 parameters is ≈1246 h⁻¹ Mpc.  All Cartesian X,Y,Z coordinates, hence eve…
- **[OpenAI_methodology/P5-M6/MAJOR]**: **P5-M6  (Arithmetic – Table VII)** –  For the cell (Rs = 50, λ_th = 0.1) the reported range 4.12 pp cannot be obtained from the four f_CW values in the same CSV (0.4986, 0.5001, 0.4984, 0.4967 → range 0.34 pp).  Either the table prints the wrong cell, or the values were recomputed after the artifact was frozen.  Cross–check all nine rows.
- **[OpenAI_methodology/P5-M7/MAJOR]**: **P5-M7  (Fig. 2 vs body)** –  Caption says “wall 41.3 %” but §IV B parag. 1 says “wall 41.3 %” *and* the text on p. 15 states “wall 40.6 % after mask-dilation”.  Clarify which fraction is meant and keep it consistent.
- **[OpenAI_methodology/P5-M8/MAJOR]**: **P5-M8  (Unsupported novelty)** –  Abstract: “To our knowledge the *largest* matched-sample environmental chirality test in DESI DR1 to date”.  No quantitative comparison to Ullah+2026 or Zapata-Zuluaga+2026 is provided (both analyse ≥1 M galaxies for environment statistics).  Supply a numeric table (N_gal, N_void, N_fil, etc.) for all published DR1 studies and show the present sample is indeed l…
- **[OpenAI_methodology/P5-N5/MINOR]**: **P5-N5  (Cross-reference)** –  Body cites “Appendix C – reproducibility checklist”; Appendix C actually contains data-availability but the bullet list called “REPRODUCIBILITY CHECKLIST” sits *outside* that appendix.  Update the \ref or move the checklist into the appendix.
- **[OpenAI_methodology/P5-N6/MINOR]**: **P5-N6  (Equation labelling)** –  Eq. (1) is quoted many times but never numbered in the PDF (shows as “(1)” only in text).  Give it a \label and use \eqref everywhere; same for Bonferroni Eq. (2).
- **[OpenAI_methodology/P5-N7/MINOR]**: **P5-N7  (Stale number)** –  p. 17 claims “97.8 % of common-mask cells retain class”; Fig. 3 caption (p. 9) repeats 97.8 %; but §IV A step 4 now says 97.9 %.  Harmonise.  -------------------------------------------------------------------- NITS -------------------------------------------------------------------- - p. 11 “σfrom half already reported in Table V are all |σ| < 2” → “is”, grammar.   - …
