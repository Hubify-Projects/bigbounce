# Verdict: MAJOR REVISIONS

**Manuscript:** "The Exact Matter-Contraction Non-Gaussian Amplitude: Four-Vertex Derivation and Conditional Large-Scale-Structure Mapping"
**Author:** Houston Golden (Independent Researcher)
**Version string on p.1:** v1.7.130, dated July 24, 2026, 18:35 PDT
**File refereed:** `02_full_draft.pdf`, 12 pages, MD5 `f7116fe3e2541d6f649876f2ec7789ee`
**Journal:** Physical Review D, Research Article
**Referee stance:** cold, verdict-blind, adversarial. No prior knowledge of this manuscript or its history.

---

## Summary

The manuscript makes one primary claim and one clearly-subordinated secondary claim.

**Primary claim (algebraic).** In a matter-dominated contracting phase (w = 0, ε = 3/2), with standard-GR cubic perturbation theory and Bunch–Davies initial data, the squeezed-limit local non-Gaussianity amplitude is f_NL^local = −35/16 = −2.1875, not the −35/8 printed in Cai, Xue, Brandenberger & Zhang (Ref. [7], JCAP 0905:011). The author obtains this by transcribing Cai et al.'s four source-level cubic-vertex shape-function contributions from the arXiv source of Ref. [7] (Table IV), summing them exactly in sympy, re-expanding in an ordered symmetric degree-nine basis to obtain the coefficient vector (c₁,…,c₆) = (3, 1, −9, 5, −33, 9) [Eq. (4)], and taking the squeezed limit [Eq. (B1)/(B3)]. He reports that Cai et al.'s own printed total polynomial (their Eq. 37) differs from the sum of their own four vertices by a spurious local term −(99/128)Σᵢkᵢ³ [Eq. (B2)] and squeezed-reduces to −305/64, i.e. to neither −35/16 nor Cai's stated −35/8; he explicitly declines to reconstruct how −35/8 arose. Cross-checks offered: Cai et al.'s own ε-order-grouped intermediates [Eq. (B5)] and Li, Quintin, Wang & Cai's general-c_s formula (Ref. [8], their Eq. 5.1), f_NL = −165/16 + 65/(8c_s²) → −35/16 at c_s = 1.

**Secondary claim (observational, heavily self-disclaimed).** The exact shape is projected onto the local template, giving a flat-grid amplitude recovery r = 0.83542294 and shape cosine r_cos = 0.98167825; an adopted convention r = 0.84 ± 0.02 maps the published Heinrich, Doré & Krause SPHEREx multi-tracer bispectrum baseline σ(f_NL^local) ≃ 0.7 to a "2.63σ" arithmetic significance. An in-house channel-native (f_NL, b_φ, A_GR) surrogate-covariance Fisher ladder gives 3.47σ / 3.14σ / 2.32σ / 0.42σ under progressively weaker nuisance assumptions (Table III). Supporting material: a linear dressed-metric bounce-transmission check, an Einstein–Cartan four-fermion torsion estimate [Eq. (5)], a Planck PR4 consistency check, and a MegaMapper outlook labelled speculative.

### What I verified independently, and it holds

I re-derived the entire algebraic core in sympy from the numbers **as printed in the PDF**, with the following results — all exact, no rounding:

| Printed claim | Location | My independent check |
|---|---|---|
| K₉ basis, Eq. (3), with (3,1,−9,5,−33,9) | p.2, Eqs. (3)–(4) | consistent |
| Eq. (B4): 256 Πk² A = 9Σk⁹ + 3Σ₍ᵢ≠ⱼ₎k⁷k² − 27Σk⁶k³ + 15Σk⁵k⁴ − 198Σ^dist k⁵k²k² + 27Σ₍ᵢ≠ⱼ≠ₗ₎k⁴k³k² | p.9 | **exactly equal** to 256Πk²·A_T from Eqs. (1)+(3); difference = 0 symbolically. The −33 (six ordered triples) ↔ −198 = 3×(−66) (three distinct monomials) bookkeeping in Sec. II A is correct. |
| Squeezed limit and its first correction, Eqs. (B1)/(B3): −35/16 + (35/64)k₁²/k² | pp.8–9 | **exact.** My series expansion of B_NL(x·k, k, k) in x gives exactly −35/16 + (35/64)x². |
| Equilateral −255/128 = −1.9922 | Table I, p.2 | **exact** |
| Folded (k₁ = 2k, k₂ = k₃ = k) −9/8 = −1.125 | Table I, p.2 | **exact** |
| Table IV four vertex rows summing to Eq. (1) at ε = 3/2 | p.10 | **exact**; I reconstructed all four rows from the typeset table and their sum equals A_T identically. |
| Table V per-vertex squeezed values (−25/16, −5/32, 0, −15/32) | p.10 | **exact**, each row reproduced individually; column sum −35/16. |
| Table V per-vertex equilateral values (−35/32, −5/32, −5/8, −15/128) | p.10 | **exact**; column sum −255/128. |
| Eq. (B5) ε-order decomposition (−5/2, +5/16, 0) | p.10 | **exact**; sum −35/16. |
| Li et al. Eq. (5.1): −165/16 + 65/8 = −35/16 | p.8 | **exact** |
| Eq. (B2) shift: −(10/3)(99/128) = −165/64, −35/16 − 165/64 = −305/64 = −4.765625 | p.9 | **exact** |
| Dimensional argument for B_NL (degree 9 − 6 − 3 = 0) | p.2 | correct |
| Eq. (5) torsion prefactor (35/16)(3/16)γ²/(1+γ²): 0.0219 at γ = 0.2375; 0.2051 at γ = 1; "1–10% of 2.1875" | p.3–4 | arithmetic correct; κn²/ρ is dimensionless as claimed |
| 2.1875×0.8354/0.7 = 2.61; ×0.84/0.7 = 2.625→2.63; naive 3.125→3.13; 0.7/0.84 = 0.83 | pp.4–6 | all correct |
| Table III ↔ Sec. VII σ's: 2.1875/0.631 = 3.47; /0.697 = 3.14; /0.941 = 2.32; /5.173 = 0.42 | pp.6–7 | all correct |
| ρ(f_NL, A_GR) = −0.4264 ⇒ 0.631/√(1−ρ²) = 0.6976 ≈ 0.697 | p.7 | **internally consistent** — a good sign the surrogate Fisher is real |
| Planck map: −0.1/0.876 = −0.11; 5.0/0.876 = 5.71; (2.1875−0.114)/5.708 = 0.363σ | p.6 | correct |
| 34.7% RSD gain: 1 − 0.449/0.688 = 0.3474 | p.5 | correct |
| Wilson-Ewing w = −0.003 ⇒ n_s − 1 = 12w/(1+3w) = −0.0363 ⇒ n_s = 0.9637 ≈ 0.964 | p.4 | correct |
| (5/12)(1−n_s) ≈ 0.015; 2.1875/0.015 ≈ 146; non-attractor f_NL = +5/2 | pp.1, 5–6 | correct |
| ∆b = f_NL b_φ/M with b_φ^UMF = 2δ_c(b₁−1) ⇒ ∆b = 2f_NL δ_c(b₁−1)/M; M = 2k²T D/(3Ω_m H₀²) | Eqs. (6)–(8), p.4 | algebraically consistent (but see Finding 15 on the D normalization) |

