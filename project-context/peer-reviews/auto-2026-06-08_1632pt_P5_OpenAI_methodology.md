# P5 auto-2026-06-08_1632pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9167 chars)
**Wall time**: 321.5s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test ...”

Scope of review
I reviewed the full 20-page manuscript, including all figures, tables, equations, and the abstract, as a methodology/statistics referee. I recomputed every quoted percentage, sigma, and key ratio from the numbers presented; checked dimensional/logic consistency of the main equations; examined the null-procedure usage and multiple-testing controls; and cross-checked whether every scalar in the abstract is traceable to the body text.

Overall assessment
The paper presents an ambitious cross-match between a large chirality catalog and DESI DR1, using multiple environment classifiers, with a stated primary analysis based on the DESIVAST void catalogs and secondary V-Web/T-Web/ASTRA/FoF consistency checks. The broad statistical framework (binomial z statistics, permutation max-stat LEE corrections, Bonferroni cross-checks) is sound in concept. However, there are several essential internal-consistency errors and presentation/traceability problems that preclude publication at PRD’s methodological rigor standard without substantial revision.

Findings

ESSENTIAL

P5-E1 (Section IV–VI, pp. 5–6; Figure 2 caption; Table II; Abstract)
Problem: Sample-size inconsistency between text/captions and the per-class counts. The abstract and Figure 2 caption state the canonical V-Web per-class results are “on the 791,635 chirality-relevant spirals,” but the class counts in Table II (void 428; wall 6,673; filament 408,187; cluster 397,505) sum to 812,793, not 791,635. Later (§VIII F, p. 12–13) you acknowledge 812,793 env-labeled spirals as a superset under a relaxed env-label filter, but this is not consistently stated where the per-class results are presented (caption and abstract).
Required fix: Reconcile and standardize the dataset definitions across the paper. If Table II/Fig. 2 use the 812,793 superset, say so explicitly in the caption and in the abstract where those numbers are quoted; alternatively, recompute per-class numbers on the 791,635 set and update all dependent statistics. Propagate the correction consistently through the abstract, §VI A text, Fig. 2 caption, and any other place these numbers are referenced.

P5-E2 (Section V, p. 4; Eq. (1))
Problem: Ambiguous/incorrect algebra in the definition of σpred. The equation is typeset as “σpred = ΔfCW / 0.5 / √N = 2 · ΔfCW · √N”. As written, ΔfCW / 0.5 / √N equals 2 ΔfCW / √N, not 2 ΔfCW √N. The intended formula is ΔfCW divided by the standard error 0.5/√N.
Required fix: Add parentheses to make the definition unambiguous and correct: σpred = ΔfCW / (0.5/√N) = 2 ΔfCW √N.

P5-E3 (Section VII, p. 8–10)
Problem: “Largest single-cell |σfrom half| across the entire sweep is 11.32 (filament at Rs = 10, λth = 0, n = 3,696,152). This is … predicted, not measured … matches the observed −11.3.” There are two severe issues: (i) n = 3,696,152 far exceeds the total number of chirality-labeled matched spirals and appears to be a count from the full DESI spectroscopic parent, for which CW/CCW labels do not exist. σfrom half cannot be “observed” on such a sample. (ii) The paragraph conflates a “predicted” value with an “observed” σ in the same sentence.
Required fix: Clarify precisely which population n refers to in the sweep (it must be the chirality-labeled matched sample, otherwise σfrom half is undefined). If this was a theoretical σpred based on an assumed Δf and a class size estimated from the matched-spiral subset, present it strictly as a prediction and remove the word “observed.” If it was inadvertently computed on the full DESI spectro sample, remove the claim. Provide the correct maximum observed |σ| across the nine cells computed on the chirality-labeled sample, or drop this sentence.

P5-E4 (Section XI, p. 17; vs. Section VI D b, p. 7)
Problem: Direct contradiction on the bright vs dark target-class split. Section VI D b reports catalog-level fCW for programs: bright 0.4970; dark 0.5051; backup 0.5143; other 0.4954, and further reports a bright-vs-dark difference at ≈3.4σ within filament. In Section XI you state: “target-class split (BGS vs. LRG-ELG-QSO) with BGS-only CW fraction within ±0.001 of LRG-ELG-QSO.” The earlier reported difference between bright and dark is ≈0.0081 at the catalog level, not ±0.001.
Required fix: Correct Section XI to reflect the actual measured bright vs dark differences reported earlier, or specify exactly what subset/statistic was used in the Section XI test (e.g., after monopole subtraction and/or in a specific environment), and provide the corresponding numbers. Ensure the statement is numerically consistent with §VI D b.

