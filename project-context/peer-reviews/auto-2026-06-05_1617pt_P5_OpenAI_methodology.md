# P5 auto-2026-06-05_1617pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7885 chars)
**Wall time**: 471.4s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals”

Scope of review
- Focus: methodology rigor, statistical validity, internal arithmetic consistency, error propagation.
- I read the entire manuscript, checked figures/tables/equations, and recomputed quoted statistics where possible from the numbers provided.

Overall assessment
The paper presents a large cross-match and a suite of null tests for environment-dependent spiral chirality. While the analysis is ambitious and much of the methodology is clearly laid out, I identified multiple internal numerical inconsistencies (sample sizes, σ predictions, Bonferroni thresholds), at least one impossible class size, a contradiction in the target-program split null test, and insufficient propagation of the catalog-level monopole uncertainty into the residual-significance statements. Some claims (e.g., χ2 p-values reported as <10−1000) are over-precise for the methods used. Several project-internal tags leak into the presentation.

Below is a detailed findings list with required fixes.

Findings

ESSENTIAL

P5-E1 (Section VII, page 9): Impossible per-class sample size in Phase 2 sweep
- Text: “The largest single-cell |σfrom half| across the entire sweep is 11.32 (filament at Rs = 10, λth = 0, n = 3,696,152).”
- Problem: The chirality-relevant matched sample is N = 791,635 (Table II context). A per-class n = 3,696,152 is impossible. This also underpins the “σpred ≈ −10” statement here.
- Required fix: Correct the sample size and recompute the quoted |σ| and its interpretation. If this σ refers to a different population (e.g., all DESI spectro rather than chirality-labeled spirals), state that explicitly, re-derive the statistic on the chirality-labeled sample, and ensure all sweep-cell σ/rs/threshold statements are computed on the same, clearly defined population.

P5-E2 (Section VI D c, page 7): V-Web filament bright/dark sample sizes exceed the class total
- Text: “filament bright (n = 416,701) σ = −2.80 vs filament dark (n = 21,203) σ = +2.85”
- Problem: The canonical V-Web filament class count is n = 408,187 (Table II). Bright + dark (416,701 + 21,203 = 437,904) exceeds the class total. Either different selection cuts are being used here or the numbers are incorrect.
- Required fix: Provide the exact sample definition used for these counts, ensure consistency with Table II, and recompute the bright/dark per-class results so that bright + dark (+ backup + other, if relevant) sum to the per-class total. Provide the exact n and fCW values used in the reported two-sample z-test.

P5-E3 (Section VI A, page 5): Incorrect σpred for filament from the Paper IV monopole
- Text: “predicting σpred(filament) ≈ −3.16 and σpred(cluster) ≈ −3.28”
- Problem: Using σpred = 2 ΔfCW √N with ΔfCW = −0.0026 and Nfil = 408,187 gives σpred ≈ −3.32 (not −3.16). The cluster value −3.28 is consistent.
- Required fix: Correct σpred(filament) to −3.32 and check downstream places where this predicted value is compared to measured σ. Ensure consistency with the later statement in VII A (page 9) that lists cluster ≈ 3.27σ and filament ≈ 3.32σ.

P5-E4 (Sections V and VI–VIII, multiple pages): No propagation of Paper IV monopole uncertainty into residual-significance claims
- Text: Throughout, σpred = 2 ΔfCW √N uses ΔfCW = −0.0026 from Paper IV as a fixed constant; residuals |σobs − σpred| are used to argue “consistent with the monopole” vs “candidate signal” without accounting for the uncertainty on ΔfCW from Paper IV (quoted earlier as fCW = 0.4974 ± 0.000279, implying σ(Δf) ≈ 0.000279).
- Problem: The uncertainty on ΔfCW propagates linearly into σpred and into the σvs-monopole residuals, changing whether residuals are statistically compatible with zero. Treating Δf as fixed overstates the precision of the monopole-subtracted residual test.
- Required fix: Carry the Paper IV uncertainty on Δf into all σpred and σvs-monopole comparisons, and revise all “within 1σ” and “Bonferroni-threshold” statements accordingly. Provide error bars or confidence intervals on σvs-monopole that include both counting statistics and Δf uncertainty.

