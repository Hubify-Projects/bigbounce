# P2 auto-2026-06-05_1617pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (13840 chars)
**Wall time**: 81.4s

---

P2-E1 (ESSENTIAL) – Abstract & throughout: unverified and likely incorrect ACT DR6 citation  
- **Location:** Abstract p.1; Sec. 1 p.1; Sec. 3.1 p.2; References p.6  
- **Problem:** The paper cites “ACT DR6 [Diego-Palazuelos and Komatsu, 2025]: β = 0.215 ± 0.074° (2.9σ)” and lists in the references “P. Diego-Palazuelos and E. Komatsu. Cosmic birefringence from the Atacama Cosmology Telescope. arXiv preprint, 2025.” I cannot locate any such paper on arXiv or NASA ADS: searches for “Diego-Palazuelos Komatsu cosmic birefringence ACT” and variants return no 2025 birefringence paper by this author pair and no ACT DR6 birefringence analysis with these numbers.[1][2] The ACT DR6 public releases to date and existing birefringence analyses do not match this metadata. This looks like a **non-existent or severely mis-identified** reference.  
- **Required fix:**  
  - Verify whether an ACT DR6 birefringence paper with these authors/results actually exists. If it does, provide the correct arXiv ID, title, and official citation, and ensure the quoted β and uncertainty match that paper’s abstract or tables.  
  - If no such paper exists or results are not yet public, remove this dataset from the analysis and all claims based on it (including the “Planck + ACT” combination, the combined β value, and any σ or ln B derived from it), or clearly mark it as **unpublished/private communication** and do not use it quantitatively in a PRD paper.  
  - Update the references accordingly.  

P2-E2 (ESSENTIAL) – Misuse of Eskilt & Komatsu 2022 results and numeric inconsistency  
- **Location:** Abstract p.1; Sec. 1 p.1; Sec. 3.1 p.2; Sec. 3.3 p.2–3  
- **Problem:**  
  - The paper claims “βobs = 0.342 ± 0.094° from the Eskilt et al. joint Planck + ACT analysis” in the abstract and later refers to “Eskilt et al. joint analysis value βobs = 0.342 ± 0.094°.” However, the reference list only includes Eskilt & Komatsu (Phys. Rev. D 106, 063503, 2022), which is a WMAP+Planck birefringence analysis and **does not** include ACT.[2]  
  - Eskilt & Komatsu 2022 report a best-fit angle of order 0.34° with an uncertainty around 0.09° in some combinations, but that is for WMAP+Planck, not “Planck + ACT.” The text thereby **mislabels the dataset and the experiment combination**.  
- **Required fix:**  
  - Correct all mentions of “Eskilt et al. joint Planck + ACT analysis” to accurately reflect what is in the cited paper (WMAP+Planck).  
  - Explicitly state which exact data combination (e.g., “Planck PR4 + WMAP 9-year,” etc.) the quoted βobs = 0.342 ± 0.094° comes from, and verify that these numbers match the published values in Eskilt & Komatsu 2022 (check abstract/tables and quote exactly).  
  - If βobs = 0.342 ± 0.094° is instead from some other (possibly newer) “Eskilt et al.” analysis, you must cite that paper explicitly with correct metadata, and ensure consistency.  

P2-E3 (ESSENTIAL) – Combined β constraint does not match a correct inverse-variance combination  
- **Location:** Abstract p.1; Sec. 3.2 Eq. (4) p.2  
- **Problem:** From Sec. 3.1 the two inputs are:  
  - Planck NPIPE: β₁ = 0.30 ± 0.11°  
  - ACT (claimed): β₂ = 0.215 ± 0.074°  
  Assuming independence, inverse-variance weighting gives:  
  - σ₁² = 0.11² = 0.0121; σ₂² = 0.074² ≈ 0.00548  
  - σ_combined² = 1 / (1/σ₁² + 1/σ₂²) ≈ 0.0038 ⇒ σ_combined ≈ 0.062°  
  - β_combined = (β₁/σ₁² + β₂/σ₂²) / (1/σ₁² + 1/σ₂²) ≈ 0.244°  
  The paper quotes βcombined = 0.242 ± 0.061° (Eq. 4), which is close but **not exactly** consistent, and since this is a simple analytic combination, the discrepancy must be explained, especially for a PRD-level methods paper.  
- **Required fix:**  
  - Recompute βcombined and its uncertainty, report the precise values (to appropriate significant figures), and show the actual formula used (including any correlations, extra error terms, or rounding conventions).  
  - If additional systematic uncertainties or correlations were accounted for, describe them explicitly and show how they alter the effective σ.  
  - Ensure that the quoted “3.9σ from zero” follows directly from βcombined / σcombined.  

