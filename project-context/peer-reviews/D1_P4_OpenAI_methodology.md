# P4 D1 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p2_chirality/chirality_catalog_paper.pdf` md5=c47abc18 pages=23
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (4941 chars)
**Wall time**: 327.1s

---

D-round visual/packaging QA (camera-ready)

P4-D1-E1 (ESSENTIAL)
- Location: Pages 3, 6–11, 15–21 (multiple)
- Problem: Very long inline file paths and artifact identifiers in the body text and captions (e.g., “pipelines/p2_chirality/outputs/...”) break lines awkwardly, risk margin overflow in two-column layout, and are visually distracting. PRD production style does not accommodate multi-line code paths in the main text.
- Required fix: Move all artifact paths/filenames to a dedicated “Supplemental Material” or a short “Data and code availability” paragraph with a compact table or numbered list. Replace in-text paths by numbered pointers to that list (e.g., “see SM-A1”). Ensure line breaks do not exceed column width.

P4-D1-M2 (MAJOR)
- Location: Table I (page 5), Table III–IV (page 11), Table VII (page 16), Table X–XI (pages 20)
- Problem: Large, multi-column tables appear in single-column width; typography is cramped; captions are very long and wrap across multiple lines; risk of illegible small fonts and column spill.
- Required fix: Convert these to wide two-column tables (table* environment) and consider moving the longest explanatory material from captions into the main text or footnotes. Ensure consistent font size and adequate spacing.

P4-D1-M3 (MAJOR)
- Location: Figure 1 (page 3), Figure 7 (page 10)
- Problem: Multi-panel images (galaxy stamp galleries, side-by-side skymaps) are dense for a two-column width; fine detail in 224×224 cutouts and pixel-level sky structure will be illegible in print.
- Required fix: Make Fig. 1 a full-width figure* with fewer, larger thumbnails per class, or split into two figures. Make Fig. 7 a full-width figure* or move one map to the Supplement and keep the most informative panel in the main text at larger size.

P4-D1-M4 (MAJOR)
- Location: Figure 2 (page 6), Figure 6 (page 9), Figure 8 (page 10), Figure 9 (page 15)
- Problem: Axis labels and tick labels appear small relative to panel size; long parenthetical notes in captions (“σ values across panels arise from distinct null procedures...”) crowd the layout.
- Required fix: Increase font sizes for axes/ticks and symbols; move repeated “distinct nulls” disclaimer into a single, clearly labeled note at the beginning of the Results section, and retain a shorter per-figure reminder (“Null procedure: see Sec. III A”).

P4-D1-m5 (MINOR)
- Location: Throughout (equations and text)
- Problem: Some math and symbols convert to literal ASCII in the prose (e.g., “ˆ y, ˆ zˆ”, “deg2”, “C
2 2
◦”).
- Required fix: Ensure all math is set in math mode (ŷ, ẑ; deg^2; C2 apodization with 2° length). Eliminate stray carets and duplicated hats.

P4-D1-m6 (MINOR)
- Location: Section headings and page breaks (multiple pages; e.g., pages 12–13)
- Problem: Occasional orphaned headings at the bottom of a column, followed by the section body on the next page/column.
- Required fix: Adjust floats and insert \enlargethispage or \vspace as needed to keep a heading with at least two lines of subsequent text in the same column.

P4-D1-n7 (NIT)
- Location: Title block (page 1)
- Problem: Very long title breaks unevenly across lines.
- Required fix: Insert manual line breaks at natural phrase boundaries to improve readability.

— End of D-round items —

PRD methodology referee report

ESSENTIAL ISSUES

P4-E1
- Section: Appendix D, page 20 (bottom paragraph before Table X)
- Problem: Typo merging a statistic with a footnote marker: “z ≈ −18.1.23” (should be “z ≈ −18.1”; the trailing “.23” appears to be a footnote or artifact number).
- Required fix: Correct to “z ≈ −18.1” and place any footnote marker properly.

