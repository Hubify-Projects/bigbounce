# P2 auto-2026-06-08_1737pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (14330 chars)
**Wall time**: 50.5s

---

I can only do a **partial citation-forensics audit** from the provided paper text plus the limited search results, because I do **not** have the full rendered PDF with figures/tables/line-by-line pagination or live ADS/arXiv results for every reference. That said, the paper as provided already contains multiple **major citation and internal-consistency failures** that would block PRD acceptance.

- **P2-E1 — Abstract, p. 1:** The abstract states “**the 3.6σ isotropic birefringence signal (βobs = 0.342±0.094◦ from the Eskilt et al. joint Planck + ACT analysis)**,” but the body later says the combined Planck+ACT measurement is used in the inference and separately quotes **βobs = 0.342 ± 0.094◦** without showing a derivation from the two measurements listed in Sec. 3.1. The paper never demonstrates that the quoted 3.6σ follows from the stated mean and uncertainty, and the abstract also mixes a significance claim with a point estimate without clarifying the null test. **Required fix:** explicitly derive the 3.6σ from the stated value, define the null hypothesis used, and ensure the same dataset/combination is used consistently throughout the abstract and body.

- **P2-E2 — Abstract, p. 1; Sec. 3.2, p. 2:** The paper claims a Gaussian summary-likelihood inference gives **β = 0.242 ± 0.061◦** from Planck HFI and ACT DR6, but the listed inputs are **0.30 ± 0.11◦** and **0.215 ± 0.074◦**. Combining these two independent measurements by inverse-variance weighting yields a mean near **0.247◦** and uncertainty near **0.061◦**, so the quoted value is plausibly rounded, but the paper never shows the computation or the exact weighting. **Required fix:** show the explicit weighted-mean calculation and confirm whether 0.242 is a rounded or derived value; otherwise this is not reproducible.

- **P2-E3 — Sec. 3.2, p. 2:** The manuscript claims **“3.9σ from zero”** for **βcombined = 0.242 ± 0.061◦**. This is arithmetically consistent only if one uses \(0.242/0.061 \approx 3.97\), i.e. nearly 4σ; calling it 3.9σ is acceptable as rounding, but the paper should not mix “3.9σ” with later “3.6σ” and “2.7σ/2.9σ” side by side without explicitly warning that these are **not directly comparable** because they come from different estimators and datasets. **Required fix:** add an explicit statement that the significances are derived from different procedures and are not directly comparable.

- **P2-E4 — Sec. 2.1, p. 1:** Equation (1) is dimensionally and mathematically unclear:  
  \[
  \Delta\phi \approx f_a \theta_i \left(1-\frac{J_0(m/H_0)}{J_0(0)}\right)
  \]
  uses a Bessel function \(J_0\) of the dimensionless ratio \(m/H_0\), but the surrounding text gives no derivation, and the approximation “**For \(m/H_0\sim1\), \(1-J_0(1)\approx0.24\)**” is then used to motivate the later numerical claim. The paper never shows that this expression is the correct cosmological solution for a thawing ALP in \(\Lambda\)CDM. **Required fix:** provide a derivation or replace the formula with a properly cited, physically justified evolution equation.

- **P2-E5 — Sec. 2.2, p. 1:** The algebra in Eq. (2) is inconsistent in notation:  
  \[
  \beta = \frac{g_{a\gamma}}{2}\Delta\phi = \frac{C_0}{2f_a}\Delta\phi \approx \frac{C_0\theta_i}{2}\times O(1)
  \]
  but the text then claims \(\Delta\phi/f_a \sim 10^{-2}\) and uses that to obtain \(\beta \approx 5\times10^{-3}\,\mathrm{rad}\approx0.27^\circ\). This is numerically inconsistent: \(5\times10^{-3}\,\mathrm{rad}\approx0.286^\circ\), but the intermediate statement \(\Delta\phi/f_a\sim10^{-2}\) would give \(\beta\sim5\times10^{-3}\,\mathrm{rad}\) only if \(C_0\theta_i\sim1\), which the paper never demonstrates. **Required fix:** present a single consistent numerical chain from model parameters to \(\beta\), with all intermediate values.

