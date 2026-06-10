# P5 R26conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.56.pdf` md5=4061bf5c pages=27
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6120 chars)
**Wall time**: 360.7s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test …”

Scope of review
I evaluated the manuscript for methodological rigor in statistics, derivation consistency, dimensional analysis, internal arithmetic, error propagation, the validity of null procedures, and the traceability of all scalars, especially those appearing in the abstract and conclusions. I re-computed every quoted σ, p-value, range, difference, and ratio from the numbers and equations provided, and checked figure/table consistency with the text.

Overall assessment
The paper presents a careful null test of environment-dependent chirality using a DESI DR1 cross-match, a T-/V-Web tidal-tensor classification, and a DESIVAST void re-projection, with extensive sensitivity and systematics checks. Many computations are internally consistent. However, there are several essential issues that must be corrected before the paper can meet PRD standards, including (i) a contradictory statement about the catalog-wide monopole significance (∼1σ vs ∼9.5σ) that appears early in the paper, (ii) multiple instances of “earlier draft”/version-history prose embedded in the scientific narrative, (iii) an explicit arithmetic error in a one-sided binomial bound (“0 of 6”) written as 1 − 0.051/6 instead of 1 − 0.05^(1/6), and (iv) confusing sample-ledger language in the abstract about which parent the DESIVAST test is “drawn from.” In addition, several major issues require revision (RSD handling, window-function deconvolution test or justification, over-detailed pipeline file paths in the main text, uniformity of units/notation, MC p-value uncertainty reporting).

Findings

ESSENTIAL

P5-E1 (Contradictory significance of the catalog monopole)
- Location: Sec. I–II, page 2 (first paragraph under INTRODUCTION and Relation to Paper IV)
- Text: “Paper IV … establishes the global mixture in the post-test-time-augmentation equivariant classifier as a CW fraction of 0.4974 ± 0.000279, consistent with parity at ∼ 1σ.”
- Problem: 0.4974 differs from 0.5 by 0.0026. With an uncertainty of 0.000279, the deviation is ~9.3σ, not ∼1σ. Later in §VIII F the manuscript itself refers to “the ∼ 9.5σ catalog-level monopole reported in Paper IV.” This is an internal contradiction.
- Required fix: Correct the statement to be numerically consistent with the quoted uncertainty and with §VIII F. If the “∼1σ” refers to a different statistic (e.g., a dipole amplitude fit or a corrected estimator), state that explicitly, present the corresponding uncertainty, and avoid conflating the binomial monopole with a different estimator.

P5-E2 (Version-history and “earlier draft” prose embedded in main text)
- Location: Multiple (e.g., Sec. VI D, p. 10–11; Sec. VII, p. 12; Sec. VIII D, p. 15–16; Sec. IX B, p. 20–22; Appendix B, p. 26)
- Text: “An earlier draft quoted … withdrawn …”; “the superseded unfiltered-join version is retained …”; “earlier draft … are withdrawn in favor of …”; “manuscript tag v0.1.56-2026-06-10”.
- Problem: PRD does not accept internal version-history commentary or retraction log prose in the body of the paper. These belong in a private change log or, if essential for reproducibility, a data/code appendix without narrative about earlier mistakes.
- Required fix: Remove all “earlier draft”, “withdrawn”, “superseded”, “recompute after defect”, “manuscript tag vX.Y” prose from the body. Where necessary, replace with clean statements of the final method and results only. If provenance is needed, move it to a brief note in a Data/Code Availability appendix (no narrative about prior drafts).

P5-E3 (Arithmetic error in one-sided “0 of 6” binomial bound)
- Location: Sec. VIII A, page 14–15 (DESIVAST per-galaxy cross-match)
- Text: “With 0 of 6, the one-sided 95% binomial upper bound on the true in-hole fraction is 1 − 0.051/6 = 39%…”
- Problem: The correct Clopper–Pearson one-sided 95% upper bound for 0/6 is 1 − 0.05^(1/6) ≈ 0.393, not “1 − 0.051/6” (which would be ≈ 0.992). The typesetting dropped the exponent.
- Required fix: Replace with 1 − 0.05^(1/6) ≈ 0.393 (39.3%), and explicitly show the exponent to avoid misinterpretation.

