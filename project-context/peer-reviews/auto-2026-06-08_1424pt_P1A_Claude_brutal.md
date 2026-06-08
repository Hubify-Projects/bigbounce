# P1A auto-2026-06-08_1424pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (12960 chars)
**Wall time**: 445.9s

---

# Referee Report: P1A — "Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"

## Overall Assessment

This manuscript attempts to establish a "channel-level no-go" for four enumerated minimal Einstein-Cartan-Holst (ECH) routes to dark energy, supplemented by a "perturbation-transparency theorem" for scalar matter. The author is admirably forthcoming about the limitations of the work — perhaps to a fault, as the abstract and body together undermine virtually every load-bearing claim through layered hedges. The paper reads less like a PRD research article and more like a self-critical audit log of a defunct research program, with extensive caveats, references to "companion papers in preparation," and confessions that the central dimensional ansatz is "not a derivation."

The core technical content that survives scrutiny is: (i) a well-known observation that torsion vanishes for canonical scalars and the Holst term becomes the Pontryagin density (this is textbook — not a theorem); (ii) a phenomenological scaling ansatz acknowledged to have wrong off-shell mass dimension; and (iii) an enumeration of 14 "barriers" of mixed novelty (the paper itself classifies some as "structural/philosophical observations"). None of this rises to PRD novelty standards.

The manuscript is also riddled with internal inconsistencies, self-superseding statements, duplicated phrasing, and a heavy reliance on "companion papers in preparation" for the actual computational verification of claims this paper makes.

---

## ESSENTIAL Findings

### P1A-E1 — Abstract/Body: Central claim is acknowledged to NOT be a theorem (pages 1, 3, 8)
The abstract states: *"This is a channel-level assessment, not an operator-level theorem: the four enumerated routes (NJL, one-loop EA, Immirzi running, parity-CMB) are not proven to be a complete diffeomorphism-invariant operator basis..."*

The paper's title and headline claim is "Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes." But the author explicitly admits the four routes do NOT span the relevant operator space — the Jackiw-Pi gravitational Chern-Simons term and parity-odd four-fermion partner are excluded. A "closure" of an incomplete enumeration is not a closure. This is the central conceptual flaw and renders the title misleading.

**Required fix:** Either (a) enumerate and close the full dimension-6 parity-odd operator basis as part of this paper, or (b) drastically retitle to "Phenomenological assessment of four selected ECH routes" and remove all "no-go," "closure," and "theorem" language throughout.

### P1A-E2 — Appendix B: Central dimensional ansatz is wrong by 3 mass dimensions (page 19)
Equation (B1): *"[L_odd] = +1"* — three units short of the +4 required for a Lagrangian density. The author then writes ρ_Λ^bounce ~ (α/M) M_Pl^5 and admits *"as a phenomenological on-shell scaling ansatz, not a controlled EFT result."*

This is not a peripheral technicality — it is the dimensional foundation of the entire dark-energy mapping (Sec. II C, Eq. 10) and of the structural-tension argument (Sec. XIV D). A PRD paper cannot rest its central numerical claims on an operator of incorrect mass dimension, then fix it via on-shell scaling. The Ξ ~ 10^-123 result, the N_tot ≈ 92 result, and the entire fine-tuning bookkeeping are then phenomenological number-juggling, not physics.

**Required fix:** Construct a dimension-+4 operator from first principles, or remove all numerical claims (Ξ ~ 10^-123, N_tot ≈ 92, 10^-2 prefactor) that depend on the ansatz.

### P1A-E3 — Abstract: β = 0.27° "prediction" is explicitly NOT an ECH prediction (page 1)
The abstract states: *"spectator-ALP birefringence β ≈ 0.27° is a benchmark consistency point, not an ECH prediction... the same benchmark arises in any GR+ALP setup with the same parameters and is not derived from the ECH action."*

Yet Sec. III A discusses CMB E-B correlations as an "observational signature," Sec. XII B presents it as a result, Sec. XV lists it as a "surviving test," and Figure 1 shows it as an ECH-class observable. The paper repeatedly leverages this number to suggest empirical content where none exists. This is misleading.

**Required fix:** Remove β ≈ 0.27° from the surviving-predictions list entirely. It is neither a prediction of the framework nor a discriminator.

### P1A-E4 — Abstract: f_NL = -35/8 is explicitly NOT an ECH prediction (page 1)
The abstract states: *"f_NL = −35/8 is a property of the matter-bounce class [1], derived from the contraction-phase cubic action with no ECH input."*

Yet the paper repeatedly cites this as the "surviving testable prediction" (Sec. XIII, Sec. XV, Table I, Figure 1). If it has "no ECH input," it has nothing to do with this paper. The author is using a result from Cai et al. 2009 [1] as the headline empirical content of their own paper.

**Required fix:** Remove f_NL = -35/8 as a result of this paper. Restrict to citing [1] in the related-work section.

### P1A-E5 — N_tot = 92 vs N_tot = 94 internal inconsistency (pages 4, 7, 17, 19)
Multiple values cited for the same quantity:
- Page 3: *"N_tot ≈ 92 post-bounce e-folds"*
- Page 7: *"Matching ρ_Λ ≈ (2.3 meV)^4 requires N_tot ≈ 92"*  
- Page 19 (Appendix B): *"giving N_tot ≈ 122 ln 10/3 ≈ 94 e-folds"* and *"(consistent at the ∼2% level with the structural-tension N_tot ≈ 92)"*

