# P1A R23conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.50.pdf` md5=6208734b pages=23
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (10437 chars)
**Wall time**: 593.1s

---

Referee report on “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”

Scope of review and standard
- Journal: Physical Review D
- Role: Methodology referee (statistical/derivational rigor, dimensional analysis, internal consistency, significance accounting, figure/table audit).
- I read the full 23-page manuscript, including equations, tables and figure captions, and recomputed or sanity-checked all stated scalars.

General assessment
The manuscript advances a “channel-level” no-go for four specific routes to dark energy within the minimal Einstein–Cartan–Holst (ECH) framework and states a “perturbation-transparency” result (Holst sector decouples for canonical scalar matter). The transparency statement is essentially correct and well known in EC/Palatini circles (torsion is algebraic, vanishes for scalar matter; Holst dual contraction vanishes on torsion-free Levi–Civita by the algebraic Bianchi identity). However, much of the paper’s quantitative content relies on phenomenological ansätze and on non-public “companion” works. Multiple core formulae and amplitude estimates are heuristically assembled; one key ratio (Eq. 15) mixes normalizations ambiguously. The action in Eq. (1) is not consistently formulated for a first-order torsionful theory. A number of “barriers” are stated without sufficient derivations or citations and with undefined symbols. The manuscript includes version-history prose and internal project bookkeeping that do not meet PRD standards. In its current form, the paper does not reach the methodological rigor required for PRD.

Below I list specific findings, each with a classification, location, the problem, and the required fix.

Findings

ESSENTIAL

P1A-E1
- Location: Sec. II A 1, Eq. (1), p. 5
- Problem: Action inconsistency. The written action SECH includes “+ (1/4) TabcTabc” while simultaneously treating torsion as a non-propagating auxiliary field to be integrated out. In minimal Einstein–Cartan–Holst, torsion has no independent kinetic term; a specific quadratic T^2 structure only appears after integrating out torsion and depends on the matter content/couplings. Including a fixed-coefficient T^2 at the level of the fundamental action is not standard and conflicts with subsequent statements that it “is a shorthand for the four-fermion contact interaction obtained after integrating out the non-propagating torsion.”
- Required fix: Present a consistent first-order (Palatini) action with independent spin connection and no ad hoc T^2 term; then explicitly integrate out torsion to obtain the four-fermion term, with all coefficients shown (including the Holst γ-dependence). Alternatively, if you choose to start directly with an effective action after integration, remove the T^2 term from Eq. (1) and present the effective four-fermion Lagrangian with a clear derivation and references.

P1A-E2
- Location: Sec. II A 2, Eq. (3), p. 6; Sec. IV A, Eq. (13), p. 9
- Problem: Torsion–spin relation and γ-dependence inconsistent. Eq. (3) states Tabc = 8πG Sabc with no γ-dependence, while Eq. (4)/Eq. (13) use the Holst-corrected axial–axial contact with γ^2/(γ^2+1). In Holst-extended EC, the algebraic torsion–spin solution depends on γ; omitting it in Eq. (3) and introducing it ad hoc in Eq. (4) is inconsistent.
- Required fix: Provide the full algebraic solution for torsion in the Holst-extended theory (e.g., following Freidel–Minic–Takeuchi or Mercuri), showing explicitly how γ enters, and derive the four-fermion term from it. Align the normalization of κ, G, and any factors of 2 or π throughout.

P1A-E3
- Location: Sec. II A 2, Eqs. (5–7), pp. 6–7; Appendix B, p. 21
- Problem: Parity-odd operator used as a load-bearing ingredient is not a controlled EFT term. You correctly note the operator in Eq. (6) has off-shell mass dimension +1 (not +4), and you treat the mapping to ρΛ as an on-shell scaling ansatz. However, several subsequent quantitative arguments and “amplitude budgets” rest on this ansatz (e.g., the Ntot ≈ 92 inference and parts of the closure narrative).
- Required fix: Either (i) replace Eq. (6) by a consistent dimension-4 local operator derived from the underlying theory, with all coefficients specified; or (ii) clearly and consistently wall off every conclusion that depends on Eq. (6) as phenomenological conjecture, removing any claims framed as derivations or channel “closures” that rely on it. All numerics tied to Eq. (6) (e.g., Dinf bookkeeping and Ξ decomposition) must be explicitly re-labeled as illustrative only.