P4-E2
- Section: Data Availability (page 22)
- Problem: Reproducibility artifacts are not yet archived with stable DOIs; the text states “A persistent archival DOI has not yet been minted.” PRD requires citable, immutable deposits at acceptance.
- Required fix: Before acceptance, deposit the exact release (catalog, code, trained weights, analysis artifacts) to a permanent archive (e.g., Zenodo) and replace placeholders/commit-only pointers with final DOIs. Provide checksums for large binary artifacts.

P4-E3
- Section: Multiple (pages 4, 14, 19–21)
- Problem: Presence of internal version/draft bookkeeping in the scientific narrative (e.g., “earlier versions of this analysis…”, “earlier version of this paragraph overstated…”, “post-R29”, “superseded by…” inside body text). PRD manuscripts must not include editorial history.
- Required fix: Remove all version-history commentary from the main text. If a correction to prior preprints is necessary, note it once in an endnote or arXiv version history, not in the journal manuscript.

P4-E4
- Section: Throughout Results/Conclusions and some figure captions (e.g., pages 8–11, 14–15)
- Problem: Multiple σ values from different null procedures are juxtaposed; most places add the “not directly comparable” caveat, but a few juxtapositions lack it (e.g., page 9 “+7.28σ / +9.78σ” without an immediate null-specifier; page 12 conclusion (a) lists z≈68–218 for injections next to the observed +7.28σ without a local reminder).
- Required fix: At every place where two or more σ values appear side-by-side and are derived under different nulls, fields, masks, or weight maps, explicitly label each with its null and restate “not directly comparable” (or place an italicized footnote reference to Sec. III A) right there.

P4-E5
- Section: Main text and Appendices (all pages citing “artifact c9b”, “c12 r24conf ...”, etc.)
- Problem: Methodological claims rely on internal artifact references that are not accessible or uniquely identified to a reader without browsing a repository tree. This breaks the standalone-reader criterion.
- Required fix: Provide a concise table in the manuscript or Supplemental Material mapping each “artifact” identifier to a stable DOI/URL and a one-line description (dataset, script, seed). Ensure every load-bearing claim (e.g., specific null sizes, injection counts) is fully specified in the paper, not just by an artifact nickname.

MAJOR ISSUES

P4-M1
- Section: Abstract (page 1) and Conclusions (pages 14–15)
- Problem: Abstract uses many technical qualifiers correctly but remains dense. Cross-check with body: all headline numbers (N=8,474,531; Nspiral=3,201,160; primary HC dipole +0.41σ with p=0.31; WLS exclusion z≈−18; monopole+mask 99.32%; MASTER +7.28σ; A50≈0.75%; A95 in (1.0%,1.5%]) are traceable and arithmetically consistent. However, two sentences risk misinterpretation by a casual reader: (i) “+7.28σ” appears in Abstract without immediate “diagnostic/systematics” qualifier in the same sentence (it appears later in the paragraph); (ii) “Falsification criterion…” is estimator-specific but could be read as universal.
- Required fix: In the Abstract, keep each σ value’s diagnostic vs. primary status unambiguous within the same sentence (e.g., “diagnostic +7.28σ”). Add “estimator-specific” to the falsification sentence.

P4-M2
- Section: Sec. IV.C (page 7–8), Injection floor statements and null-quantile
- Problem: The text presents A95,null-quantile = 0.68% alongside A50 ≈ 0.75% (injection) with a caution that these are different objects; fine. But the precision implied by 0.68% from N=10^4 null permutations should be stated with sampling error, since percentiles of heavy-tailed nulls are noisy at the 10^-4 level.
- Required fix: Report sampling uncertainty on A95,null-quantile (e.g., via bootstrap over the 10^4 null draws, giving an error band) or round to one significant figure consistent with sampling error (e.g., “≈0.7%”).