The author admits the discrepancy comes from the ansatz choice in Eq. (B2). But the structural-tension argument in Sec. XIV D depends on N_tot ≈ 92 — *exactly* — to drive the conclusion that the f_NL signature is erased. If N_tot is uncertain by ±2 e-folds due to a known ansatz dependence, the "structural tension" loses analytic teeth: the relative differential N_tot − N_exit ~ 32 is presented as a precise number when it itself depends on the off-by-3-dimensions ansatz.

**Recompute check:** 120 × ln(10)/3 = 120 × 2.3026/3 = 92.1, not 94. The author writes "122 ln 10/3 ≈ 94" — but 122 × 2.3026/3 = 93.6 ≈ 94. So the discrepancy reflects 120 vs 122 OOM hierarchy. The text says "∼ 120 orders of magnitude (not the ∼ 35 misstated in earlier drafts: the bounce-scale density is ρ_bounce ∼ M_Pl^4, not the local pseudo-density ρ_Λ^bounce ∼ 10^−2 M_Pl^4 that Eq. (B2) labels)."

**Required fix:** Pick one self-consistent number with explicit uncertainty propagation through the structural-tension argument. The "∼ 35 misstated in earlier drafts" is internal version-history that must not appear in a submitted paper.

### P1A-E6 — Internal version-history / draft-bookkeeping language in body (pages 9, 15, 19)
The following appear in the published-version body text, not the appendix:
- Page 9: *"This figure supersedes the earlier synthetic-Gaussian-likelihood value γ = 3.20 ± 0.42 used in pre-real-KDE drafts; the migration is documented in Paper III § 6."*
- Page 15: same content repeated
- Page 19: *"the ∼ 35 misstated in earlier drafts"*

This is internal draft-history that does not belong in a PRD submission. Flag each occurrence ESSENTIAL per reviewer instructions #8.

**Required fix:** Strike all "supersedes," "earlier drafts," "misstated in earlier drafts" language. Quote only the current value with provenance, not the audit trail.

### P1A-E7 — Companion-paper dependence undermines self-containment (multiple pages)
The paper repeatedly defers core verification to *"companion work in preparation [2, 6, 23, 46]"*. Specifically:
- MCMC verification of all ΛCDM+∆N_eff cosmological parameter values (Paper I(b))
- NaMaster pipeline validation (Paper I(b))
- ALP MCMC parameter fitting (Paper I(b))
- f_NL Fisher forecast (Paper II)
- Galaxy chirality classifier results (Paper IV)
- Multi-survey anomaly catalog (Paper III)

All four cited "companion papers" are "in preparation" and not publicly posted. The author writes (page 5): *"should be read as internal-analysis inputs to the present structural argument rather than as independently peer-reviewable values until Paper I(b) is publicly posted."*

A PRD submission cannot rely for verification on four unpublished, non-arXiv, non-peer-reviewed manuscripts by the same author. The paper as submitted is not independently verifiable.

**Required fix:** Either (a) post the companion papers to arXiv simultaneously and cite arXiv IDs, or (b) include the verification material as supplementary sections of this paper, or (c) remove all claims dependent on companion-paper verification.

### P1A-E8 — Perturbation-transparency "theorem" is textbook material misrepresented as novel (Sec. X, page 14)
The five-step "proof" in Sec. X B is elementary:
1. Canonical scalar has no spin density (textbook, Hehl 1976)
2. Torsion vanishes (textbook)
3. Connection reduces to Levi-Civita (textbook)
4. Holst term → Pontryagin density (well known since Holst 1996, Mercuri 2009)
5. Total derivative contributes nothing (calculus)

The author calls this a "central result" and claims it "generalizes Hehl et al. (1976) to the Holst sector and to all perturbation orders." This is overclaim. The result that the Holst term reduces to a topological density on the Levi-Civita connection is the *defining* feature of the Holst term — it is why γ is invisible in pure gravity and only becomes physical with fermions (the entire point of Freidel-Minic-Takeuchi 2005, cited as [15]).

**Required fix:** Either present this as a textbook observation in the framework section and not as a "result," or identify what is genuinely new beyond Hehl 1976 + Holst 1996 + Mercuri 2009.

### P1A-E9 — Route 2 amplitude calculation has factor-of-10^25 ambiguity not addressed honestly (Sec. IV B, page 9)
Eq. (15) gives *"∼ 10^-58 to 10^-60"* — a factor-of-100 range claimed to reflect "ε-correction perturbative-order scaling alone." But the text then says *"An alternative ordering that contracts the H_0 factor with the dimensionful coupling differently yields a numerically distinct ∼ 10^-33 ratio."*

A 25-orders-of-magnitude discrepancy between contraction orderings is not "perturbative-order scaling" — it indicates the dimensional analysis is not under control. The author cannot wave this away with *"the qualitative closure statement that Route 2 lies below the observed birefringence amplitude by ≳ 30 orders of magnitude survives any reasonable dimensional reconciliation."*

**Recompute check:** With α_em/(4π) ≈ 5×10^-4, H_0/M_Pl ~ 10^-61, M_Pl·(α/M) ~ 10^-2, β_obs ~ 6×10^-3:
- Numerator: 5×10^-4 × 10^-61 = 5×10^-65
- Denominator: 10^-2 × 6×10^-3 = 6×10^-5
- Ratio: ~8×10^-61

This gives ~10^-60, but Eq. (15) as written contains factors of M (the area-gap mass) that are not specified numerically, so the calculation is not reproducible.

**Required fix:** Resolve the 10^-33 vs 10^-60 ambiguity with a single, dimensionally consistent calculation. State exactly which Planck-mass factor goes where.

### P1A-E10 — Route 4 "closure" is not actually a closure (Sec. IV D, page 10)
The author writes: *"R4 therefore relocates the cosmological-constant problem rather than solving it. The inequality is rigid only under the one-loop matching assumption; with α/M floated, the spectator-ALP class is recovered as a viable parity-odd source..."*

