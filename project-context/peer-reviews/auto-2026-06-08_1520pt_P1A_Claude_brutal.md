# P1A auto-2026-06-08_1520pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (12016 chars)
**Wall time**: 504.9s

---

# Referee Report — Physical Review D Submission

**Manuscript**: "Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"
**Author**: H. Golden (Independent Researcher)
**Length**: 21 pages

---

## Overall assessment

This is not a publishable PRD submission. The paper is a long, self-referential negative-result essay that (i) openly retracts its own central claim within the abstract ("This is a channel-level assessment, *not* an operator-level theorem"), (ii) admits its load-bearing equation has the wrong mass dimension and survives only by phenomenological insertion of factors by hand, (iii) cites four "companion papers in preparation" by the same author as the source of nearly every numerical claim (H₀, ∆N_eff, σ(f_NL), galaxy-chirality null, NANOGrav γ posterior, ALP MCMC, NaMaster validation), and (iv) elevates a textbook two-line observation (scalar matter → zero spin density → zero torsion → Holst → Pontryagin total derivative) into a "central result." The structural narrative is internally contradictory: routes are declared "closed" and then re-described as merely "naturalness objections" or "explanatory deficits." Most of the paper's apparatus (the "14-barrier catalog," the inflation-suppression bookkeeping, the structural-tension paragraph) is post-hoc taxonomy of negative results rather than science.

I summarize specific findings below.

---

## ESSENTIAL findings (must fix before any consideration)

**P1A-E1 (Abstract, p. 1): Central claim retracted within its own abstract.**
The abstract states "We assess four enumerated minimal-Einstein-Cartan-Holst (ECH) spin-torsion channels … and find that each fails at the amplitude level," then immediately concedes "the four enumerated routes … are not proven to be a complete diffeomorphism-invariant operator basis," and acknowledges missing operators (Jackiw–Pi gravitational Chern–Simons, parity-odd four-fermion partner). A paper whose abstract retracts its own headline claim by sentence three is not a PRD result. The author must either (a) provide the operator-basis closure or (b) reframe and retitle the paper as "Partial channel-level assessment of four candidate ECH routes," not "Closure of … routes."

**P1A-E2 (Sec. II A 2, Eq. 6; Appendix B): Dark-energy operator is dimensionally inconsistent.**
The author admits openly in Appendix B that the parity-odd operator has off-shell mass dimension +1 rather than the +4 required for a Lagrangian density, then patches this by promoting α/M → αM³_Pl/M, calling it "either reading is a phenomenological dimensional assignment, not a derivation." The entire dark-energy mapping (Eqs. 10, B2) — and therefore the entire 14-barrier closure of the dark-energy route — rests on inserting three powers of M_Pl by hand. This is not a controlled EFT calculation. Either close the operator basis properly or remove all dark-energy mapping claims from the paper.

**P1A-E3 (Throughout; Sec. III B, Sec. V, Sec. VIII, Sec. XIII, Refs. [2,6,23,46]): Critical results deferred to four self-citations "in preparation."**
The galaxy-spin null (Sec. III B, V), MCMC posteriors (H₀=67.68±1.06, ∆N_eff=−0.020±0.169), NaMaster pipeline validation, ALP MCMC (9,720 samples, R̂−1<0.01), SPHEREx σ(f_NL) Fisher forecast, NANOGrav γ=2.567±0.382 real-KDE reanalysis, and the multi-survey anomaly catalog are all sourced to Papers I(b), II, III, IV "in preparation." The author even notes in Sec. I B that the cosmological parameter values "should be read as internal-analysis inputs … rather than as independently peer-reviewable values until Paper I(b) is publicly posted." PRD does not accept manuscripts whose load-bearing numbers are not independently verifiable. Either post the companion papers first, fold the necessary content into the present paper, or remove dependent claims.

**P1A-E4 (Refs. [23,46,47]): Uncitable references.**
Ref. [47] is described as a "companion technical note, available upon request from the author" — this is not acceptable in PRD. Refs. [2], [6], [23], [46] are all "(in preparation)" self-citations. PRD requires that cited material be available at the time of submission.

**P1A-E5 (Ref. [44]): Likely fabricated/invalid arXiv ID.**
"Y.-F. Cai and J.-H. Zhu, … (2026), arXiv:2603.13924 [astro-ph.CO]." The arXiv ID 2603.13924 would correspond to March 2026 in the YYMM.NNNNN scheme; the suffix .13924 is unusually high for a March 2026 monthly count and the paper title pattern reads as plausibly generated. Author must verify the arXiv ID exists and matches the cited title; PRD does not accept invented references.

