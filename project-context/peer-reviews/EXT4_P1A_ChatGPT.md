# EXT4 P1A — ChatGPT Pro Extended (in-thread delta round 4)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e5e8-96cc-83e8-918f-3b1dd3f96d96
**PDF**: paper1a_ech_nogo_v1A.0.61.pdf (md5 6f4384a8) · harvested 2026-06-11 15:50 PT
---
Referee report update — Paper 1A v1A.0.61

Reviewed file: paper1a_ech_nogo_v1A.0.61.pdf, 28 pages, dated June 11, 2026 PDT. I read the full PDF end-to-end and visually checked the rendered pages, including the re-added figures. 

paper1a_ech_nogo_v1A.0.61

1. Closure verification

I treat the v1A.0.60 report as the controlling report for this revision, then give a compact status of the longer-running original blockers/majors from v1A.0.56.

A. Closure against my v1A.0.60 fresh MAJORS
Prior item	Status	Verification
F60-M1. Appendix C still contained a dimensionally wrong ALP mapping sentence	CLOSED	Appendix C now states the correct canonical mapping, β=(α/2M)Δϕ=(αf
a
	​

/2M)Δθ, and the setup uses a dimension-+1 canonical ϕ field with θ=ϕ/f
a
	​

. This closes the normalization bug. 

paper1a_ech_nogo_v1A.0.61


F60-M2. ALP “frequency dependence / scale dependence” contradicted Appendix C	CLOSED	Sec. XIII now says the signature is “achromatic uniform rotation, the EB/TB pattern, and consistency across frequencies and experiments,” which matches Appendix C’s achromatic, no-k-dependence result. 

paper1a_ech_nogo_v1A.0.61

 

paper1a_ech_nogo_v1A.0.61


F60-M3. Data availability not version-clean	CLOSED / minor residual only	The manuscript now explicitly says v1A.0.61 uses the v1A.0.59 bundle unchanged, that frozen MCMC chains are committed, and that fresh re-verification chains must be regenerated. The public README and KNOWN_GAPS.md now agree: frozen chains are committed, fresh proxy chains are not pre-computed. 

paper1a_ech_nogo_v1A.0.61

 
GitHub
 
GitHub
 The only residual is cosmetic: the BibTeX note in the README still says v1A.0.59, but the README header says the paper version is v1A.0.61.
F60-M4. Sec. III still said the parity-odd effective action “generates” CMB birefringence	CLOSED	Sec. III A now says it would generate CMB polarization signatures only if supplemented by a photon-sector coupling, which is not derived here; the quantitative benchmark is explicitly spectator-ALP phenomenology. This is the correct scoped statement. 

paper1a_ech_nogo_v1A.0.61

B. Residual status of older original blockers/majors
Older item	Current status in v1A.0.61
B1. Dark-energy map not a controlled EFT result	PARTIAL — The ansatz status is now admirably explicit, including Appendix B’s statement that a controlled dimension-4 local EFT construction remains a separate companion treatment. That is honest, but the ansatz still underwrites the N
tot
	​

, Fig. 5, and channel-closure narrative. 

paper1a_ech_nogo_v1A.0.61


B2. Four-route closure overclaimed	PARTIAL — The abstract/conclusions are much better, but Sec. IV still says “each route is closed at the amplitude level,” while R4 is naturalness/explanatory-deficit only, and R2/R3 remain ansatz-level. 

paper1a_ech_nogo_v1A.0.61


B3. R4 amplitude contradiction	PARTIAL / mostly closed — R4 is correctly described in Sec. IV D/E as a naturalness objection rather than an amplitude exclusion, but Sec. IV’s opening blanket amplitude language and Fig. 4’s “unique surviving minimal-ECH channel” remain too strong.
B4. Reheating reset unsupported	PARTIAL — It is now conditional, correctly sourced by ⟨J
5
μ
	​

⟩, and the missing Boltzmann calculation is deferred. Still not a demonstrated washout calculation.
B5. ALP notation inconsistent	CLOSED — Canonical ϕ, dimensionless θ=ϕ/f
a
	​