P1A-E4
- Location: Sec. IV B, Eq. (14–15), p. 9–10
- Problem: One-loop birefringence ratio algebra/dimensions are unclear and inconsistent. The ratio Δθone-loop/Δθobs is expressed with a mix of H0/MPl and MPl(α/M) and βobs in a way that does not transparently follow from a well-defined operator-to-observable mapping. A straightforward dimensional estimate β1ℓ ∼ (αem/4π)(H0/MPl) yields ∼10−62 when compared to βobs ≃ 6×10−3 rad, not 10−58–10−60 as stated. The appearance of MPl(α/M) in the denominator suggests a comparison to an R4-fitted coupling, but this must be derived and the normalization fixed.
- Required fix: Derive a clean, dimensionally consistent mapping from the stated one-loop operator (Eq. 14) to a rotation angle β accrued between recombination and today, including all factors of MPl, H0, and any necessary line-of-sight integrals. Then recompute Δθone-loop/Δθobs with transparently stated assumptions. If the ratio is intended “relative to an R4 amplitude matched at α/M,” state that explicitly and justify the algebra. Correct the numerical estimate accordingly.

P1A-E5
- Location: Throughout (e.g., Abstract p. 1; Sec. I B p. 5; Secs. III, V–VII, XIII; Table I p. 4; Table IV p. 22; Fig. 4 caption p. 12; Sec. X G p. 16–17)
- Problem: Reliance on non-public “companion” works for essential claims. Multiple key numerical statements (ΛCDM+ΔNeff posteriors; NaMaster validation; SPHEREx Fisher forecasts; NANOGrav KDE reanalysis; galaxy-chirality catalog; ALP MCMC) are deferred to in-preparation companion papers without arXiv IDs. PRD papers must be self-contained or cite publicly accessible sources.
- Required fix: Either (i) provide stable arXiv identifiers for each companion work and restrict in-paper claims to those fully documented therein; or (ii) excise all claims dependent on those companions, or include sufficient methodological and numerical detail in this manuscript to reproduce the stated figures (datasets, likelihoods, priors, number of samples, convergence diagnostics, code versions, etc.). Remove internal chain-status notes.

P1A-E6
- Location: Sec. IX and Table II, pp. 12–15; Abstract p. 1; Conclusions p. 20
- Problem: “13 logically-independent barriers” are asserted without proofs of logical independence. While several barriers are sensible qualitative constraints, you do not provide a dependency graph or mutual-independence argument. You acknowledge B8 is subsumed by B14, but the rest are not justified as independent.
- Required fix: Either (i) provide an explicit demonstration of logical independence (e.g., a dependency matrix or constructive counterexamples showing each barrier is not implied by the others), or (ii) rephrase to “a catalog of constraints” and avoid the “logically-independent” claim. Clarify interdependencies.

P1A-E7
- Location: Sec. IX L (Barrier 12), Eq. (20), p. 15
- Problem: “Vacuum amplification ceiling” ΩGW|bounce ≲ (ρcrit/ρPl)^2 with numerical range 0.07–0.17 is asserted without derivation. The physical meaning of bounding an epochal total GW energy density by the square of a density ratio is unclear and not supported.
- Required fix: Supply a derivation from first principles (e.g., from the quadratic action for tensor modes through the bounce, including transfer functions) or remove the bound and its numbers. If it is an order-of-magnitude heuristic, label it clearly and do not use it as a quantitative constraint.

P1A-E8
- Location: Sec. IX A (Barrier 1), Eq. (18), p. 14
- Problem: Undefined symbols and unsupported scaling. geff ∼ 1/(MPl√|t3|) ∼ H0/MPl is stated; t3 is not defined, and the connection to Poincaré gauge theory mass scales is not derived or cited.
- Required fix: Define all symbols and either derive Eq. (18) in an appendix with proper PGT references or remove the equation and associated numerical estimate.

