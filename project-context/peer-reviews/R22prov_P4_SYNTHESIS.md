# P4 R22prov — v3 native-PDF cross-vendor SYNTHESIS

**Reviewers**: Claude_brutal, Gemini_cosmology, Grok_brutal, META_REVIEW, OpenAI_methodology, Perplexity_citations
**Total findings (across all reviewers)**: 68
**Distinct consensus groups**: 14

## Per-reviewer finding counts

| Reviewer | ESSENTIAL | MAJOR | MINOR | NIT |
|----------|-----------|-------|-------|-----|
| Claude_brutal | 0 | 0 | 0 | 0 |
| Gemini_cosmology | 2 | 1 | 4 | 2 |
| Grok_brutal | 4 | 4 | 1 | 5 |
| META_REVIEW | 3 | 7 | 6 | 0 |
| OpenAI_methodology | 10 | 6 | 8 | 5 |
| Perplexity_citations | 0 | 0 | 0 | 0 |

---

## Consensus-grouped findings (most reviewers first)

### `table_ii` — ESSENTIAL — **CONSENSUS** (4 reviewers)

Reviewers: Gemini_cosmology, Grok_brutal, META_REVIEW, OpenAI_methodology

- **[Gemini_cosmology/P4-m2/MINOR]**: **P4-m2: Ambiguity in Table II Deviation Column** *   **Section/Page:** Table II (p. 5) *   **Problem:** The column "Dev. (σ)" in Table II appears to list the absolute value of the deviation from 0.5000 in units of σ, but this is not stated. For Catalog C, the excess is negative (-0.26%), but the deviation is listed as a positive 9.5σ. *   **Required Fix:** Clarify the column header, for example, to "|fcw - 0.5|/σ", or add a footnote explaining that the absolute deviation is reported.
- **[Grok_brutal/P4-m1/MINOR]**: **P4-m1 (MINOR)**   Figure 7 caption claims the right-hand (Catalog C) map is “Catalog C (equivariant)”. The color bar is labeled in units of the per-pixel CW fraction, yet the body text (§IV B) and Table II report the same quantity only as a sky-averaged monopole. No per-pixel color-bar calibration is supplied, so the map cannot be read quantitatively against the quoted 0.4974 global fraction.
- **[META_REVIEW/P4-META-M5/MAJOR]**: P4-META-M5 Severity: MAJOR Section/page: Table III p. 7 and caption; surrounding text §IV C/D Why others missed it: Focus stayed on σ magnitudes, not dof accounting. Problem: Table III reports “Joint χ²/dof (38 bandpowers) = 161.2/38,” but the table only shows 1 single-ℓ entry plus 5 bandpowers. The provenance of “38 bandpowers” is neither shown nor referenced (binning scheme, ℓ ranges, mask/weights). Required fix: Either (a) list all 38 bandpowers (or provide them in a supplementary table) with their ℓ ranges and masks/weights, or (b) remove the χ² line from Table III and place it in an appen…
- **[META_REVIEW/P4-META-M7/MAJOR]**: P4-META-M7 Severity: MAJOR Section/page: §IV C–D and Table III p. 7; Appendix A(a) p. 11 Why others missed it: Everyone focused on null comparability, not the spectral-noise model. Problem: No shot-noise (Nℓ) debias is applied to the Ap auto-spectrum; yet absolute Cℓ amplitudes (×10−6 sr) are quoted. Using per-pixel fractions with variable denominators (Nspiral or Nall) induces pixel-dependent sampling noise that biases the auto-spectrum upward. While label-shuffle nulls can provide a significance, the reported Cℓ values are not interpretable as noise‑debiased amplitudes. Required fix: Provide…
- **[OpenAI_methodology/P4-E2/ESSENTIAL]**: P4-E2  Fig. 2 caption vs. Table II (p. 5)   Caption states a CW-fraction shift of “+2.05 % (A) to −0.53 % (C)”.   Table II gives +0.79 % (A) and −0.26 % (C) when the same definition cw/(cw+ccw) is used.  The two numbers cannot both be correct.   Required fix: Recompute and reconcile the percentages; state explicitly which denominator (all galaxies vs. spirals only) is being used in each place.
- **[OpenAI_methodology/P4-E8/ESSENTIAL]**: P4-E8  Inconsistent quoted significance for the same “ℓ = 1” quantity   • Table III (p. 7) gives “+7.28 σ” (apodised footprint, Wp = Nall).   • Appendix D (p. 12) states “σℓ=1 = +3.63”.   Both passages call the value “the ℓ = 1 excess on the canonical mask”, yet differ by a factor ≈2. The manuscript never labels them as separate estimators (apodised vs. binary, weighted vs. un-weighted) and the reader cannot tell which number underpins later arguments.   Required fix: Use unique names for the two estimators, place them in one comparison table, and explain explicitly why their σ’s differ.
- **[OpenAI_methodology/P4-m7/MINOR]**: P4-m7  Appendix D gives “σℓ=2 = +4.73”, whereas Table III shows +6.10 σ for the same (ℓ = 2) band-power. Clarify whether one value is canonical and the other apodised.

