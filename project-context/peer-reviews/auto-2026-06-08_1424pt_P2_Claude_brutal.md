# P2 auto-2026-06-08_1424pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (11596 chars)
**Wall time**: 250.6s

---

# Referee Report: P2 — "Cosmic Birefringence from a Planck-Scale Axion-Like Particle"

## Overall assessment

This is a short (6-page) paper that re-derives a well-known result from the literature (Fujita, Murai, Nakatsuka & Tsujikawa 2021) with weaker rigor, adds a Gaussian summary-likelihood combination of two public measurements that any reader could do in 5 minutes, and an underpowered MCMC. The author explicitly acknowledges in §6 that the model class is "well-studied" and that Fujita et al. (2021) "already demonstrated that a Planck-scale ALP naturally produces β∼0.3°." That is a striking self-admission that undercuts the novelty case. The "natural" prediction β ≈ 0.27° is not derived — the cosmological integration factor that fixes the answer is asserted to be "∼10⁻²" without computation, and the load-bearing O(1) factor is parametrized as "× O(1)" everywhere. There is also significant internal inconsistency between the abstract's quoted numbers and the body.

This paper does not meet the PRD bar.

---

## ESSENTIAL findings

**P2-E1 — Abstract/body inconsistency on the headline "observed" value (Abstract, p.1 vs §3.1 p.2).**
The abstract states "β_obs = 0.342 ± 0.094° from the Eskilt et al. joint Planck + ACT analysis." But §3.1 lists the two inputs used in the combination as:
- Planck NPIPE: 0.30 ± 0.11°
- ACT DR6: 0.215 ± 0.074°
Recomputing the inverse-variance-weighted combination of these two: w₁=1/0.11²=82.6, w₂=1/0.074²=182.6, combined mean = (82.6×0.30 + 182.6×0.215)/(82.6+182.6) = 64.04/265.3 = **0.241°**, σ = 1/√265.3 = **0.0614°**. That matches Eq. (4) (0.242 ± 0.061°). But this is **not** the "Eskilt et al. joint Planck + ACT" value of 0.342 ± 0.094° quoted in the abstract. The paper is conflating two different numbers: a homemade Gaussian combination (0.242°) and a literature value (0.342°). The abstract claim "3.6σ isotropic birefringence signal (β_obs = 0.342 ± 0.094°)" attributes a number to a paper while the body's actual combined constraint disagrees with it at the ~1σ level. Required fix: pick one, cite it correctly, and remove the conflation.

**P2-E2 — The "3.9σ" and "3.6σ" significances are not directly comparable and are juxtaposed without warning.**
Abstract: "3.6σ isotropic birefringence signal" (Eskilt et al.) and "β = 0.242 ± 0.061° (3.9σ from zero)" from the author's combination. These come from different procedures (full EB-spectrum joint fit vs. naive Gaussian combination of point estimates with independent-error assumption), produce *different central values* (0.342° vs 0.242°), and yet are presented as if mutually reinforcing. Per review rule #7, this requires an explicit "not directly comparable" qualifier; none appears.

**P2-E3 — The headline "natural" prediction β ≈ 0.27° is not derived.**
§2.2 p.2: "the cosmological field evolution gives Δϕ/f_a ∼ 10⁻² (from the ratio of field displacement to decay constant over the Hubble time), yielding β ≈ C₀ θ_i × 5×10⁻³ rad ≈ 0.27°." But §2.1 Eq. (1) gives Δϕ ≈ f_a θ_i (1 − J₀(m/H₀)) ≈ f_a θ_i × 0.24 for m/H₀ ∼ 1, which gives Δϕ/f_a ∼ 0.24, **not 10⁻²**. These two estimates of the same quantity disagree by a factor of ~25. Plugging Δϕ/f_a = 0.24 into Eq. (2) with C₀ ∼ θ_i ∼ 1 gives β ≈ 0.12 rad ≈ 7°, not 0.27°. The author has not actually shown the prediction is natural; the factor-of-25 gap is silently absorbed into "× O(1)." This is the central scientific claim of the paper and it is unsupported.

