# P4 R10v3 — v3 native-PDF cross-vendor SYNTHESIS

**Reviewers**: Claude_brutal, Gemini_cosmology, Grok_brutal, OpenAI_methodology, Perplexity_citations
**Total findings (across all reviewers)**: 51
**Distinct consensus groups**: 16

## Per-reviewer finding counts

| Reviewer | ESSENTIAL | MAJOR | MINOR | NIT |
|----------|-----------|-------|-------|-----|
| Claude_brutal | 0 | 0 | 0 | 0 |
| Gemini_cosmology | 2 | 1 | 3 | 1 |
| Grok_brutal | 0 | 0 | 0 | 0 |
| OpenAI_methodology | 7 | 5 | 7 | 0 |
| Perplexity_citations | 0 | 0 | 0 | 0 |

---

## Consensus-grouped findings (most reviewers first)

### `table_ii` — MAJOR — **CONSENSUS** (3 reviewers)

Reviewers: Grok_brutal, OpenAI_methodology, Perplexity_citations

- **[Grok_brutal/P4-E2/UNKNOWN]**: **P4-E2 (ESSENTIAL)**   Section: Abstract (p. 1)   Problem: The headline scalar “−0.122\(\sigma\)” is presented as the primary result, yet the body (Sec. IV C, Table III) shows this value is obtained only after MASTER deconvolution on a strict-superset subsample mask; the raw real-space dipole on the full catalog is +0.43\(\sigma\). The abstract therefore reports a processed diagnostic rather than the unprocessed observable claimed in the title.   Required fix: Rewrite the abstract to state the raw dipole first, followed by the processed value, or remove the numerical headline from the abstrac…
- **[OpenAI_methodology/P4-M4/MAJOR]**: P4-M4 Figures 2 & 3 (low-ℓ spectra): vertical axes lack units (“sr” is given only in Table III).  Axis labelling must match the units in the tables.
- **[OpenAI_methodology/P4-m3/MINOR]**: P4-m3 p. 5, Table III caption: “ℓ= 1 (single mode) anchors the dipole-isotropy null” – grammar (“anchors”) unclear.
- **[Perplexity_citations/P4-M4/UNKNOWN]**: P4-M4 (MAJOR)   Section: Sec. IV C, Table III, Appendix A and D, pages 4–5, 7–8   Problem: The use of NaMaster and the distinction between the “subsample mask” and “canonical mask” are central to the claim of a robust ℓ=1 null versus a systematic canonical residual. However, the definitions are somewhat scattered, and in particular:  - The subsample mask is called a “strict-superset subsample mask (n = 5,547,858, fsky = 0.659)” but its construction (beyond Nspiral > 10) is not clearly specified in the main body; it appears only in Appendix A as “analysis subsample mask”, yet the selection crit…

### `sigma_mixing,table_ii` — ESSENTIAL — **CONSENSUS** (2 reviewers)

Reviewers: Gemini_cosmology, Perplexity_citations

- **[Gemini_cosmology/P4-E1/ESSENTIAL]**: **P4-E1: Ambiguous definition and use of statistical significance (σ)** *   **Location:** Throughout the paper, but critically on Page 1 (Abstract and main text), Page 4 (Table I), Page 5 (Table III), and Page 6 (Conclusion b). *   **Problem:** The paper uses the symbol 'σ' to report significance, but its meaning is inconsistent. It appears to be used as a z-score, `z = (value - mean_null) / std_null`, without regard to the underlying null distribution's shape. On Page 1, the authors report a "+3.64σ" residual but immediately qualify it with `(empirical rank pmc = 0.030, i.e. ≈1.9σ Gaussian-eq…
- **[Perplexity_citations/P4-E2/UNKNOWN]**: P4-E2 (ESSENTIAL)   Section: Abstract, page 1   Problem: The abstract states “Note: σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators; see Table II for the mapping of each result to its null.” The body repeats this concept but does not re-assert the non-comparability at every juxtaposition where σ from different nulls are placed side-by-side (e.g., Table I, Table III, multiple paragraphs in Sec. IV–VI). This violates the review instruction requiring explicit “not directly comparable” qualification at every …

### `table_iv,table_iv_z` — ESSENTIAL — **CONSENSUS** (2 reviewers)

Reviewers: Gemini_cosmology, OpenAI_methodology

