# P2 auto-2026-06-08_1144pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (15420 chars)
**Wall time**: 151.8s

---

The manuscript as written does not meet Physical Review D standards for accuracy, citation reliability, or methodological transparency. Multiple key references are mis-specified or future‑dated, several quantitative claims are internally inconsistent, and some “in preparation” citations are not credible. Below is a detailed, itemized audit.

---

### P2‑E1 – Abstract, p.1 – Misquoted significance of Eskilt et al. result

**Offending text**

> “…consistent with the 3.6σ isotropic birefringence signal (βobs = 0.342±0.094◦ from the Eskilt et al. joint Planck + ACT analysis).”

**Problem**

The significance implied by the quoted mean and error is \(0.342/0.094 ≈ 3.64σ\), but this number is not shown to be taken from the cited paper and is not explicitly labeled as their value vs. the author’s recomputation. Eskilt & Komatsu (2022) report their constraints in different combinations; the manuscript does not specify which exact combination produces 0.342±0.094°. The “3.6σ” claim must be traceable to a specific table/fit in the reference and identified as such.

**Required fix (ESSENTIAL)**

- Explicitly state which exact result from Eskilt & Komatsu (2022) the quoted 0.342±0.094° corresponds to (full WMAP+Planck combination, specific EB spectrum configuration, etc.).
- Confirm that “3.6σ” is either (a) explicitly quoted in that paper or (b) your own derived ratio 0.342/0.094; in the latter case, make this clear and not present it as a quoted significance from the reference.
- If Eskilt & Komatsu (2022) do not report that exact mean and error, correct the numbers to match an actual reported value, with the correct σ.

---

### P2‑E2 – Abstract & Sec. 3.2, pp.1–2 – Inconsistent / unexplained β prediction 0.27°

**Offending text**

Abstract:

> “…this minimal setup naturally accommodates a birefringence rotation angle β ≈ 0.27◦ …”

Sec. 2.2:

> “…yielding β ≈ C0 θi × 5 × 10−3 rad ≈ 0.27◦.”

**Problem**

\(5×10^{-3}\,\text{rad} = 0.286°\), not 0.27°. More importantly, in Sec. 2.2 the 5×10^{-3} rad comes from “Δϕ/fa ∼ 10−2 … over the Hubble time” without any actual derivation or reference to the J0 expression in Eq. (1). The “prediction” is not quantitatively derived from the field equation given; it is an order‑of‑magnitude handwave, yet it is treated in the abstract as a sharp quantitative prediction. This is not acceptable at PRD level when it is central to the paper’s claim.

**Required fix (ESSENTIAL)**

- Either:
  - Provide a clear derivation of β ≈ 0.27° starting from Eq. (1), specifying the cosmological background, numerical integration, and how you obtain Δϕ/fa numerically; or
  - Explicitly downgrade the claim to a qualitative “order‑of‑magnitude” statement, not a precise prediction, and remove the specific 0.27° figure from the abstract and elsewhere.
- Correct the numerical conversion: 5×10−3 rad ≈ 0.29°, or adjust the coefficient consistently if 0.27° is the intended central value.

---

### P2‑E3 – Sec. 1, p.1 – Unsupported ACT DR6 significance claim

**Offending text**

> “The Planck HFI analysis [Minami and Komatsu, 2020] reported β = 0.35 ± 0.14◦ (2.5σ), and the ACT DR6 analysis confirmed the signal at comparable significance. Combined, the evidence exceeds 3.5σ.”

**Problem**

- The ACT DR6 birefringence analysis “Diego‑Palazuelos and Komatsu, 2025” is cited as “arXiv preprint, 2025” but no such paper is presently indexed; there is no publicly available ACT DR6 birefringence paper with those authors/date on arXiv or ADS.
- The statement “confirmed the signal at comparable significance” and “Combined, the evidence exceeds 3.5σ” is not traceable to an existing published or preprint result. This is a critical load‑bearing claim.

**Required fix (ESSENTIAL)**

- Verify that an ACT DR6 cosmic birefringence paper by Diego‑Palazuelos & Komatsu exists on arXiv/ADS with the quoted numbers; if it does not:
  - Remove all specific numerical claims (β = 0.215 ± 0.074°, 2.9σ; “comparable significance”) based on this nonexistent paper.
  - Remove or explicitly qualify the “combined evidence exceeds 3.5σ” statement as speculative or based on private communication, which PRD will typically not accept as a basis for quantitative claims.
- If such a paper appears, update the citation to the correct arXiv ID, title, and year, and make sure quoted β and σ match the abstract or tables.

---

### P2‑E4 – Sec. 3.1, p.2 – Unverified ACT DR6 numbers and combined β

**Offending text**

> “ACT DR6 [Diego-Palazuelos and Komatsu, 2025]: β = 0.215 ± 0.074◦ (2.9σ)  
>  These produce the combined constraint in Eq. 4.”

**Problem**

- As above, the ACT DR6 birefringence result is not verifiable in public databases.
- The combined constraint βcombined = 0.242 ± 0.061° is claimed, but only two measurements are given explicitly (Planck NPIPE and ACT DR6). Their inverse‑variance combination:

  \[
  β_c = \frac{0.30/0.11^2 + 0.215/0.074^2}{1/0.11^2 + 1/0.074^2} ≈ 0.245°
  \]

  and

  \[
  σ_c = (1/0.11^2 + 1/0.074^2)^{-1/2} ≈ 0.061°.
  \]

  The quoted mean 0.242° differs slightly; this could be rounding or inclusion of another measurement (WMAP?). The paper does not explain the discrepancy or list all data used in the combination.

**Required fix (ESSENTIAL)**

