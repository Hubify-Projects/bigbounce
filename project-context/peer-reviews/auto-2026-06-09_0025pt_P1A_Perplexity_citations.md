# P1A auto-2026-06-09_0025pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (10017 chars)
**Wall time**: 64.4s

---

The PDF as provided is **not publication-ready for PRD**. It contains extensive **internal/bookkeeping prose**, unresolved **self-contradictions**, multiple **unsupported numerical claims**, and a bibliography with several **future-dated or in-preparation references that cannot be verified as cited** from the text alone; that combination is enough for rejection on citation-forensics grounds.

I cannot perform the requested arXiv/NASA ADS web verification from the materials actually available in this chat because the only search results returned are unrelated PDF-accessibility pages, not the cited physics references. So I can only audit the manuscript text itself and flag issues that are already evident in the rendered paper.

- **P1A-E1 — Abstract p.1** — The abstract claims “**13 logically-independent mechanism-class constraints**” and “**channel-level closure**,” but later the manuscript repeatedly says this is **not** a full operator-basis no-go and that omitted operators remain unclosed. This is a scope mismatch in the headline claim. **Fix:** rewrite the abstract to state the exact limited scope and remove any implication of a theorem stronger than what is proven.

- **P1A-E2 — Abstract p.1** — “**The Holst dual contraction ϵµνρσ Rµνρσ vanishes identically on the Levi-Civita connection (T = 0) by the first (algebraic) Bianchi identity**” is asserted as a central theorem, but the paper also says an earlier draft misidentified this with the Pontryagin density and that the result is a corrected bookkeeping identity. **Fix:** state the precise identity cleanly, remove overclaiming language, and explicitly distinguish the Holst contraction from Pontryagin throughout.

- **P1A-E3 — Abstract p.1** — The abstract says “**Ntot ≈ 92 post-bounce e-folds**,” but Appendix B later says the same ansatz implies **Ntot ≈ 94** and that the 92 value is only approximately consistent at the 2% level. **Fix:** choose one number or present a range with explicit uncertainty and derivation.

- **P1A-E4 — Abstract p.1** — “**fNL = −35/8**” is presented as a surviving prediction, but later sections admit it is **not ECH-specific** and is a property of the matter-bounce class under additional assumptions. **Fix:** move this out of the abstract’s core result and label it as an external class-level observable.

- **P1A-E5 — Abstract p.1** — “**β ≈ 0.27°**” is described as a benchmark and then later explicitly denied as an ECH prediction. **Fix:** remove it from the abstract’s main result or clearly label it as a non-ECH spectator-ALP consistency point.

- **P1A-M1 — p.1, abstract and p.3–4** — The manuscript repeatedly says the four routes are **not** a complete operator basis, yet the title and abstract present **“closure”** in a way that reads as a theorem. **Fix:** replace “closure” with “channel-level exclusion under stated assumptions” everywhere appropriate.

- **P1A-M2 — p.1, abstract** — “**14 historical catalog entries, of which B8 is subsumed by B14**” is a self-referential counting scheme that inflates the barrier count while admitting non-independence. **Fix:** report only independent barriers in the main count and list the redundant historical entry separately.

- **P1A-M3 — p.1** — The abstract mentions “**the four enumerated routes (NJL, one-loop EA, Immirzi running, parity-CMB)**,” but later the paper says R4 is not amplitude excluded, only blocked by naturalness. **Fix:** do not present all four as equally closed on the same basis.

- **P1A-M4 — p.2 note** — The footnote starting “**a This Bianchi-identity vanishing is distinct from — and should not be confused with — the Pontryagin density**” is a long corrective aside inside the main narrative. **Fix:** move this to a short technical appendix note; it currently reads like a draft correction.

- **P1A-M5 — p.3** — “**Paper I(b) [6], in preparation**” is used to justify numerical cosmological inputs that are not independently verifiable in this paper. **Fix:** either publish the companion work first or remove all dependence on unpublished internal numbers.

