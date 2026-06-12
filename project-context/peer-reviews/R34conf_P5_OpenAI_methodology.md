# P5 R34conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.66.pdf` md5=46f419a3 pages=31
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5540 chars)
**Wall time**: 337.4s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test …” (P5)

Scope of review
I evaluated the methodology, statistical validity, internal arithmetic consistency, dimensional analysis, and reproducibility claims across the full 31-page manuscript, including all figures, tables, equations, captions, and abstract statements. Below I list all issues found, classified by severity, with page-accurate citations, the problematic text, and a required fix.

ESSENTIAL

P5-E1 (Abstract + throughout; multiple pages)
Problem: Internal versioning/review-log prose and “earlier draft” language appear repeatedly in the body of the paper. Examples include:
- Title block: “Dated: June 2026 — v0.1.66-2026-06-11”
- Sec. II, p. 3: “an earlier harmonic-space … was withdrawn in Paper IV v1.0.166…”
- Sec. VI D, p. 12: “An earlier draft quoted filament bright/dark n … and is withdrawn…”
- Sec. VII, p. 13: “An earlier draft of this table reported… and is withdrawn…”
- Sec. VIII D, p. 18: “An earlier draft reported nvoid = 86,276 / 64,514 … reproduce exactly only under a zone-indexing defect…”
These are not acceptable in a PRD article and compromise the archival record.
Required fix: Remove all “earlier draft,” “withdrawn,” internal version tags, and pipeline-debug commentary from the main text. Present only the final, audited numbers and analysis narrative. Move any provenance discussion to a short footnote in a Reproducibility Appendix if absolutely necessary.

P5-E2 (Self-containedness; multiple pages)
Problem: Heavy reliance on a companion work “Paper IV” (not peer-reviewed) for the catalog-wide monopole ΔfCW and other classifier properties. While some analyses in this paper are independent of Paper IV (e.g., the primary DESIVAST two-sample contrasts), many interpretive statements and predicted σ values use ΔfCW from Paper IV as a load-bearing quantity. A PRD article must remain intelligible and quantitatively reproducible without requiring the reader to consult an unpublished companion.
Required fix: Make the paper self-contained by:
- Using the matched-sample monopole measured within this paper (fP5_CW = 0.49719 on n = 812,793; already reported) as the default residual baseline everywhere in the main text when subtracting a monopole. Retain the propagation of the Paper IV uncertainty as a cross-check in an appendix.
- Where σpred is shown, show both variants (Paper-IV ΔfCW and P5-matched fP5_CW) or clearly relegate the Paper IV projection to an appendix. Ensure all main-text conclusions are derivable solely from quantities measured within this manuscript.

P5-E3 (Ambiguous formula notation; Sec. VIII A, p. 16)
Problem: “With 0 of 6, the one-sided 95% binomial upper bound on the true in-hole fraction is 1 − 0.051/6 = 39%,” where “0.051/6” as printed is ambiguous. The intended formula is 1 − 0.05^(1/6).
Required fix: Replace with the unambiguous expression 1 − 0.05^(1/6) ≈ 0.393, and cite a standard reference for Clopper–Pearson one-sided bounds.

P5-E4 (Naming consistency of classifier; Sec. IV A, title footnote and throughout)
Problem: The paper alternates between “V-Web” (velocity-shear) and “T-Web” (tidal-tensor) terminology, even while explicitly implementing Hahn 2007’s tidal-tensor method. Although you include a footnote, the dual use is a source of confusion to readers.
Required fix: Standardize nomenclature throughout the manuscript: either use “T-Web” consistently or retain “V-Web” only with an explicit parenthetical “(tidal-tensor T-Web of Hahn 2007)” at every first use in each major section. Adjust figure captions and table headings accordingly.

MAJOR

