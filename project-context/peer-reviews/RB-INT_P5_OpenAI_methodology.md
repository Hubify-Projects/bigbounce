# P5 RB-INT — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` md5=24506842 pages=34
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7162 chars)
**Wall time**: 465.8s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test…”

Scope of review
I evaluated methodology rigor, statistical validity, dimensional analysis, internal arithmetic, and consistency between abstract/conclusions and body. I recomputed the numerical claims that can be checked from the provided counts and equations, and audited figures/tables for consistency.

Overall assessment
The analysis is technically careful in many places, and most arithmetic checks out. However, several issues prevent acceptance at PRD in its current form. The heaviest blockers are (i) reliance on an “in preparation” Paper IV for the load-bearing chirality labels and for the catalog-wide monopole, without a citable peer-reviewed source or sufficient in-paper method/validation summary; (ii) pervasive dependence in the main text on internal artifact IDs and repository paths; and (iii) a few clarity/notation issues and one formula typo that must be corrected. Below I itemize all findings with required fixes.

Findings

ESSENTIAL

P5-E1
Section III A–B, pp. 4–5; Sec. II, p. 3; Abstract
Problem: Load-bearing dependence on “Paper IV [3] (in preparation; posted concurrently)” for (a) the per-galaxy CW/CCW labels used in every analysis; and (b) the catalog-wide monopole ∆fCW = −0.0026 that underpins the σpred baselines throughout. The paper asserts the catalog is public on HuggingFace and “posted concurrently,” but there is no citable arXiv DOI for Paper IV, nor are the classifier architecture, training, validation metrics, selection biases, and label-quality diagnostics summarized here sufficiently for independent evaluation. PRD requires that load-bearing inputs be either fully documented in the paper or in a citable, accessible preprint/publication.
Required fix: Provide a citable reference (arXiv DOI) to Paper IV with a stable version, or include in this paper a self-contained Methods appendix summarizing the classifier: architecture, training data, augmentation strategy, confusion/quality metrics, label cleaning, known systematics (including the BGS selection-function residuals), and the exact definition of the “equivariant” label subset. Also provide a DOI (Zenodo) for the exact catalog release used here. Explicitly state that all results can be reproduced without consulting non-public material.

P5-E2
Throughout main text (e.g., footnote a on p. 3; Sec. IV A steps 4–12, pp. 5–7; Secs. VI–XIII); Appendix C–D
Problem: Extensive in-line dependency on internal “artifact” IDs and GitHub repository pathnames in the narrative (e.g., “[A3]”, “env finder/01 compute vweb.py”, “[A10] outputs/17 v0151 closure recomputes.json”), plus a “Reproducibility checklist” with a manuscript tag. This version-history/engineering metadata appears in the scientific body and is not standard for PRD. While data/code availability is welcome, the manuscript should remain scientifically self-contained; critical claims should not require clicking through internal artifacts to understand or verify.
Required fix: Move all artifact IDs, repository paths, run logs, and implementation notes to a dedicated Data/Code Availability section or Supplement, and keep only stable external DOIs/URLs in the main text. Where an argument in the main text depends on an artifact, duplicate the essential numbers/tables/definitions in the paper proper so the conclusions can be followed without off-paper material. Remove “manuscript tag v0.1.92-2026-06-29” and similar version-history language from the body (keep in a data-availability note if desired).

P5-E3
Sec. VIII A, p. 18 (Clopper–Pearson bound)
Problem: Typographical error in the one-sided 95% Clopper–Pearson upper bound formula for 0/6 successes. The text reads “1 − 0.051/6 = 39% (the standard one-sided Clopper–Pearson bound 1 − α 1/n …)”. “0.051/6” is not meaningful; what is intended is 0.05^(1/6).
Required fix: Correct to 1 − α^(1/n) with α = 0.05; numerically 1 − 0.05^(1/6) = 0.393.

P5-E4
Abstract vs. Sec. V terminology; multiple sections juxtaposing σfrom half, σpred, and permutation p-values
Problem: PRD requires that different test statistics not be conflated. While the paper generally distinguishes σfrom half, σpred (monopole-referenced expectation), and permutation-based pLEE, there are places where raw σ and permutation p-values are juxtaposed without repeating the “not directly comparable” caveat (e.g., Abstract’s condensed list of σ values by class and later references to permutation p-values; Sec. VII’s “largest single-cell |σfrom half| … is predicted, not measured” is good but the sentence prior uses per-cell range without re-stating non-comparability).
Required fix: Add explicit clarifying phrases wherever σfrom half values are discussed alongside permutation p-values or σpred to reiterate that they are not directly comparable test statistics. Ensure the Abstract includes one sentence explicitly stating that σfrom half values scale with √N and are only interpreted here via the monopole-subtracted residuals or permutation p-values.

