# P4 R40conf — v3 native-PDF cross-vendor SYNTHESIS

**Reviewers**: Claude_brutal, Gemini_cosmology, Grok_brutal, OpenAI_methodology, Perplexity_citations

## ⛔ ROUND DEGRADED — reviewer leg(s) FAILED: Claude_brutal
Failed legs are API errors, NOT zero-finding clean reviews. This round
MUST NOT count toward any clean-round counter; re-run after the failure
(e.g. API credit top-up) is resolved.
**Total findings (across all reviewers)**: 31
**Distinct consensus groups**: 10

## Per-reviewer finding counts

| Reviewer | ESSENTIAL | MAJOR | MINOR | NIT |
|----------|-----------|-------|-------|-----|
| Claude_brutal | 0 | 0 | 0 | 0 |
| Gemini_cosmology | 0 | 0 | 0 | 0 |
| Grok_brutal | 2 | 3 | 0 | 2 |
| OpenAI_methodology | 6 | 6 | 10 | 2 |
| Perplexity_citations | 0 | 0 | 0 | 0 |

---

## Consensus-grouped findings (most reviewers first)

### `sigma_mixing` — ESSENTIAL — **CONSENSUS** (2 reviewers)

Reviewers: Grok_brutal, OpenAI_methodology

- **[Grok_brutal/P4-E2/ESSENTIAL]**: **P4-E2** (ESSENTIAL)   Abstract, page 1, and Sec. IV C, page 7   Problem: The abstract states the real-space dipole is “consistent with null” at +0.41σ while simultaneously highlighting a +3.64σ MASTER residual. The body correctly notes these σ values are “not directly comparable,” but the abstract does not carry this explicit qualifier. A reader scanning only the abstract receives an inconsistent impression of detection significance.   Required fix: Add the sentence “(All σ values are estimator-specific and not directly comparable across null constructions)” to the abstract.
- **[OpenAI_methodology/P4-E5/ESSENTIAL]**: P4-E5 — Abstract and Conclusions, pp. 1, 14 Problem: Several σ values from distinct null procedures are juxtaposed. While many caveats are present, in the abstract some pairs are not accompanied by a plain p‑value or amplitude, potentially inviting misinterpretation (e.g., “+3.64σ … ≈1.9σ Gaussian‑equivalent” without p in the abstract). Required fix: For every σ quoted in the abstract and conclusions, add the associated one‑sided rank p (or make explicit that Gaussian‑equivalent σ is derived from that p) and the effect size (Adip or C1 value). Retain the “not directly comparable” language. Thi…

### `audit_artifact` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P4-E2/ESSENTIAL]**: P4-E2 — Throughout body (e.g., Secs. II.B p. 3; III.B p. 4; IV.B–E pp. 5–12; Appendices A–E pp. 15–21) Problem: Pervasive inclusion of internal pipeline paths, round/version tags, and audit‑artifact filenames in the main text (e.g., “pipelines/p2_chirality/.../c17_item13_training_semantics.json”, “c12_r24conf_local_batch.json”, “post‑R29”, “c9b”, “canonical_provenance/…”, “seed 42”). PRD does not accept internal bookkeeping in the body; it also creates brittleness and violates the instruction to avoid review‑log/round‑metadata in the PDF. Required fix: Move all file‑path mentions, round/versio…

### `companion` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P4-E4/ESSENTIAL]**: P4-E4 — Appendix B.d (QC flip reconstruction), p. 17 Problem: The public Parquet release contains 2.9% of rows where “recovered flip probability falls outside [0,1] by up to 0.09,” stemming from a raw/equivariant pass mismatch. Although a QC flag is provided, leaving inconsistent columns in the main data product is a reproducibility hazard; tables/figures in the paper rely on derived quantities from these columns. Required fix: Regenerate the public release so all probability columns are internally consistent (no [0,1] violations). Alternatively, remove the inconsistent reconstructed‑flip colu…

### `length` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: Grok_brutal

- **[Grok_brutal/P4-E1/ESSENTIAL]**: **P4-E1** (ESSENTIAL)   Section: Entire manuscript (23 pages + appendices)   Problem: The paper is substantially over-length for its actual scientific payload (a carefully executed null result plus a well-quantified but expected classifier leakage diagnostic). PRD expects concise, high-impact contributions; 23 pages of text plus 11 figures and 11 tables far exceeds what is required to present the null dipole, the 99.32 % leakage fraction, and the +3.64σ residual.   Required fix: Condense to ≤14 pages (main text + figures). Move all but the three most critical diagnostic figures and Tables I–II…

