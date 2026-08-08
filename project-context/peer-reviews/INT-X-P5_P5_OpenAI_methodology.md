# P5 INT-X-P5 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` md5=e446dfce pages=33
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5313 chars)
**Wall time**: 575.9s

---

Referee report on P5 (PRD methodology)

Scope of this review
I read the entire manuscript, all figures, tables, equations, captions, and appendices. I re-computed every scalar appearing in the abstract and conclusions from values given in the body and checked internal arithmetic, null-statistic usage, dimensional consistency, and multiple-testing handling. Below I list all findings, each with an ID, location, problem, and the required fix. Classifications: ESSENTIAL (must fix for acceptance), MAJOR (substantial revision), MINOR (addressable during revision), NIT (cosmetic).

Findings

P5-E1 (ESSENTIAL)
- Location: §VIII A, p. 17 (middle), “one-sided 95% binomial upper bound… 1 − 0.051/6 = 39% (the standard one-sided Clopper–Pearson bound 1 − α1/n…)”
- Problem: Typographical/notation error. The Clopper–Pearson upper bound for 0 successes in n trials is 1 − α^(1/n), not “1 − 0.051/6”. The current text looks like division, not exponentiation. Although the numerical 39% is correct (0 successes, n = 6 gives 1 − 0.05^(1/6) ≈ 0.393), the formula as written is wrong.
- Required fix: Replace “1 − 0.051/6” with “1 − α^(1/n)” and (optionally) show the numerical evaluation 1 − 0.05^(1/6) ≈ 0.393. Clarify that α = 0.05, n = 6.

P5-E2 (ESSENTIAL)
- Location: §IV A Algorithm, p. 5 (first paragraph), and footnote a on p. 3; multiple places where “earlier preprint versions…” and artifact/backwards-compatibility labels are discussed.
- Problem: Version-history and preprint-process language (“earlier preprint versions used the ‘V-Web’ label loosely…”, “artifact filename… retained for backward compatibility”). PRD papers must stand alone; internal development history and engineering labels do not belong in the main text.
- Required fix: Remove all version-history/preprint-process language from the body and footnotes. If a nomenclature clarification is needed, state it neutrally without referring to earlier drafts (e.g., “We implement the Hahn 2007 tidal-tensor (‘T-Web’) classifier. Our software module names use ‘vweb’ for historical reasons, but all results here use the tidal-tensor formulation.”).

P5-E3 (ESSENTIAL)
- Location: §V B “Primary vs. secondary analysis paths (pre-registration caveat)”, pp. 7–8, and Abstract first paragraph (“primary designation is declared post-hoc…”).
- Problem: The “primary” analysis path (DESIVAST-anchored void test) is designated post hoc. Although the paper is commendably transparent about this, PRD methodology standards require that the inferential framework control multiplicity across the whole analysis tree, not only within the later-declared “primary family.” Restricting Bonferroni control to the five DESIVAST estimators after designating them primary post hoc is not, by itself, a sufficient guard against forking-paths across the many explored classifiers and stratifications.
- Required fix: Either (i) remove the “primary/secondary” labeling, present all analyses as exploratory, and control the family-wise error across the full pre-declared set of tests reported in Table II (e.g., a global max-stat permutation across all test families; or a hierarchical FWER procedure clearly specified); or (ii) move the DESIVAST analysis to be the sole pre-specified estimand, and demote all other analyses to descriptive with no p-values or σ-thresholds, explicitly stated as such throughout, including in the Abstract. In either case, provide a single, explicit multiplicity control statement covering the complete set of inferential claims made in the paper.

P5-E4 (ESSENTIAL)
- Location: Appendix A (pp. 30–31), “Toy EFT mapping…”
- Problem: Conceptual clarity and dimensional analysis. The proposed operator L_parity ⊃ g_ϕ (∇iϕ)(∇iρ/ρ_bg)(L̂ · ∇̂ρ) is presented as a “parity-odd pseudoscalar” regarding the L̂ · ∇̂ρ factor, but the overall Lagrangian density must be a scalar under rotations; the text does not clearly state the parity of the full operator, nor its mass dimension, nor the dimension of g_ϕ. It is easy for readers to misunderstand whether the full term is scalar (pseudoscalar × pseudoscalar) or pseudoscalar. The subsequent scaling estimate |g_ϕ ∇ϕ|/H0 ≲ 10^−2/⟨|Δρ/ρ|⟩ lacks a derivation of units.
- Required fix: (i) State explicitly the transformation properties of each factor under parity, and confirm that the product forms a rotational scalar suitable for inclusion in a Lagrangian density (or, if the intent is to include a pseudoscalar density to break parity, say so explicitly). (ii) Provide the mass-dimension counting of each factor and of g_ϕ; specify the system of units. (iii) Justify the scaling bound with a short derivation, including how the observable Δf_CW maps to this operator, or move the whole Appendix to a clearly labeled, non-inferential “outlook” without quantitative bounds. As written it risks over-interpreting the data with an under-specified toy model.

