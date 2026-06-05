# P1B R10v3p1 — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (15613 chars)
**Wall time**: 491.1s

---

# Referee Report: Technical Verification Companion to the ECH Spin-Torsion Program (P1B)

## Overall Assessment

This manuscript is presented as a "technical verification companion" to a structural no-go result, but the body explicitly admits that **none of the three analyses verifies the ECH spin-torsion sector**. The MCMC uses stock CAMB with no torsion modifications; the NaMaster work is pipeline validation, not a sky measurement; the ALP analysis is "not a distinctive ECH prediction." After scope deflation, the paper reports (a) a null result consistent with ΛCDM, (b) a pipeline self-recovery test, and (c) a consistency check with a model the authors themselves say arises identically in GR. That is not a PRD-grade contribution.

The paper also injects, mid-body, a large secondary DESI w₀w_a "quintom" claim (Table II, w₀+w_a = −1.48±0.15) that does not appear in the title or abstract, while the abstract itself emphasizes a null. This is a serious presentation failure: either the headline result is hidden, or a non-headline result is inflated. Either way, it is incoherent.

I recommend **REJECT** on first pass. Detailed findings below.

---

## ESSENTIAL findings

### P1B-E1 — Title/abstract claim of "verification" is unsupported (entire paper)
**Pages 1, 2, §I, §III, §VI:** The title declares a "Technical Verification Companion to the ECH Spin-Torsion Program." The body then states for each analysis:
- (§III) "this run … carries *no torsion modifications to the Boltzmann equations*; … It does *not* verify the spin-torsion theory module itself; that would require a bespoke modified Boltzmann code."
- (§IV) "Not a competitive sky detection."
- (§VI) "It is not derived from minimal ECH … is not a distinctive ECH prediction."

If none of the three analyses tests ECH, the paper does not verify what its title says it verifies. **Fix required:** retitle to honestly reflect scope (e.g., "Null-Consistency Checks and Pipeline Validation in the Context of the ECH Program") OR add an actual torsion-modified Boltzmann calculation. As currently framed the title is misleading.

### P1B-E2 — Abstract omits the load-bearing DESI w₀w_a claim that the body promotes as the "headline result"
**Page 1 abstract vs §V.B page 6:** The abstract reports only ∆N_eff ≈ 0 and H₀ ≈ 67.7. §V.B states: *"The headline result is w₀ = −0.812 ± 0.044 (departing from the ΛCDM point w₀=−1 at +4.3σ) and w_a = −0.667 ± 0.186 …, with w₀+w_a = −1.48 ± 0.15 requiring phantom crossing (the canonical quintom signature)."* A 4σ-level departure from ΛCDM cannot be both "the headline result" and absent from the abstract. **Fix required:** decide which claim is load-bearing and make the abstract internally consistent with the body; if w₀w_a is headline, retract the ∆N_eff-only framing of the abstract.

### P1B-E3 — Headline sigma values from non-comparable procedures juxtaposed without per-instance qualification
**Page 1 abstract:** "βˆ = 0.238° (pipeline-recovery bias 0.032°)" is juxtaposed with the published "2.4–2.9σ" sky detection in the same paragraph. A footnote later disambiguates, but Reviewer Instruction 7 is explicit: every juxtaposition must carry the "not directly comparable" qualifier. The phrase "pipeline-recovery SNR = 20.32σ" appears in §IV adjacent to the published 2.4–2.9σ without inline qualification at that point. **Fix required:** strip "σ" units from the MC pipeline-recovery numbers (they are recovery ratios, not detection significances) and add inline "(MC pipeline-recovery, not a sky-detection significance)" at every occurrence.

### P1B-E4 — Self-contradictory dataset attribution for β = 0.342° ± 0.094°
**Page 1 footnote a; §VI:** The abstract cites β = 0.342° ± 0.094° (3.6σ) as the comparison value, but footnote (a) admits this number is from the *published* PR3+WMAP9 analysis, while the "PR4/NPIPE" labels in the body refer to a *different dataset* in the public reproduction repository. So the ALP-MCMC (§VI) "re-runs actually use" a different dataset than the headline number being compared against. This is a citation-data-product mismatch in a load-bearing comparison. **Fix required:** either compare to PR3+WMAP9 numerics (and use that dataset in the MCMC) or compare to PR4/NPIPE published numerics (and switch the cited headline).

