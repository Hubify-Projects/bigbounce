# P5 auto-2026-06-06_0021pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8591 chars)
**Wall time**: 295.9s

---

Referee report for “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals”

Scope of review
I audited the statistical methodology, internal arithmetic consistency, dimensional analysis, and the traceability of every load‑bearing scalar quoted in the abstract and conclusions to computations and tables in the body. I also checked the handling of multiple-hypothesis testing, the comparability of null procedures, the definition and stability of the primary estimator, and figure/table consistency.

Overall: The paper presents a careful negative result with multiple cross‑checks. Many numbers recompute correctly from the provided counts. However, there are several methodological and internal-consistency issues that must be resolved before this can meet PRD standards. The most important are: (i) an explicit contradiction between the reported bright/dark program split in Sec. VI D and the “systematics” bullet in Sec. XI; (ii) a promise to propagate the Paper IV monopole uncertainty that is not fulfilled anywhere in the analysis; (iii) an incorrect σpred value quoted for the filament class; (iv) post‑hoc declaration of the “primary” analysis without an accompanying selection penalty; and (v) recurrent juxtaposition of Gaussian σ and permutation p-values without an explicit caveat that the two test statistics are not directly comparable at the points of comparison.

Findings

ESSENTIAL

P5-E1
- Location: Sec. XI, p.17 (Systematics and null tests; bullet list)
- Problem: Contradiction with earlier results. Text: “target-class split (BGS vs. LRG‑ELG‑QSO) with BGS‑only CW fraction within ±0.001 of LRG‑ELG‑QSO. No test produces a >3σ residual after Paper IV‑monopole correction.” This directly contradicts Sec. VI D(b), p.7, which reports bright (BGS-dominated) fCW = 0.4970 (σ = −5.25) and dark fCW = 0.5051 (σ = +1.25), i.e., a difference of 0.0081 (0.81 percentage points), far larger than ±0.001.
- Required fix: Recompute and replace the target‑program split statement in Sec. XI with the correct numbers (after and before monopole subtraction), explicitly quantify the difference and its significance (e.g., two‑sample z with counts), and reconcile with the earlier discussion in Sec. VI D. If a different selection or weighting was intended in Sec. XI, state it precisely and provide the corresponding counts.

P5-E2
- Location: Sec. II, p.2 (Relation to Paper IV; “whose uncertainty is propagated explicitly below”), Sec. V, p.4–5 (statistical methods), Sec. VIII F, p.12–13 (monopole subtraction)
- Problem: The paper states the Paper IV catalog monopole uncertainty is “propagated explicitly below,” but no propagation is actually performed. All comparisons to σpred fix ΔfCW = −0.0026 as exact, and the reported σvs-monopole residuals in Table X lack uncertainty ranges stemming from the ± uncertainty on the catalog mean (Paper IV quotes 0.4974 ± 0.000279).
- Required fix: Propagate the monopole uncertainty into σpred and σvs‑monopole for all places where these are used to draw inference (Secs. VI, VII, VIII F). For example, report σpred ± δσpred with δσpred = 2·δ(ΔfCW)·√N, and when concluding “no residual exceeds 1.15σ” include the additional uncertainty from ΔfCW in the comparison (or perform a small Bayesian posterior predictive check that marginalizes over ΔfCW). Update any significance statements that change when the monopole uncertainty is included.

P5-E3
- Location: Sec. VI A, p.5–6
- Problem: Incorrect σpred for the filament class. Text: “σpred(filament) ≈ −3.16 and σpred(cluster) ≈ −3.28.” Using Eq. (1) with ΔfCW = −0.0026 and Nfilament = 408,187 gives σpred = 2·(−0.0026)·√N = −0.0052·√408187 ≈ −3.32 (not −3.16). The cluster value −3.28 is consistent.
- Required fix: Correct the filament σpred value and any dependent textual claims.