P5-E4 (Confusing/incorrect abstract sample ledger for the DESIVAST primary test)
- Location: Abstract, page 1
- Text: “the headline DESIVAST void test is anchored on 56,981 void spirals drawn from 783,820 unique chirality-relevant matched spirals (791,635 minus 7,815 without an environment row), carried on 812,793 environment-labeled survey–program coadd rows.”
- Problem: The DESIVAST test operates on the z ≤ 0.24 low-z matched sample (nlz = 678,945; §VIII B), and does not depend on the V-Web environment table. Saying the 56,981 DESIVAST voids are “drawn from 783,820 unique … env-matched spirals” is misleading; they are drawn from the low-z cross-matched sample, irrespective of V-Web labeling. This conflates two different parents.
- Required fix: Correct the ledger to state clearly which parent set the DESIVAST test is drawn from (the z ≤ 0.24 matched sample; nlz = 678,945), and avoid implying dependence on the V-Web-labeled subset. Provide the exact numerics consistently (nvoid = 56,981 of nlz = 678,945; ∆fCW = +0.0007) in the abstract without mixing with the 783,820/812,793 V-Web counts.

P5-E5 (Presentation cleanliness—pipeline paths in body text)
- Location: Many sections (e.g., §IV A, §VI A–E, §VII, §VIII D–F, §IX A–C), pages 4–25
- Text: Frequent in-line references to local file paths, e.g., “pipelines/p5_desi_chirality/outputs/…”, “env_finder/reports/…”.
- Problem: This is not acceptable in the main narrative for a PRD article. It distracts and reads as a lab notebook. Provenance can be given in a Data/Code Availability appendix, or via a DOI to a repository, but not as line-by-line file paths throughout the Results.
- Required fix: Remove all in-line file-path references from the body. Consolidate reproducibility details in a brief Data/Code Availability appendix with one DOI and, at most, high-level directory mapping.

MAJOR

P5-M1 (RSD treatment)
- Location: §IV (V-Web classifier), §VIII (primary DESIVAST result), §XIII (Limitations), throughout
- Issue: The V-Web classifier is run in redshift space without reconstruction. While the authors discuss this (§XIII) and anchor the primary result on the DESIVAST void re-projection (which is largely RSD-insensitive for in/out-of-void membership), the headline V-Web class fractions and many diagnostics still rest on redshift-space classes. A quantitative assessment of RSD effects on class assignment is currently heuristic (σv/(aH) and a coarse eigenvalue-shift estimate).
- Required fix: Either (a) provide a mock-based or reconstructed-position re-classification to quantify RSD-induced class flips and their impact on fCW per class, or (b) confine all headline quantitative claims strictly to the DESIVAST-based primary test and move V-Web class-level numbers to a clearly marked secondary/diagnostic section with an explicit caveat. At minimum, add an uncertainty budget from RSD (e.g. via mocks or by bracketing using plausible σv) to the V-Web results.

P5-M2 (CIC window deconvolution not assessed)
- Location: §IV A step 9, page 5
- Text: “the CIC mass-assignment window is not deconvolved before the second derivatives. Only the ordering and sign of the eigenvalues relative to λth enter the classification, so λth is defined on this (window-convolved) normalization.”
- Issue: Not deconvolving CIC can bias the eigenvalue field at the grid scale. The paper does not test that omission’s effect on class assignment or on fCW per class. Grid-resolution checks are helpful but not a substitute for assessing the mass-assignment window.
- Required fix: Provide an explicit check (e.g., rebuild at one configuration with/without CIC deconvolution, or with TSC), report the fraction of galaxies changing class and the resulting change in per-class fCW. If negligible, state so quantitatively.

P5-M3 (Multiple-procedure σ and p-values—comparability and MC error bars)
- Location: Throughout Results, Tables V–VI
- Issue: The paper mixes raw σfrom half, monopole-predicted σpred, and σvs monopole residuals appropriately, and often notes non-comparability. However, MC-based p-values (NMC = 1000) are quoted to two or three decimals without MC uncertainty. For p ∼ 0.13–0.61 the Monte Carlo standard error is O(0.01).
- Required fix: Add MC uncertainty estimates to reported permutation p-values (e.g., p = 0.135 ± 0.011), or state NMC and the implied resolution explicitly wherever p is quoted. Continue to clearly distinguish raw σfrom half from σvs monopole wherever both appear.

