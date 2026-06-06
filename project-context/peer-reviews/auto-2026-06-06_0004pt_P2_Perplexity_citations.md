# P2 auto-2026-06-06_0004pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (15531 chars)
**Wall time**: 82.7s

---

P2-E1 (ESSENTIAL) – Abstract, p.1  
**Problem:** The abstract states: “...consistent with the 3.6σ isotropic birefringence signal (βobs = 0.342±0.094◦ from the Eskilt et al. joint Planck + ACT analysis).”  
- A value β = 0.342 ± 0.094° corresponds to 0.342/0.094 ≈ 3.64σ, which is consistent with “3.6σ,” but this exact combination (Planck+ACT joint analysis by “Eskilt et al.” giving 0.342 ± 0.094°) does not correspond to any published paper as of now. The cited Eskilt & Komatsu 2022 PRD paper is WMAP+Planck only, without ACT, and reports β ≈ 0.35 ± 0.14° (roughly 2.5σ), not 0.342 ± 0.094°.[2][3][4]  
**Required fix:**  
- Clarify precisely which dataset and analysis produce βobs = 0.342 ± 0.094° and provide a correct, published citation. If this is an internal re-analysis by the author, it must be clearly labeled as such and not attributed to “Eskilt et al.”  
- Remove or correct the “joint Planck + ACT analysis” phrase unless there is a real, citable paper with that exact combination.  

---

P2-E2 (ESSENTIAL) – Abstract & Sec. 3.2, p.1–2  
**Problem:** The combined constraint is quoted as β = 0.242 ± 0.061° (3.9σ from zero) from two measurements: 0.30 ± 0.11° (Planck NPIPE) and 0.215 ± 0.074° (ACT DR6).  
- Recomputing the inverse-variance weighted mean:  

  - Planck: σ₁ = 0.11 → w₁ = 1/σ₁² ≈ 82.64  
  - ACT: σ₂ = 0.074 → w₂ = 1/σ₂² ≈ 182.74  
  - β̄ = (w₁β₁ + w₂β₂)/(w₁ + w₂) ≈ (82.64·0.30 + 182.74·0.215)/(265.38) ≈ 0.239°.  
  - σ̄ = (w₁ + w₂)⁻¹/² ≈ 1/√265.38 ≈ 0.061°.  

  The correct combined mean is ≈0.239°, not 0.242°. The quoted mean is off by ~0.003°, which is small but inconsistent with the explicit numbers given and implies that either the inputs or the combination procedure differ from what is written. The quoted significance 3.9σ corresponds to 0.239/0.061 ≈ 3.92 or 0.242/0.061 ≈ 3.97; neither is exactly traceable from the stated input without clarification.  
**Required fix:**  
- Recompute the combined value and quote it consistently (to two or three significant figures) with the stated inputs and Eq. (3), or state explicitly if a more complete covariance treatment (non-diagonal covariance, additional datasets, or non-Gaussian combination) was used.  
- Adjust the quoted significance accordingly and ensure the same numbers appear consistently in the abstract and body.  

---

P2-E3 (ESSENTIAL) – Sec. 3.1, p.2  
**Problem:** ACT DR6 birefringence citation: “ACT DR6 [Diego-Palazuelos and Komatsu, 2025]: β = 0.215 ± 0.074◦ (2.9σ).” In the References this appears as: “P. Diego-Palazuelos and E. Komatsu. Cosmic birefringence from the Atacama Cosmology Telescope. arXiv preprint, 2025.”  
- As of now, there is no arXiv or ADS record with those authors, that title, and that year.[1][2]  
- Using “arXiv preprint, 2025” without an arXiv ID is not acceptable for PRD, and the specific number β = 0.215 ± 0.074° is therefore not verifiable.  
**Required fix:**  
- Provide a valid arXiv ID and full bibliographic details for the ACT birefringence result, and verify that the quoted β and uncertainty match that paper’s abstract or tables; or clearly label this as an unpublished private communication or internal analysis and remove it as a formal reference.  
- If no citable ACT DR6 birefringence result exists, the ACT DR6 numbers must be removed from the paper’s quantitative claims, or demoted to speculative/forecast status with transparent provenance.  

---

P2-E4 (ESSENTIAL) – Sec. 3.2 and Eq. (5), p.2  
**Problem:** The parameter “fphoton × C0 = 1.73 ± 0.44” is quoted with no clear definition of units or normalization, and with no derivation shown. It is stated to be “order-unity, consistent with the ALP prediction without fine-tuning.” However:  
- In standard notation, the ALP-photon coupling is gaγ = C0/fa with dimensions of inverse energy.[5] The combination “fphoton × C0” is non-standard and dimensionful; treating a dimensionful product as “order unity” is physically meaningless without a specified normalization.  
- No equation in the text connects βcombined to this specific numerical value 1.73 ± 0.44, nor does the reader see the mapping between β and “fphoton × C0.”  
**Required fix:**  
- Define precisely what “fphoton” is (decay constant in units of MPl, 10¹⁶ GeV, or something else) and specify its dimensions.  
- Provide the equation linking β to fphoton and C0, then show (even briefly) how plugging in βcombined leads to 1.73 ± 0.44.  
- Clarify why “order unity” is claimed for this dimensionless or dimensionful combination and in what units.  

---