P1A-E9
- Location: Version-history/internal notes present in body: p. 2 footnote (“Earlier versions of this manuscript erroneously…”), p. 16 footnote 3 (“An earlier version…”), Sec. I B p. 5 (chain counts “will be reported in Paper I(b)”), Table III footnote p. 17 (running chain status), Acknowledgments p. 21 (AI assistant involvement).
- Problem: PRD manuscripts must not include version-history commentary, internal project status logs, or work-in-progress chain statuses in the scientific narrative. The AI assistant acknowledgment is acceptable as an acknowledgment, but the rest is not.
- Required fix: Remove all version-history and internal status text from the main body and footnotes. Keep only standard acknowledgments. If corrections relative to earlier drafts are scientifically important, state the correct result and provide permanent references; do not discuss draft history.

P1A-E10
- Location: Sec. II C 1 (“Reheating thermal-reset barrier”), pp. 7–8
- Problem: The claimed rapid washout of a coherent axial-current background and the scaling of residual fluctuations as √nψ/T1/2 are asserted without derivation or references. The dimensions of the fluctuation scaling are unclear.
- Required fix: Provide a quantitative kinetic-theory or thermal-field-theory derivation for the washout timescale (compared to H) and for the residual ⟨J5μ⟩T statistics, with references. Ensure dimensional consistency. Otherwise, present this as a qualitative plausibility argument only.

MAJOR

P1A-M1
- Location: Sec. IV A, p. 9
- Problem: R1 (NJL) closure presented without a numeric bound. You state ρNJL ∼ κ n^2ψ is “many orders” below ρΛ but do not provide a concrete upper bound using cosmological fermion densities.
- Required fix: Insert a back-of-the-envelope numeric bound (e.g., take nψ at recombination for electrons/baryons, compute ρNJL, and compare to (2.3 meV)^4).

P1A-M2
- Location: Sec. IV C, p. 10
- Problem: R3 (running of γ) estimate Δγ/γ ∼ 10−2 and the resulting suppression (Δγ/γ)(H/MPl) ∼ 10−63 are not derived or properly referenced to a computation (e.g., Benedetti & Speziale).
- Required fix: Provide a calculation or explicit citation that yields Δγ/γ over GUT→IR running for the matter content assumed. Otherwise, weaken the claim to a dimensional upper bound.

P1A-M3
- Location: Sec. IV D, Eq. (17), p. 10–11; footnote 1 p. 10–11
- Problem: The mapping β = (α/M)Δθrec→today ∼ (α/M)√(2ρθ/m2θ) is quoted without derivation and the normalization/basis conversion to the canonical gaγ is treated in a confusing footnote. The argument mixes conventions (−¼ normalization, area-gap mass M, αem loop factor) and ends with an ad hoc “10× basis-conversion gap.”
- Required fix: Provide a clean derivation of β from the Chern–Simons operator L ⊃ −(α/4M) θ F F̃, including the integral over conformal time and the assumption for θ evolution. Then present a coherent conversion to gaγ = (αem cγ)/(2π fa) and explain the relationship to α/M with explicit numerical values. Remove the speculative “10× gap” commentary or support it via a defined UV completion.

P1A-M4
- Location: Sec. II A 3, p. 7
- Problem: “The parent black hole mass must exceed Mcrit ≈ 10−3 M⊙” is stated without citation or derivation.
- Required fix: Provide a reference or a compact derivation showing why this threshold follows from the assumed scenario; otherwise remove.

P1A-M5
- Location: Sec. IX J/K (Barriers 10–11), p. 14
- Problem: These barriers are qualitative/philosophical (UV→IR specificity dilemma; decoupling universality) without concrete derivations or counterexamples/constructions.
- Required fix: Either give formal statements with proofs or frame them as interpretive observations and remove them from the set of putative “closure constraints.”

P1A-M6
- Location: Sec. X B–D, pp. 15–16
- Problem: While the Bianchi-vanishing argument is correct, its presentation is mixed with “total derivative” language and references to Pontryagin density in a way that can mislead.
- Required fix: Present a concise differential-form derivation: e∧e∧R = −NY + T∧T; with T=0, both vanish pointwise. Emphasize the distinction from Pontryagin R∧R̃ which is a 4-form total derivative even with T=0. Remove “total derivative” language for the Holst dual.

