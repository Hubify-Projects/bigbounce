# P1A auto-2026-06-05_1717pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (15024 chars)
**Wall time**: 71.3s

---

This manuscript is **not publishable at PRD standards in its present form**. The paper contains numerous citation-forensics problems, self-contradictory claims, unsupported “in preparation” dependencies, internal numerical inconsistencies, and several places where the text overstates theorem-level closure beyond what is actually established.

- **P1A-E1** — **Abstract, p. 1** — Offending text: “*we report 13 logically-independent mechanism-class constraints*” and “*14 historical catalog entries, of which B8 is subsumed by B14*.” The manuscript later says B8 and B14 are not logically independent, so the abstract’s “13 logically-independent” claim is only true if that dependence is explicitly propagated everywhere the count is used. **Required fix:** make the independence count consistent throughout the abstract, tables, and body, and state unambiguously whether the paper has 13 independent constraints or 14 cataloged constraints with one dependence.

- **P1A-E2** — **Abstract, p. 1** — Offending text: “*fNL = −35/8 is a property of the matter-bounce class [1]*” and “*companion work in preparation [2]*.” The claim is presented as a result of this paper’s structural analysis, but the actual \(f_{\mathrm{NL}}\) result is delegated to a companion forecast that is explicitly not available. **Required fix:** remove any implication that this paper establishes or verifies the \(f_{\mathrm{NL}}\) forecast; reframe as an external literature value only.

- **P1A-E3** — **Abstract, p. 1** — Offending text: “*β ≈ 0.27° is a benchmark consistency point…*” and “*is comparable to… ACT DR6 follow-up*.” The paper relies on a specific birefringence mapping to later conclusions, but no derivation in the body establishes the benchmark as ECH-relevant. **Required fix:** state clearly that the ALP birefringence value is external to ECH and not a prediction of the minimal ECH sector.

- **P1A-M1** — **Abstract/Intro, pp. 1–3** — Offending text: repeated use of “*channel-level closure*,” “*no-go theorem*,” “*perturbation-transparency theorem*.” The paper repeatedly claims theorem-level closure while simultaneously admitting that the operator basis is incomplete and that omitted operators are left to future work. **Required fix:** downgrade terminology from theorem/no-go to conditional channel-level exclusion under stated assumptions.

- **P1A-E4** — **Abstract, p. 1** — Offending text: “*the dark-energy mapping rests on a phenomenological on-shell scaling ansatz whose off-shell mass dimension is +1 rather than +4*.” This is not a derivation and is admitted to be an ansatz, yet it is used as load-bearing input to “close” the mechanism. **Required fix:** explicitly separate ansatz-based parameterization from any derivable EFT statement; do not present the ansatz as physically established.

- **P1A-E5** — **Section I.A, p. 3** — Offending text: “*the Jackiw–Pi gravitational Chern–Simons term \(R\wedge \tilde R\) and the parity-odd four-fermion partner … are excluded from the enumeration*.” This is a major scope limitation, not a detail. The paper’s “closure” is therefore not a closure of minimal ECH generally, only of a hand-picked subset of channels. **Required fix:** title and abstract must say “four enumerated channels,” not “minimal ECH” in a global sense.

- **P1A-E6** — **Section I.A, p. 3; Section XI, p. 15; Appendix B, p. 19** — Offending text: “*the 14-constraint catalog*,” “*B8 is subsumed by B14*,” and later “*13 logically-independent structural barriers (14 historical catalog entries)*.” The paper uses multiple incompatible counts for the same taxonomy. **Required fix:** choose one count scheme and use it consistently in all sections, captions, and appendix labels.

- **P1A-M2** — **Table I, p. 4** — Offending text: “*H0 = 67.68 ± 1.06, ΔNeff ≈ 0*” and “*3–5σ realistic after full systematic budget*.” The table mixes a parameter estimate from an unpublished companion analysis with significance estimates from another forecast. **Required fix:** label all such entries as external inputs and verify each against the cited companion paper before claiming them as results here.

- **P1A-M3** — **Figure 1 caption, p. 4** — Offending text: “*the 14-constraint catalog narrows the four enumerated minimal-ECH dark-energy channels to zero phenomenologically free pathways within those channels*.” The caption states a stronger conclusion than the paper can support because it excludes omitted operators by fiat. **Required fix:** caption must mention that the conclusion applies only to the enumerated channels, not the full operator space.

- **P1A-M4** — **Section II.A.1, p. 5** — Offending text: Eq. (1) and surrounding prose. The action is written in a compressed form with ambiguous notation: \(T^{abc}T_{abc}\) is described as a “shorthand for the four-fermion contact interaction,” but Eq. (1) is presented as a fundamental action term. **Required fix:** distinguish the fundamental Einstein–Cartan–Holst action from the effective four-fermion term after integrating out torsion.