- List explicitly all measurements entering Eq. (3): if WMAP or other data are included, specify their values and uncertainties.
- Recompute and show the combined β and σ from the given numbers; ensure that the value quoted in Eq. (4) is reproducible from the listed inputs.
- If the ACT DR6 value remains unverifiable, remove it and recompute βcombined from the remaining measurements only.

---

### P2‑E5 – Sec. 3.2, p.2 – Definition and numeric value of “fphoton × C0”

**Offending text**

> “The effective photon coupling parameter:  
>  \( f_{\rm photon} \times C_0 = 1.73 ± 0.44 \) (Eq. 5).”

**Problem**

- “fphoton” is not defined anywhere in the text or equations, nor is the combination \(f_{\rm photon} × C_0\) derived from previous relations. The ALP‑photon coupling is usually \(g_{aγ} = C_0/f_a\); here the connection between Eq. (2) and Eq. (5) is not made explicit.
- It is impossible for a reader to reproduce the 1.73 ± 0.44 number from the preceding equations and data: the paper never shows the likelihood in terms of gaγ or fphoton, or the Jacobian from β to fphoton.

**Required fix (ESSENTIAL)**

- Define \(f_{\rm photon}\) precisely (e.g. is it \(f_a\), \(1/g_{aγ}\), or some rescaled parameter?), including dimensions.
- Show the explicit relation between β and \(f_{\rm photon} × C_0\) used to infer Eq. (5), and the data values entering that inference.
- Provide enough algebra that a reader can recompute the central value and uncertainty from βcombined and its σ.

---

### P2‑E6 – Sec. 3.3, p.2 – Confusion in notation for coupling: “Caγ” vs “C0”

**Offending text**

- Table 1 and Run 2 description: “Caγ flat on [1, 30] (Run 2 only).”
- Sec. 3.2 and 2.2 use “C0” and “gaγ = C0/fa”.

**Problem**

The manuscript uses “Caγ” (run prior) and “C0” (ABJ anomaly coefficient) without clearly stating whether these are the same parameter. This is ambiguous and prevents unambiguous mapping between theory and inference. For a methods paper in PRD, the coupling parameterization must be consistent.

**Required fix (ESSENTIAL)**

- Adopt a single notation for the anomaly/coupling coefficient and use it consistently in the theory section, MCMC prior, and posterior summaries.
- If “Caγ” ≡ “C0” or “C aγ = C0”, state this explicitly once and remove the inconsistent symbol.

---

### P2‑E7 – Sec. 3.3, p.2–3 – MCMC sample counts and convergence claims

**Offending text**

Table 1 and description:

> Run 1: 2,160 samples; Run 2: 6,840; Run 3: 720; all “Converged” with R̂ − 1 < 0.01.  
> “…small effective sample sizes (Neff ∼ 1,000)… Future work with longer chains (> 50,000 samples) would improve the reliability…”

**Problem**

- For a 3‑parameter (or more) ALP model with possibly non‑Gaussian posteriors, 720–6,840 total samples are marginal; quoting R̂ − 1 < 0.01 as “confirming adequate mixing” is overstated.
- The Bayes factors in Sec. 3.4 (ln B ≈ 5.17) are quoted to two decimal places despite the acknowledged poor sampling of tails. For PRD, Bayesian evidence claims based on such short chains and unstable tails are not methodologically robust.

**Required fix (MAJOR)**

- Temper the language: state that the convergence and evidence estimates are provisional and not robust to standard diagnostic scrutiny.
- Reduce the precision on ln B to at most one significant figure given the sampling limitations and explicitly qualify its reliability.
- Ideally, rerun the chains with significantly longer lengths (order ≥ 5×10^4 samples) and report Neff values to justify Bayes factor computations; otherwise, emphasize that evidence values are only indicative, not the main result.

---

### P2‑E8 – Sec. 3.4, p.3 – Bayes factor prior dependence and comparability

**Offending text**

> “ln B = 5.17 … computed via the Savage-Dickey density ratio with a flat prior β ∈ [0◦, 1◦]. The evidence is prior-dependent: ln B = 4.48 for β ∈ [0◦, 2◦] and ln B = 5.86 for β ∈ [0◦, 0.5◦].”

**Problem**

The text does mention prior dependence but does not make clear that these Bayes factors are *not directly comparable* to other null tests (e.g., Eskilt & Komatsu’s or Fujita et al.’s) that use different priors/parameterizations. Per the instructions, sigma values and evidence from different procedures must not be casually juxtaposed without explicit caveats.

**Required fix (ESSENTIAL)**

- At each place where ln B is compared implicitly or explicitly to a detection significance (e.g., “indicative evidence”), add a clear statement that Bayes factors derived under different priors are not directly comparable to each other or to σ‑based significances.
- Clarify that these ln B values are internal to this analysis and cannot be directly mapped onto the published evidence in other works without matching priors and parameterizations.

---

### P2‑E9 – Sec. 4, p.3 – Overstated LiteBIRD “9σ exclusion” claim

**Offending text**

> “For our prediction β = 0.27◦ : Significance = 0.27/0.03 = 9σ.  
>  … If LiteBIRD measures β = 0 ± 0.03◦ , the ALP explanation is excluded at 9σ.”

**Problem**

- The LiteBIRD projection σ(β) ≈ 0.03° is taken from LiteBIRD Collaboration (2023), but that number is model‑ and systematics‑dependent; the paper itself notes dependence on “self‑calibration strategy and systematic error budget,” yet treats the resulting 9σ as a hard exclusion.
- No marginalization over uncertainties in the theory prediction (C0 and θi are ∼ O(1) but not precisely known) or systematics is included; thus 9σ is not a robust, statistically justified exclusion significance.

**Required fix (MAJOR)**