### `sigma_mixing` — ESSENTIAL — **CONSENSUS** (3 reviewers)

Reviewers: Gemini_cosmology, Grok_brutal, OpenAI_methodology

- **[Gemini_cosmology/P4-m1/MINOR]**: **P4-m1: Clarification of σ-value Comparability in Table I** *   **Section/Page:** Table I (p. 4) *   **Problem:** The abstract and main text correctly warn that σ values from different null procedures are not directly comparable. However, Table I, which is the central summary of all key results, presents multiple σ values side-by-side without this warning in its caption. *   **Required Fix:** Add a sentence to the caption of Table I, such as: "Note: Significance (σ) values are defined relative to their respective nulls (listed in the 'Null' column) and are not directly comparable to each othe…
- **[Grok_brutal/P4-E2/ESSENTIAL]**: **P4-E2 (ESSENTIAL)**   Abstract (page 1) and Table I (page 4) juxtapose multiple σ values (0.43σ, 3.64σ, 7.28σ, etc.) from distinct null procedures. Although a general disclaimer exists, it is not repeated at every load-bearing comparison in the abstract or §IV C–D. PRD requires explicit “not directly comparable” qualification at each such juxtaposition. Required fix: insert the qualifier at every instance or remove cross-estimator numerical comparisons from the abstract.
- **[Grok_brutal/P4-N3/NIT]**: **P4-N3 (NIT)**   Several axis labels in Figures 4, 5, 7 use mixed capitalization (“Equatorial”, “log10”) and non-standard color-bar ranges. Required fix: enforce consistent style.  **Summary recommendation**   REJECT  The manuscript contains multiple instances of internal review language that must be removed before any scientific evaluation can proceed (E1). Even after that excision, the abstract mis-represents the raw versus post-processed results (E3), cross-estimator σ values are presented without the required comparability caveats at every use (E2), and the paper is substantially over-len…
- **[OpenAI_methodology/P4-E7/ESSENTIAL]**: P4-E7  Internal consistency of σ mapping (Table I & body)   Table I distinguishes seven null procedures, but the main text occasionally places σ from two different nulls in the same sentence without the mandatory caveat (e.g. p. 7 bottom, p. 9 top).   Required fix: At every juxtaposition of σ from different nulls, add the explicit clause “σ values are relative to their own null distributions and are not directly comparable”.
- **[OpenAI_methodology/P4-m2/MINOR]**: P4-m2  Table I caption: “its two σ values are against the global per-galaxy label-shuffle and depth-stratified nulls respectively” → please repeat that explanation in the table body.

### `audit_artifact` — ESSENTIAL — **CONSENSUS** (2 reviewers)

Reviewers: Grok_brutal, OpenAI_methodology