**P1A-E6 (Sec. IV D, p. 10): "Route 4 closure" silently downgraded to non-closure.**
The abstract and Sec. IV E claim all four routes are "closed at the amplitude level." Sec. IV D then states: "R4 is therefore *not* closed by amplitude mismatch (as prior analyses claimed); it is closed by the observation that the same coupling that produces β_obs requires an ultralight-mass tuning m_θ ∼ H₀." A naturalness objection is not an amplitude closure. The author further admits: "the channel is closed at the level of an explanatory deficit, not an amplitude no-go at the operator level." This contradicts the abstract. Either four routes are closed at amplitude level or three are; the abstract must reflect what Sec. IV proves.

**P1A-E7 (Sec. X "Perturbation-Transparency Result," pp. 14–15): Trivial result inflated to a "theorem."**
The five-step "proof" is: (1) scalar field has zero spin density; (2) torsion vanishes (algebraic Cartan equation); (3) connection becomes Levi-Civita; (4) Holst term becomes Pontryagin density, which is a total derivative; (5) total derivatives don't contribute to EOM. This is standard textbook material (Hehl et al. 1976), not a new theorem. Calling it a "central result" and "generalizes Hehl et al. (1976) to the Holst sector and to all perturbation orders" is overclaim — the generalization is automatic once one writes down the assumptions. Either provide a non-trivial extension (e.g., to non-minimally coupled scalars, propagating torsion, or fermion-loop-induced effective spin density) or downgrade the language from "theorem" / "central result" to "observation."

**P1A-E8 (Sec. IX, Table II, pp. 12–13): "13 vs 14 barriers" inconsistency repeated ad nauseam.**
The phrase "13 logically-independent constraints (14 historical catalog entries, of which B8 is subsumed by B14)" or its variants appears at least 9 times across the paper (abstract twice, Sec. I, Sec. I B, Sec. IX header, Table II caption, Sec. XIV E, Sec. XV twice). If B8 is subsumed by B14, remove B8 from the catalog and quote 13 throughout. The repeated meta-clarification is symptomatic of internal-bookkeeping prose that should not appear in a published manuscript.

**P1A-E9 (Sec. II C 1, pp. 6–7): "Order-of-magnitude matching" for Eq. (11) is not a derivation.**
The (T_reh/M_GUT)^{3/2} prefactor is described as "dimensional-analysis aesthetic," "matched to first-principles arguments at the order-of-magnitude level," and the author explicitly acknowledges "a fully rigorous first-principles derivation … is dimensional-analysis aesthetic at this level rather than calculated from a thermal partition function." The 92-e-fold "reparameterization" of the cosmological-constant fine-tuning is sourced to this aesthetic estimate. Either derive the exponent or remove the quantitative N_tot ≈ 92 claim and the entire "fine-tuning reduction from 10¹²² to 10⁵" narrative.

**P1A-E10 (Sec. III A, Eq. 12; Sec. II C; Sec. XII): No derived photon–torsion coupling, yet birefringence is claimed as a consistency check.**
Sec. III A admits: "Connecting to a quantitative rotation angle β from the gravitational/torsion operator requires an explicit photon-torsion coupling that has not been derived here." Sec. XII then quotes "spectator ALP with f_a ∼ M_Pl, m ∼ H₀ is consistent with … β = 0.342° ± 0.094°." The author concedes in Sec. XIII this "is not a distinctive ECH prediction" and arises identically in standard GR with the same ALP. So the birefringence section in this paper supplies no original content and should be cut.

**P1A-E11 (Table III, p. 16, footnote ‡): Internal MCMC status report embedded in a published table.**
Footnote ‡ contains: "At the time of this writing the chain has accumulated ~3.8×10⁴ accepted samples across the 16 chains and reports R̂ − 1 ≈ 3×10⁻², descending monotonically toward the standard publication-quality convergence target R̂ − 1 < 10⁻²at a slow-mode-dominated convergence rate; we deliberately do not commit to a specific calendar date for convergence in this footnote." This is internal bookkeeping prose ("we deliberately do not commit to a specific calendar date") and has no place in a PRD manuscript. Either complete the chain and report posteriors, or remove the entire w_0w_a column from Table III.