P2-E4 (ESSENTIAL) – Unsupported quote of 3.6σ Planck+ACT significance in abstract vs body  
- **Location:** Abstract p.1; Introduction p.1  
- **Problem:**  
  - Abstract: “consistent with the 3.6σ isotropic birefringence signal (βobs = 0.342 ± 0.094° from the Eskilt et al. joint Planck + ACT analysis).”  
  - Sec. 1 states instead: “Combined, the evidence exceeds 3.5σ.”  
  The 3.6σ / “>3.5σ” claim must be directly traceable to a cited paper. Eskilt & Komatsu 2022 report significances around 3.0–3.3σ depending on data combination, not a 3.6σ Planck+ACT result.[2] Without a specific reference, this is an **unsupported statistic.**  
- **Required fix:**  
  - Identify a specific published analysis that reports a 3.6σ isotropic birefringence detection and cite it with correct metadata, and ensure βobs and σ match that paper.  
  - If no published source exists with 3.6σ, adjust the text to quote the actual σ from the cited paper(s). Do not extrapolate.  
  - Make the abstract’s βobs and σ numerically consistent with what is later used (βobs vs βcombined) and with the cited literature.  

P2-E5 (ESSENTIAL) – Use of “in preparation” and future-dated reference with missing metadata  
- **Location:** References p.6; Sec. 6 p.5  
- **Problem:** The paper cites “Toshiya Namikawa, Kai Murai, and Sho Naokawa. Constraints on axion-like particles from cosmic birefringence. arXiv e-prints, 2025. In preparation; cited for comparison of ALP mass constraints.” There is currently a 2025 arXiv paper “Planck Constraints on Axion-Like Particles through Isotropic Cosmic Birefringence” by Murai et al. (including Namikawa) with arXiv:2506.20824, but the title and author list in this manuscript do not match exactly.[1][2][6] “Sho Naokawa” does not appear in that author list, and the phrase “In preparation; cited…” is not acceptable for PRD references.  
- **Required fix:**  
  - If the intended reference is arXiv:2506.20824, correct the citation to the actual title, author list, and arXiv ID as on arXiv/NASA ADS.[1][2][6]  
  - Remove “In preparation” language; PRD generally does not accept “in preparation” as a primary reference for quantitative claims. If the work is genuinely not yet on arXiv, either remove it from the quantitative discussion or clearly mark it as private communication and avoid using its numbers as central inputs.  
  - If instead another future paper is intended, it is **not citable** for quantitative comparison and must be removed or downgraded to a qualitative remark without any specific numeric constraints.  

P2-E6 (ESSENTIAL) – Self-citation of “companion paper” without public identifier  
- **Location:** Sec. 5 p.4; Sec. 6 p.5; References p.6  
- **Problem:** Two companion papers are cited:  
  - “Houston Golden. Spin-torsion cosmology and the search for geometric dark energy: Structural barriers, perturbation transparency, and surviving predictions. Companion paper, submitted simultaneously, 2026a.”  
  - “Houston Golden. Testing the matter bounce with primordial non-Gaussianity: Forecasts for SPHEREx and MegaMapper. Companion paper, submitted simultaneously, 2026b.”  
  Neither has an arXiv ID, DOI, or journal reference. They are used in the main text: Sec. 5 refers to “the companion paper [Golden, 2026a] for the full ECH framework and 14-barrier catalog” and Sec. 6 invokes “The matter-bounce non-Gaussianity fNL = −35/8 provides a complementary and independent test [Golden, 2026b].” These are **non-public sources** and cannot support load-bearing claims in a PRD paper.  
- **Required fix:**  
  - Either (a) make these works public (arXiv IDs) before relying on them, and then cite them with proper metadata, or (b) remove any dependence of the current paper’s main scientific claims on unpublished companion work.  
  - If fNL = −35/8 or the “14-barrier catalog” are essential to the narrative, the necessary definitions and arguments must be self-contained here or supported by already published literature. Otherwise, reduce them to brief, clearly-labeled forward-pointing remarks that do not carry argumentative weight.  

P2-E7 (ESSENTIAL) – Mixing σ-significances from different procedures without warning  
- **Location:** Abstract p.1; Sec. 1 p.1; Sec. 3.2 p.2; Sec. 4 p.3; Sec. 6 p.5  
- **Problem:** The manuscript quotes multiple σ-level significances from different analyses and procedures side-by-side without explicit cautions:  
  - Abstract: “3.6σ isotropic birefringence signal… We perform a Gaussian summary-likelihood inference … finding β = 0.242 ± 0.061° (3.9σ from zero) … We forecast that LiteBIRD… will test this prediction at 9σ significance.”  
  - Sec. 1: “Planck HFI… 2.5σ” and “ACT DR6… comparable significance. Combined, the evidence exceeds 3.5σ.”  
  - Sec. 3.2: “3.9σ from zero” from a summary likelihood; Sec. 4: 9σ forecast.  
  These are derived using different data combinations and statistical machinery (single-experiment fits, combined Gaussian summary likelihood, and Fisher-like forecast). The instructions explicitly require that **any juxtaposition of σ values from different null procedures must be accompanied by a clear statement that they are not directly comparable.**  
