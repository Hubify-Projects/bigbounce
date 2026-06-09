# P5 R22prov — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6742 chars)
**Wall time**: 392.1s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across 791,635 DR1 Matched Spirals” (P5)

Scope of review
I audited the methodology, internal arithmetic, statistical claims, and consistency across the abstract, main text, figures, and tables. I recomputed all quoted σ, ranges, proportions, and looked-elsewhere thresholds from the numbers provided. Below I list all issues found, each labeled with an ID, severity, exact location, the problem, and the required fix.

Findings

ESSENTIAL

P5-E1 (Sec. VII, pp. 9–10): Impossible sample size in Phase-2 sweep; invalid σ quote
Quoted text: “The largest single-cell |σfrom half| across the entire sweep is 11.32 (filament at Rs = 10, λth = 0, n = 3,696,152).”
Problem: σfrom half is computed on the chirality-labeled sample. The largest available chirality-labeled parent after deduplication is 2,232,212 matched primaries (Table I), of which 791,635 are chirality-relevant (CW/CCW). Even under the relaxed env-label superset you later use (812,793), no per-class population can reach 3.70×10^6. A σ computed with N = 3,696,152 on chirality requires more objects than exist in the matched sample.
Required fix: Identify which population this N refers to and correct the statement. If it is the DESI-only spectro parent (14.6M) or all matched primaries (including NS), make that explicit and do not combine it with a chirality σ statistic. Replace the 11.32σ example with a value computed from the actual chirality-relevant counts in that sweep cell. If you wish to illustrate the catalog-monopole scaling, provide σpred using the correct per-class N for the chirality-relevant sample (or the stated 812,793 superset), and show observed σfrom half values that correspond to those same Ns.

P5-E2 (Sec. XI, p. 18 vs. Sec. VI D b, p. 8): Direct contradiction in target-program split
Quoted text (Sec. XI): “target-class split (BGS vs. LRG-ELG-QSO) with BGS-only CW fraction within ±0.001 of LRG-ELG-QSO.”
But earlier (Sec. VI D b): “bright (BGS-dominated; n = 775,760) fCW = 0.4970 … dark (LRG, ELG, QSO; n = 14,782) fCW = 0.5051…”
Problem: 0.4970 vs 0.5051 differ by 0.0081 (0.81 percentage points), not within ±0.001. This is a hard numerical contradiction between two parts of the paper.
Required fix: Recompute and correct the Sec. XI systematics summary (or, if Sec. VI D b mixed populations in a way inconsistent with the intended “catalog-wide BGS vs dark” split, restate the definitions and supply the correct fCW for each). Provide the exact Ns and fCW used for the Sec. XI claim, and ensure both sections’ numbers are computed on the same population definition.

P5-E3 (Sec. IX B, pp. 15–17; Fig. 9): Filament concordance distance computed on disjoint samples
Quoted text: “filament like vs filament: 0.026 pp (✓ within spec).”
Context: Tempel overlap is n = 110,586. The value you quote for the V-Web filament bin, 0.4980, is the canonical full-sample value from Table II (n = 408,187), not obviously restricted to the 110,586-object Tempel-overlap set (your Fig. 9 left panel is labeled n = 791,635).
Problem: A class-to-class concordance distance between two classifiers must be computed on the same overlap set, not on disjoint populations. Comparing Tempel filament-like on the DR10-overlap to V-Web filament on the full 791,635 sample is not a valid concordance metric.
Required fix: Recompute fCW for the V-Web classes restricted to the Tempel-overlap subsample and report |fTempel − fV-Web| for each pair using the same matched objects. Provide Ns and Jeffreys 95% CIs for each fCW on the overlap. Update Fig. 9 to plot V-Web-on-overlap next to Tempel (or state explicitly and prominently in caption and text if the left panel is not on the overlap and remove any quantitative “concordance” claims based on it).