P5-E5 (Section VI D d, page 8): Inconsistent contingency-table sample size for bright/dark
- Text: “two-way contingency test (… four-by-two on nbright+dark = 811,609 spirals)”
- Problem: Earlier, the catalog-level program counts are bright n = 775,760 and dark n = 14,782 (Section VI D b), summing to 790,542 on the 791,635 chirality-relevant sample (with backup + other making up the remainder). The 811,609 figure is not explained and does not match earlier totals.
- Required fix: Specify the exact sample used in this contingency test, reconcile the count with earlier totals, and correct the χ2 inputs if necessary. Provide the cross-tab (counts) so the χ2 = 4932 value is reproducible.

P5-E6 (Section XI, page 17): Contradiction between target-class split “null” and earlier bright/dark difference
- Text: “target-class split (BGS vs. LRG-ELG-QSO) with BGS-only CW fraction within ±0.001 of LRG-ELG-QSO. No test produces a > 3σ residual…”
- Problem: In Section VI D b (page 7), bright (BGS-dominated) has fCW = 0.4970 and dark (LRG/ELG/QSO) has fCW = 0.5051, a difference of 0.0081 (0.81 percentage points), which is not “within ±0.001.” The two statements are irreconcilable as written.
- Required fix: Resolve the contradiction. If the Section XI statement refers to a different subset or a different conditioning (e.g., after monopole subtraction, or restricted to some class), state that explicitly and present the corresponding numbers. Otherwise, correct the claim in Section XI and revise any conclusions that depend on it.

P5-E7 (Section VII A, page 9): Mis-stated Bonferroni-9 threshold
- Text: “…zero produces a per-class |σvs monopole| residual above the Bonferroni-9 (α = 0.05) threshold |σ| ≈ 3.02.”
- Problem: For a two-sided Bonferroni family K = 9 at α = 0.05, the threshold is z such that 2(1 − Φ(z)) = α/K = 0.005555…, i.e., z ≈ 2.78, not 3.02. 3.02 corresponds to α/K ≈ 0.0025 (as used earlier for K = 4, α = 0.01).
- Required fix: Correct the Bonferroni-9 threshold and re-assess any “exceeds/does not exceed” conclusions that use the incorrect 3.02 cutoff.

MAJOR

P5-M1 (Section VI D b–c, page 7): Insufficient detail for the “|z| ≈ 3.4σ” bright-vs-dark two-sample test
- Text: “…The joint two-sample z-test on the bright-vs-dark fCW difference is |z| ≈ 3.4σ on the filament class…”
- Problem: The per-class bright/dark counts are internally inconsistent with Table II (see P5-E2), and no explicit formula, counts, or fCW values are provided to reproduce z. Given the earlier contradictions, this test is presently not reproducible.
- Required fix: Provide the exact nCW/n, fCW, and standard-error formula used in the two-proportion comparison, on a sample definition that is consistent with the class totals. Report the exact z and p-value with sufficient significant digits.

P5-M2 (Multiple sections/figures; e.g., Figure 4 caption and Section X, page 16): Project-internal tags “P5” and “P4” appear in the body and figure titles
- Text examples:
  - Figure 4 title: “P5 HEALPix per-pixel σfrom half …”
  - Section X: “This is a strong robustness result: the P5 headline null …”
  - Section VIII F: “…subtracting the P4-monopole…”
- Problem: These are internal project identifiers/version tags and should not appear in the paper body or figure titles. The paper can refer to “this work” and to “Paper IV” in citations, but “P5 headline” is not standard.
- Required fix: Remove “P5”/“P4” labels from figure titles and prose, or replace with “this work” and “Paper IV” (as a normal citation).

P5-M3 (Section IX A, page 15): Inapt comparison of V-Web “cluster volume fraction” to Tempel “cluster spiral fraction”
- Text: “…the V-Web cluster volume fraction (1.0%) is much smaller than the Tempel cluster spiral fraction … 5.3%.”
- Problem: Volume fraction and galaxy fraction are not directly comparable. This can mislead readers about classifier differences.
- Required fix: Either compare like with like (e.g., V-Web galaxy fractions per class within the matched sample vs Tempel galaxy fractions), or explicitly state that one is a grid-cell volume fraction and the other is a galaxy fraction and avoid drawing quantitative conclusions from that particular number pair.

P5-M4 (Section V, page 4; multiple uses): Use of NMC = 1000 for permutation nulls while quoting precise p-values
- Text: e.g., Table V p-values 0.607, 0.135, 0.413.
- Problem: With NMC = 1000, the Monte Carlo resolution is ≈ 0.001. Reporting three-decimal p-values is fine, but later claims that rely on close calls to thresholds (e.g., Bonferroni-corrected) should acknowledge the Monte Carlo resolution. (This is generally okay here, but please state the resolution in the Methods.)
- Required fix: Add a brief statement acknowledging the p-resolution limit of NMC = 1000 and round p-values consistently.