- Rephrase to emphasize that 9σ is a naive signal‑to‑noise estimate under idealized assumptions; it is not a rigorous statistical exclusion significance once theory uncertainties and systematics are included.
- Remove or soften “excluded at 9σ” to “strongly disfavored” or similar, making clear that the exact σ depends on the final LiteBIRD performance and modeling assumptions.

---

### P2‑E10 – Sec. 5, p.4 – Companion paper citation “Golden, 2026a” and “14‑barrier catalog”

**Offending text**

> “…see the companion paper [Golden, 2026a] for the full ECH framework and 14-barrier catalog.”

**Problem**

The reference list specifies:

> “Houston Golden. Spin-torsion cosmology … Companion paper, submitted simultaneously, 2026a.”

This is not a published work and has no arXiv ID or journal information. Using it as the unique reference for a “full ECH framework and 14‑barrier catalog” means the main supporting theory is not publicly accessible or verifiable.

**Required fix (MAJOR)**

- Either:
  - Provide an arXiv identifier for “Golden, 2026a” and confirm that the 14‑barrier catalog and ECH framework are actually accessible there; or
  - Remove or significantly downplay reliance on this companion paper. Any crucial claims needed to understand the present work must be self‑contained or based on published literature.

---

### P2‑E11 – Sec. 6, p.5 – Citation “Namikawa, Murai & Naokawa [Namikawa et al., 2025]”

**Offending text**

> “Namikawa, Murai & Naokawa [Namikawa et al., 2025] provide superior ALP mass constraints…”

Reference:

> “Toshiya Namikawa, Kai Murai, and Sho Naokawa. Constraints on axion-like particles from cosmic birefringence. arXiv e-prints, 2025. In preparation; cited for comparison of ALP mass constraints.”

**Problem**

- The correct spelling appears in current arXiv/ADS as **Fumihiro** Naokawa, not “Sho” Naokawa.[1][3][4]
- The correct paper “Planck Constraints on Axion-Like Particles through Isotropic Cosmic Birefringence” (Phys. Rev. D 111, 043514 (2025)) exists with authors T. Namikawa, K. Murai, F. Naokawa.[1][3][5] The manuscript’s title and year (“Constraints on axion-like particles from cosmic birefringence”, 2025, “in preparation”) do not match the actual article.
- The paper is not “in preparation”; it is already published in PRD.

**Required fix (ESSENTIAL)**

- Correct the reference to the actual published article, including:
  - Correct author list: T. Namikawa, K. Murai, F. Naokawa.
  - Correct title: “Planck constraints on axionlike particles through isotropic cosmic birefringence.”
  - Correct journal, volume, page, and DOI (Phys. Rev. D 111, 043514 (2025), doi:10.1103/PhysRevD.111.043514).[5]
- Remove “in preparation; cited for comparison…” since it is now published.
- Ensure that any comparison of ALP mass constraints is consistent with the actual numbers in that paper.

---

### P2‑E12 – Sec. 6, p.5 – Mis-citation of Fujita et al. (2021) properties

**Offending text**

> “Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces β ∼ 0.3◦…”

Reference:

> “Tomohiro Fujita, Kai Murai, Hiromasa Nakatsuka, and Shinji Tsujikawa. Detection of isotropic cosmic birefringence and its implications for axionlike particles including dark energy.”

**Problem**

- Fujita et al. (Phys. Rev. D 103, 043509 (2021)) analyze isotropic cosmic birefringence and ALP models, but the assertion that they “demonstrated that a Planck-scale ALP naturally produces β ∼ 0.3°” must be explicitly traceable to their text or figures.[9] They do discuss ALPs including dark energy, but whether they specifically single out fa ~ MPl and β ~ 0.3° as “natural” is not obvious from their abstract.
- The paper here presents this as a direct conclusion of Fujita et al., but no equation or table number is cited.

**Required fix (MAJOR)**

- Add a precise citation (equation, section, or figure from Fujita et al.) where the fa ∼ MPl, β ~ 0.3° scenario is discussed.
- If Fujita et al. do not explicitly claim Planck‑scale fa as “natural” producing β ~ 0.3°, rephrase to say that such a configuration is consistent with their analysis, rather than “they already demonstrated.”
- Keep the title, journal, and DOI as they are correct.

---

### P2‑E13 – Sec. 6, p.5 – Claim of novelty and “our contribution”

**Offending text**

> “Our contribution is not the model itself, but rather the specific parameter identification (fa ∼ MPl, m ∼ H0) that produces a natural prediction matching the observed signal, and the inference framework demonstrating internal consistency.”

**Problem**

- The combination fa ~ MPl and m ~ H0 is conceptually close to standard “ultralight axion / quintessence‑like ALP” setups that have been widely discussed; Fujita et al. (2021) and Namikawa et al. (2025) already explore cosmological ALPs producing isotropic birefringence. The paper does not clearly demonstrate that this parameter pairing and “natural prediction” have not already been emphasized in prior work.
- The “inference framework” is a fairly straightforward Gaussian summary likelihood plus three short MCMC runs; the claim that this is the core novel contribution is weak for PRD unless more robust methodological advances are demonstrated.

**Required fix (MAJOR)**

- Carefully review Fujita et al. and Namikawa et al. to ensure that the parameter combination fa ~ MPl, m ~ H0 producing β ~ 0.3° has not already been presented as a natural scenario.
- If similar parameter choices already appear there, rephrase the novelty claim more modestly (e.g., “We highlight…” or “We revisit…” instead of “Our contribution is…”).
- Clarify what, if anything, is methodologically new in the inference beyond previous analyses.

---

### P2‑M1 – Sec. 2.1, p.1 – Equation (1) dimensional and conceptual clarity

