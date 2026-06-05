# P2 R10v3p1 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (16853 chars)
**Wall time**: 68.5s

---

P2 contains **multiple essential citation and arithmetic failures** that prevent acceptance in PRD as written. The paper also relies on several unsupported or internally inconsistent claims about the cited birefringence measurements, the ALP parameterization, and the bibliography.

- **P2-E1 — Abstract, p. 1**
  - **Problem:** “*the 3.6σ isotropic birefringence signal (βobs = 0.342±0.094◦ from the Eskilt et al. joint Planck + ACT analysis)*”
  - **Why this is a problem:** The paper elsewhere calls this the “observed value” but does not show a derivation of \(0.342/0.094 = 3.64\), and it is not established in the paper that this value is the correct joint Planck+ACT result rather than a model-dependent summary quantity. The abstract treats it as a load-bearing datum without proof from the body.
  - **Required fix:** State exactly what dataset and estimator produced \(0.342\pm0.094^\circ\), and show the calculation of the quoted significance from those numbers.

- **P2-E2 — Abstract and Sec. 3.2, pp. 1–2**
  - **Problem:** “*We perform a Gaussian summary-likelihood inference using Planck HFI and ACT DR6 data, finding β = 0.242 ± 0.061◦ (3.9σ from zero)*”
  - **Why this is a problem:** The paper claims a combined result but never shows the explicit weighted-average computation from the two quoted measurements in Sec. 3.1. Using the listed inputs \(0.30\pm0.11\) and \(0.215\pm0.074\), the inverse-variance weighted mean is indeed close to \(0.242\), but the uncertainty and significance must be recomputed explicitly in the text. As written, the inference is under-documented for a key abstract claim.
  - **Required fix:** Show the exact weighting formula, the propagated uncertainty, and the resulting sigma significance from zero using the displayed inputs.

- **P2-M1 — Sec. 2.1, p. 2**
  - **Problem:** “*\(\Delta\phi \approx f_a\theta_i [1-J_0(m/H_0)/J_0(0)]\)*”
  - **Why this is a problem:** This expression is presented without derivation and uses a Bessel-function ansatz that is not standard for late-time ALP slow-roll evolution. The paper gives no dimensional or dynamical justification for \(J_0(m/H_0)\), and \(J_0(0)=1\) makes the normalization trivial.
  - **Required fix:** Derive the expression from the field equation in the stated cosmology, or replace it with a standard numerical integration result.

- **P2-E3 — Sec. 2.2, p. 2**
  - **Problem:** “*For \(C_0\sim1\), \(\theta_i\sim1\): the cosmological field evolution gives \(\Delta\phi/f_a\sim10^{-2}\) … yielding \(\beta\approx C_0\theta_i\times5\times10^{-3}\,\mathrm{rad}\approx0.27^\circ\).*”
  - **Why this is a problem:** This is not consistent with the paper’s own setup. If \(\beta=\Delta\phi/(2f_a)\), then \(\beta\sim 5\times10^{-3}\,\mathrm{rad}\) corresponds to \(0.286^\circ\), but the text simultaneously asserts \(\Delta\phi/f_a\sim10^{-2}\), which would indeed give \(5\times10^{-3}\,\mathrm{rad}\). The issue is that the paper never shows how the factor \(10^{-2}\) follows from the preceding dynamics, and the statement “every input is O(1)” is incompatible with the explicit small numerical factor that drives the entire prediction.
  - **Required fix:** Provide a quantitative derivation of \(\Delta\phi/f_a\) from the background evolution and explain the origin of the \(10^{-2}\) factor.

- **P2-E4 — Sec. 3.1, p. 2**
  - **Problem:** “*Planck NPIPE [Eskilt and Komatsu, 2022]: \(\beta = 0.30\pm0.11^\circ\) (2.7σ)*” and “*ACT DR6 [Diego-Palazuelos and Komatsu, 2025]: \(\beta = 0.215\pm0.074^\circ\) (2.9σ)*”
  - **Why this is a problem:** The paper gives no citations to arXiv IDs, titles, or journal metadata for the ACT result, and the reference list only says “arXiv preprint, 2025.” That is inadequate for PRD citation standards.
  - **Required fix:** Replace the placeholder reference with the full arXiv ID, title, authors, and publication status, and verify the quoted central values against the cited paper.