P5-M5 (Section VIII A, page 10): Claim of “RSD-immune” for DESIVAST membership without quantitative bound
- Text: “The DESIVAST primary path is essentially RSD-immune at the level relevant to this work…”
- Problem: The qualitative argument is reasonable, but a quantitative bound (e.g., upper bound on the fraction of galaxies moving across the void boundary given σv/(aH) and Reff distributions) would strengthen the claim and align with the otherwise quantitative tone.
- Required fix: Provide a back-of-envelope quantitative estimate (or a reference) bounding the RSD-induced misclassification rate for void membership at z ≤ 0.24 and discuss its impact on ∆fCW at the measured precision.

MINOR

P5-m1 (Abstract and Section VII, page 8–10): Unit consistency for ranges in percentage points
- Text: “never exceeds 0.22 percentage points (max 0.0022 …)”
- Problem: Good to include both notations, but ensure consistency throughout (always provide both “pp” and the decimal).
- Required fix: Standardize to “pp (decimal)” once per context.

P5-m2 (Section VI A, page 6): Void-bin 95% CI not shown where referenced
- Text: “The 95% binomial credible interval is fvoid ∈ [0.435, 0.530]”
- Problem: Nice to include; please add the exact credible-interval method (Jeffreys already stated) and numeric endpoints in the panel/figure or as a footnote for traceability.
- Required fix: Either annotate Figure 2 with CI values or add a footnote/table entry.

P5-m3 (Section V, page 4): Explicit formula for σvs-monopole not given
- Text: σvs-monopole appears later (Table X), implicitly as 2(fclass − fP5)√N.
- Problem: Define σvs-monopole explicitly once in Methods to avoid ambiguity.
- Required fix: Add σvs-monopole ≡ 2(fclass − fP5)√N (and state the fP5 used) to Section V.

P5-m4 (Section VI C–D, pages 6–7): Logistic model covariates not fully defined
- Text: “…logistic regression of CW indicator on {z, |sin δ|, cos α, confidence}…”
- Problem: “confidence” is not defined in the Methods (is this the classifier softmax or another score?).
- Required fix: Define “confidence” precisely and its range.

P5-m5 (Section VI D d, page 8): Over-precise p-value wording
- Text: “p < 10−1000”
- Problem: This is effectively zero for practical purposes and suggests unnecessary precision.
- Required fix: Replace with “p ≪ 10−10” or “p effectively zero for double-precision” (or give the exact p from a standard library if computed with high-precision, but there is no need for 10−1000).

P5-m6 (Section VIII E, page 12): Slight rounding mismatch in “max class-to-overall bright-fraction deviation 1.5 pp”
- Text: Class bright fractions {0.981, 0.962, 0.966, 0.989} vs overall 0.978; the largest deviation is 1.6 pp (0.962 vs 0.978), not 1.5 pp.
- Required fix: Correct to 1.6 pp or provide the precise unrounded values.

P5-m7 (Figures 3–7): Ensure axes/labels/units are explicit
- Problem: From the captions, most axes/units appear correct; please ensure the right-panel of Figure 3 labels σfrom half with the Bonferroni-5 α = 0.01 thresholds clearly and that all Mollweide maps include coordinate system and NSIDE.
- Required fix: Visual confirmation/update as needed.

NITS

P5-n1 (Throughout): Occasional stylistic redundancy
- Examples: repeated phrases such as “catalog-anchored re-projection,” “headline null,” etc.
- Fix: Light edit for concision.

P5-n2 (References): Minor typos/diacritics
- Check author accents and journal abbreviations for uniformity, but overall looks fine.

P5-n3 (Typographic): Hyphenation artifacts
- Likely PDF rendering artifacts; no action needed if typeset cleanly.

Length
- The paper is 20 pages. Given the breadth of cross-checks, this is acceptable for PRD if the essential/major issues are resolved. If the authors reduce duplication (particularly in narrative descriptions repeated across sections), it could likely be trimmed by ~2–4 pages without loss.

Additional cross-checks I performed
- Recomputed σfrom half from fCW and n for Table II: all consistent.
- Verified the 1.98 pp range in Table II: correct.
- Verified DESIVAST void/non-void σ in Table VII from n and f: consistent.
- Verified Table X σvs-monopole from fclass − fP5 and n: consistent.
- Verified density-quintile σpred ≈ −2.07 for N = 158,327: correct.
- Verified Bonferroni-4 thresholds: α = 0.05 gives ≈ 2.50; α = 0.01 gives ≈ 3.02: consistent with Eq. (2).
- Identified inconsistencies detailed in ESSENTIAL items above.

