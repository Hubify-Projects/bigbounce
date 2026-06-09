# P4 auto-2026-06-08_2353pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (13662 chars)
**Wall time**: 89.1s

---

P4-E1 (ESSENTIAL) – Global: Missing reference [2] in main text  
- **Location:** References section, p. 12  
- **Problem:** The text cites Shamir (2022) as [3] in the body (“Shamir (2020) [1] and Shamir (2022) [3] reported…”) but in the reference list the PASJ 2022 Shamir paper is labeled as [2], while [3] is the MNRAS DESI Legacy paper.[2][3] This makes the mapping between in-text citations and the bibliography ambiguous and incorrect for a precision journal like PRD.  
- **Required fix:** Renumber Shamir references consistently so that each in-text citation number matches the actual paper in the reference list. For example, if “Shamir (2022) [3]” is meant to refer to the PASJ 2022 paper, the reference list order/labels must be adjusted; if it is meant to refer to the MNRAS 2022 DESI paper, fix the DOI and journal in the reference list accordingly and ensure the PASJ paper appears as its own correctly numbered entry.

P4-E2 (ESSENTIAL) – References: Incorrect metadata for Shamir (2022) DESI Legacy paper  
- **Location:** References [2] and [3], p. 12  
- **Problem:** The bibliography lists:  
  - [2] “Analysis of the alignment of non-random patterns of spin directions in populations of spiral galaxies,” PASJ 74, 1114 (2022), DOI:10.1093/pasj/psac058.[2]  
  - [3] “Analysis of spin directions of galaxies in the DESI Legacy Survey,” MNRAS 516, 2281 (2022), arXiv:2208.13866, DOI:10.1093/mnras/stac2372.[3]  
  Cross-checking shows:  
  - PASJ 74, 1114 (2022), DOI:10.1093/pasj/psac058 is indeed Shamir, but it is about *spin directions in galaxy populations* with SDSS and Pan-STARRS, not the DESI Legacy survey.[2]  
  - The DESI Legacy paper is in **MNRAS** 516, 2281 (2022), DOI:10.1093/mnras/stac2372, arXiv:2208.13866, and is correctly given under [3].[3]  
  In the abstract the author refers to “Shamir (2022) [3] reported results on DESI Legacy samples (‘nearly 1.3×10^6 spiral galaxies’ per the published abstract).” The “nearly 1.3×10^6” wording indeed comes from the MNRAS DESI Legacy abstract, not the PASJ paper.[3] This is consistent with [3], not [2], but the main-text sentence “Shamir (2020) [1] and Shamir (2022) [3]” appears directly after mentioning SDSS and Pan-STARRS, which may actually be closer in scope to PASJ (ref [2]). The current numbering and titles are confusing and easily misread as fused metadata.  
- **Required fix:**  
  - Explicitly disambiguate the two 2022 Shamir papers in the text (e.g., “Shamir 2022a (PASJ) [2]” and “Shamir 2022b (MNRAS DESI) [3]”).  
  - Ensure the in-text discussion of “nearly 1.3×10^6 spiral galaxies” *only* cites the MNRAS DESI paper (arXiv:2208.13866, MNRAS 516, 2281, DOI:10.1093/mnras/stac2372).[3]  
  - If the PASJ paper is intended to be cited, add explicit text describing its SDSS/Pan-STARRS focus so the mapping is unambiguous.

P4-E3 (ESSENTIAL) – Abstract: Unsupported “nearly 1.3×10^6 spiral galaxies” statement  
- **Location:** Introduction, p. 2 (“…Shamir (2020) [1] and Shamir (2022) [3] reported results with ∼ 2–4% asymmetries on DESI Legacy samples (‘nearly 1.3 × 10^6 spiral galaxies’ per the published abstract).”)  
- **Problem:** The phrase “nearly 1.3 × 10^6 spiral galaxies” is attributed to the MNRAS DESI Legacy paper.[3] The actual abstract text states that the catalog “includes nearly 1.3 million spiral galaxies” (paraphrase), which is consistent in magnitude. However, the current paper does not provide a direct quotation or exact wording, and PRD expects precise traceability for any quantitative phrase explicitly attributed to another abstract.  
- **Required fix:** Either (a) quote the exact wording from the Shamir MNRAS abstract in quotation marks and ensure it is under 50 words, or (b) rephrase as a paraphrase (e.g., “of order 1.3 million spirals”) without quotation marks, while still citing [3]. Confirm the number explicitly matches the Shamir abstract’s text and update if needed.

