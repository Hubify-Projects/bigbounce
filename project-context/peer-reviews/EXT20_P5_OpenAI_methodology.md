# P5 EXT20 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` md5=3e5d3757 pages=32
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6060 chars)
**Wall time**: 467.3s

---

Referee report for PRD on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample”

Overview
The manuscript cross-matches a very large image-based galaxy chirality catalog to DESI DR1 spectroscopy, constructs a tidal-tensor (T-Web) cosmic-web classification, and tests whether the clockwise (CW) fraction of spiral galaxies depends on large-scale environment. A DESIVAST void catalog is used as the primary, more robust void definition, and multiple secondary checks (T-Web sensitivity sweep, Tempel FoF, ASTRA EDR, redshift/density/sky maps) are reported. The load-bearing statistical statements are omnibus homogeneity tests, binomial z-scores, permutation look-elsewhere p-values, and two-sample contrasts for the DESIVAST void vs non-void comparison.

Methodologically, many numerical claims are traceable, and most arithmetic I checked from the tables and counts is consistent. That said, the manuscript in its current form does not meet PRD standards for presentation and provenance. It contains extensive version-history language and repository-internal file paths throughout the main text, relies on an “in preparation” companion (Paper IV) for load-bearing inputs, includes a speculative EFT appendix that is not derived, and lacks a concrete frozen DOI for the code/data snapshot it repeatedly cites. I list detailed issues and required fixes below.

Findings and required actions

ESSENTIAL

- P5-E1 (Sections I–XI; multiple pages including p.3, p.4–5, p.6–7, p.8–22): Version-history and internal-repository artifacts embedded in the main text
  Problem: The paper repeatedly includes version tags, audit history, and internal filenames/paths (e.g., “Paper IV v1.0.166… withdrawn…”, “artifact filename pipelines/p5_desi_chirality/env_finder/01_compute_vweb.py…”, “deterministic seed”, “outputs/…json”). This is inappropriate for the main PRD article and reads like an internal lab report.
  Required fix: Remove all version-history prose, internal pathnames, and pipeline filenames from the main text and figures. If you wish to preserve them for reproducibility, move them to a dedicated Data and Code Availability appendix or to a separate Supplemental Material document. Keep the main text citation-style and journal-standard.

- P5-E2 (Abstract; Secs. II–V; passim): Load-bearing reliance on an unpublished companion (“Paper IV”) violates the standalone-reader test
  Problem: The chirality labels, class definitions, the catalog-wide monopole value (ΔfCW ≈ −0.0026), and several interpretive steps rely on “Paper IV [3] (in preparation).” Although you list a HuggingFace dataset slug, a PRD reader must not have to consult an unpublished companion to understand or reproduce the key inputs used here.
  Required fix: Make the manuscript self-contained regarding (i) the definition of the chirality labels used (at least a concise operational description of how “class_eq ∈ {CW, CCW}” was determined, test-time augmentation, and any quality cuts used here), and (ii) the monopole baseline you subtract. Either (a) rely exclusively on the observed matched-sample monopole (you already provide fP5_CW = 0.4972 and use it in Table XII) and eliminate all uses of the Paper IV-wide ΔfCW prediction from inference, or (b) provide a stable public DOI to the precise version of the chirality catalog used here and to a citable manuscript that defines the classifier and reports the monopole value you import. In any case, do not make the inference in this paper depend on an “in preparation” companion.

- P5-E3 (Appendix C, p.31–32; Data availability): Missing DOI/frozen release for code/data
  Problem: You state “A DOI-minted archival snapshot of this directory accompanies journal submission,” but no DOI is given.
  Required fix: Provide the exact DOI (e.g., Zenodo) of the frozen code/data snapshot corresponding to the manuscript’s results, together with the precise chirality-catalog version identifier (tag/commit) used. Without a DOI, reproducibility cannot be audited.