- **P2-E6 — Sec. 2.2, p. 1:** The manuscript says “**Every input is O(1) in natural units**,” but the same section requires a field displacement ratio \(\Delta\phi/f_a\sim10^{-2}\), which is **not** an \(O(1)\) quantity. This is a load-bearing inconsistency in the naturalness argument. **Required fix:** either remove the claim or redefine the relevant naturalness criterion with explicit justification.

- **P2-E7 — Sec. 3.1, p. 2:** The paper cites **“Planck NPIPE [Eskilt and Komatsu, 2022]”** and **“ACT DR6 [Diego-Palazuelos and Komatsu, 2025]”** as independent birefringence measurements, but no bibliographic entry for the ACT paper is provided beyond “arXiv preprint, 2025.” This is incomplete for PRD bibliography standards. **Required fix:** provide full author list, exact title, arXiv identifier, and journal status.

- **P2-E8 — Sec. 3.3, p. 2:** The MCMC priors are stated as **“log10(m/eV) flat on [-35,-30]”** while the earlier text frames the model as **\(m\sim H_0\)**. Since \(H_0\) today corresponds to an energy scale around \(10^{-33}\,\mathrm{eV}\), the prior range \([-35,-30]\) brackets this only partially and is biased toward much heavier values than \(H_0\). The paper does not explain why the prior excludes the nominal target scale cleanly or how sensitive the posterior is to this choice. **Required fix:** justify the prior range and show prior sensitivity.

- **P2-E9 — Sec. 3.3, p. 2:** The table lists **Run 1: ALP (C = 8 fixed)**, **Run 2: ALP (C free)**, **Run 3: β free**, but the text later introduces **“Caγ × θi = 3.4 ± 1.1”** and elsewhere uses **\(f_{\rm photon}\times C_0\)**. The parameter naming is inconsistent across sections, and it is unclear whether \(C\), \(C_0\), \(C_{a\gamma}\), and \(f_{\rm photon}\) are the same quantity or different ones. **Required fix:** define every parameter once and use a single symbol consistently.

- **P2-E10 — Sec. 3.3, p. 3:** The quoted posterior **“βALP = 0.336 ± 0.107◦”** and **“βfree = 0.344 ± 0.096◦”** are said to reproduce the observed value **\(0.342 \pm 0.094^\circ\)**, but the paper never specifies whether these uncertainties are posterior standard deviations, 68% credible intervals, or Gaussian approximations. **Required fix:** define the statistical meaning of each quoted uncertainty and keep the convention consistent.

- **P2-E11 — Sec. 3.4, p. 3:** The Bayes factor **ln B = 5.17** is presented as if robust, but the same paragraph admits strong prior dependence: **4.48** for \([0,2]^\circ\) and **5.86** for \([0,0.5]^\circ\). This degree of prior sensitivity makes the evidential claim materially weaker than the prose suggests. **Required fix:** either downgrade the claim substantially or provide a principled prior justification and a sensitivity table.

- **P2-E12 — Sec. 4, p. 3:** The LiteBIRD forecast says **σ(β) ≈ 0.03°** and then computes **0.27/0.03 = 9σ**. This arithmetic is fine, but the statement “**either confirming the signal or ruling out the ALP explanation decisively**” is overstated because a null detection at 9σ would reject this parameter point, not necessarily the entire ALP class. **Required fix:** narrow the claim to the specific model point studied.

- **P2-E13 — Fig. 1 caption, p. 4:** The figure is described as a **“Triangle plot”** but the PDF excerpt provided does not show axis labels, scales, or parameter definitions. The caption alone is insufficient to validate the claim that the posterior is centered at **3.4 ± 1.1**. **Required fix:** ensure all axes are labeled in the figure and the caption states exactly which parameters and priors are shown.

- **P2-E14 — Fig. 2 caption, p. 5:** The figure compares three posteriors and says they are “all consistent with each other and with the observed value,” but no quantitative consistency measure is provided. Given the same abstract also distinguishes multiple “significances,” this invites confusion between model comparison, parameter estimation, and null-hypothesis testing. **Required fix:** add explicit definitions of what is being compared and, if claiming consistency, quantify it.

