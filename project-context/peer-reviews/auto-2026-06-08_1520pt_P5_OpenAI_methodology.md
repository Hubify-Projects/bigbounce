# P5 auto-2026-06-08_1520pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9815 chars)
**Wall time**: 387.7s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test …”

Scope of review
I audited the statistical methodology, derivation chains, dimensional consistency, internal arithmetic, and the traceability of all load‑bearing scalars in the abstract, tables, figures, and conclusions. I recomputed every quoted σ-from-half and every fraction or range that is possible from the displayed numbers, and checked consistency between “primary” and “secondary” analyses and their null procedures.

Findings

P5-E1 (ESSENTIAL)
Section VII, p. 8–9 (Phase 2 sensitivity sweep)
Problem: Impossible sample size and misuse of σ in sweep narrative.
Quote: “The largest single-cell |σfrom half| across the entire sweep is 11.32 (filament at Rs = 10, λth = 0, n = 3,696,152). This is the catalog-wide ∆fCW = −0.0026 monopole leaking through the largest sample bin and is predicted, not measured.”
- The chirality-relevant matched sample is N=791,635 (Table I). No per-class count can exceed this. Reporting n=3,696,152 is arithmetically impossible for the chirality-labeled sample.
- It is methodologically inconsistent to report a “|σfrom half|” for a population without chirality labels (if the 3.7M refers to DR1 spectro counts).
Required fix: Remove or correct this paragraph. If you intend to illustrate σpred using σpred = 2∆fCW√N, use the correct matched-spiral class counts for that sweep cell and label it explicitly as a prediction, not an observed statistic. Report the true per-class N for that sweep cell (which must sum to 791,635), and provide the observed |σfrom half| alongside σpred for those classes. If the 3.7M refers to a different population, do not call it “σfrom half,” and do not mix it with observed σ in the same paragraph.

P5-E2 (ESSENTIAL)
Section VI D, p. 7 (Tracer-program stratification within the filament class)
Problem: Inconsistent and impossible counts for bright vs dark within a class.
Quote: “filament bright (n = 416,701) σ = −2.80 vs filament dark (n = 21,203) σ = +2.85”
- The total filament class has n=408,187 (Table II). Reporting bright+dark = 437,904 exceeds the total by 29,717. This invalidates the subsequent |z| ≈ 3.4σ bright-vs-dark comparison and compromises the “sign-flip” diagnostic.
Required fix: Provide a complete, internally consistent cross-tabulation of filament counts by target program (bright, dark, backup, other) that sums exactly to 408,187, and recompute all σ and the two-sample z tests. Provide the same table for the cluster class for parity. If backup/other are included in either side of a two-way split, state so explicitly and show sums.

P5-E3 (ESSENTIAL)
Section V.B, p. 5 (Primary vs secondary analysis)
Problem: Post hoc designation of “primary” analysis and incomplete multiplicity control.
- You explicitly declare the DESIVAST-anchored path as “primary” post hoc. The paper then reports many additional scans (V-Web sweeps, density/redshift/sky splits, ASTRA, Tempel).
- The multiplicity accounting is treated for the five DESIVAST estimators, but not for the broader family of secondary tests where formal “findings” (e.g., the bright–dark sign-flip and |z| ≈ 3.4σ) are quoted.
Required fix: Either (i) provide a registered analysis plan or an a priori selection rationale frozen before touching the DR1 data, or (ii) reframe every secondary finding as exploratory with no claims of significance, and apply a global multiplicity control across all reported tests if any are retained as inferential. The current bright/dark “≈3.4σ” statement must be removed or clearly labeled as exploratory and re-computed once P5-E2 is fixed.

P5-E4 (ESSENTIAL)
Whole paper (multiple locations)
Problem: Mixing of conceptually different significance measures without “not directly comparable” warnings at point of use.
- The manuscript alternates between: (a) σfrom half (binomial-normalized deviation), (b) label-shuffle permutation p-values, (c) Bonferroni z-thresholds, and (d) σpred from a catalog monopole model. In several places these appear side-by-side (e.g., Table V + Bonferroni threshold; Fig. 3 right juxtaposing σobs and σpred) without an explicit “not directly comparable” note at each juxtaposition.
Required fix: At every location where two distinct null frameworks or statistics are juxtaposed (e.g., empirical permutation p vs. Bonferroni z; σobs vs. σpred), add a local sentence clarifying they are not directly comparable and stating which one is the inferential basis. Keep σpred clearly designated as a model-based prediction, not an observed statistic.