- **[Gemini_cosmology/P4-m2/MINOR]**: **P4-m2: Minor numerical inconsistencies in Table IV** *   **Location:** Page 5, Table IV. *   **Problem:** The z-scores in the final column do not exactly match the provided data.     *   Pre-MASTER pseudo-C_l: `z = (1.696e-2 - 1.685e-2) / 0.007e-2 = 0.011 / 0.007 = 1.57`. The table reports +1.68.     *   Hemisphere max|A|: `z = (3.48e-3 - 1.69e-3) / 0.41e-3 = 1.79 / 0.41 = 4.37`. The table reports +4.42. *   **Required Fix:** Re-calculate and correct the z-scores in Table IV.
- **[OpenAI_methodology/P4-E7/ESSENTIAL]**: P4-E7 Sec. IV D, p. 4 (Table IV)     • Offending numbers Data 1.696 × 10⁻²; Null mean     (1.685 ± 0.007) × 10⁻²; z = +1.68.     • Problem (1.696 – 1.685)/0.00007 = 1.57, not 1.68.     • Required fix Re-calculate z or correct the tabulated     σ_null.  -------------------------------------------------

### `future_date` — MINOR — **CONSENSUS** (2 reviewers)

Reviewers: Gemini_cosmology, Perplexity_citations

- **[Gemini_cosmology/P4-m3/MINOR]**: **P4-m3: Future date on manuscript** *   **Location:** Page 1, under author list. *   **Problem:** The paper is dated "(Dated: June 2026)". *   **Required Fix:** Change the date to the date of submission.
- **[Perplexity_citations/P4-E1/UNKNOWN]**: P4-E1 (ESSENTIAL)   Section: Title block, page 1   Problem: The manuscript is dated “(Dated: June 2026)”, which is a future date relative to the current arXiv/PRD publication pipeline and strongly suggests the date was fabricated for the draft rather than reflecting an actual submission or acceptance date.   Required fix: Replace the date with either the actual submission date (once known) or follow PRD’s convention for undated preprints (often omitting a future “dated” field in submitted versions). Do not use a future date.  ---

### `label_noise` — UNKNOWN — **CONSENSUS** (2 reviewers)

Reviewers: Grok_brutal, Perplexity_citations

- **[Grok_brutal/P4-M3/UNKNOWN]**: **P4-M3 (MAJOR)**   Section: Sec. II B (p. 2) and Appendix B (p. 7)   Problem: 67.6 % of training labels are themselves CE-ResNet predictions; the independent GZ1 cross-match accuracy of 69.91 % is then treated as the “conservative accuracy floor.” No propagation of label noise into the final dipole uncertainty is shown.   Required fix: Monte-Carlo relabeling of the training set according to the measured 69.91 % accuracy and re-derivation of all downstream \(\sigma\) values.
- **[Grok_brutal/P4-N2/UNKNOWN]**: **P4-N2 (MINOR)**   Section: Table I caption (p. 4)   Problem: Typo “\(N_{\rm map weighted}\) exceeds \(N_{\rm catalog spiral}\) because \(W_p\) includes non-spiral galaxies” is repeated verbatim from an earlier internal draft.   Required fix: Delete the redundant clause.  **P4-NIT1 (NIT)**   Section: Multiple locations (e.g., pp. 3, 5)   Problem: Repeated use of the phrase “canonical-mask residual” without hyphen consistency.   Required fix: Standardize hyphenation.  ## Summary recommendation **REJECT**  The manuscript’s central claim is a carefully processed null result whose numerical headl…
- **[Perplexity_citations/P4-M3/UNKNOWN]**: P4-M3 (MAJOR)   Section: Sec. II B “Training Labels”, page 2; Appendix B, page 7–8   Problem: The paper states that 67.6% of training labels come from CE-ResNet predictions and that an independent GZ1 cross-match yields 69.91% accuracy (κ = 0.40), which is then used as a “conservative accuracy floor”. However, the propagation of this 69.91% to the “sub-percent systematic floor” is only briefly mentioned (Sec. IV C and VI A) and is not quantitatively derived. The chain from label noise to effective sensitivity degradation is critical to the claimed 0.75% floor and to all upper limits.   Require…

