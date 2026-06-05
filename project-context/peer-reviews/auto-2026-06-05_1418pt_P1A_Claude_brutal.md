# P1A auto-2026-06-05_1418pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (17278 chars)
**Wall time**: 504.3s

---

# Referee Report — P1A
**Manuscript:** "Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"
**Journal:** Physical Review D
**Recommendation: REJECT**

---

## Overall assessment

This is a 21-page manuscript whose substantive content is: (i) a textbook observation that algebraic torsion vanishes when the matter sector has zero spin density and the Holst term then reduces to a Pontryagin density (well known since Hehl-Datta 1971 and Mercuri 2006); (ii) order-of-magnitude amplitude estimates for four channels by which an Einstein–Cartan–Holst sector might source dark energy, each of which is closed by Planck suppression in the standard textbook way; and (iii) a list of 14 "barriers" the author concedes is really 13 (B8 = consequence of B14), of which the author further concedes only 9 are "novel" (and the novel ones are mostly restatements of dimensional analysis).

The paper acknowledges, in Appendix B, that its central equation (Eq. 6) has the **wrong mass dimension** for a local Lagrangian density, and that the entire dark-energy mapping is therefore a "phenomenological on-shell scaling ansatz, not a controlled EFT result." Four cited foundational results (companion Papers I(b), II, III, IV, and Ref. [47]) are not publicly available. Internal version-history prose, explicit references to "earlier drafts," and a figure that contradicts the text on a load-bearing number all appear in the manuscript body. None of these are acceptable in a PRD submission.

The result is not wrong, but it is also not new at the level of physics; the entire content is a long, hedged restatement of standard EFT counting plus a triviality about algebraic torsion. The paper does not meet the PRD novelty or rigor bar.

---

## ESSENTIAL findings

### P1A-E1 — Acknowledged dimensional inconsistency of the central operator
**Location:** Appendix B, p. 19; Eq. (6), p. 6; Sec. II C, p. 6.
**Issue:** The author explicitly states "[L_odd] = +1" — three units short of the +4 required for a local Lagrangian density — and concedes "the missing powers of mass do not arise from off-shell EFT counting but from on-shell scaling assumptions." Equation (B2) ρ_Λ^bounce ~ (α/M) M_Pl^5 is then called "a phenomenological on-shell scaling ansatz, not a controlled EFT result." This is not a minor technical issue; it is the manuscript's central equation and the entire dark-energy mapping rests on it. A PRD paper cannot rest its title claim on an admittedly dimensionally inconsistent operator that the author cannot promote to dimension 4 without a "phenomenological dimensional assignment."
**Fix required:** Either derive an EFT operator basis at the correct mass dimension, or withdraw the dark-energy mapping from the title, abstract, and Sec. II C.

### P1A-E2 — Four load-bearing companion papers cited as "in preparation"
**Location:** Refs. [2], [6], [23], [46], [47] (and the abstract, Sec. III B, Sec. V, Sec. VI, Sec. VIII, Sec. XII B, Sec. XIII, Sec. XIV).
**Issue:** Critical numerical results — the entire MCMC verification (H_0 = 67.68 ± 1.06, σ_8 = 0.803 ± 0.008, Δ N_eff = −0.020 ± 0.169), the full ALP MCMC, the galaxy spin null, the NANOGrav γ posterior, and the SPHEREx fNL forecast — are sourced to "in preparation" companion papers. Ref. [47] is "available upon request." Tables I, II, IV, the abstract, Sec. III B and Sec. XIV all depend on numbers that the reviewer cannot verify because the cited material does not exist publicly.
**Fix required:** Either post the companions before resubmission, or remove every numerical claim sourced to them. The structural argument must stand on its own.

### P1A-E3 — Figure 1 directly contradicts the body on a load-bearing number
**Location:** Fig. 1, p. 4 vs. Sec. X G, p. 15.
**Issue:** Figure 1 labels the PTA channel "γ = 3.0 v.s. data 3.20 ± 0.42 (P3 §6)". Section X G then states: "γ = 2.567 ± 0.382 from real-KDE re-analysis ... This figure supersedes the earlier synthetic-Gaussian-likelihood value γ = 3.20 ± 0.42 used in pre-real-KDE drafts." Table III column "PTA γ (real-KDE)" then shows a ✓ for matter bounce without quoting a value. The figure shows the explicitly superseded number.
**Fix required:** Regenerate Fig. 1 with the current value, or remove the PTA row.

### P1A-E4 — Internal version-history / audit-log language in the body
**Location:** Multiple, including:
- Sec. X G, p. 15: "This figure supersedes the earlier synthetic-Gaussian-likelihood value γ = 3.20 ± 0.42 used in pre-real-KDE drafts; the migration is documented in Paper III § 6."
- Appendix B, p. 19: "not the ∼ 35 misstated in earlier drafts"
- Appendix B, p. 19: "Either reading is a phenomenological dimensional assignment, not a derivation; we make that status explicit here so the reader is not misled by an apparent 'fix' in earlier drafts."
- Sec. IV B, p. 9: parenthetical about "A naive comparison of a rotation rate β̇ in eV against an angle uncertainty in eV would silently treat eV·s as dimensionless; the dimensionless reduction above avoids this..."
- Sec. II C 1, p. 7: half-page "Reheating thermal-reset barrier (supporting B14)" block that reads as patch material inserted to defend Barrier 14.

