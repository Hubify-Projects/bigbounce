# P1A auto-2026-06-08_1819pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (12489 chars)
**Wall time**: 400.3s

---

# Referee Report: P1A — "Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"

## Overall Assessment

This manuscript presents itself as a systematic "channel-level closure" of four ECH dark-energy routes plus a "perturbation-transparency theorem." After careful reading, the paper has fundamental structural problems that preclude publication in PRD:

1. **The central "theorem" is trivial.** The "perturbation-transparency result" reduces to: "if torsion vanishes, the Holst term vanishes." This is elementary and not new — Hehl et al. (1976) already established that canonical scalar matter has zero spin density, hence T=0, hence the Holst term contributes nothing. The paper inflates this triviality into a "central result."
2. **The "no-go" is largely a strawman.** The paper acknowledges (repeatedly) that the four routes are NOT a complete operator basis, that the dark-energy mapping is "a phenomenological ansatz, not a derivation," and that Route 4 is "a naturalness objection rather than an amplitude exclusion." After stripping these admissions, nothing rigorous remains.
3. **Extreme self-citation to companion papers "in preparation."** Five companion papers (none publicly available) are cited as load-bearing for MCMC, Fisher forecasts, galaxy chirality, anomaly catalogs, and ALP fits. This is unreviewable.
4. **The paper is grossly bloated for its actual content.** 22 pages of meta-discussion, hedging, scope caveats, and parenthetical disclaimers around perhaps 4 pages of actual technical content.
5. **Pervasive internal-audit/version-history leakage** in the body text.

I recommend **REJECT**.

---

## ESSENTIAL findings

### P1A-E1 (Abstract, p. 1; §X, p. 15): Central "theorem" is trivial and not new
The "perturbation-transparency theorem" states: canonical scalars have zero spin density ⇒ T=0 ⇒ Holst dual contraction vanishes by Bianchi. This is a textbook calculation (Hehl 1976 already establishes step 1; step 2 follows from the algebraic Bianchi identity which has been known since Riemann). The paper itself admits (§X.B) "This generalizes Hehl et al. (1976) [12] to the Holst sector," but this "generalization" is one line of algebra. **Fix:** Either demonstrate genuinely new content (e.g., closure under all matter sectors including fermions with explicit calculation; or higher-order non-minimal couplings), or remove the "theorem" framing. As stated, this does not meet PRD novelty standards.

### P1A-E2 (Abstract, p. 1; Footnote a): Embedded correction of prior error in published-style abstract
The abstract footnote reads: *"Earlier versions of this manuscript erroneously identified the two; the correction preserves the headline conclusion..."* This is internal version-history that has no place in a PRD submission abstract. It also reveals that an earlier version of this work confused the Holst dual contraction with the Pontryagin density — a fundamental error. **Fix:** Remove all "earlier version" language from the abstract footnote and from §X (footnote 2 on p. 16 also contains this language). PRD submissions present the corrected derivation as primary; they do not narrate the correction history.

### P1A-E3 (§II.A.2, p. 6; Appendix B, p. 20): Dimensional inconsistency acknowledged but unresolved
Eq. (6) has mass dimension +1, "three units short of the required +4." Appendix B states explicitly: *"this operator, as written, is not a controlled dimension-+4 EFT operator."* The paper proceeds to use this operator as the foundation of the entire dark-energy mapping. An EFT operator that is off by three powers of mass cannot be patched by "on-shell scaling assumptions" — this is not a controlled approximation, it is dimensional analysis failure. The phrase "phenomenological on-shell scaling ansatz" does not rescue the calculation. **Fix:** Either present a dimensionally consistent operator with the correct power of MPl in the coupling (and re-derive all subsequent estimates), or withdraw the dark-energy mapping entirely. The current presentation — admit the operator is broken, then use it anyway — is unacceptable.

### P1A-E4 (Abstract, p. 1; §IV, p. 8; §IX): "Closure" is a strawman because operators are admittedly omitted
The abstract states the four routes "are not proven to be a complete diffeomorphism-invariant operator basis" and explicitly lists omitted operators (Jackiw-Pi gravitational Chern-Simons R∧R̃, parity-odd four-fermion partner). A "closure" theorem that excludes the most obvious parity-odd operator in the theory (Chern-Simons) is not a closure — it is an incomplete enumeration. The Chern-Simons term is precisely the operator that would produce cosmic birefringence at the gravitational level. **Fix:** Either prove closure on the full diffeomorphism-invariant basis, or rename the result. "Channel-level closure of four enumerated routes (with the most relevant operators omitted)" is not a PRD-grade result.