### `asymmetry_factor` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P4-E2/ESSENTIAL]**: P4-E2 Sec. IV B, p. 3, line 19 (“3.86× asymmetry-suppression factor from raw +2.05 % to equivariant –0.53 %”)     • Problem The raw excess is +0.79 %, the equivariant shift     is –0.26 %.  The change in magnitude is 1.05 % and the     suppression factor |–0.26| / 0.79 = 0.33 (i.e. a 3.0×     reduction), not 2.05 % or 3.86×.      • Required fix Correct both the quoted percentage     difference and the suppression factor and propagate the     correction to Sec. VI (where the same numbers re-appear).
- **[OpenAI_methodology/P4-m1/MINOR]**: P4-m1 p. 2, col. 2: “3.86× asymmetry-suppression factor” appears twice with inconsistent capitalisation of “factor”.

### `n_mc_500,sigma_mixing` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P4-E6/ESSENTIAL]**: P4-E6 Monte-Carlo sample size for high-σ estimates     • Problem Several σ values >3 are quoted from only     N_MC = 500 permutations (e.g. the +3.64 σ canonical     residual).  With 499 degrees of freedom the sampling     error on the variance is ≈ 10 %, so the quoted σ has a     ±0.36 systematic uncertainty – too large for     “third-decimal” precision.     • Required fix Increase all permutation/null ensembles     that feed into reported σ or p < 0.01 to at least     N_MC = 10 000 or quote a bootstrap error on σ and     propagate it to the significance.

### `sigma_mixing` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P4-E5/ESSENTIAL]**: P4-E5 Throughout – sigma from different nulls shown side-by-side   • Example Table I juxtaposes –0.122 σ (label-shuffle null)     and +3.64 σ (per-pixel shuffle null) in the same column     without an explicit reminder that the numbers are not     cross-comparable.     • Required fix Add a footnote to every table/figure that     lists multiple σ values from different nulls stating     clearly “σ refers to the specific null in the     ‘Null’ column and must not be compared across rows”.

### `sigma_mixing,table_ii,table_ii_sigma_arithmetic` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P4-E1/ESSENTIAL]**: P4-E1 Sec. IV B, p. 3 (Table II, Tier A “Dev. (σ)”)     • Offending text “28.8”     • Problem With N=3 201 160 and f_CW = 0.5079,        σ_binom = √[p(1-p)/N] = 0.0002795.       (0.5079-0.5000)/0.0002795 = 28.32, not 28.8.  Same     mis-rounding propagates to the verbal 28.8 σ claim in     Sec. VI.     • Required fix Re-compute and correct the σ value (28.3 σ     to one decimal) everywhere it appears and adjust     downstream text.

### `duplicate_phrase` — MINOR — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P4-m2/MINOR]**: P4-m2 Duplicate phrase “canonical-mask residual is interpretation (ii) systematic” occurs on pp. 1 and 4.

### `table_ii,table_ii_sigma_arithmetic` — MINOR — _single-reviewer_ (1 reviewer)

Reviewers: Gemini_cosmology

- **[Gemini_cosmology/P4-m1/MINOR]**: **P4-m1: Minor numerical inconsistencies in Table II** *   **Location:** Page 4, Table II. *   **Problem:** The "Dev. (σ)" column does not exactly match a direct calculation based on the provided formula and data. Using `σ = sqrt(p(1-p)/N)` with `N=3,201,160` and `p=fcw`, the deviations are calculated as:     *   A (p=0.5079): (0.5079 - 0.5) / 0.0002794 ≈ +28.27σ (Table: 28.8)     *   B (p=0.504): (0.504 - 0.5) / 0.0002794 ≈ +14.32σ (Table: 14.6)     *   C (p=0.4974): (0.4974 - 0.5) / 0.0002794 ≈ -9.30σ (Table: 9.5)     The reported values are consistently slightly larger in magnitude. *   **R…

### `fisher_floor` — UNKNOWN — _single-reviewer_ (1 reviewer)

Reviewers: Perplexity_citations

- **[Perplexity_citations/P4-N3/UNKNOWN]**: P4-N3 (MINOR)   Section: Sec. VI A “Sensitivity Floor…”, page 6   Problem: The text states “Fisher Poisson floor at 3σ is ∼ 0.29% full-amplitude (from σ(A/2) ≈ 0.048% at Nspiral = 3,201,160, fsky = 0.46).” The use of fsky = 0.46 here is slightly inconsistent with earlier fsky values (0.49005 canonical, 0.659 subsample), and it is not explained how fsky = 0.46 is derived.   Required fix: Clarify the origin of fsky = 0.46 in this calculation (e.g., effective overlap after cuts, HEALPix mask coverage after edge effects). If it is an approximation or an intermediate estimate, say so explicitly and…

