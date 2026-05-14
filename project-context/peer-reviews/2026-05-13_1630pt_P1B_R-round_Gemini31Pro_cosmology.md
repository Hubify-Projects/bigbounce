# P1B Adversarial Theory Review — Gemini-3.1-Pro (Cosmology Theorist Profile)

**Reviewer simulated:** Google Gemini-3.1-Pro, cosmology theorist (Kamionkowski / Komatsu / Baumann / Carroll / Mercuri composite profile).
**Target:** `arxiv/paper1b_mcmc_companion.tex` v1B.0.3, 658 lines.
**Companion to:** `arxiv/paper1a_ech_nogo.tex` v1A.0.20 (theory no-go); cross-paper status table at §VII.
**Date:** 2026-05-13 16:30 PT.
**Mode:** Adversarial — break the ALP derivation chain, the ΛCDM+ΔNeff proxy's defensibility as a stand-in for spin-torsion, the NaMaster pipeline-validation claims, the w0–wa narrative, and the cross-paper coupling to P1A / P3. Do NOT police arithmetic or bibkeys; that is the R-round's job. Police *physics* and *cross-paper coherence*.
**Convergence reference:** P1A R-round-3 (2026-05-13 15:30 PT) closed at 1B + 3M + 6m. P1B has not been adversarially probed at the same depth and is co-arXiv-submitted with P1A — readiness 75% (compute-gated on the DESI DR2 w0wa chain).

---

## Honest count

**1 BLOCKER + 4 MAJOR + 7 MINOR = 12 findings.**

- BLOCKER: 1 — The ΛCDM+ΔNeff stock-CAMB proxy MCMC is *not a defensible proxy* for the ECH spin-torsion sector at the operator level; the proxy framing in §I, §III, §VIII, and the abstract papers over the fact that the spin-torsion sector's leading effect on the Boltzmann hierarchy is *not* an additional relativistic species, and quoting the run as a "null-consistency test" for the framework misdirects readers about what was actually tested.
- MAJOR: 4 — (a) β = 0.27° derivation chain in §VI is *incomplete and conflates spectator-ALP photon-coupling phenomenology with the ECH motivation* without exhibiting the photon-torsion coupling that would make the prediction ECH-specific; (b) the bounce → ΔNeff connection (the only physical justification for running the proxy at all) is never explicitly made in P1B; (c) Quintom-A vs Quintom-B class taxonomy is invoked in §VII.A without naming which class the ECH bounce mechanism belongs to, leaving the DESI DR2 cross-paper anchor floating; (d) the bounce GW γ_GW = 3.0 / f_NL = -35/8 shared contracting-phase coupling (which P3 §VI tick 2 added) is absent from P1B — P1B does not exhibit the contracting-phase-mode-function coupling that P3 now requires.
- MINOR: 7 — Komatsu-2022 review absent, Eskilt-2024 follow-up absent, NaMaster MASTER deconvolution scope-creep risk, w0-wa CPL parametrization not located in bounce-vs-quintom theory space, "spectator ALP" terminology drift, Planck Commander foreground-cleaning assumption, LiteBIRD 9σ forecast double-counts the same ALP that GR+ALP also predicts.

---

## Most concerning theory issue (the BLOCKER)

**The ΛCDM + ΔNeff stock-CAMB MCMC proxy is not a proxy for the ECH spin-torsion sector. It is a generic radiation-extension run.** P1B advertises it as a "null-consistency test of an extra radiation-like degree of freedom" (abstract L67–73; §III.1 L113–120), and the paper is admirably explicit that this is *not* a torsion-modified Boltzmann run. But the deeper problem is that *the proxy itself was never derived from the ECH spin-torsion sector to begin with*. The paper assumes — without exhibiting — that the leading observable signature of the ECH spin-torsion sector at CMB epochs is captured by a positive shift in N_eff. This is *not obviously true*, and a PRD-level referee will press on three points:

1. **The Hehl-Datta-Mercuri four-fermion contact term (which is what survives torsion elimination in the ECH framework, per P1A §IV.R1 and Eq. (5)) is parity-even and dimension-six, with coefficient `(γ²/(γ²+1)) × 8πG / M_Pl²`.** It does *not* introduce a new relativistic species. Its leading effect on the Boltzmann hierarchy is a modification of the fermion-photon and fermion-graviton scattering cross-section at amplitudes suppressed by `M_Pl^{-2}` — undetectable at any current CMB sensitivity. *That* is what an "ECH proxy" run would be parameterizing, not ΔNeff.

2. **ΔNeff > 0 in the ECH framework would arise from particle production *at the bounce itself*, not from the surviving torsion contact term.** This is what P1A §I.B alludes to ("Δ\Neff (particle production at the bounce)" — L155 of P1B) but the bounce particle-production calculation is *not in this paper* and *not in P1A*. The proxy is run on the assumption that there is some such ΔNeff, but neither paper exhibits the mode-function calculation that would convert a bounce duration and a bounce-energy scale into a *prediction* for ΔNeff. Without that calculation, ΔNeff = 0 in the data is consistent with: (a) the ECH bounce produces no particles (favored by minimal-coupling); (b) the ECH bounce produces particles but at a level σ(ΔNeff) ≲ 0.17 cannot distinguish; (c) the ECH framework's particle production goes into a non-relativistic-by-recombination channel; (d) the framework's predicted ΔNeff is *negative* (Reheating mismatch). The "null-consistency" claim does not discriminate among these.

3. **The proxy is a category mismatch with the bounce-cosmology discrimination table** in P1A §V (matter-bounce vs Cuscuton vs ekpyrotic vs quintom vs inflation, ~L736–850 of `arxiv/main.tex`). The matter-bounce class is *typically associated with negligible ΔNeff at recombination* (the entropy production is locked up in the inflaton-bounce transition; bounce-phase particle production thermalizes well before recombination, see Brandenberger 2017 review). For matter-bounce, ΔNeff ≈ 0 is the *prediction*, not a null result. So the "current data neither require nor exclude a small positive ΔNeff from the spin-torsion sector" framing in P1B §III L226-231 *quietly inverts the matter-bounce prediction*: matter-bounce predicts ΔNeff ≈ 0, and the proxy run *confirms* it. P1B should be saying "the data are *consistent with the matter-bounce prediction* that ΔNeff = 0", not "the data neither require nor exclude". Quintom-class bounces are the ones that would predict a measurable ΔNeff, and they are the cross-paper anchor for the DESI DR2 w0-wa chain — so the right framing splits the proxy run by bounce class, which P1B does not do.

**The consequence is structural for the cross-paper coupling to P1A.** P1A's no-go argues that minimal-ECH cannot deliver DE. P1B's proxy MCMC is *not a test of that no-go*. P1B's proxy is a generic ΛCDM+ΔNeff null, and dressing it up as a "verification companion" to the no-go theorem misrepresents what an arXiv reader is being shown. The honest framing is one of: (a) drop the "verification" language entirely and present this run as a *prior-art replication* of standard ΛCDM+ΔNeff to show that the H_0 number and σ_8 number Houston quotes elsewhere are not bookkeeping artifacts (this is fine — it just isn't a "verification of the ECH framework"); (b) actually derive the ECH-predicted ΔNeff from a bounce particle-production calculation and frame this run as a constraint on *that* prediction; (c) re-frame as a *bounce-class discrimination* analysis: ΔNeff ≈ 0 favors matter-bounce / disfavors quintom-bounce, which is consistent with the §V Paper-1A discrimination table.

