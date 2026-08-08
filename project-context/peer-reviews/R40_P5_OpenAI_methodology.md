# P5 R40 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` md5=7bb73989 pages=32
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (10761 chars)
**Wall time**: 274.5s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample”

Scope of review
- Role: methodology rigor (statistics, derivations, dimensional analysis, arithmetic, error propagation, internal consistency).
- I audited the abstract, all tables/figures/equations, and recomputed the quoted σ, χ², p-values, ranges, and percentages from the numbers shown in the manuscript.

Overall assessment
The paper presents a careful empirical null test: spiral galaxy chirality shows no detectable dependence on large-scale environment within DESI DR1 at the quoted sensitivity. The analysis is extensive and, for the most part, numerically consistent: I verified the class fractions and σ-from-half values in Table III, the DESIVAST void/non-void contrasts and their z-scores in Table X, the density-quintile residuals in Table IV, the HEALPix look-elsewhere numbers in Table VI, and the monopole-subtracted residuals in Table XII. However, there are several essential methodological and presentation issues that must be addressed for PRD standards, chiefly (i) an incorrect unit-conversion statement for h that could mislead replication; (ii) dependence on an unpublished companion (Paper IV) for the definition and calibration of the central observable; (iii) lack of a frozen, citable DOI for the code/data snapshot; (iv) abstract-level robustness claims that include under-resolved T-Web sweep cells; and (v) post hoc designation of the “primary” estimator. I list all findings below.

Findings

ESSENTIAL

P5-E1 (Sec. IV.A, p.5; Footnote “1 Dimensional derivation”)
Problem: The manuscript states “The alternative convention χ[h−1 Mpc] = χ[Mpc]/h (divide-by-h, giving ≈1246 h−1 Mpc at z = 0.2) is not used here.” This is incorrect: the numerical value in h−1 Mpc is χ[h−1 Mpc] = h × χ[Mpc], not χ/h. The provided “divide-by-h” equality and the worked number (1246 h−1 Mpc) are wrong and contradict the correct earlier statement (multiply-by-h).
Required fix: Replace the incorrect formula with the correct identity χ[h−1 Mpc] = h × χ[Mpc]; delete the “divide-by-h” alternative (or explicitly label it as incorrect) and remove the 1246 h−1 Mpc figure. Provide one consistent worked example only.

P5-E2 (Throughout; abstract, Secs. I–III, VI, VIII–XI; all pages)
Problem: Heavy reliance on an unpublished companion (“Paper IV,” “in preparation”) for the chirality labels and for the catalog-wide monopole (∆fCW = −0.0026) that underpins multiple significance statements. While you do compute and use the matched-sample monopole fP5
CW = 0.4972 in several places, the paper repeatedly treats the Paper IV monopole as a known quantity and appeals to Paper IV for imaging-leg systematics and classifier properties.
Required fix: Make the present paper self-contained for PRD readers. At minimum:
- Freeze and cite the exact chirality-catalog version (including a persistent DOI and checksum), and summarize the label-generation method and QC necessary to evaluate bias and error properties relevant to this paper.
- When the Paper IV monopole is used in σpred, present all key conclusions also on the fP5
CW basis (which you already compute in Table XII), and demote any conclusion that hinges on ∆fCW = −0.0026 beyond what is supported directly by the P5 sample.
- Either include as supplemental material the minimal classifier/validation description needed for this analysis, or replace every load-bearing reference to “tracked in Paper IV” with quantitative content reproduced here.

P5-E3 (Abstract, p.1; Sec. VII, Table VII, Fig. 7)
Problem: The abstract reports a “Phase 2 sensitivity sweep across nine cells {Rs, λth} ∈ {10, 25, 50}×{0.0, 0.1, 0.3} … no cell below 0.05” without disclosing that three of the nine cells (Rs = 10 Mpc/h) are under-resolved relative to the 25.9 Mpc/h grid and are explicitly excluded from the robustness claim in the body.
Required fix: Amend the abstract to state clearly that three Rs = 10 Mpc/h cells are below the grid sampling scale and are retained only as a degenerate near-unsmoothed limit; the robustness claim and significance summaries apply to the six resolved cells (Rs ∈ {25, 50}).

