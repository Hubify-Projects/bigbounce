# P1A auto-2026-06-08_1354pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (10044 chars)
**Wall time**: 487.9s

---

# Referee Report — Paper P1A
**"Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"**

## Overall Assessment

This paper is a 21-page document whose central claim — a "channel-level closure" of four ECH dark-energy routes — collapses under its own hedges. The author admits (i) the four routes are *not* a complete operator basis, (ii) the central dimensional analysis is "an ansatz, not a derivation," (iii) the two "surviving predictions" are *not* predictions of ECH, (iv) Route 4 (the ALP route) is not actually closed but only objected to on naturalness grounds, and (v) the "perturbation transparency theorem" is a near-trivial consequence of the 1976 Hehl result for canonical scalar matter. After removing these layers, the actual scientific content is: *if matter is scalar-only and the operator basis is restricted to four named channels, then the Holst sector cannot source dark energy at the amplitudes considered*. This is not a PRD-grade result. Compounding this, the paper rests heavily on **four "companion papers in preparation" by the same author** for headline numbers (MCMC values, fNL forecast significance, PTA γ posterior, galaxy chirality null), making the central numerical assertions unverifiable. The paper also contains explicit **draft-history language and internal version-tracking** in the submitted body. Length is grossly excessive for the actual content delivered.

---

## ESSENTIAL findings (must be fixed before any further review)

### P1A-E1 — Internal draft/version-history language in submitted body (multiple locations)
- **p. 15, Sec. X.G:** *"This figure supersedes the earlier synthetic-Gaussian-likelihood value γ = 3.20±0.42 used in pre-real-KDE drafts; the migration is documented in Paper III § 6."*
- **p. 16, Sec. XII.A:** *"the ∼ 35 misstated in earlier drafts"* / *"not the ∼ 35 misstated in earlier drafts"*
- **p. 19, Appendix B:** *"we make that status explicit here so the reader is not misled by an apparent 'fix' in earlier drafts."*
- **p. 16, Table III footnote ‡:** project-status-update prose ("*running on a dedicated MPI pod (16 chains, OMP threads tuned to suppress BLAS oversubscription, GetDist-built posterior covmat from a preliminary 4-chain iter1 with ∼9,500 accepted samples) ... ∼3.8×10⁴ accepted samples ... R̂−1 ≈ 3×10⁻²*").

This is review-log language. It must be removed from any PRD submission.

### P1A-E2 — Critical numerical claims rest on unsubmitted/unposted companion papers
Headline numbers (`H₀ = 67.68 ± 1.06`, `ΔN_eff = −0.020 ± 0.169`, the 309,189-sample MCMC, the σ(fNL) ≈ 0.7 SPHEREx forecast, the γ = 2.567 ± 0.382 PTA posterior, the galaxy-spin null) all reference companion papers I(b), II, III, IV explicitly tagged "**in preparation**" (refs [2], [6], [23], [46], [47]). The author even says (p. 5): *"they are documented internally rather than as externally citable arXiv-posted numbers, and should be read as internal-analysis inputs to the present structural argument rather than as independently peer-reviewable values until Paper I(b) is publicly posted."* PRD does not accept this. Either (a) all four companion papers must be on arXiv before this paper is reviewed, or (b) every number derived from them must be removed.

### P1A-E3 — The "surviving" predictions are admittedly NOT predictions of this work
Abstract, p. 1: *"The two predictions discussed below as 'surviving' are accordingly **not predictions of ECH itself**"*; and again, *"(ii) spectator-ALP birefringence β ≈ 0.27° is a benchmark consistency point, **not an ECH prediction**"*; and *"fNL = −35/8 is a property of the matter-bounce class [1], derived from the contraction-phase cubic action **with no ECH input**."* The paper therefore claims testable predictions in the abstract that it then explicitly disowns. This is misleading framing. The abstract structure must be rewritten so that the testable-prediction language is removed or recast as "predictions of unrelated frameworks not excluded by this analysis."

### P1A-E4 — Route 4 is not closed; the no-go is incomplete and is presented misleadingly
- Sec. IV.D, p. 10: *"R4 is therefore **not closed** by amplitude mismatch (as prior analyses claimed); it is closed by the observation that the same coupling that produces β_obs requires an ultralight-mass tuning m_θ ∼ H_0 to also produce ρ_Λ"* — i.e., a naturalness objection, not a closure.
- Same section: *"the spectator-ALP route does technically reproduce the dark-energy density at the R4-fitted coupling"*.
- Sec. IV.E, p. 11: *"R4 (parity-odd CMB coupling) is closed by a naturalness objection: with α/M treated as a free parameter, a spectator-ALP fit reproduces both β_obs and ρ_Λ"*.

