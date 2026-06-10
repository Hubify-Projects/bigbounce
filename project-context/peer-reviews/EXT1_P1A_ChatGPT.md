# EXT1 P1A — ChatGPT Pro Extended referee report
**Provider**: chatgpt.com web app (Big Bounce Book project) · intelligence **Pro Extended** (GPT-5.5)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e5e8-96cc-83e8-918f-3b1dd3f96d96
**PDF**: paper1a_ech_nogo_v1A.0.56.pdf (md5 96f18a36) · **Harvested**: 2026-06-10T17:05 PDT

---

Show more
Thought for 12m 0s
Referee report — Paper 1A v1A.0.56

File reviewed: paper1a_ech_nogo_v1A.0.56.pdf. I read the full 26-page PDF. Line references below use PDF page plus extracted-text line/paragraph locations because the source .tex file was not included in the upload; I grepped the on-disk PDF text extraction rather than relying only on the prompt. 

paper1a_ech_nogo_v1A.0.56

Recommendation: REJECT

This is not publishable in its present form for MNRAS, PRD, or JCAP. A substantially shorter and more disciplined resubmission could be viable if it is rebuilt around the strongest result — classical perturbation transparency of minimal ECH for canonical scalar matter — and if the remaining “dark-energy route closure” claims are demoted to a clearly labelled phenomenological audit. The current manuscript still overclaims relative to its own caveats: the dark-energy mapping is not a controlled EFT, two route closures use ansatz operators rather than derived calculations, Route 4 is explicitly not an amplitude no-go, the reheating-reset argument lacks the required kinetic calculation, and the advertised reproducibility bundle does not match the current manuscript.

I am not rejecting for the calibrated non-issues: I do not object to 2025/2026 arXiv identifiers as such; I do not object to transparent correction notes; I do not object to “posted concurrently” placeholders if the paper is submitted as part of a coordinated package. The problems below are substantive.

BLOCKERS — must fix before publication
B1. The central dark-energy map is not a valid EFT result, yet it still supports headline claims

Location: Sec. II A 2, Eq. (5)–(7), p.6; Sec. II C, Eq. (10), p.7; Appendix B, Eq. (B1)–(B2), p.23.

The manuscript openly states that the leading parity-odd operator has off-shell mass dimension +1 rather than the +4 required for a local Lagrangian density, and that the relation

ρ
Λ
bounce
	​

∼(α/M)M
Pl
5
	​

∼10
−2
M
Pl
4
	​


is a phenomenological on-shell scaling ansatz, not a controlled EFT result. That caveat is welcome, but the paper then uses the same ansatz to motivate N
tot
	​

, the “fine-tuning reduction,” the dark-energy route closure, and the structural tension with f
NL
	​

. This is too central to remain an admitted dimensional patch. 

paper1a_ech_nogo_v1A.0.56

Proposed fix: Either remove the dark-energy derivation and present the paper as a negative phenomenological audit plus a perturbation-transparency theorem, or provide a genuine dimension-4 local EFT construction: operator basis, coefficient normalization, renormalization scheme, counterterms, and an explicit derivation of the vacuum-energy mapping. Do not call Eq. (5)–(6) an “effective action” for dark energy unless it is dimensionally and variationally well defined.

B2. The four-route “closure” is not demonstrated at the level claimed

Location: Sec. IV, especially Sec. IV scope paragraph, p.9–10; Sec. IV B–C, Eq. (14)–(16), p.10–11; Sec. IV E, p.12.

The paper correctly admits that the four routes are a channel-level enumeration, not a complete operator basis; it also says R1 and R4 are not logically independent at the dimension-6 operator level and that important parity-odd operators are not enumerated, including the Jackiw–Pi gravitational Chern–Simons term and a parity-odd four-fermion partner. Yet the title, abstract, and conclusions still read as if the minimal-ECH dark-energy sector is closed in a broad sense. 