P5-M4 (Title/footnote notation in abstract)
- Location: Abstract, page 1
- Text: Footnote marker “a” appears in the abstract to define the T-Web vs V-Web terminology.
- Issue: PRD typically avoids footnotes in the abstract. This also clutters the first paragraph.
- Required fix: Move the methodological footnote from the abstract into §IV A (Algorithm) and adjust the abstract wording to avoid the footnote.

P5-M5 (Toy EFT operator in Appendix A)
- Location: Appendix A, page 25–26
- Issue: The introduced operator is explicitly labeled schematic and non-gauge-invariant, with a coordinate vector (ẑ), and not derived from the cited literature. As written, it reads as speculation and is not needed for the methods paper’s message.
- Required fix: Either remove Appendix A entirely or rewrite to (i) present only a dimensionally consistent, gauge-aware scaling argument or (ii) move it to a short “Outlook” paragraph stating that translating the observational bound to EFT parameters is model-dependent and beyond scope.

P5-M6 (Units and notation consistency)
- Location: Throughout
- Issue: Mixed usage of h−1 Mpc and Mpc/h; both are standard, but unify within the paper. Clarify where k carries units of h Mpc−1.
- Required fix: Standardize units (prefer h−1 Mpc for positions; h Mpc−1 for k). Add a one-line conventions note early in §IV A.

P5-M7 (Abstract length/complexity)
- Location: Abstract, page 1
- Issue: The abstract is overly dense and ledger-like, mixing multiple parents (V-Web rows vs unique-target vs low-z sample), primary and secondary analyses, and many symbols and caveats. This hampers clarity.
- Required fix: Rewrite the abstract to (i) clearly identify the primary test (DESIVAST void re-projection), its sample size and result, (ii) summarize the V-Web diagnostic as secondary and consistent, and (iii) avoid internal pipeline jargon. Keep to ~200–250 words.

MINOR

P5-n1 (Recompute check: “void-bin 2σ half-width ±4.8 pp”)
- Location: Abstract, page 1; §VI A, p. 7
- Check: 2σ binomial half-width at N=428 is 1/√N ≈ 0.0484 = 4.84 pp. Correct. No change needed.

P5-n2 (Range and σ computations)
- Location: Table II, p. 7; Table III, p. 8; Table VI, p. 13
- Check: All recomputed σfrom half and ranges match to rounding (filament −2.61σ; cluster −4.66σ; range 1.98 pp; quintile-3 σobs −3.94 vs σpred −2.07 ⇒ residual 1.87σ; Phase-2 ranges 1.72–4.12 pp; pLEE 0.13–0.56). No change needed.

P5-n3 (Bonferroni thresholds)
- Location: §V A, page 6; Table V, p. 11
- Check: |σ|Bonf0.01,5 ≈ 3.09; |σ|Bonf0.05,1054 ≈ 4.05. Values are reasonable. Consider noting two-sided nature explicitly next to Eq. (2).

P5-n4 (Jeffreys intervals)
- Location: Figure 3 caption, p. 7
- Issue: You refer to Jeffreys 95% intervals but do not specify the prior explicitly (Beta(1/2,1/2)); minor clarity.
- Fix: Add a parenthetical “Jeffreys prior Beta(1/2,1/2).”

P5-n5 (Clarity: DESI program overlap in two-sample tests)
- Location: §VI D.c–d, pages 10–11
- Issue: You appropriately warn that bright/dark row-level splits overlap in TARGETIDs. Consider moving the “uniquified whole-catalog” bright/dark result (|z| ≈ 2.0) into the main text next to the row-level 2.1σ to prevent misinterpretation.
- Fix: Present both numbers together; state the overlap caveat before the first mention of |z|.

NIT

P5-nt1 (Typographic spacing and primes)
- Location: Tables and text (match radii “1′′” vs “1.0 ′′”)
- Fix: Use a consistent rendering for arcseconds (e.g., 1″) throughout.

P5-nt2 (Em-dash overuse)
- Location: Multiple
- Fix: Replace long asides delimited by “— … —” with shorter sentences.

P5-nt3 (Accents/LaTeX artifacts)
- Location: Names like Rinc´on, Monotone hyphenation
- Fix: Ensure proper typesetting of accents (Rincón), primes, and equations in final LaTeX.

