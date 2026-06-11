# P5 R29 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.61.pdf` md5=5eb81cd5 pages=30
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7064 chars)
**Wall time**: 271.3s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T‑Web (Hahn 2007) Tidal‑Tensor Cross‑Check Across 791,635 DR1 Matched Spirals” (30 pp)

Scope of review
I audited the full manuscript for statistical/methodological rigor, internal arithmetic consistency, dimensional correctness, and claims vs. evidence. I recomputed all readily checkable σ, p, and range figures from the tabulated n and f values, and I checked that abstract and conclusions scalars are traceable to the body.

Overall assessment
The core methodology (binomial framing; clear separation of “σ from half” vs. monopole-referenced residuals; permutation-based look‑elsewhere control; multiple cross-checks including a three‑algorithm DESIVAST re‑projection) is, in principle, capable of supporting a null finding of environment dependence at the reported sensitivity. Many of the headline numbers in the abstract are numerically consistent with the body.

However, as submitted, the manuscript contains multiple issues that fail PRD standards for presentation and reproducibility. The paper is saturated with process/audit trail commentary (“earlier draft,” “withdrawn,” file paths, config names) that must be excised or moved to a proper data appendix/Supplement. There is at least one notation error that turns a correct binomial bound into an ambiguous expression. The paper repeatedly leans on an unpublished “Paper IV” for a load‑bearing catalog monopole, and the Data/Code availability section promises a DOI but does not provide one.

Below I itemize findings with required fixes and severity.

Findings

ESSENTIAL

P5-E1 (Sec. VIII A, p. 16): Incorrect/ambiguous formula for the 0-of-6 binomial upper bound
- Offending text: “With 0 of 6, the one-sided 95% binomial upper bound on the true in-hole fraction is 1 − 0.051/6 = 39%”
- Problem: As typeset, “0.051/6” is ambiguous/incorrect. The intended Clopper–Pearson bound is 1 − (0.05)^(1/6) ≈ 0.387. The current rendering could be read as 0.05 × (1/6).
- Required fix: Correct to 1 − 0.05^(1/6) and provide the numerical value 0.387 (38.7%) explicitly. If using Clopper–Pearson, state that by name.

P5-E2 (Multiple sections, pp. 7, 13, 17, 24, 27, 29): Process/audit-trail language and “earlier draft… withdrawn”
- Offending examples:
  - p. 7: “An earlier draft quoted filament bright/dark n … are withdrawn in favor of the declared-parent recompute…”
  - p. 13: “An earlier draft of this table reported per-cell ranges … those values are withdrawn…”
  - p. 17: “An earlier draft reported nvoid = 86,276 / 64,514 … reproduce exactly only under a zone-indexing defect…”
  - p. 24: “An earlier draft compared … is withdrawn.”
  - p. 27: “an earlier harmonic-space … statistic was withdrawn in Paper IV v1.0.166…”
  - Throughout: hard-coded file paths, JSON filenames, config tags (“pipelines/p5_desi_chirality/…”, “v0.1.61-2026-06-10”).
- Problem: PRD papers must present the final analysis, not a change log. Process commentary and internal artifact pointers belong in a Supplement/Data Appendix with stable DOIs, not in the main body.
- Required fix: Remove all “earlier draft/withdrawn” and internal pipeline-path prose from the main text. Summarize finalized methods and results cleanly. Move necessary reproducibility details (including file paths) to a Supplement with a versioned, DOI‑backed archive.

P5-E3 (Appendix B, p. 29): Missing DOI and frozen release for code/data
- Offending text: “A DOI-minted archival snapshot of this directory accompanies journal submission.”
- Problem: No DOI or archive link is actually provided. PRD reproducibility requires an accessible, immutable deposit (e.g., Zenodo/OSF) with a version tag matching the paper.
- Required fix: Provide the actual DOI(s) for (i) the analysis code snapshot, (ii) the derived analysis products needed to reproduce the tables/figures (parquets/CSVs), with file manifests and checksums. State the exact tag/commit used.

