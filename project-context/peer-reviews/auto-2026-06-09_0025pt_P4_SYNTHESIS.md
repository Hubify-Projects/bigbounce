# P4 auto-2026-06-09_0025pt — v3 native-PDF cross-vendor SYNTHESIS

**Reviewers**: P4_Claude_brutal, P4_Gemini_cosmology, P4_Grok_brutal, P4_META_REVIEW, P4_OpenAI_methodology, P4_Perplexity_citations
**Total findings (across all reviewers)**: 50
**Distinct consensus groups**: 16

## Per-reviewer finding counts

| Reviewer | ESSENTIAL | MAJOR | MINOR | NIT |
|----------|-----------|-------|-------|-----|
| P4_Claude_brutal | 0 | 0 | 0 | 0 |
| P4_Gemini_cosmology | 2 | 2 | 4 | 0 |
| P4_Grok_brutal | 2 | 3 | 0 | 3 |
| P4_META_REVIEW | 3 | 5 | 0 | 1 |
| P4_OpenAI_methodology | 0 | 0 | 0 | 0 |
| P4_Perplexity_citations | 17 | 5 | 2 | 1 |

---

## Consensus-grouped findings (most reviewers first)

### `table_ii` — ESSENTIAL — **CONSENSUS** (3 reviewers)

Reviewers: P4_Gemini_cosmology, P4_Grok_brutal, P4_Perplexity_citations

- **[P4_Gemini_cosmology/P4-E1/ESSENTIAL]**: **P4-E1: Inconsistent Galaxy Counts in Figure 2 (Page 6)** *   **Problem:** The galaxy counts for CW, CCW, and Not-Spiral classes listed in the caption of Figure 2 do not match the counts shown in the pie chart itself.     *   Caption: N_cw = 1,592,107; N_ccw = 1,609,053; N_ns = 5,273,371.     *   Pie Chart: N_cw = 1,687,069; N_ccw = 1,634,726; N_ns = 5,152,736.     While both sets of numbers sum to the same total, this is a critical inconsistency in the primary data statistics. All other statistics in the paper (e.g., the global CW fraction in Table II) depend on these numbers. *   **Required…
- **[P4_Gemini_cosmology/P4-N1/MINOR]**: **P4-N1: Discrepancy in Global CW Fraction Significance (Table II, Page 4)** *   **Problem:** The "Dev. (σ)" column in Table II appears to be calculated incorrectly. For Catalog C, the text gives f_cw = 0.4974 and σ_binom = 0.000279. The deviation from 0.5 is (0.4974 - 0.5) / 0.000279 = -9.32σ. The table reports 9.5 (and the text uses this value). Similar small discrepancies exist for the other rows. *   **Required Fix:** Recompute and correct all values in the "Dev. (σ)" column of Table II. Update the corresponding value in the main text (Sec. IV B).
- **[P4_Grok_brutal/P4-M3/MAJOR]**: **P4-M3** (Appendix D, p. 10)   The five-anchor systematics battery is presented after the headline result. The paper never quantifies the trials factor incurred by testing five correlated diagnostics on the same map; the joint χ2/dof = 4.24 quoted in Table III already indicates that the null model is inadequate, yet no global p-value for the entire battery is given.   Required fix: report a trials-corrected significance for the full systematics suite.
- **[P4_Grok_brutal/P4-N3/NIT]**: **P4-N3** (Table II, p. 4)   Excess percentages are quoted to two decimal places while the underlying binomial uncertainties are ∼0.028 %. The second decimal is not meaningful and should be dropped.  **Summary recommendation**
- **[P4_Perplexity_citations/P4-M3/MAJOR]**: P4-M3   Section: Figures 3 and 4 (pages 7–8) and Table III (page 6)   Problem: Figure 4 shows pseudo‑Cℓ curves and an orange band from the monopole-only null, while Table III presents bandpowers and a joint χ²/dof = 161.2/38≈4.24, interpreted as “dominated by mask-coupled monopole.” This interpretation is plausible but no quantitative comparison of χ² with and without a monopole-leakage template is shown, nor is a goodness‑of‑fit p‑value quoted; the conclusion that the excess is “dominated” by monopole leakage is more qualitative assertion than statistically demonstrated.   Required fix: Provi…