P5-E4
- Location: Abstract (p.1), Sec. V A (p.4–5), Sec. VI E (p.8), Table V (p.8)
- Problem: Mixed inference frameworks presented side‑by‑side (Gaussian σ thresholds, Bonferroni bounds, and permutation p-values) without explicit “not directly comparable” caveats at the points of juxtaposition. Example in Abstract: “redshift (label‑shuffle p = 0.372), projected k = 5 NN density (|σ|max = 3.94 … below Bonferroni thresholds), and sky‑position (HEALPix scans … with label‑shuffle nulls p = 0.61/0.135/0.413).”
- Required fix: At each location where σ-based thresholds and permutation‑based p-values are discussed together, insert an explicit statement that the statistics come from different null procedures and are not directly comparable, or refactor the presentation to use a single unified test per analysis (preferably the permutation‑based LEE‑controlled test, since you already implement it). Ensure conclusions are based on one pre‑declared primary null framework per analysis.

P5-E5
- Location: Sec. VII A, p.9–10
- Problem: Ambiguous language about an “observed” 11.32σ in the Phase 2 sweep that is later described as “predicted, not measured.” Text: “The largest single‑cell |σfrom half| across the entire sweep is 11.32 (filament at Rs = 10, λth = 0, n = 3,696,152). This is … predicted, not measured … matches the observed −11.3 within order unity.”
- Required fix: Clarify that this 11.32 is an expectation (σpred) based on the catalog monopole and not an observed chirality statistic (since there are no CW labels for 3.7M spectroscopic objects). Remove the word “observed” and isolate σpred values from any statements about measured statistics in the same paragraph.

MAJOR

P5-M1
- Location: Sec. V B, p.5; Abstract; Conclusions
- Problem: Primary estimator chosen post‑hoc. The DESIVAST‑anchored analysis is designated “primary” after exploring multiple classifiers; no selection penalty is applied. This is a textbook forking‑paths risk.
- Required fix: Either (i) present a principled selection rule that would have designated DESIVAST as primary a priori (e.g., largest n and peer‑reviewed VAC), and explicitly restrict the main claims to that pre‑specified criterion; or (ii) apply a conservative multiplicity correction across the family of environment classifiers considered when elevating any one to “headline” status; or (iii) move the “primary” designation into a preregistered analysis plan (if available) and cite it. Also, reflect this in the Abstract/Conclusions so the headline claim is tied to the DESIVAST analysis specifically.

P5-M2
- Location: Sec. V A, p.4–5 (Eq. 2)
- Problem: The Bonferroni “max‑|σ|” threshold formula is stated without derivation or citation, and its exact two‑sidedness and mapping to erfc−1 are not specified. You then compare to empirical max‑stat nulls and say they agree within ~10% without showing numbers.
- Required fix: Provide a brief derivation or a standard reference for Eq. (2) as applied to max‑|Z| across K bins with two‑sided tests, and tabulate, for each multi‑bin scan, the empirical 95th percentile of the max‑|σ| under permutation alongside the analytic Bonferroni threshold used. Ensure the threshold matches the intended familywise error control.

P5-M3
- Location: Sec. VII, Table VI (p.8–10)
- Problem: The Phase‑2 “range of fCW across classes” is reported per cell without the corresponding per‑class sample sizes or uncertainties. Range depends strongly on the noisiest class (void and wall).
- Required fix: For each (Rs, λth) cell, provide the per‑class n (or at least the smallest and largest class n) and the 1σ binomial uncertainties so readers can interpret the 0.05–0.22 pp ranges relative to statistical floors. Alternatively, add a panel with the per‑cell, per‑class n.

P5-M4
- Location: Sec. VIII A, p.10–11
- Problem: Overinterpretation from n = 6. The “0/6 V‑Web ‘void’ spirals inside any DESIVAST hole” is used to reinforce a strong purity claim (“0% concordance”), but n is far too small to support any rate estimate.
- Required fix: Either remove the purity‑rate language based on n = 6 and keep this as an anecdotal illustration, or expand the overlap test using all low‑z matched spirals (not just those V‑Web‑labeled as void) to compute a proper confusion matrix with binomial confidence intervals. Since you later provide much stronger DESIVAST re‑projections, the n = 6 anecdote is not needed.