**Issue:** These are review-log artifacts. A submitted paper does not reference its own earlier drafts.
**Fix required:** Remove every reference to earlier drafts, supersession, "misstated," and the meta-commentary about "we make this status explicit so the reader is not misled."

### P1A-E5 — Headline "surviving predictions" are explicitly disowned as predictions of the framework
**Location:** Abstract, p. 1; Sec. XIII, p. 16; Conclusions, p. 18.
**Issue:** The abstract says "the two predictions discussed below as 'surviving' are accordingly not predictions of ECH itself." Section XIII calls β ≈ 0.27° "a consistency check, not a prediction" and notes f_NL = −35/8 is "not specific to ECH ... not a distinctive ECH prediction." The conclusions then list these as "surviving tests." If they are not predictions of the framework, they cannot be claimed as surviving tests of the framework. The structural posture of the paper is that ECH dark-energy is closed and the surviving science is unrelated to ECH — which is then not an ECH paper.
**Fix required:** Either commit to ECH-specific predictions (and derive them) or withdraw the surviving-prediction framing.

### P1A-E6 — Eq. (15) self-acknowledged ordering ambiguity of ~25 orders of magnitude
**Location:** Sec. IV B, p. 9.
**Issue:** The Route-2 amplitude budget gives "∆θ_one-loop/∆θ_obs ∼ 10^−58 to 10^−60" and immediately concedes: "An alternative ordering that contracts the H_0 factor with the dimensionful coupling differently yields a numerically distinct ∼ 10^−33 ratio." A factor of 10^25 ambiguity in the central amplitude-budget number of Route 2 is not "robust to ordering choice." Either the dimensional analysis is under control or the no-go is not under control.
**Fix required:** Fix the dimensional analysis. The "qualitative closure statement ... survives any reasonable dimensional reconciliation" is not adequate.

### P1A-E7 — Misappropriated foundational citations
**Location:** Sec. IV B, p. 9 (refs. [19, 22]); Sec. IV C, pp. 9–10 (ref. [26]).
**Issue:** Eq. (14) is attributed to Mercuri [19] / Mercuri & Capozziello [22]. The paper itself then states: "no published calculation currently derives this exact coefficient structure from the Mercuri construction." Eq. (16) is attributed to Date–Kaul–Sengupta [26]; the paper then states: "does not itself present the explicit RG equation used below." A reader is told that the foundational result was derived elsewhere, then told the citation does not contain it. Either derive it here, or cite the actual source.
**Fix required:** Derive Eqs. (14) and (16), or cite the actual derivation. "Motivated by" + "no published calculation derives this" does not constitute citation.

### P1A-E8 — Reference [47] "available upon request"
**Location:** Ref. [47], p. 21.
**Issue:** "Companion technical note, available upon request from the author." PRD does not accept this as a citation, particularly for a load-bearing photon-coupling result invoked at Sec. XII B.
**Fix required:** Post the note or remove the claim it supports.

### P1A-E9 — Overclaiming a textbook observation as a "theorem"
**Location:** Sec. I A, p. 3; Sec. X, p. 14; abstract.
**Issue:** The "perturbation-transparency theorem" is: a scalar matter sector has zero spin density → algebraic torsion is zero → Holst → Pontryagin → boundary term. Each step is standard (Hehl–Datta 1971 for step 1–2; Holst 1996 / Mercuri 2006 for steps 3–4). Calling this a "theorem" overclaims; it is a five-line application of well-known reductions. The further claim that this is a "generalization of Hehl et al. (1976) [12] to the Holst sector and to all perturbation orders" is misleading: the proof is that torsion vanishes identically, after which all orders trivially follow; "all orders" is not the content.
**Fix required:** Demote to "observation" or "decoupling lemma." Acknowledge the standard literature instead of inflating priority.

---

## MAJOR findings

### P1A-M1 — Length grossly exceeds content
**Location:** Entire manuscript (21 pages).
**Issue:** The substantive content (perturbation-transparency observation + four-route amplitude estimates + 9 mechanism-class restatements) is ~5–6 pages of physics. The remaining 15 pages are hedging, scope qualifications, abstract-of-the-abstract repetition, redundant cross-referencing to companion papers, and review-log patches.
**Recommended maximum:** 8 pages (PRD short article format) or remove from PRD pipeline entirely.

### P1A-M2 — Abstract is 50+ lines of unreadable hedged prose
**Location:** Abstract, p. 1.
**Issue:** The abstract contains six nested parenthetical qualifications, two cross-references to forthcoming work, a self-disclaimer that the "surviving predictions" are not predictions of the framework, and a 13-line single sentence about SPHEREx accessible k-modes that is internally repeated in Sec. XIV D. An abstract should state the result.
**Fix required:** Rewrite to ≤ 250 words stating the actual result.

### P1A-M3 — Routes R1–R4 admitted to not be independent at the operator level
**Location:** Sec. IV, "Scope" paragraph, p. 8.
**Issue:** "R1 (NJL parity-even four-fermion) and R4 (parity-odd ALP/axial-current CMB coupling) are not logically independent at the dimension-6 operator level: both are projections of the same torsion-elimination operator." Two acknowledged-missing operators (Jackiw–Pi R∧R̃ and the parity-odd four-fermion partner) are admitted to be absent. The title says "Four Minimal ... Dark-Energy Routes" — but the four are not independent and the operator basis is admitted incomplete. The closure claim is therefore weaker than the title.
**Fix required:** Either close the actual operator basis (including R∧R̃ and the parity-odd partner) or retitle "amplitude bounds on selected ECH channels."