**P1A-E12 (Acknowledgments, p. 18): Substantial undisclosed AI involvement in core scientific tasks.**
"The author acknowledges the use of Claude (Anthropic) as an AI research assistant during systematic barrier-cataloging, perturbation-gate verification, and manuscript preparation." Barrier-cataloging and "perturbation-gate verification" are core scientific work, not editing. Given the paper's recurring patterns (long parenthetical hedges, repeated meta-clarifications, "we emphasize / we acknowledge" hedges, the 13-vs-14 redundancy, the contradictory closure/non-closure prose), the AI contribution appears to extend well beyond manuscript preparation. PRD requires that the author take full responsibility for all derivations; if the AI assisted with the actual "perturbation-gate verification," the author must independently re-derive and publish those derivations in human-checkable form.

---

## MAJOR findings

**P1A-M1 (Abstract, p. 1): Abstract is one giant run-on paragraph with nested parentheticals.**
The abstract is a single ~70-line block with at least eight parenthetical asides (some nested two deep), e-fold arithmetic embedded in mid-sentence, four references stuffed into qualifiers, and the structural-tension argument compressed into one parenthetical. Rewrite as a short, declarative abstract following standard PRD style.

**P1A-M2 (Sec. I, p. 3): "Three theoretical pillars … standard well-established components" is followed by claims of "novel synthesis" — but the synthesis is mostly a negative-result taxonomy.**
The "original contributions" listed (14-constraint catalog, structural tension, surviving tests) are bookkeeping observations about a model the author concludes does not work. State plainly that the paper is a negative-result analysis.

**P1A-M3 (Eq. 4, Eq. 13; Sec. II C 1): Internal inconsistency about parity character and operator order.**
Eq. (4): L_int = −(3πG/2)(γ²/(γ²+1)) J^5_μ J^{5μ} — quadratic in axial current. Eq. (13): L^NJL_tor = −(3κ/16)(ψ̄γᵃγ⁵ψ)² — quadratic. But Sec. II C 1 states "the cube of the fermion bilinear scales as the cube of the fermion number density." The interaction is quadratic in axial currents (J⁵J⁵), not cubic. Either the scaling argument is wrong or it refers to something else; clarify.

**P1A-M4 (Sec. IV B, Eq. 15; p. 9): Numerical reduction has factor-of-100 quoted ambiguity that is not honestly characterized.**
The author writes "∼ 10⁻⁵⁸ to 10⁻⁶⁰ (the factor-of-∼100 ambiguity reflects ε-correction perturbative-order scaling alone …)" and then states "an alternative ordering that contracts the H₀ factor with the dimensionful coupling differently yields a numerically distinct ∼ 10⁻³³ ratio." A 25-order-of-magnitude difference between "valid contractions" is not a perturbative-ordering ambiguity — it indicates the dimensional bookkeeping is wrong. Reconcile or admit Route 2 closure depends on the chosen contraction.

**P1A-M5 (Sec. IV D, p. 10): Route 4 closure circularly assumes the bound it derives.**
The argument: matching β_obs at the one-loop estimate α/M ∼ 10⁻²¹ GeV⁻¹ implies m_θ ∼ H₀ to also produce ρ_Λ. But the author admits: "the rigidity of the no-go is tied to the one-loop matching assumption rather than to ALP-mass kinematics alone." The "one-loop estimate" itself (Eq. 7) is acknowledged to be a phenomenological ansatz, not a derivation. The closure is circular.

**P1A-M6 (Sec. IX, Barrier 12, Eq. 20): NANOGrav comparison admitted to be deferred.**
"A quantitative comparison to NANOGrav requires propagating the bounce GW spectrum through the transfer function to the nHz band, which is deferred to a forthcoming bounce-GW dedicated paper (deferred)." If the comparison is deferred, do not list Barrier 12 as a "vacuum amplification ceiling" closure — it is an open question.

**P1A-M7 (Sec. II A 1, Eq. 2; Sec. II B, Eq. 9): Barbero–Immirzi value contradicts ρ_crit window.**
γ_SU(2) ≈ 0.274 plugged into Eq. (9) gives ρ_crit ≃ 0.27 ρ_Pl, but Ashtekar & Singh use γ = 0.2375 and quote 0.41 ρ_Pl. The author silently uses the range 0.27–0.41 ρ_Pl as if it were a published LQC range, then admits in p. 6: "this lower value is an internal extrapolation across counting schemes (not a value quoted in Ref. [11])." Then Eq. (20) in Barrier 12 uses this fabricated range. Either pick a single scheme self-consistently or carry the scheme uncertainty through the paper.

