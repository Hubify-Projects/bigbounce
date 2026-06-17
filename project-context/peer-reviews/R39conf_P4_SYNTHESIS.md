# P4 R39conf — v3 native-PDF cross-vendor SYNTHESIS

**Reviewers**: Claude_brutal, Gemini_cosmology, Grok_brutal, OpenAI_methodology, Perplexity_citations

## ⛔ ROUND DEGRADED — reviewer leg(s) FAILED: Claude_brutal
Failed legs are API errors, NOT zero-finding clean reviews. This round
MUST NOT count toward any clean-round counter; re-run after the failure
(e.g. API credit top-up) is resolved.
**Total findings (across all reviewers)**: 33
**Distinct consensus groups**: 7

## Per-reviewer finding counts

| Reviewer | ESSENTIAL | MAJOR | MINOR | NIT |
|----------|-----------|-------|-------|-----|
| Claude_brutal | 0 | 0 | 0 | 0 |
| Gemini_cosmology | 0 | 0 | 0 | 0 |
| Grok_brutal | 3 | 3 | 0 | 2 |
| OpenAI_methodology | 6 | 10 | 9 | 0 |
| Perplexity_citations | 0 | 0 | 0 | 0 |

---

## Consensus-grouped findings (most reviewers first)

### `sigma_mixing` — ESSENTIAL — **CONSENSUS** (2 reviewers)

Reviewers: Grok_brutal, OpenAI_methodology

- **[Grok_brutal/P4-E1/ESSENTIAL]**: **P4-E1 (ESSENTIAL)**   Section: Abstract (p. 1) + Table I caption (p. 5) + Sec. IV C (p. 7)   Problem: Abstract states “+0.41σ (moment-z … p = 0.31, 10^4 isotropic-null realizations)” and immediately juxtaposes “robust under per-galaxy label-shuffle null, z = 0.70”. Table I caption explicitly warns that the two σ values “are not directly comparable across rows”. The abstract omits this qualifier.   Required fix: Remove or qualify every cross-null σ comparison in the abstract; the present wording violates the paper’s own stated statistical policy.
- **[OpenAI_methodology/P4-E4/ESSENTIAL]**: P4-E4. Side-by-side σ values from different null procedures without immediate “not-comparable” caveat - Location: Page 14–15, Sec. VII.c (Conclusions): the paragraph presenting “+3.64σ” and “+7.93σ” for the canonical mask - Problem: In this specific juxtaposition, two σ values from different null constructions/field conventions are presented side-by-side without an explicit, local statement that they are not directly comparable (earlier in the paper this caveat is made; here it is missing at the point of juxtaposition). - Required fix: Add an explicit sentence immediately adjacent to this juxt…
- **[OpenAI_methodology/P4-M8/MAJOR]**: P4-M8. Abstract juxtaposes σ from different nulls without a local caveat - Location: Abstract (Page 1): “post-MASTER … (+3.64σ … canonical mask; +7.28σ, apodized footprint)” - Issue: These two σ values come from different fields/masks/nulls but are presented side-by-side in the Abstract without an explicit “not directly comparable” qualifier (you add such caveats elsewhere). - Required fix: Add a brief qualifier in the Abstract that these σ values arise from different null procedures/field conventions and are diagnostic-only, not directly comparable.
- **[OpenAI_methodology/P4-N8/MINOR]**: P4-N8. Fig. 7 caption includes numerical σ not shown in the figure - Location: Fig. 7 caption (Page 10) - Issue: The caption asserts 2.31σ (real-space) and +6.48σ (pre-MASTER) for the raw catalog, but the figure itself is just maps. Without an immediate cross-reference to a table/DOI, this is confusing. - Required fix: Either add a body-text pointer immediately adjacent to Fig. 7 to the archived computations or remove the σ values from the caption (keep captions descriptive of what is visibly shown).

### `audit_artifact` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: Grok_brutal

- **[Grok_brutal/P4-E2/ESSENTIAL]**: **P4-E2 (ESSENTIAL)**   Section: Abstract (p. 1) + footnote 1 (p. 7) + multiple artifact footnotes (pp. 2, 4, 9, 10, 15, 16, 19, 20)   Problem: The PDF body contains repeated internal-audit language (“An earlier run reported 0.43σ”, “Artifact: pipelines/p2_chirality/…”, “R7/R8-style” provenance strings, commit-hash references, superseded-run notes). PRD does not publish review-log or repository bookkeeping.   Required fix: Excise every such string; replace with stable, citable DOIs or remove.

### `length` — MAJOR — _single-reviewer_ (1 reviewer)

