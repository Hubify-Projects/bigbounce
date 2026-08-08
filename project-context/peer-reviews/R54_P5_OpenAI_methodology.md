# P5 R54 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R54_P5/p5_desi_chirality.pdf` md5=b01bfece pages=33
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6346 chars)
**Wall time**: 459.0s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample”

Scope of review
I evaluated methodology rigor, statistical validity, internal arithmetic consistency, dimensional analysis, and reproducibility. I re-computed all checkable numbers that appear in the abstract, tables, figures, and conclusions from the values printed in the manuscript. I also verified that sigma statistics from different null constructions are not conflated, and I checked the treatment of multiple testing and permutation sampling variability.

Overall assessment
The manuscript presents a careful, mostly self-consistent null result: within DESI DR1 and at the stated resolutions, spiral-galaxy chirality shows no detectable dependence on large-scale-structure environment. The bulk of the numerics I checked are internally consistent (counts, fractions, σ-from-half, simple two-sample z-tests, χ2 with d.o.f., Cramér’s V, Bonferroni thresholds, permutation p-value resolution vs NMC=1000, etc.). The paper commendably separates the raw σ-from-half (against 0.5) from monopole-referenced residuals and repeatedly cautions that σ scales like √N, which avoids a common pitfall.

That said, several items must be corrected or strengthened for PRD standards, chiefly: (i) a typographical but substantive formula error in the Clopper–Pearson one-sided bound; (ii) reproducibility: the load-bearing chirality catalog is only referenced by a HF slug and a companion “in preparation” paper — a frozen DOI for the exact catalog version used is required; (iii) a misleading “alternative convention” sentence for h−1 Mpc conversion; and (iv) some load-bearing robustness results are only described and relegated to external “artifacts” rather than summarized in the manuscript proper.

Detailed findings
ESSENTIAL

P5-E1 (Sec. VIII A, page 17): Incorrect formula for one-sided 95% binomial upper bound with 0 successes
Quoted: “with 0 of 6, the one-sided 95% binomial upper bound on the true in-hole fraction is 1 − 0.051/6 = 39% (the standard one-sided Clopper–Pearson bound 1 − α1/n …).”
Problem: The expression “0.051/6” is dimensionally and mathematically incorrect; it should read 0.05^(1/6). While the stated 39% value is numerically consistent with 1 − 0.05^(1/6) ≈ 0.393, the printed formula is wrong and could mislead readers.
Required fix: Replace “1 − 0.051/6” with “1 − 0.05^(1/6)”. Optionally add the numeric value 0.393 to show consistency.

P5-E2 (Data/provenance, Appendix C page 31; Sec. III A page 3; Abstract page 1): Missing frozen DOI for the load-bearing chirality catalog
Problem: The entire analysis depends on the 8.47M-object chirality catalog (Paper IV, “in preparation”), referenced by a mutable HuggingFace slug. The manuscript states “A DOI-minted archival snapshot … accompanies submission” for the code repository, but provides no DOI for the chirality catalog version actually used. Relying on a companion “in preparation” paper for both catalog content and the classifier-monopole interpretation does not meet PRD reproducibility standards.
Required fix: Provide a frozen DOI (e.g., Zenodo) for the exact chirality catalog version used, including an immutable checksum, and cite it in the main text and Appendix C. Ensure the catalog’s schema (columns used) is documented so the analysis can be rerun without the companion paper. Where conclusions invoke the Paper IV monopole amplitude, also report the matched-sample monopole (which you already do in Table XII) as the primary reference.

P5-E3 (Sec. IV A, footnote on page 5): Misleading “alternative convention” for h−1 Mpc conversion
Quoted: “The alternative convention χ[h−1 Mpc] = χ[Mpc]/h (divide-by-h, giving ≈1246 h−1 Mpc at z = 0.2) is not used here…”
Problem: As written, this suggests dividing by h is a “convention” for obtaining values in h−1 Mpc from Mpc. For a fixed physical length, the numerical value in h−1 Mpc units is h times the value in Mpc; dividing by h would be converting a different way (from h−1 Mpc to Mpc). The provided 1246 h−1 Mpc figure is thus not an “alternative convention” — it is the inverse transformation.
Required fix: Remove or correct this sentence to avoid confusion. A clear statement is: “To express a distance D in h−1 Mpc units, use D[h−1 Mpc] = h × D[Mpc]. The inverse conversion is D[Mpc] = D[h−1 Mpc]/h.” Keep the implemented multiply-by-h statement and sanity check (843 Mpc × 0.6766 ≈ 570 h−1 Mpc).