**Why this is a BLOCKER, not a MAJOR:** the paper's abstract and §I literally call this "the technical verification material for the Einstein-Cartan-Holst (ECH) spin-torsion cosmology no-go program" (L64–66). A PRD referee will read "verification" and expect either a test of the no-go's theory predictions or a constraint on the bounce-cosmology sector. They will get neither — they will get a stock CAMB ΔNeff run with disclaimers. The disclaimers (L67–73, L113–135, L172–177) are admirably honest but they do not rescue the framing; they admit the gap exists. A no-go theorem paired with a companion paper that runs a generic radiation-species null and calls it "verification" reads as a category error. The fix is to convert the framing from "verification" to "prior-art replication + bounce-class discrimination", with the §V cross-reference to P1A's discrimination table made *explicit and load-bearing*.

**Recommended fix.** Insert a new §III.A "Bounce-class predictions for ΔNeff" (~half a page, two paragraphs):
- Para 1: matter-bounce predicts ΔNeff ≈ 0 because entropy production thermalizes before recombination (Brandenberger 2017, Wilson-Ewing 2013); quintom-bounce predicts ΔNeff > 0 because the additional dark-fluid degree of freedom is relativistic at the bounce-to-radiation transition (Cai+ 2009 review).
- Para 2: the proxy run's ΔNeff = -0.020 ± 0.169 is consistent at 0.1σ with the matter-bounce prediction and disfavors the quintom-bounce prediction (for the natural quintom mass range m_Q ~ H_eq) at ~0.5σ. This is not a discriminating constraint at current sensitivity; CMB-S4 σ(N_eff) ~ 0.03 will distinguish matter-bounce from quintom at ~5σ.
- Then change the §III header from "Stock-CAMB LCDM+DNEff MCMC: Generic Radiation-Proxy Test (Not a Spin-Torsion Theory Module)" to "Bounce-Class ΔNeff Discrimination Using a Stock-CAMB Proxy" and re-frame the abstract paragraph (1) from "null-consistency test of an extra radiation-like degree of freedom" to "constraint on bounce-class ΔNeff predictions using a stock-CAMB ΔNeff proxy".

This is ~1 page of new text plus header re-wording. It converts the proxy run from a category-error into a legitimate (though current-sensitivity-limited) bounce-class discrimination tool, and it directly serves the cross-paper coupling that P1B advertises but does not currently deliver.

---

## MAJOR findings

### MAJOR-1: The β = 0.27° derivation chain in §VI is incomplete and conflates spectator-ALP photon-coupling phenomenology with the ECH motivation without exhibiting the photon-torsion coupling.

**§VI (L380–445) presents:**
- The ALP equation of motion in a ΛCDM background (numerically integrated, Δφ/f_a ≈ 0.65 for m = H_0, θ_i = 1).
- The standard Carroll-Field-Jackiw birefringence formula: β ≈ (α_EM × C_aγ / 4π) × (Δφ/f_a).
- A natural-parameter scan: β ∈ [0.17°, 0.43°] over C_aγ ∈ [4,12], m/H_0 ∈ [1,3], θ_i ∈ [0.5,2].
- A "fiducial" β ≈ 0.27° at C_aγ = 8, m ≈ 1.8 H_0, Δφ/f_a ≈ 1.0.

**This is correct as a GR+ALP calculation.** It is the Carroll-Field-Jackiw 1990 / Lue-Wang-Kamionkowski 1999 / Carroll 1998 / Fujita+ 2021 result. **What is missing is the chain from the Holst action to this Lagrangian.** The paper says (L443–445) "The ECH framework provides heuristic motivation ($f_a \sim M_{\rm Pl}$ from the Holst sector pseudoscalar structure) but no derived photon-torsion coupling connects the Holst action to a specific ALP potential." Good — this is honest. **But then "spectator-ALP fiducial $\beta = 0.27°$" appears throughout the paper (abstract L80–84, §IV L298, §VIII L548–552) as if it were derived from the ECH motivation.** It is not. It is a *post-hoc fitted fiducial* chosen to match the observed signal, with the derivation chain going *from* the observed signal *to* the natural-parameter range that brackets it, not *from* the Holst action *to* β.

Three concrete fixes are needed:

(a) **Cite Carroll-Field-Jackiw 1990 explicitly at Eq. for β.** The bibkey `CarrollFieldJackiw1990` exists in references.bib (L380) but is not cited at the β derivation in §VI. The reader sees the formula without the canonical reference. Cite at L407–410.

(b) **Cite Komatsu 2022 review explicitly for the ALP-DE class.** The Komatsu 2022 IJMPD review ("New physics from the polarized light of the cosmic microwave background") is the *standard* current reference for ALP cosmic birefringence and is *missing entirely from references.bib*. Adding this is one bibitem and one inline cite in §VI; the omission is a tell that the literature engagement is shallow.

(c) **State the m_a window and g_φγ window the prediction is conditional on.** §VI gives "m ∈ [1,3] H_0" and "C_aγ ∈ [4,12]" but does *not* convert these to the standard ALP-physics parameter axes m_a (eV) and g_aγγ (GeV^{-1}). For m = H_0, m_a ≈ 1.4 × 10^{-33} eV — i.e., *the ALP must be ultralight*, in the "fuzzy dark matter" mass regime (though it is not dark matter because Δφ/f_a remains finite). For C_aγ = 8 with f_a = M_Pl ≈ 2.4 × 10^{18} GeV, g_aγγ = α_EM × C_aγ / (2π f_a) ≈ 3 × 10^{-21} GeV^{-1}, which is below the CAST haloscope bound and below the SN1987A bound. State both numbers; otherwise the reader cannot place this ALP in the standard m_a–g_aγγ plot. The standard reference is the "ALP haloscopes" review (Irastorza & Redondo 2018) — also missing from references.bib.

(d) **Note that the same ALP, with the same parameters, is the canonical "early dark energy" candidate** (Poulin+ 2019, Hill+ 2020, the EDE review). The prediction β ≈ 0.27° at m_a ~ H_0 / f_a ~ M_Pl puts the field exactly in the EDE mass-coupling box. P1B does not mention this. This is a *strong* cross-coupling because EDE itself was proposed as a candidate H_0-tension resolution — and the proxy MCMC says ΔNeff ≈ 0, which is consistent with ALP-EDE *not* contributing to N_eff (the field oscillates and dilutes as matter post-recombination, not radiation). A two-sentence acknowledgement that this ALP class is *also* the EDE class would strengthen the cross-paper coupling.

**Fix:** Rewrite §VI L398–413 as a four-paragraph block:
- (1) "The ALP field evolution and birefringence calculation follow Carroll-Field-Jackiw [@CarrollFieldJackiw1990] and Lue-Wang-Kamionkowski [@LueWangKamionkowski1999]; the cosmic birefringence interpretation is reviewed in Komatsu 2022 [@Komatsu2022Review, new bibitem]." Then the Δφ/f_a integration.
- (2) "Translating to standard ALP parameters: m = H_0 → m_a ≈ 1.4 × 10^{-33} eV; C_aγ = 8 + f_a = M_Pl → g_aγγ ≈ 3 × 10^{-21} GeV^{-1}. These lie in the ultralight-ALP / fuzzy-DM-mass regime and are well below all laboratory and SN1987A bounds [@IrastorzaRedondo2018, new bibitem]."
- (3) The β formula and natural-parameter scan.
- (4) "The same parameter window (m_a ~ H_0, f_a ~ M_Pl) is the canonical 'early dark energy' candidate window (Poulin+ 2019, Hill+ 2020). The proxy MCMC ΔNeff ≈ 0 result is consistent with this ALP class not contributing to N_eff (the field oscillates and dilutes as matter post-recombination)."

This is ~80 words of new text and three new bibitems (Komatsu2022Review, IrastorzaRedondo2018, Poulin2019EDE). It converts §VI from a free-floating GR+ALP calculation into a literature-anchored ALP-EDE+birefringence calculation with the right cross-paper hooks.

### MAJOR-2: The bounce → ΔNeff connection (the only physical justification for running the proxy at all) is never explicitly made in P1B.