MAJOR

P5-M1
Primary analysis designation; Sec. V B, pp. 7–8 and Abstract
Problem: The paper declares the DESIVAST void test as “primary” post hoc (no pre-registration), after surveying multiple classifiers and stratifications. While multiplicity is treated within families, PRD favors pre-specification of the primary estimand. The authors argue the primary choice does not drive the null, but this should be tightened.
Required fix: Clearly define the primary estimand and analysis plan up front (void vs non-void ∆fCW on DESIVAST, including which void definition is the main line, and the two-sample test used), and move the “primary/secondary” declaration to the end of the Introduction. State explicitly that all other analyses are secondary diagnostics. Make explicit which of the five DESIVAST estimators is the single main estimator (e.g., catalog-native GALZONE for V2-REVOLVER) and why; keep the others as robustness.

P5-M2
RSD treatment; Sec. XIII, pp. 29–30; Sec. VIII (RSD-bounded discussion), p. 17
Problem: The paper convincingly bounds sensitivity of their DESIVAST void membership test to line-of-sight displacements via a Monte Carlo, but the T-Web classification (the secondary path used heavily for descriptive checks) is stated to be “RSD-bounded only at the scalar-displacement level”, while the dominant effect for a tidal-tensor classifier is anisotropic. The current scalar heuristic and remarks are qualitative.
Required fix: Either (i) provide a quantitative bound on potential class-boundary flips induced by RSD in the T-Web run (e.g., via a Zel’dovich/BAO-like reconstruction rerun on a representative sub-volume or through an eigenvalue-shift perturbation analysis tied to the measured eigenvalue distributions), or (ii) demote all T-Web class-level descriptive statements that could be RSD-sensitive, clearly marking them as illustrative and not load-bearing, and move RSD-sensitive content to a Supplement. The Abstract must clearly state that the headline null is anchored entirely in the DESIVAST void re-projection (which you already do), and add one sentence that all T-Web statements are redshift-space descriptive only.

P5-M3
Overreliance on internal cross-references to companion papers; Sec. I–II, pp. 3–4; Sec. XII B, p. 29
Problem: Multiple forward-looking references (“Paper II,” “Paper III,” both in preparation) are used to situate the work in a program. These are not load-bearing here, but PRD discourages using unpublished “companion” claims as part of the argument structure.
Required fix: Remove or minimize references to unpublished companion manuscripts except for the strictly necessary pointing to Paper IV for labels (see E1). Any statements about implications for bounce/inflation beyond the bounds derived here should be framed without relying on the unpublished companions.

