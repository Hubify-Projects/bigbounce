# P1A R10v3p1 — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (16349 chars)
**Wall time**: 487.7s

---

# Referee Report — P1A: "Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"

**Submitted to:** Physical Review D
**Reviewer stance:** Brutally honest. PRD is one of the most rigorous physics journals; the bar is high.

---

## Overall assessment

This paper presents itself as a "channel-level closure" of four enumerated minimal-ECH dark-energy routes, plus a "perturbation transparency theorem" for scalar matter. Strip away the heavy hedging language and what remains is:

1. A **well-known textbook observation** (Hehl–Datta 1971; Hehl et al. 1976): canonical scalar matter has no spin density, hence no torsion, hence the Holst term reduces to a boundary term. This is presented as a "central result" and "theorem" (Sec. X), but it is essentially trivial and has been known for ~50 years.

2. A **phenomenological scaling ansatz** (Eq. B2) that the authors themselves repeatedly admit is "not a derivation," is dimensionally wrong off-shell (+1 vs +4), and merely relocates the cosmological constant problem.

3. A **14-item barrier catalog** that mixes novel ECH-specific calculations with "known results" and "structural/philosophical observations" the authors explicitly admit are not new, and which they themselves admit contain a redundant entry (B8 ⊂ B14).

4. **Heavy reliance on companion papers "in preparation"** (refs [2], [6], [23], [46], [47]) for the actual MCMC, NaMaster, Fisher, and chirality results that underpin nearly every quantitative claim.

5. **Surviving "predictions" that the authors themselves repeatedly admit are NOT ECH predictions** — fNL = −35/8 is a matter-bounce-class result with "no ECH input" (per the abstract), and β ≈ 0.27° is a "benchmark consistency point, not an ECH prediction."

The paper is **honest to a fault** about its own limitations — every section contains paragraphs walking back the headline claim. After all the walk-backs, there is no clearly novel, defensible, quantitative ECH result. The structural conclusion reduces to: "minimal ECH with scalar matter behaves like GR; with fermions we make a dimensional-analysis ansatz that doesn't solve the CC problem." This is not a PRD-level contribution.

---

## ESSENTIAL findings

### P1A-E1 — The "central theorem" is textbook material misrepresented as novel
**Sec. X, p. 14.** The "perturbation-transparency theorem" reduces to: scalar matter has S=0 ⇒ T=0 ⇒ connection is Levi-Civita ⇒ Holst term becomes Pontryagin density (boundary). Steps 1–5 are immediate from Hehl et al. 1976 (cited as ref [12]). The Pontryagin-density observation for the Holst dual on a torsion-free connection is standard in any Holst/Nieh–Yan reference (e.g., the very Mercuri papers cited). The "extension to tensor sector" trivially follows because with T=0 the gravitational sector IS Einstein gravity. Labeling this a "central result" or "theorem" is overclaim. **Required fix:** Either demote to a remark stating the well-known reduction explicitly, OR demonstrate a non-trivial extension (propagating torsion, fermionic backgrounds, non-minimal couplings) and prove it as a theorem there. As written, this cannot anchor a PRD paper.

### P1A-E2 — Abstract makes claims the body retracts
**Abstract, p. 1.** Abstract states "each fails at the amplitude level under stated assumptions." Yet Sec. IV D (p. 10) **explicitly retracts** the Route 4 amplitude no-go: "R4 is therefore not closed by amplitude mismatch (as prior analyses claimed); it is closed by the observation that the same coupling that produces β_obs requires an ultralight-mass tuning m_θ ∼ H_0 ... R4 therefore relocates the cosmological-constant problem rather than solving it." This is a **naturalness objection**, not an amplitude closure. The abstract's claim that all four channels fail "at the amplitude level" is false on the authors' own showing. **Required fix:** Rewrite abstract to remove "amplitude level" universal claim. State accurately that 3 of 4 routes are closed at amplitude level and 1 (R4) is a naturalness objection.

### P1A-E3 — Dimensional inconsistency of the load-bearing operator
**Eq. (6), Eq. (B1), Appendix B, p. 19.** The parity-odd operator has off-shell dimension +1, three short of the required +4 for a local Lagrangian density. The authors openly admit "this operator, as written, is not a controlled dimension-+4 EFT operator" and that "ρΛ ∼ (α/M) M_Pl^5" (Eq. B2) is a "phenomenological on-shell scaling ansatz, not a controlled EFT result." A PRD paper cannot have its central operator be dimensionally inconsistent and acknowledged as such. The entire Ξ ∼ 10^−123 dark-energy mapping, Eq. (10), Eq. (24), depends on this. **Required fix:** Either provide a controlled dimension-+4 operator with the requisite M_Pl^3 prefactor and re-derive the closure, or remove all quantitative dark-energy mapping claims (Fig. 2, Eq. 10, the "Ntot ≈ 92" figure, the "10^120 → 10^5 reparameterization" discussion in Sec. XII A).

### P1A-E4 — "13 logically-independent" barrier count contradicted by the paper itself
**Abstract, Sec. IX, Table II, Sec. XV.** The paper repeatedly says "13 logically-independent" but lists 14 barriers, with the parenthetical "B8 is subsumed by B14." This is **redundancy as marketing**: the paper claims a 13-barrier closure and a 14-entry catalog interchangeably. Further, the authors classify Barriers 5, 6, 7, 9 as "Known results" (Sec. IX intro, p. 12) and Barrier 13 as "structural/philosophical." So of the 14 "barriers," **at most 8** are claimed novel (1, 2, 3, 4, 8, 10, 11, 12, 14 — of which 8 is subsumed by 14, giving 8 novel). The "13 logically-independent" framing is misleading. **Required fix:** State explicitly the count of novel ECH-specific barriers and stop oscillating between "13" and "14."

### P1A-E5 — Route 2 amplitude-budget calculation contains an admitted dimensional ambiguity
**Sec. IV B, p. 9, Eq. (15).** The text says: "an alternative ordering that contracts the H0 factor with the dimensionful coupling differently yields a numerically distinct ∼ 10^−33 ratio." A factor of **10^25** discrepancy depending on contraction ordering is not a controlled calculation. The further parenthetical "A naive comparison of a rotation rate β̇ in eV against an angle uncertainty in eV would silently treat eV·s as dimensionless" reveals the author has been struggling with dimensional bookkeeping. PRD does not accept "10^−58 to 10^−60 (the factor-of-∼100 ambiguity)" alongside "alternative ordering ... 10^−33" as a closure. **Required fix:** Perform a single dimensionally controlled calculation with all factors of ℏ, c, and M_Pl carried symbolically; quote one answer with one uncertainty.