P5-M1 (Contingency tests need the underlying tables; Sec. VI A, p. 7; Sec. VI D, p. 12)
Problem: You report omnibus χ² tests (CW/CCW × class; χ² = 3.55, p = 0.31) and a class × program contingency (χ² = 4932, Cramér’s V = 0.078), but the paper does not provide the 4×2 or 4×2 cell counts in the text or a table. Reproducibility within the paper requires those tables.
Required fix: Add the 4×2 count tables for CW/CCW × environment class and environment class × program (bright/dark) in an appendix or the main text, sufficient for an independent recomputation of χ², p, and Cramér’s V.

P5-M2 (Main-text littered with filesystem paths; multiple pages)
Problem: Numerous lines like “pipelines/p5_desi_chirality/outputs/…” appear inline throughout results sections (e.g., Secs. IV A.4–5 pp. 4–5; VI A p. 7; VI C p. 9; VII p. 13; VIII A–F pp. 15–21; IX A–C pp. 21–25). While excellent for a lab notebook, this clutters the scientific narrative in a PRD article.
Required fix: Consolidate all path pointers into a single Reproducibility Appendix or data-availability section. Keep the main text focused on the analysis and results, with a single pointer to the appendix/Zenodo/DOI that contains the full provenance metadata.

P5-M3 (KDTree k-sufficiency vs exact recompute; Sec. VIII B, p. 17)
Problem: You acknowledge that up to 249 hole centers can lie within a max-radius neighborhood and that k = 20 is insufficient, then show that an exact recompute moves 100 objects (0.18%) into the void class. Yet the main table (Table VIII) retains the k = 20 values for continuity.
Required fix: Promote the exact (k-unbounded) membership results to the main text/table for the DESIVAST VoidFinder test (Table VIII) and move k = 20 to a robustness note or appendix. State explicitly that the headline DESIVAST result is computed with the exact membership.

P5-M4 (Details and implications of the randoms-weighted rebuild; Sec. IX A, p. 21–23)
Problem: The BGS-randoms-weighted low-z rebuild profoundly reshapes class fractions (e.g., void 17.6% → 0.75%) and reassigns only 26.6% of matched spirals to the same class, yet the text provides only qualitative reassurance. This result is methodologically important and could concern readers about the stability of the classifier under survey selection.
Required fix: Expand the description: explicitly give per-class fCW and σ for both unweighted and randoms-weighted runs side-by-side with uncertainties; clarify the precise redshift window; justify the interpretation as a stress test; and state clearly that your primary DESIVAST-based conclusion does not depend on T-Web class fractions. Consider moving full details to an appendix with a summary in the main text.

P5-M5 (Per-galaxy class assignment uncertainty; Sec. IV A.12, p. 5)
Problem: You NN-interpolate grid-cell labels to galaxies. No quantitative estimate is provided for the fraction of galaxies that lie within one cell of a class boundary, nor the sensitivity of class labels to moving a galaxy by ≤ 1 cell.
Required fix: Provide a simple boundary-proximity diagnostic (e.g., fraction of galaxies within one cell of a class boundary) and quantify the stability of per-galaxy class assignment to a ±1-cell perturbation. A brief table or figure in an appendix suffices.

P5-M6 (Regression model completeness; Sec. VI B, p. 8)
Problem: The logistic-regression analyses are summarized in prose with a few coefficients. Readers cannot reproduce or verify without fuller details.
Required fix: Add an appendix table listing model formulae, the full coefficient sets (β, SE, z, p) for both the environment-only and the covariate-extended models, including the program-controlled variant in Sec. VI D, along with the sample size used and pseudo-R².

P5-M7 (Nomenclature consistency for “sheet” vs “wall”; multiple pages)
Problem: The paper alternates between “wall” (your V-Web term) and “sheet” (as in T-Web). While the mapping is implicit, it should be explicit whenever you compare against external classifiers (e.g., Sec. IX C, p. 25).
Required fix: At each first occurrence in a section where both appear, add “(wall ≡ sheet)” and standardize panel labels and legends accordingly.

MINOR

