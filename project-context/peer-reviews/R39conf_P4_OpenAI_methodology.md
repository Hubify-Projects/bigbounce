# P4 R39conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/chirality_catalog_paper.pdf` md5=414048af pages=23
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7235 chars)
**Wall time**: 397.9s

---

Referee report for PRD submission: “Survey-Scale Galaxy Chirality with Equivariant TTA ...” (23 pages)

Scope of review
I audited the paper for methodological rigor, statistical validity, internal arithmetic and dimensional consistency, clarity on null procedures, estimator declarations, reproducibility and provenance, and consistency of abstract and conclusions with the body. I recomputed quoted fractions, σ values from provided means/variances, and effect-size conversions wherever possible from the text, tables, and equations.

Overall assessment
The work is ambitious and methodologically detailed. Many statistical caveats are explicitly stated; most scalars check out numerically. However, there are several essential issues that preclude acceptance in PRD in its current form: provenance/version inconsistency between the title page and Data Availability; pervasive reliance on internal repository path “artifact” pointers in the main text without a frozen DOI-backed archive; and a few clarity/sigma-comparability and presentation regressions that must be repaired. I detail all findings below.

Findings

ESSENTIAL

P4-E1. Version/provenance inconsistency
- Location: Page 1 (title block) vs. Page 21 (Data Availability)
- Problem: Title page states “Dated: June 13, 2026 — v1.0.185.” Data Availability states “Repository state for this version: commit 53b41d12 (v1.0.180, June 2026).” This is a direct inconsistency for a load-bearing provenance surface.
- Required fix: Align the paper’s version identifier and commit hash. Either (a) update the Data Availability section to the exact commit hash and tag corresponding to v1.0.185 and state explicitly that all reported artifacts derive from that commit, or (b) change the title-page version to v1.0.180 to match the commit, and state what changed (if anything) between .180 and .185. Include a single frozen archival DOI (Zenodo or equivalent) for the exact tarball underlying the paper.

P4-E2. Non-archival internal “artifact” path references in main text
- Location: Multiple occurrences throughout the main text and appendices, e.g. Page 3 (Sec. II.B): “artifact pipelines/p2_chirality/outputs/canonical_provenance/c17_item13_training_semantics.json”; Page 6: “artifact c12_r24conf_local_batch.json”; Page 7 footnote 1; Pages 8–20: many “artifact c9a/c9b/...” and path-like strings.
- Problem: The paper repeatedly relies on internal repository file paths and opaque artifact identifiers as evidence for results. These are not stable, citable, or accessible in the PRD archival record, and they do not meet PRD’s standards for reproducibility in the published paper.
- Required fix: Move all such implementation-level artifact references to a public, DOI-backed supplementary archive (single frozen release) and cite it via DOI with stable filenames/paths. In the main text, replace path-like pointers with descriptive labels and DOI references (e.g., “See Supplementary Archive (DOI:...), file X.json”). Ensure that every quantitative claim that currently cites an internal “artifact” has an accessible counterpart in the archived supplement.

P4-E3. Missing frozen data/code DOIs; incomplete Data Availability
- Location: Page 21 (Data Availability)
- Problem: The text states “A persistent archival DOI (Zenodo deposit of the versioned release) has not yet been minted.” PRD requires stable, archival reproducibility. GitHub/HuggingFace tags without a DOI are insufficient.
- Required fix: Before acceptance, deposit the exact catalog(s), code snapshot, and analysis artifacts used in the paper to a stable archive (Zenodo or equivalent), mint DOIs, and cite them. The archive must include the mask files, null streams, and all arrays needed to reproduce the main tables and figures (or scripts that deterministically regenerate them from the catalog). Update the paper to reference these DOIs.