**Offending text**

> “\(Δϕ ≈ f_a θ_i (1 − J_0(m/H_0)) ≈ f_a θ_i × O(1)\)” (Eq. 1)  

**Problems**

- The appearance of a Bessel function J0(m/H0) is not derived; no equation of motion or approximation is shown that leads to such a form. For a simple massive scalar in FRW, one usually solves \(\ddotϕ + 3H\dotϕ + m^2 ϕ = 0\); the Bessel form depends on specific approximations.
- Dimensional consistency is fine (J0 is dimensionless), but the context is missing: what cosmological background and variable change lead to J0(m/H0)? Is H0 there as a constant or part of a time‑dependent H(t)? As written, it looks ad hoc.

**Required fix (MAJOR)**

- Either provide a sketch derivation of Eq. (1) from the Klein‑Gordon equation in an expanding universe or cite a standard reference where this form is derived.
- Specify the approximations used (e.g., matter‑dominated background, constant H during some epoch) and the meaning of H0 in J0(m/H0).

---

### P2‑M2 – Sec. 2.2, p.1–2 – Phrase “no fine-tuning” vs. parameters of order unity

**Offending text**

> “The key feature: this prediction involves no small or large numbers beyond the cosmological integration factor. Every input is O(1) in natural units.”

**Problem**

The paper later shows that \(C_0 θ_i ≈ 3.4 ± 1.1\) (Eq. 8); order‑unity combinations can still embed non‑trivial tuning, depending on underlying microscopic model. The blanket statement “no fine‑tuning” is stronger than justified by the presented analysis.

**Required fix (MINOR)**

- Soften the claim to e.g. “no extreme tuning” or “no parametrically small/large dimensionless numbers; C0 and θi are O(1).”
- Make clear that whether this constitutes “no fine‑tuning” depends on the microphysics of the ALP, which is not specified here.

---

### P2‑M3 – Sec. 3.3, p.2–3 – Posterior values vs. observed βobs

**Offending text**

> “βALP = 0.336 ± 0.107°, βfree = 0.344 ± 0.096°, and βobs = 0.342 ± 0.094°. The ALP model reproduces the observed birefringence with no tension.”

**Problem**

The three numbers are extremely close because the ALP β posterior is effectively being driven by the same βobs measurement. Saying “with no tension” is mathematically true but somewhat tautological. For a PRD methods paper, it would be better to quantify tension using a more standard metric (e.g., Δχ^2 or posterior predictive checks) or avoid over‑interpreting this as a non‑trivial test.

**Required fix (MINOR)**

- Either:
  - Provide a short quantitative measure of consistency (e.g., specify the probability-to-exceed for the difference), or
  - Rephrase to a more modest statement such as “the ALP posterior for β matches the directly fitted β within the quoted uncertainties.”

---

### P2‑M4 – Sec. 6, p.5 – Reference to “matter-bounce non-Gaussianity fNL = −35/8” and Golden (2026b)

**Offending text**

> “The matter-bounce non-Gaussianity fNL = −35/8 provides a complementary and independent test [Golden, 2026b].”

Reference:

> “Houston Golden. Testing the matter bounce with primordial non-Gaussianity: Forecasts for SPHEREx and MegaMapper. Companion paper, submitted simultaneously, 2026b.”

**Problem**

- This value fNL = −35/8 is a standard matter‑bounce result but is attributed to a “companion paper” that is merely “submitted” and lacks arXiv ID or publication. That companion paper is not accessible for verification of any additional technical claims.
- For a PRD article, load‑bearing external claims should depend on published or at least arXiv‑posted results.

**Required fix (MAJOR)**

- Add a proper literature citation for the standard matter‑bounce fNL = −35/8 result from the existing cosmology literature, not only to an unpublished companion paper.
- Either provide an arXiv ID for Golden (2026b) or relegate its mention to a brief note without using it to support any quantitative claim.

---

### P2‑M5 – Abstract vs. body – Consistency of σ and β values

**Offending text**

Abstract:

> “We perform a Gaussian summary-likelihood inference … finding β = 0.242 ± 0.061◦ (3.9σ from zero)… The Bayes factor in favor of nonzero rotation is ln B = 5.17…”

Body:

- Eq. (4): βcombined = 0.242 ± 0.061° (3.9σ)
- Eq. (9): ln B = 5.17

**Problem**

The abstract accurately reproduces these numbers from the body. However, the σ significance 3.9σ is simply 0.242/0.061. This is fine mathematically but it should be made clear that the Gaussian assumption and independence of the two datasets underpin this value; any correlations or non‑Gaussian tails would change the significance. PRD expects explicit articulation of such assumptions.

**Required fix (MINOR)**

- Add a sentence in Sec. 3.2 stating that the 3.9σ significance assumes Gaussian posteriors and uncorrelated measurement errors across Planck and ACT; note that correlated systematics (e.g., similar self-calibration methodology) could reduce the true significance.

---

### P2‑N1 – Equation (3), p.2 – Minor typesetting issue

**Offending text**

> “L(β) = ∏i (1/√(2πσi^2)) exp( −(βobs−β)^2 / (2σi^2) ).”

**Problem**

The indices on βobs and σ are not consistent: the exponent uses “β obs” without index; strictly it should be βi,obs or βi. This is minor but confusing.

**Required fix (NIT)**

- Replace (βobs − β) with (βi − β) or (βi,obs − β) and define βi explicitly as the ith measurement (Planck NPIPE, ACT, etc.).

---

### P2‑N2 – Table 1, p.2 – R̂ notation

**Offending text**

> “R̂ − 1”

**Problem**