### P1A-M4 — Reheating thermal-reset paragraph reads as patch material
**Location:** Sec. II C 1, p. 7, paragraph beginning "Reheating thermal-reset barrier (supporting B14)."
**Issue:** Half a page of prose explicitly labelled "supporting B14" is inserted into a Sec. II C 1 dilution discussion. The paragraph ends "We emphasize that this is bookkeeping, not progress" — i.e. the author is conceding the section adds no physics.
**Fix required:** Move to an appendix or delete.

### P1A-M5 — "13 logically-independent" / "14 historical catalog" double-counting
**Location:** Abstract; Table II caption; Sec. XV.
**Issue:** B8 is "the observational consequence of the perturbation-transparency theorem B14" and "should not be counted as logically independent." Then why is it in the catalog? Tables and prose repeatedly toggle between "13" and "14." The bookkeeping is inconsistent across sections.
**Fix required:** Decide on one number.

### P1A-M6 — Misleading "∼ 9σ" framing in Conclusions
**Location:** Sec. XV, p. 18.
**Issue:** "LiteBIRD ... detects non-zero β at ∼ 9σ (a 0.27°/0.03° overall sensitivity number)." The author then immediately concedes the relevant discrimination test is 0.73σ, not 9σ. The 9σ is a sensitivity-to-zero number — not the relevant test for the spectator-ALP hypothesis the paper is making. Listing 9σ first creates a false-confidence impression.
**Fix required:** Quote only the test that discriminates the model from the observed central value.

### P1A-M7 — Headline cosmological parameters not derived in this paper
**Location:** Sec. III B; Table IV; Table I.
**Issue:** H_0 = 67.68 ± 1.06 km/s/Mpc, σ_8 = 0.803 ± 0.008, ΔN_eff = −0.020 ± 0.169 are central to the structural-tension conclusion and the recovery of ΛCDM, but are all sourced to companion Paper I(b) "in preparation." The author notes "they are documented internally rather than as externally citable arXiv-posted numbers." This is not adequate for PRD.
**Fix required:** Post the companion or remove the headline numbers.

### P1A-M8 — Figure 2 picks one endpoint of a scheme-dependent range without noting it
**Location:** Fig. 2 caption, p. 5; ρ_crit/ρ_Pl discussion, p. 6.
**Issue:** Figure 2 labels the bounce density "ρ_c ≈ 0.27 ρ_Pl" but the text describes a scheme-dependent range 0.27–0.41 ρ_Pl. The figure quietly endorses one endpoint without noting it. The figure should plot the range or quote the band.
**Fix required:** Update caption and figure to show the band.

### P1A-M9 — β ≈ 0.27° status inconsistent across sections
**Location:** Sec. II A 2 and III A treat β as a "prediction" / "qualitatively consistent" with observation. Sec. XIII calls it a "consistency check, not a prediction." Conclusions list it as a "surviving test."
**Issue:** Three different status claims for the same number.
**Fix required:** Commit to one framing.

### P1A-M10 — Table III column "PTA γ (real-KDE)" inconsistent with Figure 1
**Location:** Table III, p. 16; Fig. 1, p. 4.
**Issue:** Figure 1 quotes the superseded γ = 3.20 ± 0.42. Table III column references the real-KDE column without quoting either value. The corresponding cells are unmotivated (matter bounce ✓, slow-roll ✗) without a number.
**Fix required:** Quote the actual numbers.

### P1A-M11 — Eq. (11) "(T_reh/M_GUT)^{3/2}" prefactor conceded to be aesthetic, not derived
**Location:** Sec. II C 1, p. 6, "Order-of-magnitude matching for Eq. (11)."
**Issue:** The 3/2 power is conceded to be "dimensional-analysis aesthetic at this level rather than calculated from a thermal partition function." Then Appendix B uses this prefactor to derive N_tot ≈ 92. The structural-tension argument at Sec. XIV D depends on N_tot. Either the prefactor is derived or N_tot ≈ 92 is not a derived quantity.
**Fix required:** Either derive the prefactor or label N_tot as an order-of-magnitude estimate everywhere it appears (including in the abstract and Fig. 1).

### P1A-M12 — Mass-dimension audit of Eq. (15): the author concedes the result is unstable
**Location:** Sec. IV B, p. 9.
**Issue:** Reproducing the calculation: (α_em/4π)(H_0/M_Pl)/[M_Pl(α/M)β_obs] with α_em/4π ≈ 5.8×10^{−4}, H_0/M_Pl ≈ 10^{−61}, M_Pl·(α/M) ≈ 10^{−2}, β_obs ≈ 6×10^{−3} gives ≈ 10^{−60}, consistent with the lower end of the quoted range. The upper end "10^{−58}" is not derivable from the quoted inputs. The author's own alternative ordering gives "∼ 10^{−33}." This is a 25-order-of-magnitude variability in a "no-go" amplitude bound.
**Fix required:** Pin down the calculation. Multiple orderings yielding 25 OOM differences is not a no-go.