P5-E5 (Abstract; Sections VI, VIII F)
Problem: Abstract states “Per-class CW fractions on the 791,635 chirality-relevant spirals are, in order … filament n= 408,187 … cluster n= 397,505 …” These n values (and the derived σ) correspond to the 812,793 superset, not 791,635.
Required fix: Align the abstract text with the corrected dataset definition per P5-E1. If the per-class n are from 812,793, state that explicitly; otherwise recompute.

P5-E6 (Data/code availability; multiple sections)
Problem: The paper repeatedly references a “companion data repository” and “analysis drivers,” but no URL/DOI is provided anywhere in the manuscript, preventing reproducibility/audit of the custom pipelines and the permutation tests.
Required fix: Provide persistent links (DOI, public repository URL) to the exact code and data snapshots used to produce the results, including configuration files and random seeds, as stated in the reproducibility checklist.

P5-E7 (Dependence on unpublished Paper IV; multiple sections incl. Abstract, §§I–II, V, VI, VIII F)
Problem: The interpretation of significance repeatedly relies on the Paper IV catalog-wide monopole offset ΔfCW = −0.0026 from an unpublished “companion work.” While you do partially re-establish the monopole on the matched sample (fP5_CW ≈ 0.4972), many quantitative interpretations (e.g., σpred overlays, density-quintile predictions in Fig. 3, Abstract claims) are explicitly tied to the Paper IV monopole.
Required fix: Either (a) provide an arXiv reference for Paper IV so the input is citable and verifiable; or (b) reframe every point that currently uses the Paper IV monopole to use the monopole measured within this paper on the matched sample (fP5_CW), and remove reliance on unpublished external values. Update the abstract to reference the fP5_CW value actually measured here when discussing the “sensitivity floor.”

P5-E8 (Table V, p. 8; Figure 4 caption, p. 9; Figure 6 caption, p. 14)
Problem: Ambiguity/inconsistency in the number of HEALPix pixels used in different tests. Table V lists npix = 1,054 (NSIDE 16), 3,303 (NSIDE 32), 7,208 (NSIDE 64) without specifying the occupancy criterion. Figure 4 caption for NSIDE=32 also reports npix=3,303, while Figure 6 (NSIDE=32) reports “885 occupied pixels” (top) and “1,496 valid pixels” (bottom), and the text (§VIII F) says “1,821 valid pixels” elsewhere. These are likely different selection cuts (occupied, ≥1 galaxy; ≥200 spirals; “both voids and ≥200 spirals,” etc.) but are not defined consistently.
Required fix: For each HEALPix analysis, state explicitly the criterion used to include a pixel (e.g., ≥1 spiral; ≥200 spirals; both ≥1 DESIVAST maximal void and ≥200 spirals), and ensure Table V and figure captions/legends specify those criteria. Harmonize the counts across the text or explain why they differ (different analyses, different cuts).

P5-E9 (Terminology, Section IV A and footnote a, pp. 3–4)
Problem: The algorithm is repeatedly called “V-Web,” but by your own footnote you are using the tidal tensor from the density field (T-Web-style; Hahn et al. 2007) and not the velocity shear (Hoffman et al. 2012 V-Web). The persistent use of “V-Web” for a T-Web-style classifier risks confusion when comparing to the literature and to your own “T-Web concurrent-literature overlay” (§IX B).
Required fix: Either rename your canonical classifier throughout to “T-Web (tidal tensor on density field)” or insert a clear, prominent statement early in §IV that all uses of “V-Web” in this paper mean the tidal-tensor/density variant (sometimes called “T-Web”) and that no velocity reconstruction is performed. Ensure the abstract/figures/tables adopt consistent nomenclature.

P5-E10 (Section IX A, p. 15; “0.2 pp spec”)
Problem: The “0.2 pp concordance spec” used to judge agreement between classifiers appears ad hoc with no justification for that tolerance level.
Required fix: Provide a quantitative justification for the 0.2 pp tolerance (e.g., expected statistical fluctuation at the given N; derived from binomial standard errors; power calculations), or drop the “spec” language and present raw differences with their uncertainties.

