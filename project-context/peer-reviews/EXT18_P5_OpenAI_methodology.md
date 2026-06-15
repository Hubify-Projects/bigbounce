# P5 EXT18 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` md5=7bb73989 pages=32
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6963 chars)
**Wall time**: 313.5s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test …” (32 pp)

Scope of review
I evaluated the manuscript for methodological rigor in statistics and data analysis, dimensional consistency, internal arithmetic, error propagation, and congruence between abstract, body, tables/figures and conclusions. I recomputed every quoted percentage, σ, χ2, p-value, and range that can be derived from displayed numbers, checked null-procedure distinctions, and audited look‑elsewhere and multiplicity handling.

Overall assessment
The analysis is extensive and, for the most part, numerically consistent with careful bookkeeping of binomial statistics, σ scaling, permutation nulls, and multiplicity. The DESIVAST-anchored primary test is statistically well-formulated, the two-sample contrasts recompute, and the numerous sensitivity checks are mostly calibrated. However, the paper contains a number of presentation and methodological issues that need to be fixed for PRD standards: (i) reliance on a companion “in preparation” paper as a load-bearing source and inclusion of version-history prose in the body; (ii) frequent embedding of repository file paths/hashes in the main narrative; (iii) a few places where σ from different procedures are juxtaposed without an immediate “not directly comparable” qualifier; (iv) some selection-function and redshift-space caveats are handled, but a small number of claims need harder numbers or relocation to the data-availability section. I list all findings below.

Findings

ESSENTIAL

P5-E1 (Abstract; p.1)
Problem: Load-bearing reliance on an unpublished companion. Abstract cites “Paper IV [3] (in preparation; …) … catalog-wide classifier-monopole systematic …” and uses its ΔfCW = −0.0026 as a predictive reference throughout.
Required fix: Make the manuscript self-contained. Replace any load-bearing use of the unpublished Paper IV with quantities estimated within this manuscript’s parent sample (you already compute fP5
CW = 0.4972 on n = 812,793). Wherever σpred is used, primary figures and text should reference the matched-sample monopole and propagate its uncertainty. Paper IV can be cited as ancillary provenance of the public label set, but not as the sole quantitative source.

P5-E2 (Sec. II, p.3; Sec. IV.A, p.4–5; elsewhere)
Problem: Version-history and preprint-provenance prose in body text. Examples: “earlier preprint versions used the ‘V-Web’ label…,” “Paper IV v1.0.166 … withdrawn … after a provenance audit … synthetic footprint,” “this version standardizes…”.
Required fix: Remove version-history narrative and internal audit commentary from the body. If needed, move a brief clarification to a short footnote or the Data Availability section. PRD manuscripts should read as a final coherent statement of method and results, not a change log.

P5-E3 (Multiple locations: Abstract p.1–2; Secs. IV–X; tables/captions)
Problem: Embedding raw repository pathnames and JSON filenames (e.g., pipelines/p5_desi_chirality/outputs/…) throughout the main text, figures, and table notes.
Required fix: Consolidate all artifact pointers into a single Data & Code Availability section (and/or an Appendix) with a frozen DOI (see P5-M7). Replace in-body file paths with short parenthetical “see Data availability” notes. Keep the main narrative free of file-system internals.

P5-E4 (Sec. VII, Table VII p.15; Sec. VI.A p.8–9; Fig. 6 caption p.14)
Problem: σ values from different null procedures appear side-by-side (raw σfrom half, monopole‑subtracted residual σobs−σpred, and permutation pLEE) without an explicit “not directly comparable” qualifier at each juxtaposition.
Required fix: Add, immediately adjacent to Table VII and anywhere both types co-appear, a sentence stating that raw σ and permutation p-values are different summary statistics and not directly comparable; interpret each within its own null. You do this globally in Sec. V, but PRD requires unambiguous local reminders at every co-display.

P5-E5 (Sec. III.D, p.4; Sec. VI.A p.8–9)
Problem: Use of a mixed row-level parent (812,793 env-labeled rows, 3.56% duplicates) for χ2 tests and σ, with only later clarification that results are reproduced on unique TARGETIDs.
Required fix: Promote the unique‑TARGETID analysis to the mainline where χ2 and key monopole/subtracted residuals are first reported (not only as a cross-check). Explicitly state which parent is used for each headline statistic and give the unique‑galaxy result alongside.

MAJOR