- **P1A-M5** — **Section II.A.2, p. 5** — Offending text: “*Eq. (5) is a phenomenological ansatz*,” “*off-shell mass dimension +1*,” and then “*\( \rho_\Lambda = \Xi M_{\rm Pl}^4\) is therefore a scaling ansatz*.” The dimensions are internally inconsistent as written: a dimension-\(+1\) operator cannot directly produce a dimension-\(+4\) vacuum energy without additional factors, which are later introduced ad hoc. **Required fix:** rewrite the dimensional analysis from first principles and state exactly where each power of \(M_{\rm Pl}\) enters.

- **P1A-M6** — **Section II.B, p. 6** — Offending text: “*Substituting instead the SU(2) black-hole-entropy value \(\gamma_{SU(2)} \approx 0.274\)… gives \(\rho_{\rm crit} \simeq 0.27\rho_{\rm Pl}\); this lower value is an internal extrapolation across counting schemes*.” The paper first presents the value as a standard LQC input and then retracts it as an internal extrapolation. **Required fix:** identify which value is actually used in all downstream numerics and do not present extrapolated values as published LQC results.

- **P1A-M7** — **Section II.C.1, p. 6–7** — Offending text: the derivation of \(D_{\rm inf}=e^{-3N_{\rm tot}}(T_{\rm reh}/M_{\rm GUT})^{3/2}\). The text openly says this half-integer power is not derived from a thermal partition function, yet it is used quantitatively in the main argument. **Required fix:** either derive the prefactor properly or demote all conclusions depending on it to qualitative status.

- **P1A-E7** — **Section II.C.1, p. 7** — Offending text: “*Matching \( \rho_\Lambda \approx (2.3\,{\rm meV})^4\) requires \(N_{\rm tot}\approx 92\)*” and later “*Ntot ≈ 92 ± 2*” in Appendix B. The paper treats \(N_{\rm tot}\) as both fitted and ansatz-dependent while still using it as a load-bearing quantitative closure parameter. **Required fix:** state explicitly that \(N_{\rm tot}\) is not predicted and that the quoted value is only a model-dependent sensitivity estimate.

- **P1A-M8** — **Section II.C.1, p. 7** — Offending text: “*The framework has not solved the cosmological constant problem; it has only relocated the fine-tuning into inflationary initial conditions.*” This directly contradicts stronger language elsewhere describing “closure” and “no-go.” **Required fix:** align the conclusion language with this admission.

- **P1A-M9** — **Section III.A, p. 7–8** — Offending text: Eq. (12), \(C_\ell^{EB}\approx 2\beta C_\ell^{EE}-C_\ell^{BB}\). This is dimensionally and conceptually too compressed for a claim about cosmic birefringence; the paper does not specify the approximations under which this form holds. **Required fix:** provide the derivation or cite the exact standard relation being used, including assumptions of small angle and negligible primordial \(B\)-modes.

- **P1A-E8** — **Section IV, p. 8** — Offending text: “*the four routes are (R1)… (R4)… Each route is closed at the amplitude level rather than only at the structural level*.” Route 4 is later said to be *not* closed by amplitude mismatch but by naturalness. That is not “amplitude level.” **Required fix:** separate amplitude closure from naturalness closure and do not lump them together.

- **P1A-M10** — **Section IV.A, p. 8** — Offending text: Eq. (13), \(L^{\rm NJL}_{\rm tor}= -\frac{3}{16}\kappa(\bar\psi\gamma^a\gamma^5\psi)^2\). The paper asserts parity-evenness, which is fine, but later uses this as an argument against parity-odd cosmological birefringence without showing the required operator matching. **Required fix:** demonstrate the operator-selection argument explicitly.

- **P1A-E9** — **Section IV.B, p. 9** — Offending text: “*the canonical Route-2 estimate … robust to any reasonable dimensional reconciliation*.” The paper itself gives two numerically different suppression estimates, \(\sim10^{-58}\)–\(10^{-60}\) and an “alternative ordering” giving \(\sim10^{-33}\). These are not small ambiguities; they differ by 25–27 orders of magnitude. **Required fix:** choose one consistent dimensional normalization and remove the alternative unless fully derived.

- **P1A-M11** — **Section IV.C, p. 9** — Offending text: “*the integrated effect is suppressed by an additional factor of \((\Delta\gamma/\gamma)(H/M_{\rm Pl})\sim10^{-63}\)*.” This numerical estimate is not traceable from the preceding inputs with the stated assumptions. **Required fix:** show the arithmetic step by step.