- **[Grok_brutal/P4-E1/ESSENTIAL]**: **P4-E1 (ESSENTIAL)**   Page 1 (abstract), lines ~15–20: “Withdrawn note: versions ≤1.0.165 of this paper reported a −0.122σ MASTER ℓ=1 null on a putative ‘strict-superset subsample mask’ … a provenance audit found that result was computed on a synthetic-footprint catalog and it is withdrawn”.   This is internal review-log / version-history prose. Required fix: delete every sentence referencing prior versions, withdrawn results, provenance audits, or round identifiers. No such language belongs in a submitted manuscript.
- **[OpenAI_methodology/P4-E1/ESSENTIAL]**: P4-E1  Abstract & throughout (pp. 1, 6, 10)   The text contains version-history and retraction bookkeeping that belongs in a “Note added” on arXiv, not in the body of a peer-review paper: • “Withdrawal note: versions ≤1.0.165 …”   • “A June 2026 provenance audit found … the result is therefore withdrawn.”   • Dozens of “Artifact:” and internal path strings.   Required fix: Remove all version-tracking prose, internal file-path comments, and audit log references from the published text.  Summarise any necessary provenance in a single concise sentence in App. A or the Data-availability section.

### `future_date` — ESSENTIAL — **CONSENSUS** (2 reviewers)

Reviewers: Gemini_cosmology, Grok_brutal

- **[Gemini_cosmology/P4-E1/ESSENTIAL]**: **P4-E1: Placeholder Date** *   **Section/Page:** Title page (p. 1), Appendix A (p. 11) *   **Problem:** The paper is dated "(Dated: June 2026)". Appendix A refers to a "June 2026 provenance audit". This future date is highly irregular and appears to be a placeholder. Scientific papers must be dated corresponding to their submission or revision date. *   **Required Fix:** Replace all instances of "June 2026" with the actual date of submission/revision.
- **[Grok_brutal/P4-N1/NIT]**: **P4-N1 (MINOR)**   Page 1 states “Dated: June 2026”. A submission date in the future is an artifact. Required fix: remove or correct.
- **[Grok_brutal/P4-N4/NIT]**: **P4-N4 (NIT)**   Page 2, “Dated: June 2026” appears in the author block. A submission date 18 months in the future is an obvious artifact and must be removed.

### `nmap_weighting` — MAJOR — **CONSENSUS** (2 reviewers)

Reviewers: Grok_brutal, META_REVIEW