Standard notation is \(\hat R − 1\) or just R̂; the table uses “R̂ − 1 < 0.01” in the caption but the text refers to “Gelman-Rubin convergence diagnostic R̂ − 1 < 0.01”. This is acceptable but could be more precise by referencing a standard definition.

**Required fix (NIT)**

- Optionally add a brief parenthetical noting that R̂ is the Gelman–Rubin convergence statistic as defined in Gelman & Rubin (1992) or a standard MCMC reference.

---

### P2‑N3 – Minor wording / style: “spectator ALP” and “does not require a contracting phase”

**Offending text**

Sec. 5:

> “The ALP is a spectator field—it does not participate in the bounce dynamics … The prediction holds in any cosmological background where the ALP field begins rolling at z ∼ 1.”

**Problem**

This is qualitatively fine but could give the impression that the result is entirely independent of the background beyond “z ~ 1 rolling,” which is not strictly correct: the J0(m/H0) factor and Δϕ depend on background expansion history. This is more conceptual than technical here.

**Required fix (MINOR)**

- Slightly qualify to “in a broad class of cosmological backgrounds with similar late‑time expansion histories, the prediction structure holds, provided the ALP begins rolling at z ∼ 1.”

---

### P2‑N4 – Reference to “Namikawa, Murai & Naokawa [Namikawa et al., 2025] provide superior ALP mass constraints”

**Problem**

Once the reference is corrected (see P2‑E11), the statement “superior ALP mass constraints” is acceptable but should specify “relative to Fujita et al. (2021)” or “relative to earlier Planck-only analyses”; as written, “superior” is vague.

**Required fix (MINOR)**

- Rephrase to “Namikawa et al. (2025) derive tighter ALP mass constraints using the full Planck EB spectrum” and, if possible, mention the key improvement (e.g., using Planck EB over prior EB treatments).

---

### P2‑N5 – Use of “Companion paper, submitted simultaneously” in references

**Offending text**

References for Golden (2026a, 2026b) both say “Companion paper, submitted simultaneously”.

**Problem**

PRD generally expects either published or arXiv‑posted references. “Submitted” is not stable metadata and will rapidly become stale. Also, without identifiers, referees and readers cannot verify the content.

**Required fix (MAJOR)**

- Either update with arXiv IDs for both companion papers or remove their references as load‑bearing sources, retaining at most a brief informal mention in the text.

---

### P2‑N6 – No figure axes/units visible in text

**Offending text**

Figure 1 and Figure 2 are only described in captions; the actual axes and units are not reproduced in the text provided.

**Problem**

As presented, I cannot see axis labels, but for PRD the figures must have clearly labeled axes, units (degrees for β, etc.), and readable legends. You must ensure that in the actual PDF, axes are labeled (e.g., β in degrees, log10(m/eV), Caγ, θi, etc.) and that posterior densities are properly normalized.

**Required fix (ESSENTIAL for final submission)**

- Verify that the PDF figures have:
  - Axis labels with symbols and units (e.g., β [deg]).
  - Legends and credible intervals stated clearly.
  - No mismatches between caption text (e.g., “Caγ × θi = 3.4 ± 1.1”) and the plotted posterior.

Since I do not have the rendered graphics here, this must be checked carefully before submission.

---

## Bibliography Forensics

1. **Minami & Komatsu (2020)**  
   - Reference: Planck 2018 birefringence extraction.  
   - Cross‑check: Physical Review Letters 125, 221301 (2020) exists with matching title and DOI 10.1103/PhysRevLett.125.221301.  
   - Status: Correct.

2. **Eskilt & Komatsu (2022)**  
   - Reference: “Improved constraints on cosmic birefringence from the WMAP and Planck…”, Phys. Rev. D 106, 063503 (2022).  
   - Cross‑check: Correct title, journal, and DOI 10.1103/PhysRevD.106.063503.  
   - Status: Citation metadata correct; see P2‑E1 regarding numerical values drawn from it.

3. **Diego‑Palazuelos & Komatsu (2025)**  
   - Reference: “Cosmic birefringence from the Atacama Cosmology Telescope. arXiv preprint, 2025.”  
   - Cross‑check: No such arXiv entry is currently indexed under those authors and title.  
   - Status: As of now, this appears to be a non‑existent or future‑dated citation. Must be fixed or removed (see P2‑E3, P2‑E4).

4. **LiteBIRD Collaboration (2023)**  
   - Reference: “LiteBIRD science goals and forecasts: a full-sky CMB polarization survey.” Prog. Theor. Exp. Phys. 2023, 042F01, doi:10.1093/ptep/ptac150.  
   - Cross‑check: Metadata correct.  
   - Status: OK.

5. **Golden (2026a, 2026b)**  
   - References: Both “Companion paper, submitted simultaneously” with no identifiers.  
   - Cross‑check: Not found on arXiv/ADS by title or author; as “submitted” future references, these are not verifiable.  
   - Status: Problematic; see P2‑E10, P2‑M4, P2‑N5.

6. **Fujita et al. (2021)**  
   - Reference: Phys. Rev. D 103, 043509 (2021), correct DOI 10.1103/PhysRevD.103.043509.  
   - Cross‑check: Title, author list, and journal are correct.  
   - Status: OK; interpretive use needs clarification (P2‑E12).

7. **Namikawa, Murai, Naokawa (2025)**  
   - Reference in text: “Constraints on axion-like particles from cosmic birefringence. arXiv e-prints, 2025. In preparation; cited…”  
   - Actual: “Planck Constraints on Axion-Like Particles through Isotropic Cosmic Birefringence,” Phys. Rev. D 111, 043514 (2025), by T. Namikawa, K. Murai, F. Naokawa (not “Sho”).[1][3][5]  
   - Status: Incorrect metadata; must be fixed as per P2‑E11.

