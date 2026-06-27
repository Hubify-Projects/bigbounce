# P4 R55 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R55_P4/chirality_catalog_paper.pdf` md5=fbed4276 pages=23
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6903 chars)
**Wall time**: 405.3s

---

Referee report on “Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)”

Scope of review
- Focus: methodology rigor (statistical validity, derivations, internal arithmetic consistency, error propagation, estimator declarations, null procedures), and fidelity of the abstract/conclusions to the body.
- I audited the numbers and equations reported in the abstract and conclusions against the main text, recomputed claims where possible, and checked the consistency of masks, normalizations, and null procedures across figures/tables.

Overall assessment
- The paper presents a large chirality-labeled catalog (8.47 M galaxies; 3.20 M spirals) and a careful estimator hierarchy culminating in a primary real-space dipole consistent with null. Many good safeguards are in place: clear primary/secondary estimator declarations, repeated warnings that σ from distinct nulls are not comparable, and multiple null constructions.
- However, the manuscript mixes multiple field definitions, masks, and null procedures across the text and abstract, with duplicate headline σ for the same qualitative diagnostic, which risks confusion. The text is also littered with internal repository path references (“artifact pipelines/...”), which are not acceptable in the main text for PRD and should be moved to Supplement/Zenodo DOIs.
- A few quantitative statements (e.g., the 65.7% edge-on labeling fraction) are not supported by a traceable derivation within the paper, and there is at least one numerical typesetting error (“z ≈ −18.1.34”).
- Several methodological results (e.g., MASTER-channel injection completeness) are quoted only as ranges without tabulated medians/IQRs and should be documented more explicitly in the paper/Supplement.

Findings

ESSENTIAL

P4-E1 (Sec. II–VII; many pages): Internal repository path “artifact” references in the body text
- Problem (multiple locations; e.g., p.3, p.5, p.6–8, p.9–12, p.14–16, p.17–22): The paper repeatedly embeds internal file paths and ephemeral artifact names (e.g., “pipelines/p2_chirality/outputs/canonical_provenance/c17_item13_training_semantics.json”, “artifact c9b”, etc.) in the main narrative.
- Required fix: Move all such references to a dedicated Reproducibility/Supplementary Materials section with stable DOIs (Zenodo or similar). In the main text, refer to numbered Supplemental sections/DOIs rather than internal paths. The Data Availability section (p.22) must include permanent DOIs for the exact versions used in the paper prior to acceptance.

P4-E2 (Abstract p.1; Sec. IV.C–D; Table I, Table III): Two different headline ℓ = 1 “canonical” σ values appear (+3.64σ from a 500-MC run and +7.93σ from a 10^4-permutation run)
- Problem: The abstract and body report both +3.64σ (500-MC direct single-mode decoupling on the canonical mask) and +7.93σ (10^4 permutations, canonical unapodized row of Table III) as “canonical” diagnostics. Although the manuscript repeatedly notes they are “not directly comparable,” presenting two canonical numbers invites reader confusion/cherry-picking.
- Required fix: Pre-declare one canonical MASTER diagnostic (estimator + field convention + mask + weight + null size) and report only that headline number in the abstract/body. Move the alternative as a consistency check to Supplement, or unify to a single null size (≥10^4) across both canonical/apodized channels and re-report consistently.

P4-E3 (Appendix D.g, p.20): Numerical typesetting error “z ≈ −18.1.34”
- Problem: The “block-bootstrap z” line reads “z ≈ −18.1.34”, evidently footnote markers bleeding into the numeric value.
- Required fix: Correct to “z ≈ −18.1” and place footnotes 3 and 4 unambiguously outside numbers. Sweep the manuscript for any other instances where superscript footnote markers may have merged with numerals.

P4-E4 (Sec. V.A, p.12): Ambiguous unit statement “0.32% (in Ap units)”
- Problem: Ap is dimensionless and equals twice the fCW deviation. Reporting a “percent” in “Ap units” is intrinsically confusing.
- Required fix: State amplitudes consistently in Ap and/or in fCW units with the explicit conversion. For example: “A = 0.0032 in Ap units (0.16% in fCW units).” Apply this convention consistently wherever percentages for Ap appear.