P5-E4 (Sec. VI D d, p. 8): Non-credible p-value reporting (“p < 10−1000”)
Quoted text: “χ2 = 4932, 3 d.o.f., p<10−1000.”
Problem: This p-reporting is not meaningful; it vastly exceeds double-precision underflow bounds and suggests a lack of control over numerical reporting. PRD expects accurate or bounded p-values (e.g., p < 10−300 with a note on numerical precision), or simply “p ≪ 10−n”.
Required fix: Compute the exact tail probability for χ2 with 3 dof at 4932 using a reliable special-function library and report it either as a floating-point value if representable or as a bound at machine precision (e.g., p < 10−308 in double precision), or as “p ≪ 10−n” with a justified n. Replace “10−1000” everywhere.

P5-E5 (Sec. IX A, p. 14–15): Method-name confusion (V-Web vs T-Web)
Quoted text: “The T-Web classifier of §IV A computes the overdensity δ = ρ/ρ¯ − 1…” but §IV A is the V-Web tidal-tensor workflow used in this paper.
Problem: This mislabeling confuses readers about which algorithm you actually modified in the z-shell selection correction. The section later refers to “the selection-corrected classifier” as if it were your own run, not the external T-Web of Ref. [11].
Required fix: Replace “T-Web” by “V-Web” throughout §IX A where you refer to your own classifier; reserve “T-Web” solely for Ref. [11]. State explicitly: “we recompute our V-Web labels with a per-redshift-shell mean-density correction.”

P5-E6 (Sec. VI D c, p. 8): Per-class bright sample exceeds the class total; inconsistent base sets
Quoted text: “filament bright (n = 416,701) σ = −2.80 vs filament dark (n = 21,203) σ = +2.85,” while Table II gives filament n = 408,187 on the canonical run.
Problem: nbright for the filament class cannot exceed the total filament n in the same dataset. Either the 416,701 figure comes from a different sample definition (e.g., the 812,793 env-labeled superset) or it is a mistake.
Required fix: State unambiguously which parent sample each of these numbers refers to (791,635 vs 812,793). Report all class-by-program Ns and fCW on the same, clearly specified parent, and ensure internal consistency (nbright + ndark + … = ntotal per class). Correct the σ values if Ns change.

MAJOR

P5-M1 (Sec. VI A, p. 6): Wrong σpred for filament from the stated monopole
Quoted text: “σpred(filament) ≈ −3.16 and σpred(cluster) ≈ −3.28,” with ∆fCW = −0.0026 and nfil = 408,187, nclus = 397,505.
Problem: σpred = 2 ∆f √N. For filament: 2 × (−0.0026) × √408,187 = −3.32 (not −3.16). Cluster −3.28 is correct.
Required fix: Correct the filament σpred value and text discussion.

P5-M2 (Abstract, p. 1; plus multiple locations): Monopole magnitude described as “~0.2 pp”
Quoted text: “sensitivity floor set by the Paper IV catalog-monopole offset of ∼0.2 pp.”
Problem: The Paper IV (and your own P5) monopole is ∆f ≈ −0.0026 = −0.26 percentage points, not “~0.2 pp”. This is not a rounding at the second decimal place; it is a 23% understatement of the systematic offset magnitude.
Required fix: Replace “~0.2 pp” by “~0.26 pp” everywhere, or state a precise value.

P5-M3 (Sec. IX A, p. 14–15): “×40 tightening” claim needs apples-to-apples basis and uncertainty
Quoted text: “cross-class range 1.98 pp → 0.05 pp (×40), with n = 812,793 joined spirals.”
Problem: The 1.98 pp range was computed on the 791,635 sample (Table II), whereas the z-shell-corrected class fractions and 0.05 pp range are reported on the 812,793 superset. This obscures whether the factor-of-40 reduction is due to the correction or partly to the changed parent set. Also, no uncertainty is quoted on the range statistic.
Required fix: Recompute both ranges on the same parent sample (preferably the 812,793 superset if that is what the corrected classifier uses) and report the pre/post ranges together with per-class Ns so that a like-for-like comparison is possible. Provide a simple uncertainty diagnostic for the range (e.g., a bootstrap across galaxies or a bound based on the per-class binomial standard errors) to support the “×40” language.