MAJOR

P5-M1 (Null-procedure comparability; multiple sections)
Problem: Different test statistics and null procedures are presented side-by-side (e.g., σfrom half vs σpred from the monopole model; per-bin Bonferroni thresholds vs empirical max-stat permutation pLEE; per-class σ vs monopole residuals) without consistently reminding the reader that these are not directly comparable significance measures in a strict statistical sense. While individual sections do explain what is plotted/tested, juxtaposed σ and p-values can be misleading without explicit caveats.
Required fix: When comparing observed σfrom half to σpred or to Bonferroni thresholds, add an explicit statement that these are different diagnostics (point estimate deviations vs. null-calibrated exceedance probabilities) and are not directly comparable as p-values. Where magnitudes are contrasted (e.g., “within 1σ of σpred”), clarify the interpretive status (model-check rather than hypothesis test).

P5-M2 (Extremely small p-value reporting; Section VI A–D, §VI D d, p. 7–8)
Problem: The contingency-test p-value is given as “p < 10−1000,” which is not meaningful to report and depends on floating-point underflow or asymptotic approximations.
Required fix: Report an interpretable bound (e.g., p < 1e−50) or the exact test-statistic with a clear statement that the p-value is effectively zero at double precision. Provide the χ2 value, degrees of freedom (already present), and effect size (e.g., maximum absolute deviation in bright fraction, already present) and drop the “10−1000” claim.

P5-M3 (Section VIII A–C, pp. 10–12)
Problem: The DESIVAST-based cross-checks are methodologically strong, but several computational details that bear on reproducibility/validity are underspecified (e.g., k=20 KDTree justification only via “sufficient”; comoving conversion details, mask/edge handling for sphere membership, handling of overlapping holes vs maximal voids; how effective radii were applied consistently across algorithms).
Required fix: Expand the methods appendix or §VIII to specify: coordinate conventions (exact cosmology, unit conversions, whether holes near the survey edge were excluded), how overlapping spheres were handled when labeling a galaxy as void/non-void, how the V2-REVOLVER/VIDE “effective radius” spheres were constructed from the catalogs (cite exact columns, units), and sensitivity of results to the KDTree k parameter (show that k=20 cannot miss any hole within the maximum hole radius at the relevant densities).

P5-M4 (Section X, p. 16–17)
Problem: For the ASTRA EDR cross-check, Table XII reports only “range” and “max |σ|,” not the per-class n or fCW. Given the strong per-galaxy classifier disagreement reported, readers need to see the actual class sizes and CW fractions under the ASTRA argmax and entropy-weighted schemes to assess precision and comparability.
Required fix: Add a table (or expand Table XII) listing per-class n and fCW (with 95% intervals) for the ASTRA argmax and entropy-weighted classifiers on the overlap. State the number of objects contributing to each class under the entropy-weighted scheme (sum of Pclass over galaxies).

P5-M5 (Section VII A, p. 9–10)
Problem: The “counting-statistics floor” is correctly identified, but the concluding claim that “zero of the nine sweep cells produces a per-class |σvs monopole| above the Bonferroni-9 threshold” is stated without showing the per-cell residuals (you only present the per-cell max-range). Given the earlier confusion in P5-E3, readers need to see at least a summary table of the worst residual per cell on the matched-spiral sample.
Required fix: Provide a compact table (9 rows) with, for each (Rs, λth), the per-class n, observed σfrom half, σpred (from fP5_CW), and σvs monopole residuals for the worst environment class. Alternatively provide these as supplemental CSV with a summary row in the main text.

MINOR

P5-m1 (Section IV B, p. 4; Figure 1)
Problem: The pie-chart is qualitative; the caption should explicitly note “in-footprint” fractions are conditional on the constructed mask (3,150,086 in-mask cells), to avoid misinterpretation as all-sky fractions.
Required fix: Amend the caption to state “volume fractions within the constructed in-footprint mask.”

P5-m2 (Section VI A, p. 5–6)
Problem: The void-bin Jeffreys interval is quoted as [0.435, 0.530] without specifying that it is Jeffreys (you later mention Jeffreys for Fig. 2 but not at the first mention).
Required fix: Add “(95% Jeffreys interval)” at first mention.