### P1A-E5 (§IV.D, p. 10–11): Route 4 closure inverted mid-paper
Earlier text claims R4 is "closed by Planck suppression" (abstract) or "naturalness objection." The actual §IV.D analysis shows the spectator-ALP fit *technically reproduces both βobs and ρΛ* with α/M ∼ 10⁻²¹ GeV⁻¹ and mθ ∼ H0. The paper then admits: *"R4 is therefore not closed by amplitude mismatch (as prior analyses claimed); it is closed by the observation that the same coupling that produces βobs requires an ultralight-mass tuning mθ ∼ H0..."* This is the cosmological constant problem itself, not a closure of the ECH route. Calling this a "channel-level closure" is dishonest — the channel works, it just doesn't solve the CC problem (which was never the claim). **Fix:** Remove R4 from the closure list, or admit the four-route closure reduces to three routes plus one open route.

### P1A-E6 (§IV.B, Eq. 15, p. 9): Dimensional analysis explicitly broken, ambiguity admitted
Eq. (15) gives the Route 2 one-loop estimate. The paper states: *"We adopt this contraction as the canonical Route-2 estimate; an alternative ordering that contracts the H₀ factor with the dimensionful coupling differently yields a numerically distinct ∼ 10⁻³³ ratio."* A 25-order-of-magnitude ambiguity in the dimensional bookkeeping is not "an alternative ordering" — it is failure to perform the calculation correctly. **Fix:** Do the calculation rigorously with explicit unit tracking, and report a single defensible number.

### P1A-E7 (§II.C.1, p. 6–7): (Treh/MGUT)^(3/2) prefactor is hand-waved
The paper provides a lengthy paragraph attempting to justify the half-integer power in Eq. (11) and concludes: *"this thermal phase-space factor is not identifiable with the Mercuri & Capozziello [22] one-loop coefficient... is therefore treated as a phenomenological phase-space ansatz, not as derivable from the one-loop anomaly coefficient."* Then in §XII.A: *"a first-principles derivation requires the full bounce-junction matching that lies outside the scope of this paper."* This is an unjustified ansatz used to motivate the headline Ntot ≈ 92 result. **Fix:** Derive the prefactor or remove the entire dilution-suppression mechanism discussion.

### P1A-E8 (Throughout): Excessive reliance on unavailable companion papers
References [2], [6], [23], [46] are all "in preparation" with internal codes "hUBIFY-2026-XXX." Load-bearing claims rely on these:
- MCMC values H0 = 67.68 ± 1.06, ∆Neff posterior, σ8, Ωm: all from [6]
- The fNL = -35/8 forecast at 3-5σ: from [2]
- The galaxy spin null: from [23]
- The PTA γ = 2.567 ± 0.382: from [46]

None of these are publicly available. The paper itself admits (p. 5): *"they are documented internally rather than as externally citable arXiv-posted numbers, and should be read as internal-analysis inputs to the present structural argument rather than as independently peer-reviewable values until Paper I(b) is publicly posted."* **Fix:** This single admission disqualifies the paper from publication. PRD does not publish papers whose central numbers reference unpublished, unavailable companion work. All load-bearing companion papers must be posted (at minimum to arXiv) and reviewed alongside this submission.

### P1A-E9 (Table I, p. 4; Table III, p. 17): Tables contain unresolved entries
Table III "w0wa DESI" column contains: *"not tested‡"* for four out of five rows with a footnote describing an in-progress MCMC that has not converged: *"At the time of this writing the chain has accumulated ∼3.8×10⁴ accepted samples... and reports R̂−1 ≈ 3×10⁻²"*, with the explicit admission *"we deliberately do not commit to a specific calendar date for convergence in this footnote."* A PRD table cannot contain "in-progress, will-converge-later" entries. **Fix:** Wait for convergence and report final results, or remove the column.

### P1A-E10 (§XIII, p. 17–18): "Surviving predictions" admitted to be not ECH predictions
The abstract advertises two "surviving" tests; the paper then explicitly admits these *"are accordingly not predictions of ECH itself, but bounce-class and GR+ALP-class observables."* So what does the paper actually predict? Nothing. **Fix:** Restructure the paper around this honest position: ECH gives no new predictions and the work is a no-go for the four enumerated channels. As written, the abstract advertises predictions the paper disclaims.

### P1A-E11 (§II.C.2 / §III.B, p. 7–8): Galaxy spin result entirely outsourced to [23]
The headline observational result ("3% Shamir claim refuted at high significance") is "reported in Paper IV [23] and are not duplicated here." A theory paper that closes a channel on observational grounds must contain those observational grounds. **Fix:** Either reproduce the analysis in this paper or remove the claim.

### P1A-E12 (Eq. (2), p. 5): Barbero-Immirzi parameter "value" is scheme-dependent, range used inconsistently
The paper quotes γSU(2) ≈ 0.274 in Eq. (2) and immediately notes this is "scheme dependence rather than a statistical or theoretical error" with the range 0.127–0.2375–0.274. Later (§II.B), the bounce density 0.27–0.41 ρPl is presented as a range derived from this scheme dependence. Yet γ enters multiplicatively in many subsequent estimates without propagating this O(2×) uncertainty. **Fix:** Either commit to a single scheme and explain why, or propagate the factor-of-two uncertainty through all downstream estimates.