- **P2-M1 — Sec. 1, p. 1:** The statement “**The combined evidence exceeds 3.5σ**” is unsupported by any derivation in the text. **Required fix:** either cite the exact combined estimator and show the calculation or remove the claim.

- **P2-M2 — Sec. 2.1, p. 1:** The claim that the field is “**frozen during radiation and matter domination**” and begins rolling at **\(z\sim O(1)\)** is plausible for \(m\sim H_0\), but the paper gives no numerical integration of the equation of motion. **Required fix:** provide a computed evolution or cite a source demonstrating this behavior for the chosen parameter values.

- **P2-M3 — Sec. 3.1, p. 2:** The phrase **“different because it fits the full EB cross-spectrum rather than combining point estimates”** may be true, but the manuscript does not explain how the two estimators relate statistically. **Required fix:** define why the two estimates differ and whether they can be combined in a joint likelihood without double counting.

- **P2-M4 — Sec. 5, p. 4:** The statement that the ALP can be “**heuristically motivated as associated with the Barbero-Immirzi pseudoscalar sector of the Holst action**” is explicitly admitted to be non-derivational, so it should not be presented as physical support for the model. **Required fix:** demote this to speculative context or remove it from the main argument.

- **P2-M5 — Sec. 6, p. 5:** The sentence “**The matter-bounce non-Gaussianity \(f_{\rm NL}=-35/8\) provides a complementary and independent test**” is out of place in a paper whose central claim is cosmic birefringence from an ALP. It reads like an unrelated promotion of the companion paper and is not substantiated here. **Required fix:** remove or sharply limit this cross-paper claim unless the connection is developed quantitatively.

- **P2-M6 — Sec. 6, p. 5:** The line “**Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces β ∼ 0.3°**” is a strong literature claim that must be verified against the cited paper’s abstract or results. Based on the provided reference, the title is **“Detection of isotropic cosmic birefringence and its implications for axionlike particles including dark energy”** and the journal/DOI look plausible, but the manuscript’s wording should not imply that the prior paper established the same parameter identification \(f_a\sim M_{\rm Pl}, m\sim H_0\) unless that is explicitly shown in the cited source. **Required fix:** narrow the claim to what the cited paper actually demonstrated.

- **P2-M7 — References, p. 6:** The entry **“P. Diego-Palazuelos and E. Komatsu. Cosmic birefringence from the Atacama Cosmology Telescope. arXiv preprint, 2025.”** is incomplete and not PRD-standard. The search results provided do not confirm this exact title; the only related result is an arXiv record for **“Planck Constraints on Axion-Like Particles through Isotropic Cosmic ...”** on arXiv ID **2506.20824**, which is a different paper. **Required fix:** supply the exact arXiv ID and full metadata, and ensure the title matches the actual preprint.

- **P2-M8 — References, p. 6:** The entry **“Toshiya Namikawa, Kai Murai, and Sho Naokawa. Constraints on axion-like particles from cosmic birefringence. arXiv e-prints, 2025. In preparation; cited for comparison of ALP mass constraints.”** is internally contradictory. A work cannot simultaneously be an **arXiv e-print** and **“In preparation”** unless the arXiv posting exists; the provided search results do not validate this citation. **Required fix:** either cite a posted arXiv identifier and correct title/status, or remove the reference entirely.

- **P2-M9 — References, p. 6:** The companion-paper citations **Golden, 2026a** and **Golden, 2026b** are not normal bibliographic entries and are not traceable as standalone publications from the text provided. They are acceptable only if the manuscript itself contains a full reference list entry with titles, venue/status, and enough information to verify them. **Required fix:** replace placeholder-style companion-paper citations with complete references or remove them from the main evidence chain.

- **P2-M10 — Entire paper:** There is a repeated reliance on internal shorthand and potentially fused symbols: **C**, **C0**, **Caγ**, and **fphoton** appear to refer to overlapping concepts. This is a bibliography-adjacent metadata integrity issue because it contaminates interpretability across equations and cited comparisons. **Required fix:** standardize notation across the manuscript and define each symbol explicitly.