### P1A-M13 — Eq. (10) and the "ρ_Λ = Ξ M_Pl^4" identification
**Location:** Sec. II C, p. 6; Appendix B, p. 19.
**Issue:** Eq. (10) writes Λ_eff = Ξ M_Pl^2 + c_ω ω². Appendix B then maps ρ_Λ = Ξ M_Pl^4 from the dimensionally-broken Eq. (B2). Then the paper notes "Either reading is a phenomenological dimensional assignment, not a derivation." The headline "Ξ ≈ 10^{−123}" depends on which reading. The "fine-tuning reduction from 10^{120} to 10^5" depends on which reading. The paper concedes this is "qualitative dimensional rearrangement rather than a quantitative bookkeeping result." A PRD paper cannot rest its central numerical claim on a self-acknowledged qualitative rearrangement.
**Fix required:** Either remove the numerical claim or place it under a "Phenomenology only" heading separate from the structural argument.

### P1A-M14 — DESI dataset combinations not specified
**Location:** Sec. I, p. 3; Sec. XIV D, p. 17.
**Issue:** "DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ (dataset-dependent)." Which combinations give which significance is not specified. The DESI numbers depend critically on which SN compilation is used (Pantheon+, Union3, DES-SN5YR).
**Fix required:** Specify the dataset combinations and the significance for each.

---

## MINOR findings

### P1A-N1 — Excessive "we emphasize" boilerplate
**Location:** Sec. II C ("We emphasize that Eq. 10 is..."), Sec. IV ("We emphasize that the four-route closure..."), Sec. XII A ("We emphasize that the..."), Appendix B ("We emphasize that the present treatment...").
**Issue:** Used as a hedging device, ~10 times.
**Fix required:** Remove most instances.

### P1A-N2 — γ_BI parameter table entry conflates "scheme spread" with "uncertainty"
**Location:** Table IV, "γ scheme range ∼0.020"; Sec. II A 1.
**Issue:** The author correctly notes this is scheme dependence, not a statistical uncertainty, but the table format reads as an error bar.
**Fix required:** Use a different column or footnote to indicate this is not a statistical uncertainty.

### P1A-N3 — γ_SU(2) ≈ 0.274 quoted to 3 sig figs but derived from black-hole entropy counting at ~ 1 sig fig
**Location:** Sec. II A 1, p. 5.
**Issue:** The DLM and ABCK counting schemes give different values (0.2375 vs 0.127 vs 0.274). Quoting "0.274" to three figures suggests precision the calculation does not have.
**Fix required:** Quote to fewer figures and cite the counting scheme inline.

### P1A-N4 — Abstract uses parenthetical to define "e^{32}"
**Location:** Abstract, p. 1.
**Issue:** Inline parenthetical "(the relative e-fold differential between bounce and CMB horizon-exit; comoving wavenumbers k are constant by definition and only physical scales scale with a^{−1} ∝ e^{−N})" is a textbook digression in the abstract.
**Fix required:** Move to body.

### P1A-N5 — Table I "Phen. assumption^a required" with non-Latin footnote arrangement
**Location:** Table I, p. 4.
**Issue:** Table I row 1 cites footnote *a*, which is not formatted as a footnote in the LaTeX source rendering; it appears as "Phen. assumption^a required" inline.
**Fix required:** Use \footnote{} or a clearly labelled note.

### P1A-N6 — "Eskilt & Komatsu" 3.6σ claim
**Location:** Abstract; Sec. IV D, p. 10; Sec. XII B, p. 16.
**Issue:** Verify the 3.6σ. Eskilt & Komatsu 2022 (arXiv:2205.13962) report β = 0.342° ± 0.094°, which is 3.64σ from zero — consistent. OK.

### P1A-N7 — Acknowledgment of AI assistance
**Location:** Acknowledgments, p. 18.
**Issue:** Disclosed appropriately. No fix required.

### P1A-N8 — Reference [44] arXiv:2603.13924
**Location:** Ref. [44].
**Issue:** arXiv identifier "2603.13924" — arXiv uses YYMM, so 2603 = March 2026. Paper is dated 2026, so this is a current/forthcoming entry. Acceptable but should be flagged as "to appear."
**Fix required:** Mark as "to appear" or verify the entry exists at the time of submission.

### P1A-N9 — Eq. (1) "T^{abc} T_{abc}" labelling
**Location:** Sec. II A 1, p. 5.
**Issue:** The author notes this is "a shorthand for the four-fermion contact interaction obtained after integrating out the non-propagating torsion; it is not an independently specified kinetic term." If it is shorthand, do not write it as a kinetic-style term in the action.
**Fix required:** Write the action with the contact term explicit, or use ψ̄γ^a γ^5 ψ-squared notation.

### P1A-N10 — Figure 2 caption double-prints "ρ_bounce ≈ 0.27 ρ_Pl"
**Location:** Fig. 2, p. 5.
**Issue:** Visual contains two labels for the bounce density; potentially redundant.
**Fix required:** Verify a single bounce label.

### P1A-N11 — "Companion" cross-references repeated ~10 times to the same Paper I(b)
**Location:** Throughout.
**Issue:** "in companion Paper I(b) [6]" appears at least 10 times; reads as a placeholder.
**Fix required:** Consolidate cross-references.

---

## Summary recommendation
**REJECT**

