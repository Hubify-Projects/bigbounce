# P5 RA-INT — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` md5=eab9162e pages=34
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5077 chars)
**Wall time**: 368.9s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample”

Scope of review
I read the full manuscript, all figures, tables, equations, footnotes, and appendices. Below I audit (i) statistical methodology and multiplicity control, (ii) dimensional consistency, (iii) internal arithmetic and cross-table consistency of all load‑bearing numbers in the abstract and conclusions, (iv) clarity about which statistics are comparable, and (v) reproducibility claims. Findings are classified as ESSENTIAL, MAJOR, MINOR, or NIT and referenced by section and page numbers as they appear in the provided PDF.

Overall assessment
The central quantitative claim (no detectable environment dependence of spiral chirality at DESI DR1 sensitivity) is well supported by the DESIVAST-anchored primary analysis and by multiple, appropriately caveated cross‑checks. Many arithmetic spot‑checks are correct at the quoted precision; where I recomputed σ, χ² and p-values from the tabulated counts, I reproduced the numbers within rounding. The paper is, however, exceptionally long and interleaves an unusual amount of repository bookkeeping (artifact IDs, file paths, seeds, driver names) in the main narrative. There are also two methodological/provenance issues that, in my view, must be addressed for PRD standards: (1) reliance on an “in preparation” Paper IV for a load‑bearing catalog‑monopole reference that is used repeatedly for σpred lines; and (2) repeated use of a row‑level parent with duplicated TARGETIDs for formal tests without systematically demonstrating that duplicates do not bias every tested statistic (the authors do provide some checks, but not for all load‑bearing tests). I list concrete required fixes below.

Findings

ESSENTIAL

P5-E1. Dependence on unpublished Paper IV for load‑bearing calibration (Section II, pp. 3–4; used throughout)
Problem: The manuscript repeatedly uses the Paper IV catalog monopole ∆fP4_CW = −0.0026 (and its “≈9σ” significance) as a reference to interpret class‑level σ and to generate σpred lines (Eq. 1). Paper IV is “in preparation” and not citable at PRD acceptance; the present paper must stand alone. Although you do compute an internal matched‑sample monopole fP5_CW = 0.49719 (Table XIII; §VIII F) and note that the headline ∆fCW contrasts are invariant to any global monopole shift, you nevertheless base several formal residual analyses (e.g., Table V, multiple σpred overlays in the density/quintile sections, Phase‑2 max‑|σobs−σpred| column in Table VIII) on the unpublished ∆fP4_CW.
Required fix: Replace every use of ∆fP4_CW (−0.0026) in σpred and residual calculations with the internally measured matched‑sample monopole fP5_CW = 0.49719 (equivalently ∆fP5_CW ≈ −0.00281) and propagate its counting uncertainty as you already do in §V. If you wish to retain the Paper IV value, it must at minimum be an arXiv‑posted preprint at submission, and any σpred tables must present both references (P5 internal and P4 external) side by side, emphasizing that all load‑bearing inferences are identical under either. Abstract language that treats the Paper IV monopole as an adopted “known reference” should be softened to “independently corroborated” and made conditional on the internal value.

P5-E2. Duplicated TARGETIDs in hypothesis tests (Sections VI A–E, VII; multiple tables; pp. 8–16)
Problem: Many formal tests (e.g., the headline T‑Web 4×2 χ² on p. 8 was checked on unique TARGETIDs, which is good; but the Phase‑2 cellwise permutation pLEE in Table VIII; the HEALPix max‑|σ| LEE tests in Table VII; density‑quintile residuals in Table V; several logistic regressions; and parts of the program splits) are computed on the 812,793 “env‑labeled parent” with 3.56% duplicated TARGETIDs (28,973 repeated survey–program coadds). You do show that the 4×2 homogeneity χ² and a few other quantities are insensitive to deduplication. However, you do not provide a systematic demonstration that the duplicates cannot bias every hypothesis test that assumes i.i.d. draws (especially the permutation‑based p-values and the Phase‑2 max‑residual statistics).
Required fix: For every load‑bearing formal test reported on the row‑level parent (Tables V, VII, VIII; the density-, redshift-, and HEALPix LEE tests; and the filament/cluster within‑class decompositions), recompute on the 783,820 unique‑TARGETID parent and add a side‑by‑side comparison (values and conclusions). For permutation tests, show that the deduplicated pLEE agrees with the row‑level pLEE within Monte‑Carlo uncertainty. State explicitly in the methods which parent (row‑level vs unique) is used for each test, and ensure no i.i.d. assumption is violated by duplicates. If a test must remain on the row‑level table (e.g., because of how the environment table is constructed), justify why duplicates cannot bias its null distribution (or switch to a resampling scheme that collapses duplicates within permutations).

