# P2 auto-2026-06-05_1517pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (16246 chars)
**Wall time**: 56.3s

---

I cannot complete the requested forensic audit to PRD referee standard from the material provided, because I do **not** have the full rendered PDF or the ability in this chat to inspect the paper’s figures/tables page-by-page and to query arXiv/NASA ADS in real time. The only reliable way to do what you asked is to verify the paper text against live bibliographic records and the actual PDF, and those inputs are incomplete here.

What I *can* do from the supplied text is identify several **high-confidence citation and internal-consistency problems** that would already block acceptance unless fixed:

- **ESSENTIAL — Reference 4 / body text mismatch**: the paper cites “ACT DR6 [Diego-Palazuelos and Komatsu, 2025]” and the bibliography lists only “P. Diego-Palazuelos and E. Komatsu. Cosmic birefringence from the Atacama Cosmology Telescope. arXiv preprint, 2025.” The title, author list, and arXiv identifier are incomplete. This is not PRD-ready because the reader cannot verify the source or reproduce the reported \( \beta=0.215\pm0.074^\circ \) result from the citation as written.

- **ESSENTIAL — “in preparation” citation used as a substantive source**: “Toshiya Namikawa, Kai Murai, and Sho Naokawa. Constraints on axion-like particles from cosmic birefringence. arXiv e-prints, 2025. In preparation; cited for comparison of ALP mass constraints.” A paper cannot cite a non-existent “arXiv e-prints” item as though it were a verifiable source, especially for a quantitative comparison claim.

- **MAJOR — Unsupported/unclear provenance for the quoted combined significance**: the abstract states “the 3.6σ isotropic birefringence signal (βobs = 0.342±0.094° from the Eskilt et al. joint Planck + ACT analysis).” The body says the same value is used, but no derivation is shown tying \(0.342/0.094\approx3.64\) to a Gaussian significance, and no explicit source in the bibliography matches a “joint Planck + ACT analysis” with that exact result. The citation trail is incomplete as written.

- **MAJOR — Likelihood combination and significance are only partially traceable**: Eq. (4) gives \( \beta_{\rm combined}=0.242\pm0.061^\circ\), and the abstract reports \(3.9\sigma\) from zero. That is numerically consistent with \(0.242/0.061\approx3.97\), but the paper never states the exact formula used for the significance or whether the quoted uncertainty is symmetric Gaussian posterior width or an error propagation from the weighted mean. This needs explicit derivation and assumptions.

- **MAJOR — Bayes factor claims lack reproducibility**: the paper reports “\( \ln B=5.17\)” and gives prior-dependence values, but the text does not provide the explicit prior normalization, evidence computation details, or likelihood definition sufficient for an independent check. For PRD, this must be fully reproducible.

- **MAJOR — Potential dimensional slippage in Eq. (2)**: the equation writes \( \beta = \frac{g_{a\gamma}}{2}\Delta\phi = \frac{C_0}{2f_a}\Delta\phi \approx \frac{C_0\theta_i}{2}\times O(1)\). The later sentence says “\(\Delta\phi/f_a \sim 10^{-2}\) … yielding \(\beta \approx C_0\theta_i\times 5\times10^{-3}\,\mathrm{rad}\approx0.27^\circ\).” This is internally plausible only if the hidden \(O(1)\) factor is actually \(\sim 2\times10^{-2}\), but the paper never shows the calculation. As written, the scaling argument is too hand-wavy for a load-bearing claim.

- **MAJOR — Figure audit impossible from text alone**: Figure 1 and Figure 2 are described, but no actual images, axes, or numerical contours are available in the provided material. I cannot verify whether axis labels, units, or contour values are correct. This must be checked against the PDF.

- **MAJOR — Overclaim in the abstract**: “either confirming the signal or ruling out the ALP explanation decisively.” A 9σ forecast on *a specific model parameter point* is not the same as a model-independent exclusion of the entire ALP explanation. This wording overstates the falsifiability claim.