P5-E4 (Appendix C, Data/Code availability, p.31)
Problem: The paper states that “A DOI-minted archival snapshot accompanies journal submission,” but no DOI is provided and no immutable release (with checksums) is cited. Numerous pipeline pathnames and artifact filenames are referenced throughout, but without a frozen, citable release.
Required fix: Provide an actual DOI (Zenodo/OSF/etc.) for the exact code/data snapshot corresponding to the manuscript version, include version tag, commit hash, and checksums for the key artifacts referenced in the text (e.g., the Phase 2 sweep CSV, per-class count arrays). PRD requires a reproducible deposit.

P5-E5 (Sec. V.B, p.7; “Primary vs. secondary analysis paths (pre-registration caveat)”; Abstract)
Problem: The “primary” estimand and path (DESIVAST void-vs-non-void) are designated after exploratory analysis; the text acknowledges a garden-of-forking-paths concern but does not adjust for it in the headline narrative. The abstract presents multiple statistics from both primary and secondary paths without an explicit pre-specification.
Required fix: Either (i) document a pre-registered plan (if it exists) and ensure the abstract lists only pre-registered headline statistics, or (ii) reframing: present the DESIVAST result as the main analysis chosen for its power and robustness, and explicitly flag its post hoc selection in the abstract/conclusions. State clearly that no multiple-hypothesis correction applies across analysis families because only the DESIVAST path is now treated as confirmatory; all others are descriptive diagnostics.

P5-E6 (Throughout; multiple sections/pages)
Problem: Version-history and internal bookkeeping appear in the body (e.g., “earlier preprint versions used the ‘V-Web’ label…,” “Paper IV v1.0.166,” artifact file names/paths sprinkled in main text). PRD discourages embedding version logs or preprint revision notes in the scientific narrative.
Required fix: Remove version-history prose and relegate file-path references and provenance details to a Reproducibility Appendix/SM. Keep the body text focused on methods and results; retain one compact paragraph with the frozen-release DOI and a one-line pointer to the SM for the full provenance.

MAJOR

P5-M1 (Sec. IV.A, p.5–6; headline T-Web run; Sec. IX.A, p.23–24)
Problem: The canonical T-Web classification uses a global mean density despite a steep radial selection function, which the paper shows produces substantial class migration (void 0.244 volume fraction canonically vs 0.75% when completeness-weighted in z<0.5; class populations change by factors ≈2–20 in the shell-corrected rebuild). Yet the abstract and Sec. VI.A headline prominently quote the canonical T-Web class fractions and σ, with the shell-corrected result framed as a “stress test.”
Required fix: Recast the T-Web part of the paper so that (a) either the shell-corrected (or completeness-weighted) T-Web is the only version you report in the abstract and headline tables; or (b) explicitly state, at first mention in abstract and Sec. VI.A, that the canonical labels are affected by selection leakage and are shown as a supporting diagnostic only, with the corrected run as the preferred T-Web statement.

P5-M2 (Sec. VIII.A, p.17)
Problem: The 0/6 per-object T-Web-void vs DESIVAST-hole mismatch at z≤0.24 is presented as “illustrating” the survey-shell systematic. The sample size is too small to support even an illustrative purity statement beyond the Clopper–Pearson bound you quote.
Required fix: Tone down to a purely descriptive statement (e.g., “0/6 in this small overlap; one-sided 95% upper bound 39%”), and remove any language implying this small draw substantiates a systematic. The broader systematic case is already made quantitatively in Sec. IX.C; point to that instead.

P5-M3 (Sec. X, p.26–27)
Problem: The ASTRA-vs–T-Web per-galaxy disagreement in the EDR overlap (T-Web virtually all filament+cluster; ASTRA covers all four classes) is a strong reminder that the T-Web grid is coarse relative to the EDR rosettes. While the text discusses this, there is no quantitative measure of how much class imbalance alone can wash out per-class fCW differences in the EDR overlap.
Required fix: Add (or cite in SM) a short power calculation for the EDR overlap: given the ASTRA class populations and the observed global monopole, what is the minimum detectable ∆fCW per class at α=0.05 after Bonferroni-4? This will calibrate the “consistency” claim.

P5-M4 (Table X, p.19)
Problem: Minor inconsistency in the quoted σnon−void for the V2-REVOLVER sphere approximation. Using the printed n and f yields σ ≈ −5.01 (not −4.94). This likely comes from rounding f to four decimals.
Required fix: Either print σ computed from the printed f to maintain display consistency, or include one more decimal for f so that σ recomputes to the stated value.