MAJOR

P5-M1. Overuse of internal “artifact” identifiers and repository paths in the main text (multiple places across pp. 5–33)
Problem: The narrative is littered with references like “[A10]”, “env_finder/01_compute_vweb.py”, “outputs/27_ext1_logistic_program_control.json”, etc., including version tags and internal driver notes. While reproducibility is commendable, PRD expects a clean scientific narrative, with detailed code/data pointers moved to Supplemental Material or a Data Availability appendix.
Required fix: Move all “artifact [A#]” callouts and repository paths to (i) a compact Data & Code Availability section or (ii) Supplemental Material with a DOI. In the main text, replace them with short, human‑readable citations (e.g., “see SM Sec. S3, Table S2”). Keep only truly load‑bearing reproducibility anchors in the main text (e.g., the GitHub repo DOI and tag).

P5-M2. Primary/secondary analysis declaration is post‑hoc; pre‑specification and multiplicity bookkeeping need to be tightened (Section V.B, pp. 7–8; Abstract)
Problem: You state the DESIVAST analysis is designated “primary” post‑hoc. While you address multiplicity within the DESIVAST family (Bonferroni‑5) and across the Phase‑2 T‑Web sweep (Bonferroni‑9), you also report numerous secondary decompositions and scans. The manuscript is careful overall, but the Abstract and Conclusions present many numbers without always marking them as “secondary diagnostics, not load‑bearing” at first mention.
Required fix: In the Abstract and end‑Conclusions, explicitly mark which result is the sole primary estimand (the DESIVAST ∆fCW null and bounds) and which are secondary diagnostics. Add one sentence in the Abstract that the T‑Web path is “diagnostic only; see body for selection‑function caveats.” Ensure every secondary test that reports |σ| also states its familywise threshold (or the LEE p), right next to the number, to avoid casual readers over‑interpreting a 2–3σ single‑bin fluctuation.

P5-M3. T‑Web selection‑function caveat should be promoted earlier (Sections IV, VI A, IX A; Abstract wording)
Problem: You later show convincingly that the global‑mean δ induces strong radial selection leakage and that a shell‑corrected rebuild tightens the null. However, you present headline T‑Web class fractions and σ in §VI A before the selection caveat is surfaced. The Abstract mentions the shell systematic only deep in the robustness paragraph.
Required fix: Up‑front in §IV (or a short caveat paragraph at the end of §IV A), state clearly that the canonical T‑Web run uses a global mean and inherits a radial selection bias that is later stress‑tested and found not to affect the chirality conclusions. In the Abstract, add “the canonical T‑Web labels inherit selection‑function systematics (addressed by a z‑shell‑corrected rebuild that also returns a null).” This will prevent misinterpretation of the small T‑Web void sample (n=428) as a physics feature.

P5-M4. Results rely on a concurrently “in submission” external DR1 T‑Web paper [11] and an EDR ASTRA catalog [12] for context; ensure the present claims are independent (Section IX.C–X)
Problem: Several contextual statements compare your volume fractions to [11] and use ASTRA EDR [12] as a per‑object cross‑check. This is fine as context, but the present claims must remain independent. At times the language could be read as leaning on [11] for validation despite the lack of a per‑object cross‑match.
Required fix: Rephrase to make it unmistakable that (i) the DESIVAST analysis alone anchors the headline; (ii) the T‑Web and ASTRA overlap tests are internal, diagnostic, and do not import external validation. Where you quote fractions from [11], mark them plainly as “context only; methods differ.”

P5-M5. Length and focus (entire manuscript)
Problem: At 34 pages for a single null test (albeit with many diagnostics), the paper significantly exceeds what is needed to establish the primary DESIVAST null plus a concise set of cross‑checks.
Required fix: Please reduce to ≤24 pages (PRD two‑column equivalent), by moving much of Sections VI.D, VII (details beyond the core grid‑resolved results), IX–XI peripheral stratifications, and Appendix D artifact tables to Supplemental Material.

MINOR

P5-m1. Small σ discrepancies (Section VI A, Table IV, p. 9)
Problem: I recompute σfrom half for the filament class (n=408,187, f=0.4980) as −2.56 using your definition; you quote −2.61. The difference is inconsequential but appears to stem from rounding in f reported to 4 d.p.
Required fix: Note in a footnote or table caption that σ values are computed from exact counts (not rounded f), which explains small apparent mismatches when recomputed from the rounded display values.

P5-m2. Clarify “pp” (percentage points) once early (Abstract and first usage)
Problem: You use “pp” correctly but without an initial definition.
Required fix: Define “pp = percentage points” at first mention in the Abstract or §V.

P5-m3. Provide the explicit count underlying “≈0.1% of in‑footprint grid cells fall inside a DESIVAST VoidFinder sphere” (Section VI A, p. 9)
Problem: This quantitative statement is useful; add the absolute number of cells and the denominator for the stated grid.
Required fix: Add the numerator/denominator to the sentence or a footnote.

P5-m4. Move the multiply‑by‑h convention footnote into Methods and ensure consistency (Section IV.A step 2, footnote 1, p. 5)
Problem: The “multiply‑by‑h” explanation is correct but unusual and easy to miss in a footnote.
Required fix: State the unit convention once in §III.B or §IV.A (“Distances are expressed in h−1 Mpc by multiplying astropy’s Mpc value by h = 0.6766”) and ensure all later uses are consistent.

P5-m5. Clarify mask dilation choice (Section IV.A step 5, p. 6; §VII)
Problem: The dilation rule “⌈Rs/cell⌉+1 iterations” is reasonable and a sensitivity check is given, but the motivation is not stated.
Required fix: Add one sentence justifying this heuristic (e.g., to ensure the smoothed kernel never samples outside the footprint), and keep the mask‑sensitivity numbers (now in [A13]) either in the main text or SM.

NIT

P5-n1. Stylistic “committed artifact,” “driver,” “re‑draw” language (multiple pages)
Fix: Replace with neutral scientific prose in the main text; keep such details for SM.

P5-n2. A few duplicated or awkward phrases (e.g., “catalog‑wide‑monopole‑projected,” “headline cosmic‑web result”)
Fix: Edit for concision.

Arithmetic and consistency audit (selected load‑bearing items)

- Abstract • nDR1 input: 16,361,731 post‑cut rows — matches §III.B and Table II.
- Abstract • Matched unique: 2,232,212 — matches Table II; chirality‑relevant 791,635 and CW/CCW split 393,592/398,043 sum to 791,635.
- Abstract • T‑Web parent: 14,622,283 GALAXY rows for classification — matches §IV.A.
- Abstract • T‑Web void bin n=428; binomial half‑width 0.5/√428 = 2.416 pp (1σ) and 4.83 pp (2σ) — matches text.
- Table IV • Void 207/428 ⇒ f=0.4836; σfrom half = −(7)/(0.5√428) = −0.676 — matches −0.68.
- Table IV • Wall 3,359/6,673 ⇒ f=0.5034; σ≈ +0.556 — matches +0.55.
- Table IV • Cluster 197,284/397,505 ⇒ f=0.4963; σ≈ −4.67 — matches −4.66.
- Omnibus χ² (Appendix B, Table XVII): recomputed 3.46–3.55 (3 d.o.f.) — p≈0.31, consistent with reported.
- Density quintiles (Table V): at N≈158,327, σpred = 2|−0.0026|√N = 2.07; maximum residual |σobs−σpred| = 1.87 — below Bonferroni‑5 threshold 3.09 — consistent.
- Phase‑2 sweep (Table VIII): resolved cells have max |σobs−σpred| ≤ 1.64; pLEE per cell 0.13–0.48 — consistent with reported.
- DESIVAST void vs non‑void (Table IX): 28,286/56,981 ⇒ 0.4964; 309,173/621,964 ⇒ ≈0.4971; ∆= +0.0007; SE(∆)≈ 0.00219; z=0.31; p=0.76; 95% CI [−0.0036, +0.0050] — all consistent.
- Three‑algorithm DESIVAST (Table XI): V2‑REVOLVER ∆= −0.0019; SE≈0.0017; z≈ −1.12; p≈0.26 — consistent; V2‑VIDE ∆≈ −0.0001; SE≈0.0019; z≈ −0.05; p≈0.96 — consistent.
- Catalog‑native GALZONE (Section VIII.D): V2‑REVOLVER ∆= −0.0037; SE≈0.0029; z= −1.25; p=0.21; V2‑VIDE ∆= +0.0019; SE≈0.0026; z= +0.72; p=0.47 — consistent.
- Maximal‑void sky stratification (Table XII): counts sum to 678,945; σ values recompute to −4.75 (0 voids), −0.43 (1–2), −0.09 (3–5), −2.04 (6+) within rounding — consistent.
- Cramér’s V (Appendix B, Table XVIII): V = √(χ²/n) = √(4933/811,609) = 0.078 — matches.
- σvs monopole (Table XIII): using fP5_CW = 0.49719, void row gives (0.4836−0.49719)/(0.5/√428)= −0.56 — matches.

Dimensional checks
- Eq. (1) σpred = 2∆fCW√N is dimensionless and consistent with the adopted Bernoulli variance convention; correctly warns about using 0.5/√N denominator for cross‑table comparability.
- Fourier‑space definitions and units (k in h Mpc−1, χ in h−1 Mpc) are self‑consistent. The “multiply‑by‑h” footnote is correct.

Effect sizes and multiple comparisons
- Where χ² tests are used, you provide effect sizes (Cramér’s V = 0.078) — good.
- For multi‑bin scans, you quote both parametric Bonferroni thresholds and empirical max‑stat pLEE; NMC=1000 implies ~0.01–0.015 resolution, which you acknowledge — good. Please keep these reminders at every pLEE appearance (see P5‑M2).

Standalone‑reader test
- The analysis treats the per‑galaxy labels as a given input. This is acceptable provided the catalog is publicly available upon publication and all inferences that require a monopole reference are expressed using the internal matched‑sample monopole (see P5‑E1). Otherwise, too much rides on an unpublished Paper IV.

Abstract‑last drift sweep
I re‑read the Abstract after the full text. Most abstracted numbers (Ns, σs, p-values, ranges, LEE p’s) trace to tables/sections. Please incorporate P5‑M2 clarifications (primary vs secondary) and P5‑E1 corrections (internal vs Paper‑IV monopole) to prevent over‑statement.

Bibliography
Dates, journals, and arXiv IDs appear consistent for [1]–[14]. Two 2026 preprints [11], [12] are “in submission” or “arXiv”; this is fine for context, but make sure the present claims do not depend on them.

## Summary recommendation
MAJOR REVISIONS

The DESIVAST‑anchored primary analysis and its statistical framing are largely sound and the internal arithmetic checks out. However, to meet PRD standards the paper must (1) remove dependence on an unpublished Paper IV monopole by basing all σpred/residual overlays on the internally measured matched‑sample monopole (or ensure Paper IV is publicly posted and clearly non‑load‑bearing), and (2) systematically demonstrate that the use of a row‑level parent with duplicated TARGETIDs does not bias any formal hypothesis test (or recompute all such tests on the unique‑TARGETID parent). In addition, the manuscript should be shortened and the heavy repository bookkeeping moved to Supplemental Material, and selection‑function caveats should be surfaced earlier. With these revisions, the paper would present a clear, rigorous null result suitable for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh‑eyes audit)