The abstract and title nonetheless advertise "channel-level closure of four routes." This is false for Route 4 in the technical sense the field uses "closure." Either the abstract must say "three amplitude closures plus one naturalness objection" or Route 4 must be argued at amplitude level. The current framing is overclaim.

### P1A-E5 — 30-orders-of-magnitude unresolved ambiguity in Route 2 amplitude estimate
Sec. IV.B, p. 9, Eq. (15) discussion: *"∆θ_one-loop/∆θ_obs ∼ 10⁻⁵⁸ to 10⁻⁶⁰ (the factor-of-∼100 ambiguity reflects ε-correction perturbative-order scaling alone…) We adopt this contraction as the canonical Route-2 estimate; an alternative ordering that contracts the H₀ factor with the dimensionful coupling differently yields a numerically distinct ∼ 10⁻³³ ratio."* A **30-order-of-magnitude** difference between two equally-defensible dimensional reductions of the same one-loop estimate is not "robust at the order-of-magnitude level"; it is a sign that the dimensional analysis is uncontrolled. The "Route 2 amplitude closure" cannot be claimed under such an ambiguity. Either commit to one calculation with full dimensional bookkeeping or withdraw the Route-2 claim.

### P1A-E6 — Routes 2 and 3 closures rest explicitly on undeclared/unproven coefficient structures
- Sec. IV.B, p. 9: *"no published calculation currently derives this exact coefficient structure from the Mercuri construction, and the present analysis uses it strictly as an upper-bound EFT ansatz."*
- Sec. IV.C, p. 10: *"we use Eq. (16) only as an upper-bound EFT ansatz for the Route-3 amplitude budget and do not claim it is taken verbatim from [26]."*

A "no-go" theorem cannot rest on ansatz coefficients chosen by the author. The body must either derive the coefficients or downgrade the language from "closes" to "is consistent with closure under one EFT ansatz."

### P1A-E7 — Central operator is dimensionally inconsistent; "scaling ansatz" admission is too late
Appendix B, p. 19: *"the parity-odd operator (Eq. 6) has off-shell mass dimension +1, not the +4 required for a local Lagrangian density."* The author then offers two reconciliations: (i) treat the on-shell evaluation as an ansatz, (ii) promote α/M → α M_Pl³/M. **Either reading is** *"a phenomenological dimensional assignment, not a derivation"*. Equation (6) appears in the body without this warning. A dimensionally inconsistent Lagrangian density cannot be used as the starting point of an amplitude no-go theorem. The mass dimension audit must appear inline at Eq. (6), and all downstream conclusions that depend on the M_Pl⁵ identification must carry an explicit "ansatz-dependent" tag.