This is a confession that Route 4 is NOT closed at the amplitude level. The header literally reads *"naturalness objection rather than amplitude no-go."* Yet the paper's central claim is a 4-route closure. This is a 3-of-4 closure with a naturalness preference, not a no-go.

**Required fix:** Revise title and abstract to reflect that one of the four routes is not amplitude-closed. The title "Channel-Level Closure of Four Minimal..." is false as written.

### P1A-E11 — Figure 1 caption contradicts paper content (page 4)
Figure 1 marks ECH/torsion as *"structurally closed (this paper)"* with a dashed red line to "w_0 w_a DE." But:
- The paper does not establish structural closure (E1, E10 above)
- "Structurally closed" is presented unconditionally despite the abstract's extensive caveats
- The arrow from "Matter bounce" to "f_NL = -35/8" is colored as ECH-permitted, yet the paper insists f_NL = -35/8 is NOT an ECH prediction (E4)

**Required fix:** Redraw Figure 1 to be consistent with the abstract's actual scope-limited claims, or remove it.

### P1A-E12 — Table III ✓ for matter-bounce f_NL contradicts E4 (page 16)
Table III shows "✓" for matter bounce producing f_NL = -35/8 with the parenthetical "(any host; not ECH-specific)." But the table is titled *"Discrimination among bouncing cosmologies and inflation by observable channels"* — implying the table demonstrates ECH-relevant discrimination. The author elsewhere explicitly disclaims this as an ECH result.

**Required fix:** Either remove the table or explicitly mark that no ECH-specific row exists.

### P1A-E13 — Eq. (10) ω parameter never defined; cosmic rotation framework introduced and abandoned (page 6)
Eq. (10): *"Λ_eff = Ξ M_Pl^2 + c_ω ω^2"* — the cosmic rotation ω is introduced with the constraint (ω/H)_0 < 5×10^-11, declared "completely negligible," and never used again. Yet Sec. II C is titled "Cosmic Rotation and Dark Energy" and the introduction (page 3) frames the model around inherited rotation from a parent black hole.

**Required fix:** Either develop the rotation phenomenology or remove it entirely.

### P1A-E14 — H_0 = 67.68 ± 1.06 km/s/Mpc cited as "MCMC verification" without verifiable source (Table I, IV; pages 4, 8, 20)
Table IV cites H_0 = 67.68 ± 1.06 km/s/Mpc with provenance *"Recovers ΛCDM"* from companion Paper I(b). This value is not derived in this paper and Paper I(b) is "in preparation." Citing your own unpublished work as a verification is circular and not acceptable in PRD.

**Required fix:** Remove all numerical cosmological parameter claims, or post Paper I(b) to arXiv prior to PRD submission and cite the arXiv ID.

### P1A-E15 — Fine-tuning hierarchy claim 10^120 → 10^5 contradicts E2 dimensional analysis (page 7)
Page 7: *"This reparameterizes the fine-tuning hierarchy from 10^122 (the genuine M_Pl^4/ρ_Λ^obs cosmological-constant hierarchy; see Appendix B) to ∼ 10^5 as sensitivity to ∆N_tot ≈ 4 e-folds."*

The 10^5 number derives directly from the dimensionally inconsistent ansatz (E2). The author then concedes *"We emphasize that this is bookkeeping, not progress."* If the whole reduction is bookkeeping built on a wrong-dimension ansatz, it should not be presented as a quantitative result.

**Required fix:** Either justify the dimensional manipulation rigorously or strike the 10^120 → 10^5 reduction claim.

---

## MAJOR Findings

### P1A-M1 — "13 logically-independent constraints" is rebranded "14 barriers" with B8/B14 collapse (pages 1, 4, 12, 18)
The paper repeatedly oscillates between "13 logically-independent" and "14 historical catalog entries." The author admits B8 (parity-even interaction) is "subsumed by B14" (perturbation transparency). This is not 13 logically independent constraints — it is 13 + 1 redundant entry. Why catalog the redundancy?

**Required fix:** Drop B8 and call it 13. The "historical catalog" framing is internal-bookkeeping.

### P1A-M2 — Barrier classification reveals weakness (page 12)
The author classifies the 14 barriers:
- Novel (9): Barriers 1, 2, 3, 4, 8, 10, 11, 12, 14
- Known (4): Barriers 5, 6, 7, 9 — "scale separation, attractor-sensitivity dilemma, parameter immunity, Liouville conservation"
- Structural/philosophical (1): Barrier 13 — "gravitational democracy"

So 5 of 14 barriers are admitted to be either textbook or "philosophical." And B8 is redundant with B14 (M1). That leaves at most 8 "novel" barriers — half what the headline claims.

**Required fix:** Honestly recount and prune to the genuinely novel barriers.

### P1A-M3 — "Reheating thermal-reset barrier" is asserted, not derived (pages 7, 15)
The reheating argument introduced on page 7 claims thermal C/P-violating scattering rates wash out ⟨J⁵_μ⟩ → 0. This is presented as an *"independent thermodynamic closure"* but no rate estimate, no comparison to the Hubble rate, no specification of which "C/P-violating scattering rates" — just assertion.

**Required fix:** Provide an actual estimate of the relevant rate (e.g., weak-interaction axial-current relaxation) compared to H at T_reh, or remove the argument.

### P1A-M4 — Eq. (11) derivation is admitted hand-waving (page 6-7)
The (T_reh/M_GUT)^(3/2) factor is justified as: *"justified here on dimensional / phase-space grounds for the axial-current variance"* and *"this thermal phase-space factor is not identifiable with the Mercuri & Capozziello [22] one-loop coefficient α_em/(4π)... is therefore treated as a phenomenological phase-space ansatz, not as derivable from the one-loop anomaly coefficient."*