P5-M4
Style/length; entire manuscript (34 pages)
Problem: The paper is very long for its core contribution (a set of precise, well-designed null tests). Much of the engineering/provenance narrative (mask-dilation options, RNG stream confirmation, exact per-cell ranges, etc.) could be condensed without loss of scientific content.
Required fix: Reduce the main text length by moving engineering details and secondary diagnostics to an Appendix or Supplement. A target main text length of ~20–24 pages would be reasonable for PRD, preserving the Introduction, Data, Methods, Primary DESIVAST analysis, Key T-Web diagnostics, Limitations, and Conclusions. Keep the code/data availability but offload [A#] inventories to Supplement.

MINOR

P5-m1
Sec. IV A step 4, p. 5; footnote 1, p. 5
Problem: Unit convention explanation (multiply-by-h vs divide-by-h) is correct but the presentation is unusual and potentially confusing. Some readers expect “Mpc/h” instead of “h−1 Mpc”.
Required fix: Add a one-line reminder that values are expressed in h−1 Mpc (Mpc/h), and that numerically D[h−1 Mpc] = h × D[Mpc]. Optionally add a parenthetical check with a second z to reassure readers.

P5-m2
Sec. VI A, Fig. 3 caption, p. 10
Problem: The caption says “σfrom half scales as √n and is therefore not comparable across rows” (correct), but the figure plots bars with 95% intervals and shows σ in the text. Slight risk of misinterpretation without explicit pointer to monopole-subtracted residuals.
Required fix: Add a sentence to the caption pointing to Table XIII for monopole-subtracted residuals per class.

P5-m3
Sec. VI C, Table V, p. 11
Problem: The σpred values assume ∆fCW = −0.0026; elsewhere σvs monopole uses fP5 = 0.49719 (−0.00281). The paper notes this later, but a footnote here would help.
Required fix: Add a footnote to Table V clarifying that σpred uses ∆f = −0.0026 (Paper IV), whereas σvs monopole later uses the matched-sample monopole.

P5-m4
Sec. IX B, Fig. 9, p. 26
Problem: The left panel is the T-Web full-sample reference; the text compares like-for-like on overlap, but the figure could be misread as mixing full-sample and overlap.
Required fix: Add “reference only” to the left-panel caption and explicitly state that the quantitative comparison uses the overlap subset.

P5-m5
Sec. VIII E, Table XII, p. 20–21
Problem: The “0 maximal voids per pixel” bin is used as a proxy for being outside the DESIVAST footprint. The text later corrects using an explicit footprint restriction, but the initial proxy could be misinterpreted.
Required fix: Move the footprint-restricted retabulation result (now in Table IX footnote text) next to Table XII, and clearly state that the proxy-only interpretation was validated by the explicit footprint restriction.

P5-m6
Sec. VI D a (z-quartiles), p. 12
Problem: A quartile crosses the Bonferroni-4 raw |σ| threshold at α = 0.01, then is argued null after monopole subtraction (residual −1.50σ). That is fine, but readers may assume a formal test was performed on the residuals.
Required fix: Add a sentence clarifying that no separate formal multiple-testing correction was applied to the residuals; the residual comparison is descriptive relative to the catalog monopole.

P5-m7
Appendix B tables, pp. 31–32
Problem: Good to include exact counts. For completeness, add the row and column totals in each table to ease recomputation by readers.
Required fix: Append marginal totals to Tables XVII and XVIII.

NITS

P5-n1
Typos/formatting: multiple instances of missing spaces around symbols (e.g., “−0.68σfrom half”), and rare double hyphens.
Required fix: Proofread and correct spacing around σ symbols and minus signs.

P5-n2
Notation: “pp” for percentage points is used frequently; it is clear but spell out “percentage points” at first use in the Abstract and once in the main text.
Required fix: Define “pp = percentage points” at first appearance.

P5-n3
Minor numeric rounding: Table XIII filament σvs monopole computed from f = 0.4980 and fP5 = 0.49719 gives ~+1.03; the table shows +0.99. This is within rounding/discretization, but add an explicit note that σvs monopole uses exact integer counts and the exact fP5 carried to full precision.
Required fix: Add a note under Table XIII that σvs monopole is computed from exact counts (not from rounded f).

Arithmetic and consistency checks (spot audit)

- Table II counts and fractions are self-consistent; sums by leg equal the matched sample 2,232,212; chirality-relevant 791,635 splits into CW 393,592 and CCW 398,043.
- Table IV σfrom half recomputed from integer counts match the reported values: filament −2.61, cluster −4.66, wall +0.55, void −0.68.
- “Range across classes” 0.5034 − 0.4836 = 0.0198 = 1.98 pp: correct.
- Eq. (1): σpred = 2 ∆fCW √N: dimensionless and consistent; example N = 408,187 and ∆f = −0.0026 gives −3.32 as quoted in text.
- Five-quintile density test: N per bin = 158,327; σpred ≈ −2.07; observed σ per bin and residuals in Table V are consistent.
- Two-sample bright–dark difference (Sec. VI D b; Sec. XI): ∆f = 0.0081 with SE ≈ 0.00416 gives |z| ≈ 1.95: correct.
- DESIVAST void vs non-void (Table IX): ∆f = +0.0007; SE ≈ 0.00219 (two-sample binomial) gives z ≈ 0.31: correct. Footprint-restricted control ∆f = +0.0018; SE ≈ 0.00232; z ≈ 0.78: correct.
- Three-algorithm DESIVAST sphere-PIS contrasts (Table XI): differences ≤ 0.0019; z∆ values reproduce from counts.
- Cramér’s V = sqrt(χ²/n) for Table XVIII: sqrt(4933/811,609) = 0.078: correct.
- HEALPix p-values and max-|σ| values are compatible with the stated Bonferroni thresholds; no case below 0.05.
- Bonferroni thresholds Eq. (2) numerically correct for examples given.

Bibliography spot check
- Hahn et al. 2007, Cautun et al. 2014, Tempel et al. 2014, and Planck 2018 references look correct with appropriate arXiv/journal info. DESIVAST ApJ 982, 38 (2025) matches the cited DOI. The two 2026 preprints [11], [12] are appropriately labeled as preprints.

Abstract–body consistency (pattern-045)
- I traced each abstract scalar (sample sizes, σ, p-values, ranges, sweep results, DESIVAST contrasts, sky-stratification correlation) to tables/sections. All checked out numerically against the body. The Abstract makes clear the primary result is DESIVAST-anchored and that T-Web is a secondary cross-check; this matches Sec. V B.

Provenance (patterns 046/047)
- The paper claims “DOI-minted archival snapshot accompanies journal submission.” Ensure a stable DOI is provided at acceptance. The in-text [A#] artifacts should be moved out of the body (see P5-E2).

Uncomputed-quantitative-claims (pattern-048)
- Most qualitative claims are backed with numbers. Keep this standard; for RSD sensitivity to T-Web (P5-M2), add a quantitative bound or demote.

Standalone-reader test
- With Paper IV unavailable, a reader cannot independently assess chirality label quality. Fix per P5-E1.

Effect sizes
- Where χ² tests are reported, Cramér’s V is provided (good). Retain this.

Recommended page count
- Recommend compressing main text to ~20–24 pages by moving secondary diagnostics and engineering details to a Supplement.

## Summary recommendation
MAJOR REVISIONS

The statistical methodology is mostly sound, the arithmetic checks out, and the main conclusions are supported by the presented counts. However, acceptance at PRD requires (i) eliminating the dependency on an “in preparation” companion for the load-bearing chirality labels by providing a citable reference or a sufficiently complete in-paper methods/validation summary; (ii) moving internal engineering artifacts and version-history notes out of the main text; and (iii) addressing RSD handling clarity for the T-Web path (quantify or clearly demote). Fix the noted clarity and typographical issues, and consider condensing. With these addressed, the paper would meet PRD’s methodology rigor standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes audit)

ESSENTIAL

P5-E5
Sec. VIII B, Table IX; §VIII A (membership method)
Problem: The primary DESIVAST void-vs-non-void result in Table IX is reported using a k=20 KDTree point-in-sphere (PIS) approximation even though the paper shows this k is formally insufficient (up to 249 hole centers can lie within one max-radius; 28% of the low-z sample has >20 candidates) and the authors already executed an exact (k-unbounded) rerun. Although the exact rerun changes void membership by only 0.18% (100 galaxies) and leaves the verdict unchanged, the main table and text still present the approximate k=20 numbers as the headline.
Required fix: Promote the exact membership counts to the primary Table IX and in all abstract/body text that quotes nvoid and ∆fCW for the DESIVAST test; relegate the k=20 approximation to a robustness note. This avoids any appearance that the primary estimator rests on an acknowledged approximation.

P5-E6
Sec. VIII B–C, Table X (program split within DESIVAST z ≤ 0.24); nearby narrative
Problem: (i) The bright+dark subtotals listed for the non-void class (615,078 + 5,845 = 620,923) do not sum to the non-void total used in Table IX (621,964). The missing 1,041 entries are presumably “backup/other,” but this is not stated. (ii) The text says “98.8% of the z ≤ 0.24 spirals are in the bright program,” then immediately gives the void-subset ratio 56,477/56,981 = 99.1% as “nbright/nlz,” which can be read as contradicting the 98.8% statement.
Required fix: Add an explicit line in Table X (or its caption) indicating the counts for backup/other and state clearly that Table X shows only bright and dark, not their sum to the Table IX total. Rephrase the 98.8% vs 99.1% sentence to distinguish “overall z ≤ 0.24 matched spirals” from the “void-assigned subset,” and provide the overall bright/dark/other percentages (with counts) to remove ambiguity.

MAJOR

P5-M5
Sec. IV–VI and throughout: canonical T-Web vs selection-corrected T-Web
Problem: The paper documents a substantial radial-selection leakage in the canonical T-Web labels and presents a selection-corrected rebuild that collapses cross-class fCW range from 1.98 pp to 0.05 pp and yields a crisper omnibus null (χ² = 0.11, p = 0.99). Yet many descriptive T-Web results (figures/tables and narrative emphasis) still use the canonical labels affected by selection leakage, with the corrected run discussed later as a “stress test.”
Required fix: Either (i) make the selection-corrected T-Web run the default for all T-Web-based descriptive statements in the main text (retaining the canonical as a Supplement robustness variant), or (ii) prominently flag, at first use and in each figure/table that uses the canonical labels, that those T-Web results are selection-contaminated and are presented as illustrative only. Add a one-sentence reminder in the Abstract or Methods that all T-Web statements in the paper that use the canonical labels are “redshift-space and selection-shaped diagnostics,” while the headline DESIVAST result is selection-independent.

MINOR

P5-m8
Sec. VIII E, Fig. 8 and Table XII
Problem: The text stratifies by maximal voids per pixel at NSIDE = 16 (297 occupied pixels), while Fig. 8’s top panel visualizes NSIDE = 32 (885 occupied). Although you note this in the caption, the jump between resolutions mid-section is easy to miss.
Required fix: Add a short parenthetical in the main text right before Table XII explicitly reminding the reader that the figure uses NSIDE = 32 for visualization while the table uses NSIDE = 16 for the stratification statistic, and that both lead to the same qualitative conclusion.

P5-m9
Sec. IV A step 7; Fourier-kernel details
Problem: The Gaussian smoothing scale Rs is specified, but the kernel convention is not stated explicitly (e.g., whether the Fourier-space kernel is exp[−(k Rs)^2/2], i.e., Rs as the real-space σ, or an alternative normalization).
Required fix: State the exact Fourier-space kernel form and confirm that Rs is the real-space Gaussian σ (not FWHM or √2 σ). This improves comparability with other T-Web implementations.

P5-m10
Appendix B, Table XVIII; definition of Cramér’s V
Problem: The text gives V = √(χ²/n). That is correct only because min(r−1, c−1) = 1 for a 4×2 table. Readers may copy the expression more generally.
Required fix: Add the general definition V = √(χ² / [n · min(r−1, c−1)]) and then note that for 4×2, min(r−1, c−1) = 1, hence the simplification used.

P5-m11
Eq. (2) explanation (Bonferroni threshold)
Problem: The sentence “each tail contributes α/2K, so |σ| thresholds apply symmetrically” can confuse given the subsequent use of erfc−1(α/K). The equality holds because erfc encodes both tails.
Required fix: Add one clarifying clause: “We solve erfc(t/√2) = α/K because P(|Z| > t) = erfc(t/√2) already accounts for both tails; equivalently, per tail is α/2K.”

P5-m12
Sec. VIII E (any-hole vs maximal-sphere)
Problem: You state “continuity within ±0.6 pp” and later quote +0.06 pp vs −0.54 pp. The reader must mentally compute the 0.60 pp span to see the consistency.
Required fix: Add the explicit difference “(difference 0.60 percentage points)” after the two ∆fCW values to make the continuity claim transparent.

J. STALE/INCONSISTENT NUMBERS

P5-J1
Sec. VIII B narrative around Table X (program fractions)
Problem: The 98.8% vs 99.1% bright-fraction wording (see P5-E6) reads as a stale/uncleared revision between the overall-in-sample and in-void-subset fractions.
Required fix: As in P5-E6, present both fractions explicitly with their denominators and clarify which population each refers to.

NO OTHER DISCREPANCIES FOUND IN A–I CLASSES
- Arithmetic spot-checks not covered in the first review (cell counts, volume fractions, σ predictions, design-effect inflation, shell-corrected class migrations, Jeffreys-interval scales) continue to reconcile with the displayed numbers within rounding.
- Figure captions vs body claims match numerically where verifiable from the tables.
- Dimensional checks on the Fourier/Poisson conventions are internally consistent given the stated normalization choice and the use-case (only eigenvalue ordering vs λth matters), with the added kernel-clarity request above (P5-m9).
- Internal cross-references (to sections, tables, and equations) point to the correct content; the pervasive artifact-ID cross-references were already flagged in the initial review (P5-E2).

Summary of why these are new
The earlier review focused on dependence on Paper IV, artifact creep in the main text, a typo in the Clopper–Pearson bound, RSD handling, and clarity/multiplicity/style issues. The fresh-eyes pass surfaced (i) the need to elevate the exact DESIVAST membership counts into the primary table; (ii) a concrete count-mismatch and clarity gap in the DESIVAST program split; and (iii) the need to either rebase or clearly demote the selection-contaminated canonical T-Web results, plus several smaller clarity fixes (NSIDE consistency, kernel definition, and statistics-formula clarity). These items tighten the paper’s primary-number presentation and reduce potential reader confusion.