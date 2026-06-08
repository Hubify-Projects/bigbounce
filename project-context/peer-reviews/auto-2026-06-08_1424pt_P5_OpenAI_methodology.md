# P5 auto-2026-06-08_1424pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8187 chars)
**Wall time**: 293.0s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals”

Scope of this review
I reviewed the full PDF as provided. My focus is methodology rigor, statistical validity, internal consistency of all scalars in the abstract and conclusions, dimensional consistency, error propagation, and figure/table arithmetic.

Overall assessment
The paper presents an ambitious and detailed null test of spiral chirality vs. environment using DESI DR1, with multiple cross-checks (V-Web, DESIVAST voids, Tempel+ FoF, ASTRA EDR). The analysis framework is in principle valuable. However, there are several essential internal inconsistencies and statistical misstatements that must be resolved before the manuscript can meet PRD standards. Most critically, the sample size used for the headline V-Web environment breakdown is inconsistent in the abstract, text, figure captions, and Table II; there is an impossible “observed” sigma computed with N larger than the number of chirality-labeled objects; and systematics statements contradict earlier results in the same paper. There is also at least one hard numerical error in a look-elsewhere Bonferroni threshold. These issues directly affect the primary quantitative claims, reproducibility, and the reader’s ability to audit the statistics.

Findings and required actions

ESSENTIAL

P5-E1. Sample-size inconsistency (abstract; Section VI A; Table II; Fig. 2)
- Location: Abstract (page 1), Section VI A/Table II (page 5), Fig. 2 caption (page 5), Section VIII F (page 12–13).
- Problem: The abstract states “per-class CW fractions on the 791,635 chirality-relevant spirals are ... filament n=408,187; cluster n=397,505; wall n=6,673; void n=428.” These four counts sum to 812,793, not 791,635. Table II lists the same counts (summing to 812,793), but Fig. 2’s caption says “n = 791,635.” Later (§VIII F) you acknowledge a superset of 812,793 env-labeled spirals relative to a 791,635 headline subsample. As written, the abstract and Fig. 2 misstate the sample on which the quoted class-wise fractions are computed, and the reader cannot tell which sample underlies which result.
- Required fix: Define precisely the chirality-labeled sample used for each environment analysis once, early in the paper, and use that sample consistently everywhere. If the V-Web class results are on the 812,793-superset, the abstract and Fig. 2 must say so, and all sigmas and fCW values there must be recomputed and reported for that sample only. If 791,635 is the intended “headline,” the class counts must sum to that number and all sigmas/fractions must be recomputed accordingly. Remove contradictory sample sizes from captions and text.

P5-E2. Impossible “observed” sigma computed with N≫Nlabels
- Location: Section VII, Phase 2 sensitivity sweep (page 8–9).
- Problem: “The largest single-cell |σfrom half| across the entire sweep is 11.32 (filament at Rs=10, λth=0, n=3,696,152).” By definition in §V, σfrom half uses the CW/CCW labels. There are only ~0.8 million chirality-labeled spirals in total; no environment cell of labeled spirals can have n=3.7 million. The paragraph then refers to that 11.32 as “observed” and simultaneously as “predicted.” This mixes apples (measured σ on the labeled sample) and oranges (a prediction based on the full DESI spectro counts) and is internally inconsistent.
- Required fix: Remove the “observed” claim for n=3,696,152. Either (a) report only measured σfrom half for the chirality-labeled sample per cell (nclass ≤ 812,793 overall), or (b) keep a prediction-only statement, clearly labeled as such, without calling it observed and without listing any n that is not an actual labeled-sample count. If you retain predictions, present them alongside the corresponding measured σ for the same labeled-sample bin and explicitly mark them as not directly comparable to permutation p-values.