Audit of abstract and conclusions numerics
- Env-labeled rows 812,793 vs unique spirals 783,820 (791,635 − 7,815): correct.
- Per-class fCW and σ in abstract: match Table II.
- Inter-class range 1.98 pp: correct (0.5034 − 0.4836).
- V-Web void n=428, 2σ half-width ≈ 4.84 pp: correct.
- Phase-2: cross-class ranges 1.7–4.1 pp; pLEE 0.13–0.56; canonical max |σvs monopole| ≤ 1.87σ: matches Table VI.
- Redshift p=0.372; density-quin’ residual 1.87σ; HEALPix p=0.61/0.135/0.413: match to Tables/figures.
- DESIVAST-anchored: nvoid=56,981; fvoid=0.4964 vs non-void 0.4971 ⇒ ∆f=+0.0007: Table VII. OK.
- Three-algorithm DESIVAST: |∆f| ≤ 0.0019; counting floor 1/(2√n) ≈ 0.0016 for n~1.03×10^5; ~1.2σ: consistent with Table VIII.
- Maximal-void HEALPix: σ concentrated in 0-void pixels (−4.75σ), others [−2.04, −0.09], Pearson r=+0.006 (p=0.88): Tables IX and Fig. 8. OK.

Length and focus
The paper is long (27 pages) relative to the core contribution (a null). Much of the valuable diagnostic content could remain, but the narrative would benefit from tighter focus. Recommendation: limit to ≤ 15 pages main text, with detailed pipeline provenance and secondary diagnostics moved to an Appendix or ancillary files.

## Summary recommendation
MAJOR REVISIONS

Justification: The core methodological result appears sound and well-supported by multiple cross-checks, but there are several essential corrections required (contradictory ∼1σ vs ∼9.5σ statement; explicit arithmetic error in a binomial bound; confusing abstract sample ledger; pervasive version-history prose in the body). In addition, major presentational and methodological clarifications are needed (either quantify RSD impacts or more clearly circumscribe V-Web results as secondary; assess CIC deconvolution; clean removal of file paths; unify units/notation; report MC p uncertainties). Addressing these will bring the paper in line with PRD standards for clarity and rigor. The conclusions can likely stand after these corrections.

---

## PASS 2 — self-critique findings (what initial review missed)

Additional findings after second-pass audit (new issues only)

P5-E6 (Permutation p-values claimed “unchanged within MC error” are not)
- Location: §VI E, p. 11
- Text: “p = 0.63/0.089/0.41 stratified vs 0.64/0.10/0.42 free-shuffle re-draws … differ from the headline 0.607/0.135/0.413 by the expected NMC = 1,000 permutation standard error.”
- Problem: At NSIDE=32 the headline free-shuffle p is 0.135, while the stratified re-draw p is 0.089. With NMC=1000, the MC s.e. at p≈0.1 is ≈0.0095, so |0.135−0.089|≈0.046 is ~4.8× the MC s.e.—not “within MC error.” Either the stratification changes the null (plausible) or the two procedures are not directly comparable; in either case, the current wording is misleading.
- Required fix: State explicitly that stratification changes the null distribution; do not characterize 0.135 vs 0.089 as “within MC error.” Report both values with MC uncertainties (e.g., 0.135±0.010 vs 0.089±0.009), and clarify that they reflect different permutation schemes.

P5-E7 (Fourier-wavevector normalization inconsistency)
- Location: §IV A step 9, p. 5
- Text: “ki = 2πni/L with L the box side (scipy fftfreq scaled by 2π/cell)”
- Problem: The parenthetical “scaled by 2π/cell” conflicts with ki = 2πni/L. Using numpy/scipy fftfreq with d=cell gives ki = 2πni/L; multiplying by “2π/cell” would be incorrect. As written, the normalization is ambiguous.
- Required fix: Correct to: “ki = 2πni/L using fftfreq(n, d=cell) and multiplying by 2π,” or equivalent. Remove “2π/cell” phrasing. Confirm units (k in h Mpc−1) after the correction.