Reviewers: Grok_brutal

- **[Grok_brutal/P4-M1/MAJOR]**: **P4-M1 (MAJOR)**   Section: Entire manuscript (23 pp.)   Problem: A null result plus systematics diagnostics is presented in a 23-page article. PRD length guidelines for a methods/null-result paper of this scope are typically ≤12–14 pages. The present length is disproportionate to the incremental observational claim.   Required fix: Condense to ≤14 pages or justify the length in a cover letter.

### `table_ii,shamir_citation` — MAJOR — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P4-M10/MAJOR]**: P4-M10. “Factor of ~6–12” tension with Shamir lacks explicit numerical basis - Location: Sec. V.A (Page 12) and Abstract (Page 1) - Issue: You state the present pipeline is inconsistent “by a factor of ∼6–12” with a ∼3% class of signals, but the two anchor amplitudes used to define the 6 and 12 bounds are not cited next to this claim. Readers cannot see immediately whether you are comparing to 0.32% (WLS best-fit) vs. 0.5–0.56% (regional maxima), or to the HC dipole floors. - Required fix: Explicitly quote the two reference amplitudes that define the lower and upper ends of the 6–12 factor nex…

### `table_iv` — MAJOR — _single-reviewer_ (1 reviewer)

Reviewers: Grok_brutal

- **[Grok_brutal/P4-M2/MAJOR]**: **P4-M2 (MAJOR)**   Section: Sec. IV D (p. 9) + Table IV (p. 11) + Fig. 8 (p. 10)   Problem: The 99.32 % “reproduction” figure for the monopole-only generative null is quoted without an effect-size statement (fractional power, Cramér’s V, or equivalent). The reader cannot judge practical significance.   Required fix: Add a quantitative effect-size metric for every headline percentage or σ claim.

### `table_ii,table_iv,fisher_floor` — MINOR — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P4-N5/MINOR]**: P4-N5. Consistency of “not directly comparable” caveats - Location: Various juxtaposed σ’s across the paper; mostly well-marked, but see P4-E4 and the following: - Problem: While the paper is generally careful, each juxtaposition of σ’s from different nulls/fields should carry a local reminder. - Required fix: Add a short parenthetical note in any remaining places where such σ’s appear side-by-side without the caveat (e.g., Sec. VII.c).  Arithmetic and dimensional checks (selected) - Catalog counts (Page 5–6): NCW = 1,592,107; NCCW = 1,609,053; NNS = 5,273,371; totals check (sum = 8,474,531; s…

## Other findings (24)