P5-M1 (MAJOR)
Section VI A, p. 5–6 (σpred values)
Problem: Numerical inconsistency in σpred magnitudes.
Quote: “predicting σpred from ∆fCW = −0.0026 gives σpred(filament) ≈ −3.16 and σpred(cluster) ≈ −3.28”
- Using Eq. (1) with Nfil=408,187 gives σpred=2∆f√N≈2(−0.0026)√408,187≈−3.32, not −3.16. For Nclu=397,505, σpred≈−3.28 (your cluster value is fine).
Required fix: Correct σpred(filament) to −3.32 (or recompute using whatever N you actually used, but then report that N). Check the same consistency wherever σpred is quoted.

P5-M2 (MAJOR)
Section VIII A, p. 10–11 (V-Web void vs DESIVAST holes, n=6)
Problem: Overinterpretation from an extremely small sample.
- From six low‑z V-Web void-class spirals, 0/6 lie inside DESIVAST holes. You then generalize to “the V-Web void class at low z is dominated by survey-edge density artifacts.” This conclusion cannot be supported by a sample of six, regardless of qualitative consistency with T-Web volume fractions.
Required fix: Reframe this as a qualitative illustration only, or better, quantify void‑label purity at low z using a larger, objective procedure (e.g., measure the fraction of low‑z V-Web void‑labeled galaxies that fall within a buffer distance of DESIVAST voids vs. a matched control). If you cannot robustly quantify, tone down to a non‑inferential remark.

P5-M3 (MAJOR)
Section VIII (RSD immunity for DESIVAST void membership), p. 10–11
Problem: The “essentially RSD‑immune” statement is too strong without a boundary‑erosion test.
- You assert σv/(aH) ≲ 5 Mpc/h is “several times smaller” than void Reff ≳10 Mpc/h, implying negligible misclassification. For small voids that is a ~50% radial shift at the scale of boundary proximity; near-boundary galaxies can flip memberships.
Required fix: Provide a quantitative bound by eroding/dilating each void by ±ΔR (e.g., ΔR=5 Mpc/h) and computing the fraction of matched spirals whose membership flips. Report the induced change in fCW. Alternatively, add this as a limitation instead of a claim of near‑immunity.

P5-M4 (MAJOR)
Section VII, p. 8–10 (Phase 2 sweep reporting)
Problem: Insufficient transparency on per-cell class populations and fCW values.
- You report only the per-cell max “range” (Table VI) and assert it is below counting-error floors, but you do not provide the underlying per-class n and fCW per cell to audit that assertion.
Required fix: Add a table (supplemental is fine) with, for each of the nine (Rs, λth) cells: per-class n and fCW (and σfrom half). Identify the cell with the maximum 0.22 pp range and show its four class values. This makes the “below counting-statistics floor” claim verifiable.

P5-M5 (MAJOR)
Section VI B, p. 6 (Logistic regression)
Problem: Incomplete reporting of regression diagnostics.
- You report a z‑coefficient “0.0059” and “no significant intercept (0.000652)” without units, standard errors, z‑scores, or p‑values. The model covariates and sample size should be restated for the regression subset.
Required fix: Report coefficient estimates with standard errors, z‑statistics, p‑values, a goodness‑of‑fit measure, and the exact N used. Clarify variable scaling/units (e.g., z raw vs. standardized).

P5-M6 (MAJOR)
Conclusions and Abstract, p. 1–2 and p. 18–19
Problem: The abstract and conclusions contain several quantitative claims that depend on sections with issues above (P5-E1, P5-E2, P5-M1–M4). In particular, the “Phase 2 sensitivity sweep … largest |σ| 11.32” and the bright/dark “|z| ≈ 3.4σ” sign‑flip are not currently supported by correct arithmetic or tables.
Required fix: After fixing the core inconsistencies, re‑audit the abstract to ensure every scalar (ranges, σ, p) has a traceable and correct source in the body.

P5-Min1 (MINOR)
Section V, p. 4–5 (Jeffreys intervals)
Problem: The text mentions “95% Jeffreys binomial credible intervals” in figures, but the intervals are never tabulated or compared numerically to Clopper–Pearson or normal approximations.
Required fix: Provide the numerical 95% intervals for Table II in an appendix/supplement or add them to the table.

P5-Min2 (MINOR)
Section IX A, p. 15–16 (Tempel FoF concordance)
Problem: The “0.026 pp” filament concordance statement is fine numerically but should include the Tempel per‑bin n used for fCW and the uncertainty on the difference.
Required fix: Add the per‑bin Ns (you give n=14,317 for filament-like) and the standard error on the difference of proportions (or a test) to show the 0.026 pp is indeed negligible relative to counting error.