- **P2-N1 — Abstract and throughout:** The prose contains several promotional phrases such as **“decisively,” “overwhelming significance,” “natural,”** and **“clean exclusion.”** These are rhetorical rather than technical. **Required fix:** replace with quantitatively precise language.

- **P2-N2 — References, p. 6:** The entry **“LiteBIRD Collaboration. LiteBIRD science goals and forecasts: a full-sky cmb polarization survey.”** is lowercase-inconsistent in the title as rendered. **Required fix:** correct capitalization to match the published title exactly.

- **P2-N3 — Sec. 5, p. 4:** The phrase **“14-barrier catalog”** is unexplained jargon and reads like internal project terminology. **Required fix:** define it or remove it.

I cannot fully verify the requested arXiv/ADS metadata for each cited paper because the prompt only supplies one relevant search result set, and those results do not include the full bibliographic entries for several cited works. However, even with that limitation, the manuscript already fails on **traceability, internal notation consistency, incomplete references, and several unsupported or overstated claims**.

## Summary recommendation
**REJECT**

The manuscript does not yet meet PRD standards for citation integrity or methodological transparency. Several references are incomplete or internally contradictory, key numerical claims are not derived transparently, the notation is inconsistent across the paper, and multiple significance statements are mixed without the required caveat that they are not directly comparable. The ALP/birefringence argument may be interesting, but in its current form it is not sufficiently auditable or reproducible for acceptance.

---

## PASS 2 — self-critique findings (what initial review missed)

P2-E15 — Arithmetic: σ for Planck-only and ACT-only measurements (Sec. 1 & 3.1)  
- The introduction quotes the Planck HFI result as **β = 0.35 ± 0.14° (2.5σ)**, but the implied significance from these numbers is \(0.35/0.14 = 2.5\) only if one rounds aggressively; many readers would regard this as borderline but acceptable.  
- More seriously, in Sec. 3.1 the Planck NPIPE and ACT DR6 results are quoted as **0.30 ± 0.11° (2.7σ)** and **0.215 ± 0.074° (2.9σ)**, respectively.  
  - For Planck NPIPE, \(0.30/0.11 \approx 2.73\), which does match 2.7σ.  
  - For ACT DR6, \(0.215/0.074 \approx 2.91\), which matches 2.9σ.  
- The **problem** is that the introduction then states **“Combined, the evidence exceeds 3.5σ”** without any explicit combined estimator or arithmetic, and the later summary-likelihood combination gives **0.242 ± 0.061° (3.9σ)**, which is *not* the same combination as “Planck HFI + ACT DR6 point estimates” referenced in the introduction. This is a stale or mismatched number rather than a clean recomputation.  
  - **New issue:** the text implicitly treats at least three different “combined” significances (3.5σ in Sec. 1, 3.6σ from Eskilt et al. in abstract/Sec. 3.1, and 3.9σ from the summary-likelihood in Sec. 3.2) as if they were interchangeable, without ever calculating the 3.5σ or tying it to a defined estimator. There is no place in the paper where the 3.5σ is explicitly derived from the quoted inputs.  

P2-E16 — Arithmetic: “matches at 1σ” claim vs numbers (Sec. 6)  
- The Discussion states: **“The prediction matches the combined Planck + ACT measurement at 1σ.”**  
- The paper’s own numbers are:  
  - Prediction: **β ≈ 0.27°** (Sec. 2.2).  
  - “Combined” summary-likelihood: **0.242 ± 0.061°** (Sec. 3.2).  
  - Eskilt joint analysis value used for the MCMC: **0.342 ± 0.094°** (Sec. 3.1).  
- If the comparison is to **0.242 ± 0.061°**, the discrepancy is \(|0.27 − 0.242| = 0.028°\), which is **0.46σ**; that is within 1σ, but the text never specifies that this is the reference.  
- If the comparison is to **0.342 ± 0.094°**, the discrepancy is \(|0.27 − 0.342| = 0.072°\), which is **0.77σ**; still within 1σ, but again the reference is unstated.  
- **New issue:** the sentence “matches the combined Planck + ACT measurement at 1σ” has no unambiguous referent; there are two different “combined” numbers in the paper, and the statement is not tied to either by an explicit calculation or citation. This is a traceability failure in the arithmetic/interpretation rather than the numeric values themselves.  

