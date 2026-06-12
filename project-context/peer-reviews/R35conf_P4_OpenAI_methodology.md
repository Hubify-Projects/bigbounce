# P4 R35conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v178.pdf` md5=0275961b pages=22
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6960 chars)
**Wall time**: 422.1s

---

Referee report (Methodology/Statistics) — PRD submission P4

I read the full 22-page manuscript carefully, including all figures, tables, equations, captions, appendices, and the abstract. I recomputed all checkable percentages, ratios, and most σ-values from the numbers provided. The work is technically ambitious and the internal cross-checking is unusually extensive. However, there are multiple essential issues that must be corrected before this can meet PRD standards, particularly around (i) clarity and consistency of statistical reporting across distinct null procedures, (ii) look-elsewhere corrections, (iii) excessive inclusion of internal-audit prose, paths and versioning in the main text and abstract, and (iv) moving load-bearing quantitative claims now referenced only by repository artifacts into the paper itself (or a formal Supplemental Material) with sufficient detail to be independently read and reviewed.

Below I list all findings. Each entry includes an ID, location, the specific problem, and the required fix. Classifications: ESSENTIAL (must fix to be publishable), MAJOR (significant revision), MINOR (address but paper can proceed), NIT (cosmetic).

ESSENTIAL

P4-E1 — Abstract (page 1)
Problem: The abstract contains version-history and audit language: “An earlier version of this paper reported a MASTER ℓ = 1 null on a subsample mask … that result is withdrawn (Appendix A) …”
Required fix: Remove version-history/audit narrative from the abstract. If retained at all, this belongs in a short provenance note in an Appendix or in a captioned footnote in the main text. The abstract must describe only the current, audited analysis and its results.

P4-E2 — Abstract (page 1)
Problem: Heterogeneous σ values are juxtaposed without an explicit “not directly comparable” qualifier at the point of juxtaposition: “post-MASTER harmonic diagnostics carry … residuals (+3.64σ … canonical mask; +7.28σ, apodized footprint)”. These are based on different masks, decoupling conventions, weight maps, and nulls.
Required fix: Add an explicit clause in the abstract at the juxtaposition itself stating these σ-values arise from different null procedures/masks/weights and are not directly comparable. Alternatively, report only one canonical value per channel in the abstract.

P4-E3 — Throughout main text and appendices (multiple pages, e.g., pp. 2–5, 7–16, 18–21)
Problem: The manuscript contains extensive internal-audit prose: local file paths (e.g., “pipelines/p2_chirality/...”), seeds, commit hashes, “artifact” labels, “earlier text misprinted...”, “post-R29”, etc. PRD style does not allow repository pathnames and internal audit logs to be embedded throughout the scientific narrative.
Required fix: Move all path-level “artifact” pointers, audit-log commentary, prior-run corrections, and version-control details to a formal Supplemental Material or a Code/Data Availability Appendix (one centralized section). Retain in the main text only succinct, publication-grade descriptions of the methods, with enough quantitative detail to validate key claims. Remove version IDs from the title block (“v1.0.178”).

P4-E4 — Appendix C, Hemisphere look-elsewhere (page 18; also referenced on pp. 4, 12)
Problem: Inconsistent LEE handling. You report a direct-MC look-elsewhere pLEE ≤ 10−4 for the hemisphere max-statistic (this already corrects for directional trials), and then additionally apply Bonferroni/BH corrections over the same grid, “downgrading” to < 1σ. This double-corrects the same trial set and leaves the reader unsure which significance is operative.
Required fix: Adopt a single, principled look-elsewhere treatment for the hemisphere scan (the direct-MC max-statistic null is appropriate). Report only that corrected p-value/σ. If you wish to show Bonferroni/BH as heuristics, present them explicitly as cross-checks and do not replace the direct-MC result with an extra penalty.

P4-E5 — Conclusions (page 14, item a) and main text reference (Sec. VII and IV.C–D)
Problem: “Harmonic-channel completeness (end-to-end) … P(≥ 3σ) = 0.92 at Ap = 0.5% and ≥ 0.999 at Ap ≥ 0.75%; Ap = 1.7% yields median z ≈ 68–218 …” These load-bearing completeness claims are not documented in the paper (no figure/table with Ninj, null definition, axis protocol, band decoupling setup, or recovery curves). They are only referenced by internal “artifact” tags.
Required fix: Add a figure or table in the paper (or Supplemental Material) showing the MASTER-channel injection/recovery results with full configuration: estimator definition (field, weight, mask, apodization), null procedure, NMC,null and Ninj per amplitude, axis protocol, and recovered z distributions. Without this, the completeness claim cannot be assessed.