- **MAJOR — “Independent of bounce cosmology” is asserted but not demonstrated**: the paper claims the birefringence prediction is independent of bounce cosmology and then later says it can be motivated within ECH. Because the main text references a “companion paper” for the ECH framework, the current paper should explicitly separate what is proven here from what depends on external unpublished work.

- **MAJOR — Citation to companion papers is not acceptable as support for core claims**: “Golden, 2026a/b” are simultaneously submitted companion papers. Core physics claims in this paper should not depend on them unless the necessary material is reproduced here.

- **MINOR — Notation inconsistency**: the paper alternates between \(f_a\), \(g_{a\gamma}\), \(C_0\), and \(C_{a\gamma}\) without a clean mapping. For example, Table 1 says “ALP (C = 8 fixed)” while the body discusses \(C_0\) and later \(C_{a\gamma}\). This should be standardized.

- **MINOR — Table 1 lacks full statistical context**: “Samples” and “\( \hat R -1\)” are listed, but there is no statement of chain count, thinning, burn-in, proposal distribution, or effective sample size definition beyond a casual mention later. For a methods paper, this is incomplete.

- **MINOR — Ambiguous use of “3.6σ” vs “3.5σ” vs “3.9σ”**: the abstract says the observational signal is 3.6σ, the introduction says “Combined, the evidence exceeds 3.5σ,” and Eq. (4) gives a 3.9σ combined constraint from zero. These are not directly contradictory, but the paper must state clearly which significance refers to which dataset and hypothesis.

- **MINOR — The bibliography entry for the ACT result is incomplete**: “arXiv preprint, 2025” is not acceptable PRD bibliography style without identifier, title capitalization, and archive number.

- **MINOR — The LiteBIRD forecast is under-justified**: the paper quotes \( \sigma(\beta)\approx0.03^\circ\) from a collaboration forecast, but no specific forecast configuration is identified. Since the significance claim is central, the exact forecast assumptions need to be stated.

- **MINOR — Internal bookkeeping language should not be in the body if it appeared there**: the manuscript uses “Run 1/2/3” and “companion paper” appropriately, but if any “R-round” or draft-history tags exist in the actual PDF they must be removed. I cannot confirm them from the text provided.

Because I cannot inspect the actual PDF and because the bibliography is visibly incomplete/non-verifiable in the supplied text, I would not recommend acceptance on this version.

## Summary recommendation
**MAJOR REVISIONS**

The paper has a potentially interesting physics claim, but the citation apparatus is not PRD-grade as submitted: at least one reference is incomplete, one is effectively unverifiable (“in preparation”), several quantitative claims lack a fully reproducible derivation, and the forecast/falsifiability language is overstated. Before acceptance, the authors must provide a complete, verifiable bibliography with arXiv IDs/DOIs, fully reproduce all quoted statistics from cited sources and their own calculations, and supply the actual PDF-level figure/table evidence for a full forensic check.

---

## PASS 2 — self-critique findings (what initial review missed)

[P2-E1: ARITHMETIC / NUMERICS]

1. **Inconsistent “3.6σ” vs quoted error bar in abstract.**  
   - Abstract: “βobs = 0.342±0.094◦ from the Eskilt et al. joint Planck + ACT analysis” and “the 3.6σ isotropic birefringence signal.”  
   - 0.342/0.094 ≈ 3.64σ, which is fine, but **Eskilt & Komatsu (2022)** is a WMAP+Planck analysis, not “joint Planck + ACT.” The ACT piece is Diego‑Palazuelos & Komatsu (2025). The numerical 3.6σ is therefore being attached to a mis‑identified dataset (a dataset mix that does not exist as cited). This is distinct from the earlier issue about incomplete citation formatting: here the *combination label* (Planck+ACT) is wrong.