- **P1A-M6 — p.3** — The paper says companion values are “**documented internally rather than as externally citable arXiv-posted numbers**.” That is unacceptable for a PRD submission when those numbers are load-bearing. **Fix:** replace internal-analysis inputs with reproducible published data or remove them.

- **P1A-M7 — p.4 Table I** — The table claims “**H0 = 67.68 ± 1.06, ∆Neff ≈ 0**” as a paper result while the text elsewhere says these are from an unpublished companion analysis and not independently peer-reviewable. **Fix:** remove or clearly segregate all unpublished posterior values from the paper’s own claims.

- **P1A-M8 — p.4 Table I** — The note “**3–5σ realistic after full systematic budget**” for fNL conflicts with the later footnote stating the raw ratio is \(4.375/0.7 \approx 6.25σ\). **Fix:** make clear which σ estimate is forecast-ideal, which is systematic-degraded, and why the reported range is 3–5 rather than ~6.

- **P1A-M9 — p.4 Fig. 1** — The figure is a schematic “map” with no quantitative axes or explicit definitions of the arrows; it appears largely decorative. **Fix:** either add quantitative content or remove it.

- **P1A-M10 — p.5–6 Eq. (1)** — The action mixes terms with inconsistent dimensional bookkeeping in the prose around \(T^{abc}T_{abc}\), and later Appendix B says the operator written in Eq. (6) is not a controlled EFT operator. **Fix:** provide a strict derivation with consistent mass dimensions or stop presenting it as an action-based foundation.

- **P1A-M11 — p.6 Eq. (4)** — The coefficient of the four-fermion term is written as \(\frac{3\pi G_N}{2}\times \frac{\gamma^2}{\gamma^2+1}\), but the surrounding text alternates between \(G\), \(G_N\), and \(M_{\rm Pl}^{-2}\) without a consistent convention. **Fix:** choose one convention and use it consistently.

- **P1A-M12 — p.6 Eq. (5–6)** — The operator \(e^I\wedge e^J\wedge F_{IJ}\) is later acknowledged to have **off-shell mass dimension +1**, not the required +4. This means the central dark-energy mapping is explicitly an ansatz, not a derivation. **Fix:** stop referring to this as an “effective action” in the usual EFT sense; call it a phenomenological scaling ansatz.

- **P1A-M13 — p.6–7** — The derivation of the \((T_{\rm reh}/M_{\rm GUT})^{3/2}\) factor is explicitly described as “**dimensional-analysis-aesthetic**” rather than derived from a thermal partition function. **Fix:** either derive it properly or remove its quantitative role in the argument.

- **P1A-M14 — p.6–7** — The manuscript alternates between saying the dilution factor is physically operative and saying it is merely bookkeeping. This is a direct internal inconsistency. **Fix:** choose one interpretation and keep it fixed.

- **P1A-M15 — p.7** — “**Mcrit ≈ 10−3 M⊙**” is asserted without a citation in the body and is not used in any transparent calculation. **Fix:** cite the source and show how it enters the argument, or remove it.

- **P1A-M16 — p.7** — The text states “**The parity-odd operator coupling α/M ∼ 10−21 GeV−1 underpredicts any plausible spin asymmetry by >100 orders of magnitude**” but the manuscript later treats that same coupling as sufficient for birefringence fits. **Fix:** explain the different observables and why one coupling can be relevant for one channel but irrelevant for the other.

- **P1A-M17 — p.8 Section IIIA** — Equation (12), \(C_\ell^{EB}\approx 2\beta C_\ell^{EE}-C_\ell^{BB}\), is presented without stating the perturbative regime or approximation order. **Fix:** specify the small-\(\beta\) assumptions and whether higher-order terms are neglected.