paper1a_ech_nogo_v1A.0.56

The problem is sharper for R2 and R3. R2 explicitly uses an operator whose exact coefficient structure is not derived in the cited literature, and the paper calls it an “upper-bound EFT ansatz.” R3 uses an RG equation that the paper itself says is a chiral-count ansatz, not the Benedetti–Speziale result. Benedetti & Speziale do compute the one-loop effective action with Immirzi dependence; their result is not the simple Eq. (16) and includes four-fermion interactions with a beta-function sign depending on ∣γ∣. 

paper1a_ech_nogo_v1A.0.56

 

paper1a_ech_nogo_v1A.0.56

 
arXiv

Proposed fix: Replace “four-route no-go theorem/closure” by “four-route phenomenological audit.” For R2/R3, either supply explicit loop calculations or state that no derived minimal-ECH amplitude is available and that the estimates are conservative ansätze. Add a table separating: derived result, cited literature result, paper’s ansatz, and conclusion supported.

B3. Route 4 directly contradicts the headline “each fails at the amplitude level” claim

Location: Abstract, p.1; Sec. IV D–E, p.11–12; Conclusions, p.22.

The abstract says the four minimal-ECH channels each fail at amplitude level, but Sec. IV D says Route 4 is not closed by amplitude mismatch. With α/M treated as a free parameter, the spectator-ALP class can reproduce both β
obs
	​

 and ρ
Λ
	​

; the closure is only a naturalness or explanatory-deficit objection. The paper eventually says exactly this, but the title/abstract/conclusion have not been consistently updated. 

paper1a_ech_nogo_v1A.0.56

Proposed fix: Rewrite the headline claim as: “R1–R3 are amplitude-suppressed under the stated ansätze; R4 is non-predictive/naturalness-limited unless an external ALP mass and photon coupling are supplied.” Do not count R4 as an amplitude no-go except under the rigid one-loop matching assumption.

B4. The reheating thermal-reset argument is physically plausible but unsupported

Location: Sec. II C 1, “Reheating thermal-reset barrier,” p.8; also Sec. XII A, p.19.

The manuscript correctly emphasizes that minimal ECH torsion is sourced by the axial-current expectation value ⟨J
5
μ
	​

⟩, not by total fermion number density n
ψ
	​

. That is an important and good correction. But the paper then asserts that C/P-violating scattering rates at reheating exceed H and erase coherent axial polarization, without showing rates, species content, chemical potentials, sphaleron/chirality-flip processes, or a Boltzmann/thermal-field-theory calculation. 

paper1a_ech_nogo_v1A.0.56

Proposed fix: Add a real thermal-reset calculation: define the axial charge/current being tracked; compute Γ
washout
	​

(T) versus H(T) for relevant species; specify whether chirality, helicity, spin polarization, or axial charge is being erased; include sphaleron and Yukawa rates where appropriate; and estimate the residual mean and variance. If this is not done, downgrade the reset to a conjectural caveat, not a barrier.

B5. ALP notation is dimensionally inconsistent

Location: Sec. IV D, Eq. (17), p.11–12; Appendix C, Eq. (C1)–(C4), p.23–24.

The paper writes the photon coupling as

−
4
1
	​

(α/M)θF
μν
	​

F
~
μν
,

which requires θ to have mass dimension 1 if α/M has dimension −1. But Appendix C then uses a potential m
θ
2
	​

f
2
(1−cosθ), where θ is dimensionless. The text later maps to the canonical ALP notation Δθ=Δϕ/f
a
	​

, which confirms that two conventions are being mixed. This affects Eq. (17), the inferred ρ
θ
	​

, and the Route-4 mass/coupling naturalness discussion. 

paper1a_ech_nogo_v1A.0.56

Proposed fix: Use one convention throughout. Recommended: write the canonical field as ϕ with

L⊃−
4
1
	​

g
ϕγ
	​