2. **Weighted‑mean combination in Eq. (4) does not match input numbers.**  
   - Inputs (Sec. 3.1):  
     • Planck NPIPE: β₁ = 0.30 ± 0.11°  
     • ACT DR6: β₂ = 0.215 ± 0.074°  
   - Inverse‑variance weighted mean:  
     w₁ = 1/0.11² ≈ 82.6, w₂ = 1/0.074² ≈ 182.7,  
     β̄ = (w₁β₁ + w₂β₂)/(w₁+w₂) ≈ (24.8 + 39.3)/265.3 ≈ 0.242° (agrees with Eq. 4).  
     σ̄ = (w₁+w₂)⁻¹/² ≈ 1/√265.3 ≈ 0.0613°, consistent with 0.061°.  
   - **New issue:** The “2.7σ” and “2.9σ” significances stated for the individual inputs do not match the quoted means and errors:  
     • Planck NPIPE: 0.30/0.11 ≈ 2.73σ (ok for “2.7σ”),  
     • ACT DR6: 0.215/0.074 ≈ 2.90σ (ok for “2.9σ”).  
     But then in the Introduction, the earlier HFI result is quoted as 0.35±0.14° (2.5σ), which is 0.35/0.14 ≈ 2.5σ, and “Combined, the evidence exceeds 3.5σ.” That “combined” σ is not defined (it mixes a superseded Planck HFI value with ACT DR6 that has not yet been introduced; later the formal combination is done with *different* Planck data and gives 3.9σ). The paper thus presents **two different “combined” significances (~3.5σ and 3.9σ) with no explicit mapping between which datasets are in each combination**. This is an arithmetic/accounting issue, not just language.

3. **“Consistent at 1σ” claim is numerically off.**  
   - Discussion: “The prediction matches the combined Planck + ACT measurement at 1σ.”  
   - Prediction: β ≈ 0.27°.  
   - Combined constraint (Eq. 4): βcombined = 0.242 ± 0.061°.  
   - Difference: |0.27 − 0.242| = 0.028°. In σ units: 0.028/0.061 ≈ 0.46σ.  
   - This is *well within* 1σ, but the claim “matches … at 1σ” is imprecise: it usually means “within 1σ” of the best fit, but in context it reads as if the prediction equals the 1σ band boundary. Not a fatal error, but the wording is sloppy given the explicit numbers.

4. **“9σ” exclusion claim lacks correct mapping to parameter space.**  
   - Eq. (10): 0.27/0.03 = 9, so the arithmetic is fine.  
   - However the text: “If LiteBIRD measures β = 0 ± 0.03◦ , the ALP explanation is excluded at 9σ.” This treats the *same* σ (forecast statistical error on β) as the null width and as the model‑prediction uncertainty, i.e., implicitly assumes a delta‑function theoretical prediction at 0.27°. In reality, the model has intrinsic spread in β (from θᵢ, C₀, etc.), so the 9σ number is not literally a null‑hypothesis significance; it’s a signal‑to‑noise ratio constructed from a single parameter point. This is a **procedural comparability problem** between σ from data and unquantified σ from theory (ties into E‑class below).

5. **“Neff ∼ 1,000” vs Table 1 sample counts.**  
   - Table 1: Run 1 has 2,160 samples, Run 2 has 6,840, Run 3 has 720.  
   - Text: “the small effective sample sizes (Neff ∼ 1,000) limit the precision…” with no run‑by‑run breakdown. For Run 3, an Neff near 1,000 is impossible given only 720 accepted samples. Unless Neff is defined per‑parameter and per‑run in some nonstandard way, this is **numerically inconsistent** for at least Run 3. The paper needs to clarify that Neff ∼ 1,000 refers only to the larger chains, or give actual Neff values.

6. **C×θi posterior vs “order unity” claim.**  
   - Eq. (8): Caγ × θi = 3.4 ± 1.1, described as “consistent with O(1) values for both parameters individually.”  
   - If both Caγ and θi are each O(1) in the usual sense (∼0.3–3), a product ∼3.4±1.1 pushes Caγ towards the upper half of the 1–30 prior if θi is not near its maximum π. Not a strict arithmetic error, but the “order unity” rhetoric is being used rather loosely (same class of overstatement as the 9σ “decisive” language).

[P2-E2: FIGURE CAPTION VS BODY]