**P2-E4 — Equation (1) is not dimensionally/physically meaningful as written.**
The Bessel function J₀ enters the *analytic solution of the WKB envelope* for an oscillating harmonic field in a power-law background; it is not a generic formula for ALP field displacement from recombination to today, and certainly not J₀(m/H₀)/J₀(0) with the prefactor written. No derivation is given. The "≈ f_a θ_i × O(1)" reduction makes the formula vacuous — anything is "O(1)" if you do not commit to a number.

**P2-E5 — Internal inconsistency: f_photon × C₀ = 1.73 ± 0.44 vs. C_aγ × θ_i = 3.4 ± 1.1 vs. Fig. 1 posteriors.**
§3.2 Eq. (5) quotes f_photon × C₀ = 1.73 ± 0.44. §3.3 Eq. (8) quotes C_aγ × θ_i = 3.4 ± 1.1. Figure 1 shows θ_i = 1.33₋₁.₁⁺⁰·⁴⁴ and C_aγ = 13.4₋₁₁⁺⁵·⁶, whose product central value is 1.33 × 13.4 = **17.8**, not 3.4. None of these three numbers (1.73, 3.4, 17.8) are self-consistent. The errors quoted on θ_i (−1.1 from a central value of 1.33) are also nonsensical since the prior lower bound is 0.01. The definition of "f_photon" is never given.

**P2-E6 — MCMC sample sizes are admitted-inadequate yet load-bearing for evidence claims.**
Table 1 reports 720, 2,160, 6,840 accepted samples. §3.3 acknowledges this is modest and that "small effective sample sizes (N_eff ∼ 1,000) limit the precision of tail estimates and evidence calculations." Yet the abstract reports ln B = 5.17 to two decimal places. Savage-Dickey ratios from O(1000) samples are not reliable to that precision. Either rerun with ≥50k samples (as the author himself suggests) or remove the Bayes factor from the abstract.

**P2-E7 — LiteBIRD 9σ claim uses the unsupported 0.27° prediction.**
§4 Eq. (10): "Significance = 0.27/0.03 = 9σ." But (a) the 0.27° prediction is not derived (E3); (b) the author's own combination is 0.242°, giving 8.1σ, not 9σ; (c) the model-independent posterior peaks at 0.342°, giving 11.4σ. The headline "9σ" is a chosen-by-narrative number. Forecast must use the *posterior central value with its uncertainty*, not a hand-picked theoretical estimate.

**P2-E8 — Eq. (2) factor of two / definition mismatch.**
Eq. (2): β = g_aγ Δϕ / 2 = C₀ Δϕ / (2 f_a). The standard ALP-CMB birefringence formula is β = (g_aγ/2)·[ϕ(t₀) − ϕ(t_dec)], so this is right in form. But then "≈ C₀ θ_i / 2 × O(1)" requires Δϕ/f_a ≈ θ_i × O(1), which is consistent with Eq. (1) — and thus inconsistent with the §2.2 substitution Δϕ/f_a ∼ 10⁻². See E3.

---

## MAJOR findings

**P2-M1 — Novelty is overstated and the author admits it.**
§6 explicitly states: "the ALP birefringence model class is well-studied in the literature. Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces β ∼ 0.3°." The abstract and conclusion still frame the result as a fresh "prediction" without that qualification. The contribution as actually scoped — a 2-point Gaussian average plus a small MCMC — is not a PRD-level result.

**P2-M2 — Diego-Palazuelos & Komatsu 2025 citation is an "arXiv preprint" with no identifier.**
References list: "P. Diego-Palazuelos and E. Komatsu. Cosmic birefringence from the Atacama Cosmology Telescope. arXiv preprint, 2025." No arXiv ID, no DOI. The ACT DR6 birefringence number 0.215 ± 0.074° must be traceable; provide the actual reference and quote-match the number.

**P2-M3 — Namikawa, Murai & Naokawa cited "in preparation" but invoked as superior.**
"Namikawa, Murai & Naokawa provide superior ALP mass constraints" — citation says "In preparation; cited for comparison." A paper that does not yet exist cannot be invoked as superior. Either replace with a published reference or drop.