- **P2-M2 — Sec. 3.2, p. 2**
  - **Problem:** “*The combined constraint is: \(\beta_{\rm combined}=0.242\pm0.061^\circ\) (3.9σ from zero)*”
  - **Why this is a problem:** The paper never demonstrates that the combination is statistically independent or that the two input measurements can be combined with the simple product likelihood shown. If one of the inputs is derived from a subset or closely related analysis to the other, the independence assumption may be invalid.
  - **Required fix:** Demonstrate the statistical independence of the two datasets or use the appropriate correlated likelihood.

- **P2-E5 — Sec. 3.2, Eq. (5), p. 2**
  - **Problem:** “*The effective photon coupling parameter: \(f_{\rm photon}\times C_0 = 1.73\pm0.44\)*”
  - **Why this is a problem:** This parameter is undefined. The paper uses \(g_{a\gamma}=C_0/f_a\) earlier, but now introduces \(f_{\rm photon}\) without definition or relation to \(f_a\). The quantity is dimensionally ambiguous and not traceable to a standard ALP parameter.
  - **Required fix:** Define \(f_{\rm photon}\), state its dimensions, and show how Eq. (5) is obtained from the fitted birefringence amplitude.

- **P2-N1 — Table 1, p. 2**
  - **Problem:** “*All runs converge to \( \hat R-1<0.01\).*”
  - **Why this is a problem:** The paper lists only accepted sample counts, not chain lengths, number of independent chains, autocorrelation times, or effective sample sizes per parameter. Claiming convergence from \(\hat R\) alone is incomplete.
  - **Required fix:** Provide full MCMC diagnostics, including number of chains, total steps, burn-in, and effective sample sizes for the quoted posteriors.

- **P2-E6 — Sec. 3.3, p. 3**
  - **Problem:** “*Priors: \(\theta_i\) flat on [0.01, π]; \(\log_{10}(m/\mathrm{eV})\) flat on [−35, −30]; \(C_{a\gamma}\) flat on [1, 30] (Run 2 only).*”
  - **Why this is a problem:** These prior ranges are extremely broad and the paper later claims the Bayes factor is meaningful. The Bayes factor is explicitly prior-dependent, but the paper does not demonstrate robustness of the quoted evidence to the prior volumes beyond three ad hoc choices for \(\beta\).
  - **Required fix:** Quantify the sensitivity of the posterior and evidence to the full prior specification on all parameters, not just \(\beta\).

- **P2-M3 — Sec. 3.3, p. 3**
  - **Problem:** “*The posterior on β from the ALP model (Run 1, C = 8 fixed): \(\beta_{\rm ALP}=0.336\pm0.107^\circ\) compared to the model-independent fit (Run 3): \(\beta_{\rm free}=0.344\pm0.096^\circ\).*”
  - **Why this is a problem:** The paper compares two uncertainties but does not say whether they come from the same likelihood or the same priors; these values are therefore not directly comparable. This is exactly the kind of side-by-side comparison that requires an explicit caveat.
  - **Required fix:** State whether the two posteriors are derived from identical likelihoods and priors, and add an explicit “not directly comparable” qualification if they are not.

- **P2-M4 — Sec. 3.4, p. 3**
  - **Problem:** “*ln B = 5.17 computed via the Savage-Dickey density ratio with a flat prior β ∈ [0°, 1°].*”
  - **Why this is a problem:** The paper quotes multiple Bayes factors for different prior widths, but gives no derivation of the numerical value \(5.17\). It is not verified against the displayed posterior density at zero, and the result is strongly prior-volume dependent.
  - **Required fix:** Show the full Savage-Dickey calculation and present the prior density at \(\beta=0\) used for each quoted \(\ln B\).

- **P2-M5 — Sec. 4, p. 3**
  - **Problem:** “*For our prediction \(\beta=0.27^\circ\): Significance = 0.27/0.03 = 9σ*”
  - **Why this is a problem:** This calculation ignores the uncertainty in the predicted \(\beta\), which the paper itself elsewhere gives as model-dependent and not exact. A forecast significance should fold in both experimental and theoretical uncertainties if the latter are non-negligible.
  - **Required fix:** Include the model uncertainty on the predicted angle or explicitly state that the 9σ is only relative to the experimental error bar.