P2-E5 (ESSENTIAL) – Sec. 3.4, p.3  
**Problem:** The Bayes factor claim: “ln B = 5.17 ... computed via the Savage-Dickey density ratio with a flat prior β ∈ [0◦ , 1◦ ]. The evidence is prior-dependent: ln B = 4.48 for β ∈ [0◦ , 2◦ ] and ln B = 5.86 for β ∈ [0◦ , 0.5◦ ].”  
- No explicit likelihood or posterior expressions are given beyond the simple Gaussian summary likelihood in Eq. (3). For a single-parameter Gaussian with mean μ and σ, the Savage–Dickey ratio can be written analytically. Using μ ≈ 0.24° and σ ≈ 0.061°, one can compute ln B for the given priors; the values 5.17, 4.48, and 5.86 are plausible but not checked or justified in the text.  
- PRD-level methods work requires at least a minimal derivation or a check pointer (e.g., equation or appendix) to verify these numbers and their sensitivity to prior choice; otherwise they are un-auditable.  
**Required fix:**  
- Include a short derivation (or an appendix) of the Savage–Dickey computation for this one-parameter Gaussian case and show how the quoted numbers are obtained from the measured μ and σ.  
- Alternatively, provide the exact Gaussian parameters (mean, σ) used for the Bayes factor (which may differ slightly from Eq. (4) if a different combination or full EB likelihood was used).  

---

P2-E6 (ESSENTIAL) – Sec. 4, Eq. (10), p.3  
**Problem:** Forecast: “σ(β) ≈ 0.03◦” from LiteBIRD and “For our prediction β = 0.27◦: Significance = 0.27/0.03 = 9σ. If LiteBIRD measures β = 0 ± 0.03◦ , the ALP explanation is excluded at 9σ.”  
- The LiteBIRD Collaboration 2023 PTEP paper’s birefringence forecasts depend strongly on the self-calibration scheme and systematics assumptions; a blanket σ(β) = 0.03° is not a general statement, and the precise forecast value must be traceable.[4]  
- The logical statement “measures β = 0 ± 0.03°” means roughly |β| < 0.06° at 2σ; rejecting a true β = 0.27° at 9σ requires that the experiment be both unbiased and statistics-dominated. Systematics, self-calibration degeneracies, or non-Gaussian posteriors could reduce the effective significance relative to the naïve 0.27/0.03 computation. The current wording presents 9σ as guaranteed, rather than as an optimistic Gaussian forecast.  
**Required fix:**  
- Cite the specific part of the LiteBIRD forecast paper that justifies σ(β) ≈ 0.03°, including the assumed self-calibration strategy. If the 0.03° comes from a particular forecast configuration, say so explicitly.  
- Rephrase the exclusion statement to make clear this is a forecast under idealized Gaussian assumptions (e.g., “would correspond to ≈ 9σ under Gaussian, statistics-dominated assumptions”).  

---

P2-E7 (ESSENTIAL) – Sec. 6, p.5; References, p.6  
**Problem:** Reference and text: “Toshiya Namikawa, Kai Murai, and Sho Naokawa. Constraints on axion-like particles from cosmic birefringence. arXiv e-prints, 2025. In preparation; cited for comparison of ALP mass constraints.” In the text: “Namikawa, Murai & Naokawa [Namikawa et al., 2025] provide superior ALP mass constraints...”  
- The actual paper on arXiv and in ADS is “Planck Constraints on Axion-Like Particles through Isotropic Cosmic Birefringence” by Toshiya Namikawa, Kai Murai, and Fumihiro Naokawa (not “Sho Naokawa”).[3][4][6]  
- The arXiv ID is 2506.20824, and the title differs from that cited.  
- Calling it “In preparation” is factually wrong; the paper is already on arXiv.  
**Required fix:**  
- Correct the author name (“Fumihiro Naokawa”), title, and status: cite the arXiv ID (2506.20824) and, if available, the journal (Phys. Rev. D 111, 043514 for the related oscillating ALP work,[5] and the correct journal details for 2506.20824 if accepted).  
- Remove “In preparation” and replace with “arXiv e-prints (arXiv:2506.20824)” or the final journal citation once available.  
- Ensure that any statements about “superior ALP mass constraints” are consistent with the actual content and results of that paper.  

---

P2-E8 (ESSENTIAL) – References, p.6 (“P. Diego-Palazuelos and E. Komatsu. Cosmic birefringence from the Atacama Cosmology Telescope. arXiv preprint, 2025.”)  
**Problem:** As above, this reference does not correspond to any actual arXiv preprint at present.[1][2] Using an uncitable future-dated preprint with no arXiv ID violates PRD standards.  
**Required fix:**  
- Either supply the correct arXiv ID and confirm the title/authors/year, or remove/downweight this reference. If the analysis is genuinely forthcoming but not posted, it should not be used as a quantitative input.  

---

P2-E9 (ESSENTIAL) – References, p.6 (“Toshiya Namikawa, Kai Murai, and Sho Naokawa…” vs. actual literature)  
**Problem:** Separate from the wrong name/status, the title used in-text (“Constraints on axion-like particles from cosmic birefringence”) closely resembles but does not match the actual paper “Planck Constraints on Axion-Like Particles through Isotropic Cosmic Birefringence.”[3][4] This is fused metadata combining the actual title with a generic phrase.  
**Required fix:**  
- Replace the generic/fused title with the exact title from arXiv/ADS.  

---