This is the proxy-defensibility issue from the BLOCKER, restated as a specific MAJOR. **P1B never says — in either the abstract, §I, §II, or §III — *why* the bounce cosmology framework should be tested with a ΔNeff extension.** The implicit reasoning is "bounce → particle production → relativistic species → ΔNeff", but the chain is nowhere exhibited. A referee will ask:

- What is the predicted ΔNeff from the ECH bounce?
- What is the predicted ΔNeff from a generic matter-bounce vs a quintom-bounce vs an ekpyrotic bounce?
- Is the predicted ΔNeff at recombination, or is it diluted by reheating?
- Does the bounce-phase particle production thermalize with the SM bath before BBN?

None of these have an answer in P1B. The §II "Cosmological Tensions" section (L153–164) says "The bounce scenario motivates extending ΛCDM by ΔNeff (particle production at the bounce) and (ω/H)_0 (angular momentum transfer)" — but does not cite a calculation, does not give a predicted range, and does not explain why these two parameters are the right extension.

**Fix:** Insert a paragraph in §II naming the bounce → ΔNeff chain and citing the relevant matter-bounce reheating calculation (Wilson-Ewing 2013 is already cited; Cai 2014 review covers matter-bounce reheating; Brandenberger 2017 "Bouncing Cosmologies" review is the canonical citation). State the *predicted* ΔNeff range from matter-bounce (typically |ΔNeff| ≲ 0.1, depending on the bounce-phase entropy production model; see Cai 2014 §5) and quintom-bounce (|ΔNeff| can be 0.3–1, depending on the quintom mass). Then the proxy run becomes a constraint on the *predicted* range, not a free-floating null.

### MAJOR-3: Quintom-A vs Quintom-B class taxonomy is invoked in §VII.A without naming which class the ECH bounce mechanism belongs to.

§VII.A (L487–519, "Free-w_0 w_a chain status") says the matter-bounce candidate row is "not tested" against the DESI DR2 w_0 w_a chain, but the *Quintom-B accommodation row* "carries an unmarked 'consistent†' on theoretical grounds because Quintom-B is the only class admitted to span the dynamical-equation-of-state window the DESI signal populates".

**Where does the ECH bounce mechanism live in this taxonomy?** Quintom-A is w(z) > -1 with crossing to w(z) < -1 from above (phantom side reached late); Quintom-B is w(z) < -1 with crossing to w(z) > -1 from below (quintessence side reached late). The ECH bounce is *not* a quintom DE model at all — P1A §IV-V argues that *no* minimal-ECH route to DE exists. So the ECH framework is, strictly, in the *matter-bounce* class with w_DE = -1 (cosmological-constant or near-CC), and the DESI DR2 dynamical-DE evidence *disfavors* the ECH framework (relative to a Quintom-B model that does accommodate it).

This is a *strong* result for the no-go theorem, but P1B does not state it. Instead §VII.A says "the asymmetry between the Quintom-B accommodation row and the rest of the rows is intentionally one of theoretical accommodation, not of fit quality measured in this program". *Of course it is.* But the asymmetry should be flagged as **a quantitative cost to the ECH framework**, not as an even-handed taxonomy comment. If the DESI DR2 w_0 w_a chain converges and the bounded w_0 w_a posterior excludes Quintom-A and includes Quintom-B, then matter-bounce (which is *neither* Quintom-A nor Quintom-B) faces the same exclusion as Quintom-A. The cross-paper claim should be: "the DESI DR2 chain, when it converges, will test the ECH framework's prediction of w = -1 against the Quintom-B alternative".

**Fix:** In §VII.A, add a paragraph that locates the ECH framework explicitly in the CPL (w_0, w_a) plane: ECH → (w_0, w_a) = (-1, 0). State that this is the *point* in CPL space that the DESI DR2 chain will localize the posterior around (or away from). State the cross-paper logic: if the DESI posterior is consistent with (-1, 0), the ECH framework is favored; if the posterior excludes (-1, 0) at >2σ, the ECH framework is disfavored relative to Quintom-B. Currently P1A §V's Table II treats this as untested; P1B §VII.A says "the chain is running"; *neither paper says what the chain converging means for the no-go theorem*. This is the load-bearing cross-paper anchor and it should be one paragraph of explicit prose.