### `n_mc_500,audit_artifact` — MAJOR — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P4-M1/MAJOR]**: P4-M1 — Multiple sections (IV.C–D pp. 7–12; Appendix A pp. 15–17) Problem: Mixed MC sizes (NMC = 500 vs 10,000) are used for closely related diagnostic claims, yet σ is reported with two‑decimal precision for the N = 500 streams (e.g., “+3.64σ”, “+4.84σ”). Finite‑MC uncertainty on z is not provided; some headline numbers (e.g., +3.64σ) are later superseded by 10k runs (+7.93σ) under a different field convention, which complicates interpretation. Required fix: Adopt a single high‑statistics null (≥10k permutations) for all load‑bearing diagnostic σ’s in the paper, or accompany each σ with its M…

### `shamir_citation` — MAJOR — _single-reviewer_ (1 reviewer)

Reviewers: Grok_brutal

- **[Grok_brutal/P4-M2/MAJOR]**: **P4-M2** (MAJOR)   Sec. V A, page 12, and abstract   Problem: The factor-of-6–12 discrepancy with Shamir et al. is attributed to bias correction, yet no matched-footprint reanalysis of the Shamir catalog under the present pipeline is performed. The claim therefore rests on an untested extrapolation.   Required fix: Either perform the matched reanalysis or qualify the statement as an inference rather than a demonstrated result.

### `table_ii` — MAJOR — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P4-M2/MAJOR]**: P4-M2 — Table II (Global CW fraction), p. 5 Problem: The Catalog B (calibrated) row reports fCW = 0.504 ± 0.0003 and z = +14.6 but does not state Nspiral for Catalog B. The quoted uncertainty implies N ≈ 2.8–3.3M but should be explicit. Required fix: Add a column with Nspiral for each tier (A/B/C) or a footnote with N_B, and verify that the stated σ matches σ = sqrt(f(1−f)/Nspiral). If the tier sample sizes differ (as they likely do), remark on implications for the z-comparison across tiers.
- **[OpenAI_methodology/P4-M6/MAJOR]**: P4-M6 — C1 amplitude/normalization mismatch across sections (Appendix A.c vs. Table III; footprint/field mixing) - Appendix A.c states: “monopole subtraction reduces decoupled C1 at ℓ = 1 from 2.30×10−5 to 1.51×10−5 … and increases σ from +1.85 to +3.64 (the canonical-mask number).” - Table III’s canonical-unapodized, MASTER-decoupled ℓ = 1 shows Cdata = 7.27×10−6, but that block explicitly uses the half‑scaled field fCW−0.5 = Ap/2. If 1.51×10−5 is in Ap units, the corresponding Ap/2 value should be 3.78×10−6 (a factor of 4), not 7.27×10−6 (≈×2.08). - The paragraph in Appendix A.c also mixes f…
- **[OpenAI_methodology/P4-m6/MINOR]**: P4-m6 — Small but systematic z–rounding inconsistencies (Table II; Sec. IV.B) - Using the displayed uncertainties, Tier A: (0.507879−0.5)/0.000274 = 28.77σ (paper: 28.72); Tier C: (0.497353−0.5)/0.000279 = −9.49σ (paper: −9.47). You note “computed from the unrounded fraction,” but the visible discrepancy exceeds simple rounding of the shown σ. Either report z computed from the displayed numbers or include a note that both numerator and denominator come from higher precision and provide those in Supplementary.
- **[OpenAI_methodology/P4-m10/MINOR]**: P4-m10 — Figure/number consistency note (Fig. 9 vs. Sec. IV.C; Table III) - Fig. 9 caption says the panel annotation uses the canonical “obs. σ ≈ +7.28,” but also mentions the injection artifact’s internal background yields 7.21. Elsewhere, Table III reports +7.31 from 10k permutations. The values are all compatible but scattered across conventions. Consider harmonizing the single “observed” number used in captions with a single agreed null (and move alternates to Supplement).  NO OTHER NEW ISSUES FOUND IN CLASSES B, C, D, E, F, G, H, I, J BEYOND THOSE ALREADY REPORTED - I rechecked figure–cap…

### `table_iv` — MAJOR — _single-reviewer_ (1 reviewer)

Reviewers: Grok_brutal