P5-m3 (Section VIII E, p. 12)
Problem: The HEALPix stratification bins (“0, 1–2, 3–5, 6+ maximal voids per pixel”) would benefit from reporting per-bin sky area fractions or pixel counts alongside n.
Required fix: Add the number of pixels (and optionally area fractions) per bin.

P5-m4 (References, p. 20)
Problem: Some references are to in-preparation/preprint works ([3], [11], [12]). This is acceptable, but please ensure that arXiv identifiers are provided (they are for [11], [12]; add for [3] if available) and that the citations are up to date at acceptance.

NIT

P5-n1 (Throughout)
Problem: Occasional over-precise significant figures for p-values and σ in prose (e.g., “p = 0.607,” “σ = −0.37” when the context would be clear with fewer decimals).
Required fix: Round to a consistent significant-figure policy (e.g., two decimals for σ, two or three significant digits for p).

P5-n2 (Section titles/wording)
Problem: The phrase “Primary vs. secondary analysis paths (pre-registration caveat)” is long and could be tightened.
Required fix: Consider “Primary analysis and multiplicity control” and place the pre-registration note as a paragraph.

P5-n3 (Typography)
Problem: A few en/em dashes and hyphenations are inconsistent.
Required fix: Normalize to journal style.

Arithmetic cross-check summary
- Table I: Counts and fractions consistent; fCW = 393,592/791,635 = 0.49719 (later used as fP5_CW).
- Table II: fCW and σ recompute correctly for each class. The summed n=812,793 conflicts with “791,635” claims (P5-E1).
- Density-quintiles (Table III): σpred ≈ 2 × 0.0026 × √158,327 ≈ 2.07; residuals match.
- DESIVAST VoidFinder (Table VII): fvoid = 0.4964 → σ ≈ −1.71; non-void 0.4971 → σ ≈ −4.59; ∆f = 0.0007; all consistent.
- Three-algorithm DESIVAST (Table VIII): |∆f| < 0.002 across algorithms; σ values consistent with N.
- HEALPix p-values (Table V): match text (0.607/0.135/0.413; abstract rounds 0.61).
- σvs monopole residuals (Table X): recompute to within rounding.
- Bright vs dark difference: Using the reported σ and N, the difference in f is ≈1.2 pp; the two-sample z ≈ 3.4, consistent with text.

Dimensional/logical checks
- Grid size/box length implies 25.9 h−1 Mpc cell size (6634/256), consistent.
- Counting-statistics floors 1/(2√n) convert to pp as stated (0.08 pp at n ~ 4×10^5, etc.).
- RSD displacement heuristic σv/(aH) ~ 5–8 h−1 Mpc is plausible at z < 0.3, but not used quantitatively in tests (fine as a caveat).

Length and focus
For the claimed contribution (an environment-dependence null, with DESIVAST as primary and V-Web as secondary diagnostics), 20 pages is borderline long. With the required corrections, I recommend focusing the main text on:
- A concise, consistent presentation of the matched sample(s);
- The DESIVAST primary analysis and its three-algorithm robustness;
- One or two key secondary checks (e.g., density- and sky-position nulls);
and moving much of the V-Web hyperparameter sweep detail to supplemental material. A target of 14–16 pages would suffice without loss of clarity.

## Summary recommendation
MAJOR REVISIONS

The manuscript contains multiple essential internal-consistency errors (most importantly, the dataset-size mismatch in the canonical V-Web result and the ambiguous/incorrect σpred formula), a conflation of predicted vs observed σ in the sweep section using an n that cannot apply to the chirality-labeled sample, and a direct contradiction on the target-program split. In addition, the dependence on an unpublished companion paper for a load-bearing monopole value should be eliminated by anchoring all interpretations to values measured within this manuscript or by citing an arXiv preprint. With these issues corrected, and with clearer, consistently defined sample subsets and pixel counts, the statistical framework appears capable of supporting the stated conclusion.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P5-E11 (Section VIII, pp. 10–12; internal DESIVAST counts inconsistent)
- Problem: Conflicting counts for the DESIVAST watershed catalogs. Early in §VIII you write “420 with V2-REVOLVER, and 295 with V2-VIDE,” but later in §VIII C you state “V2-REVOLVER ncatalog void = 1,992” and “V2-VIDE ncatalog void = 1,478.” These cannot both be correct without a clear distinction (e.g., “interior voids” vs “effective voids,” or “maximal” vs “all”). As written, readers cannot tell which catalog cardinalities were actually used.
- Required fix: Reconcile and precisely define each count (interior holes, maximal voids, effective voids, zones). Cite the exact DESIVAST HDUs/columns and the selection used for each algorithm. Update numbers everywhere for consistency.