7. **Figure 2 consistency claim not numerically supported.**  
   - Caption: “Comparison of β posteriors across all three model configurations… All three are consistent with each other and with the observed value βobs = 0.342 ± 0.094◦.”  
   - Body:  
     • βALP = 0.336 ± 0.107° (Run 1)  
     • βfree = 0.344 ± 0.096° (Run 3)  
     • βobs = 0.342 ± 0.094°.  
   - Numerically these are extremely close, so “consistent” is fine. The **new issue** is that the caption and text both talk about “all three model configurations” but never display or specify the β posterior for Run 2 explicitly in the body (only Caγ×θi). The caption implies a β distribution for Run 2 is plotted and compared, but the main text never shows or quantifies β from Run 2. This is a figure/body mismatch: a quantity used in a figure for comparison is not actually documented in the text.

[P2-E3: DIMENSIONAL CONSISTENCY / EQUATIONS]

8. **Dimensional ambiguity in Eq. (1) via Bessel function ratio.**  
   - Eq. (1): Δϕ ≈ fa θi (1 − J₀(m/H₀))/J₀(0).  
   - J₀ argument is m/H₀, which is dimensionless (ok), J₀(0)=1, so Δϕ has units of fa.  
   - Then text: “For m/H0 ∼ 1, 1 − J0 (1) ≈ 0.24; the precise value depends on the cosmological integration…” That *0.24* is treated as a fixed O(1) factor, but in reality the coefficient controlling Δϕ/fa comes from an integral over the expansion history, not just 1−J₀(1). The dimensional consistency is fine, but the **normalization is not explicit**: the transition from a rough Bessel approximation to Δϕ/fa ∼ 10⁻² in Sec. 2.2 skips the actual computation that would connect the two. This strengthens the earlier criticism but now specifically identifies Eq. (1) as the missing quantitative bridge.

9. **Eq. (2) hides a unit conversion that is never shown.**  
   - Eq. (2): β = (gaγ/2) Δϕ = (C₀/2fa) Δϕ ≈ (C₀ θi /2) × O(1).  
   - β is an angle (dimensionless in natural units). If Δϕ/fa ∼ 10⁻² is invoked, then β ≈ (C₀ θi/2)×10⁻². But the text later jumps to “β ≈ C0 θi × 5 × 10−3 rad ≈ 0.27◦” without showing how the factor “5×10⁻³” is obtained from Δϕ/fa ∼ 10⁻² and the Bessel/integration factors. This is not strictly a *dimensional* error, but **the equation as written does not explicitly contain the key dimensionless ratio Δϕ/fa**, and the normalization that matters for β is pushed into an opaque “O(1)” that is later replaced with a very specific 5×10⁻³. PRD would expect the intermediate step to be explicit.

10. **Eq. (3) notation: missing product index in exponent and inconsistent σᵢ symbols.**  
    - Eq. (3): \(L(β) = \prod_i (1/\sqrt{2πσ_i^2}) \exp[-(β^{obs} − β)^2/(2σ_i^2)]\).  
    - As typed: “(β obs − β)2 /2σ i 2 ” has mismatched spacing; strictly, it should read (βobs,i − β)²/(2σᵢ²), with the index “i” on βobs as well. The lack of an index on βobs makes it ambiguous whether multiple measurements are used; the surrounding text implies a product over i, but the equation as written is not internally consistent in its notation.

11. **Eq. (10) omits uncertainty in the prediction itself.**  
    - Eq. (10) uses β = 0.27° as a single value, not as β±σ_theory. Dimensional consistency is fine, but this is another case where the statistical normalization (what σ actually means in this equation) is not explicit. This belongs under “normalizations explicit” rather than raw units.

[P2-E4: INTERNAL CROSS‑REFERENCES]