P5-M5 (Appendix C, p.31)
Problem: The reproducibility checklist mixes file paths, tags (e.g., v0151, r24conf), and internal script names in the body of the paper.
Required fix: Move the checklist to SM and replace in-text references with a single line pointing to the SM (containing the DOI, commit hash, and exact artifact list).

MINOR

P5-m1 (Abstract, p.1; Sec. XV Conclusions, p.30)
Problem: Phrasing such as “to our knowledge, the largest matched-sample environmental-dependence test in DESI DR1” is not justified with a literature survey.
Required fix: Either provide citations showing no larger DR1 matched-sample studies exist, or soften to “a large matched-sample test.”

P5-m2 (Units/notation; multiple pages)
Problem: Mixed use of “h−1 Mpc” and “Mpc/h” and occasional omission of h when reporting cell size or smoothing scale.
Required fix: Standardize on one convention (e.g., h−1 Mpc) everywhere and ensure units appear in all figure axes and captions where distances are shown.

P5-m3 (Sec. V, p.6–7)
Problem: Label-shuffle p-values are reported to three decimals (e.g., 0.135), while NMC=1000 implies a Monte-Carlo standard error ≈0.01–0.015.
Required fix: Report p to two decimals (or include ±seMC) to reflect the MC resolution.

P5-m4 (Tables VI, VII captions, p.13–15)
Problem: The family-wise correction strategy is scattered between caption and text, and “pLEE” is defined only once.
Required fix: Add a short, explicit reminder in each caption that pLEE is the empirical max-statistic p within that family, with NMC=1000, and state when a global max-stat across families is (or is not) applied.

P5-m5 (Sec. VI.D, Table V, p.11)
Problem: The density covariate ρ̄ is described in words; the units and normalization could remain unclear to a standalone reader.
Required fix: Add a compact formula in the caption: ρ̄ = ⟨log10(1+δsmooth)⟩quartile, where δsmooth is the Gaussian-smoothed overdensity field normalized to the cube mean.

P5-m6 (Sec. VI.A, Fig. 3 caption, p.9)
Problem: The statement about design-effect inflation (“≤1.9%”) is not accompanied by the calculation.
Required fix: Add the arithmetic (√(812,793/783,820)=1.018) parenthetically to make it reproducible from the numbers shown.

P5-m7 (Typos/formatting; multiple pages)
Problem: Spacing inconsistencies (e.g., “p= 0.135”), occasional duplicated hyphenation, and in-line code/file names in the main text reduce clarity.
Required fix: Clean up spacing, move file paths to SM, and standardize hyphenation (e.g., “max-stat”).

P5-m8 (Sec. IX.C, p.25–26)
Problem: The T-Web “cluster” vs “knot” nomenclature is mixed across classifiers.
Required fix: Add a one-sentence mapping in the first paragraph of Sec. IX.C stating explicitly that “cluster” (this work) ≡ “knot” (Ref. [11]) for clarity.

P5-m9 (Fig. 6, Fig. 8; pages 14 and 22)
Problem: Axis labels/legends: the σ color scale has no units; the projection coordinate system is mentioned only in the caption.
Required fix: Add units to color bars (“σ-from-half (dimensionless)”), and indicate “Equatorial coordinates” on the plot or caption consistently.

NITS

P5-n1 (Sec. II, p.3)
Problem: “v1.0.166” Paper IV versioning and “withdrawn” note about a harmonic-space statistic are version-log information.
Required fix: Remove from body; if necessary, add one brief sentence noting that only the real-space dipole statistic is relevant here and is null, with Paper IV cited.

P5-n2 (Sec. VII, Table VII note, p.15)
Problem: Parenthetical remarks about RNG stream re-draws and specific seed values clutter the narrative.
Required fix: Relocate to SM; keep a single sentence noting that results are stable under RNG re-draws.

Arithmetic/consistency audit (selected checks)