P4-E5 (Appendix E.a, p.21): Unsupported and internally inconsistent “65.7% of b/a<0.3 edge-on systems receive CW/CCW labels”
- Problem: The statement gives a precise fraction (65.7%) but later in the same paragraph says the axis-ratio cross-match that would define the b/a < 0.3 set is “deferred.” It is unclear what sample/N produced 65.7%.
- Required fix: Provide the exact selection, N, and measurement procedure (including catalog matched for b/a) that yield 65.7%, or remove the number and rephrase qualitatively. If this fraction is from a pilot or external visual sample, document it in text or Supplement with counts.

MAJOR

P4-M1 (Sec. VI.A.b, p.13–14; Table V): Non-standard axis sampling for injection–recovery
- Problem: Initial injections use θ ∼ U(0, π) (not area-uniform); a later spot check claims negligible difference. PRD readers will expect area-uniform axis draws (cos θ ∼ U[−1,1]) throughout.
- Required fix: Redo Table V using area-uniform axis draws for all amplitudes, or provide a side-by-side table/figure quantitatively comparing both conventions (median P(σ>3), CIs). State the axis convention unambiguously where A50/A95 are quoted.

P4-M2 (Appendix C.c, p.19): Look-elsewhere corrected hemisphere p-value reported as “pLEE ≤ 10−4” with N=10^4 permutations
- Problem: With 10^4 permutations and zero exceedances, the standard report is p = 1/(N+1) ≈ 1.0×10−4 (one-sided upper limit). The inequality “≤10−4” is fine but uninformative without the observed max-statistic and null baseline.
- Required fix: Report explicitly p = 1/(N+1) = 1.0×10−4 (upper bound), and add the observed maximum asymmetry value and the null mean/σ for that max-statistic so effect size is clear.

P4-M3 (Sec. VII.a, Fig. 9; Table VI): MASTER-channel completeness and “median z” quoted only as broad ranges
- Problem: The paper states z ≈ 68–218 (Ap = 1.7%) and ≈ 209–685 (Ap = 3%) without tabulating exact medians/IQRs by axis. It also does not list the null moment calibration per amplitude.
- Required fix: Provide a small table with, for each injected amplitude and axis: number of injections, the null σ used, median recovered z, and 16–84% ranges. Clarify the null sample size per amplitude (it appears to be the same label-shuffle null used for scoring; state N).

P4-M4 (Sec. IV.D, Table IV; Sec. IV.C, Table III; Appendix A.a): Multiple field normalizations without a compact conversion map
- Problem: The monopole+mask analysis uses a pre-MASTER fCW-map pseudo-Cℓ; canonical MASTER rows use Ap or (fCW−0.5)=Ap/2 with different weightings. While each section notes the difference, it is cumbersome for readers to translate.
- Required fix: Add a one-paragraph “Normalization map” (or a small table) listing, for ℓ=1: (i) the measured C1 in the pre-MASTER fCW-map convention, (ii) the measured C1 in the MASTER Ap convention (both canonical and apodized footprints), and (iii) the corresponding null means/σ, with explicit conversions Ap ↔ fCW−1/2. This will let readers cross-check numbers without chasing artifacts.

P4-M5 (Sec. IV.C/D; Table I; Table III): Pair every headline σ with an empirical rank-p
- Problem: Some headline σ (e.g., +7.28σ apodized MASTER ℓ=1, Sec. IV.C) appear without the paired rank-p right there, although Table III contains it. PRD readers benefit from seeing both together due to heavy-tailed nulls.
- Required fix: In the main text where a σ is first reported for each channel, also report the companion empirical rank-p (one-sided) as in Table III, or add a compact table that collects (z, rank-p) pairs for all headline values.

P4-M6 (Abstract p.1; Sec. IV; Appendix A): Ambiguity of mask/field/weight per headline statistic
- Problem: The paper uses three masks/footprints and several field definitions. While Appendix A and Table VII help, many main-text headlines do not state the mask/weight explicitly.
- Required fix: For each headline number in the abstract and Sec. IV, include a parenthetical tag in-line, e.g., “apodized footprint (Nall ≥ 1), Wp=Nall, C2 2° apodization” or “canonical mask (Nspiral ≥ 10), binary weight, demonopole-subtracted Ap/2 field.”