P2-E10 (ESSENTIAL) – Sec. 2.1 & Eq. (1), p.1  
**Problem:** The field displacement is written as  
\[
\Delta\phi \approx f_a \theta_i \left(1 - \frac{J_0(m/H_0)}{J_0(0)}\right) \approx f_a \theta_i \times O(1).
\]  
- Bessel function J₀(x) satisfies J₀(0) = 1, so the fraction J₀(m/H₀)/J₀(0) is redundant. More importantly, the text later uses “For m/H₀ ∼ 1, 1 − J0(1) ≈ 0.24” as the relevant factor.  
- There is no derivation or reference for this specific Bessel-function form of the displacement in the background cosmology being considered. For m ∼ H₀, the correct solution for a scalar in an expanding universe requires solving the Klein–Gordon equation in FRW; the form given, involving J₀(m/H₀), is not standard and is left unexplained.  
**Required fix:**  
- Either provide a derivation (or a cited reference) for this Bessel-function expression in the chosen cosmology, or replace it by a correctly derived approximate solution for the scalar field evolution.  
- At minimum, remove the unnecessary J₀(0) denominator and ensure the numerical factor 1 − J₀(1) ≈ 0.24 is clearly connected to the cosmological integration.  

---

P2-E11 (ESSENTIAL) – Dimensional consistency and normalization in Sec. 2.2, p.1  
**Problem:** The text claims: “For C0 ∼ 1, θi ∼ 1: the cosmological field evolution gives ∆ϕ/fa ∼ 10−2 … yielding β ≈ C0 θi × 5 × 10−3 rad ≈ 0.27◦.” But using Eq. (2), β = (gaγ/2)Δϕ = (C0/(2fa))Δϕ. If Δϕ/fa ∼ 10⁻² and C0, θi ∼1, then  
- β ≈ (1/2)·10⁻² = 5×10⁻³ (dimensionless)  
- 5×10⁻³ rad ≈ 0.29°, not 0.27°. The text mixes C0 θi language with the factor of 1/2 in Eq. (2); the half appears to be dropped in the text when quoting 5×10⁻³ rad.  
**Required fix:**  
- Make the normalization consistent: either explicitly include or consistently absorb the factor of 1/2 into the definition of C0 or Δϕ/fa.  
- Recalculate and quote the rotation angle with numerically correct conversions (5×10⁻³ rad ≈ 0.286°). If a different factor is intended from the cosmological integration, state it explicitly.  

---

P2-M1 (MAJOR) – Abstract vs. body consistency on σ values and “3.9σ” vs. “3.6σ”, p.1–2  
**Problem:**  
- Abstract: “β ≈ 0.27◦ , consistent with the 3.6σ isotropic birefringence signal (βobs = 0.342±0.094◦...).”  
- Sec. 3.2: Combined Planck+ACT summary likelihood yields βcombined = 0.242 ± 0.061° (3.9σ).  
- The text does not clarify that these σ levels come from different procedures: one is from “Eskilt et al. joint analysis,” one from the author’s own summary likelihood. They are juxtaposed without explicit “not directly comparable” caveats at the points of comparison, contrary to the review instruction.  
**Required fix:**  
- Whenever numbers from different null procedures or likelihood constructions are compared or mentioned side by side (βobs vs. βcombined, different datasets vs. summary likelihood), add explicit statements that the significances are not directly comparable because they arise from distinct analyses and assumptions.  
- Make clear which σ is the author’s own derived quantity vs. which is taken from the literature.  

---

P2-M2 (MAJOR) – MCMC run sizes and statistical robustness, Table 1 & Sec. 3.3, p.2–3  
**Problem:**  
- Table 1 quotes sample counts 720–6,840 with R̂ − 1 < 0.01, and the text acknowledges “modest by modern standards,” with Neff ∼ 1,000.  
- These chain lengths are extremely small for any reliable Bayes factor estimation and even marginal for robust posterior tails in a 3-parameter model. Yet Bayes factors and parameter posteriors are used as substantive evidence supporting the model.  
**Required fix:**  
- At minimum, explicitly state that the quoted Bayes factors and posterior tail behavior are preliminary and not numerically robust by PRD standards.  
- Strongly recommended: rerun the chains with at least O(5×10⁴) independent samples per run, report effective sample sizes, and update posteriors/Bayes factors. If this cannot be done for this submission, downweight the interpretive claims based on Bayes factors.  

---

P2-M3 (MAJOR) – Novelty claims vs. literature, Sec. 6, p.5  
**Problem:** The paper says: “Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces β ∼ 0.3◦ , and Namikawa, Murai & Naokawa [Namikawa et al., 2025] provide superior ALP mass constraints using the full Planck EB spectrum. Our contribution is not the model itself, but rather the specific parameter identification (fa ∼ MPl , m ∼ H0 ) that produces a natural prediction matching the observed signal, and the inference framework demonstrating internal consistency.”  
- Fujita et al. 2021 indeed discuss ALP explanations for birefringence and demonstrate parameter regions producing β ∼ 0.3°.[7] Namikawa et al. 2025 (arXiv:2506.20824) provide detailed Planck ALP constraints.[3][4]  
- The claimed novelty—identifying fa ∼ MPl, m ∼ H₀ as “specific parameter identification”—appears extremely close to what is already considered in Fujita et al. and the broader ALP dark energy literature (Planck-scale decay constant and Hubble-scale mass). Without more explicit differentiation, this may not meet PRD’s bar for methodological or theoretical novelty.  
**Required fix:**  
- Carefully benchmark the model and parameter choices against Fujita et al. 2021 and related ALP dark-energy papers; explicitly state what is *technically new* here (e.g., a particular combination of data, a specific forecast pipeline, or distinct theoretical constraints).  
- If the only novelty is a restatement of known parameter regimes with a light reinterpretation, the scope of the paper must be reduced or repositioned (e.g., as a short note, not a full PRD article).  