P5-M1 (Abstract p.1–2; Sec. VIII.A p.17)
Problem: The illustrative “0/6” T‑Web void vs DESIVAST hole-membership disagreement is statistically underpowered and could be misread as an inference. You correctly qualify its illustrative nature, but it remains in the abstract’s robustness narrative.
Required fix: Remove the 0/6 statement from the abstract. In the body, keep it only as an anecdotal check (or move to Appendix), clearly labeled “illustrative only; not used for inference” and accompanied by the correct Clopper–Pearson bound (see P5-N2 on typesetting).

P5-M2 (Sec. IX.A p.22–24; selection-weighting)
Problem: The survey-selection correction via per-shell mean subtraction is presented as a “stress test” and yields a dramatic class-population migration. You then claim the chirality null “tightens by a factor ~40” with a 0.05 pp range, but the exact per-class counts and σ values for all four classes are only partially listed in prose.
Required fix: Add a compact table (analog of Table III) for the selection-corrected rebuild (both with and without the interior buffer), listing nclass, nCW, fCW, σfrom half for each class and the omnibus χ2, so the “tightening” claim is auditable at a glance.

P5-M3 (Sec. VII, Table VII p.15)
Problem: The “global max-stat correction across cells” is quoted (pglobal = 0.36 across all nine; 0.27 across six resolved), but the text does not report the number of permutations used for the global coupling, nor how cross-cell correlations were preserved beyond a brief parenthetical.
Required fix: State NMC explicitly for the global max-stat correction and one sentence describing the stream/seed reuse and how per-draw labels were propagated across cells. Add the Monte‑Carlo standard error on pglobal (± value) to show resolution.

P5-M4 (Sec. XIII p.29; RSD quantitative bound)
Problem: The “order-of-magnitude boundary-crossing estimate” invokes “~3–5% of cells near class boundaries” based on internal eigenvalue histograms, without a displayed figure or number table.
Required fix: Either (a) add a small figure or table in Appendix showing the eigenvalue distribution and the fraction within the stated band for Rs=25 h−1 Mpc; or (b) replace the 3–5% with a clear “heuristic” label and remove the numeral, to avoid implying a measured quantity.

P5-M5 (Sec. VIII.E p.20; footprint restriction)
Problem: The “footprint-restricted control” defines the usable footprint as the union of hole-sphere angular discs at NSIDE=64 intersected with their radial span. This is a bespoke proxy for the DESIVAST footprint, not its official mask.
Required fix: Clearly label this as a custom proxy in the table caption and the text, and add a sensitivity note (already hinted) on how results change under a stricter (e.g., maximal‑sphere only) angular mask. Alternatively, provide a pointer to an official DESIVAST angular mask if released.

P5-M6 (Paper length and structure)
Problem: At 32 pages, the paper reads more like a lab notebook with in-line artifact paths, cross-check inventories, and internal QA notes. This obscures the main methodological result.
Required fix: Reduce main text to ≤24 pages by moving the HEALPix scans, density/quartile/z‑quartile decompositions, and the ASTRA per-object cross-check to a single Appendix. Keep the DESIVAST three‑algorithm test (primary), the T‑Web headline table, and the Phase‑2 sweep in the main text.

P5-M7 (Appendix C p.31; data/code availability)
Problem: The manuscript promises “a DOI-minted archival snapshot … accompanies journal submission,” but no DOI is provided. Numerous in-text pointers rely on that archive.
Required fix: Before acceptance, provide a stable DOI to an archival snapshot (Zenodo or equivalent) matching the exact code/data version used. Replace “accompanies” with the actual DOI and date. Ensure all in-body artifact references are reachable from that DOI.

MINOR

P5-m1 (Sec. V p.6–7; Eq. (2))
Problem: The Bonferroni threshold formula uses erfc−1; for readers, the two-sided tail treatment can be ambiguous.
Required fix: Add a parenthetical “two-sided threshold; per-bin tail α/(2K)” directly under Eq. (2). You already verbalize it; mirror that in the equation note.

P5-m2 (Sec. III.D p.4; Table I)
Problem: The leg counts (BASS+MzLS 688,608; DECaLS 1,538,880; DES 4,724) sum to 2,232,212 after dedup, matching the “Matched primary after dedup,” but this is not stated.
Required fix: Add a brief line clarifying that the three imaging legs partition the matched-deduped set (sum equals the total), to avoid confusion.