P4-M7 (Sec. VI.A.a, p.13): Fisher floor derivation is only heuristic
- Problem: σ(A) = √(3/N) is quoted after a one-line heuristic. This is a standard result, but the derivation as written is not fully convincing.
- Required fix: Provide a short, self-contained derivation (e.g., via a least-squares estimator for A with yi ∈ {±1}) in an appendix, or cite a canonical reference deriving the √(3/N) result.

MINOR

P4-m1 (Sec. VII.c, p.15): Misleading “canonical” wording
- Problem: “the body canonical +7.28σ” is used for the apodized footprint MASTER result; elsewhere “canonical” refers to the unapodized canonical mask.
- Required fix: Reserve “canonical” for the unapodized Nspiral ≥ 10 mask; call the other “apodized footprint” consistently.

P4-m2 (Sec. IV.C, p.7–8): Significant-figure consistency for Adip and A95,nq
- Problem: Adip=4.4×10−3 and A95,nq=6.8×10−3 are mixed with 0.57% etc. Adopt a single precision convention and include the Ap ↔ % mapping each time both appear.
- Required fix: Present all amplitudes in Ap with two significant figures, and in parentheses give the fCW-equivalent percentage.

P4-m3 (Table III caption, p.11; Sec. IV.C): “Gaussian-equivalent” σ occasionally ambiguous
- Required fix: When a “Gaussian-equivalent σ” is from rank-p (rather than null moments), explicitly say “Gaussian σ from rank p”.

P4-m4 (Throughout; e.g., p.9, p.16–17): Typesetting polish
- Problem: “C 2 2 ◦”, stray spaces around symbols, occasional “monopole+mask” vs “monopole–mask”.
- Required fix: Standardize as “C2 apodization, 2°”; use consistent hyphenation for “monopole–mask”.

P4-m5 (Sec. V.A, p.12): Rephrase “0.32% (in Ap units)”
- Required fix: State as A = 0.0032 in Ap units (0.16% in fCW units).

P4-m6 (Appendix C vs Table IV): Direction-grid sizes
- Required fix: Group the 648-direction (10° grid) and 768-direction (NSIDEdir=8) hemisphere scans in one place and cross-reference to avoid confusion.

NIT

P4-N1 (Abstract p.1): Tautological phrasing “canonical unapodized row in Table III gives +7.93σ” followed by repetitions
- Required fix: Trim to a single, clear sentence.

P4-N2 (Throughout): The phrase “eight-anchor systematic battery”
- Required fix: Replace with “eight-test systematic diagnostic suite.”

P4-N3 (Throughout): Use PRD style for approximation symbols consistently (≈ vs ~).
- Required fix: Standardize per journal style.

P4-N4 (Figures): Axis labels
- Problem: Figures (e.g., Fig. 8) would benefit from explicitly stating the field convention and units in the axis label/legend.
- Required fix: Add “field = Ap (dimensionless)” or “pre-MASTER fCW-map” as appropriate.

Checks of arithmetic and internal consistency (selected)
- Catalog totals: 8,474,688 − 157 = 8,474,531; NCW+NCCW+NNS = 1,592,107 + 1,609,053 + 5,273,371 = 8,474,531. Nspiral = 3,201,160; spiral fraction 37.774% (consistent).
- Global fCW (Catalog C): 1,592,107/3,201,160 = 0.497353; σbin ≈ 0.000279; deviation from 0.5 is −0.002647 ⇒ −9.49σ (table shows −9.47; rounding ok).
- Catalog A fCW: deviation 0.007879; σ ≈ 0.000274 ⇒ 28.75σ (table +28.72; rounding ok).
- MASTER ℓ=1 (apodized footprint): (2.348×10−5 − 1.71×10−6)/2.99×10−6 = 7.28σ (matches).
- Canonical unapodized ℓ=1 (10^4 permutations): (7.27−0.57)/0.84 = 7.98σ (table shows +7.93; rounding).
- Monopole+mask leakage (pre-MASTER): data 1.6961×10−2 vs null mean 1.6846×10−2; Δ/σ = 0.00115/0.000068 = 1.69σ; reproduction 99.317% (reported 99.32%).
- Fisher floor: σ(A) = √(3/N)=9.68×10−4 (N=3.201×10^6) and 1.78×10−3 (N=9.49584×10^5) (matches text).
- Monopole subtraction: ⟨A⟩mask,gw = −0.005294 equals 2(fCW − 0.5) with fCW = 0.497353 (consistent).