- P5-E4 (Appendix A, pp.30–31): Speculative, non-gauge-invariant EFT “toy mapping” presented as an appendix without derivation
  Problem: Appendix A introduces a parity-violating operator that you explicitly acknowledge is not gauge- or rotation-invariant and is not derived from the cited literature. Including such speculative content in a methods-focused PRD article is inappropriate and risks confusing readers about the paper’s scope and rigor.
  Required fix: Remove Appendix A entirely, or move it to clearly labeled Supplemental Material and reframe as purely speculative context with no pretension of constraint-setting. The main paper should present only derived, defensible results.

- P5-E5 (Sec. V, p.6–7; throughout): Keep sigma conventions orthogonal and non-comparable every time they are juxtaposed
  Problem: You use several σ notions: σfrom half (one-sample binomial), σpred (Paper IV monopole projection), and σvs monopole (residual). While many passages do note non-comparability, there are locations where raw σfrom half values (e.g., −4.66σ) and residuals are discussed in close succession without an explicit reminder (e.g., Sec. VI D opening, Fig. 5 caption).
  Required fix: At every place where raw σfrom half and any monopole-projected or -subtracted σ appear side-by-side, explicitly state that they are not directly comparable and identify which σ is being used. Add a one-sentence reminder in the captions of Figs. 3, 5, 6, 7 and next to Tables III, VII, and XII.

MAJOR

- P5-M1 (Overall length and scope; entire manuscript): The paper is substantially longer than needed for the claimed contribution
  Problem: The main claim is a set of null results on environment-dependent chirality, with a robust DESIVAST void vs non-void primary analysis and a T-Web cross-check. The current 32-page manuscript contains extensive pipeline diagnostics, RNG stream discussions, and path-level references that could be condensed or moved to Supplemental Material.
  Required fix: Reduce the main text to ≤ 20 pages by moving the Phase-2 cell-by-cell minutiae, most of the per-pixel sky scans, and nearly all internal-artifact references to Supplemental Material. Retain in the main text the primary DESIVAST analysis, the T-Web cross-check, and one concise selection-function robustness test.

- P5-M2 (Sec. IV.A step 2, p.5): h-unit conversion clarity
  Problem: You devote a footnote to the h-conversion convention, presenting an “alternative χ[Mpc]/h” you then reject. The correct statement is simply that numeric values in h−1 Mpc are obtained by multiplying Mpc by h. Presenting a competing convention risks confusion.
  Required fix: Remove the “alternative convention” and keep a single, unambiguous statement: χ[h−1 Mpc] = h × χ[Mpc], with the numerical example. If you must mention differing usages, do so tersely and show equivalence with consistent unit definitions.

- P5-M3 (Sec. XIII, pp.28–29): Redshift-space distortion (RSD) bound is heuristic; a quantitative uncertainty budget is missing
  Problem: You state that the implied contamination is “sub-percent (~0.2 pp)” based on scalar displacement, but also that anisotropic eigenvalue deformation dominates and is not separable without reconstruction. As written, the reader cannot assess how much of your null is conditioned on this choice.
  Required fix: Soften any quantitative RSD claims in the main text to a qualitative statement unless you provide a quantitative uncertainty budget (e.g., via a small reconstructed-position reclassification test at Rs = 25 h−1 Mpc on a subvolume). Make explicit that all main results are redshift-space statements, and avoid claiming a numeric contamination floor without a demonstrable bound.

- P5-M4 (Abstract, Sec. VIII.B, Table VIII, p.18): Primary-void estimator declaration and family-wise error rate
  Problem: While you later introduce a Bonferroni-5 family for DESIVAST variants, the abstract’s “headline result” references a single ΔfCW = +0.0007 without immediately noting that five estimators were considered and controlled together.
  Required fix: In the abstract and the main-result paragraph of Sec. XV, explicitly say that the DESIVAST primary comprises five estimators (three sphere-based and two catalog-native), controlled at Bonferroni-5 family-wise α = 0.05, with all |zΔ| ≤ 1.25. This removes any perception of post-hoc estimator selection.

- P5-M5 (Secs. VI B–E; Table VI; p.13): MC permutation sample size vs reported precision
  Problem: You report permutation p-values to three decimals with NMC = 1000 (seMC ~ 0.01–0.015) and discuss stream-to-stream fluctuations.
  Required fix: Round all permutation p-values to two decimals in the main text and tables, and include the Monte Carlo standard error (or a footnote stating seMC ≈ sqrt(p(1−p)/NMC)). Alternatively, increase NMC to 10,000 for the headline HEALPix and Phase-2 max-stat tests if you wish to keep three decimals.