P5-E4 (Multiple sections and Abstract): Dependence on an unpublished “Paper IV” for a load‑bearing monopole offset
- Offending text: e.g., Abstract: “beyond the known Paper IV catalog-monopole offset of ≈0.26 pp…”; Sec. V uses ΔfCW = −0.0026 from Paper IV to compute σpred; Sec. XII compares to Shamir 2022 in terms of Paper IV dipole bound.
- Problem: The manuscript must be self‑contained for its primary claims. While you do compute a matched-sample monopole (fP5CW = 0.4972 on 812,793 rows), many explanations are framed as if ΔfCW = −0.0026 were an external “known systematic.” Since Paper IV is not peer‑reviewed and the value is not derived here, basing significance narratives on it is not acceptable.
- Required fix: Recast all significance and interpretation statements in terms of statistics measured within this manuscript (prefer the matched-sample monopole and permutation tests that condition on the observed total CW count). Where you overlay a Paper IV value, explicitly label it as external and non‑load‑bearing. In the abstract and conclusions, remove language implying reliance on Paper IV for the main inference.

P5-E5 (Equation formatting; Sec. V, p. 6): Ambiguous Eq. (1) typesetting
- Offending text: “σpred = ∆fCW 0.5/√N = 2 · ∆fCW · √N”
- Problem: The intended fraction “∆fCW / (0.5/√N)” is missing the division slash or parentheses, making the left-hand equality look dimensionally wrong.
- Required fix: Typeset as σpred = (∆fCW)/(0.5/√N) = 2∆fCW√N.

MAJOR

P5-M1 (Terminology; Sec. IV A, title footnote, pp. 4–6): “V‑Web” label used for T‑Web throughout
- Problem: You use “V‑Web” to refer to a Tidal‑tensor (Hahn 2007) classifier rather than the velocity‑shear “V‑Web.” Although footnoted, this is likely to confuse readers and Google/ADS searches.
- Required fix: Standardize terminology: use “T‑Web (Hahn 2007 tidal‑tensor)” consistently in the main text and figures, reserving “V‑Web” only when velocity‑shear methods are meant. Alternatively, carry a persistent, prominent disclaimer in the title/abstract and first mention.

P5-M2 (Length and focus): The manuscript is overlong for the narrow contribution
- Problem: 30 pages with extensive process commentary and repeated restatements of nulls is more than needed to communicate the methodology and result.
- Required fix: Trim to ≤18 pages for the main text by moving process logs, alternative joins, and extended audit-trail details to a Supplement. Keep in main text: data, core method, core null results (with counts), key robustness (Phase‑2 sweep, DESIVAST re‑projection), and concise systematics.

P5-M3 (Contingency test details; Sec. VI D, pp. 11–12): Missing cross-tab counts
- Problem: You quote the χ² = 4932, p ≪ 10−300, Cramér’s V = 0.078 for V‑Web class × target‑program, but you do not provide the underlying 4×2 table counts in the paper (only in artifacts).
- Required fix: Include the 4×2 counts (bright/dark per V‑Web class) in a table in the paper or Supplement, so readers can replicate χ², p, and V.

P5-M4 (Selection‑corrected rebuild; Sec. IX A, pp. 21–22): Provide explicit per-class counts/fractions
- Problem: You state that the cross‑class fCW range collapses to 0.05 pp and quote class fCW’s, but you do not tabulate the corresponding n, nCW per class for the selection‑corrected labels.
- Required fix: Add a table with the per-class n and nCW (and fCW with Jeffreys CI) for the selection‑corrected build (and, if retained, the randoms‑weighted variant). This is a core robustness result.

P5-M5 (RNG seeding; Sec. V A, Sec. VI E, pp. 6, 12): Shared RNG streams across families
- Problem: You note “the same config-level seed initializes each scan family’s generator,” which can induce cross‑family dependence of max‑stat p’s. While you mention distinct‑stream re‑draws in one place, this is not systematic.
- Required fix: Ensure independent RNG streams for each family of permutation tests in the main analysis, and state this explicitly. If shared‑seed runs are kept, clearly segregate them as cross‑checks.

P5-M6 (Minor math check; Sec. VI A, p. 7): Predicted σ for filament/cluster
- Observation: Using σpred = 2∆f√N with ∆f = −0.0026 yields σpred ≈ −3.32 (filament) and −3.27 (cluster) vs observed −2.61 and −4.66. You correctly frame these as monopole‑driven deviations; however, present also the matched‑sample monopole prediction (∆f ≈ −0.0028) alongside, to avoid implying dependence on Paper IV.
- Required fix: Add the matched‑sample σpred values to the discussion.