12. **Misleading “Sec. 3.4” pointer in abstract.**  
    - Abstract: “The Bayes factor in favor of nonzero rotation is ln B = 5.17 (indicative; prior-dependent, see Sec. 3.4).”  
    - Sec. 3.4 indeed discusses the Bayes factor, but labels lnB as “indicative evidence” while still quoting it as a central result. There is no real cross‑check or robustness test there; the section is more of a short footnote. The pointer is technically correct, but for PRD‑level reproducibility it over‑promises what Sec. 3.4 actually contains: there is no explicit likelihood definition in β space, no numerical evidence integration, only a one‑line mention of Savage–Dickey. This is a **content–pointer mismatch** in terms of level of detail promised vs delivered.

13. **“See Eq. (3)” vs use of βobs.**  
    - Sec. 3.1: “These produce the combined constraint in Eq. 4. For the MCMC parameter estimation (Sec. 3.3), we use the Eskilt et al. joint analysis value βobs = 0.342 ± 0.094◦, which differs because it fits the full EB cross-spectrum rather than combining point estimates.”  
    - Eq. (3) is a summary likelihood over multiple βobs,i. For the MCMC in Sec. 3.3, the likelihood is actually **just a single Gaussian in βobs**, not the product assumed in Eq. (3). The paper never states this explicitly nor gives a separate equation for the MCMC likelihood; instead, Eq. (3) stands as the only likelihood formula. This creates a **procedural mismatch** between the likelihood used for the combination (Eq. 4) and that used for the MCMC, even though only one likelihood equation is given.

[P2-E5: NULL PROCEDURE COMPARABILITY]

14. **Juxtaposition of multiple σ values from different pipelines without warning.**  
    - The text places in close succession:  
      • Planck HFI: 2.5σ (Minami & Komatsu, 2020),  
      • Planck NPIPE: 2.7σ (Eskilt & Komatsu, 2022),  
      • ACT DR6: 2.9σ,  
      • Eskilt joint analysis: 3.6σ (Planck+ACT mis‑labelled),  
      • Combined summary‑likelihood: 3.9σ.  
    - These σ values arise from *different likelihoods, data splits, and calibration models* (self‑calibration vs EB‑spectrum fits vs summary Gaussian). The paper never states that these significances **are not directly comparable** and instead uses rhetorical phrases like “Combined, the evidence exceeds 3.5σ” and “3.9σ from zero” as if they were commensurate. This is a textbook E‑class issue: σ’s from different null procedures are presented side‑by‑side without appropriate caveats.

15. **Bayes factor vs σ significance conflation.**  
    - lnB ≈ 5 is given, and separately a 3.9σ significance from zero. There is no check or mapping (e.g., via Jeffreys scale or an approximate σ–lnB relationship) to show whether these are consistent diagnostics of evidence strength. Presenting both without context encourages readers to take them as interchangeable measures of “strength of evidence,” although they originate from different null procedures and priors.

[P2-E6: ABSTRACT FAITHFULNESS]

16. **“Natural” prediction claim in abstract not backed by a real calculation.**  
    - Abstract: “For order-unity inputs, this minimal setup naturally accommodates a birefringence rotation angle β ≈ 0.27◦…”  
    - In the body, the only concrete numerical bridge is the heuristic statement in Sec. 2.2 that Δϕ/fa ∼ 10⁻² “from the ratio of field displacement to decay constant over the Hubble time.” No actual cosmological solution is shown, no integral for Δϕ(z), and the Bessel‑function approximation in Eq. (1) is not quantitatively evaluated beyond “O(1)”. The paper thus lacks a **fully explicit derivation** of the 0.27° number from the stated parameter ranges; the word “naturally” in the abstract overstates how tightly the body constrains the result.

17. **“Independent of bounce cosmology” claim only partially justified.**  
    - Abstract: “This birefringence prediction is independent of bounce cosmology…”  
    - Sec. 5 reiterates this but gives no explicit demonstration that pre‑recombination initial conditions for ϕ (e.g., θi distribution) are independent of bounce physics, or that any bounce‑induced features in the background expansion do not affect the Δϕ integral between recombination and today. The argument is qualitative (“spectator field”) but not proven. The body therefore does *not fully support* the abstract’s strong phrasing of “independent.”