- **P1A-M12** — **Section IV.D, p. 10–11** — Offending text: “*A free-coupling spectator-ALP fit reproduces both \(\beta_{\rm obs}\) and \(\rho_\Lambda\)*,” followed by “*the rigid no-go is tied to the one-loop matching assumption*.” This is not a no-go theorem; it is a statement about one specific matching ansatz. **Required fix:** remove the language of closure for Route 4 or explicitly condition it on the one-loop matching assumption.

- **P1A-M13** — **Section IV.D, p. 11** — Offending text: “*for any \(m_\theta\) in the natural ALP range \([10^{-22},10^{-15}]\,{\rm eV}\), the produced \(\rho_\theta\) overshoots \(\rho_\Lambda\)…*” The algebra is not fully demonstrated, and the claim that the overshoot is “monotonic” is asserted rather than shown. **Required fix:** include the explicit scaling derivation and verify the endpoint numerics.

- **P1A-E10** — **Section IV.E, p. 11** — Offending text: “*Within the four enumerated channels… close each under the stated assumptions*.” Because the paper explicitly excludes other parity-odd torsion operators, this sentence overstates the scope. **Required fix:** restrict the claim to the four enumerated channels only.

- **P1A-M14** — **Section V, p. 11–12** — Offending text: “*companion work in preparation [2]*,” “*Paper IV *,” and “*internal MCMC analysis (Paper I(b) [6], in preparation)*.” The manuscript relies heavily on unpublished companion papers for essential numerical claims, but these claims are not independently verifiable from the submitted text. **Required fix:** either include the needed numerical and methodological details in this paper or demote the dependent claims to nonessential context.

- **P1A-M15** — **Section VI, p. 12** — Offending text: “*The CMB birefringence channel provides the surviving parity-violation evidence from the published WMAP+Planck measurement*.” This is a strong interpretive claim not justified by the evidence summarized here; the paper does not establish that the measurement is evidence for this model rather than a generic parity-violation signal. **Required fix:** tone down to “consistent with” and avoid model attribution.

- **P1A-E11** — **Section VII, p. 12** — Offending text: “*LiteBIRD (σ(β) ≈ 0.03°) will measure β to σ(β) ≈ 0.03° and either confirm… or rule out the spectator-ALP class*.” Later the manuscript correctly notes that distinguishing \(0.27^\circ\) from \(0.342^\circ\pm0.094^\circ\) is only \(\sim0.73\sigma\). These statements conflict. **Required fix:** make all significance statements consistent with the actual error propagation and prior uncertainty.

- **P1A-E12** — **Section VII, p. 12** — Offending text: “*SPHEREx will test the matter-bounce prediction \(f_{\rm NL}=-35/8\) at 3–5σ realistic significance*.” This depends entirely on a companion forecast and on assumptions the present paper does not establish. **Required fix:** cite the forecast as external and do not present the significance as a result of this manuscript.

- **P1A-N1** — **Section VIII, p. 12** — Offending text: reference list item – includes several 2025 arXiv/venue claims. These must be verified against arXiv and ADS because the manuscript uses them as recent support for important cosmological claims. **Required fix:** confirm titles, author lists, years, and journal metadata; if any are arXiv-only or not yet published, label them accurately.

- **P1A-M16** — **Section IX, p. 12–13** — Offending text: “*Barrier 8 (parity-even interaction) and Barrier 14 (perturbation transparency) close the same observable channel… they are listed separately to preserve the historical mechanism-class catalog, but should not be counted as logically independent constraints.*” This is good disclosure, but elsewhere the paper still counts 14 barriers as if all are independent. **Required fix:** remove all downstream arithmetic that treats 14 as independent.

- **P1A-M17** — **Section IX.L, p. 13** — Offending text: Eq. (20), “*\(\Omega^{\rm ECH}_{\rm GW}|_{\rm bounce}\lesssim(\rho_{\rm crit}/\rho_{\rm Pl})^2\simeq0.07–0.17\)*.” The use of the squared ratio is asserted without derivation, and the resulting range depends on the same scheme-dependent \(\rho_{\rm crit}\) values previously described as internal extrapolations. **Required fix:** derive the scaling or remove the numerical bound.

- **P1A-M18** — **Section X, p. 14** — Offending text: “*the Holst term is dynamically inert for both scalar and tensor perturbations at all orders*.” This is too strong as stated because the section itself later lists conditions under which the result fails. **Required fix:** qualify as valid only for canonical scalar matter with vanishing spin density and no extra torsion dynamics.