This paper does not meet the PRD bar on three independent grounds. First, the author acknowledges in Appendix B that the central operator (Eq. 6) has the wrong mass dimension and that the entire dark-energy mapping is a "phenomenological on-shell scaling ansatz, not a controlled EFT result"; the title and abstract claim a "channel-level closure" of dark-energy routes that the author concedes are dimensionally inconsistent. Second, the principal numerical inputs (H_0, σ_8, ΔN_eff, the NANOGrav posterior, the SPHEREx forecast, the galaxy-spin null) are sourced to five companion papers that are "in preparation" or "available upon request" and cannot be verified; Figure 1 displays an explicitly superseded PTA value (3.20 ± 0.42) that contradicts the body (2.567 ± 0.382). Third, the manuscript carries internal version-history language ("misstated in earlier drafts," "supersedes the earlier ... pre-real-KDE drafts"), patch paragraphs labelled "(supporting B14)," 25-order-of-magnitude ordering ambiguities self-acknowledged in the no-go amplitude bound (Eq. 15), and conceded misappropriated citations for the foundational Eqs. (14) and (16). The substantive physics (algebraic torsion vanishes for scalar matter; Holst reduces to Pontryagin; minimal ECH gives no late-time dark energy at the EFT level) is correct but is a textbook observation that does not warrant 21 pages, four "in preparation" companions, and the perturbation-transparency-theorem framing. Resubmission would require a complete rewrite at ≤ 8 pages with the dimensional inconsistency resolved or the dark-energy claim withdrawn, the companion-paper dependencies removed or posted, and all version-history language excised.

---

## PASS 2 — self-critique findings (what initial review missed)

# Additional Findings — Fresh-Eyes Pass on P1A

After a second pass focused on arithmetic, figure-body consistency, dimensional auditing, and cross-references, the following new findings emerge. Several are quantitatively serious.

---

## ESSENTIAL findings

### P1A-E10 — Figure 2 uses N = 55 e-folds, while body and Appendix B require N_tot ≈ 92
**Location:** Fig. 2 (p. 5) vs. Sec. II C 1 (p. 7), Sec. XII A (p. 15), Appendix B (p. 19).

**Issue:** Figure 2 explicitly labels the inflationary-dilution arrow "After inflationary dilution (N = 55 e-folds)" and shows the resulting dilution factor "× e^{−3N} (∼ 10^{−72})." However:
- Sec. II C 1: "Matching ρ_Λ ≈ (2.3 meV)^4 requires N_tot ≈ 92."
- Appendix B: "D_inf ∼ e^{−3N_tot} ∼ 10^{−122}, giving N_tot ≈ 122 ln 10/3 ≈ 94 e-folds."
- Sec. XII A: "Ξ ≈ 10^{−123} ... decomposed as 10^{−2} × D_inf with D_inf ∼ 10^{−121}."
- Sec. XIV D / Abstract: structural-tension argument is keyed to N_tot ≈ 92.

A dilution of 10^{−72} (N=55) is **50 orders of magnitude short** of the 10^{−121}–10^{−122} required by the body to recover the observed ρ_Λ. Figure 2 is the headline schematic of the dark-energy mechanism; it does not depict the mechanism the paper actually argues for. The reader cannot reconcile the schematic with the structural-tension claim that drives Sec. XIV D.

**Fix required:** Regenerate Fig. 2 with N_tot ≈ 92 (and verify the arrow shows 10^{−122}, not 10^{−72}), or remove the figure.

### P1A-E11 — Sec. III A misrepresents the observed birefringence value
**Location:** Sec. III A, p. 7.

**Issue:** "The parity-odd structure is qualitatively consistent with the observed isotropic birefringence at β ≈ 0.27°–0.30°." But the **observed** central values quoted elsewhere in the manuscript are β_obs = 0.342° ± 0.094° (Eskilt & Komatsu) and β = 0.215° ± 0.074° (ACT DR6). Neither is 0.27°–0.30°. The "0.27°" figure is the model's *fitted* prediction (Sec. II A 2). Sec. III A therefore presents the fitted prediction as if it were the observation, conflating model and data.

This is the same conflation Sec. XV's "9σ vs 0.73σ" paragraph is at pains to disentangle. Sec. III A undoes that disentanglement at the front of the observational signatures section.

**Fix required:** State the observed central values explicitly; quote the model-fitted value separately.

### P1A-E12 — Eq. (15) "factor-of-100 ambiguity" not derivable from the stated cause
**Location:** Sec. IV B, p. 9.

**Issue:** The Route-2 amplitude ratio is quoted as "∼ 10^{−58} to 10^{−60}" with the parenthetical "the factor-of-∼100 ambiguity reflects ε-correction perturbative-order scaling alone; the eV-vs-GeV unit conversion is exact." Recomputing from the stated inputs:
- α_em/(4π) = 5.8 × 10^{−4} (using α_em = 1/137); the author's quoted "≈ 5 × 10^{−4}" is only 16% lower.
- H_0/M_Pl ≈ 10^{−61}.
- M_Pl · (α/M) ≈ 10^{−2}.
- β_obs ≈ 6 × 10^{−3} rad.

Product: 5.8 × 10^{−4} · 10^{−61} / (10^{−2} · 6 × 10^{−3}) ≈ 10^{−60}.