New issues only; numbering continues your prior scheme. Page/section refs follow the provided PDF pagination.

ESSENTIAL
None beyond those already listed.

MAJOR

P5-M6. Catalog-native GALZONE “non-void” complement is underspecified and potentially non-comparable (Section VIII.D, pp. 19–20)
- Issue: For the V2-REVOLVER/VIDE catalog-native tests you define void membership as OUT=0 ∧ ZONE≥0 ∧ VOID0≥0, but the “non-void complement” is described only as “rows that fail the catalog-native void cut.” This appears to include rows with OUT=1 and/or ZONE<0 (and possibly EDGE/DEPTH-flagged entries), yielding nnon-void far smaller than nvoid (e.g., 40,877 vs 104,912 for V2-REVOLVER). That asymmetry suggests the complement is a restricted subset of the GALZONE join, not a true in-footprint non-void control comparable to the void subset.
- Why it matters: The two-sample ∆fCW contrast can be biased if the “non-void” control is a mixture of edge/out-of-zone entries or a small, footprint-mismatched subset. Because you present these catalog-native results as part of the primary DESIVAST family, the construction of the control set must be unambiguous and comparable.
- Required fix: Explicitly define the non-void complement for the catalog-native tests (e.g., OUT=0 ∧ ZONE≥0 ∧ VOID0<0) and report the fraction of the matched-spiral sample covered by the GALZONE join under that cut. Add a like-for-like footprint restriction (as you did in Table IX’s “footprint-restricted” control) and show that the ∆fCW result is stable. If you intend the complement to include OUT=1/EDGE rows, justify why that is appropriate and quantify the impact by re-running with EDGE=0 and DEPTH≥1 (≥2) on both void and non-void sides.