P5-E8 (Permutation null does not honor duplicate TARGETIDs)
- Location: §V (Statistical methods), §VI (Results), implicitly throughout permutation-based p-values
- Issue: Many analyses operate on the 812,793-row env-labeled parent that contains duplicate rows for the same TARGETID (program coadds). The label-shuffle permutations appear to shuffle labels at the row level, potentially assigning different labels to duplicate rows for the same galaxy, inflating effective degrees of freedom relative to the data-generating process.
- Required fix: For any permutation on a row-level parent with duplicates, co-shuffle duplicate rows as a block (or run the permutation on the unique-TARGETID parent and map back). Recompute permutation p-values accordingly, or explicitly show that block-shuffling vs row-level shuffling produces indistinguishable p-values within MC error.

P5-M8 (Weighted-per-pixel correlation not fully specified; uncertainty not reported)
- Location: §VIII F, p. 17–18; Fig. 8 caption
- Text: Reports Pearson r = +0.006 (p = 0.88) and an “error-weighted” version rw = +0.004 (p = 0.91, neff ≈ 683).
- Issue: The definition of the weighted Pearson estimator and how p-values and “neff” are obtained is not given. Because σpix is heteroscedastic, the choice of weights and the null distribution of rw matter.
- Required fix: Specify the exact weighted Pearson formula, the weights used, and how p-values and neff were computed (e.g., via parametric approximation or permutation respecting weights). Provide CIs or MC uncertainties. Otherwise, move rw to an Appendix and keep the unweighted statistic in the main text.

P5-M9 (σvs monopole denominator should use p0(1−p0) rather than 0.25)
- Location: §V (last paragraph), Table X, §VIII F
- Issue: σvs monopole is computed with denominator 0.5/√N, i.e., assuming Var = 0.25/N. For tests against p0 = fP5CW ≈ 0.4972, the exact variance is p0(1−p0)/N. The numerical impact is tiny here but avoidable.
- Required fix: Use √[p0(1−p0)/N] in σvs monopole (or state that the 0.3% difference is negligible and retain the simpler form). Make the choice explicit.

P5-M10 (NSIDE inconsistency between text and figures risks confusion)
- Location: §VIII E (Maximal-void HEALPix stratification), Fig. 8
- Text: The stratified binning discussion is at NSIDE=16 (297 occupied pixels), while Fig. 8 shows NSIDE=32 (885 occupied pixels; bottom panel uses ≥200 spirals yielding 1,496 valid pixels).
- Issue: Two NSIDEs are used in adjacent exposition without a clear pointer; readers may assume Fig. 8 corresponds to the NSIDE=16 analysis in §VIII E.
- Required fix: Add one line near §VIII E explicitly noting that Table IX uses NSIDE=16, while Fig. 8 illustrates NSIDE=32 for the correlation study (§VIII F). Cross-reference both to avoid ambiguity.

P5-m7 (Equation (1) formatting is potentially ambiguous)
- Location: §V, Eq. (1), p. 5
- Text: “σpred = ΔfCW / 0.5/√N = 2 · ΔfCW · √N”
- Issue: The inline “ΔfCW / 0.5/√N” can be misread as ΔfCW / (0.5/√N). The equality clarifies it, but best to avoid ambiguity.
- Fix: Present only the unambiguous form σpred = 2 ΔfCW √N, or write σpred = (ΔfCW/0.5) √N with explicit parentheses.

P5-m8 (Jeffreys interval prior not specified in-text where first used)
- Location: §V (Statistical methods), Fig. 3 caption
- Issue: The paper mentions “Jeffreys 95% binomial credible interval” without stating the Beta(1/2, 1/2) prior at first use (only the Fig. 3 caption hints at it later).
- Fix: Add “(Jeffreys prior Beta(1/2,1/2))” at first mention in §V.

P5-nt4 (Minor wording on z-shell selection correction denominator)
- Location: §IX A, p. 19–20
- Text: “the per-shell mean taken over occupied-footprint cells only” vs later “taken instead over all cells inside a redshift-independent HEALPix NSIDE-64 angular footprint intersected with the shell’s radial range.”
- Note: Both are valid cross-checks; adding the exact number of cells used per shell in each variant (or a percentage difference) would improve clarity and reproducibility reading, but this is editorial.

Explanation
These items emerged only on a second pass focused on numerical consistency, procedure comparability, and units/normalization details. The permutation p-value discrepancy (P5-E6) and the duplicate-handling in permutations (P5-E8) affect the validity of some reported p-values. The Fourier k-normalization ambiguity (P5-E7) is a small but important dimensional-consistency fix. The remaining issues improve clarity and statistical rigor without altering the headline conclusions.