- **[Grok_brutal/P4-E3/ESSENTIAL]**: **P4-E3 (ESSENTIAL)**   Section: Abstract (p. 1) + Sec. I (p. 2) + Sec. VII (p. 14)   Problem: Abstract and introduction repeatedly assert “to our knowledge, the largest chirality-labeled galaxy catalog to date”. No quantitative comparison table or citation to the previous largest published catalog appears. The claim is therefore unsupported.   Required fix: Provide a one-line table or explicit ci…
- **[Grok_brutal/P4-M3/MAJOR]**: **P4-M3 (MAJOR)**   Section: Sec. VI A (p. 12) + Table V (p. 13)   Problem: The 50 %-recovery-at-3σ threshold (A = 0.75 %) is derived from an injection-recovery sweep performed only on the HC-broad subsample. The abstract presents this number as a survey-wide sensitivity floor without the subsample qualifier.   Required fix: State the exact subsample and selection function in the abstract or remov…
- **[Grok_brutal/P4-N1/NIT]**: **P4-N1 (MINOR)**   Section: Fig. 4 caption (p. 8) + Fig. 7 (p. 10)   Problem: Color-scale limits are given as [−0.08, +0.08] in A_p units but the accompanying text never states the conversion factor to f_CW deviation units on the same figure. Minor inconsistency.   Required fix: Add explicit conversion in caption.
- **[Grok_brutal/P4-N2/NIT]**: **P4-N2 (MINOR)**   Section: Bibliography (pp. 22–23)   Problem: Several arXiv IDs are given without journal reference even when the paper has been published (e.g., refs. 1, 5, 7). Minor formatting issue.   Required fix: Update to published citations where available.  **P4-NIT1 (NIT)**   Multiple figure captions contain the literal string “artifact: pipelines/…”. Cosmetic only.  **Summary recommen…
- **[OpenAI_methodology/P4-E1/ESSENTIAL]**: P4-E1. Version/provenance inconsistency - Location: Page 1 (title block) vs. Page 21 (Data Availability) - Problem: Title page states “Dated: June 13, 2026 — v1.0.185.” Data Availability states “Repository state for this version: commit 53b41d12 (v1.0.180, June 2026).” This is a direct inconsistency for a load-bearing provenance surface. - Required fix: Align the paper’s version identifier and com…
- **[OpenAI_methodology/P4-E2/ESSENTIAL]**: P4-E2. Non-archival internal “artifact” path references in main text - Location: Multiple occurrences throughout the main text and appendices, e.g. Page 3 (Sec. II.B): “artifact pipelines/p2_chirality/outputs/canonical_provenance/c17_item13_training_semantics.json”; Page 6: “artifact c12_r24conf_local_batch.json”; Page 7 footnote 1; Pages 8–20: many “artifact c9a/c9b/...” and path-like strings. - …
- **[OpenAI_methodology/P4-E3/ESSENTIAL]**: P4-E3. Missing frozen data/code DOIs; incomplete Data Availability - Location: Page 21 (Data Availability) - Problem: The text states “A persistent archival DOI (Zenodo deposit of the versioned release) has not yet been minted.” PRD requires stable, archival reproducibility. GitHub/HuggingFace tags without a DOI are insufficient. - Required fix: Before acceptance, deposit the exact catalog(s), cod…
- **[OpenAI_methodology/P4-M1/MAJOR]**: P4-M1. Ambiguous units/wording for amplitudes in Ap (“0.57% (Ap-unit)”) - Location: Page 7 (Sec. IV.C, unthresholded sample): “yields a 0.57% (Ap-unit) dipole...” - Problem: Ap is a dimensionless asymmetry; calling it “0.57% (Ap-unit)” is ambiguous and nonstandard. Elsewhere Ap is consistently treated as a full-amplitude fractional unit (e.g., A = 0.017 = 1.7%). - Required fix: Use a single, consi…
- **[OpenAI_methodology/P4-M2/MAJOR]**: P4-M2. Hemisphere look-elsewhere treatment mixes two corrections in a confusing way - Location: Page 19 (Appendix C.c) - Problem: You report a direct-MC maximum-statistic look-elsewhere pLEE ≤ 10−4 for the hemisphere scan (which already incorporates trials), then apply an additional Bonferroni/BH correction over the same grid, stating it reduces significance to < 1σ. This double-penalizes and conf…
- **[OpenAI_methodology/P4-M3/MAJOR]**: P4-M3. Overabundant “earlier run/rendering” and internal process commentary in the archival paper - Locations: Page 7 footnote 1 (“An earlier run reported 0.43σ ... selection-filter defect ...”), Page 10 Fig. 8 caption (“An earlier rendering ... elevated ℓ=5 bar is not reproduced ...”), similar remarks elsewhere. - Problem: Process-log and regression notes are useful in an internal audit but are o…
- **[OpenAI_methodology/P4-M4/MAJOR]**: P4-M4. Figure 9 caption uses two observed z-values (7.28 and 7.21) with a long caveat - Location: Page 15, Fig. 9 caption - Problem: The caption mentions “obs. σ≈+7.28” (paper-canonical) and “this c9b-internal value is ... 7.21.” This invites confusion. - Required fix: In the figure and caption, show a single observed value consistent with the figure’s own background null. If you wish to reference…
- **[OpenAI_methodology/P4-M5/MAJOR]**: P4-M5. Edge-on contamination fraction (65.7%) lacks a clear methodological basis in the paper - Location: Page 21 (Appendix E.a) - Problem: The text states “65.7% of visually identified edge-on systems (b/a<0.3) receive CW/CCW labels” but later calls an axis-ratio cross-match the “canonical follow-up,” implying the 65.7% number might not be derived from a documented b/a cross-match. - Required fix…
- **[OpenAI_methodology/P4-M6/MAJOR]**: P4-M6. SHA256/mask-equivalence engineering details in main text - Location: Page 20 (Appendix D.h, Table XI) - Problem: The mask-equivalence audit with SHA256 prefixes is implementation detail more suitable for a reproducibility supplement. - Required fix: Move the SHA256/mask audit to the supplementary archive; in the paper, retain a concise statement that the masks used in WLS and NaMaster are i…
- **[OpenAI_methodology/P4-N1/MINOR]**: P4-N1. Excessive internal hyphenation artifacts and encoding glitches - Location: Multiple pages; e.g., repeated “C 2 2 ◦” for “C2 apodization with 2°,” hyphenation artifacts (“canoni‑cal,” “apod‑ized”). - Problem: Typesetting/glitch artifacts reduce readability. - Required fix: Clean typesetting; ensure symbols like “C2 2°” render correctly; remove stray hyphenations.
- **[OpenAI_methodology/P4-N2/MINOR]**: P4-N2. Small typesetting error in Appendix D - Location: Page 20, near Table X text: “z ≈ −18.1.34” - Problem: The “.34” appears to be an errant footnote marker fused to the number. - Required fix: Correct to “z ≈ −18.1” with a properly formatted footnote reference if intended.
- **[OpenAI_methodology/P4-N3/MINOR]**: P4-N3. Overlength for the claimed contribution - Location: Whole paper (23 pages) - Problem: For a null-detection methodology paper, 23 pages with many internal-audit details in the main text is lengthy. - Required fix: Consider moving detailed QC and audit material (artifact paths, SHA256, earlier-run notes, extended template suites) to a supplementary appendix. A 15–18 page main paper would like…
- **[OpenAI_methodology/P4-N4/MINOR]**: P4-N4. Abstract-last drift check: minor cherry-pick in label-shuffle z - Location: Page 1 (Abstract) vs. Page 7 (Sec. IV.C) - Problem: The abstract gives the label-shuffle robustness as z = 0.70; the body reports both 0.58σ (same generator) and 0.70σ (independent implementation). - Required fix: Either quote the 0.58σ value (same generator) in the abstract or explicitly say “0.58–0.70σ under two i…
- **[OpenAI_methodology/P4-E5/ESSENTIAL]**: P4-E5. Training/augmentation accounting is internally inconsistent - Location: Sec. II.B (Page 3) - Issue: The dataset math around the 80/20 split and flip augmentation does not reconcile. You state 25,790 source images; after flip augmentation “the combined pool is 26,616 (80/20 split: ntrain = 21,293, nval = 5,323).” This implies 826 additional training images beyond the 25,790 sources. But then…
- **[OpenAI_methodology/P4-E6/ESSENTIAL]**: P4-E6. Additional provenance inconsistency: release tag vs paper date - Location: Data Availability (Page 21) - Issue: You cite “Release tag: v2026.04” for the public catalog, while the paper is dated June 13, 2026 (v1.0.185) and the repository commit pinned is v1.0.180. This is another mismatch on a load-bearing provenance surface. - Required fix: Harmonize all version surfaces (title-page versio…
- **[OpenAI_methodology/P4-M7/MAJOR]**: P4-M7. Unsubstantiated “+6.48σ pre-MASTER” claim for the raw catalog - Locations: Sec. IV.C (Page 8, paragraph beginning “In contrast, Catalog A (raw) shows…”) and Fig. 7 caption (Page 10) - Issue: You quote a +6.48σ pre-MASTER ℓ = 1 artifact for Catalog A, but no table/figure provides the inputs or null moments behind this number, nor is there a DOI-backed artifact cited for it. This is a key rhe…
- **[OpenAI_methodology/P4-M9/MAJOR]**: P4-M9. “Axis-averaged” labeling in Fig. 9 is potentially misleading - Locations: Sec. VII.a and Fig. 9 (Page 15) - Issue: The figure’s heavy black curve is described as “axis-averaged” but is actually an average over three fixed coordinate axes {x, y, z}, not an average over random axes on S2. The text elsewhere is careful to distinguish axis conventions. - Required fix: Clarify in the caption tha…
- **[OpenAI_methodology/P4-N6/MINOR]**: P4-N6. “80/20” split is actually 79.3/20.7 by count - Location: Sec. II.B (Page 3) - Issue: Given ntrain = 21,293 and nval = 5,323 (pre-augmentation totals 20,467 + 5,323 = 25,790), the realized split is 79.3%/20.7%, not 80/20. - Required fix: Either state the exact counts without the percentage or phrase it as “approximately 80/20 (20,467/5,323).”
- **[OpenAI_methodology/P4-N7/MINOR]**: P4-N7. Ambiguous formatting of “≥107” - Location: Sec. VII.e (Page 15) - Issue: “≥107 galaxies” can be read as ≥107 rather than ≥10^7. - Required fix: Write “≥10^7 galaxies” or “≥ ten million galaxies.”
- **[OpenAI_methodology/P4-N9/MINOR]**: P4-N9. Fig. 8 caption mixes current-null results with legacy rendering commentary - Location: Fig. 8 caption (Page 10) - Issue: The caption both states the current canonical battery σ’s and references an “earlier rendering” with a different ℓ = 5 bar, which is extraneous in the archival paper. - Required fix: Keep the caption focused on the null used for the plotted error bars and remove mention o…