8. **Staleness / duplication**  
   - No exact duplicate entries, but two “companion paper” references by the same author without identifiers will rapidly become stale and should be rectified.  
   - No obvious DOI mismatches for the APS or PTEP references.

---

### Length vs. Contribution

The main substantive contribution claimed is a simple order‑of‑magnitude prediction (β ~ 0.27°) for a Planck‑scale ALP, plus a two‑measurement Gaussian combination and short MCMC runs. For this level of novelty, 6 pages is already close to the upper bound. Given the current weaknesses, if the paper is substantially strengthened (rigorous derivation of the prediction, corrected references, more robust analysis), the length could remain ~6 pages. In the present form, substantial portions (e.g., bounce‑cosmology discussion, companion‑paper references) read as extraneous and could be shortened once the core physics is tightened.

---

## Summary recommendation

**REJECT**

The manuscript contains multiple critical issues: a key observational reference (ACT DR6 birefringence) is not verifiable; a major reference (Namikawa et al.) is mis‑titled, mis‑dated, and mis‑authored; some central quantitative claims (β ≈ 0.27°, 9σ LiteBIRD exclusion, ln B ≈ 5.2) are not derived with sufficient rigor; and the reliance on unpublished “companion papers” is inconsistent with PRD standards. Addressing these problems would require deep restructuring, not just minor revision. I recommend rejection, with the suggestion that the author prepare a substantially revised, fully documented analysis with correct and publicly verifiable citations before resubmission.

---

## PASS 2 — self-critique findings (what initial review missed)

P2‑E14 – Sec. 3.2, p.2 – Significance “3.9σ from zero” inconsistent with quoted mean and error  
**Class: A (arithmetic), E (null‑procedure comparability)**  

**Offending text**  
> “βcombined = 0.242 ± 0.061◦ (3.9σ from zero)” (Eq. 4)  

**Problem**  
The quoted significance does not match the displayed numbers. The ratio is  
\[
0.242/0.061 \approx 3.97,
\]  
which rounds to **4.0σ**, not 3.9σ. The text gives a σ value that is neither a correct rounding of 3.97 nor explicitly computed from a different pair of numbers. There is no indication that systematics or other uncertainties were folded in to reduce the significance; it reads as a plain signal‑to‑noise. This creates avoidable confusion about how the significance was computed.  

In addition, this 3.9σ value (or 4.0σ if corrected) is then implicitly compared in the paper to the “3.6σ” Eskilt+ACT joint result and to a 2.5σ Planck HFI result (Minami & Komatsu 2020) without an explicit statement that these significances come from **different likelihoods and null procedures**, and thus are not directly comparable. This is exactly the type of juxtaposition PRD expects to be explicitly qualified.  

**Required fix (ESSENTIAL)**  
- Recompute and state the significance consistently with the quoted numbers, e.g. “4.0σ from zero” if it is simply βcombined/σ.  
- If a different error budget (e.g. including extra systematics) was used to obtain 3.9σ, show that calculation and give the effective σ used.  
- Wherever this combined σ is compared or contrasted to σ values from other analyses (Planck‑only, ACT, Eskilt joint), add an explicit disclaimer that these significances are based on different data combinations and analysis procedures and are not strictly comparable without harmonizing assumptions.  

---

P2‑E15 – Sec. 3.3 vs. Fig. 2 – Posterior means and uncertainties not explicitly tied to figure  
**Class: B (figure‑caption vs body‑claim), H (unquantified hedges)**  

**Offending text**  
- Sec. 3.3:  
  > “βALP = 0.336 ± 0.107◦ … βfree = 0.344 ± 0.096◦ … The ALP model reproduces the observed birefringence with no tension.”  
- Fig. 2 caption:  
  > “Comparison of β posteriors across all three model configurations … All three are consistent with each other and with the observed value βobs = 0.342 ± 0.094◦.”  

**Problem**  
The figure caption asserts “all three are consistent with each other and with the observed value,” but does not state *how* this consistency is quantified, and the body text does not reference the figure when making the “no tension” claim. The reader cannot easily verify, from the figure alone, that the plotted posteriors correspond exactly to the numerical summaries in Eqs. (6)–(7), nor how close they are in standard units.  

The phrase “no tension” is a qualitative hedge that hides the actual offsets; for example, the difference between βALP and βobs is 0.006°, far below the quoted uncertainties, but the manuscript never gives a numerical measure of that agreement (e.g. Δ/σ, or a simple χ²). This falls under the common “unquantified hedges” problem PRD warns about.  

**Required fix (MINOR)**  
- Explicitly state in the Fig. 2 caption that the curves correspond to the numerical posteriors summarized in Eqs. (6) and (7), so the visual claim is clearly tied to the reported numbers.  
- Replace or supplement “no tension” / “consistent with” with a quantitative statement, e.g. “the difference between βALP and βobs is 0.006°, corresponding to <0.1σ,” or provide a simple χ² or probability‑to‑exceed value.  
- In the main text, explicitly refer to Fig. 2 when making claims about consistency, so the reader can cross‑check the numbers and the plot.  

---

P2‑E16 – Sec. 2.1–2.2 – Dimensional and normalization issues in Eqs. (1)–(2) and Δϕ/fa estimate  
**Class: C (dimensional consistency), J (stale/incomplete derivation)**  

**Offending text**  
- Eq. (1):  
  > “\(\Delta\phi \approx f_a \theta_i \Big(1 - \frac{J_0(m/H_0)}{J_0(0)}\Big) \approx f_a \theta_i \times O(1)\).”  
- Eq. (2):  
  > “\(\beta = g_{a\gamma}\frac{\Delta\phi}{2} = \frac{C_0}{2f_a}\Delta\phi \approx \frac{C_0\theta_i}{2} \times O(1)\).”  
