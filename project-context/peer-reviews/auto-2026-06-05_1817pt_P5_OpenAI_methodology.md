# P5 auto-2026-06-05_1817pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (10967 chars)
**Wall time**: 469.2s

---

Referee report for Physical Review D (methods/statistics focus)

Title: Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals

General assessment
I read the entire manuscript, all tables and figure captions, and audited the arithmetic and statistics reported in the abstract and conclusions against the body. The topic is suitable for PRD’s cosmology/methods remit and the paper assembles a substantial amount of cross-survey infrastructure. However, there are multiple methodology and internal-consistency issues that must be resolved before the results can be relied upon. Several quantitative statements in the abstract and body either conflict with each other or lack the promised uncertainty propagation. There are also places where different “sigma” conventions are juxtaposed without sufficiently explicit definitions, and at least one place where the text contradicts itself on a key systematic (bright vs dark target programs). I list specific issues below.

Findings

ESSENTIAL

P5-E1
- Location: Sec. XI (Systematics and null tests), p. 17 vs. Sec. VI D(b), p. 7
- Problem: Direct contradiction on the BGS vs. LRG/ELG/QSO (bright vs dark) split. Sec. VI D(b) reports a large difference between bright and dark: fCW = 0.4970 (bright, n = 775,760) vs 0.5051 (dark, n = 14,782), Δ = 0.0081 (8.1 pp), with σ = −5.25 vs +1.25 and a claimed two-sample z ≈ 3.4σ for the filament class. Sec. XI then states: “target-class split (BGS vs. LRG-ELG-QSO) with BGS-only CW fraction within ±0.001 of LRG-ELG-QSO.” These statements are incompatible.
- Required fix: Recompute and report the bright vs dark global fCW split in the same sample used in Sec. XI and reconcile with the Sec. VI D(b) numbers. If Sec. XI refers to a different sample/conditioning (e.g., monopole-subtracted, environment-marginalized, or different quality cuts), state this explicitly, provide the exact n per bin, the exact fCW values with uncertainties, and correct the ±0.001 claim if erroneous. If the 3.4σ filament-class difference is retained, show the actual counts and the formula used for the two-sample test.

P5-E2
- Location: Sec. VII (Phase 2 sweep), p. 9–10
- Problem: Inconsistency on the “largest single-cell |σfrom half| across the sweep.” The text states: “largest single-cell |σfrom half| across the entire sweep is 11.32 (filament at Rs = 10, λth = 0, n = 3,696,152). This is the catalog-wide ∆fCW = −0.0026 monopole… predicted, not measured: σpred ≈ −10 matches the observed −11.3 within order unity.” This mixes “observed” and “predicted,” uses an n that is incompatible with the 791,635 chirality-relevant sample, and leaves unclear which dataset that 11.32σ was computed on.
- Required fix: Specify unambiguously whether the 11.32 is computed from observed chirality labels in the matched sample (and if so, provide the actual N and the fCW for that cell/class), or if it’s a theoretical projection from the Paper IV monopole. If it is not based on the chirality-relevant sample, remove it from the sweep summary or clearly separate it as a back-of-envelope prediction. Use consistent sample sizes throughout the sweep section and avoid “observed” for values that are not empirically measured.

P5-E3
- Location: Abstract; Sec. II; Sec. V (“we explicitly compare…”); Sec. VI A; Sec. VII A; Sec. VIII F
- Problem: The manuscript repeatedly leans on the Paper IV catalog monopole ∆fCW ≈ −0.0026 (“propagated explicitly below”) to interpret deviations and to set a “∼0.2 pp” sensitivity floor, but no explicit propagation of the Paper IV uncertainty into σpred or into the “systematic floor” is actually shown. You cannot claim that the monopole uncertainty is “propagated explicitly” if no numbers or error bars are propagated into the statistics used for interpretation (e.g., Fig. 3 right panel; Table X “σvs monopole”).
- Required fix: Provide the Paper IV uncertainty on ∆fCW and propagate it into: (i) uncertainty bands on σpred = 2 ∆fCW √N where used; (ii) the stated “∼0.2 pp” floor; (iii) any “σvs monopole” residuals used for conclusions. If Paper IV is not peer-reviewed, treat ∆fCW as an external parameter with uncertainty; show how the conclusions vary across its 1–2σ range.