P5-m3 (Sec. VI.D p.11; quartiles)
Problem: The statement “cluster Q1 (ρ̄ = 1.55) is less dense than filament Q4 (ρ̄ = 1.86)” is correct but deserves a clarifying reminder that the quartiles are constructed within class.
Required fix: Add: “Quartiles are within-class by the same NN-interpolated log-density covariate; cross-class quartile means overlap by construction.”

P5-m4 (Sec. IV.A footnote p.5)
Problem: The distance-units “multiply-by-h” explanation is correct but nonstandard phrasing could confuse.
Required fix: Add a one-liner: “Numerically: D[h−1 Mpc] = h × D[Mpc] (since 1 h−1 Mpc = (1/h) Mpc).”

P5-m5 (Sec. X, Table XIV p.28)
Problem: You report T-Web-on-overlap classes with two bins having n < 100 but later say you filter classes with n ≥ 100.
Required fix: In the table, add a note: “Max |σ| and range computed excluding bins with n < 100,” and grey or footnote the under‑100 T‑Web bins.

P5-m6 (Sec. XII.C p.28)
Problem: “leaving no room for a residual environment-dependent chirality of the Shamir 2022 amplitude” is strong wording.
Required fix: Rephrase to: “our per-class constraints at ≤ O(1 pp) in well-populated classes are inconsistent with a 2–4 pp class-conditional asymmetry at DESI DR1 sensitivity.”

P5-m7 (Throughout)
Problem: Occasional unexplained acronyms upon first use (e.g., “NSIDE” appears first in abstract).
Required fix: Define HEALPix/NSIDE at first mention in the body (a footnote is fine) and in the abstract avoid acronyms, or expand once.

P5-m8 (Sec. VIII.C p.18–19; three‑algorithm totals)
Problem: The interior vs effective void counts could be misread as contradictory.
Required fix: Add a footnote clarifying “published interior-void counts vs. total effective-void counts” and point to the exact DESIVAST table.

NITS

P5-n1 (Sec. VIII.A p.17)
Problem: Typesetting of the one-sided 95% upper bound for 0/6 successes: “1 − 0.051/6” likely lost the exponent caret in typesetting.
Required fix: Replace with “1 − 0.05^{1/6} ≈ 0.39” and similarly format “α^{1/n}”.

P5-n2 (Sec. VII, Fig. 7 caption p.16)
Problem: “per-cell range of fCW across {void, wall, filament, cluster} in percentage points” — add “pp” for compactness where space allows.
Required fix: Append “(pp)” after “percentage points.”

P5-n3 (Sec. VI.E, Table VI p.13)
Problem: Present p-values with two decimals everywhere or with the Monte‑Carlo SE; currently mixed (0.135, 0.607).
Required fix: Either round consistently to two decimals or include “± seMC” once per table.

P5-n4 (Appendix B tables p.31)
Problem: The labels “CW” and “CCW” are used without a table note explaining the rounding of fCW.
Required fix: Add: “fCW rounded to 4 d.p.; σ and χ2 computed from integer counts.”

Arithmetic/consistency audit (selected)

- Table III (p.8): All fCW and σfrom half recompute from counts. Range 0.5034 − 0.4836 = 0.0198 (1.98 pp) matches text. χ2(3)=3.55; p≈0.31 stated; integers are provided in Appendix B.

- Void bin σ and pp offset in abstract: σ = −0.68; corresponding fractional offset = −0.68×(0.5/√428)= −0.0164 = −1.64 pp; 1σ half‑width 1/(2√428)=0.0242 (2.42 pp); 2σ half‑width ≈ 4.84 pp; consistent.

- σpred computed from Δf = −0.0026: Filament N=408,187 → σpred = 2×(−0.0026)×√N = −3.32; Cluster N=397,505 → −3.28 (matches p.8–9).

- DESIVAST primary (Table VIII, p.18): Δf = +0.00067; SE ≈ 0.5×√(1/56,981 + 1/621,964) = 0.00219; z=0.31; p=0.76; 95% CI [−0.0036, +0.0050]: all recompute exactly.

- Three-algorithm contrasts (Table X, p.19): Reported SE, z, p, and 95% CIs recompute from counts.

- Bonferroni thresholds: K=5, α=0.01 → |σ|≈3.09; K=5, α=0.05 → |σ|≈2.58; K=4, α=0.05 → |σ|≈2.50; K=4, α=0.01 → |σ|≈3.02; K=9, α=0.05 → |σ|≈2.77. All consistent.

- Permutation seMC: For NMC=1000, seMC ≈ √(p(1−p)/1000) = 0.010–0.015 for the reported p ranges; consistent with text.