### P1B-E5 — "Consistency with the published 3.6σ joint signal" is undercut by 25× misalignment fine-tuning
**Pages 1, 7, footnote 4:** The abstract claims the ALP with f_a ~ M_Pl, m ~ H₀ is "consistent with" β = 0.342° ± 0.094°. Footnote 4 then admits that spectator status (Ω_a ≪ 1) requires θ_i ~ 0.1, while the prior mid-point is θ_i = 0.5 — a 25× tuning. With β ∝ θ_i along the underdamped trajectory, dropping θ_i by 5× requires C_aγ to rise correspondingly (the paper notes the implied C_aγ band is 9–51, all well above standard KSVZ/DFSZ O(1)). The "spectator-ALP consistency" claim therefore requires both initial-condition fine-tuning *and* a non-minimal photon coupling. The abstract sentence "consistent with the published joint WMAP+Planck value" does not survive Reviewer Instruction 10 (every load-bearing scalar must be audited). **Fix required:** the abstract must state that consistency requires (i) ~25× initial-condition tuning and (ii) non-minimal C_aγ ≳ 9.

### P1B-E6 — Page length grossly exceeds proven content
**10 pages.** After scope deflation (P1B-E1), the contributions are: one converged null MCMC table; one Monte-Carlo pipeline-recovery number; one ALP consistency check that does not distinguish ECH from GR. This is a 3–4 page methods note, not a 10-page PRD paper. Substantial padding consists of self-corrections, sample-count reconciliations (footnote 1), internal arithmetic audits ("MB–H₀ joint-posterior offset check"), and KDE/Savage-Dickey-failure rationales. **Fix required:** compress to ≤4 pages or add genuine theory-side content (a torsion-modified Boltzmann run).

### P1B-E7 — Cross-validation comparison with Liu et al. is misleading
**§III, page 5:** "Liu et al. constrained an EC torsion model … finding torsion preferred by AIC (∆AIC = −5.7 to −6.6). Our MCMC agrees at 0.5σ in H₀ and 0.4σ in σ₈." Liu et al. use a torsion-modified Boltzmann analysis and find a preference for torsion; the present paper uses stock CAMB and finds a null. Agreement on H₀/σ₈ posterior means is therefore a tautology of using overlapping data, not a "cross-validation" of any torsion preference. Presenting it as cross-validation conflates a non-result with a positive result. **Fix required:** remove or rewrite this paragraph to clarify it is a posterior-overlap check, not an independent confirmation of any torsion preference.

### P1B-E8 — Arithmetic discrepancy between "canonical 3.6σ" and the recomputed offset (3.2σ)
**§III, page 4–5:** The text claims a 0.155 mag offset is "~3.2σ relative to the chain's σ_MB = 0.049" and that this "corresponds *exactly* to the canonical 3.6σ Hubble tension." 0.155/0.049 = 3.16σ, not 3.6σ. The two numbers are not "exactly" equal; they differ by ~12%. **Fix required:** delete "exactly" and either explain the geometric reason for the residual gap or report the offset as 3.2σ without implying it equals 3.6σ.

---

## MAJOR findings

### P1B-M1 — "Bounce scenario motivates extending ΛCDM by ∆N_eff" but the EFT operator (HDM) gives ∆N_eff = 0
**§III, page 3:** The same paragraph that motivates a ∆N_eff proxy then admits: "The Hehl–Datta–Mercuri parity-even four-fermion contact interaction that survives torsion elimination is dimension-6 and M_Pl⁻²-suppressed: its leading Boltzmann effect is a scattering-amplitude shift, *not a relativistic species, and it does not produce a ∆N_eff at recombination*." If the EFT predicts ∆N_eff = 0 by construction, the entire MCMC is testing a quantity that the underlying theory does not predict. This is not a "phenomenological proxy"; it is testing the wrong observable. **Fix required:** either justify why a parameter the theory cannot produce is the relevant probe, or remove the framing that this MCMC supports the ECH program in any way.

### P1B-M2 — Table II is a major analysis hiding inside a "companion" paper
**Page 4, Table II:** The DESI DR2 w₀w_a posterior summary (N = 128,385 samples, 16 chains, full χ² decomposition) is a stand-alone cosmological analysis with a phantom-crossing claim at the 3–4σ level. This is not "technical verification" of anything; it is a separate primary result that should either be its own paper or be lifted into the abstract with appropriate caveats. As currently embedded, it is concealed.

### P1B-M3 — "Robust ln B deferred" used as escape clause for the central w₀w_a claim
**§V.B, page 6:** All model-comparison statistics (∆AIC, ∆BIC, ln B) are "deferred to a follow-up nested-sampling analysis." The paper then promotes w₀ = −0.812 ± 0.044 as the "headline result" with phantom crossing. You cannot have it both ways: either ∆AIC/ln B is needed for a claim to be load-bearing (in which case the w₀w_a result is not headline) or it is not (in which case the deferral is fictitious). **Fix required:** report ∆AIC/∆BIC at minimum, or demote the w₀w_a paragraph from "headline result" status.