P4-E6 — Data Availability (page 21) and title block (page 1)
Problem: Inconsistent and non-final provenance. The PDF is dated “v1.0.178”; Data Availability pins “commit 53b41d12 (v1.0.175) … a Zenodo DOI … has not yet been minted”. PRD requires stable, citable releases at acceptance.
Required fix: Provide a final, frozen release of code, catalog, and model weights with a persistent DOI (e.g., Zenodo) that matches the analysis in the accepted manuscript. Remove version strings from the title page; retain a single “Dated: …” line per PRD style. Ensure URLs are typeset correctly without mid-word hyphen breaks.

P4-E7 — Abstract and Conclusions (pages 1, 14)
Problem: Side-by-side reporting of +3.64σ (500-MC, canonical-mask single-mode) and +7.93σ (10^4 permutations, canonical-unapodized block) for the same general channel is confusing. The paper alternately cites +3.64σ (for continuity with a leakage analysis) and +7.93σ (for high-statistics diagnostics).
Required fix: Identify one canonical configuration and report that as the headline diagnostic number in the abstract and conclusions; relegate alternative configurations to the body/appendix, with a clear mapping. If you keep both, explicitly state at each use why both are shown and that they are not independent detections.

P4-E8 — Throughout (e.g., p. 4 Sec. III.B; p. 15 Appendix A.d)
Problem: The manuscript repeatedly includes editorial audit language in the body (“earlier version… withdrawn… manuscript revision v1.0.76… audit artifacts are listed…”).
Required fix: Remove all editorial history from the main narrative. A brief, neutral provenance note in an appendix is acceptable. The paper must read as a self-contained, final account.

MAJOR

P4-M1 — Appendix C: Hemisphere analysis (page 18)
Problem: Ambiguity about one-sided vs two-sided conventions across tests. The text mixes one-sided rank p (default) and two-sided statements in various places without always restating the convention at point-of-use.
Required fix: Standardize and clearly label the sidedness at every reported p or σ, especially in global scans (hemisphere, RA quadrants). Prefer two-sided for absolute-value max stats unless a signed alternative is explicitly motivated.

P4-M2 — Appendix E.a (page 20)
Problem: “65.7% of b/a < 0.3 edge-on objects receive CW/CCW labels rather than not spiral” is a strong quantitative claim without a presented sample size, selection procedure, or uncertainty.
Required fix: Provide the exact counts (Ntotal, Ncw+ccw, Nns), the axis-ratio source and cut definition, and the binomial uncertainty. If this is based on an external cross-match, describe it; otherwise remove the precise percentage.

P4-M3 — Appendix C (page 18) and IV.E (page 12)
Problem: Several diagnostic claims refer to results “available in the repository” but are not tabulated in the paper: RA-quadrant σ values, confidence-bin breakdowns, per-leg × confidence-bin maxima, etc.
Required fix: Add a compact table summarizing these diagnostic σ values (with N per bin, null type, and sidedness), or move them to a formal Supplemental Material with a clear pointer.

P4-M4 — Conclusions (page 14, item b) and Sec. IV.D (pp. 9–11)
Problem: The amplitude-level statement “reproduces 99.32% of the observed pre-MASTER pseudo-Cℓ=1 power” is central. It is robustly computed, but the presentation mixes pre-/post-MASTER diagnostics and different field normalizations across sections and tables. This invites confusion.
Required fix: Present a single “leakage map” figure or a compact table that, in one place, lists for the same catalog/mask: pre-MASTER C1 data and monopole-only null mean±σ; post-MASTER-decoupled C1 data and monopole-only null mean±σ; label-shuffle null mean±σ. State explicitly the field conventions and units for each row.

P4-M5 — Sec. VI.A.b (pages 12–13)
Problem: The dilution factor g = 2a − 1 ≈ 0.398 is invoked without even a one-line derivation or a reference for symmetric CW↔CCW misclassification.
Required fix: Add a brief derivation in a footnote/appendix, or cite a standard reference for this mapping, and state the assumptions (symmetric errors, no triage). Clarify how triage to “not spiral” affects the mapping.