P5-M4 (Sec. XI, p. 18): Systematics list contains non-reproducible identifiers and insufficient detail
Quoted text: “confidence-threshold sweep pmax_cls_eq ∈ {0.4, 0.5, 0.6, 0.7, 0.8} … match-radius sweep … footprint split (N/S/DES-only) … target-class split … No test produces a >3σ residual …”
Problem: The summary provides no Ns, no per-bin fCW values, and (as noted in P5-E2) at least one line contradicts earlier results. The token “pmax_cls_eq” is unexplained notation.
Required fix: Provide a small table or appendix with, for each sweep: bin definitions, per-bin Ns, fCW, and σfrom half (or σvs monopole) so the statements can be verified. Define the “confidence” variable used and how it enters the filtering.

MINOR

P5-m5 (Sec. VII, p. 9): Mixed units presentation for the “range” statistic
Quoted text: “maximum range … is 0.22 percentage points (at Rs = 25, λth = 0.3);” later “max 0.0022 at Rs = 25, λth = 0.3.”
Problem: Mixing pp and unit-fraction without repeating the unit risks confusion.
Required fix: Use one unit consistently (preferably percentage points) and state values once.

P5-m6 (Multiple places, e.g., Sec. IX C caption, p. 16): Occasional T-Web/V-Web nomenclature drift
You sometimes use “T-Web” generically for tidal-tensor classifiers but mean “our V-Web implementation.” This is separate from P5-E5 where an explicit mislabel occurs.
Required fix: Harmonize terminology: V-Web = your implementation; T-Web = Ref. [11]. Add a one-sentence reminder where needed.

P5-m7 (Sec. IX B, p. 16; Fig. 9 caption): Claimed 0.026 pp filament concordance inconsistent with the numerical difference shown elsewhere
Your text and caption both cite 0.026 pp; using 0.4980 vs 0.4982 is 0.02 pp. Likely a rounding/source mismatch.
Required fix: After fixing P5-E3 (restricting to the overlap), report the correct difference to three significant digits and ensure caption and text match.

P5-m8 (Sec. V A, p. 5): Notation in Eq. (1) is potentially ambiguous in the linearized text
The displayed fraction “ΔfCW / (0.5/√N)” is correct. In the running text, it could be read as (ΔfCW / 0.5) / √N. The displayed equation is fine; consider adding parentheses in the inline form to avoid ambiguity.
Required fix: Optional but recommended: use explicit parentheses when repeating the equation inline.

NITS

P5-n1 (Sec. VII, p. 9): Typo in sweep grid spec
Quoted text: “Ngrid = 256 × λth ∈ {0.0, 0.1, 0.3}.”
Required fix: Replace by “Ngrid = 256^3; λth ∈ {0.0, 0.1, 0.3}.”

P5-n2 (Stylistic, multiple pages): “σfrom half”
Hyphenate as “σ-from-half” for readability or define σhalf explicitly once and use that symbol.

P5-n3 (Sec. VIII B, p. 11): VoidFinder maximum hole radius
Quoted text: “k = 20 KDTree … sufficient given the 24 Mpc/h maximum hole radius.”
Problem: The source of “24 Mpc/h” is not cited here. Later, you quote larger maximum effective radii for V2-REVOLVER/VIDE.
Required fix: Add a parenthetical citation to the DESIVAST release where this bound for VoidFinder holes is stated, or report the computed maximum from your parsed catalog.

Additional checks and confirmations

- Table I, sample sizes and separations are self-consistent; the explanation of 6.6 mas median separation due to shared Legacy astrometry is correct and helpful.
- Table II σ-from-half values recompute correctly from the stated f and N; the inter-class range 1.98 pp is correct.
- Eq. (2) Bonferroni thresholds compute to your quoted numbers for K = 5 and K = 1054.
- Table III residuals |σobs − σpred| recompute; the use of σpred = 2|Δf|√N with Δf = −0.0026 is correct.
- Table V HEALPix max-|σ| and pLEE values are plausible given NMC = 1000; you properly use the empirical max-statistic null and avoid over-precision.
- DESIVAST-anchored analyses (Tables VII–IX) have arithmetically consistent Ns and σ. The difference ΔfCW = 0.0007 in Table VII is correct. The HEALPix-per-void-density stratification sums to nlz and the σs are consistent with the stated interpretation.
- The “σ vs monopole” residuals in Table X recompute from f − fP5 on the 812,793 superset.