P1A-M7
- Location: Table III and its footnote, p. 17
- Problem: The table includes a “PTA γ” line and an extensive footnote about an ongoing chain with R̂−1 ≈ 3×10−2, hardware settings, etc., which are out of scope and unsupported by a citable analysis.
- Required fix: Remove the PTA line and footnote or replace with a published analysis. Remove chain-status commentary.

P1A-M8
- Location: Sec. III B and Sec. V, p. 8 and p. 12
- Problem: Galaxy spin null result is asserted while all methodological details and statistics are deferred to “Paper IV [23] (in preparation).”
- Required fix: Either remove this channel from the present paper or provide enough details to substantiate the null (sample size, classifier performance, dipole estimator, bias tests, uncertainties).

P1A-M9
- Location: Overlength and scope creep, entire manuscript (23 pp.)
- Problem: The core technical content (torsion decouples for scalar matter; Holst dual vanishes at T=0) can be presented succinctly. Large portions of the paper discuss forecasts, companion program, and observational channels without sufficient derivations.
- Required fix: Condense to focus on the theoretical closure arguments you can rigorously support. Recommended maximum length: 12–14 pages, moving programmatic/forecast material to an appendix or a separate, citable companion.

MINOR

P1A-m1
- Location: Notation for Pontryagin, p. 2 footnote and elsewhere
- Problem: Use of “R Re” and mixed notation; should be R∧R̃ or R⋆R with a clear definition.
- Required fix: Standardize notation for Pontryagin density and define it once.

P1A-m2
- Location: Sec. XII A and Appendix B, pp. 17–21
- Problem: Two different headline values for Ntot (≈92 vs ≈94) are discussed. While you explain the difference, the text could be crisper.
- Required fix: Present a single baseline computation (from MPl^4→ρΛ) and then discuss how the phenomenological ansatz shifts it by O(±2) e-folds.

P1A-m3
- Location: Sec. II C 1, Eq. (11), p. 7
- Problem: The prefactor (Treh/MGUT)3/2 is called an “aesthetic” estimate. This is acceptable only if it is not used critically.
- Required fix: Either supply a derivation/citation or explicitly mark every downstream use as illustrative.

P1A-m4
- Location: Figure axes and captions (Figs. 3–6)
- Problem: The captions do not detail axes units and assumptions. (E.g., for the “Hubble Parameter Evolution” and “Detection Significance Forecast” figures.)
- Required fix: Ensure every figure has clearly labeled axes with units and a caption that explains underlying assumptions and inputs.

NIT

P1A-n1
- Location: Spelling and diacritics (e.g., “Pop lawski”)
- Problem: Use standard spelling (Popławski) if possible, or consistently “Poplawski.”
- Required fix: Correct minor spelling/formatting.

P1A-n2
- Location: Hyphenation artifacts from PDF extraction (re￾ports, de￾couples, etc.)
- Problem: Cosmetic artifacts.
- Required fix: Clean in final typeset manuscript.

P1A-n3
- Location: Acknowledgments, p. 21
- Problem: The explicit mention of an AI assistant is permissible but unusual; ensure compliance with PRD policy.
- Required fix: None required if policy allows; otherwise remove.

Audit of quoted scalars
- ρcrit formula (Eq. 9) is correct; with γ = 0.2375 → 0.41 ρPl; with γ=0.274 → 0.27 ρPl; the scaling matches 1/γ^3.
- ω/H bound implies fractional Λ contribution ≲ (ω/H)^2 ≲ 2.5×10−21; your stated ≲10−22 is consistent to O(1).
- βobs = 0.342° ± 0.094° → 3.64σ and ACT 0.215° ± 0.074° → 2.90σ; both consistent.
- LiteBIRD discrimination |0.342−0.27|/√(0.03^2+0.094^2)=0.73σ recomputes correctly.
- Ntot from Ξ ≈ 10−123 with (α/M)MPl ≈ 10−2 yields Dinf ≈ 10−121 ⇒ Ntot ≈ ln(10^121)/3 ≈ 92.1; consistent. From MPl^4 → ρΛ gives ≈94; your statement is consistent.
- Overshoot (mθ/H0)^2 at mθ=10−22 eV is ∼(6.7×10^10)^2≈4.5×10^21 (~22 OOM): consistent.