P2-E17 — Arithmetic & logic: “ALP explanation is excluded at 9σ” (Sec. 4, Eq. 10)  
- The LiteBIRD forecast uses **σ(β) ≈ 0.03°** and a model prediction **β = 0.27°**, computing a detection significance of **0.27/0.03 = 9σ** in Eq. (10). That arithmetic is correct.  
- The text then states: **“If LiteBIRD measures β = 0 ± 0.03°, the ALP explanation is excluded at 9σ.”**  
- For a null measurement, the relevant test statistic is \(|0.27 − 0|/0.03 = 9σ\), which corresponds to rejection of **this specific parameter point** at 9σ, not the entire ALP explanation. The numerical 9σ is correct, but the logical extension from “this parameter point” to “the ALP explanation” is overstated.  
- **New issue (distinct from your P2-E12 wording fix):** the **same 9σ number is used both as a detection significance and as an exclusion significance** without noting that the exclusion significance assumes (i) Gaussian errors, (ii) vanishing theoretical uncertainty on β, and (iii) no degeneracy with other ALP parameters that could shift β. The paper never quantifies any theoretical or systematic uncertainty in the model prediction itself, so the quoted 9σ “exclusion” is numerically but not methodologically justified.  

P2-E18 — Arithmetic: MCMC sample counts vs claimed Neff (Sec. 3.3)  
- Table 1 lists accepted sample counts: Run 1: 2,160; Run 2: 6,840; Run 3: 720.  
- The text says: **“the small effective sample sizes (Neff ∼ 1,000) limit the precision…”**  
- For Run 3, there are only 720 total accepted samples; it is not possible for **Neff ∼ 1,000** to be true for that run. Even if Neff is quoted for the better-sampled runs, the paper does not specify which run the ∼1,000 refers to, and it reads as if it applied generically.  
- **New issue:** the Neff statement is numerically inconsistent with the table as written. At minimum, it is ambiguous and should specify per-run Neff; for Run 3 it appears outright impossible.  

P2-E19 — Equation dimensional consistency: Eq. (3) (Sec. 3.2)  
- Equation (3) is written as  
  \[
  L(\beta) = \prod_i \frac{1}{\sqrt{2\pi\sigma_i^2}} \exp\left(-\frac{(\beta_i^{\rm obs}-\beta)^2}{2\sigma_i^2}\right).
  \]  
- This is dimensionally consistent provided β and σ are in the same units (here, degrees).  
- **New issue:** the paper never specifies the unit choice in Eq. (3), yet later interprets the combined σ as **0.061°** and relates β directly to an angle in degrees without ever stating that β has been converted to **dimensionless radians** when entering the likelihood. For Gaussian likelihoods, this is typically harmless, but here β is used both in degrees (everywhere in text) and implicitly as a dimensionless variable in a probability density. The lack of explicit unit normalization is a minor but real dimensional-clarity failure for a key equation.  

P2-E20 — Equation clarity and unit normalization for ALP coupling (Eq. 2 vs later use)  
- Eq. (2) defines  
  \[
  \beta = \frac{g_{a\gamma}}{2}\Delta\phi = \frac{C_0}{2f_a}\Delta\phi,
  \]  
  but later the analysis uses **fphoton × C0** and **Caγ** as effective couplings without ever showing how these map back to \(g_{a\gamma}\) or to a dimensionless \(\beta\).  
- The rotation angle β is dimensionless in radians, yet it is quoted exclusively in degrees; Eq. (2) never spells out whether β is measured in radians or degrees in the subsequent numerical estimate.  
- **New issue (beyond your notation-consistency concerns):** the **degree–radian conversion factor is nowhere made explicit** in the chain from Eq. (2) to the numerical β ≈ 0.27°. That means Eq. (2) is dimensionally consistent only if β is in radians, but the text then drops directly into degree values without a stated conversion, which is a subtle but genuine dimensional-transparency problem for the main prediction.  