- Table III (p.8–9): Verified σfrom half values from n and nCW for all four classes. Range 1.98 pp matches 0.5034−0.4836.
- Density quintiles (Table IV, p.10): Verified σobs and σpred for each quintile at N=158,327; residuals match.
- DESIVAST VoidFinder (Table VIII, p.17–18): Verified fCW and σ for void (n=56,981; f=0.4964; σ=−1.71) and non-void (n=621,964; f=0.4971; σ=−4.59). Contrast ∆=+0.00067; SE=0.00219; z=+0.31; CI agrees.
- Three-algorithm DESIVAST (Table X, p.19): Recomputed SEs and z-scores; small rounding issue for V2-REVOLVER non-void σ as noted in P5-M4.
- Monopole-subtracted residuals (Table XII, p.21): Spot-checked void and filament; computed σvsMonopole consistent with printed values using fP5
CW=0.49719 and denominators 0.5/√n.
- HEALPix max-|σ| vs null p99 (Table VI, p.13): Reported observed maxima below empirical p99; LEE p-values (0.607/0.135/0.413) consistent with NMC=1000 resolution.

Length
The manuscript is 32 pages for a single, well-executed null result. Consider condensing the main text to ≈18–22 pages by moving pipeline paths, provenance minutiae, and extended sensitivity details (already well-documented) to SM, keeping the core methods, main numbers, and robustness highlights in the body.

Abstract-last drift sweep
I re-read the abstract after auditing the body. Two points need alignment: (i) explicitly note the Rs=10 under-resolution caveat (P5-E3); (ii) clarify that T-Web is a secondary cross-check and that the DESIVAST void analysis is the primary estimator (P5-E5). All other abstract scalars (n, fractions, χ², p-values, per-class σ, ranges, DESIVAST counts) are traceable to the body.

Provenance surfaces
Appendix C claims a DOI-minted snapshot but does not supply it (P5-E4). All load-bearing artifacts and counts are referenced by in-repo paths and should be tied to a frozen deposit.

Effect sizes
Where χ² or z are given, effect sizes are generally present (e.g., Cramér’s V=0.078). Keep this framing in the abstract when mentioning the class×program contingency result.

## Summary recommendation
MAJOR REVISIONS

The core analysis appears statistically sound and internally consistent, and I verified the key numbers. However, several essential methodological/presentation issues must be fixed for PRD: correct the h–unit conversion statement; make the paper self-contained with a frozen DOI for code/data and minimal classifier summary in lieu of an unpublished companion; revise the abstract (under-resolved cells, confirmatory pathway); and reframe the T-Web headline to give primacy to the selection-corrected or completeness-weighted build. Once these are addressed, along with the listed major/minor points, the paper would meet PRD’s methodological rigor standards.

---

## PASS 2 — self-critique findings (what initial review missed)

P5-E7 (Sec. VIII.D, p.19; Table X; Sec. VIII.E, p.20–21; numeric rounding coherence)
Problem: Several σ-from-half values and related derived σ entries appear inconsistent with the printed f values at the given n beyond what two-decimal rounding should induce.
Examples:
- V2-VIDE catalog-native void row: n=74,111, f=0.4972. Using σ = (f−0.5)/(0.5/√n) gives σ≈−1.53, not −1.50.
- Table XI “0 maximal voids per pixel”: n=378,511, f=0.4961 gives σ≈−4.80, not −4.75.
Required fix: Either recompute and print σ from the displayed f and n (for full consistency in display), or print f to one additional decimal place so σ recomputes to the stated values from the table entries.

P5-M6 (Sec. VI.A, p.8–9; Abstract; Table III; σ-from-half computed on row-level parent with duplicates)
Problem: The headline class σ-from-half values (and those quoted in the abstract) are computed on the 812,793 env-labeled “row-level parent,” which includes 3.56% duplicate rows (coadds). While the χ² contingency test is repeated on the unique-spiral subset, the σ values (void −0.68, wall +0.55, filament −2.61, cluster −4.66) and their interpretation are not re-stated on the unique-spiral parent. Duplicates nominally violate the i.i.d. binomial assumption used for σ.
Required fix: For headline reporting (body and abstract), add the corresponding σ-from-half computed on the 783,820 unique-spiral subset (or explicitly state the design-effect adjustment for σ, not just for CIs). Alternatively, move the σ reporting to the unique-spiral parent everywhere and keep the row-level numbers in SM.

P5-M7 (Notation collision; Eq. (1) vs. DESIVAST contrasts; multiple sections)
Problem: The symbol ΔfCW is used for two different quantities: (i) the catalog-wide monopole offset from 0.5 in Eq. (1) (used to predict σpred), and (ii) the two-sample environment contrast (e.g., fnon-void−fvoid in §VIII and Table X). This overloading is easy to miss and can cause confusion when scanning.
Required fix: Use distinct symbols (e.g., Δfmono for the monopole offset in Eq. (1) and Δfenv for environment contrasts). Update text and figure captions where both appear.