A 3/2 power is then numerically critical (it determines the prefactor multiplying the dominant exponential), yet the author admits it is not derived. This invalidates the structural-tension N_tot ≈ 92 result quantitatively.

**Required fix:** Either compute the prefactor properly or replace the N_tot ≈ 92 claim with an explicit order-of-magnitude bound only.

### P1A-M5 — Eq. (16) Immirzi running ansatz contradicts the cited literature (page 9-10)
The paper introduces *"the one-loop running ansatz"* dγ/d ln μ = (1/12π²)(N_F^L − N_F^R)γ + O(γ²), but the next paragraph admits: *"The actual fermion-induced perturbative running of the Immirzi parameter is computed by Benedetti & Speziale [27], who find a β-function whose sign depends on |γ| through four-fermion interactions generated when fermions are coupled to the Holst sector; our Eq. (16) is a chiral-count EFT bound rather than the full perturbative result."*

So the actual published result (Benedetti & Speziale) is referenced as different, but the paper uses an ad-hoc ansatz. The Δγ/γ ~ 10^-2 numerical claim then has no basis.

**Required fix:** Use Benedetti & Speziale's actual β-function, or restrict to a bound that is justified.

### P1A-M6 — Pontryagin density does NOT integrate to a boundary term on a general FRW background (Sec. X D, page 14)
Eq. (23): the Pontryagin density *RR is identically zero on a maximally symmetric FRW background (no parity violation at the background level). At the perturbation level it is non-zero pointwise but its integral over a homogeneous spatial slice still vanishes (or is a boundary term). However, the author writes Eq. (23) as ∂_μ K^μ — this is the standard Chern-Simons identity for the Pontryagin density, but K^μ depends on the connection in a non-covariant way. The statement that this "contributes nothing to variational equations at all orders" is true only modulo proper boundary terms. The proof in Sec. X B step 4 is too cursory for a "theorem."

**Required fix:** Provide rigorous treatment of boundary contributions, or downgrade language.

### P1A-M7 — Eq. (4) factor of 3πG_N/2 is not the standard Hehl-Datta coefficient (page 5)
Eq. (4): L_int = −(3πG_N/2) × γ²/(γ²+1) × J⁵_μ J⁵^μ. Compare to Eq. (13) which gives L_NJL = -(3/16)κ(ψ̄γ^a γ⁵ψ)². With κ = 8πG, this gives -(3/16)(8πG) = -(3πG/2) — consistent with Eq. (4) if γ→∞. But Eq. (4) introduces γ²/(γ²+1) suppression which is the Freidel-Minic-Takeuchi Holst-corrected coefficient. At γ = 0.274, this factor is 0.075/1.075 ≈ 0.07 — a strong suppression that is not propagated through Sec. IV A's amplitude estimate.

**Required fix:** Either include the γ²/(γ²+1) factor consistently or explain the inconsistency.

### P1A-M8 — Galaxy spin "underpredicts by > 100 orders of magnitude" is meaningless without amplitude definition (pages 7, 16, 17)
Repeatedly the paper claims ECH coupling *"underpredicts any plausible spin asymmetry by > 100 orders of magnitude"*. But A₀ — the dipole amplitude — is not defined, and the relevant order-of-magnitude estimate is not provided in this paper. The claim is therefore unverifiable.

**Required fix:** Provide the actual calculation, or remove the claim.

### P1A-M9 — Table I, footnote b: "3-5σ realistic after full systematic budget" is overclaim (page 4)
The footnote acknowledges this rests on Heinrich+2024 σ(f_NL) ≈ 0.7 (Fisher-ideal) degraded to "3-5σ realistic" after GR-projection, b_ϕ uncertainty, and photo-z degradation. The "3-5σ" range is given but the *computation* is in "companion work in preparation [2]." Citing your unposted future paper for the headline forecast is not acceptable.

### P1A-M10 — NANOGrav γ comparison: "real-KDE re-analysis" cited but not provided (pages 15, 17, 20)
Page 15: *"NANOGrav model comparison: γ = 2.567 ± 0.382 from real-KDE reanalysis of the 15-yr free-spectrum data (GPU MCMC, companion Paper III [46])."* This re-analysis is not derived here and exists only in an unpublished paper. The +1.13σ tension with matter-bounce γ = 3.0 is then claimed *"consistent with the data within standard frequentist tolerance"* — but the comparison cannot be evaluated without the underlying analysis.

### P1A-M11 — Table III footnote ‡ is an extended running-chain progress report (page 16)
The footnote describes a still-running w_0 w_a MCMC chain with "∼3.8×10^4 accepted samples" and "R̂ − 1 ≈ 3×10^-2", explicitly deferring conclusions until convergence. This is a draft-state progress note that does not belong in a PRD paper.

**Required fix:** Either complete the chain and report results, or remove the row from the table.

### P1A-M12 — Eq. (17) ALP birefringence formula is wrong (page 10)
β = (α/M) Δθ_{rec→today} ~ (α/M) √(2ρ_θ/m_θ²)

The standard cosmic-birefringence formula for an ALP with mass m_θ and field amplitude θ₀ is β = (α/M) (θ_today − θ_rec). For a slowly-rolling ALP θ̇ ~ m_θ θ at oscillation, and θ_0 ~ √(2ρ_θ)/m_θ. So β ~ (α/M) √(2ρ_θ)/m_θ, NOT √(2ρ_θ/m_θ²). The units of the author's expression: [√(ρ_θ/m²)] = √(E^4/E²) = E — but β should be dimensionless. The author's expression gives β dimensions of [(α/M)] × [E] = [E^-1] × [E] = dimensionless. OK so it works out, but the radical sign placement is misleading. Re-derivation gives the same numerical conclusion, so this is presentational rather than fatal.