P4-E4. Side-by-side σ values from different null procedures without immediate “not-comparable” caveat
- Location: Page 14–15, Sec. VII.c (Conclusions): the paragraph presenting “+3.64σ” and “+7.93σ” for the canonical mask
- Problem: In this specific juxtaposition, two σ values from different null constructions/field conventions are presented side-by-side without an explicit, local statement that they are not directly comparable (earlier in the paper this caveat is made; here it is missing at the point of juxtaposition).
- Required fix: Add an explicit sentence immediately adjacent to this juxtaposition clarifying that the +3.64σ and +7.93σ values are computed under different nulls/field normalizations and are not directly comparable. Consider consolidating to one canonical diagnostic number (preferably the 10k-permutation result) to avoid confusion.

MAJOR

P4-M1. Ambiguous units/wording for amplitudes in Ap (“0.57% (Ap-unit)”)
- Location: Page 7 (Sec. IV.C, unthresholded sample): “yields a 0.57% (Ap-unit) dipole...”
- Problem: Ap is a dimensionless asymmetry; calling it “0.57% (Ap-unit)” is ambiguous and nonstandard. Elsewhere Ap is consistently treated as a full-amplitude fractional unit (e.g., A = 0.017 = 1.7%).
- Required fix: Use a single, consistent amplitude convention throughout: either report Ap as a pure number (e.g., 0.0057) or as a percentage but make clear it is a fraction of unity in Ap units (e.g., “Ap = 0.57%,” explicitly noting Ap = 2(fCW − 1/2)). Remove “(Ap-unit).”

P4-M2. Hemisphere look-elsewhere treatment mixes two corrections in a confusing way
- Location: Page 19 (Appendix C.c)
- Problem: You report a direct-MC maximum-statistic look-elsewhere pLEE ≤ 10−4 for the hemisphere scan (which already incorporates trials), then apply an additional Bonferroni/BH correction over the same grid, stating it reduces significance to < 1σ. This double-penalizes and confuses interpretation.
- Required fix: Present a single principled look-elsewhere correction. If the direct-MC max-statistic null is the chosen method (it should be), report only that pLEE and explain interpretation (systematics versus cosmology). Remove or clearly segregate the heuristic Bonferroni/BH check to avoid implying a second correction of the same trials.

P4-M3. Overabundant “earlier run/rendering” and internal process commentary in the archival paper
- Locations: Page 7 footnote 1 (“An earlier run reported 0.43σ ... selection-filter defect ...”), Page 10 Fig. 8 caption (“An earlier rendering ... elevated ℓ=5 bar is not reproduced ...”), similar remarks elsewhere.
- Problem: Process-log and regression notes are useful in an internal audit but are out of scope for the archival paper; they distract and can confuse readers.
- Required fix: Remove these “earlier run/rendering” remarks from the main paper or move them to a brief note in the supplement if you must document evolution. Keep the archival paper focused on the final, audited results.

P4-M4. Figure 9 caption uses two observed z-values (7.28 and 7.21) with a long caveat
- Location: Page 15, Fig. 9 caption
- Problem: The caption mentions “obs. σ≈+7.28” (paper-canonical) and “this c9b-internal value is ... 7.21.” This invites confusion.
- Required fix: In the figure and caption, show a single observed value consistent with the figure’s own background null. If you wish to reference the paper-canonical value, do so in the main text, not in the caption of a different-null figure.

P4-M5. Edge-on contamination fraction (65.7%) lacks a clear methodological basis in the paper
- Location: Page 21 (Appendix E.a)
- Problem: The text states “65.7% of visually identified edge-on systems (b/a<0.3) receive CW/CCW labels” but later calls an axis-ratio cross-match the “canonical follow-up,” implying the 65.7% number might not be derived from a documented b/a cross-match.
- Required fix: Provide a clear derivation for the 65.7% figure (data source for b/a, sample selection, N and uncertainties), or remove the precise percentage and rephrase qualitatively. If based on a cross-match, include enough detail (or a pointer to the DOI-archived script/table) for reproducibility.

P4-M6. SHA256/mask-equivalence engineering details in main text
- Location: Page 20 (Appendix D.h, Table XI)
- Problem: The mask-equivalence audit with SHA256 prefixes is implementation detail more suitable for a reproducibility supplement.
- Required fix: Move the SHA256/mask audit to the supplementary archive; in the paper, retain a concise statement that the masks used in WLS and NaMaster are identical, with a DOI pointer to the audit.