P5-E4
- Location: Sec. VIII F (Table X and text), p. 12–13; also earlier references to “σfrom half”
- Problem: “σvs monopole” is used as a significance-like quantity but is not defined precisely. From the numbers it appears you are using σvs monopole = 2 (fCW − fP5) √N (same denominator as σfrom half). However, this is not the standard z-score for testing against p = fP5 (which would use √[N fP5 (1 − fP5)] in the denominator). As written, multiple “sigma-like” quantities appear in the paper (σfrom half, σpred, σvs monopole, two-sample z), and they are easy to confuse.
- Required fix: Add explicit definitions of every sigma-like statistic used (σfrom half, σpred, σvs monopole, two-sample z) and, wherever two different “sigmas” appear in the same paragraph/table/figure, state clearly that they are not directly comparable. For σvs monopole, either use the proper binomial variance with p = fP5 or clearly label it as a scaled residual in “σfrom half units” and avoid interpreting it as a formal p-value.

P5-E5
- Location: Sec. VI E (HEALPix scans) and Fig. 6; Sec. VIII F, p. 12–14; Table V, p. 8–9
- Problem: Inconsistent counts of “valid pixels” at NSIDE = 32. Table V quotes npix = 3,303 (apparently non-empty pixels), Fig. 6 top says 885 occupied pixels (maximal voids), Fig. 6 bottom says 1,496 valid pixels (≥ 200 spirals), while Sec. VIII F states “the distribution … across the 1,821 valid pixels.” These cannot all be correct without clear definitions.
- Required fix: Define npix consistently for each context (all-sky pixels; footprint pixels; pixels with any matched spirals; pixels with ≥ 200 spirals; pixels with ≥ 1 DESIVAST maximal void; intersection) and reconcile the contradictory counts. Update Table V and captions to make the selection criteria explicit.

MAJOR

P5-M1
- Location: Sec. VI A, p. 5–6
- Problem: Minor numerical mismatch for σpred(filament) from the Paper IV monopole. Using N = 408,187 and ∆f = −0.0026 gives σpred = 2 (−0.0026) √408,187 ≈ −3.32, not −3.16 as stated. The cluster value (−3.28) is correct for N = 397,505.
- Required fix: Correct σpred(filament) or explain the N used. If an alternative N was used (e.g., after an additional cut), state it.

P5-M2
- Location: Table V (HEALPix scan), p. 8
- Problem: “npix” is reported as 1,054 (NSIDE 16), 3,303 (NSIDE 32), 7,208 (NSIDE 64), which are not the total number of pixels at those NSIDE values (3,072; 12,288; 49,152). It appears you are counting only non-empty/footprint pixels, but this is not stated.
- Required fix: Clarify exactly what npix counts (e.g., number of pixels that contain at least one chirality-relevant galaxy) in the table caption and main text. If subsequent p-values rely on this npix (e.g., for Bonferroni), ensure the same definition is used consistently.

P5-M3
- Location: Sec. VII A (Per-cell significance framework), p. 9–10
- Problem: The sweep uses NMC = 1,000 permutations to define the empirical look-elsewhere max-stat p-values. That granularity is acceptable for p far from threshold, but the text asserts agreement “within ∼10% on all scans at α = 0.01” between the empirical LEE and Bonferroni. No quantitative comparison is shown; and with K up to thousands of pixels (Sec. VI E), NMC = 1,000 can be too coarse near the 5% family-wise threshold.
- Required fix: Provide, for at least one representative scan (e.g., NSIDE = 32), the empirical distribution of the max-|σ| under label-shuffle, the observed max-|σ|, and the resulting pLEE with its Monte Carlo uncertainty (~√[p(1−p)/NMC]). Alternatively, increase NMC to ≥10,000 for per-pixel scans to support sub-percent statements.

P5-M4
- Location: Sec. IX A (Tempel FoF cross-validation), p. 13–16
- Problem: The paper claims filament-class concordance at the 0.026 pp level. That’s consistent with the numbers presented, but you also conclude the Tempel “cluster like” differs by 0.66 pp from V-Web “cluster.” Given that the V-Web “cluster” class is defined at λth = 0 and Tempel’s multiplicity ≥ 20, these are not commensurate classes. The text has a caveat, but the figure suggests a direct visual comparison.
- Required fix: Strengthen the caveat in the caption and body: these classes are not directly comparable; the numerical differences at low-n bins should not be interpreted as environment-dependent chirality. Optionally, provide a contingency table of overlaps or a Jaccard index to quantify mapping quality.