### P1A-M13 — Forecast claim of "9σ LiteBIRD detection" then walked back (page 18)
*"LiteBIRD (σ(β) ≈ 0.03°, early 2030s) detects non-zero β at ∼ 9σ (a 0.27°/0.03° overall sensitivity number)... LiteBIRD's σ(β) = 0.03° will not by itself separate the spectator-ALP value from the current WMAP+Planck birefringence central value in a model-discrimination test."*

So "9σ" is technically a zero-vs-signal test, while model discrimination is ~0.73σ. Presenting "9σ" in the conclusion is misleading.

**Required fix:** Lead with the model-discrimination number (0.73σ), not the zero-baseline number.

### P1A-M14 — DESI 2024-2025 BAO σ values misquoted (page 3)
*"DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ (dataset-dependent) [9, 10]"* — the DESI DR2 paper cited [10] (arXiv:2503.14738) reports values dependent on dataset combinations. The 3.1-4.2σ range should be sourced precisely to specific dataset combinations within that paper, not vaguely.

### P1A-M15 — Page 1, footnote a in Table I, page 4 conflict
Table I footnote a: *"Reparameterized as sensitivity to N_tot; not solved."* So the table answers "Can bounce derive dark energy? Phen. assumption required." — but the headline of the paper says "channel-level closure," which is *"no, bounce cannot derive dark energy."* The table softens the answer; this is inconsistent.

### P1A-M16 — Bibliography issue: Reference [44] arXiv ID looks wrong (page 21)
*"[44] Y.-F. Cai and J.-H. Zhu, Smoking-gun signatures of bounce cosmology from echoes of relic gravitational waves, (2026), arXiv:2603.13924"*

arXiv IDs follow YYMM.NNNNN format. "2603" is not a valid year-month (March 2026 would be 2603, which is the future). This is either a fake/anticipated arXiv ID or a typo. Cannot exist as of publication date June 2026 unless very recent.

**Required fix:** Verify arXiv ID; if speculative future reference, remove.

### P1A-M17 — Bibliography [47] is "available upon request" — not citable (page 21)
*"[47] H. Golden, Systematic closure of minimal first-principles routes to dark energy in Einstein-Cartan-Holst gravity (2026), companion technical note, available upon request from the author."*

PRD does not accept "available upon request" citations as load-bearing references.

---

## MINOR Findings

### P1A-Mi1 — Duplicate/triplicate caveats (pages 1, 3, 17)
The same warnings about ansatz status, channel-level vs operator-level, and "perturbation-transparency restricted to canonical scalar matter" appear repeatedly. Tighten.

### P1A-Mi2 — Page 1 abstract is 1200+ words
PRD abstracts should be ~250 words. This abstract is roughly 5× too long.

### P1A-Mi3 — "WMAP+Planck Eskilt & Komatsu" attribution inconsistency
Throughout the paper, β_obs = 0.342° ± 0.094° is repeatedly attributed to "Minami & Komatsu [3]" and "Eskilt & Komatsu [4]." Be consistent — Eskilt & Komatsu (2022) is the refined value cited.

### P1A-Mi4 — Section IV "Closure summary" repeats Sec. IV text verbatim (page 11)
Sec. IV E is mostly redundant with the route-by-route narrative. Cut.

### P1A-Mi5 — Page 5 typo / inconsistency
*"309,189 frozen accepted samples across two converged dataset combinations: 176,240 full-tension + 132,949"*: 176240 + 132949 = 309189 ✓ (arithmetic OK).

### P1A-Mi6 — Figure 2 (page 5) caption refers to ansatz acknowledged elsewhere as wrong (E2)
Figure 2 illustrates the energy hierarchy from ρ_bounce ~ 0.27 ρ_Pl to Λ_obs via "× e^{-3N}". Caption admits *"This ansatz is dimensionally correct on-shell at the bounce but is not derived from the ECH action."* If the figure illustrates a non-derivation, why include it? It is decorative at best, misleading at worst.

### P1A-Mi7 — Eq. (2) γ_SU(2) ≈ 0.274 reported with "apparent uncertainty range is scheme dependence rather than statistical or theoretical error" (page 5)
This is a textbook fact but appears throughout the paper without a single source citation in the equation context. References [16-18] are listed but not co-located.

### P1A-Mi8 — Table II numbering: "B8 is subsumed by B14" but both rows kept (page 13)
Either delete the B8 row from the table or explicitly mark it as "subsumed (kept for historical completeness)." Currently both appear without table-level annotation.

### P1A-Mi9 — Reference [23] Galaxy Chirality paper title cites *"8.47M Galaxies Classified, Hemisphere Null at p_LEE < 10^-4"* — this contradicts the text claim of "DESI Legacy DR8" sample being "full" (Section VI)
Inconsistent reference between body and citation.

### P1A-Mi10 — Repeated sentence on page 5: *"PACS numbers"* are listed but no journal format check
PACS numbers are not used in modern PRD; PRD uses descriptor categories. Replace.

### P1A-Mi11 — Acknowledgment of AI assistance is at PRD-acceptable level but could be tightened
Page 18 disclosure of "Claude (Anthropic) as AI research assistant" is acceptable; verify this matches APS author-disclosure policy.

---

## NIT-Level Findings

### P1A-N1 — *"(in preparation)"* appears 6+ times in bibliography (pages 19-21)
Not citations, drafts.

