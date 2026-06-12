# EXT5 P1A — ChatGPT Pro Extended (in-thread delta round 5)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e5e8-96cc-83e8-918f-3b1dd3f96d96
**PDF**: paper1a_ech_nogo_v1A.0.63.pdf · harvested 2026-06-12 00:47 PT · state done
---
Referee report update — Paper 1A v1A.0.63

Reviewed file: paper1a_ech_nogo_v1A.0.63.pdf, 28 pages, dated June 11, 2026 PDT. I reread the full PDF and checked the rendered figures. 

paper1a_ech_nogo_v1A.0.63

1. Closure verification
A. Closure against my v1A.0.61 fresh findings
Prior item	Status	Verification
F61-M1. Fig. 3 visually contradicted its caption/text	CLOSED / minor residue	The caption now distinguishes the plotted full ΞM
Pl
2
	​

 dark-energy model curve from the negligible rotation-only contribution, explicitly saying c
ω
	​

ω
2
 is ≲10
−21
ρ
Λ
obs
	​

 and invisible on the plotted scale. This fixes the substantive contradiction. The remaining issue is a new dimensional typo in the caption; see F63-M1 below. 

paper1a_ech_nogo_v1A.0.63


F61-M2. Route 2 Eq. (15) algebraic inversion error	CLOSED	Eq. (15) now uses the inverse denominator form M
Pl
	​

(α/M)β
obs
	​

 and explains the dimensionless contraction. The earlier αβ
obs
	​

 inversion problem is gone.
F61-M3. ALP birefringence and primordial GWs still called “tests of γ”	PARTIAL	The ALP benchmark is now mostly scoped as ECH-independent, but Sec. X F and the conclusion still say ALP birefringence / primordial GW chirality are “the relevant tests of γ.” That remains too strong without a derived γ-dependent photon or tensor-parity coupling.
F61-M4. “Exclude the ALP explanation” too broad	CLOSED	Sec. XIII now correctly says LiteBIRD could exclude this uniform spectator-ALP benchmark (f
a
	​

∼M
Pl
	​

,m∼H
0
	​

) as an explanation of the current WMAP+Planck central value, not the whole ALP explanation space. 

paper1a_ech_nogo_v1A.0.63

B. Residual status of original blockers and majors
Older item	Current status in v1A.0.63
B1. Dark-energy map not a controlled EFT result	PARTIAL — The ansatz status is now very explicit: Eq. (6) has off-shell dimension +1, and ρ
Λ
	​

=ΞM
Pl
4
	​

 is a scaling ansatz rather than a controlled EFT derivation. But the same ansatz still underwrites N
tot
	​

, Fig. 2/Fig. 3, and much of the closure narrative.
B2. Four-route closure overclaimed	PARTIAL — The abstract and closure summary now state the correct per-route picture, including omitted operators and R4 naturalness-only status. However, the Sec. IV opening still says “each route is closed at the amplitude level,” which is not true for R4 and is too strong for ansatz-based R2/R3.
B3. R4 amplitude contradiction	PARTIAL / mostly closed — R4 is correctly framed in Sec. IV D/E as a naturalness/explanatory-deficit route, not an amplitude exclusion. Residual blanket amplitude wording in Sec. IV and “tests of γ” wording still overstate the implication.
B4. Reheating thermal reset unsupported	PARTIAL — The source variable is correct, ⟨J
5
μ
	​

⟩, and the washout is conditional on Γ
wash
	​

>H. The full Boltzmann calculation is still deferred, and the SM rate hierarchy remains only a qualitative scaffold. 

paper1a_ech_nogo_v1A.0.63


B5. ALP notation inconsistent	CLOSED — The canonical ϕ convention and θ=ϕ/f
a
	​

 bridge are now coherent through Eq. (17) and Appendix C. 

paper1a_ech_nogo_v1A.0.63


B6. Data/code mismatch	PARTIAL / mostly closed — The numerical values are now synchronized and the paper no longer claims full duplication of NaMaster/ALP fitting. But the public README still advertises paper version v1A.0.61 / bundle v1A.0.59 while this manuscript is v1A.0.63, and the Zenodo DOI remains pending. 
GitHub