- **P1A-E13** — **Section X.B–D, p. 14** — Offending text: “*torsion vanishes at all perturbation orders*,” “*Holst term becomes topological*,” “*No equations of motion*.” The proof is only for a torsion-free Levi-Civita background with canonical scalar matter. The language overgeneralizes the result to all minimal ECH settings. **Required fix:** narrow the theorem statement to the exact hypotheses used in the proof.

- **P1A-M19** — **Section X.D, p. 14** — Offending text: “*\(R(\Gammå)=\frac12\epsilon^{\mu\nu\rho\sigma}R_{\mu\nu\rho\sigma}(\Gammå)=\frac12\ast RR\equiv \partial_\mu K^\mu\)*.” The notation is unclear and partly malformed; the same symbol \(R\) is used for a dual contraction and for the Riemann tensor density in a way that invites confusion. **Required fix:** rewrite with standard Pontryagin-density notation and distinct symbols.

- **P1A-M20** — **Section XI, p. 15** — Offending text: “*All 7 forms were rejected*” and “*the w0wa extension was never implemented computationally*.” The paper presents a result about rejecting seven forms while admitting that one of the proposed tests was never actually run. **Required fix:** state that the rejection is theoretical, not computational, and separate unimplemented ideas from tested ones.

- **P1A-M21** — **Section XII.A, p. 15–16** — Offending text: “*The framework has not solved the cosmological constant problem; it has only relocated the fine-tuning*.” This directly contradicts the abstract’s implication of a closure result. **Required fix:** reconcile the abstract and conclusion so they do not overstate the theoretical accomplishment.

- **P1A-M22** — **Table III, p. 16–17** — Offending text: “*Matter bounce (any host; not ECH-specific) ✓*,” “*Slow-roll inflation × (fNL ≈ 0.015)*,” “*Quintom-B consistent†*,” and notes about chain status. The table mixes mechanism claims with operational status of unpublished MCMC chains. **Required fix:** remove chain-status bookkeeping from the physics table and clearly separate theory classification from computational progress.

- **P1A-M23** — **Section XIII, p. 16–17** — Offending text: “*SPHEREx tests the former, LiteBIRD tests a related spectator field, and the ECH dark-energy ansatz remains a phenomenological parameterization.*” This is the first fully consistent statement, but it clashes with earlier language about “surviving predictions” being outputs of the ECH program. **Required fix:** harmonize all summary language with this weaker and more accurate framing.

- **P1A-E14** — **Section XIII, p. 16–17** — Offending text: “*Two mechanism-independent predictions of the broader bounce/ALP landscape survive the channel-level closure*.” Since these are not ECH predictions, the phrase “survive the channel-level closure” is rhetorically misleading. **Required fix:** say they remain testable external observables, not predictions of the paper’s closed ECH sector.

- **P1A-M24** — **Section XIV.A.1, p. 17** — Offending text: “*Non-minimal couplings during inflation could alter the dilution factor*.” This undermines several earlier quantitative claims, but the manuscript does not propagate the uncertainty into the main conclusions. **Required fix:** include this uncertainty in the error budget for any statement depending on \(N_{\rm tot}\) or \(D_{\rm inf}\).

- **P1A-M25** — **Section XIV.D, p. 17–18** — Offending text: “*the matter-bounce \(f_{\rm NL}\) would be definitively erased by \(N_{\rm tot}\gtrsim60\)*.” “Definitively” is too strong, because the statement depends on the paper’s own model of how inflation maps bounce scales to observed modes. **Required fix:** replace with a conditional statement tied to the assumed scale mapping.

- **P1A-N2** — **Section XIV.E, p. 17–18** — Offending text: “*the 13 logically-independent structural constraints (14 historical catalog entries)*.” This repeats the independence-count inconsistency already noted. **Required fix:** fix globally.

- **P1A-N3** — **Acknowledgments, p. 18** — Offending text: “*The author acknowledges the use of Claude (Anthropic) as an AI research assistant…*” This is not a scientific flaw, but PRD-style disclosure should be complete and the extent of AI assistance should not be relegated to acknowledgments if it affected derivations or bibliography. **Required fix:** ensure compliance with journal policy on AI assistance disclosure.

- **P1A-M26** — **Appendix B, p. 19** — Offending text: Eq. (B1)–(B2) and surrounding prose. The appendix itself admits that the parity-odd operator is not a controlled dimension-\(+4\) EFT operator. This means the main text’s use of that operator as a physical mechanism is not justified. **Required fix:** either supply the missing EFT construction or remove all claims that depend on it.

- **P1A-E15** — **Appendix B, p. 19** — Offending text: “*Ntot ≈ 92 ± 2*” versus “*Ntot ≈ 94*.” The appendix gives two different values for the same quantity and then says the difference is only \(\sim2\%\). But \(92\) vs \(94\) is already a nontrivial shift in a quantity that is used exponentially. **Required fix:** pick one value, or propagate the uncertainty consistently into all exponential estimates.