### P1A-N2 — Page 4 Figure 1 right column item "PTA γ = 3.0" vs page 15 "γ = 3.0 sits at +1.13σ"
The figure should display the tension explicitly, not just γ = 3.0.

### P1A-N3 — Page 19 Table IV column header "Notes" gets cut off mid-line (LaTeX overflow)
Cosmetic but unprofessional.

### P1A-N4 — Duplicate phrasing: *"channel-level closure under stated assumptions"* appears ~15 times
Vary phrasing or accept the redundancy.

### P1A-N5 — Page 3 *"DESI 2024–2025"* — DESI DR2 results are 2025 (March), so the range is correct, but minor stylistic issue: pick one year if citing a single result.

---

## Page-Count Assessment

The paper is 21 pages. The genuinely novel content (if any) — the four-route enumeration + 14-barrier catalog — could fit in a 6-8 page Letter or 10-page PRD article. The hedging, version-history, repeated caveat blocks, and companion-paper deferrals inflate the length. **Recommended maximum: 10 pages** if all ESSENTIAL findings are addressed; **rejection** if not.

---

## Summary recommendation

**REJECT**

This paper does not meet the PRD standard for novelty, rigor, or self-contained verifiability. The central "channel-level closure" claim is acknowledged in the abstract to not be a theorem, to depend on a dimensionally incorrect on-shell scaling ansatz (Appendix B confesses operator dimension +1 instead of +4), and to leave the relevant operator basis (Jackiw-Pi gravitational Chern-Simons, parity-odd four-fermion partner) unanalyzed. The two "surviving" empirical predictions are explicitly disclaimed as not being ECH predictions. Route 4 is conceded to not be amplitude-closed but reframed as a "naturalness objection." The perturbation-transparency "theorem" is textbook material (Hehl 1976 + Holst 1996 + Mercuri 2009) presented with a five-step elementary proof. Verification of all numerical claims — H_0, ∆N_eff, σ(f_NL), γ_PTA, ALP MCMC, NaMaster pipeline — is deferred to four unpublished "companion papers in preparation," rendering the paper not independently reproducible. The text contains internal version-history language ("supersedes earlier draft," "misstated in earlier drafts") that should never appear in a submitted manuscript, alongside a still-running MCMC chain progress report in a table footnote. Three of the headline numbers (N_tot ≈ 92, 10^-58 Route-2 amplitude, 10^120 → 10^5 fine-tuning reduction) are internally inconsistent or rest on admitted hand-waving. The author's commendable honesty about these limitations does not rescue a paper whose stated central claim is repudiated by its own caveats. A complete rewrite restricting scope to genuinely demonstrated content (probably a short methods note pointing out which ECH operator routes face which amplitude bounds, with full operator-basis closure deferred to future work) would be more appropriate.

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional Findings — Fresh-Eyes Re-Examination

## ESSENTIAL — Additional

### P1A-E16 — Figure 2 vs body: N=55 / dilution ~10⁻⁷² contradicts text N=92 / dilution ~10⁻¹²¹ (page 5)

Figure 2 annotation: "After inflationary dilution (N = 55 e-folds)" with "× e^(−3N) (~ 10⁻⁷²)".

Verification: e^(−3×55) = e^(−165) ≈ 2.6×10⁻⁷² ✓ — the figure's arithmetic is *internally* consistent.

But the body text page 7 says "Matching ρ_Λ ≈ (2.3 meV)⁴ requires N_tot ≈ 92" and page 15 says "Ξ ≈ 10⁻¹²³, decomposed as 10⁻² × D_inf with D_inf ~ 10⁻¹²¹." Page 19 Appendix B says "N_tot ≈ 122 ln 10/3 ≈ 94 e-folds."

So Figure 2 displays N=55, D_inf~10⁻⁷², while the body uses N=92–94, D_inf~10⁻¹²¹. These are wildly different numbers attached to the SAME quantity in the SAME paper. Figure 2 is either stale (from an earlier draft) or based on a different ansatz that is not flagged.

**Required fix:** Reconcile Figure 2 with the body. If Figure 2 represents an alternative ansatz, that must be stated in the caption. Otherwise update the figure to N=92, D_inf~10⁻¹²¹.

### P1A-E17 — Eq. (23) misidentifies the Holst-dual contraction with the Pontryagin density (Sec. X D, page 14)

Eq. (23): "R̃(Γ̊) = ½ ε^μνρσ R_μνρσ(Γ̊) = ½ *R R ≡ ∂_μ K^μ (Pontryagin density; total derivative)."

These are two structurally different objects:
- **ε^μνρσ R_μνρσ** (one factor of R) — this *vanishes identically* on the Levi-Civita connection by the algebraic Bianchi identity R^μ_[νρσ] = 0, since the antisymmetrization in [μνρσ] of R_μνρσ picks out the cyclic identity. It is zero, not a total derivative.
- **ε^μνρσ R_μν^αβ R_ρσαβ** (two factors of R) — this *is* the Pontryagin/Chern-Pontryagin density ∝ *RR, generically nonzero pointwise, equal to ∂_μ K^μ where K^μ is the gravitational Chern-Simons 3-form.

The Holst term itself is (1/γ) ε_abcd e^a ∧ e^b ∧ R^cd, which on the torsion-free connection reduces (via the first Bianchi identity in the form R^a_b ∧ e^b = 0) to a vanishing/total-derivative expression — it does *not* become the Pontryagin density ∝ R²*. Mercuri's reconstruction shows the Holst term combines with the non-minimal fermion coupling to produce the Nieh-Yan invariant, not the Pontryagin invariant.