P5-E4 (Abstract page 1; Sec. V B pages 7–8): Primary estimator declaration and dependence on a companion “in preparation” paper
Problem: The paper’s primary estimand/test is designated post hoc (DESIVAST-anchored void vs non-void contrast), and several interpretations lean on Paper IV’s monopole being a classifier systematic. While you do re-measure the matched-sample monopole and emphasize that the two-sample contrasts are invariant to any catalog-wide monopole, the primary analysis should be fully anchored in this paper without reliance on an unpublished companion.
Required fix: Make the DESIVAST void-vs-non-void contrast the sole primary statistical test throughout (including in the Conclusions), and treat all references to the Paper IV monopole strictly as cross-checks. Where σpred is used, use the in-paper matched-sample monopole (fP5_CW = 0.49719) and propagate its quoted uncertainty (you already give ∼0.7σ at N ≈ 4×10^5). This keeps the manuscript self-contained.

MAJOR

P5-M1 (Sec. IX A, pages 23–24): Robustness results only described; key numbers absent from the manuscript
Problem: The selection-corrected and completeness-weighted T-Web robustness tests are important to the headline null and are repeatedly cited, but their basic per-class numbers (n per class and fCW per class) are not tabulated in the manuscript (only described and pushed to artifacts). For PRD, readers should not need to chase external artifacts to verify the central robustness claims.
Required fix: Add a small table in the main text or an appendix listing, for the selection-corrected rebuild: per-class (void/wall/filament/cluster) n and fCW (you already quote the fCW values), and likewise a concise summary for the completeness-weighted low-z stress test (per-class n and fCW or at least the void-class n and fCW). Include the stated in-window void-volume fractions pre/post weighting (17.6% → 0.75%) with their definitions.

P5-M2 (Sec. IX C, page 25): External T-Web DR1 comparison — quantify precisely
Problem: You state your T-Web void/knot fractions differ from Ref. [11] by “+8–18 pp” and “3–5 pp,” respectively, but the exact comparator values from Ref. [11] are not printed, and your own fractions are tracer- and footprint-mismatched with theirs.
Required fix: Quote the exact BGS volume-filling fractions from Ref. [11] in the text, and then state the deltas relative to your numbers explicitly (with a sentence on the caveats: footprint geometry, tracer mix, and cube vs shell). This can be a short parenthetical.

P5-M3 (Sec. V, page 6; throughout): Consistent reporting when juxtaposing σ-from-half and permutation p-values
Strength: You generally state that σ-from-half scales like √N and is not comparable across classes; you also provide label-shuffle max-stat pLEE with NMC = 1000 and note its MC resolution. In a few places (e.g., Table VII narrative) σ and p are juxtaposed without an immediate reminder of non-comparability.
Required fix: Wherever σ-from-half for multiple unequal-N classes are listed next to each other or next to p-values, add an explicit parenthetical reminding the reader that these σ are not directly comparable across rows/classes because of √N scaling (you already do this in Table III and elsewhere; extend this consistency to all such juxtapositions).

P5-M4 (Sec. III A, page 3; Appendix C page 31): Catalog dependency clarity (standalone-reader test)
Problem: The classifier details (equivariant ViT-Small with Z2 TTA) and the “equivariant” label notion are only referenced to Paper IV and a HuggingFace slug. While full ML specifics are not needed here, a minimal standalone description of the label semantics is required for readers who cannot access the companion.
Required fix: Add a brief paragraph in Sec. III A explicitly defining what “equivariant CW/CCW” labels are (e.g., how TTA was applied; that NS are excluded; the confidence column that is later used in systematics) and the minimal data schema (columns used in this paper) with a small example row schema. Point to the DOI of the frozen catalog (P5-E2).

MINOR

P5-m1 (Sec. IV B, page 6): Volume fractions presentation
The four canonical volume fractions in Fig. 2 sum to unity (0.244+0.413+0.333+0.010 = 1.000). Consider adding the exact numerical values to the caption (they are in text above; caption repeats only percentages to one decimal).