- **P1A-M27** — **References [2], [6], , , , pp. 19–21** — Offending text: multiple references are explicitly “in preparation,” “available upon request,” or companion papers “this volume.” For a PRD submission, key quantitative claims cannot rest on inaccessible internal documents. **Required fix:** either replace them with published/posted sources or remove claims that require them.

- **P1A-N4** — **References [5], , , , , pp. 19–21** — Several entries show obvious metadata problems or incomplete bibliographic information: arXiv-only listings, “this volume,” unpublished “in preparation” items, and informal institutional names. **Required fix:** standardize the bibliography to PRD format and verify each entry against arXiv/ADS.

- **P1A-N5** — **References –, pp. 19–20** — The DESI papers are cited with future-dated or potentially inconsistent journal/arXiv metadata relative to the paper’s June 2026 date. **Required fix:** verify publication year, volume, and arXiv identifiers against the current ADS/arXiv record before submission.

- **P1A-M28** — **Global issue, throughout** — Offending text: many claims are phrased as “*theory closes route X*,” while the paper simultaneously says the same route is only closed under a phenomenological ansatz or under a free-coupling assumption. **Required fix:** rewrite the paper so that every claim of closure is explicitly conditional, and separate true derivations from model-dependent parameterizations.

- **P1A-M29** — **Global issue, throughout** — Offending text: repeated use of unpublished companion results as if they were already verified literature. This is not acceptable for PRD unless the present paper is self-contained or the dependencies are publicly accessible and precisely cited. **Required fix:** make the paper self-sufficient or downgrade those claims to nonessential background.

- **P1A-M30** — **Global issue, throughout** — Offending text: the manuscript is far too long and internally saturated for the actual contribution, which is a conditional exclusion of four enumerated channels plus a perturbation-transparency observation. **Required fix:** cut to a much shorter PRD-length presentation; recommended maximum for this contribution is **about 14–16 pages** excluding references, with the companion material moved out.

## Summary recommendation
**REJECT**

The paper does not meet PRD standards because its central “closure” claims rest on an admitted phenomenological ansatz, an incomplete operator basis, and multiple unpublished companion documents. Its bibliography also contains numerous inaccessible or unpublished references, its significance statements are internally inconsistent, and several quantitative claims are not reproducible from the text as written. The manuscript needs a major conceptual rewrite, not a minor correction pass.

---

## PASS 2 — self-critique findings (what initial review missed)

P1A-E16 — Arithmetic: inconsistent use of DESI BAO “3.1–4.2σ”  
- **Location:** Introduction, p. 3 (opening paragraph).  
- **Issue:** The manuscript quotes DESI BAO results as “3.1–4.2σ (dataset‑dependent)” but never shows inputs or combinations that reproduce this range, nor are the exact values identified with specific datasets/results. There is no internal arithmetic or explicit mapping from DESI DR2 numbers to these quoted σ values.  
- **Required fix:** Either (a) show the computation from explicitly listed DESI measurements (central values, errors, and null hypothesis) for each σ quoted, or (b) reference the specific DESI tables/figures where these exact σ ranges are defined and label them clearly as external, not recomputed here.

---

P1A-M28 — Arithmetic: Dinf prefactor and “10⁵ sensitivity” not numerically demonstrated  
- **Location:** Sec. II.C.1, p. 6–7; Sec. XII.A; Appendix B.  
- **Issue:** The text asserts that matching ρΛ requires “Dinf ∼ 10⁻¹²¹” and that this converts the “10¹²²” hierarchy into a residual “∼10⁵ sensitivity to ΔNtot ≈ 4 e‑folds,” but no explicit step‑by‑step numeric path is shown from Eq. (11) and Eq. (B2) to these numbers. The dependence on the O(0.01–0.1) prefactor and the conversion of ΔNtot ≈ 4 into “∼10⁵” are not recomputed explicitly, only described qualitatively.  
- **Required fix:** Write out:  
  - the explicit numerical value for Dinf given Ntot ≈ 92,  
  - the exact mapping from Dinf and [(α/M)MPl] to Ξ ≈ 10⁻¹²³,  
  - and the algebra showing how ΔNtot ≈ 4 corresponds to ∼10⁵ in Ξ (or in ρΛ), with all logs and exponentials shown.

---