P5-M5
- Location: Sec. VIII B–C, p.11–12
- Problem: Void membership implementation for VoidFinder relies on “inside any hole sphere.” In VoidFinder, “interior” membership is defined by the union of maximal‑void hole interiors and, depending on implementation, additional geometry that can differ from a pure “any hole” test; similar concerns for watershed approximations.
- Required fix: Demonstrate (e.g., on a small controlled subset) that “inside any hole sphere” reproduces the published interior/zone memberships to within a stated tolerance, or restrict the primary void‑membership tests to the catalog‑native GALZONE/ZONEVOID flags (as you already do for V2). Clarify any approximations.

P5-M6
- Location: Sec. XIII (Limitations) and Sec. VII A (p.9–10)
- Problem: RSD treatment is qualitative. You give scalar displacement heuristics and a back‑of‑the‑envelope boundary‑crossing estimate (3–5% of cells) but do not propagate a bound on how much RSD uncertainty affects the per‑class fCW estimates at the claimed ∼0.2 pp level in filament/cluster.
- Required fix: Provide a quantitative upper bound on the impact of RSD on your per‑class fCW (e.g., by reclassifying after a simple redshift‑space perturbation consistent with σv and recomputing fCW, or by bootstrapping galaxies near class boundaries). Report the resulting additional systematic uncertainty (even a conservative bound) and reflect it in the sensitivity floor statements.

P5-M7
- Location: Sec. VI D(d), p.8
- Problem: Unrealistic p‑value precision: “χ2 = 4932, 3 d.o.f., p < 10−1000.” Double‑precision numerical routines cannot support such extreme p‑values reliably; the exact value is not informative beyond “astronomically small.”
- Required fix: Report p‑values in a numerically defensible range (e.g., p < 10−50), or report the log10‑p truncated at machine precision, and state the numerical method used to compute the tail.

MINOR

P5-N1
- Location: Abstract (p.1)
- Problem: Sensitivity floor phrasing: “catalog‑monopole offset of ∼0.2 pp.” Paper IV offset is ΔfCW ≈ −0.0026 = −0.26 pp.
- Required fix: Use 0.26 pp (or “≈0.26 pp”) for consistency; avoid implying finer precision than supported.

P5-N2
- Location: Table I, p.3
- Problem: Acceptance‑radius sensitivity band “≤ 4%” vs provided counts {2.34, 2.35, 2.37, 2.39, 2.44}×10^6 spans ~4.3% from min to max by the displayed numbers.
- Required fix: Either round the band to “≈4%” or recompute with more precise counts to justify “≤ 4%.”

P5-N3
- Location: Sec. IX A, p.13–16 (Tempel cross‑validation)
- Problem: Filament concordance stated as 0.026 pp, while displayed values 0.4980 vs 0.4982 differ by 0.020 pp at the shown precision.
- Required fix: Provide the precise values used (more decimals) or adjust the stated difference to 0.020 pp to match rounded displays.

P5-N4
- Location: Eq. (1), p.4
- Problem: Ambiguity in numerator/denominator from missing parentheses in “ΔfCW/0.5/√N.”
- Required fix: Write explicitly as σpred = (ΔfCW / 0.5) / √N = 2 ΔfCW √N.

P5-N5
- Location: Sec. IX B, p.15
- Problem: Units inconsistency: T‑Web volume uses “800 Mpc cube” while most quantities elsewhere are in Mpc/h.
- Required fix: State explicitly whether this is 800 Mpc or 800 Mpc/h and, if mixing units, note the conversion or that only relative fractions are compared.