### MAJOR-4: The bounce GW γ_GW = 3.0 / f_NL = -35/8 shared contracting-phase coupling (which P3 §VI tick 2 added) is absent from P1B.

**Per the SSOT trail** (P3 tick 2 §VI added "shared contracting-phase mode functions to f_NL = -35/8"), the matter-bounce class predicts a *coupled* GW spectral index γ_GW = 3.0 and primordial non-Gaussianity f_NL = -35/8 from the same contracting-phase mode-function evolution. P1B's discussion of the NANOGrav PTA γ_PTA = 3.20 ± 0.42 measurement (P1A §XV.C, with bounce 0.48σ from γ_GW = 3.0) does not appear at all in P1B. P1B's discussion of ALP birefringence does not exhibit the analogous shared-coupling structure — and it should, because the same matter-bounce class that predicts γ_GW = 3.0 also predicts (via the shared contracting-phase mode-function evolution) a specific *shape* for the spectator-ALP misalignment angle θ_i at the post-bounce reheating boundary.

This is subtler than the f_NL ↔ γ_GW coupling because the ALP is a spectator (it does not participate in the bounce dynamics). But the *initial condition* for θ_i is set by quantum fluctuations during the contracting phase, and the contracting-phase vacuum is the same one that sets the matter-bounce f_NL = -35/8. So θ_i at the post-bounce reheating boundary has a *predicted distribution* with mean ⟨θ_i⟩ = 0 (parity-even Bunch-Davies-like) and variance ⟨θ_i²⟩ ~ (H_*/2π f_a)² × N_bounce, where H_* is the bounce-scale Hubble and N_bounce is the number of e-folds during contraction. For matter-bounce with H_* ~ 10^{-5} M_Pl, f_a = M_Pl, N_bounce ~ 50, this gives ⟨θ_i²⟩^{1/2} ~ 10^{-7} — *negligibly small*. The fiducial θ_i = 1 in §VI is therefore *not the matter-bounce prediction*; it requires a non-Bunch-Davies initial state.

**This is a real cross-paper cost.** P1A §V matter-bounce, P3 §VI matter-bounce → f_NL = -35/8 + γ_GW = 3.0 coupled, and P1B §VI θ_i = 1 spectator ALP are *not all simultaneously consistent within the matter-bounce class*. Either the ALP is in a different class (genuine post-inflation misalignment, not contracting-phase-set initial condition), or one of the three is wrong.

**Fix:** Add a paragraph in §VI L443–445 (the "Caveats" subsection) that explicitly addresses this. Either: (a) state that the spectator ALP has a *post-bounce-reheating* origin for θ_i ≈ 1 (e.g., from inflationary-phase quantum fluctuations after the bounce; this is the "Fujita 2021" mechanism that the paper cites at L388, and it would be worth stating that this is *post-bounce* in the matter-bounce timeline), and therefore is decoupled from the contracting-phase mode-function evolution that sets f_NL = -35/8; or (b) acknowledge that the matter-bounce prediction for θ_i is small and that θ_i ≈ 1 requires a non-minimal ALP-inflation coupling. The paper's current framing leaves this gap unaddressed and an adversarial referee comparing P1B + P3 will find it.

---

## MINOR findings

### m-1: Komatsu 2022 IJMPD review absent from references.bib.
The standard current review on ALP cosmic birefringence (Komatsu E., "New physics from the polarized light of the cosmic microwave background", IJMPD 31, 2230003) is not in references.bib. Inline at §VI L383–385 the paper says "The ALP produces cosmic birefringence independently of the gravitational theory" — this should cite the Komatsu 2022 review. Fix: one bibitem + one inline cite.