P5-M5
- Location: Sec. VI D(d), p. 8
- Problem: “χ2 = 4932, 3 d.o.f., p < 10−1000.” Such extreme p-values are not meaningful to report numerically and suggest either over-precision or a formatting artifact. The χ2 value is plausible given the large N, but the p-value should be stated appropriately.
- Required fix: Replace with a bounded statement (e.g., p < 10−16) or compute the value using appropriate special functions with underflow-safe arithmetic and report to a sensible floor.

P5-M6
- Location: Multiple places (e.g., Sec. IV A, p. 3–4; Fig. 1 caption; Sec. VII line “Ngrid = 256 ×”)
- Problem: Inconsistent or incorrect notation for the grid size: “2563” appears repeatedly and “Ngrid = 256 × λth ∈ {…}” on p. 8; both should be “256^3,” and Ngrid should not be “× λth.”
- Required fix: Standardize to 256^3 and correct the stray “× λth” typo. Ensure all instances are fixed.

P5-M7
- Location: Sec. III B; Table I; Sec. III D
- Problem: You include SPECTYPE = QSO (17,180 matches) in the parent sample and possibly in the matched sample. It is unclear whether any QSOs survive into the chirality-relevant subset (CW/CCW), and whether including QSOs in the environment field estimation affects the results.
- Required fix: State explicitly whether QSOs enter the chirality-relevant sample and/or only the density field. If they enter the former, provide their count and justify that their inclusion does not bias chirality statistics (or exclude them). If they only enter the parent density field, state this clearly.

P5-M8
- Location: Sec. V (Statistical methods) and throughout where Jeffreys intervals are invoked
- Problem: You report Jeffreys 95% credible intervals but conduct significance testing via σfrom half (implicitly normal). This is fine, but please make clear the interval is Bayesian and the tests are frequentist to avoid misinterpretation.
- Required fix: One sentence clarifying the use of Bayesian intervals for visualization and frequentist tests for hypothesis testing.

P5-M9
- Location: Sec. VIII A–D (DESIVAST), p. 10–12
- Problem: “Companion data repository” is referenced repeatedly, but no URL/DOI is provided in the manuscript.
- Required fix: Provide a persistent link/DOI to the repository used to generate the figures/tables, or deposit the necessary CSVs/scripts as Supplemental Material.

MINOR

P5-n1
- Location: Abstract; Sec. VI A; Table II; Fig. 2
- Problem: All class-level fCW, σfrom half, and ranges were recomputed and are consistent. However, in Sec. VI A, σpred(filament) is slightly off (see P5-M1).
- Required fix: Correct σpred(filament) per P5-M1.

P5-n2
- Location: Sec. VI B (redshift dependence), p. 6
- Problem: Logistic regression includes a “confidence” covariate that is not defined in the text.
- Required fix: Define the “confidence” variable: origin, range, and how it is computed from the classifier outputs.

P5-n3
- Location: Sec. IX B (concurrent T-Web), p. 15
- Problem: The comparison of in-footprint volume fractions is necessarily approximate; the text notes this. Consider giving the exact V-Web fraction uncertainties (e.g., jackknife across sky regions) to support “approximate concordance.”
- Required fix: Optional: add uncertainties on V-Web volume fractions or a footnote that uncertainties are dominated by mask systematics rather than counting.

P5-n4
- Location: Throughout
- Problem: Units alternate between “Mpc/h” and “h−1 Mpc.”
- Required fix: Standardize to one convention and mention it once.

P5-n5
- Location: Sec. V B (Primary vs secondary), p. 5
- Problem: The post hoc declaration of the primary analysis is candid, but PRD readers would expect a more formal multiplicity treatment across all explored paths.
- Required fix: Add a brief statement quantifying the “garden of forking paths” risk beyond the DESIVAST Bonferroni-5 accounting (e.g., how many alternative classifiers/stratifications were inspected before choosing DESIVAST as primary), or explicitly restrict the headline claims to the DESIVAST block alone.

P5-n6
- Location: Fig. 3 caption
- Problem: The Bonferroni-5 threshold is plotted as dotted blue lines, but the underlying assumption of independence across density quintiles is only briefly mentioned earlier.
- Required fix: Add a note in the caption that Bonferroni is conservative here due to correlated bins.

P5-n7
- Location: Sec. VIII E; Table IX
- Problem: “0 maximal voids per pixel” is interpreted as “outside DESIVAST coverage.” This should be stated explicitly with a schematic of the footprint or a sentence confirming that 0-void pixels are outside the DESIVAST BGS area.
- Required fix: Clarify in text/caption.

NIT