**P2-M4 — Eskilt & Komatsu 2022 quoted value: 0.30 ± 0.11°.**
The actual Eskilt & Komatsu 2022 PRD value for the WMAP+Planck NPIPE combination commonly quoted is β ≈ 0.342° ± 0.094° (the same number the author attributes to "Eskilt et al. joint Planck + ACT" in the abstract!). The 0.30 ± 0.11° appears to be a different subset. The author appears to be using two different Eskilt numbers in two different parts of the paper without disambiguation. Trace and document every input number to its exact table in the cited paper.

**P2-M5 — "f_photon" is undefined.**
Eq. (5) introduces "f_photon × C₀ = 1.73 ± 0.44" with no prior definition of f_photon. Is it θ_i? A coupling-misalignment product? A renormalization? Define on first use.

**P2-M6 — Figure 1 posterior numbers contradict the §3.3 text.**
Fig. 1 shows β [deg] = 0.324 ± 0.099 (Run 2, C free). §3.3 Eq. (6) for Run 1 (C=8 fixed) gives 0.336 ± 0.107°. The text never gives Run 2's β posterior; the reader has to extract it from the figure. The C_aγ marginal (13.4₋₁₁⁺⁵·⁶) shows the prior on C_aγ ∈ [1,30] is dominating, and the asymmetric ±5.6/−11 error bars indicate a poorly-constrained, prior-driven posterior. The "consistent with O(1) values" claim is undermined by the data shown in the figure: the C_aγ marginal peaks well above 1 and extends to the prior boundary.

**P2-M7 — Naturalness argument is circular.**
The claim is "θ_i ∼ O(1), C₀ ∼ O(1), f_a ∼ M_Pl, m ∼ H₀ ⇒ β ≈ 0.27°." But the result depends on the "cosmological integration factor" that is *itself* identified post hoc to land on the observed value. The paper acknowledges this implicitly: "the precise value depends on the cosmological integration through the matter and dark-energy eras" (p.2) and "every input is O(1)" (p.2) and then writes "× O(1)" three times in Eqs. (1) and (2). An unconstrained O(1) factor can swing the prediction over 1–2 orders of magnitude.

**P2-M8 — Bayes factor prior dependence renders the headline number unreliable.**
§3.4: ln B ranges from 4.48 to 5.86 depending on whether the prior is [0°, 0.5°], [0°, 1°], or [0°, 2°]. The abstract quotes only the middle value 5.17 with the modest hedge "(indicative; prior-dependent, see Sec. 3.4)." For a comparison of nonzero rotation vs zero, the natural prior should be motivated physically, not chosen to give a particular ln B. With ALP priors more representative of the literature (e.g., orders of magnitude), ln B will degrade substantially.

**P2-M9 — Calibration-systematics caveat undercuts the headline.**
§6 admits residual "∼ 0.1–0.3°" systematics may exist. The combined statistical error is 0.061°; if a 0.1–0.3° systematic is present, the entire signal could be systematic. This caveat is not propagated into the abstract or the LiteBIRD "9σ" forecast.

**P2-M10 — Equation (1) cosmological-integration factor 1 − J₀(1) ≈ 0.24 is asserted with no derivation.**
J₀(1) ≈ 0.7652, so 1 − J₀(1) ≈ 0.2348. Numerically correct, but the physical content of this formula for ALP field evolution with V = m²f²(1−cos(ϕ/f)) through radiation/matter/Λ transitions is not justified. A proper analysis solves the Klein-Gordon equation in FRW; this is missing.

---

## MINOR findings

**P2-N1 — Companion papers cited without journal information.**
[Golden 2026a, 2026b] cited as "Companion paper, submitted simultaneously." No arXiv IDs, no journal targets, no identifying information. This makes the "matter-bounce fNL = −35/8" claim untraceable.

**P2-N2 — "ECH gravity" is invoked without prior definition (§5, p.4).**
"In the context of ECH gravity" — first appearance, no expansion of acronym (Einstein-Cartan-Holst?), no citation in this paper.