---

P2-M4 (MAJOR) – Companion papers “submitted simultaneously”, References p.6; Sec. 5 & 6  
**Problem:** The paper references two “companion papers” by the same author:  
- Golden 2026a: “Spin-torsion cosmology and the search for geometric dark energy: Structural barriers, perturbation transparency, and surviving predictions. Companion paper, submitted simultaneously, 2026a.”  
- Golden 2026b: “Testing the matter bounce with primordial non-Gaussianity: Forecasts for SPHEREx and MegaMapper. Companion paper, submitted simultaneously, 2026b.”  
There are no arXiv IDs, journal submissions, or ADS records corresponding to these works at this time. They are used for conceptual motivation and for fNL forecasts (“The matter-bounce non-Gaussianity fNL = −35/8 provides a complementary and independent test [Golden, 2026b].”).  
**Required fix:**  
- Either provide arXiv IDs for these companion papers or remove them as formal references.  
- Any critical theoretical or observational claims (e.g., the stated value fNL = −35/8 as a testable prediction) must be either supported by a published or posted preprint or treated purely as speculative context, clearly labeled as such. PRD will not accept reliance on uncitable “companion” manuscripts.  

---

P2-M5 (MAJOR) – Unsupported statement about fNL test, Sec. 6, p.5  
**Problem:** “The matter-bounce non-Gaussianity fNL = −35/8 provides a complementary and independent test [Golden, 2026b].”  
- There is no citable reference for this statement since Golden 2026b is not publicly available.  
- The value fNL = −35/8 appears as a precise prediction; readers cannot verify its provenance.  
**Required fix:**  
- Provide a published or arXiv-cited source that derives fNL = −35/8, or explicitly move this statement to a speculative footnote or remove it.  

---

P2-M6 (MAJOR) – Abstract scope vs. proof, p.1  
**Problem:** Abstract says: “We perform a Gaussian summary-likelihood inference using Planck HFI and ACT DR6 data, finding β = 0.242 ± 0.061◦ (3.9σ from zero) with an effective photon coupling fphoton × C0 = 1.73 ± 0.44 (order-unity, no fine-tuning). The Bayes factor in favor of nonzero rotation is ln B = 5.17...”  
- “No fine-tuning” and “order-unity” are qualitative theoretical claims, not simple empirical statements. The paper does not quantitatively define a measure of tuning or show that the allowed parameter region is typical in any statistical sense (e.g., prior volume fraction).  
- The Bayes factor is treated as a central result despite being computed from short MCMC chains and a simplistic summary-likelihood.  
**Required fix:**  
- Remove or soften “no fine-tuning” unless a quantitative tuning measure is defined and evaluated. For example, one could specify a prior on θi and C0 and show that the probability of matching the observed β within some tolerance is not small.  
- Clarify that ln B values are approximate and depend on prior choices, chain lengths, and Gaussian assumptions.  

---

P2-M7 (MAJOR) – Use of “indicative” Bayes factor without adequate caveats in Discussion/Conclusion, p.3, 5, 6  
**Problem:** Eq. (9) calls ln B = 5.17 “indicative evidence,” but later Discussion and Conclusion paragraphs treat the model as sharply supported (“The ALP model reproduces the observed birefringence with no tension,” “sharp falsifiability,” etc.) without clearly separating robust observational facts from prior-dependent Bayes factors.  
**Required fix:**  
- Include explicit caveats in the Discussion and Conclusion that the Bayes factor and parameter inferences are limited by the simplistic summary-likelihood and short chains, and that current evidence should primarily be interpreted at the level of σ significance from the underlying birefringence measurements.  

---

P2-M8 (MAJOR) – Abstract vs. body on “Planck HFI and ACT DR6” vs. actual cited datasets, p.1–2  
**Problem:** The abstract claims use of “Planck HFI and ACT DR6 data,” but the body’s formal datasets are:  
- Planck NPIPE (Eskilt & Komatsu 2022)  
- ACT DR6 (unpublished Diego-Palazuelos & Komatsu 2025)  
“Planck HFI” often refers to a distinct analysis (Minami & Komatsu 2020 PRL) on Planck 2018 HFI polarization.[2]  
**Required fix:**  
- Clarify whether the analysis uses the Minami & Komatsu 2020 HFI result, the Eskilt & Komatsu 2022 WMAP+Planck result, or both. If only the latter is used, “Planck HFI” in the abstract is misleading and should be replaced with “Planck polarization (NPIPE)” or equivalent.  

---

P2-M9 (MAJOR) – Overlap with Namikawa et al. and Fujita et al., insufficient differentiation of constraints, Sec. 3 & 6  
**Problem:** The paper presents ALP constraints and mass-coupling inferences but does not systematically compare them to the more complete analyses in Fujita et al. 2021 and Namikawa et al. 2025.[3][5][7]  
**Required fix:**  
- Include a quantitative comparison of parameter constraints (especially on m and gaγ) to Fujita et al. and Namikawa et al., acknowledging where the present work is weaker or complementary and avoiding overclaiming constraint novelty.  