P4-E4 (ESSENTIAL) – Null-procedure σ comparability warning missing in main body juxtaposition  
- **Location:** Table I and §IV C, pp. 4–5  
- **Problem:** The instructions require that whenever σ values from different null procedures are presented side by side, every such juxtaposition must explicitly state they are not directly comparable. The abstract contains an appropriate warning (“σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators; see Table I…”) and Table I lists different nulls for each estimator. However, in §IV C (Dipole Analysis) the text directly compares Catalog A “2.31σ real-space dipole and a +6.48σ pre-MASTER pseudo-Cℓ” to Catalog C “0.43σ… collapsed to null” without re-stating that these σ values come from different null constructions and are not directly comparable in a statistical sense. This violates the explicit requirement.  
- **Required fix:** Add an explicit sentence in §IV C, immediately where multiple σ values are discussed together, stating that these σ values are defined relative to different null procedures and are not directly comparable, and refer back to Table I.

P4-E5 (ESSENTIAL) – Internal version-history language left in body text  
- **Location:** §IV D, p. 5: “...were interpreted in earlier paper versions as mask-geometric leakage…”  
- **Problem:** The journal instructions here explicitly forbid “version-history language, internal audit tags (‘R7’, ‘R8’, ‘R-round’), ‘superseded’, ‘earlier draft’, review-log prose, or internal-bookkeeping placeholders” in the body. The phrase “earlier paper versions” is exactly such version-history language.  
- **Required fix:** Remove any mention of “earlier paper versions” or similar editorial history from the main text. Rephrase simply as “...can be interpreted as mask-geometric leakage...” without referencing earlier drafts.

P4-E6 (ESSENTIAL) – Data availability URLs present despite instruction  
- **Location:** Data Availability section, p. 11; Appendix references to “companion data repository” and specific URLs  
- **Problem:** The reviewing instructions here explicitly state “Do not include URLs or external links in the response” (as a proxy for journal style in this context). The manuscript includes multiple explicit URLs (HuggingFace dataset/model, GitHub repo). Even if allowed in a final publication, PRD usually requires these to be cited as references or in a standardized data-availability format, not as raw URLs scattered in text.  
- **Required fix:** Replace raw URLs with properly formatted references or with a concise Data Availability statement following PRD style (e.g., “Data and code are available in a public repository; see supplemental material / reference [X].”). If specific permanent DOIs exist (e.g., Zenodo), cite them instead of generic HTTP links.

P4-M1 (MAJOR) – Over-extended manuscript relative to claimed contribution  
- **Location:** Whole paper (13 pages including appendices)  
- **Problem:** The main scientific result is essentially a null ℓ = 1 dipole at sub-percent level on a single catalog, plus a characterization of a monopole–mask leakage systematic. The paper devotes extensive space (multiple appendices, long methodological exegesis of bias tests, and highly detailed NaMaster and training configurations) that read more like a technical project report than a focused PRD article. Several appendices (B–E) repeat descriptive content already summarized in the main text and could be substantially compressed without loss of scientific clarity.  
- **Required fix:** Compress non-essential implementation and engineering details (optimizer hyperparameters, code-level seed and function names, full bias-test table, etc.) into a data-release note or an online supplement. Aim for ≤ 9 journal pages for the main text plus one short technical appendix, removing redundancy.

