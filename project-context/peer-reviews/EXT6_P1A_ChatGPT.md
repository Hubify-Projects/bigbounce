# EXT6 P1A — ChatGPT Pro Extended (in-thread delta round 6)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e5e8-96cc-83e8-918f-3b1dd3f96d96
**PDF**: paper1a_ech_nogo_v1A.0.65.pdf (418777c6) · harvested 2026-06-12 19:51 PT

---

Referee report update — Paper 1A v1A.0.65

Reviewed file: paper1a_ech_nogo_v1A.0.65.pdf, dated June 12, 2026 PDT, 28 pages. I reread the full revised PDF and checked the rendered figures as well as the public reproducibility repository. 

paper1a_ech_nogo_v1A.0.65

1. Closure verification
A. Closure against my v1A.0.63 findings
Prior item	Status	Verification
F63-B1. Route 1 NJL unit-conversion regression	PARTIAL	The main Route 1 calculation is now physically corrected: the manuscript states 1cm
−3
≃7.66×10
−15
eV
3
, obtains ρ
NJL
	​

∼4×10
−81
eV
4
, and correctly describes this as ∼4×10
−69
ρ
Λ
	​

, far below dark energy. It also now distinguishes mean-field amplitude from incoherent variance and coherent w=−1 structure. 

paper1a_ech_nogo_v1A.0.65

 However, Sec. IV E still says “the condensate mechanism yields a vacuum energy that is parametrically too large by many orders of magnitude,” which directly contradicts the corrected Route 1 section. That stale sentence is now the main remaining blocker. 

paper1a_ech_nogo_v1A.0.65


F63-M1. Fig. 3 Ξ dimensional typo	CLOSED	Fig. 3 and the body now use the correct dimensionless identification Ξ=ρ
Λ
	​

/M
Pl
4
	​

=Λ
eff
	​

/M
Pl
2
	​

, distinguish the full ΞM
Pl
2
	​

 dark-energy curve from the rotation-only bound, and state the Saadeh rotation bound as a conservative Bianchi-IX bookkeeping upper limit. 

paper1a_ech_nogo_v1A.0.65


F63-M2. PTA/NANOGrav companion-paper attribution	CLOSED / minor residual	The forward-looking paragraph now explicitly says Paper III includes the NANOGrav 15-yr free-spectrum real-KDE GPU MCMC reanalysis used for γ
PTA
	​

. That cures the prior mismatch in the paper’s internal attribution. 

paper1a_ech_nogo_v1A.0.65

 Minor residual: the companion-paper title remains broad, so the final bibliography should make the PTA/NANOGrav component visible if it is material to this paper.
F63-M3. Reproducibility metadata not pinned to manuscript version	PARTIAL	The manuscript now says frozen MCMC chains are committed and that a Zenodo DOI will pin the submitted snapshot. 

paper1a_ech_nogo_v1A.0.65

 The public README has synchronized the key frozen-chain values, but it currently labels the paper/bundle as v1A.0.64 while the reviewed PDF is v1A.0.65; the DOI is also still pending. The known-gaps file is much clearer than before, but it still confirms no bespoke CAMB and no CMB map-level processing in the bundle. 
GitHub
+1
B. Residual status of the original v1A.0.56 blockers and majors
Original item	Current status in v1A.0.65
B1. Dark-energy map not a controlled EFT result	PARTIAL — The ansatz status is now explicit and honestly framed, including the off-shell dimension-+1 issue and the need for a separate dimension-+4 EFT/operator-basis construction. But the ansatz still underwrites N
tot
	​

, Ξ, Fig. 5, and the channel-closure narrative. 

paper1a_ech_nogo_v1A.0.65


B2. Four-route closure overclaimed	PARTIAL — The abstract is now calibrated, but Sec. IV still says “each route is closed at the amplitude level,” which is inaccurate for R4 and too strong for ansatz-level R2/R3. 

paper1a_ech_nogo_v1A.0.65


B3. R4 amplitude contradiction	PARTIAL / mostly closed — R4 is correctly framed in the abstract and Sec. IV D/E as naturalness/explanatory-deficit closure, not amplitude exclusion. Remaining issue: blanket amplitude-closure language and Fig. 4 “unique survivor” language still overstate.
B4. Reheating thermal reset unsupported	PARTIAL — The source is correctly ⟨J
5
μ
	​