P4-M3
- Section: Sec. IV.D and Table III (page 11)
- Problem: The canonical unapodized row cites z=+7.93 and rank-p=3×10^-4 from 10^4 permutations. The implied minimum p-resolution is 1/(N+1) ≈ 1.0×10^-4, which is fine; however, reporting z to two decimals based on sample σ estimated from 10^4 permutations of a heavy-tailed distribution may overstate precision.
- Required fix: Round these z values to one decimal or provide an uncertainty (e.g., via split-half variance of σnull). Confirm stability of z under a second independent 10^4 permutation stream and report the variation.

P4-M4
- Section: Appendices A–D (pages 15–21)
- Problem: Several nonstandard sections for PRD (Facilities, Software, AI tool usage) and long operational digressions (implementation guards, internal QC annotations) reduce readability and are not typical for PRD format.
- Required fix: Move “Facilities/Software/AI tool usage” to Acknowledgments or Supplemental Material, and streamline operational notes to essential methods. The core paper can be shortened by 4–6 pages without scientific loss by moving extended audits (e.g., block-scale sensitivity, mask-threshold sweeps, code-QC logs) to Supplement.

P4-M5
- Section: Sec. III.D and Appendix B (pages 4, 17–18)
- Problem: Flip-TTA protocol is clear; however, the distinction between “protocol implementation check” vs. “model equivariance” could be sharpened, and symbols in Eq. (2) should be linked to stored catalog columns without relying on recovered probabilities later.
- Required fix: Add a short, explicit mapping table (symbol → catalog column) and state any numerical tolerances used in the flip-identity QC (max deviation, fraction of rows affected) in a consolidated place (not scattered).

P4-M6
- Section: Sec. IV.E and Appendix C (pages 12, 18–19)
- Problem: “Signal-hunt diagnostics” repeatedly refer to multi-cell scans and look-elsewhere controls; while the direct-MC LEE control is solid, some reported single-cell σ values are placed without immediately stating the family-wise error control result in the same sentence.
- Required fix: Whenever reporting a maximum over scans, present simultaneously the family-wise p-value (or adjusted σ) alongside the raw maximum σ to avoid confusing the reader.

MINOR ISSUES

P4-m1
- Section: Table II (page 5)
- Problem: “Dev. (σ)” computed from unrounded fractions—good—but provide a note defining “asymmetry-A units” to connect with repeated factor-of-two statements in captions.
- Required fix: Add a single-line footer in Table II: “Asymmetry A = 2(fCW−1/2).”

P4-m2
- Section: Eq. (3) and surrounding text (page 7)
- Problem: Minor typographic consistency: use Nspiral(p) consistently (not alternating with N(p)
spiral).
- Required fix: Enforce consistent macro.

P4-m3
- Section: Sec. A (pages 15–17)
- Problem: Effective sky fraction definitions are fine; compact these into a single displayed equation to improve readability.
- Required fix: Replace prose with a boxed equation defining feff_sky, and move numeric values to a concise table (keep Table VII but shorten text).

P4-m4
- Section: References (page 22–23)
- Problem: Citation format is close to AAS; minor inconsistencies (e.g., mixed use of journal abbreviations, presence/absence of DOIs).
- Required fix: Conform to PRD reference style: consistent journal abbreviations; add DOIs where required by PRD; ensure arXiv IDs match years.

P4-m5
- Section: Conclusions (page 15)
- Problem: The phrase “A future survey detecting ... would be in tension” is fine, but please add that this tension is with the present HC real-space estimator only (already discussed in-body).
- Required fix: Append “with our primary HC real-space estimator under the stated null.”

NITS (cosmetic/typographic)

P4-N1
- Section: Throughout
- Problem: Occasional inconsistent spacing around inequalities (e.g., “Nall ≥1”).
- Required fix: Use non-breaking thin spaces around operators (“Nall ≥ 1”).

P4-N2
- Section: Fig. 9 caption (page 15)
- Problem: “obs.\ = 7.21” appears to be a LaTeX artifact.
- Required fix: Replace with “obs. z = 7.21” or remove entirely per earlier standardization.