ϕF
F
~
,β=
2
g
ϕγ
	​

	​

Δϕ,

and separately define θ=ϕ/f
a
	​

 only inside V=m
2
f
a
2
	​

(1−cosθ). Then recompute Eq. (17) and the Route-4 numerical estimates.

B6. Data and code availability are not aligned with the current manuscript

Location: Data and Code Availability, p.22; Appendix A/Table IV, p.24; external reproducibility repository.

The paper states that all materials necessary to reproduce the cosmological and galaxy-spin results are publicly available and that the repository includes Cobaya configurations, galaxy-spin code, and an implementation map. 

paper1a_ech_nogo_v1A.0.56

 The linked repository I checked is labelled as a v0.9.0 reproducibility bundle for an older “Geometric Dark Energy” version and lists reproducible numbers that do not match the present paper’s Table IV values; it also states that there are no precomputed MCMC chains and no CMB map analysis in the bundle. 
GitHub
 Its “Known Reproducibility Gaps” file further says there is no bespoke CAMB model, no precomputed chains, no CMB EB/TB map analysis, and that prior free-w
0
	​

w
a
	​

 MCMC output was retracted as bookkeeping confabulation. 
GitHub

Proposed fix: Freeze a v1A.0.56 release, ideally with a DOI, containing exact scripts, environments, figure-generation notebooks, chain files or chain hashes, GetDist outputs, classifier checkpoints or inference products, and the exact inputs for every table and figure. Until then, replace “all materials necessary” with a narrower statement.

B7. Several figures contain known wrong or stale burned-in values

Location: Fig. 1, p.5; Fig. 2, p.6; Fig. 5, p.16; Fig. 6, p.20.

Caption disclaimers do not cure wrong figure content. Fig. 1 still shows the obsolete PTA value γ=3.20±0.42 while the caption says the current value is 2.567±0.382. 

paper1a_ech_nogo_v1A.0.56

 Fig. 2 has a burned-in N≃55, e
−3N
∼10
−72
 waypoint while the quantitative bookkeeping uses N
tot
	​

≃92. 

paper1a_ech_nogo_v1A.0.56

 Fig. 5 still visually advertises a “115 orders of magnitude improvement” even though the text says this is only a reparameterization, not a solution. 

paper1a_ech_nogo_v1A.0.56

 Fig. 6 says both forecasts are decisive at ≳5σ, while the text says the SPHEREx figure is a companion-paper cross-reference and the ALP central value is not an ECH prediction. 

paper1a_ech_nogo_v1A.0.56

Proposed fix: Regenerate all figures. Do not leave incorrect numerical labels in submitted figures with “pending regeneration” captions.

B8. The “fundamental” ECH action is not written as a clean variational principle

Location: Sec. II A 1, Eq. (1), p.4–5.

The action is called fundamental but includes a T
abc
T
abc
	​

 term that is then described as a shorthand for the four-fermion contact interaction after integrating out non-propagating torsion, not something varied independently. That is confusing and not acceptable for a theory paper that rests on variational and perturbative statements. 

paper1a_ech_nogo_v1A.0.56

Proposed fix: Split the presentation into two equations: the off-shell Palatini–Holst–Dirac action with independent connection, and the on-shell effective four-fermion action after solving the Cartan equation. Do not put a non-varied shorthand term inside the “fundamental action.”

MAJORS — should fix
M1. The perturbation-transparency result is the strongest part, but the scope must be tightened

Location: Sec. X A–F, p.17–18.

For classical minimal ECH with canonical scalar matter, the logic is basically sound: the scalar has no spin density, the Cartan equation gives zero torsion, the connection is Levi-Civita, and the Holst dual contraction vanishes by the algebraic Bianchi identity rather than by being a Pontryagin density. The paper’s correction on this point is good. 

paper1a_ech_nogo_v1A.0.56