P5-E3. Contradictory target-program (bright/dark) statements
- Location: Section VI D.b (page 7) vs. Section XI (page 17).
- Problem: Section VI D.b reports a substantial bright-vs-dark difference (e.g., bright fCW=0.4970, dark fCW=0.5051; a two-sample filament-class |z|≈3.4σ). Section XI then claims as a systematics null test: “target-class split (BGS vs. LRG-ELG-QSO) with BGS-only CW fraction within ±0.001 of LRG-ELG-QSO. No test produces a >3σ residual after Paper IV-monopole correction.” These statements are incompatible. Subtracting a global monopole does not change a bright–dark difference; a ~0.0081 absolute difference (0.81 pp) is not “within ±0.001.”
- Required fix: Recompute and report the global (and class-specific) bright-vs-dark differences consistently in one place, with exact n per bin. Remove or correct the Section XI bullet. If the earlier 3.4σ result holds, retain it here with the same numbers; if a different filtering was used, state it and explain the discrepancy. Do not claim “no >3σ residual” unless the actual z-tests after the stated filtering are <3σ in all cases.

P5-E4. Misstated “−5σ” monopole on the 791,635 sample
- Location: Section VIII F (page 12–13).
- Problem: You state “−5.00σ on the 791,635 chirality-relevant sample.” From Table I, CW=393,592 and CCW=398,043 give fCW=393,592/791,635≈0.497351. Using σ=(f−0.5)/(0.5/√N) yields σ≈−4.71, not −5.00. Your −5.07σ corresponds to the 812,793-superset with fCW≈0.49719, which you also quote. The 791,635 line is wrong unless f for that subset is actually ≈0.4972 (contradicting Table I).
- Required fix: Recompute and report the 791,635-sample monopole σ from the exact counts in this paper, or remove the −5.00σ claim. Keep the 812,793-superset σ separate from the 791,635-subsample and label them unambiguously. All downstream “σpred vs σobs” comparisons should reference the correct N.

P5-E5. Bonferroni threshold error
- Location: Section VII.A (page 9).
- Problem: You state “Bonferroni-9 (α=0.05) threshold |σ| ≈ 3.02.” For K=9 two-sided Bonferroni at α=0.05, the correct Gaussian threshold is z = Φ−1(1 − α/(2K)) ≈ Φ−1(0.997222...) ≈ 2.78, not 3.02. 3.02 corresponds to α=0.01, K=4 (which you use correctly elsewhere).
- Required fix: Correct |σ|Bonf0.05,9 to ≈2.78 everywhere it is used. State explicitly whether any conclusion would change under the correct threshold (it apparently does not, given your |σ| residuals < 1.15).

P5-E6. Filament-class program-split counts exceed total filament count
- Location: Section VI D.c (page 7).
- Problem: “Filament bright (n = 416,701) vs filament dark (n = 21,203).” The total filament class (Table II) has nfilament=408,187. nbright + ndark must not exceed the total. As written, 416,701 + 21,203 = 437,904 > 408,187.
- Required fix: Provide the correct bright/dark counts for the filament class that sum to the total. Recompute the corresponding σ for each split and repeat any z-tests that use these numbers.

P5-E7. Abstract must not misattribute class results to the wrong N
- Location: Abstract (page 1).
- Problem: The abstract claims “per-class CW fractions on the 791,635 chirality-relevant spirals are ...” followed by counts that sum to 812,793. This is not a cosmetic issue: abstract numbers must be self-consistent and traceable to a single, well-defined sample.
- Required fix: Correct the abstract to quote numbers from exactly one sample, consistent with Table II and Fig. 2 after you resolve P5-E1.

MAJOR

P5-M1. σpred for filament off by ~0.16σ
- Location: Section VI A (page 6).
- Problem: You write “predicting σpred from ∆fCW = −0.0026 gives σpred(filament)≈ −3.16 and σpred(cluster)≈ −3.28.” Using Nfilament=408,187 and Ncluster=397,505, σpred = 2·(−0.0026)·√N gives −3.32 and −3.28, respectively. The filament number is off at the second significant digit.
- Required fix: Correct σpred(filament) to ≈ −3.32 (or clearly state a different ∆f used), and ensure all similar σpred references are recomputed from the stated N.