P5-M1 (MAJOR)
- Location: §VI D (pp. 10–12) and §VII A (pp. 15–16)
- Problem: Use of “σ_obs − σ_pred” as if it were a z-statistic. In several places you compare σ_obs − σ_pred to Bonferroni z-thresholds (e.g., “below the Bonferroni-4 threshold |σ| = 2.50,” Table VII column “max |σ_obs − σ_pred|” vs |σ|_Bonf). σ_obs is a z-statistic; σ_pred is a predicted mean in the same units. Their difference is not, in general, a standard-normal variate, and using the same |σ| thresholds can mislead.
- Required fix: Rephrase these passages to treat σ_obs − σ_pred as a descriptive residual only. Where you require an inferential statement, use either (a) a one-sample test against the matched-sample monopole f_P5 (as you do in Table XII), or (b) an empirical permutation for the max-statistic, which you already provide (p_LEE). Remove comparisons of σ_obs − σ_pred to Bonferroni z-thresholds.

P5-M2 (MAJOR)
- Location: §VI D (pp. 11–12), “tracer-program stratification” and two-sample z tests; also §XI Table XV.
- Problem: Two-sample z-tests are computed at the row level on overlapping bright/dark splits (the same galaxy can contribute to both splits under different programs), violating independence. You note this caveat, but still quote |z| ≈ 2.1. For PRD, either use disjoint samples or a matched-pairs (e.g., McNemar) framework.
- Required fix: Recompute program-split tests on disjoint unique-galaxy sets (or explicitly provide a paired analysis using only objects observed under both programs, with a matched-pairs test). Do not quote row-level two-sample z-scores as inferential if independence is violated.

P5-M3 (MAJOR)
- Location: Throughout (Abstract; §II; §XI; Conclusions)
- Problem: Dependence on “Paper IV (in preparation)” for load-bearing context (global monopole amplitude; imaging-leg systematics). While you do measure the matched-sample monopole internally, you still rely on Paper IV to justify the origin of the monopole and related systematics.
- Required fix: Make the manuscript fully stand-alone. Where a quantity is needed (e.g., the monopole amplitude), use only values measured within this paper’s samples (f_P5 = 0.49719) and rephrase any reliance on “Paper IV” as context, not as support. Remove any claims about Paper IV’s dipole constraints unless absolutely necessary, or cite a public preprint with stable identifiers.

P5-M4 (MAJOR)
- Location: Data/code availability, Appendix C (p. 31)
- Problem: You state “A DOI-minted archival snapshot accompanies journal submission,” but no DOI is provided in the manuscript. PRD requires long-term, citable deposits for data/code critical to reproduction.
- Required fix: Include the DOI (and version tag/commit hash) for the archived repository snapshot in the paper. Confirm that all artifacts [A1]–[A30] referenced are present in that DOI’d snapshot.

P5-M5 (MAJOR)
- Location: Overall length and presentation (33 pages main text with many asides)
- Problem: The paper’s main scientific contribution is a well-executed null on environment dependence, with an important DESIVAST re-projection. However, the manuscript is overly long for the claimed result, with many internal-engineering asides and repeated caveats that could move to Supplementary Material.
- Required fix: Condense to ≤ 22–24 manuscript pages. Keep: data description, T-Web method, DESIVAST void re-projection, the core null tests (χ^2 homogeneity, Phase-2 robustness), and the RSD/selection-function stress tests. Move: extended sky-scan permutations, repeated restatements of the monopole caveats, and long per-program digressions to an online supplement.

P5-M6 (MAJOR)
- Location: §IX A (pp. 22–24), selection-function corrected rebuild
- Problem: You state that completeness-weighting drastically reshapes class volume fractions (void fraction 17.6% → 0.75%), with only 26.6% of matched spirals retaining class labels, yet inferential statements remain the same. This is a strong—and important—result but is currently only summarized in prose.
- Required fix: Add a compact table reporting per-class n and f_CW before/after completeness weighting (for the low-z window where the randoms are applicable) so the reader can verify that the chirality null persists despite the dramatic reclassification.