18. **“Either confirming the signal or ruling out the ALP explanation decisively” overstates exclusion.**  
    - Abstract: “LiteBIRD… will test this prediction at 9σ significance—either confirming the signal or ruling out the ALP explanation decisively.”  
    - Body (Sec. 4, 6) reiterates 9σ but does not quantify the width of the predicted β distribution. Because the model has tunable O(1) parameters (C₀, θi), a null β ≈ 0 measurement could still be accommodated by atypically small θi or specific model choices; the paper never defines what part of parameter space would be excluded. Thus the abstract’s “ruling out the ALP explanation decisively” is stronger than what the body actually demonstrates.

[P2-E7: UNSUPPORTED NOVELTY CLAIMS]

19. **“Our contribution is… the specific parameter identification … and the inference framework demonstrating internal consistency” is not benchmarked against prior work.**  
    - Sec. 6: after acknowledging Fujita et al. (2021) and Namikawa et al. (2025) as prior literature, the author claims novelty in a “specific parameter identification (fa ∼ MPl, m ∼ H0)” and an “inference framework demonstrating internal consistency.” There is no explicit comparison of this inference framework to that of Fujita et al. or Namikawa et al. (e.g., whether they also explore Planck‑scale fa or similar mass ranges). The novelty statement is thus **not quantitatively substantiated**.

[P2-E8: UNQUANTIFIED HEDGES]

20. **“No tension” claim is unquantified.**  
    - Sec. 3.3: “…βALP = 0.336 ± 0.107°, βfree = 0.344 ± 0.096°, and βobs = 0.342 ± 0.094°. The ALP model reproduces the observed birefringence with no tension.”  
    - The differences are small, but “no tension” could be quantified, e.g. by Δβ/σ_combined. The text does not provide any such calculation; this is a classic case of a qualitative hedge without numbers. Not a fatal flaw, but it fits class H you asked to check.

21. **“Broadly compatible” calibration/systematics discussion lacks specific bounds.**  
    - Sec. 6 speaks of “∼0.1–0.3° systematics” and “residual systematics could arise…” but never compares these potential systematics quantitatively against the 0.27° signal prediction, nor does it explain whether a 0.3° systematic would completely mimic the signal. The language suggests “debated but probably okay”, yet the numbers would allow systematics comparable to or larger than the claimed effect.

[P2-E9: APPENDIX VS MAIN TEXT]

22. **(No appendix present.)**  
    - There are no appendices in the provided text, so I cannot check appendix vs main‑text mismatches. This is why the original review did not flag any A‑class issues here.

[P2-E10: STALE / INCONSISTENT NUMBERS]

23. **“3.6σ signal” vs “Combined, the evidence exceeds 3.5σ” vs 3.9σ combined.**  
    - Introduction: “Combined, the evidence exceeds 3.5σ.”  
    - Abstract & Conclusion: “3.6σ isotropic birefringence signal” from Eskilt et al. joint analysis.  
    - Sec. 3.2: combined constraint is 3.9σ.  
    - These three “headline” significances are all presented as current state‑of‑the‑art, but they correspond to **different and partially incompatible dataset combinations** (old HFI+ACT, “joint analysis” with mislabelled dataset, and summary‑likelihood combination of Planck NPIPE+ACT). The likely explanation is that numbers have been updated at different drafting stages and not fully harmonized. This is more than cosmetic: it confuses the reader about which result is the one the model is supposed to match.

24. **βobs used inconsistently as “Eskilt et al. joint Planck + ACT” vs WMAP+Planck.**  
    - βobs = 0.342 ± 0.094° is attributed to an “Eskilt et al. joint Planck + ACT analysis” in the abstract and used as “observed value” throughout, but the only Eskilt & Komatsu paper in the references is a WMAP+Planck analysis. The “joint Planck + ACT” phrase appears to be a leftover from an earlier or aspirational version and is not supported by the current reference list.

If you want, I can next rewrite the report section with these new findings merged cleanly into your existing [P2‑E#, M#, m#, N#] structure, so you can drop it directly into a PRD referee form.