- **P1A-M18 — p.8 Section IIIA** — “**The parity-odd structure is qualitatively consistent with the observed isotropic birefringence at β ≈ 0.27°–0.30°**” conflicts with the later use of \(\beta_{\rm obs}=0.342°\pm0.094°\) as the relevant central value. **Fix:** keep one observational target value and distinguish it from benchmark values.

- **P1A-M19 — p.8 Section IIIB** — The claim that the spin asymmetry null “**refutes Shamir’s claimed 3% asymmetry at high significance**” is not supported here by any reproduced statistical calculation. **Fix:** include the exact statistic, sample size, null model, and p-value derivation in this paper or cite a fully accessible source.

- **P1A-M20 — p.9 Eq. (14–15)** — The one-loop Route 2 amplitude estimate contains multiple dimensionful manipulations and then admits an alternative ordering giving a “**numerically distinct ∼10−33 ratio**.” That is a serious instability in the no-go estimate. **Fix:** provide one unambiguous dimensional derivation and remove the alternative estimate unless it is fully justified.

- **P1A-M21 — p.9 Route 2** — The paper says the coefficient is “**not literally derived**” and is used as an “**upper-bound EFT ansatz**.” That is not sufficient for a hard no-go statement at PRD level. **Fix:** present it as a heuristic bound, not as a proof of closure.

- **P1A-M22 — p.9 Route 3** — The equation \(d\gamma/d\ln\mu = \frac{1}{12\pi^2}(N_{FL}-N_{FR})\gamma + O(\gamma^2)\) is admitted to be only “schematically motivated” and not the explicit RG equation from the cited literature. **Fix:** either derive or correctly quote the actual running from the source paper.

- **P1A-M23 — p.9 Route 3** — The claim “**suppressed by an additional factor of (∆γ/γ)·(H/MPl) ∼ 10−63 relative to the dark-energy density**” is dimensionally opaque and not shown from a reproducible chain of equations. **Fix:** show the complete dimensional conversion.

- **P1A-M24 — p.10 Route 4** — The manuscript states that \(m_\theta\sim H_0\) is required, then later says the natural ALP range \(10^{-22}\)–\(10^{-15}\) eV overshoots ρΛ by 22–36 OOM. This is internally consistent only under the fixed one-loop matching assumption, which the paper itself says is not derived. **Fix:** separate the assumption-dependent and assumption-free statements.

- **P1A-M25 — p.10 Route 4** — “**if α/M is instead treated as a free phenomenological parameter, both βobs and ρΛ can be matched for arbitrary mθ**” means the stated no-go is not fundamental. **Fix:** downgrade the claim from no-go to parameter-tuning critique.

- **P1A-M26 — p.11 Section V** — The galaxy spin pipeline is delegated to “Paper IV ” and no reproducible method is shown here despite the result being used in the argument. **Fix:** include at least the essential methodology and the exact statistic used.

- **P1A-M27 — p.11 Section VI** — The paper mixes “confirmed null,” “consistent with ΛCDM,” and “surviving parity-violation evidence” without explicitly distinguishing which result pertains to which dataset and null model. **Fix:** add a clean result matrix with one line per channel and one null hypothesis per line.

- **P1A-M28 — p.11 Section VII footnote** — The footnote contains a computation of \(|0.342-0.27|/\sqrt{0.03^2+0.094^2}\) but then concludes LiteBIRD will not separate the values. That arithmetic is fine, but it should be in the main text if used to support a central claim. **Fix:** move the numerical discrimination argument into the main body.

- **P1A-M29 — p.12 Table II** — Barriers 8 and 14 are explicitly said to be non-independent, but Table II still counts them as separate items in the headline “14 constraints.” **Fix:** present 13 independent barriers and one dependent consequence, not 14 equal constraints.

- **P1A-M30 — p.12 Barrier 1** — “**To achieve geff ∼ 1, one needs mT ∼ MPl**” is asserted without derivation. **Fix:** show the coupling estimate and the scale relation explicitly.