P5-m1 (Abstract rounding consistency; Abstract p. 1 and Sec. VI E p. 12)
Problem: HEALPix look-elsewhere p-values in the abstract are given as 0.61/0.135/0.413, while Table VI shows 0.607/0.135/0.413. This is fine but please state that values are rounded to two decimals in the abstract.
Required fix: Add “(rounded)” or round to two decimals uniformly (0.61/0.14/0.41).

P5-m2 (Effect sizes; multiple places)
Problem: While you report Cramér’s V = 0.078 for the class × program contingency, effect sizes are not consistently presented for other omnibus tests (e.g., the main 4×2 χ²).
Required fix: Report Cramér’s V for the principal 4×2 CW/CCW × class test as well.

P5-m3 (Units confirmation; Sec. IV A.2, p. 4)
Problem: The text says “astropy returns χ in Mpc and we multiply by h explicitly to work in h−1 Mpc (sanity value: χ(z = 0.2) = 570.4 h−1 Mpc).” This is correct numerically but is a common point of confusion.
Required fix: Add a parenthetical clarification: “multiplying a value in Mpc by h yields a value expressed in h−1 Mpc.”

P5-m4 (Equation typography; Sec. V, p. 6 and Eq. (1))
Problem: σfrom half is used throughout; occasionally the denominator description (0.5/√N vs. exact √(p0(1 − p0))/…) appears in prose only.
Required fix: Include the exact standard-error form explicitly once, and keep the “not directly comparable across n” caveat visually proximate to any tables where σ are juxtaposed across rows (you already do this well; just ensure consistency in all tables/figures).

P5-m5 (Sky stratification proxy caveat; Sec. VIII E, p. 19)
Problem: The text clarifies that “0 maximal voids per pixel” is a proxy for being outside DESIVAST coverage. This is important and should be emphasized where the −4.75σ result is first mentioned.
Required fix: Add a short parenthetical “(proxy for outside DESIVAST footprint)” next to the “0 maximal voids per pixel” label in Table XI caption or the text introducing it.

P5-m6 (Appendix A phrasing)
Problem: The toy EFT operator is clearly labeled schematic, but it currently reads like a proposed Lagrangian term with potential gauge/rotation issues (which you acknowledge).
Required fix: Preface Appendix A with a sentence: “This section provides only an order-of-magnitude back-of-the-envelope mapping; it is not used anywhere in the main analysis or conclusions.”

NIT

P5-n1 (Typos/formatting)
- Sec. VII, p. 13: “near-unsmoothed” hyphenation ok; ensure consistent formatting of “Mpc/h” vs “h−1 Mpc”.
- Minor hyphen consistency (“monopole-subtracted,” “look-elsewhere”)—make consistent.

P5-n2 (Figure labels)
- Fig. 2 (p. 5): Ensure that the “cluster” slice’s 1.0% is legible at journal column width; if necessary, include values in legend.

Arithmetic and consistency audit (selected checks)

- Abstract numbers match body:
  - DR1 input rows 16.36M (Table I), matched galaxies 2.232M (Table I), chirality-relevant 791,635 (Table I).
  - Per-class fCW and σ values (Table III) match abstract; range 1.98 pp = 0.5034 − 0.4836.
  - 4×2 χ² = 3.55, p = 0.31 (Sec. VI A), unique-spiral χ² = 3.00, p = 0.39 (Sec. VI A).
  - Phase-2 sweep ranges 1.72–4.12 pp and label-shuffle pLEE 0.13–0.56 (Table VII). Under-resolved Rs = 10 caveat noted.
  - Redshift p = 0.372 (Sec. VI B).
  - Density quintiles: |σ|max = 3.94, σpred = 2.07, residual 1.87 < 3.09 (Fig. 5/Table IV).
  - HEALPix p-values 0.607/0.135/0.413 (Table VI).
  - DESIVAST VoidFinder: nvoid = 56,981, fvoid = 0.4964 vs fnon-void = 0.4971, Δ = +0.0007, z = 0.31, p = 0.76 (Table VIII).
  - Three-algorithm DESIVAST: |ΔfCW| ≤ 0.0019 (Table X).
  - V2-REVOLVER GALZONE: nvoid = 104,912, fvoid = 0.4992, σ = −0.52; two-sample z = −1.25 (Sec. VIII D).
  - Maximal-void sky stratification (Table XI) totals sum to nlz = 678,945; σ concentrated in “0 voids/pixel” bin.
  - Pearson r = +0.006 (p = 0.88) at NSIDE = 32 (Sec. VIII F); matches Fig. 8 and text.
  - Program split: bright fCW = 0.4970 (n = 775,760) vs dark 0.5051 (n = 14,782), Δ = 0.81 pp, z ≈ 1.95 (Table XV).