P4-N3
- Section: Appendix E footnote 4 (page 21)
- Problem: Very long footnote; risks readability.
- Required fix: Move to Supplemental Material or compress to one sentence with a cross-reference to Sec. IV.D.

Arithmetic and internal-consistency audit highlights

- Catalog counts and fractions: CW 1,592,107; CCW 1,609,053; Nspiral=3,201,160 → fCW=1,592,107/3,201,160=0.497353 (matches); σbin ≈ sqrt(0.25/N)=0.000279 (matches); deviations in Table II are consistent: +28.7σ (A), −9.47σ (C).
- Fisher floor: σ(A)=√(3/N) for N=3,201,160 gives 9.68×10^-4; for N=949,584 gives 1.78×10^-3 (matches).
- MASTER ℓ=1 apodized: (2.348×10^-5 − 1.71×10^-6)/2.99×10^-6 = 7.28 (matches).
- Canonical unapodized Table III: (7.27−0.57)/0.84=7.97 → z=7.9 (matches rounding).
- Monopole+mask pre-MASTER reproduction: 1.6846/1.6961=0.9932 → 99.32%; z=(1.6961−1.6846)/0.0068=1.69 (matches).
- Hemisphere max|A| z=(3.484−1.693)/0.405=4.42 (matches).
- GZ1 cross-match confusion matrix sums to 240,919; chirality accuracy among mutual spirals ≈81,939/117,205=0.699 (matches 69.91%).
- Effect sizes consistently provided alongside significances; where “diagnostic” channels are used, this is mostly clear. Ensure per P4-E4 that every juxtaposition is labeled.

Scope and length

P4-M7 (MAJOR)
- The manuscript is long (23 pages) for PRD given the number of diagnostic side-channels and extensive operational commentary. The core scientific contribution (primary null in real space; WLS exclusion; identification of monopole–mask leakage) can be communicated in ~16–18 pages.
- Recommendation: Move extended implementation/QC, most artifact-path details, and some secondary diagnostic panels to Supplemental Material; keep only the minimal diagnostics needed to support the primary claims.

## Summary recommendation
MAJOR REVISIONS

The statistical methodology is careful and the arithmetic checks out; the authors clearly distinguish diagnostic from primary channels in most places. However, the manuscript in its current form does not meet PRD production and methodological presentation standards due to (i) unresolved production-critical items (DOIs missing; internal version/draft language present; long code paths in text), (ii) a few essential clarity/typography fixes (erroneous “z ≈ −18.1.23”; missing local “not comparable” caveats in some juxtapositions), and (iii) excessive length and operational detail for a PRD article. Addressing the ESSENTIAL and MAJOR points above, consolidating null-procedure labeling, and moving nonessential diagnostics/QC to Supplemental Material should make the paper suitable for reconsideration.

---

## PASS 2 — self-critique findings (what initial review missed)

P4-E6 (ESSENTIAL)
- Location: Figure 7 caption (page 10)
- Problem: Two σ values from different estimators/nulls are juxtaposed without local labeling or an explicit “not directly comparable” caveat: “2.31σ real-space dipole + +6.48σ pre-MASTER ℓ = 1 artifact.”
- Required fix: Add explicit null/estimator labels in the caption (e.g., “2.31σ, real-space, isotropic-permutation null; 6.48σ, pre-MASTER pseudo-Cℓ, label-shuffle null”) and state “not directly comparable; see Sec. III A.”

P4-E7 (ESSENTIAL)
- Location: Table III caption (“Appendix A.a”), Appendix A cross-refs
- Problem: Nonstandard subsection referencing (“Appendix A.a”) is not PRD style and may not resolve with the journal’s float/cross-ref system.
- Required fix: Replace “Appendix A.a” with a standard cross-reference (e.g., “Appendix A, item a” or “Appendix A 1”) using a proper \label/\ref so it compiles in PRD.

