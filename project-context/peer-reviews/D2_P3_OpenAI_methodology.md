# P3 D2 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=7c935f19 pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6999 chars)
**Wall time**: 475.7s

---

Production/D2 camera-ready visual check (rendered PDF)
- Overall: The visual issues flagged in D1 (squished tables, cramped/missing figures, equation/text overflow, colorbar/label overlap, dense abstract) appear resolved. All tables render full width and legibly; figures are present, sized appropriately, and their axis titles/legends are readable at print scale; equations do not overrun margins; no colorbar overlaps are visible; the abstract text wraps cleanly.
- No new regressions found: no figure/table overflows, no text into margins, no overlapping elements, no bad float placement, no half-blank pages, and no orphaned section headings.
- Minor visual nit: Table I’s footnotes are extremely long and dense; although they render, they push the limits of readability. Consider moving portions of those prose footnotes into the main text or an appendix, keeping only the key legend markers under the table.

Referee report (methodology/statistics)

Scope and standard: PRD methods review focused on statistical validity, derivation chains, dimensional analysis, internal arithmetic, and error propagation. I audited the abstract and conclusions against the body text, recomputed all checkable ratios and sigmas, and examined tables/figures for consistency.

Findings

ESSENTIAL

P3-E1 — Data availability placeholders and non-final release language
- Location: Data availability (page 23); also Abstract (page 1).
- Problem: The manuscript contains non-final placeholders and future-tense promises: “will be publicly released with the arXiv posting,” and “A Zenodo DOI will be minted at submission and cited here in place of this sentence (DOI inserted at submission).” No DOI is given. Multiple internal run-paths and manifest file names are cited as if public but depend on a not-yet-public repository state.
- Required fix: Provide a permanent DOI (Zenodo or equivalent) for the exact frozen dataset and model weights used in the paper; include a release tag/commit hash for the code repository; replace all future-tense release language and placeholders with final, citable links. If the public release is not ready, remove strong reproducibility claims and defer release to a companion data paper; PRD acceptance requires stable provenance.

P3-E2 — eROSITA axis irreproducibility vs. rate presentation
- Location: Section III E (pages 10–12), Table I row for eROSITA (page 7), Abstract (page 1).
- Problem: The paper states that the eROSITA per-object SBigAE score axis is irreproducible (after testing 16 monotone rescalings), and releases a membership list only. Despite this, Table I presents a numeric “Rate 0.03%” and the abstract lists “298 … ≈ top 0.03%” in a way that can be mistaken for an empirical anomaly frequency. Footnotes try to qualify this, but the table and abstract still read as a measured rate.
- Required fix: Remove the numeric rate from Table I for eROSITA and replace with “— (fixed-count membership list; no reproducible score axis)” or an equivalent unambiguous label. In the abstract, explicitly say “n = 298 fixed-count membership list (membership-only tier; no reproducible per-object score axis)” and avoid implying a measured rate (“≈ top 0.03%” can remain only if it is clearly labeled as a rank cap, not a frequency). This is necessary to prevent misinterpretation.

P3-E3 — Normalization fitted on full sample, not training-split: missing robustness for NEOWISE and Gaia
- Location: Section II B, tabular-survey preprocessing (pages 3–4).
- Problem: For tabular surveys, scalers were fit on the full sample rather than the training split. An eROSITA robustness check is provided (top-298 overlap J=0.76; Spearman ρ=0.94), but analogous checks for NEOWISE and Gaia are “queued.” This affects anomaly scores because per-feature scaling changes the MSE weights and can reorder tails.
- Required fix: Provide the same “training-split-only scaler” robustness check for NEOWISE and Gaia used in this paper. At minimum, report top-1% Jaccard overlaps and rank correlations against the production runs. If infeasible, re-train NEOWISE and Gaia with train-only scalers and update counts/overlaps accordingly. Without these, the tabular results lack a key reproducibility control.