MINOR

- P5-m1 (Abstract; passim): Define “pp” at first use
  Problem: “pp” (percentage points) appears in the abstract before it is defined.
  Required fix: Add “pp = percentage points” at its first occurrence in the abstract.

- P5-m2 (Sec. VI A, Fig. 3; p.9): Confidence intervals vs duplicate rows
  Problem: You draw Jeffreys CIs on an env-labeled parent with 3.56% duplicates and note a worst-case 1.9% inflation. This is correct, but the caption only briefly states it.
  Required fix: Add in the caption that the displayed CIs are approximate because of duplicate rows, and point to the unique-galaxy recompute for exact inference.

- P5-m3 (Sec. VII, Table VII; p.15): Label “grid-unresolved” rows more prominently
  Problem: The Rs = 10 h−1 Mpc rows are below grid resolution and excluded from robustness, but appear in the same table block.
  Required fix: Shade or otherwise visually separate the Rs = 10 rows, and add a one-line reminder in the caption that they are excluded from robustness claims.

- P5-m4 (Sec. IX.B, Fig. 9; pp.24–26): Clarify that the Tempel mapping is approximate
  Problem: The “isolated/small group/filament-like/cluster-like” mapping is not a 1-1 match to T-Web classes.
  Required fix: Add a one-sentence reminder in the caption that the mapping is approximate and class definitions differ (richness vs tidal eigenvalue), so only the filament comparison is meaningfully powered.

- P5-m5 (Typography; passim): Accents and hyphenation
  Problem: Misrendered accents (e.g., “Cram´er’s”), repeated long dashes, and stray spacing occur.
  Required fix: Standardize typography (“Cramér’s”), remove double spaces/hyphenation artifacts.

NITS

- P5-n1 (Sec. III.D, p.4): Clarify why 6.6 mas median separation arises
  Problem: You ascribe it to shared astrometry. A brief parenthetical “due to common DR8 Tractor astrometry” is fine, but consider stating explicitly that this implies the 1″ radius is purely conservative.

- P5-n2 (Fig. 1 caption, p.4): Label axis “redshift z”
  Problem: The current “DESI z” is clear but nonstandard.
  Required fix: Change x-axis label to “redshift z”.

- P5-n3 (Sec. VI D, Table V; p.11): Provide units for ρ¯
  Problem: You define ρ¯ as mean of log10(1+δsmooth). Note it’s dimensionless in the table caption.

Audit of headline scalars and internal arithmetic
I recomputed all load-bearing numbers quoted in the abstract and conclusions from the displayed counts/tables:

- Table I matched counts, chirality-relevant n = 791,635: consistent with abstract.
- T-Web class fractions and σfrom half (Table III): fvoid = 0.4836 (N = 428, σ = −0.68), fwall = 0.5034 (N = 6,673, σ = +0.55), ffilament = 0.4980 (N = 408,187, σ = −2.61), fcluster = 0.4963 (N = 397,505, σ = −4.66). All σ recompute from counts to the stated values.
- Range across classes = 1.98 pp: 0.5034 − 0.4836 = 0.0198.
- Omnibus χ2 = 3.55, 3 d.o.f., p = 0.31 (Table XVI counts): consistent.
- DESIVAST primary void-vs-non-void contrast (Table VIII): ΔfCW = +0.0007 with SE = 0.00219 → zΔ = +0.31, two-sided pΔ = 0.76: consistent.
- DESIVAST three-algorithm robustness (Table X): all |ΔfCW| ≤ 0.0019 (sphere) and ≤ 0.0037 (catalog-native), with zΔ magnitudes ≤ 1.25: consistent.
- HEALPix max-|σ| p-values (Table VI): NSIDE = 16/32/64 p = 0.607/0.135/0.413 with |σ|obs within the null |σ|max,99 values: consistent with NMC = 1000.
- Phase-2 sweep (Table VII): range and nvoid values, max residuals ≤ 1.64σ for resolved Rs ∈ {25, 50} cells; all label-shuffle pLEE ≥ 0.13: consistent.
- Density-quintile residuals (Table IV): maximum |σobs − σpred| = 1.87, below Bonferroni-5 |σ| ≈ 3.09: consistent.
- Bright vs dark whole-catalog difference (Table XV): 0.4970 vs 0.5051 (difference 0.81 pp), |z| ≈ 1.95 unique-galaxy: consistent.
- Cramér’s V for T-Web×program (Table XVII): V = sqrt(χ2/n) = sqrt(4932/811609) ≈ 0.078: consistent.