### P1A-E6 — The "surviving" predictions are not predictions of this paper
**Abstract, Sec. XIII, Sec. XV.** Abstract states: "fNL = −35/8 is a property of the matter-bounce class [1], derived from the contraction-phase cubic action with no ECH input"; β ≈ 0.27° "is a benchmark consistency point, not an ECH prediction." Yet Table I lists fNL = −35/8 as the paper's "Testable prediction" answer to "Testable prediction?", and the conclusions and abstract repeatedly cite both as the "surviving" results. **This is the paper presenting non-results as results.** If neither prediction is derived from ECH, the paper has zero predictive content. **Required fix:** Remove fNL and β from any list of paper-specific predictions; relegate them to a "context" paragraph noting they are not derived here.

### P1A-E7 — MCMC, Fisher, NaMaster, and chirality results are all in unposted companion papers
**Throughout — refs [2], [6], [23], [46], [47] all "in preparation."** The cosmological parameters quoted (H0 = 67.68 ± 1.06, Δ_Neff = −0.020 ± 0.169, σ_8 = 0.803 ± 0.008, Ω_m = 0.308 ± 0.005, etc. in Table IV), the SPHEREx 3–5σ Fisher forecast, the NANOGrav γ = 2.567 ± 0.382 figure, and the galaxy chirality null are **all sourced to non-public papers** by the same author, marked "documented internally rather than as externally citable arXiv-posted numbers" (p. 5). PRD requires verifiable inputs. A paper cannot rest its quantitative scaffold on five simultaneously-unposted companion works by the same single author. **Required fix:** Either post the companion papers first (so they have arXiv IDs reviewable here) or remove all quantitative claims that depend on them.

### P1A-E8 — Self-citation of an inaccessible "companion technical note"
**Ref [47], p. 21.** "H. Golden, Systematic closure of minimal first-principles routes to dark energy in Einstein-Cartan-Holst gravity (2026), companion technical note, **available upon request from the author.**" This is the citation supporting "The parity assessment finds no photon coupling in the minimal framework" (Sec. XII B). An unposted note "available on request" is not a citable source in PRD. **Required fix:** Either post the technical note publicly or carry the argument in the main text.

### P1A-E9 — Sigma-level comparison errors with WMAP/Planck/ACT birefringence
**Abstract and Sec. III A, Sec. IV D, Sec. XII B.** The paper repeatedly cites β_obs = 0.342° ± 0.094° at "∼3.6σ from β=0." Recompute: 0.342/0.094 = 3.64σ. OK that's consistent. ACT DR6: 0.215/0.074 = 2.91σ. OK. But the abstract states the ECH prediction β ≈ 0.27° "sits inside the WMAP+Planck 1σ band." Check: |0.342 − 0.27|/0.094 = 0.77σ. OK consistent with "inside 1σ." However, the conclusion (p. 18) states LiteBIRD will detect non-zero β at "∼ 9σ (a 0.27°/0.03° overall sensitivity number)" then states the model-discrimination is "0.072°/0.0987° ≈ 0.73σ." Recompute: √(0.03² + 0.094²) = √(0.0009 + 0.008836) = √0.009736 ≈ 0.0987 ✓; 0.072/0.0987 ≈ 0.729 ✓. The arithmetic is right, but the juxtaposition of "∼9σ detection" alongside "0.73σ discrimination" without explicitly labeling them as referring to different null hypotheses at every appearance is exactly what the reviewer instructions flag as ESSENTIAL. The body partially does this in the conclusion, but Table III and the abstract do not. **Required fix:** Every appearance of "9σ" or "0.27°" sensitivity number must be flanked by "not directly comparable to discrimination against the WMAP+Planck central value."

### P1A-E10 — Internal audit / version-history language in the body
The body contains multiple internal-bookkeeping artifacts:
- p. 5: "Cosmological parameter values referenced in this paper ... should be read as internal-analysis inputs to the present structural argument rather than as independently peer-reviewable values until Paper I(b) is publicly posted."
- p. 15: "This figure supersedes the earlier synthetic-Gaussian-likelihood value γ = 3.20 ± 0.42 used in pre-real-KDE drafts; the migration is documented in Paper III § 6."
- p. 19: "(not the ∼ 35 misstated in earlier drafts: ..."
- p. 19: "we make that status explicit here so the reader is not misled by an apparent 'fix' in earlier drafts."
- p. 16 (Table III footnote ‡): extended internal status report on a running MCMC chain ("At the time of this writing the chain has accumulated ∼3.8×10^4 accepted samples ... R̂ − 1 ≈ 3×10^−2 ... we deliberately do not commit to a specific calendar date for convergence in this footnote").

PRD body text must not contain references to "earlier drafts," "pre-real-KDE drafts," "misstated," "apparent fix," or in-progress chain status. **Required fix:** Remove all such phrasing. The reader of the published version does not have access to earlier drafts and should not be reminded of them.

### P1A-E11 — Structural tension is internally contradictory
**Sec. XIV D, Sec. I (item 2), Sec. XIII.** The paper argues Ntot ≈ 92 e-folds are required for dark-energy suppression, but this would erase fNL = −35/8 at SPHEREx scales. Then the paper claims fNL = −35/8 as a "surviving prediction." This is logically contradictory **unless** the dark-energy mechanism is rejected — which the paper indeed argues. But then the fNL claim relies on the dark-energy mechanism being wrong. The paper handles this by saying fNL is "not an ECH prediction" — but then it's not a surviving prediction of the paper at all. The structural-tension argument either kills the framework's predictivity entirely or is misframed. **Required fix:** Pick one stance and state it once. Either (a) the dark-energy mechanism is dead, and so is fNL = −35/8 as an ECH signature, leaving the paper with zero predictions; or (b) the dark-energy mechanism survives in a specific regime where Ntot is small enough to preserve fNL, in which case derive that regime quantitatively.