- Sec. 2.2 text:  
  > “…the cosmological field evolution gives Δϕ/fa ∼ 10−2 … yielding β ≈ C0 θi × 5 × 10−3 rad ≈ 0.27◦.”  

**Problem**  
1. **Incomplete normalization in Eq. (1)**: The ratio \(J_0(m/H_0)/J_0(0)\) is written, but \(J_0(0)=1\). This makes the fraction trivial and suggests either a relic of an earlier derivation or missing factors. As written, Eq. (1) reduces to \(\Delta\phi \approx f_a \theta_i(1-J_0(m/H_0))\), so the explicit division by \(J_0(0)\) is unnecessary and confusing. This hints at a partially edited equation.  

2. **Mismatch between “O(1)” and later numerical claim**: Eq. (1) and Eq. (2) say the factor multiplying \(C_0\theta_i/2\) is “O(1)”, but the text then states Δϕ/fa ∼ 10−2. For “O(1)” to be coherent with Δϕ/fa ∼ 10−2, the implicit factor would need to be ∼ 10−2, not order unity. Either the O(1) notation is misleading, or the Δϕ/fa estimate carries an extra implicit small factor that is not shown.  

3. **Dimensional clarity**: The basic dimensions are fine (ϕ and f_a both have mass dimension 1, so Δϕ/fa is dimensionless and β is dimensionless), but the presented expressions obscure which part of the calculation is responsible for the smallness of Δϕ/fa. PRD will expect the normalization to be explicit, not hidden in a vague “O(1)” factor that later is effectively 10−2.  

**Required fix (MAJOR)**  
- Simplify Eq. (1) to the form actually used, e.g. \(\Delta\phi \approx f_a\theta_i[1-J_0(m/H_0)]\), and explicitly explain where this comes from. If a more general expression motivated the J0(0) denominator, show it or remove the denominator.  
- Replace the generic “× O(1)” language with an explicit numerical factor consistent with the stated Δϕ/fa ∼ 10−2, e.g.  
  \[
  \Delta\phi \approx f_a\theta_i \times \kappa,\quad \kappa \simeq 0.01,
  \]  
  and state how κ is obtained.  
- Make the chain  
  \[
  \Delta\phi/f_a \to \beta
  \]  
  explicit, giving the actual numerical coefficient and its dependence on cosmological parameters, so the small factor 10−2 is manifest rather than buried in “O(1)”.  

---

P2‑E17 – Sec. 3.2 vs. Sec. 3.1 – Incomplete description of data entering the summary likelihood  
**Class: D (internal cross‑references), J (stale numbers)**  

**Offending text**  
- Sec. 3.1: “We use two independent birefringence measurements for the summary‑likelihood combination (Eq. 3): Planck NPIPE … ACT DR6 … These produce the combined constraint in Eq. 4.”  
- Sec. 3.2: “We perform a Gaussian summary‑likelihood analysis, combining the measurements under the assumption of independent errors: … The combined constraint is: βcombined = 0.242 ± 0.061◦ (3.9σ from zero).”  

**Problem**  
The text asserts that Eq. (4) is the result of combining “two independent birefringence measurements,” but does not show the intermediate step: the mean and variance implied by L(β) in Eq. (3). The reader must independently reconstruct that the Planck NPIPE and ACT DR6 numbers are indeed the only inputs, and there is no explicit confirmation that no additional data (e.g. WMAP, older Planck HFI) were folded into βcombined.  

Given the earlier statement that Eskilt et al. use WMAP + Planck and that Minami & Komatsu (2020) is also discussed, there is a risk of misinterpretation: Eq. (4) could be read as a combination of more than the two listed measurements, especially since the quoted βcombined almost but not exactly matches the two‑measurement inverse‑variance combination. This is an internal cross‑reference ambiguity.  

**Required fix (MAJOR)**  
- In Sec. 3.2, explicitly write the analytic inverse‑variance combination formula and show the step from the Planck and ACT inputs to βcombined and σcombined.  
- Add a clear statement that *only* the two listed measurements (Planck NPIPE and ACT DR6) enter Eq. (4), and that the Eskilt joint value and Minami & Komatsu result are not part of the combination.  
- If any additional dataset was actually included (e.g. WMAP constraints), list it, provide its numbers, and show the full combination explicitly so Eq. (4) can be reproduced.  

---

P2‑E18 – Abstract and Sec. 6 – “Matches the combined Planck + ACT measurement at 1σ” not quantified  
**Class: F (abstract faithfulness), H (unquantified hedges), E (σ comparability)**  

**Offending text**  
- Abstract:  
  > “…this minimal setup naturally accommodates a birefringence rotation angle β ≈ 0.27◦, consistent with the 3.6σ isotropic birefringence signal (βobs = 0.342±0.094◦…).”  
- Sec. 6, point 2:  
  > “The prediction matches the combined Planck + ACT measurement at 1σ.”  

**Problem**  
The “1σ” statement is not backed by an explicit calculation in the body. Using the combined value βcombined = 0.242 ± 0.061°, the difference between prediction and combined measurement is  
\[
\Delta\beta = 0.27^\circ - 0.242^\circ = 0.028^\circ,
\]  
so, relative to the combined σ, \(\Delta\beta/\sigma \approx 0.46σ\), i.e. well within 1σ. However, this computation is nowhere shown.  

Moreover, the abstract links β ≈ 0.27° directly to βobs = 0.342 ± 0.094° (Eskilt joint Planck+ACT), which yields  
\[
\Delta\beta = 0.072^\circ,\quad \Delta\beta/\sigma \approx 0.77σ,
\]  
again within 1σ, but this is not spelled out either. The text uses qualitative phrases (“consistent with,” “matches … at 1σ”) without providing the actual Δ/σ values, and it quietly mixes two different “measurements” (βobs vs βcombined) as objects with which the prediction is consistent. This is a subtle but important comparability issue.  