P5-M2. Reproducibility: missing explicit repository/DOI
- Location: Throughout; Appendix B (page 19).
- Problem: Multiple references to “companion data repository” are made, but no URL/DOI is given in the text. PRD requires actionable data/code availability to reproduce the numbers and figures.
- Required fix: Provide a working public URL and/or DOI for the code, configuration files, and derived data products sufficient to reproduce every table/figure number (including the Phase 2 sweep summaries). Include exact commit hashes or release tags corresponding to this submission.

P5-M3. Overstatement of DESIVAST RSD “immunity”
- Location: Section VIII (page 10–11).
- Problem: You characterize the DESIVAST membership test as “essentially RSD-immune” and then note relevant caveats. While the qualitative argument is reasonable (void Reff ≫ σv/H), it is not quantified. Given the precision claimed (sub-0.2 pp differences), even a small fraction of boundary-crossers could matter.
- Required fix: Temper the claim or provide a quantitative bound (e.g., an upper limit on membership flips under a plausible RSD displacement model, with void-size distribution folded in). At minimum, rephrase as “expected to be small compared to our current statistical precision” and point to a future reconstruction-based check.

P5-M4. χ2 p-value hyperbole
- Location: Section VI D.d (page 8).
- Problem: Reporting “p < 10−1000” is not meaningful. Provide an actual computed p-value (or an upper bound derived from a stable asymptotic) with enough digits to support your interpretation.
- Required fix: Quote p (e.g., p < 10−x with a reasonable x based on numerical evaluation), and provide the contingency-table counts so the reader can verify the χ2 statistic and p-value independently.

P5-M5. Logistic regression reporting incomplete
- Location: Section VI B (page 6).
- Problem: You report a z-coefficient “0.0059” without units, standard error, or model specification (link function, covariates fully listed, handling of class imbalance). The intercept is reported as “0.000652” without uncertainty.
- Required fix: Provide the regression specification (logit link), covariate list, the estimated coefficient for z with its standard error and p-value (or z-score), and the intercept with uncertainty. State whether robust standard errors were used.

P5-M6. KDTree “k=20” sufficiency claim needs justification
- Location: Section VIII B (page 11).
- Problem: You state k=20 neighbors are “sufficient given the 24 Mpc/h maximum hole radius” without demonstrating that no missed matches occur at that k over the full volume.
- Required fix: Provide a bounding argument (e.g., a maximum hole-center surface density and a safe k computed from it) or show that increasing k (e.g., to 50 or 100) does not change nvoid by more than a negligible amount.

P5-M7. Clear segregation of in-sample statistical tests
- Location: Multiple.
- Problem: The manuscript presents binomial σ-from-half values, permutation p-values, and predictions from an external monopole offset side-by-side. In at least one place (Phase 2, P5-E2) they are inadvertently conflated.
- Required fix: Wherever different null procedures are juxtaposed, insert an explicit sentence stating they are not directly comparable statistics and serve different diagnostic roles (binomial σ for deviation from 0.5; σpred as a catalog-bias expectation; permutation p for LEE-controlled significance). Ensure this is done at every side-by-side presentation (mandatory per the review instructions).

MINOR

P5-n1. Minor textual/typographical issues
- Locations: multiple.
- Examples: (a) Stray “a” footnote marker injected into body on page 1–2 (“a on the full 14,622,283...”); (b) Using “2563” instead of 256^3 in several places; (c) Some hyphenation and spacing issues (“comoving grid with a 25 Mpc/h Gaussian smoothing” is fine; but ensure consistent use of units).
- Required fix: Clean up footnote marker placement, superscripts, and typesetting.

P5-n2. Clarify “pp” usage
- Location: Throughout.
- Problem: “pp” (percentage points) is used widely; define it once early (e.g., in Statistical Methods) for clarity.
- Required fix: Add a brief definition the first time “pp” is used.

P5-n3. Reference details
- Location: References [11], [12].
- Problem: Both are 2026 arXiv preprints. Ensure that if these are revised/submitted versions, the arXiv identifiers and titles exactly match those cited and that the comparisons you draw correspond to the tracer and volume selections in those works.
- Required fix: Verify and, if needed, update titles/IDs and clarify any caveats in the comparison text.