- **Required fix:**  
  - Wherever these σ values appear together (abstract, introduction, discussion), add an explicit sentence to the effect that “These σ values arise from different data combinations and statistical procedures and are not directly comparable in a strict statistical sense.”  
  - Clarify for each σ which dataset(s) and method were used (e.g., “3.9σ from our combined Gaussian summary-likelihood; 2.5σ from Planck HFI alone,” etc.)  
  - Avoid implying a monotonic strengthening of evidence across differently defined σ’s.  

P2-E8 (ESSENTIAL) – Unverified / inaccurate claim about Fujita et al. 2021 results  
- **Location:** Sec. 6 p.5; References p.6  
- **Problem:** The text states: “Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces β ∼ 0.3°.” Fujita et al. 2021 (Phys. Rev. D 103, 043509) indeed study isotropic birefringence and ALPs, but their focus is on constraints and implications; whether they “demonstrated that a Planck-scale ALP naturally produces β ∼ 0.3°” in the precise naturalness sense claimed here is not an obvious headline conclusion from the abstract/tables.[7] This statement looks like an interpretive overreach beyond what is explicitly demonstrated in that paper.  
- **Required fix:**  
  - Verify in Fujita et al. 2021 that the specific combination “Planck-scale decay constant + Hubble-scale mass naturally gives β ~ 0.3°” is clearly stated. If not, either soften the language (“can accommodate” instead of “already demonstrated”) and/or provide a more precise and accurate summary of their result.  
  - Ensure any quoted numerical values or parameter ranges from Fujita et al. are explicitly traceable to that paper’s figures/tables.  

P2-M1 (MAJOR) – Dimensional and definitional sloppiness in Eq. (1) and discussion of Δϕ/fa  
- **Location:** Sec. 2.1 Eq. (1) p.1–2; Sec. 2.2 p.2  
- **Problem:**  
  - Eq. (1) writes Δϕ ≈ fa θi (1 − J0(m/H0)/J0(0)). J0 is dimensionless; J0(0) = 1, so this is effectively Δϕ ≈ fa θi (1 − J0(m/H0)). This is dimensionally okay (Δϕ has dimension of fa), but the derivation is not shown and the factor (1 − J0(1) ≈ 0.24) is asserted without justification.  
  - Sec. 2.2 states: “the cosmological field evolution gives Δϕ/fa ∼ 10⁻² … yielding β ≈ C0 θi × 5 × 10⁻³ rad ≈ 0.27°.” This is internally inconsistent: if Δϕ/fa ~ 10⁻² and β = Δϕ/(2fa) (for C0 θi ~ 1), then β ~ 5×10⁻³, which is 0.005, not in radians vs degrees; 5×10⁻³ rad ≈ 0.29°, so the text is mixing “10⁻²” and “5×10⁻³” without clearly explaining the factors of 2 and C0θi.  
- **Required fix:**  
  - Either provide a brief derivation (or at least a clear reference with equation numbers) for Eq. (1) showing how the Bessel function arises and how the numerical coefficient 0.24 is obtained from a realistic ΛCDM background, or simplify the presentation to a parameterized factor with a citation.  
  - Clarify the numerical relation between Δϕ/fa, C0θi, and β. If Δϕ/fa ≈ 10⁻² C0θi, then β = C0θi × 5×10⁻³ rad implies Δϕ/fa ≈ 10⁻²; show this consistently and keep either β or Δϕ/fa as the primary dimensionless number.  
  - Cleanly distinguish radians vs degrees when quoting approximate numbers and ensure all factors of 2 are properly accounted for.  

P2-M2 (MAJOR) – Summary-likelihood assumptions and independence of datasets not justified  
- **Location:** Sec. 3.2 Eq. (3) p.2  
- **Problem:** The likelihood is taken as a product of independent Gaussians over the two measurements (Planck NPIPE and ACT DR6). However, the paper does not discuss a crucial issue: the extent to which these measurements share common systematics or calibration methods (e.g., both relying on Minami-Komatsu self-calibration). Treating them as independent can artificially tighten constraints and inflate the quoted σ (e.g., 3.9σ).  
- **Required fix:**  
  - Discuss potential correlations (both statistical and systematic) between the Planck and ACT birefringence measurements.  
  - Either justify approximate independence (e.g., different instruments, frequencies, analysis pipelines, and self-calibration strategies) or incorporate a simple correlation model and show how it changes βcombined and its significance.  
  - At minimum, add a caveat that the independence assumption might overstate the combined significance and that a full joint analysis would be preferable.  