MINOR

P4-N1. Excessive internal hyphenation artifacts and encoding glitches
- Location: Multiple pages; e.g., repeated “C 2 2 ◦” for “C2 apodization with 2°,” hyphenation artifacts (“canoni‑cal,” “apod‑ized”).
- Problem: Typesetting/glitch artifacts reduce readability.
- Required fix: Clean typesetting; ensure symbols like “C2 2°” render correctly; remove stray hyphenations.

P4-N2. Small typesetting error in Appendix D
- Location: Page 20, near Table X text: “z ≈ −18.1.34”
- Problem: The “.34” appears to be an errant footnote marker fused to the number.
- Required fix: Correct to “z ≈ −18.1” with a properly formatted footnote reference if intended.

P4-N3. Overlength for the claimed contribution
- Location: Whole paper (23 pages)
- Problem: For a null-detection methodology paper, 23 pages with many internal-audit details in the main text is lengthy.
- Required fix: Consider moving detailed QC and audit material (artifact paths, SHA256, earlier-run notes, extended template suites) to a supplementary appendix. A 15–18 page main paper would likely suffice.

P4-N4. Abstract-last drift check: minor cherry-pick in label-shuffle z
- Location: Page 1 (Abstract) vs. Page 7 (Sec. IV.C)
- Problem: The abstract gives the label-shuffle robustness as z = 0.70; the body reports both 0.58σ (same generator) and 0.70σ (independent implementation).
- Required fix: Either quote the 0.58σ value (same generator) in the abstract or explicitly say “0.58–0.70σ under two independent implementations” to avoid the appearance of cherry-picking the larger |z|.

P4-N5. Consistency of “not directly comparable” caveats
- Location: Various juxtaposed σ’s across the paper; mostly well-marked, but see P4-E4 and the following:
- Problem: While the paper is generally careful, each juxtaposition of σ’s from different nulls/fields should carry a local reminder.
- Required fix: Add a short parenthetical note in any remaining places where such σ’s appear side-by-side without the caveat (e.g., Sec. VII.c).

Arithmetic and dimensional checks (selected)
- Catalog counts (Page 5–6): NCW = 1,592,107; NCCW = 1,609,053; NNS = 5,273,371; totals check (sum = 8,474,531; spirals = 3,201,160).
- fCW (Catalog C): 1,592,107 / 3,201,160 = 0.497353; binomial σ ≈ 0.000279; deviation z ≈ −9.5; matches Table II.
- Catalog A fCW = 0.507879; σ ≈ 0.000274; z ≈ +28.7; matches Table II.
- Asymmetry suppression |Araw|/|Aeq| = 0.015758/0.005294 ≈ 2.98×; matches text (Page 5–6).
- Real-space HC dipole: reported 0.41σ and p = 0.31 from 10^4 isotropic permutations; consistent.
- MASTER apodized ℓ=1: (2.348e−5 − 1.71e−6)/2.99e−6 ≈ 7.29σ; matches +7.28σ.
- Canonical pre-/post-MASTER monopole leakage: reproduction fraction 99.32%; hemisphere max |A| z = (3.484e−3−1.693e−3)/0.405e−3 ≈ 4.42; both consistent with Table IV.
- Block-bootstrap WLS exclusion: (0.00455 − 0.034)/0.00163 ≈ −18.1σ; matches Table X.
- Fisher floors: σ(A) = √(3/N) checks for N = 3.2M (9.7e−4; 3σ ≈ 0.29%) and N = 0.95M (1.78e−3; 3σ ≈ 0.53%); consistent.
- Confusion matrix totals (Page 18): rows sum to 240,919; chirality accuracy on CW/CCW-labeled = 81,939/117,205 = 0.6991; matches text.

Other comments
- Novelty claim appears factually supported (3.2M spirals vs. 1.95M in CE-ResNet).
- Effect sizes are generally reported alongside σ throughout; good.
- Citations (journals/years/arXiv) appear correct for the ones spot-checked.