P5-Min1 (MINOR)
- Location: Abstract and §VI A (p. 8), Table III
- Problem: Range across classes “1.98 percentage points” is correct (0.5034 − 0.4836 = 0.0198), but you immediately juxtapose σ_from-half values of different bins (e.g., −2.61 vs −4.66). Although you have an earlier caveat that σ scales as √N, the Abstract would benefit from an explicit reminder at that juxtaposition.
- Required fix: In the Abstract sentence that lists per-class σ values, add “(σ scales as √N; not comparable across classes).” Alternatively, omit σ’s from the Abstract and report only f_CW and the omnibus χ^2 p-value.

P5-Min2 (MINOR)
- Location: §VIII B / Table VIII (p. 18–19)
- Problem: You alternate between n_void = 56,981 (k=20 KDTree) and 57,081 (exact). This is explained in the text, but scattered references in the Abstract and body could confuse readers.
- Required fix: Choose one canonical n_void for the manuscript (preferably the exact value) and relegate the other to a parenthetical (“k = 20 approximation moves membership by 0.18% with no change in conclusions”).

P5-Min3 (MINOR)
- Location: §IV A step 4–5 (p. 5)
- Problem: Mask-building details are clear, but the box side 6,634 h^−1 Mpc and the implied cell size 25.9 h^−1 Mpc appear without stating how the bounding box is constructed from the survey shell (e.g., min/max of comoving Cartesian coordinates).
- Required fix: Add one sentence clarifying how the DR1 bounding cube is defined (e.g., min/max of χ·(cosδ cosα, …) over the z-window), to make the 6,634 value reproducible.

P5-Min4 (MINOR)
- Location: §VI D, Table V caption (p. 11)
- Problem: The caption mixes log10 notation and linear density verbally; this is correct but could be crisper to avoid misreading.
- Required fix: Add “Values 0.90–2.21 are log10(1+δ_smooth); in linear units these correspond to 8–162 times the cube-mean cell density.”

P5-Min5 (MINOR)
- Location: §X (pp. 26–27)
- Problem: The EDR-overlap ASTRA vs. T-Web per-galaxy disagreement is large and important for interpreting classifier dependence; however the specific per-class f_CW numbers for the T-Web-on-overlap are not printed (only n).
- Required fix: Add a small table (or footnote) of f_CW (with Jeffreys 95% intervals) for ASTRA argmax, ASTRA entropy-weighted, and T-Web-on-overlap, so the reader can see the near-identity of f_CW across classifiers.

P5-Min6 (MINOR)
- Location: §IX C, concurrent-literature comparison (p. 25–26)
- Problem: The reported T-Web volume fractions from Ref. [11] are compared qualitatively. Given the methodological differences, this is acceptable, but please state explicitly whether your λ_th and smoothing differ from theirs (and if so, how that impacts the void/knot fractions).
- Required fix: Add one sentence noting that both works use a T-Web classifier but with different smoothing, λ_th and volume geometry (periodic cube vs. survey shell), which largely explains the void/knot differences.

P5-N1 (NIT)
- Location: Throughout (e.g., §VI F p. 21)
- Problem: Occasional hyphenation/typography (e.g., “monopole- subtraction” vs. “monopole subtraction”; superfluous spaces).
- Required fix: Copy-edit for minor hyphenation/spacing consistency.

P5-N2 (NIT)
- Location: Eq. (1) p. 6 and surrounding
- Problem: You define Δf_CW as “fractional deviation from 0.5,” but later also use f_P5 − 0.5. Both are fine, but ensure consistent symbol usage in the immediate neighborhood of Eq. (1) to avoid confusion.
- Required fix: Add an explicit line “We use Δf_CW ≡ f_CW − 0.5 throughout; where we reference the matched-sample monopole f_P5, we set Δf = f_P5 − 0.5.”

Arithmetic and consistency audit (selected checks)

- Table III counts/ratios and σ_from-half all check:
  • Void: 207/428 = 0.4836; σ = (207 − 214)/(0.5√428) = −0.68.
  • Wall: 3359/6673 = 0.5034; σ = +0.55.
  • Filament: 203,261/408,187 = 0.4980; σ = −2.61.
  • Cluster: 197,284/397,505 = 0.4963; σ = −4.66.
  • Range: 0.5034 − 0.4836 = 1.98 pp. Omnibus χ^2(3) = 3.55, p = 0.31 (consistent with counts in Appendix B).