### P1A-E12 — Mass-dimension reconciliation across Sec. IV intro is incoherent
**Sec. IV, p. 8.** The "(a)" technical aspect states: "the dimensional reconstruction of ρΛ^bounce in Appendix B requires an internally consistent mass-dimension accounting between (α/M) M_Pl^3 (dimension +2) and the equivalent rewriting [(α/M) M_Pl] M_Pl^4 (dimension +4); the choice of M_Pl^5 vs. M_Pl^3 controls the subsequent Ntot ≈ 92 bookkeeping." This admits the headline Ntot ≈ 92 number depends on an unresolved dimensional ambiguity. PRD cannot accept "M_Pl^3 vs M_Pl^5 controls Ntot" as a footnote. **Required fix:** Resolve the ambiguity in a single dimensional calculation; quote one Ntot value with its actual uncertainty.

### P1A-E13 — Paper length is excessive for the contribution
The paper is **21 pages** to communicate: (i) a textbook observation (Sec. X), (ii) a phenomenological scaling ansatz the authors disown (App. B), (iii) a catalog of barriers half of which they call "known," (iv) four channel closures, one of which they retract mid-paper. Stripped of internal-audit language, deferrals to companion papers, repeated walk-backs of the abstract, and the ~3 pages of caveat paragraphs about "stated assumptions," the actual content is **~6 pages**. **Required fix:** Compress to ≤10 pages or convert to a comment/short paper. PRD does not publish 21-page channel closures of a phenomenological framework with no derived prediction.

---

## MAJOR findings

### P1A-M1 — "Channel-level closure" vs. "operator-level theorem" disclaimer is repeated to the point of undermining the paper
The phrase "channel-level closure, not operator-level theorem" or close variants appears in the title, abstract (twice), Sec. I (three times), Sec. IV ("Scope"), Sec. IX, Sec. XIV E, and conclusion. This level of caveat self-undermining is unusual and suggests the authors know the claim is fragile. **Fix:** State the scope once in the introduction and once in the conclusion; remove the other ~6 repetitions.

### P1A-M2 — Table I "Testable prediction" row is misleading
**Table I, p. 4.** Lists fNL = −35/8 as "Yes, class-level" — but footnote c admits "not fully mechanism-independent across the bouncing-cosmology landscape; not a distinctive ECH prediction." A "Yes" with a footnote saying "actually no, not a distinctive prediction" is a misleading executive summary. **Fix:** Change the cell to "Not derived from ECH; matter-bounce-class observable."

### P1A-M3 — Eq. (11) order-of-magnitude matching of (Treh/MGUT)^{3/2} is hand-waving
**Sec. II C 1, p. 6–7.** The half-integer power is justified as "dimensional analysis aesthetic at this level rather than calculated from a thermal partition function" — the authors literally call it "aesthetic." A PRD paper cannot use a controlling exponent that the authors describe as aesthetic without derivation. **Fix:** Either derive it from a phase-space integral or drop the (Treh/MGUT)^{3/2} prefactor and absorb it into Ntot's uncertainty.

### P1A-M4 — Fig. 1 caption claims dashed-box "channel-level closure"
**Fig. 1 caption, p. 4.** "ECH appears bordered with a dashed box marked channel-level closure under stated assumptions (this paper)—the 14-constraint catalog narrows the four enumerated minimal-ECH dark-energy channels to zero phenomenologically free pathways within those channels." Verify: looking at the rendered figure, the ECH/torsion box is in red (not clearly dashed in the description); the legend says "structurally closed (this paper)." Several "outside-ECH route" arrows are drawn, but the figure does not clearly show closure. **Fix:** Either redraw with clear visual distinction between "closed" and "outside-route" or remove the figure.

### P1A-M5 — Fig. 2 illustrates an ansatz the body admits is wrong
**Fig. 2 caption, p. 5.** "Energy density hierarchy from the Planck scale to the observed dark energy scale, illustrating the phenomenological scaling ansatz ρvac ∼ [(α/M) M_Pl] M_Pl^4. This ansatz is dimensionally correct on-shell at the bounce but is not derived from the ECH action." A figure illustrating an admittedly-non-derived ansatz, with the famous 10^−122 hierarchy on display as if explained, is figure-as-illustration, not figure-as-evidence. **Fix:** Remove the figure or relabel as a heuristic schematic with no quantitative content.

### P1A-M6 — Table II repeats author's own admitted classification problem
**Table II, p. 13.** Lists 14 barriers, with header note that B8 ⊂ B14 and "should not be counted as logically independent." Including a row that the table caption disowns is poor scientific presentation. **Fix:** Either drop B8 or keep both and stop claiming "13 logically-independent."

### P1A-M7 — Table III "consistent†" vs "not tested‡" footnotes describe an in-progress chain
**Table III, p. 16.** The Quintom-B row marked "consistent†" with a footnote admitting "the MCMC analysis hosted in companion Paper I(b) was not extended to the w0wa parameter space." The "not tested‡" footnote is a 12-line in-progress chain status. **A table in a PRD paper should not contain "running chain" status reports.** **Fix:** Either run the chains to convergence before submission and report results, or remove the table.

### P1A-M8 — Route 1 "parity-even" claim is correct but the rebuttal of "parity-odd component by component" is confused
**Sec. IV intro (c), p. 8.** "the axial-vector current ψ̄γ^a γ^5 ψ is a pseudovector (parity-odd component by component), but the Lorentz contraction of two such pseudovectors gives a scalar that is parity-even (each component's parity-odd factor squared is +1)." This is **wrong reasoning**, even though the conclusion is right. The parity of a Lorentz scalar built from two pseudovectors is +1 because the contraction is over a Lorentz index, not because "each component's parity-odd factor squared is +1" (parity is a discrete spacetime symmetry, not a per-component sign). The author appears to be confusing parity of the vector field components under P with the parity of the contracted scalar. **Fix:** Rewrite this aside correctly: J^μ_5 J_{5μ} is parity-even because under parity J_5^0 → −J_5^0 and J_5^i → +J_5^i (axial vector), and the Lorentz invariant J_5^μ J_{5μ} = (J_5^0)² − |J⃗_5|² is invariant under P, giving the same scalar with no sign change.