P4-M6 — Sec. VII.a (page 14)
Problem: Very large reported z (≈ 68–218 at Ap = 1.7%) from MASTER-channel injections are plausible but currently unsupported by in-paper distributions.
Required fix: Add (or move from artifacts to Supplemental Material) at least one representative recovered-z distribution plot for an injected Ap (e.g., 0.75%, 1.7%) showing the null distribution, the recovered distribution, and the fraction exceeding 3σ.

P4-M7 — Sec. IV.C (pages 7–8), Appendix A (pages 15–16)
Problem: The paper uses two slightly different MASTER estimators (single-ℓ decoupling vs. inclusion in a 39-band scheme). This is mentioned, but the mapping and the reason for the numerical differences are not crystal clear to a standalone reader.
Required fix: Add one clarifying sentence in Sec. IV.C explicitly contrasting the two decoupling schemes and why they yield slightly different C1 amplitudes for the same data.

P4-M8 — General clarity, presentation length
Problem: While reproducibility is laudable, the current narrative is weighed down by extensive implementation minutiae, making the core scientific results harder to follow. For PRD, much of this belongs in Supplemental Material.
Required fix: Move code-level and conditioning/audit details (e.g., matrix condition numbers, seed listings, pathnames) to Supplemental Material. Aim to reduce the main text to ≤ 18 pages without loss of scientific content.

MINOR

P4-n1 — Sec. IV.B (page 5), Table II
Problem: Catalog-B row: cw/(cw+ccw) = 0.504 ± 0.0003, Dev +14.6σ. Nspiral(B) is not given. While the σ is plausible, the denominator should be stated explicitly for transparency.
Required fix: Add Nspiral for Catalog B or a footnote stating it equals the Catalog A spiral count (if true) so readers can verify the σ.

P4-n2 — Appendix A.a (page 15)
Problem: Typesetting inconsistencies around the apodization label (“C 2 2 ◦”, “C2 2◦”, “C
2 2
◦”). This is confusing.
Required fix: Standardize to “C2 apodization, 2° length” (or the NaMaster notation in a consistent style) throughout.

P4-n3 — Table III caption (page 11)
Problem: Units and normalization could be clearer. One block is “×10^6” with Ap field and another is the half-scaled fCW − 0.5 field. Although you state z and rank-p are invariant under this scaling, the table would benefit from a brief parenthetical reminding readers of the exact amplitude unit per block.
Required fix: Add a parenthetical in the caption stating the amplitude units for each block and that z/p are invariant to this constant scaling.

P4-n4 — Table IX (page 19)
Problem: Minor typo: “ˆ zˆ” in “dipole ẑ” column header/content.
Required fix: Fix the stray hat.

P4-n5 — URLs (page 21)
Problem: Line breaks insert hyphens/spaces into URLs (e.g., “dataset s/bamfai/galaxy- chirality- catalog”).
Required fix: Use proper URL breaking or \url{} to ensure clickable, unbroken links in the final PDF.

P4-n6 — Sec. IV.B (page 5)
Problem: The phrase “percentages truncated rather than rounded” is correct, but consider adding the exact integer counts next to any percentage where a truncation choice may surprise readers.
Required fix: No change required for correctness, but a reminder to include integer counts where possible.

NIT

P4-N1 — Style (multiple pages)
Problem: Frequent use of “systematics-attributed” and similar qualifiers is fine, but consider avoiding overuse to improve readability.
Required fix: Editorial pass.

P4-N2 — Acknowledgments (page 21)
Problem: “AI tool usage” sentence is acceptable but optional for PRD; defer to journal policy.
Required fix: None mandatory.

Arithmetic and internal-consistency checks I performed

- Counts: NCW + NCCW + NNS = 8,474,531 (ok). Spiral count 3,201,160 (ok). Parent removal 8,474,688 − 157 = 8,474,531 (ok).
- Global fCW (Catalog C): 1,592,107/3,201,160 = 0.497353; σbinomial ≈ 0.000279; dev −9.49σ (consistent with table).
- Catalog A fCW: 0.507879; σ ≈ 0.000274; dev +28.7σ (consistent).
- Asymmetry conversion: A = 2(fCW − 0.5): +0.788% → +1.576%, −0.265% → −0.529% (consistent).
- Fisher floor: σ(A) = √(3/N) → 9.7×10−4 (N = 3.20116×10^6) and 1.78×10−3 (N = 9.49584×10^5) (both match).
- WLS bootstrap exclusion: (0.00455 − 0.034)/0.00163 = −18.1 (ok).
- Monopole-leakage pre-MASTER reproduction: (1.6961 − 1.6846)×10−2 over 0.0068×10−2 → z = +1.69 (ok).
- Hemisphere max |A|: (3.484 − 1.693)/0.405 ×10−3 → z = +4.42 (ok).
- MASTER apodized ℓ = 1 (10k): (24.74 − 1.93)/3.12 → z = +7.31; canonical unapodized: (7.27 − 0.57)/0.84 → z ≈ +7.98 (tabulated 7.93; rounding ok).
- Monopole subtraction shift of ⟨A⟩mask,gw = −0.005294 matches 2(fCW − 0.5) with fCW = 0.497353.