⟩, not total fermion number density, and the washout is conditional. But no Boltzmann calculation is included; it remains a plausible thermodynamic caveat, not a demonstrated closure.
B5. ALP notation inconsistent	CLOSED — The canonical ϕ convention, θ=ϕ/f
a
	​

 bridge, and β=(α/2M)Δϕ=(αf
a
	​

/2M)Δθ normalization are now coherent. 

paper1a_ech_nogo_v1A.0.65


B6. Data/code mismatch	PARTIAL / mostly closed — Values are synced and the limitations are clearer, but the public bundle is still one manuscript version behind and the Zenodo DOI is not inserted. 
GitHub
+1

B7. Stale figure values	PARTIAL — The old numerical errors are mostly fixed, including Fig. 3 and γ
PTA
	​

. Fig. 4 and Fig. 6 still contain interpretive overclaiming.
B8. “Fundamental” action includes on-shell shorthand	PARTIAL — The footnote is clear that T
abc
T
abc
	​

 is an on-shell Hehl–Datta shorthand and not varied independently, but Eq. (1) still visually includes it inside the displayed “fundamental action.” 

paper1a_ech_nogo_v1A.0.65


M1. Perturbation-transparency scope	CLOSED / minor residue — The result is now scoped to classical scalar/tensor perturbations around the torsion-free branch, with the Bianchi-identity proof cleanly stated. The remaining “total derivative” step is unnecessary but not damaging. 

paper1a_ech_nogo_v1A.0.65


M2. N
tot
	​

–f
NL
	​

 mode history	PARTIAL — The scale-history ledger is clearer and the sign of the fine-tuning score is fixed. But the transfer function is still deferred while “definitively erased” language remains. 

paper1a_ech_nogo_v1A.0.65


M3. Companion-paper dependence	PARTIAL — The paper now repeatedly says companion values are not used in the structural proof, but it still imports MCMC, galaxy-spin, ALP, SPHEREx, and PTA values into tables/figures. 

paper1a_ech_nogo_v1A.0.65


M4. DESI/quintom language	CLOSED — Now framed as model-level dynamical-DE accommodation, not posterior preference or empirical support for a specific quintom scenario.
M5. Theorem/no-go language over a mixed catalogue	PARTIAL — “Perturbation-transparency result” is mostly correct, but “Four-Route No-Go” and blanket amplitude-closure language still exceed a pure ansatz-level audit.
M6. Route 1 density language	PARTIAL — Main Route 1 calculation is corrected; Sec. IV E still contains the opposite sign statement.
M7. ALP benchmark/forecast oversold	MOSTLY CLOSED — The benchmark is correctly ECH-independent and LiteBIRD model discrimination is correctly given as ∼0.7σ against the current WMAP+Planck central value, not ∼2.4σ. 

paper1a_ech_nogo_v1A.0.65


M8. Scope-language cleanup	PARTIAL — The abstract and many body sections are much improved; Sec. IV opening, Fig. 4, Fig. 6, and “tests of γ” wording still need final cleanup.
2. Fresh pass — new findings only
BLOCKERS
F65-B1. Sec. IV E now contradicts the corrected Route 1 result

Location: Sec. IV E, p.14; compare Sec. IV A, p.11.

The Route 1 section is now correct: for post-recombination baryon/electron densities, ρ
NJL
	​

∼n
ψ
2
	​

/M
Pl
2
	​

≈4×10
−81
eV
4
∼4×10
−69
ρ
Λ
	​

, i.e. far below the dark-energy density. 

paper1a_ech_nogo_v1A.0.65

 But the closure summary still says the “condensate mechanism yields a vacuum energy that is parametrically too large by many orders of magnitude.” That is the old sign/error class surviving in the most important summary paragraph. 

paper1a_ech_nogo_v1A.0.65

Proposed fix: Replace the stale sentence with: “The NJL contact term is far below ρ
Λ
	​

 for late-time Standard Model number densities, parity-even, and lacks a coherent w=−1 mean-field component; incoherent thermal variance is not a coherent dark-energy source.” Then scan the full manuscript for “too large,” “overshoot,” and “condensate” to ensure no remaining Route-1 sign residues.

MAJORS
F65-M1. Sec. IV still says every route is amplitude-closed

Location: Sec. IV opening and scope paragraph, p.10–11.