## Summary recommendation
MAJOR REVISIONS

Justification: The manuscript contains multiple internal inconsistencies affecting central quantitative claims (impossible per-class sample size in the Phase 2 sweep; mismatched per-class bright/dark counts; incorrect σpred in a headline comparison; a mis-stated Bonferroni threshold; and a direct contradiction in the target-class split “null” vs earlier reported differences). Additionally, the analysis treats the Paper IV monopole as fixed without propagating its uncertainty into residual-significance statements. These issues must be corrected and the affected inferences re-evaluated before the paper can meet PRD standards. The overall approach is promising, but the numerical and methodological corrections listed above are necessary.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS AFTER SECOND PASS

ESSENTIAL

P5-E8 (Section II, page 2): Misstated significance of Paper IV global mixture
- Text: “Paper IV … establishes the global mixture … 0.4974 ± 0.000279, consistent with parity at ∼ 1σ.”
- Problem: The deviation from 0.5 is 0.0026; 0.0026/0.000279 ≈ 9.3σ, not ∼1σ. If the intent is “consistent after treating it as classifier bias,” that still does not make the quoted statistical statement correct.
- Required fix: Correct the significance (∼9.3σ away from 0.5 on statistical errors), or explicitly state that this offset is interpreted as a classifier monopole and not a cosmological signal, while keeping the correct statistical discrepancy.

P5-E9 (Section VIII F, page 12): Impossible “env-labeled” superset larger than chirality-relevant sample
- Text: “fP5CW = 0.4972 (−5.07σ on n = 812,793 env-labeled spirals … 21,158-row excess over the 791,635-spiral headline subsample…)” and “The per-class nCW values on the 812,793 superset sum to 404,111…”
- Problem: The chirality-relevant matched sample is 791,635 (Table I). You cannot have 812,793 CW/CCW-labeled spirals. The explanation (“relaxed env-label confidence”) does not resolve this contradiction because it addresses the environment label, not chirality labels.
- Required fix: Reconcile the counts. If 812,793 includes objects outside the 791,635 chirality-relevant set, name that set explicitly and explain how they acquired CW/CCW labels. Otherwise correct the number and recompute fP5CW and −5.07σ on the valid sample.

P5-E10 (Section VIII B, page 11): Unsafe k-NN shortcut for void membership
- Text: “point-in-sphere test … via a k = 20 nearest-neighbour KDTree query on the hole centres, sufficient given the 24 Mpc/h maximum hole radius.”
- Problem: A fixed-k query is not guaranteed to return all sphere centers within 24 Mpc/h in locally crowded regions; a containing sphere can be missed if >20 centers lie within 24 Mpc/h. This risks false negatives in void membership and biases nvoid and ∆fCW.
- Required fix: Replace k-NN with a radius search (query_ball_point) at 24 Mpc/h (or the algorithm-specific maximum) or prove an upper bound on local hole-center density that guarantees k=20 suffices. Re-run the membership and update Table VII/VIII if counts change. Also clarify the “24 Mpc/h maximum hole radius” vs the later “maximal-void Reff up to 32 Mpc/h” by distinguishing “holes” vs “maximal voids.”

P5-E11 (Eq. 1, Section V, page 4): Inconsistent/mis-parenthesized σpred formula
- Text: “σpred = ΔfCW/0.5/√N = 2·ΔfCW·√N”
- Problem: As written, Δf/0.5/√N equals 2Δf/√N, not 2Δf√N. The left-hand expression is dimensionally/numerically inconsistent with the right-hand expression and with later uses.
- Required fix: Correct to σpred = (ΔfCW/0.5)·√N = 2ΔfCW√N and ensure all computed σpred values used this form.

MAJOR

P5-M6 (Section VIII F and Figure 4 vs Methods): Unexplained change in valid-pixel counts at NSIDE=32
- Text: Figure 4 caption: NSIDE=32, npix=3,303; Section VIII F: “distribution … across the 1,821 valid pixels”.
- Problem: The drop from 3,303 to 1,821 “valid pixels” is not defined (minimum-per-pixel count? additional masking?). This affects the σ-distribution moments reported.
- Required fix: State the per-pixel minimum-count threshold(s) used in each analysis, justify them, and make the per-pixel counts reproducible. If thresholds differ across analyses, say so explicitly.