Abstract-last drift sweep
Every quantitative claim I checked in the abstract maps to a number or table in the body. One presentational adjustment is needed (P5-M4): explicitly note in the abstract that the DESIVAST primary comprises five estimators controlled as a family (you already do this in Sec. V.B/Table II), to avoid any perception of post-hoc selection.

Provenance surfaces
The paper promises a DOI-minted archive but provides no DOI. This must be remedied (P5-E3). The extensive inclusion of file paths and version tags throughout the main text should be moved to Supplementary or excised (P5-E1). The chirality-catalog version must be pinned to a stable public release (P5-E2).

Effect sizes
Where appropriate, you include effect sizes (e.g., Cramér’s V = 0.078 for the large χ2). This is good. Keep that practice wherever large-χ2/small-p results appear.

## Summary recommendation
MAJOR REVISIONS

The core statistical analysis appears careful and internally consistent, and the primary DESIVAST-based null result is supported by multiple cross-checks. However, the manuscript does not yet meet PRD standards due to (i) pervasive version-history/path artifacts embedded in the main text, (ii) reliance on an unpublished companion for load-bearing inputs, (iii) lack of a concrete DOI for the frozen code/data, and (iv) inclusion of a speculative, non-derived EFT appendix. Addressing the essential items (P5-E1–E4) and the major presentation/clarity issues (P5-M1–M5) is required before the scientific content can be fully evaluated for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS AFTER SECOND-PASS AUDIT

New issues only; items from the first report are not repeated.

ESSENTIAL

- P5-E6 (Sec. VI D, Table V; density variable definition vs numbers): Inconsistent scale for the reported density statistic
  Problem: The caption states that ρ̄ is “the quartile mean of log10(1 + δsmooth)”. The tabulated values (e.g., ρ̄ = 1.55–2.21 for cluster quartiles; 0.90–1.86 for filament quartiles) are far too large for log10(1 + δ) at Rs = 25 Mpc/h (they imply overdensities of 10^1.5–10^2.2 ≳ 30–160), but are perfectly plausible if ρ̄ actually denotes the linear density contrast 1 + δsmooth (i.e., density relative to the mean). Required fix: Correct the definition to match the numbers (likely ρ̄ ≡ ⟨1 + δsmooth⟩), or, if the log10 definition is intended, correct the table values and all dependent text. Also state explicitly that the variable is dimensionless.

- P5-E7 (Fig. 9 vs text; comparability of panels): Non-like-for-like visualization on the T-Web side of the Tempel cross-validation figure
  Problem: The left panel shows the full-sample canonical T-Web result “as reference,” while the right panel shows the Tempel overlap. The body’s quantitative “like-for-like” comparison is T-Web-on-overlap vs Tempel-on-overlap, but that T-Web-on-overlap distribution is not what is plotted on the left. This invites a visual misread (left vs right panels are not commensurate). Required fix: Replace the left panel with the T-Web-on-overlap distribution (the one actually used for the 0.29 pp filament concordance), or add an additional panel showing T-Web-on-overlap and make the non-comparability explicit in the caption.

MAJOR

- P5-M6 (Claims of “largest”/novelty; Abstract/Sec. VIII B): Unqualified novelty claim
  Problem: Statements like “to our knowledge, the largest matched-sample environmental-dependence test of spiral chirality in DESI DR1 to date” are not supported with a concrete comparison (scope, sample size, prior art bounds). Required fix: Either qualify the claim narrowly (e.g., “within DESI DR1, using DESIVAST voids”) and cite prior DESI/Legacy analyses, or remove the novelty language.