---

P2-m1 (MINOR) – Numerical consistency: 0.27° vs. 0.286°, p.1–3  
**Problem:** Throughout the paper, β ≈ 0.27° is quoted as the “prediction,” while conversions like 5×10⁻³ rad actually correspond to ≈0.286°.  
**Required fix:**  
- Decide on a consistent central value (e.g., 0.28°) or state clearly that 0.27° is an approximate rounded value arising from a more detailed integration.  

---

P2-m2 (MINOR) – Equation (3) formatting, p.2  
**Problem:** In Eq. (3), the product sign and indices are somewhat unclear:  
\[
L(\beta) = \prod_i \frac{1}{\sqrt{2\pi\sigma_i^2}} \exp\left[-\frac{(\beta_{\text{obs}} - \beta)^2}{2\sigma_i^2}\right].
\]  
The notation “β obs” without a subscript i is ambiguous; different experiments have different βobs.  
**Required fix:**  
- Replace β obs → β_i in the exponent to match the product index, e.g., \((\beta_i - \beta)^2\).  

---

P2-m3 (MINOR) – Table 1 usefulness, p.2  
**Problem:** Table 1 lists MCMC run configurations and status but does not report key diagnostic statistics (effective sample sizes, acceptance rates, etc.). As a result, it is only marginally informative.  
**Required fix:**  
- Either enhance Table 1 to include Neff and acceptance rates or move these details to the text and reserve the table for more substantial results.  

---

P2-m4 (MINOR) – Figure captions vs. content, p.4–5  
**Problem:**  
- Figure 1 caption: “Triangle plot from the extended ALP MCMC (Run 2, C free)...” No axes/parameters are described explicitly (e.g., which parameters are plotted).  
- Figure 2 caption: “Comparison of β posteriors across all three model configurations...” No details on binning, normalization, or whether the curves are normalized to unity.  
**Required fix:**  
- Expand captions to specify which parameters are shown and how the posteriors are normalized.  

---

P2-m5 (MINOR) – “ECH gravity... 14-barrier catalog”, Sec. 5, p.4–5  
**Problem:** The reference to a “14-barrier catalog” in Golden 2026a is unexplained and potentially confusing in a paper that otherwise focuses on ALP birefringence.  
**Required fix:**  
- Either briefly define what “14-barrier catalog” refers to or remove the phrase; otherwise it reads as unexplained jargon tied to an uncitable companion paper.  

---

P2-n1 (NIT) – Typographic issues and diacritics, throughout  
**Problem:** Minor typographical inconsistencies:  
- “coeﬀicient” with “ﬀ” ligature appears at least once.  
- Spacing around degree symbols occasionally inconsistent (“0◦ ,” “0 ◦”).  
**Required fix:**  
- Standardize typography (use plain “coefficient” and consistent spacing around “°”).  

---

P2-n2 (NIT) – Redundant phrasing in Introduction, p.1  
**Problem:** Minor redundancy: “has emerged as a compelling signal in recent CMB data” and “the evidence exceeds 3.5σ” are somewhat repetitive given the detailed numbers immediately following.  
**Required fix:**  
- Slightly tighten the wording to avoid redundancy (optional).  

---

P2-n3 (NIT) – Small notational mismatches, p.2–3  
**Problem:** The notation for the coupling “C0” vs. “Caγ” vs. “C” vs. “C free” is slightly confusing: in different places, C0, Caγ, and C are used without a single concise definitional equation.  
**Required fix:**  
- Add a short subsection or boxed equation defining all coupling-related symbols and their relationships, and use them consistently in tables and text.  

---

## Summary recommendation
**MAJOR REVISIONS**

The paper has multiple critical issues that prevent acceptance in its current form: key references (ACT DR6 birefringence, Namikawa et al., companion papers) are mis-cited or uncitable; at least one statistical claim uses a non-existent “joint Planck + ACT” analysis; Bayes factors and “no fine-tuning” claims are insufficiently justified; dimensional and normalization issues appear in the ALP prediction; and MCMC chains are too short for the weight placed on their results. These issues must be fully corrected, with verifiable bibliographic details, clarified methodology, and improved numerical consistency, before the work can be considered at PRD’s standard.

---

## PASS 2 — self-critique findings (what initial review missed)

P2-E12 (ESSENTIAL) – Arithmetic/significance of “Combined, the evidence exceeds 3.5σ.”, Introduction, p.1  
**Problem:** The Introduction states: “The Planck HFI analysis … reported β = 0.35 ± 0.14° (2.5σ), and the ACT DR6 analysis confirmed the signal at comparable significance. Combined, the evidence exceeds 3.5σ.”  
- If the two measurements are treated as independent Gaussians with the quoted significances 2.5σ (Planck) and 2.9σ (ACT DR6, from Sec. 3.1), the standard quadrature combination gives \(\sqrt{2.5^2 + 2.9^2} ≈ 3.8σ\), not merely “exceeds 3.5σ,” and more importantly this implicit computation is *not* what is actually used elsewhere in the paper. The rest of the analysis uses the NPIPE value 0.30 ± 0.11° and an ACT 0.215 ± 0.074° result, not the 0.35 ± 0.14° Planck HFI number.  
- Thus the “combined” 3.5σ statement is arithmetically untraceable from the explicitly stated inputs, and it implicitly mixes datasets (HFI vs. NPIPE) and null procedures without explanation.  
**Required fix:**  
- Either (a) remove the “Combined, the evidence exceeds 3.5σ” sentence, or (b) explicitly show the combination formula and specify exactly which β and σ values (HFI vs. NPIPE, DR6 vs. joint analyses) are being combined.  
- Clarify that this “>3.5σ” figure is separate from the 3.9σ summary-likelihood result quoted later, and indicate that they arise from different combinations and are not directly comparable.  