- **[Grok_brutal/P4-M1/MAJOR]**: **P4-M1** (MAJOR)   Sec. IV D and Table IV, page 11   Problem: The 99.32 % monopole-mask leakage claim is computed from a 500-realization binomial generative null. The quoted residual (+1.69σ) after subtraction is presented without an accompanying effect-size statement (fractional power remaining or Cramér’s V). The reader cannot judge whether the residual is practically negligible.   Required fix: Report the post-subtraction fractional power explicitly and state the practical significance.

### `sigma_mixing,duplicate_phrase` — NIT — _single-reviewer_ (1 reviewer)

Reviewers: Grok_brutal

- **[Grok_brutal/P4-N2/NIT]**: **P4-N2** (MINOR)   Table I, footnote a, page 5   Problem: The canonical f_sky = 0.4801 value is stated for the high-confidence subsample while the main analysis uses f_sky = 0.49005. The two numbers are close but not identical; the difference is never quantified.   Required fix: State the numerical difference and confirm it does not affect any quoted σ at the reported precision.  **P4-NIT1** (NIT)   Multiple locations (e.g., page 1, page 4)   Problem: Occasional typographic artifacts (“canonical canonical-mask”, repeated “Note: the σ values…” phrasing) that survived proofreading.   Required f…

## Other findings (18)