Length and focus
The manuscript (21 pages) is long for the central result (an environmental-independence null), with substantial digressions. After addressing the essential/major issues, I recommend tightening:

- Focus the primary narrative on the DESIVAST-anchored result and the z-shell–corrected V-Web rerun. Summarize secondary cross-checks more compactly, pushing many details (e.g., per-bin σ maps, repeated restatements) to a supplementary or data release note.
- A lean target would be ≤15 journal pages without losing methodological content.

## Summary recommendation
MAJOR REVISIONS

The core scientific conclusion (no detectable dependence of spiral chirality on large-scale environment at DR1-and-25 Mpc/h resolution) is plausible and, after corrections, could merit publication. However, there are several essential methodological inconsistencies that must be fixed before PRD can consider the paper: an impossible sample size used to illustrate σ-scaling, a hard contradiction in the target-program split, a flawed cross-classifier concordance computed on disjoint samples, and a non-credible p-value (“10−1000”). These, along with terminological confusion and a few numerical misstatements, need correction and clearer, consistent reporting on a single, well-defined parent sample for each analysis. Once these issues are resolved and the text tightened, the paper can be re-evaluated.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW ADDITIONAL FINDINGS (second-pass audit)

ESSENTIAL
None newly found beyond those in the first report.

MAJOR

P5-M5 (Sec. VIII E vs Fig. 8 top; HEALPix NSIDE and counts inconsistent)
- Problem: The text bins DESIVAST maximal voids at NSIDE = 16, reporting 297 occupied pixels (median 14 voids/pixel). Fig. 8’s top panel is labeled NSIDE = 32 with 885 occupied pixels (median 4 voids/pixel). The figure and the body describe different NSIDEs and yield incompatible counts without explicit linkage to which analysis (including Table IX) each supports.
- Required fix: State explicitly which NSIDE is used for Table IX. Align the figure and text to the same NSIDE or present both consistently, with a clear rationale. Update all quoted occupied-pixel counts and medians so the caption and text match the analysis being interpreted.

P5-M6 (Sec. VIII F; consistency of monopole subtraction parent)
- Problem: σvs monopole in Table X is computed for the 791,635-class table using fP5CW derived on the 812,793 env-labeled superset. While the difference is small, it mixes parents and prevents an exact apples-to-apples residual.
- Required fix: Recompute σvs monopole using the monopole measured on the exact same parent set as the per-class values (791,635), and report the superset version separately (or demonstrate that using either parent changes all σvs monopole by <0.02).

P5-M7 (Sec. VIII B; KDTree k=20 is not a guaranteed-safe membership query)
- Problem: The VoidFinder-based “void/non-void” assignment uses a fixed-k nearest-neighbor search (k = 20) on hole centers to decide point-in-sphere membership, justified by a 24 Mpc/h maximum hole radius. Fixed-k does not guarantee capturing all holes with centers within 24 Mpc/h if local hole-center density exceeds 20, which can produce false “non-void” assignments.
- Required fix: Replace the fixed-k query with a radius query (center-distance ≤ Rmax) or prove that, for all points in the nlz sample, the number of hole centers within 24 Mpc/h never exceeds 20. Add a k-sensitivity or radius-query replication showing identical membership counts.

MINOR

P5-m9 (Fig. 5 right caption; sign error in σpred formula)
- Problem: Caption states σpred = −2ΔfCW√N at ΔfCW = −0.0026. Eq. (1) defines σpred = 2ΔfCW√N. The extra minus flips the sign when ΔfCW < 0.
- Required fix: Use σpred = 2ΔfCW√N (the sign then follows from ΔfCW).

P5-m10 (Table II and Abstract; filament σ-from-half slightly off)
- Problem: For filament (f = 0.4980, N = 408,187), σ-from-half recomputes to −2.56, not −2.61 as reported.
- Required fix: Correct σ to −2.56 and propagate wherever reused.