- **P2-N2 — Figure 1, p. 4**
  - **Problem:** “*Triangle plot from the extended ALP MCMC (Run 2, C free).*”
  - **Why this is a problem:** The figure is described but not shown in the text provided in a way that permits auditing of axis labels, priors, or numerical contours. The caption also uses the undefined product \(C_{a\gamma}\times\theta_i\) without clarifying the parameterization in the actual sampled space.
  - **Required fix:** Include the full figure with axis labels, units, and contour levels, and specify exactly which parameter combinations were sampled.

- **P2-E7 — Sec. 5, p. 4**
  - **Problem:** “*the Barbero-Immirzi pseudoscalar sector of the Holst action, providing a natural theoretical context for \(f_a\sim M_{\rm Pl}\); see the companion paper [Golden, 2026a] for the full ECH framework and 14-barrier catalog.*”
  - **Why this is a problem:** This is speculative framing, not a derivation. It imports an external framework without demonstrating any actual mapping to the ALP action used in the paper.
  - **Required fix:** Either supply a derivation or remove the claim that the Holst action motivates the parameter choice.

- **P2-M6 — Sec. 5, p. 4**
  - **Problem:** “*see the companion paper [Golden, 2026a] for the full ECH framework and 14-barrier catalog*”
  - **Why this is a problem:** This is internal-bookkeeping language and depends on a companion paper that is not part of the present argument. It also reads like draft-level cross-referencing rather than a publication-ready citation.
  - **Required fix:** Replace with a normal external citation or remove the phrase.

- **P2-M7 — Sec. 6, p. 5**
  - **Problem:** “*The matter-bounce non-Gaussianity \(f_{\rm NL}=-35/8\) provides a complementary and independent test [Golden, 2026b].*”
  - **Why this is a problem:** This is a dangling claim: the paper does not connect the stated non-Gaussianity to the ALP birefringence model, and the cited companion paper is not a proper reference.
  - **Required fix:** Either remove the sentence or explain why it is relevant to the present ALP model.

- **P2-E8 — Sec. 6, p. 5**
  - **Problem:** “*Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces \(\beta\sim0.3^\circ\)*”
  - **Why this is a problem:** The paper does not verify that this exact quantitative claim appears in the cited PRD article, nor does it provide a page, equation, or table reference. As written, the statement is a quotation-like attribution without traceability.
  - **Required fix:** Add the exact equation or table from the cited source that supports the numerical claim.

- **P2-E9 — References, p. 6**
  - **Problem:** “*P. Diego-Palazuelos and E. Komatsu. Cosmic birefringence from the Atacama Cosmology Telescope. arXiv preprint, 2025.*”
  - **Why this is a problem:** The reference is incomplete. The paper should include the arXiv ID, full author list, and title exactly as on arXiv/NASA ADS. The current entry is not acceptable for a PRD bibliography.
  - **Required fix:** Replace with a complete bibliographic entry and verify the metadata against arXiv and ADS.

- **P2-E10 — References, p. 6**
  - **Problem:** “*Toshiya Namikawa, Kai Murai, and Sho Naokawa. Constraints on axion-like particles from cosmic birefringence. arXiv e-prints, 2025. In preparation; cited for comparison of ALP mass constraints.*”
  - **Why this is a problem:** “In preparation” is not a citable publication. The reference is unverifiable and functionally a placeholder.
  - **Required fix:** Remove the citation unless a public arXiv/preprint record exists and replace it with the actual bibliographic metadata.

- **P2-M8 — References, p. 6**
  - **Problem:** The bibliography mixes published papers, incomplete arXiv placeholders, and companion papers labeled “submitted simultaneously” without formal bibliographic data.
  - **Why this is a problem:** PRD requires reproducible references. The current bibliography is not audit-ready and contains stale or nonstandard entries.
  - **Required fix:** Normalize all references to standard bibliographic form and remove any placeholder or internal-status language.