This is an unusually clean algebraic core, and I want to be explicit that I found **no error anywhere in the printed symbolic mathematics**. I checked every displayed equation and every table entry that can be checked. That is the manuscript's genuine strength and it should not be lost in revision.

### Why I nonetheless cannot recommend acceptance

Three structural problems stand between this manuscript and a PRD Research Article.

1. **The central claim is a correction of the literature that the manuscript itself cannot close.** The paper does not perform an independent in-in calculation; it re-sums *transcribed intermediate expressions from the very paper it is correcting*, and its "three independent cross-checks" are not independent in the way claimed. Meanwhile *two* independently published total polynomials (Cai Eq. 37 and Li Eq. 4.19, which the author states agree coefficient-for-coefficient) disagree with the re-summation. The economical alternative hypothesis — that the author's permutation/summation convention for reading the vertex expressions differs from the convention under which those polynomials were assembled — is asserted away rather than excluded. (Findings 1–4.)

2. **The observational half asymmetrically applies the squeezed-limit projection argument.** The manuscript invokes Pajer–Schmidt–Zaldarriaga and Tanaka–Urakawa to push the inflationary local signal to "→ 0⁺" (Table II) while leaving the bounce prediction at its full −2.1875, and never addresses why the same observed-squeezed-limit/conformal-Fermi treatment does not also remove the bounce's squeezed signal. The entire "≫ 146" contrast, the paper's one comparative statement, rests on this untreated asymmetry. (Finding 5.)

3. **Several load-bearing numbers cannot be reconstructed from what is printed**, including the two numbers in the abstract (r, r_cos), the entire in-house Fisher ladder (no survey specification appears anywhere in the paper), the undefined r = 0.876, and the transmission bound 6.8×10⁻⁸. A PRD paper must be reproducible from its own text; a pointer to a script is not a substitute. (Findings 6–10.)

Additionally, roughly half the manuscript consists of material the author explicitly and repeatedly declares is not a result ("illustrative", "conditional", "not a paper headline", "not a forecast", "not a detection forecast", "not a result", "retained only as provenance artifacts"). A Research Article should not be half-composed of disclaimed content. (Finding 11.)

---

## Findings

### ESSENTIAL

**1. [ESSENTIAL] The "correction to the literature" is not established; no independent derivation is performed.**
*Location:* Title; Abstract ll. 15–16 ("The result corrects the unreproduced printed −35/8 literature value"); Sec. X Conclusion p.8 ("replaces the unreproduced printed −35/8 value"); Appendix B "Trusted-expression provenance," p.8.

The abstract and title advertise a "Four-Vertex Derivation." Appendix B states plainly what was actually done: "Cai et al.'s four source-level vertex expressions and their ε-order-grouped intermediates are **trusted inputs**." No cubic action is varied, no mode functions are written down, no in-in time integral is performed anywhere in the manuscript. Table IV contains pure momentum polynomials with all time dependence already integrated out *by the source being corrected*. What is demonstrated is: "the four expressions, as I transcribed them, sum to −35/16." That is a transcription-plus-summation exercise, not a derivation.

This matters because the claim being made is that a 2009 JCAP result published by four authors is wrong by a factor of two. The evidentiary bar for overturning a published value is an independent computation, and the manuscript does not clear it. Please either (a) perform the in-in calculation from the cubic action ab initio — write the mode functions for ε = 3/2 contraction with Bunch–Davies initial data, perform the four time integrals, and show the squeezed limit; or (b) retitle and reframe throughout so that the claim is exactly "the printed vertex expressions of Ref. [7] sum to −35/16, in agreement with Ref. [8]'s Eq. (5.1) at c_s = 1; the origin of the separately printed −35/8 is not determined here." Option (b) is defensible, but then "Derivation" must leave the title and "corrects the literature value" must leave the abstract.

**2. [ESSENTIAL] The alternative hypothesis — that the author's reading convention, not the literature, is the source of the discrepancy — is asserted away, not excluded, and the manuscript's own evidence points against it.**
*Location:* Appendix B, p.9: "Treating the repeated (5,2,2) orbit as three distinct monomials while retaining six (4,3,2) permutations is not this source convention: it drops a factor of two from only one orbit and breaks the equal forms of Cai et al.'s vertex expressions." Also p.9: "Li et al.'s printed total polynomial A_tot (their Eq. 4.19) agrees with Cai et al.'s transcribed polynomial A_T (their Eq. 37) coefficient-for-coefficient at c_s = 1."

The manuscript establishes that **two independently published total polynomials agree with each other** and both disagree with the author's re-summation of the vertex rows. By the author's own account this forces Ref. [8] to be internally inconsistent (their Eq. 4.19 → −305/64 vs. their Eq. 5.1 → −35/16) as well as Ref. [7]. When a single re-summation is in tension with two independent published assemblies, the leading hypothesis is a convention mismatch in the re-summation, not a shared error in the literature. The manuscript's sole rebuttal is a one-sentence typographical argument about which notation "breaks the equal forms of Cai et al.'s vertex expressions."