P3-E4 — Internal audit artifacts and run-paths embedded in the main text
- Location: Multiple pages (e.g., pages 3–5, 7–8, 11–12, 15–16, 23–25) citing internal paths like pipelines/p3_anomaly_engine/... and JSON filenames.
- Problem: The main text relies heavily on internal run manifests and pathnames as load-bearing evidence. PRD articles must be self-contained. These audit artifacts belong in a supplementary data release or a formal Supplemental Material, not in-line throughout the narrative.
- Required fix: Move all internal run-path references and JSON artifact names to a single consolidated “Reproducibility and run manifests” appendix or Supplemental Material, with a short pointer in the main text. Preserve the detail, but remove in-line path lists from the body. Cite only stable DOIs/commit hashes and high-level filenames in-text.

P3-E5 — Planck top-200 selection scored on training+validation set
- Location: Section III F (pages 11–12).
- Problem: The Planck native convolutional autoencoder scores the full 2×10^5-patch bank including the training patches; the released top-200 is not held-out. The authors argue against memorization via an enrichment toward validation patches (48/200 in val; binomial p ~ 4×10^-4), but the correct protocol for anomaly evaluation is to score held-out data.
- Required fix: Provide a top-200 list constructed from validation-only patches and report the overlap with the published list (e.g., “validation-only top-200 overlaps the full-bank top-200 by X/Y”). If the overlap is high, include that metric and keep the current list with the caveat; if the overlap is low, publish the validation-only set as the canonical Planck tier.

MAJOR

P3-M1 — Gate thresholds are heuristic; no pre-registration or power analysis
- Location: Section II D (page 5) and Section VI D(ii) (page 21–22).
- Problem: The validation gate thresholds (val-loss ≤ 0.30; injection-recovery ≥ 50% at 5σ; Jaccard ≥ 0.70/0.50) are heuristic. The manuscript states they are “heuristic engineering thresholds” without power calculations. For a methods paper, readers need to understand the risk of false PASS/FAIL classification.
- Required fix: Provide justification for these thresholds (e.g., sensitivity analyses showing conclusions are insensitive to moderate changes), or at least a table scanning alternative thresholds with unchanged pass/fail outcomes for each survey. Clarify any gate(s) that would flip under stricter cuts (you note SDSS 64% vs 50% is marginal), and explain the scientific impact if flipped.

P3-M2 — Mixed radii in SIMBAD unmatched headline and figure
- Location: Section IV A and Figure 6 (pages 13–14).
- Problem: Per-survey unmatched fractions use 5″, but the pooled “aggregate 58.8%” uses 3″. While the text explains this, the figure labels do not specify radii for each bar and can mislead.
- Required fix: Standardize the radius (preferably 5″) across all reported SIMBAD unmatched fractions, or annotate each bar in Figure 6 with the radius used and include an inset panel showing the sensitivity of the pooled fraction to 3″ vs 5″. Ensure the legend/caption explicitly flags the mismatch to avoid reader confusion.

P3-M3 — Single-architecture dependence on DESI for load-bearing conclusions
- Location: Throughout DESI analysis (pages 5–9; 17–19).
- Problem: DESI is the anchor survey; claims rely on a single deterministic autoencoder. You do provide k-fold and OOD Jaccard tests, which is commendable, but there is no independent algorithmic confirmation (e.g., VAE, IF on latent, one-class SVM). For a methods paper with ambitious scale claims, the ranking’s model dependence should be quantified.
- Required fix: Add an independent detector cross-check on a stratified DESI slice (e.g., IF or VAE on the same 128-d latent) and report top-1% overlaps and Spearman ρ; or, if infeasible, explicitly caveat in the abstract and conclusions that DESI’s rankings are single-architecture-derived and state the measured fold/OOD stability along with their limitations.

P3-M4 — eROSITA “top-5” SIF/raw table vs score irreproducibility
- Location: Table IV (page 12).
- Problem: You correctly omit the irreproducible SBigAE values, but the row header “First five entries of the released top-298 … with SIF,raw” can be misread as implying the IF/raw axis governs the top-298. It does not.
- Required fix: Amend the table caption to explicitly say: “Ranking is by the committed raw BigAE reconstruction score; SIF,raw is provided only for cross-validation mapping and did not determine selection.” Also add the exact raw-score threshold used (3.4119) in the caption for clarity.