### P1A-E13 (§IV.C, Eq. 16, p. 10): Route 3 RG equation is admitted to be incorrect
Eq. (16) is presented and the paper immediately admits: *"we use Eq. (16) only as an upper-bound EFT ansatz... and do not claim it is taken verbatim from [26]. The actual fermion-induced perturbative running of the Immirzi parameter is computed by Benedetti & Speziale [27], who find a β-function whose sign depends on |γ| through four-fermion interactions... our Eq. (16) is a chiral-count EFT bound rather than the full perturbative result."* So Eq. (16) is wrong, but used anyway. **Fix:** Use the correct β-function from [27] or remove the Route 3 closure.

### P1A-E14 (§XIV.D, p. 19): Structural tension is misframed
The paper describes "structural tension" between Ntot ≈ 92 dark-energy requirement and Ntot ≳ 60 fNL erasure. But the four-route closure has already rejected the dark-energy mechanism — there is no tension because one side does not exist. The paper admits: *"the no-go has already closed the four amplitude routes by which minimal ECH could source dark energy, so the structural-tension argument has nothing remaining to bind against at the route-amplitude level."* This invalidates the abstract's claim of a "structural tension" finding. **Fix:** Remove the structural tension as an independent result.

---

## MAJOR findings

### P1A-M1 (Abstract): Sigma values not directly comparable
Abstract juxtaposes: *"βobs = 0.342° ± 0.094° (∼3.6σ from β = 0)... ACT DR6 follow-up β = 0.215° ± 0.074° at ∼2.9σ."* These are two different measurements with overlapping but distinct systematics. The paper later admits they differ by ~1.4σ from each other. **Fix:** Add explicit "these are independent measurements with different analysis pipelines and are not directly comparable as a combined detection" qualifier.

### P1A-M2 (Abstract, footnote on p. 4 Table I): Footnote `b` says "3–5σ realistic" with multiple regimes
Table I footnote b admits the 3-5σ range depends on which systematic budget is applied, and references Heinrich+2024 σ(fNL)≈0.7. With |fNL|=4.375 and σ=0.7, raw ratio is 6.25σ. With σ=1.0 (post-systematic), ratio is 4.4σ. So the "3-5σ" range is at best 4.4-6.25σ raw — the lower bound "3σ" appears nowhere in the calculation. **Fix:** Correct the reported sigma range or show explicit derivation of the 3σ lower bound.

### P1A-M3 (Table II, p. 14): Catalog redundancy admitted
The note on Table II reads: *"Barriers 8... and 14... close the same observable channel... by non-independent routes; B14 is the first-principles theorem that subsumes B8... They are listed separately to preserve the historical mechanism-class catalog, but should not be counted as logically independent constraints."* The paper then advertises "14 constraints" in the abstract anyway. This is dishonest accounting. **Fix:** Drop B8, report 13 constraints consistently throughout.

### P1A-M4 (§II.B, Eq. 9, p. 6): Internal extrapolation across counting schemes
*"this lower value is an internal extrapolation across counting schemes (not a value quoted in Ref. [11])"* — but ρcrit ≃ 0.27 ρPl is used throughout the paper as if it were a published LQC value. **Fix:** Use only the published Ashtekar–Singh value ρcrit ≃ 0.41 ρPl, or clearly mark the 0.27 value as the author's own extrapolation everywhere it appears.

### P1A-M5 (§II.C, Eq. 10): "Phenomenological parameterization, not first-principles derivation"
This admission appears immediately after the central dark-energy equation. Yet the equation is used throughout. **Fix:** Either derive Eq. (10) or remove all claims that depend on it (i.e., remove the entire dark-energy framework).

### P1A-M6 (§III.A, Eq. 12): Headline birefringence formula presented without derivation
*"Connecting to a quantitative rotation angle β from the gravitational/torsion operator requires an explicit photon-torsion coupling that has not been derived here."* So the paper claims observational consistency with cosmic birefringence without deriving how its operator produces birefringence. **Fix:** Either derive the photon-torsion coupling or remove the birefringence consistency claim.

### P1A-M7 (Throughout): Repeated 92 e-fold / 60 e-fold / 32 e-fold differential
The phrase "Ntot ≈ 92, Nexit ≈ 60, relative differential ∼ 32" appears at least 4 times verbatim across abstract, §I, §XIII, §XIV.D. **Fix:** Consolidate into one careful presentation.

### P1A-M8 (Bibliography, [10]): Citation accuracy
Ref [10] cites "DESI DR2 results II" as Phys. Rev. D 112, 083515 (2025). Verify: DESI DR2 BAO paper arXiv:2503.14738 is the BAO+constraints paper; the volume/page should be checked against the actual published version.

### P1A-M9 (§IV.B, p. 9): "Motivated by (but not literally derived in)" admission
*"motivated by (but not literally derived in) the Holst+non-minimal-fermion construction of Mercuri and Mercuri & Capozziello — those works establish the classical structure of the Holst term coupled to fermions and the Nieh–Yan invariant, not this exact one-loop operator — we adopt the phenomenological one-loop parity-odd operator..."* The Route 2 closure rests on an operator that no published reference contains. **Fix:** Derive the operator from first principles or withdraw Route 2.