**P1A-M8 (Sec. V, p. 11): Entire "data methods" section defers to companion Paper IV.**
"The catalog construction, sample size, validation accuracy, bias-audit suite, equivariant CW-fraction monopole, and dipole significance are reported in Paper IV [23] and are not duplicated here." A "Data Methods" section that contains no methods is not a section.

**P1A-M9 (Sec. XI, p. 15): "Hybrid loophole" closure is claimed but never computed.**
"The loophole was explored theoretically but the w₀wₐ extension was never implemented computationally in this program." Then the conclusion "All 7 forms were rejected" has no computational basis. Either implement the extension or remove the rejection claim.

**P1A-M10 (Sec. XV, p. 18): LiteBIRD "9σ" claim is misleading.**
"LiteBIRD (σ(β) ≈ 0.03°, early 2030s) detects non-zero β at ∼ 9σ (a 0.27°/0.03° overall sensitivity number)." This is a detection-against-zero number, not a discrimination of the prediction. The author then immediately admits "the ∼ 9σ test will not by itself separate the spectator-ALP class from generic-ALP fits to the observed signal." Move the "9σ" out of conclusions entirely — it tests the wrong null.

**P1A-M11 (Sec. II C 1 "Reheating thermal-reset barrier" paragraph, p. 7): New ad-hoc "barrier" introduced inside a derivation.**
A multi-paragraph "supporting B14" thermodynamic argument is inserted mid-derivation, then qualified as "bookkeeping, not progress." If it's bookkeeping, remove it. If it's a 15th barrier, catalog it formally. Either way, embedding new structural arguments inside Sec. II is poor organization.

**P1A-M12 (Eq. 16, p. 9): RG ansatz attributed to Date–Kaul–Sengupta but admitted not to be derived there.**
"Schematically motivated by their construction, we adopt the one-loop running ansatz dγ/d ln μ = (1/12π²)(N^L_F − N^R_F)γ … we use Eq. (16) only as an upper-bound EFT ansatz … and do not claim it is taken verbatim from [26]." The actual perturbative Immirzi β-function is computed by Benedetti & Speziale [27] with different sign/structure. Use the correct β-function or remove the Route-3 quantitative claim.

**P1A-M13 (Figure 1, p. 4): Figure is decorative, not informative.**
The flowchart shows arrows from bounce mechanisms to observables with no quantitative content. Caption claims "narrows the four enumerated minimal-ECH dark-energy channels to zero" — but this is the paper's negative-result thesis, not something the figure proves. Remove or replace with a quantitative figure.

**P1A-M14 (Figure 2, p. 5): Figure 2 illustrates the ansatz it is supposed to demonstrate.**
Caption: "illustrating the phenomenological scaling ansatz ρ_vac ∼ [(α/M)M_Pl]M_Pl⁴ … This ansatz is dimensionally correct on-shell at the bounce but is not derived from the ECH action." A figure that admits in its own caption that it illustrates an undefined ansatz is not a result.

---

## MINOR findings

**P1A-m1 (Sec. I, p. 3):** "DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ (dataset-dependent)" — quote the actual dataset combinations rather than the range.

**P1A-m2 (Sec. II A 2, last paragraph p. 5):** Domagała–Lewandowski–Meissner γ value is correctly cited but the parenthetical "the ∼0.020 figure that appears in the parameter-budget table … is *not* propagated as a statistical error in any quantitative claim" is unnecessarily defensive.

**P1A-m3 (Sec. II A 2, Eq. 7):** δ_NY is undefined.

**P1A-m4 (Sec. IV A, Eq. 13):** Parity character clarification ("parity-even because pseudovector-squared is +1") belongs in a footnote, not the technical-aspect parenthetical at the start of Sec. IV.

**P1A-m5 (Sec. IV B, p. 9):** "A naive comparison of a rotation rate β̇ in eV against an angle uncertainty in eV would silently treat eV·s as dimensionless" — this defensive aside acknowledges a prior dimensional error. Either fix silently or expand into a proper appendix; do not leave the historical artifact in the body.

**P1A-m6 (Sec. VII, footnote 1):** "3–5σ realistic" range is computed from two different σ(f_NL) values without clarification. Inline arithmetic in a footnote is hard to follow.

**P1A-m7 (Sec. IX, Barrier 7, p. 13):** "γ is fixed by the LQG area spectrum at a universal value" — but the paper's own scheme dependence (Sec. II A) contradicts this universality.