- **P2-N3 — Entire paper**
  - **Problem:** The paper is only 6 pages but makes multiple substantial claims: a new prediction, a data combination, MCMC inference, Bayes factors, and a LiteBIRD forecast.
  - **Why this is a problem:** For the breadth of claims, the manuscript is too compressed to be methodologically convincing. Key derivations, likelihood definitions, and diagnostic checks are underdeveloped.
  - **Required fix:** Expand the methods and append the exact likelihood, priors, chain diagnostics, and derivations. A realistic target is **8–10 pages** for the main text, plus references/appendix if needed.

- **P2-M9 — Abstract, p. 1**
  - **Problem:** “*This birefringence prediction is independent of bounce cosmology and can be tested regardless of whether the universe underwent a contracting phase.*”
  - **Why this is a problem:** This is not supported by any calculation in the paper; it is an unsupported novelty/independence claim.
  - **Required fix:** Either remove the statement or provide a clear argument showing why the prediction is mathematically independent of the bounce scenario.

- **P2-N4 — Sec. 1, p. 1**
  - **Problem:** “*Combined, the evidence exceeds 3.5σ.*”
  - **Why this is a problem:** This is an unsupported synthesis of multiple measurements with no combined statistic shown. The paper later quotes 3.9σ from its own weighted combination, which is not the same statement.
  - **Required fix:** Distinguish clearly between the significance of the literature-level evidence and the paper’s own combined estimate.

- **P2-M10 — Sec. 2.2, p. 2**
  - **Problem:** “*C0 is an order-unity coefficient from the ABJ anomaly.*”
  - **Why this is a problem:** The normalization of \(C_0\) is not fixed, and the notation conflicts with later \(C_{a\gamma}\). This is a fused/unstable parameterization.
  - **Required fix:** Use one consistent symbol for the axion-photon coupling coefficient and define it unambiguously.

- **P2-N5 — References, p. 6**
  - **Problem:** “*LiteBIRD Collaboration. LiteBIRD science goals and forecasts: a full-sky cmb polarization survey. Prog. Theor. Exp. Phys., 2023:042F01, 2023.*”
  - **Why this is a problem:** The title capitalization and venue formatting are nonstandard, and the citation is not given in a form that can be cleanly matched to ADS.
  - **Required fix:** Standardize the title and verify the journal metadata exactly.

- **P2-M11 — Figure 2, p. 4**
  - **Problem:** “*Comparison of β posteriors across all three model configurations … All three are consistent with each other and with the observed value*”
  - **Why this is a problem:** This is a qualitative claim unsupported by a quantitative overlap metric. The figure caption asserts consistency without giving credible intervals or evidence ratios.
  - **Required fix:** Add explicit posterior summaries or a metric of agreement.

- **P2-N6 — Sec. 3.3, p. 3**
  - **Problem:** “*small effective sample sizes (\(N_{\rm eff}\sim1{,}000\))*”
  - **Why this is a problem:** This is not tied to any reported chain statistics or parameter-wise effective sample sizes. It is an unverified audit statement inside the results section.
  - **Required fix:** Report the actual \(N_{\rm eff}\) values per parameter and chain.

- **P2-E11 — References, p. 6**
  - **Problem:** The paper cites “*Minami and Komatsu, 2020*” and “*Eskilt and Komatsu, 2022*” but does not verify whether the quoted numbers match the cited articles’ abstract/table values.
  - **Why this is a problem:** The manuscript uses these numbers as the foundation of the entire analysis, so the exact provenance must be traceable.
  - **Required fix:** Add a short table giving the source, exact quoted value, and location in the source paper.

## Summary recommendation
**REJECT**

This manuscript is not ready for PRD because its central numerical claims are insufficiently traced, several references are incomplete or non-citable, and multiple load-bearing statements are unsupported or internally under-justified. The combination of citation metadata failures, placeholder-style bibliography entries, weak derivations for the ALP prediction, and under-documented inference machinery means the paper does not meet the standard for reproducibility or auditability required by the journal.

---

## PASS 2 — self-critique findings (what initial review missed)