## Summary recommendation
MAJOR REVISIONS

Justification: The core methodology is careful, and most numbers check out. However, PRD cannot accept a paper that has (i) inconsistent version/provenance between the title and Data Availability, (ii) no frozen DOI-backed reproducibility archive, and (iii) persistent reliance on internal repository “artifact” pointers in the main text. Additionally, there are presentation issues (double look-elsewhere corrections; sporadic missing null-comparability caveats; ambiguous Ap-% wording; process-log remarks) that must be cleaned up. Addressing the ESSENTIAL and MAJOR points above, with a consolidated, DOI-anchored reproducibility package and tightened presentation, would make the paper suitable for reconsideration.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass)

ESSENTIAL

P4-E5. Training/augmentation accounting is internally inconsistent
- Location: Sec. II.B (Page 3)
- Issue: The dataset math around the 80/20 split and flip augmentation does not reconcile. You state 25,790 source images; after flip augmentation “the combined pool is 26,616 (80/20 split: ntrain = 21,293, nval = 5,323).” This implies 826 additional training images beyond the 25,790 sources. But then the pre-augmentation training pool would be 21,293 − 826 = 20,467, i.e., 79.3% of 25,790, not the stated 80%. Also, a “horizontal-flip augmentation of the training split” typically doubles that split (not +4%); here only 826 images were added. Clarify precisely:
  • How the 80/20 split was computed (by count or by target proportions).
  • Which subset received deterministic flips and why only +826 were added.
  • Provide an auditable, DOI-archived manifest for train/val indices and the augmentation policy so the 26,616 accounting is exactly reproducible.

P4-E6. Additional provenance inconsistency: release tag vs paper date
- Location: Data Availability (Page 21)
- Issue: You cite “Release tag: v2026.04” for the public catalog, while the paper is dated June 13, 2026 (v1.0.185) and the repository commit pinned is v1.0.180. This is another mismatch on a load-bearing provenance surface.
- Required fix: Harmonize all version surfaces (title-page version, commit hash, release tag) and bind them to a single DOI-archived snapshot. Each dataset/model/code reference in Data Availability should include the exact DOI and version string used in the analysis.

MAJOR

P4-M7. Unsubstantiated “+6.48σ pre-MASTER” claim for the raw catalog
- Locations: Sec. IV.C (Page 8, paragraph beginning “In contrast, Catalog A (raw) shows…”) and Fig. 7 caption (Page 10)
- Issue: You quote a +6.48σ pre-MASTER ℓ = 1 artifact for Catalog A, but no table/figure provides the inputs or null moments behind this number, nor is there a DOI-backed artifact cited for it. This is a key rhetorical contrast with the equivariant pipeline.
- Required fix: Provide the exact field convention, mask/weight, null definition, and a DOI-archived array supporting the +6.48σ value (or remove the number and state the qualitative point without an unsupported σ).

P4-M8. Abstract juxtaposes σ from different nulls without a local caveat
- Location: Abstract (Page 1): “post-MASTER … (+3.64σ … canonical mask; +7.28σ, apodized footprint)”
- Issue: These two σ values come from different fields/masks/nulls but are presented side-by-side in the Abstract without an explicit “not directly comparable” qualifier (you add such caveats elsewhere).
- Required fix: Add a brief qualifier in the Abstract that these σ values arise from different null procedures/field conventions and are diagnostic-only, not directly comparable.

P4-M9. “Axis-averaged” labeling in Fig. 9 is potentially misleading
- Locations: Sec. VII.a and Fig. 9 (Page 15)
- Issue: The figure’s heavy black curve is described as “axis-averaged” but is actually an average over three fixed coordinate axes {x, y, z}, not an average over random axes on S2. The text elsewhere is careful to distinguish axis conventions.
- Required fix: Clarify in the caption that the black curve is the mean over the three fixed coordinate axes; do not imply it’s an average over uniformly random orientations.