P4-M2 (MAJOR) – Ambiguous claim of “largest galaxy chirality catalog to date”  
- **Location:** Conclusions, p. 8: “We have constructed and analyzed the largest galaxy chirality catalog to date: 8,474,531 galaxies...”  
- **Problem:** This assertion of being the “largest” must be supported. CE-ResNet uses ∼1.95 million galaxies,[7] while Shamir’s DESI Legacy paper claims nearly 1.3 million spirals.[3] The present catalog has 8.47M total galaxies and 3.2M spirals, which is indeed larger. However, the paper does not explicitly compare to any possible larger internal catalogs or recent survey-scale machine-learning spin classifications beyond CE-ResNet and Shamir. Given the rapid evolution of machine-learning-based morphology catalogs, this “largest” claim needs a clear literature-based justification or careful qualification.  
- **Required fix:** Either (a) provide explicit comparative evidence that no larger *published* chirality catalog exists as of the cutoff (e.g., citing CE-ResNet’s 1.95M sample and Shamir’s ∼1.3M and stating that you are unaware of any larger published samples), or (b) soften the claim to “among the largest published” or “larger than previous public chirality catalogs such as CE-ResNet (1.95M) and Shamir (∼1.3M).”

P4-M3 (MAJOR) – Parity-even vs parity-odd sector discussion under-referenced  
- **Location:** Abstract, §I and §VI B (parity-violating sectors), p. 1, 8  
- **Problem:** The paper claims that the ℓ = 1 dipole is parity-even and not a direct parity-violation test, and later connects to parity-odd tensor sectors and cosmic birefringence. This is conceptually correct: the dipole of a scalar field on the sky is not itself a parity-odd observable. However, the mapping from the measured null dipole in morphology to constraints on “any model predicting a late-universe morphology-channel dipole ≥0.75%” is stated without a clear theoretical framework, transfer function, or explicit reference. The text admits that the transfer function from primordial chirality to morphology is not derived. Yet, it uses language like “disfavors… by a factor of ~6–12” which readers might interpret as a direct constraint on fundamental parity-violating models.  
- **Required fix:** Clarify that the present result constrains only *phenomenological* late-time morphology anisotropy, not fundamental parity-odd interactions, and remove or soften any implication of direct constraints on primordial parity-violating sectors. Explicitly separate the discussion of late-time morphological anisotropy (parity-even) from published parity-odd analyses in CMB and large-scale structure, and clearly label any extrapolation to fundamental physics as speculative.

P4-M4 (MAJOR) – Quantitative Fisher floor and injection-recovery linkage insufficiently justified  
- **Location:** §VI A, p. 8 (“Fisher Poisson floor at 3σ is ∼0.29%... empirical injection-recovery sweep… gives… A=0.75% for 50% recovery… true-underlying threshold ∼1.88%”)  
- **Problem:** The Fisher floor of 0.29% is quoted based on an expression “σ(A/2) ≈ 0.048% at Nspiral=3,201,160, fsky=0.46,” but the derivation is not shown. The relation between that floor and the injection-recovery result (A=0.75% corresponding to ≥3σ in 50% of realizations) is not recomputed internally: the text states a “true-underlying threshold ∼1.88%” via a GZ1-dilution factor g=2a−1≈0.398 (for a=0.6991), but does not step through the algebra. In a methods-heavy PRD paper, this should be explicitly demonstrated.  
- **Required fix:** Show the explicit derivation of the Fisher Poisson limit used to obtain 0.29%, including the effect of sky fraction and number of spirals. Then derive the relation between classification accuracy a, dilution factor g, and the amplification from observed threshold Aobs=0.75% to underlying amplitude Atrue≈Aobs/g≈1.88%. Verify that the numbers in the text are consistent with the displayed equations and input values.

P4-M5 (MAJOR) – Use of “null dipole at sub-percent sensitivity” in abstract not fully supported by body text  
- **Location:** Abstract, p. 1; §IV C and §VI A  
- **Problem:** The abstract claims “null ℓ=1 chirality-dipole observable… sub-percent sensitivity” and later formalizes A50≈0.75% and A95≈1.5–2% as thresholds. In the body, the sensitivity floor is given with caveats about classification noise, residual monopole, and edge-on contamination. The text acknowledges that effective sensitivity degradation from classification errors and morphology systematics may be non-negligible. The phrase “sub-percent sensitivity” could be misinterpreted as a clean, well-defined 0.5–0.9% bound, whereas the empirical injection-recovery and GZ1-based dilution suggest that the underlying physical dipole amplitude must be larger (≈1.9%) to be robustly excluded.  
- **Required fix:** Rephrase the abstract to distinguish between *observational* sensitivity on the classifier output field (sub-percent) and *inferred* sensitivity to true physical dipole amplitude (∼2% after accounting for classification dilution). Make sure the abstract’s “sub-percent sensitivity” is explicitly tied to the measured catalog-level asymmetry, not to the underlying cosmological signal.