**P1A-m8 (Sec. XII A, p. 15):** "fine-tuning reduction from 10¹²⁰ to 10⁵" is the headline of the section but the section concedes it "should be read as a qualitative dimensional rearrangement rather than a quantitative bookkeeping result." Remove from headline.

**P1A-m9 (Sec. XIV A, p. 17):** "Stock CAMB with ∆N_eff is a phenomenological proxy, not a bespoke spin-torsion Boltzmann module." Then the MCMC results in Table I and elsewhere quoted as "consistent with ΛCDM" do not test ECH.

**P1A-m10 (Sec. XV, p. 18):** Conclusions repeat the abstract verbatim in several places (e.g. the 13-vs-14 clarification).

**P1A-m11 (Refs. [3,4,5]):** Birefringence is cited as 3.6σ from Eskilt & Komatsu and 2.9σ from ACT DR6 Diego-Palazuelos. Verify these σ values against the published papers' abstracts (Eskilt & Komatsu 2022 quote 3.6σ; ACT DR6 publication should be checked).

**P1A-m12 (Ref. [29]):** LiteBIRD σ(β) ≈ 0.03° — cite the specific section/table of the LiteBIRD PTEP paper.

**P1A-m13 (Table IV, p. 20):** "Verified Value" column for parameters not yet posted in Paper I(b) is misleading — these are not verified values, they are internal posteriors.

---

## NITs

**P1A-n1 (Throughout):** "We acknowledge … We emphasize … We treat this explicitly as an ansatz, not a derivation" is used so frequently it loses force. Tighten.

**P1A-n2 (Fig. 1 caption):** Dashed-box convention is described but not visually distinct in the figure.

**P1A-n3 (Sec. II A 2, Step 3):** "Motivated by (but not literally derived in)" is awkward phrasing — rewrite.

**P1A-n4 (Table I footnote a):** "Reparameterized as sensitivity to N_tot; not solved" is a confession, not a footnote.

**P1A-n5 (Sec. III B):** "MCMC verification and cosmological fits" subsection title with no MCMC results in this paper.

**P1A-n6 (Sec. X.D, Eq. 23):** R̃(Γ̊) introduced without prior definition of R̃ vs the R̃ used elsewhere.

**P1A-n7 (Sec. XIV D):** Run-on sentence with three nested parentheticals on "structural tension."

---

## Page-count assessment

The substantive content (one trivial transparency observation + a taxonomy of 13 reasons a model does not work, all qualified by an admitted dimensional inconsistency and an incomplete operator basis) would fit in 4–6 pages as a Comment or Brief Report. **Recommended maximum length: 6 pages** if recast as a Brief Report; otherwise the operator-level closure and the actual MCMC/Fisher/galaxy-spin computations must be folded into the present paper (raising it to a coherent ∼15-page Article).

---

## Summary recommendation

**REJECT**

The manuscript fails the PRD threshold on multiple independent grounds: the central claim is retracted within the abstract; the dark-energy mapping rests on an operator the author admits is dimensionally inconsistent; the "perturbation-transparency theorem" is a textbook two-line observation inflated into a central result; every load-bearing numerical claim (MCMC posteriors, galaxy-spin null, σ(f_NL) forecast, NANOGrav posterior, ALP MCMC) is deferred to four self-cited "in preparation" companion papers that are not independently verifiable; Route 4 is silently downgraded from "amplitude closure" to "explanatory deficit" mid-paper; one reference (arXiv:2603.13924) appears likely fabricated; one is "available upon request"; and internal MCMC status reports ("we deliberately do not commit to a specific calendar date for convergence in this footnote") appear in published tables. The acknowledged AI involvement in "perturbation-gate verification" and "barrier cataloging" — coupled with the paper's pervasive run-on hedging, redundant meta-clarifications, and contradictory closure prose — raises further concerns about the human verification of the derivations. The paper is not salvageable by revision in its current scope; the author would need to (a) publish the companion papers first, (b) provide a genuine operator-basis closure rather than a four-channel enumeration, (c) resolve the dimensional inconsistency, and (d) reduce the manuscript to ≤6 pages as a Brief Report, before resubmission could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional Findings on Second Pass

After re-examining the manuscript with focus on arithmetic, dimensional consistency, citation accuracy, and figure-body alignment, I identify the following new issues not flagged in the initial review.

---

## ESSENTIAL (new)