### P1A-M9 — "Reheating thermal-reset barrier" introduces a new physical argument labeled "supporting B14"
**Sec. II C 1, p. 7.** The "reheating thermal-reset barrier" is a substantial new physical argument about C/P-equilibration of the axial current. It is presented inline in a section on Eq. (11) and labeled "supporting B14," but it is a distinct mechanism — arguably Barrier 15. The placement (inside a derivation paragraph for the suppression factor) and labeling are confused. **Fix:** Either promote this to a named barrier with its own section, or remove. The argument also assumes ⟨J^5_μ⟩_T → 0 in C/P-equilibrium thermal bath — but in the Standard Model the electroweak sector violates C and P; the argument needs justification.

### P1A-M10 — Eq. (12) cosmic birefringence formula misses a normalization
**Eq. (12), p. 7.** C_ℓ^EB ≈ 2β(C_ℓ^EE − C_ℓ^BB). The standard small-β result is C_ℓ^EB = (1/2) sin(4β)(C_ℓ^EE − C_ℓ^BB) ≈ 2β(C_ℓ^EE − C_ℓ^BB) for β in radians. The equation is dimensionally OK if β is in radians, but the paper repeatedly quotes β in degrees. **Fix:** Specify units. State β is in radians in Eq. (12) and convert when comparing to 0.342°.

### P1A-M11 — Ntot ≈ 92 vs Ntot ≈ 94 discrepancy is unresolved
**App. B, p. 19.** Two derivations give 92 and 94 e-folds; the paper says the offset is "∼ 2% level." Then: "the small offset reflects that the structural tension uses Eq. (B2) as the input ansatz, while the genuine M_Pl^4-to-ρ_Λ^obs hierarchy uses the unrescaled Planck density." So **the two are using different ansätze and disagree by 2 e-folds**, yet both are quoted in the main text without clear indication of which is "the" number. **Fix:** Pick one, derive it, state it, and use it consistently. Drop the other.

### P1A-M12 — "Acknowledgments" section discloses Claude AI use but companion papers may have undisclosed AI assistance
**Acknowledgments, p. 18.** "The author acknowledges the use of Claude (Anthropic) as an AI research assistant during systematic barrier-cataloging, perturbation-gate verification, and manuscript preparation. All scientific claims, derivations, numerical results, and bibliographic attributions were independently verified by the author." The disclosure is appropriate. However, PRD policy requires AI assistance be disclosed; verify the companion papers also disclose this. **Fix:** No fix to this paper; verify companion papers comply.

### P1A-M13 — Sec. VIII "Related Work" is thin and mis-attributes recent papers
**Sec. VIII, p. 12.** "Recent independent support includes Liu et al. [41] (EC torsion fits the S8 tension), Legner et al. [42] (torsion condensation), and Alam et al. [43] (non-singular bounces in modified gravity)." These are recent 2025 preprints; calling them "independent support" without engagement is name-dropping. Liu et al. address S8 not the cosmological constant; Legner et al. address H0 not DE in the ECH framework analyzed here. **Fix:** Either engage substantively or remove.

### P1A-M14 — γ_PTA "real-KDE" reanalysis is sourced to unposted Paper III
**Sec. X G, p. 15; Table III; Table IV.** The number γ = 2.567 ± 0.382 with "+1.13σ above the posterior mean" for the matter-bounce prediction γ = 3.0 — recompute: (3.0 − 2.567)/0.382 = 1.13 ✓ arithmetic correct. But the entire analysis is in unposted Paper III [46]. PRD cannot accept a sigma value from a non-public companion. **Fix:** Post Paper III first or remove this comparison.

### P1A-M15 — Figure 2 quotes ρ_vac ∼ (α/M) M_Pl^5
**Fig. 2, p. 5.** Caption: "ρ_vac ∼ [(α/M) M_Pl] M_Pl^4." Body says (α/M) M_Pl^5 ∼ 10^−2 M_Pl^4 (Eq. B2). These are consistent only if (α/M) M_Pl ∼ 10^−2, i.e., α/M ∼ 10^−2 / M_Pl ∼ 10^−21 GeV^{−1}. OK consistent. But the figure displays "ρ_vac ∼ (α/M) M_Pl^5" prominently, which has dimension M_Pl^5 — wrong by one mass dimension if α/M has dim −1. **Fix:** Check figure dimensions carefully.

---

## MINOR findings

### P1A-Mi1 — Inconsistent dataset MCMC sample counts
p. 5: "309,189 frozen accepted samples ... 176,240 full-tension + 132,949 Planck+BAO+SN." Sum: 176,240 + 132,949 = 309,189 ✓.

### P1A-Mi2 — "∼ 92 e-folds" in abstract vs "Ntot ≈ 92" body vs "Ntot ≈ 94" App. B
See M11. Abstract should match App. B's controlled estimate or state the uncertainty.

### P1A-Mi3 — Sec. IV A: κ = 8πG vs κ = 1/M_Pl^2
**p. 9.** Text uses both "κ = 8πG" and "κ = 1/M_Pl^2." With M_Pl^{reduced} = (8πG)^{−1/2}, these are equivalent up to convention. **Fix:** State convention explicitly.

### P1A-Mi4 — Eq. (15) numerical evaluation
α_em/(4π) ≈ 5.8×10^{−4}; H0/M_Pl ≈ 10^{−61}; M_Pl·(α/M) ≈ 10^{−2}; β_obs ≈ 6×10^{−3} rad. Plug in: 5.8×10^{−4} · 10^{−61} / (10^{−2} · 6×10^{−3}) = 5.8×10^{−65} / 6×10^{−5} ≈ 10^{−60}. The paper says "10^{−58} to 10^{−60}." Lower bound recomputes as ~10^{−60}; upper bound 10^{−58} would need αem/(4π) ≈ 1, not justified. **Fix:** State a single value 10^{−60} with no spurious upper bound.

### P1A-Mi5 — Sec. IV D claim that mθ ∼ H0 gives ρθ = ρΛ
Recompute: ρ_θ = m_θ² β² / [2(α/M)²]; m_θ = H_0 = 1.5×10^{−33} eV; β = 6×10^{−3} rad; α/M = 10^{−21} GeV^{−1} = 10^{−30} eV^{−1}.
ρ_θ = (1.5×10^{−33})² · (6×10^{−3})² / [2·(10^{−30})²]
    = 2.25×10^{−66} · 3.6×10^{−5} / 2×10^{−60}
    = 8.1×10^{−71} / 2×10^{−60}
    = 4×10^{−11} eV⁴ ≈ ρ_Λ (≈ 2.8×10^{−11} eV⁴)