P5-i1
- Location: Typos and formatting: “2563” vs “256^3”; “Ngrid = 256 × λth …”; occasional doubled spaces; a stray hyphenation artifact (“per￾cent”).
- Required fix: Copy edit.

P5-i2
- Location: Sec. XIII (Limitations), p. 17–18
- Problem: The scalar RSD displacement argument is fine as a heuristic; the text already notes it is insufficient. Consider moving some of this to an appendix or compressing.
- Required fix: Editorial.

P5-i3
- Location: Bibliography
- Problem: Check author list formatting for [13] (accents), and ensure arXiv IDs and years match the cited versions. The citation style is acceptable but please verify all metadata.

Length
At 20 pages, the manuscript is long for the core contribution (an environment-dependence null at DR1 resolution plus DESIVAST void cross-check). If the authors can compress sections VI D (many sub-stratifications) and XIII (RSD caveats) without loss of rigor, a target length of ~14–16 pages would improve readability.

Audit of abstract and conclusions
- All abstract class-level fCW and σ values match Table II within rounding.
- “Range across classes is 1.98 pp” matches 0.5034 − 0.4836.
- Phase 2 “max 0.22 pp” matches Table VI.
- HEALPix p-values (0.61/0.135/0.413) match Table V within rounding (0.607/0.135/0.413).
- DESIVAST-anchored re-projection: n = 56,981; fvoid = 0.4964; fnon-void = 0.4971; Δ = 0.0007: matches Table VII.
- “V2-REVOLVER catalog-native … σvoid = −0.24” matches Sec. VIII D.
- “Two-sample z-test … ≈ 3.4σ” is asserted but not supported with actual counts in the text; please add them (see P5-E1).
- “Propagated explicitly” for the Paper IV monopole uncertainty is claimed in the abstract but not actually done (P5-E3).

## Summary recommendation
MAJOR REVISIONS

The core result—a null detection of environment-dependent spiral chirality at DESI DR1 resolution with a robust DESIVAST void cross-check—is plausible and many numerics check out. However, several essential inconsistencies (notably the contradictory statements on bright vs dark target-program differences, the unclear “observed vs predicted” 11.3σ statement with inconsistent N, and the unfulfilled promise to propagate the Paper IV monopole uncertainty) must be corrected. Additional major clarifications around sigma definitions and HEALPix pixel accounting are required. Once these issues are addressed with precise definitions, reconciled numbers, and proper uncertainty propagation, the paper could be suitable for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS AFTER SECOND-PASS AUDIT

ESSENTIAL

P5-E6
- Location: Sec. V, Eq. (1)
- Problem: Algebraic inconsistency. The displayed identity reads σpred = ΔfCW/0.5/√N = 2·ΔfCW·√N. The left-hand expression equals 2ΔfCW/√N, not 2ΔfCW√N. As written, the two right-hand sides are not equal.
- Required fix: Correct Eq. (1) to σpred = 2ΔfCW√N, and remove the erroneous ΔfCW/0.5/√N term (or fix it if intended). Explicitly state the derivation from σfrom half = 2(f − 0.5)√N.

P5-E7
- Location: Sec. IV A (Algorithm, steps 1–12); throughout V-Web results
- Problem: The V-Web density field is built from a heterogeneous tracer mix (BGS, LRG, ELG, QSO) over 0.01 ≤ z ≤ 2.0 without any correction for the strong radial selection function or tracer-dependent n(z). You form δ = ρ/ρ̄ − 1 using a single global mean across the in-footprint mask. This induces a large artificial radial gradient in δ and can bias tidal eigenvalues and class boundaries. No random catalog, completeness weighting, or per-z renormalization is used.
- Required fix: Either (a) reconstruct the density field with an appropriate selection-function correction (e.g., randoms, per-tracer/per-z weights, or per-slice renormalization) and re-run V-Web; or (b) restrict the parent to a volume-limited, homogeneous sample (e.g., DESI BGS to a fixed z) and show the headline results are unchanged. At minimum, provide a quantitative test (e.g., compare class fractions and fCW by class when using a per-z renormalized δ) to demonstrate robustness to the radial selection.

P5-E8
- Location: Sec. IV A, step 12 vs. Sec. VI D/Table IV
- Problem: Density variable inconsistency. Step 12 says you “NN-interpolate the per-cell label + smoothed logdensity to each galaxy,” but density quartiles in Table IV are reported as ρ̄ ≈ 0.90–2.21 (linear units). It is unclear whether quartiles are formed on log ρ, linear ρ, or something else.
- Required fix: Specify precisely which field is used for density stratification (log10 ρ, ln ρ, or ρ/ρ̄) and ensure Table IV and related text reflect that choice. If you used logdensity for interpolation but linear density for quartiling, recompute one way consistently and update all quoted ρ̄ values and conclusions.