MINOR

P5-m1 (Abstract consistency; pp. 1–2): Precision of HEALPix p-values
- Observation: Abstract reports p = 0.61/0.135/0.413; Table VI shows 0.607/0.135/0.413. This is acceptable rounding, but note MC p’s are ±0.01–0.015.
- Suggested fix: Add “±0.01 MC error” qualifier in the abstract or say “≈0.61” to avoid overprecision.

P5-m2 (Eq. 2, p. 6): Clarify two‑sided Bonferroni mapping
- Problem: The derivation uses erfc−1(α/K). To prevent confusion about two‑sided vs. one‑sided, note explicitly that erfc(Z/√2) = α/K is the two‑sided mapping, and give an example computation (e.g., K = 5 → Z ≈ 3.09).
- Fix: Short explanatory sentence after Eq. (2).

P5-m3 (Units and symbols; Sec. IV A step 2, p. 4): h conventions
- Observation: You mix “Mpc/h,” “h−1 Mpc,” and “h Mpc−1.” While physically consistent, some instances have spacing/encoding issues.
- Fix: Uniformize units formatting throughout.

P5-m4 (Figure clarity): Provide axes labels/units explicitly where implied
- Observation: Figs. 4–6 axes are interpretable but not fully labeled with units (e.g., redshift is dimensionless, density quintiles are rank bins).
- Fix: Add explicit axis labels “redshift z (dimensionless),” “density quintile (rank),” etc., for stand-alone clarity.

P5-m5 (CIC window deconvolution; Sec. IV A step 9, p. 5): Impact statement
- Suggestion: Briefly comment on how not deconvolving the CIC window could bias eigenvalue magnitudes and why only ordering matters for the classifier.

P5-m6 (ASTRA overlap; Sec. X, pp. 25–26): Explicit class‑wise counts for V‑Web on overlap
- Observation: You list V‑Web overlap counts in prose. For completeness, mirror the ASTRA table with a row listing n per V‑Web class in the overlap.

NIT

P5-n1 (Typos/formatting): Several minor typographic glitches
- Examples: “σfrom half” sometimes missing hyphen, superscripts spacing (“h −1 Mpc”), duplicated spaces, inconsistent use of “pp” vs “percentage points.”
- Fix: Copyedit.

P5-n2 (Claims of novelty; Sec. VIII B, p. 17): “to our knowledge, the largest…”
- Suggestion: Rephrase to “a large” or add a citation justifying “largest”; otherwise remove “to our knowledge.”

P5-n3 (Appendix A scope): The toy EFT mapping is clearly labeled as heuristic
- Suggestion: Move to Supplement or trim; keep caveats prominent to avoid implying a derived constraint.

Audit of abstract and conclusions vs body (Pattern‑045)
- All load‑bearing numerics in the abstract (matched/mapped N’s, class fractions, σ’s, χ² and p’s, Phase‑2 ranges and p’s, DESIVAST ∆f = +0.0007, Tempel 0.29 pp, bright/dark differences, Cramér’s V) are traceable in the body and numerically consistent within rounding and MC resolution.
- One phrasing to adjust per P5‑E4: remove framing that treats the Paper IV monopole as “known” and instead emphasize the matched‑sample monopole conditioning and the permutation‑based nulls used here.

Internal arithmetic spot checks
- σfrom half values in Table III recompute from n and f (void −0.68, wall +0.55, filament −2.61, cluster −4.66).
- Density quintiles (Table IV): σpred = 2∆f√N ≈ −2.07 at N = 158,327; observed largest residual |σobs − σpred| = 1.87 — matches.
- DESIVAST VoidFinder (Table VIII): nvoid = 56,981, fvoid = 0.4964 → σ ≈ −1.71; non‑void f = 0.4971 → σ ≈ −4.59 — matches.
- Three‑algorithm DESIVAST (Table X): |∆fCW| ≤ 0.0019; the claimed 1.2σ for REVOLVER vs 1/(2√n) ≈ 0.00156 is consistent.
- HEALPix scan p’s (Table VI) match abstract and text.