Paper says "≈ 2.8×10^{−11} eV⁴." Within a factor of ~2 ✓. Marginally OK; clarify.

### P1A-Mi6 — Eq. (20) GW ceiling
Ω_GW^bounce ≲ (ρcrit/ρPl)² ≈ 0.07–0.17.
(0.27)² = 0.0729; (0.41)² = 0.168. ✓ arithmetic correct. The window 0.07–0.17 is fine but enormous — it allows up to ~17% of bounce energy in GW, which would severely impact BBN. The text doesn't engage with this. **Fix:** Add the actual BBN constraint and note whether the ceiling saturates it.

### P1A-Mi7 — Acknowledgement of Shamir
"We acknowledge Lior Shamir for providing aggregate CW/CCW galaxy spin counts for the A(z) comparison." But the body says the galaxy spin null refutes Shamir's claims. Confirm the acknowledgement is appropriate; it appears to be acknowledging data sharing despite scientific disagreement, which is fine.

### P1A-Mi8 — Reference [44] arXiv ID
"arXiv:2603.13924" — arXiv IDs starting "2603" do not exist (yet); arXiv IDs go YYMM.NNNNN. **Fix:** Verify ID; likely typo for 2503 or 2403.

### P1A-Mi9 — Inconsistent citation style for Eskilt & Komatsu
Sometimes "[4]," sometimes named "Eskilt & Komatsu [4]," sometimes "WMAP+Planck Eskilt & Komatsu measurement." **Fix:** Pick one style.

### P1A-Mi10 — Footnote 1 (p. 11) on fNL forecast
Lists σ(fNL) ≈ 0.7 Fisher-ideal and σ(fNL) ≈ 1.0 with systematics, gives 6.25σ → 5–5.5σ → 3–5σ degradation chain. The degradation factors (r ≈ 0.84 template overlap, GR-projection, photo-z) compound multiplicatively. Compute: 4.375 / 1.0 = 4.4σ; with r=0.84 → 3.7σ. So 3–5σ is plausible if generous. Mark as OK.

### P1A-Mi11 — Sec. II A 2 Eq. (7)
"α/M ∼ (g²/32π²)(γ/M) ln(Λ_UV²/μ²) + δ_NY"
This expression has α/M on the left (mass dim −1) and γ/M on the right (mass dim −1) ✓. But the coefficient g²/32π² is α_g/(2π) for a U(1)-like coupling. Origin not specified ("g" undefined). **Fix:** Define g.

### P1A-Mi12 — "Equation 10" or "Eq. (10)" inconsistency
Sec. II C 1, p. 6: "the parity-odd operator in Eq. (10) has mass dimension +1 (Sec. II C)." But Eq. (10) is the ρ_Λ parameterization, not the parity-odd operator. The parity-odd operator is Eq. (6). **Fix:** Correct citation.

### P1A-Mi13 — Table IV "Notes" column truncated
**Table IV, p. 20.** Notes appear truncated at the right edge (e.g., "scheme dependen", "Bounce γ = 3.0 at +1.1"). **Fix:** Reformat to fit page width.

### P1A-Mi14 — Sec. VII falsification criterion (3)
"(3) MCMC parameter values (H0, σ8, ΔNeff) are already consistent with standard ΛCDM, constraining the framework rather than falsifying it." Consistency with ΛCDM does not constrain a framework that recovers ΛCDM as a limit; it provides null information. **Fix:** Rephrase.

### P1A-Mi15 — Saadeh et al. citation [21] for (ω/H)0
"CMB isotropy bounds give (ω/H)0 < 5 × 10^{−11}." Saadeh et al. 2016 set bounds on anisotropy; the specific rotation bound 5×10^{−11} should be cross-checked.

### P1A-Mi16 — Sec. III A "qualitatively consistent with the observed isotropic birefringence at β ≈ 0.27° – 0.30°"
The Eskilt & Komatsu 2022 central value is 0.342°. Where does 0.27°–0.30° come from? Earlier Minami & Komatsu reported ∼0.35°; subsequent refinements landed at 0.342°. The "0.27°" appears to be the **spectator-ALP-fitted** value, not the observed value. The phrasing "observed isotropic birefringence at β ≈ 0.27°–0.30°" is misleading. **Fix:** Distinguish observed (0.342°±0.094°) from fitted-spectator-ALP-benchmark (0.27°).

---

## NITs

### P1A-N1 — "Diego-Palazuelos & Komatsu [5]"
Confirm citation. ACT DR6 birefringence paper authorship has many authors; check whether "& Komatsu" is the appropriate short citation.

### P1A-N2 — "loop quantum cosmology" capitalization
Sometimes "Loop Quantum Cosmology" (capitalized), sometimes "loop quantum cosmology." Standardize.

### P1A-N3 — Eq. (16) "schematically motivated"
"Schematically motivated by their construction, we adopt the one-loop running ansatz..." then "we use Eq. (16) only as an upper-bound EFT ansatz." Multiple disclaimers per equation reduce confidence.

### P1A-N4 — Use of "PDT" timezone in date
"Dated: June 2, 2026 PDT" — PRD does not require timezone on date.

### P1A-N5 — "(Sec. IX; 14 historical catalog entries, of which B8 is subsumed by B14 per the perturbation-transparency result)"
Long parentheticals in abstract reduce readability. Restructure.

### P1A-N6 — Footnote on Quintom-B chain in Table III caption
12-line footnote in a caption is excessive.

### P1A-N7 — "RunPod H200 and H100 instances" in Acknowledgments
Hardware vendor in acknowledgments is unusual. Optional removal.

---

## Summary recommendation

**REJECT**