**Required fix (ESSENTIAL)**  
- In Sec. 6, explicitly show the calculation of Δβ/σ that leads to the “1σ” claim, and clearly state which measurement (βcombined or βobs) is being used.  
- In the abstract, either specify that “0.27° lies within 1σ of the 0.342 ± 0.094° Eskilt et al. result” and show Δ/σ somewhere in the body, or soften the wording to a qualitative statement (“broadly consistent”) and avoid quoting a σ level that is never derived.  
- Add a brief clarification that the “3.6σ” significance and the “1σ agreement” are based on different likelihoods / null procedures (Eskilt joint analysis vs. author’s Gaussian summary likelihood) and are therefore not strictly comparable unless assumptions are matched.  

---

P2‑E19 – Sec. 3.3 and Table 1 – R̂ and Neff inconsistency  
**Class: A (arithmetic / internal consistency), D (cross‑reference)**  

**Offending text**  
- Table 1: three runs with total “Samples” of 2,160; 6,840; and 720, each marked “Converged” with R̂ − 1 < 0.01.  
- Sec. 3.3:  
  > “The Gelman-Rubin convergence diagnostic R̂ − 1 < 0.01 confirms adequate mixing, but the small effective sample sizes (Neff ∼ 1,000) limit the precision…”  

**Problem**  
Given the stated total accepted samples (720–6,840), claiming Neff ∼ 1,000 for runs with only 720 total samples appears inconsistent. For a single‑chain MCMC, Neff cannot exceed the total number of samples; for multiple chains, a Neff of order 1,000 could be plausible, but the manuscript does not specify the number of chains or how the total “Samples” count is constructed (per chain vs total). This makes it impossible for the reader to reconcile the Table 1 counts with Neff ∼ 1,000 and with R̂ − 1 < 0.01.  

This is not merely a stylistic point: PRD expects that quoted convergence diagnostics and effective sample sizes be *reproducible* from the stated chain configuration. As written, the numbers are opaque and potentially inconsistent.  

**Required fix (MAJOR)**  
- Clarify whether the “Samples” column in Table 1 gives the number *per chain* or the total across all chains.  
- If multiple chains were used, state how many chains per run and how Neff was computed (e.g. from split chains, using a standard MCMC library).  
- Ensure that Neff values reported in the text are consistent with the total number of samples and the implied autocorrelation; if Neff ∼ 1,000 is only for the best‑sampled parameters and not for all, make that explicit.  

---

P2‑E20 – Sec. 7 – Abstract vs. conclusion wording on LiteBIRD significance  
**Class: F (abstract faithfulness), E (σ comparability)**  

**Offending text**  
- Abstract:  
  > “We forecast that LiteBIRD, with σ(β) ≈ 0.03◦, will test this prediction at 9σ significance—either confirming the signal or ruling out the ALP explanation decisively.”  
- Sec. 7:  
  > “LiteBIRD will provide a decisive test at ∼ 9σ statistical significance, contingent on the self-calibration strategy and systematic error budget.”  

**Problem**  
The conclusion correctly adds a caveat (“contingent on the self‑calibration strategy and systematic error budget”), but the abstract presents the 9σ value in a more absolute way (“will test … at 9σ significance”) without that qualifier. This is a classic abstract‑vs‑body mismatch: the body acknowledges that σ(β) ≈ 0.03° is a *projected* statistical uncertainty that depends on assumptions, but the abstract reads as if 9σ were a robust forecast independent of systematics.  

**Required fix (MAJOR)**  
- Modify the abstract to mirror the caveat already present in Sec. 7, e.g. “will *in principle* test this prediction at ≳9σ statistical significance, subject to LiteBIRD’s final self‑calibration strategy and systematic error budget.”  
- Ensure that all mentions of the 9σ forecast (abstract, Sec. 4, Sec. 6, Sec. 7) consistently characterize it as a naive signal‑to‑noise estimate relying on an idealized σ(β) and not a full end‑to‑end forecast including systematics and theory uncertainties.  

---

P2‑E21 – References section – Inconsistent treatment of preprints vs. published results  
**Class: D (cross‑references), J (stale numbers)**  

**Offending text**  
- For Diego‑Palazuelos and Komatsu: “arXiv preprint, 2025.”  
- For Namikawa, Murai, Naokawa: “arXiv e‑prints, 2025. In preparation; cited for comparison of ALP mass constraints.”  

**Problem**  
The body of the paper uses numerical values and “superior constraints” language that treat these works as if they were fully established results, while the reference list explicitly calls one of them “In preparation” and gives no arXiv identifier. This inconsistency complicates the reader’s ability to verify the data and constraints used and violates PRD’s expectation that load‑bearing numerical claims be traceable to publicly available sources.  

This overlaps with some of your earlier points but adds the specific issue that the **references section and the body make conflicting claims about publication status**: in the text, ACT DR6 is treated as a completed analysis; in the references, it is an “arXiv preprint” without ID; Namikawa et al. are “in preparation” while the body attributes published‑level constraints to them.  

**Required fix (ESSENTIAL)**  
- Align the references with the actual publication status (and update names, titles, years, and DOIs where appropriate).  
- In the body, clearly distinguish between published, arXiv‑available, and “in preparation” / private‑communication‑level results, and avoid using the latter as the basis for firm numerical claims.  

---

If you want, I can next go through the equations and the β–coupling mapping in more detail, and draft specific replacement text and equations that would bring the analysis up to a PRD‑acceptable standard.