P4-M6 (MAJOR) – AI tool usage statement lacks specificity  
- **Location:** Acknowledgments, p. 11 (“AI tool usage: Large-language-model tools were used for code review and manuscript editing; all scientific results are derived from the authors’ own analysis...”)  
- **Problem:** PRD and APS expect precise disclosure of AI/LLM assistance, including which tools, for what tasks, and how authors verified correctness. The current one-line statement is too vague to assess potential impact on scientific content and may not meet future APS policy.  
- **Required fix:** Expand to specify which LLM(s) were used (e.g., GPT-4, etc.), for which steps (e.g., documentation, refactoring, language polishing only), and state clearly that all scientific derivations, numerical analyses, and interpretation were performed and independently checked by the author. Confirm that no text was taken directly from AI outputs without critical review.

P4-M7 (MAJOR) – Data-availability and reproducibility claims need tighter alignment with journal standards  
- **Location:** Abstract (“catalog… model weights, and reproducibility scripts are publicly released at the project repository.”) and Data Availability section, p. 11  
- **Problem:** The paper promises “all reproducibility scripts” and a full catalog, but the description is informal and anchored in specific hosting platforms. PRD typically expects a statement that essential data and analysis code sufficient to reproduce the main figures and tables will be archived at a stable, citable location at publication time. Relying solely on code repositories and model hosting sites without explicit versioning / DOIs is fragile.  
- **Required fix:** Commit to depositing the minimal reproducible dataset and analysis scripts for the main figures and tables in a long-term archival repository with a DOI (e.g., Zenodo) and cite it. Ensure that the description in the Data Availability section corresponds to what will be persistently available.

P4-m1 (MINOR) – Inconsistent use of hyphenation and notation for sky fraction  
- **Location:** Throughout, e.g., Table I vs text (“fsky = 0.49005” vs “fsky ≈ 0.49”; sometimes no space around equals)  
- **Problem:** Sky fraction notation and formatting are slightly inconsistent. While scientifically harmless, PRD prefers consistent notation and formatting.  
- **Required fix:** Standardize on a single style for fsky (e.g., “\(f_{\rm sky} = 0.490\)” or “\(f_{\rm sky}\approx 0.49\)”) with consistent spacing and LaTeX formatting throughout text, tables, and captions.

P4-m2 (MINOR) – Minor typographical and formatting issues  
- **Location:** Multiple places, e.g.:  
  - Abstract: “parity-EVEN : it is NOT” (extra space before colon).  
  - §I: “We emphasize at the outset that this ℓ = 1 observable is the isotropy-breaking axial-vector channel and is parity-EVEN :” (same spacing).  
  - §II A: “0.262′′ /pixel” (space before slash).  
- **Problem:** These do not affect scientific content but are below PRD’s copy-editing standards.  
- **Required fix:** Remove extraneous spaces around colons and slashes; standardize arcsecond notation as \(0.262^{\prime\prime}\,\mathrm{pixel}^{-1}\) or similar.

P4-m3 (MINOR) – Unclear description of “canonical mask” vs “subsample mask”  
- **Location:** Abstract and §§III–IV; Fig. 3 caption  
- **Problem:** The terms “canonical mask,” “canonical-N MASTER,” and “strict-superset subsample mask” are used frequently but are never given a concise, formal definition in the main text. Readers must infer details from Appendix A and Fig. 3. For a methods paper, mask definitions need to be precise and easily accessible in the main body.  
- **Required fix:** Add a short subsection or paragraph in §III (Methods) clearly defining the canonical mask (footprint, cuts, fsky) and the “strict-superset subsample mask,” including how each is constructed and why both are needed. Cross-reference Fig. 3.