P2-E12 — Abstract vs. body, σ-level of “3.6σ” joint signal  
- **Problem:** The abstract calls the Eskilt et al. joint Planck+ACT result “the 3.6σ isotropic birefringence signal (βobs = 0.342±0.094◦)”, but nowhere in the body is 3.6σ derived or even mentioned; Sec. 3.1 only restates the value and uncertainty and then uses it for MCMC, without detailing any hypothesis test or null distribution.  
- **Why this is a problem:** The σ level is a *primary headline number* for the paper but is not traced to any explicit test statistic or likelihood in the text, nor is it described as coming from Eskilt et al. rather than from the simple ratio 0.342/0.094. This is another abstract claim without in‑paper derivation or clear attribution.  
- **Required fix:** Either (a) explicitly state that 3.6σ is the significance reported by Eskilt et al. and cite the exact equation/table, or (b) show the computation of the 3.6σ value from βobs and its uncertainty and state what null model it refers to.


P2-E13 — Sec. 1, “Combined, the evidence exceeds 3.5σ” vs. quoted numbers  
- **Problem:** Sec. 1 cites Planck HFI β = 0.35 ± 0.14◦ (2.5σ) and says “the ACT DR6 analysis confirmed the signal at comparable significance. Combined, the evidence exceeds 3.5σ.” No ACT value is given in Sec. 1, and the only ACT number in the paper is β = 0.215 ± 0.074◦ (2.9σ) in Sec. 3.1. A proper inverse‑variance combination of 2.5σ and 2.9σ is not shown anywhere.  
- **Why this is a problem:** The 3.5σ statement is a new combined significance not derived in the text and not obviously equal to any of the later “3.9σ from zero” claims. It is numerically inconsistent with the later combined result (3.9σ), yet is presented as if summarizing literature.  
- **Required fix:** Either remove this sentence or explicitly compute and show the combined significance from the actual literature values, making clear whether it refers to Minami+Komatsu + ACT, to Eskilt+Komatsu alone, or to some other set, and ensure it is consistent and not double‑counting the same sky.


P2-E14 — Sec. 2.1 vs. Sec. 2.2, inconsistent scaling of Δϕ/fa  
- **Problem:** Eq. (1) states Δϕ ≈ fa θi × O(1), and explicitly for m/H0 ∼ 1 uses 1 − J0(1) ≈ 0.24, i.e. Δϕ/fa ∼ 0.24 θi (order unity). Sec. 2.2 then asserts “the cosmological field evolution gives Δϕ/fa ∼ 10−2 … yielding β ≈ C0 θi × 5 × 10−3 rad ≈ 0.27◦.” The body never reconciles the 0.24 factor with 10−2, and no intermediate suppression mechanism is given.  
- **Why this is a problem:** These two sections give mutually incompatible orders of magnitude for the same quantity. The final β prediction depends crucially on Δϕ/fa ∼ 10−2, not on the O(1) value implied by Eq. (1). This is a **stale internal inconsistency**: Eq. (1) looks like an earlier rough estimate that was not updated to match the later calibrated 10−2 factor.  
- **Required fix:** Re-derive Δϕ/fa in a single consistent framework. Either update Eq. (1) to contain the 10−2 scale with explicit justification, or adjust Sec. 2.2 to use the same numerical factor as Eq. (1) and recompute β. As it stands, the prediction β ≈ 0.27◦ is not tied to a coherent Δϕ/fa calculation.


P2-E15 — Eq. (2) normalization vs. later use of C0 and Caγ  
- **Problem:** Eq. (2) writes β = gaγ Δϕ/2 = C0Δϕ/(2fa) and then approximates β ≈ C0 θi × O(1)/2, but Sec. 2.2 later rewrites the prediction as β ≈ C0 θi × 5 × 10−3 rad with no factor of 1/2, and Sec. 3.3 introduces Caγ as a separate coupling with a product Caγ × θi = 3.4 ± 1.1.  
- **Why this is a problem:** The paper alternates between C0 and Caγ, sometimes including the 1/2 factor from β = Δϕ/(2fa) and sometimes apparently absorbing it into C0 or Caγ. This produces a risk of a hidden factor‑of‑two error in the numerical mapping between Caγ × θi and β, and makes it impossible to reconstruct the exact normalization used to get β ≈ 0.27◦.  
- **Required fix:** Unify the notation (single symbol for the dimensionless anomaly coefficient), explicitly state whether the factor of 1/2 is absorbed into that symbol or kept separate, and show the full numerical mapping from Caγ × θi in Eq. (8) to β in degrees. Confirm that no factor‑of‑two mismatch is present.