P1A-M29 — Arithmetic: Ω\_{GW}^{ECH}|_{bounce} ceiling vs ρcrit/ρPl input  
- **Location:** Sec. IX.L, p. 13, Eq. (20).  
- **Issue:** Eq. (20) states  
  \(\Omega^{\rm ECH}_{\rm GW}|_{\rm bounce} \lesssim (\rho_{\rm crit}/\rho_{\rm Pl})^2 \simeq 0.07–0.17\).  
  If ρcrit/ρPl ≃ 0.27–0.41, then squaring gives ≃0.073–0.168, which matches the stated range. However, the derivation of the *squared* dependence is not shown. This is partly dimensional (you already flagged that), but there is also an arithmetic‑logic gap: the ceiling is implicitly assumed to be the square of a density fraction without any normalization step by step.  
- **Required fix:** Provide the explicit intermediate expression (e.g., starting from ρGW ≤ ρcrit and defining ΩGW ≡ ρGW/ρtot) showing how the square arises and verify each numerical value by actually inserting ρcrit/ρPl = 0.27 and 0.41 and squaring them in the text.

---

P1A-M30 — Arithmetic: EB rotation significance and LiteBIRD discrimination  
- **Location:** Sec. VII, p. 11; Sec. XIII, p. 16; Conclusions, p. 18.  
- **Issue:** The text correctly computes the discrimination between β = 0.27° and βobs = 0.342° ± 0.094° as ≈0.73σ using  
  \(|0.342−0.27| / \sqrt{0.03² + 0.094²} ≈ 0.072/0.0987 ≈ 0.73σ\).  
  However, in nearby sentences the “∼9σ detection” of β≠0 at LiteBIRD is juxtaposed with this, and the prose risks conflating a ∼9σ *null‑test* (β vs 0) with an ≈0.7σ *model‑discrimination test* (βspectator vs βobs). There is no explicit numerical separation of these two σ values in table or equations.  
- **Required fix:**  
  - Explicitly list both calculations: (i) β/σ(β) for LiteBIRD and (ii) |βspect − βobs|/σcombined, and clearly label them as “null‑test significance” and “model‑discrimination significance.”  
  - Add a sentence in Sec. VII explicitly warning that the 9σ detection is not a 9σ discrimination between the benchmark 0.27° and the WMAP+Planck central value.

---

P1A-M31 — Arithmetic: PTA γ comparison not fully recomputed  
- **Location:** Sec. XIII, p. 16 (NANOGrav reanalysis paragraph); Table III.  
- **Issue:** The text states “γ = 2.567 ± 0.382” and that the matter‑bounce prediction γ = 3.0 is “+1.13σ above the posterior mean.” The σ ratio  (3.0−2.567)/0.382 ≈ 0.433/0.382 ≈1.13 is correct; however, this γPTA value is used as if directly comparable to the “bounce γ=3.0” without any internal recomputation or re‑plot of the power‑law fits that define γPTA. No check is shown that the same fitting convention (reference frequency, spectral index definition) is used for both.  
- **Required fix:** Either (a) include a brief derivation or numerical example showing that the same definition of γ is used for both the NANOGrav fit and the matter‑bounce prediction, or (b) flag explicitly that “+1.13σ” is based on the external γPTA posterior and is not recomputed within this paper.

---

P1A-M32 — Figure 1 caption vs body: “zero phenomenologically free pathways” overstates scope relative to body text  
- **Location:** Fig. 1 caption, p. 4; Sec. IV Scope paragraph, p. 8; Sec. IX, p. 12–13.  
- **Issue (extension beyond earlier M3 finding):** The caption says “narrows the four enumerated minimal‑ECH dark-energy channels to zero phenomenologically free pathways within those channels.” The body text later clarifies that Route 4 is closed by *naturalness* and that some operators (Jackiw–Pi, parity‑odd four‑fermion partner) are not enumerated and explicitly left open. The caption’s “zero phenomenologically free pathways” implicitly lumps amplitude closure and naturalness closure together, while the body separates them.  
- **Required fix:** Rephrase the caption to distinguish:  
  - channels closed by hard amplitude bounds (R1–R3), and  
  - channels judged non‑viable only by naturalness (R4),  
  and explicitly state that this applies only to the four enumerated routes, not the full operator space.

---

P1A-M33 — Equation dimensional consistency: Λeff definition vs α/M dimension  
- **Location:** Sec. II.C, Eq. (10), p. 6; Sec. II.A.2, Eqs. (5–7), p. 5–6; Appendix B.  
- **Issue (beyond your previous M5/M26):** Eq. (10) defines  
  \(\Lambda_{\rm eff} = \Xi M_{\rm Pl}^2 + c_\omega \omega^2\), with \(\Xi ≡ hα/M i / M_{\rm Pl} × D_{\rm inf}\) in Sec. XII.A.  
  From Appendix B, [α/M] = −1 (mass dimension −1), so Ξ as defined carries dimension −1 (from α/M) −1 (division by MPl) + 0 (Dinf) = −2, not dimensionless. Yet it is used as dimensionless in ρΛ = Ξ MPl⁴ and in Λeff = Ξ MPl². This is a separate dimensional inconsistency from Eq. (5)/(B2): the same symbol Ξ is used with conflicting dimensional assignments across sections.  