P5-E12 (Section VI A, p. 6; void-bin explanation)
- Problem: Logical mismatch in the “Void-bin smallness” paragraph. It states the small nvoid arises because “The small cluster volume fraction of 1% plus the sparse r ≤ 17.8 … yields a small chirality-relevant void sample.” The cluster volume fraction has no bearing on why the void class is under-populated. This appears to be a copy/paste mistake (“cluster” should not be invoked to explain void scarcity).
- Required fix: Correct the explanation. If the intended point is that voids are underdense and the matched spiral catalog is flux-limited, state that directly (and, if possible, quantify the expected suppression).

P5-E13 (Section VIII B–C, pp. 11–12; KDTree k-NN membership can miss true members)
- Problem: The point-in-sphere membership test uses a fixed k-nearest-neighbour (k=20) KDTree search on void centers, justified by “sufficient given the 24 Mpc/h maximum hole radius.” This approach is unsafe in general: a sphere with a large radius whose center lies farther than the k-th nearest center can still contain the galaxy, so k-NN does not guarantee completeness unless k is chosen adaptively or a radius (ball) query is used. The risk is amplified because later you cite larger maximum effective radii for watershed voids (43.5, 55.9 Mpc/h), and even for maximal VoidFinder voids you note 10–32 Mpc/h radii (§VIII E).
- Required fix: Replace the fixed-k nearest-neighbour query with a radius/ball query using the true per-algorithm maximum effective radius, or prove (with distance-to-20th-centre distributions) that k=20 guarantees coverage for all points. Re-run the membership if needed and report sensitivity of nvoid and ΔfCW to this correction.

P5-E14 (Section VIII F, p. 13; definition of σ vs monopole)
- Problem: The σvs monopole residuals appear to be computed by re-using the 0.5/√N standard error (the “σ-from-half” denominator) after subtracting fP5_CW. If the null mean is fP5_CW ≠ 0.5, the correct standard error is √[fP5(1−fP5)]/√N, not 0.5/√N. Using 0.5/√N biases the reported “|σvs monopole| < 1.15” comparisons slightly.
- Required fix: Recompute σvs monopole with the correct standard error for p = fP5_CW in each bin, and update the quoted residuals and any thresholds that depend on them.

P5-E15 (Section VIII A–E, pp. 10–12; inconsistent maximum-radius statements)
- Problem: You justify k=20 using a “24 Mpc/h maximum hole radius” (VoidFinder), but later report DESIVAST maximal void radii of 10–32 Mpc/h and watershed maximum effective radii of 43.5–55.9 Mpc/h. The stated “maximum radius” used for completeness is not aligned with the larger effective radii reported elsewhere, and it is not cited to a catalog column.
- Required fix: State and cite the true per-algorithm maxima (by reading the catalog columns used) and ensure the membership search radius accounts for the largest relevant effective radius. If different for VoidFinder vs REVOLVER/VIDE, say so explicitly and use correct values in each test.

P5-E16 (Cross-reference error; §VIII “RSD treatment for DESIVAST,” p. 10)
- Problem: The sentence “This is in contrast to the V-Web secondary path (§XIII)” mis-references §XIII (Limitations) instead of the V-Web methods/results (§IV/§VI).
- Required fix: Correct the section reference.

MAJOR

P5-M6 (Section VI B, p. 6; logistic regression lacks uncertainty)
- Problem: You report a logistic-regression z-coefficient “0.0059 with no significant intercept (0.000652)” but provide no standard errors or p-values. The conclusion “consistent with no redshift dependence” is therefore unsupported quantitatively.
- Required fix: Report coefficient estimates with standard errors, z-scores, and p-values (or CIs). State the sample size used and model details (link, predictors, any interactions). If regularization was used, specify it.