P2-E21 — Internal cross-reference: “Eq. 3” vs location of summary likelihood (Sec. 3.1)  
- Sec. 3.1 says: **“We use two independent birefringence measurements for the summary-likelihood combination (Eq. 3).”**  
- Eq. (3) is indeed the summary-likelihood defined in Sec. 3.2, so the numeric cross-reference is correct.  
- **New issue:** the text here calls it *“summary-likelihood combination (Eq. 3)”* but immediately after, Sec. 3.2 uses that same Eq. (3) to define **L(β)** as a product over *i* that includes **βobs**, without ever stating explicitly that the βobs used in Eq. (3) are precisely the two measurements listed in Sec. 3.1. There is a missing explicit mapping from “Planck NPIPE, ACT DR6” to the \(\beta_i^{\rm obs}\) in Eq. (3). This is a cross-reference clarity failure rather than a mislabel, but it directly affects reproducibility of the likelihood.  

P2-E22 — Null-procedure comparability: significance list in Discussion bullet 2 (Sec. 6)  
- Bullet 2 in Sec. 6 reads: **“Consistency with data: The prediction matches the combined Planck + ACT measurement at 1σ.”**  
- Earlier, the paper has:  
  - **2.5σ** (Planck HFI; different pipeline).  
  - **2.7σ** (Planck NPIPE).  
  - **2.9σ** (ACT DR6).  
  - **3.5σ** (“combined” from introduction, never defined).  
  - **3.6σ** (Eskilt joint Planck+ACT).  
  - **3.9σ** (summary-likelihood combination).  
- **New issue (distinct from P2-E3 and P2-M1):** the Discussion uses “matches at 1σ” as if it were an invariant, without acknowledging that the σ-structure depends on which of these heterogeneous estimators and datasets is chosen as the “combined Planck + ACT measurement.” This is an additional juxtaposition of σ-values from different null procedures without an explicit “not directly comparable” caveat in the interpretive summary.  

P2-E23 — Abstract faithfulness: definition of “natural” vs body (Abstract vs Sec. 2/6)  
- Abstract: “This minimal setup naturally accommodates a birefringence rotation angle β ≈ 0.27° … The prediction is natural in the sense that fa ∼ MPl is the natural scale … m ∼ H0 ensures the field is rolling today, and θi ∼ O(1) is generic.”  
- In the body:  
  - Sec. 2.2 asserts **Δϕ/fa ∼ 10⁻²** “from the ratio of field displacement to decay constant over the Hubble time” without computing it.  
  - Sec. 6 bullet 1 repeats the “naturalness” claim but does not quantify the conditions under which Δϕ/fa is indeed ∼10⁻² for θi ∼ 1 and m ∼ H₀.  
- **New issue (beyond your P2-E6 and P2-M2 naturalness concerns):** the **abstract defines “natural” explicitly in terms of mass, scale, and misalignment**, but the body never shows that these assumptions *uniquely* or *robustly* lead to β ≈ 0.27° across the stated prior range (log₁₀ m/eV ∈ [−35, −30], θi ∈ [0.01, π]). The forecast and the MCMC both treat β as a free parameter; there is no calculation demonstrating that for *generic* draws from the stated priors the model yields β ∼ 0.27°. Thus the abstract’s strong naturalness definition is not actually substantiated by the quantitative parts of the body, which treat β largely phenomenologically.  

P2-E24 — Abstract faithfulness: “spectator ALP” vs role in data analysis (Abstract vs Sec. 3)  
- Abstract: “We present predictions and constraints for cosmic birefringence from a spectator axion-like particle …”  
- Body:  
  - Sec. 3.2 and 3.3 treat β as a directly fitted parameter with summary likelihoods and MCMC, without incorporating the ALP’s full dynamics (e.g., mass dependence, time evolution) into the likelihood; the ALP physics enters only through simple proportionality between β and a coupling parameter or Caγ × θi.  