B7. Stale/wrong figure values	PARTIAL — The old PTA, N
tot
	​

, ALP, and Fig. 3 issues are mostly fixed. Fig. 1 still visually says “SPHEREx, mechanism-indep.” and Fig. 4 still says “parameter-independent” and “unique surviving minimal-ECH channel,” which remain overstated.
B8. “Fundamental action” includes on-shell shorthand	PARTIAL — The footnote is clear that T
abc
T
abc
	​

 is an on-shell Hehl–Datta shorthand and is not varied independently, but Eq. (1) still visually places it inside the “fundamental action.” 

paper1a_ech_nogo_v1A.0.63


M1. Perturbation-transparency scope	CLOSED — The proof now rests on the first Bianchi identity, not the deleted pair-exchange chain, and the scalar/tensor scope is clear. The remaining total-derivative step is unnecessary but not fatal. 

paper1a_ech_nogo_v1A.0.63


M2. N
tot
	​

–f
NL
	​

 mode-history derivation	PARTIAL — The mode-history ledger and scoping are improved, but the transfer function and N
coh
	​

 calculation remain deferred while “definitively erased” language persists.
M3. Companion-paper dependence	PARTIAL — Companion imports are now caveated as internal inputs not used in the structural proof, but the manuscript still carries many companion values and forecasts. 

paper1a_ech_nogo_v1A.0.63


M4. DESI/quintom language	CLOSED — The problematic model-specific DESI/quintom overclaim has been removed.
M5. Theorem/no-go language over broad catalogue	PARTIAL — “Perturbation-transparency result” is now the right phrase, but “Four-Route No-Go” and blanket amplitude-closure wording still exceed what is shown.
M6. Route 1 density language	REGRESSION — The internal round removed the previous incorrect chain but introduced a worse one: Sec. IV A now says post-recombination densities give ρ
NJL
	​

∼O(1)eV
4
, far above ρ
Λ
	​

. That is off by roughly 80 orders in the wrong direction; see F63-B1.
M7. ALP benchmark/forecast oversold	MOSTLY CLOSED — The benchmark is now correctly ECH-independent and LiteBIRD discrimination is scoped. Residual “tests of γ” wording remains.
M8. Scope-language cleanup	PARTIAL — Body text is substantially improved, but Fig. 1, Fig. 4, Sec. IV opening, and the conclusion still contain overstrong remnants.
2. Fresh pass — new findings only
New BLOCKERS
F63-B1. Route 1 now contains a severe unit-conversion regression and a flawed mean-field argument

Location: Sec. IV A, p.11.

The revision says a naive post-recombination estimate n
ψ
	​

∼O(10
2
)cm
−3
 gives ρ
NJL
	​

∼O(1)eV
4
, far above ρ
Λ
	​

. 

paper1a_ech_nogo_v1A.0.63

 That is not correct. Using 1cm
−3
≃7.7×10
−15
eV
3
, n∼10
2
cm
−3
 gives n∼10
−12
eV
3
, and n
2
/M
Pl
2
	​

∼10
−80
eV
4
, not O(1)eV
4
. The previous v1A.0.61-style value, ρ
NJL
	​

∼4×10
−80
eV
4
∼10
−69
ρ
Λ
	​

, was the correct order of magnitude. 

paper1a_ech_nogo_v1A.0.61

The proposed replacement argument is also not safe as written: ⟨J
5
μ
	​

⟩≃0 in an unpolarized bath does not by itself imply ⟨J
5
μ
	​

J
5μ
	​

⟩=0. For a four-fermion contact operator, the distinction between coherent mean axial current, local variance, condensate expectation, and thermal/incoherent stress-energy matters.

Proposed fix: Restore the correct density conversion and state the Route-1 closure in two parts: late-time mean-field amplitude n
2
/M
Pl
2
	​

 is negligible for baryon/electron densities, and any incoherent thermal variance is not a coherent w=−1 vacuum component. Do not claim that ⟨J
5
	​

⟩=0 alone makes the four-fermion operator vanish.

New MAJORS
F63-M1. Fig. 3 caption has a new dimensional typo in Ξ

Location: Fig. 3, p.7.