- Formula checks:
  - σfrom half = 2 (fCW − 0.5) √N used consistently.
  - Bonferroni thresholds computed correctly (e.g., K = 5 at α = 0.01 → |σ| ≈ 3.09).

- Units and dimensions:
  - χ(z = 0.2) ≈ 570 h−1 Mpc is numerically consistent with Planck 2018 cosmology and the stated Mpc→h−1 Mpc conversion by multiplying by h.
  - k-units and Poisson sign conventions consistent.

- Data-availability:
  - A DOI-minted archival snapshot is promised; ensure it is created at acceptance and cited in the final version.

Length and presentation

The manuscript is long (31 pages) for a focused negative result. While the breadth of robustness checks is commendable, much of the pipeline-path commentary and some cross-check detail could be moved to appendices/supplement to bring the main text to ~20–22 pages without loss of scientific content. Please restructure accordingly.

## Summary recommendation
MAJOR REVISIONS

The core statistical methodology is careful, and the main quantitative claims are internally consistent and appropriately caveated. However, the manuscript in its present form contains unacceptable internal version/review-log language, is not sufficiently self-contained with respect to its dependence on an unpublished companion (Paper IV), and mixes lab-notebook filesystem paths into the main narrative. Addressing the essential and major items above, and streamlining the presentation, will bring the paper to PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P5-E5 (Units/Dimensional consistency; Sec. IV A.2, p. 4; multiple occurrences)
Problem: The unit conversion statement is incorrect and the “sanity value” appears mislabeled.
- Text: “astropy returns χ in Mpc and we multiply by h explicitly to work in h−1 Mpc (sanity value: χ(z = 0.2) = 570.4 h−1 Mpc).”
- Issue: To convert Mpc → h−1 Mpc one must divide by h (or multiply by 1/h). Multiplying by h produces Mpc/h, not h−1 Mpc. Numerically, χ(z ≈ 0.2) ≈ 830–850 Mpc (Planck18), which is ≈ 830/0.6766 ≈ 1,200 h−1 Mpc, not 570 h−1 Mpc. The quoted 570 value is consistent with Mpc/h, not h−1 Mpc.
Required fix:
- Correct the conversion rule (“divide by h to obtain h−1 Mpc; multiply by h to obtain Mpc/h”).
- Relabel the “sanity value” as χ(z = 0.2) ≈ 570 Mpc/h, or provide the correct h−1 Mpc value (~1,200 h−1 Mpc).
- Audit the manuscript for consistent and correct use of Mpc/h vs h−1 Mpc, and explicitly state which convention the code uses for X/Y/Z and Rs.

MAJOR

P5-M8 (Global Mpc/h vs h−1 Mpc consistency; multiple sections/tables/figures)
Problem: The manuscript uses “Mpc/h” and “h−1 Mpc” interchangeably, and in places inconsistently (e.g., DESIVAST hole radii cited as “Mpc/h” while earlier text asserts “h−1 Mpc” coordinates). Given P5-E5, this risks reader confusion and undermines reproducibility (and raises concern about potential silent unit mismatches between catalogs and code).
Required fix:
- Standardize on one distance convention (recommend h−1 Mpc for positions and radii; h Mpc−1 for k). State it once early and adhere to it everywhere (text, figures, captions, tables).
- Where external catalogs have explicit units (DESIVAST, ASTRA), confirm and state exact unit conventions used in the joins/reprojections.
- Add a short unit-conversion footnote in Methods and in the Reproducibility Appendix confirming the code-level unit handling.