P5-m11 (Sec. VIII F vs Fig. 8 bottom; “valid pixels” counts unclear)
- Problem: Sec. VIII F references “1,821 valid pixels” at NSIDE = 32 on the “same matched-spiral catalog,” while Fig. 8 bottom (NSIDE = 32) reports 1,496 valid pixels for the z ≤ 0.24 cut. The thresholds (e.g., ≥ 200 spirals/pixel, z-cut) differ but are not stated alongside the 1,821 number.
- Required fix: For each pixel-level statistic, specify NSIDE, redshift cut, and spiral-per-pixel threshold. Report the count of valid pixels for each configuration in-text or in a table so the numbers can be reconciled.

P5-m12 (Abstract; “~5 pp” counting-statistics statement ambiguous)
- Problem: “counting statistics of ∼5 pp (… ∼2σ on the binomial null)” refers to the void bin (N = 428), where one-sided 1σ ≈ 2.4 pp and 2σ ≈ 4.8–5.0 pp. As written, it’s unclear whether “∼5 pp” is a half-width, full-width, or a 2σ half-width.
- Required fix: Specify “approximately ±2.4 pp (1σ) or ±4.8–5.0 pp (2σ) for the void bin,” avoiding ambiguity.

P5-m13 (Novelty claim; largest/first unsupported)
- Problem: Statements such as “largest matched-sample environmental-dependence test to date” are not accompanied by a quantitative comparison to prior works/samples.
- Required fix: Either add a brief comparison table/citation set quantifying prior sample sizes and classes analyzed, or soften to “to our knowledge” and remove the superlative.

P5-m14 (Units/notation for “density” in within-class tables)
- Problem: The symbol “ρ̄” is used for the per-galaxy (smoothed) density proxy in Table IV without defining units or normalization (linear vs log-density). This impedes reproducibility.
- Required fix: Define precisely how the per-galaxy density used for quartiles is constructed (e.g., smoothed overdensity δ, or log10[1+δ], normalization, and any clipping), and ensure symbols reflect that definition.

P5-m15 (Sec. VIII A; confusing cross-reference “V-Web secondary path (§XIII)”)
- Problem: The phrase suggests §XIII covers the “V-Web secondary path,” but §XIII is the Limitations section. This cross-reference is confusing and appears misapplied.
- Required fix: Replace by a direct reference to the relevant V-Web methodology section(s) (§IV/§VII) and, if desired, additionally cite §XIII for the RSD caveat.

P5-m16 (Sec. VII A; “counting-statistics floor” phrasing is misleading)
- Problem: The text says the per-cell inter-class range (max 0.22 pp) is “below the per-class counting-statistics floor,” then clarifies it’s below the wall/void floors, but not the filament/cluster floors (~0.08 pp). The phrase “the dominant per-class measurement uncertainty” is ambiguous.
- Required fix: State explicitly: “0.22 pp is above the filament/cluster 1σ (~0.08 pp) but below the wall (~0.6 pp) and void (~2.4 pp) 1σ; thus, the measured range is dominated by the low-N classes in the range statistic.”

P5-m17 (Sec. VI D b; bright vs dark z-test not reproducible as written)
- Problem: A |z| ≈ 3.4 claim is made for the filament bright-vs-dark difference without providing the underlying fCW and N per subgroup on the same parent definition (see also P5-E2). This precludes independent recomputation.
- Required fix: Provide Nbright, fbright and Ndark, fdark for the exact parent used (812,793 or 791,635) and the two-sample z formula inputs so the |z| ≈ 3.4 can be verified.

NITS

P5-n4 (Typo; stray minus in “HEALPix-NSIDE-= 32”)
- Required fix: Remove the extraneous hyphen.

P5-n5 (Units consistency)
- Problem: Mpc/h and h−1 Mpc are used interchangeably in different places.
- Required fix: Pick one convention and apply uniformly.

Explanation of completeness
This second pass focused on A–J checks that often expose hidden inconsistencies. The most consequential new findings are the HEALPix NSIDE/body–figure mismatch (P5-M5) and the KDTree fixed-k membership method (P5-M7), which can affect void membership assignments. Several additional minor inconsistencies (formula sign, σ rounding, parent matching for residuals, ambiguous phrasing, and cross-references) should be straightforward to correct and will improve rigor and reproducibility.