**P2-N3 — Figure 2 axis label issue.**
Figure 2: legend says "Model 0: beta free" but Table 1 calls it "Run 3" and §3.3 labels it "β free." Use consistent run labels.

**P2-N4 — Figure 2: green shaded "observed" band has no width specified in the caption.**
The shaded region appears to span ~0.25–0.44°, presumably ±1σ around 0.342°, but the caption does not say so.

**P2-N5 — "C = 8 fixed" choice is unmotivated.**
Run 1 fixes C = 8. Why 8? The QCD anomaly coefficient is typically O(1). If 8 is the E/N ratio for some grand unified embedding, say so. Otherwise this is arbitrary.

**P2-N6 — Triangle plot caption (Fig. 1) says product is "3.4 ± 1.1," text Eq. (8) says same, but neither matches the visible marginals.**
Compute: 1.33 × 13.4 = 17.8, with large covariance. The quoted 3.4 ± 1.1 must come from a derived parameter or after some selection; explain.

**P2-N7 — Reference list inconsistent capitalization.**
"cmb polarization survey" should be "CMB" (LiteBIRD reference).

**P2-N8 — "ABJ anomaly" used in §2.2 without expanding (Adler-Bell-Jackiw).**

**P2-N9 — Section 5 is one paragraph and adds nothing — the author himself says the result is "independent of bounce cosmology." Cut.**

**P2-N10 — Acknowledgment "use of AI research assistants during the analysis and manuscript preparation" — PRD requires specifics on what was AI-generated, especially for analysis code.**

**P2-N11 — "spectator field" used without definition in this paper (only in passing).**

**P2-N12 — Eq. (3): "independent errors" assumption between Planck NPIPE and ACT DR6 is reasonable but should be stated as an assumption, not implicitly.**

**P2-N13 — The "1σ" consistency claim in Discussion item 2 needs to specify which observed value: the author's own 0.242° or the literature's 0.342°.**

---

## Pagination / scope

The paper is 6 pages including references, with two figures (one of which is a triangle plot from an underpowered MCMC, the other a kernel density plot showing three near-identical Gaussians). The actual scientific content — a 2-measurement Gaussian average and a 6,840-sample MCMC reproducing a literature result — fits in ~2 pages of a PRD Letter at most. The current length is justified only if the central claim (E3) is rigorously derived. As submitted, it is not.

## Recommended max page count if revised
PRL-style 4 pages, OR substantially expand the field-evolution derivation (E3, E4) to PRD article length with a real Boltzmann/Klein-Gordon calculation.

---

## Summary recommendation
**REJECT**

The paper's central technical claim — that fa ∼ MPl, m ∼ H₀, θ_i ∼ O(1) naturally produce β ≈ 0.27° — is not derived; the load-bearing cosmological integration factor disagrees with the paper's own Eq. (1) by a factor of ~25 (E3). The abstract attributes a literature value (0.342 ± 0.094°) to "Eskilt et al. joint Planck + ACT" while the body's actual combined constraint is 0.242 ± 0.061° — these are different numbers conflated throughout (E1). Three different effective coupling-misalignment products are quoted in three places (1.73, 3.4, 17.8) with none consistent (E5). The MCMC is admitted-underpowered (E6) yet a Bayes factor is quoted to two decimals. The novelty is explicitly admitted to overlap with Fujita et al. 2021 (M1). The headline "9σ LiteBIRD test" is computed from an undefended 0.27° prediction (E7). The Diego-Palazuelos and Namikawa citations are an arXiv-IDless preprint and an in-preparation paper (M2, M3). This is well below the PRD bar; a substantial rewrite anchored in a real Klein-Gordon solution and self-consistent numbers would be required before resubmission anywhere.

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional Referee Findings — Second-Pass Review

The initial review caught the major numerical inconsistencies but missed several deeper structural problems. The new findings below are independent of those already flagged.

---

## NEW ESSENTIAL findings