### P1A-M10 (Fig. 3 caption, p. 13): Caption-content mismatch
Caption describes "Naturalness landscape for the four minimal-ECH dark-energy routes... (mass×coupling) plane." The actual figure shows (top) "Renormalization Group Running of α/M" — a line — and (bottom) "Dark Energy Fine-Tuning Comparison" — a bar chart of fine-tuning scores for ΛCDM/Quintessence/f(R)/Spin-Torsion. Neither is a "(mass×coupling) plane." **Fix:** Rewrite the caption to match the figure, or replace the figure to match the caption.

### P1A-M11 (Fig. 2, p. 5): Energy density hierarchy figure shows ×10⁻¹²² dilution
The figure caption claims this is illustrating the phenomenological scaling ansatz, but the figure shows specific numerical values (10⁹⁵ GeV⁴, ρc ≈ 0.27 ρPl, ρvac ≈ α/M M⁴Pl) that mix the broken-dimension Eq. (6) result with phenomenological matching. This visualizes an ansatz that the paper admits is not derived. **Fix:** Either remove the figure or mark prominently as "phenomenological visualization."

### P1A-M12 (§XII.A, p. 16): "Bookkeeping, not progress"
The author himself states: *"We emphasize that this is bookkeeping, not progress: the residual 10⁵ tracks the exponential e⁻³ᴺᵗᵒᵗ and inherits its sensitivity from the initial-condition choice for Ntot... The framework has not solved the cosmological constant problem; it has only relocated the fine-tuning into inflationary initial conditions."* **Fix:** This admission should appear in the abstract, not buried on page 16. Currently the abstract implies the framework reduces fine-tuning.

### P1A-M13 (Table I and abstract): "Class-level" qualification weakens claim
Table I, footnote c: *"Class-level: scalar-only w = 0 matter-bounce under Assumption (f) of the companion forecast [2]; not fully mechanism-independent across the bouncing-cosmology landscape; not a distinctive ECH prediction."* Then Table I row says "Yes, class-level" for the testable prediction. **Fix:** This should be "No" — the prediction is not from ECH.

### P1A-M14 (§XV.2, p. 20): LiteBIRD significance arithmetic
*"detects non-zero β at ∼ 9σ (a 0.27°/0.03° overall sensitivity number)."* Then: differential test gives 0.73σ. Then: *"the ∼ 9σ test will not by itself separate the spectator-ALP class from generic-ALP fits."* Self-contradictory; the 9σ number is meaningless because the relevant null hypothesis is not β=0. **Fix:** Drop the 9σ claim entirely.

### P1A-M15 (§XV "Forward"): References future papers as program continuation
This violates PRD's standard that a paper's value should not depend on future work by the same author. **Fix:** Remove forward-reference to future companion papers.

### P1A-M16 (§II.A.2, p. 5): Definition of M
*"M = Marea-gap ∼ MPl/√γ is the LQG area-gap mass scale (from the LQG area-gap ∆ ∝ γ ℓ²P, the inverse-length / mass scale is M∆ ∼ MPl/√γ up to numerical constants)"*. With γ ≈ 0.274, √γ ≈ 0.52, so M ∼ MPl/0.52 ≈ 2 MPl. Then α/M ∼ 10⁻²¹ GeV⁻¹ implies α ∼ 10⁻² (with MPl ∼ 10¹⁹ GeV). The paper later quotes "(α/M) MPl ∼ 10⁻²". Self-consistent? Yes if α ∼ 10⁻². But the paper does not state α separately and ambiguates throughout. **Fix:** Quote α directly, not just α/M.

---

## MINOR findings

### P1A-N1 (Abstract): Excessive scope caveats
The abstract contains 4 explicit scope-limiting paragraphs ("This is a channel-level assessment, not an operator-level theorem"; "we acknowledge missing operators... explicitly"; "we treat this scaling explicitly as an ansatz, not a derivation"; "The role of this paper is the channel-level closure..."). After these, what is actually claimed? The abstract is structured to insulate the paper from criticism rather than communicate results.

### P1A-N2 (Abstract): Footnote `a` is content-bearing
Footnote `a` in the abstract corrects a mathematical statement: "This Bianchi-identity vanishing is distinct from... the Pontryagin density..." This should be in the body, not in an abstract footnote.

### P1A-N3 (Throughout): Em-dashes and parentheticals indicate poor editing
Numerous sentences contain 3+ nested parentheticals or em-dash interruptions, e.g., the abstract's *"a contracting-phase quantity mode with kSPHEREx ∼ 10⁻¹ h/Mpc is pushed to kphysbounce ∼ kphysSPHEREx eNtot−Nexit ∼ e³² kphysSPHEREx at Ntot ∼ 92, Nexit ∼ 60 (the relative e-fold differential between bounce and CMB horizon-exit; comoving wavenumbers k are constant by definition and only physical scales scale with a⁻¹ ∝ e⁻ᴺ)"* — this is unparseable.