P5-E9
- Location: Sec. VI D(d), p. 8; Sec. VIII F, p. 12–13
- Problem: Unexplained sample-size mismatch. The env-class × target-program contingency test uses nbright+dark = 811,609 “spirals.” Elsewhere the chirality-relevant sample is 791,635. Sec. VIII F introduces an 812,793 “env-labeled superset,” but this reconciliation appears only later and not where the χ2 test is presented.
- Required fix: State explicitly, at the point of use in Sec. VI D(d), which sample (and cuts) produce 811,609, how it relates to the 791,635 headline sample, and why the extra rows are included (or excluded). Provide per-bin counts for the contingency table on the exact sample used for χ2.

P5-E10
- Location: Sec. V, first paragraph (“exact binomial 95% credible interval”); Fig. 2/3 captions
- Problem: Terminology conflation. You describe intervals as “exact binomial 95% credible,” mixing frequentist “exact” (Clopper–Pearson) with Bayesian “credible” (Jeffreys) language. Later you refer to “Jeffreys binomial credible intervals.”
- Required fix: Use consistent terminology. If you use Jeffreys, say “Jeffreys 95% credible intervals (Bayesian).” If you use Clopper–Pearson, say “Clopper–Pearson 95% confidence intervals (exact frequentist).” Update all mentions and captions accordingly.

MAJOR

P5-M10
- Location: Sec. V, Eq. (2) and related text; Table V captions
- Problem: Two-sided vs one-sided mapping. You use |σ|Bonfα,K = √2 erfc−1(α/K) as the Bonferroni “two-sided” threshold but do not show the derivation. For two-sided tests on a standard normal, z = Φ−1(1 − α/(2K)) = √2 erfc−1(α/K). This is correct only if α is the family-wise two-sided level and independence is assumed. The manuscript does not clearly connect α, K, and “two-sided” in captions/tables, inviting confusion.
- Required fix: Add one sentence deriving the mapping and clarifying that α is family-wise two-sided, hence the α/(2K) per-tail split. Ensure all quoted Bonferroni thresholds use the same convention and that captions (e.g., Table V, Fig. 3) state it explicitly.

P5-M11
- Location: Sec. V (nulls) vs results sections
- Problem: “Position-shuffle” null is introduced but never shown. All reported empirical p-values and LEE checks appear to use only label-shuffle. This leaves the reader unsure whether both null procedures were run and whether they agree.
- Required fix: For at least one representative analysis (e.g., NSIDE = 32 map and the density-quintile scan), report the position-shuffle max-stat pLEE alongside label-shuffle and comment on their agreement or differences.

P5-M12
- Location: Sec. III D, Table I (“p50 separation 0.0066′′; p99 0.30′′”)
- Problem: The median separation of 0.0066 arcsec (6.6 mas) is implausibly small for cross-matching two catalogs that do not share identical coordinates, and is far below typical Legacy astrometric uncertainties. It may reflect repeated coordinates or a unit/rounding artifact.
- Required fix: Verify the separation computation and units. Report additional quantiles (p10, p90) and, if many objects have identical RA/Dec across catalogs, state this explicitly. If a unit/precision artifact exists, correct the reported values.

P5-M13
- Location: Sec. VIII E, Table IX; Fig. 6; surrounding text
- Problem: The conclusion that the −4.75σ signal is concentrated in “0 maximal voids per pixel” hinges on these pixels being outside DESIVAST coverage, but the manuscript does not show a footprint overlay at NSIDE = 16 to substantiate this. The top panel of Fig. 6 is NSIDE = 32 (void counts), while Table IX is NSIDE = 16 (stratification), making visual cross-check difficult.
- Required fix: Add a small panel showing the DESIVAST footprint mask at NSIDE = 16, or overlay “0-void” pixels on a DESIVAST coverage map, and confirm quantitatively the fraction of 0-void pixels that lie outside coverage.

P5-M14
- Location: Sec. VIII F, Table X
- Problem: Baseline for σvs monopole mixes samples. You subtract fP5 measured on the 812,793 “env-labeled superset” but evaluate residuals for classes on the 791,635 headline subsample. This slight mismatch can bias σvs monopole at the fourth decimal.
- Required fix: Recompute σvs monopole using the monopole estimated on the exact same subset to which the residual is applied (i.e., per-class residuals within the 791,635 sample), or show the residuals are numerically indistinguishable if using the superset baseline.