P3-M5 — Excessive in-text repository paths impair readability (editorial)
- Location: Multiple across pages.
- Problem: Besides reproducibility, the sheer volume of pathnames breaks reading flow.
- Required fix: Centralize in an appendix/Supplement as in P3-E4 and refer succinctly from the main text.

MINOR

P3-n1 — Abstract claim alignment and caveats
- Location: Abstract (pages 1–2).
- Problem: The abstract is careful, but two places should add explicit caveats already present in the body:
  - The 269,317 “catalog-grade” tier includes the 200 Planck patches; the strictly point-source subset is 269,117. You state both in different spots; keep both together once.
  - The “σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98]” line should carry the “positivity-respecting form” caveat in brief, and that the central is a convex-mapping artifact pending higher S/N (you do say “noise-driven forecast” later; bring that clarity up).
- Required fix: Add a parenthetical “(central value from convex mapping; appropriate summary is the [3.92, 8.98] envelope; no detection)” in the abstract sentence.

P3-n2 — Length and organization
- Location: Whole paper (29 pages).
- Problem: The paper is long for the claimed contributions; much operational detail could move to Supplemental Material to improve readability.
- Required fix: Target ≤ 22 pages for the main text by moving path/manifests, some extended footnote prose under Table I, and the computational throughput appendix to Supplemental, keeping only essential methods and validated results in the main text.

P3-n3 — Notation hygiene
- Location: Eq. (1) (page 4) and surrounding text.
- Problem: Minor typesetting: repeated carets (xˆ) and summation limits “X N i=1” can be cleaned for clarity.
- Required fix: Standardize notation (e.g., \hat{x}) and summation as ∑_{i=1}^N.

P3-n4 — Figure 6 label clarity
- Location: Figure 6 (page 14).
- Problem: The asterisk next to LAMOST is explained in the caption body but not keyed next to the bar.
- Required fix: Add a legend entry “* training-bias artifact” inside the figure or a panel note so the asterisk is unambiguous.

P3-n5 — Minor rounding consistency
- Location: Various (e.g., “≈ 0.9×” for 2,468/2,685 = 0.919).
- Required fix: Where simple ratios are given, use consistent rounding (e.g., 0.92×) or state “~0.9×” explicitly as approximate.

NITS (cosmetic)

P3-N1 — Hyphenation consistency: “re-score/rescore,” “cross-transfer/crosstransfer”
- Location: Throughout.
- Fix: Standardize terminology.

P3-N2 — Table I caption length
- Location: Page 7–8.
- Fix: Consider splitting footnotes into a short in-table legend and moving elaboration to main text/appendix.

Arithmetic and internal consistency checks (spot-audits)
- DESI anomaly rate: 195,829/22,504,897 = 0.870% (matches 0.87%).
- DESI vs Liang et al.: 195,829/2,685 ≈ 72.95 (~73×), science-class-restricted 2,468/2,685 ≈ 0.92× (reported ~0.9×).
- Cross-survey dedup: input sum 388,493; collapsed 10,213; unique 378,280; compression 10,213/388,493 ≈ 2.63% (matches).
- Catalog-grade vs exploratory split: 378,280 − 269,317 = 108,963 (LAMOST-only uniques), consistent with 113,342 − 4,379 = 108,963.
- NEOWISE polar-cap fraction: 17/436 = 3.90%; two 10° caps cover 1 − cos(10°) ≈ 1.52%; ratio ≈ 2.57× (reported 2.6×).
- SIMBAD false-match at 5″: π(5″)^2 × 3×10^-5 arcsec^-2 ≈ 2.36×10^-3 per source; ×195,829 ≈ 462 false matches (reported “∼460”).
- Multi-tracer Fisher: F0 = 1/(8.98)^2 ≈ 0.01239; with c=0.0747 and α=0.19: 1/σ^2 ≈ 0.01509 → σ ≈ 8.14. Envelope computed consistently.
- NANOGrav γ shift: (3.0−2.567)/0.382 ≈ 1.13σ; (4.33−2.567)/0.382 ≈ 4.61σ (matches).