P5-Min3 (MINOR)
Section VIII F, p. 12–13 (HEALPix σvs monopole distribution)
Problem: You report mean, std, skewness, and excess kurtosis for σvs monopole at NSIDE=32 across “1,821 valid pixels,” but the selection criterion for pixel validity is not repeated here (a threshold appears later for a different analysis).
Required fix: Specify the per‑pixel minimum-count criterion used for this 1,821‑pixel set.

P5-Min4 (MINOR)
Equation (1), p. 4
Problem: The first form σpred = ΔfCW/0.5/√N is unconventional and may be misread.
Required fix: Present the single compact form σpred = 2ΔfCW√N and, if you keep the first, clarify the algebraic equivalence in text.

P5-N1 (NIT)
Footnote “a” on p. 2: grammar/placement (“a We use the tidal-tensor …”) bleeds into body text. Fix footnote formatting.
P5-N2 (NIT)
Extremely small p reported as “p < 10−1000” (p. 8). This is not meaningful beyond machine precision in typical software.
Required fix: Report p ≪ 10−16 or give the test statistic and degrees of freedom and let readers infer extremeness.

P5-N3 (NIT)
Minor spacing/typos: e.g., “Density- quartile” (extra space) on p. 7; “Phase 2 sweep robustness (Sec￾tion VII)” line breaks; a few accent/encoding artifacts in author names (e.g., Rinc´on).
Required fix: Standard copy-edit pass.

Length
For the methodological contribution (null test and cross‑validation), 20 pages is longer than necessary, especially with repeated narrative. If streamlined after the mandatory fixes, a 12–15 page main text plus a short appendix/supplement (tables for Phase‑2 cells, regression details) would suffice.

Additional cross‑checks performed (pass)
- Table I tallies: CW+CCW+NS=2,232,212; SPECTYPE GALAXY+QSO=2,232,212 — consistent.
- Table II fCW, σfrom half recompute correctly; range 0.5034–0.4836=1.98 pp — correct.
- Density‑quintile σpred at N≈158,327: 2|Δf|√N≈2.07; residuals match Table III.
- DESIVAST void analysis: nvoid=56,981, f=0.4964 yields σ≈−1.72; non‑void N=621,964 f=0.4971 σ≈−4.57; Δf=0.0007 — consistent.
- HEALPix maximal‑void stratification sums to nlz=678,945 and σ values match simple recomputation.

Reproducibility/data availability
You state “companion data repository” repeatedly but do not provide an explicit URL/DOI in the manuscript. For PRD standards, a concrete link is required, with frozen code/configs to reproduce the exact tables/figures.

Required fix: Add a persistent DOI (Zenodo or equivalent) with the code/config and all tables used to generate Figures/Tables (including the nine-cell sweep per-class outputs).

## Summary recommendation
MAJOR REVISIONS

Justification: The core DESIVAST‑anchored void/non‑void null and the main V‑Web class‑level nulls are, on balance, methodologically sound and most arithmetic checks out. However, there are critical inconsistencies that must be corrected before the paper meets PRD standards: an impossible sample size and misuse of σ in the Phase‑2 sweep; internally inconsistent filament bright/dark counts that undermine a highlighted diagnostic; a few σpred numerical mismatches; overinterpretation from n=6 in a low‑z void purity check; incomplete reporting for the sweep and the regression; and missing repository links. These are fixable, but they are essential for a rigorous methodological paper.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (fresh-eyes audit)

P5-E5 (ESSENTIAL)
Section VI D b vs Section XI (target-program split)
Problem: Direct contradiction between two places in the manuscript about bright vs dark differences.
- Section VI D b reports bright 0.4970 vs dark 0.5051 on the full matched-spiral catalog (Δf ≈ 0.0081), and highlights a sign flip within filament (and a |z| ≈ 3.4σ difference once P5‑E2 is fixed).
- Section XI (Systematics) states: “target-class split (BGS vs. LRG‑ELG‑QSO) with BGS‑only CW fraction within ±0.001 of LRG‑ELG‑QSO.”
These statements cannot both be true.
Required fix: Recompute and report a single, authoritative bright vs dark comparison for exactly the same population in both sections, with counts, fractions, σ, and a two‑sample test. If Section XI intended a different subset (e.g., z‑limited or env‑labeled‑only), state it and reconcile the numbers. Remove whichever statement arose from an inconsistent subset or stale numbers.