---

P2-E13 (ESSENTIAL) – Arithmetic of “prediction matches … at 1σ”, Discussion, p.6  
**Problem:** The Discussion claims: “The prediction matches the combined Planck + ACT measurement at 1σ.”  
- The model “prediction” emphasized in the paper is β ≈ 0.27°. The combined summary-likelihood result is βcombined = 0.242 ± 0.061°. The difference is |0.27 − 0.242| = 0.028°. Relative to σ = 0.061°, this is ≈0.46σ, which is *within* 1σ, but not “at 1σ” in the usual statistical sense.  
- Using “at 1σ” suggests the prediction sits at the edge of the 68% confidence interval, rather than near its center; this overstates the discrepancy and is numerically imprecise given the already quoted uncertainties.  
**Required fix:**  
- Rephrase the statement to something quantitatively accurate, e.g. “The prediction lies well within the 1σ range of the combined Planck + ACT measurement (≈0.5σ away from the mean).”  
- Ensure that any similar “at nσ” language in the Discussion or Conclusion is aligned with a straightforward \(|\Delta|/σ\) calculation using the numbers given in Sec. 3.2.  

---

P2-E14 (ESSENTIAL) – Dimensional inconsistency in Eq. (2) and Caγ prior, Sec. 2.2 & 3.3, p.2–3  
**Problem:** Eq. (2) defines \(g_{a\gamma} = C_0 / f_a\) and writes \(\beta = (g_{a\gamma}/2)\,\Delta\phi = (C_0/(2f_a))\,\Delta\phi\).[p.2] Under standard conventions, \(g_{a\gamma}\) has dimensions of inverse energy, \(f_a\) has dimensions of energy, and \(\Delta\phi\) has dimensions of energy, so \(\beta\) is dimensionless radians as required.  
However:  
- The priors are later specified as “\(C_{a\gamma}\) flat on [1, 30] (Run 2 only).”[p.3] This introduces a new symbol \(C_{a\gamma}\) with no explicit definition or units, but it is clearly intended to be related to the previous \(C_0\) and/or \(g_{a\gamma}\).  
- The posterior result is then quoted as “\(C_{a\gamma} \times \theta_i = 3.4 ± 1.1\)”[Eq. (8)], treated as a dimensionless “coupling-misalignment product,” but there is no equation showing how \(C_{a\gamma}\) connects back to \(C_0/f_a\) or to the dimensional combination in Eq. (2).  
- This creates a hidden dimensional inconsistency: Eq. (2) uses a dimensionful coupling \(g_{a\gamma}\), while Sec. 3.3 treats \(C_{a\gamma}\) as a pure number in the same role, without specifying the normalization scale that makes it dimensionless.  
**Required fix:**  
- Explicitly define \(C_{a\gamma}\) and its units (e.g., “\(C_{a\gamma} \equiv g_{a\gamma} M_{\rm Pl}\)” or similar), and show the equation that connects \(C_{a\gamma}\) to \(C_0\) and \(f_a\).  
- Rewrite Eq. (8) (and the Run 2 prior description) in a way that keeps track of dimensions consistently, so that the reader can see exactly how a dimensionless product \(C_{a\gamma}\theta_i\) emerges from the dimensionful coupling \(g_{a\gamma}\).  

---

P2-E15 (ESSENTIAL) – Missing definition and dimensional status of “fphoton × C0”, Eq. (5), p.2  
**Problem (distinct from P2-E4):** Eq. (5) states “\(f_{\rm photon} × C_0 = 1.73 ± 0.44\)” but nowhere in the paper is \(f_{\rm photon}\) defined relative to the physical decay constant \(f_a\) or any fixed mass scale. The Introduction and Sec. 2 use \(f_a\) and \(g_{a\gamma} = C_0/f_a\), but \(f_{\rm photon}\) appears only in Eq. (5) and in the Abstract.  
- Without a definition, the reader cannot tell whether \(f_{\rm photon} × C_0\) is dimensionless (e.g., \(f_{\rm photon} \equiv g_{a\gamma} M_{\rm Pl}\)) or has dimensions of energy, and hence cannot interpret “1.73 ± 0.44” physically.  
- Because Eq. (5) is presented as a central numerical result (quoted again in the Abstract), the missing definition prevents any independent recomputation or use of this parameter.  
**Required fix:**  
- Add a clear definition in Sec. 2 or 3 of what \(f_{\rm photon}\) is, including its relation to \(f_a\), \(g_{a\gamma}\), and any reference scale.  
- Show the explicit formula used to derive \(f_{\rm photon} × C_0\) from βcombined and the assumed field evolution (e.g. via \(\Delta\phi/f_a\)), so that a reader can recompute the 1.73 ± 0.44 value from the stated inputs.  