This affects:
1. **Sec. X B step 4** ("Holst term becomes topological. The Holst term evaluated with the Levi-Civita connection gives ½ ε^μνρσ R_μνρσ(Γ̊), which on a torsion-free connection is the Pontryagin density ∝ RR̃.") — wrong identification.
2. **Abstract** ("the Holst dual contraction ε^μνρσ R_μνρσ reduces on the Levi-Civita connection to the Pontryagin density ∝ RR̃") — repeats the same error.
3. **The conclusion** still holds (zero is trivially a "total derivative"), but the reasoning is misstated, which matters for the "extension to nonperturbative parity channels" argument: if the Holst term reduces to genuine ∝ R*R, it could in principle source primordial GW birefringence through the gravitational Chern-Simons mechanism (Jackiw-Pi); if it reduces to zero, the entire connection to nonperturbative parity channels through *this* operator is severed.

A PRD-level "central result" cannot rest on a misidentification of two fundamentally different topological invariants.

**Required fix:** Either (a) demonstrate explicitly that the Holst term reduces to the Pontryagin density on the Levi-Civita connection (it does not, by Bianchi), or (b) correctly state that the Holst term vanishes (modulo Nieh-Yan boundary terms) on the Levi-Civita connection, which then weakens but does not destroy the perturbation-transparency conclusion. In either case, the abstract sentence is wrong.

---

## MAJOR — Additional

### P1A-M10 — 1.4σ consistency claim between WMAP+Planck and ACT DR6 is incorrectly computed (page 10)

Page 10: "[Eskilt & Komatsu β = 0.342° ± 0.094°] ... [ACT DR6] β = 0.215° ± 0.074° at ∼2.9σ, consistent within ∼ 1.4σ".

The correct two-sided difference test:
Δβ = 0.342° − 0.215° = 0.127°
σ_combined = √(0.094² + 0.074²) = √(0.008836 + 0.005476) = √0.014312 = 0.1196°
Δβ/σ_combined = 0.127/0.1196 = **1.06σ**

The paper's "1.4σ" matches dividing by the larger single uncertainty alone: 0.127/0.094 = 1.35σ — a non-standard procedure that overstates tension and is methodologically incorrect for combining two independent measurements.

Both methods compare different null hypotheses without flagging. Per reviewer instruction E (null-procedure comparability), this is a flag.

**Required fix:** State 1.06σ (or whatever the author intends as the correct combination) with explicit formula.

### P1A-M11 — Sec. IV "three technical aspects" admits the M_Pl³ vs M_Pl⁵ choice is free, but this is the entire dark-energy mapping (page 8)

Page 8 item (a): *"the dimensional reconstruction of ρ_Λ^bounce in Appendix B requires an internally consistent mass-dimension accounting between (α/M) M_Pl³ (dimension +2) and the equivalent rewriting [(α/M) M_Pl] M_Pl⁴ (dimension +4); the choice of M_Pl⁵ vs. M_Pl³ controls the subsequent N_tot ≈ 92 bookkeeping."*

These are *not* "equivalent rewritings" — they differ by a factor of M_Pl² ≈ 10³⁸ GeV². The author then says the choice "controls" the result. So the central N_tot ≈ 92 number is parametrically sensitive (38 orders of magnitude in M_Pl² ≈ 12.7 e-folds difference) to an unjustified dimensional choice.

Verification: M_Pl² ~ 10³⁸ GeV² corresponds to ln(10³⁸)/3 ≈ 29 e-folds difference. The author's quoted 92 vs 94 (∼2 e-folds) does *not* reflect the actual ∼29 e-folds the M_Pl³ vs M_Pl⁵ ambiguity should produce. Either the author has implicitly fixed the choice (and the "structural-tension" argument is therefore mechanism-independent only modulo that fixing), or the 2-e-fold offset claim is wrong by an order of magnitude.

**Required fix:** Either rigorously fix the dimensional choice with explicit argument, or carry the ∼29-e-fold uncertainty through to the structural-tension conclusion, which would obliterate the N_tot ≈ 92 numerical claim entirely.

### P1A-M12 — Barrier 6 ("Attractor-Sensitivity Dilemma") is a false dichotomy (page 12)

*"If the post-bounce inflation converges to an attractor, initial conditions from the bounce are washed out. If it is sensitive to initial conditions, inflation itself is destabilized."*

This is not exhaustive. Inflationary models routinely exhibit *partial* attractor behavior: certain modes are washed out while others (e.g., the inflaton field value at horizon exit, the duration of inflation) carry imprint of initial conditions. Examples: Starobinsky inflation has attractor behavior in φ̇ but not in N_e; chaotic inflation has attractor in slow-roll trajectory but allows different N_e depending on initial φ. The dichotomy "attractor OR unstable" excludes the standard intermediate case.

The barrier as stated does not actually close any well-defined mechanism class.

**Required fix:** Either rigorously demonstrate that no intermediate-sensitivity inflationary model can transmit ECH-bounce information to dark energy (this would be a major undertaking), or remove Barrier 6.

### P1A-M13 — Barrier 9 ("Liouville Conservation") misapplies Liouville's theorem (page 13)

*"Phase-space volume conservation prevents irreversible selection among post-bounce states from pre-bounce dynamics."*

Liouville's theorem states that phase-space volume is preserved under Hamiltonian evolution. It does *not* state that the *distribution* in phase space cannot be reshaped: a sharply peaked initial distribution can evolve into a sharply peaked final distribution at a different location, and the "selection" between distinct post-bounce branches is determined by the specific Hamiltonian dynamics, not by volume considerations. Moreover, the LQC bounce is *not* generated by canonical Hamiltonian evolution at the bounce point (it involves holonomy corrections that modify the symplectic structure), so Liouville's theorem strictly speaking does not apply at the bounce in the form invoked.