- P5-M7 (Sec. VII, Table VII; global max-stat LEE): Missing Monte Carlo details for the across-cells max-stat correction
  Problem: You report a “global max-stat correction across cells” with pglobal = 0.36 (all nine) and 0.27 (resolved six) but do not state NMC nor the corresponding seMC for these global tests (you do for per-cell tests). Required fix: Report NMC used for the global max-stat permutation and give either seMC ≈ sqrt(p(1−p)/NMC) or round pglobal to two decimals with a brief note on MC precision.

- P5-M8 (Sec. VIII E, RSD fixed-void-geometry perturbation): Summary statistics for ΔfCW under the Monte Carlo not fully reported
  Problem: You present the range of ΔfCW across 200 LOS-perturbation realizations ([−0.34, +0.37] pp) and the max two-sample |z| (1.93), but do not report the mean and standard deviation of ΔfCW over realizations. Required fix: Add ⟨ΔfCW⟩ ± SD over the 200 draws (void and non-void), so the reader can assess stability more quantitatively; keep the “range” as supporting context.

MINOR

- P5-m6 (Sec. VI D, first sentence): σ-type misuse in prose
  Problem: “The catalog-wide-monopole-projected cluster-class deviation of −4.7σ…” here “−4.7σ” is the raw σfrom half (Table III), not a monopole-projected quantity. Required fix: Rephrase to “the observed (raw) deviation of −4.7σ, which is attributable to the catalog-wide monopole,” or similar, to avoid σ-type conflation at this prominent spot.

- P5-m7 (Sec. VI D, Table V caption and column header): Units/definition reminder
  Problem: Even after correcting P5-E6, the table should explicitly state “dimensionless” for ρ̄ and clearly indicate whether it is 1 + δsmooth or log10(1 + δsmooth). Required fix: Update the caption/column header accordingly.

NITS

- P5-n4 (Sec. VIII F, Table XII): Minor rounding drifts
  Observation: Two entries show small rounding inconsistencies — void row lists fCW − fP5_CW = −0.0135 vs −0.0136 from 0.4836 − 0.49719; filament σvs monopole is listed as +0.99 while a direct recomputation using the stated denominator gives ≈ +1.02. Required fix: Harmonize rounding to a consistent rule (e.g., 3–4 decimals for fractions, 2 decimals for σ), or footnote any intentional rounding choices.

Explanation of coverage
- Arithmetic (A): I rechecked all headline σ, χ2, ranges, permutation p-values, and binomial contrasts used in the abstract and conclusions. With the exception of the small rounding drifts noted in P5-n4 and the density-scale inconsistency in P5-E6, the numbers recompute from the displayed counts.
- Figure-caption vs body (B): The main new mismatch is Fig. 9 (P5-E7). Other figures are consistent with the body text and units once captions are read carefully.
- Dimensional consistency (C): Main equations are dimensionally consistent; the only scale inconsistency appears in Table V (P5-E6).
- Internal cross-references (D): Spot checks of section/table/appendix references resolve correctly.
- Null-procedure comparability (E): A fresh instance of σ-type conflation was found in Sec. VI D’s opening sentence (P5-m6); otherwise, the paper mostly maintains the distinctions.
- Abstract faithfulness (F): Each abstract claim maps to a computation or table in the body; no new discrepancies found.
- Unsupported novelty (G): One novelty claim (P5-M6) should be qualified or dropped.
- Unquantified hedges (H): Where “consistent with” appears, deltas and uncertainties are generally given; the RSD Monte Carlo could use a mean±SD (P5-M8).
- Appendix vs main (I): No new inconsistencies beyond those already flagged in the initial review (Appendix A scope; Appendix C DOI).
- Stale numbers (J): No new stale-number inconsistencies found beyond minor rounding (P5-n4).

Overall, aside from the density-variable mislabel (P5-E6) and the non-like-for-like Fig. 9 presentation (P5-E7), the second pass did not uncover additional load-bearing numerical inconsistencies.