### P1A-N4 (§I, p. 3): "Through 7 foundation studies (Foundations A–G) and 6 observational research branches (Branches H, J, L, M, N, O)"
The lettering "H, J, L, M, N, O" skips I and K with no explanation. **Fix:** Renumber or explain the gaps.

### P1A-N5 (§V, p. 11): Section title is "Data Methods: Galaxy Spin Analysis" but contains no data
The section contains 4 sentences, all of which delegate to [23]. This is not a section; it is a citation.

### P1A-N6 (§VI, p. 11): "Systematic Analysis" is one paragraph
With no actual systematic analysis. Delegates to [6] and [2].

### P1A-N7 (Table IV, p. 21): "Prior" column inconsistencies
γ prior is "Fixed: 0.274" then "Verified Value" is "0.274 (scheme range ∼0.020)" — but the body identifies the scheme range as 0.127–0.2375–0.274, much wider than 0.020. **Fix:** Reconcile.

### P1A-N8 (Table IV): "MCMC posterior values are from companion Paper I(b)"
None of these values can be independently verified.

### P1A-N9 (Acknowledgments, p. 20): AI assistant disclosure
*"The author acknowledges the use of Claude (Anthropic) as an AI research assistant during systematic barrier-cataloging, perturbation-gate verification, and manuscript preparation."* This is appropriately disclosed but raises concern given the elementary nature of the "perturbation-gate" result and the extensive hedging language characteristic of LLM output.

### P1A-N10 (§I.A, p. 3): "14 mechanism-class structural constraints"
Subsequently the paper says 13 logically independent constraints with B8 subsumed. The abstract and body alternate between 13 and 14. **Fix:** Pick one number and use consistently.

### P1A-N11 (References [2], [6], [23], [46]): Self-citation density
4 of 47 references are to the same author's unpublished work. **Fix:** Either post these papers or remove citations to them.

### P1A-N12 (§IV.D, p. 11): "this overshoot conclusion is conditional on the one-loop estimate... being rigidly bounded"
Lengthy parenthetical admitting the conclusion can be evaded by treating α/M as free. **Fix:** State the conditional cleanly.

### P1A-N13 (§X.B, step 4, p. 15): Phrasing "No equations of motion. A total derivative contributes nothing to variational equations at all orders."
But the paper has just argued in step 4 that the Holst term *vanishes identically* (not that it is a total derivative). Step 5 is then irrelevant. **Fix:** Remove step 5 — the term vanishes; total-derivative argument is unneeded.

### P1A-N14 (§XII.B, p. 17): "All four routes either... yield clean negative results"
"Clean negative results" overstates a no-go that the author admits is dimensionally broken (E3), depends on operators not derived in references (M9), uses incorrect RG equations (E13), and is reframed as a naturalness objection (E5).

### P1A-N15 (Fig. 1, p. 4): "Bounce-mechanism → observable-prediction map"
The figure is qualitative and decorative. Lines and boxes have no quantitative content. **Fix:** Replace with quantitative content or remove.

### P1A-N16 (Fig. 4, p. 18): "Detection Significance Forecast"
Y-axis is "Detection Significance (σ)", x-axis is "Year." Lines for "CMB E-B", "Galaxy Spins", "Combined" — but the paper has just stated galaxy spins are null at >100 orders of magnitude underprediction. Plotting them as rising-significance forecast is misleading. **Fix:** Remove galaxy spins curve or relabel.

### P1A-N17 (§VIII): "No prior work assembles these into a single quantitative framework"
This is a novelty claim. Given the paper's own admissions that the framework is phenomenological, dimensionally broken, and reproduces ΛCDM, what is the "quantitative framework" exactly? **Fix:** Drop the claim.

### P1A-N18 (§I.A): "Our framework collects well-established theoretical components and tests them as a channel-level amplitude closure"
"Collects" + "tests" + "channel-level amplitude closure" — verb-noun chain is opaque. **Fix:** Plain English.

### P1A-N19 (Throughout): Use of "we" by single author
Conventional but worth noting.

### P1A-N20 (§II.C, p. 6): "CMB isotropy bounds give (ω/H)0 < 5 × 10⁻¹¹ [21]"
Saadeh et al. 2016 quote anisotropy bounds; "(ω/H)0 < 5 × 10⁻¹¹" should be checked against the cited paper's actual constraint.

### P1A-N21 (§II.A.2): "the apparent uncertainty range is scheme dependence rather than a statistical or theoretical error"
This is correct but should not be presented as an "uncertainty" at all. The three values are three different theoretical predictions; there is no statistical interpretation. **Fix:** Present as three competing theoretical values, not as a "range."

---

## Length recommendation

For its actual content (one trivial theorem, four phenomenological no-go arguments with admitted dimensional problems, and pointers to companion papers), this manuscript should be **at most 8 pages** in PRD format. 22 pages is unjustifiable. The bloat consists of repeated scope caveats, hedging paragraphs, internal-bookkeeping discussion, and structural-tension repetition.

---

## Summary recommendation