P5-N6
- Location: Sec. X, Table XII (p.16–17)
- Problem: The V‑Web “max |σ|” on the EDR overlap is quoted as 2.68; since this is a restricted sample, readers benefit from seeing class‑wise n as well.
- Required fix: Add per‑class n for the overlap to Table XII (or in a footnote).

P5-N7
- Location: Throughout
- Problem: Occasional use of internal campaign code “P5” and references to “Paper IV” that is not yet peer‑reviewed in places that could be read as external validation.
- Required fix: Keep “P5” internal tag usage minimal and consistently remind readers that Paper IV is an external input with its own uncertainty, not a peer‑reviewed prior.

NITS

P5-T1
- Location: Fig. 3 (p.7)
- Observation: Axes are clear; consider labeling the right‑panel y‑axis explicitly as “σfrom half” to match the notation.

P5-T2
- Location: Sec. VIII E, Table IX (p.12)
- Observation: Good to state explicitly that “0 maximal voids per pixel” corresponds to outside DESIVAST coverage (not simply “void‑poor” sky), which you explain in text; mirror this in the caption for self‑containment.

P5-T3
- Location: Bibliography
- Observation: Check capitalization/accents in author names (e.g., Rincón) for consistency with journal style.

Length and focus
For a negative result, 20 pages are on the long side. Much of Secs. IX–X and parts of VII could be streamlined without loss of scientific content. A 12–14 page main text (plus ancillary material in a data repository) would improve clarity.

Audit of key numbers (spot checks)
- Table II σfrom half recompute correctly from counts (void −0.68, wall +0.55, filament −2.61, cluster −4.66).
- Abstract class fractions and n agree with Table II.
- Range across classes 1.98 pp = 0.5034 − 0.4836.
- Density quintiles: |σ|max = 3.94; σpred per quintile at N ≈ 158,327 is 2·0.0026·√N ≈ 2.07; residual 1.87 (Table III) consistent.
- HEALPix p‑values in Table V match abstract within rounding.
- DESIVAST void vs non‑void: ΔfCW = 0.0007 (Table VII) consistent; σ magnitudes scale with √N as stated.
- Table X σvs‑monopole recompute from f − fP5 and N; values consistent within rounding.

## Summary recommendation
MAJOR REVISIONS

The core negative result appears sound and many computations check out, but the paper in its current form fails PRD methodological rigor on several points: an internal contradiction in the systematics section, lack of propagation of the monopole uncertainty despite promising it, an incorrect σpred value for a load‑bearing comparison, post‑hoc designation of the primary analysis without a selection penalty, and inconsistent presentation of heterogeneous test statistics without explicit caveats. Addressing the ESSENTIAL and MAJOR items above, with corrected numbers and clarified methodology, will likely suffice to bring the paper to PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass)

ESSENTIAL

P5-E6
- Location: Sec. VI D(c), p.7; Sec. VI D(b), p.7; Table II, p.5; Sec. VI D(d), p.8
- Problem: Inconsistent filament bright/dark sample sizes. You state filament bright n = 416,701 and filament dark n = 21,203, which sum to 437,904 > the total filament-class chirality-relevant count n = 408,187 (Table II). This also conflicts with the earlier full-catalog program totals (bright n = 775,760; dark n = 14,782). The filament dark count (21,203) exceeds the total dark count across all classes (14,782), which is impossible if these are the same selection.
- Required fix: Recompute and report the correct filament bright/dark n, and ensure all per-class-by-program Ns are consistent with the global program totals for the same selection and filtering. Update the quoted σ values, the |z| ≈ 3.4σ two-sample test, and any text that depends on these Ns.

P5-E7
- Location: Abstract (p.1), Phase‑2 sensitivity sentence
- Problem: Unit inconsistency. You write “never exceeds 0.22 percentage points (max 0.0022 at Rs = 25, λth = 0.3)”. 0.0022 is 0.22 percentage points as a fraction; mixing “pp” and fractional units is confusing and reads as a 100× discrepancy.
- Required fix: Use one unit consistently. E.g., “0.22 percentage points (0.0022 in fractional units)” or just “0.22 percentage points.”