This paper does not meet the PRD threshold. The "central theorem" (Sec. X) is a textbook reduction known since Hehl–Datta 1971; the dark-energy mapping rests on a dimensionally inconsistent operator (off-shell dim +1 vs +4) that the authors openly call an unjustified ansatz; the abstract claim of "amplitude-level closure" is contradicted by Sec. IV D, which the authors themselves retract to a "naturalness objection"; the two "surviving predictions" (fNL = −35/8 and β ≈ 0.27°) are explicitly disowned by the authors as non-ECH results; ~5 load-bearing companion papers are unposted "in preparation," with one cited "available upon request"; the body contains version-history language ("supersedes earlier draft," "pre-real-KDE drafts," "misstated in earlier drafts," in-progress chain status in a table footnote) inappropriate for a published paper; the headline "13 logically-independent constraints" oscillates with "14 historical entries" and explicitly admits one is redundant; and the paper is 21 pages for what is essentially a phenomenological no-go assembled around a 50-year-old observation, with no derived prediction and no new positive content. To be reconsidered, the authors must (i) post the companion papers so their numerical claims are verifiable, (ii) eliminate the dimensional inconsistency in the load-bearing operator or remove all quantitative dark-energy claims, (iii) compress the paper to ≤10 pages, (iv) remove all version-history and internal-audit language, (v) align the abstract with what the body actually proves, and (vi) state clearly that the paper derives no original predictions of its own.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report — Second-Pass Findings

**Reviewer stance:** Fresh-eyes re-examination of P1A, focusing on arithmetic, dimensional consistency, figure-body matches, and technical correctness that the first pass may have under-scrutinized.

---

## ESSENTIAL findings (new)

### P1A-E14 — The "central theorem" reduces Holst to the wrong object
**Sec. X B Step 4 (p. 14); Eq. (23); Abstract; Conclusions.** The paper repeatedly claims that the Holst term on a torsion-free Levi-Civita connection "reduces … to the Pontryagin density ∝ RR̃ — generically non-zero pointwise but a total derivative." This is **technically incorrect**.

- The Holst-dual contraction ε^{μνρσ}R_{μνρσ} is **linear** in R.
- The Pontryagin (Chern–Pontryagin) density is *R·R = (1/2)ε^{μνρσ}R^{αβ}_{μν}R_{αβρσ}, which is **quadratic** in R.
- On a torsion-free connection, ε^{μνρσ}R_{μνρσ} = 0 **identically** (by the first Bianchi identity R^{a}_{[bcd]} = 0), not a non-zero total derivative.

The Holst term on Levi-Civita is **identically zero in vacuum** (this is the standard textbook result that motivates calling Holst "topological" only in the presence of torsion, via Nieh–Yan). Saying "generically non-zero pointwise but a total derivative" misrepresents both the algebraic structure and the standard literature (Mercuri [19], Holst [25]) that the paper cites.

The conclusion (Holst contributes nothing to EOM with scalar matter) is **right by a different mechanism** (Holst is zero, not a non-zero boundary term), so the perturbation-transparency observation survives — but Eq. (23), Sec. X B Step 4, and the abstract's headline phrasing about the Pontryagin density and pointwise-nonzero total derivatives are all incorrect. **Required fix:** Replace the Pontryagin-density claim throughout (abstract, Sec. X B Step 4, Eq. 23, Sec. X D, Conclusions) with the correct statement: "On a torsion-free connection, the Holst term vanishes identically by the first Bianchi identity." This also undermines the rhetorical force of E1 in a new way: the "theorem" doesn't even need a topological / boundary-term argument; it's just zero.

### P1A-E15 — Arithmetic error: ACT vs WMAP+Planck consistency
**Sec. IV D, p. 10.** Paper states the ACT DR6 value β = 0.215° ± 0.074° is "consistent within ∼ 1.4σ" with WMAP+Planck β = 0.342° ± 0.094°. Recompute the proper two-measurement tension:

|0.342 − 0.215| / √(0.094² + 0.074²) = 0.127 / √(0.008836 + 0.005476) = 0.127 / 0.1197 = **1.06σ**

The "1.4σ" figure is what you get from dividing by only the WMAP+Planck uncertainty (0.127/0.094 ≈ 1.35σ), which is the wrong methodology for testing consistency of two independent measurements. **Required fix:** Change "1.4σ" → "1.06σ" with √(σ₁² + σ₂²) combination, or state explicitly that the comparison uses only the WMAP+Planck uncertainty (in which case explain why).

### P1A-E16 — Figure 2 internally inconsistent with body text
**Fig. 2 (p. 5).** The figure shows a suppression factor "×e^{−3N} (∼10^{−72})" labeled at "After inflationary dilution (N = 55 e-folds)." Recompute: e^{−3·55} = e^{−165} ≈ 10^{−71.7} ≈ 10^{−72} ✓ — the figure's internal arithmetic is right.

**But the body text (Sec. II C 1, Sec. XII A, Sec. XIV D, App. B) consistently uses Ntot ≈ 92 e-folds with Dinf ∼ 10^{−121}.** The figure depicts N = 55 (the standard slow-roll number) with Dinf ∼ 10^{−72}, neither of which appears anywhere else in the paper. There is no caption note explaining why the figure uses different numerical values from the body. The reader is left unable to reconcile the figure with the entire dimensional argument of Sec. II C, Sec. XII A, and Appendix B. **Required fix:** Either redo Fig. 2 with N = 92, Dinf = 10^{−121} to match the body, or add an explicit caption sentence stating that N = 55 is shown to illustrate the *insufficiency* of standard inflationary e-folds and that the body's N ≈ 92 is the matching value. As drawn the figure contradicts the paper's own numerical scaffolding.

### P1A-E17 — Cosmological-constant hierarchy quoted with three inconsistent values
The famous CC hierarchy appears as:
- **10^{122}** in Appendix B ("hierarchy is M_Pl^4/ρobs ∼ 10^{122}")
- **10^{120}** in Sec. XII A ("the fine-tuning reduction from 10^{120} to 10^5")
- **10^{123}** implicit in Ξ ∼ 10^{−123} (Sec. II C, Sec. XII A) and the App. B Ntot derivation gives 122 ln10/3 ≈ 94 e-folds vs. the body's 92.