However, “all perturbation orders” should be phrased as “all classical metric/scalar perturbation orders around the torsion-free branch.” It should not be allowed to read as a quantum statement or as covering fermion loops, propagating torsion, non-minimal matter couplings, dynamical Immirzi fields, or boundary sectors. The paper lists some exclusions, but the theorem wording remains broader than the proof. 

paper1a_ech_nogo_v1A.0.56

Proposed fix: State the theorem formally with assumptions, then prove it by varying the first-order action and showing that the Holst-modified Cartan equation has the torsion-free solution for spinless matter. Delete or quarantine the “total derivative” step after the pointwise Bianchi identity, because it distracts from the stronger result.

M2. The N
tot
	​

–f
NL
	​

 tension needs a real mode-history derivation

Location: Abstract, p.1; Sec. XIII, p.20–21; Sec. XIV D, p.21.

The claimed tension — N
tot
	​

≃92 needed for the dark-energy ansatz erases a matter-bounce f
NL
	​

=−35/8 signal at SPHEREx scales — is plausible as a scale-separation argument, but the manuscript does not show a full mode-history calculation through contraction, bounce, inflation, reheating, and late-time observation. The paper itself says the matter-bounce f
NL
	​

 result is class-level and not ECH-specific. 

paper1a_ech_nogo_v1A.0.56

Proposed fix: Either provide the mode-transfer calculation or explicitly label this as a heuristic consistency check. Define N
tot
	​

, N
exit
	​

, the bounce scale, and the mapping of SPHEREx k-modes through the whole history. Do not use it as an independent no-go mechanism unless the derivation is included.

M3. Observational claims rely too heavily on unpublished companion papers

Location: Sec. I B, p.4; Sec. V–VII, p.13; Sec. X G, p.18; Sec. XIII, p.20; Conclusions, p.22.

The paper imports MCMC values, NaMaster validation, ALP fits, galaxy-chirality results, NANOGrav real-KDE fits, and SPHEREx forecasts from companion manuscripts that are “posted concurrently” or “in preparation.” That is acceptable as a programmatic placeholder, but not as the evidentiary basis for claims in a standalone journal article. The external SPHEREx bispectrum forecast literature does support σ(f
NL
	​

)≃0.7 in an idealized bispectrum-only forecast, but the paper’s 3–5σ statement depends on companion assumptions. 
arXiv

Proposed fix: In this paper, keep only claims supported by published external literature or by calculations shown here. Move internal MCMC, NANOGrav, galaxy-chirality, and NaMaster statements to a clearly marked “not used in the proof” paragraph unless the companion papers are simultaneously available to referees.

M4. DESI/quintom language is too strong

Location: Introduction, p.3; Sec. XIV D, p.21.

The paper says DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ, which is broadly consistent with DESI DR2 reporting a preference for w
0
	​

w
a
	​

 models at 3.1σ with CMB and 2.8–4.2σ when combined with different supernova samples. 
arXiv
 But the manuscript goes further by saying this lends empirical support to quintom scenarios. That is too model-specific.

Proposed fix: Replace “empirical support to quintom scenarios” with “motivates phenomenological dynamical-dark-energy models, including w
0
	​

w
a
	​

 and quintom-like parameterizations.”

M5. The “structural-incompatibility theorem” language overstates a mixed catalogue

Location: Sec. IV opening, p.9; Sec. IX, p.14–17; Table II, p.15.

Some barriers are calculations or standard decoupling arguments; others are heuristic or philosophical: Liouville conservation, gravitational democracy, UV–IR specificity, attractor sensitivity. The paper acknowledges some assumptions, but still packages the result as a theorem-level closure.

Proposed fix: Use “constraint catalogue” or “mechanism audit” for Sec. IX. Reserve “theorem” only for perturbation transparency, if the proof is tightened as suggested above.

M6. Route 1 is probably right, but the density language should be made precise

Location: Sec. IV A, p.10.