- **P1A-M31 — p.13 Fig. 3** — The “naturalness window” is visually defined but not numerically specified in the caption or axes. **Fix:** label the axes and define the gray band quantitatively.

- **P1A-M32 — p.14 Barrier 12** — Equation (20), \(\Omega^{\rm ECH}_{GW}|_{\rm bounce}\lesssim (\rho_{\rm crit}/\rho_{\rm Pl})^2\), is presented as an upper bound but then compared to PTA amplitudes in a way the text itself says is not directly comparable. **Fix:** either derive the transfer function or remove the PTA comparison from the quantitative claim.

- **P1A-M33 — p.15 Section X, step 4** — The proof claims the Holst term vanishes “**at any order**” on the Levi-Civita connection. That conclusion should be stated carefully: what vanishes is the specific Holst contraction under the stated assumptions, not all possible parity-odd effects in the full theory. **Fix:** narrow the statement to the exact operator and assumption set.

- **P1A-M34 — p.16 Section XI** — The “hybrid loophole” discussion is internally confusing: it says the mechanism is “closed,” then says the paper adds “w0wa” with no new theoretical content, then says the quantitative test is unfinished. **Fix:** reorganize into a short limitations subsection and remove the appearance of an incomplete side-analysis.

- **P1A-M35 — p.16–17** — The manuscript repeatedly says results are “not a prediction of ECH itself” while still using them in the paper’s advertised “surviving predictions.” **Fix:** separate *ECH predictions* from *broader bounce/ALP phenomenology*.

- **P1A-M36 — p.17 Section XII A** — “**Ξ ≈ 10−123, decomposed as 10−2 × Dinf with Dinf ∼ 10−121**” is a numerical chaining of unverified ansatz factors. **Fix:** show the origin of each factor and whether the decomposition is derived or chosen.

- **P1A-M37 — p.17** — The claim “**the framework has not solved the cosmological constant problem; it has only relocated the fine-tuning**” is honest, but it directly contradicts the earlier rhetorical framing of a “closure theorem.” **Fix:** tone down the abstract and title language accordingly.

- **P1A-M38 — p.18 Table III** — Several entries are marked “not tested” or “—” while the caption suggests a model discrimination table. **Fix:** do not present uncomputed cells as if they support a conclusion.

- **P1A-M39 — p.18 Section XIII** — The text says SPHEREx tests are “**3–5σ realistic significance**” but the footnote itself calculates a 6.25σ idealized number. **Fix:** harmonize the forecast numbers and state the assumptions used for each.

- **P1A-M40 — p.18 Section XIII** — “**LiteBIRD will detect non-zero β at ∼9σ (0.27°/0.03° overall sensitivity number)**” is later immediately revised to say the *model-discrimination* test against the current central value is only ~0.73σ. This is not a contradiction if stated carefully, but here it is not. **Fix:** distinguish “detection vs zero” from “discrimination vs current central value” in the main text.

- **P1A-M41 — p.19 Section XIV D** — The “structural tension” between Ntot and fNL is used as a supporting argument, but it depends on assumptions from the companion Paper II and on the ansatz in Appendix B. **Fix:** clearly mark this as conditional and not standalone.

- **P1A-M42 — p.19 Section XIV E** — The claim that the 13 barriers “close each” of the four routes is too strong given the admitted incompleteness of the operator basis. **Fix:** state that the four *enumerated channels* are closed, not the full ECH parity-odd sector.

- **P1A-M43 — p.20 Data and Code Availability** — The repository path is presented, but no commit hash, archived release, or data snapshot is given. **Fix:** provide a frozen archival version suitable for refereeing.

- **P1A-M44 — p.20 Appendix A / B** — Appendix B says “**Ntot ≈ 92**” and also “**Ntot ≈ 94**” from the same hierarchy, calling the difference an ansatz choice. This undermines the precision of every load-bearing e-fold statement in the paper. **Fix:** define the parameter with an uncertainty budget before using it in conclusions.