P5-M7 (MAJOR)
Section VII A (Bonferroni-9 threshold)
Problem: The Bonferroni family-wise z-threshold for the nine-cell sweep is misstated.
- You quote “Bonferroni-9 (α = 0.05) threshold |σ| ≈ 3.02.” Using Eq. (2), the two-sided normal threshold should be zBonf = √2 erfc−1(α/K) = √2 erfc−1(0.05/9) ≈ 2.8 (≈2.77–2.83 depending on numeric routine), not 3.02.
Required fix: Correct the threshold and audit any inferential statements that relied on 3.02. If you intended α per tail or a different calibration, state it explicitly and use a consistent formula.

P5-M8 (MAJOR)
Section VIII B (DESIVAST void membership via KDTree k=20)
Problem: The k-NN shortcut risks false negatives.
- Testing point-in-sphere membership by checking only the k = 20 nearest hole centers is not guaranteed to find all containing spheres when many centers lie within Rmax (your own text cites VoidFinder Rmax ≈ 24 Mpc/h). A galaxy can be inside a farther but large-radius sphere that is not among the 20 nearest centers.
Required fix: Replace with a radius-query (ball tree) at R = Rmax per algorithm, or a per-galaxy check against all spheres within each file’s stated radius. Recompute nvoid, fvoid, and σ for the DESIVAST-anchored analysis and report the delta vs the k-NN approximation.

P5-M9 (MAJOR)
Section V (Nulls declared) vs Results (what is reported)
Problem: “Position-shuffle” null is described but never used in Results.
- The methods promise two nulls (label-shuffle and position-shuffle). All reported permutation p-values are from label shuffles; I found no position-shuffle results in the figures, tables, or text.
Required fix: Either report the position-shuffle outcomes wherever you use permutation nulls (HEALPix scans, redshift/density splits, etc.), or remove the claim and adjust the Methods.

P5-M10 (MAJOR)
Figures and text (monopole baselines 0.4974 vs 0.4972)
Problem: Inconsistent baseline for the dotted “catalog monopole” line.
- Several plots/text use the Paper IV global mean 0.4974 as the reference line, while §VIII F establishes that the working DR1‑matched sample has fP5 = 0.4972. Using 0.4974 in those figures subtly biases “visual residuals.”
Required fix: Use the sample-specific baseline consistently in all figures that visualize this sample, or show both lines with a caption note. In Table X specifically, recompute σvs monopole using the exact baseline of the same subset to which the rows apply (see next item).

P5-M11 (MAJOR)
Section VIII F (σvs monopole table uses a different-sample baseline)
Problem: Table X applies the 812,793‑object “P5” baseline to residuals described as “on the matched‑spiral subsample.”
- If any residuals in Table X are computed on the 791,635 headline subsample, they must use that subsample’s monopole (not the 812,793 superset’s 0.49719), or you must explicitly state that all rows are recomputed on the 812,793 set.
Required fix: Make the sample alignment explicit and recompute residuals so that each “σvs monopole” uses the baseline from the same population being summarized.

P5-M12 (MAJOR)
Section VI B (Logistic regression model specification)
Problem: The angular dependence is under-specified.
- Testing RA dependence with only cos α (without sin α) cannot capture a general azimuthal mode; similarly using |sin δ| alone does not span the typical spherical-harmonic basis used for sky tests. The conclusion “no redshift dependence” is fine for z, but the “no sky dependence” inference drawn from this regression is underpowered.
Required fix: Include both sin α and cos α and a symmetric pair for declination (e.g., sin δ and cos δ, or fit Yℓm up to ℓ = 1) alongside z and confidence. Report full coefficients, standard errors, z/p, N, and a fit quality measure.

P5-M13 (MAJOR)
Global (permutation resolution vs LEE statements)
Problem: NMC = 1000 permutations yields p-value granularity of ~0.001. For LEE-corrected decisions and multi-NSIDE pixel scans, this resolution can be marginal.
Required fix: Increase NMC (e.g., 50,000–100,000) for the headline permutation-based LEE calls (HEALPix, redshift/density quintiles), or report Monte Carlo uncertainty on p (e.g., Clopper–Pearson intervals for the permutation tail count) and confirm that conclusions are invariant.

P5-Min5 (MINOR)
Section IX A and Figure 7 (“0.2 pp concordance spec”)
Problem: The 0.2 pp “spec” for classifier concordance is invoked but never defined or justified.
Required fix: Define this specification quantitatively (e.g., require |Δf| less than the combined 1σ standard error of the difference for the two classifiers on the overlap), and report the standard error/test for the 0.026 pp filament case.