Effect-size context and estimator-specificity

- The manuscript generally provides effect sizes alongside σ (e.g., real-space Adip ≈ 4.4×10−3, AUL95 = 6.8×10−3), and repeatedly cautions that σ from different nulls are not cross-comparable. This is good practice. However, per P4-E2, the abstract needs to carry this caveat exactly at the point of juxtaposition.

Stand-alone reader test

- With the ESSENTIAL/MAJOR fixes above (especially moving repository-only quantitative claims into the paper or Supplemental Material), the paper will be self-contained. As submitted, several key completeness and diagnostic assertions are not independently checkable from the PDF.

Length

- The main scientific content can be conveyed in ≤ 18 pages. I recommend moving implementation-level audit material to Supplemental Material.

## Summary recommendation
MAJOR REVISIONS

The core methodology and many numerical claims are sound and well cross-checked, and the null result is convincingly supported by the primary real-space estimator and the WLS bootstrap exclusion. However, the manuscript in its present form does not meet PRD standards for presentation and statistical clarity. It mixes heterogeneous σ-values without sufficient caveats in the abstract, includes extensive internal-audit prose and version history in the main text and abstract, presents key completeness claims only via repository artifacts rather than in-paper figures/tables, and contains inconsistent look-elsewhere correction logic that must be cleaned up. Addressing the ESSENTIAL/MAJOR items above, consolidating the diagnostic reporting, and moving audit minutiae to Supplemental Material will make the paper suitable for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eye pass)

ESSENTIAL

P4-E9 — Sec. V.A vs Sec. IV.B (pages 12 vs 5–6)
Problem: In Sec. V.A you state “our maximum regional asymmetry is 0.32%.” Earlier (Sec. IV.B) you report per-region fCW deviations up to 0.49% (equal-area full sample) and 0.56% (HC subsample), and 0.46% in equal-count slabs. These numbers do not reconcile with the claimed 0.32% “maximum regional asymmetry,” which is undefined and appears inconsistent with your own regional maxima.
Required fix: Define precisely what “regional asymmetry” refers to (region geometry, statistic, units), identify the dataset/tier/threshold used, and reconcile it quantitatively with the larger per-region deviations already reported. If 0.32% refers to a different partition or estimator, say so and provide the corresponding numbers for that partition.

MAJOR

P4-M9 — Sec. II.B, Appendix B (pages 2–3, 16)
Problem: Training-set accounting is unclear/internally inconsistent. You state 25,790 source images; after “flip augmentation of the training split” the “combined pool is 26,616,” with the 826-image difference attributed to “augmented duplicates.” If augmentation is applied to the training split only and on-the-fly (as implied later), the persistent dataset size should not increase by 826. As written, it is ambiguous whether flips are materialized into the manifest, and why only +826 images appear rather than +ntrain.
Required fix: Clarify exactly how augmentation is implemented and counted (on-the-fly vs duplicated entries), and provide the precise per-split counts before/after augmentation. If only training is augmented, explicitly show how 26,616 arises from 25,790 and the 80/20 split.

P4-M10 — Sec. IV.B (page 6)
Problem: The statement that p = fglobal_CW vs p = 0.5 realizations yield “a 0.39σ shift in the standard error of the difference; N = 500” lacks definition of the test statistic and σ (which variance and which standard error). As written, it is under-specified.
Required fix: Specify exactly how the 0.39σ was computed: define the statistic (difference of means), the estimator of its standard error (pooled or bootstrap; formula), and report the two means with their uncertainties.

P4-M11 — Abstract/Sec. IV.C (pages 1, 7–8)
Problem: You label AUL95 (the 95th percentile of the null Adipole distribution) an “upper limit,” then correctly note it has “no frequentist coverage guarantee.” Calling it an “upper limit” is misleading in a PRD context and risks reader confusion.
Required fix: Rename AUL95 throughout to “95th-percentile null threshold” or equivalent, and avoid the term “upper limit” unless you provide a proper confidence-interval construction.