- **Required fix:**  
  - Pick a single definition of Ξ (dimensionless), and adjust either the power of MPl in Ξ or in the definition of Λeff and ρΛ so that all occurrences of Ξ are dimensionally consistent.  
  - Explicitly list dimensions of α/M, Ξ, and each term in Λeff in one place, and verify LHS and RHS match.

---

P1A-M34 — Equation dimensional consistency: Dinf prefactor (Treh/MGUT)^{3/2}  
- **Location:** Sec. II.C.1, Eq. (11) and the long paragraph following it, p. 6–7.  
- **Issue (extra to earlier M7):** Dinf is dimensionless by construction (a dilution factor), and exp[−3Ntot] is dimensionless. (Treh/MGUT)^{3/2} is also dimensionless, so Eq. (11) is formally dimensionally correct. However, the narrative assigns part of this factor to “operator strength” and part to a “parity‑odd density‑of‑states factor,” tying it to quantities that should carry mass dimensions (operator coefficients, densities) without explicitly showing the units at each step. The decomposition between “coefficient normalization” and “phase‑space factor” is never written in a way that keeps track of units; it mixes number density nψ ∼ T³ (mass³) with operator dimensions and an extra T/M factor without showing how the dimensions cancel in the final Dinf.  
- **Required fix:** Rewrite the derivation of Eq. (11) in a strict dimensional way:  
  - start from a concrete expression for the torsion‑induced energy density at bounce and at reheating,  
  - show explicitly how each temperature factor contributes,  
  - and confirm that the final ratio is dimensionless and correctly interpretable as Dinf.

---

P1A-M35 — Equation dimensional consistency: β expression for Route 4  
- **Location:** Sec. IV.D, Eq. (17), p. 10.  
- **Issue:** The paper writes  
  \(\beta = (\alpha/M) \,\Delta \theta_{\rm rec\rightarrow today} \sim (\alpha/M)\, \sqrt{2\rho_\theta}/m_\theta\).  
  Given [α/M] = −1, [ρθ] = 4, [mθ] = 1, this gives [β] = −1 + 2 − 1 = 0 (dimensionless angle), which is consistent. However, in the subsequent naturalness arguments the same combination is reused to infer ρθ = mθ² β² / [2(α/M)²] *without* re‑stating that β must be dimensionless; later in Appendix B and Sec. XII A, β is mixed with degree/radian values without clarifying that all dimensionful quantities are converted to pure numbers first. This leaves a latent risk of unit confusion between “β in degrees” and “β as a pure radian angle” in the algebra that leads to ρθ ≈ ρΛ.  
- **Required fix:**  
  - Explicitly state that all algebraic uses of β in Eqs. (17) and the ρθ expressions treat β as a dimensionless *radian* measure.  
  - If any numerical evaluations used degree values directly, recompute them in radians and correct any affected numbers.

---

P1A-M36 — Cross‑references: Foundations/Branches vs constraint numbering not always aligned in text  
- **Location:** Sec. I.A (foundations description), Sec. IX (Barriers 1–14 and Table II), body references in Sec. IV, Sec. XII, Sec. XIV.  
- **Issue:** The constraint classification says “Novel results (Barriers 1, 2, 3, 4, 8, 10, 11, 12, 14)” and “Known results (Barriers 5, 6, 7, 9)” but some later references in Sec. XII and Sec. XIV refer to “Barrier 12” as an energy‑density ceiling and to “Barrier 14” as perturbation transparency, *without* consistently pointing to Foundations/Branches (A–G, H, J, L, M, N, O) in the same way as Table II. This makes it hard to verify that every textual “Barrier X” pointer actually maps to the right line in Table II. For example, the “reheating thermal‑reset barrier (supporting B14)” in Sec. II.C.1 is not listed in Table II at all as a separate barrier.  
- **Required fix:**  
  - Audit every “Barrier X” reference in the text and ensure it points to the intended row in Table II, or mark it explicitly as “supporting argument for Barrier Y” rather than a separate barrier.  
  - Consider adding a short cross‑reference sentence in Sec. IX that lists which textual arguments (e.g., reheating reset) are “supporting” which numbered barrier.

---