That is not enough. Please make this decisive. Concretely: (i) reproduce Ref. [7]'s Eq. (37) *from* the Table IV rows under some stated permutation convention, or demonstrate that no consistent convention does so; (ii) state explicitly whether Ref. [7]'s Σ notation is defined in that paper and quote the definition; (iii) most persuasively, do Finding 1(a) — an independent in-in computation settles this immediately and makes the convention argument moot.

I note as a diagnostic, and offer it constructively: the claimed discrepancy −(99/128)Σkᵢ³ is a *pure local shape*, and the only Table IV row producing a Σkᵢ³ term is the field-redefinition row, whose ε¹ piece is −(ε/2)Σkᵢ³ = −(96/128)Σkᵢ³ at ε = 3/2. The discrepancy is therefore numerically adjacent to the entire field-redefinition ε¹ contribution. Whether or not that is coincidence, the field-redefinition term — which alone carries −25/16 of the total −35/16, per Table V — is the single most convention-sensitive object in the calculation (it depends on the redefinition coefficient's evaluation time and on whether the redefinition is applied before or after the squeezed limit). The manuscript never discusses it. It should.

**3. [ESSENTIAL] The squeezed-limit projection argument is applied asymmetrically to inflation and to the bounce, and the consistency-relation status of matter contraction is never addressed.**
*Location:* Introduction p.1 ll. 55–60; Table II, p.6, "local observer" row: f_NL^bounce = −2.1875, f_NL^inf → 0⁺, ratio ≫ 146; Sec. VI A p.5; Abstract-adjacent claim in Intro ll. 28–31 ("the bounce-vs-inflation contrast remains |f_NL^bounce| ≫ |f_NL^inf| after the observable projection treatment").

The manuscript uses Refs. [3, 4] to argue that the inflationary consistency-relation term is absorbed by the coordinate/projection treatment and therefore "→ 0⁺" as an observable. It then leaves the bounce entry at its full primordial value in the *same* row of the *same* table. But Maldacena's consistency relation and the Pajer–Schmidt–Zaldarriaga projection theorem are statements about the squeezed limit of any single-clock adiabatic mode — and a matter-dominated contraction driven by a single clock is *prima facie* within their scope, with n_s ≈ 1 implying a consistency-relation f_NL ≈ 0, flatly at odds with −35/16.

The standard resolution in the bouncing-cosmology literature is that matter contraction is **not an attractor** — the spectrum is carried by what would be the decaying mode in expansion — so the consistency relation is evaded. That may well be right. But the manuscript never says it, never cites it, and never demonstrates it. As written, the paper's one comparative claim ("≫ 146", stated in the Introduction, Sec. VI, Table II and implicitly in the abstract) rests on applying a subtraction to the denominator and not to the numerator.

This must be fixed before the observational sections mean anything. Required: an explicit subsection establishing (i) whether the matter-contraction squeezed limit satisfies or violates the single-clock consistency relation and why; (ii) what the *observed* squeezed bispectrum is after the same conformal-Fermi/projection treatment that is applied to inflation in Table II; (iii) if the −35/16 does survive, a citation or derivation to that effect. If the answer is that −35/16 does *not* survive the observed-squeezed-limit projection, Secs. III–VIII must be withdrawn.

### MAJOR

**4. [MAJOR] The three cross-checks are presented as independent; at least one is an algebraic identity, and the count is internally inconsistent.**
*Location:* Appendix B p.9: "Two independent certifications bracket this result. First, Cai et al.'s own ε-order-grouped intermediate expressions (A^ε, A^ε², A^ε³; Eq. B5) sum to the Table IV total exactly (**difference = 0 symbolically**)…"; p.9 "what is certified, **four independent ways**, is −35/16"; p.9 "certified vertex-by-vertex and **cross-checked three ways**"; p.11 "The correction −35/16 is therefore certified vertex-by-vertex and cross-checked three ways."

Three problems.

(a) The manuscript states three counts of the same thing — "two independent certifications," "three ways," "four independent ways" — within two pages. Pick one and use it consistently.

(b) The ε-order-grouped check is not independent of the vertex sum *if* the grouped expressions were obtained by regrouping Table IV. The text is ambiguous: p.9 calls them "Cai et al.'s own ε-order-grouped intermediate expressions" (implying separate transcription), but p.10 says "The order-grouped values Eq. (B5) are the ε-decomposition Cai et al. describe, **made explicit**" (implying derivation by the author). If the latter, "difference = 0 symbolically" is a tautology and provides zero independent evidence. State unambiguously which it is, and if they were separately transcribed, display them.

(c) Ref. [8] is not independent of Ref. [7] in the sense required: Y.-F. Cai is a co-author of both. And Ref. [8]'s *own* printed polynomial (Eq. 4.19) contradicts its Eq. (5.1) under the author's reduction. Calling Eq. (5.1) "a wholly separate in-in method" (p.10) overstates the independence of a formula from the same group whose companion equation in the same paper disagrees.

I verified (Table V per-vertex, Eq. B5 order-by-order) that all of these *arithmetic* statements are exactly true. The objection is to their epistemic weight, not their correctness.

**5. [MAJOR] r = 0.83542294 and r_cos = 0.98167825 are quoted to eight significant figures from a grid and inner product that are never defined; I could not reproduce them.**
*Location:* Abstract ll. 18–19; Sec. II A p.2 ("On the fixed 23,098-triangle ratio grid…"); Sec. III B p.4.

The manuscript names "the fixed 23,098-triangle ratio grid" exactly once and never specifies: the k range, the ratio parametrization, the triangle-inequality handling, the binning, the measure, the weighting, or the definition of the inner product used to form r and r_cos. Nor does it write down the local template it projects against.

I attempted reproduction using Eq. (3) and four natural readings of a "flat grid" of 23,098 triangles, defining s ≡ B_NL/(−35/16), r = ⟨w·s⟩/⟨w⟩, r_cos = ⟨w·s⟩/√(⟨w⟩⟨w·s²⟩):

| weighting | r | r_cos |
|---|---|---|
| flat, unweighted (23,344 triangles) | 0.8588 | 0.9915 |
| Fisher-type w = (Σk³)²/(k₁k₂k₃)³ | 0.7897 | 0.9681 |
| Fisher-type × k₁k₂k₃ measure | 0.8208 | 0.9773 |
| w = 1/Σk³ | 0.8308 | 0.9828 |
| w = 1/(k₁k₂k₃) | 0.8062 | 0.9774 |

None reproduces (0.83542294, 0.98167825). I also note a consistency constraint the pair must satisfy: r_cos = 1/√(1 + σ_s²/r²) implies the weighted standard deviation of s must be σ_s = 0.1622 at mean 0.8354. Since s is bounded on [0.5143 (folded), 1 (squeezed)], that σ is 71% of the maximum attainable spread for that mean — i.e. the quoted pair requires an unusually bimodal weighting with roughly half its weight near the folded boundary, which is not what a "flat" triangle grid produces.

The pair may well be correct under the author's actual convention, but a referee cannot check it and a reader cannot use it. Please add: the explicit definition of the grid (bounds, spacing, count derivation), the local template B^loc(k₁,k₂,k₃) in closed form, and the inner product ⟨B, B'⟩ with its weight, as displayed equations. Then re-quote r to the number of digits the grid actually justifies — eight significant figures on a discretized grid is not meaningful precision regardless.

**6. [MAJOR] r = 0.876 is used for a published-data comparison, is never defined, is given two different names, and lies outside the paper's own adopted ±0.02 envelope.**
*Location:* Sec. III B p.4 ("…and the **previously defined signal-only endpoint** 0.876"); Sec. VIII p.6 ("using the **CMB-weighted recovery** r = 0.876 gives f_NL^bounce = −0.11 ± 5.71, only 0.36σ from the predicted −35/16"); Sec. III B/Eq. (10) "r = 0.84 ± 0.02".

Four distinct defects in one number.

(a) It is *not* previously defined. I searched the full text: the first occurrence of 0.876 is the sentence that calls it "previously defined."

(b) It is called "the signal-only endpoint" on p.4 and "the CMB-weighted recovery" on p.6. These are different concepts. Which is it?

(c) 0.876 lies **outside** [0.82, 0.86]. Sec. II A justifies keeping r = 0.84 ± 0.02 on the grounds that "the interval describes estimator-weight variation" — but the paper then uses an estimator weighting (CMB) whose recovery falls outside that interval. Either the envelope is wrong or 0.876 is not an estimator-weight variant.

(d) Sec. III B presents 0.8354 and 0.876 as the two endpoints of the spread, then writes the spread as 0.84 ± 0.02. The envelope of [0.8354, 0.876] is 0.8557 ± 0.0203. As written, the adopted central value is not the centre of its own stated endpoints and the quoted half-width does not reach the upper one.

This directly affects the Planck consistency statement (p.6) and Fig. 2, and should be resolved by defining every r variant used, in one place, with its inner product.

**7. [MAJOR] The in-house Fisher forecasts (C13/C14/C15) are reported to three digits with no survey specification, no covariance definition, and no Fisher equation anywhere in the manuscript.**
*Location:* Sec. IV pp.4–5 (σ = 0.626, 0.687, 0.631, 0.688; r_eff = 0.9929, 0.9986; RSD σ = 0.417, 0.449, r_eff = 0.9953, 0.9991, 0.9981); Sec. VII p.7 (σ = 0.631, 0.697, 0.941, 5.173; ρ = −0.4264, −0.5025, +0.9909); Table III p.7.

The manuscript reports something like twenty forecast numbers derived from calculations it describes only as "two in-house Fisher calculations… under a leading-order Gaussian multi-tracer covariance" and a "channel-native (f_NL, b_φ, A_GR) surrogate Fisher." Nowhere in twelve pages does the paper state: the survey volume or redshift range; the tracer set and their number densities; the linear biases b₁ (despite b₁ appearing in Eq. 7); k_min, k_max, or the binning; the number of triangles entering the bispectrum Fisher; the fiducial cosmology; the form of the covariance; or the Fisher matrix itself. Not one Fisher-matrix equation appears in the paper.

Sec. III C, titled "Galaxy Bispectrum," is two sentences long and contains no equations at all, in a paper whose entire observational content is a bispectrum forecast.

A Research Article reporting forecast σ's to three significant figures must contain the specification that produces them. Pointing to `scripts/c13_…py`, `scripts/c14_…py`, `scripts/c15_…py` is appropriate for reproduction but does not discharge the obligation to state the calculation. Please add a specification table (survey, tracers, n̄(z), b₁(z), k-range, binning, fiducial cosmology) and the displayed Fisher/covariance expressions, or remove the numbers.

I note in the paper's favour that the one cross-check available to me *passed*: ρ(f_NL, A_GR) = −0.4264 with σ_fixed = 0.631 gives σ_marg = 0.631/√(1−0.4264²) = 0.6976, matching the quoted 0.697 exactly. That is evidence the surrogate Fisher is a real calculation. It still is not a specified one.

**8. [MAJOR] The transmission bound |δf_NL| ≤ 6.8×10⁻⁸ is not reconstructible from the quoted numbers, and the stated k⁶ scaling contradicts the quoted endpoints.**
*Location:* Sec. II C p.3: "the measured departure is |T_c − 1| = 2.7×10⁻¹⁰ to 2.2×10⁻⁵ across kη_B = 0.002–0.03 (…the growth toward large k is k⁶ gradient-basis truncation, not physics), so the scheme-specific transmission correction to the −35/16 amplitude is |δf_NL| ≤ 6.8×10⁻⁸ at the observable scale kη_B = 10⁻²."

(a) **The stated scaling is inconsistent with the stated endpoints.** The quoted ratio is 2.2×10⁻⁵ / 2.7×10⁻¹⁰ = 8.15×10⁴ over a k range of 15×. Pure k⁶ growth would give 15⁶ = 1.14×10⁷, a factor of 140 larger. The implied exponent is log(8.15×10⁴)/log(15) = 4.18, not 6. Either the endpoints or the "k⁶" attribution is wrong.

(b) **The bound is not reconstructible.** No relation between |T_c − 1| and δf_NL is given anywhere. Interpolating the quoted range to kη_B = 10⁻² gives |T_c − 1| ≈ 2.3×10⁻⁷ (measured exponent) or ≈ 4.2×10⁻⁶ (asserted k⁶). Multiplying by |f_NL| = 2.1875 (one leg) or 3|f_NL| (three legs) gives 5×10⁻⁷ to 2.8×10⁻⁵ — one to three orders of magnitude above the quoted 6.8×10⁻⁸. I cannot get 6.8×10⁻⁸ from anything printed. Please display the map from T_c(k) to δf_NL.

(c) **A linear result is being used to bound a cubic quantity.** The calculation described is the transmission of "the Weinberg constant (conserved) **curvature mode**" — a linear-order statement, as the manuscript itself insists everywhere else ("only linear transfer is verified," Sec. II B; "a fully nonlinear third-order branch calculation remains open," Sec. II C). Converting |T_c − 1| into a bound on the correction to a *cubic* amplitude is exactly the nonlinear step the paper repeatedly disclaims. Either derive the relation (in which case some of the cubic-transfer gate is closed and the paper should say so) or withdraw the numerical bound and state only the linear result.

**9. [MAJOR] Misattributed citation for the paper's headline number, contradicting the paper's own Appendix B.**
*Location:* Introduction p.1: "A distinctive pre-bounce result is the negative local amplitude f_NL = −35/16 = −2.1875 **[7–9]**."

Ref. [7] is Cai et al., which by this manuscript's own central claim publishes **−35/8**, not −35/16. Citing [7] as a source for −35/16 directly contradicts Appendix B and the abstract. Ref. [9] is D. Wands, "Local non-Gaussianity from **inflation**," CQG 27, 124002 (2010) — a review of local non-Gaussianity from inflationary models, which does not derive a matter-bounce amplitude at all. Of the three, only Ref. [8] (Li et al., via Eq. 5.1 at c_s = 1) actually supports −35/16, and even that only after the manuscript's own reduction.

Please restrict this citation to what each reference actually states, and consider flagging in the Introduction — not only in Appendix B — that the value in Ref. [7] differs.

**10. [MAJOR] Figure 2 displays four model bands that appear nowhere in the text, carry no citations, no stated ranges and no derivation; one of them is an equilateral-shape model plotted on a local-f_NL axis.**
*Location:* Fig. 2, p.6, rows "Exotic multi-field," "DBI inflation (equilateral)," "Standard curvaton," "Single-field slow-roll."

The caption describes only the blue SPHEREx bar. The other four rows — a wide orange band spanning roughly −7 to +1, a pink "DBI inflation (equilateral shape, not local)" band, a yellow curvaton band spanning roughly −1 to +3, and a green slow-roll point — have no source, no defining parameters, and no discussion in the body. The body text (Sec. VI A) mentions curvaton and non-attractor models in one sentence with a single citation [18] that covers only the +5/2 non-attractor value.

Separately, plotting a DBI/equilateral model on an axis labelled f_NL^local is a category error even with the parenthetical annotation, since equilateral and local amplitudes are not commensurable numbers. The manuscript says so itself two sentences earlier ("Non-canonical single-field models (DBI, etc.) produce equilateral-shape f_NL, not local").

Please either supply the parameters and citations for every band (and remove the equilateral row or move it to a separate panel), or reduce Fig. 2 to the elements the paper can defend.

**11. [MAJOR] Roughly half the manuscript is explicitly disclaimed by its own author as not constituting a result.**
*Location:* Abstract ll. 22–24; Introduction ll. 30–34, 44–46; Sec. III B p.4; Sec. IV p.4; Sec. V p.5; Sec. VII p.6; Sec. IX p.8; Sec. X p.8; Appendix A p.8.

Non-exhaustive inventory of self-disclaimers: "illustrative conditional diagnostics, not an observational headline, a new joint-covariance forecast, or a detection forecast" (abstract); "The observational numbers are illustrative conditional mappings, not a unified or independent survey forecast" (Intro); "not a paper headline, an independently reproduced SPHEREx likelihood, or a detection forecast" (Sec. IV); "This is an outlook only and is not used in the abstract, conclusion, or evidence claims" (Sec. V); "The observational material is an illustration, not a second headline result" (Sec. IX); "This is not a forecast or model-selection result… the scans are therefore retained only as provenance artifacts" (Appendix A).

The candour is genuinely commendable and I want to credit it. But the consequence is a Research Article in which Secs. III, IV, V, VI, VII, VIII, IX and Appendix A — pages 4 through 8 — are declared by the author not to be results. Appendix A in particular describes a Bayes-factor scan, reports no Bayes factors, and states the scan is not a model-selection result; it should simply be deleted. PRD readers and editors will ask what the article contributes beyond Appendix B.

My recommendation, offered constructively: either (i) reduce the observational material to a short, fully specified section that *does* claim something (which requires closing Findings 3, 5, 6, 7), or (ii) cut Secs. III–VIII and Appendix A entirely and submit the algebraic result — which is correct and is worth publishing — as a **Comment on Cai et al.**, PRD Brief Report, or equivalent. Option (ii) is a clean, publishable paper today. Option (i) is a substantially larger project.

**12. [MAJOR] Table II's "local observer" row states f_NL^inf → 0⁺, which overstates Refs. [3, 4].**
*Location:* Table II, p.6.

Refs. [3, 4] show that the *leading* single-clock consistency-relation contribution to the observed squeezed bispectrum is cancelled by projection/coordinate effects, leaving residuals that are parametrically suppressed but nonzero, and that genuine relativistic projection contributions remain. Writing "→ 0⁺" in a table cell, and then a ratio of "≫ 146," asserts an exact cancellation that the cited works do not establish. The manuscript's own body text is more careful ("leaving parametrically smaller slow-roll and projection residuals"); the table is not. Please replace "→ 0⁺" with the actual parametric scaling of the residual, or with a citation-backed magnitude.

Note also that this interacts with Finding 3: the very same relativistic projection terms are modelled in the paper's own surrogate Fisher via the amplitude A_GR, whose marginalization *degrades* the bounce sensitivity from 3.47σ to 3.14σ. The paper therefore already knows projection terms matter for the bounce channel — which makes leaving the bounce entry untouched in Table II harder to justify.

**13. [MAJOR] Table II is captioned as the "quasi-dust matter bounce" but reports the exact w = 0 value, whose quasi-dust correction the paper states is unquantified.**
*Location:* Table II caption, p.6: "Expected squeezed-limit local f_NL for the **quasi-dust** matter bounce…"; cf. Sec. VI B p.6: "The quasi-dust correction is presently unquantified because its coefficient requires evaluating all four cubic integrals with quasi-dust mode functions"; Sec. II D p.4.

The paper's viable model (Sec. II D) has w = −0.003, not w = 0, and the paper is emphatic that the quasi-dust correction to f_NL has not been computed. Presenting −2.1875 to five significant figures in a table captioned "quasi-dust" is therefore not supported. Either relabel the row "exact matter limit (w = 0)" or attach the unquantified-correction caveat inside the table.

This compounds a real gap: the paper's *only* concrete model realization (Wilson–Ewing quasi-dust, used to fit n_s = 0.964) is one for which the paper's central number has explicitly **not** been computed. A referee will ask how a percent-level departure in w, which shifts n_s by 3.6%, is known to leave the cubic amplitude at −35/16. "Existing scaling arguments suggest percent-level changes" (Sec. II C) is asserted without citation or derivation.

### MINOR

**14. [MINOR] The gradient-expansion integral K = ∫z²dη is not defined, and d_cut never is.**
*Location:* Sec. II C, p.3: "in the effective-fluid variable (z ∝ a/c_s) the corresponding gradient-expansion basis integral K = ∫z²dη diverges as d_cut^(−1/2) at the H = 0 pole (fitted exponent −0.4998 against the analytic −1/2)".

Three problems: (i) the object controlling constant-mode/decaying-mode mixing in Mukhanov–Sasaki form is conventionally ∫dη/z², not ∫z²dη — if the latter is intended, say why; (ii) `d_cut` is introduced without definition (a cutoff in what variable, with what units?); (iii) the integration limits are not given, so the "divergence" is not a well-posed statement. A single sentence defining K, its limits, and d_cut would fix this.

**15. [MINOR] The growth-factor normalization convention in Eq. (8) conflicts with the cited source and risks a ≈30% error in ∆b.**
*Location:* Sec. III A, p.4, Eq. (8) and the surrounding text: "D(z) is the linear growth factor (**normalized to D(0) = 1**)"; citing Refs. [11, 15].

The form M(k,z) = 2k²T(k)D(z)/(3Ω_m H₀²) as given by Slosar et al. (Ref. [15]) uses a growth factor normalized so that D(z) → 1/(1+z) during matter domination, not D(0) = 1. In ΛCDM the two conventions differ by g(0)/g(∞) ≈ 1.3, and mixing them is a well-known ~30% trap in scale-dependent-bias forecasts. With D(0) = 1 as stated, Eq. (8) does not reduce to the Slosar form. Since Eqs. (6)–(8) are declared canonical for "All downstream Fisher weightings, plots, and forecasts," this propagates into every σ in Sec. IV and Table III. Please state the convention explicitly and confirm which one the scripts use.

**16. [MINOR] "Bounded explicitly" overstates what Eq. (5) provides.**
*Location:* Sec. II C p.3: "(f) fermion-sourced torsion negligible during contraction and the bounce—**now bounded explicitly** below rather than assumed"; contrast with the same section's own parenthesis, "(an **asserted** energy-density transfer proxy, |δf_NL^tor| ≲ |f_NL| ρ_tor/ρ, **not a derived in-in propagation** of the four-fermion operator)".

The manuscript is admirably explicit that the proxy is asserted, and then calls the result a bound anyway. An order-of-magnitude estimate built on an asserted proxy plus an assumed spin-coherence relation ⟨J₅²⟩ ≲ n_ψ² is an estimate, not a bound. Please use "estimated" consistently, in Sec. II C and wherever assumption (f) is referenced.

**17. [MINOR] The claim n_ψ,c ∼ 3×10⁻² M_Pl³ is not traceable from printed quantities.**
*Location:* Sec. II C, p.4: "The correction reaches the earlier δf_NL ∼ 10⁻³ order-of-magnitude reference level only for n_ψ,c ∼ 3×10⁻² M_Pl³".

Eq. (5) gives δf_NL in terms of x_ψ ≡ κn_ψ,c²/ρ_c, but the manuscript never states ρ_c (in LQC typically ≈ 0.41 ρ_Pl, but this is not said), never states which Planck-mass convention M_Pl denotes (reduced or not — the two differ by √(8π) and hence by ~10³ in n = M_Pl³), and never fixes γ for this particular statement. Working backwards, I obtain n_ψ,c ranging from ≈4×10⁻² to ≈1.4×10⁻¹ M_pl³ depending on γ and the ρ_c convention. Please state ρ_c, the M_Pl convention, and the γ used.

**18. [MINOR] "Unique coefficients" is convention-dependent, and the manuscript proves this itself.**
*Location:* Abstract l. 13 ("obtain the **unique** coefficients (3, 1, −9, 5, −33, 9)"); Eq. (4) p.2 ("The coefficient vector is therefore **uniquely**"); Sec. IX p.8.

Uniqueness holds only relative to a fixed basis convention. The whole of Sec. II A and half of Appendix B is devoted to showing that the (5,2,2) orbit admits two natural readings differing by a factor of two (−33 over six ordered triples vs. −66 over three distinct monomials), and Eq. (B4) uses the *other* convention (−198 over Σ^dist) for the same quantity. The coefficient vector is therefore unique *given* the ordered-basis convention, which is precisely the thing in dispute with the literature. Please qualify: "unique in the ordered symmetric basis defined in Eq. (3)."

**19. [MINOR] r_eff is described as "not the bare σ ratio," and then illustrated with the bare σ ratio, which numerically equals it.**
*Location:* Sec. IV, p.5: "with survey-weighted Fisher recovery r_eff = 0.9929 and 0.9986, respectively (**a covariance-weighted information cosine, not the bare σ ratio**, e.g. 0.626/0.631 = 0.992)."

0.626/0.631 = 0.9921 and the quoted r_eff = 0.9929 agree to 0.08%. The example therefore illustrates the opposite of the point it is making. Either give the defining equation for r_eff (preferred) or drop the parenthetical.

**20. [MINOR] Sec. III C makes an unsupported comparative robustness claim.**
*Location:* Sec. III C, p.4, in full: "The galaxy bispectrum provides an independent measurement channel that accesses information at shorter wavelengths, reducing the dependence on ultra-large-scale modes [1]. This makes bispectrum-based constraints **more robust to large-scale systematics** than power-spectrum-based scale-dependent bias alone."

The second sentence is a substantive claim about relative systematic robustness of two estimators, carrying no citation and no supporting analysis. It is also in tension with Sec. VII, which lists "photometric-redshift outliers" and "non-Gaussian covariance terms" among the dominant unmodelled effects — both of which affect the bispectrum channel. Either support it or soften it.

**21. [MINOR] Internal revision history appears in the submitted text.**
*Location:* Sec. II A p.2 ("**The earlier three-benchmark fit** mistook this bookkeeping redundancy for a physical coefficient uncertainty"); Sec. IX p.8 ("This resolves the **earlier artificial coefficient freedom**"); Data and Code Availability p.8 ("**The retired benchmark-fit coefficient scan** is not used or distributed as an uncertainty model"); Sec. II C p.3 ("more than four orders of magnitude below **the earlier order-of-magnitude residual**"); Appendix A p.8 in its entirety.

A submitted manuscript should describe what it does, not what previous unpublished drafts of itself did. "The earlier three-benchmark fit" has no referent for a reader encountering this paper for the first time. Please remove all references to superseded internal versions.

**22. [MINOR] The archival deposit named in the Data Availability statement is explicitly not the submitted manuscript.**
*Location:* Data and Code Availability, p.8: "That deposit archives the reviewed **v1.7.125** release PDF and source (the exact bytes reviewed at that release); the present manuscript is **v1.7.130, 5 patch releases ahead**, and will be added to the same Zenodo record as a new version on the next re-stage."

A data-availability statement that points to a DOI while stating that the DOI does not contain this version defeats its own purpose. Re-deposit before resubmission and cite the version DOI corresponding to the submitted manuscript.

**23. [MINOR] A load-bearing supporting claim rests on a non-peer-reviewed, non-arXiv, self-deposited companion.**
*Location:* Sec. II C p.3 ("…follow the standard Einstein–Cartan–Holst result [13] **as convention-audited in the companion paper [14]** (reproduced here to 0.1%)"); Ref. [14], p.11, which states of itself: "it is not an arXiv preprint and the paper is not peer reviewed."

The four-fermion coefficient −(3κ/16)[γ²/(1+γ²)] should be sourced to Ref. [13] (Freidel, Minic & Takeuchi) directly, with the conventions stated inline. A Zenodo-only self-deposit that announces its own non-peer-reviewed status cannot carry a convention audit for a PRD submission.

**24. [MINOR] The 30% b_φ theory prior — an entire row of Table III and a number in the abstract — has no citation.**
*Location:* Sec. IV p.5: "a declared 30% Gaussian theory prior on b_φ (**an illustrative benchmark bracketing typical assembly-bias departures from the universal-mass-function b_φ**, not a first-principles bound)"; Table III row 3; Abstract l. 21.

The "typical assembly-bias departures" being bracketed are measured quantities in the literature (separate-universe b_φ calibrations and their assembly-bias dependence), and none of that literature is cited anywhere in the manuscript. Since this prior is the sole difference between the 2.32σ and 0.42σ rows — i.e. between "interesting" and "nothing" — it needs a citation-backed justification or the row should be removed.

**25. [MINOR] The manuscript never discusses the anisotropy (BKL) instability of a matter-dominated contraction.**
*Location:* absent; would belong in Sec. II C Assumptions or Sec. II D.

Anisotropic shear grows as a⁻⁶ in a contracting universe and generically dominates a w = 0 background, which is the best-known objection to the matter-bounce scenario. The manuscript's assumption list (a)–(f) does not mention it. At minimum a sentence and a citation acknowledging the assumption of an isotropic contraction is required.

**26. [MINOR] The time-integration convergence and cutoff-independence of the vertex contributions is never discussed.**
*Location:* Appendix B, pp.8–10.

Table IV consists of momentum polynomials with all conformal-time dependence already integrated out. In a matter contraction, ζ grows as |η|⁻³, so the in-in time integrals are dominated by the end of contraction and are potentially sensitive to where they are terminated (η_B, the bounce time). Since the manuscript's whole thesis is that a factor of two in this result is in dispute, and since a cutoff-dependent contribution is a natural place for such a factor to hide, the paper should state explicitly whether the four vertex integrals converge as η → 0⁻ and whether the quoted result is independent of the termination. Currently a reader cannot tell, because no time integral appears.

**27. [MINOR] The ±0.02 spread on r is never propagated into any quoted significance.**
*Location:* Eq. (10) p.4; Sec. IV p.4; Sec. X p.8.

The manuscript adopts r = 0.84 ± 0.02 and then reports "2.63σ" with no uncertainty. Propagating the stated spread gives 2.56σ–2.69σ. Since the paper is otherwise scrupulous about not quoting unbacked precision, it should either propagate this or say why it does not.

**28. [MINOR] The AI usage disclosure is disproportionate and partly argumentative.**
*Location:* "AI USAGE DISCLOSURE," p.8, approximately 40 lines.

Disclosure is appropriate and required. However, this section occupies most of a page, names specific vendor model versions, and reads in substantial part as a methodological defence ("What remained with the author is the scientific content…", "Findings raised by the AI reviewers were adjudicated individually against the source and the artifacts, not adopted on the reviewer's authority"). It also describes commercial LLMs as having served as "independent cross-checking and adversarial referee-style reviewers," which readers may reasonably read as a claim of prior peer review. I recommend reducing this to three or four sentences stating what tools were used for what, and the author's assumption of full responsibility — which is the substance PRD's policy asks for.

### NIT

**29. [NIT] Bibliography capitalization is broken throughout.**
*Location:* References, pp.11–12. Examples: "Measuring **fnl** with the **spherex** multi-tracer redshift space bispectrum" [1]; "**Non-gaussian** features" [2]; "Cosmology with the **spherex** all-sky spectral survey" [10]; "**non-gaussianities**" [11]; "**dESI** DR1 LRG combined PNG constraint" [20]; "**dESI** QSO assembly-bias PNG analysis" [21]. "Dore" should be "Doré" in [1], [10], [11].

**30. [NIT] Several references are missing publication years or volume/page data.**
*Location:* Ref. [2] "JHEP 0305, 013" (no year); Ref. [8] "JCAP 03, 031" (no year — 2017); Ref. [12] "JCAP 1303, 026" (no year); Ref. [20] "J. Cosmol. Astropart. Phys. (2024)" (no volume, no article number).

**31. [NIT] Explanatory notes are embedded inside reference entries.**
*Location:* Refs. [14], [20], [21]. E.g. [20] contains "dESI DR1 LRG combined PNG constraint; f_NL^loc = −3.6+9.0/−9.1; σ ≈ 9–10" inside the bibliography entry. These belong in the body text (Sec. VIII), not in the reference list.

**32. [NIT] Raw repository file paths are typeset inline in the body text.**
*Location:* Sec. II C, p.3: `research/cubic_bounce_transmission/g1_dressedmetric_ic_close.py`, `research/cubic_bounce_transmission/g1_dressedmetric_ic_close.json`, `research/cubic_bounce_transmission/g3_torsion_fourfermion_bound.py`; also several in Appendix B (`scripts/caili_certification/cai_conv.py`, etc.).

These break badly across lines in the two-column format and interrupt the physics. Move them to the Data and Code Availability section, which already lists most of the other scripts.

**33. [NIT] Grammatical slip in the abstract.**
*Location:* Abstract, ll. 12–13: "…by re-summing all four cubic vertices, **re-expand** the result in the ordered symmetric basis, and obtain…". Should be "re-expanding … and obtaining".

**34. [NIT] "Doubly parity-protected" is used without defining which parity.**
*Location:* Sec. II C, p.3: "the Weinberg constant (conserved) curvature mode continues smoothly—and, for the symmetric bounce, **doubly parity-protected**—through the bounded transition".

From context this appears to mean symmetry under η → −η about the bounce, not spatial parity. Since the same paragraph also discusses "an odd-parity or asymmetric completion," the ambiguity should be removed.

**35. [NIT] The "Scope and conventions" block preempts the Introduction.**
*Location:* Sec. I, p.1, first paragraph.

The article opens with a dense caveat-and-notation block ("Here r denotes amplitude recovery, r_eff the survey-weighted recovery check, r_cos the shape cosine, and ρ a Fisher correlation") before the physics introduction begins mid-paragraph at "The inflationary paradigm provides a remarkably successful framework…". Consider moving scope/conventions to the end of Sec. I or into a short subsection so the Introduction reads as an introduction.

**36. [NIT] The Planck value should be quoted with its estimator.**
*Location:* Sec. VIII, p.6: "Planck PR4/NPIPE reports f_NL = −0.1 ± 5.0 [19]."

PR4 papers report several local-f_NL estimates (differing by estimator, mask, and whether the lensing–ISW bias is subtracted). Please state which is quoted.

---

## Closing remarks

I want to be clear about the shape of this report, because the finding count alone would misrepresent it.

The algebra in this manuscript is **correct**. I checked every displayed equation and every table entry that admits a check — Eqs. (1)–(4), (B1)–(B5), Tables I, IV and V, the ε-order decomposition, the dimensional analysis, and every piece of downstream arithmetic including the Fisher-marginalization consistency ρ(f_NL, A_GR) = −0.4264 ⇒ 0.697 — and found no error. Table IV's four rows sum exactly to Eq. (1). Table V's per-vertex squeezed and equilateral columns each reproduce individually and sum exactly to −35/16 and −255/128. The squeezed expansion is exactly −35/16 + (35/64)k₁²/k². That is a genuinely clean piece of symbolic work and the author deserves credit for it, as well as for a level of self-disclosure about limitations that is rare and that made this manuscript unusually efficient to referee.

What prevents acceptance is not the mathematics. It is three things.

First, the manuscript's headline claim — that a published literature value is wrong by a factor of two — is supported by re-summing transcribed expressions from the paper being corrected, against two independently printed polynomials that agree with each other. No independent in-in derivation is performed, and the single alternative explanation (a convention mismatch in the author's own reading) is dismissed in one sentence. An independent derivation from the cubic action would settle this in a way nothing else will, and would convert this from a contested transcription dispute into a solid, citable result. I would strongly encourage the author to do it: given the quality of the symbolic work already demonstrated, it appears to be within reach, and it would transform the paper.