P5-E8
- Location: Sec. VII A, p.9–10 (Phase‑2)
- Problem: Numerical mismatch for the quoted 11.32 “σ”. Using your own formula σpred = 2·ΔfCW·√N with ΔfCW = −0.0026 and the stated N = 3,696,152 gives σpred ≈ −10.0, not −11.32. Even using ΔfCW = −0.0028 gives ≈ −10.75. The stated magnitude is inconsistent with the inputs.
- Required fix: Correct the value and explicitly label it as σpred (not observed), with the ΔfCW and N used. If a different N was intended (e.g., a different cell or class population), report it.

MAJOR

P5-M8
- Location: Sec. VII A, p.10 (Bonferroni-9 threshold)
- Problem: Miscomputed Bonferroni familywise threshold. You state the Bonferroni-9 (α = 0.05) threshold is |σ| ≈ 3.02. For two-sided control across K independent Zs, zBonf = Φ−1(1 − α/(2K)). With K = 9 and α = 0.05, zBonf ≈ Φ−1(1 − 0.05/18) ≈ 2.77, not 3.02.
- Required fix: Correct the threshold and confirm that conclusions (none exceed threshold) remain unchanged under the correct value. If you used a different definition, provide a derivation/citation and show numeric agreement to a standard formula.

P5-M9
- Location: Sec. VI E (Table V, “npix”), Fig. 4 caption (“npix = 3,303”), Sec. VIII F (per-pixel moments: “1,821 valid pixels”), Sec. VIII E (NSIDE = 16: “297 occupied pixels”)
- Problem: Inconsistent definitions/cuts for “valid” pixels and resulting pixel counts across sections and figures. The number of analyzed pixels at NSIDE = 32 appears as 3,303 (Fig. 4), 1,821 (Sec. VIII F), and 1,496 (Fig. 6 bottom, with ≥200 spirals), with different or unstated minimum-count criteria.
- Required fix: Standardize and state the per-pixel spiral-count threshold(s) used for each analysis, and reconcile the reported pixel counts in captions and text. A small summary table (NSIDE, spiral-count cut, npix) would resolve this.

P5-M10
- Location: Sec. VI D(b)–(d), p.7–8 (two‑sample z on bright vs dark)
- Problem: The bright/dark two-sample z‑test is presented without adjusting for the documented dependence between V‑Web class and target program (Sec. VI D(d), χ2 p ≪ 10−50) and without controlling for covariates (z, density, leg). As written, the test can be confounded by program–class mixing.
- Required fix: Reanalyze the bright/dark contrast using a regression framework (e.g., logistic regression of CW on program with controls for class, redshift, density, leg, and their interactions), or stratified tests within homogeneous strata, and report adjusted effect sizes with uncertainties. Make clear which result (unadjusted vs adjusted) you rely on in the discussion.

MINOR

P5-N8
- Location: Sec. VI B, p.6 (logistic regression)
- Problem: Coefficients reported without uncertainties. You state “z-coefficient of 0.0059 with no significant intercept (0.000652)” but provide no standard errors or CIs.
- Required fix: Report coefficient ± SE (or CI), test statistics, and model specification (link, covariates, sample size, goodness-of-fit).

P5-N9
- Location: Sec. III C–D, Table I caption/context
- Problem: “1.0″ (DESI fiber positioning tolerance)” is inaccurate; 1″ is an astrometric cross-match tolerance, not a fiber positioning tolerance.
- Required fix: Rephrase to “astrometric matching tolerance” (or cite the astrometric precision motivating 1″), and remove “fiber positioning.”

P5-N10
- Location: Throughout (e.g., Sec. IV A, steps 4, 11; captions)
- Problem: Ambiguous notation “2563” for grid size; can be misread as 2,563 instead of 256^3.
- Required fix: Use 256^3 consistently for clarity.