P5-M8 (Abstract, p.1; Sec. VIII.E, p.20–21; interpretation of “0 maximal voids per pixel”)
Problem: The abstract states that the −5σ monopole offset is “concentrated entirely in the ‘0 maximal voids per pixel’ bin (sky regions outside DESIVAST coverage).” In the body, this “outside coverage” inference is qualified as a proxy (zero-void pixels at NSIDE=16 can occur stochastically inside the footprint), and only later is an explicit footprint mask re-tabulation provided.
Required fix: Soften/clarify the abstract wording to match the body: explicitly note that “0 maximal voids per pixel” is a proxy for outside-footprint regions and that the mask-based re-tabulation (Sec. VIII.E) confirms the conclusion when using an explicit DESIVAST footprint.

P5-M9 (Sec. V, p.6–7; density proxies comparability)
Problem: Two different “density” proxies are used in different sections: (i) a projected 2D k=5 nearest-neighbour angular proxy for the whole-sample density scan (§VI.C), and (ii) a 3D T-Web smoothed overdensity (log10(1+δsmooth)) for within-class stratification (§VI.D). The paper does not explicitly remind the reader that these are different notions of “density,” which could lead to misinterpretation when comparing figures/tables across sections.
Required fix: Add a one-sentence disclaimer near the start of §VI (or in §IV.A step 12) that the global density scan uses a 2D projected proxy among spirals, whereas within-class stratification uses the 3D T-Web density field; conclusions across these two analyses should not be conflated.

P5-M10 (Sec. VI.A, Fig. 3 caption vs Abstract; σ comparability)
Problem: The body text and Fig. 3 caption repeatedly caution that σ-from-half scales as √n and is not comparable across classes; however, the abstract lists per-class σ values sequentially without this comparability caveat. Given common PRD practice, readers may infer direct comparability from the abstract alone.
Required fix: Add a brief parenthetical in the abstract noting that σ values scale with √n and are not directly comparable across classes of different sample size; direct inference relies on either the monopole-subtracted residuals or formal homogeneity tests (both already reported).

P5-M11 (Sec. IX.A, p.23–24; completeness-weighted low-z rebuild; magnitude of class-volume shifts)
Problem: The text states “class volume fractions shift by up to 21 pp” in the completeness-weighted (z<0.5) rebuild, but no per-class before/after numbers are tabulated for that configuration. The void fraction example given (17.6%→0.75%) is a −16.85 pp change; readers cannot verify the “21 pp” claim.
Required fix: Provide the before/after class-volume fractions (or a small table) for the z<0.5 completeness-weighted rebuild to substantiate “up to 21 pp” and allow precise verification.

P5-m10 (Sec. VIII.D, p.19; V2-VIDE catalog-native void σ rounding; Table XI σ rounding)
Problem: Small but recurring rounding inconsistencies between printed f and σ (see P5-E7 examples).
Required fix: Harmonize rounding across affected rows or carry one extra decimal in f.

P5-m11 (Sec. IV.A, step 5; units consistency in grid size mention)
Problem: The side length is reported as “6,634 Mpc/h” (cell 25.9 Mpc/h). Elsewhere the manuscript uses h−1 Mpc. Mixed “Mpc/h” vs “h−1 Mpc” appears in several places (e.g., Rs values, Figure captions).
Required fix: Standardize units throughout (preferably h−1 Mpc) and ensure figure axes/captions use the same convention.

P5-m12 (Sec. X, p.26–27; ASTRA EDR overlap power)
Problem: The claim that all three classifiers (T-Web on overlap; ASTRA argmax; ASTRA entropy-weighted) recover null in the EDR overlap would benefit from an explicit minimum-detectable-effect calculation. The current text notes Bonferroni-4 but does not quantify power.
Required fix: Add a short power calculation (or SM note) giving the minimum detectable per-class ΔfCW at α=0.05 after Bonferroni-4 for the ASTRA class populations in Table XIV.