- **P1A-M45 — p.20 Appendix B** — The statement that “**a controlled EFT-level construction remains left to a separate companion treatment**” is essentially an admission that the core operator claim is not yet established. **Fix:** downgrade the paper’s claims accordingly.

- **P1A-M46 — p.21–23 References** — Several cited works are marked “**in preparation**,” “**this volume**,” or given internal IDs like **hUBIFY-2026-001B**. That is not an acceptable bibliography for claims that depend on them. **Fix:** remove reliance on unpublished internal references or make the underlying data/publication accessible and citable.

- **P1A-M47 — p.21 Ref. [2], [6], , , ** — The bibliography includes multiple self-citations to unpublished companion papers that are used for numerically essential claims. This is a citation-support problem, not merely a style issue. **Fix:** either publish them or eliminate all dependence on them.

- **P1A-M48 — p.21 Ref. [5]** — The entry is a 2025 arXiv preprint dated **2509.13654**, which is a future arXiv identifier relative to the paper date of June 8, 2026? Actually this is not future-dated relative to the manuscript date, but it is still a preprint-only citation for a precise quantitative claim. **Fix:** verify the manuscript’s date and, if needed, cite the published version if one exists.

- **P1A-M49 — p.21 Ref. ** — The citation is to **arXiv:2603.13924**, which is future-dated relative to the manuscript date if the manuscript is June 8, 2026 and the arXiv submission is March 2026, so this is not future-dated; however the paper still uses it as if it is already established literature. **Fix:** ensure the paper date and reference date are consistent everywhere.

- **P1A-M50 — p.22 Ref. ** — The note appended to the citation contains editorial prose: “**Used in P1A Sec. VI to point readers to the bounce-class alternative DE mechanism that survives the 14 ECH-specific structural barriers**.” That is manuscript-internal commentary, not bibliographic metadata. **Fix:** remove all such notes from the reference list.

- **P1A-M51 — p.23 Ref. ** — The final reference line is truncated: “**H. Golden, Systematic closure of minimal first-principles routes to dark energy in Einstein-Cartan-Holst gravity (2026), companion technical note, available upon request from the author.**” This is not a proper citable reference. **Fix:** complete the bibliographic entry or delete it.

- **P1A-M52 — throughout** — The manuscript repeatedly references “**companion work in preparation**,” “**Paper I(b)**,” “**Paper II**,” “**Paper III**,” and “**Paper IV**” as if they are established parts of the literature. They are internal project placeholders. **Fix:** remove them from the main scientific argument.

- **P1A-M53 — throughout** — The paper uses several phrases that read like internal draft notes: “**scope and limitations**,” “**bookkeeping**,” “**reparameterization**,” “**companion internal MCMC analysis**,” “**frozen accepted samples**,” and “**not yet converged**,” sometimes in sections that should contain final results. **Fix:** strip all draft-status language from the body.

- **P1A-M54 — throughout** — The paper makes repeated novelty claims such as “**no prior work assembles these into a single quantitative framework**” and “**the first-principles theorem**” without establishing a literature survey sufficient to support “no prior work.” **Fix:** either document the novelty rigorously or soften the claim.

- **P1A-M55 — throughout** — There are numerous places where the paper states a quantity is “**fitted**,” “**assumed**,” “**phenomenological**,” or “**bookkeeping**” and then later uses it as if it were derived. This is a core logical inconsistency. **Fix:** enforce a strict distinction between derived results and assumptions.

- **P1A-M56 — throughout** — The paper is too long for the claimed contribution. A channel-level no-go with perturbation transparency, bibliography audit issues, and companion-paper placeholders should be substantially shorter. **Recommended maximum length:** about **12–15 pages** excluding references and appendices. **Fix:** cut auxiliary speculation, repeated caveats, and all unpublished companion dependence.

## Summary recommendation
**REJECT**