Stand‑alone reader test (Pattern‑046/047)
- The analysis can be followed without opening Paper IV, but several discussions assume Paper IV’s monopole as “known.” With P5‑E4 addressed (reframing around the matched‑sample monopole and permutation nulls), the paper will be stand‑alone. Ensure that all external catalog descriptions necessary to reproduce the joins (columns used, filters) are specified here (most are, good).

Uncomputed/qualitative claims (Pattern‑048)
- Most “dominates,” “consistent with,” “robust to” statements are quantified with numbers and/or artifact pointers. Where you assert ratios like “within 1.01× the void‑bin 2σ floor,” you do give the worst‑case ratio (good). Keep/expand this practice in the trimmed version.

Effect sizes (Pattern‑019)
- For the V‑Web class × program contingency, you provide Cramér’s V = 0.078 (good). For χ² omnibus tests, retaining a brief effect‑size framing is helpful (you generally do this).

## Summary recommendation
MAJOR REVISIONS

The core statistical methodology and most numerical claims check out, and the main null result seems supported by multiple, consistent analyses. However, the manuscript requires substantial editorial and reproducibility revisions to meet PRD standards: remove process/“earlier draft” commentary from the main text, correct the binomial‑bound notation error, decouple load‑bearing inferences from an unpublished companion’s monopole, and provide an actual DOI‑backed archival snapshot. Trim the paper to a more focused length and add a few missing tables for key cross‑tabs and the selection‑corrected rebuild. With these fixes, the paper could be re‑evaluated.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS AFTER SECOND-PASS AUDIT

ESSENTIAL

P5-E6 (Sec. VI A and Fig. 3 caption): Inconsistent duplicate-row fraction
- Offending text: “the 2.7% duplicate rows violate strict i.i.d.,” and “the 2.7% duplicate rows do not drive the verdict.”
- Problem: The counts imply a larger duplicate-row share. The env-labeled parent has 812,793 rows and 783,820 unique TARGETIDs, i.e., 28,973 extra rows. That is 28,973/812,793 ≈ 3.57% of rows (or 28,973/783,820 ≈ 3.69% relative to unique). Stating 2.7% is arithmetically inconsistent with the provided counts.
- Required fix: Correct the stated duplicate fraction (either as share of rows ≈ 3.6% or of unique ≈ 3.7%), and keep the design-effect inflation calculation consistent with the corrected fraction.

MAJOR

P5-M7 (Across Sec. V–VII, Fig. 5 right): Mixed null comparators without a single controlling reference
- Observation: You juxtapose (i) analytic Bonferroni thresholds derived from a standard-normal σ-from-half null, and (ii) permutation-based max-stat p-values (conditional on the observed global CW count). These are not strictly on the same null.
- Required fix: State explicitly in each place where both are shown that the Bonferroni threshold corresponds to the unconditional N(0,1) max-|σ| null, while the permutation pLEE is conditional on the observed matched-sample monopole. Either (a) present both but label them as different nulls, or (b) adopt the permutation max-stat as the primary control and move the parametric thresholds to Supplement with a brief rationale.

P5-M8 (Sec. IX A, completeness-weighted rebuild): Missing tabulation of class counts
- Problem: You report large shifts (void volume fraction 17.6% → 0.75%; “only 44% of common-mask cells and 26.6% of matched spirals retain their class,” and class-level fCW values), but no table of class n, nCW, and fCW is provided for either the completeness-weighted or the (recomputed) unweighted-in-window control.
- Required fix: Add a table with per-class n, nCW, fCW (with Jeffreys CI) for both the weighted rebuild and its matched unweighted control. This robustness result should be numerically reproducible in the paper/Supplement, not only via artifacts.

P5-M9 (Sec. VIII E, sky-position proxy for DESIVAST coverage): Proxy conflation risk
- Observation: You interpret “0 maximal voids per NSIDE=16 pixel” as “outside DESIVAST coverage.” While you flag it as a proxy, the body text then uses it causally to attribute the −4.75σ bin to outside coverage.
- Required fix: Provide an explicit intersection with the public DESIVAST angular mask (or polygon footprint), or move this inference to the Supplement and clearly label it as a proxy-only analysis. If mask construction is deferred, soften the causal attribution and quantify the fraction of 0-void pixels that are demonstrably inside the DESIVAST BGS footprint.