**P1A-E13 (Sec. IV D, p. 10; Sec. XII B, p. 16): Arithmetic error in inter-experiment σ-discrepancy.**
The paper states the Eskilt & Komatsu and ACT DR6 birefringence values are "consistent within ∼ 1.4σ":

- β₁ = 0.342° ± 0.094° (Eskilt & Komatsu)
- β₂ = 0.215° ± 0.074° (ACT DR6)

The proper σ-discrepancy for two independent measurements is:

|0.342 − 0.215| / √(0.094² + 0.074²) = 0.127 / 0.1196 = **1.06σ**, NOT 1.4σ.

The paper's "1.4σ" appears to come from dividing 0.127/0.094 = 1.35 ≈ 1.4, which would treat only one experiment's uncertainty rather than the combined uncertainty. This is the wrong null procedure. The actual tension is ~1σ. This should be corrected; it is the kind of basic error that referees will catch and that undermines reader confidence in the rest of the paper's numerical claims.

**P1A-E14 (Sec. II A 2, p. 5; Refs. [17,18]): Citation error — wrong γ value attributed to Domagała-Lewandowski / Meissner.**
The footnote states:

> "the refined SU(2) full counting [17, 18] gives γ_SU(2) ≈ 0.274 (adopted in this paper), and the further Domagała–Lewandowski–Meissner refinement gives γ_DLM ≈ 0.2375."

Refs [17] and [18] *are* Domagała–Lewandowski (gr-qc/0407051) and Meissner (gr-qc/0407052). Meissner's classic result is γ ≈ 0.2375 — i.e., the "DLM refinement" value the author quotes second. The 0.274 value (sometimes 0.2740) attributed to refs [17,18] is *not* what those references give. The "0.274 vs 0.2375" distinction in the LQG-BHE literature usually traces to different counting prescriptions in Agullo–Barbero–Borja–Diaz-Polo or related work, not to DLM/Meissner. The adopted γ value drives the ρ_crit window in Sec. II B (0.27 ρ_Pl) and propagates through Barrier 12 (Eq. 20). Either fix the attribution or replace γ = 0.274 with the actually-cited γ = 0.2375 (which would shift ρ_crit to 0.41 ρ_Pl and collapse the spurious "0.27–0.41 ρ_Pl scheme-dependent window").

---

## MAJOR (new)

**P1A-M15 (Sec. III A, p. 7; Table IV "Observational channel parameters", p. 20): "β ≈ 0.27°–0.30°" range is not derived and does not match observed values.**
Sec. III A states: "The parity-odd structure is qualitatively consistent with the observed isotropic birefringence at β ≈ 0.27°–0.30°." Table IV lists "β: 0.27° (midpoint)" with no derivation.

The actual observed values are 0.342° ± 0.094° (WMAP+Planck) and 0.215° ± 0.074° (ACT DR6). The mid-range 0.27°–0.30° corresponds to neither central value. My independent calculation via Eq. (17) with m_θ ≈ H₀ = 1.4 × 10⁻³³ eV, ρ_θ = ρ_Λ, α/M = 10⁻²¹ GeV⁻¹ yields β ≈ 0.278° — matching only the lower endpoint of the quoted range. The upper bound of 0.30° has no shown derivation. This appears to be a stale post-hoc fit value carried over from an earlier draft; the same number reappears across Sec. XII B and Sec. XV. Either derive the range or replace with the actually-computed central value.

**P1A-M16 (Sec. IV B, Eq. 15, p. 9): "10⁻⁵⁸ to 10⁻⁶⁰" range has wrong upper bound.**
Re-computing with the paper's own inputs:
- α_em/(4π) ≈ 5.8 × 10⁻⁴ (or 10⁻³ at OOM)
- H₀/M_Pl ≈ 10⁻⁶¹
- M_Pl × (α/M) ≈ 10⁻²
- β_obs ≈ 6 × 10⁻³

Ratio = (5.8 × 10⁻⁴ × 10⁻⁶¹) / (10⁻² × 6 × 10⁻³) ≈ **10⁻⁶⁰** (not 10⁻⁵⁸).

The paper's quoted "10⁻⁵⁸ to 10⁻⁶⁰" upper bound is not reproducible from the values given. The author cryptically attributes the "factor-of-∼100 ambiguity" to "ε-correction perturbative-order scaling alone" — but no ε-correction is defined anywhere in the text, and a 2-OOM ambiguity is not an ε-correction. Either derive the upper bound or replace with the order-of-magnitude estimate ~10⁻⁶⁰. The Route-2 closure does not depend on this detail, but the inconsistency undermines confidence.