**P2-E9 — MCMC posterior on m contradicts the abstract's headline "m ∼ H₀" claim (Fig. 1 vs Abstract).**
Figure 1 shows log₁₀(m_a/eV) = −31.4₋₁.₂⁺¹·⁴. Convert to H₀ units: H₀ ≈ 67 km/s/Mpc → ℏH₀ ≈ 1.44 × 10⁻³³ eV → log₁₀(H₀/eV) ≈ **−32.84**. So the posterior central value is m ≈ 10^(−31.4) eV ≈ 10^1.44 × H₀ ≈ **28 H₀**, not m ∼ H₀. The abstract, §2.1, and §7 (Conclusion) all repeatedly assert m ∼ H₀ is the natural and inferred value. At m ≈ 30 H₀, the field would have started rolling at z ~ 30, not z ~ 1 as §2.1 explicitly states, and would have undergone many oscillations between recombination and today — invalidating Eq. (1)'s slow-roll/single-displacement formula entirely. The posterior also sits within 1σ of the prior upper edge (log₁₀ m_a/eV = −30), so the constraint is partly prior-driven. This is a substantive contradiction between the headline naturalness claim and the actual inference.

**P2-E10 — MCMC posterior on C_aγ contradicts the abstract's "order-unity" claim.**
Figure 1: C_aγ = 13.4₋₁₁⁺⁵·⁶. The asymmetric −11/+5.6 error with prior lower bound at 1 indicates the data strongly prefer C_aγ ≳ 5; the maximum-likelihood value is ~13, an order of magnitude above the "order-unity" claim repeated in the abstract, §2.2, §3.3, and §7. The data are telling the author that C_aγ ~ 10–15 is preferred, which is *the opposite* of the naturalness claim that motivates the whole paper. Also: the choice C = 8 (fixed) in Run 1 is now seen to be a deliberate compromise between the "natural" value 1 and the data-preferred value 13.4 — entirely unmotivated *a priori*.

**P2-E11 — Misattribution: Eskilt & Komatsu 2022 is WMAP+Planck, not "joint Planck + ACT."**
Abstract: "β_obs = 0.342 ± 0.094° from the Eskilt et al. joint Planck + ACT analysis." Bibliography entry for Eskilt & Komatsu 2022 is titled "Improved constraints on cosmic birefringence from the **WMAP and Planck** cosmic microwave background polarization data." There is no Planck+ACT joint analysis in Eskilt & Komatsu 2022. The author is misattributing the dataset and likely the central value. The 0.342 ± 0.094° is the WMAP+Planck NPIPE value, not Planck+ACT. Trace and fix every appearance.

**P2-E12 — Summary-likelihood uncertainty (0.061°) is implausibly smaller than the proper joint-analysis uncertainty (0.094°).**
The author's naive inverse-variance combination of Planck NPIPE (σ=0.11°) and ACT DR6 (σ=0.074°) gives σ_combined = 0.061°. But the actual literature "joint Eskilt-style" analysis with proper EB-spectrum handling, foreground covariances, and shared calibration systematics gives σ = 0.094° — **50% larger**. This means the author's "independent errors" assumption (Eq. 3) is wrong and is inflating the significance. With the proper σ ≈ 0.094°, the combined significance is 0.242/0.094 = **2.6σ**, not the headline 3.9σ. The abstract's "3.9σ" is a methodological artifact of pretending the two measurements are uncorrelated. (Planck and ACT share sample variance for overlapping sky regions, share polarized dust foreground models, and share calibration assumptions.)

**P2-E13 — LiteBIRD "decisive exclusion" claim is wrong: the ALP model has free parameters.**
Abstract: "either confirming the signal or **ruling out the ALP explanation decisively**." But the ALP model has C_aγ × θ_i as a free product. A LiteBIRD null result β = 0 ± 0.03° would not rule out the ALP model; it would constrain C_aγ × θ_i to be small. Since the posterior already extends to C_aγ ~ 25 (Fig. 1), the model can accommodate β = 0 by letting C_aγ θ_i → 0 (a region the current prior excludes only because the lower bound on C_aγ is 1). The claim of "decisive exclusion" only holds if you fix the parameters to the maximum-likelihood values from current data, which is not how model exclusion works.

---

## NEW MAJOR findings