This barrier is invalid as stated.

**Required fix:** Either provide a rigorous argument (perhaps based on time-reversal symmetry of the LQC dynamics specifically) or remove Barrier 9.

### P1A-M14 — Eq. (7) introduces δ_NY without defining it (page 6)

Eq. (7): α/M ∼ (g²/32π²)(γ/M) ln(Λ²_UV/μ²) + δ_NY

δ_NY ("Nieh-Yan correction"?) is never defined or quantified. Yet this is the operator coefficient that drives the entire dark-energy mapping. The reader cannot evaluate whether the "motivating order of magnitude [(α/M) M_Pl] ∼ 10⁻²" survives inclusion of δ_NY.

**Required fix:** Define δ_NY, give its order of magnitude, and demonstrate that the 10⁻² conclusion is robust.

---

## MINOR — Additional

### P1A-m1 — "Scheme range ∼0.020" does not match the actual scheme spread (page 5)

Page 5: γ_SU(2) ≈ 0.274 quoted with "scheme range ∼0.020" (also in Table IV). But the page-5 text enumerates three schemes: γ_U(1) ≈ 0.127, γ_SU(2) ≈ 0.274, γ_DLM ≈ 0.2375. The full scheme spread is 0.274 − 0.127 = 0.147, or even restricting to SU(2)-class schemes 0.274 − 0.2375 = 0.037 (still not 0.020). The "∼0.020" figure has no clear referent and is misleading; it understates the actual scheme dependence by an order of magnitude.

**Required fix:** State the range explicitly, e.g., 0.127–0.274, or use 0.037 if restricting to SU(2)-class schemes.

### P1A-m2 — γ²/(γ²+1) suppression factor at γ=0.274 is 0.07, not propagated in amplitude estimates

Eq. (4): coefficient γ²/(γ²+1) appears in the Holst-extended NJL operator. At γ = 0.274:
γ²/(γ²+1) = 0.0750/1.0750 = 0.0698 ≈ 0.07

So the Holst-correction to the standard Hehl-Datta NJL operator is a *suppression* by factor ∼14 at the LQG-preferred γ value. This factor is nowhere propagated into the Route 1 amplitude estimate in Sec. IV A — the calculation uses the bare Hehl-Datta coefficient. The Route 1 amplitude is therefore overstated by ∼14× compared to what the paper's own action structure prescribes. This does not change the qualitative no-go (Route 1 is overwhelmingly suppressed anyway), but the inconsistency should be fixed.

**Required fix:** Either include γ²/(γ²+1) in Route 1 amplitude estimate, or explain why Eq. (4) and Sec. IV A use different coefficient structures.

### P1A-m3 — Eq. (15) input ratios do not yield the stated output range

Recomputing Eq. (15) with the explicit inputs the paper provides (α_em/(4π) ≈ 5×10⁻⁴, H_0/M_Pl ~ 10⁻⁶¹, M_Pl·(α/M) ~ 10⁻², β_obs ~ 6×10⁻³):

Numerator: 5×10⁻⁴ × 10⁻⁶¹ = 5×10⁻⁶⁵
Denominator: 10⁻² × 6×10⁻³ = 6×10⁻⁵
Ratio: 8×10⁻⁶¹ ≈ 10⁻⁶⁰

The stated output "10⁻⁵⁸ to 10⁻⁶⁰" upper end has no derivation; only the lower end matches the inputs. The "factor-of-100 ambiguity" claimed to be "ε-correction perturbative-order scaling alone" is not visible in the displayed inputs.

**Required fix:** Either provide the calculation that yields 10⁻⁵⁸, or correct the stated range to ~10⁻⁶⁰ with appropriate single-digit precision.

### P1A-m4 — Table IV "Verified Value" column conflates fitted, derived, and assumed parameters

Table IV (page 20) lists in the "Verified Value" column:
- γ = 0.274 (fundamental, fixed by area spectrum)
- N_tot ≈ 92 (fitted)
- H_0 = 67.68 ± 1.06 km/s/Mpc (from companion MCMC, not verified in this paper)
- σ_8, Ω_m (derived from MCMC priors, not from ECH physics)

Calling all of these "verified" obscures the distinction between fundamental, fitted, MCMC-derived, and assumed values. A reader cannot tell which numbers carry empirical weight.

**Required fix:** Rename column to "Value" and add explicit provenance flags (e.g., "fixed," "fitted," "MCMC-derived," "ansatz").

---

## NEUTRAL Observations

### P1A-N1 — Tone of self-criticism is unusually heavy for a research paper

The abstract alone contains: "channel-level assessment, *not* an operator-level theorem," "not proven to be a complete diffeomorphism-invariant operator basis," "rests on a phenomenological on-shell scaling ansatz," "we treat this scaling explicitly as an ansatz, not a derivation," "the two predictions discussed below as 'surviving' are accordingly *not* predictions of ECH itself," "is *not* derived from the ECH action," "we do not claim a full operator-basis closure."

This level of self-correction in an abstract is exceptional and suggests either (a) the paper has been heavily revised in response to prior criticism and is now in a state of partial retraction, or (b) the author is preemptively responding to anticipated criticism. Either way, the disclaimers are so thorough that they undermine the value proposition of submission: a paper that explicitly disclaims its title's main claim, its central result's status as a theorem, its phenomenological mapping's derivability, and its surviving tests' relevance to the framework is operating outside the standard scope of a primary PRD research article. The work might be more naturally a review or "Comments" piece.

This is offered as a meta-observation, not a recommendation for action; the editor may want to consider the genre fit.