P5-m2 (Sec. VI A, Fig. 3, page 9): Design-effect qualifier
You correctly note a worst-case design-effect inflation of ≤1.9% due to duplicates. For clarity, add the corresponding widened CI numbers (± inflator) for the void/wall bars in the caption or a sentence indicating the impact is visually negligible at plot scale.

P5-m3 (Sec. VI D, Table V, page 10): Provide the actual fCW per quartile
You list n and σfrom half per quartile for cluster/filament, but not the corresponding fCW. Adding the fCW numbers (or Δ from 0.5 in pp) would make it easier for readers to gauge effect sizes directly, consistent with your emphasis on percentage-point ranges elsewhere.

P5-m4 (Sec. VIII E, page 20): Clarify sphere sets and radii
You note that hole-sphere maximum radius is 24.5 h−1 Mpc, while maximal-void effective radii are 10–32 h−1 Mpc. Add a one-line reminder that maximal spheres can be larger than any constituent hole because they are defined differently, to help readers reconcile the numbers without needing to infer.

P5-m5 (Appendix B, page 31): Include column totals
For Tables XVI–XVII, add row/column totals to ease independent χ2 recomputation by eye (you already provide n and marginals in text).

NITS

P5-n1 (Typo, multiple pages): Hyphenation and small typos
Examples: “de- generate” (Sec. VII, page 15), “per-cap join” (Sec. VIII D, page 19), “statisti￾cal” line breaks in awkward places. Please run a final typography pass to remove mid-word hyphenations introduced by line wrapping.

P5-n2 (Footnote placement, pages 2–3): The footnote marker “a” after the title on page 2 spills its sentence start (“with Φ”) onto page 3 in a way that reads as truncated. Consider moving the entire footnote body to a single page for readability.

P5-n3 (Consistency): You use both “h−1 Mpc” and “Mpc/h”. Although equivalent, pick one form in equations/footnotes for consistency (text can keep both).

Internal arithmetic and methodological checks (selected highlights)
- Abstract numbers reconcile with the body: 16,361,731 ZWARN=0 rows; 14,622,283 galaxies in the T-Web parent; 2,232,212 matched and deduped; 791,635 chirality-relevant; 812,793 env-labeled rows (with 783,820 unique spirals).
- Table III per-class fractions and σ-from-half recompute: filament 203,261/408,187=0.4980 → σ≈−2.56; cluster 197,284/397,505=0.4963 → σ≈−4.67; wall 3,359/6,673=0.5034 → σ≈+0.56; void 207/428=0.4836 → σ≈−0.68; all consistent within rounding.
- Bonferroni thresholds: K=5 at α=0.01 gives |σ|≈3.09; K=9 at α=0.05 gives |σ|≈2.77; correct.
- Density-quintile residuals (Table IV) match σpred = 2Δf √N with Δf = −0.0026; max residual |σobs − σpred| = 1.87 < 3.09.
- DESIVAST void vs non-void (Table VIII): Δf = +0.00067; SE = 0.00219; z = +0.31; p = 0.76; correct.
- Three-algorithm DESIVAST sphere-PIS contrasts (Table X): all |Δf| ≤ 0.0019 with z ≤ 1.12; correct. Catalog-native GALZONE contrasts: V2-REVOLVER Δ = −0.0037, z = −1.25; V2-VIDE Δ = +0.0019, z = +0.72; correct.
- Program-stratified filament: bright n=394,181 (0.4976), dark n=13,759 (0.5069), two-sample |z| ≈ 2.1 at the row level; consistent with the caveat that samples are not disjoint in TARGETID; whole-catalog unique-galaxy bright vs dark |z|=1.957 is transparently reported.
- Contingency χ2 and Cramér’s V recompute: class×program χ2=4933 on n=811,609 gives V=0.078; correct.
- Phase-2 sweep Table VII: ranges and pLEE values are plausible; the RS=10 cells are properly flagged as unresolved.

Length and focus
At 33 pages (including appendices), the paper is long for what is essentially a carefully demonstrated null. Much of the length is justified by robustness checks, but several robustness summaries could be compressed if key numbers are moved into compact tables. A focused version could likely be reduced to ~22–25 pages without loss of scientific content by:
- Moving some narrative repetition about the monopole to a single consolidated subsection.
- Consolidating robustness summaries into one or two compact tables in the main text and moving descriptive prose to an appendix.