**P2-M11 — Intro "Combined, the evidence exceeds 3.5σ" lacks a citation and the combination is ambiguous.**
§1 p.1: "The Planck HFI analysis reported β = 0.35±0.14° (2.5σ), and the ACT DR6 analysis confirmed the signal at comparable significance. Combined, the evidence exceeds 3.5σ." No citation for the "combined" number; no specification of which analysis combined them. If naively combining 2.5σ and 2.5σ in quadrature, you get √(2×2.5²) = 3.54σ — but only if you assume the *measurements are independent and unbiased*. This is the same wrong assumption that produces E12.

**P2-M12 — The "Planck NPIPE" value 0.30 ± 0.11° in §3.1 is attributed to Eskilt & Komatsu 2022, but that paper combines WMAP+Planck.**
The Planck-only NPIPE value 0.30 ± 0.11° appears in Diego-Palazuelos et al. 2022, not Eskilt & Komatsu 2022. The author is citing the wrong paper for the wrong number. Either swap the citation or swap the number.

**P2-M13 — Run 1 sample size (2,160) is too small for the quoted ±0.107° error on β.**
Eq. (6) quotes β_ALP = 0.336 ± 0.107° from Run 1 (C = 8 fixed, 2,160 samples). With N_eff ≪ 2,160 (likely ~500–1,000 after burn-in and autocorrelation), the standard error on the posterior mean is dominated by Monte Carlo noise. With ~1,000 effective samples and σ_post ≈ 0.1°, the MC error on the central value is ~0.003°, which is acceptable but tight. More concerning: ±0.107° on β when the data input is 0.342 ± 0.094° suggests the prior on θ_i is *adding* noise — i.e., the model is degrading the constraint. A model that worsens the inferred error compared to a direct measurement is not adding information.

**P2-M14 — θ_i posterior in Fig. 1 (1.33₋₁.₁⁺⁰·⁴⁴) is essentially the prior.**
The flat prior θ_i ∈ [0.01, π] has mean π/2 ≈ 1.57 and σ ≈ π/√12 ≈ 0.91. Posterior central 1.33 ± ~0.8 (asymmetric) is statistically consistent with the prior. The data do not constrain θ_i — they only constrain the product C_aγ θ_i. Fig. 1's tight-looking diagonal panel for θ_i is misleading; the constraint is from prior + the C_aγ × θ_i degeneracy, not from the data alone.

**P2-M15 — Eq. (1) is invalid in the regime preferred by the MCMC.**
The formula Δϕ ≈ f_a θ_i (1 − J₀(m/H₀)/J₀(0)) is only meaningful for m/H₀ ≲ 1 (slow-roll to first-oscillation). For m/H₀ ~ 30 (the MCMC posterior, see E9), the field has oscillated many times since z ~ 30 and the appropriate quantity is the time-averaged field expectation value with damped envelope ⟨ϕ⟩ ∝ a^(−3/2), giving Δϕ ≈ 0 to leading order (no net rotation). The formula used in the paper does not apply to the regime the MCMC actually prefers. This is a fundamental inconsistency between the analytic model (§2) and the numerical results (§3).

**P2-M16 — The "f_photon × C₀ = 1.73 ± 0.44" value (Eq. 5) numerically equals 7.15 × β_combined.**
1.73 ± 0.44 has σ/μ = 0.254, same as 0.061/0.242 = 0.252. And 1.73/0.242 = 7.15. So Eq. (5) is just a rescaled β. The undefined "f_photon" parameter is acting as a renaming, not a physically meaningful normalization. Without a definition, this equation conveys no new information.

**P2-M17 — §1 reports Minami & Komatsu 2020 as "2.5σ," but the original paper claims 2.4σ (99.2% C.L.).**
Minor but: 0.35/0.14 = 2.50σ as one-sided, but the original M&K result was 99.2% C.L. ≈ 2.40σ two-sided. The author is using one-sided convention without saying so, while the literature uses two-sided. Be explicit.

---

## NEW MINOR findings

**P2-N14 — Fig. 1 caption says "the coupling-misalignment product C_aγ × θ_i is centered at 3.4 ± 1.1." This is the claim in §3.3 Eq. (8) but is inconsistent with the visible marginals (1.33 × 13.4 = 17.8). The discrepancy is not explained.**