### `shamir_citation` — ESSENTIAL — **CONSENSUS** (2 reviewers)

Reviewers: P4_Grok_brutal, P4_Perplexity_citations

- **[P4_Grok_brutal/P4-M2/MAJOR]**: **P4-M2** (Sec. V A, p. 6)   The paper states that its maximum regional asymmetry (0.32 %) and dipole (0.43σ) are “inconsistent … by a factor of ∼6–12” with Shamir’s ∼3 % claims. The comparison mixes different estimators (per-bin vs. global dipole), different masks, and different null hypotheses without a matched re-analysis of the SDSS sample through the present pipeline.   Required fix: either perform a homogeneous re-analysis or qualify the numerical factor as an order-of-magnitude estimate only.
- **[P4_Perplexity_citations/P4-E9/ESSENTIAL]**: P4-E9   Section: Sec. I Introduction (page 2) – Shamir citations [1–4]   Problem: The text states “Shamir (2012) [4] reported a 2–4σ dipole with per-bin asymmetry amplitudes of ∼5–20% using ∼1.27×10⁵ SDSS galaxies. Shamir (2020) [1] and Shamir (2022) [3] reported results with ∼2–4% asymmetries on DESI Legacy samples (‘nearly 1.3×10⁶ spiral galaxies’ per the published abstract).” In [4] (Phys. Lett. B 715, 25, arXiv:1207.5464), the sample size and asymmetry amplitudes are indeed large, but the quoted “∼1.27×10⁵” and “5–20%” must match the paper’s abstract and main tables; similarly, [3] (MNRAS …
- **[P4_Perplexity_citations/P4-m6/MINOR]**: P4-m6   Section: Throughout (all pages) – novelty claims   Problem: The paper repeatedly claims “largest galaxy chirality catalog to date: 8,474,531 galaxies” and “survey-scale coverage of 8.47 million galaxies (3.2M spirals, 1.6× CE-ResNet’s scale)” as key novelties. While 3.2M spirals is indeed larger than the ∼1.95M in Jia et al. [7], no systematic survey of prior catalogs is provided (e.g. potential larger but noisier spiral samples, or catalogs with different selection criteria).   Required fix: Either (a) add a short subsection explicitly reviewing the sizes of previous chirality‑classif…

### `sigma_mixing` — ESSENTIAL — **CONSENSUS** (2 reviewers)

Reviewers: P4_Grok_brutal, P4_Perplexity_citations

- **[P4_Grok_brutal/P4-E2/ESSENTIAL]**: **P4-E2** (Abstract, p. 1; Table I caption, p. 4)   The abstract asserts “σ values … are not directly comparable across estimators.” Table I nevertheless places the real-space (+0.43σ), MASTER (−0.122σ), canonical (+3.64σ), and hemisphere (pLEE ≤ 10−4) results in a single table without repeating the non-comparability caveat in every row or in the table caption. This violates the explicit instruction given in the review criteria.   Required fix: add the qualifier to every table entry and to the table caption itself.
- **[P4_Perplexity_citations/P4-E2/ESSENTIAL]**: P4-E2   Section: Abstract (page 1), sentence “Note: σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators; see Table I for the mapping of each result to its null.”   Problem: Despite this caveat in the abstract, later sections juxtapose σ-values from different null procedures directly as if they were comparable (e.g., +3.64σ canonical-mask residual vs −0.122σ subsample ℓ=1 null; +4.31σ “monopole-preserving” pseudo‑Cℓ vs 0.43σ real‑space dipole) without reiterating non‑comparability at each juxtaposition. The in…

### `table_iv` — MAJOR — **CONSENSUS** (2 reviewers)

Reviewers: P4_Gemini_cosmology, P4_META_REVIEW

- **[P4_Gemini_cosmology/P4-M1/MAJOR]**: **P4-M1: Analysis Based on "In Queue" Re-run (Footnote 1, Page 5)** *   **Problem:** Footnote 1 reveals that a key methodological choice for the generative null (using `N_spiral(p)` trials vs. `N_all(p)` trials) has a quantitative impact, and that a "parallel rerun on N(p)all-trial draws is in queue". A published paper cannot be based on incomplete or provisional analysis. The statement that the "headline conclusion... is robust to the trial-pool choice" is an assertion that must be demonstrated with the final analysis. *   **Required Fix:** The author must complete the `N_all(p)` re-run and u…
- **[P4_META_REVIEW/P4-META-M5/MAJOR]**: ## P4-META-M5 [MAJOR] — Footnote 1's "robustness" claim is internally contradictory **Section**: Footnote 1, p. 5 (continued p. 5–6) **Why missed**: Gemini flagged the "in queue" issue as a major revision, but did not notice the logical contradiction *within* the footnote. **Problem**: Footnote 1 makes two incompatible claims: > "the size of the resulting shift in the headline 99.3% reproduction figure (and in the +1.68σ residual of Table IV) is **not predictable analytically**" followed immediately by: > "the qualitative reproduction structure... is **robust to the trial-pool choice**; the qu…

### `fisher_floor` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: P4_Perplexity_citations

- **[P4_Perplexity_citations/P4-E4/ESSENTIAL]**: P4-E4   Section: Abstract (page 1) – Falsification criterion paragraph   Problem: The abstract states A₉₅ ≈ 1.5–2% with “empirical 50%-recovery-at-3σ threshold of A₅₀ ≈ 0.75%” and claims that a future detection at A≈0.75% and 5σ would be “entirely consistent with the present non-detection.” In Sec. VI A, the Fisher 3σ floor is 0.29% and the empirical injection‑recovery gives P(σ>3)=0.55 at A=0.75% and 0.15 at A=0.5%; the mapping from these points to A₉₅ ≈ 1.5–2% is asserted but not actually demonstrated, and 0.75% is repeatedly used both as an “empirical sensitivity floor” and as a threshold f…
- **[P4_Perplexity_citations/P4-E17/ESSENTIAL]**: P4-E17   Section: Sec. VI A “Sensitivity floor” (page 8)   Problem: The Fisher Poisson 3σ floor is quoted as ~0.29% (from σ(A/2) ≈ 0.048% at N_spiral = 3,201,160, f_sky = 0.46). Recomputing: for a binomial proportion p≈0.5 and N≈3.2×10⁶, σ(p) ≈ sqrt(0.25/N) ≈ 0.00028 (0.028%); a 3σ excess in p is ~0.084% in the half‑amplitude A/2, so A ≈ 0.17%, not 0.29%, unless additional factors (e.g. f_sky, pixelization) are included. The derivation of 0.29% is not shown.   Required fix: Provide an explicit derivation for the 0.29% Fisher floor, including all factors (f_sky, effective number of modes, pixel…

### `iye_citation,shamir_citation` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: P4_Perplexity_citations

- **[P4_Perplexity_citations/P4-E16/ESSENTIAL]**: P4-E16   Section: Sec. V A “Shamir (2012, 2020, 2022)” (page 6–7)   Problem: The text asserts: “These conclusions corroborate and extend the methodological critique of Iye et al. (2021) [5] with 3.2×10⁶ spirals (30× extension).” The claim of a “30× extension” in sample size relative to Iye et al. [5] must be numerically correct and sourced. Iye et al. (ApJ 907, 123, arXiv:2011.00662) use 80,000 galaxies (or another reported number); the factor of 30 is approximate and not explicitly given in [5].   Required fix: Quote the exact spiral sample size in Iye et al. [5] from their paper and compute …

### `n_mc_500,table_ii,table_iv` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: P4_Perplexity_citations

- **[P4_Perplexity_citations/P4-E3/ESSENTIAL]**: P4-E3   Section: Abstract (page 1) & Sec. IV C / Table III (page 6)   Problem: The abstract quotes the “post‑MASTER dipole significance is −0.122σ (subsample mask, headline)” and a “real‑space post‑TTA Catalog C dipole is +0.43σ (p = 0.30, isotropic-null bootstrap, NMC = 10,000).” In Sec. IV C, the ℓ=1 MASTER measurement is C1meas = 1.494×10⁻⁶, ⟨C1null⟩=1.546×10⁻⁶, σnull=4.29×10⁻⁷, which indeed gives (1.494−1.546)/4.29×10⁻⁷ ≃ −0.12σ, so this is numerically consistent. However, the abstract also states: “A canonical-mask diagnostic… raw pseudo-C₁ … is reproduced at 99.3% of its observed amplitu…

### `n_mc_500,table_iv` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: P4_META_REVIEW

- **[P4_META_REVIEW/P4-META-E2/ESSENTIAL]**: ## P4-META-E2 [ESSENTIAL] — N_MC = 500 caps achievable empirical significance at ~2.88σ **Section**: Sec. IV D (p. 4–5), Appendix A (p. 9), Table IV **Why missed**: Reviewers verified the MC procedure ran, but did not check whether the MC budget could in principle support the quoted significance. **Problem**: The per-pixel-shuffle null uses N_MC = 500. The minimum non-zero achievable p-value is 1/500 = 0.002, corresponding to a two-sided Gaussian-equivalent of ~2.88σ. The reported p_MC = 15/500 = 0.030 (= 1.88σ one-sided) is internally consistent, but the "moment-ratio" +3.64σ cannot be *empir…

### `nmap_weighting` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: P4_Perplexity_citations

- **[P4_Perplexity_citations/P4-E12/ESSENTIAL]**: P4-E12   Section: Sec. III A Declared Analysis Hierarchy (page 3) & Table I (page 4)   Problem: Table I defines N_map^weighted = Σ_p W_p where W_p = N_all^(p), and claims “N_map^weighted exceeds N_catalog,spiral because W_p includes non-spiral galaxies (~62% of the catalog); each galaxy is counted once.” However, with NSIDE=64 pixels of area ~0.84 deg², many galaxies will fall in the same pixel, so Σ_p N_all^(p) should equal the total number of galaxies (i.e. 8.47M), whereas Table I lists N_map^weighted = 5,547,858; this is *less* than the total number of galaxies and also < N_catalog,total, c…

### `table_ii,asymmetry_factor` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: P4_Perplexity_citations

- **[P4_Perplexity_citations/P4-E13/ESSENTIAL]**: P4-E13   Section: Sec. IV B “Global CW fraction” (page 4) vs. Table II (page 4)   Problem: Table II lists Catalog C cw/(cw+ccw) = 0.4974 ± 0.000279 with “Dev.(σ) = 9.5,” but (0.4974−0.5)/0.000279 ≈ −9.3σ, not −9.5σ (depending on rounding). Additionally, the text describes the “3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%,” implying that Catalog A is +0.79% (0.5079) and Catalog C is −0.26% (0.4974). The wording “+2.05% to −0.53%” is unclear: 0.5079–0.5 = +0.79%, not +2.05%; 0.4974–0.5 = −0.26%, not −0.53%. There is an unexplained factor-of-two.   Required fix: Recomp…

### `table_ii,table_iv` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: P4_META_REVIEW

- **[P4_META_REVIEW/P4-META-E1/ESSENTIAL]**: ## P4-META-E1 [ESSENTIAL] — The +3.64σ headline number is, by the paper's own admission, ≈1.9σ **Section**: Abstract (p. 1); Sec. IV D, Table IV (p. 6); Conclusions (p. 8) **Why missed**: Buried inside a parenthetical in the abstract's third paragraph; reviewers focused on the leading "+3.64σ" number itself, not the parenthetical demolition that immediately follows it. **Problem**: The abstract states, verbatim: > "The post-MASTER canonical-mask direct-MC residual is +3.64σ (z = ∆/σ_null moment-ratio; **empirical rank p_MC = 0.030, i.e. ≈1.9σ Gaussian-equivalent**; 500-MC binomial per-pixel-sh…

### `table_ii,cosmic_variance` — MAJOR — _single-reviewer_ (1 reviewer)

Reviewers: P4_META_REVIEW

- **[P4_META_REVIEW/P4-META-M3/MAJOR]**: ## P4-META-M3 [MAJOR] — Single-mode ℓ=1 MASTER with 3 a_ℓm modes is cosmic-variance dominated **Section**: Sec. IV C, Table III (p. 6); Appendix A (p. 9) **Why missed**: All reviewers accepted MASTER as a black box; none audited the multipole-counting. **Problem**: At ℓ=1 there are 2ℓ+1 = 3 a_1m modes. The full-sky Gaussian cosmic variance on C_1 is √(2/(2ℓ+1)) × C_1 = 82% of the mean. Mode-coupling on f_sky = 0.659 inflates this. The label-shuffle null used as the σ denominator (σ_null = 4.29×10⁻⁷) is the *classifier-shot-noise* variance, not the cosmic-variance of a true dipole, and the two …

### `length` — MINOR — _single-reviewer_ (1 reviewer)

Reviewers: P4_Perplexity_citations

- **[P4_Perplexity_citations/P4-m7/MINOR]**: P4-m7   Section: Length and structure (entire manuscript)   Problem: The paper runs 13 pages with a heavy emphasis on internal diagnostics, appendices, and qualitative interpretation of systematics. For the claimed primary scientific result (“a null ℓ=1 subsample-mask dipole”), the length appears excessive: multiple pages repeat the same qualitative statement that the canonical-mask residual is not cosmological. Many details (e.g. full bias‑hardening suite, morphology systematics) are appropriate as supplemental material but could be condensed for PRD.   Required fix: Condense and reorganize: …

### `table_iv,table_iv_z` — MINOR — _single-reviewer_ (1 reviewer)

Reviewers: P4_Gemini_cosmology

- **[P4_Gemini_cosmology/P4-N2/MINOR]**: **P4-N2: Discrepancy in Monopole Null z-score (Table IV, Page 6)** *   **Problem:** The z-score for the "Pre-MASTER pseudo-C_l" statistic in Table IV is calculated as +1.68. My calculation is (1.696 - 1.685) / 0.007 = 1.57. This is a minor but noticeable discrepancy. *   **Required Fix:** Please recompute and, if necessary, correct the z-score in Table IV.

### `future_date` — NIT — _single-reviewer_ (1 reviewer)

Reviewers: P4_Grok_brutal

- **[P4_Grok_brutal/P4-N1/NIT]**: **P4-N1** (Title page, p. 1)   The manuscript is dated “June 2026.” This is a future date relative to any current submission and constitutes an internal bookkeeping artifact that should be removed.

## Other findings (26)

- **[P4_Gemini_cosmology/P4-E2/ESSENTIAL]**: **P4-E2: Inconsistent Figure and Caption for Figure 4 (Page 8)** *   **Problem:** The caption for Figure 4 describes a different figure from the one that is shown.     *   The caption states: "Top: l=1 dipole power. Bottom: l=2 quadrupole. Black: data; orange band: 500-MC monopole-only generative null...".     *   The figure shown is a single bar chart for multipoles l=1 to l=5, with blue bars for…
- **[P4_Gemini_cosmology/P4-M2/MAJOR]**: **P4-M2: Confusing and Opaque Footnote on Subsample Robustness (Footnote 2, Page 11)** *   **Problem:** Footnote 2 on page 11 is extremely dense and difficult to parse. It introduces a new, previously unmentioned estimator ("monopole-preserving Catalog-C-full +4.31σ") in a footnote to make a point about high-confidence subsamples. This makes the argument hard to follow and obscures the main point.…
- **[P4_Gemini_cosmology/P4-N3/MINOR]**: **P4-N3: Scope of Parity-Odd Signal (Sec. VI B, Page 8)** *   **Problem:** The text states "the parity-odd signal lives in the l=0 monopole and even-l multipoles." While this is true for scalar fields like temperature, for a projected spin field (an axial vector), the parity-odd modes are different. A full 3D analysis would be required, but this statement might be an oversimplification for the spe…
- **[P4_Gemini_cosmology/P4-N4/MINOR]**: **P4-N4: Typo in Dilution Factor Formula (Sec. VI A, Page 8)** *   **Problem:** The text gives the GZ1-dilution factor as "g=2a-1 ≈ 0.398 for a = 0.6991". The formula should be `g = 2a - 1`. The use of "a-" is a clear typographical error. *   **Required Fix:** Correct the typo to `g = 2a - 1`.
- **[P4_Grok_brutal/P4-E1/ESSENTIAL]**: **P4-E1** (Abstract, p. 1; Sec. IV D, p. 4)   The abstract headline states a “null ℓ=1 chirality-dipole observable … −0.122σ” while simultaneously advertising “Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual.” The +3.64σ canonical-mask residual is interpreted as leakage on the basis of a single generative monopole-only null that reproduces 99.3 % of the pre-MASTER pow…
- **[P4_Grok_brutal/P4-M1/MAJOR]**: **P4-M1** (Sec. IV C, p. 4; Fig. 3, p. 7)   The real-space dipole on Catalog C is reported as +0.43σ (p = 0.30) from an isotropic bootstrap (NMC = 10 000). The same catalog yields Cℓ=1 = 1.494 × 10−6 after MASTER deconvolution, 3.29σ below the null mean. No end-to-end simulation injecting a known cosmological dipole, passing it through the full ViT+TTA+MASTER pipeline, and recovering the input amp…
- **[P4_Grok_brutal/P4-N2/NIT]**: **P4-N2** (Fig. 1 caption, p. 5)   The caption states “flip swap correlation = 1.000 by construction.” This is tautological; the figure adds no new information beyond the definition of TTA and should be removed or replaced with a diagnostic that can fail.
- **[P4_META_REVIEW/P4-META-E3/ESSENTIAL]**: ## P4-META-E3 [ESSENTIAL] — Headline "subsample mask" is chosen post-hoc; no pre-registration **Section**: Sec. III A (p. 3), Sec. IV C (p. 4), Appendix A (p. 9) **Why missed**: All reviewers treated the mask hierarchy as given. Nobody asked whether the f_sky = 0.659 "subsample" mask was selected *because* it gave the null result. **Problem**: The same Catalog C data evaluated on the **canonical m…
- **[P4_META_REVIEW/P4-META-M1/MAJOR]**: ## P4-META-M1 [MAJOR] — Bias-hardening T6 and T8 thresholds are loose by factors of 12–35× relative to the science **Section**: Appendix B, Table V (p. 10) **Why missed**: Reviewers verified the tests "pass" but did not compare the pass thresholds to the sensitivity floor claimed in the science. **Problem**: T8 declares CW/CCW balance acceptable at 50% ± 10%, and the result is 49.7%. The science c…
- **[P4_META_REVIEW/P4-META-M2/MAJOR]**: ## P4-META-M2 [MAJOR] — Injection-recovery uses 471k HC subsample but is applied to 3.2M sample **Section**: Sec. VI A (p. 8), Table I row (vi) **Why missed**: Grok demanded an injection campaign and Perplexity asked about A₉₅ definition, but neither checked the sample-size mismatch between the injection target and the science target. **Problem**: The empirical 50%-recovery-at-3σ threshold A₅₀ ≈ 0…
- **[P4_META_REVIEW/P4-META-M4/MAJOR]**: ## P4-META-M4 [MAJOR] — W_p = N_all is the wrong weight for a spiral-chirality field **Section**: Appendix A (p. 9), Table I caption (p. 4) **Why missed**: Perplexity flagged the definition ambiguity but not the optimality of the choice. **Problem**: The asymmetry field is A_p = (N_CW − N_CCW)/N_spiral defined on spirals only. The optimal inverse-variance weight is W_p ∝ N_spiral(p), since the sho…
- **[P4_META_REVIEW/P4-META-N1/NIT]**: ## P4-META-N1 [MINOR] — The dilution factor g = 2a − 1 assumes random Bernoulli classifier errors **Section**: Sec. VI A (p. 8) **Why missed**: Perplexity flagged the propagation as undocumented but did not audit the model. **Problem**: The paper writes "GZ1-dilution factor g = 2a − 1 ≈ 0.398 for a = 0.6991, giving a true-underlying threshold ~1.88%." This formula is correct *only* if classifier e…
- **[P4_Perplexity_citations/P4-E1/ESSENTIAL]**: P4-E1   Section: Title / Header (page 1)   Problem: The title claims a **“Galaxy chirality catalog v1.0.159”** context in the reviewer metadata, but the rendered paper’s title and body do not specify any version tag for the released catalog, while the Data Availability section refers instead to a HuggingFace release “v2026.04” and a GitHub repo “bigbounce” with no explicit semantic link to “v1.0.1…
- **[P4_Perplexity_citations/P4-E5/ESSENTIAL]**: P4-E5   Section: Abstract, first paragraph (page 1) and Table I (page 4)   Problem: The abstract states: “8.47 M sources, 471 049 high-confidence per-spiral after peq_CW > 0.9,” while Table I’s entry (vi) injection floor states “A = 0.75%” threshold on “471,049 HC.” However, Sec. VI A defines the injection‑recovery using “HC-spiral subsample (N = 471,049, N_MC,null = 1000, N_MC,inj = 100 per ampli…
- **[P4_Perplexity_citations/P4-E6/ESSENTIAL]**: P4-E6   Section: Sec. II B “Training Labels” (page 2) and Sec. III C (page 3) vs. Figure 1 (page 5)   Problem: The main text clearly states that production uses **2‑fold** TTA (original + horizontal flip), with rotations used only for diagnostics: “We restrict to 2-fold TTA… A direct D₄‑TTA hold-out… confirms… Full details in Appendix B.” However, Figure 1 depicts “Test-time D4 equivariant averagi…
- **[P4_Perplexity_citations/P4-E7/ESSENTIAL]**: P4-E7   Section: Data / Galaxy Images (page 2)   Problem: The paper cites “Smith42/galaxies dataset on HuggingFace (… 8,474,688 galaxy images)” but provides no formal citation (author, year, persistent identifier) in the References list, despite this dataset being the foundational data source. This is a serious citation omission by PRD standards, where all external data products must be referenced…
- **[P4_Perplexity_citations/P4-E8/ESSENTIAL]**: P4-E8   Section: Sec. I Introduction (page 2), paragraph summarizing Jia et al. [7]   Problem: The text claims: “Jia et al. [7] introduced CE-ResNet… yielding cw/ccw = 0.998 on ∼ 1.95 million galaxies.” In the cited paper [7] (Jia, Zhu & Pen 2023, ApJ 943, 32, arXiv:2210.04168), the main reported outcome is that the CW and CCW counts are consistent with parity (cw/ccw ratio close to 1) but the spe…
- **[P4_Perplexity_citations/P4-E10/ESSENTIAL]**: P4-E10   Section: Sec. I Introduction (page 2), “Jia et al. [7] … cw/ccw = 0.998 on ∼ 1.95 million galaxies” vs Sec. V B (page 7)   Problem: Sec. V B states: “CE-ResNet [7] achieves cw/ccw = 0.998 with architectural equivariance on 1.95 million galaxies. Our Catalog C achieves 1.6× the spiral coverage…” implying CE-ResNet’s spiral sample is 1.95M and this is *directly comparable* to the 3.2M spira…
- **[P4_Perplexity_citations/P4-E11/ESSENTIAL]**: P4-E11   Section: Sec. II A “Galaxy Images” (page 2)   Problem: The paper states: “Each image is a 224×224 pixel cutout in grz bands at 0.262″/pixel.” DESI Legacy DR8 has a nominal pixel scale of 0.262 arcsec/pixel, but “Smith42/galaxies” as a derived dataset may have resampled or cropped images. This exact pixel scale and size is not supported by a citation to DR8  or to the dataset description. …
- **[P4_Perplexity_citations/P4-E14/ESSENTIAL]**: P4-E14   Section: Sec. IV C “Dipole Analysis” (page 4–5) – simple dipole 0.43σ, p=0.30   Problem: The simple dipole significance is reported as 0.43σ with p = 0.30 from 10,000 bootstrap realizations. A one-sided Gaussian mapping from 0.43σ gives p ≈ 0.33, and two-sided p ≈ 0.67. It is unclear which convention is used and how p=0.30 is derived; this misalignment may confuse readers and slightly mis…
- **[P4_Perplexity_citations/P4-E15/ESSENTIAL]**: P4-E15   Section: Sec. IV D “Monopole+mask leakage generative null” (page 4–5), footnote 1   Problem: Footnote 1 acknowledges that an earlier version used ambiguous wording “Binomial(n_total, p_global_CW)” and that a rerun with N_all(p) is “in queue” and may change the quantitative “99.3%” reproduction figure. However, the main text still bases key conclusions (e.g. that prior literature’s pre‑MAS…
- **[P4_Perplexity_citations/P4-M1/MAJOR]**: P4-M1   Section: Sec. III B “Model Architecture” (page 3) and Appendix B (page 9–10)   Problem: The architecture and training details are described, but there is no quantitative uncertainty propagation from classifier misclassification (69.91% agreement with GZ1; Cohen’s κ=0.40) into the cosmological dipole constraints beyond a brief mention of a “GZ1-dilution factor g ≈ 0.398.” The paper claims t…
- **[P4_Perplexity_citations/P4-M2/MAJOR]**: P4-M2   Section: Equations (2) and (3) (page 3–4)   Problem: Equation (2) defines equivariant probabilities as arithmetic averages of original and flipped outputs, but does not explicitly state that the same input image is used for both passes, nor how stochastic augmentations (e.g. random crops, noise) during inference are controlled. This affects reproducibility of the catalog and the derived st…
- **[P4_Perplexity_citations/P4-M4/MAJOR]**: P4-M4   Section: Data Availability (page 11–12)   Problem: Data and code availability URLs are given in prose but not as formal references, and there is no explicit statement that the archived artifacts correspond exactly to the version used in the paper (e.g., no Git commit hash, no DOIs, and no specification that the models and scripts can reproduce all tables within numerical tolerances). PRD s…
- **[P4_Perplexity_citations/P4-M5/MAJOR]**: P4-M5   Section: References [1]–[7], – (pages 12–13)   Problem: Several references are incomplete or inconsistent in style for PRD:   – [1], [3], [7] mix arXiv and DOI but do not include volume/page for all.   – Some multi-author lists have “et al.” but the in‑text citations sometimes rely on exact author combinations (e.g. “Jia et al. (2023)” vs “H. Jia, H.-M. Zhu, and U.-L. Pen”).   – The datase…
- **[P4_Perplexity_citations/P4-N1/NIT]**: P4-N1   Section: Minor wording / typos (multiple pages)   Problem: Various small issues:   – “NaMaster low-ℓ deconvolution artifact. Interpretation (iii) sharp-edge variant” (missing hyphen and commas).   – “cw/ccw = 0.998” vs “CW/CCW” inconsistent capitalization.   – “probes classifier non-equivariance” should be “non‑equivariance”.   – Some sentences run long and would benefit from restructuring…