, Eq. (17), and Appendix C are now coherent.
B6. Data/code mismatch	CLOSED — The main numerical values and frozen-chain documentation are now synchronized with the public README and known-gaps file. 

paper1a_ech_nogo_v1A.0.61

 
GitHub

B7. Stale burned-in figure values	PARTIAL / regression via new figure — The old stale values are mostly fixed. However, the re-added Fig. 3 now introduces a new visual inconsistency; see Fresh Major F61-M1 below.
B8. “Fundamental” action includes on-shell shorthand	PARTIAL — The footnote is clear, but Eq. (1) still visually puts the on-shell T
abc
T
abc
	​

 shorthand inside the “fundamental action.” 

paper1a_ech_nogo_v1A.0.61


M1. Perturbation-transparency scope	CLOSED — The pair-exchange chain is removed; the proof now rests on the first Bianchi identity, with appropriate torsion-free/metric-compatible assumptions. 

paper1a_ech_nogo_v1A.0.61


M2. N
tot
	​

–f
NL
	​

 mode-history derivation	PARTIAL — The scale-history ledger and caveat are improved, but the transfer function is still deferred while “definitively erased” remains.
M3. Companion-paper dependence	PARTIAL — Companion imports are now well caveated and not used for the structural proof, but the paper still carries many companion values and forecasts.
M4. DESI/quintom language	CLOSED — Now framed as motivation for dynamical-dark-energy parameterizations outside minimal ECH.
M5. “Theorem/no-go” over broad catalogue	PARTIAL — The paper is more careful, but “Four-Route No-Go” and residual amplitude-closure language still overstate an ansatz-level channel audit.
M6. Route 1 density language	CLOSED — The late-time/post-recombination density regime is now explicit.
M7. ALP benchmark/forecast oversold	MOSTLY CLOSED — The benchmark and LiteBIRD differential comparison are now correct, but “tests of γ” wording remains problematic; see F61-M3.
M8. Scope-language cleanup	PARTIAL — Most body text is scoped correctly; Fig. 1, Fig. 4, Sec. IV opening, and the γ-test phrasing still need cleanup.
2. Fresh pass — new findings only
New BLOCKERS

None. I did not find a new fatal flaw introduced in v1A.0.61.

New MAJORS
F61-M1. Re-added Fig. 3 visually contradicts its own caption and the text

Location: Fig. 3, p.7.

The caption and surrounding text say the rotation contribution is negligible at the ≲10
−21
ρ
Λ
obs
	​

 level, with (ω/H)
0
2
	​

<2.5×10
−21
. But the figure’s lower panel visibly plots ΔH/H
ΛCDM
	​

 at the percent level, roughly 2–3%, not 10
−21
. The caption says the dark-energy mechanism is the ΞM
Pl
2
	​

 term, not rotation, but the visual reads like a measurable spin-torsion deviation in H(z). 

paper1a_ech_nogo_v1A.0.61

Proposed fix: Regenerate Fig. 3 so the plotted rotation-only residual is actually invisible on a linear percent axis, or relabel the plotted orange curve as something other than the rotation contribution. If the figure is instead showing a phenomenological Λ
eff
	​

 model difference, the caption must not describe it as a residual-rotation bound.

F61-M2. Route 2 Eq. (15) contains an algebraic inversion error in the second proportionality

Location: Sec. IV B, Eq. (15), p.11.

The first expression is

Δθ
obs
	​

Δθ
one−loop
	​

	​

∼
M
Pl
	​

(α/M)β
obs
	​

(α
em
	​

/4π)(H
0
	​

/M
Pl
	​

)
	​

.

Since M
Pl
	​

(α/M)=αM
Pl
	​

/M, the equivalent form should scale as

4π
α
em
	​

	​

M
Pl
	​

H
0
	​

	​

αM
Pl
	​

β
obs
	​

M
	​

,

not as something proportional to αβ
obs
	​