P5-Min6 (MINOR)
Section VII (typo in sweep grid definition)
Problem: “Ngrid = 256 × λth ∈ {0.0, 0.1, 0.3}” appears; Ngrid should be 256^3 and is orthogonal to λth.
Required fix: Correct the sentence to “Ngrid = 256^3; λth ∈ {0.0, 0.1, 0.3}.”

P5-Min7 (MINOR)
Nomenclature consistency (V‑Web vs T‑Web)
Problem: You are using a Tidal‑tensor density Hessian (often called T‑Web), not the velocity‑shear V‑Web. The footnote mentions this, but the body repeatedly says “V‑Web,” which risks confusion.
Required fix: Either rename throughout to “T‑Web (tidal‑tensor) classifier” or keep “V‑Web” with an upfront, bold caveat and replace “velocity shear” terminology wherever it might mislead.

P5-Min8 (MINOR)
Section XII B (reference to “Paper III”)
Problem: Paper III is cited in text but is absent from the references.
Required fix: Add a placeholder citation for Paper III or remove the claim until a citable entry exists.

P5-Min9 (MINOR)
Table I and usage of SPECTYPE=QSO in the chirality-relevant set
Problem: You include 17,180 spectroscopic QSOs in the matched catalog. The number of QSOs inside the chirality‑relevant subset is not reported, and QSOs are unlikely to be valid spiral morphology targets.
Required fix: Report how many QSOs are in the CW/CCW subset. Provide a sensitivity check excluding all spectroscopic QSOs from the chirality‑relevant sample and show that headline results are unchanged.

P5-Min10 (MINOR)
Figure captions and baseline lines
Problem: Several figures overlay the Paper IV global line (0.4974) while the text in §VIII F emphasizes the sample monopole (0.4972).
Required fix: State in each caption which baseline is drawn and why; consider drawing both with a legend.

P5-Min11 (MINOR)
HEALPix “valid pixels” counts inconsistent across sections
Problem: §VIII F reports statistics over 1,821 valid NSIDE=32 pixels, while Fig. 6 bottom (also NSIDE=32) uses 1,496 valid pixels. These likely reflect different cuts (z ≤ 0.24 vs full, and/or ≥ 200 spirals per pixel), but the criteria are not co-stated.
Required fix: For each HEALPix analysis, specify the exact sample and per-pixel count threshold, and reconcile the differing valid‑pixel counts in text.

P5-Min12 (MINOR)
Section IV A (Poisson normalization and λth units)
Problem: Φ(k) = −δk/k^2 omits the 4πG a^2 ρ̄ factor (or an explicit rescaling). Since you sweep λth = 0–0.3, its numerical meaning depends on this normalization.
Required fix: Add a sentence explaining the rescaling convention and that λth values are dimensionless thresholds in these rescaled units, not directly comparable to other works unless the same convention is used.

P5-Min13 (MINOR)
Permutation p-values reporting
Problem: p-values like 0.135 from 1,000 permutations are point estimates without uncertainty.
Required fix: Report p with a Monte Carlo standard error or an exact binomial CI (e.g., p = 0.135 ± 0.011 for NMC = 1000) where p is used to support LEE decisions.

P5-Min14 (MINOR)
Section V (definition of “confidence” covariate)
Problem: The logistic regression uses a “confidence” covariate, but its definition (e.g., max softmax probability of CW/CCW classifier) and scaling are not given here.
Required fix: Define “confidence,” give its range, and confirm whether it is standardized in the regression.

P5-Min15 (MINOR)
Figure 6 top caption vs body text
Problem: The caption notes “885 occupied pixels, median 4 voids/pix” at NSIDE=32, but the body discussion earlier at NSIDE=16 lists “297 occupied pixels, median 14 voids/pix.” The difference in NSIDE explains this, but it is not explicitly connected.
Required fix: Add a clarifying sentence connecting the different NSIDEs and why the voids/pixel distribution changes.

Explanation
These issues were not covered in my initial report and arose from a stricter pass focused on cross‑section consistency, baseline alignment, multiple-testing thresholds, and method guarantees (k-NN void membership). Several are arithmetic/logic contradictions (E5, M7), some are missing method results that were promised in Methods (M9), and others are specification/clarity gaps that materially affect interpretation (M10–M13). Addressing them will materially improve rigor and reproducibility.