Abstract-last drift (pattern-045) check
I re-read the abstract after the full paper. The abstract’s numerical claims (counts, fractions, σ, χ2, p-values, Phase-2 ranges and pLEE, DESIVAST Δf and n, Tempel cross-check size, HEALPix p-values, bright/dark differences, and RSD scope) are traceable and consistent with the body. The caveats about √N scaling and non-comparability are explicitly stated in the abstract near the class σ list.

Provenance surfaces (patterns 046/047)
- Code: a frozen GitHub tag is provided and claimed to be DOI-minted. Provide the DOI string in the manuscript (P5-E2 requires this anyway).
- Data: as above, a frozen DOI for the chirality catalog must be added.
- External VACs: DESIVAST links and versions appear correct; ASTRA EDR and Tempel DR10 citations look accurate.

Uncomputed quantitative claims (pattern-048)
Most qualitative “dominates” or “consistent with” statements are numerically supported (e.g., void-bin counting noise ranges and max residuals); where not, a pointer to an artifact is given. For PRD, add the minimal per-class numbers for the selection-corrected and completeness-weighted robustness runs in text (P5-M1).

Effect sizes
The manuscript consistently reports effect sizes in percentage points alongside σ/p and uses Cramér’s V for the large χ2, which is appropriate.

## Summary recommendation
MAJOR REVISIONS

The core statistical methodology is sound and the internal numerics I checked are consistent. However, PRD reproducibility and clarity standards require (i) correcting the Clopper–Pearson formula; (ii) providing a frozen DOI for the exact chirality catalog used, with a brief standalone description of the label semantics; (iii) correcting the misleading “alternative convention” for h−1 Mpc; and (iv) bringing a few load-bearing robustness numbers from external artifacts into the manuscript. With these fixes and minor clarifications, the paper would meet PRD’s methodological rigor and reproducibility bar for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

P5-E5 (Sec. IX A, selection-completeness weighting): Undefined α in δw formula and missing normalization details
Quoted: “δw = ng/(α nr) − 1 on randoms-supported cells…”
Problem: α is not defined anywhere in the manuscript, and the normalization convention (e.g., α = Ng/Nr within the same mask and redshift window) is not stated. For readers to reproduce δw unambiguously, α and the support mask used to compute it must be explicit. This is a dimensional/definition gap in the only place where a weighted overdensity is introduced.
Required fix: Define α explicitly (e.g., α ≡ ∑ng/∑nr over the identical angular/radial mask) and state the mask and redshift window used to compute it. If α is computed per shell, say so.

P5-E6 (Sec. VIII A, RSD Monte Carlo): Ambiguous membership-flip arithmetic
Quoted: “reassigns ∼ 4.4 × 10^4 hole-union memberships per realization (the void count rises from 57,081 to 76,490 ± 161…)”
Problem: A net increase of 76,490 − 57,081 = 19,409 void members per realization is reported, yet “reassigns ∼ 4.4×10^4” suggests roughly 44k flips. If the 44k counts in→out + out→in flips (with a net +19.4k), that should be said; as written, the numbers look inconsistent.
Required fix: Report both directions explicitly: #in→out, #out→in, and the net change, or rephrase to “total flips ~44k; net +19.4k.” Include percentages relative to the 678,945-galaxy low-z parent.

P5-E7 (Appendix A, toy EFT mapping): Dimensional consistency of the schematic operator is unclear
Quoted: “Lparity ⊃ gϕ (∇iϕ) (∇iρ/ρbg) (L̂·ẑ) … bound |gϕ (∇ϕ)/H0| ≲ 10−2/⟨|Δρ/ρbg|⟩.”
Problem: Even as a toy parametrization, gϕ and ∇ϕ units are not stated, leaving the ratio |gϕ∇ϕ|/H0 dimensionally ambiguous; ρ-gradient units and the contraction with L̂·ẑ are also left implicit. Given PRD’s standards, the toy expression should at least specify a unit convention that renders the bound dimensionless.
Required fix: State the intended units (e.g., ϕ dimensionless, ∇ϕ in H0 units so that gϕ is dimensionless), or rewrite the bound in terms of manifestly dimensionless ratios (e.g., |gϕ ∇ϕ|/(aH) at z ≈ 0.2). Emphasize again that this is schematic.