The manuscript does not meet PRD standards in its current form because the central claims are repeatedly weakened or contradicted by the text itself, the numerical results are not consistently derived, the bibliography relies heavily on unpublished companion works and internal identifiers, and the paper conflates a limited channel-level argument with a much stronger theorem-like closure claim. Before resubmission, the authors would need to remove internal draft language, publish or eliminate all companion dependencies, reconcile the inconsistent e-fold and σ statements, and present a much narrower, fully reproducible result set.

---

## PASS 2 — self-critique findings (what initial review missed)

P1A-E6 — Abstract / p.1, DESI significance numbers  
The abstract and Introduction quote “DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ (dataset-dependent).” This σ-range is not recomputed or traced to any explicit test statistic or dataset definition in the body; the DESI DR2 reference  is later described as “DESI DR2 results II: … cosmological constraints” without stating which combination of probes yields 3.1σ vs 4.2σ or under what null. There is no in‑text calculation or row in any table demonstrating those values.  
**Fix:** Either (i) quote a specific DESI DR2 w₀–wₐ fit with its test statistic and confidence, or (ii) soften to a qualitative statement (“reports evidence for dynamical dark energy”) with an explicit citation, removing the unsupported 3.1–4.2σ range.

P1A-M57 — Eq. (11) and Dinf definition (dimensional / numerical consistency)  
Eq. (11) defines \(D_{\rm inf} = \exp[-3N_{\rm tot}] \times (T_{\rm reh}/M_{\rm GUT})^{3/2}\). Later, Appendix B states “Ξ ≈ 10⁻¹²³, decomposed as 10⁻² × Dinf with Dinf ∼ 10⁻¹²¹,” and that “Dinf ∼ e⁻³Ntot.” For Ntot ≈ 92 used throughout, \(\exp[-3N_{\rm tot}] \approx \exp(-276) \approx 10^{-120}\), not 10⁻¹²¹, and multiplying by \((T_{\rm reh}/M_{\rm GUT})^{3/2} ≈ 0.03\) gives \(D_{\rm inf} \sim 3\times10^{-122}\), not 10⁻¹²¹. This discrepancy propagates into the statement that the hierarchy is reduced from 10¹²² to “∼10⁵” of sensitivity to ΔNtot; numerically, a three‑e‑fold change changes Dinf by ~e⁻⁹ ~ 10⁻⁴, not five orders of magnitude.  
**Fix:** Recompute Dinf and Ξ consistently (including the Treh/MGUT prefactor), state the correct order of magnitude, and correct the “10⁻¹²¹” and “10⁵” sensitivity claims accordingly.

P1A-M58 — Eq. (20) gravitational-wave ceiling vs. quoted numerical range  
Barrier 12 gives \(\Omega^{\rm ECH}_{\rm GW}|_{\rm bounce} \lesssim (\rho_{\rm crit}/\rho_{\rm Pl})^2\) and then says this is “≃ 0.07–0.17,” using \(\rho_{\rm crit}/\rho_{\rm Pl} ≃ 0.27–0.41\). Squaring 0.27 and 0.41 gives ~0.073 and ~0.168, so the numbers are arithmetically consistent. However, elsewhere ρcrit/ρPl is also associated with values derived for different γ (0.2375 and 0.274), and Appendix B acknowledges ambiguity between “0.27–0.41” and a “0.41” canonical value. The ceiling is then discussed as if it were sharp to two significant figures.  
**Fix:** Explicitly state that the 0.07–0.17 range is just the square of the adopted 0.27–0.41 window and is itself scheme‑dependent at the 30–40% level; avoid using this bound later as if it were a precise numerical constraint.