- **New issue:** the abstract’s framing as “predictions and constraints for cosmic birefringence from a spectator ALP” suggests that the data analysis includes the *time-dependent* ALP-induced EB spectrum, yet **no such model-dependent EB angular power spectrum** is ever written or used. The constraints are on β, not on the ALP field evolution itself. This is a faithfulness gap between the “ALP prediction” advertised and the phenomenological β-fitting actually performed.  

P2-E25 — Unquantified hedges: “no tension” (Sec. 3.3)  
- Sec. 3.3 states: “The ALP model reproduces the observed birefringence with **no tension**.”  
- The numbers:  
  - ALP model (Run 1): 0.336 ± 0.107°.  
  - Model-independent fit: 0.344 ± 0.096°.  
  - Observed value: 0.342 ± 0.094°.  
- The central values differ by \(|0.336 − 0.342| = 0.006°\), which is indeed tiny relative to the errors, but the statement “no tension” is not quantified: no χ², no p-value, no posterior predictive check.  
- **New issue:** this is an **unquantified hedge**: a qualitative “no tension” statement used in place of a quantitative consistency measure, despite having sufficient numbers to compute a simple Δ/σ or χ². Given the paper’s emphasis on σ-levels elsewhere, this stands out as an uncharacteristically unquantified assertion.  

P2-E26 — Unquantified hedge: “all three are consistent” (Fig. 2 caption vs body)  
- Fig. 2 caption: “All three [posteriors] are consistent with each other and with the observed value βobs = 0.342 ± 0.094°.”  
- Sec. 3.3 provides posterior means and 1σ widths but **no overlap metric** (e.g., pairwise differences in units of combined σ, Kullback–Leibler divergences, or posterior predictive comparisons).  
- **New issue (beyond your P2-E14):** the **body never quantifies the consistency claim made in the caption**, not even with a straightforward comparison such as \(|\beta_{\rm ALP} − \beta_{\rm free}|/\sqrt{\sigma_{\rm ALP}^2 + \sigma_{\rm free}^2}\). Since σ-level arithmetic is used heavily elsewhere, this omission is conspicuous and fits the “unquantified hedge” pattern.  

P2-E27 — Stale/mismatched numbers: “3.6σ Eskilt et al. joint Planck + ACT” vs cited paper (Sec. 3.1 & abstract)  
- The abstract and Sec. 3.1 both refer to **“βobs = 0.342 ± 0.094°”** as **“the 3.6σ isotropic birefringence signal”** from Eskilt et al.  
- Numerically, \(0.342/0.094 ≈ 3.64\), consistent with a 3.6σ statement.  
- **New issue:** the paper never clarifies whether the **3.6σ** is the significance *quoted by Eskilt et al.* or rederived here, and it does not show that the same estimator and priors were used. Given that other combined significances (3.5σ, 3.9σ) are the author’s own constructions, the 3.6σ could be a **stale import from Eskilt et al.** being mixed with the author’s different analysis, yet it is presented as if all these σ values live in the same statistical framework. This is an additional cross-procedure comparability problem, beyond the earlier generic “significances are mixed” concern.  

P2-E28 — Appendix/main-text mismatch (implicit)  
- There are no appendices in the provided text, but the main text repeatedly alludes to additional structure (e.g., “full ECH framework and 14-barrier catalog” in the companion paper; Savage–Dickey Bayes factor calculation details; Hubble-time field evolution giving Δϕ/fa ∼ 10⁻²) that would typically require technical derivations.  
- **New issue (by absence):** the paper makes **nontrivial methodological claims (Savage–Dickey, cosmological integration, MCMC setup, prior dependence)** without providing either an appendix or a pointer to where the concrete calculation is presented. For PRD, this leaves the main analysis under-documented, especially for the Bayes factor and the cosmological evolution that generate the central β ≈ 0.27° prediction. This is a structural incompleteness rather than a mislabel, but it falls squarely under the “appendix vs main text” rigor expectation.  

If you would like, I can next:  
- Explicitly recompute the inverse-variance combination of the Planck NPIPE and ACT DR6 numbers to show the exact 0.242/0.061 derivation, and  
- Propose precise, minimal wording and equation fixes that would repair the most serious new issues (P2-E15, E17, E18, E23, E24, E27) to PRD standards.