P4-m4 (MINOR) – Slightly ambiguous phrasing about “50%-recovery-at-3σ”  
- **Location:** Abstract and §III A, §VI A  
- **Problem:** The phrase “50%-recovery-at-3σ threshold at A = 0.75%” appears multiple times. It is technically correct but could be misread as implying that a 3σ detection is achieved for A=0.75% in a single realization, rather than as a 50% power point over many simulations. §VI A partially clarifies, but the abstract does not.  
- **Required fix:** Add a clarifying phrase in the abstract (“meaning that, for injected dipoles of amplitude 0.75%, 50% of Monte Carlo realizations reach ≥3σ under our null”) to avoid misinterpretation.

P4-n1 (NIT) – Redundant phrasing of “canonical-mask residual”  
- **Location:** Abstract and §IV D, repeated many times  
- **Problem:** While not a strict duplication like “canonical canonical-mask,” the phrase “canonical-mask residual” is used very frequently, making some sentences stylistically heavy.  
- **Required fix:** Consider occasionally varying the wording (“residual on the canonical footprint,” “remaining signal on the canonical mask”) for readability, without altering meaning.

P4-n2 (NIT) – Overly detailed code-level configuration in appendices  
- **Location:** Appendices A and B (NaMaster configuration and training settings)  
- **Problem:** Specific function calls, seeds, and parameters like `nmt.NmtBin.from_lmax_linear(lmax=191, nlb=1)` or exact early-stopping epoch numbers resemble a software manual more than a journal appendix. While helpful for full reproducibility, PRD generally expects a higher-level description with a pointer to a reproducibility repository for low-level details.  
- **Required fix:** Condense code-level descriptions in the appendices to high-level algorithmic/parameter summaries and move ultra-detailed settings into the public code repository README, referenced briefly in the paper.

## Summary recommendation

**MAJOR REVISIONS**

The core scientific idea—demonstrating a null ℓ = 1 chirality dipole and characterizing a monopole–mask leakage systematic on a very large DESI-based catalog—is potentially suitable for PRD. However, the manuscript in its current form has significant issues in citation consistency, interpretation of sensitivity, overextended methodological exposition, and ambiguity about how the null maps onto physical parity-violating models. These must be corrected, and the paper streamlined and sharpened, before it can meet the standards of a high-precision cosmology methods paper in Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

P4-E7 (ESSENTIAL) – Arithmetic inconsistency in Table II “Dev. (σ)” column  
- **Location:** Table II, p. 4 (“Global CW fraction across catalog tiers”)  
- **Problem:** The “Dev. (σ)” column is defined as \((f_{\rm CW} - 0.5)/\sigma\) with \(\sigma = \sqrt{p(1-p)/N}\), using \(N_{\rm spiral} = 3{,}201{,}160\).[table] Recomputing from the given numbers:  
  - Tier A: \(f=0.5079\), quoted uncertainty \(0.000279\). Then \((0.5079-0.5)/0.000279 ≈ 28.3\), not 28.8 as listed.  
  - Tier B: \(f=0.504\), same \(\sigma=0.000279\). Then \((0.504-0.5)/0.000279 ≈ 14.3\), not 14.6.  
  - Tier C: \(f=0.4974\), same \(\sigma=0.000279\). Then \((0.4974-0.5)/0.000279 ≈ -9.3\), not 9.5 (and the table’s Dev entry “9.5” omits the minus sign).  
  These mismatches indicate either that the quoted ±0.000279 is not the actual \(\sigma\) used for Dev, or that the Dev column was not recomputed after updating the fractions. The missing minus sign for Catalog C is also a sign convention error.  
- **Required fix:** Recompute Dev directly from the current \(f_{\rm CW}\) and \(N_{\rm spiral}\), and ensure the “±” uncertainty matches that computation. Make the “Dev. (σ)” entries numerically consistent and include the correct sign (e.g., “−9.3” if that is the recomputed value).