Bibliography spot-check
- Key references (Hehl et al. 1976; Holst 1996; Freidel–Minic–Takeuchi 2005; Mercuri 2009; Saadeh et al. 2016; Planck 2018; LiteBIRD 2023) are accurate. Newer 2024–2026 citations are plausible but many crucial analyses are “in preparation”; this must be rectified per Essential finding P1A-E5.

## Summary recommendation
REJECT

The central “perturbation-transparency” statement is correct but well known; the rest of the manuscript relies heavily on phenomenological ansätze, ambiguous operator normalizations, and non-public companion analyses. Core equations (the action and the one-loop ratio) are inconsistent or insufficiently derived. Multiple assertions of “logically independent” barriers lack proof, and several numerical “closures” are unsupported. The paper also contains version-history/internal status text not acceptable for PRD. Substantial restructuring, rigorous derivations, elimination of dependencies on in-preparation work, and condensation would be required before reconsideration.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS AFTER SECOND-PASS (A–J AUDIT)

P1A-E11
- Location: Sec. IV B, Eq. (14), p. 9
- Problem (C: dimensional consistency): The stated one‑loop operator Γone-loop ⊃ −(1/16π^2)[β(γ)/MPl] ∫√−g ∂μθ J5μ has the wrong mass dimension. In 4D, ∂μθ carries mass dimension 1 and J5μ carries 3, so the operator needs a dimensionless coefficient for the Lagrangian density to remain mass^4. Your 1/MPl factor makes the coupling dimension −1, rendering the density mass^3. δNY is also introduced later without defined dimension, compounding the mismatch.
- Required fix: Restore dimensional consistency. Either remove 1/MPl and define β(γ) as a dimensionless finite part of a renormalized dimension‑4 operator, or, if an inverse mass scale is truly present, supply an extra mass factor (e.g., 1/MPl → 1/M^2 with a clearly defined heavy scale) so that the total coefficient is dimensionless. Define δNY with explicit mass dimension and origin. Then redo the β prediction and Δθone-loop/Δθobs ratio with consistent units.

P1A-E12
- Location: Sec. II A 2, Eq. (7), pp. 6–7
- Problem (C: dimensional consistency; D: undefined symbols): The estimate α/M ∼ [g^2/(32π^2)] (γ/M) ln(Λ^2/μ^2) + δNY is dimensionally inconsistent unless δNY carries dimension −1 and g is explicitly dimensionless. The mixture of γ/M with a log suggests an EFT threshold-matching term, but the mass dimensions of all terms in α/M must match. δNY is undefined and unreferenced.
- Required fix: Provide a short derivation or citation that yields Eq. (7) with consistent dimensions, define δNY and its mass dimension, and make clear whether M is the LQG area‑gap scale or a generic EFT cutoff. If Eq. (7) is only a heuristic scaling, relabel it as such and wall off all numerical inferences that rely on it.

P1A-E13
- Location: Sec. II C, Eq. (10), p. 6; Fig. 3 caption p. 6
- Problem (C: dimensional consistency; A: arithmetic): Λeff = Ξ MPl^2 + cω ω^2 is presented without defining cω. If cω is dimensionless, ω^2 has dimensions H^2, so cω ω^2 cannot be added to Λ (mass^2) unless you specify a normalization (e.g., Λeff = Ξ MPl^2 + cω ω^2 with cω implicitly ∝ 1/H^2 or with a hidden MPl^−2 factor). The caption then compares cω ω^2 directly to ρΛ, which would require an extra factor of MPl^2 to convert Λ→ρ. The stated “≲10−22 ρΛ” bound implicitly uses (ω/H)^2 ≲ 2.5×10−21; the extra factor ~2.5 mismatch is unexplained and appears to rely on an undefined cω.
- Required fix: Define cω and write the energy density consistently (e.g., ρrot = MPl^2 cω ω^2). Then recompute the bound numerically and state precisely whether you compare Λ or ρ. If an O(1) coefficient reduces 2.5×10−21 to 10−22, specify it.