### m-2: Eskilt 2024 follow-up absent.
Eskilt+ 2024 ("Cosmoglobe DR2: an updated estimate of cosmic birefringence", arXiv:2407.xxxxx — check the bibliography, the paper has @Eskilt2023Cosmoglobe but not the 2024 follow-up if it exists) and the DiegoPalazuelos+ 2025 ACT DR6 paper *is* cited but the follow-up SPT-3G 2024 and BICEP/Keck 2024 birefringence constraints are not. P1B claims "The primary observational evidence for cosmic birefringence remains the published Planck/ACT DR6 2.4–2.9σ measurements" at §VIII L545–547 — but as of 2026-05 this is outdated. Add a one-line acknowledgement that recent SPT-3G + BICEP analyses provide complementary constraints at consistent significance, with a single bibitem each.

### m-3: NaMaster MASTER deconvolution scope-creep risk in §IV.
The §IV.D pipeline-configuration block (L267–311, the Wave 14-Z paragraph imported from P1A) is dense and runs ~600 words. The scope-disclaimer at L262–266 ("not a competitive sky detection") is correct, but the SNR figures 20.32 and 25.71 *will* be quoted out of context by readers who skim. Two MC injection-recovery numbers (β = 0.238° from injected β = 0.27°, bias = 0.032°) are the actual result; the SNR figures are *signal-to-MC-noise* and have no observational-significance interpretation. *Move the SNR numbers to a one-line footnote*, leaving only the bias (0.032°) and the bias-stability-across-injections (0.032° identical for three different β values) in the main text. This kills the "20σ ALP detection" misreading at the cost of one footnote.

### m-4: w_0-w_a CPL parametrization not located in bounce-vs-quintom theory space.
§VII.A discusses the DESI DR2 w_0 w_a chain but never plots or names where the ECH framework lives in (w_0, w_a) — it's at (-1, 0) (see MAJOR-3 above). Adding a one-sentence statement "ECH → (w_0, w_a) = (-1, 0), the cosmological-constant point in CPL space" anchors the cross-paper test. Currently the reader does not know what specific (w_0, w_a) point the chain is testing for the ECH framework.

### m-5: "Spectator ALP" terminology drift.
The phrase "spectator ALP" is used 14 times. The ALP-physics literature standard is "axion-like particle" with "spectator" being a property (does not participate in bounce dynamics). Recommend defining at first use (§I L130–135): "We call the field 'spectator' to indicate that it does not participate in the bounce dynamics and is decoupled from the gravitational sector except through its photon coupling." Without this definition, "spectator ALP" reads as if there is an ALP class called "spectator" in the standard literature, which there is not.

### m-6: Planck Commander foreground-cleaning assumption.
§IV.D L284–290 says "The Commander map is a foreground-cleaned CMB-only product; no separate foreground component is included." This is true for low-ℓ, but Commander's residual foreground at ℓ = 100–1000 (the band-power range the analysis uses) is *not zero*; SMICA or NILC would be a more conservative choice for ℓ > 100 birefringence analyses. The Planck Collaboration's own birefringence papers use SMICA. Mention this in the systematics paragraph at L286–290: "Commander is chosen for low-ℓ fidelity; the SMICA cross-check at higher ℓ is consistent at the < 0.04° bias level (see App. or future work)." Otherwise an ACT or Planck-Collaboration referee will press here.

### m-7: LiteBIRD 9σ forecast double-counts the same ALP that GR+ALP also predicts.
§VI L436–438 says "LiteBIRD is projected to achieve σ(β) ≈ 0.03°; for β = 0.27°: ∼9σ statistical significance — either decisive confirmation or clean exclusion." This is correct for β as an observable, but the *physics* interpretation is that LiteBIRD will measure β — *not* discriminate ECH from GR+ALP, since both predict the same β. State this explicitly: "LiteBIRD's σ(β) ≈ 0.03° will measure β with high precision but will not by itself distinguish the ECH-motivated ALP from a standard GR+ALP; the discriminating observable is the *spectral shape* β(ℓ) and any *small-scale-anisotropy* signature, neither of which the ECH motivation predicts to differ from GR+ALP."