**REJECT**

The paper presents a trivial result (Holst term vanishes when torsion vanishes — a one-line consequence of Hehl 1976 and the algebraic Bianchi identity) inflated into a "central theorem"; its dark-energy "closure" rests on (i) an operator the paper itself admits is dimensionally broken by three powers of mass, (ii) an RG equation the paper admits is not the correct β-function, (iii) a one-loop operator no published reference contains, and (iv) a "naturalness" closure that reduces to the cosmological constant problem the framework is supposed to address. Four of the 47 references are unavailable companion papers by the same author that carry the load-bearing observational claims (MCMC, Fisher forecasts, galaxy chirality, PTA analysis). The abstract advertises "surviving predictions" that the body explicitly disclaims as not ECH predictions. The paper contains internal version-history language ("earlier versions of this manuscript erroneously identified..."), in-progress MCMC entries that have not converged, and a figure caption that does not describe the figure. The author's own admission "this is bookkeeping, not progress" appears on page 16. None of these problems can be fixed by revision; the paper would need to be rewritten around its actual content — namely, a few pages of straightforward observations about the Holst sector for scalar matter — and the dark-energy framework abandoned or rederived with dimensionally consistent operators.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report (continued): Additional Findings from Targeted Re-examination

After applying the targeted checklist (A–J), I identify the following additional findings not in my initial review. The new findings include several substantive **ESSENTIAL** issues (particularly misattribution of the central γ value to wrong references, misrepresentation of the basic ECH action, and a stale figure value), several **MAJOR** arithmetic inconsistencies, and a few minor items.

---

## ESSENTIAL findings (additional)

### P1A-E15 (Eq. (2), p. 5; refs [17,18]): Misattribution of γSU(2) ≈ 0.274
The paper claims γSU(2) ≈ 0.274 "from the refined SU(2) full counting [17, 18]." References [17] (Domagała & Lewandowski) and [18] (Meissner) give γDLM ≈ 0.2375, not 0.274. The paper itself acknowledges this in the same paragraph: *"the further Domaga la–Lewandowski–Meissner refinement gives γDLM ≈ 0.2375."* So γDLM ≠ 0.274. The numerical value 0.274 that anchors the entire dark-energy mapping and the bounce density ρcrit ≈ 0.27 ρPl does not appear in any of the cited LQG black-hole-entropy papers. The standard published SU(2) refined counting value is 0.2375 (ln 3/(π√8)). The author's central value 0.274 is either uncited from a separate paper (e.g., Agullo et al., Ghosh-Mitra, or other refined-counting works) or is an internal modification. **Fix:** Identify the actual literature source of γ = 0.274 with a proper citation, or use the standard published value 0.2375 throughout.

### P1A-E16 (Eq. (1), p. 5): Misrepresentation of the ECH action
Eq. (1) displays the action as containing an explicit "+(1/4) Tabc Tabc" kinetic-style term. The text immediately afterward concedes: *"The Tabc Tabc term in Eq. (1) is a shorthand for the four-fermion contact interaction obtained after integrating out the non-propagating torsion; it is not an independently specified kinetic term."* This is a misrepresentation of the standard Einstein-Cartan-Holst action. The minimal ECH action contains only the Holst-extended curvature term; torsion is determined algebraically by the Cartan equation (Eq. 3), and the T·T-like structure emerges only AFTER integrating out torsion. By writing T² as if it were part of the fundamental action, the paper presents a non-standard (and confusing) form of the ECH action as if it were canonical. **Fix:** Display the genuine ECH action without the T² term, and present the four-fermion contact interaction as a derived consequence of torsion elimination, as is standard.

### P1A-E17 (§IV.B and Eq. 15, p. 9): Internal inconsistency in Route 2 closure
The detailed calculation following Eq. (15) gives ∆θone-loop/∆θobs ∼ 10⁻⁵⁸ to 10⁻⁶⁰. However, recomputation of the chain shown gives:
- numerator: 10⁻³ · 10⁻⁶¹ = 10⁻⁶⁴
- denominator: 10⁻² · 6·10⁻³ = 6·10⁻⁵
- ratio: ≈ 1.7·10⁻⁶⁰

So the derived value is single-valued at ≈ 10⁻⁶⁰; the upper bound 10⁻⁵⁸ is not produced by the calculation shown. The paper claims a "factor-of-∼100 ambiguity reflects ε-correction perturbative-order scaling alone" without showing this ε-correction. **Then** the paper says: *"Route 2 lies below the observed birefringence amplitude by ≳ 30 orders of magnitude survives any reasonable dimensional reconciliation."* So we have three different closure depths (30, 58, 60 orders) in adjacent paragraphs. **Fix:** Reconcile the three numbers or commit to one with explicit derivation.

---

## MAJOR findings (additional)