P5-n4. Length relative to contribution
- Observation: The paper runs 20 pages for a net conclusion of a null result. Given the number of secondary cross-checks, this may be justifiable, but the paper would be clearer if focused on the DESIVAST primary analysis and one deterministic (V-Web) and one probabilistic (ASTRA) cross-check, with the rest moved to a Supplement or Data Appendix.
- Recommendation: Target 12–14 pages main text by moving some diagnostic scans (e.g., repeated quartile tables, some map figures) to an online supplement.

P5-n5. Consistency in HEALPix pixel counts
- Location: Section VIII E (page 12–13) vs. Fig. 6 (page 14).
- Problem: Different pixel-count thresholds and NSIDE values are used in different sections (e.g., 1,496 valid pixels vs. 1,821). These appear to pertain to different redshift cuts and overlap criteria, but this is not made explicit.
- Required fix: Where such numbers are given, clearly state the redshift and count thresholds used and that the figures refer to different subsamples.

NIT

P5-nt1. Replace “thin spherical shell” with a brief quantitative note
- Location: §IX B (page 15).
- Suggestion: Add the approximate radial thickness over which the mask is significant, to give the reader a scale for the “shell” effect.

P5-nt2. “P5” internal tag
- Location: Throughout.
- Suggestion: While not harmful, consider removing internal series tags (“P5”) from the main text unless needed for cross-referencing your own series; PRD readers may find them distracting.

Audit of abstract and conclusion scalars
- 2,232,212 unique matched galaxies; 791,635 chirality-relevant: consistent with Table I.
- Class counts in abstract (void 428, wall 6,673, filament 408,187, cluster 397,505): sum to 812,793, not 791,635 (P5-E1).
- Per-class fCW values (0.4836, 0.5034, 0.4980, 0.4963) and σfrom half (−0.68, +0.55, −2.61, −4.66): check out arithmetically for the counts shown in Table II.
- Range across classes 1.98 pp: correct (0.5034 − 0.4836).
- Phase 2 max range 0.22 pp at Rs=25, λth=0.3: matches Table VI.
- Label-shuffle HEALPix p-values 0.61/0.135/0.413: matches Table V.
- Pearson r=+0.006, p=0.88: internally consistent with n≈727.
- DESIVAST void vs non-void ∆fCW=0.0007 with nvoid=56,981: matches Table VII.
- “−5σ catalog-level signal concentrated entirely in the 0 maximal voids per pixel bin”: Table IX supports −4.75σ there; characterization is fair.

Most abstract claims are traceable and numerically correct once the sample-size inconsistency is resolved; the headline “environment-independence within present sensitivity” is supported by the DESIVAST primary analysis.

## Summary recommendation
MAJOR REVISIONS

The core idea and much of the analysis are sound, but the manuscript currently contains essential inconsistencies in sample sizes and sigma calculations, an impossible “observed” sigma based on N larger than the labeled sample, a miscomputed Bonferroni threshold, and contradictory statements about target-program splits. These must be corrected and the sample definitions made consistent across abstract, text, tables, and figures. Reproducibility also requires an explicit code/data repository link. With these fixes and modest tightening, the paper could meet PRD’s methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS AFTER SECOND-PASS AUDIT

I re-checked the manuscript specifically for fresh arithmetic, caption/body mismatches, dimensional consistency, cross-references, null-procedure comparability, abstract faithfulness, unsupported novelty, hedges, appendix consistency, and stale numbers. The items below are in addition to the issues already listed in my initial review. I continue your numbering.

ESSENTIAL

P5-E8. Equation (1) algebraic inconsistency (units/operations)
- Location: §V, Eq. (1).
- Problem: You write σpred = ΔfCW/0.5/√N = 2·ΔfCW·√N. The left expression simplifies to 2·ΔfCW/√N, not 2·ΔfCW·√N. The second equality is correct; the first is not.
- Required fix: Correct the first expression to ΔfCW/(0.5/√N) or remove it; ensure all downstream uses match the correct 2·ΔfCW·√N form.