**P1A-M17 (Sec. II C, Eq. 10 vs Sec. XII A vs Appendix B): Ξ dimensional convention is internally inconsistent.**
Eq. (10) defines Λ_eff = Ξ M_Pl² + c_ω ω². If Λ_eff is the cosmological-constant-convention dim-2 quantity (consistent with Eq. (10)'s c_ω ω² term), then Ξ ~ (H₀/M_Pl)² ~ **10⁻¹²²** (dimensionless).

But Sec. XII A states "Ξ ≈ 10⁻¹²³, decomposed as 10⁻² × D_inf with D_inf ~ 10⁻¹²¹," and Appendix B uses ρ_Λ = Ξ M_Pl⁴ with Ξ ≈ 10⁻¹²³ in the dim-4 convention.

These are *different* definitions of Ξ, differing by an extra factor of M_Pl² ≡ M_Pl⁴ /M_Pl². The paper uses both interchangeably without flagging the convention switch. This is consequential because the "fine-tuning reduction" narrative in Sec. XII A inherits this confusion. Either pick one convention (the dim-4 ρ_Λ = Ξ M_Pl⁴ convention is the standard one for vacuum energy) and fix Eq. (10) to read Λ_eff = Ξ M_Pl² with Ξ ≈ 10⁻¹²², or rewrite Eq. (10) entirely.

**P1A-M18 (Sec. IX, Table II caption and Sec. XV): "B8 subsumed by B14" claim does not survive inspection.**
The author repeatedly states B8 (Parity-Even Interaction, Branch H) is "the observational consequence of the perturbation-transparency theorem B14." Examining the actual contents:

- B8 (Sec. IX H): The fermion-axial-current bilinear (J⁵)² is a Lorentz scalar, parity-even, and therefore cannot generate primordial GW tensor chirality.
- B14 (Sec. IX N → Sec. X): For canonical *scalar* matter (no fermions), torsion vanishes algebraically and Holst reduces to a Pontryagin total derivative.

These are about different matter sectors (fermions for B8, canonical scalars for B14) and different observable channels (the parity quantum number of an interaction term vs the on-shell value of a connection field). B14 does not imply B8 — fermion-loop-induced effective vertices can still be parity-non-trivial at higher orders. The "13 logically-independent / 14 historical catalog entries / B8 subsumed by B14" mantra (repeated ≥9 times across the paper) does not survive the textual definitions of B8 and B14 themselves. Either provide a derivation that B14 ⇒ B8, or count 14 throughout.

**P1A-M19 (Sec. II C 1, p. 6): "a⁻³ dilution of operator value" confuses source and operator.**
The author argues exp(-3 N_tot) torsion dilution because "fermion number density dilutes as a⁻³." But in minimal ECH, the source for the algebraic Cartan equation is the *axial current density* J^5_μ, not the fermion number density n_ψ. The "reheating thermal-reset barrier" paragraph on the next page (added as a defensive aside) acknowledges precisely this — that the thermal axial current vanishes in mean. So the a⁻³ dilution argument is self-contradicted within two pages: the operator value at late times is set not by adiabatic dilution of an initial bounce-era value but by the instantaneous thermal axial expectation (which is ~zero). The exp(-3 N_tot) exponential structure on which the "92 e-fold" reparameterization rests is therefore physically inoperative, by the author's own subsequent argument. This goes beyond a bookkeeping issue: it eliminates the entire suppression-mechanism narrative. Reframe.

---

## MINOR (new)

**P1A-m14 (Sec. IV B, Eq. 15):** α_em/(4π) is written as "10⁻³" but the actual value is 5.8 × 10⁻⁴ — a 2× rounding error that propagates into the OOM estimate. Use 10⁻⁴ (closer) or carry the precise value.

**P1A-m15 (Sec. II A 2 footnote):** "U(1) horizon-state counting [16] gives γ_U(1) ≈ 0.127 (using γ = ln 2/(π√3))." Actually ABCK [16] proposed both U(1) and SU(2) counting schemes; the 0.127 value is the lowest-spin-only U(1) result, not "the" U(1) result. The full U(1) counting gives γ ≈ 0.2375 (matching Meissner). The footnote conflates two distinct counting schemes.

**P1A-m16 (Sec. Eq. 18):** "g_eff ~ 1/(M_Pl√|t_3|) ~ H_0/M_Pl ~ 10⁻⁶¹." For the chain of approximate equalities to hold, t_3 must have implicit mass dimension -2 (i.e., t_3 ~ 1/H_0²). The dimensional structure of the PGT parameter t_3 is left implicit; readers unfamiliar with PGT conventions will not be able to verify the equality. Add a footnote stating the convention for t_3.

**P1A-m17 (Sec. III A, p. 8):** "Spectator-ALP parameter fitting and the NaMaster pipeline validation are in companion Paper I(b) [6]." This is the same sentence pattern as ≥7 other deferral statements in the paper. The cumulative effect is that this paper is essentially a long abstract of work hosted elsewhere.

**P1A-m18 (Table III, Quintom-B row, p. 16):** The column "w₀wₐ DESI" shows "consistent†" with footnote text "Quintom-B can in principle accommodate the DESI w₀wₐ evidence; the MCMC analysis hosted in companion Paper I(b) was not extended to the w₀wₐ parameter space." A "consistent" verdict not backed by an MCMC chain is not a fit result. Either remove the column or mark all rows as "not tested."

**P1A-m19 (Sec. II C 1, p. 7):** "comoving wavenumbers k are constant by definition and only physical scales scale with a⁻¹ ∝ e⁻ᴺ." This is restated four times in the paper (abstract, Sec. I A, Sec. II C 1, Sec. XIV D) — once would suffice, and stating a textbook fact "by definition" reads as defensive against a perceived prior reviewer.

**P1A-m20 (Sec. VII footnote 1):** "σ(f_NL) ≈ 0.7 Fisher-ideal (raw ratio |f_NL|/σ = 4.375/0.7 ≈ 6.25σ, degraded to ~5–5.5σ optimistic after template-overlap correction r ≈ 0.84." With σ(f_NL) ≈ 1.0 (post-systematic), the raw ratio is 4.375, × 0.84 ≈ 3.7σ. The footnote claims the realistic range is "3–5σ" — but 3.7σ does not match the 3σ lower bound either. Either provide the additional systematic factor that brings 3.7 → 3, or revise the lower bound to ~3.7σ.

**P1A-m21 (Refs. [16] vs [17] vs [18]):** All three references are cited for γ-counting schemes but the attribution of specific numerical values to specific references is muddled (P1A-E14, P1A-m15). Provide a clean table mapping each scheme to its source.

---

## NITs (new)

**P1A-n8 (Sec. XII A):** "The framework has not solved the cosmological constant problem; it has only relocated the fine-tuning into inflationary initial conditions." This honest admission appears in a discussion paragraph that *follows* the headline claim of "10¹²⁰ → 10⁵ reduction" in Sec. I. The reader should encounter the admission first, the bookkeeping second.

**P1A-n9 (Acknowledgments, p. 18):** "We thank the Planck, CMB-S4, LiteBIRD, LSST, and DESI collaborations." Acknowledging future collaborations (CMB-S4, LiteBIRD) by name for "providing the observational foundation" is unusual — they have not yet provided observations.

**P1A-n10 (Sec. XV, p. 18):** The 2.4σ / 0.73σ recalculation in the LiteBIRD prediction paragraph (already P1A-M10 in initial review) explicitly walks back the conclusion's own "9σ" claim — the walked-back number appears in the same sentence as the original claim. This is a clear sign of unresolved editing.

**P1A-n11 (Footnote markers):** Footnote 1 (Sec. VII) is the only numbered footnote in the body. Sec. III B and others use unnumbered marginal notes. Standardize.

---

## Closing remark on the second pass

The arithmetic errors (P1A-E13, P1A-M16), the citation error (P1A-E14), the dimensional-convention drift (P1A-M17), and the self-contradicting suppression argument (P1A-M19) are not isolated typos. They are symptoms that the paper has been edited many times, with downstream consequences not always propagated to upstream prose. Combined with the initial-review issues — dimensional-inconsistency of the central operator (P1A-E2), abstract walkback (P1A-E1, E6), trivial-result-as-theorem (P1A-E7), references-in-preparation (P1A-E3), and unverifiable references (P1A-E4, E5) — the manuscript is not yet in a state where individual fixes can produce a publishable paper. The recommendation stands: reject with leave to resubmit as a substantially shorter Brief Report after the four companion papers are publicly available and after the operator basis is properly closed (or after the dark-energy mapping is removed and the paper is reframed as a perturbation-theory note).