P2-M3 (MAJOR) – Bayes factor computation under-specified and likely over-precise  
- **Location:** Sec. 3.4 Eq. (9) p.3  
- **Problem:** The paper quotes ln B = 5.17 (and 4.48, 5.86 for other priors) from a Savage-Dickey density ratio using a flat prior β ∈ [0°, 1°] etc., based on modest MCMC samples (Neff ~ 1000). The implementation details (prior on β in the ALP model vs null, kernel density estimation, binning choice, convergence checks) are not given, yet ln B is quoted to three significant figures. Given the small sample size and the heavy reliance on summary likelihoods, this level of numerical precision is not justified.  
- **Required fix:**  
  - Provide details of the Savage-Dickey implementation (prior on β, method for estimating posterior density at β = 0, numerical uncertainty on ln B).  
  - Reduce the precision of ln B to at most 1–2 significant digits (e.g., ln B ≈ 5.2 ± 0.3), and propagate the sampling uncertainty.  
  - Clearly state that the evidence is approximate and limited by the modest chain lengths and summary-likelihood approach.  

P2-M4 (MAJOR) – MCMC configuration and convergence assessment not adequate for PRD methods paper  
- **Location:** Table 1 p.2; Sec. 3.3 p.2–3  
- **Problem:**  
  - Sample sizes (720–6840 accepted samples) are very small by current standards, especially for 3-parameter (or more) models.  
  - Only Gelman-Rubin R̂ − 1 < 0.01 is reported, without effective sample size per parameter, autocorrelation times, or multiple-chain diagnostics.  
  - Yet tight parameter constraints (e.g., βALP = 0.336 ± 0.107°, Caγ × θi = 3.4 ± 1.1) are quoted as if robust.  
- **Required fix:**  
  - Either rerun the MCMC chains with significantly larger sample sizes (O(10⁴–10⁵) effective samples) and report standard convergence diagnostics, or clearly mark all MCMC results as preliminary/illustrative and do not rely on them for core conclusions.  
  - Report effective sample sizes per parameter and show that tails and Bayes factors are stable under chain thinning and different initializations.  

P2-M5 (MAJOR) – LiteBIRD forecast oversimplified and missing reference check  
- **Location:** Sec. 4 Eq. (10) p.3; abstract p.1; references p.6  
- **Problem:**  
  - The LiteBIRD forecast is simply Significance = 0.27/0.03 = 9σ, assuming σ(β) = 0.03° and central value 0.27°. This ignores potential systematic errors and the fact that LiteBIRD’s σ(β) depends on self-calibration choices and foregrounds, as the text briefly acknowledges but does not quantify.  
  - The reference “LiteBIRD Collaboration. LiteBIRD science goals and forecasts: a full-sky cmb polarization survey. Prog. Theor. Exp. Phys., 2023:042F01, 2023.” is real, but you must verify that σ(β) ≈ 0.03° is indeed quoted there and under what assumptions.[4]  
- **Required fix:**  
  - Verify in the LiteBIRD paper the exact forecasted σ(β) and cite the relevant figure/table.  
  - Clarify that 9σ is an **idealized statistical significance**, and provide at least a simple discussion of how self-calibration and residual systematics might degrade this (e.g., give a range).  
  - Avoid claiming “decisive” 9σ exclusion without a more nuanced forecast including systematics.  

P2-M6 (MAJOR) – Claims of “naturalness” and “no fine-tuning” not quantitatively supported  
- **Location:** Abstract p.1; Sec. 2.2 p.2; Sec. 6 p.5; Conclusion p.5  
- **Problem:** The manuscript repeatedly asserts that the model is “natural,” uses “no fine-tuning,” and that all parameters are O(1). Yet the actual parameter choices (fa ~ MPl, m ~ H0, θi ~ O(1), C0 ~ O(1)) are not drawn from a well-defined measure or theory prior; it is not shown that large fractions of allowed parameter space give β ≈ 0.27°. This is especially delicate in axion cosmology, where decay constants and masses are heavily constrained.  
- **Required fix:**  
  - Either provide a quantitative naturalness argument (e.g., showing that O(1) variations in θi and C0 preserve β in a narrow range, or defining a prior over parameter space and demonstrating that the observed β is typical) or soften all naturalness claims to descriptive language.  
  - Explicitly discuss how sensitive β is to variations in m around H0 and to fa differing by factors of a few from MPl.  