### P1A-M17 (§II.A.2, p. 6; §III.A, p. 8; §IV.D, p. 10; §XII.B, p. 17): WMAP+Planck vs ACT DR6 consistency miscomputed
The paper repeatedly states: *"ACT DR6 follow-up... β = 0.215° ± 0.074°... consistent within ∼1.4σ."* Direct calculation:
- ∆β = 0.342 - 0.215 = 0.127°
- σ_combined = √(0.094² + 0.074²) = √(0.00884 + 0.00548) = √0.01432 = 0.120°
- ∆β/σ = 0.127°/0.120° = **1.06σ**, not 1.4σ.

The 1.4σ figure does not match the quoted central values and uncertainties. **Fix:** Recompute using the standard quadrature-sum and report the correct value.

### P1A-M18 (Fig. 1, p. 4; vs. §X.G, p. 16; Table IV, p. 21): Stale PTA value in figure
Fig. 1 contains an annotation: *"PTA γ = 3.0 vs data 3.20 ± 0.42 (P3 §6)"*. But §X.G of this same paper states: *"NANOGrav model comparison: γ = 2.567 ± 0.382 from real-KDE re-analysis... This figure supersedes the earlier synthetic-Gaussian-likelihood value γ = 3.20 ± 0.42 used in pre-real-KDE drafts."* Table IV likewise uses 2.567 ± 0.382 with "+1.1σ" deviation. Therefore Fig. 1 retains a stale annotation that the body of the paper explicitly supersedes. **Fix:** Update Fig. 1 to the current PTA value.

### P1A-M19 (Table IV, p. 21): "Scheme range ∼0.020" not matched by any prescription spread
Table IV cites γ as "0.274 (scheme range ∼0.020)". The body (§II.A.1) explicitly enumerates the three competing values: γU(1) = 0.127, γSU(2) = 0.274, γDLM = 0.2375. The spread between any pair:
- 0.274 − 0.127 = 0.147
- 0.274 − 0.2375 = 0.0365
- 0.2375 − 0.127 = 0.1105

None of these is 0.020. The footnote in §II.A.1 admits *"the ∼0.020 figure... is the spread between counting prescriptions"* — but the spread between prescriptions, as enumerated by the author himself, is at minimum 0.037 and as large as 0.147. The 0.020 figure has no justification. **Fix:** Use one of the actual spread values, or remove the spurious 0.020 figure.

### P1A-M20 (Table I, p. 4; Table IV, p. 21): H0 value doesn't match Planck 2018 reference
Both tables list H0 = 67.68 ± 1.06 as "MCMC verified" or "MCMC proxy from companion". The Planck 2018 baseline (ref [7]) reports H0 = 67.36 ± 0.54 (Planck+lowE+lensing) or 67.27 ± 0.60. The reported central value is ~0.3 km/s/Mpc higher than Planck 2018 and the uncertainty is ~2× larger. The paper does not explain the deviation from its own cited Planck reference. If the value comes from companion Paper I(b) and reflects the inclusion of ∆Neff, the broadening makes sense, but no derivation is shown. **Fix:** Either source the value from the actual Planck reference, or explain the offset and broadening explicitly.

### P1A-M21 (Eq. (16), §IV.C, p. 10): Stated chiral-running estimate inconsistent with stated formula
Eq. (16): dγ/dlnμ = γ(N^L_F − N^R_F)/(12π²). The paper claims *"In the Standard Model, the chiral asymmetry is generated by the SU(2)L doublets; numerically, ∆γ/γ ∼ 10⁻² over the running from the GUT scale to the IR."*

Computing: SM has (N^L − N^R) ≈ 3 per generation (counting Weyl spinors: ~8 LH − ~7 RH per gen; precise count depends on convention). With ∆lnμ ≈ ln(10^16 GeV / 10^-3 eV) = ln(10^28) ≈ 64:
- ∆γ/γ = 3·64/(12π²) ≈ 192/118 ≈ 1.6 — **not 10⁻²**.

The 10⁻² estimate is off by ~two orders of magnitude. The downstream Route-3 closure ratio "(∆γ/γ)·(H/MPl) ∼ 10⁻⁶³" would change to ~10⁻⁶¹ but the qualitative closure survives. The arithmetic is nonetheless wrong by ×100. **Fix:** Use the running consistent with Eq. (16), or use a different RG estimate with cited justification.

### P1A-M22 (Eq. (10), p. 6): Mass-dimension labeling in central equation
Eq. (10) writes "Λeff = Ξ M²Pl + cω ω²" where Λeff is labeled "effective cosmological constant". In the body the cosmological constant is sometimes treated as ρΛ (mass dim 4) and sometimes as Λ (mass dim 2). Eq. (10) uses the curvature-dimension convention (Λ ~ mass²) consistent with M²Pl · Ξ, but the surrounding discussion conflates Λeff with ρΛ ~ Ξ M⁴Pl. The two are related by Λeff = (8π/3) ρΛ/M²Pl, but the paper uses them interchangeably. **Fix:** Use one convention consistently.