### `length` — UNKNOWN — _single-reviewer_ (1 reviewer)

Reviewers: Grok_brutal

- **[Grok_brutal/P4-M1/UNKNOWN]**: **P4-M1 (MAJOR)**   Section: Entire manuscript (10 pages + 5 appendices)   Problem: The core scientific claim is a single null result at \(\ell=1\) after two post-processing steps. The length exceeds any comparable null-result methods paper in the recent chirality literature by a factor of ~3.   Required fix: Reduce to a 5-page Letter (including all tables/figures) or justify the page count with a new positive detection.

### `shamir_citation` — UNKNOWN — _single-reviewer_ (1 reviewer)

Reviewers: Perplexity_citations

- **[Perplexity_citations/P4-E5/UNKNOWN]**: P4-E5 (ESSENTIAL)   Section: References [1]–, page 9–10   Problem: Several references to Shamir and related spin-parity works compress multiple papers into a single entry or have metadata inconsistencies:  - [1] “L. Shamir, ‘Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles,’ Astrophys. Space Sci. 365, 136 (2020), arXiv:2007.16116.”     Web search confirms arXiv:2007.16116 is titled “Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity asymmetry and multipoles” in Astrophysics and Space Science 365:136 (2020). The title in the refer…
- **[Perplexity_citations/P4-M1/UNKNOWN]**: P4-M1 (MAJOR)   Section: Abstract and Conclusion, pages 1 and 7   Problem: The claim “The present null disfavors the Shamir ∼ 2–4% detection class at the amplitude level under our pipeline… by a factor of ∼ 6–12” is presented without a clear quantitative mapping from the Shamir dipole amplitudes (which are per-bin asymmetries and may be defined differently) to the current paper’s dipole amplitude parameter A and detection threshold. In particular, Shamir’s 2–4% is sometimes a per-hemisphere excess rather than a full-sky dipole amplitude, while this work’s 0.75% sensitivity is a full-amplitude …

### `table_ii,asymmetry_factor` — UNKNOWN — _single-reviewer_ (1 reviewer)

Reviewers: Perplexity_citations

- **[Perplexity_citations/P4-N2/UNKNOWN]**: P4-N2 (MINOR)   Section: Sec. IV A, Table II, page 4   Problem: In Table II, the “Dev. (σ)” column lists “9.5” for Catalog C (equivariant), corresponding to the monopole deviation from 0.5. The text in Sec. IV B refers to “The Catalog C residual (9.5σ from 0.5000, Table II)… The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%…” However, the raw asymmetry is 0.5079 (0.79% excess) and the equivariant is 0.4974 (−0.26% excess), giving a suppression factor of about 0.79 / 0.26 ≈ 3.0, not 3.86. It is possible the 3.86 factor comes from a different pairing (e.g., A vs C), bu…

## Other findings (26)