- Cramér’s V (Sec. VI.D p.12): V=√(χ2/n)=√(4932/811,609)=0.078; matches.

- Selection-corrected rebuild (Sec. IX.A p.24): fCW per class (void 0.4971, wall 0.4968, filament 0.4973, cluster 0.4973) → cross-class range 0.0005 = 0.05 pp; matches claim.

Dimensional/algorithmic checks

- Tidal-tensor pipeline steps are dimensionally consistent (δ dimensionless; Φ(k) ∝ −δ/k2; Tij(k) ∝ kikjδ/k2). Eigenvalue thresholding at λth defined on the windowed normalization is acceptable; you state the CIC window is not deconvolved.

- Distance-units convention (Mpc → h−1 Mpc via multiplication by h) is properly justified (P5-m4 requests a clarifying line).

- Dilation rule ⌈Rs/cell⌉+1 is sensible and verified by re-runs.

Standalone-reader test

- With P5-E1 fixed, the manuscript becomes self-contained: DR1 selection, cross-match radius, environment pipeline, and statistics are detailed. Current wording still leans on the unpublished Paper IV for the catalog monopole; replacing that with the matched-sample estimate resolves the issue.

Effect sizes

- For the huge class×program χ2, Cramér’s V is given (0.078). For other χ2 (4×2 homogeneity), the effect is small; you already interpret qualitatively. Fine.

Abstract-last drift sweep

- After reading the body, the abstract’s numerical claims (class fractions, σ, χ2, p, Phase‑2 pLEE span 0.13–0.56, ΔfCW=+0.0007 with DESIVAST) are supported by the body/tables. The only overreach is the 0/6 illustrative check (P5‑M1).

Bibliography

- Citations appear consistent (Planck 2018 A&A 641 A6; Tempel 2014 A&A 566 A1; Rincón et al. 2025 ApJ 982, 38). Preprints [11],[12] are correctly marked as preprints; claims are framed as contemporaneous consistency checks.

## Summary recommendation
MAJOR REVISIONS

The central statistical result is sound and the numbers check out. However, the manuscript, as written, does not meet PRD presentation and independence standards: it relies on an “in preparation” companion for a load‑bearing quantity, includes version-history prose and many internal file‑path references in the main text, and needs clearer local caveats where multiple σ’s/p-values are juxtaposed. Addressing the essential and major items above will produce a clean, self-contained, and publishable methods paper.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (second-pass audit)

The items below are new relative to my first report. I do not repeat earlier issues.

ESSENTIAL

P5-E6 (Null RNG seeding; Sec. V p.6–7; Sec. VII p.15)
Problem: The manuscript states that “the same config-level seed initializes each scan family’s generator, so identical underlying random streams are shared across families,” with a spot re-draw only for the HEALPix scan. Reusing identical RNG streams across distinct tests can couple permutation outcomes across families and complicate any global look-elsewhere accounting.
Required fix: Use independent seeds for each test family and for each Phase-2 cell (documenting the seeds), or explicitly demonstrate with additional re-draws that all reported permutation p-values are stable across independent streams for every family. If a global max-statistic is reported across multiple families, ensure permutations are propagated from a single draw consistently and document the scheme.

MAJOR

P5-M8 (Speculative EFT appendix; Appendix A)
Problem: Appendix A introduces a bespoke parity-violating toy operator and translates the empirical null into a “bound” on gϕ|∇ϕ| without a derivation tied to a gauge-invariant observable or a published framework. Even with caveats, this reads as a theoretical inference unsupported by the data analysis.
Required fix: Either (i) remove Appendix A (or move it to a brief “Outlook” paragraph without equations), or (ii) provide a concrete derivation with references showing how the measured class-conditional ΔfCW maps to a well-defined, gauge-invariant operator and transfer function, and clearly state the statistical bound with propagated uncertainties. As written, this section risks overreach relative to PRD standards for empirically focused manuscripts.

P5-M9 (Concurrent‑literature volume‑fraction comparison; Sec. IX.C p.25)
Problem: The claimed +8–18 pp “excess void fraction” relative to Ref. [11] is asserted qualitatively from tracer- and volume-mismatched runs. No like-for-like comparison (same tracer, same volume/geometry) is shown to substantiate the stated range.
Required fix: Either perform a like‑for‑like subvolume/tracer re-run to quantify the differences, or explicitly label the +8–18 pp as heuristic and remove the numerical range. If retained, report the exact numbers for your classifier restricted to the 800 Mpc cube and tracer used in Ref. [11], and vice versa if available.