**P2-N15 — Diagonal panels in Fig. 1 show one-dimensional marginals; off-diagonal panels show 2D contours. But the C_aγ vs θ_i contour shows a strong anti-correlation banana, indicating these two parameters are degenerate at the ~5σ level. The "product" 3.4 ± 1.1 (if computed as a derived parameter along the degeneracy direction) is the only constrained combination. Yet the abstract treats C₀ and θ_i as separately "natural" — they are not separately constrained.**

**P2-N16 — Fig. 2 caption: "All three are consistent with each other and with the observed value β_obs = 0.342 ± 0.094°." The model-independent (black dashed) curve in Fig. 2 should peak at 0.342° by construction, but visually peaks closer to 0.35°. Hard to tell from the figure resolution; verify.**

**P2-N17 — Run 1 (C = 8 fixed) gives β_ALP = 0.336 ± 0.107°. Run 2 (C free) gives β = 0.324 ± 0.099° (read from Fig. 1). These differ by 0.012° — within MC error, but the *fixed* version has a larger error than the *free* version. This is backwards: adding a parameter (Run 2) should not decrease the error on β unless there is a constraint pulling β tighter, which requires explanation.**

**P2-N18 — §1 "joint Planck + ACT" appears in the abstract, but the body never performs a joint Planck+ACT analysis. The only "joint" analysis is the author's homemade Gaussian average. This is misleading framing.**

**P2-N19 — §6 invokes "f_NL = −35/8" from a companion paper for a complementary test. −35/8 ≈ −4.375. The matter-bounce f_NL prediction is a well-known specific number; this should be cited to its original derivation in the literature (e.g., Cai et al. 2009), not exclusively to the author's own companion paper.**

**P2-N20 — Acknowledgment of "AI research assistants" provides no specifics. PRD policy and ApJ/Nature norms increasingly require disclosure of *what* AI did: literature search? Code generation? Manuscript drafting? Symbolic computation? The current single sentence is non-disclosure.**

**P2-N21 — The Eq. (2) factor of 1/2 (β = g_aγ Δϕ / 2) requires the integration ∫_(t_dec)^(t₀) dt ∂_t ϕ to be Δϕ = ϕ(t₀) − ϕ(t_dec), with the photon experiencing the rotation rate (g_aγ/2)∂_t ϕ integrated along the line of sight. This is fine, but the factor depends on the convention for g_aγ in L = −(g_aγ/4)ϕ F F̃. State the convention.**

**P2-N22 — §4 LiteBIRD forecast: "σ(β) ≈ 0.03°" is cited to LiteBIRD Collaboration 2023, but the actual forecast precision depends strongly on r, foreground residuals, and HWP systematics. The 0.03° number is the best-case, statistics-only floor. Use a range (0.03°–0.1°) for realism.**

---

## SUMMARY of second-pass additions

The most damaging new finding is **P2-E9** (MCMC posterior prefers m ≈ 30 H₀, contradicting the abstract's m ∼ H₀ headline) coupled with **P2-E10** (posterior C_aγ ≈ 13, contradicting "order-unity" claim) and **P2-M15** (Eq. (1) breaks down in the regime preferred by the data). Together these show that the author's naturalness argument is contradicted by his own MCMC: the data prefer parameters that are neither natural nor consistent with the analytic framework used to motivate the prediction.

**P2-E11** (misattribution of Eskilt & Komatsu 2022 as "Planck+ACT") and **P2-E12** (naive error combination underestimates uncertainty by 50%, inflating 2.6σ → 3.9σ) further undermine the headline statistical claims.

**P2-E13** (LiteBIRD null cannot "decisively exclude" the model because C_aγ θ_i is free) shows the paper's central forecast framing is logically incorrect.

The recommendation remains **REJECT**, with the additional observation that the data the author himself presents (Fig. 1) actively *contradict* the naturalness claim that motivates the paper. The MCMC posterior is the strongest argument against the paper's thesis, and the author has not addressed it.