P4-M10. “Factor of ~6–12” tension with Shamir lacks explicit numerical basis
- Location: Sec. V.A (Page 12) and Abstract (Page 1)
- Issue: You state the present pipeline is inconsistent “by a factor of ∼6–12” with a ∼3% class of signals, but the two anchor amplitudes used to define the 6 and 12 bounds are not cited next to this claim. Readers cannot see immediately whether you are comparing to 0.32% (WLS best-fit) vs. 0.5–0.56% (regional maxima), or to the HC dipole floors.
- Required fix: Explicitly quote the two reference amplitudes that define the lower and upper ends of the 6–12 factor next to the claim (e.g., 3%/0.56% ≈ 5.4 and 3%/0.25–0.32% ≈ 9.4–12) and cite the DOI-archived computations used.

J. STALE/CONSISTENCY

P4-J1. Minor inconsistencies in quoted z-values across sections
- Locations: Sec. IV.C and Table III (Pages 8–11)
- Issue: The apodized ℓ = 1 significance appears as +7.28 in the body and +7.31 in Table III (10k-permutation recompute). Similarly, the canonical-unapodized z computed from the rounded table entries yields ≈7.98 rather than 7.93 (likely rounding of inputs).
- Required fix: Choose a single canonical z for each estimator/null and use it consistently across the paper, or add a parenthetical noting that the table entries are rounded and z is computed from full-precision arrays.

MINOR

P4-N6. “80/20” split is actually 79.3/20.7 by count
- Location: Sec. II.B (Page 3)
- Issue: Given ntrain = 21,293 and nval = 5,323 (pre-augmentation totals 20,467 + 5,323 = 25,790), the realized split is 79.3%/20.7%, not 80/20.
- Required fix: Either state the exact counts without the percentage or phrase it as “approximately 80/20 (20,467/5,323).”

P4-N7. Ambiguous formatting of “≥107”
- Location: Sec. VII.e (Page 15)
- Issue: “≥107 galaxies” can be read as ≥107 rather than ≥10^7.
- Required fix: Write “≥10^7 galaxies” or “≥ ten million galaxies.”

P4-N8. Fig. 7 caption includes numerical σ not shown in the figure
- Location: Fig. 7 caption (Page 10)
- Issue: The caption asserts 2.31σ (real-space) and +6.48σ (pre-MASTER) for the raw catalog, but the figure itself is just maps. Without an immediate cross-reference to a table/DOI, this is confusing.
- Required fix: Either add a body-text pointer immediately adjacent to Fig. 7 to the archived computations or remove the σ values from the caption (keep captions descriptive of what is visibly shown).

P4-N9. Fig. 8 caption mixes current-null results with legacy rendering commentary
- Location: Fig. 8 caption (Page 10)
- Issue: The caption both states the current canonical battery σ’s and references an “earlier rendering” with a different ℓ = 5 bar, which is extraneous in the archival paper.
- Required fix: Keep the caption focused on the null used for the plotted error bars and remove mention of prior renderings (this also aligns with your own policy to avoid process-log remarks in the main text).

WHY THESE ARE NEW
- The training/augmentation accounting inconsistency (P4-E5/P4-N6) was not covered previously and directly affects reproducibility and the interpretation of validation metrics.
- The raw-catalog +6.48σ claim (P4-M7) is a prominent contrast point that currently lacks citable support.
- Additional juxtaposition/comparability and axis-averaging clarity issues (P4-M8/P4-M9) arise in the Abstract and Fig. 9, beyond those noted earlier in Sec. VII.c.
- The “6–12×” statement (P4-M10) needs explicit numeric anchors; this hedge was not previously examined.
- Minor stale/rounding inconsistencies (P4-J1) and caption/body alignment issues (P4-N8/N9) are distinct from prior points and improve clarity.

These additions, combined with the earlier ESSENTIAL items (version/DOI/provenance; internal artifact pointers; look-elsewhere treatment; σ-comparability caveats), should bring the manuscript to PRD’s rigor and reproducibility standards.