P5-E9. ∆fCW sign inconsistency in Table VIII vs stated fractions
- Location: §VIII B–C; Table VIII.
- Problem: For VoidFinder you report fvoid=0.4964, fnon-void=0.4971, yet Table VIII lists ∆fCW=+0.0007. If ∆fCW ≡ fvoid − fnon-void, this should be −0.0007. In the text you also quote “∆fCW = 0.0007” without defining sign. REVOLVER is reported as −0.0019, implying a signed convention was intended.
- Required fix: Define ∆fCW explicitly once (e.g., fvoid − fnon-void) and make all rows and text consistent with that definition. Correct the VoidFinder row and any references accordingly.

P5-E10. Phase-2 cell at Rs=10 Mpc/h is under-resolved on a 25.9 Mpc/h grid
- Location: §VII (sweep description and Fig. 5).
- Problem: The canonical grid has cell size ≈25.9 Mpc/h. A Gaussian smoothing of Rs=10 Mpc/h is below the grid scale and cannot be meaningfully represented at Ngrid=256^3. Results at Rs=10 are therefore not physically resolved.
- Required fix: Either (a) rerun the Rs=10 cells on a finer grid (e.g., Ngrid≥512^3) and update all numbers, or (b) remove Rs=10 from the sweep and state explicitly that the smallest resolved Rs at Ngrid=256^3 is ≳ one cell.

P5-E11. Cluster redshift-quartile claim contradicts the quoted σ
- Location: §VI D.a.
- Problem: You state “none [of the four cluster z-quartiles] individually crossing the Bonferroni-4 |σ|=3.02 threshold at α=0.01,” but you also report Z3 σ=−3.14, which exceeds 3.02.
- Required fix: Correct the sentence (either acknowledge Z3 crosses the α=0.01, K=4 threshold, or provide the precise threshold used), and update any downstream interpretation.

P5-E12. DESIVAST V2 void-count inconsistencies
- Location: Abstract/§VIII (multiple places).
- Problem: The manuscript quotes two different sets of catalog-wide void counts for the DESIVAST watershed catalogs: 420 (REVOLVER) and 295 (VIDE) earlier; later §VIII C lists nvoid=1,992 (REVOLVER effective voids) and 1,478 (VIDE). These cannot both be true without a clear distinction (e.g., “maximal voids” vs “effective voids” vs “zones”).
- Required fix: Reconcile and define the counting conventions (interior/maximal/effective/zone-level) and use one set consistently. Provide the exact DESIVAST file/HDU and field names corresponding to these counts.

P5-E13. Fig. 5 caption misleads on which sample underlies the fCW ranges
- Location: Fig. 5 caption vs §VII text.
- Problem: The caption emphasizes the 14,622,283-galaxy DR1 spectro sample used to compute the tidal tensor, but the reported per-class fCW ranges are computed on the chirality-labeled matched subset. As written, a reader could infer the range uses all 14.6M objects.
- Required fix: Amend the caption to state explicitly that fCW ranges are measured on the chirality-labeled matched-spiral subset, while the tidal field is computed from the full spectroscopic parent.

MAJOR

P5-M8. Bonferroni-5 threshold at α=0.05 miscomputed
- Location: §V B, “Multiplicity bookkeeping.”
- Problem: You quote |σ|Bonf0.05,5 ≈ 2.81. The correct two-sided Bonferroni Gaussian threshold is z=Φ−1(1−α/(2K))≈Φ−1(0.995)=2.575.
- Required fix: Correct the threshold to ≈2.58 and state explicitly whether any conclusion changes (it appears not).

P5-M9. KDTree maximum-hole-radius inconsistency undermines sufficiency claim
- Location: §VIII A–D.
- Problem: You justify a KDTree k=20 by citing a “24 Mpc/h maximum hole radius,” but elsewhere you state effective radii up to 32–55.9 Mpc/h (V2-VIDE). The “k=20 is sufficient” claim relies on an incorrect or inconsistent radius bound.
- Required fix: Use the true maximum effective radius per algorithm (VoidFinder/V2-REVOLVER/V2-VIDE), update k accordingly, and show that increasing k (e.g., 20→100) does not change nvoid beyond a negligible tolerance.