P1A-M59 — Eq. (15) one-loop Route‑2 ratio: inconsistent dimensional reduction narrative  
In the Route‑2 discussion, the dimensionless ratio \(\Delta\theta_{\rm one–loop}/\Delta\theta_{\rm obs}\) is claimed to be “∼10⁻⁵⁸ to 10⁻⁶⁰,” with an “alternative ordering” giving a “∼10⁻³³ ratio.” The text attributes the enormous spread solely to “ε‑correction perturbative‑order scaling,” but the difference between 10⁻³³ and 10⁻⁶⁰ is 27 orders of magnitude—far larger than any order‑one or αem/4π ambiguity and incompatible with a unique EFT estimate. No explicit algebra is shown to justify either 10⁻³³ or 10⁻⁶⁰, and the claim that “the eV‑vs‑GeV unit conversion is exact and is not a source of ambiguity” is not backed up by a transparent check.  
**Fix:** Present the full step‑by‑step conversion from the one‑loop operator to the rotation angle, including all uses of H₀, MPl, and α/M in consistent units, and remove any alternative estimate that cannot be reproduced to within a factor ~few. If genuine scheme dependence can span 27 orders of magnitude, the route must be downgraded to “uncontrolled” rather than “firmly amplitude‑suppressed.”

P1A-M60 — Eq. (17) spectator-ALP energy density arithmetic  
Route 4 inverts the birefringence formula to claim that for α/M = 10⁻²¹ GeV⁻¹, β ≈ 6×10⁻³ rad, and mθ ≈ 1.5×10⁻³³ eV, the resulting ρθ is “≈ 2.8×10⁻¹¹ eV⁴ ≈ ρΛ to within a factor of unity.” Using \(ρ_\Lambda \sim (2.3\ {\rm meV})^4 \approx 2.8\times10^{-11}\ {\rm eV}^4\) this is numerically consistent, but the derivation silently assumes a specific normalization for ρθ (e.g. averaging over oscillations and taking θi∼O(1)) without showing the intermediate steps.  
**Fix:** Explicitly display the intermediate calculation for ρθ from β, including any factors of 1/2 or angular averaging, and confirm that the numerical equality with ρΛ is not an artefact of dropped O(1) constants.

P1A-M61 — Overshoot factors “22–36 OOM” vs. quoted mass range  
The text states that for the “natural ALP range (10⁻²²–10⁻¹⁵ eV) the produced ρθ ∝ mθ² overshoots ρΛ … bounded below by … ∼22 OOM at mθ ∼ 10⁻²² eV and grows to ∼36 OOM at … 10⁻¹⁵ eV.” Given that the tuned value is mθ ≃ H₀ ≃ 1.5×10⁻³³ eV, the mass ratios are mθ/H₀ ≃ 10¹¹ at 10⁻²² eV and ≃10¹⁸ at 10⁻¹⁵ eV, so (mθ/H₀)² ≃10²² and 10³⁶ respectively. Those are the correct overshoot *factors*, but calling them “22–36 orders of magnitude” in ρ is only correct if the tuned point itself is taken as ρΛ; since earlier the hierarchy relative to MPl⁴ is 10¹²², these overshoot factors are numerically correct but conceptually conflated with the CC hierarchy.  
**Fix:** Clarify that “overshoot by 22–36 orders of magnitude *relative to ρΛ*” means a multiplicative factor of 10²²–10³⁶ in ρθ compared to the tuned ρΛ value, and separate this clearly from the 10¹²² Planck‑to‑Λ hierarchy discussed in Appendix B.

P1A-M62 — σ-scaling and “3–5σ realistic” in Table I footnote vs. later text  
Table I footnote (b) describes “3–5σ realistic after full systematic budget” for fNL, starting from a raw Fisher σ(fNL) ≈ 0.7 (|fNL|/σ ~ 6.25σ) and then degrading to σ ≈ 1.0 after “GR‑projection and photo‑z marginalization,” implying significance ~4.4σ. Later, Sec. VII repeats “3–5σ realistic” but also mentions “∼5–5.5σ optimistic after template-overlap correction r ≈ 0.84,” and Sec. XIII describes SPHEREx as giving “3–5σ realistic significance” with σ(fNL) ≈ 0.7–1.0. There is no single consistent chain laid out that explains when the effective σ lands at 3σ vs 5σ; the same inputs are rhetorically pushed to different headline ranges depending on context.  
**Fix:** Choose one propagation chain (Fisher → template overlap → GR projection → photo‑z) and publish a single table or equation where each step’s σ(fNL) and significance is computed. Use that one set of numbers consistently throughout the paper.