P5-M5 (Sec. VII, Table VII footnote vs table body): Inconsistent pLEE ranges between headline and “re-draw” text
Table VII lists pLEE spanning 0.13–0.56 across the nine cells (and 0.13–0.48 over the resolved six). The footnote then says the stratified re-draws are “0.14–0.54 vs. free 0.16–0.55,” which appears to contradict the 0.13 and 0.56 bounds in the same table.
Required fix: Clarify explicitly that the 0.16–0.55 range refers to a distinct RNG re-draw (not the headline numbers), and keep a single authoritative range in the main table text. If both are kept, label them unambiguously as “headline” vs “re-draw.”

P5-M6 (Sec. X, ASTRA EDR cross-validation): Max-|σ| across classifiers compared without a comparability reminder
Problem: The table and paragraph juxtapose “max |σ| vs 1/2” across ASTRA-argmax, ASTRA-entropy, and T-Web-on-overlap without an explicit reminder that these maxima arise from different class Ns and class partitions and are not directly comparable (you add such caveats elsewhere).
Required fix: Add the same √N non-comparability parenthetical you use in Sec. VI A/Table III, or prefer reporting pp effect sizes alongside σ with a note that class Ns differ per classifier.

P5-M7 (Sec. IV A, kernel specification): Gaussian smoothing kernel not fully specified in-text
Problem: The code artifacts likely fix this, but the manuscript only says “Gaussian-smooth δ in Fourier space with kernel Rs.” For reproducibility, the kernel should be stated (e.g., exp[−(kRs)^2/2]) and whether Rs is the Gaussian σ or FWHM.
Required fix: Add the explicit kernel functional form and the σ vs FWHM convention.

P5-J1 (Minor stale/mismatched numbers): HEALPix valid-pixel counts and p-ranges used in distinct contexts may confuse readers
- Sec. VI E reports NSIDE=32 pLEE = 0.135 with npix = 3,303 (all occupied pixels), while Fig. 8 bottom caption and Sec. VIII F report 1,496/1,791 valid pixels under a ≥200-spirals cut and different redshift cuts. These are distinct analyses but could be misread as inconsistent.
Required fix: Add one sentence in Fig. 8 caption and in Sec. VIII F reminding the reader that the pixel masks and cuts differ (full redshift vs z ≤ 0.24; with/without ≥200 cut), hence the different npix.

P5-m6 (Sec. III D, bounding box vs cell size): Box side 6,634 h−1 Mpc vs 256×25.9 = 6,630 h−1 Mpc
This likely reflects rounding, but the text gives both numbers. Consider harmonizing (e.g., “≈6,63×10^3 h−1 Mpc”) to avoid readers puzzling over a 4 Mpc/h discrepancy.

P5-m7 (Sec. VI A, Fig. 3): Use the matched-sample monopole as the dotted reference line
Figure 3 uses the Paper IV catalog monopole (0.4974) as the dotted line while the text later emphasizes the matched-sample monopole (0.49719). For consistency with your own preference to self-contain on P5 measurements, consider plotting the matched-sample line (difference is small, but clarity helps).

P5-m8 (Sec. VIII A, KDTree k sufficiency): Surprising “28% have > 20 holes within Rmax” deserves one clarifying sentence
Given Rmax = 24.5 h−1 Mpc, “28% … have more than 20 such candidates” sounds high without context. One sentence explaining that overlapping VoidFinder holes are dense by construction near void edges would prevent misinterpretation.

P5-m9 (Sec. IX A, completeness-weighted test): Quote the precise pre/post in-window class volume fractions in-table
You state “void volume fraction collapses from 17.6% to 0.75%” in prose. For completeness, add the full four-class in-window fractions pre/post weighting into the new robustness table you were already asked to add (P5-M1 in your first review), keeping readers in-manuscript.

P5-m10 (Sec. VIII F, per-pixel σvs-monopole stats): Define the ≥200-spirals pixel cut once
You present both ≥200 and other cuts across sections. A one-line definition near the first appearance (“we call pixels with ≥200 spirals ‘valid’ in per-pixel σ plots”) would reduce reader friction.

NO other discrepancies were found in recomputing the remaining σ-from-half values, two-sample z, χ2, Cramér’s V, Bonferroni thresholds, Jeffreys-CI half-widths, and simple percentage-point ranges that are printed in tables and figures; all matched to within rounding.