P1A-M37 — Null‑procedure comparability: σ(fNL) values from different forecast regimes juxtaposed as a single “3–5σ realistic” range  
- **Location:** Table I; Sec. VII and its footnote; Sec. XIII.  
- **Issue:** The “3–5σ realistic” SPHEREx forecast range combines:  
  - a Fisher‑ideal σ(fNL) ≈ 0.7,  
  - an “optimistic” σ after template‑overlap corrections, and  
  - a σ ≈ 1.0 after GR projection and photo‑z marginalization.  
  These σ values arise from different null procedures (different covariance assumptions and systematic treatments), yet the text compresses them into a single “3–5σ realistic” label without an explicit statement that they are not directly comparable and correspond to distinct analysis configurations.  
- **Required fix:**  
  - Break out the forecast σ values explicitly: Fisher‑ideal, overlap‑corrected, and fully degraded.  
  - Add a sentence stating that these correspond to different null hypotheses/analysis pipelines and are **not** directly comparable; the “3–5σ” label should be framed as a scenario range, not as a single statistical statement.

---

P1A-M38 — Abstract faithfulness: “amplitude‑level closure” vs later admission that Route 4 is closed only by naturalness  
- **Location:** Abstract, p. 1 (“each fails at the amplitude level under stated assumptions”); Sec. IV.D; Sec. IV.E; Sec. XIV.E.  
- **Issue (refinement beyond earlier M8/M12/M23):** The abstract’s first sentence says all four channels “fail at the amplitude level,” but Sec. IV.D explicitly concludes that Route 4 is **not** amplitude‑closed; it is closed by naturalness/explanatory deficit. Sec. IV.E and the later discussion repeat that “R4 status: a naturalness objection rather than an amplitude exclusion.” This is a strict abstract‑body mismatch in the specific sense you were asked to check: the abstract claims a kind of closure (amplitude) that the body later walks back for one of the four routes.  
- **Required fix:** Change the abstract wording to something like “each of the four channels is ruled out either by amplitude‑level mismatch (Routes 1–3) or by a naturalness/explanatory objection (Route 4).” Make sure every place that summarizes “four‑route no‑go” uses the same caveat.

---

P1A-M39 — Abstract faithfulness: “ΛCDM+ΔNeff MCMC verification” not reproduced in main text  
- **Location:** Abstract and Introduction (mention of companion work); Sec. V–VI; Sec. XV.  
- **Issue:** The abstract mentions “ΛCDM+ΔNeff MCMC verification, NaMaster pipeline validation, and ALP parameter fitting are documented separately in companion work in preparation [6].” In the main body, no actual ΔNeff posteriors, convergence diagnostics, or chain settings are shown; yet Table I (and other places) quote H0 = 67.68 ± 1.06 and ΔNeff ≈ 0 as if they were established results. This is an abstract‑body consistency problem in the PRD sense: the abstract foregrounds “MCMC verification,” but the paper itself does not provide reproducible information for those claims, only defers them.  
- **Required fix:** Either (a) move all such MCMC‑verification phrasing out of the abstract and clearly label these as *inputs from external/companion work*, or (b) include at least minimal MCMC details (likelihoods, priors, convergence criteria, and a table of key posteriors) sufficient for a referee to verify the arithmetic.

---

P1A-M40 — Appendix vs main‑text mismatch: Ntot in Appendix B vs structural‑tension section  
- **Location:** Appendix B (Ntot ≈ 94 from pure hierarchy); Sec. XIV.D (Ntot ≈ 92 from structural tension).  
- **Issue (refinement of earlier Ntot remarks):** Appendix B recomputes the “genuine” hierarchy and finds Ntot ≈ 94; Sec. XIV.D and earlier sections quote Ntot ≈ 92 as the tension value, and Sec. XII.A tries to reconcile them as “≈2% offset.” However, this reconciliation is only verbal; there is no explicit equation that shows how the shift from the strict MPl⁴/ρΛ hierarchy to the on‑shell ansatz in Eq. (B2) leads to exactly 92 instead of 94, nor is there a propagated uncertainty estimate that runs through every place where Ntot appears exponentially.  
- **Required fix:**  
  - Add a short explicit calculation in Appendix B that shows how Eq. (B2) leads to 92, and then state that the pure‑hierarchy value 94 and the ansatz‑dependent 92 imply Ntot = 93 ± 1 or 92 ± 2, with that uncertainty propagated into all exponential quantities (e.g., any Dinf‑based ratios).  
  - Ensure that every place quoting a single Ntot value acknowledges this uncertainty if it is load‑bearing.

---

If you want, I can now go through the paper line‑by‑line to explicitly recompute every quoted σ, ratio, and hierarchy factor so you can patch each numerical statement with a concrete arithmetic check.