P2-E16 — Sec. 3.2, Gaussian likelihood Eq. (3) missing σi factor and ambiguous notation  
- **Problem:** Eq. (3) writes  
  \(L(\beta) = \prod_i \frac{1}{\sqrt{2\pi\sigma_i^2}}\exp\left[-(\beta^{\rm obs} - \beta)^2/(2\sigma_i^2)\right]\)  
  but in the text it is typeset as  
  \(\prod_i 1/\sqrt{2\pi\sigma_i^2} \exp(- (β^{\rm obs}-β)_i^2 / 2σ_i^2)\) with βobs and σi indices not clearly attached and the parentheses inconsistent. There is no explicit statement that βobs,i and σi correspond to the Planck and ACT entries in Sec. 3.1.  
- **Why this is a problem:** As written, the equation is syntactically and notationally sloppy: the subscript i appears in the exponent but not in βobs in the prefactor, and the 1/(2σi^2) factor is outside the squared difference in the body text markup. For a two‑point Gaussian combination whose result is central to the paper, the likelihood expression needs to be unambiguous.  
- **Required fix:** Rewrite Eq. (3) with explicit indices and parentheses, e.g. \(L(\beta) = \prod_i [1/\sqrt{2\pi\sigma_i^2}] \exp[-(\beta_{{\rm obs},i}-\beta)^2/(2\sigma_i^2)]\), and explicitly map i = Planck, ACT with their numerical values. Verify that Eq. (4) follows from this exact likelihood.


P2-E17 — Sec. 3.3, “Neff ∼ 1,000” vs. Table 1 sample counts  
- **Problem:** Sec. 3.3 states “these sample sizes (720–6,840 accepted samples) are modest… the small effective sample sizes (Neff ∼ 1,000) limit the precision of tail estimates.” Table 1 lists only “Samples” (2,160; 6,840; 720) but no separate Neff. For Run 3, 720 total accepted samples cannot plausibly yield Neff ≈ 1,000.  
- **Why this is a problem:** The stated effective sample size is numerically inconsistent with the total sample counts for at least one run, and no chain length, thinning, or number of chains is given that could resolve this. This appears to be a **stale, untraceable number** and undermines the credibility of the MCMC diagnostics.  
- **Required fix:** Report the actual Neff per parameter and per run, and ensure they do not exceed the total number of samples in any run. If Neff ≈ 1,000 refers only to Run 2, say so explicitly and remove or correct any overstated effective sizes.


P2-E18 — Sec. 3.3, “ALP model reproduces the observed birefringence with no tension” without quantitative comparison  
- **Problem:** Sec. 3.3 claims “The ALP model reproduces the observed birefringence with no tension” after quoting βALP = 0.336 ± 0.107◦, βfree = 0.344 ± 0.096◦, and βobs = 0.342 ± 0.094◦. No quantitative measure of “tension” is provided.  
- **Why this is a problem:** The phrase “no tension” is an unquantified hedge. Even though the central values are close, the paper does not show a Δβ/σcombined or a Bayes factor comparing βALP vs. βfree vs. βobs. PRD generally expects claims about tension/consistency to be backed by explicit statistics.  
- **Required fix:** Provide a simple measure, e.g. |βALP − βobs|/√(σALP^2 + σobs^2), and state the resulting σ‑difference. If it is clearly < 1σ, then the “no tension” language is justified; otherwise soften the claim and report the actual level.


P2-E19 — Sec. 3.4, multiple ln B values without checked consistency  
- **Problem:** Sec. 3.4 quotes ln B = 5.17 for β ∈ [0°,1°], ln B = 4.48 for β ∈ [0°,2°], and ln B = 5.86 for β ∈ [0°,0.5°], all “computed via the Savage-Dickey density ratio,” but gives neither the posterior density at β = 0 nor the normalization of the priors.  
- **Why this is a problem:** These three ln B values imply posterior density at β = 0 changing in a specific way with prior width, and the paper gives no numerical check that these values are internally consistent with the reported β posteriors (e.g., βfree = 0.344 ± 0.096◦). Given the Gaussian‑like posteriors, one can naively approximate ln B; the stated numbers look plausible but are not verified, and readers cannot reproduce them. This is another instance of **null‑procedure comparability**: different prior choices yield different ln B, but the text does not quantify the induced spread relative to statistical uncertainty.  
- **Required fix:** Show the posterior density value at β = 0 used in the Savage‑Dickey calculation, indicate how it was estimated (kernel density, histogram, etc.), and demonstrate that all three quoted ln B follow from the same posterior. Add a short statement quantifying how much ln B varies when the prior width is doubled/halved.