Effect-size qualifications
- Where χ^2 uniformity is quoted, a Cramér’s V is provided (≈ 0.0064) with proper caveats about selection functions — good.
- Comparability warnings between σ(fNL) forecasts and PTA γ are present — good; keep them wherever the two are juxtaposed.

Bibliography spot-check
- Cited works and years appear plausible; ensure final arXiv IDs correspond to the cited claims on acceptance.

## Summary recommendation
MAJOR REVISIONS

The manuscript is ambitious and methodologically careful in many respects (cross-validation gates, extensive caveats), and most arithmetic checks out. However, PRD acceptance requires stronger reproducibility and presentation hygiene: (i) remove all release placeholders and provide final DOIs/commits; (ii) prevent misinterpretation of the eROSITA “rate” by removing the numeric rate and emphasizing membership-only; (iii) supply the missing train-only-scaler robustness checks for NEOWISE and Gaia; (iv) provide a held-out-only Planck top-200 overlap or adopt a held-out list; and (v) move internal run-manifest pathnames to supplemental material. Addressing these will bring the work to PRD standards without changing the scientific thrust. The remaining items are important but can be handled in the same revision.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW ADDITIONAL FINDINGS (fresh-eyes audit)

ESSENTIAL

P3-E6 — Planck “rate” mixes denominators; fixed-count selection not labeled consistently
- Location: Table I (row “Planck CMB”), caption note ♢, Section III F, Abstract.
- Problem: Table I shows Planck “Rate 1.00%” using Ntotal = 20,000 (cross-transfer patch bank), but the released tier is the top-200 of a 2×10^5 native bank (0.10%). The caption note explains this, yet the table still presents 1.00% as if it were a measured rate. This mixes denominators and invites misinterpretation when scanning the table.
- Required fix: Replace the “1.00%” entry with an unambiguous fixed-count label, e.g., “— (fixed-count 200 patches; 200/20,000 in cross-transfer bank; 200/200,000 in native bank)” or split the cell into “200/20,000 (baseline), 200/200,000 (native)”. Also mirror this fixed-count language in the Abstract to avoid implying a data-driven frequency.

MAJOR

P3-M6 — NEOWISE pre-mask vs post-mask counts are mixed across table/text; SIMBAD denominator unclear
- Location: Table I (NEOWISE row), Table I caption (†), Section III H, Path-C totals and sums in Table I caption.
- Problem: The NEOWISE row lists Nanom = 436 (top-1%), but the Path-C pipeline retains 419 after the ecliptic-pole mask and uses 419 in the Path-C sums (388,493). Presenting 436 in the table while summing with 419 in the totals is double-bookkeeping that can confuse readers. It is also unclear whether the 45% SIMBAD-unmatched figure is computed on 436 or 419.
- Required fix: Show both numbers explicitly as “436 selected, 419 retained after mask (96.1%)” in Table I, and state the SIMBAD-unmatched percentage on the retained set (or provide both). Alternatively, add a separate “Retained” column for all surveys where masking or QA removes entries.

P3-M7 — “84% ultra-cool dwarfs” in SDSS cross-transfer set lacks quantitative backing and conflicts with Table III taxonomy labels
- Location: Section III C (paragraph beginning “UMAP/HDBSCAN clustering...”), Fig. 4 caption, Table III.
- Problem: The text and Fig. 4 caption assert that ∼84% of the SDSS cross-transfer anomalies are ultra-cool dwarfs (M7–T2), but Table III’s category counts do not include a “cool dwarf” class and instead list “Uncategorized” (52.7%) and “NIR excess/high-z” (33.0%), which do not transparently sum to “84% cool dwarfs.” The mapping from HDBSCAN clusters to physical classes is not quantified in the text.
- Required fix: Provide a numeric confusion/association table between HDBSCAN clusters and the physical labels (including the cluster-wise counts that sum to “84%”), or soften the claim to a qualitative statement. At minimum, report the fraction of the sample assigned to the “cool dwarf” cluster(s) and how those clusters were labeled from spectra.