- **[Grok_brutal/P4-M3/MAJOR]**: **P4-M3** (MAJOR)   Appendix D, page 19   Problem: The eight-anchor systematic battery is presented as exhaustive, but the joint nuisance-marginalized WLS fit (Table X) still yields a 14.7× inflation of the dipole amplitude uncertainty when spatial coherence is respected. This indicates the “clean 1.7 % dipole” exclusion is sensitive to the precise covariance model; the paper does not propagate th…
- **[Grok_brutal/P4-N1/NIT]**: **P4-N1** (MINOR)   Fig. 4 caption and Sec. IV C   Problem: The color scale of the Mollweide map is given in Aₚ units, but the accompanying text repeatedly quotes f_CW-deviation units without reminding the reader that Aₚ = 2(f_CW – ½). Minor risk of misreading.   Required fix: Add “(Aₚ = 2(f_CW – ½))” once in the figure caption.
- **[OpenAI_methodology/P4-E1/ESSENTIAL]**: P4-E1 — Sec. II.B (Training Labels), p. 3 Problem: Inconsistent training-set augmentation arithmetic. Text states 25,790 source images; after horizontal‑flip augmentation of the training split the “combined pool is 26,616 (80/20 split: ntrain = 21,293, nval = 5,323). The 826‑image difference … arises entirely from horizontal‑flip augmentation applied to the training split only.” This is inconsiste…
- **[OpenAI_methodology/P4-E3/ESSENTIAL]**: P4-E3 — Data Availability, pp. 21–22 Problem: No persistent DOI for the released catalog/code/model at submission time (“A persistent archival DOI … has not yet been minted”). PRD requires a frozen, citable release for reproducibility. Required fix: Mint DOIs (e.g., Zenodo) for: (i) the exact catalog used (all three tiers), (ii) model weights, and (iii) analysis scripts producing the reported numb…
- **[OpenAI_methodology/P4-M3/MAJOR]**: P4-M3 — Appendix C.e (Per‑imaging‑leg multiplicity), p. 19 Problem: The statement “a Gaussian Bonferroni‑15 estimate would underpredict this family‑wise p by ∼250×” is quantitative but unsupported by numbers. Required fix: Provide the exact Bonferroni p estimate used, the empirical family‑wise p from the max‑statistic null, and the ratio; or remove the “∼250×” claim.
- **[OpenAI_methodology/P4-M4/MAJOR]**: P4-M4 — Diagnostic σ presentation for heavy‑tailed nulls (Sec. IV.D, Appendix A; multiple pages) Problem: The paper rightly emphasizes that the permutation null is heavy‑tailed and that “moment‑z” and Gaussian‑equivalent σ need not agree. However, many panels foreground moment‑z alone. Required fix: For every low‑ℓ diagnostic where non‑Gaussian nulls are used, report rank p (with finite‑N resoluti…
- **[OpenAI_methodology/P4-M5/MAJOR]**: P4-M5 — Length vs. contribution (entire manuscript) Problem: The body interleaves primary results with extensive audit‑artifact prose, making the paper longer and harder to parse than necessary for the stated contribution. Required fix: Move detailed artifact paths, additional mask sweeps, and secondary diagnostics (e.g., many of the Appendix C/E stratifications) to Supplement. A tight main paper …
- **[OpenAI_methodology/P4-m1/MINOR]**: P4-m1 — Appendix D.g, p. 20 Problem: Typo “z ≈ −18.1.23” (stray “23” footnote marker). Required fix: Correct to “z ≈ −18.1” and place the footnote marker properly.
- **[OpenAI_methodology/P4-m2/MINOR]**: P4-m2 — Abstract phrasing, p. 1 Problem: “+3.64σ moment‑z, ≈1.9σ Gaussian‑equivalent” is potentially confusing without a p‑value; the parenthetical note later in the abstract is long. Required fix: Add “(one‑sided p ≈ 0.03)” next to the 3.64σ diagnostic in the abstract, or streamline to “3.64σ (p ≈ 0.03; diagnostic only)”.
- **[OpenAI_methodology/P4-m3/MINOR]**: P4-m3 — Notational consistency, various Problem: Occasional spacing/diacritics inconsistencies (“C 2 2 ◦”, “ˆ zˆ”). Required fix: Standardize to “C2 apodization with 2° length” and consistent vector hats.
- **[OpenAI_methodology/P4-m4/MINOR]**: P4-m4 — Claim of “largest chirality‑labeled catalog,” p. 2 and Conclusions p. 14 Problem: Novelty claim is plausible (3.2M spirals vs 1.95M in Jia et al.). Tighten wording to “largest to date to our knowledge; 3.2M spirals vs. ~1.95M in CE‑ResNet (Jia et al. 2023).” Ensure the comparator in [7] indeed refers to spirals with chirality labels, not total galaxies.
- **[OpenAI_methodology/P4-m5/MINOR]**: P4-m5 — Reporting precision, various tables Problem: Mixed significant‑figure usage (e.g., fractions with 6 decimals vs. percentages to 3 s.f.; Cℓ “×10^6” vs raw units). Required fix: Adopt a uniform reporting precision consistent with MC/statistical uncertainty.
- **[OpenAI_methodology/P4-n1/NIT]**: P4-n1 — Minor grammar/linebreak artifacts in URLs and names (Data Availability, pp. 21–22). Required fix: Avoid hyphenating URLs; ensure copy‑and‑paste works.
- **[OpenAI_methodology/P4-n2/NIT]**: P4-n2 — Figure/caption cross‑references Problem: Some captions include long parentheticals about null conventions without directly pointing to the exact subsection. Required fix: Add explicit “see Sec. III A for null‑procedure definitions.”  Abstract‑last drift sweep - All primary abstract claims (N = 8.47M; Nspiral = 3.201M; HC real‑space dipole +0.41σ, p = 0.31; WLS template exclusion z ≈ −18 fo…
- **[OpenAI_methodology/P4-E6/ESSENTIAL]**: P4-E6 — Canonical-mask “in-mask spiral count” inconsistency (Sec. IV.C vs. Appendix D.h) - The body states that, for the unthresholded test, “all 3,200,420 in-mask equivariant spirals; the remaining 740 of the catalog’s 3,201,160 spirals lie in pixels below the Nspiral(p) ≥ 10 canonical-mask threshold” (Sec. IV.C). - Appendix D.h’s WLS mask-equivalence audit table, however, reports “In-mask spiral…
- **[OpenAI_methodology/P4-m7/MINOR]**: P4-m7 — Table VII header/labeling ambiguity (fsky vs feff_sky) - The table header reads “fsky,” but several rows are effective sky fractions feff_sky = ⟨W⟩^2/⟨W^2⟩ (weighted/apodized), while others are raw geometric pixel fractions (binary masks). You do explain the distinction in text, but the table heading is misleading. - Required fix: Rename the rightmost column to “sky fraction (fsky or feff_…
- **[OpenAI_methodology/P4-m8/MINOR]**: P4-m8 — Null‑naming inconsistency for the primary real‑space dipole (Sec. IV.C vs Table I) - The text calls the null “per‑pixel isotropic permutation” while Table I labels it “iso. boot.” They appear to be the same procedure. Standardize the naming (“per‑pixel permutation null”) across the paper to avoid confusion, and point to the subsection where it is defined.
- **[OpenAI_methodology/P4-m9/MINOR]**: P4-m9 — Appendix A.c wording mixes footprints in one sentence - “On the Nall ≥ 1 footprint … increases σ … (the canonical‑mask number).” This conflates the Nall ≥ 1 footprint (used for the apodized MASTER diagnostic) with the canonical mask. Please split and make each footprint’s numbers self‑contained.