P5-M7 (Section IX A, page 16): Filament concordance arithmetic from displayed numbers
- Text: “filament like vs filament: 0.026 pp (✓ within spec)”
- Problem: Using the f values shown (0.4982 vs 0.4980) gives 0.0002 = 0.02 pp, not 0.026 pp. The difference is tiny but the manuscript emphasizes sub-0.2 pp precision.
- Required fix: Either use the numbers actually displayed (0.02 pp) or report the underlying more precise values used and match them in the plots.

P5-M8 (Section VI B, page 6): Mis-specified logistic model for sky-position dependence
- Text: “logistic regression of the CW indicator on {z, |sin δ|, cos α, confidence}…”
- Problems:
  - RA modeled with only cos α, which imposes a phase and prevents detection of a general dipole in RA unless aligned to that phase. Standard practice is to include both sin α and cos α.
  - No standard errors/t-values are reported for coefficients (you report only point estimates).
  - “confidence” covariate is undefined (see earlier minor P5-m4 in your first review).
- Required fix: Include both sin α and cos α (or equivalently a 2D harmonic basis), define “confidence,” and report coefficient uncertainties. If results change, update the redshift/sky-dependence conclusions.

P5-M9 (Section VI C, Figure 3, page 7; Methods Section V): Declared primary LEE control (empirical max-stat) not used/reported for density-quintile scan
- Text: Methods state the empirical max-stat permutation null is primary; Figure 3 and text use Bonferroni thresholds only for the density-quintile scan.
- Problem: Inconsistent with the stated primary LEE control; also no pLEE is reported for the density-quintile scan.
- Required fix: Report the empirical max-stat pLEE for the density-quintile scan (NMC=1000), or state why Bonferroni is sufficient in this case and revise the Methods to reflect actual practice.

P5-M10 (Section VII, page 8): Typo/ambiguity in sweep description
- Text: “sweep over nine cells Rs ∈ {10, 25, 50} Mpc/h × Ngrid = 256 × λth ∈ {0.0, 0.1, 0.3}”
- Problem: Reads as if “Ngrid = 256 × λth”; likely a typesetting error for “Ngrid = 256^3; λth ∈ {…}”.
- Required fix: Fix the notation to avoid confusion.

P5-M11 (Sections VIII B vs VIII E): “24 Mpc/h maximum hole radius” vs “maximal-void Reff up to 32 Mpc/h”
- Problem: These appear contradictory without context. In VoidFinder, “holes” (spheres) differ from “maximal voids”; radii ranges are different.
- Required fix: Add one sentence clarifying that the 24 Mpc/h cap applies to interior hole spheres, while maximal-void effective radii extend to ~32 Mpc/h, and that the membership test in VIII B uses holes.

MINOR

P5-m8 (Section V, page 4): Mixed terminology “exact binomial 95% credible interval”
- Problem: “Exact” usually refers to Clopper–Pearson confidence intervals; Jeffreys intervals are Bayesian credible intervals. Mixing “exact” with “credible” is confusing.
- Required fix: Use consistent terminology: e.g., “95% Jeffreys binomial credible intervals.”

P5-m9 (Section VI B, page 6): Logistic regression reporting
- Problem: Only point estimates are given (“z-coefficient 0.0059 … intercept 0.000652”), with no standard errors or sample size. Units/scale of coefficients are unclear.
- Required fix: Report standard errors (or z/t-scores), sample size, and clarify scaling.

P5-m10 (Section VIII F, page 13): Per-pixel σvs-monopole distribution sample definition
- Problem: The phrase “on the same matched-spiral catalog” is ambiguous given multiple sample definitions elsewhere (e.g., 791,635 vs 812,793).
- Required fix: State explicitly which sample and any per-pixel count threshold were used for the 1,821-pixel σvs-monopole distribution.

P5-m11 (Methods, Section V): RNG/version reproducibility
- Problem: “NumPy default rng” is version-sensitive; only the seed is specified (version given later in Appendix).
- Required fix: Add the NumPy version used to Methods or explicitly point to the pinned environment in the companion repository.

P5-m12 (Throughout): Unit formatting for “pp”
- Problem: Occasionally “0.22 percentage points (0.0022)” vs “0.22 pp” appear without the decimal in the same sentence.
- Required fix: Standardize to “X pp (Y in fraction)” on first mention per context, as you already do in some places.

If the authors address both the earlier set of issues and the additional points above (particularly E8–E11), the manuscript’s numerical and methodological consistency will be substantially improved.