- **[Gemini_cosmology/P4-E2/ESSENTIAL]**: **P4-E2: Reference to previous drafts of the paper** *   **Location:** Page 4, Section IV D, first paragraph. *   **Problem:** The text states: "The canonical-mask direct-MC l = 1 value of +3.64σ and the local hemisphere maximum of 3.05σ were interpreted in earlier paper versions as mask-geometric leakage...". This is unprofessional and unacceptable for a formal publication. The paper should be a …
- **[Gemini_cosmology/P4-M1/MAJOR]**: **P4-M1: Inconsistent interpretation of the +3.64σ canonical-mask residual** *   **Location:** Page 1, Abstract and main text. *   **Problem:** The abstract states the "+3.64σ canonical-mask residual is consistent with monopole leakage... and is not interpreted as a cosmological signal." However, the text on the same page states this result is from a test "under proper galaxy-weighted monopole sub…
- **[Gemini_cosmology/P4-N1/NIT]**: **P4-N1: Placeholder contact information** *   **Location:** Page 1, footnote. *   **Problem:** The contact email `houston@hubify.com` appears to be a placeholder. *   **Required Fix:** Provide a stable, professional contact email for the corresponding author.  ## Summary recommendation
- **[Grok_brutal/P4-E1/UNKNOWN]**: **P4-E1 (ESSENTIAL)**   Section: Abstract (p. 1) and Table I (p. 4)   Problem: Multiple \(\sigma\) values obtained from qualitatively different null procedures (isotropic bootstrap, pp-shuffle, binomial monopole-only, max-stat MC) are placed side-by-side in the abstract, Table I, and Sec. IV C without the explicit qualifier “not directly comparable” appearing at every juxtaposition. The single not…
- **[Grok_brutal/P4-M2/UNKNOWN]**: **P4-M2 (MAJOR)**   Section: Sec. IV D and Appendix D (pp. 4–5, 8)   Problem: The generative monopole-only null is asserted to reproduce “99.3 % of the observed pre-MASTER pseudo-\(C_\ell\) power,” yet the binomial draws are performed on the exact canonical mask geometry that already contains the survey-depth gradient under test. This is circular.   Required fix: Repeat the null test on randomized…
- **[Grok_brutal/P4-N1/UNKNOWN]**: **P4-N1 (MINOR)**   Section: Title page (p. 1)   Problem: Date “June 2026” appears in a manuscript under review in 2024/2025.   Required fix: Remove or correct the date.
- **[OpenAI_methodology/P4-E3/ESSENTIAL]**: P4-E3 Sec. VI A, p. 6 (“Fisher Poisson floor at 3 σ is ∼ 0.29 % … σ(A/2)≈0.048 %”)     • Problem For N=3 201 160 and p=0.5 the standard error on     the mean asymmetry is 0.0279 %, not 0.048 %.  A 3 σ     detection threshold is therefore ≈ 0.167 %, not 0.29 %.     • Required fix Re-derive the Fisher lower bound, display     the algebra, and correct both quoted numbers.
- **[OpenAI_methodology/P4-E4/ESSENTIAL]**: P4-E4 Sec. IV C a, p. 4 (“Simple dipole … significance 0.43 σ”)     • Problem Only the significance is given; the dipole     amplitude (Δf_CW), its uncertainty and the direction     (in Galactic or equatorial coordinates) are not     reported, yet later sections rely on this value.     • Required fix Quote the fitted dipole amplitude,     1-σ error bar, and the dipole axis in a reproducible     co…
- **[OpenAI_methodology/P4-M1/MAJOR]**: P4-M1 Sec. A, p. 7: statement that monopole subtraction “increases σ from +1.85 to +3.64” although the amplitude decreases.  This requires an explicit explanation of why σ_null shrinks by > (3.64/1.85)² ≈ 3.9 between the two runs; otherwise the change is unintuitive.
- **[OpenAI_methodology/P4-M2/MAJOR]**: P4-M2 Table I, p. 4: the “Null” column mixes “pp-shuffle”, “label-shuffle”, “isotropic bootstrap” and “monopole-only” but the algorithms are not defined anywhere.  Provide precise definitions (what quantity is shuffled, whether shuffles are within-pixel or global, etc.) and the seeds.
- **[OpenAI_methodology/P4-M3/MAJOR]**: P4-M3 Sec. IV D: the claim that the monopole-only null “reproduces 99.3 % of the observed amplitude” is hard to audit because the definition of “amplitude” (pseudo-C_ℓ, un-binned, or band-power?) is not repeated here.  Spell out the exact statistic and show the single-number ratio.
- **[OpenAI_methodology/P4-M5/MAJOR]**: P4-M5 The paper is 10 text-dense pages plus five appendices but contains only one primary scientific result (the null dipole).  A reduction to ≲ 7 PRD pages would improve clarity.  -------------------------------
- **[OpenAI_methodology/P4-m4/MINOR]**: P4-m4 p. 8, App. C, part d: minus sign missing before “0.03 σ”.
- **[OpenAI_methodology/P4-m5/MINOR]**: P4-m5 Reference [12] year incorrect – Dosovitskiy et al. (2021 not 2020).  --------------------- NITS  – cosmetic only ---------------------
- **[OpenAI_methodology/P4-n1/MINOR]**: P4-n1 p. 1, PACS numbers out of date; PRD now uses “Physics Subject Headings”.
- **[OpenAI_methodology/P4-n2/MINOR]**: P4-n2 Several inline URLs break across lines without \url{} wrapping (pp. 2 and 9).  ---------------------------------------------------------------- ## Summary recommendation
- **[Perplexity_citations/P4-E3/UNKNOWN]**: P4-E3 (ESSENTIAL)   Section: Throughout, but especially Abstract and Sec. IV A–C, pages 1–5   Problem: The abstract quotes several quantitative results (e.g., “5,547,858”, “fsky = 0.659”, “−0.122σ”, “+0.43σ (p = 0.30)”, “pglobal_CW = 0.4974”, “500-MC”, “NMC = 10,000”, “3.64σ”, “pMC = 0.030”, “∼ 1.7%”, “r = −0.65 with σ = −2.89”, amplitude ≥ 0.75% threshold) and calls them headline findings, per th…
- **[Perplexity_citations/P4-E4/UNKNOWN]**: P4-E4 (ESSENTIAL)   Section: Data availability, Appendix E, page 9   Problem: The URLs in the Data Availability section appear inconsistent with the earlier description of the parent sample and catalog:  - The main text (Sec. II A) states the parent sample is “Smith42/galaxies” on HuggingFace.   - The Data Availability section gives “https://huggingface.co/datasets/bamfai/galaxy- chirality- catalo…
- **[Perplexity_citations/P4-M2/UNKNOWN]**: P4-M2 (MAJOR)   Section: VII Conclusions, item (d), page 7   Problem: The statement “A future survey detecting a chirality dipole at σ > 5 with amplitude ≳ 0.75% at ≥ 10^7 galaxies would falsify the present null” is too strong, given that the present null is conditional on specific analysis choices (DESI Legacy footprint, ViT-Small classifier, TTA protocol, monopole subtraction, and null procedure…
- **[Perplexity_citations/P4-M5/UNKNOWN]**: P4-M5 (MAJOR)   Section: Sec. II A “Galaxy Images”, page 2   Problem: The description “Smith42/galaxies dataset on HuggingFace (… 8,474,688 galaxy images)” is specific enough that readers may assume this is a stable, published dataset with fixed contents. As a citation forensics auditor, I cannot verify that such a dataset exists under that exact name, and there is no conventional astronomical pub…
- **[Perplexity_citations/P4-M6/UNKNOWN]**: P4-M6 (MAJOR)   Section: AI tool usage (end of paper), page 9   Problem: The paper states “AI tool usage: Large-language-model tools were used for code review and manuscript editing; all scientific results are derived from the authors’ own analysis and the cited public datasets.” PRD currently has evolving policies about LLM usage and may require explicit disclosure of which models, what version, …
- **[Perplexity_citations/P4-N1/UNKNOWN]**: P4-N1 (MINOR)   Section: Title, page 1   Problem: The title contains an en-dash-like minus symbol in “A −0.122σ Subsample-Mask ℓ = 1 Null,” which may not survive all journal typesetting pipelines correctly and could be rendered inconsistently.   Required fix: Replace “−0.122σ” with plain ASCII “-0.122σ” in the title or ensure that the minus sign is the journal’s preferred Unicode minus in all inst…
- **[Perplexity_citations/P4-N4/UNKNOWN]**: P4-N4 (MINOR)   Section: Data availability and throughout, pages 2–9   Problem: The manuscript uses a mix of styles for survey names and dataset references, e.g., “DESI Legacy Imaging Surveys DR8” vs “DESI Legacy Survey” vs “DESI Legacy imaging”. Similarly, “Galaxy Zoo DESI predictions catalog” vs “Galaxy Zoo DESI”. This inconsistency can make citation forensics and future searches harder.   Requi…
- **[Perplexity_citations/P4-N5/UNKNOWN]**: P4-N5 (NIT)   Section: Sec. III C, Eq. (2), page 3   Problem: The use of the half-factor is written as “12” instead of an explicit 1/2, which may be a typographical artifact of PDF text extraction (“12 PCW^orig” rather than “½ P_CW^orig”). While a reader can infer the intent, it is not typographically correct.   Required fix: Ensure that in the LaTeX source the factor is clearly typeset as 1/2 (e.…
- **[Perplexity_citations/P4-N6/UNKNOWN]**: P4-N6 (NIT)   Section: Appendix D, boundary-distance variance check, page 8   Problem: The phrase “signal is NOT a positive detection…” uses all caps “NOT”, which is stylistically informal for PRD and could be toned down.   Required fix: Replace “NOT” with italic emphasis (“not”) or rephrase the sentence in standard formal style.  ---  Length and focus assessment
- **[Perplexity_citations/P4-M7/UNKNOWN]**: P4-M7 (MAJOR)   The paper is 10 pages, with substantial space devoted to appendices detailing NaMaster configuration, classifier training, and systematic diagnostics. Given the claimed main contribution—a null ℓ=1 chirality-dipole measurement and identification of a monopole–mask leakage channel—the length is borderline but defensible. However, parts of Appendices C–E read as extended narrative ra…