P1A-M63 — β forecast: 9σ vs 0.73σ discrimination (null comparability)  
Sec. XIII says LiteBIRD will “detect non-zero β at ∼9σ (0.27°/0.03° overall sensitivity number)” but also that it can only distinguish β=0.27° from the current central value 0.342° at ~0.73σ using \(|0.342-0.27|/\sqrt{0.03^2+0.094^2}\). The paper correctly notes that these use different null hypotheses (zero vs current central), but this distinction is scattered between Sec. XIII and earlier text; in several places LiteBIRD’s “decisive (≳5σ)” power is described without restating that it is only “decisive” against β=0, not against the current βobs.  
**Fix:** Whenever the 9σ detection number is quoted, immediately state “relative to β=0” and, in the same sentence or a nearby one, explicitly state the 0.73σ discrimination vs current central βobs, to avoid readers misinterpreting 9σ as model‑discrimination power.

P1A-M64 — Table III entries labeled “not tested” vs. text implying quantitative comparison  
Table III uses “✓/×/—/not tested” to summarize discrimination among bounce and inflation models. The legend says “— denotes not applicable or not computed,” and the footnote emphasizes that w₀wₐ chains are not converged. However, the body text around Sec. XII–XIV occasionally refers to Quintom‑B as “accommodating the DESI w₀wₐ evidence” and describes the table as showing “discrimination among bouncing cosmologies and inflation by observable channels,” which implies more quantitative support than “not tested‡” actually provides.  
**Fix:** Rephrase the discussion of Table III explicitly as “qualitative model‑accommodation summary” and emphasize that rows marked “not tested‡” are purely theoretical plausibility statements, not the result of any quantitative fit in this program.

P1A-M65 — Internal consistency of Ntot ≈ 92 vs ≈ 94 (abstract vs Appendix B)  
The abstract and Sec. I highlight a specific value “Ntot ≈ 92 post‑bounce e‑folds” as required to match ρΛ. Appendix B then explicitly derives Ntot ≈ 94 from the genuine MPl⁴/ρΛ hierarchy and says the 92 vs 94 difference is an “∼2% level” offset from the ansatz choice. The main text nevertheless continues to use 92 as if it were the unique value, including in the structural‑tension argument against fNL.  
**Fix:** Either (i) pick one canonical value (e.g. 93±1) derived from a single transparent chain and use it consistently, or (ii) present Ntot as a range with an explicit ± uncertainty driven by the ansatz choice and propagate that uncertainty into the structural‑tension and “fine‑tuning reduction” discussion.

P1A-M66 — Barrier classification (novel vs known) without quantitative support  
Sec. IX classifies Barriers 1, 2, 3, 4, 8, 10, 11, 12, 14 as “Novel results” and Barriers 5, 6, 7, 9 as “Known results,” then states “No prior work assembles these into a single quantitative framework with systematic barrier testing.” There is no literature-based comparison or explicit demonstration that, for example, Barrier 4 or 12 goes beyond existing Planck‑suppression arguments or GW energy‑budget ceiling estimates; “novel” is asserted, not shown.  
**Fix:** Either remove the “Novel results / Known results” labeling, or add explicit references and comparative discussion showing that each “novel” barrier represents a genuinely new derivation or combination not present in prior ECH/torsion or bounce literature.

If you want, I can next go through each displayed equation and explicitly tabulate its left‑ vs right‑hand dimensions and any missing factors; that tends to uncover a few more subtle inconsistencies.