The NJL/contact conclusion is plausible: a late-time four-fermion energy density is Planck suppressed and parity even. But the phrase “largest plausible cosmic fermion densities at recombination or post-recombination” should be narrowed. Early-universe thermal fermion densities can be enormous; the argument only closes late-time coherent dark energy in the minimal contact channel. 

paper1a_ech_nogo_v1A.0.56

Proposed fix: Say “for late-time or post-recombination Standard Model number densities” and separate that from bounce/thermal-era density arguments.

M7. The ALP birefringence benchmark is correctly demoted, but the paper still oversells the forecast

Location: Sec. III A, p.9; Sec. XIII, p.20; Conclusions, p.22.

The paper now correctly says β≃0.27
∘
 is a benchmark consistency point, not an ECH prediction, and that the same setup exists in GR+ALP. That is the right framing. 

paper1a_ech_nogo_v1A.0.56

 The external ACT DR6 follow-up value β=0.215
∘
±0.074
∘
 is a real 2025/2026 result, so it should not be flagged as nonexistent. 
arXiv
 The LiteBIRD forecast language, however, should cite current LiteBIRD cosmic-birefringence forecasts and distinguish a nonzero-β detection from model discrimination among ALP parameter choices. 
arXiv

Proposed fix: Keep β≈0.27
∘
 only as a benchmark. Remove language implying that the central value itself is a prediction; if claiming a spectral or scale-dependent prediction, actually compute it.

M8. The source-language cleanup mostly landed, but headline language has not caught up

Location: Abstract, p.1; Sec. I scope paragraph, p.3; Sec. IV E, p.12; Conclusions, p.22.

The paper contains many appropriate caveats: channel-level not operator-level; ansatz not derivation; companion results not yet peer-reviewable; R4 is naturalness-only. But those caveats coexist with stronger title/abstract/conclusion claims. 

paper1a_ech_nogo_v1A.0.56

Proposed fix: Propagate the cautious language into the title, abstract first sentence, Sec. IV title, and conclusion. A possible title would be: “Phenomenological Constraints on Four Minimal Einstein–Cartan–Holst Dark-Energy Channels and Perturbation Transparency for Scalar Matter.”

MINORS — polish and presentation

Abstract: Too long and overloaded for MNRAS/JCAP/PRD. Move correction history, companion-paper logistics, and most caveats into the introduction.

PACS: PACS numbers are deprecated for most current workflows. Use keywords instead unless the target journal explicitly asks for PACS.

Notation overload: γ is used for Barbero–Immirzi and PTA slope; β is used for birefringence and RG functions. Use γ
BI
	​

, γ
PTA
	​

, β
CB
	​

, etc.

Eq. (15): The denominator and second proportionality are hard to parse dimensionally. Rewrite with a clean definition of every dimensionless ratio.

Fig. captions: Several captions are essay-length and contain correction history. Move correction history to a short note in the text.

Table II: The B8/B14 non-independence is correctly noted but should also be reflected in the count column: “14 catalogue entries, 13 independent.”

Table III: “Quintom-B — consistent” while other rows are “not tested” is confusing because this is theoretical accommodation, not a posterior result.

Sec. X Step 5: “A total derivative contributes nothing…” should be removed or rewritten because the previous step says the Holst contraction vanishes pointwise at T=0.

Acknowledgments: I found no residual Grok/Gemini/ChatGPT log text in the PDF extraction; only a normal Claude acknowledgement remains. That is acceptable, but “all scientific claims were independently verified” is too sweeping given the unresolved reproducibility gaps.

Names/accents: Fix Popławski, Domagała, Gödel, and related LaTeX encoding consistently.

Strengths

The paper is unusually transparent about caveats, prior errors, ansatz status, omitted operators, and companion-paper dependence. This is scientifically healthy, even though the remaining claims still overreach.