P4-E8 (ESSENTIAL)
- Location: Sec. IV.C, paragraph beginning “Sensitivity to the confidence threshold: dropping the confidence threshold entirely…”
- Problem: The observed unthresholded amplitude A=0.57% is compared to A50≈0.36%, A95≈0.63% computed under a per-pixel binomial null, while the z-values immediately preceding are reported for both pixel-permutation and per-galaxy label-shuffle nulls. The comparison mixes null conventions without an explicit local reminder.
- Required fix: Add a short sentence noting that the injection floors cited here use the binomial null (distinct from the permutation/label-shuffle nulls used for z), and state “not directly comparable across null conventions.”

P4-M8 (MAJOR)
- Location: Sec. V.A (Comparison with previous work)
- Problem: Units inconsistency and potential ambiguity: “maximum WLS template amplitude … 0.32% (in Ap units…)”. Elsewhere Ap is given as dimensionless (×10−3) without “%”. Appending “%” to Ap values is nonstandard and invites confusion with fCW units.
- Required fix: Express Ap values consistently as dimensionless (e.g., 3.2×10−3), and when helpful also translate to fCW units in parentheses (“=0.16% in fCW deviation”). Audit the section for any lingering “%” after Ap.

P4-M9 (MAJOR)
- Location: Appendix D.d (Leg-proxy ℓ=1 partial closure)
- Problem: The claim “∼25% of the observed canonical-mask ℓ=1 amplitude” is not numerically grounded in the text (no absolute amplitudes or error bars shown).
- Required fix: Provide the measured |Cℓ=1| (or amplitude) for the leg-proxy contribution and the total, with uncertainties, and show how the 25% fraction is computed. Add a brief sensitivity check (e.g., under alternative weights or apodization).

P4-M10 (MAJOR)
- Location: Appendix E.a (Edge-on galaxy contamination)
- Problem: The statement “65.7% of b/a<0.3 objects receive CW/CCW labels” lacks the sample size and uncertainty.
- Required fix: Report N(b/a<0.3), counts per class, and a binomial uncertainty on the 65.7%. If derived from a subset, state the selection and mask.

P4-M11 (MAJOR)
- Location: Appendix A.c (Monopole subtraction paragraph)
- Problem: σ values (“+1.85” to “+3.64”) are presented without explicitly restating the null size for these specific computations. Since σ depends on the null sample, precision and comparability are unclear locally.
- Required fix: Add the null definition and size (e.g., “500 label-shuffle permutations”) right in this paragraph, and append “not directly comparable to σ from other null sizes.”

P4-M12 (MAJOR)
- Location: Throughout the Results where null names appear (e.g., Sec. IV.C, VI.A, VII; Appendix A–D)
- Problem: Inconsistent nomenclature for nulls (“isotropic-bootstrap,” “pixel-permutation,” “per-galaxy label-shuffle,” “per-pixel binomial”) risks reader confusion.
- Required fix: Add a one-line glossary in Sec. III A that defines each null name precisely and mandate its consistent use. Where a different null is used later (e.g., binomial for a specific injection), restate the exact name and parameters.

P4-m7 (MINOR)
- Location: Figure 8 caption vs. body text (Sec. IV.D)
- Problem: Embedded annotation in Fig. 8 reports σℓ=1 = +3.63 while the body text reports +3.64 for the same canonical-mask residual.
- Required fix: Harmonize the rounding (choose one and use it consistently).

P4-N4 (NIT)
- Location: Captions and body (e.g., Fig. 2 caption “§III D” vs. body “Sec. III D”)
- Problem: Mixed use of “§” and “Sec.” for section references.
- Required fix: Standardize to “Sec.” per PRD style.

NO OTHER ADDITIONAL ARITHMETIC DISCREPANCIES FOUND
- I rechecked each explicit arithmetic example not covered in the initial review (e.g., monopole-subtraction 34% reduction, confusion-matrix sums/accuracies, hemisphere statistic, block-bootstrap exclusion math). All recomputed values match the manuscript’s numbers within rounding. The remaining numerical claims without adjacent inputs (e.g., several z-values reported only with their null moments) cannot be independently verified from the text alone.