---

P2-M10 (MAJOR) – Internal inconsistency between Eq. (2) text and the factor of 1/2 in the birefringence conversion, Sec. 2.2, p.2  
**Problem (distinct from P2-E11 normalization check):** Eq. (2) clearly states \(\beta = (g_{a\gamma}/2)\Delta\phi\), including the factor 1/2.[p.2] Immediately below, the text says: “For \(C_0 ∼ 1, θ_i ∼ 1: the cosmological field evolution gives \(\Delta\phi/f_a ∼ 10^{-2}\) … yielding \(\beta ≈ C_0 θ_i × 5 × 10^{-3}\,\text{rad} ≈ 0.27°\).” The symbol \(C_0 θ_i\) is used, but the displayed expression “\(× 5×10^{-3}\,\text{rad}\)” does not show the 1/2 factor that appears in Eq. (2).  
- If \(\Delta\phi/f_a ≈ 10^{-2}\), then using Eq. (2) literally yields \(\beta ≈ (C_0 θ_i/2) × 10^{-2} = C_0 θ_i × 5×10^{-3}\) radians, i.e. the 5×10⁻³ rad is **already** the half-reduced value. But the text does not show the intermediate step and initially phrases the estimate in terms of \(\Delta\phi/f_a\); a reader could easily infer that the 1/2 has been dropped.  
- Because the paper repeatedly emphasizes “no fine-tuning” and “order-unity” for these parameters, this kind of normalization ambiguity undermines confidence in the quantitative calibration of β to the underlying ALP parameters.  
**Required fix:**  
- Insert an explicit intermediate step in Sec. 2.2 making clear that the 1/2 from Eq. (2) has been applied, e.g., “With \(\Delta\phi/f_a ≈ 10^{-2}\), Eq. (2) gives \(\beta ≈ (C_0 θ_i/2) × 10^{-2} = C_0 θ_i × 5×10^{-3}\,\text{rad}\).”  
- Ensure that all later uses of this calibration (e.g., in deriving Eq. (5) and the LiteBIRD forecast) reference this clarified normalization, so that a single consistent β–parameter mapping is used throughout.  

---

P2-M11 (MAJOR) – Abstract claims vs. body support for “order-unity, no fine-tuning” and “natural” parameters, Abstract & Sec. 2, 3, 6  
**Problem (beyond earlier tuning-language comments):** The Abstract says the effective photon coupling is “\(f_{\rm photon} × C_0 = 1.73 ± 0.44\) (order-unity, no fine-tuning),” and the Introduction/Discussion repeatedly use the terms “natural” and “no tuning is required.”[Abstract, p.1; Sec. 2.2; Sec. 6]  
However, the body does not:  
- Specify any prior ranges for \(C_0\) (or \(C_{a\gamma}\)) and θi that would allow a quantitative measure of how typical the inferred range 1.73 ± 0.44 is within the assumed parameter space.  
- Provide any calculation of the fraction of prior volume that yields β within the observed 1σ or 2σ band.  
- Discuss sensitivity to changing the prior ranges on θi or the coupling beyond a brief note that they are “O(1).”  
Thus the “no fine-tuning” claim in the Abstract is not actually demonstrated anywhere in the body; it is a qualitative assertion rather than a supported quantitative result.  
**Required fix:**  
- Either remove “no fine-tuning” from the Abstract and replace it with a descriptive but neutral phrase (e.g., “with an effective photon coupling of order unity”), or  
- Add a subsection (e.g., in Sec. 3.3 or 6) that explicitly defines the priors on \(C_0\) (or \(C_{a\gamma}\)) and θi, and computes the probability that β falls in the observed interval, thereby justifying the “no fine-tuning” claim quantitatively.  

---

P2-M12 (MAJOR) – Abstract faithfulness regarding “Planck HFI and ACT DR6 data” vs. actual datasets, Abstract & Sec. 3.1  
**Problem (more specific than P2-M8):** The Abstract states: “We perform a Gaussian summary-likelihood inference using Planck HFI and ACT DR6 data…”[Abstract]  
- In Sec. 3.1, the summary-likelihood inputs are explicitly given as Planck NPIPE [Eskilt & Komatsu 2022] and ACT DR6.[p.2] NPIPE is a distinct reprocessing of Planck data and is *not* the same as the Minami & Komatsu 2020 HFI-only analysis.  
- The Introduction also mentions the HFI Minami & Komatsu result 0.35 ± 0.14° as a separate earlier measurement.[p.1]  
- No actual summary-likelihood combination using the Minami & Komatsu HFI number is presented; all explicit combinations in Sec. 3.2 use the NPIPE value 0.30 ± 0.11°.  
**Required fix:**  
- Correct the Abstract to state “Planck NPIPE and ACT DR6” rather than “Planck HFI and ACT DR6,” unless a separate analysis using the Minami & Komatsu HFI result is included and shown.  
- Add a short clarifying sentence in Sec. 3.1 distinguishing the older HFI result from the NPIPE result used in the main inference, to prevent readers from thinking both are being combined.  

---

P2-M13 (MAJOR) – Abstract faithfulness for “The Bayes factor … ln B = 5.17” vs. numerical robustness discussion, Abstract vs. Sec. 3.3–3.4  
**Problem:** The Abstract presents “The Bayes factor in favor of nonzero rotation is ln B = 5.17 (indicative; prior-dependent, see Sec. 3.4).” This gives the Bayes factor prominent billing as a headline result.  
- In Sec. 3.3 the author explicitly acknowledges that the chain sizes are small (720–6,840 samples, Neff ∼ 1,000) and that this “limits the precision of tail estimates and evidence calculations.”[p.3]  
- Sec. 3.4 characterizes ln B = 5.17 as “indicative evidence” and notes its strong prior dependence, but the Abstract does not mention any limitation beyond a brief parenthetical reference.  
- In the Discussion and Conclusion, the emphasis on “sharp falsifiability” and consistency with data can give the impression that ln B ≈ 5 is a robust, high-precision model-selection result, despite the acknowledged numerical limitations.  
**Required fix:**  
- In the Abstract, explicitly note that the Bayes factor is approximate and based on a simple Gaussian summary-likelihood and modest MCMC chains, e.g., “We estimate a Bayes factor ln B ≈ 5 in favor of nonzero rotation, under Gaussian assumptions and for the priors described in Sec. 3.4.”  
- Adjust the Discussion/Conclusion language so that the Bayes factor is clearly framed as an indicative, prior-dependent diagnostic, not as a definitive model-selection result on par with the quoted σ-level detections.  

---

P2-M14 (MAJOR) – Unexplained reuse of different βobs values and σ-levels across sections (null-procedure comparability), Sec. 1, 3.1, 3.3, 7  
**Problem (beyond P2-M1):** The paper uses several β measurements and significances without clearly keeping track of which null procedure each refers to:  
- Introduction: β = 0.35 ± 0.14° (2.5σ) from Minami & Komatsu 2020, and “Combined, the evidence exceeds 3.5σ.”[p.1]  
- Sec. 3.1: Planck NPIPE β = 0.30 ± 0.11° (2.7σ), ACT DR6 β = 0.215 ± 0.074° (2.9σ), and an “Eskilt et al. joint analysis value βobs = 0.342 ± 0.094°,” which “differs because it fits the full EB cross-spectrum.”[p.2]  
- Abstract & Conclusion: repeated reference to a “3.6σ Eskilt et al. joint Planck + ACT signal,” with βobs = 0.342 ± 0.094°.[Abstract; p.7]  
These multiple βobs and σ combinations are mentioned in close proximity in the Introduction, Sec. 3, and Conclusion, but the text does not systematically flag which σ values are derived from point-estimate combinations versus full-spectrum likelihoods, nor does it warn the reader each time that they are not directly comparable.  
**Required fix:**  
- Add a short subsection or paragraph in Sec. 3 explicitly listing the distinct analyses (HFI self-calibration, NPIPE point estimate, ACT DR6 point estimate, Eskilt joint EB analysis), their βobs and uncertainties, and the specific null procedures used.  
- Whenever a σ level from one of these is compared with another (e.g., when saying the model is “consistent with the 3.6σ Eskilt et al. signal” *and* the 3.9σ combined Planck+ACT point-estimate result), add explicit language that they arise from different likelihood constructions and should not be interpreted as strictly additive or directly comparable.  

---

P2-m1 (MINOR) – Figure 2 caption vs. body wording, p.4 & Sec. 3.3  
**Problem:** Figure 2’s caption says: “All three are consistent with each other and with the observed value βobs = 0.342 ± 0.094°.” The body text in Sec. 3.3 states:  
- Run 1: βALP = 0.336 ± 0.107°  
- Run 3: βfree = 0.344 ± 0.096°  
- Observed: βobs = 0.342 ± 0.094°  
Numerically, the three means are indeed close, but the caption’s “consistent with each other” is qualitative and could be misread as a formal statistical compatibility test having been performed (e.g., χ², p-value). The paper does not present such a test; it simply quotes means and errors.  
**Required fix:**  
- Slightly soften or qualify the caption, e.g., “The three posteriors have nearly identical means and overlapping 1σ ranges, and visually appear consistent with each other and with βobs = 0.342 ± 0.094°.” This makes clear that the statement is descriptive rather than the result of an explicit compatibility test.  

---

P2-m2 (MINOR) – Internal cross-reference precision: “see Sec. 3.4” in Abstract vs. Bayes factor implementation, Abstract & Sec. 3.4  
**Problem:** The Abstract’s parenthetical “(indicative; prior-dependent, see Sec. 3.4)” implies that Sec. 3.4 will provide enough methodological detail to reconstruct ln B = 5.17. In practice, Sec. 3.4 gives:  
- The prior ranges on β for three different Bayes factors.  
- The three ln B values.  
But it does **not** show the explicit formula for the Savage–Dickey ratio in the one-parameter Gaussian case, nor does it state the exact μ and σ that were used (e.g., whether μ = 0.242°, σ = 0.061° from Eq. 4, or slightly different numbers derived directly from the MCMC).  
**Required fix:**  
- In Sec. 3.4, add a one-line formula giving the analytic Savage–Dickey expression for a Gaussian likelihood with mean μ and σ and a uniform prior over [0, βmax], and state explicitly which μ and σ are used.  
- This will make the Abstract’s “see Sec. 3.4” pointer accurate, in the sense that a reader could reconstruct ln B numerically from the information given.  

---

If you would like, I can now step through all σ-level and Bayes-factor calculations explicitly (using the stated inputs) to provide a line-by-line numerical check you can paste into your revision notes.