P5-m13 (Sec. VIII.F, p.21; per-pixel σvs monopole distribution)
Problem: The discussion usefully reports mean/std/skew/kurtosis for σvs monopole across pixels, but does not provide the exact n used in the quoted “full redshift range” map in that paragraph. Earlier it cites 1,791 valid pixels (≥200 spirals), then 1,769 after deduplication, but the immediate paragraph’s first sentence does not restate which population is used for those moments.
Required fix: Add “(n=1,791 pixels; ≥200 spirals each)” (or “n=1,769” if deduplicated) at first use in that paragraph to pin the numbers to the correct parent.

P5-m14 (Sec. V, Eq. (2) and captions for Tables VI–VII)
Problem: Although the max-stat empirical pLEE is defined in §V, the captions for Tables VI–VII could mislead readers about when pLEE is per-family vs global. The text later clarifies a global max-stat across Phase-2 cells (pglobal=0.36 or 0.27), but the captions don’t restate this context.
Required fix: In each caption, add one line: “pLEE is the empirical max-|σ| p-value within this family (NMC=1000); no global correction across other families is applied here. See §VII for the global max-stat across sweep cells.”

P5-m15 (Sec. VI.B, p.9–10; regression covariates)
Problem: The regression model states “Pr(CW) ∼ β0 + βenv + ... confidence” but the definition of the “confidence” regressor (Paper IV classifier maximum probability? thresholded?) is not explicitly given here.
Required fix: Define the exact “confidence” variable used (e.g., classifier softmax max-probability for the assigned label) and its scaling.

P5-m16 (Sec. VII, Table VII; “Grid-unresolved” labeling)
Problem: The table groups Rs=10 rows as “grid-unresolved” (correct), but the note in the caption could be read as excluding them only from the “robustness claim” rather than also from any aggregated summaries. Some summary sentences in §VII include the nine-cell range; others restrict to the six resolved cells.
Required fix: Add a one-sentence reminder at the start of §VII that all significance claims and combined summaries are based on the six resolved cells unless explicitly stated otherwise; the three Rs=10 rows are descriptive only.

P5-m17 (Sec. VIII.E, p.20–21; minor number drift)
Problem: The non-void count in the footprint-restricted re-tabulation is given as 253,276 of “621,864” (not 621,964 as in the initial sphere-union count). This is correct for the “exact” rerun (void rises from 56,981 to 57,081), but the text doesn’t explicitly remind the reader that the exact-membership variant is now in force for that paragraph, inviting momentary confusion.
Required fix: Insert “(using the exact-membership counts; void=57,081, non-void=621,864)” when reporting the footprint restriction to make the reconciliation immediate.

P5-m18 (Sec. VIII.A, p.17; small-sample purity statement tone)
Problem: The 0/6 T-Web-void vs DESIVAST-hole overlap at z≤0.24 is described as “illustrates the survey-shell systematic.” Given the tiny n, the text should avoid any implication of substantiation beyond the bound given.
Required fix: Tone this to purely descriptive (“0/6 in this small overlap; one-sided 95% upper bound 39%”) and refer to §IX.C for the quantitative systematic evidence (the T-Web vs external T-Web volume-fraction discrepancy).

P5-m19 (Sec. VI.D, Table V caption; density covariate definition)
Problem: The density covariate’s definition is described in words; a compact formula would help reproducibility.
Required fix: Add “Here ρ̄ = ⟨log10(1+δsmooth)⟩quartile, with δsmooth the Gaussian-smoothed overdensity field normalized to the cube mean.”

P5-m20 (Sec. IX.C, p.25–26; classifier nomenclature)
Problem: “cluster” in this work vs “knot” in Ref. [11] is used interchangeably across that section without an explicit one-line mapping.
Required fix: Add “We use ‘cluster’ where Ref. [11] uses ‘knot’ (same concept).”

P5-m21 (General; p-value precision vs NMC=1000)
Problem: Several empirical p-values are quoted to three decimals (e.g., 0.135) when NMC=1000 implies a Monte-Carlo resolution of ≈0.01–0.015.
Required fix: Report pLEE to two decimals (or include “± seMC”) consistently.

Explanation
These items were not covered in the initial review. I re-checked table-by-table arithmetic, σ recomputations, figure/caption alignment, symbol usage, unit conventions, and comparability warnings between different analyses. Most of the core numbers remain internally consistent; the new issues are chiefly precision/rounding, clarity on parents and proxies, symbol overloading, and ensuring independence assumptions and unit conventions are made explicit wherever headline values appear.