MINOR

P5-m6. Incorrect “alternative convention” for h-units (Section IV.A, footnote 1, p. 5)
- Issue: The footnote presents χ[h−1 Mpc] = χ[Mpc]/h as an “alternative convention.” That is not an alternative; it is incorrect for converting a numerical value in Mpc to a numerical value in h−1 Mpc. The correct conversion is χ[h−1 Mpc] = h × χ[Mpc].
- Fix: Remove the divide-by-h “alternative” and state the correct conversion unambiguously. If you wish, note that some codebases output comoving coordinates already in Mpc/h; that is a different situation than unit conversion.

P5-m7. Stale count for interior-buffer excision (Section IX.A, “z-shell selection-corrected classifier,” p. 24)
- Issue: You state the interior-buffer variant “retains 782,015 of the 783,820 unique env-matched spirals” (implying 1,805 removed) and then: “(1,862 spirals removed).” These two numbers disagree by 57.
- Fix: Recompute and reconcile the removal count; correct both the text and any downstream percentages if needed.

P5-m8. RSD Monte Carlo membership flips vs net void-count change (Section VIII, RSD paragraph, p. 17)
- Issue: You report “reassigns ∼4.4×10^4 hole-union memberships per realization,” while the net void count rises by ≈19,409 (57,081 → 76,490). This is plausibly “both-direction flips” vs “net increase,” but it is ambiguous as written.
- Fix: Clarify explicitly that ≈44k is the total number of in↔out flips (sum of both directions), while the net in–out balance increases the void tally by ≈19.4k. If available, quote the mean numbers of out→in and in→out flips separately.