### P1A-M23 (§II.C.1, pp. 6-7): Unjustified "cube of bilinear" argument
The paragraph defending the a⁻³ dilution states: *"the cube of the fermion bilinear scales as the cube of the fermion number density at the bounce-density regime where the algebraic relation is saturated."* The bilinear ψ̄γψ has mass dimension 3; its cube has dimension 9, not 3 times the number density. The claim that this "scales as the cube of the fermion number density" is dimensionally and physically unclear, and no derivation is shown. The argument supporting the a⁻³ dilution falls back on hand-waving. **Fix:** Provide a rigorous derivation of the dilution scaling at the operator level.

### P1A-M24 (Fig. 4 caption, p. 18 vs. body): Caption claims "≳ 5σ on Stage III/IV timescales"; body says "3–5σ realistic"
Fig. 4 caption states: *"Both forecasts are decisive (≳ 5σ on Stage III/IV survey timescales)."* But Table I footnote b, §VII, §XIII, and §XV all quote the matter-bounce fNL forecast as "3–5σ realistic". The figure caption's "≳ 5σ" is incompatible with the explicit lower bound 3σ stated four times elsewhere. **Fix:** Reconcile the figure caption with the body forecast.

---

## MINOR findings (additional)

### P1A-N4 (§IX.A, p. 12): Hierarchy quoted as 10⁻¹²⁰ not 10⁻¹²²
Eq. (18) implies √|t3| ~ MPl/H0 ~ 10⁶¹, hence |t3| ~ 10¹²², hence δm²T/m²T ~ 10⁻¹²². The paper quotes 10⁻¹²⁰. Minor arithmetic off by factor ~100.

### P1A-N5 (§II.C.1, p. 7): (Treh/MGUT)^(3/2) prefactor estimate range
Paper states the (Treh/MGUT)^(3/2) prefactor is "O(0.01–0.1)" at Treh ~ 10^15 GeV, MGUT ~ 10^16 GeV. Direct computation: (0.1)^(1.5) = 0.0316. So the value sits at the lower endpoint of the stated range, not in the middle. Minor presentation issue.

### P1A-N6 (Table III, p. 17): Asymmetric checkmarks for matter bounce
Table III row "Matter bounce" gives ✓ for fNL and ✓ for PTA γ, but the PTA γ "✓" is followed by Table-internal reference to real-KDE re-analysis. The matter-bounce → PTA γ relationship is much weaker than the matter-bounce → fNL one (the +1.1σ deviation from the posterior mean is consistency, not a positive prediction confirmation). The use of ✓ for both is misleading. Should be ✓ vs. consistent.

### P1A-N7 (Acknowledgments, p. 20): AI assistant disclosure
*"The author acknowledges the use of Claude (Anthropic) as an AI research assistant during systematic barrier-cataloging, perturbation-gate verification, and manuscript preparation."* PRD policy on AI use should be verified; the disclosure is appropriate practice, but if "perturbation-gate verification" includes the mathematical derivation in §X, this is potentially a concern given the manuscript-acknowledged earlier confusion of the Holst dual contraction with the Pontryagin density (a fundamental mathematical error in an earlier version, per footnote `a`).

### P1A-N8 (§II.C, Eq. 10): The cω ω² rotation term
Eq. (10) includes a cω ω² term where ω is the cosmic rotation rate. The paper notes the CMB isotropy bound (ω/H)0 < 5×10⁻¹¹ "making rotation completely negligible." If the term is negligible by 22 orders of magnitude, why is it kept in the central equation? It serves only to advertise the rotating-universe motivation. Minor formal point but suggests the equation is not the working one.

### P1A-N9 (Throughout): The phrase "(in preparation)" appears 10+ times
Refs [2], [6], [23], [46] are each cited multiple times as "in preparation". This pattern in a PRD submission indicates the manuscript is not standalone-publishable.

### P1A-N10 (§XIII (2), p. 18): "0.27° (midpoint)" is undefined
Table IV: β = "0.27° (midpoint)". Midpoint of what range? The WMAP+Planck value 0.342 ± 0.094 has a 1σ range [0.248°, 0.436°], whose midpoint is 0.342°. The 0.27° value cited as the spectator-ALP "benchmark" is *not* the midpoint of anything explicit. **Fix:** Define what "midpoint" means or remove the qualifier.

---

## Summary of Additional Findings

3 new ESSENTIAL items (γ value misattribution; misrepresentation of ECH action; internally inconsistent Route 2 closure depth), 8 new MAJOR items (consistency-σ miscalculation; stale figure annotation; spurious "0.020" scheme spread; H0 deviation from Planck reference unexplained; chiral-running estimate inconsistent with stated formula; mass-dimension confusion in central equation; "cube of bilinear" hand-waving; caption-vs-body forecast mismatch), and 7 minor items.

These reinforce my initial recommendation of **REJECT**. The new findings — particularly the misattribution of the central γ value to references that give a different value (P1A-E15), the misrepresentation of the basic ECH action (P1A-E16), and the stale figure annotation that the body explicitly supersedes (P1A-M18) — indicate that the manuscript has not been carefully cross-checked even at the level of internal consistency between its own sections, much less verified against the references it cites. These are the kinds of errors that would survive into print and require errata.