The "10^{−58}" upper bound is **not derivable** from the stated inputs at any perturbative-order ambiguity; a 16% variation in α_em cannot produce a 100× spread. The author's own immediately following sentence — "An alternative ordering ... yields a numerically distinct ∼ 10^{−33} ratio" — concedes the real ambiguity is 27 OOM, not 2 OOM. The factor-of-100 framing is therefore not just unsupported but appears designed to obscure the 10^{−33}-vs-10^{−60} ordering instability the author already concedes one sentence later.

**Fix required:** Either justify the 10^{−58} upper bound from a calculation, or drop the "10^{−58} to 10^{−60}" range and quote only the value the calculation supports.

### P1A-E13 — Table IV: γ "scheme range ∼0.020" inconsistent with the actual scheme spread quoted in Sec. II A 1
**Location:** Table IV (p. 20) vs. Sec. II A 1 (p. 5).

**Issue:** Table IV row for γ reads "0.274 (scheme range ∼0.020)." But Sec. II A 1 lists three counting schemes:
- γ_U(1) ≈ 0.127 (Ashtekar–Baez–Corichi–Krasnov)
- γ_SU(2) ≈ 0.274 (Meissner)
- γ_DLM ≈ 0.2375 (Domagała–Lewandowski–Meissner)

The actual scheme spread is **0.147** (from 0.127 to 0.274), or **0.037** between DLM and SU(2), or **0.11** between DLM and U(1). The figure 0.020 corresponds to no pairwise comparison in the text. Sec. II A 1 itself states: "the ∼ 0.020 figure that appears in the parameter-budget table (Appendix B) is the spread between counting prescriptions, retained as an effective range only" — but no pairwise spread is 0.020. The table number does not exist in the calculation it is purported to summarize.

**Fix required:** Replace 0.020 with the actual scheme spread (0.127–0.274), or remove the column entirely as not statistically meaningful.

### P1A-E14 — "Cube of the fermion bilinear" dilution argument in Sec. II C 1 is incoherent
**Location:** Sec. II C 1, "Order-of-magnitude matching for Eq. (11)" paragraph, p. 6.

**Issue:** The paragraph justifies the exp[−3N_tot] dilution factor by claiming:
> "Fermion number density dilutes as a^{−3} under cosmological expansion ... and holds at the cubic axial-current operator level because the cube of the fermion bilinear scales as the cube of the fermion number density at the bounce-density regime where the algebraic relation is saturated."

This is dimensionally wrong. The torsion source is the axial bilinear ⟨ψ̄γ^[a γ^b γ^c] ψ⟩ ~ a^{−3} (single power of the bilinear). The torsion-induced four-fermion contact term (Hehl–Datta NJL) is L ~ G·(ψ̄γψ)² ~ a^{−6}. There is no "cubic axial-current operator" that scales as a^{−3} at the level of the action. If T ~ a^{−3} and the operator that controls the parity-odd action is linear in T, dilution is a^{−3}; if it is quadratic (e.g., T²), it is a^{−6}. The author conflates these by appealing to a "cube" that has no clear referent. The exp[−3N_tot] structure is then carried through Appendix B, the Sec. XII A reparametrization, and the Sec. XIV D structural tension on the strength of this incoherent argument.

**Fix required:** Specify which operator in the action is being diluted, identify its torsion-dependence (T, T², T³, etc.), and recompute the dilution factor accordingly. If the operator is quadratic, the exponent is −6, not −3, and the structural tension calculation changes by a factor of two.

### P1A-E15 — Table III "Quintom-B / w_0 w_a DESI / consistent†" is a model-class claim presented as a fit-quality entry
**Location:** Table III (p. 16) and its footnote †.

**Issue:** The Quintom-B row in the w_0 w_a DESI column reads "consistent†." Footnote † reveals: "Quintom-B can in principle accommodate the DESI w_0 w_a evidence; the MCMC analysis hosted in companion Paper I(b) was not extended to the w_0 w_a parameter space, so this row is reported as 'consistent at the model level' rather than a posterior-preference ✓." Other rows are labeled "not tested‡" because the author also did not test them. A "✓"-style entry for an untested model in a discriminator table is misleading — it gives Quintom-B credit for an empirical match the author admits was not measured. The asymmetric treatment of Quintom-B vs. the other "not tested‡" entries is a presentational bias.

**Fix required:** Mark Quintom-B as "not tested" like the other rows, or remove the w_0 w_a column.

---

## MAJOR findings

### P1A-M15 — Λ_eff (dim 2) and ρ_Λ (dim 4) used interchangeably
**Location:** Eq. (10), Sec. II C, p. 6 vs. Eq. (B2), p. 19.

**Issue:** Eq. (10) writes Λ_eff = Ξ M_Pl² + c_ω ω², where Λ_eff is the cosmological constant (mass-dim 2). Immediately afterward, Sec. II C states "The dark energy scale is set by Ξ ∼ 10^{−123}." Appendix B then identifies ρ_Λ = Ξ M_Pl^4 (mass-dim 4). The same dimensionless Ξ cannot be both the coefficient of M_Pl² in Λ and the coefficient of M_Pl^4 in ρ_Λ; these differ by a factor of M_Pl². The Sec. XII A formula "Ξ ≡ [(α/M) M_Pl] D_inf" with Ξ ≈ 10^{−123} matches the ρ_Λ identification, not the Λ_eff identification of Eq. (10). Either Eq. (10) is dimensionally wrong, or Ξ is being given two incompatible meanings.