The perturbation-transparency observation is a worthwhile result: in minimal ECH with canonical scalar matter, the scalar/tensor perturbation sector should indeed reduce to GR because torsion is not sourced and the Holst contraction vanishes on the Levi-Civita connection by the algebraic Bianchi identity.

The Route-4 reframing is a real improvement: the paper no longer pretends that spectator-ALP birefringence is an ECH prediction and correctly treats β≃0.27
∘
 as a benchmark consistency point rather than a derived torsion signal.

The paper correctly distinguishes axial-current expectation value from total fermion number density in the reheating discussion; this is the right physical quantity for algebraic torsion.

The manuscript’s treatment of the Benedetti–Speziale citation is much improved: it now acknowledges that Eq. (16) is not their result and that their actual computation concerns the perturbative Immirzi dependence with fermions.

Specific requested scrutiny
1. Four-route channel-level closure: not publishable as closure in current form

R1 is the most defensible: the late-time NJL/contact channel is Planck suppressed and parity even. R2 and R3 are not derived closures; they use ansatz EFT estimates. R4 is explicitly not an amplitude closure, only a naturalness objection. The paper’s own scope paragraph concedes non-exhaustiveness and omitted operators, so the correct conclusion is narrower: “these four illustrative channels do not provide a derived minimal-ECH dark-energy mechanism under the stated assumptions.” 

paper1a_ech_nogo_v1A.0.56

2. Perturbation transparency for canonical scalar matter: strong, but scope must be formalized

This is the paper’s best result. With canonical scalar matter, the spin current vanishes; in minimal first-order ECH, torsion is algebraic and vanishes; the Holst term then vanishes on the Levi-Civita connection by the first Bianchi identity. The result should be published only with explicit assumptions: classical, minimal, spinless matter, no propagating torsion, no dynamical Immirzi field, no non-minimal matter couplings, and no boundary/topological sector being used as an observable. 

paper1a_ech_nogo_v1A.0.56

3. Reheating thermal reset via axial-current expectation: right variable, missing calculation

The paper now correctly says the torsion source is ⟨J
5
μ
	​

⟩, not n
ψ
	​

. But it must not claim a barrier until it calculates washout rates and residual coherent axial current. The present text is a plausible argument, not a demonstrated closure. 

paper1a_ech_nogo_v1A.0.56

4. ALP birefringence β≈0.27
∘
: correct benchmark framing, but notation bug remains

The manuscript correctly states that the ALP benchmark is not an ECH prediction and is reproducible in GR+ALP with the same parameters. This passes the conceptual scrutiny. The remaining blocker is the mixed dimensionful/dimensionless ALP field notation in Eq. (17) and Appendix C. 

paper1a_ech_nogo_v1A.0.56

5. External 3-reviewer R-round closures: partially landed

Embedded LLM-log purge: Passed in the PDF text I inspected. No Grok/Gemini/ChatGPT review-log residue was found; only a normal Claude acknowledgement remains.

Scope-language sweep: Mostly landed in body text, but not in the title/abstract/conclusions. The paper still overclaims “closure” relative to its caveats.

Benedetti–Speziale citation fix: Landed substantially. The paper now distinguishes its Eq. (16) ansatz from their actual calculation, and the external record supports the citation correction. 
arXiv

Route 4 naturalness reframe: Landed in Sec. IV D/E, but not propagated consistently into the headline claim that each route fails at amplitude level. 

paper1a_ech_nogo_v1A.0.56

Bottom line

The paper contains one potentially publishable theoretical result — perturbation transparency of minimal ECH for canonical scalar matter — embedded in an overextended dark-energy/no-go narrative. I would reject the current manuscript, but I would encourage resubmission after a major reconstruction: remove or strictly demote the uncontrolled dark-energy ansatz, regenerate stale figures, fix the ALP convention, supply or delete the reheating washout calculation, and retitle the work as a constrained phenomenological audit rather than a structural closure theorem.

Sources

Pro Extended