- DESIVAST VoidFinder re-projection (Table VIII): f_void = 0.4964 (n=56,981) and f_non-void = 0.4971 (n=621,964); Δ = +0.0007 with SE = √[0.25(1/56981 + 1/621964)] = 0.00219; z = 0.31; two-sided p ≈ 0.76; 95% CI [−0.0036, +0.0050]. All consistent.
- Three-algorithm sphere-PIS contrasts (Table X) recompute to within rounding (SEs and z’s checked from nlz − n_void totals).
- Maximal-void HEALPix stratification (Table XI): “0 voids/pixel” bin n=378,511, f=0.4961 gives σ = 2(f − 0.5)√N ≈ −4.80 (text: −4.75), consistent within rounding.
- Phase-2 sweep p_LEE range 0.13–0.56 matches Table VII (resolved cells 0.13–0.48; unresolved 0.38–0.56).

Statistical-methods audit

- Distinction of σ_from-half, σ_vs-monopole, and permutation p-values is largely maintained. One caveat (P5-M1) is to avoid treating σ_obs − σ_pred as a test statistic with z-thresholds.
- N_MC = 1000 for permutation-based p-values is acceptable given the reported p ranges (≥ 0.089); MC SEs are correctly noted.
- Multiple-testing control: done per-family (Bonferroni-5 for DESIVAST primaries; Bonferroni-9 for Phase 2 grid). However, the post-hoc “primary” designation requires a global, pre-declared multiplicity treatment or rephrasing as exploratory (P5-E3).

Dimensional/algorithm checks

- T-Web implementation is internally consistent: Φ(k) = −δ/k^2; Tij(k) = +k_i k_j δ/k^2 under the stated Fourier sign convention; λ_th = 0; Gaussian smoothing at stated Rs; mask dilation iterations computed as ⌈Rs/cell⌉ + 1.
- Units: comoving distances converted to h^−1 Mpc by multiplying by h; sanity value χ(z=0.2) ≈ 570 h^−1 Mpc agrees with Planck18 cosmology.
- Grid resolution caveat for Rs = 10 Mpc/h is explicitly stated and excluded from robustness claims.

Abstract-last drift sweep

- The Abstract is, in general, consistent with the body. The following items need tightening per the findings above:
  • Explicitly state that the “primary” DESIVAST designation is post hoc but that all inferential claims control for multiplicity across the reported tests (after implementing P5-E3).
  • Avoid σ juxtaposition across classes without the √N caveat (P5-Min1).
  • Ensure the permutation p-value ranges and Phase 2 sweep statements match Table VII (they do).

Bibliography

- Checks out where needed. Please ensure that any “in preparation” references are replaced with stable preprints or removed from load-bearing claims (P5-M3).

Standalone-reader test

- With the above fixes, the paper can be read independently of “Paper IV”. As written, too many statements lean on “Paper IV (in preparation)”. Use only internal measurements for inferential claims.

Effect sizes

- Where contingency tests are reported, the paper already gives Cramér’s V for class × program. Good. For other large-n χ^2 results, consider stating the maximum class deviation in percentage points (you often do), which is helpful.

## Summary recommendation
MAJOR REVISIONS

The central result—a careful, well-powered null on environment-dependent spiral chirality, strengthened by a DESIVAST re-projection—is solid and the arithmetic is largely correct. However, several methodology and presentation issues must be addressed before this is suitable for PRD: (i) remove version-history prose and fix the Clopper–Pearson formula; (ii) resolve the post-hoc “primary” designation with a proper, global multiplicity framework; (iii) clarify the Appendix-A operator (parity and dimensional analysis); (iv) avoid treating σ_obs − σ_pred as a z-statistic; (v) correct the overlapping-samples z-test; and (vi) provide a DOI for the archived code/data snapshot. Condensing the manuscript will also improve clarity.

---

## PASS 2 — self-critique findings (what initial review missed)

P5—ADDITIONAL FINDINGS (fresh-eyes audit)

Scope of this addendum
I re-ran the A–J checklist you requested, focusing only on NEW issues not covered in my earlier report. Items are labeled in continuity with the prior numbering and classified as ESSENTIAL (E), MAJOR (M), MINOR (Min), or NIT (N).

New findings

P5-M7 (MAJOR)
- Location: Fig. 8 (top panel caption) vs §VIII E (body, first paragraph under “HEALPix sky-position stratification”)
- Problem: Inconsistency in the number of occupied HEALPix pixels for the DESIVAST maximal-void map at NSIDE=32. The Fig. 8 top caption states “npix = 3,303 occupied,” whereas the body text explicitly notes that the NSIDE=32 maximal-void map has 885 occupied pixels (contrasted with 297 at NSIDE=16). This looks like a copy-over from the chirality-pixel scan (NSIDE=32, npix=3,303 in Table VI) rather than the void map.
- Required fix: Correct the Fig. 8 caption to report the NSIDE=32 maximal-void occupied-pixel count actually used (885), or revise the body if 3,303 was in fact the value for the void map. State clearly, in both places, whether npix refers to the void map or to the chirality-pixel map to avoid cross-test confusion.