**Fix required:** Pick a consistent dimensional convention and rewrite Eqs. (10) and (B2) with matching dimensions.

### P1A-M16 — D_inf and N_tot values inconsistent between Sec. XII A and Appendix B
**Location:** Sec. XII A (p. 15) vs. Appendix B (p. 19).

**Issue:** Sec. XII A: "Ξ ≈ 10^{−123}, decomposed as 10^{−2} × D_inf with D_inf ∼ 10^{−121}." Appendix B: "D_inf ∼ e^{−3N_tot} ∼ 10^{−122}, giving N_tot ≈ 122 ln 10/3 ≈ 94 e-folds." Recomputing: at N_tot = 92, D_inf = e^{−276} ≈ 10^{−119.9}, not 10^{−121}. At N_tot = 94, D_inf ≈ 10^{−122.5}. The "10^{−121}" of Sec. XII A and "10^{−122}" of Appendix B straddle N_tot ≈ 92–94, but neither matches the headline N_tot = 92 with internal consistency. The author flags this as "the ∼2% level offset" but does not reconcile it. The structural-tension argument in Sec. XIV D, which uses the e^{N_tot − N_exit} = e^{32} factor, inherits this 2-e-fold uncertainty.

**Fix required:** Reconcile the three numbers (N_tot, D_inf, Ξ) to a single internally consistent value, or quote N_tot = 93 ± 2 explicitly in the abstract and figures.

### P1A-M17 — App. B "(α/M) M_Pl^3 (dimension +2)" is presented as a "rewriting" of a dimension +4 expression
**Location:** Sec. IV intro, p. 8 ("Three technical aspects"); Appendix B, p. 19.

**Issue:** Sec. IV intro states that the dimensional accounting requires consistency "between (α/M) M_Pl^3 (dimension +2) and the equivalent rewriting [(α/M) M_Pl] M_Pl^4 (dimension +4)." But (α/M) M_Pl^3 has dimension [mass^{−1}][mass^3] = [mass^2], **not** equivalent to [(α/M) M_Pl] M_Pl^4 = [mass^4]. These two expressions differ by two powers of mass and cannot be related by "rewriting." The "internally consistent mass-dimension accounting" the author proposes is itself dimensionally inconsistent. This is a different and additional error from the +1-vs-+4 issue already flagged in P1A-E1.

**Fix required:** Drop the false equivalence or specify the missing M_Pl² factor.

### P1A-M18 — Reheating-thermal-reset argument confuses spin density with axial current
**Location:** Sec. II C 1, "Reheating thermal-reset barrier" paragraph, p. 7.

**Issue:** The argument claims that "torsion in minimal ECH ... tracks the instantaneous local fermion axial current density via the Cartan algebraic equation T^λ_μν ∝ S^λ_μν ∝ ⟨ψ̄γ^[λ γ^μ γ^ν] ψ⟩. Critically, this source is the axial current ⟨J^5_μ⟩, not the total fermion number density n_ψ." Then: "A thermal unpolarized fermion bath ... has ⟨J^5_μ⟩ → 0 in the mean."

This conflates the (totally antisymmetric) spin density tensor S^abc with the axial current J^5_μ. For a Dirac spinor, the antisymmetric S^abc and J^5_d are related by an ε contraction, so an unpolarized bath has ⟨S^abc⟩_T → 0 only in the **mean**, while ⟨S² ⟩_T is generically non-zero and quadratic in the bath density. The energy density entering Λ_eff comes from T·T-type contractions, not from ⟨T⟩ alone. The argument as written claims torsion is "instantaneously inherited" by a coherent-mean-zero configuration but does not address the fluctuation contribution ⟨T²⟩_T ~ n_ψ², which generically dominates the action. The thermodynamic erasure claim is therefore underderived.

**Fix required:** Compute ⟨T·T⟩_T at thermal equilibrium and show it does not contribute to the parity-odd vacuum energy at the required level, or withdraw the "parallel thermodynamic erasure channel" argument.

### P1A-M19 — Cross-reference error: Cartan equation cited as Eq. (13) instead of Eq. (3)
**Location:** Sec. II C 1, "Reheating thermal-reset barrier" paragraph, p. 7.

**Issue:** The paragraph states: "torsion in Einstein-Cartan-Holst is a non-propagating algebraic field whose value at any cosmological epoch is set by the fermion axial current density via the Cartan equation T^abc ∝ ψ̄γ^[a γ^b γ^c] ψ (Sec. IV A, Eq. 13)." But Eq. (13) is the Hehl–Datta four-fermion contact term L^NJL_tor = −(3/16)κ(ψ̄γ^a γ^5 ψ)², not the Cartan algebraic relation. The Cartan equation in this form appears as Eq. (3) in Sec. II A 2, T^abc = 8πG S^abc, with the bilinear definition S^abc = (1/4)ψ̄γ^[a γ^bc] ψ. The cross-reference is wrong.

**Fix required:** Replace with "(Sec. II A 2, Eq. 3)."

### P1A-M20 — Eq. (10) defines Λ_eff with c_ω ω² but Sec. II C immediately reports (ω/H_0) bound on cosmic rotation, no further use of c_ω
**Location:** Eq. (10), p. 6.