P5-M10. Boundary-crossing RSD width vs eigenvalue shift lacks quantitative consistency
- Location: §VII A (RSD heuristic).
- Problem: You posit a boundary band |λ−λth|≤σrsd/Rs and then quote an “eigenvalue-shift magnitude ∼0.04 σλ” for σrsd∼5 Mpc/h and Rs=25 Mpc/h. σrsd/Rs≈0.2, not 0.04; mapping that to 0.04 σλ without derivation is unclear and dimensionally suspect.
- Required fix: Provide a derivation linking σrsd/Rs to a shift in the eigenvalue distribution (including normalization of λ), or remove the 0.04 σλ figure and rephrase qualitatively.

P5-M11. Overinterpretation of the 0/6 V-Web void vs DESIVAST-void match
- Location: §VIII A.
- Problem: The statement “0% concordance … meaning the V-Web ‘void’ label at low z should be read as ‘not in a DESIVAST-defined … minimum’” is too strong for n=6. It may be consistent with survey-edge effects, but cannot substantiate a general “should be read as” claim.
- Required fix: Temper to “in this very small test sample we found 0/6; this is consistent with survey-edge artifacts and motivates using DESIVAST voids for the primary analysis,” and avoid general inferences from n=6.

MINOR

P5-n6. Typo conflating grid size with λth in Phase 2 description
- Location: §VII (“Ngrid = 256 × λth ∈ {0.0, 0.1, 0.3}”).
- Problem: As written, it reads as if Ngrid depends on λth. This is a typesetting error.
- Required fix: Replace with “Ngrid = 256^3; λth ∈ {0.0, 0.1, 0.3}.”

P5-n7. Ambiguous density units in Table IV and surrounding text
- Location: §VI D and Table IV.
- Problem: “¯ρ” values (e.g., 1.55, 1.86) are used without defining the normalization (counts per cell? 1+δ from smoothed field?). Earlier you also mention ρ̄cell=4.64 galaxies/cell.
- Required fix: Define the density unit used for quartiles (e.g., 1+δ from the smoothed field at Rs=25 Mpc/h) and distinguish it clearly from raw counts/cell.

P5-n8. Absent numeric support for “cluster-class joint |z| ≈ 0.5σ” in the bright/dark split
- Location: §VI D.b (end).
- Problem: You quote a “cluster class joint |z| ≈ 0.5σ” without giving the underlying nbright, ndark, and fCW for the cluster split.
- Required fix: Provide the exact counts and fractions used to compute this 0.5σ value (as you did for the filament class).

P5-n9. Per-cell permutation pLEE phrasing is ambiguous
- Location: §VII A (“Pre-cell label-shuffle null”).
- Problem: The sentence “returns max-class p-values in the range pLEE=0.41–0.67 across the nine cells” is hard to parse; pLEE was defined as the max-statistic across K bins. “Max-class p-values” reads like per-class p-values.
- Required fix: Clarify that for each cell you compute the empirical p-value of the maximum |σ| across the four classes, and report that pLEE range.

NIT

P5-nt3. Novelty/scale claims need one-line quantitative context
- Location: §VIII B (end) and Conclusions.
- Problem: Phrases like “largest matched-sample environmental-dependence test … to date” are plausible but unsupported.
- Suggested fix: Add a clause comparing your nvoid (e.g., 56,981 DESIVAST-defined void spirals) to prior published void-chirality samples, or cite why this is largest to your knowledge.

Explanation
These additions stem from re-deriving every equation and checking figure captions and body text for consistency. The under-resolution of Rs=10 on a 256^3 grid, Eq. (1)’s algebraic mismatch, the ∆fCW sign error in Table VIII, the Bonferroni-5 threshold error at α=0.05, the z-quartile misstatement, and the inconsistent DESIVAST watershed void counts are the most consequential new findings. Addressing them will materially improve correctness and reproducibility.