### P1A-E8 — "Perturbation transparency theorem" is essentially a 1976 result, not a new theorem
Sec. X is presented as the *"central result"* of the paper. Its content (p. 14): for canonical scalar matter, S = 0 ⇒ T = 0 ⇒ Γ = Γ̊ ⇒ Holst → Pontryagin, which is a total derivative. This was implicit in Hehl, von der Heyde, Kerlick & Nester (1976) [12] (cited by the author) and is a textbook consequence. Calling this a "theorem" central to the paper is overclaim. Recast as "consequence" or "observation," remove "generalizes Hehl et al. (1976) to … all perturbation orders" (it doesn't — the all-orders statement is trivially equivalent to the order-zero statement once S = 0).

### P1A-E9 — Abstract is wildly out of PRD format
The abstract is approximately **700 words** and contains literature citations, equations, and footnote-like asides ("a contracting-phase quantity mode with k_SPHEREx ~ 10⁻¹ h/Mpc is pushed to k^phys_bounce ~ k^phys_SPHEREx e^{N_tot - N_exit} ~ e³² k^phys_SPHEREx…"). PRD's standard limit is ~250 words and no inline citations. The abstract must be rewritten to a single paragraph stating the claim, the method, and the conclusion.

### P1A-E10 — Internal "13 logically-independent / 14 historical catalog entries" bookkeeping is incoherent
Repeatedly: *"13 logically-independent mechanism-class constraints"* but *"14 historical catalog entries, of which B8 is subsumed by B14"* (abstract; pp. 4, 14, 17, 18). Listing 14 items and immediately admitting one is subsumed by another is padding. Either (a) eliminate B8 entirely, or (b) keep the 14 catalog and stop calling them "logically independent." The repeated dual-counting framing reads as an attempt to inflate the appearance of structural support and should be removed.

### P1A-E11 — "Internal MCMC" cited as evidence for ΛCDM consistency cannot be used as paper evidence
p. 5: *"Cosmological parameter values referenced in this paper (H_0 = 67.68 ± 1.06, ∆N_eff ≈ 0, etc.) are drawn from the companion internal MCMC analysis (Paper I(b) [6], in preparation); they are documented internally rather than as externally citable arXiv-posted numbers."* An "internal" un-posted MCMC chain is not citable evidence in PRD. Either remove these numbers from the paper or post Paper I(b) and re-cite.

### P1A-E12 — Conclusion's "9σ" claim is self-admitted to be the wrong test
p. 18: *"LiteBIRD … detects non-zero β at ∼ 9σ (a 0.27°/0.03° overall sensitivity number). The relevant model-discrimination test, however, is the differential against the prior central value … LiteBIRD will distinguish the spectator-ALP-derived 0.27° from the observed 0.342° at … ≈ 0.73σ."* The "9σ" number is therefore advertised in a position of prominence while the actual model-discrimination significance is sub-sigma. Per the reviewer guidelines, sigma values from different null procedures must not appear side by side without "not directly comparable" qualifications throughout — the qualifier appears only after the headline number. Remove the 9σ figure or relocate it with a primary "this is not the relevant test" tag.

### P1A-E13 — Numerical inconsistency between "10¹²⁰", "10¹²¹", "10¹²²", and "10¹²³"
- Abstract / Sec. II.C: *"Ξ ∼ 10⁻¹²³"*
- p. 7: *"reparameterizes the fine-tuning hierarchy from 10¹²² ... to ∼10⁵"*
- Sec. XII.A, p. 15: *"D_inf ∼ 10⁻¹²¹"*; later *"the ∼ 35 misstated in earlier drafts"* and rewrites to *"10¹²²"*
- Appendix B, p. 19: *"D_inf ∼ e^{−3N_tot} ∼ 10⁻¹²²"*; *"N_tot ≈ 122 ln 10/3 ≈ 94 e-folds (consistent at the ∼ 2% level with the structural-tension N_tot ≈ 92 quoted in Sec. XIV D)"*

So the paper carries two values of N_tot (92 and 94) with internally inconsistent decompositions of Ξ. Recompute: 3 × 92 × log₁₀ e = 119.84 → 10⁻¹²⁰, not 10⁻¹²¹ or 10⁻¹²². The 1–2 order-of-magnitude inconsistency runs through every dimensional bookkeeping argument and must be tabulated and reconciled in a single audit.

---

## MAJOR findings

### P1A-M1 — Page length grossly exceeds scientific content
The actual derived result is one paragraph (Sec. X.B, p. 14, five steps). The accompanying 20 pages are largely (i) restatements of well-known no-go arguments, (ii) bookkeeping of an admitted ansatz, (iii) repetition of structural-tension wording across abstract, Sec. I, Sec. XIII, Sec. XIV.D, Sec. XV. Recommended maximum page count for the content delivered: **8 pages** (PRD Brief Report or one PRD article).

### P1A-M2 — Repetition of the "structural tension" / "N_tot ≈ 92 vs fNL erasure" paragraph
Verbatim or near-verbatim appearances of the *"e^32 k_SPHEREx ... vacuum-inflationary subhorizon"* passage in: abstract (p. 1), Sec. I.A (p. 3), Sec. XIII (pp. 16–17), Sec. XIV.D (p. 17), Sec. XV (p. 18 indirectly). Consolidate to one place.

### P1A-M3 — Section IV "Scope" caveat undermines section's stated purpose
Sec. IV opens by *"closing"* the four routes, then in the "Scope" paragraph (p. 8) admits *"we close R1–R4 at the channel-amplitude level because that is the level at which the observational budget of Sec. III discriminates; a full operator-level no-go would require enumerating all dimension-6 parity-odd four-fermion + gravitational Chern-Simons operators … which is deferred to a follow-up theory paper."* If the operator-level no-go is deferred, the title's "Channel-Level Closure" framing should make this explicit and stop using "no-go" without qualification in the body.

### P1A-M4 — Eq. (11) `(T_reh/M_GUT)^(3/2)` factor is "dimensional-analysis aesthetic"
Sec. II.C.1 (pp. 6–7) lengthy footnote: *"a fully rigorous first-principles derivation of the half-integer power requires the parity-odd density-of-states phase-space integral, which is dimensional-analysis aesthetic at this level rather than calculated from a thermal partition function."* This load-bearing prefactor of the dark-energy matching is openly described as aesthetic. PRD-grade work cannot use load-bearing aesthetic prefactors.

### P1A-M5 — "Barrier 13 (Gravitational Democracy)" admitted to be philosophy
Sec. IX preamble (p. 12): *"Structural/philosophical observations (Barrier 13): gravitational democracy, included for completeness."* Philosophical observations included for completeness should not be counted toward a quantitative "14-barrier closure." Remove from the count.

### P1A-M6 — Barbero–Immirzi "uncertainty" is presented in ± form (Table IV, p. 20)
Table IV: *"γ ... 0.274 (scheme range ∼0.020)"*. Earlier (p. 5) author explicitly admits this is **not** a statistical uncertainty. Presenting it in a column whose other entries are 1σ posteriors (`H₀ = 67.68 ± 1.06`) is misleading. Either move γ to a separate panel or render as a range, e.g., `0.13–0.27`.

### P1A-M7 — Sec. XI ("Hybrid Dark-Energy Loophole") is hand-waved
*"The loophole was explored theoretically but the w0wa extension was never implemented computationally in this program."* A non-implemented exploration of 7 disguised forms of w₀wₐ is not a refutation of those forms. Remove or replace with explicit references to the (existing) literature ruling them out.

### P1A-M8 — Table III footnote ‡ is a project-status update, not a paper footnote
p. 16: chain status, MPI pod configuration, OMP thread tuning, R̂−1 ≈ 3×10⁻², "we deliberately do not commit to a specific calendar date for convergence." This is fully inappropriate for a published table. Replace with a single line: "w₀wₐ chain not yet converged at submission."

### P1A-M9 — Inconsistent γ_PTA reporting
Table IV (p. 20): γ_PTA = 2.567 ± 0.382 (real-KDE GPU MCMC). Sec. X.G (p. 15): same. **But** the Figure 1 right column (p. 4) shows *"PTA γ = 3.0 v.s. data 3.20 ± 0.42 (P3 §6)"* — referencing the pre-real-KDE value the paper otherwise calls "superseded." Either update the figure to the new value or remove the figure entry.

### P1A-M10 — Fig. 1 (p. 4) caption / content mismatch
Caption says ECH appears "bordered with a dashed box marked *channel-level closure under stated assumptions (this paper)* — the 14-constraint catalog narrows the four enumerated minimal-ECH dark-energy channels to **zero phenomenologically free pathways**." The body explicitly disputes this: Route 4 admits a free-coupling spectator-ALP fit reproduces both observables (p. 10). The figure overclaims what the body proves.

### P1A-M11 — DESI 2024-2025 statement understates citation precision
p. 3: *"DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ (dataset-dependent)"*. Refs [9, 10] should be split: DESI DR1 (2024) and DESI DR2 (2025) report distinct significances per dataset; the 3.1σ vs 4.2σ range collapses two different significances from different combinations. Cite the specific dataset combination per quoted sigma value.

### P1A-M12 — "Channel-Level Closure" of route 1 silently uses a parity audit fixed inline
Sec. IV opening (p. 8): the parity-classification of (ψγ^aγ^5ψ)² is "addressed in-line" with a tortured explanation: *"the axial-vector current ... is a pseudovector (parity-odd component by component), but the Lorentz contraction of two such pseudovectors gives a scalar that is parity-even"*. Standard textbook content presented as if it required justification — suggests a previous draft had the parity wrong. Should be reduced to a single line or removed.

### P1A-M13 — Eq. (15) — quoted α_em/(4π) ≈ 5×10⁻⁴ and ≈ 5.8×10⁻⁴ in same sentence
*"αem/(4π) ≈ 5×10⁻⁴ (more precisely ≈ 5.8×10⁻⁴ since αem ≈ 1/137)"*. Pick one and stop the parenthetical correction.

---

## MINOR findings

### P1A-Mi1 — "Date PDT" timestamp
p. 1 header: *"Dated: June 2, 2026 PDT"*. Time zones belong on internal documents, not PRD title pages.

### P1A-Mi2 — Acknowledgment of Claude AI
p. 18: appropriate but should follow PRD's specific AI-use guidelines once they're finalized; verify current journal policy.

### P1A-Mi3 — Self-citation hash tags in references
[2], [6], [23], [46], [47] include in-house identifiers like *"hUBIFY-2026-002; companion paper, this volume."* Remove the hash tags. PRD references should not include internal project codes.

### P1A-Mi4 — Reference [44] arXiv ID
*"Y.-F. Cai and J.-H. Zhu (2026), arXiv:2603.13924"*. arXiv numbering is YYMM.NNNNN; "2603" would correspond to March 2026, plausible given the paper's date but the user should verify the ID exists before submission.

### P1A-Mi5 — Reference [10] DESI DR2 cited as PRD 112, 083515 (2025)
Verify the volume/page assignment matches the published PRD article rather than the arXiv version.

### P1A-Mi6 — Repeated em-dashed asides in body equations
e.g., p. 6 *"(this is the standard cold-relic scaling for a non-relativistic species, and holds at the cubic axial-current operator level because the cube of the fermion bilinear scales as the cube of the fermion number density at the bounce-density regime where the algebraic relation is saturated…)"* — running ~150 words inside an equation justification. Convert to a separate paragraph or footnote.

### P1A-Mi7 — Figure 2 (p. 5) caption
*"illustrating the phenomenological scaling ansatz ρ_vac ∼ [(α/M) M_Pl] M⁴_Pl"* — useful figure but axis labeling not fully described in the caption. Confirm the y-axis explicitly says "log₁₀(ρ/ρ_Pl)" or similar.

### P1A-Mi8 — Sec. II.B and Sec. II.C reproduce known LQC content
Eqs. (8)–(9) and standard LQC bounce density discussion are textbook material. Cut by 50%.

### P1A-Mi9 — Section XIII reproduces Sec. I.A content
*"Survival of mechanism-independent tests"* appears in nearly identical form in introduction and again as Sec. XIII. Pick one location.

### P1A-Mi10 — Sec. X.D Eq. (23) typesetting
*"R̃(Γ̊) = ½ ε^{μνρσ} R_{μνρσ}(Γ̊) = ½ *R R ≡ ∂_μ K^μ"* — the middle expression `*R R` is ambiguous notation; spell out `(*R)R` or `RR̃`.

---

## NIT-level

- N1 — *"This work in preparation [6]"* phrasing redundantly used dozens of times. Standard form: "in preparation."
- N2 — Inconsistent comma usage in author byline / affiliation footer.
- N3 — Eq. (4): J⁵_μ J⁵^μ written without explicit parentheses; convention OK but could be clarified.
- N4 — Multiple parenthetical asides nested 3 deep ("(...(...(...)...)...)") on pp. 1, 6, 7, 17 hurt readability.

---

## Summary recommendation

**REJECT**

The paper does not meet PRD's standards. The headline result ("channel-level closure of four ECH dark-energy routes") is undermined by the author's own admissions: the operator basis is incomplete, the central dimensional analysis is an ansatz (off-shell mass-dimension mismatch of +3), Route 2's amplitude estimate carries an unresolved 30-order-of-magnitude ambiguity, Routes 2 and 3 rest on ansatz coefficients explicitly not derived from the cited literature, Route 4 is not closed at all but only objected-to on naturalness, and the "central perturbation-transparency theorem" is a textbook consequence of the 1976 Hehl et al. result for spinless matter. The two "surviving testable predictions" are admitted in the abstract not to be predictions of the framework. Numerical headline values (H₀, ΔN_eff, σ(fNL), γ_PTA) are sourced from four unposted companion papers by the same author and cannot be verified. The submitted body contains explicit draft-history language (*"earlier drafts," "supersedes," "misstated"*) and project-status updates that have no place in a journal article. Length is roughly 3× the content delivered. Before any further review, the author must (i) post the four companion papers, (ii) eliminate every "in earlier drafts" passage, (iii) resolve the Route 2 ambiguity, (iv) rewrite the abstract to honestly summarize what is proved, (v) either close Route 4 at amplitude level or rename the paper's central claim. A substantially shortened resubmission (≤ 8 pages) might be considered, but the present manuscript is not viable.

---

## PASS 2 — self-critique findings (what initial review missed)

# Second-Pass Referee Report — Paper P1A
**Additional findings from focused arithmetic, cross-reference, and abstract-faithfulness audit**

---

## ESSENTIAL findings (new)

### P1A-E14 — Arithmetically incorrect ACT-vs-WMAP+Planck tension figure
p. 10, Sec. IV.D: *"the independent ACT DR6 follow-up of Diego-Palazuelos & Komatsu [5] reports β = 0.215° ± 0.074° at ∼2.9σ, **consistent within ∼ 1.4σ**"*. Recompute the differential:
- Δβ = 0.342° − 0.215° = 0.127°
- σ_combined = √(0.094² + 0.074²) = √(0.00884 + 0.00548) = √0.01432 = 0.1197°
- Δβ / σ_combined = 0.127 / 0.1197 = **1.06σ**, not 1.4σ.

The 1.4σ figure is wrong by ≈30%. This is the only direct quantitative tension statement between the two leading birefringence measurements in the paper and it propagates into the discussion of whether the spectator-ALP "benchmark consistency" claim is reasonable. Fix the arithmetic.

### P1A-E15 — Credit misattribution: Eskilt & Komatsu's value attributed to Minami & Komatsu
Abstract (p. 1): *"βobs = 0.342° ± 0.094° (∼ 3.6σ from β = 0, **first reported by Minami & Komatsu [3]** and refined by Eskilt & Komatsu [4])"*. This is incorrect. Minami & Komatsu 2020 [3] reported β = 0.35° ± 0.14° at ∼2.4σ. The value β = 0.342° ± 0.094° at 3.6σ is from Eskilt & Komatsu 2022 [4], NOT first reported by Minami & Komatsu. The credit assignment in the abstract conflates two distinct measurements with different significances. Recast as: *"first detected by Minami & Komatsu [3] (β = 0.35° ± 0.14°, ∼2.4σ) and refined to β = 0.342° ± 0.094° (∼3.6σ) by Eskilt & Komatsu [4]"*.

### P1A-E16 — Broken cross-reference in abstract
Abstract (p. 1): *"we acknowledge missing operators (Jackiw-Pi gravitational Chern-Simons R∧R̃, parity-odd four-fermion partner with γ_BI/(γ²_BI + 1) · 8πG coefficient) explicitly **in Sec. IV and Sec. XI**."*

Sec. XI is titled "The Hybrid Dark-Energy Loophole" and discusses w₀wₐ CPL extensions, quintessence scalars, curvaton-derived potentials, etc. It contains **zero discussion** of the Jackiw-Pi gravitational Chern-Simons term or the parity-odd four-fermion partner. The correct cross-reference is to Sec. IV (Scope paragraph) and Sec. IV.E (Closure summary). The abstract's pointer to Sec. XI is a broken cross-reference that misleads any reviewer who follows it.

---

## MAJOR findings (new)

### P1A-M14 — Sec. III.A's "observed isotropic birefringence at β ≈ 0.27°–0.30°" doesn't bracket either measurement
p. 8, Sec. III.A: *"The parity-odd structure is qualitatively consistent with the observed isotropic birefringence at β ≈ 0.27°–0.30°."*

But neither of the two birefringence measurements the paper itself cites falls in this range:
- WMAP+Planck (Eskilt & Komatsu): 0.342° ± 0.094° — **above** 0.30°
- ACT DR6 (Diego-Palazuelos & Komatsu): 0.215° ± 0.074° — **below** 0.27°

The "0.27°–0.30°" interval excludes both central values and appears to be the author's model prediction repackaged as an "observed" range. Either source this range or rewrite to "the model prediction β ≈ 0.27° is qualitatively consistent with the observed central value 0.342° at ∼0.7σ", which is the correct framing.

### P1A-M15 — Backfit indication: ρ_θ computation in Sec. IV.D matches ρ_Λ exactly to two digits
p. 10, Sec. IV.D: *"ρ_θ = m_θ²β²/[2(α/M)²]; plugging in α/M = 10⁻²¹ GeV⁻¹, β = β_obs ≈ 6 × 10⁻³ rad, and m_θ = H_0 ≈ 1.5 × 10⁻³³ eV gives **ρ_θ ≈ 2.8 × 10⁻¹¹ eV⁴ ≈ ρ_Λ** to within a factor of unity"*.

Independent recomputation with the stated inputs gives:
- ρ_θ = (1.5×10⁻³³)² × (6×10⁻³)² / [2 × (10⁻³⁰)²] = 4.05 × 10⁻¹¹ eV⁴

The author's claimed value 2.8 × 10⁻¹¹ eV⁴ is the **exact** value of ρ_Λ = (2.3 meV)⁴. The forward-computation with stated parameters gives 4.05 × 10⁻¹¹, a factor of 1.4 higher. The value quoted in the paper appears to have been set equal to ρ_Λ rather than computed from the stated inputs. To get 2.8 × 10⁻¹¹ requires α/M = 1.2 × 10⁻²¹ GeV⁻¹, not the 10⁻²¹ stated. Either restate as "the input α/M = 1.2 × 10⁻²¹ GeV⁻¹ is chosen so that the spectator ALP saturates ρ_Λ", or compute ρ_θ honestly from the stated input and report 4 × 10⁻¹¹.

### P1A-M16 — Eq. (16) RG running estimate "Δγ/γ ∼ 10⁻²" inconsistent with the formula's own SM prediction
p. 9–10, Sec. IV.C: *"In the Standard Model, the chiral asymmetry is generated by the SU(2)_L doublets; numerically, Δγ/γ ∼ 10⁻² over the running from the GUT scale to the IR."*

Applying Eq. (16), dγ/d ln μ = γ × (N_F^L − N_F^R)/(12π²), with SM chiral asymmetry N_F^L − N_F^R ∼ 45 (15 LH Weyl fermions × 3 generations, no RH partners) and Δ ln μ ∼ ln(10¹⁹) ≈ 44 from M_GUT to IR:
- Δγ/γ ≈ 44 × 45 / (12 π²) ≈ 16.7,

i.e. the perturbative expansion breaks down at order unity, ∼3 orders of magnitude away from the quoted "10⁻²". The footnote does say "we use Eq. (16) only as an upper-bound EFT ansatz" but the quoted numerical conclusion "10⁻²" is not consistent with the formula at SM matter content. Reconcile the prefactor convention or remove the "10⁻²" estimate.

### P1A-M17 — H₀/σ₈ tension language ambiguity in Table I and conclusion
p. 4, Table I: *"H_0/σ_8 tension resolution? → H_0 = 67.68 ± 1.06, ΔN_eff ≈ 0 → Recovers ΛCDM."*

This is misleading: the "H₀ tension" refers to the discrepancy between local SH0ES (~73) and CMB-anchored (~67). Quoting an H₀ ≈ 67.7 internally-MCMC'd value that sits firmly on the Planck side does **not** "resolve" the tension; it merely recovers one side of it. The correct status is "does not address the H₀ tension." Same applies to the σ₈ tension. Table I currently signals to the reader that the framework solves these tensions when in fact it does not engage them.

### P1A-M18 — Eq. (15) quoted spread of 10⁻⁵⁸ to 10⁻⁶⁰ doesn't reproduce in straightforward substitution
Re-substituting the author's own values into Eq. (15):
- (α_em/4π) × (H₀/M_Pl) / [M_Pl(α/M) × β_obs]
- ≈ 5 × 10⁻⁴ × 10⁻⁶¹ / (10⁻² × 6 × 10⁻³)
- ≈ 5 × 10⁻⁶⁵ / 6 × 10⁻⁵ ≈ 8 × 10⁻⁶¹

So the canonical estimate lands at ∼10⁻⁶⁰ to 10⁻⁶¹. The paper claims "∼ 10⁻⁵⁸ to 10⁻⁶⁰" — the upper end 10⁻⁵⁸ doesn't appear from any choice of "ε-correction perturbative-order scaling alone" with the inputs supplied. The 100× spread internal to the canonical estimate is unjustified by the inputs as written.

---

## minor findings (new)

### P1A-mi11 — "factor of ~3" tightening from LiteBIRD
Sec. IV.D, p. 10: *"LiteBIRD … will tighten this bound by a factor of ∼3"* (correct: 0.094/0.03 = 3.13). However the tightening referenced is on σ(β), not on the bound on α/M or m_θ. Statement is technically correct but ambiguous about what quantity is tightened.

### P1A-mi12 — "factor of unity" stretched
Sec. IV.D, p. 10: ρ_θ "to within a factor of unity" of ρ_Λ. Recompute gives 4.05/2.8 ≈ 1.4. "Factor of unity" typically means within ∼20%; here it's 40%. Either quote "to within a factor of 1.5" or recompute.

### P1A-mi13 — γ²/(γ²+1) coefficient in Eq. (4) numerical value not used downstream
For γ = 0.274, γ²/(γ²+1) = 0.075/1.075 = 0.0698. The structural barriers Sec. IX use neither this prefactor nor its parity-odd partner γ/(γ²+1) = 0.256 numerically. The Holst coupling enters via mass-dimension arguments only. This is not a flaw per se but the explicit γ-dependence is presented in Eq. (4) only to be discarded — flagging in case it is intentional (then justify) or accidental (then remove the γ-explicit coefficient).

### P1A-mi14 — "30-orders-of-magnitude" Route 2 ambiguity is actually 27 OOM
P1A-E5 above said "30 OOM"; the paper reports 10⁻⁵⁸ → 10⁻⁶⁰ canonical vs 10⁻³³ alternative, i.e. |−60 − (−33)| = 27 OOM. Both are catastrophically large; flagging only for arithmetic precision in any rebuttal letter.

### P1A-mi15 — `0.342° / 0.094° = 3.64`, paper rounds to 3.6σ (acceptable)
Just confirming the abstract value is consistent at 1-sig-fig rounding. Acceptable.

### P1A-mi16 — `0.215° / 0.074° = 2.91`, paper rounds to 2.9σ (acceptable)
Same as above.

### P1A-mi17 — `√3 / (32 π² × 0.274³) = 0.267 ≈ 0.27`
Spot-check: ρ_crit/ρ_Pl from Eq. (9) at γ = 0.274 reproduces the quoted 0.27 ρ_Pl. ✓ Arithmetic clean.

### P1A-mi18 — `√3 / (32 π² × 0.2375³) = 0.41`
Spot-check: ρ_crit/ρ_Pl at γ = 0.2375 reproduces the standard 0.41 ρ_Pl from Ashtekar & Singh. ✓ Arithmetic clean.

### P1A-mi19 — Heinrich et al. degraded sensitivity arithmetic
Footnote 1, p. 11: "raw ratio |fNL|/σ = 4.375/0.7 ≈ 6.25σ, degraded to ∼5–5.5σ optimistic after template-overlap correction r ≈ 0.84". With r = 0.84: 6.25 × 0.84 = 5.25σ. ✓ matches "∼5–5.5σ".

---

## Summary of second-pass

Six new ESSENTIAL/MAJOR issues surfaced under arithmetic and cross-reference audit:

1. **E14** — wrong σ value for ACT-vs-WMAP+Planck tension (1.4σ → actual 1.06σ);
2. **E15** — Eskilt & Komatsu's value misattributed to Minami & Komatsu in the abstract;
3. **E16** — abstract cross-reference to Sec. XI for "missing operators" is broken (Sec. XI is about CPL w₀wₐ);
4. **M14** — "observed birefringence 0.27°–0.30°" doesn't include either cited measurement;
5. **M15** — ρ_θ = 2.8 × 10⁻¹¹ eV⁴ appears back-fitted to ρ_Λ rather than computed from stated α/M;
6. **M16** — Eq. (16) numerical estimate Δγ/γ ∼ 10⁻² inconsistent with the equation's own application to SM chiral content;
7. **M17** — H₀/σ₈ "tension resolution" language in Table I is misleading;
8. **M18** — Eq. (15) "10⁻⁵⁸ to 10⁻⁶⁰" canonical spread doesn't reproduce from stated inputs.

Combined with the first-pass findings, the paper exhibits a pattern of:
- (a) hand-arithmetic errors at the OOM level in load-bearing dimensional estimates,
- (b) load-bearing numerical claims that don't recompute from stated inputs,
- (c) misattribution and broken cross-references in the abstract itself,
- (d) "consistency" framing that conceals actual numerical disagreements.

This pattern further reinforces the original recommendation of **REJECT**. The errors in the abstract (E15, E16) alone are disqualifying for a PRD-grade submission, since the abstract is precisely the location where editorial scrutiny demands zero broken-cross-reference and zero credit-misattribution defects.