Recompute: M_Pl = 1.22×10^{28} eV, M_Pl^4 ≈ 2.2×10^{112} eV^4. ρobs = (2.3 meV)^4 = 2.8×10^{−11} eV^4. Ratio = 0.79×10^{123} ≈ **10^{123}**. The correct universal number is 123, not 120 or 122. The paper switches between three values within a 21-page document. **Required fix:** Adopt one value consistently (10^{123} is the most accurate; 10^{120} appears to be a stale legacy number) and re-derive Ntot from that value. The current text yields Ntot ≈ 92 from "10^{121}" (Dinf), ≈ 94 from "10^{122}" (App. B), and an unstated value from "10^{120}" (Sec. XII A); pick one.

### P1A-E18 — "Foundations A–G" and "Branches H, J, L, M, N, O" are uncited and undefined
**Abstract, Sec. I, Sec. IX, Sec. XV.** The paper invokes "7 foundation studies (Foundations A–G)" and "6 observational research branches (Branches H, J, L, M, N, O)" as the source of the 14-barrier catalog (which is itself the load-bearing structural claim of the paper). No reference is given for any of these 13 "studies" / "branches." They do not appear to be sections of this paper (which has sections numbered I–XV), nor are they cited as published works, internal technical notes, or even the companion papers [2, 6, 23, 46, 47]. The reader cannot find what these "studies" are. **Required fix:** Either provide explicit citations / labels mapping "Foundation A" through "Branch O" to specific sections, internal documents, or published references — or remove the framing and present the 14 barriers as authored claims of this paper alone. As currently written this is unverifiable citation by acronym.

### P1A-E19 — Template-overlap σ(fNL) arithmetic uses the wrong formula
**Sec. VII footnote 1 (p. 11).** Paper states: σ(fNL) ≈ 0.7 Fisher-ideal, |fNL|/σ = 4.375/0.7 ≈ 6.25σ, "degraded to ∼5–5.5σ optimistic after template-overlap correction r ≈ 0.84 between the matter-bounce shape and the local/equilateral basis." Implicit arithmetic: 6.25 × 0.84 ≈ 5.25σ.

This is the wrong formula for a template-overlap correction. For a Fisher matrix with correlation r between two template parameters, the marginalized uncertainty scales as σ_marg = σ_ideal / √(1 − r²). Equivalently, the marginalized S/N when fitting the matter-bounce amplitude in the presence of a degenerate local-template direction is:

S/N_marg = S/N_ideal × √(1 − r²) = 6.25 × √(1 − 0.7056) = 6.25 × 0.543 = **3.39σ**

not 5.25σ. The correct degraded ideal-Fisher S/N is ∼3.4σ, which after the further GR-projection / bϕ / photo-z systematics quoted in Sec. VI would degrade further (perhaps to ∼2–2.5σ realistic), not the "3–5σ realistic" advertised. **Required fix:** Redo the template-overlap arithmetic using √(1 − r²), update the headline "3–5σ" forecast, and update Table I, Sec. VII, Sec. XIII, and Sec. XV accordingly. If the original formula has a justification (e.g., r is being used as a different quantity), that justification must be stated explicitly.

---

## MAJOR findings (new)

### P1A-M11 — "A_0" galaxy-spin amplitude undefined
**Sec. III B, Sec. XIV A 2, Sec. XIV B.** The quantity "A_0" is invoked three times as the amplitude the framework "underpredicts by > 100 orders of magnitude," but it is never defined in the main text. The reader cannot evaluate the claim. (Presumably it is the dipole amplitude of the CW-fraction sphere harmonic, but this is buried in companion Paper IV [23].) **Fix:** Define A_0 at first use, or remove the quantitative "100 orders of magnitude" claim and replace with a qualitative statement.

### P1A-M12 — Eq. (18) dimensional consistency unclear
**Eq. (18), Sec. IX A.** g_eff ∼ 1/(M_Pl √|t_3|) ∼ H_0/M_Pl ∼ 10^{−61}. If g_eff is dimensionless (which would make it "coupling-like" and the 10^{−61} numerical value meaningful), then 1/(M_Pl √|t_3|) requires |t_3| to have dimension M^{−2}, i.e. t_3 is a coupling with dim M^{−2}. This is plausible for a PGT parameter, but the paper never states the dimension or definition of t_3. Without that, the equation cannot be verified. **Fix:** Define t_3 and state its dimension; alternatively cite the specific PGT reference where this combination is standard.

### P1A-M13 — "Reheating thermal-reset barrier" assumes C/P-equilibrium in a C/P-violating Standard Model
**Sec. II C 1 (p. 7), "Reheating thermal-reset barrier" paragraph.** The argument that ⟨J^5_μ⟩_T → 0 in a thermal bath rests on "approximate C/P-equilibrium," but the electroweak Standard Model violates both C and P maximally; weak processes do not equilibrate axial charges in the way the argument implicitly requires. The author handwaves "C/P-violating scattering rates that randomize axial polarization exceed the Hubble rate at T ∼ T_reh," which is the opposite of equilibrium — it's chirality-flipping rates that thermalize axial charge to zero through *strong* parity-violating dynamics, which is only true if Yukawa rates dominate over weak rates at the reheating temperature. This is not obvious and depends on the reheating model. **Fix:** Either provide a quantitative comparison of axial-equilibration vs. Hubble rates at T_reh, or weaken the claim to "may be erased depending on the reheating model."

### P1A-M14 — Table I footnote 'b' depends on retracted Fisher arithmetic
**Table I footnote b.** "3–5σ realistic after full systematic budget (GR-projection, bϕ uncertainty, photo-z degradation) under Heinrich+2024 σ(fNL)≈0.7." This forecast is the headline "Yes, class-level" testable prediction. Per E19, the underlying arithmetic appears wrong; correcting it gives ≲ 3.4σ ideal and ≲ 2.5σ realistic. **Fix:** Coupled to E19. The "3–5σ" cell in Table I and the "Yes" testable-prediction status need to be revised.

### P1A-M15 — Eq. (12) cosmic birefringence formula assumes small β, not stated
**Eq. (12), p. 7.** C_ℓ^EB ≈ 2β(C_ℓ^EE − C_ℓ^BB) is the small-β expansion of C_ℓ^EB = (1/2)sin(4β)(C_ℓ^EE − C_ℓ^BB). β here is in radians (β = 0.27° = 4.7×10^{−3} rad), so the small-β approximation is fine, but the paper repeatedly quotes β in degrees throughout and never specifies units in Eq. (12). **Fix:** State β is in radians at Eq. (12), or use sin(4β) explicitly.