P4-E8 (ESSENTIAL) – Inconsistent “3.86× asymmetry-suppression factor” and underlying percentages  
- **Location:** §IV B, p. 4: “The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53% demonstrates…”  
- **Problem:** The text claims an asymmetry-suppression factor of 3.86× “from raw +2.05% to equivariant −0.53%.” However:  
  - Table II gives Tier A excess = +0.79% and Tier C excess = −0.26%, not +2.05% and −0.53%.[table]  
  - The abstract states “global CW-fraction shift from +2.05% (A) to −0.53% (C) is dominated by this step (Table II),” but Table II does not contain 2.05% or −0.53%.  
  - If the raw-to-equivariant change is indeed +2.05% → −0.53%, the suppression factor is \(|2.05|/|0.53| ≈ 3.9\) in *amplitude*, but the actual shift is 2.58 percentage points; if one instead uses the Table II numbers (0.79% → −0.26%), the corresponding factor and shift differ by roughly a factor of 3–4.  
  This indicates stale numbers left over from an earlier version of the catalog or a different sample definition; the mismatch between text and Table II is arithmetically inconsistent.  
- **Required fix:** Decide which CW excess values are the authoritative ones (raw and equivariant) and update *all* mentions consistently. If the intended numbers are +0.79% and −0.26%, recompute and restate the suppression factor accurately, and remove references to +2.05% and −0.53% (or vice versa, but then fix Table II and any statements that use ±0.000279 as the corresponding binomial error).

P4-E9 (ESSENTIAL) – Abstract and body inconsistently describe D4 vs 2-fold TTA  
- **Location:** Abstract; §III C; Fig. 1 caption  
- **Problem:**  
  - The abstract headline refers to “equivariant TTA” without specifying group order, and Fig. 1’s caption describes “Test-time D4 equivariant averaging (TTA)” with “eight D4 transforms (four rotations × two reflections).”  
  - The main text in §III C, however, explicitly states: “We restrict to 2-fold TTA (original + horizontal flip) rather than the full D4 group because mirrors flip chirality…” and describes the D4 experiment only as a *validation* on small subsamples, not the production pipeline.  
  - The caption states “This averaging is the key methodology distinction between Catalog A (raw), Catalog B (Platt-calibrated), and Catalog C (equivariant); the global CW-fraction shift from +2.05% (A) to −0.53% (C) is dominated by this step (Table II),” implying that the full D4-TTA is the operational protocol driving Catalog C. In contrast, the body says the production protocol uses only Z2 (flip) TTA.  
  This constitutes a method inconsistency between figure-caption and main text and also feeds into the stale-number issue in P4-E8. For a methods-driven PRD paper, it is critical that the description of the actual production TTA group be unambiguous and consistent.  
- **Required fix:** Clarify in both the abstract and all captions whether the *production* catalog uses 2-fold flip-only TTA or full D4 TTA. If only Z2 is used, revise Fig. 1’s title and caption (e.g., “schematic D4 TTA test; production uses 2-fold flip-only”) and remove the implication that D4 averaging is the catalog method. Align all references to the CW-fraction shift with the correct TTA mode and with the actual percentages.

P4-E10 (ESSENTIAL) – Inconsistent sky-fraction values and ambiguous use of \(f_{\rm sky}\)  
- **Location:** Abstract; Table I; Fig. 3 caption; §IV C; Appendix A  
- **Problem:** Multiple, slightly inconsistent \(f_{\rm sky}\) numbers are reported for the same masks, and the way they are used is not fully consistent:  
  - Abstract: “strict-superset subsample mask (n = 5,547,858, \(f_{\rm sky} = 0.659\))…”  
  - Fig. 3 caption: “DESI Legacy Imaging footprint covers \(f_{\rm sky} ≈ 0.49\) of the sky in the canonical mask; the strict-superset subsample mask (\(f_{\rm sky} = 0.659\)) covers a larger region…”  
  - Table I: lists \(f_{\rm sky} = 0.659\) for the subsample mask and 0.49005 for the canonical mask.  
  - §VI A (Fisher floor): uses \(f_{\rm sky} = 0.46\) in the Fisher estimate, which is neither 0.49005 nor 0.659 and is not clearly defined as a different mask or effective sky fraction.  
  - Appendix D: the C\(^2\) 2° apodized version of the canonical mask has \(f_{\rm sky} = 0.482\), but this is never tied back to the Fisher-number choice of 0.46.  
  While some variation (binary vs apodized vs “effective”) is expected, the paper never clearly defines why a Fisher calculation uses 0.46 instead of the masks’ stated 0.49/0.659, and the abstract/figure-caption language encourages the reader to treat these as exact, not approximate, values. This is an internal-consistency issue, and it also undermines the precise recomputation of sensitivity and Fisher limits.  