Second, the observational half applies the squeezed-limit projection argument to inflation but not to the bounce, without ever establishing the consistency-relation status of a single-clock matter contraction. That gap sits underneath Table II, Sec. VI, and the "≫ 146" contrast repeated in the Introduction. It must be closed before any of the comparative claims can stand.

Third, a number of load-bearing quantities — including both numbers in the abstract (r, r_cos), the undefined r = 0.876, the entire Fisher ladder, and the 6.8×10⁻⁸ transmission bound — cannot be reconstructed from the text. I attempted r and r_cos under four natural conventions and reproduced none of them; I could not obtain 6.8×10⁻⁸ from the quoted |T_c − 1| under any relation I could construct; and the stated k⁶ scaling is inconsistent with the paper's own quoted endpoints (implied exponent 4.18). Committed scripts are welcome, but a PRD article must be reproducible from its own pages.

**I would also urge the author and editor to consider a structural alternative.** By the manuscript's own repeated declaration, Secs. III–VIII and Appendix A are not results. If Findings 3, 5, 6 and 7 cannot be closed with a fully specified survey forecast, the strongest version of this work is a short Comment or Brief Report containing Sec. II A, Sec. II B, and Appendix B, with the observational material removed entirely. That paper would be correct, tightly scoped, and publishable after addressing Findings 1, 2, 4, 9, 18 and 26. The present twelve-page form asks the reader to weigh five pages of explicitly disclaimed material, and the algebraic contribution is weaker for the company it keeps.

**Verdict: MAJOR REVISIONS.**

**Finding counts:** ESSENTIAL 3 · MAJOR 10 · MINOR 15 · NIT 8 · **total 36.**