P2-M7 (MAJOR) – Abstract overstates what is actually shown  
- **Location:** Abstract p.1  
- **Problem:** The abstract says “We present predictions and constraints for cosmic birefringence from a spectator axion-like particle (ALP)… We perform a Gaussian summary-likelihood inference using Planck HFI and ACT DR6 data, finding β = 0.242 ± 0.061° (3.9σ)… We forecast that LiteBIRD… will test this prediction at 9σ significance.” Given the issues above (non-verified ACT dataset, simplistic combination, small-sample MCMC, oversimplified forecast), this reads as if robust, experiment-level results are presented, which is not supported by the actual methodological rigor.  
- **Required fix:**  
  - Rewrite the abstract to clearly indicate the exploratory nature of the analysis, the approximations (Gaussian summary likelihood, assumed independence, approximate Bayes factor), and the dependence on unverified ACT DR6 results.  
  - Until the ACT DR6 citation is corrected and all calculations are fully documented, avoid phrasing that implies final, experiment-collaboration-level constraints.  

P2-N1 (NIT) – Minor numerical rounding inconsistencies  
- **Location:** Sec. 3.2 Eq. (4) p.2; Sec. 3.3 Eqs. (6–8) p.2–3  
- **Problem:** Some quoted uncertainties are rounded inconsistently (e.g., 0.061° vs 0.062° from simple propagation; βALP = 0.336 ± 0.107° compared to βobs = 0.342 ± 0.094°). While small, PRD expects consistent rounding and precision.  
- **Required fix:**  
  - Adopt a consistent significant-figure policy (e.g., 2 significant figures for uncertainties) and ensure all central values are rounded accordingly.  

P2-N2 (NIT) – Reference formatting and capitalization  
- **Location:** References p.6  
- **Problem:**  
  - Some titles are not properly capitalized (“cmb” instead of “CMB”; “axionlike” vs “axion-like”; inconsistent hyphenation).  
  - “arXiv preprint” as a venue is non-standard; PRD prefers “arXiv:xxxx.xxxxx.”  
- **Required fix:**  
  - Standardize reference formatting to PRD style: full journal names or standard abbreviations, arXiv IDs where appropriate, correct capitalization of “CMB,” “ALP,” etc.  

P2-N3 (NIT) – Slightly over-assertive novelty statement  
- **Location:** Sec. 6 p.5  
- **Problem:** The paper states, “Our contribution is not the model itself, but rather the specific parameter identification (fa ∼ MPl, m ∼ H0) that produces a natural prediction matching the observed signal, and the inference framework demonstrating internal consistency.” Given Fujita et al. and other ALP birefringence works, it is possible that similar parameter choices have been discussed.  
- **Required fix:**  
  - Insert a modest caveat acknowledging that similar parameter regimes may have been considered elsewhere, and clarify precisely what is new (e.g., “We emphasize the particular combination fa ~ MPl, m ~ H0 as a simple benchmark and illustrate its compatibility with current birefringence measurements using a summary-likelihood approach”).  

P2-N4 (NIT) – Acknowledgements language about AI assistants  
- **Location:** Acknowledgments p.5  
- **Problem:** “The author acknowledges the use of AI research assistants during the analysis and manuscript preparation.” Some journals request more specific statements or disclosures when AI tools are used.  
- **Required fix:**  
  - Check PRD’s current policy on AI tool disclosure and adjust wording if necessary (e.g., specifying that AI tools were not listed as authors and that the author remains responsible for all content).  

P2-N5 (NIT) – Minor wording and style issues  
- **Location:** Throughout  
- **Problem:** A few phrases are informal for PRD (“consumer hardware,” “clean exclusion,” “overwhelming significance”).  
- **Required fix:**  
  - Replace with more formal wording (e.g., “standard desktop computing resources,” “strong exclusion,” “high statistical significance”).  

## Summary recommendation

**MAJOR REVISIONS**

The paper’s core idea—an ALP with fa ~ MPl and m ~ H0 giving a natural birefringence angle—could be interesting, but the current manuscript does not meet PRD standards in its handling of citations, data sources, and statistical rigor. A key ACT DR6 reference appears nonexistent or misidentified, the combined constraints and quoted significances rely on under-documented assumptions and small-sample MCMC, and several references (including “in preparation” and companion papers) are not yet suitable as quantitative support. These issues must be resolved, with corrected references, fully traceable numbers, more cautious claims, and better-documented methodology, before the work can be considered for publication in PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