**Issue:** Eq. (10) introduces a second term c_ω ω² in Λ_eff, with c_ω undefined. The next sentence reports the (ω/H_0) bound and concludes "rotation completely negligible." c_ω never reappears. If the rotation term is negligible, it should not appear in the headline equation; if it is essential, c_ω must be defined and constrained. As written, c_ω is dead weight in the model action.

**Fix required:** Either define c_ω and use it, or drop the c_ω ω² term from Eq. (10).

### P1A-M21 — Table IV "Notes" column truncated in the rendered PDF
**Location:** Table IV, p. 20.

**Issue:** Two table cells are cut off mid-word in the rendered PDF:
- γ row: "LQG area spectrum (Eq. 2; scheme dependen" (missing "ce" or "ce; ...")
- γ_PTA row: "Bounce γ = 3.0 at +1.1" (missing "3σ above mean" or similar)

This is a typography/formatting failure of the parameter summary table, the primary reference for the paper's numerical claims.

**Fix required:** Rebuild the table with proper column widths.

---

## MINOR / NOTATIONAL findings

### P1A-N10 — Eq. (23) Pontryagin-density normalization is non-standard
**Location:** Sec. X D, Eq. (23), p. 14.

**Issue:** Eq. (23) writes R̃(Γ̊) = (1/2) ε^μνρσ R_μνρσ(Γ̊) = (1/2) *RR. The factor of 1/2 appears in both the definition of R̃ and the identification with *RR, which would imply *RR = ε^μνρσ R_μνρσ without the 1/2. Standard conventions (e.g., Misner–Thorne–Wheeler, or the Jackiw–Pi gravitational Chern–Simons literature) put the (1/2) in *RR = (1/2) R_μνρσ ε^μνρσ_κ^λ R^κλ — i.e., the dual contraction is on Riemann, not on Holst. The normalization in Eq. (23) is ambiguous and the reader cannot determine whether the proportionality is to *RR or to (1/2) *RR.

**Fix required:** Restore the standard Pontryagin normalization or specify the convention.

### P1A-N11 — Eq. (15) units issue in the parenthetical caveat
**Location:** Sec. IV B, p. 9.

**Issue:** The parenthetical "(A naive comparison of a rotation rate β̇ in eV against an angle uncertainty in eV would silently treat eV·s as dimensionless...)" reads as version-history commentary about an error in a previous draft. β̇ in natural units is [mass^1] = eV, an angle is dimensionless, so the comparison is *not* dimensional-incompatible in natural units. The parenthetical defends against an error that does not exist in the displayed equation, and should be removed.

**Fix required:** Remove the parenthetical.

### P1A-N12 — Abstract's "1σ band" claim for β ≈ 0.27° is correct but stated imprecisely
**Location:** Abstract, p. 1.

**Issue:** The abstract says β ≈ 0.27° "sits inside the WMAP+Planck 1σ band β_obs = 0.342° ± 0.094°." Computing: |0.342 − 0.27|/0.094 = 0.77σ, so 0.27° is at 0.77σ below the central value. This is "inside the 1σ band" in the sense that |0.77| < 1. Acceptable, but combined with Sec. XV's correctly computed 0.73σ vs. LiteBIRD, the abstract should quote the same separation explicitly so the reader knows the model prediction is on the lower edge of the 1σ band, not at the center.

**Fix required:** Add "(0.77σ below central)" for transparency.

### P1A-N13 — Sec. IV C "1/(12π²)" prefactor in Eq. (16) presented without derivation
**Location:** Sec. IV C, p. 9.

**Issue:** "The 1/(12π²) prefactor is the natural chiral-loop coefficient at this order." This is a hand-wave. The actual fermion-induced β-function for γ depends on representation, dimension of the chiral multiplet, and regularization scheme; the Benedetti–Speziale result the author cites does not give 1/(12π²) as the universal coefficient. The author concedes "we use Eq. (16) only as an upper-bound EFT ansatz." If it is an upper-bound ansatz, the prefactor should be max(natural coefficients) with justification, not "1/(12π²)" stated as natural.

**Fix required:** Cite the source of 1/(12π²) or replace with an explicit upper bound.

### P1A-N14 — γ_U(1) = ln 2/(π√3) arithmetic
**Location:** Sec. II A 1, p. 5. ✓ Verified: 0.693/5.441 = 0.1274. Correct.

### P1A-N15 — "fNL = −35/8 = −4.375" arithmetic in Table IV
**Location:** Table IV. ✓ Verified.

---

## Summary

The second pass uncovered six additional ESSENTIAL findings — including a 50-OOM mismatch between Figure 2 and the body's required dilution factor (P1A-E10), a misrepresentation of the observed birefringence value (P1A-E11), an unsupported factor-of-100 ambiguity claim in the Route-2 amplitude budget (P1A-E12), a fabricated scheme-spread number in Table IV (P1A-E13), an incoherent dilution-power argument (P1A-E14), and a misleading discriminator-table entry (P1A-E15) — plus seven MAJOR and five MINOR new findings. The dimensional accounting of the paper is internally inconsistent at multiple distinct levels (P1A-E1, P1A-M15, P1A-M17), and the central schematic Figure 2 does not depict the mechanism the paper actually argues for. The recommendation of REJECT is reinforced.