P3-M8 — Anomaly-score vs SNR independence claim is based on a non-random, stratified sample
- Location: Section III A (last paragraph on SNR correlation).
- Problem: The paper states ρ = −0.03 (p = 0.12) on a deliberately stratified, log-uniform-in-SNR subsample of N = 2,670 and then uses this to argue the effect size is negligible. Because the design is not a random sample of the production population, the p-value is not interpretable as a population test, and the result may not reflect the behavior in the full catalog.
- Required fix: Repeat the analysis on a true random subsample (or multiple bootstrap subsamples) of the production DESI catalog and report the distribution of ρ and p across draws. Alternatively, compute the correlation on the full dataset using scalable estimators and report the effect size with a precision interval. If infeasible, explicitly caveat that no population-level test has been performed and remove any inference beyond “in this stratified test, the effect was small.”

MINOR

P3-n6 — Cramér’s V expression mis-typed; off-by-one in (k−1)
- Location: Section IV B (first paragraph).
- Problem: The text writes “Cramér’s V = √(χ2/(N·(k−1))) = 376,713/(378,280 × 24,047) ≈ 0.0064.” The numeric value 0.0064 corresponds to the square root of the ratio, but the square root is dropped in the numeric substitution line. Also, just above, dof is reported as 24,048, implying k−1 = 24,048 rather than 24,047.
- Required fix: Correct the displayed algebra to include the square root in the numeric substitution and use a consistent (k−1) matching the stated dof.

P3-n7 — Planck injection-recovery threshold reference unclear
- Location: Section III F; Fig. 10 caption.
- Problem: For Planck, the 100% recovery at 5σ is stated, but it is not explicit in-text whether the recovery criterion uses the same “99th-percentile clean-MSE threshold” used elsewhere for spectral/tabular surveys. Readers may assume a shared criterion across panels in Fig. 10.
- Required fix: Add a one-sentence clarification in Section III F or the Fig. 10 caption explicitly stating the decision threshold used for Planck (e.g., “recovered if per-patch MSE exceeded the native 99th-percentile clean threshold”).

P3-n8 — Table IV (eROSITA top-5) lacks the raw-score threshold in the table body
- Location: Table IV.
- Problem: The text (Sec. III E) mentions the committed raw-score rank-298 threshold 3.4119, but the table itself omits it. Including this would help readers reconcile selection without hunting in the prose.
- Required fix: Add “Raw-score rank-298 threshold = 3.4119” to the Table IV caption or a footnote.

P3-n9 — NEOWISE top anomaly figure vs text: clarify whether the SIMBAD-unmatched status is pre- or post-mask
- Location: Fig. 5 caption, Section III H.
- Problem: The figure notes “no prior SIMBAD entry within 5′′,” but it is not stated whether this status is computed on the pre-mask selection (436) or the retained post-mask set (419). Small, but consistent bookkeeping matters given the mask discussion.
- Required fix: Add “computed on the retained post-mask sample” (or specify otherwise) to Fig. 5 caption.

NITS (cosmetic)

P3-N3 — Cramér’s V symbol formatting
- Location: Section IV B.
- Fix: Use a consistent math font for V and ensure the radical covers the entire fraction to avoid ambiguity.

P3-N4 — Table I clarity for fixed-count tiers
- Location: Table I.
- Fix: Add a compact legend marker (e.g., “FC”) next to Planck, Gaia, NEOWISE counts with a legend “FC = fixed-count/top-percentile selection; not a measured anomaly frequency,” so readers do not need to parse a long caption to understand the rate cells.

Explanation
The initial review did not catch (i) the denominator inconsistency for the Planck “rate,” (ii) the NEOWISE pre-/post-mask count mismatch in Table I versus totals, (iii) the unsupported “84% cool dwarfs” quantification in SDSS relative to Table III’s taxonomy, (iv) the reliance on a non-random stratified sample for the SNR-independence claim, and (v) a minor algebraic slip in the Cramér’s V display. All other earlier essential/major issues remain, but the items above require additional clarification or minor analysis before PRD acceptance.