The abstract and closure summary mostly state the calibrated claim: R1–R3 are amplitude-suppressed under assumptions; R4 is naturalness/explanatory-deficit closure. But Sec. IV still says “each route is closed at the amplitude level,” even though R4 is explicitly not amplitude-closed and R2/R3 are ansatz-level amplitude budgets. 

paper1a_ech_nogo_v1A.0.65

Proposed fix: Replace with: “R1 is amplitude-suppressed by the standard contact term; R2/R3 are amplitude-suppressed under the upper-bound ansätze stated below; R4 is not amplitude-excluded and is instead non-predictive/naturalness-limited without an external ALP mass and photon coupling.”

F65-M2. Fig. 4 still overstates the observational programme

Location: Fig. 4, p.15.

The paper now correctly describes the surviving tests as ECH-independent class tests. But the rendered Fig. 4 caption still says the surveys deliver “parameter-independent” discrimination and that the joint outcome “falsifies the surviving ECH framework or leaves it as the unique survivor.” This is not compatible with the body text: SPHEREx tests a scalar-only w=0 matter-bounce class, and LiteBIRD tests a uniform spectator-ALP benchmark, neither of which is a unique ECH prediction.

Proposed fix: Rewrite the Fig. 4 caption as: “Observational timeline for two ECH-independent class tests. These tests can falsify the relevant matter-bounce and uniform spectator-ALP benchmarks under the stated assumptions; they do not identify a unique surviving minimal-ECH channel.”

F65-M3. Public reproducibility metadata is still one version behind

Location: Data and Code Availability, p.25; public README / known-gaps file.

The manuscript says a Zenodo release will pin the submitted snapshot and that frozen chains are committed. 

paper1a_ech_nogo_v1A.0.65

 The public README is now much better synchronized numerically, but it labels the current paper and bundle as v1A.0.64, while the reviewed PDF is v1A.0.65; the DOI remains “to be inserted.” The known-gaps file clearly says the bundle includes frozen chains but not fresh chains, no custom CAMB, and no CMB map-level processing. 
GitHub
+1

Proposed fix: Before submission, tag a v1A.0.65 repository release, update README/BibTeX/known-gaps metadata to v1A.0.65, insert the Zenodo DOI, and state explicitly whether v1A.0.65 is byte-identical to v1A.0.64 or not.

F65-M4. “Tests of γ” remains too strong without a derived γ-dependent observable

Location: Introduction, p.3–4; Sec. X F / conclusions, p.20 and p.24.

The paper still says tests of γ shift to nonperturbative parity-violating channels such as ALP birefringence and primordial GWs. 

paper1a_ech_nogo_v1A.0.65

 But the paper also says the ALP benchmark is not ECH-specific and that no photon-torsion coupling is derived. The current manuscript therefore has ECH-independent parity probes, not Barbero–Immirzi measurements.

Proposed fix: Replace “tests of γ” with “parity-sensitive channels outside the scalar/tensor transparency sector.” Add that they become tests of γ
BI
	​

 only in a model that derives a γ
BI
	​

-dependent photon or tensor-parity coupling.

MINORS

Fig. 6, p.22: The caption still says the SPHEREx forecast is “decisive (≳5σ)” even though the same caption and Table I give a 2.6–5σ realistic range. Use “potentially decisive in optimistic configurations; 2.6–5σ after the stated systematic budget.” 

paper1a_ech_nogo_v1A.0.65

Sec. X B, p.19: Delete Step 5 (“A total derivative contributes nothing…”) or move it to a footnote. The proof already says the Holst dual contraction vanishes pointwise by the first Bianchi identity. 

paper1a_ech_nogo_v1A.0.65

Sec. IV title: “Four-Route No-Go” still sounds stronger than the paper’s actual “channel-level closure under assumptions.” “Four-Route Channel Audit” would better match the revised content.

PACS, p.2: Replace PACS with journal keywords unless the target journal explicitly asks for PACS.

Names/encoding: “Pop lawski” and “Domaga la” still render without proper diacritics in extracted text. Use robust LaTeX accent commands or ASCII consistently.

3. Updated recommendation

Recommendation: MAJOR REVISIONS.

The paper moved toward publishability since v1A.0.63: the NJL calculation, Ξ dimensional caption, γ-scheme spread, ALP mapping, and f
NL
	​

 forecast labels are materially improved. It is not yet ready for acceptance because the closure summary still contains the wrong-sign NJL claim, Sec. IV/Fig. 4 still overstate the per-route closure, and the reproducibility snapshot is not yet pinned to the reviewed version.