P2-E9 (ESSENTIAL) – Incorrect significance quoted for Planck NPIPE “2.7σ”  
- **Location:** Sec. 3.1 p.2 (“Planck NPIPE [Eskilt and Komatsu, 2022]: β = 0.30 ± 0.11° (2.7σ)”)  
- **Problem:** The quoted significance does not match the given mean and error. Using the paper’s own numbers, \(0.30/0.11 ≈ 2.73\), which rounds to **2.7σ** if one keeps a single decimal, but the text gives only one decimal place in the angle and two in the error, implying a precision where 0.30/0.11 should be stated as 2.7σ or 2.73σ consistently across the paper. Elsewhere, e.g. for the combined constraint, “3.9σ” is given with one decimal place for a similarly simple ratio. The lack of a consistent significant-figure policy across all σ values (some rounded to one decimal, some to an integer) is an **arithmetic/rounding inconsistency** at the level PRD typically expects to be uniform.  
- **Required fix:**  
  - Decide on a consistent precision for σ values derived from simple ratios (e.g., one decimal place).  
  - Recompute and round all such significances uniformly (Planck NPIPE, ACT, combined, MCMC posteriors, etc.), making sure the quoted σ matches the corresponding \(β/σ_β\) at that level of precision.  

P2-E10 (ESSENTIAL) – Mismatch between quoted “3.9σ” and underlying β/σ values across text  
- **Location:** Abstract p.1 (“β = 0.242 ± 0.061° (3.9σ from zero)”); Sec. 3.2 Eq. (4) p.2; Sec. 6 bullet 2 p.5 (“matches the combined Planck + ACT measurement at 1σ”)  
- **Problem:**  
  - For the summary-likelihood result, \(0.242/0.061 ≈ 3.97\), which rounds to **4.0σ**, not 3.9σ, at one decimal place. This is a small but non-negligible rounding discrepancy for a central quantitative claim in a methods paper.  
  - In Sec. 6, the statement “matches the combined Planck + ACT measurement at 1σ” is ambiguous and numerically unsupported as written. If “prediction” refers to β ≈ 0.27° and “combined measurement” to βcombined = 0.242 ± 0.061°, the difference is |0.27 − 0.242| = 0.028°, which is ≈0.46σ using σ = 0.061°, i.e. less than 0.5σ, not “1σ.” If instead the comparison is to βobs = 0.342 ± 0.094°, the difference is 0.072°, which is ≈0.77σ, still < 1σ. The “1σ” phrasing therefore overstates the discrepancy and is not backed by a clear, explicitly computed ratio.  
- **Required fix:**  
  - For Eq. (4), either:  
    - Recompute βcombined and σcombined at higher precision and then round both the central value and significance consistently (e.g., 0.242 ± 0.061° → 4.0σ), or  
    - Adjust σcombined slightly (e.g., 0.062°) if that is what the actual calculation yields, and ensure β/σ matches the quoted σ-level exactly.  
  - In Sec. 6, replace “matches … at 1σ” with a quantitatively accurate statement such as “agrees within ≲0.5σ” or “well within 1σ,” and explicitly identify which data point is being compared to which model prediction.  

P2-E11 (ESSENTIAL) – Internal inconsistency: prediction β ≈ 0.27° vs. MCMC-derived βALP = 0.336°  
- **Location:** Abstract p.1; Sec. 2.2 p.2; Sec. 3.3 Eqs. (6–7) p.2–3; Sec. 6 bullets 1–3 p.5; Sec. 7 p.5  
- **Problem:**  
  - The abstract and Sec. 2.2 emphasise a *model prediction* of **β ≈ 0.27°** based on order-unity parameters and the claimed cosmological integration factor, presented as the central theoretical output.  
  - The MCMC analysis of the ALP model (Run 1) yields **βALP = 0.336 ± 0.107°**, while the model-independent fit gives βfree = 0.344 ± 0.096° and the adopted “observed” value is βobs = 0.342 ± 0.094°. These are mutually consistent, but all are centered around **0.34°**, not 0.27°.  
  - The Discussion bullet “Consistency with data: The prediction matches the combined Planck + ACT measurement at 1σ” and the Conclusion’s “naturally accommodates cosmic birefringence at β ≈ 0.27°” thereby mix two different central values (0.27° vs ~0.34°) without clearly explaining which is *predicted* and which is *inferred* from data. This is not a pure arithmetic error but an **internal numerical inconsistency** between the “prediction” stated early and the posterior mean actually obtained from the ALP fit.  
- **Required fix:**  
  - Decide which number represents the model’s actual prediction under the chosen parameter priors. If the posterior in the ALP model peaks at ~0.34°, then the “prediction” should be updated or rephrased as “the model naturally yields β in the range 0.3°–0.35° consistent with the observed ~0.34° signal,” rather than a specific 0.27°.  
  - Alternatively, if 0.27° is intended as a fiducial analytic estimate, clearly distinguish in the abstract and conclusions between the *analytic estimate* (0.27°) and the *data-driven posterior mean* (~0.34°), and quantify their difference (≈0.7σ) instead of claiming a direct match.  