### P1B-M4 — NaMaster MC does not test what the abstract claims it tests
**Abstract, §IV:** The abstract explicitly states the MC "confirms the algebraic pseudo-C_ℓ E→B deconvolution under MASTER mode coupling, NOT the physical separation of the cosmic-rotation angle β from the instrumental-miscalibration angle α." If the foreground-cleaned Commander map *removes* the very component required to break the β–α degeneracy, then the recovery test does not validate the analysis chain used to extract β from real Planck data. The MC therefore validates an algebraic identity (M_ℓℓ' inversion) that does not require the Planck data to validate. **Fix required:** state the validation as a software unit test, not as supporting evidence for the literature β values.

### P1B-M5 — Bias 0.032° → 0.040° characterization revised in-text; suggests pre-publication instability
**§IV, page 5–6:** "the bias was initially characterized as strictly 'stable across all three injections' at 0.032°, but the 0.342° injection actually gives 0.040°, a relative ~12% amplitude-dependent component." This is internal-bookkeeping language that should not appear in a journal submission. **Fix required:** delete the meta-narrative and report the final result.

### P1B-M6 — Long sample-count reconciliation footnote in §III (footnote 1)
**Page 2 fn. 1:** Six sentences of arithmetic reconciling 309,189, 216,432, 119,617, 123,129, 123,368, 114,992, with comments like "within ±1% of the 123,368 exact computation, with the small offset reflecting the chain-end-truncation of partial samples at the burn-in cut." This is referee-reply prose, not a paper. **Fix required:** report one canonical sample count per chain in the table and remove the footnote.

### P1B-M7 — The Eq. (3) numeric coincidence is presented as a derivation but is a re-arrangement
**§VI, page 7:** β ≈ α_EM × 8 / (4π) × 1.07 ≈ 0.29° matches the "fiducial" β ≈ 0.27° claimed at the abstract level. But the prefactor 1.07 is just ∆ϕ/f_a at the chosen scan-prior midpoint and C_aγ = 8 is hand-chosen. The formula is dimensionally fine and the arithmetic checks (α_EM × 8 / (4π) × 1.07 → 0.285°), but the framing implies this is a prediction. It is a re-arrangement at a tuned midpoint. **Fix required:** label the equation as a parameter-choice readout rather than a prediction.

### P1B-M8 — "Independent verification" of the NaMaster pipeline is the authors' own run
**§IV, page 5:** Subsection header "Independent verification (production 500-realization run, April 2026)" is self-referential. "Independent" here apparently means a later code run by the same author. **Fix required:** retitle (e.g., "Production 500-realization run").

### P1B-M9 — Caγ benchmark interpretation softens an exclusion into a "non-generic" statement
**§VI, page 7:** Required C_aγ ∈ [9, 51], with the abstract claiming the "natural" parameter envelope brackets the observed β. C_aγ ≥ 9 is *not* natural — KSVZ/DFSZ models predict O(1). The text concedes this ("entire required range therefore lies outside minimal ALP photon-coupling benchmarks") but the abstract and §VII still say the parameters are "natural." **Fix required:** reconcile the abstract phrasing with the body admission.

### P1B-M10 — "Stock CAMB" is the entire analysis, but is presented as a "phenomenological proxy for the spin-torsion sector's possible effective radiation contribution"
**§III:** Without a derivation linking the spin-torsion sector to a ∆N_eff prediction (and §III itself rules out such a derivation; see P1B-M2 above), calling stock CAMB a "proxy" for spin-torsion is rhetorical. **Fix required:** drop the "proxy" framing and present this as what it is — a standard ΛCDM+∆N_eff fit useful for the broader bounce-class compatibility argument made in Paper I(a).

### P1B-M11 — Internal-audit / referee-reply prose embedded throughout
Numerous passages are written as referee-reply rebuttals rather than as paper text:
- "An earlier count erroneously quoted '98.6% quintom-B' weight; in the actual converged chain there are zero free-w₀w_a samples at the LCDM point" (§III p.3)
- "the bias was initially characterized as strictly 'stable across all three injections' at 0.032°" (§IV p.5)
- "This addresses earlier reviewer concerns that the reported 67.68 was inconsistent with active SH0ES likelihood" (§III p.4)
- "NOT a YAML alias failure; the parameters are correctly aliased" (§III p.5)
- "the prior caveat promised a Savage-Dickey ratio on the converged 2D (w, w_a) marginal, but with zero free-w₀w_a samples at the LCDM point the KDE estimator fails catastrophically" (§III p.3)

Each of these is internal review-loop language and should be removed before submission.

### P1B-M12 — Figure 1 caption number disagrees with Table I
**Page 5:** Figure 1 caption says "119,617 post-burnin samples, getdist-thinned from 176,240 raw." Table I lists "Total samples 176,240" but no post-burnin count. Footnote 1 separately computes "123,368" exact and "123,129" actual. So at least four different sample counts (176,240; 123,368; 123,129; 119,617) describe the same chain. **Fix required:** one number per chain, defined unambiguously.

### P1B-M13 — Marginal-tail "+4.3σ" is repeatedly described as "departing from ΛCDM"
**Page 4 Table II, page 6 §V.B:** Footnote (a) to Table II correctly notes this is "a posterior-tail extrapolation distance only, *not* a Bayes-factor or ln B exclusion and *not* a frequentist tension." But §V.B then writes "departing from the ΛCDM point w₀=−1 at +4.3σ" without that qualifier. Reviewer Instruction 7 applies. **Fix required:** every "Nσ from LCDM" usage must carry the marginal-tail-only caveat inline.

---

## MINOR findings

### P1B-m1 — Bibliography year mismatch for ref [3]
Citation [3] is dated 2025 (arXiv:2509.13654) but labeled "ACT DR6"; ACT DR6 main release is 2025. Consistent, but verify the arXiv ID resolves; "2509" is a future YYMM for the 2025 ref, possibly correct, but should be double-checked at copy-edit.

### P1B-m2 — PACS numbers used
PACS was retired by APS in 2017 in favor of PhySH. PRD does not require PACS. Replace.

### P1B-m3 — Equation (3): magnitude check OK, but δϕ/f_a = 1.07 implausibly large for m ≈ 1.8H₀
The text writes m ≈ 1.8 H₀, ∆ϕ/f_a ≈ 1.0. For an underdamped axion with m ~ 2H₀, the field oscillates and Δϕ/f_a should be of order θ_i with damping, not unity. Specify whether this is end-state displacement or maximum excursion.

### P1B-m4 — Mode-coupling matrix function: LaTeX-rendered underscore
"NmtWorkspace.compute coupling matrix" should be `compute_coupling_matrix` (typo / underscore lost).

### P1B-m5 — Abstract footnote (a) is excessively long
Footnote (a) on page 1 occupies a significant fraction of the first page below the abstract and reads as an erratum. Move to the body.

### P1B-m6 — "Acknowledgments" claims Claude was used as "AI research assistant"
PRD has begun requiring AI-use statements. This disclosure is welcome, but the claim "All scientific claims … were independently verified by the author" is undermined by the level of arithmetic confusion in §III footnote 1, the bias narrative in §IV, the headline-result drift between abstract and §V, and the missing AIC/BIC numbers. The disclosure should specify which sections used AI and how.

### P1B-m7 — Inverse-variance combination uses values that the paper itself flags as not jointly valid
**Eq. (4), §VI:** Combining Planck NPIPE 0.30°±0.11° with ACT DR6 0.215°±0.074° via simple inverse-variance ignores shared sky region and shared component-separation systematics. The paper acknowledges this and labels it "auxiliary cross-check only." If it cannot be used as headline, it adds noise rather than signal. Consider removing.

### P1B-m8 — "fNL = −35/8" appears in §I as if a present-paper result
**Page 2:** "the surviving matter-bounce-specific test predictions (fNL = −35/8, …)" is stated in the introduction's "What is NOT in this paper" paragraph. This is appropriately cited to Paper I(a) but the placement (a value attributed without external citation here) reads as if it were a result of this paper.

### P1B-m9 — Table I, footnote a: "k = 7" referenced as "elsewhere in this paper" but the body uses "8 cosmological" (Table II caption)
There is internal inconsistency between "7 cosmological + 10 Planck nuisance" (Table I, ∆N_eff run) and "8 cosmological + 9 nuisance" (Table II, w₀w_a run). These are different runs, but the footnote does not say so clearly.

### P1B-m10 — "third Planck-only run currently at sub-convergence sample count" appears in the abstract
A "currently ongoing" qualifier in an abstract is unusual for a journal submission. Either include the third run or remove the mention.

### P1B-m11 — Repeated phrase: "load-bearing"
The phrase "load-bearing" appears in §V.B and Appendix A in similar constructions about which parameters are deferred. Not a duplicate-words bug, but stylistic repetition.

### P1B-m12 — w_pivot phrasing inconsistent
Table II reports w_pivot = −1.0344 ± 0.0301, "−1.1σ from −1." (−1.0344 − (−1))/0.0301 = −1.14σ. The 1.1σ rounding is fine, but elsewhere in the paper sigma values are quoted to one decimal with different rounding conventions. Standardize.

---

## NIT findings

### P1B-N1 — Date: "2026-06-03 PDT"
Includes a timezone in the dateline; PRD style does not use timezone tags.

### P1B-N2 — Footnote 3 (§VI page 6) is essentially a defensive caveat about background-cosmology choice
Tone is conversational. Compress.

### P1B-N3 — Table III "Claims classification" table is appropriate as a transparency tool but unusual for a PRD body
Consider relocating to Supplemental Material.

### P1B-N4 — "RunPod H200 instances" in Acknowledgments
Hardware vendor in acknowledgments is unusual; either cite as a service or remove.

### P1B-N5 — "$\sim 25\times$ tuning" referenced as a self-citation to "fn. 4"
"fn. 4" appears multiple times as an inline reference. Use proper footnote machinery so the LaTeX `\footnote{}` numbering is consistent.

---

## Summary recommendation

**REJECT**

The paper's central problem is that its title and abstract advertise verification of an ECH spin-torsion program, but the body of the paper transparently admits that each of the three analyses either (a) uses an unmodified Boltzmann code that cannot test the theory, (b) is a software self-recovery test on a foreground-cleaned map that has had the discriminating component removed, or (c) is consistent with the data in a way that is identical in standard GR and requires both 25× initial-condition fine-tuning and a non-minimal photon coupling. After honest scope deflation, the load-bearing scientific output of 10 pages is one null ∆N_eff result, one pipeline unit test, and one consistency check with a model the authors say does not distinguish their theory. Simultaneously, a substantial DESI w₀w_a "headline" quintom claim (Table II) is buried in the body and absent from the abstract, while ∆AIC/∆BIC/ln B numbers needed to evaluate that claim are explicitly deferred. The manuscript also contains pervasive referee-reply prose, internal sample-count reconciliations, self-corrections of prior characterizations, and dataset-attribution mismatches in the cited headline number. A PRD submission must speak in finished sentences about a controlled result; this draft does neither. The author should restructure into a short methods note that drops the verification framing, OR add a torsion-modified Boltzmann analysis that actually tests ECH.

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional Findings (Fresh-Eyes Pass)

Re-reading the manuscript with explicit checks across the requested categories surfaces several issues my first pass did not catch. The most significant are an apparent S₈ uncertainty that disagrees with naïve error propagation by ~50%, an ALP-MCMC posterior that sits **outside** the "natural range" the same section quotes, and a "scan midpoint" definition that uses the lower edge of the prior rather than its midpoint. New findings below; nothing previously flagged is repeated.

---

## ESSENTIAL findings

### P1B-E9 — Table I: S₈ uncertainty for Planck+BAO+SN is inconsistent with propagated σ(σ₈) and σ(Ωₘ)
**Page 3, Table I:** For Planck+BAO+SN, the table lists σ₈ = 0.812 ± 0.009, Ωₘ = 0.312 ± 0.006, and S₈ = 0.831 ± 0.018. But for the same chain, naïve uncorrelated propagation gives

σ(S₈) ≈ S₈·√[(σ_σ₈/σ₈)² + ¼(σ_Ωₘ/Ωₘ)²] = 0.831·√[(0.009/0.812)² + ¼(0.006/0.312)²] ≈ 0.012.

In a real chain σ₈ and Ωₘ are typically anti-correlated, which would tighten σ(S₈) further (the full-tension row shows σ(S₈) = 0.008 < propagated 0.010, consistent with negative correlation). The reported 0.018 is **50% wider** than naïve propagation and ~2× wider than the full-tension row, even though the underlying σ₈ and Ωₘ uncertainties are barely different across rows. This is either a typo (likely a stale or transposed digit), or a different definition of S₈ between rows. The number is load-bearing because S₈ appears in the abstract's lineage and in the DES-Y3 prior comparison.
**Fix required:** recompute σ(S₈) for both rows from the actual MCMC samples and reconcile; if 0.018 is correct, explain why an anti-correlation flips between rows.

### P1B-E10 — "Scan-midpoint θᵢ = 0.5" is the lower edge of the prior, not the midpoint, and breaks the 25× tuning arithmetic
**Footnote 4 (p. 7), Appendix C:** Appendix C states the θᵢ prior is uniform on **[0.5, 2]**. Footnote 4 then writes "θᵢ = 0.1 vs the scan-midpoint θᵢ = 0.5". But 0.5 is the **lower bound** of the prior; the midpoint of [0.5, 2] is 1.25 (linear) or 1.0 (geometric). The "25×" tuning the paper repeatedly invokes is (0.5/0.1)² = 25 via Ωₐ ∝ θᵢ². Using the actual midpoint:
- linear midpoint 1.25: tuning is (1.25/0.1)² = **156×**
- geometric midpoint 1.0: tuning is (1.0/0.1)² = **100×**

So either the tuning is 4–6× worse than the paper admits, or the prior should be re-defined so that 0.5 is genuinely "natural midpoint" (e.g., prior on [0.1, 0.9]). The "25×" figure that appears in the abstract, §VI, footnote 4, and §VII is internally inconsistent with the prior actually stated in Appendix C.
**Fix required:** either change "scan-midpoint" to "lower edge of scan prior" and update all 25× references to 100–156× (geometric or linear), or redefine the prior so that 0.5 is genuinely the midpoint.

---

## MAJOR findings

### P1B-M14 — ALP-MCMC posterior implies Δϕ/fₐ outside the "natural range" stated in the same section
**§VI, page 7:** With C_aγ = 8 fixed and the relation β = (α_EM/4π)·C_aγ·(Δϕ/fₐ), the posterior βALP = 0.336° ± 0.107° implies Δϕ/fₐ = β/[(α_EM/4π)·8] = 0.336°/0.266° ≈ **1.26**, which lies **outside** the natural envelope [0.2, 1.1] quoted three sentences earlier ("ALP trajectories … Δϕ/fₐ ∈ [0.2, 1.1]"). Equivalently, the data prefer a corner of model space the paper has just labeled as outside the natural range. The posterior central value is therefore not in the "natural" region; the apparent "consistency" of the model with data is being purchased by allowing the chain to wander into the non-natural tail.
**Fix required:** either widen the natural envelope to admit the posterior central value, or report the (m/H₀, θᵢ) posterior mode explicitly so the reader can verify it is interior to the prior support.

### P1B-M15 — Eq. (2) and Eq. (3) use *different* "fiducial midpoints" two lines apart
**§VI:** Eq. (2) defines a fiducial (m = H₀, θᵢ = 1) yielding Δϕ/fₐ ≈ 0.65; Eq. (3) immediately below uses (m ≈ 1.8 H₀, θᵢ = 1) yielding "Δϕ/fₐ ≈ 1.07" via "1.07" as a prefactor. The "fiducial value β ≈ 0.27°" claimed in the same paragraph corresponds to Δϕ/fₐ ≈ 1.0, a third value. Three different fiducial parameter points appear in three adjacent sentences, all labelled "fiducial."
**Fix required:** pick one fiducial point, state it explicitly with all three quantities (m/H₀, θᵢ, Δϕ/fₐ), and remove the others.

### P1B-M16 — H₀ uncertainty inverts between extended models: tighter when *more* parameters are sampled
**Tables I vs II:** Table I (∆N_eff extension, 7 cosmological parameters, Planck NPIPE CamSpec + BAO + Pantheon+): σ(H₀) = 1.09. Table II (w₀w_a extension, 8 cosmological parameters, DESI DR2 + Planck PR4 lowl+CamSpec.TTTEEE + lensing + DES-Y5 + Pantheon+): σ(H₀) = 0.455. A model with more parameters and partially overlapping data is **2.4× more constraining** on H₀. This is unusual; in most MCMC analyses, adding w₀w_a degeneracies broadens H₀, not tightens it. The likely explanation is a different Planck likelihood stack (PR3 NPIPE CamSpec vs PR4 lowl+highl.CamSpec) and DESI DR2 vs DESI DR1, but if so the two tables are not directly comparable runs and the reader has no way to know without reverse-engineering the YAMLs.
**Fix required:** explicitly state which Planck likelihood version and which DESI release each table uses, and explain the σ(H₀) inversion.

### P1B-M17 — Pipeline-recovery bias is 2.7σ relative to the MC noise floor
**§IV, Eq. (1):** β̂ = 0.238° with SNR = 20.32 implies σ_MC ≈ 0.238°/20.32 = 0.0117°. The 0.032° bias is then **2.7σ in MC units** — not a small residual but a substantial systematic. For a pipeline that is being held out as validating the deconvolution of cosmic-rotation angles at the level of published 2.4–2.9σ detections (i.e., comparable to or below 0.1° in the data), a 2.7σ bias in the recovery would dominate any sky measurement at the same precision.
**Fix required:** report bias/σ_MC explicitly in the abstract and §IV; the apparent "0.032° bias" hides the fact that this is a multi-σ MC effect.

### P1B-M18 — Monte Carlo noise level (ACT, 10 µK·arcmin) does not match the Planck Commander map being processed
**§IV, page 5:** "The 500 Monte Carlo realizations are drawn at ACT-noise level ∆P = 10 µK·arcmin… The Commander map is a foreground-cleaned CMB-only product." Planck Commander is *Planck* noise, not ACT noise. Mixing ACT noise on a Planck map produces an MC pipeline that does not match either survey. The justification "a conservative worst-case bias check" is not adequate — neither survey actually has this noise/foreground combination, so the bias derived from this MC has no clear interpretation as a validation for either Planck or ACT analyses.
**Fix required:** either use Planck-level noise on the Planck map (the matching configuration), or state explicitly that the MC is not a validation for any specific real analysis.

### P1B-M19 — ALP-MCMC reports only the C_aγ = 8 result; the C_aγ = 4 and 12 chain results are silently suppressed
**§VI vs Appendix C:** Appendix C states C_aγ takes "one of {4, 8, 12} across the three configurations." §VI quotes only "βALP = 0.336° ± 0.107° (C_aγ = 8 fixed)." The C_aγ = 4 and C_aγ = 12 chains exist (3,240 samples each per the appendix) but their β posteriors are not reported. Since the entire "naturalness" of the photon coupling is in dispute (P1B-M9), the C_aγ = 4 and C_aγ = 12 chain posteriors are the load-bearing comparison: if C_aγ = 4 cannot produce β ≈ 0.34° at any (m, θᵢ) in the prior, that is a model-rejection signal that the paper buries.
**Fix required:** report all three βALP posteriors (C_aγ = 4, 8, 12) in a table.

### P1B-M20 — Reference [1] ("Paper I(a)") is unpublished; the entire "companion" framing is non-verifiable
**Bibliography:** Reference [1] is "H. Golden, Structural Closure of Einstein–Cartan–Holst Dark Energy… (in preparation) (2026), HUBIFY-2026-001A; companion paper, this volume." References [4], [5], [6] are also "in preparation" by the same author. The present paper is positioned as a "technical verification companion" to Paper I(a), but the parent paper does not exist in any retrievable form. A reviewer cannot check what the 14 barriers actually are, what the perturbation-transparency theorem actually proves, or whether the present paper's claims about Paper I(a) are accurate.
**Fix required:** post Paper I(a) to arXiv before submitting the companion; PRD does not accept "companion to a paper in preparation."

### P1B-M21 — βALP and βfree are fit to a different dataset than βobs they are compared to
**§VI, page 7:** The text writes "βALP = 0.336° ± 0.107° (C_aγ = 8 fixed), consistent with the model-independent fit βfree = 0.344° ± 0.096° (… Planck PR4 + ACT DR6 EB-spectrum likelihoods …) and the observed βobs = 0.342° ± 0.094°. All three within 1σ." But per footnote (a) on page 1, βobs = 0.342° ± 0.094° is the published value from **PR3 + WMAP9**, while βALP and βfree are fit to **PR4/NPIPE + ACT DR6**. The "All three within 1σ" comparison is therefore across datasets — these are not independent measurements of the same posterior. The fact that they agree at 1σ tells you nothing about whether the model fits Planck PR4 + ACT DR6 well; it tells you the chain converged near the headline number with a comparable error bar, which is what an MCMC with that data product should do regardless of the model.
**Fix required:** compare βfree to a Planck PR4 + ACT DR6 published number (e.g., the relevant entry in [3]), not to the PR3 + WMAP9 number from [2].

### P1B-M22 — Δχ² between w₀w_a and ΛCDM chains is not reported, even though it is computable from the present runs
**§V.B:** "Robust Bayesian evidence / Bayes factor ln B is NOT reported here." A frequentist Δχ² between the (w₀w_a) and (ΛCDM) best-fit points on the **identical likelihood stack** does not require nested sampling — only a maximizer run on the ΛCDM-restricted slice of the same likelihood. The paper omits even this simpler diagnostic, which would unambiguously settle whether the apparent +4.3σ marginal-tail departure corresponds to a meaningful improvement in fit. Reporting "phantom crossing required" without Δχ² leaves the reader unable to distinguish a real improvement from a volume effect.
**Fix required:** report Δχ² = χ²(w₀=−1, w_a=0; max) − χ²(w₀, w_a; max) on the same likelihood; this is a few CPU-hours, not a nested-sampling run.

---

## MINOR findings

### P1B-m13 — Acknowledgments thanks LiteBIRD "for providing the data"
**Page 8, Acknowledgments:** "We thank the Planck, ACT, LiteBIRD, and Cobaya collaborations for providing the data, code, and observational infrastructure used in these analyses." LiteBIRD has not flown and has not provided data; it is referenced only as a forecast in §VI. Cobaya is software, not data. Remove or rephrase.

### P1B-m14 — Hehl–Datta–Mercuri attribution: Datta is not cited
**§III, page 3, refs [8, 9]:** The "Hehl–Datta–Mercuri parity-even four-fermion contact interaction" is attributed to references [8] (Hehl-Heyde-Kerlick-Nester 1976) and [9] (Mercuri 2006). The eponymous "Datta" is presumably D. Datta (1971, Nuovo Cimento B 6:1), which is not in the bibliography. Either cite Datta or rename the operator.

### P1B-m15 — Cosmic-birefringence formula β = (α_EM/4π)·C_aγ·(Δϕ/fₐ) is uncited
**§VI, Eq. (3):** The formula derives from Carroll-Field-Jackiw 1990 (PRD 41:1231) / Harari-Sikivie 1992. The paper uses it without citation; a method note in a verification-companion paper should cite at least one of these.

### P1B-m16 — Sample-count for ALP-MCMC per chain is unstated
**Appendix C:** "9,720 total accepted samples across 3 configurations" gives 3,240 per C_aγ value. But how many MCMC chains per configuration? If 1 chain × 3,240 samples, R̂ cannot be computed at all. If 4 chains × 810 samples each, the posterior is severely under-sampled. The number of parallel chains per configuration must be stated for R̂-1 < 0.01 to be meaningful.

### P1B-m17 — Equation (3) prefactor "1.07" vs stated "Δϕ/fₐ ≈ 1.0" — rounding inconsistency
**§VI page 7:** Eq. (3) uses prefactor 1.07; the paragraph below states "the fiducial value β ≈ 0.27° corresponds to … Δϕ/fₐ ≈ 1.0." Computed β with Δϕ/fₐ = 1.0 and C_aγ = 8: β = 0.266°. With 1.07: β = 0.285° ≈ 0.29° (matches Eq. 3). So the "fiducial β ≈ 0.27°" rounds 0.285° to 0.27°, which is a 5% downward rounding. The "≈ 0.27°" pervades the abstract and §VI; either round to 0.29° honestly or revise Eq. (3) to use 1.0.

### P1B-m18 — Table II "χ²_total = 14037.4 ± 5.6" sample-scatter σ presented without specifying it is sample-scatter, not goodness-of-fit
The ±5.6 here is the chain-sample scatter of −2 ln L at the posterior, not an uncertainty in goodness-of-fit. A reader unfamiliar with Cobaya output will misread this. Clarify in the caption.

### P1B-m19 — Footnote 1 final post-burnin count "216,432" is presented as the canonical total, but the abstract uses 309,189 (raw)
**Page 1 abstract vs footnote 1 page 2:** The abstract emphasizes "309,189 frozen samples"; footnote 1 reveals the post-burnin total is 216,432. The 309,189 raw figure inflates the impression of statistical power by ~43%. Standard practice is to quote post-burnin sample counts as the "size" of an MCMC analysis.

---

## NIT findings

### P1B-N6 — "Both ends are larger than the standard KSVZ/DFSZ benchmark range"
KSVZ and DFSZ are *QCD axion* benchmarks (with m_a ↔ f_a fixed by the QCD anomaly). Applying them as a sanity check for an ultra-light ALP (m ~ H₀, f_a ~ M_Pl) is conventional but not strictly apples-to-apples. A footnote acknowledging this would help.

### P1B-N7 — "the chain settles into the 3.6σ-discrepant joint posterior" (§III)
"3.6σ-discrepant" is shorthand; quote the exact figure once. Repeated qualitative invocations of "3.6σ" without recomputing it for each context obscure which 3.6σ is being referenced (Eskilt+Komatsu birefringence vs Riess H₀ vs the inverse-variance combination).

### P1B-N8 — Footnote (a)-style attribution to PRD vs arXiv "PR3+WMAP9 vs PR4/NPIPE" should appear in the bibliography itself
The disambiguation should be in ref [2] rather than as an abstract footnote.

---

## Summary of new-pass conclusions

The fresh-eyes pass strengthens the original recommendation to **REJECT**. The most concerning new findings are:

1. **P1B-E9**: Table I's S₈ ± 0.018 for Planck+BAO+SN does not propagate from σ₈ and Ωₘ; this is either a typo or an undocumented definitional change between rows.
2. **P1B-E10**: The "25× tuning" cited throughout the paper as the spectator-fine-tuning cost is computed relative to "midpoint θᵢ = 0.5," but 0.5 is the **lower edge** of the [0.5, 2] prior, not the midpoint. The honest tuning at the linear or geometric midpoint is 100–156×, four to six times worse than the abstract admits.
3. **P1B-M14**: The C_aγ = 8 ALP posterior implies Δϕ/fₐ ≈ 1.26, **outside** the "natural range [0.2, 1.1]" the same section claims accommodates the data.
4. **P1B-M21**: βobs and βfree are compared as if same-dataset quantities, but the published 0.342° ± 0.094° is from PR3 + WMAP9 while βfree is fit to PR4 + ACT DR6.
5. **P1B-M20**: The parent paper [1] is unpublished, making the companion framing non-verifiable.

Together with the issues from the initial review, these collectively indicate that the paper's load-bearing comparisons are constructed across mismatched datasets, with inconsistent uncertainty propagation, and with a "natural"-parameter envelope that does not contain the posterior the data prefer. The arithmetic underpinning the headline "consistency" claim does not survive recomputation.