P5-m9. Typesetting of the Clopper–Pearson bound (Section VIII.A, p. 18)
- Issue: The 0-successes upper bound is written as “1 − 0.051/6 = 39%,” which reads like 0.05×(1/6). From context you clearly intend 1 − 0.05^(1/6).
- Fix: Typeset the exponent explicitly (1 − 0.05^{1/6}) to avoid misinterpretation.

P5-m10. Minor σ rounding note (multiple tables)
- Issue: A few σfrom half values will not reproduce exactly from the rounded f in the same row (e.g., Table IV filament).
- Fix: Add a uniform note (once) that σ values are computed from exact integer counts, not the rounded f displayed.

NIT

P5-n3. “18.8% of the cube” denominator not shown alongside the counts (Section IV.A step 5, p. 6)
- You give the in-mask and total-cell counts elsewhere, but consider adding “3,150,086 / 16,777,216 = 18.8%” inline for self-containment.

P5-n4. Bonferroni threshold formula reminder (Section V.A, Eq. 2)
- As a reader convenience, add “two-sided” next to the threshold values when first quoted for K=5 and K=9, even though you explain it just above Eq. (2).

Why these are new
- These items were not covered in the original review. In particular, the GALZONE complement definition (P5-M6) affects a primary-family robustness line; the h-units “alternative” is a factual error (albeit not load-bearing); the interior-buffer count mismatch (P5-m7) and the RSD flip/net-change clarification (P5-m8) are arithmetic/clarity issues that can be corrected quickly but should not persist into a final version.

I rechecked remaining tables/figures/equations for the A–J audit classes; beyond the points above, displayed σ, χ², p-values, counts, and figure-caption/body claims were consistent at the quoted precision, and equation dimensions are sound.