P2-M8 (MAJOR) – Dimensional and definitional ambiguity in Eq. (2) and definition of \(f_{\text{photon}}\)  
- **Location:** Sec. 2.2 Eq. (2) p.2; Sec. 3.2 Eq. (5) p.2; abstract p.1  
- **Problem:**  
  - Eq. (2) writes \(β = g_{aγ}\Deltaϕ/2 = C_0 \Deltaϕ/(2 f_a)\) and then “≈ \(C_0 θ_i /2 × O(1)\).” It is later claimed that “the cosmological field evolution gives Δϕ/fa ∼ 10⁻² … yielding β ≈ C0 θi × 5 × 10⁻³ rad.” Combining β = Δϕ/(2 f_a) and Δϕ/f_a ∼ 10⁻² implies β ∼ 5×10⁻³ (dimensionless), i.e. 5×10⁻³ rad, but the text places the factor C0 θi outside both relations in a way that blurs whether Δϕ/fa ∼ 10⁻² includes C0 θi or not.  
  - In Sec. 3.2, the paper defines an “effective photon coupling parameter” \(f_{\text{photon}} × C_0 = 1.73 ± 0.44\) without ever explicitly defining \(f_{\text{photon}}\) in Eq. (2) or earlier. Dimensional analysis suggests \(f_{\text{photon}}\) is intended to be \(M_{\rm Pl}/f_a\) or similar, but this is never stated. The numerical result 1.73 ± 0.44 therefore lacks a clear dimensional or physical interpretation.  
- **Required fix:**  
  - Clarify whether Δϕ/fa ∼ 10⁻² refers to the *pure field displacement ratio* (independent of C0 θi) or already includes the anomaly coefficient and misalignment. Rewrite Eq. (2) so that either:  
    - \(Δϕ/fa ≈ 10^{-2} θ_i\) and then explicitly \(\beta = (C_0 θ_i /2) × 10^{-2}\), or  
    - \(Δϕ/fa ≈ 10^{-2}\) and then \(\beta = (C_0 θ_i /2) × 10^{-2}\), making the dependence unambiguous.  
  - Introduce \(f_{\text{photon}}\) explicitly, with units and definition (e.g. \(f_{\text{photon}} ≡ f_a/M_{\rm Pl}\) or its inverse), and show how Eq. (5) is derived from Eq. (2) and the combined β constraint. Without this, Eq. (5) is dimensionally opaque and not reproducible.  

P2-M9 (MAJOR) – Abstract claims not fully supported or qualified by body text  
- **Location:** Abstract p.1 vs. Secs. 2–4  
- **Problem (sentence-by-sentence check):**  
  - “We present predictions and constraints … with Planck-scale decay constant … and mass m ∼ H0.” – The body indeed considers this setup, but **never shows an explicit parameter-space scan or quantitative argument** that fa ∼ MPl and m ∼ H0 are the only or preferred region; they are assumed. The word “predictions” implies a more rigorous derivation than is actually given (a single back-of-the-envelope estimate in Sec. 2.2).  
  - “For order-unity inputs, this minimal setup naturally accommodates β ≈ 0.27° …” – As noted above, the only explicit number derived from data is βALP ≈ 0.336°; the 0.27° value is analytic and not propagated through the MCMC. The body does not contain a section where “natural” is quantified (no sensitivity analysis in m, fa, θi).  
  - “We perform a Gaussian summary-likelihood inference … finding β = 0.242 ± 0.061° (3.9σ) … fphoton × C0 = 1.73 ± 0.44 (order-unity, no fine-tuning)” – Sec. 3.2 gives these numbers but does not show the explicit mapping from β to \(f_{\text{photon}}×C_0\) or demonstrate that *any* O(1) variation in θi and C0 leaves β within the observed range. The phrase “no fine-tuning” is not backed by a quantitative measure of tuning.  
  - “The Bayes factor in favor of nonzero rotation is ln B = 5.17 (indicative; prior-dependent, see Sec. 3.4).” – Sec. 3.4 repeats the value and gives prior ranges but no numerical uncertainty or implementation detail; the word “indicative” is present, but the abstract still presents ln B as a sharp figure rather than a rough estimate.  
  - “We forecast that LiteBIRD … will test this prediction at 9σ significance—either confirming … or ruling out … decisively.” – Sec. 4 explicitly uses 0.27/0.03 = 9σ and acknowledges dependence on self-calibration only in a cursory way. The words “decisively” and “will test at 9σ” remain an overstatement compared to the modest, purely statistical forecast actually performed.  
- **Required fix:**  
  - For each quantitative abstract claim, add or strengthen the corresponding justification in the body:  
    - Provide a short robustness check showing how β varies with m around H0 and fa around MPl, or soften “naturally accommodates” to “can accommodate” unless such a check is added.  
    - Either remove “no fine-tuning” from the abstract or back it with a sensitivity discussion in Sec. 2.2 quantifying how typical β ≈ 0.27° is in the assumed parameter ranges.  
    - For the 9σ forecast, explicitly call it an *idealized statistical* forecast in the abstract and refer to the systematic limitations discussed in Sec. 4 and Sec. 6.  