P2-E20 — Sec. 4, “If LiteBIRD measures β = 0 ± 0.03◦, the ALP explanation is excluded at 9σ”  
- **Problem:** The text takes 0.27/0.03 = 9 and interprets this as an exclusion “at 9σ,” ignoring any theoretical/model uncertainty in the prediction and treating the σ purely as the experimental σ(β). This is acknowledged implicitly only by saying the significance is “9σ” but not specifying “experimental-only.”  
- **Why this is a problem:** This is an *over-interpretation* of the 9σ number: it conflates an experimental detection significance with the rejection significance of a model prediction that itself has unquantified spread (e.g., variations in C0, θi, m/H0). As used, 9σ is a strong rhetorical claim not backed by a combined error budget.  
- **Required fix:** Explicitly state that “9σ” is computed using only the forecasted experimental uncertainty, and either (a) provide an estimate of the theoretical uncertainty in β and show the combined significance, or (b) qualify the sentence to say “up to 9σ under the assumption that the theoretical prediction is exact.”


P2-E21 — Fig. 1 caption vs. text: Caγ × θi vs. C0 notation  
- **Problem:** The Fig. 1 caption refers to “the coupling-misalignment product Caγ × θi” centered at 3.4 ± 1.1, consistent with order‑unity natural values. Sec. 3.3 uses the same notation in Eq. (8) but elsewhere the paper defines C0 from the ABJ anomaly and gaγ = C0/fa. No explicit equation connects Caγ in Fig. 1/Eq. (8) to C0 in Eq. (2) or to the “effective photon coupling” fphoton × C0 in Eq. (5).  
- **Why this is a problem:** The figures and main text use overlapping but non‑identical symbols for the same physical quantity (axion‑photon coupling), preventing readers from checking whether the sampled Caγ × θi posterior is consistent with the fphoton × C0 inferred from βcombined. This is a **figure‑vs‑body mismatch in parameterization**.  
- **Required fix:** Add a sentence in Sec. 3.3 or the Fig. 1 caption defining Caγ explicitly and relating Caγ × θi numerically to the C0, fphoton combination in Eq. (5). Check that the central values are consistent when mapped into the same parameter space.


P2-E22 — Fig. 2 caption vs. “matches at 1σ” in Discussion  
- **Problem:** Fig. 2’s caption claims “All three [β posteriors] are consistent with each other and with the observed value βobs = 0.342 ± 0.094◦.” Sec. 6 then states “The prediction matches the combined Planck + ACT measurement at 1σ.” However, the actual central values quoted are βALP = 0.336 ± 0.107◦, βfree = 0.344 ± 0.096◦, βobs = 0.342 ± 0.094◦, and βcombined = 0.242 ± 0.061◦; the prediction 0.27◦ is not directly plotted in Fig. 2 or compared numerically to βcombined.  
- **Why this is a problem:** The phrase “matches … at 1σ” is not backed by any explicit comparison between βprediction = 0.27◦ and βcombined = 0.242 ± 0.061◦ (or βobs), and Fig. 2 does not show the prediction as a distinct curve or band. This is another unquantified consistency claim bridging different β definitions (prediction vs. combined vs. joint analysis).  
- **Required fix:** Either (a) show βprediction as a vertical line or prior in Fig. 2 and quantify the overlap with βcombined (e.g., |0.27−0.242|/0.061 ≈ 0.46σ), or (b) add a short computation in Sec. 6 explicitly giving the σ difference. Clarify which posterior (combined, joint, or model‑independent) is meant by “combined Planck + ACT measurement.”