P1A-E14
- Location: Sec. II A 2, Eqs. (5–6), pp. 6–7
- Problem (C/D: undefined notation and operator content): FIJ[K, R˚] is never defined; in Eq. (6) you then write ε μνρσ eIμ eJν FIJρσ as the “leading contribution.” It is unclear whether F denotes the full curvature of the independent spin connection, a function of contorsion K only, or the Levi–Civita curvature. This ambiguity prevents a meaningful dimensional/variational analysis and conflates topological vs. torsionful content.
- Required fix: Define FIJ precisely (full curvature 2‑form? contorsion-dependent part only?) and state the contraction unambiguously in either forms or components with conventions (signs, indices, ε normalization). Then revisit the dimensional argument tied to Eq. (6).

P1A-E15
- Location: Sec. II A 2, Eq. (4), p. 6; Sec. IV A, Eq. (13), p. 9
- Problem (C: conventions; E: null comparability): The axial–axial contact appears with an overall negative sign, L ⊃ −(3/16) κ (γ^2/(γ^2+1)) (J5)^2. Standard EC conventions often yield + (3/16) κ (J5)^2 (sign depends on metric and γ5 definitions). You do not state metric signature, ε0123, or γ5 convention, making the sign and interpretation (repulsive vs. attractive channel) ambiguous; later text claims “repulsive at γ=0.274,” which depends entirely on unstated conventions.
- Required fix: State your metric, ε, and γ5 conventions and align coefficients with a standard reference derivation. If you retain a nonstandard sign, explain the physical implication and verify downstream claims (e.g., “repulsive”) with that convention.

P1A-M10
- Location: Sec. X F (Implications), p. 16; Abstract p. 1
- Problem (F: abstract faithfulness; H: unquantified hedges): The text repeatedly frames “nonperturbative parity channels (ALP birefringence, primordial GWs) [as] relevant tests of γ.” Cosmic birefringence from L ⊃ θ F F̃ probes the photon–ALP coupling (or a Chern–Simons–like sector), not the Barbero–Immirzi parameter, unless you supply an explicit γ→photon coupling map. No such derivation is given here.
- Required fix: Rephrase to make clear that EB/TB parity tests probe ALP/photon parity-odd sectors generically; they are not tests of γ absent a demonstrated γ→EM coupling. Remove “tests of γ” from the abstract and Sec. X unless you add a derivation.

P1A-M11
- Location: Fig. 6 caption, p. 18 vs. body text Sec. VII (p. 12) and Sec. XIII (p. 18)
- Problem (B: figure-caption vs body-claim; A: arithmetic consistency): The caption states both forecasts are “decisive (≳ 5σ on Stage III/IV survey timescales).” The body repeatedly quotes 3–5σ realistic for SPHEREx after systematics. This is an internal inconsistency in claimed significance levels.
- Required fix: Harmonize the claims. If 3–5σ is your best estimate after systematics, remove “≳ 5σ” from the caption, or else document assumptions that raise it above 5σ and show the arithmetic.

P1A-M12
- Location: Fig. 5 and caption, p. 13
- Problem (B: figure-caption vs body-claim; G: unsupported novelty/values): The “Dark-Energy Fine-Tuning Comparison” panel assigns numerical “fine-tuning scores” (e.g., 10^40 for f(R), 10^60 for quintessence, 10^120 for ΛCDM) without any derivation or references in the body. The caption/body provide no formal definition of the metric plotted, how the numbers were obtained, or error bars.
- Required fix: Define the fine‑tuning metric quantitatively and either derive or cite each bar’s value. Otherwise, remove the numeric bars and keep only a qualitative schematic.