P5-M10 (RSD Monte‑Carlo ± notation; Sec. VIII.A p.17)
Problem: The RSD sensitivity test reports “76,490 ± 161” without specifying whether “±” is the standard deviation across realizations or the standard error of the mean.
Required fix: State explicitly whether the uncertainty is SD or SE, and report both if helpful. For completeness, also report the dispersion of ΔfCW across realizations (SD), not just its range.

MINOR

P5-m9 (Grid‑resolution convergence presentation; Sec. IX.A p.24)
Problem: The Ngrid ∈ {128^3, 256^3, 384^3} convergence check is described in prose, but no compact table is given with nclass, fCW, and σ for each resolution.
Required fix: Add a small table (or an Appendix table) summarizing class populations and fCW per grid, so readers can audit convergence numerically.

P5-m10 (Monopole‑subtracted residual rounding; Table XII p.21)
Problem: Recomputing σvs monopole for the filament class using the stated fP5_CW = 0.4972 and the integer counts yields ≈ +1.03, whereas Table XII lists +0.99. The difference is small but suggests a rounding/base-parent mismatch (row-level vs. unique‑TARGETID).
Required fix: Clarify which parent and monopole (row‑level 812,793 vs. unique 783,820; fP5_CW = 0.49719 vs. 0.4972) are used for Table XII. Consider adding both versions or fixing all σvs monopole to a single declared parent so all values recompute exactly.

P5-m11 (Permutation families and global coupling; Sec. VII, Table VII p.15)
Problem: For the “global max-stat correction across cells,” the text gives pglobal but not the number of coupled permutations used nor the Monte‑Carlo SE on pglobal.
Required fix: State the exact NMC used for the global coupling, confirm that the same permuted label assignment was propagated to all nine cells per draw, and quote pglobal ± seMC.

P5-m12 (Mixing Bayesian CIs with frequentist tests; multiple)
Problem: The manuscript alternates Jeffreys 95% binomial credible intervals with frequentist χ^2, z, and permutation p-values without a local reminder that the intervals and tests live in different inferential paradigms.
Required fix: Add a one-sentence note (e.g., in Sec. V and once where CIs and p-values are juxtaposed) that Jeffreys intervals are Bayesian summaries and are not used for hypothesis testing here; tests are based on the frequentist procedures described.

P5-m13 (Selection-corrected shell build: completeness weights; Sec. IX.A p.23)
Problem: The completeness‑weighted rebuild (δw = ng/(α nr) − 1) is crucial and only described in text with large class‑fraction shifts. A compact tabulation of class counts and fCW for the weighted vs. unweighted window would make the “both are null” claim auditable.
Required fix: Add a small table with (weighted vs. unweighted) nclass, fCW, and σ for the in‑window (0.01 < z < 0.50) run.

P5-m14 (Regression multiple‑testing note; Sec. VI.B p.9–10)
Problem: The logistic regression includes several covariates and highlights a single marginal “classifier confidence” predictor (p ≈ 0.02) without multiple‑testing context.
Required fix: Note that no multiplicity correction is applied to individual coefficients; emphasise that inference relies on the joint Wald tests (which are null).

NITS

P5-n5 (Caption clarity on units; multiple)
Problem: Some captions report ranges in “percentage points” without “(pp)” shorthand introduced, while the text uses “pp.”
Required fix: Standardize captions to include “(pp)” after the first occurrence of “percentage points.”

P5-n6 (Terminology in Sec. VIII.E p.20)
Problem: The text alternates between “any-hole” and “hole‑union” membership; both mean the same construction.
Required fix: Use one term consistently and parenthetically define it once.

P5-n7 (Section‑reference consistency; multiple)
Problem: Mixed “Sec.” vs “§” and A/B/C subsection references; occasionally a subsection letter is used without the section number (e.g., “§VIII E” vs “Sec. VIII.E”).
Required fix: Normalize section reference style throughout for PRD house style.

Explanation of completeness
I re-ran arithmetic checks for all tabulated counts and key claims, verified σ computations directly from integer counts, spot-checked p‑values and ranges, compared figure captions with body claims, scanned equations for unit consistency, and cross-checked internal references. Most numbers remain self‑consistent; the new items focus on RNG/LEE rigor, speculative theory overreach, explicit tabulation omissions that impede auditability, and a few small presentational clarifications.