Abstract-last drift sweep
- Every abstract claim is traceable to the body. The key caveats (“σ from distinct nulls not directly comparable,” “harmonic-channel results diagnostic-only,” “A95 bracketed,” “falsification criterion estimator-specific”) are present in the abstract and sustained in the body. However, reporting two headline canonical ℓ=1 σ values in the abstract (3.64σ and 7.93σ) needs consolidation per P4-E2.

Provenance surfaces
- Data Availability (p.22) cites a GitHub commit and a HuggingFace tag; it explicitly says the persistent DOI is “not yet minted.” For PRD acceptance, the exact analysis artifacts must have a frozen DOI. This is part of P4-E1.

Length
- The paper is long (23 pages) for a methods null-detection report. With consolidation of duplicate diagnostics, removal of inline artifact pointers to Supplement, and unification of the canonical MASTER statistic, this could likely be reduced to ~18 pages without loss of content.

## Summary recommendation
MAJOR REVISIONS

The methodology is largely sound and many internal checks are done carefully, but the manuscript in its present form does not meet PRD standards for clarity and presentation. The most urgent issues are: (i) removal/relocation of internal artifact paths and provision of stable DOIs, (ii) consolidation to a single declared canonical MASTER diagnostic and consistent reporting in the abstract/body, (iii) correction of a numerical typesetting error, and (iv) support/clarify the edge-on 65.7% number and axis-draw convention for injections. Addressing the enumerated ESSENTIAL and MAJOR items will make the results unambiguous and reproducible at PRD’s bar.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-pass only; new items that were not in my initial report)

ESSENTIAL

P4-E6 (Sec. IV.C vs Table III): Inconsistent C1 data value for the apodized MASTER ℓ=1 channel
- Issue: The body text states C1 = 2.348×10−5 (500-MC null: ⟨C1⟩=1.71×10−6, σ=2.99×10−6, z=+7.28). Table III (10^4 permutations) reports C1 = 24.74×10−6 = 2.474×10−5 with ⟨C1⟩=1.93×10−6, σ=3.12×10−6, z=+7.31. The measured C1 differs by ~5% between text and table, beyond mere rounding. The manuscript does not state that the measured C1 itself changed (only the null changed).
- Required fix: Unify the reported measured C1 to a single definitive value (and state its null) in both text and table, or explicitly explain why different measured C1 values appear (e.g., different field versions, apodization, or exact map used). Pick one canonical apodized result and use it consistently.

MAJOR

P4-M8 (Sec. IV.C vs Abstract): Conflicting z for the HC real-space dipole under the per-galaxy label-shuffle null
- Issue: Sec. IV.C gives z = 0.58 (rank-p = 0.26) for the HC real-space dipole under a per-galaxy label-shuffle null, and then says an independent implementation gives z = 0.70 (p = 0.23). The abstract cites z = 0.70 without clarifying it comes from a different implementation. This is a headline diagnostic reported in the abstract.
- Required fix: Choose one definitive value (with its exact null size/seed) for the per-galaxy label-shuffle result and report only that number consistently (abstract and body). If both are kept, present them side by side with precise methodological differences and explain why they differ.

P4-M9 (Sec. V.A vs Appendix D.g/Table X): Best-fit dipole amplitude mismatch (0.32% vs 0.455% in Ap units)
- Issue: Sec. V.A states “maximum WLS template amplitude … 0.32% (in Ap units)” for a “full-footprint regional fit,” while Appendix D.g/Table X reports Abest_dipole = 4.55×10−3 (0.455% in Ap units) from the joint nuisance-marginalized WLS. The relationship between these two “best-fit” amplitudes (different design/mask/weight?) is not explained, yet both are used to compare against literature amplitudes.
- Required fix: Clarify precisely what each amplitude refers to (mask, weighting, template set, regional vs global fit) and reconcile the discrepancy. Provide a short table of best-fit amplitudes across the distinct WLS variants (with masks/weights/templates), so the reader can understand why 0.32% and 0.455% differ.