P2-E23 — Sec. 5, “prediction holds in any cosmological background where the ALP field begins rolling at z ∼ 1”  
- **Problem:** Sec. 5 asserts that the prediction “holds in any cosmological background where the ALP field begins rolling at z ∼ 1,” but the dynamical estimate in Sec. 2.1 (via Eq. (1)) was derived assuming standard late‑time ΛCDM expansion (explicit use of H0 and a specific J0(m/H0) factor). No calculation is shown for non‑ΛCDM backgrounds or for modified expansion histories.  
- **Why this is a problem:** This is a **new universality claim** going beyond what is calculated; whether the ALP begins rolling at z ∼ 1 depends on the detailed H(z), and the resulting Δϕ also depends on the integral of H−1 over time. The paper does not show that Δϕ/fa is insensitive to the detailed background beyond the rolling redshift.  
- **Required fix:** Either soften the statement (“in standard ΛCDM-like backgrounds”) or add a short argument or appendix showing that for a wide class of late‑time H(z) histories with the same onset redshift, the resulting Δϕ/fa and hence β vary only at the O(1) level, preserving the prediction.


P2-E24 — Sec. 6, “prediction matches … at 1σ” vs. ALP prior/likelihood differences  
- **Problem:** The Discussion’s bullet (2) says “The prediction matches the combined Planck + ACT measurement at 1σ.” The combined measurement is derived under a *model‑independent* β likelihood (Sec. 3.2), whereas the ALP prediction in Sec. 2.2 relies on specific priors on θi, m, and C0 and uses Eskilt’s joint analysis value for calibration in the MCMC (Sec. 3.3). These are not the same null procedure.  
- **Why this is a problem:** This is another instance of **null-procedure comparability**: the “1σ” closeness is being used rhetorically without clarifying that one side comes from a simple Gaussian summary likelihood and the other from a specific ALP parameter prior plus dynamical model. Without this caveat, readers may interpret the 1σ agreement as more robust than it is.  
- **Required fix:** Add a qualification noting that the 1σ comparison is between a model prediction and a model-independent combined estimate, and that the exact level of agreement depends on the chosen priors and cosmology. Optionally, provide the posterior predictive distribution for β under the ALP model and compare that distribution to βcombined.


P2-E25 — Sec. 6, “Namikawa, Murai & Naokawa [Namikawa et al., 2025] provide superior ALP mass constraints”  
- **Problem:** The text claims the 2025 Namikawa et al. work provides “superior ALP mass constraints using the full Planck EB spectrum,” but the reference is listed as “In preparation; cited for comparison of ALP mass constraints.” There is no quantitative comparison of mass bounds in the paper and no public result to check.  
- **Why this is a problem:** This is both an **unsupported novelty/comparison claim** and a pointer to a non‑public source. It suggests that the current paper’s constraints are subdominant and uses that fact rhetorically, but provides no numbers and no reproducible citation.  
- **Required fix:** Remove the claim or replace it with a comparison to an actually published/preprint source with explicit mass bounds. If Namikawa et al. is now public, update the reference to full arXiv/journal metadata and quote the relevant ALP mass constraints numerically.


P2-E26 — Appendices absent vs. references in main text to “full ECH framework and 14-barrier catalog”  
- **Problem:** Sec. 5 refers to “the companion paper [Golden, 2026a] for the full ECH framework and 14-barrier catalog” and Sec. 6 references [Golden, 2026b] for fNL = −35/8. There is no appendix in this paper containing any of these derivations or catalogs; both are external and currently only cited as “Companion paper, submitted simultaneously.”  
- **Why this is a problem:** The main text leans on external, non‑published companion work for background on ECH gravity and the matter‑bounce non‑Gaussianity, but does not present any self-contained derivation or even a concise summary in an appendix. This falls under **appendix vs. main-text mismatch** in the sense that key theoretical context is outsourced to non‑auditable documents.  
- **Required fix:** Either remove these references as structural support for the present paper’s claims, or (preferably) summarize the minimal needed ECH/matter‑bounce results in an appendix, with clear equations and assumptions, so that the current paper is self-contained even if the companions remain unpublished.


If you want, I can next go through and explicitly recompute every σ and combined value (Planck+ACT combination, Bayes factors under Gaussian approximations, etc.) and list the exact numerical checks so you can see which ones are correct and which need recalculation or clearer documentation.