P5-N11
- Location: Sec. VII, first paragraph
- Problem: Typo in sweep description: “Ngrid = 256 × λth ∈ {0.0, 0.1, 0.3}.” Ngrid should not depend on λth.
- Required fix: Correct to “Ngrid = 256^3; λth ∈ {0.0, 0.1, 0.3}.”

P5-N12
- Location: Sec. V, p.4–5; figure captions
- Problem: Mixed terminology for intervals: “exact binomial 95% credible interval” vs “95% Jeffreys binomial credible interval.” “Exact credible” is contradictory and Jeffreys is an approximate Bayesian interval with Beta(1/2,1/2) prior.
- Required fix: Standardize to “95% Jeffreys credible intervals (Beta(1/2,1/2))” or “Clopper–Pearson 95% confidence intervals” if you use exact frequentist, and be consistent.

P5-N13
- Location: Sec. V A, Eq. (2); Table V; Sec. VI E text
- Problem: Permutation p-values (empirical max-stat) are reported, but the Monte Carlo sampling uncertainty from NMC = 1000 is not quantified (typical ± ~0.01–0.02 at p ≈ 0.1–0.6). Several conclusions phrase these p-values as precise.
- Required fix: Quote p-values with an uncertainty or at least a resolution bound (e.g., “p = 0.135 ± 0.011, NMC = 1000”) and indicate the seed already listed in the checklist.

P5-N14
- Location: Sec. V, p.4–5
- Problem: You define both a label-shuffle and a position-shuffle null, but results are presented almost exclusively for the label-shuffle, while some text implies both are “primary.”
- Required fix: For each analysis, state explicitly which null was used for inference, and either present both or justify the choice of one.

P5-N15
- Location: Sec. IV A, step 8–9 (Poisson and tidal tensor)
- Problem: Dimensional normalization is not stated. Φ(k) = −δk/k^2 omits the conventional factors (4πG ρ̄ a^2, growth normalization) used to obtain a physically normalized potential; for a classifier this may be fine, but readers cannot infer the exact normalization of λi.
- Required fix: Add a sentence that you work in dimensionless units with δ normalized to unity variance and that overall multiplicative factors in Φ(k) cancel in the eigenvalue sign test, or provide the exact normalization used.

P5-N16
- Location: Sec. VII A, “Counting-statistics floor” bullet
- Problem: The quoted 1σ floors (e.g., ~0.08 pp for n ~ 4×10^5) are correct, but no numeric link is shown to the reported per-cell ranges in Table VI for each cell.
- Required fix: Add a compact per-cell mini-table or figure panel showing the smallest and largest per-class n for each cell so readers can compare the 0.05–0.22 pp ranges to the relevant statistical floors.

P5-N17
- Location: Sec. XI (Systematics bullets)
- Problem: Footprint split (“N/S/DES-only”) claims “within ±0.002 of global” without counts or CIs.
- Required fix: Provide the per-footprint n and fCW ± CI, or move to supplement.

NITS

P5-T4
- Location: Fig. 5 caption (Phase‑2 heat‑map)
- Observation: Clarify the colorbar unit explicitly as “percentage points” to match Table VI.

P5-T5
- Location: Sec. VIII B, first paragraph
- Observation: “k = 20 KDTree … sufficient given the 24 Mpc/h maximum hole radius” — briefly note the nearest‑center distance distribution (e.g., 99th‑percentile) or add a pointer to a check in the repository to justify k = 20.

Explanation for why these are new
The issues above were not covered in the initial review. They arise from a second, line-by-line audit focusing on arithmetic cross‑checks (notably the filament bright/dark counts and the 11.32σ discrepancy), unit/notation consistency (pp vs fraction; 256^3; Ngrid typo), comparability and configuration consistency across pixel‑level analyses, and completeness/robustness of the bright/dark contrast methodology. These items materially improve the paper’s rigor and clarity and align with PRD expectations.