P4-M10 (Sec. II.B; Appendix B.a): Training augmentation accounting is unusual and under-documented
- Issue: Only 826 extra images are credited to horizontal-flip augmentation (26,616 − 25,790), implying flips were not applied wholesale to the training pool. This is atypical for static augmentation and hard to square with the stated procedure.
- Required fix: Explicitly describe the augmentation protocol that yields +826 images (e.g., was flip applied to a small flagged subset only? was augmentation on-the-fly per epoch rather than dataset expansion?). Provide pre/post-augmentation counts for each source, and confirm that the validation set is leak-free from augmentation artifacts.

P4-M11 (Throughout Sec. IV–VII; Tables III–V; Appendices): Heterogeneous null sample sizes and backgrounds impede clarity
- Issue: The manuscript alternates among NMC = 200, 500, 1000, 2000, 10,000, and mixed background constructions (pixel-permutation, label-shuffle, depth-stratified) for closely related diagnostics, while giving headline σ in the body without always tagging the null size/type at the point of first mention.
- Required fix: Standardize null sizes for each declared headline estimator (e.g., always 10^4 for MASTER, 10^4 for real-space HC, etc.) or add a consolidated table mapping each headline σ to its exact null definition and NMC. Then keep those exact pairs in the abstract/body to avoid drift.

MINOR

P4-m7 (Appendix D.g, footnote 3): Inconsistent super-pixel counts for NSIDE=4
- Issue: The footnote first states “would fall to ∼110” super-pixels at NSIDE=4, then gives a measured run with “∼127 super-pixels.”
- Required fix: Replace both with the exact number actually used and keep consistent (“127 super-pixels”), or keep one rounded number consistently.

P4-m8 (Sec. III.A.b; Sec. IV.C; Fig. 9 caption): Apodized MASTER ℓ=1 “z” drifts between 7.28 and 7.31
- Issue: The text alternates between +7.28 (500-MC) and +7.31 (10^4). The figure footnote also cites 7.21 within a separate internal-null scoring. This is confusing for a single headline diagnostic.
- Required fix: Pick one canonical apodized ℓ=1 σ and use it consistently across text/captions; if a different null is used in a figure-internal scorer, explicitly mark it as internal and non-canonical once, not with a third number.

P4-m9 (Data Availability): Potentially malformed model/catalog URLs
- Issue: The catalog URL has embedded spaces (“galaxy- chirality- catalog”) which likely break the link.
- Required fix: Verify and correct all URLs; avoid line breaks or spurious spaces in DOIs/links.

P4-m10 (Fig. 9 label; Sec. VII.a): Notation glitch “axis x, ˆ y, ˆ zˆ”
- Issue: Extra hat on z (ˆ zˆ).
- Required fix: Standardize to x̂, ŷ, ẑ.

P4-m11 (Throughout): “104-permutation” typesetting without caret
- Issue: Several places show “104 -permutation” (missing ^).
- Required fix: Standardize to 10^4 everywhere.

P4-m12 (Appendix A.a): Unreferenced “pre-subtraction” σ = +1.85 claim
- Issue: Statement “increases σ from +1.85 to +3.64” for canonical-mask decoupled C1 lacks a nearby reproduction of the pre-subtraction numbers (C1, ⟨C1⟩, σnull).
- Required fix: Provide the pre-subtraction values (data, null mean, null σ) or remove the +1.85 claim.

P4-m13 (Fig. 7 caption): Missing null specification for quoted σ
- Issue: Caption reports “2.31σ” (real-space) and “+6.48σ” (pre-MASTER ℓ=1) without stating the nulls or NMC locally (needed because the figure juxtaposes two estimators).
- Required fix: Add parenthetical null type and NMC for both σ in the caption.

NIT

P4-N5 (Throughout): “10^4” spacing/parenthesis inconsistencies and occasional “104”
- Fix: Normalize typography for all exponents and permutation counts.

P4-N6 (Sec. VII; elsewhere): Occasional “≈” vs “~” usage mixed
- Fix: Standardize per PRD style.

P4-N7 (Sec. IV.C footnotes; Appendix captions): Minor punctuation/spacing around units (e.g., “2◦” vs “2 °”)
- Fix: Use a single consistent style (e.g., “2°”) throughout.

Explanation
I focused on items routinely missed on first pass: stale numeric drift between body and tables, inconsistent reporting of the same diagnostic across sections, augmentation accounting, and small but confusing cross-reference/notation mismatches. The apodized C1 mismatch and the dual z values for the label-shuffle real-space dipole are the most consequential new issues, because both touch headline diagnostics that appear in the abstract.