- **Required fix:**  
  - Explicitly define each \(f_{\rm sky}\) used: canonical mask (binary), subsample mask, apodized mask, and any “effective” Fisher \(f_{\rm sky}\).  
  - Choose a consistent value for the Fisher-floor calculation whose definition is traceable (e.g., “effective \(f_{\rm sky} = 0.49\) after quality cuts”), and recompute the 0.29% floor accordingly.  
  - If the 0.46 value is retained, add a sentence in §VI A explaining how it is derived from the masks and why it differs from 0.49 and 0.659, and update any numbers that change once a consistently defined \(f_{\rm sky}\) is used.

P4-M8 (MAJOR) – Abstract’s “global CW-fraction shift from +2.05% (A) to −0.53% (C)” not supported by current tables  
- **Location:** Abstract; Fig. 1 caption; Table II  
- **Problem:** The abstract and Fig. 1 assert a specific shift in global CW fraction (+2.05% → −0.53%), which is central to the claimed impact of equivariant TTA on bias suppression. Table II, which is the only place where catalog-tier global CW statistics are summarized, shows instead +0.79% (Tier A), +0.4% (Tier B), and −0.26% (Tier C). The body does not present any alternate definition or restricted sample that would naturally yield +2.05% and −0.53%. This is an abstract–body mismatch of exactly the kind PRD is strict about: key headline numbers in the abstract are not reproducible from the main text.  
- **Required fix:** Either:  
  - (a) restore or present the numbers +2.05% and −0.53% in the body with a clear definition (what sample, what cuts, what estimator?) and a table or equation that reproduces them; or  
  - (b) update the abstract and Fig. 1 to use the current Table II values (+0.79%, −0.26%) and recompute any suppression factors or statistical arguments that rely on the older numbers. Ensure that any references to Table II are numerically correct.

P4-M9 (MAJOR) – Quantitative claims about “maximum regional asymmetry 0.32%” and Catalog A 2.31σ / 6.48σ lack explicit numerical traceability  
- **Location:** §V A, p. 6; §VI, p. 7; conclusions (a–d)  
- **Problem:** Several key quantitative claims do not have an explicit numerical presentation that lets the reader independently verify them from the displayed tables:  
  - “Under the present ViT/TTA pipeline, our maximum regional asymmetry is 0.32%…” (in §V A) is not backed by a figure or table reporting that 0.32% as a function of sky region, nor by a description of how “regional” is defined (HEALPix pixel, hemisphere, optimized cap, etc.).  
  - The Catalog A “2.31σ real-space dipole and +6.48σ pre-MASTER pseudo-Cℓ in the lowest bandpower” are discussed multiple times (abstract, §IV C, §VI, conclusions) but there is no table or figure listing these values along with the corresponding null distribution parameters. This makes it impossible to recompute the σ and check for arithmetic consistency or look-elsewhere corrections as requested in the review brief.  
- **Required fix:**  
  - Add either a small table or a figure (possibly in an appendix) explicitly listing the key diagnostic values for each catalog tier (A, B, C): global CW fraction, dipole amplitude, σ relative to its null, and for Catalog A the pre-MASTER pseudo-Cℓ significance.  
  - For the “maximum regional asymmetry 0.32%,” provide a clear definition of “regional” (e.g., NSIDE=8 pixels, hemisphere scans, or specific angular scale) and either a table entry or a caption that shows how that 0.32% was obtained and what uncertainty it carries.