The caption says the orange curve uses Ξ=ρ
Λ
	​

/M
Pl
2
	​

≈10
−123
. That is dimensionally wrong. In the body immediately below, the paper correctly defines ρ
Λ
	​

=Λ
eff
	​

M
Pl
2
	​

=ΞM
Pl
4
	​

, so the dimensionless quantity is Ξ=ρ
Λ
	​

/M
Pl
4
	​

, while Λ
eff
	​

/M
Pl
2
	​

 would also be dimensionless. 

paper1a_ech_nogo_v1A.0.63

Proposed fix: Replace “Ξ=ρ
Λ
	​

/M
Pl
2
	​

” with “Ξ=ρ
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

.” This is important because the paper’s central caveat is dimensional bookkeeping.

F63-M2. PTA/NANOGrav claim appears to cite the wrong companion paper

Location: Sec. X G, p.20; References, Paper III [46].

Sec. X G attributes γ
PTA
	​

=2.567±0.382 from a real-KDE GPU MCMC reanalysis of NANOGrav 15-year free-spectrum data to companion Paper III [46]. 

paper1a_ech_nogo_v1A.0.63

 But the data/code and forward-looking text identify Paper III [46] as a “multi-survey anomaly catalog,” not a PTA/NANOGrav real-KDE analysis. 

paper1a_ech_nogo_v1A.0.63

 This is not a small citation typo because the PTA value appears in Fig. 1, Table IV, and the bounce-discrimination discussion.

Proposed fix: Cite the actual PTA/NANOGrav companion manuscript or remove the γ
PTA
	​

 numerical claim from this paper until the relevant analysis is public and correctly referenced. If the anomaly-catalog Paper III really contains the PTA analysis, the title/description in the references and forward paragraph must say so.

F63-M3. Reproducibility metadata still does not pin v1A.0.63

Location: Data and Code Availability, p.24–25; public repository metadata.

The paper now says code/data are available, frozen MCMC chains are committed, and a Zenodo release will pin the submitted snapshot. That is an improvement. 

paper1a_ech_nogo_v1A.0.63

 However, the public README still labels the paper version as v1A.0.61 and the bundle as v1A.0.59, with BibTeX metadata also at v1A.0.59, while the submitted manuscript is v1A.0.63. 
GitHub
 The known-gaps file now consistently says frozen chains are committed and fresh proxy chains are not precomputed, which is good, but it also confirms that no CMB EB/TB map-level processing is included. 
GitHub

Proposed fix: Before submission, create a v1A.0.63 tag/release and update README/BibTeX/known-gaps metadata to match the manuscript exactly. Insert the Zenodo DOI or remove the promise until the DOI exists.

New MINORS

Fig. 3, p.7: The figure legend still says “Spin-Torsion,” although the caption now says the plotted orange curve is the full Ξ-fit dark-energy parameterization, not rotation. Rename the legend to “Ξ-fit ECH ansatz” or “full ECH-DE ansatz.”

Fig. 1, p.5: The SPHEREx box still says “mechanism-indep.” The body now correctly says “ECH-independent class test.” Update the visual label.

Fig. 4, p.15: “Parameter-independent” and “unique surviving minimal-ECH channel” remain too strong. The tests are class-level and ECH-independent; they do not identify a unique surviving minimal-ECH channel.

Fig. 6, p.22: The caption says the SPHEREx forecast is “decisive (≳5σ)” while the same caption and Sec. XIII give a 2.6–5σ post-systematics range. Use “potentially decisive in the optimistic regime.”

PACS, p.2: Replace PACS with journal keywords unless the target journal explicitly requests PACS.

Names/encoding: “Pop lawski” and “Domaga la” still render without proper diacritics in the extracted/rendered text. Fix with robust LaTeX accent commands or use ASCII consistently.

3. Updated recommendation

Recommendation: MAJOR REVISIONS.

The paper moved slightly toward publishability in ALP normalization, Fig. 3 scoping, and Appendix C, but the new Route-1 NJL regression is serious enough to keep the verdict at major revisions; the paper is not ready for acceptance until that calculation, the Ξ dimensional typo, and the remaining citation/scope issues are fixed.