P5-M10 (Sec. VIII B, k=20 KDTree guard retained in main text numbers): Final values should use the exact recompute
- Observation: You show the k=20 KDTree-based membership statistics in the main Table VIII and retain them “for continuity with the released artifacts,” while noting that the exact recompute changes nvoid by +100 and shifts ΔfCW by 0.1 pp.
- Required fix: Promote the exact recompute (no k-limit) to the main numbers and relegate the k=20 guard to a sensitivity footnote. Main-text headline numbers should reflect the exact computation.

MINOR

P5-m7 (Sec. V, MC p-value precision beyond resolution): Overprecision and identical 3-decimal matches
- Observation: Multiple MC p-values are quoted to three decimals (e.g., p = 0.120 vs 0.119), and some “free vs stratified” comparisons report exactly matching values to 3 decimals with NMC = 1000, where seMC ≈ 0.009–0.015.
- Suggested fix: Standardize MC p to two significant digits and/or append “±0.01 (MC)” where appropriate. For “free vs stratified” comparisons, quote the absolute difference and note it is within 1 seMC.

P5-m8 (Sec. IV A step 9): Units phrasing for k
- Observation: “k carries physical h Mpc−1 units” is confusing. h Mpc−1 is standard comoving convention, not “physical.”
- Fix: Rephrase to “k is in h Mpc−1 (comoving units).”

P5-m9 (Sec. VIII F vs. Fig. 8 bottom): Pixel-count context could be clearer
- Observation: The text quotes 1,791 valid pixels (NSIDE=32, ≥ 200 spirals, full env-labeled parent), while Fig. 8 bottom shows 1,496 valid pixels (z ≤ 0.24 subset). Both are consistent but not cross-referenced.
- Fix: Add a parenthetical in the figure caption noting the z ≤ 0.24 restriction (already present) and, in text where 1,791 is cited, remind the reader that this is the full-redshift env-labeled parent; the 1,496 figure pertains to the z ≤ 0.24 subset.

P5-m10 (Sec. IV A step 4): “pp” vs. fraction micro-mix
- Observation: You write per-class changes “−0.005 pp” and “+0.013 pp.” Those are 5×10−3 and 1.3×10−2 percentage points (i.e., 5×10−5 and 1.3×10−4 in fraction), which is unusually fine precision for a prose statement.
- Suggested fix: Either round to 0.01 pp or report as fractional changes to avoid confusion.

P5-m11 (Sec. VIII C/D): Two nvoid values for REVOLVER without side-by-side context
- Observation: nvoid = 102,911 (REVOLVER spheres; Table X) vs 104,912 (catalog-native GALZONE; Sec. VIII D). You explain the definitions differ, but the reader must jump across sections to reconcile.
- Fix: Add a small side-by-side line in Table X or an inline parenthetical noting the catalog-native nvoid for immediate context.

P5-m12 (Sec. XI, footprint-leg vs. Table I numbers): Clarify DES vs DES-only counts
- Observation: Table I lists Leg DES matched primaries = 4,724, while the systematics split shows “DES-only” n = 1,924 (chirality-relevant). The difference stems from restricting to chirality-relevant spirals, but this is not stated.
- Fix: Add a note that footprint splits in Table XV are on the chirality-relevant subset, hence lower than the matched-primary footprint counts in Table I.

NIT

P5-n4 (Units consistency): Minor spacing/encoding in several “h −1 Mpc,” “Mpc/h,” and “h Mpc−1” occurrences.
- Fix: Uniformize to h−1 Mpc and h Mpc−1 throughout.

P5-n5 (Figure axis labels): A few axes are missing explicit unit notes (e.g., Fig. 4 redshift is dimensionless; Fig. 5 x-axis is a rank bin).
- Fix: Add explicit unit/meaning to axes for stand-alone clarity.

EXPLANATION

The second-pass emphasis was on recomputing counts/fractions-derived quantities, checking figure/body consistency, and scanning for unflagged arithmetic or comparability issues. Most headline numerics remained consistent with the body and with internal arithmetic. The notable new hard error is the duplicate-row fraction (2.7% vs ~3.6–3.7% by the paper’s own counts). Additional presentation/rigor issues include mixing parametric and permutation nulls without a uniform controlling reference, missing numeric tables for the completeness-weighted rebuild, and the need to promote the exact DESIVAST membership recompute to the main-text numbers. All other items are clarity and precision improvements.