P5-Min7 (MINOR)
- Location: §V, just below Eq. (1) (denominator comparison paragraph)
- Problem: The factor stated for the ratio of standard errors uses 4 p0(1−p0), which is the square of the correct factor. The ratio of σ-denominators between using 0.5/√N and √[p0(1−p0)]/√N is 2√[p0(1−p0)], not 4 p0(1−p0). Numerically the mistake is tiny near p0≈0.5 (both ≈1), but the expression is dimensionally off.
- Required fix: Replace “the exact √[p0(1−p0)]/N denominator differs from it by a factor 4 p0(1−p0)” with “differs by a factor 2√[p0(1−p0)] (≈0.99998 at p0=0.4972).”

P5-Min8 (MINOR)
- Location: §VI D, “Logistic regression controlling for target program” (first sentence), and §VI A/Table XVII
- Problem: Population mismatch not explained. The bright+dark subset size is 811,609 rows in Table XVII and §VI A, but the logistic regression controlling for program is reported on 782,710 bright+dark env-matched spirals. The ~28.9k-row reduction is not justified (deduping? exclusions?). This affects reproducibility of the regression p-values.
- Required fix: State precisely why the regression sample is 782,710 (e.g., deduplication to unique TARGETIDs, removal of conflicts, covariate completeness, etc.) and ensure the counts in that model are traceable from the published artifacts.

P5-Min9 (MINOR)
- Location: §VIII F, paragraph beginning “At the HEALPix NSIDE=32 per-pixel level…”
- Problem: Mixed-scope pixel statistics appear closely together and could be misread. This paragraph quotes “1,791 valid pixels (≥200 spirals, full redshift range)” and then later compares to the deduplicated-parent recompute “1,769 valid pixels,” while Fig. 8 bottom (z≤0.24 only) shows 1,496 valid pixels. All are consistent once scopes are parsed, but the text does not explicitly restate the scope change near the numbers.
- Required fix: Add a short parenthetical after each pixel count clarifying the scope (full-z vs z≤0.24; row-level vs unique) to avoid inadvertent cross-comparison.

P5-Min10 (MINOR)
- Location: §IX A, “Redshift-shell selection-corrected classifier,” line reporting shell populations
- Problem: The statement “every shell ≥ 2.16×10^5 galaxies” is fine, but the corresponding per-class fCW before/after weighting (called for in my earlier M6) would help verify that the dramatic reclassification leaves fCW unchanged. Right now this key stress test lives mostly in prose.
- Required fix: Add a compact table with before/after per-class n and fCW for the low-z completeness-weighted stress test (z-range explicitly stated), aligning with the “void fraction 17.6% → 0.75%” prose. This will also close the loop for readers checking arithmetic on that strong claim.

P5-N3 (NIT)
- Location: §IV A footnote 1, “alternative convention χ[h−1 Mpc] = χ[Mpc]/h”
- Problem: The sentence is correct in form but could be misread as saying the divide-by-h convention is “not used here because it would imply 1246 h−1 Mpc at z=0.2.” The numeric example (843/0.6766=1246) is arithmetically correct but may confuse readers since many codes report χ in h−1 Mpc using that very convention. The “not used here” phrasing reads like a dismissal of a common convention rather than a choice of one of two equivalent parameterizations.
- Required fix: Rephrase to: “Two equivalent conventions exist; we adopt multiply-by-h when reporting values in h−1 Mpc (e.g., 843 Mpc → 570 h−1 Mpc). The alternative divide-by-h convention (843 Mpc → 1246 h−1 Mpc) is not used in this paper.” This keeps the arithmetic and avoids implying one is improper.

Explanation
- I did not repeat issues previously flagged (E1–E4, M1–M6, Min1–Min6, N1–N2). The new items arose from a close read of figure captions vs text (M7), a dimensional check around Eq. (1) (Min7), reconciliation of sample sizes in the regression (Min8), and consistency/clarity of pixel-scope declarations (Min9). I also suggest a clarifying table for the strong completeness-weighting claim (Min10) and a wording polish on the h−1 Mpc unit note (N3).

If you address these, together with the earlier required changes, the manuscript’s rigor and reproducibility will be materially improved.