---

## minor findings (new)

### P1A-m1 — Table IV "scheme range ∼0.020" is misleading
**Table IV.** γ "(scheme range ∼0.020)" — but the scheme range goes from 0.127 (U(1)) to 0.2375 (DLM) to 0.274 (SU(2)), a spread of ~0.15, not 0.020. The 0.020 figure refers only to the DLM–SU(2) sub-spread. **Fix:** State the full counting-scheme spread or specify which sub-range "0.020" refers to.

### P1A-m2 — Page 4 Fig. 1 lists 6 bounce mechanisms but only 5 are tabulated in Table III
**Fig. 1 (p. 4) vs Table III (p. 16).** Fig. 1 left column shows LQC, ECH/torsion, Matter bounce, Quintom-B, Cuscuton, Ekpyrotic (6 mechanisms). Table III rows are Matter bounce, Slow-roll inflation, Quintom-B, Cuscuton bounce, Ekpyrotic (5 — Slow-roll replaces LQC and ECH). LQC and ECH disappear from the discrimination table. **Fix:** Reconcile or state explicitly that ECH closure means it isn't in the discrimination table.

### P1A-m3 — Conclusion's "∼9σ" LiteBIRD detection number is mechanism-ambiguous
**Sec. XV, p. 18.** "LiteBIRD (σ(β) ≈ 0.03°, early 2030s) detects non-zero β at ∼ 9σ (a 0.27°/0.03° overall sensitivity number)." Per E9 (initial review) this is null-hypothesis-vs-zero, not vs. WMAP+Planck central. The 9σ is also inconsistent with using the spectator-ALP value 0.27° as the prediction *and* using current observations β_obs = 0.342° as the prior. If LiteBIRD measures β_LiteBIRD = 0.27° (the ECH prediction), the detection vs. β=0 is 9σ. But then the discrimination from the WMAP+Planck central 0.342° is 0.072°/0.03° = 2.4σ, not 0.73σ — *if LiteBIRD itself is the new prior, with σ=0.03°*. The paper's 0.73σ uses the prior σ=0.094° but this then doesn't propagate the LiteBIRD update. The full Bayesian update is more subtle than either single number. **Fix:** Either pick a single discrimination framework (LiteBIRD prior, combined prior, or current prior) and quote that consistently, or stop reporting σ numbers without specifying the null and prior explicitly.

### P1A-m4 — Eq. (7) one-loop estimate has dimension mismatch
**Eq. (7), p. 6.** α/M ∼ (g²/32π²)(γ/M) ln(Λ²_UV/μ²) + δ_NY. LHS has dim −1 (since α dimensionless, M dim 1). RHS: g², γ, ln(...), δ_NY all dimensionless; γ/M is dim −1. So LHS dim = −1, RHS dim = −1. ✓ Actually OK on closer inspection. Withdrawing this flag — but the structure is dimensionally tight and worth a sentence noting that the "α dimensionless" and "M ∼ M_area-gap ∼ M_Pl/√γ" interpretations are both required for Eq. (7) to be dimensionally consistent.

### P1A-m5 — Sec. IV B "the Mercuri & Capozziello [22] one-loop coefficient α_em/(4π)" attribution
Sec. II C 1 reheating paragraph cites "the Mercuri & Capozziello [22] one-loop coefficient α_em/(4π)" but Sec. IV B Eq. (14) attributes the same one-loop structure to Mercuri's Peccei-Quinn paper [19] with the "phenomenological one-loop parity-odd operator" disclaimer that "no published calculation currently derives this exact coefficient structure." If no published calculation derives it, the attribution to "the Mercuri & Capozziello one-loop coefficient" is incorrect. **Fix:** Either cite [22] for the coefficient (in which case point to the specific equation) or remove the attribution and state it as the author's EFT ansatz.

### P1A-m6 — Acknowledgments expose an unusual research-conduct admission
**Acknowledgments, p. 18.** "The author acknowledges the use of Claude (Anthropic) as an AI research assistant during systematic barrier-cataloging, perturbation-gate verification, and manuscript preparation." Many of the issues flagged in E14 (technical misidentification of the Holst-on-Levi-Civita reduction), E16 (figure-body Ntot mismatch), E17 (CC hierarchy 10^{120}/10^{122}/10^{123} oscillation), E18 (uncited "Foundations A–G" framework), and E19 (template-overlap arithmetic) are characteristic of AI-assisted drafting without independent technical verification. The author claims "all scientific claims, derivations, numerical results, and bibliographic attributions were independently verified by the author," but the technical errors found in this re-read suggest the verification was incomplete. **Fix:** No editorial action required of the manuscript itself, but the referee notes for the editor's attention that the AI-assistance disclosure paired with the density of technical inconsistencies surfaced in second-pass review warrants a careful corrected resubmission with independent expert review of the gravitational-action algebra (especially Eq. 23 and Sec. X B Step 4) before any further consideration.

---

## Summary of second-pass findings

Second-pass review surfaced **6 Essential + 5 Major + 6 minor** new issues, of which the most damaging are:

1. **E14**: the "central theorem" misidentifies the Holst-on-Levi-Civita reduction (Pontryagin density is wrong; the correct statement is that the term vanishes identically by first Bianchi). This is a *technical gravitational-algebra error*, not a presentation issue.
2. **E15, E19**: arithmetic errors in the two headline σ figures (ACT/WMAP+Planck consistency and SPHEREx fNL forecast).
3. **E16**: figure-body numerical inconsistency in Fig. 2 (N = 55 in figure, Ntot ≈ 92 in body).
4. **E17**: three inconsistent values for the CC hierarchy (10^{120} / 10^{122} / 10^{123}).
5. **E18**: the entire "Foundations A–G + Branches H–O" framework on which the 14-barrier catalog is built is uncited and undefined.

Combined with the initial review's findings, the paper has accumulated **enough technical errors in the central gravitational algebra and the headline arithmetic that a recommendation of rejection or major-revision-with-independent-expert-verification is warranted.** The Pontryagin-density misidentification in particular is the kind of error that should not survive any competent re-read of an ECH paper claiming a "central theorem" about the Holst sector.