P5-M7 (Section V vs Figures; “exact binomial” vs Jeffreys intervals)
- Problem: §V states you report “exact binomial 95% credible interval,” which conflates frequentist “exact” (Clopper–Pearson) with Bayesian Jeffreys intervals. Later captions explicitly say “Jeffreys binomial credible intervals.”
- Required fix: Standardize the terminology. If you use Jeffreys intervals everywhere, say “95% Jeffreys credible intervals” consistently and remove “exact.” If you mix intervals, state which is used where and why.

P5-M8 (Section IX A, p. 15; Tempel concordance against Paper IV mean)
- Problem: In Fig. 7/§IX A you compare the Tempel-class fCW to the Paper IV global mean line. For a fair concordance test, you should compare class fCW values between the two classifiers on the same matched overlap, or to the overlap’s own monopole, not to an external catalog-wide mean (especially one from an unpublished companion; see P5-E7 in your first report).
- Required fix: Report Δf between Tempel and V-Web on the overlap with uncertainties, and, if you include a “mean” line, use the overlap mean fCW with its CI.

P5-M9 (Section VII, pp. 8–10; λth normalization not specified)
- Problem: You sweep λth ∈ {0.0, 0.1, 0.3} but do not define the normalization of Φ and Tij that makes these dimensionless thresholds interpretable across implementations. While λth=0 is geometric, non-zero λth depends on the precise conventions used in your Poisson solve and tidal-tensor normalization.
- Required fix: State the normalization (e.g., Φ from δ via Poisson without 4πG factors, Tij = ∂i∂jΦ with units suppressed; any rescaling applied prior to thresholding). If these λth are purely relative within your pipeline, say so and caution readers against direct cross-paper comparisons.

P5-M10 (Section V XI “systematics,” p. 17; undefined variable)
- Problem: The “confidence-threshold sweep” mentions “pmax_cls_eq ∈ {0.4,…},” but this variable is never defined (is it the classifier softmax confidence for the equivariant label? a probability from Paper IV?).
- Required fix: Define the variable precisely and how it is computed, and specify which subset is filtered by it.

MINOR

P5-m5 (Figure 2 caption and §VI A wording)
- Problem: At first mention in §VI A, the void-bin interval is given without the “Jeffreys” qualifier (you add it later in the Fig. 2 caption).
- Required fix: Add “(95% Jeffreys interval)” at first mention to avoid confusion.

P5-m6 (Units/style; throughout)
- Problem: Mixed notation for comoving-length units (“Mpc/h” vs “h−1 Mpc”) and for grid size (“2563” vs “256^3”).
- Required fix: Standardize units and grid notation to journal style.

P5-m7 (Section VIII E, p. 12; HEALPix binning metadata)
- Problem: For the “0, 1–2, 3–5, 6+ maximal voids per pixel” stratification, only the galaxy counts and σ are provided; pixel counts or area fractions per bin are omitted.
- Required fix: Add the number of pixels (and optionally sky-area fraction) per bin to contextualize the n.

P5-m8 (Section VII A, p. 9; duplicated magnitudes)
- Problem: Abstract and text state “0.22 percentage points (0.0022)” redundantly.
- Required fix: Pick one representation or state “0.22 percentage points (pp).”

P5-m9 (Section IV A Step 12, p. 3; interpolation choice)
- Problem: You state “NN-interpolate the per-cell label + smoothed logdensity to each galaxy,” which is effectively nearest-cell assignment. This can matter at 25.9 Mpc/h cell size near class boundaries.
- Required fix: Clarify whether labels are assigned by nearest-cell, trilinear interpolation of eigenvalues with post-thresholding, or another scheme; note any tests of robustness to this choice.

NIT

P5-n4 (Precision/presentation; scattered)
- Problem: Rounding/precision could be tightened in logistic-regression coefficients and some p-values; “2563” typographic convenience appears several times.
- Required fix: Adopt a consistent rounding policy (two decimals for σ, two–three sig figs for p), and render 256^3 for clarity.

Explanation
These findings are new and non-overlapping with your initial review. They address additional arithmetic/logical mismatches (DESIVAST catalog cardinalities, void-bin explanation), a methodological correctness risk (fixed-k KDTree membership potentially missing true void members), a definition/denominator issue in σ vs monopole, a wrong internal cross-reference, missing uncertainty on regression, interval terminology, λth normalization, undefined variables, and several presentation/clarity points.