P2-M10 (MAJOR) – Juxtaposition of multiple σ-values without explicit “not directly comparable” caveat (additional instances)  
- **Location:**  
  - Abstract p.1 (“3.6σ isotropic birefringence signal … finding … 3.9σ from zero … will test this prediction at 9σ significance”)  
  - Sec. 1 p.1 (“2.5σ … comparable significance … Combined, the evidence exceeds 3.5σ”)  
  - Sec. 6 p.5 (“2.5σ Planck HFI”, implicit 3.6σ from joint analysis, 3.9σ from summary-likelihood, 9σ from LiteBIRD forecast referenced together)  
- **Problem:** You already flagged mixed σ’s in your earlier review, but a fresh check shows additional locations where **three different σ-values** (3.6σ literature summary, 3.9σ combined fit, 9σ forecast) appear in the same sentence or short paragraph without any note that they are based on different data combinations and statistical procedures (full-spectrum fit, Gaussian combination of point estimates, Fisher-like forecast). For PRD, this is particularly misleading in the abstract, where readers may interpret them as commensurate.  
- **Required fix:**  
  - In the abstract and Sec. 1, add an explicit sentence such as: “These σ values are derived from different analyses (literature joint fit, our summary-likelihood combination, and a simple Fisher-style forecast) and are not directly comparable in a strict statistical sense.”  
  - Ensure that wherever 3.6σ, 3.9σ, and 9σ appear in close proximity, the data and method behind each are named, and it is clear that they represent different null procedures.  

P2-N3 (NIT) – Figure captions vs body text not perfectly aligned in quantitative detail  
- **Location:** Fig. 1 caption p.4; Sec. 3.3 p.2–3; Fig. 2 caption p.4  
- **Problem:**  
  - Fig. 1 caption: “The posterior on the coupling-misalignment product Caγ × θi is centered at 3.4 ± 1.1, consistent with order-unity natural values.” Sec. 3.3 Eq. (8) also gives 3.4 ± 1.1, so the numbers match, but **“order-unity natural values”** in the caption overlaps with the “naturalness” claims in the text that are not quantitatively demonstrated; this is more of a semantic than numerical mismatch, but PRD typically expects captions to be descriptive rather than interpretive.  
  - Fig. 2 caption: “All three are consistent with each other and with the observed value βobs = 0.342 ± 0.094°.” In Sec. 3.3, the quoted posteriors (0.336 ± 0.107°, 0.344 ± 0.096°, and βobs = 0.342 ± 0.094°) are indeed mutually consistent numerically, but the caption does not state the σ-level of this consistency or indicate the exact data used for each curve. This can be interpreted as a mild **underspecification** relative to the more explicit text.  
- **Required fix:**  
  - Keep the numerical values but consider making the captions purely descriptive, e.g. “centered at 3.4 ± 1.1 (see Eq. 8)” and “consistent within 1σ with βobs = 0.342 ± 0.094°,” to match the quantitative language of the main text and avoid duplicating interpretive claims.  

P2-N4 (NIT) – Cross-reference precision and clarity  
- **Location:** Multiple: abstract “see Sec. 3.4”; Sec. 3.2 “Eq. (3)”; Sec. 3.3 “Run 1, C = 8 fixed”; Sec. 5 “see the companion paper [Golden, 2026a]”; Sec. 6 “[Golden, 2026b]”  
- **Problem:** The main LaTeX cross-references (\eqref, \ref) are numerically correct for the internal equations (Eq. 1–10), but several textual cross-references are **underspecified or point to non-public or non-existent material**:  
  - Abstract “see Sec. 3.4” is fine, but Sec. 3.4 does not provide enough detail to justify the three significant digits of ln B quoted in the abstract.  
  - “Run 1, C = 8 fixed” and “Run 2, C free” are described only briefly in Table 1 and Sec. 3.3; the value C = 8 comes out of nowhere for a reader not seeing the companion paper.  
  - References to [Golden, 2026a,b] are still non-public, so while the cross-reference itself is formally correct, it is not useful for readers and puts weight on untraceable material.  
- **Required fix:**  
  - Where cross-references point to sections that contain only minimal detail (e.g. Bayes factor implementation in Sec. 3.4), add the missing information or temper the precision of the claims dependent on them.  
  - Either remove the dependence on C = 8 (or explain its origin in this paper), or clearly mark it as an illustrative choice, not a value justified in the non-public companion.  

If you implement all the fixes from the initial review plus the additional corrections above, the manuscript’s numerical and logical consistency will be substantially closer to what PRD referees expect.