P1A-M13
- Location: Sec. II A 2 (Step 3 and Step 4), pp. 6–7; Sec. IV D, Eq. (17), pp. 10–11
- Problem (I: appendix/main mismatch; D: cross‑sector conflation): The same symbol α/M is used for two distinct sectors: (i) a gravitational Holst/NY‑motivated parity‑odd coupling normalized with the LQG area‑gap scale, and (ii) the photon Chern–Simons ALP coupling. Treating these as numerically identical without a demonstrated mapping conflates unrelated UV physics.
- Required fix: Use distinct symbols (e.g., (α/M)grav vs (α/M)γγ) and state clearly that any numerical identification is an assumption, not a derivation. Redo any amplitude fits or “overshoot” claims that silently equate them.

P1A-M14
- Location: Sec. XIII, p. 18 (birefringence “spectral signature”)
- Problem (H: unquantified hedges; conceptual): The text presents “frequency dependence” as a quantitative prediction for ALP birefringence. For a Chern–Simons coupling with a slowly varying homogeneous θ, the rotation angle is achromatic; frequency dependence is characteristic of Faraday rotation or time‑varying/oscillatory axion scenarios with additional assumptions. No such model is specified.
- Required fix: Clarify that the benchmark EB signal from a homogeneous rolling ALP is frequency independent. If you intend oscillatory/inhomogeneous scenarios that create scale/frequency signatures, state the model and show the predicted dependence.

P1A-m5
- Location: Sec. IV B (classical discussion), p. 9; scattered
- Problem (C: terminology/consistency): The Holst term is described as “topological in vacuum.” With T=0, e∧e∧R is not a topological invariant; it vanishes identically by the algebraic Bianchi identity, while Pontryagin R∧R̃ is the true topological 4‑form. The mixed “total derivative” phrasing appears again later.
- Required fix: Replace “topological” by a precise statement: on a torsion‑free connection, e∧e∧R vanishes identically by the algebraic Bianchi identity; Nieh–Yan is an exact form but requires torsion. Keep Pontryagin terminology separate.

P1A-m6
- Location: Fig. 1 caption vs Abstract/Sec. XIII
- Problem (B: figure-caption vs body-claim): The caption says “the surviving testable prediction is the matter-bounce fNL = −35/8,” but the abstract/body list two surviving mechanism-independent tests (fNL and ALP birefringence).
- Required fix: Make the caption plural or clearly mark ALP birefringence as “not ECH-specific but still testable.”

P1A-m7
- Location: Appendix B, p. 21
- Problem (J: stale/ambiguous notation): The line “MPl^4/ρΛobs ∼ 1019 GeV×4/(10−3 eV)^4 ∼ 10^122” is typographically ambiguous (“×4” looks like multiplication by 4, not exponentiation).
- Required fix: Write explicitly “(10^19 GeV)^4/(10^−3 eV)^4” to avoid confusion.

P1A-m8
- Location: Sec. II C 1, Eq. (11) usage downstream; Sec. XII A
- Problem (E: null‑procedure comparability; H: unquantified hedges): The (Treh/MGUT)3/2 prefactor is called an “aesthetic” estimate yet later used to argue O(0.01–0.1) robustness without a derivation. This is acceptable only if no closure or tension claim relies on it.
- Required fix: Every place the prefactor influences a quantitative claim (e.g., Ntot sensitivity), annotate it as illustrative and provide an uncertainty band showing its impact; or supply a derivation/citation.

P1A-m9
- Location: Sec. III A, Eq. (12)
- Problem (C: assumptions not stated): The EB ≈ 2β(EE−BB) relation assumes small, spatially uniform β and negligible higher‑order terms. The text later mentions “scale dependence” but does not state this assumption alongside Eq. (12).
- Required fix: State explicitly that Eq. (12) is the small‑angle, uniform‑β limit, and note that departures require scale‑dependent treatments.

Explanation of coverage
- I focused on new issues under A–J not raised in the initial review. Many core structural problems (action inconsistency, reliance on non‑public companions, independence claims, heuristic operators, ambiguous one‑loop ratio, undefined symbols, overlength/scope) were already flagged previously and are not repeated here. The new findings add concrete dimensional inconsistencies, cross‑sector conflations, caption–body mismatches, and conceptual misstatements likely to matter for PRD‑level rigor.