P5-M9 (Significance calibration for residual |σobs − σpred|; Sec. VII/Table VII and elsewhere residual comparisons)
Problem: The manuscript compares the residual statistic |σobs − σpred| directly to Bonferroni thresholds derived for |σ| (assumed standard normal). Because σpred is estimated (or projected from an external estimate) and not a fixed known parameter, the residual’s null distribution is not exactly N(0,1). This can misstate significance, especially where σpred uncertainty is non-negligible.
Required fix:
- Either (a) provide an empirical permutation-based null (conditional on total CW) for the residual statistic and report p-values (preferred), or (b) clearly move the Bonferroni comparison for residuals to an appendix as heuristic and rely on the reported permutation max-stat pLEE as the primary inferential statement in the main text.
- If retaining analytic comparisons, propagate the uncertainty on the monopole used to form σpred and reflect it in residual z-scores or uncertainty bands.

MINOR

P5-m7 (Bonferroni threshold two-sided clarity; Eq. (2), multiple uses)
Problem: Eq. (2) uses erfc−1 without explicitly restating that the family-wise control is two-sided on the max-|σ| statistic. In several places thresholds are quoted (e.g., K = 4 at α = 0.05 as |σ| ≈ 2.50) without stating two-sidedness; the exact two-sided value is ≈ 2.47.
Required fix:
- State explicitly that thresholds are two-sided max-|σ|. Consider using the z1−α/(2K) notation alongside Eq. (2), and standardize quoted numerical thresholds (e.g., 2.47 for K = 4, α = 0.05; 2.58 for K = 5, α = 0.05; 3.02 for K = 4, α = 0.01).

P5-m8 (Figure/pixelization clarity; Fig. 8 vs Sec. VIII E)
Problem: Fig. 8 uses NSIDE = 32, while Table XI and text analysis in Sec. VIII E primarily use NSIDE = 16. Although the text notes this, a reader may miss it when scanning figures.
Required fix:
- Add an explicit note in the Fig. 8 caption that the analysis table in Sec. VIII E uses NSIDE = 16 and that the figure uses NSIDE = 32 for visualization, to avoid perceived inconsistencies.

P5-m9 (σvs-monopole table rounding consistency; Table XII)
Problem: Recomputing the filament row σvs-monopole using fP5_CW = 0.49719 and N = 408,187 yields ≈ +1.02 (not +0.99). The difference is within rounding but appears to mix fP5 rounding across rows.
Required fix:
- State fP5_CW with the precision actually used in the calculation (e.g., 0.49719) and ensure consistent rounding across all rows, or add a note that small row-to-row discrepancies reflect rounding in fP5_CW and N.

P5-m10 (Randoms-weighted rebuild presentation; Sec. IX A)
Problem: While you do provide an illustrative void-bin uncertainty and a qualitative summary, the side-by-side numbers for all classes are only partially given.
Required fix:
- In addition to the expanded Appendix requested in P5-M4 (first review), add a compact table in the Appendix giving n, fCW, and σ (with Jeffreys 95% CI) for each class in unweighted vs weighted runs (and the precise redshift window), so the “substantially reshapes class fractions yet leaves fCW per class within uncertainty” claim is numerically transparent.

JUSTIFICATION OF SCOPE

These are new items not covered in my initial review. The most consequential is the unit-conversion error and global Mpc/h vs h−1 Mpc consistency (P5-E5, P5-M8), which directly affect dimensional correctness and, potentially, code–catalog interoperability. The residual-significance calibration (P5-M9) strengthens the inferential rigor where a heuristic z-threshold was previously used. The remaining minors improve clarity and numerical consistency.