- **[Grok_brutal/P4-N2/NIT]**: **P4-N2 (MINOR)**   Table I caption and footnote 1 contain inconsistent wording on whether Nmap weighted includes NS galaxies. The numerical value 8 474 531 appears without an explicit statement that it equals Σ Wp. Required fix: make the definition unambiguous.
- **[META_REVIEW/P4-META-M6/MAJOR]**: P4-META-M6 Severity: MAJOR Section/page: Table I row (iv) p. 4; Appendix A(c) p. 11 Why others missed it: They commented on effective fsky, not the sum-of-weights inconsistency. Problem: Row (iv) (apodized MASTER diagnostic) quotes Nmap weighted = 8,474,531 while also stating that a C2 2° apodization is applied. With apodization, Σp Wp should no longer equal the total object count; quoting the un-apodized sum side-by-side with apodized results is misleading. Required fix: Report both (i) the geometric fsky of the binary footprint, (ii) the effective fsky after apodization and weighting (⟨W⟩²/⟨…

### `n_mc_500,sigma_mixing` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P4-E5/ESSENTIAL]**: P4-E5  MASTER ℓ = 1 diagnostic significance (pp. 6–7)   The +7.28 σ value is obtained from only NMC = 500 label-shuffle realisations.  With 500 draws the sampling uncertainty of the standard deviation itself is ≈6 %.  A >7 σ claim is therefore unsupported.   Required fix: Either raise the MC count to ≥10 000 or quote the significance as a rank p-value (≤1/500 = 0.002, i.e. <3 σ) rather than a Gaussian σ.  Clarify that the result is entirely diagnostic and not used for cosmology.

### `table_ii,table_iv` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P4-E9/ESSENTIAL]**: P4-E9  Unit/normalisation mismatch between Tables III and IV   Table III quotes Cℓ in “×10⁻⁶ sr”, e.g. C₁ = 23.48 × 10⁻⁶.   Table IV lists a “Pre-MASTER pseudo-C(ℓ=1)ℓ” of 1.696 × 10⁻² with no units — 3 orders of magnitude larger than Table III despite purporting to be the same raw (pre-MASTER) spectrum. One table is clearly using an un-announced multiplicative factor.   Required fix: State units in Table IV, reconcile the scaling, and ensure both tables use the same convention.
- **[OpenAI_methodology/P4-M5/MAJOR]**: P4-M5  Drifting mask definitions (0.49005 / 0.491 / 0.494)   The same footprint is variously quoted as fsky = 0.49005 (Table IV), 0.491 (Table III caption), and 0.494 (Table I row (iv) and many places in the text). It is impossible to know which area each statistic uses.   Fix: Freeze one binary mask, quote its exact fsky once in §II, and propagate that single value everywhere; list any alternative masks in a separate table.

### `table_iv` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: META_REVIEW

- **[META_REVIEW/P4-META-E3/ESSENTIAL]**: P4-META-E3 Severity: ESSENTIAL Section/page: Abstract p. 1; §IV D p. 7; Table IV p. 8; Appendix C p. 12 Why others missed it: Prior reviews noted pLEE ambiguity but not the internal double counting. Problem: Hemisphere “look-elsewhere” significance is double-counted. The text reports a direct-MC look‑elsewhere pLEE ≤ 10−4 and then further applies Bonferroni/BH over ~650 directions, yielding “post-LEE significance < 1σ.” A direct max-statistic MC already incorporates the look-elsewhere scan; adding Bonferroni/BH constitutes a second, extraneous penalty. Compounding this, Table IV lists a pre‑LE…
- **[META_REVIEW/P4-META-m11/MINOR]**: P4-META-m11 Severity: MINOR Section/page: Table IV p. 8 vs Appendix C p. 12 Why others missed it: Hemispheric numbers appear in different places with different contexts. Problem: Hemisphere max-statistic inconsistencies: Table IV reports z = +4.42 for NSIDEdir = 8, while Appendix C states “maximum asymmetry 3.05σ” for the hemisphere scan. They are presented as the same diagnostic but differ by ~1.4σ. Required fix: Present both numbers in one place with exact definitions (grid, estimator, null, one‑ vs two‑sided), or replace one. A single, consistent hemisphere result should remain in the paper…

### `fisher_floor` — MAJOR — _single-reviewer_ (1 reviewer)

Reviewers: Grok_brutal

- **[Grok_brutal/P4-M4/MAJOR]**: **P4-M4 (MAJOR)**   §VI A states the Fisher Poisson floor at 3σ is “~0.29% full-amplitude (from σ(A/2)≈0.048%…)”. Direct recalculation from the binomial error on N_spiral=3,201,160 gives σ(f−0.5)=2.79×10^{-4}, hence σ_A=5.58×10^{-4} (0.0558%) if A≡2(f−0.5). The quoted 0.048% and 0.29% figures are therefore numerically inconsistent with the N_spiral value used everywhere else. Required fix: correct the arithmetic or define A explicitly.

### `length` — MAJOR — _single-reviewer_ (1 reviewer)

Reviewers: Grok_brutal

- **[Grok_brutal/P4-M1/MAJOR]**: **P4-M1 (MAJOR)**   The manuscript is 15 pages (plus appendices) for a null-result systematics paper. PRD cosmology methods papers reporting a non-detection are routinely expected to be ≤8–10 pages. The extensive diagnostic sections (§IV D–E, Appendices C–E) largely repeat the same conclusion (monopole-mask leakage). Required fix: condense to ≤10 pages or justify the length.

### `sigma_mixing,table_ii,table_ii_sigma_arithmetic` — MAJOR — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P4-M6/MAJOR]**: P4-M6  Discrepant σ in Table II   Using Table II numbers, (0.5079 – 0.5)/0.000279 = 28.3 σ for Catalog A, yet the table lists 28.8 σ. Either Nspiral differs from 3 201 160 or a rounding/typing error occurred. Similar 2–3 % discrepancies appear in the other rows.   Fix: Recompute Dev.(σ) from the listed counts, update the table, and certify that all σ values are internally consistent.  --------------------------------------------------------------------

### `table_ii,shamir_citation` — MAJOR — _single-reviewer_ (1 reviewer)

Reviewers: Grok_brutal

- **[Grok_brutal/P4-M2/MAJOR]**: **P4-M2 (MAJOR)**   Figure 4 (page 7) and the associated MASTER band-power table (Table III) show the ℓ=1 residual is +7.28σ on the apodized footprint, yet the text repeatedly labels it “non-headline” and “systematics-attributed.” No quantitative test demonstrates that the same pipeline would recover an injected cosmological dipole of the amplitude claimed by Shamir et al. (~1.7–3 %). Required fix: add an end-to-end injection-recovery test on the real DESI footprint that quantifies completeness versus the claimed prior signals.

### `duplicate_phrase` — MINOR — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P4-m4/MINOR]**: P4-m4  Duplicate phrasing: “canonical canonical-mask” (p. 7 line 3).

## Other findings (39)

- **[Gemini_cosmology/P4-E2/ESSENTIAL]**: **P4-E2: Conflicting Significance Metrics for Canonical-Mask Residual** *   **Section/Page:** Abstract (p. 1), Section VII.b (p. 10) *   **Problem:** The significance of the post-MASTER canonical-mask residual is presented in a confusing manner. The abstract states: "+3.64σ (z = Δ/σ_null moment-ratio; empirical rank p_mc = 0.030, i.e. ≈1.9σ Gaussian-equivalent)". This presents two different signif…
- **[Gemini_cosmology/P4-M1/MAJOR]**: **P4-M1: Scope and Interpretation of the Withdrawn Result** *   **Section/Page:** Abstract (p. 1), Appendix A (p. 11) *   **Problem:** The paper commendably withdraws a previous null result. The new result on the same analysis channel (apodized-footprint MASTER l=1) is a highly significant +7.28σ excess, which is now attributed to systematics. The abstract states the old result was on a "putative …
- **[Gemini_cosmology/P4-m3/MINOR]**: **P4-m3: Consistency of High-Confidence Sample Size** *   **Section/Page:** Abstract (p. 1), Table I (p. 4) *   **Problem:** The abstract states "471,049 high-confidence per-spiral after p_eq > 0.9". However, the "injection floor" estimator in Table I, which is the only result that appears to use this high-confidence (HC) sample, lists the sample size as "471,049 HC". It is not immediately clear w…
- **[Gemini_cosmology/P4-m4/MINOR]**: **P4-m4: Footnote 2 Clarity** *   **Section/Page:** Appendix E (p. 13) *   **Problem:** Footnote 2 is critical for understanding the robustness checks on high-confidence subsamples. It explains a subtle but important point about the "monopole-preserving" estimator. While the content is correct, its density makes it difficult to parse. *   **Required Fix:** Consider slightly rephrasing the footnote…
- **[Gemini_cosmology/P4-N1/NIT]**: **P4-N1: Awkward Phrasing in Falsification Criterion** *   **Section/Page:** Abstract (p. 1) *   **Problem:** The sentence "a future 5σ detection at A ~ 0.75% would be entirely consistent with the present non-detection (only 50% of injected A = 0.75% signals are recovered at 3σ under our null; a detection in the unrecovered half is not in tension with non-detection in the recovered half)" is convo…
- **[Gemini_cosmology/P4-N2/NIT]**: **P4-N2: Redundant Word in Abstract** *   **Section/Page:** Abstract (p. 1) *   **Problem:** The phrase "The MASTER-deconvolved pseudo-C_l channel on the patchy survey footprint is presented as a systematics diagnostic, not an independent cosmological null." is slightly redundant. *   **Required Fix:** Suggest simplifying to "The MASTER-deconvolved pseudo-C_l channel on the patchy survey footprint…
- **[Grok_brutal/P4-E3/ESSENTIAL]**: **P4-E3 (ESSENTIAL)**   Abstract claims “a null real-space chirality dipole” at +0.43σ (p=0.30) as the headline scientific result. The body (§IV C, page 6) shows this is obtained only after 2-fold TTA + MASTER deconvolution; the raw Catalog A dipole is 2.31σ. The abstract therefore mis-states what the pipeline actually measures before post-processing. Required fix: rewrite the abstract to state th…
- **[Grok_brutal/P4-M3/MAJOR]**: **P4-M3 (MAJOR)**   The falsification criterion (§I, page 2) is defined at A95≈1.5–2 % for a future 5σ detection. No calculation shows how this threshold maps onto the present survey’s effective number of independent modes after mask and depth weighting. Required fix: derive the numerical threshold from the survey’s mode count and mask power spectrum.
- **[Grok_brutal/P4-E4/ESSENTIAL]**: **P4-E4 (ESSENTIAL)**   Abstract and §IV C both quote the headline dipole as “+0.43σ (p=0.30)” from an isotropic bootstrap (N_MC=10,000). The body text never states the exact bootstrap realization count used for the p-value itself; the only N_MC=10,000 reference is to a different test. Required fix: either recompute and report the p-value from the stated 10,000 realizations or remove the parenthet…
- **[Grok_brutal/P4-N5/NIT]**: **P4-N5 (NIT)**   Table I row (v) lists “p_LEE ≤10^{-4}” while the caption states the null is “max-stat MC”. The two descriptions are not equivalent; the table entry is therefore ambiguous.  NO ADDITIONAL FINDINGS on dimensional consistency, internal cross-references, or appendix/main-text mismatch; those checks were clean. All new items above are arithmetic, caption-body, or presentation defects …
- **[META_REVIEW/P4-META-E1/ESSENTIAL]**: P4-META-E1 Severity: ESSENTIAL Section/page: Appendix A(a–b), pp. 10–11; Sec. IV D (and Abstract) Why others missed it: Everyone focused on σ inconsistencies but not on the MASTER algebra itself. Problem: The manuscript claims “MASTER mode-coupling deconvolution removes the leakage,” yet Appendix A(a) explicitly states that the MASTER mode-coupling matrix does NOT include ℓ = 0 on either the input…
- **[META_REVIEW/P4-META-E2/ESSENTIAL]**: P4-META-E2 Severity: ESSENTIAL Section/page: §II.B Training Labels, p. 3 Why others missed it: Reviewers focused on systematics, not book-keeping. Problem: The training-set composition does not add up. The text lists 6,637 (GZ1) + 17,153 (CE‑ResNet) + 2,000 (synthetic) = 25,790 images, but then states “The combined training set contains 26,636 images.” The 846-image discrepancy is unexplained. Req…
- **[META_REVIEW/P4-META-M4/MAJOR]**: P4-META-M4 Severity: MAJOR Section/page: §VI.A (Sensitivity), p. 9; Abstract p. 1; Table I row (vii) Why others missed it: They asked for more injections but not the estimator/sample/null mismatch. Problem: The quoted A50≈0.75% and A95≈1.5–2% thresholds come from injections on the high‑confidence (HC) subsample (N=471,049) under a per‑pixel label‑shuffle null, yet these thresholds are used to fram…
- **[META_REVIEW/P4-META-M8/MAJOR]**: P4-META-M8 Severity: MAJOR Section/page: §III C p. 3; Appendix B d. p. 11; §V.B p. 8 Why others missed it: The CE‑ResNet cross‑use was acknowledged but not stress‑tested. Problem: Potential footprint/systematics imprint via training labels is untested. 67.6% of training labels come from CE‑ResNet predictions on DESI DR8, i.e., drawn from the same survey footprint used for inference. If CE‑ResNet h…
- **[META_REVIEW/P4-META-M9/MAJOR]**: P4-META-M9 Severity: MAJOR Section/page: §IV C p. 6 vs §IV C/D and Appendix D/E Why others missed it: They noted mask mismatches generally, not this precise threshold inconsistency. Problem: The real‑space dipole uses pixels “containing > 10 spiral galaxies,” while the canonical‑mask MASTER analyses use Nspiral(p) ≥ 5. The threshold change is not justified and can alter sky coverage and dipole var…
- **[META_REVIEW/P4-META-M10/MAJOR]**: P4-META-M10 Severity: MAJOR Section/page: Abstract p. 1 (“pMC = 0.030, i.e. ≈1.9σ”); also §IV D Why others missed it: They asked to state sidedness but did not check the mapping numerically. Problem: The mapping p = 0.030 → “≈1.9σ Gaussian‑equivalent” is only true for a one‑sided conversion. Two‑sided p = 0.03 corresponds to ≈2.17σ. The paper never states sidedness here; the abstract thus understa…
- **[META_REVIEW/P4-META-m12/MINOR]**: P4-META-m12 Severity: MINOR Section/page: Appendix D(f) p. 13 (WLS fit) Why others missed it: The focus was on the final z-scores, not the regression design. Problem: Potential collinearity in the WLS template fit is not addressed (constant term + leg fractions + density and density²). Without reporting condition numbers, orthogonalization, or SVD/ridge handling, the quoted uncertainties and extre…
- **[META_REVIEW/P4-META-m13/MINOR]**: P4-META-m13 Severity: MINOR Section/page: Table I p. 4; Appendix A(c) p. 11 Why others missed it: They noted fsky presentation, but not the nomenclature drift. Problem: The notation “C2 2° apodization” is undefined and non-standard in PRD context. It is unclear whether this is a cosine‑squared roll‑off with a 2° apodization length, a Tukey window, or something else. Required fix: Define precisely …
- **[META_REVIEW/P4-META-m14/MINOR]**: P4-META-m14 Severity: MINOR Section/page: Data Availability p. 14 Why others missed it: They focused on length and clarity, not repository logistics. Problem: The catalog “release tag: v2026.04” and model link may not exist at review time (future-stamped), undermining immediate reproducibility. Required fix: Provide a permanent DOI (e.g., Zenodo) or a time‑stamped tag/commit hash that is already l…
- **[META_REVIEW/P4-META-m15/MINOR]**: P4-META-m15 Severity: MINOR Section/page: §IV C–D p. 6–7; Appendix A(a) p. 11 Why others missed it: Discussions centered on null types, not weighting biases. Problem: The “depth‑stratified null” permutes labels within Nall(p) deciles, preserving only the marginal depth distribution, not the joint spatial/depth structure. Given known leg‑dependent systematics, this null can be anti‑conservative (or…
- **[META_REVIEW/P4-META-m16/MINOR]**: P4-META-m16 Severity: MINOR Section/page: §III A p. 3; Appendix A(a) p. 11 Why others missed it: They flagged A-definition drift but not the impact on noise statistics. Problem: Two definitions of Ap are used (spiral‑denominator vs all‑galaxies denominator) with different shot‑noise properties, but the paper never quantifies the induced change in variance and effective fsky across estimators. Requ…
- **[OpenAI_methodology/P4-E3/ESSENTIAL]**: P4-E3  Real-space dipole (pp. 6 & 10)   Only the significance “+0.43 σ (p = 0.30)” is quoted.  The best-fit amplitude |A|, its 1 σ uncertainty, and the dipole direction (in Galactic or Equatorial coordinates) are not given, preventing reproduction.   Required fix: Provide the three Cartesian components or (A, l, b) with uncertainties and the exact estimator definition.
- **[OpenAI_methodology/P4-E4/ESSENTIAL]**: P4-E4  Template-fit exclusion (Table I row (ii) & App. D, p. 13)   The manuscript quotes “z ≈ −18” for ruling out a 1.7 % dipole but does not give (i) the fitted amplitude with its bootstrap error, (ii) the χ² or likelihood ratio, or (iii) the number of free nuisance parameters.   Required fix: Tabulate Abest, σboot, χ²/d.o.f. and make the exclusion criterion quantitative (e.g. p-value or Δχ²).
- **[OpenAI_methodology/P4-E6/ESSENTIAL]**: P4-E6  Mixed units for amplitudes (many places, e.g. p. 6 & App. D)   The manuscript alternates between “in fCW units”, “full-amplitude”, and “% asymmetry” without definition.   Required fix: Adopt one symbol (e.g. A≡(NCW−NCCW)/(NCW+NCCW)) throughout, state unambiguously whether a quoted percentage is 100 × A or 100 × A/2, and amend every occurrence.
- **[OpenAI_methodology/P4-M1/MAJOR]**: P4-M1  Method description of the isotropic bootstrap (p. 6)   The text does not state how the 10 000 “isotropic” realisations are generated: random sky rotations, latitude scrambles, or label permutations?  The dipole variance depends on the choice.   Fix: Describe the bootstrap algorithm in a numbered list and justify that it is unbiased.
- **[OpenAI_methodology/P4-M2/MAJOR]**: P4-M2  WLS block bootstrap (App. D, p. 13)   Only NSIDE = 8 blocks and Nboot = 1000 are mentioned.  No convergence check or block-size dependence study is shown.   Fix: Provide a plot or table demonstrating that σ(Adipole) is stable against doubling the block size and/or the number of bootstrap draws.
- **[OpenAI_methodology/P4-M3/MAJOR]**: P4-M3  Page length (15 pp)   For what is essentially a dipole null result, 15 typeset pages plus very long appendix-style footnotes is excessive.   Fix: Reduce to ≤10 journal pages by moving code-path discussion and catalogue minutiae to an external “extended data” document.
- **[OpenAI_methodology/P4-M4/MAJOR]**: P4-M4  Residual systematics attribution chain (Sec. IV D & App. D)   The dismissal of interpretation (i) relies on three qualitative diagnostics.  No quantitative goodness-of-fit to a “dipole-only” model is given.   Fix: Add a formal likelihood ratio or Δχ² test comparing the dipole-only model with the 9-template systematic model over the canonical mask.
- **[OpenAI_methodology/P4-m1/MINOR]**: P4-m1  Equation (2) (p. 3): missing “=0.5” prefactor formatting; typeset with clearer parentheses.
- **[OpenAI_methodology/P4-m3/MINOR]**: P4-m3  Footnote 1 (p. 6) contains a 16-line digression better placed in App. A.
- **[OpenAI_methodology/P4-m5/MINOR]**: P4-m5  Several references lack journal page numbers (e.g. Ref. [6]).
- **[OpenAI_methodology/P4-n1/NIT]**: P4-n1  PACS numbers obsolete; use “Physics Subject Headings” or omit.
- **[OpenAI_methodology/P4-n2/NIT]**: P4-n2  “flip-swap correlation = 1.000” – give the number of decimal places justified by the sample size.
- **[OpenAI_methodology/P4-n3/NIT]**: P4-n3  Avoid first-person plural “We urge all future studies” in a PRD methods paper.  -------------------------------------------------------------------- ## Summary recommendation
- **[OpenAI_methodology/P4-E10/ESSENTIAL]**: P4-E10  Sensitivity-floor calculation uses an undefined fsky   Section VI A cites “fsky = 0.46” when computing the Fisher floor, yet everywhere else the analysis footprint is 0.490–0.494. No mask at fsky = 0.46 is described.   Required fix: Specify which mask has fsky = 0.46 or correct the calculation; recompute the 0.29 % floor if the true fsky differs.  ------------------------------------------…
- **[OpenAI_methodology/P4-m6/MINOR]**: P4-m6  Table I row (iv) labels fsky = 0.494 but, per Appendix A, the effective sky fraction after depth-weighting is 0.452. Stating the binary-mask area in a weighted-spectrum row is misleading. Quote both the geometric and the effective fsky or adopt one consistently.
- **[OpenAI_methodology/P4-m8/MINOR]**: P4-m8  Figure 8 caption says the orange band is “500-MC monopole-only null”, but the legend in the panel labels it “Null expectation (1000 shuffles)”. The draw count must be stated consistently.  --------------------------------------------------------------------
- **[OpenAI_methodology/P4-n4/NIT]**: P4-n4  Table V lists r = 1.000 to three decimal places. Given 8.47 M samples, quote either 1.0000 ± 0.0002 or round to 1.00; three decimals look artificially precise.
- **[OpenAI_methodology/P4-n5/NIT]**: P4-n5  In Sect. III C: “Z2 and D4 to within |∆⟨pCW⟩|<0.0016” — the inequality sign is flipped in the next sentence (“argmax-CW-fraction shift (−1.35 %)”); restate both numbers with the same precision and inequality orientation.  -------------------------------------------------------------------- ## Brief rationale The additional inconsistencies above were uncovered by re-computing quoted values a…