P4-M12 — Table III caption, units (page 11)
Problem: The caption refers to the “Ap field, ×10−6 sr scale.” For a dimensionless scalar field under standard NaMaster/HEALPix normalization, Cℓ is dimensionless (variance per multipole), not “per sr.” The unit statement is likely incorrect and risks confusion given your two field normalizations in the table.
Required fix: Correct the units. State explicitly that Cb values are dimensionless (under your chosen normalization), and keep the “×10^6” purely as a display scaling factor. Retain the clear note that z and rank-p are invariant under the constant field rescaling between Ap and fCW−0.5.

P4-M13 — Sec. IV.E vs Sec. IV.C (pages 12 vs 7–8)
Problem: In Sec. IV.E you cite a confidence-binned dipole result for [0.5,0.6) peq, then say “cutting to peq > 0.6 gives −0.03σ under the same confidence-stratified dipole estimator,” while Sec. IV.C reports +0.41σ for the peq > 0.6 primary estimator. The two use different statistics/nulls, but this is not stated here and is confusing.
Required fix: Add one clarifying sentence in Sec. IV.E explicitly stating that the confidence-binned dipole statistic and null differ from the primary HC real-space dipole, and that these numbers are not directly comparable.

MINOR

P4-n7 — Sec. VII.a, Appendix A/Table III usage (pages 14–16)
Problem: Several MASTER-channel summaries and the bar plot in Fig. 8 mix “pseudo-Cℓ” (pre-MASTER) language with post-MASTER-decoupled significances in the same narrative flow. While you do caution, the figure/caption/body interplay remains easy to misread.
Required fix: Add a one-line tag in Fig. 8 caption indicating explicitly whether the displayed bars are pre- or post-MASTER, and cross-reference the exact section where the post-MASTER single-ℓ result (+3.64σ or +7.93σ in canonical variants) is computed.

P4-n8 — Sec. III.D (page 4)
Problem: “flip-swap correlation = 1.000 by construction” is slightly overstated given finite-precision implementation and your own later note that reconstructed flips can fall outside [0,1] for 2.9% of rows due to raw/eq pass mismatch.
Required fix: Soften to “1.000 to numerical precision under the implemented TTA protocol” and point to the QC note that flags rare raw/equivariant pass mismatches (already in Appendix B).

P4-n9 — Sec. VII.c and Appendix D (pages 14, 18–20)
Problem: Some diagnostic nulls use N = 200 permutations (e.g., the canonical 200-MC “multi-null battery”), which is marginal for stable tail σ estimates and invites run-to-run variability; this is hinted at in the text.
Required fix: Add a brief sentence acknowledging the sampling limitation at N = 200 for tail σ estimates and pointing to the higher-statistics 10k runs where available, or increase N for the battery in a revised version.

P4-n10 — Table I, row labeling (page 5)
Problem: Row (vi) “monopole+mask null … +1.69” leaves the statistic unlabeled in the column header; only the main text reveals it is a z-value.
Required fix: Append “(z)” or “(σ)” in the “Reported statistic” cell for that row for immediate clarity.

P4-n11 — Appendix D.h (page 20)
Problem: rℓ definition and use are careful, but when you quote rℓ=2 = −0.65 you rely on both auto-powers being positive. The text says rℓ is “quoted only where both auto-powers are positive,” but this caveat isn’t restated at the rℓ=2 value.
Required fix: Add a parenthetical “(both auto-powers positive at ℓ=2)” alongside the quoted rℓ=2.

P4-n12 — Sec. IV.C.b (page 8)
Problem: The weight-map sweep summary is clear, but the phrase “±1σ level” is ambiguous because each variant has its own σnull. 
Required fix: Rephrase to “changes the recovered z by O(1) across weight choices,” or specify the actual z-range across weights.

NO OTHER DISCREPANCIES IN ARITHMETIC OR DIMENSIONAL CONSISTENCY WERE FOUND
- All recomputed ratios, counts, and σ-values I spot-checked beyond those in my first report remain numerically consistent within rounding.
- Equations (2)–(4) are dimensionally consistent; Ap is dimensionless; σ(A) derivation at A = 0 is correct for the stated Fisher idealization.

With these additions, the earlier ESSENTIAL/MAJOR items plus the new inconsistencies above should bring the manuscript to PRD standards for statistical rigor and presentation clarity.