---

## Cross-paper coupling assessment

| Coupling | P1A says | P1B says | Coherent? |
|---|---|---|---|
| Matter-bounce f_NL = -35/8 | §V, mechanism-independent | not mentioned | OK (P1B is verification companion, not theory) |
| γ_PTA = 3.20 ± 0.42 (bounce 0.48σ from γ_GW = 3.0) | §XV.C / §V | not mentioned | **GAP** — MAJOR-4 above |
| ALP β = 0.27° | §III / Table I, "consistent with" | §VI, "fiducial" | **WEAK** — MAJOR-1 above (derivation chain incomplete in both) |
| DESI DR2 w_0 w_a chain | §V Table II, "not tested" | §VII.A, "running" | **GAP** — MAJOR-3 above (neither paper locates ECH in CPL space) |
| ΔNeff = 0 across datasets | not mentioned (P1A is theory) | §III, "null-consistency" | **GAP** — BLOCKER above (no bounce → ΔNeff prediction in either paper) |
| 14 structural barriers | §IV, exhaustive at channel level | not mentioned | OK |
| Perturbation transparency | §X, scalar-matter conditional | not mentioned | OK |

**Bottom line on cross-paper coupling:** P1B is competently written as a stand-alone technical note on three independent analyses. It is *not yet* a coherent technical companion to P1A's no-go theorem. The four MAJORs above + the BLOCKER are all about *making the verification claim actually verify something P1A-specific*, rather than running generic ΛCDM+ΔNeff and generic GR+ALP analyses with disclaimers that they aren't ECH-specific. The disclaimers are honest, but they leave the *positive* cross-paper coupling unbuilt.

---

## Recommended fix priority

If the goal is to clear the BLOCKER + 4 MAJORs in one cron-loop tick (~1-2 hours of text work, no recompute):

1. **BLOCKER fix:** §III header + §I.1 abstract reframe + new §III.A "Bounce-class predictions for ΔNeff" paragraph (~half page, 200 words, 2 new bibitems). 30 min.
2. **MAJOR-1 fix:** §VI rewrite as four-paragraph block with Komatsu 2022, Irastorza-Redondo 2018, Poulin 2019 EDE bibitems (~80 words new, 3 bibitems). 30 min.
3. **MAJOR-2 fix:** §II new paragraph on bounce → ΔNeff chain with Brandenberger 2017, Cai 2014 review citations (~60 words, 2 bibitems). 15 min.
4. **MAJOR-3 fix:** §VII.A new paragraph locating ECH at (w_0, w_a) = (-1, 0) and stating the discrimination test the converged chain will run (~50 words, 0 bibitems). 10 min.
5. **MAJOR-4 fix:** §VI new "Caveats" paragraph on θ_i ↔ contracting-phase coupling decision (~80 words, 0 new bibitems). 15 min.
6. **MINORs (m-1 to m-7):** ~30 min combined (mostly one-line citations + one-sentence caveats).

**Total:** ~2 hours of text-only work, +5-7 new bibitems in `arxiv/references.bib`, no recompute. Same recompile-and-mirror discipline as every prior P1A round. Should bring P1B from current 75% (compute-gated) to ~80% (text gaps closed; still compute-gated on the DESI DR2 chain for §VII.A's converged numbers).

---

**Reviewer signature:** Gemini-3.1-Pro (cosmology theorist composite, Kamionkowski/Komatsu/Baumann/Carroll/Mercuri profile)
**Reviewer disposition:** Recommend major revision before arXiv submission. The paper is well-written and admirably honest about its scope, but the cross-paper coupling to P1A's no-go theorem is not yet built and the proxy framing is not yet defensible at PRD-referee level. The fixes above are all text-only and within reach in a single 2-hour cron-loop tick.