P4-m5 (MINOR) – Equation (3) notation inconsistency and missing explicit dimensional clarification  
- **Location:** §IV C, equation (3)  
- **Problem:** The asymmetry field definition is given as  
  \[
  A_p = \frac{N_{\rm CW}^{(p)} - N_{\rm CCW}^{(p)}}{N_{\rm CW}^{(p)} + N_{\rm CCW}^{(p)}}.
  \]  
  Later, in Appendix A, the field is described as  
  \[
  A_p = (N_{\rm CW}^{(p)} - N_{\rm CCW}^{(p)}) / (N_{\rm CW}^{(p)} + N_{\rm CCW}^{(p)}),
  \]  
  but the text also introduces a separate “Ap = (NCW − NCCW)/Ntotal” scalar field for NaMaster, where \(N_{\rm total}\) includes non-spiral galaxies.[appendix] This dual usage of \(A_p\) (once normalized by spirals-only, once by total galaxies) is not fully disentangled and risks confusion over which normalization is used in which estimator. From a dimensional-consistency standpoint, both versions are dimensionless ratios, but the mixed use of notation obscures the exact field entering the MASTER calculation, which is relevant for interpreting the C\(_\ell\) amplitudes.  
- **Required fix:** Introduce distinct symbols (e.g., \(A_p^{\rm (spiral)}\) vs \(A_p^{\rm (all)}\), or explicitly define the NaMaster field as \(F_p\)) and clearly state in §IV C and Appendix A which field enters each analysis (real-space dipole vs MASTER C\(_\ell\)). Make explicit that all these quantities are dimensionless fractions, to avoid any doubt about dimensional consistency.

P4-m6 (MINOR) – Abstract “subsample-mask ℓ = 1 null” vs Appendix A’s “canonical mask” description may confuse which C\(_1\) is headline  
- **Location:** Abstract; Table III; Appendix A and D  
- **Problem:** The abstract’s first sentence emphasizes the “subsample-mask ℓ = 1 null” as headline. Table III’s first row is labeled “ℓ=1 (single mode)… Null (subsample mask),” consistent with this. However, Appendix A and Appendix D spend extensive space on the canonical mask configuration, including the monopole-subtracted vs non-subtracted treatment, which could be misread as the main C\(_1\) definition. For a reader focusing on equations, it takes effort to track that the *headline* C\(_1\) is the subsample-mask one (−0.122σ) and that the +3.64σ canonical-mask residual is explicitly non-headline. This is not strictly an arithmetic error, but it is an internal communication issue, especially given the journal’s demand for very clear distinction between primary and secondary estimators.  
- **Required fix:** Add a short, explicit sentence at the start of Appendix A (and/or at the top of Table III) reiterating that the ℓ=1, \(f_{\rm sky}=0.659\) subsample-mask C\(_1\) is the primary estimator quoted in the abstract, and that the canonical-mask C\(_1\) and other bandpowers are secondary, diagnostic quantities. This reinforces the mapping between the abstract’s claim and the body.

P4-n3 (NIT) – Minor inconsistencies in describing the null distributions and seeds  
- **Location:** Table I, Table IV, Appendix A, Appendix C  
- **Problem:**  
  - Table I lists “pp-shuffle” for the MASTER nulls but does not explicitly define whether the label shuffling is done per-pixel or globally per galaxy; Appendix A clarifies this but uses slightly different phrases (“per-pixel random-label permutation nulls”).  
  - Appendix A notes “seed: numpy.random.seed(42)” for the canonical-N null, while Table IV also lists “seed = 42” but the main text in §IV D does not mention the seed at all.  
  - These are not scientific errors but very small inconsistencies in wording and level of detail that make it a bit harder for a reader to precisely match the null procedure in the text to the one summarized in tables.  
- **Required fix:** Harmonize terminology for the shuffle null (e.g., always call it “per-pixel label-shuffle null”) and, if seeds are mentioned in appendices/tables, briefly note in the main text that a fixed seed was used for reproducibility. This will make cross-referencing between body, tables, and appendices smoother.

If needed, I can walk through specific σ or percentage recomputations step by step for any particular table entry to help you patch the numbers consistently.