. The numerical estimate that follows uses the first expression and is therefore not obviously numerically damaged, but the printed second proportionality is wrong in the central Route-2 dimensional-reduction equation. 

paper1a_ech_nogo_v1A.0.61

Proposed fix: Delete the second proportionality or replace it with the corrected inverse form. Then recalc the displayed intermediate scaling in one line so the reader can reproduce 10
−60
.

F61-M3. The paper still calls ALP birefringence and primordial GWs “tests of γ” without deriving a γ-dependent observable

Location: Sec. I A, p.3; Sec. X F, p.19; Conclusions, p.24.

The paper correctly says the spectator-ALP β≃0.27
∘
 benchmark is not an ECH prediction and that no photon-torsion coupling is derived. But the conclusion still says perturbation transparency identifies ALP birefringence and primordial GWs as the relevant tests of γ. That is too strong: in the present manuscript, ALP birefringence is an external GR+ALP benchmark, not a Barbero-Immirzi measurement. 

paper1a_ech_nogo_v1A.0.61

Proposed fix: Replace “tests of γ” with “nonperturbative parity channels outside the proven scalar/tensor transparency sector.” Add: “They become tests of γ only in a specified model that derives a γ-dependent photon or tensor-parity coupling.”

F61-M4. LiteBIRD “exclude the ALP explanation” phrasing is still too broad

Location: Sec. VII, p.14–15; Sec. XIII, p.22; Conclusions, p.24.

The corrected 0.73σ model-discrimination statement is good. However, Sec. XIII still says LiteBIRD will “exclude the ALP explanation” if the non-zero-β signal is not confirmed. Uniform spectator ALP with the specific benchmark parameters could be excluded; the broader ALP explanation space cannot be excluded by a single uniform-rotation forecast without specifying priors, f
a
	​

, m
θ
	​

, coupling normalization, anisotropy, and time evolution.

Proposed fix: Use “exclude this uniform spectator-ALP benchmark as an explanation of the current WMAP+Planck central value,” not “exclude the ALP explanation.”

New MINORS

Fig. 1, p.5: The green SPHEREx box still says “mechanism-indep.” The text now correctly says scalar-only w=0 matter-bounce class and ECH-independent, not fully mechanism-independent. Replace the visual label with “ECH-indep. class test.” 

paper1a_ech_nogo_v1A.0.61

Fig. 4, p.15: “Parameter-independent” is too strong for SPHEREx because the forecast explicitly depends on systematics, bias priors, template overlap, photo-z, and survey assumptions. Replace with “model-comparison / class-level.” 

paper1a_ech_nogo_v1A.0.61

Fig. 6, p.21: “SPHEREx forecast is decisive (≳5σ)” conflicts with the same caption’s “2.6–5σ projection.” Say “potentially decisive in the optimistic regime; 2.6–5σ after systematic budget.” 

paper1a_ech_nogo_v1A.0.61

Sec. X B step 5, p.19: The total-derivative step remains distracting. Since the Holst dual vanishes pointwise at T=0, move the nonzero-torsion Nieh–Yan boundary comment to a footnote.

Sec. XI, p.20: The unconverged w
0
	​

w
a
	​

 chain status is still too operational for this paper. The table footnote was cleaned up, but the section still points to a non-converged chain. One sentence saying “no w
0
	​

w
a
	​

 posterior is used here” is enough.

PACS, p.2: Replace PACS with journal keywords unless the target journal requests PACS.

Names/encoding: “Pop lawski” and “Domaga la” still render without proper diacritics in the parsed PDF. Fix with robust LaTeX accenting or use ASCII consistently.

3. Updated recommendation

Recommendation: MAJOR REVISIONS.

The paper moved toward publishability since v1A.0.60: the ALP normalization, EB/ALP scoping, Appendix C, and reproducibility documentation are materially improved. I still would not recommend acceptance because the re-added Fig. 3 contradicts the text, Route 2’s central dimensional equation has an algebraic error, and residual “amplitude closure / unique survivor / tests of γ” language continues to overstate what the carefully scoped argument proves.
