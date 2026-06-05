# P1A auto-2026-06-05_1517pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (10781 chars)
**Wall time**: 400.8s

---

# Referee Report: P1A — "Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"

## Overall assessment

This manuscript fails to meet the standards of *Physical Review D*. The paper is a 21-page channel-level "no-go" argument that, on close reading, rests almost entirely on a phenomenological scaling ansatz the authors themselves admit is not derived (Appendix B), combined with four "closure" arguments that vary in rigor from order-of-magnitude EFT estimates to "naturalness objections rather than amplitude no-go" (Route 4, by the authors' own admission). The central "perturbation transparency theorem" reduces to a textbook statement (canonical scalars have zero spin density, hence zero torsion in EC theory, hence Holst is topological) that has been understood since Hehl et al. 1976. The 14-barrier catalog is acknowledged in-text to contain redundancies (B8 subsumed by B14), with several entries explicitly labeled "known results" or "structural/philosophical observations." The abstract and body are saturated with internal hedges ("under stated assumptions", "phenomenological ansatz", "channel-level, not operator-level", "not derived from the ECH action") that, when extracted, leave very little load-bearing content. This is not a PRD paper; it is closer to a research note or methods commentary that has been padded with a 14-barrier table and four routes whose closures are largely re-statements of well-known suppression arguments.

I list findings below. The list is long because the paper has many problems.

---

## ESSENTIAL findings

**P1A-E1 — Abstract over-claims relative to what is proven (Page 1).**
The abstract opens "We assess four enumerated minimal-Einstein-Cartan-Holst (ECH) spin-torsion channels … and find that each fails at the amplitude level." But Sec. IV D (page 10) explicitly states Route 4 is closed by *"a naturalness objection rather than an amplitude no-go at the operator level"* and that *"a free-coupling spectator-ALP fit reproduces both βobs and ρΛ."* The abstract's "fails at the amplitude level" framing is therefore false for ¼ of the enumerated routes. Required fix: rewrite the abstract to state that 3 routes close on amplitude and 1 closes on naturalness/explanatory deficit only.

**P1A-E2 — Central "result" is a textbook consequence (Sec. X, pages 14–15).**
The "perturbation transparency theorem" reads, in full: (i) canonical scalars have zero spin density; (ii) hence T=0 by the Cartan algebraic equation; (iii) hence Γ = Levi-Civita; (iv) hence Holst becomes Pontryagin density, which is a total derivative. This is a five-line restatement of Hehl et al. (1976) and is not a new theorem. Marketing this as the "central result" of the paper, and as a generalization of Hehl et al. "to all perturbation orders" (page 14), is over-claiming: once T=0 *exactly* (not perturbatively), there is nothing to extend to higher orders. Required fix: demote from "theorem" to "remark," remove "central result" framing, and explicitly cite that the underlying physics is in Hehl et al. 1976.

**P1A-E3 — Appendix B admits the dark-energy mapping is not a derivation (Page 19).**
The paper's entire dark-energy mapping rests on Eq. (B2): ρΛ^bounce ~ (α/M) M_Pl^5 ~ 10⁻² M_Pl⁴. The authors openly state: *"the missing powers of mass do not arise from off-shell EFT counting but from on-shell scaling assumptions … We therefore treat the relation … as a phenomenological on-shell scaling ansatz, not a controlled EFT result."* The operator in Eq. (6) has off-shell mass dimension +1, three units short of +4. The paper's headline numerical result N_tot ≈ 92 e-folds, the 10¹²² → 10⁵ "fine-tuning reduction," and the structural-tension argument in Sec. XIV D *all* depend on this admitted-not-derived ansatz. A PRD paper cannot have its central numerical claims rest on an admitted "ansatz, not a derivation." Either derive it or remove the numerical claims that depend on it.

**P1A-E4 — Route 4 closure is logically incoherent (Sec. IV D, page 10).**
The text states m_θ = H₀ ≈ 1.5×10⁻³³ eV recovers ρ_θ ≈ ρΛ "to within a factor of unity," then concludes this "is precisely the cosmological constant problem in disguise rather than its solution." But this is not a closure — it is exactly the statement that R4 *does* reproduce dark energy with no additional tuning beyond fixing the ALP mass at the observed scale. The authors then qualify: *"R4 is therefore not closed by amplitude mismatch (as prior analyses claimed)"* and *"the channel is closed at the level of an explanatory deficit, not an amplitude no-go at the operator level."* "Explanatory deficit" is not closure. This route is, by the paper's own arithmetic, *open*. Required fix: explicitly state R4 is *not* closed; the abstract's "each fails at the amplitude level" claim must be retracted (see P1A-E1).

**P1A-E5 — N_tot ≈ 92 vs. N_tot ≈ 94 inconsistency in Appendix B (Page 19).**
Appendix B states: *"Ntot ≈ 122 ln10/3 ≈ 94 e-folds (consistent at the ∼2% level with the structural-tension Ntot ≈ 92 quoted in Sec. XIV D)."* But the paper repeatedly quotes "N_tot ≈ 92" as a *headline number* driving the structural tension between dark energy and matter-bounce fNL (abstract, Sec. XIV D, Sec. XIII). If the ansatz uncertainty alone shifts this by ~2 e-folds, the structural tension argument loses precision. More seriously, the abstract's exponential e^(N_tot − N_exit) ~ e^32 prefactor is being quoted to two significant figures from inputs that have ±2 uncertainty. Recompute: e^(92−60) = e^32 ≈ 7.9×10¹³; e^(94−60) = e^34 ≈ 5.8×10¹⁴. The structural-tension differential changes by an order of magnitude under the authors' own admitted ansatz uncertainty.

**P1A-E6 — 13 vs. 14 barrier count is confused throughout (Sec. IX, Sec. XV).**
The paper alternates between "14 mechanism-class constraints," "13 logically-independent," "14 historical catalog entries." Sec. IX classifies four entries as "Known results" (5, 6, 7, 9) and one as "Structural/philosophical observations" (13), so by the paper's own classification at most 9 entries are *novel*, not 13 or 14. The headline number "13 logically-independent" cannot be sustained when 5 entries are admittedly not novel. Required fix: state honestly how many barriers are new ECH-specific calculations vs. textbook restatements.

**P1A-E7 — Route 2 dimensional analysis has an unresolved order-of-magnitude ambiguity (Sec. IV B, page 9).**
The text computes the Route-2 suppression as "∼ 10⁻⁵⁸ to 10⁻⁶⁰" then states *"an alternative ordering that contracts the H₀ factor with the dimensionful coupling differently yields a numerically distinct ∼ 10⁻³³ ratio."* A ~25-orders-of-magnitude ambiguity in the suppression factor (10⁻⁶⁰ vs. 10⁻³³) is not "a factor-of-∼100 ambiguity"; it is the difference between a closure by 60 OOM and a closure by 33 OOM. While both still close the route, presenting "∼ 10⁻⁵⁸ to 10⁻⁶⁰" as "the canonical estimate" without resolving why the alternative ordering is wrong is unacceptable in a PRD methods paper. Required fix: derive the correct dimensional reduction from the Lagrangian and state which contraction is dimensionally consistent.

**P1A-E8 — Eq. (7) has an explicit dimensional inconsistency (Sec. II A 2, page 6).**
Equation 7 reads α/M ~ [g²/(32π²)] (γ/M) ln(Λ²_UV/μ²) + δ_NY. The LHS has units of [mass]⁻¹. The RHS has γ/M with units [mass]⁻¹ multiplied by a dimensionless log, plus δ_NY whose units are unspecified. This is internally consistent if δ_NY has units of [mass]⁻¹, but the paper never specifies δ_NY's dimensions and uses Eq. (7) to "motivate" α/M ~ 10⁻² (a dimensionless number) two lines later, which is dimensionally inconsistent with the LHS being [mass]⁻¹. Required fix: state δ_NY's dimensions and clarify whether α/M is dimensionful or whether [(α/M) M_Pl] is the dimensionless quantity.

**P1A-E9 — Page count grossly exceeds contribution (whole paper).**
The paper occupies 21 pages to present (i) a textbook perturbation-transparency observation, (ii) four order-of-magnitude amplitude estimates closing routes, (iii) a 14-row table half of which is admittedly not novel, and (iv) a dark-energy mapping the authors themselves call an ansatz not a derivation. The novel content fits comfortably in 6–8 pages. The remainder is repetition (the SPHEREx-erasure paragraph is restated essentially verbatim in the abstract, Sec. I, Sec. XIII, and Sec. XIV D), excessive cross-referencing to four companion papers all marked "in preparation," and extensive in-line hedging that re-litigates the same caveats. Required fix: reduce to 8 pages or convert to a brief Comment.

**P1A-E10 — Heavy reliance on companion papers "in preparation" (Refs. [2, 6, 23, 46]).**
The paper repeatedly defers load-bearing claims to companion papers in preparation: MCMC values (H₀ = 67.68 ± 1.06, ∆N_eff), the SPHEREx Fisher forecast (3–5σ on fNL), the galaxy chirality null, the NaMaster pipeline, the ALP parameter fitting, and the PTA γ = 2.567 ± 0.382. The paper *explicitly states* (page 5): *"Cosmological parameter values referenced in this paper … are drawn from the companion internal MCMC analysis (Paper I(b) [6], in preparation); they are documented internally rather than as externally citable arXiv-posted numbers."* PRD does not accept "documented internally" as a citation. Either post the companion papers as a coordinated submission or remove all dependent claims.

**P1A-E11 — Sigma values from incomparable null procedures juxtaposed without qualification.**
Sec. XV "Surviving tests" states LiteBIRD "detects non-zero β at ∼ 9σ (a 0.27°/0.03° overall sensitivity number)" and immediately notes the *model-discrimination* test against the WMAP+Planck central value yields only 0.73σ. The "∼ 9σ" headline is the sensitivity against β=0; the 0.73σ is against the measured central value. These are not directly comparable. The paper does add a corrective sentence, but the "∼ 9σ" still appears as a headline and could be quoted out of context. Required fix: remove the "∼ 9σ" framing entirely or qualify at every juxtaposition.

**P1A-E12 — fNL 3–5σ forecast is contingent on undisplayed inputs (Sec. VII footnote 1, page 11).**
The footnote describes σ(fNL) ≈ 0.7 Fisher-ideal → "5–5.5σ optimistic after template-overlap correction r ≈ 0.84" → "3–5σ realistic after GR-projection and photo-z marginalization." Recompute: 4.375/0.7 = 6.25σ; 4.375/1.0 = 4.375σ. The "3–5σ realistic" range is therefore the band from σ(fNL) between 0.875 (5σ) and 1.46 (3σ). The footnote says "σ(fNL) ≈ 1.0" gives "3–5σ realistic," which is arithmetically wrong: σ=1.0 gives 4.375σ, not "3–5σ." Required fix: recompute and report a single defensible value, or define the range explicitly.

---

## MAJOR findings

**P1A-M1 — Reheating thermal-reset paragraph contradicts the paper's own dark-energy mechanism (Sec. II C 1, page 7).**
The "Reheating thermal-reset barrier" paragraph argues that the C/P-violating thermal background drives ⟨J⁵_μ⟩ → 0 *regardless of N_tot*, "providing an independent thermodynamic closure … that does not require the dimensional bookkeeping of Appendix B or the specific value of N_tot." But this destroys the entire D_inf ∝ exp(−3N_tot) mechanism that drives the rest of the paper, including the "structural tension" with fNL in Sec. XIV D. The paper admits this: *"this is bookkeeping, not progress."* If the reheating thermal-reset closes the channel independently, then the N_tot ≈ 92 result is meaningless, and the entire Sec. XIV D structural tension dissolves. The paper does not resolve this internal contradiction.

**P1A-M2 — "Mercuri-motivated" derivations are not actually derived from Mercuri's work.**
Sec. II A 2 says Eq. (5) is "Motivated by … the Holst+non-minimal-fermion construction of Mercuri [19]." Sec. IV B says Eq. (14) is "Motivated by (but not literally derived in) the Holst+non-minimal-fermion construction of Mercuri and Mercuri & Capozziello." Sec. IV C says Eq. (16) is "Schematically motivated by their construction" of Date, Kaul & Sengupta but "does not itself present the explicit RG equation used below." These admissions cumulatively mean the four-route closure rests on three ansatz-level operators presented as if they follow from the literature. PRD requires that operators used in load-bearing amplitude estimates be either derived or cited as published. Required fix: either derive each operator or cite a paper that does.

**P1A-M3 — Table I row "H0/σ8 tension resolution? Recovers ΛCDM" (page 4).**
This row claims the paper "Recovers ΛCDM" with H₀ = 67.68 ± 1.06 and ∆N_eff ≈ 0. But "recovers ΛCDM" means the framework does *not* resolve H₀ tension. Listing this as a positive outcome in an executive-summary table misrepresents what the paper achieves. Either remove the row or label it honestly as "framework does not resolve H₀ tension."

**P1A-M4 — Figure 2 caption: "phenomenological scaling ansatz" admission undermines figure's content (Page 5).**
Figure 2 displays the energy hierarchy from M_Pl^4 down to Λ_obs with the explicit relation ρ_vac ~ [(α/M) M_Pl] M_Pl⁴. The caption admits *"This ansatz is dimensionally correct on-shell at the bounce but is not derived from the ECH action."* A figure illustrating a non-derived ansatz cannot be presented as a scientific result. Either drop the figure or relabel as "Cartoon of the assumed scaling."

**P1A-M5 — Table III: "consistent†" Quintom-B row without posterior support (Page 16).**
The footnote admits *"The MCMC analysis hosted in companion Paper I(b) was not extended to the w₀wₐ parameter space, so this row is reported as 'consistent at the model level' rather than a posterior-preference ✓."* Listing a row as "consistent" when it has not been tested computationally is misleading. Either run the chain or remove the row.

**P1A-M6 — Table III footnote ‡ explicitly states the chain has not converged.**
The footnote reports: *"At the time of this writing the chain has accumulated ∼3.8×10⁴ accepted samples … and reports R̂ − 1 ≈ 3×10⁻², descending monotonically toward the standard publication-quality convergence target R̂ − 1 < 10⁻²."* In other words, the running chain *does not meet PRD convergence standards* and the authors know it. Either wait for convergence or remove all dependent claims. Currently the paper publicly admits to running unconverged MCMC chains while citing their preliminary results.

**P1A-M7 — Eq. (15) numerical inconsistency.**
Plug in: α_em/4π ≈ 5×10⁻⁴, H₀/M_Pl ≈ 10⁻⁶¹, M_Pl·(α/M) ≈ 10⁻², β_obs ≈ 6×10⁻³. Then ∆θ_one-loop/∆θ_obs ≈ (5×10⁻⁴)(10⁻⁶¹)/[(10⁻²)(6×10⁻³)] ≈ (5×10⁻⁶⁵)/(6×10⁻⁵) ≈ 8×10⁻⁶¹, not "10⁻⁵⁸ to 10⁻⁶⁰". Recompute and reconcile.

**P1A-M8 — Sec. II A 2 BI scheme dependence quoted as if it were error (Page 5–6).**
The text states γ_SU(2) ≈ 0.274 then "the apparent uncertainty range is scheme dependence rather than a statistical or theoretical error." Yet Table IV (page 20) lists "0.274 (scheme range ∼0.020)" as if it were a quantitative uncertainty. Either the scheme range propagates into the headline numbers (e.g., ρ_crit = 0.27–0.41 ρ_Pl) or it does not. The paper uses both treatments interchangeably.

**P1A-M9 — Heinrich et al. citation: traceability check.**
The paper cites Heinrich, Doré & Krause (Ref. [36]) for σ(fNL) ≈ 0.7 from SPHEREx. The referenced paper (arXiv:2311.13082) provides multi-tracer forecasts; the specific value σ(fNL) ≈ 0.7 must be verified against the cited paper's tables for the matter-bounce shape, not local-type. The paper's footnote 1 invokes a "template-overlap correction r ≈ 0.84 between the matter-bounce shape and the local/equilateral basis" — this correction does not appear to be in Heinrich et al. and is not cited to any source. Required fix: cite the source of r ≈ 0.84 or derive it.

**P1A-M10 — Sec. III A: β value inconsistent.**
The body states "qualitatively consistent with the observed isotropic birefringence at β ≈ 0.27°–0.30°." Eskilt & Komatsu (Ref. [4]) report 0.342° ± 0.094°. The paper's "0.27°" benchmark sits ~0.8σ low. Calling this "consistent" without quantifying is sloppy.

**P1A-M11 — Footnote about PTA γ = 2.567 ± 0.382 sits at "+1.13σ above the posterior mean" (Sec. X G).**
Posterior mean is 2.567, prediction is 3.0, σ = 0.382: (3.0 − 2.567)/0.382 = 1.133σ. Arithmetic checks. But the paper labels this as "consistent within standard frequentist tolerance" while the abstract elsewhere lists the same comparison as the surviving "PTA γ = 3.0 v.s. data 3.20 ± 0.42 (P3 §6)" in Fig. 1. The Fig. 1 number (3.20 ± 0.42) contradicts the Sec. X G number (2.567 ± 0.382), the explanation being "This figure supersedes the earlier synthetic-Gaussian-likelihood value γ = 3.20±0.42 used in pre-real-KDE drafts." This is internal version-history language and should not appear in the body of a PRD submission. The Fig. 1 number should be updated, not left contradicting the body.

**P1A-M12 — Fig. 1 caption and content do not match the body.**
Fig. 1 lists "PTA γ = 3.0 v.s. data 3.20 ± 0.42 (P3 §6)" as a surviving prediction, contradicting the text at Sec. X G which states this number is superseded by 2.567 ± 0.382. The figure must be updated to match the body.

**P1A-M13 — Citation [22] Mercuri & Capozziello "One-loop corrections to the Holst term."**
Verify this paper actually derives Eq. (14)'s α_em/(4π) one-loop chiral-anomaly suppression for the Holst+fermion sector. The paper admits "no published calculation currently derives this exact coefficient structure" (page 9), which contradicts using [22] as a quantitative source.

**P1A-M14 — "Channel-level, not operator-level" scope caveat repeated 6+ times.**
The Scope caveat appears in the abstract, Sec. I, Sec. IV (Scope paragraph), Sec. IV E, Sec. XIV E, Sec. XV, and Sec. XV again. Repeating the same caveat half a dozen times is filler and signals that the authors are aware their result does not support the headline framing. Consolidate to one statement.

**P1A-M15 — "0.27° spectator-ALP benchmark" is admitted not to be an ECH prediction.**
Abstract (page 1) and Sec. XIII (page 16) explicitly state this is "not an ECH prediction" but a benchmark consistency point that "arises in any GR+ALP setup with the same parameters." Then why is it listed in the paper as a "surviving prediction" of the ECH framework? It is unrelated to ECH. Required fix: remove from the "surviving predictions" list.

**P1A-M16 — Same applies to fNL = −35/8.**
Abstract (page 1): "fNL = −35/8 is a property of the matter-bounce class … derived from the contraction-phase cubic action with no ECH input." Then it is not an ECH prediction. Why does it appear as a "surviving test" of the present ECH-focused paper? The honest framing is that the paper has zero surviving predictions of its own.

**P1A-M17 — Eq. (13) prefactor needs verification against Hehl & Datta.**
The paper writes L = −(3/16)κ(ψ̄γ^a γ⁵ ψ)². Verify the (3/16) factor against the original Hehl-Datta (1971) derivation. Some textbook treatments give (3κ/8) or (3κ/16); the conventions on Lorentz contraction differ.

---

## MINOR findings

**P1A-Mi1 — "On-shell mass dimension is +1 rather than +4" appears 4+ times.**
This caveat is over-repeated; consolidate.

**P1A-Mi2 — Sec. II C 1 paragraph is 1200+ words for an order-of-magnitude estimate.**
The "Order-of-magnitude matching for Eq. (11)" paragraph is excessively long and could be reduced to half a page. The reader is told three times the (T_reh/M_GUT)^(3/2) prefactor is "dimensional-analysis aesthetic" and "not derived from a thermal partition function."

**P1A-Mi3 — Sec. IX classification is opaque.**
"Novel results (Barriers 1, 2, 3, 4, 8, 10, 11, 12, 14)" — 9 barriers labeled novel, but B8 is admitted to be subsumed by B14, leaving 8. Then "13 logically-independent" cannot be right.

**P1A-Mi4 — Eq. (4) sign and prefactor consistency.**
The 4-fermion contact term has coefficient −(3πG_N/2)·γ²/(γ²+1). Verify the sign and the γ²/(γ²+1) ratio against Freidel-Minic-Takeuchi (Ref. [15]).

**P1A-Mi5 — Inconsistent capitalization of "Loop Quantum Cosmology" / "loop quantum cosmology" throughout.

**P1A-Mi6 — Abstract page 1: "(14 historical catalog entries, of which B8 is subsumed by B14 per the perturbation-transparency result)."**
This is internal-bookkeeping language that should not appear in an abstract.

**P1A-Mi7 — "We acknowledge missing operators (Jackiw-Pi gravitational Chern-Simons R∧R̃, parity-odd four-fermion partner …) explicitly in Sec. IV and Sec. XI."**
Acknowledging missing operators in the abstract is a confession that the paper's central "channel-level closure" claim is incomplete. PRD abstracts should state what the paper proves, not what it omits.

**P1A-Mi8 — Sec. III A: "Spectator-ALP parameter fitting and the NaMaster pipeline validation are in companion Paper I(b)."**
Repeated 4+ times throughout the paper. Once is enough.

**P1A-Mi9 — Eq. (12) is dimensionally trivial (standard birefringence formula) and adds no content.**

**P1A-Mi10 — "Definitively erased" used to describe an erasure that depends on the unknown N_tot value (Sec. XIV D).**
The verb "definitively" is too strong for a conditional claim.

**P1A-Mi11 — Acknowledgments admit AI assistance during "systematic barrier-cataloging, perturbation-gate verification, and manuscript preparation."**
This raises questions about the verified novelty of the 14-barrier catalog, but PRD does not currently forbid AI-assisted authorship; flag for transparency.

**P1A-Mi12 — Page 5: "309,189 frozen accepted samples across two converged dataset combinations."**
This very specific number is for a companion paper. Why is it in the body of this paper at all?

**P1A-Mi13 — "Cobaya v3.6.1" — code version specifics belong in a methods paper, not a theory paper.**

**P1A-Mi14 — "Stock CAMB with ∆N_eff" admitted as "phenomenological proxy, not a bespoke spin-torsion Boltzmann module" (Sec. XIV A 2).**
Then the MCMC results have no specific ECH content and should not be quoted as supporting the framework.

**P1A-Mi15 — Date "June 2, 2026 PDT" — submission dated in the future relative to most cited literature.**

**P1A-Mi16 — Ref. [44]: "Y.-F. Cai and J.-H. Zhu, … (2026), arXiv:2603.13924"** — arXiv ID 2603.* does not exist; arXiv IDs use YYMM and 2603 would be March 2026. Verify ID validity.

**P1A-Mi17 — Ref. [43]: "S. Alam, S. Sen, and S. Sengupta, … Eur. Phys. J. C (2025), arXiv:2509.03508"** — arXiv 2509.* is September 2025; verify acceptance date.

**P1A-Mi18 — Ref. [47]: "H. Golden, … (2026), companion technical note, available upon request from the author."**
PRD does not accept "available upon request" citations for load-bearing references.

---

## NITs

**P1A-N1 — Various unicode rendering issues throughout (e.g., "Pop lawski" with broken łigature, "G¨odel" instead of Gödel, "Domaga la" with broken ł, "ϵ" vs "ε" inconsistently used).**

**P1A-N2 — Table IV row "γ_PTA" comparison "Bounce γ = 3.0 at +1.1[…]"** — last digit cut off in the rendered table.

**P1A-N3 — "ψγ¯" appears throughout instead of ψ̄γ — Bar-rendering bug.

**P1A-N4 — Figure 2 axis labels and content cannot be fully audited from the rendered low-resolution figure; ensure axis units (GeV⁴) are present.**

**P1A-N5 — "13 logically-independent" appears 8+ times throughout; consolidate.

**P1A-N6 — "phenomenological" appears 23+ times; tone down.

**P1A-N7 — Abstract is 1100+ words; PRD abstract limit guidance is ~250 words.

---

## Summary recommendation

**REJECT**

The paper does not meet PRD standards. The central "perturbation transparency theorem" is a textbook restatement of Hehl et al. 1976; the dark-energy mapping is admitted to be a phenomenological ansatz, not a derivation (Appendix B); one of the four "closed" routes (R4) is openly conceded not to be closed at the amplitude level; the 14-barrier catalog contains admitted redundancies and "known results" inflating the headline count; the abstract over-claims ("each fails at the amplitude level") relative to what Sec. IV D actually argues; the load-bearing MCMC, Fisher, and chirality results are deferred to four companion papers all "in preparation," one of whose chain is publicly admitted not to have converged; arithmetic inconsistencies appear in Eq. (15) and the σ(fNL) → significance calculation; figure and body disagree on the PTA γ value with the body containing internal "supersedes earlier draft" language; the page count is 2–3× larger than the novel content justifies. The honest version of this paper is a 4-page Comment noting that ECH with canonical scalars trivially yields T=0 and that the standard channels for sourcing dark energy from ECH are amplitude- or naturalness-suppressed. It should not appear in PRD in its current form.

---

## PASS 2 — self-critique findings (what initial review missed)

# Second-Pass Referee Report: Additional Findings

After re-examining the paper with fresh attention to arithmetic, dimensional consistency, figure-text alignment, and the technical content of the "central result," I identified a number of additional issues not flagged in my initial review. The most serious is a conceptual error in Eq. (23) that undermines the paper's headline "perturbation transparency theorem."

---

## ESSENTIAL findings (new)

**P1A-E13 — Eq. (23) misidentifies the Holst dual as the Pontryagin density (Sec. X D, page 14).**
The paper's headline "perturbation transparency theorem" states (Eq. 23):
*"R̃(Γ̊) = (1/2)ε^{μνρσ} R_{μνρσ}(Γ̊) = (1/2) *R R ≡ ∂_μ K^μ (Pontryagin density; total derivative)."*

This is incorrect on two distinct counts:

(i) **Dimensional / structural error.** The Pontryagin density is *R R = (1/2)ε^{μνρσ} R^{αβ}_{μν} R_{αβρσ}, which is *quadratic* in the Riemann tensor and has mass dimension +4. The Holst dual ε^{μνρσ} R_{μνρσ} is *linear* in Riemann and has mass dimension +2. These cannot be equated, and ε^{μνρσ} R_{μνρσ} is not "the Pontryagin density."

(ii) **The Holst dual does not reduce to a total derivative — it vanishes identically on a torsion-free connection.** By the first (algebraic) Bianchi identity R_{μ[νρσ]} = 0 on Levi-Civita, ε^{μνρσ} R_{μνρσ} ≡ 0 pointwise. The standard LQG-literature statement is that the Holst term vanishes identically in vacuum (Holst 1996, Ref. [25]), *not* that it is a Pontryagin total-derivative. The Nieh–Yan invariant (which involves torsion explicitly) is the topological / total-derivative piece, but Nieh–Yan vanishes when T=0 also.

Either way, the abstract's qualifier *"generically non-zero pointwise but a total derivative"* is incorrect: ε^{μνρσ} R_{μνρσ} is identically zero pointwise on Levi-Civita, not a generically non-zero total derivative. The Sec. X B "Proof" step 4 (*"on a torsion-free connection is the Pontryagin density ∝ RR̃"*) carries the same conflation. This is a technical error in what the paper repeatedly labels its "central result." The conclusion (Holst decouples for canonical scalars) survives, but for a completely different reason than stated. Required fix: replace the Pontryagin-density claim throughout (abstract, Sec. X B step 4, Eq. 23, Sec. X D) with the correct statement that ε^{μνρσ} R_{μνρσ} vanishes identically on Levi-Civita by the first Bianchi identity.

**P1A-E14 — Abstract numerical claim about ACT–WMAP+Planck consistency is wrong by ~30%.**
Abstract (page 1) states ACT DR6 β = 0.215° ± 0.074° "is comparable to" WMAP+Planck β = 0.342° ± 0.094° at "∼1.4σ." Recompute the differential consistency: (0.342 − 0.215)/√(0.094² + 0.074²) = 0.127/√(0.00884 + 0.00548) = 0.127/0.1197 ≈ **1.06σ**, not 1.4σ. The same number is implicitly used in the body (Sec. XII B). Either the 1.4σ is wrong or it incorporates an additional systematic the paper does not disclose.

---

## MAJOR findings (new)

**P1A-M18 — Internal inconsistency in αem/(4π) between Sec. IV B prose and Sec. IV B plug-in.**
Sec. IV B states "αem/(4π) ≈ 5×10⁻⁴ (more precisely ≈ 5.8×10⁻⁴ since αem ≈ 1/137)". Two lines later the actual plug-in uses αem/(4π) ≈ 10⁻³: *"the dimensionless ratio is ∆θ_one-loop/∆θ_obs ∼ 10⁻³ · 10⁻⁶¹/(10⁻² · 6 × 10⁻³)"*. Using the stated 5×10⁻⁴ gives ≈ 8×10⁻⁶¹; using the plugged-in 10⁻³ gives ≈ 1.7×10⁻⁶⁰. Neither value matches the headline range "∼ 10⁻⁵⁸ to 10⁻⁶⁰." The "10⁻⁵⁸" endpoint is not derivable from any combination of the stated inputs. The factor-of-100 range is unjustified.

**P1A-M19 — Companion paper [46] title does not match its cited content.**
Sec. X G and Table IV cite Ref. [46] ("Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Anomalies and Native-Trained Novelty Rates from 37.3 Million Sources") for "γ = 2.567 ± 0.382 from real-KDE re-analysis of the 15-yr free-spectrum data (GPU MCMC, companion Paper III [46])". A multi-survey anomaly catalog is not a PTA timing-data re-analysis. Either the title or the citation is wrong; the load-bearing PTA number cannot be sourced from a paper whose title describes a different analysis.

**P1A-M20 — Eq. (14) has a missing power of M_Pl for action dimensionlessness.**
Eq. (14) reads Γ_one-loop^{parity-odd} = −(1/16π²)(β(γ)/M_Pl) ∫ d⁴x √(−g) ∂_μ θ(x) J^{5μ}. The Nieh–Yan pseudoscalar θ in Mercuri's normalization is dimensionless (a phase). Then ∂_μ θ has [M], J^{5μ} = ψ̄γ^μγ^5ψ has [M³], product has [M⁴]. Divided by M_Pl gives [M³]; integrated over d⁴x ([M⁻⁴]) gives [M⁻¹]. The action is not dimensionless. Required fix: clarify θ's dimensions or insert the missing M_Pl factor. As written, the downstream amplitude estimate (which inverts this against the Planck-mass coupling) is dimensionally inconsistent.

**P1A-M21 — Sec. IV D "fractional width ∆m_θ/m_θ ∼ 10⁻¹" is not derived, and is then inconsistent with the dimensionful-tuning claim.**
Sec. IV D states *"the m_θ ∼ H₀ window where both observables are simultaneously matched has fractional width ∆m_θ/m_θ ∼ 10⁻¹, representing a dimensionful tuning of order 10⁻³³ eV/M_Pl ∼ 10⁻⁶¹."* Two problems:
(i) The 10⁻¹ fractional width is not derived; where does 0.1 come from? It is not the ratio of any quantity to any other quantity computed in the section.
(ii) The dimensionful-tuning number 10⁻⁶¹ is computed using m_θ ~ H₀ itself (10⁻³³ eV / M_Pl), not the width ∆m_θ ~ 0.1 H₀ ~ 10⁻³⁴ eV / M_Pl ~ 10⁻⁶². Internal inconsistency: the "width" 10⁻¹ does not enter the dimensionful estimate.

**P1A-M22 — Sec. IV (R3) Standard Model chiral-asymmetry estimate is undefined.**
Sec. IV C states *"In the Standard Model, the chiral asymmetry is generated by the SU(2)_L doublets; numerically, ∆γ/γ ∼ 10⁻² over the running from the GUT scale to the IR."* With N_F^L = 15 and N_F^R = 6 (per generation, depending on normalization), Eq. (16) gives dγ/d ln μ = (9/12π²)γ × 3 generations / ln scale. Running from GUT (∼10¹⁶ GeV) to IR (∼1 eV) is ln(10²⁵) ≈ 58. Then ∆γ/γ ≈ (27/(12π²))·58·γ ≈ 13·γ ≈ 13·0.274 ≈ 3.5, not 10⁻². The "∆γ/γ ∼ 10⁻²" claim is off by 2+ orders of magnitude from a naive application of the paper's own RG equation. Either Eq. (16) has the wrong coefficient or the "10⁻²" is wrong; the Route 3 amplitude budget is unverified.

**P1A-M23 — Sec. XII B Routes list does not match Sec. IV Routes list.**
Sec. XII B states *"(i) NJL condensate, (ii) one-loop fermion effective action, (iii) dynamical Immirzi field, (iv) parity-sensitive CMB phenomenology."* Sec. IV labels them (R1 NJL contact, R2 **one-loop graviton corrections to the Holst sector**, R3 **quantum running of the Immirzi parameter**, R4 parity-odd CMB). The two lists differ at items (ii) and (iii): "one-loop fermion EA" ≠ "one-loop graviton corrections"; "dynamical Immirzi field" ≠ "quantum running of Immirzi." These are physically distinct mechanisms. Either the paper closes 4 routes or it closes 6 (or 8, if both lists are separate). The conclusion *"All four yield clean negative results"* is therefore ambiguous: which four?

**P1A-M24 — Table I claims "14 constraints" but abstract claims "13 logically-independent."**
Table I row "Can bounce derive dark energy? 14 constraints map minimal-ECH route space" contradicts abstract "13 logically-independent." The reconciliation (14 historical, B8 subsumed by B14, leaving 13) is stated in the body but Table I, in the executive-summary position, contradicts the abstract.

**P1A-M25 — Table IV cosmological values diverge measurably from Planck 2018 values cited as the prior.**
Table IV reports σ8 = 0.803 ± 0.008 and Ω_m = 0.308 ± 0.005 from the companion MCMC. Planck 2018 (Ref. [7]) gives σ8 = 0.811 ± 0.006 and Ω_m = 0.315 ± 0.007 (TT+TE+EE+lowE+lensing). The Table IV σ8 sits 0.8σ below Planck; Ω_m sits 0.8σ below Planck. The companion's "consistent with standard ΛCDM" framing should quantify these tensions, especially given the σ8-tension discussion in Sec. XIV B.

---

## MINOR findings (new)

**P1A-Mi4 — Sec. IX branch numbering skips letters.**
The six observational branches are labeled "H, J, L, M, N, O." Branches I and K are missing without comment. If branches existed and were dropped, say so; if not, renumber.

**P1A-Mi5 — Eq. (15) cancellation pathway shown only one way.**
The "alternative ordering yields ∼ 10⁻³³" alternative is mentioned but the derivation of the alternative is not shown. The reader cannot adjudicate which contraction is correct.

**P1A-Mi6 — Sec. II A 2 "the inverse-length / mass scale is M_Δ ∼ M_Pl/√γ up to numerical constants."**
The LQG area gap is Δ = 4√3 π γ ℓ_P². The corresponding mass scale satisfying M² ~ 1/Δ gives M ~ M_Pl/√(4√3 π γ) ~ 0.21 M_Pl/√γ at γ = 0.274. "Up to numerical constants" hides an O(0.2) factor that propagates through Eq. (5).

**P1A-Mi7 — Sec. XII A "the surplus required to close the gap is ∼ 14 e-folds" is undefined.**
Surplus relative to what baseline? From the body, N_tot ≈ 92 closes the gap; the ε-correction shifts by ≲ 1 e-fold. The "14 e-folds" surplus is not derived in context.

**P1A-Mi8 — Sec. III A "qualitatively consistent with β ≈ 0.27°–0.30°" is undefined.**
Eskilt & Komatsu central value is 0.342°. ACT DR6 is 0.215°. The "0.27°–0.30°" window is neither the WMAP+Planck range, nor the ACT range, nor their joint range. Where does this window come from?

**P1A-Mi9 — Sec. II C 1 ρ_crit window 0.27–0.41 quoted as if both values are physical.**
0.41 ρ_Pl corresponds to γ = 0.2375 (Domagała–Lewandowski–Meissner); 0.27 ρ_Pl corresponds to γ = 0.274 (SU(2) full). These are two different counting schemes — the paper should pick one for headline use and note the other in passing, not interpolate.

**P1A-Mi10 — Sec. XV "0.27°/0.03°" overall sensitivity number again uses the unsupported 0.27° benchmark.**
The "9σ" headline depends on the 0.27° spectator-ALP value, which is admitted to be a tuned benchmark with no first-principles derivation. The "9σ" is then a circular statement: a benchmark chosen near the observed signal will be detected at high significance against zero by construction.

---

## Items examined and confirmed consistent

For the record (so the authors know what I did look at): I verified the arithmetic of (mθ/H₀)² → 10²² and 10³⁶ at mθ = 10⁻²² and 10⁻¹⁵ eV (Sec. IV D); the e^32 differential at N_tot − N_exit = 32 (abstract); the (4.375/0.7) = 6.25σ Fisher-ideal estimate and 6.25 × 0.84 ≈ 5.25σ template-corrected estimate (Sec. VII footnote 1); the 122 × ln(10)/3 ≈ 94 e-fold estimate (Appendix B); the (3.0 − 2.567)/0.382 = 1.13σ PTA comparison (Sec. X G); the ρ_crit derivation at γ = 0.274 → 0.27 ρ_Pl and γ = 0.2375 → 0.41 ρ_Pl (Sec. II B); and the Eq. (17) R4 amplitude reproducing β_obs ≈ 5×10⁻³ rad at m_θ ~ H₀, α/M ~ 10⁻²¹ GeV⁻¹ (Sec. IV D). These check out. The remaining problems are documented above.