MINOR

P5-n8
- Location: Sec. VII A, bullet “Paper-IV-monopole reference,” p. 9–10 vs Table X
- Problem: You state “|σvs monopole| at all four classes falls below 1.15,” while Table X shows a maximum of 1.11. Likely rounding drift, but it is inconsistent.
- Required fix: Harmonize the quoted maximum with Table X (1.11) or explain the source of the 1.15 figure.

P5-n9
- Location: Sec. IV A, steps 8–11; Fig. 1 caption
- Problem: Poisson normalization is not stated. You write Φ(k) = −δk/k^2 and Tij = kikjΦ(k). In many V-/T-Web implementations, normalizations (e.g., growth rate factors, 4πG a^2 ρ̄) are absorbed or explicitly stated so that λth has a clear meaning across Rs choices. Here, λth = 0 is claimed as “geometric default,” but the normalization of Φ (and hence eigenvalues) is not documented.
- Required fix: Add a sentence clarifying that you adopt the dimensionless normalization Φ(k) = −δk/k^2 (hence Tij = −(kikj/k^2) δk) and that λth = 0 depends only on eigenvalue sign, making normalization irrelevant for class counts; or state the normalization adopted if different.

P5-n10
- Location: Sec. VII (Phase 2 sweep) and Table VI
- Problem: The sweep narrative occasionally mixes “range in percentage points” with fractional values (e.g., “max 0.0022”). While you do parenthetically translate once, other instances omit the unit conversion.
- Required fix: Standardize to percentage points throughout this section, or present both fractional and pp consistently (e.g., “0.22 pp = 0.0022”).

P5-n11
- Location: Sec. V (Statistical methods)
- Problem: You often interpret σfrom half as a significance without caveat. For small N bins or large deviations from 0.5, σfrom half is only an approximation to a binomial z-test under p0 = 0.5 and can be conservative/liberal relative to exact tests.
- Required fix: Add a brief note that σfrom half is used as a standardized effect-size proxy; formal hypothesis tests rely on permutation nulls or exact binomial tests where appropriate.

P5-n12
- Location: Sec. VIII A (“k = 20 KDTree query … sufficient given the 24 Mpc/h maximum hole radius”)
- Problem: The rationale for k = 20 as “sufficient” is qualitative.
- Required fix: Add a one-line quantitative check (e.g., show that for all galaxies the distance to the 20th nearest hole center exceeds the maximum hole radius, hence the membership test is complete).

P5-n13
- Location: Abstract; Sec. VIII (“largest matched-sample environmental-dependence test … to date”)
- Problem: Novelty claim is not supported with explicit comparisons. While likely true, no enumeration of prior sample sizes/tests is provided.
- Required fix: Either soften the claim (“to our knowledge”) or cite prior works with their effective n to justify “largest.”

P5-n14
- Location: Sec. VI B (logistic regression)
- Problem: The covariates include cos α and |sin δ| without motivation.
- Required fix: Briefly justify these choices (e.g., to capture a dipole-like anisotropy in equatorial coordinates) and note that the result is unchanged if alternative spherical-harmonic bases are used.

NIT

P5-i4
- Location: Throughout
- Problem: Unit/style consistency. Occasional alternation between pp and fractional units within the same sentence; scattered “2563” notations persist outside places already flagged; a few hyphenation artifacts remain.
- Required fix: Global copy edit to standardize to 256^3, consistent pp vs fraction usage, and remove hyphenation artifacts.

P5-i5
- Location: Appendix A (toy EFT operator)
- Problem: Dimensional bookkeeping is not explicit. The operator form is acknowledged as schematic, but the mass/length dimensions of gϕ∇ϕ·∇ρ/ρbg within a Lagrangian density are not stated, nor the reference scale for “H0 units.”
- Required fix: Add a clarifying note on assumed dimensions and scaling (e.g., working in units where c = 1, and treating the operator as a phenomenological coupling normalized by H0 to make the bound dimensionless).

Explanation for why these are new
The items above arise from a focused second-pass check on arithmetic/units consistency, null-procedure comparability, and density-field construction details. They do not duplicate issues already raised in the initial report (bright/dark contradiction, 11.3σ ambiguity, monopole-uncertainty propagation, sigma-definition clarity, HEALPix pixel-accounting, etc.).